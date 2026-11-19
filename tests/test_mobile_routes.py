"""The iOS app API: anonymous devices, locked/unlocked bill views, in-app purchase unlocks, data deletion."""

import hashlib
import json

import pytest
from fastapi.testclient import TestClient

import api
import config
import mobile_purchases
import report
import scan_pipeline
from db import get_db
from main import app
from tests.conftest import SAMPLE_BILL

client = TestClient(app, follow_redirects=False)
WEBHOOK_AUTH = "hook-secret"
PAGE = ("pages", ("bill.jpg", b"fake-image", "image/jpeg"))


@pytest.fixture(autouse=True)
def mobile_setup(monkeypatch):
    monkeypatch.setattr(config, "SLIM_LAUNCH", True)
    monkeypatch.setattr(config, "REVENUECAT_SECRET_API_KEY", "")
    monkeypatch.setattr(config, "REVENUECAT_WEBHOOK_AUTH", WEBHOOK_AUTH)
    monkeypatch.setattr(scan_pipeline.scanner, "process_bill_with_verification", lambda *a: dict(SAMPLE_BILL))
    api._rate_buckets.clear()


def new_device():
    data = client.post("/api/m/device", json={"app_version": "1.0.0"}).json()["data"]
    return data["device_id"], {"Authorization": f"Bearer {data['token']}"}


def scan(headers, zip_code="33021"):
    response = client.post("/api/m/scan", files=[PAGE], data={"zip_code": zip_code}, headers=headers)
    assert response.status_code == 200, response.text
    return response.json()["data"]


def clean_scan(headers, monkeypatch):
    empty = {"findings": [], "total_findings": 0, "total_potential_savings": 0}
    monkeypatch.setattr(scan_pipeline.analyzer, "analyze_bill", lambda extracted, zip_code: empty)
    return scan(headers)


# ── Devices and profile ────────────────────────────────────────────────────────

def test_registered_device_can_list_bills_and_bad_token_cannot():
    _, headers = new_device()
    assert client.get("/api/m/bills", headers=headers).json() == {"status": "ok", "data": {"bills": [], "free_checks_remaining": config.FREE_CHECKS_LIMIT}}
    assert client.get("/api/m/bills", headers={"Authorization": "Bearer nope"}).status_code == 401
    assert client.get("/api/m/bills").status_code == 401


def test_token_is_stored_only_as_a_hash():
    client.post("/api/m/device", json={"app_version": "1.0.0"})
    with get_db() as db:
        row = db.execute("SELECT token_hash FROM mobile_devices").fetchone()
    assert len(row["token_hash"]) == len(hashlib.sha256(b"x").hexdigest())


def test_profile_saves_onboarding_answers_and_rejects_unknown_values():
    device_id, headers = new_device()
    answers = {
        "zip_code": "92111", "attribution_source": "tiktok", "bill_type": "er", "amount_band": "2k_10k",
        "insurance_status": "uninsured", "situations": ["too_high", "collections"], "due_band": "past_due",
        "onboarding_variant": "A",
    }
    assert client.post("/api/m/profile", json=answers, headers=headers).status_code == 200
    with get_db() as db:
        row = db.execute("SELECT * FROM mobile_devices WHERE device_id = ?", (device_id,)).fetchone()
    assert (row["zip_code"], row["bill_type"], row["situations_json"]) == ("92111", "er", '["collections", "too_high"]')
    assert client.post("/api/m/profile", json={"bill_type": "pet_vet"}, headers=headers).status_code == 400
    assert client.post("/api/m/profile", json={"zip_code": "9211"}, headers=headers).status_code == 400


def test_events_keep_known_names_only():
    device_id, headers = new_device()
    client.post("/api/m/events", json={"name": "paywall_viewed", "props": {"variant": "A"}}, headers=headers)
    client.post("/api/m/events", json={"name": "made_up_event"}, headers=headers)
    with get_db() as db:
        names = [r["name"] for r in db.execute("SELECT name FROM mobile_events WHERE device_id = ?", (device_id,))]
    assert names == ["paywall_viewed"]


# ── Scan and the locked view ───────────────────────────────────────────────────

def test_flagged_scan_is_locked_with_a_teaser_and_no_charge_details():
    _, headers = new_device()
    view = scan(headers)
    assert view["locked"] is True
    assert view["report"] is None
    assert view["teaser"]["charge_count"] > 0
    assert view["price"] == {"report_product_id": "bk_report_unlock", "plus_default_min_owed": config.PLUS_DEFAULT_MIN_OWED}
    assert view["bill"]["provider_name"] == "Memorial Regional Hospital"
    assert view["free_charge"]["description"]
    assert "finding_ids" not in str(view)
    shown = [i for i in SAMPLE_BILL["line_items"] if i["description"] in str(view)]
    assert len(shown) <= 1


def test_clean_scan_is_unlocked_without_payment(monkeypatch):
    _, headers = new_device()
    view = clean_scan(headers, monkeypatch)
    assert view["locked"] is False
    assert view["report"]["charges"] == []


def test_scan_rejects_bad_zip_and_wrong_file_type():
    _, headers = new_device()
    assert client.post("/api/m/scan", files=[PAGE], data={"zip_code": "abc"}, headers=headers).status_code == 400
    bad = ("pages", ("bill.txt", b"hello", "text/plain"))
    assert client.post("/api/m/scan", files=[bad], data={"zip_code": "33021"}, headers=headers).status_code == 400


def test_another_device_cannot_read_a_bill():
    _, headers_a = new_device()
    _, headers_b = new_device()
    bill_id = scan(headers_a)["bill_id"]
    assert client.get(f"/api/m/bills/{bill_id}", headers=headers_a).status_code == 200
    assert client.get(f"/api/m/bills/{bill_id}", headers=headers_b).status_code == 403
    assert client.get("/api/m/bills", headers=headers_b).json()["data"]["bills"] == []


# ── In-app purchases ───────────────────────────────────────────────────────────

def test_purchase_unlocks_the_report_and_a_second_bill_cannot_reuse_it():
    _, headers = new_device()
    first, second = scan(headers)["bill_id"], scan(headers)["bill_id"]
    unlocked = client.post(f"/api/m/bills/{first}/unlock", json={"transaction_id": "test_tx1"}, headers=headers)
    assert unlocked.status_code == 200
    view = unlocked.json()["data"]
    assert view["locked"] is False
    assert view["report"]["charges"][0]["finding_ids"]
    again = client.post(f"/api/m/bills/{first}/unlock", json={"transaction_id": "test_tx1"}, headers=headers)
    assert again.status_code == 200
    reuse = client.post(f"/api/m/bills/{second}/unlock", json={"transaction_id": "test_tx1"}, headers=headers)
    assert reuse.status_code == 409
    assert client.get(f"/api/m/bills/{second}", headers=headers).json()["data"]["locked"] is True


def test_unverifiable_purchase_does_not_unlock():
    _, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    response = client.post(f"/api/m/bills/{bill_id}/unlock", json={"transaction_id": "forged-123"}, headers=headers)
    assert response.status_code == 402
    assert client.get(f"/api/m/bills/{bill_id}", headers=headers).json()["data"]["locked"] is True


def test_letter_and_phone_script_need_the_unlock():
    _, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    letter = {"requestor_name": "Maria Lopez", "account_number": "ACCT-88213"}
    assert client.post(f"/api/m/bills/{bill_id}/letter", json=letter, headers=headers).status_code == 402
    assert client.get(f"/api/m/bills/{bill_id}/phone-script", headers=headers).status_code == 402
    client.post(f"/api/m/bills/{bill_id}/unlock", json={"transaction_id": "test_tx2"}, headers=headers)
    result = client.post(f"/api/m/bills/{bill_id}/letter", json=letter, headers=headers)
    assert result.status_code == 200
    assert "Maria Lopez" in result.json()["data"]["letter"]
    assert client.get(f"/api/m/bills/{bill_id}/phone-script", headers=headers).json()["data"]["script"]


def plus_event(device_id, kind, ms=None):
    event = {"type": kind, "app_user_id": device_id, "entitlement_ids": ["plus"], "expiration_at_ms": ms}
    return client.post("/api/m/revenuecat/webhook", json={"event": event}, headers={"Authorization": WEBHOOK_AUTH})


def test_plus_subscription_unlocks_bills_and_keeps_them_after_it_lapses():
    device_id, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    assert client.post(f"/api/m/bills/{bill_id}/unlock", json={}, headers=headers).status_code == 402
    assert plus_event(device_id, "INITIAL_PURCHASE", 4102444800000).status_code == 200
    assert client.post(f"/api/m/bills/{bill_id}/unlock", json={}, headers=headers).json()["data"]["locked"] is False
    assert scan(headers)["locked"] is False
    assert plus_event(device_id, "EXPIRATION").status_code == 200
    assert client.get(f"/api/m/bills/{bill_id}", headers=headers).json()["data"]["locked"] is False
    assert scan(headers)["locked"] is True


def test_webhook_rejects_wrong_auth():
    event = {"event": {"type": "INITIAL_PURCHASE", "app_user_id": "x", "entitlement_ids": ["plus"]}}
    assert client.post("/api/m/revenuecat/webhook", json=event, headers={"Authorization": "wrong"}).status_code == 401
    assert client.post("/api/m/revenuecat/webhook", json=event).status_code == 401


def test_refund_of_a_report_purchase_relocks_the_bill():
    device_id, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    client.post(f"/api/m/bills/{bill_id}/unlock", json={"transaction_id": "test_tx3"}, headers=headers)
    refund = {"type": "CANCELLATION", "app_user_id": device_id, "product_id": "bk_report_unlock",
              "transaction_id": "test_tx3"}
    client.post("/api/m/revenuecat/webhook", json={"event": refund}, headers={"Authorization": WEBHOOK_AUTH})
    assert client.get(f"/api/m/bills/{bill_id}", headers=headers).json()["data"]["locked"] is True


def test_revenuecat_lookup_is_used_outside_mock_mode(monkeypatch):
    monkeypatch.setattr(config, "REVENUECAT_SECRET_API_KEY", "sk_live_x")
    seen = {}
    purchases = {"bk_report_unlock": [{"store_transaction_id": "2000000123"}]}
    monkeypatch.setattr(mobile_purchases, "_fetch_subscriber", lambda d: seen.setdefault("d", d) and {"non_subscriptions": purchases})
    device_id, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    assert client.post(f"/api/m/bills/{bill_id}/unlock", json={"transaction_id": "test_tx9"}, headers=headers).status_code == 402
    ok = client.post(f"/api/m/bills/{bill_id}/unlock", json={"transaction_id": "2000000123"}, headers=headers)
    assert ok.status_code == 200 and seen["d"] == device_id


# ── Deleting data ──────────────────────────────────────────────────────────────

def test_delete_bill_removes_it_for_the_device():
    _, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    assert client.delete(f"/api/m/bills/{bill_id}", headers=headers).json()["data"] == {"deleted": True}
    assert client.get("/api/m/bills", headers=headers).json()["data"]["bills"] == []


def test_delete_device_removes_bills_events_and_the_device():
    device_id, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    client.post("/api/m/events", json={"name": "scan_started"}, headers=headers)
    assert client.delete("/api/m/device", headers=headers).status_code == 200
    with get_db() as db:
        counts = [db.execute(sql, (arg,)).fetchone()[0] for sql, arg in [
            ("SELECT COUNT(*) FROM bills WHERE id = ?", bill_id),
            ("SELECT COUNT(*) FROM bill_access_sessions WHERE session_id = ?", device_id),
            ("SELECT COUNT(*) FROM mobile_events WHERE device_id = ?", device_id),
            ("SELECT COUNT(*) FROM mobile_devices WHERE device_id = ?", device_id),
        ]]
    assert counts == [0, 0, 0, 0]
    assert client.get("/api/m/bills", headers=headers).status_code == 401


# ── Hospital lookup for onboarding ─────────────────────────────────────────────

def seed_hospital(facility_id, name, procedures, markup=4.2):
    with get_db() as db:
        db.execute(
            "INSERT INTO hospitals (facility_id, name, city, state, slug, state_slug, city_slug) "
            "VALUES (?, ?, 'San Diego', 'CA', ?, 'california', 'san-diego')",
            (facility_id, name, facility_id),
        )
        db.execute(
            "INSERT INTO billing_metrics (facility_id, avg_markup_vs_medicare, procedures_compared, billing_grade) "
            "VALUES (?, ?, ?, 'D')",
            (facility_id, markup, procedures),
        )


def test_hospital_search_returns_facility_id():
    seed_hospital("050100", "SCRIPPS MERCY HOSPITAL", 12)
    _, headers = new_device()
    results = client.get("/api/m/hospitals/search?q=scripps", headers=headers).json()["data"]["hospitals"]
    assert results[0]["facility_id"] == "050100" and results[0]["city"] == "San Diego"
    assert client.get("/api/m/hospitals/search?q=s", headers=headers).json()["data"]["hospitals"] == []


def test_hospital_insight_needs_enough_procedures():
    seed_hospital("050100", "SCRIPPS MERCY HOSPITAL", 12)
    seed_hospital("050200", "SMALL DATA HOSPITAL", config.RANKING_MIN_PROCEDURES - 1)
    _, headers = new_device()
    full = client.get("/api/m/hospital-insight?facility_id=050100", headers=headers).json()["data"]
    assert (full["avg_markup"], full["billing_grade"], full["procedures_compared"]) == (4.2, None, 12)  # fewer than GRADE_MIN_PROCEDURES compared: no grade shown
    assert client.get("/api/m/hospital-insight?facility_id=050200", headers=headers).json()["data"] is None
    assert client.get("/api/m/hospital-insight?facility_id=999999", headers=headers).json()["data"] is None


# ── Universal links ────────────────────────────────────────────────────────────

def test_apple_app_site_association_serves_json(monkeypatch):
    assert client.get("/.well-known/apple-app-site-association").status_code == 404
    monkeypatch.setattr(config, "IOS_APP_ID", "ABCDE12345.app.billkarma.ios")
    response = client.get("/.well-known/apple-app-site-association")
    assert response.headers["content-type"].startswith("application/json")
    assert response.json()["applinks"]["details"][0]["appIDs"] == ["ABCDE12345.app.billkarma.ios"]
    assert client.get("/app/scan").headers["location"] == "/scan"


def test_outcome_is_recorded_and_bad_input_rejected():
    _, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    good = client.post(f"/api/m/bills/{bill_id}/outcome", json={"outcome": "reduced", "final_patient_owes": 0}, headers=headers)
    assert good.status_code == 200 and good.json()["data"]["actual_savings"] >= 0
    bad = client.post(f"/api/m/bills/{bill_id}/outcome", json={"outcome": "magic"}, headers=headers)
    assert bad.status_code == 400
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) FROM dispute_outcomes WHERE bill_id = ?", (bill_id,)).fetchone()[0] == 1


def test_rejection_reason_is_validated_and_stored():
    _, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    bad = client.post(f"/api/m/bills/{bill_id}/outcome", json={"outcome": "no_change", "final_patient_owes": 100, "reason_category": "rude"}, headers=headers)
    assert bad.status_code == 400
    good = client.post(f"/api/m/bills/{bill_id}/outcome", json={"outcome": "no_change", "final_patient_owes": 100, "reason_category": "modifier"}, headers=headers)
    assert good.status_code == 200
    with get_db() as db:
        assert db.execute("SELECT reason_category FROM dispute_outcomes WHERE bill_id = ?", (bill_id,)).fetchone()[0] == "modifier"


def test_assistance_check_letter_and_wins():
    _, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    assert client.get("/api/m/assistance/guidelines", headers=headers).json()["data"]["year"] == 2026
    check = client.post(f"/api/m/bills/{bill_id}/assistance", json={"fpl_percentage": 140, "household_size": 3}, headers=headers)
    assert check.json()["data"]["eligibility"] == "likely_full"
    letter = client.post(f"/api/m/bills/{bill_id}/assistance-letter",
                         json={"fpl_percentage": 140, "household_size": 3, "name": "Dana Reyes"}, headers=headers)
    assert "Financial Assistance" in letter.json()["data"]["letter"]
    assert client.post(f"/api/m/bills/{bill_id}/assistance", json={"fpl_percentage": -5, "household_size": 3}, headers=headers).status_code == 400
    assert client.get("/api/m/wins", headers=headers).json()["data"]["reports"] == 0
    client.post(f"/api/m/bills/{bill_id}/outcome", json={"outcome": "no_change", "final_patient_owes": 9999999}, headers=headers)
    assert client.get("/api/m/wins", headers=headers).json()["data"]["total_saved"] == 0


# ── Insurance statement (EOB) ──────────────────────────────────────────────────

EOB_PAGE = ("eob_pages", ("eob.jpg", b"fake-eob", "image/jpeg"))


def fake_pages(eob_owes):
    eob = {"bill_date": "2026-10-03", "total_patient_owes": eob_owes, "line_items": []}
    return lambda images: eob if images[0][0] == b"fake-eob" else dict(SAMPLE_BILL)


def test_scan_with_a_statement_flags_a_bill_that_asks_for_more(monkeypatch):
    monkeypatch.setattr(scan_pipeline, "extract_pages", fake_pages(640.0))
    _, headers = new_device()
    response = client.post("/api/m/scan", files=[PAGE, EOB_PAGE], data={"zip_code": "33021"}, headers=headers)
    check = response.json()["data"]["insurance_check"]
    assert check == {"status": "mismatch", "eob_owed": 640.0, "bill_owed": 4215.0, "difference": 3575.0, "eob_date": "2026-10-03"}


def test_statement_lines_become_observations_only_for_a_consenting_device(monkeypatch):
    with get_db() as db:
        db.execute("INSERT OR IGNORE INTO hospitals (facility_id, name, city, state, zip, slug, state_slug, city_slug) "
                   "VALUES ('999001', ?, 'Miami', 'FL', '33021', 'x', 'florida', 'miami')", (SAMPLE_BILL["provider_name"],))
    eob = {"bill_date": "2026-10-03", "insurer_name": "Aetna", "total_patient_owes": 640.0, "line_items": [
        {"cpt_code": "99285", "allowed_amount": 900.0, "charged_amount": 4200.0}]}
    monkeypatch.setattr(scan_pipeline, "extract_pages", lambda images: eob if images[0][0] == b"fake-eob" else dict(SAMPLE_BILL))

    def observations():
        with get_db() as db:
            return db.execute("SELECT COUNT(*) FROM price_observations WHERE source_type = 'eob'").fetchone()[0]

    device_id, headers = new_device()
    client.post("/api/m/scan", files=[PAGE, EOB_PAGE], data={"zip_code": "33021"}, headers=headers)
    assert observations() == 0
    with get_db() as db:
        db.execute("UPDATE mobile_devices SET data_improvement = 1 WHERE device_id = ?", (device_id,))
    client.post("/api/m/scan", files=[PAGE, EOB_PAGE], data={"zip_code": "33021"}, headers=headers)
    assert observations() == 1


def test_statement_that_agrees_with_the_bill_matches_and_unreadable_is_reported(monkeypatch):
    _, headers = new_device()
    monkeypatch.setattr(scan_pipeline, "extract_pages", fake_pages(4215.0))
    match = client.post("/api/m/scan", files=[PAGE, EOB_PAGE], data={"zip_code": "33021"}, headers=headers)
    assert match.json()["data"]["insurance_check"] == {"status": "match"}
    monkeypatch.setattr(scan_pipeline, "extract_pages", fake_pages(None))
    unreadable = client.post("/api/m/scan", files=[PAGE, EOB_PAGE], data={"zip_code": "33021"}, headers=headers)
    assert unreadable.json()["data"]["insurance_check"] == {"status": "unreadable"}


def test_bill_without_a_statement_has_no_insurance_check():
    _, headers = new_device()
    assert scan(headers)["insurance_check"] is None


def test_adding_a_statement_later_keeps_the_same_bill_and_unlock(monkeypatch):
    device_id, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    report.record_pending(bill_id, "iap:test", "")
    report.mark_paid("iap:test")
    monkeypatch.setattr(scan_pipeline, "extract_pages", fake_pages(640.0))
    response = client.post(f"/api/m/bills/{bill_id}/eob", files=[EOB_PAGE], headers=headers)
    data = response.json()["data"]
    assert data["bill_id"] == bill_id and data["locked"] is False
    assert data["insurance_check"]["status"] == "mismatch"


def test_adding_a_statement_to_a_bill_with_no_stored_lines_asks_for_a_rescan(monkeypatch):
    _, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    with get_db() as db:
        db.execute("DELETE FROM line_items WHERE bill_id = ?", (bill_id,))
    response = client.post(f"/api/m/bills/{bill_id}/eob", files=[EOB_PAGE], headers=headers)
    assert response.status_code == 409


def test_letter_names_the_statement_amounts():
    from dispute_workflow import _eob_paragraph
    text = _eob_paragraph("99285", "ER visit", "$4,500.00", "2026-01-10",
                          {"eob_patient_owes": 640.0, "total_patient_owes": 1840.0, "eob_date": "2026-10-03"})
    assert "$640.00" in text and "$1,840.00" in text and "$1,200.00" in text and "2026-10-03" in text


# ── Sending the letter ─────────────────────────────────────────────────────────

def unlocked_bill(headers):
    bill_id = scan(headers)["bill_id"]
    report.record_pending(bill_id, f"iap:{bill_id}", "")
    report.mark_paid(f"iap:{bill_id}")
    return bill_id


def test_contact_uses_printed_details_and_never_invents_an_email(monkeypatch):
    printed = {**SAMPLE_BILL, "billing_phone": "(954) 555-0142", "billing_email": "not an email",
               "billing_address": "PO Box 100, Hollywood FL 33021"}
    monkeypatch.setattr(scan_pipeline.scanner, "process_bill_with_verification", lambda *a: dict(printed))
    _, headers = new_device()
    bill_id = unlocked_bill(headers)
    data = client.get(f"/api/m/bills/{bill_id}/contact", headers=headers).json()["data"]
    assert data["phone"] == "(954) 555-0142" and data["email"] is None
    assert data["address"].startswith("PO Box 100") and data["source"] == "bill"


def test_contact_needs_an_unlocked_bill():
    _, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    assert client.get(f"/api/m/bills/{bill_id}/contact", headers=headers).status_code == 402


def test_sent_is_recorded_and_shows_in_my_bills():
    _, headers = new_device()
    bill_id = unlocked_bill(headers)
    assert client.post(f"/api/m/bills/{bill_id}/sent", json={"channel": "fax"}, headers=headers).status_code == 400
    assert client.post(f"/api/m/bills/{bill_id}/sent", json={"channel": "email"}, headers=headers).status_code == 200
    summary = client.get("/api/m/bills", headers=headers).json()["data"]["bills"][0]
    assert summary["sent_at"]


def test_improvement_consent_is_off_by_default_logged_and_must_be_a_boolean():
    device_id, headers = new_device()
    with get_db() as db:
        assert db.execute("SELECT data_improvement FROM mobile_devices WHERE device_id = ?", (device_id,)).fetchone()[0] == 0
    assert client.post("/api/m/consent", json={"granted": "yes"}, headers=headers).status_code == 400
    assert client.post("/api/m/consent", json={"granted": True}, headers=headers).status_code == 200
    with get_db() as db:
        assert db.execute("SELECT data_improvement FROM mobile_devices WHERE device_id = ?", (device_id,)).fetchone()[0] == 1
        assert db.execute("SELECT COUNT(*) FROM consent_logs WHERE consent_type = 'data_improvement'").fetchone()[0] >= 1


# ── Verified outcomes ──────────────────────────────────────────────────────────

def statement(owes, provider="Memorial Regional Hospital"):
    return lambda images: {"provider_name": provider, "total_patient_owes": owes, "line_items": []}


def verify_call(headers, bill_id):
    return client.post(f"/api/m/bills/{bill_id}/outcome/verify", files=[("pages", ("new.jpg", b"new-statement", "image/jpeg"))], headers=headers)


def test_a_lower_balance_from_the_same_hospital_verifies_and_earns_plus(monkeypatch):
    device_id, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    client.post(f"/api/m/bills/{bill_id}/outcome", json={"outcome": "reduced", "final_patient_owes": 3000}, headers=headers)
    monkeypatch.setattr(scan_pipeline, "extract_pages", statement(1500.0))
    result = verify_call(headers, bill_id).json()["data"]
    assert result == {"verified": True, "actual_savings": 2715.0, "reward_days": 90}
    assert mobile_purchases.plus_is_active(device_id)
    assert client.get("/api/m/wins", headers=headers).json()["data"]["total_saved"] == 2715.0


def test_unverified_reports_do_not_count_in_wins_and_bad_statements_do_not_verify(monkeypatch):
    device_id, headers = new_device()
    bill_id = scan(headers)["bill_id"]
    client.post(f"/api/m/bills/{bill_id}/outcome", json={"outcome": "reduced", "final_patient_owes": 100}, headers=headers)
    assert client.get("/api/m/wins", headers=headers).json()["data"]["total_saved"] == 0
    for owes, provider, reason in ((5000.0, "Memorial Regional Hospital", "not_lower"), (100.0, "Sunrise Clinic", "different_hospital"), (None, "Memorial Regional Hospital", "unreadable")):
        monkeypatch.setattr(scan_pipeline, "extract_pages", statement(owes, provider))
        assert verify_call(headers, bill_id).json()["data"] == {"verified": False, "reason": reason}
    assert not mobile_purchases.plus_is_active(device_id)


def test_hospital_outcomes_need_ten_verified_cases_per_rule():
    import json
    import outcome_stats
    with get_db() as db:
        db.execute("DELETE FROM dispute_outcomes WHERE facility_id = 'F9'")
        for index in range(12):
            db.execute("INSERT INTO dispute_outcomes (facility_id, verified, actual_savings, rule_ids) VALUES ('F9', 1, ?, ?)",
                       (100.0 if index < 9 else 0.0, json.dumps(["RULE_DUPLICATE_SAME_CODE_DATE_AMOUNT"])))
        for index in range(4):
            db.execute("INSERT INTO dispute_outcomes (facility_id, verified, actual_savings, rule_ids) VALUES ('F9', 1, 50, ?)",
                       (json.dumps(["RULE_NCCI_UNBUNDLING"]),))
    stats = outcome_stats.get_hospital_outcomes("F9")
    assert list(stats) == ["RULE_DUPLICATE_SAME_CODE_DATE_AMOUNT"]
    assert (stats["RULE_DUPLICATE_SAME_CODE_DATE_AMOUNT"]["verified"], stats["RULE_DUPLICATE_SAME_CODE_DATE_AMOUNT"]["succeeded"]) == (12, 9)
    assert outcome_stats.outcome_line("Harbor View", "F9", ["RULE_DUPLICATE_SAME_CODE_DATE_AMOUNT"]) == \
        "Harbor View corrected duplicate charges for 9 of 12 BillKarma users"


def test_scan_infers_the_bill_type_and_profile_patch_is_accepted():
    device_id, headers = new_device()
    scan(headers)
    with get_db() as db:
        assert db.execute("SELECT bill_type FROM mobile_devices WHERE device_id = ?", (device_id,)).fetchone()[0] == "er"
    assert client.patch("/api/m/profile", json={"situations": ["too_high"], "due_band": "this_month"}, headers=headers).status_code == 200


def test_locked_view_lists_evidence_kinds_of_locked_charges_and_no_line_details():
    _, headers = new_device()
    view = scan(headers)
    assert view["locked"] and view["teaser"]["locked_kinds"]
    assert set(view["teaser"]["locked_kinds"]) <= {"official", "bill", "check"}
    assert len(view["teaser"]["locked_kinds"]) == view["teaser"]["charge_count"] - 1
    free = view["free_charge"]
    text = json.dumps({key: value for key, value in view.items() if key != "free_charge"})
    for item in SAMPLE_BILL["line_items"]:
        if item["description"] != free["description"]:
            assert item["description"] not in text
    assert view["price"]["plus_default_min_owed"] == config.PLUS_DEFAULT_MIN_OWED


# ── Free check limit, public stats, explainer pages ────────────────────────────

def distinct_flagged_scan(headers, monkeypatch, provider, total):
    bill = {**SAMPLE_BILL, "provider_name": provider, "total_charged": total}
    monkeypatch.setattr(scan_pipeline.scanner, "process_bill_with_verification", lambda *a: dict(bill))
    return scan(headers)


def test_a_clean_bill_does_not_use_a_check_and_the_fourth_flagged_bill_has_no_free_preview(monkeypatch):
    _, headers = new_device()
    real_analyze = scan_pipeline.analyzer.analyze_bill
    clean = clean_scan(headers, monkeypatch)
    assert clean["free_checks_remaining"] == config.FREE_CHECKS_LIMIT
    monkeypatch.setattr(scan_pipeline.analyzer, "analyze_bill", real_analyze)
    views = [distinct_flagged_scan(headers, monkeypatch, f"Hospital {n} Medical Center", 12000.0 + n) for n in range(4)]
    assert [v["free_charge"] is not None for v in views] == [True, True, True, False]
    assert views[3]["free_checks_remaining"] == 0 and views[3]["free_limit_reached"] is True
    assert views[3]["teaser"]["charge_count"] > 0 and views[3]["teaser"]["locked_kinds"]
    assert client.get("/api/m/bills", headers=headers).json()["data"]["free_checks_remaining"] == 0


def test_rescanning_the_same_bill_does_not_use_another_check(monkeypatch):
    _, headers = new_device()
    for _ in range(3):
        view = scan(headers)
    assert view["free_checks_remaining"] == config.FREE_CHECKS_LIMIT - 1 and view["free_charge"] is not None


def test_public_stats_stay_null_until_the_totals_are_large_enough():
    assert client.get("/api/m/stats").json()["data"] == {"verified": None}


def test_explainer_pages_render():
    assert "Grade A" in client.get("/how-we-grade/").text
    assert "Medicare Physician Fee Schedule" in client.get("/sources/").text


def test_bill_view_names_the_hospital_so_the_app_can_load_its_policy():
    with get_db() as db:
        db.execute("DELETE FROM hospitals WHERE facility_id = 'FP1'")
        db.execute("INSERT INTO hospitals (facility_id, name, city, state, zip, slug, state_slug, city_slug) VALUES "
                   "('FP1', 'Memorial Regional Hospital', 'Hollywood', 'FL', '33021', 'memorial-regional', 'florida', 'hollywood')")
    _, headers = new_device()
    assert scan(headers)["facility_id"] == "FP1"
