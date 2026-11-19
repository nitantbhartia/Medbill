"""B16.6: 200 synthetic bills with planted errors and legitimate look-alikes. Each rule is scored on how many planted errors it
catches and how many look-alikes it wrongly flags. The deploy gate blocks a release that makes either number worse."""

from __future__ import annotations

import json
import random
from pathlib import Path

import analyzer
import config
from db import get_db

BENCHMARK_DIR = Path("data/rule_benchmark")
BASELINE_FILE = BENCHMARK_DIR / "baseline.json"
STRONG = ("high", "medium")
FLAGS = ("QUANTITY_RULE_V2", "ER_LEVEL_RULE_V2", "DUPLICATE_MODIFIERS", "INSURED_PRICE_INFO_ONLY")
MUE_ROWS = [("96372", 4)]  # the limits the planted quantity errors are measured against
PROVIDERS = ["Memorial Regional Hospital", "Aspirus Iron River Hospital", "Broward Health Medical Center", "Sharp Memorial Hospital"]
FILLER = [("71046", "Chest X-Ray 2 views", 380.0), ("70450", "CT Head without contrast", 1200.0), ("99213", "Office visit level 3", 240.0)]
DAY = "2026-02-18"


def _line(code, description, amount, quantity=1, **extra):
    return {"cpt_code": code, "description": description, "quantity": quantity, "charged_amount": amount, "date_of_service": DAY, **extra}


# Each case: (rule it tests, "planted" or "lookalike", the finding type that rule produces, the codes of the lines under test,
# the lines that make the case, how many bills). Findings on the filler lines are not the case's business and are not counted.
CASES = [
    ("duplicate", "planted", "duplicate_charge", ("71046",), lambda: [_line("71046", "Chest X-Ray 2 views", 850.0)] * 2, 25),
    ("unbundling", "planted", "unbundling", ("80048", "80053"), lambda: [_line("80048", "Basic metabolic panel", 90.0), _line("80053", "Comprehensive metabolic panel", 140.0)], 25),
    ("quantity", "planted", "quantity_flag", ("96372",), lambda: [_line("96372", "Injection", 300.0, quantity=12)], 25),
    ("eob", "planted", "eob_mismatch", ("99283",), lambda: [_line("99283", "ER visit level 3", 900.0, insurance_paid=300.0, insurance_adjustment=200.0, patient_responsibility=50.0)], 25),
    ("duplicate", "lookalike", "duplicate_charge", ("85025",), lambda: [_line("85025", "CBC with differential", 85.0), _line("85025", "CBC with differential", 85.0, modifiers=["91"])], 20),
    ("duplicate", "lookalike", "duplicate_charge", ("73030",), lambda: [_line("73030", "Shoulder X-Ray", 300.0, modifiers=["RT"]), _line("73030", "Shoulder X-Ray", 300.0, modifiers=["LT"])], 15),
    ("duplicate", "lookalike", "duplicate_charge", ("93306",), lambda: [_line("93306", "Echocardiogram", 700.0, modifiers=["26"]), _line("93306", "Echocardiogram", 700.0, modifiers=["TC"])], 15),
    ("quantity", "lookalike", "quantity_flag", ("J1100",), lambda: [_line("J1100", "Dexamethasone injection per unit", 45.0, quantity=3)], 15),
    ("er_level", "lookalike", "upcoding", ("99285",), lambda: [_line("99285", "ER visit level 5", 3100.0), _line("74177", "CT abdomen pelvis", 2200.0), _line("96365", "IV infusion", 400.0)], 15),
    ("price", "lookalike", "price_markup", ("99283",), lambda: [_line("99283", "ER visit level 3", 900.0, insurance_paid=300.0, insurance_adjustment=600.0, patient_responsibility=0.0)], 20),
]


def generate_bills(seed: int = 2026) -> list[dict]:
    """The same 200 bills for the same seed: truth, the rule and finding type under test, and whether the case is a planted error."""
    rng = random.Random(seed)
    bills = []
    for rule, kind, finding_type, codes, make_lines, count in CASES:
        for _ in range(count):
            extra = rng.sample(FILLER, rng.randint(1, 2))
            lines = [dict(line) for line in make_lines()] + [_line(code, description, amount) for code, description, amount in extra]
            rng.shuffle(lines)
            bills.append({
                "id": f"rb_{len(bills):03d}", "layout": rng.choice(("table", "statement", "compact")), "rule": rule, "kind": kind,
                "finding_type": finding_type, "codes": list(codes), "provider_name": rng.choice(PROVIDERS),
                "total_charged": round(sum(line["charged_amount"] for line in lines), 2), "line_items": lines,
            })
    return bills


def save(bills: list[dict], directory: Path = BENCHMARK_DIR) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    for bill in bills:
        (directory / f"{bill['id']}.json").write_text(json.dumps(bill, indent=1))


def load(directory: Path = BENCHMARK_DIR) -> list[dict]:
    return [json.loads(path.read_text()) for path in sorted(directory.glob("rb_*.json"))]


def prepare_database() -> None:
    """The limits the planted quantity errors need, and the Medicare rates the price look-alikes are compared with."""
    from seed_data import seed_if_empty
    seed_if_empty()
    with get_db() as db:
        for code, units in MUE_ROWS:
            db.execute("INSERT OR REPLACE INTO mue_limits (code, max_units, setting, version) VALUES (?, ?, 'practitioner', 'benchmark')", (code, units))


def _flagged(bill: dict) -> bool:
    extracted = {"provider_name": bill["provider_name"], "total_charged": bill["total_charged"], "total_patient_owes": bill["total_charged"],
                 "line_items": [dict(line) for line in bill["line_items"]]}
    findings = analyzer.analyze_bill(extracted, "90048")["findings"]
    return any(f["type"] == bill["finding_type"] and f.get("severity") in STRONG and (f.get("line_item") or {}).get("cpt_code") in bill["codes"]
               for f in findings)


def run(bills: list[dict]) -> dict:
    """Per rule: planted errors caught and look-alikes wrongly flagged, with the production rule flags on."""
    saved = {flag: getattr(config, flag) for flag in FLAGS}
    for flag in FLAGS:
        setattr(config, flag, True)
    report: dict[str, dict] = {}
    real_freshness = analyzer.get_data_freshness
    analyzer.get_data_freshness = lambda: {"medicare_pfs": {"fresh": True}, "ncci_edits": {"fresh": True}}  # the benchmark is not about data age
    try:
        for bill in bills:
            row = report.setdefault(bill["rule"], {"planted": 0, "caught": 0, "lookalikes": 0, "false_flags": 0})
            flagged = _flagged(bill)
            if bill["kind"] == "planted":
                row["planted"] += 1
                row["caught"] += flagged
            else:
                row["lookalikes"] += 1
                row["false_flags"] += flagged
    finally:
        analyzer.get_data_freshness = real_freshness
        for flag, value in saved.items():
            setattr(config, flag, value)
    for row in report.values():
        row["catch_rate"] = round(row["caught"] / row["planted"], 4) if row["planted"] else None
        row["false_flag_rate"] = round(row["false_flags"] / row["lookalikes"], 4) if row["lookalikes"] else None
    return report


def regressions(current: dict, baseline: dict) -> list[str]:
    """A rule fails when its catch rate falls, or its false-flag rate rises, by more than RULE_GATE_MAX_DROP_PCT points."""
    failures = []
    for rule, base in baseline.items():
        now = current.get(rule)
        if not now:
            failures.append(f"{rule}: missing from this run")
            continue
        if base["catch_rate"] is not None and (base["catch_rate"] - now["catch_rate"]) * 100 > config.RULE_GATE_MAX_DROP_PCT:
            failures.append(f"{rule}: caught {now['catch_rate']:.0%} of planted errors, was {base['catch_rate']:.0%}")
        if base["false_flag_rate"] is not None and (now["false_flag_rate"] - base["false_flag_rate"]) * 100 > config.RULE_GATE_MAX_DROP_PCT:
            failures.append(f"{rule}: wrongly flagged {now['false_flag_rate']:.0%} of look-alikes, was {base['false_flag_rate']:.0%}")
    return failures
