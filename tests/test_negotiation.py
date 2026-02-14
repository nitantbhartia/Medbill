"""Tests for negotiation — email validation, phone script, negotiation creation."""

import sys
import json
from unittest.mock import MagicMock

# Mock google.genai so negotiation.py can be imported without the real SDK
sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

from negotiation import (  # noqa: E402
    validate_outbound_email,
    create_negotiation,
    approve_and_send,
    generate_phone_script,
    generate_message_script,
    PROHIBITED_PATTERNS,
    NEGOTIATION_STAGES,
)
from analyzer import analyze_bill, save_bill_and_findings  # noqa: E402
from db import get_db  # noqa: E402
from tests.conftest import SAMPLE_BILL  # noqa: E402


class TestValidateOutboundEmail:
    def test_clean_email_approved(self):
        body = (
            "Dear billing department, I am writing regarding account #12345. "
            "I noticed a potential duplicate charge for CPT 71046 on January 10. "
            "Could you please review and correct this? Thank you."
        )
        result = validate_outbound_email(body)
        assert result["approved"] is True
        assert result["violations"] == []

    def test_lawsuit_threat_blocked(self):
        body = "If you don't fix this, I will file a lawsuit against the hospital."
        result = validate_outbound_email(body)
        assert result["approved"] is False
        assert len(result["violations"]) > 0

    def test_legal_action_blocked(self):
        body = "We will take legal action if this is not resolved."
        result = validate_outbound_email(body)
        assert result["approved"] is False

    def test_fraud_language_blocked(self):
        body = "This is clearly fraud and theft by the hospital."
        result = validate_outbound_email(body)
        assert result["approved"] is False

    def test_demand_language_blocked(self):
        body = "We demand you reduce the bill immediately. You must immediately correct this."
        result = validate_outbound_email(body)
        assert result["approved"] is False

    def test_claiming_to_be_lawyer_blocked(self):
        body = "I am a lawyer representing the patient in this matter."
        result = validate_outbound_email(body)
        assert result["approved"] is False

    def test_guarantee_language_blocked(self):
        body = "We guarantee the bill will be reduced by at least $2,000."
        result = validate_outbound_email(body)
        assert result["approved"] is False

    def test_medical_necessity_blocked(self):
        body = "This procedure was medically unnecessary and should not have been prescribed."
        result = validate_outbound_email(body)
        assert result["approved"] is False

    def test_diagnosis_wrong_blocked(self):
        body = "The diagnosis was incorrect and needs to be changed."
        result = validate_outbound_email(body)
        assert result["approved"] is False

    def test_case_insensitive_matching(self):
        body = "THIS IS ILLEGAL and constitutes FRAUD by the hospital."
        result = validate_outbound_email(body)
        assert result["approved"] is False


class TestCreateNegotiation:
    def _create_bill(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        with get_db() as db:
            cursor = db.execute(
                "INSERT INTO users (email, zip_code) VALUES (?, ?)",
                ("test@test.com", "33021"),
            )
            user_id = cursor.lastrowid
        return bill_id, user_id

    def test_create_negotiation(self):
        bill_id, user_id = self._create_bill()
        neg_id = create_negotiation(bill_id, user_id, "ACC-12345", "billing@hospital.com")
        assert neg_id > 0

        with get_db() as db:
            neg = db.execute("SELECT * FROM negotiations WHERE id = ?", (neg_id,)).fetchone()
        assert neg["bill_id"] == bill_id
        assert neg["account_number"] == "ACC-12345"
        assert neg["status"] == "pending_auth"
        assert neg["current_stage"] == "stage_1"

    def test_create_negotiation_invalid_bill(self):
        import pytest
        with pytest.raises(ValueError, match="not found"):
            create_negotiation(99999, 1, "ACC-123")


class TestApproveAndSend:
    def test_approve_message(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        with get_db() as db:
            cursor = db.execute(
                "INSERT INTO users (email, zip_code) VALUES (?, ?)",
                ("test2@test.com", "33021"),
            )
            user_id = cursor.lastrowid

        neg_id = create_negotiation(bill_id, user_id, "ACC-999")

        with get_db() as db:
            cursor = db.execute(
                "INSERT INTO negotiation_messages (negotiation_id, direction, stage, "
                "subject, body, patient_summary) VALUES (?, 'outbound', 'stage_1', "
                "'Test Subject', 'Test body', 'Test summary')",
                (neg_id,),
            )
            msg_id = cursor.lastrowid

        result = approve_and_send(msg_id)
        assert result is True

        with get_db() as db:
            msg = db.execute("SELECT * FROM negotiation_messages WHERE id = ?", (msg_id,)).fetchone()
            assert msg["user_approved"] == 1
            assert msg["approved_at"] is not None

            neg = db.execute("SELECT * FROM negotiations WHERE id = ?", (neg_id,)).fetchone()
            assert neg["status"] == "awaiting_response"
            assert neg["rounds_completed"] == 1


class TestGeneratePhoneScript:
    def test_script_generated(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_phone_script(bill_id)
        assert len(script) > 0
        assert "account" in script.lower() or "bill" in script.lower()

    def test_script_references_findings(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_phone_script(bill_id)
        assert "$" in script or "CPT" in script

    def test_no_findings_returns_empty(self):
        with get_db() as db:
            cursor = db.execute(
                "INSERT INTO bills (provider_name, total_charged, total_patient_owes, "
                "total_findings, status) VALUES ('Test', 100, 100, 0, 'analyzed')"
            )
        script = generate_phone_script(cursor.lastrowid)
        assert script == ""

    def test_nonexistent_bill_returns_empty(self):
        assert generate_phone_script(99999) == ""


class TestGenerateMessageScript:
    def test_script_generated(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_message_script(bill_id)
        assert len(script) > 0
        assert "Billing Department" in script

    def test_script_includes_findings(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_message_script(bill_id)
        assert "$" in script or "CPT" in script

    def test_script_is_professional(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_message_script(bill_id)
        assert "respectfully" in script.lower() or "request" in script.lower()
        assert "Subject:" in script

    def test_no_findings_returns_empty(self):
        with get_db() as db:
            cursor = db.execute(
                "INSERT INTO bills (provider_name, total_charged, total_patient_owes, "
                "total_findings, status) VALUES ('Test', 100, 100, 0, 'analyzed')"
            )
        assert generate_message_script(cursor.lastrowid) == ""

    def test_nonexistent_bill_returns_empty(self):
        assert generate_message_script(99999) == ""


class TestNegotiationStages:
    def test_all_stages_defined(self):
        expected = ["stage_1", "stage_2", "stage_3", "stage_4"]
        for stage in expected:
            assert stage in NEGOTIATION_STAGES
            assert "name" in NEGOTIATION_STAGES[stage]
            assert "tone" in NEGOTIATION_STAGES[stage]
