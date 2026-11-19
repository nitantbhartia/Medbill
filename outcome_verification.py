"""Verify a reported saving with the new statement the hospital sent."""

from __future__ import annotations

import hashlib
import json

import config
import mobile_purchases
import scan_pipeline
from analyzer import _HOSPITAL_GENERIC, _norm_hospital_name, find_hospital_match
from db import get_db

GENERIC_WORDS = _HOSPITAL_GENERIC | {"medical", "center", "hospital", "health", "regional", "community", "memorial"}


def _same_hospital(first: str | None, second: str | None) -> bool:
    def words(name):
        every = {w for w in _norm_hospital_name(name or "").split() if w not in _HOSPITAL_GENERIC and len(w) > 2}
        return (every - GENERIC_WORDS) or every
    a, b = words(first), words(second)
    return bool(a and b) and len(a & b) >= min(config.VERIFY_NAME_MATCH_MIN_SHARED_WORDS, len(a), len(b))


def bill_rule_ids(bill_id: int) -> list[str]:
    with get_db() as db:
        rows = db.execute("SELECT DISTINCT rule_id FROM findings WHERE bill_id = ? AND rule_id IS NOT NULL", (bill_id,)).fetchall()
    return [row["rule_id"] for row in rows]


def facility_for(bill: dict) -> str | None:
    match = find_hospital_match(bill.get("provider_name") or "", bill.get("zip_code"))
    return match["facility_id"] if match else None


def record_reported(bill_id: int, bill: dict, outcome: str, final_owed: float, reason_category: str | None = None) -> float:
    """A self-reported outcome. Unverified until the user sends the new statement.
    A rejection keeps the rules that were flagged and the reason the hospital gave."""
    rejected = json.dumps(bill_rule_ids(bill_id)) if outcome in config.REJECTED_OUTCOMES else None
    original = bill.get("total_patient_owes") or 0
    saved = max(0, original - final_owed)
    with get_db() as db:
        db.execute(
            "INSERT INTO dispute_outcomes (bill_id, hospital_name, called_billing, outcome, original_patient_owes, "
            "final_patient_owes, actual_savings, shared_publicly, facility_id, rule_ids, rejected_rule_ids, reason_category) "
            "VALUES (?, ?, 1, ?, ?, ?, ?, 0, ?, ?, ?, ?)",
            (bill_id, bill.get("provider_name"), outcome, original, final_owed, saved, facility_for(bill),
             json.dumps(bill_rule_ids(bill_id)), rejected, reason_category if rejected else None))
    return saved


def verify_with_statement(bill_id: int, device_id: str, images: list[tuple[bytes, str]]) -> dict:
    """Read the new statement. It verifies the outcome when its patient balance is lower than the original
    and it is from the same hospital. Verifying earns free Plus."""
    with get_db() as db:
        bill = dict(db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone())
    statement = scan_pipeline.extract_pages(images)
    new_owed = statement.get("total_patient_owes")
    original = bill.get("total_patient_owes")
    if new_owed is None or original is None:
        return {"verified": False, "reason": "unreadable"}
    if not _same_hospital(bill.get("provider_name"), statement.get("provider_name")):
        return {"verified": False, "reason": "different_hospital"}
    if new_owed >= original:
        return {"verified": False, "reason": "not_lower"}
    saved = round(original - new_owed, 2)
    digest = hashlib.sha256(images[0][0]).hexdigest()
    with get_db() as db:
        updated = db.execute(
            "UPDATE dispute_outcomes SET verified = 1, final_patient_owes = ?, actual_savings = ?, evidence_upload_id = ?, "
            "facility_id = COALESCE(facility_id, ?), rule_ids = ? WHERE id = (SELECT MAX(id) FROM dispute_outcomes WHERE bill_id = ?)",
            (new_owed, saved, digest, facility_for(bill), json.dumps(bill_rule_ids(bill_id)), bill_id)).rowcount
        if not updated:
            db.execute(
                "INSERT INTO dispute_outcomes (bill_id, hospital_name, called_billing, outcome, original_patient_owes, final_patient_owes, "
                "actual_savings, shared_publicly, verified, evidence_upload_id, facility_id, rule_ids) "
                "VALUES (?, ?, 1, 'reduced', ?, ?, ?, 0, 1, ?, ?, ?)",
                (bill_id, bill.get("provider_name"), original, new_owed, saved, digest, facility_for(bill),
                 json.dumps(bill_rule_ids(bill_id))))
    mobile_purchases.grant_reward_plus(device_id, config.VERIFY_REWARD_PLUS_DAYS)
    return {"verified": True, "actual_savings": saved, "reward_days": config.VERIFY_REWARD_PLUS_DAYS}
