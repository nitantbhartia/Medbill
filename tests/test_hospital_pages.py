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

import config  # noqa: E402
from db import get_db  # noqa: E402
from hospital_seo import upsert_hospital_row  # noqa: E402
from main import app  # noqa: E402


client = TestClient(app)


def _seed_hospital():
    upsert_hospital_row(
        {
            "facility_id": "10001",
            "name": "Memorial Regional Hospital",
            "address": "3501 Johnson St",
            "city": "Hollywood",
            "state": "FL",
            "zip": "33021",
            "ownership": "Voluntary non-profit",
            "hospital_type": "Acute Care Hospitals",
            "cms_star_rating": 3,
            "slug": "memorial-regional-hospital-hollywood",
            "is_nonprofit": 1,
        }
    )
    with get_db() as db:
        db.execute(
            """
            INSERT INTO hcahps_scores (
                facility_id, recommend_yes, doctor_communication_top,
                nurse_communication_top, survey_period
            ) VALUES (?, ?, ?, ?, ?)
            """,
            ("010001", 72.0, 78.0, 74.0, "2025-Q4"),
        )
        db.execute(
            """
            INSERT INTO hospital_financials (
                facility_id, total_charges, total_revenue, cost_to_charge_ratio, charity_care_pct_revenue,
                nonprofit_status, has_financial_assistance, fa_application_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("010001", 1200000000.0, 400000000.0, 0.33, 2.1, 1, 1, "https://example.org/fap"),
        )
        db.execute(
            """
            INSERT INTO transparency_files (facility_id, file_url, parse_status, file_format)
            VALUES (?, ?, ?, ?)
            """,
            ("010001", "https://example.org/transparency.csv", "parsed", "csv"),
        )
        db.execute(
            """
            INSERT INTO hospital_prices (
                facility_id, cpt_code, description, gross_charge, cash_price,
                medicare_rate, markup_vs_medicare, data_year
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("010001", "99285", "ER visit level 5", 2800.0, 1600.0, 227.0, 12.33, 2026),
        )
        db.execute(
            """
            INSERT INTO billing_metrics (
                facility_id, avg_markup_vs_medicare, median_markup_vs_medicare,
                max_markup_vs_medicare, procedures_compared, cash_discount_avg_pct, billing_grade
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            ("010001", 12.33, 12.33, 12.33, 8, 42.9, "F"),
        )
        db.execute(
            """
            INSERT INTO benchmark_averages (
                scope, cpt_code, avg_gross_charge, avg_cash_price,
                avg_markup_vs_medicare, hospital_count
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            ("FL", "99285", 2400.0, 1400.0, 10.8, 12),
        )


class TestHospitalSeoPages:
    def test_hospital_index_redirect(self):
        _seed_hospital()
        resp = client.get("/hospital")
        assert resp.status_code == 200  # followed redirect
        assert "Hospital Billing Report Card Directory" in resp.text
        assert "/hospitals/fl/" in resp.text

    def test_state_page(self):
        _seed_hospital()
        resp = client.get("/hospitals/fl/")
        assert resp.status_code == 200
        assert "FL Hospital Billing Report Cards" in resp.text
        assert "Memorial Regional Hospital" in resp.text
        assert "/hospitals/fl/hollywood/memorial-regional-hospital-hollywood/" in resp.text

    def test_city_page(self):
        _seed_hospital()
        resp = client.get("/hospitals/fl/hollywood/")
        assert resp.status_code == 200
        assert "Hollywood, FL Hospital Billing Comparison" in resp.text
        assert "Memorial Regional Hospital" in resp.text

    def test_hospital_profile_page(self):
        _seed_hospital()
        resp = client.get("/hospitals/fl/hollywood/memorial-regional-hospital-hollywood/")
        assert resp.status_code == 200
        assert "Memorial Regional Hospital" in resp.text
        assert "Billing Profile" in resp.text
        assert "Common Procedure Prices" in resp.text
        assert "Scan My Bill" in resp.text
        expected = f'<link rel="canonical" href="{config.APP_URL.rstrip("/")}/hospitals/fl/hollywood/memorial-regional-hospital-hollywood/"'
        assert expected in resp.text

    def test_legacy_route_redirects_to_canonical(self):
        _seed_hospital()
        resp = client.get("/hospital/fl/memorial-regional-hospital-hollywood", follow_redirects=False)
        assert resp.status_code == 301
        assert resp.headers["location"] == "/hospitals/fl/hollywood/memorial-regional-hospital-hollywood/"

    def test_sitemap_contains_hospital_paths(self):
        _seed_hospital()
        resp = client.get("/sitemap-hospitals.xml")
        assert resp.status_code == 200
        assert resp.headers["content-type"].startswith("application/xml")
        assert "/hospitals/fl/" in resp.text
        assert "/hospitals/fl/hollywood/memorial-regional-hospital-hollywood/" in resp.text
