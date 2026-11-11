import re

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_landing_leads_with_the_hospital_bill_dispute():
    r = client.get("/")
    assert r.status_code == 200
    assert "We&rsquo;ll dispute it in writing." in r.text
    assert 'href="/scan"' in r.text


def test_landing_shows_flat_fee_tiers_from_config():
    text = re.sub(r"\s+", " ", client.get("/").text)
    assert "Bills under $1,000" in text and "$29" in text
    assert "Bills over $20,000" in text and "$149" in text
    assert "7, 14, 30, 45" in text


def test_landing_states_what_we_dont_do():
    r = client.get("/")
    assert "What we don&rsquo;t do" in r.text
    assert 'href="/household"' not in r.text.split("<footer")[0]


def test_search_console_tag_renders_only_when_configured(monkeypatch):
    import config
    assert "google-site-verification" not in client.get("/").text
    monkeypatch.setattr(config, "GOOGLE_SITE_VERIFICATION", "abc123")
    assert '<meta name="google-site-verification" content="abc123">' in client.get("/").text
