import sqlite3
import os
from contextlib import contextmanager

import config

_connection = None


def get_connection() -> sqlite3.Connection:
    global _connection
    if _connection is None:
        db_dir = os.path.dirname(config.DB_PATH)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)
        _connection = sqlite3.connect(config.DB_PATH, check_same_thread=False)
        _connection.row_factory = sqlite3.Row
        _connection.execute("PRAGMA journal_mode=WAL")
        _connection.execute("PRAGMA foreign_keys=ON")
    return _connection


@contextmanager
def get_db():
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise


def init_db():
    with get_db() as db:
        db.executescript(SCHEMA)
        _run_migrations(db)


def _run_migrations(db):
    """Add columns that may be missing from older databases."""
    def ensure_columns(table_name: str, required: dict[str, str]) -> None:
        existing_cols = {row[1] for row in db.execute(f"PRAGMA table_info({table_name})").fetchall()}
        for col, col_type in required.items():
            if col not in existing_cols:
                db.execute(f"ALTER TABLE {table_name} ADD COLUMN {col} {col_type}")

    existing = {row[1] for row in db.execute("PRAGMA table_info(bills)").fetchall()}
    if "zip_code" not in existing:
        db.execute("ALTER TABLE bills ADD COLUMN zip_code TEXT")
    ensure_columns(
        "findings",
        {
            "rule_id": "TEXT",
            "confidence": "TEXT",
            "evidence_source": "TEXT",
            "evidence_json": "TEXT",
        },
    )
    ensure_columns("hospitals", {"lat": "REAL", "lon": "REAL"})
    ensure_columns(
        "hospitals",
        {
            "facility_type": "TEXT",
            "accepts_medicare": "INTEGER",
            "accepts_medicaid": "INTEGER",
            "is_hospital_owned": "INTEGER DEFAULT 0",
        },
    )

    # ZIP code centroid coordinates (for procedure hospital finder)
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS zip_latlon (
            zip TEXT PRIMARY KEY,
            lat REAL NOT NULL,
            lon REAL NOT NULL,
            state TEXT,
            city TEXT
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_zip_latlon_state ON zip_latlon(state)")

    # Geo mapping table (for ZIP -> Medicare locality/region)
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS zip_locality_map (
            zip_prefix TEXT PRIMARY KEY,
            locality TEXT,
            state TEXT,
            region TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute(
        "CREATE INDEX IF NOT EXISTS idx_zip_locality_state ON zip_locality_map(state)"
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS consent_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER REFERENCES users(id),
            bill_id INTEGER REFERENCES bills(id),
            consent_type TEXT NOT NULL,
            consent_version TEXT NOT NULL,
            ip_address TEXT,
            user_agent TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER REFERENCES users(id),
            bill_id INTEGER REFERENCES bills(id),
            action TEXT NOT NULL,
            resource_type TEXT NOT NULL,
            resource_id TEXT,
            metadata TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_audit_bill ON audit_logs(bill_id)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_consent_bill ON consent_logs(bill_id)")
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS hospital_directory (
            facility_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT,
            city TEXT,
            state TEXT,
            state_slug TEXT,
            zip TEXT,
            county TEXT,
            phone TEXT,
            hospital_type TEXT,
            ownership TEXT,
            emergency_services TEXT,
            overall_rating INTEGER,
            bed_count INTEGER,
            teaching_status TEXT,
            system_affiliation TEXT,
            slug TEXT,
            last_updated DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_hospital_directory_slug ON hospital_directory(state_slug, slug)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_hospital_directory_state ON hospital_directory(state_slug)")
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS hospital_quality (
            facility_id TEXT PRIMARY KEY REFERENCES hospital_directory(facility_id),
            hcahps_summary TEXT,
            patient_experience_score REAL,
            readmission_score REAL,
            mortality_score REAL,
            updated_at DATE
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS hospital_financials (
            facility_id TEXT PRIMARY KEY REFERENCES hospital_directory(facility_id),
            total_charges REAL,
            total_revenue REAL,
            cost_to_charge_ratio REAL,
            charity_care_amount REAL,
            charity_care_pct REAL,
            nonprofit_status INTEGER,
            has_financial_assistance_policy INTEGER,
            financial_assistance_url TEXT,
            irs_990_url TEXT,
            updated_at DATE
        )
        """
    )
    ensure_columns(
        "hospital_financials",
        {
            "net_patient_revenue": "REAL",
            "charity_care_charges": "REAL",
            "charity_care_costs": "REAL",
            "charity_care_pct_revenue": "REAL",
            "bad_debt": "REAL",
            "operating_margin": "REAL",
            "has_financial_assistance": "INTEGER",
            "fa_income_threshold": "TEXT",
            "fa_application_url": "TEXT",
            "ein": "TEXT",
            "cost_report_year": "INTEGER",
        },
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS hospital_procedure_prices (
            facility_id TEXT REFERENCES hospital_directory(facility_id),
            cpt_code TEXT,
            description TEXT,
            gross_charge REAL,
            cash_price REAL,
            medicare_rate REAL,
            avg_negotiated_rate REAL,
            min_negotiated_rate REAL,
            max_negotiated_rate REAL,
            state_avg_rate REAL,
            last_updated DATE,
            PRIMARY KEY (facility_id, cpt_code)
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_hospital_prices_facility ON hospital_procedure_prices(facility_id)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_hospital_prices_cpt ON hospital_procedure_prices(cpt_code)")
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS hospitals (
            facility_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            zip TEXT,
            county TEXT,
            phone TEXT,
            hospital_type TEXT,
            ownership TEXT,
            is_nonprofit INTEGER,
            emergency_services INTEGER,
            bed_count INTEGER,
            teaching_status TEXT,
            system_affiliation TEXT,
            cms_star_rating INTEGER,
            slug TEXT NOT NULL,
            state_slug TEXT NOT NULL,
            city_slug TEXT NOT NULL,
            cms_data_updated DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_hospitals_slug_scope ON hospitals(state_slug, city_slug, slug)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_hospitals_state ON hospitals(state)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_hospitals_city_state ON hospitals(city, state)")
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS hcahps_scores (
            facility_id TEXT PRIMARY KEY REFERENCES hospitals(facility_id),
            overall_rating_pct_9_10 REAL,
            overall_rating_pct_7_8 REAL,
            overall_rating_pct_1_6 REAL,
            recommend_yes REAL,
            doctor_communication_top REAL,
            nurse_communication_top REAL,
            staff_responsiveness_top REAL,
            medicine_communication_top REAL,
            discharge_info_top REAL,
            care_transition_top REAL,
            hospital_cleanliness_top REAL,
            hospital_quietness_top REAL,
            survey_response_count INTEGER,
            survey_period TEXT,
            data_updated DATE
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS transparency_files (
            facility_id TEXT PRIMARY KEY REFERENCES hospitals(facility_id),
            file_url TEXT,
            file_format TEXT,
            file_size_mb REAL,
            has_standard_codes INTEGER,
            parse_status TEXT,
            row_count INTEGER,
            procedures_extracted INTEGER,
            last_downloaded DATE,
            last_parsed DATE,
            parse_notes TEXT
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_transparency_status ON transparency_files(parse_status)")
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS transparency_parse_results (
            facility_id TEXT PRIMARY KEY,
            facility_type TEXT NOT NULL DEFAULT 'hospital',
            file_url TEXT,
            file_format TEXT,
            file_size_mb REAL,
            has_standard_codes INTEGER,
            parse_status TEXT,
            row_count INTEGER,
            procedures_extracted INTEGER,
            last_downloaded DATE,
            last_parsed DATE,
            parse_notes TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute(
        "CREATE INDEX IF NOT EXISTS idx_parse_results_type_status ON transparency_parse_results(facility_type, parse_status)"
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS hospital_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            facility_id TEXT REFERENCES hospitals(facility_id),
            cpt_code TEXT NOT NULL,
            description TEXT,
            gross_charge REAL,
            cash_price REAL,
            min_negotiated_rate REAL,
            max_negotiated_rate REAL,
            avg_negotiated_rate REAL,
            medicare_rate REAL,
            markup_vs_medicare REAL,
            data_year INTEGER,
            UNIQUE(facility_id, cpt_code, data_year)
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_hospital_prices2_facility ON hospital_prices(facility_id)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_hospital_prices2_cpt ON hospital_prices(cpt_code)")
    ensure_columns(
        "hospital_prices",
        {
            "facility_type": "TEXT",
            "medicare_benchmark_type": "TEXT",
            "medicare_benchmark_rate": "REAL",
        },
    )
    db.execute(
        "CREATE INDEX IF NOT EXISTS idx_proc_prices_facility_type ON hospital_prices(facility_type, cpt_code)"
    )
    db.execute("UPDATE hospital_prices SET facility_type = 'hospital' WHERE facility_type IS NULL OR TRIM(facility_type) = ''")
    db.execute(
        """
        UPDATE hospital_prices
        SET medicare_benchmark_type = COALESCE(medicare_benchmark_type, 'opps'),
            medicare_benchmark_rate = COALESCE(medicare_benchmark_rate, medicare_rate)
        WHERE facility_type = 'hospital'
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS procedure_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            facility_id TEXT NOT NULL,
            cpt_code TEXT NOT NULL,
            description TEXT,
            gross_charge REAL,
            cash_price REAL,
            min_negotiated_rate REAL,
            max_negotiated_rate REAL,
            avg_negotiated_rate REAL,
            medicare_rate REAL,
            markup_vs_medicare REAL,
            data_year INTEGER,
            facility_type TEXT,
            medicare_benchmark_type TEXT,
            medicare_benchmark_rate REAL,
            UNIQUE(facility_id, cpt_code, data_year)
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_proc_prices_facility ON procedure_prices(facility_id)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_proc_prices_cpt ON procedure_prices(cpt_code)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_proc_prices_type_cpt ON procedure_prices(facility_type, cpt_code)")
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS billing_metrics (
            facility_id TEXT PRIMARY KEY REFERENCES hospitals(facility_id),
            avg_markup_vs_medicare REAL,
            median_markup_vs_medicare REAL,
            max_markup_vs_medicare REAL,
            procedures_compared INTEGER,
            cash_discount_avg_pct REAL,
            billing_grade TEXT,
            state_rank INTEGER,
            national_percentile INTEGER,
            computed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS benchmark_averages (
            scope TEXT NOT NULL,
            cpt_code TEXT NOT NULL,
            avg_gross_charge REAL,
            avg_cash_price REAL,
            avg_markup_vs_medicare REAL,
            hospital_count INTEGER,
            computed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (scope, cpt_code)
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_benchmark_scope ON benchmark_averages(scope)")

    db.execute(
        """
        CREATE TABLE IF NOT EXISTS facilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            facility_id TEXT UNIQUE,
            name TEXT NOT NULL,
            address TEXT,
            city TEXT,
            state TEXT,
            state_slug TEXT,
            city_slug TEXT,
            zip TEXT,
            county TEXT,
            phone TEXT,
            facility_type TEXT NOT NULL DEFAULT 'hospital',
            ownership_type TEXT,
            ownership_subtype TEXT,
            ownership_code TEXT,
            accepts_medicare INTEGER,
            accepts_medicaid INTEGER,
            is_hospital_owned INTEGER DEFAULT 0,
            parent_hospital_id INTEGER REFERENCES facilities(id),
            parent_system TEXT,
            system_affiliation TEXT,
            asc_specialties TEXT,
            imaging_modalities TEXT,
            lat REAL,
            lon REAL,
            slug TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            CHECK (facility_type IN ('hospital', 'asc', 'imaging_center', 'urgent_care', 'lab'))
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_facilities_type ON facilities(facility_type)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_facilities_type_state ON facilities(facility_type, state)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_facilities_location ON facilities(state_slug, city_slug, slug)")

    db.execute(
        """
        CREATE TABLE IF NOT EXISTS asc_medicare_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpt_code TEXT NOT NULL,
            description TEXT,
            medicare_asc_rate REAL,
            effective_year INTEGER,
            is_covered_asc_procedure INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_asc_rates_cpt ON asc_medicare_rates(cpt_code, effective_year)")

    db.execute(
        """
        CREATE TABLE IF NOT EXISTS facility_billing_metrics (
            facility_id TEXT PRIMARY KEY,
            facility_type TEXT NOT NULL,
            avg_markup REAL,
            median_markup REAL,
            max_markup REAL,
            procedures_compared INTEGER,
            billing_grade TEXT,
            benchmark_type TEXT,
            computed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_facility_metrics_type ON facility_billing_metrics(facility_type)")
    db.execute(
        """
        INSERT OR IGNORE INTO facility_billing_metrics (
            facility_id, facility_type, avg_markup, median_markup, max_markup,
            procedures_compared, billing_grade, benchmark_type, computed_at
        )
        SELECT
            bm.facility_id,
            'hospital',
            bm.avg_markup_vs_medicare,
            bm.median_markup_vs_medicare,
            bm.max_markup_vs_medicare,
            bm.procedures_compared,
            bm.billing_grade,
            'opps',
            bm.computed_at
        FROM billing_metrics bm
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS hospital_content (
            facility_id TEXT PRIMARY KEY REFERENCES hospitals(facility_id),
            dispute_tips TEXT,
            meta_description TEXT,
            structured_data_json TEXT,
            generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            model_used TEXT
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS data_refresh_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL,
            refresh_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            records_updated INTEGER,
            status TEXT,
            notes TEXT
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS price_observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_type TEXT NOT NULL,              -- mrf | user_bill | public_extract
            source_ref TEXT NOT NULL,               -- stable source key to dedupe reloads
            code_type TEXT NOT NULL DEFAULT 'CPT',
            code TEXT NOT NULL,
            facility_id TEXT,
            payer TEXT,
            plan_name TEXT,
            place_of_service TEXT,
            geo_zip5 TEXT,
            geo_city TEXT,
            geo_state TEXT,
            billed_amount REAL,
            allowed_amount REAL,
            cash_price REAL,
            gross_charge REAL,
            medicare_rate REAL,
            event_date DATE,
            effective_year INTEGER,
            confidence REAL DEFAULT 0.5,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(source_type, source_ref)
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_price_obs_code ON price_observations(code)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_price_obs_geo_zip ON price_observations(geo_zip5)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_price_obs_geo_state ON price_observations(geo_state)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_price_obs_source ON price_observations(source_type)")
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS fair_price_bands (
            geo_scope TEXT NOT NULL,                -- zip | city | state | national
            geo_value TEXT NOT NULL,                -- zip: 33101, city: MIAMI|FL, state: FL, national: US
            code_type TEXT NOT NULL DEFAULT 'CPT',
            code TEXT NOT NULL,
            sample_size INTEGER NOT NULL,
            p25 REAL,
            p50 REAL,
            p75 REAL,
            p90 REAL,
            confidence_mean REAL,
            method TEXT NOT NULL DEFAULT 'no_api_v1',
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (geo_scope, geo_value, code_type, code, method)
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_fair_bands_code ON fair_price_bands(code)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_fair_bands_geo ON fair_price_bands(geo_scope, geo_value)")
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS data_source_crosswalk (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_name TEXT NOT NULL,
            source_entity_id TEXT NOT NULL,
            facility_id TEXT NOT NULL,
            match_method TEXT,
            match_confidence REAL,
            last_verified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(source_name, source_entity_id)
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_crosswalk_facility ON data_source_crosswalk(facility_id)")
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS data_quality_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status TEXT NOT NULL,
            coverage_json TEXT,
            checks_json TEXT,
            notes TEXT
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_quality_runs_date ON data_quality_runs(run_date)")
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS dispute_claims (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bill_id INTEGER NOT NULL REFERENCES bills(id),
            user_id INTEGER REFERENCES users(id),
            current_status TEXT NOT NULL DEFAULT 'drafted',
            channel TEXT DEFAULT 'provider_billing',
            assignee TEXT,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_dispute_claims_bill ON dispute_claims(bill_id)")
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS dispute_claim_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            claim_id INTEGER NOT NULL REFERENCES dispute_claims(id),
            from_status TEXT,
            to_status TEXT NOT NULL,
            event_note TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_dispute_claim_events_claim ON dispute_claim_events(claim_id)")

    # Enrichment fields — Tier 1 (Phase 1)
    ensure_columns(
        "hospitals",
        {
            "ownership_type": "TEXT",
            "ownership_subtype": "TEXT",
            "ownership_code": "TEXT",
            "hospital_size": "TEXT",
            "patient_experience": "TEXT",
            "quality_measures": "TEXT",
            "cms_stars_last_updated": "DATE",
            "enrichment_last_run": "DATE",
            "enrichment_source": "TEXT",
            "enrichment_match_confidence": "TEXT",
            # Tier 2 (Phase 2)
            "charity_care_pct": "REAL",
            "charity_care_reported": "INTEGER",
            "charity_care_report_year": "INTEGER",
            "compliance_status": "TEXT",
            "compliance_last_checked": "DATE",
            "procedures_in_file": "INTEGER",
            "parent_system": "TEXT",
            "is_pe_owned": "INTEGER DEFAULT 0",
            "pe_firm": "TEXT",
            "pe_acquisition_year": "INTEGER",
            "pe_exit_year": "INTEGER",
        },
    )

    # CMS POS enrichment staging table
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS cms_pos_enrichment (
            ccn TEXT PRIMARY KEY,
            fac_name TEXT,
            st_adr TEXT,
            city_name TEXT,
            state_cd TEXT,
            zip_cd TEXT,
            latitude REAL,
            longitude REAL,
            crtfd_bed_cnt INTEGER,
            gnrl_cntl_type_cd TEXT,
            gnrl_fac_type_cd TEXT,
            orgnl_prtcptn_dt TEXT,
            phne_num TEXT,
            loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_cms_pos_state ON cms_pos_enrichment(state_cd)")

    # Hospitals that couldn't be matched to CMS POS data
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS enrichment_unmatched (
            facility_id TEXT PRIMARY KEY,
            name TEXT,
            city TEXT,
            state TEXT,
            reason TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    # Coordinates validation log
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS coordinates_validation (
            facility_id TEXT PRIMARY KEY,
            name TEXT,
            city TEXT,
            state TEXT,
            latitude REAL,
            longitude REAL,
            issue TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    # PE ownership reference data
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS pe_ownership (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hospital_name TEXT,
            ccn TEXT,
            pe_firm TEXT,
            acquisition_year INTEGER,
            exit_year INTEGER,
            current_parent_system TEXT,
            source_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_pe_ownership_ccn ON pe_ownership(ccn)")

    # Enrichment run log
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS enrichment_run_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            hospitals_processed INTEGER,
            ownership_updated INTEGER,
            coordinates_updated INTEGER,
            stars_updated INTEGER,
            ownership_unknown_remaining INTEGER,
            stars_not_rated_remaining INTEGER,
            errors TEXT
        )
        """
    )

    # Enrichment changelog for tracking field changes over time
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS enrichment_changelog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            facility_id TEXT NOT NULL,
            field_name TEXT NOT NULL,
            old_value TEXT,
            new_value TEXT,
            changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_enrichment_changelog_fid ON enrichment_changelog(facility_id)")

    # Unified facilities mirror with discriminator for cross-facility queries.
    db.execute(
        """
        INSERT INTO facilities (
            facility_id, name, address, city, state, state_slug, city_slug, zip,
            county, phone, facility_type, ownership_type, ownership_subtype, ownership_code,
            accepts_medicare, accepts_medicaid, is_hospital_owned, parent_system,
            system_affiliation, lat, lon, slug, updated_at
        )
        SELECT
            h.facility_id,
            h.name,
            h.address,
            h.city,
            h.state,
            h.state_slug,
            h.city_slug,
            h.zip,
            h.county,
            h.phone,
            'hospital',
            h.ownership_type,
            h.ownership_subtype,
            h.ownership_code,
            1,
            NULL,
            0,
            h.parent_system,
            h.system_affiliation,
            h.lat,
            h.lon,
            h.slug,
            CURRENT_TIMESTAMP
        FROM hospitals h
        WHERE h.facility_id IS NOT NULL
        ON CONFLICT(facility_id) DO UPDATE SET
            name=excluded.name,
            address=excluded.address,
            city=excluded.city,
            state=excluded.state,
            state_slug=excluded.state_slug,
            city_slug=excluded.city_slug,
            zip=excluded.zip,
            county=excluded.county,
            phone=excluded.phone,
            facility_type='hospital',
            ownership_type=COALESCE(excluded.ownership_type, facilities.ownership_type),
            ownership_subtype=COALESCE(excluded.ownership_subtype, facilities.ownership_subtype),
            ownership_code=COALESCE(excluded.ownership_code, facilities.ownership_code),
            accepts_medicare=COALESCE(facilities.accepts_medicare, 1),
            parent_system=COALESCE(excluded.parent_system, facilities.parent_system),
            system_affiliation=COALESCE(excluded.system_affiliation, facilities.system_affiliation),
            lat=COALESCE(excluded.lat, facilities.lat),
            lon=COALESCE(excluded.lon, facilities.lon),
            slug=COALESCE(excluded.slug, facilities.slug),
            updated_at=CURRENT_TIMESTAMP
        """
    )

    # Backward-compatible sync to canonical tables.
    db.execute(
        """
        INSERT OR IGNORE INTO hospitals (
            facility_id, name, address, city, state, zip, county, phone, hospital_type,
            ownership, is_nonprofit, emergency_services, bed_count, teaching_status,
            system_affiliation, cms_star_rating, slug, state_slug, city_slug, cms_data_updated
        )
        SELECT
            facility_id, name, address, COALESCE(city, ''), COALESCE(state, ''), zip, county, phone, hospital_type,
            ownership,
            CASE
                WHEN lower(COALESCE(ownership, '')) LIKE '%nonprofit%' THEN 1
                ELSE 0
            END AS is_nonprofit,
            CASE
                WHEN lower(COALESCE(emergency_services, '')) IN ('yes', 'true', '1') THEN 1
                ELSE 0
            END AS emergency_services,
            bed_count, teaching_status, system_affiliation, overall_rating, slug, state_slug,
            lower(replace(COALESCE(city, ''), ' ', '-')) AS city_slug,
            last_updated
        FROM hospital_directory
        WHERE facility_id IS NOT NULL
        """
    )
    db.execute(
        """
        INSERT OR IGNORE INTO hcahps_scores (
            facility_id, recommend_yes, doctor_communication_top, nurse_communication_top,
            staff_responsiveness_top, medicine_communication_top, discharge_info_top,
            care_transition_top, survey_period, data_updated
        )
        SELECT
            facility_id, patient_experience_score, patient_experience_score, patient_experience_score,
            patient_experience_score, patient_experience_score, patient_experience_score,
            patient_experience_score, NULL, updated_at
        FROM hospital_quality
        WHERE facility_id IS NOT NULL
        """
    )
    db.execute(
        """
        INSERT OR IGNORE INTO hospital_prices (
            facility_id, cpt_code, description, gross_charge, cash_price, min_negotiated_rate,
            max_negotiated_rate, avg_negotiated_rate, medicare_rate, markup_vs_medicare, data_year
        )
        SELECT
            facility_id, cpt_code, description, gross_charge, cash_price, min_negotiated_rate,
            max_negotiated_rate, avg_negotiated_rate, medicare_rate,
            CASE WHEN medicare_rate > 0 AND gross_charge IS NOT NULL THEN gross_charge / medicare_rate ELSE NULL END,
            CAST(substr(COALESCE(last_updated, ''), 1, 4) AS INTEGER)
        FROM hospital_procedure_prices
        WHERE facility_id IS NOT NULL AND cpt_code IS NOT NULL
        """
    )

    # Concierge interest queue (success-fee prompt captures)
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS concierge_interest (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            disputed_amount REAL,
            bill_context TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.execute("CREATE INDEX IF NOT EXISTS idx_concierge_created ON concierge_interest(created_at)")

    # Additional fields for richer dispute tracking
    ensure_columns(
        "dispute_outcomes",
        {
            "dispute_stage": "TEXT",
            "days_to_resolution": "INTEGER",
        },
    )


SCHEMA = """
-- Users
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    zip_code TEXT,
    state TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Scanned bills
CREATE TABLE IF NOT EXISTS bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    provider_name TEXT,
    provider_address TEXT,
    bill_date DATE,
    zip_code TEXT,
    total_charged REAL,
    total_patient_owes REAL,
    total_findings INTEGER DEFAULT 0,
    total_potential_savings REAL DEFAULT 0,
    status TEXT DEFAULT 'scanned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Extracted line items
CREATE TABLE IF NOT EXISTS line_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER REFERENCES bills(id),
    date_of_service DATE,
    cpt_code TEXT,
    description TEXT,
    quantity INTEGER DEFAULT 1,
    charged_amount REAL,
    insurance_paid REAL,
    insurance_adjustment REAL,
    patient_responsibility REAL,
    medicare_rate REAL,
    markup_multiple REAL,
    extraction_confidence TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_line_items_bill ON line_items(bill_id);
CREATE INDEX IF NOT EXISTS idx_line_items_cpt ON line_items(cpt_code);

-- Analysis findings
CREATE TABLE IF NOT EXISTS findings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER REFERENCES bills(id),
    line_item_id INTEGER REFERENCES line_items(id),
    finding_type TEXT,
    rule_id TEXT,
    severity TEXT,
    confidence TEXT,
    evidence_source TEXT,
    evidence_json TEXT,
    potential_savings REAL,
    message TEXT,
    details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_findings_bill ON findings(bill_id);

-- Medicare rates
CREATE TABLE IF NOT EXISTS medicare_rates (
    cpt_code TEXT NOT NULL,
    description TEXT,
    locality TEXT NOT NULL,
    state TEXT,
    non_facility_rate REAL,
    facility_rate REAL,
    effective_year INTEGER,
    PRIMARY KEY (cpt_code, locality, effective_year)
);

CREATE INDEX IF NOT EXISTS idx_medicare_cpt ON medicare_rates(cpt_code);

-- Hospital OPPS rates
CREATE TABLE IF NOT EXISTS hospital_opps_rates (
    cpt_code TEXT NOT NULL,
    apc TEXT,
    description TEXT,
    national_payment_rate REAL,
    effective_year INTEGER,
    PRIMARY KEY (cpt_code, effective_year)
);

-- NCCI unbundling edits
CREATE TABLE IF NOT EXISTS ncci_edits (
    column_1_code TEXT NOT NULL,
    column_2_code TEXT NOT NULL,
    effective_date DATE,
    deletion_date DATE,
    modifier_indicator TEXT,
    PRIMARY KEY (column_1_code, column_2_code, effective_date)
);

-- Hospital profiles
CREATE TABLE IF NOT EXISTS hospital_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cms_provider_id TEXT UNIQUE,
    name TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    avg_markup_vs_medicare REAL,
    total_bills_scanned INTEGER DEFAULT 0,
    pct_with_issues REAL,
    common_issues TEXT,
    billscan_grade TEXT,
    pricing_stars INTEGER,
    accuracy_stars INTEGER,
    responsiveness_stars INTEGER,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_hospital_state ON hospital_profiles(state);
CREATE INDEX IF NOT EXISTS idx_hospital_city ON hospital_profiles(city, state);

-- ZIP to locality/region mapping
CREATE TABLE IF NOT EXISTS zip_locality_map (
    zip_prefix TEXT PRIMARY KEY,
    locality TEXT,
    state TEXT,
    region TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_zip_locality_state ON zip_locality_map(state);

-- Consent logs
CREATE TABLE IF NOT EXISTS consent_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    bill_id INTEGER REFERENCES bills(id),
    consent_type TEXT NOT NULL,
    consent_version TEXT NOT NULL,
    ip_address TEXT,
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_consent_bill ON consent_logs(bill_id);

-- Audit logs
CREATE TABLE IF NOT EXISTS audit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    bill_id INTEGER REFERENCES bills(id),
    action TEXT NOT NULL,
    resource_type TEXT NOT NULL,
    resource_id TEXT,
    metadata TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_audit_bill ON audit_logs(bill_id);

-- Dispute outcomes
CREATE TABLE IF NOT EXISTS dispute_outcomes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER REFERENCES bills(id),
    user_id INTEGER REFERENCES users(id),
    hospital_name TEXT,
    called_billing BOOLEAN,
    outcome TEXT,
    original_patient_owes REAL,
    final_patient_owes REAL,
    actual_savings REAL,
    notes TEXT,
    shared_publicly BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Claim workflow tracking
CREATE TABLE IF NOT EXISTS dispute_claims (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER NOT NULL REFERENCES bills(id),
    user_id INTEGER REFERENCES users(id),
    current_status TEXT NOT NULL DEFAULT 'drafted',
    channel TEXT DEFAULT 'provider_billing',
    assignee TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_dispute_claims_bill ON dispute_claims(bill_id);

CREATE TABLE IF NOT EXISTS dispute_claim_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_id INTEGER NOT NULL REFERENCES dispute_claims(id),
    from_status TEXT,
    to_status TEXT NOT NULL,
    event_note TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_dispute_claim_events_claim ON dispute_claim_events(claim_id);

-- Procedure benchmarks
CREATE TABLE IF NOT EXISTS procedure_benchmarks (
    cpt_code TEXT NOT NULL,
    region TEXT NOT NULL,
    sample_size INTEGER,
    avg_charged REAL,
    median_charged REAL,
    p25_charged REAL,
    p75_charged REAL,
    min_charged REAL,
    max_charged REAL,
    medicare_rate REAL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (cpt_code, region)
);

-- Public stories
CREATE TABLE IF NOT EXISTS public_stories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER REFERENCES bills(id),
    city TEXT,
    state TEXT,
    procedure_summary TEXT,
    total_billed REAL,
    findings_summary TEXT,
    potential_savings REAL,
    actual_savings REAL,
    user_approved BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Negotiations
CREATE TABLE IF NOT EXISTS negotiations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER REFERENCES bills(id),
    user_id INTEGER REFERENCES users(id),
    hospital_name TEXT,
    hospital_email TEXT,
    account_number TEXT,
    status TEXT DEFAULT 'pending_auth',
    current_stage TEXT DEFAULT 'stage_1',
    original_amount REAL,
    current_amount REAL,
    total_savings REAL DEFAULT 0,
    fee_charged REAL DEFAULT 0,
    fee_percentage REAL DEFAULT 0.15,
    fee_cap REAL DEFAULT 500,
    rounds_completed INTEGER DEFAULT 0,
    authorization_signed_at TIMESTAMP,
    card_token TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS negotiation_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    negotiation_id INTEGER REFERENCES negotiations(id),
    direction TEXT NOT NULL,
    stage TEXT,
    subject TEXT,
    body TEXT,
    patient_summary TEXT,
    ai_analysis TEXT,
    user_approved BOOLEAN DEFAULT 0,
    approved_at TIMESTAMP,
    sent_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_neg_bill ON negotiations(bill_id);
CREATE INDEX IF NOT EXISTS idx_neg_status ON negotiations(status);
CREATE INDEX IF NOT EXISTS idx_neg_msg ON negotiation_messages(negotiation_id);

-- Articles (content engine)
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    slug TEXT UNIQUE,
    target_keyword TEXT,
    status TEXT NOT NULL DEFAULT 'backlog',
    markdown_content TEXT,
    meta_title TEXT,
    meta_description TEXT,
    validation_status TEXT,
    seo_score INTEGER,
    readability_score REAL,
    published_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- SEO hospital directory
CREATE TABLE IF NOT EXISTS hospital_directory (
    facility_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    state_slug TEXT,
    zip TEXT,
    county TEXT,
    phone TEXT,
    hospital_type TEXT,
    ownership TEXT,
    emergency_services TEXT,
    overall_rating INTEGER,
    bed_count INTEGER,
    teaching_status TEXT,
    system_affiliation TEXT,
    slug TEXT,
    last_updated DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_hospital_directory_slug ON hospital_directory(state_slug, slug);
CREATE INDEX IF NOT EXISTS idx_hospital_directory_state ON hospital_directory(state_slug);

CREATE TABLE IF NOT EXISTS hospital_quality (
    facility_id TEXT PRIMARY KEY REFERENCES hospital_directory(facility_id),
    hcahps_summary TEXT,
    patient_experience_score REAL,
    readmission_score REAL,
    mortality_score REAL,
    updated_at DATE
);

CREATE TABLE IF NOT EXISTS hospital_financials (
    facility_id TEXT PRIMARY KEY REFERENCES hospital_directory(facility_id),
    total_charges REAL,
    total_revenue REAL,
    cost_to_charge_ratio REAL,
    charity_care_amount REAL,
    charity_care_pct REAL,
    nonprofit_status INTEGER,
    has_financial_assistance_policy INTEGER,
    financial_assistance_url TEXT,
    irs_990_url TEXT,
    updated_at DATE
);

CREATE TABLE IF NOT EXISTS hospital_procedure_prices (
    facility_id TEXT REFERENCES hospital_directory(facility_id),
    cpt_code TEXT,
    description TEXT,
    gross_charge REAL,
    cash_price REAL,
    medicare_rate REAL,
    avg_negotiated_rate REAL,
    min_negotiated_rate REAL,
    max_negotiated_rate REAL,
    state_avg_rate REAL,
    last_updated DATE,
    PRIMARY KEY (facility_id, cpt_code)
);

CREATE INDEX IF NOT EXISTS idx_hospital_prices_facility ON hospital_procedure_prices(facility_id);
CREATE INDEX IF NOT EXISTS idx_hospital_prices_cpt ON hospital_procedure_prices(cpt_code);

-- Canonical hospitals table
CREATE TABLE IF NOT EXISTS hospitals (
    facility_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip TEXT,
    county TEXT,
    phone TEXT,
    hospital_type TEXT,
    ownership TEXT,
    is_nonprofit INTEGER,
    emergency_services INTEGER,
    bed_count INTEGER,
    teaching_status TEXT,
    system_affiliation TEXT,
    cms_star_rating INTEGER,
    slug TEXT NOT NULL,
    state_slug TEXT NOT NULL,
    city_slug TEXT NOT NULL,
    cms_data_updated DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_hospitals_slug_scope ON hospitals(state_slug, city_slug, slug);
CREATE INDEX IF NOT EXISTS idx_hospitals_state ON hospitals(state);
CREATE INDEX IF NOT EXISTS idx_hospitals_city_state ON hospitals(city, state);

CREATE TABLE IF NOT EXISTS hcahps_scores (
    facility_id TEXT PRIMARY KEY REFERENCES hospitals(facility_id),
    overall_rating_pct_9_10 REAL,
    overall_rating_pct_7_8 REAL,
    overall_rating_pct_1_6 REAL,
    recommend_yes REAL,
    doctor_communication_top REAL,
    nurse_communication_top REAL,
    staff_responsiveness_top REAL,
    medicine_communication_top REAL,
    discharge_info_top REAL,
    care_transition_top REAL,
    hospital_cleanliness_top REAL,
    hospital_quietness_top REAL,
    survey_response_count INTEGER,
    survey_period TEXT,
    data_updated DATE
);

CREATE TABLE IF NOT EXISTS transparency_files (
    facility_id TEXT PRIMARY KEY REFERENCES hospitals(facility_id),
    file_url TEXT,
    file_format TEXT,
    file_size_mb REAL,
    has_standard_codes INTEGER,
    parse_status TEXT,
    row_count INTEGER,
    procedures_extracted INTEGER,
    last_downloaded DATE,
    last_parsed DATE,
    parse_notes TEXT
);

CREATE INDEX IF NOT EXISTS idx_transparency_status ON transparency_files(parse_status);

CREATE TABLE IF NOT EXISTS hospital_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    facility_id TEXT REFERENCES hospitals(facility_id),
    cpt_code TEXT NOT NULL,
    description TEXT,
    gross_charge REAL,
    cash_price REAL,
    min_negotiated_rate REAL,
    max_negotiated_rate REAL,
    avg_negotiated_rate REAL,
    medicare_rate REAL,
    markup_vs_medicare REAL,
    data_year INTEGER,
    UNIQUE(facility_id, cpt_code, data_year)
);

CREATE INDEX IF NOT EXISTS idx_hospital_prices2_facility ON hospital_prices(facility_id);
CREATE INDEX IF NOT EXISTS idx_hospital_prices2_cpt ON hospital_prices(cpt_code);

CREATE TABLE IF NOT EXISTS billing_metrics (
    facility_id TEXT PRIMARY KEY REFERENCES hospitals(facility_id),
    avg_markup_vs_medicare REAL,
    median_markup_vs_medicare REAL,
    max_markup_vs_medicare REAL,
    procedures_compared INTEGER,
    cash_discount_avg_pct REAL,
    billing_grade TEXT,
    state_rank INTEGER,
    national_percentile INTEGER,
    computed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS benchmark_averages (
    scope TEXT NOT NULL,
    cpt_code TEXT NOT NULL,
    avg_gross_charge REAL,
    avg_cash_price REAL,
    avg_markup_vs_medicare REAL,
    hospital_count INTEGER,
    computed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (scope, cpt_code)
);

CREATE INDEX IF NOT EXISTS idx_benchmark_scope ON benchmark_averages(scope);

CREATE TABLE IF NOT EXISTS hospital_content (
    facility_id TEXT PRIMARY KEY REFERENCES hospitals(facility_id),
    dispute_tips TEXT,
    meta_description TEXT,
    structured_data_json TEXT,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    model_used TEXT
);

CREATE TABLE IF NOT EXISTS data_refresh_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    refresh_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    records_updated INTEGER,
    status TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS price_observations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_type TEXT NOT NULL,
    source_ref TEXT NOT NULL,
    code_type TEXT NOT NULL DEFAULT 'CPT',
    code TEXT NOT NULL,
    facility_id TEXT,
    payer TEXT,
    plan_name TEXT,
    place_of_service TEXT,
    geo_zip5 TEXT,
    geo_city TEXT,
    geo_state TEXT,
    billed_amount REAL,
    allowed_amount REAL,
    cash_price REAL,
    gross_charge REAL,
    medicare_rate REAL,
    event_date DATE,
    effective_year INTEGER,
    confidence REAL DEFAULT 0.5,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(source_type, source_ref)
);

CREATE INDEX IF NOT EXISTS idx_price_obs_code ON price_observations(code);
CREATE INDEX IF NOT EXISTS idx_price_obs_geo_zip ON price_observations(geo_zip5);
CREATE INDEX IF NOT EXISTS idx_price_obs_geo_state ON price_observations(geo_state);
CREATE INDEX IF NOT EXISTS idx_price_obs_source ON price_observations(source_type);

CREATE TABLE IF NOT EXISTS fair_price_bands (
    geo_scope TEXT NOT NULL,
    geo_value TEXT NOT NULL,
    code_type TEXT NOT NULL DEFAULT 'CPT',
    code TEXT NOT NULL,
    sample_size INTEGER NOT NULL,
    p25 REAL,
    p50 REAL,
    p75 REAL,
    p90 REAL,
    confidence_mean REAL,
    method TEXT NOT NULL DEFAULT 'no_api_v1',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (geo_scope, geo_value, code_type, code, method)
);

CREATE INDEX IF NOT EXISTS idx_fair_bands_code ON fair_price_bands(code);
CREATE INDEX IF NOT EXISTS idx_fair_bands_geo ON fair_price_bands(geo_scope, geo_value);

CREATE TABLE IF NOT EXISTS dispute_payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER NOT NULL REFERENCES bills(id),
    stripe_session_id TEXT UNIQUE,
    stripe_payment_intent_id TEXT UNIQUE,
    amount_cents INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    patient_email TEXT,
    refunded_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_dispute_payments_bill ON dispute_payments(bill_id);
CREATE INDEX IF NOT EXISTS idx_dispute_payments_session ON dispute_payments(stripe_session_id);

CREATE TABLE IF NOT EXISTS esign_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER NOT NULL REFERENCES bills(id),
    patient_name TEXT NOT NULL,
    patient_email TEXT NOT NULL,
    hipaa_signed_at TIMESTAMP,
    rep_signed_at TIMESTAMP,
    tos_signed_at TIMESTAMP,
    ip_address TEXT,
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_esign_bill ON esign_records(bill_id);

CREATE TABLE IF NOT EXISTS dispute_cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER NOT NULL REFERENCES bills(id),
    payment_id INTEGER REFERENCES dispute_payments(id),
    patient_name TEXT NOT NULL,
    patient_email TEXT NOT NULL,
    patient_address TEXT,
    account_number TEXT,
    hospital_billing_email TEXT,
    hospital_billing_fax TEXT,
    status TEXT NOT NULL DEFAULT 'paid',
    is_nonprofit INTEGER DEFAULT 0,
    financial_assistance_filed INTEGER DEFAULT 0,
    initial_sent_at TIMESTAMP,
    followups_sent INTEGER DEFAULT 0,
    next_followup_at DATE,
    resolved_at TIMESTAMP,
    outcome TEXT,
    actual_savings REAL,
    refunded_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_dispute_cases_bill ON dispute_cases(bill_id);
CREATE INDEX IF NOT EXISTS idx_dispute_cases_status ON dispute_cases(status);
CREATE INDEX IF NOT EXISTS idx_dispute_cases_followup ON dispute_cases(next_followup_at);

CREATE TABLE IF NOT EXISTS followup_queue (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL REFERENCES dispute_cases(id),
    followup_number INTEGER NOT NULL,
    scheduled_for DATE NOT NULL,
    sent_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_followup_case ON followup_queue(case_id);
CREATE INDEX IF NOT EXISTS idx_followup_scheduled ON followup_queue(scheduled_for, sent_at);
"""
