"""Tests for scanner — confidence flags and verification logic.
Gemini API calls are mocked since we can't make real API calls in tests."""

import sys
from unittest.mock import MagicMock

# Mock the google.genai module so scanner can be imported without the real SDK
_mock_genai = MagicMock()
sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", _mock_genai)
sys.modules.setdefault("google.genai.types", MagicMock())

from scanner import _add_confidence_flags, _quality_score, _merge_candidate  # noqa: E402


class TestAddConfidenceFlags:
    def test_high_confidence_normal_item(self):
        extracted = {
            "line_items": [
                {"cpt_code": "99283", "description": "ER visit",
                 "charged_amount": 500.00, "quantity": 1},
            ]
        }
        result = _add_confidence_flags(extracted)
        assert result["line_items"][0]["confidence"] == "high"

    def test_low_confidence_no_cpt(self):
        extracted = {
            "line_items": [
                {"cpt_code": None, "description": "Some service",
                 "charged_amount": 500.00, "quantity": 1},
            ]
        }
        result = _add_confidence_flags(extracted)
        assert result["line_items"][0]["confidence"] == "low"
        assert "flag" in result["line_items"][0]

    def test_medium_confidence_high_charge(self):
        extracted = {
            "line_items": [
                {"cpt_code": "99285", "description": "ER visit",
                 "charged_amount": 60000.00, "quantity": 1},
            ]
        }
        result = _add_confidence_flags(extracted)
        assert result["line_items"][0]["confidence"] == "medium"
        assert "very high" in result["line_items"][0]["flag"].lower()

    def test_medium_confidence_high_quantity(self):
        extracted = {
            "line_items": [
                {"cpt_code": "71046", "description": "X-Ray",
                 "charged_amount": 500.00, "quantity": 5},
            ]
        }
        result = _add_confidence_flags(extracted)
        assert result["line_items"][0]["confidence"] == "medium"
        assert "5 units" in result["line_items"][0]["flag"]

    def test_empty_line_items(self):
        extracted = {"line_items": []}
        result = _add_confidence_flags(extracted)
        assert result["line_items"] == []

    def test_multiple_items_each_assessed(self):
        extracted = {
            "line_items": [
                {"cpt_code": "99283", "description": "ER", "charged_amount": 500, "quantity": 1},
                {"cpt_code": None, "description": "Unknown", "charged_amount": 200, "quantity": 1},
                {"cpt_code": "71046", "description": "X-Ray", "charged_amount": 100, "quantity": 8},
            ]
        }
        result = _add_confidence_flags(extracted)
        assert result["line_items"][0]["confidence"] == "high"
        assert result["line_items"][1]["confidence"] == "low"
        assert result["line_items"][2]["confidence"] == "medium"


class TestOcrQualityScoring:
    def test_quality_score_penalizes_reconciliation_mismatch(self):
        strong_reconciled = {
            "provider_name": "Test",
            "total_charged": 1500.0,
            "line_items": [
                {"cpt_code": "99283", "description": "ER visit", "charged_amount": 1000.0},
                {"cpt_code": "71046", "description": "X-ray", "charged_amount": 500.0},
            ],
        }
        poor_reconciled = {
            "provider_name": "Test",
            "total_charged": 1500.0,
            "line_items": [
                {"cpt_code": "99283", "description": "ER visit", "charged_amount": 4000.0},
                {"cpt_code": None, "description": "", "charged_amount": None},
            ],
        }
        good_score, good_meta = _quality_score(strong_reconciled)
        bad_score, bad_meta = _quality_score(poor_reconciled)
        assert good_score > bad_score
        assert good_meta["reconciliation_pct"] is not None
        assert bad_meta["reconciliation_pct"] is not None

    def test_merge_candidate_fills_missing_fields(self):
        best = {
            "provider_name": "",
            "line_items": [{"cpt_code": None, "description": "", "charged_amount": None, "quantity": 0}],
        }
        fallback = {
            "provider_name": "Provider Name",
            "line_items": [{"cpt_code": "99283", "description": "ER visit", "charged_amount": 800.0, "quantity": 1}],
        }
        merged = _merge_candidate(best, fallback)
        assert merged["provider_name"] == "Provider Name"
        assert merged["line_items"][0]["cpt_code"] == "99283"
        assert merged["line_items"][0]["description"] == "ER visit"
        assert merged["line_items"][0]["charged_amount"] == 800.0
        assert merged["line_items"][0]["quantity"] == 1
