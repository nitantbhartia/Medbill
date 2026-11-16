"""Partner referral codes: validate them, and count scans per code for ops."""

import re

import config
from db import get_db

_REFERRAL_RE = re.compile(config.REFERRAL_CODE_PATTERN)


def valid_referral(raw: str | None) -> str | None:
    if raw and _REFERRAL_RE.fullmatch(raw):
        return raw
    return None


def partner_scan_counts() -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            "SELECT referral_code, COUNT(*) AS scans FROM bills "
            "WHERE referral_code IS NOT NULL AND created_at >= datetime('now', ?) "
            "GROUP BY referral_code ORDER BY scans DESC, referral_code",
            (f"-{config.PARTNER_REPORT_DAYS} days",),
        ).fetchall()
    return [dict(row) for row in rows]
