import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())
os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import config  # noqa: E402
from main import app  # noqa: E402

client = TestClient(app)


def test_header_has_check_a_bill_button_and_mobile_menu():
    html = client.get("/").text
    assert 'class="bk-btn bk-btn-sm bk-header-cta"' in html
    assert '<details class="bk-menu">' in html


def test_guides_index_lists_featured_and_every_category_without_cards():
    html = client.get("/guides/").text
    assert "Start here" in html
    for slug, _label in config.FEATURED_GUIDE_SLUGS:
        assert f'href="/guides/{slug}/"' in html
    assert html.count('class="bk-topic"') >= 5
    assert len(html) < 400_000


def test_guide_page_makes_no_medical_review_claim():
    html = client.get("/guides/medical-bill-negotiation-service-cost/").text
    assert "Medically reviewed" not in html
    assert "Fact-checked" not in html
    assert "not legal or medical advice" in html


def test_no_green_brand_color_left_in_templates():
    for name in ("scan.html", "guide.html", "guides_index.html", "about.html"):
        with open(os.path.join("templates", name)) as f:
            assert "#00824F" not in f.read().upper()


def test_homepage_shows_example_bill_with_flagged_errors_upfront():
    html = client.get("/").text
    hero = html.split('id="how"')[0]
    assert 'class="bk-statement"' in hero
    assert "Billed twice for one draw." in hero
    assert "Flagged, 3 charges" in hero and "$4,680.00" in hero
    assert "to unlock" in hero


def test_guides_index_has_filter_and_labeled_start_path():
    html = client.get("/guides/").text
    assert 'id="guide-filter"' in html
    assert 'data-label="Step 1"' in html


def test_css_is_cache_busted():
    html = client.get("/").text
    assert f"/static/css/site.css?v={config.ASSET_VERSION}" in html


def test_no_unsourced_error_rate_claim_on_scan_or_guides():
    for path in ("/scan", "/guides/upcoding-unbundling-hospital-bills/"):
        assert "1 in 4" not in client.get(path).text


def test_privacy_and_terms_pages_exist_and_are_linked_from_the_footer():
    privacy = client.get("/privacy/")
    assert privacy.status_code == 200
    assert "We do not save the file itself" in privacy.text
    assert "support@billkarma.app" in privacy.text

    terms = client.get("/terms/")
    assert terms.status_code == 200
    assert "REFUND POLICY" in terms.text

    footer = client.get("/").text.split("<footer")[1]
    assert 'href="/privacy/"' in footer and 'href="/terms/"' in footer
