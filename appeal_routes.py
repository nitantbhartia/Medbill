"""Pages for the denied-claim appeal service: intake, checkout, case status and approval."""

import logging

from fastapi import APIRouter, File, Request, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

import appeals
import config
import payment
from appeal_letter import DENIAL_REASONS, PLAN_TYPES, SERVICE_TIMINGS
from private_uploads import save_private_upload, validate_upload

log = logging.getLogger(__name__)
router = APIRouter()
templates = Jinja2Templates(directory="templates")
templates.env.globals["config"] = config


def _base_url() -> str:
    return config.APP_URL.rstrip("/")


def _render_intake(request: Request, form: dict, errors: list[str], status_code: int = 200) -> HTMLResponse:
    return templates.TemplateResponse(
        "appeal.html",
        {
            "request": request,
            "form": form,
            "errors": errors,
            "reasons": DENIAL_REASONS,
            "plan_types": PLAN_TYPES,
            "timings": SERVICE_TIMINGS,
            "price": config.APPEAL_PRICE_CENTS // 100,
            "price_large": config.APPEAL_PRICE_LARGE_CENTS // 100,
            "large_threshold": config.APPEAL_LARGE_CLAIM_THRESHOLD,
            "canonical_url": f"{_base_url()}/appeal",
            "og_title": "Appeal a Denied Insurance Claim | BillKarma",
            "og_description": "Send us your denial letter. We write the appeal, send it to your insurer and track the deadlines. Flat fee.",
            "meta_robots": "index, follow",
        },
        status_code=status_code,
    )


def _checkout_redirect(case: dict) -> RedirectResponse:
    session = payment.create_payment_checkout(
        product_name="BillKarma insurance appeal",
        amount_cents=case["price_cents"],
        email=case["email"],
        metadata={"payment_purpose": "appeal_case", "appeal_case_id": case["id"]},
        success_url=f"{_base_url()}/appeal/paid?session_id={{CHECKOUT_SESSION_ID}}",
        cancel_url=f"{_base_url()}/appeal/case/{case['token']}",
    )
    appeals.set_checkout_session(case["id"], session["id"])
    return RedirectResponse(session["url"], status_code=303)


@router.get("/appeal", response_class=HTMLResponse)
async def appeal_intake_page(request: Request):
    return _render_intake(request, {}, [])


@router.post("/appeal", response_class=HTMLResponse)
async def appeal_intake_submit(request: Request, denial_letter: UploadFile | None = File(None)):
    form = {key: value for key, value in (await request.form()).items() if isinstance(value, str)}
    errors = appeals.validate_intake(form)
    letter_bytes = await denial_letter.read() if denial_letter and denial_letter.filename else b""
    if letter_bytes:
        upload_error = validate_upload(denial_letter.content_type, letter_bytes)
        if upload_error:
            errors.append(f"Denial letter: {upload_error}")
    if errors:
        return _render_intake(request, form, errors, status_code=400)
    if not config.STRIPE_SECRET_KEY:
        log.error("Appeal intake received but STRIPE_SECRET_KEY is not configured")
        return _render_intake(request, form, ["Payments aren't available right now. Please try again later."], status_code=503)

    path = save_private_upload("appeals", denial_letter.content_type, letter_bytes) if letter_bytes else None
    case = appeals.create_case(form, path)
    return _checkout_redirect(case)


@router.get("/appeal/paid")
async def appeal_paid(session_id: str = ""):
    """Stripe sends the customer here after paying. The webhook also records payment; both are safe to repeat."""
    case = appeals.get_case_by_session(session_id) if session_id else None
    if not case:
        return RedirectResponse("/appeal", status_code=303)
    try:
        session = payment.get_session(session_id)
    except RuntimeError as exc:
        log.error("Could not confirm appeal checkout %s: %s", session_id, exc)
        return RedirectResponse(f"/appeal/case/{case['token']}", status_code=303)
    if session.get("payment_status") == "paid":
        appeals.mark_paid(case["id"])
    return RedirectResponse(f"/appeal/case/{case['token']}", status_code=303)


@router.get("/appeal/case/{token}", response_class=HTMLResponse)
async def appeal_case_page(request: Request, token: str):
    case = appeals.get_case_by_token(token)
    if not case:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Appeal not found"}, status_code=404)
    return templates.TemplateResponse(
        "appeal_case.html",
        {
            "request": request,
            "case": case,
            "status_label": appeals.STATUS_LABELS.get(case["status"], case["status"]),
            "reason_label": DENIAL_REASONS.get(case["denial_reason"], ""),
            "outcome_label": appeals.OUTCOMES.get(case["outcome"] or "", ""),
            "dates": appeals.deadlines(case),
            "meta_robots": "noindex, nofollow",
        },
    )


@router.post("/appeal/case/{token}/pay")
async def appeal_case_pay(token: str):
    case = appeals.get_case_by_token(token)
    if not case or case["status"] != "awaiting_payment":
        return RedirectResponse(f"/appeal/case/{token}", status_code=303)
    return _checkout_redirect(case)


@router.post("/appeal/case/{token}/approve")
async def appeal_case_approve(request: Request, token: str):
    case = appeals.get_case_by_token(token)
    letter_text = str((await request.form()).get("letter_text") or "")
    if case and case["status"] == "drafted" and letter_text.strip():
        appeals.approve(case, letter_text)
    return RedirectResponse(f"/appeal/case/{token}", status_code=303)
