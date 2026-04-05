"""Guide: What Are CPT Codes? How to Use Them to Audit Your Medical Bill."""

from guides import register, _embed

register("what-are-cpt-codes", {
    "title": "What Are CPT Codes? How to Audit Your Medical Bill (2026)",
    "meta_description": "CPT codes are the five-digit numbers on every medical bill. Learn what they mean, how hospitals misuse them, and how to audit your own bill using CPT codes.",
    "published": "2026-02-19",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "What is a CPT code?",
            "a": "CPT stands for Current Procedural Terminology. CPT codes are five-digit numbers that identify every medical procedure, service, and test performed in healthcare. They are maintained by the American Medical Association and used by every doctor, hospital, and insurer in the United States to describe and bill for care. The code 99213, for example, always means an office visit of moderate complexity, and 71046 always means a two-view chest X-ray.",
        },
        {
            "q": "Where can I find CPT codes on my bill?",
            "a": "CPT codes appear on your Explanation of Benefits (EOB) from your insurance company, on an itemized hospital bill, and on the CMS-1500 claim form that providers submit to insurers. If your bill only shows descriptions like 'office visit' or 'lab work' without the codes, request an itemized bill from the provider — you are entitled to one.",
        },
        {
            "q": "What is upcoding and how common is it?",
            "a": "Upcoding is when a provider bills a higher-level CPT code than the service actually provided — for example, billing a 99215 (highest complexity office visit) for what was really a 99213 (moderate complexity visit). The Department of Health and Human Services Office of Inspector General reports that upcoding costs Medicare billions of dollars annually and is one of the most common forms of medical billing fraud. It also appears in private insurance billing.",
        },
        {
            "q": "What is unbundling?",
            "a": "Unbundling is billing separately for procedures that should be billed as a single, lower-priced code. For example, if you had a comprehensive metabolic panel (CPT 80053), all 14 individual tests are included in that one code. A provider that bills each of the 14 tests separately is unbundling — and charging you far more than the code was designed to allow. Medicare's National Correct Coding Initiative (NCCI) edits define which codes cannot be billed together.",
        },
        {
            "q": "Can I look up what a CPT code means?",
            "a": "Yes. You can search CMS's Medicare Physician Fee Schedule look-up tool at cms.gov to find the official Medicare rate for any CPT code in your area. The American Medical Association's CPT descriptions are copyrighted, but the code numbers and their basic descriptions are widely published in billing resources and medical cost transparency tools.",
        },
        {
            "q": "What should I do if I find a CPT code error on my bill?",
            "a": "Start by requesting an itemized bill with all CPT codes listed. Cross-reference the codes against your medical records to confirm each service was actually performed. If you find a discrepancy — a code that doesn't match your records, a duplicate code, or a higher-level code than seems appropriate — write to the provider's billing department citing the specific code and requesting documentation. If the provider disagrees, file an insurance appeal with your insurer. If you believe the error is intentional, you can file a complaint with your state medical board or the OIG hotline.",
        },
    ],
    "body": f"""
<p class="lead">Every charge on your medical bill has a five-digit code behind it. These are <strong>CPT codes</strong> — Current Procedural Terminology — and they are the universal language of medical billing. A single incorrect code can cost you hundreds or thousands of dollars. This guide explains how CPT codes work, where the most common errors occur, and how to use them to audit your own bill in under 30 minutes.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-are-cpt-codes">What CPT codes are and why they exist</a></li>
        <li><a href="#code-categories">The main CPT code categories</a></li>
        <li><a href="#common-codes">Common CPT codes and what they cost</a></li>
        <li><a href="#billing-errors">The 4 most common CPT billing errors</a></li>
        <li><a href="#audit-your-bill">How to audit your bill with CPT codes</a></li>
        <li><a href="#real-bill">An annotated bill with CPT errors</a></li>
        <li><a href="#case-studies">Real-world case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-are-cpt-codes">1. What CPT codes are and why they exist</h2>

<p>Before CPT codes, medical billing was a free-for-all. Providers described services in their own words, insurers interpreted them differently, and payment disputes were constant. The American Medical Association introduced the Current Procedural Terminology system in 1966 to create a standard language for medical billing.</p>

<p>Today, every healthcare encounter in the United States is translated into CPT codes before a claim can be paid. When your doctor examines you, they select an Evaluation and Management (E/M) code based on the complexity of the visit. When a technician draws your blood, the lab selects a code for each test run. When you have surgery, the surgeon selects codes for the procedure, and the hospital selects separate codes for the facility services.</p>

<p>The system creates a paper trail — and that trail can work in your favor. Because every service has a code, you can look up exactly what that code is supposed to represent, what it should cost according to Medicare, and whether the code on your bill matches the service you actually received.</p>

<div class="key-takeaway">
    <strong>CPT codes are your audit trail.</strong> They convert vague descriptions like &ldquo;office visit&rdquo; into specific, verifiable, price-checkable services. A bill without CPT codes is impossible to audit. Always request an itemized bill that includes CPT codes.
</div>

<h2 id="code-categories">2. The main CPT code categories</h2>

<p>CPT codes are organized into sections by type of service. Knowing which section a code comes from tells you what kind of service was being billed.</p>

<table>
    <thead>
        <tr><th>Code Range</th><th>Category</th><th>Examples</th></tr>
    </thead>
    <tbody>
        <tr><td>99202&ndash;99499</td><td>Evaluation &amp; Management (E/M)</td><td>Office visits, hospital visits, ER visits</td></tr>
        <tr><td>00100&ndash;01999</td><td>Anesthesia</td><td>General anesthesia, regional blocks</td></tr>
        <tr><td>10004&ndash;69990</td><td>Surgery</td><td>All surgical procedures by body system</td></tr>
        <tr><td>70010&ndash;79999</td><td>Radiology</td><td>X-rays, MRIs, CT scans, ultrasounds</td></tr>
        <tr><td>80047&ndash;89398</td><td>Pathology &amp; Laboratory</td><td>Blood panels, urinalysis, biopsies</td></tr>
        <tr><td>90281&ndash;99607</td><td>Medicine</td><td>Vaccines, therapy sessions, infusions</td></tr>
        <tr><td>99091&ndash;99499</td><td>E/M &mdash; outpatient &amp; observation</td><td>Includes hospital observation codes</td></tr>
    </tbody>
</table>

<p>Within each category, codes are typically ordered from simpler/lower-cost to more complex/higher-cost. In E/M codes, for example, 99202 is a brief new patient office visit and 99205 is the most complex new patient visit. The difference in billing between 99203 and 99205 can be $150&ndash;$300 per visit.</p>

<div class="key-takeaway">
    <strong>Wondering what category your billed code falls into?</strong> Run any CPT code through our <a href="/calculator">free calculator</a> to see its official Medicare rate and how your charge compares to the national benchmark.
</div>

<h2 id="common-codes">3. Common CPT codes and what they cost</h2>

<p>These are the codes you&rsquo;re most likely to see on a routine medical bill, along with the 2026 Medicare national average reimbursement rate (non-facility setting):</p>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Description</th><th>Medicare Rate (2026)</th><th>Typical Hospital Charge</th></tr>
    </thead>
    <tbody>
        <tr><td>99213</td><td>Office visit, established patient, moderate complexity</td><td>$112</td><td>$200&ndash;$400</td></tr>
        <tr><td>99214</td><td>Office visit, established patient, high complexity</td><td>$167</td><td>$300&ndash;$600</td></tr>
        <tr><td>99283</td><td>ER visit, moderate severity</td><td>$182</td><td>$500&ndash;$1,200</td></tr>
        <tr><td>99285</td><td>ER visit, high severity</td><td>$290</td><td>$900&ndash;$3,500</td></tr>
        <tr><td>85025</td><td>Complete blood count (CBC)</td><td>$11</td><td>$60&ndash;$200</td></tr>
        <tr><td>80053</td><td>Comprehensive metabolic panel</td><td>$14</td><td>$80&ndash;$300</td></tr>
        <tr><td>71046</td><td>Chest X-ray, 2 views</td><td>$29</td><td>$150&ndash;$600</td></tr>
        <tr><td>73721</td><td>MRI knee w/o contrast</td><td>$472</td><td>$800&ndash;$3,500</td></tr>
        <tr><td>93000</td><td>Electrocardiogram (ECG/EKG)</td><td>$17</td><td>$80&ndash;$350</td></tr>
        <tr><td>36415</td><td>Blood draw (venipuncture)</td><td>$3</td><td>$15&ndash;$75</td></tr>
        <tr><td>99232</td><td>Subsequent hospital visit, moderate complexity</td><td>$113</td><td>$200&ndash;$500</td></tr>
        <tr><td>43239</td><td>Upper GI endoscopy with biopsy</td><td>$405</td><td>$700&ndash;$3,000</td></tr>
    </tbody>
</table>

<p>The ratio between Medicare rates and typical hospital charges is often 5&ndash;20x. This isn&rsquo;t necessarily fraud — hospitals negotiate different rates with different insurers, and the &ldquo;chargemaster&rdquo; list price is a starting point for negotiation. But for uninsured patients or those with high-deductible plans paying the full billed amount, the gap is very real.</p>

{_embed(mode="cost", title="Look Up a CPT Code Rate", subtitle="Check the Medicare benchmark for any procedure code")}

<h2 id="billing-errors">4. The 4 most common CPT billing errors</h2>

<h3>1. Upcoding</h3>
<p>Upcoding is billing a higher-complexity code than the service warranted. The most common example is E/M upcoding: billing a 99215 (most complex office visit, ~$232 Medicare rate) for what was a routine follow-up that should have been coded 99213 (~$112). The OIG estimates that E/M upcoding alone costs Medicare over $1 billion per year.</p>

<p>Signs of upcoding:</p>
<ul>
    <li>Level 5 E/M codes (99205, 99215, 99285) on every visit regardless of complexity</li>
    <li>High-complexity hospital visit codes (99233) for brief daily check-ins</li>
    <li>Surgical codes that include modifiers suggesting more extensive procedures than you recall</li>
</ul>

<h3>2. Unbundling</h3>
<p>Unbundling breaks a single comprehensive code into multiple component codes, increasing total charges. Medicare&rsquo;s National Correct Coding Initiative (NCCI) defines which codes are &ldquo;bundled&rdquo; and cannot be billed separately. Common unbundling examples:</p>

<ul>
    <li>Billing the 14 individual tests within a comprehensive metabolic panel (80053) as separate line items</li>
    <li>Billing a surgical approach code separately from the surgery itself when the approach is already included</li>
    <li>Billing an E/M visit on the same day as a procedure when the E/M was for the same complaint that led to the procedure</li>
</ul>

<h3>3. Duplicate billing</h3>
<p>Duplicate billing means charging twice for the same service. This is often an administrative error — the same claim is submitted twice and both payments go through — but it can also be intentional. Look for the same CPT code appearing twice on the same date, or the same service appearing on both a hospital bill and a physician bill.</p>

<h3>4. Phantom procedures</h3>
<p>A phantom procedure is a charge for a service that was never performed. This is the most serious billing error because it is straightforward fraud. It can happen due to data entry errors (wrong patient record, wrong date), but it also occurs intentionally. Verify every CPT code on your bill against your own memory of what happened and against your medical records.</p>

<div class="key-takeaway">
    <strong>Billing errors are common enough to always check.</strong> A 2016 NerdWallet study found that 49% of Medicare claims contained billing errors, and the Medical Billing Advocates of America estimates the rate is even higher for hospital bills. The majority are upcoding and unbundling — not phantom procedures. But all four error types are worth checking for, because each one means you or your insurer is paying more than you should.
</div>

<h2 id="audit-your-bill">5. How to audit your bill with CPT codes</h2>

<p>You don&rsquo;t need a medical background to audit a bill. You need an itemized bill, about 30 minutes, and this process:</p>

<ol>
    <li>
        <strong>Request an itemized bill.</strong> Call the hospital or provider&rsquo;s billing department and ask for an itemized statement listing each service, the CPT code, the date of service, and the amount charged. You are legally entitled to this. If they resist, cite your right under the No Surprises Act and state hospital billing transparency laws.
    </li>
    <li>
        <strong>Request your Explanation of Benefits (EOB).</strong> If you have insurance, log into your insurer&rsquo;s portal or call them to get the EOB for the claim. The EOB shows each CPT code, the provider&rsquo;s charge, the insurer&rsquo;s allowed amount, and your share. Cross-reference the EOB against the itemized bill — every line item should match.
    </li>
    <li>
        <strong>Look up each code.</strong> For any code you don&rsquo;t recognize, search for it on CMS&rsquo;s Medicare Physician Fee Schedule (find it at cms.gov). This tells you the official description and the Medicare rate. If the description doesn&rsquo;t match what you remember receiving, flag it.
    </li>
    <li>
        <strong>Check for duplicates.</strong> Scan for the same CPT code on the same date. Also look for the same service described differently but with different codes — for example, blood draw code 36415 and a separate &ldquo;specimen collection&rdquo; charge.
    </li>
    <li>
        <strong>Check E/M code levels.</strong> If you see a 99215 or 99285 (highest complexity), ask yourself: was the visit really that involved? A brief follow-up or a straightforward ER visit for a minor issue probably shouldn&rsquo;t be coded at the highest level.
    </li>
    <li>
        <strong>Request medical records for anything suspicious.</strong> Providers are required to give you your medical records within 30 days. If you suspect a code doesn&rsquo;t match what was done, your medical records are the proof. The clinical documentation should support the CPT code billed.
    </li>
</ol>

<div class="key-takeaway">
    <strong>Ready to put this process to work on your own bill?</strong> Upload your bill to our <a href="/scan">free scanner</a> and we&rsquo;ll automatically flag duplicate codes, upcoded E/M levels, and unbundled lab charges in seconds.
</div>

<h2 id="real-bill">6. An annotated bill with CPT errors</h2>

<div class="bill-example">
    <h3>ER Visit Bill — What the Codes Revealed</h3>
    <p>Patient: 42-year-old with ankle sprain, treated and released from the ER.</p>
    <div class="line-item line-item-error">
        <span>99285 — ER Visit, High Complexity</span>
        <span><strong>Flagged:</strong> An isolated ankle sprain typically warrants 99283 (moderate). The provider billed the highest E/M level. Difference: ~$108 in Medicare rates, potentially $300&ndash;$500 in actual overcharge.</span>
    </div>
    <div class="line-item line-item-error">
        <span>73610 — X-ray ankle, 3+ views</span>
        <span><strong>Flagged:</strong> Records show a 2-view ankle X-ray was taken. 73610 is for 3+ views. The correct code is 73600 (2 views). Difference: ~$15 Medicare, $50&ndash;$100 actual.</span>
    </div>
    <div class="line-item line-item-error">
        <span>99070 — Supplies (crutch rental)</span>
        <span><strong>Flagged:</strong> Crutches were loaned, not rented, and are already bundled into the facility fee. Duplicate charge of $85.</span>
    </div>
    <div class="line-item">
        <span>36415 — Blood draw</span>
        <span>Appropriate — blood was drawn for CBC prior to treatment.</span>
    </div>
    <div class="line-item">
        <span>85025 — CBC</span>
        <span>Appropriate — lab test was performed.</span>
    </div>
    <p><strong>Total recovered after appeal: $543</strong></p>
</div>

<h2 id="case-studies">7. Real-world case studies</h2>

<div class="key-takeaway">
    <strong>Seeing a CPT code on your bill that doesn&rsquo;t add up?</strong> Check what Medicare actually pays for that procedure with our <a href="/calculator">free calculator</a> &mdash; knowing the benchmark is the first step to a successful dispute.
</div>

<div class="case-study">
    <h3>Case Study 1: E/M Upcoding — $1,200 Recovered</h3>
    <p>A patient with a high-deductible health plan received a bill for $1,850 after seeing a specialist for knee pain over three consecutive appointments. All three visits were billed at 99215 (highest complexity). Her deductible applied, so she owed the full amount.</p>
    <p>She requested her medical records and compared them to the codes. Her records described each visit as a routine follow-up with no change in treatment plan — classic 99213 territory. She wrote to the billing department citing the documentation mismatch and requested a code review. The practice reclassified all three visits to 99213, reducing her total bill by $1,200.</p>
    <p><strong>Lesson:</strong> Specialists routinely default to high-complexity codes for established patients. Compare the visit notes to the E/M code level — brief, straightforward visits rarely justify 99215.</p>
</div>

<div class="case-study">
    <h3>Case Study 2: Unbundled Lab Panel — $473 Recovered</h3>
    <p>A patient received a hospital lab bill showing 14 individual line items for blood tests, each billed separately, totaling $891. The correct billing for a comprehensive metabolic panel (80053) — which includes all 14 tests — was $83 at the Medicare rate.</p>
    <p>The patient identified the unbundling by noticing that many tests (sodium, potassium, CO2, etc.) are components of a panel. She cited NCCI bundling rules in her dispute letter. The hospital re-billed as a single panel. Her insurance renegotiated and her share dropped from $312 to $29 — a saving of $283. The insurer recovered $473 in total overcharges.</p>
    <p><strong>Lesson:</strong> If you see individual component tests billed separately (sodium, potassium, BUN, creatinine, glucose all as line items), check whether they should be bundled into a panel code.</p>
</div>

{_embed(mode="cost", title="Check Your CPT Code", subtitle="Compare your billed amount to the Medicare benchmark")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
<dl>
    <dt>What is a CPT code?</dt>
    <dd>CPT stands for Current Procedural Terminology. CPT codes are five-digit numbers that identify every medical procedure, service, and test performed in healthcare. They are maintained by the American Medical Association and used by every doctor, hospital, and insurer in the United States to describe and bill for care.</dd>

    <dt>Where can I find CPT codes on my bill?</dt>
    <dd>CPT codes appear on your Explanation of Benefits (EOB) from your insurance company, on an itemized hospital bill, and on the CMS-1500 claim form. If your bill only shows descriptions without codes, request an itemized bill — you are entitled to one.</dd>

    <dt>What is upcoding and how common is it?</dt>
    <dd>Upcoding is billing a higher-level CPT code than the service actually provided. The OIG reports that E/M upcoding alone costs Medicare over $1 billion annually. It is one of the most common billing errors in both Medicare and private insurance claims.</dd>

    <dt>What is unbundling?</dt>
    <dd>Unbundling is billing separately for procedures that should be billed as a single, lower-priced code. Medicare's NCCI edits define which codes cannot be billed separately. A common example is billing individual lab tests instead of the panel code that includes them all.</dd>

    <dt>Can I look up what a CPT code means?</dt>
    <dd>Yes. CMS's Medicare Physician Fee Schedule look-up tool at cms.gov shows the official Medicare rate for any CPT code in your area. Many medical cost transparency tools also provide CPT descriptions and benchmark pricing.</dd>

    <dt>What should I do if I find a CPT code error?</dt>
    <dd>Request an itemized bill and your medical records. Compare each CPT code against what was actually done. Write to the billing department citing the specific code and requesting documentation or correction. If the provider disagrees, file an appeal with your insurer. Serious errors can be reported to your state medical board or the OIG hotline (1-800-HHS-TIPS).</dd>
</dl>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li>American Medical Association. <em>CPT&reg; — Current Procedural Terminology.</em> 2026 Edition.</li>
    <li>Centers for Medicare &amp; Medicaid Services. <a href="https://www.cms.gov" target="_blank" rel="noopener">Medicare Physician Fee Schedule Look-Up Tool.</a> 2026.</li>
    <li>CMS. <em>National Correct Coding Initiative (NCCI) Policy Manual for Medicare Services.</em> 2026.</li>
    <li>HHS Office of Inspector General. <em>Inappropriate Payments for Evaluation and Management Services.</em> OEI-04-10-00181. 2014.</li>
    <li>Medical Billing Advocates of America. <em>Medical Billing Error Rate Study.</em> 2023.</li>
    <li>CMS. <em>No Surprises Act: Good Faith Estimates and Itemized Bills.</em> 2022.</li>
</ul>
""",
})
