"""Guide: Understanding Your Explanation of Benefits (EOB)."""

from guides import register, _embed

register("understanding-explanation-of-benefits", {
    "title": "Understanding Your Explanation of Benefits (EOB): What Every Line Means",
    "meta_description": "Your Explanation of Benefits is the key to catching billing errors. Learn how to read every section of an EOB, spot discrepancies, and save money on medical bills.",
    "published": "2026-02-18",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What is an Explanation of Benefits (EOB)?",
            "a": "An Explanation of Benefits is a statement from your health insurance company that shows how a medical claim was processed. It is NOT a bill. It shows what the provider charged, what your insurance allowed, what insurance paid, and what you may owe. You receive an EOB after every medical service that is submitted to your insurance.",
        },
        {
            "q": "Is an EOB the same as a medical bill?",
            "a": "No. An EOB is from your insurance company and explains how they processed a claim. A medical bill is from the provider (hospital, doctor, lab) and requests payment. Always compare the two - the 'patient responsibility' on your EOB should match the amount on your bill. If the bill is higher than the EOB says you owe, contact the provider.",
        },
        {
            "q": "What does 'allowed amount' mean on an EOB?",
            "a": "The allowed amount (also called 'eligible amount' or 'negotiated rate') is the maximum amount your insurance plan has agreed to pay for a specific service. It is almost always less than the provider's billed charge. In-network providers have agreed to accept the allowed amount as full payment. The difference between the billed amount and the allowed amount is the 'contractual adjustment' that in-network providers write off.",
        },
        {
            "q": "Why does my EOB say 'not covered' for a service?",
            "a": "Common reasons: the service requires prior authorization that was not obtained, the service is considered not medically necessary by your plan, the service is excluded from your plan benefits, or the claim was submitted with incorrect coding. If you believe the service should be covered, you can appeal the decision with your insurance company.",
        },
        {
            "q": "What should I do if my bill is different from my EOB?",
            "a": "If your medical bill shows a higher patient responsibility than your EOB, contact the provider's billing department and ask them to recheck against the EOB. Common causes: the provider hasn't applied the insurance payment yet, the provider is balance billing for the contractual adjustment (not allowed for in-network providers), or the bill was sent before insurance processed the claim.",
        },
    ],
    "body": f"""
<p class="lead">Your Explanation of Benefits (EOB) is the single most important document for catching billing errors&mdash;yet most people throw it away without reading it. The EOB shows exactly what your insurance approved, what they paid, and what you actually owe. When the number on your bill doesn&rsquo;t match the number on your EOB, someone made a mistake. Here&rsquo;s how to read every line and spot the discrepancies.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-eob">What is an EOB (and what it is NOT)</a></li>
        <li><a href="#anatomy">Anatomy of an EOB</a></li>
        <li><a href="#real-eob">A real EOB, annotated</a></li>
        <li><a href="#key-numbers">The 5 key numbers on every EOB</a></li>
        <li><a href="#eob-vs-bill">EOB vs. medical bill: how to compare them</a></li>
        <li><a href="#common-errors">Common EOB errors and what to do</a></li>
        <li><a href="#denied-claims">What to do when a claim is denied</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-eob">1. What is an EOB (and what it is NOT)</h2>

<p>An Explanation of Benefits is a statement your health insurance company sends you after a medical claim is processed. It explains:</p>

<ul>
    <li>What medical services were submitted to insurance</li>
    <li>What the provider charged</li>
    <li>What your insurance plan allows for those services (the &ldquo;allowed amount&rdquo;)</li>
    <li>What your insurance paid</li>
    <li>What you may owe (deductible, copay, coinsurance)</li>
</ul>

<div class="key-takeaway">
    <strong>An EOB is NOT a bill.</strong> It says &ldquo;This is not a bill&rdquo; right on it. Your actual bill comes from the provider (hospital, doctor, lab). But the EOB tells you what you <em>should</em> owe&mdash;so if the bill says something different, someone made a mistake.
</div>

<h2 id="anatomy">2. Anatomy of an EOB</h2>

<p>A standard EOB has these sections:</p>

<table>
    <thead>
        <tr><th>Section</th><th>What It Shows</th><th>Why It Matters</th></tr>
    </thead>
    <tbody>
        <tr><td>Patient &amp; plan info</td><td>Your name, ID number, group number, claim number</td><td>Verify this is the correct patient and plan. Errors here cause claim denials.</td></tr>
        <tr><td>Provider info</td><td>Doctor or facility name, network status (in/out)</td><td>Network status determines your cost-sharing rate. In-network = lower cost.</td></tr>
        <tr><td>Date of service</td><td>When the service was performed</td><td>Match this against your records. Wrong dates can indicate billing errors.</td></tr>
        <tr><td>Service description &amp; CPT code</td><td>What was done, identified by CPT code</td><td>Verify these match the services you actually received.</td></tr>
        <tr><td>Billed amount</td><td>What the provider charged</td><td>This is the full chargemaster price&mdash;almost always higher than what insurance pays.</td></tr>
        <tr><td>Allowed amount</td><td>The negotiated rate your insurance accepts</td><td>This is the real price. In-network providers write off the difference.</td></tr>
        <tr><td>Insurance paid</td><td>What your insurer sent to the provider</td><td>The allowed amount minus your cost-sharing.</td></tr>
        <tr><td>Your responsibility</td><td>Deductible, copay, and/or coinsurance</td><td>This is what you should actually owe. Compare against your bill.</td></tr>
        <tr><td>Remarks/codes</td><td>Explanation codes for adjustments or denials</td><td>Tells you WHY something was adjusted or denied. Key for appeals.</td></tr>
    </tbody>
</table>

<h2 id="real-eob">3. A real EOB, annotated</h2>

<p>Here&rsquo;s what an actual EOB looks like for an ER visit. We&rsquo;ve highlighted the key numbers and where errors commonly appear:</p>

<div class="bill-example">
    <div class="bill-header">Explanation of Benefits &mdash; BlueCross BlueShield &mdash; Claim #2026-0122-4891</div>
    <div class="line-item">
        <span><strong>Provider:</strong> Regional Medical Center (In-Network)</span>
        <span><strong>Date:</strong> 01/22/2026</span>
    </div>
    <div class="line-item" style="border-bottom: 2px solid #D1D5DB; margin-top: 8px; padding-bottom: 8px;">
        <span><strong>Service</strong></span>
        <span><strong>Billed &rarr; Allowed &rarr; Ins. Paid &rarr; You Owe</strong></span>
    </div>
    <div class="line-item">
        <span>99284 &mdash; ER Visit Level 4</span>
        <span>$2,890 &rarr; $742 &rarr; $593 &rarr; $149</span>
    </div>
    <div class="line-item">
        <span>71046 &mdash; Chest X-ray, 2 views</span>
        <span>$940 &rarr; $127 &rarr; $102 &rarr; $25</span>
    </div>
    <div class="line-item">
        <span>80053 &mdash; Comprehensive Metabolic Panel</span>
        <span>$487 &rarr; $14 &rarr; $11 &rarr; $3</span>
    </div>
    <div class="line-item flagged">
        <span>85025 &mdash; CBC (appears twice) &nbsp; &#9888; <em>Duplicate on bill but insurance only paid once</em></span>
        <span>$182 &rarr; $10 &rarr; $8 &rarr; $2</span>
    </div>
    <div class="line-item">
        <span>96374 &mdash; IV Push</span>
        <span>$348 &rarr; $86 &rarr; $69 &rarr; $17</span>
    </div>
    <div class="line-total">
        <span>TOTALS</span>
        <span>$4,847 &rarr; $979 &rarr; $783 &rarr; $196</span>
    </div>
</div>

<p>Look at the difference between the &ldquo;Billed&rdquo; column ($4,847) and the &ldquo;Allowed&rdquo; column ($979). That&rsquo;s <strong>$3,868</strong> in charges that the insurance company negotiated down to zero. The provider accepted $979 as full payment because they&rsquo;re in-network.</p>

<p><strong>What the patient actually owes: $196</strong> (the coinsurance on the allowed amount).</p>

<div class="key-takeaway">
    <strong>The catch:</strong> If the hospital sends a bill for $4,847 (the billed amount) instead of $196 (what the EOB says you owe), you need to call billing immediately. This happens more often than you&rsquo;d think&mdash;especially if insurance payment hasn&rsquo;t been applied yet.
</div>

<h2 id="key-numbers">4. The 5 key numbers on every EOB</h2>

<h3>a) Billed amount (provider&rsquo;s charge)</h3>

<p>What the provider submitted to insurance. This is the chargemaster price&mdash;the inflated sticker price. For in-network providers, this number is meaningless because they&rsquo;ve agreed to accept less.</p>

<h3>b) Allowed amount (negotiated rate)</h3>

<p>The maximum amount your insurance plan will recognize for a service. This is the real price. The difference between the billed amount and the allowed amount is the &ldquo;contractual adjustment&rdquo; that in-network providers write off.</p>

<p>For the ER visit above: the hospital billed $2,890 for the Level 4 visit, but the allowed amount is $742. The hospital writes off the $2,148 difference. You can look up what Medicare pays for the same services to see how your plan&rsquo;s allowed amounts compare:</p>

{_embed(mode="cost", title="Compare your EOB to Medicare rates", subtitle="Enter a CPT code from your EOB to see the Medicare rate.")}

<h3>c) Insurance paid</h3>

<p>The amount your insurer sent directly to the provider. This is the allowed amount minus your cost-sharing (deductible, copay, coinsurance).</p>

<h3>d) Patient responsibility</h3>

<p>What you owe. This includes your deductible (if not met), copay, and coinsurance. <strong>This number should match your medical bill.</strong> If the bill is higher, contact the provider.</p>

<h3>e) Deductible applied</h3>

<p>How much of the allowed amount was applied to your annual deductible. If your deductible is $1,500 and you haven&rsquo;t used any of it yet, the first $1,500 of allowed charges will come out of your pocket before insurance starts paying their share.</p>

<h2 id="eob-vs-bill">5. EOB vs. medical bill: how to compare them</h2>

<p>This is where you catch errors. Line up your EOB and your medical bill side by side and check these three things:</p>

<table>
    <thead>
        <tr><th>Check</th><th>EOB Says</th><th>Bill Says</th><th>If Different</th></tr>
    </thead>
    <tbody>
        <tr><td>Patient responsibility total</td><td>$196</td><td>Should be $196</td><td>If the bill is higher, the provider may not have applied insurance payment or is balance billing.</td></tr>
        <tr><td>Services listed</td><td>5 line items</td><td>Should match</td><td>If the bill has services not on the EOB, those charges were either denied or never submitted to insurance.</td></tr>
        <tr><td>CPT codes</td><td>99284, 71046, 80053, 85025, 96374</td><td>Should match</td><td>Different codes on the bill vs. EOB suggest a billing or coding error.</td></tr>
    </tbody>
</table>

<div class="case-study">
    <h3>Common scenario: bill doesn&rsquo;t match EOB</h3>
    <p>A patient&rsquo;s EOB shows patient responsibility of <strong>$196</strong>. The hospital sends a bill for <strong>$1,847</strong>. What happened? The hospital applied the insurance payment ($783) to the billed amount ($4,847) instead of the allowed amount ($979). Result: the patient is being asked to pay $1,847 more than they owe.</p>
    <p><strong>Fix:</strong> Call billing with your EOB in hand. Say: &ldquo;My EOB shows patient responsibility of $196 for this claim. Your bill shows $1,847. Can you recheck the insurance payment application on this account?&rdquo;</p>
</div>

<h2 id="common-errors">6. Common EOB errors and what to do</h2>

<h3>a) Claim processed as out-of-network when provider is in-network</h3>

<p><strong>Impact:</strong> Your cost-sharing is calculated at the much higher out-of-network rate. Instead of a $40 copay, you might owe $800+ in coinsurance.</p>
<p><strong>Fix:</strong> Call your insurance company. Provide the provider&rsquo;s NPI (National Provider Identifier) and ask them to verify network status and reprocess the claim.</p>

<h3>b) Service denied as &ldquo;not medically necessary&rdquo;</h3>

<p><strong>Impact:</strong> Insurance pays $0. You&rsquo;re responsible for the full billed amount.</p>
<p><strong>Fix:</strong> Ask your doctor&rsquo;s office to submit clinical notes supporting the medical necessity. Then file an appeal with your insurance company. First-level appeals succeed about 40&ndash;50% of the time.</p>

<h3>c) Duplicate claim denial</h3>

<p><strong>Impact:</strong> Insurance thinks a claim was already submitted and denies the second one. If the provider then bills you for the denied amount, you could be overpaying.</p>
<p><strong>Fix:</strong> Check whether the service was truly performed once or twice. If once, the duplicate denial is correct and you should ensure the provider doesn&rsquo;t bill you for the denied claim.</p>

<h3>d) Wrong patient or policy information</h3>

<p><strong>Impact:</strong> Claim denied entirely. Common after marriage, job change, or when a dependent turns 26.</p>
<p><strong>Fix:</strong> Verify your insurance information with the provider and ask them to resubmit with corrected details.</p>

<h2 id="denied-claims">7. What to do when a claim is denied</h2>

<ol>
    <li><strong>Read the denial reason code on the EOB.</strong> Every denial includes a reason code and description. Understanding why it was denied tells you how to appeal.</li>
    <li><strong>Call your insurance company.</strong> Ask them to explain the denial in plain language. Ask specifically what documentation would be needed to overturn it.</li>
    <li><strong>Gather supporting documentation.</strong> Clinical notes from your doctor, prior authorization records, or proof of medical necessity.</li>
    <li><strong>File a first-level appeal.</strong> Most plans allow you to appeal within 180 days. Send a letter with your claim number, the reason you believe the denial is wrong, and supporting documentation.</li>
    <li><strong>Request an external review if the internal appeal fails.</strong> Under the ACA, you have the right to an independent external review for most denials. The external reviewer&rsquo;s decision is binding on the insurance company.</li>
</ol>

<div class="key-takeaway">
    <strong>Don&rsquo;t accept the first &ldquo;no.&rdquo;</strong> Studies show that 40&ndash;50% of first-level insurance appeals are successful, and external reviews overturn denials about 40% of the time. Many patients never appeal&mdash;insurance companies count on this.
</div>

<p>If your EOB shows a denied claim or unexpected charges, <a href="/scan">upload your bill to BillKarma</a> to identify errors automatically and get help with the dispute process.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is an Explanation of Benefits (EOB)?</h3>
        <p>An EOB is a statement from your health insurance company showing how a medical claim was processed. It shows what the provider charged, what your insurance allowed, what insurance paid, and what you may owe. It is not a bill&mdash;your bill comes from the provider.</p>
    </div>

    <div class="faq-item">
        <h3>Is an EOB the same as a medical bill?</h3>
        <p>No. An EOB is from your insurance company; a bill is from the provider. Always compare them. The &ldquo;patient responsibility&rdquo; on your EOB should match your bill. If the bill is higher, contact the provider&rsquo;s billing department with your EOB. <a href="/guides/how-to-read-your-medical-bill">Learn how to read your medical bill here.</a></p>
    </div>

    <div class="faq-item">
        <h3>What does &ldquo;allowed amount&rdquo; mean on an EOB?</h3>
        <p>The allowed amount is the maximum your insurance plan will recognize for a service. In-network providers accept this as full payment and write off the difference between their charge and the allowed amount. This is the real price&mdash;not the billed amount. Use our <a href="/calculator">calculator</a> to compare allowed amounts to Medicare rates.</p>
    </div>

    <div class="faq-item">
        <h3>Why does my EOB say &ldquo;not covered&rdquo; for a service?</h3>
        <p>Common reasons: the service requires prior authorization that wasn&rsquo;t obtained, the service is excluded from your plan, or the claim was submitted with incorrect coding. You have the right to appeal&mdash;40&ndash;50% of first-level appeals succeed.</p>
    </div>

    <div class="faq-item">
        <h3>What should I do if my bill is different from my EOB?</h3>
        <p>Contact the provider&rsquo;s billing department with your EOB. Common causes: the provider hasn&rsquo;t applied the insurance payment, is balance billing (not allowed for in-network providers), or sent the bill before insurance processed the claim.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.healthcare.gov/health-care-law-protections/appeals/" target="_blank" rel="noopener">HealthCare.gov: How to Appeal a Health Insurance Decision</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">No Surprises Act &mdash; CMS</a></li>
    <li><a href="https://www.kff.org/private-insurance/issue-brief/claims-denials-and-appeals-in-aca-marketplace-plans/" target="_blank" rel="noopener">KFF: Claims Denials and Appeals Data</a></li>
    <li><a href="https://www.naic.org/state_web_map.htm" target="_blank" rel="noopener">NAIC: State Insurance Commissioner Directory</a></li>
</ul>
""",
})
