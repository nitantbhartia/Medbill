"""Tests for the FastAPI API endpoints (no Gemini calls — tests analysis + persistence)."""

import sys
import json
import pytest
from unittest.mock import MagicMock

# Mock google.genai before importing main/scanner/negotiation
sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

import os  # noqa: E402
os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import db as _db  # noqa: E402
from api import _merge_eob_into_extracted  # noqa: E402
from main import app  # noqa: E402
from analyzer import analyze_bill, save_bill_and_findings, get_bill_results  # noqa: E402
from tests.conftest import SAMPLE_BILL  # noqa: E402


@pytest.fixture(autouse=True)
def setup_db():
    _db._connection = None
    _db.init_db()
    from seed_data import seed_if_empty
    seed_if_empty()
    yield
    if _db._connection:
        _db._connection.close()
        _db._connection = None


client = TestClient(app)


class TestStatsEndpoint:
    def test_stats_empty(self):
        resp = client.get("/api/stats")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert data["data"]["bills_scanned"] == 0


class TestEobMerge:
    def test_merge_eob_into_extracted_by_cpt(self):
        extracted = {
            "line_items": [
                {"cpt_code": "99283", "description": "ER visit", "charged_amount": 1000.0},
                {"cpt_code": "71046", "description": "Xray", "charged_amount": 200.0},
            ]
        }
        eob = {
            "line_items": [
                {"cpt_code": "71046", "insurance_paid": 100.0, "insurance_adjustment": 80.0, "patient_responsibility": 20.0},
                {"cpt_code": "99283", "insurance_paid": 400.0, "insurance_adjustment": 500.0, "patient_responsibility": 100.0},
            ]
        }
        merged = _merge_eob_into_extracted(extracted, eob)
        assert merged["line_items"][0]["insurance_paid"] == 400.0
        assert merged["line_items"][1]["insurance_paid"] == 100.0

    def test_stats_after_bill(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        save_bill_and_findings(None, SAMPLE_BILL, analysis)
        resp = client.get("/api/stats")
        assert resp.status_code == 200
        assert resp.json()["data"]["bills_scanned"] >= 1


class TestEffectivenessStatsEndpoint:
    def test_effectiveness_empty(self):
        resp = client.get("/api/stats/effectiveness")
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert data["overall"]["outcomes"] == 0
        assert data["overall"]["precision_proxy"] == 0.0

    def test_effectiveness_after_outcome(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)

        with _db.get_db() as db:
            cursor = db.execute(
                "INSERT INTO users (email, zip_code) VALUES (?, ?)",
                ("eff_test@test.com", "33021"),
            )
            user_id = cursor.lastrowid
            db.execute(
                "INSERT INTO dispute_outcomes (bill_id, user_id, hospital_name, called_billing, "
                "outcome, original_patient_owes, final_patient_owes, actual_savings) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (bill_id, user_id, "Test Hospital", 1, "reduced", 1000.0, 600.0, 400.0),
            )

        resp = client.get("/api/stats/effectiveness")
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert data["overall"]["outcomes"] >= 1
        assert data["overall"]["precision_proxy"] > 0


class TestResultsEndpoint:
    def test_get_results(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        resp = client.get(f"/api/results/{bill_id}")
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert data["bill"]["id"] == bill_id
        assert len(data["findings"]) > 0

    def test_get_results_404(self):
        resp = client.get("/api/results/99999")
        assert resp.status_code == 404


class TestDisputePacketEndpoint:
    def test_get_packet(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        resp = client.get(f"/api/dispute-packet/{bill_id}")
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert data["bill"]["id"] == bill_id
        assert "cover_letter" in data


class TestAppealPlaybookEndpoint:
    def test_get_playbook(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        resp = client.get(f"/api/appeal-playbook/{bill_id}")
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert data["bill_id"] == bill_id
        assert len(data["steps"]) > 0


class TestPhoneScriptEndpoint:
    def test_get_script(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        resp = client.get(f"/api/phone-script/{bill_id}")
        assert resp.status_code == 200
        assert len(resp.json()["data"]["script"]) > 0

    def test_get_script_404(self):
        resp = client.get("/api/phone-script/99999")
        assert resp.status_code == 404


class TestConfirmItemsEndpoint:
    def test_confirm_items(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)

        items = [
            {"cpt_code": "99283", "description": "ER visit", "charged_amount": 500,
             "quantity": 1, "date_of_service": "2026-01-10"},
        ]
        resp = client.post(
            "/api/confirm-items",
            data={"bill_id": bill_id, "confirmed_items": json.dumps(items)},
        )
        assert resp.status_code == 200
        assert resp.json()["data"]["items_confirmed"] == 1


class TestAnalyzeConfirmedEndpoint:
    def test_analyze_confirmed_persists_patient_responsibility(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)

        resp = client.post(
            f"/api/analyze/{bill_id}",
            json={
                "line_items": [
                    {
                        "cpt_code": "99285",
                        "description": "Emergency department visit, high severity",
                        "billed_amount": 4500.0,
                        "patient_responsibility": 321.45,
                        "quantity": 1,
                    }
                ]
            },
        )
        assert resp.status_code == 200

        results = get_bill_results(bill_id)
        assert results is not None
        assert len(results["line_items"]) == 1
        assert float(results["line_items"][0]["patient_responsibility"]) == 321.45


class TestDisputeOutcomeEndpoint:
    def test_record_outcome(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)

        with _db.get_db() as db:
            cursor = db.execute(
                "INSERT INTO users (email, zip_code) VALUES (?, ?)",
                ("api_test@test.com", "33021"),
            )
            user_id = cursor.lastrowid

        resp = client.post(
            "/api/dispute-outcome",
            data={
                "bill_id": bill_id,
                "user_id": user_id,
                "called_billing": True,
                "outcome": "reduced",
                "final_patient_owes": 2000.00,
                "notes": "They agreed to remove duplicate",
                "share_publicly": False,
            },
        )
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert data["actual_savings"] > 0

    def test_dispute_outcome_missing_bill_404(self):
        resp = client.post(
            "/api/dispute-outcome",
            data={
                "bill_id": 99999,
                "user_id": 1,
                "outcome": "reduced",
                "final_patient_owes": 100,
            },
        )
        assert resp.status_code == 404


class TestNegotiateStartEndpoint:
    def test_start_negotiation(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)

        with _db.get_db() as db:
            cursor = db.execute(
                "INSERT INTO users (email, zip_code) VALUES (?, ?)",
                ("neg_test@test.com", "33021"),
            )
            user_id = cursor.lastrowid

        resp = client.post(
            "/api/negotiate/start",
            data={
                "bill_id": bill_id,
                "user_id": user_id,
                "account_number": "ACC-TEST-123",
                "hospital_email": "billing@test.com",
            },
        )
        assert resp.status_code == 200
        assert resp.json()["data"]["negotiation_id"] > 0


class TestNegotiationCopilotEndpoint:
    def test_copilot_summary(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        with _db.get_db() as db:
            cursor = db.execute(
                "INSERT INTO users (email, zip_code) VALUES (?, ?)",
                ("copilot_test@test.com", "33021"),
            )
            user_id = cursor.lastrowid
        start = client.post(
            "/api/negotiate/start",
            data={
                "bill_id": bill_id,
                "user_id": user_id,
                "account_number": "ACC-CP-1",
                "hospital_email": "billing@test.com",
            },
        )
        negotiation_id = start.json()["data"]["negotiation_id"]
        resp = client.get(f"/api/negotiate/{negotiation_id}/copilot")
        assert resp.status_code == 200
        assert resp.json()["data"]["negotiation_id"] == negotiation_id


class TestComplianceEndpoints:
    def test_capture_consent(self):
        resp = client.post(
            "/api/consent",
            data={
                "consent_type": "tos",
                "consent_version": "v1",
            },
        )
        assert resp.status_code == 200
        assert resp.json()["data"]["consent_id"] > 0

    def test_export_and_delete_bill(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        export = client.get(f"/api/bills/{bill_id}/export")
        assert export.status_code == 200
        assert export.json()["data"]["bill"]["id"] == bill_id

        delete = client.delete(f"/api/bills/{bill_id}")
        assert delete.status_code == 200
        assert delete.json()["data"]["deleted"] is True

        after = client.get(f"/api/results/{bill_id}")
        assert after.status_code == 404


class TestOpsEndpoints:
    def test_ocr_benchmark_endpoint(self):
        resp = client.get("/api/ops/ocr-benchmark")
        assert resp.status_code == 200
        payload = resp.json()["data"]
        assert "aggregate" in payload
        assert "overall_score" in payload["aggregate"]


class TestDisputeLetterEndpoint:
    def test_dispute_letter_from_selected_findings(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        results = get_bill_results(bill_id)
        assert results is not None
        finding_ids = [results["findings"][0]["id"]]

        resp = client.post(
            f"/api/dispute-letter/{bill_id}",
            json={"finding_ids": finding_ids, "requestor_name": "Alex Patient"},
        )
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert data["bill_id"] == bill_id
        assert data["finding_count"] == 1
        assert "Alex Patient" in data["letter"]


class TestClaimWorkflowEndpoints:
    def test_create_and_progress_claim_status(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)

        created = client.post(
            "/api/claims",
            data={"bill_id": bill_id, "channel": "provider_billing", "note": "Start claim"},
        )
        assert created.status_code == 200
        claim_id = created.json()["data"]["claim_id"]

        listed = client.get(f"/api/claims/{bill_id}")
        assert listed.status_code == 200
        assert len(listed.json()["data"]["claims"]) >= 1

        progressed = client.post(
            f"/api/claims/{claim_id}/status",
            data={"status": "sent", "note": "Submitted by portal"},
        )
        assert progressed.status_code == 200
        assert progressed.json()["data"]["to_status"] == "sent"
