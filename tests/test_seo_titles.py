import guides
import guide_seo
from hospital_seo import _build_meta_description, _build_page_title


def test_guide_titles_and_descriptions_fit_search_limits():
    for slug, guide in guides.GUIDES.items():
        if slug in guides.GUIDE_REDIRECTS:
            continue
        assert len(guide_seo.seo_description(guide)) <= guide_seo.META_MAX, slug


def test_overrides_point_at_live_guides_and_fit():
    for slug, (title, meta) in guide_seo.SEO_OVERRIDES.items():
        assert slug in guides.GUIDES and slug not in guides.GUIDE_REDIRECTS, slug
        assert len(title) <= guide_seo.TITLE_MAX and len(meta) <= guide_seo.META_MAX, slug


def test_hospital_title_leads_with_markup_when_it_fits():
    h = {"name": "Yale-New Haven Hospital", "avg_markup_vs_medicare": 4.27, "billing_grade": "D", "phone": "(203) 688-4242"}
    assert _build_page_title(h) == "Yale-New Haven Hospital Billing Phone: Prices 4.3x Medicare"
    meta = _build_meta_description(h, [])
    assert "(203) 688-4242" in meta and "4.3x Medicare (grade D)" in meta and len(meta) <= 155


def test_hospital_title_without_data_and_long_name_stays_under_60():
    h = {"name": "University of Pittsburgh Medical Center Presbyterian Shadyside Hospital"}
    assert len(_build_page_title(h)) <= 60
    assert len(_build_meta_description(h, [])) <= 155
