"""Tests for validators.nsa — No Surprises Act applicability checks."""

from validators.nsa import check_no_surprises_act
from tests.conftest import SAMPLE_BILL_EMERGENCY_HIGH_OOP


class TestNoSurprisesAct:
    def test_emergency_high_oop_flagged(self):
        result = check_no_surprises_act({**SAMPLE_BILL_EMERGENCY_HIGH_OOP, "insurer_name": "Aetna"})
        assert result is not None
        assert result["type"] == "no_surprises_act"
        assert result["severity"] == "high"
        assert result["potential_savings"] > 0
        assert "No Surprises Act" in result["message"]

    def test_non_emergency_not_flagged(self):
        bill = {
            "total_charged": 5000.00,
            "total_patient_owes": 4000.00,
            "line_items": [
                {"cpt_code": "99214", "description": "Office visit", "charged_amount": 5000.00},
            ],
        }
        assert check_no_surprises_act(bill) is None

    def test_emergency_low_oop_not_flagged(self):
        bill = {
            "total_charged": 10000.00,
            "total_patient_owes": 1000.00,  # only 10% — not high
            "line_items": [
                {"cpt_code": "99285", "description": "ER visit", "charged_amount": 6000.00},
            ],
        }
        assert check_no_surprises_act(bill) is None

    def test_out_of_network_indicator_flagged(self):
        bill = {
            "total_charged": 5000.00,
            "total_patient_owes": 1000.00,
            "line_items": [
                {"cpt_code": "99285", "description": "out of network ER visit",
                 "charged_amount": 5000.00},
            ],
        }
        result = check_no_surprises_act(bill)
        assert result is not None

    def test_empty_bill_not_flagged(self):
        assert check_no_surprises_act({"line_items": []}) is None

    def test_missing_totals_not_flagged(self):
        bill = {
            "line_items": [
                {"cpt_code": "99285", "description": "ER visit", "charged_amount": 500.00},
            ],
        }
        assert check_no_surprises_act(bill) is None

    def test_self_pay_rutherford_bill_not_flagged(self):
        bill = {
            "provider_name": "Saint Thomas Rutherford Hospital",
            "total_charged": 6609.40,
            "total_patient_owes": 6609.40,
            "line_items": [
                {"cpt_code": "74176", "description": "CT abdomen and pelvis without contrast", "charged_amount": 4699.40},
                {"cpt_code": "99282", "description": "Emergency department visit, level 2", "charged_amount": 1910.00},
            ],
        }
        assert check_no_surprises_act(bill) is None

    def test_insured_emergency_bill_with_payments_flagged(self):
        bill = {
            "total_charged": 6609.40,
            "total_patient_owes": 5200.00,
            "line_items": [
                {"cpt_code": "99282", "description": "Emergency department visit, level 2",
                 "charged_amount": 1910.00, "insurance_paid": 150.00, "insurance_adjustment": 300.00},
            ],
        }
        assert check_no_surprises_act(bill) is not None
