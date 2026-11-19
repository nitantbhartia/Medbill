"""Why each rule flags a charge: what kind of evidence it is, a plain sentence, and the public source.

kind: "official" = a public dataset or federal rule, "bill" = printed on the user's own bill or EOB,
"check" = a BillKarma heuristic (worth asking about, not proof)."""

from __future__ import annotations

import config

CMS_PFS_URL = "https://www.cms.gov/medicare/payment/fee-schedules/physician"
CMS_OPPS_URL = "https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient/addendum-a-b-updates"
CMS_NCCI_URL = "https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits"
CMS_BILL_RIGHTS_URL = "https://www.cms.gov/medical-bill-rights"

# explanation uses the values in `needs`; fallback is used when any of them is missing.
RULES = {
    "RULE_QUANTITY_OVER_MUE": {
        "kind": "official",
        "explanation": "Medicare's limit for code {code} is {limit} per day; you were billed {quantity}.",
        "needs": ("code", "limit", "quantity"),
        "fallback": "Medicare publishes a daily limit for this code, and this bill is over it.",
        "source_name": "CMS medically unlikely edits",
        "source_url": "https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medically-unlikely-edits",
        "source_year": lambda: None,
    },
    "RULE_INSURER_CONTRACTED_RATE": {
        "kind": "official",
        "explanation": "{insurer}'s contracted rate at {hospital} for code {code} is {rate}. You were charged {charged}.",
        "needs": ("insurer", "hospital", "code", "rate", "charged"),
        "fallback": "Your insurer's contracted rate at this hospital, from the hospital's own price file, is below what this bill asks.",
        "source_name": "Hospital price transparency file",
        "source_url": "https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency",
        "source_year": lambda: None,
    },
    "RULE_MARKUP_VS_MEDICARE": {
        "kind": "official",
        "explanation": "Medicare pays {medicare} for code {code}. This bill charges {charged}, which is {markup}× that.",
        "needs": ("medicare", "code", "charged", "markup"),
        "fallback": "Medicare's published price for this service is far below what this bill charges.",
        "source_name": "CMS Medicare Physician Fee Schedule",
        "source_url": CMS_PFS_URL,
        "source_year": lambda: config.MEDICARE_PFS_YEAR,
    },
    "RULE_NCCI_UNBUNDLING": {
        "kind": "official",
        "explanation": "Medicare's coding edits pay {code} and {other} as one service. Billing both separately is usually not allowed.",
        "needs": ("code", "other"),
        "fallback": "Medicare's coding edits pay these codes as one service. Billing both separately is usually not allowed.",
        "source_name": "CMS NCCI edits",
        "source_url": CMS_NCCI_URL,
        "source_year": lambda: config.NCCI_EDITS_VERSION,
    },
    "RULE_NO_SURPRISES_ACT_HEURISTIC": {
        "kind": "official",
        "explanation": "Out-of-network emergency care is generally billed at in-network cost sharing under federal law.",
        "needs": (),
        "fallback": "",
        "source_name": "CMS: Your medical bill rights",
        "source_url": CMS_BILL_RIGHTS_URL,
        "source_year": lambda: None,
    },
    "RULE_DUPLICATE_SAME_CODE_DATE_AMOUNT": {
        "kind": "bill",
        "explanation": "The same code, date and amount appear {times} times on this bill.",
        "needs": ("times",),
        "fallback": "The same code, date and amount appear more than once on this bill.",
        "source_name": "Your bill",
    },
    "RULE_EOB_RECONCILIATION": {
        "kind": "bill",
        "explanation": "Your insurance statement doesn't match what this bill asks you to pay.",
        "needs": (),
        "fallback": "",
        "source_name": "Your insurance statement",
    },
    "RULE_ER_LEVEL_UPCODING_HEURISTIC": {
        "kind": "check",
        "explanation": "The highest emergency visit level is for the most severe cases. Ask for the records that support it.",
        "needs": (),
        "fallback": "",
        "source_name": "BillKarma check",
    },
    "RULE_HIGH_QUANTITY_CHECK": {
        "kind": "check",
        "explanation": "A quantity of {quantity} is unusually high for this code.",
        "needs": ("quantity",),
        "fallback": "The quantity billed is unusually high for this code.",
        "source_name": "BillKarma check",
    },
    "RULE_REGIONAL_BENCHMARK_OUTLIER": {
        "kind": "check",
        "explanation": "Above the typical charge in your region.",
        "needs": (),
        "fallback": "",
        "source_name": "BillKarma check",
    },
}


def _dollars(amount) -> str | None:
    return f"${float(amount):,.0f}" if amount else None


def _values(details: dict) -> dict:
    item = details.get("line_item") or {}
    related = details.get("related_items") or []
    quantity = item.get("quantity")
    return {
        "code": item.get("cpt_code"),
        "medicare": _dollars(details.get("medicare_rate")),
        "charged": _dollars(item.get("charged_amount")),
        "markup": details.get("markup_multiple"),
        "other": related[0].get("cpt_code") if related and isinstance(related[0], dict) else None,
        "times": len(details["duplicate_of"]) + 1 if details.get("duplicate_of") else None,
        "quantity": quantity if isinstance(quantity, (int, float)) and quantity > 1 else None,
        "limit": details.get("mue_limit"),
        "insurer": details.get("insurer"),
        "hospital": details.get("hospital_name"),
        "rate": _dollars(details.get("contracted_rate")),
    }


def basis_for(rule_id: str | None, details: dict) -> dict | None:
    """The evidence behind one finding, or None for a rule we have no source for."""
    rule = RULES.get(rule_id or "")
    if not rule:
        return None
    values = _values(details)
    complete = all(values[name] is not None for name in rule["needs"])
    text = rule["explanation"].format(**values) if complete else rule["fallback"]
    year = details.get("rate_year") or details.get("source_version") if rule_id in ("RULE_INSURER_CONTRACTED_RATE", "RULE_QUANTITY_OVER_MUE") \
        else (rule["source_year"]() if "source_year" in rule else None)
    basis = {"kind": rule["kind"], "rule_id": rule_id, "explanation": text,
             "source_name": rule["source_name"], "source_url": (details.get("rate_source_url") if rule_id == "RULE_INSURER_CONTRACTED_RATE" else None) or rule.get("source_url")}
    if year:
        basis["source_year"] = year
    return basis


# What a hospital may legitimately say about a flagged charge, and what to say back. Fixed text, never written by a model.
HOSPITAL_REPLIES = {
    "different_time_or_room": {
        "may_say": "The two charges were for separate visits, times or rooms.",
        "say_back": "Please send the record showing the separate times or rooms, and the time each was ordered.",
    },
    "different_revenue_code": {
        "may_say": "The two lines are for different departments, so they are not the same charge.",
        "say_back": "Please explain what each line is for and send the itemized bill that shows the department for each.",
    },
    "allowed_modifier": {
        "may_say": "A modifier on the bill shows these two services were separate.",
        "say_back": "Please send the documentation that shows these services were done separately, not as one procedure.",
    },
    "different_dates_or_providers": {
        "may_say": "These services were on different dates or by different providers.",
        "say_back": "Please send the record showing the date and provider for each service.",
    },
    "drug_or_supply": {
        "may_say": "Drugs and supplies are priced by the hospital's own pharmacy and supply list, not by Medicare's physician rates.",
        "say_back": "Please send the itemized price for this drug or supply and say how the price was set.",
    },
}


def reply_for(reason: str | None) -> dict | None:
    return HOSPITAL_REPLIES.get(reason or "")
