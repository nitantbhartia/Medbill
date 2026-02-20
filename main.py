import logging

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, Response, JSONResponse

import config
import db
from api import router as api_router
from analyzer import get_bill_results, get_stats
from compliance import log_audit
from hospital_seo import (
    find_hospitals,
    get_cities_for_state,
    get_grade_distribution,
    get_hospital_profile,
    get_hospital_sitemap_paths,
    get_sample_hospitals,
    get_state_hospitals,
    get_state_index_stats,
    resolve_hospital_slug,
    state_display_name,
)
from compare_pages import get_comparison_data, search_hospitals_for_compare
from procedure_pages import (
    get_hospitals_near_zip_for_cpt,
    get_procedure_profile,
    get_top_cpt_codes,
)

logging.basicConfig(
    level=logging.DEBUG if config.DEBUG else logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

app = FastAPI(title=config.APP_NAME)
app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
def startup():
    db.init_db()
    if config.AUTO_BOOTSTRAP_HOSPITAL_DATA:
        from hospital_bootstrap import ensure_hospital_data_bootstrap
        ensure_hospital_data_bootstrap()
    # Seed data if database is empty
    from seed_data import seed_if_empty
    seed_if_empty()


# --- Page routes ---


@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    stats = get_stats()
    canonical_url = f"{config.APP_URL.rstrip('/')}/"
    grade_dist = get_grade_distribution()
    sample_hospitals = get_sample_hospitals(6)

    from guides import list_guides, get_guide
    priority_slugs = [
        "hospital-billing-grades-explained",
        "common-hospital-billing-errors",
        "private-equity-hospital-billing",
    ]
    featured_guides = []
    for slug in priority_slugs:
        g = get_guide(slug)
        if g:
            word_count = len(g.get("body", "").split())
            g["reading_time"] = max(1, word_count // 200)
            featured_guides.append(g)
    if len(featured_guides) < 3:
        for g in list_guides():
            if g["slug"] not in priority_slugs:
                word_count = len(g.get("body", "").split())
                g["reading_time"] = max(1, word_count // 200)
                featured_guides.append(g)
                if len(featured_guides) >= 3:
                    break

    with db.get_db() as conn:
        hospital_count = conn.execute(
            "SELECT COUNT(*) AS n FROM billing_metrics WHERE billing_grade IS NOT NULL"
        ).fetchone()["n"]

    return templates.TemplateResponse(
        "landing.html",
        {
            "request": request,
            "stats": stats,
            "canonical_url": canonical_url,
            "grade_distribution": grade_dist,
            "sample_hospitals": sample_hospitals,
            "featured_guides": featured_guides,
            "hospital_count": hospital_count,
            "og_title": "BillKarma — Hospital Billing Grades, Bill Scanner & Price Transparency",
            "og_description": "Check any U.S. hospital's billing grade before you schedule. Scan your bill for errors. Fight overcharges with real Medicare data. 6,000+ hospitals graded free.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/scan", response_class=HTMLResponse)
async def scan_page(request: Request):
    return templates.TemplateResponse("scan.html", {"request": request})


@app.get("/confirm/{bill_id}", response_class=HTMLResponse)
async def confirm_page(request: Request, bill_id: int):
    results = get_bill_results(bill_id)
    if not results:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"})
    log_audit(action="view_confirm", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id)
    return templates.TemplateResponse("confirm.html", {"request": request, "data": results})


@app.get("/results/{bill_id}", response_class=HTMLResponse)
async def results_page(request: Request, bill_id: int):
    results = get_bill_results(bill_id)
    if not results:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"})
    log_audit(action="view_results_page", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id)

    from negotiation import generate_phone_script, generate_message_script
    phone_script = generate_phone_script(bill_id)
    message_script = generate_message_script(bill_id)

    return templates.TemplateResponse(
        "results.html",
        {"request": request, "data": results, "phone_script": phone_script, "message_script": message_script},
    )


@app.get("/calculator", response_class=HTMLResponse)
async def calculator_page(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/calculator"
    return templates.TemplateResponse(
        "calculator.html",
        {
            "request": request,
            "canonical_url": canonical_url,
        },
    )


@app.get("/calculator/embed", response_class=HTMLResponse)
async def calculator_embed(
    request: Request,
    mode: str = "cost",
    cpt: str = "",
    zip: str = "",
    title: str = "",
    subtitle: str = "",
    btn_text: str = "",
    cta_text: str = "",
    cta_url: str = "",
):
    """Embeddable calculator widget for iframes in articles."""
    return templates.TemplateResponse(
        "calculator_embed.html",
        {
            "request": request,
            "mode": mode,
            "prefill_cpt": cpt,
            "prefill_zip": zip,
            "title": title,
            "subtitle": subtitle,
            "btn_text": btn_text or ("Check Markup" if mode == "markup" else "Look Up"),
            "cta_text": cta_text,
            "cta_url": cta_url,
            "base_url": "",
        },
    )


@app.get("/guides/{slug}", response_class=HTMLResponse)
async def guide_page(request: Request, slug: str):
    """Serve a guide article by slug."""
    from guides import get_guide
    guide = get_guide(slug)
    if not guide:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Guide not found"})
    canonical_url = f"{config.APP_URL.rstrip('/')}/guides/{slug}"
    return templates.TemplateResponse(
        "guide.html",
        {
            "request": request,
            "guide": guide,
            "canonical_url": canonical_url,
            "og_title": guide["title"] + " | BillKarma",
            "og_description": guide["meta_description"],
            "meta_description": guide["meta_description"],
            "meta_robots": "index, follow",
        },
    )


@app.get("/guides/", response_class=HTMLResponse)
async def guides_index(request: Request):
    """List all published guides."""
    from guides import list_guides
    canonical_url = f"{config.APP_URL.rstrip('/')}/guides/"
    return templates.TemplateResponse(
        "guides_index.html",
        {
            "request": request,
            "guides": list_guides(),
            "canonical_url": canonical_url,
            "og_title": "Medical Billing Guides | BillKarma",
            "og_description": "Free guides on how to read, dispute, and reduce medical bills.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/hospital")
async def hospital_index_redirect():
    return RedirectResponse(url="/hospitals/", status_code=301)


@app.get("/hospitals/", response_class=HTMLResponse)
async def hospital_index_page(request: Request, q: str = ""):
    states = get_state_index_stats()
    results = find_hospitals(q) if q else []
    canonical_url = f"{config.APP_URL.rstrip('/')}/hospitals/"
    return templates.TemplateResponse(
        "hospitals_index.html",
        {
            "request": request,
            "states": states,
            "search_query": q,
            "search_results": results,
            "canonical_url": canonical_url,
            "og_title": "Hospital Billing Report Card Directory | BillKarma",
            "og_description": "Search US hospital billing report cards by state, city, and hospital name.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/hospital/{state_slug}")
async def hospital_state_redirect(state_slug: str):
    return RedirectResponse(url=f"/hospitals/{state_slug}/", status_code=301)


@app.get("/hospitals/{state_slug}/", response_class=HTMLResponse)
async def hospital_state_page(
    request: Request,
    state_slug: str,
    sort: str = "grade",
    ownership: str = "",
    page: int = 1,
):
    hospitals, total = get_state_hospitals(state_slug, sort=sort, ownership=ownership, page=page)
    state_name = hospitals[0]["state"] if hospitals else state_display_name(state_slug)
    cities = get_cities_for_state(state_slug)
    canonical_url = f"{config.APP_URL.rstrip('/')}/hospitals/{state_slug}/"
    return templates.TemplateResponse(
        "hospitals_state.html",
        {
            "request": request,
            "hospitals": hospitals,
            "state_name": state_name,
            "state_slug": state_slug,
            "cities": cities,
            "sort": sort,
            "ownership": ownership,
            "page": page,
            "per_page": 50,
            "total": total,
            "canonical_url": canonical_url,
            "og_title": f"{state_name} Hospital Billing Report Cards | BillKarma",
            "og_description": f"Compare billing grades and markup ratios for hospitals in {state_name}.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/hospitals/{state_slug}/{city_slug}/", response_class=HTMLResponse)
async def hospital_city_page(
    request: Request,
    state_slug: str,
    city_slug: str,
    sort: str = "grade",
    page: int = 1,
):
    from hospital_seo import get_city_hospitals

    hospitals, total = get_city_hospitals(state_slug, city_slug, sort=sort, page=page)
    city_name = hospitals[0]["city"] if hospitals else city_slug.replace("-", " ").title()
    state_name = hospitals[0]["state"] if hospitals else state_display_name(state_slug)
    canonical_url = f"{config.APP_URL.rstrip('/')}/hospitals/{state_slug}/{city_slug}/"
    return templates.TemplateResponse(
        "hospitals_city.html",
        {
            "request": request,
            "hospitals": hospitals,
            "city_name": city_name,
            "city_slug": city_slug,
            "state_name": state_name,
            "state_slug": state_slug,
            "sort": sort,
            "page": page,
            "per_page": 50,
            "total": total,
            "canonical_url": canonical_url,
            "og_title": f"{city_name}, {state_name} Hospital Billing Comparison | BillKarma",
            "og_description": f"Compare billing grades and markup ratios across hospitals in {city_name}, {state_name}.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/hospital/{state_slug}/{hospital_slug}")
async def hospital_profile_redirect_legacy(state_slug: str, hospital_slug: str):
    from db import get_db

    with get_db() as db_conn:
        row = db_conn.execute(
            "SELECT city_slug FROM hospitals WHERE state_slug = ? AND slug = ? LIMIT 1",
            (state_slug, hospital_slug),
        ).fetchone()
    if not row:
        return RedirectResponse(url=f"/hospitals/{state_slug}/", status_code=301)
    return RedirectResponse(url=f"/hospitals/{state_slug}/{row['city_slug']}/{hospital_slug}/", status_code=301)


@app.get("/hospitals/{state_slug}/{city_slug}/{hospital_slug}/", response_class=HTMLResponse)
async def hospital_profile_page(request: Request, state_slug: str, city_slug: str, hospital_slug: str):
    canonical_slug = resolve_hospital_slug(state_slug, city_slug, hospital_slug)
    if canonical_slug and canonical_slug != hospital_slug:
        return RedirectResponse(url=f"/hospitals/{state_slug}/{city_slug}/{canonical_slug}/", status_code=301)

    profile = get_hospital_profile(state_slug, city_slug, canonical_slug or hospital_slug)
    if not profile:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Hospital not found"})
    canonical_url = f"{config.APP_URL.rstrip('/')}/hospitals/{state_slug}/{city_slug}/{canonical_slug or hospital_slug}/"

    seo = profile["seo"]
    return templates.TemplateResponse(
        "hospitals_detail.html",
        {
            "request": request,
            "data": profile,
            "canonical_url": canonical_url,
            "og_title": seo["page_title"],
            "og_description": seo["meta_description"],
            "meta_description": seo["meta_description"],
            "meta_robots": "index, follow",
            "enable_affiliate_slots": config.ENABLE_AFFILIATE_SLOTS,
            "affiliate_url": config.AFFILIATE_URL,
            "enable_hospital_claim": config.ENABLE_HOSPITAL_CLAIM,
            "claim_hospital_url": config.CLAIM_HOSPITAL_URL,
        },
    )


@app.get("/procedures/", response_class=HTMLResponse)
async def procedure_index_page(request: Request):
    procedures = get_top_cpt_codes(100)
    # Group by body system
    groups: dict[str, list] = {}
    for p in procedures:
        groups.setdefault(p["body_system"], []).append(p)
    canonical_url = f"{config.APP_URL.rstrip('/')}/procedures/"
    return templates.TemplateResponse(
        "procedures_index.html",
        {
            "request": request,
            "groups": groups,
            "total": len(procedures),
            "canonical_url": canonical_url,
            "og_title": "Procedure Cost Directory: Medicare Rates & Hospital Grades | BillKarma",
            "og_description": "See Medicare rates, national average charges, and billing grades for 100 common procedures. Find the best-priced hospital near you.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/procedures/{cpt_code}/", response_class=HTMLResponse)
async def procedure_detail_page(request: Request, cpt_code: str):
    profile = get_procedure_profile(cpt_code)
    if not profile:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Procedure not found"})
    canonical_url = f"{config.APP_URL.rstrip('/')}/procedures/{cpt_code}/"
    seo = profile["seo"]
    return templates.TemplateResponse(
        "procedures_detail.html",
        {
            "request": request,
            "data": profile,
            "canonical_url": canonical_url,
            "og_title": seo["page_title"],
            "og_description": seo["meta_description"],
            "meta_description": seo["meta_description"],
            "meta_robots": "index, follow",
        },
    )


@app.get("/api/procedures/{cpt_code}/hospitals")
async def procedure_hospitals_by_zip(cpt_code: str, zip: str = ""):
    """Return hospitals near a zip code with data for this CPT code (AJAX)."""
    if not zip or len(zip) < 5:
        return JSONResponse({"error": "zip required"}, status_code=400)
    results = get_hospitals_near_zip_for_cpt(cpt_code, zip)
    if not results:
        return JSONResponse({"hospitals": [], "found": False})
    return JSONResponse({"hospitals": results, "found": True})


@app.get("/api/hospitals/search")
async def hospital_search_api(q: str = ""):
    """JSON hospital autocomplete for comparison tool."""
    results = search_hospitals_for_compare(q) if len(q.strip()) >= 2 else []
    return JSONResponse({"results": results})


@app.get("/compare/", response_class=HTMLResponse)
async def compare_index(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/compare/"
    return templates.TemplateResponse(
        "compare_index.html",
        {
            "request": request,
            "canonical_url": canonical_url,
            "og_title": "Hospital Comparison Tool | BillKarma",
            "og_description": "Compare any two hospitals side-by-side: billing grade, markup vs Medicare, CMS stars, and procedure prices.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/compare/{fid_a}/vs/{fid_b}/", response_class=HTMLResponse)
async def compare_detail(request: Request, fid_a: str, fid_b: str):
    data = get_comparison_data(fid_a, fid_b)
    if not data:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "message": "One or both hospitals not found."},
        )
    name_a = data["a"]["name"]
    name_b = data["b"]["name"]
    canonical_url = f"{config.APP_URL.rstrip('/')}/compare/{fid_a}/vs/{fid_b}/"
    return templates.TemplateResponse(
        "compare_detail.html",
        {
            "request": request,
            "data": data,
            "canonical_url": canonical_url,
            "og_title": f"{name_a} vs {name_b} | BillKarma",
            "og_description": (
                f"Compare billing grades and procedure prices: {name_a} vs {name_b}. "
                "See which hospital charges less relative to Medicare."
            ),
            "meta_robots": "index, follow",
        },
    )


@app.get("/sitemap.xml")
async def sitemap_main():
    return RedirectResponse(url="/sitemap-hospitals.xml", status_code=301)


@app.get("/hospitals/sitemap.xml")
async def hospital_sitemap():
    return RedirectResponse(url="/sitemap-hospitals.xml", status_code=301)


@app.get("/sitemap-hospitals.xml")
async def hospital_sitemap_v2():
    from guides import get_guide_slugs

    base = config.APP_URL.rstrip("/")
    guide_paths = [f"/guides/{slug}" for slug in get_guide_slugs()]
    paths = ["/", "/guides/", "/calculator", *guide_paths, *get_hospital_sitemap_paths()]
    urlset = "".join(
        f"<url><loc>{base}{path}</loc></url>"
        for path in paths
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{urlset}</urlset>"
    )
    return Response(content=xml, media_type="application/xml")


@app.get("/robots.txt")
async def robots_txt():
    body = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {config.APP_URL.rstrip('/')}/sitemap.xml\n"
    )
    return Response(content=body, media_type="text/plain")


@app.get("/ops/data-quality")
async def ops_data_quality():
    with db.get_db() as conn:
        hospitals_total = conn.execute("SELECT COUNT(*) AS n FROM hospitals").fetchone()["n"]
        metrics_with_avg = conn.execute(
            "SELECT COUNT(*) AS n FROM billing_metrics WHERE avg_markup_vs_medicare IS NOT NULL"
        ).fetchone()["n"]
        hcahps_rows = conn.execute("SELECT COUNT(*) AS n FROM hcahps_scores").fetchone()["n"]
        hcahps_recommend_yes = conn.execute(
            "SELECT COUNT(*) AS n FROM hcahps_scores WHERE recommend_yes IS NOT NULL"
        ).fetchone()["n"]
        transparency_parsed = conn.execute(
            "SELECT COUNT(*) AS n FROM transparency_files WHERE parse_status IN ('parsed', 'partial')"
        ).fetchone()["n"]
        prices_rows = conn.execute("SELECT COUNT(*) AS n FROM hospital_prices").fetchone()["n"]
        grade_rows = conn.execute(
            """
            SELECT billing_grade, COUNT(*) AS n
            FROM billing_metrics
            GROUP BY billing_grade
            """
        ).fetchall()
        markup_rows = conn.execute(
            """
            SELECT avg_markup_vs_medicare
            FROM billing_metrics
            WHERE avg_markup_vs_medicare IS NOT NULL
            ORDER BY avg_markup_vs_medicare
            """
        ).fetchall()
        refreshes = conn.execute(
            """
            SELECT source, MAX(refresh_date) AS last_refresh
            FROM data_refresh_log
            GROUP BY source
            ORDER BY source
            """
        ).fetchall()

    markups = [r["avg_markup_vs_medicare"] for r in markup_rows]
    def _quantile(p: float) -> float | None:
        if not markups:
            return None
        idx = int((len(markups) - 1) * p)
        return float(markups[idx])

    payload = {
        "hospitals_total": hospitals_total,
        "metrics_with_avg": metrics_with_avg,
        "metrics_coverage_pct": round((metrics_with_avg / hospitals_total * 100), 2) if hospitals_total else 0.0,
        "hcahps_rows": hcahps_rows,
        "hcahps_recommend_yes": hcahps_recommend_yes,
        "hcahps_recommend_coverage_pct": round((hcahps_recommend_yes / hospitals_total * 100), 2) if hospitals_total else 0.0,
        "transparency_parsed": transparency_parsed,
        "transparency_parsed_pct": round((transparency_parsed / hospitals_total * 100), 2) if hospitals_total else 0.0,
        "hospital_prices_rows": prices_rows,
        "grade_distribution": {r["billing_grade"]: r["n"] for r in grade_rows},
        "markup_quantiles": {
            "p50": _quantile(0.50),
            "p75": _quantile(0.75),
            "p90": _quantile(0.90),
            "p95": _quantile(0.95),
        },
        "last_refresh_by_source": {r["source"]: r["last_refresh"] for r in refreshes},
    }
    return JSONResponse(payload)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=config.DEBUG)
