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
    for slug in config.FEATURED_GUIDE_SLUGS:
        assert f'href="/guides/{slug}/"' in html
    assert html.count('<details class="bk-fold">') >= 5
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
