"""Pillar guide: CPT Codes & Medicare Rates — hub for 51 CPT code spoke pages."""
from guides import register

_SLUG = "cpt-codes-medicare-rates-complete-guide"

_CPT_INDEX = [
    # ER Visits
    ("cpt-99281-er-visit-level-1", "99281", "ER Visit – Level 1", "$29"),
    ("cpt-99282-er-visit-level-2", "99282", "ER Visit – Level 2", "$61"),
    ("cpt-99283-er-visit-level-3", "99283", "ER Visit – Level 3", "$116"),
    ("cpt-99284-er-visit-level-4", "99284", "ER Visit – Level 4", "$183"),
    ("cpt-99285-er-visit-level-5", "99285", "ER Visit – Level 5", "$266"),
    # Office Visits
    ("cpt-99212-office-visit-level-2", "99212", "Office Visit – Level 2", "$47"),
    ("cpt-99213-office-visit-level-3", "99213", "Office Visit – Level 3", "$82"),
    ("cpt-99214-office-visit-level-4", "99214", "Office Visit – Level 4", "$118"),
    ("cpt-99215-office-visit-level-5", "99215", "Office Visit – Level 5", "$172"),
    # Hospital Care
    ("cpt-99232-subsequent-hospital-care-moderate", "99232", "Subsequent Hospital Care – Moderate", "$71"),
    ("cpt-99233-subsequent-hospital-care-high", "99233", "Subsequent Hospital Care – High", "$105"),
    # Imaging
    ("cpt-70553-mri-brain-with-contrast", "70553", "MRI Brain (With Contrast)", "$268"),
    ("cpt-72148-mri-lumbar-spine", "72148", "MRI Lumbar Spine", "$200"),
    ("cpt-74177-ct-abdomen-pelvis-contrast", "74177", "CT Abdomen/Pelvis (With Contrast)", "$233"),
    ("cpt-74178-ct-abdomen-pelvis-w-wo-contrast", "74178", "CT Abdomen/Pelvis (W/WO Contrast)", "$272"),
    ("cpt-71046-chest-xray-2-views", "71046", "Chest X-Ray (2 Views)", "$29"),
    # Lab Tests
    ("cpt-80048-basic-metabolic-panel", "80048", "Basic Metabolic Panel (BMP)", "$14"),
    ("cpt-80053-comprehensive-metabolic-panel", "80053", "Comprehensive Metabolic Panel (CMP)", "$18"),
    ("cpt-85025-complete-blood-count-cbc", "85025", "Complete Blood Count (CBC)", "$12"),
    ("cpt-84443-thyroid-tsh-test", "84443", "TSH (Thyroid) Test", "$26"),
    # GI Procedures
    ("cpt-45378-colonoscopy-diagnostic", "45378", "Colonoscopy – Diagnostic", "$208"),
    ("cpt-45380-colonoscopy-with-biopsy", "45380", "Colonoscopy with Biopsy", "$257"),
    ("cpt-43239-upper-gi-endoscopy-biopsy", "43239", "Upper GI Endoscopy with Biopsy", "$211"),
    # Orthopedic Surgery
    ("cpt-27447-total-knee-replacement", "27447", "Total Knee Replacement", "$1,572"),
    ("cpt-27130-total-hip-replacement", "27130", "Total Hip Replacement", "$1,531"),
    ("cpt-29827-shoulder-arthroscopy-rotator-cuff", "29827", "Shoulder Arthroscopy – Rotator Cuff Repair", "$678"),
    ("cpt-29881-knee-arthroscopy-meniscectomy", "29881", "Knee Arthroscopy – Meniscectomy", "$421"),
    # General Surgery
    ("cpt-47562-laparoscopic-cholecystectomy", "47562", "Laparoscopic Cholecystectomy (Gallbladder)", "$715"),
    ("cpt-49505-inguinal-hernia-repair", "49505", "Inguinal Hernia Repair", "$424"),
    ("cpt-44970-appendectomy-laparoscopic", "44970", "Appendectomy – Laparoscopic", "$734"),
    ("cpt-44950-appendectomy-open", "44950", "Appendectomy – Open", "$589"),
    # Spine
    ("cpt-63047-lumbar-laminectomy", "63047", "Lumbar Laminectomy", "$1,238"),
    ("cpt-22612-lumbar-spinal-fusion", "22612", "Lumbar Spinal Fusion", "$2,174"),
    # Cardiac
    ("cpt-92928-coronary-stent-placement", "92928", "Coronary Stent Placement", "$2,109"),
    ("cpt-93000-ekg-with-interpretation", "93000", "EKG/ECG with Interpretation", "$18"),
    ("cpt-93306-echocardiogram-complete", "93306", "Echocardiogram (Complete)", "$183"),
    # Ophthalmology
    ("cpt-66984-cataract-surgery", "66984", "Cataract Surgery with Lens Implant", "$718"),
    # Dermatology
    ("cpt-11401-skin-lesion-excision", "11401", "Skin Lesion Excision", "$149"),
    # Oncology
    ("cpt-38221-bone-marrow-biopsy", "38221", "Bone Marrow Biopsy", "$180"),
    ("cpt-19307-modified-radical-mastectomy", "19307", "Modified Radical Mastectomy", "$1,456"),
    # Physical Therapy
    ("cpt-97110-physical-therapy-exercise", "97110", "PT – Therapeutic Exercise", "$28"),
    ("cpt-97530-physical-therapy-therapeutic-activities", "97530", "PT – Therapeutic Activities", "$28"),
    # Mental Health
    ("cpt-90834-psychotherapy-45-minutes", "90834", "Psychotherapy – 45 Minutes", "$75"),
    ("cpt-90837-psychotherapy-60-minutes", "90837", "Psychotherapy – 60 Minutes", "$99"),
    ("cpt-90847-family-therapy-with-patient", "90847", "Family Therapy with Patient Present", "$95"),
    # Obstetrics
    ("cpt-59400-vaginal-delivery-ob", "59400", "Vaginal Delivery – Global OB Package", "$2,291"),
    ("cpt-59510-cesarean-delivery-ob", "59510", "Cesarean Delivery – Global OB Package", "$2,698"),
    # Anesthesia
    ("cpt-00400-anesthesia-superficial", "00400", "Anesthesia – Superficial Procedures", "$199"),
    # Other
    ("cpt-20610-joint-injection-large", "20610", "Joint Aspiration/Injection – Large", "$77"),
    ("cpt-99213-annual-wellness-visit", "99213", "Annual Wellness Visit", "$82"),
]


def _build_cpt_table_rows():
    rows = []
    for slug, code, name, rate in _CPT_INDEX:
        rows.append(
            f'<tr><td><a href="/guides/{slug}/" class="font-medium text-accent-600">{code}</a></td>'
            f'<td>{name}</td>'
            f'<td class="text-right font-mono">{rate}</td></tr>'
        )
    return "\n".join(rows)


def _build_spoke_links(category_pairs):
    """Build a linked list of spoke guides for a given category."""
    items = []
    for slug, code, name, rate in category_pairs:
        items.append(f'<li><a href="/guides/{slug}/">CPT {code}: {name} — Medicare rate {rate}</a></li>')
    return "<ul>" + "\n".join(items) + "</ul>"


_ER_SPOKES = [(s, c, n, r) for s, c, n, r in _CPT_INDEX if "er-visit" in s.lower()]
_OFFICE_SPOKES = [(s, c, n, r) for s, c, n, r in _CPT_INDEX if "office-visit" in s.lower() or "annual-wellness" in s.lower()]
_IMAGING_SPOKES = [(s, c, n, r) for s, c, n, r in _CPT_INDEX if any(x in s for x in ["mri-", "ct-", "xray", "chest-x"])]
_LAB_SPOKES = [(s, c, n, r) for s, c, n, r in _CPT_INDEX if any(x in s for x in ["metabolic-panel", "blood-count", "thyroid"])]
_SURGERY_SPOKES = [(s, c, n, r) for s, c, n, r in _CPT_INDEX if any(x in s for x in ["cholecystectomy", "hernia", "appendectomy", "knee-replacement", "hip-replacement", "arthroscopy", "laminectomy", "spinal-fusion", "mastectomy", "cataract"])]
_CARDIAC_SPOKES = [(s, c, n, r) for s, c, n, r in _CPT_INDEX if any(x in s for x in ["stent", "ekg", "echocardiogram"])]
_THERAPY_SPOKES = [(s, c, n, r) for s, c, n, r in _CPT_INDEX if any(x in s for x in ["physical-therapy", "psychotherapy", "family-therapy"])]
_OB_SPOKES = [(s, c, n, r) for s, c, n, r in _CPT_INDEX if any(x in s for x in ["delivery", "cesarean"])]


_BODY = f"""
<p class="lead">CPT codes (Current Procedural Terminology) are the universal 5-digit billing codes used by hospitals, physicians, and labs to report every medical service. Your bill lists these codes to tell insurance companies — and Medicare — exactly what was done and at what charge. This guide explains how CPT codes work, lists Medicare's published reimbursement rates for the 50 most common procedures, and shows you how to spot overbilling.</p>

<div class="answer-box">
<strong>Quick Answer</strong>
A CPT code is a 5-digit number assigned to every medical procedure and service. Medicare publishes a set payment rate for each code. If your hospital charged more than 3× the Medicare rate, you may have an overcharge worth disputing.
</div>

<h2>What Are CPT Codes?</h2>
<p>CPT codes were created and are maintained by the American Medical Association (AMA). Every covered service — from a blood test ($12 at Medicare rates) to a knee replacement ($1,572) — has a code. When a hospital or doctor submits a claim to your insurance, they list CPT codes to describe each service.</p>

<p>The codes fall into three categories:</p>
<ul>
<li><strong>Category I</strong> — The main codes covering procedures, services, and tests (the ones you'll see on most bills)</li>
<li><strong>Category II</strong> — Tracking codes for performance measurement (usually not billed to patients)</li>
<li><strong>Category III</strong> — Temporary codes for new and experimental technology</li>
</ul>

<p>Each year, CMS publishes the <strong>Medicare Physician Fee Schedule</strong> — a table of what Medicare will pay for every CPT code in every geographic region. This is the benchmark BillKarma uses to flag overcharges.</p>

<h2>Medicare's Published Rates for the 50 Most Common CPT Codes</h2>
<p>The table below shows national average Medicare facility rates (what Medicare pays the hospital or facility). These rates are published by CMS and updated annually. Your actual bill may be higher — sometimes much higher.</p>

<table>
<thead>
<tr><th>CPT Code</th><th>Procedure</th><th>Medicare Rate (Facility)</th></tr>
</thead>
<tbody>
{_build_cpt_table_rows()}
</tbody>
</table>

<p><em>Rates are national averages. Local rates vary by geographic area. Source: CMS 2026 Medicare Physician Fee Schedule.</em></p>

<h2>ER Visit CPT Codes (99281–99285)</h2>
<p>Emergency room visits are billed using one of five "evaluation and management" (E/M) codes based on complexity. Level 5 (99285) is the highest and most expensive. You should be billed at the level matching your actual condition — not automatically at Level 4 or 5, which hospitals sometimes do to maximize revenue.</p>
{_build_spoke_links(_ER_SPOKES)}

<h2>Office Visit CPT Codes (99212–99215)</h2>
<p>Outpatient office visits are also billed on a complexity scale. A routine annual physical should rarely be coded as a Level 5 (99215) visit. If you see a high-level code on a short appointment, request an explanation.</p>
{_build_spoke_links(_OFFICE_SPOKES)}

<h2>Imaging CPT Codes (MRI, CT, X-Ray)</h2>
<p>Imaging is one of the most widely overbilled categories. The same MRI can cost $200 at a freestanding imaging center and $3,000+ at a hospital — the Medicare rate is the same for both. The difference is entirely facility markup.</p>
{_build_spoke_links(_IMAGING_SPOKES)}

<h2>Lab Test CPT Codes</h2>
<p>Lab tests have some of the lowest Medicare rates of any service — most panels cost under $20 at Medicare rates. Charges of $100–$400 for basic panels are common and worth disputing.</p>
{_build_spoke_links(_LAB_SPOKES)}

<h2>Surgery CPT Codes</h2>
<p>Surgical procedures have the highest Medicare rates and also the highest potential for overbilling. Common issues include unbundling (billing separately for components of a single surgery), assistant surgeon charges, and facility fees layered on top of the surgeon's bill.</p>
{_build_spoke_links(_SURGERY_SPOKES)}

<h2>Cardiac CPT Codes</h2>
{_build_spoke_links(_CARDIAC_SPOKES)}

<h2>Physical and Mental Health Therapy CPT Codes</h2>
<p>Therapy visits are commonly billed without itemized CPT codes on patient statements. Ask your provider for a superbill that lists the exact codes — this is your right under HIPAA.</p>
{_build_spoke_links(_THERAPY_SPOKES)}

<h2>Obstetrics CPT Codes</h2>
<p>Maternity care is often billed as a "global package" (all prenatal visits + delivery + postpartum). The global package codes (59400, 59510) are often underpriced by insurers while hospitals add facility fees separately — resulting in surprise bills.</p>
{_build_spoke_links(_OB_SPOKES)}

<h2>How to Use CPT Codes to Audit Your Bill</h2>
<ol>
<li><strong>Request your itemized bill.</strong> Every hospital must provide one. Call the billing department and ask for an itemized statement listing each CPT code and charge.</li>
<li><strong>Look up the Medicare rate.</strong> Find your CPT code in the table above or use BillKarma's <a href="/calculator">Medicare rate calculator</a>.</li>
<li><strong>Calculate the markup.</strong> Divide your charge by the Medicare rate. A 3× markup is typical. Above 5× is often disputable.</li>
<li><strong>Check for common errors:</strong>
<ul>
<li>Duplicate charges (same CPT code billed twice)</li>
<li>Upcoding (a routine level-3 visit billed as level-5)</li>
<li>Unbundling (components of a packaged procedure billed separately)</li>
<li>Services you didn't receive</li>
</ul>
</li>
<li><strong>Send a dispute letter.</strong> Use our <a href="/guides/medical-bill-dispute-letter/">free dispute letter template</a> to formally challenge incorrect charges.</li>
</ol>

<h2>Common CPT Code Billing Errors to Watch For</h2>
<p><strong>Upcoding:</strong> A hospital bills CPT 99285 (Level 5 ER visit, $266 Medicare rate) when your visit was actually a Level 3 ($116). This adds $150+ to Medicare's payment — and multiples of that to what you owe.</p>

<p><strong>Unbundling:</strong> A colonoscopy with biopsy (CPT 45380, $257 Medicare rate) should be billed as a single code. Some facilities bill separately for the scope, the biopsy specimen, and the pathology — multiplying what you owe.</p>

<p><strong>Facility fees added to already-included codes:</strong> Some hospital outpatient departments add a facility fee on top of a CPT code that already includes facility overhead. This is improper double billing.</p>

<h2>Frequently Asked Questions</h2>

<h3>How do I find the CPT code on my bill?</h3>
<p>Look for a column labeled "Procedure Code," "CPT," or "Service Code" on your Explanation of Benefits (EOB) or itemized hospital bill. If you only received a summary statement, call the billing department and specifically ask for an itemized bill with CPT codes.</p>

<h3>Can a hospital charge any amount for a CPT code?</h3>
<p>Technically yes — hospitals set their own prices ("chargemaster" rates). But if your insurer has a negotiated contract, you pay the contracted rate. If you're uninsured, hospitals must offer a good-faith estimate before non-emergency services under the No Surprises Act.</p>

<h3>What does "facility rate" vs "non-facility rate" mean?</h3>
<p>Medicare publishes two rates per CPT code: a facility rate (for services provided in a hospital or outpatient department) and a non-facility rate (for office-based services). Hospital outpatient departments typically charge more than independent physician offices for identical services.</p>

<h3>What is the 3× rule for CPT code billing?</h3>
<p>A common patient-advocacy benchmark: if a hospital charges more than 3× the Medicare rate for a CPT code, the overcharge is worth disputing. Some hospitals charge 10×–20× Medicare rates for common procedures.</p>

<h3>Do CPT codes change each year?</h3>
<p>Yes. The AMA updates the CPT code set annually (effective January 1). New codes are added, others are deleted, and descriptions change. Medicare rates are also updated annually via the Medicare Physician Fee Schedule Final Rule, published each November.</p>
"""

register(_SLUG, {
    "title": "CPT Codes & Medicare Rates: The Complete Patient's Guide (2026)",
    "meta_description": "Understand CPT billing codes, look up Medicare reimbursement rates for 50 common procedures, and learn how to spot overbilling on your hospital bill.",
    "published": "2026-04-16",
    "reviewed_on": "2026-04-16",
    "author": "BillKarma Team",
    "reviewer": {"name": "BillKarma Medical Billing Research Team", "credential": "Certified Medical Billing Specialists", "profile_url": "/about/"},
    "category": "Billing Basics",
    "faqs": [
        {"q": "What is a CPT code?", "a": "A CPT (Current Procedural Terminology) code is a 5-digit number that identifies a specific medical procedure or service on your bill. Created by the American Medical Association, CPT codes are used by hospitals, doctors, and labs to bill insurance companies and Medicare for every service provided."},
        {"q": "How do I look up Medicare rates for CPT codes?", "a": "You can find Medicare rates in the CMS Medicare Physician Fee Schedule, published each year. BillKarma's Medicare rate calculator also lets you look up rates by CPT code and location. The table in this guide shows national average facility rates for 50 of the most common procedures."},
        {"q": "What is considered an overcharge on a CPT code?", "a": "A common rule of thumb is that hospital charges above 3× the Medicare rate may be overcharges worth disputing. Some hospitals charge 10–20× Medicare rates for imaging and lab tests. Compare your charged amount to the Medicare rate using the table above."},
        {"q": "Can I request an itemized bill with CPT codes?", "a": "Yes. You have the right to an itemized bill listing every CPT code and charge. Call the hospital billing department and specifically request an itemized statement. Under HIPAA, providers must supply this upon request."},
    ],
    "body": _BODY,
})
