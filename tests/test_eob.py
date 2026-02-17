"""Tests for EOB reconciliation validator."""

from validators.eob import check_eob_reconciliation


class TestEobReconciliation:
    def test_flags_mismatch(self):
        extracted = {
            "line_items": [
                {
                    "description": "Test service",
                    "charged_amount": 500.0,
                    "insurance_paid": 200.0,
                    "insurance_adjustment": 200.0,
                    "patient_responsibility": 50.0,
                    "date_of_service": "2026-01-01",
                }
            ]
        }
        findings = check_eob_reconciliation(extracted)
        assert len(findings) == 1
        assert findings[0]["type"] == "eob_mismatch"

    def test_ignores_balanced_line(self):
        extracted = {
            "line_items": [
                {
                    "description": "Balanced service",
                    "charged_amount": 500.0,
                    "insurance_paid": 200.0,
                    "insurance_adjustment": 200.0,
                    "patient_responsibility": 100.0,
                }
            ]
        }
        findings = check_eob_reconciliation(extracted)
        assert findings == []
