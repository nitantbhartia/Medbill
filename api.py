import collections
import json
import logging
import re
import sqlite3
import time
from datetime import datetime

from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Request
from fastapi.responses import JSONResponse

import config
import email_service
import scanner
import analyzer
import negotiation
import payment as payment_module
import dispute_service
import esign as esign_module
from dispute_workflow import build_dispute_letter, build_phone_script, get_outcome_stats
from db import get_db
from dispute_packet import generate_dispute_packet
from appeal_playbooks import generate_appeal_playbook
from provider_intelligence import get_provider_intelligence
from tools_catalog import get_tool
from tools_engine import run_tool, hash_payload
from compliance import (
    scrub_extracted_data,
    record_consent,
    log_audit,
    export_bill_data,
    delete_bill_data,
    purge_old_data,
)
from ocr_benchmark import run_manifest
from access_control import (
    get_or_create_session_id,
    grant_bill_access,
    is_admin_request,
    require_bill_access,
    require_case_access,
    set_session_cookie,
)

log = logging.getLogger(__name__)
router = APIRouter(prefix="/api")

_rate_buckets: dict[str, list[float]] = collections.defaultdict(list)
_tools_rate_buckets: dict[str, list[float]] = collections.defaultdict(list)


def _check_rate_limit(ip: str) -> bool:
    """Return True if the request is allowed. Prunes expired timestamps in-place."""
    now = time.monotonic()
    window = config.RATE_LIMIT_WINDOW_SECONDS
    bucket = _rate_buckets[ip]
    _rate_buckets[ip] = [t for t in bucket if now - t < window]
    if len(_rate_buckets[ip]) >= config.RATE_LIMIT_REQUESTS:
        return False
    _rate_buckets[ip].append(now)
    return True


def _check_tools_rate_limit(ip: str) -> bool:
    """Rate limit for tool APIs to reduce abuse and noisy scans."""
    now = time.monotonic()
    window = config.TOOLS_RATE_LIMIT_WINDOW_SECONDS
    bucket = _tools_rate_buckets[ip]
    _tools_rate_buckets[ip] = [t for t in bucket if now - t < window]
    if len(_tools_rate_buckets[ip]) >= config.TOOLS_RATE_LIMIT_REQUESTS:
        return False
    _tools_rate_buckets[ip].append(now)
    return True


ALLOWED_MIME_TYPES = {
    "image/jpeg", "image/png", "image/gif", "image/webp",
    "image/heic", "image/heif", "image/tiff", "image/bmp",
    "application/pdf",
}

CLAIM_TRANSITIONS = {
    "drafted": {"sent", "denied"},
    "sent": {"acknowledged", "denied"},
    "acknowledged": {"resolved", "denied"},
    "resolved": set(),
    "denied": set(),
}


def _validate_email(email: str) -> bool:
    token = (email or "").strip()
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", token))


async def _parse_json_object(request: Request) -> dict:
    try:
        payload = await request.json()
    except json.JSONDecodeError:
        raise HTTPException(400, "Invalid JSON payload")
    if not isinstance(payload, dict):
        raise HTTPException(400, "Payload must be a JSON object")
    return payload


def _assert_payload_size(payload: dict, limit_bytes: int, message: str) -> None:
    size = len(json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))
    if size > limit_bytes:
        raise HTTPException(413, message)


def _require_admin_access(request: Request) -> None:
    """Require explicit admin token in production; fallback localhost-only in debug."""
    if not is_admin_request(request):
        raise HTTPException(403, "Admin token required")


@router.post("/scan")
async def scan_bill(
    request: Request,
    images: list[UploadFile] = File(...),
    eob_images: list[UploadFile] | None = File(None),
    portal_images: list[UploadFile] | None = File(None),
    zip_code: str = Form("00000"),
    email: str = Form(""),
):
    """Scan one or more bill images, extract line items, and analyze."""
    if not images:
        raise HTTPException(400, "No files uploaded")

    # Rate limit by client IP
    client_ip = request.client.host if request.client else "unknown"
    if not _check_rate_limit(client_ip):
        raise HTTPException(
            429,
            f"Too many scans. Max {config.RATE_LIMIT_REQUESTS} per hour per IP.",
        )

    # Validate ZIP code format
    zip_code = zip_code.strip()
    if not re.fullmatch(r"\d{5}", zip_code):
        raise HTTPException(400, "zip_code must be a 5-digit US ZIP code")

    # Validate each uploaded file
    max_bytes = config.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    all_uploads = list(images) + (list(eob_images) if eob_images else []) + (list(portal_images) if portal_images else [])
    for upload in all_uploads:
        if not upload or not upload.filename:
            continue
        mime = upload.content_type or ""
        if mime not in ALLOWED_MIME_TYPES:
            raise HTTPException(400, f"Unsupported file type '{mime}'. Upload images or PDFs only.")
        # Peek at size without consuming the stream
        data = await upload.read()
        if len(data) > max_bytes:
            raise HTTPException(400, f"File '{upload.filename}' exceeds {config.MAX_UPLOAD_SIZE_MB} MB limit.")
        # Rewind for later reading
        await upload.seek(0)

    # Get or create user
    user_id = None
    if email:
        with get_db() as db:
            row = db.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()
            if row:
                user_id = row["id"]
            else:
                cursor = db.execute(
                    "INSERT INTO users (email, zip_code) VALUES (?, ?)",
                    (email, zip_code),
                )
                user_id = cursor.lastrowid

    # Extract bill data
    try:
        if len(images) == 1:
            image_bytes = await images[0].read()
            mime_type = images[0].content_type or "image/jpeg"
            extracted = scanner.process_bill_with_verification(image_bytes, mime_type)
        else:
            image_list = []
            for f in images:
                img = await f.read()
                image_list.append((img, f.content_type or "image/jpeg"))
            extracted = scanner.process_multi_page_bill(image_list)
    except Exception as e:
        log.error("Scan extraction failed: %s", e, exc_info=True)
        raise HTTPException(500, f"Failed to extract bill data: {e}")

    session_id, created_session = get_or_create_session_id(request)

    # Analyze and persist
    try:
        extracted = scrub_extracted_data(extracted)
        if eob_images:
            eob_uploads = [f for f in eob_images if f and f.filename]
            if eob_uploads:
                if len(eob_uploads) == 1:
                    eob_bytes = await eob_uploads[0].read()
                    eob_data = scanner.process_bill_with_verification(
                        eob_bytes, eob_uploads[0].content_type or "image/jpeg"
                    )
                else:
                    eob_image_list = []
                    for f in eob_uploads:
                        eob_image_list.append((await f.read(), f.content_type or "image/jpeg"))
                    eob_data = scanner.process_multi_page_bill(eob_image_list)
                extracted = analyzer.merge_eob_into_extracted(extracted, scrub_extracted_data(eob_data))
        analysis = analyzer.analyze_bill(extracted, zip_code)
        bill_id = analyzer.save_bill_and_findings(user_id, extracted, analysis, zip_code)
        try:
            grant_bill_access(session_id, bill_id)
        except Exception as access_exc:
            log.warning("Unable to persist bill access mapping for bill_id=%s: %s", bill_id, access_exc)

        # Track all evidence uploads
        with get_db() as db:
            try:
                for i, f in enumerate(images):
                    if f and f.filename:
                        db.execute(
                            "INSERT INTO evidence_uploads (bill_id, evidence_type, file_index, original_filename) VALUES (?, 'bill_page', ?, ?)",
                            (bill_id, i, f.filename),
                        )
                for i, f in enumerate(eob_images or []):
                    if f and f.filename:
                        db.execute(
                            "INSERT INTO evidence_uploads (bill_id, evidence_type, file_index, original_filename) VALUES (?, 'eob_page', ?, ?)",
                            (bill_id, i, f.filename),
                        )
                for i, f in enumerate(portal_images or []):
                    if f and f.filename:
                        db.execute(
                            "INSERT INTO evidence_uploads (bill_id, evidence_type, file_index, original_filename) VALUES (?, 'portal_screenshot', ?, ?)",
                            (bill_id, i, f.filename),
                        )
            except sqlite3.IntegrityError:
                # Can occur in mocked/integration tests when bill persistence is stubbed.
                log.warning("Skipping evidence_uploads persistence for bill_id=%s due to FK mismatch", bill_id)

        log_audit(
            action="scan_and_analyze",
            resource_type="bill",
            resource_id=str(bill_id),
            user_id=user_id,
            bill_id=bill_id,
            metadata={"zip_code": zip_code, "findings": analysis.get("total_findings", 0)},
        )
    except Exception as e:
        log.error("Analysis/save failed: %s", e, exc_info=True)
        raise HTTPException(500, f"Failed to analyze bill: {e}")

    extraction_meta = extracted.get("_extraction_meta", {})
    has_eob = bool(eob_images and any(f and f.filename for f in eob_images))
    has_portal = bool(portal_images and any(f and f.filename for f in portal_images))
    payload = {
        "status": "ok",
        "data": {
            "bill_id": bill_id,
            "extracted": extracted,
            "analysis": analysis,
            "extraction_quality": {
                "score": extraction_meta.get("quality_score"),
                "variant": extraction_meta.get("selected_variant"),
            },
            "evidence_types": ["bill"] + (["eob"] if has_eob else []) + (["portal"] if has_portal else []),
        },
    }
    response = JSONResponse(payload)
    if created_session:
        set_session_cookie(response, session_id)
    return response


@router.post("/analyze/{bill_id}")
async def analyze_confirmed(request: Request, bill_id: int, payload: dict):
    """Re-analyze a bill after user confirms/edits line items."""
    require_bill_access(request, bill_id)
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            raise HTTPException(404, "Bill not found")

        zip_code = bill["zip_code"] or "00000"

        # Preserve insurance data from original line items before replacing
        original_items = db.execute(
            "SELECT cpt_code, date_of_service, insurance_paid, "
            "insurance_adjustment, patient_responsibility "
            "FROM line_items WHERE bill_id = ?",
            (bill_id,),
        ).fetchall()
        insurance_by_cpt = {}
        for orig in original_items:
            if orig["cpt_code"]:
                insurance_by_cpt[orig["cpt_code"]] = {
                    "insurance_paid": orig["insurance_paid"],
                    "insurance_adjustment": orig["insurance_adjustment"],
                    "patient_responsibility": orig["patient_responsibility"],
                    "date_of_service": orig["date_of_service"],
                }

        # Update line items with user-confirmed data
        db.execute("DELETE FROM line_items WHERE bill_id = ?", (bill_id,))
        db.execute("DELETE FROM findings WHERE bill_id = ?", (bill_id,))

        items = payload.get("line_items", [])
        for item in items:
            ins = insurance_by_cpt.get(item.get("cpt_code"), {})
            patient_responsibility = item.get("patient_responsibility")
            if patient_responsibility is None:
                patient_responsibility = ins.get("patient_responsibility")
            charged_amount = item.get("billed_amount")
            if charged_amount is None:
                charged_amount = patient_responsibility
            db.execute(
                "INSERT INTO line_items (bill_id, cpt_code, description, "
                "charged_amount, quantity, date_of_service, insurance_paid, "
                "insurance_adjustment, patient_responsibility, extraction_confidence) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'high')",
                (
                    bill_id,
                    item.get("cpt_code"),
                    item.get("description"),
                    charged_amount,
                    item.get("quantity", 1),
                    ins.get("date_of_service"),
                    ins.get("insurance_paid"),
                    ins.get("insurance_adjustment"),
                    patient_responsibility,
                ),
            )

    # Re-analyze with confirmed items, including insurance context
    extracted = {
        "provider_name": bill["provider_name"],
        "provider_address": bill["provider_address"],
        "bill_date": bill["bill_date"],
        "total_charged": bill["total_charged"],
        "total_patient_owes": bill["total_patient_owes"],
        "line_items": [
            {
                "cpt_code": item.get("cpt_code"),
                "description": item.get("description"),
                "charged_amount": (
                    item.get("billed_amount")
                    if item.get("billed_amount") is not None
                    else item.get("patient_responsibility")
                ),
                "patient_responsibility": item.get("patient_responsibility"),
                "quantity": item.get("quantity", 1),
                **insurance_by_cpt.get(item.get("cpt_code"), {}),
            }
            for item in items
        ],
    }

    try:
        analysis = analyzer.analyze_bill(extracted, zip_code)
    except Exception as e:
        log.error("Re-analysis failed: %s", e, exc_info=True)
        raise HTTPException(500, f"Analysis failed: {e}")

    # Save findings and update bill totals
    with get_db() as db:
        for finding in analysis.get("findings", []):
            db.execute(
                "INSERT INTO findings (bill_id, finding_type, rule_id, severity, confidence, "
                "evidence_source, evidence_json, potential_savings, message, details) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    bill_id,
                    finding["type"],
                    finding.get("rule_id"),
                    finding["severity"],
                    finding.get("confidence"),
                    (finding.get("evidence") or {}).get("source"),
                    json.dumps(finding.get("evidence") or {}),
                    finding.get("potential_savings", 0),
                    finding["message"],
                    json.dumps(finding),
                ),
            )
        db.execute(
            "UPDATE bills SET total_findings = ?, total_potential_savings = ?, status = 'analyzed' "
            "WHERE id = ?",
            (analysis["total_findings"], analysis["total_potential_savings"], bill_id),
        )

    return {"status": "ok", "data": {"bill_id": bill_id}}


@router.get("/results/{bill_id}")
async def get_results(request: Request, bill_id: int):
    """Get analysis results for a scanned bill."""
    require_bill_access(request, bill_id)
    results = analyzer.get_bill_results(bill_id)
    if not results:
        raise HTTPException(404, "Bill not found")
    log_audit(action="view_results", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id)
    return {"status": "ok", "data": results}


@router.get("/stats")
async def get_stats():
    """Get aggregate stats for the live counter."""
    stats = analyzer.get_stats()
    return {"status": "ok", "data": stats}


@router.get("/stats/effectiveness")
async def get_effectiveness_stats():
    """Get historical effectiveness metrics from dispute outcomes."""
    metrics = analyzer.get_effectiveness_metrics()
    return {"status": "ok", "data": metrics}


@router.get("/hospitals/search")
async def search_hospitals(q: str = "", limit: int = 8):
    """Autocomplete endpoint for hospital search."""
    from hospital_seo import find_hospitals
    results = find_hospitals(q, limit=min(limit, 20))
    return {"status": "ok", "data": results}


@router.get("/dispute-packet/{bill_id}")
async def get_dispute_packet(request: Request, bill_id: int):
    """Generate a full dispute packet."""
    require_bill_access(request, bill_id)
    packet = generate_dispute_packet(bill_id)
    if not packet:
        raise HTTPException(404, "Bill not found")
    log_audit(action="generate_dispute_packet", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id)
    return {"status": "ok", "data": packet}


@router.post("/dispute-letter/{bill_id}")
async def get_dispute_letter(request: Request, bill_id: int, payload: dict):
    """Generate a structured dispute letter from selected findings."""
    require_bill_access(request, bill_id)
    selected_ids = payload.get("finding_ids", [])
    requestor_name = payload.get("requestor_name", "[Your Name]")
    account_number = payload.get("account_number", "[Account Number]")
    if not isinstance(selected_ids, list):
        raise HTTPException(400, "finding_ids must be an array")

    result = build_dispute_letter(
        bill_id,
        finding_ids=selected_ids or None,
        requestor_name=requestor_name,
        account_number=account_number,
    )
    if not result:
        raise HTTPException(404, "Bill not found or no findings available")

    log_audit(
        action="generate_dispute_letter",
        resource_type="bill",
        resource_id=str(bill_id),
        bill_id=bill_id,
        metadata={"finding_count": result["finding_count"], "total_disputed": result["total_disputed"]},
    )
    return {"status": "ok", "data": {**result, "bill_id": bill_id}}


@router.get("/dispute-phone-script/{bill_id}")
async def get_dispute_phone_script(request: Request, bill_id: int):
    """Generate a structured phone script for disputing flagged charges."""
    require_bill_access(request, bill_id)
    script = build_phone_script(bill_id)
    if not script:
        raise HTTPException(404, "Bill not found or no findings")
    return {"status": "ok", "data": {"script": script}}


@router.get("/dispute-stats")
async def dispute_stats():
    """Return aggregate dispute outcome stats (shown on site once 50+ outcomes exist)."""
    return {"status": "ok", "data": get_outcome_stats()}


@router.post("/concierge-interest")
async def record_concierge_interest(
    email: str = Form(...),
    disputed_amount: float = Form(0),
    bill_context: str = Form(""),
):
    """Capture email and disputed amount from success-fee prompt (interest only, no enrollment)."""
    email = (email or "").strip().lower()
    if not email or "@" not in email:
        raise HTTPException(400, "Valid email required")
    with get_db() as db:
        db.execute(
            "INSERT INTO concierge_interest (email, disputed_amount, bill_context) VALUES (?, ?, ?)",
            (email, disputed_amount, bill_context[:500] if bill_context else ""),
        )
    log_audit(
        action="concierge_interest",
        resource_type="concierge",
        resource_id=email,
        metadata={"disputed_amount": disputed_amount},
    )
    return {"status": "ok", "data": {"queued": True}}


def _build_report_html(results: dict) -> str:
    """Build an HTML email body from bill results."""
    bill = results.get("bill", {})
    findings = results.get("findings", [])
    provider = bill.get("provider_name") or "your provider"
    bill_date = bill.get("bill_date") or "N/A"
    total_charged = bill.get("total_charged")
    total_owes = bill.get("total_patient_owes")
    savings = bill.get("total_potential_savings") or 0
    bill_id = bill.get("id", "")
    results_url = f"{config.APP_URL.rstrip('/')}/results/{bill_id}"

    severity_colors = {"high": "#b91c1c", "medium": "#b45309", "low": "#1d4ed8"}

    finding_rows = ""
    for f in findings[:10]:  # cap at 10 in email
        sev = f.get("severity", "low")
        color = severity_colors.get(sev, "#374151")
        est = f.get("potential_savings") or f.get("estimated_patient_savings") or 0
        finding_rows += (
            f'<tr>'
            f'<td style="padding:8px 12px;border-bottom:1px solid #e5e7eb;color:{color};font-weight:600;text-transform:uppercase;font-size:11px">{sev}</td>'
            f'<td style="padding:8px 12px;border-bottom:1px solid #e5e7eb;font-size:13px;color:#111827">{f.get("message", "")}</td>'
            f'<td style="padding:8px 12px;border-bottom:1px solid #e5e7eb;font-size:13px;color:#059669;white-space:nowrap">'
            f'{"$" + f"{est:,.2f}" if est else "—"}</td>'
            f'</tr>'
        )
    if len(findings) > 10:
        finding_rows += (
            f'<tr><td colspan="3" style="padding:8px 12px;font-size:12px;color:#6b7280">'
            f'…and {len(findings) - 10} more issues. View the full report online.</td></tr>'
        )

    charge_line = f"${total_charged:,.2f}" if total_charged else "N/A"
    owes_line = f"${total_owes:,.2f}" if total_owes is not None else "N/A"

    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"></head>
<body style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f9fafb;margin:0;padding:24px">
  <div style="max-width:600px;margin:0 auto;background:#fff;border:1px solid #e5e7eb;border-radius:8px;overflow:hidden">
    <div style="background:#0f766e;padding:24px 28px">
      <p style="margin:0;color:#ccfbf1;font-size:13px;font-weight:600;letter-spacing:.05em">BILLKARMA REPORT</p>
      <h1 style="margin:6px 0 0;color:#fff;font-size:22px;font-weight:700">{len(findings)} issue{"s" if len(findings) != 1 else ""} found</h1>
    </div>
    <div style="padding:24px 28px">
      <table style="width:100%;border-collapse:collapse;margin-bottom:20px">
        <tr>
          <td style="font-size:12px;color:#6b7280;padding:4px 0">Provider</td>
          <td style="font-size:13px;color:#111827;font-weight:500;padding:4px 0">{provider}</td>
        </tr>
        <tr>
          <td style="font-size:12px;color:#6b7280;padding:4px 0">Bill date</td>
          <td style="font-size:13px;color:#111827;padding:4px 0">{bill_date}</td>
        </tr>
        <tr>
          <td style="font-size:12px;color:#6b7280;padding:4px 0">Total charged</td>
          <td style="font-size:13px;color:#111827;padding:4px 0">{charge_line}</td>
        </tr>
        <tr>
          <td style="font-size:12px;color:#6b7280;padding:4px 0">You owe</td>
          <td style="font-size:13px;color:#111827;font-weight:600;padding:4px 0">{owes_line}</td>
        </tr>
        <tr>
          <td style="font-size:12px;color:#6b7280;padding:4px 0">Potential savings</td>
          <td style="font-size:14px;color:#059669;font-weight:700;padding:4px 0">${savings:,.2f}</td>
        </tr>
      </table>
      {"<h2 style='font-size:14px;font-weight:600;color:#111827;margin:0 0 12px'>Issues found</h2><table style='width:100%;border-collapse:collapse;border:1px solid #e5e7eb;border-radius:6px;overflow:hidden'><thead><tr><th style='padding:8px 12px;background:#f9fafb;text-align:left;font-size:11px;color:#6b7280;font-weight:600;text-transform:uppercase'>Severity</th><th style='padding:8px 12px;background:#f9fafb;text-align:left;font-size:11px;color:#6b7280;font-weight:600;text-transform:uppercase'>Finding</th><th style='padding:8px 12px;background:#f9fafb;text-align:left;font-size:11px;color:#6b7280;font-weight:600;text-transform:uppercase'>Est. savings</th></tr></thead><tbody>" + finding_rows + "</tbody></table>" if findings else "<p style='color:#059669;font-weight:600'>No significant issues found — your bill looks clean.</p>"}
      <div style="margin-top:24px;text-align:center">
        <a href="{results_url}" style="display:inline-block;background:#0f766e;color:#fff;text-decoration:none;padding:10px 24px;border-radius:6px;font-size:14px;font-weight:600">View full report &amp; dispute tools →</a>
      </div>
    </div>
    <div style="padding:16px 28px;border-top:1px solid #e5e7eb;background:#f9fafb">
      <p style="margin:0;font-size:11px;color:#9ca3af">BillKarma compares charges against CMS Medicare rate data. This is not medical or legal advice.</p>
    </div>
  </div>
</body></html>"""


@router.post("/email-report")
async def email_report(request: Request):
    """Email a bill report to the user. Requires SENDGRID_API_KEY to deliver."""
    body = await request.json()
    bill_id = body.get("bill_id")
    to_email = (body.get("email") or "").strip()

    if not to_email:
        raise HTTPException(400, "email is required")
    if not bill_id:
        raise HTTPException(400, "bill_id is required")

    results = analyzer.get_bill_results(int(bill_id))
    if not results:
        raise HTTPException(404, "Bill not found")

    bill = results["bill"]
    findings_count = bill.get("total_findings") or len(results.get("findings", []))
    savings = bill.get("total_potential_savings") or 0

    subject = f"Your BillKarma report: {findings_count} issue{'s' if findings_count != 1 else ''} found"
    if savings:
        subject += f" — up to ${savings:,.0f} in potential savings"

    html = _build_report_html(results)

    try:
        sent = email_service.send_email(to_email, subject, html)
    except RuntimeError as e:
        log.error("email_report delivery failed: %s", e)
        raise HTTPException(503, "Email delivery failed. Check back later or copy your report manually.")

    log_audit(
        action="email_report",
        resource_type="bill",
        resource_id=str(bill_id),
        bill_id=int(bill_id),
        metadata={"email": to_email, "sent": sent},
    )
    return {"status": "ok", "data": {"sent": sent}}


@router.get("/appeal-playbook/{bill_id}")
async def get_appeal_playbook(request: Request, bill_id: int):
    """Generate issue-specific appeal steps."""
    require_bill_access(request, bill_id)
    playbook = generate_appeal_playbook(bill_id)
    if not playbook:
        raise HTTPException(404, "Bill not found")
    return {"status": "ok", "data": playbook}


@router.get("/appeal-template/{bill_id}")
async def get_appeal_template(request: Request, bill_id: int):
    """Generate an insurance appeal letter from findings."""
    require_bill_access(request, bill_id)
    from dispute_workflow import build_appeal_letter
    result = build_appeal_letter(bill_id)
    if not result:
        raise HTTPException(404, "Bill not found or no findings")
    log_audit(action="generate_appeal_template", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id)
    return {"status": "ok", "data": result}


@router.get("/phone-script/{bill_id}")
async def get_phone_script(request: Request, bill_id: int):
    """Generate a phone script for disputing a bill."""
    require_bill_access(request, bill_id)
    script = negotiation.generate_phone_script(bill_id)
    if not script:
        raise HTTPException(404, "Bill not found or no findings")
    return {"status": "ok", "data": {"script": script}}


@router.get("/message-script/{bill_id}")
async def get_message_script(request: Request, bill_id: int):
    """Generate a written message script for portal/text disputes."""
    require_bill_access(request, bill_id)
    script = negotiation.generate_message_script(bill_id)
    if not script:
        raise HTTPException(404, "Bill not found or no findings")
    return {"status": "ok", "data": {"script": script}}


# --- Negotiation endpoints ---


@router.post("/negotiate/start")
async def start_negotiation(
    request: Request,
    bill_id: int = Form(...),
    user_id: int = Form(None),
    account_number: str = Form(...),
    hospital_email: str = Form(""),
):
    """Create a new negotiation for a bill."""
    require_bill_access(request, bill_id)
    try:
        neg_id = negotiation.create_negotiation(bill_id, user_id, account_number, hospital_email)
    except ValueError as e:
        raise HTTPException(404, str(e))
    return {"status": "ok", "data": {"negotiation_id": neg_id}}


@router.post("/negotiate/{negotiation_id}/generate")
async def generate_email(negotiation_id: int):
    """Generate the next dispute email draft."""
    email_data = negotiation.generate_dispute_email(negotiation_id)
    return {"status": "ok", "data": email_data}


@router.post("/negotiate/message/{message_id}/approve")
async def approve_message(message_id: int):
    """Approve and send a drafted negotiation email."""
    negotiation.approve_and_send(message_id)
    return {"status": "ok", "data": {"sent": True}}


@router.post("/negotiate/{negotiation_id}/response")
async def record_response(negotiation_id: int, body: str = Form(...)):
    """Record and parse a hospital response."""
    analysis = negotiation.record_hospital_response(negotiation_id, body)
    return {"status": "ok", "data": analysis}


@router.get("/negotiate/{negotiation_id}/copilot")
async def negotiation_copilot(negotiation_id: int):
    """Return stage tracking and recommended next reply."""
    data = negotiation.get_copilot_summary(negotiation_id)
    if not data:
        raise HTTPException(404, "Negotiation not found")
    return {"status": "ok", "data": data}


# --- Dispute outcome tracking ---


VALID_OUTCOMES = {"pending", "reduced", "forgiven", "no_change", "sent_to_collections"}


@router.post("/dispute-outcome")
async def record_dispute_outcome(
    request: Request,
    bill_id: int = Form(...),
    user_id: int = Form(None),
    called_billing: bool = Form(False),
    outcome: str = Form("pending"),
    final_patient_owes: float = Form(0),
    notes: str = Form(""),
    share_publicly: bool = Form(False),
):
    """Record what happened after the user disputed their bill."""
    require_bill_access(request, bill_id)
    if outcome not in VALID_OUTCOMES:
        raise HTTPException(400, f"outcome must be one of: {', '.join(sorted(VALID_OUTCOMES))}")
    if final_patient_owes < 0:
        raise HTTPException(400, "final_patient_owes cannot be negative")

    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            raise HTTPException(404, "Bill not found")

        original = bill["total_patient_owes"] or 0
        actual_savings = max(0, original - final_patient_owes)

        db.execute(
            "INSERT INTO dispute_outcomes (bill_id, user_id, hospital_name, called_billing, "
            "outcome, original_patient_owes, final_patient_owes, actual_savings, notes, shared_publicly) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                bill_id,
                user_id,
                bill["provider_name"],
                called_billing,
                outcome,
                original,
                final_patient_owes,
                actual_savings,
                notes,
                share_publicly,
            ),
        )

    # New outcome data invalidates adaptive thresholds and stats caches
    analyzer._invalidate_adaptive_cache()

    log_audit(
        action="record_dispute_outcome",
        resource_type="bill",
        resource_id=str(bill_id),
        user_id=user_id,
        bill_id=bill_id,
        metadata={"outcome": outcome, "actual_savings": actual_savings},
    )
    return {"status": "ok", "data": {"actual_savings": actual_savings}}


@router.post("/claims")
async def create_claim(
    request: Request,
    bill_id: int = Form(...),
    user_id: int = Form(None),
    channel: str = Form("provider_billing"),
    note: str = Form(""),
):
    """Create a new claim workflow record for a bill."""
    require_bill_access(request, bill_id)
    with get_db() as db:
        bill = db.execute("SELECT id FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            raise HTTPException(404, "Bill not found")

        cursor = db.execute(
            "INSERT INTO dispute_claims (bill_id, user_id, current_status, channel, notes) VALUES (?, ?, 'drafted', ?, ?)",
            (bill_id, user_id, channel, note),
        )
        claim_id = cursor.lastrowid
        db.execute(
            "INSERT INTO dispute_claim_events (claim_id, from_status, to_status, event_note) VALUES (?, ?, ?, ?)",
            (claim_id, None, "drafted", "Claim created"),
        )
    log_audit(action="create_claim", resource_type="claim", resource_id=str(claim_id), bill_id=bill_id)

    return {"status": "ok", "data": {"claim_id": claim_id, "current_status": "drafted"}}


@router.get("/claims/{bill_id}")
async def list_claims(request: Request, bill_id: int):
    """List claim workflow records for a bill."""
    require_bill_access(request, bill_id)
    with get_db() as db:
        rows = db.execute(
            "SELECT * FROM dispute_claims WHERE bill_id = ? ORDER BY id DESC",
            (bill_id,),
        ).fetchall()
        claims = []
        for row in rows:
            events = db.execute(
                "SELECT from_status, to_status, event_note, created_at FROM dispute_claim_events "
                "WHERE claim_id = ? ORDER BY id",
                (row["id"],),
            ).fetchall()
            claim = dict(row)
            claim["events"] = [dict(e) for e in events]
            claims.append(claim)
    return {"status": "ok", "data": {"bill_id": bill_id, "claims": claims}}


@router.post("/claims/{claim_id}/status")
async def update_claim_status(request: Request, claim_id: int, status: str = Form(...), note: str = Form("")):
    """Transition a claim status and append an audit event."""
    target = (status or "").strip().lower()
    if target not in CLAIM_TRANSITIONS:
        raise HTTPException(400, f"Invalid status '{status}'")

    with get_db() as db:
        claim = db.execute("SELECT * FROM dispute_claims WHERE id = ?", (claim_id,)).fetchone()
        if not claim:
            raise HTTPException(404, "Claim not found")
        require_bill_access(request, int(claim["bill_id"]))

        prev = claim["current_status"]
        allowed = CLAIM_TRANSITIONS.get(prev, set())
        if target not in allowed:
            raise HTTPException(400, f"Cannot transition from '{prev}' to '{target}'")
        db.execute(
            "UPDATE dispute_claims SET current_status = ?, updated_at = CURRENT_TIMESTAMP, "
            "notes = CASE WHEN ? != '' THEN COALESCE(notes, '') || '\n' || ? ELSE notes END "
            "WHERE id = ?",
            (target, note, note, claim_id),
        )
        db.execute(
            "INSERT INTO dispute_claim_events (claim_id, from_status, to_status, event_note) VALUES (?, ?, ?, ?)",
            (claim_id, prev, target, note or "status update"),
        )
    log_audit(
        action="update_claim_status",
        resource_type="claim",
        resource_id=str(claim_id),
        metadata={"from": prev, "to": target},
    )

    return {"status": "ok", "data": {"claim_id": claim_id, "from_status": prev, "to_status": target}}


@router.get("/calculator/cost")
async def calculator_cost_lookup(cpt_code: str, zip_code: str = ""):
    """Look up Medicare rate and benchmarks for a procedure by CPT code and ZIP."""
    cpt_code = cpt_code.strip().upper()
    zip_code = zip_code.strip()

    if not cpt_code:
        raise HTTPException(400, "cpt_code is required")

    from validators.pricing import get_medicare_rate, get_opps_rate
    from validators.geo import get_medicare_locality, get_region
    from validators.benchmarks import get_benchmark

    locality = get_medicare_locality(zip_code) if zip_code else "0000000"
    medicare_rate = get_medicare_rate(cpt_code, locality)
    opps_rate = get_opps_rate(cpt_code)
    benchmark = get_benchmark(cpt_code, zip_code)

    with get_db() as db:
        desc_row = db.execute(
            "SELECT description FROM medicare_rates WHERE cpt_code = ? AND description IS NOT NULL LIMIT 1",
            (cpt_code,),
        ).fetchone()

    description = desc_row["description"] if desc_row else None
    total_medicare = None
    if medicare_rate and opps_rate:
        total_medicare = round(medicare_rate + opps_rate, 2)

    result = {
        "cpt_code": cpt_code,
        "zip_code": zip_code or None,
        "description": description,
        "medicare_rate": medicare_rate,
        "opps_rate": opps_rate,
        "total_medicare": total_medicare,
        "locality": locality,
        "region": get_region(zip_code) if zip_code else "national",
    }

    if benchmark:
        result["benchmark"] = {
            "median_charged": benchmark.get("median_charged"),
            "p25_charged": benchmark.get("p25_charged"),
            "p75_charged": benchmark.get("p75_charged"),
            "sample_size": benchmark.get("sample_size"),
            "region": benchmark.get("region"),
        }

    return {"status": "ok", "data": result}


@router.get("/calculator/markup")
async def calculator_markup_check(cpt_code: str, charged: float, zip_code: str = ""):
    """Check how a charge compares to Medicare and regional benchmarks."""
    cpt_code = cpt_code.strip().upper()
    zip_code = zip_code.strip()

    if not cpt_code:
        raise HTTPException(400, "cpt_code is required")
    if charged <= 0:
        raise HTTPException(400, "charged must be positive")

    from validators.pricing import get_medicare_rate, get_opps_rate
    from validators.geo import get_medicare_locality, get_region
    from validators.benchmarks import get_benchmark

    locality = get_medicare_locality(zip_code) if zip_code else "0000000"
    medicare_rate = get_medicare_rate(cpt_code, locality)
    opps_rate = get_opps_rate(cpt_code)
    benchmark = get_benchmark(cpt_code, zip_code)

    with get_db() as db:
        desc_row = db.execute(
            "SELECT description FROM medicare_rates WHERE cpt_code = ? AND description IS NOT NULL LIMIT 1",
            (cpt_code,),
        ).fetchone()

    description = desc_row["description"] if desc_row else None

    result = {
        "cpt_code": cpt_code,
        "charged": charged,
        "zip_code": zip_code or None,
        "description": description,
    }

    if medicare_rate:
        markup = round(charged / medicare_rate, 1)
        fair_price = round(medicare_rate * config.MEDICARE_MARKUP_THRESHOLD, 2)
        potential_savings = round(max(0, charged - fair_price), 2)

        total_medicare = None
        if opps_rate:
            total_medicare = round(medicare_rate + opps_rate, 2)

        result["medicare"] = {
            "rate": medicare_rate,
            "opps_rate": opps_rate,
            "total_medicare": total_medicare,
            "markup": markup,
            "fair_estimate": fair_price,
            "potential_savings": potential_savings,
            "assessment": (
                "high" if markup > config.HIGH_MARKUP_THRESHOLD
                else "elevated" if markup > config.MEDICARE_MARKUP_THRESHOLD
                else "fair"
            ),
        }

    if benchmark and benchmark.get("median_charged"):
        result["benchmark"] = {
            "median_charged": benchmark["median_charged"],
            "p75_charged": benchmark.get("p75_charged"),
            "sample_size": benchmark.get("sample_size"),
            "region": benchmark.get("region"),
            "vs_median": round(charged / benchmark["median_charged"], 1),
        }

    return {"status": "ok", "data": result}


@router.post("/tools/{slug}/run")
async def run_tool_endpoint(slug: str, request: Request):
    """Run a deterministic tool workflow and persist run metadata."""
    client_ip = request.client.host if request.client else "unknown"
    if not _check_tools_rate_limit(client_ip):
        raise HTTPException(
            429,
            f"Too many tool requests. Max {config.TOOLS_RATE_LIMIT_REQUESTS} per window.",
        )
    tool = get_tool(slug)
    if not tool:
        raise HTTPException(404, "Tool not found")

    payload = await _parse_json_object(request)
    _assert_payload_size(
        payload,
        config.MAX_TOOL_PAYLOAD_BYTES,
        f"Payload too large. Limit is {config.MAX_TOOL_PAYLOAD_BYTES} bytes.",
    )

    try:
        result = run_tool(slug, payload)
    except ValueError as exc:
        raise HTTPException(400, str(exc))
    except Exception as exc:
        log.error("tools_run failed for %s: %s", slug, exc, exc_info=True)
        raise HTTPException(500, "Tool run failed")

    with get_db() as db:
        db.execute(
            """
            INSERT INTO tool_runs (tool_slug, input_hash, input_json, result_state, result_json)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                slug,
                hash_payload(payload),
                json.dumps(payload),
                result.get("result_state"),
                json.dumps(result),
            ),
        )
    return result


@router.post("/tools/lead-capture")
async def tool_lead_capture(request: Request):
    """Capture tool lead emails for lifecycle follow-up (no immediate drip send)."""
    client_ip = request.client.host if request.client else "unknown"
    if not _check_tools_rate_limit(client_ip):
        raise HTTPException(
            429,
            f"Too many tool requests. Max {config.TOOLS_RATE_LIMIT_REQUESTS} per window.",
        )

    payload = await _parse_json_object(request)
    _assert_payload_size(
        payload,
        config.MAX_TOOL_CONTEXT_BYTES,
        f"Payload too large. Limit is {config.MAX_TOOL_CONTEXT_BYTES} bytes.",
    )

    email = (payload.get("email") or "").strip().lower()
    tool_slug = (payload.get("tool_slug") or "").strip()
    lead_magnet_key = (payload.get("lead_magnet_key") or "").strip()
    context = payload.get("context")

    if not _validate_email(email):
        raise HTTPException(400, "Valid email required")
    if not get_tool(tool_slug):
        raise HTTPException(400, "Unknown tool_slug")
    if context is not None and not isinstance(context, (dict, list, str, int, float, bool)):
        raise HTTPException(400, "context must be a JSON scalar, array, or object")

    with get_db() as db:
        db.execute(
            """
            INSERT INTO tool_leads (email, tool_slug, lead_magnet_key, payload_json)
            VALUES (?, ?, ?, ?)
            """,
            (
                email,
                tool_slug,
                lead_magnet_key or None,
                json.dumps(context, ensure_ascii=False) if context is not None else None,
            ),
        )

    return {"status": "ok", "data": {"captured": True}}


@router.get("/ops/ocr-benchmark")
async def ocr_benchmark(request: Request):
    """Run OCR benchmark over local fixture manifest."""
    _require_admin_access(request)
    manifest = "data/ocr_benchmark/manifest.json"
    try:
        result = run_manifest(manifest)
    except FileNotFoundError:
        raise HTTPException(404, "Benchmark manifest not found. Run scripts/generate_ocr_benchmark_samples.py first.")
    return {"status": "ok", "data": result}


@router.get("/provider-intelligence/{provider_name}")
async def provider_intel(provider_name: str):
    """Provider-level issue and outcomes intelligence."""
    return {"status": "ok", "data": get_provider_intelligence(provider_name)}


@router.post("/consent")
async def capture_consent(
    request: Request,
    user_id: int = Form(None),
    bill_id: int = Form(None),
    consent_type: str = Form(...),
    consent_version: str = Form(...),
):
    consent_id = record_consent(
        user_id=user_id,
        bill_id=bill_id,
        consent_type=consent_type,
        consent_version=consent_version,
        ip_address=(request.client.host if request.client else ""),
        user_agent=request.headers.get("user-agent", ""),
    )
    log_audit(
        action="capture_consent",
        resource_type="consent",
        resource_id=str(consent_id),
        user_id=user_id,
        bill_id=bill_id,
        metadata={"consent_type": consent_type, "consent_version": consent_version},
    )
    return {"status": "ok", "data": {"consent_id": consent_id}}


@router.get("/bills/{bill_id}/export")
async def export_bill(request: Request, bill_id: int):
    _require_admin_access(request)
    payload = export_bill_data(bill_id)
    if not payload:
        raise HTTPException(404, "Bill not found")
    log_audit(action="export_bill", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id)
    return {"status": "ok", "data": payload}


@router.delete("/bills/{bill_id}")
async def delete_bill(request: Request, bill_id: int):
    _require_admin_access(request)
    deleted = delete_bill_data(bill_id)
    if not deleted:
        raise HTTPException(404, "Bill not found")
    # Bill row is deleted above, so avoid FK violations in audit_logs.bill_id.
    log_audit(
        action="delete_bill",
        resource_type="bill",
        resource_id=str(bill_id),
        bill_id=None,
        metadata={"deleted_bill_id": bill_id},
    )
    return {"status": "ok", "data": {"deleted": True}}


@router.post("/compliance/purge-old")
async def purge_old(request: Request, days: int = Form(365)):
    _require_admin_access(request)
    if days < 1 or days > 3650:
        raise HTTPException(400, "days must be between 1 and 3650")
    deleted = purge_old_data(days=days)
    log_audit(action="purge_old_data", resource_type="compliance", resource_id=str(days), metadata={"deleted": deleted})
    return {"status": "ok", "data": {"deleted_bills": deleted, "days": days}}


@router.post("/confirm-items")
async def confirm_items(
    request: Request,
    bill_id: int = Form(...),
    confirmed_items: str = Form(...),
):
    """User confirms/edits extracted line items before analysis."""
    require_bill_access(request, bill_id)
    try:
        items = json.loads(confirmed_items)
    except json.JSONDecodeError as e:
        raise HTTPException(400, f"Invalid JSON in confirmed_items: {e}")

    with get_db() as db:
        # Delete old line items and re-insert confirmed ones
        db.execute("DELETE FROM line_items WHERE bill_id = ?", (bill_id,))
        for item in items:
            db.execute(
                "INSERT INTO line_items (bill_id, date_of_service, cpt_code, description, "
                "quantity, charged_amount, insurance_paid, insurance_adjustment, "
                "patient_responsibility, extraction_confidence) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'high')",
                (
                    bill_id,
                    item.get("date_of_service"),
                    item.get("cpt_code"),
                    item.get("description"),
                    item.get("quantity", 1),
                    item.get("charged_amount"),
                    item.get("insurance_paid"),
                    item.get("insurance_adjustment"),
                    item.get("patient_responsibility"),
                ),
            )

    return {"status": "ok", "data": {"bill_id": bill_id, "items_confirmed": len(items)}}


# ──────────────────────────────────────────────────────────────────────────────
# DISPUTE SERVICE — Paid dispute activation, e-sign, payment, follow-ups
# ──────────────────────────────────────────────────────────────────────────────


@router.post("/dispute/checkout")
async def create_dispute_checkout(
    request: Request,
    bill_id: int = Form(...),
    email: str = Form(...),
):
    """Create a Stripe Checkout session for the dispute service fee."""
    require_bill_access(request, bill_id)
    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        raise HTTPException(400, "Invalid email address")

    with get_db() as db:
        bill = db.execute("SELECT total_patient_owes, total_charged FROM bills WHERE id = ?", (bill_id,)).fetchone()
    if not bill:
        raise HTTPException(404, "Bill not found")

    bill_total = float(bill["total_patient_owes"] or bill["total_charged"] or 0)
    fee_cents = payment_module.calculate_fee(bill_total)

    try:
        session = payment_module.create_checkout_session(
            bill_id=bill_id,
            email=email,
            amount_cents=fee_cents,
        )
    except RuntimeError as exc:
        raise HTTPException(500, str(exc))

    return {"status": "ok", "data": {"checkout_url": session["url"], "session_id": session["id"], "fee_cents": fee_cents}}


@router.post("/stripe/webhook")
async def stripe_webhook(request: Request):
    """Handle Stripe webhook events (payment.completed, charge.refunded)."""
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")

    if not config.STRIPE_WEBHOOK_SECRET and not config.DEBUG:
        raise HTTPException(503, "Webhook secret not configured")

    if config.STRIPE_WEBHOOK_SECRET:
        if not payment_module.verify_webhook_signature(payload, sig_header, config.STRIPE_WEBHOOK_SECRET):
            raise HTTPException(400, "Invalid webhook signature")

    try:
        event = json.loads(payload)
    except json.JSONDecodeError:
        raise HTTPException(400, "Invalid JSON")

    event_type = event.get("type", "")
    data = event.get("data", {}).get("object", {})

    if event_type == "checkout.session.completed":
        session_id = data.get("id")
        metadata = data.get("metadata", {})
        payment_purpose = metadata.get("payment_purpose", "")

        if payment_purpose == "debt_letter":
            # Certified mail payment — trigger Lob send
            debt_letter_id = metadata.get("debt_letter_id")
            if debt_letter_id:
                try:
                    with get_db() as db:
                        lob_result = debt_fighter.send_via_lob(db, int(debt_letter_id), config.LOB_API_KEY)
                    log_audit(action="debt_letter_sent", resource_type="debt_letter",
                              resource_id=debt_letter_id,
                              metadata={"lob_id": lob_result.get("lob_id"), "tracking": lob_result.get("tracking_number")})
                except Exception as exc:
                    log.error("Lob send failed for debt_letter_id=%s: %s", debt_letter_id, exc)
                    # Payment succeeded — mark as 'pending_send' so we can retry
                    with get_db() as db:
                        db.execute(
                            "UPDATE debt_letters SET status = 'pending_send', stripe_payment_id = ? WHERE id = ?",
                            (session_id, int(debt_letter_id)),
                        )
        else:
            # Dispute service payment
            bill_id = payment_module.record_payment_success(session_id)
            if bill_id:
                log_audit(action="payment_completed", resource_type="dispute_payment",
                          resource_id=session_id, metadata={"bill_id": bill_id})

    return {"status": "ok"}


@router.get("/dispute/session/{session_id}")
async def get_dispute_session_context(request: Request, session_id: str):
    """Resolve Stripe session to bill/case context for resilient post-checkout UX."""
    if not session_id or len(session_id) > 200:
        raise HTTPException(400, "Invalid session_id")

    with get_db() as db:
        payment_row = db.execute(
            "SELECT bill_id, status FROM dispute_payments WHERE stripe_session_id = ?",
            (session_id,),
        ).fetchone()
        if not payment_row:
            raise HTTPException(404, "Session not found")

        bill_id = int(payment_row["bill_id"])
        case_row = db.execute(
            "SELECT id, patient_name, patient_email, patient_address, account_number "
            "FROM dispute_cases WHERE bill_id = ? ORDER BY id DESC LIMIT 1",
            (bill_id,),
        ).fetchone()
        esign_row = db.execute(
            "SELECT patient_name, patient_email FROM esign_records WHERE bill_id = ? ORDER BY id DESC LIMIT 1",
            (bill_id,),
        ).fetchone()

    sid, created = get_or_create_session_id(request)
    try:
        grant_bill_access(sid, bill_id)
    except Exception as exc:
        log.warning("Unable to grant bill access from session context for bill_id=%s: %s", bill_id, exc)

    payload = {
        "status": "ok",
        "data": {
            "bill_id": bill_id,
            "payment_status": payment_row["status"],
            "case_id": int(case_row["id"]) if case_row else None,
            "patient_name": (case_row["patient_name"] if case_row else None) or (esign_row["patient_name"] if esign_row else None),
            "patient_email": (case_row["patient_email"] if case_row else None) or (esign_row["patient_email"] if esign_row else None),
            "patient_address": case_row["patient_address"] if case_row else None,
            "account_number": case_row["account_number"] if case_row else None,
        },
    }
    response = JSONResponse(payload)
    if created:
        set_session_cookie(response, sid)
    return response


@router.get("/dispute/esign/{bill_id}")
async def get_esign_status(request: Request, bill_id: int):
    """Get e-signature status for all three documents."""
    require_bill_access(request, bill_id)
    status = esign_module.get_status(bill_id)
    return {"status": "ok", "data": status}


@router.post("/dispute/esign/{bill_id}")
async def record_esign(
    request: Request,
    bill_id: int,
    patient_name: str = Form(...),
    patient_email: str = Form(...),
    doc_type: str = Form(...),
):
    """Record an e-signature for a specific document type."""
    require_bill_access(request, bill_id)
    if doc_type not in esign_module.ALL_DOCS:
        raise HTTPException(400, f"doc_type must be one of: {', '.join(esign_module.ALL_DOCS)}")

    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", patient_email):
        raise HTTPException(400, "Invalid email address")

    ip = request.client.host if request.client else "unknown"
    user_agent = request.headers.get("user-agent", "")

    esign_module.get_or_create_session(bill_id, patient_name, patient_email)
    esign_module.record_signature(bill_id, doc_type, ip, user_agent)

    record_consent(
        user_id=None, bill_id=bill_id,
        consent_type=doc_type, consent_version=esign_module.ESIGN_VERSION,
        ip_address=ip, user_agent=user_agent,
    )

    status = esign_module.get_status(bill_id)
    return {"status": "ok", "data": status}


@router.post("/dispute/activate")
async def activate_dispute(
    request: Request,
    bill_id: int = Form(...),
    stripe_session_id: str = Form(...),
    patient_name: str = Form(...),
    patient_email: str = Form(...),
    patient_address: str = Form(""),
    account_number: str = Form(""),
    hospital_billing_email: str = Form(""),
    hospital_billing_fax: str = Form(""),
    preferred_channels: str = Form("email"),
):
    """Activate a paid dispute case after payment and e-sign completion."""
    require_bill_access(request, bill_id)
    # Verify all docs are signed
    esign_status = esign_module.get_status(bill_id)
    if not esign_status.get("all_signed"):
        raise HTTPException(400, "All three documents must be signed before activating dispute")

    # Verify payment is confirmed
    payment_row = payment_module.get_payment_for_bill(bill_id)
    if not payment_row or payment_row["status"] != "paid":
        # Try to confirm from Stripe
        try:
            session = payment_module.get_session(stripe_session_id)
            if session.get("payment_status") == "paid":
                payment_module.record_payment_success(stripe_session_id)
                payment_row = payment_module.get_payment_for_bill(bill_id)
        except Exception:
            pass

    if not payment_row or payment_row["status"] != "paid":
        raise HTTPException(402, "Payment not confirmed")

    try:
        case_id = dispute_service.activate_dispute(
            bill_id=bill_id,
            payment_id=payment_row["id"],
            patient_name=patient_name,
            patient_email=patient_email,
            patient_address=patient_address,
            account_number=account_number,
            hospital_billing_email=hospital_billing_email,
            hospital_billing_fax=hospital_billing_fax,
            preferred_channels=preferred_channels,
        )
    except Exception as exc:
        log.error("Failed to activate dispute for bill %d: %s", bill_id, exc)
        raise HTTPException(500, "Failed to activate dispute")

    log_audit(action="dispute_activated", resource_type="dispute_case",
              resource_id=str(case_id), bill_id=bill_id)

    return {"status": "ok", "data": {"case_id": case_id}}


@router.get("/dispute/dashboard/{bill_id}")
async def dispute_dashboard(request: Request, bill_id: int):
    """Get the full dispute dashboard data for a bill."""
    require_bill_access(request, bill_id)
    summary = dispute_service.get_dispute_summary(bill_id)
    return {"status": "ok", "data": summary}


@router.post("/dispute/resolve/{case_id}")
async def resolve_dispute(
    request: Request,
    case_id: int,
    outcome: str = Form(...),
    actual_savings: float = Form(0.0),
):
    """Mark a dispute case as resolved."""
    _require_admin_access(request)
    valid_outcomes = {"reduced", "forgiven", "denied", "payment_plan", "other"}
    if outcome not in valid_outcomes:
        raise HTTPException(400, f"outcome must be one of: {', '.join(valid_outcomes)}")

    case = dispute_service.get_case(case_id)
    if not case:
        raise HTTPException(404, "Case not found")

    dispute_service.mark_resolved(case_id, outcome, actual_savings if actual_savings > 0 else None)
    log_audit(action="dispute_resolved", resource_type="dispute_case",
              resource_id=str(case_id), metadata={"outcome": outcome, "savings": actual_savings})

    return {"status": "ok", "data": {"case_id": case_id, "outcome": outcome}}


@router.post("/dispute/refund/{case_id}")
async def request_refund(request: Request, case_id: int):
    """Issue a refund for a dispute case that couldn't be resolved."""
    _require_admin_access(request)
    case = dispute_service.get_case(case_id)
    if not case:
        raise HTTPException(404, "Case not found")
    if case["status"] == "refunded":
        return {"status": "ok", "data": {"message": "Already refunded"}}
    if case["status"] == "resolved":
        raise HTTPException(400, "Cannot refund a resolved case")

    try:
        refunded = dispute_service.issue_refund_for_case(case_id)
    except Exception as exc:
        raise HTTPException(500, f"Refund failed: {exc}")

    log_audit(action="dispute_refunded", resource_type="dispute_case", resource_id=str(case_id))

    return {"status": "ok", "data": {"refunded": refunded}}


@router.post("/dispute/{case_id}/pause")
async def pause_dispute(request: Request, case_id: int):
    """Pause follow-ups for a dispute case."""
    require_case_access(request, case_id)
    case = dispute_service.get_case(case_id)
    if not case:
        raise HTTPException(404, "Case not found")
    if case["status"] not in ("active", "sent"):
        raise HTTPException(400, f"Cannot pause a case with status '{case['status']}'")

    dispute_service.pause_dispute(case_id)
    log_audit(action="dispute_paused", resource_type="dispute_case", resource_id=str(case_id))
    return {"status": "ok", "data": {"case_id": case_id, "new_status": "paused"}}


@router.post("/dispute/{case_id}/escalate")
async def escalate_dispute(request: Request, case_id: int):
    """Escalate a dispute case."""
    require_case_access(request, case_id)
    case = dispute_service.get_case(case_id)
    if not case:
        raise HTTPException(404, "Case not found")
    if case["status"] not in ("active", "sent"):
        raise HTTPException(400, f"Cannot escalate a case with status '{case['status']}'")

    dispute_service.escalate_dispute(case_id)
    log_audit(action="dispute_escalated", resource_type="dispute_case", resource_id=str(case_id))
    return {"status": "ok", "data": {"case_id": case_id, "escalated": True}}


@router.post("/dispute/run-followups")
async def run_followups(request: Request):
    """Admin endpoint: process all overdue follow-ups."""
    _require_admin_access(request)
    sent = dispute_service.process_due_followups()
    return {"status": "ok", "data": {"followups_sent": sent}}


@router.get("/dispute/fee")
async def get_dispute_fee(request: Request, bill_id: int):
    """Return the dispute fee for a bill based on its total."""
    require_bill_access(request, bill_id)
    with get_db() as db:
        bill = db.execute("SELECT total_patient_owes, total_charged FROM bills WHERE id = ?", (bill_id,)).fetchone()
    if not bill:
        raise HTTPException(404, "Bill not found")

    bill_total = float(bill["total_patient_owes"] or bill["total_charged"] or 0)
    fee_cents = payment_module.calculate_fee(bill_total)

    return {"status": "ok", "data": {"fee_cents": fee_cents, "fee_dollars": fee_cents / 100}}


# ──────────────────────────────────────────────────────────────────────────────
# DEBT FIGHTER — SOL calculator, FDCPA letters, charity care, settlement
# ──────────────────────────────────────────────────────────────────────────────

import debt_fighter


def _debt_rate_check(request: Request):
    """Rate-limit debt fighter endpoints (same limits as /scan)."""
    client_ip = request.client.host if request.client else "unknown"
    if not _check_rate_limit(client_ip):
        raise HTTPException(429, "Too many requests. Please try again later.")


@router.post("/sol-check")
async def sol_check(request: Request):
    """Check statute of limitations for a medical debt."""
    _debt_rate_check(request)
    body = await request.json()
    state = (body.get("state") or "").strip()
    start_date = (body.get("start_date") or "").strip()

    if not state or not start_date:
        raise HTTPException(400, "state and start_date are required")

    result = debt_fighter.check_sol(state, start_date)
    if result["status"] == "error":
        raise HTTPException(400, result["message"])

    log_audit(action="sol_check", resource_type="debt_tool",
              resource_id=state, metadata={"state": state, "start_date": start_date})
    return {"status": "ok", "data": result}


@router.get("/collection-notice/letter-types")
async def get_letter_types():
    """Return available FDCPA letter types with descriptions."""
    return {"status": "ok", "data": debt_fighter.LETTER_TYPES}


@router.get("/collection-notice/rights")
async def get_fdcpa_rights():
    """Return FDCPA rights educational content."""
    return {
        "status": "ok",
        "data": {
            "rights": debt_fighter.FDCPA_RIGHTS,
            "certified_mail_guide": debt_fighter.CERTIFIED_MAIL_GUIDE,
        },
    }


@router.post("/collection-notice/generate")
async def generate_fdcpa_letter(request: Request):
    """Generate an FDCPA letter (validation, cease & desist, or dispute)."""
    _debt_rate_check(request)
    body = await request.json()

    letter_type = (body.get("letter_type") or "debt_validation").strip()
    required = ["user_name", "user_address", "collector_name", "collector_address",
                "account_number", "amount"]
    missing = [f for f in required if not (body.get(f) or "").strip()]
    if missing:
        raise HTTPException(400, f"Missing required fields: {', '.join(missing)}")

    try:
        result = debt_fighter.generate_fdcpa_letter(
            letter_type=letter_type,
            user_name=body["user_name"].strip(),
            user_address=body["user_address"].strip(),
            collector_name=body["collector_name"].strip(),
            collector_address=body["collector_address"].strip(),
            account_number=body["account_number"].strip(),
            amount=body["amount"].strip(),
            date_of_notice=(body.get("date_of_notice") or "").strip(),
            dispute_reason=(body.get("dispute_reason") or "").strip(),
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc))

    user_email = (body.get("email") or "").strip()
    with get_db() as db:
        cursor = db.execute(
            "INSERT INTO debt_letters "
            "(letter_type, user_email, user_name, user_address, collector_name, collector_address, account_number, amount, letter_text) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (letter_type, user_email or None, result["user_name"], result["user_address"],
             result["collector_name"], result["collector_address"],
             result["account_number"], result["amount"], result["letter_text"]),
        )
        debt_letter_id = cursor.lastrowid

    result["debt_letter_id"] = debt_letter_id
    result["certified_mail_price_cents"] = config.FDCPA_LETTER_PRICE_CENTS

    log_audit(action="generate_fdcpa_letter", resource_type="debt_letter",
              resource_id=result["account_number"],
              metadata={"letter_type": letter_type, "collector": result["collector_name"]})
    return {"status": "ok", "data": result}


@router.post("/collection-notice/send")
async def send_fdcpa_letter(request: Request):
    """Send the FDCPA letter via certified mail (Lob integration placeholder)."""
    _debt_rate_check(request)
    body = await request.json()
    letter_text = (body.get("letter_text") or "").strip()
    if not letter_text:
        raise HTTPException(400, "letter_text is required")

    if not config.LOB_API_KEY:
        return {
            "status": "ok",
            "data": {
                "sent": False,
                "message": "Certified mail sending is coming soon. For now, download your letter and mail it yourself.",
                "certified_mail_guide": debt_fighter.CERTIFIED_MAIL_GUIDE,
                "letter_text": letter_text,
            },
        }

    return {
        "status": "ok",
        "data": {
            "sent": False,
            "message": "Lob integration pending. Download and mail the letter yourself via USPS Certified Mail.",
            "certified_mail_guide": debt_fighter.CERTIFIED_MAIL_GUIDE,
        },
    }


@router.get("/charity-care/hospital-search")
async def search_hospitals_charity(request: Request):
    """Search hospitals by name for charity care info."""
    q = (request.query_params.get("q") or "").strip()
    state = (request.query_params.get("state") or "").strip()
    if len(q) < 2:
        return {"status": "ok", "data": []}

    with get_db() as db:
        results = debt_fighter.search_hospitals_for_charity(db, q, state)
    return {"status": "ok", "data": results}


@router.get("/charity-care/hospital/{facility_id}")
async def get_hospital_charity_detail(facility_id: str):
    """Get detailed charity care info for a specific hospital."""
    with get_db() as db:
        result = debt_fighter.get_hospital_charity_detail(db, facility_id)
    if not result:
        raise HTTPException(404, "Hospital not found")
    return {"status": "ok", "data": result}


@router.post("/charity-care/check")
async def check_charity_care(request: Request):
    """Check charity care eligibility based on income and household size."""
    _debt_rate_check(request)
    body = await request.json()

    try:
        income = float(body.get("income", 0))
        household_size = int(body.get("household_size", 1))
    except (ValueError, TypeError):
        raise HTTPException(400, "income must be a number, household_size must be an integer")

    if income <= 0:
        raise HTTPException(400, "income must be positive")
    if household_size < 1 or household_size > 20:
        raise HTTPException(400, "household_size must be between 1 and 20")

    result = debt_fighter.check_charity_care(income, household_size)
    log_audit(action="charity_care_check", resource_type="debt_tool",
              resource_id="eligibility",
              metadata={"fpl_pct": result["fpl_percentage"], "eligibility": result["eligibility"]})
    return {"status": "ok", "data": result}


@router.post("/charity-care/application")
async def generate_charity_application(request: Request):
    """Generate a charity care application cover letter."""
    _debt_rate_check(request)
    body = await request.json()

    required = ["user_name", "user_address", "hospital_name", "hospital_address",
                "account_number", "bill_amount", "income", "household_size"]
    missing = [f for f in required if not body.get(f)]
    if missing:
        raise HTTPException(400, f"Missing required fields: {', '.join(missing)}")

    try:
        income = float(body["income"])
        household_size = int(body["household_size"])
        result = debt_fighter.generate_charity_care_letter(
            user_name=str(body["user_name"]).strip(),
            user_address=str(body["user_address"]).strip(),
            hospital_name=str(body["hospital_name"]).strip(),
            hospital_address=str(body["hospital_address"]).strip(),
            account_number=str(body["account_number"]).strip(),
            bill_amount=str(body["bill_amount"]).strip(),
            income=income,
            household_size=household_size,
            date_of_service=(body.get("date_of_service") or "").strip(),
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc))

    user_email = (body.get("email") or "").strip()
    with get_db() as db:
        cursor = db.execute(
            "INSERT INTO debt_letters "
            "(letter_type, user_email, user_name, user_address, collector_name, collector_address, account_number, amount, letter_text) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ("charity_care_application", user_email or None, result["user_name"],
             str(body["user_address"]).strip(), result["hospital_name"],
             str(body["hospital_address"]).strip(),
             result["account_number"], result["bill_amount"], result["letter_text"]),
        )
        debt_letter_id = cursor.lastrowid

    result["debt_letter_id"] = debt_letter_id
    result["certified_mail_price_cents"] = config.CHARITY_CARE_APP_PRICE_CENTS

    log_audit(action="generate_charity_letter", resource_type="debt_letter",
              resource_id=result["account_number"],
              metadata={"letter_type": "charity_care", "hospital": result["hospital_name"]})
    return {"status": "ok", "data": result}


@router.post("/collection-notice/checkout")
async def collection_notice_checkout(request: Request):
    """Create Stripe checkout session to send an FDCPA letter via certified mail ($19)."""
    _debt_rate_check(request)
    body = await request.json()
    debt_letter_id = body.get("debt_letter_id")
    email = (body.get("email") or "").strip()

    if not debt_letter_id:
        raise HTTPException(400, "debt_letter_id is required")
    if not email or "@" not in email:
        raise HTTPException(400, "A valid email is required for delivery confirmation")
    if not config.STRIPE_SECRET_KEY:
        raise HTTPException(503, "Payment processing is not configured")

    with get_db() as db:
        row = db.execute("SELECT id, status, letter_type FROM debt_letters WHERE id = ?", (debt_letter_id,)).fetchone()
    if not row:
        raise HTTPException(404, "Letter not found")
    if row["status"] in ("sent", "delivered"):
        raise HTTPException(400, "This letter has already been sent")

    app_url = config.APP_URL.rstrip("/")
    success_url = f"{app_url}/collection-notice/send-success?session_id={{CHECKOUT_SESSION_ID}}"
    cancel_url = f"{app_url}/collection-notice"

    params = {
        "mode": "payment",
        "customer_email": email,
        "line_items[0][price_data][currency]": "usd",
        "line_items[0][price_data][unit_amount]": str(config.FDCPA_LETTER_PRICE_CENTS),
        "line_items[0][price_data][product_data][name]": "FDCPA Certified Mail — BillKarma",
        "line_items[0][price_data][product_data][description]": (
            "Your letter is printed and mailed via USPS Certified Mail with tracking."
        ),
        "line_items[0][quantity]": "1",
        "metadata[debt_letter_id]": str(debt_letter_id),
        "metadata[payment_purpose]": "debt_letter",
        "success_url": success_url,
        "cancel_url": cancel_url,
    }

    try:
        session = payment_module._stripe_post("checkout/sessions", params)
    except RuntimeError as exc:
        log.error("Stripe checkout error: %s", exc)
        raise HTTPException(500, "Payment session could not be created")

    with get_db() as db:
        db.execute(
            "UPDATE debt_letters SET user_email = ?, stripe_payment_id = ? WHERE id = ?",
            (email, session["id"], debt_letter_id),
        )

    log_audit(action="debt_letter_checkout", resource_type="debt_letter",
              resource_id=str(debt_letter_id), metadata={"session": session["id"]})
    return {"status": "ok", "data": {"checkout_url": session["url"], "session_id": session["id"]}}


@router.get("/collection-notice/status-by-session")
async def get_debt_letter_status_by_session(session_id: str):
    """Look up delivery status for a debt letter by Stripe session ID."""
    with get_db() as db:
        row = db.execute(
            "SELECT id, status, lob_id, tracking_number, sent_at, letter_type FROM debt_letters WHERE stripe_payment_id = ?",
            (session_id,),
        ).fetchone()
    if not row:
        return {"status": "ok", "data": {"status": "pending"}}

    tracking_url = ""
    if row["tracking_number"]:
        tracking_url = f"https://tools.usps.com/go/TrackConfirmAction?tLabels={row['tracking_number']}"

    return {
        "status": "ok",
        "data": {
            "debt_letter_id": row["id"],
            "status": row["status"],
            "tracking_number": row["tracking_number"],
            "tracking_url": tracking_url,
            "sent_at": row["sent_at"],
        },
    }


@router.get("/collection-notice/status/{debt_letter_id}")
async def get_debt_letter_status(debt_letter_id: int):
    """Return delivery status for a sent debt letter."""
    with get_db() as db:
        row = db.execute(
            "SELECT id, status, lob_id, tracking_number, sent_at, letter_type FROM debt_letters WHERE id = ?",
            (debt_letter_id,),
        ).fetchone()
    if not row:
        raise HTTPException(404, "Letter not found")

    tracking_url = ""
    if row["tracking_number"]:
        tracking_url = f"https://tools.usps.com/go/TrackConfirmAction?tLabels={row['tracking_number']}"

    return {
        "status": "ok",
        "data": {
            "debt_letter_id": row["id"],
            "status": row["status"],
            "lob_id": row["lob_id"],
            "tracking_number": row["tracking_number"],
            "tracking_url": tracking_url,
            "sent_at": row["sent_at"],
            "letter_type": row["letter_type"],
        },
    }


@router.post("/charity-care/checkout")
async def charity_care_checkout(request: Request):
    """Create Stripe checkout session to send a charity care packet via certified mail ($9)."""
    _debt_rate_check(request)
    body = await request.json()
    debt_letter_id = body.get("debt_letter_id")
    email = (body.get("email") or "").strip()

    if not debt_letter_id:
        raise HTTPException(400, "debt_letter_id is required")
    if not email or "@" not in email:
        raise HTTPException(400, "A valid email is required for delivery confirmation")
    if not config.STRIPE_SECRET_KEY:
        raise HTTPException(503, "Payment processing is not configured")

    with get_db() as db:
        row = db.execute("SELECT id, status FROM debt_letters WHERE id = ?", (debt_letter_id,)).fetchone()
    if not row:
        raise HTTPException(404, "Letter not found")
    if row["status"] in ("sent", "delivered"):
        raise HTTPException(400, "This letter has already been sent")

    app_url = config.APP_URL.rstrip("/")
    success_url = f"{app_url}/charity-care/send-success?session_id={{CHECKOUT_SESSION_ID}}"
    cancel_url = f"{app_url}/charity-care/apply"

    params = {
        "mode": "payment",
        "customer_email": email,
        "line_items[0][price_data][currency]": "usd",
        "line_items[0][price_data][unit_amount]": str(config.CHARITY_CARE_APP_PRICE_CENTS),
        "line_items[0][price_data][product_data][name]": "Charity Care Application — BillKarma",
        "line_items[0][price_data][product_data][description]": (
            "Your cover letter is printed and mailed via USPS Certified Mail with tracking."
        ),
        "line_items[0][quantity]": "1",
        "metadata[debt_letter_id]": str(debt_letter_id),
        "metadata[payment_purpose]": "debt_letter",
        "success_url": success_url,
        "cancel_url": cancel_url,
    }

    try:
        session = payment_module._stripe_post("checkout/sessions", params)
    except RuntimeError as exc:
        log.error("Stripe checkout error: %s", exc)
        raise HTTPException(500, "Payment session could not be created")

    with get_db() as db:
        db.execute(
            "UPDATE debt_letters SET user_email = ?, stripe_payment_id = ? WHERE id = ?",
            (email, session["id"], debt_letter_id),
        )

    log_audit(action="charity_care_checkout", resource_type="debt_letter",
              resource_id=str(debt_letter_id), metadata={"session": session["id"]})
    return {"status": "ok", "data": {"checkout_url": session["url"], "session_id": session["id"]}}


@router.post("/settlement/generate")
async def generate_settlement(request: Request):
    """Generate a settlement offer letter."""
    _debt_rate_check(request)
    body = await request.json()

    required = ["user_name", "user_address", "collector_name", "collector_address",
                "account_number", "original_amount", "offer_amount"]
    missing = [f for f in required if not (body.get(f) or "").strip()]
    if missing:
        raise HTTPException(400, f"Missing required fields: {', '.join(missing)}")

    try:
        result = debt_fighter.generate_settlement_letter(
            user_name=body["user_name"].strip(),
            user_address=body["user_address"].strip(),
            collector_name=body["collector_name"].strip(),
            collector_address=body["collector_address"].strip(),
            account_number=body["account_number"].strip(),
            original_amount=body["original_amount"].strip(),
            offer_amount=body["offer_amount"].strip(),
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc))

    with get_db() as db:
        db.execute(
            "INSERT INTO debt_letters (letter_type, user_name, collector_name, account_number, amount, letter_text) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            ("settlement_offer", result["user_name"], result["collector_name"],
             result["account_number"], result["original_amount"], result["letter_text"]),
        )

    log_audit(action="generate_settlement_letter", resource_type="debt_letter",
              resource_id=result["account_number"],
              metadata={"letter_type": "settlement", "collector": result["collector_name"]})
    return {"status": "ok", "data": result}
