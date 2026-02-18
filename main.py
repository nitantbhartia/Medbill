import logging

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, Response

import config
import db
from api import router as api_router
from analyzer import get_bill_results, get_stats
from hospital_seo import (
    get_cities_for_state,
    get_hospital_profile,
    get_hospital_sitemap_paths,
    get_state_hospitals,
    get_state_index_stats,
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
    # Seed data if database is empty
    from seed_data import seed_if_empty
    seed_if_empty()


# --- Page routes ---


@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    stats = get_stats()
    return templates.TemplateResponse("landing.html", {"request": request, "stats": stats})


@app.get("/scan", response_class=HTMLResponse)
async def scan_page(request: Request):
    return templates.TemplateResponse("scan.html", {"request": request})


@app.get("/confirm/{bill_id}", response_class=HTMLResponse)
async def confirm_page(request: Request, bill_id: int):
    results = get_bill_results(bill_id)
    if not results:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"})
    return templates.TemplateResponse("confirm.html", {"request": request, "data": results})


@app.get("/results/{bill_id}", response_class=HTMLResponse)
async def results_page(request: Request, bill_id: int):
    results = get_bill_results(bill_id)
    if not results:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"})

    from negotiation import generate_phone_script, generate_message_script
    phone_script = generate_phone_script(bill_id)
    message_script = generate_message_script(bill_id)

    return templates.TemplateResponse(
        "results.html",
        {"request": request, "data": results, "phone_script": phone_script, "message_script": message_script},
    )


@app.get("/hospital")
async def hospital_index_redirect():
    return RedirectResponse(url="/hospitals/", status_code=301)


@app.get("/hospitals/", response_class=HTMLResponse)
async def hospital_index_page(request: Request):
    states = get_state_index_stats()
    canonical_url = f"{config.APP_URL.rstrip('/')}/hospitals/"
    return templates.TemplateResponse(
        "hospitals_index.html",
        {"request": request, "states": states, "canonical_url": canonical_url},
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
    state_name = hospitals[0]["state"] if hospitals else state_slug.upper()
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
    state_name = hospitals[0]["state"] if hospitals else state_slug.upper()
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
    profile = get_hospital_profile(state_slug, city_slug, hospital_slug)
    if not profile:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Hospital not found"})
    canonical_url = f"{config.APP_URL.rstrip('/')}/hospitals/{state_slug}/{city_slug}/{hospital_slug}/"
    return templates.TemplateResponse(
        "hospitals_detail.html",
        {
            "request": request,
            "data": profile,
            "canonical_url": canonical_url,
            "enable_affiliate_slots": config.ENABLE_AFFILIATE_SLOTS,
            "affiliate_url": config.AFFILIATE_URL,
            "enable_hospital_claim": config.ENABLE_HOSPITAL_CLAIM,
            "claim_hospital_url": config.CLAIM_HOSPITAL_URL,
        },
    )


@app.get("/hospitals/sitemap.xml")
async def hospital_sitemap():
    return RedirectResponse(url="/sitemap-hospitals.xml", status_code=301)


@app.get("/sitemap-hospitals.xml")
async def hospital_sitemap_v2():
    base = config.APP_URL.rstrip("/")
    urlset = "".join(
        f"<url><loc>{base}{path}</loc></url>"
        for path in get_hospital_sitemap_paths()
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{urlset}</urlset>"
    )
    return Response(content=xml, media_type="application/xml")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=config.DEBUG)
