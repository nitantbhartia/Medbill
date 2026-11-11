import re

from fastapi.testclient import TestClient

import guides
from main import app

client = TestClient(app)


def test_every_redirect_ends_on_a_live_guide():
    for slug in guides.GUIDE_REDIRECTS:
        final = guides.resolve_redirect(slug)
        assert final in guides.GUIDES and final not in guides.GUIDE_REDIRECTS, slug


def test_redirected_guide_is_one_hop_to_final_url():
    r = client.get("/guides/preventive-care-billing-errors/", follow_redirects=False)
    assert r.status_code == 301
    assert r.headers["location"] == "/guides/what-preventive-care-is-free/"


def test_no_slash_redirected_guide_is_one_hop():
    r = client.get("/guides/colonoscopy-billing", follow_redirects=False)
    assert r.status_code == 301
    assert r.headers["location"] == "/guides/colonoscopy-cost/"


def test_guide_bodies_never_link_to_a_redirect():
    for slug, guide in guides.GUIDES.items():
        targets = re.findall(r'href="(?:https://billkarma\.app)?/guides/([a-z0-9-]+)/', guide["body"])
        assert not set(targets) & set(guides.GUIDE_REDIRECTS), slug


def test_duplicate_slug_registration_is_rejected():
    slug = next(iter(guides.GUIDES))
    try:
        guides.register(slug, {"title": "Dup", "body": ""})
    except ValueError:
        return
    raise AssertionError("duplicate registration should raise")
