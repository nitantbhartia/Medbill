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
from hospital_seo import get_hospital_profile, upsert_hospital_row  # noqa: E402
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
            INSERT INTO medicare_rates (cpt_code, description, locality, facility_rate, non_facility_rate, effective_year)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(cpt_code, locality, effective_year) DO UPDATE SET description=excluded.description
            """,
            ("99285", "Emergency visit, high severity", "0000000", 227.0, 227.0, 2026),
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

    def test_profile_uses_description_fallback_and_cash_column_logic(self):
        _seed_hospital()
        with get_db() as db:
            db.execute(
                """
                INSERT INTO hospital_prices (
                    facility_id, cpt_code, description, gross_charge, cash_price,
                    medicare_rate, markup_vs_medicare, data_year
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(facility_id, cpt_code, data_year) DO UPDATE SET
                    description=excluded.description,
                    gross_charge=excluded.gross_charge,
                    cash_price=excluded.cash_price,
                    medicare_rate=excluded.medicare_rate,
                    markup_vs_medicare=excluded.markup_vs_medicare
                """,
                ("010001", "99284", None, 1400.0, 1400.0, 157.0, 8.92, 2026),
            )
            db.execute(
                """
                INSERT INTO medicare_rates (cpt_code, description, locality, facility_rate, non_facility_rate, effective_year)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(cpt_code, locality, effective_year) DO UPDATE SET description=excluded.description
                """,
                ("99284", "Emergency visit, moderate-high severity", "0000000", 157.0, 157.0, 2026),
            )

        profile = get_hospital_profile("fl", "hollywood", "memorial-regional-hospital-hollywood")
        assert profile is not None
        by_code = {row["cpt_code"]: row for row in profile["prices"]}
        assert by_code["99284"]["description"] == "Emergency visit, moderate-high severity"
        assert profile["show_cash_column"] is True

    def test_nearby_hospitals_excludes_empty_metrics_and_normalizes_name(self):
        _seed_hospital()
        upsert_hospital_row(
            {
                "facility_id": "10002",
                "name": "ASCENSION ALLEGAN HOSPITAL",
                "city": "Hollywood",
                "state": "FL",
                "slug": "ascension-allegan-hospital-hollywood",
            }
        )
        upsert_hospital_row(
            {
                "facility_id": "10003",
                "name": "No Data Medical Center",
                "city": "Hollywood",
                "state": "FL",
                "slug": "no-data-medical-center-hollywood",
            }
        )
        with get_db() as db:
            db.execute(
                """
                INSERT INTO billing_metrics (
                    facility_id, avg_markup_vs_medicare, median_markup_vs_medicare,
                    max_markup_vs_medicare, procedures_compared, cash_discount_avg_pct, billing_grade
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                ("010002", 3.4, 3.2, 4.0, 10, 20.0, "C"),
            )
            db.execute(
                "INSERT INTO billing_metrics (facility_id, procedures_compared, billing_grade) VALUES (?, ?, ?)",
                ("010003", 0, "N/A"),
            )

        profile = get_hospital_profile("fl", "hollywood", "memorial-regional-hospital-hollywood")
        assert profile is not None
        names = [row["name"] for row in profile["nearby"]]
        assert "Ascension Allegan Hospital" in names
        assert "No Data Medical Center" not in names
