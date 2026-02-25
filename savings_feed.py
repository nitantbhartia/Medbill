"""Community Savings Feed — anonymous, aggregated display of recent savings wins."""

from db import get_db

# Friendly finding type labels
FINDING_LABELS = {
    "price_markup": "overcharge vs Medicare",
    "duplicate_charge": "duplicate charge removed",
    "unbundling": "unbundling correction",
    "upcoding": "coding level correction",
    "no_surprises_act": "No Surprises Act violation",
    "benchmark_outlier": "above-market pricing",
    "eob_mismatch": "insurance math error",
    "quantity_flag": "quantity correction",
}


def get_recent_savings(limit: int = 20) -> list[dict]:
    """Return recent anonymized savings events for the community feed."""
    with get_db() as db:
        rows = db.execute(
            """
            SELECT
                b.provider_name,
                b.zip_code,
                f.finding_type,
                f.severity,
                f.potential_savings,
                f.created_at,
                b.total_charged
            FROM findings f
            JOIN bills b ON b.id = f.bill_id
            WHERE f.potential_savings > 0
              AND b.provider_name IS NOT NULL
            ORDER BY f.created_at DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    feed = []
    for row in rows:
        row = dict(row)
        # Anonymize: only show city-level info from zip, not full provider name
        provider = row.get("provider_name") or "a hospital"
        # Truncate provider to first word + "Medical Center" style
        words = provider.split()
        if len(words) > 2:
            provider = words[0] + " " + words[1] + "..."
        else:
            provider = provider[:20]

        finding_label = FINDING_LABELS.get(row["finding_type"], "billing issue")
        savings = float(row["potential_savings"] or 0)

        feed.append({
            "provider_hint": provider,
            "zip_prefix": (row.get("zip_code") or "")[:3] + "xx",
            "finding_label": finding_label,
            "severity": row["severity"],
            "savings": round(savings, 2),
            "total_charged": float(row.get("total_charged") or 0),
            "created_at": row["created_at"],
        })
    return feed


def get_aggregate_stats() -> dict:
    """Return aggregate community savings stats for social proof."""
    with get_db() as db:
        row = db.execute(
            """
            SELECT
                COUNT(DISTINCT b.id) AS bills_analyzed,
                COALESCE(SUM(f.potential_savings), 0) AS total_savings_found,
                COUNT(f.id) AS total_issues_found,
                COALESCE(AVG(f.potential_savings), 0) AS avg_savings_per_issue,
                (SELECT COUNT(DISTINCT bill_id) FROM findings WHERE potential_savings > 0) AS bills_with_savings
            FROM bills b
            LEFT JOIN findings f ON f.bill_id = b.id AND f.potential_savings > 0
            """
        ).fetchone()

        outcome_row = db.execute(
            """
            SELECT
                COUNT(*) AS total_disputes,
                SUM(CASE WHEN actual_savings > 0 THEN 1 ELSE 0 END) AS successful_disputes,
                COALESCE(SUM(actual_savings), 0) AS total_realized_savings
            FROM dispute_outcomes
            """
        ).fetchone()

        # Top finding types by total savings
        type_rows = db.execute(
            """
            SELECT
                finding_type,
                COUNT(*) AS count,
                SUM(potential_savings) AS total_savings
            FROM findings
            WHERE potential_savings > 0
            GROUP BY finding_type
            ORDER BY total_savings DESC
            LIMIT 5
            """
        ).fetchall()

    stats = dict(row)
    outcomes = dict(outcome_row)
    stats["total_disputes"] = outcomes["total_disputes"]
    stats["successful_disputes"] = outcomes["successful_disputes"]
    stats["total_realized_savings"] = outcomes["total_realized_savings"]

    stats["top_finding_types"] = [
        {
            "type": FINDING_LABELS.get(r["finding_type"], r["finding_type"]),
            "count": r["count"],
            "total_savings": round(float(r["total_savings"] or 0), 2),
        }
        for r in type_rows
    ]

    return stats
