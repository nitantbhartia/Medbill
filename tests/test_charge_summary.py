from analyzer import analyze_bill, get_bill_results, save_bill_and_findings
from charge_summary import group_findings_by_charge
from tests.conftest import SAMPLE_BILL, SAMPLE_BILL_WITH_DUPLICATES


def _results(bill):
    analysis = analyze_bill(bill, "33021")
    return get_bill_results(save_bill_and_findings(None, bill, analysis, "33021"))


def test_each_charge_counts_once_and_total_fits_what_is_owed():
    results = _results(SAMPLE_BILL)
    summary = group_findings_by_charge(results["findings"], SAMPLE_BILL["total_patient_owes"])
    codes = [c["code"] for c in summary["charges"]]
    assert sorted(codes) == ["71046", "80053", "99285"]
    er = next(c for c in summary["charges"] if c["code"] == "99285")
    assert er["savings"] == 1200.0
    assert len(er["reasons"]) >= 2
    assert summary["total_savings"] == 1400.0
    assert summary["total_savings"] <= SAMPLE_BILL["total_patient_owes"]


def test_strongest_reason_comes_first_and_ids_are_kept_for_the_letter():
    results = _results(SAMPLE_BILL_WITH_DUPLICATES)
    summary = group_findings_by_charge(results["findings"])
    top = summary["charges"][0]
    assert top["strong"]
    assert top["reasons"][0]["severity"] == "high"
    all_ids = sorted(i for c in summary["charges"] for i in c["finding_ids"])
    assert all_ids == sorted(f["id"] for f in results["findings"])


def test_total_is_capped_at_amount_owed():
    findings = [
        {"id": 1, "finding_type": "price_markup", "severity": "high", "potential_savings": 900,
         "parsed_details": {"line_item": {"cpt_code": "99285", "description": "ER visit", "charged_amount": 3000}}},
        {"id": 2, "finding_type": "duplicate_charge", "severity": "high", "potential_savings": 700,
         "parsed_details": {"line_item": {"cpt_code": "71046", "description": "Chest X-ray", "charged_amount": 700}}},
    ]
    assert group_findings_by_charge(findings, amount_owed=1000)["total_savings"] == 1000


def test_duplicate_leads_and_reasons_are_not_repeated():
    results = _results(SAMPLE_BILL_WITH_DUPLICATES)
    xray = next(c for c in group_findings_by_charge(results["findings"])["charges"] if c["code"] == "71046")
    labels = [r["label"] for r in xray["reasons"]]
    assert labels[0] == "Billed more than once"
    assert len(labels) == len(set(labels))
