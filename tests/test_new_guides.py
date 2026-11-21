import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())
os.environ["DB_PATH"] = ":memory:"

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

import config  # noqa: E402
import guide_seo  # noqa: E402
from guides import GUIDES  # noqa: E402
from main import app  # noqa: E402

client = TestClient(app)

NEW_GUIDES = (
    "insurers-not-paying-er-bills-no-surprises-act",
    "medicaid-work-requirements-hospital-bills",
    "hospital-leaving-medicare-advantage-network",
    "uninsured-hospital-price-limits-refunds",
    "medicare-2027-costs-what-changes",
    "going-uninsured-2027-hospital-bills",
    "medicare-wiser-prior-authorization",
    "new-medical-debt-laws-2026",
    "ai-insurance-claim-denials-appeal",
    "site-neutral-facility-fees-2026",
    "billkarma-vs-goodbill-medical-bills",
    "upcoding-unbundling-hospital-bills",
    "hospital-revenue-codes-explained",
    "multiple-bills-one-hospital-visit",
    "hospital-did-not-bill-insurance",
    "pay-hospital-bill-while-disputing",
    "medical-credit-cards-hospital-bills",
    "er-level-5-charge-99285",
    "trauma-activation-fee",
    "medical-identity-theft-bills",
    "financial-assistance-after-paying-hospital-bill",
    "hospital-bill-higher-than-estimate",
    "medicare-summary-notice-vs-hospital-bill",
)


@pytest.mark.parametrize("slug", NEW_GUIDES)
def test_new_guide_renders_with_sources_faq_and_no_leftover_braces(slug):
    r = client.get(f"/guides/{slug}/")
    assert r.status_code == 200
    assert 'id="sources"' in r.text
    assert 'id="faq"' in r.text
    assert "{{" not in r.text and "{_embed" not in r.text


@pytest.mark.parametrize("slug", NEW_GUIDES)
def test_new_guide_title_and_description_fit_search_results(slug):
    guide = GUIDES[slug]
    assert len(guide_seo.seo_title(guide)) <= config.SEO_TITLE_MAX_CHARS
    assert len(guide_seo.seo_description(guide)) <= config.SEO_META_MAX_CHARS


def test_comparison_pages_link_to_each_other():
    resolve = client.get("/guides/billkarma-vs-resolve-medical-bills/").text
    assert "/guides/billkarma-vs-goodbill-medical-bills/" in resolve


def test_goodbill_page_states_verified_terms():
    html = client.get("/guides/billkarma-vs-goodbill-medical-bills/").text
    assert "20% of savings" in html
    assert "$1,000" in html
    assert "help.goodbill.com" in html
