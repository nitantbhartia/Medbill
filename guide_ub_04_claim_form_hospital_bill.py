"""Guide: UB-04 Form: How to Get the Most Detailed Hospital Bill."""

from guides import register

register("ub-04-claim-form-hospital-bill", {
    "title": "UB-04 Form: How to Get the Most Detailed Hospital Bill",
    "meta_description": "The UB-04 is the claim a hospital sends your insurer, with codes, units and dates for every charge. Here is how to ask for it and what to check.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "What is a UB-04 form?",
            "a": "The UB-04, also called the CMS-1450, is the standard claim form hospitals and other institutional providers use to bill Medicare and most state Medicaid agencies. It lists codes, units, dates, charges, diagnoses and the payer for your visit.",
        },
        {
            "q": "Is a UB-04 the same as an itemized bill?",
            "a": "No. An itemized bill is a list of charges prepared for you, and its layout varies by hospital. The UB-04 is the claim sent to your insurer, in standard fields. Having both is useful.",
        },
        {
            "q": "Do I have a legal right to get my UB-04?",
            "a": "The HIPAA Privacy Rule gives you a right to copies of the billing records in your designated record set (45 CFR 164.501 and 164.524). A provider does not have to create new documents, so if the hospital keeps no UB-04 image, ask for the claim data as submitted.",
        },
        {
            "q": "How long does the hospital have to send it, and can it charge me?",
            "a": "It must act within 30 calendar days of receiving your request, with one extension of up to 30 days if it tells you in writing why. Fees are limited to reasonable, cost-based copying costs, not search and retrieval.",
        },
        {
            "q": "Can the hospital refuse because I have not paid my bill?",
            "a": "No. HHS guidance says a covered entity may not withhold or deny access to your health information because you have not paid for the care. It may still charge the allowed copy fee.",
        },
        {
            "q": "What should I do with the UB-04 once I have it?",
            "a": "Compare it to your Explanation of Benefits (EOB) and itemized bill: dates, payer, codes, units and the total line. Ask the billing office in writing about anything that does not match.",
        },
    ],
    "body": f"""
<p class="lead">If your hospital bill is a one-line summary or a vague list of charges, ask the hospital for a copy of your UB-04 claim form. The UB-04 is the claim the hospital sent your insurance company, and it shows the billing codes, units, dates and charges for each line, in a standard layout. HIPAA gives you a right to your billing records. Here is how to ask and what to check.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-ub04">What the UB-04 (CMS-1450) is</a></li>
        <li><a href="#three-documents">Patient statement vs. itemized bill vs. UB-04</a></li>
        <li><a href="#fields">The fields to read, and what to check</a></li>
        <li><a href="#your-right">Your right to your billing records</a></li>
        <li><a href="#how-to-ask">How to ask for your UB-04, step by step</a></li>
        <li><a href="#sample-request">Sample request wording</a></li>
        <li><a href="#how-to-use">How to use it: compare to your EOB</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-ub04">1. What the UB-04 (CMS-1450) is</h2>

<p>The UB-04 is the standard claim form for <strong>institutional providers</strong> &mdash; hospitals, skilled nursing facilities, home health agencies and similar facilities. CMS (the Centers for Medicare &amp; Medicaid Services) calls it the CMS-1450. The form itself is designed by the National Uniform Billing Committee (NUBC), not by CMS.</p>

<p>CMS says the form is used to bill Medicare and most state Medicaid agencies. For Medicare, paper is for providers with a waiver from the electronic claims requirement, so most claims travel electronically. Either way, the hospital holds the same claim data.</p>

<p>The UB-04 covers the facility&rsquo;s own charges. If you also got separate bills from a doctor&rsquo;s group for their professional services, those are not on the hospital&rsquo;s UB-04.</p>

<h2 id="three-documents">2. Patient statement vs. itemized bill vs. UB-04</h2>

<table>
    <thead>
        <tr>
            <th>Document</th>
            <th>Who it is for</th>
            <th>What it usually shows</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Patient statement (summary bill)</td>
            <td>You</td>
            <td>Total charges, insurance payments and adjustments, and the balance you owe. Often few or no line details.</td>
        </tr>
        <tr>
            <td>Itemized bill</td>
            <td>You</td>
            <td>A list of each charge with a description and price. The layout and level of detail differ from hospital to hospital, and some do not show billing codes.</td>
        </tr>
        <tr>
            <td>UB-04 / claim</td>
            <td>Your insurer (Medicare, Medicaid or a private plan)</td>
            <td>Standard fields: type of bill, dates, revenue codes, HCPCS/CPT codes, units, charges per line, total charges, diagnosis codes and the payer.</td>
        </tr>
    </tbody>
</table>

<p>The UB-04 is <em>what your insurer was asked to pay for</em>. Your EOB (Explanation of Benefits) is the insurer&rsquo;s answer to it.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>A summary bill tells you what you owe. The UB-04 tells you what was billed and why, line by line. If you have not asked for an itemized bill yet, start with our guide on <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a>, then ask for the UB-04 too.</p>
</div>

<h2 id="fields">3. The fields to read, and what to check</h2>

<p>Every box on the UB-04 is called a <strong>form locator</strong>, or FL. CMS&rsquo;s Medicare Claims Processing Manual, Chapter 25, explains each one. You do not need to read all of them. These are the ones that matter most when you are checking a bill.</p>

<table>
    <thead>
        <tr>
            <th>Field (form locator)</th>
            <th>What it means</th>
            <th>What to check</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>FL 3a &ndash; Patient control number</td>
            <td>The hospital&rsquo;s account number for this bill</td>
            <td>Matches the account number on your statement</td>
        </tr>
        <tr>
            <td>FL 4 &ndash; Type of bill</td>
            <td>A four-digit code. After a leading zero, the digits show the type of facility, the type of care, and where this bill falls in the sequence of bills for that stay or visit (the &ldquo;frequency&rdquo;).</td>
            <td>If the hospital sent more than one bill for your visit, compare the last digit and ask which claim is final</td>
        </tr>
        <tr>
            <td>FL 6 &ndash; Statement covers period</td>
            <td>First and last dates included on this bill</td>
            <td>Dates match when you were actually there</td>
        </tr>
        <tr>
            <td>FL 12 &ndash; Admission date; FL 17 &ndash; Discharge status</td>
            <td>The inpatient admission date and a code for your status as of the &ldquo;through&rdquo; date</td>
            <td>Admission date is right, and you were actually admitted (not kept under observation as an outpatient)</td>
        </tr>
        <tr>
            <td>FL 42 &ndash; Revenue code</td>
            <td>A four-digit code for the hospital department or type of charge. For example, CMS lists revenue codes 0300&ndash;0319 as laboratory. Code 0001 marks the total line.</td>
            <td>Departments make sense for your visit (see <a href="/guides/hospital-revenue-codes-explained/">hospital revenue codes explained</a>)</td>
        </tr>
        <tr>
            <td>FL 44 &ndash; HCPCS/rates</td>
            <td>For outpatient services, the HCPCS or CPT code for the procedure. On inpatient bills, the room rate.</td>
            <td>Each code matches a service you received (see <a href="/guides/what-are-cpt-codes/">what are CPT codes</a>)</td>
        </tr>
        <tr>
            <td>FL 45 &ndash; Service date</td>
            <td>The date of each line, required on outpatient bills</td>
            <td>No service dated on a day you were not there</td>
        </tr>
        <tr>
            <td>FL 46 &ndash; Units of service</td>
            <td>How many: days in a room, or how many times a coded procedure was done</td>
            <td>Units are not higher than what happened (for example, one scan billed as two)</td>
        </tr>
        <tr>
            <td>FL 47 &ndash; Total charges; FL 48 &ndash; Non-covered charges</td>
            <td>Charges for each line, with the overall sum on the 0001 line. Non-covered charges are listed separately.</td>
            <td>The 0001 total matches the &ldquo;amount billed&rdquo; on your EOB</td>
        </tr>
        <tr>
            <td>FL 50 &ndash; Payer</td>
            <td>The insurer billed. Line A is primary, B and C are secondary and tertiary.</td>
            <td>Right insurer, in the right order if you have more than one plan</td>
        </tr>
        <tr>
            <td>FL 67 &ndash; Principal diagnosis; FL 67A&ndash;Q &ndash; Other diagnoses</td>
            <td>ICD-10 diagnosis codes for why you were treated</td>
            <td>Diagnoses describe your actual condition (see <a href="/guides/icd10-drg-codes/">ICD-10 and DRG codes</a>)</td>
        </tr>
        <tr>
            <td>FL 74 &ndash; Principal procedure</td>
            <td>Inpatient procedure code and date. Not used on outpatient claims.</td>
            <td>The procedure listed is the one you had</td>
        </tr>
    </tbody>
</table>

<p><strong>HCPCS</strong> codes are Medicare&rsquo;s procedure and supply codes; <strong>CPT codes</strong> (five-digit service codes) are part of that set.</p>

<h2 id="your-right">4. Your right to your billing records</h2>

<p>The HIPAA Privacy Rule gives you a right to inspect and get a copy of your health information held in a <strong>designated record set</strong> (45 CFR 164.524). The rule defines that term in 45 CFR 164.501 to include &ldquo;the medical records and billing records about individuals&rdquo; kept by or for a health care provider. For health plans, it includes their enrollment, payment and claims records.</p>

<p>The HHS Office for Civil Rights (OCR), which enforces HIPAA, says this covers billing, payment and claims records. How a request works:</p>

<ul>
    <li><strong>Written requests.</strong> The hospital may require you to ask in writing, and may ask you to use its own form, if it tells you so.</li>
    <li><strong>30 days.</strong> The hospital must act no later than 30 calendar days after it gets your request. It may take one extension of up to 30 more days, but only if, within the first 30 days, it gives you a written reason for the delay and the date it will finish.</li>
    <li><strong>Format.</strong> You can ask for an electronic copy of records kept electronically.</li>
    <li><strong>Fees.</strong> The hospital may charge only a reasonable, cost-based fee for copying labor, supplies and postage. It may not charge for searching for or retrieving records. OCR says a provider may charge a flat fee of up to $6.50 for electronic copies of records kept electronically, and that this flat fee is an option, not a cap.</li>
    <li><strong>Unpaid bills.</strong> OCR says a provider may not withhold or deny access because you have not paid for your care.</li>
    <li><strong>Denials.</strong> A denial must be in writing, in plain language, and explain how to file a complaint with the hospital or with OCR.</li>
</ul>

<p>One limit: OCR says a provider does not have to create new information. If the hospital keeps no printed UB-04, ask for the claim data it sent in whatever readable form it has.</p>

<p>Your insurer&rsquo;s claims records are in its designated record set too, so you can also ask your insurer for the claim it received.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Your billing records are part of your HIPAA right of access, with a 30-day clock and limits on fees. For more on how that right works with your full chart, read our guide to <a href="/guides/medical-records-rights/">your medical records rights</a>.</p>
</div>

<h2 id="how-to-ask">5. How to ask for your UB-04, step by step</h2>

<ol>
    <li><strong>Find the right office.</strong> Call the number on your statement and ask whether billing or medical records handles claim copies, and whether there is a required form.</li>
    <li><strong>Gather your details.</strong> Name, date of birth, account number, dates of service and insurer.</li>
    <li><strong>Ask in writing.</strong> Use the hospital&rsquo;s form if it has one, plus a letter like the sample below. Ask for the itemized bill at the same time.</li>
    <li><strong>Keep proof.</strong> Send it by portal, email, fax or certified mail, and note the date it was received.</li>
    <li><strong>Mark your calendar.</strong> Count 30 calendar days from receipt. If you get nothing and no written extension notice, follow up in writing and cite 45 CFR 164.524.</li>
</ol>

<h2 id="sample-request">6. Sample request wording</h2>

<blockquote>
<p>To: Patient Financial Services / Health Information Management<br>
Re: Request for copies of billing records under 45 CFR 164.524<br>
Patient: [Full name], date of birth [MM/DD/YYYY]<br>
Account number: [number] &nbsp; Dates of service: [dates]</p>
<p>I am requesting a copy of the billing records in my designated record set for the dates of service above, including:</p>
<p>1. A copy of each UB-04 (CMS-1450) claim submitted to any payer for this account, including any corrected or replacement claims, or the claim data as submitted if a UB-04 image is not kept.<br>
2. An itemized statement of all charges, with revenue codes, HCPCS/CPT codes, units and service dates.</p>
<p>Please send these electronically to [email or portal], or by mail to [address]. Please tell me in advance about any fee. I understand the HIPAA Privacy Rule requires a response within 30 days of receipt.</p>
<p>Thank you,<br>[Name, phone, signature, date]</p>
</blockquote>

<p>If a billing dispute turns into a legal question, consider talking to a consumer attorney or legal aid.</p>

<h2 id="how-to-use">7. How to use it: compare to your EOB</h2>

<p>Lay the UB-04 next to your EOB and itemized bill.</p>

<ol>
    <li><strong>Match the claim.</strong> The dates (FL 6), payer (FL 50) and 0001 total should match the claim on your EOB. If not, ask which claim is final.</li>
    <li><strong>Check dates line by line.</strong> Every service date (FL 45) should fall on a day you were at the hospital.</li>
    <li><strong>Check units.</strong> Look for units (FL 46) that seem high for what happened. Example: if a line shows 2 units of a scan at $1,200 each, that line totals $2,400. If you had one scan, that is a discrepancy worth asking about.</li>
    <li><strong>Check codes.</strong> Look up unfamiliar codes, and watch for the same code twice on one date.</li>
    <li><strong>Check admission status.</strong> If you thought you were an outpatient but FL 12 shows an inpatient admission date, ask the hospital to explain.</li>
    <li><strong>Check diagnoses.</strong> If a code does not describe your condition, ask about it.</li>
    <li><strong>Write it down.</strong> List each question with the line, code, date and amount, and send it to billing in writing.</li>
</ol>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Codes and units are where the details live. To see how the charges on your bill compare with what Medicare pays for the same codes, <a href="/scan">check your bill free</a>. To learn how to read the insurer&rsquo;s side, see our <a href="/guides/explanation-of-benefits-eob/">Explanation of Benefits guide</a>.</p>
</div>

<p>If something does not add up, see <a href="/guides/how-to-dispute-a-medical-bill/">how to dispute a medical bill</a> and our <a href="/guides/medical-bill-dispute-letter/">dispute letter guide</a>. Billing errors can be honest mistakes, so a calm letter that names the line and code is a good start.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is a UB-04 form?</h3>
        <p>The UB-04, also called the CMS-1450, is the standard claim form hospitals and other institutional providers use to bill Medicare and most state Medicaid agencies. It lists codes, units, dates, charges, diagnoses and the payer for your visit.</p>
    </div>
    <div class="faq-item">
        <h3>Is a UB-04 the same as an itemized bill?</h3>
        <p>No. An itemized bill is a list of charges prepared for you, and its layout varies by hospital. The UB-04 is the claim sent to your insurer, in standard fields. Having both is useful.</p>
    </div>
    <div class="faq-item">
        <h3>Do I have a legal right to get my UB-04?</h3>
        <p>The HIPAA Privacy Rule gives you a right to copies of the billing records in your designated record set (45 CFR 164.501 and 164.524). A provider does not have to create new documents, so if the hospital keeps no UB-04 image, ask for the claim data as submitted.</p>
    </div>
    <div class="faq-item">
        <h3>How long does the hospital have to send it, and can it charge me?</h3>
        <p>It must act within 30 calendar days of receiving your request, with one extension of up to 30 days if it tells you in writing why. Fees are limited to reasonable, cost-based copying costs, not search and retrieval.</p>
    </div>
    <div class="faq-item">
        <h3>Can the hospital refuse because I have not paid my bill?</h3>
        <p>No. HHS guidance says a covered entity may not withhold or deny access to your health information because you have not paid for the care. It may still charge the allowed copy fee.</p>
    </div>
    <div class="faq-item">
        <h3>What should I do with the UB-04 once I have it?</h3>
        <p>Compare it to your Explanation of Benefits (EOB) and itemized bill: dates, payer, codes, units and the total line. Ask the billing office in writing about anything that does not match.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/billing/electronicbillingeditrans/1450" target="_blank" rel="noopener">CMS &mdash; Institutional paper claim form (CMS-1450)</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c25.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 25: Completing and Processing the Form CMS-1450 Data Set</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.501" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 164.501, Definitions (designated record set)</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.524" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 164.524, Access of individuals to protected health information</a></li>
    <li><a href="https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/access/index.html" target="_blank" rel="noopener">HHS Office for Civil Rights &mdash; Individuals&rsquo; Right under HIPAA to Access their Health Information</a></li>
</ul>
""",
})
