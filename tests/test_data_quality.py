"""Tests for nightly data quality helpers."""

from __future__ import annotations

from data_quality import compare_coverage, latest_quality_run, run_consistency_checks, save_quality_run
from db import get_db


def test_compare_coverage_flags_regression_over_threshold():
    previous = [
        {"cpt_code": "99285", "radius_miles": 75, "coverage_ratio": 0.70},
        {"cpt_code": "70551", "radius_miles": 75, "coverage_ratio": 0.50},
    ]
    current = [
        {"cpt_code": "99285", "radius_miles": 75, "coverage_ratio": 0.55},
        {"cpt_code": "70551", "radius_miles": 75, "coverage_ratio": 0.45},
    ]
    out = compare_coverage(current, previous, max_drop_ratio=0.10)
    assert len(out) == 1
    assert out[0]["cpt_code"] == "99285"


def test_run_consistency_checks_detects_invalid_values():
    with get_db() as db:
        db.execute(
            """
            INSERT INTO procedure_prices (
                facility_id, cpt_code, gross_charge, markup_vs_medicare, data_year, facility_type
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            ("bad-facility", "99999", -1.0, 999.0, 2020, "hospital"),
        )
    out = run_consistency_checks()
    checks = out["checks"]
    assert checks["invalid_gross_prices"] >= 1
    assert checks["invalid_markups"] >= 1
    assert checks["stale_pricing_rows"] >= 1
    assert out["all_passed"] is False


def test_save_and_load_latest_quality_run_round_trip():
    run_id = save_quality_run(
        status="PASS",
        coverage=[{"cpt_code": "99285", "radius_miles": 75, "coverage_ratio": 0.9}],
        checks={"consistency": {"checks": {}, "all_passed": True}, "regressions": []},
        notes="unit test",
    )
    assert run_id > 0
    row = latest_quality_run()
    assert row is not None
    assert row["id"] == run_id
    assert row["status"] == "PASS"
    assert row["notes"] == "unit test"
