"""Guide: How to Dispute a Medical Bill."""

from guides import register, _embed

register("how-to-dispute-a-medical-bill", {
    "title": "How to Dispute a Medical Bill: A Step-by-Step Guide With Templates",
    "meta_description": "Learn exactly how to dispute a medical bill with sample letters, phone scripts, and step-by-step instructions. Know your rights and save hundreds.",
    "published": "2026-02-18",
    "author": "BillKarma Team",
    "category": "Taking Action",
    "faqs": [
        {
            "q": "How long do I have to dispute a medical bill?",
            "a": "Most hospitals allow disputes within 120-180 days of the billing date. However, you should act quickly. Once a bill goes to collections (typically after 90-120 days of non-payment), it becomes harder to dispute. Contact billing within 30 days of receiving the bill for best results.",
        },
        {
            "q": "Can I dispute a medical bill that has already gone to collections?",
            "a": "Yes. Under the Fair Debt Collection Practices Act (FDCPA), you have 30 days from the first collection notice to request debt validation. The collector must provide proof that the debt is accurate and that they have the right to collect it. If the bill contains errors, the original hospital billing department can still correct them.",
        },
        {
            "q": "Will disputing a medical bill hurt my credit score?",
            "a": "No. Disputing a bill does not affect your credit score. As of 2023, the three major credit bureaus (Experian, TransUnion, Equifax) no longer include medical debt under $500 on credit reports. Paid medical collections are also removed. Unpaid medical debt over $500 can only appear after 12 months, giving you time to resolve disputes.",
        },
        {
            "q": "What if the hospital refuses to adjust my bill?",
            "a": "Escalate in this order: (1) Ask for a supervisor in the billing department, (2) Contact the hospital patient advocate, (3) File a complaint with your state insurance commissioner, (4) If you have insurance, ask your insurer to review the charges, (5) Consult a medical billing advocate for complex cases.",
        },
        {
            "q": "Do I need a lawyer to dispute a medical bill?",
            "a": "In most cases, no. The majority of billing errors can be resolved by contacting the hospital billing department directly with documentation of the error. A lawyer is only necessary if the dispute involves potential legal issues like balance billing violations under the No Surprises Act or if the bill has gone to collections and you are being sued.",
        },
        {
            "q": "Should I pay my medical bill while I dispute it?",
            "a": "You should pay the portion you do not dispute to show good faith. For the disputed amount, send a written dispute letter explaining that you are contesting specific charges. Request that the hospital not send the disputed portion to collections while the dispute is active. Many hospitals will place a hold on the disputed amount.",
        },
    ],
    "body": f"""
<p class="lead">You found an error on your medical bill. Now what? Most patients never dispute because they don&rsquo;t know where to start. This guide walks you through the entire process&mdash;from writing your first dispute letter to escalating if the hospital won&rsquo;t budge&mdash;with real templates you can copy and send today.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#before-you-dispute">Before you dispute: gather your evidence</a></li>
        <li><a href="#dispute-letter">How to write a dispute letter (with template)</a></li>
        <li><a href="#phone-script">Phone script for calling billing</a></li>
        <li><a href="#what-to-dispute">What&rsquo;s worth disputing (and what isn&rsquo;t)</a></li>
        <li><a href="#escalation">How to escalate when billing says no</a></li>
        <li><a href="#timeline">Dispute timeline: what to expect</a></li>
        <li><a href="#real-examples">Real dispute results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="before-you-dispute">1. Before you dispute: gather your evidence</h2>

<p>A dispute without evidence is just a complaint. Before you contact the hospital, collect these four things:</p>

<ol>
    <li><strong>Your itemized bill</strong> &mdash; Not the summary statement. You need a line-by-line breakdown showing CPT codes, descriptions, quantities, and charges. Call billing and request one if you don&rsquo;t have it. <a href="/guides/how-to-read-your-medical-bill">Here&rsquo;s how to read each line.</a></li>
    <li><strong>Medicare rates for each CPT code</strong> &mdash; These are your pricing benchmark. Use our <a href="/calculator">cost calculator</a> to look up the Medicare allowable rate for each service in your area.</li>
    <li><strong>Your Explanation of Benefits (EOB)</strong> &mdash; If you have insurance, your EOB shows what your insurer approved, what they paid, and what they think you owe. Compare this against the hospital&rsquo;s bill&mdash;discrepancies are common.</li>
    <li><strong>Discharge paperwork</strong> &mdash; Your discharge summary lists what services you actually received. This is your proof if the bill includes services you didn&rsquo;t get or quantities that don&rsquo;t match.</li>
</ol>

<p>Look up each CPT code from your bill to build your evidence:</p>

{_embed(mode="markup", title="Build your dispute evidence", subtitle="Enter a CPT code and amount from your bill to see the Medicare rate.", height="420")}

<div class="key-takeaway">
    <strong>Key rule:</strong> Never call billing to dispute without your evidence ready. You want specific numbers, not vague complaints. &ldquo;My bill seems too high&rdquo; gets nowhere. &ldquo;CPT 71046 is billed at $940 but Medicare pays $127&mdash;that&rsquo;s a 7.4x markup&rdquo; gets results.
</div>

<h2 id="dispute-letter">2. How to write a dispute letter (with template)</h2>

<p>A written dispute creates a paper trail. Always send a letter&mdash;even if you also call. Here&rsquo;s what to include:</p>

<ul>
    <li>Your name, account number, and date of service</li>
    <li>The specific line items you&rsquo;re disputing (CPT code, description, charged amount)</li>
    <li>The reason each charge is wrong (duplicate, unbundled, above Medicare benchmark, etc.)</li>
    <li>The Medicare rate for each disputed service</li>
    <li>What you&rsquo;re requesting (removal, reduction to a specific amount, or review)</li>
</ul>

<div class="case-study">
    <h3>Sample dispute letter</h3>
    <p><em>[Your Name]<br>[Your Address]<br>[Date]</em></p>
    <p><em>RE: Account #[ACCOUNT NUMBER], Date of Service [DATE]</em></p>
    <p>Dear Billing Department,</p>
    <p>I am writing to dispute the following charges on my itemized statement:</p>
    <p><strong>1. CPT 85025 &mdash; Complete Blood Count &mdash; $182.00</strong><br>This test appears twice on my bill for the same date of service. I received one CBC, not two. I am requesting removal of the duplicate charge ($182.00).</p>
    <p><strong>2. CPT 80048 &mdash; Basic Metabolic Panel &mdash; $294.00</strong><br>My bill also includes CPT 80053 (Comprehensive Metabolic Panel) on the same date. Per CMS NCCI edits, CPT 80048 is bundled into 80053 and should not be billed separately. I am requesting removal of this charge ($294.00).</p>
    <p><strong>3. CPT 71046 &mdash; Chest X-ray, 2 views &mdash; $940.00</strong><br>The Medicare allowable rate for this service in my area is approximately $127. The charged amount is 7.4x the Medicare rate. I am requesting a reduction to a reasonable rate.</p>
    <p>Total disputed amount: <strong>$1,416.00</strong></p>
    <p>Please review these charges and provide a corrected statement within 30 days. I am happy to pay the undisputed portion of my bill promptly.</p>
    <p><em>Sincerely,<br>[Your Name]</em></p>
</div>

<p><strong>How to send it:</strong> Use the hospital&rsquo;s patient portal if available (it creates a timestamped record). Otherwise, send via certified mail with return receipt. Keep a copy of everything.</p>

<h2 id="phone-script">3. Phone script for calling billing</h2>

<p>Sometimes a phone call resolves things faster than a letter. Here&rsquo;s a script you can read from:</p>

<div class="case-study">
    <h3>Phone script</h3>
    <p>&ldquo;Hi, I&rsquo;m calling about account number [NUMBER], date of service [DATE]. I&rsquo;ve reviewed my itemized bill and found some charges I&rsquo;d like to discuss.</p>
    <p>First, CPT 85025 appears twice on my statement. I only received one blood draw. Can you confirm whether this is a duplicate?</p>
    <p>Second, I see both CPT 80048 and 80053 billed on the same date. The comprehensive panel includes all tests in the basic panel, so these shouldn&rsquo;t be billed separately under NCCI rules.</p>
    <p>Third, CPT 71046 is billed at $940. The Medicare rate for a two-view chest X-ray is about $127. I&rsquo;d like to discuss a more reasonable rate.</p>
    <p>I&rsquo;ve also sent a written dispute to your department. Can you tell me what the next steps are for reviewing these charges?&rdquo;</p>
</div>

<div class="key-takeaway">
    <strong>Pro tip:</strong> Write down the name of every person you speak with, the date and time of the call, and any reference or case numbers. If you need to escalate later, this documentation is essential.
</div>

<p>Want a custom dispute script generated from your specific bill? <a href="/scan">Upload your bill to BillKarma</a> and we&rsquo;ll create a personalized phone script and dispute letter automatically.</p>

<h2 id="what-to-dispute">4. What&rsquo;s worth disputing (and what isn&rsquo;t)</h2>

<p>Not every charge is worth fighting over. Focus your energy on the high-impact items:</p>

<table>
    <thead>
        <tr><th>Worth Disputing</th><th>Typical Savings</th><th>Difficulty</th></tr>
    </thead>
    <tbody>
        <tr><td>Duplicate charges</td><td>$100&ndash;$500 per duplicate</td><td>Easy &mdash; clear-cut error</td></tr>
        <tr><td>Unbundling errors</td><td>$200&ndash;$800 per violation</td><td>Easy &mdash; cite NCCI edits</td></tr>
        <tr><td>Upcoded ER visit</td><td>$500&ndash;$3,000</td><td>Moderate &mdash; may need clinical notes</td></tr>
        <tr><td>Charges over 5x Medicare</td><td>$300&ndash;$5,000+</td><td>Moderate &mdash; negotiation required</td></tr>
        <tr><td>Services not received</td><td>Varies</td><td>Easy &mdash; compare to discharge summary</td></tr>
    </tbody>
</table>

<table>
    <thead>
        <tr><th>Usually Not Worth Disputing</th><th>Why</th></tr>
    </thead>
    <tbody>
        <tr><td>Charges under $50</td><td>Time investment exceeds potential savings</td></tr>
        <tr><td>Charges at 1&ndash;2x Medicare</td><td>Within normal commercial pricing range</td></tr>
        <tr><td>Facility fees you agreed to</td><td>Signed consent typically covers these</td></tr>
    </tbody>
</table>

<h2 id="escalation">5. How to escalate when billing says no</h2>

<p>If the billing department denies your dispute or stops responding, here&rsquo;s the escalation ladder:</p>

<ol>
    <li><strong>Billing supervisor</strong> &mdash; Ask for a supervisor or manager in the billing department. Front-line staff often can&rsquo;t approve adjustments above a certain threshold.</li>
    <li><strong>Patient advocate</strong> &mdash; Most hospitals have a patient advocate or ombudsman. Their job is to resolve patient complaints. Ask the hospital operator to transfer you.</li>
    <li><strong>Your insurance company</strong> &mdash; If you&rsquo;re insured, call your insurer&rsquo;s member services number and ask them to review the charges. Insurers have leverage that individual patients don&rsquo;t.</li>
    <li><strong>State insurance commissioner</strong> &mdash; Every state has a Department of Insurance that accepts complaints about medical billing. Filing a complaint often gets a response from the hospital within weeks.</li>
    <li><strong>State attorney general</strong> &mdash; For patterns of overcharging, your state AG&rsquo;s consumer protection division may investigate.</li>
    <li><strong>Medical billing advocate</strong> &mdash; For complex disputes (over $5,000 in potential savings), a professional billing advocate charges 25&ndash;35% of savings but knows exactly how to work the system.</li>
</ol>

<div class="key-takeaway">
    <strong>Important:</strong> At each step, reference your previous communications. &ldquo;I sent a dispute letter on [date] and spoke with [name] on [date]. Here are the case numbers.&rdquo; Documentation turns a complaint into a credible dispute.
</div>

<h2 id="timeline">6. Dispute timeline: what to expect</h2>

<table>
    <thead>
        <tr><th>Stage</th><th>Timeframe</th><th>What Happens</th></tr>
    </thead>
    <tbody>
        <tr><td>Send dispute letter</td><td>Day 1</td><td>Clock starts. Hospital should acknowledge within 5&ndash;7 business days.</td></tr>
        <tr><td>Hospital review</td><td>Days 7&ndash;30</td><td>Billing department investigates. May ask for additional info.</td></tr>
        <tr><td>Initial response</td><td>Days 14&ndash;45</td><td>Hospital sends adjusted bill or denial with explanation.</td></tr>
        <tr><td>Escalation (if needed)</td><td>Days 30&ndash;60</td><td>Contact patient advocate or file state complaint.</td></tr>
        <tr><td>Resolution</td><td>Days 30&ndash;90</td><td>Most disputes resolve within 90 days. Complex cases may take longer.</td></tr>
    </tbody>
</table>

<p><strong>During the dispute:</strong> Pay the undisputed portion of your bill on time. Request in writing that the disputed amount not be sent to collections while the review is active. Most hospitals will agree to this.</p>

<h2 id="real-examples">7. Real dispute results</h2>

<div class="case-study">
    <h3>Example 1: ER visit &mdash; $1,289 in errors found, $940 reduced</h3>
    <p>A patient received a $5,323 ER bill for abdominal pain. <a href="/scan">BillKarma&rsquo;s scanner</a> identified a duplicate CBC ($182), an unbundled lab panel ($294), and a chest X-ray billed at 7.4x Medicare rates ($813 above 3x benchmark). The patient sent a dispute letter citing all three findings. The hospital removed the duplicate and unbundled charge and reduced the X-ray to $450. <strong>Total reduction: $940.</strong></p>
</div>

<div class="case-study">
    <h3>Example 2: Outpatient surgery &mdash; upcoded anesthesia</h3>
    <p>A patient had a 45-minute outpatient knee arthroscopy but was billed for 90 minutes of anesthesia time (CPT 01382). At $150 per 15-minute unit, the extra 45 minutes added <strong>$450</strong> to the bill. After disputing with the surgical center and providing the actual procedure duration from the operative report, the anesthesia charge was corrected. <strong>Total reduction: $450.</strong></p>
</div>

<div class="case-study">
    <h3>Example 3: Lab work &mdash; balance billing after insurance</h3>
    <p>A patient&rsquo;s in-network lab billed $1,200 for a panel of tests. Insurance paid the contracted rate of $340, but the lab sent the patient a bill for the remaining $860. Under in-network agreements, the lab cannot balance bill the patient for the difference. The patient cited their EOB and the balance was written off. <strong>Total reduction: $860.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How long do I have to dispute a medical bill?</h3>
        <p>Most hospitals allow disputes within 120&ndash;180 days of the billing date. However, you should act quickly. Once a bill goes to collections (typically after 90&ndash;120 days of non-payment), it becomes harder to dispute. Contact billing within 30 days of receiving the bill for best results.</p>
    </div>

    <div class="faq-item">
        <h3>Can I dispute a medical bill that has already gone to collections?</h3>
        <p>Yes. Under the Fair Debt Collection Practices Act (FDCPA), you have 30 days from the first collection notice to request debt validation. The collector must provide proof that the debt is accurate and that they have the right to collect it. If the bill contains errors, the original hospital billing department can still correct them.</p>
    </div>

    <div class="faq-item">
        <h3>Will disputing a medical bill hurt my credit score?</h3>
        <p>No. Disputing a bill does not affect your credit score. As of 2023, the three major credit bureaus no longer include medical debt under $500 on credit reports. Paid medical collections are also removed. Unpaid medical debt over $500 can only appear after 12 months, giving you time to resolve disputes.</p>
    </div>

    <div class="faq-item">
        <h3>What if the hospital refuses to adjust my bill?</h3>
        <p>Escalate in this order: (1) Ask for a supervisor in the billing department, (2) Contact the hospital patient advocate, (3) File a complaint with your state insurance commissioner, (4) If you have insurance, ask your insurer to review the charges, (5) Consult a medical billing advocate for complex cases.</p>
    </div>

    <div class="faq-item">
        <h3>Do I need a lawyer to dispute a medical bill?</h3>
        <p>In most cases, no. The majority of billing errors can be resolved by contacting the hospital billing department directly with documentation of the error. A lawyer is only necessary if the dispute involves potential legal issues like balance billing violations under the <a href="/guides/no-surprises-act-explained">No Surprises Act</a> or if the bill has gone to collections and you are being sued.</p>
    </div>

    <div class="faq-item">
        <h3>Should I pay my medical bill while I dispute it?</h3>
        <p>You should pay the portion you do not dispute to show good faith. For the disputed amount, send a written dispute letter explaining that you are contesting specific charges. Request that the hospital not send the disputed portion to collections while the dispute is active.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-edits" target="_blank" rel="noopener">CMS National Correct Coding Initiative (NCCI) Edits</a></li>
    <li><a href="https://www.consumerfinance.gov/ask-cfpb/what-are-my-rights-when-dealing-with-debt-collectors-en-1403/" target="_blank" rel="noopener">CFPB: Your Rights When Dealing With Debt Collectors</a></li>
    <li><a href="https://www.consumerfinance.gov/about-us/newsroom/cfpb-publishes-report-on-medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt and Credit Reporting Changes</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">No Surprises Act &mdash; CMS</a></li>
    <li><a href="https://www.naic.org/state_web_map.htm" target="_blank" rel="noopener">NAIC: State Insurance Commissioner Directory</a></li>
</ul>
""",
})
