"""Tests for the enrichment pipeline."""

import csv
import io
import json
import os
import tempfile

import pytest

import db as _db
from db import get_db
from enrichment import (
    _format_phone,
    _hospital_size_label,
    _is_valid_coord,
    _name_similarity,
    _normalize_name,
    _title_case_address,
    coverage_report,
    extract_asc_and_imaging_from_pos,
    load_pos_file,
    match_pos_to_hospitals,
    update_beds_from_pos,
    update_compliance_status,
    update_coordinates_from_pos,
    update_ownership_from_pos,
    update_pe_ownership,
    standardize_addresses_from_pos,
    OWNERSHIP_CODE_MAP,
    OWNERSHIP_GROUP_MAP,
)
from hospital_seo import (
    generate_deterministic_tips,
    generate_intro_paragraph,
    _generate_ungraded_intro,
)


# ---------------------------------------------------------------------------
# Helper: write a minimal POS CSV to a temp file
# ---------------------------------------------------------------------------

def _write_pos_csv(rows: list[dict], extra_fields: list[str] | None = None) -> str:
    fields = [
        "PRVDR_NUM", "FAC_NAME", "ST_ADR", "CITY_NAME", "STATE_CD",
        "ZIP_CD", "LATITUDE", "LONGITUDE", "CRTFD_BED_CNT",
        "GNRL_CNTL_TYPE_CD", "GNRL_FAC_TYPE_CD", "ORGNL_PRTCPTN_DT", "PHNE_NUM",
    ]
    if extra_fields:
        for field in extra_fields:
            if field not in fields:
                fields.append(field)
    fd, path = tempfile.mkstemp(suffix=".csv")
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})
    return path


def _seed_hospital(facility_id: str, name: str = "Test Hospital", state: str = "TX", city: str = "Austin") -> None:
    with get_db() as db:
        db.execute(
            """
            INSERT OR IGNORE INTO hospitals
                (facility_id, name, city, state, slug, state_slug, city_slug)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (facility_id, name, city, state, f"test-{facility_id}", state.lower(), city.lower()),
        )


# ---------------------------------------------------------------------------
# Unit tests — pure helpers
# ---------------------------------------------------------------------------

class TestHelpers:
    def test_normalize_name_strips_suffixes(self):
        # "memorial", "hospital", "center" are all in the strip list — result is empty
        assert _normalize_name("Memorial Hospital Center") == ""
        # "medical" and "center" stripped; "saint" kept, "mary s" kept
        result = _normalize_name("Saint Mary's Medical Center")
        assert "medical" not in result
        assert "center" not in result

    def test_name_similarity_exact(self):
        assert _name_similarity("Community Hospital", "Community Hospital") == 1.0

    def test_name_similarity_fuzzy_high(self):
        # Full name vs abbreviated — still substantially similar
        score = _name_similarity("Mercy Medical Center", "Mercy Medical Ctr")
        assert score >= 0.65

    def test_name_similarity_low_for_different(self):
        score = _name_similarity("Cedar Sinai Medical", "Johns Hopkins Hospital")
        assert score < 0.5

    def test_hospital_size_label(self):
        assert _hospital_size_label(10) == "Critical Access / Small"
        assert _hospital_size_label(50) == "Community (Small)"
        assert _hospital_size_label(150) == "Community (Medium)"
        assert _hospital_size_label(400) == "Regional Medical Center"
        assert _hospital_size_label(600) == "Large Academic / Tertiary"
        assert _hospital_size_label(None) is None

    def test_format_phone_10digit(self):
        assert _format_phone("5125551234") == "(512) 555-1234"

    def test_format_phone_11digit(self):
        assert _format_phone("15125551234") == "(512) 555-1234"

    def test_format_phone_none(self):
        assert _format_phone(None) is None

    def test_format_phone_already_formatted(self):
        result = _format_phone("(512) 555-1234")
        assert result == "(512) 555-1234"

    def test_title_case_address_uppercased(self):
        assert _title_case_address("123 MAIN STREET") == "123 Main Street"

    def test_title_case_address_none(self):
        assert _title_case_address(None) is None

    def test_is_valid_coord_conus(self):
        assert _is_valid_coord(37.7749, -122.4194)  # San Francisco

    def test_is_valid_coord_alaska(self):
        assert _is_valid_coord(61.2181, -149.9003)  # Anchorage

    def test_is_valid_coord_hawaii(self):
        assert _is_valid_coord(21.3069, -157.8583)  # Honolulu

    def test_is_valid_coord_out_of_bounds(self):
        assert not _is_valid_coord(0.0, 0.0)

    def test_is_valid_coord_none(self):
        assert not _is_valid_coord(None, None)

    def test_ownership_code_map_complete(self):
        for code in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]:
            assert code in OWNERSHIP_CODE_MAP
            assert code in OWNERSHIP_GROUP_MAP

    def test_ownership_group_nonprofit(self):
        for code in ["01", "02", "03"]:
            assert OWNERSHIP_GROUP_MAP[code] == "Nonprofit"

    def test_ownership_group_forprofit(self):
        for code in ["04", "05", "06", "07"]:
            assert OWNERSHIP_GROUP_MAP[code] == "For-profit"

    def test_ownership_group_government(self):
        for code in ["08", "09", "10", "11", "12", "13"]:
            assert OWNERSHIP_GROUP_MAP[code] == "Government (Public)"


# ---------------------------------------------------------------------------
# POS file loading
# ---------------------------------------------------------------------------

class TestPosFileLoading:
    def test_load_pos_creates_rows(self, tmp_path):
        path = _write_pos_csv([
            {
                "PRVDR_NUM": "450123",
                "FAC_NAME": "Test Hospital",
                "ST_ADR": "100 MAIN ST",
                "CITY_NAME": "HOUSTON",
                "STATE_CD": "TX",
                "ZIP_CD": "77001",
                "LATITUDE": "29.7604",
                "LONGITUDE": "-95.3698",
                "CRTFD_BED_CNT": "250",
                "GNRL_CNTL_TYPE_CD": "02",
                "GNRL_FAC_TYPE_CD": "01",
                "PHNE_NUM": "7135551234",
            }
        ])
        count = load_pos_file(path)
        assert count == 1
        with get_db() as db:
            row = db.execute("SELECT * FROM cms_pos_enrichment WHERE ccn = '450123'").fetchone()
        assert row is not None
        assert row["fac_name"] == "Test Hospital"
        assert row["latitude"] == pytest.approx(29.7604)
        assert row["gnrl_cntl_type_cd"] == "02"
        os.unlink(path)

    def test_load_pos_skips_empty_ccn(self, tmp_path):
        path = _write_pos_csv([
            {"PRVDR_NUM": "", "FAC_NAME": "Ghost Hospital", "STATE_CD": "TX"},
        ])
        count = load_pos_file(path)
        assert count == 0
        os.unlink(path)

    def test_load_pos_zero_pads_ccn(self, tmp_path):
        path = _write_pos_csv([
            {
                "PRVDR_NUM": "1234",  # should zero-pad to 001234
                "FAC_NAME": "Short ID Hospital",
                "STATE_CD": "TX",
                "GNRL_CNTL_TYPE_CD": "05",
                "GNRL_FAC_TYPE_CD": "01",
            }
        ])
        load_pos_file(path)
        with get_db() as db:
            row = db.execute("SELECT ccn FROM cms_pos_enrichment WHERE ccn = '001234'").fetchone()
        assert row is not None
        os.unlink(path)


class TestNonHospitalExtraction:
    def test_extracts_legacy_asc_and_imaging_codes(self):
        with get_db() as db:
            db.execute(
                """
                INSERT OR REPLACE INTO facilities (
                    facility_id, name, city, state, state_slug, city_slug, slug, facility_type
                ) VALUES ('450123', 'Parent Hospital', 'Austin', 'TX', 'tx', 'austin', 'parent-hospital-austin', 'hospital')
                """
            )
            db.execute(
                """
                INSERT OR REPLACE INTO hospitals (
                    facility_id, name, city, state, slug, state_slug, city_slug
                ) VALUES ('450123', 'Parent Hospital', 'Austin', 'TX', 'parent-hospital-austin', 'tx', 'austin')
                """
            )

        path = _write_pos_csv(
            [
                {
                    "PRVDR_NUM": "111111",
                    "FAC_NAME": "Austin Surgery Center",
                    "CITY_NAME": "AUSTIN",
                    "STATE_CD": "TX",
                    "ZIP_CD": "78701",
                    "GNRL_CNTL_TYPE_CD": "05",
                    "GNRL_FAC_TYPE_CD": "17",
                    "ORGNL_PRTCPTN_DT": "20210101",
                    "CRTFCTN_DT": "20210101",
                },
                {
                    "PRVDR_NUM": "222222",
                    "FAC_NAME": "Austin Advanced Imaging",
                    "CITY_NAME": "AUSTIN",
                    "STATE_CD": "TX",
                    "ZIP_CD": "78702",
                    "GNRL_CNTL_TYPE_CD": "05",
                    "GNRL_FAC_TYPE_CD": "28",
                    "ORGNL_PRTCPTN_DT": "20210101",
                    "CRTFCTN_DT": "20210101",
                },
            ],
            extra_fields=["CRTFCTN_DT"],
        )
        counts = extract_asc_and_imaging_from_pos(path, strict_min_expected=0)
        assert counts["asc"] == 1
        assert counts["imaging_center"] == 1
        with get_db() as db:
            asc = db.execute("SELECT facility_type FROM facilities WHERE facility_id = 'asc-111111'").fetchone()
            img = db.execute("SELECT facility_type FROM facilities WHERE facility_id = 'img-222222'").fetchone()
        assert asc["facility_type"] == "asc"
        assert img["facility_type"] == "imaging_center"
        os.unlink(path)

    def test_extracts_fallback_schema_using_flags_and_name_markers(self):
        path = _write_pos_csv(
            [
                {
                    "PRVDR_NUM": "333333",
                    "FAC_NAME": "Capital Ambulatory Surgery Center",
                    "CITY_NAME": "HOUSTON",
                    "STATE_CD": "TX",
                    "ZIP_CD": "77001",
                    "GNRL_CNTL_TYPE_CD": "05",
                    "GNRL_FAC_TYPE_CD": "",
                    "FREESTNDNG_ASC_SW": "Y",
                    "CRTFCTN_DT": "20220101",
                    "ORGNL_PRTCPTN_DT": "20220101",
                },
                {
                    "PRVDR_NUM": "444444",
                    "FAC_NAME": "River City Imaging",
                    "CITY_NAME": "HOUSTON",
                    "STATE_CD": "TX",
                    "ZIP_CD": "77002",
                    "GNRL_CNTL_TYPE_CD": "05",
                    "GNRL_FAC_TYPE_CD": "",
                    "RDLGY_SRVC_CD": "Y",
                    "CRTFCTN_DT": "20220101",
                    "ORGNL_PRTCPTN_DT": "20220101",
                },
            ],
            extra_fields=["FREESTNDNG_ASC_SW", "RDLGY_SRVC_CD", "CRTFCTN_DT"],
        )
        counts = extract_asc_and_imaging_from_pos(path, strict_min_expected=0)
        assert counts["asc"] == 1
        assert counts["imaging_center"] == 1
        os.unlink(path)

    def test_raises_when_non_hospital_extraction_volume_is_suspiciously_low(self):
        path = _write_pos_csv(
            [
                {
                    "PRVDR_NUM": "555555",
                    "FAC_NAME": "Single Tiny Extract",
                    "CITY_NAME": "HOUSTON",
                    "STATE_CD": "TX",
                    "ZIP_CD": "77001",
                    "GNRL_CNTL_TYPE_CD": "05",
                    "GNRL_FAC_TYPE_CD": "17",
                    "CRTFCTN_DT": "20220101",
                    "ORGNL_PRTCPTN_DT": "20220101",
                },
            ],
            extra_fields=["CRTFCTN_DT"],
        )
        with pytest.raises(RuntimeError):
            extract_asc_and_imaging_from_pos(path, strict_min_expected=5)
        os.unlink(path)


# ---------------------------------------------------------------------------
# Hospital matching
# ---------------------------------------------------------------------------

class TestHospitalMatching:
    def test_match_by_ccn(self):
        _seed_hospital("450123", "Houston Medical Center", "TX", "Houston")
        path = _write_pos_csv([
            {
                "PRVDR_NUM": "450123",
                "FAC_NAME": "Houston Medical Center",
                "STATE_CD": "TX",
                "GNRL_CNTL_TYPE_CD": "02",
                "GNRL_FAC_TYPE_CD": "01",
            }
        ])
        load_pos_file(path)
        matched = match_pos_to_hospitals()
        assert "450123" in matched
        assert matched["450123"] == "450123"
        os.unlink(path)

    def test_no_match_logs_unmatched(self):
        _seed_hospital("999999", "Orphaned Hospital", "CA", "Sacramento")
        path = _write_pos_csv([
            {
                "PRVDR_NUM": "111111",
                "FAC_NAME": "Completely Different Name",
                "STATE_CD": "TX",
                "GNRL_CNTL_TYPE_CD": "02",
                "GNRL_FAC_TYPE_CD": "01",
            }
        ])
        load_pos_file(path)
        match_pos_to_hospitals()
        with get_db() as db:
            row = db.execute("SELECT * FROM enrichment_unmatched WHERE facility_id = '999999'").fetchone()
        assert row is not None
        os.unlink(path)


# ---------------------------------------------------------------------------
# Ownership update
# ---------------------------------------------------------------------------

class TestOwnershipUpdate:
    def test_ownership_mapped_correctly(self):
        _seed_hospital("450100", "Test Nonprofit", "TX", "Dallas")
        path = _write_pos_csv([
            {
                "PRVDR_NUM": "450100",
                "FAC_NAME": "Test Nonprofit",
                "STATE_CD": "TX",
                "GNRL_CNTL_TYPE_CD": "02",
                "GNRL_FAC_TYPE_CD": "01",
            }
        ])
        load_pos_file(path)
        matched = {"450100": "450100"}
        update_ownership_from_pos(matched)
        with get_db() as db:
            row = db.execute("SELECT ownership_type, ownership_subtype, ownership_code FROM hospitals WHERE facility_id = '450100'").fetchone()
        assert row["ownership_type"] == "Nonprofit"
        assert row["ownership_subtype"] == "Nonprofit (Private)"
        assert row["ownership_code"] == "02"
        os.unlink(path)

    def test_government_ownership_mapped(self):
        _seed_hospital("450200", "County Hospital", "TX", "El Paso")
        path = _write_pos_csv([
            {
                "PRVDR_NUM": "450200",
                "FAC_NAME": "County Hospital",
                "STATE_CD": "TX",
                "GNRL_CNTL_TYPE_CD": "10",
                "GNRL_FAC_TYPE_CD": "01",
            }
        ])
        load_pos_file(path)
        update_ownership_from_pos({"450200": "450200"})
        with get_db() as db:
            row = db.execute("SELECT ownership_type FROM hospitals WHERE facility_id = '450200'").fetchone()
        assert row["ownership_type"] == "Government (Public)"
        os.unlink(path)


# ---------------------------------------------------------------------------
# Coordinates update
# ---------------------------------------------------------------------------

class TestCoordinatesUpdate:
    def test_coordinates_updated(self):
        _seed_hospital("450300", "Geo Hospital", "TX", "San Antonio")
        path = _write_pos_csv([
            {
                "PRVDR_NUM": "450300",
                "FAC_NAME": "Geo Hospital",
                "STATE_CD": "TX",
                "LATITUDE": "29.4241",
                "LONGITUDE": "-98.4936",
                "GNRL_CNTL_TYPE_CD": "02",
                "GNRL_FAC_TYPE_CD": "01",
            }
        ])
        load_pos_file(path)
        updated, flagged = update_coordinates_from_pos({"450300": "450300"})
        assert updated == 1
        assert flagged == 0
        with get_db() as db:
            row = db.execute("SELECT lat, lon FROM hospitals WHERE facility_id = '450300'").fetchone()
        assert row["lat"] == pytest.approx(29.4241)
        assert row["lon"] == pytest.approx(-98.4936)
        os.unlink(path)

    def test_invalid_coords_flagged(self):
        _seed_hospital("450400", "Overseas Hospital", "TX", "Houston")
        path = _write_pos_csv([
            {
                "PRVDR_NUM": "450400",
                "FAC_NAME": "Overseas Hospital",
                "STATE_CD": "TX",
                "LATITUDE": "51.5",
                "LONGITUDE": "0.1",  # London — not in US
                "GNRL_CNTL_TYPE_CD": "02",
                "GNRL_FAC_TYPE_CD": "01",
            }
        ])
        load_pos_file(path)
        updated, flagged = update_coordinates_from_pos({"450400": "450400"})
        assert flagged == 1
        with get_db() as db:
            row = db.execute("SELECT issue FROM coordinates_validation WHERE facility_id = '450400'").fetchone()
        assert row is not None
        assert row["issue"] == "out_of_us_bounds"
        os.unlink(path)


# ---------------------------------------------------------------------------
# Bed count update
# ---------------------------------------------------------------------------

class TestBedsUpdate:
    def test_beds_and_size_set(self):
        _seed_hospital("450500", "Big Hospital", "TX", "Lubbock")
        path = _write_pos_csv([
            {
                "PRVDR_NUM": "450500",
                "FAC_NAME": "Big Hospital",
                "STATE_CD": "TX",
                "CRTFD_BED_CNT": "550",
                "GNRL_CNTL_TYPE_CD": "05",
                "GNRL_FAC_TYPE_CD": "01",
            }
        ])
        load_pos_file(path)
        update_beds_from_pos({"450500": "450500"})
        with get_db() as db:
            row = db.execute("SELECT bed_count, hospital_size FROM hospitals WHERE facility_id = '450500'").fetchone()
        assert row["bed_count"] == 550
        assert row["hospital_size"] == "Large Academic / Tertiary"
        os.unlink(path)


# ---------------------------------------------------------------------------
# Compliance status
# ---------------------------------------------------------------------------

class TestComplianceStatus:
    def _seed_transparency(self, facility_id: str, parse_status: str, procs: int, has_codes: int = 1) -> None:
        _seed_hospital(facility_id, f"Hospital {facility_id}", "TX", "Austin")
        with get_db() as db:
            db.execute(
                """
                INSERT OR REPLACE INTO transparency_files
                    (facility_id, parse_status, procedures_extracted, has_standard_codes)
                VALUES (?, ?, ?, ?)
                """,
                (facility_id, parse_status, procs, has_codes),
            )

    def test_compliant_with_50_procs_and_codes(self):
        self._seed_transparency("450600", "success", 75, 1)
        update_compliance_status()
        with get_db() as db:
            row = db.execute("SELECT compliance_status FROM hospitals WHERE facility_id = '450600'").fetchone()
        assert row["compliance_status"] == "Compliant"

    def test_partial_with_few_procs(self):
        self._seed_transparency("450601", "success", 20, 0)
        update_compliance_status()
        with get_db() as db:
            row = db.execute("SELECT compliance_status FROM hospitals WHERE facility_id = '450601'").fetchone()
        assert row["compliance_status"] == "Partial"

    def test_non_compliant_on_parse_error(self):
        self._seed_transparency("450602", "error", 0)
        update_compliance_status()
        with get_db() as db:
            row = db.execute("SELECT compliance_status FROM hospitals WHERE facility_id = '450602'").fetchone()
        assert row["compliance_status"] == "Non-compliant"

    def test_unverified_when_no_file(self):
        _seed_hospital("450603", "Mystery Hospital", "TX", "Waco")
        update_compliance_status()
        with get_db() as db:
            row = db.execute("SELECT compliance_status FROM hospitals WHERE facility_id = '450603'").fetchone()
        assert row["compliance_status"] == "Unverified"


# ---------------------------------------------------------------------------
# Coverage report
# ---------------------------------------------------------------------------

class TestCoverageReport:
    def test_coverage_report_returns_totals(self):
        _seed_hospital("990001", "Report Hospital", "CA", "Los Angeles")
        report = coverage_report()
        assert "total_hospitals" in report
        assert report["total_hospitals"] >= 1


# ---------------------------------------------------------------------------
# hospital_seo.py — N/A page prose generation
# ---------------------------------------------------------------------------

class TestUngradedIntroParagraph:
    def _hospital(self, **kwargs) -> dict:
        base = {
            "name": "Mercy General Hospital",
            "city": "Springfield",
            "state": "Illinois",
            "billing_grade": "N/A",
            "avg_markup_vs_medicare": None,
            "procedures_compared": 0,
            "is_nonprofit": 1,
            "ownership_type": "Nonprofit",
            "bed_count": 200,
            "cms_star_rating": None,
            "is_pe_owned": 0,
            "pe_firm": None,
            "pe_acquisition_year": None,
            "compliance_status": "Unverified",
        }
        base.update(kwargs)
        return base

    def test_returns_string_for_na_grade(self):
        result = generate_intro_paragraph(self._hospital())
        assert isinstance(result, str)
        assert len(result) > 50

    def test_mentions_hospital_name(self):
        result = _generate_ungraded_intro(self._hospital())
        assert "Mercy General Hospital" in result

    def test_mentions_location(self):
        result = _generate_ungraded_intro(self._hospital())
        assert "Springfield" in result
        assert "Illinois" in result

    def test_mentions_bed_count(self):
        result = _generate_ungraded_intro(self._hospital())
        assert "200" in result

    def test_mentions_cms_stars_when_available(self):
        result = _generate_ungraded_intro(self._hospital(cms_star_rating=4))
        assert "4 out of 5 stars" in result

    def test_mentions_nonprofit_policy(self):
        result = _generate_ungraded_intro(self._hospital())
        assert "501(r)" in result

    def test_mentions_non_compliant(self):
        result = _generate_ungraded_intro(self._hospital(compliance_status="Non-compliant"))
        assert "machine-readable" in result.lower()

    def test_pe_mention(self):
        result = _generate_ungraded_intro(self._hospital(is_pe_owned=1, pe_firm="Apollo Global", pe_acquisition_year=2021))
        assert "Apollo Global" in result
        assert "2021" in result

    def test_no_unknown_in_output(self):
        result = _generate_ungraded_intro(self._hospital(ownership_type="Unknown"))
        assert "Unknown" not in result


class TestNaDisputeTips:
    def _hospital(self, **kwargs) -> dict:
        base = {
            "name": "Hillside Hospital",
            "billing_grade": "N/A",
            "avg_markup_vs_medicare": None,
            "is_nonprofit": 1,
            "procedures_compared": 0,
            "phone": "(512) 555-0100",
            "cash_discount_avg_pct": None,
        }
        base.update(kwargs)
        return base

    def test_na_tips_no_unknown_markup(self):
        tips = generate_deterministic_tips(self._hospital(), {})
        assert "unknown" not in tips.lower()
        assert "N/A" not in tips

    def test_na_tips_mentions_medicare(self):
        tips = generate_deterministic_tips(self._hospital(), {})
        assert "Medicare" in tips

    def test_na_tips_mentions_phone(self):
        tips = generate_deterministic_tips(self._hospital(), {})
        assert "(512) 555-0100" in tips

    def test_graded_tips_unchanged(self):
        hospital = {
            "name": "Test Hospital",
            "billing_grade": "B",
            "avg_markup_vs_medicare": 2.5,
            "is_nonprofit": 0,
            "procedures_compared": 50,
            "phone": None,
            "cash_discount_avg_pct": None,
        }
        tips = generate_deterministic_tips(hospital, {})
        assert "2.5x" in tips
        assert "grade of B" in tips
