"""Hospital data ETL and transparency parsing utilities."""

from __future__ import annotations

import csv
import json
import os
import re
import tempfile
from glob import glob
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import urlopen
from datetime import date
from typing import Iterable

from db import get_db
from hospital_seo import (
    city_slug_from_name,
    log_refresh,
    normalize_facility_id,
    slugify,
    state_slug_from_code,
    upsert_hospital_row,
)

TARGET_PROCEDURES = {
    "99281", "99282", "99283", "99284", "99285", "71046", "71045", "74177", "70553", "72148",
    "73721", "76856", "76805", "77067", "74176", "70551", "72141", "73221", "80053", "85025",
    "80061", "81001", "84443", "82947", "85610", "83036", "87086", "86900", "80048", "36415",
    "27447", "27130", "29881", "27236", "23472", "22551", "22630", "47562", "44970", "49505",
    "43239", "45378", "45385", "49650", "59400", "59510", "59025", "59000", "93000", "93306",
    "93458", "93010", "00810", "00740", "01996", "00300", "94640", "94060", "94010", "90834",
    "90837", "90791", "99213", "99214", "99243", "10060", "20610", "11042",
}

COLUMN_VARIANTS = {
    "code": ["code", "cpt", "cpt_code", "hcpcs", "hcpcs_code", "procedure_code", "billing_code", "service_code"],
    "description": ["description", "service_description", "procedure_description", "item_description", "service"],
    "gross_charge": ["gross_charge", "gross", "standard_charge", "chargemaster", "list_price", "charge", "price", "amount"],
    "cash_price": ["cash_price", "self_pay", "discounted_cash", "self_pay_price", "cash", "discount_cash_price"],
    "negotiated_rate": ["negotiated_rate", "allowed_amount", "contracted_rate", "payer_rate", "negotiated_amount"],
}


def parse_float(value: str | int | float | None) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    txt = str(value).strip().replace(",", "").replace("$", "").replace("%", "")
    if txt == "":
        return None
    try:
        return float(txt)
    except ValueError:
        return None


def numeric_by_patterns(row: dict, patterns: tuple[str, ...]) -> float | None:
    # Try exact/known columns first via `first`.
    val = parse_float(first(row, patterns))
    if val is not None:
        return val
    # Fallback: fuzzy column search for coded CMS fields.
    for key, raw in row.items():
        k = str(key).strip().lower().replace(" ", "_")
        if all(token in k for token in patterns):
            v = parse_float(raw)
            if v is not None:
                return v
    # Broader fallback: any key containing one token pattern.
    for key, raw in row.items():
        k = str(key).strip().lower().replace(" ", "_")
        if any(token in k for token in patterns):
            v = parse_float(raw)
            if v is not None:
                return v
    return None


def parse_int(value: str | int | float | None) -> int | None:
    num = parse_float(value)
    if num is None:
        return None
    return int(num)


def first(row: dict, keys: Iterable[str]) -> str | None:
    for key in keys:
        if key in row and row[key] not in (None, ""):
            return row[key]
    normalized = {str(k).strip().lower().replace(" ", "_"): v for k, v in row.items()}
    for key in keys:
        nk = str(key).strip().lower().replace(" ", "_")
        if nk in normalized and normalized[nk] not in (None, ""):
            return normalized[nk]
    return None


def auto_map_columns(columns: list[str]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    normalized = {c: c.lower().strip().replace(" ", "_") for c in columns}

    for standard_name, variants in COLUMN_VARIANTS.items():
        found = None
        for col, norm in normalized.items():
            if norm in variants:
                found = col
                break
        if not found:
            for col, norm in normalized.items():
                if any(v in norm for v in variants):
                    found = col
                    break
        if found:
            mapping[standard_name] = found

    return mapping


def detect_file_format(path: str) -> str:
    lower = path.lower()
    if lower.endswith(".csv"):
        return "csv"
    if lower.endswith(".json"):
        return "json"
    if lower.endswith(".xlsx"):
        return "xlsx"
    return "unknown"


def load_csv_rows(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def load_json_rows(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        payload = json.load(f)
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, dict)]
    if isinstance(payload, dict):
        for key in ("data", "items", "rows"):
            val = payload.get(key)
            if isinstance(val, list):
                return [row for row in val if isinstance(row, dict)]
    return []


def load_xlsx_rows(path: str) -> list[dict]:
    try:
        from openpyxl import load_workbook  # type: ignore
    except Exception:
        return []
    wb = load_workbook(path, read_only=True, data_only=True)
    ws = wb.active
    rows_iter = ws.iter_rows(values_only=True)
    header = next(rows_iter, None)
    if not header:
        return []
    cols = [str(h).strip() if h is not None else "" for h in header]
    rows: list[dict] = []
    for item in rows_iter:
        row = {}
        for i, col in enumerate(cols):
            if not col:
                continue
            row[col] = item[i] if i < len(item) else None
        rows.append(row)
    return rows


def load_rows_by_format(path: str, fmt: str) -> list[dict]:
    if fmt == "csv":
        return load_csv_rows(path)
    if fmt == "json":
        return load_json_rows(path)
    if fmt == "xlsx":
        return load_xlsx_rows(path)
    return []


def is_valid_cpt(code: str | None) -> bool:
    if not code:
        return False
    txt = str(code).strip().upper()
    if txt in TARGET_PROCEDURES:
        return True
    return bool(len(txt) == 5 and txt[0].isalnum() and txt[1:].isdigit())


def normalize_price_rows(rows: list[dict]) -> list[dict]:
    if not rows:
        return []
    mapping = auto_map_columns(list(rows[0].keys()))
    code_col = mapping.get("code")
    if not code_col:
        return []

    normalized = []
    for row in rows:
        code = row.get(code_col)
        if code is None:
            continue
        cpt_code, inferred_modifier = split_cpt_modifier(str(code))
        if not is_valid_cpt(cpt_code):
            continue
        desc = row.get(mapping.get("description", "")) if mapping.get("description") else None
        gross = parse_float(row.get(mapping.get("gross_charge", ""))) if mapping.get("gross_charge") else None
        cash = parse_float(row.get(mapping.get("cash_price", ""))) if mapping.get("cash_price") else None
        negotiated = parse_float(row.get(mapping.get("negotiated_rate", ""))) if mapping.get("negotiated_rate") else None
        modifier = (
            first(
                row,
                (
                    "modifier",
                    "mod",
                    "cpt_modifier",
                    "hcpcs_modifier",
                    "code_modifier",
                ),
            )
            or inferred_modifier
        )
        normalized.append(
            {
                "cpt_code": cpt_code,
                "cpt_modifier": normalize_modifier(modifier),
                "description": str(desc).strip() if desc is not None else None,
                "gross_charge": gross,
                "cash_price": cash,
                "avg_negotiated_rate": negotiated,
                "min_negotiated_rate": negotiated,
                "max_negotiated_rate": negotiated,
            }
        )
    return normalized


def normalize_modifier(value: str | None) -> str | None:
    if not value:
        return None
    txt = str(value).strip().upper()
    if not txt:
        return None
    if txt in {"26", "TC"}:
        return txt
    return None


def split_cpt_modifier(raw_code: str) -> tuple[str | None, str | None]:
    txt = str(raw_code or "").strip().upper()
    if not txt:
        return None, None
    m = re.match(r"^([A-Z0-9]{5})[-:\s]?((26|TC))$", txt)
    if m:
        return m.group(1), m.group(2)
    if len(txt) == 7 and txt[:5].isalnum() and txt[5:] in {"26", "TC"}:
        return txt[:5], txt[5:]
    return txt, None


def get_latest_medicare_rate(cpt_code: str) -> float | None:
    with get_db() as db:
        row = db.execute(
            """
            SELECT COALESCE(facility_rate, non_facility_rate) AS rate
            FROM medicare_rates
            WHERE cpt_code = ?
            ORDER BY effective_year DESC
            LIMIT 1
            """,
            (cpt_code,),
        ).fetchone()
    return float(row["rate"]) if row and row["rate"] is not None else None


def _facility_zip(facility_id: str) -> str | None:
    with get_db() as db:
        row = db.execute("SELECT zip FROM facilities WHERE facility_id = ? LIMIT 1", (facility_id,)).fetchone()
        if not row or not row["zip"]:
            row = db.execute("SELECT zip FROM hospitals WHERE facility_id = ? LIMIT 1", (facility_id,)).fetchone()
    if not row or not row["zip"]:
        return None
    zip_digits = "".join(ch for ch in str(row["zip"]) if ch.isdigit())
    return zip_digits[:5] if len(zip_digits) >= 5 else None


def _locality_for_zip(zip_code: str | None) -> str | None:
    if not zip_code:
        return None
    with get_db() as db:
        row = db.execute(
            """
            SELECT locality
            FROM zip_locality_map
            WHERE ? LIKE zip_prefix || '%'
            ORDER BY LENGTH(zip_prefix) DESC
            LIMIT 1
            """,
            (zip_code,),
        ).fetchone()
    return str(row["locality"]).strip() if row and row["locality"] else None


def get_medicare_rate_for_facility(facility_id: str, cpt_code: str) -> float | None:
    raw = str(facility_id or "").strip()
    if not raw:
        return None
    normalized = normalize_facility_id(raw)
    fid = raw
    if normalized:
        with get_db() as db:
            has_normalized = db.execute(
                "SELECT 1 FROM facilities WHERE facility_id = ? LIMIT 1",
                (normalized,),
            ).fetchone() or db.execute(
                "SELECT 1 FROM hospitals WHERE facility_id = ? LIMIT 1",
                (normalized,),
            ).fetchone()
        if has_normalized:
            fid = normalized
    zip_code = _facility_zip(fid)
    locality = _locality_for_zip(zip_code)
    with get_db() as db:
        if locality:
            row = db.execute(
                """
                SELECT COALESCE(facility_rate, non_facility_rate) AS rate
                FROM medicare_rates
                WHERE cpt_code = ? AND locality = ?
                ORDER BY effective_year DESC
                LIMIT 1
                """,
                (cpt_code, locality),
            ).fetchone()
            if row and row["rate"] is not None:
                return float(row["rate"])
        # Fallback when locality mapping missing: best available CPT rate.
        row = db.execute(
            """
            SELECT COALESCE(facility_rate, non_facility_rate) AS rate
            FROM medicare_rates
            WHERE cpt_code = ?
            ORDER BY effective_year DESC
            LIMIT 1
            """,
            (cpt_code,),
        ).fetchone()
    return float(row["rate"]) if row and row["rate"] is not None else None


def get_latest_opps_rate(cpt_code: str) -> float | None:
    with get_db() as db:
        row = db.execute(
            """
            SELECT national_payment_rate AS rate
            FROM hospital_opps_rates
            WHERE cpt_code = ?
            ORDER BY effective_year DESC
            LIMIT 1
            """,
            (cpt_code,),
        ).fetchone()
    return float(row["rate"]) if row and row["rate"] is not None else None


def get_latest_asc_rate(cpt_code: str) -> tuple[float | None, bool]:
    with get_db() as db:
        row = db.execute(
            """
            SELECT medicare_asc_rate AS rate, is_covered_asc_procedure AS covered
            FROM asc_medicare_rates
            WHERE cpt_code = ?
            ORDER BY effective_year DESC
            LIMIT 1
            """,
            (cpt_code,),
        ).fetchone()
    if not row:
        return None, False
    return (
        float(row["rate"]) if row["rate"] is not None else None,
        bool(row["covered"]) if row["covered"] is not None else False,
    )


def resolve_benchmark_for_row(facility_id: str, facility_type: str, row: dict) -> tuple[str, float | None]:
    cpt = row["cpt_code"]
    modifier = normalize_modifier(row.get("cpt_modifier"))
    ftype = (facility_type or "hospital").strip().lower()

    if ftype == "asc":
        asc_rate, covered = get_latest_asc_rate(cpt)
        if not covered:
            return "asc", None
        return "asc", asc_rate

    if ftype == "imaging_center":
        # Professional component lines (26/TC) should use PFS.
        if modifier in {"26", "TC"}:
            return "pfs", get_medicare_rate_for_facility(facility_id, cpt)
        opps = get_latest_opps_rate(cpt)
        if opps is not None:
            return "opps", opps
        return "pfs", get_medicare_rate_for_facility(facility_id, cpt)

    opps = get_latest_opps_rate(cpt)
    if opps is not None:
        return "opps", opps
    return "pfs", get_medicare_rate_for_facility(facility_id, cpt)


def upsert_hospital_price(facility_id: str, row: dict, data_year: int | None = None) -> None:
    facility_id = normalize_facility_id(facility_id)
    if not facility_id:
        return
    medicare = get_medicare_rate_for_facility(facility_id, row["cpt_code"])
    gross = row.get("gross_charge")
    markup = (gross / medicare) if (gross is not None and medicare and medicare > 0) else None
    year = data_year or date.today().year

    with get_db() as db:
        db.execute(
            """
            INSERT INTO hospital_prices (
                facility_id, cpt_code, description, gross_charge, cash_price,
                min_negotiated_rate, max_negotiated_rate, avg_negotiated_rate,
                medicare_rate, markup_vs_medicare, data_year,
                facility_type, medicare_benchmark_type, medicare_benchmark_rate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(facility_id, cpt_code, data_year) DO UPDATE SET
                description=excluded.description,
                gross_charge=excluded.gross_charge,
                cash_price=excluded.cash_price,
                min_negotiated_rate=excluded.min_negotiated_rate,
                max_negotiated_rate=excluded.max_negotiated_rate,
                avg_negotiated_rate=excluded.avg_negotiated_rate,
                medicare_rate=excluded.medicare_rate,
                markup_vs_medicare=excluded.markup_vs_medicare,
                facility_type='hospital',
                medicare_benchmark_type='opps',
                medicare_benchmark_rate=excluded.medicare_rate
            """,
            (
                facility_id,
                row["cpt_code"],
                row.get("description"),
                row.get("gross_charge"),
                row.get("cash_price"),
                row.get("min_negotiated_rate"),
                row.get("max_negotiated_rate"),
                row.get("avg_negotiated_rate"),
                medicare,
                markup,
                year,
                "hospital",
                "opps",
                medicare,
            ),
        )
        # Backward-compatible mirror.
        db.execute(
            """
            INSERT INTO hospital_procedure_prices (
                facility_id, cpt_code, description, gross_charge, cash_price,
                medicare_rate, avg_negotiated_rate, min_negotiated_rate,
                max_negotiated_rate, state_avg_rate, last_updated
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_DATE)
            ON CONFLICT(facility_id, cpt_code) DO UPDATE SET
                description=excluded.description,
                gross_charge=excluded.gross_charge,
                cash_price=excluded.cash_price,
                medicare_rate=excluded.medicare_rate,
                avg_negotiated_rate=excluded.avg_negotiated_rate,
                min_negotiated_rate=excluded.min_negotiated_rate,
                max_negotiated_rate=excluded.max_negotiated_rate,
                last_updated=CURRENT_DATE
            """,
            (
                facility_id,
                row["cpt_code"],
                row.get("description"),
                row.get("gross_charge"),
                row.get("cash_price"),
                medicare,
                row.get("avg_negotiated_rate"),
                row.get("min_negotiated_rate"),
                row.get("max_negotiated_rate"),
                None,
            ),
        )


def upsert_facility_procedure_price(
    facility_id: str,
    row: dict,
    facility_type: str,
    data_year: int | None = None,
) -> None:
    ftype = (facility_type or "hospital").strip().lower()
    if ftype not in {"hospital", "asc", "imaging_center"}:
        ftype = "hospital"
    raw_fid = str(facility_id or "").strip()
    if not raw_fid:
        return
    facility_id = normalize_facility_id(raw_fid) if ftype == "hospital" else raw_fid
    if not facility_id:
        return
    benchmark_type, benchmark_rate = resolve_benchmark_for_row(facility_id, ftype, row)
    gross = row.get("gross_charge")
    markup = (gross / benchmark_rate) if (gross is not None and benchmark_rate and benchmark_rate > 0) else None
    year = data_year or date.today().year

    with get_db() as db:
        db.execute(
            """
            INSERT INTO procedure_prices (
                facility_id, cpt_code, description, gross_charge, cash_price,
                min_negotiated_rate, max_negotiated_rate, avg_negotiated_rate,
                medicare_rate, markup_vs_medicare, data_year,
                facility_type, medicare_benchmark_type, medicare_benchmark_rate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(facility_id, cpt_code, data_year) DO UPDATE SET
                description=excluded.description,
                gross_charge=excluded.gross_charge,
                cash_price=excluded.cash_price,
                min_negotiated_rate=excluded.min_negotiated_rate,
                max_negotiated_rate=excluded.max_negotiated_rate,
                avg_negotiated_rate=excluded.avg_negotiated_rate,
                medicare_rate=excluded.medicare_rate,
                markup_vs_medicare=excluded.markup_vs_medicare,
                facility_type=excluded.facility_type,
                medicare_benchmark_type=excluded.medicare_benchmark_type,
                medicare_benchmark_rate=excluded.medicare_benchmark_rate
            """,
            (
                facility_id,
                row["cpt_code"],
                row.get("description"),
                row.get("gross_charge"),
                row.get("cash_price"),
                row.get("min_negotiated_rate"),
                row.get("max_negotiated_rate"),
                row.get("avg_negotiated_rate"),
                benchmark_rate,
                markup,
                year,
                ftype,
                benchmark_type,
                benchmark_rate,
            ),
        )

    if ftype == "hospital":
        upsert_hospital_price(facility_id, row, data_year=year)


def _parse_cms_lat_lon(row: dict) -> tuple[float | None, float | None]:
    """Extract lat/lon from CMS row. Tries explicit columns then 'Location' field."""
    lat = parse_float(first(row, ("Latitude", "lat", "LAT")))
    lon = parse_float(first(row, ("Longitude", "Long", "LON", "lng", "Lon")))
    if lat is not None and lon is not None:
        return lat, lon
    # CMS sometimes encodes as "POINT (lon lat)" or "lat, lon"
    loc = str(first(row, ("Location", "location")) or "").strip()
    if not loc:
        return None, None
    # POINT (-97.512 36.567) format
    m = re.search(r"POINT\s*\(\s*(-?\d+\.?\d*)\s+(-?\d+\.?\d*)\s*\)", loc, re.I)
    if m:
        return float(m.group(2)), float(m.group(1))  # lat, lon (POINT is lon lat)
    # "lat, lon" format
    parts = loc.split(",")
    if len(parts) == 2:
        try:
            return float(parts[0].strip()), float(parts[1].strip())
        except ValueError:
            pass
    return None, None


def load_cms_general(path: str) -> int:
    rows = load_csv_rows(path)
    count = 0
    for row in rows:
        fid = first(row, ("Facility ID", "facility_id", "ccn"))
        name = first(row, ("Facility Name", "Hospital Name", "name"))
        state = first(row, ("State", "state"))
        city = first(row, ("City", "City/Town", "city"))
        if not fid or not name or not state or not city:
            continue
        lat, lon = _parse_cms_lat_lon(row)
        upsert_hospital_row(
            {
                "facility_id": fid,
                "name": str(name).strip(),
                "address": first(row, ("Address", "Facility Address", "address")),
                "city": city,
                "state": state,
                "zip": first(row, ("ZIP Code", "Zip Code", "zip")),
                "county": first(row, ("County Name", "county")),
                "phone": first(row, ("Phone Number", "phone")),
                "hospital_type": first(row, ("Hospital Type", "hospital_type")),
                "ownership": first(row, ("Hospital Ownership", "ownership")),
                "emergency_services": first(row, ("Emergency Services", "emergency_services")),
                "bed_count": parse_int(first(row, ("Number of Beds", "bed_count"))),
                "teaching_status": first(row, ("Teaching Status", "teaching_status")),
                "system_affiliation": first(row, ("System Affiliation", "system_affiliation")),
                "cms_star_rating": parse_int(first(row, ("Hospital overall rating", "Overall Rating", "overall_rating"))),
                "slug": slugify(f"{name}-{city}"),
                "state_slug": state_slug_from_code(str(state)),
                "city_slug": city_slug_from_name(str(city)),
                "cms_data_updated": first(row, ("Last Updated", "Date", "last_updated")),
                "lat": lat,
                "lon": lon,
            }
        )
        count += 1

    log_refresh("cms_general", count, "success")
    return count


def load_hcahps(path: str) -> int:
    rows = load_csv_rows(path)
    count = 0
    with get_db() as db:
        for row in rows:
            fid = normalize_facility_id(first(row, ("Facility ID", "facility_id", "ccn")))
            if not fid:
                continue
            db.execute(
                """
                INSERT INTO hcahps_scores (
                    facility_id, overall_rating_pct_9_10, overall_rating_pct_7_8,
                    overall_rating_pct_1_6, recommend_yes, doctor_communication_top,
                    nurse_communication_top, staff_responsiveness_top,
                    medicine_communication_top, discharge_info_top, care_transition_top,
                    hospital_cleanliness_top, hospital_quietness_top,
                    survey_response_count, survey_period, data_updated
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, COALESCE(?, CURRENT_DATE))
                ON CONFLICT(facility_id) DO UPDATE SET
                    overall_rating_pct_9_10=excluded.overall_rating_pct_9_10,
                    overall_rating_pct_7_8=excluded.overall_rating_pct_7_8,
                    overall_rating_pct_1_6=excluded.overall_rating_pct_1_6,
                    recommend_yes=excluded.recommend_yes,
                    doctor_communication_top=excluded.doctor_communication_top,
                    nurse_communication_top=excluded.nurse_communication_top,
                    staff_responsiveness_top=excluded.staff_responsiveness_top,
                    medicine_communication_top=excluded.medicine_communication_top,
                    discharge_info_top=excluded.discharge_info_top,
                    care_transition_top=excluded.care_transition_top,
                    hospital_cleanliness_top=excluded.hospital_cleanliness_top,
                    hospital_quietness_top=excluded.hospital_quietness_top,
                    survey_response_count=excluded.survey_response_count,
                    survey_period=excluded.survey_period,
                    data_updated=excluded.data_updated
                """,
                (
                    fid,
                    numeric_by_patterns(row, ("overall", "9", "10"))
                    or numeric_by_patterns(row, ("h_hsp_rating_9_10",)),
                    numeric_by_patterns(row, ("overall", "7", "8"))
                    or numeric_by_patterns(row, ("h_hsp_rating_7_8",)),
                    numeric_by_patterns(row, ("overall", "1", "6"))
                    or numeric_by_patterns(row, ("h_hsp_rating_0_6",)),
                    numeric_by_patterns(row, ("recommend",))
                    or numeric_by_patterns(row, ("recmnd",))
                    or numeric_by_patterns(row, ("h_recmnd_dy_p",)),
                    numeric_by_patterns(row, ("doctor", "communication"))
                    or numeric_by_patterns(row, ("h_comp_1",)),
                    numeric_by_patterns(row, ("nurse", "communication"))
                    or numeric_by_patterns(row, ("h_comp_2",)),
                    numeric_by_patterns(row, ("staff", "responsiveness"))
                    or numeric_by_patterns(row, ("h_comp_3",)),
                    numeric_by_patterns(row, ("medicine", "communication"))
                    or numeric_by_patterns(row, ("h_comp_5",)),
                    numeric_by_patterns(row, ("discharge", "information"))
                    or numeric_by_patterns(row, ("h_comp_6",)),
                    numeric_by_patterns(row, ("care", "transition"))
                    or numeric_by_patterns(row, ("h_comp_7",)),
                    numeric_by_patterns(row, ("cleanliness",))
                    or numeric_by_patterns(row, ("h_comp_8",)),
                    numeric_by_patterns(row, ("quietness",))
                    or numeric_by_patterns(row, ("h_comp_9",)),
                    parse_int(first(row, ("survey_response_count", "Survey Response Count"))),
                    first(row, ("survey_period", "Survey Period")),
                    first(row, ("Last Updated", "data_updated", "last_updated")),
                ),
            )
            # mirror legacy
            db.execute(
                """
                INSERT INTO hospital_quality (
                    facility_id, hcahps_summary, patient_experience_score,
                    readmission_score, mortality_score, updated_at
                ) VALUES (?, ?, ?, ?, ?, COALESCE(?, CURRENT_DATE))
                ON CONFLICT(facility_id) DO UPDATE SET
                    hcahps_summary=excluded.hcahps_summary,
                    patient_experience_score=excluded.patient_experience_score,
                    readmission_score=excluded.readmission_score,
                    mortality_score=excluded.mortality_score,
                    updated_at=excluded.updated_at
                """,
                (
                    fid,
                    first(row, ("HCAHPS Summary Star Rating", "hcahps_summary")),
                    numeric_by_patterns(row, ("recommend",))
                    or numeric_by_patterns(row, ("recmnd",))
                    or numeric_by_patterns(row, ("h_recmnd_dy_p",)),
                    parse_float(first(row, ("readmission_score", "Readmission Score"))),
                    parse_float(first(row, ("mortality_score", "Mortality Score"))),
                    first(row, ("Last Updated", "data_updated", "last_updated")),
                ),
            )
            count += 1

    log_refresh("hcahps", count, "success")
    return count


def load_cost_reports(path: str) -> int:
    rows = load_csv_rows(path)
    count = 0
    with get_db() as db:
        for row in rows:
            fid = normalize_facility_id(first(row, ("Facility ID", "facility_id", "ccn")))
            if not fid:
                continue
            db.execute(
                """
                INSERT INTO hospital_financials (
                    facility_id, total_charges, total_revenue, net_patient_revenue,
                    charity_care_charges, charity_care_costs, charity_care_pct_revenue,
                    bad_debt, cost_to_charge_ratio, operating_margin,
                    has_financial_assistance, fa_income_threshold, fa_application_url,
                    ein, cost_report_year, data_updated,
                    charity_care_amount, charity_care_pct, nonprofit_status,
                    has_financial_assistance_policy, financial_assistance_url, irs_990_url
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, COALESCE(?, CURRENT_DATE), ?, ?, ?, ?, ?, ?)
                ON CONFLICT(facility_id) DO UPDATE SET
                    total_charges=excluded.total_charges,
                    total_revenue=excluded.total_revenue,
                    net_patient_revenue=excluded.net_patient_revenue,
                    charity_care_charges=excluded.charity_care_charges,
                    charity_care_costs=excluded.charity_care_costs,
                    charity_care_pct_revenue=excluded.charity_care_pct_revenue,
                    bad_debt=excluded.bad_debt,
                    cost_to_charge_ratio=excluded.cost_to_charge_ratio,
                    operating_margin=excluded.operating_margin,
                    has_financial_assistance=excluded.has_financial_assistance,
                    fa_income_threshold=excluded.fa_income_threshold,
                    fa_application_url=excluded.fa_application_url,
                    ein=excluded.ein,
                    cost_report_year=excluded.cost_report_year,
                    data_updated=excluded.data_updated,
                    charity_care_amount=excluded.charity_care_amount,
                    charity_care_pct=excluded.charity_care_pct,
                    nonprofit_status=excluded.nonprofit_status,
                    has_financial_assistance_policy=excluded.has_financial_assistance_policy,
                    financial_assistance_url=excluded.financial_assistance_url,
                    irs_990_url=excluded.irs_990_url
                """,
                (
                    fid,
                    parse_float(first(row, ("Total Charges", "total_charges"))),
                    parse_float(first(row, ("Total Revenue", "total_revenue"))),
                    parse_float(first(row, ("Net Patient Revenue", "net_patient_revenue"))),
                    parse_float(first(row, ("Charity Care Charges", "charity_care_charges"))),
                    parse_float(first(row, ("Charity Care Costs", "charity_care_costs"))),
                    parse_float(first(row, ("Charity Care Percent", "charity_care_pct_revenue", "charity_care_pct"))),
                    parse_float(first(row, ("Bad Debt", "bad_debt"))),
                    parse_float(first(row, ("Cost to Charge Ratio", "cost_to_charge_ratio"))),
                    parse_float(first(row, ("Operating Margin", "operating_margin"))),
                    parse_int(first(row, ("Has Financial Assistance Policy", "has_financial_assistance"))),
                    first(row, ("FA Income Threshold", "fa_income_threshold")),
                    first(row, ("Financial Assistance URL", "fa_application_url", "financial_assistance_url")),
                    first(row, ("EIN", "ein")),
                    parse_int(first(row, ("Cost Report Year", "cost_report_year"))),
                    first(row, ("Last Updated", "data_updated", "last_updated")),
                    parse_float(first(row, ("Charity Care Amount", "charity_care_amount"))),
                    parse_float(first(row, ("Charity Care Percent", "charity_care_pct"))),
                    parse_int(first(row, ("Nonprofit Status", "nonprofit_status"))),
                    parse_int(first(row, ("Has Financial Assistance Policy", "has_financial_assistance_policy"))),
                    first(row, ("Financial Assistance URL", "financial_assistance_url")),
                    first(row, ("IRS 990 URL", "irs_990_url")),
                ),
            )
            count += 1

    log_refresh("cost_reports", count, "success")
    return count


def load_provider_of_services(path: str) -> int:
    rows = load_csv_rows(path)
    count = 0
    with get_db() as db:
        for row in rows:
            fid = normalize_facility_id(first(row, ("Facility ID", "facility_id", "ccn", "Provider Number")))
            if not fid:
                continue
            bed_count = parse_int(first(row, ("Bed Count", "bed_count", "Beds")))
            teaching = first(row, ("Teaching Status", "teaching_status", "Residency Program"))
            system = first(row, ("System Affiliation", "system_affiliation", "Chain Organization"))
            db.execute(
                """
                UPDATE hospitals
                SET bed_count = COALESCE(?, bed_count),
                    teaching_status = COALESCE(?, teaching_status),
                    system_affiliation = COALESCE(?, system_affiliation),
                    updated_at = CURRENT_TIMESTAMP
                WHERE facility_id = ?
                """,
                (bed_count, teaching, system, fid),
            )
            db.execute(
                """
                UPDATE hospital_directory
                SET bed_count = COALESCE(?, bed_count),
                    teaching_status = COALESCE(?, teaching_status),
                    system_affiliation = COALESCE(?, system_affiliation)
                WHERE facility_id = ?
                """,
                (bed_count, teaching, system, fid),
            )
            count += 1

    log_refresh("provider_of_services", count, "success")
    return count


def load_medicare_rates(path: str, effective_year: int | None = None) -> int:
    rows = load_csv_rows(path)
    count = 0
    with get_db() as db:
        for row in rows:
            cpt = first(row, ("cpt_code", "CPT", "HCPCS", "code"))
            locality = first(row, ("locality", "Locality", "Carrier Locality")) or "0000000"
            if not cpt:
                continue
            year = effective_year or parse_int(first(row, ("effective_year", "year", "Year"))) or date.today().year
            db.execute(
                """
                INSERT INTO medicare_rates (
                    cpt_code, description, locality, state, non_facility_rate, facility_rate, effective_year
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(cpt_code, locality, effective_year) DO UPDATE SET
                    description=excluded.description,
                    state=excluded.state,
                    non_facility_rate=excluded.non_facility_rate,
                    facility_rate=excluded.facility_rate
                """,
                (
                    str(cpt).strip().upper(),
                    first(row, ("description", "Description")),
                    locality,
                    first(row, ("state", "State")),
                    parse_float(first(row, ("non_facility_rate", "Non Facility Rate"))),
                    parse_float(first(row, ("facility_rate", "Facility Rate"))),
                    year,
                ),
            )
            count += 1

    log_refresh("medicare_rates", count, "success")
    return count


def load_transparency_index(path: str) -> int:
    rows = load_csv_rows(path)
    count = 0
    with get_db() as db:
        for row in rows:
            fid = normalize_facility_id(first(row, ("facility_id", "Facility ID", "ccn")))
            if not fid:
                continue
            url = first(row, ("file_url", "url", "standard_charges_url", "machine_readable_url"))
            db.execute(
                """
                INSERT INTO transparency_files (
                    facility_id, file_url, parse_status, file_format, last_downloaded
                ) VALUES (?, ?, 'pending', NULL, CURRENT_DATE)
                ON CONFLICT(facility_id) DO UPDATE SET
                    file_url=excluded.file_url,
                    parse_status='pending',
                    last_downloaded=CURRENT_DATE
                """,
                (fid, url),
            )
            ftype_row = db.execute(
                "SELECT facility_type FROM facilities WHERE facility_id = ? LIMIT 1",
                (fid,),
            ).fetchone()
            facility_type = (ftype_row["facility_type"] if ftype_row and ftype_row["facility_type"] else "hospital")
            db.execute(
                """
                INSERT INTO transparency_parse_results (
                    facility_id, facility_type, file_url, parse_status, last_downloaded
                ) VALUES (?, ?, ?, 'pending', CURRENT_DATE)
                ON CONFLICT(facility_id) DO UPDATE SET
                    facility_type=excluded.facility_type,
                    file_url=excluded.file_url,
                    parse_status='pending',
                    last_downloaded=CURRENT_DATE,
                    updated_at=CURRENT_TIMESTAMP
                """,
                (fid, facility_type, url),
            )
            count += 1

    log_refresh("transparency_index", count, "success")
    return count


def select_top_hospitals_by_beds(limit: int = 300) -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            """
            SELECT facility_id, name, state, city, bed_count
            FROM hospitals
            ORDER BY COALESCE(bed_count, 0) DESC, name
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    return [dict(r) for r in rows]


def select_facilities_for_transparency(
    facility_types: tuple[str, ...] = ("hospital", "asc", "imaging_center"),
    limit: int | None = None,
) -> list[dict]:
    placeholders = ",".join("?" for _ in facility_types)
    limit_sql = "LIMIT ?" if limit else ""
    params: list[object] = [*facility_types]
    if limit:
        params.append(limit)
    with get_db() as db:
        rows = db.execute(
            f"""
            SELECT facility_id, facility_type, name, slug
            FROM facilities
            WHERE facility_type IN ({placeholders})
            ORDER BY CASE WHEN facility_type = 'hospital' THEN 0 WHEN facility_type = 'asc' THEN 1 ELSE 2 END,
                     name
            {limit_sql}
            """,
            tuple(params),
        ).fetchall()
    return [dict(r) for r in rows]


def _update_parse_result(
    db,
    facility_id: str,
    facility_type: str,
    file_url: str | None,
    *,
    file_format: str | None = None,
    file_size_mb: float | None = None,
    has_standard_codes: int | None = None,
    parse_status: str,
    parse_notes: str | None = None,
    row_count: int | None = None,
    procedures_extracted: int | None = None,
) -> None:
    db.execute(
        """
        INSERT INTO transparency_parse_results (
            facility_id, facility_type, file_url, file_format, file_size_mb,
            has_standard_codes, parse_status, parse_notes, row_count, procedures_extracted,
            last_parsed, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_DATE, CURRENT_TIMESTAMP)
        ON CONFLICT(facility_id) DO UPDATE SET
            facility_type=excluded.facility_type,
            file_url=excluded.file_url,
            file_format=excluded.file_format,
            file_size_mb=excluded.file_size_mb,
            has_standard_codes=excluded.has_standard_codes,
            parse_status=excluded.parse_status,
            parse_notes=excluded.parse_notes,
            row_count=excluded.row_count,
            procedures_extracted=excluded.procedures_extracted,
            last_parsed=CURRENT_DATE,
            updated_at=CURRENT_TIMESTAMP
        """,
        (
            facility_id,
            facility_type,
            file_url,
            file_format,
            file_size_mb,
            has_standard_codes,
            parse_status,
            parse_notes,
            row_count,
            procedures_extracted,
        ),
    )


def _update_hospital_transparency_file(
    db,
    facility_id: str,
    file_url: str | None,
    *,
    file_format: str | None = None,
    file_size_mb: float | None = None,
    has_standard_codes: int | None = None,
    parse_status: str,
    parse_notes: str | None = None,
    row_count: int | None = None,
    procedures_extracted: int | None = None,
) -> None:
    db.execute(
        """
        INSERT INTO transparency_files (
            facility_id, file_url, file_format, file_size_mb, has_standard_codes,
            parse_status, parse_notes, row_count, procedures_extracted, last_parsed
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_DATE)
        ON CONFLICT(facility_id) DO UPDATE SET
            file_url=excluded.file_url,
            file_format=excluded.file_format,
            file_size_mb=excluded.file_size_mb,
            has_standard_codes=excluded.has_standard_codes,
            parse_status=excluded.parse_status,
            parse_notes=excluded.parse_notes,
            row_count=excluded.row_count,
            procedures_extracted=excluded.procedures_extracted,
            last_parsed=CURRENT_DATE
        """,
        (
            facility_id,
            file_url,
            file_format,
            file_size_mb,
            has_standard_codes,
            parse_status,
            parse_notes,
            row_count,
            procedures_extracted,
        ),
    )


def _resolve_file_url(db, facility_id: str, facility_type: str) -> str | None:
    pr = db.execute(
        "SELECT file_url FROM transparency_parse_results WHERE facility_id = ?",
        (facility_id,),
    ).fetchone()
    if pr and pr["file_url"]:
        return str(pr["file_url"])
    if facility_type == "hospital":
        tf = db.execute(
            "SELECT file_url FROM transparency_files WHERE facility_id = ?",
            (facility_id,),
        ).fetchone()
        if tf and tf["file_url"]:
            return str(tf["file_url"])
    return None


def _guess_local_file(files_dir: str, facility_id: str, slug: str | None) -> str | None:
    if not files_dir:
        return None
    patterns = [facility_id, normalize_facility_id(facility_id)]
    if slug:
        patterns.append(slug)
    for p in patterns:
        if not p:
            continue
        for ext in ("csv", "json", "xlsx"):
            matches = glob(os.path.join(files_dir, f"*{p}*.{ext}"))
            if matches:
                return matches[0]
    return None


def parse_transparency_file(path: str) -> tuple[list[dict], str, str]:
    fmt = detect_file_format(path)
    if fmt == "unknown":
        return [], fmt, "unsupported_format"

    rows = load_rows_by_format(path, fmt)
    if not rows:
        return [], fmt, "empty_or_unreadable"

    normalized = normalize_price_rows(rows)
    if not normalized:
        return [], fmt, "no_standard_codes"

    extracted = [r for r in normalized if r["cpt_code"] in TARGET_PROCEDURES]
    if not extracted:
        extracted = normalized[:200]
    return extracted, fmt, "parsed"


def refresh_top300_transparency(files_dir: str = "", data_year: int | None = None) -> dict:
    selected = [{"facility_id": r["facility_id"], "facility_type": "hospital", "slug": None} for r in select_top_hospitals_by_beds(limit=300)]
    return refresh_facility_transparency(selected=selected, files_dir=files_dir, data_year=data_year)


def refresh_facility_transparency(
    selected: list[dict] | None = None,
    files_dir: str = "",
    data_year: int | None = None,
    facility_types: tuple[str, ...] = ("hospital", "asc", "imaging_center"),
    limit: int | None = None,
) -> dict:
    selected = selected or select_facilities_for_transparency(facility_types=facility_types, limit=limit)
    parsed = 0
    failed = 0
    missing = 0

    with get_db() as db:
        for item in selected:
            facility_type = (item.get("facility_type") or "hospital").strip().lower()
            raw_fid = str(item.get("facility_id") or "").strip()
            fid = normalize_facility_id(raw_fid) if facility_type == "hospital" else raw_fid
            if not fid:
                continue
            file_url = _resolve_file_url(db, fid, facility_type)
            local_path = None
            temp_download = None

            if file_url and (file_url.startswith("/") or file_url.startswith(".")):
                local_path = file_url
            elif file_url and files_dir:
                local_path = os.path.join(files_dir, os.path.basename(file_url))
            elif file_url and str(file_url).startswith(("http://", "https://")):
                parsed_url = urlparse(str(file_url))
                ext = os.path.splitext(parsed_url.path)[1].lower()
                if ext not in (".csv", ".xlsx", ".json"):
                    ext = ".csv"
                try:
                    with urlopen(str(file_url), timeout=20) as resp:
                        body = resp.read()
                    if body:
                        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
                            tmp.write(body)
                            temp_download = tmp.name
                            local_path = temp_download
                except (TimeoutError, URLError, OSError):
                    _update_parse_result(
                        db,
                        fid,
                        facility_type,
                        file_url,
                        parse_status="failed",
                        parse_notes="download_failed",
                    )
                    if facility_type == "hospital":
                        _update_hospital_transparency_file(
                            db,
                            fid,
                            file_url,
                            parse_status="failed",
                            parse_notes="download_failed",
                        )
                    failed += 1
                    continue

            if not local_path:
                local_path = _guess_local_file(files_dir, fid, item.get("slug"))

            if not local_path or not os.path.exists(local_path):
                if temp_download and os.path.exists(temp_download):
                    try:
                        os.remove(temp_download)
                    except OSError:
                        pass
                _update_parse_result(
                    db,
                    fid,
                    facility_type,
                    file_url,
                    parse_status="not_found",
                    parse_notes="File missing in local run",
                )
                if facility_type == "hospital":
                    _update_hospital_transparency_file(
                        db,
                        fid,
                        file_url,
                        parse_status="not_found",
                        parse_notes="File missing in local run",
                    )
                missing += 1
                continue

            rows, fmt, status = parse_transparency_file(local_path)
            if status != "parsed":
                if temp_download and os.path.exists(temp_download):
                    try:
                        os.remove(temp_download)
                    except OSError:
                        pass
                _update_parse_result(
                    db,
                    fid,
                    facility_type,
                    file_url,
                    file_format=fmt,
                    parse_status=status,
                    parse_notes=status,
                    row_count=0,
                    procedures_extracted=0,
                )
                if facility_type == "hospital":
                    _update_hospital_transparency_file(
                        db,
                        fid,
                        file_url,
                        file_format=fmt,
                        parse_status=status,
                        parse_notes=status,
                        row_count=0,
                        procedures_extracted=0,
                    )
                failed += 1
                continue

            for item in rows:
                upsert_facility_procedure_price(fid, item, facility_type, data_year=data_year)

            size_mb = (os.path.getsize(local_path) / (1024 * 1024)) if os.path.exists(local_path) else None
            _update_parse_result(
                db,
                fid,
                facility_type,
                file_url,
                file_format=fmt,
                file_size_mb=size_mb,
                has_standard_codes=1,
                parse_status="parsed",
                parse_notes=None,
                row_count=len(rows),
                procedures_extracted=len(rows),
            )
            if facility_type == "hospital":
                _update_hospital_transparency_file(
                    db,
                    fid,
                    file_url,
                    file_format=fmt,
                    file_size_mb=size_mb,
                    has_standard_codes=1,
                    parse_status="parsed",
                    parse_notes=None,
                    row_count=len(rows),
                    procedures_extracted=len(rows),
                )
            parsed += 1
            if temp_download and os.path.exists(temp_download):
                try:
                    os.remove(temp_download)
                except OSError:
                    pass

    total = len(selected)
    log_refresh(
        "transparency_refresh",
        parsed,
        "partial" if (failed or missing) else "success",
        f"selected={total} parsed={parsed} failed={failed} missing={missing}",
    )
    return {
        "selected": total,
        "parsed": parsed,
        "failed": failed,
        "missing": missing,
    }
