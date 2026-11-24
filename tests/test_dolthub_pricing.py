"""Tests for turning DoltHub price rows into gross charge and negotiated-rate columns."""

import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())
os.environ["DB_PATH"] = ":memory:"

from scripts.load_pricing_from_dolthub import summarize_dolthub_prices  # noqa: E402

RUTHERFORD_10060 = [
    {"payer": "BCBS MISSIONPOINT", "price": "394.86"},
    {"payer": "BCBS TENNCARE SELECT", "price": "25.71"},
    {"payer": "CIGNA LOCALPLUS", "price": "2138.5"},
    {"payer": "AETNA", "price": "1520"},
]


def test_gross_charge_stays_empty_when_only_negotiated_rates_exist():
    summary = summarize_dolthub_prices(RUTHERFORD_10060)

    assert summary["gross_charge"] is None
    assert summary["max_negotiated_rate"] == 2138.5
    assert summary["min_negotiated_rate"] == 25.71


def test_gross_charge_comes_from_gross_labelled_row():
    items = RUTHERFORD_10060 + [{"payer": "GROSS CHARGE", "price": "2155.70"}, {"payer": "DISCOUNTED CASH", "price": "646.71"}]
    summary = summarize_dolthub_prices(items)

    assert summary["gross_charge"] == 2155.70
    assert summary["cash_price"] == 646.71
    assert summary["max_negotiated_rate"] == 2138.5


def test_empty_or_unpriced_rows_return_none():
    assert summarize_dolthub_prices([]) is None
    assert summarize_dolthub_prices([{"payer": "AETNA", "price": None}]) is None
