"""The one BillView shape the iOS app renders. A locked view never contains finding text."""

from __future__ import annotations

from fastapi import HTTPException

import config
import mobile_purchases
import report
from analyzer import get_bill_results
from charge_summary import group_findings_by_charge
from db import get_db

HEADER_FIELDS = ("id", "provider_name", "bill_date", "total_charged", "total_patient_owes")


def free_charge(results: dict) -> dict | None:
    """One strongest charge shown free on a locked bill. With a single flagged charge, only its name and reason."""
    bill = results["bill"]
    owed = float(bill.get("total_patient_owes") or bill.get("total_charged") or 0) or None
    charges = group_findings_by_charge(results["findings"], owed)["charges"]
    strong = [c for c in charges if c["strong"]]
    if not strong:
        return None
    # A real billing error makes the best free proof; otherwise the biggest price gap.
    best = max(strong, key=lambda c: (c["error_savings"] > 0, c["error_savings"] or c["savings"]))
    reason = best["reasons"][0]
    if len(charges) == 1:
        return {"code": best["code"], "description": best["description"], "reason_label": reason["label"]}
    return {
        "code": best["code"], "description": best["description"], "date": best["date"],
        "charged": best["charged"], "medicare_rate": best["medicare_rate"], "markup": best["markup"],
        "savings": best["savings"], "severity": best["severity"], "strong": True,
        "reason_label": reason["label"], "reason_message": reason["message"],
    }


def headline(summary: dict | None) -> dict | None:
    """Mobile shows one number: billing errors when there are any, else the price-gap total."""
    if not summary:
        return summary
    return {**summary, "total_savings": summary["headline_amount"]}


def read_check(results: dict) -> str | None:
    """Warn when the scan probably misread the bill: line items that don't add up to the total."""
    total = float(results["bill"].get("total_charged") or 0)
    lines = sum(float(item.get("charged_amount") or 0) for item in results["line_items"])
    if not results["line_items"] or not total or not lines:
        return None
    if abs(lines - total) <= max(total * config.READ_CHECK_TOLERANCE, config.READ_CHECK_MIN_GAP):
        return None
    return f"The charges we read add up to ${lines:,.0f}, but the bill total reads ${total:,.0f}. Retake the photo if that looks wrong."


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
        "teaser": headline(report.teaser(bill_id)),
        "report": None,
        "price": {"report_product_id": mobile_purchases.REPORT_PRODUCTS[0]},
        "extraction_quality": None,
        "free_charge": None if unlocked else free_charge(results),
        "read_warning": read_check(results),
        "line_item_count": len(results["line_items"]),
        "has_line_item_codes": any(item.get("cpt_code") for item in results["line_items"]),
    }
    if unlocked:
        owed = float(bill.get("total_patient_owes") or bill.get("total_charged") or 0) or None
        view["report"] = headline(group_findings_by_charge(results["findings"], owed))
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
        info = headline(report.teaser(row["id"])) or {"charge_count": 0, "total_savings": 0, "headline_kind": "pricing"}
        summaries.append({
            "bill_id": row["id"],
            "provider_name": row["provider_name"],
            "bill_date": row["bill_date"],
            "total_patient_owes": row["total_patient_owes"],
            "charge_count": info["charge_count"],
            "total_savings": info["total_savings"],
            "headline_kind": info["headline_kind"],
            "locked": not report.is_unlocked(row["id"]),
            "created_at": row["created_at"],
        })
    return summaries
