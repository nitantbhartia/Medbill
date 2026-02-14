"""Shared test fixtures — sets up an in-memory SQLite database seeded with
reference Medicare rates and NCCI edits before every test module."""

import os
import sys
import pytest

# Make project root importable
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Force an in-memory database so tests never touch production data
os.environ["DB_PATH"] = ":memory:"

import config  # noqa: E402 — must come after env override
config.DB_PATH = ":memory:"

import db as _db  # noqa: E402


@pytest.fixture(autouse=True)
def fresh_db():
    """Reset the global connection and reinitialise the schema + seed data
    before *every* test so tests are fully isolated."""
    _db._connection = None  # force a new connection
    _db.init_db()
    from seed_data import seed_if_empty
    seed_if_empty()
    yield
    if _db._connection:
        _db._connection.close()
        _db._connection = None


# ---------------------------------------------------------------------------
# Reusable sample data
# ---------------------------------------------------------------------------

SAMPLE_BILL = {
    "provider_name": "Memorial Regional Hospital",
    "provider_address": "3501 Johnson St, Hollywood, FL 33021",
    "bill_date": "2026-01-15",
    "total_charged": 12847.00,
    "total_patient_owes": 4215.00,
    "line_items": [
        {
            "date_of_service": "2026-01-10",
            "cpt_code": "99285",
            "description": "Emergency department visit, high severity",
            "quantity": 1,
            "charged_amount": 4500.00,
            "insurance_paid": 1800.00,
            "insurance_adjustment": 1500.00,
            "patient_responsibility": 1200.00,
        },
        {
            "date_of_service": "2026-01-10",
            "cpt_code": "71046",
            "description": "Chest X-Ray, 2 views",
            "quantity": 1,
            "charged_amount": 850.00,
            "insurance_paid": 180.00,
            "insurance_adjustment": 520.00,
            "patient_responsibility": 150.00,
        },
        {
            "date_of_service": "2026-01-10",
            "cpt_code": "80053",
            "description": "Comprehensive metabolic panel",
            "quantity": 1,
            "charged_amount": 350.00,
            "insurance_paid": 50.00,
            "insurance_adjustment": 250.00,
            "patient_responsibility": 50.00,
        },
    ],
}

SAMPLE_BILL_WITH_DUPLICATES = {
    "provider_name": "Test Hospital",
    "provider_address": "123 Main St, Test, FL 33021",
    "bill_date": "2026-02-01",
    "total_charged": 1700.00,
    "total_patient_owes": 1700.00,
    "line_items": [
        {
            "date_of_service": "2026-02-01",
            "cpt_code": "71046",
            "description": "Chest X-Ray, 2 views",
            "quantity": 1,
            "charged_amount": 850.00,
        },
        {
            "date_of_service": "2026-02-01",
            "cpt_code": "71046",
            "description": "Chest X-Ray, 2 views",
            "quantity": 1,
            "charged_amount": 850.00,
        },
    ],
}

SAMPLE_BILL_WITH_UNBUNDLING = {
    "provider_name": "Test Hospital",
    "provider_address": "123 Main St, Test, FL 33021",
    "bill_date": "2026-02-01",
    "total_charged": 600.00,
    "total_patient_owes": 600.00,
    "line_items": [
        {
            "date_of_service": "2026-02-01",
            "cpt_code": "80048",
            "description": "Basic metabolic panel",
            "quantity": 1,
            "charged_amount": 250.00,
        },
        {
            "date_of_service": "2026-02-01",
            "cpt_code": "80053",
            "description": "Comprehensive metabolic panel",
            "quantity": 1,
            "charged_amount": 350.00,
        },
    ],
}

SAMPLE_BILL_EMERGENCY_HIGH_OOP = {
    "provider_name": "ER Hospital",
    "provider_address": "456 Emergency Rd, Miami, FL 33101",
    "bill_date": "2026-01-20",
    "total_charged": 10000.00,
    "total_patient_owes": 8000.00,
    "line_items": [
        {
            "date_of_service": "2026-01-20",
            "cpt_code": "99285",
            "description": "Emergency department visit, high severity",
            "quantity": 1,
            "charged_amount": 6000.00,
            "patient_responsibility": 5000.00,
        },
        {
            "date_of_service": "2026-01-20",
            "cpt_code": "71046",
            "description": "Chest X-Ray, 2 views",
            "quantity": 1,
            "charged_amount": 4000.00,
            "patient_responsibility": 3000.00,
        },
    ],
}
