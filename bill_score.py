"""Bill Health Score — a 0-100 score that makes billing findings concrete and shareable."""

import hashlib
import json

from db import get_db

# Score weights (sum to ~100 for a perfect bill)
WEIGHT_NO_FINDINGS = 40
WEIGHT_LOW_MARKUP = 25
WEIGHT_NO_DUPLICATES = 15
WEIGHT_NO_UNBUNDLING = 10
WEIGHT_EOB_MATCH = 10

GRADE_THRESHOLDS = [
    (90, "A", "Excellent — this bill looks clean"),
    (75, "B", "Good — minor issues found"),
    (55, "C", "Fair — some charges worth questioning"),
    (35, "D", "Poor — significant billing problems detected"),
    (0, "F", "Failing — serious overcharges detected"),
]


def compute_bill_score(bill_id: int) -> dict | None:
    """Compute a 0-100 Bill Health Score for a scanned bill."""
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            return None

        findings = db.execute(
            "SELECT finding_type, severity, confidence, potential_savings, details "
            "FROM findings WHERE bill_id = ?",
            (bill_id,),
        ).fetchall()

        line_items = db.execute(
            "SELECT markup_multiple FROM line_items WHERE bill_id = ?",
            (bill_id,),
        ).fetchall()

    bill = dict(bill)
    total_charged = float(bill.get("total_charged") or 0)
    total_savings = float(bill.get("total_potential_savings") or 0)

    score = 100.0
    deductions = []

    # 1. Finding count penalty
    finding_types = [dict(f)["finding_type"] for f in findings]
    severity_counts = {"high": 0, "medium": 0, "low": 0}
    for f in findings:
        sev = dict(f).get("severity", "low")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    high_penalty = severity_counts["high"] * 12
    med_penalty = severity_counts["medium"] * 6
    low_penalty = severity_counts["low"] * 2
    finding_penalty = min(high_penalty + med_penalty + low_penalty, WEIGHT_NO_FINDINGS)
    score -= finding_penalty
    if finding_penalty > 0:
        deductions.append(f"-{finding_penalty:.0f} for {len(findings)} billing issue(s)")

    # 2. Markup penalty
    markups = [float(li["markup_multiple"]) for li in line_items if li["markup_multiple"]]
    if markups:
        avg_markup = sum(markups) / len(markups)
        if avg_markup > 5:
            markup_penalty = WEIGHT_LOW_MARKUP
        elif avg_markup > 3:
            markup_penalty = int(WEIGHT_LOW_MARKUP * 0.6)
        elif avg_markup > 2:
            markup_penalty = int(WEIGHT_LOW_MARKUP * 0.3)
        else:
            markup_penalty = 0
        score -= markup_penalty
        if markup_penalty > 0:
            deductions.append(f"-{markup_penalty} for {avg_markup:.1f}x avg markup vs Medicare")

    # 3. Duplicate charges penalty
    dup_count = finding_types.count("duplicate_charge")
    if dup_count:
        dup_penalty = min(dup_count * 8, WEIGHT_NO_DUPLICATES)
        score -= dup_penalty
        deductions.append(f"-{dup_penalty} for {dup_count} duplicate charge(s)")

    # 4. Unbundling penalty
    unbundle_count = finding_types.count("unbundling")
    if unbundle_count:
        unbundle_penalty = min(unbundle_count * 5, WEIGHT_NO_UNBUNDLING)
        score -= unbundle_penalty
        deductions.append(f"-{unbundle_penalty} for {unbundle_count} unbundling issue(s)")

    # 5. EOB mismatch penalty
    eob_count = finding_types.count("eob_mismatch")
    if eob_count:
        eob_penalty = min(eob_count * 5, WEIGHT_EOB_MATCH)
        score -= eob_penalty
        deductions.append(f"-{eob_penalty} for {eob_count} EOB mismatch(es)")

    score = max(0, min(100, round(score)))

    grade, grade_label, grade_desc = "F", "F", "Failing"
    for threshold, g, desc in GRADE_THRESHOLDS:
        if score >= threshold:
            grade, grade_label, grade_desc = g, g, desc
            break

    # Savings as percentage of bill
    savings_pct = round(total_savings / total_charged * 100, 1) if total_charged > 0 else 0

    # Generate a shareable token (deterministic from bill_id)
    share_token = hashlib.sha256(f"billkarma-score-{bill_id}".encode()).hexdigest()[:12]

    return {
        "bill_id": bill_id,
        "score": score,
        "grade": grade,
        "grade_description": grade_desc,
        "deductions": deductions,
        "total_charged": total_charged,
        "potential_savings": total_savings,
        "savings_pct": savings_pct,
        "finding_count": len(findings),
        "severity_breakdown": severity_counts,
        "share_token": share_token,
        "provider_name": bill.get("provider_name"),
    }


def get_score_by_token(share_token: str) -> dict | None:
    """Look up a bill score by share token (for public share pages)."""
    with get_db() as db:
        rows = db.execute("SELECT id FROM bills ORDER BY id").fetchall()

    for row in rows:
        bill_id = row["id"]
        expected = hashlib.sha256(f"billkarma-score-{bill_id}".encode()).hexdigest()[:12]
        if expected == share_token:
            return compute_bill_score(bill_id)
    return None
