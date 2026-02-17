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
    existing = {row[1] for row in db.execute("PRAGMA table_info(bills)").fetchall()}
    if "zip_code" not in existing:
        db.execute("ALTER TABLE bills ADD COLUMN zip_code TEXT")

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
    severity TEXT,
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
"""
