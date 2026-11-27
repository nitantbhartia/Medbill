"""Concierge operations queue: paid appeals and household help requests, for the person working them."""

import logging
import os
import secrets
import threading

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

import appeals
import code_lookup
import config
import dispute_service
import hospital_locations
import household
import price_file_loader
import referrals
import traffic
from access_control import is_admin_request
from db import get_db

log = logging.getLogger(__name__)
router = APIRouter()
templates = Jinja2Templates(directory="templates")
templates.env.globals["config"] = config

ADMIN_COOKIE_NAME = "bk_admin"
PRICE_LOAD_TARGET_KEYS = ("facility_id", "name_phrase", "site", "location_name")


def _require_ops(request: Request) -> None:
    token = (config.ADMIN_API_TOKEN or "").strip()
    cookie = request.cookies.get(ADMIN_COOKIE_NAME, "")
    if is_admin_request(request) or (token and cookie and secrets.compare_digest(cookie, token)):
        return
    raise HTTPException(403, "Admin token required")


def _back() -> RedirectResponse:
    return RedirectResponse("/ops/concierge", status_code=303)


@router.get("/ops/login")
async def ops_login(request: Request, token: str = ""):
    """Exchange the admin token for a cookie so the queue works in a browser. Use once, then bookmark the queue."""
    from api import _check_rate_limit, _request_client_key
    if not _check_rate_limit(f"ops-login:{_request_client_key(request)}", config.OPS_LOGIN_ATTEMPTS_PER_HOUR):
        raise HTTPException(429, "Too many attempts. Try again in an hour.")
    expected = (config.ADMIN_API_TOKEN or "").strip()
    if not expected or not secrets.compare_digest(token, expected):
        raise HTTPException(403, "Invalid admin token")
    response = RedirectResponse("/ops/concierge", status_code=303)
    response.set_cookie(ADMIN_COOKIE_NAME, token, max_age=60 * 60 * 24 * 30, httponly=True, secure=not config.DEBUG, samesite="strict", path="/ops")
    return response


@router.get("/ops/concierge", response_class=HTMLResponse)
async def ops_queue(request: Request):
    _require_ops(request)
    cases = appeals.list_open_cases()
    for case in cases:
        case["dates"] = appeals.deadlines(case)
    return templates.TemplateResponse(
        "ops_concierge.html",
        {
            "request": request,
            "cases": cases,
            "status_labels": appeals.STATUS_LABELS,
            "outcomes": appeals.OUTCOMES,
            "help_requests": household.open_requests(),
            "disputes": dispute_service.cases_needing_attention(),
            "lob_ready": bool(config.LOB_API_KEY),
            "meta_robots": "noindex, nofollow",
        },
    )


@router.post("/ops/load-chargemaster")
async def ops_load_chargemaster(request: Request):
    """Rows of {facility_name, description, code} extracted from HCAI workbooks (scripts/load_hcai_chargemasters.py --post-to)."""
    _require_ops(request)
    rows = await request.json()
    if not isinstance(rows, list) or len(rows) > config.CHARGEMASTER_POST_MAX_ROWS:
        raise HTTPException(400, "Send a list of at most %d rows" % config.CHARGEMASTER_POST_MAX_ROWS)
    if not all(isinstance(row, dict) and all(isinstance(row.get(key), str) and row[key].strip() for key in ("facility_name", "description", "code")) for row in rows):
        raise HTTPException(400, "Every row needs facility_name, description and code as text")
    return {"status": "ok", "data": code_lookup.load_chargemaster(rows, config.HCAI_CHARGEMASTER_PAGE)}


@router.post("/ops/load-hospital-prices")
async def ops_load_hospital_prices(request: Request):
    """Start a one-off load of hospitals' published price files, each found through the cms-hpt.txt on its website:
    [{facility_id, name_phrase, site, location_name}]. It runs in the background; results go to the log and data_refresh_log."""
    _require_ops(request)
    targets = await request.json()
    if not isinstance(targets, list) or not 0 < len(targets) <= config.PRICE_LOAD_MAX_TARGETS:
        raise HTTPException(400, "Send a list of 1 to %d hospitals" % config.PRICE_LOAD_MAX_TARGETS)
    if not all(isinstance(t, dict) and all(isinstance(t.get(key), str) and t[key].strip() for key in PRICE_LOAD_TARGET_KEYS) for t in targets):
        raise HTTPException(400, "Every hospital needs %s as text" % ", ".join(PRICE_LOAD_TARGET_KEYS))
    if not all(t["site"].startswith("https://") for t in targets):
        raise HTTPException(400, "site must be the hospital website root, starting with https://")
    threading.Thread(target=price_file_loader.load_listed_hospitals, args=(targets,), daemon=True, name="price-load").start()
    return {"status": "ok", "data": {"started": len(targets)}}


@router.post("/ops/repair-hospital-locations")
async def ops_repair_hospital_locations(request: Request):
    """Start a one-off check of every hospital's city and state against its CMS record, fixing the ones that disagree."""
    _require_ops(request)
    threading.Thread(target=hospital_locations.run_location_repair, daemon=True, name="location-repair").start()
    return {"status": "ok", "data": {"started": True}}


@router.get("/ops/partners", response_class=HTMLResponse)
async def ops_partners(request: Request):
    _require_ops(request)
    return templates.TemplateResponse(
        "ops_partners.html",
        {
            "request": request,
            "counts": referrals.partner_scan_counts(),
            "sources": traffic.source_report(config.PARTNER_REPORT_DAYS),
            "days": config.PARTNER_REPORT_DAYS,
            "meta_robots": "noindex, nofollow",
        },
    )


@router.get("/ops/concierge/appeals/{case_id}/denial-letter")
async def ops_denial_letter(request: Request, case_id: int):
    _require_ops(request)
    case = appeals.get_case(case_id)
    if not case or not case["denial_letter_path"] or not os.path.exists(case["denial_letter_path"]):
        raise HTTPException(404, "No denial letter uploaded")
    return FileResponse(case["denial_letter_path"])


@router.get("/ops/concierge/documents/{document_id}")
async def ops_household_document(request: Request, document_id: int):
    _require_ops(request)
    with get_db() as db:
        row = db.execute("SELECT file_path FROM household_documents WHERE id = ?", (document_id,)).fetchone()
    if not row or not os.path.exists(row["file_path"]):
        raise HTTPException(404, "Document not found")
    return FileResponse(row["file_path"])


@router.post("/ops/concierge/appeals/{case_id}/mail")
async def ops_mail_appeal(request: Request, case_id: int):
    _require_ops(request)
    case = appeals.get_case(case_id)
    if not case or case["status"] != "approved":
        raise HTTPException(400, "Only approved appeals can be mailed")
    try:
        appeals.mail_by_lob(case)
    except (RuntimeError, ValueError) as exc:
        log.error("Mailing appeal #%s failed: %s", case_id, exc)
        raise HTTPException(502, f"Mailing failed: {exc}")
    return _back()


@router.post("/ops/concierge/appeals/{case_id}/sent")
async def ops_mark_sent(request: Request, case_id: int):
    _require_ops(request)
    case = appeals.get_case(case_id)
    form = await request.form()
    if not case or case["status"] != "approved":
        raise HTTPException(400, "Only approved appeals can be marked sent")
    appeals.record_sent(case, str(form.get("method") or "fax"), str(form.get("tracking_number") or ""))
    return _back()


@router.post("/ops/concierge/appeals/{case_id}/outcome")
async def ops_record_outcome(request: Request, case_id: int):
    _require_ops(request)
    case = appeals.get_case(case_id)
    form = await request.form()
    if not case or case["status"] != "sent":
        raise HTTPException(400, "Only sent appeals can get an outcome")
    recovered = str(form.get("amount_recovered") or "").replace(",", "")
    try:
        appeals.record_outcome(case, str(form.get("outcome") or ""), float(recovered) if recovered else None)
    except ValueError as exc:
        raise HTTPException(400, str(exc))
    return _back()


@router.post("/ops/concierge/appeals/{case_id}/notes")
async def ops_appeal_notes(request: Request, case_id: int):
    _require_ops(request)
    notes = str((await request.form()).get("ops_notes") or "")
    with get_db() as db:
        db.execute("UPDATE appeal_cases SET ops_notes = ? WHERE id = ?", (notes, case_id))
    return _back()


@router.post("/ops/concierge/requests/{request_id}/resolve")
async def ops_resolve_request(request: Request, request_id: int):
    _require_ops(request)
    household.resolve_request(request_id, str((await request.form()).get("resolution") or ""))
    return _back()
