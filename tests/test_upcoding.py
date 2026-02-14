"""Tests for validators.upcoding — ER visit level upcoding detection."""

from validators.upcoding import check_upcoding, ER_VISIT_LEVELS


class TestCheckUpcoding:
    def test_level_5_flagged(self):
        item = {"cpt_code": "99285", "description": "ER level 5", "charged_amount": 4500.00}
        result = check_upcoding(item)
        assert result is not None
        assert result["type"] == "upcoding"
        assert result["severity"] == "medium"
        assert result["billed_level"] == 5
        assert result["likely_level"] == 4
        assert result["correct_code"] == "99284"
        assert result["potential_savings"] > 0

    def test_level_4_flagged(self):
        item = {"cpt_code": "99284", "description": "ER level 4", "charged_amount": 3000.00}
        result = check_upcoding(item)
        assert result is not None
        assert result["billed_level"] == 4
        assert result["likely_level"] == 3
        assert result["correct_code"] == "99283"

    def test_level_3_not_flagged(self):
        item = {"cpt_code": "99283", "description": "ER level 3", "charged_amount": 500.00}
        assert check_upcoding(item) is None

    def test_level_2_not_flagged(self):
        item = {"cpt_code": "99282", "description": "ER level 2", "charged_amount": 300.00}
        assert check_upcoding(item) is None

    def test_level_1_not_flagged(self):
        item = {"cpt_code": "99281", "description": "ER level 1", "charged_amount": 100.00}
        assert check_upcoding(item) is None

    def test_non_er_code_not_flagged(self):
        item = {"cpt_code": "71046", "description": "Chest X-Ray", "charged_amount": 850.00}
        assert check_upcoding(item) is None

    def test_no_cpt_returns_none(self):
        item = {"description": "test", "charged_amount": 100}
        assert check_upcoding(item) is None

    def test_savings_is_positive(self):
        item = {"cpt_code": "99285", "description": "ER level 5", "charged_amount": 4500.00}
        result = check_upcoding(item)
        assert result["potential_savings"] > 0
        assert result["correct_rate"] > 0

    def test_er_visit_levels_data_complete(self):
        assert len(ER_VISIT_LEVELS) == 5
        for code in ["99281", "99282", "99283", "99284", "99285"]:
            assert code in ER_VISIT_LEVELS
            assert "level" in ER_VISIT_LEVELS[code]
            assert "description" in ER_VISIT_LEVELS[code]
