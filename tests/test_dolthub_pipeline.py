"""Integration tests for DoltHub pricing fallback pipeline internals."""

from __future__ import annotations

import sqlite3
from pathlib import Path

import config
import db as _db
from hospital_seo import upsert_hospital_row
from scripts import load_pricing_from_dolthub as dolt_loader


def test_load_prices_for_matches_persists_crosswalk_and_parse_status(monkeypatch, tmp_path):
    db_path = Path(tmp_path) / "dolthub_pipeline.db"
    old_db_path = config.DB_PATH
    config.DB_PATH = str(db_path)
    _db._connection = None
    try:
        _db.init_db()

        upsert_hospital_row(
            {
                "facility_id": "99111",
                "name": "Pipeline Test Hospital",
                "address": "10 Test Ave",
                "city": "Miami",
                "state": "FL",
                "zip": "33101",
                "slug": "pipeline-test-hospital-miami",
                "lat": 25.7617,
                "lon": -80.1918,
            }
        )

        # Ensure this code gets a benchmark so markup can be calculated.
        with sqlite3.connect(config.DB_PATH) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO medicare_rates (
                    cpt_code, description, locality, state, non_facility_rate, facility_rate, effective_year
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                ("99285", "ED visit level 5", "0000000", None, 227.0, 227.0, 2026),
            )
            conn.commit()

        def _fake_api_query(sql: str, retries: int = 3):
            if "FROM prices" in sql:
                return [
                    {"npi_number": "1234567890", "code": "99285", "payer": "gross charge", "price": "2400.00"},
                    {"npi_number": "1234567890", "code": "99285", "payer": "cash", "price": "800.00"},
                ]
            return []

        monkeypatch.setattr(dolt_loader, "api_query", _fake_api_query)

        matches = {
            "099111": {
                "npi": "1234567890",
                "method": "exact_name_city_state",
                "confidence": 1.0,
            }
        }
        out = dolt_loader.load_prices_for_matches(matches, year=2026)
        assert out["rows"] == 1
        assert out["facilities"] == 1

        with sqlite3.connect(config.DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cross = conn.execute(
                """
                SELECT source_name, source_entity_id, facility_id, match_method, match_confidence
                FROM data_source_crosswalk
                WHERE source_name = 'dolthub_hospital_price_transparency'
                  AND source_entity_id = '1234567890'
                """
            ).fetchone()
            assert cross is not None
            assert cross["facility_id"] == "099111"
            assert cross["match_method"] == "exact_name_city_state"
            assert round(float(cross["match_confidence"]), 2) == 1.0

            tf = conn.execute(
                "SELECT parse_status FROM transparency_files WHERE facility_id = '099111'"
            ).fetchone()
            assert tf is not None
            assert tf["parse_status"] == "parsed"
    finally:
        if _db._connection:
            _db._connection.close()
        _db._connection = None
        config.DB_PATH = old_db_path
