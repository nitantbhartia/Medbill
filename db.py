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
"""
