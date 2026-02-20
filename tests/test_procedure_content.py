"""Tests for high-value procedure cost content pages."""

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
        db.execute(
            """
            INSERT OR REPLACE INTO hospital_prices (
                facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            ("022001", "70553", "MRI BRAIN W WO CONTRAST", 3000.0, 317.0, 9.5, 2026),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO hospital_prices (
                facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            ("022001", "45378", "COLONOSCOPY", 2400.0, 164.0, 14.6, 2026),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO facilities (
                facility_id, name, city, state, state_slug, city_slug, slug, facility_type, lat, lon
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("img-seed-1", "Independent MRI Center", "Dallas", "TX", "tx", "dallas", "independent-mri-center", "imaging_center", 32.777, -96.79),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO facilities (
                facility_id, name, city, state, state_slug, city_slug, slug, facility_type, lat, lon
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("asc-seed-1", "Independent ASC", "Dallas", "TX", "tx", "dallas", "independent-asc", "asc", 32.775, -96.80),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO procedure_prices (
                facility_id, cpt_code, description, gross_charge, medicare_benchmark_rate, markup_vs_medicare, data_year, facility_type, medicare_benchmark_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("img-seed-1", "70553", "MRI BRAIN W WO CONTRAST", 900.0, 317.0, 2.8, 2026, "imaging_center", "opps"),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO procedure_prices (
                facility_id, cpt_code, description, gross_charge, medicare_benchmark_rate, markup_vs_medicare, data_year, facility_type, medicare_benchmark_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("asc-seed-1", "45378", "COLONOSCOPY", 850.0, 164.0, 5.2, 2026, "asc", "asc"),
        )


def test_mri_cost_page_renders():
    _seed()
    resp = client.get("/procedures/mri-cost/")
    assert resp.status_code == 200
    assert "How Much Does an MRI Cost?" in resp.text
    assert "Imaging Centers" in resp.text


def test_colonoscopy_cost_page_renders():
    _seed()
    resp = client.get("/procedures/colonoscopy-cost/")
    assert resp.status_code == 200
    assert "How Much Does a Colonoscopy Cost?" in resp.text
    assert "Preventive vs diagnostic colonoscopy billing" in resp.text
