"""Tests for hospital comparison tool (/compare/ and /compare/{a}/vs/{b}/)."""

import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import db as _db  # noqa: E402
from db import get_db  # noqa: E402
from hospital_seo import upsert_hospital_row  # noqa: E402
from main import app  # noqa: E402
from compare_pages import (  # noqa: E402
    get_comparison_data,
    get_hospital_for_compare,
    get_common_procedures,
    search_hospitals_for_compare,
)

_db.init_db()
client = TestClient(app)

_FID_A = "099001"
_FID_B = "099002"


def _seed():
    upsert_hospital_row({
        "facility_id": "99001",
        "name": "Test General Hospital",
        "address": "100 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip": "62701",
        "ownership": "Voluntary non-profit - Private",
        "hospital_type": "Acute Care Hospitals",
        "bed_count": 200,
        "cms_star_rating": 4,
        "slug": "test-general-hospital-springfield",
        "is_nonprofit": 1,
        "lat": 39.7817,
        "lon": -89.6501,
    })
    upsert_hospital_row({
        "facility_id": "99002",
        "name": "Test Specialty Center",
        "address": "200 Oak Ave",
        "city": "Springfield",
        "state": "IL",
        "zip": "62702",
        "ownership": "Proprietary",
        "hospital_type": "Acute Care Hospitals",
        "bed_count": 80,
        "cms_star_rating": 3,
        "slug": "test-specialty-center-springfield",
        "is_nonprofit": 0,
        "lat": 39.7900,
        "lon": -89.6400,
    })
    with get_db() as db:
        db.execute(
            "INSERT OR IGNORE INTO billing_metrics (facility_id, avg_markup_vs_medicare, billing_grade, procedures_compared, state_rank) VALUES (?, ?, ?, ?, ?)",
            (_FID_A, 2.5, "A", 15, 2),
        )
        db.execute(
            "INSERT OR IGNORE INTO billing_metrics (facility_id, avg_markup_vs_medicare, billing_grade, procedures_compared, state_rank) VALUES (?, ?, ?, ?, ?)",
            (_FID_B, 5.2, "D", 12, 45),
        )
        for fid, charge, markup in [(_FID_A, 4200.0, 2.1), (_FID_B, 9800.0, 4.9)]:
            db.execute(
                "INSERT OR IGNORE INTO hospital_prices (facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (fid, "27447", "TOTAL KNEE REPLACEMENT", charge, 2000.0, markup, 2025),
            )
        for fid, charge, markup in [(_FID_A, 3100.0, 1.8), (_FID_B, 7500.0, 4.4)]:
            db.execute(
                "INSERT OR IGNORE INTO hospital_prices (facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (fid, "70553", "MRI BRAIN W CONTRAST", charge, 1720.0, markup, 2025),
            )


# ---- Page route tests ----

def test_compare_index_renders():
    _seed()
    resp = client.get("/compare/")
    assert resp.status_code == 200
    assert "Hospital Comparison Tool" in resp.text


def test_compare_query_deeplink_redirects():
    _seed()
    resp = client.get(f"/compare/?facility-a={_FID_A}&facility-b={_FID_B}", follow_redirects=False)
    assert resp.status_code in (301, 302, 307)
    assert resp.headers["location"] == f"/compare/{_FID_A}/vs/{_FID_B}/"


def test_compare_detail_renders():
    _seed()
    resp = client.get(f"/compare/{_FID_A}/vs/{_FID_B}/")
    assert resp.status_code == 200
    assert "Test General Hospital" in resp.text
    assert "Test Specialty Center" in resp.text
    assert 'data-free-map="compare"' in resp.text
    assert '"@type": "WebPage"' in resp.text
    assert "Reviewed" in resp.text


def test_compare_detail_shows_verdict():
    _seed()
    resp = client.get(f"/compare/{_FID_A}/vs/{_FID_B}/")
    assert resp.status_code == 200
    assert "Better Value" in resp.text or "Tie" in resp.text or "Insufficient Data" in resp.text


def test_compare_detail_shows_grade_table():
    _seed()
    resp = client.get(f"/compare/{_FID_A}/vs/{_FID_B}/")
    assert resp.status_code == 200
    assert "Billing Grade" in resp.text


def test_compare_detail_shows_procedure_table():
    _seed()
    resp = client.get(f"/compare/{_FID_A}/vs/{_FID_B}/")
    assert resp.status_code == 200
    assert "Procedure Price Comparison" in resp.text or "27447" in resp.text


def test_compare_detail_not_found():
    _seed()
    resp = client.get("/compare/000000/vs/000001/")
    assert resp.status_code == 200
    assert "not found" in resp.text.lower()


def test_compare_detail_shows_ctas():
    _seed()
    resp = client.get(f"/compare/{_FID_A}/vs/{_FID_B}/")
    assert resp.status_code == 200
    assert "Scan Your Bill" in resp.text


def test_compare_detail_shows_share_url():
    _seed()
    resp = client.get(f"/compare/{_FID_A}/vs/{_FID_B}/")
    assert resp.status_code == 200
    assert "shareUrl" in resp.text or "/compare/" in resp.text


def test_compare_seo_route_renders_human_readable_page():
    _seed()
    resp = client.get("/compare/test-general-hospital-springfield-vs-test-specialty-center-springfield/")
    assert resp.status_code == 200
    assert "Which Costs Less" in resp.text or "Test General Hospital" in resp.text


# ---- API tests ----

def test_hospital_search_api_requires_query():
    resp = client.get("/api/hospitals/search")
    assert resp.status_code == 200
    data = resp.json()
    results = data.get("results")
    if results is None:
        results = data.get("data", [])
    assert results == []


def test_hospital_search_api_returns_results():
    _seed()
    resp = client.get("/api/hospitals/search?q=Test")
    assert resp.status_code == 200
    data = resp.json()
    results = data.get("results")
    if results is None:
        results = data.get("data", [])
    assert len(results) >= 1
    # Each result must include key display/search fields.
    for r in results:
        assert "name" in r
        assert "city" in r
        assert "state" in r


def test_hospital_search_api_short_query_returns_empty():
    resp = client.get("/api/hospitals/search?q=T")
    assert resp.status_code == 200
    payload = resp.json()
    results = payload.get("results")
    if results is None:
        results = payload.get("data", [])
    assert results == []


# ---- Function tests ----

def test_get_hospital_for_compare_found():
    _seed()
    h = get_hospital_for_compare(_FID_A)
    assert h is not None
    assert h["facility_id"] == _FID_A
    assert h["billing_grade"] == "A"
    assert "grade_badge" in h
    assert "grade_color" in h
    assert "ownership_label" in h


def test_get_hospital_for_compare_not_found():
    _seed()
    h = get_hospital_for_compare("000000")
    assert h is None


def test_get_common_procedures_returns_shared():
    _seed()
    procs = get_common_procedures(_FID_A, _FID_B)
    assert len(procs) >= 1
    for p in procs:
        assert "cpt_code" in p
        assert "charge_a" in p
        assert "charge_b" in p
        assert "cheaper" in p
        assert p["cheaper"] in ("a", "b")
        assert "savings" in p


def test_get_comparison_data_full():
    _seed()
    data = get_comparison_data(_FID_A, _FID_B)
    assert data is not None
    assert "a" in data and "b" in data
    assert "common_procedures" in data
    assert "verdict" in data
    assert "map_data" in data
    assert data["map_data"]["available"] is True
    assert "winner" in data["verdict"]
    assert data["verdict"]["winner"] in ("a", "b", "tie", "unknown")


def test_get_comparison_data_verdict_winner_a():
    """Hospital A has grade A, B has grade D — A should win."""
    _seed()
    data = get_comparison_data(_FID_A, _FID_B)
    assert data["verdict"]["winner"] == "a"


def test_get_comparison_data_missing_hospital():
    _seed()
    data = get_comparison_data(_FID_A, "000000")
    assert data is None


def test_search_hospitals_for_compare_found():
    _seed()
    results = search_hospitals_for_compare("Test")
    assert len(results) >= 1
    for r in results:
        assert "facility_id" in r
        assert "name" in r
        assert "city" in r
        assert "state" in r


def test_search_hospitals_for_compare_short_query():
    results = search_hospitals_for_compare("T")
    assert results == []


def test_compare_detail_distance_shown():
    _seed()
    data = get_comparison_data(_FID_A, _FID_B)
    assert data["distance_miles"] is not None
    assert data["distance_miles"] < 5.0  # Both are in Springfield, close together
    assert data["map_data"]["line"]["show"] is True


def test_compare_map_fallback_without_coordinates():
    _seed()
    with get_db() as db:
        db.execute("UPDATE hospitals SET lat = NULL, lon = NULL WHERE facility_id = ?", (_FID_A,))
    data = get_comparison_data(_FID_A, _FID_B)
    assert data is not None
    assert data["map_data"]["available"] is False


# ---- Float facility ID cleanup tests ----


def test_compare_detail_redirects_float_ids():
    """Float-suffixed facility IDs in URLs get 301-redirected to clean versions."""
    _seed()
    resp = client.get(f"/compare/{_FID_A}.0/vs/{_FID_B}.0/", follow_redirects=False)
    assert resp.status_code == 301
    assert resp.headers["location"] == f"/compare/{_FID_A}/vs/{_FID_B}/"


def test_compare_query_cleans_float_hospital_param():
    """The ?hospital= param gets cleaned of .0 suffix before redirect."""
    _seed()
    resp = client.get(f"/compare/?hospital={_FID_A}.0", follow_redirects=False)
    assert resp.status_code == 301
    assert f"{_FID_A}.0" not in resp.headers["location"]
    assert _FID_A in resp.headers["location"]


def test_normalize_facility_id_strips_float():
    from hospital_seo import normalize_facility_id
    assert normalize_facility_id("1659325629.0") == "1659325629"
    assert normalize_facility_id("010001.0") == "010001"
    assert normalize_facility_id("010001") == "010001"
    assert normalize_facility_id(None) is None
    assert normalize_facility_id("") is None
