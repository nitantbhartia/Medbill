"""Directory/data helpers for non-hospital facilities."""

from __future__ import annotations

import json

from db import get_db


def _decode_json_list(raw: str | None) -> list[str]:
    if not raw:
        return []
    try:
        value = json.loads(raw)
    except Exception:
        return []
    return value if isinstance(value, list) else []


def get_facility_state_index(facility_type: str) -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            """
            SELECT state_slug, state, COUNT(*) AS facilities
            FROM facilities
            WHERE facility_type = ?
              AND state_slug IS NOT NULL
              AND state_slug != ''
            GROUP BY state_slug, state
            ORDER BY facilities DESC, state
            """,
            (facility_type,),
        ).fetchall()
    return [dict(r) for r in rows]


def get_facilities_in_scope(
    facility_type: str,
    state_slug: str | None = None,
    city_slug: str | None = None,
    limit: int = 250,
) -> list[dict]:
    where = ["f.facility_type = ?"]
    params: list = [facility_type]
    if state_slug:
        where.append("f.state_slug = ?")
        params.append(state_slug)
    if city_slug:
        where.append("f.city_slug = ?")
        params.append(city_slug)
    where_sql = " AND ".join(where)

    with get_db() as db:
        rows = db.execute(
            f"""
            SELECT
                f.facility_id, f.name, f.city, f.state, f.state_slug, f.city_slug, f.slug,
                f.is_hospital_owned, f.asc_specialties, f.imaging_modalities,
                fm.billing_grade, fm.avg_markup
            FROM facilities f
            LEFT JOIN facility_billing_metrics fm ON fm.facility_id = f.facility_id
            WHERE {where_sql}
            ORDER BY
                CASE fm.billing_grade WHEN 'A' THEN 1 WHEN 'B' THEN 2 WHEN 'C' THEN 3 WHEN 'D' THEN 4 WHEN 'F' THEN 5 ELSE 6 END,
                f.name ASC
            LIMIT ?
            """,
            (*params, limit),
        ).fetchall()

    out = []
    for r in rows:
        d = dict(r)
        d["asc_specialties"] = _decode_json_list(d.get("asc_specialties"))
        d["imaging_modalities"] = _decode_json_list(d.get("imaging_modalities"))
        out.append(d)
    return out


def get_facility_profile(facility_type: str, state_slug: str, city_slug: str, slug: str) -> dict | None:
    with get_db() as db:
        facility = db.execute(
            """
            SELECT
                f.*, fm.billing_grade, fm.avg_markup, fm.benchmark_type
            FROM facilities f
            LEFT JOIN facility_billing_metrics fm ON fm.facility_id = f.facility_id
            WHERE f.facility_type = ?
              AND f.state_slug = ?
              AND f.city_slug = ?
              AND f.slug = ?
            LIMIT 1
            """,
            (facility_type, state_slug, city_slug, slug),
        ).fetchone()
        if not facility:
            return None
        prices = db.execute(
            """
            SELECT
                cpt_code, description, gross_charge,
                COALESCE(medicare_benchmark_rate, medicare_rate) AS benchmark_rate,
                COALESCE(medicare_benchmark_type, 'opps') AS benchmark_type,
                markup_vs_medicare
            FROM procedure_prices
            WHERE facility_id = ?
            ORDER BY markup_vs_medicare DESC
            LIMIT 30
            """,
            (facility["facility_id"],),
        ).fetchall()

    data = dict(facility)
    data["prices"] = [dict(p) for p in prices]
    data["asc_specialties"] = _decode_json_list(data.get("asc_specialties"))
    data["imaging_modalities"] = _decode_json_list(data.get("imaging_modalities"))
    return data
