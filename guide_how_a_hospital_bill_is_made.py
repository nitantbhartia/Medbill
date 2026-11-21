"""Guide: How a Hospital Bill Gets Made: From Chargemaster to Mailbox."""

from guides import register

register("how-a-hospital-bill-is-made", {
    "title": "How a Hospital Bill Is Made: Chargemaster to Mailbox",
    "meta_description": "How a hospital bill is made, in 9 stops: from registration and the chargemaster to coding, claims, the EOB and collections, and what to ask for at each.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "What is a hospital chargemaster?",
            "a": "Federal price transparency rules define the chargemaster as the list of all individual items and services a hospital keeps for which it has set a charge. The price on that list, before any discounts, is called the gross charge. Insurers usually pay a lower negotiated rate, and many hospitals also set a discounted cash price for people paying on their own.",
        },
        {
            "q": "What is the difference between a UB-04 and a CMS-1500?",
            "a": "The UB-04 (also called Form CMS-1450) is the claim form hospitals and other institutions use, and its electronic version is the 837 institutional claim. The CMS-1500 is the paper form doctors and other non-institutional providers use, and its electronic version is the 837 professional claim. That is one reason you can get a hospital bill and separate doctor bills for the same visit.",
        },
        {
            "q": "Is an explanation of benefits a bill?",
            "a": "No. CMS says an explanation of benefits (EOB) is not a bill. It shows what the provider charged, what your plan allowed and paid, and what you may owe. CMS also says your bill should not be higher than the patient balance on the EOB, and if it is, you should talk to your provider.",
        },
        {
            "q": "How long does a nonprofit hospital have to wait before sending my bill to collections?",
            "a": "Under IRS rules for nonprofit (501(c)(3)) hospitals, the hospital cannot start extraordinary collection actions, such as selling your debt or reporting it to credit bureaus, for at least 120 days after the first bill sent after you leave the hospital. It also has to send written notice at least 30 days before starting those actions, and you have at least 240 days from that first bill to apply for financial assistance. These rules do not cover for-profit hospitals, though some states have their own rules.",
        },
        {
            "q": "What is a payer edit, like NCCI?",
            "a": "A payer edit is an automatic check a payer runs on a claim before paying it. For Medicare, CMS runs the National Correct Coding Initiative (NCCI), which flags code pairs that should not be billed together and service units that look too high for one patient on one day. Private insurers use their own editing rules.",
        },
    ],
    "body": f"""
<p class="lead">A hospital bill is made in stages: your visit is registered, your care is written down, each item is priced from the hospital&rsquo;s master price list (the chargemaster), turned into billing codes, sent to your insurer as a claim, checked, paid or denied, and only then billed to you. A mistake at any stop can ride all the way to your mailbox, so it helps to know what happens at each one and which document to ask for.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#map">The route at a glance</a></li>
        <li><a href="#stop-1">Stop 1: Registration</a></li>
        <li><a href="#stop-2">Stop 2: Your care is documented</a></li>
        <li><a href="#stop-3">Stop 3: Charge capture and the chargemaster</a></li>
        <li><a href="#stop-4">Stop 4: Coding</a></li>
        <li><a href="#stop-5">Stop 5: The claim</a></li>
        <li><a href="#stop-6">Stop 6: Claim scrubbing and payer edits</a></li>
        <li><a href="#stop-7">Stop 7: Adjudication and the EOB</a></li>
        <li><a href="#stop-8">Stop 8: Your patient statement</a></li>
        <li><a href="#stop-9">Stop 9: Follow-up and collections</a></li>
        <li><a href="#what-to-do">What to do with your bill, step by step</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="map">1. The route at a glance</h2>
<p>Each of the nine stops leaves a paper trail. When something looks off, find the stop where it went wrong and ask for that stop&rsquo;s paperwork.</p>

<table>
    <thead>
        <tr><th>Stop</th><th>What happens</th><th>Paper trail you can ask for</th></tr>
    </thead>
    <tbody>
        <tr><td>1. Registration</td><td>Your name, insurance and visit type are entered</td><td>The insurance and demographic info on file</td></tr>
        <tr><td>2. Documentation</td><td>Staff record what was done</td><td>Your medical records</td></tr>
        <tr><td>3. Charge capture</td><td>Each item gets a price from the chargemaster</td><td>An itemized bill</td></tr>
        <tr><td>4. Coding</td><td>Services and diagnoses become codes</td><td>Itemized bill with CPT/HCPCS and revenue codes</td></tr>
        <tr><td>5. Claim</td><td>Codes go to the insurer on a UB-04 or CMS-1500</td><td>A copy of the claim</td></tr>
        <tr><td>6. Scrubbing and edits</td><td>Software checks the claim for code conflicts</td><td>Denial or remark codes</td></tr>
        <tr><td>7. Adjudication</td><td>Insurer decides what to pay</td><td>Explanation of benefits (EOB)</td></tr>
        <tr><td>8. Patient statement</td><td>Hospital bills you for the rest</td><td>The statement and payment history</td></tr>
        <tr><td>9. Follow-up</td><td>Reminders, then possibly collections</td><td>Financial assistance policy and notices</td></tr>
    </tbody>
</table>

<h2 id="stop-1">2. Stop 1: Registration</h2>
<p>Your bill starts at the front desk. Staff enter your name, insurance plan, member ID, and whether you are an inpatient (formally admitted) or an outpatient.</p>
<h3>Where mistakes can creep in</h3>
<p>A typo in your member ID or an old insurance card can send the claim to the wrong place. Then the full charge may land on you.</p>
<h3>What you can ask for</h3>
<p>Ask billing to read back the insurance on your account. If your plan was not billed, see <a href="/guides/hospital-did-not-bill-insurance/">what to do when a hospital didn&rsquo;t bill insurance</a>.</p>

<h2 id="stop-2">3. Stop 2: Your care is documented</h2>
<p>Doctors, nurses and technicians record orders, medicines, tests and supplies. In general, every charge should match something in your chart.</p>
<h3>Where mistakes can creep in</h3>
<p>An order can be canceled but still charged, or a test ordered twice.</p>
<h3>What you can ask for</h3>
<p>Under the HIPAA Privacy Rule (45 CFR 164.524), you generally have a right to see and get a copy of your health records. Comparing records with your bill helps you spot charges for things that did not happen. See <a href="/guides/how-to-request-medical-records/">how to request medical records</a>.</p>

<h2 id="stop-3">4. Stop 3: Charge capture and the chargemaster</h2>
<p>&ldquo;Charge capture&rdquo; matches each service and supply in your record to a line on the hospital&rsquo;s price list. Federal price transparency rules (45 CFR 180.20) define the key terms:</p>
<ul>
    <li><strong>Chargemaster</strong> (also called the charge description master, or CDM): the list of all individual items and services the hospital keeps for which it has set a charge.</li>
    <li><strong>Gross charge</strong>: the chargemaster price, before any discounts.</li>
    <li><strong>Payer-specific negotiated charge</strong>: the rate the hospital agreed to with a particular insurer.</li>
    <li><strong>Discounted cash price</strong>: the charge for someone paying cash.</li>
</ul>
<p>Hospitals must post a file of all their standard charges and a consumer-friendly list of shoppable services (45 CFR 180.40), so you can often look up a price yourself.</p>
<h3>Where mistakes can creep in</h3>
<p>A supply can be scanned twice, a medicine charged at the wrong dose, or a room billed for an extra day. These are the classic <a href="/guides/duplicate-charges-hospital-bills/">duplicate charges</a> and quantity errors.</p>
<h3>What you can ask for</h3>
<p>Ask for an itemized bill listing every charge with a date, description and quantity.</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>Most of what can go wrong at stops 1 through 3 only shows up on an itemized bill. Ask for one first, then <a href="/scan">check your bill free</a> to compare each line with what Medicare pays for the same code.</p></div>

<h2 id="stop-4">5. Stop 4: Coding</h2>
<p>Next, coders translate your care into standard codes:</p>
<ul>
    <li><strong>CPT and HCPCS codes</strong> describe what was done. CPT is maintained by the American Medical Association. HCPCS Level II, maintained by CMS, mostly covers products, supplies and services like ambulance rides. See <a href="/guides/cpt-codes-explained/">CPT codes explained</a>.</li>
    <li><strong>ICD-10 codes</strong> describe why: your diagnosis. ICD-10 has been used for diagnoses since October 1, 2015. See <a href="/guides/icd10-drg-codes/">ICD-10 and DRG codes</a>.</li>
    <li><strong>Revenue codes</strong> are four-digit codes that sort charges by department. Lab tests, for example, use revenue codes 0300 to 0319. See <a href="/guides/hospital-revenue-codes-explained/">hospital revenue codes explained</a>.</li>
</ul>
<h3>Where mistakes can creep in</h3>
<p>A code can describe a bigger service than you got (upcoding), or one procedure can be split into several codes (unbundling). A diagnosis code that doesn&rsquo;t fit can trigger a denial. Our guide to <a href="/guides/upcoding-unbundling-hospital-bills/">upcoding and unbundling</a> shows what each looks like.</p>
<h3>What you can ask for</h3>
<p>Ask for CPT or HCPCS codes next to each line, not just descriptions.</p>

<h2 id="stop-5">6. Stop 5: The claim</h2>
<p>The coded charges go into a claim, a formal payment request to your insurer. There are two kinds:</p>
<ul>
    <li><strong>Institutional claims</strong> come from the hospital itself. The paper version is Form CMS-1450, also known as the UB-04, and the electronic version is the ASC X12 837 institutional claim (often called the 837I). On the UB-04, each line pairs a revenue code (Form Locator 42) with a HCPCS code for outpatient services (Form Locator 44) and a charge (Form Locator 47).</li>
    <li><strong>Professional claims</strong> come from doctors and other non-institutional providers. CMS calls the CMS-1500 the standard paper form for them; the electronic version is the 837 professional claim (often called the 837P).</li>
</ul>
<p>That split is why one ER trip can bring a hospital bill plus separate doctor bills. See <a href="/guides/multiple-bills-one-hospital-visit/">multiple bills from one hospital visit</a>.</p>
<p>For Medicare, a claim for services on or after January 1, 2010 generally must be filed within 1 calendar year after the date of service, with some exceptions (42 CFR 424.44). Private plans set their own deadlines.</p>
<h3>Where mistakes can creep in</h3>
<p>Wrong dates or units can slip in, or the claim may not be sent at all.</p>
<h3>What you can ask for</h3>
<p>Ask for a copy of the claim (a UB-04 for hospital charges). It shows exactly what your insurer saw.</p>

<h2 id="stop-6">7. Stop 6: Claim scrubbing and payer edits</h2>
<p>The hospital&rsquo;s &ldquo;scrubber&rdquo; software checks the claim for missing fields. The payer then runs its own edits.</p>
<p>For Medicare, CMS runs the National Correct Coding Initiative (NCCI). Its procedure-to-procedure (PTP) edits stop payment for code pairs reported together incorrectly, and its medically unlikely edits (MUEs) stop payment when units look wrong. CMS updates them quarterly. Private insurers use their own rules.</p>
<h3>Where mistakes can creep in</h3>
<p>Edits are built for payers, not patients, and miss some problems. If you are uninsured, no insurer edit may look at your charges.</p>
<h3>What you can ask for</h3>
<p>Ask what any denial or remark code means. If you are self-pay, ask whether the bill was checked against standard coding edits.</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>If no insurer reviewed your claim, you are the only check left. Our <a href="/guides/medical-bill-audit-checklist/">medical bill audit checklist</a> walks through the same kinds of checks, line by line.</p></div>

<h2 id="stop-7">8. Stop 7: Adjudication and the EOB</h2>
<p>&ldquo;Adjudication&rdquo; is the insurer deciding what to pay, using its negotiated rate and your deductible and coinsurance. It then sends an explanation of benefits (EOB). CMS says an EOB isn&rsquo;t a bill. It lists provider charges, allowed charges (what the provider will be paid), what the insurer paid, and the patient balance.</p>
<p><strong>Example:</strong> A hospital charges $2,400. The plan&rsquo;s allowed amount is $900. If your deductible is already met and you owe 20% coinsurance, the plan pays $720 (80% of $900) and your patient balance is $180. Whether you can be billed for the $1,500 gap depends on whether the hospital is in your network.</p>
<h3>Where mistakes can creep in</h3>
<p>The hospital may bill you before the insurer finishes, or for more than the EOB says. A denial may have a fixable cause, like a missing code.</p>
<h3>What you can ask for</h3>
<p>Keep every EOB. CMS says your bill should not be higher than the patient balance; if it is, talk to your provider. See <a href="/guides/explanation-of-benefits-eob/">how to read an EOB</a>, and if a claim was denied, <a href="/guides/insurance-claim-denied-what-to-do/">what to do next</a>.</p>

<h2 id="stop-8">9. Stop 8: Your patient statement</h2>
<p>The patient statement shows what the hospital says you owe after insurance. It is often a short summary.</p>
<h3>Where mistakes can creep in</h3>
<p>Payments may not be posted yet, or a fixable denial may be shifted to you.</p>
<h3>What you can ask for</h3>
<p>Ask for the itemized bill, a payment history and the financial assistance policy, and ask in writing for a hold while you review. Our guide on <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a> has wording you can use.</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>Before paying a patient statement, line it up with your EOB and itemized bill. Want a second look? <a href="/scan">Scan your bill free</a> to flag possible duplicates and see each code&rsquo;s Medicare rate.</p></div>

<h2 id="stop-9">10. Stop 9: Follow-up and collections</h2>
<p>Unpaid bills bring reminders, then possibly a collector. For nonprofit hospitals, IRS rules under Section 501(r)(6) set a timeline:</p>
<ul>
    <li>The hospital must hold off on &ldquo;extraordinary collection actions&rdquo; for at least <strong>120 days</strong> after the first bill sent after you leave the hospital. These actions include selling your debt, reporting it to credit bureaus, and legal steps like liens or wage garnishment.</li>
    <li>It must give you written notice at least <strong>30 days</strong> before starting those actions, with a plain-language summary of its financial assistance policy.</li>
    <li>You have at least <strong>240 days</strong> from that first bill to apply for financial assistance.</li>
    <li>If you send a complete application, the hospital must suspend those actions until it decides.</li>
</ul>
<p>These rules apply to nonprofit hospitals only. Some states add their own protections. See <a href="/guides/how-long-before-medical-bill-goes-to-collections/">how long before a medical bill goes to collections</a>.</p>
<h3>Where mistakes can creep in</h3>
<p>An account can go to collections while a dispute, claim or assistance application is still open.</p>
<h3>What you can ask for</h3>
<p>Ask for the financial assistance policy and application, and the date of your first post-discharge bill. If you think your rights were not followed, consider talking to a consumer attorney or legal aid.</p>

<h2 id="what-to-do">11. What to do with your bill, step by step</h2>
<ol>
    <li><strong>Gather the trail.</strong> Statement, EOBs and notices.</li>
    <li><strong>Request the itemized bill with codes.</strong> Ask for CPT/HCPCS and revenue codes on every line.</li>
    <li><strong>Check registration.</strong> Confirm the hospital has the right insurance on file and billed it.</li>
    <li><strong>Compare bill to EOB.</strong> Your balance should not be higher than the EOB&rsquo;s patient balance.</li>
    <li><strong>Compare bill to records.</strong> Look for duplicates, wrong quantities and missing services.</li>
    <li><strong>Ask about financial assistance.</strong> Note your first bill&rsquo;s date to track the 120- and 240-day windows.</li>
    <li><strong>Dispute in writing.</strong> List each line you question, and keep copies. See <a href="/guides/how-to-dispute-a-medical-bill/">how to dispute a medical bill</a>.</li>
</ol>

<h2 id="faq">Frequently asked questions</h2>
<div class="faq-section">
    <div class="faq-item">
        <h3>What is a hospital chargemaster?</h3>
        <p>Federal price transparency rules define the chargemaster as the list of all individual items and services a hospital keeps for which it has set a charge. The price on that list, before any discounts, is called the gross charge. Insurers usually pay a lower negotiated rate, and many hospitals also set a discounted cash price for people paying on their own.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between a UB-04 and a CMS-1500?</h3>
        <p>The UB-04 (also called Form CMS-1450) is the claim form hospitals and other institutions use, and its electronic version is the 837 institutional claim. The CMS-1500 is the paper form doctors and other non-institutional providers use, and its electronic version is the 837 professional claim. That is one reason you can get a hospital bill and separate doctor bills for the same visit.</p>
    </div>
    <div class="faq-item">
        <h3>Is an explanation of benefits a bill?</h3>
        <p>No. CMS says an explanation of benefits (EOB) is not a bill. It shows what the provider charged, what your plan allowed and paid, and what you may owe. CMS also says your bill should not be higher than the patient balance on the EOB, and if it is, you should talk to your provider.</p>
    </div>
    <div class="faq-item">
        <h3>How long does a nonprofit hospital have to wait before sending my bill to collections?</h3>
        <p>Under IRS rules for nonprofit (501(c)(3)) hospitals, the hospital cannot start extraordinary collection actions, such as selling your debt or reporting it to credit bureaus, for at least 120 days after the first bill sent after you leave the hospital. It also has to send written notice at least 30 days before starting those actions, and you have at least 240 days from that first bill to apply for financial assistance. These rules do not cover for-profit hospitals, though some states have their own rules.</p>
    </div>
    <div class="faq-item">
        <h3>What is a payer edit, like NCCI?</h3>
        <p>A payer edit is an automatic check a payer runs on a claim before paying it. For Medicare, CMS runs the National Correct Coding Initiative (NCCI), which flags code pairs that should not be billed together and service units that look too high for one patient on one day. Private insurers use their own editing rules.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>
<ul class="sources-list">
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-E/part-180/subpart-A/section-180.20" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 180.20, Price transparency definitions (chargemaster, gross charge, standard charge)</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-E/part-180/subpart-B/section-180.40" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 180.40, Hospital price transparency general requirements</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.524" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 164.524, Access of individuals to protected health information</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system" target="_blank" rel="noopener">CMS &mdash; Healthcare Common Procedure Coding System (HCPCS)</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/icd-10-codes" target="_blank" rel="noopener">CMS &mdash; ICD-10</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c25.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 25: Completing and Processing the Form CMS-1450 Data Set</a></li>
    <li><a href="https://www.cms.gov/medicare/billing/electronicbillingeditrans/1500" target="_blank" rel="noopener">CMS &mdash; Professional paper claim form (CMS-1500)</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-162/subpart-K/section-162.1102" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 162.1102, Standards for health care claims (ASC X12 837 institutional and professional)</a></li>
    <li><a href="https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-424/subpart-C/section-424.44" target="_blank" rel="noopener">eCFR &mdash; 42 CFR 424.44, Time limits for filing Medicare claims</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits" target="_blank" rel="noopener">CMS &mdash; National Correct Coding Initiative (NCCI) Edits</a></li>
    <li><a href="https://www.cms.gov/medical-bill-rights/help/guides/explanation-of-benefits" target="_blank" rel="noopener">CMS &mdash; How to read a health insurance explanation of benefits</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/billing-and-collections-section-501r6" target="_blank" rel="noopener">IRS &mdash; Billing and Collections, Section 501(r)(6)</a></li>
</ul>
""",
})
