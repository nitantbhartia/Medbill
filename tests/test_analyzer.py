"""Tests for analyzer — full bill analysis pipeline, confidence scoring, persistence."""

import json

from analyzer import (
    analyze_bill, save_bill_and_findings, get_bill_results, get_stats,
    _assign_confidence, _prorate_patient_responsibility,
)
from db import get_db
from tests.conftest import (
    SAMPLE_BILL,
    SAMPLE_BILL_WITH_DUPLICATES,
    SAMPLE_BILL_WITH_UNBUNDLING,
    SAMPLE_BILL_EMERGENCY_HIGH_OOP,
)


class TestAnalyzeBill:
    def test_sample_bill_finds_issues(self):
        result = analyze_bill(SAMPLE_BILL, "33021")
        assert result["total_findings"] > 0
        assert result["total_potential_savings"] > 0
        assert result["bill_total"] == 12847.00
        assert result["patient_owes"] == 4215.00

    def test_findings_sorted_by_severity(self):
        result = analyze_bill(SAMPLE_BILL, "33021")
        severities = [f["severity"] for f in result["findings"]]
        order = {"high": 0, "medium": 1, "low": 2}
        for i in range(len(severities) - 1):
            assert order[severities[i]] <= order[severities[i + 1]]

    def test_duplicate_bill_detected(self):
        result = analyze_bill(SAMPLE_BILL_WITH_DUPLICATES, "33021")
        dup_findings = [f for f in result["findings"] if f["type"] == "duplicate_charge"]
        assert len(dup_findings) >= 1

    def test_unbundling_detected(self):
        result = analyze_bill(SAMPLE_BILL_WITH_UNBUNDLING, "33021")
        unbundle = [f for f in result["findings"] if f["type"] == "unbundling"]
        assert len(unbundle) >= 1

    def test_upcoding_detected_for_level_5_er(self):
        result = analyze_bill(SAMPLE_BILL, "33021")
        upcode = [f for f in result["findings"] if f["type"] == "upcoding"]
        assert len(upcode) >= 1

    def test_price_markup_detected(self):
        result = analyze_bill(SAMPLE_BILL, "33021")
        markups = [f for f in result["findings"] if f["type"] == "price_markup"]
        assert len(markups) >= 1

    def test_nsa_detected_for_emergency_high_oop(self):
        result = analyze_bill(SAMPLE_BILL_EMERGENCY_HIGH_OOP, "33021")
        nsa = [f for f in result["findings"] if f["type"] == "no_surprises_act"]
        assert len(nsa) >= 1

    def test_empty_bill_no_findings(self):
        result = analyze_bill({"line_items": []}, "33021")
        assert result["total_findings"] == 0
        assert result["total_potential_savings"] == 0

    def test_quantity_flag(self):
        bill = {
            "line_items": [
                {"cpt_code": "71046", "description": "X-Ray",
                 "charged_amount": 1000.00, "quantity": 3},
            ]
        }
        result = analyze_bill(bill, "33021")
        qty_flags = [f for f in result["findings"] if f["type"] == "quantity_flag"]
        assert len(qty_flags) >= 1

    def test_warnings_populated(self):
        result = analyze_bill(SAMPLE_BILL, "33021")
        assert "warnings" in result
        assert isinstance(result["warnings"], list)

    def test_confidence_assigned_to_findings(self):
        result = analyze_bill(SAMPLE_BILL, "33021")
        for finding in result["findings"]:
            assert "confidence" in finding
            assert finding["confidence"] in ("high", "medium", "low")
            assert "evidence" in finding
            assert finding["evidence"]["source"]


class TestConfidenceScoring:
    def test_duplicate_is_high(self):
        assert _assign_confidence({"type": "duplicate_charge"}) == "high"

    def test_high_markup_is_high(self):
        assert _assign_confidence({"type": "price_markup", "markup_multiple": 7}) == "high"

    def test_moderate_markup_is_medium(self):
        assert _assign_confidence({"type": "price_markup", "markup_multiple": 4}) == "medium"

    def test_unbundling_mod0_is_high(self):
        assert _assign_confidence({"type": "unbundling", "modifier_indicator": "0"}) == "high"

    def test_unbundling_mod1_is_medium(self):
        assert _assign_confidence({"type": "unbundling", "modifier_indicator": "1"}) == "medium"

    def test_upcoding_is_medium(self):
        assert _assign_confidence({"type": "upcoding"}) == "medium"

    def test_quantity_flag_is_low(self):
        assert _assign_confidence({"type": "quantity_flag"}) == "low"

    def test_nsa_is_low(self):
        assert _assign_confidence({"type": "no_surprises_act"}) == "low"

    def test_unknown_type_is_low(self):
        assert _assign_confidence({"type": "something_new"}) == "low"


class TestSaveAndRetrieve:
    def test_save_and_get_results(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        assert bill_id > 0

        results = get_bill_results(bill_id)
        assert results is not None
        assert results["bill"]["id"] == bill_id
        assert results["bill"]["provider_name"] == "Memorial Regional Hospital"
        assert len(results["line_items"]) == 3
        assert len(results["findings"]) > 0

    def test_findings_persisted_correctly(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        results = get_bill_results(bill_id)

        for finding in results["findings"]:
            assert finding["finding_type"] is not None
            assert finding["severity"] in ("high", "medium", "low")
            assert finding["message"]

    def test_nonexistent_bill_returns_none(self):
        assert get_bill_results(99999) is None

    def test_line_item_medicare_rate_populated(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        results = get_bill_results(bill_id)

        # At least one line item should have a Medicare rate
        rates = [li["medicare_rate"] for li in results["line_items"] if li["medicare_rate"]]
        assert len(rates) > 0


class TestGetStats:
    def test_empty_db_returns_zeros(self):
        stats = get_stats()
        assert stats["bills_scanned"] == 0
        assert stats["total_found"] == 0

    def test_stats_after_save(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        save_bill_and_findings(None, SAMPLE_BILL, analysis)

        stats = get_stats()
        assert stats["bills_scanned"] >= 1
        assert stats["total_found"] > 0
        assert stats["avg_savings"] > 0


class TestProration:
    def test_prorates_total_patient_owes_across_items(self):
        extracted = {
            "total_patient_owes": 300.0,
            "line_items": [
                {"charged_amount": 600.0},
                {"charged_amount": 400.0},
            ],
        }
        _prorate_patient_responsibility(extracted)
        assert extracted["line_items"][0]["patient_responsibility"] == 180.0
        assert extracted["line_items"][1]["patient_responsibility"] == 120.0

    def test_skips_proration_when_per_line_data_exists(self):
        extracted = {
            "total_patient_owes": 300.0,
            "line_items": [
                {"charged_amount": 600.0, "patient_responsibility": 200.0},
                {"charged_amount": 400.0},
            ],
        }
        _prorate_patient_responsibility(extracted)
        assert extracted["line_items"][0]["patient_responsibility"] == 200.0
        assert extracted["line_items"][1].get("patient_responsibility") is None

    def test_skips_proration_when_no_total_patient_owes(self):
        extracted = {
            "line_items": [{"charged_amount": 600.0}],
        }
        _prorate_patient_responsibility(extracted)
        assert extracted["line_items"][0].get("patient_responsibility") is None

    def test_savings_capped_to_prorated_share(self):
        bill = {
            "total_charged": 1000.0,
            "total_patient_owes": 200.0,
            "line_items": [
                {"cpt_code": "99285", "description": "ER visit high", "charged_amount": 1000.0, "quantity": 1},
            ],
        }
        result = analyze_bill(bill, "33021")
        if result["total_findings"] > 0:
            assert result["total_potential_savings"] <= 200.0

    def test_infers_patient_owes_from_insurance_breakdown_when_missing(self):
        bill = {
            "total_charged": 740.62,
            "line_items": [
                {
                    "cpt_code": "99214",
                    "description": "Office visit established",
                    "charged_amount": 350.30,
                    "insurance_paid": 300.00,
                    "insurance_adjustment": 0.0,
                    "quantity": 1,
                },
                {
                    "cpt_code": "99396",
                    "description": "Preventive visit",
                    "charged_amount": 390.32,
                    "insurance_paid": 338.53,
                    "insurance_adjustment": 0.0,
                    "quantity": 1,
                },
            ],
        }
        result = analyze_bill(bill, "33021")
        assert result["patient_owes"] == 102.09
        assert result["patient_owes_inferred_source"] == "charged_minus_insurance"
        assert result["total_potential_savings"] <= 102.09

    def test_infers_patient_owes_from_line_responsibility_when_missing(self):
        bill = {
            "total_charged": 1000.0,
            "line_items": [
                {
                    "cpt_code": "99214",
                    "description": "Office visit established",
                    "charged_amount": 600.0,
                    "patient_responsibility": 60.0,
                    "quantity": 1,
                },
                {
                    "cpt_code": "99213",
                    "description": "Office visit",
                    "charged_amount": 400.0,
                    "patient_responsibility": 40.0,
                    "quantity": 1,
                },
            ],
        }
        result = analyze_bill(bill, "33021")
        assert result["patient_owes"] == 100.0
        assert result["patient_owes_inferred_source"] == "line_item_patient_responsibility"
        assert result["total_potential_savings"] <= 100.0
