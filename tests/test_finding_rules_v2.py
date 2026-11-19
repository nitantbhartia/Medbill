"""B16: quantities, ER level, modifiers and insured price info, each behind its flag. Findings may only get weaker."""

import pytest

import analyzer
import config
from db import get_db
from validators.modifiers import modifiers_of


def line(code, qty=1, amount=100.0, date="2026-03-03", **extra):
    return {"cpt_code": code, "description": f"Service {code}", "quantity": qty, "charged_amount": amount,
            "date_of_service": date, **extra}


def run(*lines, **bill):
    extracted = {"provider_name": "Test Hospital", "provider_address": "1 Main St", "bill_date": "2026-03-04",
                 "total_charged": sum(l["charged_amount"] for l in lines), "total_patient_owes": 500.0,
                 "line_items": list(lines), **bill}
    return analyzer.analyze_bill(extracted, "92103")["findings"]


def of(findings, kind):
    return [f for f in findings if f["type"] == kind]


@pytest.fixture
def mue():
    with get_db() as db:
        db.execute("DELETE FROM mue_limits")
        for code, limit in (("J1885", 8), ("36415", 3), ("96374", 2)):
            db.execute("INSERT INTO mue_limits (code, max_units, setting, version, effective_date) VALUES (?, ?, 'practitioner', '2026 Q1', '2026-01-01')", (code, limit))


@pytest.fixture
def v2(monkeypatch):
    for flag in ("QUANTITY_RULE_V2", "ER_LEVEL_RULE_V2", "DUPLICATE_MODIFIERS", "INSURED_PRICE_INFO_ONLY"):
        monkeypatch.setattr(config, flag, True)


# ── B16.1 quantities ───────────────────────────────────────────────────────────

def test_quantities_under_the_limit_make_no_finding(v2, mue):
    assert not of(run(line("J1885", 4, 80.0), line("36415", 3, 45.0)), "quantity_flag")
    assert not of(run(line("J1885", 4, 80.0), line("36415", 3, 45.0)), "quantity_question")


def test_only_the_excess_over_the_limit_is_flagged(v2, mue):
    finding = of(run(line("96374", 5, 500.0)), "quantity_flag")[0]
    assert (finding["mue_limit"], finding["billed_quantity"], finding["potential_savings"]) == (2, 5, 300.0)
    assert finding["rule_id"] == "RULE_QUANTITY_OVER_MUE" and "limit for code 96374 is 2 per day" in finding["message"]


def test_lines_with_the_same_code_and_date_are_summed(v2, mue):
    assert of(run(line("96374", 1, 100.0), line("96374", 2, 200.0)), "quantity_flag")


def test_a_high_quantity_with_no_published_limit_is_a_zero_dollar_note(v2, mue):
    note = of(run(line("99999", 6, 600.0)), "quantity_question")[0]
    assert note["severity"] == "low" and note["potential_savings"] == 0


def test_old_quantity_rule_is_unchanged_when_the_flag_is_off(mue):
    assert of(run(line("J1885", 4, 80.0)), "quantity_flag")


# ── B16.2 ER level ─────────────────────────────────────────────────────────────

def test_a_level_5_with_ct_iv_and_labs_makes_no_finding(v2):
    support = [line("70450", amount=900.0), line("96374", amount=90.0), line("80053"), line("85025"), line("84443")]
    assert not of(run(line("99285", amount=3000.0), *support), "upcoding")


def test_a_level_5_alone_is_a_low_note_and_never_60_percent_of_the_charge(v2):
    finding = of(run(line("99285", amount=3000.0)), "upcoding")[0]
    assert finding["severity"] == "low" and finding["potential_savings"] == 0
    assert "Please send the documentation that supports a level 5 visit" in finding["message"]


def test_a_level_4_alone_is_a_zero_dollar_note_and_a_level_3_is_fine(v2):
    assert of(run(line("99284", amount=2000.0)), "upcoding")[0]["potential_savings"] == 0
    assert not of(run(line("99283", amount=900.0)), "upcoding")


# ── B16.3 modifiers ────────────────────────────────────────────────────────────

def test_a_repeat_lab_test_with_modifier_91_is_not_a_duplicate(v2):
    assert not of(run(line("85025", modifiers=["91"]), line("85025", modifiers=["91"])), "duplicate_charge")


def test_a_repeat_lab_test_with_no_modifiers_is_worth_asking_not_strong(v2):
    finding = of(run(line("85025"), line("85025")), "duplicate_charge")[0]
    assert finding["severity"] == "low" and finding["potential_savings"] == 0 and "modifier 91" in finding["message"]


def test_left_and_right_are_not_duplicates(v2):
    assert not of(run(line("73630", modifiers=["RT"]), line("73630", modifiers=["LT"])), "duplicate_charge")


def test_a_doctors_reading_and_the_facility_part_are_not_duplicates(v2):
    assert not of(run(line("71046", modifiers=["26"]), line("71046", modifiers=["TC"])), "duplicate_charge")


def test_an_exact_duplicate_with_no_modifiers_on_a_non_lab_code_is_still_high(v2):
    assert of(run(line("71046", amount=412.0), line("71046", amount=412.0)), "duplicate_charge")[0]["severity"] == "high"


def test_modifiers_read_as_a_list_or_as_json_text():
    assert modifiers_of({"modifiers": ["rt"]}) == {"RT"} and modifiers_of({"modifiers": '["91"]'}) == {"91"}


# ── B16.4 insured in-network prices ────────────────────────────────────────────

def insured_line(**extra):
    return line("99285", amount=6000.0, insurance_paid=900.0, insurance_adjustment=4800.0, patient_responsibility=300.0, **extra)


def test_an_insured_line_with_an_adjustment_and_a_big_markup_is_information_only(v2):
    with get_db() as db:
        db.execute("DELETE FROM medicare_rates WHERE cpt_code = '99285'")
        db.execute("INSERT INTO medicare_rates (cpt_code, facility_rate, non_facility_rate, locality, effective_year) VALUES ('99285', 1000, 1000, '0000000', 2026)")
    findings = run(insured_line())
    assert not of(findings, "price_markup")
    info = of(findings, "price_info")
    assert info and info[0]["potential_savings"] == 0 and "already applied its discount" in info[0]["message"]


def test_the_same_line_on_a_self_pay_bill_is_unchanged(v2):
    with get_db() as db:
        db.execute("DELETE FROM medicare_rates WHERE cpt_code = '99285'")
        db.execute("INSERT INTO medicare_rates (cpt_code, facility_rate, non_facility_rate, locality, effective_year) VALUES ('99285', 1000, 1000, '0000000', 2026)")
    assert of(run(line("99285", amount=6000.0)), "price_markup")


def test_all_info_findings_make_the_bill_clean_and_free():
    from charge_summary import group_findings_by_charge
    finding = {"id": 1, "finding_type": "price_info", "rule_id": "RULE_MARKUP_VS_MEDICARE", "severity": "low", "potential_savings": 0,
               "message": "Priced at 6x", "parsed_details": {"line_item": line("99285", amount=6000.0), "markup_multiple": 6.0}}
    summary = group_findings_by_charge([finding])
    assert summary["info_only"] and summary["total_savings"] == 0 and summary["strong_count"] == 0


def test_the_diff_script_reports_added_findings_and_writes_nothing(tmp_path):
    import finding_diff
    entry = {"id": "sample", "bill": {"provider_name": "Test Hospital", "total_patient_owes": 500.0},
             "line_items": [line("99285", amount=3000.0)], "stored": []}
    summary = finding_diff.run([entry], str(tmp_path / "diff.csv"))
    assert summary["changes"] >= 1 and "upcoding" in (tmp_path / "diff.csv").read_text()
    assert config.ER_LEVEL_RULE_V2 is False  # flags are put back after the run
