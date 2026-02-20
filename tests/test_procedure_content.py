"""Tests for high-value procedure cost content pages (Week 1)."""

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

_db.init_db()
client = TestClient(app)


def _seed():
    upsert_hospital_row(
        {
            "facility_id": "22001",
            "name": "Content Seed Hospital",
            "city": "Dallas",
            "state": "TX",
            "slug": "content-seed-hospital-dallas",
            "lat": 32.7767,
            "lon": -96.7970,
        }
    )
    with get_db() as db:
        db.execute(
            "INSERT OR REPLACE INTO billing_metrics (facility_id, avg_markup_vs_medicare, procedures_compared, billing_grade) VALUES (?, ?, ?, ?)",
            ("022001", 4.0, 10, "C"),
        )
        # Week 1: MRI (CPT 70551)
        db.execute(
            "INSERT OR REPLACE INTO hospital_prices (facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("022001", "70551", "MRI BRAIN W/O CONTRAST", 2800.0, 317.0, 8.8, 2026),
        )
        # Week 1: Colonoscopy (CPT 45378)
        db.execute(
            "INSERT OR REPLACE INTO hospital_prices (facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("022001", "45378", "COLONOSCOPY", 2400.0, 164.0, 14.6, 2026),
        )
        # Week 1: CT Scan (CPT 74177)
        db.execute(
            "INSERT OR REPLACE INTO hospital_prices (facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("022001", "74177", "CT ABDOMEN AND PELVIS W CONTRAST", 3200.0, 281.0, 11.4, 2026),
        )
        # Week 1: ER Visit (CPT 99284)
        db.execute(
            "INSERT OR REPLACE INTO hospital_prices (facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("022001", "99284", "EMERGENCY DEPT VISIT HIGH COMPLEXITY", 1850.0, 202.0, 9.2, 2026),
        )
        # Week 1: Knee Replacement (CPT 27447)
        db.execute(
            "INSERT OR REPLACE INTO hospital_prices (facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("022001", "27447", "TOTAL KNEE ARTHROPLASTY", 18500.0, 1159.0, 16.0, 2026),
        )

        # Imaging center for MRI and CT
        db.execute(
            "INSERT OR REPLACE INTO facilities (facility_id, name, city, state, state_slug, city_slug, slug, facility_type, lat, lon) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ("img-seed-1", "Independent MRI Center", "Dallas", "TX", "tx", "dallas", "independent-mri-center", "imaging_center", 32.777, -96.79),
        )
        db.execute(
            "INSERT OR REPLACE INTO procedure_prices (facility_id, cpt_code, description, gross_charge, medicare_benchmark_rate, markup_vs_medicare, data_year, facility_type, medicare_benchmark_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ("img-seed-1", "70551", "MRI BRAIN W/O CONTRAST", 780.0, 317.0, 2.5, 2026, "imaging_center", "opps"),
        )
        db.execute(
            "INSERT OR REPLACE INTO procedure_prices (facility_id, cpt_code, description, gross_charge, medicare_benchmark_rate, markup_vs_medicare, data_year, facility_type, medicare_benchmark_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ("img-seed-1", "74177", "CT ABDOMEN AND PELVIS W CONTRAST", 520.0, 281.0, 1.9, 2026, "imaging_center", "opps"),
        )

        # Surgery center for colonoscopy and knee replacement
        db.execute(
            "INSERT OR REPLACE INTO facilities (facility_id, name, city, state, state_slug, city_slug, slug, facility_type, lat, lon) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ("asc-seed-1", "Independent ASC", "Dallas", "TX", "tx", "dallas", "independent-asc", "asc", 32.775, -96.80),
        )
        db.execute(
            "INSERT OR REPLACE INTO procedure_prices (facility_id, cpt_code, description, gross_charge, medicare_benchmark_rate, markup_vs_medicare, data_year, facility_type, medicare_benchmark_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ("asc-seed-1", "45378", "COLONOSCOPY", 850.0, 164.0, 5.2, 2026, "asc", "asc"),
        )
        db.execute(
            "INSERT OR REPLACE INTO procedure_prices (facility_id, cpt_code, description, gross_charge, medicare_benchmark_rate, markup_vs_medicare, data_year, facility_type, medicare_benchmark_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ("asc-seed-1", "27447", "TOTAL KNEE ARTHROPLASTY", 5200.0, 1159.0, 4.5, 2026, "asc", "asc"),
        )


# ── Week 1 procedure pages ────────────────────────────────────────────

def test_mri_cost_page_renders():
    _seed()
    resp = client.get("/procedures/mri-cost/")
    assert resp.status_code == 200
    text = resp.text
    assert "MRI Cost: What You Should Pay in 2026" in text
    assert "Imaging Centers" in text
    assert "The Short Answer" in text
    assert "Find facilities near me" in text


def test_colonoscopy_cost_page_renders():
    _seed()
    resp = client.get("/procedures/colonoscopy-cost/")
    assert resp.status_code == 200
    text = resp.text
    assert "Colonoscopy Cost: What You Should Pay in 2026" in text
    assert "Preventive vs. diagnostic billing matters" in text
    assert "The Short Answer" in text


def test_ct_scan_cost_page_renders():
    _seed()
    resp = client.get("/procedures/ct-scan-cost/")
    assert resp.status_code == 200
    text = resp.text
    assert "CT Scan Cost: What You Should Pay in 2026" in text
    assert "The Short Answer" in text
    assert "Imaging Centers" in text


def test_er_visit_cost_page_renders():
    _seed()
    resp = client.get("/procedures/er-visit-cost/")
    assert resp.status_code == 200
    text = resp.text
    assert "ER Visit Cost: What Different Levels Cost in 2026" in text
    assert "ER billing has two separate charges" in text
    assert "The Short Answer" in text


def test_knee_replacement_cost_page_renders():
    _seed()
    resp = client.get("/procedures/knee-replacement-cost/")
    assert resp.status_code == 200
    text = resp.text
    assert "Knee Replacement Cost: Hospital vs. Surgery Center" in text
    assert "The Short Answer" in text
    assert "Surgery Centers" in text


# ── Template section tests ────────────────────────────────────────────

def test_what_to_ask_section_present():
    _seed()
    resp = client.get("/procedures/mri-cost/")
    assert resp.status_code == 200
    assert "Can this MRI be done at an independent imaging center" in resp.text


def test_what_to_ask_colonoscopy_specific():
    _seed()
    resp = client.get("/procedures/colonoscopy-cost/")
    assert resp.status_code == 200
    assert "preventive or diagnostic colonoscopy" in resp.text


def test_what_to_ask_er_specific():
    _seed()
    resp = client.get("/procedures/er-visit-cost/")
    assert resp.status_code == 200
    assert "What level of ER service is being billed" in resp.text


def test_what_to_ask_knee_specific():
    _seed()
    resp = client.get("/procedures/knee-replacement-cost/")
    assert resp.status_code == 200
    assert "ambulatory surgery center" in resp.text


def test_facility_finder_box_present():
    _seed()
    resp = client.get("/procedures/mri-cost/")
    assert resp.status_code == 200
    assert "finder-box" in resp.text or "Find facilities near me" in resp.text


def test_fair_price_box_present():
    _seed()
    resp = client.get("/procedures/mri-cost/")
    assert resp.status_code == 200
    assert "What is a fair price for" in resp.text
    assert "Fair market range" in resp.text


def test_cta_box_present():
    _seed()
    resp = client.get("/procedures/mri-cost/")
    assert resp.status_code == 200
    assert "Scan My Bill Free" in resp.text


def test_hero_stats_grid_present():
    _seed()
    resp = client.get("/procedures/mri-cost/")
    assert resp.status_code == 200
    assert "Hospital avg" in resp.text
    assert "Medicare rate" in resp.text


def test_unknown_slug_returns_error():
    resp = client.get("/procedures/nonexistent-cost/")
    assert resp.status_code in (200, 404)
    if resp.status_code == 200:
        assert "not found" in resp.text.lower()


def test_get_content_page_data_returns_what_to_ask():
    _seed()
    from procedure_content import get_content_page_data
    data = get_content_page_data("mri-cost")
    assert data is not None
    assert "what_to_ask" in data
    assert len(data["what_to_ask"]) > 0
    assert any("imaging center" in q.lower() for q in data["what_to_ask"])


def test_get_content_page_data_er_flags():
    _seed()
    from procedure_content import get_content_page_data
    data = get_content_page_data("er-visit-cost")
    assert data is not None
    assert data["is_er_content"] is True
    assert data["is_colonoscopy_content"] is False


def test_get_content_page_data_colonoscopy_flags():
    _seed()
    from procedure_content import get_content_page_data
    data = get_content_page_data("colonoscopy-cost")
    assert data is not None
    assert data["is_colonoscopy_content"] is True
    assert data["is_er_content"] is False


def test_all_week1_slugs_have_data():
    _seed()
    from procedure_content import get_content_page_data
    week1_slugs = ["mri-cost", "colonoscopy-cost", "ct-scan-cost", "er-visit-cost", "knee-replacement-cost"]
    for slug in week1_slugs:
        data = get_content_page_data(slug)
        assert data is not None, f"No data for slug: {slug}"
        assert data.get("content_heading"), f"No heading for slug: {slug}"
        assert data.get("what_to_ask"), f"No what_to_ask for slug: {slug}"
