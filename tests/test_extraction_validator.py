"""Tests for validators.extraction — post-OCR extraction validation."""

from validators.extraction import validate_extraction, validate_cpt_description, cpt_exists


class TestValidateExtraction:
    def test_clean_bill_no_issues(self):
        bill = {
            "total_charged": 1200.00,
            "line_items": [
                {
                    "cpt_code": "99283",
                    "description": "ER visit level 3",
                    "charged_amount": 500.00,
                    "date_of_service": "2026-01-10",
                    "quantity": 1,
                },
                {
                    "cpt_code": "71046",
                    "description": "Chest X-Ray",
                    "charged_amount": 700.00,
                    "date_of_service": "2026-01-10",
                    "quantity": 1,
                },
            ],
        }
        issues = validate_extraction(bill)
        assert issues == []

    def test_invalid_cpt_format_flagged(self):
        bill = {
            "line_items": [
                {"cpt_code": "99", "description": "test", "charged_amount": 100},
            ]
        }
        issues = validate_extraction(bill)
        assert any("Invalid CPT format" in i for i in issues)

    def test_unknown_cpt_flagged(self):
        bill = {
            "line_items": [
                {"cpt_code": "ZZZZ1", "description": "test", "charged_amount": 100},
            ]
        }
        issues = validate_extraction(bill)
        assert any("Unknown CPT code" in i for i in issues)

    def test_negative_amount_flagged(self):
        bill = {
            "line_items": [
                {"cpt_code": "99283", "description": "test", "charged_amount": -50.00},
            ]
        }
        issues = validate_extraction(bill)
        assert any("Negative charge" in i for i in issues)

    def test_high_amount_flagged(self):
        bill = {
            "line_items": [
                {"cpt_code": "99283", "description": "test", "charged_amount": 600000.00},
            ]
        }
        issues = validate_extraction(bill)
        assert any("Suspiciously high" in i for i in issues)

    def test_future_date_flagged(self):
        bill = {
            "line_items": [
                {"cpt_code": "99283", "description": "test",
                 "charged_amount": 100, "date_of_service": "2099-01-01"},
            ]
        }
        issues = validate_extraction(bill)
        assert any("Future date" in i for i in issues)

    def test_old_date_flagged(self):
        bill = {
            "line_items": [
                {"cpt_code": "99283", "description": "test",
                 "charged_amount": 100, "date_of_service": "2015-01-01"},
            ]
        }
        issues = validate_extraction(bill)
        assert any("Very old date" in i for i in issues)

    def test_total_mismatch_flagged(self):
        bill = {
            "total_charged": 5000.00,
            "line_items": [
                {"cpt_code": "99283", "description": "test", "charged_amount": 100.00},
            ],
        }
        issues = validate_extraction(bill)
        assert any("doesn't match" in i for i in issues)

    def test_total_matches_no_issue(self):
        bill = {
            "total_charged": 100.00,
            "line_items": [
                {"cpt_code": "99283", "description": "test", "charged_amount": 100.00},
            ],
        }
        issues = validate_extraction(bill)
        assert not any("doesn't match" in i for i in issues)

    def test_negative_quantity_flagged(self):
        bill = {
            "line_items": [
                {"cpt_code": "99283", "description": "test",
                 "charged_amount": 100, "quantity": -1},
            ]
        }
        issues = validate_extraction(bill)
        assert any("Negative quantity" in i for i in issues)

    def test_empty_bill_no_issues(self):
        assert validate_extraction({"line_items": []}) == []

    def test_unparseable_date_flagged(self):
        bill = {
            "line_items": [
                {"cpt_code": "99283", "description": "test",
                 "charged_amount": 100, "date_of_service": "not-a-date"},
            ]
        }
        issues = validate_extraction(bill)
        assert any("Unparseable date" in i for i in issues)


class TestCptExists:
    def test_known_code_exists(self):
        assert cpt_exists("99283") is True

    def test_unknown_code_not_exists(self):
        assert cpt_exists("ZZZZZ") is False


class TestValidateCptDescription:
    def test_matching_description_passes(self):
        # "99283" is "ED visit, level 3 (moderate severity)" in seed data
        assert validate_cpt_description("99283", "Emergency department visit level 3") is True

    def test_unrelated_description_fails(self):
        assert validate_cpt_description("99283", "knee replacement surgery bilateral") is False

    def test_empty_inputs_pass(self):
        assert validate_cpt_description("", "anything") is True
        assert validate_cpt_description("99283", "") is True

    def test_unknown_code_passes(self):
        # No reference data to compare against
        assert validate_cpt_description("ZZZZZ", "anything") is True
