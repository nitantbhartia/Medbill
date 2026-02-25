"""Bill Watch — let users subscribe to price alerts for providers and procedures."""

import re

from db import get_db

MAX_WATCHES_PER_EMAIL = 10
VALID_WATCH_TYPES = ("provider", "procedure", "zip")


def add_watch(email: str, watch_type: str, watch_value: str, zip_code: str = "") -> dict:
    """Create a price watch subscription."""
    email = (email or "").strip().lower()
    if not email or not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
        return {"ok": False, "error": "Invalid email address"}

    if watch_type not in VALID_WATCH_TYPES:
        return {"ok": False, "error": f"Invalid watch type. Must be one of: {', '.join(VALID_WATCH_TYPES)}"}

    watch_value = (watch_value or "").strip()
    if not watch_value:
        return {"ok": False, "error": "Watch value is required"}

    with get_db() as db:
        # Check limits
        existing = db.execute(
            "SELECT COUNT(*) AS n FROM bill_watches WHERE email = ? AND active = 1",
            (email,),
        ).fetchone()["n"]

        if existing >= MAX_WATCHES_PER_EMAIL:
            return {"ok": False, "error": f"Maximum of {MAX_WATCHES_PER_EMAIL} active watches per email"}

        # Check for duplicate
        dup = db.execute(
            "SELECT id FROM bill_watches WHERE email = ? AND watch_type = ? AND watch_value = ? AND active = 1",
            (email, watch_type, watch_value),
        ).fetchone()
        if dup:
            return {"ok": False, "error": "You already have an active watch for this"}

        db.execute(
            "INSERT INTO bill_watches (email, watch_type, watch_value, zip_code) VALUES (?, ?, ?, ?)",
            (email, watch_type, watch_value, zip_code),
        )

    return {"ok": True, "message": "Watch created! We'll email you when we find relevant price updates."}


def remove_watch(watch_id: int, email: str) -> dict:
    """Deactivate a watch subscription."""
    with get_db() as db:
        result = db.execute(
            "UPDATE bill_watches SET active = 0 WHERE id = ? AND email = ?",
            (watch_id, email),
        )
        if result.rowcount == 0:
            return {"ok": False, "error": "Watch not found"}
    return {"ok": True, "message": "Watch removed"}


def get_watches_for_email(email: str) -> list[dict]:
    """List all active watches for an email."""
    email = (email or "").strip().lower()
    with get_db() as db:
        rows = db.execute(
            "SELECT * FROM bill_watches WHERE email = ? AND active = 1 ORDER BY created_at DESC",
            (email,),
        ).fetchall()
    return [dict(r) for r in rows]


def get_pending_alerts(limit: int = 100) -> list[dict]:
    """Find watches that match recent price changes (for batch processing)."""
    with get_db() as db:
        # Provider watches: match against recent hospital_prices changes
        provider_alerts = db.execute(
            """
            SELECT
                w.id AS watch_id,
                w.email,
                w.watch_value AS provider_name,
                h.name AS matched_provider,
                h.facility_id,
                COUNT(hp.cpt_code) AS price_updates
            FROM bill_watches w
            JOIN hospitals h ON lower(h.name) LIKE '%' || lower(w.watch_value) || '%'
            JOIN hospital_prices hp ON hp.facility_id = h.facility_id
            WHERE w.active = 1
              AND w.watch_type = 'provider'
              AND w.last_notified_at IS NULL
            GROUP BY w.id
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

        # Procedure watches: match against fair_price_bands updates
        procedure_alerts = db.execute(
            """
            SELECT
                w.id AS watch_id,
                w.email,
                w.watch_value AS cpt_code,
                fpb.p50 AS median_price,
                fpb.geo_value,
                fpb.sample_size
            FROM bill_watches w
            JOIN fair_price_bands fpb ON fpb.code = w.watch_value
              AND fpb.geo_scope = 'state'
            WHERE w.active = 1
              AND w.watch_type = 'procedure'
              AND w.last_notified_at IS NULL
            GROUP BY w.id
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    alerts = []
    for row in provider_alerts:
        alerts.append({**dict(row), "alert_type": "provider"})
    for row in procedure_alerts:
        alerts.append({**dict(row), "alert_type": "procedure"})
    return alerts


def mark_notified(watch_id: int) -> None:
    """Mark a watch as notified so it doesn't fire again until next cycle."""
    with get_db() as db:
        db.execute(
            "UPDATE bill_watches SET last_notified_at = CURRENT_TIMESTAMP WHERE id = ?",
            (watch_id,),
        )
