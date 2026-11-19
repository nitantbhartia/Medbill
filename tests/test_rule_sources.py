import pytest

from analyzer import RULE_ID_BY_TYPE
from rule_sources import RULES, basis_for

PRICE_DETAILS = {"line_item": {"cpt_code": "99285", "charged_amount": 3100.0}, "medicare_rate": 412.0, "markup_multiple": 7.5}


def test_every_analyzer_rule_has_a_source():
    assert set(RULE_ID_BY_TYPE.values()) <= set(RULES)


def test_markup_basis_names_the_data_year_and_values():
    basis = basis_for("RULE_MARKUP_VS_MEDICARE", PRICE_DETAILS)
    assert basis["kind"] == "official" and basis["source_year"] == 2026
    assert "$412" in basis["explanation"] and "99285" in basis["explanation"] and "7.5" in basis["explanation"]


@pytest.mark.parametrize("rule_id", sorted(RULES))
def test_no_template_renders_with_missing_values_or_braces(rule_id):
    text = basis_for(rule_id, {})["explanation"]
    assert text and "{" not in text and "None" not in text


def test_check_rules_are_never_official():
    assert all(basis_for(rule_id, {})["kind"] != "official" for rule_id, rule in RULES.items() if rule["kind"] == "check")


def test_duplicate_counts_the_matches():
    details = {"line_item": {"cpt_code": "85025"}, "duplicate_of": [{}]}
    assert "2 times" in basis_for("RULE_DUPLICATE_SAME_CODE_DATE_AMOUNT", details)["explanation"]


def test_unknown_rule_has_no_basis():
    assert basis_for("RULE_GENERIC_HEURISTIC", {}) is None
