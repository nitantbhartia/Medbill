"""Figures for the research report and press page, computed from hospitals' own price files.

Only list prices (gross charges) are used, compared hospital to hospital for the same billing
code, so no figure depends on choosing a Medicare rate."""

from __future__ import annotations

import statistics

import config
from db import get_db
from hospital_seo import state_display_name


def _percentile(values: list[float], pct: float) -> float:
    ordered = sorted(values)
    index = (len(ordered) - 1) * pct
    low = int(index)
    high = min(low + 1, len(ordered) - 1)
    return ordered[low] + (ordered[high] - ordered[low]) * (index - low)


def _latest_prices(db, cpt_code: str) -> list[dict]:
    """One list price per hospital for a code, from its most recent data year."""
    rows = db.execute(
        """
        SELECT p.facility_id, p.gross_charge, p.description, h.state
        FROM hospital_prices p
        JOIN hospitals h ON h.facility_id = p.facility_id
        WHERE p.cpt_code = ? AND p.gross_charge > 0
          AND p.data_year = (SELECT MAX(data_year) FROM hospital_prices q
                             WHERE q.facility_id = p.facility_id AND q.cpt_code = p.cpt_code)
        """,
        (cpt_code,),
    ).fetchall()
    return [dict(row) for row in rows]


def procedure_spreads() -> list[dict]:
    """For each report code with enough hospitals: low, typical and high list price."""
    spreads = []
    with get_db() as db:
        for code in config.REPORT_CODES:
            rows = _latest_prices(db, code)
            if len(rows) < config.REPORT_MIN_HOSPITALS:
                continue
            prices = [r["gross_charge"] for r in rows]
            p10, p90 = _percentile(prices, 0.10), _percentile(prices, 0.90)
            spreads.append({
                "code": code,
                "description": next((r["description"] for r in rows if r["description"]), code),
                "hospitals": len(rows),
                "p10": round(p10),
                "median": round(statistics.median(prices)),
                "p90": round(p90),
                "spread": round(p90 / p10, 1) if p10 else None,
            })
    return spreads


def state_medians(cpt_code: str = config.REPORT_STATE_CODE) -> list[dict]:
    """Median list price by state for one code, highest first."""
    by_state: dict[str, list[float]] = {}
    with get_db() as db:
        for row in _latest_prices(db, cpt_code):
            by_state.setdefault(row["state"], []).append(row["gross_charge"])
    medians = [
        {"state": state, "state_name": state_display_name(state), "hospitals": len(prices),
         "median": round(statistics.median(prices))}
        for state, prices in by_state.items() if state and len(prices) >= config.REPORT_MIN_STATE_HOSPITALS
    ]
    return sorted(medians, key=lambda m: -m["median"])


def coverage() -> dict:
    """How much data stands behind the figures."""
    with get_db() as db:
        hospitals = db.execute("SELECT COUNT(*) FROM hospitals").fetchone()[0]
        priced = db.execute("SELECT COUNT(DISTINCT facility_id) FROM hospital_prices WHERE gross_charge > 0").fetchone()[0]
        prices = db.execute("SELECT COUNT(*) FROM hospital_prices WHERE gross_charge > 0").fetchone()[0]
        states = db.execute("SELECT COUNT(DISTINCT state) FROM hospitals WHERE state IS NOT NULL AND state != ''").fetchone()[0]
        year = db.execute("SELECT MAX(data_year) FROM hospital_prices").fetchone()[0]
    return {"hospitals": hospitals, "hospitals_with_prices": priced, "price_points": prices, "states": states, "data_year": year}
