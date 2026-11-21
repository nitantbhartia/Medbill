"""Guide: J-Codes on a Hospital Bill: How to Check Drug Charges."""

from guides import register

register("j-codes-hospital-drug-charges", {
    "title": "J-Codes on a Hospital Bill: How to Check Drug Charges",
    "meta_description": "J-codes are billing codes for drugs like injections and IV drugs. Learn how units work and how to compare each drug line to Medicare’s per-unit price.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "What is a J-code on a hospital bill?",
            "a": "A J-code is a HCPCS Level II code, a five-character code that starts with a letter and is maintained by CMS. Most J-codes describe drugs given by injection or infusion. Each J-code names the drug and the amount that counts as one billing unit, such as 0.1 mg or 10 mg.",
        },
        {
            "q": "How do I know if the units for a drug are right?",
            "a": "Find the amount of the drug you were actually given in your medication administration record. Divide that dose by the amount in the J-code’s description. For example, hydromorphone code J1171 is billed per 0.1 mg, so a 1 mg dose is 10 units. If the bill does not match, ask the billing office about that line.",
        },
        {
            "q": "What does Medicare pay for a drug with a J-code?",
            "a": "For most separately payable Part B drugs, Medicare’s payment limit is the average sales price (ASP) plus 6 percent. CMS posts these per-unit limits each quarter. Under the hospital outpatient payment system, Medicare does not pay separately for low-cost drugs (under $140 per day in 2026); their cost is bundled into the visit.",
        },
        {
            "q": "Why was I charged for my own pills after an outpatient or observation stay?",
            "a": "Medicare Part B generally does not cover drugs you would normally take on your own, often called self-administered drugs, when you get them in a hospital outpatient setting. If you have Part D, you may be able to file a claim with your drug plan for a refund.",
        },
        {
            "q": "How do I get the medication administration record?",
            "a": "Ask the hospital’s medical records office for it. Under HIPAA, the hospital must act on your request within 30 days, with one possible 30-day extension. It may require the request in writing and may charge a reasonable, cost-based fee.",
        },
    ],
    "body": f"""
<p class="lead">A J-code on your hospital bill is a billing code for a drug, usually one given by injection or IV, and each code is billed in fixed units like &ldquo;per 0.1 mg&rdquo; or &ldquo;up to 10 mg.&rdquo; To check a drug charge, divide the dose you got by the code&rsquo;s unit size, make sure the units on the bill match, and then compare the price per unit to what Medicare pays for that code.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-are-j-codes">What J-codes are</a></li>
        <li><a href="#units">How drug units work</a></li>
        <li><a href="#unit-errors">Common unit problems to look for</a></li>
        <li><a href="#revenue-codes">Revenue codes 0636 and 025x</a></li>
        <li><a href="#asp-benchmark">Using Medicare&rsquo;s ASP files as a benchmark</a></li>
        <li><a href="#example">Example: checking two drug lines</a></li>
        <li><a href="#self-administered">Self-administered drugs and Medicare</a></li>
        <li><a href="#what-to-do">What to do, step by step</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-are-j-codes">1. What J-codes are</h2>

<p>Hospitals describe what they did and what they used with standard codes. Services like an ER visit or an IV start usually use <a href="/guides/cpt-codes-explained/">CPT codes</a>, which are five numbers. Drugs, supplies and some other items use HCPCS Level II codes (Healthcare Common Procedure Coding System). CMS, the federal agency that runs Medicare, keeps this code set. Each code is one capital letter followed by four numbers.</p>

<p>Codes that start with J are the ones you will see most for drugs: J1885, J2405, J7030 and so on. Most J-codes describe drugs given by injection or infusion. A few describe oral drugs, such as certain transplant and cancer medicines. You may also see some drugs under C or Q codes.</p>

<p>CMS&rsquo;s 2026 coding manual says each drug code&rsquo;s description has three parts:</p>
<ul>
    <li><strong>Route:</strong> how the drug is given, such as &ldquo;injection&rdquo; or &ldquo;oral.&rdquo;</li>
    <li><strong>Drug name:</strong> the generic name.</li>
    <li><strong>Dose description:</strong> the amount of drug that equals <em>one billing unit</em>.</li>
</ul>

<p>That last part is the key. A code is priced per unit, not per shot or per bag.</p>

<h2 id="units">2. How drug units work</h2>

<p>The &ldquo;units&rdquo; or &ldquo;qty&rdquo; column next to a J-code tells you how many billing units the hospital charged. The basic math is:</p>

<p><strong>Units = dose you were given &divide; amount in one billing unit</strong></p>

<p>Claims cannot take fractions of a unit. CMS builds dose descriptions so that common doses come out to whole numbers where it can. Here are real codes and their unit sizes from a Medicare contractor&rsquo;s drug fee list for October 1 through December 31, 2026:</p>

<table>
    <thead>
        <tr>
            <th>Code</th>
            <th>Drug (as described)</th>
            <th>One unit equals</th>
            <th>Medicare fee per unit (Q4 2026)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>J1171</td>
            <td>Injection, hydromorphone</td>
            <td>0.1 mg</td>
            <td>$0.224</td>
        </tr>
        <tr>
            <td>J2270</td>
            <td>Injection, morphine sulfate</td>
            <td>Up to 10 mg</td>
            <td>$7.259</td>
        </tr>
        <tr>
            <td>J3010</td>
            <td>Injection, fentanyl citrate</td>
            <td>0.1 mg</td>
            <td>$1.362</td>
        </tr>
        <tr>
            <td>J2919</td>
            <td>Injection, methylprednisolone sodium succinate</td>
            <td>5 mg</td>
            <td>$0.255</td>
        </tr>
    </tbody>
</table>

<p>Source: CGS Administrators (a Medicare contractor), DME MAC Jurisdiction C drug fee schedule. That list notes that a code and fee being on it does not mean Medicare covers the drug. Fees change every quarter.</p>

<p>Hydromorphone and fentanyl are counted in tenths of a milligram, so one dose can be 10 or more units. Morphine under J2270 counts any amount up to 10 mg as one unit.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>A big unit count is not wrong by itself. It may just mean the code uses a small unit size. Before you question a line, look up the code&rsquo;s unit and do the division. If you want a quick first pass, <a href="/scan">check your bill free at /scan</a> to see each coded line next to its Medicare rate.</p>
</div>

<h2 id="unit-errors">3. Common unit problems to look for</h2>

<p>Treat these as questions to ask, not proof of wrongdoing. Billing offices make honest mistakes.</p>

<ul>
    <li><strong>Milligrams entered as units.</strong> A 4 mg dose of morphine billed as 4 units of J2270, when the code counts up to 10 mg as one unit, would charge four times too much.</li>
    <li><strong>Doses that were ordered but not given.</strong> Compare each drug line to the times and amounts in your medication administration record (MAR), the nursing log of every dose actually given to you.</li>
    <li><strong>The same dose on two lines or two dates.</strong> Look for one drug billed under two codes, or billed again on a day you were already discharged.</li>
    <li><strong>Leftover drug from a vial.</strong> When a drug comes in a single-dose vial, Medicare pays for the full labeled amount, including the part thrown away. Medicare does not pay for discarded amounts from multiple-dose vials. Hospitals report the discarded amount on its own line, marked with a JW modifier. A vial-sized charge can be correct, so ask before assuming it is an error.</li>
</ul>

<h2 id="revenue-codes">4. Revenue codes 0636 and 025x</h2>

<p>On a hospital itemized bill, each line usually also has a four-digit revenue code. It tells the payer which hospital department the charge came from. Our <a href="/guides/hospital-revenue-codes-explained/">revenue codes guide</a> covers the full list.</p>

<p>For drugs, two groups matter:</p>
<ul>
    <li><strong>0636 &ndash; Drugs requiring detailed coding.</strong> CMS lists this among commonly used revenue codes. Lines under 0636 should carry a specific HCPCS drug code, such as a J-code, so you can check the units.</li>
    <li><strong>0250&ndash;0259 &ndash; Pharmacy.</strong> State Medicaid agencies such as North Carolina&rsquo;s list these as pharmacy revenue codes.</li>
</ul>

<p>If a pharmacy line shows only a drug name and price, with no code, you cannot match it to Medicare&rsquo;s per-unit price. Ask the billing office for the drug name, strength, dose given and the HCPCS code or National Drug Code (NDC) for that line.</p>

<h2 id="asp-benchmark">5. Using Medicare&rsquo;s ASP files as a benchmark</h2>

<p>To judge a drug price, start with what Medicare pays. CMS says most separately payable Part B drugs have a payment limit of the average sales price (ASP) plus 6 percent. ASP is the average price the drug maker gets from its sales, after most discounts.</p>

<p>Key facts from CMS and MedPAC, the agency that advises Congress on Medicare payment:</p>
<ul>
    <li><strong>They are per unit.</strong> CMS publishes the payment limit for each code every quarter in its Medicare Part B Payment Limit Files. As of November 2026, the newest posted file is for October 2026.</li>
    <li><strong>They lag.</strong> Rates update quarterly, based on sales data from two quarters earlier.</li>
    <li><strong>Hospital outpatient rules differ for cheap drugs.</strong> Medicare pays ASP plus 6 percent for drugs it pays separately in hospital outpatient departments. But low-cost drugs (under $140 per day in 2026) are bundled into the payment for the visit or procedure, with no separate drug payment. The per-unit figure is still a fair yardstick for what the drug itself is worth.</li>
    <li><strong>Your share.</strong> People with Medicare generally pay 20 percent of the Medicare amount for Part B drugs.</li>
    <li><strong>A listed price is not a coverage promise.</strong> CMS says a code being in, or missing from, the file does not show whether Medicare covers the drug.</li>
</ul>

<p>Hospitals set their own list prices (the <a href="/guides/hospital-chargemaster-explained/">chargemaster</a>), which can differ a lot from Medicare&rsquo;s amount. A gap does not prove a mistake. It can still support a discount or financial assistance request.</p>

<h2 id="example">6. Example: checking two drug lines</h2>

<p><strong>Example:</strong> This is an illustration, not a real bill. Say you went to the ER. Your medication administration record shows morphine 4 mg IV once, and hydromorphone 0.5 mg IV twice, for 1 mg total. Your itemized bill shows:</p>

<table>
    <thead>
        <tr>
            <th>Line</th>
            <th>Billed</th>
            <th>Correct units</th>
            <th>Correct charge at the hospital&rsquo;s price</th>
            <th>Medicare fee for correct units</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0636 J2270 morphine</td>
            <td>4 units &times; $38.00 = $152.00</td>
            <td>4 mg &divide; up to 10 mg = 1 unit</td>
            <td>1 &times; $38.00 = $38.00</td>
            <td>1 &times; $7.259 = $7.26</td>
        </tr>
        <tr>
            <td>0636 J1171 hydromorphone</td>
            <td>10 units &times; $6.50 = $65.00</td>
            <td>1 mg &divide; 0.1 mg = 10 units</td>
            <td>10 &times; $6.50 = $65.00</td>
            <td>10 &times; $0.224 = $2.24</td>
        </tr>
    </tbody>
</table>

<p>The morphine line looks like a unit error. 4 mg was billed as 4 units, but J2270 counts any amount up to 10 mg as one unit. Fixing it would lower that line from $152.00 to $38.00, a $114.00 difference. The hydromorphone units are correct, so that line is about price, not units: $65.00 billed against a Medicare fee of $2.24 for the same 10 units.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Check units first, then price. A unit error is a clear correction to ask for in writing. A high price on correct units is something to raise in a discount or financial assistance request. Our <a href="/guides/medical-bill-dispute-letter/">dispute letter guide</a> shows how to put both in writing.</p>
</div>

<h2 id="self-administered">7. Self-administered drugs and Medicare</h2>

<p>After an outpatient or observation visit, you may see charges for pills you would normally take yourself. Medicare.gov says Part B generally does not cover prescription and over-the-counter drugs you get in an outpatient setting, which are sometimes called self-administered drugs.</p>

<p>Medicare contractors keep self-administered drug exclusion lists. One contractor&rsquo;s list explains that &ldquo;usually&rdquo; self-administered means more than 50 percent of the time for all Medicare patients who use the drug. A CMS tip sheet notes that Part B covers only certain drugs in these settings, such as drugs given by infusion.</p>

<p>If you have Part D drug coverage, you may get some of that money back. Medicare.gov says you will likely pay out of pocket and then file a claim with your drug plan. A CMS tip sheet adds that the plan generally pays only its in-network cost for drugs on its formulary, minus your usual cost sharing, and needs receipts and paperwork. If you were in observation, our <a href="/guides/medicare-observation-status-billing/">observation status guide</a> explains how the rest of the bill works.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Self-administered drug charges after an outpatient or observation stay may be billed correctly, but you may be able to file a Part D claim for part of the cost. Get the itemized drug list first. Our guide on <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a> shows what to ask for.</p>
</div>

<h2 id="what-to-do">8. What to do, step by step</h2>

<ol>
    <li><strong>Get the itemized bill.</strong> Ask for line-level detail with revenue codes, HCPCS codes, units and dates of service for every drug.</li>
    <li><strong>Request your medication administration record.</strong> Ask the medical records office for your records from the visit, including the MAR. Under HIPAA, you have a right to see your medical and billing records. The hospital must act within 30 days, with one possible 30-day extension. It may require a written request and charge a reasonable, cost-based fee. See <a href="/guides/how-to-request-medical-records/">how to request medical records</a>.</li>
    <li><strong>Look up each J-code&rsquo;s unit size.</strong> Use the code description in CMS&rsquo;s current quarterly Part B payment limit file.</li>
    <li><strong>Do the unit math.</strong> For each drug line, divide the dose given (from the MAR) by the unit size. Mark any line where billed units do not match.</li>
    <li><strong>Compare price per unit.</strong> Multiply the correct units by Medicare&rsquo;s payment limit for that code. Note the gap.</li>
    <li><strong>Put your questions in writing.</strong> List each line, the units you expected and why, and ask for a corrected bill. Keep copies.</li>
    <li><strong>Ask about financial assistance.</strong> If the prices are the problem rather than the units, ask whether you qualify for the hospital&rsquo;s financial assistance program.</li>
</ol>

<p>If a bill has gone to collections or you have received court papers, consider talking to a consumer attorney or legal aid.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is a J-code on a hospital bill?</h3>
        <p>A J-code is a HCPCS Level II code, a five-character code that starts with a letter and is maintained by CMS. Most J-codes describe drugs given by injection or infusion. Each J-code names the drug and the amount that counts as one billing unit, such as 0.1 mg or 10 mg.</p>
    </div>
    <div class="faq-item">
        <h3>How do I know if the units for a drug are right?</h3>
        <p>Find the amount of the drug you were actually given in your medication administration record. Divide that dose by the amount in the J-code&rsquo;s description. For example, hydromorphone code J1171 is billed per 0.1 mg, so a 1 mg dose is 10 units. If the bill does not match, ask the billing office about that line.</p>
    </div>
    <div class="faq-item">
        <h3>What does Medicare pay for a drug with a J-code?</h3>
        <p>For most separately payable Part B drugs, Medicare&rsquo;s payment limit is the average sales price (ASP) plus 6 percent. CMS posts these per-unit limits each quarter. Under the hospital outpatient payment system, Medicare does not pay separately for low-cost drugs (under $140 per day in 2026); their cost is bundled into the visit.</p>
    </div>
    <div class="faq-item">
        <h3>Why was I charged for my own pills after an outpatient or observation stay?</h3>
        <p>Medicare Part B generally does not cover drugs you would normally take on your own, often called self-administered drugs, when you get them in a hospital outpatient setting. If you have Part D, you may be able to file a claim with your drug plan for a refund.</p>
    </div>
    <div class="faq-item">
        <h3>How do I get the medication administration record?</h3>
        <p>Ask the hospital&rsquo;s medical records office for it. Under HIPAA, the hospital must act on your request within 30 days, with one possible 30-day extension. It may require the request in writing and may charge a reasonable, cost-based fee.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/files/document/hcpcs-level-ii-drug-biological-product-coding-development-manual.pdf" target="_blank" rel="noopener">CMS &mdash; HCPCS Level II Drug and Biological Product Coding Development Manual (October 2, 2026)</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system" target="_blank" rel="noopener">CMS &mdash; Healthcare Common Procedure Coding System (HCPCS)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/part-b-drugs" target="_blank" rel="noopener">CMS &mdash; Medicare Part B Drug Average Sales Price</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/part-b-drugs/asp-pricing-files" target="_blank" rel="noopener">CMS &mdash; Medicare Part B Drug Payment Limit Files (ASP pricing files)</a></li>
    <li><a href="https://www.medpac.gov/wp-content/uploads/2026/10/MedPAC_Payment_Basics_26_PartB_FINAL_SEC.pdf" target="_blank" rel="noopener">MedPAC &mdash; Part B Drug Payment Systems, Payment Basics (October 2026)</a></li>
    <li><a href="https://www.cgsmedicare.com/jc/coverage/fees/4thqrtr26drug.pdf" target="_blank" rel="noopener">CGS Administrators &mdash; DME MAC Jurisdiction C Drug Fees, October 1&ndash;December 31, 2026</a></li>
    <li><a href="https://www.cms.gov/Outreach-and-Education/MLN/WBT/MLN7388180-MLN-WBT-1450/1450/lesson05/13/index.html" target="_blank" rel="noopener">CMS Medicare Learning Network &mdash; Revenue Codes</a></li>
    <li><a href="https://medicaid.ncdhhs.gov/blog/2022/03/30/pharmacy-billing-reminder-revenue-codes-025x-and-063x" target="_blank" rel="noopener">NC Medicaid &mdash; Pharmacy Billing Reminder for Revenue Codes 025x and 063x</a></li>
    <li><a href="https://www.medicare.gov/coverage/outpatient-hospital-services" target="_blank" rel="noopener">Medicare.gov &mdash; Outpatient hospital services</a></li>
    <li><a href="https://www.medicare.gov/coverage/prescription-drugs-outpatient" target="_blank" rel="noopener">Medicare.gov &mdash; Prescription drugs (outpatient)</a></li>
    <li><a href="https://www.cms.gov/files/document/11331-ppdf" target="_blank" rel="noopener">CMS &mdash; Tip Sheet: Billing for Self-Administered Drugs Given in Outpatient Settings</a></li>
    <li><a href="https://www.cms.gov/medicare-coverage-database/view/article.aspx?articleid=52527" target="_blank" rel="noopener">CMS Medicare Coverage Database &mdash; Self-Administered Drug Exclusion List (Article A52527, CGS)</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.524" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 164.524, Access of individuals to protected health information</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.501" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 164.501, Definitions (designated record set)</a></li>
</ul>
""",
})
