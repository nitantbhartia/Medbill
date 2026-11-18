"""The iOS app API: anonymous devices, locked/unlocked bill views, in-app purchase unlocks, data deletion."""

import hashlib

import pytest
from fastapi.testclient import TestClient

import api
import config
import mobile_purchases
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
    assert client.get("/api/m/bills", headers=headers).json() == {"status": "ok", "data": {"bills": []}}
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
    assert view["price"] == {"report_product_id": "bk_report_unlock"}
    assert view["bill"]["provider_name"] == "Memorial Regional Hospital"
    for item in SAMPLE_BILL["line_items"]:
        assert item["description"] not in str(view)


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
    assert (full["avg_markup"], full["billing_grade"], full["procedures_compared"]) == (4.2, "D", 12)
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
