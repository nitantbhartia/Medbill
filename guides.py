"""Guide articles served at /guides/{slug}.

Each guide is a dict with title, meta_description, published date, and
body (HTML string). Calculators are embedded inline via iframes.
"""

GUIDES = {}


def register(slug: str, guide: dict):
    GUIDES[slug] = {**guide, "slug": slug}


def get_guide(slug: str) -> dict | None:
    return GUIDES.get(slug)


def list_guides() -> list[dict]:
    return sorted(GUIDES.values(), key=lambda g: g.get("published", ""), reverse=True)


def get_guide_slugs() -> list[str]:
    return list(GUIDES.keys())


def get_guides_for_sitemap() -> list[tuple[str, str]]:
    """Return (slug, published_date) pairs for all guides, sorted newest first."""
    return [
        (slug, g.get("published", "2026-01-01"))
        for slug, g in sorted(GUIDES.items(), key=lambda x: x[1].get("published", ""), reverse=True)
    ]


def get_related_guides(current_slug: str, limit: int = 4) -> list[dict]:
    """Return guides in the same category, excluding the current guide."""
    current = GUIDES.get(current_slug)
    if not current:
        return []
    category = current.get("category", "")
    related = [
        g for slug, g in GUIDES.items()
        if slug != current_slug and g.get("category") == category
    ]
    related.sort(key=lambda g: g.get("published", ""), reverse=True)
    return related[:limit]


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
# Batch 6: trending 2026 topics
import guide_medicaid_cuts_2026
import guide_site_neutral_payment_2026
import guide_glp1_denied_2026
import guide_medicare_costs_2026
import guide_biosimilar_drugs_savings
import guide_short_term_health_insurance
import guide_healthcare_costs_rising_2026
import guide_medicaid_to_marketplace_2026
import guide_copay_accumulator_programs
import guide_tariffs_drug_prices_2026
# Batch 7: high-conversion articles
import guide_medical_bill_vs_eob
import guide_spouse_medical_debt
import guide_medical_bill_while_traveling
import guide_negotiate_before_procedure
import guide_prior_auth_denied_2026
import guide_medical_bill_after_job_loss
import guide_self_pay_patient_rights
import guide_medical_credit_cards
import guide_er_vs_urgent_care_costs
import guide_second_opinion_insurance
# Batch 8: trending state and policy topics
import guide_states_ban_medical_debt_credit
import guide_medicare_part_d_cap_2026
import guide_california_new_healthcare_laws_2026
import guide_illinois_facility_fee_transparency
import guide_healthcare_costs_by_state
import guide_ground_ambulance_billing
import guide_aca_premium_increases_2026
import guide_hospital_refund_overpayment
import guide_ai_healthcare_patient_rights
import guide_florida_healthcare_crisis_2026
# Batch 9: high-ranking keyword guides
import guide_dental_costs_saving
import guide_mental_health_therapy_costs
import guide_understanding_deductibles
import guide_prescription_drug_costs_2026
import guide_medical_debt_over_50
import guide_telehealth_costs_comparison
import guide_price_transparency_how_to_use
import guide_outpatient_surgery_savings
import guide_choosing_health_insurance_plan
import guide_medical_bills_during_divorce
# Batch 10: state billing law + charity care guides
import guide_tennessee_medical_billing
import guide_wisconsin_medical_billing
import guide_missouri_medical_billing
import guide_alabama_medical_billing
import guide_south_carolina_medical_billing
import guide_oregon_medical_billing
import guide_nevada_medical_billing
import guide_kentucky_medical_billing
import guide_louisiana_medical_billing
import guide_oklahoma_medical_billing
import guide_tennessee_charity_care
import guide_wisconsin_charity_care
import guide_missouri_charity_care
