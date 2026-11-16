"""Spanish-language section: /es/ home, /es/escanear/ and six translated guides."""

import json

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates

import config
from es_content import HOME, SCAN
from es_guides_bills import GUIDES as BILL_GUIDES
from es_guides_debt import GUIDES as DEBT_GUIDES



def _require_enabled() -> None:
    if not config.ES_PAGES_ENABLED:
        raise HTTPException(404)


router = APIRouter(dependencies=[Depends(_require_enabled)])
templates = Jinja2Templates(directory="templates")
templates.env.globals["config"] = config

# Order shown on the /es/ home page.
GUIDES = [BILL_GUIDES[0], BILL_GUIDES[1], DEBT_GUIDES[0], DEBT_GUIDES[1], DEBT_GUIDES[2], BILL_GUIDES[2]]
GUIDES_BY_SLUG = {g["slug"]: g for g in GUIDES}

# English path -> Spanish path. The English paths match each English page's canonical URL.
ES_PATH_FOR_EN_PATH = {"/": "/es/", "/scan": "/es/escanear/"}
ES_PATH_FOR_EN_PATH.update({f"/guides/{g['en_slug']}/": f"/es/guias/{g['slug']}/" for g in GUIDES})
ES_PATHS = list(ES_PATH_FOR_EN_PATH.values())


def _absolute(path: str) -> str:
    return config.APP_URL.rstrip("/") + path


def hreflang_links_for_english(en_path: str) -> list[tuple[str, str]]:
    """Alternate links for an English page that has a Spanish counterpart; [] if it has none."""
    es_path = ES_PATH_FOR_EN_PATH.get(en_path)
    if not config.ES_PAGES_ENABLED or not es_path:
        return []
    return [("en", _absolute(en_path)), ("es", _absolute(es_path)), ("x-default", _absolute(en_path))]


def _spanish_context(request: Request, en_path: str, **extra) -> dict:
    es_path = ES_PATH_FOR_EN_PATH[en_path]
    return {
        "request": request,
        "lang": "es",
        "en_url": en_path,
        "canonical_url": _absolute(es_path),
        "hreflang_links": [("es", _absolute(es_path)), ("en", _absolute(en_path)), ("x-default", _absolute(en_path))],
        "meta_robots": "index, follow",
        **extra,
    }


def _json_ld(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False).replace("</", "<\\/")


def _structured_data(guide: dict, published: str, modified: str, url: str) -> tuple[str, str]:
    organization = {"@type": "Organization", "name": "BillKarma", "url": _absolute("/")}
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "inLanguage": "es",
        "headline": guide["title"],
        "description": guide["description"],
        "datePublished": published,
        "dateModified": modified,
        "mainEntityOfPage": url,
        "author": organization,
        "publisher": organization,
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": "es",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in guide["faqs"]
        ],
    }
    return _json_ld(article), _json_ld(faq)


@router.get("/es/", response_class=HTMLResponse)
async def es_home(request: Request):
    context = _spanish_context(
        request, "/", page=HOME, guides=GUIDES, og_title=HOME["title"], og_description=HOME["description"],
    )
    return templates.TemplateResponse("es_page.html", context)


@router.get("/es/escanear/", response_class=HTMLResponse)
async def es_scan(request: Request):
    context = _spanish_context(
        request, "/scan", page=SCAN, og_title=SCAN["title"], og_description=SCAN["description"],
    )
    return templates.TemplateResponse("es_page.html", context)


@router.get("/es/guias/{slug}/", response_class=HTMLResponse)
async def es_guide(request: Request, slug: str):
    guide = GUIDES_BY_SLUG.get(slug)
    if not guide:
        return templates.TemplateResponse(
            "error.html", {"request": request, "lang": "es", "message": "Guía no encontrada"}, status_code=404
        )
    from guides import get_guide
    english = get_guide(guide["en_slug"])
    published = english["published"]
    modified = english.get("reviewed_on") or published
    en_path = f"/guides/{guide['en_slug']}/"
    context = _spanish_context(request, en_path, guide=guide, published=published)
    context["article_json"], context["faq_json"] = _structured_data(guide, published, modified, context["canonical_url"])
    context["og_title"] = guide["title"]
    context["og_description"] = guide["description"]
    return templates.TemplateResponse("es_guide.html", context)


@router.get("/sitemap-es.xml")
async def es_sitemap():
    entries = "".join(
        f"<url><loc>{_absolute(path)}</loc><lastmod>{config.SITE_UPDATED}</lastmod><priority>0.7</priority></url>"
        for path in ES_PATHS
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{entries}</urlset>"
    )
    return Response(content=xml, media_type="application/xml")
