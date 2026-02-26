"""Guide: Your Medical Billing Rights: A State-by-State Overview."""

from guides import register, _embed

register("medical-billing-rights-overview", {
    "title": "Your Medical Billing Rights: A State-by-State Overview",
    "meta_description": "Know your medical billing rights. Federal and state laws protect you from surprise bills, require itemized statements, and limit debt collection. Full overview.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Do I have the right to an itemized medical bill?",
            "a": "Yes. Under federal law, you have the right to request an itemized statement from any healthcare provider. The No Surprises Act reinforced this by requiring providers to give uninsured and self-pay patients a good faith estimate before scheduled services. Most states also have their own itemized bill requirements, with some mandating that hospitals provide itemized bills automatically rather than only on request. Always request a bill with CPT codes and individual line items, not just a summary total."
        },
        {
            "q": "How long does a hospital have to bill me after treatment?",
            "a": "There is no single federal time limit for billing. Time limits vary by state and range from as little as 6 months to as long as 10 years, with most states falling between 2 and 6 years. Many states require prompt billing — California requires providers to bill within 365 days of service for insured patients, while Texas requires initial billing within the first billing cycle after service. If you receive a bill years after treatment, check your state's timely billing laws."
        },
        {
            "q": "Can a hospital sue me for unpaid medical bills?",
            "a": "Yes, hospitals and debt collectors can sue for unpaid medical bills. However, they must file within your state's statute of limitations for debt collection, which ranges from 3 to 10 years depending on the state. Nonprofit hospitals that sue patients without first screening them for financial assistance may be violating IRS Section 501(r) requirements. If you are sued, respond to the lawsuit within the deadline — ignoring it results in a default judgment."
        },
        {
            "q": "What is the No Surprises Act and does it apply to me?",
            "a": "The No Surprises Act is a federal law effective January 1, 2022, that protects patients with private insurance from surprise out-of-network bills in emergency situations and from out-of-network providers at in-network facilities. It also gives uninsured patients the right to a good faith estimate before scheduled services. It applies to most commercial insurance plans but does not apply to Medicare, Medicaid, TRICARE, or VA benefits, which have separate protections."
        },
        {
            "q": "Can medical debt appear on my credit report?",
            "a": "As of 2023, the three major credit bureaus no longer include medical debt under $500 on credit reports, and paid medical collections are removed entirely. Medical debt that goes to collections cannot appear on your credit report for at least one year, giving you time to dispute or resolve it. Some states have additional protections — for example, Colorado and New York prohibit medical debt from appearing on credit reports entirely under state law."
        },
    ],
    "body": f"""
<p class="lead">Patients in the United States have more medical billing protections than most people realize. Between federal laws like the No Surprises Act, EMTALA, and the Fair Debt Collection Practices Act, and a patchwork of state-level protections covering everything from timely billing requirements to charity care mandates, <strong>you have legal rights at every stage of the billing process</strong> — from the moment you receive care through debt collection. The challenge is knowing which rights apply to your situation. This guide maps out the full landscape.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#federal-rights">Federal billing rights every patient has</a></li>
        <li><a href="#no-surprises-act">The No Surprises Act: surprise bill protections</a></li>
        <li><a href="#debt-collection">Medical debt collection rights (FDCPA)</a></li>
        <li><a href="#state-protections">State-level billing protections</a></li>
        <li><a href="#timely-billing">Time limits on medical billing by state</a></li>
        <li><a href="#transparency">Price transparency requirements</a></li>
        <li><a href="#action-steps">How to exercise your billing rights</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="federal-rights">1. Federal billing rights every patient has</h2>

<p>Several federal laws establish baseline protections that apply in every state. These are your foundational rights regardless of where you live or what insurance you have:</p>

<table>
    <thead>
        <tr>
            <th>Federal Law</th>
            <th>What It Protects</th>
            <th>Who It Covers</th>
            <th>Effective Since</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>No Surprises Act</strong></td>
            <td>Bans surprise out-of-network bills for emergency care and at in-network facilities; requires good faith estimates for uninsured patients</td>
            <td>Patients with private insurance; uninsured/self-pay patients</td>
            <td>January 2022</td>
        </tr>
        <tr>
            <td><strong>EMTALA</strong></td>
            <td>Requires hospitals to screen and stabilize anyone who arrives at an ER, regardless of ability to pay or insurance status</td>
            <td>All patients at Medicare-participating hospitals (virtually all hospitals)</td>
            <td>1986</td>
        </tr>
        <tr>
            <td><strong>FDCPA</strong></td>
            <td>Prohibits abusive, deceptive, and unfair debt collection practices; requires validation of debts; limits contact methods and times</td>
            <td>All consumers contacted by third-party debt collectors</td>
            <td>1977</td>
        </tr>
        <tr>
            <td><strong>HIPAA</strong></td>
            <td>Gives patients the right to access their medical records, including billing records; limits how health information is shared</td>
            <td>All patients at covered entities (hospitals, clinics, insurers)</td>
            <td>1996</td>
        </tr>
        <tr>
            <td><strong>IRS Section 501(r)</strong></td>
            <td>Requires nonprofit hospitals to have a written financial assistance policy, publicize it, screen patients before collections, and limit charges for assistance-eligible patients</td>
            <td>Patients at nonprofit (tax-exempt) hospitals</td>
            <td>2010 (ACA)</td>
        </tr>
        <tr>
            <td><strong>Hospital Price Transparency Rule</strong></td>
            <td>Requires hospitals to publish machine-readable files of all standard charges and display prices for 300 shoppable services</td>
            <td>All patients; all hospitals</td>
            <td>January 2021</td>
        </tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Your most powerful federal rights:</strong> You cannot be surprise-billed in an emergency. You are entitled to an itemized bill. Nonprofit hospitals must offer financial assistance before sending you to collections. Debt collectors must validate debts and follow strict rules. These rights apply everywhere in the United States. If you have a bill you suspect violates any of these protections, <a href="/scan">upload it to BillKarma</a> — we will flag surprise charges, coding errors, and overcharges automatically.
</div>

<h2 id="no-surprises-act">2. The No Surprises Act: surprise bill protections</h2>

<p>The No Surprises Act (NSA) is the most significant federal billing protection enacted in the last decade. It covers three main scenarios:</p>

<ul>
    <li><strong>Emergency services:</strong> You cannot be balance-billed by any out-of-network provider during an emergency visit — the ER physician, radiologist, anesthesiologist, or any specialist called in. Your cost-sharing is calculated at in-network rates.</li>
    <li><strong>Non-emergency services at in-network facilities:</strong> If you go to an in-network hospital for scheduled care and are treated by an out-of-network provider you did not choose (common with anesthesiologists, pathologists, and assistant surgeons), you are protected from balance billing.</li>
    <li><strong>Good faith estimates for uninsured patients:</strong> Providers must give uninsured or self-pay patients a written estimate before scheduled services. If the final bill exceeds the estimate by $400 or more, you can initiate a dispute within 120 days.</li>
</ul>

<p>The NSA applies to commercial insurance (employer plans, marketplace plans, individual plans). It does not apply to Medicare, Medicaid, TRICARE, or VA — these programs have their own, separate protections. For a deeper look at how these protections work in practice, see our <a href="/guides/no-surprises-act-explained">full No Surprises Act guide</a>.</p>

{_embed(mode="markup", title="Check if your bill has surprise charges", subtitle="Enter a CPT code and billed amount to compare against in-network benchmarks.", height="420")}

<h2 id="debt-collection">3. Medical debt collection rights (FDCPA)</h2>

<p>If a medical bill goes to a third-party debt collector, the Fair Debt Collection Practices Act gives you these specific protections:</p>

<ul>
    <li><strong>Right to debt validation.</strong> Within 30 days of first contact, you can request written validation of the debt — the original creditor, the amount, and proof that you owe it. The collector must stop collection efforts until they provide validation.</li>
    <li><strong>Limits on contact.</strong> Collectors cannot call before 8 a.m. or after 9 p.m. They cannot contact you at work if you tell them your employer prohibits it. They cannot use abusive language or make threats they cannot legally carry out.</li>
    <li><strong>Right to cease communication.</strong> You can send a written letter telling a collector to stop contacting you. After receiving it, they can only contact you to confirm they will stop or to notify you of a specific legal action.</li>
    <li><strong>No false or misleading statements.</strong> Collectors cannot misrepresent the amount owed, threaten legal action they do not intend to take, or falsely claim to be attorneys or government officials.</li>
    <li><strong>Credit reporting protections.</strong> As of 2023, medical debt under $500 is excluded from credit reports. Paid medical collections are removed entirely. Unpaid medical debt cannot appear on a credit report for at least one year from the date it was sent to collections.</li>
</ul>

<p>For detailed guidance on handling debt collectors, see our <a href="/guides/fdcpa-rights-medical-debt">FDCPA rights guide</a> and <a href="/guides/debt-validation-letter-medical-bills">debt validation letter template</a>.</p>

<h2 id="state-protections">4. State-level billing protections</h2>

<p>Many states have enacted billing protections that go beyond federal law. Here are some of the strongest state-level protections:</p>

<table>
    <thead>
        <tr>
            <th>State</th>
            <th>Key Protection</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>California</strong></td>
            <td>Timely billing + charity care</td>
            <td>Providers must bill insured patients within 365 days; nonprofit hospitals must offer financial assistance to patients under 400% FPL; limits charges for uninsured to Medicare rates</td>
        </tr>
        <tr>
            <td><strong>New York</strong></td>
            <td>Surprise bill ban + credit protections</td>
            <td>State surprise bill law (predates NSA); prohibits medical debt on credit reports; requires hospitals to offer financial assistance</td>
        </tr>
        <tr>
            <td><strong>Texas</strong></td>
            <td>Surprise bill mediation</td>
            <td>State mediation process for surprise out-of-network bills exceeding $500; applies to state-regulated insurance plans</td>
        </tr>
        <tr>
            <td><strong>Colorado</strong></td>
            <td>Medical debt credit ban</td>
            <td>Prohibits medical debt from appearing on consumer credit reports under state law; limits interest on medical debt to 3%</td>
        </tr>
        <tr>
            <td><strong>Illinois</strong></td>
            <td>Charity care mandate</td>
            <td>Nonprofit hospitals must provide free care to patients under 200% FPL and discounted care up to 600% FPL; among the most generous thresholds in the country</td>
        </tr>
        <tr>
            <td><strong>Oregon</strong></td>
            <td>Hospital financial assistance</td>
            <td>All hospitals (including for-profit) must screen patients for financial assistance before pursuing collections; limits charges for qualifying patients</td>
        </tr>
        <tr>
            <td><strong>Maryland</strong></td>
            <td>Rate regulation</td>
            <td>Only state with all-payer hospital rate regulation &mdash; the Health Services Cost Review Commission sets rates that all insurers and hospitals must follow</td>
        </tr>
    </tbody>
</table>

<p>Your state may have additional protections not listed here. Contact your state attorney general's consumer protection division or your state insurance department to find out what specific protections apply where you live. You can also <a href="/hospitals/">check your hospital's billing grade</a> in our directory to see whether it has a track record of compliance with financial assistance and billing transparency rules.</p>

<h2 id="timely-billing">5. Time limits on medical billing by state</h2>

<p>Many states impose time limits on how long a provider has to send you a bill (timely billing or timely filing requirements) and how long they can pursue collection through a lawsuit (statute of limitations on medical debt). These are two different deadlines:</p>

<ul>
    <li><strong>Timely billing:</strong> How long the provider has to send you the initial bill after the date of service. If they miss this window, they may be prohibited from billing you at all. Not all states have specific timely billing laws.</li>
    <li><strong>Statute of limitations:</strong> How long a creditor or collector has to file a lawsuit against you for unpaid medical debt. Once this expires, the debt becomes "time-barred" and cannot be collected through the courts (though the creditor can still attempt voluntary collection). This ranges from 3 to 10 years depending on the state.</li>
</ul>

<p>If you receive a bill that seems unreasonably old, check both deadlines. A bill that arrives three years after service may violate your state's timely billing requirement even if it falls within the statute of limitations for lawsuits. See our <a href="/guides/medical-debt-statute-of-limitations">statute of limitations guide</a> for state-by-state details.</p>

<div class="case-study">
    <h3>Case study: $8,400 ER bill arrives 14 months late in California</h3>
    <p>A patient in California received an $8,400 emergency room bill 14 months after the date of service. The patient had been insured at the time of the visit, but the hospital had failed to bill the insurance company within the insurer's timely filing window (typically 90 to 180 days). Under California law (Health and Safety Code Section 127425), hospitals cannot bill insured patients more than 365 days after service. The patient sent a written response citing the law and noting the bill arrived outside the 365-day window. The hospital withdrew the bill entirely. <strong>Result: $8,400 bill eliminated.</strong></p>
    <p>Have an old or suspicious bill? <a href="/scan">Scan it with BillKarma</a> to check for timing issues, coding errors, and overcharges before you pay.</p>
</div>

<h2 id="transparency">6. Price transparency requirements</h2>

<p>Since January 2021, federal rules have required hospitals to make their prices public. As of 2025, CMS has increased enforcement penalties and compliance rates have improved, though gaps remain:</p>

<ul>
    <li><strong>Machine-readable file:</strong> Every hospital must publish a complete file of standard charges for all items and services, including gross charges, discounted cash prices, payer-specific negotiated rates, and de-identified minimum and maximum rates.</li>
    <li><strong>Shoppable services display:</strong> Hospitals must display prices for at least 300 "shoppable" services in a consumer-friendly format — meaning patients can compare prices before receiving care.</li>
    <li><strong>Insurer price transparency:</strong> The Transparency in Coverage Rule requires health insurers to publish machine-readable files of negotiated rates with in-network providers and allowed amounts for out-of-network providers.</li>
</ul>

<p>In practice, you can use these tools to compare hospital prices before a scheduled procedure and to verify after the fact whether the charges on your bill match the hospital's published rates. If a hospital charges you more than their published rate for your insurance plan, that discrepancy is worth disputing. Use the <a href="/calculator">BillKarma cost calculator</a> to look up Medicare rates for any procedure code and compare them against what you were charged.</p>

<div class="key-takeaway">
    <strong>Use price transparency to your advantage:</strong> Before any scheduled procedure, check the hospital's published prices. After receiving a bill, compare the charges to published rates. Any discrepancy between the published rate and your bill is a basis for dispute. <a href="/scan">Upload your bill to BillKarma</a> to automatically compare your charges against Medicare benchmarks.
</div>

<h2 id="action-steps">7. How to exercise your billing rights</h2>

<ol>
    <li><strong>Always request an itemized bill with CPT codes.</strong> A summary statement is not enough. You need individual line items to identify errors, duplicates, and overcharges. Our <a href="/guides/medical-bill-audit-checklist">12-point audit checklist</a> walks you through exactly what to look for on each line.</li>
    <li><strong>Compare every bill to your Explanation of Benefits.</strong> Your insurer's EOB shows what was billed, what they paid, and what you owe. If the provider's bill does not match the EOB, one of them is wrong.</li>
    <li><strong>Check for No Surprises Act protections.</strong> If you see out-of-network charges from an ER visit or from a provider you did not choose at an in-network facility, cite the NSA and request reprocessing.</li>
    <li><strong>Request debt validation before paying a collector.</strong> If a medical bill goes to collections, send a written validation request within 30 days. Do not pay until the debt is validated with documentation.</li>
    <li><strong>Apply for financial assistance at nonprofit hospitals.</strong> Under 501(r), nonprofit hospitals must have a written financial assistance policy and screen patients before pursuing collections. Apply even if you have insurance — many policies cover the patient-responsibility portion. See our <a href="/guides/hospital-financial-assistance-guide">financial assistance guide</a> for a step-by-step walkthrough.</li>
    <li><strong>Know your state's deadlines.</strong> Check timely billing laws and the statute of limitations for medical debt in your state. An old bill may be uncollectible.</li>
    <li><strong>File complaints when rights are violated.</strong> Report No Surprises Act violations to CMS at cms.gov/nosurprises. Report FDCPA violations to the CFPB at consumerfinance.gov. Report state law violations to your state attorney general.</li>
</ol>

<h2 id="faq">8. Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Do I have the right to an itemized medical bill?</h3>
        <p>Yes. You can request an itemized statement with CPT codes from any healthcare provider. The No Surprises Act also requires providers to give uninsured patients a good faith estimate before scheduled services. Many states require hospitals to provide itemized bills automatically. Always request line-item detail rather than a summary total.</p>
    </div>

    <div class="faq-item">
        <h3>How long does a hospital have to bill me after treatment?</h3>
        <p>Time limits vary by state. California requires billing within 365 days for insured patients. Texas requires initial billing within the first billing cycle. Many states do not have specific timely billing laws, but all have a statute of limitations on debt collection lawsuits (typically 3 to 10 years). See our <a href="/guides/medical-debt-statute-of-limitations">statute of limitations guide</a> for state-specific deadlines.</p>
    </div>

    <div class="faq-item">
        <h3>Can a hospital sue me for unpaid medical bills?</h3>
        <p>Yes, but they must file within your state's statute of limitations. Nonprofit hospitals that sue without first screening for financial assistance may be violating IRS 501(r) requirements. Always respond to a lawsuit within the deadline — ignoring it results in a default judgment. Check whether your hospital is nonprofit in our <a href="/hospitals/">hospital directory</a>, and see our <a href="/guides/medical-debt-lawsuit-defense">lawsuit defense guide</a> for what to do if you are sued.</p>
    </div>

    <div class="faq-item">
        <h3>What is the No Surprises Act and does it apply to me?</h3>
        <p>The No Surprises Act protects patients with private insurance from surprise out-of-network bills in emergencies and from providers they did not choose at in-network facilities. It also gives uninsured patients the right to good faith estimates. It does not apply to Medicare, Medicaid, TRICARE, or VA. See our <a href="/guides/no-surprises-act-explained">full No Surprises Act guide</a> for details.</p>
    </div>

    <div class="faq-item">
        <h3>Can medical debt appear on my credit report?</h3>
        <p>Medical debt under $500 is excluded from credit reports. Paid medical collections are removed entirely. Unpaid medical debt cannot appear for at least one year from the date it was sent to collections. Some states like Colorado and New York ban medical debt from credit reports under state law. See our <a href="/guides/medical-debt-credit-score">medical debt and credit guide</a> for full details.</p>
    </div>
</div>

<h2 id="sources">9. Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Overview and Consumer Resources</a></li>
    <li><a href="#" target="_blank" rel="noopener">Federal Trade Commission: Fair Debt Collection Practices Act &mdash; Full Text and Compliance Guide</a></li>
    <li><a href="#" target="_blank" rel="noopener">IRS: Section 501(r) Requirements for Charitable Hospital Organizations</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: Hospital Price Transparency Rule &mdash; Requirements and Enforcement Updates (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Consumer Financial Protection Bureau: Medical Debt and Credit Reporting &mdash; 2023 Policy Changes</a></li>
    <li><a href="#" target="_blank" rel="noopener">KFF: State Balance Billing Protections &mdash; Survey of State Laws and Regulations</a></li>
    <li><a href="#" target="_blank" rel="noopener">National Consumer Law Center: Medical Debt Collection by State &mdash; Statute of Limitations and Consumer Protections</a></li>
</ul>
""",
})
