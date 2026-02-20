from free_pricing import (
    load_target_codes,
    recompute_fair_price_bands,
    refresh_price_observations,
    resolve_fair_price,
)
from db import get_db


def _insert_hospital(db, facility_id: str, name: str, city: str, state: str, zip_code: str) -> None:
    db.execute(
        """
        INSERT INTO hospitals (
            facility_id, name, city, state, zip, slug, state_slug, city_slug
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (facility_id, name, city, state, zip_code, f"{name.lower()}-{facility_id}", state.lower(), city.lower()),
    )


def test_free_price_bands_build_and_zip_resolution():
    with get_db() as db:
        _insert_hospital(db, "100001", "Alpha Hospital", "Miami", "FL", "33101")
        _insert_hospital(db, "100002", "Beta Hospital", "Miami", "FL", "33101")
        _insert_hospital(db, "100003", "Gamma Hospital", "Orlando", "FL", "32801")

        db.execute(
            """
            INSERT INTO hospital_prices (
                facility_id, cpt_code, gross_charge, cash_price, avg_negotiated_rate, medicare_rate, data_year
            ) VALUES
                ('100001', '99285', 4500, 900, 700, 200, 2026),
                ('100002', '99285', 4300, 880, 680, 200, 2026),
                ('100003', '99285', 5000, 950, 760, 200, 2026)
            """
        )

    codes = {"99285"}
    obs = refresh_price_observations(codes=codes, data_year=2026, include_user_bills=False)
    assert obs.inserted_mrf >= 3

    bands = recompute_fair_price_bands(
        codes=codes,
        min_sample_zip=2,
        min_sample_city=2,
        min_sample_state=2,
        min_sample_national=2,
    )
    assert bands.inserted_rows >= 3
    assert bands.zip_rows >= 1
    assert bands.state_rows >= 1
    assert bands.national_rows >= 1

    zip_row = resolve_fair_price("99285", zip_code="33101", state="FL")
    assert zip_row is not None
    assert zip_row["geo_scope"] == "zip"
    assert zip_row["sample_size"] >= 2


def test_free_price_fallback_to_state_then_national():
    with get_db() as db:
        _insert_hospital(db, "200001", "Delta Hospital", "Tampa", "FL", "33602")
        _insert_hospital(db, "300001", "Echo Hospital", "Houston", "TX", "77002")

        db.execute(
            """
            INSERT INTO hospital_prices (
                facility_id, cpt_code, gross_charge, cash_price, avg_negotiated_rate, medicare_rate, data_year
            ) VALUES
                ('200001', '71046', 1200, 300, 240, 90, 2026),
                ('300001', '71046', 1300, 320, 260, 90, 2026)
            """
        )

    codes = {"71046"}
    refresh_price_observations(codes=codes, data_year=2026, include_user_bills=False)
    recompute_fair_price_bands(
        codes=codes,
        min_sample_zip=2,     # prevent zip rows
        min_sample_city=2,    # prevent city rows
        min_sample_state=1,   # allow state rows
        min_sample_national=2,
    )

    state_row = resolve_fair_price("71046", zip_code="99999", state="FL")
    assert state_row is not None
    assert state_row["geo_scope"] == "state"

    national_row = resolve_fair_price("71046", zip_code="99999")
    assert national_row is not None
    assert national_row["geo_scope"] == "national"


def test_load_target_codes_fallback_non_empty():
    codes = load_target_codes(path="data/config/shoppable_codes_top50.txt", limit=50)
    assert len(codes) >= 40
    assert "99285" in codes
