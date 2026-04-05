"""Guide: Hospice Billing: What Medicare Covers and What Families Actually Pay."""

from guides import register, _embed

register("hospice-billing", {
    "title": "Hospice Billing: What Medicare Covers",
    "meta_description": "Medicare hospice covers nearly all end-of-life care. Learn the 4 care levels, what is NOT covered, room and board rules, and how to spot billing errors.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "Does Medicare cover hospice care?",
            "a": "Yes. The Medicare Hospice Benefit (Part A) covers virtually all costs related to the terminal illness: nursing care, medications for pain and symptom management, medical equipment (hospital bed, wheelchair, oxygen), medical supplies, hospice aide and homemaker services, social work, chaplain services, grief counseling for the family, and short-term inpatient care. The patient pays nothing for these services except a small copay for outpatient drugs ($5 or 5% of the cost, whichever is less).",
        },
        {
            "q": "What does hospice NOT cover?",
            "a": "Hospice does not cover curative treatment for the terminal illness. If a patient elects hospice for cancer, for example, chemotherapy intended to cure the cancer is not covered (though palliative chemotherapy to relieve symptoms may be). Hospice also does not cover treatments for conditions unrelated to the terminal diagnosis, room and board at a nursing home (unless the patient is there for respite care or acute symptom management), or care from providers not arranged by the hospice team.",
        },
        {
            "q": "Can I revoke hospice and go back to regular Medicare?",
            "a": "Yes, at any time. A patient can revoke the hospice benefit in writing and return to standard Medicare coverage. This might happen if the patient decides to pursue curative treatment, or if their condition unexpectedly improves. Revocation takes effect on the date the patient signs the revocation statement. The patient can re-elect hospice later if they meet eligibility criteria again.",
        },
        {
            "q": "What are the 4 levels of hospice care?",
            "a": "Medicare defines four levels: (1) Routine Home Care, the standard level where care is provided at home; (2) Continuous Home Care, 8-24 hours of nursing care at home during a medical crisis; (3) Inpatient Respite Care, up to 5 days in a facility to give family caregivers a break; and (4) General Inpatient Care, short-term inpatient care at a hospital or hospice facility for acute symptom management that cannot be managed at home. Each level has a different daily reimbursement rate.",
        },
        {
            "q": "Who pays for room and board during hospice?",
            "a": "If the patient is at home, there is no room and board charge. If the patient is in a nursing home, Medicaid or the patient's own funds pay for room and board; hospice covers only the hospice-related care. If the patient is admitted to an inpatient hospice facility or hospital for acute symptom management (General Inpatient Care level), Medicare hospice covers the full cost including room and board. Respite care room and board is also covered by Medicare, with a 5% coinsurance to the patient.",
        },
    ],
    "body": f"""
<p class="lead">The Medicare Hospice Benefit covers over <strong>1.7 million Americans</strong> each year and pays for nearly all end-of-life care costs&mdash;yet <strong>1 in 5 hospice families report receiving unexpected bills</strong> for services that should have been covered. The most common errors involve medications, durable medical equipment, and charges for care related to the terminal illness that the hospice agency should have provided. Here is how hospice billing works, what Medicare actually pays, and how to protect your family from billing mistakes during an already difficult time.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#hospice-benefit">The Medicare Hospice Benefit explained</a></li>
        <li><a href="#four-levels">The 4 levels of hospice care and their costs</a></li>
        <li><a href="#what-is-not-covered">What hospice does NOT cover</a></li>
        <li><a href="#billing-errors">Common hospice billing errors</a></li>
        <li><a href="#room-and-board">Room and board: who pays what</a></li>
        <li><a href="#revocation">Revocation, recertification, and benefit periods</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="hospice-benefit">1. The Medicare Hospice Benefit explained</h2>

<p>When a patient elects the Medicare Hospice Benefit, they are choosing comfort-focused care instead of curative treatment for their terminal illness. Medicare Part A then covers virtually all costs related to the terminal condition. The patient&rsquo;s regular Medicare benefits continue for any conditions <strong>unrelated</strong> to the terminal diagnosis.</p>

<p>To qualify, the patient must:</p>

<ul>
    <li>Be eligible for Medicare Part A</li>
    <li>Have a terminal illness with a life expectancy of 6 months or less, as certified by the hospice medical director and the patient&rsquo;s attending physician</li>
    <li>Sign an election statement choosing hospice care and acknowledging the shift from curative to palliative goals</li>
</ul>

<p>What Medicare hospice covers:</p>

<table>
    <thead>
        <tr><th>Service</th><th>Covered?</th><th>Patient Cost</th></tr>
    </thead>
    <tbody>
        <tr><td>Nursing visits (RN and LPN)</td><td>Yes</td><td>$0</td></tr>
        <tr><td>Medications for pain and symptom management</td><td>Yes</td><td>$5 or 5% copay (whichever is less)</td></tr>
        <tr><td>Durable medical equipment (hospital bed, oxygen, wheelchair)</td><td>Yes</td><td>$0</td></tr>
        <tr><td>Medical supplies (wound care, catheters, etc.)</td><td>Yes</td><td>$0</td></tr>
        <tr><td>Hospice aide / homemaker services</td><td>Yes</td><td>$0</td></tr>
        <tr><td>Social worker visits</td><td>Yes</td><td>$0</td></tr>
        <tr><td>Chaplain / spiritual counseling</td><td>Yes</td><td>$0</td></tr>
        <tr><td>Bereavement counseling for family (13 months)</td><td>Yes</td><td>$0</td></tr>
        <tr><td>Short-term inpatient care (symptom management)</td><td>Yes</td><td>$0</td></tr>
        <tr><td>Respite care (up to 5 days)</td><td>Yes</td><td>5% of Medicare-approved rate (~$10/day)</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Key point:</strong> The hospice agency receives a daily payment from Medicare and is responsible for providing or arranging <strong>all</strong> care related to the terminal illness. If you receive a separate bill from a pharmacy, DME supplier, or outside provider for a service related to the terminal condition, that bill may be the hospice agency&rsquo;s responsibility&mdash;not yours. <a href="/scan">Upload the bill to BillKarma</a> to check whether the charge should have been covered under the hospice benefit.
</div>

<h2 id="four-levels">2. The 4 levels of hospice care and their costs</h2>

<p>Medicare pays the hospice agency a fixed daily rate that varies by the level of care being provided. Understanding these levels helps families know what care to expect and what the billing should reflect.</p>

<table>
    <thead>
        <tr><th>Level</th><th>Description</th><th>Where Provided</th><th>Medicare Daily Rate (2026)</th><th>Patient Cost</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Routine Home Care</strong></td><td>Standard hospice: periodic visits by nurses, aides, social workers. Patient is stable.</td><td>Home (or nursing facility)</td><td>$218/day (days 1&ndash;60), $172/day (61+)</td><td>$0</td></tr>
        <tr><td><strong>Continuous Home Care</strong></td><td>8&ndash;24 hours of nursing during a crisis period (uncontrolled pain, acute distress).</td><td>Home</td><td>$63/hour (minimum 8 hours)</td><td>$0</td></tr>
        <tr><td><strong>Inpatient Respite Care</strong></td><td>Up to 5 consecutive days in a facility to relieve family caregivers.</td><td>Hospital, SNF, or hospice facility</td><td>$203/day</td><td>5% coinsurance (~$10/day)</td></tr>
        <tr><td><strong>General Inpatient Care (GIP)</strong></td><td>Short-term inpatient stay for acute symptom management that cannot be handled at home.</td><td>Hospital or hospice inpatient facility</td><td>$1,145/day</td><td>$0</td></tr>
    </tbody>
</table>

<p>The most common level is Routine Home Care, which covers approximately 97% of all hospice days. General Inpatient Care is the most expensive level and is reserved for acute crises&mdash;uncontrolled pain requiring IV medication adjustments, severe respiratory distress, or other symptoms that cannot be managed at home. GIP stays are typically 3&ndash;7 days.</p>

<p>A common billing issue arises when a hospice agency bills Medicare for Routine Home Care on days the patient is actually receiving General Inpatient Care, or vice versa. This can affect family responsibility if the patient has Medicaid or a secondary insurer. Use our <a href="/calculator">cost calculator</a> to look up hospice-related CPT codes and compare charges.</p>

<h2 id="what-is-not-covered">3. What hospice does NOT cover</h2>

<p>Understanding what falls outside the hospice benefit prevents the most common source of unexpected bills:</p>

<ul>
    <li><strong>Curative treatment for the terminal illness.</strong> If the patient elects hospice for lung cancer, chemotherapy intended to cure the cancer is not covered. However, palliative chemotherapy or radiation to relieve symptoms (e.g., shrink a tumor pressing on an airway) <em>is</em> covered if the hospice medical director approves it as part of the comfort care plan.</li>
    <li><strong>Treatment for unrelated conditions.</strong> A hospice patient who breaks a hip in a fall can receive standard Medicare-covered treatment for the fracture. The hip treatment is not the hospice agency&rsquo;s responsibility&mdash;it is billed to regular Medicare Part A and Part B. Verify that your provider bills the unrelated condition to standard Medicare, not the hospice benefit.</li>
    <li><strong>Room and board in a nursing facility.</strong> If the hospice patient resides in a nursing home, the hospice benefit covers only the hospice-specific care. The nursing home room and board is paid by Medicaid (if the patient qualifies), private insurance, or the patient&rsquo;s own funds.</li>
    <li><strong>Emergency room visits for the terminal condition.</strong> ER visits related to the terminal illness should go through the hospice agency first. If the patient goes directly to the ER for a terminal-illness-related issue without hospice coordination, the ER may bill standard Medicare, which may not pay because the patient is on the hospice benefit&mdash;leaving the family with the bill.</li>
</ul>

<div class="key-takeaway">
    <strong>Before any medical appointment or ER visit for a hospice patient:</strong> Call the hospice agency first. They will determine whether the issue is related to the terminal illness (and therefore their responsibility to manage) or unrelated (and therefore billable to standard Medicare). This one call prevents the most common hospice billing errors. Check your hospice provider&rsquo;s track record in our <a href="/hospitals/">hospital directory</a>.
</div>

<h2 id="billing-errors">4. Common hospice billing errors</h2>

<div class="bill-example">
    <div class="bill-header">Statement from Valley Pharmacy &mdash; Patient: James R. &mdash; DOS: 01/05/2026&ndash;01/31/2026</div>
    <div class="line-item error">
        <span>Morphine sulfate 15mg tabs (90ct) &nbsp; &#10060; <em>Pain medication for terminal illness should be provided by hospice agency, not billed to patient</em></span>
        <span>$285.00</span>
    </div>
    <div class="line-item error">
        <span>Ondansetron 4mg ODT (30ct) &nbsp; &#10060; <em>Anti-nausea medication related to terminal condition; hospice responsibility</em></span>
        <span>$142.00</span>
    </div>
    <div class="line-item flagged">
        <span>Lisinopril 10mg tabs (30ct) &nbsp; &#9888; <em>Blood pressure medication&mdash;may be unrelated to terminal diagnosis. Verify with hospice team.</em></span>
        <span>$18.00</span>
    </div>
    <div class="line-item">
        <span>Omeprazole 20mg caps (30ct) &mdash; Unrelated to terminal diagnosis per hospice plan</span>
        <span>$22.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED TO PATIENT</span>
        <span>$467.00</span>
    </div>
</div>

<p>The bill above shows the most common hospice billing error: <strong>medications related to the terminal illness billed directly to the patient or their insurance instead of through the hospice agency.</strong> When a patient elects hospice, the hospice agency becomes responsible for providing and paying for all medications related to the terminal condition. The patient should only pay the small hospice drug copay ($5 or 5%), and the hospice agency should be the entity obtaining and delivering these drugs.</p>

<p>Other common hospice billing errors:</p>

<ul>
    <li><strong>DME billed to the patient or Medicare Part B:</strong> Hospital beds, oxygen concentrators, and wheelchairs related to the terminal illness are covered under the hospice benefit. If a DME supplier bills these to regular Medicare or directly to the patient, it is an error. Contact the hospice agency and ask them to arrange the equipment through their contracted suppliers.</li>
    <li><strong>Ambulance transport billed to the patient:</strong> If the hospice agency arranges transport to an inpatient facility for GIP-level care, the transport is part of the hospice benefit.</li>
    <li><strong>Attending physician billed at full fee:</strong> The patient&rsquo;s attending physician (not the hospice medical director) can bill Medicare Part B for visits, but only for the patient&rsquo;s portion of cost-sharing. If the attending physician bills the patient for the full visit charge, this is incorrect.</li>
</ul>

<div class="case-study">
    <h3>Case study: Family billed $12,000 for drugs that should have been covered under hospice benefit</h3>
    <p>The family of a 78-year-old hospice patient with terminal pancreatic cancer received bills totaling <strong>$12,340</strong> from a retail pharmacy over a 4-month period. The bills were for pain medications (fentanyl patches, morphine liquid, gabapentin), anti-nausea drugs, and anxiolytics&mdash;all related to the terminal cancer diagnosis. The family had been paying out of pocket, not realizing these drugs were the hospice agency&rsquo;s responsibility.</p>
    <p>After the patient&rsquo;s daughter contacted BillKarma and reviewed the hospice benefit, she called the hospice agency and provided the pharmacy receipts. The hospice agency acknowledged the error&mdash;their pharmacy coordinator had failed to set up the patient&rsquo;s prescriptions through the agency&rsquo;s contracted pharmacy. The agency reimbursed the family for all drug costs related to the terminal diagnosis: <strong>$11,280</strong> (after deducting the $5 copays the patient would have owed per prescription). The remaining $1,060 was for medications unrelated to the terminal illness, which were correctly billed to the patient&rsquo;s Medicare Part D plan.</p>
</div>

<p>If you suspect your family is being billed for services that should be covered by hospice, <a href="/scan">upload the bills to BillKarma</a> for a quick check against the Medicare Hospice Benefit coverage rules.</p>

<h2 id="room-and-board">5. Room and board: who pays what</h2>

<p>Room and board is the most confusing part of hospice billing, because the answer depends entirely on <strong>where</strong> the patient is receiving care and <strong>what level</strong> of care is being provided:</p>

<ul>
    <li><strong>Patient is at home:</strong> No room and board charge. Medicare pays the hospice agency a daily rate, and the agency provides all services at the patient&rsquo;s home.</li>
    <li><strong>Patient is in a nursing home (Routine Home Care level):</strong> Medicare hospice covers the hospice care (nursing visits, medications, supplies). Room and board at the nursing home is <strong>not</strong> covered by hospice. If the patient qualifies for Medicaid, Medicaid pays the nursing home room and board. Otherwise, the patient or family pays privately.</li>
    <li><strong>Patient is admitted for General Inpatient Care (GIP):</strong> Medicare hospice covers <strong>everything</strong>, including room and board. This is for acute symptom crises requiring inpatient-level management. The patient owes $0 for a GIP stay.</li>
    <li><strong>Patient is admitted for Respite Care:</strong> Medicare hospice covers the stay with a <strong>5% coinsurance</strong> charged to the patient (approximately $10 per day). Respite stays are limited to 5 consecutive days.</li>
</ul>

<p>A significant billing problem occurs when a patient in a nursing home is on hospice at the Routine Home Care level, but the nursing home bills the family for &ldquo;hospice-related&rdquo; supplies or services that should be provided by the hospice agency. If you receive a bill from the nursing facility for supplies like wound care materials, oxygen, or catheter kits for a hospice patient, contact the hospice agency&mdash;these items are their responsibility, not the nursing home&rsquo;s to bill. Learn more about nursing facility billing in our <a href="/guides/skilled-nursing-billing">skilled nursing billing guide</a>. You can also check the nursing home&rsquo;s billing track record in our <a href="/hospitals/">hospital and provider directory</a>.</p>

<p>If you are uncertain whether a bill you received should have been covered under the hospice benefit, <a href="/scan">upload it to BillKarma</a> and we will flag charges that appear to be the hospice agency&rsquo;s responsibility. For more on understanding what your insurance paid and what you owe, see our <a href="/guides/understanding-your-explanation-of-benefits">guide to reading your EOB</a>.</p>

{_embed(mode="markup", title="Check hospice-related charges", subtitle="See whether your charges should be covered under the hospice benefit.", height="420")}

<h2 id="revocation">6. Revocation, recertification, and benefit periods</h2>

<p>The hospice benefit is organized into benefit periods: two initial 90-day periods, followed by unlimited 60-day periods. At the start of each period, a physician must recertify that the patient&rsquo;s life expectancy remains 6 months or less. There is no maximum duration&mdash;patients can remain on hospice for years if they continue to meet eligibility criteria.</p>

<p><strong>Revocation:</strong> A patient can revoke (leave) the hospice benefit at any time by signing a written statement. Revocation is effective on the date of the signature. The patient returns to standard Medicare coverage. Common reasons to revoke include deciding to pursue curative treatment, the patient&rsquo;s condition unexpectedly improving, or dissatisfaction with the hospice agency (in which case the patient can re-elect hospice with a different agency).</p>

<p><strong>Discharge vs. revocation:</strong> The hospice agency can discharge a patient if they no longer meet eligibility criteria (condition has improved), move outside the agency&rsquo;s service area, or exhibit behavior that makes care unsafe. Discharge is different from revocation&mdash;discharge is the agency&rsquo;s decision, revocation is the patient&rsquo;s.</p>

<div class="case-study">
    <h3>Case study: Hospice agency continued billing after patient revoked</h3>
    <p>A family in Florida revoked their father&rsquo;s hospice benefit on March 1 so he could receive a clinical trial treatment for his lung cancer. The hospice agency continued billing Medicare for Routine Home Care through March 22&mdash;21 days after revocation. When the patient later needed to re-enroll in hospice (the trial was unsuccessful), the hospice agency claimed his benefit period had been &ldquo;used up&rdquo; because of the 21 extra billed days.</p>
    <p>The family contacted Medicare and discovered the overbilling. Medicare recouped <strong>$4,578</strong> (21 days &times; $218/day) from the hospice agency and confirmed the patient was eligible for a new benefit period. The patient re-elected hospice with a different agency. <strong>Family savings: $4,578 in improperly billed days, plus restored benefit eligibility.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: $4,800 overcharge for continuous home care days that were actually routine care</h3>
    <p>The family of an 82-year-old hospice patient with end-stage COPD received a statement from the hospice agency showing 8 days billed to Medicare as Continuous Home Care ($63/hour, minimum 8 hours per day) during a single month. Continuous Home Care requires 8&ndash;24 hours of predominantly nursing care during a documented medical crisis. The family knew from their own daily logs that the patient had received only the standard 1&ndash;2 hour nursing visits on those days&mdash;no crisis, no extended nursing presence.</p>
    <p>They contacted Medicare&rsquo;s hotline (1-800-MEDICARE) and reported the discrepancy. A Medicare auditor reviewed the clinical documentation and confirmed that the 8 days did not meet Continuous Home Care criteria&mdash;the nursing notes documented only routine visits with no crisis-level care. Medicare reclassified the 8 days from Continuous Home Care to Routine Home Care and recouped the difference from the hospice agency: <strong>$4,800</strong> ($600/day overbilled &times; 8 days). The family owed nothing additional. <strong>Overcharge reversed: $4,800.</strong></p>
    <p><strong>Lesson:</strong> Keep a daily log of every hospice visit&mdash;who came, how long they stayed, and what care was provided. If your loved one&rsquo;s hospice bills show Continuous Home Care or General Inpatient Care days, verify that the level of care actually matched what was delivered.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Medicare cover hospice care?</h3>
        <p>Yes. Medicare Part A covers virtually all costs related to the terminal illness under the hospice benefit: nursing, medications (with a small $5 copay), medical equipment, supplies, aide services, social work, chaplain services, and bereavement counseling. The patient pays $0 for most services. To qualify, a physician must certify a life expectancy of 6 months or less.</p>
    </div>

    <div class="faq-item">
        <h3>What does hospice NOT cover?</h3>
        <p>Hospice does not cover curative treatment for the terminal illness (only comfort care), room and board at a nursing facility (unless the patient is there for respite or GIP-level care), treatments unrelated to the terminal diagnosis (these are billed to standard Medicare), or ER visits for the terminal condition without hospice coordination.</p>
    </div>

    <div class="faq-item">
        <h3>Can I revoke hospice and go back to regular Medicare?</h3>
        <p>Yes, at any time. Sign a written revocation statement and you return to standard Medicare coverage immediately. You can re-elect hospice later if you meet eligibility criteria. Revocation makes sense if you decide to pursue curative treatment or your condition unexpectedly improves.</p>
    </div>

    <div class="faq-item">
        <h3>What are the 4 levels of hospice care?</h3>
        <p>Routine Home Care (standard periodic visits, $218/day), Continuous Home Care (8&ndash;24 hours of nursing during a crisis, $63/hour), Inpatient Respite Care (up to 5 days to relieve caregivers, $203/day with 5% coinsurance), and General Inpatient Care (acute symptom management at a hospital/facility, $1,145/day, $0 to patient). The level should match the patient&rsquo;s documented clinical needs.</p>
    </div>

    <div class="faq-item">
        <h3>Who pays for room and board during hospice?</h3>
        <p>At home: no room and board charge. In a nursing home: Medicaid or the patient pays room and board; hospice covers only the hospice care. For General Inpatient Care: Medicare hospice covers everything including room and board ($0 to patient). For Respite Care: Medicare covers with a 5% coinsurance (~$10/day to patient).</p>
    </div>
</div>

<div class="key-takeaway">
    <strong>Received a suspicious hospice bill?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we&rsquo;ll flag any charges that should be covered under the Medicare hospice benefit. Check your hospice provider&rsquo;s billing record in our <a href="/hospitals/">hospital directory</a>.
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-for-service-providers/hospice" target="_blank" rel="noopener">CMS: Medicare Hospice Benefit Payment Rates (2026)</a></li>
    <li><a href="https://www.medicare.gov/coverage/hospice-care" target="_blank" rel="noopener">Medicare.gov: Hospice Care Coverage Details</a></li>
    <li><a href="https://www.nhpco.org/research/facts-and-figures/" target="_blank" rel="noopener">National Hospice and Palliative Care Organization: Facts and Figures (2025)</a></li>
    <li><a href="https://oig.hhs.gov/reports-and-publications/featured-topics/hospice/" target="_blank" rel="noopener">HHS Office of Inspector General: Hospice Billing Oversight Reports</a></li>
    <li><a href="https://www.medpac.gov/document/hospice-services/" target="_blank" rel="noopener">MedPAC: Report to Congress on Hospice Payment and Quality</a></li>
</ul>
""",
})
