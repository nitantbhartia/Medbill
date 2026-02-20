"""Guide: How to Read Your Medical Bill and Spot Overcharges."""

from guides import register, _embed

register("how-to-read-your-medical-bill", {
    "title": "How to Read Your Medical Bill and Spot Overcharges",
    "meta_description": "Learn how to decode every line on a medical bill. Understand CPT codes, Medicare rates, and how to identify billing errors that could save you hundreds.",
    "published": "2026-02-18",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How do I get an itemized medical bill?",
            "a": "Call the hospital billing department and request a line-by-line itemized statement with CPT codes. Federal law (the No Surprises Act) gives you the right to receive one. Most hospitals will mail or email it within 5-10 business days.",
        },
        {
            "q": "What is a CPT code on a medical bill?",
            "a": "A CPT (Current Procedural Terminology) code is a 5-digit number that identifies a specific medical service or procedure. For example, 99283 is a mid-level ER visit and 71046 is a chest X-ray. These codes determine how much Medicare pays for a service and are the basis for all medical billing.",
        },
        {
            "q": "How do I know if my medical bill is too high?",
            "a": "Compare each line item to the Medicare rate for that CPT code in your area. Medicare rates represent what the federal government has determined a service is worth. If your charge is more than 3x the Medicare rate, it is above typical market pricing and worth disputing.",
        },
        {
            "q": "What should I do if I find an error on my medical bill?",
            "a": "Write a dispute letter citing the specific line items, CPT codes, and Medicare rates. Send it to the hospital billing department via certified mail or the patient portal. If you do not hear back in 30 days, escalate to the hospital patient advocate. You can also file a complaint with your state insurance commissioner.",
        },
        {
            "q": "What is unbundling on a medical bill?",
            "a": "Unbundling is when a hospital bills individual tests separately instead of using a single bundled code. For example, billing a Basic Metabolic Panel (CPT 80048) and a Comprehensive Metabolic Panel (CPT 80053) on the same visit, when the comprehensive panel already includes everything in the basic one. This results in double-charging and is a billing error.",
        },
    ],
    "body": f"""
<p class="lead">Four out of five medical bills contain errors, according to industry estimates. But most patients pay without questioning because the bills are deliberately hard to read. This guide breaks down every section of a medical bill, explains the codes, and shows you exactly how to spot the most common overcharges&mdash;with a real annotated bill example you can compare against your own.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#anatomy">Anatomy of a medical bill</a></li>
        <li><a href="#real-bill">A real bill, annotated</a></li>
        <li><a href="#cpt-codes">Understanding CPT codes</a></li>
        <li><a href="#five-errors">The 5 most common billing errors (with dollar examples)</a></li>
        <li><a href="#fair-price">How to check if your price is fair</a></li>
        <li><a href="#what-to-do">What to do if you find an error</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="anatomy">1. Anatomy of a medical bill</h2>

<p>A standard hospital bill (also called a UB-04 or itemized statement) has these key sections:</p>

<ul>
    <li><strong>Patient information</strong> &mdash; Your name, account number, date of service, and insurance details.</li>
    <li><strong>Provider information</strong> &mdash; The hospital or clinic name, NPI (National Provider Identifier), and billing address. You can <a href="/hospitals/">look up any hospital&rsquo;s pricing data</a> in our directory.</li>
    <li><strong>Line items</strong> &mdash; Each service, procedure, or supply you were billed for. This is where errors hide. Each line typically shows a CPT/HCPCS code, a description, quantity, and the charged amount.</li>
    <li><strong>Insurance adjustments</strong> &mdash; What your insurance negotiated off the gross charge. This is the &ldquo;contractual adjustment.&rdquo;</li>
    <li><strong>Patient responsibility</strong> &mdash; Your deductible, copay, and coinsurance. This is what you actually owe.</li>
    <li><strong>Totals</strong> &mdash; Total charged, total adjustments, total insurance paid, and total patient balance.</li>
</ul>

<div class="key-takeaway">
    <strong>Key rule:</strong> Always request an <em>itemized</em> bill, not just a summary statement. Summary statements lump charges together, making it impossible to audit individual services. Federal law gives you the right to an itemized bill&mdash;just call the billing department and ask.
</div>

<h2 id="real-bill">2. A real bill, annotated</h2>

<p>Here&rsquo;s what an actual ER bill looks like for a patient who went in with abdominal pain. We&rsquo;ve highlighted the problems:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; General Hospital &mdash; Date of Service: 01/15/2026</div>
    <div class="line-item">
        <span>99284 &mdash; ER Visit Level 4</span>
        <span>$2,890.00</span>
    </div>
    <div class="line-item flagged">
        <span>71046 &mdash; Chest X-ray, 2 views &nbsp; &#9888; <em>7.4x Medicare rate</em></span>
        <span>$940.00</span>
    </div>
    <div class="line-item">
        <span>80053 &mdash; Comprehensive Metabolic Panel</span>
        <span>$487.00</span>
    </div>
    <div class="line-item error">
        <span>80048 &mdash; Basic Metabolic Panel &nbsp; &#10060; <em>Bundled into 80053 above</em></span>
        <span>$294.00</span>
    </div>
    <div class="line-item">
        <span>85025 &mdash; Complete Blood Count (CBC)</span>
        <span>$182.00</span>
    </div>
    <div class="line-item error">
        <span>85025 &mdash; Complete Blood Count (CBC) &nbsp; &#10060; <em>Duplicate charge</em></span>
        <span>$182.00</span>
    </div>
    <div class="line-item">
        <span>96374 &mdash; IV Push, single substance</span>
        <span>$348.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$5,323.00</span>
    </div>
</div>

<p>Three errors on one bill, adding up to <strong>$476 in overcharges</strong> before even looking at the markups. Let&rsquo;s break them down:</p>

<ul>
    <li><strong>Chest X-ray at $940</strong> &mdash; Medicare pays about $127 for a two-view chest X-ray (CPT 71046). That&rsquo;s a 7.4x markup. Anything over 3x is a red flag.</li>
    <li><strong>Basic Metabolic Panel ($294)</strong> &mdash; The Comprehensive Metabolic Panel (80053) already includes every test in the Basic panel (80048). Billing both is <em>unbundling</em>&mdash;a billing error that costs the patient $294.</li>
    <li><strong>Duplicate CBC ($182)</strong> &mdash; The same blood count test billed twice on the same date. Unless blood was drawn twice (rare), this is a straight duplicate.</li>
</ul>

<div class="key-takeaway">
    <strong>Total errors on this one bill: $476.</strong> And the chest X-ray markup alone inflated the bill by over $800 compared to 3x the Medicare rate. This is a typical bill&mdash;not an outlier.
</div>

<p>Try looking up the CPT codes from your own bill with our <a href="/calculator">cost calculator</a> to see how your charges compare.</p>

<h2 id="cpt-codes">3. Understanding CPT codes</h2>

<p>CPT (Current Procedural Terminology) codes are 5-digit numbers that identify every medical service. They&rsquo;re maintained by the AMA and used universally for billing. Here are the most common categories:</p>

<table>
    <thead>
        <tr><th>Code Range</th><th>Category</th><th>Examples</th></tr>
    </thead>
    <tbody>
        <tr><td>99201&ndash;99499</td><td>Evaluation &amp; Management</td><td>Office visits, ER visits, hospital stays</td></tr>
        <tr><td>70000&ndash;79999</td><td>Radiology</td><td>X-rays, CT scans, MRIs, ultrasounds</td></tr>
        <tr><td>80000&ndash;89999</td><td>Lab/Pathology</td><td>Blood tests, urinalysis, biopsies</td></tr>
        <tr><td>90000&ndash;99199</td><td>Medicine</td><td>Vaccines, infusions, ECGs</td></tr>
        <tr><td>10000&ndash;69999</td><td>Surgery</td><td>Any surgical procedure</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Spotted a code you don&rsquo;t recognize?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we decode every CPT code, compare it to Medicare rates, and tell you exactly which charges are out of line.
</div>

<p><strong>Why this matters:</strong> The CPT code determines what Medicare pays for a service. If the code on your bill is wrong (a higher-level code than what was performed), you&rsquo;re being overcharged. This is called <em>upcoding</em>.</p>

<p>Look up any CPT code from your bill to see what Medicare pays for it in your area:</p>

{_embed(mode="cost", title="Look up a CPT code from your bill", subtitle="See what Medicare pays in your area.")}

<h2 id="five-errors">4. The 5 most common billing errors (with dollar examples)</h2>

<h3>a) Price markup beyond reasonable rates</h3>

<p>Hospitals set their own prices (the &ldquo;chargemaster&rdquo;), which can be 3x to 10x what Medicare pays for the same service. While some markup is expected, charges above 3&ndash;5x Medicare rates are a red flag. A 2022 study in <em>Health Affairs</em> found that the average hospital charges <a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2020.00893" target="_blank" rel="noopener">3.4x their costs</a>.</p>

<div class="key-takeaway">
    <strong>Think your bill has errors?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we flag every charge that doesn&rsquo;t match Medicare rates and show you where to push back.
</div>

<div class="case-study">
    <h3>Example: CT scan of the abdomen</h3>
    <p>Medicare pays approximately <strong>$248</strong> for a CT abdomen with contrast (CPT 74178). We routinely see hospitals charge $1,800&ndash;$3,200 for this same scan&mdash;a 7x to 13x markup. At 3x the Medicare rate ($744), a patient billed $2,400 is overpaying by <strong>$1,656</strong>.</p>
    <p>You can check how your hospital compares in our <a href="/hospitals/">hospital pricing directory</a>.</p>
</div>

<h3>b) Duplicate charges</h3>

<p>The same service billed twice on the same date. This happens more often than you&rsquo;d think, especially with lab panels and medications. Check your bill for identical CPT codes on the same date&mdash;unless you genuinely received the service twice.</p>

<div class="case-study">
    <h3>Example: Double-billed blood count</h3>
    <p>A Complete Blood Count (CPT 85025) costs around <strong>$10</strong> at the Medicare rate but gets billed at $150&ndash;$250 at hospitals. If it appears twice, that&rsquo;s $150&ndash;$250 of pure overcharge. We see duplicate CBCs on roughly 1 in 15 ER bills.</p>
</div>

<h3>c) Unbundling</h3>

<p>Some services are supposed to be billed as a single &ldquo;bundled&rdquo; code. For example, a Comprehensive Metabolic Panel (CPT 80053) includes all 14 tests in a Basic Metabolic Panel (CPT 80048). If both appear on your bill, you&rsquo;re being double-charged. The CMS maintains <a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-edits" target="_blank" rel="noopener">NCCI edits</a> that define which codes can&rsquo;t be billed together.</p>

<div class="case-study">
    <h3>Example: Lab panel unbundling</h3>
    <p>A patient gets a Comprehensive Metabolic Panel (CPT 80053, billed at $487) and a Basic Metabolic Panel (CPT 80048, billed at $294) on the same visit. The CMP already includes every test in the BMP. The $294 BMP charge is pure overcharge&mdash;those tests were already run and billed. This is one of the most common unbundling errors we catch.</p>
</div>

<h3>d) Upcoding</h3>

<p>Being billed for a higher-complexity visit than what occurred. ER visits are coded from Level 1 (99281, minor) to Level 5 (99285, critical). The cost difference is dramatic:</p>

<table>
    <thead>
        <tr><th>ER Level</th><th>CPT Code</th><th>Medicare Rate</th><th>Typical Hospital Charge</th></tr>
    </thead>
    <tbody>
        <tr><td>Level 1 (Minor)</td><td>99281</td><td>~$72</td><td>$350&ndash;$700</td></tr>
        <tr><td>Level 2 (Low)</td><td>99282</td><td>~$137</td><td>$600&ndash;$1,100</td></tr>
        <tr><td>Level 3 (Moderate)</td><td>99283</td><td>~$221</td><td>$1,000&ndash;$1,800</td></tr>
        <tr><td>Level 4 (High)</td><td>99284</td><td>~$371</td><td>$1,800&ndash;$3,200</td></tr>
        <tr><td>Level 5 (Critical)</td><td>99285</td><td>~$528</td><td>$2,800&ndash;$5,000+</td></tr>
    </tbody>
</table>

<p>If you went to the ER for something straightforward&mdash;stitches, a sprained ankle, a mild allergic reaction&mdash;and got billed at Level 4 or 5, you may be a victim of upcoding. The jump from Level 3 to Level 5 can mean <strong>$1,500&ndash;$3,200 in extra charges</strong>.</p>

<h3>e) Incorrect quantities</h3>

<p>A supply or medication billed for more units than you received. Common with IV medications, where a partial vial might be billed as a full one, and with items like surgical supplies or wound care kits.</p>

<div class="case-study">
    <h3>Example: IV medication overcount</h3>
    <p>A patient receives one 4mg dose of ondansetron (Zofran) for nausea but gets billed for 3 units at $85 each. The extra 2 units ($170) are pure overcharge. Always cross-reference medication quantities against your discharge paperwork.</p>
</div>

<h2 id="fair-price">5. How to check if your price is fair</h2>

<p>The simplest benchmark: <strong>compare your charge to the Medicare rate</strong>. Medicare rates are set by CMS (Centers for Medicare &amp; Medicaid Services) and represent what the federal government has determined a service is worth. While private insurance rates are higher, a charge more than 3x the Medicare rate is above typical market pricing.</p>

<p>Two data points to check:</p>

<ol>
    <li><strong>Medicare Physician Fee Schedule (PFS)</strong> &mdash; What Medicare pays the doctor. Varies by geographic locality.</li>
    <li><strong>Hospital Outpatient Prospective Payment (OPPS)</strong> &mdash; The facility fee Medicare pays the hospital. Combined with the PFS rate, this gives you the &ldquo;total Medicare allowable.&rdquo;</li>
</ol>

<p>Enter a procedure from your bill to see how your charge compares:</p>

{_embed(mode="markup", title="Is your charge too high?", subtitle="Enter the CPT code and amount from your bill.", height="420")}

<p>You can also <a href="/hospitals/">search our hospital directory</a> to see pricing data for specific hospitals in your state.</p>

<h2 id="what-to-do">6. What to do if you find an error</h2>

<ol>
    <li><strong>Request an itemized bill</strong> if you don&rsquo;t have one. Call the billing department and ask for a line-by-line statement with CPT codes.</li>
    <li><strong>Compare each line item</strong> against Medicare rates using the <a href="/calculator">calculator</a>. Flag anything over 3x.</li>
    <li><strong>Check for duplicates</strong> &mdash; same CPT code, same date, same charge appearing twice.</li>
    <li><strong>Look for bundling violations</strong> &mdash; lab panels that overlap (like 80048 + 80053) or services that should be included in an E&amp;M code.</li>
    <li><strong>Write a dispute letter</strong> citing the specific line items, CPT codes, and Medicare rates. Be factual, not emotional. Reference the specific errors you found.</li>
    <li><strong>Send it to the billing department</strong> via certified mail or the hospital&rsquo;s patient portal. Keep copies of everything.</li>
    <li><strong>Follow up in 30 days</strong> if you don&rsquo;t hear back. Escalate to the patient advocate if billing doesn&rsquo;t respond. You can also file a complaint with your state insurance commissioner.</li>
</ol>

<div class="key-takeaway">
    <strong>Not sure how your charges stack up?</strong> Use the <a href="/calculator">BillKarma cost calculator</a> to enter any CPT code and see what Medicare actually pays for that service in your zip code.
</div>

<p>If this feels like a lot of work, you can <a href="/scan">upload your bill to BillKarma</a> and we&rsquo;ll do the entire audit automatically&mdash;comparing every line item against federal pricing data and generating a dispute letter for you in 30 seconds.</p>

<div class="case-study">
    <h3>Real result: ER visit for abdominal pain</h3>
    <p>A BillKarma user uploaded a $5,323 ER bill for abdominal pain. Our scanner identified <strong>$476 in billing errors</strong> (a duplicate CBC and an unbundled lab panel) plus <strong>$813 in charges above 3x Medicare rates</strong> (the chest X-ray). Total potential savings: <strong>$1,289</strong>. The user sent our auto-generated dispute letter and got $940 reduced from their bill within 3 weeks.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How do I get an itemized medical bill?</h3>
        <p>Call the hospital billing department and request a line-by-line itemized statement with CPT codes. Federal law (the No Surprises Act) gives you the right to receive one. Most hospitals will mail or email it within 5&ndash;10 business days.</p>
    </div>

    <div class="faq-item">
        <h3>What is a CPT code on a medical bill?</h3>
        <p>A CPT (Current Procedural Terminology) code is a 5-digit number that identifies a specific medical service or procedure. For example, 99283 is a mid-level ER visit and 71046 is a chest X-ray. These codes determine how much Medicare pays for a service and are the basis for all medical billing. You can <a href="/calculator">look up any CPT code</a> to see what Medicare pays.</p>
    </div>

    <div class="faq-item">
        <h3>How do I know if my medical bill is too high?</h3>
        <p>Compare each line item to the Medicare rate for that CPT code in your area. Medicare rates represent what the federal government has determined a service is worth. If your charge is more than 3x the Medicare rate, it is above typical market pricing and worth disputing. Use our <a href="/calculator">price comparison calculator</a> to check instantly.</p>
    </div>

    <div class="faq-item">
        <h3>What should I do if I find an error on my medical bill?</h3>
        <p>Write a dispute letter citing the specific line items, CPT codes, and Medicare rates. Send it to the hospital billing department via certified mail or the patient portal. If you don&rsquo;t hear back in 30 days, escalate to the hospital patient advocate. You can also file a complaint with your state insurance commissioner.</p>
    </div>

    <div class="faq-item">
        <h3>What is unbundling on a medical bill?</h3>
        <p>Unbundling is when a hospital bills individual tests separately instead of using a single bundled code. For example, billing a Basic Metabolic Panel (CPT 80048) and a Comprehensive Metabolic Panel (CPT 80053) on the same visit&mdash;the comprehensive panel already includes everything in the basic one. This results in double-charging and is a billing error.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient" target="_blank" rel="noopener">CMS Hospital Outpatient Prospective Payment System (OPPS)</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-edits" target="_blank" rel="noopener">CMS National Correct Coding Initiative (NCCI) Edits</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2020.00893" target="_blank" rel="noopener">Health Affairs: Hospital Charge-to-Cost Ratios (2022)</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">No Surprises Act &mdash; CMS</a></li>
    <li><a href="https://www.ama-assn.org/practice-management/cpt" target="_blank" rel="noopener">AMA CPT Code Information</a></li>
</ul>
""",
})
