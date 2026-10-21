"""Denied-claim appeal service: intake, checkout, payment, approval, sending, outcome and deadlines."""

import json
from datetime import date

import pytest
from fastapi.testclient import TestClient

import appeals
import config
import payment
from appeal_letter import build_appeal_letter
from main import app

client = TestClient(app, base_url="https://testserver")

INTAKE = {
    "insurer_name": "Aetna",
    "plan_type": "employer",
    "denial_reason": "medical_necessity",
    "service_timing": "post_service",
    "denial_date": "2026-09-15",
    "amount_denied": "7840.00",
    "member_id": "W123456789",
    "claim_number": "EB-2026-0915-4471",
    "provider_name": "Inova Fair Oaks Hospital",
    "service_date": "2026-08-28",
    "service_description": "MRI of the lumbar spine (CPT 72148)",
    "insurer_appeal_address": "Aetna Appeals, PO Box 14463, Lexington, KY 40512",
    "patient_name": "Dana Whitfield",
    "email": "dana@example.com",
    "phone": "703-555-0142",
    "mailing_address": "4100 Legato Rd, Fairfax, VA 22033",
    "authorization_name": "Dana Whitfield",
}


@pytest.fixture
def stripe(monkeypatch, tmp_path):
    monkeypatch.setattr(config, "STRIPE_SECRET_KEY", "sk_test_x")
    monkeypatch.setattr(config, "PRIVATE_UPLOAD_DIR", str(tmp_path))
    sessions = {}

    def fake_checkout(**kwargs):
        sid = f"cs_test_{len(sessions) + 1}"
        sessions[sid] = kwargs
        return {"id": sid, "url": f"https://checkout.stripe.test/{sid}"}

    monkeypatch.setattr(payment, "create_payment_checkout", fake_checkout)
    monkeypatch.setattr(payment, "get_session", lambda sid: {"id": sid, "payment_status": "paid"})
    return sessions


def _submit(form=None, files=None):
    return client.post("/appeal", data=form or INTAKE, files=files, follow_redirects=False)


def test_intake_page_renders():
    resp = client.get("/appeal")
    assert resp.status_code == 200
    assert "We'll appeal it." in resp.text
    assert 'name="denial_reason"' in resp.text


def test_invalid_intake_shows_errors_and_keeps_values(stripe):
    resp = _submit({**INTAKE, "denial_reason": "", "amount_denied": "0"})
    assert resp.status_code == 400
    assert "Choose the reason the claim was denied." in resp.text
    assert "Enter the amount denied." in resp.text
    assert 'value="Dana Whitfield"' in resp.text
    assert stripe == {}


def test_intake_redirects_to_checkout_with_large_claim_price(stripe):
    resp = _submit(files={"denial_letter": ("denial.pdf", b"%PDF-1.4 denial", "application/pdf")})
    assert resp.status_code == 303
    assert resp.headers["location"].startswith("https://checkout.stripe.test/")
    (checkout,) = stripe.values()
    assert checkout["amount_cents"] == config.APPEAL_PRICE_LARGE_CENTS
    assert checkout["metadata"]["payment_purpose"] == "appeal_case"
    case = appeals.get_case(int(checkout["metadata"]["appeal_case_id"]))
    assert case["status"] == "awaiting_payment"
    with open(case["denial_letter_path"], "rb") as f:
        assert f.read() == b"%PDF-1.4 denial"


def test_small_claim_gets_standard_price():
    assert appeals.price_for_amount(1200) == config.APPEAL_PRICE_CENTS
    assert appeals.price_for_amount(config.APPEAL_LARGE_CLAIM_THRESHOLD) == config.APPEAL_PRICE_LARGE_CENTS


def test_rejects_unsupported_denial_letter_type(stripe):
    resp = _submit(files={"denial_letter": ("denial.exe", b"MZ", "application/octet-stream")})
    assert resp.status_code == 400
    assert "Denial letter: Upload a PDF or a photo" in resp.text


def test_intake_without_stripe_is_unavailable(monkeypatch):
    monkeypatch.setattr(config, "STRIPE_SECRET_KEY", "")
    resp = _submit()
    assert resp.status_code == 503
    assert "Payments aren&#39;t available" in resp.text


def test_full_flow_paid_approved_sent_decided(stripe):
    _submit()
    (session_id,) = stripe.keys()
    resp = client.get(f"/appeal/paid?session_id={session_id}", follow_redirects=False)
    token = resp.headers["location"].rsplit("/", 1)[1]
    case = appeals.get_case_by_token(token)
    assert case["status"] == "drafted"
    assert "Request for internal appeal" in case["letter_text"]
    assert "EB-2026-0915-4471" in case["letter_text"]
    assert "29 CFR 2560.503-1" in case["letter_text"]

    page = client.get(f"/appeal/case/{token}")
    assert "Review your appeal letter" in page.text
    assert "March 14, 2027" in page.text  # 180 days after the Sept 15 denial

    edited = case["letter_text"] + "\n\nP.S. My doctor's letter is attached."
    client.post(f"/appeal/case/{token}/approve", data={"letter_text": edited})
    case = appeals.get_case_by_token(token)
    assert case["status"] == "approved"
    assert case["letter_text"].endswith("My doctor's letter is attached.")

    ops_headers = {"x-admin-token": "ops-secret"}
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(config, "ADMIN_API_TOKEN", "ops-secret")
        queue = client.get("/ops/concierge", headers=ops_headers)
        assert "Dana Whitfield" in queue.text
        client.post(f"/ops/concierge/appeals/{case['id']}/sent", data={"method": "fax", "tracking_number": "FAX-889"}, headers=ops_headers)
        case = appeals.get_case(case["id"])
        assert case["status"] == "sent" and case["tracking_number"] == "FAX-889"
        assert appeals.deadlines(case)["decision_due"] is not None
        client.post(f"/ops/concierge/appeals/{case['id']}/outcome", data={"outcome": "overturned", "amount_recovered": "7,840"}, headers=ops_headers)
    case = appeals.get_case(case["id"])
    assert case["status"] == "decided" and case["amount_recovered"] == 7840.0
    assert "Denial overturned" in client.get(f"/appeal/case/{token}").text


def test_paid_redirect_ignores_unpaid_session(stripe, monkeypatch):
    _submit()
    (session_id,) = stripe.keys()
    monkeypatch.setattr(payment, "get_session", lambda sid: {"id": sid, "payment_status": "unpaid"})
    client.get(f"/appeal/paid?session_id={session_id}")
    assert appeals.get_case_by_session(session_id)["status"] == "awaiting_payment"


def test_webhook_marks_paid_once(stripe, monkeypatch):
    _submit()
    (session_id,) = stripe.keys()
    case_id = int(stripe[session_id]["metadata"]["appeal_case_id"])
    monkeypatch.setattr(config, "STRIPE_WEBHOOK_SECRET", "")
    monkeypatch.setattr(config, "DEBUG", True)
    event = {"type": "checkout.session.completed", "data": {"object": {
        "id": session_id, "payment_status": "paid",
        "metadata": {"payment_purpose": "appeal_case", "appeal_case_id": str(case_id)},
    }}}
    assert client.post("/api/stripe/webhook", content=json.dumps(event)).status_code == 200
    assert appeals.get_case(case_id)["status"] == "drafted"
    assert appeals.mark_paid(case_id) is False


def test_ops_queue_requires_admin(monkeypatch):
    monkeypatch.setattr(config, "ADMIN_API_TOKEN", "ops-secret")
    assert client.get("/ops/concierge").status_code == 403
    assert client.get("/ops/login?token=wrong").status_code == 403
    login = client.get("/ops/login?token=ops-secret", follow_redirects=False)
    assert login.status_code == 303 and "bk_admin" in login.headers["set-cookie"]


def test_mail_by_lob_uses_certified_mail(monkeypatch):
    case = appeals.create_case(INTAKE, None)
    appeals.mark_paid(case["id"])
    appeals.approve(appeals.get_case(case["id"]), "Approved letter text")
    sent = {}
    monkeypatch.setattr(config, "LOB_API_KEY", "test_lob")
    monkeypatch.setattr(appeals, "send_certified_letter", lambda **kw: sent.update(kw) or {"lob_id": "ltr_1", "tracking_number": "9407 1000", "expected_delivery_date": ""})
    appeals.mail_by_lob(appeals.get_case(case["id"]))
    assert sent["to_address"] == INTAKE["insurer_appeal_address"]
    assert sent["letter_text"] == "Approved letter text"
    assert appeals.get_case(case["id"])["sent_method"] == "certified_mail"


def test_medicare_advantage_deadline_and_urgent_letter():
    form = {**INTAKE, "plan_type": "medicare_advantage", "service_timing": "urgent"}
    case = appeals.create_case(form, None)
    assert appeals.deadlines(case)["file_by"] == date(2026, 11, 19)  # 65 days
    letter = build_appeal_letter(case, today=date(2026, 10, 1))
    assert "EXPEDITED" in letter and "72 hours" in letter and "42 CFR 422.578" in letter
    assert letter.startswith("October 1, 2026")


def test_unknown_case_is_404():
    assert client.get("/appeal/case/not-a-real-token").status_code == 404
