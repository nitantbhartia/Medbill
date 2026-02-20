"""Tests for data_refresh — health check and CSV loading."""

import os
import tempfile

from data_refresh import (
    refresh_asc_rates,
    data_health_check,
    refresh_medicare_rates,
    refresh_ncci_edits,
    refresh_zip_localities,
)
from db import get_db


class TestDataHealthCheck:
    def test_seeded_db_passes_medicare(self):
        result = data_health_check()
        assert result["checks"]["medicare_rates"]["passed"] is True

    def test_empty_hospital_profiles_fails(self):
        result = data_health_check()
        assert result["checks"]["hospital_profiles"]["passed"] is False
        assert "hospital_profiles" in result["stale_sources"]


class TestRefreshMedicareRates:
    def test_load_csv(self):
        csv_content = (
            "HCPCS,DESCRIPTION,LOCALITY,STATE,NON_FACILITY_RATE,FACILITY_RATE,EFFECTIVE_YEAR\n"
            "99999,Test procedure,0000000,FL,100.00,80.00,2026\n"
            "99998,Another test,0000000,FL,200.00,150.00,2026\n"
        )
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write(csv_content)
            f.flush()
            path = f.name

        try:
            count = refresh_medicare_rates(path)
            assert count == 2

            with get_db() as db:
                row = db.execute(
                    "SELECT facility_rate FROM medicare_rates WHERE cpt_code = '99999'"
                ).fetchone()
                assert row["facility_rate"] == 80.00
        finally:
            os.unlink(path)


class TestRefreshNcciEdits:
    def test_load_csv(self):
        csv_content = (
            "COLUMN_1,COLUMN_2,EFFECTIVE_DATE,DELETION_DATE,MODIFIER_INDICATOR\n"
            "99999,99998,2026-01-01,,1\n"
        )
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write(csv_content)
            f.flush()
            path = f.name

        try:
            count = refresh_ncci_edits(path)
            assert count == 1

            with get_db() as db:
                row = db.execute(
                    "SELECT modifier_indicator FROM ncci_edits "
                    "WHERE column_1_code = '99999' AND column_2_code = '99998'"
                ).fetchone()
                assert row["modifier_indicator"] == "1"
        finally:
            os.unlink(path)


class TestRefreshZipLocalities:
    def test_load_csv(self):
        csv_content = (
            "ZIP_PREFIX,LOCALITY,STATE,REGION\n"
            "33021,0000000,FL,southeast\n"
        )
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write(csv_content)
            f.flush()
            path = f.name

        try:
            count = refresh_zip_localities(path)
            assert count == 1

            with get_db() as db:
                row = db.execute(
                    "SELECT region FROM zip_locality_map WHERE zip_prefix = '33021'"
                ).fetchone()
                assert row["region"] == "southeast"
        finally:
            os.unlink(path)


class TestRefreshAscRates:
    def test_load_csv(self):
        csv_content = (
            "HCPCS,SHORT_DESCRIPTOR,ASC_PAYMENT_RATE,EFFECTIVE_YEAR,FACILITY_INDICATOR\n"
            "45378,DIAGNOSTIC COLONOSCOPY,164.00,2026,Y\n"
            "99900,NONCOVERED TEST,10.00,2026,N\n"
        )
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write(csv_content)
            f.flush()
            path = f.name

        try:
            count = refresh_asc_rates(path)
            assert count == 2
            with get_db() as db:
                row = db.execute(
                    "SELECT medicare_asc_rate, is_covered_asc_procedure FROM asc_medicare_rates WHERE cpt_code = '45378'"
                ).fetchone()
                assert row["medicare_asc_rate"] == 164.00
                assert row["is_covered_asc_procedure"] == 1
                row2 = db.execute(
                    "SELECT is_covered_asc_procedure FROM asc_medicare_rates WHERE cpt_code = '99900'"
                ).fetchone()
                assert row2["is_covered_asc_procedure"] == 0
        finally:
            os.unlink(path)
