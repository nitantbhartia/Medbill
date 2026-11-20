"""ClaimCoach tables. Imported by db.init_db(); must not import db."""

SCHEMA = """
CREATE TABLE IF NOT EXISTS cc_cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT NOT NULL,
    for_whom TEXT NOT NULL DEFAULT 'self',  -- self | someone_else
    plan_type TEXT,  -- individual | employer | medicare_advantage | original_medicare | medicaid | other
    service_timing TEXT,  -- pre_service | post_service | urgent
    denial_reason TEXT,
    level TEXT NOT NULL DEFAULT 'internal',  -- internal | external | ire | qic | fair_hearing
    extracted_json TEXT,
    schema_version TEXT,
    notice_date DATE,
    file_by DATE,
    deadline_source TEXT,  -- letter | default
    status TEXT NOT NULL DEFAULT 'draft',  -- draft | sent | decided
    sent_at TIMESTAMP, sent_channel TEXT,  -- sent_channel: mail | fax | self
    decision_due DATE,
    outcome TEXT,  -- overturned | partial | upheld
    amount_denied REAL, amount_recovered REAL,
    plain_reason TEXT, needs_confirmation TEXT, letter_text TEXT, decided_at DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_cc_cases_device ON cc_cases(device_id, created_at);
CREATE TABLE IF NOT EXISTS cc_case_unlocks (
    case_id INTEGER NOT NULL,
    source TEXT NOT NULL UNIQUE,
    product_id TEXT,
    status TEXT NOT NULL DEFAULT 'paid',  -- paid | refunded
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_cc_unlocks_case ON cc_case_unlocks(case_id);
CREATE TABLE IF NOT EXISTS cc_sends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    channel TEXT NOT NULL,  -- mail | fax
    provider_ref TEXT, tracking_number TEXT, status TEXT,
    approved_text_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_cc_sends_case ON cc_sends(case_id);
"""


def init(db) -> None:
    db.executescript(SCHEMA)
    columns = {row[1] for row in db.execute("PRAGMA table_info(mobile_devices)").fetchall()}
    if "app" not in columns:
        db.execute("ALTER TABLE mobile_devices ADD COLUMN app TEXT NOT NULL DEFAULT 'billkarma'")
