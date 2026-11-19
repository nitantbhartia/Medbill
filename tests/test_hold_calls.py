"""B17.1: hold calls through a recorded phone call (menu, hold music, a person), missed calls, hours, budget and the kill switch."""

import base64
import hashlib
import hmac
from datetime import datetime, timezone

import pytest
from fastapi.testclient import TestClient

import api
import config
import hold_calls
import mobile_purchases
import report
import scan_pipeline
import twilio_client
from db import get_db
from main import app
from tests.conftest import SAMPLE_BILL

client = TestClient(app, follow_redirects=False)
WEEKDAY_NOON_UTC = datetime(2026, 11, 18, 20, 0, tzinfo=timezone.utc)   # Wednesday, noon in California
SATURDAY_UTC = datetime(2026, 11, 21, 20, 0, tzinfo=timezone.utc)
USER, HOSPITAL = "(619) 555-0100", "(619) 555-0142"

# What the hospital's line said, in order: a menu, a recording while holding, then a person.
RECORDED_CALL = ["Thank you for calling Harbor View. For billing questions press 2.", "Your call is important to us. Please hold.",
                 "Your call is important to us. Please hold.", "Hi, this is Maria in patient billing, how can I help you?"]


@pytest.fixture(autouse=True)
def setup(monkeypatch):
    sent = []
    monkeypatch.setattr(config, "HOLD_CALLS_ENABLED", True)
    monkeypatch.setattr(config, "SLIM_LAUNCH", True)
    monkeypatch.setattr(config, "TWILIO_ACCOUNT_SID", "AC123")
    monkeypatch.setattr(config, "TWILIO_AUTH_TOKEN", "secret")
    monkeypatch.setattr(config, "TWILIO_FROM_NUMBER", "+16195550000")
    monkeypatch.setattr(scan_pipeline.scanner, "process_bill_with_verification", lambda *a: dict(SAMPLE_BILL))
    monkeypatch.setattr(twilio_client, "create_call", lambda to, *a, **k: sent.append(("call", to, k)) or f"CA{len(sent)}")
    monkeypatch.setattr(twilio_client, "update_call", lambda sid, twiml: sent.append(("update", sid, twiml)))
    monkeypatch.setattr(twilio_client, "hang_up", lambda sid: sent.append(("hangup", sid)))
    api._rate_buckets.clear()
    return sent


@pytest.fixture
def sent(setup):
    return setup


def paid_bill_for_new_device():
    data = client.post("/api/m/device", json={"app_version": "1.0.0"}).json()["data"]
    headers = {"Authorization": f"Bearer {data['token']}"}
    bill_id = client.post("/api/m/scan", files=[("pages", ("b.jpg", b"x", "image/jpeg"))], data={"zip_code": "33021"}, headers=headers).json()["data"]["bill_id"]
    report.record_pending(bill_id, f"iap:{bill_id}", "")
    report.mark_paid(f"iap:{bill_id}")
    with get_db() as db:
        db.execute("INSERT INTO phone_verifications (device_id, phone_hash, verified_at) VALUES (?, ?, datetime('now'))",
                   (data["device_id"], hold_calls.phone_hash(USER)))
    return data["device_id"], bill_id, headers


def feed(call_id, lines):
    for text in lines:
        hold_calls.handle_utterance(call_id, text, lambda t: "2" if "press" in t.lower() else "WAIT", lambda t: "this is maria" in t.lower())


def start(device_id, bill_id, now=WEEKDAY_NOON_UTC):
    return hold_calls.request_call(device_id, bill_id, HOSPITAL, USER, now=now)


def status_of(call_id):
    with get_db() as db:
        return db.execute("SELECT * FROM hold_calls WHERE id = ?", (call_id,)).fetchone()


def test_a_recorded_call_goes_through_the_menu_holds_and_rings_the_patient_when_a_person_answers(sent):
    device_id, bill_id, _ = paid_bill_for_new_device()
    call_id = start(device_id, bill_id)["call_id"]
    feed(call_id, RECORDED_CALL)
    row = status_of(call_id)
    assert row["status"] == "connecting" and row["menu_path"] == "2" and row["human_at"]
    updates = [item for item in sent if item[0] == "update"]
    assert 'digits="w2"' in updates[0][2]
    assert config.HOLD_DISCLOSURE.split(",")[0] in updates[1][2] and "<Stop><Transcription/>" in updates[1][2]
    user_leg = [item for item in sent if item[0] == "call"][-1]
    assert user_leg[1] == "+16195550100" and user_leg[2]["timeout_seconds"] == config.HOLD_CALL_USER_RING_SECONDS


def test_nothing_after_the_person_answers_is_read(sent):
    device_id, bill_id, _ = paid_bill_for_new_device()
    call_id = start(device_id, bill_id)["call_id"]
    feed(call_id, RECORDED_CALL)
    before = len(sent)
    feed(call_id, ["Hi, this is Maria, who am I speaking with?", "The patient's name is Dana Reyes."])
    assert len(sent) == before and status_of(call_id)["status"] == "connecting"


def test_an_unanswered_patient_is_a_missed_call_that_keeps_the_included_call(sent):
    device_id, bill_id, _ = paid_bill_for_new_device()
    call_id = start(device_id, bill_id)["call_id"]
    feed(call_id, RECORDED_CALL)
    hold_calls.user_missed(call_id)
    assert status_of(call_id)["status"] == "missed" and hold_calls.entitlement(device_id, bill_id) == "included"
    assert any(config.HOLD_USER_MISSED_MESSAGE in item[2] for item in sent if item[0] == "update")


def test_a_connected_call_uses_the_included_call_and_the_numbers_are_hashed_afterwards(sent):
    device_id, bill_id, _ = paid_bill_for_new_device()
    call_id = start(device_id, bill_id)["call_id"]
    feed(call_id, RECORDED_CALL)
    hold_calls.user_answered(call_id)
    hold_calls.finish(call_id, "connected", "completed")
    assert hold_calls.entitlement(device_id, bill_id) is None
    stored = status_of(call_id)
    assert "555" not in stored["user_number"] and "555" not in stored["hospital_number"]


def test_a_hold_that_hits_the_limit_fails_without_using_the_call(sent):
    device_id, bill_id, _ = paid_bill_for_new_device()
    call_id = start(device_id, bill_id)["call_id"]
    hold_calls.call_ended(call_id, "completed")
    assert (status_of(call_id)["status"], status_of(call_id)["end_reason"]) == ("failed", "hold_timeout")
    assert hold_calls.entitlement(device_id, bill_id) == "included"


def test_a_request_outside_business_hours_is_queued_for_the_next_opening(sent):
    device_id, bill_id, _ = paid_bill_for_new_device()
    result = start(device_id, bill_id, now=SATURDAY_UTC)
    assert result["status"] == "queued" and result["starts_at"].startswith("2026-11-23T16:00")  # Monday 8:00 in California
    assert not [item for item in sent if item[0] == "call"]


def test_over_the_daily_budget_returns_503_with_a_clear_message(sent, monkeypatch):
    device_id, bill_id, headers = paid_bill_for_new_device()
    monkeypatch.setattr(config, "HOLD_CALL_DAILY_BUDGET_CENTS", 100)
    response = client.post(f"/api/m/bills/{bill_id}/hold-call", json={"hospital_number": HOSPITAL, "user_number": USER}, headers=headers)
    assert response.status_code == 503 and "limit for today" in response.json()["detail"]


def test_the_kill_switch_turns_everything_off(sent, monkeypatch):
    device_id, bill_id, headers = paid_bill_for_new_device()
    monkeypatch.setattr(config, "HOLD_CALLS_ENABLED", False)
    assert client.post(f"/api/m/bills/{bill_id}/hold-call", json={"hospital_number": HOSPITAL, "user_number": USER}, headers=headers).status_code == 503


def test_requests_need_an_unlocked_report_a_verified_number_and_only_one_active_call(sent):
    device_id, bill_id, headers = paid_bill_for_new_device()
    with pytest.raises(hold_calls.HoldCallError) as unverified:
        hold_calls.request_call(device_id, bill_id, HOSPITAL, "(619) 555-0199", now=WEEKDAY_NOON_UTC)
    assert unverified.value.status == 403
    start(device_id, bill_id)
    with pytest.raises(hold_calls.HoldCallError) as busy:
        start(device_id, bill_id)
    assert busy.value.status == 409


def test_webhooks_reject_a_bad_signature_and_accept_a_good_one(sent):
    device_id, bill_id, _ = paid_bill_for_new_device()
    call_id = start(device_id, bill_id)["call_id"]
    url = f"{config.APP_URL.rstrip('/')}/api/hold/twiml/{call_id}"
    assert client.post(f"/api/hold/twiml/{call_id}", data={"CallSid": "CA1"}, headers={"X-Twilio-Signature": "nope"}).status_code == 403
    signature = base64.b64encode(hmac.new(b"secret", (url + "CallSidCA1").encode(), hashlib.sha1).digest()).decode()
    good = client.post(f"/api/hold/twiml/{call_id}", data={"CallSid": "CA1"}, headers={"X-Twilio-Signature": signature})
    assert good.status_code == 200 and "<Transcription" in good.text
