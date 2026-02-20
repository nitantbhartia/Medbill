"""Tests for procedure cost pages (/procedures/ index and detail)."""

import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import db as _db  # noqa: E402
from db import get_db  # noqa: E402
from hospital_seo import upsert_hospital_row  # noqa: E402
from main import app  # noqa: E402
from main import _search_procedures  # noqa: E402
from procedure_pages import (  # noqa: E402
    get_providers_near_zip_for_cpt,
    get_procedure_profile,
    get_top_cpt_codes,
    get_zip_latlon,
)

# Initialize schema explicitly before any requests
_db.init_db()
client = TestClient(app)

# normalize_facility_id zero-pads to 6 chars: "99001" -> "099001"
_FID_A = "099001"
_FID_B = "099002"


def _seed():
    upsert_hospital_row(
        {
            "facility_id": "99001",
            "name": "Test General Hospital",
            "address": "100 Main St",
            "city": "Springfield",
            "state": "IL",
            "zip": "62701",
            "ownership": "Voluntary non-profit - Private",
            "hospital_type": "Acute Care Hospitals",
            "bed_count": 200,
            "cms_star_rating": 4,
            "slug": "test-general-hospital-springfield",
            "is_nonprofit": 1,
            "lat": 39.7817,
            "lon": -89.6501,
        }
    )
    upsert_hospital_row(
        {
            "facility_id": "99002",
            "name": "Test Specialty Center",
            "address": "200 Oak Ave",
            "city": "Springfield",
            "state": "IL",
            "zip": "62702",
            "ownership": "Proprietary",
            "hospital_type": "Acute Care Hospitals",
            "bed_count": 80,
            "cms_star_rating": 3,
            "slug": "test-specialty-center-springfield",
            "is_nonprofit": 0,
            "lat": 39.7900,
            "lon": -89.6400,
        }
    )
    with get_db() as db:
        db.execute(
            """
            INSERT OR IGNORE INTO billing_metrics (
                facility_id, avg_markup_vs_medicare, billing_grade,
                procedures_compared, state_rank
            ) VALUES (?, ?, ?, ?, ?)
            """,
            (_FID_A, 2.5, "A", 15, 2),
        )
        db.execute(
            """
            INSERT OR IGNORE INTO billing_metrics (
                facility_id, avg_markup_vs_medicare, billing_grade,
                procedures_compared, state_rank
            ) VALUES (?, ?, ?, ?, ?)
            """,
            (_FID_B, 5.2, "D", 12, 45),
        )
        # Seed procedure pricing for knee replacement (CPT 27447)
        for fid, charge, markup in [(_FID_A, 4200.0, 2.1), (_FID_B, 9800.0, 4.9)]:
            db.execute(
                """
                INSERT OR IGNORE INTO hospital_prices
                    (facility_id, cpt_code, description, gross_charge,
                     medicare_rate, markup_vs_medicare, data_year)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (fid, "27447", "TOTAL KNEE REPLACEMENT", charge, 2000.0, markup, 2025),
            )
        db.execute(
            """
            INSERT OR REPLACE INTO facilities (
                facility_id, name, address, city, state, state_slug, city_slug, zip,
                facility_type, is_hospital_owned, slug, lat, lon, accepts_medicare
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "asc-100001",
                "Independent Surgery Partners",
                "300 Pine St",
                "Springfield",
                "IL",
                "il",
                "springfield",
                "62701",
                "asc",
                0,
                "independent-surgery-partners-springfield-surgery-center",
                39.7825,
                -89.6510,
                1,
            ),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO facility_billing_metrics (
                facility_id, facility_type, avg_markup, median_markup, max_markup,
                procedures_compared, billing_grade, benchmark_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("asc-100001", "asc", 2.0, 2.0, 2.0, 6, "A", "asc"),
        )
        db.execute(
            """
            INSERT OR IGNORE INTO procedure_prices (
                facility_id, cpt_code, description, gross_charge,
                medicare_rate, markup_vs_medicare, data_year,
                facility_type, medicare_benchmark_type, medicare_benchmark_rate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "asc-100001",
                "27447",
                "TOTAL KNEE REPLACEMENT",
                2400.0,
                1200.0,
                2.0,
                2025,
                "asc",
                "asc",
                1200.0,
            ),
        )
        # Seed imaging code (CPT 70553 — brain MRI)
        for fid, charge, markup in [(_FID_A, 3100.0, 1.8), (_FID_B, 7500.0, 4.4)]:
            db.execute(
                """
                INSERT OR IGNORE INTO hospital_prices
                    (facility_id, cpt_code, description, gross_charge,
                     medicare_rate, markup_vs_medicare, data_year)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (fid, "70553", "MRI BRAIN W CONTRAST", charge, 1720.0, markup, 2025),
            )
        db.execute(
            """
            INSERT OR REPLACE INTO facilities (
                facility_id, name, address, city, state, state_slug, city_slug, zip,
                facility_type, is_hospital_owned, slug, lat, lon, accepts_medicare
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "img-200001",
                "Springfield Advanced Imaging",
                "400 Lake St",
                "Springfield",
                "IL",
                "il",
                "springfield",
                "62701",
                "imaging_center",
                1,
                "springfield-advanced-imaging-springfield-imaging-center",
                39.7830,
                -89.6495,
                1,
            ),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO facility_billing_metrics (
                facility_id, facility_type, avg_markup, median_markup, max_markup,
                procedures_compared, billing_grade, benchmark_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("img-200001", "imaging_center", 3.2, 3.2, 3.2, 8, "C", "opps"),
        )
        db.execute(
            """
            INSERT OR IGNORE INTO procedure_prices (
                facility_id, cpt_code, description, gross_charge,
                medicare_rate, markup_vs_medicare, data_year,
                facility_type, medicare_benchmark_type, medicare_benchmark_rate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "img-200001",
                "70553",
                "MRI BRAIN W CONTRAST",
                900.0,
                300.0,
                3.0,
                2025,
                "imaging_center",
                "opps",
                300.0,
            ),
        )
        # Seed zip lat/lon for zip 62701
        try:
            db.execute(
                "INSERT OR IGNORE INTO zip_latlon (zip, lat, lon, state, city) VALUES (?, ?, ?, ?, ?)",
                ("62701", 39.7817, -89.6501, "IL", "Springfield"),
            )
        except Exception:
            pass


def test_procedure_index_page_renders():
    _seed()
    resp = client.get("/procedures/")
    assert resp.status_code == 200
    assert "Procedure Cost Directory" in resp.text


def test_procedure_index_shows_cpt_codes():
    _seed()
    resp = client.get("/procedures/")
    assert resp.status_code == 200
    # Should list our seeded CPT codes
    assert "27447" in resp.text or "Knee" in resp.text


def test_procedure_detail_knee_replacement():
    _seed()
    resp = client.get("/procedures/27447/")
    assert resp.status_code == 200
    assert "Total Knee Replacement" in resp.text or "27447" in resp.text
    assert "What It Costs" in resp.text


def test_procedure_detail_imaging():
    _seed()
    resp = client.get("/procedures/70553/")
    assert resp.status_code == 200
    assert "70553" in resp.text


def test_procedure_detail_not_found():
    _seed()
    resp = client.get("/procedures/99999/")
    assert resp.status_code == 200
    assert "not found" in resp.text.lower()


def test_procedure_detail_shows_grade_table():
    _seed()
    resp = client.get("/procedures/27447/")
    assert resp.status_code == 200
    assert "Cost by Billing Grade" in resp.text


def test_procedure_detail_shows_fair_price_explainer():
    _seed()
    resp = client.get("/procedures/27447/")
    assert resp.status_code == 200
    assert "Fair Price" in resp.text or "Medicare" in resp.text


def test_procedure_detail_shows_faq():
    _seed()
    resp = client.get("/procedures/27447/")
    assert resp.status_code == 200
    assert "Frequently Asked Questions" in resp.text


def test_procedure_detail_shows_hospital_finder():
    _seed()
    resp = client.get("/procedures/27447/")
    assert resp.status_code == 200
    assert "Find Providers Near You" in resp.text


def test_api_hospitals_by_zip_requires_zip():
    _seed()
    resp = client.get("/api/procedures/27447/hospitals")
    assert resp.status_code == 400


def test_api_hospitals_by_zip_returns_results():
    _seed()
    resp = client.get("/api/procedures/27447/hospitals?zip=62701")
    assert resp.status_code == 200
    data = resp.json()
    assert "hospitals" in data


def test_api_providers_by_zip_returns_mixed_facility_types():
    _seed()
    resp = client.get("/api/procedures/27447/providers?zip=62701")
    assert resp.status_code == 200
    data = resp.json()
    assert "providers" in data
    types = {r["facility_type"] for r in data["providers"]}
    assert "hospital" in types
    assert "asc" in types


def test_get_providers_asc_uses_asc_benchmark_type():
    _seed()
    rows = get_providers_near_zip_for_cpt("27447", "62701", limit=20, facility_type="asc")
    assert rows
    assert all(r["facility_type"] == "asc" for r in rows)
    assert all(r["medicare_benchmark_type"] == "asc" for r in rows)


def test_search_procedures_includes_hospital_prices_when_procedure_prices_missing():
    _seed()
    with get_db() as db:
        db.execute("DELETE FROM procedure_prices WHERE cpt_code = '70553'")
    rows = _search_procedures("mri", limit=10)
    assert rows
    assert any((r.get("cpt_code") == "70553") for r in rows)


def test_search_procedures_keyword_fallback_when_descriptions_missing():
    _seed()
    with get_db() as db:
        db.execute("DELETE FROM procedure_prices WHERE cpt_code = '70553'")
        db.execute("UPDATE hospital_prices SET description = NULL WHERE cpt_code = '70553'")
    rows = _search_procedures("mri", limit=10)
    assert rows
    assert any((r.get("cpt_code") == "70553") for r in rows)


def test_search_procedures_dedupes_hospital_and_procedure_rows():
    _seed()
    with get_db() as db:
        db.execute(
            """
            INSERT OR REPLACE INTO procedure_prices (
                facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year, facility_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (_FID_A, "70553", "MRI BRAIN W CONTRAST", 3100.0, 1720.0, 1.8, 2025, "hospital"),
        )
    rows = _search_procedures("70553", limit=5, exact_only=True)
    assert rows
    row = rows[0]
    # Deduped result should match single-source value, not an inflated double-count aggregate.
    assert round(float(row.get("hospital_avg") or 0.0), 2) == 5300.0


def test_get_providers_falls_back_when_zip_coords_missing():
    _seed()
    with get_db() as db:
        db.execute("DELETE FROM zip_latlon")
    rows = get_providers_near_zip_for_cpt("27447", "62701", limit=10, facility_type="all")
    assert rows
    assert all("name" in r and r["name"] for r in rows)


def test_get_providers_without_coords_prefers_zip_state_over_national_cheapest():
    _seed()
    with get_db() as db:
        db.execute("DELETE FROM zip_latlon")
        db.execute(
            "INSERT OR REPLACE INTO zip_locality_map (zip_prefix, locality, state, region) VALUES (?, ?, ?, ?)",
            ("627", "L0001", "IL", "Midwest"),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO facilities (
                facility_id, name, address, city, state, state_slug, city_slug, zip,
                facility_type, is_hospital_owned, slug, accepts_medicare
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "asc-fl-cheap",
                "Florida Discount Center",
                "1 Palm Dr",
                "Miami",
                "FL",
                "fl",
                "miami",
                "33101",
                "asc",
                0,
                "florida-discount-center-miami-surgery-center",
                1,
            ),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO facility_billing_metrics (
                facility_id, facility_type, avg_markup, median_markup, max_markup,
                procedures_compared, billing_grade, benchmark_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("asc-fl-cheap", "asc", 1.1, 1.1, 1.1, 10, "A", "asc"),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO procedure_prices (
                facility_id, cpt_code, description, gross_charge,
                medicare_rate, markup_vs_medicare, data_year,
                facility_type, medicare_benchmark_type, medicare_benchmark_rate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "asc-fl-cheap",
                "27447",
                "TOTAL KNEE REPLACEMENT",
                100.0,
                90.0,
                1.1,
                2025,
                "asc",
                "asc",
                90.0,
            ),
        )

    rows = get_providers_near_zip_for_cpt("27447", "62701", limit=10, facility_type="all")
    assert rows
    assert all((r.get("state") or "").upper() == "IL" for r in rows)


def test_get_providers_without_coords_returns_empty_when_zip_unresolvable():
    _seed()
    with get_db() as db:
        db.execute("DELETE FROM zip_latlon")
        db.execute("DELETE FROM zip_locality_map")
    rows = get_providers_near_zip_for_cpt("27447", "92111", limit=10, facility_type="all")
    assert rows == []


def test_get_top_cpt_codes_returns_list():
    _seed()
    codes = get_top_cpt_codes(10)
    assert isinstance(codes, list)
    # Each entry should have required keys
    for c in codes:
        assert "cpt_code" in c
        assert "name" in c
        assert "body_system" in c
        assert "hospital_count" in c


def test_get_procedure_profile_surgical():
    _seed()
    profile = get_procedure_profile("27447")
    assert profile is not None
    assert profile["cpt_code"] == "27447"
    assert profile["name"] == "Total Knee Replacement"
    assert profile["procedure_type"] == "surgical"
    assert profile["body_system"] == "Musculoskeletal"
    assert profile["header"]["hospital_count"] >= 1
    assert len(profile["faq"]) == 3
    assert "seo" in profile


def test_get_procedure_profile_imaging():
    _seed()
    profile = get_procedure_profile("70553")
    assert profile is not None
    assert profile["procedure_type"] == "imaging"


def test_get_procedure_profile_unknown_returns_none():
    _seed()
    profile = get_procedure_profile("00000")
    assert profile is None


def test_get_zip_latlon_found():
    _seed()
    result = get_zip_latlon("62701")
    assert result is not None
    lat, lon = result
    assert abs(lat - 39.7817) < 0.01
    assert abs(lon - (-89.6501)) < 0.01


def test_get_zip_latlon_unknown():
    _seed()
    result = get_zip_latlon("00000")
    assert result is None


def test_get_zip_latlon_invalid():
    assert get_zip_latlon("abc") is None
    assert get_zip_latlon("") is None


def test_procedure_detail_seo_title():
    _seed()
    profile = get_procedure_profile("27447")
    assert profile is not None
    title = profile["seo"]["page_title"]
    assert "BillKarma" in title
    assert len(title) <= 60


def test_procedure_detail_seo_description():
    _seed()
    profile = get_procedure_profile("27447")
    assert profile is not None
    desc = profile["seo"]["meta_description"]
    assert "27447" in desc
    assert len(desc) <= 155


def test_procedure_profile_trims_extreme_outliers_in_header_stats():
    _seed()
    with get_db() as db:
        # Add one extreme malformed charge and one normal peer for CPT 70551.
        upsert_hospital_row(
            {
                "facility_id": "99003",
                "name": "Outlier Test Hospital",
                "city": "Springfield",
                "state": "IL",
                "slug": "outlier-test-hospital-springfield",
                "lat": 39.78,
                "lon": -89.66,
            }
        )
        upsert_hospital_row(
            {
                "facility_id": "99004",
                "name": "Normal Test Hospital",
                "city": "Springfield",
                "state": "IL",
                "slug": "normal-test-hospital-springfield",
                "lat": 39.79,
                "lon": -89.64,
            }
        )
        db.execute(
            "INSERT OR REPLACE INTO billing_metrics (facility_id, avg_markup_vs_medicare, procedures_compared, billing_grade) VALUES (?, ?, ?, ?)",
            ("099003", 5000.0, 8, "F"),
        )
        db.execute(
            "INSERT OR REPLACE INTO billing_metrics (facility_id, avg_markup_vs_medicare, procedures_compared, billing_grade) VALUES (?, ?, ?, ?)",
            ("099004", 4.0, 8, "C"),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO hospital_prices (
                facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            ("099003", "70551", "MRI BRAIN STEM W/O DYE", 7055101.0, 195.0, 36180.0, 2026),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO hospital_prices (
                facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            ("099004", "70551", "MRI BRAIN STEM W/O DYE", 3800.0, 195.0, 19.5, 2026),
        )

    profile = get_procedure_profile("70551")
    assert profile is not None
    assert profile["header"]["excluded_outliers"] >= 1
    assert profile["header"]["national_avg_charge"] < 10000
    assert profile["range_bar"]["max_charge"] < 100000


def test_procedure_profile_keeps_mri_acronym_in_name():
    _seed()
    with get_db() as db:
        db.execute(
            """
            INSERT OR REPLACE INTO hospital_prices (
                facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            ("099001", "70551", "MRI BRAIN STEM W/O DYE", 3000.0, 195.0, 15.3, 2026),
        )
    profile = get_procedure_profile("70551")
    assert profile is not None
    assert "MRI" in profile["name"]
    assert "Mri" not in profile["name"]


def test_get_procedure_profile_uses_medicare_rate_fallback_when_markup_missing():
    _db._connection = None
    _db.init_db()
    upsert_hospital_row(
        {
            "facility_id": "99101",
            "name": "Fallback Benchmark Hospital",
            "address": "10 Test Way",
            "city": "Austin",
            "state": "TX",
            "zip": "73301",
            "slug": "fallback-benchmark-hospital-austin",
            "lat": 30.2672,
            "lon": -97.7431,
        }
    )
    with get_db() as db:
        db.execute(
            """
            INSERT INTO medicare_rates (cpt_code, locality, facility_rate, non_facility_rate, effective_year)
            VALUES (?, ?, ?, ?, ?)
            """,
            ("99284", "0000000", 250.0, 250.0, 2026),
        )
        db.execute(
            """
            INSERT INTO hospital_prices (
                facility_id, cpt_code, description, gross_charge,
                medicare_rate, markup_vs_medicare, data_year, facility_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("099101", "99284", "Level 4 ER Visit", 1250.0, None, None, 2026, "hospital"),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO billing_metrics (
                facility_id, avg_markup_vs_medicare, billing_grade, procedures_compared, state_rank
            ) VALUES (?, ?, ?, ?, ?)
            """,
            ("099101", 5.0, "D", 25, 1),
        )

    profile = get_procedure_profile("99284")
    assert profile is not None
    assert profile["header"]["medicare_rate"] is not None
    assert profile["header"]["avg_markup"] is not None


def test_get_procedure_profile_dedupes_hospital_and_procedure_price_duplicates():
    _db._connection = None
    _db.init_db()
    upsert_hospital_row(
        {
            "facility_id": "99201",
            "name": "Duplicate Source Hospital",
            "city": "Austin",
            "state": "TX",
            "slug": "duplicate-source-hospital-austin",
            "lat": 30.26,
            "lon": -97.74,
        }
    )
    with get_db() as db:
        db.execute(
            """
            INSERT INTO hospital_prices (
                facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year, facility_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("099201", "70551", "MRI BRAIN STEM W/O DYE", 2000.0, 200.0, 10.0, 2026, "hospital"),
        )
        db.execute(
            """
            INSERT INTO procedure_prices (
                facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year, facility_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("099201", "70551", "MRI BRAIN STEM W/O DYE", 2000.0, 200.0, 10.0, 2026, "hospital"),
        )

    profile = get_procedure_profile("70551")
    assert profile is not None
    assert profile["header"]["provider_count"] == 1
    assert profile["header"]["national_avg_charge"] == 2000.0
