"""Regression test for /api/email-report bill access control."""

import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import api as api_module  # noqa: E402
import db as _db  # noqa: E402
from analyzer import analyze_bill, save_bill_and_findings  # noqa: E402
from main import app  # noqa: E402
from tests.conftest import SAMPLE_BILL  # noqa: E402


client = TestClient(app)


def _seed_bill() -> int:
    _db._connection = None
    _db.init_db()
    from seed_data import seed_if_empty

    seed_if_empty()
    analysis = analyze_bill(SAMPLE_BILL, "33021")
    return save_bill_and_findings(None, SAMPLE_BILL, analysis)


def test_email_report_requires_bill_access(monkeypatch):
    # Emulate production-style gate in tests.
    monkeypatch.setattr(api_module.config, "ENV", "production")
    monkeypatch.setattr(api_module, "is_admin_request", lambda _request: False)
    monkeypatch.setattr(api_module.email_service, "send_email", lambda *_args, **_kwargs: True)
    api_module._email_report_rate_buckets.clear()

    bill_id = _seed_bill()

    resp = client.post("/api/email-report", json={"bill_id": bill_id, "email": "nobody@example.com"})
    assert resp.status_code == 403


def test_email_report_rate_limited_when_access_allowed(monkeypatch):
    monkeypatch.setattr(api_module.config, "ENV", "production")
    monkeypatch.setattr(api_module, "is_admin_request", lambda _request: False)
    monkeypatch.setattr(api_module.config, "EMAIL_REPORT_RATE_LIMIT_REQUESTS", 1)
    monkeypatch.setattr(api_module.config, "EMAIL_REPORT_RATE_LIMIT_WINDOW_SECONDS", 3600)
    monkeypatch.setattr(api_module.email_service, "send_email", lambda *_args, **_kwargs: True)
    api_module._email_report_rate_buckets.clear()

    bill_id = _seed_bill()

    # Use an admin header to avoid cookie plumbing in unit tests while still exercising the limiter.
    headers = {"x-admin-token": "token", "cf-connecting-ip": "203.0.113.200"}
    monkeypatch.setattr(api_module.config, "ADMIN_API_TOKEN", "token")

    first = client.post("/api/email-report", json={"bill_id": bill_id, "email": "a@example.com"}, headers=headers)
    second = client.post("/api/email-report", json={"bill_id": bill_id, "email": "a@example.com"}, headers=headers)
    assert first.status_code == 200
    assert second.status_code == 429
