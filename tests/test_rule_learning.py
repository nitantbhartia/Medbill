import json

import analyzer
import config
import outcome_verification
import rule_learning
from db import get_db
from rule_sources import RULES

DUP = "RULE_DUPLICATE_SAME_CODE_DATE_AMOUNT"


def _outcome(rule_id, won, facility="050625"):
    with get_db() as db:
        if won:
            db.execute("INSERT INTO dispute_outcomes (outcome, verified, actual_savings, rule_ids, facility_id) VALUES ('reduced', 1, 100, ?, ?)",
                       (json.dumps([rule_id]), facility))
        else:
            db.execute("INSERT INTO dispute_outcomes (outcome, rejected_rule_ids, reason_category, facility_id) VALUES ('denied', ?, 'correct_as_billed', ?)",
                       (json.dumps([rule_id]), facility))


def test_rule_with_too_few_outcomes_is_not_judged():
    for _ in range(config.OUTCOME_MIN_SAMPLE - 1):
        _outcome(DUP, False)
    assert rule_learning.rule_precision() == {}
    assert rule_learning.nightly_update() == []


def test_mostly_rejected_rule_is_demoted_and_logged():
    for _ in range(9):
        _outcome(DUP, False)
    _outcome(DUP, True)
    changes = rule_learning.nightly_update()
    assert any("Demoted" in line and DUP in line for line in changes)
    assert DUP in rule_learning.demoted_rules("050625")
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) AS n FROM data_quality_runs WHERE status = ?", (config.RULE_DEMOTION_RUN_STATUS,)).fetchone()["n"] == 1
    assert rule_learning.nightly_update() == []  # no repeat entry for the same demotion


def test_demotion_is_lifted_only_after_thirty_days_back_above_the_line():
    for _ in range(9):
        _outcome(DUP, False)
    _outcome(DUP, True)
    rule_learning.nightly_update()
    with get_db() as db:
        db.execute("DELETE FROM dispute_outcomes")
    for _ in range(10):
        _outcome(DUP, True)
    rule_learning.nightly_update()
    assert DUP in rule_learning.demoted_rules(None)  # above the line for one day only
    with get_db() as db:
        db.execute("UPDATE rule_demotions SET above_since = datetime('now', '-31 days')")
    assert any("Lifted" in line for line in rule_learning.nightly_update())
    assert rule_learning.demoted_rules(None) == set()


def test_demoted_rule_shows_as_worth_asking_in_analysis():
    with get_db() as db:
        db.execute("INSERT INTO rule_demotions (rule_id, facility_id, precision, sample) VALUES (?, '', 0.1, 20)", (DUP,))
    bill = {"provider_name": "Mercy General", "total_charged": 1700.0, "total_patient_owes": 1700.0, "line_items": [
        {"cpt_code": "71046", "description": "Chest X-Ray", "quantity": 1, "charged_amount": 850.0, "date_of_service": "2026-03-02"},
        {"cpt_code": "71046", "description": "Chest X-Ray", "quantity": 1, "charged_amount": 850.0, "date_of_service": "2026-03-02"}]}
    result = analyzer.analyze_bill(bill, "90048")
    dup = next(f for f in result["findings"] if f["type"] == "duplicate_charge")
    assert dup["severity"] == "low" and dup["demoted"]


def test_shadow_rule_findings_are_stored_apart_and_never_counted(monkeypatch):
    monkeypatch.setitem(RULES[DUP], "shadow", True)
    bill = {"provider_name": "Mercy General", "total_charged": 1700.0, "total_patient_owes": 1700.0, "line_items": [
        {"cpt_code": "71046", "description": "Chest X-Ray", "quantity": 1, "charged_amount": 850.0, "date_of_service": "2026-03-02"},
        {"cpt_code": "71046", "description": "Chest X-Ray", "quantity": 1, "charged_amount": 850.0, "date_of_service": "2026-03-02"}]}
    result = analyzer.analyze_bill(bill, "90048")
    assert not any(f["type"] == "duplicate_charge" for f in result["findings"])
    assert result["shadow_findings"]
    bill_id = analyzer.save_bill_and_findings(None, bill, result, "90048")
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) AS n FROM shadow_findings WHERE bill_id = ?", (bill_id,)).fetchone()["n"] >= 1
        assert db.execute("SELECT COUNT(*) AS n FROM findings WHERE bill_id = ? AND finding_type = 'duplicate_charge'", (bill_id,)).fetchone()["n"] == 0


def test_reported_rejection_keeps_rules_and_reason():
    bill = {"provider_name": "Mercy General", "total_patient_owes": 500.0, "zip_code": "90048"}
    with get_db() as db:
        bill_id = db.execute("INSERT INTO bills (provider_name, total_patient_owes) VALUES ('Mercy General', 500)").lastrowid
        db.execute("INSERT INTO findings (bill_id, finding_type, rule_id, severity, message, details) VALUES (?, 'duplicate_charge', ?, 'high', 'x', '{}')", (bill_id, DUP))
    outcome_verification.record_reported(bill_id, bill, "no_change", 500.0, "modifier")
    with get_db() as db:
        row = db.execute("SELECT rejected_rule_ids, reason_category FROM dispute_outcomes WHERE bill_id = ?", (bill_id,)).fetchone()
    assert json.loads(row["rejected_rule_ids"]) == [DUP] and row["reason_category"] == "modifier"
