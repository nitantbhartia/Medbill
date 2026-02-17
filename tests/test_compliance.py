"""Tests for compliance helpers."""

from analyzer import analyze_bill, save_bill_and_findings
from compliance import scrub_extracted_data, export_bill_data, delete_bill_data, record_consent
from tests.conftest import SAMPLE_BILL


class TestComplianceHelpers:
    def test_scrub_extracted_data(self):
        payload = dict(SAMPLE_BILL)
        payload["patient_name"] = "Jane Doe"
        payload["account_number"] = "ABC123456789"
        out = scrub_extracted_data(payload)
        assert out["patient_name"] is None
        assert out["account_number"].endswith("6789")

    def test_export_and_delete(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        consent_id = record_consent(None, bill_id, "tos", "v1")
        assert consent_id > 0

        exported = export_bill_data(bill_id)
        assert exported is not None
        assert exported["bill"]["id"] == bill_id
        assert delete_bill_data(bill_id) is True
        assert export_bill_data(bill_id) is None
