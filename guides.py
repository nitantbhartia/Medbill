"""Guide articles served at /guides/{slug}.

Each guide is a dict with title, meta_description, published date, and
body (HTML string). Calculators are embedded inline via iframes.
"""

from __future__ import annotations

GUIDES = {}


_DEFAULT_REVIEWED = "2026-04-05"


def register(slug: str, guide: dict):
    published = guide.get("published")
    reviewed_on = guide.get("reviewed_on") or _DEFAULT_REVIEWED
    GUIDES[slug] = {**guide, "slug": slug, "reviewed_on": reviewed_on}


def get_guide(slug: str) -> dict | None:
    return GUIDES.get(slug)


def list_guides() -> list[dict]:
    return sorted(GUIDES.values(), key=lambda g: g.get("published", ""), reverse=True)


def get_related_guides(slug: str, limit: int = 3) -> list[dict]:
    """Return up to `limit` other guides related to the given slug, preferring same category."""
    current = GUIDES.get(slug)
    if not current:
        return []

    category = current.get("category", "")
    same = [
        {"slug": s, "title": g["title"], "category": g.get("category", "")}
        for s, g in GUIDES.items()
        if s != slug and g.get("category") == category
    ]
    if len(same) >= limit:
        return same[:limit]

    other = [
        {"slug": s, "title": g["title"], "category": g.get("category", "")}
        for s, g in GUIDES.items()
        if s != slug and g.get("category") != category
    ]
    return (same + other)[:limit]


def get_guide_slugs() -> list[str]:
    return list(GUIDES.keys())


def _category_slug(name: str) -> str:
    return name.lower().replace(" ", "-").replace("&", "and").replace("/", "-")


def get_all_categories() -> list[dict]:
    """Return categories sorted by guide count descending."""
    counts: dict[str, int] = {}
    for g in GUIDES.values():
        cat = g.get("category", "")
        if cat:
            counts[cat] = counts.get(cat, 0) + 1
    return sorted(
        [{"name": name, "slug": _category_slug(name), "count": count} for name, count in counts.items()],
        key=lambda c: -c["count"],
    )


def get_guides_by_category(category_slug: str) -> list[dict]:
    """Return all guides matching a category slug, sorted newest first."""
    return sorted(
        [g for g in GUIDES.values() if _category_slug(g.get("category", "")) == category_slug],
        key=lambda g: g.get("published", ""),
        reverse=True,
    )


def get_guides_for_sitemap() -> list[tuple[str, str]]:
    """Return (slug, published_date) pairs for all guides, sorted newest first."""
    return [
        (slug, g.get("published", "2026-01-01"))
        for slug, g in sorted(GUIDES.items(), key=lambda x: x[1].get("published", ""), reverse=True)
    ]


# Keyword → slug map for auto internal linking (most specific phrases first)
_LINK_MAP: list[tuple[str, str]] = [
    ("No Surprises Act", "no-surprises-act-explained"),
    ("Good Faith Estimate", "good-faith-estimate-rights"),
    ("explanation of benefits", "understanding-your-eob"),
    ("Explanation of Benefits", "understanding-your-eob"),
    ("charity care", "hospital-financial-assistance-charity-care"),
    ("balance billing", "balance-billing"),
    ("balance bill", "balance-billing"),
    ("prior authorization", "prior-authorization-denials"),
    ("prior auth", "prior-authorization-denials"),
    ("observation status", "observation-status-billing"),
    ("itemized bill", "how-to-get-itemized-hospital-bill"),
    ("medical debt collections", "medical-bill-collections-rights"),
    ("debt collector", "fdcpa-rights-medical-debt-collectors"),
    ("FDCPA", "fdcpa-rights-medical-debt-collectors"),
    ("debt validation", "debt-validation-letter-medical-debt"),
    ("statute of limitations", "medical-debt-statute-of-limitations"),
    ("hospital lien", "hospital-liens-explained"),
    ("CPT code", "what-are-cpt-codes"),
    ("DRG code", "icd10-drg-codes"),
    ("ICD-10", "icd10-drg-codes"),
    ("out-of-pocket maximum", "out-of-pocket-maximum-explained"),
    ("out of pocket maximum", "out-of-pocket-maximum-explained"),
    ("deductible", "copay-vs-coinsurance-vs-deductible"),
    ("coinsurance", "copay-vs-coinsurance-vs-deductible"),
    ("HSA", "hsa-fsa-pay-medical-bills"),
    ("FSA", "hsa-fsa-pay-medical-bills"),
    ("COBRA", "cobra-insurance-billing-guide"),
    ("medical billing advocate", "medical-billing-advocate"),
    ("superbill", "what-is-a-superbill"),
    ("appeal", "how-to-appeal-insurance-denial-and-win"),
    ("dispute letter", "medical-bill-dispute-letter"),
    ("payment plan", "hospital-payment-plans"),
    ("wage garnishment", "medical-debt-wage-garnishment"),
    ("medical bankruptcy", "medical-bankruptcy-guide"),
    ("hardship", "medical-bill-financial-hardship"),
    ("surprise bill", "no-surprises-act-explained"),
    ("facility fee", "guide_facility_fees_explained"),
    ("chargemaster", "hospital-chargemaster-explained"),
]


def inject_internal_links(html: str, current_slug: str) -> str:
    """Auto-link first occurrence of key phrases to relevant guides (skips current slug)."""
    import re
    # Pre-seed with slugs already linked in the HTML so we don't double-link
    already = set(re.findall(r'/guides/([^/"]+)/', html))
    linked_slugs: set[str] = {current_slug} | already

    # Split HTML into alternating text/tag segments; only modify text segments
    segments = re.split(r"(<[^>]+>)", html)
    inside_anchor = 0
    result = []

    for seg in segments:
        if seg.startswith("<"):
            tag_lower = seg.lower()
            if tag_lower.startswith("<a"):
                inside_anchor += 1
            elif tag_lower.startswith("</a"):
                inside_anchor = max(0, inside_anchor - 1)
            result.append(seg)
            continue

        if inside_anchor or not seg.strip():
            result.append(seg)
            continue

        for phrase, slug in _LINK_MAP:
            if slug in linked_slugs:
                continue
            idx = seg.find(phrase)
            if idx == -1:
                continue
            linked_slugs.add(slug)
            seg = (
                seg[:idx]
                + f'<a href="/guides/{slug}/">{phrase}</a>'
                + seg[idx + len(phrase):]
            )
            break  # one link per text segment to avoid over-linking

        result.append(seg)

    return "".join(result)


def _embed(mode="cost", cpt="", title="", subtitle="", height="380"):
    """Return an iframe snippet for embedding a calculator in article body."""
    params = f"mode={mode}"
    if cpt:
        params += f"&cpt={cpt}"
    if title:
        params += f"&title={title.replace('&', '%26')}"
    if subtitle:
        params += f"&subtitle={subtitle.replace('&', '%26')}"
    return (
        f'<iframe src="/calculator/embed?{params}" '
        f'width="100%" height="{height}" style="border:none; border-radius:18px;" '
        f'loading="lazy" title="{title or "Calculator"}"></iframe>'
    )


# Import all guide content modules (each calls register() on import)
import guide_read_bill
import guide_dispute_bill
import guide_er_bills
import guide_no_surprises_act
import guide_negotiate_bills
import guide_eob
import guide_imaging_costs
import guide_surgery_costs
import guide_charity_care
import guide_appeal_denial
import guide_medical_debt_collections
import guide_ambulance_bills
import guide_lab_test_costs
import guide_mental_health_billing
import guide_observation_status
import guide_cpt_codes
import guide_hospital_drug_charges
import guide_prior_authorization
import guide_anesthesia_billing
import guide_balance_billing
import guide_medicare_advantage
import guide_hospital_billing_grades
import guide_forprofit_vs_nonprofit_hospitals
import guide_hospital_billing_errors
import guide_private_equity_hospitals
import guide_hospital_cash_pay
import guide_hospital_price_transparency
import guide_copay_deductible
import guide_inpatient_outpatient
import guide_maternity_bill
import guide_physical_therapy_billing
import guide_out_of_pocket_maximum
import guide_dispute_letter_template
import guide_telehealth_billing
import guide_urgent_care_billing
import guide_medical_billing_advocate
import guide_medical_debt_statute
import guide_california_medical_billing
import guide_texas_hospital_charity_care
import guide_florida_hospital_billing_rights
import guide_new_york_medical_billing_laws
import guide_illinois_hospital_charity_care
import guide_pennsylvania_hospital_charity_care
import guide_georgia_hospital_billing_rights
import guide_ohio_hospital_billing_rights
import guide_north_carolina_medical_debt
import guide_michigan_hospital_billing_rights
import guide_medicare_billing
import guide_medical_debt_credit_score
import guide_hsa_fsa_medical_bills
import guide_cobra_billing
import guide_newborn_hospital_bills
import guide_cancer_treatment_billing
import guide_orthopedic_surgery_billing
import guide_prescription_drug_billing
import guide_workers_comp_billing
import guide_medical_bankruptcy
import guide_colonoscopy_billing
import guide_glp1_drug_coverage
import guide_cardiac_billing
import guide_sleep_study_billing
import guide_home_health_billing
# Debt Collection Defense guides
import guide_fdcpa_rights
import guide_debt_validation_letter
import guide_medical_debt_lawsuit_defense
import guide_stop_debt_collector_calls
import guide_zombie_medical_debt
# Bill Affordability guides
import guide_cant_afford_medical_bill
import guide_hospital_payment_plans
import guide_medical_bill_hardship
import guide_uninsured_hospital_bills
import guide_medical_bill_income_discounts
# Pay-for-Delete / Settlement guides
import guide_pay_for_delete_medical_debt
import guide_medical_debt_settlement
# Medical Debt Forgiveness
import guide_medical_debt_forgiveness
# New guides
import guide_dental_billing
import guide_medical_debt_after_death
import guide_preventive_care_billing
import guide_how_health_insurance_works
import guide_car_accident_medical_bills
# Skilled Nursing, Rights, Financial Assistance, Audit guides
import guide_skilled_nursing_billing
import guide_surprise_assistant_surgeon_bills
import guide_medical_billing_rights_overview
import guide_hospital_financial_assistance
import guide_medical_bill_audit_checklist
# Freestanding ER, Fertility, Genetic Testing, Dialysis, Dermatology guides
import guide_freestanding_er_billing
import guide_fertility_treatment_billing
import guide_genetic_testing_billing
import guide_dialysis_billing
import guide_dermatology_billing
# Rehab, Device, ICD-10/DRG, Hearing Aid, Allergy Testing guides
import guide_rehabilitation_billing
import guide_medical_device_billing
import guide_icd10_drg_codes
import guide_hearing_aids_billing
import guide_allergy_testing_billing
# Bariatric, Medical Records, Pediatric, Hospice, Chiropractic guides
import guide_weight_loss_surgery_billing
import guide_medical_records_rights
import guide_pediatric_billing
import guide_hospice_billing
import guide_chiropractic_billing
# New guides batch: trending 2026 topics
import guide_facility_fees_explained
import guide_good_faith_estimate
import guide_medical_debt_wage_garnishment
import guide_bill_after_insurance
import guide_medical_billing_errors_statistics
import guide_how_to_get_itemized_bill
import guide_hospital_price_transparency_2026
import guide_medical_debt_credit_report_2026
import guide_aca_subsidy_cliff_2026
import guide_insurance_denial_appeal_win
import guide_out_of_network_bills
import guide_medical_debt_buying_house
import guide_coordination_of_benefits
import guide_nicu_bills
# Batch 3: actionable guides
import guide_dispute_phone_scripts
import guide_hospital_chargemaster
import guide_surprise_bills_after_surgery
import guide_duplicate_charges
import guide_medical_bill_time_limit
import guide_patient_rights_emergency_room
# Batch 4: state-specific guides
import guide_colorado_medical_billing
import guide_virginia_medical_billing
import guide_new_jersey_medical_billing
import guide_arizona_medical_billing
import guide_massachusetts_medical_billing
import guide_maryland_medical_billing
import guide_minnesota_medical_billing
import guide_indiana_medical_billing
import guide_washington_medical_billing
import guide_connecticut_medical_billing
# Batch 5: high-value guides
import guide_medical_bill_hardship_letter
import guide_what_happens_dont_pay_medical_bills
import guide_average_cost_of_childbirth
import guide_how_to_check_doctor_in_network
import guide_medical_billing_codes_explained
import guide_what_is_a_superbill
import guide_how_to_get_medical_bills_reduced
import guide_hospital_liens_explained
import guide_air_ambulance_bills
import guide_medical_billing_coding_mistakes
# Batch 6: SEO guide expansion
import guide_csection_costs
import guide_medical_tax_deduction
import guide_how_to_apply_for_medicaid
import guide_medical_billing_scams
import guide_appendectomy_costs
import guide_veterans_medical_bills
import guide_medicare_vs_medicaid
import guide_knee_replacement_costs
import guide_surgery_center_vs_hospital
import guide_medical_debt_divorce
# Batch 7: procedure cost guides
import guide_hip_replacement_costs
import guide_spinal_fusion_costs
import guide_blood_test_costs
import guide_epidural_costs
import guide_tonsillectomy_costs
import guide_cataract_surgery_costs
import guide_acl_surgery_costs
import guide_gallbladder_surgery_costs
import guide_xray_costs
import guide_how_to_choose_health_insurance
# Batch 8: imaging, procedure, and specialty guides
import guide_mri_costs
import guide_ct_scan_costs
import guide_ultrasound_costs
import guide_hernia_surgery_costs
import guide_hysterectomy_costs
import guide_endoscopy_billing
import guide_wisconsin_medical_billing
import guide_missouri_medical_billing
import guide_stroke_treatment_billing
import guide_plastic_surgery_billing
import guide_podiatry_billing
import guide_nevada_medical_billing
import guide_oregon_medical_billing
import guide_tennessee_hospital_charity_care
import guide_nursing_home_billing
# Batch 9: state guides + dental/vision/HR guides
import guide_south_carolina_medical_billing
import guide_dental_implant_cost
import guide_root_canal_cost
import guide_wisdom_teeth_removal_cost
import guide_alabama_medical_billing
import guide_louisiana_medical_billing
import guide_invisalign_cost
import guide_kentucky_medical_billing
import guide_oklahoma_medical_billing
import guide_lasik_cost
import guide_open_enrollment_guide
import guide_utah_medical_billing
import guide_arkansas_medical_billing
