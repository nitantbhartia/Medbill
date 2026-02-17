"""Provider-level intelligence and outcomes summary."""

from __future__ import annotations

from db import get_db


def get_provider_intelligence(provider_name: str) -> dict:
    with get_db() as db:
        overview = db.execute(
            "SELECT COUNT(*) AS bills_scanned, "
            "COALESCE(AVG(total_potential_savings), 0) AS avg_estimated_savings, "
            "COALESCE(SUM(total_potential_savings), 0) AS total_estimated_savings "
            "FROM bills WHERE provider_name = ?",
            (provider_name,),
        ).fetchone()

        issue_mix = db.execute(
            "SELECT f.finding_type, COUNT(*) AS count "
            "FROM findings f JOIN bills b ON b.id = f.bill_id "
            "WHERE b.provider_name = ? "
            "GROUP BY f.finding_type ORDER BY count DESC",
            (provider_name,),
        ).fetchall()

        outcomes = db.execute(
            "SELECT COUNT(*) AS outcomes, "
            "COALESCE(SUM(actual_savings), 0) AS realized_savings, "
            "COALESCE(AVG(actual_savings), 0) AS avg_realized_savings "
            "FROM dispute_outcomes WHERE hospital_name = ?",
            (provider_name,),
        ).fetchone()

    return {
        "provider_name": provider_name,
        "overview": dict(overview),
        "issue_mix": [dict(r) for r in issue_mix],
        "outcomes": dict(outcomes),
    }
