"""Regression tests for hospital SEO landing pages and sitemap."""

import os
import sys
from unittest.mock import MagicMock

# Mock google.genai before app import chain.
sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

from db import get_db  # noqa: E402
from main import app  # noqa: E402


client = TestClient(app)


def _seed_hospital():
    with get_db() as db:
        db.execute(
            """
            INSERT INTO hospital_directory (
                facility_id, name, address, city, state, state_slug, zip,
                ownership, hospital_type, overall_rating, slug
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "10001",
                "Memorial Regional Hospital",
                "3501 Johnson St",
                "Hollywood",
                "FL",
                "fl",
                "33021",
                "Voluntary non-profit",
                "Acute Care Hospitals",
                3,
                "memorial-regional-hospital-hollywood",
            ),
        )
        db.execute(
            """
            INSERT INTO hospital_quality (
                facility_id, hcahps_summary, patient_experience_score,
                readmission_score, mortality_score
            ) VALUES (?, ?, ?, ?, ?)
            """,
            ("10001", "3", 72.0, 12.0, 8.0),
        )
        db.execute(
            """
            INSERT INTO hospital_financials (
                facility_id, total_charges, total_revenue, cost_to_charge_ratio,
                charity_care_pct, nonprofit_status, has_financial_assistance_policy,
                financial_assistance_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("10001", 1200000000.0, 400000000.0, 0.33, 2.1, 1, 1, "https://example.org/fap"),
        )
        db.execute(
            """
            INSERT INTO hospital_procedure_prices (
                facility_id, cpt_code, description, gross_charge,
                medicare_rate, state_avg_rate
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            ("10001", "99285", "ER visit level 5", 2800.0, 227.0, 2400.0),
        )


class TestHospitalSeoPages:
    def test_hospital_index_page(self):
        _seed_hospital()
        resp = client.get("/hospital")
        assert resp.status_code == 200
        assert "Hospital Billing Review Directory" in resp.text
        assert "/hospital/fl" in resp.text

    def test_state_page(self):
        _seed_hospital()
        resp = client.get("/hospital/fl")
        assert resp.status_code == 200
        assert "Florida".lower()[:2] or "FL"
        assert "Memorial Regional Hospital" in resp.text
        assert "/hospital/fl/memorial-regional-hospital-hollywood" in resp.text

    def test_hospital_profile_page(self):
        _seed_hospital()
        resp = client.get("/hospital/fl/memorial-regional-hospital-hollywood")
        assert resp.status_code == 200
        assert "Memorial Regional Hospital Billing Report Card" in resp.text
        assert "Avg Markup vs Medicare" in resp.text
        assert "Common Procedures and Prices" in resp.text
        assert "Scan your bill now" in resp.text

    def test_sitemap_contains_hospital_paths(self):
        _seed_hospital()
        resp = client.get("/hospitals/sitemap.xml")
        assert resp.status_code == 200
        assert resp.headers["content-type"].startswith("application/xml")
        assert "/hospital/fl" in resp.text
        assert "/hospital/fl/memorial-regional-hospital-hollywood" in resp.text
