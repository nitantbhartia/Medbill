"""My Bills dashboard — lists all bills a user has scanned in their session."""

from __future__ import annotations

from db import get_db


def get_session_bills(session_id: str) -> list[dict]:
    """Return all bills accessible to this session, newest first."""
    if not session_id:
        return []
    with get_db() as db:
        rows = db.execute(
            """
            SELECT b.id, b.provider_name, b.total_charged,
                   b.total_patient_owes, b.finding_count,
                   b.potential_savings, b.created_at,
                   dc.id AS case_id, dc.status AS case_status,
                   dc.realized_savings
            FROM bills b
            JOIN bill_access_sessions bas ON bas.bill_id = b.id
            LEFT JOIN dispute_cases dc ON dc.bill_id = b.id
            WHERE bas.session_id = ?
            ORDER BY b.created_at DESC
            LIMIT 50
            """,
            (session_id,),
        ).fetchall()
    return [dict(r) for r in rows]


def get_session_summary(bills: list[dict]) -> dict:
    """Aggregate stats across all session bills."""
    total_charged = sum(b.get("total_charged") or 0 for b in bills)
    total_savings = sum(b.get("potential_savings") or 0 for b in bills)
    total_issues = sum(b.get("finding_count") or 0 for b in bills)
    total_realized = sum(b.get("realized_savings") or 0 for b in bills)
    disputed = sum(1 for b in bills if b.get("case_id"))
    resolved = sum(1 for b in bills if b.get("case_status") == "resolved")

    return {
        "bill_count": len(bills),
        "total_charged": round(total_charged, 2),
        "total_potential_savings": round(total_savings, 2),
        "total_issues": total_issues,
        "total_realized_savings": round(total_realized, 2),
        "disputed_count": disputed,
        "resolved_count": resolved,
    }
