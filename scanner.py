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
        data = json.loads(cleaned)
    except json.JSONDecodeError:
        # Remove trailing commas before } or ]
        cleaned = re.sub(r",\s*([}\]])", r"\1", cleaned)
        data = json.loads(cleaned)

    return _normalize_structure(data)


def _normalize_structure(data) -> dict:
    """Ensure Gemini response has the expected {line_items: [...]} shape."""
    # Gemini returned a bare list — wrap it
    if isinstance(data, list):
        return {"line_items": data}

    if not isinstance(data, dict):
        return {"line_items": []}

    # line_items is a single object instead of a list
    items = data.get("line_items")
    if isinstance(items, dict):
        data["line_items"] = [items]
    elif not isinstance(items, list):
        data["line_items"] = []

    return data

EXTRACTION_PROMPT = """You are a medical bill parser. Extract EVERY line item from this medical bill image.

Return a JSON object with this exact structure:
{
  "provider_name": "Hospital or doctor name",
  "provider_address": "Full address",
  "patient_name": "Patient name (will be redacted)",
  "bill_date": "YYYY-MM-DD",
  "account_number": "Account or invoice number",
  "total_charged": 1234.56,
  "total_patient_owes": 567.89,
  "line_items": [
    {
      "date_of_service": "YYYY-MM-DD",
      "cpt_code": "99283",
      "description": "Service description",
      "quantity": 1,
      "charged_amount": 500.00,
      "insurance_paid": 300.00,
      "insurance_adjustment": 100.00,
      "patient_responsibility": 100.00
    }
  ]
}

CRITICAL RULES:
- The "line_items" field MUST be an array containing ALL line items from the bill.
- Extract EVERY service line, even if there are 20+. Do not summarize or skip any.
- If a field is not visible or unclear, use null.
- CPT codes may be labeled "Procedure Code", "Service Code", "HCPCS", or just a 5-digit code.
- Some bills show only descriptions without codes — still extract those items.
- EOBs (Explanation of Benefits) have a different layout than hospital bills — handle both.
- Medical bills format varies widely. Look for tables, grids, or lists of services.

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
