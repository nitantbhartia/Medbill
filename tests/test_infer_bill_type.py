import pytest

from analyzer import infer_bill_type


def lines(*codes):
    return [{"cpt_code": code, "description": "x", "charged_amount": 100.0} for code in codes]


@pytest.mark.parametrize("codes,expected", [
    (("99285", "85025", "71046"), "er"),
    (("99283",), "er"),
    (("0120", "99232"), "hospital_stay"),
    (("99223", "80053"), "hospital_stay"),
    (("47562", "00840"), "surgery"),
    (("71046", "80053", "85025"), "lab_imaging"),
    (("99213", "36415"), "doctor"),
    ((None, "J1100"), "other"),
])
def test_bill_type_comes_from_the_codes(codes, expected):
    assert infer_bill_type(lines(*codes)) == expected


def test_no_lines_is_other():
    assert infer_bill_type([]) == "other"
