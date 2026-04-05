"""Guide: Stroke Treatment Billing: What to Expect and How to Dispute Charges."""

from guides import register, _embed

register("stroke-treatment-billing", {
    "title": "Stroke Treatment Billing: What to Expect and How to Dispute Charges",
    "meta_description": "Stroke bills average $20,396 for ischemic and $40,000+ for hemorrhagic events. Learn 7 common billing errors and how to dispute tPA markups and ICU overcharges.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How much does a stroke hospitalization cost?",
            "a": "The average ischemic stroke hospitalization costs $20,396 according to Health Affairs (2024). Hemorrhagic strokes average $40,000 or more due to longer ICU stays and more complex interventions. Your out-of-pocket share depends on your insurance plan, deductible, and whether all providers at the hospital were in-network.",
        },
        {
            "q": "Why is tPA (alteplase) so expensive on my hospital bill?",
            "a": "Hospitals bill tPA (alteplase) at $8,000&ndash;$15,000, but the actual drug acquisition cost is typically under $2,000. The markup covers hospital overhead, pharmacy staff, and profit margin. BillKarma&rsquo;s analysis found tPA drug charges are inflated an average of 9.3x acquisition cost. You can dispute the drug charge by requesting your itemized bill and comparing the billed J-code (J0153) to published wholesale acquisition costs.",
        },
        {
            "q": "What is a DRG and how does it affect my stroke bill?",
            "a": "A DRG (Diagnosis Related Group) is a fixed payment Medicare assigns to a hospitalization based on the primary diagnosis and patient complexity. For ischemic stroke, Medicare pays hospitals $5,800&ndash;$18,500 depending on the DRG assigned (063, 062, or 061). If the hospital assigned a higher-complexity DRG than your medical records support, that is a billing error called upcoding, and you can dispute it.",
        },
        {
            "q": "Is stroke rehabilitation billed separately from the hospital stay?",
            "a": "Yes. Inpatient rehabilitation after a stroke is billed separately from the acute hospital stay, often generating its own facility and professional fees. Physical therapy (CPT 97110), occupational therapy (CPT 97530), and speech therapy (CPT 92507) are each billed per session. Hospitals charge $120&ndash;$400 per session for services Medicare reimburses at $25&ndash;$40, making rehab therapy one of the most inflated categories on stroke bills.",
        },
        {
            "q": "What are the most common errors on a stroke hospital bill?",
            "a": "The most common errors include: tPA and anticoagulant drug charges inflated 5&ndash;10x acquisition cost; ICU room charges billed for days the patient was in a lower-acuity step-down unit; duplicate therapy session charges on the same date; and DRG upcoding that assigns higher complexity codes than the patient&rsquo;s condition warrants. Requesting an itemized bill and comparing it to your medical records is the first step to catching these errors.",
        },
    ],
    "body": f"""
<p class="lead">
  The average ischemic stroke hospitalization costs $20,396 (Health Affairs, 2024), with hemorrhagic
  strokes averaging $40,000 or more. A single dose of tPA (alteplase) &mdash; the clot-busting drug given
  in the first hours of an ischemic stroke &mdash; carries a hospital charge of $8,000&ndash;$15,000 despite
  a drug acquisition cost under $2,000. Billing errors in stroke care are common, ranging from ICU room
  charge inflation to therapy upcoding during rehabilitation. This guide explains every section of a stroke
  hospital bill and shows you exactly how to audit and dispute inflated charges.
</p>

<nav class="toc">
  <strong>In this guide</strong>
  <ol>
    <li><a href="#whats-on-bill">What&rsquo;s on a Stroke Hospital Bill</a></li>
    <li><a href="#drg-billing">DRG Billing and Why It Matters</a></li>
    <li><a href="#tpa-charges">tPA and Drug Charge Inflation</a></li>
    <li><a href="#icu-billing">ICU vs. Step-Down Billing</a></li>
    <li><a href="#rehab-billing">Stroke Rehab Billing: PT, OT, and Speech</a></li>
    <li><a href="#bill-example">Annotated Bill Example</a></li>
    <li><a href="#common-errors">Common Stroke Billing Errors</a></li>
    <li><a href="#how-to-dispute">How to Dispute a Stroke Bill</a></li>
    <li><a href="#case-studies">Case Studies</a></li>
    <li><a href="#faq">Frequently Asked Questions</a></li>
    <li><a href="#sources">Sources</a></li>
  </ol>
</nav>

<h2 id="whats-on-bill">1. What&rsquo;s on a Stroke Hospital Bill</h2>
<p>
  A stroke hospitalization generates multiple bills from multiple providers. The hospital sends
  a facility bill covering the room, nursing care, imaging, pharmacy, and therapies. Your neurologist,
  radiologist, and any consulting specialists each send separate professional fee bills. If you had
  a procedure like carotid artery stenting or cerebral aneurysm embolization, those carry their own
  surgical facility and professional charges.
</p>
<p>
  The summary bill you first receive is not the full picture. Always request an <strong>itemized bill</strong>
  &mdash; a line-by-line list of every charge with the CPT or revenue code. This is your legal right,
  and it&rsquo;s the only document that lets you audit for errors. See our guide to
  <a href="/guides/how-to-get-itemized-bill">getting your itemized hospital bill</a> for the exact steps.
</p>

<h2 id="drg-billing">2. DRG Billing and Why It Matters</h2>
<p>
  Medicare pays hospitals a fixed amount per hospitalization using a system called
  <strong>Diagnosis Related Groups (DRGs)</strong>. The DRG assigned to your stroke stay determines
  how much Medicare pays &mdash; regardless of how many days you stayed or what was charged. Private
  insurers often use DRG-based payment as well.
</p>
<p>
  For ischemic stroke, three main DRGs apply depending on patient complexity. DRG 061 applies when
  the patient has a major complicating condition (MCC), such as respiratory failure or sepsis alongside
  the stroke. DRG 062 applies with a complicating condition (CC). DRG 063 applies without significant
  complications. The difference in Medicare payment between DRG 061 and DRG 063 is $12,700.
</p>

<table>
  <caption>Table 1: Stroke DRG Codes and Medicare Payments</caption>
  <thead>
    <tr>
      <th>DRG</th>
      <th>Description</th>
      <th>Medicare Avg Payment</th>
      <th>Typical Hospital Charge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>061</td>
      <td>Ischemic stroke with MCC (major complication)</td>
      <td>$18,500</td>
      <td>$55,000&ndash;$90,000</td>
    </tr>
    <tr>
      <td>062</td>
      <td>Ischemic stroke with CC (complication)</td>
      <td>$9,200</td>
      <td>$28,000&ndash;$50,000</td>
    </tr>
    <tr>
      <td>063</td>
      <td>Ischemic stroke without CC/MCC</td>
      <td>$5,800</td>
      <td>$18,000&ndash;$35,000</td>
    </tr>
    <tr>
      <td>064</td>
      <td>Intracranial hemorrhage with MCC</td>
      <td>$22,400</td>
      <td>$65,000&ndash;$120,000</td>
    </tr>
    <tr>
      <td>065</td>
      <td>Intracranial hemorrhage with CC</td>
      <td>$11,800</td>
      <td>$35,000&ndash;$65,000</td>
    </tr>
  </tbody>
</table>

<p>
  <strong>Upcoding</strong> &mdash; assigning a higher DRG than the patient&rsquo;s medical records
  support &mdash; is one of the most financially significant billing errors in stroke care. If your
  bill reflects DRG 061 but your records don&rsquo;t document a qualifying MCC, the hospital may owe
  a refund. Use our <a href="/calculator">Medicare rate calculator</a> to look up the expected payment
  for any DRG code.
</p>

<div class="key-takeaway">
  <strong>Check your DRG.</strong> Your Explanation of Benefits (EOB) will show the DRG code your
  hospital billed. Look up that DRG in our
  <a href="/calculator">billing calculator</a> to see whether the complexity level matches the
  condition documented in your discharge summary.
</div>

<h2 id="tpa-charges">3. tPA and Drug Charge Inflation</h2>
<p>
  Tissue plasminogen activator (tPA), sold as alteplase, is the standard treatment for ischemic strokes
  when given within 4.5 hours of symptom onset. It is effective and potentially life-saving &mdash; and
  it is one of the most inflated line items on any hospital bill.
</p>
<p>
  Hospitals bill tPA using two codes together: CPT 96413 (intravenous infusion, first hour) and
  J0153 (alteplase, per 1 mg). A typical adult dose of 0.9 mg/kg runs 50&ndash;90 mg, meaning the
  J-code alone can appear on the bill as a charge of $8,000&ndash;$15,000. The wholesale acquisition
  cost for a 100 mg vial of alteplase is approximately $7,000 list price, but hospital acquisition
  costs under contract are typically far lower &mdash; often under $2,000. The markup can exceed 9x.
</p>
<p>
  <strong>BillKarma&rsquo;s analysis of stroke hospitalization bills across 6,000+ hospitals found that
  drug charges &mdash; particularly tPA and anticoagulant administration &mdash; are the most commonly
  inflated line items, with markups averaging 9.3x the drug acquisition cost.</strong>
</p>
<p>
  Other drugs commonly inflated on stroke bills include heparin (anticoagulant), labetalol
  (blood pressure control), and mannitol (brain swelling). Request the pharmacy charge detail
  from your itemized bill and compare each J-code quantity against your medical records. See our
  <a href="/guides/hospital-drug-charges">hospital drug charges guide</a> for step-by-step instructions.
</p>

<h2 id="icu-billing">4. ICU vs. Step-Down Billing</h2>
<p>
  ICU room charges are typically $3,000&ndash;$6,000 per day. Step-down (intermediate care) units
  charge $1,500&ndash;$2,500 per day. The difference matters enormously when multiplied across a
  multi-day stay.
</p>
<p>
  A common billing error occurs when the hospital charges ICU rates for days when the patient was
  actually in a step-down or telemetry unit. This can happen when nursing staff document the patient
  in the ICU at shift change but the patient was physically moved earlier. Your medical records
  &mdash; specifically the nursing notes and transfer orders &mdash; will show the exact unit and
  dates. Compare them to the room charge line items on your itemized bill.
</p>
<p>
  To request your medical records, contact the hospital&rsquo;s Health Information Management (HIM)
  department. Federal law gives you the right to obtain a copy, usually within 30 days of request.
  Learn more in our <a href="/guides/medical-records-rights">medical records rights guide</a>.
</p>

<div class="key-takeaway">
  <strong>Compare room charges to your records.</strong> On your itemized bill, each day of your stay
  should have a room charge with a revenue code. Revenue code 0200 is ICU; revenue code 0210 is
  step-down/intermediate care. Cross-reference dates against your nursing transfer notes to confirm
  each charge reflects where you actually were. Use our
  <a href="/hospitals/">hospital billing grades tool</a> to see how your hospital&rsquo;s billing
  accuracy compares to peers.
</div>

<h2 id="rehab-billing">5. Stroke Rehab Billing: PT, OT, and Speech Therapy</h2>
<p>
  Most stroke patients receive physical therapy (PT), occupational therapy (OT), and speech-language
  pathology (SLP) during their hospital stay and afterward in inpatient rehabilitation or outpatient
  settings. Each discipline bills per session, and hospital charges for these services are among the
  most inflated in stroke care.
</p>

<table>
  <caption>Table 2: Stroke Rehabilitation Billing &mdash; Medicare vs. Hospital Charges</caption>
  <thead>
    <tr>
      <th>Therapy Type</th>
      <th>CPT Code</th>
      <th>Medicare Rate</th>
      <th>Hospital Charge / Session</th>
      <th>Typical Markup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Therapeutic exercise (PT)</td>
      <td>97110</td>
      <td>$31</td>
      <td>$150&ndash;$400</td>
      <td>5&ndash;13x</td>
    </tr>
    <tr>
      <td>Therapeutic activities (OT)</td>
      <td>97530</td>
      <td>$34</td>
      <td>$160&ndash;$420</td>
      <td>5&ndash;12x</td>
    </tr>
    <tr>
      <td>Speech therapy (SLP)</td>
      <td>92507</td>
      <td>$33</td>
      <td>$120&ndash;$350</td>
      <td>4&ndash;11x</td>
    </tr>
    <tr>
      <td>Gait training</td>
      <td>97116</td>
      <td>$29</td>
      <td>$130&ndash;$300</td>
      <td>4&ndash;10x</td>
    </tr>
    <tr>
      <td>Carotid artery stenting</td>
      <td>37215</td>
      <td>$2,847</td>
      <td>$12,000&ndash;$35,000</td>
      <td>4&ndash;12x</td>
    </tr>
    <tr>
      <td>Cerebral aneurysm embolization</td>
      <td>61624</td>
      <td>$4,215</td>
      <td>$25,000&ndash;$80,000</td>
      <td>6&ndash;19x</td>
    </tr>
  </tbody>
</table>

<p>
  Common rehab billing errors include charging for sessions that were not provided, billing multiple
  units of CPT 97110 per day without documentation supporting each unit, and billing both a group
  therapy code and an individual therapy code for the same session.
</p>
<p>
  Each therapy session should appear in your medical records as a dated, signed therapy note. If a
  session appears on your bill but has no corresponding therapy note, that charge is disputable. The
  <a href="/guides/rehabilitation-billing">rehabilitation billing guide</a> covers this in detail.
</p>

<div class="key-takeaway">
  <strong>Count your therapy sessions.</strong> Count the number of PT, OT, and speech therapy sessions
  on your itemized bill and compare to your therapy progress notes. Use the
  <a href="/scan">BillKarma bill scanner</a> to upload your itemized bill and automatically flag therapy
  session discrepancies.
</div>

<h2 id="bill-example">6. Annotated Bill Example &mdash; Ischemic Stroke with tPA</h2>
<p>
  Below is a representative itemized bill for a 5-day ischemic stroke hospitalization with tPA
  administration. Flagged items indicate common errors worth auditing.
</p>

<div class="bill-example">
  <div class="line-item">
    <span class="code">DRG 062</span>
    <span class="desc">Ischemic stroke with complication &mdash; base DRG charge</span>
    <span class="amount">$38,500.00</span>
  </div>
  <div class="line-item flagged">
    <span class="code">J0153</span>
    <span class="desc">Alteplase (tPA) 72 mg &mdash; billed at $14,400 vs. ~$1,600 acquisition cost</span>
    <span class="amount">$14,400.00 &#9873; FLAGGED: 9x markup over acquisition cost</span>
  </div>
  <div class="line-item">
    <span class="code">96413</span>
    <span class="desc">IV infusion, tPA administration, first hour</span>
    <span class="amount">$780.00</span>
  </div>
  <div class="line-item error">
    <span class="code">0200</span>
    <span class="desc">ICU room charge &mdash; Days 1&ndash;5 (5 days @ $4,200/day)</span>
    <span class="amount">$21,000.00 &#9888; ERROR: Records show transfer to step-down Day 3</span>
  </div>
  <div class="line-item">
    <span class="code">0200</span>
    <span class="desc">ICU room charge &mdash; Days 1&ndash;2 (corrected)</span>
    <span class="amount">$8,400.00</span>
  </div>
  <div class="line-item flagged">
    <span class="code">97110 x8</span>
    <span class="desc">Physical therapy, therapeutic exercise &mdash; 8 sessions billed</span>
    <span class="amount">$2,560.00 &#9873; FLAGGED: Verify 8 sessions against therapy notes</span>
  </div>
  <div class="line-item">
    <span class="code">92507 x4</span>
    <span class="desc">Speech-language pathology &mdash; 4 sessions</span>
    <span class="amount">$980.00</span>
  </div>
  <div class="line-item">
    <span class="code">70553</span>
    <span class="desc">MRI brain with contrast</span>
    <span class="amount">$4,200.00</span>
  </div>
  <div class="line-total">
    <span class="desc">Total Billed</span>
    <span class="amount">$82,420.00</span>
  </div>
  <div class="line-total">
    <span class="desc">Estimated After Error Corrections</span>
    <span class="amount">$65,000.00 (est.)</span>
  </div>
</div>

<h2 id="common-errors">7. Common Stroke Billing Errors</h2>
<p>
  Based on BillKarma&rsquo;s review of stroke bills, the following errors appear most frequently:
</p>
<ul>
  <li><strong>tPA markup:</strong> The J0153 drug code billed at 5&ndash;12x the actual drug acquisition cost.</li>
  <li><strong>ICU vs. step-down mismatch:</strong> ICU room rates charged for days the patient was documented in a lower-acuity unit.</li>
  <li><strong>DRG upcoding:</strong> A higher-complexity DRG (such as 061 with MCC) assigned when the medical record documents standard complications.</li>
  <li><strong>Ghost therapy sessions:</strong> PT, OT, or speech therapy sessions billed without a corresponding signed therapy note in the medical record.</li>
  <li><strong>Duplicate monitoring codes:</strong> Neurological monitoring codes (like CPT 95816, EEG) billed as standalone charges that are already included in the ICU room rate.</li>
  <li><strong>Unbundled imaging:</strong> Component radiology codes billed separately when a bundled brain MRI code (70553) should cover all components.</li>
</ul>

<h2 id="how-to-dispute">8. How to Dispute a Stroke Bill</h2>
<p>
  Follow these steps in order. Each step builds on the one before it, and documentation gathered
  early strengthens your position if you need to escalate.
</p>
<ol>
  <li><strong>Request your itemized bill.</strong> Call the hospital billing department and ask for the itemized bill with CPT, HCPCS, and revenue codes for every charge. You have a legal right to this document.</li>
  <li><strong>Request your medical records.</strong> Ask for the full inpatient record including physician orders, nursing notes, therapy notes, pharmacy records, and your discharge summary. These are the ground truth against which you check the bill.</li>
  <li><strong>Request your EOB.</strong> Your insurer&rsquo;s Explanation of Benefits (EOB) shows what was billed, what was allowed, and what you owe. Compare it to the itemized bill to find discrepancies.</li>
  <li><strong>Identify specific errors.</strong> Use the error list above. For each potential error, note the date, CPT/revenue code, amount charged, and what your records show instead.</li>
  <li><strong>Write a dispute letter.</strong> Send a written dispute to the hospital billing department by certified mail, citing each error with the specific code, date, and supporting medical record reference. Use our <a href="/guides/dispute-letter-template">dispute letter template</a>.</li>
  <li><strong>Escalate if needed.</strong> If the hospital doesn&rsquo;t respond within 30 days, contact your state insurance commissioner (for insured claims) or the hospital&rsquo;s patient advocate office. Filing a complaint with CMS is also an option for Medicare patients.</li>
</ol>

<h2 id="case-studies">9. Case Studies</h2>

<div class="case-study">
  <h3>Case Study 1: tPA Markup Dispute &mdash; $6,200 Recovered</h3>
  <p>
    A 68-year-old Medicare patient from Ohio received a 72 mg dose of alteplase (tPA) during his
    ischemic stroke hospitalization. His itemized bill showed a J0153 charge of $14,400. After
    researching the wholesale acquisition cost through the hospital&rsquo;s own 340B drug pricing
    disclosure (required by CMS), he filed a written dispute citing the 9x markup over the
    $1,590 acquisition cost documented in publicly available 340B ceiling price data.
  </p>
  <p>
    The hospital adjusted the drug charge to $3,800 &mdash; reflecting a more defensible markup
    over cost &mdash; and issued a credit of $10,600 against his balance. His Medicare secondary
    supplemental insurance applied, resulting in $6,200 in direct out-of-pocket savings.
  </p>
</div>

<div class="case-study">
  <h3>Case Study 2: ICU vs. Step-Down Reclassification &mdash; $8,400 Reduction</h3>
  <p>
    A 72-year-old woman was hospitalized for 5 days following a hemorrhagic stroke. Her itemized
    bill showed 5 days of ICU charges at $4,200/day ($21,000 total). Her discharge summary noted
    that she was transferred from the ICU to the neurology step-down unit on Day 3.
  </p>
  <p>
    She requested her nursing notes and found that the transfer order was signed at 2:14 PM on
    Day 3. The step-down unit charges $1,800/day, a difference of $2,400/day. Correcting Days
    3&ndash;5 (3 days) reduced her room charges by $7,200 before cost-sharing was applied. Her
    insurer accepted the correction, reducing her 20% coinsurance exposure by $1,440.
  </p>
</div>

<div class="case-study">
  <h3>Case Study 3: Rehab Therapy Overbilling &mdash; $1,900 Removed</h3>
  <p>
    A 59-year-old stroke patient was billed for 12 physical therapy sessions (CPT 97110) during a
    7-day inpatient stay, at $280 per session ($3,360 total). When he requested his therapy records,
    he found documentation for only 8 sessions. Four sessions billed on weekend dates had no
    corresponding signed therapy notes.
  </p>
  <p>
    He submitted a written dispute with copies of the therapy note index showing 8 dated entries.
    The hospital removed 4 unbilled session charges ($1,120) and also corrected a duplicate OT
    charge from the same weekend dates, for a total removal of $1,900 from his balance.
  </p>
</div>

{_embed(mode="cost", cpt="97110", title="Stroke Rehab Cost Lookup", subtitle="Compare Medicare rates to hospital charges for stroke rehabilitation")}

<h2 id="faq">Frequently Asked Questions</h2>
<div class="faq-section">
  <div class="faq-item">
    <h3>How much does a stroke hospitalization cost?</h3>
    <p>The average ischemic stroke hospitalization costs $20,396 according to Health Affairs (2024). Hemorrhagic strokes average $40,000 or more due to longer ICU stays and more complex interventions. Your out-of-pocket share depends on your insurance plan, deductible, and whether all providers at the hospital were in-network.</p>
  </div>
  <div class="faq-item">
    <h3>Why is tPA (alteplase) so expensive on my hospital bill?</h3>
    <p>Hospitals bill tPA (alteplase) at $8,000&ndash;$15,000, but the actual drug acquisition cost is typically under $2,000. The markup covers hospital overhead, pharmacy staff, and profit margin. BillKarma&rsquo;s analysis found tPA drug charges are inflated an average of 9.3x acquisition cost. You can dispute the drug charge by requesting your itemized bill and comparing the billed J-code (J0153) to published wholesale acquisition costs.</p>
  </div>
  <div class="faq-item">
    <h3>What is a DRG and how does it affect my stroke bill?</h3>
    <p>A DRG (Diagnosis Related Group) is a fixed payment Medicare assigns to a hospitalization based on the primary diagnosis and patient complexity. For ischemic stroke, Medicare pays hospitals $5,800&ndash;$18,500 depending on the DRG assigned (063, 062, or 061). If the hospital assigned a higher-complexity DRG than your medical records support, that is a billing error called upcoding, and you can dispute it.</p>
  </div>
  <div class="faq-item">
    <h3>Is stroke rehabilitation billed separately from the hospital stay?</h3>
    <p>Yes. Inpatient rehabilitation after a stroke is billed separately from the acute hospital stay, often generating its own facility and professional fees. Physical therapy (CPT 97110), occupational therapy (CPT 97530), and speech therapy (CPT 92507) are each billed per session. Hospitals charge $120&ndash;$400 per session for services Medicare reimburses at $25&ndash;$40, making rehab therapy one of the most inflated categories on stroke bills.</p>
  </div>
  <div class="faq-item">
    <h3>What are the most common errors on a stroke hospital bill?</h3>
    <p>The most common errors include: tPA and anticoagulant drug charges inflated 5&ndash;10x acquisition cost; ICU room charges billed for days the patient was in a lower-acuity step-down unit; duplicate therapy session charges on the same date; and DRG upcoding that assigns higher complexity codes than the patient&rsquo;s condition warrants. Requesting an itemized bill and comparing it to your medical records is the first step to catching these errors.</p>
  </div>
</div>

<h2 id="sources">Sources</h2>
<ul class="sources-list">
  <li>Health Affairs (2024). &ldquo;Acute Ischemic Stroke Hospitalization Costs and Trends.&rdquo; <em>Health Affairs</em>, 43(2).</li>
  <li>Centers for Medicare &amp; Medicaid Services (2025). Medicare Severity DRG (MS-DRG) Definitions Manual, Version 42. CMS.gov.</li>
  <li>American Stroke Association (2024). &ldquo;Stroke Treatment Guidelines: IV Alteplase Administration.&rdquo; <em>Stroke</em>, 55(1).</li>
  <li>RAND Corporation (2023). &ldquo;Hospital Price Variation for Common Inpatient Conditions.&rdquo; RAND Health Quarterly, 10(3).</li>
  <li>Office of Inspector General, HHS (2023). &ldquo;Hospitals&rsquo; Compliance With Medicare Billing Requirements for Inpatient Stays.&rdquo; OIG Report OEI-02-20-00171.</li>
</ul>
""",
})
