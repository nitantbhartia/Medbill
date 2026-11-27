"""Loading a hospital's published standard-charges file, and checking hospital locations against CMS."""

import os
import shutil
from datetime import date

import pytest

import config
import price_file_loader
from data_quality import hospitals_off_cms_location
from db import get_db
from hospital_etl import load_cms_general
from hospital_seo import recompute_billing_metrics, upsert_hospital_row

TEST_DATA = os.path.join(os.path.dirname(__file__), "test_data")
RUTHERFORD_FILE = os.path.join(TEST_DATA, "rutherford_cms_sample.csv")  # rows cut from the hospital's real 2026 file
CMS_GENERAL = os.path.join(TEST_DATA, "cms_hospital_general_sample.csv")
RUTHERFORD_URL = "https://hospital.example/621869474_saint-thomas-rutherford-hospital_standardcharges.csv"  # placeholder address
RUTHERFORD = {"facility_id": "440053", "name": "SAINT THOMAS RUTHERFORD HOSPITAL", "city": "MURFREESBORO", "state": "TN", "zip": "37129"}
INFO_LINES = (
    "hospital_name,last_updated_on,version,location_name,hospital_address,license_number|CA,type_2_npi,attestation\n"
    "Scripps Mercy Hospital,10/01/2026,3.0.0,Scripps Mercy Hospital San Diego,4077 Fifth Ave San Diego CA 92103,090000074|CA,1154305399,TRUE\n"
    "description,code|1,code|1|type,modifiers,setting,billing_class,standard_charge|gross,standard_charge|discounted_cash\n"
)


def saved_prices(facility_id: str) -> dict:
    with get_db() as db:
        rows = db.execute("SELECT * FROM hospital_prices WHERE facility_id = ?", (facility_id,)).fetchall()
    return {row["cpt_code"]: dict(row) for row in rows}


def write_file(tmp_path, rows: str) -> str:
    path = tmp_path / "standardcharges.csv"
    path.write_text(INFO_LINES + rows)
    return str(path)


def test_real_file_loads_er_price_with_source_url_and_file_date():
    upsert_hospital_row(RUTHERFORD)

    result = price_file_loader.load_price_file("440053", RUTHERFORD_FILE, RUTHERFORD_URL)

    er = saved_prices("440053")["99285"]
    assert result["status"] == "loaded" and result["file_updated_on"] == "2026-01-01"
    assert result["er_prices"]["99285"] == {"gross": 3200.0, "cash": 960.0}
    assert (er["gross_charge"], er["cash_price"], er["data_year"]) == (3200.0, 960.0, date.today().year)
    assert (er["source_url"], er["source_updated_on"]) == (RUTHERFORD_URL, "2026-01-01")
    assert er["medicare_benchmark_type"] == "opps" and er["markup_vs_medicare"] == pytest.approx(3200.0 / er["medicare_rate"])


def test_error_page_saved_as_csv_is_skipped_and_loads_nothing():
    upsert_hospital_row(RUTHERFORD)

    result = price_file_loader.load_price_file("440053", os.path.join(TEST_DATA, "blocked_download_standardcharges.csv"), RUTHERFORD_URL)

    assert result["status"] == "skipped" and "last_updated_on" in result["reason"]
    assert saved_prices("440053") == {}


def test_empty_file_is_skipped_and_loads_nothing():
    upsert_hospital_row(RUTHERFORD)

    result = price_file_loader.load_price_file("440053", os.path.join(TEST_DATA, "empty_standardcharges.csv"), RUTHERFORD_URL)

    assert result["status"] == "skipped"
    assert saved_prices("440053") == {}


def test_hospital_without_a_level_5_gross_charge_is_skipped(tmp_path):
    path = write_file(tmp_path, "HC ED VISIT LEVEL 4,99284,CPT,,outpatient,facility,2874.00,1437.00\n"
                                "HC ED VISIT LEVEL 5,99285,CPT,,outpatient,facility,,2105.50\n")

    with pytest.raises(ValueError, match="99285"):
        price_file_loader.read_list_prices(path)


def test_two_plain_level_5_charges_are_not_guessed_between(tmp_path):
    path = write_file(tmp_path, "HC ED VISIT LEVEL 5,99285,CPT,,outpatient,facility,4211.00,2105.50\n"
                                "HC ED VISIT LEVEL 5 EXTENDED,99285,CPT,,outpatient,facility,6890.00,3445.00\n")

    with pytest.raises(ValueError, match="99285"):
        price_file_loader.read_list_prices(path)


def test_trauma_critical_and_lwbs_lines_are_not_the_visit_charge(tmp_path):
    # Charge lines and gross charges as published in Sharp Memorial Hospital's file (cash prices here are illustrative).
    path = write_file(tmp_path, "HC ER LWBS W/TESTS PROVIDED,99281,CPT,,outpatient,facility,500.00,250.00\n"
                                "HC ER TYPE I MINIMAL,99281,CPT,,outpatient,facility,999.00,499.50\n"
                                "HC EMERGENCY DEPARTMENT LEVEL 4 VISIT HIGH/URGENT SEVERITY,99284,CPT,,outpatient,facility,5200.00,2600.00\n"
                                "HC ER TRAUMA LVL IV,99284,CPT,,outpatient,facility,10400.00,5200.00\n"
                                "HC EMERGENCY DEPARTMENT LEVEL 5 VISIT HIGH SEVERITY&THREAT FUNC,99285,CPT,,outpatient,facility,7600.00,3800.00\n"
                                "HC ER TYPE CRITICAL LT 30MIN,99285,CPT,,outpatient,facility,9500.00,4750.00\n"
                                "HC ER TRAUMA LVL V ADVANCED,99285,CPT,,outpatient,facility,15200.00,7600.00\n")

    prices = {p["cpt_code"]: p["gross_charge"] for p in price_file_loader.read_list_prices(path)}

    assert prices == {"99281": 999.0, "99284": 5200.0, "99285": 7600.0}


def test_a_lone_trauma_line_is_still_the_only_published_charge(tmp_path):
    path = write_file(tmp_path, "HC ER LEVEL V TRAUMA,99285,CPT,,outpatient,facility,23622.75,11811.38\n")

    prices = price_file_loader.read_list_prices(path)

    assert [(p["cpt_code"], p["gross_charge"]) for p in prices] == [("99285", 23622.75)]


def test_physician_inpatient_and_modifier_rows_are_not_the_er_list_price(tmp_path):
    path = write_file(tmp_path, "PR ED VISIT LEVEL 5,99285,CPT,,outpatient,professional,987.00,493.50\n"
                                "HC ED VISIT LEVEL 5,99285,CPT,25,outpatient,facility,3158.25,1579.13\n"
                                "HC ED VISIT LEVEL 5,99285,CPT,,inpatient,facility,5000.00,2500.00\n"
                                "HC ED VISIT LEVEL 5,99285,CPT,,outpatient,facility,4211.00,2105.50\n"
                                "HC ED VISIT LEVEL 3,99283,CPT,,outpatient,facility,1642.00,821.00\n"
                                "HC ED VISIT LEVEL 3 OBS,99283,CPT,,outpatient,facility,1810.00,905.00\n")

    prices = {p["cpt_code"]: p for p in price_file_loader.read_list_prices(path)}

    assert (prices["99285"]["gross_charge"], prices["99285"]["cash_price"]) == (4211.0, 2105.5)
    assert "99283" not in prices


def test_file_is_not_loaded_onto_a_different_hospital(monkeypatch):
    upsert_hospital_row(RUTHERFORD)
    monkeypatch.setattr(price_file_loader, "download_price_file", lambda url, path: shutil.copy(RUTHERFORD_FILE, path))

    wrong = price_file_loader.fetch_and_load("440053", "SCRIPPS MERCY", RUTHERFORD_URL)
    missing = price_file_loader.fetch_and_load("050077", "SCRIPPS MERCY", RUTHERFORD_URL)

    assert (wrong["status"], missing["status"]) == ("skipped", "skipped")
    assert saved_prices("440053") == {}


def test_failed_download_is_skipped(monkeypatch):
    upsert_hospital_row(RUTHERFORD)

    def refuse(url, path):
        raise OSError("HTTP Error 403: Forbidden")
    monkeypatch.setattr(price_file_loader, "download_price_file", refuse)

    result = price_file_loader.fetch_and_load("440053", "RUTHERFORD", RUTHERFORD_URL)

    assert result["status"] == "skipped" and "403" in result["reason"]


def test_san_diego_load_runs_once_and_grades_only_loaded_hospitals(monkeypatch):
    upsert_hospital_row(RUTHERFORD)
    monkeypatch.setattr(config, "SAN_DIEGO_PRICE_FILES", (("440053", "RUTHERFORD", RUTHERFORD_URL), ("050077", "SCRIPPS MERCY", RUTHERFORD_URL)))
    monkeypatch.setattr(price_file_loader, "download_price_file", lambda url, path: shutil.copy(RUTHERFORD_FILE, path))
    monkeypatch.setattr(price_file_loader, "log_location_mismatches", lambda: None)

    first_run = price_file_loader.load_san_diego_prices_once()

    assert [r["status"] for r in first_run] == ["loaded", "skipped"]
    assert first_run[0]["city"] == "MURFREESBORO" and first_run[0]["billing_grade"] == "N/A"  # one comparable code is too few to grade
    assert price_file_loader.load_san_diego_prices_once() is None


def test_failed_first_attempt_is_not_repeated(monkeypatch):
    def crash(*entry):
        raise RuntimeError("out of disk")
    monkeypatch.setattr(price_file_loader, "fetch_and_load", crash)

    with pytest.raises(RuntimeError):
        price_file_loader.load_san_diego_prices_once()

    assert price_file_loader.load_san_diego_prices_once() is None


def test_regrade_of_one_hospital_leaves_other_grades_alone():
    upsert_hospital_row(RUTHERFORD)
    upsert_hospital_row({"facility_id": "050100", "name": "SHARP MEMORIAL HOSPITAL", "city": "SAN DIEGO", "state": "CA", "zip": "92123"})
    charges = (("99281", 340.0, 68.0), ("99283", 1485.0, 297.0), ("99285", 3865.0, 773.0), ("71046", 360.0, 72.0), ("74177", 1320.0, 264.0))
    with get_db() as db:
        for facility_id in ("440053", "050100"):
            for code, gross, medicare in charges:
                db.execute("INSERT INTO hospital_prices (facility_id, cpt_code, gross_charge, medicare_rate, markup_vs_medicare, data_year) VALUES (?, ?, ?, ?, ?, ?)",
                           (facility_id, code, gross, medicare, gross / medicare, 2026))
        db.execute("INSERT INTO billing_metrics (facility_id, billing_grade, avg_markup_vs_medicare) VALUES ('440053', 'B', 2.4)")

    recompute_billing_metrics(only_facility_ids={"050100"})

    with get_db() as db:
        grades = {r["facility_id"]: r["billing_grade"] for r in db.execute("SELECT facility_id, billing_grade FROM billing_metrics")}
    assert grades == {"440053": "B", "050100": "D"}


def test_page_text_catch_up_rewrites_only_the_san_diego_hospitals_and_runs_once(monkeypatch):
    upsert_hospital_row(RUTHERFORD)
    upsert_hospital_row({"facility_id": "050100", "name": "SHARP MEMORIAL HOSPITAL", "city": "SAN DIEGO", "state": "CA", "zip": "92123"})
    stale = "SHARP MEMORIAL HOSPITAL does not have enough pricing data in their published file for BillKarma to compute a billing grade."
    with get_db() as db:
        db.execute("INSERT INTO billing_metrics (facility_id, billing_grade, avg_markup_vs_medicare, procedures_compared) VALUES ('050100', 'F', 10.21, 31)")
        db.executemany("INSERT INTO hospital_content (facility_id, dispute_tips) VALUES (?, ?)", [("050100", stale), ("440053", "kept as written")])
    monkeypatch.setattr(config, "SAN_DIEGO_PRICE_FILES", (("050100", "SHARP MEMORIAL", RUTHERFORD_URL),))

    assert price_file_loader.refresh_san_diego_page_text_once() == 1
    assert price_file_loader.refresh_san_diego_page_text_once() is None

    with get_db() as db:
        tips = {r["facility_id"]: r["dispute_tips"] for r in db.execute("SELECT facility_id, dispute_tips FROM hospital_content")}
    assert "enough pricing data" not in tips["050100"] and "10.2x" in tips["050100"]
    assert tips["440053"] == "kept as written"


def test_hospital_city_and_state_match_its_cms_record():
    load_cms_general(CMS_GENERAL)

    assert hospitals_off_cms_location(CMS_GENERAL) == []


def test_hospital_saved_under_its_health_systems_city_is_reported():
    load_cms_general(CMS_GENERAL)
    with get_db() as db:
        db.execute("UPDATE hospitals SET city = 'NASHVILLE' WHERE facility_id = '440053'")

    off = hospitals_off_cms_location(CMS_GENERAL)

    assert [(h["facility_id"], h["city"], h["cms_city"], h["cms_state"]) for h in off] == [("440053", "NASHVILLE", "MURFREESBORO", "TN")]


def test_graded_hospital_with_no_cms_record_is_reported():
    upsert_hospital_row({"facility_id": "1234567893", "name": "AdventHealth South Overland Park", "city": "Tampa", "state": "FL", "zip": "33607"})
    with get_db() as db:
        db.execute("INSERT INTO billing_metrics (facility_id, billing_grade, avg_markup_vs_medicare) VALUES ('1234567893', 'C', 4.1)")

    off = hospitals_off_cms_location(CMS_GENERAL)

    assert [(h["facility_id"], h["city"], h["cms_city"]) for h in off] == [("1234567893", "Tampa", None)]
