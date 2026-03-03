"""Guide: ER vs Urgent Care vs Telehealth Costs."""

from guides import register, _embed

register("er-vs-urgent-care-costs", {
    "title": "ER vs. Urgent Care vs. Telehealth: Cost Comparison and When to Go Where",
    "meta_description": "Average ER visit costs $2,200 vs. $250 at urgent care vs. $75 for telehealth. Know which conditions need the ER and which don't. Save thousands.",
    "published": "2026-03-03",
    "author": "BillKarma Team",
    "category": "Medical Bills",
    "faqs": [
        {
            "q": "How much does an ER visit cost vs. urgent care?",
            "a": "The average ER visit costs $2,200 (with some visits exceeding $10,000) while the average urgent care visit costs $150-$300. This difference exists primarily because of the facility fee: ERs charge a facility fee of $500-$3,000 just for walking through the door, regardless of what treatment you receive. Urgent care centers do not charge facility fees. For the same condition (e.g., a minor laceration), the ER will charge 5-10x more than urgent care for essentially the same treatment.",
        },
        {
            "q": "When should I go to the ER instead of urgent care?",
            "a": "Go to the ER for: chest pain or suspected heart attack, stroke symptoms (face drooping, arm weakness, speech difficulty), severe difficulty breathing, uncontrolled bleeding, loss of consciousness, severe allergic reactions (anaphylaxis), major trauma or broken bones with visible deformity, seizures, poisoning or overdose, and severe abdominal pain with fever. Go to urgent care for: minor cuts needing stitches, sprains and minor fractures, mild to moderate infections, flu symptoms, minor burns, rashes, eye infections, and minor allergic reactions.",
        },
        {
            "q": "Does insurance cover urgent care visits?",
            "a": "Yes. Most insurance plans cover urgent care visits with a copay of $25-$75, significantly less than the ER copay of $150-$500. Under the ACA, emergency services must be covered at in-network rates even at out-of-network ERs, and the No Surprises Act prevents balance billing for ER visits. However, urgent care visits at out-of-network facilities may result in higher costs. Check your plan's network before going to urgent care.",
        },
        {
            "q": "Can I use telehealth instead of going to the ER or urgent care?",
            "a": "Telehealth is appropriate for many conditions that don't require physical examination or testing: cold and flu symptoms, minor skin issues, medication refills, urinary symptoms, mental health concerns, minor eye issues (pink eye), and follow-up visits. Telehealth visits cost $50-$75 without insurance or $0-$25 with insurance. Most telehealth services can prescribe medications and order lab work. It's available 24/7 and eliminates travel time and waiting rooms.",
        },
        {
            "q": "What is a facility fee and why does the ER charge one?",
            "a": "A facility fee is a separate charge for the use of the facility itself, distinct from the charges for actual medical services. ERs charge facility fees of $500-$3,000+ because they must maintain 24/7 readiness with specialized equipment, trauma capabilities, and staffing. The facility fee is charged regardless of whether you use any of those capabilities. If you visit the ER for a sore throat, you still pay the facility fee designed to cover trauma and critical care readiness. This is the primary reason ER visits are so expensive.",
        },
        {
            "q": "What if I went to the ER and the bill is too high?",
            "a": "If you've already received an ER bill: scan it for errors (duplicate charges, upcoding are common in ER billing), check if the facility fee is appropriate for the level of care received, verify that the No Surprises Act was applied correctly (no balance billing for emergency services), apply for hospital financial assistance if you qualify, negotiate the bill using Medicare rates as a benchmark, and request an itemized bill to review every charge. Upload the bill to BillKarma for automated error detection.",
        },
    ],
    "body": f"""
<p class="lead">The average ER visit costs <strong>$2,200</strong>. The average urgent care visit costs <strong>$250</strong>. Telehealth costs <strong>$50&ndash;$75</strong>. For many conditions, all three provide the same quality of care. The difference is thousands of dollars. Knowing where to go &mdash; and where NOT to go &mdash; is one of the simplest ways to avoid massive medical bills. Here is how to make the right call every time.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-comparison">The real cost comparison</a></li>
        <li><a href="#when-er">When you MUST go to the ER</a></li>
        <li><a href="#when-urgent-care">When urgent care is the right choice</a></li>
        <li><a href="#when-telehealth">When telehealth saves the most</a></li>
        <li><a href="#facility-fee">The facility fee: why ERs cost so much</a></li>
        <li><a href="#reduce-er-bill">Already got an ER bill? How to reduce it</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-comparison">1. The real cost comparison</h2>

<table>
    <thead>
        <tr><th>Setting</th><th>Average cost (uninsured)</th><th>Typical copay (insured)</th><th>Wait time</th><th>Hours</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Emergency Room</strong></td><td>$2,200 (range: $600&ndash;$20,000+)</td><td>$150&ndash;$500</td><td>2&ndash;6 hours</td><td>24/7</td></tr>
        <tr><td><strong>Urgent Care</strong></td><td>$150&ndash;$300</td><td>$25&ndash;$75</td><td>15&ndash;45 min</td><td>8am&ndash;8pm typical</td></tr>
        <tr><td><strong>Telehealth</strong></td><td>$50&ndash;$75</td><td>$0&ndash;$25</td><td>0&ndash;15 min</td><td>24/7 (many services)</td></tr>
        <tr><td><strong>Primary Care</strong></td><td>$150&ndash;$350</td><td>$20&ndash;$50</td><td>Days&ndash;weeks for appointment</td><td>Business hours</td></tr>
    </tbody>
</table>

<div class="bill-example">
    <div class="bill-header">Same condition, different settings: minor laceration (cut needing stitches)</div>
    <div class="line-item flagged">
        <span>Emergency Room (facility fee + ER physician + supplies)</span>
        <span>$1,800&ndash;$3,500</span>
    </div>
    <div class="line-item">
        <span>Urgent Care (visit + procedure + supplies)</span>
        <span>$200&ndash;$500</span>
    </div>
    <div class="line-total">
        <span>Savings by choosing urgent care</span>
        <span>$1,300&ndash;$3,000</span>
    </div>
</div>

<div class="bill-example">
    <div class="bill-header">Same condition, different settings: UTI (urinary tract infection)</div>
    <div class="line-item flagged">
        <span>Emergency Room</span>
        <span>$1,200&ndash;$2,500</span>
    </div>
    <div class="line-item">
        <span>Urgent Care</span>
        <span>$150&ndash;$250</span>
    </div>
    <div class="line-item">
        <span>Telehealth</span>
        <span>$50&ndash;$75</span>
    </div>
    <div class="line-total">
        <span>Savings: Telehealth vs. ER</span>
        <span>$1,125&ndash;$2,425</span>
    </div>
</div>

<h2 id="when-er">2. When you MUST go to the ER</h2>

<p>The ER is designed for life-threatening emergencies. Go to the ER immediately for:</p>

<ul>
    <li><strong>Chest pain or pressure</strong> &mdash; could indicate heart attack</li>
    <li><strong>Stroke symptoms</strong> &mdash; face drooping, arm weakness, speech difficulty (remember FAST)</li>
    <li><strong>Severe difficulty breathing</strong> &mdash; can&rsquo;t catch breath, turning blue</li>
    <li><strong>Uncontrolled bleeding</strong> &mdash; can&rsquo;t stop with direct pressure</li>
    <li><strong>Loss of consciousness or altered mental status</strong></li>
    <li><strong>Severe allergic reaction (anaphylaxis)</strong> &mdash; throat swelling, difficulty breathing</li>
    <li><strong>Major trauma</strong> &mdash; car accident, fall from height, head injury with confusion</li>
    <li><strong>Compound fracture</strong> &mdash; bone visible through skin</li>
    <li><strong>Seizure</strong> &mdash; especially first-time or prolonged</li>
    <li><strong>Poisoning or overdose</strong></li>
    <li><strong>Severe burns</strong> &mdash; larger than your palm, on face/hands/genitals, or chemical/electrical</li>
    <li><strong>Pregnancy emergencies</strong> &mdash; heavy bleeding, severe pain, water breaking before 37 weeks</li>
</ul>

<div class="key-takeaway">
    <strong>When in doubt, call 911 or go to the ER.</strong> This guide is about avoiding <em>unnecessary</em> ER visits for non-emergencies, not about avoiding the ER when you genuinely need it. If you think you&rsquo;re having a medical emergency, go to the ER. Your life is worth more than any medical bill. You can always <a href="/scan">scan the bill for errors</a> and negotiate later.
</div>

<h2 id="when-urgent-care">3. When urgent care is the right choice</h2>

<p>Urgent care centers can handle most non-life-threatening conditions that need same-day attention:</p>

<table>
    <thead>
        <tr><th>Condition</th><th>Urgent care can handle?</th><th>Typical cost</th></tr>
    </thead>
    <tbody>
        <tr><td>Minor cuts needing stitches</td><td>Yes</td><td>$200&ndash;$500</td></tr>
        <tr><td>Sprains and strains</td><td>Yes (X-ray available at most)</td><td>$200&ndash;$400</td></tr>
        <tr><td>Simple fractures (fingers, toes, wrist)</td><td>Yes</td><td>$250&ndash;$600</td></tr>
        <tr><td>Ear infections, sinus infections</td><td>Yes</td><td>$150&ndash;$250</td></tr>
        <tr><td>Flu, cold, COVID symptoms</td><td>Yes (testing available)</td><td>$150&ndash;$300</td></tr>
        <tr><td>Urinary tract infections</td><td>Yes</td><td>$150&ndash;$250</td></tr>
        <tr><td>Minor burns</td><td>Yes</td><td>$150&ndash;$350</td></tr>
        <tr><td>Rashes, skin infections</td><td>Yes</td><td>$150&ndash;$250</td></tr>
        <tr><td>Pink eye, styes</td><td>Yes</td><td>$150&ndash;$200</td></tr>
        <tr><td>Minor allergic reactions (no breathing issues)</td><td>Yes</td><td>$150&ndash;$300</td></tr>
        <tr><td>Back pain (non-traumatic)</td><td>Yes</td><td>$150&ndash;$300</td></tr>
    </tbody>
</table>

<p><strong>Tips for urgent care visits:</strong></p>
<ul>
    <li>Check that the facility is <strong>in-network</strong> before going. Use your insurer&rsquo;s provider search tool.</li>
    <li>Many urgent care centers accept <strong>walk-ins and same-day online scheduling</strong>.</li>
    <li>Ask about <strong>self-pay rates</strong> if you&rsquo;re uninsured &mdash; many offer flat rates of $150&ndash;$200.</li>
    <li>Avoid urgent care centers attached to hospitals &mdash; some charge <strong>hospital facility fees</strong> that make them nearly as expensive as the ER.</li>
</ul>

<h2 id="when-telehealth">4. When telehealth saves the most</h2>

<p>Telehealth is the most cost-effective option for conditions that don&rsquo;t require physical examination or testing:</p>

<ul>
    <li><strong>Cold and flu symptoms</strong> &mdash; diagnosis and prescription without leaving home</li>
    <li><strong>Urinary tract infections</strong> &mdash; many providers can diagnose based on symptoms alone</li>
    <li><strong>Medication refills</strong> &mdash; when your doctor is unavailable and you need a prescription renewed</li>
    <li><strong>Skin rashes</strong> &mdash; send photos for evaluation</li>
    <li><strong>Pink eye</strong> &mdash; visual diagnosis, antibiotic prescription</li>
    <li><strong>Mental health</strong> &mdash; therapy and psychiatry sessions</li>
    <li><strong>Minor allergic reactions</strong> &mdash; medication recommendations</li>
    <li><strong>Follow-up visits</strong> &mdash; check-ins after procedures or medication changes</li>
</ul>

<p><strong>Popular telehealth options:</strong></p>
<ul>
    <li><strong>Your insurance plan&rsquo;s telehealth</strong> &mdash; often $0&ndash;$25 copay. Check your plan first.</li>
    <li><strong>Amazon Clinic, Sesame, PlushCare</strong> &mdash; flat-rate visits $50&ndash;$75 without insurance.</li>
    <li><strong>Urgent care telehealth</strong> &mdash; many urgent care chains now offer virtual visits at lower rates than in-person.</li>
</ul>

<h2 id="facility-fee">5. The facility fee: why ERs cost so much</h2>

<p>The single biggest reason ER visits are expensive is the <strong>facility fee</strong> &mdash; a separate charge for using the emergency department, distinct from any charges for medical services you receive.</p>

<div class="bill-example">
    <div class="bill-header">Anatomy of an ER bill for a sore throat (strep test + antibiotic)</div>
    <div class="line-item flagged">
        <span>Emergency department facility fee (Level 3)</span>
        <span>$1,400</span>
    </div>
    <div class="line-item">
        <span>ER physician evaluation (99283)</span>
        <span>$350</span>
    </div>
    <div class="line-item">
        <span>Rapid strep test</span>
        <span>$55</span>
    </div>
    <div class="line-item">
        <span>Antibiotic prescription</span>
        <span>$15</span>
    </div>
    <div class="line-total">
        <span>Total ER bill for a sore throat</span>
        <span>$1,820</span>
    </div>
</div>

<p>The same visit at urgent care: $150&ndash;$200 total. The difference is almost entirely the facility fee.</p>

<p><strong>Why facility fees exist:</strong> ERs must maintain 24/7 staffing, specialized equipment, trauma capabilities, and regulatory compliance. These costs are spread across all patients via facility fees. The problem is that patients with non-emergency conditions pay the same facility fee as trauma patients.</p>

<p><strong>Watch out for &ldquo;freestanding ERs.&rdquo;</strong> These look like urgent care centers but are classified as emergency rooms and charge ER-level facility fees. Look for the word &ldquo;emergency&rdquo; in the facility name. If it says &ldquo;emergency&rdquo; instead of &ldquo;urgent care,&rdquo; expect ER pricing.</p>

<h2 id="reduce-er-bill">6. Already got an ER bill? How to reduce it</h2>

<p>If you&rsquo;ve already visited the ER and received a large bill:</p>

<ol>
    <li><strong>Request an itemized bill.</strong> Ask for a detailed breakdown of every charge. ER bills are notorious for errors.</li>
    <li><strong>Scan for errors.</strong> <a href="/scan">Upload the bill to BillKarma</a> to check for duplicate charges, upcoding (billing a higher ER level than the care warranted), and unbundling.</li>
    <li><strong>Check the facility fee level.</strong> ER visits are coded Level 1&ndash;5. A sore throat should be Level 1&ndash;2, not Level 4&ndash;5. If the facility fee level doesn&rsquo;t match the severity of your condition, this is upcoding.</li>
    <li><strong>Verify No Surprises Act compliance.</strong> If you received emergency care at an out-of-network facility, the No Surprises Act limits what you can be charged. You should not be balance-billed.</li>
    <li><strong>Apply for financial assistance.</strong> <a href="/charity-care">Check eligibility</a> at the hospital. ER bills are covered under hospital financial assistance programs.</li>
    <li><strong>Negotiate using Medicare rates.</strong> Use the <a href="/calculator">BillKarma calculator</a> to check what Medicare pays for the same ER visit level. Offer 150&ndash;200% of Medicare as a fair price.</li>
</ol>

<div class="case-study">
    <h3>Case study: $4,800 ER bill reduced to $600</h3>
    <p><strong>Situation:</strong> David went to the ER at 10pm for severe abdominal pain, worried it was appendicitis. After a CT scan and blood work, the diagnosis was gastritis. He received IV fluids, an antacid, and was discharged 4 hours later. Total bill: $4,800.</p>
    <p><strong>What he did:</strong> He <a href="/scan">uploaded the bill to BillKarma</a>, which flagged: the visit was coded as Level 5 (highest severity) when it should have been Level 3, adding $1,200 in excess facility fees. The CT scan was billed at $2,100 when the hospital&rsquo;s published cash rate was $800. He called billing, disputed the ER level coding, requested the published CT scan rate, and applied for the hospital&rsquo;s self-pay discount (30%).</p>
    <p><strong>Result:</strong> Corrected ER level: $1,400 &rarr; $800. CT scan corrected to published rate: $2,100 &rarr; $800. Remaining charges: $500. 30% self-pay discount applied. <strong>Final bill: $600 instead of $4,800.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Can urgent care handle broken bones?</h3>
        <p>Many urgent care centers can diagnose and treat simple fractures (fingers, toes, wrists) with X-ray and splinting. Complex fractures, compound fractures (bone through skin), or fractures requiring surgery need the ER. When in doubt, call the urgent care center first and describe the injury &mdash; they&rsquo;ll tell you if they can handle it.</p>
    </div>
    <div class="faq-item">
        <h3>What if urgent care is closed and it&rsquo;s not an emergency?</h3>
        <p>Options: 24/7 telehealth for conditions that don&rsquo;t need in-person care, nurse hotlines (many insurance plans offer 24/7 nurse lines that can advise you), or wait until urgent care opens in the morning if the condition is stable. Going to the ER for a non-emergency at 2am will cost thousands for the same care you could get at urgent care for $200 in a few hours.</p>
    </div>
    <div class="faq-item">
        <h3>What is a freestanding ER and why should I avoid it?</h3>
        <p>Freestanding ERs are emergency rooms that are not attached to a hospital. They look like urgent care centers but charge ER prices, including facility fees of $1,000+. They are most common in Texas, Colorado, and Ohio. Always check whether a facility is &ldquo;urgent care&rdquo; or &ldquo;emergency&rdquo; before walking in. If it says &ldquo;emergency,&rdquo; expect ER pricing.</p>
    </div>
    <div class="faq-item">
        <h3>Does the No Surprises Act protect me in the ER?</h3>
        <p>Yes. The No Surprises Act prevents balance billing for emergency services at out-of-network facilities. You cannot be charged more than in-network cost-sharing for emergency care. This applies to both the facility fee and physician charges. If you receive a balance bill for emergency care, <a href="/scan">upload it to BillKarma</a> to verify compliance.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.healthsystemtracker.org/chart-collection/how-much-does-it-cost-to-go-to-the-emergency-room/" target="_blank" rel="noopener">Peterson-KFF Health System Tracker: Cost of Emergency Room Visits</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Emergency Services Protections</a></li>
    <li><a href="https://www.acep.org/life-as-a-physician/ethics/emtala/emtala-fact-sheet/" target="_blank" rel="noopener">ACEP: EMTALA Fact Sheet &mdash; Emergency Treatment Rights</a></li>
    <li><a href="https://www.ucaoa.org/resources/industry-reports" target="_blank" rel="noopener">Urgent Care Association: Urgent Care Industry Benchmarking Report</a></li>
    <li><a href="https://www.hhs.gov/about/news/telehealth-coverage-and-payment" target="_blank" rel="noopener">HHS: Telehealth Coverage and Payment Policy</a></li>
</ul>
""",
})
