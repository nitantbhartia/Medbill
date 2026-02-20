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
from hospital_etl import auto_map_columns, first, get_medicare_rate_for_facility, load_hcahps, normalize_price_rows, refresh_facility_transparency, upsert_facility_procedure_price, upsert_hospital_price  # noqa: E402
from hospital_seo import (  # noqa: E402
    clear_comparison_cache,
    get_hospital_profile,
    recompute_benchmarks,
    recompute_billing_metrics,
    recompute_facility_billing_metrics,
    upsert_hospital_row,
)
from main import _build_home_procedure_cards, _build_home_sample_facilities  # noqa: E402
from procedure_pages import get_procedure_profile  # noqa: E402


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


def test_normalize_price_rows_extracts_modifier_from_code_suffix():
    rows = [{"cpt_code": "70553-26", "description": "MRI pro fee", "gross_charge": "900"}]
    norm = normalize_price_rows(rows)
    assert len(norm) == 1
    assert norm[0]["cpt_code"] == "70553"
    assert norm[0]["cpt_modifier"] == "26"


def test_metrics_compute_grade_and_benchmarks():
    _db._connection = None
    _db.init_db()

    with get_db() as conn:
        # Insert latest medicare reference for CPTs used.
        for cpt, rate in [
            ("99285", 500.0),
            ("99284", 500.0),
            ("99283", 500.0),
            ("99282", 500.0),
            ("99281", 500.0),
            ("99291", 500.0),
            ("99292", 500.0),
            ("93000", 500.0),
            ("80053", 500.0),
            ("74177", 500.0),
        ]:
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

    # >=10 rows to get non-N/A grade
    for cpt in ["99285", "99284", "99283", "99282", "99281", "99291", "99292", "93000", "80053", "74177"]:
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


def test_recompute_clears_stale_markup_for_na_grade():
    _db._connection = None
    _db.init_db()

    upsert_hospital_row(
        {
            "facility_id": "70001",
            "name": "Stale Markup Hospital",
            "city": "Austin",
            "state": "TX",
            "slug": "stale-markup-hospital-austin",
        }
    )

    with get_db() as conn:
        # <10 comparable rows means final grade must be N/A.
        for i, markup in enumerate([220.0, 240.0, 260.0], start=1):
            conn.execute(
                """
                INSERT INTO hospital_prices (
                    facility_id, cpt_code, description, gross_charge, cash_price,
                    medicare_rate, markup_vs_medicare, data_year
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                ("070001", f"99{i:03d}", "Synthetic", 1000.0, 800.0, 5.0, markup, 2026),
            )
        # Simulate stale pre-existing metric that should be wiped.
        conn.execute(
            """
            INSERT INTO billing_metrics (
                facility_id, avg_markup_vs_medicare, median_markup_vs_medicare,
                max_markup_vs_medicare, procedures_compared, billing_grade
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            ("070001", 240.0, 240.0, 260.0, 3, "C"),
        )
        conn.execute(
            """
            INSERT INTO facility_billing_metrics (
                facility_id, facility_type, avg_markup, median_markup, max_markup,
                procedures_compared, billing_grade, benchmark_type
            ) VALUES (?, 'hospital', ?, ?, ?, ?, ?, ?)
            """,
            ("070001", 240.0, 240.0, 260.0, 3, "C", "opps"),
        )

    recompute_billing_metrics()
    recompute_facility_billing_metrics()

    with get_db() as conn:
        hospital_metric = conn.execute(
            """
            SELECT billing_grade, avg_markup_vs_medicare, median_markup_vs_medicare, max_markup_vs_medicare
            FROM billing_metrics
            WHERE facility_id = ?
            """,
            ("070001",),
        ).fetchone()
        facility_metric = conn.execute(
            """
            SELECT billing_grade, avg_markup, median_markup, max_markup
            FROM facility_billing_metrics
            WHERE facility_id = ?
            """,
            ("070001",),
        ).fetchone()

    assert hospital_metric["billing_grade"] == "N/A"
    assert hospital_metric["avg_markup_vs_medicare"] is None
    assert hospital_metric["median_markup_vs_medicare"] is None
    assert hospital_metric["max_markup_vs_medicare"] is None
    assert facility_metric["billing_grade"] == "N/A"
    assert facility_metric["avg_markup"] is None
    assert facility_metric["median_markup"] is None
    assert facility_metric["max_markup"] is None


def test_recompute_billing_metrics_trims_outlier_markups():
    _db._connection = None
    _db.init_db()
    upsert_hospital_row(
        {
            "facility_id": "74001",
            "name": "Outlier General",
            "city": "Dallas",
            "state": "TX",
            "slug": "outlier-general-dallas",
        }
    )
    with get_db() as conn:
        base_markups = [2.2, 2.3, 2.4, 2.5, 2.1, 2.6, 2.7, 2.4, 2.5, 2.3]
        for i, markup in enumerate(base_markups, start=1):
            conn.execute(
                """
                INSERT INTO hospital_prices (
                    facility_id, cpt_code, description, gross_charge, cash_price,
                    medicare_rate, markup_vs_medicare, data_year
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                ("074001", f"84{i:03d}", "Synthetic", markup * 100.0, markup * 80.0, 100.0, markup, 2026),
            )
        # Extreme but in-range value that should be dropped by IQR trimming.
        conn.execute(
            """
            INSERT INTO hospital_prices (
                facility_id, cpt_code, description, gross_charge, cash_price,
                medicare_rate, markup_vs_medicare, data_year
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("074001", "84999", "Synthetic Outlier", 12000.0, 9000.0, 100.0, 120.0, 2026),
        )

    recompute_billing_metrics()

    with get_db() as conn:
        metric = conn.execute(
            "SELECT avg_markup_vs_medicare, max_markup_vs_medicare, procedures_compared, billing_grade FROM billing_metrics WHERE facility_id = ?",
            ("074001",),
        ).fetchone()
    assert metric is not None
    assert metric["procedures_compared"] == 10
    assert metric["avg_markup_vs_medicare"] < 3.0
    assert metric["max_markup_vs_medicare"] < 3.0
    assert metric["billing_grade"] in {"A", "B"}


def test_home_sample_facilities_excludes_na_and_extreme_markup():
    _db._connection = None
    _db.init_db()

    upsert_hospital_row(
        {"facility_id": "71001", "name": "Valid Hospital A", "city": "Miami", "state": "FL", "slug": "valid-hospital-a"}
    )
    upsert_hospital_row(
        {"facility_id": "71002", "name": "Valid Hospital B", "city": "Miami", "state": "FL", "slug": "valid-hospital-b"}
    )
    upsert_hospital_row(
        {"facility_id": "71003", "name": "Bad Stale Hospital", "city": "Miami", "state": "FL", "slug": "bad-stale-hospital"}
    )

    with get_db() as conn:
        conn.execute(
            "INSERT OR REPLACE INTO billing_metrics (facility_id, avg_markup_vs_medicare, median_markup_vs_medicare, max_markup_vs_medicare, procedures_compared, billing_grade) VALUES (?, ?, ?, ?, ?, ?)",
            ("071001", 2.4, 2.3, 2.8, 24, "A"),
        )
        conn.execute(
            "INSERT OR REPLACE INTO billing_metrics (facility_id, avg_markup_vs_medicare, median_markup_vs_medicare, max_markup_vs_medicare, procedures_compared, billing_grade) VALUES (?, ?, ?, ?, ?, ?)",
            ("071002", 9.6, 9.2, 12.0, 22, "F"),
        )
        conn.execute(
            "INSERT OR REPLACE INTO billing_metrics (facility_id, avg_markup_vs_medicare, median_markup_vs_medicare, max_markup_vs_medicare, procedures_compared, billing_grade) VALUES (?, ?, ?, ?, ?, ?)",
            ("071003", 258.6, 250.0, 300.0, 3, "N/A"),
        )
        conn.execute(
            "INSERT OR REPLACE INTO facility_billing_metrics (facility_id, facility_type, avg_markup, median_markup, max_markup, procedures_compared, billing_grade, benchmark_type) VALUES (?, 'hospital', ?, ?, ?, ?, ?, ?)",
            ("071001", 2.4, 2.3, 2.8, 24, "A", "opps"),
        )
        conn.execute(
            "INSERT OR REPLACE INTO facility_billing_metrics (facility_id, facility_type, avg_markup, median_markup, max_markup, procedures_compared, billing_grade, benchmark_type) VALUES (?, 'hospital', ?, ?, ?, ?, ?, ?)",
            ("071002", 9.6, 9.2, 12.0, 22, "F", "opps"),
        )
        # Should never be shown once filters are applied.
        conn.execute(
            "INSERT OR REPLACE INTO facility_billing_metrics (facility_id, facility_type, avg_markup, median_markup, max_markup, procedures_compared, billing_grade, benchmark_type) VALUES (?, 'hospital', ?, ?, ?, ?, ?, ?)",
            ("071003", 258.6, 250.0, 300.0, 3, "N/A", "opps"),
        )

    cards = _build_home_sample_facilities(10)
    assert cards
    assert all(c.get("billing_grade") in {"A", "B", "C", "D", "F"} for c in cards)
    assert all(c.get("avg_markup") is not None and 0.5 <= float(c.get("avg_markup")) <= 150.0 for c in cards)
    assert all(int(c.get("procedures_compared") or 0) >= 20 for c in cards)


def test_home_procedure_cards_fallback_to_hospital_prices_when_procedure_prices_missing():
    _db._connection = None
    _db.init_db()
    upsert_hospital_row(
        {"facility_id": "75001", "name": "Fallback Hospital", "city": "Austin", "state": "TX", "slug": "fallback-hospital-austin"}
    )
    with get_db() as conn:
        conn.execute(
            """
            INSERT INTO hospital_prices (
                facility_id, cpt_code, description, gross_charge, cash_price,
                medicare_rate, markup_vs_medicare, data_year, facility_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("075001", "70551", "MRI Brain W/O Contrast", 2400.0, 1200.0, 300.0, 8.0, 2026, "hospital"),
        )
        # Ensure no procedure_prices rows exist for this CPT.
        conn.execute("DELETE FROM procedure_prices WHERE cpt_code = '70551'")

    cards = _build_home_procedure_cards()
    mri = next((c for c in cards if c.get("cpt_code") == "70551"), None)
    assert mri is not None
    assert mri.get("hospital_avg") is not None
    assert mri.get("hospital_markup") is not None


def test_home_procedure_cards_derive_markup_from_medicare_rate_when_missing():
    _db._connection = None
    _db.init_db()
    upsert_hospital_row(
        {"facility_id": "76001", "name": "Derived Markup Hospital", "city": "Austin", "state": "TX", "slug": "derived-markup-hospital-austin"}
    )
    with get_db() as conn:
        conn.execute(
            "INSERT INTO medicare_rates (cpt_code, locality, facility_rate, non_facility_rate, effective_year) VALUES (?, ?, ?, ?, ?)",
            ("99284", "0000000", 250.0, 250.0, 2026),
        )
        conn.execute(
            """
            INSERT INTO hospital_prices (
                facility_id, cpt_code, description, gross_charge, cash_price,
                medicare_rate, markup_vs_medicare, data_year, facility_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("076001", "99284", "Level 4 ER Visit", 1250.0, 900.0, None, None, 2026, "hospital"),
        )
        conn.execute("DELETE FROM procedure_prices WHERE cpt_code = '99284'")

    cards = _build_home_procedure_cards()
    er = next((c for c in cards if c.get("cpt_code") == "99284"), None)
    assert er is not None
    assert er.get("hospital_avg") == 1250.0
    assert er.get("hospital_markup") is not None
    assert float(er.get("hospital_markup")) >= 4.9


def test_home_procedure_cards_match_procedure_profile_hospital_metrics():
    _db._connection = None
    _db.init_db()
    upsert_hospital_row(
        {"facility_id": "77001", "name": "Card Consistency Hospital A", "city": "Austin", "state": "TX", "slug": "card-consistency-austin-a"}
    )
    upsert_hospital_row(
        {"facility_id": "77002", "name": "Card Consistency Hospital B", "city": "Austin", "state": "TX", "slug": "card-consistency-austin-b"}
    )
    with get_db() as conn:
        conn.execute(
            "INSERT INTO hospital_prices (facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year, facility_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ("077001", "70551", "MRI BRAIN W/O CONTRAST", 2000.0, 200.0, 10.0, 2026, "hospital"),
        )
        conn.execute(
            "INSERT INTO hospital_prices (facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year, facility_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ("077002", "70551", "MRI BRAIN W/O CONTRAST", 3000.0, 200.0, 15.0, 2026, "hospital"),
        )

    cards = _build_home_procedure_cards()
    mri_card = next((c for c in cards if c.get("cpt_code") == "70551"), None)
    assert mri_card is not None
    profile = get_procedure_profile("70551")
    assert profile is not None
    hospital_row = next((r for r in profile.get("ranges_by_type", []) if r.get("facility_type") == "hospital"), None)
    assert hospital_row is not None
    assert round(float(mri_card["hospital_avg"]), 2) == round(float(hospital_row["avg_charge"]), 2)
    assert round(float(mri_card["hospital_markup"]), 2) == round(float(hospital_row["avg_markup"]), 2)


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


def test_upsert_facility_procedure_price_asc_uses_asc_rate():
    _db._connection = None
    _db.init_db()

    with get_db() as conn:
        conn.execute(
            """
            INSERT INTO facilities (facility_id, name, city, state, state_slug, city_slug, slug, facility_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'asc')
            """,
            ("asc100", "ASC One", "Miami", "FL", "fl", "miami", "asc-one-miami-surgery-center"),
        )
        conn.execute(
            """
            INSERT INTO asc_medicare_rates (cpt_code, description, medicare_asc_rate, effective_year, is_covered_asc_procedure)
            VALUES ('45378', 'COLONOSCOPY', 164.0, 2026, 1)
            """
        )

    upsert_facility_procedure_price(
        "asc100",
        {"cpt_code": "45378", "description": "COLONOSCOPY", "gross_charge": 820.0},
        "asc",
        data_year=2026,
    )

    with get_db() as conn:
        row = conn.execute(
            """
            SELECT facility_type, medicare_benchmark_type, medicare_benchmark_rate, markup_vs_medicare
            FROM procedure_prices
            WHERE facility_id = 'asc100' AND cpt_code = '45378' AND data_year = 2026
            """
        ).fetchone()
    assert row is not None
    assert row["facility_type"] == "asc"
    assert row["medicare_benchmark_type"] == "asc"
    assert round(row["medicare_benchmark_rate"], 2) == 164.00
    assert round(row["markup_vs_medicare"], 1) == 5.0


def test_upsert_facility_procedure_price_imaging_modifier_uses_pfs():
    _db._connection = None
    _db.init_db()

    with get_db() as conn:
        conn.execute(
            """
            INSERT INTO facilities (facility_id, name, city, state, state_slug, city_slug, zip, slug, facility_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'imaging_center')
            """,
            ("img100", "Imaging One", "Miami", "FL", "fl", "miami", "33101", "imaging-one-miami-imaging-center"),
        )
        conn.execute(
            "INSERT INTO zip_locality_map (zip_prefix, locality, state, region) VALUES ('331', 'L001', 'FL', 'South')"
        )
        conn.execute(
            """
            INSERT INTO medicare_rates (cpt_code, locality, facility_rate, non_facility_rate, effective_year)
            VALUES ('70553', 'L001', 210.0, 220.0, 2026)
            """
        )
        conn.execute(
            """
            INSERT INTO hospital_opps_rates (cpt_code, apc, description, national_payment_rate, effective_year)
            VALUES ('70553', '5571', 'MRI', 317.0, 2026)
            """
        )

    upsert_facility_procedure_price(
        "img100",
        {"cpt_code": "70553", "cpt_modifier": "26", "description": "MRI brain", "gross_charge": 840.0},
        "imaging_center",
        data_year=2026,
    )

    with get_db() as conn:
        row = conn.execute(
            """
            SELECT medicare_benchmark_type, medicare_benchmark_rate
            FROM procedure_prices
            WHERE facility_id = 'img100' AND cpt_code = '70553' AND data_year = 2026
            """
        ).fetchone()
    assert row is not None
    assert row["medicare_benchmark_type"] == "pfs"
    assert round(row["medicare_benchmark_rate"], 2) == 210.00


def test_refresh_facility_transparency_tracks_non_hospital_parse_results():
    _db._connection = None
    _db.init_db()
    tmp_dir = tempfile.mkdtemp(prefix="asc-transparency-")
    csv_path = os.path.join(tmp_dir, "asc-two-miami-surgery-center.csv")
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write("cpt_code,description,gross_charge,cash_price\n45378,COLONOSCOPY,900,600\n")

    try:
        with get_db() as conn:
            conn.execute(
                """
                INSERT INTO facilities (facility_id, name, city, state, state_slug, city_slug, slug, facility_type)
                VALUES ('asc200', 'ASC Two', 'Miami', 'FL', 'fl', 'miami', 'asc-two-miami-surgery-center', 'asc')
                """
            )
            conn.execute(
                """
                INSERT INTO asc_medicare_rates (cpt_code, description, medicare_asc_rate, effective_year, is_covered_asc_procedure)
                VALUES ('45378', 'COLONOSCOPY', 180.0, 2026, 1)
                """
            )

        summary = refresh_facility_transparency(
            selected=[{"facility_id": "asc200", "facility_type": "asc", "slug": "asc-two-miami-surgery-center"}],
            files_dir=os.path.dirname(csv_path),
            data_year=2026,
        )
        assert summary["parsed"] == 1

        with get_db() as conn:
                parse_row = conn.execute(
                    "SELECT facility_type, parse_status FROM transparency_parse_results WHERE facility_id = 'asc200'"
                ).fetchone()
                price_row = conn.execute(
                    "SELECT facility_type, medicare_benchmark_type FROM procedure_prices WHERE facility_id = 'asc200' AND cpt_code = '45378'"
                ).fetchone()
        assert parse_row is not None
        assert parse_row["facility_type"] == "asc"
        assert parse_row["parse_status"] == "parsed"
        assert price_row is not None
        assert price_row["facility_type"] == "asc"
        assert price_row["medicare_benchmark_type"] == "asc"
    finally:
        if os.path.exists(csv_path):
            os.unlink(csv_path)
        os.rmdir(tmp_dir)
