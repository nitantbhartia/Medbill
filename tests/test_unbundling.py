"""Tests for validators.unbundling — NCCI edit violation detection."""

from validators.unbundling import check_unbundling, _check_ncci_modifier


class TestCheckUnbundling:
    def test_bmp_cmp_flagged(self):
        items = [
            {"cpt_code": "80048", "description": "Basic metabolic panel",
             "charged_amount": 250.00},
            {"cpt_code": "80053", "description": "Comprehensive metabolic panel",
             "charged_amount": 350.00},
        ]
        result = check_unbundling(items[0], items)
        assert result is not None
        assert result["type"] == "unbundling"
        assert result["bundled_code"] == "80053"
        assert result["potential_savings"] > 0

    def test_only_first_code_reports(self):
        items = [
            {"cpt_code": "80048", "description": "BMP", "charged_amount": 250.00},
            {"cpt_code": "80053", "description": "CMP", "charged_amount": 350.00},
        ]
        # First component code should report
        assert check_unbundling(items[0], items) is not None
        # Second should not (avoids double-counting)
        assert check_unbundling(items[1], items) is None

    def test_cbc_pair_flagged(self):
        items = [
            {"cpt_code": "85025", "description": "CBC with diff", "charged_amount": 100.00},
            {"cpt_code": "85027", "description": "CBC without diff", "charged_amount": 80.00},
        ]
        result = check_unbundling(items[0], items)
        assert result is not None
        assert result["bundled_code"] == "85025"

    def test_er_multiple_levels_flagged(self):
        items = [
            {"cpt_code": "99283", "description": "ER level 3", "charged_amount": 500.00},
            {"cpt_code": "99285", "description": "ER level 5", "charged_amount": 1200.00},
        ]
        result = check_unbundling(items[0], items)
        assert result is not None
        assert result["bundled_code"] == "highest_only"

    def test_ekg_tracing_and_full_flagged(self):
        items = [
            {"cpt_code": "93000", "description": "ECG full", "charged_amount": 200.00},
            {"cpt_code": "93005", "description": "ECG tracing", "charged_amount": 100.00},
        ]
        result = check_unbundling(items[0], items)
        assert result is not None

    def test_unrelated_codes_not_flagged(self):
        items = [
            {"cpt_code": "99283", "description": "ER visit", "charged_amount": 500.00},
            {"cpt_code": "71046", "description": "Chest X-Ray", "charged_amount": 850.00},
        ]
        assert check_unbundling(items[0], items) is None
        assert check_unbundling(items[1], items) is None

    def test_single_item_not_flagged(self):
        items = [
            {"cpt_code": "80048", "description": "BMP", "charged_amount": 250.00},
        ]
        assert check_unbundling(items[0], items) is None

    def test_no_cpt_returns_none(self):
        items = [{"description": "test", "charged_amount": 100}]
        assert check_unbundling(items[0], items) is None


class TestNcciModifier:
    def test_known_pair_returns_indicator(self):
        # seeded: 80053 -> 80048 with modifier_indicator "0"
        ind = _check_ncci_modifier("80053", "80048")
        assert ind == "0"

    def test_reversed_pair_also_found(self):
        ind = _check_ncci_modifier("80048", "80053")
        assert ind == "0"

    def test_unknown_pair_returns_none(self):
        ind = _check_ncci_modifier("99999", "88888")
        assert ind is None

    def test_modifier_indicator_affects_severity(self):
        """Pairs with modifier_indicator '0' should be medium severity."""
        items = [
            {"cpt_code": "80048", "description": "BMP", "charged_amount": 250.00},
            {"cpt_code": "80053", "description": "CMP", "charged_amount": 350.00},
        ]
        result = check_unbundling(items[0], items)
        assert result is not None
        # Our seeded data has modifier_indicator "0" for this pair
        assert result["severity"] == "medium"
