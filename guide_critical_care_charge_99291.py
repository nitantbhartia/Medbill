"""Guide: Critical Care Charge (CPT 99291) on an ER Bill."""

from guides import register

register("critical-care-charge-99291", {
    "title": "Critical Care Charge (CPT 99291) on an ER Bill",
    "meta_description": "CPT 99291 means at least 30 minutes of critical care for a life-threatening condition. Learn how the time is counted and how to check your ER bill.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "What does CPT 99291 mean on an ER bill?",
            "a": "CPT 99291 is the billing code for the first 30 to 74 minutes of critical care. Medicare uses the CPT definition: care for a patient with acute impairment of one or more vital organ systems, where there is a probability of imminent or life-threatening deterioration. It is a time-based code, so the medical record should show how many minutes of critical care were provided.",
        },
        {
            "q": "Can I be charged for critical care if I wasn't in the ICU?",
            "a": "Yes. CMS says critical care is typically furnished in a critical care area, which can include an intensive care unit or an emergency care facility. Your condition and the documented time matter, not the room.",
        },
        {
            "q": "When can 99292 be billed under Medicare?",
            "a": "Under Medicare's policy since 2022, 99291 covers the first 30 to 74 minutes, and 99292 can be added only for each additional complete 30 minutes. That means the first 99292 needs at least 104 total minutes of critical care on that date. CMS has said this differs from CPT codebook guidance, so private insurers may use a different rule.",
        },
        {
            "q": "Why do I have two critical care charges from the same ER visit?",
            "a": "The doctor's group bills for the clinician's time, and the hospital bills for its facility costs. Both can list 99291. Medicare tells hospitals that provide less than 30 minutes of critical care to bill a visit, typically an emergency department visit, instead.",
        },
        {
            "q": "How do I dispute a critical care charge I think is wrong?",
            "a": "Get an itemized bill and your ER records, including any critical care time statement. Compare the minutes to the codes. If the record does not support them, ask the billing office in writing for a coding review, keep copies, and contact your plan.",
        },
        {
            "q": "What does Medicare pay for CPT 99291 in 2026?",
            "a": "Based on the CMS 2026 physician fee schedule file (October release), the national facility amount for the doctor's part of 99291 is about $199.07 at the $33.4009 conversion factor. It varies by location and excludes the hospital's separate facility payment.",
        },
    ],
    "body": f"""
<p class="lead">CPT 99291 is the code for the first 30 to 74 minutes of critical care: hands-on care for a patient whose vital organs are failing or at real risk of failing. If your ER visit did not feel that serious, you can ask the hospital for the records that show the condition and the minutes behind the charge, and request a coding review if they do not support it.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-it-means">What &ldquo;critical care&rdquo; means for billing</a></li>
        <li><a href="#time-rules">How critical care time is counted</a></li>
        <li><a href="#two-bills">Doctor bill vs. hospital bill (and trauma activation)</a></li>
        <li><a href="#vs-level-5">Critical care vs. a level 5 ER visit (99285)</a></li>
        <li><a href="#example">Example: checking the minutes</a></li>
        <li><a href="#what-to-do">What to do if you question the charge</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-it-means">1. What &ldquo;critical care&rdquo; means for billing</h2>

<p>A CPT code (the standard billing code for a medical service) tells your insurer what was done. Two codes cover critical care:</p>

<ul>
    <li><strong>99291:</strong> critical care, first 30&ndash;74 minutes</li>
    <li><strong>99292:</strong> each additional 30 minutes (an &ldquo;add-on&rdquo; code that is only billed with 99291)</li>
</ul>

<p>Since January 1, 2022, Medicare has used the CPT definition. In plain terms, critical care is care given directly by a physician or other qualified clinician to a patient with <strong>acute impairment of one or more vital organ systems</strong>, where there is a <strong>probability of imminent or life-threatening deterioration</strong>. It involves high-complexity decisions to treat organ failure or prevent the patient from getting worse.</p>

<p>Three CMS rules matter for your bill:</p>

<ul>
    <li><strong>It is about your condition, not the room.</strong> CMS says critical care is typically furnished in a critical care area, which can include an intensive care unit (ICU) <em>or an emergency care facility</em>. You do not have to be admitted to the ICU for 99291 to apply.</li>
    <li><strong>It is time-based.</strong> CMS requires the clinician to document the total critical care time in the medical record (not necessarily start and stop times).</li>
    <li><strong>It takes the clinician&rsquo;s full attention.</strong> For any minute counted as critical care, the clinician cannot be caring for another patient.</li>
</ul>

<p>Pain, fear or many tests do not by themselves make care &ldquo;critical.&rdquo; The record has to show a threat to a vital organ system and the time spent treating it.</p>

<h2 id="time-rules">2. How critical care time is counted</h2>

<p>The clinician adds up all critical care minutes for one patient on one date, even if spread out. Under Medicare&rsquo;s policy, 99291 is billed once per date for 30&ndash;74 minutes, and 99292 is added only for each additional <em>complete</em> 30 minutes. CMS confirmed in its 2023 fee schedule rule that the first 99292 requires <strong>104 total minutes</strong> (74 + 30).</p>

<table>
    <thead>
        <tr>
            <th>Documented critical care time (one date)</th>
            <th>What Medicare&rsquo;s rule allows the clinician to bill</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Under 30 minutes</td>
            <td>Not enough for 99291 (its range starts at 30 minutes)</td>
        </tr>
        <tr>
            <td>30&ndash;103 minutes</td>
            <td>99291 &times; 1</td>
        </tr>
        <tr>
            <td>104&ndash;133 minutes</td>
            <td>99291 &times; 1 + 99292 &times; 1</td>
        </tr>
        <tr>
            <td>134&ndash;163 minutes</td>
            <td>99291 &times; 1 + 99292 &times; 2</td>
        </tr>
    </tbody>
</table>

<p>Other Medicare rules on what counts:</p>

<ul>
    <li><strong>Separate procedures don&rsquo;t count as critical care time.</strong> Time spent on a separately billed procedure should be billed on its own and left out of the critical care minutes.</li>
    <li><strong>Some services are bundled in.</strong> CMS lists items included in the critical care code for the clinician providing it, such as reading chest X-rays, pulse oximetry, blood gases, ECGs, ventilator management and vascular access. That clinician should not bill them separately for the same period.</li>
    <li><strong>Earlier ER visit on the same date.</strong> Both an ER visit and critical care can be billed for the same date only if the record shows the ER visit came first, when you did not yet need critical care, and that the two services did not overlap.</li>
</ul>

<p><strong>Private insurance may differ.</strong> CMS acknowledges its 104-minute rule differs from CPT codebook guidance, which commenters said allows 99292 after 75 minutes. Your private plan&rsquo;s policy decides which rule applies.</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>Critical care is billed by the minute, so the documented time is the first thing to check. If the bill shows 99292 but you were in the ER a short time, compare the codes to the record. Our guide on <a href="/guides/how-to-request-medical-records/">how to request your medical records</a> explains how to get the notes.</p></div>

<h2 id="two-bills">3. Doctor bill vs. hospital bill (and trauma activation)</h2>

<p>An ER visit often produces two bills, and both can show 99291:</p>

<ul>
    <li><strong>The professional bill</strong> comes from the ER doctor&rsquo;s group for the clinician&rsquo;s time and decisions. The time rules in section 2 apply here.</li>
    <li><strong>The facility bill</strong> comes from the hospital for its staff, space and equipment. Medicare&rsquo;s outpatient manual tells hospitals to follow the CPT instructions for 99291.</li>
</ul>

<p>For the hospital bill, Medicare counts the time a physician and/or hospital staff spend in <strong>active face-to-face critical care</strong>. If several staff members work on you at the same time, those minutes count once. Medicare applies the same 30-minute minimum to hospitals: a hospital that provides less than 30 minutes of critical care should bill a visit instead, typically an emergency department visit. Under Medicare&rsquo;s outpatient system, 99292 is packaged into the main payment and not paid separately for the hospital, though hospitals should still report it.</p>

<h3>Where trauma activation fits</h3>

<p>A trauma activation fee is a charge for calling in a trauma team before you arrive. Medicare links it to critical care. A hospital may bill one unit of <strong>G0390</strong> (trauma activation associated with hospital critical care) only when:</p>

<ul>
    <li>the hospital also bills 99291 (and 99292, if it applies) for the same date,</li>
    <li>it reports a trauma revenue code in the 68x series on the same date,</li>
    <li>it is a trauma center licensed or designated by a state or local authority, or verified by the American College of Surgeons, and</li>
    <li>there was prehospital notification based on field triage criteria, or you were transferred from another hospital, and the team responded.</li>
</ul>

<p>If you see G0390 without a critical care code, or you arrived on your own with no ambulance notice or transfer, ask how these conditions were met. Our <a href="/guides/trauma-activation-fee/">trauma activation fee guide</a> covers this charge in more detail.</p>

<h2 id="vs-level-5">4. Critical care vs. a level 5 ER visit (99285)</h2>

<p>The highest regular ER visit code is <strong>99285</strong>, a visit with high-complexity medical decision-making. Critical care is separate: it needs a life-threatening condition and at least 30 documented minutes. A visit can be serious without meeting that definition.</p>

<p>Below is what Medicare&rsquo;s 2026 physician fee schedule pays the doctor: national facility amounts (the rate when the doctor works in a hospital) from the CMS October 2026 relative value file, before local adjustment and excluding the hospital&rsquo;s own payment.</p>

<table>
    <thead>
        <tr>
            <th>Code</th>
            <th>Facility total RVUs</th>
            <th>2026 national amount ($33.4009 conversion factor)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>99285 &ndash; ER visit, high complexity</td>
            <td>5.13</td>
            <td>$171.35</td>
        </tr>
        <tr>
            <td>99291 &ndash; critical care, first 30&ndash;74 min</td>
            <td>5.96</td>
            <td>$199.07</td>
        </tr>
        <tr>
            <td>99292 &ndash; each additional 30 min</td>
            <td>3.00</td>
            <td>$100.20</td>
        </tr>
    </tbody>
</table>

<p>RVUs (relative value units) are the points Medicare assigns to each service; multiplying by the conversion factor gives the dollar amount. Clinicians in qualifying alternative payment models use a slightly higher 2026 conversion factor ($33.5675), which puts 99291 at about $200.06. Your area&rsquo;s amount may differ; the CMS Physician Fee Schedule look-up tool shows local rates. For more on the ER visit levels, see our guide to the <a href="/guides/er-level-5-charge-99285/">level 5 ER charge (99285)</a>.</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>If your notes describe a serious but stable visit, the question is whether the record supports critical care or an ER visit code like 99285. You can <a href="/scan">check your bill free</a> to see each line next to Medicare&rsquo;s rate and flag charges worth asking about.</p></div>

<h2 id="example">5. Example: checking the minutes</h2>

<p><strong>Example:</strong> This is an illustration, not a real patient or hospital. A Medicare patient&rsquo;s bill from the ER doctor&rsquo;s group lists 99291 &times; 1 and 99292 &times; 1. The patient requests the ER physician note, which states &ldquo;critical care time: 70 minutes, excluding separately billable procedures.&rdquo;</p>

<ul>
    <li>70 minutes falls in the 30&ndash;103 minute range, so Medicare&rsquo;s rule supports 99291 &times; 1.</li>
    <li>The first 99292 needs 104 minutes. At 70 minutes, the 99292 line does not appear to be supported.</li>
    <li>At 2026 national facility amounts, the billed codes add up to $199.07 + $100.20 = $299.27. With only 99291, the amount is $199.07, a difference of $100.20.</li>
</ul>

<p>If the note listed 25 minutes instead, that is under the 30-minute minimum for 99291, so the patient could ask whether an ER visit code such as 99285 ($171.35 nationally) fits the record better.</p>

<h2 id="what-to-do">6. What to do if you question the charge</h2>

<ol>
    <li><strong>Get an itemized bill from each provider.</strong> Ask both the hospital and the physician group for a bill that lists each CPT and HCPCS code, units and date. Our guide on <a href="/guides/how-to-get-itemized-hospital-bill/">getting an itemized hospital bill</a> shows how.</li>
    <li><strong>Request your ER records.</strong> Ask for the ER physician note, any critical care time statement, nursing notes, and (for the hospital) trauma activation records. Under HIPAA, a provider generally must act on your access request no later than 30 days after receiving it.</li>
    <li><strong>Find the condition and the minutes.</strong> Look for a stated total of critical care time and a description of what was life-threatening, such as low blood pressure, breathing failure or a dangerous heart rhythm. Note whether procedure time was excluded.</li>
    <li><strong>Match the minutes to the codes.</strong> Use the table in section 2. Check for 99292 billed under 104 minutes (Medicare), 99291 billed with under 30 minutes, or bundled items like pulse oximetry billed separately by the same clinician during critical care.</li>
    <li><strong>Check your insurer&rsquo;s statement.</strong> Compare the bill with your Explanation of Benefits or Medicare Summary Notice and make sure the codes and your share match.</li>
    <li><strong>Write to the billing office.</strong> Ask for a coding review of the specific lines, cite the documented minutes, and ask them to hold the account while they review it. Our <a href="/guides/medical-bill-dispute-letter/">medical bill dispute letter guide</a> has a template.</li>
    <li><strong>Escalate if needed.</strong> If the provider does not correct a charge you believe is unsupported, you can file an appeal with your insurer or Medicare. For a large balance or collections, consider talking to a consumer attorney or legal aid.</li>
</ol>

<div class="key-takeaway"><h3>Key takeaway</h3><p>A short, specific letter works better than a general complaint: name the code, the date, the minutes in your record and the rule. For the full process, see <a href="/guides/how-to-dispute-a-medical-bill/">how to dispute a medical bill</a>.</p></div>

<p>Critical care can be correctly billed even if you felt fine afterward, because fast treatment may have stopped a dangerous decline. The goal is to confirm the record supports the codes, not to assume a mistake.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What does CPT 99291 mean on an ER bill?</h3>
        <p>CPT 99291 is the billing code for the first 30 to 74 minutes of critical care. Medicare uses the CPT definition: care for a patient with acute impairment of one or more vital organ systems, where there is a probability of imminent or life-threatening deterioration. It is a time-based code, so the medical record should show how many minutes of critical care were provided.</p>
    </div>
    <div class="faq-item">
        <h3>Can I be charged for critical care if I wasn't in the ICU?</h3>
        <p>Yes. CMS says critical care is typically furnished in a critical care area, which can include an intensive care unit or an emergency care facility. Your condition and the documented time matter, not the room.</p>
    </div>
    <div class="faq-item">
        <h3>When can 99292 be billed under Medicare?</h3>
        <p>Under Medicare&rsquo;s policy since 2022, 99291 covers the first 30 to 74 minutes, and 99292 can be added only for each additional complete 30 minutes. That means the first 99292 needs at least 104 total minutes of critical care on that date. CMS has said this differs from CPT codebook guidance, so private insurers may use a different rule.</p>
    </div>
    <div class="faq-item">
        <h3>Why do I have two critical care charges from the same ER visit?</h3>
        <p>The doctor&rsquo;s group bills for the clinician&rsquo;s time, and the hospital bills for its facility costs. Both can list 99291. Medicare tells hospitals that provide less than 30 minutes of critical care to bill a visit, typically an emergency department visit, instead.</p>
    </div>
    <div class="faq-item">
        <h3>How do I dispute a critical care charge I think is wrong?</h3>
        <p>Get an itemized bill and your ER records, including any critical care time statement. Compare the minutes to the codes. If the record does not support them, ask the billing office in writing for a coding review, keep copies, and contact your plan.</p>
    </div>
    <div class="faq-item">
        <h3>What does Medicare pay for CPT 99291 in 2026?</h3>
        <p>Based on the CMS 2026 physician fee schedule file (October release), the national facility amount for the doctor&rsquo;s part of 99291 is about $199.07 at the $33.4009 conversion factor. It varies by location and excludes the hospital&rsquo;s separate facility payment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c12.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 12, Section 30.6.12 (Critical Care Visits)</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c04.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 4, Section 160.1 (Critical Care Services, hospital outpatient)</a></li>
    <li><a href="https://www.govinfo.gov/content/pkg/FR-2021-11-19/html/2021-23972.htm" target="_blank" rel="noopener">Federal Register &mdash; CY 2022 Physician Fee Schedule Final Rule (86 FR 64996), Critical Care Services</a></li>
    <li><a href="https://www.govinfo.gov/content/pkg/FR-2022-11-18/html/2022-23873.htm" target="_blank" rel="noopener">Federal Register &mdash; CY 2023 Physician Fee Schedule Final Rule (87 FR 69404), Technical Correction for Split (or Shared) Critical Care Services</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician/pfs-relative-value-files/rvu26d" target="_blank" rel="noopener">CMS &mdash; PFS Relative Value Files, RVU26D (2026, October release)</a></li>
    <li><a href="https://www.cms.gov/medicare/physician-fee-schedule/search" target="_blank" rel="noopener">CMS &mdash; Physician Fee Schedule Look-Up Tool</a></li>
    <li><a href="https://www.govinfo.gov/content/pkg/CFR-2024-title45-vol2/xml/CFR-2024-title45-vol2-sec164-524.xml" target="_blank" rel="noopener">GovInfo &mdash; 45 CFR 164.524, Access of individuals to protected health information</a></li>
</ul>
""",
})
