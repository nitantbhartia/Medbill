from __future__ import annotations

import hashlib
import json
from datetime import date, datetime
from typing import Any

from db import get_db
from tools_catalog import get_tool
from validators.benchmarks import get_benchmark
from validators.duplicates import find_duplicates
from validators.geo import get_medicare_locality, get_region
from validators.pricing import get_medicare_rate, get_opps_rate
from validators.unbundling import check_unbundling


FPL_2026 = {
    1: 15650,
    2: 21150,
    3: 26650,
    4: 32150,
    5: 37650,
    6: 43150,
    7: 48650,
    8: 54150,
}

STATE_SOL_YEARS = {
    "AL": 6, "AK": 3, "AZ": 6, "AR": 5, "CA": 4, "CO": 6, "CT": 6, "DE": 3,
    "FL": 5, "GA": 6, "HI": 6, "ID": 5, "IL": 5, "IN": 6, "IA": 10, "KS": 5,
    "KY": 5, "LA": 3, "ME": 6, "MD": 3, "MA": 6, "MI": 6, "MN": 6, "MS": 3,
    "MO": 10, "MT": 8, "NE": 5, "NV": 6, "NH": 3, "NJ": 6, "NM": 6, "NY": 6,
    "NC": 3, "ND": 6, "OH": 6, "OK": 5, "OR": 6, "PA": 4, "RI": 10, "SC": 3,
    "SD": 6, "TN": 6, "TX": 4, "UT": 6, "VT": 6, "VA": 5, "WA": 6, "WV": 5,
    "WI": 6, "WY": 10,
}

STATE_CODES = {
    "ALABAMA": "AL", "ALASKA": "AK", "ARIZONA": "AZ", "ARKANSAS": "AR", "CALIFORNIA": "CA",
    "COLORADO": "CO", "CONNECTICUT": "CT", "DELAWARE": "DE", "FLORIDA": "FL", "GEORGIA": "GA",
    "HAWAII": "HI", "IDAHO": "ID", "ILLINOIS": "IL", "INDIANA": "IN", "IOWA": "IA",
    "KANSAS": "KS", "KENTUCKY": "KY", "LOUISIANA": "LA", "MAINE": "ME", "MARYLAND": "MD",
    "MASSACHUSETTS": "MA", "MICHIGAN": "MI", "MINNESOTA": "MN", "MISSISSIPPI": "MS", "MISSOURI": "MO",
    "MONTANA": "MT", "NEBRASKA": "NE", "NEVADA": "NV", "NEW HAMPSHIRE": "NH", "NEW JERSEY": "NJ",
    "NEW MEXICO": "NM", "NEW YORK": "NY", "NORTH CAROLINA": "NC", "NORTH DAKOTA": "ND", "OHIO": "OH",
    "OKLAHOMA": "OK", "OREGON": "OR", "PENNSYLVANIA": "PA", "RHODE ISLAND": "RI", "SOUTH CAROLINA": "SC",
    "SOUTH DAKOTA": "SD", "TENNESSEE": "TN", "TEXAS": "TX", "UTAH": "UT", "VERMONT": "VT",
    "VIRGINIA": "VA", "WASHINGTON": "WA", "WEST VIRGINIA": "WV", "WISCONSIN": "WI", "WYOMING": "WY",
}

DENIAL_REASON_MAP = {
    "CO-16": "Missing or incomplete information. Request claim reprocessing after corrections.",
    "CO-50": "Not medically necessary. Include physician documentation and guideline support.",
    "CO-97": "Service included in another service. Request coding-level review.",
    "CO-197": "Precertification/authorization absent. Provide retro-auth records if available.",
    "A1": "Claim denied due to missing/invalid information. Submit corrected claim details.",
}


def _to_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None or value == "":
            return default
        return float(value)
    except Exception:
        return default


def _to_int(value: Any, default: int = 0) -> int:
    try:
        if value is None or value == "":
            return default
        return int(float(value))
    except Exception:
        return default


def _parse_items_json(payload: dict[str, Any], key: str = "line_items_json") -> list[dict[str, Any]]:
    raw = payload.get(key)
    if not raw:
        return []
    if isinstance(raw, list):
        return [x for x in raw if isinstance(x, dict)]
    if isinstance(raw, str):
        try:
            data = json.loads(raw)
            if isinstance(data, list):
                return [x for x in data if isinstance(x, dict)]
        except Exception:
            return []
    return []


def _resolve_state_code(state: str) -> str | None:
    if not state:
        return None
    t = state.strip().upper()
    if len(t) == 2 and t in STATE_SOL_YEARS:
        return t
    return STATE_CODES.get(t)


def _build_cta(tool: dict[str, Any], state_key: str) -> dict[str, Any]:
    ctas = tool.get("ctas") or {}
    cta = ctas.get(state_key) or ctas.get("default") or next(iter(ctas.values()), {})
    return {
        "headline": cta.get("headline", "Upload your bill for a full audit."),
        "body": cta.get("body", "Our full audit can identify additional savings opportunities."),
        "primary_label": cta.get("primary_label", "Upload My Bill — Free Audit"),
        "primary_url": cta.get("primary_url", "/scan"),
        "secondary_label": cta.get("secondary_label"),
        "secondary_url": cta.get("secondary_url"),
        "footnote": cta.get("footnote", "Free audit. $29-149 to fight it. No savings? Full refund."),
    }


def _hospital_by_name(name: str) -> dict[str, Any] | None:
    token = (name or "").strip()
    if not token:
        return None
    like = f"%{token}%"
    with get_db() as db:
        row = db.execute(
            """
            SELECT h.facility_id, h.name, h.ownership, h.is_nonprofit,
                   COALESCE(fbm.billing_grade, bm.billing_grade) AS billing_grade,
                   COALESCE(fbm.avg_markup, bm.avg_markup_vs_medicare) AS avg_markup
            FROM hospitals h
            LEFT JOIN facility_billing_metrics fbm ON fbm.facility_id = h.facility_id
            LEFT JOIN billing_metrics bm ON bm.facility_id = h.facility_id
            WHERE h.name LIKE ?
            ORDER BY CASE WHEN lower(h.name)=lower(?) THEN 0 ELSE 1 END, h.name
            LIMIT 1
            """,
            (like, token),
        ).fetchone()
    return dict(row) if row else None


def _lookup_cpt(cpt_code: str, zip_code: str = "") -> dict[str, Any] | None:
    cpt = (cpt_code or "").strip().upper()
    if not cpt:
        return None
    locality = get_medicare_locality((zip_code or "").strip())
    medicare = get_medicare_rate(cpt, locality)
    opps = get_opps_rate(cpt)
    benchmark = get_benchmark(cpt, zip_code)
    with get_db() as db:
        row = db.execute(
            "SELECT description FROM medicare_rates WHERE cpt_code = ? AND description IS NOT NULL LIMIT 1",
            (cpt,),
        ).fetchone()
    if not any([medicare, opps, benchmark, row]):
        return None
    return {
        "cpt_code": cpt,
        "description": row["description"] if row else None,
        "medicare_rate": medicare,
        "opps_rate": opps,
        "benchmark": benchmark,
        "locality": locality,
        "region": get_region(zip_code) if zip_code else "national",
    }


def run_tool(slug: str, payload: dict[str, Any]) -> dict[str, Any]:
    tool = get_tool(slug)
    if not tool:
        raise ValueError("Unknown tool slug")

    handlers = {
        "medical-bill-error-checker": _run_medical_bill_error_checker,
        "hospital-financial-assistance-calculator": _run_financial_assistance,
        "medical-bill-dispute-letter-generator": _run_dispute_letter_generator,
        "surprise-bill-checker": _run_surprise_bill_checker,
        "medical-bill-negotiation-script-generator": _run_negotiation_script_generator,
        "procedure-cost-estimator": _run_procedure_cost_estimator,
        "hospital-billing-grade-lookup": _run_hospital_billing_grade_lookup,
        "good-faith-estimate-calculator": _run_good_faith_estimator,
        "medical-debt-statute-of-limitations-checker": _run_debt_sol_checker,
        "medical-debt-rights-checker": _run_debt_rights_checker,
        "debt-validation-letter-generator": _run_debt_validation_generator,
        "insurance-denial-appeal-letter-generator": _run_denial_appeal_generator,
        "eob-decoder": _run_eob_decoder,
        "medical-bill-payment-plan-calculator": _run_payment_plan_calculator,
        "cpt-code-lookup": _run_cpt_lookup,
        "medicare-rate-lookup": _run_medicare_rate_lookup,
    }
    state_key, summary, details = handlers[slug](payload)
    return {
        "status": "ok",
        "tool_slug": slug,
        "result_state": state_key,
        "summary": summary,
        "details": details,
        "cta": _build_cta(tool, state_key),
        "lead_magnet": tool.get("lead_magnet", {}),
    }


def hash_payload(payload: dict[str, Any]) -> str:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def _run_medical_bill_error_checker(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    zip_code = (payload.get("zip_code") or "").strip()
    items = _parse_items_json(payload)
    issues: list[dict[str, Any]] = []
    total_savings = 0.0

    for item in items:
        cpt = (item.get("cpt_code") or "").strip().upper()
        charged = _to_float(item.get("charged_amount"))
        item["cpt_code"] = cpt
        item["charged_amount"] = charged
        item["quantity"] = _to_int(item.get("quantity"), 1)

    for idx, item in enumerate(items):
        dup = find_duplicates(item, items)
        if dup:
            issues.append({"type": dup["type"], "message": dup["message"], "potential_savings": dup.get("potential_savings", 0)})
            total_savings += _to_float(dup.get("potential_savings"))

        unbundle = check_unbundling(item, items)
        if unbundle:
            issues.append({"type": unbundle["type"], "message": unbundle["message"], "potential_savings": unbundle.get("potential_savings", 0)})
            total_savings += _to_float(unbundle.get("potential_savings"))

        if not item.get("cpt_code"):
            continue
        locality = get_medicare_locality(zip_code)
        medicare_rate = get_medicare_rate(item["cpt_code"], locality)
        if medicare_rate and item["charged_amount"] > (medicare_rate * 3):
            savings = max(0.0, item["charged_amount"] - (medicare_rate * 3))
            issues.append(
                {
                    "type": "price_markup",
                    "message": f"CPT {item['cpt_code']} billed at {item['charged_amount']/medicare_rate:.1f}x Medicare.",
                    "potential_savings": round(savings, 2),
                }
            )
            total_savings += savings

        if idx > 40:
            break

    issues = sorted(issues, key=lambda x: x.get("potential_savings", 0), reverse=True)[:12]
    if issues:
        return (
            "issues_found",
            f"Found {len(issues)} potential issue(s) with estimated overcharges around ${total_savings:,.2f}.",
            {"issues": issues, "issue_count": len(issues), "estimated_overcharge": round(total_savings, 2)},
        )
    return (
        "none_found",
        "No obvious coding or pricing issues were detected from the entered lines.",
        {"issues": [], "issue_count": 0, "estimated_overcharge": 0.0},
    )


def _run_financial_assistance(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    income = _to_float(payload.get("income"))
    household_size = max(1, _to_int(payload.get("household_size"), 1))
    hospital_name = (payload.get("hospital_name") or "").strip()
    hospital = _hospital_by_name(hospital_name)

    base = FPL_2026.get(household_size, FPL_2026[8] + ((household_size - 8) * 5500))
    ratio = (income / base * 100) if base else 0.0
    likely_discount = "50-100%" if ratio <= 300 else "0-40%" if ratio <= 400 else "unlikely"

    is_nonprofit = None
    ownership = None
    if hospital:
        ownership = hospital.get("ownership")
        is_nonprofit = bool(hospital.get("is_nonprofit"))
        if is_nonprofit is False and ownership and ("nonprofit" in ownership.lower() or "non-profit" in ownership.lower()):
            is_nonprofit = True

    details = {
        "hospital_name": hospital.get("name") if hospital else hospital_name,
        "income": income,
        "household_size": household_size,
        "fpl_percent": round(ratio, 1),
        "estimated_discount": likely_discount,
        "hospital_found": bool(hospital),
        "ownership": ownership,
        "is_nonprofit": is_nonprofit,
    }

    if is_nonprofit is False:
        return ("for_profit", "Hospital appears to be for-profit; federal charity-care rules may not apply directly.", details)
    if ratio <= 400:
        return ("likely_eligible", f"Estimated household income is {ratio:.1f}% of FPL. You may qualify for assistance.", details)
    return ("may_not_qualify", f"Estimated household income is {ratio:.1f}% of FPL, above typical charity-care thresholds.", details)


def _run_dispute_letter_generator(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    patient = (payload.get("patient_name") or "[Your Name]").strip()
    hospital = (payload.get("hospital_name") or "[Hospital Name]").strip()
    account = (payload.get("account_number") or "[Account Number]").strip()
    dtype = (payload.get("dispute_type") or "billing_error").strip()
    notes = (payload.get("notes") or "").strip()

    focus = {
        "overcharge": "charges appear excessive vs Medicare benchmarks",
        "billing_error": "statement contains coding/billing inconsistencies",
        "financial_hardship": "bill imposes severe financial hardship",
        "insurance_denial": "insurance processing and responsibility require re-review",
    }.get(dtype, "charges require formal billing review")

    letter = (
        f"{date.today().isoformat()}\n\n"
        f"{patient}\n[Address]\n[Email/Phone]\n\n"
        f"Billing Department\n{hospital}\n\n"
        f"Re: Account {account}\n\n"
        f"Dear Billing Department,\n\n"
        f"I am requesting a formal review of my account because {focus}.\n"
        f"Please provide a corrected itemized statement, written explanation of all disputed charges, and pause collection activity while this review is pending.\n\n"
        f"Additional context: {notes or 'Please review all charges and insurance application details.'}\n\n"
        f"Please respond in writing within 30 days.\n\n"
        f"Sincerely,\n{patient}\n"
    )

    return ("generated", "Your dispute letter draft is ready.", {"letter": letter, "dispute_type": dtype})


def _run_surprise_bill_checker(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    emergency = (payload.get("emergency_care") or "unsure").strip().lower()
    in_network = (payload.get("facility_in_network") or "unsure").strip().lower()
    out_network_provider = (payload.get("provider_out_of_network") or "unsure").strip().lower()

    if emergency == "yes" and out_network_provider == "yes":
        return (
            "protected",
            "Scenario is likely covered by No Surprises protections (emergency + out-of-network provider).",
            {"emergency_care": emergency, "facility_in_network": in_network, "provider_out_of_network": out_network_provider},
        )
    if emergency == "no" and in_network == "no" and out_network_provider == "no":
        return (
            "not_protected",
            "This scenario does not look like a classic No Surprises protected case.",
            {"emergency_care": emergency, "facility_in_network": in_network, "provider_out_of_network": out_network_provider},
        )
    return (
        "unclear",
        "Additional details are needed to determine whether No Surprises Act protections apply.",
        {"emergency_care": emergency, "facility_in_network": in_network, "provider_out_of_network": out_network_provider},
    )


def _run_negotiation_script_generator(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    amount = _to_float(payload.get("bill_amount"))
    hospital_type = (payload.get("hospital_type") or "unknown").strip().replace("_", " ")
    insurance = (payload.get("insurance_status") or "insured").strip().replace("_", " ")

    script = (
        "Hello, I'm calling to request a billing review for my account.\n"
        f"My current balance is ${amount:,.2f}. I am a {insurance} patient and this is a {hospital_type} facility.\n"
        "I am requesting an itemized review, prompt-pay discount options, and any financial assistance eligibility review.\n"
        "Please note in my file that I am disputing potentially inflated charges and request written follow-up.\n"
    )
    return ("generated", "Negotiation script generated.", {"script": script})


def _run_procedure_cost_estimator(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    cpt = (payload.get("cpt_code") or "").strip().upper()
    zip_code = (payload.get("zip_code") or "").strip()
    lookup = _lookup_cpt(cpt, zip_code)
    if not lookup:
        return ("estimated", "No benchmark record found. Try another CPT code.", {"cpt_code": cpt, "zip_code": zip_code})

    benchmark = lookup.get("benchmark") or {}
    low = benchmark.get("p25_charged")
    high = benchmark.get("p75_charged")
    median = benchmark.get("median_charged")
    summary = (
        f"Fair range for CPT {cpt} is approximately ${low:,.0f}–${high:,.0f}."
        if low and high
        else f"Benchmark median for CPT {cpt} is approximately ${median:,.0f}."
        if median
        else f"Medicare reference rate for CPT {cpt} is ${_to_float(lookup.get('medicare_rate')):,.2f}."
    )
    return ("estimated", summary, {"lookup": lookup})


def _run_hospital_billing_grade_lookup(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    hospital_name = (payload.get("hospital_name") or "").strip()
    hospital = _hospital_by_name(hospital_name)
    if not hospital:
        return ("not_found", "No matching hospital found.", {"hospital_name": hospital_name})

    grade = (hospital.get("billing_grade") or "N/A").upper()
    state = "found_f" if grade == "F" else "found"
    return (state, f"{hospital.get('name')} has billing grade {grade}.", hospital)


def _run_good_faith_estimator(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    return _run_procedure_cost_estimator(payload)


def _run_debt_sol_checker(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    st = _resolve_state_code((payload.get("state") or "").strip())
    dos = (payload.get("date_of_service") or "").strip()
    if not st or st not in STATE_SOL_YEARS:
        return ("within_window", "State not recognized. Please enter a valid U.S. state.", {"state": payload.get("state")})

    years = STATE_SOL_YEARS[st]
    try:
        service_date = datetime.strptime(dos, "%Y-%m-%d").date()
    except Exception:
        service_date = date.today()

    elapsed_years = (date.today() - service_date).days / 365.25
    state_key = "expired" if elapsed_years > years else "within_window"
    summary = (
        f"In {st}, statute of limitations is typically {years} years; debt appears beyond that window."
        if state_key == "expired"
        else f"In {st}, statute of limitations is typically {years} years; debt appears within that window."
    )
    details = {
        "state": st,
        "statute_years": years,
        "date_of_service": service_date.isoformat(),
        "elapsed_years": round(elapsed_years, 2),
        "legal_disclaimer": "Informational only, not legal advice.",
        "last_updated": "2026-02-21",
    }
    return (state_key, summary, details)


def _run_debt_rights_checker(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    st = _resolve_state_code((payload.get("state") or "").strip()) or "N/A"
    in_collections = (payload.get("in_collections") or "unsure").strip().lower()
    in_30 = (payload.get("first_notice_within_30_days") or "unsure").strip().lower()

    rights = [
        "You can request debt validation within 30 days of first collector notice.",
        "Collectors must stop collection activity until validation is provided after timely request.",
        "Medical collections under current federal rules are typically not reported until at least 1 year old.",
    ]
    if in_collections == "yes":
        rights.append("You can send written cease-communication instructions under FDCPA limits.")
    if in_30 == "yes":
        rights.append("You are in the strongest validation request window right now.")
    rights.append(f"State selected: {st}. Check state-specific SOL before acknowledging debt.")

    return ("rights_summary", "Rights summary generated from your answers.", {"rights": rights, "state": st, "last_updated": "2026-02-21"})


def _run_debt_validation_generator(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    patient = (payload.get("patient_name") or "[Your Name]").strip()
    collector = (payload.get("collector_name") or "[Collector]").strip()
    account = (payload.get("account_number") or "[Account Number]").strip()
    notice = (payload.get("date_of_notice") or "[Notice Date]").strip()
    letter = (
        f"{date.today().isoformat()}\n\n"
        f"To: {collector}\n"
        f"Re: Debt Validation Request, Account {account}\n\n"
        f"I am writing in response to your notice dated {notice}. Under 15 U.S.C. § 1692g, I request full validation of this debt, including itemized statements, chain of assignment, and proof this account is legally collectible.\n"
        "Please cease collection activity until validation is provided.\n\n"
        f"Sincerely,\n{patient}\n"
    )
    return ("generated", "Debt validation letter generated.", {"letter": letter})


def _run_denial_appeal_generator(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    patient = (payload.get("patient_name") or "[Patient]").strip()
    insurer = (payload.get("insurance_company") or "[Insurance Company]").strip()
    code = (payload.get("denial_reason_code") or "UNKNOWN").strip().upper()
    procedure = (payload.get("procedure") or "the requested service").strip()
    denial_date = (payload.get("date_of_denial") or "").strip()

    reason = DENIAL_REASON_MAP.get(code, "Reason code not mapped; request full denial rationale and policy citation.")
    letter = (
        f"{date.today().isoformat()}\n\n"
        f"To: {insurer} Appeals Department\n"
        f"Re: Internal Appeal for denied claim ({code})\n\n"
        f"I am appealing denial code {code} for {procedure}.\n"
        f"Reasoning to address: {reason}\n"
        "Please provide full policy language, clinical rationale, and reprocess this claim.\n\n"
        f"Member: {patient}\n"
        f"Denial date: {denial_date or '[date]'}\n"
        "Note: Internal appeals are commonly due within 180 days of denial.\n"
    )
    return ("generated", "Insurance denial appeal letter generated.", {"letter": letter, "reason_mapping": reason})


def _run_eob_decoder(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    lines = _parse_items_json(payload)
    decoded: list[dict[str, Any]] = []
    discrepancies: list[str] = []

    for line in lines[:50]:
        billed = _to_float(line.get("billed_amount") or line.get("billed"))
        allowed = _to_float(line.get("allowed_amount") or line.get("allowed"))
        paid = _to_float(line.get("insurance_paid") or line.get("paid"))
        patient = _to_float(line.get("patient_owes") or line.get("patient_responsibility"))
        desc = (line.get("description") or line.get("cpt_code") or "line item").strip()

        reconciliation_gap = round(abs((paid + patient) - allowed), 2)
        if allowed > 0 and reconciliation_gap > 1:
            discrepancies.append(f"{desc}: paid + patient responsibility differs from allowed by ${reconciliation_gap:,.2f}.")

        decoded.append(
            {
                "description": desc,
                "billed": billed,
                "allowed": allowed,
                "insurance_paid": paid,
                "patient_owes": patient,
                "plain_english": f"Provider billed ${billed:,.2f}, insurer allowed ${allowed:,.2f}, insurance paid ${paid:,.2f}, patient owes ${patient:,.2f}.",
            }
        )

    return (
        "decoded",
        f"Decoded {len(decoded)} EOB line item(s).",
        {"decoded_items": decoded, "discrepancies": discrepancies},
    )


def _run_payment_plan_calculator(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    bill_amount = _to_float(payload.get("bill_amount"))
    monthly_budget = max(_to_float(payload.get("monthly_budget")), 1.0)
    apr = max(_to_float(payload.get("interest_rate")), 0.0) / 100.0

    if apr == 0:
        months = int((bill_amount + monthly_budget - 1) // monthly_budget)
        total_paid = round(months * monthly_budget, 2)
    else:
        monthly_rate = apr / 12
        balance = bill_amount
        months = 0
        total_paid = 0.0
        while balance > 0 and months < 1200:
            interest = balance * monthly_rate
            principal = monthly_budget - interest
            if principal <= 0:
                break
            balance -= principal
            total_paid += monthly_budget
            months += 1
        if balance > 0:
            months = 1200

    details = {
        "bill_amount": bill_amount,
        "monthly_budget": monthly_budget,
        "apr": round(apr * 100, 2),
        "months": months,
        "total_paid": round(total_paid, 2),
    }
    return ("calculated", f"At ${monthly_budget:,.2f}/month, payoff timeline is about {months} month(s).", details)


def _run_cpt_lookup(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    cpt = (payload.get("cpt_code") or "").strip().upper()
    zip_code = (payload.get("zip_code") or "").strip()
    lookup = _lookup_cpt(cpt, zip_code)
    if not lookup:
        return ("not_found", f"No benchmark entry found for CPT {cpt}.", {"cpt_code": cpt, "zip_code": zip_code})
    med = _to_float(lookup.get("medicare_rate"))
    return ("found", f"CPT {cpt} found. Medicare reference is ${med:,.2f}.", {"lookup": lookup})


def _run_medicare_rate_lookup(payload: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    cpt = (payload.get("cpt_code") or "").strip().upper()
    zip_code = (payload.get("zip_code") or "").strip()
    lookup = _lookup_cpt(cpt, zip_code)
    if not lookup or not lookup.get("medicare_rate"):
        return ("not_found", "No direct Medicare rate found for this query.", {"cpt_code": cpt, "zip_code": zip_code})
    med = _to_float(lookup.get("medicare_rate"))
    benchmark = lookup.get("benchmark") or {}
    median = _to_float(benchmark.get("median_charged"))
    multiple = round(median / med, 1) if med and median else None
    details = {"lookup": lookup, "average_charge_multiple": multiple}
    summary = f"Medicare rate for {cpt} in this locality is ${med:,.2f}."
    if multiple:
        summary += f" Typical billed charges are around {multiple}x that benchmark."
    return ("found", summary, details)
