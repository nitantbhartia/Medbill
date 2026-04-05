"""Hospital directory SEO helpers, ranking logic, and deterministic content."""

from __future__ import annotations

import json
import math
import re
import time
from collections import defaultdict

from config import APP_URL, ENABLE_FREE_MAPS
from db import get_db

GRADE_THRESHOLDS = (
    (2.0, "A"),
    (3.0, "B"),
    (5.0, "C"),
    (8.0, "D"),
)
STATE_COMPARISON_MIN_SAMPLE_SIZE = 25
NEARBY_RADIUS_MILES = 50.0
# Highest-search-volume procedures for FAQ Q2, checked in priority order
FAQ_PRIORITY_CPTS = ("27447", "70553", "45378", "27130", "74178", "71045")
NATIONAL_AVG_MARKUP = 3.4  # approximate for FAQ answers
_EARTH_RADIUS_MILES = 3958.8
# ~1 degree lat ≈ 69 miles; padding for lon variation at different latitudes
_LAT_DEGREE_MILES = 69.0
_LON_DEGREE_MILES_EQUATOR = 69.17
NATIONAL_COMPARISON_MIN_SAMPLE_SIZE = 100
COMPARISON_CACHE_TTL_SECONDS = 900
CONTENT_TEMPLATE_VERSION = "deterministic-template-v2"
MAP_GRADE_COLORS = {
    "A": "#00B37E",
    "B": "#52C41A",
    "C": "#FAAD14",
    "D": "#FA8C16",
    "F": "#E53E3E",
    "N/A": "#9CA3AF",
}

US_STATE_NAMES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
    "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "FL": "Florida", "GA": "Georgia",
    "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa",
    "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri",
    "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
    "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio",
    "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont",
    "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming",
    "DC": "District of Columbia",
}

# Consumer-friendly aliases for commonly searched CPT/HCPCS codes.
FRIENDLY_CPT_DESCRIPTIONS = {
    "20610": "Joint Injection (drainage)",
    "11042": "Wound Debridement",
    "27447": "Total Knee Replacement",
    "22551": "Cervical Spine Fusion",
    "29881": "Knee Arthroscopy",
    "27130": "Total Hip Replacement",
    "10060": "Abscess Drainage",
    "27236": "Hip Fracture Repair",
    "23472": "Shoulder Replacement",
}

HOSPITAL_NAME_OVERRIDES_BY_ID: dict[str, str] = {}
HOSPITAL_NAME_OVERRIDES_BY_NAME = {
    "beaumont ashn": "Beaumont Hospital",
    "beaumont ashn llc": "Beaumont Hospital",
}

_comparison_cache: dict[str, tuple[float, dict[str, float | int | bool | None]]] = {}


def slugify(value: str) -> str:
    text = (value or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def state_slug_from_code(state_code: str) -> str:
    return slugify(state_code or "")


def city_slug_from_name(city: str) -> str:
    return slugify(city or "")


def normalize_facility_id(value: str | None) -> str | None:
    if not value:
        return None
    s = str(value).strip()
    # Strip ".0" suffix from float-parsed CSV values (e.g. "1659325629.0" → "1659325629")
    if s.endswith(".0"):
        prefix = s[:-2]
        if prefix.isdigit():
            s = prefix
    return s.zfill(6)


def _to_bool_int(value: str | int | None) -> int | None:
    if value is None:
        return None
    if isinstance(value, int):
        return 1 if value else 0
    txt = str(value).strip().lower()
    return 1 if txt in ("1", "true", "yes", "y") else 0


def _looks_nonprofit_from_ownership(ownership: str | None) -> bool | None:
    if not ownership:
        return None
    txt = str(ownership).strip().lower()
    nonprofit_markers = ("non-profit", "nonprofit", "non profit", "not-for-profit", "not for profit", "voluntary", "church")
    non_nonprofit_markers = ("proprietary", "for-profit", "for profit", "physician", "government")
    if any(marker in txt for marker in nonprofit_markers):
        return True
    if any(marker in txt for marker in non_nonprofit_markers):
        return False
    return None


def _ownership_display_label(ownership: str | None) -> str:
    """Map CMS ownership text to a human-readable label."""
    if not ownership:
        return "Unknown"
    txt = ownership.strip()
    txt_lower = txt.lower()
    if "voluntary non-profit" in txt_lower or "voluntary non profit" in txt_lower:
        if "church" in txt_lower:
            return "Nonprofit (Church-affiliated)"
        if "private" in txt_lower:
            return "Nonprofit (Private)"
        return "Nonprofit"
    if "non-profit" in txt_lower or "non profit" in txt_lower or "nonprofit" in txt_lower:
        return "Nonprofit"
    if "proprietary" in txt_lower or "for-profit" in txt_lower or "for profit" in txt_lower:
        return "For-profit"
    if "government" in txt_lower:
        if "federal" in txt_lower:
            return "Government (Federal)"
        if "district" in txt_lower or "authority" in txt_lower:
            return "Government (Public District)"
        if "state" in txt_lower:
            return "Government (State)"
        if "local" in txt_lower or "city" in txt_lower or "county" in txt_lower:
            return "Government (Local)"
        return "Government"
    if "physician" in txt_lower:
        return "For-profit (Physician-owned)"
    return txt  # Return raw value if unrecognized rather than hiding it


def _normalized_name_key(value: str) -> str:
    txt = re.sub(r"[^a-z0-9]+", " ", (value or "").strip().lower())
    return re.sub(r"\s+", " ", txt).strip()


def _display_name(name: str | None, facility_id: str | None = None) -> str:
    fid = normalize_facility_id(facility_id)
    if fid and fid in HOSPITAL_NAME_OVERRIDES_BY_ID:
        return HOSPITAL_NAME_OVERRIDES_BY_ID[fid]
    txt = (name or "").strip()
    if not txt:
        return ""
    txt = re.sub(r"\s+", " ", txt).strip().strip(",")
    txt = txt.title() if txt.isupper() else txt
    txt = re.sub(r"(?i)\s*(?:,\s*)?(llc|inc|inc\.|corp|corporation|co|company)\s*$", "", txt).strip()
    txt = HOSPITAL_NAME_OVERRIDES_BY_NAME.get(_normalized_name_key(txt), txt)
    return txt


def _display_city(city: str | None) -> str:
    txt = (city or "").strip()
    if not txt:
        return ""
    txt = re.sub(r"\s+", " ", txt)
    return txt.title() if txt.isupper() else txt


def state_display_name(state: str | None) -> str:
    txt = (state or "").strip()
    if not txt:
        return ""
    code = txt.upper()
    if code in US_STATE_NAMES:
        return US_STATE_NAMES[code]
    return txt.title() if txt.isupper() else txt


def upsert_hospital_row(row: dict) -> None:
    facility_id = normalize_facility_id(row.get("facility_id"))
    if not facility_id:
        return

    state = (row.get("state") or "").strip()
    city = (row.get("city") or "").strip()
    state_slug = row.get("state_slug") or state_slug_from_code(state)
    city_slug = row.get("city_slug") or city_slug_from_name(city)
    slug = row.get("slug") or slugify(f"{row.get('name', '')}-{city}")

    ownership = row.get("ownership")
    is_nonprofit = row.get("is_nonprofit")
    if is_nonprofit is None:
        inferred = _looks_nonprofit_from_ownership(ownership)
        is_nonprofit = 1 if inferred is True else 0 if inferred is False else None

    with get_db() as db:
        existing = db.execute(
            """
            SELECT facility_id FROM hospitals
            WHERE state_slug = ? AND city_slug = ? AND slug = ?
            """,
            (state_slug, city_slug, slug),
        ).fetchone()
        if existing and existing["facility_id"] != facility_id:
            slug = f"{slug}-{facility_id.lower()}"

        db.execute(
            """
            INSERT INTO hospitals (
                facility_id, name, address, city, state, zip, county, phone,
                hospital_type, ownership, is_nonprofit, emergency_services,
                bed_count, teaching_status, system_affiliation, cms_star_rating,
                slug, state_slug, city_slug, cms_data_updated, lat, lon
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, COALESCE(?, CURRENT_DATE), ?, ?)
            ON CONFLICT(facility_id) DO UPDATE SET
                name=excluded.name,
                address=excluded.address,
                city=excluded.city,
                state=excluded.state,
                zip=excluded.zip,
                county=excluded.county,
                phone=excluded.phone,
                hospital_type=excluded.hospital_type,
                ownership=excluded.ownership,
                is_nonprofit=excluded.is_nonprofit,
                emergency_services=excluded.emergency_services,
                bed_count=excluded.bed_count,
                teaching_status=excluded.teaching_status,
                system_affiliation=excluded.system_affiliation,
                cms_star_rating=excluded.cms_star_rating,
                slug=excluded.slug,
                state_slug=excluded.state_slug,
                city_slug=excluded.city_slug,
                cms_data_updated=excluded.cms_data_updated,
                lat=COALESCE(excluded.lat, lat),
                lon=COALESCE(excluded.lon, lon),
                updated_at=CURRENT_TIMESTAMP
            """,
            (
                facility_id,
                row.get("name"),
                row.get("address"),
                city,
                state,
                row.get("zip"),
                row.get("county"),
                row.get("phone"),
                row.get("hospital_type"),
                ownership,
                _to_bool_int(is_nonprofit),
                _to_bool_int(row.get("emergency_services")),
                row.get("bed_count"),
                row.get("teaching_status"),
                row.get("system_affiliation"),
                row.get("cms_star_rating") if row.get("cms_star_rating") is not None else row.get("overall_rating"),
                slug,
                state_slug,
                city_slug,
                row.get("cms_data_updated") or row.get("last_updated"),
                row.get("lat"),
                row.get("lon"),
            ),
        )

        db.execute(
            """
            INSERT INTO facilities (
                facility_id, name, address, city, state, state_slug, city_slug, zip, county, phone,
                facility_type, ownership_type, accepts_medicare, is_hospital_owned, parent_system,
                system_affiliation, lat, lon, slug
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'hospital', ?, 1, 0, ?, ?, ?, ?, ?)
            ON CONFLICT(facility_id) DO UPDATE SET
                name=excluded.name,
                address=excluded.address,
                city=excluded.city,
                state=excluded.state,
                state_slug=excluded.state_slug,
                city_slug=excluded.city_slug,
                zip=excluded.zip,
                county=excluded.county,
                phone=excluded.phone,
                facility_type='hospital',
                ownership_type=COALESCE(excluded.ownership_type, facilities.ownership_type),
                accepts_medicare=COALESCE(facilities.accepts_medicare, 1),
                parent_system=COALESCE(excluded.parent_system, facilities.parent_system),
                system_affiliation=COALESCE(excluded.system_affiliation, facilities.system_affiliation),
                lat=COALESCE(excluded.lat, facilities.lat),
                lon=COALESCE(excluded.lon, facilities.lon),
                slug=COALESCE(excluded.slug, facilities.slug),
                updated_at=CURRENT_TIMESTAMP
            """,
            (
                facility_id,
                row.get("name"),
                row.get("address"),
                city,
                state,
                state_slug,
                city_slug,
                row.get("zip"),
                row.get("county"),
                row.get("phone"),
                row.get("ownership_type"),
                row.get("parent_system"),
                row.get("system_affiliation"),
                row.get("lat"),
                row.get("lon"),
                slug,
            ),
        )

        # Backward-compatible mirror for existing routes/code paths.
        db.execute(
            """
            INSERT INTO hospital_directory (
                facility_id, name, address, city, state, state_slug, zip, county, phone,
                hospital_type, ownership, emergency_services, overall_rating,
                bed_count, teaching_status, system_affiliation, slug, last_updated
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, COALESCE(?, CURRENT_DATE))
            ON CONFLICT(facility_id) DO UPDATE SET
                name=excluded.name,
                address=excluded.address,
                city=excluded.city,
                state=excluded.state,
                state_slug=excluded.state_slug,
                zip=excluded.zip,
                county=excluded.county,
                phone=excluded.phone,
                hospital_type=excluded.hospital_type,
                ownership=excluded.ownership,
                emergency_services=excluded.emergency_services,
                overall_rating=excluded.overall_rating,
                bed_count=excluded.bed_count,
                teaching_status=excluded.teaching_status,
                system_affiliation=excluded.system_affiliation,
                slug=excluded.slug,
                last_updated=excluded.last_updated
            """,
            (
                facility_id,
                row.get("name"),
                row.get("address"),
                city,
                state,
                state_slug,
                row.get("zip"),
                row.get("county"),
                row.get("phone"),
                row.get("hospital_type"),
                ownership,
                row.get("emergency_services"),
                row.get("cms_star_rating") if row.get("cms_star_rating") is not None else row.get("overall_rating"),
                row.get("bed_count"),
                row.get("teaching_status"),
                row.get("system_affiliation"),
                slug,
                row.get("cms_data_updated") or row.get("last_updated"),
            ),
        )


def log_refresh(source: str, records_updated: int, status: str, notes: str = "") -> None:
    with get_db() as db:
        db.execute(
            "INSERT INTO data_refresh_log (source, records_updated, status, notes) VALUES (?, ?, ?, ?)",
            (source, records_updated, status, notes),
        )


def clear_comparison_cache() -> None:
    _comparison_cache.clear()


def get_grade_distribution() -> dict[str, int]:
    """Count hospitals per billing grade for the homepage visualization."""
    with get_db() as db:
        rows = db.execute(
            """
            SELECT billing_grade, COUNT(*) AS n
            FROM billing_metrics
            WHERE billing_grade IS NOT NULL AND billing_grade != ''
            GROUP BY billing_grade
            """
        ).fetchall()
    return {row["billing_grade"]: row["n"] for row in rows}


def get_sample_hospitals(count: int = 6) -> list[dict]:
    """Select diverse hospital cards for homepage showcase.

    Picks 1 A/B, 2 C, 2 D/F, 1 with highest single-procedure markup.
    All from different states, with at least 10 procedures compared.
    Uses state_slug (raw code) for dedup to match the SQL column.
    Excludes behavioral/psychiatric facilities to keep homepage sample broadly relevant.
    """
    with get_db() as db:
        buckets = [
            (("A", "B"), 1),
            (("C",), 2),
            (("D", "F"), 2),
        ]
        seen_states: set[str] = set()
        results: list[dict] = []

        for grades, limit in buckets:
            placeholders = ",".join("?" * len(grades))
            params: list = list(grades)
            state_clause = ""
            if seen_states:
                state_clause = " AND h.state_slug NOT IN (%s)" % ",".join("?" * len(seen_states))
                params.extend(seen_states)
            params.append(limit)

            rows = db.execute(
                f"""
                SELECT h.facility_id, h.name, h.city, h.state, h.slug,
                       h.state_slug, h.city_slug,
                       m.billing_grade, m.avg_markup_vs_medicare,
                       m.procedures_compared
                FROM hospitals h
                JOIN billing_metrics m ON m.facility_id = h.facility_id
                WHERE m.billing_grade IN ({placeholders})
                  AND m.avg_markup_vs_medicare IS NOT NULL
                  AND m.procedures_compared >= 10
                  AND lower(COALESCE(h.name, '')) NOT LIKE '%behavioral%'
                  AND lower(COALESCE(h.name, '')) NOT LIKE '%psychi%'
                  AND lower(COALESCE(h.hospital_type, '')) NOT LIKE '%behavioral%'
                  AND lower(COALESCE(h.hospital_type, '')) NOT LIKE '%psychi%'
                  {state_clause}
                ORDER BY
                    CASE WHEN lower(COALESCE(h.hospital_type, '')) LIKE '%acute%' THEN 0 ELSE 1 END,
                    m.procedures_compared DESC
                LIMIT ?
                """,
                params,
            ).fetchall()

            for row in rows:
                item = dict(row)
                seen_states.add(item["state_slug"])
                item["name"] = _display_name(item.get("name"), item.get("facility_id"))
                item["city"] = _display_city(item.get("city"))
                item["state"] = state_display_name(item.get("state"))
                results.append(item)

        # Fill remaining slot: hospital with the most dramatic single-procedure markup
        if len(results) < count:
            existing_ids = [r["facility_id"] for r in results]
            id_clause = ""
            state_clause = ""
            params2: list = []
            if existing_ids:
                id_clause = "AND h.facility_id NOT IN (%s)" % ",".join("?" * len(existing_ids))
                params2.extend(existing_ids)
            if seen_states:
                state_clause = "AND h.state_slug NOT IN (%s)" % ",".join("?" * len(seen_states))
                params2.extend(seen_states)

            dramatic = db.execute(
                f"""
                SELECT h.facility_id, h.name, h.city, h.state, h.slug,
                       h.state_slug, h.city_slug,
                       m.billing_grade, m.avg_markup_vs_medicare,
                       m.procedures_compared,
                       p.description AS standout_procedure,
                       p.markup_vs_medicare AS standout_markup
                FROM hospitals h
                JOIN billing_metrics m ON m.facility_id = h.facility_id
                JOIN hospital_prices p ON p.facility_id = h.facility_id
                WHERE m.procedures_compared >= 10
                  AND p.markup_vs_medicare IS NOT NULL
                  AND lower(COALESCE(h.name, '')) NOT LIKE '%behavioral%'
                  AND lower(COALESCE(h.name, '')) NOT LIKE '%psychi%'
                  AND lower(COALESCE(h.hospital_type, '')) NOT LIKE '%behavioral%'
                  AND lower(COALESCE(h.hospital_type, '')) NOT LIKE '%psychi%'
                  {id_clause}
                  {state_clause}
                ORDER BY p.markup_vs_medicare DESC
                LIMIT 1
                """,
                params2,
            ).fetchone()

            if dramatic:
                item = dict(dramatic)
                item["name"] = _display_name(item.get("name"), item.get("facility_id"))
                item["city"] = _display_city(item.get("city"))
                item["state"] = state_display_name(item.get("state"))
                results.append(item)

    # Mix grades so homepage rows feel representative, not ranked.
    lower_risk = [r for r in results if (r.get("billing_grade") or "").upper() in ("A", "B", "C")]
    higher_risk = [r for r in results if (r.get("billing_grade") or "").upper() in ("D", "F")]
    mixed: list[dict] = []
    while lower_risk or higher_risk:
        if lower_risk:
            mixed.append(lower_risk.pop(0))
        if higher_risk:
            mixed.append(higher_risk.pop(0))

    if len(mixed) < len(results):
        mixed.extend(results[len(mixed):])

    return mixed[:count]


def get_sample_facilities(count: int = 6) -> list[dict]:
    """Mixed sample cards for homepage: include hospital + ASC + imaging when available."""
    with get_db() as db:
        rows = db.execute(
            """
            SELECT
                f.facility_id, f.name, f.city, f.state, f.state_slug, f.city_slug, f.slug, f.facility_type,
                CASE
                    WHEN f.facility_type = 'hospital' THEN bm.billing_grade
                    ELSE fm.billing_grade
                END AS billing_grade,
                CASE
                    WHEN f.facility_type = 'hospital' THEN bm.avg_markup_vs_medicare
                    ELSE fm.avg_markup
                END AS avg_markup_vs_medicare
            FROM facilities f
            LEFT JOIN facility_billing_metrics fm ON fm.facility_id = f.facility_id
            LEFT JOIN billing_metrics bm ON bm.facility_id = f.facility_id
            WHERE f.slug IS NOT NULL
              AND f.state_slug IS NOT NULL
              AND (
                (f.facility_type = 'hospital' AND bm.billing_grade IN ('A','B','C','D','F') AND bm.avg_markup_vs_medicare IS NOT NULL)
                OR
                (f.facility_type != 'hospital' AND fm.billing_grade IN ('A','B','C','D','F') AND fm.avg_markup IS NOT NULL)
              )
            ORDER BY
              CASE
                WHEN f.facility_type = 'hospital' THEN bm.billing_grade
                ELSE fm.billing_grade
              END
                WHEN 'A' THEN 1 WHEN 'B' THEN 2 WHEN 'C' THEN 3 WHEN 'D' THEN 4 WHEN 'F' THEN 5 ELSE 6 END,
              f.name
            LIMIT 300
            """
        ).fetchall()

    out = [dict(r) for r in rows]
    for r in out:
        r["name"] = _display_name(r.get("name"), r.get("facility_id"))
        r["city"] = _display_city(r.get("city"))
        r["state"] = state_display_name(r.get("state"))
        r["facility_type_label"] = {
            "hospital": "Hospital",
            "asc": "Surgery Center",
            "imaging_center": "Imaging Center",
        }.get(r.get("facility_type") or "hospital", "Provider")

    hospitals = [r for r in out if r.get("facility_type") == "hospital"]
    ascs = [r for r in out if r.get("facility_type") == "asc"]
    imaging = [r for r in out if r.get("facility_type") == "imaging_center"]
    selected: list[dict] = []
    if hospitals:
        selected.append(hospitals[0])
    if ascs:
        selected.append(ascs[0])
    if imaging:
        selected.append(imaging[0])
    for row in out:
        if row in selected:
            continue
        selected.append(row)
        if len(selected) >= count:
            break
    return selected[:count]


def get_state_index_stats() -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            """
            SELECT state_slug, state, COUNT(*) AS hospitals
            FROM hospitals
            GROUP BY state_slug, state
            ORDER BY hospitals DESC, state
            """
        ).fetchall()
    output = []
    for row in rows:
        item = dict(row)
        item["state"] = state_display_name(item.get("state") or item.get("state_slug"))
        output.append(item)
    return output


def get_cities_for_state(state_slug: str) -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            """
            SELECT city_slug, city, COUNT(*) AS hospitals
            FROM hospitals
            WHERE state_slug = ?
            GROUP BY city_slug, city
            ORDER BY hospitals DESC, city
            """,
            (state_slug,),
        ).fetchall()
    output = []
    for row in rows:
        item = dict(row)
        item["city"] = _display_city(item.get("city"))
        output.append(item)
    return output


def get_state_hospitals(
    state_slug: str,
    *,
    sort: str = "grade",
    ownership: str = "",
    page: int = 1,
    per_page: int = 50,
) -> tuple[list[dict], int]:
    page = max(1, int(page))
    per_page = max(1, min(100, int(per_page)))
    offset = (page - 1) * per_page

    where = ["h.state_slug = ?"]
    params: list = [state_slug]
    if ownership:
        where.append("lower(COALESCE(h.ownership, '')) LIKE ?")
        params.append(f"%{ownership.lower()}%")

    order_by = {
        "name": "h.name ASC",
        "stars": "h.cms_star_rating DESC, h.name ASC",
        "markup": "m.avg_markup_vs_medicare DESC, h.name ASC",
        "grade": "CASE m.billing_grade WHEN 'A' THEN 1 WHEN 'B' THEN 2 WHEN 'C' THEN 3 WHEN 'D' THEN 4 WHEN 'F' THEN 5 ELSE 6 END, h.name ASC",
    }.get(sort, "h.name ASC")

    where_sql = " AND ".join(where)
    with get_db() as db:
        total = db.execute(
            f"SELECT COUNT(*) AS c FROM hospitals h WHERE {where_sql}",
            params,
        ).fetchone()["c"]
        rows = db.execute(
            f"""
            SELECT h.facility_id, h.name, h.city, h.state, h.ownership, h.cms_star_rating,
                   h.slug, h.state_slug, h.city_slug,
                   m.billing_grade, m.avg_markup_vs_medicare
            FROM hospitals h
            LEFT JOIN billing_metrics m ON m.facility_id = h.facility_id
            WHERE {where_sql}
            ORDER BY {order_by}
            LIMIT ? OFFSET ?
            """,
            [*params, per_page, offset],
        ).fetchall()

    output = []
    for row in rows:
        item = dict(row)
        item["name"] = _display_name(item.get("name"), item.get("facility_id"))
        item["city"] = _display_city(item.get("city"))
        item["state"] = state_display_name(item.get("state"))
        output.append(item)
    return output, int(total)


def get_city_hospitals(
    state_slug: str,
    city_slug: str,
    *,
    sort: str = "grade",
    page: int = 1,
    per_page: int = 50,
) -> tuple[list[dict], int]:
    page = max(1, int(page))
    per_page = max(1, min(100, int(per_page)))
    offset = (page - 1) * per_page

    order_by = {
        "name": "h.name ASC",
        "stars": "h.cms_star_rating DESC, h.name ASC",
        "markup": "m.avg_markup_vs_medicare DESC, h.name ASC",
        "grade": "CASE m.billing_grade WHEN 'A' THEN 1 WHEN 'B' THEN 2 WHEN 'C' THEN 3 WHEN 'D' THEN 4 WHEN 'F' THEN 5 ELSE 6 END, h.name ASC",
    }.get(sort, "h.name ASC")

    with get_db() as db:
        total = db.execute(
            "SELECT COUNT(*) AS c FROM hospitals h WHERE h.state_slug = ? AND h.city_slug = ?",
            (state_slug, city_slug),
        ).fetchone()["c"]
        rows = db.execute(
            f"""
            SELECT h.facility_id, h.name, h.city, h.state, h.ownership, h.cms_star_rating,
                   h.slug, h.state_slug, h.city_slug,
                   m.billing_grade, m.avg_markup_vs_medicare
            FROM hospitals h
            LEFT JOIN billing_metrics m ON m.facility_id = h.facility_id
            WHERE h.state_slug = ? AND h.city_slug = ?
            ORDER BY {order_by}
            LIMIT ? OFFSET ?
            """,
            (state_slug, city_slug, per_page, offset),
        ).fetchall()

    output = []
    for row in rows:
        item = dict(row)
        item["name"] = _display_name(item.get("name"), item.get("facility_id"))
        item["city"] = _display_city(item.get("city"))
        item["state"] = state_display_name(item.get("state"))
        output.append(item)
    return output, int(total)


def _lookup_content_for_hospital(facility_id: str) -> dict:
    with get_db() as db:
        row = db.execute("SELECT * FROM hospital_content WHERE facility_id = ?", (facility_id,)).fetchone()
    return dict(row) if row else {}


def _build_markup_band(markup: float | None) -> str:
    if markup is None:
        return "unknown"
    if markup < 2:
        return "fair"
    if markup < 5:
        return "high"
    return "excessive"


def _grade_index(grade: str | None) -> int | None:
    order = {"A": 0, "B": 1, "C": 2, "D": 3, "F": 4}
    return order.get((grade or "").strip().upper())


def _grade_position_from_markup(markup: float | int | None) -> float | None:
    """Map markup-vs-Medicare onto a 0..1 gauge where 0=F and 1=A."""
    if markup is None:
        return None
    try:
        m = float(markup)
    except (TypeError, ValueError):
        return None

    if m <= 0:
        return 1.0
    if m < 2.0:
        return 0.8 + (2.0 - m) / 2.0 * 0.2
    if m < 3.0:
        return 0.6 + (3.0 - m) / 1.0 * 0.2
    if m < 5.0:
        return 0.4 + (5.0 - m) / 2.0 * 0.2
    if m < 8.0:
        return 0.2 + (8.0 - m) / 3.0 * 0.2

    # Compress very high markups into the bottom red band.
    cap = min(m, 14.0)
    return max(0.0, 0.2 - (cap - 8.0) / 6.0 * 0.2)


def _gauge_xy(pct: float | None, radius: float, cx: float = 120.0, cy: float = 120.0) -> dict | None:
    if pct is None:
        return None
    p = max(0.0, min(1.0, float(pct)))
    angle = math.pi * (1.0 - p)  # 0..1 maps F(left) -> A(right)
    return {
        "x": cx + radius * math.cos(angle),
        "y": cy - radius * math.sin(angle),
    }


def _haversine_miles(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Return distance in miles between two lat/lon points."""
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    return 2 * _EARTH_RADIUS_MILES * math.asin(math.sqrt(a))


def _robust_average_markups(markups: list[float], low_q: float = 0.05, high_q: float = 0.95) -> float | None:
    clean = sorted(
        float(v)
        for v in markups
        if isinstance(v, (int, float)) and 0.5 <= float(v) <= 15.0
    )
    if not clean:
        return None
    if len(clean) < 20:
        return sum(clean) / len(clean)
    lo = int(len(clean) * low_q)
    hi = int(len(clean) * high_q)
    trimmed = clean[lo:max(lo + 1, hi)]
    if not trimmed:
        trimmed = clean
    return sum(trimmed) / len(trimmed)


def _filter_markup_outliers(markups: list[float], hard_min: float = 0.5, hard_max: float = 150.0) -> list[float]:
    """Apply hard bounds, then trim statistical outliers via IQR when sample size is sufficient."""
    clean = sorted(
        float(v)
        for v in markups
        if isinstance(v, (int, float)) and hard_min <= float(v) <= hard_max
    )
    if len(clean) < 8:
        return clean

    q1 = clean[int((len(clean) - 1) * 0.25)]
    q3 = clean[int((len(clean) - 1) * 0.75)]
    iqr = q3 - q1
    if iqr <= 0:
        return clean

    low = max(hard_min, q1 - 1.5 * iqr)
    high = min(hard_max, q3 + 1.5 * iqr)
    trimmed = [v for v in clean if low <= v <= high]
    return trimmed if trimmed else clean


def _comparison_averages_for_state(state_code: str | None) -> dict[str, float | None]:
    key = (state_code or "").upper()
    cached = _comparison_cache.get(key)
    now = time.time()
    if cached and (now - cached[0]) <= COMPARISON_CACHE_TTL_SECONDS:
        return dict(cached[1])

    with get_db() as db:
        national_rows = db.execute(
            """
            SELECT avg_markup_vs_medicare
            FROM billing_metrics
            WHERE avg_markup_vs_medicare IS NOT NULL
            """
        ).fetchall()
        state_rows = db.execute(
            """
            SELECT bm.avg_markup_vs_medicare
            FROM billing_metrics bm
            JOIN hospitals h ON h.facility_id = bm.facility_id
            WHERE bm.avg_markup_vs_medicare IS NOT NULL
              AND h.state = ?
            """,
            (state_code,),
        ).fetchall() if state_code else []

    national = _robust_average_markups([r["avg_markup_vs_medicare"] for r in national_rows])
    state = _robust_average_markups([r["avg_markup_vs_medicare"] for r in state_rows]) if state_rows else None
    state_n = len(state_rows)
    national_n = len(national_rows)
    show_state = state_n >= STATE_COMPARISON_MIN_SAMPLE_SIZE
    show_national = national_n >= NATIONAL_COMPARISON_MIN_SAMPLE_SIZE
    payload: dict[str, float | int | bool | None] = {
        "state_avg_markup": state if show_state else None,
        "national_avg_markup": national if show_national else None,
        "state_avg_markup_raw": state,
        "national_avg_markup_raw": national,
        "state_sample_size": state_n,
        "national_sample_size": national_n,
        "state_min_sample_size": STATE_COMPARISON_MIN_SAMPLE_SIZE,
        "national_min_sample_size": NATIONAL_COMPARISON_MIN_SAMPLE_SIZE,
        "show_state_comparison": show_state,
        "show_national_comparison": show_national,
        "show_comparison_chart": bool(show_state or show_national),
    }
    _comparison_cache[key] = (now, payload)
    return dict(payload)


def get_hospital_profile(state_slug: str, city_slug: str, hospital_slug: str) -> dict | None:
    with get_db() as db:
        hospital = db.execute(
            """
            SELECT h.*,
                   COALESCE(h.ownership, hd.ownership) AS ownership_fallback,
                   m.avg_markup_vs_medicare, m.median_markup_vs_medicare, m.max_markup_vs_medicare,
                   m.procedures_compared, m.cash_discount_avg_pct, m.billing_grade, m.state_rank,
                   m.national_percentile, m.computed_at
            FROM hospitals h
            LEFT JOIN hospital_directory hd ON hd.facility_id = h.facility_id
            LEFT JOIN billing_metrics m ON m.facility_id = h.facility_id
            WHERE h.state_slug = ? AND h.city_slug = ? AND h.slug = ?
            """,
            (state_slug, city_slug, hospital_slug),
        ).fetchone()
        if not hospital:
            return None

        quality = db.execute(
            "SELECT * FROM hcahps_scores WHERE facility_id = ?",
            (hospital["facility_id"],),
        ).fetchone()
        financials = db.execute(
            "SELECT * FROM hospital_financials WHERE facility_id = ?",
            (hospital["facility_id"],),
        ).fetchone()
        transparency = db.execute(
            "SELECT * FROM transparency_files WHERE facility_id = ?",
            (hospital["facility_id"],),
        ).fetchone()
        prices = db.execute(
            """
            SELECT hp.cpt_code,
                   COALESCE(
                     NULLIF(TRIM(hp.description), ''),
                     (
                        SELECT mr.description
                        FROM medicare_rates mr
                        WHERE mr.cpt_code = hp.cpt_code
                          AND mr.description IS NOT NULL
                          AND TRIM(mr.description) != ''
                        ORDER BY mr.effective_year DESC
                        LIMIT 1
                     )
                   ) AS description,
                   hp.gross_charge, hp.cash_price,
                   hp.medicare_rate, hp.markup_vs_medicare,
                   ba.avg_markup_vs_medicare AS state_avg_markup
            FROM hospital_prices hp
            LEFT JOIN benchmark_averages ba
              ON ba.scope = ? AND ba.cpt_code = hp.cpt_code
            WHERE hp.facility_id = ?
              AND hp.medicare_rate IS NOT NULL
              AND hp.medicare_rate > 0
              AND hp.markup_vs_medicare IS NOT NULL
            ORDER BY hp.markup_vs_medicare DESC, hp.gross_charge DESC
            LIMIT 40
            """,
            (hospital["state"], hospital["facility_id"]),
        ).fetchall()
    hospital_d = dict(hospital)
    state_code = hospital_d.get("state")
    if not hospital_d.get("ownership") and hospital_d.get("ownership_fallback"):
        hospital_d["ownership"] = hospital_d.get("ownership_fallback")
    quality_d = dict(quality) if quality else {}
    financials_d = dict(financials) if financials else {}
    transparency_d = dict(transparency) if transparency else {}
    comparison_d = _comparison_averages_for_state(state_code)
    hospital_d["name"] = _display_name(hospital_d.get("name"), hospital_d.get("facility_id"))
    hospital_d["city"] = _display_city(hospital_d.get("city"))
    hospital_d["state"] = state_display_name(state_code)
    npct = hospital_d.get("national_percentile")
    if isinstance(npct, int):
        hospital_d["aggressiveness_percentile"] = npct
        hospital_d["fairness_percentile"] = max(1, min(100, 101 - npct))
    else:
        hospital_d["aggressiveness_percentile"] = None
        hospital_d["fairness_percentile"] = None
    nonprofit_flag = hospital_d.get("is_nonprofit")
    ownership_nonprofit = _looks_nonprofit_from_ownership(hospital_d.get("ownership"))
    if nonprofit_flag in (None, 0) and ownership_nonprofit is True:
        nonprofit_flag = 1
    if nonprofit_flag in (None, 0) and ownership_nonprofit is False:
        nonprofit_flag = 0
    fin_nonprofit = financials_d.get("nonprofit_status")
    if nonprofit_flag in (None, 0) and fin_nonprofit in (1, "1", True):
        nonprofit_flag = 1
    if nonprofit_flag is None and fin_nonprofit in (0, "0", False):
        nonprofit_flag = 0
    hospital_d["is_nonprofit"] = 1 if nonprofit_flag else 0

    # Prefer enriched ownership_type (from CMS POS codes) over raw text
    enriched_ownership = hospital_d.get("ownership_type")
    if enriched_ownership and enriched_ownership not in ("Unknown", ""):
        hospital_d["nonprofit_status_label"] = enriched_ownership
    else:
        hospital_d["nonprofit_status_label"] = _ownership_display_label(hospital_d.get("ownership"))
    prices_d = [dict(p) for p in prices]

    show_cash_column = False
    for row in prices_d:
        row["markup_band"] = _build_markup_band(row.get("markup_vs_medicare"))
        code = row.get("cpt_code")
        row["description"] = FRIENDLY_CPT_DESCRIPTIONS.get(code) or row.get("description") or f"CPT {code}"
        gross = row.get("gross_charge")
        cash = row.get("cash_price")
        has_cash_discount = bool(
            gross is not None and cash is not None and gross > 0 and cash < (gross * 0.999)
        )
        row["has_cash_discount"] = has_cash_discount
        if has_cash_discount:
            show_cash_column = True

    content = _lookup_content_for_hospital(hospital_d["facility_id"])
    tips = content.get("dispute_tips")
    content_version = (content.get("model_used") or "").strip()
    if not tips or "loaded data" in str(tips).lower() or content_version != CONTENT_TEMPLATE_VERSION:
        tips = generate_deterministic_tips(hospital_d, financials_d, comparison_d)
    intro_paragraph = generate_intro_paragraph(hospital_d, comparison_d, top_prices=prices_d[:5])

    nearby, nearby_all_shown = get_nearby_hospitals(
        state_slug=hospital_d["state_slug"],
        city_slug=hospital_d["city_slug"],
        facility_id=hospital_d["facility_id"],
        state_code=state_code,
        lat=hospital_d.get("lat"),
        lon=hospital_d.get("lon"),
    )
    map_data = _build_hospital_map_data(hospital_d, nearby)
    surgery_center_alternatives = _get_nearby_asc_alternatives(hospital_d, prices_d) if (hospital_d.get("billing_grade") or "").upper() in {"D", "F"} else []

    hospital_markup = hospital_d.get("avg_markup_vs_medicare")
    state_markup = comparison_d.get("state_avg_markup")
    national_markup = comparison_d.get("national_avg_markup")

    hospital_gauge_pct = _grade_position_from_markup(hospital_markup)
    if hospital_gauge_pct is None:
        hospital_grade_idx = _grade_index(hospital_d.get("billing_grade"))
        hospital_gauge_pct = None if hospital_grade_idx is None else max(0.0, min(1.0, (4 - hospital_grade_idx) / 4))

    gauge_markers = {
        "hospital": hospital_gauge_pct,
        "state": _grade_position_from_markup(state_markup),
        "national": _grade_position_from_markup(national_markup),
    }
    gauge_points = {
        "hospital_tip": _gauge_xy(gauge_markers["hospital"], radius=72),
        "state": _gauge_xy(gauge_markers["state"], radius=100),
        "national": _gauge_xy(gauge_markers["national"], radius=90),
    }
    donut_radius = 96.0
    donut_length = math.pi * donut_radius
    donut_progress = donut_length * hospital_gauge_pct if hospital_gauge_pct is not None else None
    grade_donut = {
        "radius": donut_radius,
        "length": donut_length,
        "progress": donut_progress,
        "hospital": _gauge_xy(gauge_markers["hospital"], radius=96, cx=120, cy=140),
        "state": _gauge_xy(gauge_markers["state"], radius=96, cx=120, cy=140),
        "national": _gauge_xy(gauge_markers["national"], radius=96, cx=120, cy=140),
    }

    comparison_max = max(
        [
            v
            for v in (
                hospital_markup,
                state_markup,
                national_markup,
            )
            if isinstance(v, (int, float))
        ]
        or [1.0]
    )
    comparison_max = max(comparison_max, 1.0)

    section_updated = {
        "directory": hospital_d.get("cms_data_updated"),
        "quality": quality_d.get("data_updated"),
        "financials": financials_d.get("data_updated") or financials_d.get("updated_at") or financials_d.get("cost_report_year"),
        "pricing": transparency_d.get("last_parsed") or transparency_d.get("last_downloaded"),
        "metrics": hospital_d.get("computed_at"),
        "tips": content.get("generated_at"),
    }
    for key, value in list(section_updated.items()):
        section_updated[key] = str(value) if value not in (None, "") else None

    seo = generate_seo_elements(
        hospital_d=hospital_d,
        prices_d=prices_d,
        financials_d=financials_d,
        state_code=state_code or "",
        state_slug=hospital_d["state_slug"],
        city_slug=hospital_d["city_slug"],
    )

    return {
        "hospital": hospital_d,
        "quality": quality_d,
        "financials": financials_d,
        "transparency": transparency_d,
        "comparison": comparison_d,
        "grade_gauge_pct": hospital_gauge_pct,
        "grade_gauge_markers": gauge_markers,
        "grade_gauge_points": gauge_points,
        "grade_donut": grade_donut,
        "comparison_max": comparison_max,
        "prices": prices_d,
        "show_cash_column": show_cash_column,
        "tips": tips,
        "intro_paragraph": intro_paragraph,
        "content": content,
        "nearby": nearby,
        "nearby_all_shown": nearby_all_shown,
        "surgery_center_alternatives": surgery_center_alternatives,
        "map_data": map_data,
        "section_updated": section_updated,
        "seo": seo,
    }


def get_nearby_hospitals(
    state_slug: str,
    city_slug: str,
    facility_id: str,
    state_code: str | None = None,
    lat: float | None = None,
    lon: float | None = None,
    limit: int = 5,
) -> tuple[list[dict], bool]:
    """Return (nearby_list, all_shown) where all_shown=True means fewer than limit
    exist within radius. When lat/lon unavailable falls back to state filter."""
    if lat is not None and lon is not None:
        return _get_nearby_by_coords(facility_id, lat, lon, limit)
    results = _get_nearby_by_state(state_slug, city_slug, facility_id, state_code, limit)
    return results, False  # can't tell if all shown without coords


def _get_nearby_by_coords(facility_id: str, lat: float, lon: float, limit: int) -> tuple[list[dict], bool]:
    """Use bounding box pre-filter then exact Haversine sort."""
    lat_delta = NEARBY_RADIUS_MILES / _LAT_DEGREE_MILES
    lon_delta = NEARBY_RADIUS_MILES / (_LON_DEGREE_MILES_EQUATOR * math.cos(math.radians(lat)))
    with get_db() as db:
        rows = db.execute(
            """
            SELECT h.facility_id, h.name, h.slug, h.city, h.state_slug, h.city_slug,
                   h.lat, h.lon, m.billing_grade, m.avg_markup_vs_medicare
            FROM hospitals h
            LEFT JOIN billing_metrics m ON m.facility_id = h.facility_id
            WHERE h.facility_id != ?
              AND h.lat BETWEEN ? AND ?
              AND h.lon BETWEEN ? AND ?
              AND (m.avg_markup_vs_medicare IS NOT NULL OR (m.billing_grade IS NOT NULL AND m.billing_grade != 'N/A'))
            """,
            (facility_id, lat - lat_delta, lat + lat_delta, lon - lon_delta, lon + lon_delta),
        ).fetchall()

    candidates = []
    for row in rows:
        h_lat = row["lat"]
        h_lon = row["lon"]
        if h_lat is None or h_lon is None:
            continue
        dist = _haversine_miles(lat, lon, float(h_lat), float(h_lon))
        if dist <= NEARBY_RADIUS_MILES:
            item = dict(row)
            item["distance_miles"] = round(dist, 1)
            candidates.append(item)

    candidates.sort(key=lambda x: x["distance_miles"])
    all_shown = len(candidates) <= limit
    output = []
    for item in candidates[:limit]:
        item["name"] = _display_name(item.get("name"), item.get("facility_id"))
        item["city"] = _display_city(item.get("city"))
        output.append(item)
    return output, all_shown


def _get_nearby_by_state(
    state_slug: str, city_slug: str, facility_id: str, state_code: str | None, limit: int
) -> list[dict]:
    """Fallback: same-state hospitals when coordinates are unavailable."""
    state_filter = "AND h.state = ?" if state_code else ""
    params: list = [state_slug]
    if state_code:
        params.append(state_code)
    params += [facility_id, city_slug, city_slug, city_slug, limit]
    with get_db() as db:
        rows = db.execute(
            f"""
            SELECT h.facility_id, h.name, h.slug, h.city, h.state_slug, h.city_slug,
                   h.cms_star_rating, h.lat, h.lon, m.billing_grade, m.avg_markup_vs_medicare
            FROM hospitals h
            LEFT JOIN billing_metrics m ON m.facility_id = h.facility_id
            WHERE h.state_slug = ?
              {state_filter}
              AND h.facility_id != ?
              AND (m.avg_markup_vs_medicare IS NOT NULL OR (m.billing_grade IS NOT NULL AND m.billing_grade != 'N/A'))
              AND (h.city_slug = ? OR h.city_slug != ?)
            ORDER BY CASE WHEN h.city_slug = ? THEN 0 ELSE 1 END,
                     CASE WHEN m.avg_markup_vs_medicare IS NOT NULL THEN 0 ELSE 1 END,
                     h.name
            LIMIT ?
            """,
            params,
        ).fetchall()
    output = []
    for row in rows:
        item = dict(row)
        item["name"] = _display_name(item.get("name"), item.get("facility_id"))
        item["city"] = _display_city(item.get("city"))
        output.append(item)
    return output


def _safe_float(value) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _map_marker_for_hospital(row: dict, profile_url: str | None = None, is_current: bool = False) -> dict | None:
    lat = _safe_float(row.get("lat"))
    lon = _safe_float(row.get("lon"))
    if lat is None or lon is None:
        return None
    grade = row.get("billing_grade") or "N/A"
    avg_markup = row.get("avg_markup_vs_medicare")
    distance = row.get("distance_miles")
    return {
        "facility_id": row.get("facility_id"),
        "name": row.get("name"),
        "lat": lat,
        "lon": lon,
        "grade": grade,
        "grade_color": MAP_GRADE_COLORS.get(grade, MAP_GRADE_COLORS["N/A"]),
        "avg_markup_vs_medicare": avg_markup,
        "distance_miles": distance,
        "profile_url": profile_url,
        "is_current": is_current,
    }


def _build_hospital_map_data(hospital: dict, nearby: list[dict]) -> dict:
    if not ENABLE_FREE_MAPS:
        return {
            "available": False,
            "aria_label": f"Map showing location of {hospital.get('name')} and nearby hospitals",
            "fallback_text": f"Map disabled for {hospital.get('name')}.",
            "legend": "A <=2x · B 2-3x · C 3-5x · D 5-8x · F 8x+",
            "tile_max_zoom": 18,
            "current": None,
            "nearby": [],
        }
    current_marker = _map_marker_for_hospital(
        hospital,
        profile_url=f"/hospitals/{hospital.get('state_slug')}/{hospital.get('city_slug')}/{hospital.get('slug')}/",
        is_current=True,
    )
    nearby_markers = []
    for row in nearby:
        marker = _map_marker_for_hospital(
            row,
            profile_url=f"/hospitals/{row.get('state_slug')}/{row.get('city_slug')}/{row.get('slug')}/",
        )
        if marker:
            nearby_markers.append(marker)

    available = current_marker is not None
    fallback_neighbors = []
    for row in nearby[:3]:
        name = row.get("name")
        dist = row.get("distance_miles")
        if name:
            if dist is not None:
                fallback_neighbors.append(f"{name} ({dist} miles)")
            else:
                fallback_neighbors.append(str(name))
    if fallback_neighbors:
        nearby_text = ", ".join(fallback_neighbors)
    else:
        nearby_text = "No nearby hospitals with comparable billing data."

    address_parts = [hospital.get("address"), hospital.get("city"), hospital.get("state"), hospital.get("zip")]
    address_text = ", ".join([str(x) for x in address_parts if x])
    fallback_text = (
        f"Map shows {hospital.get('name')} at {address_text}. "
        f"Nearby hospitals within 50 miles include {nearby_text}."
    )
    return {
        "available": available,
        "aria_label": f"Map showing location of {hospital.get('name')} and nearby hospitals",
        "fallback_text": fallback_text,
        "legend": "A <=2x · B 2-3x · C 3-5x · D 5-8x · F 8x+",
        "tile_max_zoom": 18,
        "current": current_marker,
        "nearby": nearby_markers,
    }


def _get_nearby_asc_alternatives(hospital_d: dict, hospital_prices: list[dict], limit: int = 3) -> list[dict]:
    """Find nearby ASCs with overlapping procedures for high-markup hospitals."""
    lat = hospital_d.get("lat")
    lon = hospital_d.get("lon")
    if lat is None or lon is None:
        return []
    try:
        lat_f = float(lat)
        lon_f = float(lon)
    except (TypeError, ValueError):
        return []

    cpt_to_hospital_price = {
        p.get("cpt_code"): p for p in hospital_prices if p.get("cpt_code") and p.get("gross_charge") is not None
    }
    if not cpt_to_hospital_price:
        return []
    cpts = list(cpt_to_hospital_price.keys())
    placeholders = ",".join(["?"] * len(cpts))

    with get_db() as db:
        asc_rows = db.execute(
            """
            SELECT
                f.facility_id, f.name, f.state_slug, f.city_slug, f.slug, f.lat, f.lon, f.city,
                fm.billing_grade, fm.avg_markup
            FROM facilities f
            LEFT JOIN facility_billing_metrics fm ON fm.facility_id = f.facility_id
            WHERE f.facility_type = 'asc'
              AND f.lat IS NOT NULL
              AND f.lon IS NOT NULL
            """
        ).fetchall()
        price_rows = db.execute(
            f"""
            SELECT facility_id, cpt_code, gross_charge
            FROM procedure_prices
            WHERE facility_type = 'asc'
              AND cpt_code IN ({placeholders})
              AND gross_charge IS NOT NULL
            """,
            tuple(cpts),
        ).fetchall()

    asc_prices: dict[str, dict[str, float]] = {}
    for row in price_rows:
        d = dict(row)
        asc_prices.setdefault(d["facility_id"], {})[d["cpt_code"]] = d["gross_charge"]

    candidates = []
    for row in asc_rows:
        d = dict(row)
        fid = d["facility_id"]
        if fid not in asc_prices:
            continue
        dist = _haversine_miles(lat_f, lon_f, float(d["lat"]), float(d["lon"]))
        if dist > 25.0:
            continue
        overlap = []
        for cpt, asc_charge in asc_prices[fid].items():
            h = cpt_to_hospital_price.get(cpt)
            if not h:
                continue
            h_charge = h.get("gross_charge")
            if h_charge is None:
                continue
            overlap.append(
                {
                    "cpt_code": cpt,
                    "description": h.get("description") or f"CPT {cpt}",
                    "hospital_charge": h_charge,
                    "asc_charge": asc_charge,
                    "savings": h_charge - asc_charge,
                }
            )
        if not overlap:
            continue
        overlap.sort(key=lambda x: x["savings"], reverse=True)
        sample = overlap[0]
        candidates.append(
            {
                "facility_id": fid,
                "name": d["name"],
                "city": d.get("city"),
                "state_slug": d["state_slug"],
                "city_slug": d["city_slug"],
                "slug": d["slug"],
                "distance_miles": round(dist, 1),
                "billing_grade": d.get("billing_grade"),
                "avg_markup": d.get("avg_markup"),
                "sample": sample,
                "overlap_count": len(overlap),
            }
        )
    candidates.sort(key=lambda x: (_grade_index(x.get("billing_grade")), -(x["sample"]["savings"] or 0.0), x["distance_miles"]))
    return candidates[:limit]


def find_hospitals(query: str, limit: int = 20) -> list[dict]:
    q = (query or "").strip()
    if len(q) < 2:
        return []
    token = f"%{q}%"
    with get_db() as db:
        rows = db.execute(
            """
            SELECT h.name, h.city, h.state, h.slug, h.state_slug, h.city_slug,
                   m.billing_grade
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
    output = []
    for row in rows:
        item = dict(row)
        item["name"] = _display_name(item.get("name"), item.get("facility_id"))
        item["city"] = _display_city(item.get("city"))
        item["state"] = state_display_name(item.get("state"))
        output.append(item)
    return output


def resolve_hospital_slug(state_slug: str, city_slug: str, hospital_slug: str) -> str | None:
    target = slugify(hospital_slug)
    with get_db() as db:
        exact = db.execute(
            """
            SELECT slug FROM hospitals
            WHERE state_slug = ? AND city_slug = ? AND slug = ?
            LIMIT 1
            """,
            (state_slug, city_slug, target),
        ).fetchone()
        if exact:
            return exact["slug"]

        fallback = db.execute(
            """
            SELECT slug
            FROM hospitals
            WHERE state_slug = ? AND city_slug = ?
              AND (
                slug LIKE ? || '-%'
                OR replace(slug, '-inc', '') = ?
                OR replace(slug, '-llc', '') = ?
              )
            ORDER BY LENGTH(slug) ASC
            LIMIT 1
            """,
            (state_slug, city_slug, target, target, target),
        ).fetchone()
    return fallback["slug"] if fallback else None


def _grade_from_avg_markup(avg_markup: float | None) -> str:
    if avg_markup is None:
        return "N/A"
    for bound, grade in GRADE_THRESHOLDS:
        if avg_markup < bound:
            return grade
    return "F"


def recompute_benchmarks() -> int:
    with get_db() as db:
        db.execute("DELETE FROM benchmark_averages")
        rows = db.execute(
            """
            SELECT 'national' AS scope, cpt_code,
                   AVG(gross_charge) AS avg_gross,
                   AVG(cash_price) AS avg_cash,
                   COUNT(DISTINCT facility_id) AS hospital_count
            FROM hospital_prices
            WHERE gross_charge IS NOT NULL
            GROUP BY cpt_code
            """
        ).fetchall()
        state_rows = db.execute(
            """
            SELECT h.state AS scope, hp.cpt_code,
                   AVG(hp.gross_charge) AS avg_gross,
                   AVG(hp.cash_price) AS avg_cash,
                   COUNT(DISTINCT hp.facility_id) AS hospital_count
            FROM hospital_prices hp
            JOIN hospitals h ON h.facility_id = hp.facility_id
            WHERE hp.gross_charge IS NOT NULL
            GROUP BY h.state, hp.cpt_code
            """
        ).fetchall()
        markup_rows = db.execute(
            """
            SELECT 'national' AS scope, cpt_code, markup_vs_medicare
            FROM hospital_prices
            WHERE markup_vs_medicare IS NOT NULL
            UNION ALL
            SELECT h.state AS scope, hp.cpt_code, hp.markup_vs_medicare
            FROM hospital_prices hp
            JOIN hospitals h ON h.facility_id = hp.facility_id
            WHERE hp.markup_vs_medicare IS NOT NULL
            """
        ).fetchall()
        markup_by_scope_code: dict[tuple[str, str], list[float]] = defaultdict(list)
        for r in markup_rows:
            scope = r["scope"]
            code = r["cpt_code"]
            value = r["markup_vs_medicare"]
            if scope and code and value is not None:
                markup_by_scope_code[(scope, code)].append(float(value))

        inserted = 0
        for row in [*rows, *state_rows]:
            robust_markup = _robust_average_markups(markup_by_scope_code.get((row["scope"], row["cpt_code"]), []))
            db.execute(
                """
                INSERT INTO benchmark_averages (
                    scope, cpt_code, avg_gross_charge, avg_cash_price,
                    avg_markup_vs_medicare, hospital_count
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    row["scope"],
                    row["cpt_code"],
                    row["avg_gross"],
                    row["avg_cash"],
                    robust_markup,
                    row["hospital_count"],
                ),
            )
            inserted += 1

    clear_comparison_cache()
    return inserted


def recompute_billing_metrics() -> int:
    with get_db() as db:
        facilities = db.execute("SELECT facility_id, state FROM hospitals").fetchall()
        transparency = {
            row["facility_id"]: {
                "parse_status": row["parse_status"],
                "parse_notes": row["parse_notes"],
            }
            for row in db.execute(
                "SELECT facility_id, parse_status, parse_notes FROM transparency_files"
            ).fetchall()
        }
        upserted = 0
        min_points = 5

        for f in facilities:
            tf = transparency.get(f["facility_id"])
            rows = db.execute(
                """
                SELECT gross_charge, cash_price, markup_vs_medicare
                FROM hospital_prices
                WHERE facility_id = ?
                  AND gross_charge IS NOT NULL
                  AND markup_vs_medicare IS NOT NULL
                """,
                (f["facility_id"],),
            ).fetchall()

            if len(rows) < min_points:
                if not tf:
                    ungraded_reason = "missing_transparency_file"
                elif tf["parse_status"] == "not_found":
                    ungraded_reason = "transparency_file_not_found"
                elif tf["parse_status"] in ("failed", "unsupported_format", "empty_or_unreadable", "no_standard_codes"):
                    ungraded_reason = "transparency_parse_failed"
                else:
                    ungraded_reason = "insufficient_comparable_rows"
                db.execute(
                    """
                    INSERT INTO billing_metrics (
                        facility_id, avg_markup_vs_medicare, median_markup_vs_medicare,
                        max_markup_vs_medicare, procedures_compared, cash_discount_avg_pct,
                        billing_grade, ungraded_reason, grade_confidence, computed_at
                    ) VALUES (?, NULL, NULL, NULL, ?, NULL, 'N/A', ?, NULL, CURRENT_TIMESTAMP)
                    ON CONFLICT(facility_id) DO UPDATE SET
                        avg_markup_vs_medicare=NULL,
                        median_markup_vs_medicare=NULL,
                        max_markup_vs_medicare=NULL,
                        procedures_compared=excluded.procedures_compared,
                        cash_discount_avg_pct=NULL,
                        billing_grade='N/A',
                        ungraded_reason=excluded.ungraded_reason,
                        grade_confidence=NULL,
                        computed_at=CURRENT_TIMESTAMP
                    """,
                    (f["facility_id"], len(rows), ungraded_reason),
                )
                upserted += 1
                continue

            raw_markups = [float(r["markup_vs_medicare"]) for r in rows if r["markup_vs_medicare"] is not None]
            markups = _filter_markup_outliers(raw_markups)
            if len(markups) < min_points:
                db.execute(
                    """
                    INSERT INTO billing_metrics (
                        facility_id, avg_markup_vs_medicare, median_markup_vs_medicare,
                        max_markup_vs_medicare, procedures_compared, cash_discount_avg_pct,
                        billing_grade, ungraded_reason, grade_confidence, computed_at
                    ) VALUES (?, NULL, NULL, NULL, ?, NULL, 'N/A', ?, NULL, CURRENT_TIMESTAMP)
                    ON CONFLICT(facility_id) DO UPDATE SET
                        avg_markup_vs_medicare=NULL,
                        median_markup_vs_medicare=NULL,
                        max_markup_vs_medicare=NULL,
                        procedures_compared=excluded.procedures_compared,
                        cash_discount_avg_pct=NULL,
                        billing_grade='N/A',
                        ungraded_reason=excluded.ungraded_reason,
                        grade_confidence=NULL,
                        computed_at=CURRENT_TIMESTAMP
                    """,
                    (f["facility_id"], len(markups), "insufficient_rows_after_outlier_filter"),
                )
                upserted += 1
                continue
            avg_markup = sum(markups) / len(markups)
            med_markup = sorted(markups)[len(markups) // 2]
            max_markup = max(markups)
            grade_confidence = "high" if len(markups) >= 10 else "medium"

            cash_discounts = []
            for r in rows:
                gross = r["gross_charge"]
                cash = r["cash_price"]
                if gross and cash and gross > 0:
                    cash_discounts.append((1 - (cash / gross)) * 100)

            grade = _grade_from_avg_markup(avg_markup)
            cash_discount_avg = (sum(cash_discounts) / len(cash_discounts)) if cash_discounts else None

            db.execute(
                """
                INSERT INTO billing_metrics (
                    facility_id, avg_markup_vs_medicare, median_markup_vs_medicare,
                    max_markup_vs_medicare, procedures_compared, cash_discount_avg_pct,
                    billing_grade, ungraded_reason, grade_confidence, computed_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, NULL, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(facility_id) DO UPDATE SET
                    avg_markup_vs_medicare=excluded.avg_markup_vs_medicare,
                    median_markup_vs_medicare=excluded.median_markup_vs_medicare,
                    max_markup_vs_medicare=excluded.max_markup_vs_medicare,
                    procedures_compared=excluded.procedures_compared,
                    cash_discount_avg_pct=excluded.cash_discount_avg_pct,
                    billing_grade=excluded.billing_grade,
                    ungraded_reason=NULL,
                    grade_confidence=excluded.grade_confidence,
                    computed_at=CURRENT_TIMESTAMP
                """,
                (
                    f["facility_id"],
                    round(avg_markup, 2),
                    round(med_markup, 2),
                    round(max_markup, 2),
                    len(markups),
                    round(cash_discount_avg, 2) if cash_discount_avg is not None else None,
                    grade,
                    grade_confidence,
                ),
            )
            upserted += 1

        # state rank and national percentile backfill
        all_rows = db.execute(
            """
            SELECT h.facility_id, h.state, bm.avg_markup_vs_medicare
            FROM hospitals h
            JOIN billing_metrics bm ON bm.facility_id = h.facility_id
            WHERE bm.avg_markup_vs_medicare IS NOT NULL
            ORDER BY bm.avg_markup_vs_medicare DESC
            """
        ).fetchall()

        total = len(all_rows)
        by_state: dict[str, list] = defaultdict(list)
        for row in all_rows:
            by_state[row["state"]].append(row)

        for idx, row in enumerate(all_rows, start=1):
            percentile = int(round((idx / total) * 100)) if total else None
            state_list = by_state[row["state"]]
            state_rank = next(i for i, s in enumerate(state_list, start=1) if s["facility_id"] == row["facility_id"])
            db.execute(
                "UPDATE billing_metrics SET state_rank = ?, national_percentile = ? WHERE facility_id = ?",
                (state_rank, percentile, row["facility_id"]),
            )

    clear_comparison_cache()
    return upserted


def recompute_facility_billing_metrics() -> int:
    """Compute billing metrics across hospitals, ASCs, and imaging centers."""
    with get_db() as db:
        facilities = db.execute(
            """
            SELECT facility_id, facility_type
            FROM facilities
            WHERE facility_type IN ('hospital', 'asc', 'imaging_center')
            """
        ).fetchall()
        upserted = 0

        for f in facilities:
            facility_id = f["facility_id"]
            facility_type = f["facility_type"] or "hospital"
            benchmark_type = "asc" if facility_type == "asc" else "opps"

            if facility_type == "asc":
                rows = db.execute(
                    """
                    SELECT hp.gross_charge, hp.cash_price, hp.markup_vs_medicare
                    FROM hospital_prices hp
                    WHERE hp.facility_id = ?
                      AND hp.gross_charge IS NOT NULL
                      AND hp.markup_vs_medicare IS NOT NULL
                      AND (
                        hp.medicare_benchmark_type = 'asc'
                        OR EXISTS (
                            SELECT 1
                            FROM asc_medicare_rates ar
                            WHERE ar.cpt_code = hp.cpt_code
                              AND ar.is_covered_asc_procedure = 1
                              AND (hp.data_year IS NULL OR ar.effective_year = hp.data_year)
                        )
                      )
                    """,
                    (facility_id,),
                ).fetchall()
            else:
                rows = db.execute(
                    """
                    SELECT gross_charge, cash_price, markup_vs_medicare
                    FROM hospital_prices
                    WHERE facility_id = ?
                      AND gross_charge IS NOT NULL
                      AND markup_vs_medicare IS NOT NULL
                    """,
                    (facility_id,),
                ).fetchall()

            raw_markups = [float(r["markup_vs_medicare"]) for r in rows if r["markup_vs_medicare"] is not None]
            markups = _filter_markup_outliers(raw_markups)

            min_points = 10 if facility_type == "hospital" else 5
            if len(markups) < min_points:
                db.execute(
                    """
                    INSERT INTO facility_billing_metrics (
                        facility_id, facility_type, avg_markup, median_markup,
                        max_markup, procedures_compared, billing_grade, benchmark_type, computed_at
                    ) VALUES (?, ?, NULL, NULL, NULL, ?, 'N/A', ?, CURRENT_TIMESTAMP)
                    ON CONFLICT(facility_id) DO UPDATE SET
                        facility_type=excluded.facility_type,
                        avg_markup=NULL,
                        median_markup=NULL,
                        max_markup=NULL,
                        procedures_compared=excluded.procedures_compared,
                        billing_grade='N/A',
                        benchmark_type=excluded.benchmark_type,
                        computed_at=CURRENT_TIMESTAMP
                    """,
                    (facility_id, facility_type, len(markups), benchmark_type),
                )
                upserted += 1
                continue

            avg_markup = sum(markups) / len(markups)
            med_markup = sorted(markups)[len(markups) // 2]
            max_markup = max(markups)
            grade = _grade_from_avg_markup(avg_markup)

            db.execute(
                """
                INSERT INTO facility_billing_metrics (
                    facility_id, facility_type, avg_markup, median_markup,
                    max_markup, procedures_compared, billing_grade, benchmark_type, computed_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(facility_id) DO UPDATE SET
                    facility_type=excluded.facility_type,
                    avg_markup=excluded.avg_markup,
                    median_markup=excluded.median_markup,
                    max_markup=excluded.max_markup,
                    procedures_compared=excluded.procedures_compared,
                    billing_grade=excluded.billing_grade,
                    benchmark_type=excluded.benchmark_type,
                    computed_at=CURRENT_TIMESTAMP
                """,
                (
                    facility_id,
                    facility_type,
                    round(avg_markup, 2),
                    round(med_markup, 2),
                    round(max_markup, 2),
                    len(markups),
                    grade,
                    benchmark_type,
                ),
            )
            upserted += 1

    clear_comparison_cache()
    return upserted


def _generate_ungraded_intro(hospital: dict) -> str:
    """Generate fallback prose summary for hospitals with no billing grade."""
    name = hospital.get("name", "This hospital")
    city = hospital.get("city") or ""
    state = hospital.get("state") or ""
    location = f"in {city}, {state}" if city and state else (f"in {state}" if state else "")

    ownership_type = hospital.get("ownership_type") or hospital.get("ownership") or ""
    beds = hospital.get("bed_count")
    stars = hospital.get("cms_star_rating")
    procedures = hospital.get("procedures_compared") or 0
    is_pe = bool(hospital.get("is_pe_owned"))
    pe_firm = hospital.get("pe_firm") or ""
    pe_year = hospital.get("pe_acquisition_year")
    is_nonprofit = bool(hospital.get("is_nonprofit"))
    compliance = hospital.get("compliance_status") or "Unverified"

    ownership_txt = ownership_type if ownership_type and ownership_type not in ("Unknown", "") else "general"
    pe_txt = ""
    if is_pe and pe_firm:
        pe_txt = f", owned by {pe_firm}" + (f" since {pe_year}" if pe_year else "")
    beds_txt = f" with {beds:,} certified beds" if beds else ""

    intro = f"{name} {location} is a {ownership_txt} hospital{pe_txt}{beds_txt}."

    if stars:
        intro += f" CMS rates it {stars} out of 5 stars for overall quality."

    if procedures > 0:
        intro += (
            f" BillKarma was unable to compute a billing grade for this hospital because"
            f" their published price transparency file contains only {procedures}"
            f" procedure{'s' if procedures != 1 else ''}"
            " — insufficient for a representative markup analysis."
        )
    else:
        intro += (
            " BillKarma was unable to compute a billing grade for this hospital because"
            " no usable pricing data was found in their published price transparency file."
        )

    if compliance == "Non-compliant":
        intro += (
            " This hospital has not posted a complete machine-readable price file"
            " as required by federal law."
        )

    if is_nonprofit:
        intro += (
            " As a nonprofit hospital, they are required under IRS 501(r) to maintain"
            " a written financial assistance policy. Contact their billing department to request it."
        )

    return intro


def generate_intro_paragraph(
    hospital: dict,
    comparison: dict | None = None,
    top_prices: list[dict] | None = None,
) -> str:
    """Generate a 3-4 sentence hospital summary for SEO and page readability."""
    name = hospital.get("name", "This hospital")
    city = hospital.get("city") or ""
    state = hospital.get("state") or ""
    grade = hospital.get("billing_grade") or "N/A"
    markup = hospital.get("avg_markup_vs_medicare")
    procedures = hospital.get("procedures_compared")
    state_rank = hospital.get("state_rank")

    if not grade or grade == "N/A" or markup is None:
        return _generate_ungraded_intro(hospital)

    location = f"in {city}, {state}" if city and state else (f"in {state}" if state else "")
    markup_txt = f"{markup:.1f}x"
    proc_txt = f" across {procedures:,} procedures in their published price transparency file" if procedures else ""

    parts = [
        f"{name} {location} receives a BillKarma billing grade of {grade} "
        f"based on an average markup of {markup_txt} Medicare rates{proc_txt}."
    ]

    # State rank sentence
    if state_rank and state:
        if state_rank <= 10:
            parts.append(f"This places it among the 10 most expensive hospitals in {state} by markup ratio.")
        elif state_rank <= 25:
            parts.append(f"This places it in the top 25 most expensive hospitals in {state} by markup ratio.")
        else:
            parts.append(f"This places it at rank {state_rank} in {state} by markup ratio.")

    # Top 2 highest-markup procedures
    if top_prices:
        top2 = [p for p in top_prices if p.get("markup_vs_medicare") and p.get("description")][:2]
        if len(top2) == 2:
            p1, p2 = top2
            parts.append(
                f"The highest individual markups are for {p1['description']} ({p1['markup_vs_medicare']:.1f}x Medicare) "
                f"and {p2['description']} ({p2['markup_vs_medicare']:.1f}x Medicare)."
            )
        elif len(top2) == 1:
            p1 = top2[0]
            parts.append(f"The highest individual markup is for {p1['description']} ({p1['markup_vs_medicare']:.1f}x Medicare).")

    # Grade-based advisory
    if grade in ("D", "F"):
        parts.append(
            "Patients with scheduled procedures at this hospital should review costs and compare nearby alternatives "
            "before confirming — charges at D and F grade hospitals are significantly above the national average."
        )
    elif grade == "C":
        parts.append(
            "This hospital prices above the national average. "
            "Review procedure-level costs before scheduling non-emergency care."
        )
    elif grade in ("A", "B"):
        if state:
            parts.append(
                f"This hospital prices its services closer to Medicare benchmarks than most facilities in {state}, "
                "making it one of the more cost-transparent options in the area."
            )

    return " ".join(parts)


def generate_deterministic_tips(hospital: dict, financials: dict, comparison: dict | None = None) -> str:
    grade = hospital.get("billing_grade") or "N/A"
    markup = hospital.get("avg_markup_vs_medicare")
    markup_txt = f"{markup:.1f}x" if isinstance(markup, (int, float)) else None
    nonprofit = bool(hospital.get("is_nonprofit") or financials.get("nonprofit_status"))
    charity_pct = financials.get("charity_care_pct_revenue") or financials.get("charity_care_pct")
    charity_txt = f"{float(charity_pct):.1f}%" if charity_pct is not None else "not reported"
    cash_discount = hospital.get("cash_discount_avg_pct")
    cash_txt = f"{float(cash_discount):.1f}%" if cash_discount is not None else None

    # N/A hospitals — no grade or markup data
    if grade == "N/A" or markup_txt is None:
        name = hospital.get("name", "This hospital")
        procedures = hospital.get("procedures_compared") or 0
        phone = hospital.get("phone")
        contact_txt = f" Call billing at {phone} and request an itemized statement with CPT codes." if phone else ""

        markup_hint = ""
        if procedures > 0 and markup is not None:
            markup_hint = (
                f" The procedure data we do have shows a markup of approximately {markup:.1f}x Medicare"
                " — use this as a reference point when reviewing your full bill."
            )

        para1 = (
            f"{name} does not have enough pricing data in their published file for BillKarma"
            " to compute a billing grade. However, you can still dispute individual charges"
            f" using Medicare rates as your benchmark.{markup_hint}"
        )

        if nonprofit:
            para2 = (
                "As a nonprofit hospital, they are required under IRS Section 501(r) to have"
                " a written financial assistance policy. Ask their billing department for the"
                " Financial Assistance Policy (FAP) application and income eligibility thresholds"
                " before making any payment."
            )
        else:
            para2 = (
                "Request the self-pay or cash discount rate from billing — most hospitals offer"
                " significant reductions off their list prices for uninsured or high-deductible patients."
            )

        para3 = (
            "Request an itemized bill with CPT codes from their billing department,"
            " then use the BillKarma calculator to look up the Medicare rate for each code."
            + contact_txt
        )
        return "\n\n".join((para1, para2, para3))

    cmp_data = comparison or {}
    state_avg = cmp_data.get("state_avg_markup")
    national_avg = cmp_data.get("national_avg_markup")
    show_state = bool(cmp_data.get("show_state_comparison"))
    show_national = bool(cmp_data.get("show_national_comparison"))
    context_bits = []
    if show_state and isinstance(state_avg, (int, float)):
        relation = "above" if isinstance(markup, (int, float)) and markup > state_avg else "below"
        context_bits.append(f"{relation} the state average ({state_avg:.1f}x)")
    if show_national and isinstance(national_avg, (int, float)):
        relation = "above" if isinstance(markup, (int, float)) and markup > national_avg else "below"
        context_bits.append(f"{relation} the national average ({national_avg:.1f}x)")
    context_txt = ""
    if context_bits:
        context_txt = " In currently loaded benchmark samples, this is " + " and ".join(context_bits) + "."

    para1 = (
        f"{hospital.get('name', 'This hospital')} currently shows a billing grade of {grade} "
        f"with an average markup around {markup_txt} versus Medicare reference rates.{context_txt} "
        "Use that benchmark when asking billing to review line items and justify large gaps."
    )

    if nonprofit:
        para2 = (
            f"This hospital appears to be nonprofit. Ask for the formal financial assistance application, "
            f"income thresholds, and deadline rules before making payment commitments. "
            f"Reported charity-care level is {charity_txt}."
        )
    else:
        if cash_txt and float(cash_discount) > 0:
            para2 = (
                f"If you are self-pay or high-deductible, ask for the cash/self-pay schedule first. "
                f"Recent cash discounts are around {cash_txt}, which can be a practical anchor in your negotiation."
            )
        else:
            para2 = (
                "If you are self-pay or high-deductible, still request the cash/self-pay schedule in writing. "
                "If no discount is offered, ask for a supervisor review, payment-plan options, and item-level justification."
            )

    phone = hospital.get("phone")
    contact_txt = f" Call billing at {phone} and ask for an itemized review plus written adjustment options." if phone else ""
    para3 = (
        "Before paying, scan your bill with BillKarma to identify line-item issues and generate a dispute packet."
        + contact_txt
    )
    return "\n\n".join((para1, para2, para3))


def generate_and_save_hospital_content(limit: int | None = None) -> int:
    with get_db() as db:
        query = (
            """
            SELECT h.facility_id, h.name, h.state, h.city, h.ownership, h.is_nonprofit,
                   bm.billing_grade, bm.avg_markup_vs_medicare, bm.cash_discount_avg_pct,
                   hf.charity_care_pct_revenue, hf.charity_care_pct
            FROM hospitals h
            LEFT JOIN billing_metrics bm ON bm.facility_id = h.facility_id
            LEFT JOIN hospital_financials hf ON hf.facility_id = h.facility_id
            ORDER BY h.name
            """
        )
        if limit:
            query += " LIMIT ?"
            rows = db.execute(query, (limit,)).fetchall()
        else:
            rows = db.execute(query).fetchall()

        saved = 0
        for row in rows:
            data = dict(row)
            tips = generate_deterministic_tips(data, data, _comparison_averages_for_state(data.get("state")))
            meta = (
                f"{data['name']} billing review in {data['city']}, {data['state']}. "
                f"Compare markup vs Medicare, financial assistance, and dispute options before paying."
            )
            schema = {
                "@context": "https://schema.org",
                "@type": "Hospital",
                "name": data["name"],
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": data["city"],
                    "addressRegion": data["state"],
                },
            }
            db.execute(
                """
                INSERT INTO hospital_content (facility_id, dispute_tips, meta_description, structured_data_json, model_used)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(facility_id) DO UPDATE SET
                    dispute_tips=excluded.dispute_tips,
                    meta_description=excluded.meta_description,
                    structured_data_json=excluded.structured_data_json,
                    generated_at=CURRENT_TIMESTAMP,
                    model_used=excluded.model_used
                """,
                (data["facility_id"], tips, meta, json.dumps(schema), CONTENT_TEMPLATE_VERSION),
            )
            saved += 1
    return saved


def get_hospital_sitemap_paths() -> list[str]:
    with get_db() as db:
        states = db.execute(
            "SELECT DISTINCT state_slug FROM hospitals WHERE state_slug IS NOT NULL ORDER BY state_slug"
        ).fetchall()
        cities = db.execute(
            "SELECT DISTINCT state_slug, city_slug FROM hospitals WHERE state_slug IS NOT NULL AND city_slug IS NOT NULL ORDER BY state_slug, city_slug"
        ).fetchall()
        hospitals = db.execute(
            "SELECT state_slug, city_slug, slug FROM hospitals WHERE state_slug IS NOT NULL AND city_slug IS NOT NULL AND slug IS NOT NULL ORDER BY state_slug, city_slug, slug"
        ).fetchall()

    paths = ["/hospitals/"]
    paths.extend([f"/hospitals/{r['state_slug']}/" for r in states])
    paths.extend([f"/hospitals/{r['state_slug']}/{r['city_slug']}/" for r in cities])
    paths.extend([f"/hospitals/{r['state_slug']}/{r['city_slug']}/{r['slug']}/" for r in hospitals])
    return paths


# Backward-compat wrappers

def upsert_hospital_directory_row(row: dict) -> None:
    upsert_hospital_row(row)


def get_state_hospitals_legacy(state_slug: str, limit: int = 200) -> list[dict]:
    rows, _ = get_state_hospitals(state_slug=state_slug, per_page=limit)
    return rows


# ---------------------------------------------------------------------------
# SEO + structured data generation
# ---------------------------------------------------------------------------

def _truncate_name(name: str, max_len: int) -> str:
    """Truncate hospital name to max_len chars, appending '...' if cut."""
    if len(name) <= max_len:
        return name
    return name[: max_len - 3].rstrip() + "..."


def _get_national_avg_charge(cpt_code: str) -> float | None:
    """Return national average gross charge for a CPT code from benchmark_averages."""
    try:
        with get_db() as db:
            row = db.execute(
                "SELECT avg_gross_charge FROM benchmark_averages WHERE scope = 'national' AND cpt_code = ?",
                (cpt_code,),
            ).fetchone()
        return float(row["avg_gross_charge"]) if row and row["avg_gross_charge"] else None
    except Exception:
        return None


def _build_page_title(name: str) -> str:
    full_suffix = " Billing: Phone, Pay Online & Financial Help | BillKarma"
    short_suffix = " Billing & Financial Help | BillKarma"
    title = name + full_suffix
    if len(title) > 60:
        title = name + short_suffix
    if len(title) > 60:
        title = _truncate_name(name, 60 - len(short_suffix)) + short_suffix
    return title


def _build_meta_description(hospital_d: dict, prices_d: list[dict]) -> str:
    name = hospital_d.get("name", "")
    desc = (
        f"Contact {name} billing department. "
        f"Find the billing phone number, pay your bill online, "
        f"request an itemized statement, or apply for financial assistance."
    )
    if len(desc) <= 155:
        return desc
    # Truncate at last word boundary before 152 chars, append ellipsis
    cut = desc[:152]
    last_space = cut.rfind(" ")
    return (cut[:last_space] if last_space > 100 else cut) + "..."


def _build_faq_schema(hospital_d: dict, prices_d: list[dict], financials_d: dict) -> dict:
    name = hospital_d.get("name", "This hospital")
    grade = hospital_d.get("billing_grade") or "N/A"
    markup = hospital_d.get("avg_markup_vs_medicare")
    procedures = hospital_d.get("procedures_compared") or len(prices_d)
    markup_txt = f"{markup:.1f}x" if isinstance(markup, (int, float)) else "unknown"
    ownership_label = hospital_d.get("nonprofit_status_label", "Unknown")

    # Q1: billing grade
    q1_answer = (
        f"BillKarma gives {name} a billing grade of {grade}. "
        f"This grade is based on an average markup of {markup_txt} Medicare rates "
        f"across {procedures} procedures in their CMS-published price transparency file."
    )
    if grade in ("F", "D"):
        q1_answer += f" This is above the national average of approximately {NATIONAL_AVG_MARKUP}x Medicare."
    elif grade in ("A", "B"):
        q1_answer += (
            f" This is below the national average of approximately {NATIONAL_AVG_MARKUP}x Medicare, "
            "making it one of the more fairly priced hospitals in the area."
        )

    # Q2: procedure price — first priority CPT found in hospital data
    prices_by_cpt = {p["cpt_code"]: p for p in prices_d if p.get("cpt_code")}
    q2_proc = next((prices_by_cpt[c] for c in FAQ_PRIORITY_CPTS if c in prices_by_cpt), None)
    if q2_proc:
        cpt = q2_proc["cpt_code"]
        proc_name = q2_proc.get("description") or f"CPT {cpt}"
        charge = q2_proc.get("gross_charge")
        medicare = q2_proc.get("medicare_rate")
        proc_markup = q2_proc.get("markup_vs_medicare")
        charge_txt = f"${charge:,.2f}" if charge else "not reported"
        medicare_txt = f"${medicare:,.2f}" if medicare else "not available"
        markup_proc_txt = f"{proc_markup:.1f}x" if isinstance(proc_markup, (int, float)) else "unknown"
        national_avg = _get_national_avg_charge(cpt)
        nat_txt = f" The national average charge for this procedure is approximately ${national_avg:,.0f}." if national_avg else ""
        q2_question = f"How much does {proc_name} cost at {name}?"
        q2_answer = (
            f"{name} lists {proc_name} (CPT {cpt}) at {charge_txt}. "
            f"The Medicare rate for this procedure is {medicare_txt}, "
            f"making this a {markup_proc_txt} markup.{nat_txt}"
        )
    else:
        q2_question = f"How much do common procedures cost at {name}?"
        q2_answer = (
            f"{name} has an average markup of {markup_txt} Medicare rates. "
            "See the procedure price table on this page for specific CPT codes and charges."
        )

    # Q3: financial assistance
    if "nonprofit" in ownership_label.lower():
        q3_answer = (
            f"{name} is a nonprofit hospital and is required under IRS Section 501(r) to maintain "
            "a written financial assistance policy. Contact their billing department to request the "
            "Financial Assistance Policy (FAP) application. Eligibility typically covers patients up "
            "to 200–400% of the Federal Poverty Level, though thresholds vary by hospital."
        )
    elif "for-profit" in ownership_label.lower() or "proprietary" in ownership_label.lower():
        q3_answer = (
            f"{name} is a for-profit hospital with no federal charity care requirement. However, "
            "most for-profit hospitals offer self-pay discounts. Ask their billing department "
            "specifically for the 'self-pay discount rate' or 'cash settlement rate' — many "
            "for-profit hospitals offer 40–60% off gross charges for cash-paying patients."
        )
    elif "government" in ownership_label.lower():
        q3_answer = (
            f"{name} is a government-owned hospital and typically offers sliding-scale financial "
            "assistance programs with broader income eligibility than private hospitals. "
            "Contact their billing department for income-based assistance options."
        )
    else:
        q3_answer = (
            f"Contact {name}'s billing department to ask about financial assistance programs. "
            "Request their written financial assistance policy and ask about income eligibility thresholds."
        )

    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"What is {name}'s billing grade?",
                "acceptedAnswer": {"@type": "Answer", "text": q1_answer},
            },
            {
                "@type": "Question",
                "name": q2_question,
                "acceptedAnswer": {"@type": "Answer", "text": q2_answer},
            },
            {
                "@type": "Question",
                "name": f"Does {name} offer financial assistance?",
                "acceptedAnswer": {"@type": "Answer", "text": q3_answer},
            },
        ],
    }


def _build_breadcrumb_schema(hospital_d: dict, state_slug: str, city_slug: str) -> dict:
    base = APP_URL.rstrip("/")
    state_display = hospital_d.get("state") or state_slug
    city_display = hospital_d.get("city") or city_slug
    name = hospital_d.get("name", "")
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "BillKarma", "item": f"{base}/"},
            {"@type": "ListItem", "position": 2, "name": "Hospitals", "item": f"{base}/hospitals/"},
            {"@type": "ListItem", "position": 3, "name": state_display, "item": f"{base}/hospitals/{state_slug}/"},
            {"@type": "ListItem", "position": 4, "name": city_display, "item": f"{base}/hospitals/{state_slug}/{city_slug}/"},
            {"@type": "ListItem", "position": 5, "name": name, "item": f"{base}/hospitals/{state_slug}/{city_slug}/{hospital_d.get('slug', '')}/"},
        ],
    }


def _build_hospital_schema(hospital_d: dict, state_code: str) -> dict:
    schema: dict = {
        "@context": "https://schema.org",
        "@type": "Hospital",
        "name": hospital_d.get("name", ""),
        "address": {
            "@type": "PostalAddress",
            "streetAddress": hospital_d.get("address") or "",
            "addressLocality": hospital_d.get("city") or "",
            "addressRegion": state_code or "",
            "postalCode": hospital_d.get("zip") or "",
            "addressCountry": "US",
        },
    }
    if hospital_d.get("phone"):
        schema["telephone"] = hospital_d["phone"]
    stars = hospital_d.get("cms_star_rating")
    if stars and isinstance(stars, (int, float)):
        schema["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": int(stars),
            "bestRating": 5,
            "worstRating": 1,
            "ratingCount": 1,
            "description": "CMS Hospital Compare overall star rating",
        }
    return schema


def generate_seo_elements(
    hospital_d: dict,
    prices_d: list[dict],
    financials_d: dict,
    state_code: str,
    state_slug: str,
    city_slug: str,
) -> dict:
    """Return dict of SEO metadata and JSON-LD schema strings for a hospital page."""
    # Stash raw state code for meta description builder
    hospital_d["_state_code"] = state_code

    page_title = _build_page_title(hospital_d.get("name", ""))
    meta_description = _build_meta_description(hospital_d, prices_d)
    faq_schema = _build_faq_schema(hospital_d, prices_d, financials_d)
    breadcrumb_schema = _build_breadcrumb_schema(hospital_d, state_slug, city_slug)
    hospital_schema = _build_hospital_schema(hospital_d, state_code)

    return {
        "page_title": page_title,
        "meta_description": meta_description,
        "faq_schema_json": json.dumps(faq_schema, ensure_ascii=False),
        "breadcrumb_schema_json": json.dumps(breadcrumb_schema, ensure_ascii=False),
        "hospital_schema_json": json.dumps(hospital_schema, ensure_ascii=False),
    }
