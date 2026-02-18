"""Tests for db module — schema initialization and basic operations."""

from db import get_db, init_db


class TestDatabaseInit:
    def test_tables_created(self):
        expected_tables = [
            "users", "bills", "line_items", "findings", "medicare_rates",
            "hospital_opps_rates", "ncci_edits", "hospital_profiles",
            "dispute_outcomes", "procedure_benchmarks", "public_stories",
            "negotiations", "negotiation_messages", "articles",
            "zip_locality_map",
            "consent_logs", "audit_logs",
            "hospital_directory", "hospital_quality", "hospital_financials",
            "hospital_procedure_prices",
            "hospitals", "hcahps_scores", "transparency_files",
            "hospital_prices", "billing_metrics", "benchmark_averages",
            "hospital_content", "data_refresh_log",
        ]
        with get_db() as db:
            rows = db.execute(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
            ).fetchall()
            table_names = [r["name"] for r in rows]

        for table in expected_tables:
            assert table in table_names, f"Missing table: {table}"

    def test_indexes_created(self):
        expected_indexes = [
            "idx_line_items_bill", "idx_line_items_cpt", "idx_findings_bill",
            "idx_medicare_cpt", "idx_hospital_state", "idx_hospital_city",
            "idx_neg_bill", "idx_neg_status", "idx_neg_msg",
            "idx_zip_locality_state",
            "idx_consent_bill", "idx_audit_bill",
            "idx_hospital_directory_slug", "idx_hospital_directory_state",
            "idx_hospital_prices_facility", "idx_hospital_prices_cpt",
            "idx_hospitals_slug_scope", "idx_hospitals_state", "idx_hospitals_city_state",
            "idx_transparency_status", "idx_hospital_prices2_facility",
            "idx_hospital_prices2_cpt", "idx_benchmark_scope",
        ]
        with get_db() as db:
            rows = db.execute(
                "SELECT name FROM sqlite_master WHERE type='index' ORDER BY name"
            ).fetchall()
            index_names = [r["name"] for r in rows]

        for idx in expected_indexes:
            assert idx in index_names, f"Missing index: {idx}"

    def test_foreign_keys_on(self):
        with get_db() as db:
            row = db.execute("PRAGMA foreign_keys").fetchone()
            assert row[0] == 1

    def test_wal_mode(self):
        with get_db() as db:
            row = db.execute("PRAGMA journal_mode").fetchone()
            # In-memory databases report "memory" instead of "wal"
            assert row[0] in ("wal", "memory")

    def test_insert_and_query_user(self):
        with get_db() as db:
            db.execute(
                "INSERT INTO users (email, zip_code, state) VALUES (?, ?, ?)",
                ("test@db.com", "33021", "FL"),
            )
            row = db.execute("SELECT * FROM users WHERE email = ?", ("test@db.com",)).fetchone()
        assert row["zip_code"] == "33021"
        assert row["state"] == "FL"

    def test_row_factory(self):
        with get_db() as db:
            db.execute(
                "INSERT INTO users (email, zip_code) VALUES (?, ?)",
                ("row_test@db.com", "90210"),
            )
            row = db.execute("SELECT * FROM users WHERE email = ?", ("row_test@db.com",)).fetchone()
        # Should be accessible by column name
        assert row["email"] == "row_test@db.com"


class TestSeedData:
    def test_medicare_rates_seeded(self):
        with get_db() as db:
            row = db.execute("SELECT COUNT(*) as cnt FROM medicare_rates").fetchone()
        assert row["cnt"] > 0

    def test_ncci_edits_seeded(self):
        with get_db() as db:
            row = db.execute("SELECT COUNT(*) as cnt FROM ncci_edits").fetchone()
        assert row["cnt"] > 0

    def test_known_rate_present(self):
        with get_db() as db:
            row = db.execute(
                "SELECT facility_rate FROM medicare_rates WHERE cpt_code = '99285'"
            ).fetchone()
        assert row["facility_rate"] == 227.00

    def test_known_ncci_edit_present(self):
        with get_db() as db:
            row = db.execute(
                "SELECT modifier_indicator FROM ncci_edits "
                "WHERE column_1_code = '80053' AND column_2_code = '80048'"
            ).fetchone()
        assert row["modifier_indicator"] == "0"
