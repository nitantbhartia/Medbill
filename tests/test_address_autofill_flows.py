"""Regression tests for address autofill wiring on remaining debt/dispute flows."""

import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import config  # noqa: E402
import db as _db  # noqa: E402
from main import app  # noqa: E402


client = TestClient(app)


def _insert_bill() -> int:
    with _db.get_db() as conn:
        cur = conn.execute(
            """
            INSERT INTO bills (provider_name, bill_date, total_charged, total_patient_owes)
            VALUES (?, ?, ?, ?)
            """,
            ("Test Hospital", "2026-02-24", 1200.0, 800.0),
        )
        return int(cur.lastrowid)


def test_settle_debt_has_address_fields():
    resp = client.get("/settle-debt")
    assert resp.status_code == 200
    html = resp.text
    assert 'id="user_address"' in html
    assert 'id="collector_address"' in html


def test_settle_debt_places_script_enabled(monkeypatch):
    monkeypatch.setattr(config, "GOOGLE_PLACES_API_KEY", "test-key-123")
    resp = client.get("/settle-debt")
    assert resp.status_code == 200
    html = resp.text
    assert "maps.googleapis.com/maps/api/js" in html
    assert "callback=initSettleDebtAddressAutofill" in html


def test_settle_debt_places_script_disabled(monkeypatch):
    monkeypatch.setattr(config, "GOOGLE_PLACES_API_KEY", "")
    resp = client.get("/settle-debt")
    assert resp.status_code == 200
    html = resp.text
    assert "maps.googleapis.com/maps/api/js" not in html


def test_dispute_activate_has_address_field():
    bill_id = _insert_bill()
    resp = client.get(f"/dispute/activate/{bill_id}")
    assert resp.status_code == 200
    html = resp.text
    assert 'id="patient-address"' in html


def test_dispute_activate_places_script_enabled(monkeypatch):
    monkeypatch.setattr(config, "GOOGLE_PLACES_API_KEY", "test-key-123")
    bill_id = _insert_bill()
    resp = client.get(f"/dispute/activate/{bill_id}")
    assert resp.status_code == 200
    html = resp.text
    assert "maps.googleapis.com/maps/api/js" in html
    assert "callback=initDisputeActivateAddressAutofill" in html


def test_dispute_activate_places_script_disabled(monkeypatch):
    monkeypatch.setattr(config, "GOOGLE_PLACES_API_KEY", "")
    bill_id = _insert_bill()
    resp = client.get(f"/dispute/activate/{bill_id}")
    assert resp.status_code == 200
    html = resp.text
    assert "maps.googleapis.com/maps/api/js" not in html
