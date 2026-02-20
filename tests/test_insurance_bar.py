"""Tests for insurance plan personalization bar on hospital and procedure pages."""

import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import db as _db  # noqa: E402
from db import get_db  # noqa: E402
from hospital_seo import upsert_hospital_row  # noqa: E402
from main import app  # noqa: E402

_db.init_db()
client = TestClient(app)

_FID_A = "099001"


def _seed():
    upsert_hospital_row({
        "facility_id": "99001",
        "name": "Test General Hospital",
        "address": "100 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip": "62701",
        "ownership": "Voluntary non-profit - Private",
        "hospital_type": "Acute Care Hospitals",
        "bed_count": 200,
        "cms_star_rating": 4,
        "slug": "test-general-hospital-springfield",
        "is_nonprofit": 1,
        "lat": 39.7817,
        "lon": -89.6501,
    })
    with get_db() as db:
        db.execute(
            "INSERT OR IGNORE INTO billing_metrics (facility_id, avg_markup_vs_medicare, billing_grade, procedures_compared, state_rank) VALUES (?, ?, ?, ?, ?)",
            (_FID_A, 2.5, "A", 15, 2),
        )
        db.execute(
            "INSERT OR IGNORE INTO hospital_prices (facility_id, cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare, data_year) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (_FID_A, "27447", "TOTAL KNEE REPLACEMENT", 4200.0, 2000.0, 2.1, 2025),
        )


# ---- Hospital detail page tests ----

def test_hospital_detail_includes_insurance_bar():
    _seed()
    resp = client.get("/hospitals/il/springfield/test-general-hospital-springfield/")
    assert resp.status_code == 200
    assert "bk-ins-bar" in resp.text


def test_hospital_detail_has_add_my_insurance_button():
    _seed()
    resp = client.get("/hospitals/il/springfield/test-general-hospital-springfield/")
    assert resp.status_code == 200
    assert "Add My Insurance" in resp.text or "Add your insurance" in resp.text


def test_hospital_detail_has_oop_column_header():
    _seed()
    resp = client.get("/hospitals/il/springfield/test-general-hospital-springfield/")
    assert resp.status_code == 200
    assert "bk-oop-th" in resp.text
    assert "Your Est. Cost" in resp.text


def test_hospital_detail_price_rows_have_data_charge():
    _seed()
    resp = client.get("/hospitals/il/springfield/test-general-hospital-springfield/")
    assert resp.status_code == 200
    assert 'data-charge="' in resp.text


def test_hospital_detail_includes_local_storage_key():
    _seed()
    resp = client.get("/hospitals/il/springfield/test-general-hospital-springfield/")
    assert resp.status_code == 200
    assert "billkarma_insurance_plan" in resp.text


def test_hospital_detail_has_disclaimer():
    _seed()
    resp = client.get("/hospitals/il/springfield/test-general-hospital-springfield/")
    assert resp.status_code == 200
    assert "coinsurance" in resp.text or "deductible" in resp.text.lower()


# ---- Procedure detail page tests ----

def test_procedure_detail_includes_insurance_bar():
    _seed()
    resp = client.get("/procedures/27447/")
    assert resp.status_code == 200
    assert "bk-ins-bar" in resp.text


def test_procedure_detail_has_oop_column_header():
    _seed()
    resp = client.get("/procedures/27447/")
    assert resp.status_code == 200
    assert "bk-oop-th" in resp.text


def test_procedure_detail_hospital_rows_have_data_charge():
    _seed()
    resp = client.get("/procedures/27447/")
    assert resp.status_code == 200
    assert 'data-charge="' in resp.text


def test_procedure_detail_includes_local_storage_key():
    _seed()
    resp = client.get("/procedures/27447/")
    assert resp.status_code == 200
    assert "billkarma_insurance_plan" in resp.text


def test_insurance_bar_has_plan_type_options():
    _seed()
    resp = client.get("/procedures/27447/")
    assert resp.status_code == 200
    assert "PPO" in resp.text
    assert "HMO" in resp.text
    assert "HDHP" in resp.text


def test_insurance_bar_has_deductible_input():
    _seed()
    resp = client.get("/procedures/27447/")
    assert resp.status_code == 200
    assert "Remaining Deductible" in resp.text or "bk-f-ded" in resp.text


def test_insurance_bar_has_deductible_tracker():
    _seed()
    resp = client.get("/procedures/27447/")
    assert resp.status_code == 200
    assert "bk-ded-tracker" in resp.text


def test_insurance_bar_disclaimer_present():
    _seed()
    resp = client.get("/hospitals/il/springfield/test-general-hospital-springfield/")
    assert resp.status_code == 200
    # Disclaimer should mention coinsurance/estimates
    assert "coinsurance" in resp.text or "Actual costs" in resp.text
