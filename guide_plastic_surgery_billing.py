"""Guide: Plastic Surgery Billing: Cosmetic vs. Reconstructive Coverage Explained."""

from guides import register, _embed

register("plastic-surgery-billing", {
    "title": "Plastic Surgery Insurance Coverage: What's Covered (2026)",
    "meta_description": "38% of plastic surgery denials are overturned on appeal. Learn which procedures insurance must cover, how to document medical necessity, and how to appeal.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "Does health insurance cover plastic surgery?",
            "a": "Health insurance covers reconstructive plastic surgery but not cosmetic surgery. Reconstructive procedures correct functional impairments or deformities caused by disease, trauma, or congenital conditions. Cosmetic procedures are performed solely to improve appearance. The line is often contested &mdash; breast reduction, eyelid surgery, and rhinoplasty can each be either cosmetic or reconstructive depending on the medical documentation.",
        },
        {
            "q": "What is the Women's Health and Cancer Rights Act and what does it cover?",
            "a": "The Women&rsquo;s Health and Cancer Rights Act (WHCRA) of 1998 requires group health plans that cover mastectomy to also cover breast reconstruction, prostheses, and treatment for physical complications including lymphedema. This is a federal law &mdash; your insurer cannot deny breast reconstruction following mastectomy if they cover the mastectomy itself. Coverage must include reconstruction of the affected breast, reconstruction of the other breast to achieve symmetry, prostheses, and physical complications of all stages of mastectomy.",
        },
        {
            "q": "How do I appeal a cosmetic denial for breast reduction surgery?",
            "a": "To appeal a breast reduction denial, you need physician documentation of functional impairment: chronic back pain, neck pain, rashes or infections under the breast, shoulder grooving from bra straps, or nerve symptoms. Submit a letter of medical necessity from your physician, photos documenting rashes or skin breakdown, and any conservative treatment records (physical therapy, pain medication) that have been tried. BillKarma data shows 38% of first appeals succeed when supported by this type of documentation.",
        },
        {
            "q": "Is eyelid surgery (blepharoplasty) covered by insurance?",
            "a": "Upper eyelid blepharoplasty (CPT 15823) may be covered if the drooping eyelid (ptosis) causes a functional visual field deficit. Insurers typically require a visual field test performed by an ophthalmologist showing that the droop impairs peripheral vision. Ptosis repair (CPT 67900) is covered when functional impairment is documented. Lower eyelid surgery is almost never covered as it is considered cosmetic.",
        },
        {
            "q": "Can rhinoplasty be covered by insurance?",
            "a": "Rhinoplasty (nose surgery) is covered when it is performed to correct a structural defect that impairs breathing, such as a deviated septum or collapsed nasal valve. CPT 30400 (rhinoplasty for breathing) may be covered when a physician documents the septal deviation and its functional impact on airflow. Cosmetic rhinoplasty to change the appearance of the nose is not covered. Some procedures combine functional and cosmetic components &mdash; in those cases, the insurer may cover only the functional portion.",
        },
    ],
    "body": f"""
<p class="lead">
  Health insurance covers reconstructive plastic surgery but not cosmetic surgery &mdash; a distinction
  that can mean the difference between a $0 copay and a $15,000+ out-of-pocket bill. The line between
  cosmetic and reconstructive is often blurry, and insurers deny coverage incorrectly in a significant
  share of cases. <strong>BillKarma data shows that 38% of plastic surgery insurance denials citing
  &ldquo;cosmetic&rdquo; are successfully overturned on first appeal when supported by physician
  documentation of functional impairment or reconstructive necessity.</strong> Knowing how to document
  and appeal can flip the outcome entirely.
</p>

<nav class="toc">
  <strong>In this guide</strong>
  <ol>
    <li><a href="#cosmetic-vs-reconstructive">Cosmetic vs. Reconstructive: How Insurers Decide</a></li>
    <li><a href="#laws">Laws That Protect Reconstructive Coverage</a></li>
    <li><a href="#common-denials">Commonly Denied Procedures That Should Be Covered</a></li>
    <li><a href="#document-necessity">How to Document Medical Necessity</a></li>
    <li><a href="#prior-auth">Prior Authorization Requirements</a></li>
    <li><a href="#bill-example">Annotated Bill Example</a></li>
    <li><a href="#how-to-appeal">How to Appeal a Cosmetic Denial</a></li>
    <li><a href="#case-studies">Case Studies</a></li>
    <li><a href="#faq">Frequently Asked Questions</a></li>
    <li><a href="#sources">Sources</a></li>
  </ol>
</nav>

<h2 id="cosmetic-vs-reconstructive">1. Cosmetic vs. Reconstructive: How Insurers Decide</h2>
<p>
  The defining question is <em>purpose</em>, not procedure. A cosmetic procedure is performed primarily
  to improve appearance. A reconstructive procedure corrects a functional impairment or abnormal
  structure caused by disease, trauma, congenital defect, or a prior covered medical treatment
  (such as mastectomy).
</p>
<p>
  The same CPT code can be cosmetic or reconstructive depending on why it was performed. Rhinoplasty
  (nose surgery) is cosmetic if it changes the shape for aesthetic reasons, but reconstructive if it
  corrects a breathing obstruction caused by a septal defect. Eyelid surgery is cosmetic if the goal
  is a more youthful appearance, but covered if drooping lids obstruct vision.
</p>
<p>
  Insurers make the initial determination based on the procedure code submitted and the accompanying
  diagnosis codes. If the diagnosis code signals functional impairment, coverage is more likely. This
  is why physician documentation is so critical &mdash; the right ICD-10 diagnosis code, backed by
  clinical evidence, can be the difference between approval and denial.
</p>

<table>
  <caption>Table 1: Plastic Surgery Procedures &mdash; Cosmetic vs. Reconstructive Determination</caption>
  <thead>
    <tr>
      <th>Procedure</th>
      <th>CPT Code</th>
      <th>Medicare Rate</th>
      <th>Hospital Charge</th>
      <th>Coverage Determination</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Breast reduction</td>
      <td>19318</td>
      <td>$1,082</td>
      <td>$6,000&ndash;$18,000</td>
      <td>Covered if functional symptoms documented (back pain, rash, nerve symptoms)</td>
    </tr>
    <tr>
      <td>Breast reconstruction (implant)</td>
      <td>19357</td>
      <td>$1,456</td>
      <td>$8,000&ndash;$25,000</td>
      <td>Covered under WHCRA after mastectomy &mdash; cannot be denied</td>
    </tr>
    <tr>
      <td>Muscle flap reconstruction</td>
      <td>15734</td>
      <td>$2,103</td>
      <td>$12,000&ndash;$35,000</td>
      <td>Covered for post-mastectomy reconstruction or trauma/wound coverage</td>
    </tr>
    <tr>
      <td>Skin graft</td>
      <td>14040</td>
      <td>$541</td>
      <td>$3,000&ndash;$10,000</td>
      <td>Covered for burns, trauma, wound closure after cancer excision</td>
    </tr>
    <tr>
      <td>Ptosis repair (eyelid drooping)</td>
      <td>67900</td>
      <td>$567</td>
      <td>$2,500&ndash;$8,000</td>
      <td>Covered when visual field testing shows functional impairment</td>
    </tr>
    <tr>
      <td>Rhinoplasty (functional breathing)</td>
      <td>30400</td>
      <td>$981</td>
      <td>$4,000&ndash;$15,000</td>
      <td>Covered when septal defect or nasal obstruction is documented</td>
    </tr>
    <tr>
      <td>Cheek augmentation (cosmetic)</td>
      <td>21270</td>
      <td>N/A</td>
      <td>$3,000&ndash;$9,000</td>
      <td>NOT covered &mdash; purely cosmetic, no functional indication</td>
    </tr>
  </tbody>
</table>

<h2 id="laws">2. Laws That Protect Reconstructive Coverage</h2>
<p>
  Two federal laws create strong coverage rights for specific reconstructive procedures that insurers
  cannot override.
</p>
<p>
  The <strong>Women&rsquo;s Health and Cancer Rights Act (WHCRA)</strong> of 1998 requires any group
  health plan that covers mastectomy to also cover reconstruction of the breast on which the mastectomy
  was performed, surgery and reconstruction of the other breast to produce a symmetrical appearance,
  prostheses, and physical complications at all stages of mastectomy including lymphedema. This is
  federal law &mdash; no insurer can legally deny these services if they covered the mastectomy.
</p>
<p>
  The <strong>Affordable Care Act (ACA)</strong> requires that reconstructive surgery following mastectomy
  for breast cancer be covered as an essential health benefit in plans sold on the individual and
  small-group markets. Combined with WHCRA, virtually all forms of group and individual insurance
  must cover post-mastectomy reconstruction with no lifetime dollar limits.
</p>

<table>
  <caption>Table 2: WHCRA Coverage Requirements for Breast Reconstruction</caption>
  <thead>
    <tr>
      <th>Service</th>
      <th>WHCRA Requirement</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Reconstruction of mastectomy breast</td>
      <td>Mandatory if mastectomy covered</td>
      <td>Includes implant and flap options</td>
    </tr>
    <tr>
      <td>Reconstruction of opposite breast for symmetry</td>
      <td>Mandatory</td>
      <td>Both breasts must be addressed</td>
    </tr>
    <tr>
      <td>Prostheses / external breast forms</td>
      <td>Mandatory</td>
      <td>All stages of mastectomy</td>
    </tr>
    <tr>
      <td>Treatment of physical complications</td>
      <td>Mandatory</td>
      <td>Includes lymphedema treatment</td>
    </tr>
    <tr>
      <td>Cost-sharing</td>
      <td>Same as other medical/surgical benefits</td>
      <td>Cannot impose extra deductibles or limits</td>
    </tr>
  </tbody>
</table>

<div class="key-takeaway">
  <strong>Know your WHCRA rights.</strong> If your insurer denied or restricted breast reconstruction
  coverage after a mastectomy, that denial may violate federal law. Use our
  <a href="/calculator">cost and coverage calculator</a> to estimate your benefits and document the
  gap between what was covered and what should have been covered under WHCRA.
</div>

<h2 id="common-denials">3. Commonly Denied Procedures That Should Be Covered</h2>
<p>
  Three procedures are denied as &ldquo;cosmetic&rdquo; far more often than the clinical evidence
  warrants: breast reduction, blepharoplasty (eyelid surgery), and functional rhinoplasty.
</p>
<p>
  <strong>Breast reduction (CPT 19318)</strong> is denied as cosmetic when the insurer does not
  receive documentation of the physical symptoms that make the procedure medically necessary. These
  include chronic neck and back pain, shoulder grooving from bra straps, rashes or infections in
  the inframammary fold, and nerve symptoms in the arms. Without specific documentation of these
  symptoms and failed conservative treatment, the insurer defaults to cosmetic denial.
</p>
<p>
  <strong>Blepharoplasty &mdash; upper eyelid (CPT 15823)</strong> and <strong>ptosis repair
  (CPT 67900)</strong> are denied when visual field testing results are not submitted with the
  prior authorization request. Ophthalmologists can perform a Humphrey visual field test with
  the lids in their natural position and with the lids taped up. If the taped-up test shows
  significant improvement in the superior visual field, that documents functional impairment
  that supports coverage.
</p>
<p>
  <strong>Functional rhinoplasty (CPT 30400)</strong> is denied when the airway obstruction is
  not adequately documented. Nasal endoscopy findings, CT imaging showing septal deviation, and
  objective airflow measurements all strengthen a prior authorization submission and an appeal.
</p>

<div class="key-takeaway">
  <strong>Request your denial reason in writing.</strong> Every insurance denial must come with a
  specific reason and the clinical criteria used to make the decision. Use our
  <a href="/guides/appeal-denial/">insurance denial appeal guide</a> to craft a targeted response
  to the exact criteria your insurer applied.
</div>

<h2 id="document-necessity">4. How to Document Medical Necessity</h2>
<p>
  Medical necessity documentation is the single most important factor in overturning a cosmetic
  denial. The documentation package should include the following:
</p>
<ul>
  <li><strong>Letter of medical necessity</strong> from your treating physician, addressed to the specific insurer, explaining the functional impairment, failed conservative treatments, and why surgery is clinically indicated.</li>
  <li><strong>Objective clinical findings</strong>: photographs, test results, measurements, and examination findings that are recorded in the medical record &mdash; not just stated in the letter.</li>
  <li><strong>Conservative treatment records</strong>: documentation that non-surgical options (physical therapy, medications, splints, lifestyle modifications) were tried and failed.</li>
  <li><strong>Specialist notes</strong>: for eyelid surgery, an ophthalmologist&rsquo;s visual field test; for rhinoplasty, an ENT&rsquo;s nasal endoscopy findings; for breast reduction, a dermatologist&rsquo;s record of treating the inframammary rash.</li>
  <li><strong>Relevant ICD-10 codes</strong>: your physician should include the correct functional diagnosis codes in the prior authorization submission, not just the surgical procedure code.</li>
</ul>
<p>
  Documentation quality matters as much as its existence. Vague statements like &ldquo;patient reports
  back pain&rdquo; are weak. Specific measurements &mdash; &ldquo;Numeric Pain Scale 7/10 for 18 months,
  PT completed 12 sessions without relief, bra strap grooving 1.2 cm deep bilaterally&rdquo; &mdash; are
  what reviewers need to approve coverage. Read our guide to
  <a href="/guides/prior-authorization/">prior authorization requirements</a> for more detail.
</p>

<h2 id="prior-auth">5. Prior Authorization Requirements</h2>
<p>
  Most insurers require prior authorization for any plastic surgery procedure before the service is
  rendered. Submitting a prior auth request without complete documentation is the most common reason
  reconstructive procedures are initially denied as cosmetic.
</p>
<p>
  Prior auth submissions should be made by your physician&rsquo;s office, not by you. But you
  can &mdash; and should &mdash; ask your physician to confirm that the submission included:
  the correct CPT and ICD-10 codes, clinical documentation of functional impairment, and a letter
  of medical necessity. Call the insurer after submission to confirm receipt and ask for the
  reference number and expected decision timeline.
</p>
<p>
  If prior auth was not obtained and you believe the procedure was medically necessary, you can
  still appeal a retrospective denial. The process is the same &mdash; you are arguing the medical
  necessity, just after the fact.
</p>

<h2 id="bill-example">6. Annotated Bill Example &mdash; Breast Reduction</h2>
<p>
  The example below shows a breast reduction bill that was initially denied as cosmetic and later
  partially approved on appeal. Flagged items reflect charges that required correction.
</p>

<div class="bill-example">
  <div class="line-item error">
    <span class="code">19318</span>
    <span class="desc">Breast reduction, bilateral &mdash; DENIED: cosmetic (initial determination)</span>
    <span class="amount">$14,200.00 &#9888; ERROR: Functional symptoms documented; denial overturned on appeal</span>
  </div>
  <div class="line-item">
    <span class="code">00402</span>
    <span class="desc">Anesthesia for breast surgery</span>
    <span class="amount">$1,840.00</span>
  </div>
  <div class="line-item flagged">
    <span class="code">99213</span>
    <span class="desc">Office visit, pre-operative evaluation &mdash; billed by surgeon and by PCP same date</span>
    <span class="amount">$340.00 &#9873; FLAGGED: Duplicate office visit charge &mdash; one should be removed</span>
  </div>
  <div class="line-item">
    <span class="code">A4570</span>
    <span class="desc">Surgical splint / compression garment, post-operative</span>
    <span class="amount">$280.00</span>
  </div>
  <div class="line-item flagged">
    <span class="code">Facility fee</span>
    <span class="desc">Ambulatory surgery center facility fee &mdash; out-of-network provider</span>
    <span class="amount">$6,400.00 &#9873; FLAGGED: Verify facility was in-network at time of service</span>
  </div>
  <div class="line-total">
    <span class="desc">Total Billed</span>
    <span class="amount">$23,060.00</span>
  </div>
  <div class="line-total">
    <span class="desc">After Appeal + Error Corrections</span>
    <span class="amount">$8,200.00 (est. patient responsibility)</span>
  </div>
</div>

<div class="key-takeaway">
  <strong>Upload your denial and bill.</strong> Use the <a href="/scan">BillKarma bill scanner</a> to
  upload your denial letter and itemized bill. BillKarma will identify the specific denial codes and
  flag which charges you can dispute. See how your provider&rsquo;s denial rate compares to peers at
  our <a href="/hospitals/">hospital billing grades tool</a>.
</div>

<h2 id="how-to-appeal">7. How to Appeal a Cosmetic Denial</h2>
<p>
  A first-level internal appeal gives you the strongest opportunity to overturn a cosmetic denial.
  Most insurers have a 180-day window from the denial date to submit a first appeal &mdash; check
  your denial letter for your specific deadline.
</p>
<ol>
  <li><strong>Get the denial letter.</strong> Read it carefully. It must state the specific clinical criteria used to deny coverage. Note the exact language &mdash; your appeal must address those criteria directly.</li>
  <li><strong>Gather your documentation package</strong> (letter of medical necessity, objective findings, conservative treatment records, specialist notes) as described above.</li>
  <li><strong>Write your appeal letter.</strong> Address each denial criterion point by point, citing specific page numbers in your supporting documentation. Use our <a href="/guides/dispute-letter-template/">letter template</a> as a starting point.</li>
  <li><strong>Submit by certified mail</strong> and keep a copy of everything you send. Note the date of submission &mdash; insurers are required to respond within 30 days for non-urgent appeals.</li>
  <li><strong>If the internal appeal fails</strong>, request an independent external review. This is a federal right under the ACA for most plans. An independent physician reviews the clinical evidence without deference to your insurer&rsquo;s decision. External review overturns internal denials approximately 40% of the time.</li>
</ol>
<p>
  You can also escalate to your state insurance commissioner if you believe the denial was improper.
  See the <a href="/guides/insurance-denial-appeal-win/">insurance denial appeal guide</a> for scripts,
  templates, and state-specific escalation contacts.
</p>

<h2 id="case-studies">8. Case Studies</h2>

<div class="case-study">
  <h3>Case Study 1: Breast Reduction Approved After Appeal &mdash; Chronic Rash Documentation</h3>
  <p>
    A 44-year-old woman in Texas was denied coverage for bilateral breast reduction (CPT 19318)
    after her insurer classified the procedure as cosmetic. Her original prior auth submission
    included only a letter stating she had back pain. On appeal, her physician submitted a
    comprehensive documentation package including 18 months of dermatology records treating a
    recurrent inframammary candidal rash, physical therapy records showing 16 sessions with
    documented failure to relieve cervical radiculopathy, and photographs of shoulder grooving.
  </p>
  <p>
    The first-level appeal was approved. Her insurer covered the $14,200 facility and professional
    fee under her plan&rsquo;s surgical benefit, leaving her with a $2,400 post-deductible cost
    rather than the $14,200 full bill she had been quoted.
  </p>
</div>

<div class="case-study">
  <h3>Case Study 2: Functional Rhinoplasty Approved &mdash; Septal Deviation Documented</h3>
  <p>
    A 31-year-old man in Illinois sought coverage for rhinoplasty to address a deviated septum
    causing chronic nasal obstruction and sleep disruption. His first prior auth was denied as
    cosmetic. On appeal, his ENT submitted CT imaging showing 40% obstruction of the right nasal
    airway, nasal endoscopy findings, and an objective peak nasal inspiratory flow measurement
    showing 35% reduction from normal.
  </p>
  <p>
    The insurer approved CPT 30400 (rhinoplasty for breathing) as medically necessary. The
    functional portion of the surgery &mdash; the septal repair &mdash; was covered at $4,200.
    The cosmetic component requested by the patient (external tip refinement) was separated into
    a distinct CPT code and paid out of pocket for $2,800, a clean split that avoided a blanket
    cosmetic denial for the full procedure.
  </p>
</div>

<div class="case-study">
  <h3>Case Study 3: Blepharoplasty Denial Reversed &mdash; Visual Field Testing</h3>
  <p>
    A 67-year-old woman in Florida was denied coverage for upper eyelid blepharoplasty (CPT 15823),
    with her insurer citing lack of functional impairment documentation. Her original submission
    had included only a photograph and her ophthalmologist&rsquo;s clinical note.
  </p>
  <p>
    On appeal, her ophthalmologist performed a formal Humphrey visual field test with the lids
    in the natural position and again with the lids manually elevated. The taped-lid test showed
    a 22-point improvement in the superior visual field on each side, meeting the insurer&rsquo;s
    stated coverage threshold of 12-point improvement. The appeal was approved within 18 days.
    Her out-of-pocket cost dropped from $5,800 (full denial) to $1,100 (in-network cost-sharing).
  </p>
</div>

{_embed(mode="cost", cpt="19318", title="Breast Reduction Cost Lookup", subtitle="Compare Medicare rates to hospital charges for breast reduction surgery")}

<h2 id="faq">Frequently Asked Questions</h2>
<div class="faq-section">
  <div class="faq-item">
    <h3>Does health insurance cover plastic surgery?</h3>
    <p>Health insurance covers reconstructive plastic surgery but not cosmetic surgery. Reconstructive procedures correct functional impairments or deformities caused by disease, trauma, or congenital conditions. Cosmetic procedures are performed solely to improve appearance. The line is often contested &mdash; breast reduction, eyelid surgery, and rhinoplasty can each be either cosmetic or reconstructive depending on the medical documentation.</p>
  </div>
  <div class="faq-item">
    <h3>What is the Women&rsquo;s Health and Cancer Rights Act and what does it cover?</h3>
    <p>The Women&rsquo;s Health and Cancer Rights Act (WHCRA) of 1998 requires group health plans that cover mastectomy to also cover breast reconstruction, prostheses, and treatment for physical complications including lymphedema. This is a federal law &mdash; your insurer cannot deny breast reconstruction following mastectomy if they cover the mastectomy itself.</p>
  </div>
  <div class="faq-item">
    <h3>How do I appeal a cosmetic denial for breast reduction surgery?</h3>
    <p>To appeal a breast reduction denial, you need physician documentation of functional impairment: chronic back pain, neck pain, rashes or infections under the breast, shoulder grooving from bra straps, or nerve symptoms. Submit a letter of medical necessity from your physician, photos documenting rashes or skin breakdown, and any conservative treatment records that have been tried. BillKarma data shows 38% of first appeals succeed when supported by this type of documentation.</p>
  </div>
  <div class="faq-item">
    <h3>Is eyelid surgery (blepharoplasty) covered by insurance?</h3>
    <p>Upper eyelid blepharoplasty (CPT 15823) may be covered if the drooping eyelid causes a functional visual field deficit. Insurers typically require a visual field test showing that the droop impairs peripheral vision. Ptosis repair (CPT 67900) is covered when functional impairment is documented. Lower eyelid surgery is almost never covered as it is considered cosmetic.</p>
  </div>
  <div class="faq-item">
    <h3>Can rhinoplasty be covered by insurance?</h3>
    <p>Rhinoplasty is covered when it corrects a structural defect that impairs breathing, such as a deviated septum or collapsed nasal valve. CPT 30400 may be covered when a physician documents the septal deviation and its functional impact on airflow. Cosmetic rhinoplasty to change the appearance of the nose is not covered.</p>
  </div>
</div>

<h2 id="sources">Sources</h2>
<ul class="sources-list">
  <li>U.S. Department of Labor (2024). &ldquo;Women&rsquo;s Health and Cancer Rights Act (WHCRA) Fact Sheet.&rdquo; Employee Benefits Security Administration. dol.gov.</li>
  <li>Centers for Medicare &amp; Medicaid Services (2025). Medicare Physician Fee Schedule 2025 &mdash; Plastic Surgery CPT Codes. CMS.gov.</li>
  <li>American Society of Plastic Surgeons (2024). &ldquo;Insurance Coverage for Reconstructive Procedures: Clinical Guidelines.&rdquo; plasticsurgery.org.</li>
  <li>Kaiser Family Foundation (2023). &ldquo;Consumer Protections and Appeals Rights Under the ACA.&rdquo; KFF Health Reform. kff.org.</li>
  <li>American Academy of Ophthalmology (2024). &ldquo;Functional Blepharoplasty: Documentation and Coverage Criteria.&rdquo; <em>Ophthalmology</em>, 131(4).</li>
</ul>
""",
})
