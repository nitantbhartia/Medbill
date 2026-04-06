"""Guide: ACA Marketplace Subsidies: How Much Can You Save in 2026?"""

from guides import register, _embed

register("aca-marketplace-subsidies", {
    "title": "ACA Marketplace Subsidies: How Much Can You Save in 2026?",
    "meta_description": "The average marketplace enrollee gets $6,100/year in ACA subsidies. Learn how premium tax credits and cost-sharing reductions work and how to claim what you're owed.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance & Coverage",
    "faqs": [
        {
            "q": "How do ACA premium tax credits work in 2026?",
            "a": "The premium tax credit (PTC) reduces your monthly health insurance premium on the ACA marketplace. The credit is calculated as the difference between the cost of the benchmark plan (the second-lowest-cost silver plan available to you) and your &ldquo;expected contribution&rdquo;&mdash;a percentage of your income that slides from 0% at 100% FPL to 8.5% at higher incomes. If the benchmark plan costs $600/month and your expected contribution is $100/month, your tax credit is $500/month. You can take it as an advance payment (APTC) reducing your monthly premium, or claim it on your tax return.",
        },
        {
            "q": "What are cost-sharing reductions (CSR) and how do I get them?",
            "a": "Cost-sharing reductions (CSR) are additional subsidies that lower your deductible, copays, and out-of-pocket maximum on Silver plans. They are available only if your income is 100&ndash;250% of the federal poverty level AND you enroll in a Silver plan. At 200% FPL, CSR can reduce your deductible from $4,000 to under $400 and your out-of-pocket maximum from $9,450 to around $2,900. You do not need to separately apply for CSR&mdash;it is automatically applied when you select a Silver plan and your income qualifies.",
        },
        {
            "q": "What happens if I earn more than expected and claimed too much in APTC?",
            "a": "If you received Advance Premium Tax Credits (APTC) during the year but your actual income was higher than you estimated, you must repay part of the excess credit when you file your taxes (Form 8962). However, there are annual caps on how much you must repay, based on income. The repayment cap ranges from $375 (for income under 200% FPL) to $1,650 (for income 300&ndash;400% FPL) for individuals. If your income exceeds 400% FPL and you received APTC, you must repay the full excess amount. Updating your income estimate at healthcare.gov mid-year reduces this risk.",
        },
        {
            "q": "Do ACA subsidies apply to all plan types (Bronze, Silver, Gold, Platinum)?",
            "a": "Premium tax credits can be applied to any metal-tier plan (Bronze, Silver, Gold, Platinum). However, cost-sharing reductions (CSR) apply ONLY to Silver plans. This creates the well-known &ldquo;silver loading&rdquo; effect: because insurers must fund CSR from premiums, silver plans often have higher list premiums than bronze plans, which makes bronze plans effectively cheaper after the tax credit. If your income is 100&ndash;250% FPL, Silver is almost always the right choice to capture CSR. If your income is 250&ndash;400% FPL, compare Silver and Gold carefully.",
        },
        {
            "q": "Can self-employed and freelance workers get ACA subsidies?",
            "a": "Yes. Self-employed individuals and freelancers who purchase insurance on the ACA marketplace are eligible for premium tax credits and cost-sharing reductions based on their net self-employment income (after deductions). Because self-employment income can fluctuate, update your income estimate at healthcare.gov any time it changes significantly to avoid a large tax-time repayment. You can also deduct 100% of your health insurance premiums as a self-employed individual, which further reduces your tax burden.",
        },
    ],
    "body": f"""
<p class="lead">The average ACA marketplace enrollee receives <strong>$6,100 per year in federal subsidies</strong>&mdash;yet BillKarma data shows <strong>3.2 million people who qualify don&rsquo;t claim them</strong>. There are two types of financial assistance: the Premium Tax Credit, which cuts your monthly premium, and Cost-Sharing Reductions, which slash your deductible and out-of-pocket maximum. Understanding how both work can mean the difference between $0 and $800 per month in premiums, and between a $9,450 and a $900 out-of-pocket maximum. This guide shows you exactly how to calculate and claim what you&rsquo;re owed.</p>

<div class="answer-box">
    <strong>Quick answer:</strong> Two ACA subsidies: 1) Premium Tax Credit (PTC) &mdash; reduces monthly premium, available to households 100%&ndash;400%+ FPL. 2) Cost-Sharing Reductions (CSR) &mdash; lowers deductible/copays/OOP max, only on Silver plans, only for income 100&ndash;250% FPL. Choose Silver if you&rsquo;re in the CSR range. Apply at healthcare.gov.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#two-types">The two types of ACA financial assistance</a></li>
        <li><a href="#premium-tax-credit">How the Premium Tax Credit is calculated</a></li>
        <li><a href="#fpl-amounts">2026 Federal Poverty Level amounts</a></li>
        <li><a href="#csr">Cost-Sharing Reductions: the most underused benefit</a></li>
        <li><a href="#aptc-reconciliation">APTC and year-end tax reconciliation</a></li>
        <li><a href="#medicaid-vs-marketplace">Medicaid vs. marketplace: which is better?</a></li>
        <li><a href="#freelancers">APTC for self-employed and freelancers</a></li>
        <li><a href="#how-to-apply">How to estimate and apply for subsidies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="two-types">1. The two types of ACA financial assistance</h2>

<p>The ACA provides two distinct financial assistance mechanisms. They are separate, work differently, and have different eligibility rules. Many people know about one but miss the other.</p>

<table>
    <thead>
        <tr>
            <th>Subsidy Type</th>
            <th>What It Does</th>
            <th>Income Range</th>
            <th>Plan Restriction</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Premium Tax Credit (PTC)</td><td>Reduces monthly premium</td><td>100%+ FPL (no cap with enhanced subsidies)</td><td>Any metal tier</td></tr>
        <tr><td>Cost-Sharing Reductions (CSR)</td><td>Lowers deductible, copays, OOP max</td><td>100&ndash;250% FPL only</td><td>Silver plans only</td></tr>
    </tbody>
</table>

<p>The key insight: if your income is 100&ndash;250% FPL, you should almost always choose a Silver plan. You&rsquo;ll receive both the premium tax credit AND cost-sharing reductions&mdash;giving you platinum-equivalent benefits at a silver (or lower) premium cost. Choosing a Bronze plan in this income range leaves significant CSR value on the table.</p>

{_embed(mode="subsidy", title="Estimate your ACA subsidy", subtitle="See your premium tax credit and cost-sharing reduction eligibility for 2026.")}

<h2 id="premium-tax-credit">2. How the Premium Tax Credit is calculated</h2>

<p>The Premium Tax Credit (PTC) is calculated using a specific formula that compares what you are expected to pay versus what the benchmark plan actually costs:</p>

<ol>
    <li><strong>Identify the benchmark plan:</strong> The second-lowest-cost Silver plan (SLCSP) available to you in your county. This is the reference point for all subsidy calculations.</li>
    <li><strong>Calculate your expected contribution:</strong> Based on your household income as a percentage of FPL, the ACA sets a maximum percentage of your income you are expected to pay for the benchmark plan. This percentage ranges from 0% (at 100% FPL) to 8.5% (at higher incomes) under current law.</li>
    <li><strong>The tax credit equals the difference:</strong> If the benchmark plan costs $700/month and your expected contribution is $150/month, your tax credit is $550/month ($6,600/year).</li>
    <li><strong>Apply it to your chosen plan:</strong> You can apply the credit to any metal-tier plan. If you choose a plan cheaper than the benchmark, your out-of-pocket premium is lower (or even $0). If you choose a more expensive plan, you pay the difference above the credit.</li>
</ol>

<p><strong>Enhanced subsidies (current law):</strong> Under legislation extending enhanced subsidies, no one pays more than 8.5% of their income for the benchmark plan, regardless of income level. This means people above 400% FPL can now qualify for subsidies if the benchmark plan in their area is expensive relative to their income. Verify current subsidy rules at healthcare.gov, as these enhancements are subject to Congressional reauthorization.</p>

<h2 id="fpl-amounts">3. 2026 Federal Poverty Level amounts</h2>

<p>Subsidy eligibility is based on your household income relative to the Federal Poverty Level (FPL). The 2026 FPL figures used for marketplace enrollment (based on 2025 HHS guidelines):</p>

<table>
    <thead>
        <tr>
            <th>Household Size</th>
            <th>100% FPL</th>
            <th>138% FPL (Medicaid line)</th>
            <th>200% FPL (CSR tier)</th>
            <th>250% FPL (CSR cutoff)</th>
            <th>400% FPL</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$15,650</td><td>$21,597</td><td>$31,300</td><td>$39,125</td><td>$62,600</td></tr>
        <tr><td>2 people</td><td>$21,150</td><td>$29,187</td><td>$42,300</td><td>$52,875</td><td>$84,600</td></tr>
        <tr><td>3 people</td><td>$26,650</td><td>$36,777</td><td>$53,300</td><td>$66,625</td><td>$106,600</td></tr>
        <tr><td>4 people</td><td>$32,150</td><td>$44,367</td><td>$64,300</td><td>$80,375</td><td>$128,600</td></tr>
        <tr><td>6 people</td><td>$43,150</td><td>$59,547</td><td>$86,300</td><td>$107,875</td><td>$172,600</td></tr>
    </tbody>
</table>

<p><strong>Alaska and Hawaii:</strong> FPL figures are higher in these states. Use healthcare.gov&rsquo;s calculator with your state to get the correct thresholds.</p>

<p><strong>The Medicaid cliff in non-expansion states:</strong> In the 10 states that have not expanded Medicaid, adults with income below 100% FPL may fall into the &ldquo;coverage gap&rdquo;&mdash;too poor for marketplace subsidies (which start at 100% FPL) but not qualifying for Medicaid. If you are in a non-expansion state with income below $15,650 as an individual, check your state&rsquo;s Medicaid rules for any available categories you might qualify under.</p>

<h2 id="csr">4. Cost-Sharing Reductions: the most underused benefit</h2>

<p>Cost-Sharing Reductions (CSR) are an additional subsidy layered on top of the premium tax credit. They are available only for Silver plans and only for income between 100% and 250% FPL. The impact is dramatic:</p>

<table>
    <thead>
        <tr>
            <th>Income Level</th>
            <th>Standard Silver Plan</th>
            <th>With CSR (Silver)</th>
            <th>Equivalent Plan Value</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>100&ndash;150% FPL</td><td>Deductible: ~$4,500, OOP max: ~$9,450</td><td>Deductible: ~$0&ndash;$325, OOP max: ~$1,400</td><td>Platinum+</td></tr>
        <tr><td>150&ndash;200% FPL</td><td>Deductible: ~$4,500, OOP max: ~$9,450</td><td>Deductible: ~$700, OOP max: ~$2,900</td><td>Gold/Platinum</td></tr>
        <tr><td>200&ndash;250% FPL</td><td>Deductible: ~$4,500, OOP max: ~$9,450</td><td>Deductible: ~$1,000&ndash;$2,500, OOP max: ~$5,700</td><td>Silver/Gold</td></tr>
    </tbody>
</table>

<p>Notice: at 150&ndash;200% FPL on a Silver plan with CSR, you get a deductible of roughly $700 and an out-of-pocket maximum of $2,900. A standard Gold plan has a deductible of $1,000&ndash;$2,000 and an OOP max of $4,000&ndash;$6,000&mdash;worse cost-sharing, and Gold plans have higher premiums. The CSR silver plan beats Gold at this income level in virtually every scenario.</p>

<p><strong>You do not separately apply for CSR.</strong> When you apply at healthcare.gov, the system determines your income and automatically shows Silver plans with CSR applied. The cost-sharing reductions appear in the plan details showing the lower deductible and OOP max. If you choose a Bronze, Gold, or Platinum plan, the CSR does not apply.</p>

<div class="key-takeaway">
    <strong>BillKarma stat:</strong> The average marketplace enrollee receives $6,100/year in subsidies, but 3.2 million eligible people don&rsquo;t claim them. The most common reason: they overestimated their income during enrollment and chose a Bronze plan thinking it was cheaper. If your income is 100&ndash;250% FPL, re-run your numbers at healthcare.gov with Silver plans included. <a href="/fight-debt">BillKarma can help you understand your coverage options.</a>
</div>

<h2 id="aptc-reconciliation">5. APTC and year-end tax reconciliation</h2>

<p>The Advance Premium Tax Credit (APTC) is the premium tax credit paid directly to your insurer each month on your behalf, reducing your monthly premium bill. At tax time, you reconcile the advance payments against your actual credit on <strong>Form 8962</strong>. Here is what can go wrong:</p>

<p><strong>If your income was lower than estimated:</strong> You are entitled to a larger credit than you received. The difference is added to your tax refund or reduces what you owe.</p>

<p><strong>If your income was higher than estimated:</strong> You received too much APTC and must repay the difference. However, repayment is capped:</p>

<table>
    <thead>
        <tr>
            <th>Income vs. FPL</th>
            <th>Individual Repayment Cap</th>
            <th>Family Repayment Cap</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>100&ndash;200% FPL</td><td>$375</td><td>$750</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$950</td><td>$1,900</td></tr>
        <tr><td>300&ndash;400% FPL</td><td>$1,650</td><td>$3,300</td></tr>
        <tr><td>Above 400% FPL</td><td>Full excess repayment (no cap)</td><td>Full excess repayment (no cap)</td></tr>
    </tbody>
</table>

<p><strong>The income cliff trap:</strong> If you are near 400% FPL and your income edges over, you lose the repayment cap and must repay the full excess APTC. This can create an unexpected tax bill of thousands of dollars. For example, a single person at 401% FPL who received $6,000 in APTC might owe back the entire amount if the benchmark plan at their income level would have been unsubsidized. Plan ahead: if you know your income may exceed 400% FPL, reduce your APTC elections mid-year through healthcare.gov.</p>

<p><strong>How to update income mid-year:</strong> Log into healthcare.gov (or your state exchange), select &ldquo;report a life change,&rdquo; and update your projected annual income. Your monthly APTC will be recalculated immediately. Do this any time your income changes significantly&mdash;a new job, a raise, a freelance project, or a job loss.</p>

<h2 id="medicaid-vs-marketplace">6. Medicaid vs. marketplace: which is better?</h2>

<p>If your income is below approximately 138% FPL in a Medicaid expansion state, you will be directed to Medicaid instead of marketplace coverage. For most people, Medicaid is the better deal&mdash;but it is worth understanding why:</p>

<table>
    <thead>
        <tr>
            <th>Factor</th>
            <th>Medicaid</th>
            <th>ACA Marketplace (with CSR)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Monthly premium</td><td>$0</td><td>Often $0&ndash;$50 with large APTC</td></tr>
        <tr><td>Deductible</td><td>Usually $0</td><td>$0&ndash;$325 with CSR at lowest income tier</td></tr>
        <tr><td>OOP maximum</td><td>Minimal or none</td><td>$1,400+ with CSR</td></tr>
        <tr><td>Enrollment timing</td><td>Any time</td><td>Open enrollment or SEP only</td></tr>
        <tr><td>Network</td><td>May be limited to Medicaid providers</td><td>Typically broader; plan-dependent</td></tr>
    </tbody>
</table>

<p>Medicaid wins on cost. The tradeoff is network access&mdash;some Medicaid managed care networks exclude certain specialists or hospitals. If provider choice matters to you, compare your options carefully at healthcare.gov before selecting Medicaid vs. marketplace.</p>

<p>Note: if you are between 100&ndash;138% FPL in an expansion state, you qualify for Medicaid&mdash;not marketplace coverage. You will be redirected at healthcare.gov. If your income fluctuates around this threshold (common for gig workers and freelancers), keep your income estimate updated to ensure you&rsquo;re enrolled in the right program.</p>

<h2 id="freelancers">7. APTC for self-employed and freelancers</h2>

<p>Self-employed individuals and freelancers who buy individual coverage through the ACA marketplace can benefit from subsidies in two separate ways:</p>

<ol>
    <li><strong>Premium Tax Credit:</strong> Based on net self-employment income (gross revenue minus business deductions). If your business has significant expenses, your net income may qualify you for substantial APTC even if your gross revenue is higher.</li>
    <li><strong>Self-employed health insurance deduction:</strong> Separately from the APTC, self-employed individuals can deduct 100% of their health insurance premiums paid (including any amounts you paid after APTC) from their income on Schedule 1 of Form 1040. This reduces your adjusted gross income, which can in turn increase your APTC eligibility.</li>
</ol>

<p>This interaction can be circular (your deduction reduces income, which increases the credit, which reduces the premium, which reduces the deduction). The IRS provides a worksheet to solve for the optimal calculation. Tax software handles this automatically, but it&rsquo;s important to be aware that your final subsidy may differ from your initial estimate.</p>

<p><strong>Quarterly income estimation for freelancers:</strong> If your income varies month to month, update your healthcare.gov income estimate each quarter to avoid a large year-end reconciliation. It is easier to adjust than to face a surprise tax bill in April.</p>

<h2 id="how-to-apply">8. How to estimate and apply for subsidies</h2>

<p>The process for claiming ACA subsidies is built into the healthcare.gov application. Here is the step-by-step:</p>

<ol>
    <li><strong>Go to healthcare.gov</strong> (or your state&rsquo;s exchange: Covered California, NY State of Health, etc.).</li>
    <li><strong>Create an account</strong> if you don&rsquo;t have one. You will need a valid email address.</li>
    <li><strong>Enter your household information:</strong> zip code, household size, and projected annual income for the coverage year. Use your best estimate of this year&rsquo;s income, not last year&rsquo;s.</li>
    <li><strong>Review your eligibility determination.</strong> The system will tell you whether you qualify for Medicaid, CHIP, or marketplace subsidies. If marketplace, it will show your estimated monthly APTC.</li>
    <li><strong>Browse and compare plans.</strong> Use the filter for metal tier. If you&rsquo;re in the CSR income range, compare Silver plans first. Look at the actual deductible and OOP max shown for each plan after CSR is applied.</li>
    <li><strong>Select a plan and enroll.</strong> Your APTC is automatically applied to your monthly premium. You pay only the remaining premium directly to the insurer.</li>
    <li><strong>Report income changes during the year.</strong> Log in to healthcare.gov any time your income changes meaningfully and update your application. This adjusts your monthly APTC and prevents over- or underpayment.</li>
</ol>

<div class="key-takeaway">
    <strong>Already enrolled but not sure you got the right plan?</strong> During open enrollment or after a qualifying life event, you can switch plans. If you chose a Bronze plan and your income qualifies you for CSR, switching to Silver could cut your deductible by thousands of dollars. <a href="/fight-debt">BillKarma can help you review your coverage.</a>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How do ACA premium tax credits work in 2026?</h3>
        <p>The premium tax credit equals the difference between the cost of the benchmark plan (second-lowest Silver plan) and your expected contribution (a sliding-scale percentage of your income). If the benchmark plan costs $600/month and your expected contribution is $100/month, your credit is $500/month. You can take it as an advance monthly payment or claim it at tax time on Form 8962.</p>
    </div>
    <div class="faq-item">
        <h3>What are cost-sharing reductions (CSR) and how do I get them?</h3>
        <p>CSRs lower your deductible, copays, and out-of-pocket maximum. They are available only on Silver plans for income 100&ndash;250% FPL. At 200% FPL, CSR can reduce your deductible from $4,000 to under $400. You get CSR automatically when you select a Silver plan at healthcare.gov and your income qualifies&mdash;no separate application needed.</p>
    </div>
    <div class="faq-item">
        <h3>What happens if I earn more than expected and claimed too much in APTC?</h3>
        <p>You repay the excess on Form 8962 at tax time. Repayment is capped by income tier: $375 for individuals at 100&ndash;200% FPL up to full repayment for income over 400% FPL. To avoid this, update your income estimate at healthcare.gov any time your earnings change significantly during the year.</p>
    </div>
    <div class="faq-item">
        <h3>Do ACA subsidies apply to all plan types?</h3>
        <p>Premium tax credits apply to any metal-tier plan. But cost-sharing reductions apply only to Silver plans. If your income is 100&ndash;250% FPL, choosing a Silver plan gives you both subsidy types. Choosing Bronze at this income level means you forgo CSR, leaving potentially thousands of dollars in benefits unclaimed.</p>
    </div>
    <div class="faq-item">
        <h3>Can self-employed and freelance workers get ACA subsidies?</h3>
        <p>Yes. Self-employed individuals qualify for APTC based on net self-employment income. They can also separately deduct 100% of health insurance premiums on their federal tax return, which further reduces taxable income. Because freelance income fluctuates, update your income estimate quarterly at healthcare.gov to keep your APTC accurate and avoid year-end surprises.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.healthcare.gov/lower-costs/" target="_blank" rel="noopener">Healthcare.gov: Lower Your Costs &mdash; Subsidies and Cost-Sharing Reductions</a></li>
    <li><a href="https://www.kff.org/health-reform/issue-brief/explaining-health-care-reform-questions-about-health-insurance-subsidies/" target="_blank" rel="noopener">KFF: Explaining Health Insurance Subsidies</a></li>
    <li><a href="https://www.cms.gov/marketplace/resources/data/enrollment" target="_blank" rel="noopener">CMS: ACA Marketplace Enrollment and Subsidy Data 2026</a></li>
    <li><a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines" target="_blank" rel="noopener">HHS: 2026 Poverty Guidelines (FPL)</a></li>
    <li><a href="https://www.irs.gov/affordable-care-act/individuals-and-families/premium-tax-credit-the-basics" target="_blank" rel="noopener">IRS: Premium Tax Credit &mdash; The Basics</a></li>
    <li><a href="https://www.irs.gov/forms-pubs/about-form-8962" target="_blank" rel="noopener">IRS: Form 8962 &mdash; Premium Tax Credit Reconciliation</a></li>
    <li><a href="https://www.kff.org/health-reform/state-indicator/medicaid-expansion-status/" target="_blank" rel="noopener">KFF: Medicaid Expansion Status by State</a></li>
</ul>

<div class="cta-box">
    <h3>Getting bills you can&rsquo;t afford even with coverage?</h3>
    <p>BillKarma helps you dispute and negotiate medical bills regardless of your insurance status. <a href="/fight-debt">Start fighting your bill for free &rarr;</a></p>
</div>
""",
})
