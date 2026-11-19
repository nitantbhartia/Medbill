import json
import subprocess
import sys

import accuracy_gate
import config
import rule_benchmark


def test_two_hundred_bills_in_three_layouts_and_the_same_every_time():
    bills = rule_benchmark.generate_bills()
    assert len(bills) == 200 and {b["layout"] for b in bills} == {"table", "statement", "compact"}
    assert sum(b["kind"] == "planted" for b in bills) == 100
    assert bills == rule_benchmark.generate_bills()
    assert bills == rule_benchmark.load(), "regenerate with scripts/rule_benchmark.py --generate"


def test_every_planted_error_is_caught_and_no_lookalike_is_flagged():
    rule_benchmark.prepare_database()
    report = rule_benchmark.run(rule_benchmark.load())
    for rule, row in report.items():
        assert row["caught"] == row["planted"], rule
        assert row["false_flags"] == 0, rule
    assert report["duplicate"]["lookalikes"] == 50 and report["quantity"]["planted"] == 25


def test_the_benchmark_notices_when_a_rule_gets_worse(monkeypatch):
    rule_benchmark.prepare_database()
    baseline = rule_benchmark.run(rule_benchmark.load())
    monkeypatch.setattr("validators.duplicates.explains_repeat", lambda first, second: False)
    monkeypatch.setattr("validators.duplicates.modifiers_of", lambda item: set())
    worse = rule_benchmark.run(rule_benchmark.load())
    assert worse["duplicate"]["false_flags"] > 0
    assert any("duplicate" in line for line in rule_benchmark.regressions(worse, baseline))


def test_gate_tolerates_small_changes_only():
    base = {"duplicate": {"catch_rate": 1.0, "false_flag_rate": 0.0}}
    assert rule_benchmark.regressions({"duplicate": {"catch_rate": 0.99, "false_flag_rate": 0.01}}, base) == []
    assert rule_benchmark.regressions({"duplicate": {"catch_rate": 0.9, "false_flag_rate": 0.0}}, base)
    assert rule_benchmark.regressions({"duplicate": {"catch_rate": 1.0, "false_flag_rate": 0.1}}, base)
    assert rule_benchmark.regressions({}, base) == ["duplicate: missing from this run"]


def test_deploy_gate_script_passes_on_the_saved_baseline():
    ok = accuracy_gate.rule_gate()
    assert ok == []
    baseline = json.loads(rule_benchmark.BASELINE_FILE.read_text())
    assert set(baseline) == {"duplicate", "unbundling", "quantity", "eob", "er_level", "price"}
