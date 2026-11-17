import re

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_landing_leads_with_the_hospital_bill_dispute():
    r = client.get("/")
    assert r.status_code == 200
    assert "we&rsquo;ll dispute it in writing." in r.text
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


def test_landing_shows_the_real_dispute_letter_and_followup_schedule():
    text = client.get("/").text
    assert "DUPLICATE BILLING — CPT 36415 (Blood Draw)" in text
    assert "CPT 80048 is not normally billed separately when CPT 80053 applies" in text
    assert "Final follow-up, or your money back" in text
    assert "$99 flat, refunded if not reduced" in text
    assert "Median reduction" not in text  # hidden until there are enough reported outcomes


def test_landing_hero_upload_posts_to_the_scan_api_and_falls_back_to_the_scan_page():
    text = client.get("/").text
    assert 'id="bill-file"' in text and "fetch('/api/scan'" in text
    assert '<a href="/scan" class="bk-btn" id="bill-pick">' in text


def test_results_page_explains_in_spanish_that_the_letter_is_english(monkeypatch):
    import config
    from analyzer import analyze_bill, save_bill_and_findings
    from tests.conftest import SAMPLE_BILL

    bill_id = save_bill_and_findings(None, SAMPLE_BILL, analyze_bill(SAMPLE_BILL, "33021"), "33021")
    monkeypatch.setattr(config, "ES_PAGES_ENABLED", True)
    html = client.get(f"/results/{bill_id}").text
    assert "la carta de disputa se envía en inglés" in html
    assert "En español:" in html
    monkeypatch.setattr(config, "ES_PAGES_ENABLED", False)
    assert "la carta de disputa se envía en inglés" not in client.get(f"/results/{bill_id}").text
