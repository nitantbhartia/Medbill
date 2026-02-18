import json
import logging
from datetime import datetime

from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Request
from fastapi.responses import JSONResponse

import config
import scanner
import analyzer
import negotiation
from db import get_db
from dispute_packet import generate_dispute_packet
from appeal_playbooks import generate_appeal_playbook
from provider_intelligence import get_provider_intelligence
from compliance import (
    scrub_extracted_data,
    record_consent,
    log_audit,
    export_bill_data,
    delete_bill_data,
    purge_old_data,
)
from ocr_benchmark import run_manifest

log = logging.getLogger(__name__)
router = APIRouter(prefix="/api")
CLAIM_TRANSITIONS = {
    "drafted": {"sent", "denied"},
    "sent": {"acknowledged", "denied"},
    "acknowledged": {"resolved", "denied"},
    "resolved": set(),
    "denied": set(),
}


@router.post("/scan")
async def scan_bill(
    images: list[UploadFile] = File(...),
    eob_images: list[UploadFile] | None = File(None),
    zip_code: str = Form("00000"),
    email: str = Form(""),
):
    """Scan one or more bill images, extract line items, and analyze."""
    if not images:
        raise HTTPException(400, "No files uploaded")

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

    return {
        "status": "ok",
        "data": {
            "bill_id": bill_id,
            "extracted": extracted,
            "analysis": analysis,
        },
    }


@router.post("/analyze/{bill_id}")
async def analyze_confirmed(bill_id: int, payload: dict):
    """Re-analyze a bill after user confirms/edits line items."""
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
async def get_results(bill_id: int):
    """Get analysis results for a scanned bill."""
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


@router.get("/dispute-packet/{bill_id}")
async def get_dispute_packet(bill_id: int):
    """Generate a full dispute packet."""
    packet = generate_dispute_packet(bill_id)
    if not packet:
        raise HTTPException(404, "Bill not found")
    log_audit(action="generate_dispute_packet", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id)
    return {"status": "ok", "data": packet}


@router.post("/dispute-letter/{bill_id}")
async def get_dispute_letter(bill_id: int, payload: dict):
    """
    Generate a focused dispute letter from selected findings.
    """
    selected_ids = payload.get("finding_ids", [])
    requestor_name = payload.get("requestor_name", "Patient")
    if not isinstance(selected_ids, list):
        raise HTTPException(400, "finding_ids must be an array")

    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            raise HTTPException(404, "Bill not found")

        if selected_ids:
            placeholders = ",".join(["?"] * len(selected_ids))
            rows = db.execute(
                f"SELECT * FROM findings WHERE bill_id = ? AND id IN ({placeholders}) ORDER BY id",
                [bill_id, *selected_ids],
            ).fetchall()
        else:
            rows = db.execute("SELECT * FROM findings WHERE bill_id = ? ORDER BY id", (bill_id,)).fetchall()

    if not rows:
        raise HTTPException(400, "No findings available for dispute letter")

    bill_dict = dict(bill)
    bullets = []
    total = 0.0
    for row in rows:
        detail = json.loads(row["details"] or "{}")
        li = detail.get("line_item") or {}
        cpt = li.get("cpt_code") or "N/A"
        evidence = detail.get("evidence") or {}
        source = evidence.get("source", "rule_engine")
        est = float(detail.get("estimated_patient_savings") or row["potential_savings"] or 0.0)
        total += est
        bullets.append(
            f"- {row['message']} (CPT: {cpt}, est. savings: ${est:,.2f})"
        )

    letter = (
        f"Date: {datetime.utcnow().strftime('%Y-%m-%d')}\n\n"
        f"To: Billing Department, {bill_dict.get('provider_name') or 'Provider'}\n"
        f"Re: Account review request for bill #{bill_id}\n\n"
        f"Hello,\n\n"
        f"I am requesting an item-level review and correction of charges on my bill dated "
        f"{bill_dict.get('bill_date') or 'N/A'}. I found the following issues in my audit:\n\n"
        f"{chr(10).join(bullets)}\n\n"
        f"Please send a corrected itemized statement and any rebill submissions to my insurer where applicable. "
        f"The estimated patient-impact amount under review is ${total:,.2f}.\n\n"
        f"Sincerely,\n"
        f"{requestor_name}\n"
    )
    log_audit(
        action="generate_dispute_letter",
        resource_type="bill",
        resource_id=str(bill_id),
        bill_id=bill_id,
        metadata={"finding_count": len(rows), "estimated_patient_impact": round(total, 2)},
    )

    return {
        "status": "ok",
        "data": {
            "bill_id": bill_id,
            "finding_count": len(rows),
            "estimated_patient_impact": round(total, 2),
            "letter": letter,
        },
    }


@router.get("/appeal-playbook/{bill_id}")
async def get_appeal_playbook(bill_id: int):
    """Generate issue-specific appeal steps."""
    playbook = generate_appeal_playbook(bill_id)
    if not playbook:
        raise HTTPException(404, "Bill not found")
    return {"status": "ok", "data": playbook}


@router.get("/phone-script/{bill_id}")
async def get_phone_script(bill_id: int):
    """Generate a phone script for disputing a bill."""
    script = negotiation.generate_phone_script(bill_id)
    if not script:
        raise HTTPException(404, "Bill not found or no findings")
    return {"status": "ok", "data": {"script": script}}


@router.get("/message-script/{bill_id}")
async def get_message_script(bill_id: int):
    """Generate a written message script for portal/text disputes."""
    script = negotiation.generate_message_script(bill_id)
    if not script:
        raise HTTPException(404, "Bill not found or no findings")
    return {"status": "ok", "data": {"script": script}}


# --- Negotiation endpoints ---


@router.post("/negotiate/start")
async def start_negotiation(
    bill_id: int = Form(...),
    user_id: int = Form(...),
    account_number: str = Form(...),
    hospital_email: str = Form(""),
):
    """Create a new negotiation for a bill."""
    neg_id = negotiation.create_negotiation(bill_id, user_id, account_number, hospital_email)
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


@router.post("/dispute-outcome")
async def record_dispute_outcome(
    bill_id: int = Form(...),
    user_id: int = Form(...),
    called_billing: bool = Form(False),
    outcome: str = Form("pending"),
    final_patient_owes: float = Form(0),
    notes: str = Form(""),
    share_publicly: bool = Form(False),
):
    """Record what happened after the user disputed their bill."""
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

    return {"status": "ok", "data": {"actual_savings": actual_savings}}


@router.post("/claims")
async def create_claim(
    bill_id: int = Form(...),
    user_id: int = Form(None),
    channel: str = Form("provider_billing"),
    note: str = Form(""),
):
    """Create a new claim workflow record for a bill."""
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
async def list_claims(bill_id: int):
    """List claim workflow records for a bill."""
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
async def update_claim_status(claim_id: int, status: str = Form(...), note: str = Form("")):
    """Transition a claim status and append an audit event."""
    target = (status or "").strip().lower()
    if target not in CLAIM_TRANSITIONS:
        raise HTTPException(400, f"Invalid status '{status}'")

    with get_db() as db:
        claim = db.execute("SELECT * FROM dispute_claims WHERE id = ?", (claim_id,)).fetchone()
        if not claim:
            raise HTTPException(404, "Claim not found")

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


@router.get("/ops/ocr-benchmark")
async def ocr_benchmark():
    """Run OCR benchmark over local fixture manifest."""
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
async def export_bill(bill_id: int):
    payload = export_bill_data(bill_id)
    if not payload:
        raise HTTPException(404, "Bill not found")
    log_audit(action="export_bill", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id)
    return {"status": "ok", "data": payload}


@router.delete("/bills/{bill_id}")
async def delete_bill(bill_id: int):
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
async def purge_old(days: int = Form(365)):
    deleted = purge_old_data(days=days)
    log_audit(action="purge_old_data", resource_type="compliance", resource_id=str(days), metadata={"deleted": deleted})
    return {"status": "ok", "data": {"deleted_bills": deleted, "days": days}}


@router.post("/confirm-items")
async def confirm_items(
    bill_id: int = Form(...),
    confirmed_items: str = Form(...),
):
    """User confirms/edits extracted line items before analysis."""
    items = json.loads(confirmed_items)

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
