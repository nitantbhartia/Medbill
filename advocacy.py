"""Advocacy Workspace — case management, document processing, analysis, and letter generation.

This module wraps existing scanner, analyzer, and letter generation capabilities
in a case management layer for advocacy organizations.
"""

import json
import logging
import secrets
from datetime import date, datetime

from fastapi import HTTPException

import analyzer
import scanner
from compliance import scrub_extracted_data
from db import get_db
from dispute_workflow import build_dispute_letter, build_appeal_letter
from debt_fighter import generate_fdcpa_letter, generate_charity_care_letter, LEGAL_DISCLAIMER

log = logging.getLogger(__name__)

# Status auto-advance rules (system-driven transitions)
AUTO_ADVANCE = {
    "new": "docs_uploaded",
    "docs_uploaded": "analyzed",
    "analyzed": "letter_generated",
}

VALID_STATUSES = {
    "new", "docs_uploaded", "analyzed", "letter_generated",
    "sent", "awaiting_response", "resolved", "closed",
}

VALID_DOC_TYPES = {"hospital_bill", "eob", "denial_letter", "itemized_bill", "other"}

LETTER_TYPES = {"insurance_appeal", "hospital_dispute", "charity_care", "debt_validation"}

VALID_OUTCOMES = {"resolved_reduced", "resolved_forgiven", "resolved_denied", "unknown"}

VALID_ROLES = {"admin", "advocate", "viewer"}


# ── Activity Timeline ────────────────────────────────────────────────────────

def log_activity(case_id: int, user_id: int | None, action: str,
                 detail: str = None, metadata: dict = None, db=None) -> None:
    """Log a case activity event. Accepts an optional db connection for transactional logging."""
    meta_json = json.dumps(metadata) if metadata else None

    def _insert(conn):
        conn.execute(
            "INSERT INTO case_activity (case_id, user_id, action, detail, metadata) VALUES (?, ?, ?, ?, ?)",
            (case_id, user_id, action, detail, meta_json),
        )

    if db:
        _insert(db)
    else:
        with get_db() as conn:
            _insert(conn)


def get_activity(case_id: int, org_id: int, limit: int = 100) -> list[dict]:
    """Get activity timeline for a case."""
    _ = get_case(case_id, org_id)  # verify access
    with get_db() as db:
        rows = db.execute(
            """
            SELECT a.*, u.name as user_name
            FROM case_activity a
            LEFT JOIN users u ON a.user_id = u.id
            WHERE a.case_id = ?
            ORDER BY a.created_at DESC
            LIMIT ?
            """,
            (case_id, limit),
        ).fetchall()
    return [dict(r) for r in rows]


# ── Case CRUD ────────────────────────────────────────────────────────────────

def create_case(org_id: int, user_id: int, patient_label: str, **kwargs) -> dict:
    """Create a new advocacy case."""
    patient_label = (patient_label or "").strip()
    if not patient_label:
        raise HTTPException(400, "Patient label is required")

    hospital_name = (kwargs.get("hospital_name") or "").strip() or None
    dos = (kwargs.get("date_of_service") or "").strip() or None
    title = f"{patient_label} - {hospital_name or 'Unknown'} - {dos or 'No date'}"

    with get_db() as db:
        cursor = db.execute(
            """
            INSERT INTO advocacy_cases
                (org_id, created_by, patient_label, title, hospital_name,
                 insurance_carrier, date_of_service, bill_amount, notes, tags,
                 patient_consent, assigned_to)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                org_id,
                user_id,
                patient_label,
                title,
                hospital_name,
                (kwargs.get("insurance_carrier") or "").strip() or None,
                dos,
                kwargs.get("bill_amount"),
                (kwargs.get("notes") or "").strip() or None,
                (kwargs.get("tags") or "").strip() or None,
                1 if kwargs.get("patient_consent") else 0,
                kwargs.get("assigned_to") or user_id,
            ),
        )
        case_id = cursor.lastrowid
        log_activity(case_id, user_id, "case_created", f"Case created for {patient_label}", db=db)

    return get_case(case_id, org_id)


def get_case(case_id: int, org_id: int) -> dict:
    """Fetch a single case. Raises 404 if not found or wrong org."""
    with get_db() as db:
        row = db.execute(
            """
            SELECT c.*, u.name as created_by_name, a.name as assigned_to_name
            FROM advocacy_cases c
            LEFT JOIN users u ON c.created_by = u.id
            LEFT JOIN users a ON c.assigned_to = a.id
            WHERE c.id = ? AND c.org_id = ?
            """,
            (case_id, org_id),
        ).fetchone()

    if not row:
        raise HTTPException(404, "Case not found")
    return dict(row)


def list_cases(org_id: int, status: str = None, assigned_to: int = None,
               search: str = None, limit: int = 100, offset: int = 0) -> dict:
    """List cases for an org with optional filters."""
    conditions = ["c.org_id = ?"]
    params: list = [org_id]

    if status:
        conditions.append("c.status = ?")
        params.append(status)
    if assigned_to:
        conditions.append("c.assigned_to = ?")
        params.append(assigned_to)
    if search:
        conditions.append("(c.patient_label LIKE ? OR c.hospital_name LIKE ? OR c.tags LIKE ?)")
        term = f"%{search}%"
        params.extend([term, term, term])

    where = " AND ".join(conditions)

    with get_db() as db:
        count = db.execute(
            f"SELECT COUNT(*) as cnt FROM advocacy_cases c WHERE {where}", params
        ).fetchone()["cnt"]

        rows = db.execute(
            f"""
            SELECT c.*, u.name as assigned_to_name
            FROM advocacy_cases c
            LEFT JOIN users u ON c.assigned_to = u.id
            WHERE {where}
            ORDER BY c.updated_at DESC
            LIMIT ? OFFSET ?
            """,
            params + [limit, offset],
        ).fetchall()

    return {"cases": [dict(r) for r in rows], "total": count}


def update_case(case_id: int, org_id: int, **kwargs) -> dict:
    """Update case fields. Only updates provided fields."""
    allowed = {
        "patient_label", "hospital_name", "insurance_carrier", "date_of_service",
        "bill_amount", "notes", "tags", "assigned_to", "status", "outcome",
        "outcome_amount", "patient_consent",
    }
    updates = {k: v for k, v in kwargs.items() if k in allowed and v is not None}
    if not updates:
        raise HTTPException(400, "No valid fields to update")

    if "status" in updates and updates["status"] not in VALID_STATUSES:
        raise HTTPException(400, f"Invalid status: {updates['status']}")
    if "outcome" in updates and updates["outcome"] not in VALID_OUTCOMES:
        raise HTTPException(400, f"Invalid outcome: {updates['outcome']}")

    set_parts = [f"{k} = ?" for k in updates]
    set_parts.append("updated_at = CURRENT_TIMESTAMP")
    values = list(updates.values())

    with get_db() as db:
        result = db.execute(
            f"UPDATE advocacy_cases SET {', '.join(set_parts)} WHERE id = ? AND org_id = ?",
            values + [case_id, org_id],
        )
        if result.rowcount == 0:
            raise HTTPException(404, "Case not found")

        fields_str = ", ".join(updates.keys())
        log_activity(case_id, None, "case_updated", f"Updated: {fields_str}", metadata=updates, db=db)

    return get_case(case_id, org_id)


def _auto_advance_status(db, case_id: int, trigger: str) -> None:
    """Auto-advance case status if current status matches the trigger's prerequisite."""
    row = db.execute("SELECT status FROM advocacy_cases WHERE id = ?", (case_id,)).fetchone()
    if not row:
        return
    current = row["status"]
    if current in AUTO_ADVANCE and AUTO_ADVANCE[current] == trigger:
        # Only advance to the expected next status
        pass
    elif trigger in AUTO_ADVANCE.values():
        # Current status should be the key that maps to this trigger
        for from_status, to_status in AUTO_ADVANCE.items():
            if to_status == trigger and current == from_status:
                db.execute(
                    "UPDATE advocacy_cases SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
                    (trigger, case_id),
                )
                return
    # Direct advancement: if current status maps to this trigger value
    if AUTO_ADVANCE.get(current) == trigger:
        db.execute(
            "UPDATE advocacy_cases SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            (trigger, case_id),
        )


# ── Document Management ──────────────────────────────────────────────────────

def upload_document(case_id: int, org_id: int, filename: str, file_data: bytes,
                    mime_type: str, doc_type: str = "other") -> dict:
    """Upload a document to a case and trigger extraction."""
    if doc_type not in VALID_DOC_TYPES:
        doc_type = "other"

    # Verify case belongs to org
    with get_db() as db:
        case = db.execute(
            "SELECT id, status FROM advocacy_cases WHERE id = ? AND org_id = ?",
            (case_id, org_id),
        ).fetchone()
        if not case:
            raise HTTPException(404, "Case not found")

        cursor = db.execute(
            """
            INSERT INTO case_documents (case_id, doc_type, filename, file_data, mime_type, file_size_bytes)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (case_id, doc_type, filename, file_data, mime_type, len(file_data)),
        )
        doc_id = cursor.lastrowid

        # Auto-advance to docs_uploaded
        _auto_advance_status(db, case_id, "docs_uploaded")
        log_activity(case_id, None, "document_uploaded", f"Uploaded {filename} ({doc_type})", db=db)

    # Run extraction
    extraction = _extract_document(doc_id, file_data, mime_type)
    return {"id": doc_id, "filename": filename, "doc_type": doc_type, "extraction": extraction}


def _extract_document(doc_id: int, file_data: bytes, mime_type: str) -> dict:
    """Run OCR extraction on a document and store results."""
    try:
        extracted = scanner.process_bill_with_verification(file_data, mime_type)
        extracted = scrub_extracted_data(extracted)
        status = "extracted"
    except Exception as e:
        log.warning("Extraction failed for doc %d: %s", doc_id, e)
        extracted = {"error": str(e)}
        status = "failed"

    with get_db() as db:
        db.execute(
            "UPDATE case_documents SET extraction_status = ?, extracted_json = ? WHERE id = ?",
            (status, json.dumps(extracted), doc_id),
        )

    return {"status": status, "data": extracted if status == "extracted" else None}


def get_case_documents(case_id: int, org_id: int) -> list[dict]:
    """List documents for a case (without file_data blob)."""
    with get_db() as db:
        case = db.execute(
            "SELECT id FROM advocacy_cases WHERE id = ? AND org_id = ?",
            (case_id, org_id),
        ).fetchone()
        if not case:
            raise HTTPException(404, "Case not found")

        rows = db.execute(
            """
            SELECT id, case_id, doc_type, filename, mime_type, file_size_bytes,
                   extraction_status, extracted_json, created_at
            FROM case_documents WHERE case_id = ?
            ORDER BY created_at
            """,
            (case_id,),
        ).fetchall()
    return [dict(r) for r in rows]


def get_document_file(doc_id: int, case_id: int, org_id: int) -> dict:
    """Fetch document file data for download/preview."""
    with get_db() as db:
        row = db.execute(
            """
            SELECT d.file_data, d.filename, d.mime_type
            FROM case_documents d
            JOIN advocacy_cases c ON d.case_id = c.id
            WHERE d.id = ? AND d.case_id = ? AND c.org_id = ?
            """,
            (doc_id, case_id, org_id),
        ).fetchone()
    if not row:
        raise HTTPException(404, "Document not found")
    return dict(row)


def delete_document(doc_id: int, case_id: int, org_id: int) -> None:
    """Delete a document from a case."""
    with get_db() as db:
        result = db.execute(
            """
            DELETE FROM case_documents WHERE id = ? AND case_id = ?
            AND case_id IN (SELECT id FROM advocacy_cases WHERE org_id = ?)
            """,
            (doc_id, case_id, org_id),
        )
        if result.rowcount == 0:
            raise HTTPException(404, "Document not found")
        log_activity(case_id, None, "document_deleted", f"Deleted document {doc_id}", db=db)


# ── Overrides ────────────────────────────────────────────────────────────────

def set_override(case_id: int, org_id: int, user_id: int, field_name: str, field_value: str) -> dict:
    """Set an advocate override for a case field."""
    with get_db() as db:
        case = db.execute(
            "SELECT id FROM advocacy_cases WHERE id = ? AND org_id = ?",
            (case_id, org_id),
        ).fetchone()
        if not case:
            raise HTTPException(404, "Case not found")

        db.execute(
            """
            INSERT INTO case_overrides (case_id, field_name, field_value, set_by)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(case_id, field_name) DO UPDATE SET field_value = ?, set_by = ?
            """,
            (case_id, field_name, field_value, user_id, field_value, user_id),
        )
    return {"case_id": case_id, "field_name": field_name, "field_value": field_value}


def get_overrides(case_id: int) -> dict:
    """Get all overrides for a case as a dict."""
    with get_db() as db:
        rows = db.execute(
            "SELECT field_name, field_value FROM case_overrides WHERE case_id = ?",
            (case_id,),
        ).fetchall()
    return {r["field_name"]: r["field_value"] for r in rows}


# ── Analysis ─────────────────────────────────────────────────────────────────

def _build_merged_extraction(case_id: int) -> dict | None:
    """Merge all document extractions for a case, applying overrides."""
    with get_db() as db:
        docs = db.execute(
            """
            SELECT doc_type, extracted_json FROM case_documents
            WHERE case_id = ? AND extraction_status = 'extracted'
            ORDER BY created_at
            """,
            (case_id,),
        ).fetchall()

    if not docs:
        return None

    # Start with the first bill-type document, or the first doc
    merged = {}
    eob_data = None
    for doc in docs:
        data = json.loads(doc["extracted_json"] or "{}")
        if doc["doc_type"] in ("hospital_bill", "itemized_bill") and not merged.get("line_items"):
            merged = data
        elif doc["doc_type"] == "eob":
            eob_data = data
        elif not merged.get("line_items"):
            merged = data

    # Merge EOB if present
    if eob_data:
        merged = analyzer.merge_eob_into_extracted(merged, eob_data)

    # Apply overrides
    overrides = get_overrides(case_id)
    field_map = {
        "total_charged": "total_charged",
        "total_patient_owes": "total_patient_owes",
        "provider_name": "provider_name",
        "bill_date": "bill_date",
        "date_of_service": "bill_date",
        "account_number": "account_number",
        "claim_number": "claim_number",
    }
    for override_key, extract_key in field_map.items():
        if override_key in overrides:
            val = overrides[override_key]
            if extract_key in ("total_charged", "total_patient_owes"):
                try:
                    val = float(val)
                except ValueError:
                    continue
            merged[extract_key] = val

    return merged


def run_analysis(case_id: int, org_id: int) -> dict:
    """Run the full analysis pipeline on a case's documents."""
    case = get_case(case_id, org_id)

    merged = _build_merged_extraction(case_id)
    if not merged or not merged.get("line_items"):
        raise HTTPException(400, "No extractable data found. Upload documents or enter fields manually.")

    zip_code = "00000"
    address = merged.get("provider_address", "")
    if address:
        import re
        zip_match = re.search(r"\b(\d{5})\b", address)
        if zip_match:
            zip_code = zip_match.group(1)

    analysis = analyzer.analyze_bill(merged, zip_code)

    # Save bill + findings if not already saved
    if not case.get("bill_id"):
        bill_id = analyzer.save_bill_and_findings(None, merged, analysis, zip_code)
        with get_db() as db:
            db.execute(
                """
                UPDATE advocacy_cases
                SET bill_id = ?, bill_amount = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
                """,
                (bill_id, merged.get("total_charged"), case_id),
            )
            _auto_advance_status(db, case_id, "analyzed")
    else:
        # Re-analysis: update existing bill
        bill_id = case["bill_id"]
        with get_db() as db:
            db.execute("DELETE FROM findings WHERE bill_id = ?", (bill_id,))
            db.execute("DELETE FROM line_items WHERE bill_id = ?", (bill_id,))

            # Re-save line items and findings
            from validators.pricing import get_medicare_rate
            for item in merged.get("line_items", []):
                medicare_rate = get_medicare_rate(item.get("cpt_code", "")) if item.get("cpt_code") else None
                markup = (
                    round(item["charged_amount"] / medicare_rate, 2)
                    if medicare_rate and item.get("charged_amount")
                    else None
                )
                db.execute(
                    """INSERT INTO line_items (bill_id, date_of_service, cpt_code, description,
                       quantity, charged_amount, insurance_paid, insurance_adjustment,
                       patient_responsibility, medicare_rate, markup_multiple, extraction_confidence)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (bill_id, item.get("date_of_service"), item.get("cpt_code"),
                     item.get("description"), item.get("quantity", 1),
                     item.get("charged_amount"), item.get("insurance_paid"),
                     item.get("insurance_adjustment"), item.get("patient_responsibility"),
                     medicare_rate, markup, item.get("confidence", "high")),
                )

            for finding in analysis.get("findings", []):
                db.execute(
                    """INSERT INTO findings (bill_id, finding_type, rule_id, severity, confidence,
                       evidence_source, evidence_json, potential_savings, message, details)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (bill_id, finding["type"], finding.get("rule_id"),
                     finding["severity"], finding.get("confidence"),
                     (finding.get("evidence") or {}).get("source"),
                     json.dumps(finding.get("evidence") or {}),
                     finding.get("potential_savings", 0),
                     finding["message"], json.dumps(finding)),
                )

            db.execute(
                "UPDATE bills SET total_findings = ?, total_potential_savings = ? WHERE id = ?",
                (analysis["total_findings"], analysis["total_potential_savings"], bill_id),
            )
            _auto_advance_status(db, case_id, "analyzed")

    log_activity(
        case_id, None, "analysis_run",
        f"Found {analysis['total_findings']} issues, ${analysis['total_potential_savings']:,.2f} potential savings",
    )

    # Build recommendations
    recommendations = _build_recommendations(analysis, merged, case)

    return {
        "status": "ok",
        "bill_id": bill_id,
        "analysis": analysis,
        "recommendations": recommendations,
        "extracted": {
            "provider_name": merged.get("provider_name"),
            "total_charged": merged.get("total_charged"),
            "total_patient_owes": merged.get("total_patient_owes"),
            "line_items_count": len(merged.get("line_items", [])),
        },
    }


def get_case_analysis(case_id: int, org_id: int) -> dict | None:
    """Fetch existing analysis results for a case."""
    case = get_case(case_id, org_id)
    if not case.get("bill_id"):
        return None

    results = analyzer.get_bill_results(case["bill_id"])
    if not results:
        return None

    merged = _build_merged_extraction(case_id)
    recommendations = _build_recommendations(
        {"findings": results.get("findings", []),
         "total_findings": len(results.get("findings", [])),
         "total_potential_savings": results.get("total_potential_savings", 0)},
        merged or {},
        case,
    )

    return {
        "bill_id": case["bill_id"],
        "results": results,
        "recommendations": recommendations,
    }


# ── Recommendations ──────────────────────────────────────────────────────────

def _build_recommendations(analysis: dict, extracted: dict, case: dict) -> list[dict]:
    """Build deterministic recommendations based on findings.

    Each recommendation is traceable to specific findings/evidence.
    No LLM reasoning — rules map finding types to actions.
    """
    recommendations = []
    findings = analysis.get("findings", [])
    finding_types = {f.get("type") for f in findings}

    has_billing_errors = bool(
        finding_types & {"duplicate", "duplicate_charge", "unbundling", "upcoding", "price_markup", "ncci"}
    )
    has_denial = any(
        "denial" in (f.get("message") or "").lower() or "denied" in (f.get("message") or "").lower()
        for f in findings
    )
    has_high_markup = any(
        f.get("type") == "price_markup" and f.get("severity") in ("high", "medium")
        for f in findings
    )

    # Primary recommendation
    if has_denial:
        evidence = [f for f in findings if "denial" in (f.get("message") or "").lower() or "denied" in (f.get("message") or "").lower()]
        recommendations.append({
            "action": "Generate insurance appeal letter",
            "letter_type": "insurance_appeal",
            "priority": 1,
            "reason": "Denial or underpayment detected in EOB/documents.",
            "based_on": [f.get("message", "") for f in evidence[:3]],
        })

    if has_billing_errors:
        error_findings = [f for f in findings if f.get("type") in {"duplicate", "duplicate_charge", "unbundling", "upcoding", "price_markup", "ncci"}]
        total_savings = sum(f.get("potential_savings", 0) for f in error_findings)
        recommendations.append({
            "action": "Generate hospital dispute letter",
            "letter_type": "hospital_dispute",
            "priority": 1 if not has_denial else 2,
            "reason": f"Found {len(error_findings)} billing issue(s) with ${total_savings:,.2f} in potential savings.",
            "based_on": [f.get("message", "") for f in error_findings[:5]],
        })

    if has_high_markup:
        recommendations.append({
            "action": "Generate charity care request",
            "letter_type": "charity_care",
            "priority": 3,
            "reason": "High markup detected. If patient has limited income, hospital financial assistance may apply.",
            "based_on": ["Charges significantly exceed Medicare benchmark rates."],
        })

    # Debt validation if this looks like a collections case
    if case.get("tags") and "collections" in (case.get("tags") or "").lower():
        recommendations.append({
            "action": "Generate debt validation letter",
            "letter_type": "debt_validation",
            "priority": 1,
            "reason": "Case tagged as collections. Debt validation letter protects patient rights under FDCPA.",
            "based_on": ["Case metadata indicates collection activity."],
        })

    # Fallback: if no findings but bill exists
    if not recommendations and extracted.get("line_items"):
        recommendations.append({
            "action": "Request itemized bill",
            "letter_type": None,
            "priority": 2,
            "reason": "No billing issues detected, but requesting an itemized bill can reveal hidden charges.",
            "based_on": ["Standard advocacy practice for high-value bills."],
        })

    recommendations.sort(key=lambda r: r["priority"])
    return recommendations


# ── Letter Generation ────────────────────────────────────────────────────────

def generate_letter(case_id: int, org_id: int, user_id: int, letter_type: str,
                    input_fields: dict = None) -> dict:
    """Generate a letter for a case. Returns the letter content and metadata."""
    if letter_type not in LETTER_TYPES:
        raise HTTPException(400, f"Invalid letter type. Must be one of: {', '.join(LETTER_TYPES)}")

    case = get_case(case_id, org_id)
    fields = input_fields or {}

    # Build defaults from case data + extraction
    patient_name = fields.get("patient_name", case.get("patient_label", "[Patient Name]"))
    account_number = fields.get("account_number", "[Account Number]")
    hospital_name = fields.get("hospital_name", case.get("hospital_name", "[Hospital/Provider Name]"))
    dos = fields.get("date_of_service", case.get("date_of_service", "[Date of Service]"))

    # Try to get from overrides/extraction
    overrides = get_overrides(case_id)
    if "account_number" in overrides:
        account_number = overrides["account_number"]

    if case.get("bill_id"):
        with get_db() as db:
            bill = db.execute("SELECT * FROM bills WHERE id = ?", (case["bill_id"],)).fetchone()
            if bill:
                if hospital_name == "[Hospital/Provider Name]" and bill["provider_name"]:
                    hospital_name = bill["provider_name"]
                if dos == "[Date of Service]" and bill["bill_date"]:
                    dos = bill["bill_date"]

    content = None

    if letter_type == "hospital_dispute" and case.get("bill_id"):
        result = build_dispute_letter(
            case["bill_id"],
            requestor_name=patient_name,
            account_number=account_number,
        )
        if result:
            content = result["letter"]

    elif letter_type == "insurance_appeal" and case.get("bill_id"):
        result = build_appeal_letter(
            case["bill_id"],
            requestor_name=patient_name,
            policy_number=fields.get("policy_number", "[Policy Number]"),
        )
        if result:
            content = result["letter"]

    elif letter_type == "charity_care":
        income = float(fields.get("income", 0))
        household_size = int(fields.get("household_size", 1))
        bill_amount = str(case.get("bill_amount") or fields.get("bill_amount", "0"))
        result = generate_charity_care_letter(
            user_name=patient_name,
            user_address=fields.get("patient_address", "[Patient Address]"),
            hospital_name=hospital_name,
            hospital_address=fields.get("hospital_address", "[Hospital Address]"),
            account_number=account_number,
            bill_amount=bill_amount,
            income=income,
            household_size=household_size,
            date_of_service=dos,
        )
        content = result.get("letter_text")

    elif letter_type == "debt_validation":
        result = generate_fdcpa_letter(
            letter_type="debt_validation",
            user_name=patient_name,
            user_address=fields.get("patient_address", "[Patient Address]"),
            collector_name=fields.get("collector_name", "[Collector Name]"),
            collector_address=fields.get("collector_address", "[Collector Address]"),
            account_number=account_number,
            amount=str(case.get("bill_amount") or fields.get("amount", "0")),
        )
        content = result.get("letter_text")

    if not content:
        # Fallback: generate a generic letter shell
        today_str = date.today().strftime("%B %d, %Y")
        content = (
            f"{today_str}\n\n"
            f"{patient_name}\n[Patient Address]\n\n"
            f"To: {hospital_name}\n[Recipient Address]\n\n"
            f"Re: Account {account_number} — Date of Service: {dos}\n\n"
            f"Dear Billing Department,\n\n"
            f"[Letter body — please edit this draft with specific details.]\n\n"
            f"Sincerely,\n{patient_name}\n"
        )

    # Save letter
    with get_db() as db:
        cursor = db.execute(
            """
            INSERT INTO case_letters (case_id, letter_type, input_fields, content, generated_by)
            VALUES (?, ?, ?, ?, ?)
            """,
            (case_id, letter_type, json.dumps(fields), content, user_id),
        )
        letter_id = cursor.lastrowid
        _auto_advance_status(db, case_id, "letter_generated")
        log_activity(case_id, user_id, "letter_generated", f"Generated {letter_type} letter", db=db)

    return {
        "id": letter_id,
        "case_id": case_id,
        "letter_type": letter_type,
        "content": content,
        "disclaimer": LEGAL_DISCLAIMER,
    }


def update_letter(letter_id: int, case_id: int, org_id: int, content: str,
                  expected_updated_at: str = None, user_id: int = None) -> dict:
    """Update letter content with optimistic locking and version history."""
    with get_db() as db:
        row = db.execute(
            """
            SELECT l.id, l.updated_at, l.content FROM case_letters l
            JOIN advocacy_cases c ON l.case_id = c.id
            WHERE l.id = ? AND l.case_id = ? AND c.org_id = ?
            """,
            (letter_id, case_id, org_id),
        ).fetchone()

        if not row:
            raise HTTPException(404, "Letter not found")

        if expected_updated_at and row["updated_at"] != expected_updated_at:
            raise HTTPException(
                409,
                "Letter was edited by someone else. Reload to see changes.",
            )

        # Save previous version before overwriting
        editor_id = user_id or 0
        db.execute(
            "INSERT INTO letter_versions (letter_id, content, edited_by) VALUES (?, ?, ?)",
            (letter_id, row["content"], editor_id),
        )

        db.execute(
            "UPDATE case_letters SET content = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            (content, letter_id),
        )
        log_activity(case_id, user_id, "letter_edited", f"Edited letter {letter_id}", db=db)

    return {"id": letter_id, "status": "updated"}


def mark_letter_reviewed(letter_id: int, case_id: int, org_id: int, user_id: int) -> dict:
    """Mark a letter as human-reviewed."""
    with get_db() as db:
        result = db.execute(
            """
            UPDATE case_letters SET reviewed = 1, reviewed_by = ?
            WHERE id = ? AND case_id = ?
            AND case_id IN (SELECT id FROM advocacy_cases WHERE org_id = ?)
            """,
            (user_id, letter_id, case_id, org_id),
        )
        if result.rowcount == 0:
            raise HTTPException(404, "Letter not found")
        log_activity(case_id, user_id, "letter_reviewed", f"Reviewed letter {letter_id}", db=db)

    return {"id": letter_id, "reviewed": True}


def mark_letter_sent(letter_id: int, case_id: int, org_id: int, sent_date: str = None) -> dict:
    """Mark a letter as sent."""
    if not sent_date:
        sent_date = date.today().isoformat()

    with get_db() as db:
        result = db.execute(
            """
            UPDATE case_letters SET marked_sent = 1, sent_date = ?
            WHERE id = ? AND case_id = ?
            AND case_id IN (SELECT id FROM advocacy_cases WHERE org_id = ?)
            """,
            (sent_date, letter_id, case_id, org_id),
        )
        if result.rowcount == 0:
            raise HTTPException(404, "Letter not found")
        log_activity(case_id, None, "letter_sent", f"Letter {letter_id} marked sent on {sent_date}", db=db)

    return {"id": letter_id, "marked_sent": True, "sent_date": sent_date}


def get_case_letters(case_id: int, org_id: int) -> list[dict]:
    """List all letters for a case."""
    with get_db() as db:
        case = db.execute(
            "SELECT id FROM advocacy_cases WHERE id = ? AND org_id = ?",
            (case_id, org_id),
        ).fetchone()
        if not case:
            raise HTTPException(404, "Case not found")

        rows = db.execute(
            """
            SELECT l.*, u.name as generated_by_name, r.name as reviewed_by_name
            FROM case_letters l
            LEFT JOIN users u ON l.generated_by = u.id
            LEFT JOIN users r ON l.reviewed_by = r.id
            WHERE l.case_id = ?
            ORDER BY l.created_at DESC
            """,
            (case_id,),
        ).fetchall()

    return [dict(r) for r in rows]


# ── Notes ────────────────────────────────────────────────────────────────────

def add_note(case_id: int, org_id: int, user_id: int, content: str) -> dict:
    """Add a note to a case."""
    content = (content or "").strip()
    if not content:
        raise HTTPException(400, "Note content required")

    with get_db() as db:
        case = db.execute(
            "SELECT id FROM advocacy_cases WHERE id = ? AND org_id = ?",
            (case_id, org_id),
        ).fetchone()
        if not case:
            raise HTTPException(404, "Case not found")

        cursor = db.execute(
            "INSERT INTO case_notes (case_id, author_id, content) VALUES (?, ?, ?)",
            (case_id, user_id, content),
        )
        db.execute(
            "UPDATE advocacy_cases SET updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            (case_id,),
        )
        log_activity(case_id, user_id, "note_added", "Added a note", db=db)
        return {"id": cursor.lastrowid, "content": content}


def get_case_notes(case_id: int, org_id: int) -> list[dict]:
    """List notes for a case."""
    with get_db() as db:
        rows = db.execute(
            """
            SELECT n.*, u.name as author_name
            FROM case_notes n
            JOIN users u ON n.author_id = u.id
            WHERE n.case_id = ? AND n.case_id IN (SELECT id FROM advocacy_cases WHERE org_id = ?)
            ORDER BY n.created_at DESC
            """,
            (case_id, org_id),
        ).fetchall()
    return [dict(r) for r in rows]


# ── Share Links ─────────────────────────────────────────────────────────────

def create_share_link(case_id: int, org_id: int, user_id: int,
                      label: str = None, expires_days: int = None) -> dict:
    """Create a read-only share link for a case."""
    _ = get_case(case_id, org_id)  # verify access
    token = secrets.token_urlsafe(32)
    expires_at = None
    if expires_days and expires_days > 0:
        from datetime import timedelta
        expires_at = (datetime.utcnow().replace(microsecond=0) + timedelta(days=expires_days)).isoformat()

    with get_db() as db:
        cursor = db.execute(
            """
            INSERT INTO case_share_links (case_id, token, created_by, label, expires_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (case_id, token, user_id, (label or "").strip() or None, expires_at),
        )
        link_id = cursor.lastrowid
        log_activity(case_id, user_id, "share_link_created", label or "Share link created", db=db)

    return {"id": link_id, "token": token, "label": label, "expires_at": expires_at}


def list_share_links(case_id: int, org_id: int) -> list[dict]:
    """List all share links for a case."""
    _ = get_case(case_id, org_id)
    with get_db() as db:
        rows = db.execute(
            """
            SELECT s.id, s.token, s.label, s.active, s.expires_at, s.created_at,
                   u.name as created_by_name
            FROM case_share_links s
            JOIN users u ON s.created_by = u.id
            WHERE s.case_id = ?
            ORDER BY s.created_at DESC
            """,
            (case_id,),
        ).fetchall()
    return [dict(r) for r in rows]


def revoke_share_link(link_id: int, case_id: int, org_id: int) -> None:
    """Deactivate a share link."""
    _ = get_case(case_id, org_id)
    with get_db() as db:
        result = db.execute(
            "UPDATE case_share_links SET active = 0 WHERE id = ? AND case_id = ?",
            (link_id, case_id),
        )
        if result.rowcount == 0:
            raise HTTPException(404, "Share link not found")
        log_activity(case_id, None, "share_link_revoked", f"Revoked share link {link_id}", db=db)


def get_shared_case(token: str) -> dict:
    """Get case data via a share token. Returns case + read-only context."""
    with get_db() as db:
        link = db.execute(
            """
            SELECT s.case_id, s.active, s.expires_at, c.org_id
            FROM case_share_links s
            JOIN advocacy_cases c ON s.case_id = c.id
            WHERE s.token = ?
            """,
            (token,),
        ).fetchone()

    if not link:
        raise HTTPException(404, "Share link not found or expired")
    if not link["active"]:
        raise HTTPException(410, "Share link has been revoked")
    if link["expires_at"]:
        try:
            exp = datetime.fromisoformat(link["expires_at"])
            if datetime.utcnow() > exp:
                raise HTTPException(410, "Share link has expired")
        except ValueError:
            pass

    case = get_case(link["case_id"], link["org_id"])
    # Strip sensitive fields for shared view
    for key in ("created_by", "assigned_to", "created_by_name", "assigned_to_name"):
        case.pop(key, None)
    return case


# ── Letter Version History ──────────────────────────────────────────────────

def get_letter_versions(letter_id: int, case_id: int, org_id: int) -> list[dict]:
    """Get version history for a letter."""
    with get_db() as db:
        # Verify access
        letter = db.execute(
            """
            SELECT l.id FROM case_letters l
            JOIN advocacy_cases c ON l.case_id = c.id
            WHERE l.id = ? AND l.case_id = ? AND c.org_id = ?
            """,
            (letter_id, case_id, org_id),
        ).fetchone()
        if not letter:
            raise HTTPException(404, "Letter not found")

        rows = db.execute(
            """
            SELECT v.id, v.content, v.created_at, u.name as edited_by_name
            FROM letter_versions v
            LEFT JOIN users u ON v.edited_by = u.id
            WHERE v.letter_id = ?
            ORDER BY v.created_at DESC
            """,
            (letter_id,),
        ).fetchall()
    return [dict(r) for r in rows]


def restore_letter_version(version_id: int, letter_id: int, case_id: int,
                           org_id: int, user_id: int) -> dict:
    """Restore a letter to a previous version."""
    with get_db() as db:
        version = db.execute(
            """
            SELECT v.content FROM letter_versions v
            JOIN case_letters l ON v.letter_id = l.id
            JOIN advocacy_cases c ON l.case_id = c.id
            WHERE v.id = ? AND v.letter_id = ? AND l.case_id = ? AND c.org_id = ?
            """,
            (version_id, letter_id, case_id, org_id),
        ).fetchone()
        if not version:
            raise HTTPException(404, "Version not found")

    # Use update_letter which handles version saving and activity logging
    return update_letter(letter_id, case_id, org_id, version["content"], user_id=user_id)


# ── Bulk Operations ─────────────────────────────────────────────────────────

def bulk_update_status(org_id: int, case_ids: list[int], status: str, user_id: int = None) -> dict:
    """Update status for multiple cases at once."""
    if not case_ids:
        raise HTTPException(400, "No case IDs provided")
    if status not in VALID_STATUSES:
        raise HTTPException(400, f"Invalid status: {status}")
    if len(case_ids) > 100:
        raise HTTPException(400, "Maximum 100 cases per bulk operation")

    updated = 0
    with get_db() as db:
        for cid in case_ids:
            result = db.execute(
                "UPDATE advocacy_cases SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ? AND org_id = ?",
                (status, cid, org_id),
            )
            if result.rowcount > 0:
                updated += 1
                log_activity(cid, user_id, "status_changed", f"Status changed to {status} (bulk)", db=db)

    return {"updated": updated, "total": len(case_ids), "status": status}


def bulk_assign(org_id: int, case_ids: list[int], assigned_to: int, user_id: int = None) -> dict:
    """Assign multiple cases to a user."""
    if not case_ids:
        raise HTTPException(400, "No case IDs provided")
    if len(case_ids) > 100:
        raise HTTPException(400, "Maximum 100 cases per bulk operation")

    # Verify assignee is an org member
    with get_db() as db:
        member = db.execute(
            "SELECT id FROM org_members WHERE org_id = ? AND user_id = ? AND status = 'active'",
            (org_id, assigned_to),
        ).fetchone()
        if not member:
            raise HTTPException(400, "Assignee is not an active member of this organization")

    updated = 0
    with get_db() as db:
        for cid in case_ids:
            result = db.execute(
                "UPDATE advocacy_cases SET assigned_to = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ? AND org_id = ?",
                (assigned_to, cid, org_id),
            )
            if result.rowcount > 0:
                updated += 1
                log_activity(cid, user_id, "case_assigned", f"Assigned to user {assigned_to} (bulk)", db=db)

    return {"updated": updated, "total": len(case_ids), "assigned_to": assigned_to}


def bulk_export(org_id: int, case_ids: list[int] = None, status: str = None) -> list[dict]:
    """Export case data as JSON. If no case_ids, export all (with optional status filter)."""
    conditions = ["c.org_id = ?"]
    params: list = [org_id]

    if case_ids:
        placeholders = ",".join("?" * len(case_ids))
        conditions.append(f"c.id IN ({placeholders})")
        params.extend(case_ids)
    if status:
        conditions.append("c.status = ?")
        params.append(status)

    where = " AND ".join(conditions)

    with get_db() as db:
        cases = db.execute(
            f"""
            SELECT c.*, u.name as created_by_name, a.name as assigned_to_name
            FROM advocacy_cases c
            LEFT JOIN users u ON c.created_by = u.id
            LEFT JOIN users a ON c.assigned_to = a.id
            WHERE {where}
            ORDER BY c.created_at DESC
            """,
            params,
        ).fetchall()

        result = []
        for case in cases:
            case_dict = dict(case)
            cid = case_dict["id"]

            # Get notes
            notes = db.execute(
                "SELECT n.content, u.name as author_name, n.created_at FROM case_notes n JOIN users u ON n.author_id = u.id WHERE n.case_id = ? ORDER BY n.created_at",
                (cid,),
            ).fetchall()
            case_dict["notes_list"] = [dict(n) for n in notes]

            # Get letters (without full content for brevity)
            letters = db.execute(
                "SELECT letter_type, marked_sent, sent_date, reviewed, created_at FROM case_letters WHERE case_id = ? ORDER BY created_at",
                (cid,),
            ).fetchall()
            case_dict["letters"] = [dict(l) for l in letters]

            # Get overrides
            overrides = db.execute(
                "SELECT field_name, field_value FROM case_overrides WHERE case_id = ?",
                (cid,),
            ).fetchall()
            case_dict["overrides"] = {r["field_name"]: r["field_value"] for r in overrides}

            result.append(case_dict)

    return result
