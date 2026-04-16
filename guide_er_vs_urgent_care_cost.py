"""Guide: ER vs. Urgent Care Cost Comparison."""

from guides import register, _embed

register("emergency-room-vs-urgent-care-cost", {
    "title": "ER vs. Urgent Care Cost: The Complete 2026 Comparison",
    "meta_description": "Average ER visit costs $1,500–$3,000+. Urgent care averages $100–$200. Freestanding ERs charge ER prices without being hospitals. See when to go where and how to avoid surprise bills.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "How much does an ER visit cost vs. urgent care?",
            "a": "An average ER visit costs $1,500–$3,000+ in facility fees alone, before adding the physician's separate bill. Urgent care visits average $100–$200 total. After insurance, ER patients typically pay $150–$300 in copays, while urgent care copays are $25–$75. For the same condition treated at both settings, ER patients pay 5–15 times more than urgent care patients.",
        },
        {
            "q": "When should I go to the ER vs. urgent care?",
            "a": "Go to the ER for: chest pain, difficulty breathing, stroke symptoms (face drooping, arm weakness, speech difficulty), severe abdominal pain, major trauma, altered consciousness, uncontrolled bleeding, severe allergic reactions, and any life-threatening symptom. Go to urgent care for: minor infections (ear, sinus, UTI), sprains and strains, minor cuts needing stitches, flu symptoms, mild asthma, rashes, and conditions your primary care doctor would typically see.",
        },
        {
            "q": "What is a freestanding ER and why is it expensive?",
            "a": "A freestanding emergency room (FSER) is an ER that operates independently from a hospital—it's not physically connected to a hospital building. Despite looking like an urgent care center, it charges ER prices: the same $1,500–$3,000+ facility fees, the same ER E&M codes (99281–99285), and the same insurance cost-sharing as a hospital ER. BillKarma data shows freestanding ER patients pay an average of $2,400 more than hospital-based ER patients for the same conditions. Many patients arrive not knowing they're at a freestanding ER.",
        },
        {
            "q": "Can the ER turn me away if I can't pay?",
            "a": "No. Under the Emergency Medical Treatment and Labor Act (EMTALA), every hospital with an emergency department must provide a medical screening examination and stabilizing treatment to any patient who comes in, regardless of their ability to pay, insurance status, or citizenship. EMTALA applies to hospital-based ERs. Freestanding ERs in some states are not subject to EMTALA—another reason to know the difference before you arrive.",
        },
        {
            "q": "Are surprise bills possible at the ER?",
            "a": "Yes. Even if the hospital is in-network, the ER physician may be out-of-network—they are often employed by a separate staffing company, not the hospital. The No Surprises Act (effective 2022) now protects patients from most surprise bills for emergency care: you cannot be charged more than in-network cost-sharing for emergency services, even from OON providers. However, if you voluntarily consent to OON care after the emergency is stabilized, the No Surprises Act protections no longer apply.",
        },
    ],
    "body": f"""
<p class="lead">An average ER visit costs <strong>$1,500&ndash;$3,000+</strong> in facility fees alone. Urgent care averages <strong>$100&ndash;$200</strong> total. The wrong choice costs thousands. Freestanding ERs are the most dangerous trap&mdash;they look like urgent care but charge ER prices, and BillKarma finds freestanding ER patients pay an average of <strong>$2,400 more</strong> than hospital ER patients for identical conditions.</p>

<div class="answer-box">
    <strong>Quick answer:</strong> ER facility fees run $1,500&ndash;$3,000+ before the physician&rsquo;s separate bill. Urgent care costs $100&ndash;$200 total. After insurance, ER copays are $150&ndash;$300 vs. $25&ndash;$75 at urgent care. Freestanding ERs charge ER prices in urgent-care-looking buildings&mdash;always check the sign before entering. The No Surprises Act protects you from OON ER physician bills.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-comparison">Cost comparison: ER vs. urgent care vs. retail clinic</a></li>
        <li><a href="#when-er">When to go to the ER</a></li>
        <li><a href="#when-urgent-care">When urgent care is appropriate</a></li>
        <li><a href="#freestanding-er">Freestanding ERs: the most expensive trap</a></li>
        <li><a href="#insurance-coverage">How insurance treats ER visits differently</a></li>
        <li><a href="#emtala">EMTALA: your right to emergency care</a></li>
        <li><a href="#billing-codes">ER vs. urgent care billing codes</a></li>
        <li><a href="#surprise-billing">Surprise billing in the ER</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-comparison">1. Cost comparison: ER vs. urgent care vs. retail clinic</h2>

<table>
    <thead>
        <tr><th>Setting</th><th>Avg Total Cost</th><th>Avg Insurance Copay</th><th>Physician Bill Separate?</th><th>Wait Time</th></tr>
    </thead>
    <tbody>
        <tr><td>Hospital emergency room</td><td>$1,500&ndash;$3,500+</td><td>$150&ndash;$300</td><td>Yes (usually)</td><td>1&ndash;4+ hours</td></tr>
        <tr><td>Freestanding emergency room</td><td>$1,500&ndash;$3,500+</td><td>$150&ndash;$300 (if in-network)</td><td>Yes</td><td>Shorter than hospital ER</td></tr>
        <tr><td>Urgent care center</td><td>$100&ndash;$250</td><td>$25&ndash;$75</td><td>No (one bill)</td><td>15&ndash;60 minutes</td></tr>
        <tr><td>MinuteClinic / retail clinic</td><td>$70&ndash;$150</td><td>$15&ndash;$40</td><td>No</td><td>15&ndash;45 minutes</td></tr>
        <tr><td>Telehealth visit</td><td>$50&ndash;$100</td><td>$10&ndash;$40</td><td>No</td><td>Minutes</td></tr>
        <tr><td>Primary care office visit</td><td>$100&ndash;$200</td><td>$20&ndash;$50</td><td>No</td><td>Next available appt</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The ER bills two ways.</strong> Your ER visit generates (at minimum) two separate bills: one from the hospital for the facility fee, and one from the emergency physician or physician group for the professional fee. Sometimes you also receive bills from radiologists who read your X-rays and laboratorians who processed your bloodwork. A single ER visit can produce 3&ndash;5 separate bills.
</div>

{_embed(mode="cost", cpt="99285", title="Look Up ER Visit Rates", subtitle="See what Medicare pays for high-acuity ER visits (CPT 99285) in your area.")}

<h2 id="when-er">2. When to go to the ER</h2>

<p>The ER is the right choice when a delay in care could result in serious harm. Go to the ER for:</p>

<ul>
    <li><strong>Chest pain or pressure</strong> (assume cardiac until proven otherwise)</li>
    <li><strong>Difficulty breathing or shortness of breath</strong> at rest</li>
    <li><strong>Stroke symptoms:</strong> sudden facial drooping, arm weakness, slurred speech, sudden severe headache (&ldquo;worst headache of my life&rdquo;)</li>
    <li><strong>Major trauma:</strong> car accidents, falls from height, severe lacerations, suspected fractures with deformity</li>
    <li><strong>Altered consciousness or confusion</strong></li>
    <li><strong>Uncontrolled bleeding</strong> that pressure won&rsquo;t stop</li>
    <li><strong>Severe allergic reactions</strong> with throat swelling, difficulty swallowing, or hives with breathing changes</li>
    <li><strong>Severe abdominal pain,</strong> especially with rigidity, vomiting blood, or rectal bleeding</li>
    <li><strong>Suspected poisoning or overdose</strong></li>
    <li><strong>Suicidal ideation with plan or intent</strong></li>
</ul>

<p>When in doubt, call 911 or your physician. If you have to ask &ldquo;should I call 911?&rdquo;&mdash;call 911.</p>

<h2 id="when-urgent-care">3. When urgent care is appropriate</h2>

<p>Urgent care handles conditions that need attention today but aren&rsquo;t life-threatening:</p>

<ul>
    <li>Ear infections, sinus infections, strep throat</li>
    <li>Urinary tract infections (uncomplicated)</li>
    <li>Minor cuts requiring stitches (wound is controlled)</li>
    <li>Sprains and strains (when there&rsquo;s no obvious bone deformity)</li>
    <li>X-rays for suspected minor fractures (non-displaced)</li>
    <li>Flu symptoms, fever (adults without major comorbidities)</li>
    <li>Mild asthma flare (if you have rescue inhaler and are improving)</li>
    <li>Skin rashes, minor burns, insect bites</li>
    <li>STI testing, pregnancy tests</li>
    <li>COVID-19 testing and treatment</li>
</ul>

<div class="case-study">
    <h3>UTI: urgent care vs. ER cost comparison</h3>
    <p>A patient with classic UTI symptoms (frequency, burning, no fever, no back pain) went to the ER because it was late on a Sunday. Her bill: $2,340 facility fee + $280 physician fee = $2,620 before insurance. Her copay was $300. The same condition treated at an urgent care center down the street would have cost $140 total, with a $40 copay. <strong>Cost of going to the wrong setting: $260 in extra out-of-pocket and $2,480 in extra system cost.</strong></p>
</div>

<h2 id="freestanding-er">4. Freestanding ERs: the most expensive trap</h2>

<p>A freestanding emergency room (FSER) is a state-licensed emergency room that is not physically connected to a hospital. They are designed to look like urgent care centers&mdash;clean, fast, and easy to park at. But they charge hospital ER prices.</p>

<table>
    <thead>
        <tr><th>Feature</th><th>Hospital ER</th><th>Freestanding ER</th><th>Urgent Care</th></tr>
    </thead>
    <tbody>
        <tr><td>Facility fee</td><td>$1,500&ndash;$3,500+</td><td>$1,500&ndash;$3,500+</td><td>$0 (one bundled charge)</td></tr>
        <tr><td>E&M billing codes</td><td>99281&ndash;99285</td><td>99281&ndash;99285</td><td>99202&ndash;99215</td></tr>
        <tr><td>Physician bill separate</td><td>Usually yes</td><td>Usually yes</td><td>No</td></tr>
        <tr><td>Subject to EMTALA</td><td>Yes</td><td>Sometimes (state-dependent)</td><td>No</td></tr>
        <tr><td>In-network (typical)</td><td>Often yes</td><td>Often not</td><td>Varies</td></tr>
        <tr><td>Can treat life threats</td><td>Yes</td><td>Limited (must transfer)</td><td>No</td></tr>
    </tbody>
</table>

<p><strong>BillKarma finding: freestanding ER patients pay an average of $2,400 more</strong> than hospital-based ER patients for the same presenting conditions. Part of this is due to higher rates of out-of-network status at FSERs. Part is due to facility fees charged at ER rates for conditions that urgent care could have handled at a fraction of the cost.</p>

<p><strong>How to spot a freestanding ER:</strong> Look for the words &ldquo;Emergency Room,&rdquo; &ldquo;Emergency Center,&rdquo; or &ldquo;Emergency Care&rdquo; on the sign. &ldquo;Urgent Care,&rdquo; &ldquo;Clinic,&rdquo; or &ldquo;Walk-In Care&rdquo; indicates a lower-cost setting. If you&rsquo;re not sure, ask at the front desk: &ldquo;Are you a freestanding ER or an urgent care center?&rdquo; and &ldquo;Are you in-network with my insurance?&rdquo; before checking in.</p>

<h2 id="insurance-coverage">5. How insurance treats ER visits differently</h2>

<p>Your insurance plan likely applies different cost-sharing rules to ER visits than to other care:</p>

<ul>
    <li><strong>ER copay (not waived if not admitted):</strong> Most plans charge an ER copay of $150&ndash;$300. Some plans waive the ER copay if you&rsquo;re admitted to the hospital. If you visit the ER and are sent home, the copay usually applies in full.</li>
    <li><strong>&ldquo;True emergency&rdquo; requirements:</strong> Some plans have provisions to charge higher cost-sharing if they determine the ER visit wasn&rsquo;t a &ldquo;true emergency.&rdquo; This is legally complex&mdash;the Prudent Layperson Standard (adopted in most states and federal law) defines an emergency as a condition that a reasonable layperson would believe requires immediate attention. Insurers cannot retroactively penalize you for a good-faith ER visit that turned out to be minor.</li>
    <li><strong>Out-of-network ERs:</strong> Under the No Surprises Act, you cannot be charged more than in-network cost-sharing for emergency services at any ER, even if the hospital is out-of-network. This does not apply to freestanding ERs in all states.</li>
    <li><strong>Separate deductibles:</strong> Some plans (especially grandfathered plans and some HMOs) have a separate ER deductible in addition to the general deductible. Read your Summary of Benefits.</li>
</ul>

<h2 id="emtala">6. EMTALA: your right to emergency care</h2>

<p>The Emergency Medical Treatment and Labor Act (EMTALA), enacted in 1986, gives every person the right to:</p>

<ul>
    <li>A medical screening examination at any Medicare-participating hospital ER, regardless of ability to pay, insurance status, or immigration status</li>
    <li>Stabilizing treatment for any emergency medical condition identified in the screening</li>
    <li>Safe transfer to another facility, if needed, once stabilized</li>
</ul>

<p><strong>What EMTALA does not do:</strong> It does not forgive your bill. After the emergency is stabilized, the hospital can and will bill you. It does not apply to freestanding ERs in states that haven&rsquo;t extended EMTALA to them. It does not guarantee ongoing care beyond stabilization.</p>

<p>If you are turned away or denied a screening exam at a hospital ER, you can file an EMTALA complaint with the CMS regional office. Hospitals found in violation face significant fines and can lose Medicare participation.</p>

<h2 id="billing-codes">7. ER vs. urgent care billing codes</h2>

<p>The billing code used by the provider is the single most important determinant of how much you&rsquo;re charged. Here&rsquo;s how they differ:</p>

<table>
    <thead>
        <tr><th>Code</th><th>Setting</th><th>Acuity Level</th><th>Medicare Rate (Professional)</th></tr>
    </thead>
    <tbody>
        <tr><td>99281</td><td>ER</td><td>Minor (minimal evaluation)</td><td>~$26</td></tr>
        <tr><td>99282</td><td>ER</td><td>Low acuity</td><td>~$52</td></tr>
        <tr><td>99283</td><td>ER</td><td>Moderate acuity</td><td>~$101</td></tr>
        <tr><td>99284</td><td>ER</td><td>High acuity</td><td>~$174</td></tr>
        <tr><td>99285</td><td>ER</td><td>Highest acuity (usually with decision-making)</td><td>~$239</td></tr>
        <tr><td>99202&ndash;99203</td><td>Clinic / urgent care</td><td>Low complexity</td><td>~$73&ndash;$112</td></tr>
        <tr><td>99204&ndash;99205</td><td>Clinic / urgent care</td><td>Moderate-high complexity</td><td>~$153&ndash;$218</td></tr>
        <tr><td>99213&ndash;99215</td><td>Clinic / urgent care (established)</td><td>Low-high complexity</td><td>~$93&ndash;$208</td></tr>
    </tbody>
</table>

<p><strong>The facility fee is separate from these E&M codes.</strong> The E&M code captures the physician&rsquo;s professional work. The hospital charges a separate facility fee (its own E&M-equivalent scale: Level 1&ndash;5 for ERs) that typically costs far more than the physician fee. At urgent care, there is no separate facility fee&mdash;the clinic charges one bill that covers both the physician and the facility.</p>

<h2 id="surprise-billing">8. Surprise billing in the ER</h2>

<p>Even if your hospital is in-network, you may receive an out-of-network bill from the ER physician. This happens because hospitals contract with physician staffing companies (like Envision, TeamHealth) that negotiate their own contracts&mdash;sometimes separate from the hospital&rsquo;s insurance contracts.</p>

<p><strong>The No Surprises Act (effective 2022) protects you:</strong></p>

<ul>
    <li>For emergency services, you cannot be charged more than your in-network cost-sharing amount, even if the ER physician is out-of-network</li>
    <li>The OON provider and insurer must settle billing disputes through arbitration&mdash;you are not involved in or responsible for that dispute</li>
    <li>You must receive a notice (required by law) if any provider involved in your care is OON</li>
    <li>After the emergency is stabilized, you can consent to ongoing OON care&mdash;but the surprise billing protections only continue if you do not sign the OON consent form</li>
</ul>

<p><strong>If you receive a surprise bill from an ER physician:</strong> Do not pay it at the OON rate. Call your insurer and tell them you received an OON bill for emergency services. They must process it at in-network cost-sharing under the No Surprises Act. If they refuse, file a complaint at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener noreferrer">cms.gov/nosurprises</a>.</p>

<div class="cta-box">
    <h3>Got an ER bill that looks wrong?</h3>
    <p>ER bills are among the most error-prone in healthcare. Upload your itemized ER bill to BillKarma. We check for duplicate charges, upcoded E&M levels, unbundled lab and imaging charges, and No Surprises Act violations.</p>
    <a href="/fight-debt" class="cta-button">Audit My ER Bill &rarr;</a>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does an ER visit cost vs. urgent care?</h3>
        <p>ER visits cost $1,500&ndash;$3,500+ in facility fees alone, plus a separate physician bill. Urgent care averages $100&ndash;$200 total (one bill). After insurance, ER copays run $150&ndash;$300 vs. $25&ndash;$75 at urgent care. For non-emergency conditions, urgent care costs 5&ndash;15 times less.</p>
    </div>

    <div class="faq-item">
        <h3>What is a freestanding ER?</h3>
        <p>A freestanding ER is a state-licensed emergency room not connected to a hospital. It charges ER-level facility fees ($1,500&ndash;$3,500+) but often isn&rsquo;t in-network with major insurers. BillKarma finds freestanding ER patients pay an average of $2,400 more than hospital ER patients for identical conditions. Check the sign before entering and always confirm in-network status.</p>
    </div>

    <div class="faq-item">
        <h3>Can the ER bill me if I can&rsquo;t afford to pay?</h3>
        <p>Yes. EMTALA requires the ER to treat you regardless of ability to pay, but it does not forgive the bill. After treatment, apply for the hospital&rsquo;s financial assistance (charity care) program. Nonprofit hospitals are required to have these programs and must help patients who meet income thresholds. See our <a href="/guides/hospital-financial-assistance-charity-care/">financial assistance guide</a>.</p>
    </div>

    <div class="faq-item">
        <h3>Does the No Surprises Act protect me from OON ER bills?</h3>
        <p>Yes. For emergency services, you can only be charged in-network cost-sharing, even if the ER physician is OON. If you receive an OON bill for emergency care, call your insurer and report it. Do not pay at the OON rate. You can also file a complaint at cms.gov/nosurprises.</p>
    </div>

    <div class="faq-item">
        <h3>What is the cheapest option for non-emergency care?</h3>
        <p>Telehealth is typically cheapest at $10&ndash;$40 after insurance. Retail clinics (MinuteClinic, CVS Health, etc.) run $15&ndash;$40 copay and handle minor conditions quickly. Urgent care ($25&ndash;$75 copay) handles conditions requiring a physical exam, X-rays, or minor procedures. Save the ER for genuine emergencies.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener noreferrer">CMS: No Surprises Act &mdash; Patient Protections</a></li>
    <li><a href="https://www.cms.gov/Regulations-and-Guidance/Legislation/EMTALA" target="_blank" rel="noopener noreferrer">CMS: Emergency Medical Treatment &amp; Labor Act (EMTALA)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener noreferrer">CMS: Medicare Physician Fee Schedule (ER E&M codes 99281&ndash;99285)</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/cost-differences-in-freestanding-emergency-departments-vs-hospital-emergency-departments/" target="_blank" rel="noopener noreferrer">KFF: Cost Differences: Freestanding ERs vs. Hospital ERs</a></li>
    <li><a href="https://www.rand.org/pubs/research_reports/RRA1275-1.html" target="_blank" rel="noopener noreferrer">RAND: Freestanding Emergency Department Cost Analysis</a></li>
    <li><a href="https://www.hcup-us.ahrq.gov/" target="_blank" rel="noopener noreferrer">AHRQ HCUP: Emergency Department Utilization and Cost Data</a></li>
</ul>
""",
})
