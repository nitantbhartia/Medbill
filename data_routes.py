"""Public data pages: the /data/ overview, the grades CSV and per-hospital grade badges."""

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, Response, StreamingResponse
from fastapi.templating import Jinja2Templates

import config
from hospital_downloads import get_graded_hospital, get_graded_hospitals, iter_grades_csv, render_badge_svg

router = APIRouter()
templates = Jinja2Templates(directory="templates")
templates.env.globals["config"] = config


@router.get("/data/", response_class=HTMLResponse)
async def data_page(request: Request):
    title = "Hospital Billing Grades Data: Free Download"
    description = "Download BillKarma's A-F billing grade for every graded US hospital as a CSV. Free under CC BY 4.0."
    return templates.TemplateResponse(
        "data.html",
        {
            "request": request,
            "page_title": title,
            "meta_description": description,
            "og_title": title,
            "og_description": description,
            "canonical_url": f"{config.APP_URL.rstrip('/')}/data/",
            "meta_robots": "index, follow",
        },
    )


@router.get("/data/hospital-billing-grades.csv")
async def hospital_grades_csv():
    return StreamingResponse(
        iter_grades_csv(get_graded_hospitals()),
        media_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="hospital-billing-grades.csv"'},
    )


@router.get("/badge/{facility_id}.svg")
async def hospital_grade_badge(facility_id: str):
    hospital = get_graded_hospital(facility_id)
    if not hospital:
        raise HTTPException(status_code=404, detail="No billing grade for this hospital")
    return Response(
        content=render_badge_svg(hospital),
        media_type="image/svg+xml",
        headers={"Cache-Control": f"public, max-age={config.BADGE_CACHE_MAX_AGE_SECONDS}"},
    )
