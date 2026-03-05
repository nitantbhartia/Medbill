"""API endpoints for Advocacy Workspace.

All endpoints are scoped under /api/advocacy/ and require authentication.
"""

import json
import logging

from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Request
from fastapi.responses import JSONResponse, Response

import config
import advocacy
import auth
import org_management
from org_management import require_org_writer

log = logging.getLogger(__name__)

router = APIRouter(prefix="/api/advocacy")

ALLOWED_MIME_TYPES = {
    "image/jpeg", "image/png", "image/gif", "image/webp",
    "image/heic", "image/heif", "image/tiff", "image/bmp",
    "application/pdf",
}

AUTH_COOKIE_NAME = "bk_auth"
AUTH_COOKIE_MAX_AGE = 60 * 60 * 24 * 45  # 45 days


def _set_auth_cookie(response: Response, token: str) -> None:
    response.set_cookie(
        AUTH_COOKIE_NAME,
        token,
        max_age=AUTH_COOKIE_MAX_AGE,
        httponly=True,
        secure=not config.DEBUG,
        samesite="lax",
        path="/",
    )


# ── Auth endpoints ───────────────────────────────────────────────────────────

@router.post("/auth/register")
async def register(request: Request):
    payload = await request.json()
    user = auth.register_user(
        email=payload.get("email", ""),
        password=payload.get("password", ""),
        name=payload.get("name", ""),
    )
    token = auth.create_auth_session(user["id"])
    response = JSONResponse({"status": "ok", "data": {"user": user}})
    _set_auth_cookie(response, token)
    return response


@router.post("/auth/login")
async def login(request: Request):
    payload = await request.json()
    user = auth.login_user(
        email=payload.get("email", ""),
        password=payload.get("password", ""),
    )
    token = auth.create_auth_session(user["id"])
    response = JSONResponse({"status": "ok", "data": {"user": user}})
    _set_auth_cookie(response, token)
    return response


@router.post("/auth/logout")
async def logout(request: Request):
    token = request.cookies.get(AUTH_COOKIE_NAME)
    if token:
        auth.invalidate_session(token)
    response = JSONResponse({"status": "ok"})
    response.delete_cookie(AUTH_COOKIE_NAME, path="/")
    return response


@router.get("/auth/me")
async def get_me(request: Request):
    user = auth.get_current_user(request)
    if not user:
        return JSONResponse({"status": "ok", "data": {"user": None}})
    orgs = org_management.get_user_orgs(user["id"])
    return JSONResponse({"status": "ok", "data": {"user": user, "orgs": orgs}})


# ── Org endpoints ────────────────────────────────────────────────────────────

@router.post("/orgs")
async def create_org(request: Request):
    payload = await request.json()
    org = org_management.create_org(
        request,
        name=payload.get("name", ""),
        contact_email=payload.get("contact_email", ""),
        org_type=payload.get("org_type", "nonprofit"),
    )
    return JSONResponse({"status": "ok", "data": org})


@router.get("/orgs/{org_id}/members")
async def list_members(request: Request, org_id: int):
    org_management.require_org_member(request, org_id)
    members = org_management.get_org_members(org_id)
    return JSONResponse({"status": "ok", "data": members})


@router.post("/orgs/{org_id}/members")
async def invite_member(request: Request, org_id: int):
    payload = await request.json()
    result = org_management.invite_member(
        request, org_id,
        email=payload.get("email", ""),
        role=payload.get("role", "advocate"),
    )
    return JSONResponse({"status": "ok", "data": result})


@router.delete("/orgs/{org_id}/members/{member_id}")
async def remove_member(request: Request, org_id: int, member_id: int):
    org_management.remove_member(request, org_id, member_id)
    return JSONResponse({"status": "ok"})


# ── Case endpoints ───────────────────────────────────────────────────────────

@router.post("/orgs/{org_id}/cases")
async def create_case(request: Request, org_id: int):
    member = require_org_writer(request, org_id)
    payload = await request.json()
    case = advocacy.create_case(
        org_id=org_id,
        user_id=member["id"],
        patient_label=payload.get("patient_label", ""),
        hospital_name=payload.get("hospital_name"),
        insurance_carrier=payload.get("insurance_carrier"),
        date_of_service=payload.get("date_of_service"),
        bill_amount=payload.get("bill_amount"),
        notes=payload.get("notes"),
        tags=payload.get("tags"),
        patient_consent=payload.get("patient_consent"),
        assigned_to=payload.get("assigned_to"),
    )
    return JSONResponse({"status": "ok", "data": case})


@router.get("/orgs/{org_id}/cases")
async def list_cases(request: Request, org_id: int):
    org_management.require_org_member(request, org_id)
    params = request.query_params
    try:
        assigned_to = int(params["assigned_to"]) if params.get("assigned_to") else None
        limit = min(int(params.get("limit", 100)), 500)
        offset = int(params.get("offset", 0))
    except (ValueError, TypeError):
        raise HTTPException(400, "Invalid query parameter value")
    result = advocacy.list_cases(
        org_id=org_id,
        status=params.get("status"),
        assigned_to=assigned_to,
        search=params.get("search"),
        limit=limit,
        offset=offset,
    )
    return JSONResponse({"status": "ok", "data": result})


@router.get("/orgs/{org_id}/cases/{case_id}")
async def get_case(request: Request, org_id: int, case_id: int):
    org_management.require_org_member(request, org_id)
    case = advocacy.get_case(case_id, org_id)
    return JSONResponse({"status": "ok", "data": case})


@router.patch("/orgs/{org_id}/cases/{case_id}")
async def update_case(request: Request, org_id: int, case_id: int):
    member = require_org_writer(request, org_id)
    payload = await request.json()
    case = advocacy.update_case(case_id, org_id, **payload)
    return JSONResponse({"status": "ok", "data": case})


# ── Document endpoints ───────────────────────────────────────────────────────

@router.post("/orgs/{org_id}/cases/{case_id}/documents")
async def upload_document(
    request: Request,
    org_id: int,
    case_id: int,
    file: UploadFile = File(...),
    doc_type: str = Form("other"),
):
    member = require_org_writer(request, org_id)

    mime = file.content_type or ""
    if mime not in ALLOWED_MIME_TYPES:
        raise HTTPException(400, f"Unsupported file type '{mime}'. Upload images or PDFs only.")

    file_data = await file.read()
    max_bytes = config.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    if len(file_data) > max_bytes:
        raise HTTPException(400, f"File exceeds {config.MAX_UPLOAD_SIZE_MB} MB limit.")

    result = advocacy.upload_document(
        case_id=case_id,
        org_id=org_id,
        filename=file.filename or "upload",
        file_data=file_data,
        mime_type=mime,
        doc_type=doc_type,
    )
    return JSONResponse({"status": "ok", "data": result})


@router.get("/orgs/{org_id}/cases/{case_id}/documents")
async def list_documents(request: Request, org_id: int, case_id: int):
    org_management.require_org_member(request, org_id)
    docs = advocacy.get_case_documents(case_id, org_id)
    # Strip extracted_json from list view for brevity
    for doc in docs:
        if doc.get("extracted_json"):
            parsed = json.loads(doc["extracted_json"])
            doc["extraction_summary"] = {
                "line_items_count": len(parsed.get("line_items", [])),
                "provider_name": parsed.get("provider_name"),
                "total_charged": parsed.get("total_charged"),
            }
            del doc["extracted_json"]
    return JSONResponse({"status": "ok", "data": docs})


@router.get("/orgs/{org_id}/cases/{case_id}/documents/{doc_id}/file")
async def download_document(request: Request, org_id: int, case_id: int, doc_id: int):
    org_management.require_org_member(request, org_id)
    doc = advocacy.get_document_file(doc_id, case_id, org_id)
    safe_name = doc["filename"].replace('"', '_').replace('\n', '_').replace('\r', '_')
    return Response(
        content=doc["file_data"],
        media_type=doc["mime_type"],
        headers={"Content-Disposition": f'attachment; filename="{safe_name}"'},
    )


@router.delete("/orgs/{org_id}/cases/{case_id}/documents/{doc_id}")
async def delete_document(request: Request, org_id: int, case_id: int, doc_id: int):
    member = require_org_writer(request, org_id)
    advocacy.delete_document(doc_id, case_id, org_id)
    return JSONResponse({"status": "ok"})


# ── Override endpoints ───────────────────────────────────────────────────────

@router.post("/orgs/{org_id}/cases/{case_id}/overrides")
async def set_override(request: Request, org_id: int, case_id: int):
    member = require_org_writer(request, org_id)
    payload = await request.json()
    result = advocacy.set_override(
        case_id=case_id,
        org_id=org_id,
        user_id=member["id"],
        field_name=payload.get("field_name", ""),
        field_value=payload.get("field_value", ""),
    )
    return JSONResponse({"status": "ok", "data": result})


@router.get("/orgs/{org_id}/cases/{case_id}/overrides")
async def get_overrides(request: Request, org_id: int, case_id: int):
    org_management.require_org_member(request, org_id)
    overrides = advocacy.get_overrides(case_id)
    return JSONResponse({"status": "ok", "data": overrides})


# ── Analysis endpoints ───────────────────────────────────────────────────────

@router.post("/orgs/{org_id}/cases/{case_id}/analyze")
async def run_analysis(request: Request, org_id: int, case_id: int):
    org_management.require_org_member(request, org_id)
    result = advocacy.run_analysis(case_id, org_id)
    return JSONResponse({"status": "ok", "data": result})


@router.get("/orgs/{org_id}/cases/{case_id}/analysis")
async def get_analysis(request: Request, org_id: int, case_id: int):
    org_management.require_org_member(request, org_id)
    result = advocacy.get_case_analysis(case_id, org_id)
    if not result:
        return JSONResponse({"status": "ok", "data": None})
    return JSONResponse({"status": "ok", "data": result})


# ── Letter endpoints ─────────────────────────────────────────────────────────

@router.post("/orgs/{org_id}/cases/{case_id}/letters")
async def generate_letter(request: Request, org_id: int, case_id: int):
    member = require_org_writer(request, org_id)
    payload = await request.json()
    result = advocacy.generate_letter(
        case_id=case_id,
        org_id=org_id,
        user_id=member["id"],
        letter_type=payload.get("letter_type", ""),
        input_fields=payload.get("fields", {}),
    )
    return JSONResponse({"status": "ok", "data": result})


@router.get("/orgs/{org_id}/cases/{case_id}/letters")
async def list_letters(request: Request, org_id: int, case_id: int):
    org_management.require_org_member(request, org_id)
    letters = advocacy.get_case_letters(case_id, org_id)
    return JSONResponse({"status": "ok", "data": letters})


@router.patch("/orgs/{org_id}/cases/{case_id}/letters/{letter_id}")
async def update_letter(request: Request, org_id: int, case_id: int, letter_id: int):
    member = require_org_writer(request, org_id)
    payload = await request.json()
    result = advocacy.update_letter(
        letter_id=letter_id,
        case_id=case_id,
        org_id=org_id,
        content=payload.get("content", ""),
        expected_updated_at=payload.get("expected_updated_at"),
        user_id=member["id"],
    )
    return JSONResponse({"status": "ok", "data": result})


@router.post("/orgs/{org_id}/cases/{case_id}/letters/{letter_id}/review")
async def review_letter(request: Request, org_id: int, case_id: int, letter_id: int):
    member = require_org_writer(request, org_id)
    result = advocacy.mark_letter_reviewed(letter_id, case_id, org_id, member["id"])
    return JSONResponse({"status": "ok", "data": result})


@router.post("/orgs/{org_id}/cases/{case_id}/letters/{letter_id}/sent")
async def mark_sent(request: Request, org_id: int, case_id: int, letter_id: int):
    require_org_writer(request, org_id)
    payload = await request.json()
    result = advocacy.mark_letter_sent(
        letter_id, case_id, org_id,
        sent_date=payload.get("sent_date"),
    )
    return JSONResponse({"status": "ok", "data": result})


@router.get("/orgs/{org_id}/cases/{case_id}/letters/{letter_id}/pdf")
async def export_letter_pdf(request: Request, org_id: int, case_id: int, letter_id: int):
    org_management.require_org_member(request, org_id)
    letters = advocacy.get_case_letters(case_id, org_id)
    letter = next((l for l in letters if l["id"] == letter_id), None)
    if not letter:
        raise HTTPException(404, "Letter not found")

    pdf_bytes = _render_letter_pdf(letter["content"], letter["letter_type"])
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="letter_{letter_id}.pdf"'},
    )


def _render_letter_pdf(content: str, letter_type: str) -> bytes:
    """Render letter text as PDF using weasyprint."""
    try:
        from weasyprint import HTML
    except ImportError:
        raise HTTPException(500, "PDF export not available (weasyprint not installed)")

    # Escape HTML entities in content, preserve newlines
    from html import escape
    escaped = escape(content)
    html_content = escaped.replace("\n", "<br>")

    html_str = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
    @page {{ margin: 1in; size: letter; }}
    body {{ font-family: Georgia, 'Times New Roman', serif; font-size: 12pt; line-height: 1.5; color: #1a1a1a; }}
    .disclaimer {{ margin-top: 2em; padding-top: 1em; border-top: 1px solid #ccc; font-size: 9pt; color: #666; }}
</style></head>
<body>
    <div>{html_content}</div>
    <div class="disclaimer">
        <p>DISCLAIMER: This document was generated by BillKarma as a self-help tool.
        It does not constitute legal advice or medical advice. Please verify all details
        before sending. Consult an attorney for complex situations.</p>
    </div>
</body></html>"""

    return HTML(string=html_str).write_pdf()


# ── Note endpoints ───────────────────────────────────────────────────────────

@router.post("/orgs/{org_id}/cases/{case_id}/notes")
async def add_note(request: Request, org_id: int, case_id: int):
    member = require_org_writer(request, org_id)
    payload = await request.json()
    result = advocacy.add_note(case_id, org_id, member["id"], payload.get("content", ""))
    return JSONResponse({"status": "ok", "data": result})


@router.get("/orgs/{org_id}/cases/{case_id}/notes")
async def list_notes(request: Request, org_id: int, case_id: int):
    org_management.require_org_member(request, org_id)
    notes = advocacy.get_case_notes(case_id, org_id)
    return JSONResponse({"status": "ok", "data": notes})


# ── Activity Timeline endpoints ─────────────────────────────────────────────

@router.get("/orgs/{org_id}/cases/{case_id}/activity")
async def get_activity(request: Request, org_id: int, case_id: int):
    org_management.require_org_member(request, org_id)
    try:
        limit = min(int(request.query_params.get("limit", 100)), 500)
    except (ValueError, TypeError):
        limit = 100
    activity = advocacy.get_activity(case_id, org_id, limit=limit)
    return JSONResponse({"status": "ok", "data": activity})


# ── Share Link endpoints ────────────────────────────────────────────────────

@router.post("/orgs/{org_id}/cases/{case_id}/share")
async def create_share_link(request: Request, org_id: int, case_id: int):
    member = require_org_writer(request, org_id)
    payload = await request.json()
    result = advocacy.create_share_link(
        case_id=case_id,
        org_id=org_id,
        user_id=member["id"],
        label=payload.get("label"),
        expires_days=payload.get("expires_days"),
    )
    return JSONResponse({"status": "ok", "data": result})


@router.get("/orgs/{org_id}/cases/{case_id}/share")
async def list_share_links(request: Request, org_id: int, case_id: int):
    org_management.require_org_member(request, org_id)
    links = advocacy.list_share_links(case_id, org_id)
    return JSONResponse({"status": "ok", "data": links})


@router.delete("/orgs/{org_id}/cases/{case_id}/share/{link_id}")
async def revoke_share_link(request: Request, org_id: int, case_id: int, link_id: int):
    require_org_writer(request, org_id)
    advocacy.revoke_share_link(link_id, case_id, org_id)
    return JSONResponse({"status": "ok"})


@router.get("/shared/{token}")
async def get_shared_case(token: str):
    """Public endpoint — no auth required. Returns read-only case view."""
    case = advocacy.get_shared_case(token)
    return JSONResponse({"status": "ok", "data": case})


# ── Letter Version History endpoints ────────────────────────────────────────

@router.get("/orgs/{org_id}/cases/{case_id}/letters/{letter_id}/versions")
async def get_letter_versions(request: Request, org_id: int, case_id: int, letter_id: int):
    org_management.require_org_member(request, org_id)
    versions = advocacy.get_letter_versions(letter_id, case_id, org_id)
    return JSONResponse({"status": "ok", "data": versions})


@router.post("/orgs/{org_id}/cases/{case_id}/letters/{letter_id}/versions/{version_id}/restore")
async def restore_letter_version(request: Request, org_id: int, case_id: int, letter_id: int, version_id: int):
    member = require_org_writer(request, org_id)
    result = advocacy.restore_letter_version(version_id, letter_id, case_id, org_id, member["id"])
    return JSONResponse({"status": "ok", "data": result})


# ── Bulk Operations endpoints ───────────────────────────────────────────────

@router.post("/orgs/{org_id}/cases/bulk/status")
async def bulk_update_status(request: Request, org_id: int):
    member = require_org_writer(request, org_id)
    payload = await request.json()
    result = advocacy.bulk_update_status(
        org_id=org_id,
        case_ids=payload.get("case_ids", []),
        status=payload.get("status", ""),
        user_id=member["id"],
    )
    return JSONResponse({"status": "ok", "data": result})


@router.post("/orgs/{org_id}/cases/bulk/assign")
async def bulk_assign(request: Request, org_id: int):
    member = require_org_writer(request, org_id)
    payload = await request.json()
    result = advocacy.bulk_assign(
        org_id=org_id,
        case_ids=payload.get("case_ids", []),
        assigned_to=payload.get("assigned_to", 0),
        user_id=member["id"],
    )
    return JSONResponse({"status": "ok", "data": result})


@router.post("/orgs/{org_id}/cases/bulk/export")
async def bulk_export(request: Request, org_id: int):
    org_management.require_org_member(request, org_id)
    payload = await request.json()
    result = advocacy.bulk_export(
        org_id=org_id,
        case_ids=payload.get("case_ids"),
        status=payload.get("status"),
    )
    return JSONResponse({"status": "ok", "data": result})


@router.post("/orgs/{org_id}/cases/bulk/export-csv")
async def bulk_export_csv(request: Request, org_id: int):
    org_management.require_org_member(request, org_id)
    payload = await request.json()
    csv_data = advocacy.bulk_export_csv(
        org_id=org_id,
        case_ids=payload.get("case_ids"),
        status=payload.get("status"),
    )
    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="cases_export.csv"'},
    )


# ── Dashboard endpoint ─────────────────────────────────────────────────────

@router.get("/orgs/{org_id}/dashboard")
async def get_dashboard(request: Request, org_id: int):
    org_management.require_org_member(request, org_id)
    stats = advocacy.get_dashboard_stats(org_id)
    return JSONResponse({"status": "ok", "data": stats})


# ── Template endpoints ──────────────────────────────────────────────────────

@router.get("/orgs/{org_id}/templates")
async def list_templates(request: Request, org_id: int):
    org_management.require_org_member(request, org_id)
    templates = advocacy.get_templates(org_id)
    return JSONResponse({"status": "ok", "data": templates})


@router.post("/orgs/{org_id}/templates")
async def create_template(request: Request, org_id: int):
    member = require_org_writer(request, org_id)
    payload = await request.json()
    result = advocacy.create_template(
        org_id=org_id,
        user_id=member["id"],
        name=payload.get("name", ""),
        template_type=payload.get("template_type", ""),
        default_fields=payload.get("default_fields", {}),
    )
    return JSONResponse({"status": "ok", "data": result})


@router.delete("/orgs/{org_id}/templates/{template_id}")
async def delete_template(request: Request, org_id: int, template_id: int):
    require_org_writer(request, org_id)
    advocacy.delete_template(template_id, org_id)
    return JSONResponse({"status": "ok"})


# ── Email Sending endpoint ──────────────────────────────────────────────────

@router.post("/orgs/{org_id}/cases/{case_id}/letters/{letter_id}/email")
async def send_letter_email(request: Request, org_id: int, case_id: int, letter_id: int):
    member = require_org_writer(request, org_id)
    payload = await request.json()
    result = advocacy.send_letter_email(
        case_id=case_id,
        org_id=org_id,
        letter_id=letter_id,
        user_id=member["id"],
        recipient_email=payload.get("recipient_email", ""),
    )
    return JSONResponse({"status": "ok", "data": result})


# ── Communication Log endpoints ─────────────────────────────────────────────

@router.get("/orgs/{org_id}/cases/{case_id}/communications")
async def list_communications(request: Request, org_id: int, case_id: int):
    org_management.require_org_member(request, org_id)
    comms = advocacy.get_communications(case_id, org_id)
    return JSONResponse({"status": "ok", "data": comms})


@router.post("/orgs/{org_id}/cases/{case_id}/communications")
async def log_communication(request: Request, org_id: int, case_id: int):
    member = require_org_writer(request, org_id)
    payload = await request.json()
    result = advocacy.log_inbound_communication(
        case_id=case_id,
        org_id=org_id,
        user_id=member["id"],
        channel=payload.get("channel", "email"),
        subject=payload.get("subject", ""),
        notes=payload.get("notes", ""),
    )
    return JSONResponse({"status": "ok", "data": result})


# ── Dashboard Funnel endpoint ───────────────────────────────────────────────

@router.get("/orgs/{org_id}/dashboard/funnel")
async def get_dashboard_funnel(request: Request, org_id: int):
    org_management.require_org_member(request, org_id)
    result = advocacy.get_dashboard_funnel(org_id)
    return JSONResponse({"status": "ok", "data": result})
