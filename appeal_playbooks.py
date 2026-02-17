"""Appeal playbook generation by finding type."""

from __future__ import annotations

from db import get_db


PLAYBOOKS = {
    "duplicate_charge": [
        "Request charge audit for duplicate CPT/date lines.",
        "Ask for corrected claim and resubmission.",
        "Request updated EOB and patient balance recalculation.",
    ],
    "price_markup": [
        "Request itemized rationale for outlier pricing.",
        "Ask for fair-price adjustment / prompt-pay discount.",
        "If insured, request provider-side correction and insurer resubmission.",
    ],
    "unbundling": [
        "Reference NCCI bundling guidance and request coding review.",
        "Ask coding team to validate modifier usage.",
        "Request corrected claim submission.",
    ],
    "upcoding": [
        "Request documentation review for visit level.",
        "Ask for coding audit and corrected CPT if warranted.",
        "Request claim reprocessing after correction.",
    ],
    "eob_mismatch": [
        "Request line-level EOB reconciliation worksheet.",
        "Ask for explanation of payment/adjustment mismatch.",
        "Request corrected statement before payment.",
    ],
}


def generate_appeal_playbook(bill_id: int) -> dict | None:
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            return None
        findings = db.execute("SELECT * FROM findings WHERE bill_id = ?", (bill_id,)).fetchall()
        line_items = db.execute("SELECT * FROM line_items WHERE bill_id = ?", (bill_id,)).fetchall()

    insured = any(li["insurance_paid"] or li["patient_responsibility"] for li in line_items)
    steps = []
    seen = set()
    for f in findings:
        ftype = f["finding_type"]
        if ftype in seen:
            continue
        seen.add(ftype)
        steps.extend(PLAYBOOKS.get(ftype, ["Request formal itemized review and written response."]))

    if insured:
        steps.append("Ask provider to resubmit corrected claim to insurance.")
    else:
        steps.append("Request self-pay reprice and hardship/financial assistance review.")

    return {
        "bill_id": bill_id,
        "provider_name": bill["provider_name"],
        "insured_flow": insured,
        "finding_types": sorted(seen),
        "steps": steps,
    }
