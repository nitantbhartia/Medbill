import json

import analyzer
import config
import report_recheck
from dispute_workflow import build_phone_script
from db import get_db

DUP_LINES = [
    {"cpt_code": "71046", "description": "Chest X-Ray", "quantity": 1, "charged_amount": 850.0, "date_of_service": "2026-03-02"},
    {"cpt_code": "71046", "description": "Chest X-Ray", "quantity": 1, "charged_amount": 850.0, "date_of_service": "2026-03-02"},
]


def _saved_bill(lines, stored_finding=None, sent=False, rules_version="old") -> int:
    extracted = {"provider_name": "Mercy General", "total_charged": 1700.0, "total_patient_owes": 1700.0, "line_items": [dict(l) for l in lines]}
    bill_id = analyzer.save_bill_and_findings(None, extracted, {"total_findings": 0, "total_potential_savings": 0, "findings": []}, "90048")
    with get_db() as db:
        db.execute("UPDATE bills SET rules_version = ?, sent_at = ? WHERE id = ?", (rules_version, "2026-03-05" if sent else None, bill_id))
        db.execute("INSERT INTO report_unlocks (bill_id, stripe_session_id, amount_cents, status) VALUES (?, ?, 1999, 'paid')", (bill_id, f"s{bill_id}"))
        if stored_finding:
            db.execute("INSERT INTO findings (bill_id, finding_type, severity, potential_savings, message, details) VALUES (?, ?, 'high', 850, 'x', ?)",
                       (bill_id, stored_finding["type"], json.dumps(stored_finding)))
    return bill_id


def test_new_bill_stores_rules_and_dataset_versions():
    bill_id = _saved_bill(DUP_LINES, rules_version=config.RULES_VERSION)
    with get_db() as db:
        row = db.execute("SELECT rules_version, dataset_versions FROM bills WHERE id = ?", (bill_id,)).fetchone()
    assert json.loads(row["dataset_versions"])["medicare_pfs"] == config.MEDICARE_PFS_YEAR
    assert row["rules_version"] == config.RULES_VERSION


def test_new_strong_finding_is_listed_and_a_notice_is_recorded_on_apply():
    bill_id = _saved_bill(DUP_LINES)
    changes = report_recheck.recheck_unlocked()
    assert [c["bill_id"] for c in changes] == [bill_id] and changes[0]["added"]
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) AS n FROM findings WHERE bill_id = ?", (bill_id,)).fetchone()["n"] == 0  # recheck writes nothing
    report_recheck.apply_change(changes[0])
    notice = report_recheck.notices_for(bill_id)[0]
    assert notice["kind"] == "new_finding" and "Mercy General" in notice["message"]
    assert report_recheck.recheck_unlocked() == []  # now on the current version


def test_withdrawn_finding_notice_has_refund_link_and_phone_script_line(monkeypatch):
    monkeypatch.setattr(config, "DUPLICATE_MODIFIERS", True)
    lines = [DUP_LINES[0], {**DUP_LINES[1], "modifiers": ["91"], "cpt_code": "71046"}]
    stored = {"type": "duplicate_charge", "severity": "high", "line_item": lines[0]}
    bill_id = _saved_bill(lines, stored_finding=stored, sent=True)
    change = report_recheck.recheck_unlocked()[0]
    assert change["withdrawn"] and change["letter_sent"]
    report_recheck.apply_change(change)
    notice = next(n for n in report_recheck.notices_for(bill_id) if n["kind"] == "withdrawn")
    assert notice["kind"] == "withdrawn" and notice["refund_url"] == config.APPLE_REFUND_URL
    assert "withdraw that item" in notice["message"]
    with get_db() as db:
        db.execute("INSERT INTO findings (bill_id, finding_type, severity, potential_savings, message, details) VALUES (?, 'price_markup', 'low', 0, 'x', ?)",
                   (bill_id, json.dumps({"line_item": lines[0]})))
    assert "WITHDRAW THESE ITEMS" in build_phone_script(bill_id)


def test_bill_already_on_current_rules_is_not_rechecked():
    _saved_bill(DUP_LINES, rules_version=config.RULES_VERSION)
    assert report_recheck.recheck_unlocked() == []
