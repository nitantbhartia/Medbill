from __future__ import annotations

from typing import Any


TOOLS: list[dict[str, Any]] = [
    {
        "slug": "medical-bill-error-checker",
        "title": "Medical Bill Error Checker",
        "category": "High Intent",
        "description": "Check CPT charges against Medicare rates and flag likely billing issues.",
        "keywords": ["check medical bill for errors", "medical bill audit", "hospital bill errors"],
        "inline_nudge": "Tip: Most people don't have CPT codes handy. Upload your full bill and our AI extracts them automatically.",
        "primary_input_hint": "Enter CPT lines as JSON array: [{\"cpt_code\":\"99285\",\"charged_amount\":4500,\"date_of_service\":\"2026-01-10\",\"quantity\":1}]",
        "form_fields": [
            {"name": "zip_code", "label": "ZIP code", "type": "text", "placeholder": "e.g. 10001"},
            {"name": "line_items_json", "label": "Bill line items (JSON)", "type": "textarea", "rows": 7},
        ],
        "lead_magnet": {
            "key": "audit_checklist",
            "title": "Get our free Medical Bill Audit Checklist",
            "description": "7 things to check before you pay any hospital bill.",
            "button_label": "Send Me the Checklist",
        },
        "ctas": {
            "issues_found": {
                "headline": "We found potential billing errors totaling meaningful overcharges.",
                "body": "This is based on the codes you entered. A full bill audit also checks unbundling, duplicate charges, and financial assistance eligibility.",
                "primary_label": "Upload My Bill - Free Audit",
                "primary_url": "/scan",
                "secondary_label": "Upload My Bill Instead",
                "secondary_url": "/scan",
                "footnote": "Free audit. $29-149 to fight it. No savings? Full refund.",
            },
            "none_found": {
                "headline": "No obvious coding errors found based on the codes you entered.",
                "body": "Coding errors are only one type of overcharge. Upload your full bill and our AI also checks for prices above published rates, assistance eligibility, and No Surprises Act violations.",
                "primary_label": "Upload My Bill for a Full Audit - Free",
                "primary_url": "/scan",
                "footnote": "Free audit. $29-149 to fight it. No savings? Full refund.",
            },
        },
    },
    {
        "slug": "hospital-financial-assistance-calculator",
        "title": "Hospital Financial Assistance Eligibility Calculator",
        "category": "High Intent",
        "description": "Estimate charity care eligibility using income, household size, and hospital status.",
        "keywords": ["hospital charity care eligibility", "501r financial assistance", "hospital bill forgiveness"],
        "inline_nudge": "Did you know? Over 50% of Americans may qualify for some hospital financial assistance and never apply.",
        "form_fields": [
            {"name": "hospital_name", "label": "Hospital name", "type": "text", "placeholder": "e.g. Memorial Regional Hospital"},
            {"name": "income", "label": "Annual household income", "type": "number", "placeholder": "e.g. 52000"},
            {"name": "household_size", "label": "Household size", "type": "number", "placeholder": "e.g. 3"},
        ],
        "lead_magnet": {
            "key": "charity_care_guide",
            "title": "Free guide: How to Apply for Hospital Financial Assistance (Step by Step)",
            "description": "Includes sample application, required documents checklist, and what to say.",
            "button_label": "Send Me the Guide",
        },
        "ctas": {
            "likely_eligible": {
                "headline": "Good news - you likely qualify for financial assistance.",
                "body": "You could receive 50-100% off your bill. We handle the entire application, dispute overcharges, and follow up until resolved.",
                "primary_label": "Upload My Bill - We'll File for You",
                "primary_url": "/scan",
                "footnote": "Free audit. $29-149 to fight it. No savings? Full refund.",
            },
            "may_not_qualify": {
                "headline": "You may not qualify for financial assistance based on standard thresholds.",
                "body": "That does not mean you should pay full price. Hospitals often overcharge versus Medicare rates.",
                "primary_label": "Upload My Bill - See What You Actually Owe",
                "primary_url": "/scan",
                "footnote": "Free audit. $29-149 to fight it. No savings? Full refund.",
            },
            "for_profit": {
                "headline": "This appears to be a for-profit hospital and not required to offer 501(r) charity care.",
                "body": "You still have options: dispute billing errors, request prompt-pay discounts, and negotiate.",
                "primary_label": "Upload My Bill - Find Your Overcharges",
                "primary_url": "/scan",
                "footnote": "Free audit. $29-149 to fight it. No savings? Full refund.",
            },
        },
    },
    {
        "slug": "medical-bill-dispute-letter-generator",
        "title": "Medical Bill Dispute Letter Generator",
        "category": "High Intent",
        "description": "Generate a professional dispute letter for billing errors, hardship, or denial issues.",
        "keywords": ["medical bill dispute letter template", "hospital bill negotiation letter"],
        "inline_nudge": "Writing the dispute letter is step 1. Follow-ups are where most people stall.",
        "form_fields": [
            {"name": "patient_name", "label": "Your name", "type": "text"},
            {"name": "hospital_name", "label": "Hospital name", "type": "text"},
            {"name": "account_number", "label": "Account number", "type": "text"},
            {"name": "dispute_type", "label": "Dispute type", "type": "select", "options": ["overcharge", "billing_error", "financial_hardship", "insurance_denial"]},
            {"name": "notes", "label": "Context", "type": "textarea", "rows": 5},
        ],
        "lead_magnet": {
            "key": "followup_templates",
            "title": "Get our follow-up email templates",
            "description": "What to send at day 7, 14, and 30 if the hospital does not respond.",
            "button_label": "Send Me the Templates",
        },
        "ctas": {
            "generated": {
                "headline": "Your dispute letter is ready.",
                "body": "What happens next matters more than the letter itself. Want us to send this and handle day 7, 14, 30, and 45 follow-ups?",
                "primary_label": "Upload My Bill - We Handle Everything",
                "primary_url": "/scan",
                "secondary_label": "Upload My Bill for a Stronger Dispute",
                "secondary_url": "/scan",
                "footnote": "$29-149 flat fee. No savings in 45 days? Full refund.",
            }
        },
    },
    {
        "slug": "surprise-bill-checker",
        "title": "Surprise Bill Checker (No Surprises Act)",
        "category": "High Intent",
        "description": "Check if your situation is likely protected under federal No Surprises Act rules.",
        "keywords": ["no surprises act", "surprise medical bill", "balance billing"],
        "inline_nudge": "Answer a few questions to see if your bill may violate federal protections.",
        "form_fields": [
            {"name": "emergency_care", "label": "Was this emergency care?", "type": "select", "options": ["yes", "no", "unsure"]},
            {"name": "facility_in_network", "label": "Was the facility in-network?", "type": "select", "options": ["yes", "no", "unsure"]},
            {"name": "provider_out_of_network", "label": "Was provider out-of-network?", "type": "select", "options": ["yes", "no", "unsure"]},
        ],
        "lead_magnet": {
            "key": "nsa_guide",
            "title": "Know Your Rights: The Complete Guide to the No Surprises Act",
            "description": "What is covered, what is not, and exactly how to file a dispute.",
            "button_label": "Send Me the Guide",
        },
        "ctas": {
            "protected": {
                "headline": "Your bill is likely protected under the No Surprises Act.",
                "body": "If you are being billed above in-network cost-sharing, this may be illegal. We can file the dispute on your behalf.",
                "primary_label": "Upload My Bill - File a No Surprises Act Dispute",
                "primary_url": "/scan",
                "footnote": "Free audit. $29-149 to fight it. No savings? Full refund.",
            },
            "not_protected": {
                "headline": "Your situation may not fall under the No Surprises Act.",
                "body": "That does not mean the bill is fair. We can still check for overcharges, coding errors, and assistance eligibility.",
                "primary_label": "Upload My Bill - Free Audit",
                "primary_url": "/scan",
                "footnote": "Free audit. $29-149 to fight it. No savings? Full refund.",
            },
            "unclear": {
                "headline": "We cannot determine eligibility from the information provided.",
                "body": "Upload your full bill and EOB and we will analyze No Surprises Act applicability and alternatives.",
                "primary_label": "Upload My Bill - We'll Figure It Out",
                "primary_url": "/scan",
                "footnote": "Free audit. $29-149 to fight it. No savings? Full refund.",
            },
        },
    },
    {
        "slug": "medical-bill-negotiation-script-generator",
        "title": "Medical Bill Negotiation Script Generator",
        "category": "High Intent",
        "description": "Generate negotiation scripts for phone or written billing conversations.",
        "keywords": ["how to negotiate hospital bill", "medical bill negotiation script"],
        "inline_nudge": "Don't want to make the call? We can handle dispute follow-ups in writing.",
        "form_fields": [
            {"name": "bill_amount", "label": "Bill amount", "type": "number"},
            {"name": "hospital_type", "label": "Hospital type", "type": "select", "options": ["nonprofit", "for_profit", "government", "unknown"]},
            {"name": "insurance_status", "label": "Insurance status", "type": "select", "options": ["insured", "uninsured", "out_of_network"]},
        ],
        "lead_magnet": {
            "key": "negotiation_phrases",
            "title": "Negotiation cheat sheet",
            "description": "The 5 phrases that actually work when calling hospital billing departments.",
            "button_label": "Send Me the Cheat Sheet",
        },
        "ctas": {
            "generated": {
                "headline": "Your negotiation script is ready.",
                "body": "Hate making that call? Upload your bill and we handle the dispute in writing with formal follow-ups.",
                "primary_label": "Upload My Bill - Skip the Phone Call",
                "primary_url": "/scan",
                "footnote": "$29-149. No savings? Full refund. Zero phone calls required from you.",
            }
        },
    },
    {
        "slug": "procedure-cost-estimator",
        "title": "Procedure Cost Estimator",
        "category": "Research",
        "description": "Estimate fair pricing ranges for procedures by CPT and ZIP.",
        "keywords": ["how much does procedure cost", "cost without insurance"],
        "inline_nudge": "Already had this procedure? Compare your bill against fair range before paying.",
        "form_fields": [
            {"name": "cpt_code", "label": "CPT code", "type": "text"},
            {"name": "zip_code", "label": "ZIP code", "type": "text"},
        ],
        "lead_magnet": {
            "key": "preprocedure_checklist",
            "title": "Pre-procedure checklist",
            "description": "5 questions to ask before any medical procedure to protect yourself from overcharges.",
            "button_label": "Send Me the Checklist",
        },
        "ctas": {
            "estimated": {
                "headline": "Based on our data, your fair price estimate range is ready.",
                "body": "Already had the procedure? Compare your actual bill to this estimate to evaluate dispute grounds.",
                "primary_label": "Upload My Bill - Compare to Fair Price",
                "primary_url": "/scan",
            }
        },
    },
    {
        "slug": "hospital-billing-grade-lookup",
        "title": "Hospital Billing Grade Lookup",
        "category": "Research",
        "description": "Find a hospital's billing grade and markup vs Medicare.",
        "keywords": ["hospital billing grade", "does hospital overcharge"],
        "inline_nudge": "Hospitals with poor grades can still be disputed line-by-line.",
        "form_fields": [{"name": "hospital_name", "label": "Hospital name", "type": "text"}],
        "lead_magnet": {
            "key": "hospital_grade_explainer",
            "title": "Hospital billing grade explainer",
            "description": "How billing grades and markup ratios are calculated.",
            "button_label": "Send Me the Guide",
        },
        "ctas": {
            "found_f": {
                "headline": "This hospital has an F billing grade.",
                "body": "Predatory pricing above 8x Medicare rates can indicate strong overcharge risk.",
                "primary_label": "Upload My Bill - See Your Overcharges",
                "primary_url": "/scan",
            },
            "found": {
                "headline": "Hospital billing grade found.",
                "body": "Upload your bill and we'll identify every overcharge tied to your statement.",
                "primary_label": "Upload My Bill - Free Audit",
                "primary_url": "/scan",
            },
            "not_found": {
                "headline": "No direct hospital match found.",
                "body": "Upload your bill anyway and we'll audit charges independent of directory lookup.",
                "primary_label": "Upload My Bill - Free Audit",
                "primary_url": "/scan",
            },
        },
    },
    {
        "slug": "good-faith-estimate-calculator",
        "title": "Good Faith Estimate Calculator",
        "category": "Research",
        "description": "Estimate expected costs and compare to your actual bill.",
        "keywords": ["good faith estimate", "estimate medical costs before surgery"],
        "inline_nudge": "If final bill is $400+ above estimate, you may have a dispute pathway.",
        "form_fields": [
            {"name": "cpt_code", "label": "Procedure CPT code", "type": "text"},
            {"name": "zip_code", "label": "ZIP code", "type": "text"},
        ],
        "lead_magnet": {
            "key": "gfe_checklist",
            "title": "Pre-procedure checklist",
            "description": "Questions and documentation to request before care.",
            "button_label": "Send Me the Checklist",
        },
        "ctas": {
            "estimated": {
                "headline": "Your estimate range is ready.",
                "body": "If your final bill is $400+ above estimate, you may have a dispute option.",
                "primary_label": "Upload My Bill - Compare to Fair Price",
                "primary_url": "/scan",
            }
        },
    },
    {
        "slug": "medical-debt-statute-of-limitations-checker",
        "title": "Medical Debt Statute of Limitations Checker",
        "category": "Debt/Collections",
        "description": "Check debt collection lawsuit windows by state.",
        "keywords": ["medical debt statute of limitations", "how long can they collect"],
        "inline_nudge": "Statute timelines vary by state and debt type; this is informational only.",
        "form_fields": [
            {"name": "state", "label": "State (name or 2-letter code)", "type": "text"},
            {"name": "date_of_service", "label": "Date of service", "type": "date"},
        ],
        "lead_magnet": {
            "key": "state_debt_guide",
            "title": "State-by-state medical debt guide",
            "description": "Statutes of limitations, credit reporting rules, and your rights in your state.",
            "button_label": "Send Me My State Guide",
        },
        "ctas": {
            "within_window": {
                "headline": "Debt appears within the collection lawsuit window.",
                "body": "You can still dispute original charges and request documentation.",
                "primary_label": "Upload My Bill - Check for Errors",
                "primary_url": "/scan",
            },
            "expired": {
                "headline": "Debt may be outside the statute of limitations.",
                "body": "Collectors may still contact you, but legal options may be limited.",
                "primary_label": "Upload My Bill",
                "primary_url": "/scan",
                "secondary_label": "Download Cease & Desist Letter Template",
                "secondary_url": "#results",
            },
        },
    },
    {
        "slug": "medical-debt-rights-checker",
        "title": "Medical Debt Rights Checker",
        "category": "Debt/Collections",
        "description": "Get a personalized rights summary for your debt stage.",
        "keywords": ["medical debt credit report", "medical bill collections rights"],
        "inline_nudge": "Knowing rights is step 1. Enforcing them is step 2.",
        "form_fields": [
            {"name": "state", "label": "State", "type": "text"},
            {"name": "in_collections", "label": "In collections?", "type": "select", "options": ["yes", "no", "unsure"]},
            {"name": "first_notice_within_30_days", "label": "First collector notice within 30 days?", "type": "select", "options": ["yes", "no", "unsure"]},
        ],
        "lead_magnet": {
            "key": "state_debt_guide",
            "title": "Know Your Rights: Medical Debt Guide",
            "description": "Federal and state rights summary.",
            "button_label": "Send Me the Guide",
        },
        "ctas": {
            "rights_summary": {
                "headline": "Your rights summary is ready.",
                "body": "Upload your bill and we'll apply these rights in formal dispute letters.",
                "primary_label": "Upload My Bill - Exercise Your Rights",
                "primary_url": "/scan",
            }
        },
    },
    {
        "slug": "debt-validation-letter-generator",
        "title": "Debt Validation Letter Generator",
        "category": "Debt/Collections",
        "description": "Generate an FDCPA debt validation request letter.",
        "keywords": ["debt validation letter medical", "medical debt dispute letter"],
        "inline_nudge": "Send within 30 days of first collection contact for strongest protections.",
        "form_fields": [
            {"name": "patient_name", "label": "Your name", "type": "text"},
            {"name": "collector_name", "label": "Collection agency", "type": "text"},
            {"name": "account_number", "label": "Account/reference number", "type": "text"},
            {"name": "date_of_notice", "label": "Date of collector notice", "type": "date"},
        ],
        "lead_magnet": {
            "key": "debt_response_pack",
            "title": "Debt response pack",
            "description": "Validation, cease-contact, and dispute templates.",
            "button_label": "Send Me the Templates",
        },
        "ctas": {
            "generated": {
                "headline": "Debt validation letter generated.",
                "body": "While validation is pending, audit the original bill for billing errors.",
                "primary_label": "Upload My Bill - Audit the Original Charges",
                "primary_url": "/scan",
            }
        },
    },
    {
        "slug": "insurance-denial-appeal-letter-generator",
        "title": "Insurance Denial Appeal Letter Generator",
        "category": "Insurance Issues",
        "description": "Generate a denial appeal letter with reason-code-specific language.",
        "keywords": ["insurance denial appeal letter", "claim denied template"],
        "inline_nudge": "Important: internal appeals usually have a 180-day filing deadline.",
        "form_fields": [
            {"name": "patient_name", "label": "Your name", "type": "text"},
            {"name": "insurance_company", "label": "Insurance company", "type": "text"},
            {"name": "denial_reason_code", "label": "Denial reason code", "type": "text"},
            {"name": "procedure", "label": "Procedure/service", "type": "text"},
            {"name": "date_of_denial", "label": "Denial date", "type": "date"},
        ],
        "lead_magnet": {
            "key": "appeal_kit",
            "title": "Insurance Denial Appeal Kit",
            "description": "Deadline tracker, required documents checklist, and sample letters.",
            "button_label": "Send Me the Kit",
        },
        "ctas": {
            "generated": {
                "headline": "Appeal letter generated.",
                "body": "Important: internal appeals are commonly due within 180 days from denial date.",
                "primary_label": "Upload My Bill & Denial Letter - We Handle the Appeal",
                "primary_url": "/scan",
                "footnote": "$29-149. No savings? Full refund.",
            }
        },
    },
    {
        "slug": "eob-decoder",
        "title": "EOB Decoder",
        "category": "Insurance Issues",
        "description": "Decode EOB line items into plain-English payment breakdowns.",
        "keywords": ["how to read EOB", "explanation of benefits explained"],
        "inline_nudge": "If billed amounts and EOB responsibility do not align, dispute before paying.",
        "form_fields": [
            {"name": "line_items_json", "label": "EOB lines (JSON)", "type": "textarea", "rows": 7},
        ],
        "lead_magnet": {
            "key": "eob_quick_guide",
            "title": "EOB quick guide",
            "description": "How to validate what you owe and why.",
            "button_label": "Send Me the Guide",
        },
        "ctas": {
            "decoded": {
                "headline": "Your EOB has been decoded.",
                "body": "See something off? Upload your full bill and we'll cross-check every line.",
                "primary_label": "Upload My Bill - Full Audit",
                "primary_url": "/scan",
            }
        },
    },
    {
        "slug": "medical-bill-payment-plan-calculator",
        "title": "Medical Bill Payment Plan Calculator",
        "category": "Quick Calculators",
        "description": "Estimate payoff timeline based on bill amount and monthly budget.",
        "keywords": ["medical bill payment plan", "hospital payment plan calculator"],
        "inline_nudge": "Before committing to payments, validate whether the bill itself is correct.",
        "form_fields": [
            {"name": "bill_amount", "label": "Bill amount", "type": "number"},
            {"name": "monthly_budget", "label": "Monthly payment budget", "type": "number"},
            {"name": "interest_rate", "label": "APR % (optional)", "type": "number", "placeholder": "0"},
        ],
        "lead_magnet": {
            "key": "payment_plan_playbook",
            "title": "Payment plan playbook",
            "description": "How to avoid locking in overcharges before committing to monthly payments.",
            "button_label": "Send Me the Guide",
        },
        "ctas": {
            "calculated": {
                "headline": "Payment timeline calculated.",
                "body": "Before signing a plan, check if the bill is inflated.",
                "primary_label": "Upload My Bill - Check for Errors First",
                "primary_url": "/scan",
            }
        },
    },
    {
        "slug": "cpt-code-lookup",
        "title": "CPT Code Lookup",
        "category": "Quick Calculators",
        "description": "Look up CPT descriptions, Medicare rates, and fair-price context.",
        "keywords": ["CPT code lookup", "what is CPT code"],
        "inline_nudge": "A single CPT overcharge often means broader issues across the bill.",
        "form_fields": [
            {"name": "cpt_code", "label": "CPT code", "type": "text"},
            {"name": "zip_code", "label": "ZIP code (optional)", "type": "text"},
        ],
        "lead_magnet": {
            "key": "cpt_leverage_guide",
            "title": "CPT leverage guide",
            "description": "How to use code-level evidence in dispute letters and calls.",
            "button_label": "Send Me the Guide",
        },
        "ctas": {
            "found": {
                "headline": "CPT pricing context found.",
                "body": "If your billed amount is far above benchmark, you likely have leverage.",
                "primary_label": "Upload My Bill - See All Your Overcharges",
                "primary_url": "/scan",
            },
            "not_found": {
                "headline": "CPT code not found in benchmark tables.",
                "body": "Upload your bill anyway and we'll audit line-by-line with available evidence.",
                "primary_label": "Upload My Bill - Free Audit",
                "primary_url": "/scan",
            },
        },
    },
    {
        "slug": "medicare-rate-lookup",
        "title": "Medicare Rate Lookup",
        "category": "Quick Calculators",
        "description": "Find Medicare reimbursement references by CPT and ZIP locality.",
        "keywords": ["Medicare rate for procedure", "Medicare reimbursement rate"],
        "inline_nudge": "Hospitals often bill multiples above Medicare benchmarks.",
        "form_fields": [
            {"name": "cpt_code", "label": "CPT code", "type": "text"},
            {"name": "zip_code", "label": "ZIP code", "type": "text"},
        ],
        "lead_magnet": {
            "key": "medicare_benchmark_guide",
            "title": "Medicare benchmark guide",
            "description": "How to apply Medicare rates and locality references in disputes.",
            "button_label": "Send Me the Guide",
        },
        "ctas": {
            "found": {
                "headline": "Medicare rate found for your query.",
                "body": "If your bill is 2-3x+ this level, you may be significantly overcharged.",
                "primary_label": "Upload My Bill - Free Audit",
                "primary_url": "/scan",
            },
            "not_found": {
                "headline": "No direct Medicare rate found for this code/locality.",
                "body": "Upload your bill and we'll evaluate available alternatives and charge consistency.",
                "primary_label": "Upload My Bill - Free Audit",
                "primary_url": "/scan",
            },
        },
    },
]

TOOLS_BY_SLUG = {tool["slug"]: tool for tool in TOOLS}


def list_tools() -> list[dict[str, Any]]:
    return TOOLS


def get_tool(slug: str) -> dict[str, Any] | None:
    return TOOLS_BY_SLUG.get((slug or "").strip())
