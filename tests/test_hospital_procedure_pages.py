"""Hospital x procedure pages: one hospital's charge for one CPT code."""

from tests.test_hospital_pages import _seed_hospital, client  # noqa: F401  (sets up app + in-memory DB)

import config
from db import get_db
from hospital_procedure_pages import get_hospital_procedure_page, get_hospital_procedure_sitemap_paths
from hospital_seo import upsert_hospital_row

HOSPITAL_PATH = "/hospitals/fl/hollywood/memorial-regional-hospital-hollywood"


def _seed_cheaper_hospital():
    upsert_hospital_row(
        {"facility_id": "10002", "name": "Baptist Health Plantation", "city": "Plantation", "state": "FL",
         "slug": "baptist-health-plantation", "ownership": "Voluntary non-profit"}
    )
    with get_db() as db:
        db.execute(
            "INSERT INTO hospital_prices (facility_id, cpt_code, description, gross_charge, cash_price, "
            "medicare_rate, markup_vs_medicare, data_year) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ("010002", "99285", "ER visit level 5", 1500.0, 900.0, 227.0, 6.61, 2026),
        )


def _seed_price():
    _seed_hospital()


def test_procedure_page_shows_charge_fair_price_and_cheaper_alternative():
    _seed_price()
    _seed_cheaper_hospital()
    response = client.get(f"{HOSPITAL_PATH}/99285/")
    assert response.status_code == 200
    html = response.text
    assert "$2,800.00" in html
    assert "$681.00" in html  # 3x the $227 Medicare rate
    assert "Baptist Health Plantation" in html
    assert 'application/ld+json' in html


def test_procedure_data_computes_amount_above_fair_price():
    _seed_price()
    page = get_hospital_procedure_page("fl", "hollywood", "memorial-regional-hospital-hollywood", "99285")
    assert page["price"]["above_fair"] == 2119.0
    assert page["canonical_url"].endswith(f"{HOSPITAL_PATH}/99285/")


def test_procedure_page_404_for_unknown_code_and_hospital():
    _seed_price()
    assert client.get(f"{HOSPITAL_PATH}/00000/").status_code == 404
    assert client.get("/hospitals/fl/hollywood/no-such-hospital/99285/").status_code == 404


def test_sitemap_lists_only_widely_priced_codes(monkeypatch):
    _seed_price()
    assert get_hospital_procedure_sitemap_paths() == []
    monkeypatch.setattr(config, "HOSPITAL_PROCEDURE_MIN_HOSPITALS", 1)
    assert f"{HOSPITAL_PATH}/99285/" in get_hospital_procedure_sitemap_paths()
    assert f"{HOSPITAL_PATH}/99285/" in client.get("/sitemap-hospital-procedures.xml").text
    assert "sitemap-hospital-procedures.xml" in client.get("/sitemap.xml").text


def test_rare_code_is_noindex_and_title_uses_plain_name(monkeypatch):
    _seed_price()
    html = client.get(f"{HOSPITAL_PATH}/99285/").text
    assert 'content="noindex, follow"' in html
    monkeypatch.setattr(config, "HOSPITAL_PROCEDURE_MIN_HOSPITALS", 1)
    assert 'content="noindex' not in client.get(f"{HOSPITAL_PATH}/99285/").text
