"""Free-scan limits. Every scan costs AI tokens and there is no login, so each scan is counted three ways,
all over the last 24 hours and all stored in the database so a restart does not reset them:

- per visitor (session cookie on the web, device in the app): successful scans only, so a blurry photo can be retried
- per network address: every attempt, because clearing cookies is easy and a failed read still costs tokens
- site-wide: every attempt, a ceiling on what one bad day can cost
"""

from __future__ import annotations

import logging

from fastapi import HTTPException

import config
from db import get_db

log = logging.getLogger(__name__)

WINDOW = "-1 day"
TOTAL_KEY = "total"


def _count(db, key: str) -> int:
    row = db.execute(
        "SELECT COUNT(*) AS n FROM scan_attempts WHERE key = ? AND created_at >= datetime('now', ?)", (key, WINDOW)
    ).fetchone()
    return row["n"]


def check_and_count(visitor_key: str, address_key: str, visitor_limit: int, address_limit: int) -> None:
    """Raise 429 when this visitor or address has used its scans, 503 when the site-wide ceiling is reached.
    Otherwise count one attempt against the address and the site."""
    with get_db() as db:
        db.execute("DELETE FROM scan_attempts WHERE created_at < datetime('now', '-2 days')")
        if _count(db, visitor_key) >= visitor_limit:
            raise HTTPException(429, f"You've used your {visitor_limit} free bill checks for today. Please come back tomorrow, "
                                     "or email support@billkarma.app if you need more.")
        if _count(db, address_key) >= address_limit:
            raise HTTPException(429, "Too many bill checks from this network today. Please try again tomorrow.")
        if _count(db, TOTAL_KEY) >= config.SCAN_DAILY_LIMIT_TOTAL:
            log.error("Site-wide scan ceiling reached (%s in 24h); scans are refused until it clears", config.SCAN_DAILY_LIMIT_TOTAL)
            raise HTTPException(503, "We're checking a lot of bills right now. Please try again in a few hours.")
        db.executemany("INSERT INTO scan_attempts (key) VALUES (?)", [(address_key,), (TOTAL_KEY,)])


def count_success(visitor_key: str) -> None:
    with get_db() as db:
        db.execute("INSERT INTO scan_attempts (key) VALUES (?)", (visitor_key,))


def count_extra_read() -> None:
    """A follow-up read (an added insurance statement, a new statement to verify) counts against the site only."""
    with get_db() as db:
        if _count(db, TOTAL_KEY) >= config.SCAN_DAILY_LIMIT_TOTAL:
            raise HTTPException(503, "We're checking a lot of bills right now. Please try again in a few hours.")
        db.execute("INSERT INTO scan_attempts (key) VALUES (?)", (TOTAL_KEY,))
