"""The Bill Check Report: free teaser, paid unlock.

A bill with flagged charges shows only a count and a savings ceiling until it is unlocked.
Unlocking (one Stripe payment per bill) reveals each charge, the dispute letter and the phone script.
A bill with nothing flagged has nothing to unlock, so it is never charged for.
"""

from __future__ import annotations

import logging

from fastapi import HTTPException

import config
from analyzer import get_bill_results
from charge_summary import group_findings_by_charge
from db import get_db

log = logging.getLogger(__name__)

PAID = "paid"
PENDING = "pending"


def teaser(bill_id: int) -> dict | None:
    """What the free results page shows: how many charges are flagged and the most they could save."""
    results = get_bill_results(bill_id)
    if not results:
        return None
    bill = results.get("bill") or {}
    owed = float(bill.get("total_patient_owes") or bill.get("total_charged") or 0) or None
    summary = group_findings_by_charge(results.get("findings") or [], owed)
    return {
        "charge_count": len(summary["charges"]),
        "strong_count": summary["strong_count"],
        "total_savings": summary["total_savings"],
        "reason_counts": _reason_counts(summary["charges"]),
    }


def _reason_counts(charges: list[dict]) -> list[dict]:
    """How many flagged charges have each kind of problem, e.g. 2 x 'Possible duplicate'."""
    counts: dict[str, int] = {}
    for charge in charges:
        label = charge["reasons"][0]["label"]
        counts[label] = counts.get(label, 0) + 1
    return [{"label": label, "count": count} for label, count in sorted(counts.items(), key=lambda kv: -kv[1])]


def has_flagged_charges(bill_id: int) -> bool:
    info = teaser(bill_id)
    return bool(info and info["charge_count"])


def is_paid(bill_id: int) -> bool:
    with get_db() as db:
        row = db.execute(
            "SELECT 1 FROM report_unlocks WHERE bill_id = ? AND status = ? LIMIT 1", (bill_id, PAID)
        ).fetchone()
    return row is not None


def is_unlocked(bill_id: int) -> bool:
    """True when the full report may be shown: paid, nothing to unlock, or the slim launch is off."""
    if not config.SLIM_LAUNCH:
        return True
    return is_paid(bill_id) or not has_flagged_charges(bill_id)


def require_unlocked(bill_id: int) -> None:
    """Raise 402 with a clear message when the full report has not been unlocked for this bill."""
    if not is_unlocked(bill_id):
        raise HTTPException(
            402,
            f"Unlock the full report for ${config.REPORT_PRICE_CENTS / 100:,.0f} to see every flagged charge "
            "and get the dispute letter and phone script.",
        )


def record_pending(bill_id: int, session_id: str, email: str) -> None:
    with get_db() as db:
        db.execute(
            "INSERT OR IGNORE INTO report_unlocks (bill_id, stripe_session_id, amount_cents, status, patient_email) "
            "VALUES (?, ?, ?, ?, ?)",
            (bill_id, session_id, config.REPORT_PRICE_CENTS, PENDING, email),
        )


def mark_paid(session_id: str) -> int | None:
    """Mark a pending unlock as paid and return its bill_id; None if unknown or already paid."""
    with get_db() as db:
        row = db.execute(
            "SELECT id, bill_id, status FROM report_unlocks WHERE stripe_session_id = ?", (session_id,)
        ).fetchone()
        if not row or row["status"] == PAID:
            return None
        db.execute(
            "UPDATE report_unlocks SET status = ?, paid_at = CURRENT_TIMESTAMP WHERE id = ?", (PAID, row["id"])
        )
        return row["bill_id"]


def bill_for_session(session_id: str) -> int | None:
    with get_db() as db:
        row = db.execute(
            "SELECT bill_id FROM report_unlocks WHERE stripe_session_id = ?", (session_id,)
        ).fetchone()
    return row["bill_id"] if row else None


def pending_session_ids(bill_id: int) -> list[str]:
    """Checkout sessions started for this bill that have not been marked paid yet, newest first."""
    with get_db() as db:
        rows = db.execute(
            "SELECT stripe_session_id FROM report_unlocks WHERE bill_id = ? AND status = ? ORDER BY id DESC",
            (bill_id, PENDING),
        ).fetchall()
    return [row["stripe_session_id"] for row in rows]
