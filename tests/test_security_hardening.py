"""Privacy and abuse protections added in the production-readiness pass."""

import io

import pytest
from fastapi.testclient import TestClient
from PIL import Image

import api
import config
import hold_calls
import scan_pipeline
import scanner
import twilio_client
from db import get_db
from main import app
from tests.conftest import SAMPLE_BILL

client = TestClient(app, follow_redirects=False)
PAGE = ("pages", ("bill.jpg", b"x", "image/jpeg"))


@pytest.fixture(autouse=True)
def setup(monkeypatch):
    monkeypatch.setattr(config, "SLIM_LAUNCH", True)
    monkeypatch.setattr(scan_pipeline.scanner, "process_bill_with_verification", lambda *a: dict(SAMPLE_BILL))
    api._rate_buckets.clear()


def device():
    data = client.post("/api/m/device", json={"app_version": "1.0.0"}).json()["data"]
    return data["device_id"], {"Authorization": f"Bearer {data['token']}"}


def test_deleting_a_device_removes_its_phone_numbers_calls_and_corrections():
    device_id, headers = device()
    bill_id = client.post("/api/m/scan", files=[PAGE], data={"zip_code": "33021"}, headers=headers).json()["data"]["bill_id"]
    with get_db() as db:
        db.execute("INSERT INTO phone_verifications (device_id, phone_hash, verified_at) VALUES (?, 'h', datetime('now'))", (device_id,))
        db.execute("INSERT INTO hold_call_credits (transaction_id, device_id) VALUES ('t1', ?)", (device_id,))
        call_id = db.execute("INSERT INTO hold_calls (bill_id, device_id, hospital_number, user_number) VALUES (?, ?, '+16195550142', '+16195550100')",
                             (bill_id, device_id)).lastrowid
        db.execute("INSERT INTO hold_call_events (call_id, status) VALUES (?, 'holding')", (call_id,))
        db.execute("INSERT INTO extraction_corrections (bill_id, line_index, field, extracted_value, confirmed_value) VALUES (?, 0, 'charged_amount', '1', '2')", (bill_id,))
    assert client.delete("/api/m/device", headers=headers).status_code == 200
    with get_db() as db:
        counts = [db.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0] for table in
                  ("phone_verifications", "hold_call_credits", "hold_calls", "hold_call_events", "extraction_corrections")]
    assert counts == [0, 0, 0, 0, 0]


def test_sms_codes_are_rate_limited_per_device_and_per_number(monkeypatch):
    monkeypatch.setattr(config, "HOLD_CALLS_ENABLED", True)
    monkeypatch.setattr(config, "TWILIO_VERIFY_SERVICE_SID", "VA1")
    sent = []
    monkeypatch.setattr(twilio_client, "start_verification", lambda phone: sent.append(phone))
    _, headers = device()
    codes = [client.post("/api/m/phone/verify", json={"phone": "(619) 555-0100"}, headers=headers).status_code for _ in range(5)]
    assert codes == [200, 200, 200, 429, 429] and len(sent) == 3  # three per number
    _, other = device()
    assert client.post("/api/m/phone/verify", json={"phone": "(619) 555-0100"}, headers=other).status_code == 429  # a victim's number can't be pumped from another device


def test_phone_numbers_are_validated(monkeypatch):
    monkeypatch.setattr(config, "HOLD_CALLS_ENABLED", True)
    _, headers = device()
    assert client.post("/api/m/phone/verify", json={"phone": "12345"}, headers=headers).status_code == 400
    assert client.post("/api/m/phone/verify/check", json={"phone": "(619) 555-0100", "code": "12ab56"}, headers=headers).status_code == 400


def test_unexpected_scan_errors_are_not_echoed_to_the_client(monkeypatch):
    def boom(*args):
        raise ValueError("secret internal detail /app/venv/site-packages/x.py line 4")
    monkeypatch.setattr(scan_pipeline.scanner, "process_bill_with_verification", boom)
    _, headers = device()
    response = client.post("/api/m/scan", files=[PAGE], data={"zip_code": "33021"}, headers=headers)
    assert response.status_code == 400 and "secret" not in response.text and "Try clearer photos" in response.text


def test_our_own_user_facing_errors_are_still_shown(monkeypatch):
    def bad_file(*args):
        raise ValueError("That file isn't a readable PDF. Try photos of the pages instead.")
    monkeypatch.setattr(scan_pipeline.scanner, "process_bill_with_verification", bad_file)
    _, headers = device()
    assert "readable PDF" in client.post("/api/m/scan", files=[PAGE], data={"zip_code": "33021"}, headers=headers).text


def test_a_decompression_bomb_sized_image_is_refused(monkeypatch):
    monkeypatch.setattr(config, "OCR_MAX_IMAGE_PIXELS", 100)
    buffer = io.BytesIO()
    Image.new("RGB", (50, 50)).save(buffer, format="PNG")
    with pytest.raises(ValueError, match="too large"):
        scanner._prepare_media_for_ocr(buffer.getvalue(), "image/png")


def test_stale_hold_calls_are_failed_and_their_numbers_hashed():
    device_id, headers = device()
    bill_id = client.post("/api/m/scan", files=[PAGE], data={"zip_code": "33021"}, headers=headers).json()["data"]["bill_id"]
    with get_db() as db:
        call_id = db.execute("INSERT INTO hold_calls (bill_id, device_id, hospital_number, user_number, status, created_at) "
                             "VALUES (?, ?, '+16195550142', '+16195550100', 'holding', datetime('now', '-3 hours'))", (bill_id, device_id)).lastrowid
    assert hold_calls.reap_stale_calls() == 1
    with get_db() as db:
        row = db.execute("SELECT status, user_number FROM hold_calls WHERE id = ?", (call_id,)).fetchone()
    assert row["status"] == "failed" and "555" not in row["user_number"]


def test_the_indexnow_admin_endpoint_is_closed_without_a_configured_token(monkeypatch):
    monkeypatch.setattr(config, "ADMIN_API_TOKEN", "")
    assert client.post("/admin/ping-indexnow").status_code == 401
    monkeypatch.setattr(config, "ADMIN_API_TOKEN", "s3cret")
    assert client.post("/admin/ping-indexnow", headers={"X-Admin-Token": "wrong"}).status_code == 401
