"""Hospital comparison tool — data queries and verdict generation."""

from __future__ import annotations

import math

from config import ENABLE_FREE_MAPS
from db import get_db
from hospital_seo import (
    FRIENDLY_CPT_DESCRIPTIONS,
    _display_city,
    _display_name,
    _grade_index,
    _ownership_display_label,
    state_display_name,
)

_GRADE_COLORS = {
    "A": "#22c55e", "B": "#84cc16", "C": "#f59e0b", "D": "#f97316", "F": "#ef4444",
}
_GRADE_BADGE = {
    "A": "bg-green-100 text-green-700",
    "B": "bg-lime-100 text-lime-700",
    "C": "bg-yellow-100 text-yellow-700",
    "D": "bg-orange-100 text-orange-700",
    "F": "bg-red-100 text-red-700",
}
_ALL_PRICES_CTE = """
WITH all_prices AS (
    SELECT
        facility_id, cpt_code, description, gross_charge,
        medicare_rate, markup_vs_medicare,
        facility_type, medicare_benchmark_type, medicare_benchmark_rate
    FROM hospital_prices
    UNION ALL
    SELECT
        facility_id, cpt_code, description, gross_charge,
        medicare_rate, markup_vs_medicare,
        facility_type, medicare_benchmark_type, medicare_benchmark_rate
    FROM procedure_prices
)
"""


def search_hospitals_for_compare(query: str, limit: int = 10) -> list[dict]:
    """Search hospitals by name/city/state and return fields needed for comparison autocomplete."""
    q = (query or "").strip()
    if len(q) < 2:
        return []
    token = f"%{q}%"
    with get_db() as db:
        rows = db.execute(
            """
            SELECT h.facility_id, h.name, h.city, h.state, h.slug, h.state_slug, h.city_slug,
                   m.billing_grade, m.avg_markup_vs_medicare
            FROM hospitals h
            LEFT JOIN billing_metrics m ON m.facility_id = h.facility_id
            WHERE h.name LIKE ? OR h.city LIKE ? OR h.state LIKE ?
            ORDER BY
              CASE WHEN lower(h.name) LIKE lower(?) THEN 0 ELSE 1 END,
              h.name
            LIMIT ?
            """,
            (token, token, token, f"{q.lower()}%", limit),
        ).fetchall()
    result = []
    for row in rows:
        d = dict(row)
        d["name"] = _display_name(d.get("name"), d.get("facility_id"))
        d["city"] = _display_city(d.get("city"))
        d["state"] = state_display_name(d.get("state"))
        result.append(d)
    return result


def get_hospital_for_compare(facility_id: str) -> dict | None:
    """Return core stats for one provider, or None if not found."""
    with get_db() as db:
        row = db.execute(
            """
            SELECT
                h.facility_id, h.name, h.city, h.state, h.state_slug, h.city_slug, h.slug,
                h.ownership, h.is_nonprofit, h.cms_star_rating, h.bed_count, h.lat, h.lon,
                m.billing_grade, m.avg_markup_vs_medicare, m.procedures_compared,
                m.state_rank, m.national_percentile,
                tf.parse_status, tf.procedures_extracted, tf.has_standard_codes,
                hf.charity_care_pct, hf.charity_care_pct_revenue,
                hf.has_financial_assistance_policy, hf.nonprofit_status
            FROM hospitals h
            LEFT JOIN billing_metrics m ON m.facility_id = h.facility_id
            LEFT JOIN transparency_files tf ON tf.facility_id = h.facility_id
            LEFT JOIN hospital_financials hf ON hf.facility_id = h.facility_id
            WHERE h.facility_id = ?
            """,
            (facility_id,),
        ).fetchone()
        if not row:
            row = db.execute(
                """
                SELECT
                    f.facility_id, f.name, f.city, f.state, f.state_slug, f.city_slug, f.slug,
                    f.ownership_type AS ownership, NULL AS is_nonprofit, NULL AS cms_star_rating, NULL AS bed_count,
                    f.lat, f.lon,
                    fm.billing_grade, fm.avg_markup AS avg_markup_vs_medicare, fm.procedures_compared,
                    NULL AS state_rank, NULL AS national_percentile,
                    NULL AS parse_status, NULL AS procedures_extracted, NULL AS has_standard_codes,
                    NULL AS charity_care_pct, NULL AS charity_care_pct_revenue,
                    NULL AS has_financial_assistance_policy, NULL AS nonprofit_status,
                    f.facility_type
                FROM facilities f
                LEFT JOIN facility_billing_metrics fm ON fm.facility_id = f.facility_id
                WHERE f.facility_id = ?
                """,
                (facility_id,),
            ).fetchone()
    if not row:
        return None
    d = dict(row)
    d["name"] = _display_name(d.get("name"), d.get("facility_id"))
    d["city"] = _display_city(d.get("city"))
    d["state"] = state_display_name(d.get("state"))
    d["ownership_label"] = _ownership_display_label(d.get("ownership"))
    d["grade_color"] = _GRADE_COLORS.get(d.get("billing_grade") or "", "#9ca3af")
    d["grade_badge"] = _GRADE_BADGE.get(d.get("billing_grade") or "", "bg-gray-100 text-gray-600")
    d["facility_type"] = d.get("facility_type") or "hospital"
    d["has_transparency"] = bool(d.get("parse_status") in ("parsed", "partial"))
    charity = d.get("charity_care_pct_revenue") or d.get("charity_care_pct")
    d["charity_pct"] = round(float(charity), 1) if charity is not None else None
    d["has_financial_assistance"] = bool(
        d.get("has_financial_assistance_policy") or d.get("nonprofit_status") == 1 or d.get("is_nonprofit") == 1
    )
    return d


def get_common_procedures(fid_a: str, fid_b: str, limit: int = 20) -> list[dict]:
    """Return procedures priced by both facilities, sorted by biggest absolute price gap."""
    with get_db() as db:
        rows = db.execute(
            f"""
            {_ALL_PRICES_CTE}
            SELECT
                a.cpt_code,
                COALESCE(NULLIF(TRIM(a.description), ''), NULLIF(TRIM(b.description), '')) AS description,
                a.gross_charge AS charge_a,
                b.gross_charge AS charge_b,
                COALESCE(a.medicare_benchmark_rate, a.medicare_rate) AS medicare_rate,
                a.markup_vs_medicare AS markup_a,
                b.markup_vs_medicare AS markup_b
            FROM all_prices a
            JOIN all_prices b ON b.cpt_code = a.cpt_code AND b.facility_id = ?
            WHERE a.facility_id = ?
              AND a.gross_charge IS NOT NULL
              AND b.gross_charge IS NOT NULL
              AND COALESCE(a.medicare_benchmark_rate, a.medicare_rate) IS NOT NULL
              AND COALESCE(a.medicare_benchmark_rate, a.medicare_rate) > 0
            ORDER BY ABS(a.gross_charge - b.gross_charge) DESC
            LIMIT ?
            """,
            (fid_b, fid_a, limit),
        ).fetchall()

    result = []
    for row in rows:
        d = dict(row)
        cpt = d["cpt_code"]
        raw_desc = (d.get("description") or "").strip()
        d["name"] = FRIENDLY_CPT_DESCRIPTIONS.get(cpt) or (raw_desc.title() if raw_desc else f"CPT {cpt}")
        charge_a = d.get("charge_a") or 0.0
        charge_b = d.get("charge_b") or 0.0
        d["cheaper"] = "a" if charge_a <= charge_b else "b"
        d["savings"] = round(abs(charge_a - charge_b), 2)
        result.append(d)
    return result


def get_comparison_data(fid_a: str, fid_b: str) -> dict | None:
    """Return full comparison dict for two hospitals by facility_id."""
    h_a = get_hospital_for_compare(fid_a)
    h_b = get_hospital_for_compare(fid_b)
    if not h_a or not h_b:
        return None
    common = get_common_procedures(fid_a, fid_b)
    verdict = _build_verdict(h_a, h_b, common)
    distance_miles = _distance_between(h_a, h_b)
    map_data = _build_compare_map_data(h_a, h_b, distance_miles)
    return {
        "a": h_a,
        "b": h_b,
        "common_procedures": common,
        "verdict": verdict,
        "distance_miles": distance_miles,
        "map_data": map_data,
    }


def _distance_between(h_a: dict, h_b: dict) -> float | None:
    lat_a, lon_a = h_a.get("lat"), h_a.get("lon")
    lat_b, lon_b = h_b.get("lat"), h_b.get("lon")
    if None in (lat_a, lon_a, lat_b, lon_b):
        return None
    return round(_haversine(float(lat_a), float(lon_a), float(lat_b), float(lon_b)), 1)


def _haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 3958.8
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlam = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlam / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def _build_verdict(h_a: dict, h_b: dict, common: list[dict]) -> dict:
    grade_a = h_a.get("billing_grade")
    grade_b = h_b.get("billing_grade")
    markup_a = h_a.get("avg_markup_vs_medicare")
    markup_b = h_b.get("avg_markup_vs_medicare")
    gi_a = _grade_index(grade_a)
    gi_b = _grade_index(grade_b)
    name_a = h_a.get("name", "Hospital A")
    name_b = h_b.get("name", "Hospital B")

    if gi_a is not None and gi_b is not None:
        if gi_a < gi_b:
            winner = "a"
        elif gi_b < gi_a:
            winner = "b"
        else:
            winner = "tie"
    elif markup_a is not None and markup_b is not None:
        winner = "a" if markup_a < markup_b else ("b" if markup_b < markup_a else "tie")
    else:
        winner = "unknown"

    savings_a_over_b = sum(p["savings"] for p in common if p.get("cheaper") == "b")
    savings_b_over_a = sum(p["savings"] for p in common if p.get("cheaper") == "a")

    if winner == "a":
        cheaper_name = name_a
        grade_display = f"Grade {grade_a} vs {grade_b or 'N/A'}"
        summary = (
            f"{name_a} receives a billing grade of {grade_a or 'N/A'} compared to "
            f"{name_b}'s {grade_b or 'N/A'}. Based on markup vs Medicare, "
            f"{name_a} is the more fairly priced option."
        )
    elif winner == "b":
        cheaper_name = name_b
        grade_display = f"Grade {grade_b} vs {grade_a or 'N/A'}"
        summary = (
            f"{name_b} receives a billing grade of {grade_b or 'N/A'} compared to "
            f"{name_a}'s {grade_a or 'N/A'}. Based on markup vs Medicare, "
            f"{name_b} is the more fairly priced option."
        )
    elif winner == "tie":
        cheaper_name = None
        grade_display = f"Both Grade {grade_a}"
        summary = (
            f"Both hospitals share a billing grade of {grade_a or 'N/A'}. "
            f"Compare individual procedure prices below to find the better deal for your specific care."
        )
    else:
        cheaper_name = None
        grade_display = "Insufficient data"
        summary = "Not enough billing data to determine which hospital charges less. Review procedure prices below."

    return {
        "winner": winner,
        "cheaper_name": cheaper_name,
        "grade_display": grade_display,
        "summary": summary,
        "common_count": len(common),
        "savings_if_choose_a": round(savings_a_over_b, 2),
        "savings_if_choose_b": round(savings_b_over_a, 2),
    }


def _safe_float(value) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _build_compare_map_data(h_a: dict, h_b: dict, distance_miles: float | None) -> dict:
    if not ENABLE_FREE_MAPS:
        return {
            "available": False,
            "aria_label": f"Map comparing locations of {h_a.get('name')} and {h_b.get('name')}",
            "fallback_text": f"Map disabled for comparison between {h_a.get('name')} and {h_b.get('name')}.",
            "legend": "A <=2x · B 2-3x · C 3-5x · D 5-8x · F 8x+",
            "hospitals": [],
            "line": {"show": False, "distance_miles": distance_miles},
            "tile_max_zoom": 18,
        }

    lat_a, lon_a = _safe_float(h_a.get("lat")), _safe_float(h_a.get("lon"))
    lat_b, lon_b = _safe_float(h_b.get("lat")), _safe_float(h_b.get("lon"))
    available = None not in (lat_a, lon_a, lat_b, lon_b)

    marker_a = {
        "facility_id": h_a.get("facility_id"),
        "name": h_a.get("name"),
        "lat": lat_a,
        "lon": lon_a,
        "grade": h_a.get("billing_grade") or "N/A",
        "grade_color": h_a.get("grade_color") or "#9ca3af",
        "profile_url": f"/hospitals/{h_a.get('state_slug')}/{h_a.get('city_slug')}/{h_a.get('slug')}/",
    }
    marker_b = {
        "facility_id": h_b.get("facility_id"),
        "name": h_b.get("name"),
        "lat": lat_b,
        "lon": lon_b,
        "grade": h_b.get("billing_grade") or "N/A",
        "grade_color": h_b.get("grade_color") or "#9ca3af",
        "profile_url": f"/hospitals/{h_b.get('state_slug')}/{h_b.get('city_slug')}/{h_b.get('slug')}/",
    }
    line = {
        "show": bool(distance_miles is not None and distance_miles <= 100 and available),
        "distance_miles": distance_miles,
    }
    fallback_text = (
        f"Map compares {h_a.get('name')} and {h_b.get('name')}. "
        f"Distance between hospitals: {distance_miles} miles."
        if distance_miles is not None
        else f"Map compares {h_a.get('name')} and {h_b.get('name')}."
    )
    return {
        "available": available,
        "aria_label": f"Map comparing locations of {h_a.get('name')} and {h_b.get('name')}",
        "fallback_text": fallback_text,
        "legend": "A <=2x · B 2-3x · C 3-5x · D 5-8x · F 8x+",
        "hospitals": [marker_a, marker_b],
        "line": line,
        "tile_max_zoom": 18,
    }
