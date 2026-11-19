"""The user confirms or fixes the few lines a scan couldn't read clearly. Every answer is saved as a labelled example."""

from __future__ import annotations

import re

import analyzer
import scan_pipeline
from db import get_db

CODE = re.compile(r"[0-9A-Z]{5}")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
NUMBER_FIELDS = {"charged_amount", "insurance_paid", "insurance_adjustment", "patient_responsibility"}
EDITABLE_FIELDS = NUMBER_FIELDS | {"quantity", "cpt_code", "date_of_service"}


class InvalidConfirmation(ValueError):
    """The request names a line or value we can't accept."""


def _clean(field: str, value):
    if field in NUMBER_FIELDS | {"quantity"}:
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0:
            raise InvalidConfirmation(f"{field} must be a number that is not negative")
        return int(value) if field == "quantity" else float(value)
    pattern = CODE if field == "cpt_code" else DATE
    if not isinstance(value, str) or not pattern.fullmatch(value.strip().upper() if field == "cpt_code" else value.strip()):
        raise InvalidConfirmation(f"{field} is not in the expected format")
    return value.strip().upper() if field == "cpt_code" else value.strip()


def _validated(confirmations: list[dict]) -> list[tuple[int, str, object]]:
    if not isinstance(confirmations, list) or not confirmations:
        raise InvalidConfirmation("Send at least one line to confirm")
    checked = []
    for entry in confirmations:
        index, field = entry.get("line_index"), entry.get("field")
        if not isinstance(index, int) or isinstance(index, bool) or index < 0:
            raise InvalidConfirmation("line_index must be a whole number")
        if field not in EDITABLE_FIELDS:
            raise InvalidConfirmation(f"{field} can't be edited")
        checked.append((index, field, _clean(field, entry.get("value"))))
    return checked


def apply_confirmations(bill_id: int, confirmations: list[dict]) -> None:
    """Save the confirmed values and the corrections, then re-run the analysis on the corrected lines."""
    checked = _validated(confirmations)
    with get_db() as db:
        rows = db.execute("SELECT * FROM line_items WHERE bill_id = ? ORDER BY id", (bill_id,)).fetchall()
        for index, field, value in checked:
            if index >= len(rows) or not rows[index]["needs_confirm"]:
                raise InvalidConfirmation(f"Line {index} isn't waiting for confirmation")
        for index, field, value in checked:
            row = rows[index]
            db.execute(f"UPDATE line_items SET {field} = ?, needs_confirm = 0 WHERE id = ?", (value, row["id"]))
            db.execute(
                "INSERT INTO extraction_corrections (bill_id, line_index, field, extracted_value, confirmed_value, issue_kind) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (bill_id, index, field, str(row[field]), str(value), row["issue_kind"]),
            )
    bill, extracted = scan_pipeline.rebuild_extracted(bill_id)
    analysis = analyzer.analyze_bill(extracted, bill["zip_code"] or "")
    analyzer.replace_findings_and_insurance_fields(bill_id, extracted, analysis)


def record_web_corrections(bill_id: int, original_rows, edited_items: list[dict]) -> None:
    """Corrections made on the web confirm page, compared with what the scan read, line by line."""
    pairs = (("cpt_code", "cpt_code"), ("charged_amount", "billed_amount"), ("quantity", "quantity"))
    with get_db() as db:
        for index, (row, edited) in enumerate(zip(original_rows, edited_items)):
            for stored_field, edited_field in pairs:
                if edited.get(edited_field) is not None and edited[edited_field] != row[stored_field]:
                    db.execute(
                        "INSERT INTO extraction_corrections (bill_id, line_index, field, extracted_value, confirmed_value, issue_kind) "
                        "VALUES (?, ?, ?, ?, ?, ?)",
                        (bill_id, index, stored_field, str(row[stored_field]), str(edited[edited_field]), "web_edit"),
                    )
