import json
import re
import base64
import logging

from google import genai
from google.genai import types

import config

log = logging.getLogger(__name__)


def _parse_json_response(text: str) -> dict:
    """Parse JSON from Gemini, handling common formatting quirks."""
    # Strip markdown code fences
    cleaned = re.sub(r"^```(?:json)?\s*\n?", "", text.strip())
    cleaned = re.sub(r"\n?```\s*$", "", cleaned)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # Remove trailing commas before } or ]
    cleaned = re.sub(r",\s*([}\]])", r"\1", cleaned)
    return json.loads(cleaned)

EXTRACTION_PROMPT = """You are a medical bill parser. Extract every line item from this medical bill image.

For each line item, extract:
- date_of_service: date the service was performed (YYYY-MM-DD)
- cpt_code: the CPT or HCPCS code (5-digit alphanumeric, e.g., "99283", "J0170")
- description: the text description of the service
- quantity: number of units billed (default 1 if not shown)
- charged_amount: the amount billed by the provider
- insurance_paid: amount the insurance company paid (if visible, null otherwise)
- insurance_adjustment: amount written off by insurance (if visible, null otherwise)
- patient_responsibility: amount the patient owes (if visible, null otherwise)

Also extract:
- provider_name: hospital or doctor name
- provider_address: address (for geographic rate comparison)
- patient_name: (will be redacted, extract for verification only)
- bill_date: date the bill was issued
- account_number: (for reference)
- total_charged: total amount billed
- total_patient_owes: total patient responsibility

If a field is not visible or unclear, return null.
If you see multiple pages, process all of them.

IMPORTANT:
- Medical bills format varies widely. Look for tables, grids, or lists of services.
- CPT codes may be labeled as "Procedure Code", "Service Code", "HCPCS", or just a 5-digit code.
- Some bills show only descriptions without codes — still extract those items.
- EOBs (Explanation of Benefits) from insurance have a different layout than hospital bills — handle both.

Return valid JSON only. No markdown, no preamble."""


def _get_client() -> genai.Client:
    return genai.Client(api_key=config.GEMINI_API_KEY)


def _coerce_numeric(value):
    """Safely convert a value to float. Gemini sometimes returns numbers as strings."""
    if value is None:
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def _add_confidence_flags(extracted: dict) -> dict:
    """Normalize numeric fields and flag items that need user confirmation."""
    for item in extracted.get("line_items", []):
        # Normalize numeric fields that Gemini may return as strings
        for field in ("charged_amount", "insurance_paid", "insurance_adjustment",
                      "patient_responsibility"):
            item[field] = _coerce_numeric(item.get(field))
        qty = _coerce_numeric(item.get("quantity"))
        item["quantity"] = int(qty) if qty else 1

        item["confidence"] = "high"

        if item.get("cpt_code") is None:
            item["confidence"] = "low"
            item["flag"] = "No procedure code found. Can you find a 5-digit code on this line?"

        if item["charged_amount"] and item["charged_amount"] > config.HIGH_CHARGE_FLAG:
            item["confidence"] = "medium"
            item["flag"] = "This charge seems very high. Please verify."

        if item["quantity"] > config.HIGH_QUANTITY_FLAG:
            item["confidence"] = "medium"
            item["flag"] = f"Billed for {item['quantity']} units. Is that correct?"

    # Normalize bill-level totals
    extracted["total_charged"] = _coerce_numeric(extracted.get("total_charged"))
    extracted["total_patient_owes"] = _coerce_numeric(extracted.get("total_patient_owes"))

    return extracted


def process_bill_image(image_bytes: bytes, mime_type: str = "image/jpeg") -> dict:
    """
    Send a single bill image to Gemini Flash Vision.
    Returns extracted data with confidence flags.
    """
    client = _get_client()

    image_part = types.Part.from_bytes(data=image_bytes, mime_type=mime_type)

    response = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=[image_part, EXTRACTION_PROMPT],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        ),
    )

    extracted = _parse_json_response(response.text)
    return _add_confidence_flags(extracted)


def process_bill_with_verification(image_bytes: bytes, mime_type: str = "image/jpeg") -> dict:
    """
    For high-value bills (>$5k), run extraction twice with different prompts
    and compare results. Flags discrepancies for user review.
    """
    extracted_1 = process_bill_image(image_bytes, mime_type)

    total = extracted_1.get("total_charged") or 0
    if total < config.DOUBLE_EXTRACTION_THRESHOLD:
        return extracted_1

    # Second extraction with a differently-phrased prompt
    client = _get_client()
    verification_prompt = (
        "Extract all billing line items from this medical bill. "
        "For each: cpt_code, description, charged_amount, quantity, date_of_service. "
        "Also extract: total_charged, provider_name. Return JSON only."
    )
    image_part = types.Part.from_bytes(data=image_bytes, mime_type=mime_type)
    response = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=[image_part, verification_prompt],
        config=types.GenerateContentConfig(response_mime_type="application/json"),
    )
    extracted_2 = _parse_json_response(response.text)

    # Compare line item counts
    count_1 = len(extracted_1.get("line_items", []))
    count_2 = len(extracted_2.get("line_items", []))
    if count_1 != count_2:
        extracted_1["_verification_warning"] = (
            f"Double-extraction found {count_1} vs {count_2} line items. "
            "Please review carefully."
        )

    # Compare totals
    total_2 = extracted_2.get("total_charged") or 0
    if total and total_2 and abs(total - total_2) > 1:
        existing = extracted_1.get("_verification_warning", "")
        extracted_1["_verification_warning"] = (
            existing + f" Totals differ: ${total:,.2f} vs ${total_2:,.2f}."
        ).strip()

    # Compare individual line item amounts
    items_1 = extracted_1.get("line_items", [])
    items_2 = extracted_2.get("line_items", [])
    for i, item in enumerate(items_1):
        if i < len(items_2):
            amt_1 = item.get("charged_amount") or 0
            amt_2 = items_2[i].get("charged_amount") or 0
            if amt_1 and amt_2 and abs(amt_1 - amt_2) > 1:
                item["confidence"] = "medium"
                item["flag"] = (
                    f"Verification found different amount (${amt_2:,.2f}). Please check."
                )

    return extracted_1


def process_multi_page_bill(images: list[tuple[bytes, str]]) -> dict:
    """
    Process multi-page bills by sending all images in one request.
    Each item in images is (image_bytes, mime_type).
    """
    client = _get_client()

    contents = []
    for i, (img_bytes, mime_type) in enumerate(images):
        contents.append(f"Page {i + 1} of {len(images)}:")
        contents.append(types.Part.from_bytes(data=img_bytes, mime_type=mime_type))

    multi_page_prompt = (
        EXTRACTION_PROMPT
        + "\nThis is a multi-page bill. Combine all line items from all pages "
        "into one list. Do not duplicate items that appear on a summary page "
        "and a detail page."
    )
    contents.append(multi_page_prompt)

    response = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=contents,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        ),
    )

    extracted = _parse_json_response(response.text)
    return _add_confidence_flags(extracted)
