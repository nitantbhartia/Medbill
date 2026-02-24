import json
import re
import base64
import logging
from io import BytesIO

from google import genai
from google.genai import types

import config

log = logging.getLogger(__name__)

try:
    from PIL import Image, ImageFilter, ImageOps
except ImportError:  # pragma: no cover - optional dependency fallback
    Image = None
    ImageFilter = None
    ImageOps = None


def _parse_json_response(text: str) -> dict:
    """Parse JSON from Gemini, handling common formatting quirks."""
    # Strip markdown code fences
    cleaned = re.sub(r"^```(?:json)?\s*\n?", "", text.strip())
    cleaned = re.sub(r"\n?```\s*$", "", cleaned)

    try:
        data = json.loads(cleaned)
        return _normalize_structure(data)
    except json.JSONDecodeError:
        pass

    # Remove trailing commas before } or ] and retry
    try:
        cleaned = re.sub(r",\s*([}\]])", r"\1", cleaned)
        data = json.loads(cleaned)
        return _normalize_structure(data)
    except json.JSONDecodeError as e:
        log.error("Failed to parse Gemini JSON response after cleanup: %s. Raw text: %.200s", e, text)
        raise ValueError(f"Gemini returned unparseable JSON: {e}") from e


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
- For total_patient_owes, look for labels including: "Outstanding balance", "Amount due", "Remaining responsibility", "Patient responsibility", "You owe", "Balance due".
- CPT codes may be labeled "Procedure Code", "Service Code", "HCPCS", or just a 5-digit code.
- Some bills show only descriptions without codes — still extract those items.
- EOBs (Explanation of Benefits) have a different layout than hospital bills — handle both.
- For insurer portal/EOB layouts, do NOT confuse total_charged with total_patient_owes. If both are present, extract both.
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
    for idx, item in enumerate(extracted.get("line_items", [])):
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

        # Best-effort source anchor for explainability UX.
        snippet_parts = []
        if item.get("cpt_code"):
            snippet_parts.append(str(item.get("cpt_code")))
        if item.get("description"):
            snippet_parts.append(str(item.get("description")))
        if item.get("charged_amount") is not None:
            snippet_parts.append(f"${item.get('charged_amount')}")
        item["source_anchor"] = {
            "line_index": idx + 1,
            "snippet": " | ".join(snippet_parts)[:180],
        }

    # Normalize bill-level totals
    extracted["total_charged"] = _coerce_numeric(extracted.get("total_charged"))
    extracted["total_patient_owes"] = _coerce_numeric(extracted.get("total_patient_owes"))

    # Backfill missing patient-owes using line-level insurance breakdowns.
    if not extracted.get("total_patient_owes"):
        line_items = extracted.get("line_items", [])
        line_resp_values = [
            float(item.get("patient_responsibility"))
            for item in line_items
            if item.get("patient_responsibility") is not None
        ]
        if line_resp_values:
            extracted["total_patient_owes"] = round(max(0.0, sum(line_resp_values)), 2)
        elif extracted.get("total_charged"):
            total_charged = float(extracted.get("total_charged") or 0.0)
            insurance_paid = sum(
                float(item.get("insurance_paid") or 0.0)
                for item in line_items
                if item.get("insurance_paid") is not None
            )
            insurance_adj = sum(
                float(item.get("insurance_adjustment") or 0.0)
                for item in line_items
                if item.get("insurance_adjustment") is not None
            )
            if insurance_paid or insurance_adj:
                inferred = max(0.0, total_charged - insurance_paid - insurance_adj)
                extracted["total_patient_owes"] = round(min(inferred, total_charged), 2)

    return extracted


def _run_vision_extraction(image_bytes: bytes, mime_type: str, prompt: str) -> dict:
    """Run Gemini vision extraction with a supplied prompt."""
    client = _get_client()
    image_part = types.Part.from_bytes(data=image_bytes, mime_type=mime_type)
    response = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=[image_part, prompt],
        config=types.GenerateContentConfig(response_mime_type="application/json"),
    )
    extracted = _parse_json_response(response.text)
    return _add_confidence_flags(extracted)


def _serialize_image(image_obj) -> bytes:
    buf = BytesIO()
    image_obj.save(buf, format="PNG")
    return buf.getvalue()


def _preprocess_variants(image_bytes: bytes, mime_type: str) -> list[tuple[str, bytes, str]]:
    """
    Build OCR-friendly variants.
    Returns (label, bytes, mime_type) tuples and always includes original.
    """
    variants = [("original", image_bytes, mime_type)]
    if not config.OCR_PREPROCESS_ENABLED or Image is None:
        return variants[: max(1, config.OCR_MAX_VARIANTS)]

    try:
        img = Image.open(BytesIO(image_bytes))
        img = ImageOps.exif_transpose(img)
        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")

        gray = ImageOps.grayscale(img)
        high_contrast = ImageOps.autocontrast(gray, cutoff=2)
        variants.append(("gray_autocontrast", _serialize_image(high_contrast), "image/png"))

        if ImageFilter is not None:
            sharp = high_contrast.filter(ImageFilter.UnsharpMask(radius=1.8, percent=180, threshold=2))
            variants.append(("sharpened", _serialize_image(sharp), "image/png"))

        thresholded = high_contrast.point(lambda px: 255 if px > 170 else 0).convert("L")
        variants.append(("thresholded", _serialize_image(thresholded), "image/png"))
    except Exception as exc:
        log.warning("OCR preprocessing skipped due to image error: %s", exc)

    return variants[: max(1, config.OCR_MAX_VARIANTS)]


def _is_valid_cpt(code) -> bool:
    return bool(code and re.fullmatch(r"\d{5}", str(code).strip()))


def _to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _quality_score(extracted: dict) -> tuple[float, dict]:
    """
    Score extraction quality based on completeness + reconciliation.
    Higher score is better.
    """
    items = extracted.get("line_items", [])
    if not isinstance(items, list):
        items = []

    cpt_count = 0
    amount_count = 0
    described_count = 0
    charged_sum = 0.0
    charged_lines = 0
    for item in items:
        if _is_valid_cpt(item.get("cpt_code")):
            cpt_count += 1
        amount = _to_float(item.get("charged_amount"))
        if amount is not None and amount > 0:
            amount_count += 1
            charged_lines += 1
            charged_sum += amount
        if item.get("description") and len(str(item.get("description")).strip()) >= 4:
            described_count += 1

    score = 0.0
    score += min(len(items), 25) * config.OCR_SCORE_PER_LINE_ITEM
    score += cpt_count * config.OCR_SCORE_PER_CPT
    score += amount_count * config.OCR_SCORE_PER_AMOUNT
    score += described_count * config.OCR_SCORE_PER_DESCRIPTION

    if extracted.get("provider_name"):
        score += config.OCR_SCORE_PROVIDER_NAME
    if _to_float(extracted.get("total_charged")) is not None:
        score += config.OCR_SCORE_TOTAL_CHARGED
    if _to_float(extracted.get("total_patient_owes")) is not None:
        score += config.OCR_SCORE_TOTAL_PATIENT_OWES

    recon_delta = None
    recon_pct = None
    total = _to_float(extracted.get("total_charged"))
    if total and charged_lines:
        recon_delta = charged_sum - total
        recon_pct = abs(recon_delta) / total * 100.0 if total else None
        if recon_pct is not None and recon_pct > config.OCR_RECONCILIATION_TOLERANCE_PCT:
            score -= min(config.OCR_SCORE_MAX_RECON_PENALTY, recon_pct * config.OCR_SCORE_RECON_PENALTY_MULTIPLIER)

    meta = {
        "line_items": len(items),
        "cpt_count": cpt_count,
        "amount_count": amount_count,
        "described_count": described_count,
        "charged_sum": round(charged_sum, 2),
        "reconciliation_delta": round(recon_delta, 2) if recon_delta is not None else None,
        "reconciliation_pct": round(recon_pct, 2) if recon_pct is not None else None,
    }
    return score, meta


def _merge_candidate(best: dict, fallback: dict) -> dict:
    """Fill missing fields in best extraction from fallback extraction."""
    merged = dict(best)
    for key in ("provider_name", "provider_address", "bill_date", "account_number", "total_charged", "total_patient_owes"):
        if merged.get(key) in (None, "", 0) and fallback.get(key) not in (None, "", 0):
            merged[key] = fallback.get(key)

    best_items = list(merged.get("line_items", []))
    alt_items = list(fallback.get("line_items", []))
    for idx, item in enumerate(best_items):
        if idx >= len(alt_items):
            break
        alt = alt_items[idx]
        if item.get("cpt_code") in (None, "") and alt.get("cpt_code"):
            item["cpt_code"] = alt.get("cpt_code")
        if item.get("description") in (None, "") and alt.get("description"):
            item["description"] = alt.get("description")
        if item.get("charged_amount") in (None, 0) and _to_float(alt.get("charged_amount")) is not None:
            item["charged_amount"] = alt.get("charged_amount")
        if item.get("quantity") in (None, 0) and _to_float(alt.get("quantity")) is not None:
            item["quantity"] = int(float(alt.get("quantity")))
    merged["line_items"] = best_items
    return merged


def _extract_with_ensemble(image_bytes: bytes, mime_type: str) -> dict:
    """
    Run extraction across preprocessed variants and pick/merge best result.
    """
    variants = _preprocess_variants(image_bytes, mime_type)
    candidates = []
    for label, variant_bytes, variant_mime in variants:
        try:
            extracted = _run_vision_extraction(variant_bytes, variant_mime, EXTRACTION_PROMPT)
            score, meta = _quality_score(extracted)
            meta["variant"] = label
            meta["quality_score"] = round(score, 2)
            candidates.append((score, extracted, meta))
        except Exception as exc:
            log.warning("Variant extraction failed for %s: %s", label, exc)

    if not candidates:
        raise RuntimeError("No OCR extraction candidates succeeded")

    candidates.sort(key=lambda tup: tup[0], reverse=True)
    best_score, best_extract, best_meta = candidates[0]
    merged = best_extract
    if len(candidates) > 1:
        merged = _merge_candidate(best_extract, candidates[1][1])

    merged["_extraction_meta"] = {
        "selected_variant": best_meta.get("variant"),
        "quality_score": round(best_score, 2),
        "candidates": [c[2] for c in candidates],
        "ensemble_enabled": True,
    }
    return merged


def process_bill_image(image_bytes: bytes, mime_type: str = "image/jpeg") -> dict:
    """
    Send a single bill image to Gemini Flash Vision.
    Returns extracted data with confidence flags.
    """
    if config.OCR_ENSEMBLE_ENABLED:
        return _extract_with_ensemble(image_bytes, mime_type)
    return _run_vision_extraction(image_bytes, mime_type, EXTRACTION_PROMPT)


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
    verification_prompt = (
        "Extract all billing line items from this medical bill. "
        "For each: cpt_code, description, charged_amount, quantity, date_of_service. "
        "Also extract: total_charged, provider_name. Return JSON only."
    )
    extracted_2 = _run_vision_extraction(image_bytes, mime_type, verification_prompt)

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
    extracted = _add_confidence_flags(extracted)
    score, meta = _quality_score(extracted)
    extracted["_extraction_meta"] = {
        "selected_variant": "multi_page_combined",
        "quality_score": round(score, 2),
        "candidates": [{**meta, "variant": "multi_page_combined", "quality_score": round(score, 2)}],
        "ensemble_enabled": False,
    }
    return extracted
