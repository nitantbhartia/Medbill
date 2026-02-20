"""Procedure cost page helpers — data queries and deterministic content generation."""

from __future__ import annotations

import math
import re

from db import get_db

_PROCEDURE_RADIUS_MILES = 75.0
_EARTH_RADIUS_MILES = 3958.8

# Friendly consumer names for common CPT codes
_FRIENDLY_NAMES: dict[str, str] = {
    "10060": "Abscess Drainage",
    "11042": "Wound Debridement",
    "20610": "Joint Injection",
    "22551": "Cervical Spine Fusion",
    "23472": "Shoulder Replacement",
    "27130": "Total Hip Replacement",
    "27236": "Hip Fracture Repair",
    "27447": "Total Knee Replacement",
    "29881": "Knee Arthroscopy",
    "43239": "Upper GI Endoscopy with Biopsy",
    "45378": "Colonoscopy",
    "70450": "Head CT Scan",
    "70553": "Brain MRI with Contrast",
    "71045": "Chest X-Ray",
    "71250": "Chest CT Scan",
    "73221": "Wrist MRI",
    "73223": "Shoulder MRI",
    "73721": "Knee MRI",
    "74178": "Abdominal CT Scan",
    "74177": "Abdominal CT with Contrast",
    "74183": "Abdominal MRI with Contrast",
    "76700": "Abdominal Ultrasound",
    "76805": "Obstetric Ultrasound",
    "80053": "Comprehensive Metabolic Panel",
    "80061": "Lipid Panel",
    "85025": "Complete Blood Count",
    "93000": "Electrocardiogram (ECG)",
}

_GRADE_COLORS = {
    "A": "#22c55e", "B": "#84cc16", "C": "#f59e0b", "D": "#f97316", "F": "#ef4444",
}
_GRADE_BADGE_CLASSES = {
    "A": "bg-green-100 text-green-700",
    "B": "bg-lime-100 text-lime-700",
    "C": "bg-yellow-100 text-yellow-700",
    "D": "bg-orange-100 text-orange-700",
    "F": "bg-red-100 text-red-700",
}
_FACILITY_TYPE_LABELS = {
    "hospital": "Hospital",
    "asc": "Surgery Center",
    "imaging_center": "Imaging Center",
}
_BENCHMARK_TYPE_LABELS = {
    "opps": "Medicare OPPS",
    "asc": "Medicare ASC",
    "pfs": "Physician Fee Schedule",
    "clfs": "Clinical Lab Fee Schedule",
}
_ALL_PRICES_CTE = """
WITH all_prices AS (
    SELECT
        facility_id, cpt_code, description, gross_charge, cash_price,
        min_negotiated_rate, max_negotiated_rate, avg_negotiated_rate,
        medicare_rate, markup_vs_medicare, data_year,
        facility_type, medicare_benchmark_type, medicare_benchmark_rate
    FROM procedure_prices
    UNION ALL
    SELECT
        hp.facility_id, hp.cpt_code, hp.description, hp.gross_charge, hp.cash_price,
        hp.min_negotiated_rate, hp.max_negotiated_rate, hp.avg_negotiated_rate,
        hp.medicare_rate, hp.markup_vs_medicare, hp.data_year,
        hp.facility_type, hp.medicare_benchmark_type, hp.medicare_benchmark_rate
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
_BODY_SYSTEMS: list[tuple[int, int, str]] = [
    (10000, 19999, "Skin & Soft Tissue"),
    (20000, 29999, "Musculoskeletal"),
    (30000, 39999, "Respiratory"),
    (40000, 49999, "Digestive"),
    (50000, 59999, "Urinary"),
    (60000, 69999, "Endocrine & Nervous"),
    (70000, 79999, "Radiology & Imaging"),
    (80000, 89999, "Laboratory"),
    (90000, 99999, "Medicine"),
]


def _body_system(cpt_code: str) -> str:
    try:
        n = int(cpt_code)
    except (ValueError, TypeError):
        return "Other"
    for lo, hi, name in _BODY_SYSTEMS:
        if lo <= n <= hi:
            return name
    return "Other"


def _classify_cpt(cpt_code: str) -> str:
    """Return 'imaging', 'surgical', or 'outpatient'."""
    try:
        n = int(cpt_code)
    except (ValueError, TypeError):
        return "outpatient"
    if 70000 <= n <= 79999:
        return "imaging"
    if 10000 <= n <= 69999:
        return "surgical"
    return "outpatient"


def _facility_type_for_cpt(cpt_code: str) -> str:
    t = _classify_cpt(cpt_code)
    if t == "imaging":
        return "imaging_center"
    if t == "surgical":
        return "asc"
    return "hospital"


def _parse_sort(sort_by: str) -> str:
    value = (sort_by or "").strip().lower()
    return value if value in {"patient_cost", "markup"} else "patient_cost"


def _provider_profile_url(row: dict) -> str:
    state_slug = row.get("state_slug") or ""
    city_slug = row.get("city_slug") or ""
    slug = row.get("slug") or ""
    ftype = row.get("facility_type") or "hospital"
    if ftype == "asc":
        return f"/surgery-centers/{state_slug}/{city_slug}/{slug}/"
    if ftype == "imaging_center":
        return f"/imaging/{state_slug}/{city_slug}/{slug}/"
    return f"/hospitals/{state_slug}/{city_slug}/{slug}/"


def _friendly_name(cpt_code: str, raw_description: str) -> str:
    if cpt_code in _FRIENDLY_NAMES:
        return _FRIENDLY_NAMES[cpt_code]
    desc = (raw_description or "").strip()
    if not desc:
        return f"CPT {cpt_code}"
    # Truncate to 60 chars at word boundary
    def _format_desc(text: str) -> str:
        out = text.title()
        out = re.sub(r"\bMri\b", "MRI", out)
        out = re.sub(r"\bCt\b", "CT", out)
        out = re.sub(r"\bEcg\b", "ECG", out)
        out = re.sub(r"\bGi\b", "GI", out)
        out = re.sub(r"\bEr\b", "ER", out)
        return out

    if len(desc) <= 60:
        return _format_desc(desc)
    return _format_desc(desc[:57].rsplit(" ", 1)[0]) + "..."


def _quantile(values_sorted: list[float], p: float) -> float:
    if not values_sorted:
        return 0.0
    p = max(0.0, min(1.0, p))
    idx = int((len(values_sorted) - 1) * p)
    return float(values_sorted[idx])


def _trim_outlier_rows(rows: list[dict], value_key: str = "gross_charge") -> tuple[list[dict], int]:
    sane_rows = [
        r for r in rows
        if r.get(value_key) is not None
        and float(r[value_key]) > 0
        and float(r[value_key]) <= 1_000_000.0
    ]
    sanity_removed = len(rows) - len(sane_rows)
    values = sorted(float(r[value_key]) for r in sane_rows)
    n = len(values)
    if n < 12:
        return sane_rows if sane_rows else rows, sanity_removed
    q1 = _quantile(values, 0.25)
    q3 = _quantile(values, 0.75)
    iqr = max(q3 - q1, 0.0)
    upper = q3 + (3.0 * iqr)
    if upper <= 0:
        return rows, 0
    trimmed = [r for r in sane_rows if r.get(value_key) is not None and float(r[value_key]) <= upper]
    removed = len(sane_rows) - len(trimmed)
    if removed <= 0:
        return sane_rows if sane_rows else rows, sanity_removed
    # Guardrail: if filter is too aggressive, keep raw rows.
    if removed > int(len(sane_rows) * 0.30):
        return sane_rows if sane_rows else rows, sanity_removed
    return trimmed, removed + sanity_removed


def _procedure_description(name: str, cpt_code: str, procedure_type: str) -> str:
    if procedure_type == "imaging":
        return (
            f"{name} (CPT {cpt_code}) is a diagnostic imaging scan that gives physicians "
            f"detailed views of internal structures without surgery. It is typically ordered "
            f"to evaluate an injury, disease, or condition that cannot be fully assessed through "
            f"a physical exam alone. The scan usually takes 15 to 60 minutes to complete."
        )
    if procedure_type == "surgical":
        return (
            f"{name} (CPT {cpt_code}) is a surgical procedure typically performed in a hospital "
            f"or accredited outpatient surgical center. It is usually recommended after more "
            f"conservative treatments—such as medication or physical therapy—have not resolved "
            f"the underlying problem. Recovery time ranges from a few days to several weeks "
            f"depending on patient health and procedure complexity."
        )
    return (
        f"{name} (CPT {cpt_code}) is an outpatient procedure or diagnostic test performed in "
        f"a hospital, clinic, or ambulatory care setting. It is typically completed in a single "
        f"visit, and most patients return to normal activities the same day or within 24 hours."
    )


def _grade_badge_class(grade: str | None) -> str:
    return _GRADE_BADGE_CLASSES.get(grade or "", "bg-gray-100 text-gray-600")


def _haversine_miles(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlam = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlam / 2) ** 2
    return 2 * _EARTH_RADIUS_MILES * math.asin(math.sqrt(a))


def get_zip_latlon(zip_code: str) -> tuple[float, float] | None:
    clean = (zip_code or "").strip()[:5]
    if not clean.isdigit():
        return None
    with get_db() as db:
        try:
            row = db.execute(
                "SELECT lat, lon FROM zip_latlon WHERE zip = ? LIMIT 1", (clean,)
            ).fetchone()
        except Exception:
            return None
    return (float(row["lat"]), float(row["lon"])) if row else None


def _resolve_state_from_zip(zip_code: str) -> str | None:
    clean = (zip_code or "").strip()[:5]
    if len(clean) != 5 or not clean.isdigit():
        return None
    prefix = clean[:3]
    with get_db() as db:
        # Prefer explicit ZIP centroid mapping when available.
        row = db.execute(
            "SELECT state FROM zip_latlon WHERE zip = ? AND state IS NOT NULL AND trim(state) <> '' LIMIT 1",
            (clean,),
        ).fetchone()
        if row and row["state"]:
            return str(row["state"]).strip().upper()

        # Fallback to ZIP prefix -> state mapping used by locality benchmarks.
        row = db.execute(
            "SELECT state FROM zip_locality_map WHERE zip_prefix = ? AND state IS NOT NULL AND trim(state) <> '' LIMIT 1",
            (prefix,),
        ).fetchone()
        if row and row["state"]:
            return str(row["state"]).strip().upper()

        # Last resort: infer from facilities/hospitals that carry this exact ZIP.
        row = db.execute(
            """
            SELECT state, COUNT(*) AS cnt
            FROM (
                SELECT UPPER(state) AS state
                FROM facilities
                WHERE zip IS NOT NULL
                  AND substr(zip, 1, 5) = ?
                  AND state IS NOT NULL
                  AND trim(state) <> ''
                UNION ALL
                SELECT UPPER(state) AS state
                FROM hospitals
                WHERE zip IS NOT NULL
                  AND substr(zip, 1, 5) = ?
                  AND state IS NOT NULL
                  AND trim(state) <> ''
            ) s
            GROUP BY state
            ORDER BY cnt DESC, state ASC
            LIMIT 1
            """,
            (clean, clean),
        ).fetchone()
        if row and row["state"]:
            return str(row["state"]).strip().upper()
    return None


def get_top_cpt_codes(limit: int = 100) -> list[dict]:
    """Return top CPT codes ranked by provider coverage, with basic stats."""
    with get_db() as db:
        rows = db.execute(
            f"""
            {_ALL_PRICES_CTE}
            SELECT
                hp.cpt_code,
                COUNT(DISTINCT hp.facility_id) AS provider_count,
                AVG(hp.gross_charge) AS avg_charge,
                AVG(COALESCE(hp.medicare_benchmark_rate, hp.medicare_rate)) AS avg_medicare_rate,
                AVG(hp.markup_vs_medicare) AS avg_markup,
                (AVG(hp.markup_vs_medicare * hp.markup_vs_medicare)
                 - AVG(hp.markup_vs_medicare) * AVG(hp.markup_vs_medicare)) AS markup_variance,
                COALESCE(
                    NULLIF(TRIM(hp.description), ''),
                    (SELECT mr.description FROM medicare_rates mr
                     WHERE mr.cpt_code = hp.cpt_code
                       AND mr.description IS NOT NULL
                     ORDER BY mr.effective_year DESC LIMIT 1)
                ) AS description
            FROM all_prices hp
            WHERE hp.gross_charge IS NOT NULL
              AND COALESCE(hp.medicare_benchmark_rate, hp.medicare_rate) IS NOT NULL
              AND COALESCE(hp.medicare_benchmark_rate, hp.medicare_rate) > 0
              AND hp.markup_vs_medicare IS NOT NULL
            GROUP BY hp.cpt_code
            ORDER BY provider_count DESC, markup_variance DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    result = []
    for row in rows:
        d = dict(row)
        cpt = d["cpt_code"]
        name = _friendly_name(cpt, d.get("description") or "")
        result.append({
            **d,
            # Backward compatible alias used by templates/tests.
            "hospital_count": d.get("provider_count", 0),
            "name": name,
            "body_system": _body_system(cpt),
            "procedure_type": _classify_cpt(cpt),
        })
    return result


def get_procedure_profile(cpt_code: str) -> dict | None:
    """Return full data dict for a procedure detail page."""
    resolved_rate_expr = """
    COALESCE(
        hp.medicare_benchmark_rate,
        hp.medicare_rate,
        (
            SELECT mr.facility_rate
            FROM medicare_rates mr
            WHERE mr.cpt_code = hp.cpt_code
              AND mr.facility_rate IS NOT NULL
            ORDER BY mr.effective_year DESC
            LIMIT 1
        )
    )
    """
    resolved_markup_expr = f"""
    COALESCE(
        hp.markup_vs_medicare,
        CASE
            WHEN ({resolved_rate_expr}) > 0 THEN hp.gross_charge / ({resolved_rate_expr})
            ELSE NULL
        END
    )
    """
    with get_db() as db:
        detail_rows = db.execute(
            f"""
            {_ALL_PRICES_CTE}
            SELECT
                hp.facility_id,
                hp.gross_charge,
                {resolved_rate_expr} AS medicare_rate,
                {resolved_markup_expr} AS markup_vs_medicare,
                COALESCE(fm.billing_grade, m.billing_grade) AS billing_grade,
                COALESCE(f.facility_type, hp.facility_type, 'hospital') AS facility_type,
                COALESCE(
                    NULLIF(TRIM(hp.description), ''),
                    (SELECT mr.description FROM medicare_rates mr
                     WHERE mr.cpt_code = hp.cpt_code
                       AND mr.description IS NOT NULL
                     ORDER BY mr.effective_year DESC LIMIT 1)
                ) AS description
            FROM all_prices hp
            LEFT JOIN facilities f ON f.facility_id = hp.facility_id
            LEFT JOIN facility_billing_metrics fm ON fm.facility_id = hp.facility_id
            LEFT JOIN billing_metrics m ON m.facility_id = hp.facility_id
            WHERE hp.cpt_code = ?
              AND hp.gross_charge IS NOT NULL
              AND ({resolved_rate_expr}) IS NOT NULL
              AND ({resolved_rate_expr}) > 0
            """,
            (cpt_code,),
        ).fetchall()

        if not detail_rows:
            return None

        cheapest = db.execute(
            f"""
            {_ALL_PRICES_CTE}
            SELECT
                COALESCE(f.name, h.name) AS name,
                COALESCE(f.city, h.city) AS city,
                COALESCE(f.state, h.state) AS state,
                COALESCE(f.state_slug, h.state_slug) AS state_slug,
                COALESCE(f.city_slug, h.city_slug) AS city_slug,
                COALESCE(f.slug, h.slug) AS slug,
                COALESCE(f.facility_type, hp.facility_type, 'hospital') AS facility_type,
                COALESCE(fm.billing_grade, m.billing_grade) AS billing_grade,
                COALESCE(f.is_hospital_owned, 0) AS is_hospital_owned,
                hp.gross_charge,
                {resolved_rate_expr} AS medicare_rate,
                COALESCE(hp.medicare_benchmark_type, CASE WHEN COALESCE(f.facility_type, hp.facility_type, 'hospital') = 'asc' THEN 'asc' ELSE 'opps' END) AS medicare_benchmark_type,
                {resolved_markup_expr} AS markup_vs_medicare
            FROM all_prices hp
            LEFT JOIN facilities f ON f.facility_id = hp.facility_id
            LEFT JOIN hospitals h ON h.facility_id = hp.facility_id
            LEFT JOIN facility_billing_metrics fm ON fm.facility_id = hp.facility_id
            LEFT JOIN billing_metrics m ON m.facility_id = hp.facility_id
            WHERE hp.cpt_code = ?
              AND hp.gross_charge IS NOT NULL
              AND ({resolved_markup_expr}) IS NOT NULL
              AND COALESCE(f.name, h.name) IS NOT NULL
            ORDER BY ({resolved_markup_expr}) ASC
            LIMIT 30
            """,
            (cpt_code,),
        ).fetchall()

        try:
            cpt_n = int(cpt_code)
            related_rows = db.execute(
                f"""
                {_ALL_PRICES_CTE}
                SELECT
                    hp.cpt_code,
                    COUNT(DISTINCT hp.facility_id) AS hospital_count,
                    AVG(hp.gross_charge) AS avg_charge,
                    COALESCE(
                        NULLIF(TRIM(hp.description), ''),
                        (SELECT mr.description FROM medicare_rates mr
                         WHERE mr.cpt_code = hp.cpt_code
                           AND mr.description IS NOT NULL
                         ORDER BY mr.effective_year DESC LIMIT 1)
                    ) AS description
                FROM all_prices hp
                WHERE hp.cpt_code != ?
                  AND CAST(hp.cpt_code AS INTEGER) BETWEEN ? AND ?
                  AND hp.gross_charge IS NOT NULL
                GROUP BY hp.cpt_code
                ORDER BY hospital_count DESC
                LIMIT 3
                """,
                (cpt_code, cpt_n - 5000, cpt_n + 5000),
            ).fetchall()
        except (ValueError, TypeError):
            related_rows = []

    detail = [dict(r) for r in detail_rows]
    filtered_detail, excluded_outliers = _trim_outlier_rows(detail, "gross_charge")
    if not filtered_detail:
        filtered_detail = detail
        excluded_outliers = 0

    provider_ids = {r["facility_id"] for r in filtered_detail if r.get("facility_id")}
    avg_charge = (sum(float(r["gross_charge"]) for r in filtered_detail) / len(filtered_detail)) if filtered_detail else None
    avg_medicare_rate = (
        sum(float(r["medicare_rate"]) for r in filtered_detail) / len(filtered_detail)
        if filtered_detail
        else None
    )
    markups = [float(r["markup_vs_medicare"]) for r in filtered_detail if r.get("markup_vs_medicare") is not None]
    header = {
        "provider_count": len(provider_ids),
        "avg_charge": avg_charge,
        "avg_medicare_rate": avg_medicare_rate,
        "min_charge": min(float(r["gross_charge"]) for r in filtered_detail) if filtered_detail else None,
        "max_charge": max(float(r["gross_charge"]) for r in filtered_detail) if filtered_detail else None,
        "avg_markup": (sum(markups) / len(markups)) if markups else None,
        "description": next((r.get("description") for r in filtered_detail if (r.get("description") or "").strip()), None),
        "excluded_outliers": excluded_outliers,
    }
    desc_raw = header.get("description") or ""
    name = _friendly_name(cpt_code, desc_raw)
    procedure_type = _classify_cpt(cpt_code)
    medicare_rate = header.get("avg_medicare_rate")
    avg_charge = header.get("avg_charge")

    by_grade_map: dict[str, list[dict]] = {}
    for r in filtered_detail:
        g = (r.get("billing_grade") or "").strip()
        if not g:
            continue
        by_grade_map.setdefault(g, []).append(r)
    by_grade = []
    for grade in sorted(by_grade_map):
        rows = by_grade_map[grade]
        g_charge = sum(float(r["gross_charge"]) for r in rows) / len(rows)
        g_medicare = sum(float(r["medicare_rate"]) for r in rows) / len(rows)
        by_grade.append(
            {
                "billing_grade": grade,
                "avg_charge": g_charge,
                "avg_medicare_rate": g_medicare,
                "provider_count": len(rows),
                "hospital_count": len(rows),
                "patient_cost": round(g_charge * 0.20, 2),
                "color": _GRADE_COLORS.get(grade, "#9ca3af"),
                "badge_class": _grade_badge_class(grade),
            }
        )

    cheapest_list = [
        {
            **dict(r),
            "facility_type_label": _FACILITY_TYPE_LABELS.get(r["facility_type"] or "hospital", "Provider"),
            "benchmark_label": _BENCHMARK_TYPE_LABELS.get(r["medicare_benchmark_type"] or "opps", "Medicare"),
            "ownership_badge": "Hospital-owned" if r["is_hospital_owned"] else "Independent",
            "profile_url": _provider_profile_url(dict(r)),
            "badge_class": _grade_badge_class(r["billing_grade"]),
        }
        for r in cheapest
    ][:10]

    by_type_map: dict[str, list[dict]] = {}
    for r in filtered_detail:
        if r.get("markup_vs_medicare") is None:
            continue
        ftype = (r.get("facility_type") or "hospital").strip().lower()
        by_type_map.setdefault(ftype, []).append(r)

    ranges_by_type = []
    for ftype, rows in by_type_map.items():
        if ftype not in {"hospital", "asc", "imaging_center"}:
            continue
        charges = [float(r["gross_charge"]) for r in rows]
        type_markups = [float(r["markup_vs_medicare"]) for r in rows if r.get("markup_vs_medicare") is not None]
        ranges_by_type.append(
            {
                "facility_type": ftype,
                "provider_count": len(rows),
                "min_charge": min(charges),
                "max_charge": max(charges),
                "avg_charge": sum(charges) / len(charges),
                "avg_markup": (sum(type_markups) / len(type_markups)) if type_markups else None,
                "facility_type_label": _FACILITY_TYPE_LABELS.get(ftype, ftype.title()),
                "benchmark_label": "ASC rate" if ftype == "asc" else "Medicare",
            }
        )

    related = [
        {
            "cpt_code": r["cpt_code"],
            "name": _friendly_name(r["cpt_code"], r["description"] or ""),
            "hospital_count": r["hospital_count"],
            "avg_charge": r["avg_charge"],
        }
        for r in related_rows
    ]

    # SVG range bar: positions as 0.0–1.0 fractions within min–max span
    min_c = header.get("min_charge") or 0.0
    max_c = header.get("max_charge") or 1.0
    span = max(max_c - min_c, 1.0)

    def _pos(v: float | None) -> float | None:
        if v is None:
            return None
        return max(0.0, min(1.0, (v - min_c) / span))

    range_bar = {
        "min_charge": min_c,
        "max_charge": max_c,
        "avg_charge": avg_charge,
        "medicare_rate": medicare_rate,
        "medicare_pos": _pos(medicare_rate),
        "avg_pos": _pos(avg_charge),
        "zone_a_end": _pos(medicare_rate * 2.0) if medicare_rate else None,
        "zone_b_end": _pos(medicare_rate * 3.0) if medicare_rate else None,
        "zone_c_end": _pos(medicare_rate * 5.0) if medicare_rate else None,
        "zone_d_end": _pos(medicare_rate * 8.0) if medicare_rate else None,
    }

    return {
        "cpt_code": cpt_code,
        "name": name,
        "description": _procedure_description(name, cpt_code, procedure_type),
        "procedure_type": procedure_type,
        "body_system": _body_system(cpt_code),
        "header": {
            "medicare_rate": medicare_rate,
            "national_avg_charge": avg_charge,
            "provider_count": header["provider_count"],
            "hospital_count": header["provider_count"],
            "avg_markup": header.get("avg_markup"),
            "excluded_outliers": header.get("excluded_outliers", 0),
        },
        "by_grade": by_grade,
        "range_bar": range_bar,
        "cheapest_hospitals": [r for r in cheapest_list if r.get("facility_type") == "hospital"][:10],
        "cheapest_providers": cheapest_list,
        "ranges_by_type": ranges_by_type,
        "faq": _build_procedure_faq(name, cpt_code, procedure_type, medicare_rate, avg_charge),
        "related": related,
        "seo": _build_procedure_seo(name, cpt_code, medicare_rate, avg_charge, header["provider_count"]),
    }


def get_providers_near_zip_for_cpt(
    cpt_code: str,
    zip_code: str,
    limit: int = 10,
    facility_type: str = "all",
    grade_ab_only: bool = False,
    sort_by: str = "patient_cost",
    radius_miles: float = _PROCEDURE_RADIUS_MILES,
) -> list[dict]:
    """Return up to `limit` providers near zip for a CPT code across facility types."""
    coords = get_zip_latlon(zip_code)
    if not coords:
        return _get_providers_without_zip_coords(
            cpt_code=cpt_code,
            zip_code=zip_code,
            limit=limit,
            facility_type=facility_type,
            grade_ab_only=grade_ab_only,
            sort_by=sort_by,
        )
    zip_lat, zip_lon = coords
    radius = max(5.0, min(float(radius_miles or _PROCEDURE_RADIUS_MILES), 200.0))
    lat_delta = radius / 69.0
    lon_delta = radius / max(69.17 * math.cos(math.radians(zip_lat)), 0.1)
    sort_key = _parse_sort(sort_by)
    normalized_type = (facility_type or "all").strip().lower()
    allowed = {"all", "hospital", "asc", "imaging_center"}
    if normalized_type not in allowed:
        normalized_type = "all"

    with get_db() as db:
        where_type = ""
        params: list = [cpt_code]
        params.extend(
            [
                zip_lat - lat_delta,
                zip_lat + lat_delta,
                zip_lon - lon_delta,
                zip_lon + lon_delta,
            ]
        )
        if normalized_type != "all":
            where_type = " AND COALESCE(f.facility_type, hp.facility_type, 'hospital') = ?"
            params.append(normalized_type)
        candidates = db.execute(
            f"""
            {_ALL_PRICES_CTE}
            SELECT
                COALESCE(f.name, h.name) AS name,
                COALESCE(f.city, h.city) AS city,
                COALESCE(f.state, h.state) AS state,
                COALESCE(f.state_slug, h.state_slug) AS state_slug,
                COALESCE(f.city_slug, h.city_slug) AS city_slug,
                COALESCE(f.slug, h.slug) AS slug,
                COALESCE(f.facility_type, hp.facility_type, 'hospital') AS facility_type,
                COALESCE(f.lat, h.lat) AS lat,
                COALESCE(f.lon, h.lon) AS lon,
                COALESCE(fm.billing_grade, m.billing_grade) AS billing_grade,
                COALESCE(f.is_hospital_owned, 0) AS is_hospital_owned,
                hp.gross_charge,
                COALESCE(hp.medicare_benchmark_rate, hp.medicare_rate) AS medicare_rate,
                COALESCE(hp.medicare_benchmark_type, CASE WHEN COALESCE(f.facility_type, hp.facility_type, 'hospital') = 'asc' THEN 'asc' ELSE 'opps' END) AS medicare_benchmark_type,
                hp.markup_vs_medicare
            FROM all_prices hp
            LEFT JOIN facilities f ON f.facility_id = hp.facility_id
            LEFT JOIN hospitals h ON h.facility_id = hp.facility_id
            LEFT JOIN facility_billing_metrics fm ON fm.facility_id = hp.facility_id
            LEFT JOIN billing_metrics m ON m.facility_id = hp.facility_id
            WHERE hp.cpt_code = ?
              AND hp.gross_charge IS NOT NULL
              AND hp.markup_vs_medicare IS NOT NULL
              AND COALESCE(f.lat, h.lat) BETWEEN ? AND ?
              AND COALESCE(f.lon, h.lon) BETWEEN ? AND ?
              AND COALESCE(f.name, h.name) IS NOT NULL
              {where_type}
            ORDER BY hp.gross_charge ASC
            LIMIT 250
            """,
            tuple(params),
        ).fetchall()

    results = []
    for row in candidates:
        if row["lat"] is None or row["lon"] is None:
            continue
        dist = _haversine_miles(zip_lat, zip_lon, row["lat"], row["lon"])
        if dist <= radius:
            if grade_ab_only and (row["billing_grade"] or "").upper() not in {"A", "B"}:
                continue
            charge = row["gross_charge"] or 0.0
            results.append({
                **dict(row),
                "facility_type_label": _FACILITY_TYPE_LABELS.get(row["facility_type"] or "hospital", "Provider"),
                "ownership_badge": "Hospital-owned" if row["is_hospital_owned"] else "Independent",
                "benchmark_label": _BENCHMARK_TYPE_LABELS.get(row["medicare_benchmark_type"] or "opps", "Medicare"),
                "profile_url": _provider_profile_url(dict(row)),
                "estimated_patient_cost": round(charge * 0.20, 2) if charge else None,
                "distance_miles": round(dist, 1),
                "badge_class": _grade_badge_class(row["billing_grade"]),
            })

    if sort_key == "markup":
        results.sort(key=lambda r: (r["markup_vs_medicare"] is None, r["markup_vs_medicare"] or 0.0))
    else:
        results.sort(key=lambda r: (r["estimated_patient_cost"] is None, r["estimated_patient_cost"] or 0.0))
    return results[:limit]


def _get_providers_without_zip_coords(
    cpt_code: str,
    zip_code: str,
    limit: int,
    facility_type: str,
    grade_ab_only: bool,
    sort_by: str,
) -> list[dict]:
    sort_key = _parse_sort(sort_by)
    normalized_type = (facility_type or "all").strip().lower()
    allowed = {"all", "hospital", "asc", "imaging_center"}
    if normalized_type not in allowed:
        normalized_type = "all"
    zip_clean = (zip_code or "").strip()[:5]
    state = _resolve_state_from_zip(zip_clean)
    if zip_clean and state is None:
        # Avoid showing misleading nationwide "nearby" results when geo resolution fails.
        return []

    with get_db() as db:
        where_type = ""
        where_state = ""
        params: list = [cpt_code]
        if state:
            where_state = " AND UPPER(COALESCE(f.state, h.state)) = ?"
            params.append(state)
        if normalized_type != "all":
            where_type = " AND COALESCE(f.facility_type, hp.facility_type, 'hospital') = ?"
            params.append(normalized_type)
        candidates = db.execute(
            f"""
            {_ALL_PRICES_CTE}
            SELECT
                COALESCE(f.name, h.name) AS name,
                COALESCE(f.city, h.city) AS city,
                COALESCE(f.state, h.state) AS state,
                COALESCE(f.state_slug, h.state_slug) AS state_slug,
                COALESCE(f.city_slug, h.city_slug) AS city_slug,
                COALESCE(f.slug, h.slug) AS slug,
                COALESCE(f.facility_type, hp.facility_type, 'hospital') AS facility_type,
                COALESCE(fm.billing_grade, m.billing_grade) AS billing_grade,
                COALESCE(f.is_hospital_owned, 0) AS is_hospital_owned,
                hp.gross_charge,
                COALESCE(hp.medicare_benchmark_rate, hp.medicare_rate) AS medicare_rate,
                COALESCE(hp.medicare_benchmark_type, CASE WHEN COALESCE(f.facility_type, hp.facility_type, 'hospital') = 'asc' THEN 'asc' ELSE 'opps' END) AS medicare_benchmark_type,
                hp.markup_vs_medicare
            FROM all_prices hp
            LEFT JOIN facilities f ON f.facility_id = hp.facility_id
            LEFT JOIN hospitals h ON h.facility_id = hp.facility_id
            LEFT JOIN facility_billing_metrics fm ON fm.facility_id = hp.facility_id
            LEFT JOIN billing_metrics m ON m.facility_id = hp.facility_id
            WHERE hp.cpt_code = ?
              AND hp.gross_charge IS NOT NULL
              AND hp.markup_vs_medicare IS NOT NULL
              AND COALESCE(f.name, h.name) IS NOT NULL
              {where_state}
              {where_type}
            ORDER BY hp.gross_charge ASC
            LIMIT 500
            """,
            tuple(params),
        ).fetchall()

    results = []
    for row in candidates:
        if grade_ab_only and (row["billing_grade"] or "").upper() not in {"A", "B"}:
            continue
        charge = row["gross_charge"] or 0.0
        results.append({
            **dict(row),
            "facility_type_label": _FACILITY_TYPE_LABELS.get(row["facility_type"] or "hospital", "Provider"),
            "ownership_badge": "Hospital-owned" if row["is_hospital_owned"] else "Independent",
            "benchmark_label": _BENCHMARK_TYPE_LABELS.get(row["medicare_benchmark_type"] or "opps", "Medicare"),
            "profile_url": _provider_profile_url(dict(row)),
            "estimated_patient_cost": round(charge * 0.20, 2) if charge else None,
            "distance_miles": None,
            "badge_class": _grade_badge_class(row["billing_grade"]),
        })

    if sort_key == "markup":
        results.sort(key=lambda r: (r["markup_vs_medicare"] is None, r["markup_vs_medicare"] or 0.0))
    else:
        results.sort(key=lambda r: (r["estimated_patient_cost"] is None, r["estimated_patient_cost"] or 0.0))
    return results[:limit]


def get_hospitals_near_zip_for_cpt(cpt_code: str, zip_code: str, limit: int = 10) -> list[dict]:
    """Backward-compatible wrapper for hospital-only provider search."""
    return get_providers_near_zip_for_cpt(
        cpt_code=cpt_code,
        zip_code=zip_code,
        limit=limit,
        facility_type="hospital",
        grade_ab_only=False,
        sort_by="patient_cost",
        radius_miles=_PROCEDURE_RADIUS_MILES,
    )


def _build_procedure_faq(
    name: str,
    cpt_code: str,
    procedure_type: str,
    medicare_rate: float | None,
    avg_charge: float | None,
) -> list[dict]:
    rate_str = f"${medicare_rate:,.0f}" if medicare_rate else "the Medicare rate"
    avg_str = f"${avg_charge:,.0f}" if avg_charge else "the national average"
    two_x_str = f"${medicare_rate * 2:,.0f}" if medicare_rate else "two times Medicare"
    patient_cost_str = f"${avg_charge * 0.20:,.0f}" if avg_charge else "a significant portion"

    if procedure_type == "imaging":
        return [
            {
                "q": f"Why does {name} cost so much more at some hospitals than others?",
                "a": (
                    f"Hospital charges for {name} (CPT {cpt_code}) vary dramatically—sometimes "
                    f"by 10x or more—because hospitals set their own gross charges independently. "
                    f"Medicare pays {rate_str} for this procedure based on actual delivery costs, "
                    f"but hospitals are not required to match that rate. The national average charge "
                    f"is {avg_str}. Using a price transparency tool helps you find a fairly priced facility."
                ),
            },
            {
                "q": f"Can I shop around for {name} if my doctor ordered it?",
                "a": (
                    f"Yes. As long as the same CPT code ({cpt_code}) is billed, the ordering physician "
                    f"does not need to be at the same facility that performs the scan. You can call "
                    f"hospitals and freestanding imaging centers to ask for their cash price or "
                    f"expected out-of-pocket cost before scheduling. Freestanding imaging centers "
                    f"typically charge significantly less than hospital outpatient departments."
                ),
            },
            {
                "q": f"What should I do if I received a bill for {name} that seems high?",
                "a": (
                    f"Compare the charge on your bill to the Medicare reference rate of {rate_str}. "
                    f"If the hospital billed more than {two_x_str} (two times Medicare), you may be "
                    f"able to negotiate. Request an itemized bill, check for duplicate charges, and "
                    f"ask whether a prompt-pay or financial hardship discount applies. You can also "
                    f"upload your bill to BillKarma for a free automated review."
                ),
            },
        ]

    if procedure_type == "surgical":
        return [
            {
                "q": f"How much does {name} cost with insurance?",
                "a": (
                    f"With insurance, your out-of-pocket cost for {name} (CPT {cpt_code}) depends "
                    f"on your deductible, coinsurance rate, and in-network status. Medicare pays "
                    f"{rate_str} for this procedure; the national average hospital charge is {avg_str}. "
                    f"Under standard 20% coinsurance after deductible, a patient at an average-charging "
                    f"hospital would owe approximately {patient_cost_str}. Always verify your benefits "
                    f"before scheduling."
                ),
            },
            {
                "q": f"Does where I have {name} done affect my recovery?",
                "a": (
                    f"Hospital quality and surgical volume can influence outcomes for procedures like "
                    f"{name}. High-volume centers tend to have lower complication rates for complex "
                    f"surgeries. However, billing grade is separate from quality ratings—some highly "
                    f"graded billing hospitals also have strong clinical outcomes. Review both the "
                    f"BillKarma billing grade and CMS quality stars when choosing a facility."
                ),
            },
            {
                "q": f"How do I negotiate the cost of {name} if I'm on a high-deductible plan?",
                "a": (
                    f"If you're paying a significant portion out-of-pocket, ask the hospital for their "
                    f"cash price before scheduling. Many hospitals offer 10–40% discounts for self-pay "
                    f"patients. Medicare pays {rate_str} for this procedure—use that as your negotiating "
                    f"anchor. Also ask the billing department about payment plans or charity care if "
                    f"the cost poses a financial hardship."
                ),
            },
        ]

    # outpatient / diagnostic
    return [
        {
            "q": f"Is {name} covered by insurance?",
            "a": (
                f"{name} (CPT {cpt_code}) is generally covered by most insurance plans when medically "
                f"necessary, but coverage varies by plan type and medical necessity criteria. Medicare "
                f"pays {rate_str} for this procedure. Always confirm your benefit coverage and any "
                f"prior authorization requirements with your insurer before scheduling."
            ),
        },
        {
            "q": f"Why might I be billed separately for {name} by multiple providers?",
            "a": (
                f"When {name} is performed at a hospital outpatient facility, you may receive separate "
                f"bills from the hospital (facility fee) and from the physician or specialist who "
                f"performed or interpreted the procedure. This split billing—professional fee plus "
                f"facility fee—is common. The national average hospital charge is {avg_str}, so make "
                f"sure each individual bill reflects only the services that were actually provided."
            ),
        },
        {
            "q": f"How can I find out what my insurance will pay for {name} before I go?",
            "a": (
                f"Call the member services number on your insurance card and ask for a cost estimate "
                f"or Explanation of Benefits preview for CPT {cpt_code}. Also confirm whether the "
                f"facility you're considering is in-network. Medicare's reference rate for this "
                f"procedure is {rate_str}—if a hospital charges significantly more, you may owe more "
                f"out-of-pocket than expected even with insurance."
            ),
        },
    ]


def _build_procedure_seo(
    name: str,
    cpt_code: str,
    medicare_rate: float | None,
    avg_charge: float | None,
    hospital_count: int,
) -> dict:
    rate_str = f"${medicare_rate:,.0f}" if medicare_rate else "N/A"
    avg_str = f"${avg_charge:,.0f}" if avg_charge else "N/A"
    title = f"{name}: Cost, Grade & Prices | BillKarma"
    if len(title) > 60:
        short = name[:28].rsplit(" ", 1)[0] if len(name) > 28 else name
        title = f"{short}: Cost & Fair Prices | BillKarma"
    desc = (
        f"CPT {cpt_code} · Medicare rate {rate_str} · National avg {avg_str}. "
        f"Compare {hospital_count:,} hospitals by billing grade and see if your bill is fair."
    )
    if len(desc) > 155:
        desc = desc[:152].rsplit(" ", 1)[0] + "..."
    return {"page_title": title, "meta_description": desc}
