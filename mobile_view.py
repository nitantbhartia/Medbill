"""The one BillView shape the iOS app renders. A locked view never contains finding text."""

from __future__ import annotations

from fastapi import HTTPException

import config
import insurance_check
import outcome_verification
import mobile_purchases
import json
import report
import report_recheck
from analyzer import get_bill_results
from charge_summary import group_findings_by_charge
from db import get_db

HEADER_FIELDS = ("id", "provider_name", "bill_date", "total_charged", "total_patient_owes", "sent_at")


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
        "reason_label": reason["label"], "reason_message": reason["message"], "basis": reason["basis"],
    }


def locked_kinds(results: dict, free: dict | None) -> list[str]:
    """The evidence kind (official, bill or check) of each charge that stays locked, in display order.
    Reveals no code, description or amount."""
    owed = float(results["bill"].get("total_patient_owes") or results["bill"].get("total_charged") or 0) or None
    charges = group_findings_by_charge(results["findings"], owed)["charges"]
    free_key = (free["code"], free["description"]) if free else None
    kinds = []
    for charge in charges:
        if (charge["code"], charge["description"]) == free_key:
            continue
        basis = charge["reasons"][0]["basis"] if charge["reasons"] else None
        kinds.append(basis["kind"] if basis else "check")
    return kinds


def flagged_bill_keys(device_id: str) -> list[tuple]:
    """Each distinct flagged bill this device has checked, in order. A re-scan of the same bill (same provider, total and
    date) is one check, and a bill with no findings isn't one."""
    with get_db() as db:
        rows = db.execute(
            "SELECT b.provider_name, b.total_charged, b.bill_date FROM bills b "
            "JOIN bill_access_sessions s ON s.bill_id = b.id WHERE s.session_id = ? AND b.total_findings > 0 "
            "ORDER BY b.created_at, b.id", (device_id,)).fetchall()
    keys = []
    for row in rows:
        key = (row["provider_name"], row["total_charged"], row["bill_date"])
        if key not in keys:
            keys.append(key)
    return keys


def free_checks_remaining(device_id: str) -> int:
    return max(config.FREE_CHECKS_LIMIT - len(flagged_bill_keys(device_id)), 0)


def over_free_limit(device_id: str, bill: dict) -> bool:
    """True from the fourth distinct flagged bill on: the scan still runs, but the free preview charge is withheld."""
    keys = flagged_bill_keys(device_id)
    key = (bill.get("provider_name"), bill.get("total_charged"), bill.get("bill_date"))
    return key in keys and keys.index(key) >= config.FREE_CHECKS_LIMIT


def headline(summary: dict | None) -> dict | None:
    """Mobile shows one number: billing errors when there are any, else the price-gap total."""
    if not summary:
        return summary
    shown = {**summary, "total_savings": summary["headline_amount"]}
    if summary.get("info_only"):
        shown.update(total_savings=0, strong_count=0, charges=[], charge_count=0, reason_counts=[],
                     info_note="Prices on this bill are high, but your insurance already reduced them.")
    return shown


CONFIRM_MESSAGES = {
    "line_math": "The quantity and price on this line don't match its amount.",
    "payer_math": "The amounts on this line don't add up.",
    "negative_amount": "This amount reads as negative.",
    "invalid_code": "We couldn't read this billing code.",
    "unknown_code": "We couldn't match this billing code.",
}


def confirm_lines(results: dict) -> list[dict]:
    """The few lines the scan couldn't read clearly, with the value we read, for the user to confirm."""
    lines = []
    for index, item in enumerate(results["line_items"]):
        if not item.get("needs_confirm"):
            continue
        lookup = json.loads(item["issue_choices"]) if item.get("issue_choices") else None
        message = CONFIRM_MESSAGES.get(item["issue_kind"], "We couldn't read this line clearly.")
        if lookup and len(lookup["choices"]) == 1:
            choice = lookup["choices"][0]
            message = f"This looks like {choice['description']} (code {choice['code']}) at {lookup['hospital']}. Right?"
        elif lookup:
            message = f"{lookup['hospital']}'s price list has more than one code for this. Which is it?"
        lines.append({"line_index": index, "code": item.get("cpt_code"), "description": item.get("description"),
                      "date": item.get("date_of_service"), "field": item["issue_field"],
                      "read_value": item.get(item["issue_field"]), "kind": item["issue_kind"],
                      "choices": [c["code"] for c in lookup["choices"]] if lookup else None,
                      "message": message})
    return lines


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
        "price": {"report_product_id": mobile_purchases.REPORT_PRODUCTS[0], "plus_default_min_owed": config.PLUS_DEFAULT_MIN_OWED},
        "extraction_quality": None,
        "free_charge": None if unlocked else free_charge(results),
        "free_checks_remaining": free_checks_remaining(device_id),
        "facility_id": outcome_verification.facility_for(bill),
        "free_limit_reached": False,
        "read_warning": read_check(results),
        "confirm_lines": confirm_lines(results),
        "insurance_check": insurance_check.view(bill),
        "notices": report_recheck.notices_for(bill_id),
        "line_item_count": len(results["line_items"]),
        "has_line_item_codes": any(item.get("cpt_code") for item in results["line_items"]),
    }
    if not unlocked and over_free_limit(device_id, bill):
        view["free_charge"], view["free_limit_reached"] = None, True
    if not unlocked and view["teaser"]:
        view["teaser"]["locked_kinds"] = locked_kinds(results, view["free_charge"])
    if unlocked:
        owed = float(bill.get("total_patient_owes") or bill.get("total_charged") or 0) or None
        view["report"] = headline(group_findings_by_charge(results["findings"], owed))
    return view


def list_bill_summaries(device_id: str) -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            "SELECT b.id, b.provider_name, b.bill_date, b.total_patient_owes, b.created_at, b.sent_at "
            "FROM bills b JOIN bill_access_sessions bas ON bas.bill_id = b.id "
            "WHERE bas.session_id = ? ORDER BY b.created_at DESC, b.id DESC LIMIT 100",
            (device_id,),
        ).fetchall()
    summaries = []
    for row in rows:
        info = headline(report.teaser(row["id"], with_outcome=False)) or {"charge_count": 0, "total_savings": 0, "headline_kind": "pricing"}
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
            "sent_at": row["sent_at"],
        })
    return summaries
