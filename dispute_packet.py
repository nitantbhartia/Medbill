"""Dispute packet generator."""

from __future__ import annotations

import json
from datetime import datetime

from db import get_db


def generate_dispute_packet(bill_id: int) -> dict | None:
    """Build a structured dispute packet for download/email."""
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            return None
        line_items = db.execute(
            "SELECT * FROM line_items WHERE bill_id = ? ORDER BY id", (bill_id,)
        ).fetchall()
        findings = db.execute(
            "SELECT * FROM findings WHERE bill_id = ? ORDER BY "
            "CASE severity WHEN 'high' THEN 0 WHEN 'medium' THEN 1 ELSE 2 END",
            (bill_id,),
        ).fetchall()

    bill = dict(bill)
    items = [dict(li) for li in line_items]
    finding_rows = []
    references = set()
    for f in findings:
        raw = dict(f)
        details = json.loads(raw.get("details") or "{}")
        evidence = details.get("evidence") or {}
        if evidence.get("source"):
            references.add(evidence["source"])
        finding_rows.append(
            {
                "type": raw.get("finding_type"),
                "severity": raw.get("severity"),
                "message": raw.get("message"),
                "estimated_patient_savings": details.get("estimated_patient_savings", raw.get("potential_savings", 0)),
                "cpt_code": (details.get("line_item") or {}).get("cpt_code"),
                "evidence": evidence,
            }
        )

    cover_letter = (
        f"To Billing Department,\n\n"
        f"I am requesting review of account related to service date {bill.get('bill_date') or 'N/A'} "
        f"from {bill.get('provider_name') or 'provider'}. Attached is a line-by-line review "
        f"of potential billing discrepancies.\n\n"
        f"I request correction and resubmission to insurance where applicable.\n\n"
        f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC"
    )

    return {
        "bill": bill,
        "line_items": items,
        "findings": finding_rows,
        "cover_letter": cover_letter,
        "references": sorted(references),
        "disclaimer": (
            "Informational review only. This packet is not legal advice and does not guarantee an outcome."
        ),
    }
