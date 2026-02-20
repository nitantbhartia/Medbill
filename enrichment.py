"""
Hospital data enrichment pipeline.

Phase 1 — CMS Core Data (Tier 1: Easy fields):
  - CMS Provider of Services (POS) file: ownership, coordinates, bed count, address
  - CMS Care Compare API: star ratings, quality measures

Phase 2 — Secondary Data (Tier 2: Medium fields):
  - HCRIS cost reports: charity care percentage
  - Compliance status: derived from existing transparency_files data
  - PE ownership: from pe_ownership reference table
  - Address standardization

Run via: python enrichment.py
Or import and call run_phase1() / run_phase2() directly.
"""

from __future__ import annotations

import csv
import io
import json
import logging
import re
import urllib.request
from datetime import date
from difflib import SequenceMatcher

from db import get_db

log = logging.getLogger(__name__)

# CMS POS file download endpoint (data.cms.gov API)
CMS_POS_API = (
    "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities"
    "/provider-of-services-file-hospital-non-hospital-facilities"
    "/api/1/datastore/query/fc9c4f94-3527-481b-a2a6-7f8e01dcfe52/0"
)

# CMS Care Compare hospital quality API
CMS_CARE_COMPARE_API = "https://data.cms.gov/provider-data/api/1/datastore/query/xubh-q36u/0"

# CMS GNRL_CNTL_TYPE_CD → display value mapping
OWNERSHIP_CODE_MAP = {
    "01": "Nonprofit (Church)",
    "02": "Nonprofit (Private)",
    "03": "Nonprofit (Other)",
    "04": "For-profit (Individual)",
    "05": "For-profit (Corporation)",
    "06": "For-profit (Partnership)",
    "07": "For-profit (Other)",
    "08": "Government (Federal)",
    "09": "Government (City)",
    "10": "Government (County)",
    "11": "Government (State)",
    "12": "Government (Hospital District)",
    "13": "Government (City/County)",
}

# Group ownership codes for display
OWNERSHIP_GROUP_MAP = {
    "01": "Nonprofit",
    "02": "Nonprofit",
    "03": "Nonprofit",
    "04": "For-profit",
    "05": "For-profit",
    "06": "For-profit",
    "07": "For-profit",
    "08": "Government (Public)",
    "09": "Government (Public)",
    "10": "Government (Public)",
    "11": "Government (Public)",
    "12": "Government (Public)",
    "13": "Government (Public)",
}

# Hospital size classification by certified bed count
HOSPITAL_SIZE_MAP = [
    (25, "Critical Access / Small"),
    (100, "Community (Small)"),
    (300, "Community (Medium)"),
    (500, "Regional Medical Center"),
]

# Suffixes to strip during name normalization for matching
_STRIP_SUFFIXES = (
    r"\b(?:inc|llc|corp|corporation|system|health|hospital|medical|center|regional|"
    r"authority|district|services|care|community|memorial|general|saint|st|mount|mt)\b"
)

# Continental US / AK / HI coordinate bounds for validation
_CONUS_LAT = (24.0, 50.0)
_CONUS_LON = (-125.0, -65.0)
_AK_LAT = (51.0, 72.0)
_AK_LON = (-170.0, -130.0)
_HI_LAT = (18.0, 23.5)
_HI_LON = (-161.0, -154.0)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _normalize_name(name: str) -> str:
    txt = (name or "").lower()
    txt = re.sub(r"[^a-z0-9\s]", " ", txt)
    txt = re.sub(_STRIP_SUFFIXES, " ", txt)
    return re.sub(r"\s+", " ", txt).strip()


def _name_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, _normalize_name(a), _normalize_name(b)).ratio()


def _hospital_size_label(beds: int | None) -> str | None:
    if not beds:
        return None
    for threshold, label in HOSPITAL_SIZE_MAP:
        if beds < threshold:
            return label
    return "Large Academic / Tertiary"


def _format_phone(raw: str | None) -> str | None:
    if not raw:
        return None
    digits = re.sub(r"\D", "", str(raw))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    if len(digits) == 11 and digits[0] == "1":
        return f"({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    return raw.strip() or None


def _title_case_address(raw: str | None) -> str | None:
    if not raw:
        return None
    txt = raw.strip()
    if txt.isupper() or txt.islower():
        txt = txt.title()
    return txt


def _is_valid_coord(lat: float | None, lon: float | None) -> bool:
    if lat is None or lon is None:
        return False
    if _CONUS_LAT[0] <= lat <= _CONUS_LAT[1] and _CONUS_LON[0] <= lon <= _CONUS_LON[1]:
        return True
    if _AK_LAT[0] <= lat <= _AK_LAT[1] and _AK_LON[0] <= lon <= _AK_LON[1]:
        return True
    if _HI_LAT[0] <= lat <= _HI_LAT[1] and _HI_LON[0] <= lon <= _HI_LON[1]:
        return True
    return False


def _fetch_json_paginated(base_url: str, page_size: int = 1000) -> list[dict]:
    """Fetch all pages from a CMS datastore API endpoint."""
    results: list[dict] = []
    offset = 0
    while True:
        url = f"{base_url}?limit={page_size}&offset={offset}"
        log.info("Fetching %s", url)
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                data = json.loads(resp.read())
        except Exception as exc:
            log.error("Failed to fetch %s: %s", url, exc)
            break
        records = data.get("data") or data.get("results") or []
        if not records:
            break
        results.extend(records)
        if len(records) < page_size:
            break
        offset += page_size
    return results


# ---------------------------------------------------------------------------
# Phase 1A — Download and parse CMS POS file
# ---------------------------------------------------------------------------

def load_pos_file(csv_path: str) -> int:
    """
    Parse a local CMS POS CSV and populate cms_pos_enrichment.
    Returns count of rows loaded.
    """
    rows = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            fac_type = (row.get("GNRL_FAC_TYPE_CD") or "").strip()
            # Only load hospitals (01 = general, 02 = long-term, etc.)
            if fac_type not in {"01", "02", "21", "22"}:
                fac_type_raw = fac_type  # keep it but still load
            ccn = (row.get("PRVDR_NUM") or "").strip().zfill(6)
            if not ccn or ccn == "000000":
                continue
            try:
                lat = float(row["LATITUDE"]) if row.get("LATITUDE", "").strip() else None
                lon = float(row["LONGITUDE"]) if row.get("LONGITUDE", "").strip() else None
                beds = int(row["CRTFD_BED_CNT"]) if row.get("CRTFD_BED_CNT", "").strip() else None
            except (ValueError, KeyError):
                lat = lon = beds = None
            rows.append((
                ccn,
                (row.get("FAC_NAME") or "").strip(),
                (row.get("ST_ADR") or "").strip(),
                (row.get("CITY_NAME") or "").strip(),
                (row.get("STATE_CD") or "").strip(),
                (row.get("ZIP_CD") or "").strip()[:5],
                lat,
                lon,
                beds,
                (row.get("GNRL_CNTL_TYPE_CD") or "").strip().zfill(2),
                fac_type,
                (row.get("ORGNL_PRTCPTN_DT") or "").strip() or None,
                (row.get("PHNE_NUM") or "").strip() or None,
            ))

    with get_db() as db:
        db.execute("DELETE FROM cms_pos_enrichment")
        db.executemany(
            """
            INSERT INTO cms_pos_enrichment (
                ccn, fac_name, st_adr, city_name, state_cd, zip_cd,
                latitude, longitude, crtfd_bed_cnt, gnrl_cntl_type_cd,
                gnrl_fac_type_cd, orgnl_prtcptn_dt, phne_num
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            rows,
        )
    log.info("Loaded %d POS records", len(rows))
    return len(rows)


# ---------------------------------------------------------------------------
# Phase 1B — Match POS data to BillKarma hospitals
# ---------------------------------------------------------------------------

def match_pos_to_hospitals() -> dict[str, str]:
    """
    Match cms_pos_enrichment records to hospitals table.
    Returns {facility_id -> ccn} for matched hospitals.
    Logs unmatched hospitals to enrichment_unmatched.
    """
    with get_db() as db:
        hospitals = db.execute(
            "SELECT facility_id, name, city, state FROM hospitals"
        ).fetchall()
        pos_by_ccn = {
            row["ccn"]: dict(row)
            for row in db.execute("SELECT * FROM cms_pos_enrichment").fetchall()
        }

    matched: dict[str, str] = {}   # facility_id -> ccn
    unmatched: list[dict] = []

    # Build name-state index of POS records for fuzzy matching
    pos_by_state: dict[str, list[dict]] = {}
    for ccn, pos in pos_by_ccn.items():
        state = (pos.get("state_cd") or "").upper()
        pos_by_state.setdefault(state, []).append(pos)

    for h in hospitals:
        fid = h["facility_id"]
        state = (h["state"] or "").upper()

        # Match 1: CCN == facility_id (6-digit zero-padded)
        ccn_candidate = str(fid).zfill(6)
        if ccn_candidate in pos_by_ccn:
            matched[fid] = ccn_candidate
            continue

        # Match 2: Fuzzy name + state
        best_ccn = None
        best_score = 0.0
        for pos in pos_by_state.get(state, []):
            score = _name_similarity(h["name"] or "", pos.get("fac_name") or "")
            if score > best_score:
                best_score = score
                best_ccn = pos["ccn"]

        if best_score >= 0.85 and best_ccn:
            matched[fid] = best_ccn
            continue

        unmatched.append({
            "facility_id": fid,
            "name": h["name"],
            "city": h["city"],
            "state": state,
            "reason": f"name_score={best_score:.2f}" if best_ccn else "no_pos_in_state",
        })

    # Log unmatched
    with get_db() as db:
        db.execute("DELETE FROM enrichment_unmatched")
        db.executemany(
            """
            INSERT OR REPLACE INTO enrichment_unmatched (facility_id, name, city, state, reason)
            VALUES (:facility_id, :name, :city, :state, :reason)
            """,
            unmatched,
        )

    total = len(hospitals)
    matched_count = len(matched)
    log.info(
        "POS match: %d/%d hospitals matched (%.1f%%)",
        matched_count, total, 100 * matched_count / total if total else 0,
    )
    return matched


# ---------------------------------------------------------------------------
# Phase 1C — Update ownership type
# ---------------------------------------------------------------------------

def update_ownership_from_pos(matched: dict[str, str]) -> int:
    """Apply CMS ownership codes to hospitals table. Returns update count."""
    updated = 0
    with get_db() as db:
        pos_data = {
            row["ccn"]: dict(row)
            for row in db.execute("SELECT ccn, gnrl_cntl_type_cd, fac_name FROM cms_pos_enrichment").fetchall()
        }
        for fid, ccn in matched.items():
            pos = pos_data.get(ccn)
            if not pos:
                continue
            code = (pos.get("gnrl_cntl_type_cd") or "").strip().lstrip("0").zfill(2)
            if not code or code == "00":
                continue
            ownership_type = OWNERSHIP_GROUP_MAP.get(code, "Unknown")
            ownership_subtype = OWNERSHIP_CODE_MAP.get(code)
            db.execute(
                """
                UPDATE hospitals
                SET ownership_type = ?, ownership_subtype = ?, ownership_code = ?,
                    enrichment_source = 'cms_pos', enrichment_last_run = CURRENT_DATE,
                    enrichment_match_confidence = 'high'
                WHERE facility_id = ?
                """,
                (ownership_type, ownership_subtype, code, fid),
            )
            updated += 1
    log.info("Ownership updated for %d hospitals", updated)
    return updated


# ---------------------------------------------------------------------------
# Phase 1D — Update coordinates
# ---------------------------------------------------------------------------

def update_coordinates_from_pos(matched: dict[str, str]) -> tuple[int, int]:
    """
    Update lat/lon from POS data. Returns (updated_count, flagged_count).
    Flags coordinates outside US bounds to coordinates_validation.
    """
    updated = 0
    flagged = 0
    issues: list[dict] = []

    with get_db() as db:
        pos_data = {
            row["ccn"]: dict(row)
            for row in db.execute(
                "SELECT ccn, latitude, longitude, fac_name, city_name, state_cd FROM cms_pos_enrichment"
            ).fetchall()
        }
        for fid, ccn in matched.items():
            pos = pos_data.get(ccn)
            if not pos:
                continue
            lat = pos.get("latitude")
            lon = pos.get("longitude")
            if lat is None or lon is None:
                continue
            if not _is_valid_coord(lat, lon):
                issues.append({
                    "facility_id": fid,
                    "name": pos.get("fac_name"),
                    "city": pos.get("city_name"),
                    "state": pos.get("state_cd"),
                    "latitude": lat,
                    "longitude": lon,
                    "issue": "out_of_us_bounds",
                })
                flagged += 1
                continue
            db.execute(
                "UPDATE hospitals SET lat = ?, lon = ? WHERE facility_id = ?",
                (lat, lon, fid),
            )
            updated += 1

        # Flag hospitals still missing coords after update (skip already-flagged)
        already_flagged = {i["facility_id"] for i in issues}
        null_coord = db.execute(
            """
            SELECT h.facility_id, h.name, h.city, h.state
            FROM hospitals h
            WHERE h.lat IS NULL AND h.facility_id IS NOT NULL
            """
        ).fetchall()
        for row in null_coord:
            if row["facility_id"] in already_flagged:
                continue
            issues.append({
                "facility_id": row["facility_id"],
                "name": row["name"],
                "city": row["city"],
                "state": row["state"],
                "latitude": None,
                "longitude": None,
                "issue": "null_after_update",
            })

        db.execute("DELETE FROM coordinates_validation")
        db.executemany(
            """
            INSERT OR REPLACE INTO coordinates_validation
                (facility_id, name, city, state, latitude, longitude, issue)
            VALUES (:facility_id, :name, :city, :state, :latitude, :longitude, :issue)
            """,
            issues,
        )

    log.info("Coordinates updated: %d, flagged: %d", updated, flagged)
    return updated, flagged


# ---------------------------------------------------------------------------
# Phase 1E — Update bed count and hospital size
# ---------------------------------------------------------------------------

def update_beds_from_pos(matched: dict[str, str]) -> int:
    """Update bed count and hospital_size classification from POS. Returns update count."""
    updated = 0
    with get_db() as db:
        pos_data = {
            row["ccn"]: dict(row)
            for row in db.execute("SELECT ccn, crtfd_bed_cnt FROM cms_pos_enrichment").fetchall()
        }
        for fid, ccn in matched.items():
            pos = pos_data.get(ccn)
            if not pos:
                continue
            beds = pos.get("crtfd_bed_cnt")
            if beds is None:
                continue
            size_label = _hospital_size_label(int(beds))
            db.execute(
                "UPDATE hospitals SET bed_count = ?, hospital_size = ? WHERE facility_id = ?",
                (beds, size_label, fid),
            )
            updated += 1
    log.info("Bed count updated for %d hospitals", updated)
    return updated


# ---------------------------------------------------------------------------
# Phase 1F — Fetch CMS Care Compare star ratings
# ---------------------------------------------------------------------------

def fetch_care_compare_ratings() -> int:
    """
    Fetch all hospital quality records from CMS Care Compare API.
    Updates cms_star_rating, patient_experience, quality_measures in hospitals table.
    Returns count of hospitals updated.
    """
    records = _fetch_json_paginated(CMS_CARE_COMPARE_API)
    if not records:
        log.warning("No Care Compare records returned")
        return 0

    updated = 0
    with get_db() as db:
        for rec in records:
            ccn = (rec.get("facility_id") or "").strip().zfill(6)
            if not ccn or ccn == "000000":
                continue

            raw_rating = rec.get("overall_rating") or rec.get("overall_star_rating", "")
            try:
                stars = int(raw_rating)
                if not 1 <= stars <= 5:
                    stars = None
            except (ValueError, TypeError):
                stars = None

            raw_exp = (rec.get("patient_experience_rating") or rec.get("patient_experience_national_comparison") or "").strip()
            exp_map = {
                "above": "Above Average",
                "above the national average": "Above Average",
                "same": "Average",
                "same as the national average": "Average",
                "below": "Below Average",
                "below the national average": "Below Average",
            }
            patient_exp = exp_map.get(raw_exp.lower())

            quality_measures = {
                "mortality": rec.get("mortality_national_comparison"),
                "safety": rec.get("safety_of_care_national_comparison"),
                "readmission": rec.get("readmission_national_comparison"),
                "patient_experience": rec.get("patient_experience_national_comparison"),
                "effectiveness": rec.get("effectiveness_of_care_national_comparison"),
                "timeliness": rec.get("timeliness_of_care_national_comparison"),
            }

            db.execute(
                """
                UPDATE hospitals
                SET cms_star_rating = ?,
                    patient_experience = ?,
                    quality_measures = ?,
                    cms_stars_last_updated = CURRENT_DATE
                WHERE facility_id = ?
                """,
                (stars, patient_exp, json.dumps(quality_measures), ccn),
            )
            if db.execute("SELECT changes()").fetchone()[0]:
                updated += 1

    log.info("CMS Care Compare: updated %d hospitals", updated)
    return updated


# ---------------------------------------------------------------------------
# Phase 1G — Run full Phase 1 batch and log results
# ---------------------------------------------------------------------------

def run_phase1(pos_csv_path: str | None = None) -> dict:
    """
    Run full Phase 1 enrichment. If pos_csv_path is None, skips POS steps
    (useful when CMS POS data was already loaded separately).
    Returns summary dict.
    """
    with get_db() as db:
        before = db.execute(
            """
            SELECT
                SUM(CASE WHEN ownership_type IS NOT NULL AND ownership_type != 'Unknown' THEN 1 ELSE 0 END) AS ownership_known,
                SUM(CASE WHEN cms_star_rating IS NOT NULL THEN 1 ELSE 0 END) AS stars_known,
                SUM(CASE WHEN lat IS NOT NULL THEN 1 ELSE 0 END) AS coords_known,
                COUNT(*) AS total
            FROM hospitals
            """
        ).fetchone()

    ownership_updated = 0
    coords_updated = 0
    beds_updated = 0
    matched: dict[str, str] = {}

    if pos_csv_path:
        load_pos_file(pos_csv_path)
        matched = match_pos_to_hospitals()
        ownership_updated = update_ownership_from_pos(matched)
        coords_updated, _ = update_coordinates_from_pos(matched)
        beds_updated = update_beds_from_pos(matched)

    stars_updated = fetch_care_compare_ratings()

    with get_db() as db:
        after = db.execute(
            """
            SELECT
                SUM(CASE WHEN ownership_type IS NOT NULL AND ownership_type != 'Unknown' THEN 1 ELSE 0 END) AS ownership_known,
                SUM(CASE WHEN cms_star_rating IS NOT NULL THEN 1 ELSE 0 END) AS stars_known,
                SUM(CASE WHEN lat IS NOT NULL THEN 1 ELSE 0 END) AS coords_known,
                SUM(CASE WHEN ownership_type IS NULL OR ownership_type = 'Unknown' THEN 1 ELSE 0 END) AS ownership_unknown,
                SUM(CASE WHEN cms_star_rating IS NULL THEN 1 ELSE 0 END) AS stars_null,
                COUNT(*) AS total
            FROM hospitals
            """
        ).fetchone()

        db.execute(
            """
            INSERT INTO enrichment_run_log (
                hospitals_processed, ownership_updated, coordinates_updated,
                stars_updated, ownership_unknown_remaining, stars_not_rated_remaining, errors
            ) VALUES (?, ?, ?, ?, ?, ?, '[]')
            """,
            (
                after["total"],
                ownership_updated,
                coords_updated,
                stars_updated,
                after["ownership_unknown"],
                after["stars_null"],
            ),
        )

    summary = {
        "phase": 1,
        "run_date": str(date.today()),
        "hospitals_processed": after["total"],
        "pos_matched": len(matched),
        "ownership_updated": ownership_updated,
        "coordinates_updated": coords_updated,
        "beds_updated": beds_updated,
        "stars_updated": stars_updated,
        "before": {
            "ownership_known": before["ownership_known"],
            "stars_known": before["stars_known"],
            "coords_known": before["coords_known"],
        },
        "after": {
            "ownership_known": after["ownership_known"],
            "stars_known": after["stars_known"],
            "coords_known": after["coords_known"],
            "ownership_unknown_remaining": after["ownership_unknown"],
            "stars_null_remaining": after["stars_null"],
        },
    }
    log.info("Phase 1 complete: %s", summary)
    return summary


# ---------------------------------------------------------------------------
# Phase 2A — Charity care from HCRIS
# ---------------------------------------------------------------------------

def load_hcris_charity_care(csv_path: str) -> int:
    """
    Load charity care percentages from a pre-extracted HCRIS CSV.
    Expected columns: CCN, CHARITY_CARE_COST, TOTAL_NET_REVENUE, REPORT_YEAR
    Returns count of hospitals updated.
    """
    updated = 0
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        with get_db() as db:
            for row in reader:
                ccn = (row.get("CCN") or "").strip().zfill(6)
                if not ccn or ccn == "000000":
                    continue
                try:
                    charity_cost = float(row.get("CHARITY_CARE_COST") or 0)
                    net_revenue = float(row.get("TOTAL_NET_REVENUE") or 0)
                    report_year = int(row.get("REPORT_YEAR") or 0)
                except (ValueError, TypeError):
                    continue

                if net_revenue <= 0:
                    pct = None
                    reported = True  # has S-10 but revenue=0 (unusual)
                else:
                    pct = round(min((charity_cost / net_revenue) * 100, 99.9), 2)
                    reported = True

                # Update directly by CCN (which equals facility_id for hospitals)
                db.execute(
                    """
                    UPDATE hospitals
                    SET charity_care_pct = ?,
                        charity_care_reported = ?,
                        charity_care_report_year = ?
                    WHERE facility_id = ?
                    """,
                    (pct, 1 if reported else 0, report_year or None, ccn),
                )
                if db.execute("SELECT changes()").fetchone()[0]:
                    updated += 1

    # Mark for-profit hospitals with NULL as "not required to report"
    with get_db() as db:
        db.execute(
            """
            UPDATE hospitals
            SET charity_care_reported = 0
            WHERE charity_care_pct IS NULL
              AND charity_care_reported IS NULL
              AND (ownership_type = 'For-profit' OR ownership_code IN ('04','05','06','07'))
            """
        )

    log.info("HCRIS charity care updated for %d hospitals", updated)
    return updated


# ---------------------------------------------------------------------------
# Phase 2B — Compliance status from transparency file data
# ---------------------------------------------------------------------------

def update_compliance_status() -> int:
    """
    Derive compliance_status for all hospitals from transparency_files table.
    Uses existing parse results — no new downloads needed.
    Returns count updated.
    """
    updated = 0
    with get_db() as db:
        hospitals = db.execute("SELECT facility_id FROM hospitals").fetchall()
        for h in hospitals:
            fid = h["facility_id"]
            tf = db.execute(
                "SELECT parse_status, procedures_extracted, has_standard_codes FROM transparency_files WHERE facility_id = ?",
                (fid,),
            ).fetchone()

            if tf is None:
                status = "Unverified"
                procs = None
            elif tf["parse_status"] == "error" or not tf["procedures_extracted"]:
                status = "Non-compliant"
                procs = 0
            else:
                procs = tf["procedures_extracted"] or 0
                has_codes = bool(tf["has_standard_codes"])
                if procs >= 50 and has_codes:
                    status = "Compliant"
                elif procs > 0:
                    status = "Partial"
                else:
                    status = "Non-compliant"

            db.execute(
                """
                UPDATE hospitals
                SET compliance_status = ?, procedures_in_file = ?,
                    compliance_last_checked = CURRENT_DATE
                WHERE facility_id = ?
                """,
                (status, procs, fid),
            )
            updated += 1

    log.info("Compliance status updated for %d hospitals", updated)
    return updated


# ---------------------------------------------------------------------------
# Phase 2C — PE ownership from pe_ownership table
# ---------------------------------------------------------------------------

def update_pe_ownership() -> int:
    """
    Match pe_ownership records to hospitals and set PE flags.
    Returns count of hospitals marked as PE-owned.
    """
    updated = 0
    with get_db() as db:
        pe_records = db.execute("SELECT * FROM pe_ownership").fetchall()
        if not pe_records:
            log.info("No PE ownership records to apply")
            return 0

        for pe in pe_records:
            ccn = (pe.get("ccn") or "").strip().zfill(6)
            matched_fid = None

            if ccn and ccn != "000000":
                row = db.execute(
                    "SELECT facility_id FROM hospitals WHERE facility_id = ?", (ccn,)
                ).fetchone()
                if row:
                    matched_fid = row["facility_id"]

            if not matched_fid and pe.get("hospital_name"):
                # Fuzzy name match
                candidates = db.execute(
                    "SELECT facility_id, name FROM hospitals LIMIT 5000"
                ).fetchall()
                best_fid = None
                best_score = 0.0
                for c in candidates:
                    score = _name_similarity(pe["hospital_name"], c["name"] or "")
                    if score > best_score:
                        best_score = score
                        best_fid = c["facility_id"]
                if best_score >= 0.9:
                    matched_fid = best_fid

            if not matched_fid:
                continue

            db.execute(
                """
                UPDATE hospitals
                SET is_pe_owned = 1,
                    pe_firm = ?,
                    pe_acquisition_year = ?,
                    pe_exit_year = ?,
                    parent_system = COALESCE(?, parent_system)
                WHERE facility_id = ?
                """,
                (
                    pe.get("pe_firm"),
                    pe.get("acquisition_year"),
                    pe.get("exit_year"),
                    pe.get("current_parent_system"),
                    matched_fid,
                ),
            )
            updated += 1

    log.info("PE ownership applied to %d hospitals", updated)
    return updated


# ---------------------------------------------------------------------------
# Phase 2D — Address standardization from POS data
# ---------------------------------------------------------------------------

def standardize_addresses_from_pos(matched: dict[str, str]) -> int:
    """
    Update address, phone to Title Case using POS as authoritative source.
    Returns update count.
    """
    updated = 0
    with get_db() as db:
        pos_data = {
            row["ccn"]: dict(row)
            for row in db.execute(
                "SELECT ccn, st_adr, city_name, zip_cd, phne_num FROM cms_pos_enrichment"
            ).fetchall()
        }
        for fid, ccn in matched.items():
            pos = pos_data.get(ccn)
            if not pos:
                continue
            address = _title_case_address(pos.get("st_adr"))
            city = _title_case_address(pos.get("city_name"))
            zip_code = (pos.get("zip_cd") or "")[:5] or None
            phone = _format_phone(pos.get("phne_num"))
            db.execute(
                """
                UPDATE hospitals
                SET address = COALESCE(?, address),
                    city = COALESCE(?, city),
                    zip = COALESCE(?, zip),
                    phone = COALESCE(?, phone)
                WHERE facility_id = ?
                """,
                (address, city, zip_code, phone, fid),
            )
            updated += 1

    log.info("Address standardized for %d hospitals", updated)
    return updated


# ---------------------------------------------------------------------------
# Phase 2 — Run all secondary enrichment
# ---------------------------------------------------------------------------

def run_phase2(hcris_csv_path: str | None = None) -> dict:
    """Run full Phase 2 enrichment. Returns summary dict."""
    compliance_updated = update_compliance_status()
    pe_updated = update_pe_ownership()
    charity_updated = 0
    if hcris_csv_path:
        charity_updated = load_hcris_charity_care(hcris_csv_path)

    # Re-run address standardization if POS data was loaded
    addr_updated = 0
    with get_db() as db:
        pos_count = db.execute("SELECT COUNT(*) AS n FROM cms_pos_enrichment").fetchone()["n"]
    if pos_count > 0:
        matched = match_pos_to_hospitals()
        addr_updated = standardize_addresses_from_pos(matched)

    summary = {
        "phase": 2,
        "run_date": str(date.today()),
        "compliance_updated": compliance_updated,
        "pe_ownership_applied": pe_updated,
        "charity_care_updated": charity_updated,
        "addresses_standardized": addr_updated,
    }
    log.info("Phase 2 complete: %s", summary)
    return summary


# ---------------------------------------------------------------------------
# Validation query — coverage check
# ---------------------------------------------------------------------------

def coverage_report() -> dict:
    """Return coverage statistics for all enrichment fields."""
    with get_db() as db:
        row = db.execute(
            """
            SELECT
                COUNT(*) AS total_hospitals,
                SUM(CASE WHEN ownership_type IS NOT NULL AND ownership_type != 'Unknown'
                    THEN 1 ELSE 0 END) AS ownership_known,
                SUM(CASE WHEN cms_star_rating IS NOT NULL THEN 1 ELSE 0 END) AS stars_known,
                SUM(CASE WHEN lat IS NOT NULL THEN 1 ELSE 0 END) AS coords_known,
                SUM(CASE WHEN charity_care_pct IS NOT NULL THEN 1 ELSE 0 END) AS charity_known,
                SUM(CASE WHEN compliance_status IS NOT NULL
                    AND compliance_status != 'Unverified' THEN 1 ELSE 0 END) AS compliance_known,
                SUM(CASE WHEN is_pe_owned = 1 THEN 1 ELSE 0 END) AS pe_owned_count
            FROM hospitals
            """
        ).fetchone()
    return dict(row)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    pos_path = sys.argv[1] if len(sys.argv) > 1 else None
    hcris_path = sys.argv[2] if len(sys.argv) > 2 else None

    p1 = run_phase1(pos_path)
    p2 = run_phase2(hcris_path)
    cov = coverage_report()

    print("\n=== Phase 1 Summary ===")
    print(json.dumps(p1, indent=2))
    print("\n=== Phase 2 Summary ===")
    print(json.dumps(p2, indent=2))
    print("\n=== Coverage Report ===")
    print(json.dumps(cov, indent=2))
