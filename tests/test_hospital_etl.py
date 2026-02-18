"""Tests for hospital ETL parser and metric computation contracts."""

import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

import db as _db  # noqa: E402
from db import get_db  # noqa: E402
from hospital_etl import auto_map_columns, normalize_price_rows, upsert_hospital_price  # noqa: E402
from hospital_seo import recompute_benchmarks, recompute_billing_metrics, upsert_hospital_row  # noqa: E402


def test_auto_map_columns_detects_core_fields():
    cols = ["Procedure Code", "Service Description", "Gross Charge", "Discounted Cash", "Negotiated Rate"]
    mapped = auto_map_columns(cols)
    assert mapped["code"] == "Procedure Code"
    assert mapped["description"] == "Service Description"
    assert mapped["gross_charge"] == "Gross Charge"
    assert mapped["cash_price"] == "Discounted Cash"


def test_normalize_price_rows_keeps_valid_cpt():
    rows = [
        {"cpt_code": "99285", "description": "ER", "gross_charge": "2800", "cash_price": "1600"},
        {"cpt_code": "ABC", "description": "Bad", "gross_charge": "100"},
    ]
    norm = normalize_price_rows(rows)
    assert len(norm) == 1
    assert norm[0]["cpt_code"] == "99285"


def test_metrics_compute_grade_and_benchmarks():
    _db._connection = None
    _db.init_db()

    with get_db() as conn:
        # Insert latest medicare reference for CPTs used.
        for cpt, rate in [("99285", 227.0), ("99284", 157.0), ("99283", 98.0), ("99282", 52.0), ("99281", 27.0)]:
            conn.execute(
                "INSERT INTO medicare_rates (cpt_code, locality, facility_rate, non_facility_rate, effective_year) VALUES (?, ?, ?, ?, ?)",
                (cpt, "0000000", rate, rate, 2026),
            )

    upsert_hospital_row(
        {
            "facility_id": "10001",
            "name": "Memorial Regional Hospital",
            "city": "Hollywood",
            "state": "FL",
            "slug": "memorial-regional-hospital-hollywood",
        }
    )

    # >= 5 rows to get non-N/A grade
    for cpt in ["99285", "99284", "99283", "99282", "99281"]:
        upsert_hospital_price(
            "10001",
            {
                "cpt_code": cpt,
                "description": "ER visit",
                "gross_charge": 2800.0,
                "cash_price": 1500.0,
                "avg_negotiated_rate": 1400.0,
                "min_negotiated_rate": 1200.0,
                "max_negotiated_rate": 1700.0,
            },
            data_year=2026,
        )

    bench = recompute_benchmarks()
    metrics = recompute_billing_metrics()
    assert bench > 0
    assert metrics > 0

    with get_db() as conn:
        row = conn.execute("SELECT billing_grade, avg_markup_vs_medicare FROM billing_metrics WHERE facility_id = ?", ("010001",)).fetchone()
    assert row is not None
    assert row["billing_grade"] in ("A", "B", "C", "D", "F", "N/A")
    assert row["avg_markup_vs_medicare"] is not None
