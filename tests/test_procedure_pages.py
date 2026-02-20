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
from procedure_pages import (  # noqa: E402
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
    assert "Find Hospitals Near You" in resp.text


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
