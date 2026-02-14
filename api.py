import json
import logging

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse

import scanner
import analyzer
import negotiation
from db import get_db

log = logging.getLogger(__name__)
router = APIRouter(prefix="/api")


@router.post("/scan")
async def scan_bill(
    images: list[UploadFile] = File(...),
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
            extracted = scanner.process_bill_image(image_bytes, mime_type)
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
        analysis = analyzer.analyze_bill(extracted, zip_code)
        bill_id = analyzer.save_bill_and_findings(user_id, extracted, analysis, zip_code)
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

        # Update line items with user-confirmed data
        db.execute("DELETE FROM line_items WHERE bill_id = ?", (bill_id,))
        db.execute("DELETE FROM findings WHERE bill_id = ?", (bill_id,))

        items = payload.get("line_items", [])
        for item in items:
            db.execute(
                "INSERT INTO line_items (bill_id, cpt_code, description, "
                "charged_amount, quantity, extraction_confidence) "
                "VALUES (?, ?, ?, ?, ?, 'high')",
                (
                    bill_id,
                    item.get("cpt_code"),
                    item.get("description"),
                    item.get("billed_amount"),
                    item.get("quantity", 1),
                ),
            )

    # Re-analyze with confirmed items
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
                "charged_amount": item.get("billed_amount"),
                "quantity": item.get("quantity", 1),
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
                "INSERT INTO findings (bill_id, finding_type, severity, "
                "potential_savings, message, details) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    bill_id,
                    finding["type"],
                    finding["severity"],
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
    return {"status": "ok", "data": results}


@router.get("/stats")
async def get_stats():
    """Get aggregate stats for the live counter."""
    stats = analyzer.get_stats()
    return {"status": "ok", "data": stats}


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
