"""Compare what the bill asks for with what the patient's insurance statement (EOB) says they owe."""

from __future__ import annotations

import config
from db import get_db


def _eob_owed(eob_data: dict) -> float | None:
    if eob_data.get("total_patient_owes") is not None:
        return float(eob_data["total_patient_owes"])
    shares = [float(item["patient_responsibility"]) for item in eob_data.get("line_items") or []
              if item.get("patient_responsibility") is not None]
    return sum(shares) if shares else None


def record(bill_id: int, eob_data: dict, bill_owed: float | None) -> None:
    """Store the result on the bill. No status when the bill has no owed amount to compare."""
    owed = _eob_owed(eob_data)
    if owed is None:
        status = "unreadable"
    elif bill_owed is None:
        status = None
    else:
        status = "mismatch" if bill_owed - owed > config.EOB_MATCH_TOLERANCE_DOLLARS else "match"
    with get_db() as db:
        db.execute("UPDATE bills SET eob_patient_owes = ?, eob_date = ?, eob_status = ? WHERE id = ?",
                   (owed, eob_data.get("bill_date"), status, bill_id))


def view(bill: dict) -> dict | None:
    """The insurance_check object for BillView: null, match, mismatch or unreadable."""
    status = bill.get("eob_status")
    if not status:
        return None
    if status != "mismatch":
        return {"status": status}
    bill_owed = float(bill.get("total_patient_owes") or 0)
    eob_owed = float(bill["eob_patient_owes"])
    return {"status": "mismatch", "eob_owed": eob_owed, "bill_owed": bill_owed,
            "difference": round(bill_owed - eob_owed, 2), "eob_date": bill.get("eob_date")}
