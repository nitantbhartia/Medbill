"""Smoke tests for ASC and imaging directory routes."""

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
from main import app  # noqa: E402

_db.init_db()
client = TestClient(app)


def _seed_facilities():
    with get_db() as db:
        db.execute(
            """
            INSERT OR REPLACE INTO facilities (
                facility_id, name, city, state, state_slug, city_slug, zip, facility_type, slug, is_hospital_owned
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("asc-t1", "Metro Surgery", "Austin", "TX", "tx", "austin", "78701", "asc", "metro-surgery-austin-surgery-center", 0),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO facilities (
                facility_id, name, city, state, state_slug, city_slug, zip, facility_type, slug, is_hospital_owned
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("img-t1", "Metro Imaging", "Austin", "TX", "tx", "austin", "78701", "imaging_center", "metro-imaging-austin-imaging-center", 1),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO facility_billing_metrics (
                facility_id, facility_type, avg_markup, billing_grade, procedures_compared, benchmark_type
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            ("asc-t1", "asc", 2.2, "B", 5, "asc"),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO facility_billing_metrics (
                facility_id, facility_type, avg_markup, billing_grade, procedures_compared, benchmark_type
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            ("img-t1", "imaging_center", 3.5, "C", 6, "opps"),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO procedure_prices (
                facility_id, cpt_code, description, gross_charge, medicare_benchmark_rate,
                markup_vs_medicare, data_year, facility_type, medicare_benchmark_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("asc-t1", "45378", "COLONOSCOPY", 900.0, 180.0, 5.0, 2026, "asc", "asc"),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO procedure_prices (
                facility_id, cpt_code, description, gross_charge, medicare_benchmark_rate,
                markup_vs_medicare, data_year, facility_type, medicare_benchmark_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("img-t1", "70553", "MRI BRAIN", 1100.0, 320.0, 3.4, 2026, "imaging_center", "opps"),
        )


def test_surgery_center_routes_render():
    _seed_facilities()
    assert client.get("/surgery-centers/").status_code == 200
    assert client.get("/surgery-centers/tx/").status_code == 200
    assert client.get("/surgery-centers/tx/austin/").status_code == 200
    detail = client.get("/surgery-centers/tx/austin/metro-surgery-austin-surgery-center/")
    assert detail.status_code == 200
    assert "Metro Surgery" in detail.text


def test_imaging_routes_render():
    _seed_facilities()
    assert client.get("/imaging/").status_code == 200
    assert client.get("/imaging/tx/").status_code == 200
    assert client.get("/imaging/tx/austin/").status_code == 200
    detail = client.get("/imaging/tx/austin/metro-imaging-austin-imaging-center/")
    assert detail.status_code == 200
    assert "Metro Imaging" in detail.text
