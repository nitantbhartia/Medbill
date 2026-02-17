"""Compliance helpers: consent logs, audit logs, PHI minimization, export/delete controls."""

from __future__ import annotations

import json
from datetime import datetime, timedelta

from db import get_db


def scrub_extracted_data(extracted: dict) -> dict:
    """Remove or mask high-risk identifiers before persistence."""
    cleaned = dict(extracted)
    # Do not persist full patient name by default.
    cleaned["patient_name"] = None
    acct = cleaned.get("account_number")
    if acct and isinstance(acct, str):
        stripped = acct.strip()
        cleaned["account_number"] = f"***{stripped[-4:]}" if len(stripped) > 4 else "***"
    return cleaned


def record_consent(
    user_id: int | None,
    bill_id: int | None,
    consent_type: str,
    consent_version: str,
    ip_address: str = "",
    user_agent: str = "",
) -> int:
    with get_db() as db:
        cur = db.execute(
            "INSERT INTO consent_logs (user_id, bill_id, consent_type, consent_version, ip_address, user_agent) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, bill_id, consent_type, consent_version, ip_address, user_agent),
        )
        return cur.lastrowid


def log_audit(
    action: str,
    resource_type: str,
    resource_id: str = "",
    user_id: int | None = None,
    bill_id: int | None = None,
    metadata: dict | None = None,
) -> int:
    with get_db() as db:
        cur = db.execute(
            "INSERT INTO audit_logs (user_id, bill_id, action, resource_type, resource_id, metadata) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, bill_id, action, resource_type, resource_id, json.dumps(metadata or {})),
        )
        return cur.lastrowid


def export_bill_data(bill_id: int) -> dict | None:
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            return None
        line_items = db.execute("SELECT * FROM line_items WHERE bill_id = ?", (bill_id,)).fetchall()
        findings = db.execute("SELECT * FROM findings WHERE bill_id = ?", (bill_id,)).fetchall()
        outcomes = db.execute("SELECT * FROM dispute_outcomes WHERE bill_id = ?", (bill_id,)).fetchall()
        neg = db.execute("SELECT * FROM negotiations WHERE bill_id = ?", (bill_id,)).fetchall()
        consents = db.execute("SELECT * FROM consent_logs WHERE bill_id = ?", (bill_id,)).fetchall()

    return {
        "exported_at": datetime.utcnow().isoformat(),
        "bill": dict(bill),
        "line_items": [dict(x) for x in line_items],
        "findings": [dict(x) for x in findings],
        "outcomes": [dict(x) for x in outcomes],
        "negotiations": [dict(x) for x in neg],
        "consents": [dict(x) for x in consents],
    }


def delete_bill_data(bill_id: int) -> bool:
    with get_db() as db:
        bill = db.execute("SELECT id FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            return False
        # dependent tables (manual cleanup to avoid relying on ON DELETE CASCADE)
        neg_ids = [
            row["id"]
            for row in db.execute("SELECT id FROM negotiations WHERE bill_id = ?", (bill_id,)).fetchall()
        ]
        for neg_id in neg_ids:
            db.execute("DELETE FROM negotiation_messages WHERE negotiation_id = ?", (neg_id,))
        db.execute("DELETE FROM negotiations WHERE bill_id = ?", (bill_id,))
        db.execute("DELETE FROM dispute_outcomes WHERE bill_id = ?", (bill_id,))
        db.execute("DELETE FROM public_stories WHERE bill_id = ?", (bill_id,))
        db.execute("DELETE FROM findings WHERE bill_id = ?", (bill_id,))
        db.execute("DELETE FROM line_items WHERE bill_id = ?", (bill_id,))
        db.execute("DELETE FROM consent_logs WHERE bill_id = ?", (bill_id,))
        db.execute("DELETE FROM audit_logs WHERE bill_id = ?", (bill_id,))
        db.execute("DELETE FROM bills WHERE id = ?", (bill_id,))
    return True


def purge_old_data(days: int = 365) -> int:
    cutoff = (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    with get_db() as db:
        old_ids = [
            row["id"]
            for row in db.execute(
                "SELECT id FROM bills WHERE created_at < ?",
                (cutoff,),
            ).fetchall()
        ]
    deleted = 0
    for bill_id in old_ids:
        if delete_bill_data(bill_id):
            deleted += 1
    return deleted
