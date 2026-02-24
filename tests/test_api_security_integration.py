"""Security, integration, and regression coverage for production-hardening changes."""

import os
import sys
from unittest.mock import MagicMock

import pytest

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import config  # noqa: E402
import api as api_module  # noqa: E402
from main import app  # noqa: E402
from db import get_db  # noqa: E402


client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_tool_buckets():
    api_module._tools_rate_buckets.clear()
    yield
    api_module._tools_rate_buckets.clear()


@pytest.fixture()
def prod_mode(monkeypatch):
    old_debug = config.DEBUG
    old_env = config.ENV
    monkeypatch.setattr(config, "DEBUG", False)
    monkeypatch.setattr(config, "ENV", "production")
    yield
    monkeypatch.setattr(config, "DEBUG", old_debug)
    monkeypatch.setattr(config, "ENV", old_env)


def test_tools_run_rejects_invalid_json_body():
    resp = client.post(
        "/api/tools/medical-debt-statute-of-limitations-checker/run",
        data="not-json",
        headers={"content-type": "application/json"},
    )
    assert resp.status_code == 400
    assert "Invalid JSON payload" in resp.text


def test_tools_run_rejects_oversized_payload(monkeypatch):
    monkeypatch.setattr(config, "MAX_TOOL_PAYLOAD_BYTES", 100)
    payload = {"state": "FL", "date_of_service": "2020-01-01", "notes": "x" * 500}
    resp = client.post("/api/tools/medical-debt-statute-of-limitations-checker/run", json=payload)
    assert resp.status_code == 413


def test_tools_lead_capture_rejects_unknown_tool():
    payload = {
        "email": "person@example.com",
        "tool_slug": "medical-bill-error-checker",
        "lead_magnet_key": "audit_checklist",
        "context": {"ok": "yes"},
    }
    assert client.post("/api/tools/lead-capture", json=payload).status_code == 200

    payload["tool_slug"] = "not-a-real-tool"
    resp = client.post("/api/tools/lead-capture", json=payload)
    assert resp.status_code == 400


def test_tools_rate_limit_enforced(monkeypatch):
    monkeypatch.setattr(config, "TOOLS_RATE_LIMIT_REQUESTS", 1)
    monkeypatch.setattr(config, "TOOLS_RATE_LIMIT_WINDOW_SECONDS", 3600)

    payload = {"state": "FL", "date_of_service": "2019-01-01"}
    first = client.post("/api/tools/medical-debt-statute-of-limitations-checker/run", json=payload)
    second = client.post("/api/tools/medical-debt-statute-of-limitations-checker/run", json=payload)
    assert first.status_code == 200
    assert second.status_code == 429


def test_prod_admin_guard_blocks_purge_without_token(prod_mode, monkeypatch):
    monkeypatch.setattr(config, "ADMIN_API_TOKEN", "")
    resp = client.post("/api/compliance/purge-old", data={"days": 365})
    assert resp.status_code == 403


def test_prod_admin_guard_allows_with_token(prod_mode, monkeypatch):
    monkeypatch.setattr(config, "ADMIN_API_TOKEN", "secret-token")
    denied = client.post("/api/compliance/purge-old", data={"days": 30})
    allowed = client.post("/api/compliance/purge-old", data={"days": 30}, headers={"x-admin-token": "secret-token"})
    assert denied.status_code == 403
    assert allowed.status_code == 200


def test_prod_webhook_requires_secret(prod_mode, monkeypatch):
    monkeypatch.setattr(config, "STRIPE_WEBHOOK_SECRET", "")
    resp = client.post("/api/stripe/webhook", data='{"type":"checkout.session.completed","data":{"object":{}}}')
    assert resp.status_code == 503


def test_tools_flow_persists_run_and_lead_regression():
    run = client.post(
        "/api/tools/hospital-financial-assistance-calculator/run",
        json={"hospital_name": "", "income": 35000, "household_size": 2},
    )
    assert run.status_code == 200

    lead = client.post(
        "/api/tools/lead-capture",
        json={
            "email": "flow@example.com",
            "tool_slug": "hospital-financial-assistance-calculator",
            "lead_magnet_key": "charity_care_guide",
            "context": {"source": "integration-test"},
        },
    )
    assert lead.status_code == 200

    with get_db() as db:
        run_row = db.execute(
            "SELECT tool_slug, result_state FROM tool_runs WHERE tool_slug = ? ORDER BY id DESC LIMIT 1",
            ("hospital-financial-assistance-calculator",),
        ).fetchone()
        lead_row = db.execute(
            "SELECT email, tool_slug FROM tool_leads WHERE email = ? ORDER BY id DESC LIMIT 1",
            ("flow@example.com",),
        ).fetchone()

    assert run_row is not None
    assert run_row["tool_slug"] == "hospital-financial-assistance-calculator"
    assert lead_row is not None
    assert lead_row["tool_slug"] == "hospital-financial-assistance-calculator"


def test_prod_admin_guard_blocks_export_delete(prod_mode, monkeypatch):
    monkeypatch.setattr(config, "ADMIN_API_TOKEN", "")

    resp_export = client.get("/api/bills/1/export")
    resp_delete = client.delete("/api/bills/1")
    assert resp_export.status_code == 403
    assert resp_delete.status_code == 403
