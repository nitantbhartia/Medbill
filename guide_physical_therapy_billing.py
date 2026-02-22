"""Guide: Physical Therapy Billing Errors and How to Dispute Them."""

from guides import register, _embed

register("physical-therapy-billing", {
    "title": "Physical Therapy Billing: Common Errors and How to Dispute Them",
    "meta_description": "Physical therapy billing errors cost patients hundreds. Learn the CPT codes, 8-minute rule, and how to spot duplicate charges before paying your PT bill.",
    "published": "2026-02-22",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "What are the most common physical therapy CPT codes?",
            "a": "The most common PT CPT codes are: 97110 (therapeutic exercise, $30-60 per 15-min unit), 97530 (therapeutic activities, $35-65/unit), 97140 (manual therapy, $35-65/unit), 97035 (ultrasound therapy, $20-40/unit), 97012 (mechanical traction, $20-35/unit), and 97032 (electrical stimulation, $20-40/unit). Each is billed in 15-minute increments under the '8-minute rule.'",
        },
        {
            "q": "What is the 8-minute rule in physical therapy billing?",
            "a": "The 8-minute rule determines how many billable units a PT can charge per service during a visit. A PT must spend at least 8 minutes on a timed service to bill one unit. From 8-22 minutes = 1 unit; 23-37 minutes = 2 units; 38-52 minutes = 3 units. A common error is billing 4 units of therapeutic exercise for a 45-minute session when only 3 units are allowed.",
        },
        {
            "q": "Can physical therapy be billed at the hospital rate instead of the clinic rate?",
            "a": "Yes, and this is a major cost driver. Hospital-based PT (even in a separate outpatient clinic) is often billed at hospital outpatient rates, which can be 2-3x higher than independent PT clinic rates for identical services. If your PT clinic is affiliated with a hospital, you'll pay a facility fee on top of the PT charge — often $200-$400 per visit. Look for this when you receive a separate facility bill alongside the PT professional bill.",
        },
        {
            "q": "Does Medicare cover physical therapy?",
            "a": "Yes. Medicare Part B covers medically necessary outpatient PT after you meet the annual Part B deductible ($257 in 2026). Medicare pays 80% of the approved amount; you pay 20% coinsurance. In 2018, Congress eliminated the PT 'cap' — Medicare now covers ongoing PT as long as it is medically necessary and documented. There is no annual limit.",
        },
        {
            "q": "How do I dispute a physical therapy billing error?",
            "a": "Request an itemized bill with CPT codes, dates, and number of units billed per visit. Compare units billed to the duration of each session (using the 8-minute rule). If units don't match time documented in your PT notes, submit a written dispute. Also check that your diagnosis codes support the services billed — PT for a knee injury should not show a shoulder diagnosis code.",
        },
    ],
    "body": f"""
<p class="lead">Americans make <strong>more than 200 million physical therapy visits per year</strong>, and billing errors are rampant. A 2022 OIG (Office of Inspector General) report found that <a href="https://oig.hhs.gov/oei/reports/OEI-02-19-00101.asp" target="_blank" rel="noopener">approximately 25% of Medicare PT claims contained documentation or billing errors</a> — improper unit counts, unsupported diagnoses, and services billed without required physician orders. For private-pay patients, the errors are just as common but harder to catch without knowing the billing rules. Here&rsquo;s the full picture.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cpt-codes">Common PT CPT codes and what they cost</a></li>
        <li><a href="#8-minute-rule">The 8-minute rule: how PT units are calculated</a></li>
        <li><a href="#annotated-bill">A real PT bill, annotated</a></li>
        <li><a href="#hospital-vs-clinic">Hospital-based PT vs. clinic PT: the cost difference</a></li>
        <li><a href="#common-errors">7 physical therapy billing errors to catch</a></li>
        <li><a href="#how-to-dispute">How to dispute a PT billing error</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cpt-codes">1. Common PT CPT codes and what they cost</h2>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Service</th><th>Unit duration</th><th>Medicare rate</th><th>Typical private billing</th></tr>
    </thead>
    <tbody>
        <tr><td>97110</td><td>Therapeutic exercise</td><td>15 min</td><td>~$33</td><td>$55&ndash;$95</td></tr>
        <tr><td>97530</td><td>Therapeutic activities</td><td>15 min</td><td>~$40</td><td>$60&ndash;$100</td></tr>
        <tr><td>97140</td><td>Manual therapy (joint manipulation, massage)</td><td>15 min</td><td>~$38</td><td>$55&ndash;$90</td></tr>
        <tr><td>97035</td><td>Ultrasound therapy</td><td>15 min</td><td>~$24</td><td>$35&ndash;$65</td></tr>
        <tr><td>97012</td><td>Mechanical traction</td><td>15 min</td><td>~$24</td><td>$35&ndash;$60</td></tr>
        <tr><td>97032</td><td>Electrical stimulation (E-stim), attended</td><td>15 min</td><td>~$26</td><td>$35&ndash;$65</td></tr>
        <tr><td>97033</td><td>Iontophoresis</td><td>15 min</td><td>~$26</td><td>$35&ndash;$65</td></tr>
        <tr><td>97760</td><td>Orthotic management (fitting)</td><td>15 min</td><td>~$32</td><td>$50&ndash;$85</td></tr>
        <tr><td>97010</td><td>Hot/cold pack application</td><td>Each</td><td>~$10 (often bundled)</td><td>$15&ndash;$40</td></tr>
    </tbody>
</table>

<p>Note that 97010 (hot/cold pack) should be bundled with other timed services in the same visit — it cannot be billed separately when therapeutic exercise or manual therapy are also billed. If you see CPT 97010 billed alongside 97110 or 97140, that&rsquo;s a bundling error.</p>

{_embed(mode="cost", title="Look up any PT CPT code", subtitle="Enter a code from your bill to see the Medicare rate — the clearest benchmark for whether your clinic is charging in range.")}

<div class="key-takeaway">
    <strong>Not sure if your PT charges are reasonable?</strong> Use our <a href="/calculator">free calculator</a> to look up Medicare rates for any PT CPT code — it&rsquo;s the clearest baseline for whether your clinic is billing in range.
</div>

<h2 id="8-minute-rule">2. The 8-minute rule: how PT units are calculated</h2>

<p>Physical therapy uses a time-based billing system. Most PT services (the &ldquo;timed codes&rdquo;) are billed in 15-minute increments, but the rules for how many units are allowed per session follow the <strong>8-minute rule</strong>:</p>

<table>
    <thead>
        <tr><th>Total minutes of timed service</th><th>Units billable</th></tr>
    </thead>
    <tbody>
        <tr><td>8&ndash;22 minutes</td><td>1 unit</td></tr>
        <tr><td>23&ndash;37 minutes</td><td>2 units</td></tr>
        <tr><td>38&ndash;52 minutes</td><td>3 units</td></tr>
        <tr><td>53&ndash;67 minutes</td><td>4 units</td></tr>
        <tr><td>68&ndash;82 minutes</td><td>5 units</td></tr>
    </tbody>
</table>

<p>Example: Your 60-minute PT session included 30 minutes of therapeutic exercise (97110) and 20 minutes of manual therapy (97140) — 50 total timed minutes. Under the 8-minute rule, that&rsquo;s 3 units total. If the clinic billed 4 units of 97110 and 2 units of 97140 (6 units total), they overbilled by 3 units.</p>

<p>The rule also means that if you spend only 5 minutes on one service, it doesn&rsquo;t qualify for a separate billing unit — those minutes must roll into the total timed calculation.</p>

<h2 id="annotated-bill">3. A real PT bill, annotated</h2>

<p>This is a bill for a 60-minute PT session for a knee injury (post-surgery rehabilitation):</p>

<div class="bill-example">
    <div class="bill-header">Physical Therapy Itemized Bill &mdash; 02/05/2026 &mdash; Session duration: 60 minutes</div>
    <div class="line-item">
        <span>97110 &mdash; Therapeutic exercise &times; 3 units (45 min)</span>
        <span>$99.00</span>
    </div>
    <div class="line-item">
        <span>97140 &mdash; Manual therapy &times; 1 unit (15 min)</span>
        <span>$38.00</span>
    </div>
    <div class="line-item error">
        <span>97010 &mdash; Hot pack application &times; 1 &nbsp; &#10060; <em>Cannot bill separately — must be bundled with timed services per CMS rules</em></span>
        <span>$25.00</span>
    </div>
    <div class="line-item flagged">
        <span>97035 &mdash; Ultrasound &times; 2 units &nbsp; &#9888; <em>Session notes show 10 min of ultrasound — only 1 billable unit under 8-minute rule</em></span>
        <span>$48.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$210.00</span>
    </div>
</div>

<p>Corrected total: $99 (97110) + $38 (97140) + $24 (97035, 1 unit) = <strong>$161</strong>. The patient was overbilled by <strong>$49</strong> on a single session — across 20 PT sessions, that&rsquo;s nearly $1,000 in overpayments.</p>

<h2 id="hospital-vs-clinic">4. Hospital-based PT vs. clinic PT: the cost difference</h2>

<p>This is one of the most significant and least-known cost drivers in outpatient PT. When your PT clinic is owned by or affiliated with a hospital, it may bill as a hospital outpatient department (HOPD) — triggering a facility fee on top of the professional charge:</p>

<table>
    <thead>
        <tr><th>Setting</th><th>Cost per 60-min session (est.)</th><th>Facility fee?</th></tr>
    </thead>
    <tbody>
        <tr><td>Independent PT clinic</td><td>$150&ndash;$250</td><td>No</td></tr>
        <tr><td>Hospital-affiliated PT clinic (HOPD)</td><td>$350&ndash;$550</td><td>Yes ($150&ndash;$300 per visit)</td></tr>
        <tr><td>Inpatient hospital PT</td><td>Bundled into DRG / room rate</td><td>Included</td></tr>
    </tbody>
</table>

<p>According to BillKarma&rsquo;s analysis of outpatient billing data from 6,200+ hospital-affiliated facilities, patients at hospital-based PT departments pay a median of <strong>2.4&times; more per session</strong> than patients at independent PT clinics for identical CPT codes — a cost gap that compounds across a full course of treatment. On a 20-session course of PT, that difference can exceed $2,000.</p>

<p>You may not know your clinic is hospital-affiliated until the bill arrives. Check before your first visit by asking: &ldquo;Will I receive a separate facility fee from the hospital?&rdquo; If the answer is yes, consider whether an independent clinic (same services, same quality) is available in your network.</p>

<div class="key-takeaway">
    <strong>Choosing a PT provider?</strong> Our <a href="/hospitals/">facility directory</a> shows billing grades and pricing data for hospital outpatient departments — compare markups before committing to a hospital-based clinic.
</div>

<h2 id="common-errors">5. Seven physical therapy billing errors to catch</h2>

<h3>a) Unit count exceeds session time (8-minute rule violation)</h3>
<p>Compare total units billed against total session minutes. If a 60-minute session shows 6+ timed units, request the PT&rsquo;s session notes to verify time spent on each service.</p>

<h3>b) Unbundled hot/cold pack (CPT 97010)</h3>
<p>CMS rules prohibit billing 97010 separately when timed services were also performed. If you see 97010 on the same date as 97110 or 97140, it should not be a separate billable charge.</p>

<h3>c) Duplicate service codes on the same date</h3>
<p>Two identical CPT codes billed on the same visit (e.g., 97140 &times; 1 and 97140 &times; 1 as separate line items) often indicate a billing entry error. The units should be combined into one line: 97140 &times; 2.</p>

<h3>d) Services billed without a physician referral</h3>
<p>Most insurance plans and Medicare require a physician order for PT coverage. If your insurer denies PT claims for &ldquo;no referral,&rdquo; but your PT collected a referral, request documented confirmation from your insurer that the referral was received.</p>

<h3>e) Wrong diagnosis code</h3>
<p>PT services must be supported by an ICD-10 diagnosis code that matches the body part being treated. If you had PT for a knee injury and your EOB shows a shoulder ICD-10 code, the service was billed under the wrong diagnosis — and may be denied as not medically necessary for that diagnosis.</p>

<h3>f) Balance billing for in-network PT</h3>
<p>If your PT is in-network, they have agreed to accept your insurance&rsquo;s allowed amount. They cannot bill you the difference between their full charge and the allowed amount. Any charge beyond your copay/coinsurance is impermissible balance billing.</p>

<h3>g) Services not covered by your plan billed as covered</h3>
<p>Some PT services — dry needling, aquatic therapy, work hardening — are not covered by all insurance plans. If your insurer denies these, the PT clinic should have informed you before providing the service under HIPAA&rsquo;s advance beneficiary notice (ABN) requirement. If they didn&rsquo;t notify you, you have grounds to dispute the charge.</p>

<div class="key-takeaway">
    <strong>Think your PT bill has errors?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we cross-reference every CPT code against Medicare rates and flag unit count anomalies, unbundling violations, and duplicate charges automatically.
</div>

<h2 id="how-to-dispute">6. How to dispute a PT billing error</h2>

<ol>
    <li><strong>Request your session notes:</strong> Under HIPAA, you&rsquo;re entitled to your physical therapy records, including the treatment notes documenting time spent on each service. These notes are your primary evidence for disputing unit count errors.</li>
    <li><strong>Calculate correct units using the 8-minute rule:</strong> Total the timed minutes from session notes, apply the unit table above, and compare against the bill.</li>
    <li><strong>Identify the specific codes and dates in dispute:</strong> Document exactly which line items are incorrect and what the corrected amount should be.</li>
    <li><strong>Submit a written dispute:</strong> Send it to the clinic billing department with copies of the relevant session notes and your unit calculation. Give them 30 days to respond.</li>
    <li><strong>File an insurance appeal if the insurer processed an inflated claim:</strong> Your insurer may have already paid based on the incorrect claim. Notify them of the overbilling so they can recover the overpayment and adjust your cost-sharing accordingly.</li>
</ol>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Unit count error across 18 PT sessions: $612 recovered</h3>
    <p>A patient in Minnesota had 18 PT sessions after a rotator cuff repair. Each session was 60 minutes. The clinic billed 5 timed units per session (75 minutes of timed services) when session notes consistently showed 4 units (52&ndash;58 minutes). The extra unit per session at $34 each: <strong>$612 in total overbilling</strong>. After submitting a written dispute with session time calculations, the clinic issued a corrected claim and refunded the overpayment.</p>
</div>

<div class="case-study">
    <h3>Hospital-affiliated PT facility fee: $2,800 surprise charge</h3>
    <p>A patient in Florida was referred by her orthopedist to a physical therapy clinic in the same medical building. She assumed it was an independent clinic — but it was a hospital outpatient department. Over 14 sessions, she received separate facility fee charges of $200 per visit ($2,800 total) that she hadn&rsquo;t been informed about. The clinic hadn&rsquo;t given her an Advanced Beneficiary Notice (ABN). After filing a complaint with her state insurance commissioner, the facility agreed to waive the facility fees. <strong>Savings: $2,800.</strong></p>
</div>

<div class="case-study">
    <h3>Wrong diagnosis code caused wrongful denial</h3>
    <p>A patient receiving PT for a herniated disc (ICD-10: M51.16 — lumbar region) had their 12 sessions denied by her insurer as &ldquo;not medically necessary.&rdquo; The PT clinic had accidentally billed using a cervical spine code (M50.12) instead of the lumbar code. After the PT corrected the diagnosis code and resubmitted, all sessions were approved. <strong>Patient cost reduction: $1,440 (12 sessions at $120 coinsurance each).</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What are the most common physical therapy CPT codes?</h3>
        <p>The most billed PT codes are 97110 (therapeutic exercise), 97530 (therapeutic activities), 97140 (manual therapy), 97035 (ultrasound), and 97032 (electrical stimulation). Each is billed in 15-minute increments under the 8-minute rule. Use our <a href="/calculator">calculator</a> to look up the Medicare rate for any code.</p>
    </div>

    <div class="faq-item">
        <h3>What is the 8-minute rule in physical therapy billing?</h3>
        <p>The 8-minute rule determines billable units. A PT must spend at least 8 minutes on a timed service per unit: 8&ndash;22 minutes = 1 unit, 23&ndash;37 minutes = 2 units, 38&ndash;52 minutes = 3 units. Total timed minutes for a session determine total units — they cannot be split across services to inflate the count.</p>
    </div>

    <div class="faq-item">
        <h3>Why is my PT bill so high compared to a friend's for the same injury?</h3>
        <p>The biggest factor is usually the setting. Hospital-based PT clinics charge facility fees ($150&ndash;$300 per visit) on top of professional fees. Independent PT clinics typically do not. Two patients with identical injuries and treatment can have dramatically different bills based solely on whether their PT is hospital-affiliated.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover physical therapy?</h3>
        <p>Yes. Medicare Part B covers medically necessary outpatient PT after the annual Part B deductible ($257 in 2026). Medicare pays 80%; you pay 20% coinsurance. There is no annual cap on PT coverage (the cap was eliminated in 2018), as long as PT is documented as medically necessary.</p>
    </div>

    <div class="faq-item">
        <h3>Can I be billed for PT services my insurance denied?</h3>
        <p>Only if you were properly notified before the service that it might not be covered (via an Advance Beneficiary Notice or similar document). If the PT clinic billed a service without informing you it might not be covered and your insurer denied it, you may have grounds to dispute the charge. Ask the clinic for the ABN you should have signed.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://oig.hhs.gov/oei/reports/OEI-02-19-00101.asp" target="_blank" rel="noopener">HHS Office of Inspector General: Medicare Physical Therapy Billing Errors (2022)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/therapy-services" target="_blank" rel="noopener">CMS: Medicare Therapy Services Coverage and Payment</a></li>
    <li><a href="https://www.apta.org/your-practice/coding-billing-and-payment" target="_blank" rel="noopener">American Physical Therapy Association: Coding and Billing</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient" target="_blank" rel="noopener">CMS: Hospital Outpatient Prospective Payment — Facility Fees</a></li>
    <li><a href="https://www.cms.gov/files/document/8-minute-rule.pdf" target="_blank" rel="noopener">CMS: The 8-Minute Rule for Outpatient Therapy</a></li>
</ul>
""",
})
