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
from main import app  # noqa: E402
from analyzer import analyze_bill, save_bill_and_findings  # noqa: E402
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

    def test_stats_after_bill(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        save_bill_and_findings(None, SAMPLE_BILL, analysis)
        resp = client.get("/api/stats")
        assert resp.status_code == 200
        assert resp.json()["data"]["bills_scanned"] >= 1


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
