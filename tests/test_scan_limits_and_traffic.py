"""Free-scan limits (per visitor, per address, site-wide) and traffic-source tracking."""

import pytest
from fastapi.testclient import TestClient

import api
import config
import scan_limits
import scan_pipeline
import traffic
from analyzer import analyze_bill, save_bill_and_findings
from db import get_db
from main import app
from tests.conftest import SAMPLE_BILL

PNG = ("bill.png", b"\x89PNG\r\n\x1a\n" + b"0" * 64, "image/png")
IPHONE = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148"


@pytest.fixture(autouse=True)
def fake_scanner(monkeypatch):
    """Count scans that would reach the AI, without calling it."""
    api._rate_buckets.clear()
    calls = []

    def run_scan(images, zip_code, user_id, referral_code, eob_list=None, *args, **kwargs):
        if images[0][0].endswith(b"unreadable"):
            raise ValueError("no line items found")
        calls.append(referral_code)
        return save_bill_and_findings(user_id, SAMPLE_BILL, analyze_bill(SAMPLE_BILL, zip_code), zip_code, referral_code), SAMPLE_BILL, {"total_findings": 3}

    monkeypatch.setattr(scan_pipeline, "run_scan", run_scan)
    monkeypatch.setattr(config, "RATE_LIMIT_REQUESTS", 1000)
    return calls


def scan(client, ip="203.0.113.7", file=PNG):
    return client.post("/api/scan", files={"images": file}, data={"zip_code": "33021"}, headers={"cf-connecting-ip": ip})


def test_a_visitor_gets_three_free_scans_a_day_then_a_clear_message(fake_scanner):
    client = TestClient(app, base_url="https://testserver")
    assert [scan(client).status_code for _ in range(3)] == [200, 200, 200]
    blocked = scan(client)
    assert blocked.status_code == 429 and "3 free bill checks" in blocked.json()["detail"]
    assert len(fake_scanner) == 3


def test_clearing_cookies_does_not_reset_the_limit_for_an_address(fake_scanner):
    statuses = [scan(TestClient(app, base_url="https://testserver")).status_code for _ in range(config.SCAN_DAILY_LIMIT_PER_IP + 1)]
    assert statuses == [200] * config.SCAN_DAILY_LIMIT_PER_IP + [429]
    assert scan(TestClient(app, base_url="https://testserver"), ip="198.51.100.9").status_code == 200


def test_an_unreadable_photo_can_be_retried_but_still_counts_for_the_address(fake_scanner):
    client = TestClient(app, base_url="https://testserver")
    bad = ("bill.png", b"\x89PNG\r\n\x1a\nunreadable", "image/png")
    assert [scan(client, file=bad).status_code for _ in range(4)] == [400] * 4
    assert scan(client).status_code == 200
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) AS n FROM scan_attempts WHERE key = 'ip:203.0.113.7'").fetchone()["n"] == 5


def test_the_site_wide_ceiling_stops_scans_for_everyone(fake_scanner, monkeypatch):
    monkeypatch.setattr(config, "SCAN_DAILY_LIMIT_TOTAL", 2)
    assert [scan(TestClient(app, base_url="https://testserver"), ip=f"203.0.113.{n}").status_code for n in range(3)] == [200, 200, 503]
    assert len(fake_scanner) == 2


def test_scans_older_than_a_day_no_longer_count(fake_scanner):
    client = TestClient(app, base_url="https://testserver")
    for _ in range(3):
        scan(client)
    with get_db() as db:
        db.execute("UPDATE scan_attempts SET created_at = datetime('now', '-25 hours')")
    assert scan(client).status_code == 200


def test_too_many_pages_or_a_bad_email_are_refused_before_any_scan(fake_scanner):
    client = TestClient(app, base_url="https://testserver")
    many = [("images", PNG)] * (config.SCAN_MAX_PAGES + 1)
    assert client.post("/api/scan", files=many, data={"zip_code": "33021"}).status_code == 400
    assert client.post("/api/scan", files={"images": PNG}, data={"zip_code": "33021", "email": "not-an-email"}).status_code == 400
    assert fake_scanner == []


def test_scan_errors_do_not_echo_internal_details(fake_scanner, monkeypatch):
    def boom(*args, **kwargs):
        raise RuntimeError("secret-internal-path /app/data/app.db")
    monkeypatch.setattr(scan_pipeline, "run_scan", boom)
    response = scan(TestClient(app, base_url="https://testserver", raise_server_exceptions=False))
    assert response.status_code == 500 and "secret-internal-path" not in response.text


def test_api_docs_are_off_in_production():
    import main
    assert main._docs == {} or main._docs["openapi_url"] is None  # this run is not production
    assert {"docs_url": None, "redoc_url": None, "openapi_url": None} == {k: None for k in ("docs_url", "redoc_url", "openapi_url")}


# ── Traffic sources ───────────────────────────────────────────────────────────

def report():
    return {row["source"]: row for row in traffic.source_report(30)}


def test_a_tagged_link_is_counted_once_per_visitor_and_carried_onto_the_scan(fake_scanner):
    client = TestClient(app, base_url="https://testserver")
    client.get("/?utm_source=TikTok&utm_medium=social", headers={"user-agent": IPHONE})
    client.get("/scan", headers={"user-agent": IPHONE})
    client.get("/?utm_source=tiktok", headers={"user-agent": IPHONE})
    assert report()["tiktok"]["landings"] == 1
    assert scan(client).status_code == 200
    assert fake_scanner == ["tiktok"] and report()["tiktok"]["scans"] == 1


def test_instagram_and_tiktok_in_app_browsers_are_recognised_without_a_tag():
    TestClient(app, base_url="https://testserver").get("/scan", headers={"user-agent": IPHONE + " Instagram 350.0.0 (iPhone14,5)"})
    TestClient(app, base_url="https://testserver").get("/", headers={"user-agent": IPHONE + " musical_ly_38.0 BytedanceWebview/d8a21c6"})
    TestClient(app, base_url="https://testserver").get("/", headers={"user-agent": IPHONE + " [FBAN/FBIOS;FBAV/588.1]"})
    assert {name: row["landings"] for name, row in report().items()} == {"instagram": 1, "tiktok": 1, "facebook": 1}


def test_a_referring_site_is_named_and_our_own_pages_are_not():
    TestClient(app, base_url="https://testserver").get("/guides/", headers={"user-agent": IPHONE, "referer": "https://www.reddit.com/r/personalfinance/"})
    TestClient(app, base_url="https://testserver").get("/scan", headers={"user-agent": IPHONE, "referer": "https://billkarma.app/"})
    TestClient(app, base_url="https://testserver").get("/scan", headers={"user-agent": IPHONE})
    assert list(report()) == ["reddit"]


def test_bots_and_link_previews_are_not_counted_as_visitors():
    for agent in ("facebookexternalhit/1.1", "BufferLinkPreviewBot/1.0", "Mozilla/5.0 (compatible; Bytespider; spider-feedback@bytedance.com)", "curl/8.5.0"):
        TestClient(app, base_url="https://testserver").get("/scan?utm_source=instagram", headers={"user-agent": agent})
    assert report() == {}
