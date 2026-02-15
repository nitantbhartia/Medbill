"""Tests for regional procedure benchmarks."""

from validators.benchmarks import check_benchmark, get_benchmark, _get_region
from db import get_db


class TestGetRegion:
    def test_southeast_zip(self):
        assert _get_region("33021") == "southeast"

    def test_northeast_zip(self):
        assert _get_region("10001") == "northeast"

    def test_midwest_zip(self):
        assert _get_region("60601") == "midwest"

    def test_west_zip(self):
        assert _get_region("90210") == "west"

    def test_empty_zip_returns_national(self):
        assert _get_region("") == "national"

    def test_none_zip_returns_national(self):
        assert _get_region(None) == "national"


class TestGetBenchmark:
    def test_national_benchmark_exists(self):
        result = get_benchmark("99285")
        assert result is not None
        assert result["region"] == "national"
        assert result["median_charged"] > 0

    def test_regional_preferred_over_national(self):
        # zip 33021 = southeast, and we have southeast data for 99285
        result = get_benchmark("99285", "33021")
        assert result is not None
        assert result["region"] == "southeast"

    def test_falls_back_to_national(self):
        # 80053 only has national benchmarks, not northeast
        result = get_benchmark("80053", "10001")
        assert result is not None
        assert result["region"] == "national"

    def test_unknown_cpt_returns_none(self):
        assert get_benchmark("ZZZZZ") is None

    def test_benchmark_has_required_fields(self):
        result = get_benchmark("71046")
        assert result is not None
        for field in ("avg_charged", "median_charged", "p25_charged", "p75_charged",
                      "sample_size", "region"):
            assert field in result


class TestCheckBenchmark:
    def test_high_charge_flagged(self):
        item = {
            "cpt_code": "99285",
            "description": "ED visit level 5",
            "charged_amount": 8000.00,
        }
        result = check_benchmark(item)
        assert result is not None
        assert result["type"] == "benchmark_outlier"
        assert result["potential_savings"] > 0
        assert "75th percentile" in result["message"] or "highest" in result["message"]

    def test_reasonable_charge_not_flagged(self):
        # national median for 99285 is $2500, p75 is $3600
        item = {
            "cpt_code": "99285",
            "description": "ED visit level 5",
            "charged_amount": 2000.00,
        }
        result = check_benchmark(item)
        assert result is None

    def test_no_cpt_returns_none(self):
        item = {"description": "Something", "charged_amount": 5000.00}
        result = check_benchmark(item)
        assert result is None

    def test_no_charged_amount_returns_none(self):
        item = {"cpt_code": "99285", "description": "ED visit"}
        result = check_benchmark(item)
        assert result is None

    def test_unknown_cpt_returns_none(self):
        item = {"cpt_code": "ZZZZZ", "description": "Unknown", "charged_amount": 5000.00}
        result = check_benchmark(item)
        assert result is None

    def test_regional_benchmark_used(self):
        item = {
            "cpt_code": "99285",
            "description": "ED visit level 5",
            "charged_amount": 8000.00,
        }
        result = check_benchmark(item, "33021")
        assert result is not None
        assert result["region"] == "southeast"

    def test_severity_low_for_moderate_outlier(self):
        # Just above p75 ($3600 national) but not 1.5x p75
        item = {
            "cpt_code": "99285",
            "description": "ED visit level 5",
            "charged_amount": 4000.00,
        }
        result = check_benchmark(item)
        assert result is not None
        assert result["severity"] == "low"

    def test_severity_medium_for_extreme_outlier(self):
        # Well above 1.5x p75
        item = {
            "cpt_code": "99285",
            "description": "ED visit level 5",
            "charged_amount": 10000.00,
        }
        result = check_benchmark(item)
        assert result is not None
        assert result["severity"] == "medium"

    def test_message_includes_sample_size(self):
        item = {
            "cpt_code": "71046",
            "description": "Chest X-ray",
            "charged_amount": 1500.00,
        }
        result = check_benchmark(item)
        assert result is not None
        assert "bills" in result["message"]
