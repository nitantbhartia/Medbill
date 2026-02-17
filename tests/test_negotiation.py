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
    _phone_lines_for_finding,
    _message_line_for_finding,
    _is_insurance_processed,
    PROHIBITED_PATTERNS,
    NEGOTIATION_STAGES,
)
from analyzer import analyze_bill, save_bill_and_findings  # noqa: E402
from db import get_db  # noqa: E402
from tests.conftest import (  # noqa: E402
    SAMPLE_BILL,
    SAMPLE_BILL_WITH_DUPLICATES,
    SAMPLE_BILL_WITH_UNBUNDLING,
    SAMPLE_BILL_EMERGENCY_HIGH_OOP,
)


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

    def test_script_has_prep_section(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_phone_script(bill_id)
        assert "BEFORE YOU CALL" in script
        assert "itemized bill" in script.lower()

    def test_script_has_objection_handling(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_phone_script(bill_id)
        assert "IF THEY PUSH BACK" in script
        assert "supervisor" in script.lower()

    def test_script_includes_provider_name(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_phone_script(bill_id)
        assert "Memorial Regional Hospital" in script

    def test_insured_script_asks_for_resubmission(self):
        """SAMPLE_BILL has insurance data, so script should ask to resubmit."""
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_phone_script(bill_id)
        assert "resubmitted to my insurance" in script
        assert "patient responsibility" in script

    def test_uninsured_script_shows_total_savings(self):
        """SAMPLE_BILL_WITH_DUPLICATES has no insurance data, keeps old framing."""
        analysis = analyze_bill(SAMPLE_BILL_WITH_DUPLICATES, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL_WITH_DUPLICATES, analysis)
        script = generate_phone_script(bill_id)
        assert "adjustments total approximately" in script or "corrected bill" in script

    def test_script_shows_up_to_five_findings(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_phone_script(bill_id)
        # Should have numbered POINT markers
        assert "POINT 1:" in script

    def test_duplicate_bill_mentions_billed_twice(self):
        analysis = analyze_bill(SAMPLE_BILL_WITH_DUPLICATES, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL_WITH_DUPLICATES, analysis)
        script = generate_phone_script(bill_id)
        assert "billed twice" in script.lower() or "performed twice" in script.lower()

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

    def test_script_requests_response_deadline(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_message_script(bill_id)
        assert "30 days" in script

    def test_script_mentions_financial_assistance(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_message_script(bill_id)
        assert "financial assistance" in script.lower()

    def test_duplicate_bill_mentions_duplicate(self):
        analysis = analyze_bill(SAMPLE_BILL_WITH_DUPLICATES, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL_WITH_DUPLICATES, analysis)
        script = generate_message_script(bill_id)
        assert "duplicate" in script.lower()

    def test_unbundling_bill_mentions_ncci(self):
        analysis = analyze_bill(SAMPLE_BILL_WITH_UNBUNDLING, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL_WITH_UNBUNDLING, analysis)
        script = generate_message_script(bill_id)
        assert "NCCI" in script

    def test_no_findings_returns_empty(self):
        with get_db() as db:
            cursor = db.execute(
                "INSERT INTO bills (provider_name, total_charged, total_patient_owes, "
                "total_findings, status) VALUES ('Test', 100, 100, 0, 'analyzed')"
            )
        assert generate_message_script(cursor.lastrowid) == ""

    def test_nonexistent_bill_returns_empty(self):
        assert generate_message_script(99999) == ""


class TestPhoneLinesForFinding:
    """Unit tests for _phone_lines_for_finding with all 7 finding types."""

    def test_duplicate_charge(self):
        finding = {"finding_type": "duplicate_charge", "message": "dup"}
        details = {"potential_savings": 850.00}
        li = {"description": "Chest X-ray", "cpt_code": "71046", "date_of_service": "2026-01-10"}
        lines = _phone_lines_for_finding(finding, details, li)
        assert any("billed twice" in l for l in lines)
        assert any("$850.00" in l for l in lines)

    def test_price_markup_with_opps(self):
        finding = {"finding_type": "price_markup", "message": "markup"}
        details = {
            "charged": 4500.00, "medicare_rate": 227.00,
            "markup_multiple": 19.8, "total_medicare": 1000.00,
        }
        li = {"description": "ED visit", "cpt_code": "99285"}
        lines = _phone_lines_for_finding(finding, details, li)
        text = " ".join(lines)
        assert "19.8x" in text
        assert "$1,000.00" in text
        assert "facility fee" in text

    def test_price_markup_without_opps(self):
        finding = {"finding_type": "price_markup", "message": "markup"}
        details = {"charged": 350.00, "medicare_rate": 14.49, "markup_multiple": 24.2}
        li = {"description": "CMP", "cpt_code": "80053"}
        lines = _phone_lines_for_finding(finding, details, li)
        text = " ".join(lines)
        assert "24.2x" in text
        assert "facility fee" not in text

    def test_unbundling(self):
        finding = {"finding_type": "unbundling", "message": "unbundle"}
        details = {"code_1": "80053", "code_2": "80048", "potential_savings": 250.00}
        li = {}
        lines = _phone_lines_for_finding(finding, details, li)
        text = " ".join(lines)
        assert "NCCI" in text
        assert "80053" in text
        assert "80048" in text

    def test_upcoding(self):
        finding = {"finding_type": "upcoding", "message": "upcode"}
        details = {"billed_level": "5", "likely_level": "3", "potential_savings": 200.00}
        li = {}
        lines = _phone_lines_for_finding(finding, details, li)
        text = " ".join(lines)
        assert "Level 5" in text
        assert "Level 3" in text

    def test_quantity_flag(self):
        finding = {"finding_type": "quantity_flag", "message": "qty"}
        details = {}
        li = {"description": "CBC", "quantity": 3}
        lines = _phone_lines_for_finding(finding, details, li)
        assert any("3 units" in l for l in lines)

    def test_benchmark_outlier(self):
        finding = {"finding_type": "benchmark_outlier", "message": "bench"}
        details = {"charged": 8000.00, "median_charged": 2500.00, "sample_size": 3800}
        li = {"description": "ED visit"}
        lines = _phone_lines_for_finding(finding, details, li)
        text = " ".join(lines)
        assert "median" in text
        assert "3800" in text

    def test_no_surprises_act(self):
        finding = {"finding_type": "no_surprises_act", "message": "nsa"}
        lines = _phone_lines_for_finding(finding, {}, {})
        text = " ".join(lines)
        assert "No Surprises Act" in text

    def test_unknown_type_uses_message(self):
        finding = {"finding_type": "something_new", "message": "custom message here"}
        lines = _phone_lines_for_finding(finding, {}, {})
        assert lines == ["custom message here"]


class TestMessageLineForFinding:
    """Unit tests for _message_line_for_finding with all 7 finding types."""

    def test_duplicate_charge(self):
        finding = {"finding_type": "duplicate_charge", "message": "dup"}
        details = {"potential_savings": 850.00}
        li = {"description": "Chest X-ray", "cpt_code": "71046", "date_of_service": "2026-01-10"}
        line = _message_line_for_finding(1, finding, details, li)
        assert line.startswith("1.")
        assert "duplicate" in line.lower()
        assert "$850.00" in line

    def test_price_markup_with_opps(self):
        finding = {"finding_type": "price_markup", "message": "markup"}
        details = {
            "charged": 4500.00, "medicare_rate": 227.00,
            "markup_multiple": 19.8, "total_medicare": 1000.00,
        }
        li = {"description": "ED visit", "cpt_code": "99285"}
        line = _message_line_for_finding(2, finding, details, li)
        assert "OPPS" in line
        assert "$1,000.00" in line

    def test_unbundling_references_ncci(self):
        finding = {"finding_type": "unbundling", "message": "unbundle"}
        details = {"code_1": "80053", "code_2": "80048", "potential_savings": 250.00}
        line = _message_line_for_finding(3, finding, details, {})
        assert "NCCI" in line
        assert "$250.00" in line

    def test_upcoding(self):
        finding = {"finding_type": "upcoding", "message": "upcode"}
        details = {"billed_level": "5", "likely_level": "3"}
        li = {"cpt_code": "99285"}
        line = _message_line_for_finding(1, finding, details, li)
        assert "Level 5" in line
        assert "documentation" in line.lower()

    def test_quantity_flag(self):
        finding = {"finding_type": "quantity_flag", "message": "qty"}
        li = {"description": "CBC", "quantity": 3}
        line = _message_line_for_finding(1, finding, {}, li)
        assert "3 units" in line

    def test_benchmark_outlier(self):
        finding = {"finding_type": "benchmark_outlier", "message": "bench"}
        details = {"charged": 8000.00, "median_charged": 2500.00, "sample_size": 3800}
        li = {"description": "ED visit", "cpt_code": "99285"}
        line = _message_line_for_finding(1, finding, details, li)
        assert "median" in line
        assert "fair-price" in line.lower()

    def test_no_surprises_act(self):
        finding = {"finding_type": "no_surprises_act", "message": "nsa"}
        line = _message_line_for_finding(1, finding, {}, {})
        assert "No Surprises Act" in line
        assert "federal law" in line.lower()

    def test_unknown_type_uses_message(self):
        finding = {"finding_type": "other", "message": "custom issue"}
        line = _message_line_for_finding(4, finding, {}, {})
        assert line == "4. custom issue"


class TestInsuranceAwareness:
    """Tests for insurance-processed vs self-pay script differences."""

    def test_is_insurance_processed_with_insurance(self):
        items = [{"insurance_paid": 500, "patient_responsibility": 100}]
        assert _is_insurance_processed(items) is True

    def test_is_insurance_processed_without_insurance(self):
        items = [{"charged_amount": 500}]
        assert _is_insurance_processed(items) is False

    def test_is_insurance_processed_patient_resp_only(self):
        items = [{"patient_responsibility": 200}]
        assert _is_insurance_processed(items) is True

    def test_phone_insured_mentions_patient_responsibility(self):
        """Full integration: SAMPLE_BILL has insurance, script should reference patient resp."""
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_phone_script(bill_id)
        assert "$4,215.00" in script
        assert "insurance has processed" in script

    def test_phone_uninsured_mentions_standard_rate(self):
        """SAMPLE_BILL_WITH_DUPLICATES has no insurance, script uses self-pay language."""
        analysis = analyze_bill(SAMPLE_BILL_WITH_DUPLICATES, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL_WITH_DUPLICATES, analysis)
        script = generate_phone_script(bill_id)
        assert "self-pay" in script.lower() or "standard rate" in script.lower()

    def test_message_insured_asks_resubmit(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_message_script(bill_id)
        assert "resubmitted to my insurance" in script
        assert "$4,215.00" in script

    def test_message_uninsured_shows_total_savings(self):
        analysis = analyze_bill(SAMPLE_BILL_WITH_DUPLICATES, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL_WITH_DUPLICATES, analysis)
        script = generate_message_script(bill_id)
        assert "corrected bill" in script or "potential adjustment" in script

    def test_phone_markup_insured_uses_patient_resp(self):
        """When line item has patient_responsibility, phone line references it."""
        finding = {"finding_type": "price_markup", "message": "markup"}
        details = {"charged": 4500.00, "medicare_rate": 227.00, "markup_multiple": 19.8}
        li = {"description": "ED visit", "cpt_code": "99285", "patient_responsibility": 1200.00}
        lines = _phone_lines_for_finding(finding, details, li)
        text = " ".join(lines)
        assert "$1,200.00" in text
        assert "patient responsibility" in text
        assert "prompt-pay" in text.lower() or "fair-price" in text.lower()

    def test_phone_markup_uninsured_uses_charged(self):
        """When no patient_responsibility, phone line references charged amount."""
        finding = {"finding_type": "price_markup", "message": "markup"}
        details = {"charged": 4500.00, "medicare_rate": 227.00, "markup_multiple": 19.8}
        li = {"description": "ED visit", "cpt_code": "99285"}
        lines = _phone_lines_for_finding(finding, details, li)
        text = " ".join(lines)
        assert "$4,500.00" in text
        assert "19.8x" in text

    def test_phone_duplicate_insured_asks_resubmit(self):
        finding = {"finding_type": "duplicate_charge", "message": "dup"}
        details = {"potential_savings": 850.00}
        li = {"description": "X-ray", "cpt_code": "71046", "date_of_service": "2026-01-10",
              "insurance_paid": 180.00}
        lines = _phone_lines_for_finding(finding, details, li)
        text = " ".join(lines)
        assert "resubmitted" in text

    def test_phone_duplicate_uninsured_shows_savings(self):
        finding = {"finding_type": "duplicate_charge", "message": "dup"}
        details = {"potential_savings": 850.00}
        li = {"description": "X-ray", "cpt_code": "71046", "date_of_service": "2026-01-10"}
        lines = _phone_lines_for_finding(finding, details, li)
        text = " ".join(lines)
        assert "$850.00" in text
        assert "removed" in text

    def test_message_markup_insured_uses_patient_resp(self):
        finding = {"finding_type": "price_markup", "message": "markup"}
        details = {"charged": 4500.00, "medicare_rate": 227.00, "markup_multiple": 19.8}
        li = {"description": "ED visit", "cpt_code": "99285", "patient_responsibility": 1200.00}
        line = _message_line_for_finding(1, finding, details, li)
        assert "$1,200.00" in line
        assert "patient responsibility" in line

    def test_message_unbundling_insured_asks_resubmit(self):
        finding = {"finding_type": "unbundling", "message": "unbundle"}
        details = {"code_1": "80053", "code_2": "80048", "potential_savings": 250.00}
        li = {"insurance_paid": 100.00}
        line = _message_line_for_finding(1, finding, details, li)
        assert "resubmit" in line.lower()

    def test_insured_objection_handling_different(self):
        """Insured script has different objection handling."""
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        script = generate_phone_script(bill_id)
        assert "your insurance determined what you owe" in script
        assert "prompt-pay discount" in script


class TestNegotiationStages:
    def test_all_stages_defined(self):
        expected = ["stage_1", "stage_2", "stage_3", "stage_4"]
        for stage in expected:
            assert stage in NEGOTIATION_STAGES
            assert "name" in NEGOTIATION_STAGES[stage]
            assert "tone" in NEGOTIATION_STAGES[stage]
