"""Tests for data_freshness — freshness monitoring and warnings."""

from datetime import date

from data_freshness import get_data_freshness, get_data_freshness_warnings
from db import get_db


class TestGetDataFreshness:
    def test_seeded_db_has_fresh_rates(self):
        result = get_data_freshness()
        assert "medicare_pfs" in result
        assert result["medicare_pfs"]["latest_year"] == 2026
        assert result["medicare_pfs"]["fresh"] is True
        assert result["medicare_pfs"]["warning"] is None

    def test_ncci_edits_status(self):
        result = get_data_freshness()
        assert "ncci_edits" in result
        assert result["ncci_edits"]["latest_date"] is not None

    def test_hospital_profiles_empty(self):
        result = get_data_freshness()
        assert result["hospital_profiles"]["count"] == 0
        assert result["hospital_profiles"]["fresh"] is False

    def test_row_counts_populated(self):
        result = get_data_freshness()
        assert result["medicare_row_count"] > 0
        assert result["ncci_row_count"] > 0


class TestGetDataFreshnessWarnings:
    def test_current_year_no_rate_warning(self):
        warnings = get_data_freshness_warnings("2026-06-15")
        rate_warnings = [w for w in warnings if "Medicare rates" in w]
        assert len(rate_warnings) == 0

    def test_future_year_warns(self):
        warnings = get_data_freshness_warnings("2027-06-15")
        assert any("2027" in w for w in warnings)

    def test_past_year_warns(self):
        warnings = get_data_freshness_warnings("2025-06-15")
        assert any("2025" in w for w in warnings)

    def test_string_date_accepted(self):
        warnings = get_data_freshness_warnings("2026-06-15")
        assert isinstance(warnings, list)

    def test_date_object_accepted(self):
        warnings = get_data_freshness_warnings(date(2026, 6, 15))
        assert isinstance(warnings, list)

    def test_bad_date_string_warns(self):
        warnings = get_data_freshness_warnings("not-a-date")
        assert any("Could not parse" in w for w in warnings)

    def test_stale_ncci_edits_warning(self):
        # Make NCCI edits look stale
        with get_db() as db:
            db.execute("UPDATE ncci_edits SET effective_date = '2020-01-01'")

        warnings = get_data_freshness_warnings("2026-06-15")
        assert any("bundling rules" in w for w in warnings)
