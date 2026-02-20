"""Integration + regression tests for critical user-facing flows.

These tests lock down:
1) Landing-page UX contract elements.
2) End-to-end scan endpoint orchestration (extract -> scrub -> analyze -> persist).
"""

import os
import sys
from unittest.mock import MagicMock

# Mock google.genai before importing app modules that import scanner.
sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import api as api_module  # noqa: E402
from analyzer import analyze_bill, save_bill_and_findings  # noqa: E402
import db as _db  # noqa: E402
from db import get_db  # noqa: E402
from hospital_seo import upsert_hospital_row  # noqa: E402
from main import app  # noqa: E402
from tests.conftest import SAMPLE_BILL  # noqa: E402


client = TestClient(app)


class TestLandingPageRegression:
    def test_landing_has_core_ux_contract(self):
        resp = client.get("/")
        assert resp.status_code == 200
        html = resp.text

        # Core value prop + key interaction controls should stay stable.
        assert "Compare prices across hospitals, surgery centers, and imaging centers" in html
        assert 'id="heroSearchForm"' in html
        assert 'id="heroSearch"' in html
        assert 'id="facilityCardsGrid"' in html
        assert 'id="procedureCardsGrid"' in html


class TestPageFlowRegression:
    def test_confirm_page_missing_bill_shows_error(self):
        resp = client.get("/confirm/999999")
        assert resp.status_code == 200
        assert "Bill not found" in resp.text

    def test_confirm_page_renders_extracted_items_for_existing_bill(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis, "33021")

        resp = client.get(f"/confirm/{bill_id}")
        assert resp.status_code == 200
        html = resp.text
        assert "Confirm extracted items" in html
        assert f'value="{bill_id}"' in html
        assert "Analyze" in html


class TestScanEndpointIntegration:
    def test_scan_single_file_happy_path(self, monkeypatch):
        extracted_payload = {"provider_name": "Test Provider", "line_items": [{"cpt_code": "99283"}]}
        analysis_payload = {"total_findings": 1, "total_potential_savings": 123.0, "findings": []}

        calls = {"single": 0, "analyze": 0, "save": 0, "scrub": 0}

        def fake_single(image_bytes, mime_type):
            calls["single"] += 1
            assert image_bytes == b"fake-image"
            assert mime_type == "image/png"
            return extracted_payload

        def fake_scrub(extracted):
            calls["scrub"] += 1
            assert extracted == extracted_payload
            return extracted

        def fake_analyze(extracted, zip_code):
            calls["analyze"] += 1
            assert extracted == extracted_payload
            assert zip_code == "33021"
            return analysis_payload

        def fake_save(user_id, extracted, analysis, zip_code="00000"):
            calls["save"] += 1
            assert user_id is None
            assert extracted == extracted_payload
            assert analysis == analysis_payload
            assert zip_code == "33021"
            return 77

        monkeypatch.setattr(api_module.scanner, "process_bill_with_verification", fake_single)
        monkeypatch.setattr(api_module, "scrub_extracted_data", fake_scrub)
        monkeypatch.setattr(api_module.analyzer, "analyze_bill", fake_analyze)
        monkeypatch.setattr(api_module.analyzer, "save_bill_and_findings", fake_save)
        monkeypatch.setattr(api_module, "log_audit", lambda **kwargs: None)

        resp = client.post(
            "/api/scan",
            files=[("images", ("bill.png", b"fake-image", "image/png"))],
            data={"zip_code": "33021"},
        )

        assert resp.status_code == 200
        data = resp.json()["data"]
        assert data["bill_id"] == 77
        assert data["extracted"] == extracted_payload
        assert data["analysis"] == analysis_payload
        assert calls == {"single": 1, "analyze": 1, "save": 1, "scrub": 1}

    def test_scan_multi_file_uses_multi_page_extractor(self, monkeypatch):
        extracted_payload = {"provider_name": "Multi Provider", "line_items": [{"cpt_code": "71046"}]}
        analysis_payload = {"total_findings": 0, "total_potential_savings": 0.0, "findings": []}

        calls = {"multi": 0}

        def fake_multi(image_list):
            calls["multi"] += 1
            assert len(image_list) == 2
            assert image_list[0][0] == b"page-one"
            assert image_list[1][0] == b"page-two"
            return extracted_payload

        monkeypatch.setattr(api_module.scanner, "process_multi_page_bill", fake_multi)
        monkeypatch.setattr(api_module, "scrub_extracted_data", lambda extracted: extracted)
        monkeypatch.setattr(api_module.analyzer, "analyze_bill", lambda extracted, zip_code: analysis_payload)
        monkeypatch.setattr(api_module.analyzer, "save_bill_and_findings", lambda *args, **kwargs: 88)
        monkeypatch.setattr(api_module, "log_audit", lambda **kwargs: None)

        resp = client.post(
            "/api/scan",
            files=[
                ("images", ("page1.png", b"page-one", "image/png")),
                ("images", ("page2.png", b"page-two", "image/png")),
            ],
            data={"zip_code": "33021"},
        )

        assert resp.status_code == 200
        assert resp.json()["data"]["bill_id"] == 88
        assert calls["multi"] == 1

    def test_scan_with_optional_eob_upload_enriches_payload(self, monkeypatch):
        bill_payload = {"provider_name": "Bill Provider", "line_items": [{"cpt_code": "99283", "charged_amount": 1000.0}]}
        eob_payload = {
            "provider_name": "Bill Provider",
            "line_items": [{"cpt_code": "99283", "insurance_paid": 400.0, "insurance_adjustment": 500.0, "patient_responsibility": 100.0}],
        }
        seen = {"insurance_paid": None}

        def fake_extract(image_bytes, _mime):
            if image_bytes == b"fake-eob":
                return eob_payload
            return bill_payload

        monkeypatch.setattr(api_module.scanner, "process_bill_with_verification", fake_extract)
        monkeypatch.setattr(api_module, "scrub_extracted_data", lambda extracted: extracted)
        monkeypatch.setattr(api_module, "log_audit", lambda **kwargs: None)

        def fake_analyze(extracted, _zip_code):
            seen["insurance_paid"] = extracted["line_items"][0].get("insurance_paid")
            return {"total_findings": 0, "total_potential_savings": 0.0, "findings": []}

        monkeypatch.setattr(api_module.analyzer, "analyze_bill", fake_analyze)
        monkeypatch.setattr(api_module.analyzer, "save_bill_and_findings", lambda *args, **kwargs: 99)

        resp = client.post(
            "/api/scan",
            files=[
                ("images", ("bill.png", b"fake-image", "image/png")),
                ("eob_images", ("eob.png", b"fake-eob", "image/png")),
            ],
            data={"zip_code": "33021"},
        )
        assert resp.status_code == 200
        assert resp.json()["data"]["bill_id"] == 99
        assert seen["insurance_paid"] == 400.0

    def test_scan_returns_500_when_extraction_fails(self, monkeypatch):
        def boom(*_args, **_kwargs):
            raise RuntimeError("extractor crashed")

        monkeypatch.setattr(api_module.scanner, "process_bill_with_verification", boom)

        resp = client.post(
            "/api/scan",
            files=[("images", ("bill.png", b"fake-image", "image/png"))],
        )

        assert resp.status_code == 500
        assert "Failed to extract bill data" in resp.json()["detail"]

    def test_scan_returns_500_when_analysis_fails(self, monkeypatch):
        monkeypatch.setattr(
            api_module.scanner,
            "process_bill_with_verification",
            lambda *_args, **_kwargs: {"provider_name": "Any", "line_items": []},
        )
        monkeypatch.setattr(api_module, "scrub_extracted_data", lambda extracted: extracted)
        monkeypatch.setattr(
            api_module.analyzer,
            "analyze_bill",
            lambda *_args, **_kwargs: (_ for _ in ()).throw(RuntimeError("analysis crashed")),
        )

        resp = client.post(
            "/api/scan",
            files=[("images", ("bill.png", b"fake-image", "image/png"))],
            data={"zip_code": "33021"},
        )

        assert resp.status_code == 500
        assert "Failed to analyze bill" in resp.json()["detail"]

    def test_scan_to_results_and_dispute_artifacts_flow(self, monkeypatch):
        extracted_payload = {
            "provider_name": "Flow Provider",
            "provider_address": "123 Main St",
            "line_items": [{"cpt_code": "99283", "description": "ER visit", "charged_amount": 1200.0, "quantity": 1}],
            "total_charged": 1200.0,
            "total_patient_owes": 600.0,
        }
        analysis_payload = {
            "total_findings": 1,
            "total_potential_savings": 200.0,
            "findings": [
                {
                    "type": "price_markup",
                    "severity": "high",
                    "message": "Marked up vs Medicare",
                    "potential_savings": 200.0,
                    "confidence": "high",
                    "rule_id": "RULE_MARKUP_VS_MEDICARE",
                    "evidence": {"source": "cms_medicare_pfs_opps"},
                    "line_item": {"cpt_code": "99283"},
                }
            ],
        }

        monkeypatch.setattr(
            api_module.scanner,
            "process_bill_with_verification",
            lambda *_args, **_kwargs: extracted_payload,
        )
        monkeypatch.setattr(api_module, "scrub_extracted_data", lambda extracted: extracted)
        monkeypatch.setattr(api_module.analyzer, "analyze_bill", lambda *_args, **_kwargs: analysis_payload)
        monkeypatch.setattr(api_module, "log_audit", lambda **kwargs: None)

        scan = client.post(
            "/api/scan",
            files=[("images", ("bill.png", b"fake-image", "image/png"))],
            data={"zip_code": "33021"},
        )
        assert scan.status_code == 200
        bill_id = scan.json()["data"]["bill_id"]

        results = client.get(f"/api/results/{bill_id}")
        assert results.status_code == 200
        assert results.json()["data"]["bill"]["id"] == bill_id

        packet = client.get(f"/api/dispute-packet/{bill_id}")
        assert packet.status_code == 200
        assert "cover_letter" in packet.json()["data"]

        finding_id = results.json()["data"]["findings"][0]["id"]
        letter = client.post(
            f"/api/dispute-letter/{bill_id}",
            json={"finding_ids": [finding_id], "requestor_name": "Flow Tester"},
        )
        assert letter.status_code == 200
        assert "Flow Tester" in letter.json()["data"]["letter"]


class TestPricingConsistencyRegression:
    @staticmethod
    def _seed_consistency_fixture():
        _db._connection = None
        _db.init_db()
        upsert_hospital_row(
            {
                "facility_id": "99151",
                "name": "Consistency Hospital A",
                "city": "Springfield",
                "state": "IL",
                "slug": "consistency-hospital-a-springfield",
                "lat": 39.7817,
                "lon": -89.6501,
            }
        )
        upsert_hospital_row(
            {
                "facility_id": "99152",
                "name": "Consistency Hospital B",
                "city": "Springfield",
                "state": "IL",
                "slug": "consistency-hospital-b-springfield",
                "lat": 39.79,
                "lon": -89.64,
            }
        )
        with get_db() as db:
            db.execute(
                "INSERT OR REPLACE INTO billing_metrics (facility_id, avg_markup_vs_medicare, procedures_compared, billing_grade) VALUES (?, ?, ?, ?)",
                ("099151", 10.0, 20, "F"),
            )
            db.execute(
                "INSERT OR REPLACE INTO billing_metrics (facility_id, avg_markup_vs_medicare, procedures_compared, billing_grade) VALUES (?, ?, ?, ?)",
                ("099152", 15.0, 20, "F"),
            )
            db.execute(
                "INSERT OR REPLACE INTO hospital_prices (facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year, facility_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                ("099151", "70551", "MRI BRAIN STEM W/O DYE", 2000.0, 200.0, 10.0, 2026, "hospital"),
            )
            db.execute(
                "INSERT OR REPLACE INTO hospital_prices (facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year, facility_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                ("099152", "70551", "MRI BRAIN STEM W/O DYE", 3000.0, 200.0, 15.0, 2026, "hospital"),
            )

    @staticmethod
    def _extract_money_int(pattern: str, text: str) -> int:
        import re

        m = re.search(pattern, text, flags=re.S)
        assert m is not None
        return int(m.group(1).replace(",", ""))

    def test_homepage_and_mri_article_hospital_avg_match(self):
        self._seed_consistency_fixture()

        landing = client.get("/")
        assert landing.status_code == 200
        landing_price = self._extract_money_int(
            r'<div class="procedure-name">[^<]*MRI[^<]*</div>\s*<div class="procedure-price">\$([0-9,]+)</div>',
            landing.text,
        )

        mri = client.get("/procedures/mri-cost/")
        assert mri.status_code == 200
        mri_hosp_avg = self._extract_money_int(
            r'<div class="hero-stat-label">Hospital avg</div>\s*<div class="hero-stat-value">\$([0-9,]+)</div>',
            mri.text,
        )

        assert landing_price == 2500
        assert mri_hosp_avg == 2500
        assert landing_price == mri_hosp_avg

    def test_mri_detail_and_article_medicare_rate_match(self):
        self._seed_consistency_fixture()

        detail = client.get("/procedures/70551/")
        assert detail.status_code == 200
        detail_rate = self._extract_money_int(r"Medicare rate:\s*<strong>\$([0-9,]+)</strong>", detail.text)

        article = client.get("/procedures/mri-cost/")
        assert article.status_code == 200
        article_rate = self._extract_money_int(
            r'<div class="hero-stat-label">Medicare rate</div>\s*<div class="hero-stat-value">\$([0-9,]+)</div>',
            article.text,
        )

        assert detail_rate == 200
        assert article_rate == 200
        assert detail_rate == article_rate

    def test_hospital_profile_table_matches_seeded_price(self):
        self._seed_consistency_fixture()
        page = client.get("/hospitals/il/springfield/consistency-hospital-a-springfield/")
        assert page.status_code == 200
        assert "70551" in page.text
        assert "$2000.00" in page.text
