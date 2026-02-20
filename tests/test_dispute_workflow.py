"""Tests for the Task 6 dispute workflow: letter builder, phone script, outcome stats, and API endpoints."""

import json
import sys
from unittest.mock import MagicMock

# Mock google.genai before any imports that may pull it in
sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

import os  # noqa: E402
os.environ["DB_PATH"] = ":memory:"

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

import db as _db  # noqa: E402
from main import app  # noqa: E402
from dispute_workflow import build_dispute_letter, build_phone_script, get_outcome_stats  # noqa: E402


client = TestClient(app)


@pytest.fixture(autouse=True)
def fresh_db():
    _db._connection = None
    _db.init_db()
    from seed_data import seed_if_empty
    seed_if_empty()
    yield
    if _db._connection:
        _db._connection.close()
        _db._connection = None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _insert_bill(provider_name="Test Hospital", bill_date="2026-01-10") -> int:
    with _db.get_db() as db:
        cur = db.execute(
            "INSERT INTO bills (provider_name, bill_date, total_charged) VALUES (?, ?, ?)",
            (provider_name, bill_date, 5000.0),
        )
        return cur.lastrowid


def _insert_finding(bill_id: int, finding_type: str, cpt_code: str, details: dict, savings: float = 500.0) -> int:
    # cpt_code is stored in details["line_item"]["cpt_code"] — findings table has no cpt_code column
    with _db.get_db() as db:
        cur = db.execute(
            "INSERT INTO findings (bill_id, finding_type, potential_savings, details) VALUES (?, ?, ?, ?)",
            (bill_id, finding_type, savings, json.dumps(details)),
        )
        return cur.lastrowid


def _pricing_details(cpt_code: str, description: str, charged: float, medicare: float) -> dict:
    return {
        "line_item": {"cpt_code": cpt_code, "description": description, "charged_amount": charged},
        "medicare_rate": medicare,
    }


# ---------------------------------------------------------------------------
# build_dispute_letter
# ---------------------------------------------------------------------------

class TestBuildDisputeLetter:
    def test_returns_none_for_nonexistent_bill(self):
        result = build_dispute_letter(bill_id=9999)
        assert result is None

    def test_returns_none_when_no_findings(self):
        bill_id = _insert_bill()
        result = build_dispute_letter(bill_id=bill_id)
        assert result is None

    def test_pricing_finding_produces_letter(self):
        bill_id = _insert_bill(provider_name="City Medical Center")
        _insert_finding(
            bill_id, "pricing", "74177",
            _pricing_details("74177", "CT abdomen with contrast", 2624.0, 320.0),
            savings=2304.0,
        )
        result = build_dispute_letter(bill_id=bill_id, requestor_name="Jane Doe", account_number="ACC-001")
        assert result is not None
        assert "Jane Doe" in result["letter"]
        assert "ACC-001" in result["letter"]
        assert "City Medical Center" in result["letter"]
        assert "EXCESSIVE CHARGE" in result["letter"]
        assert "74177" in result["letter"]
        assert result["finding_count"] == 1
        assert result["total_disputed"] == 2304.0

    def test_duplicate_finding_produces_correct_paragraph(self):
        bill_id = _insert_bill()
        details = {
            "line_item": {"cpt_code": "71046", "description": "Chest X-Ray", "charged_amount": 850.0},
            "duplicate_count": 2,
        }
        _insert_finding(bill_id, "duplicate", "71046", details, savings=850.0)
        result = build_dispute_letter(bill_id=bill_id)
        assert result is not None
        assert "DUPLICATE BILLING" in result["letter"]
        assert "2 time(s)" in result["letter"]

    def test_ncci_finding_produces_correct_paragraph(self):
        bill_id = _insert_bill()
        details = {
            "line_item": {"cpt_code": "80048", "description": "Basic metabolic panel", "charged_amount": 250.0},
            "bundled_code": "80053",
        }
        _insert_finding(bill_id, "ncci", "80048", details, savings=250.0)
        result = build_dispute_letter(bill_id=bill_id)
        assert result is not None
        assert "NCCI BUNDLING VIOLATION" in result["letter"]
        assert "80048" in result["letter"]

    def test_upcoding_finding_produces_correct_paragraph(self):
        bill_id = _insert_bill()
        details = {
            "line_item": {"cpt_code": "99285", "description": "ER visit level 5", "charged_amount": 4500.0},
            "expected_code": "99283",
        }
        _insert_finding(bill_id, "upcoding", "99285", details, savings=1400.0)
        result = build_dispute_letter(bill_id=bill_id)
        assert result is not None
        assert "UPCODING CONCERN" in result["letter"]
        assert "99285" in result["letter"]
        assert "99283" in result["letter"]

    def test_finding_ids_filter_works(self):
        bill_id = _insert_bill()
        id1 = _insert_finding(
            bill_id, "pricing", "71046",
            _pricing_details("71046", "Chest X-Ray", 850.0, 51.0),
            savings=799.0,
        )
        _insert_finding(
            bill_id, "pricing", "74177",
            _pricing_details("74177", "CT abdomen", 2624.0, 320.0),
            savings=2304.0,
        )
        result = build_dispute_letter(bill_id=bill_id, finding_ids=[id1])
        assert result is not None
        assert result["finding_count"] == 1
        assert result["total_disputed"] == 799.0

    def test_multiple_findings_sum_total_disputed(self):
        bill_id = _insert_bill()
        _insert_finding(
            bill_id, "pricing", "71046",
            _pricing_details("71046", "Chest X-Ray", 850.0, 51.0),
            savings=500.0,
        )
        _insert_finding(
            bill_id, "pricing", "74177",
            _pricing_details("74177", "CT abdomen", 2624.0, 320.0),
            savings=1000.0,
        )
        result = build_dispute_letter(bill_id=bill_id)
        assert result is not None
        assert result["finding_count"] == 2
        assert result["total_disputed"] == 1500.0

    def test_letter_contains_required_sections(self):
        bill_id = _insert_bill()
        _insert_finding(
            bill_id, "pricing", "99285",
            _pricing_details("99285", "ER visit", 4500.0, 512.0),
            savings=3000.0,
        )
        result = build_dispute_letter(bill_id=bill_id)
        letter = result["letter"]
        assert "DISPUTED CHARGES" in letter
        assert "REQUESTED ACTION" in letter
        assert "30 days" in letter


# ---------------------------------------------------------------------------
# build_phone_script
# ---------------------------------------------------------------------------

class TestBuildPhoneScript:
    def test_returns_none_for_nonexistent_bill(self):
        assert build_phone_script(bill_id=9999) is None

    def test_returns_none_when_no_findings(self):
        bill_id = _insert_bill()
        assert build_phone_script(bill_id=bill_id) is None

    def test_script_contains_required_sections(self):
        bill_id = _insert_bill(provider_name="River Medical")
        _insert_finding(
            bill_id, "pricing", "99285",
            _pricing_details("99285", "ER visit", 4500.0, 512.0),
        )
        script = build_phone_script(bill_id=bill_id)
        assert script is not None
        assert "BEFORE YOU CALL" in script
        assert "OPENING" in script
        assert "FOR EACH DISPUTED CHARGE" in script
        assert "IF THEY RESIST" in script
        assert "TAKE NOTES" in script

    def test_script_includes_provider_name(self):
        bill_id = _insert_bill(provider_name="River Medical")
        _insert_finding(
            bill_id, "pricing", "71046",
            _pricing_details("71046", "Chest X-Ray", 850.0, 51.0),
        )
        script = build_phone_script(bill_id=bill_id)
        assert "River Medical" in script

    def test_duplicate_finding_has_specific_language(self):
        bill_id = _insert_bill()
        details = {
            "line_item": {"cpt_code": "71046", "description": "Chest X-Ray", "charged_amount": 850.0},
            "duplicate_count": 2,
        }
        _insert_finding(bill_id, "duplicate", "71046", details)
        script = build_phone_script(bill_id=bill_id)
        assert "more than once" in script

    def test_ncci_finding_has_specific_language(self):
        bill_id = _insert_bill()
        details = {
            "line_item": {"cpt_code": "80048", "description": "Basic metabolic panel", "charged_amount": 250.0},
        }
        _insert_finding(bill_id, "ncci", "80048", details)
        script = build_phone_script(bill_id=bill_id)
        assert "NCCI" in script

    def test_upcoding_finding_has_specific_language(self):
        bill_id = _insert_bill()
        details = {
            "line_item": {"cpt_code": "99285", "description": "ER visit", "charged_amount": 4500.0},
        }
        _insert_finding(bill_id, "upcoding", "99285", details)
        script = build_phone_script(bill_id=bill_id)
        assert "clinical notes" in script


# ---------------------------------------------------------------------------
# get_outcome_stats
# ---------------------------------------------------------------------------

class TestGetOutcomeStats:
    def test_empty_db_returns_zeroes(self):
        stats = get_outcome_stats()
        assert stats["total_disputes"] == 0
        assert stats["recovery_count"] == 0
        assert stats["median_recovered"] is None
        assert stats["show_stat"] is False

    def test_below_threshold_show_stat_false(self):
        with _db.get_db() as db:
            for i in range(10):
                db.execute(
                    "INSERT INTO dispute_outcomes (outcome, actual_savings) VALUES (?, ?)",
                    ("reduced", float(100 + i * 10)),
                )
        stats = get_outcome_stats()
        assert stats["total_disputes"] == 10
        assert stats["show_stat"] is False

    def test_at_threshold_show_stat_true(self):
        with _db.get_db() as db:
            for i in range(50):
                db.execute(
                    "INSERT INTO dispute_outcomes (outcome, actual_savings) VALUES (?, ?)",
                    ("reduced", float(200 + i * 5)),
                )
        stats = get_outcome_stats()
        assert stats["total_disputes"] == 50
        assert stats["show_stat"] is True
        assert stats["median_recovered"] is not None

    def test_median_calculated_correctly(self):
        with _db.get_db() as db:
            for amount in [100.0, 200.0, 300.0]:
                db.execute(
                    "INSERT INTO dispute_outcomes (outcome, actual_savings) VALUES (?, ?)",
                    ("reduced", amount),
                )
        stats = get_outcome_stats()
        assert stats["median_recovered"] == 200.0

    def test_only_reduced_and_forgiven_count_for_savings(self):
        with _db.get_db() as db:
            db.execute(
                "INSERT INTO dispute_outcomes (outcome, actual_savings) VALUES (?, ?)",
                ("denied", 500.0),
            )
            db.execute(
                "INSERT INTO dispute_outcomes (outcome, actual_savings) VALUES (?, ?)",
                ("reduced", 300.0),
            )
        stats = get_outcome_stats()
        assert stats["total_disputes"] == 2
        assert stats["recovery_count"] == 1
        assert stats["median_recovered"] == 300.0


# ---------------------------------------------------------------------------
# API: /api/dispute-letter/{bill_id}
# ---------------------------------------------------------------------------

class TestDisputeLetterAPI:
    def test_nonexistent_bill_returns_404(self):
        resp = client.post("/api/dispute-letter/9999", json={})
        assert resp.status_code == 404

    def test_bill_with_no_findings_returns_404(self):
        bill_id = _insert_bill()
        resp = client.post(f"/api/dispute-letter/{bill_id}", json={})
        assert resp.status_code == 404

    def test_returns_letter_for_valid_bill(self):
        bill_id = _insert_bill(provider_name="Downtown Hospital")
        _insert_finding(
            bill_id, "pricing", "99285",
            _pricing_details("99285", "ER visit", 4500.0, 512.0),
            savings=3000.0,
        )
        resp = client.post(f"/api/dispute-letter/{bill_id}", json={})
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert "letter" in data["data"]
        assert "EXCESSIVE CHARGE" in data["data"]["letter"]
        assert data["data"]["finding_count"] == 1

    def test_account_number_param_used_in_letter(self):
        bill_id = _insert_bill()
        _insert_finding(
            bill_id, "pricing", "71046",
            _pricing_details("71046", "Chest X-Ray", 850.0, 51.0),
        )
        resp = client.post(f"/api/dispute-letter/{bill_id}", json={"account_number": "TEST-999"})
        assert resp.status_code == 200
        assert "TEST-999" in resp.json()["data"]["letter"]


# ---------------------------------------------------------------------------
# API: /api/dispute-phone-script/{bill_id}
# ---------------------------------------------------------------------------

class TestDisputePhoneScriptAPI:
    def test_nonexistent_bill_returns_404(self):
        resp = client.get("/api/dispute-phone-script/9999")
        assert resp.status_code == 404

    def test_returns_script_for_valid_bill(self):
        bill_id = _insert_bill(provider_name="Mercy Hospital")
        _insert_finding(
            bill_id, "pricing", "74177",
            _pricing_details("74177", "CT abdomen", 2624.0, 320.0),
        )
        resp = client.get(f"/api/dispute-phone-script/{bill_id}")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert "script" in data["data"]
        assert "BEFORE YOU CALL" in data["data"]["script"]


# ---------------------------------------------------------------------------
# API: /api/dispute-stats
# ---------------------------------------------------------------------------

class TestDisputeStatsAPI:
    def test_returns_stats_shape(self):
        resp = client.get("/api/dispute-stats")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert "total_disputes" in data["data"]
        assert "show_stat" in data["data"]

    def test_reflects_inserted_outcomes(self):
        with _db.get_db() as db:
            db.execute(
                "INSERT INTO dispute_outcomes (outcome, actual_savings) VALUES (?, ?)",
                ("reduced", 450.0),
            )
        resp = client.get("/api/dispute-stats")
        assert resp.status_code == 200
        assert resp.json()["data"]["total_disputes"] == 1


# ---------------------------------------------------------------------------
# API: /api/concierge-interest
# ---------------------------------------------------------------------------

class TestConciergeInterestAPI:
    def test_saves_email_successfully(self):
        resp = client.post(
            "/api/concierge-interest",
            data={"email": "test@example.com", "disputed_amount": "1500.00", "bill_context": "ER visit"},
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"

        with _db.get_db() as db:
            row = db.execute("SELECT * FROM concierge_interest WHERE email = ?", ("test@example.com",)).fetchone()
        assert row is not None
        assert row["disputed_amount"] == 1500.0

    def test_rejects_invalid_email(self):
        resp = client.post(
            "/api/concierge-interest",
            data={"email": "not-an-email", "disputed_amount": "500"},
        )
        assert resp.status_code == 400

    def test_email_required(self):
        resp = client.post("/api/concierge-interest", data={"disputed_amount": "500"})
        assert resp.status_code == 422


# ---------------------------------------------------------------------------
# Page rendering: results.html
# ---------------------------------------------------------------------------

class TestResultsPageRendering:
    def test_results_page_has_dispute_packet(self):
        bill_id = _insert_bill(provider_name="General Hospital")
        _insert_finding(
            bill_id, "pricing", "99285",
            _pricing_details("99285", "ER visit", 4500.0, 512.0),
            savings=3000.0,
        )
        resp = client.get(f"/results/{bill_id}")
        assert resp.status_code == 200
        html = resp.text
        assert "dispute-packet" in html

    def test_results_page_has_outcome_tracker(self):
        bill_id = _insert_bill()
        _insert_finding(
            bill_id, "pricing", "71046",
            _pricing_details("71046", "Chest X-Ray", 850.0, 51.0),
        )
        resp = client.get(f"/results/{bill_id}")
        assert resp.status_code == 200
        assert "outcome-tracker" in resp.text

    def test_results_page_404_for_missing_bill(self):
        resp = client.get("/results/9999")
        assert resp.status_code == 200
        assert "not found" in resp.text.lower()
