"""Hospitals saved with a junk state ('73', 'L', 'Florida') must end up at a real state URL."""

import sqlite3

from db import get_db
from hospital_seo import normalize_state_code, repair_hospital_states, upsert_hospital_row
from tests.test_hospital_pages import client  # noqa: F401  (sets up app + in-memory DB)


def _zip_in(state: str, zip_code: str):
    with get_db() as db:
        db.execute("INSERT OR REPLACE INTO zip_latlon (zip, lat, lon, state, city) VALUES (?, 40.8, -115.7, ?, 'Elko')", (zip_code, state))


def test_full_state_names_and_codes_normalize_without_a_zip():
    assert normalize_state_code("Florida", "") == "FL"
    assert normalize_state_code("fl", "") == "FL"
    assert normalize_state_code("Puerto Rico", "") == "PR"


def test_junk_state_is_inferred_from_the_zip():
    _zip_in("NV", "89801")
    assert normalize_state_code("73", "89801") == "NV"
    assert normalize_state_code("73", "") is None


def test_new_hospital_with_junk_state_is_saved_under_the_real_state():
    _zip_in("AL", "36701")
    upsert_hospital_row({"facility_id": "010999", "name": "Vaughan Regional Medical Center", "city": "Selma",
                         "state": "L", "zip": "36701", "slug": "vaughan-regional-medical-center-selma"})
    with get_db() as db:
        row = db.execute("SELECT state, state_slug FROM hospitals WHERE facility_id = '010999'").fetchone()
    assert (row["state"], row["state_slug"]) == ("AL", "al")


def test_hospital_with_unknown_state_is_not_saved():
    upsert_hospital_row({"facility_id": "010998", "name": "Mystery Hospital", "city": "Nowhere", "state": "73", "zip": "00000"})
    with get_db() as db:
        assert db.execute("SELECT 1 FROM hospitals WHERE facility_id = '010998'").fetchone() is None


def test_repair_fixes_existing_rows_and_their_page_addresses():
    _zip_in("NV", "89801")
    upsert_hospital_row({"facility_id": "010997", "name": "Northeastern Nevada Regional Hospital", "city": "Elko",
                         "state": "NV", "zip": "89801", "slug": "northeastern-nevada-regional-hospital-elko"})
    with get_db() as db:
        db.execute("UPDATE hospitals SET state = '73', state_slug = '73' WHERE facility_id = '010997'")
    assert repair_hospital_states() == 1
    assert client.get("/hospitals/nv/elko/northeastern-nevada-regional-hospital-elko/").status_code == 200
    assert repair_hospital_states() == 0
