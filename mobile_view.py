"""The one BillView shape the iOS app renders. A locked view never contains finding text."""

from __future__ import annotations

from fastapi import HTTPException

import mobile_purchases
import report
from analyzer import get_bill_results
from charge_summary import group_findings_by_charge
from db import get_db

HEADER_FIELDS = ("id", "provider_name", "bill_date", "total_charged", "total_patient_owes")


def build_bill_view(bill_id: int, device_id: str) -> dict:
    results = get_bill_results(bill_id)
    if not results:
        raise HTTPException(404, "Bill not found")
    if not report.is_unlocked(bill_id):
        mobile_purchases.unlock_with_plus(device_id, bill_id)
    unlocked = report.is_unlocked(bill_id)
    bill = results["bill"]
    view = {
        "bill_id": bill_id,
        "locked": not unlocked,
        "bill": {field: bill.get(field) for field in HEADER_FIELDS},
        "teaser": report.teaser(bill_id),
        "report": None,
        "price": {"report_product_id": mobile_purchases.REPORT_PRODUCTS[0]},
        "extraction_quality": None,
    }
    if unlocked:
        owed = float(bill.get("total_patient_owes") or bill.get("total_charged") or 0) or None
        view["report"] = group_findings_by_charge(results["findings"], owed)
    return view


def list_bill_summaries(device_id: str) -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            "SELECT b.id, b.provider_name, b.bill_date, b.total_patient_owes, b.created_at "
            "FROM bills b JOIN bill_access_sessions bas ON bas.bill_id = b.id "
            "WHERE bas.session_id = ? ORDER BY b.created_at DESC, b.id DESC LIMIT 100",
            (device_id,),
        ).fetchall()
    summaries = []
    for row in rows:
        info = report.teaser(row["id"]) or {"charge_count": 0, "total_savings": 0}
        summaries.append({
            "bill_id": row["id"],
            "provider_name": row["provider_name"],
            "bill_date": row["bill_date"],
            "total_patient_owes": row["total_patient_owes"],
            "charge_count": info["charge_count"],
            "total_savings": info["total_savings"],
            "locked": not report.is_unlocked(row["id"]),
            "created_at": row["created_at"],
        })
    return summaries
