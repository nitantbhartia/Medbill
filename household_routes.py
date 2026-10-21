"""Pages for the household bill plan: account, subscription checkout, dashboard and uploads."""

import logging
from urllib.parse import quote

from fastapi import APIRouter, File, HTTPException, Request, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

import auth
import config
import household
import payment
from advocacy_api import AUTH_COOKIE_NAME, _set_auth_cookie
from private_uploads import save_private_upload, validate_upload

log = logging.getLogger(__name__)
router = APIRouter()
templates = Jinja2Templates(directory="templates")
templates.env.globals["config"] = config


def _base_url() -> str:
    return config.APP_URL.rstrip("/")


def _render_account(request: Request, mode: str, error: str = "", email: str = "", status_code: int = 200) -> HTMLResponse:
    return templates.TemplateResponse(
        "account.html",
        {"request": request, "mode": mode, "error": error, "email": email, "meta_robots": "noindex, follow"},
        status_code=status_code,
    )


def _login_response(user_id: int, next_url: str) -> RedirectResponse:
    response = RedirectResponse(next_url, status_code=303)
    _set_auth_cookie(response, auth.create_auth_session(user_id))
    return response


@router.get("/household", response_class=HTMLResponse)
async def household_page(request: Request):
    user = auth.get_current_user(request)
    if user and household.is_active(user["id"]):
        return RedirectResponse("/household/dashboard", status_code=303)
    return templates.TemplateResponse(
        "household.html",
        {
            "request": request,
            "user": user,
            "plans": household.PLANS,
            "canonical_url": f"{_base_url()}/household",
            "og_title": "BillKarma Household — We Check Every Medical Bill Against Your EOB",
            "og_description": "Forward your family's medical bills and insurance statements. We tell you what to pay, catch overbilling and recover overpayments.",
            "meta_robots": "index, follow",
        },
    )


@router.get("/account", response_class=HTMLResponse)
async def account_page(request: Request, mode: str = "register"):
    return _render_account(request, "login" if mode == "login" else "register")


@router.post("/account/register")
async def account_register(request: Request):
    form = await request.form()
    email = str(form.get("email") or "")
    try:
        user = auth.register_user(email, str(form.get("password") or ""), str(form.get("name") or ""))
    except HTTPException as exc:
        return _render_account(request, "register", exc.detail, email, status_code=exc.status_code)
    return _login_response(user["id"], "/household")


@router.post("/account/login")
async def account_login(request: Request):
    form = await request.form()
    email = str(form.get("email") or "")
    try:
        user = auth.login_user(email, str(form.get("password") or ""))
    except HTTPException as exc:
        return _render_account(request, "login", exc.detail, email, status_code=exc.status_code)
    return _login_response(user["id"], "/household")


@router.post("/account/logout")
async def account_logout(request: Request):
    token = request.cookies.get(AUTH_COOKIE_NAME)
    if token:
        auth.invalidate_session(token)
    response = RedirectResponse("/household", status_code=303)
    response.delete_cookie(AUTH_COOKIE_NAME, path="/")
    return response


@router.post("/household/checkout")
async def household_checkout(request: Request):
    user = auth.get_current_user(request)
    if not user:
        return RedirectResponse("/account", status_code=303)
    plan = str((await request.form()).get("plan") or "yearly")
    if plan not in household.PLANS:
        raise HTTPException(400, "Unknown plan")
    if not config.STRIPE_SECRET_KEY:
        log.error("Household checkout requested but STRIPE_SECRET_KEY is not configured")
        raise HTTPException(503, "Payments aren't available right now. Please try again later.")
    chosen = household.PLANS[plan]
    session = payment.create_subscription_checkout(
        product_name="BillKarma Household",
        amount_cents=chosen["cents"],
        interval=chosen["interval"],
        email=user["email"],
        metadata={"payment_purpose": "household", "user_id": user["id"], "plan": plan},
        success_url=f"{_base_url()}/household/welcome?session_id={{CHECKOUT_SESSION_ID}}",
        cancel_url=f"{_base_url()}/household",
    )
    household.record_checkout(user["id"], plan, session["id"])
    return RedirectResponse(session["url"], status_code=303)


@router.get("/household/welcome")
async def household_welcome(request: Request, session_id: str = ""):
    """Stripe returns here after checkout. The webhook also activates the member; both are safe to repeat."""
    user = auth.get_current_user(request)
    membership = household.get_membership(user["id"]) if user else None
    if membership and session_id and membership["stripe_session_id"] == session_id:
        try:
            household.activate_from_session(payment.get_session(session_id))
        except RuntimeError as exc:
            log.error("Could not confirm household checkout %s: %s", session_id, exc)
    return RedirectResponse("/household/dashboard", status_code=303)


@router.get("/household/dashboard", response_class=HTMLResponse)
async def household_dashboard(request: Request, error: str = ""):
    user = auth.get_current_user(request)
    if not user:
        return RedirectResponse("/account?mode=login", status_code=303)
    membership = household.get_membership(user["id"])
    if not membership or membership["status"] not in household.ACTIVE_STATUSES:
        return RedirectResponse("/household", status_code=303)
    return templates.TemplateResponse(
        "household_dashboard.html",
        {
            "request": request,
            "user": user,
            "membership": membership,
            "data": household.dashboard(user["id"]),
            "doc_types": household.DOC_TYPES,
            "error": error,
            "meta_robots": "noindex, nofollow",
        },
    )


def _require_member(request: Request) -> dict:
    user = auth.require_auth(request)
    if not household.is_active(user["id"]):
        raise HTTPException(403, "An active BillKarma Household plan is required")
    return user


@router.post("/household/documents")
async def household_upload(request: Request, document: UploadFile = File(...)):
    user = _require_member(request)
    form = {key: value for key, value in (await request.form()).items() if isinstance(value, str)}
    doc_type = form.get("doc_type")
    data = await document.read()
    error = validate_upload(document.content_type, data)
    if doc_type not in household.DOC_TYPES:
        error = "Choose whether this is a bill or an EOB."
    if error:
        return RedirectResponse(f"/household/dashboard?error={quote(error)}", status_code=303)
    path = save_private_upload(f"household/{user['id']}", document.content_type, data)
    form["original_filename"] = (document.filename or "")[:200]
    household.add_document(user["id"], doc_type, path, document.content_type, data, form)
    return RedirectResponse("/household/dashboard", status_code=303)


@router.post("/household/documents/{bill_id}/link")
async def household_link(request: Request, bill_id: int):
    user = _require_member(request)
    eob_id = str((await request.form()).get("eob_id") or "")
    household.link_eob(user["id"], bill_id, int(eob_id) if eob_id.isdigit() else None)
    return RedirectResponse("/household/dashboard", status_code=303)


@router.post("/household/requests")
async def household_request_help(request: Request):
    user = _require_member(request)
    form = await request.form()
    document_id = str(form.get("document_id") or "")
    household.request_help(user["id"], int(document_id) if document_id.isdigit() else None, str(form.get("note") or ""))
    return RedirectResponse("/household/dashboard", status_code=303)


@router.post("/household/billing")
async def household_billing_portal(request: Request):
    user = auth.require_auth(request)
    membership = household.get_membership(user["id"])
    if not membership or not membership["stripe_customer_id"]:
        return RedirectResponse("/household", status_code=303)
    portal = payment.create_billing_portal_session(membership["stripe_customer_id"], f"{_base_url()}/household/dashboard")
    return RedirectResponse(portal["url"], status_code=303)
