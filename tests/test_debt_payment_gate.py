"""Security tests for debt-letter payment gating and anti-abuse rate limits."""

import os
import sys
from unittest.mock import MagicMock

import pytest

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import api as api_module  # noqa: E402
import config  # noqa: E402
from db import get_db  # noqa: E402
from main import app  # noqa: E402

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_debt_buckets():
    api_module._debt_rate_buckets.clear()
    yield
    api_module._debt_rate_buckets.clear()


def _insert_letter(stripe_payment_id: str | None = None) -> int:
    with get_db() as db:
        cur = db.execute(
            """
            INSERT INTO debt_letters (
                letter_type, user_name, collector_name, account_number, amount,
                letter_text, stripe_payment_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "debt_validation",
                "Test User",
                "Collector Co",
                "ACC-1",
                "100.00",
                "Sample letter text",
                stripe_payment_id,
            ),
        )
        return int(cur.lastrowid)


def test_send_letter_requires_prior_payment():
    letter_id = _insert_letter(None)
    resp = client.post(
        "/api/collection-notice/send",
        json={"debt_letter_id": letter_id, "letter_text": "Sample"},
        headers={"cf-connecting-ip": "198.51.100.10"},
    )
    assert resp.status_code == 402
    assert "Payment required" in resp.text


def test_send_letter_rejects_unpaid_stripe_session(monkeypatch):
    letter_id = _insert_letter("cs_unpaid")
    monkeypatch.setattr(
        api_module.payment_module,
        "get_session",
        lambda _sid: {"payment_status": "unpaid", "metadata": {"debt_letter_id": str(letter_id)}},
    )
    resp = client.post(
        "/api/collection-notice/send",
        json={"debt_letter_id": letter_id, "letter_text": "Sample"},
        headers={"cf-connecting-ip": "198.51.100.11"},
    )
    assert resp.status_code == 402


def test_send_letter_rejects_mismatched_paid_session(monkeypatch):
    letter_id = _insert_letter("cs_paid_bad_meta")
    monkeypatch.setattr(
        api_module.payment_module,
        "get_session",
        lambda _sid: {"payment_status": "paid", "metadata": {"debt_letter_id": "999999"}},
    )
    resp = client.post(
        "/api/collection-notice/send",
        json={"debt_letter_id": letter_id, "letter_text": "Sample"},
        headers={"cf-connecting-ip": "198.51.100.12"},
    )
    assert resp.status_code == 403


def test_send_letter_allows_paid_matching_session(monkeypatch):
    monkeypatch.setattr(config, "LOB_API_KEY", "")
    letter_id = _insert_letter("cs_paid_ok")
    monkeypatch.setattr(
        api_module.payment_module,
        "get_session",
        lambda _sid: {"payment_status": "paid", "metadata": {"debt_letter_id": str(letter_id)}},
    )
    resp = client.post(
        "/api/collection-notice/send",
        json={"debt_letter_id": letter_id, "letter_text": "Sample"},
        headers={"cf-connecting-ip": "198.51.100.13"},
    )
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_debt_generate_rate_limited_by_forwarded_ip(monkeypatch):
    monkeypatch.setattr(config, "DEBT_RATE_LIMIT_REQUESTS", 1)
    monkeypatch.setattr(config, "DEBT_RATE_LIMIT_WINDOW_SECONDS", 3600)

    payload = {
        "letter_type": "debt_validation",
        "user_name": "Rate Limit User",
        "user_address": "1 Main St, Miami, FL 33101",
        "collector_name": "Collector Co",
        "collector_address": "2 Elm St, Dallas, TX 75001",
        "account_number": "RATE-1",
        "amount": "100.00",
    }
    headers = {"cf-connecting-ip": "203.0.113.10"}
    first = client.post("/api/collection-notice/generate", json=payload, headers=headers)
    second = client.post("/api/collection-notice/generate", json=payload, headers=headers)
    assert first.status_code == 200
    assert second.status_code == 429
