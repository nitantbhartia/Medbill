"""A hospital's city and state must match its own CMS record, not a health system's billing address."""

import io
import json
import os

import hospital_locations
from db import get_db
from hospital_etl import load_cms_general
from hospital_seo import upsert_hospital_row

CMS_SAMPLE = os.path.join(os.path.dirname(__file__), "test_data", "cms_hospital_general_sample.csv")
# What CMS's NPI registry returns for NPI 1316536253 (addresses only).
SOUTH_OVERLAND_PARK_NPI = {"results": [{"addresses": [
    {"address_purpose": "LOCATION", "address_1": "7820 W 165TH ST", "city": "OVERLAND PARK", "state": "KS", "postal_code": "662232925"},
    {"address_purpose": "MAILING", "address_1": "7820 W 165TH ST", "city": "OVERLAND PARK", "state": "KS", "postal_code": "662232925"},
]}]}
# NPI 1912509191: the mailing address is in another city, and must not be used.
WATERMAN_NPI = {"results": [{"addresses": [
    {"address_purpose": "MAILING", "address_1": "3253 DORNICH DR", "city": "MOUNT DORA", "state": "FL", "postal_code": "327579756"},
    {"address_purpose": "LOCATION", "address_1": "1000 WATERMAN WAY", "city": "TAVARES", "state": "FL", "postal_code": "327785266"},
]}]}


def seed_as_production_had_it():
    """The CMS directory, plus two DoltHub-seeded rows listed under Tampa, FL, the city production showed for them."""
    load_cms_general(CMS_SAMPLE)
    for npi, name in (("1316536253", "AdventHealth South Overland Park"), ("1912509191", "AdventHealth Waterman")):
        upsert_hospital_row({"facility_id": npi, "name": name, "address": "14055 Riveredge Dr", "city": "Tampa", "state": "FL", "zip": "33637"})


def cms_records(monkeypatch) -> dict:
    registry = {"1316536253": SOUTH_OVERLAND_PARK_NPI, "1912509191": WATERMAN_NPI}
    monkeypatch.setattr(hospital_locations.urllib.request, "urlopen",
                        lambda request, timeout: io.BytesIO(json.dumps(registry[request.full_url.rsplit("=", 1)[1]]).encode()))
    records = hospital_locations.read_cms_directory(CMS_SAMPLE)
    records.update({npi: hospital_locations.npi_practice_location(npi) for npi in registry})
    return records


def test_no_hospital_disagrees_with_its_cms_record_after_repair(monkeypatch):
    seed_as_production_had_it()
    records = cms_records(monkeypatch)

    assert hospital_locations.repair_hospital_locations(records) == 2

    assert hospital_locations.location_mismatches(records) == []
    with get_db() as db:
        moved = {row["facility_id"]: dict(row) for row in db.execute(
            "SELECT facility_id, city, state, zip, city_slug, state_slug FROM hospitals WHERE LENGTH(facility_id) = 10")}
        mirror = db.execute("SELECT city, state FROM facilities WHERE facility_id = '1316536253'").fetchone()
    assert moved["1316536253"] == {"facility_id": "1316536253", "city": "OVERLAND PARK", "state": "KS", "zip": "66223",
                                   "city_slug": "overland-park", "state_slug": "ks"}
    assert (moved["1912509191"]["city"], moved["1912509191"]["state"]) == ("TAVARES", "FL")
    assert (mirror["city"], mirror["state"]) == ("OVERLAND PARK", "KS")


def test_billing_address_city_is_reported_as_a_mismatch(monkeypatch):
    seed_as_production_had_it()

    wrong = {m["facility_id"]: (m["city"], m["state"], m["cms"]["city"], m["cms"]["state"])
             for m in hospital_locations.location_mismatches(cms_records(monkeypatch))}

    assert wrong == {
        "1316536253": ("Tampa", "FL", "OVERLAND PARK", "KS"),
        "1912509191": ("Tampa", "FL", "TAVARES", "FL"),
    }


def test_old_page_address_redirects_after_a_hospital_moves(monkeypatch):
    from fastapi.testclient import TestClient
    import main

    seed_as_production_had_it()
    hospital_locations.repair_hospital_locations(cms_records(monkeypatch))

    response = TestClient(main.app).get("/hospitals/fl/tampa/adventhealth-south-overland-park-tampa/", follow_redirects=False)

    assert response.status_code == 301
    assert response.headers["location"] == "/hospitals/ks/overland-park/adventhealth-south-overland-park-tampa/"
