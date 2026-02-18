"""Tests for hospital ETL parser and metric computation contracts."""

import io
import os
import sys
import tempfile
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

import db as _db  # noqa: E402
from db import get_db  # noqa: E402
import hospital_etl  # noqa: E402
from hospital_etl import auto_map_columns, first, get_medicare_rate_for_facility, load_hcahps, normalize_price_rows, upsert_hospital_price  # noqa: E402
from hospital_seo import clear_comparison_cache, get_hospital_profile, recompute_benchmarks, recompute_billing_metrics, upsert_hospital_row  # noqa: E402


def test_auto_map_columns_detects_core_fields():
    cols = ["Procedure Code", "Service Description", "Gross Charge", "Discounted Cash", "Negotiated Rate"]
    mapped = auto_map_columns(cols)
    assert mapped["code"] == "Procedure Code"
    assert mapped["description"] == "Service Description"
    assert mapped["gross_charge"] == "Gross Charge"
    assert mapped["cash_price"] == "Discounted Cash"


def test_first_matches_case_insensitive_headers():
    row = {"HCPCS": "99285", "NON_FACILITY_RATE": "684.22"}
    assert first(row, ("cpt_code", "hcpcs")) == "99285"
    assert first(row, ("non_facility_rate", "Non Facility Rate")) == "684.22"


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


def test_refresh_top300_transparency_downloads_remote_file(monkeypatch):
    _db._connection = None
    _db.init_db()
    upsert_hospital_row(
        {
            "facility_id": "10001",
            "name": "Test Hospital",
            "city": "Miami",
            "state": "FL",
            "slug": "test-hospital-miami",
            "bed_count": 999,
        }
    )
    with get_db() as conn:
        conn.execute(
            "INSERT INTO medicare_rates (cpt_code, locality, facility_rate, non_facility_rate, effective_year) VALUES (?, ?, ?, ?, ?)",
            ("99285", "0000000", 280.0, 280.0, 2026),
        )
        conn.execute(
            "INSERT INTO transparency_files (facility_id, file_url, parse_status) VALUES (?, ?, 'pending')",
            ("010001", "https://example.org/prices.csv"),
        )

    class FakeResponse(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    def fake_urlopen(url, timeout=20):  # noqa: ARG001
        payload = b"cpt_code,description,gross_charge,cash_price\n99285,ER Visit,2800,1500\n"
        return FakeResponse(payload)

    monkeypatch.setattr(hospital_etl, "urlopen", fake_urlopen)
    monkeypatch.setattr(hospital_etl, "select_top_hospitals_by_beds", lambda limit=300: [{"facility_id": "010001"}])  # noqa: ARG005

    result = hospital_etl.refresh_top300_transparency(files_dir="", data_year=2026)
    assert result["parsed"] == 1
    with get_db() as conn:
        tf = conn.execute(
            "SELECT parse_status, file_format, procedures_extracted FROM transparency_files WHERE facility_id = ?",
            ("010001",),
        ).fetchone()
        pc = conn.execute("SELECT COUNT(*) AS n FROM hospital_prices WHERE facility_id = ?", ("010001",)).fetchone()
    assert tf["parse_status"] == "parsed"
    assert tf["file_format"] == "csv"
    assert tf["procedures_extracted"] >= 1
    assert pc["n"] >= 1


def test_refresh_top300_transparency_marks_download_failure(monkeypatch):
    _db._connection = None
    _db.init_db()
    upsert_hospital_row(
        {
            "facility_id": "10002",
            "name": "Fail Hospital",
            "city": "Tampa",
            "state": "FL",
            "slug": "fail-hospital-tampa",
            "bed_count": 998,
        }
    )
    with get_db() as conn:
        conn.execute(
            "INSERT INTO transparency_files (facility_id, file_url, parse_status) VALUES (?, ?, 'pending')",
            ("010002", "https://example.org/missing.csv"),
        )

    def fake_urlopen_fail(url, timeout=20):  # noqa: ARG001
        raise hospital_etl.URLError("boom")

    monkeypatch.setattr(hospital_etl, "urlopen", fake_urlopen_fail)
    monkeypatch.setattr(hospital_etl, "select_top_hospitals_by_beds", lambda limit=300: [{"facility_id": "010002"}])  # noqa: ARG005

    result = hospital_etl.refresh_top300_transparency(files_dir="", data_year=2026)
    assert result["failed"] == 1
    with get_db() as conn:
        tf = conn.execute(
            "SELECT parse_status, parse_notes FROM transparency_files WHERE facility_id = ?",
            ("010002",),
        ).fetchone()
    assert tf["parse_status"] == "failed"
    assert tf["parse_notes"] == "download_failed"


def test_profile_comparison_averages_stay_realistic_with_normal_seed():
    _db._connection = None
    _db.init_db()

    # Seed one target hospital + enough peers in-state and national.
    upsert_hospital_row(
        {"facility_id": "90001", "name": "Target", "city": "Miami", "state": "FL", "slug": "target-miami"}
    )
    with get_db() as conn:
        conn.execute(
            "INSERT INTO billing_metrics (facility_id, avg_markup_vs_medicare, procedures_compared, billing_grade) VALUES (?, ?, ?, ?)",
            ("090001", 6.5, 10, "D"),
        )

    for i in range(35):
        fid = f"91{i:03d}"
        state = "FL" if i < 26 else "GA"
        upsert_hospital_row(
            {"facility_id": fid, "name": f"Peer {i}", "city": "City", "state": state, "slug": f"peer-{i}"}
        )
        with get_db() as conn:
            conn.execute(
                "INSERT INTO billing_metrics (facility_id, avg_markup_vs_medicare, procedures_compared, billing_grade) VALUES (?, ?, ?, ?)",
                (fid.zfill(6), 3.5 + (i % 6) * 0.3, 10, "C"),
            )

    clear_comparison_cache()
    profile = get_hospital_profile("fl", "miami", "target-miami")
    assert profile is not None
    assert 2.0 < profile["comparison"]["state_avg_markup"] < 10.0
    # National display can be gated (<100 sample), so assert raw benchmark integrity.
    assert 2.0 < profile["comparison"]["national_avg_markup_raw"] < 10.0


def test_load_hcahps_handles_cms_coded_columns():
    _db._connection = None
    _db.init_db()
    upsert_hospital_row(
        {"facility_id": "92001", "name": "HCAHPS Test", "city": "Austin", "state": "TX", "slug": "hcahps-test-austin"}
    )

    csv_text = (
        "Facility ID,H_RECMND_DY_P,H_COMP_1_A_P,H_COMP_2_A_P,Survey Period\n"
        "92001,67,78,74,2025-Q4\n"
    )
    with tempfile.NamedTemporaryFile("w+", suffix=".csv", delete=False) as f:
        f.write(csv_text)
        path = f.name
    try:
        count = load_hcahps(path)
        assert count == 1
        with get_db() as conn:
            row = conn.execute(
                "SELECT recommend_yes, doctor_communication_top, nurse_communication_top FROM hcahps_scores WHERE facility_id = ?",
                ("092001",),
            ).fetchone()
        assert row is not None
        assert row["recommend_yes"] == 67
        assert row["doctor_communication_top"] == 78
        assert row["nurse_communication_top"] == 74
    finally:
        os.unlink(path)


def test_locality_aware_medicare_rate_lookup():
    _db._connection = None
    _db.init_db()
    upsert_hospital_row(
        {"facility_id": "93001", "name": "Locality Test", "city": "Miami", "state": "FL", "zip": "33101", "slug": "locality-test-miami"}
    )
    with get_db() as conn:
        conn.execute(
            "INSERT INTO zip_locality_map (zip_prefix, locality, state, region) VALUES (?, ?, ?, ?)",
            ("331", "L001", "FL", "South"),
        )
        conn.execute(
            "INSERT INTO medicare_rates (cpt_code, locality, facility_rate, non_facility_rate, effective_year) VALUES (?, ?, ?, ?, ?)",
            ("99285", "L001", 410.0, 390.0, 2026),
        )
        conn.execute(
            "INSERT INTO medicare_rates (cpt_code, locality, facility_rate, non_facility_rate, effective_year) VALUES (?, ?, ?, ?, ?)",
            ("99285", "0000000", 220.0, 210.0, 2026),
        )
    rate = get_medicare_rate_for_facility("93001", "99285")
    assert rate == 410.0
