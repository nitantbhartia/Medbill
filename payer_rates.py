"""Insurer-specific prices from hospital price files: one row per payer and plan, with insurer names made comparable."""

from __future__ import annotations

import re
from datetime import date, datetime, timedelta

import config
from db import get_db

WIDE_COLUMN = re.compile(r"standard_charge\|(?P<payer>[^|]+)\|(?P<plan>[^|]+)\|negotiated_dollar$", re.I)

# Names as they appear on price files and statements, by hand for the main California insurers.
PAYER_ALIASES = {
    "Anthem Blue Cross": ["anthem blue cross", "anthem bc", "anthem bc life & health", "blue cross of california", "anthem blue cross life and health"],
    "Blue Shield of California": ["blue shield of california", "blue shield ca", "california blue shield", "blue shield"],
    "Kaiser Permanente": ["kaiser permanente", "kaiser foundation health plan", "kaiser"],
    "Health Net": ["health net", "health net of california", "healthnet"],
    "Aetna": ["aetna", "aetna life insurance", "aetna health of california"],
    "Cigna": ["cigna", "cigna healthcare", "connecticut general life"],
    "UnitedHealthcare": ["unitedhealthcare", "united healthcare", "uhc", "united healthcare insurance"],
    "Sharp Health Plan": ["sharp health plan", "sharp health plan inc"],
    "Molina Healthcare": ["molina healthcare", "molina healthcare of california", "molina"],
    "Oscar Health": ["oscar health", "oscar insurance", "oscar"],
    "L.A. Care Health Plan": ["la care", "l.a. care", "l.a. care health plan", "los angeles care health plan"],
    "Health Plan of San Joaquin": ["health plan of san joaquin", "hpsj"],
    "Western Health Advantage": ["western health advantage", "wha"],
    "Sutter Health Plus": ["sutter health plus", "sutter plus"],
    "Humana": ["humana", "humana health plan of california"],
}


def _norm(name: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9& ]", " ", str(name).lower())).strip()


def seed_aliases() -> None:
    with get_db() as db:
        for canonical, aliases in PAYER_ALIASES.items():
            for alias in aliases + [canonical]:
                db.execute("INSERT OR REPLACE INTO payer_aliases (alias, canonical) VALUES (?, ?)", (_norm(alias), canonical))


def canonical_payer(name: str | None) -> str | None:
    """One name for an insurer. Exact alias first, then a name that contains an alias. None when unknown."""
    if not name or not _norm(name):
        return None
    text = _norm(name)
    with get_db() as db:
        row = db.execute("SELECT canonical FROM payer_aliases WHERE alias = ?", (text,)).fetchone()
        if row:
            return row["canonical"]
        for alias in db.execute("SELECT alias, canonical FROM payer_aliases ORDER BY length(alias) DESC"):
            if len(alias["alias"]) >= 5 and alias["alias"] in text:
                return alias["canonical"]
    return None


def save_payer_rates(facility_id: str, rows: list[dict], source_url: str, file_updated: str | None, year: int | None = None) -> int:
    """Store one observation per payer, plan and code. A reload replaces the same source row."""
    saved = 0
    parsed_at = datetime.now().isoformat(timespec="seconds")
    with get_db() as db:
        for row in rows:
            if not row.get("payer") or not (row.get("avg_negotiated_rate") or row.get("median_allowed")):
                continue
            canonical = canonical_payer(row["payer"]) or row["payer"]
            ref = f"{facility_id}|{row['cpt_code']}|{canonical}|{row.get('plan_name') or ''}|{year or ''}"
            db.execute(
                "INSERT OR REPLACE INTO price_observations (source_type, source_ref, code, facility_id, payer, plan_name, "
                "negotiated_rate, median_allowed, p10_allowed, p90_allowed, source_url, file_updated, parsed_at, effective_year, confidence) "
                "VALUES ('mrf', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0.9)",
                (ref, row["cpt_code"], facility_id, canonical, row.get("plan_name"), row.get("avg_negotiated_rate"),
                 row.get("median_allowed"), row.get("p10_allowed"), row.get("p90_allowed"), source_url, file_updated, parsed_at, year),
            )
            saved += 1
    return saved


def find_contracted_rate(facility_id: str, code: str, insurer: str | None) -> dict | None:
    """The insurer's rate at this hospital for this code, from a file no older than MRF_MAX_AGE_DAYS. Plans are averaged."""
    payer = canonical_payer(insurer)
    if not payer:
        return None
    oldest = (date.today() - timedelta(days=config.MRF_MAX_AGE_DAYS)).isoformat()
    with get_db() as db:
        row = db.execute(
            "SELECT AVG(COALESCE(negotiated_rate, median_allowed)) AS rate, MAX(source_url) AS source_url, "
            "MAX(file_updated) AS file_updated, MAX(effective_year) AS year FROM price_observations "
            "WHERE source_type = 'mrf' AND facility_id = ? AND code = ? AND payer = ? "
            "AND COALESCE(file_updated, substr(parsed_at, 1, 10)) >= ?",
            (facility_id, code, payer, oldest)).fetchone()
    if not row or row["rate"] is None:
        return None
    return {"payer": payer, "rate": round(row["rate"], 2), "source_url": row["source_url"],
            "file_updated": row["file_updated"], "year": row["year"]}
