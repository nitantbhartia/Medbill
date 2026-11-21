"""Guide: Transferred Between Hospitals? Why You Got Two ER Bills."""

from guides import register

register("er-transfer-two-hospital-bills", {
    "title": "Transferred Between Hospitals? Why You Got Two ER Bills",
    "meta_description": "Transferred to a second hospital? Each hospital bills for its own care, and the ambulance bills too. See which bills are protected and how to check each.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "Why did I get ER bills from two hospitals after one emergency?",
            "a": "Each hospital is a separate facility that gave you its own care. The first billed for checking and stabilizing you. The second billed for the care you got after you arrived. Doctors at each hospital may bill separately, and the ambulance company sends its own bill.",
        },
        {
            "q": "Is the air ambulance transfer covered by the No Surprises Act?",
            "a": "For most private health plans, yes. CMS says an out-of-network air ambulance provider cannot charge you more than your in-network cost-sharing for covered care. People with Medicare and Medicaid have their own protections. If a bill asks for more than your explanation of benefits says you owe, call the No Surprises Help Desk at 1-800-985-3059.",
        },
        {
            "q": "Does the No Surprises Act protect me from a ground ambulance bill?",
            "a": "Generally, no, unless your state has its own law. CMS listed 10 states with ground ambulance protections as of November 15, 2021, and that list may be out of date. As of November 2026, we could not confirm any new federal ground ambulance protection.",
        },
        {
            "q": "If I have Medicare and was admitted at the second hospital, do I pay two deductibles?",
            "a": "Not for the inpatient part. Original Medicare charges the Part A deductible ($1,736 in 2026) once per benefit period, which ends after you have not been an inpatient for 60 days in a row. Medicare Advantage plans set their own cost-sharing.",
        },
        {
            "q": "Can both hospitals bill me for the same test?",
            "a": "Each hospital can bill for tests it actually did, and the second hospital may repeat a scan. One hospital should not bill for a service the other did. Compare itemized bills from both against your explanation of benefits.",
        },
    ],
    "body": f"""
<p class="lead">You got two ER bills because two separate hospitals cared for you, and each one bills for the care it gave. The first hospital billed for checking and stabilizing you, the second billed for the care after the transfer, and the ambulance company sends its own bill for the ride. What you can control is making sure each bill is accurate, matches your insurance paperwork, and gets the federal protections it qualifies for.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#why-transfer">Why hospitals transfer patients</a></li>
        <li><a href="#why-two-bills">Why each hospital sends its own bill</a></li>
        <li><a href="#bill-table">Every bill you might get, and what protects you</a></li>
        <li><a href="#ambulance">The transfer ambulance: air vs. ground</a></li>
        <li><a href="#admitted">If you were admitted at the second hospital</a></li>
        <li><a href="#what-to-do">What to do: match every bill to your EOB</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="why-transfer">1. Why hospitals transfer patients</h2>

<p>A federal law called EMTALA (the Emergency Medical Treatment and Labor Act) sets rules for hospitals that take part in Medicare and have an emergency department. Its rule, 42 CFR 489.24, says the hospital must give you a medical screening exam and cannot delay it to ask how you will pay.</p>

<p>If your emergency condition is not yet stabilized, the hospital can transfer you only if you ask for it in writing, or a doctor certifies that the benefits of care elsewhere outweigh the risks of the move. The transfer must also be &ldquo;appropriate,&rdquo; which at a high level means:</p>

<ul>
    <li>The first hospital treats you as well as it can to lower the risk of moving you.</li>
    <li>The receiving hospital has space and qualified staff, and has agreed to accept you.</li>
    <li>Your medical records go with you.</li>
    <li>The move uses qualified staff and equipment, including life support if needed.</li>
</ul>

<p>Common reasons include a specialist, an ICU bed or equipment the first hospital lacks. EMTALA is about safe care. It does not decide who pays, so the billing questions below depend on your insurance and other laws.</p>

<h2 id="why-two-bills">2. Why each hospital sends its own bill</h2>

<p>Each hospital is a separate facility with its own billing office, and each usually bills in two parts:</p>

<ul>
    <li><strong>The facility bill</strong> covers the hospital&rsquo;s room, nurses, equipment, tests and supplies.</li>
    <li><strong>Professional bills</strong> come from the doctors who treated you, such as the ER doctor or a radiologist. Some work for outside groups that bill on their own.</li>
</ul>

<p>So one transfer can produce five or more bills. Our guide on <a href="/guides/multiple-bills-one-hospital-visit/">multiple bills for one hospital visit</a> explains the split. If the second hospital admitted you, its bill is for an inpatient stay, which changes what you pay (see section 5).</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Two ER bills after a transfer are expected, but each should charge only for care that hospital gave. <a href="/scan">Check each hospital bill free</a> to see every line compared to the Medicare rate and flag possible duplicates.</p>
</div>

<h2 id="bill-table">3. Every bill you might get, and what protects you</h2>

<p>The No Surprises Act is a federal law that applies to plan years starting on or after January 1, 2022. It protects people with most private insurance (job-based, Marketplace and other individual plans) from many surprise out-of-network bills. CMS says people with Medicare and Medicaid already have protections against surprise billing.</p>

<table>
    <thead>
        <tr>
            <th>Bill</th>
            <th>Who sends it</th>
            <th>Main protections (private insurance)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>First ER visit (facility)</td>
            <td>The first hospital</td>
            <td>No Surprises Act: an out-of-network ER can bill you no more than in-network cost-sharing for emergency services. No prior authorization required.</td>
        </tr>
        <tr>
            <td>First ER doctors</td>
            <td>ER or radiology physician groups</td>
            <td>Same emergency protection.</td>
        </tr>
        <tr>
            <td>Air ambulance transfer</td>
            <td>Air ambulance company</td>
            <td>No Surprises Act: no more than in-network cost-sharing for covered services.</td>
        </tr>
        <tr>
            <td>Ground ambulance transfer</td>
            <td>Ambulance company, fire department or hospital</td>
            <td>Generally not covered by the No Surprises Act. Some state laws apply.</td>
        </tr>
        <tr>
            <td>Second hospital (facility)</td>
            <td>The receiving hospital</td>
            <td>Emergency protections if it gave you emergency services, which can extend to care after you were stabilized. Otherwise, normal network rules.</td>
        </tr>
        <tr>
            <td>Second hospital doctors</td>
            <td>Specialists, hospitalists, surgeons</td>
            <td>Emergency protections for emergency care. The law also limits bills from certain out-of-network doctors at in-network hospitals.</td>
        </tr>
    </tbody>
</table>

<p>Under the federal rule (45 CFR 149.410), care after you are stabilized loses the emergency protection only if, among other conditions, the treating doctor decides you can travel by car or non-emergency transport to a nearby in-network facility, and you get a written notice and sign consent. If you were asked to sign a form waiving your protections, keep a copy. Whether the receiving hospital&rsquo;s care counts as part of the same emergency depends on your case, so if your plan treated it as out-of-network, ask the plan to explain and call the No Surprises Help Desk at 1-800-985-3059.</p>

<h2 id="ambulance">4. The transfer ambulance: air vs. ground</h2>

<h3>Air ambulance</h3>

<p>CMS lists air ambulance services among the bills the No Surprises Act covers. If you had covered care and were flown by an out-of-network air ambulance, the provider cannot charge you more than your in-network cost-sharing (copay, coinsurance and deductible). If the bill asks for more than your EOB (explanation of benefits, the statement your insurer sends after processing a claim) says you owe, raise it with the company and the Help Desk. See our <a href="/guides/air-ambulance-bills/">air ambulance bills guide</a>.</p>

<h3>Ground ambulance</h3>

<p>CMS says ground ambulance services generally are not covered by the No Surprises Act&rsquo;s billing protections unless state law says otherwise, and these providers can still charge out-of-network rates. CMS listed 10 states with ground ambulance protections as of November 15, 2021. That list is dated, so check with your state insurance department.</p>

<p>The law created an Advisory Committee on Ground Ambulance and Patient Billing, which CMS says issued its report on August 28, 2024. As of November 2026, we could not confirm any new federal law protecting patients from ground ambulance balance bills. CMS suggests asking the provider whether it can lower the bill or set up a payment plan.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>A transfer can put the same service on more than one bill. Learn how to spot <a href="/guides/duplicate-charges-hospital-bills/">duplicate charges on hospital bills</a> before you pay any of them.</p>
</div>

<h3>Medicare and the transfer ride</h3>

<p>Original Medicare Part B covers ground ambulance when traveling any other way could endanger your health, but only to the nearest appropriate facility. It covers air ambulance when you need fast transport that ground transport cannot provide. After the Part B deductible, you pay 20% of the Medicare-approved amount.</p>

<h3>Prior authorization</h3>

<p>Prior authorization means your insurer approves a service in advance. Private plans cannot require it for emergency services. A scheduled, non-emergency transfer may be treated differently depending on your plan. If a claim was denied for lack of prior authorization, get the denial in writing and consider an appeal. See <a href="/guides/how-to-appeal-insurance-denial/">how to appeal an insurance denial</a>.</p>

<h2 id="admitted">5. If you were admitted at the second hospital</h2>

<p><strong>Original Medicare.</strong> Part A covers inpatient care. In 2026 you pay a $1,736 deductible, then $0 per day for days 1 to 60 and $434 per day for days 61 to 90. Medicare.gov lists the 2027 deductible as $1,776.</p>

<p>The deductible applies per <strong>benefit period</strong>. Under 42 CFR 409.60, a benefit period starts when you begin inpatient care and ends once you have gone at least 60 days in a row without being an inpatient in a hospital or skilled nursing facility.</p>

<p><strong>Example:</strong> You have Original Medicare. In 2026 you are seen in one ER, then transferred and admitted to a second hospital for 5 days. You pay the $1,736 Part A deductible once. If you are readmitted 30 days after going home, you are still in the same benefit period, so no second Part A deductible.</p>

<p>If you were kept &ldquo;under observation&rdquo; instead, you are an outpatient even overnight, and costs work differently. See <a href="/guides/hospital-observation-status/">hospital observation status</a>.</p>

<p><strong>Private insurance or Medicare Advantage.</strong> Your plan&rsquo;s own deductible, coinsurance and out-of-pocket maximum apply. Check your plan documents, and see <a href="/guides/inpatient-vs-outpatient-billing/">inpatient vs. outpatient billing</a>.</p>

<h2 id="what-to-do">6. What to do: match every bill to your EOB</h2>

<p>Every bill should match a claim your insurer processed, and you should pay only what the EOB says you owe.</p>

<ol>
    <li><strong>List every bill.</strong> Note the sender, date of service, account number and amount for each.</li>
    <li><strong>Gather your EOBs</strong> from your insurer&rsquo;s website or your Medicare account. Our <a href="/guides/explanation-of-benefits-eob/">EOB guide</a> explains each field.</li>
    <li><strong>Match them up.</strong> Check that the provider, date and &ldquo;you may owe&rdquo; amount match. If a bill has no EOB, ask the provider whether it was sent to your insurance.</li>
    <li><strong>Ask for itemized bills</strong> with billing codes from each hospital. See <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a>.</li>
    <li><strong>Check for duplicates across bills.</strong> Look for the same service billed by both hospitals at the same date and time, or the ride billed by both the ambulance company and a hospital.</li>
    <li><strong>Check protection status.</strong> If an EOB shows out-of-network cost-sharing for emergency care or an air ambulance, ask your insurer why, and call the Help Desk at 1-800-985-3059.</li>
    <li><strong>Appeal denials in writing.</strong> Disputes under the No Surprises Act&rsquo;s emergency and air ambulance rules can also go to external review by an independent organization.</li>
    <li><strong>Apply for financial assistance</strong> at each hospital separately, since each has its own policy.</li>
    <li><strong>Get help if needed</strong> from your state&rsquo;s consumer assistance program. If it becomes a legal question, consider talking to a consumer attorney or legal aid.</li>
</ol>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>If the ambulance bill is the biggest one, start there. Our guide on <a href="/guides/how-to-fight-an-ambulance-bill/">how to fight an ambulance bill</a> covers what to ask for and how to dispute it in writing.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Why did I get ER bills from two hospitals after one emergency?</h3>
        <p>Each hospital is a separate facility that gave you its own care. The first billed for checking and stabilizing you. The second billed for the care you got after you arrived. Doctors at each hospital may bill separately, and the ambulance company sends its own bill.</p>
    </div>
    <div class="faq-item">
        <h3>Is the air ambulance transfer covered by the No Surprises Act?</h3>
        <p>For most private health plans, yes. CMS says an out-of-network air ambulance provider cannot charge you more than your in-network cost-sharing for covered care. People with Medicare and Medicaid have their own protections. If a bill asks for more than your explanation of benefits says you owe, call the No Surprises Help Desk at 1-800-985-3059.</p>
    </div>
    <div class="faq-item">
        <h3>Does the No Surprises Act protect me from a ground ambulance bill?</h3>
        <p>Generally, no, unless your state has its own law. CMS listed 10 states with ground ambulance protections as of November 15, 2021, and that list may be out of date. As of November 2026, we could not confirm any new federal ground ambulance protection.</p>
    </div>
    <div class="faq-item">
        <h3>If I have Medicare and was admitted at the second hospital, do I pay two deductibles?</h3>
        <p>Not for the inpatient part. Original Medicare charges the Part A deductible ($1,736 in 2026) once per benefit period, which ends after you have not been an inpatient for 60 days in a row. Medicare Advantage plans set their own cost-sharing.</p>
    </div>
    <div class="faq-item">
        <h3>Can both hospitals bill me for the same test?</h3>
        <p>Each hospital can bill for tests it actually did, and the second hospital may repeat a scan. One hospital should not bill for a service the other did. Compare itemized bills from both against your explanation of benefits.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.govinfo.gov/content/pkg/CFR-2024-title42-vol5/xml/CFR-2024-title42-vol5-sec489-24.xml" target="_blank" rel="noopener">GovInfo &mdash; 42 CFR 489.24, Special responsibilities of Medicare hospitals in emergency cases (EMTALA)</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-149/subpart-B/section-149.110" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 149.110, Preventing surprise medical bills for emergency services</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-149/subpart-E/section-149.410" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 149.410, Balance billing in cases of emergency services</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-147/section-147.136" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 147.136, Internal claims and appeals and external review processes</a></li>
    <li><a href="https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/know-your-rights/insurance" target="_blank" rel="noopener">CMS &mdash; Know your medical bill rights when using insurance</a></li>
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/no-surprises-understand-your-rights-against-surprise-medical-bills" target="_blank" rel="noopener">CMS &mdash; No Surprises: Understand your rights against surprise medical bills (fact sheet, January 3, 2022)</a></li>
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/requirements-related-surprise-billing-part-i-interim-final-rule-comment-period" target="_blank" rel="noopener">CMS &mdash; Requirements Related to Surprise Billing; Part I Interim Final Rule (fact sheet)</a></li>
    <li><a href="https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/find-action-plan/ground-ambulance-bill" target="_blank" rel="noopener">CMS &mdash; Action plan: Ground ambulance bill</a></li>
    <li><a href="https://www.cms.gov/regulations-guidance/advisory-committees/advisory-committee-ground-ambulance-and-patient-billing-gapb" target="_blank" rel="noopener">CMS &mdash; Advisory Committee on Ground Ambulance and Patient Billing (GAPB)</a></li>
    <li><a href="https://www.medicare.gov/coverage/ambulance-services" target="_blank" rel="noopener">Medicare.gov &mdash; Ambulance services</a></li>
    <li><a href="https://www.medicare.gov/coverage/inpatient-hospital-care" target="_blank" rel="noopener">Medicare.gov &mdash; Inpatient hospital care</a></li>
    <li><a href="https://www.govinfo.gov/content/pkg/CFR-2024-title42-vol2/xml/CFR-2024-title42-vol2-sec409-60.xml" target="_blank" rel="noopener">GovInfo &mdash; 42 CFR 409.60, Benefit periods</a></li>
</ul>
""",
})
