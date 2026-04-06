"""Directory/data helpers for ASC and imaging facility pages."""

from __future__ import annotations

import json
import math
from typing import Any

from config import APP_URL
from db import get_db

_ALL_PRICES_CTE = """
WITH all_prices AS (
    SELECT
        facility_id, cpt_code, description, gross_charge, cash_price,
        medicare_rate, markup_vs_medicare, data_year,
        facility_type, medicare_benchmark_type, medicare_benchmark_rate
    FROM hospital_prices
    UNION ALL
    SELECT
        facility_id, cpt_code, description, gross_charge, cash_price,
        medicare_rate, markup_vs_medicare, data_year,
        facility_type, medicare_benchmark_type, medicare_benchmark_rate
    FROM procedure_prices
)
"""

_ASC_SPECIALTY_RANGES: list[tuple[int, int, str]] = [
    (10000, 19999, "Skin/Soft Tissue/Breast"),
    (20000, 29999, "Orthopedic"),
    (40000, 49999, "GI / Colonoscopy"),
    (50000, 59999, "Urology / OB"),
    (60000, 69999, "Endocrine / ENT / Ophthalmology"),
]

_IMAGING_MODALITY_RANGES: list[tuple[int, int, str]] = [
    (70010, 70699, "X-ray"),
    (70450, 70498, "CT"),
    (70540, 70599, "MRI"),
    (71010, 71048, "X-ray"),
    (71250, 71275, "CT"),
    (71550, 71555, "MRI"),
    (72125, 72133, "CT"),
    (72141, 72158, "MRI"),
    (73200, 73206, "CT"),
    (73218, 73223, "MRI"),
    (73700, 73706, "CT"),
    (73718, 73723, "MRI"),
    (74150, 74178, "CT"),
    (74181, 74185, "MRI"),
    (76506, 76999, "Ultrasound"),
    (77001, 77099, "Mammography"),
    (78811, 78816, "PET"),
]


def _decode_json_list(raw: str | None) -> list[str]:
    if not raw:
        return []
    try:
        value = json.loads(raw)
    except Exception:
        return []
    return value if isinstance(value, list) else []


def _grade_sort_value(grade: str | None) -> int:
    g = (grade or "").upper()
    return {"A": 1, "B": 2, "C": 3, "D": 4, "F": 5}.get(g, 6)


def _profile_url(row: dict[str, Any]) -> str:
    ftype = row.get("facility_type") or "hospital"
    if ftype == "asc":
        return f"/surgery-centers/{row.get('state_slug')}/{row.get('city_slug')}/{row.get('slug')}/"
    if ftype == "imaging_center":
        return f"/imaging/{row.get('state_slug')}/{row.get('city_slug')}/{row.get('slug')}/"
    return f"/hospitals/{row.get('state_slug')}/{row.get('city_slug')}/{row.get('slug')}/"


def _safe_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _haversine_miles(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 3958.8
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlam = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlam / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def _asc_specialty_for_cpt(cpt_code: str) -> str | None:
    try:
        code = int(cpt_code)
    except (TypeError, ValueError):
        return None
    for lo, hi, label in _ASC_SPECIALTY_RANGES:
        if lo <= code <= hi:
            return label
    return None


def _imaging_modality_for_cpt(cpt_code: str) -> str | None:
    try:
        code = int(cpt_code)
    except (TypeError, ValueError):
        return None
    for lo, hi, label in _IMAGING_MODALITY_RANGES:
        if lo <= code <= hi:
            return label
    return None


def _extract_specialties_from_prices(prices: list[dict]) -> list[str]:
    out = []
    for p in prices:
        label = _asc_specialty_for_cpt(p.get("cpt_code") or "")
        if label:
            out.append(label)
    return sorted(set(out))


def _extract_modalities_from_prices(prices: list[dict]) -> list[str]:
    out = []
    for p in prices:
        label = _imaging_modality_for_cpt(p.get("cpt_code") or "")
        if label:
            out.append(label)
    return sorted(set(out))


def _group_prices_by_modality(prices: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = {}
    for row in prices:
        modality = _imaging_modality_for_cpt(row.get("cpt_code") or "") or "Other"
        grouped.setdefault(modality, []).append(row)
    order = {"MRI": 1, "CT": 2, "X-ray": 3, "Ultrasound": 4, "Mammography": 5, "PET": 6, "Other": 7}
    result = []
    for mod, rows in grouped.items():
        rows_sorted = sorted(rows, key=lambda r: (r.get("markup_ratio") is None, -(r.get("markup_ratio") or 0.0)))
        result.append({"modality": mod, "rows": rows_sorted[:12]})
    result.sort(key=lambda r: order.get(r["modality"], 99))
    return result


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


def get_landing_stats(facility_type: str) -> dict[str, Any]:
    with get_db() as db:
        if facility_type == "asc":
            row = db.execute(
                """
                WITH hosp AS (
                    SELECT p.cpt_code, AVG(p.gross_charge) AS avg_charge
                    FROM hospital_prices p
                    JOIN hospitals h ON h.facility_id = p.facility_id
                    WHERE p.gross_charge IS NOT NULL
                      AND CAST(p.cpt_code AS INTEGER) BETWEEN 10000 AND 69999
                    GROUP BY p.cpt_code
                ),
                ascs AS (
                    SELECT p.cpt_code, AVG(p.gross_charge) AS avg_charge
                    FROM procedure_prices p
                    WHERE p.facility_type = 'asc'
                      AND p.gross_charge IS NOT NULL
                    GROUP BY p.cpt_code
                )
                SELECT
                    AVG(hosp.avg_charge) AS hospital_avg,
                    AVG(ascs.avg_charge) AS asc_avg
                FROM hosp JOIN ascs ON ascs.cpt_code = hosp.cpt_code
                """
            ).fetchone()
            hosp = _safe_float(row["hospital_avg"]) if row else None
            asc = _safe_float(row["asc_avg"]) if row else None
            pct = ((hosp - asc) / hosp * 100) if (hosp and asc and hosp > 0) else None
            return {"hospital_avg": hosp, "asc_avg": asc, "pct_less": pct}
        row = db.execute(
            """
            WITH hosp AS (
                SELECT AVG(gross_charge) AS avg_charge
                FROM hospital_prices
                WHERE cpt_code = '70553' AND gross_charge IS NOT NULL
            ),
            img AS (
                SELECT AVG(gross_charge) AS avg_charge
                FROM procedure_prices
                WHERE facility_type = 'imaging_center'
                  AND cpt_code = '70553'
                  AND gross_charge IS NOT NULL
            )
            SELECT hosp.avg_charge AS hospital_mri_avg, img.avg_charge AS imaging_mri_avg FROM hosp, img
            """
        ).fetchone()
        hosp = _safe_float(row["hospital_mri_avg"]) if row else None
        img = _safe_float(row["imaging_mri_avg"]) if row else None
        return {"hospital_mri_avg": hosp, "imaging_mri_avg": img}


def get_facilities_in_scope(
    facility_type: str,
    state_slug: str | None = None,
    city_slug: str | None = None,
    limit: int = 250,
) -> list[dict]:
    where = ["f.facility_type = ?"]
    params: list[Any] = [facility_type]
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
        d["profile_url"] = _profile_url(d)
        out.append(d)
    return out


def _nearest_hospital_comparison(
    facility: dict[str, Any],
    prices: list[dict[str, Any]],
) -> dict[str, Any] | None:
    lat, lon = _safe_float(facility.get("lat")), _safe_float(facility.get("lon"))
    if lat is None or lon is None:
        return None
    cpts = [p.get("cpt_code") for p in prices if p.get("cpt_code")]
    if not cpts:
        return None
    placeholders = ",".join(["?"] * len(cpts))

    with get_db() as db:
        rows = db.execute(
            f"""
            SELECT
                h.facility_id, h.name, h.state_slug, h.city_slug, h.slug, h.lat, h.lon,
                bm.billing_grade, bm.avg_markup_vs_medicare,
                hp.cpt_code, hp.gross_charge
            FROM hospitals h
            LEFT JOIN billing_metrics bm ON bm.facility_id = h.facility_id
            JOIN hospital_prices hp ON hp.facility_id = h.facility_id
            WHERE hp.cpt_code IN ({placeholders})
              AND hp.gross_charge IS NOT NULL
              AND h.lat IS NOT NULL AND h.lon IS NOT NULL
            """,
            tuple(cpts),
        ).fetchall()

    if not rows:
        return None
    nearest: dict[str, Any] = {}
    for row in rows:
        d = dict(row)
        hid = d["facility_id"]
        dist = _haversine_miles(lat, lon, float(d["lat"]), float(d["lon"]))
        if hid not in nearest or dist < nearest[hid]["distance_miles"]:
            nearest[hid] = {
                "facility_id": hid,
                "name": d["name"],
                "state_slug": d["state_slug"],
                "city_slug": d["city_slug"],
                "slug": d["slug"],
                "distance_miles": dist,
                "billing_grade": d.get("billing_grade"),
                "avg_markup_vs_medicare": d.get("avg_markup_vs_medicare"),
                "cpt_prices": {},
            }
        nearest[hid]["cpt_prices"][d["cpt_code"]] = d["gross_charge"]
    hospital = min(nearest.values(), key=lambda x: x["distance_miles"])
    by_cpt = {p["cpt_code"]: p for p in prices}

    comparable = []
    for cpt, this_row in by_cpt.items():
        h_charge = hospital["cpt_prices"].get(cpt)
        if h_charge is None or this_row.get("this_charge") is None:
            continue
        comparable.append(
            {
                "cpt_code": cpt,
                "procedure": this_row.get("description"),
                "this_charge": this_row.get("this_charge"),
                "hospital_charge": h_charge,
                "benchmark_rate": this_row.get("benchmark_rate"),
                "markup_ratio": this_row.get("markup_ratio"),
                "is_cheaper": this_row.get("this_charge") < h_charge,
            }
        )
    if not comparable:
        return None
    avg_this = sum(x["this_charge"] for x in comparable) / len(comparable)
    avg_hosp = sum(x["hospital_charge"] for x in comparable) / len(comparable)
    pct = ((avg_hosp - avg_this) / avg_hosp) * 100 if avg_hosp > 0 else 0.0
    return {
        "hospital": hospital,
        "comparable_count": len(comparable),
        "avg_this": avg_this,
        "avg_hospital": avg_hosp,
        "pct_less_than_hospital": round(pct, 1),
        "comparison_rows": sorted(comparable, key=lambda r: r["markup_ratio"] or 0.0, reverse=True)[:12],
    }


def _nearby_facilities(
    facility: dict[str, Any],
    same_type_radius: float,
    hospital_radius: float,
) -> dict[str, list[dict]]:
    lat, lon = _safe_float(facility.get("lat")), _safe_float(facility.get("lon"))
    if lat is None or lon is None:
        return {"same_type": [], "hospitals": []}
    this_id = facility["facility_id"]
    this_type = facility["facility_type"]

    with get_db() as db:
        same_rows = db.execute(
            """
            SELECT f.facility_id, f.name, f.city, f.state, f.state_slug, f.city_slug, f.slug,
                   f.lat, f.lon, f.is_hospital_owned, fm.billing_grade, fm.avg_markup
            FROM facilities f
            LEFT JOIN facility_billing_metrics fm ON fm.facility_id = f.facility_id
            WHERE f.facility_type = ? AND f.facility_id != ? AND f.lat IS NOT NULL AND f.lon IS NOT NULL
            """,
            (this_type, this_id),
        ).fetchall()
        hospital_rows = db.execute(
            """
            SELECT h.facility_id, h.name, h.city, h.state, h.state_slug, h.city_slug, h.slug,
                   h.lat, h.lon, bm.billing_grade, bm.avg_markup_vs_medicare AS avg_markup
            FROM hospitals h
            LEFT JOIN billing_metrics bm ON bm.facility_id = h.facility_id
            WHERE h.lat IS NOT NULL AND h.lon IS NOT NULL
            """,
        ).fetchall()

    same, hospitals = [], []
    for row in same_rows:
        d = dict(row)
        dist = _haversine_miles(lat, lon, float(d["lat"]), float(d["lon"]))
        if dist <= same_type_radius:
            d["distance_miles"] = round(dist, 1)
            d["profile_url"] = _profile_url({**d, "facility_type": this_type})
            same.append(d)
    for row in hospital_rows:
        d = dict(row)
        dist = _haversine_miles(lat, lon, float(d["lat"]), float(d["lon"]))
        if dist <= hospital_radius:
            d["distance_miles"] = round(dist, 1)
            d["profile_url"] = _profile_url({**d, "facility_type": "hospital"})
            hospitals.append(d)
    same.sort(key=lambda r: (_grade_sort_value(r.get("billing_grade")), r.get("avg_markup") or 999.0, r["distance_miles"]))
    hospitals.sort(key=lambda r: (_grade_sort_value(r.get("billing_grade")), r.get("avg_markup") or 999.0, r["distance_miles"]))
    return {"same_type": same[:12], "hospitals": hospitals[:12]}


def _build_facility_seo(facility: dict[str, Any], nearest_cmp: dict[str, Any] | None) -> dict[str, str]:
    name = facility.get("name", "")
    city = facility.get("city", "")
    state = facility.get("state", "")
    grade = facility.get("billing_grade") or "N/A"
    ftype = facility.get("facility_type")
    if ftype == "asc":
        title = f"{name} Surgery Center Prices & Grade | BillKarma"
        meta = (
            f"{name} in {city}, {state} is an ambulatory surgery center with a BillKarma billing grade of {grade}. "
            "See procedure prices, compare to nearby hospitals, and check if your bill is fair."
        )
    else:
        mods = facility.get("imaging_modalities") or []
        mods_txt = ", ".join(mods[:4]) if mods else "MRI, CT, and X-ray"
        title = f"{name} MRI & Imaging Prices | BillKarma"
        meta = (
            f"{name} in {city}, {state} offers {mods_txt}. BillKarma billing grade: {grade}. "
            "Compare MRI and CT scan prices to Medicare rates and nearby imaging centers."
        )
    return {"page_title": title[:65], "meta_description": meta[:170]}


def _build_facility_faq_schema(facility: dict[str, Any], prices: list[dict], nearest_cmp: dict[str, Any] | None) -> dict:
    name = facility.get("name", "This facility")
    ftype = facility.get("facility_type")
    phone = facility.get("phone") or "the center directly"
    if ftype == "asc":
        nearest_name = nearest_cmp["hospital"]["name"] if nearest_cmp else "the nearest hospital"
        if nearest_cmp:
            pct = nearest_cmp.get("pct_less_than_hospital", 0.0)
            direction = "less" if pct >= 0 else "more"
            compare_text = f"For procedures available at both facilities, {name} charges an average of {abs(pct):.1f}% {direction} than {nearest_name}."
        else:
            compare_text = f"Direct overlap data with nearby hospitals is limited for {name}."
        top5 = prices[:5]
        top_text = "; ".join(
            f"{p.get('description') or p.get('cpt_code')} (${p.get('this_charge', 0):,.0f})"
            for p in top5
        ) or "Procedure-level pricing is available on this page."
        accepts = "Yes" if facility.get("accepts_medicare") else "Not confirmed in current CMS records."
        qas = [
            ("Is {name} cheaper than going to a hospital?".format(name=name), compare_text),
            ("What procedures does {name} perform?".format(name=name), top_text),
            ("Does {name} accept Medicare?".format(name=name), accepts),
        ]
    else:
        mri = next((p for p in prices if p.get("cpt_code") in ("70553", "72148")), prices[0] if prices else None)
        if mri:
            code = mri.get("cpt_code")
            charge = mri.get("this_charge")
            bench = mri.get("benchmark_rate")
            ratio = mri.get("markup_ratio")
            mri_text = (
                f"{name} charges ${charge:,.0f} for {mri.get('description') or 'this MRI'} (CPT {code}). "
                f"The Medicare rate is ${bench:,.0f}, for a {ratio:.1f}x markup."
            )
        else:
            mri_text = f"MRI pricing data for {name} is currently limited."
        if nearest_cmp:
            pct = nearest_cmp.get("pct_less_than_hospital", 0.0)
            cmp_text = f"Compared with nearby hospital imaging charges, {name} is about {abs(pct):.1f}% {'less' if pct >= 0 else 'more'} expensive for overlapping scans."
        else:
            cmp_text = f"Nearby hospital comparison data for {name} is currently limited."
        referral = (
            f"Most imaging centers require a physician referral for insurance coverage. "
            f"For self-pay patients, many imaging centers accept direct scheduling. Contact {name} at {phone} to confirm."
        )
        qas = [
            ("How much does an MRI cost at {name}?".format(name=name), mri_text),
            ("Is {name} cheaper than hospital imaging?".format(name=name), cmp_text),
            ("Do I need a referral for {name}?".format(name=name), referral),
        ]

    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in qas
        ],
    }


def _build_facility_breadcrumb_schema(facility: dict[str, Any]) -> dict:
    base = APP_URL.rstrip("/")
    ftype = facility.get("facility_type")
    if ftype == "asc":
        root_name, root_path = "Surgery Centers", "surgery-centers"
    else:
        root_name, root_path = "Imaging Centers", "imaging"
    state_slug = facility.get("state_slug", "")
    city_slug = facility.get("city_slug", "")
    slug = facility.get("slug", "")
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "BillKarma", "item": f"{base}/"},
            {"@type": "ListItem", "position": 2, "name": root_name, "item": f"{base}/{root_path}/"},
            {"@type": "ListItem", "position": 3, "name": facility.get("state", state_slug).upper(), "item": f"{base}/{root_path}/{state_slug}/"},
            {"@type": "ListItem", "position": 4, "name": facility.get("city", city_slug), "item": f"{base}/{root_path}/{state_slug}/{city_slug}/"},
            {"@type": "ListItem", "position": 5, "name": facility.get("name", ""), "item": f"{base}/{root_path}/{state_slug}/{city_slug}/{slug}/"},
        ],
    }


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
            f"""
            {_ALL_PRICES_CTE}
            SELECT
                cpt_code, description, gross_charge, cash_price,
                COALESCE(medicare_benchmark_rate, medicare_rate) AS benchmark_rate,
                COALESCE(medicare_benchmark_type, 'opps') AS benchmark_type,
                markup_vs_medicare
            FROM all_prices
            WHERE facility_id = ?
              AND gross_charge IS NOT NULL
            ORDER BY markup_vs_medicare DESC
            LIMIT 200
            """,
            (facility["facility_id"],),
        ).fetchall()

    data = dict(facility)
    prices_d = []
    for row in prices:
        d = dict(row)
        d["this_charge"] = d.get("gross_charge")
        d["benchmark_rate"] = d.get("benchmark_rate")
        d["markup_ratio"] = d.get("markup_vs_medicare")
        prices_d.append(d)
    data["prices"] = prices_d
    data["asc_specialties"] = _decode_json_list(data.get("asc_specialties")) or _extract_specialties_from_prices(prices_d)
    data["imaging_modalities"] = _decode_json_list(data.get("imaging_modalities")) or _extract_modalities_from_prices(prices_d)

    nearest_cmp = _nearest_hospital_comparison(data, prices_d)
    nearby = _nearby_facilities(
        data,
        same_type_radius=50.0 if facility_type == "asc" else 25.0,
        hospital_radius=50.0,
    )
    imaging_groups = _group_prices_by_modality(prices_d) if facility_type == "imaging_center" else []

    if facility_type == "imaging_center":
        # Cash-vs-charge callout examples.
        cash_callouts = []
        for row in prices_d:
            gross = _safe_float(row.get("this_charge"))
            cash = _safe_float(row.get("cash_price"))
            if gross and cash and gross > 0 and cash < gross * 0.9:
                pct = ((gross - cash) / gross) * 100
                cash_callouts.append(
                    {
                        "description": row.get("description") or f"CPT {row.get('cpt_code')}",
                        "cash_price": cash,
                        "discount_pct": round(pct, 1),
                    }
                )
        data["cash_callouts"] = cash_callouts[:3]
    else:
        data["cash_callouts"] = []

    faq_schema = _build_facility_faq_schema(data, prices_d, nearest_cmp)
    breadcrumb_schema = _build_facility_breadcrumb_schema(data)
    seo = _build_facility_seo(data, nearest_cmp)

    data.update(
        {
            "nearest_hospital_comparison": nearest_cmp,
            "nearby_same_type": nearby["same_type"],
            "nearby_hospitals": nearby["hospitals"],
            "imaging_groups": imaging_groups,
            "seo": {
                **seo,
                "faq_schema_json": json.dumps(faq_schema, ensure_ascii=False),
                "breadcrumb_schema_json": json.dumps(breadcrumb_schema, ensure_ascii=False),
            },
        }
    )
    return data


def get_facility_sitemap_paths() -> list[str]:
    """Return all facility URL paths for ASC and imaging center pages."""
    with get_db() as db:
        asc_states = db.execute(
            "SELECT DISTINCT state_slug FROM facilities WHERE facility_type = 'asc' AND state_slug IS NOT NULL ORDER BY state_slug"
        ).fetchall()
        asc_cities = db.execute(
            "SELECT DISTINCT state_slug, city_slug FROM facilities WHERE facility_type = 'asc' AND state_slug IS NOT NULL AND city_slug IS NOT NULL ORDER BY state_slug, city_slug"
        ).fetchall()
        asc_facilities = db.execute(
            "SELECT state_slug, city_slug, slug FROM facilities WHERE facility_type = 'asc' AND state_slug IS NOT NULL AND city_slug IS NOT NULL AND slug IS NOT NULL ORDER BY state_slug, city_slug, slug"
        ).fetchall()
        img_states = db.execute(
            "SELECT DISTINCT state_slug FROM facilities WHERE facility_type = 'imaging_center' AND state_slug IS NOT NULL ORDER BY state_slug"
        ).fetchall()
        img_cities = db.execute(
            "SELECT DISTINCT state_slug, city_slug FROM facilities WHERE facility_type = 'imaging_center' AND state_slug IS NOT NULL AND city_slug IS NOT NULL ORDER BY state_slug, city_slug"
        ).fetchall()
        img_facilities = db.execute(
            "SELECT state_slug, city_slug, slug FROM facilities WHERE facility_type = 'imaging_center' AND state_slug IS NOT NULL AND city_slug IS NOT NULL AND slug IS NOT NULL ORDER BY state_slug, city_slug, slug"
        ).fetchall()

    paths = ["/surgery-centers/", "/imaging/"]
    paths.extend([f"/surgery-centers/{r['state_slug']}/" for r in asc_states])
    paths.extend([f"/surgery-centers/{r['state_slug']}/{r['city_slug']}/" for r in asc_cities])
    paths.extend([f"/surgery-centers/{r['state_slug']}/{r['city_slug']}/{r['slug']}/" for r in asc_facilities])
    paths.extend([f"/imaging/{r['state_slug']}/" for r in img_states])
    paths.extend([f"/imaging/{r['state_slug']}/{r['city_slug']}/" for r in img_cities])
    paths.extend([f"/imaging/{r['state_slug']}/{r['city_slug']}/{r['slug']}/" for r in img_facilities])
    return paths
