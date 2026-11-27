"""Loading a hospital's published price file: found through cms-hpt.txt, read as it downloads."""

import io
import os

import pytest

import config
import hospital_etl
import mrf_loader
from db import get_db
from hospital_seo import recompute_billing_metrics, upsert_hospital_row

SCRIPPS_SAMPLE = os.path.join(os.path.dirname(__file__), "test_data", "scripps_mercy_cms_sample.csv")
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
# 99285 is the 2026 national hospital outpatient rate production uses; the lower levels are test values in proportion.
OPPS_RATES = {"99281": 91.07, "99282": 165.63, "99283": 290.47, "99284": 432.80, "99285": 608.43}


@pytest.fixture
def scripps_mercy():
    upsert_hospital_row({"facility_id": "050077", "name": "SCRIPPS MERCY HOSPITAL", "address": "4077 5TH AVE", "city": "SAN DIEGO",
                         "state": "CA", "zip": "92103", "slug": "scripps-mercy-hospital-san-diego"})
    with get_db() as db:
        for code, rate in OPPS_RATES.items():
            db.execute("INSERT OR REPLACE INTO hospital_opps_rates (cpt_code, description, national_payment_rate, effective_year) "
                       "VALUES (?, 'Emergency dept visit', ?, 2026)", (code, rate))


def serve(monkeypatch, price_file: bytes, hpt: str = SCRIPPS_HPT):
    def fake_open(url):
        return io.BytesIO(hpt.encode() if url.endswith("/cms-hpt.txt") else price_file)
    monkeypatch.setattr(mrf_loader, "_open", fake_open)


def load_scripps():
    return mrf_loader.load_hospital_prices("050077", "https://www.scripps.org", "Scripps Mercy Hospital San Diego", data_year=2026)


def test_real_file_cut_loads_er_prices_with_source_and_grade(monkeypatch, scripps_mercy):
    with open(SCRIPPS_SAMPLE, "rb") as f:
        serve(monkeypatch, f.read())

    result = load_scripps()
    recompute_billing_metrics()

    assert result["status"] == "loaded" and result["rows"] == 5
    assert result["er_gross_charges"] == {"99281": 839.92, "99282": 1312.38, "99283": 2414.77, "99284": 3884.63, "99285": 7874.25}
    with get_db() as db:
        level5 = dict(db.execute("SELECT * FROM hospital_prices WHERE facility_id = '050077' AND cpt_code = '99285'").fetchone())
        grade = db.execute("SELECT billing_grade, procedures_compared FROM billing_metrics WHERE facility_id = '050077'").fetchone()
    # The file also lists "HC ER Level V Trauma" at $23,622.75 under 99285; the plain visit is the list price.
    assert (level5["description"], level5["gross_charge"], level5["cash_price"]) == ("HC ER Level V", 7874.25, 1968.56)
    assert (level5["source_url"], level5["source_updated"]) == (SCRIPPS_FILE_URL, "2026-03-30")
    assert round(level5["markup_vs_medicare"], 1) == 12.9
    assert (grade["billing_grade"], grade["procedures_compared"]) == ("F", 5)
    from mcp_server import get_hospital_prices
    listed = get_hospital_prices("050077", "99285")["prices"][0]
    assert (listed["list_price"], listed["source_file"], listed["source_file_updated"]) == (7874.25, SCRIPPS_FILE_URL, "2026-03-30")


def test_malformed_file_loads_nothing(monkeypatch, scripps_mercy):
    """A download cut off inside a quoted field: the CSV reader gives up instead of inventing rows."""
    with open(SCRIPPS_SAMPLE, "rb") as f:
        header = b"\n".join(f.read().split(b"\n")[:3])
    serve(monkeypatch, header + b'\n"HC ER Level V","PX-40100004","CDM","99285","CPT","0450","RC","","","both","","",7874.25,1968.56,"' + b"x" * 200_000)

    assert load_scripps()["status"] == "malformed_file"
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) FROM hospital_prices WHERE facility_id = '050077'").fetchone()[0] == 0


def test_error_page_instead_of_a_price_file_loads_nothing(monkeypatch, scripps_mercy):
    serve(monkeypatch, b"<!DOCTYPE html>\n<html><head><title>403 Forbidden</title></head>\n<body>Access denied, 99285</body></html>\n")

    assert load_scripps()["status"] == "unsupported_format"
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) FROM hospital_prices WHERE facility_id = '050077'").fetchone()[0] == 0


def test_empty_file_loads_nothing(monkeypatch, scripps_mercy):
    serve(monkeypatch, b"")

    assert load_scripps()["status"] == "empty_file"
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) FROM hospital_prices WHERE facility_id = '050077'").fetchone()[0] == 0


def test_hospital_without_a_level_5_gross_charge_is_skipped(monkeypatch, scripps_mercy):
    with open(SCRIPPS_SAMPLE, "rb") as f:
        lines = f.read().split(b"\n")
    serve(monkeypatch, b"\n".join(line for line in lines if b'"99285"' not in line))

    assert load_scripps()["status"] == "no_99285_gross_charge"
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) FROM hospital_prices WHERE facility_id = '050077'").fetchone()[0] == 0


def test_json_price_file_is_reported_not_guessed(monkeypatch, scripps_mercy):
    hpt = "location-name: UC San Diego Hillcrest Medical Center\nmrf-url: https://hsfiles.ucsd.edu/patientBilling/UC-San-Diego-Standard-Charges-956006144.json\n"
    serve(monkeypatch, b'{   "hospital_name": "UC San Diego Medical Center",   "last_updated_on": "2026-04-01",   "version": "3.0"}', hpt)

    result = mrf_loader.load_hospital_prices("050077", "https://health.ucsd.edu", "UC San Diego Hillcrest Medical Center")

    assert result["status"] == "unsupported_format"


def test_location_missing_from_cms_hpt(monkeypatch, scripps_mercy):
    serve(monkeypatch, b"")

    assert mrf_loader.load_hospital_prices("050077", "https://www.scripps.org", "Scripps Hospital Nowhere")["status"] == "not_listed_in_cms_hpt"


def test_file_date_reads_both_formats_hospitals_use():
    assert mrf_loader.file_date("2026-03-30") == "2026-03-30"
    assert mrf_loader.file_date("4/1/2026") == "2026-04-01"
    assert mrf_loader.file_date("") is None


def test_ops_endpoint_needs_the_admin_token_and_valid_targets(monkeypatch):
    from fastapi.testclient import TestClient
    import main

    started = []
    monkeypatch.setattr(config, "ADMIN_API_TOKEN", "ops-secret")
    monkeypatch.setattr(mrf_loader, "run_price_load", started.append)
    client = TestClient(main.app)
    target = {"facility_id": "050077", "site": "https://www.scripps.org", "location_name": "Scripps Mercy Hospital San Diego"}
    admin = {"x-admin-token": "ops-secret"}

    assert client.post("/ops/load-hospital-prices", json=[target]).status_code == 403
    assert client.post("/ops/load-hospital-prices", json=[{"facility_id": "050077"}], headers=admin).status_code == 400
    assert client.post("/ops/load-hospital-prices", json=[{**target, "site": "http://internal"}], headers=admin).status_code == 400
    ok = client.post("/ops/load-hospital-prices", json=[target], headers=admin)
    assert ok.json() == {"status": "ok", "data": {"started": 1}}


TRI_CITY_HEADER = ("description,code|1,code|1|type,code|2,code|2|type,code|3,code|3|type,code|4,code|4|type,billing_class,setting,"
                   "drug_unit_of_measurement,drug_type_of_measurement,standard_charge|gross,standard_charge|discounted_cash,payer_name,"
                   "plan_name,modifiers,standard_charge|negotiated_dollar")


def price_file(*rows: str) -> io.BytesIO:
    return io.BytesIO("\n".join(["hospital_name,last_updated_on,version", "Tri-City Medical Center,2026-05-29,3.0.0", TRI_CITY_HEADER, *rows]).encode())


def test_list_price_is_the_plain_facility_charge_whatever_the_file_order():
    """Tri-City's file lists level 5 three ways (the first three rows, payer columns shortened). The with-procedure
    row (modifier 25) is not the plain visit, and neither is a professional fee of the kind other files carry."""
    rows, preamble, status = mrf_loader.read_price_csv(price_file(
        "9928525 LEVEL 5 ED SERVICES W/PROC TechFee,143025102,CDM,450,RC,99285,HCPCS,,,facility,outpatient,,,5750.00000,3450.00000,AETNA,PPO,25,4536.75",
        "99285 - Level 5,143088102,CDM,450,RC,99285,HCPCS,,,facility,outpatient,,,5951.25000,3570.75000,AETNA,PPO,,4695.54",
        "99285 ER VISIT LEVEL 5 TechFee,143088102,CDM,450,RC,99285,HCPCS,,,facility,outpatient,,,5750.00000,3450.00000,AETNA,PPO,,4536.75",
        "ED PHYSICIAN LEVEL 5,900285,CDM,981,RC,99285,HCPCS,,,professional,outpatient,,,1100.00000,660.00000,AETNA,PPO,,410.00",
    ))
    level5 = hospital_etl.summarize_by_code(rows)[0]

    assert (status, preamble["last_updated_on"]) == ("parsed", "2026-05-29")
    assert (level5["description"], level5["gross_charge"], level5["cash_price"]) == ("99285 ER VISIT LEVEL 5 TechFee", 5750.0, 3450.0)


def test_kaiser_wide_file_with_capitalised_modifiers_column():
    """Kaiser's header spells the column "Modifiers " and wraps descriptions in extra quotes. The first row is from its
    Zion file; the second adds a modifier to show that column is still read."""
    header = ("description,code|1,code|1|type,code|2,code|2|type,Modifiers ,setting,drug_unit_of_measurement,drug_type_of_measurement,"
              "standard_charge|gross,standard_charge|discounted_cash,standard_charge|[KAISER FOUNDATION HEALTH PLAN, INC.]|[COMMERCIAL]|negotiated_dollar")
    file = io.BytesIO("\n".join([
        "hospital_name,last_updated_on,version", "KAISER FOUNDATION HOSPITAL - SAN DIEGO - ZION,4/1/2026,3.0.1", header,
        '"""FACILITY USE-EMERGENCY ROOM, LEVEL 5""",6540,CDM,99285,CPT,,both,,,6316,3284.32,3880',
        '"""FACILITY USE-EMERGENCY ROOM, LEVEL 5""",6540,CDM,99285,CPT,25,both,,,5000,2600,3000',
    ]).encode())

    rows, preamble, status = mrf_loader.read_price_csv(file)
    level5 = hospital_etl.summarize_by_code(rows)[0]

    assert (status, mrf_loader.file_date(preamble["last_updated_on"])) == ("parsed", "2026-04-01")
    assert (level5["description"], level5["gross_charge"], level5["cash_price"]) == ("FACILITY USE-EMERGENCY ROOM, LEVEL 5", 6316.0, 3284.32)


class CutShortDownload(io.BytesIO):
    """What http.client hands back when the server closes the connection early: a clean end of file, with bytes still owed."""
    length = 578_000_000


def test_download_cut_short_after_the_er_rows_loads_nothing(monkeypatch, scripps_mercy):
    with open(SCRIPPS_SAMPLE, "rb") as f:
        partial_file = f.read()
    monkeypatch.setattr(mrf_loader, "_open", lambda url: io.BytesIO(SCRIPPS_HPT.encode()) if url.endswith("/cms-hpt.txt") else CutShortDownload(partial_file))

    assert load_scripps()["status"] == "download_incomplete"
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) FROM hospital_prices WHERE facility_id = '050077'").fetchone()[0] == 0


def test_cms_hpt_with_a_byte_order_mark_and_two_files_per_location():
    entries = mrf_loader.parse_cms_hpt(b"\xef\xbb\xbflocation-name: Sharp Memorial Hospital\nmrf-url: https://example.org/a.csv\nmrf-url: https://example.org/a.json\n".decode("utf-8-sig"))

    assert entries == [{"location-name": "Sharp Memorial Hospital", "mrf-url": "https://example.org/a.csv"}]
