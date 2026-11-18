import re

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_landing_leads_with_the_free_check_and_one_price():
    text = re.sub(r"\s+", " ", client.get("/").text)
    assert "Is your hospital bill wrong?" in text and "Find out free." in text
    assert 'href="/scan"' in text
    assert "Free" in text and "$19 once" in text
    assert "You pay nothing" in text


def test_landing_sells_only_the_report_and_names_no_other_product():
    text = re.sub(r"\s+", " ", client.get("/").text)
    assert "What&rsquo;s in your $19 report" in text
    assert "One price: $19 per bill" in text
    for stale in ("we dispute it for you", "Bills under $1,000", "Full refund", "Follow-ups", "household", "Household"):
        assert stale not in text


def test_landing_states_what_we_dont_do():
    r = client.get("/")
    assert "What we don&rsquo;t do" in r.text
    assert 'href="/household"' not in r.text.split("<footer")[0]


def test_search_console_tag_renders_only_when_configured(monkeypatch):
    import config
    assert "google-site-verification" not in client.get("/").text
    monkeypatch.setattr(config, "GOOGLE_SITE_VERIFICATION", "abc123")
    assert '<meta name="google-site-verification" content="abc123">' in client.get("/").text


def test_landing_shows_the_real_dispute_letter_the_report_contains():
    text = client.get("/").text
    assert "DUPLICATE BILLING — CPT 36415 (Blood Draw)" in text
    assert "CPT 80048 is not normally billed separately when CPT 80053 applies" in text
    assert "A dispute letter" in text and "A phone script" in text


def test_landing_hero_upload_posts_to_the_scan_api_and_falls_back_to_the_scan_page():
    text = client.get("/").text
    assert 'id="bill-file"' in text and "fetch('/api/scan'" in text
    assert '<a href="/scan" class="bk-btn" id="bill-pick">' in text


def test_results_page_explains_in_spanish_that_the_letter_is_english(monkeypatch):
    import config
    from analyzer import analyze_bill, save_bill_and_findings
    from tests.conftest import SAMPLE_BILL

    bill_id = save_bill_and_findings(None, SAMPLE_BILL, analyze_bill(SAMPLE_BILL, "33021"), "33021")
    monkeypatch.setattr(config, "SLIM_LAUNCH", True)
    monkeypatch.setattr(config, "ES_PAGES_ENABLED", True)
    html = client.get(f"/results/{bill_id}").text
    assert "la carta de disputa está escrita en inglés" in html
    assert "En español:" in html
    monkeypatch.setattr(config, "ES_PAGES_ENABLED", False)
    assert "la carta de disputa está escrita en inglés" not in client.get(f"/results/{bill_id}").text
