import logging

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, Response

import config
import db
from api import router as api_router
from analyzer import get_bill_results, get_stats
from hospital_seo import (
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


@app.get("/hospital", response_class=HTMLResponse)
async def hospital_index_page(request: Request):
    states = get_state_index_stats()
    return templates.TemplateResponse("hospital_index.html", {"request": request, "states": states})


@app.get("/hospital/{state_slug}", response_class=HTMLResponse)
async def hospital_state_page(request: Request, state_slug: str):
    hospitals = get_state_hospitals(state_slug)
    state_name = hospitals[0]["state"] if hospitals else state_slug.upper()
    return templates.TemplateResponse(
        "hospital_state_index.html",
        {"request": request, "hospitals": hospitals, "state_name": state_name},
    )


@app.get("/hospital/{state_slug}/{hospital_slug}", response_class=HTMLResponse)
async def hospital_profile_page(request: Request, state_slug: str, hospital_slug: str):
    profile = get_hospital_profile(state_slug, hospital_slug)
    if not profile:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Hospital not found"})
    return templates.TemplateResponse("hospital_profile.html", {"request": request, "data": profile})


@app.get("/hospitals/sitemap.xml")
async def hospital_sitemap():
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
