import json
import base64
import logging

from google import genai
from google.genai import types

import config

log = logging.getLogger(__name__)

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


def _add_confidence_flags(extracted: dict) -> dict:
    """Flag items that need user confirmation."""
    for item in extracted.get("line_items", []):
        item["confidence"] = "high"

        if item.get("cpt_code") is None:
            item["confidence"] = "low"
            item["flag"] = "No procedure code found. Can you find a 5-digit code on this line?"

        if item.get("charged_amount") and item["charged_amount"] > config.HIGH_CHARGE_FLAG:
            item["confidence"] = "medium"
            item["flag"] = "This charge seems very high. Please verify."

        if item.get("quantity") and item["quantity"] > config.HIGH_QUANTITY_FLAG:
            item["confidence"] = "medium"
            item["flag"] = f"Billed for {item['quantity']} units. Is that correct?"

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

    extracted = json.loads(response.text)
    return _add_confidence_flags(extracted)


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

    extracted = json.loads(response.text)
    return _add_confidence_flags(extracted)
