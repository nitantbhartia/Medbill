import json

import config
from analyzer import analyze_bill
from rule_sources import HOSPITAL_REPLIES
from validators.innocent_explanations import apply_innocent_explanations
from validators.llm_review import apply_reviews, review_findings


def _duplicate(**extra):
    item = {"cpt_code": "85025", "description": "CBC", "charged_amount": 85.0, "quantity": 1, **extra}
    return {"type": "duplicate_charge", "severity": "high", "line_item": item, "duplicate_of": [dict(item, **extra)], "potential_savings": 85.0}


def test_different_times_downgrade_a_duplicate_one_level():
    finding = _duplicate()
    finding["duplicate_of"] = [dict(finding["line_item"], time="14:05")]
    finding["line_item"]["time"] = "06:10"
    apply_innocent_explanations([finding])
    assert finding["severity"] == "medium" and finding["innocent_reason"] == "different_time_or_room"


def test_plain_duplicate_is_untouched():
    finding = _duplicate()
    apply_innocent_explanations([finding])
    assert finding["severity"] == "high" and "innocent_reason" not in finding


def test_unbundling_with_allowed_modifier_downgrades():
    finding = {"type": "unbundling", "severity": "high", "line_item": {"cpt_code": "36415", "modifiers": ["59"]}, "related_items": [{"cpt_code": "36410"}]}
    apply_innocent_explanations([finding])
    assert finding["severity"] == "medium" and finding["innocent_reason"] == "allowed_modifier"


def test_drug_line_price_flag_is_downgraded_but_a_visit_is_not():
    drug = {"type": "price_markup", "severity": "high", "line_item": {"cpt_code": "J1100"}}
    visit = {"type": "price_markup", "severity": "high", "line_item": {"cpt_code": "99285"}}
    apply_innocent_explanations([drug, visit])
    assert drug["severity"] == "medium" and drug["innocent_reason"] == "drug_or_supply"
    assert visit["severity"] == "high"


def test_every_reason_has_both_reply_sentences():
    assert all(r["may_say"] and r["say_back"] for r in HOSPITAL_REPLIES.values())


def test_analyzer_downgraded_finding_leaves_the_total(monkeypatch):
    bill = {"provider_name": "Test Hospital", "total_charged": 500.0, "line_items": [
        {"cpt_code": "J1100", "description": "Dexamethasone injection", "charged_amount": 500.0, "quantity": 1, "date_of_service": "2026-01-05"}]}
    result = analyze_bill(bill, "90048")
    for finding in result["findings"]:
        if finding.get("innocent_reason"):
            assert finding["severity"] != "high"
    strong = sum(f["potential_savings"] for f in result["findings"] if f["severity"] in ("high", "medium"))
    assert result["total_potential_savings"] <= strong + 0.01


def test_llm_cannot_add_change_or_upgrade():
    findings = [{"type": "price_markup", "severity": "low", "potential_savings": 100.0}, {"type": "unbundling", "severity": "high", "potential_savings": 50.0}]
    reviews = [
        {"index": 5, "verdict": "downgrade", "explanation": "no such finding"},
        {"index": 0, "verdict": "upgrade", "explanation": "x"},
        {"index": 1, "verdict": "downgrade", "explanation": "Separate procedure.", "potential_savings": 9999, "severity": "high"},
        {"type": "new_finding", "severity": "high"},
    ]
    apply_reviews(findings, reviews)
    assert len(findings) == 2
    assert findings[0] == {"type": "price_markup", "severity": "low", "potential_savings": 100.0}
    assert findings[1]["severity"] == "medium" and findings[1]["potential_savings"] == 50.0


def test_llm_failure_leaves_findings_unchanged(monkeypatch):
    monkeypatch.setattr(config, "LLM_REVIEW_ENABLED", True)
    monkeypatch.setattr(config, "GEMINI_API_KEY", "test")
    findings = [{"type": "unbundling", "severity": "high"}]

    def broken(*_):
        raise json.JSONDecodeError("bad", "", 0)

    review_findings([], findings, ask=broken)
    assert findings[0]["severity"] == "high"


def test_llm_review_is_off_by_default():
    findings = [{"type": "unbundling", "severity": "high"}]
    review_findings([], findings, ask=lambda *_: [{"index": 0, "verdict": "downgrade", "explanation": "x"}])
    assert findings[0]["severity"] == "high"
