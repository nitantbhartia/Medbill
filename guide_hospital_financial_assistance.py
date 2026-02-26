"""Guide: How to Apply for Hospital Financial Assistance: A Step-by-Step Guide."""

from guides import register, _embed

register("hospital-financial-assistance-guide", {
    "title": "How to Apply for Hospital Financial Assistance: A Step-by-Step Guide",
    "meta_description": "Nonprofit hospitals must offer financial assistance by law. Learn 501(r) requirements, income thresholds, the application process, and what to do if denied.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Financial Assistance",
    "faqs": [
        {
            "q": "Who qualifies for hospital financial assistance?",
            "a": "Eligibility varies by hospital, but most nonprofit hospital financial assistance policies cover patients with household incomes below 200% to 400% of the Federal Poverty Level. For a single person in 2024, that means an annual income below approximately $30,120 to $60,240. Many hospitals offer a sliding scale: patients below 200% FPL often qualify for free care, while patients between 200% and 400% FPL may receive discounts of 25% to 75%. Some hospitals extend assistance to patients up to 500% or even 600% FPL."
        },
        {
            "q": "Can I apply for financial assistance if I have health insurance?",
            "a": "Yes. Hospital financial assistance can cover the patient-responsibility portion of your bill — the deductible, coinsurance, and copay amounts that remain after your insurance pays its share. If your insurance left you with a large out-of-pocket balance and your income falls within the hospital's eligibility thresholds, you can apply for assistance on the amount you owe. Having insurance does not disqualify you."
        },
        {
            "q": "What is a 501(r) hospital and why does it matter?",
            "a": "A 501(r) hospital is a nonprofit hospital that has tax-exempt status under Section 501(c)(3) of the Internal Revenue Code. In exchange for not paying federal income taxes, these hospitals must comply with Section 501(r) of the IRS code, which requires them to have a written financial assistance policy, publicize it widely, screen patients for eligibility before pursuing extraordinary collection actions like lawsuits or credit reporting, and limit charges for financial-assistance-eligible patients to no more than the amount generally billed to insured patients."
        },
        {
            "q": "How long do I have to apply for hospital financial assistance?",
            "a": "Under IRS Section 501(r), nonprofit hospitals must accept financial assistance applications for at least 240 days after the first post-discharge billing statement. Many hospitals accept applications beyond this window. You can apply even if you have already made partial payments or set up a payment plan. The critical deadline is before the hospital takes extraordinary collection actions — after that point, your options become more limited."
        },
        {
            "q": "What if the hospital denies my financial assistance application?",
            "a": "You have the right to appeal. Ask for the denial reason in writing. Common reasons include incomplete applications, missing documents, or income slightly above the threshold. Resubmit with any missing documentation and a letter explaining any extenuating circumstances (recent job loss, medical expenses, other debts). If the appeal is denied, contact the hospital's patient advocate, your state attorney general's office, or a nonprofit patient advocacy organization for help."
        },
    ],
    "body": f"""
<p class="lead">Approximately 60% of hospitals in the United States are nonprofit institutions, and <strong>every one of them is legally required to offer financial assistance to patients who cannot afford their bills</strong>. Under IRS Section 501(r), these hospitals must have a written financial assistance policy, publicize it, and screen patients for eligibility before sending them to collections. Yet billions of dollars in available assistance go unclaimed each year because patients do not know to apply. This guide walks you through the entire process, step by step. Before you apply, <a href="/scan">upload your bill to BillKarma</a> to check for billing errors — reducing the bill first makes financial assistance go further.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#501r">What 501(r) requires hospitals to do</a></li>
        <li><a href="#income-thresholds">Income thresholds: who qualifies</a></li>
        <li><a href="#fpl-table">2024 Federal Poverty Level reference table</a></li>
        <li><a href="#step-by-step">Step-by-step application process</a></li>
        <li><a href="#documents">Documents you will need</a></li>
        <li><a href="#denied">What to do if your application is denied</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="501r">1. What 501(r) requires hospitals to do</h2>

<p>IRS Section 501(r), enacted as part of the Affordable Care Act in 2010, sets four requirements for nonprofit hospitals to maintain their tax-exempt status:</p>

<ol>
    <li><strong>Written financial assistance policy (FAP).</strong> The hospital must have a written policy describing who is eligible, how to apply, what basis is used to calculate charges for eligible patients, and what collection actions the hospital may take. This policy must be available in the languages spoken by the community the hospital serves.</li>
    <li><strong>Wide publicity.</strong> The hospital must make the FAP widely available — posted on the hospital's website, provided to patients at admission, included with billing statements, and available in the emergency department and admissions areas. They cannot bury it.</li>
    <li><strong>Screening before collections.</strong> The hospital must make reasonable efforts to determine whether a patient is eligible for financial assistance before taking extraordinary collection actions. "Extraordinary collection actions" include lawsuits, liens on property, wage garnishments, and reporting debt to credit agencies. The hospital must wait at least 120 days from the first billing statement before initiating these actions.</li>
    <li><strong>Charge limitations.</strong> Financial-assistance-eligible patients cannot be charged more than the Amount Generally Billed (AGB) to insured patients. This means the hospital cannot charge you the full chargemaster rate — they must limit charges to something approximating what they accept from insurance companies.</li>
</ol>

<div class="key-takeaway">
    <strong>If a nonprofit hospital sends you to collections without first offering financial assistance and giving you a reasonable opportunity to apply, they may be violating federal law.</strong> Report violations to the IRS using Form 13909 or contact your state attorney general's consumer protection office. You can check whether your hospital is nonprofit (and therefore subject to 501(r)) at <a href="/hospitals/">our hospital directory</a>.
</div>

<h2 id="income-thresholds">2. Income thresholds: who qualifies</h2>

<p>Financial assistance eligibility is based on your household income as a percentage of the Federal Poverty Level (FPL). Each hospital sets its own thresholds, but here is the typical structure:</p>

<table>
    <thead>
        <tr>
            <th>Household Income (% of FPL)</th>
            <th>Typical Discount</th>
            <th>What It Means</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Below 200% FPL</strong></td>
            <td>100% (free care)</td>
            <td>Full bill write-off; you owe $0. Most nonprofit hospitals offer free care at this level.</td>
        </tr>
        <tr>
            <td><strong>200%&ndash;300% FPL</strong></td>
            <td>50%&ndash;75% discount</td>
            <td>Significant reduction. A $20,000 bill might be reduced to $5,000&ndash;$10,000.</td>
        </tr>
        <tr>
            <td><strong>300%&ndash;400% FPL</strong></td>
            <td>25%&ndash;50% discount</td>
            <td>Moderate reduction. Some hospitals cap charges at the Amount Generally Billed (AGB) to insured patients.</td>
        </tr>
        <tr>
            <td><strong>400%+ FPL</strong></td>
            <td>Varies (some hospitals extend to 500%&ndash;600%)</td>
            <td>Some hospitals offer smaller discounts or payment plans at this level. Always ask.</td>
        </tr>
    </tbody>
</table>

<p>The thresholds above are common, but every hospital is different. Some of the most generous programs extend free care to 300% FPL and discounted care to 600% FPL (notably in Illinois, where state law requires this). Always check your specific hospital's FAP — it is available on their website and by request from the billing department. You can also use the <a href="/calculator">BillKarma cost calculator</a> to see what Medicare pays for the services on your bill — this gives you a baseline for evaluating whether the hospital's charges are reasonable even after a discount.</p>

<h2 id="fpl-table">3. 2024 Federal Poverty Level reference table</h2>

<p>Use this table to determine where your household income falls relative to the FPL. These are the 2024 guidelines (used for assistance applications through early 2026 until the 2025 guidelines are published):</p>

<table>
    <thead>
        <tr>
            <th>Family Size</th>
            <th>100% FPL</th>
            <th>200% FPL</th>
            <th>300% FPL</th>
            <th>400% FPL</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>$15,060</td>
            <td>$30,120</td>
            <td>$45,180</td>
            <td>$60,240</td>
        </tr>
        <tr>
            <td>2</td>
            <td>$20,440</td>
            <td>$40,880</td>
            <td>$61,320</td>
            <td>$81,760</td>
        </tr>
        <tr>
            <td>3</td>
            <td>$25,820</td>
            <td>$51,640</td>
            <td>$77,460</td>
            <td>$103,280</td>
        </tr>
        <tr>
            <td>4</td>
            <td>$31,200</td>
            <td>$62,400</td>
            <td>$93,600</td>
            <td>$124,800</td>
        </tr>
        <tr>
            <td>5</td>
            <td>$36,580</td>
            <td>$73,160</td>
            <td>$109,740</td>
            <td>$146,320</td>
        </tr>
        <tr>
            <td>6</td>
            <td>$41,960</td>
            <td>$83,920</td>
            <td>$125,880</td>
            <td>$167,840</td>
        </tr>
        <tr>
            <td>7</td>
            <td>$47,340</td>
            <td>$94,680</td>
            <td>$142,020</td>
            <td>$189,360</td>
        </tr>
        <tr>
            <td>8</td>
            <td>$52,720</td>
            <td>$105,440</td>
            <td>$158,160</td>
            <td>$210,880</td>
        </tr>
    </tbody>
</table>

<p>For each additional person beyond 8, add $5,380 to the 100% FPL figure. Alaska and Hawaii have higher FPL thresholds — add approximately $1,880 (Alaska) or $1,730 (Hawaii) per family member above the base amount.</p>

<h2 id="step-by-step">4. Step-by-step application process</h2>

<ol>
    <li><strong>Confirm the hospital is nonprofit.</strong> Check the hospital's website for "501(c)(3)" or "tax-exempt" status. You can also search the IRS Tax Exempt Organization Search tool or check our <a href="/hospitals/">hospital directory</a>. Approximately 60% of US hospitals are nonprofit.</li>
    <li><strong>Find the financial assistance policy.</strong> Look on the hospital's website under "Billing," "Financial Services," or "Patient Financial Assistance." You can also call the billing department and say: "I would like a copy of your financial assistance policy and an application form."</li>
    <li><strong>Download and complete the application.</strong> The application typically asks for your household size, household income, employment status, and insurance information. Fill in every section completely — incomplete applications are the most common reason for delays and denials.</li>
    <li><strong>Gather your supporting documents.</strong> See the full list in the next section. At minimum, you will need proof of income and proof of household size.</li>
    <li><strong>Submit the application.</strong> Submit by certified mail, in person at the patient financial services office, or through the hospital's online portal. Keep a copy of everything you submit and a record of the submission date.</li>
    <li><strong>Request a billing hold.</strong> When you submit the application, ask the hospital to place your account on hold during the review period. Most hospitals will pause collection activity while a financial assistance application is pending. Get this confirmation in writing.</li>
    <li><strong>Follow up after 30 days.</strong> If you have not received a response within 30 days, call the patient financial services department for a status update. Ask for the name of the person handling your application and a direct phone number.</li>
</ol>

{_embed(mode="markup", title="How much could financial assistance save you?", subtitle="Enter your billed amount to see potential reductions at different discount levels.", height="420")}

<h2 id="documents">5. Documents you will need</h2>

<p>Most hospital financial assistance applications require the following documentation. Gather these before starting the application to avoid delays:</p>

<ul>
    <li><strong>Proof of income</strong> — your two most recent pay stubs, or your most recent tax return (Form 1040), or a letter from your employer stating your annual salary. If you are unemployed, provide your most recent unemployment benefits statement or a signed letter stating you are unemployed with no income.</li>
    <li><strong>Proof of household size</strong> — a copy of your most recent tax return showing dependents, or birth certificates for children, or a signed statement listing everyone in your household.</li>
    <li><strong>Insurance information</strong> — a copy of your insurance card (front and back) and the Explanation of Benefits (EOB) showing what insurance paid on the bill in question. If you are uninsured, state this on the application.</li>
    <li><strong>The bill</strong> — a copy of the hospital bill you are requesting assistance for, including the account number and date of service.</li>
    <li><strong>Bank statements</strong> — some hospitals request one to three months of checking and savings account statements. Not all hospitals require this.</li>
    <li><strong>Proof of hardship (if applicable)</strong> — documentation of recent job loss, disability, divorce, death of a spouse, or other financial hardship that affects your ability to pay. This is not always required but strengthens your application.</li>
</ul>

<div class="key-takeaway">
    <strong>Missing a document?</strong> Submit the application with everything you have and note which documents are pending. A partial application submitted on time is better than a complete application submitted late. You can provide additional documents during the review process. While your application is in progress, <a href="/scan">scan your bill with BillKarma</a> to identify any billing errors worth disputing separately — correcting overcharges on top of financial assistance can dramatically reduce what you owe.
</div>

<h2 id="denied">6. What to do if your application is denied</h2>

<p>A denial is not the end of the process. Financial assistance denials can be appealed, and many are overturned when patients provide additional information.</p>

<ol>
    <li><strong>Request the denial reason in writing.</strong> The hospital must tell you why you were denied. Common reasons: income above the threshold, incomplete application, missing documents, or the bill is from a for-profit entity within the hospital system that is not covered by the FAP.</li>
    <li><strong>Address the specific reason.</strong> If documents were missing, gather and submit them. If your income was slightly above the threshold, write a letter explaining extraordinary expenses — medical costs, rent increases, childcare — that reduce your effective ability to pay.</li>
    <li><strong>File a formal appeal.</strong> Most hospitals have a written appeal process. Include any new documentation and a clear explanation of why you believe you qualify.</li>
    <li><strong>Ask about alternative programs.</strong> Even if you do not qualify for the formal financial assistance program, ask about hardship discounts, prompt-pay discounts, or extended payment plans with no interest. Many hospitals offer these outside the FAP. See our <a href="/guides/how-to-negotiate-a-medical-bill">negotiation guide</a> for strategies to reduce your bill even without formal financial assistance.</li>
    <li><strong>Contact your state attorney general.</strong> If you believe the hospital failed to follow its own financial assistance policy or failed to screen you before taking collection action, file a complaint with your state attorney general's consumer protection division.</li>
    <li><strong>Report 501(r) violations to the IRS.</strong> If a nonprofit hospital denied your application without following its own written policy, or took extraordinary collection actions without giving you a reasonable opportunity to apply, you can file IRS Form 13909 to report a potential 501(r) violation.</li>
</ol>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Family of four earning $58,000 gets $34,000 hospital bill reduced to $0</h3>
    <p>A family of four in Illinois with a household income of $58,000 (186% FPL) received a $34,000 bill after an emergency appendectomy at a nonprofit hospital. The family had insurance, but their high-deductible plan left them with $8,200 in patient responsibility (deductible plus coinsurance). They contacted the hospital's patient financial services department and requested a financial assistance application. Because their income fell below the hospital's 200% FPL threshold for free care, and Illinois state law requires nonprofit hospitals to provide free care to patients under 200% FPL, the hospital approved the application and wrote off the entire $8,200 patient responsibility. The family also learned that the hospital's published AGB rate for the procedure was $12,400 — less than half the $34,000 gross charge. <strong>Result: $8,200 patient responsibility eliminated entirely.</strong></p>
    <p>If you are in a similar situation, <a href="/scan">upload your bill to BillKarma</a> to check for errors before applying for assistance, and review our <a href="/guides/medical-billing-rights-overview">medical billing rights overview</a> to know your full protections.</p>
</div>

<div class="case-study">
    <h3>Uninsured patient negotiates $47,000 ER bill down to $6,100 through financial assistance</h3>
    <p>A 32-year-old uninsured patient in Texas was hospitalized for three days after a motorcycle accident. The hospital bill totaled $47,000 at chargemaster rates. The patient earned $42,000 per year (single, 279% FPL). He applied for the hospital's financial assistance program, which offered a sliding-scale discount for patients between 200% and 400% FPL. At 279% FPL, the hospital's policy provided a 65% discount on the AGB rate. The hospital first recalculated the bill from the $47,000 chargemaster rate to the AGB rate of $17,400, then applied the 65% discount, reducing the bill to $6,090. The hospital also offered a 12-month interest-free payment plan. <strong>Result: $47,000 reduced to $6,090 — an 87% reduction.</strong></p>
</div>

<h2 id="faq">8. Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Who qualifies for hospital financial assistance?</h3>
        <p>Eligibility varies by hospital. Most nonprofit hospitals offer free care to patients below 200% of the Federal Poverty Level and discounted care up to 300% or 400% FPL. For a family of four in 2024, 200% FPL is $62,400 and 400% FPL is $124,800. Some hospitals extend assistance higher. Check your hospital's specific financial assistance policy on their website or by calling the billing department. If your bill seems inflated, <a href="/guides/medical-bill-audit-checklist">audit it first</a> using our 12-point checklist before applying for assistance.</p>
    </div>

    <div class="faq-item">
        <h3>Can I apply for financial assistance if I have health insurance?</h3>
        <p>Yes. Financial assistance can cover the patient-responsibility portion of your bill — deductibles, coinsurance, and copays remaining after insurance pays. If your income qualifies and your out-of-pocket amount is unaffordable, apply. Having insurance does not disqualify you from hospital financial assistance programs.</p>
    </div>

    <div class="faq-item">
        <h3>What is a 501(r) hospital and why does it matter?</h3>
        <p>A 501(r) hospital is a nonprofit, tax-exempt hospital required by the IRS to offer financial assistance, publicize the program, and screen patients for eligibility before pursuing collections. Approximately 60% of US hospitals are nonprofit and subject to these rules. You can verify your hospital's status in our <a href="/hospitals/">hospital directory</a>.</p>
    </div>

    <div class="faq-item">
        <h3>How long do I have to apply for hospital financial assistance?</h3>
        <p>Under 501(r), hospitals must accept applications for at least 240 days after the first billing statement. Many hospitals accept applications beyond this window. You can apply even after making partial payments. The key is to apply before the hospital takes extraordinary collection actions like lawsuits or credit reporting.</p>
    </div>

    <div class="faq-item">
        <h3>What if the hospital denies my financial assistance application?</h3>
        <p>Request the denial reason in writing, address the specific issue (missing documents, income above threshold), and file a formal appeal. If your income was close to the threshold, explain extraordinary expenses that reduce your ability to pay. If the hospital is not following its own policy, file complaints with your state attorney general and the IRS (Form 13909). See our <a href="/guides/hospital-financial-assistance-charity-care">charity care guide</a> for additional strategies.</p>
    </div>
</div>

<h2 id="sources">9. Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">IRS: Section 501(r) Requirements for Charitable Hospital Organizations &mdash; Final Regulations and Guidance</a></li>
    <li><a href="#" target="_blank" rel="noopener">HHS Office of the Assistant Secretary for Planning and Evaluation: 2024 Federal Poverty Guidelines</a></li>
    <li><a href="#" target="_blank" rel="noopener">KFF: Nonprofit Hospitals&rsquo; Community Benefit and Financial Assistance &mdash; Compliance and Spending Analysis</a></li>
    <li><a href="#" target="_blank" rel="noopener">Consumer Financial Protection Bureau: Medical Billing and Collections &mdash; Consumer Complaint Data and Policy Analysis</a></li>
    <li><a href="#" target="_blank" rel="noopener">American Hospital Association: Hospital Financial Assistance Fact Sheet &mdash; Charity Care Spending by State</a></li>
    <li><a href="#" target="_blank" rel="noopener">National Consumer Law Center: Hospital Financial Assistance Policies &mdash; Best Practices and Enforcement Guide</a></li>
</ul>
""",
})
