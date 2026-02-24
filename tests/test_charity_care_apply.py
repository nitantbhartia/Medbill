"""Regression tests for charity-care apply page address autofill wiring."""

import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import config  # noqa: E402
from main import app  # noqa: E402


client = TestClient(app)


def test_charity_apply_has_address_fields():
    resp = client.get("/charity-care/apply")
    assert resp.status_code == 200
    html = resp.text
    assert 'id="user-address"' in html
    assert 'id="hosp-address"' in html


def test_charity_apply_places_script_enabled(monkeypatch):
    monkeypatch.setattr(config, "GOOGLE_PLACES_API_KEY", "test-key-123")
    resp = client.get("/charity-care/apply")
    assert resp.status_code == 200
    html = resp.text
    assert "maps.googleapis.com/maps/api/js" in html
    assert "callback=initCharityApplyAddressAutofill" in html


def test_charity_apply_places_script_disabled(monkeypatch):
    monkeypatch.setattr(config, "GOOGLE_PLACES_API_KEY", "")
    resp = client.get("/charity-care/apply")
    assert resp.status_code == 200
    html = resp.text
    assert "maps.googleapis.com/maps/api/js" not in html
