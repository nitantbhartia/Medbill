"""Tests for provider intelligence aggregation."""

from analyzer import analyze_bill, save_bill_and_findings
from provider_intelligence import get_provider_intelligence
from db import get_db
from tests.conftest import SAMPLE_BILL


class TestProviderIntelligence:
    def test_returns_provider_summary(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        with get_db() as db:
            db.execute(
                "INSERT INTO users (email, zip_code) VALUES (?, ?)",
                ("provider@test.com", "33021"),
            )
            user_id = db.execute("SELECT id FROM users WHERE email = ?", ("provider@test.com",)).fetchone()["id"]
            db.execute(
                "INSERT INTO dispute_outcomes (bill_id, user_id, hospital_name, called_billing, "
                "outcome, original_patient_owes, final_patient_owes, actual_savings) "
                "VALUES (?, ?, ?, 1, 'reduced', 1000, 700, 300)",
                (bill_id, user_id, SAMPLE_BILL["provider_name"]),
            )

        data = get_provider_intelligence(SAMPLE_BILL["provider_name"])
        assert data["provider_name"] == SAMPLE_BILL["provider_name"]
        assert data["overview"]["bills_scanned"] >= 1
