"""Programmatic CPT code reference guides. One guide per top-50 CPT code.

Each entry: (code, name, slug_suffix, medicare_rate, typical_charge_low,
             typical_charge_high, category, one_line_description)
"""
from guides import register

_CPT_DATA = [
    # Emergency Room visits
    ("99281", "ER Visit – Level 1 (Minimal)", "er-visit-level-1", 31, 200, 600, "Emergency Room",
     "Level 1 ER evaluation for minor problems requiring minimal medical decision-making."),
    ("99282", "ER Visit – Level 2 (Low)", "er-visit-level-2", 74, 400, 1100, "Emergency Room",
     "Level 2 ER visit for low-complexity problems such as minor injuries or infections."),
    ("99283", "ER Visit – Level 3 (Moderate)", "er-visit-level-3", 130, 700, 2000, "Emergency Room",
     "Level 3 ER visit — the most commonly billed ER code. Moderate medical complexity."),
    ("99284", "ER Visit – Level 4 (Moderate-High)", "er-visit-level-4", 213, 1200, 3500, "Emergency Room",
     "Level 4 ER visit for moderately-high complexity problems requiring detailed evaluation."),
    ("99285", "ER Visit – Level 5 (High Complexity)", "er-visit-level-5", 330, 2000, 6000, "Emergency Room",
     "Level 5 ER visit — the highest ER code, often the subject of upcoding disputes."),
    # Office visits
    ("99212", "Office Visit – Level 2", "office-visit-level-2", 46, 150, 400, "Office Visits",
     "Straightforward office visit for a simple or self-limited problem."),
    ("99213", "Office Visit – Level 3", "office-visit-level-3", 78, 200, 600, "Office Visits",
     "The most common outpatient office visit code — low-to-moderate medical complexity."),
    ("99214", "Office Visit – Level 4", "office-visit-level-4", 113, 300, 900, "Office Visits",
     "Office visit for moderate medical complexity; often billed for chronic condition management."),
    ("99215", "Office Visit – Level 5", "office-visit-level-5", 147, 400, 1200, "Office Visits",
     "High-complexity office visit; appropriate for patients with multiple chronic conditions."),
    # Hospital care
    ("99232", "Subsequent Hospital Care – Moderate", "subsequent-hospital-care-moderate", 73, 300, 900, "Hospital Care",
     "Daily hospital visit (rounds) for a moderately complex inpatient."),
    ("99233", "Subsequent Hospital Care – High", "subsequent-hospital-care-high", 106, 400, 1200, "Hospital Care",
     "Daily hospital visit for a highly complex inpatient — often over-billed on long stays."),
    # Imaging
    ("71046", "Chest X-Ray (2 Views)", "chest-xray-2-views", 50, 200, 1200, "Imaging",
     "Two-view chest X-ray, among the most commonly ordered diagnostic imaging tests."),
    ("72148", "MRI Lumbar Spine (No Contrast)", "mri-lumbar-spine", 215, 1000, 5000, "Imaging",
     "MRI of the lower back without contrast — one of the most frequent MRI orders."),
    ("70553", "MRI Brain (With Contrast)", "mri-brain-with-contrast", 388, 1500, 7000, "Imaging",
     "Brain MRI with gadolinium contrast for evaluating tumors, MS, and stroke."),
    ("74177", "CT Abdomen/Pelvis (With Contrast)", "ct-abdomen-pelvis-contrast", 275, 1200, 6000, "Imaging",
     "CT scan of the abdomen and pelvis with IV contrast — standard ER workup imaging."),
    ("74178", "CT Abdomen/Pelvis (W/WO Contrast)", "ct-abdomen-pelvis-w-wo-contrast", 340, 1500, 7000, "Imaging",
     "CT of abdomen/pelvis performed both without and with contrast — higher cost than single phase."),
    ("93306", "Echocardiogram (Complete)", "echocardiogram-complete", 320, 1200, 4000, "Imaging",
     "Transthoracic echocardiogram with Doppler — standard cardiac imaging study."),
    # Lab / diagnostics
    ("93000", "EKG/ECG with Interpretation", "ekg-with-interpretation", 28, 100, 500, "Lab & Diagnostics",
     "12-lead electrocardiogram with physician interpretation and report."),
    ("80053", "Comprehensive Metabolic Panel", "comprehensive-metabolic-panel", 16, 50, 300, "Lab & Diagnostics",
     "14-test panel measuring kidney, liver, electrolytes, and blood sugar."),
    ("85025", "Complete Blood Count (CBC)", "complete-blood-count-cbc", 13, 40, 250, "Lab & Diagnostics",
     "Standard blood count measuring red cells, white cells, and platelets."),
    ("80048", "Basic Metabolic Panel", "basic-metabolic-panel", 14, 40, 250, "Lab & Diagnostics",
     "8-test panel measuring kidney function, electrolytes, and blood glucose."),
    ("84443", "Thyroid Stimulating Hormone (TSH)", "thyroid-tsh-test", 26, 60, 400, "Lab & Diagnostics",
     "TSH blood test for evaluating thyroid function — commonly ordered in primary care."),
    # GI procedures
    ("45378", "Colonoscopy – Diagnostic", "colonoscopy-diagnostic", 248, 1000, 4000, "GI Procedures",
     "Diagnostic colonoscopy without removal of tissue — screening or diagnostic."),
    ("45380", "Colonoscopy with Biopsy", "colonoscopy-with-biopsy", 340, 1400, 5000, "GI Procedures",
     "Colonoscopy with biopsy of abnormal tissue. Often billed instead of 45378."),
    ("43239", "Upper GI Endoscopy with Biopsy", "upper-gi-endoscopy-biopsy", 282, 1000, 4000, "GI Procedures",
     "EGD (esophagogastroduodenoscopy) with biopsy — evaluates stomach and esophagus."),
    # Orthopedic surgery
    ("27447", "Total Knee Replacement", "total-knee-replacement", 1916, 20000, 60000, "Orthopedic Surgery",
     "Complete knee replacement — one of the highest-markup procedures in US hospitals."),
    ("27130", "Total Hip Replacement", "total-hip-replacement", 1790, 18000, 55000, "Orthopedic Surgery",
     "Total hip arthroplasty — a major elective surgery with very high chargemaster markups."),
    ("29827", "Shoulder Arthroscopy – Rotator Cuff Repair", "shoulder-arthroscopy-rotator-cuff", 880, 5000, 20000, "Orthopedic Surgery",
     "Minimally invasive shoulder surgery to repair torn rotator cuff tendons."),
    ("29881", "Knee Arthroscopy – Meniscectomy", "knee-arthroscopy-meniscectomy", 580, 3500, 14000, "Orthopedic Surgery",
     "Arthroscopic knee surgery to remove damaged meniscus — common outpatient procedure."),
    ("20610", "Joint Aspiration/Injection – Large", "joint-injection-large", 82, 250, 1500, "Orthopedic Surgery",
     "Aspiration or injection of a large joint (knee, hip, shoulder) — often done in office."),
    # General surgery
    ("47562", "Laparoscopic Cholecystectomy", "laparoscopic-cholecystectomy", 1450, 8000, 30000, "General Surgery",
     "Minimally invasive gallbladder removal — one of the most common US surgeries."),
    ("49505", "Inguinal Hernia Repair", "inguinal-hernia-repair", 775, 4000, 18000, "General Surgery",
     "Open repair of an inguinal (groin) hernia — routine but frequently overcharged."),
    ("44950", "Appendectomy – Open", "appendectomy-open", 1100, 8000, 25000, "General Surgery",
     "Open surgical removal of the appendix — performed in emergency appendicitis."),
    ("44970", "Appendectomy – Laparoscopic", "appendectomy-laparoscopic", 1250, 9000, 28000, "General Surgery",
     "Laparoscopic appendectomy — minimally invasive alternative to open appendectomy."),
    # Spine surgery
    ("63047", "Lumbar Laminectomy", "lumbar-laminectomy", 1200, 8000, 35000, "Spine Surgery",
     "Surgical removal of part of the lumbar vertebrae to relieve spinal stenosis or disc herniation."),
    ("22612", "Lumbar Spinal Fusion (Single Level)", "lumbar-spinal-fusion", 2300, 20000, 80000, "Spine Surgery",
     "Fusion of two or more lumbar vertebrae — the most expensive elective surgery by markup ratio."),
    # Cardiac
    ("92928", "Coronary Stent Placement (Single)", "coronary-stent-placement", 5200, 30000, 100000, "Cardiac",
     "Percutaneous coronary intervention with stent — performed during cardiac catheterization for blocked arteries."),
    # Ophthalmology
    ("66984", "Cataract Surgery with Lens Implant", "cataract-surgery", 745, 3000, 8000, "Ophthalmology",
     "Outpatient cataract extraction with intraocular lens insertion — extremely common in patients 65+."),
    # Breast surgery
    ("19307", "Modified Radical Mastectomy", "modified-radical-mastectomy", 2800, 15000, 50000, "Oncology Surgery",
     "Surgical removal of the breast and axillary lymph nodes for breast cancer treatment."),
    # Other
    ("38221", "Bone Marrow Biopsy", "bone-marrow-biopsy", 185, 1000, 5000, "Oncology",
     "Needle biopsy of bone marrow — used to diagnose blood cancers and disorders."),
    ("11401", "Excision Benign Skin Lesion (Trunk/Arms/Legs, 0.6–1.0cm)", "skin-lesion-excision", 130, 400, 2000, "Dermatology",
     "Surgical removal of a benign skin growth — frequently billed for moles and cysts."),
    # Mental health
    ("90837", "Psychotherapy – 60 Minutes", "psychotherapy-60-minutes", 169, 250, 500, "Mental Health",
     "Standard individual psychotherapy session — 60 minutes with a licensed therapist."),
    ("90834", "Psychotherapy – 45 Minutes", "psychotherapy-45-minutes", 131, 200, 420, "Mental Health",
     "45-minute individual psychotherapy session — often billed for ongoing therapy."),
    ("90847", "Family Therapy with Patient Present", "family-therapy-with-patient", 115, 200, 400, "Mental Health",
     "Family or couples psychotherapy session with the identified patient present."),
    # Physical therapy
    ("97110", "PT – Therapeutic Exercise", "physical-therapy-exercise", 45, 100, 350, "Physical Therapy",
     "One-on-one therapeutic exercise supervised by a physical therapist."),
    ("97530", "PT – Therapeutic Activities", "physical-therapy-therapeutic-activities", 44, 100, 350, "Physical Therapy",
     "Functional activities such as balance and coordination training with a physical therapist."),
    # Obstetrics
    ("59400", "Vaginal Delivery – Global OB Package", "vaginal-delivery-ob", 2200, 10000, 25000, "Obstetrics",
     "Global obstetric package: prenatal visits, vaginal delivery, and postpartum care."),
    ("59510", "Cesarean Delivery – Global OB Package", "cesarean-delivery-ob", 2800, 15000, 40000, "Obstetrics",
     "Global OB package including prenatal care, C-section delivery, and postpartum follow-up."),
    # Preventive
    ("99213", "Annual Wellness Visit", "annual-wellness-visit", 78, 200, 800, "Preventive",
     "Preventive annual wellness visit — covered at 100% under ACA for most insured patients."),
    # Anesthesia representative
    ("00400", "Anesthesia – Superficial Procedures", "anesthesia-superficial", 95, 500, 3000, "Anesthesia",
     "Base anesthesia code for superficial surface procedures — billed per time unit."),
]

# Deduplicate (99213 appears twice above for different contexts — keep last)
_seen: dict[str, tuple] = {}
for entry in _CPT_DATA:
    key = entry[0] + entry[2]  # code + slug_suffix
    _seen[key] = entry
_CPT_DATA = list(_seen.values())


def _build_guide(code: str, name: str, slug_suffix: str, medicare_rate: int,
                 low: int, high: int, category: str, description: str) -> dict:
    slug = f"cpt-{code}-{slug_suffix}"
    markup_low = round(low / medicare_rate, 1)
    markup_high = round(high / medicare_rate, 1)
    return {
        "slug": slug,
        "title": f"CPT Code {code}: {name} — Medicare Rate & What to Check",
        "meta_description": (
            f"CPT code {code} ({name}): Medicare pays ${medicare_rate:,}. Hospitals typically charge "
            f"${low:,}–${high:,} ({markup_low}–{markup_high}x Medicare). Learn what the code means, "
            f"what to dispute, and how to check your bill."
        ),
        "category": category,
        "published": "2026-04-15",
        "reviewed_on": "2026-04-15",
        "author": "BillKarma Team",
        "faqs": [
            {
                "q": f"What is CPT code {code}?",
                "a": f"CPT code {code} is the billing code for {name}. {description} "
                     f"The Medicare-approved payment for this service is approximately ${medicare_rate:,}.",
            },
            {
                "q": f"How much does CPT {code} cost?",
                "a": (
                    f"Medicare pays approximately ${medicare_rate:,} for CPT {code}. "
                    f"Hospital chargemaster prices typically range from ${low:,} to ${high:,} "
                    f"({markup_low}–{markup_high}x the Medicare rate). Insured patients pay their "
                    f"negotiated rate; uninsured patients are often billed the full chargemaster price."
                ),
            },
            {
                "q": f"Is CPT {code} covered by insurance?",
                "a": (
                    f"Most major insurance plans cover CPT {code} when medically necessary. "
                    f"Coverage depends on your specific plan, whether the provider is in-network, "
                    f"and whether any prior authorization was required. Check your Explanation of "
                    f"Benefits (EOB) to confirm how the claim was processed."
                ),
            },
            {
                "q": f"How do I dispute a CPT {code} charge?",
                "a": (
                    f"If your bill shows CPT {code} at more than 3x the Medicare rate (${medicare_rate * 3:,}), "
                    f"submit a written dispute letter citing the CMS benchmark. Also verify the code "
                    f"matches your medical records — upcoding (billing a more complex code than was "
                    f"performed) is one of the most common billing errors."
                ),
            },
        ],
        "body": f"""<p class="lead">CPT code {code} is the billing code for <strong>{name}</strong>. {description} Medicare pays approximately <strong>${medicare_rate:,}</strong> for this service. Hospitals typically charge ${low:,}–${high:,} ({markup_low}–{markup_high}x Medicare).</p>

<h2>What CPT {code} means on your bill</h2>
<p>When you see CPT {code} on an itemized hospital bill or Explanation of Benefits, it means you were billed for {name.lower()}. This code is used by all hospitals, physician offices, and outpatient facilities in the United States to report this service to insurers and Medicare.</p>
<p>The charge listed next to CPT {code} on your bill is the hospital's chargemaster (list) price — not what Medicare or your insurer pays. The actual cost to a Medicare patient is ${medicare_rate:,}. For insured commercial patients, the negotiated rate is typically ${int(medicare_rate * 1.8):,}–${int(medicare_rate * 2.5):,}. Uninsured patients are often billed the full chargemaster amount of ${low:,}–${high:,} unless they specifically ask for a discount or a self-pay rate.</p>

<h2>Medicare rate for CPT {code}: What payers actually pay</h2>
<p>The CMS (Centers for Medicare &amp; Medicaid Services) Medicare rate for CPT {code} is approximately <strong>${medicare_rate:,}</strong> for facility-based services. This is the most transparent public benchmark for this procedure and is updated annually in the Medicare Physician Fee Schedule.</p>
<table>
  <tr><th>Payer</th><th>Typical payment for CPT {code}</th><th>How it's set</th></tr>
  <tr><td>Medicare (CMS)</td><td>${medicare_rate:,}</td><td>Federal fee schedule, published annually</td></tr>
  <tr><td>Commercial insurance</td><td>${int(medicare_rate * 1.8):,}–${int(medicare_rate * 2.5):,}</td><td>Negotiated contract rate</td></tr>
  <tr><td>Medicaid</td><td>${int(medicare_rate * 0.7):,}–${int(medicare_rate * 1.0):,}</td><td>State-set rate, typically lower than Medicare</td></tr>
  <tr><td>Hospital chargemaster</td><td>${low:,}–${high:,}</td><td>Hospital's internal list price; almost nobody pays this</td></tr>
  <tr><td>Uninsured / self-pay</td><td>${int(low * 0.4):,}–${high:,}</td><td>Full charge unless you negotiate or qualify for charity care</td></tr>
</table>

<h2>How to check your CPT {code} charge</h2>
<ol>
  <li><strong>Get the itemized bill.</strong> Confirm CPT {code} is listed with the date of service, quantity, and charge. Request it in writing if you only received a summary statement.</li>
  <li><strong>Check the Medicare rate.</strong> The benchmark for CPT {code} is ${medicare_rate:,}. Any charge above ${medicare_rate * 3:,} (3x Medicare) is worth disputing.</li>
  <li><strong>Verify it matches your records.</strong> CPT {code} should appear in your medical records as a documented service. If you don't recognize it, request your records and compare.</li>
  <li><strong>Check for duplicates.</strong> CPT {code} on the same date more than once is a red flag unless the procedure was genuinely performed multiple times with clinical justification.</li>
  <li><strong>Confirm the code is correct for your situation.</strong> The code should match the actual complexity and nature of the service provided. Ask your provider to explain in writing why this specific code was chosen.</li>
</ol>

<h2>When CPT {code} is commonly overbilled</h2>
<p>Billing departments may improperly bill CPT {code} in these situations:</p>
<ul>
  <li><strong>Upcoding:</strong> Billing CPT {code} when a lower-complexity code better reflects the actual service performed. This is especially common for evaluation and management (E/M) codes where the documentation doesn't support the level billed.</li>
  <li><strong>Unbundling:</strong> Billing CPT {code} alongside other codes that should be included in a single bundled charge. CMS's National Correct Coding Initiative (NCCI) edits define which codes may not be billed together.</li>
  <li><strong>Duplicate billing:</strong> The same CPT {code} appearing twice on the same date without documented clinical reason.</li>
  <li><strong>Phantom charges:</strong> In rare cases, CPT {code} appears on a bill for a service you did not receive. Always cross-reference your bill with your medical records.</li>
</ul>

<h2>Sample dispute letter for a CPT {code} overcharge</h2>
<p>If your bill shows CPT {code} at more than 3x the Medicare rate (${medicare_rate * 3:,}), use this letter as a starting point:</p>
<blockquote>
<p><em>Dear [Hospital] Billing Department,</em></p>
<p><em>I am writing to dispute the charge of $[AMOUNT] for CPT code {code} ({name}) on my bill dated [DATE]. According to the CMS 2026 Medicare Physician Fee Schedule, the Medicare facility rate for CPT {code} is approximately ${medicare_rate:,}. My charge of $[AMOUNT] represents a markup of [X]x the Medicare benchmark.</em></p>
<p><em>I am requesting: (1) a written explanation of how this charge was calculated; (2) any clinical documentation supporting this code; and (3) an adjusted rate closer to the Medicare benchmark or your lowest available self-pay rate.</em></p>
<p><em>Please respond within 30 days. I am prepared to escalate this dispute to my state insurance commissioner and the CMS Price Transparency hotline if needed.</em></p>
</blockquote>
<p>For a complete customizable template, see our <a href="/guides/medical-bill-dispute-letter/">free medical bill dispute letter guide</a>.</p>

<h2>Common billing problems with CPT {code}</h2>
<ul>
  <li><strong>Excessive markup:</strong> Charging more than 3–5x the Medicare rate of ${medicare_rate:,} is worth a formal dispute.</li>
  <li><strong>Missing itemization:</strong> You have the right to an itemized bill listing every CPT code. If you received only a summary, request the itemized version immediately.</li>
  <li><strong>Wrong payer rate applied:</strong> If you have insurance, confirm your EOB shows the negotiated rate was applied — not the full chargemaster price.</li>
  <li><strong>No prior authorization:</strong> Some insurers require prior authorization for CPT {code}. If it wasn't obtained, your insurer may deny the claim and bill you directly — even if the service was medically necessary.</li>
</ul>

<div class="key-takeaway"><strong>Bottom line:</strong> The Medicare benchmark for CPT {code} is ${medicare_rate:,}. A charge above ${int(medicare_rate * 3):,} (3x Medicare) is worth a formal dispute. Use the sample letter above or upload your bill to BillKarma for an automated check of every line item.</div>

<p>For the full list of CPT codes and Medicare rates, see our <a href="/guides/cpt-codes-medicare-rates-complete-guide/">Complete CPT Codes &amp; Medicare Rates Guide</a>.</p>""",
    }


for _entry in _CPT_DATA:
    _g = _build_guide(*_entry)
    register(_g["slug"], _g)
