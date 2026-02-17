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
from main import app  # noqa: E402
from tests.conftest import SAMPLE_BILL  # noqa: E402


client = TestClient(app)


class TestLandingPageRegression:
    def test_landing_has_core_ux_contract(self):
        resp = client.get("/")
        assert resp.status_code == 200
        html = resp.text

        # Core value prop + key interaction controls should stay stable.
        assert "your health is personal. your debt shouldn't be." in html
        assert 'id="dropZone"' in html
        assert 'id="startAudit"' in html
        assert "PHI Redaction Enabled" in html
        assert "/api/scan" in html


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
