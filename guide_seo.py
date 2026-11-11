"""Search titles and meta descriptions for guides.

Hand-written overrides for the core pages in the hospital-bill niche
(see reference/POSITIONING.md). Every other guide gets its own title,
with the brand suffix added only when it fits, and a meta description
trimmed at a sentence or word boundary.
"""

from __future__ import annotations

import html

import config

TITLE_MAX = config.SEO_TITLE_MAX_CHARS
META_MAX = config.SEO_META_MAX_CHARS
BRAND_SUFFIX = " | BillKarma"

# slug -> (title, meta description). Titles <= 60 chars, metas <= 155.
SEO_OVERRIDES = {
    "how-to-dispute-a-medical-bill": (
        "How to Dispute a Hospital Bill: 5 Steps + Free Letter",
        "Get the itemized bill, compare each charge to Medicare, then dispute in writing. "
        "Step-by-step guide with a free letter and the deadlines that matter.",
    ),
    "how-to-get-itemized-hospital-bill": (
        "How to Get an Itemized Hospital Bill (Free Letter)",
        "Hospitals must give you every charge and billing code if you ask. "
        "Use our free request letter, what to say on the phone, and what to check first.",
    ),
    "medical-bill-dispute-letter": (
        "Medical Bill Dispute Letter: Free Template That Works",
        "A fill-in dispute letter for hospital bills: wrong charges, duplicates, prices far above "
        "Medicare. What to include, where to send it and when to follow up.",
    ),
    "common-hospital-billing-errors": (
        "7 Common Hospital Billing Errors (and How to Spot Them)",
        "Duplicate lines, unbundled codes, wrong quantities, services you never got. "
        "How to find each error on an itemized bill and get it corrected.",
    ),
    "duplicate-charges-hospital-bills": (
        "Duplicate Charges on a Hospital Bill: How to Fix Them",
        "Billed twice for the same test or supply? How to confirm a duplicate on your itemized "
        "bill and get it removed, with a ready-to-send dispute letter.",
    ),
    "hospital-financial-assistance-charity-care": (
        "Hospital Charity Care: Do You Qualify? Income Limits",
        "Nonprofit hospitals must offer free or discounted care. See typical income limits, how to "
        "apply, and how to get a bill reduced even after it's sent.",
    ),
    "hospital-charity-care-by-state": (
        "Hospital Charity Care by State: Rules and Income Limits",
        "State-by-state rules for hospital financial assistance: who qualifies, how much is "
        "forgiven, and how to apply for help with a hospital bill.",
    ),
    "how-to-negotiate-medical-bills": (
        "How to Negotiate a Hospital Bill: Scripts That Work",
        "What to say to hospital billing, what to ask for, and the Medicare-rate number to "
        "anchor on. Word-for-word scripts for calls and letters.",
    ),
    "medical-bill-negotiation-script": (
        "Medical Bill Negotiation Script: Exactly What to Say",
        "A word-for-word phone script for hospital billing: asking for an itemized bill, "
        "disputing charges, prompt-pay discounts and payment plans.",
    ),
    "balance-billing": (
        "Balance Billing: When It's Illegal and How to Fight It",
        "Got a bill for the gap between what a provider charged and what insurance paid? "
        "When that's banned, when it isn't, and how to dispute it.",
    ),
    "no-surprises-act-explained": (
        "No Surprises Act: What It Covers and How to Use It",
        "Which surprise bills the federal law bans, what it doesn't cover, and how to dispute a "
        "bill that breaks it. ER, out-of-network and good faith estimates.",
    ),
    "why-emergency-room-bills-are-so-high": (
        "Why ER Bills Are So High (and How to Lower Yours)",
        "ER visit levels, facility fees and out-of-network doctors explain most of an ER bill. "
        "How to check each charge and dispute the ones that are wrong.",
    ),
    "uninsured-hospital-bill": (
        "Uninsured Hospital Bill? How to Cut It Down",
        "Uninsured patients are often billed full list price. Ask for financial assistance, "
        "a self-pay discount and an itemized bill. Here's how, step by step.",
    ),
    "debt-validation-letter-medical-debt": (
        "Medical Debt Validation Letter: Free Template",
        "Make a collector prove a medical debt is yours and the amount is right. Free letter, "
        "the 30-day window, and what the collector must do next.",
    ),
    "how-to-read-your-medical-bill": (
        "How to Read a Hospital Bill, Line by Line",
        "What every column on a hospital bill means: revenue codes, CPT codes, quantities, "
        "adjustments. Learn what to check before you pay.",
    ),
    "hospital-chargemaster-explained": (
        "Hospital Chargemaster: Why List Prices Are So High",
        "The chargemaster is a hospital's internal price list, often several times what Medicare "
        "pays. What it means for your bill and how to push back.",
    ),
    "observation-status-billing": (
        "Observation Status vs Inpatient: Why Your Bill Is Higher",
        "Observation stays are billed as outpatient, which can raise what you owe. "
        "How to tell which you had and how to challenge it.",
    ),
    "hospital-facility-fees-explained": (
        "Hospital Facility Fees: Why You Were Billed Twice",
        "A facility fee is charged on top of the doctor's bill at hospital-owned clinics. "
        "When it applies, typical amounts, and how to dispute one.",
    ),
    "cant-afford-medical-bill": (
        "Can't Afford a Hospital Bill? 7 Options Before Collections",
        "Financial assistance, payment plans, discounts and disputes: what to do, in order, "
        "before a hospital bill goes to collections.",
    ),
    "how-to-get-medical-bills-reduced": (
        "How to Get a Hospital Bill Reduced After Insurance",
        "Still owe a lot after insurance paid? Check for errors, compare to Medicare rates, "
        "ask for financial assistance and dispute in writing.",
    ),
    "medical-bill-audit-checklist": (
        "Hospital Bill Audit Checklist: 12 Things to Check",
        "A 12-point checklist to audit an itemized hospital bill yourself: duplicates, "
        "quantities, dates, codes and prices compared to Medicare.",
    ),
    "what-happens-if-you-dont-pay-medical-bills": (
        "What Happens If You Don't Pay a Hospital Bill?",
        "The timeline from first bill to collections, credit reporting and lawsuits, "
        "and what you can do at each stage to protect yourself.",
    ),
    "hospital-payment-plans": (
        "Hospital Payment Plans: How to Get 0% Interest",
        "Most hospitals offer interest-free payment plans if you ask. How to set one up, "
        "what monthly amount to ask for, and what to avoid.",
    ),
}


def _with_brand(title: str) -> str:
    branded = title + BRAND_SUFFIX
    return branded if len(branded) <= TITLE_MAX else title


def _trim(text: str, limit: int) -> str:
    """Cut at the last full sentence that fits, else the last word, never mid-word."""
    if len(text) <= limit:
        return text
    cut = text[:limit]
    sentence_end = cut.rfind(". ")
    if sentence_end >= limit // 2:
        return cut[: sentence_end + 1]
    return cut[: cut[: limit - 3].rfind(" ")] + "..."


def seo_title(guide: dict) -> str:
    override = SEO_OVERRIDES.get(guide.get("slug", ""))
    title = override[0] if override else html.unescape(guide["title"])
    return _with_brand(title)


def seo_description(guide: dict) -> str:
    override = SEO_OVERRIDES.get(guide.get("slug", ""))
    if override:
        return override[1]
    return _trim(html.unescape(guide.get("meta_description", "")), META_MAX)
