"""Data quality coverage + consistency checks for nightly monitoring."""

from __future__ import annotations

import json
from datetime import date
from typing import Any

from db import get_db
from procedure_pages import get_providers_near_zip_for_cpt

_ALL_PRICES_CTE = """
WITH all_prices AS (
    SELECT
        facility_id, cpt_code, gross_charge, markup_vs_medicare, data_year, facility_type
    FROM procedure_prices
    UNION ALL
    SELECT
        hp.facility_id, hp.cpt_code, hp.gross_charge, hp.markup_vs_medicare, hp.data_year, hp.facility_type
    FROM hospital_prices hp
    WHERE NOT EXISTS (
        SELECT 1
        FROM procedure_prices pp
        WHERE pp.facility_id = hp.facility_id
          AND pp.cpt_code = hp.cpt_code
          AND COALESCE(pp.data_year, -1) = COALESCE(hp.data_year, -1)
          AND COALESCE(pp.facility_type, 'hospital') = COALESCE(hp.facility_type, 'hospital')
    )
)
"""


def monitored_cpt_codes(limit: int = 20) -> list[str]:
    with get_db() as db:
        rows = db.execute(
            f"""
            {_ALL_PRICES_CTE}
            SELECT cpt_code, COUNT(DISTINCT facility_id) AS n
            FROM all_prices
            WHERE gross_charge IS NOT NULL
            GROUP BY cpt_code
            ORDER BY n DESC
            LIMIT ?
            """,
            (max(1, limit),),
        ).fetchall()
    return [str(r["cpt_code"]) for r in rows]


def sampled_zips(limit: int = 250) -> list[str]:
    with get_db() as db:
        rows = db.execute(
            """
            SELECT zip
            FROM zip_latlon
            WHERE zip IS NOT NULL AND LENGTH(zip) = 5
            ORDER BY zip
            LIMIT ?
            """,
            (max(1, limit),),
        ).fetchall()
    return [str(r["zip"]) for r in rows]


def compute_coverage(
    cpt_codes: list[str],
    radii_miles: list[int],
    zip_samples: list[str],
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    if not cpt_codes or not radii_miles or not zip_samples:
        return out
    for cpt in cpt_codes:
        for radius in radii_miles:
            covered = 0
            for z in zip_samples:
                rows = get_providers_near_zip_for_cpt(
                    cpt_code=cpt,
                    zip_code=z,
                    limit=1,
                    facility_type="all",
                    grade_ab_only=False,
                    sort_by="patient_cost",
                    radius_miles=float(radius),
                )
                if rows:
                    covered += 1
            sample_count = len(zip_samples)
            out.append(
                {
                    "cpt_code": cpt,
                    "radius_miles": int(radius),
                    "zip_samples": sample_count,
                    "covered_zips": covered,
                    "coverage_ratio": (covered / sample_count) if sample_count else 0.0,
                }
            )
    return out


def run_consistency_checks() -> dict[str, Any]:
    current_year = date.today().year
    with get_db() as db:
        invalid_gross = db.execute(
            """
            SELECT COUNT(1) AS n
            FROM (
                SELECT gross_charge FROM procedure_prices
                UNION ALL
                SELECT gross_charge FROM hospital_prices
            )
            WHERE gross_charge IS NOT NULL
              AND (gross_charge <= 0 OR gross_charge > 1000000)
            """
        ).fetchone()["n"]
        invalid_markup = db.execute(
            """
            SELECT COUNT(1) AS n
            FROM (
                SELECT markup_vs_medicare FROM procedure_prices
                UNION ALL
                SELECT markup_vs_medicare FROM hospital_prices
            )
            WHERE markup_vs_medicare IS NOT NULL
              AND (markup_vs_medicare <= 0 OR markup_vs_medicare > 50)
            """
        ).fetchone()["n"]
        priced_missing_coords = db.execute(
            f"""
            {_ALL_PRICES_CTE}
            SELECT COUNT(DISTINCT ap.facility_id) AS n
            FROM all_prices ap
            LEFT JOIN facilities f ON f.facility_id = ap.facility_id
            LEFT JOIN hospitals h ON h.facility_id = ap.facility_id
            WHERE ap.gross_charge IS NOT NULL
              AND COALESCE(f.lat, h.lat) IS NULL
              AND COALESCE(f.lon, h.lon) IS NULL
            """
        ).fetchone()["n"]
        stale_rows = db.execute(
            """
            SELECT COUNT(1) AS n
            FROM (
                SELECT data_year FROM procedure_prices
                UNION ALL
                SELECT data_year FROM hospital_prices
            )
            WHERE data_year IS NOT NULL AND data_year < ?
            """,
            (current_year - 1,),
        ).fetchone()["n"]
        zip_state_mismatch = db.execute(
            """
            SELECT COUNT(1) AS n
            FROM facilities f
            JOIN zip_locality_map zm
              ON substr(COALESCE(f.zip, ''), 1, 5) = zm.zip_prefix
            WHERE LENGTH(COALESCE(f.zip, '')) >= 5
              AND zm.state IS NOT NULL
              AND f.state IS NOT NULL
              AND UPPER(f.state) <> UPPER(zm.state)
            """
        ).fetchone()["n"]

    checks = {
        "invalid_gross_prices": int(invalid_gross),
        "invalid_markups": int(invalid_markup),
        "priced_facilities_missing_coords": int(priced_missing_coords),
        "stale_pricing_rows": int(stale_rows),
        "zip_state_mismatch": int(zip_state_mismatch),
    }
    return {
        "checks": checks,
        "all_passed": all(v == 0 for v in checks.values()),
    }


def compare_coverage(
    current: list[dict[str, Any]],
    previous: list[dict[str, Any]] | None,
    max_drop_ratio: float = 0.10,
) -> list[dict[str, Any]]:
    if not previous:
        return []
    prev_index = {(r["cpt_code"], int(r["radius_miles"])): r for r in previous}
    regressions: list[dict[str, Any]] = []
    for cur in current:
        key = (cur["cpt_code"], int(cur["radius_miles"]))
        prv = prev_index.get(key)
        if not prv:
            continue
        prev_ratio = float(prv.get("coverage_ratio") or 0.0)
        cur_ratio = float(cur.get("coverage_ratio") or 0.0)
        if prev_ratio <= 0:
            continue
        drop = prev_ratio - cur_ratio
        if drop > max_drop_ratio:
            regressions.append(
                {
                    "cpt_code": cur["cpt_code"],
                    "radius_miles": int(cur["radius_miles"]),
                    "previous_ratio": prev_ratio,
                    "current_ratio": cur_ratio,
                    "drop": drop,
                }
            )
    return regressions


def latest_quality_run() -> dict[str, Any] | None:
    with get_db() as db:
        row = db.execute(
            """
            SELECT id, run_date, status, coverage_json, checks_json, notes
            FROM data_quality_runs
            ORDER BY id DESC
            LIMIT 1
            """
        ).fetchone()
    if not row:
        return None
    return {
        "id": row["id"],
        "run_date": row["run_date"],
        "status": row["status"],
        "coverage": json.loads(row["coverage_json"] or "[]"),
        "checks": json.loads(row["checks_json"] or "{}"),
        "notes": row["notes"],
    }


def save_quality_run(
    status: str,
    coverage: list[dict[str, Any]],
    checks: dict[str, Any],
    notes: str = "",
) -> int:
    with get_db() as db:
        db.execute(
            """
            INSERT INTO data_quality_runs (status, coverage_json, checks_json, notes)
            VALUES (?, ?, ?, ?)
            """,
            (status, json.dumps(coverage), json.dumps(checks), notes),
        )
        row = db.execute("SELECT last_insert_rowid() AS id").fetchone()
        return int(row["id"])

