"""Guide: Physical Therapy Cost Per Session."""

from guides import register, _embed

register("physical-therapy-cost-per-session", {
    "title": "Physical Therapy Cost Per Session in 2026 (With & Without Insurance)",
    "meta_description": "Physical therapy costs $75–$350/session without insurance. With insurance, most patients pay a $20–$75 copay. See PT billing codes, visit limits, and how to spot billing errors.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does physical therapy cost per session without insurance?",
            "a": "Without insurance, a physical therapy session typically costs $75–$350 depending on session type and location. An initial evaluation runs higher ($150–$300) because it includes assessment, diagnosis, and treatment planning. Follow-up sessions average $100–$200. Telehealth PT is often cheaper at $50–$150. Clinic location matters too—urban PT clinics charge 30–50% more than suburban or rural practices.",
        },
        {
            "q": "How much does physical therapy cost with insurance?",
            "a": "With insurance, most patients pay a $20–$75 copay per session after meeting their deductible. If you haven't met your deductible, you'll pay the full contracted rate (usually $80–$180) until you do. Once your deductible is met, you pay coinsurance (typically 20%) or your flat copay. Many plans cap PT visits at 30–60 per year, so tracking your usage matters.",
        },
        {
            "q": "Does Medicare cover physical therapy?",
            "a": "Yes. Medicare Part B covers outpatient physical therapy when it's medically necessary and provided by a licensed PT. After meeting the Part B deductible ($257 in 2026), Medicare pays 80% and you pay 20%. There's no hard annual visit cap under Original Medicare, but the 'functional improvement standard' applies—coverage continues as long as you're making measurable progress. A Medigap supplement can cover your 20% coinsurance.",
        },
        {
            "q": "How many PT sessions will I need?",
            "a": "It depends on the diagnosis. An acute soft-tissue injury (sprain, strain) typically resolves in 6–12 sessions over 4–6 weeks. Post-surgical rehab requires significantly more: knee replacement patients average 20–30 sessions, rotator cuff repair 24–36 sessions, and ACL reconstruction 30–40 sessions over 4–6 months. Your PT will set functional goals and track progress to justify continued sessions to your insurer.",
        },
        {
            "q": "What are common physical therapy billing errors?",
            "a": "The most common PT billing error is time unit manipulation—billing for more 15-minute therapy units than were actually delivered. Regulations require at least 8 minutes of direct contact to bill one unit. Other errors include billing for a licensed PT when an aide provided the service, duplicate charges for the same modality in one session, upcoding an evaluation level (97162 vs 97161), and billing for services on dates the patient wasn't present. BillKarma finds PT billing errors in 28% of claims.",
        },
    ],
    "body": f"""
<p class="lead">Physical therapy costs <strong>$75&ndash;$350 per session</strong> without insurance. With insurance, most patients pay a <strong>$20&ndash;$75 copay</strong> per visit. But PT bills are riddled with errors&mdash;BillKarma finds billing mistakes in 28% of PT claims, most involving manipulated time units. Here&rsquo;s what PT actually costs, what insurance covers, and how to protect yourself.</p>

<div class="answer-box">
    <strong>Quick answer:</strong> A standard follow-up PT session costs $100&ndash;$200 without insurance, or a $20&ndash;$75 insurance copay. Your initial evaluation runs higher ($150&ndash;$300). Medicare Part B covers PT at 80% after your deductible. Most private plans cap visits at 30&ndash;60/year. Time unit fraud is the #1 PT billing error&mdash;always request an itemized bill.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-breakdown">Cost breakdown: initial eval vs. follow-up sessions</a></li>
        <li><a href="#with-without-insurance">Cost with vs. without insurance</a></li>
        <li><a href="#medicare-coverage">Medicare Part B coverage for PT</a></li>
        <li><a href="#session-count">How many sessions will you need?</a></li>
        <li><a href="#settings">Home vs. clinic vs. telehealth PT</a></li>
        <li><a href="#billing-codes">PT billing codes explained</a></li>
        <li><a href="#billing-errors">Common PT billing errors</a></li>
        <li><a href="#find-pt">How to find in-network PT and OON reimbursement</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-breakdown">1. Cost breakdown: initial eval vs. follow-up sessions</h2>

<p>Your first PT appointment (the initial evaluation) costs more than follow-up sessions. The PT must assess your condition, review medical history, perform functional testing, and create a treatment plan. After that, follow-up visits are shorter and more focused.</p>

<table>
    <thead>
        <tr><th>Visit Type</th><th>CPT Code</th><th>Without Insurance</th><th>Medicare Rate</th></tr>
    </thead>
    <tbody>
        <tr><td>Initial evaluation (low complexity)</td><td>97161</td><td>$100&ndash;$175</td><td>~$87</td></tr>
        <tr><td>Initial evaluation (moderate complexity)</td><td>97162</td><td>$125&ndash;$225</td><td>~$111</td></tr>
        <tr><td>Initial evaluation (high complexity)</td><td>97163</td><td>$150&ndash;$300</td><td>~$134</td></tr>
        <tr><td>Follow-up / re-evaluation</td><td>97164</td><td>$75&ndash;$150</td><td>~$63</td></tr>
        <tr><td>Therapeutic exercise (per 15-min unit)</td><td>97110</td><td>$30&ndash;$80/unit</td><td>~$32</td></tr>
        <tr><td>Manual therapy (per 15-min unit)</td><td>97140</td><td>$35&ndash;$85/unit</td><td>~$31</td></tr>
        <tr><td>Neuromuscular re-education (per unit)</td><td>97112</td><td>$30&ndash;$75/unit</td><td>~$33</td></tr>
        <tr><td>Ultrasound therapy</td><td>97035</td><td>$25&ndash;$60</td><td>~$16</td></tr>
    </tbody>
</table>

<p>A typical 60-minute follow-up session bills 3&ndash;4 units of timed codes (97110, 97140, etc.) plus any modalities. At Medicare rates, a session might total $120&ndash;$160. At a private clinic&rsquo;s cash rate, the same session could be $160&ndash;$250.</p>

{_embed(mode="cost", cpt="97110", title="Look Up PT Billing Code Rates", subtitle="See what Medicare pays for therapeutic exercise (97110) and other PT codes in your area.")}

<h2 id="with-without-insurance">2. Cost with vs. without insurance</h2>

<table>
    <thead>
        <tr><th>Coverage Scenario</th><th>Per-Session Cost</th><th>Annual Cost (20 sessions)</th></tr>
    </thead>
    <tbody>
        <tr><td>Employer insurance (copay model)</td><td>$20&ndash;$75 copay</td><td>$400&ndash;$1,500</td></tr>
        <tr><td>Employer insurance (coinsurance, deductible met)</td><td>20% of ~$150 = ~$30</td><td>~$600</td></tr>
        <tr><td>Employer insurance (deductible not met)</td><td>$80&ndash;$180 full contracted rate</td><td>$1,600&ndash;$3,600</td></tr>
        <tr><td>Medicare Part B (after deductible)</td><td>20% of Medicare rate (~$25&ndash;$40)</td><td>$500&ndash;$800</td></tr>
        <tr><td>Medicare + Medigap supplement</td><td>$0 after deductible</td><td>$0 (deductible applies)</td></tr>
        <tr><td>Uninsured (cash pay rate)</td><td>$75&ndash;$200</td><td>$1,500&ndash;$4,000</td></tr>
        <tr><td>Telehealth PT (uninsured)</td><td>$50&ndash;$150</td><td>$1,000&ndash;$3,000</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Check your visit limit before you start.</strong> Most employer plans cap PT at 30&ndash;60 visits per year. If you&rsquo;re recovering from surgery and need 30&ndash;40 sessions, you could exhaust your benefit mid-recovery. Ask your insurer about limits before your first appointment and plan accordingly.
</div>

<h2 id="medicare-coverage">3. Medicare Part B coverage for PT</h2>

<p>Medicare Part B covers outpatient PT when all of these are true:</p>

<ul>
    <li>Services are medically necessary (not just maintenance)</li>
    <li>Your PT is a Medicare-enrolled provider</li>
    <li>You are making functional progress toward measurable goals</li>
    <li>A physician certifies the plan of care</li>
</ul>

<p><strong>The functional improvement standard</strong> is critical. Medicare requires documentation that you&rsquo;re progressing&mdash;not just maintaining your current function. If your PT isn&rsquo;t documenting measurable goals and outcomes, your claims may be denied mid-course.</p>

<table>
    <thead>
        <tr><th>What Medicare Covers</th><th>Your Cost</th></tr>
    </thead>
    <tbody>
        <tr><td>Outpatient PT (after Part B deductible)</td><td>20% coinsurance (~$25&ndash;$40/session)</td></tr>
        <tr><td>Home health PT (if homebound)</td><td>$0 (Part A / Home Health benefit)</td></tr>
        <tr><td>Inpatient rehab facility PT</td><td>Part A deductible, then $0 for days 1&ndash;20</td></tr>
    </tbody>
</table>

<p><strong>Common diagnoses covered by Medicare PT:</strong> joint replacement recovery, stroke rehabilitation, fracture recovery, back pain (when conservative treatment is indicated), balance disorders, post-surgical rehab, COPD (pulmonary rehab), and neurological conditions including Parkinson&rsquo;s disease.</p>

<p><strong>Prior authorization:</strong> Original Medicare does not require prior auth for outpatient PT. Medicare Advantage plans often do&mdash;check before your first appointment.</p>

<h2 id="session-count">4. How many sessions will you need?</h2>

<table>
    <thead>
        <tr><th>Condition</th><th>Typical Session Count</th><th>Duration</th></tr>
    </thead>
    <tbody>
        <tr><td>Acute soft-tissue injury (sprain/strain)</td><td>6&ndash;12 sessions</td><td>3&ndash;6 weeks</td></tr>
        <tr><td>Low back pain (acute episode)</td><td>8&ndash;16 sessions</td><td>4&ndash;8 weeks</td></tr>
        <tr><td>Shoulder impingement / rotator cuff strain</td><td>12&ndash;20 sessions</td><td>6&ndash;10 weeks</td></tr>
        <tr><td>Total knee replacement (post-op)</td><td>20&ndash;30 sessions</td><td>8&ndash;12 weeks</td></tr>
        <tr><td>ACL reconstruction (post-op)</td><td>30&ndash;40 sessions</td><td>4&ndash;6 months</td></tr>
        <tr><td>Rotator cuff repair (post-op)</td><td>24&ndash;36 sessions</td><td>3&ndash;5 months</td></tr>
        <tr><td>Stroke rehabilitation</td><td>Ongoing (30&ndash;60+ sessions)</td><td>3&ndash;12 months</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Session count affects your total cost significantly.</strong> If your plan has a 30-visit cap and your ACL recovery needs 35 sessions, you&rsquo;ll pay out of pocket for the last 5 visits. Ask your surgeon and PT for a realistic session estimate before surgery so you can plan financially.
</div>

<h2 id="settings">5. Home vs. clinic vs. telehealth PT</h2>

<p>Physical therapy is delivered in several settings, each with different costs and coverage rules:</p>

<ul>
    <li><strong>Outpatient clinic:</strong> The most common setting. Fully equipped gym, hands-on manual therapy, specialized equipment. Costs $100&ndash;$350/session without insurance. Most insurance applies here.</li>
    <li><strong>Home health PT:</strong> A PT comes to your home. Covered by Medicare when you&rsquo;re &ldquo;homebound&rdquo; (substantial effort to leave home). Post-surgical patients often qualify immediately after discharge. No cost-sharing under Original Medicare Part A.</li>
    <li><strong>Telehealth PT:</strong> Video-based PT for exercises, education, and monitoring. Costs $50&ndash;$150/session. Excellent for maintaining gains after in-person care ends. Coverage varies&mdash;most major insurers cover it, but not all plans do at the same rate as in-person.</li>
    <li><strong>Hospital outpatient PT department:</strong> Higher cost than independent clinic (facility fee applies). Expect 30&ndash;50% more per session. Use only when your condition requires hospital-level equipment or supervision.</li>
</ul>

<h2 id="billing-codes">6. PT billing codes explained</h2>

<p>PT sessions are billed using timed codes (per 15-minute unit) and untimed codes (flat fee per service). Understanding these helps you read your EOB and spot errors.</p>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Service</th><th>Type</th><th>Medicare Rate</th></tr>
    </thead>
    <tbody>
        <tr><td>97110</td><td>Therapeutic exercise</td><td>Timed (per 15 min)</td><td>~$32</td></tr>
        <tr><td>97140</td><td>Manual therapy techniques</td><td>Timed (per 15 min)</td><td>~$31</td></tr>
        <tr><td>97112</td><td>Neuromuscular re-education</td><td>Timed (per 15 min)</td><td>~$33</td></tr>
        <tr><td>97530</td><td>Therapeutic activities</td><td>Timed (per 15 min)</td><td>~$34</td></tr>
        <tr><td>97035</td><td>Ultrasound therapy</td><td>Timed (per 15 min)</td><td>~$16</td></tr>
        <tr><td>97012</td><td>Mechanical traction</td><td>Untimed</td><td>~$17</td></tr>
        <tr><td>97032</td><td>Electrical stimulation (manual)</td><td>Timed (per 15 min)</td><td>~$18</td></tr>
        <tr><td>97033</td><td>Iontophoresis</td><td>Timed (per 15 min)</td><td>~$25</td></tr>
        <tr><td>97018</td><td>Paraffin bath</td><td>Untimed</td><td>~$10</td></tr>
    </tbody>
</table>

<p>A 60-minute session might include 2 units of 97110, 1 unit of 97140, and 1 unit of 97530 (4 units total). Medicare&rsquo;s 8-minute rule means each unit requires at least 8 minutes of direct contact. A PT cannot bill 4 units from a 30-minute session.</p>

<h2 id="billing-errors">7. Common PT billing errors</h2>

<p>BillKarma finds billing errors in <strong>28% of physical therapy claims</strong>. Time unit manipulation is the most common, but there are several others to watch for:</p>

<ul>
    <li><strong>Time unit manipulation:</strong> Billing 4 units (60 minutes of timed therapy) when only 45 minutes were provided. Each unit requires 8+ minutes. A 45-minute session can only bill 3 units by CMS rules&mdash;not 4.</li>
    <li><strong>Upcoding the evaluation:</strong> Billing a high-complexity evaluation (97163) when the patient&rsquo;s condition warranted only a low or moderate complexity code (97161 or 97162).</li>
    <li><strong>Billing for aide-provided services as PT services:</strong> A PT aide or tech cannot bill under the PT&rsquo;s license. Only licensed PTs and PTAs under PT supervision can bill licensed PT codes.</li>
    <li><strong>Duplicate modality billing:</strong> Billing both 97032 (electrical stim, manual) and 97014 (electrical stim, unattended) for the same session on the same body area.</li>
    <li><strong>Services not provided:</strong> Billing for ultrasound, traction, or other modalities that were not documented or performed.</li>
    <li><strong>Wrong date of service:</strong> Billing on a day the patient was not seen (common in high-volume clinics).</li>
</ul>

<div class="case-study">
    <h3>$1,200 PT overcharge caught with an itemized bill</h3>
    <p>A patient recovering from a rotator cuff repair received a PT bill for 24 sessions. After requesting an itemized statement with CPT codes, she found that 18 of 24 sessions billed 4 timed units, but her appointment records confirmed sessions were 45 minutes&mdash;not 60. At 4 units each, the clinic had overbilled by roughly 1 unit per session. After disputing with the billing office and her insurer, <strong>$1,200 was credited back</strong> to her account.</p>
</div>

<div class="cta-box">
    <h3>Is your PT bill accurate?</h3>
    <p>Upload your physical therapy EOB or itemized bill to BillKarma. We check every timed code unit against your session length, flag evaluation upcoding, and identify duplicate charges automatically.</p>
    <a href="/fight-debt" class="cta-button">Audit My PT Bill &rarr;</a>
</div>

<h2 id="find-pt">8. How to find in-network PT and OON reimbursement</h2>

<p><strong>Finding in-network PT:</strong> Use your insurer&rsquo;s online provider directory, filtering by specialty "Physical Therapy" in your zip code. Call the clinic before your first appointment to confirm they accept your specific plan&mdash;provider directories are often outdated. Confirm both the clinic and your specific PT are in-network (sometimes the facility is in-network but an individual PT is not).</p>

<p><strong>Out-of-network PT reimbursement:</strong> If you choose an OON PT (or your insurer has no in-network PTs in your area), most PPO plans reimburse 50&ndash;70% of the &ldquo;allowed amount&rdquo; after your OON deductible. HMO plans typically pay nothing OON except emergencies. If you&rsquo;re seeing an OON PT, request a superbill (itemized receipt with CPT codes and diagnosis codes) and submit it directly to your insurer for reimbursement.</p>

<p><strong>Prior authorization for PT:</strong> Many commercial plans require prior auth for PT, especially if requesting more than the initial approved sessions (commonly 6&ndash;10 sessions initially). Your PT&rsquo;s office typically handles prior auth, but confirm it&rsquo;s been approved before each new set of authorized visits to avoid unexpected bills.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does physical therapy cost per session without insurance?</h3>
        <p>$75&ndash;$350 depending on session type and location. Initial evaluations cost more ($150&ndash;$300). Telehealth PT costs $50&ndash;$150. Urban clinics are typically 30&ndash;50% more expensive than suburban or rural practices.</p>
    </div>

    <div class="faq-item">
        <h3>How much does physical therapy cost with insurance?</h3>
        <p>A $20&ndash;$75 copay per session for most plans. If your deductible isn&rsquo;t met, you&rsquo;ll pay the contracted rate ($80&ndash;$180). Most plans have annual visit caps (30&ndash;60 visits). Track your visits to avoid unexpected bills when you exceed your limit.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover physical therapy?</h3>
        <p>Yes. Medicare Part B covers outpatient PT at 80% after your Part B deductible ($257 in 2026). You pay 20% coinsurance (~$25&ndash;$40/session). There&rsquo;s no hard annual cap, but you must show functional improvement. Medigap supplements cover your 20% share.</p>
    </div>

    <div class="faq-item">
        <h3>How many PT sessions do I need after surgery?</h3>
        <p>Post-surgical PT varies: knee replacement needs 20&ndash;30 sessions, ACL reconstruction 30&ndash;40 sessions, rotator cuff repair 24&ndash;36 sessions. Your PT will set measurable goals and document progress to justify continued sessions to your insurer.</p>
    </div>

    <div class="faq-item">
        <h3>What is the most common PT billing fraud?</h3>
        <p>Time unit manipulation&mdash;billing more 15-minute units than were actually delivered. CMS requires at least 8 minutes of direct contact per unit. A 45-minute session can only bill 3 timed units, not 4. Always request an itemized bill and compare billed units to your actual session length.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener noreferrer">CMS: Medicare Physician Fee Schedule (PT CPT codes)</a></li>
    <li><a href="https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/bp102c15.pdf" target="_blank" rel="noopener noreferrer">CMS: Medicare Benefit Policy Manual &mdash; Chapter 15, Covered Medical and Other Health Services (PT)</a></li>
    <li><a href="https://www.apta.org/patient-care/public-health-population-care/physical-therapy-outcomes-registry" target="_blank" rel="noopener noreferrer">APTA: Physical Therapy Outcomes Registry</a></li>
    <li><a href="https://www.hhs.gov/opa/no-surprises/index.html" target="_blank" rel="noopener noreferrer">HHS: No Surprises Act &mdash; Good Faith Estimates</a></li>
    <li><a href="https://www.hcup-us.ahrq.gov/" target="_blank" rel="noopener noreferrer">AHRQ HCUP: Hospital Costs by Procedure</a></li>
</ul>
""",
})
