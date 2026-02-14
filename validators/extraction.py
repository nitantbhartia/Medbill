"""Post-extraction validation for OCR output quality."""

import re
from datetime import datetime, date

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


def validate_extraction(extracted: dict) -> list[str]:
    """
    Validate extracted bill data for common OCR errors.
    Returns a list of issue strings (empty means clean).
    """
    issues = []

    for item in extracted.get("line_items", []):
        desc = item.get("description", "unknown")

        # CPT code format: 5 alphanumeric characters
        cpt = item.get("cpt_code")
        if cpt and not re.match(r"^[0-9A-Z]{5}$", cpt):
            issues.append(f"Invalid CPT format: {cpt} on '{desc}'")

        # CPT code exists in Medicare table
        if cpt and re.match(r"^[0-9A-Z]{5}$", cpt) and not cpt_exists(cpt):
            issues.append(f"Unknown CPT code: {cpt} on '{desc}'")

        # Sanity check amounts
        amount = item.get("charged_amount")
        if amount is not None:
            if amount > MAX_REASONABLE_CHARGE:
                issues.append(f"Suspiciously high charge: ${amount:,.2f} on '{desc}'")
            if amount < 0:
                issues.append(f"Negative charge: ${amount:,.2f} on '{desc}'")

        # Date validation
        dos_str = item.get("date_of_service")
        if dos_str:
            dos = _parse_date(dos_str)
            if dos is None:
                issues.append(f"Unparseable date: {dos_str} on '{desc}'")
            elif dos > date.today():
                issues.append(f"Future date of service: {dos_str} on '{desc}'")
            elif dos < MIN_REASONABLE_DATE:
                issues.append(f"Very old date of service: {dos_str} on '{desc}'")

        # Quantity check
        qty = item.get("quantity")
        if qty is not None and qty < 0:
            issues.append(f"Negative quantity: {qty} on '{desc}'")

    # Cross-check line item total vs stated total
    line_total = sum(item.get("charged_amount") or 0 for item in extracted.get("line_items", []))
    stated_total = extracted.get("total_charged")
    if stated_total and line_total > 0 and abs(line_total - stated_total) > 1.0:
        issues.append(
            f"Line items total (${line_total:,.2f}) doesn't match "
            f"stated total (${stated_total:,.2f})"
        )

    return issues


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
