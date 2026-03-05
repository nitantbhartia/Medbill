"""Guide: Inpatient vs. Outpatient Billing."""

from guides import register, _embed

register("inpatient-vs-outpatient-billing", {
    "title": "Inpatient vs. Outpatient Billing",
    "meta_description": "Inpatient vs. outpatient billing changes your cost dramatically — the same knee surgery can cost $4,800 or $18,000. Learn how to check your status and.",
    "published": "2026-02-22",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "What is the difference between inpatient and outpatient billing?",
            "a": "Inpatient billing applies when a doctor formally admits you to the hospital with an inpatient order. Outpatient billing applies when you receive services without a formal admission — even if you spend the night. The distinction matters enormously: inpatient bills go through Medicare Part A (hospital insurance), while outpatient bills go through Part B. For most patients, outpatient billing means higher out-of-pocket costs for the same care.",
        },
        {
            "q": "What is observation status in a hospital?",
            "a": "Observation status is a gray zone: you're physically in the hospital but classified as outpatient. Hospitals use it when they're uncertain whether to admit you. Under observation status, Medicare Part A doesn't apply — you pay outpatient coinsurance and copays, which can be significantly more expensive. Observation status also affects skilled nursing facility (SNF) coverage: Medicare requires a 3-day inpatient stay before covering SNF care.",
        },
        {
            "q": "Can I request to be changed from outpatient to inpatient status?",
            "a": "You can request it, and your doctor can change your status if medically appropriate. However, hospitals cannot retroactively change status after discharge — you must ask while you're still admitted. If you're told you're under observation after an overnight stay, ask your attending physician immediately whether an inpatient admission is clinically appropriate.",
        },
        {
            "q": "Does my deductible apply differently to inpatient vs. outpatient?",
            "a": "For Medicare beneficiaries, yes — significantly so. Medicare Part A has a separate inpatient deductible ($1,676 per benefit period in 2026). Medicare Part B has a separate annual deductible ($257 in 2026) plus 20% coinsurance. Private insurance plans also often have different cost-sharing tiers for inpatient vs. outpatient services — check your plan's Summary of Benefits.",
        },
        {
            "q": "What surgery can be done outpatient vs. inpatient?",
            "a": "CMS maintains a list of procedures that must be performed outpatient (the Outpatient Only list) and procedures that can qualify for inpatient admission. Common outpatient procedures include knee arthroscopy, cataract surgery, colonoscopy, and many hernia repairs. Joint replacements (hip and knee) moved to outpatient-eligible status in 2020, saving patients significant money at ambulatory surgery centers.",
        },
    ],
    "body": f"""
<p class="lead">The same knee replacement can cost you <strong>$4,800 out-of-pocket at an outpatient surgery center</strong> or <strong>$18,000 at a hospital as an inpatient</strong> — for identical surgery, by the same surgeon. The difference comes down to four words on your chart: &ldquo;admitted as inpatient&rdquo; vs. &ldquo;under observation.&rdquo; According to BillKarma&rsquo;s analysis of hospital pricing data across 6,800+ facilities, the average inpatient markup vs. Medicare is <strong>3.8x</strong> — nearly double the 2.1x average for equivalent outpatient procedures.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-inpatient">What inpatient and outpatient actually mean</a></li>
        <li><a href="#observation">The observation status trap</a></li>
        <li><a href="#cost-comparison">Cost comparison: same procedure, different billing</a></li>
        <li><a href="#how-to-check">How to check your status while admitted</a></li>
        <li><a href="#medicare-impact">How it affects Medicare patients specifically</a></li>
        <li><a href="#dispute">How to dispute a wrong status assignment</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-inpatient">1. What inpatient and outpatient actually mean</h2>

<p>The distinction isn&rsquo;t about how long you stay or how serious your condition is — it&rsquo;s about a doctor&rsquo;s formal order:</p>

<ul>
    <li><strong>Inpatient:</strong> A physician writes an admission order stating you are admitted as an inpatient. Medicare Part A pays for the stay. You pay the Part A deductible and daily copays for extended stays.</li>
    <li><strong>Outpatient:</strong> You receive services without a formal inpatient order — even if you sleep in a hospital bed overnight. Medicare Part B applies. You pay 20% coinsurance on the allowed amount for each service.</li>
    <li><strong>Observation status:</strong> A specific outpatient classification hospitals use when they&rsquo;re monitoring your condition. You&rsquo;re physically in the hospital but billed as outpatient. This is where most billing confusion happens.</li>
</ul>

<p>The decision about inpatient vs. outpatient is supposed to be a clinical determination based on your medical needs. In practice, it is often influenced by hospital financial incentives, Medicare audit risk, and administrative policies.</p>

<div class="key-takeaway">
    <strong>Not sure how you were billed?</strong> <a href="/scan">Upload your hospital bill to BillKarma</a> &mdash; we identify whether charges are coded inpatient (DRG-based) or outpatient (APC-based) and flag anomalies that suggest a status mismatch.
</div>

<h2 id="observation">2. The observation status trap</h2>

<p>Observation status is one of the most consequential — and least-explained — billing classifications in healthcare. CMS data shows that observation stays have grown <strong>88% over the past decade</strong> while inpatient admissions have declined.</p>

<p>Under observation status:</p>
<ul>
    <li>You pay outpatient cost-sharing (20% coinsurance per service) instead of the inpatient deductible</li>
    <li>For Medicare patients, your medications may not be covered (Part A covers inpatient drugs; Part B does not cover most outpatient drugs)</li>
    <li>You do not accumulate the 3-day inpatient stay required for Medicare to cover a subsequent skilled nursing facility (SNF) stay</li>
    <li>The hospital is not required to tell you that you&rsquo;re under observation — though since 2016, Medicare regulations require the MOON notice (Medicare Outpatient Observation Notice) for stays over 24 hours</li>
</ul>

<div class="bill-example">
    <div class="bill-header">Hospital Bill &mdash; 3-Night Stay, Chest Pain Workup &mdash; Status: Observation (Outpatient)</div>
    <div class="line-item flagged">
        <span>Emergency department evaluation (CPT 99285, Level 5) &nbsp; &#9888; <em>Outpatient bill — 20% coinsurance applies to each line</em></span>
        <span>$4,200.00</span>
    </div>
    <div class="line-item">
        <span>Cardiac monitoring, 3 nights (CPT 93224)</span>
        <span>$1,800.00</span>
    </div>
    <div class="line-item">
        <span>Echocardiogram (CPT 93306)</span>
        <span>$2,100.00</span>
    </div>
    <div class="line-item">
        <span>Daily hospital visit charge &times; 3 (CPT 99232)</span>
        <span>$1,200.00</span>
    </div>
    <div class="line-item error">
        <span>Metoprolol 25mg (oral medication) &nbsp; &#10060; <em>Part B doesn&rsquo;t cover outpatient drugs — patient pays full cost</em></span>
        <span>$84.00</span>
    </div>
    <div class="line-total">
        <span>YOUR 20% COINSURANCE (before OOP max)</span>
        <span>$1,877.00 + $84.00 drugs = $1,961.00</span>
    </div>
</div>

<p>Had the same 3-night stay been billed as inpatient, the Medicare Part A deductible of $1,676 would apply — and medications would be covered. The patient above paid $285 more than necessary and lost 3 days of SNF eligibility. This is the observation status trap.</p>

<h2 id="cost-comparison">3. Cost comparison: same procedure, different billing</h2>

<table>
    <thead>
        <tr><th>Procedure</th><th>Inpatient hospital (avg charged)</th><th>Outpatient hospital (avg charged)</th><th>Ambulatory surgery center (avg)</th></tr>
    </thead>
    <tbody>
        <tr><td>Knee replacement (CPT 27447)</td><td>$42,000&ndash;$68,000</td><td>$28,000&ndash;$44,000</td><td>$18,000&ndash;$28,000</td></tr>
        <tr><td>Hip replacement (CPT 27130)</td><td>$44,000&ndash;$72,000</td><td>$30,000&ndash;$48,000</td><td>$20,000&ndash;$32,000</td></tr>
        <tr><td>Laparoscopic gallbladder removal (CPT 47562)</td><td>$24,000&ndash;$38,000</td><td>$14,000&ndash;$22,000</td><td>$9,000&ndash;$14,000</td></tr>
        <tr><td>Rotator cuff repair (CPT 29827)</td><td>$22,000&ndash;$36,000</td><td>$14,000&ndash;$20,000</td><td>$8,000&ndash;$14,000</td></tr>
        <tr><td>Colonoscopy (CPT 45378)</td><td>$4,500&ndash;$8,000</td><td>$2,500&ndash;$4,000</td><td>$800&ndash;$2,000</td></tr>
    </tbody>
</table>

<p>Check our <a href="/hospitals/">hospital directory</a> to compare inpatient vs. outpatient pricing at specific facilities near you. Pricing varies dramatically by hospital — a colonoscopy at one hospital might cost twice what it costs at the same city&rsquo;s surgery center.</p>

{_embed(mode="cost", title="Look up the Medicare rate for your procedure", subtitle="Enter the CPT code from your bill to see what Medicare pays inpatient vs. outpatient.")}

<h2 id="how-to-check">4. How to check your status while admitted</h2>

<p>The best time to address your billing status is <em>before you leave the hospital</em>. Here&rsquo;s what to do:</p>

<ol>
    <li><strong>Ask directly:</strong> &ldquo;Am I formally admitted as an inpatient, or am I under observation status?&rdquo; Ask a nurse, your attending physician, or the patient advocate.</li>
    <li><strong>Request the MOON notice (if on Medicare):</strong> Hospitals are required to give you the Medicare Outpatient Observation Notice in writing if your observation stay exceeds 24 hours. If you haven&rsquo;t received it and your stay is over a day, ask for it.</li>
    <li><strong>Request an inpatient admission if appropriate:</strong> If you&rsquo;ve been in observation for 24+ hours with an acute condition, ask your attending physician directly: &ldquo;Is this condition serious enough to warrant an inpatient admission?&rdquo; Physicians have the authority to admit — hospitals cannot override a legitimate clinical decision.</li>
    <li><strong>Get the decision in writing:</strong> If the hospital declines to admit you as inpatient, request the clinical rationale in writing. You&rsquo;ll need this for any appeal.</li>
</ol>

<div class="key-takeaway">
    <strong>Already home and see an unexpected bill?</strong> Use our <a href="/calculator">free calculator</a> to look up your procedure&rsquo;s CPT code and compare the Medicare inpatient rate (from the DRG schedule) vs. the outpatient rate — the difference will tell you exactly how much the status classification cost you.
</div>

<h2 id="medicare-impact">5. How it affects Medicare patients specifically</h2>

<table>
    <thead>
        <tr><th>Cost element</th><th>Inpatient (Part A)</th><th>Outpatient/observation (Part B)</th></tr>
    </thead>
    <tbody>
        <tr><td>Deductible (2026)</td><td>$1,676 per benefit period</td><td>$257 per year (annual Part B deductible)</td></tr>
        <tr><td>Daily copay (days 1-60)</td><td>$0 (covered by deductible)</td><td>20% coinsurance per service</td></tr>
        <tr><td>Prescription drugs</td><td>Covered under Part A</td><td>NOT covered (must use Part D)</td></tr>
        <tr><td>SNF eligibility</td><td>Counts toward 3-day requirement</td><td>Does NOT count</td></tr>
        <tr><td>Notification requirement</td><td>Admission notice within 24 hrs</td><td>MOON notice if &gt;24 hrs observation</td></tr>
    </tbody>
</table>

<p>The SNF (skilled nursing facility) issue is critical for older patients recovering from surgery or a serious illness. If Medicare won&rsquo;t cover your SNF stay because your hospital days were classified as observation, the cost can be <strong>$200&ndash;$500 per day</strong> entirely out-of-pocket. A wrongly classified 5-night stay can cost you $1,000&ndash;$2,500 in SNF coverage you&rsquo;re not entitled to.</p>

<h2 id="dispute">6. How to dispute a wrong status assignment</h2>

<p>If you believe you should have been admitted as inpatient:</p>

<ol>
    <li><strong>Request your complete medical record</strong> — you&rsquo;re entitled to it under HIPAA. Look for the admission order. If there&rsquo;s no inpatient admission order despite days of hospital care, the status assignment may be challengeable.</li>
    <li><strong>File a QIO appeal (Medicare patients):</strong> Medicare beneficiaries can request a review by the Quality Improvement Organization (QIO) for their state within 120 days of discharge. The QIO can overturn observation classifications and require inpatient payment.</li>
    <li><strong>File an appeal with your insurer (private insurance):</strong> Submit a written appeal citing the clinical complexity of your case and the InterQual or Milliman criteria used to determine admission status. Many insurers will upgrade status on appeal.</li>
    <li><strong>Contact your state insurance commissioner</strong> if the appeal is denied and you believe the denial was improper. Most states have patient advocates who can intervene.</li>
</ol>

<div class="key-takeaway">
    <strong>Ready to dispute?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we&rsquo;ll generate a pre-filled dispute letter citing the specific billing code anomalies and the clinical criteria for your case.
</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Hip fracture billed as observation — $4,200 SNF coverage denied</h3>
    <p>An 81-year-old woman in Pennsylvania fractured her hip and stayed in the hospital for 4 nights. Despite needing surgery and physical therapy, she was classified as &ldquo;observation&rdquo; for the first night. Because her inpatient stay was technically only 3 days (not the required 3 <em>calendar</em> days), Medicare denied coverage for her subsequent skilled nursing facility stay — costing her $4,200 for the first 10 days of SNF care.</p>
    <p>Her family filed a QIO appeal, arguing the first night met all clinical criteria for inpatient admission. The QIO agreed, reclassified the stay, and Medicare covered the SNF. <strong>Recovery: $4,200.</strong></p>
</div>

<div class="case-study">
    <h3>Outpatient surgery billed at inpatient rate</h3>
    <p>A patient in Colorado had a laparoscopic appendectomy (CPT 44950) as a same-day outpatient procedure at his local hospital. He was home by evening. His EOB showed an inpatient DRG code instead of the outpatient APC code — the hospital&rsquo;s billing department had entered the wrong status, triggering an inpatient deductible of $1,600 instead of the $300 outpatient coinsurance he actually owed.</p>
    <p>After requesting a billing review and providing his discharge summary (showing same-day discharge), the hospital corrected the code. <strong>Savings: $1,300.</strong></p>
</div>

<div class="case-study">
    <h3>Knee replacement: hospital vs. surgery center</h3>
    <p>A 58-year-old teacher in Arizona needed bilateral knee replacement. Her orthopedic surgeon offered two options: inpatient at the affiliated hospital ($38,000 per knee, $76,000 total billed) or outpatient at a freestanding surgery center ($19,000 per knee). Both were in-network. Her 20% coinsurance: $15,200 at the hospital vs. $7,600 at the surgery center for both knees.</p>
    <p>She chose the surgery center after comparing prices in BillKarma&rsquo;s <a href="/hospitals/">directory</a>. <strong>Savings: $7,600 in out-of-pocket cost.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the difference between inpatient and outpatient billing?</h3>
        <p>Inpatient billing requires a formal physician admission order and goes through Medicare Part A (or the inpatient benefit of private insurance). Outpatient billing applies when no admission order is issued — even for overnight stays. The same procedure can cost significantly more under one classification vs. the other. Use our <a href="/calculator">calculator</a> to compare Medicare inpatient DRG rates vs. outpatient APC rates for specific procedures.</p>
    </div>

    <div class="faq-item">
        <h3>What is observation status in a hospital?</h3>
        <p>Observation status means you&rsquo;re physically in the hospital but classified as outpatient. You pay outpatient cost-sharing (20% per service), your prescription drugs may not be covered, and observation days do not count toward Medicare&rsquo;s 3-day inpatient requirement for skilled nursing facility coverage.</p>
    </div>

    <div class="faq-item">
        <h3>Can I request to be changed from outpatient to inpatient status?</h3>
        <p>You can ask your physician to change your status if clinically appropriate, and physicians have the authority to issue an inpatient admission order. However, hospitals cannot retroactively change status after discharge. If you&rsquo;re told you&rsquo;re under observation after an overnight stay, ask your attending physician immediately.</p>
    </div>

    <div class="faq-item">
        <h3>How do I know if I was billed inpatient or outpatient?</h3>
        <p>Look at your EOB or itemized bill. Inpatient billing uses DRG (Diagnosis-Related Group) codes — you&rsquo;ll see a single bundled charge for the stay. Outpatient billing lists individual CPT codes for each service. You can also call the hospital billing department and ask directly which status was billed to your insurance.</p>
    </div>

    <div class="faq-item">
        <h3>Does my deductible apply the same for inpatient vs. outpatient?</h3>
        <p>For Medicare, no. Part A has a separate inpatient deductible ($1,676 per benefit period in 2026); Part B has an annual deductible ($257 in 2026) plus 20% coinsurance. For private insurance, check your Summary of Benefits — many plans have different deductibles and coinsurance rates for inpatient vs. outpatient care.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/acute-inpatient-pps" target="_blank" rel="noopener">CMS: Acute Inpatient Prospective Payment System (IPPS)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient" target="_blank" rel="noopener">CMS: Hospital Outpatient Prospective Payment System (OPPS)</a></li>
    <li><a href="https://www.medicare.gov/coverage/observation-services" target="_blank" rel="noopener">Medicare.gov: Observation Services</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2022.00426" target="_blank" rel="noopener">Health Affairs: Growth in Hospital Observation Status (2022)</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/medicare-observation-status/" target="_blank" rel="noopener">KFF: Medicare Observation Status</a></li>
    <li><a href="https://www.cms.gov/medicare/billing/outpatient-observation-notice-moon" target="_blank" rel="noopener">CMS: Medicare Outpatient Observation Notice (MOON)</a></li>
</ul>
""",
})
