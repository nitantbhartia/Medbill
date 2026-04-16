"""Guide articles served at /guides/{slug}.

Each guide is a dict with title, meta_description, published date, and
body (HTML string). Calculators are embedded inline via iframes.
"""

from __future__ import annotations

GUIDES = {}


_DEFAULT_REVIEWED = "2026-04-05"


# Legacy slug -> canonical slug. Routes 301 to the canonical and internal
# surfaces (sitemap, related_guides, link map) skip / rewrite these.
GUIDE_REDIRECTS = {
    # EOB cluster
    "understanding-explanation-of-benefits": "explanation-of-benefits-eob",
    "explanation-of-benefits-eob-guide": "explanation-of-benefits-eob",
    "understanding-your-eob": "explanation-of-benefits-eob",
    "understanding-your-explanation-of-benefits": "explanation-of-benefits-eob",
    "how-to-read-an-eob": "explanation-of-benefits-eob",
    "how-to-read-your-eob": "explanation-of-benefits-eob",
    # Appeal / denial cluster
    "appeal-denial": "how-to-appeal-insurance-denial",
    "appeal-insurance-denial": "how-to-appeal-insurance-denial",
    "how-to-appeal-a-denied-claim": "how-to-appeal-insurance-denial",
    "how-to-appeal-an-insurance-denial": "how-to-appeal-insurance-denial",
    "how-to-appeal-health-insurance-denial": "how-to-appeal-insurance-denial",
    "insurance-denial-appeal": "how-to-appeal-insurance-denial",
    "insurance-denial-appeal-win": "how-to-appeal-insurance-denial-and-win",
    "how-to-appeal-a-medical-bill": "how-to-dispute-a-medical-bill",
    "how-to-appeal-a-medical-bill-denial": "how-to-dispute-a-medical-bill",
    # Balance billing / NSA cluster
    "balance-billing-and-surprise-medical-bills": "balance-billing",
    "balance-billing-protection": "balance-billing",
    "understanding-balance-billing": "balance-billing",
    "no-surprises-act": "no-surprises-act-explained",
    "no-surprises-act-guide": "no-surprises-act-explained",
    # Financial assistance cluster
    "charity-care": "hospital-financial-assistance-charity-care",
    "hospital-charity-care-financial-assistance": "hospital-financial-assistance-charity-care",
    "hospital-financial-assistance": "hospital-financial-assistance-charity-care",
    "hospital-financial-assistance-guide": "hospital-financial-assistance-charity-care",
    # CPT codes cluster
    "cpt-codes": "what-are-cpt-codes",
    # Debt / collections cluster
    "debt-validation-letter-medical-bills": "debt-validation-letter-medical-debt",
    "medical-bill-collections-rights": "medical-debt-collections-rights",
    "medical-debt-and-debt-collectors": "settle-medical-debt-collections",
    "medical-debt-lawsuit-defense": "medical-debt-laws-by-state",
    # Dispute / itemized cluster
    "dispute-bill": "how-to-dispute-a-medical-bill",
    "dispute-letter-template": "medical-bill-dispute-letter",
    "duplicate-charges": "duplicate-charges-hospital-bills",
    "hospital-billing-errors": "common-hospital-billing-errors",
    "how-to-get-itemized-bill": "how-to-get-itemized-hospital-bill",
    "how-to-negotiate-a-medical-bill": "how-to-negotiate-medical-bills",
    # Medicare cluster
    "medicare-billing": "how-medicare-billing-works",
    "medicare-billing-explained": "how-medicare-billing-works",
    # Observation status cluster
    "observation-status": "observation-status-billing",
    "observation-status-explained": "observation-status-billing",
    "observation-status-vs-inpatient": "observation-status-billing",
    # Misc legacy slugs
    "facility-fees-explained": "hospital-facility-fees-explained",
    "fdcpa-medical-debt-rights": "fdcpa-rights-medical-debt-collectors",
    "fdcpa-rights-medical-debt": "fdcpa-rights-medical-debt-collectors",
    "inpatient-outpatient": "inpatient-vs-outpatient-billing",
    "medical-billing-advocates": "medical-billing-advocate",
    "out-of-network-bills": "out-of-network-medical-bills",
    "out-of-pocket-maximum-explained": "out-of-pocket-maximum",
    "pe-hospital-billing": "private-equity-hospital-billing",
    "pediatric-medical-billing": "pediatric-billing",
    "preventive-care-billing-errors": "preventive-care-billing",
    "skilled-nursing-billing": "skilled-nursing-facility-billing",
    "surgery-center-vs-hospital": "surgery-center-vs-hospital-cost",
    "er-bills": "why-emergency-room-bills-are-so-high",
    "surgery-costs-billing": "how-much-does-surgery-cost",
}


def register(slug: str, guide: dict):
    published = guide.get("published")
    reviewed_on = guide.get("reviewed_on") or _DEFAULT_REVIEWED
    GUIDES[slug] = {**guide, "slug": slug, "reviewed_on": reviewed_on}


def get_guide(slug: str) -> dict | None:
    return GUIDES.get(slug)


def list_guides() -> list[dict]:
    return sorted(GUIDES.values(), key=lambda g: g.get("published", ""), reverse=True)


def get_related_guides(slug: str, limit: int = 5) -> list[dict]:
    """Return up to `limit` guides related to slug by category and title-keyword overlap."""
    current = GUIDES.get(slug)
    if not current:
        return []

    category = current.get("category", "")
    title_words = set(current.get("title", "").lower().split())
    _STOP = {"a", "an", "the", "and", "or", "of", "in", "to", "for", "on", "at",
             "your", "my", "how", "why", "what", "is", "are", "with", "from", "by",
             "2026", "2025", "2024", "guide", "explained", "complete"}
    title_keys = title_words - _STOP

    scored = []
    for s, g in GUIDES.items():
        if s == slug or s in GUIDE_REDIRECTS:
            continue
        score = 0
        if g.get("category") == category:
            score += 10
        other_words = set(g.get("title", "").lower().split()) - _STOP
        score += len(title_keys & other_words) * 3
        if score > 0:
            scored.append((score, s, g))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [
        {"slug": s, "title": g["title"], "category": g.get("category", "")}
        for _, s, g in scored[:limit]
    ]


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
        if slug not in GUIDE_REDIRECTS
    ]


# Keyword → slug map for auto internal linking (most specific phrases first)
_LINK_MAP: list[tuple[str, str]] = [
    # Regulations & rights
    ("No Surprises Act", "no-surprises-act-explained"),
    ("Good Faith Estimate", "good-faith-estimate-rights"),
    ("FDCPA", "fdcpa-rights-medical-debt-collectors"),
    ("COBRA", "cobra-insurance-billing-guide"),
    # Billing documents & concepts
    ("explanation of benefits", "explanation-of-benefits-eob"),
    ("Explanation of Benefits", "explanation-of-benefits-eob"),
    ("EOB", "explanation-of-benefits-eob"),
    ("superbill", "what-is-a-superbill"),
    ("itemized bill", "how-to-get-itemized-hospital-bill"),
    ("chargemaster", "hospital-chargemaster-explained"),
    ("facility fee", "hospital-facility-fees-explained"),
    ("observation status", "observation-status-billing"),
    ("DRG code", "icd10-drg-codes"),
    ("ICD-10", "icd10-drg-codes"),
    ("CPT code", "what-are-cpt-codes"),
    # Insurance concepts
    ("out-of-pocket maximum", "out-of-pocket-maximum"),
    ("out of pocket maximum", "out-of-pocket-maximum"),
    ("coordination of benefits", "coordination-of-benefits-dual-insurance"),
    ("dual eligible", "dual-eligible-medicare-medicaid-billing"),
    ("coinsurance", "copay-vs-coinsurance-vs-deductible"),
    ("deductible", "copay-vs-coinsurance-vs-deductible"),
    ("HSA", "hsa-fsa-pay-medical-bills"),
    ("FSA", "hsa-fsa-pay-medical-bills"),
    ("open enrollment", "open-enrollment-health-insurance"),
    ("short-term health insurance", "short-term-health-insurance"),
    ("prior authorization", "prior-authorization"),
    ("prior auth", "prior-authorization"),
    ("out-of-network emergency", "out-of-network-emergency-room-bill"),
    ("out-of-network", "out-of-network-medical-bills"),
    ("in-network", "out-of-network-medical-bills"),
    # Billing errors
    ("billing error", "common-hospital-billing-errors"),
    ("billing errors", "common-hospital-billing-errors"),
    ("duplicate charge", "duplicate-charges-hospital-bills"),
    ("duplicate charges", "duplicate-charges-hospital-bills"),
    ("upcoding", "common-hospital-billing-errors"),
    ("unbundling", "common-hospital-billing-errors"),
    # Overcharges & pricing
    ("Medicare rate", "average-hospital-markup-over-medicare"),
    ("Medicare benchmark", "average-hospital-markup-over-medicare"),
    ("hospital markup", "average-hospital-markup-over-medicare"),
    ("chargemaster price", "hospital-chargemaster-explained"),
    # Disputes & appeals
    ("dispute letter", "medical-bill-dispute-letter"),
    ("insurance denial", "how-to-appeal-insurance-denial-and-win"),
    ("claim denial", "how-to-appeal-insurance-denial-and-win"),
    ("denied claim", "how-to-appeal-insurance-denial-and-win"),
    ("appeal", "how-to-appeal-insurance-denial-and-win"),
    ("medical billing advocate", "medical-billing-advocate"),
    ("patient advocate", "medical-billing-advocate"),
    # Surprise billing types
    ("balance billing", "balance-billing"),
    ("balance bill", "balance-billing"),
    ("surprise bill", "no-surprises-act-explained"),
    ("surprise medical bill", "no-surprises-act-explained"),
    ("surprise ambulance bill", "surprise-ambulance-bill"),
    ("air ambulance", "air-ambulance-bills"),
    ("ambulance bill", "ambulance-bill"),
    ("assistant surgeon", "surprise-assistant-surgeon-bills"),
    ("anesthesiologist", "anesthesia-billing"),
    ("anesthesia bill", "anesthesia-billing"),
    ("freestanding ER", "freestanding-er-billing"),
    # Specific settings
    ("emergency room", "why-emergency-room-bills-are-so-high"),
    ("ER visit", "why-emergency-room-bills-are-so-high"),
    ("urgent care", "urgent-care-billing"),
    ("surgery center", "surgery-center-vs-hospital-cost"),
    ("skilled nursing", "skilled-nursing-facility-billing"),
    ("nursing home", "nursing-home-billing"),
    ("NICU", "nicu-bills-explained"),
    ("newborn", "newborn-hospital-bill-guide"),
    ("childbirth", "average-cost-of-childbirth-2026"),
    # Imaging & diagnostics
    ("MRI", "mri-costs"),
    ("CT scan", "ct-scan-costs"),
    ("colonoscopy", "colonoscopy-billing"),
    ("lab test", "why-lab-test-bills-are-so-high"),
    ("blood work", "blood-work-cost"),
    ("physical therapy", "physical-therapy-billing"),
    # Specific conditions & treatments
    ("cancer treatment", "cancer-treatment-billing"),
    ("chemotherapy", "chemotherapy-cost"),
    ("dialysis", "dialysis-billing"),
    ("prescription drug", "prescription-drug-billing-errors"),
    ("telehealth", "telehealth-billing-insurance"),
    # Medical debt & collections
    ("medical debt collections", "medical-debt-collections-rights"),
    ("debt collector", "fdcpa-rights-medical-debt-collectors"),
    ("stop collector calls", "stop-medical-debt-collector-calls"),
    ("debt validation", "debt-validation-letter-medical-debt"),
    ("statute of limitations", "medical-debt-statute-of-limitations"),
    ("medical debt expires", "when-medical-debt-expires-statute-of-limitations"),
    ("zombie debt", "zombie-medical-debt"),
    ("pay for delete", "pay-for-delete-medical-debt"),
    ("settle medical debt", "settle-medical-debt-collections"),
    ("hospital sued", "can-hospital-sue-unpaid-medical-bills"),
    ("sued for medical", "sued-for-medical-debt"),
    ("hospital lien", "hospital-liens-explained"),
    ("wage garnishment", "medical-debt-wage-garnishment"),
    ("medical bankruptcy", "medical-bankruptcy-guide"),
    ("uninsured hospital bill", "uninsured-hospital-bill"),
    ("without insurance", "uninsured-hospital-bill"),
    # Financial assistance
    ("charity care", "hospital-financial-assistance-charity-care"),
    ("financial assistance", "hospital-financial-assistance-charity-care"),
    ("federal poverty level", "federal-poverty-level-medical-bills-2026"),
    ("hardship", "medical-bill-financial-hardship"),
    ("payment plan", "hospital-payment-plans"),
    # Hospital types & ownership
    ("nonprofit hospital", "for-profit-vs-nonprofit-hospital-billing"),
    ("for-profit hospital", "for-profit-vs-nonprofit-hospital-billing"),
    ("private equity hospital", "private-equity-hospital-billing"),
    # Specific insurers
    ("UnitedHealthcare", "unitedhealthcare-billing-disputes"),
    ("Aetna", "aetna-insurance-billing-disputes"),
    ("Blue Cross", "blue-cross-blue-shield-billing-disputes"),
    ("Cigna", "cigna-billing-disputes-guide"),
    ("Humana", "humana-billing-disputes-guide"),
    # Government programs
    ("Medicare", "what-does-medicare-cover"),
    ("workers' compensation", "workers-compensation-medical-billing"),
    ("workers compensation", "workers-compensation-medical-billing"),
    # Audit & audit concepts
    ("medical bill audit", "what-is-a-medical-bill-audit"),
    ("billing error rate", "what-percentage-of-hospital-bills-have-errors"),
    # Pillar guides
    ("CPT codes and Medicare rates", "cpt-codes-medicare-rates-complete-guide"),
    ("CPT code guide", "cpt-codes-medicare-rates-complete-guide"),
    ("medical debt laws by state", "medical-debt-laws-by-state"),
    ("state medical debt laws", "medical-debt-laws-by-state"),
    # Misc
    ("patient rights", "patient-rights-emergency-room"),
]


_SCAN_CTA_BLOCK = (
    '<div class="guide-cta-inline">'
    '<h3>Got a bill for this? Check it free.</h3>'
    '<p>Upload your medical bill and we\'ll compare every line against Medicare rates — flagging overcharges in 30 seconds. 1 in 4 bills has an error.</p>'
    '<a href="/scan">Scan My Bill Free &rarr;</a>'
    '</div>'
)


def inject_scan_cta(html: str) -> str:
    """Inject a scan CTA after the 3rd </h2> for long guides that lack one."""
    import re
    if 'guide-cta-inline' in html:
        return html
    if len(re.sub(r'<[^>]+>', '', html).split()) < 500:
        return html
    # Insert after 3rd </h2>, falling back to halfway through
    pos, count = 0, 0
    while count < 3:
        found = html.find('</h2>', pos)
        if found == -1:
            break
        pos = found + len('</h2>')
        count += 1
    if count < 2:
        pos = len(html) // 2
    return html[:pos] + _SCAN_CTA_BLOCK + html[pos:]


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
import guide_iowa_medical_billing
import guide_new_mexico_medical_billing
import guide_nebraska_medical_billing
# Batch 10: procedure costs + insurance guides
import guide_mammogram_cost
import guide_vasectomy_cost
import guide_shoulder_surgery_cost
import guide_dexa_scan_cost
import guide_medigap_medicare_supplement
import guide_carpal_tunnel_surgery_cost
import guide_pet_scan_cost
import guide_medicare_part_d_explained
import guide_short_term_health_insurance
import guide_addiction_treatment_billing
# Batch 11: dental insurance, comparison guides, Medicare Advantage
import guide_dental_insurance_explained
import guide_dental_discount_plan_vs_insurance
import guide_best_worst_states_medical_debt
import guide_hospital_vs_asc_cost
import guide_dental_implant_alternatives
# Batch 12: remaining state guides (AK, DE, HI, ID, ME, MS, MT, NH, ND, RI, SD, VT, WV, WY)
import guide_alaska_medical_billing
import guide_delaware_medical_billing
import guide_hawaii_medical_billing
import guide_idaho_medical_billing
import guide_maine_medical_billing
import guide_mississippi_medical_billing
import guide_montana_medical_billing
import guide_new_hampshire_medical_billing
import guide_north_dakota_medical_billing
import guide_rhode_island_medical_billing
import guide_south_dakota_medical_billing
import guide_vermont_medical_billing
import guide_west_virginia_medical_billing
import guide_wyoming_medical_billing
# Batch 13: high-volume SEO guides
import guide_what_medicare_covers
import guide_hospital_billing_timeline
import guide_therapy_session_cost
import guide_medicaid_income_limits
import guide_out_of_network_er_billing
import guide_insurance_claim_denied
import guide_prior_auth_medication
import guide_bypass_surgery_cost
import guide_chemotherapy_cost
import guide_free_medical_care_low_income
import guide_medical_bill_negotiation_script
import guide_mental_health_parity_billing
import guide_physical_therapy_cost_session
import guide_stent_surgery_cost
import guide_cpap_machine_cost
import guide_insulin_cost
import guide_knee_arthroscopy_cost
import guide_radiation_therapy_cost
import guide_autism_aba_billing
import guide_er_vs_urgent_care_cost
# Batch 14: high-volume cost + coverage guides
import guide_cataract_surgery_cost
import guide_colonoscopy_cost
import guide_hip_replacement_cost
import guide_sleep_study_cost
import guide_observation_status_billing
import guide_ultrasound_cost
import guide_birth_control_insurance_coverage
import guide_drug_formulary_tiers
import guide_tummy_tuck_insurance_coverage
# Batch 15: IVF, dental crown, hearing aids, spinal fusion, endoscopy, vision, balance billing, eye exam, bankruptcy
import guide_ivf_cost
import guide_dental_crown_cost
import guide_hearing_aid_cost
import guide_spinal_fusion_cost
import guide_endoscopy_cost
import guide_vision_insurance_explained
import guide_eye_exam_cost
import guide_medical_debt_bankruptcy
import guide_gallbladder_surgery_cost
# Batch 16: hernia, appendectomy, tonsillectomy, STD testing, blood work, dermatology, echo, anesthesia, kidney stone
import guide_hernia_surgery_cost
import guide_appendectomy_cost
import guide_tonsillectomy_cost
import guide_std_testing_cost
import guide_blood_work_cost
import guide_dermatologist_cost
import guide_echocardiogram_cost
import guide_kidney_stone_treatment_cost
import guide_cgm_cost
# Batch 17: baby cost, Ozempic, health insurance, car accident, ACA subsidies, Botox, telehealth, rhinoplasty, allergy, genetic testing, psych, home health, pain mgmt, acne, eating disorders, liposuction, workers comp, LTC, emergency dental, hair loss
import guide_botox_insurance_coverage
import guide_having_a_baby_cost
import guide_ozempic_wegovy_cost
import guide_how_to_get_health_insurance
import guide_rhinoplasty_insurance_coverage
import guide_psychiatric_hospital_billing
import guide_home_health_care_billing
import guide_pain_management_billing
import guide_liposuction_insurance_coverage
import guide_workers_comp_medical_billing
import guide_long_term_care_insurance
import guide_emergency_dental_cost
import guide_hair_loss_treatment_cost
import guide_acne_treatment_cost
import guide_eating_disorder_treatment_cost
import guide_allergy_testing_cost
import guide_genetic_testing_cost
import guide_aca_marketplace_subsidies
# Batch 17: insurance basics, cost guides, preventive care, specialty
import guide_deductible_explained
import guide_hmo_ppo_plan_types
import guide_eob_explained
import guide_coinsurance_explained
import guide_ambulance_bill
import guide_prescription_drug_cost
import guide_diabetes_management_cost
import guide_preventive_care_free
import guide_hpv_vaccine_cost
import guide_asthma_treatment_cost
import guide_critical_illness_insurance
import guide_medical_records_request
import guide_stroke_treatment_cost
import guide_fertility_preservation_cost
import guide_hospital_indemnity_insurance
import guide_second_opinion_billing
import guide_dialysis_cost
import guide_hospital_bill_itemized
import guide_explanation_of_benefits_eob
import guide_balance_billing_fight
import guide_insurance_denial_appeal
import guide_cpt_codes_explained
import guide_surprise_ambulance_bill
# Batch 20: Insurance carrier billing guides
import guide_unitedhealthcare_billing
import guide_aetna_billing_disputes
import guide_bcbs_billing_disputes
import guide_cigna_billing_disputes
import guide_humana_billing_disputes
import guide_kaiser_billing_disputes
import guide_medicaid_managed_care_billing
import guide_insurance_prior_auth_denied
# Batch 20 part 2: Financial assistance guides
import guide_charity_care_by_state
import guide_medical_debt_forgiveness2
import guide_hardship_payment_plan
import guide_negotiate_medical_bill_to_zero
import guide_fpl_income_limits_2026
import guide_medical_bill_statute_limitations_debt
# Batch 19: Medicare & Medicaid billing cluster
import guide_medicare_billing_disputes
import guide_medicare_part_b_coverage
import guide_medicare_advantage_billing
import guide_medicaid_billing_rights
import guide_medicare_supplement_medigap
import guide_medicare_part_d_formulary
import guide_medicare_preventive_care
import guide_medicaid_spend_down
import guide_medicare_observation_status
import guide_dual_eligible_billing
# PAA (People Also Ask) guides
import guide_paa_what_is_medical_bill_audit
import guide_paa_average_hospital_markup
import guide_paa_percentage_bills_have_errors
import guide_paa_can_hospitals_charge_whatever
import guide_paa_hospital_sue_unpaid
import guide_paa_er_without_insurance
import guide_paa_no_surprises_act_coverage
import guide_paa_find_hospital_prices
import guide_paa_medical_debt_7_years
import guide_paa_itemized_bill_required
for _paa in [
    guide_paa_what_is_medical_bill_audit,
    guide_paa_average_hospital_markup,
    guide_paa_percentage_bills_have_errors,
    guide_paa_can_hospitals_charge_whatever,
    guide_paa_hospital_sue_unpaid,
    guide_paa_er_without_insurance,
    guide_paa_no_surprises_act_coverage,
    guide_paa_find_hospital_prices,
    guide_paa_medical_debt_7_years,
    guide_paa_itemized_bill_required,
]:
    register(_paa.GUIDE["slug"], _paa.GUIDE)
# CPT code reference guides (self-registering on import)
import guide_cpt_library  # noqa: F401
# State medical debt law guides (self-registering on import)
import guide_state_debt_laws  # noqa: F401
# Pillar guides (hub pages for programmatic spoke clusters)
import guide_pillar_cpt_codes  # noqa: F401
import guide_pillar_state_debt_laws  # noqa: F401


def _extend_link_map_from_guides():
    """Auto-add title-based entries for guides not yet covered by _LINK_MAP."""
    import re
    _STOP = {"a", "an", "the", "and", "or", "of", "in", "to", "for", "on", "at",
              "vs", "your", "my", "our", "how", "why", "what", "when", "is", "are",
              "with", "from", "by", "as", "be", "has", "have", "after", "before",
              "about", "—", "-", "&", "2026", "2025", "2024"}

    covered_slugs = {slug for _, slug in _LINK_MAP}
    additions: list[tuple[str, str]] = []

    for slug, guide in GUIDES.items():
        if slug in covered_slugs or slug in GUIDE_REDIRECTS:
            continue
        title = guide.get("title", "")
        # Use title up to first colon, dash, or em-dash as the phrase
        phrase = re.split(r"[:\-—(]", title)[0].strip()
        # Strip trailing punctuation and common suffixes like "(2026)"
        phrase = re.sub(r"\s*\(?\d{4}\)?$", "", phrase).strip()
        if not phrase or len(phrase) < 8:
            continue
        # Skip if phrase is all stop words
        words = [w.lower().strip(".,") for w in phrase.split()]
        if all(w in _STOP for w in words):
            continue
        additions.append((phrase, slug))

    _LINK_MAP.extend(additions)


def _rewrite_redirected_link_targets():
    """Retarget any _LINK_MAP entry that points at a redirected slug."""
    for i, (phrase, slug) in enumerate(_LINK_MAP):
        if slug in GUIDE_REDIRECTS:
            _LINK_MAP[i] = (phrase, GUIDE_REDIRECTS[slug])


_extend_link_map_from_guides()
_rewrite_redirected_link_targets()
