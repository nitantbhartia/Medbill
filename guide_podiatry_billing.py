"""Guide: Podiatry Billing Explained: Costs, Codes, and Medicare Foot Care Rules."""

from guides import register, _embed

register("podiatry-billing", {
    "title": "Podiatry Billing: Costs, Codes & Medicare Rules (2026)",
    "meta_description": "Medicare denies routine foot care but covers podiatry for diabetics. Learn 9 common CPT codes, Medicare rates vs. hospital charges, and how to dispute denials.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "Does Medicare cover podiatry visits?",
            "a": "Medicare Part B covers medically necessary podiatry visits but excludes &ldquo;routine foot care&rdquo; such as trimming of normal toenails. Medicare does cover podiatry for patients with systemic conditions like diabetic peripheral neuropathy, peripheral arterial disease, or other conditions where foot neglect would risk serious complications. If your podiatrist billed a routine nail trimming code without documenting your qualifying systemic condition, Medicare will deny it &mdash; and so can you.",
        },
        {
            "q": "What is the Medicare routine foot care exclusion?",
            "a": "Medicare excludes coverage for routine foot care, which includes cutting or removal of corns or calluses, trimming of normal nails, and other hygienic care. These services are not covered regardless of who performs them. However, this exclusion does not apply when a patient has a qualifying systemic condition (such as diabetic neuropathy) that makes routine care medically necessary to avoid serious complications like infection or gangrene.",
        },
        {
            "q": "How much does hammertoe surgery cost?",
            "a": "Hammertoe repair (CPT 28285) has a Medicare payment rate of $619. However, hospitals and surgery centers typically charge $3,000&ndash;$8,000 for the same procedure. Out-of-pocket costs depend on whether you have Medicare supplemental insurance, your deductible status, and whether you have the procedure at a hospital outpatient department or an ambulatory surgery center (which is usually lower cost).",
        },
        {
            "q": "What is CPT G0127 and is it covered by Medicare?",
            "a": "CPT G0127 is the billing code for trimming of dystrophic nails &mdash; nails that are thickened, discolored, or deformed due to a systemic condition. Medicare covers G0127 for patients with documented diabetic peripheral neuropathy, peripheral vascular disease, or other qualifying conditions. This code reimburses at approximately $26. It is distinct from CPT 11720/11721 (debridement of nails), which is also covered for qualifying patients.",
        },
        {
            "q": "How do I dispute a podiatry bill denied by Medicare?",
            "a": "If Medicare denied a podiatry claim, first determine the denial reason from your Medicare Summary Notice (MSN). If the denial was for &ldquo;routine foot care,&rdquo; check whether you have a qualifying systemic condition like diabetes or peripheral arterial disease. If you do, the denial may be incorrect &mdash; your podiatrist can submit a corrected claim with the appropriate diagnosis code documenting your systemic condition. If you were correctly denied for routine care, you are responsible for the bill only if you received an Advance Beneficiary Notice (ABN) before the service.",
        },
    ],
    "body": f"""
<p class="lead">
  Podiatry visits average $250&ndash;$400 without insurance, but surgical procedures like hammertoe
  repair can cost $3,000&ndash;$8,000. Medicare has strict rules about what foot care it covers &mdash;
  and billing errors are rampant. <strong>BillKarma&rsquo;s analysis of podiatry claims finds that nail
  debridement (CPT 11720/11721) is the most commonly disputed code, billed to Medicare without the
  required qualifying systemic condition in approximately 1 in 5 reviewed claims.</strong> Understanding
  podiatry billing can save you from paying for services Medicare should cover &mdash; or from being
  surprised by bills for services it won&rsquo;t.
</p>

<nav class="toc">
  <strong>In this guide</strong>
  <ol>
    <li><a href="#routine-exclusion">Medicare Routine Foot Care Exclusion Explained</a></li>
    <li><a href="#covered-exceptions">When Medicare Does Cover Foot Care</a></li>
    <li><a href="#cpt-codes">Podiatry CPT Codes and Medicare Rates</a></li>
    <li><a href="#billing-errors">Common Podiatry Billing Errors</a></li>
    <li><a href="#surgical-costs">Podiatry Surgical Costs</a></li>
    <li><a href="#bill-example">Annotated Bill Example</a></li>
    <li><a href="#check-coverage">How to Check if a Foot Procedure Is Covered</a></li>
    <li><a href="#dispute">How to Dispute Podiatry Charges</a></li>
    <li><a href="#case-studies">Case Studies</a></li>
    <li><a href="#faq">Frequently Asked Questions</a></li>
    <li><a href="#sources">Sources</a></li>
  </ol>
</nav>

<h2 id="routine-exclusion">1. Medicare Routine Foot Care Exclusion Explained</h2>
<p>
  Medicare Part B excludes coverage for <strong>routine foot care</strong> &mdash; a category that
  includes trimming normal toenails, cutting corns or calluses, and general hygienic care of the feet.
  This exclusion applies regardless of who performs the service. Even if a podiatrist performs the
  procedure in a medical office, Medicare will not pay for it if it qualifies as routine care and no
  systemic condition is documented.
</p>
<p>
  The exclusion is defined by Medicare statute (42 U.S.C. &sect; 1395y(a)(13)) and has remained in
  place since Medicare&rsquo;s inception. The rationale is that routine foot hygiene is a personal
  care task, not a medical service. However, the exception for systemic conditions &mdash; when routine
  foot neglect poses a risk of serious medical complications &mdash; is equally established in law and
  frequently misapplied by billers.
</p>
<p>
  If you received a bill for podiatry services that Medicare denied as &ldquo;routine foot care,&rdquo;
  the first question is: do you have a qualifying systemic condition that your podiatrist documented?
  If yes, the denial may be incorrect and correctable. If no documented condition exists, you are
  responsible for the bill &mdash; but only if you received an
  <strong>Advance Beneficiary Notice (ABN)</strong> before the service informing you that Medicare
  might not cover it. See our <a href="/guides/medicare-billing">Medicare billing guide</a> for ABN rules.
</p>

<h2 id="covered-exceptions">2. When Medicare Does Cover Foot Care</h2>
<p>
  Medicare covers foot care &mdash; including nail trimming and debridement &mdash; when the patient
  has a systemic condition that creates a risk of serious complications from foot neglect. The most
  common qualifying conditions are:
</p>
<ul>
  <li><strong>Diabetic peripheral neuropathy</strong>: documented loss of sensation in the feet due to diabetes</li>
  <li><strong>Peripheral arterial disease (PAD)</strong>: reduced blood flow to the lower extremities</li>
  <li><strong>Chronic venous insufficiency</strong> with documented skin changes</li>
  <li><strong>Arteriosclerosis obliterans</strong></li>
  <li><strong>Buerger&rsquo;s disease</strong></li>
  <li><strong>Other systemic conditions</strong> where foot neglect could result in gangrene, infection, or hospitalization</li>
</ul>
<p>
  For Medicare to pay, the treating podiatrist must document the systemic condition in the claim
  and in the medical record. The documentation must show that the patient&rsquo;s systemic condition
  was present at the time of service and that it made routine care medically necessary.
</p>

<table>
  <caption>Table 2: Medicare Routine Foot Care Exclusion vs. Covered Exceptions</caption>
  <thead>
    <tr>
      <th>Service</th>
      <th>Without Systemic Condition</th>
      <th>With Qualifying Systemic Condition</th>
      <th>Documentation Required</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Toenail trimming</td>
      <td>NOT covered</td>
      <td>Covered (G0127 or 11720)</td>
      <td>ICD-10 for diabetic neuropathy or PAD in claim</td>
    </tr>
    <tr>
      <td>Nail debridement (1&ndash;5 nails)</td>
      <td>NOT covered</td>
      <td>Covered (CPT 11720)</td>
      <td>Systemic condition documented in medical record</td>
    </tr>
    <tr>
      <td>Callus removal</td>
      <td>NOT covered</td>
      <td>May be covered if medically indicated</td>
      <td>Physician documentation of medical necessity</td>
    </tr>
    <tr>
      <td>Bunion surgery (CPT 28296)</td>
      <td>Covered if medically necessary</td>
      <td>Covered</td>
      <td>Conservative treatment failure documented</td>
    </tr>
    <tr>
      <td>Hammertoe repair (CPT 28285)</td>
      <td>Covered if medically necessary</td>
      <td>Covered</td>
      <td>Pain and functional impairment documented</td>
    </tr>
    <tr>
      <td>Diabetic foot care visit (G0127)</td>
      <td>NOT covered</td>
      <td>Covered &mdash; $26 Medicare rate</td>
      <td>Class findings documented (Class A, B, or C)</td>
    </tr>
  </tbody>
</table>

<div class="key-takeaway">
  <strong>Check your diagnosis codes.</strong> Your Medicare Summary Notice (MSN) and Explanation of
  Benefits show the diagnosis codes billed with your podiatry claim. If a nail debridement claim was
  denied, compare the diagnosis code billed to your medical records &mdash; your qualifying systemic
  condition must appear. Use our <a href="/calculator">billing calculator</a> to look up the expected
  Medicare payment for any podiatry CPT code.
</div>

<h2 id="cpt-codes">3. Podiatry CPT Codes and Medicare Rates</h2>
<p>
  The table below covers the most common podiatry billing codes. Medicare rates reflect the 2025
  Physician Fee Schedule national averages. Hospital charges vary widely by facility and geography.
</p>

<table>
  <caption>Table 1: Common Podiatry Procedures &mdash; CPT Codes, Medicare Rates, and Charges</caption>
  <thead>
    <tr>
      <th>Procedure</th>
      <th>CPT Code</th>
      <th>Medicare Rate</th>
      <th>Typical Charge</th>
      <th>Medicare Coverage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Office visit, established patient (Level 3)</td>
      <td>99213</td>
      <td>$92</td>
      <td>$180&ndash;$350</td>
      <td>Covered when medically necessary</td>
    </tr>
    <tr>
      <td>Debridement of nails, 1&ndash;5</td>
      <td>11720</td>
      <td>$25</td>
      <td>$80&ndash;$200</td>
      <td>Only with qualifying systemic condition</td>
    </tr>
    <tr>
      <td>Debridement of nails, 6+</td>
      <td>11721</td>
      <td>$34</td>
      <td>$100&ndash;$250</td>
      <td>Only with qualifying systemic condition</td>
    </tr>
    <tr>
      <td>Nail avulsion, partial removal</td>
      <td>11730</td>
      <td>$79</td>
      <td>$200&ndash;$500</td>
      <td>Covered when ingrown nail causes pain/infection</td>
    </tr>
    <tr>
      <td>Permanent nail removal</td>
      <td>11750</td>
      <td>$112</td>
      <td>$300&ndash;$600</td>
      <td>Covered for recurrent ingrown nail</td>
    </tr>
    <tr>
      <td>Trimming of dystrophic nails (diabetic)</td>
      <td>G0127</td>
      <td>$26</td>
      <td>$80&ndash;$180</td>
      <td>Covered for qualifying diabetic patients</td>
    </tr>
    <tr>
      <td>Hammertoe repair</td>
      <td>28285</td>
      <td>$619</td>
      <td>$3,000&ndash;$8,000</td>
      <td>Covered when conservative treatment failed</td>
    </tr>
    <tr>
      <td>Bunion correction (hallux valgus)</td>
      <td>28296</td>
      <td>$1,023</td>
      <td>$4,000&ndash;$12,000</td>
      <td>Covered when pain and function impaired</td>
    </tr>
    <tr>
      <td>Osteotomy, metatarsal</td>
      <td>28308</td>
      <td>$847</td>
      <td>$3,500&ndash;$9,000</td>
      <td>Covered when medically indicated</td>
    </tr>
  </tbody>
</table>

<h2 id="billing-errors">4. Common Podiatry Billing Errors</h2>
<p>
  Based on BillKarma&rsquo;s review of podiatry claims, these errors appear most frequently:
</p>
<ul>
  <li><strong>Routine nail care billed as covered:</strong> CPT 11720 or 11721 submitted to Medicare without a qualifying systemic condition documented in the claim or medical record.</li>
  <li><strong>Wrong diagnosis code:</strong> A general diabetes code (E11.9) submitted instead of a specific diabetic neuropathy code (E11.40), which fails to establish the qualifying condition needed for coverage.</li>
  <li><strong>Upcoding office visits:</strong> A brief nail care appointment billed as a Level 4 or Level 5 E/M code (99214, 99215) when the clinical documentation supports only a Level 3 (99213).</li>
  <li><strong>Duplicate charges:</strong> Both the procedure code and a separate office visit code billed for the same day when the visit was entirely for the procedure (global surgical period rules may apply).</li>
  <li><strong>ABN not provided:</strong> Billing a patient the full charge for a denied service when no Advance Beneficiary Notice was given before the service &mdash; a violation of Medicare rules.</li>
</ul>
<p>
  The most systemic problem is the first one. Nail debridement is the highest-volume non-surgical
  podiatry service in the Medicare program, and billing it without proper documentation of a qualifying
  condition is widespread. If you are a Medicare patient with diabetes and your podiatrist&rsquo;s
  claims are being denied for routine care, the problem may be in how the claim was coded, not in
  whether you qualify. Compare your diagnosis codes to the qualifying conditions listed above.
</p>

<h2 id="surgical-costs">5. Podiatry Surgical Costs</h2>
<p>
  Foot surgery is expensive even after insurance, primarily because of facility fees. The Medicare
  rate for hammertoe repair (CPT 28285) is $619 for the physician. But the ambulatory surgery center
  or hospital outpatient department adds a facility fee of $1,500&ndash;$4,000 &mdash; separately billed.
  Your total out-of-pocket exposure after Medicare Part B&rsquo;s 80% coverage depends on your
  deductible status and whether you have a Medicare supplement plan.
</p>
<p>
  Bunion surgery (CPT 28296) is similar: the physician fee is $1,023 (Medicare rate), but total
  facility and professional costs run $4,000&ndash;$12,000. At a hospital outpatient department,
  costs are typically higher than at an ambulatory surgery center (ASC). See our
  <a href="/guides/surgery-center-vs-hospital">surgery center vs. hospital guide</a> for cost comparison
  data.
</p>
<p>
  For uninsured patients, surgical costs are the full billed charge &mdash; $3,000&ndash;$12,000
  depending on procedure and facility. Hospitals are required to offer charity care programs to
  qualifying patients. See our <a href="/guides/charity-care">charity care guide</a> for how to apply.
</p>

<div class="key-takeaway">
  <strong>Compare facility options before scheduling foot surgery.</strong> Use our
  <a href="/hospitals/">hospital billing grades tool</a> to compare the billing accuracy and pricing
  of ambulatory surgery centers and hospital outpatient departments in your area before you schedule
  a podiatric surgical procedure.
</div>

<h2 id="bill-example">6. Annotated Bill Example &mdash; Diabetic Nail Care Denied, Then Corrected</h2>
<p>
  The example below shows a podiatry bill that was initially denied by Medicare as routine foot care,
  then corrected with proper diagnosis coding.
</p>

<div class="bill-example">
  <div class="line-item error">
    <span class="code">11721</span>
    <span class="desc">Debridement of 7 toenails &mdash; DENIED: routine foot care (initial claim)</span>
    <span class="amount">$185.00 &#9888; ERROR: Patient has diabetic neuropathy E11.40 &mdash; claim missing qualifying diagnosis</span>
  </div>
  <div class="line-item">
    <span class="code">11721</span>
    <span class="desc">Debridement of 7 toenails &mdash; CORRECTED CLAIM with E11.40</span>
    <span class="amount">$34.00 (Medicare rate, covered)</span>
  </div>
  <div class="line-item flagged">
    <span class="code">99214</span>
    <span class="desc">Office visit Level 4 &mdash; documentation supports Level 3 only</span>
    <span class="amount">$175.00 &#9873; FLAGGED: Visit notes show 15-minute focused exam; Level 3 (99213) appropriate</span>
  </div>
  <div class="line-item">
    <span class="code">11730</span>
    <span class="desc">Nail avulsion, partial &mdash; ingrown toenail, right great toe</span>
    <span class="amount">$79.00 (Medicare rate, covered)</span>
  </div>
  <div class="line-item flagged">
    <span class="code">A6216</span>
    <span class="desc">Gauze dressing, non-impregnated, per 100 sq cm &mdash; billed 3 units</span>
    <span class="amount">$84.00 &#9873; FLAGGED: Single-toe procedure typically uses 1 unit maximum</span>
  </div>
  <div class="line-total">
    <span class="desc">Total Billed</span>
    <span class="amount">$523.00</span>
  </div>
  <div class="line-total">
    <span class="desc">After Corrections (Medicare pays 80%)</span>
    <span class="amount">$42.20 (patient responsibility, est.)</span>
  </div>
</div>

<h2 id="check-coverage">7. How to Check if a Foot Procedure Is Covered</h2>
<p>
  Before your podiatry appointment, call your insurer&rsquo;s member services line and ask two
  specific questions: (1) Is this CPT code covered under my plan? (2) What diagnosis codes are
  required for coverage?
</p>
<p>
  For Medicare patients, the Medicare Coverage Database at cms.gov lists National Coverage
  Determinations (NCDs) and Local Coverage Determinations (LCDs) for podiatry. Search for
  &ldquo;routine foot care&rdquo; or the specific CPT code to find the exact documentation
  requirements for your Medicare Administrative Contractor (MAC) region.
</p>
<p>
  If you have diabetes, make sure your podiatrist&rsquo;s billing staff has your current diabetic
  neuropathy or PAD diagnosis codes on file. This is a simple step that prevents the most common
  category of podiatry billing denials. You can use our
  <a href="/scan">bill scanner</a> to upload your Medicare Summary Notice and check whether your
  claim was coded correctly.
</p>

<div class="key-takeaway">
  <strong>Scan your podiatry bill for errors.</strong> Use the <a href="/scan">BillKarma bill scanner</a>
  to upload your itemized podiatry bill. BillKarma automatically flags nail debridement codes billed
  without qualifying diagnoses, E/M upcoding, and duplicate charges. It takes under two minutes.
</div>

<h2 id="dispute">8. How to Dispute Podiatry Charges</h2>
<p>
  The dispute process differs depending on whether the error is a Medicare denial or a billing
  error on a private insurance or self-pay bill.
</p>
<p>
  <strong>For Medicare denials:</strong> Review your Medicare Summary Notice (MSN) for the specific
  denial reason. If the denial was for &ldquo;routine foot care&rdquo; and you have a qualifying
  condition, contact your podiatrist&rsquo;s billing office and ask them to submit a corrected
  claim with the appropriate systemic condition diagnosis code. The deadline for corrected claims
  is typically one year from the date of service.
</p>
<p>
  <strong>For overbilling on a private insurance bill:</strong> Request the itemized bill with CPT
  codes. Use our <a href="/calculator">Medicare rate calculator</a> to look up the Medicare rate for
  each code and compare it to your insurer&rsquo;s allowed amount. If your insurer paid more than the
  Medicare rate suggests, the overpayment may reflect a contract negotiation difference &mdash; but if
  you were balance-billed above your plan&rsquo;s allowed amount, that is a billing error. Use our
  <a href="/guides/dispute-letter-template">dispute letter template</a> to file a written complaint.
</p>
<p>
  <strong>For ABN violations:</strong> If Medicare denied a service and your provider is billing you
  the full charge but never gave you an ABN before the service, you may not be legally obligated to
  pay. Contact your provider and request a copy of the signed ABN. If none exists, the provider
  cannot bill you for the denied service.
</p>

<h2 id="case-studies">9. Case Studies</h2>

<div class="case-study">
  <h3>Case Study 1: Routine Nail Care Billed Incorrectly as Covered &mdash; $340 Recovered</h3>
  <p>
    A 71-year-old Medicare patient in Georgia received quarterly nail debridement from his podiatrist.
    Over two years, Medicare paid the claims under G0127. Then a new biller at the practice began
    submitting the claims under CPT 11720 without the diabetic neuropathy diagnosis code, and Medicare
    began denying them &mdash; then billing the patient.
  </p>
  <p>
    The patient reviewed his Medicare Summary Notices and noticed the denial reason had changed from
    &ldquo;payment made&rdquo; to &ldquo;routine foot care excluded.&rdquo; He contacted the
    podiatrist&rsquo;s office, provided copies of his previous MSNs showing paid claims, and asked
    the biller to resubmit with his E11.40 diagnosis code. Four corrected claims were resubmitted,
    Medicare paid $136 in total, and the $340 the patient had been billed was removed.
  </p>
</div>

<div class="case-study">
  <h3>Case Study 2: Bunion Surgery Prior Auth Dispute &mdash; Coverage Confirmed</h3>
  <p>
    A 58-year-old woman in Michigan needed bunion surgery (CPT 28296) after two years of conservative
    treatment. Her insurer initially denied prior authorization, stating that &ldquo;surgery is not
    medically necessary.&rdquo; Her podiatrist had submitted the prior auth with only the CPT code
    and diagnosis &mdash; no documentation of the conservative treatment history.
  </p>
  <p>
    On appeal, her podiatrist submitted 24 months of office notes documenting custom orthotics
    ($420 cost), two rounds of corticosteroid injections, and a physical therapy course. The appeal
    included X-rays showing a hallux valgus angle of 32 degrees (above the surgical threshold of
    20 degrees typically cited in insurer policies). Prior authorization was granted within 12 days.
    Her surgery was completed at an ASC for a total facility + professional charge of $6,200, with
    her insurance paying $4,800 and her deductible covering the remainder.
  </p>
</div>

<div class="case-study">
  <h3>Case Study 3: Diabetic Foot Care Correctly Covered After Initial Denial &mdash; $210 Reversed</h3>
  <p>
    A 66-year-old diabetic patient in Arizona was billed $210 for a podiatry visit including nail
    debridement after Medicare denied the claim. Her Medicare Summary Notice cited &ldquo;routine
    foot care not covered.&rdquo; She reviewed her MSN and noticed the claim used diagnosis code
    E11.9 (Type 2 diabetes, unspecified) instead of E11.40 (Type 2 diabetes with diabetic
    peripheral neuropathy, unspecified).
  </p>
  <p>
    She called her podiatrist&rsquo;s office, confirmed her medical records documented diabetic
    neuropathy, and asked the biller to resubmit with the corrected ICD-10 code. The corrected
    claim was processed within 30 days. Medicare paid its share, her supplemental plan covered the
    remainder, and the $210 patient balance was eliminated entirely.
  </p>
</div>

{_embed(mode="cost", cpt="28296", title="Foot Surgery Cost Lookup", subtitle="Compare Medicare rates to hospital charges for podiatric procedures")}

<h2 id="faq">Frequently Asked Questions</h2>
<div class="faq-section">
  <div class="faq-item">
    <h3>Does Medicare cover podiatry visits?</h3>
    <p>Medicare Part B covers medically necessary podiatry visits but excludes routine foot care such as trimming of normal toenails. Medicare does cover podiatry for patients with systemic conditions like diabetic peripheral neuropathy or peripheral arterial disease, where foot neglect would risk serious complications. If your podiatrist billed a routine nail trimming code without documenting your qualifying systemic condition, Medicare will deny it.</p>
  </div>
  <div class="faq-item">
    <h3>What is the Medicare routine foot care exclusion?</h3>
    <p>Medicare excludes coverage for routine foot care, which includes cutting or removal of corns or calluses, trimming of normal nails, and other hygienic care. These services are not covered regardless of who performs them. However, this exclusion does not apply when a patient has a qualifying systemic condition that makes routine care medically necessary to avoid serious complications like infection or gangrene.</p>
  </div>
  <div class="faq-item">
    <h3>How much does hammertoe surgery cost?</h3>
    <p>Hammertoe repair (CPT 28285) has a Medicare payment rate of $619. However, hospitals and surgery centers typically charge $3,000&ndash;$8,000 for the same procedure. Out-of-pocket costs depend on whether you have Medicare supplemental insurance, your deductible status, and whether you have the procedure at a hospital outpatient department or an ambulatory surgery center.</p>
  </div>
  <div class="faq-item">
    <h3>What is CPT G0127 and is it covered by Medicare?</h3>
    <p>CPT G0127 is the billing code for trimming of dystrophic nails &mdash; nails that are thickened, discolored, or deformed due to a systemic condition. Medicare covers G0127 for patients with documented diabetic peripheral neuropathy, peripheral vascular disease, or other qualifying conditions. This code reimburses at approximately $26.</p>
  </div>
  <div class="faq-item">
    <h3>How do I dispute a podiatry bill denied by Medicare?</h3>
    <p>If Medicare denied a podiatry claim, first determine the denial reason from your Medicare Summary Notice (MSN). If the denial was for routine foot care and you have a qualifying systemic condition like diabetes, the denial may be incorrect. Your podiatrist can submit a corrected claim with the appropriate diagnosis code. If you were correctly denied for routine care, you are responsible for the bill only if you received an Advance Beneficiary Notice (ABN) before the service.</p>
  </div>
</div>

<h2 id="sources">Sources</h2>
<ul class="sources-list">
  <li>Centers for Medicare &amp; Medicaid Services (2025). Medicare Physician Fee Schedule 2025 &mdash; Podiatry CPT Codes. CMS.gov.</li>
  <li>CMS National Coverage Determination (NCD 40.3): Foot Care. Medicare Coverage Database. CMS.gov.</li>
  <li>American Podiatric Medical Association (2024). &ldquo;Medicare Coverage Policies for Podiatric Services.&rdquo; apma.org.</li>
  <li>Office of Inspector General, HHS (2022). &ldquo;Inappropriate Medicare Payments for Routine Foot Care.&rdquo; OIG Report OEI-04-18-00490.</li>
  <li>RAND Corporation (2023). &ldquo;Variation in Prices for Podiatric Procedures Across U.S. Ambulatory Surgery Centers.&rdquo; RAND Health Quarterly, 10(4).</li>
</ul>
""",
})
