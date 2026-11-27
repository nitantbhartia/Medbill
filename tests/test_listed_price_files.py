"""Loading hospitals named in POST /ops/load-hospital-prices: each file is found through the site's cms-hpt.txt."""

import io
import os
import shutil

import pytest

import config
import price_file_loader
from db import get_db
from hospital_seo import upsert_hospital_row

TEST_DATA = os.path.join(os.path.dirname(__file__), "test_data")
SCRIPPS_SAMPLE = os.path.join(TEST_DATA, "scripps_mercy_cms_sample.csv")  # rows cut from the hospital's real file, Nov 27 2026
SCRIPPS_FILE_URL = "https://apps.scripps.org/pricetransparency/951684089_Scripps-Mercy-Hospital-San-Diego_standardcharges.csv"
SCRIPPS_HPT = f"""location-name: Scripps Memorial Hospital La Jolla
source-page-url: https://www.scripps.org/patients-and-visitors/billing/price-transparency
mrf-url: https://apps.scripps.org/pricetransparency/951684089_Scripps-Memorial-Hospital-La-Jolla_standardcharges.csv
contact-name: Billing Inquiries
contact-email: billinginquiries@scrippshealth.org

location-name: Scripps Mercy Hospital San Diego
source-page-url: https://www.scripps.org/patients-and-visitors/billing/price-transparency
mrf-url: {SCRIPPS_FILE_URL}
contact-name: Billing Inquiries
contact-email: billinginquiries@scrippshealth.org
"""
SCRIPPS_TARGET = {"facility_id": "050077", "name_phrase": "Scripps Mercy", "site": "https://www.scripps.org",
                  "location_name": "Scripps Mercy Hospital San Diego"}
# 99285 is the 2026 national hospital outpatient rate production uses; the lower levels are test values in proportion.
OPPS_RATES = {"99281": 91.07, "99282": 165.63, "99283": 290.47, "99284": 432.80, "99285": 608.43}
INFO_LINES = "hospital_name,last_updated_on,version\n{name},{updated},3.0.0\n"


@pytest.fixture
def scripps_mercy():
    upsert_hospital_row({"facility_id": "050077", "name": "SCRIPPS MERCY HOSPITAL", "address": "4077 5TH AVE", "city": "SAN DIEGO",
                         "state": "CA", "zip": "92103", "slug": "scripps-mercy-hospital-san-diego"})
    with get_db() as db:
        for code, rate in OPPS_RATES.items():
            db.execute("INSERT OR REPLACE INTO hospital_opps_rates (cpt_code, description, national_payment_rate, effective_year) "
                       "VALUES (?, 'Emergency dept visit', ?, 2026)", (code, rate))


def serve(monkeypatch, price_file: str, hpt: str = SCRIPPS_HPT):
    """Stand in for the two downloads: the site's cms-hpt.txt and the price file it lists."""
    monkeypatch.setattr(price_file_loader, "urlopen", lambda request, timeout: io.BytesIO(hpt.encode()))
    monkeypatch.setattr(price_file_loader, "download_price_file", lambda url, path: shutil.copyfile(price_file, path))


def write_file(tmp_path, name: str, updated: str, header: str, *rows: str) -> str:
    path = tmp_path / "standardcharges.csv"
    path.write_text(INFO_LINES.format(name=name, updated=updated) + "\n".join([header, *rows]) + "\n")
    return str(path)


def test_real_scripps_cut_loads_the_plain_level_5_visit_and_grades(monkeypatch, scripps_mercy):
    serve(monkeypatch, SCRIPPS_SAMPLE)

    results = price_file_loader.load_listed_hospitals([SCRIPPS_TARGET])

    assert results[0]["status"] == "loaded" and results[0]["source_url"] == SCRIPPS_FILE_URL
    with get_db() as db:
        level5 = dict(db.execute("SELECT * FROM hospital_prices WHERE facility_id = '050077' AND cpt_code = '99285'").fetchone())
        grade = db.execute("SELECT billing_grade, procedures_compared FROM billing_metrics WHERE facility_id = '050077'").fetchone()
        logged = db.execute("SELECT status FROM data_refresh_log WHERE source = ?", (price_file_loader.LISTED_LOAD_SOURCE,)).fetchone()
    # The file also lists "HC ER Level V Trauma" at $23,622.75 under 99285.
    assert (level5["description"], level5["gross_charge"], level5["cash_price"]) == ("HC ER Level V", 7874.25, 1968.56)
    assert (level5["source_url"], level5["source_updated_on"]) == (SCRIPPS_FILE_URL, "2026-03-30")
    assert round(level5["markup_vs_medicare"], 1) == 12.9
    assert (grade["billing_grade"], grade["procedures_compared"], logged["status"]) == ("F", 5, "success")
    from mcp_server import get_hospital_prices
    listed = get_hospital_prices("050077", "99285")["prices"][0]
    assert (listed["list_price"], listed["source_file"], listed["source_file_updated"]) == (7874.25, SCRIPPS_FILE_URL, "2026-03-30")


def test_location_not_listed_in_cms_hpt_is_skipped(monkeypatch, scripps_mercy):
    serve(monkeypatch, SCRIPPS_SAMPLE)

    result = price_file_loader.load_listed_hospital({**SCRIPPS_TARGET, "location_name": "Scripps Hospital Nowhere"})

    assert result["status"] == "skipped" and "not listed" in result["reason"]


def test_file_listed_for_another_hospital_is_not_loaded(monkeypatch, scripps_mercy):
    serve(monkeypatch, SCRIPPS_SAMPLE)

    result = price_file_loader.load_listed_hospital({**SCRIPPS_TARGET, "name_phrase": "Sharp Memorial"})

    assert result["status"] == "skipped"
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) FROM hospital_prices WHERE facility_id = '050077'").fetchone()[0] == 0


def test_cms_hpt_with_a_byte_order_mark_and_two_files_per_location():
    text = b"\xef\xbb\xbflocation-name: Sharp Memorial Hospital\nmrf-url: https://example.org/a.csv\nmrf-url: https://example.org/a.json\n"

    assert price_file_loader.parse_cms_hpt(text.decode("utf-8-sig")) == {"sharp memorial hospital": "https://example.org/a.csv"}


class CutShortDownload(io.BytesIO):
    """What http.client hands back when the server closes the connection early: a clean end of file, with bytes still owed."""
    length = 578_000_000


def test_download_cut_short_is_an_error_not_a_smaller_file(monkeypatch, tmp_path):
    with open(SCRIPPS_SAMPLE, "rb") as f:
        received = f.read()
    monkeypatch.setattr(price_file_loader, "urlopen", lambda request, timeout: CutShortDownload(received))

    with pytest.raises(ValueError, match="bytes short"):
        price_file_loader.download_price_file(SCRIPPS_FILE_URL, str(tmp_path / "standardcharges.csv"))


def test_kaiser_wide_file_with_capitalised_modifiers_column(tmp_path):
    """Kaiser's header spells the column "Modifiers ". The first row is from its Zion file; the second adds a modifier."""
    path = write_file(
        tmp_path, "KAISER FOUNDATION HOSPITAL - SAN DIEGO - ZION", "4/1/2026",
        "description,code|1,code|1|type,code|2,code|2|type,Modifiers ,setting,drug_unit_of_measurement,drug_type_of_measurement,"
        "standard_charge|gross,standard_charge|discounted_cash",
        '"""FACILITY USE-EMERGENCY ROOM, LEVEL 5""",6540,CDM,99285,CPT,,both,,,6316,3284.32',
        '"""FACILITY USE-EMERGENCY ROOM, LEVEL 5""",6540,CDM,99285,CPT,25,both,,,5000,2600',
    )

    level5 = price_file_loader.read_list_prices(path)[0]

    assert price_file_loader.file_updated_on(path) == "2026-04-01"
    assert (level5["cpt_code"], level5["gross_charge"], level5["cash_price"]) == ("99285", 6316.0, 3284.32)


def test_two_plain_level_5_lines_at_different_prices_are_not_guessed_between(tmp_path):
    """Tri-City's file (Nov 27 2026) lists these two plain level 5 lines, plus a with-procedure line under modifier 25."""
    path = write_file(
        tmp_path, "Tri-City Medical Center", "2026-05-29",
        "description,code|1,code|1|type,code|2,code|2|type,code|3,code|3|type,billing_class,setting,standard_charge|gross,"
        "standard_charge|discounted_cash,modifiers",
        "9928525 LEVEL 5 ED SERVICES W/PROC TechFee,143025102,CDM,450,RC,99285,HCPCS,facility,outpatient,5750.00000,3450.00000,25",
        "99285 - Level 5,143088102,CDM,450,RC,99285,HCPCS,facility,outpatient,5951.25000,3570.75000,",
        "99285 ER VISIT LEVEL 5 TechFee,143088102,CDM,450,RC,99285,HCPCS,facility,outpatient,5750.00000,3450.00000,",
    )

    with pytest.raises(ValueError, match="no single gross charge for 99285"):
        price_file_loader.read_list_prices(path)


def test_ops_endpoint_needs_the_admin_token_and_valid_targets(monkeypatch):
    from fastapi.testclient import TestClient
    import main

    started = []
    monkeypatch.setattr(config, "ADMIN_API_TOKEN", "ops-secret")
    monkeypatch.setattr(price_file_loader, "load_listed_hospitals", started.append)
    client = TestClient(main.app)
    admin = {"x-admin-token": "ops-secret"}

    assert client.post("/ops/load-hospital-prices", json=[SCRIPPS_TARGET]).status_code == 403
    assert client.post("/ops/load-hospital-prices", json=[{"facility_id": "050077"}], headers=admin).status_code == 400
    assert client.post("/ops/load-hospital-prices", json=[{**SCRIPPS_TARGET, "site": "http://internal"}], headers=admin).status_code == 400
    ok = client.post("/ops/load-hospital-prices", json=[SCRIPPS_TARGET], headers=admin)
    assert ok.json() == {"status": "ok", "data": {"started": 1}}
    assert started == [[SCRIPPS_TARGET]]
