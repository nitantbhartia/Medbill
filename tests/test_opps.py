"""Tests for OPPS rate lookup and integration with pricing validator."""

from validators.pricing import get_opps_rate, check_pricing, get_medicare_locality
from db import get_db


class TestGetOppsRate:
    def test_known_cpt_returns_rate(self):
        rate = get_opps_rate("99285")
        assert rate is not None
        assert rate == 773.00

    def test_year_match(self):
        rate = get_opps_rate("99285", "2026-01-10")
        assert rate == 773.00

    def test_unknown_cpt_returns_none(self):
        assert get_opps_rate("ZZZZZ") is None

    def test_chest_xray_opps(self):
        rate = get_opps_rate("71046")
        assert rate == 72.00

    def test_lab_opps(self):
        rate = get_opps_rate("80053")
        assert rate == 15.00

    def test_surgical_opps(self):
        rate = get_opps_rate("27447")
        assert rate == 12998.00


class TestCheckPricingWithOpps:
    def test_pricing_finding_includes_opps(self):
        item = {
            "cpt_code": "99285",
            "description": "ED visit level 5",
            "charged_amount": 4500.00,
            "date_of_service": "2026-01-10",
        }
        locality = get_medicare_locality("33021")
        result = check_pricing(item, locality)
        assert result is not None
        assert "opps_rate" in result
        assert result["opps_rate"] == 773.00
        assert "total_medicare" in result
        # PFS (227) + OPPS (773) = 1000
        assert result["total_medicare"] == 1000.00
        assert "hospital fee" in result["message"]

    def test_pricing_without_opps(self):
        # J0170 has no OPPS rate
        with get_db() as db:
            db.execute(
                "INSERT OR REPLACE INTO medicare_rates "
                "(cpt_code, description, locality, state, facility_rate, effective_year) "
                "VALUES ('J9999', 'Test drug', '0000000', NULL, 50.00, 2026)"
            )
        item = {
            "cpt_code": "J9999",
            "description": "Test drug",
            "charged_amount": 500.00,
        }
        result = check_pricing(item, "0000000")
        assert result is not None
        assert "opps_rate" not in result


class TestOppsSeeded:
    def test_all_seeded_opps_rates(self):
        with get_db() as db:
            count = db.execute("SELECT COUNT(*) as cnt FROM hospital_opps_rates").fetchone()
        assert count["cnt"] >= 17

    def test_opps_rate_structure(self):
        with get_db() as db:
            row = db.execute(
                "SELECT * FROM hospital_opps_rates WHERE cpt_code = '99283'"
            ).fetchone()
        assert row is not None
        assert row["apc"] == "5023"
        assert row["national_payment_rate"] == 297.00
        assert row["effective_year"] == 2026
