"""Quick Triage Quiz — 4 questions, personalized action plan with CTA."""

from __future__ import annotations


QUESTIONS = [
    {
        "id": "situation",
        "text": "What\u2019s going on with your medical bill?",
        "options": [
            {"value": "got_bill", "label": "I got a bill I think is too high"},
            {"value": "collections", "label": "My bill went to collections"},
            {"value": "cant_afford", "label": "I can\u2019t afford to pay"},
            {"value": "denied", "label": "My insurance denied a claim"},
        ],
    },
    {
        "id": "amount",
        "text": "How much is the bill?",
        "options": [
            {"value": "under_500", "label": "Under $500"},
            {"value": "500_2000", "label": "$500 \u2013 $2,000"},
            {"value": "2000_10000", "label": "$2,000 \u2013 $10,000"},
            {"value": "over_10000", "label": "Over $10,000"},
        ],
    },
    {
        "id": "insurance",
        "text": "What\u2019s your insurance situation?",
        "options": [
            {"value": "insured", "label": "Insured (in-network)"},
            {"value": "oon", "label": "Insured (out-of-network)"},
            {"value": "uninsured", "label": "Uninsured / self-pay"},
            {"value": "medicare", "label": "Medicare or Medicaid"},
        ],
    },
    {
        "id": "timing",
        "text": "When did you receive this bill?",
        "options": [
            {"value": "this_week", "label": "This week"},
            {"value": "this_month", "label": "Within the last month"},
            {"value": "few_months", "label": "1\u20136 months ago"},
            {"value": "over_6", "label": "Over 6 months ago"},
        ],
    },
]


def get_recommendation(answers: dict) -> dict:
    """Return a personalized recommendation based on quiz answers."""
    situation = answers.get("situation", "")
    amount = answers.get("amount", "")
    insurance = answers.get("insurance", "")
    timing = answers.get("timing", "")

    actions = []
    headline = ""
    urgency = ""

    # Collections path
    if situation == "collections":
        headline = "You have strong legal protections. Here\u2019s your plan."
        if timing in ("this_week", "this_month"):
            urgency = "Act now \u2014 you have 30 days from first contact for the strongest FDCPA protections."
        actions.append({
            "title": "Send a debt validation letter",
            "description": "Force the collector to prove they own the debt and the amount is correct. They must stop collecting until they respond.",
            "impact": "high",
            "url": "/collection-notice",
            "button": "Generate FDCPA Letter",
            "price": "$19 via certified mail",
        })
        actions.append({
            "title": "Check statute of limitations",
            "description": "If the debt is past your state\u2019s SOL, collectors generally cannot sue you.",
            "impact": "high",
            "url": "/statute-of-limitations",
            "button": "Check SOL \u2014 Free",
            "price": "Free",
        })
        if amount in ("2000_10000", "over_10000"):
            actions.append({
                "title": "Negotiate a settlement",
                "description": "Collectors often accept 20\u201350 cents on the dollar, especially for older debts.",
                "impact": "high",
                "url": "/settle-debt",
                "button": "Generate Settlement Offer",
                "price": "$9",
            })
        actions.append({
            "title": "Scan the original bill for errors",
            "description": "If the underlying bill has errors, the debt amount may be wrong. Dispute the original charges.",
            "impact": "medium",
            "url": "/scan",
            "button": "Scan Bill \u2014 Free",
            "price": "Free",
        })

    # Can't afford path
    elif situation == "cant_afford":
        headline = "You may qualify for bill forgiveness or major discounts."
        actions.append({
            "title": "Check charity care eligibility",
            "description": "Most nonprofit hospitals must forgive bills for lower-income patients. You can apply even after collections.",
            "impact": "high",
            "url": "/charity-care",
            "button": "Check Eligibility \u2014 Free",
            "price": "Free",
        })
        if insurance == "uninsured":
            actions.append({
                "title": "Request the self-pay / cash rate",
                "description": "Hospitals must offer uninsured patients a discount. These are often 40\u201360% below the billed amount.",
                "impact": "high",
                "url": "/guides/hospital-cash-pay-rates",
                "button": "Learn How",
                "price": "Free",
            })
        actions.append({
            "title": "Scan your bill for overcharges",
            "description": "Reduce the amount before negotiating. Billing errors are found in 80% of hospital bills.",
            "impact": "high",
            "url": "/scan",
            "button": "Scan Bill \u2014 Free",
            "price": "Free",
        })
        actions.append({
            "title": "Set up a payment plan",
            "description": "Most hospitals offer interest-free payment plans. Use our calculator to plan your payments.",
            "impact": "medium",
            "url": "/tools/medical-bill-payment-plan-calculator/",
            "button": "Calculate Payments",
            "price": "Free",
        })

    # Insurance denied path
    elif situation == "denied":
        headline = "Insurance denials can be appealed \u2014 and often overturned."
        if timing in ("this_week", "this_month"):
            urgency = "Internal appeals are typically due within 180 days of denial. Start now."
        actions.append({
            "title": "Generate an appeal letter",
            "description": "We create a denial-code-specific appeal letter with the right language and legal citations.",
            "impact": "high",
            "url": "/tools/insurance-denial-appeal-letter-generator/",
            "button": "Generate Appeal Letter",
            "price": "Free",
        })
        if insurance == "oon":
            actions.append({
                "title": "Check No Surprises Act protections",
                "description": "If this was emergency care or at an in-network facility, federal law may cap your costs.",
                "impact": "high",
                "url": "/tools/surprise-bill-checker/",
                "button": "Check Protections",
                "price": "Free",
            })
        actions.append({
            "title": "Scan the bill for errors",
            "description": "Coding errors can cause denials. Fix the code, resubmit the claim.",
            "impact": "medium",
            "url": "/scan",
            "button": "Scan Bill \u2014 Free",
            "price": "Free",
        })

    # Got a bill (default / most common)
    else:
        headline = "Let\u2019s find out if you\u2019re being overcharged."
        actions.append({
            "title": "Scan your bill for errors",
            "description": "Our AI checks every charge against Medicare rates and flags duplicates, unbundling, upcoding, and overcharges.",
            "impact": "high",
            "url": "/scan",
            "button": "Scan My Bill \u2014 Free",
            "price": "Free",
        })
        if amount in ("2000_10000", "over_10000"):
            actions.append({
                "title": "Estimate your savings",
                "description": "Get an instant estimate of how much you could save based on your hospital\u2019s billing data.",
                "impact": "high",
                "url": "/estimate",
                "button": "Estimate Savings \u2014 Free",
                "price": "Free",
            })
        if insurance == "oon":
            actions.append({
                "title": "Check No Surprises Act protections",
                "description": "Out-of-network? Federal law may cap what you owe for emergency care.",
                "impact": "high",
                "url": "/tools/surprise-bill-checker/",
                "button": "Check Protections",
                "price": "Free",
            })
        if insurance == "uninsured":
            actions.append({
                "title": "Check charity care eligibility",
                "description": "Nonprofit hospitals must offer financial assistance. You may qualify for 50\u2013100% off.",
                "impact": "high",
                "url": "/charity-care",
                "button": "Check Eligibility \u2014 Free",
                "price": "Free",
            })
        actions.append({
            "title": "Look up your hospital\u2019s billing grade",
            "description": "See how your hospital\u2019s prices compare to Medicare benchmarks.",
            "impact": "medium",
            "url": "/hospitals/",
            "button": "Find Hospital",
            "price": "Free",
        })

    return {
        "headline": headline,
        "urgency": urgency,
        "actions": actions,
        "situation": situation,
        "amount": amount,
        "insurance": insurance,
        "timing": timing,
    }
