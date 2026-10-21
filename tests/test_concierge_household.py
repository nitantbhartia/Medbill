"""Household bill plan: account, subscription checkout, webhook, uploads, bill-vs-EOB check, help requests."""

import json

import pytest
from fastapi.testclient import TestClient

import config
import household
import payment
from db import get_db
from main import app

PDF = ("bill.pdf", b"%PDF-1.4 bill", "application/pdf")


@pytest.fixture
def client(monkeypatch, tmp_path):
    monkeypatch.setattr(config, "STRIPE_SECRET_KEY", "sk_test_x")
    monkeypatch.setattr(config, "GEMINI_API_KEY", "")
    monkeypatch.setattr(config, "PRIVATE_UPLOAD_DIR", str(tmp_path))
    monkeypatch.setattr(
        payment, "create_subscription_checkout",
        lambda **kw: {"id": "cs_sub_1", "url": "https://checkout.stripe.test/cs_sub_1", "kw": kw},
    )
    return TestClient(app, base_url="https://testserver")


def _register(client, email="sam@example.com"):
    resp = client.post("/account/register", data={"name": "Sam Ortiz", "email": email, "password": "correct horse"}, follow_redirects=False)
    assert resp.status_code == 303
    with get_db() as db:
        return db.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()["id"]


def _activate(user_id, monkeypatch=None):
    household.record_checkout(user_id, "yearly", "cs_sub_1")
    household.activate_from_session({"mode": "subscription", "customer": "cus_1", "subscription": "sub_1", "metadata": {"user_id": str(user_id)}})


def _upload(client, **fields):
    data = {"doc_type": "bill", **fields}
    return client.post("/household/documents", data=data, files={"document": PDF}, follow_redirects=False)


def test_landing_shows_plans_and_signup(client):
    resp = client.get("/household")
    assert resp.status_code == 200
    assert "$199 a year" in resp.text and "$20 a month" in resp.text
    assert 'href="/account"' in resp.text


def test_dashboard_requires_login_and_membership(client):
    assert client.get("/household/dashboard", follow_redirects=False).headers["location"] == "/account?mode=login"
    _register(client)
    assert client.get("/household/dashboard", follow_redirects=False).headers["location"] == "/household"


def test_checkout_records_pending_membership(client):
    user_id = _register(client)
    resp = client.post("/household/checkout", data={"plan": "monthly"}, follow_redirects=False)
    assert resp.headers["location"] == "https://checkout.stripe.test/cs_sub_1"
    membership = household.get_membership(user_id)
    assert membership["plan"] == "monthly" and membership["status"] == "pending"


def test_webhook_activates_then_cancels(client, monkeypatch):
    user_id = _register(client)
    client.post("/household/checkout", data={"plan": "yearly"})
    monkeypatch.setattr(config, "STRIPE_WEBHOOK_SECRET", "")
    monkeypatch.setattr(config, "DEBUG", True)
    completed = {"type": "checkout.session.completed", "data": {"object": {
        "id": "cs_sub_1", "mode": "subscription", "customer": "cus_9", "subscription": "sub_9",
        "metadata": {"payment_purpose": "household", "user_id": str(user_id)},
    }}}
    client.post("/api/stripe/webhook", content=json.dumps(completed))
    assert household.is_active(user_id)
    assert client.get("/household/dashboard").status_code == 200

    deleted = {"type": "customer.subscription.deleted", "data": {"object": {"id": "sub_9", "status": "canceled"}}}
    client.post("/api/stripe/webhook", content=json.dumps(deleted))
    assert not household.is_active(user_id)


def test_bill_without_eob_says_wait_then_overbilled_after_eob(client):
    user_id = _register(client)
    _activate(user_id)
    _upload(client, provider_name="Inova Fair Oaks Hospital", service_date="2026-08-28", amount_due="1840.00")
    bill = household.dashboard(user_id)["bills"][0]
    assert bill["check"]["verdict"] == "wait"

    _upload(client, doc_type="eob", provider_name="INOVA FAIR OAKS HOSPITAL", service_date="2026-08-28", patient_responsibility="412.60")
    bill = household.dashboard(user_id)["bills"][0]
    assert bill["eob_document_id"] is not None  # linked automatically by provider and date
    assert bill["check"]["verdict"] == "overbilled"
    assert "$1,427.40 more" in bill["check"]["message"]
    page = client.get("/household/dashboard")
    assert "Overbilled." in page.text


def test_check_bill_verdicts():
    eob = {"patient_responsibility": 250.0}
    assert household.check_bill({"amount_due": 250.4, "amount_paid": 0}, eob)["verdict"] == "ok"
    assert household.check_bill({"amount_due": 0, "amount_paid": 400.0}, eob)["verdict"] == "overpaid"
    assert household.check_bill({"amount_due": None}, eob)["verdict"] == "review"


def test_upload_without_amounts_and_no_scanner_needs_review(client):
    user_id = _register(client)
    _activate(user_id)
    _upload(client, provider_name="Quest Diagnostics")
    with get_db() as db:
        row = db.execute("SELECT extraction_status FROM household_documents WHERE user_id = ?", (user_id,)).fetchone()
    assert row["extraction_status"] == "needs_review"


def test_upload_fills_amount_from_scanner(client, monkeypatch):
    user_id = _register(client)
    _activate(user_id)
    monkeypatch.setattr(config, "GEMINI_API_KEY", "test")
    monkeypatch.setattr(household.scanner, "process_bill_with_verification", lambda data, mime: {
        "provider_name": "Quest Diagnostics", "total_patient_owes": 186.25,
        "line_items": [{"date_of_service": "2026-09-02", "cpt_code": "80053"}],
    })
    _upload(client)
    bill = household.dashboard(user_id)["bills"][0]
    assert bill["amount_due"] == 186.25 and bill["provider_name"] == "Quest Diagnostics" and bill["service_date"] == "2026-09-02"


def test_non_member_cannot_upload(client):
    _register(client)
    assert _upload(client).status_code == 403


def test_help_request_reaches_ops_and_resolution_closes_it(client, monkeypatch):
    user_id = _register(client)
    _activate(user_id)
    _upload(client, provider_name="Inova Fair Oaks Hospital", amount_due="900")
    bill_id = household.dashboard(user_id)["bills"][0]["id"]
    client.post("/household/requests", data={"document_id": str(bill_id), "note": "Please call them"})
    assert "We're on it" in client.get("/household/dashboard").text

    monkeypatch.setattr(config, "ADMIN_API_TOKEN", "ops-secret")
    queue = client.get("/ops/concierge", headers={"x-admin-token": "ops-secret"})
    assert "Please call them" in queue.text
    request_id = household.open_requests()[0]["id"]
    sent = []
    monkeypatch.setattr(household.email_service, "send_email", lambda to, subject, html: sent.append(to) or True)
    client.post(f"/ops/concierge/requests/{request_id}/resolve", data={"resolution": "Called billing, balance reduced to $412.60"}, headers={"x-admin-token": "ops-secret"})
    assert household.open_requests() == []
    assert sent == ["sam@example.com"]


def test_login_with_wrong_password_shows_error(client):
    _register(client)
    client.cookies.clear()
    resp = client.post("/account/login", data={"email": "sam@example.com", "password": "wrong password"})
    assert resp.status_code == 401
    assert "Invalid email or password" in resp.text
