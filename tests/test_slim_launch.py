"""The slim launch: free scan and teaser, one $19.99 Bill Check Report, every other product hidden."""

import hashlib
import hmac
import json
import re
import time

import pytest
from fastapi.testclient import TestClient

import config
import payment
import report
from analyzer import analyze_bill, save_bill_and_findings
from db import get_db
from main import app
from tests.conftest import SAMPLE_BILL

client = TestClient(app, follow_redirects=False)
WEBHOOK_SECRET = "whsec_test"


@pytest.fixture(autouse=True)
def slim_on(monkeypatch):
    monkeypatch.setattr(config, "SLIM_LAUNCH", True)
    monkeypatch.setattr(config, "STRIPE_WEBHOOK_SECRET", WEBHOOK_SECRET)


@pytest.fixture
def flagged_bill():
    return save_bill_and_findings(None, SAMPLE_BILL, analyze_bill(SAMPLE_BILL, "33021"), "33021")


@pytest.fixture
def clean_bill():
    analysis = {"findings": [], "total_findings": 0, "total_potential_savings": 0}
    return save_bill_and_findings(None, SAMPLE_BILL, analysis, "33021")


def text_of(response):
    return re.sub(r"\s+", " ", response.text)


def send_webhook(session_id, bill_id, paid=True, purpose=config.REPORT_PAYMENT_PURPOSE):
    event = {
        "type": "checkout.session.completed",
        "data": {"object": {
            "id": session_id,
            "payment_status": "paid" if paid else "unpaid",
            "metadata": {"payment_purpose": purpose, "bill_id": str(bill_id)},
        }},
    }
    body = json.dumps(event)
    stamp = int(time.time())
    signature = hmac.new(WEBHOOK_SECRET.encode(), f"{stamp}.{body}".encode(), hashlib.sha256).hexdigest()
    return client.post("/api/stripe/webhook", content=body, headers={"stripe-signature": f"t={stamp},v1={signature}"})


def unlock(bill_id, session_id="cs_test_1"):
    report.record_pending(bill_id, session_id, "buyer@example.com")
    assert send_webhook(session_id, bill_id).status_code == 200


# ── The free teaser ────────────────────────────────────────────────────────────

def test_locked_results_show_the_count_the_savings_and_one_price(flagged_bill):
    html = text_of(client.get(f"/results/{flagged_bill}"))
    teaser = report.teaser(flagged_bill)
    assert f"{teaser['charge_count']} charge" in html
    assert "billing errors we found" in html or "above typical Medicare pricing" in html
    assert "Unlock your full report" in html
    assert "Unlock my report for $19.99" in html
    assert 'action="/report/checkout"' in html


def test_locked_results_show_one_charge_free_and_hide_the_rest_and_the_letter_tools(flagged_bill):
    from analyzer import get_bill_results
    from mobile_view import free_charge
    free = free_charge(get_bill_results(flagged_bill))
    html = client.get(f"/results/{flagged_bill}").text
    assert "Free preview" in html and free["description"] in html
    assert html.count("Medicare pays $") == 1
    assert 'id="gen-letter-btn"' not in html
    assert 'id="gen-phone-btn"' not in html
    assert "Charges we flagged" not in html
    for item in SAMPLE_BILL["line_items"]:
        if item["description"] != free["description"]:
            assert item["description"] not in html


def test_the_free_preview_is_gone_once_the_report_is_unlocked(flagged_bill):
    unlock(flagged_bill)
    assert "Free preview" not in client.get(f"/results/{flagged_bill}").text


def test_locked_results_name_no_other_product(flagged_bill):
    html = text_of(client.get(f"/results/{flagged_bill}"))
    for stale in ("Dispute these for", "We dispute it for you", "Insurance Appeal", "Ask AI", "autopilot", "household"):
        assert stale not in html


def test_the_price_comes_from_config(flagged_bill, monkeypatch):
    monkeypatch.setattr(config, "REPORT_PRICE_CENTS", 2500)
    assert "Unlock my report for $25" in text_of(client.get(f"/results/{flagged_bill}"))
    assert "$25 once" in text_of(client.get("/"))


# ── The paywall on every endpoint that carries findings ───────────────────────

def test_the_results_api_returns_only_the_teaser_while_locked(flagged_bill):
    data = client.get(f"/api/results/{flagged_bill}").json()["data"]
    assert data["locked"] is True
    assert data["charge_count"] >= 1 and "findings" not in data


@pytest.mark.parametrize("method,path", [
    ("get", "/api/dispute-phone-script/{id}"),
    ("get", "/api/dispute-packet/{id}"),
    ("get", "/api/score/{id}"),
    ("post", "/api/dispute-letter/{id}"),
    ("post", "/api/email-report"),
])
def test_letters_script_packet_score_and_email_need_the_unlock(flagged_bill, method, path):
    url = path.format(id=flagged_bill)
    if method == "post" and path.endswith("email-report"):
        response = client.post(url, json={"bill_id": flagged_bill, "email": "a@b.co"})
    elif method == "post":
        response = client.post(url, json={"finding_ids": []})
    else:
        response = client.get(url)
    assert response.status_code == 402
    assert "$19.99" in response.json()["detail"]


# ── Checkout ───────────────────────────────────────────────────────────────────

def stub_stripe(monkeypatch, session_id="cs_test_1"):
    monkeypatch.setattr(payment, "create_report_checkout",
                        lambda bill_id, email: {"id": session_id, "url": f"https://checkout.stripe.test/{session_id}"})


def test_checkout_sends_the_buyer_to_stripe_and_records_a_pending_unlock(flagged_bill, monkeypatch):
    stub_stripe(monkeypatch)
    response = client.post("/report/checkout", data={"bill_id": flagged_bill, "email": "buyer@example.com"})
    assert response.status_code == 303 and response.headers["location"] == "https://checkout.stripe.test/cs_test_1"
    assert report.pending_session_ids(flagged_bill) == ["cs_test_1"]
    assert not report.is_paid(flagged_bill)


def test_checkout_charges_the_configured_price_for_one_bill(flagged_bill, monkeypatch):
    sent = {}
    monkeypatch.setattr(payment, "create_payment_checkout", lambda **kw: sent.update(kw) or {"id": "cs_1", "url": "https://x"})
    payment.create_report_checkout(flagged_bill, "buyer@example.com")
    assert sent["amount_cents"] == 1999 and sent["metadata"]["bill_id"] == flagged_bill
    assert sent["metadata"]["payment_purpose"] == config.REPORT_PAYMENT_PURPOSE
    assert "/report/success?session_id={CHECKOUT_SESSION_ID}" in sent["success_url"]
    assert sent["cancel_url"].endswith(f"/results/{flagged_bill}#unlock")


def test_checkout_rejects_a_bad_email_without_calling_stripe(flagged_bill, monkeypatch):
    monkeypatch.setattr(payment, "create_report_checkout", lambda *a: pytest.fail("Stripe must not be called"))
    response = client.post("/report/checkout", data={"bill_id": flagged_bill, "email": "not-an-email"})
    assert response.headers["location"] == f"/results/{flagged_bill}?checkout_error=email#unlock"
    page = client.get(response.headers["location"].split("#")[0])
    assert "Please enter a valid email address." in page.text


def test_checkout_failure_sends_the_buyer_back_with_a_clear_message(flagged_bill, monkeypatch):
    def boom(bill_id, email):
        raise RuntimeError("Stripe is down")
    monkeypatch.setattr(payment, "create_report_checkout", boom)
    response = client.post("/report/checkout", data={"bill_id": flagged_bill, "email": "buyer@example.com"})
    assert response.headers["location"] == f"/results/{flagged_bill}?checkout_error=unavailable#unlock"
    assert "Checkout isn&rsquo;t available right now" in client.get(f"/results/{flagged_bill}?checkout_error=unavailable").text


def test_a_bill_with_nothing_flagged_is_never_charged(clean_bill, monkeypatch):
    monkeypatch.setattr(payment, "create_report_checkout", lambda *a: pytest.fail("a clean bill must not reach Stripe"))
    response = client.post("/report/checkout", data={"bill_id": clean_bill, "email": "buyer@example.com"})
    assert response.headers["location"] == f"/results/{clean_bill}"
    page = text_of(client.get(f"/results/{clean_bill}"))
    assert "Your bill looks clean" in page and "nothing to unlock and nothing to pay" in page
    assert "Unlock my report" not in page


def test_an_already_unlocked_bill_is_not_charged_again(flagged_bill, monkeypatch):
    unlock(flagged_bill)
    monkeypatch.setattr(payment, "create_report_checkout", lambda *a: pytest.fail("must not charge twice"))
    response = client.post("/report/checkout", data={"bill_id": flagged_bill, "email": "buyer@example.com"})
    assert response.headers["location"] == f"/results/{flagged_bill}"


def test_a_buyer_who_paid_but_beat_the_webhook_is_not_charged_twice(flagged_bill, monkeypatch):
    report.record_pending(flagged_bill, "cs_paid", "buyer@example.com")
    monkeypatch.setattr(payment, "get_session", lambda sid: {"payment_status": "paid"})
    monkeypatch.setattr(payment, "create_report_checkout", lambda *a: pytest.fail("must not charge twice"))
    response = client.post("/report/checkout", data={"bill_id": flagged_bill, "email": "buyer@example.com"})
    assert response.headers["location"] == f"/results/{flagged_bill}?unlocked=1"
    assert report.is_paid(flagged_bill)


# ── Unlocking ──────────────────────────────────────────────────────────────────

def test_a_signed_paid_webhook_unlocks_the_report(flagged_bill):
    unlock(flagged_bill)
    assert report.is_paid(flagged_bill)
    html = client.get(f"/results/{flagged_bill}").text
    assert "Charges we flagged" in html and "Medicare pays $" in html
    assert 'id="gen-letter-btn"' in html and 'id="gen-phone-btn"' in html
    assert "Unlock my report" not in html


def test_an_unpaid_or_unsigned_webhook_unlocks_nothing(flagged_bill):
    report.record_pending(flagged_bill, "cs_x", "buyer@example.com")
    assert send_webhook("cs_x", flagged_bill, paid=False).status_code == 200
    assert not report.is_paid(flagged_bill)
    forged = client.post("/api/stripe/webhook", content="{}", headers={"stripe-signature": "t=1,v1=bad"})
    assert forged.status_code == 400


def test_the_webhook_is_idempotent(flagged_bill):
    unlock(flagged_bill)
    assert send_webhook("cs_test_1", flagged_bill).status_code == 200
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) AS n FROM report_unlocks WHERE bill_id = ?", (flagged_bill,)).fetchone()["n"] == 1


def test_only_the_unlocked_page_ships_the_script_behind_the_letter_and_phone_buttons(flagged_bill):
    letter_call, phone_call = "fetch('/api/dispute-letter/'", "fetch('/api/dispute-phone-script/'"
    locked = client.get(f"/results/{flagged_bill}").text
    assert letter_call not in locked and phone_call not in locked
    unlock(flagged_bill)
    unlocked = client.get(f"/results/{flagged_bill}").text
    assert letter_call in unlocked and phone_call in unlocked


def test_unlocked_api_serves_letter_script_and_full_results(flagged_bill):
    unlock(flagged_bill)
    assert client.post(f"/api/dispute-letter/{flagged_bill}", json={"finding_ids": []}).status_code == 200
    assert client.get(f"/api/dispute-phone-script/{flagged_bill}").status_code == 200
    assert "findings" in client.get(f"/api/results/{flagged_bill}").json()["data"]


def test_unlocking_one_bill_does_not_unlock_another(flagged_bill):
    other = save_bill_and_findings(None, SAMPLE_BILL, analyze_bill(SAMPLE_BILL, "33021"), "33021")
    unlock(flagged_bill)
    assert client.get(f"/api/dispute-phone-script/{other}").status_code == 402


def test_the_unlocked_page_says_so_after_checkout(flagged_bill):
    unlock(flagged_bill)
    html = text_of(client.get(f"/results/{flagged_bill}?unlocked=1"))
    assert "Your report is unlocked." in html and "Your next steps" in html


# ── Returning from Stripe ──────────────────────────────────────────────────────

def test_success_page_for_an_unknown_session_is_a_clear_404():
    assert client.get("/report/success?session_id=cs_nope").status_code == 404
    assert client.get("/report/success").status_code == 404


def test_success_confirms_with_stripe_and_opens_the_report(flagged_bill, monkeypatch):
    report.record_pending(flagged_bill, "cs_ok", "buyer@example.com")
    monkeypatch.setattr(payment, "get_session", lambda sid: {"payment_status": "paid"})
    response = client.get("/report/success?session_id=cs_ok")
    assert response.status_code == 303 and response.headers["location"] == f"/results/{flagged_bill}?unlocked=1"
    assert report.is_paid(flagged_bill)


def test_success_waits_politely_while_payment_is_unconfirmed(flagged_bill, monkeypatch):
    report.record_pending(flagged_bill, "cs_wait", "buyer@example.com")
    monkeypatch.setattr(payment, "get_session", lambda sid: {"payment_status": "unpaid"})
    response = client.get("/report/success?session_id=cs_wait")
    assert response.status_code == 200 and 'http-equiv="refresh"' in response.text
    assert "Confirming your payment" in response.text and not report.is_paid(flagged_bill)


def test_success_survives_a_stripe_outage(flagged_bill, monkeypatch):
    report.record_pending(flagged_bill, "cs_out", "buyer@example.com")
    def boom(sid):
        raise RuntimeError("Stripe down")
    monkeypatch.setattr(payment, "get_session", boom)
    assert client.get("/report/success?session_id=cs_out").status_code == 200


# ── Everything else is hidden ──────────────────────────────────────────────────

@pytest.mark.parametrize("path", [
    "/autopilot/strategy/1", "/autopilot/dashboard/1", "/dispute/activate/1", "/dispute/dashboard",
    "/household", "/appeal", "/advisor/1", "/advocacy/login", "/fight-debt", "/collection-notice",
    "/charity-care", "/charity-care/apply", "/settle-debt", "/score/1",
])
def test_other_product_pages_send_the_visitor_to_the_free_scan(path):
    response = client.get(path)
    assert response.status_code == 302 and response.headers["location"] == "/scan"


@pytest.mark.parametrize("path", [
    "/api/dispute/checkout", "/api/appeal-template/1", "/api/phone-script/1", "/api/advisor/stream",
    "/api/autopilot/strategy", "/api/collection-notice/checkout", "/api/charity-care/application",
    "/api/household", "/api/advocacy/cases", "/api/negotiate/start", "/api/claims",
])
def test_other_product_api_routes_answer_404(path):
    for method in (client.get, client.post):
        response = method(path)
        assert response.status_code == 404 and response.json()["status"] == "error"


def test_the_free_surface_stays_open():
    for path in ("/", "/scan", "/guides/", "/hospitals/", "/itemized-bill", "/terms/", "/privacy/", "/about/"):
        assert client.get(path).status_code == 200, path


def test_no_visible_page_links_to_a_hidden_product():
    for path in ("/", "/scan", "/guides/", "/about/", "/terms/"):
        html = client.get(path).text
        for hidden in ('href="/household', 'href="/appeal', 'href="/collection-notice', 'href="/charity-care',
                       'href="/autopilot', 'href="/dispute/', 'href="/advocacy'):
            assert hidden not in html, (path, hidden)


def test_turning_the_flag_off_restores_free_results_and_the_hidden_routes(flagged_bill, monkeypatch):
    monkeypatch.setattr(config, "SLIM_LAUNCH", False)
    assert client.get(f"/api/dispute-phone-script/{flagged_bill}").status_code == 200
    assert "Unlock my report" not in client.get(f"/results/{flagged_bill}").text
    assert client.get("/household").status_code == 200


# ── Value prop is clear in every flow ──────────────────────────────────────────

def test_homepage_scan_and_results_all_state_the_same_offer(flagged_bill):
    home, scan, results = (text_of(client.get(p)) for p in ("/", "/scan", f"/results/{flagged_bill}"))
    assert "Free" in home and "$19.99" in home
    assert "Free to check, no account" in scan and "$19.99 only if you want the full report" in scan
    assert "$19.99" in results and "dispute letter" in results.lower() and "phone script" in results.lower()


def test_scan_faq_structured_data_matches_the_real_offer():
    scan = client.get("/scan").text
    assert "you can unlock the full report" in scan
    assert "negotiation services" not in scan


def test_terms_describe_the_report_not_a_dispute_service():
    html = text_of(client.get("/terms/"))
    assert "The Bill Check Report" in html and "e-sign" not in html.lower()


def test_the_sitemap_does_not_advertise_hidden_pages(monkeypatch):
    assert "/fight-debt" not in client.get("/sitemap-core.xml").text
    assert f"{config.APP_URL.rstrip('/')}/itemized-bill" in client.get("/sitemap-core.xml").text
    monkeypatch.setattr(config, "SLIM_LAUNCH", False)
    assert "/fight-debt" in client.get("/sitemap-core.xml").text


# ── /api/scan must not hand out the paid findings ──────────────────────────────

def test_scan_response_hides_findings_until_unlocked(monkeypatch):
    import scan_pipeline

    monkeypatch.setattr(scan_pipeline.scanner, "process_bill_with_verification", lambda *a: dict(SAMPLE_BILL))
    response = client.post(
        "/api/scan",
        files=[("images", ("bill.png", b"fake-image", "image/png"))],
        data={"zip_code": "33021"},
    )
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["analysis"]["locked"] is True
    assert "findings" not in data["analysis"]
    assert data["analysis"]["charge_count"] > 0
