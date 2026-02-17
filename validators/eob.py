"""Reconcile provider bill lines with EOB/payment math."""


def check_eob_reconciliation(extracted_data: dict) -> list[dict]:
    """
    Validate line-level insurance math:
    charged ≈ insurance_paid + insurance_adjustment + patient_responsibility
    """
    findings = []
    for item in extracted_data.get("line_items", []):
        charged = item.get("charged_amount")
        ins_paid = item.get("insurance_paid")
        ins_adj = item.get("insurance_adjustment")
        patient = item.get("patient_responsibility")

        if charged is None:
            continue
        if ins_paid is None and ins_adj is None and patient is None:
            continue

        total = (ins_paid or 0) + (ins_adj or 0) + (patient or 0)
        diff = round(float(charged) - float(total), 2)
        if abs(diff) <= 1.0:
            continue

        findings.append(
            {
                "type": "eob_mismatch",
                "severity": "medium",
                "line_item": item,
                "potential_savings": max(0.0, diff),
                "message": (
                    f"EOB reconciliation mismatch for '{item.get('description', 'service')}'. "
                    f"Billed ${charged:,.2f}, but insurance-paid + adjustment + patient-share "
                    f"totals ${total:,.2f} (difference ${diff:,.2f})."
                ),
                "evidence": {
                    "source": "insurance_reconciliation",
                    "data_date": item.get("date_of_service"),
                    "sample_size": 1,
                    "limitations": "Depends on extracted EOB fields being accurate.",
                },
            }
        )
    return findings
