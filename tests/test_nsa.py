"""Tests for validators.nsa — No Surprises Act applicability checks."""

from validators.nsa import check_no_surprises_act
from tests.conftest import SAMPLE_BILL_EMERGENCY_HIGH_OOP


class TestNoSurprisesAct:
    def test_emergency_high_oop_flagged(self):
        result = check_no_surprises_act(SAMPLE_BILL_EMERGENCY_HIGH_OOP)
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
