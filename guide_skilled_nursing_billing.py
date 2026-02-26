"""Guide: Skilled Nursing Facility Billing: Costs, Medicare Coverage, and Appeals."""

from guides import register, _embed

register("skilled-nursing-facility-billing", {
    "title": "Skilled Nursing Facility Billing: Costs, Medicare Coverage, and Appeals",
    "meta_description": "Medicare covers up to 100 days in a skilled nursing facility, but coinsurance starts at day 21. Learn SNF costs, coverage rules, and how to appeal denials.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How many days does Medicare cover in a skilled nursing facility?",
            "a": "Medicare covers up to 100 days per benefit period in a skilled nursing facility. Days 1 through 20 are covered in full with no coinsurance. Days 21 through 100 require a daily coinsurance payment of $204.50 in 2026. After day 100, Medicare coverage ends entirely and you are responsible for the full daily rate, which averages $250 to $400 or more depending on location and facility type."
        },
        {
            "q": "What qualifies me for Medicare SNF coverage?",
            "a": "You must meet three requirements: a qualifying hospital stay of at least three consecutive inpatient days (observation status does not count), admission to a Medicare-certified SNF within 30 days of discharge, and a need for skilled nursing or therapy services that can only be provided in a SNF setting. Your doctor must certify that daily skilled care is medically necessary."
        },
        {
            "q": "What is the difference between skilled nursing care and custodial care?",
            "a": "Skilled nursing care requires the expertise of licensed professionals — wound care, IV therapy, physical therapy, injections, and complex medication management. Custodial care involves help with daily activities like bathing, dressing, eating, and transferring, and does not require licensed professionals. Medicare covers skilled nursing care but does not cover custodial care alone. Many SNF denials happen because Medicare determines the patient needs custodial care, not skilled care."
        },
        {
            "q": "Can I appeal a Medicare SNF coverage denial?",
            "a": "Yes. You have the right to appeal any Medicare coverage denial. Start by filing a redetermination with your Medicare Administrative Contractor within 120 days of the denial notice. If denied again, you can request a reconsideration by a Qualified Independent Contractor, then escalate to an Administrative Law Judge hearing if the amount in dispute exceeds $180. Most successful appeals include a detailed letter from the treating physician explaining why skilled care remains medically necessary."
        },
        {
            "q": "Does Medicaid cover skilled nursing facility costs?",
            "a": "Yes, but only after you have exhausted most of your personal assets. Medicaid is the largest payer of long-term nursing home care in the United States. To qualify, you must meet strict income and asset limits that vary by state — typically under $2,000 in countable assets for an individual. Medicaid covers the full daily SNF rate with no coinsurance, but the application process can take 45 to 90 days, and facilities may have limited Medicaid beds."
        },
    ],
    "body": f"""
<p class="lead">A skilled nursing facility stay after a hospital discharge is one of the most expensive healthcare events most families will face. Medicare covers up to 100 days per benefit period, but <strong>coinsurance of $204.50 per day kicks in at day 21</strong> — meaning a full 100-day stay can cost a Medicare patient over <strong>$16,000 in coinsurance alone</strong>. After day 100, private-pay rates of $250 to $400 per day take over entirely. Understanding the coverage timeline, knowing when to appeal, and exploring financial assistance options can save families tens of thousands of dollars.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#medicare-coverage">Medicare SNF coverage: the 100-day rule explained</a></li>
        <li><a href="#qualifying">How to qualify for Medicare SNF coverage</a></li>
        <li><a href="#costs">SNF costs: what you will actually pay</a></li>
        <li><a href="#common-denials">Common reasons for SNF coverage denials</a></li>
        <li><a href="#appeals">How to appeal a Medicare SNF denial</a></li>
        <li><a href="#medicaid">Medicaid as a last resort for long-term care</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="medicare-coverage">1. Medicare SNF coverage: the 100-day rule explained</h2>

<p>Medicare Part A covers skilled nursing facility care in a tiered structure. The cost to the patient changes dramatically depending on how long the stay lasts. Here is the full breakdown for 2026:</p>

<table>
    <thead>
        <tr>
            <th>Days of Stay</th>
            <th>Medicare Pays</th>
            <th>You Pay</th>
            <th>Total Patient Cost (Cumulative)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Days 1&ndash;20</strong></td>
            <td>100% of approved costs</td>
            <td>$0 per day</td>
            <td>$0</td>
        </tr>
        <tr>
            <td><strong>Days 21&ndash;100</strong></td>
            <td>All costs except coinsurance</td>
            <td>$204.50 per day (2026 rate)</td>
            <td>Up to $16,360</td>
        </tr>
        <tr>
            <td><strong>Days 101+</strong></td>
            <td>$0 &mdash; coverage ends</td>
            <td>Full daily rate ($250&ndash;$400+)</td>
            <td>$250&ndash;$400+ per day, no cap</td>
        </tr>
    </tbody>
</table>

<p>A <strong>benefit period</strong> begins the day you are admitted as an inpatient to a hospital and ends when you have been out of a hospital or SNF for 60 consecutive days. If you are readmitted after 60 days, a new benefit period begins and the 100-day clock resets. This matters because patients who cycle between hospital and SNF within the same benefit period continue using their existing 100 days rather than starting over.</p>

<div class="key-takeaway">
    <strong>Key point:</strong> The three-day hospital stay requirement means observation status does not count. If your hospital stay was classified as observation rather than inpatient, Medicare will deny your SNF coverage entirely. See our <a href="/guides/observation-status">observation status guide</a> for how to check and appeal your status. If you already have a SNF bill in hand, <a href="/scan">upload it to BillKarma</a> — we will flag coverage issues, coinsurance miscalculations, and line-item errors in minutes.
</div>

<h2 id="qualifying">2. How to qualify for Medicare SNF coverage</h2>

<p>Medicare sets three requirements for SNF coverage, and all three must be met:</p>

<ol>
    <li><strong>A qualifying three-day inpatient hospital stay.</strong> You must spend at least three consecutive calendar days as an admitted inpatient (not counting the discharge day). Observation hours do not count toward this requirement, even if you spent multiple nights in the hospital. This is the single most common reason for SNF coverage denials.</li>
    <li><strong>SNF admission within 30 days of hospital discharge.</strong> You must enter the SNF within 30 days of leaving the hospital. If the gap exceeds 30 days, Medicare will not cover the SNF stay unless you have another qualifying hospital admission in between.</li>
    <li><strong>Medical necessity for daily skilled care.</strong> A physician must certify that you need skilled nursing services or skilled rehabilitation therapy (physical therapy, occupational therapy, or speech therapy) on a daily basis that can only be provided in a SNF setting. Custodial care alone — help with bathing, dressing, eating — does not qualify.</li>
</ol>

<p>The skilled care requirement is where most disputes arise. Medicare defines "skilled" as care that requires the training and judgment of a licensed nurse or therapist. Examples include wound care for a surgical incision, IV antibiotic therapy, physical therapy after a joint replacement, and insulin management for a newly diagnosed diabetic. If your care could be performed by an unlicensed caregiver, Medicare considers it custodial and will not cover the SNF stay.</p>

{_embed(mode="cost", cpt="99304", title="SNF Initial Care Visit", subtitle="See what Medicare pays for a skilled nursing facility evaluation.")}

<h2 id="costs">3. SNF costs: what you will actually pay</h2>

<p>The total cost of a SNF stay depends on how long you are there, whether Medicare is covering it, and what region you are in. Here are the realistic numbers:</p>

<table>
    <thead>
        <tr>
            <th>Scenario</th>
            <th>Daily Cost</th>
            <th>30-Day Cost</th>
            <th>90-Day Cost</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Medicare days 1&ndash;20</td>
            <td>$0</td>
            <td>$0 (for 20 days)</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td>Medicare days 21&ndash;100 (coinsurance)</td>
            <td>$204.50</td>
            <td>$6,135</td>
            <td>$14,315 (days 21&ndash;90)</td>
        </tr>
        <tr>
            <td>Private pay (no Medicare)</td>
            <td>$250&ndash;$400+</td>
            <td>$7,500&ndash;$12,000</td>
            <td>$22,500&ndash;$36,000</td>
        </tr>
        <tr>
            <td>Medicaid (if eligible)</td>
            <td>$0 (Medicaid rate)</td>
            <td>$0</td>
            <td>$0</td>
        </tr>
    </tbody>
</table>

<p>For a typical Medicare patient who stays the full 100 days: the first 20 days cost nothing, and days 21 through 100 cost $204.50 per day &times; 80 days = <strong>$16,360 in total coinsurance</strong>. If you have a Medigap policy (Medicare Supplement Insurance), many plans cover some or all of the day 21&ndash;100 coinsurance. Medigap Plan C, Plan F, and Plan G all cover the full SNF coinsurance. Check your Medigap plan benefits before assuming you will owe the full amount. You can <a href="/calculator">look up Medicare rates</a> for specific SNF services to verify the charges on your statement.</p>

<p>Private-pay rates vary significantly by state. The national median for a semi-private room is approximately $290 per day ($8,700 per month), while a private room averages $330 per day ($9,900 per month). In high-cost areas like the Northeast and West Coast, rates can exceed $400 per day. You can <a href="/hospitals/">check your facility's billing grade</a> in our hospital directory to see how their charges compare to regional averages.</p>

<h2 id="common-denials">4. Common reasons for SNF coverage denials</h2>

<p>Medicare denies SNF coverage more often than many patients expect. According to the HHS Office of Inspector General, Medicare Advantage plans denied approximately 13% of prior authorization requests for SNF admissions in recent years — and many of those denials were later overturned on appeal. The most common denial reasons are:</p>

<ul>
    <li><strong>No qualifying three-day inpatient stay.</strong> The patient was on observation status, or the inpatient stay was fewer than three full days. This is the most frequent and most frustrating denial because it is often discovered only after the SNF admission.</li>
    <li><strong>Care deemed custodial, not skilled.</strong> Medicare determined that the patient needs assistance with daily activities but does not require licensed nursing or therapy services on a daily basis. This denial often comes after an initial period of coverage when Medicare decides the patient has "plateaued" in rehabilitation.</li>
    <li><strong>Patient not making progress.</strong> For rehabilitation therapy (PT, OT, speech), Medicare may deny coverage if it determines the patient is no longer making measurable functional improvement. However, the Jimmo v. Sebelius settlement clarified that Medicare cannot deny coverage solely because a patient is not improving — maintenance therapy to prevent decline can also qualify as skilled care.</li>
    <li><strong>Prior authorization denied (Medicare Advantage).</strong> Medicare Advantage plans can require prior authorization for SNF stays, and denials are common. Original Medicare (Parts A and B) does not require prior authorization for SNF care.</li>
</ul>

<div class="key-takeaway">
    <strong>Important:</strong> If your SNF coverage is denied while you are still in the facility, the SNF must give you an Advance Beneficiary Notice (ABN) before charging you privately. Do not sign the ABN without understanding that it means you are agreeing to pay out of pocket. You have the right to appeal the denial before accepting private-pay responsibility. For step-by-step appeal instructions, see our <a href="/guides/how-to-appeal-a-medical-bill-denial">appeal guide</a>.
</div>

<h2 id="appeals">5. How to appeal a Medicare SNF denial</h2>

<p>Medicare SNF denials are among the most successfully appealed decisions in the Medicare system. The key is to act quickly and provide strong medical documentation.</p>

<ol>
    <li><strong>Level 1 — Redetermination.</strong> File with your Medicare Administrative Contractor (MAC) within 120 days of the denial notice. Include a detailed letter from the treating physician explaining exactly what skilled services are needed and why they can only be provided in a SNF. Success rate at this level: approximately 30&ndash;40%.</li>
    <li><strong>Level 2 — Reconsideration.</strong> If the redetermination is denied, request a reconsideration by a Qualified Independent Contractor (QIC) within 180 days. The QIC is an independent organization, not the same entity that made the initial decision. Provide any additional medical records or physician statements.</li>
    <li><strong>Level 3 — Administrative Law Judge (ALJ) hearing.</strong> If the amount in dispute exceeds $180 (2026 threshold), you can request a hearing before an ALJ within 60 days. This is where many patients win — ALJs overturn SNF denials at rates estimated above 50% in some analyses because they review the full medical record in context.</li>
    <li><strong>Level 4 — Medicare Appeals Council.</strong> If the ALJ rules against you, request review by the Medicare Appeals Council within 60 days.</li>
    <li><strong>Level 5 — Federal court.</strong> For amounts exceeding $1,840 (2026), you can file in federal district court within 60 days of the Council decision.</li>
</ol>

<p><strong>While the appeal is pending:</strong> If you file a timely appeal (before the SNF stops providing services), Medicare may be required to continue coverage during the appeal process. Ask the SNF about continuing coverage pending appeal — this is your right under the expedited review process if your care is being terminated.</p>

<div class="case-study">
    <h3>Case study: 82-year-old denied at day 22 — appeal recovers $14,500</h3>
    <p>An 82-year-old patient in Pennsylvania was admitted to a SNF after hip replacement surgery. Medicare covered days 1 through 22, then denied continued coverage, stating the patient no longer required skilled rehabilitation. The denial came from a Medicare Advantage plan via prior authorization review. The patient's physical therapist documented that the patient could not walk independently, could not transfer from bed to wheelchair without assistance, and was at high risk for falls. The family filed a Level 1 appeal with a letter from the orthopedic surgeon and the PT's functional assessment. The appeal was denied. At Level 2 reconsideration, they submitted video documentation of the patient's mobility limitations and updated progress notes showing incremental but measurable improvement in walking distance (from 10 feet to 45 feet over 14 days). The QIC overturned the denial and authorized coverage through day 85. <strong>Total coinsurance saved: $12,800. Total private-pay charges avoided: $14,500.</strong></p>
    <p>If you are facing a similar situation, <a href="/scan">scan your SNF bill with BillKarma</a> to identify line-item errors or overcharges before starting the appeal process.</p>
</div>

<h2 id="medicaid">6. Medicaid as a last resort for long-term care</h2>

<p>When Medicare coverage runs out after 100 days and the patient still needs SNF care, Medicaid becomes the primary payer for those who qualify. Medicaid is the largest payer of long-term nursing home care in the United States, covering approximately 62% of all nursing home residents.</p>

<p>Medicaid eligibility for long-term care requires meeting strict financial thresholds that vary by state but generally include:</p>

<ul>
    <li><strong>Income limit:</strong> Typically under $2,829 per month for an individual (2026, varies by state). Some states use a "medically needy" pathway that allows higher-income individuals to "spend down" to the limit.</li>
    <li><strong>Asset limit:</strong> Typically $2,000 in countable assets for an individual. Your home (up to a certain equity value), one vehicle, personal belongings, and a small amount of life insurance are generally exempt.</li>
    <li><strong>Spousal protections:</strong> If one spouse needs nursing home care, the community spouse (the one still living at home) can keep a portion of the couple's assets — the Community Spouse Resource Allowance, which ranges from approximately $30,000 to $154,000 depending on the state.</li>
</ul>

<p>Medicaid has a <strong>five-year lookback period</strong> for asset transfers. If you gave away assets within five years of applying for Medicaid, those transfers can trigger a penalty period during which Medicaid will not pay for your care. This is why families should consult an elder law attorney well before a nursing home admission is imminent. Many nonprofit SNFs also offer <a href="/guides/hospital-financial-assistance-guide">financial assistance programs</a> separate from Medicaid — check your facility's charity care policy before assuming you must pay the full private rate.</p>

<p><strong>The application process</strong> typically takes 45 to 90 days. During the gap between Medicare coverage ending and Medicaid approval, the SNF may require private pay. Many facilities will accept a "Medicaid pending" status, meaning they will bill Medicaid retroactively once the application is approved. However, not all facilities accept Medicaid patients, and Medicaid beds may be limited. Before choosing a SNF, check whether the facility accepts Medicaid and review its billing practices in our <a href="/hospitals/">hospital directory</a>.</p>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Observation status blocks SNF coverage — family pays $9,600 out of pocket</h3>
    <p>A 76-year-old woman in Ohio was hospitalized for three nights after a fall that fractured her wrist and aggravated a chronic back condition. She was discharged to a SNF for rehabilitation. After 8 days, the SNF informed the family that Medicare had denied coverage because the hospital stay was classified as observation status — not inpatient admission. Despite spending three nights in the hospital, the observation classification meant she had zero qualifying inpatient days. The family was billed $320 per day for the 8 days already spent in the SNF ($2,560) plus the remaining 22 days of rehabilitation at the same rate ($7,040). <strong>Total private-pay cost: $9,600</strong> for care that would have been fully covered under Medicare if the hospital had classified the stay as inpatient. <a href="/scan">Upload your SNF or hospital bill to BillKarma</a> to catch observation status issues and other coverage problems early.</p>
</div>

<div class="case-study">
    <h3>Medigap policy covers $16,360 in SNF coinsurance</h3>
    <p>A 79-year-old man in Florida was admitted to a SNF after knee replacement surgery. His Medicare coverage was approved for the full 100 days. Without supplemental insurance, his coinsurance for days 21 through 100 would have been $204.50 &times; 80 = $16,360. Because he had a Medigap Plan G policy (monthly premium: $185), the plan covered the entire SNF coinsurance amount. His total out-of-pocket cost for 100 days of skilled nursing care: <strong>$0 beyond his Medigap premium</strong>. The annual cost of his Medigap policy ($2,220) was less than one-seventh of the coinsurance it covered.</p>
</div>

<h2 id="faq">8. Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How many days does Medicare cover in a skilled nursing facility?</h3>
        <p>Medicare covers up to 100 days per benefit period. Days 1 through 20 are fully covered. Days 21 through 100 require a daily coinsurance of $204.50 (2026). After day 100, Medicare pays nothing. A benefit period resets after you have been out of a hospital or SNF for 60 consecutive days.</p>
    </div>

    <div class="faq-item">
        <h3>What qualifies me for Medicare SNF coverage?</h3>
        <p>You need three things: a qualifying three-day inpatient hospital stay (observation status does not count), admission to a Medicare-certified SNF within 30 days of discharge, and a physician certification that you need daily skilled nursing or therapy services. See our <a href="/guides/observation-status">observation status guide</a> to verify your hospital stay classification.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between skilled nursing care and custodial care?</h3>
        <p>Skilled care requires licensed professionals — wound care, IV therapy, physical therapy, medication management. Custodial care is help with daily activities like bathing and dressing. Medicare covers skilled care but not custodial care alone. Many denials hinge on this distinction, especially after initial improvement when Medicare may classify ongoing needs as custodial.</p>
    </div>

    <div class="faq-item">
        <h3>Can I appeal a Medicare SNF coverage denial?</h3>
        <p>Yes, and you should. SNF denials are among the most successfully appealed Medicare decisions. File a Level 1 redetermination within 120 days, then escalate to reconsideration and an ALJ hearing if needed. Include detailed physician documentation of why skilled care remains necessary. Our <a href="/guides/how-to-appeal-a-medical-bill-denial">appeal guide</a> walks through each level.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicaid cover skilled nursing facility costs?</h3>
        <p>Yes, for those who qualify financially. Medicaid is the largest payer of long-term nursing home care in the US. Eligibility requires meeting strict income and asset limits (typically under $2,000 in assets for an individual). Medicaid covers the full daily rate with no coinsurance but has a five-year lookback period for asset transfers. If you do not qualify for Medicaid, you may still be able to <a href="/guides/how-to-negotiate-a-medical-bill">negotiate the private-pay rate</a> directly with the facility.</p>
    </div>
</div>

<h2 id="sources">9. Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">CMS: Medicare Skilled Nursing Facility Coverage &mdash; Benefit Period Rules and Coinsurance Rates (2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">HHS Office of Inspector General: Medicare Advantage Prior Authorization Denials for Skilled Nursing Facility Care</a></li>
    <li><a href="#" target="_blank" rel="noopener">MedPAC: March 2025 Report to Congress &mdash; Skilled Nursing Facility Services, Chapter 8</a></li>
    <li><a href="#" target="_blank" rel="noopener">KFF: Medicaid&rsquo;s Role in Nursing Home Care &mdash; Coverage, Spending, and Eligibility</a></li>
    <li><a href="#" target="_blank" rel="noopener">Jimmo v. Sebelius Settlement: CMS Clarification on Skilled Care Coverage Standards</a></li>
    <li><a href="#" target="_blank" rel="noopener">Genworth Financial: Cost of Care Survey &mdash; 2025 Median Nursing Home Costs by State</a></li>
</ul>
""",
})
