"""Post-extraction validation for OCR output quality."""

import re
from datetime import datetime, date

import config
from db import get_db

MAX_REASONABLE_CHARGE = 500000
MIN_REASONABLE_DATE = date(2020, 1, 1)


def cpt_exists(cpt_code: str) -> bool:
    """Check if a CPT code exists in the Medicare rates table."""
    with get_db() as db:
        row = db.execute(
            "SELECT 1 FROM medicare_rates WHERE cpt_code = ? LIMIT 1", (cpt_code,)
        ).fetchone()
    return row is not None


def _parse_date(date_str: str) -> date | None:
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%m-%d-%Y"):
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None


# Issues the app can ask the user about: a line the scanner probably misread.
LINE_ISSUE_KINDS = {"invalid_code", "unknown_code", "negative_amount", "line_math", "payer_math"}


def _issue(line_index: int | None, field: str, kind: str, message: str) -> dict:
    return {"line_index": line_index, "field": field, "kind": kind, "message": message}


def line_issues(item: dict, line_index: int) -> list[dict]:
    """Everything wrong with one extracted line."""
    issues = []
    desc = item.get("description", "unknown")
    cpt = item.get("cpt_code")
    if cpt and not re.match(r"^[0-9A-Z]{5}$", cpt):
        issues.append(_issue(line_index, "cpt_code", "invalid_code", f"Invalid CPT format: {cpt} on '{desc}'"))
    elif cpt and not cpt_exists(cpt):
        issues.append(_issue(line_index, "cpt_code", "unknown_code", f"Unknown CPT code: {cpt} on '{desc}'"))

    amount = item.get("charged_amount")
    if amount is not None:
        if amount > MAX_REASONABLE_CHARGE:
            issues.append(_issue(line_index, "charged_amount", "high_amount", f"Suspiciously high charge: ${amount:,.2f} on '{desc}'"))
        if amount < 0:
            issues.append(_issue(line_index, "charged_amount", "negative_amount", f"Negative charge: ${amount:,.2f} on '{desc}'"))

    dos_str = item.get("date_of_service")
    if dos_str:
        dos = _parse_date(dos_str)
        if dos is None:
            issues.append(_issue(line_index, "date_of_service", "bad_date", f"Unparseable date: {dos_str} on '{desc}'"))
        elif dos > date.today():
            issues.append(_issue(line_index, "date_of_service", "bad_date", f"Future date of service: {dos_str} on '{desc}'"))
        elif dos < MIN_REASONABLE_DATE:
            issues.append(_issue(line_index, "date_of_service", "bad_date", f"Very old date of service: {dos_str} on '{desc}'"))

    qty = item.get("quantity")
    if qty is not None and qty < 0:
        issues.append(_issue(line_index, "quantity", "negative_quantity", f"Negative quantity: {qty} on '{desc}'"))

    unit_price = item.get("unit_price")
    if amount is not None and unit_price is not None and qty:
        if abs(qty * unit_price - amount) > config.OCR_LINE_MATH_TOLERANCE:
            issues.append(_issue(line_index, "charged_amount", "line_math",
                                 f"{qty} x ${unit_price:,.2f} is not ${amount:,.2f} on '{desc}'"))

    parts = [item.get(name) for name in ("insurance_paid", "insurance_adjustment", "patient_responsibility")]
    if amount is not None and None not in parts:
        if abs(amount - sum(parts)) > config.OCR_LINE_MATH_TOLERANCE:
            issues.append(_issue(line_index, "patient_responsibility", "payer_math",
                                 f"Billed, insurance paid, adjustment and patient share don't add up on '{desc}'"))
    return issues


def find_extraction_issues(extracted: dict) -> list[dict]:
    """Structured issues: {line_index, field, kind, message}. line_index is None for the whole bill."""
    items = extracted.get("line_items", [])
    issues = [issue for index, item in enumerate(items) for issue in line_issues(item, index)]
    line_total = sum(item.get("charged_amount") or 0 for item in items)
    stated_total = extracted.get("total_charged")
    if stated_total and line_total > 0 and abs(line_total - stated_total) > 1.0:
        issues.append(_issue(None, "total_charged", "line_sum",
                             f"Line items total (${line_total:,.2f}) doesn't match stated total (${stated_total:,.2f})"))
    return issues


def validate_extraction(extracted: dict) -> list[str]:
    """The issue messages, for callers that only show warnings."""
    return [issue["message"] for issue in find_extraction_issues(extracted)]


def validate_cpt_description(cpt_code: str, bill_description: str) -> bool:
    """
    Cross-check that a CPT code's Medicare description roughly matches
    the description on the bill. Returns True if they seem compatible.
    """
    if not cpt_code or not bill_description:
        return True  # can't validate, assume ok

    with get_db() as db:
        row = db.execute(
            "SELECT description FROM medicare_rates WHERE cpt_code = ? LIMIT 1",
            (cpt_code,),
        ).fetchone()

    if not row or not row["description"]:
        return True  # no reference description available

    # Simple word overlap check
    ref_words = set(row["description"].lower().split())
    bill_words = set(bill_description.lower().split())

    # Remove common filler words
    filler = {"the", "a", "an", "of", "and", "or", "with", "without", "for", "in", "to"}
    ref_words -= filler
    bill_words -= filler

    if not ref_words:
        return True

    overlap = len(ref_words & bill_words) / len(ref_words)
    return overlap >= 0.2  # at least 20% word overlap
