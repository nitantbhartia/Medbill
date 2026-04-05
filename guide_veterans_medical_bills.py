"""Guide: Veterans Medical Bill Rights: VA Benefits Explained."""

from guides import register, _embed

register("veterans-medical-bill-rights", {
    "title": "Veterans Medical Bill Rights: VA Benefits Explained",
    "meta_description": "Veterans can get free or low-cost healthcare through the VA. Learn your priority group, copay rates, how to fight wrongful bills, and community care options.",
    "published": "2026-04-04",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Do all veterans get free VA healthcare?",
            "a": "No. Whether you pay copays depends on your VA priority group, which is based on service-connected disability rating, income, and other factors. Veterans in Priority Groups 1\u20136 generally pay no copays or very low copays. Groups 7 and 8 (higher-income veterans with no service-connected disability) pay copays similar to private insurance. Veterans with a 50% or higher service-connected disability rating receive free VA healthcare for all conditions.",
        },
        {
            "q": "Can a non-VA hospital bill me if the VA authorized community care?",
            "a": "No. If the VA authorized your community care visit, the non-VA provider must bill the VA directly \u2014 not you. If you receive a bill from a community care provider, do not pay it. Contact the VA Community Care office at 1-877-881-7618 and provide the authorization number. Under the MISSION Act, veterans are protected from balance billing for VA-authorized community care.",
        },
        {
            "q": "What does the PACT Act cover for veterans?",
            "a": "The PACT Act (2022) expanded VA healthcare to veterans exposed to burn pits, Agent Orange, and other toxic substances. It covers conditions presumed to be caused by toxic exposure, including over 20 cancers (lung, bladder, kidney, and others), respiratory conditions like chronic bronchitis and COPD, and conditions linked to Agent Orange exposure. If you served in a toxic exposure area, you may qualify for free healthcare and disability compensation.",
        },
        {
            "q": "How do I dispute a VA medical bill?",
            "a": "Contact the VA Health Resource Center at 1-866-400-1238 within 30 days of receiving the bill. Explain why you believe the bill is incorrect \u2014 common reasons include incorrect copay charges, bills for service-connected conditions (which should be free), or charges for VA-authorized community care. You can also submit a written dispute to your VA medical center\u2019s Revenue Office. Request a waiver of copay charges if you are experiencing financial hardship.",
        },
        {
            "q": "Can I use VA healthcare and private insurance at the same time?",
            "a": "Yes. Many veterans have both VA healthcare and private insurance (through an employer, Medicare, or Medicaid). The VA may bill your private insurance for treatment of non-service-connected conditions, but you will never owe more than the VA copay amount. If you have Medicare, the VA does not bill Medicare. You can choose to use VA care, private insurance, or both depending on the situation.",
        },
    ],
    "body": f"""
<p class="lead">Over <strong>9 million veterans</strong> are enrolled in VA healthcare, but millions more are eligible and don&rsquo;t know it. The VA provides free or low-cost healthcare to qualifying veterans &mdash; and after the <strong>PACT Act of 2022</strong>, eligibility expanded dramatically for veterans exposed to toxic substances. Yet veterans routinely receive billing errors, wrongful bills from community care providers, and copay charges for conditions that should be free. This guide covers your rights, your benefits, and how to fight back.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#eligibility">VA healthcare eligibility and priority groups</a></li>
        <li><a href="#copays">VA copay rates by priority group</a></li>
        <li><a href="#coverage">What the VA covers vs. doesn&rsquo;t cover</a></li>
        <li><a href="#community-care">Community care and the MISSION Act</a></li>
        <li><a href="#pact-act">PACT Act and toxic exposure coverage</a></li>
        <li><a href="#billing-problems">Common billing problems and how to fight them</a></li>
        <li><a href="#hardship">Financial hardship and copay exemptions</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="eligibility">1. VA healthcare eligibility and priority groups</h2>

<p>To enroll in VA healthcare, you must have served in the active military, naval, or air service and been discharged under conditions other than dishonorable. The VA assigns every enrolled veteran to a <strong>priority group (1 through 8)</strong> based on service-connected disability, income, and other factors. Your priority group determines your copay obligations and how quickly you can access care.</p>

<table>
    <thead>
        <tr><th>Priority group</th><th>Who qualifies</th><th>Copay status</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>1</strong></td><td>50%+ service-connected disability; unemployable due to service-connected condition</td><td>No copays for any care</td></tr>
        <tr><td><strong>2</strong></td><td>30&ndash;40% service-connected disability</td><td>No copays for any care</td></tr>
        <tr><td><strong>3</strong></td><td>10&ndash;20% service-connected disability; former POWs; Purple Heart recipients; discharge for disability</td><td>No copays for any care</td></tr>
        <tr><td><strong>4</strong></td><td>Catastrophically disabled (regardless of service connection)</td><td>No copays for any care</td></tr>
        <tr><td><strong>5</strong></td><td>Low-income veterans below the VA income threshold; pension recipients</td><td>No copays for most care</td></tr>
        <tr><td><strong>6</strong></td><td>Toxic exposure veterans (PACT Act); Gulf War, Vietnam, WWII service in specific locations; Project 112/SHAD</td><td>No copays for exposure-related care</td></tr>
        <tr><td><strong>7</strong></td><td>Veterans with income above the VA threshold but below the geographic income limit; agreeing to pay copays</td><td>Reduced copays</td></tr>
        <tr><td><strong>8</strong></td><td>Veterans with income above the geographic income limit; agreeing to pay copays</td><td>Full copays</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Key point:</strong> All veterans with <strong>any service-connected disability rating</strong> (even 0%) receive free care for that specific condition. Veterans rated 50% or higher receive free care for <em>all</em> conditions, service-connected or not.
</div>

<h2 id="copays">2. VA copay rates by priority group</h2>

<p>For veterans in Priority Groups 7 and 8, the VA charges copays that are significantly lower than private insurance costs. Here are the 2026 rates:</p>

<table>
    <thead>
        <tr><th>Service type</th><th>Priority Group 1&ndash;6</th><th>Priority Group 7</th><th>Priority Group 8</th></tr>
    </thead>
    <tbody>
        <tr><td>Primary care visit</td><td>$0</td><td>$15</td><td>$50</td></tr>
        <tr><td>Specialty care visit</td><td>$0</td><td>$50</td><td>$50</td></tr>
        <tr><td>Inpatient stay (per day)</td><td>$0</td><td>$0 for first 90 days*</td><td>Capped at $1,920/year</td></tr>
        <tr><td>Outpatient medications (Tier 1)</td><td>$0</td><td>$5</td><td>$9</td></tr>
        <tr><td>Outpatient medications (Tier 2)</td><td>$0</td><td>$8</td><td>$13</td></tr>
        <tr><td>Outpatient medications (Tier 3)</td><td>$0</td><td>$11</td><td>$17</td></tr>
        <tr><td>Urgent care (VA)</td><td>$0</td><td>$30</td><td>$50</td></tr>
        <tr><td>Emergency care (VA)</td><td>$0</td><td>$50</td><td>$50</td></tr>
    </tbody>
</table>

<p><small>*Group 7 veterans do not pay inpatient copays for the first 90 days; they pay a small daily rate thereafter. Annual medication copay cap for Groups 7&ndash;8 is $700.</small></p>

<div class="case-study">
    <h3>Case study: VA vs. private insurance costs</h3>
    <p>Robert, a 58-year-old Army veteran with a 20% service-connected disability (Priority Group 3), needed knee replacement surgery. At a private hospital with his employer&rsquo;s insurance, his estimated out-of-pocket cost was <strong>$6,800</strong> (deductible plus coinsurance). Through the VA, the surgery was performed at no cost &mdash; <strong>$0 copay</strong>. For veterans in higher priority groups, even the copay amounts pale in comparison to private insurance costs.</p>
</div>

<h2 id="coverage">3. What the VA covers vs. doesn&rsquo;t cover</h2>

<p>The VA provides a comprehensive medical benefits package:</p>

<h3>Covered services</h3>

<ul>
    <li>Preventive care (screenings, immunizations, health counseling)</li>
    <li>Primary care and specialist visits</li>
    <li>Inpatient and outpatient surgery</li>
    <li>Mental health and substance use disorder treatment</li>
    <li>Prescription medications</li>
    <li>Emergency care (at VA and non-VA facilities)</li>
    <li>Prosthetics, orthotics, and assistive devices</li>
    <li>Home healthcare and skilled nursing</li>
    <li>Physical, occupational, and speech therapy</li>
    <li>Audiology and hearing aids</li>
    <li>Vision care (for some veterans)</li>
    <li>Dental care (limited &mdash; see below)</li>
    <li>Caregiver support programs</li>
    <li>Telehealth services</li>
</ul>

<h3>Limited or not covered</h3>

<ul>
    <li><strong>Dental care</strong>: Only free for veterans with 100% disability, service-connected dental conditions, former POWs, or those enrolled within 180 days of discharge. Others can purchase a VA dental insurance plan (VADIP) starting at ~$14/month.</li>
    <li><strong>Long-term custodial care</strong>: Not guaranteed; availability depends on resources.</li>
    <li><strong>Cosmetic surgery</strong>: Not covered unless related to a service-connected condition.</li>
    <li><strong>Fertility treatments</strong>: IVF covered only for veterans with service-connected conditions affecting fertility.</li>
</ul>

<h2 id="community-care">4. Community care and the MISSION Act</h2>

<p>The <strong>VA MISSION Act (2018)</strong> expanded veterans&rsquo; ability to receive care from non-VA providers paid for by the VA. This is called &ldquo;community care,&rdquo; and it applies when:</p>

<ul>
    <li>The VA cannot provide the service you need</li>
    <li>The VA cannot schedule an appointment within <strong>20 days</strong> (for primary/mental health care) or <strong>28 days</strong> (for specialty care)</li>
    <li>You would need to drive more than <strong>30 minutes</strong> to a VA facility (for primary care) or <strong>60 minutes</strong> (for specialty care)</li>
    <li>It is in your best medical interest (as determined by your VA provider)</li>
    <li>The VA facility does not meet quality standards for that service</li>
</ul>

<div class="key-takeaway">
    <strong>Critical rule:</strong> Community care must be <strong>pre-authorized by the VA</strong>. If you go to a non-VA provider without VA authorization, the VA will not pay the bill and you will be responsible for the full amount. The only exception is emergency care, where different rules apply.
</div>

<h3>How community care billing works</h3>

<ol>
    <li>Your VA provider determines you need community care and submits a referral.</li>
    <li>The VA issues an authorization and sends it to an approved community care provider.</li>
    <li>You receive care from the community provider.</li>
    <li>The provider bills the <strong>VA directly</strong> &mdash; not you.</li>
    <li>You may owe a VA copay (based on your priority group), but never the provider&rsquo;s full charge.</li>
</ol>

<p>If a community care provider sends you a bill, <strong>do not pay it</strong>. This is a common problem. See the billing disputes section below for steps to resolve it.</p>

<h2 id="pact-act">5. PACT Act and toxic exposure coverage</h2>

<p>The <strong>Sergeant First Class Heath Robinson Honoring Our Promise to Address Comprehensive Toxics (PACT) Act</strong>, signed in 2022, is the largest expansion of VA healthcare in decades. It extends eligibility and benefits to veterans exposed to:</p>

<ul>
    <li><strong>Burn pits</strong> (Iraq, Afghanistan, Southwest Asia &mdash; post-9/11 service)</li>
    <li><strong>Agent Orange</strong> (Vietnam, Thailand, and other locations)</li>
    <li><strong>Radiation</strong> (nuclear weapons testing, Hiroshima/Nagasaki cleanup)</li>
    <li><strong>Contaminated water at Camp Lejeune</strong> (1953&ndash;1987)</li>
    <li><strong>Other toxic substances</strong> (Project 112/SHAD, Panama Canal Zone, etc.)</li>
</ul>

<h3>Conditions covered as presumptive under the PACT Act</h3>

<p>If you served in a qualifying location and develop one of these conditions, the VA <strong>presumes</strong> it was caused by your service &mdash; no need to prove the connection:</p>

<table>
    <thead>
        <tr><th>Exposure type</th><th>Presumptive conditions</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Burn pits / airborne hazards</strong></td>
            <td>Lung cancer, kidney cancer, bladder cancer, melanoma, reproductive cancers, pancreatic cancer, brain cancer, head/neck cancers, lymphoma, respiratory conditions (COPD, chronic bronchitis, constrictive bronchiolitis), and others</td>
        </tr>
        <tr>
            <td><strong>Agent Orange</strong></td>
            <td>Bladder cancer, hypertension, Parkinson&rsquo;s disease, Type 2 diabetes, ischemic heart disease, non-Hodgkin&rsquo;s lymphoma, prostate cancer, soft tissue sarcoma, and 12+ additional conditions</td>
        </tr>
        <tr>
            <td><strong>Camp Lejeune water</strong></td>
            <td>Kidney cancer, liver cancer, non-Hodgkin&rsquo;s lymphoma, bladder cancer, leukemia, multiple myeloma, Parkinson&rsquo;s disease, and others</td>
        </tr>
        <tr>
            <td><strong>Radiation</strong></td>
            <td>Various cancers including leukemia, thyroid cancer, breast cancer, lung cancer, and others</td>
        </tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Action step:</strong> If you served in Iraq, Afghanistan, or other toxic exposure locations and have not enrolled in VA healthcare, <a href="https://www.va.gov/health-care/apply/application/introduction" target="_blank" rel="noopener noreferrer">apply now through the VA website</a>. The PACT Act removed the 10-year enrollment window for post-9/11 combat veterans, meaning you can enroll at any time.
</div>

<div class="case-study">
    <h3>Case study: PACT Act coverage saves $47,000</h3>
    <p>David, an Army veteran who served in Iraq from 2005 to 2007, was diagnosed with kidney cancer at age 42. His private insurance quoted him <strong>$47,000 in out-of-pocket costs</strong> for surgery and treatment. A veterans service organization helped David enroll in VA healthcare under the PACT Act. Because kidney cancer is a presumptive condition for burn pit exposure, the VA covered <strong>100% of his treatment at zero cost</strong> and approved a service-connected disability rating that provides monthly compensation.</p>
</div>

<h2 id="billing-problems">6. Common billing problems and how to fight them</h2>

<p>Veterans face several unique billing issues. Here are the most common and how to resolve each one:</p>

<h3>Problem 1: Bill from a community care provider</h3>

<p>This is the most frequent issue. A non-VA provider treats you under community care authorization, then bills you directly instead of the VA.</p>

<p><strong>Solution:</strong></p>
<ol>
    <li>Do not pay the bill.</li>
    <li>Find your community care authorization number (check your VA records or call your VA medical center).</li>
    <li>Call the VA Community Care office at <strong>1-877-881-7618</strong>.</li>
    <li>Provide the authorization number and the bill details.</li>
    <li>Ask the VA to contact the provider and process payment.</li>
    <li>Send the provider a letter (keep a copy) stating the VA authorized the care and the provider must bill the VA, not you.</li>
</ol>

<h3>Problem 2: Copay charged for a service-connected condition</h3>

<p>You should never be charged a copay for treatment of a service-connected condition, regardless of your priority group.</p>

<p><strong>Solution:</strong></p>
<ol>
    <li>Call the VA billing office at <strong>1-866-400-1238</strong>.</li>
    <li>Reference your service-connected disability rating and the condition treated.</li>
    <li>Ask them to reclassify the visit as service-connected and remove the copay.</li>
    <li>If unresolved, file a written dispute with your VA medical center&rsquo;s Revenue Utilization Office.</li>
</ol>

<h3>Problem 3: Balance billing from a non-VA emergency room</h3>

<p>If you go to a non-VA emergency room, the VA may cover the cost, but the ER may try to bill you for the balance between their charges and what the VA pays.</p>

<p><strong>Solution:</strong></p>
<ol>
    <li>Notify the VA within <strong>72 hours</strong> of the emergency visit (call 1-844-724-7842).</li>
    <li>Under federal law, once the VA agrees to pay, the non-VA provider must accept the VA&rsquo;s payment as payment in full.</li>
    <li>If you receive a balance bill, send the provider a copy of the VA payment authorization and cite <strong>38 U.S.C. &sect; 1725</strong> (the VA emergency care statute).</li>
    <li>File a complaint with your state attorney general if the provider persists.</li>
</ol>

<p>For general guidance on disputing any medical bill, see our <a href="/guides/how-to-dispute-a-medical-bill">complete guide to disputing medical bills</a> and our <a href="/guides/medical-billing-rights-overview">overview of medical billing rights</a>.</p>

<h3>Problem 4: Bill for care you thought was VA-authorized</h3>

<p>Sometimes veterans believe they have community care authorization when they don&rsquo;t, or the authorization expires before treatment is complete.</p>

<p><strong>Solution:</strong></p>
<ol>
    <li>Contact your VA Patient Advocate at your local VA medical center.</li>
    <li>Explain the situation and ask them to review whether authorization should have been granted.</li>
    <li>If the VA determines the care was medically necessary and should have been authorized, they may agree to pay retroactively.</li>
    <li>If the VA will not pay, negotiate directly with the provider &mdash; ask for a discount or payment plan. <a href="/scan">Upload the bill to BillKarma</a> to check for overcharges before negotiating.</li>
</ol>

<div class="key-takeaway">
    <strong>Important:</strong> Keep records of <em>everything</em> &mdash; authorization numbers, phone call dates and names, letters sent and received. The VA bureaucracy can be slow, and documentation is your best protection.
</div>

<h2 id="hardship">7. Financial hardship and copay exemptions</h2>

<p>If you are a veteran in Priority Group 7 or 8 and cannot afford your VA copays, you have options:</p>

<h3>Hardship determination</h3>

<p>You can request a <strong>hardship determination</strong> from the VA if your income has dropped or your expenses have increased since you enrolled. The VA will reassess your financial situation and may move you to a lower priority group with reduced or eliminated copays. Common qualifying situations include:</p>

<ul>
    <li>Job loss or reduced income</li>
    <li>Large medical expenses not covered by the VA</li>
    <li>Bankruptcy</li>
    <li>Natural disaster or emergency</li>
</ul>

<h3>Copay waiver (write-off)</h3>

<p>If you owe VA copays you cannot pay, you can request a <strong>copay waiver</strong> using <strong>VA Form 5655</strong> (Financial Status Report). The VA will review your income, expenses, and assets to determine if collecting the debt would cause undue financial hardship. If approved, the VA will write off the debt entirely.</p>

<h3>Copay repayment plans</h3>

<p>If you don&rsquo;t qualify for a waiver but cannot pay the full amount, the VA offers repayment plans with no interest. Contact the VA Health Resource Center at <strong>1-866-400-1238</strong> to set one up. The VA cannot send your debt to collections if you are on an active repayment plan.</p>

<div class="case-study">
    <h3>Case study: Copay waiver approved after job loss</h3>
    <p>Linda, a Navy veteran in Priority Group 7, had accumulated <strong>$1,850 in VA copays</strong> after a series of specialty visits. When she lost her job, she submitted VA Form 5655 documenting her reduced income and increased expenses. The VA approved a full copay waiver within 60 days, reducing her balance to <strong>$0</strong>. She was also reassigned to Priority Group 5 (low income), eliminating future copays until her income increased.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Do all veterans get free VA healthcare?</h3>
        <p>No. Whether you pay copays depends on your VA priority group, which is based on service-connected disability rating, income, and other factors. Veterans in Priority Groups 1&ndash;6 generally pay no copays or very low copays. Groups 7 and 8 (higher-income veterans with no service-connected disability) pay copays similar to &mdash; but lower than &mdash; private insurance. Veterans with a <strong>50% or higher</strong> service-connected disability rating receive free VA healthcare for all conditions.</p>
    </div>
    <div class="faq-item">
        <h3>Can a non-VA hospital bill me if the VA authorized community care?</h3>
        <p>No. If the VA authorized your community care visit, the non-VA provider must bill the VA directly &mdash; not you. If you receive a bill from a community care provider, do not pay it. Contact the VA Community Care office at <strong>1-877-881-7618</strong> and provide the authorization number. Under the MISSION Act, veterans are protected from balance billing for VA-authorized community care.</p>
    </div>
    <div class="faq-item">
        <h3>What does the PACT Act cover for veterans?</h3>
        <p>The PACT Act expanded VA healthcare to veterans exposed to burn pits, Agent Orange, and other toxic substances. It covers conditions presumed to be caused by toxic exposure, including over 20 cancers, respiratory conditions like COPD and chronic bronchitis, and conditions linked to Agent Orange. If you served in a toxic exposure area, you may qualify for free healthcare and disability compensation.</p>
    </div>
    <div class="faq-item">
        <h3>How do I dispute a VA medical bill?</h3>
        <p>Contact the VA Health Resource Center at <strong>1-866-400-1238</strong> within 30 days of receiving the bill. Explain why you believe the bill is incorrect &mdash; common reasons include incorrect copay charges, bills for service-connected conditions (which should be free), or charges for VA-authorized community care. You can also submit a written dispute to your VA medical center&rsquo;s Revenue Office. Request a waiver if you are experiencing financial hardship.</p>
    </div>
    <div class="faq-item">
        <h3>Can I use VA healthcare and private insurance at the same time?</h3>
        <p>Yes. Many veterans have both VA healthcare and private insurance (through an employer, Medicare, or Medicaid). The VA may bill your private insurance for treatment of non-service-connected conditions, but you will never owe more than the VA copay amount. If you have Medicare, the VA does not bill Medicare. You can choose to use VA care, private insurance, or both depending on the situation.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.va.gov/health-care/eligibility/" target="_blank" rel="noopener noreferrer">VA.gov &mdash; Health Care Eligibility</a></li>
    <li><a href="https://www.va.gov/health-care/copay-rates/" target="_blank" rel="noopener noreferrer">VA.gov &mdash; VA Health Care Copay Rates</a></li>
    <li><a href="https://www.va.gov/COMMUNITYCARE/programs/veterans/index.asp" target="_blank" rel="noopener noreferrer">VA.gov &mdash; Community Care Programs for Veterans</a></li>
    <li><a href="https://www.va.gov/resources/the-pact-act-and-your-va-benefits/" target="_blank" rel="noopener noreferrer">VA.gov &mdash; The PACT Act and Your VA Benefits</a></li>
    <li><a href="https://www.congress.gov/bill/117th-congress/house-bill/3967" target="_blank" rel="noopener noreferrer">Congress.gov &mdash; PACT Act of 2022 (H.R. 3967)</a></li>
    <li><a href="https://www.va.gov/COMMUNITYCARE/programs/veterans/Emergency-Care.asp" target="_blank" rel="noopener noreferrer">VA.gov &mdash; Emergency Care Reimbursement</a></li>
</ul>
""",
})
