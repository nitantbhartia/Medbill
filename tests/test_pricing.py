"""Tests for validators.pricing — Medicare rate lookup and price markup checks."""

from validators.pricing import get_medicare_rate, check_pricing, validate_geo_match, get_medicare_locality


class TestGetMedicareRate:
    def test_known_cpt_returns_rate(self):
        rate = get_medicare_rate("99285")
        assert rate is not None
        assert rate == 227.00

    def test_unknown_cpt_returns_none(self):
        rate = get_medicare_rate("ZZZZZ")
        assert rate is None

    def test_date_of_service_year_matching(self):
        # Our seed data is for 2026 — requesting 2026 should work
        rate = get_medicare_rate("99283", "0000000", "2026-06-15")
        assert rate is not None
        assert rate == 98.00

    def test_fallback_when_year_missing(self):
        # Requesting 2025 should fall back to 2026 data
        rate = get_medicare_rate("99283", "0000000", "2025-06-15")
        assert rate is not None
        assert rate == 98.00

    def test_bad_date_format_gracefully_handled(self):
        rate = get_medicare_rate("99283", "0000000", "not-a-date")
        assert rate is not None  # falls back to non-date-filtered lookup

    def test_locality_fallback(self):
        # We only seeded "0000000" locality, but a different locality should fall back
        rate = get_medicare_rate("99285", "9999999")
        assert rate is not None
        assert rate == 227.00


class TestCheckPricing:
    def test_high_markup_flagged(self):
        item = {
            "cpt_code": "71046",
            "description": "Chest X-Ray",
            "charged_amount": 850.00,
            "date_of_service": "2026-01-10",
        }
        result = check_pricing(item, "0000000")
        assert result is not None
        assert result["type"] == "price_markup"
        assert result["severity"] == "high"
        assert result["markup_multiple"] > 5
        assert result["potential_savings"] > 0

    def test_moderate_markup_flagged(self):
        # 98 * 3.5 = 343 — between 3x and 5x for 99283
        item = {
            "cpt_code": "99283",
            "description": "ER visit level 3",
            "charged_amount": 343.00,
        }
        result = check_pricing(item, "0000000")
        assert result is not None
        assert result["severity"] == "medium"

    def test_reasonable_price_not_flagged(self):
        item = {
            "cpt_code": "99283",
            "description": "ER visit level 3",
            "charged_amount": 200.00,  # ~2x Medicare — under threshold
        }
        result = check_pricing(item, "0000000")
        assert result is None

    def test_missing_cpt_returns_none(self):
        result = check_pricing({"description": "test", "charged_amount": 100}, "0000000")
        assert result is None

    def test_missing_amount_returns_none(self):
        result = check_pricing({"cpt_code": "99283", "description": "test"}, "0000000")
        assert result is None

    def test_unknown_cpt_returns_none(self):
        item = {"cpt_code": "ZZZZZ", "description": "test", "charged_amount": 5000}
        result = check_pricing(item, "0000000")
        assert result is None


class TestValidateGeoMatch:
    def test_matching_zips_no_warning(self):
        assert validate_geo_match("33021", "3501 Johnson St, Hollywood, FL 33021") is None

    def test_same_prefix_no_warning(self):
        assert validate_geo_match("33022", "3501 Johnson St, Hollywood, FL 33021") is None

    def test_different_area_warns(self):
        warning = validate_geo_match("90210", "3501 Johnson St, Hollywood, FL 33021")
        assert warning is not None
        assert "different areas" in warning

    def test_no_zip_in_address_no_warning(self):
        assert validate_geo_match("33021", "Some Hospital, FL") is None

    def test_empty_inputs_no_warning(self):
        assert validate_geo_match("", "123 St, FL 33021") is None
        assert validate_geo_match("33021", None) is None
        assert validate_geo_match("33021", "") is None


class TestGetMedicareLocality:
    def test_default_locality(self):
        # No users in db match, should return default
        locality = get_medicare_locality("99999")
        assert locality == "0000000"
