"""B16.8: after a rule change, re-run recent unlocked bills and tell the user when a strong finding appears or goes away.
A report never changes without a dated notice."""

import json
import logging

import analyzer
import config
from charge_summary import NOTE_TYPES
from db import get_db
from scan_pipeline import CannotRebuild, rebuild_extracted

log = logging.getLogger(__name__)

STRONG = ("high", "medium")


def _name(finding: dict) -> str:
    item = finding.get("line_item") or {}
    return item.get("description") or item.get("cpt_code") or "a charge"


def _strong(findings: list[dict]) -> dict:
    """Strong findings keyed by (type, code), each with the charge's name."""
    return {
        (f["type"], (f.get("line_item") or {}).get("cpt_code")): _name(f)
        for f in findings if f.get("severity") in STRONG and f["type"] not in NOTE_TYPES
    }


def _stored_findings(bill_id: int) -> list[dict]:
    with get_db() as db:
        rows = db.execute("SELECT finding_type, severity, details FROM findings WHERE bill_id = ?", (bill_id,)).fetchall()
    return [{**json.loads(row["details"] or "{}"), "type": row["finding_type"], "severity": row["severity"]} for row in rows]


def recheck_bill(bill_id: int) -> dict | None:
    """What a re-run would change on one bill, or None when no strong finding is added or withdrawn. Writes nothing."""
    try:
        bill, extracted = rebuild_extracted(bill_id)
    except CannotRebuild:
        return None
    analysis = analyzer.analyze_bill(extracted, bill["zip_code"] or "")
    old, new = _strong(_stored_findings(bill_id)), _strong(analysis["findings"])
    added = [new[key] for key in new if key not in old]
    withdrawn = [old[key] for key in old if key not in new]
    if not added and not withdrawn:
        return None
    return {"bill_id": bill_id, "provider": bill["provider_name"] or "your", "added": added, "withdrawn": withdrawn,
            "letter_sent": bool(bill["sent_at"]), "extracted": extracted, "analysis": analysis}


def recheck_unlocked(days: int = config.RECHECK_DAYS) -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            "SELECT DISTINCT b.id FROM bills b JOIN report_unlocks u ON u.bill_id = b.id AND u.status = 'paid' "
            "WHERE b.created_at >= date('now', ?) AND COALESCE(b.rules_version, '') != ?",
            (f"-{days} days", config.RULES_VERSION),
        ).fetchall()
    return [change for change in (recheck_bill(row["id"]) for row in rows) if change]


def _messages(change: dict) -> list[tuple[str, str, list[str]]]:
    """One notice for what was added and one for what was withdrawn: (kind, message, charge names)."""
    provider, notices = change["provider"], []
    if change["added"]:
        notices.append(("new_finding", f"We found something new on your {provider} bill: {', '.join(change['added'])}. Your report is updated.", change["added"]))
    if change["withdrawn"]:
        text = (f"We corrected your {provider} report: {', '.join(change['withdrawn'])} that we flagged is likely correct, "
                f"because our check was refined. You can request a refund through Apple: {config.APPLE_REFUND_URL}")
        if change["letter_sent"]:
            text += " You already sent your letter, so call the billing office and withdraw that item."
        notices.append(("withdrawn", text, change["withdrawn"]))
    return notices


def apply_change(change: dict) -> None:
    """Update the report and record a dated notice for each change."""
    analyzer.replace_findings_and_insurance_fields(change["bill_id"], change["extracted"], change["analysis"])
    with get_db() as db:
        db.execute(
            "UPDATE bills SET rules_version = ?, dataset_versions = ? WHERE id = ?",
            (config.RULES_VERSION, json.dumps(analyzer.dataset_versions()), change["bill_id"]),
        )
        for kind, message, items in _messages(change):
            db.execute("INSERT INTO bill_notices (bill_id, kind, message, items_json) VALUES (?, ?, ?, ?)",
                       (change["bill_id"], kind, message, json.dumps(items)))


def notices_for(bill_id: int) -> list[dict]:
    with get_db() as db:
        rows = db.execute("SELECT kind, message, created_at FROM bill_notices WHERE bill_id = ? ORDER BY id DESC", (bill_id,)).fetchall()
    return [{**dict(row), "refund_url": config.APPLE_REFUND_URL if row["kind"] == "withdrawn" else None} for row in rows]


def withdrawn_items_for_sent_letter(bill_id: int) -> list[str]:
    """Charges we withdrew after the user already sent a letter that named them."""
    with get_db() as db:
        sent = db.execute("SELECT sent_at FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not sent or not sent["sent_at"]:
            return []
        rows = db.execute("SELECT items_json FROM bill_notices WHERE bill_id = ? AND kind = 'withdrawn'", (bill_id,)).fetchall()
    return [item for row in rows for item in json.loads(row["items_json"] or "[]")]
