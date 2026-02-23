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
