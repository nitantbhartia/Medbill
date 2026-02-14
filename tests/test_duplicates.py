"""Tests for validators.duplicates — duplicate charge detection."""

from validators.duplicates import find_duplicates


class TestFindDuplicates:
    def test_exact_duplicate_detected(self):
        items = [
            {"cpt_code": "71046", "date_of_service": "2026-01-10", "quantity": 1,
             "charged_amount": 850.00, "description": "Chest X-Ray"},
            {"cpt_code": "71046", "date_of_service": "2026-01-10", "quantity": 1,
             "charged_amount": 850.00, "description": "Chest X-Ray"},
        ]
        result = find_duplicates(items[0], items)
        assert result is not None
        assert result["type"] == "duplicate_charge"
        assert result["severity"] == "high"
        assert result["potential_savings"] == 850.00

    def test_second_item_not_double_reported(self):
        items = [
            {"cpt_code": "71046", "date_of_service": "2026-01-10", "quantity": 1,
             "charged_amount": 850.00, "description": "Chest X-Ray"},
            {"cpt_code": "71046", "date_of_service": "2026-01-10", "quantity": 1,
             "charged_amount": 850.00, "description": "Chest X-Ray"},
        ]
        # First item reports the duplicate
        assert find_duplicates(items[0], items) is not None
        # Second item should NOT also report (avoids double-counting)
        assert find_duplicates(items[1], items) is None

    def test_different_dates_not_flagged(self):
        items = [
            {"cpt_code": "71046", "date_of_service": "2026-01-10", "quantity": 1,
             "charged_amount": 850.00, "description": "Chest X-Ray"},
            {"cpt_code": "71046", "date_of_service": "2026-01-11", "quantity": 1,
             "charged_amount": 850.00, "description": "Chest X-Ray"},
        ]
        assert find_duplicates(items[0], items) is None

    def test_different_amounts_not_flagged(self):
        items = [
            {"cpt_code": "71046", "date_of_service": "2026-01-10", "quantity": 1,
             "charged_amount": 850.00, "description": "Chest X-Ray"},
            {"cpt_code": "71046", "date_of_service": "2026-01-10", "quantity": 1,
             "charged_amount": 900.00, "description": "Chest X-Ray"},
        ]
        assert find_duplicates(items[0], items) is None

    def test_different_codes_not_flagged(self):
        items = [
            {"cpt_code": "71046", "date_of_service": "2026-01-10", "quantity": 1,
             "charged_amount": 850.00, "description": "Chest X-Ray 2v"},
            {"cpt_code": "71045", "date_of_service": "2026-01-10", "quantity": 1,
             "charged_amount": 850.00, "description": "Chest X-Ray 1v"},
        ]
        assert find_duplicates(items[0], items) is None

    def test_no_cpt_code_returns_none(self):
        items = [{"description": "test", "date_of_service": "2026-01-10"}]
        assert find_duplicates(items[0], items) is None

    def test_single_item_no_duplicate(self):
        items = [
            {"cpt_code": "71046", "date_of_service": "2026-01-10", "quantity": 1,
             "charged_amount": 850.00, "description": "Chest X-Ray"},
        ]
        assert find_duplicates(items[0], items) is None

    def test_triple_duplicate(self):
        item = {"cpt_code": "71046", "date_of_service": "2026-01-10",
                "quantity": 1, "charged_amount": 850.00, "description": "X-Ray"}
        items = [item, {**item}, {**item}]
        # Only the first should report
        result = find_duplicates(items[0], items)
        assert result is not None
        assert "3 times" in result["message"]
