"""Guide: Medical Debt and Buying a House."""

from guides import register, _embed

register("medical-debt-buying-house", {
    "title": "Medical Debt and Buying a House",
    "meta_description": "Medical debt rules changed for homebuyers. Learn how medical collections affect mortgage approval, FICO scores lenders use, and strategies to buy a house.",
    "published": "2026-02-28",
    "author": "BillKarma Team",
    "category": "Medical Debt",
    "faqs": [
        {
            "q": "Can I get a mortgage with medical debt on my credit report?",
            "a": "Yes. Medical debt under $500 no longer appears on credit reports as of April 2023, and paid medical collections are removed entirely. If your medical debt is over $500 and unpaid, it may still appear on your report and lower your FICO score. However, many mortgage programs &mdash; especially FHA and VA loans &mdash; allow approval even with collections on your report, depending on the total amount and your compensating factors like income and down payment.",
        },
        {
            "q": "Do mortgage lenders see medical debt that was removed from my credit report?",
            "a": "No. If medical debt has been removed from your credit report under the 2022&ndash;2023 bureau policies (paid collections, debts under $500, debts less than 12 months old), lenders pulling your credit will not see it. The debt is fully excluded from the report the lender receives. However, if the lender asks you to disclose all debts during manual underwriting, you may need to mention outstanding medical obligations even if they are not on your credit report.",
        },
        {
            "q": "Does medical debt affect my debt-to-income ratio for a mortgage?",
            "a": "Medical debt that does not appear on your credit report generally will not be included in your DTI ratio calculation. However, if you have active payment plans with hospitals or collection agencies, a manual underwriter may count those monthly payments toward your DTI. FHA loans require manual underwriters to consider any known recurring obligations, even if they are not on the credit report.",
        },
        {
            "q": "Should I pay off medical collections before applying for a mortgage?",
            "a": "It depends on the amount. If the debt is under $500, it is already off your report &mdash; paying it won&rsquo;t change your credit score. If it is over $500, paying it will trigger removal under bureau policy and can improve your score. But negotiate the amount first: collectors buy medical debt for 4&ndash;7 cents on the dollar, so you should settle for 30&ndash;50% of the balance. Time your payment at least 60 days before your mortgage application to allow the bureau update to process.",
        },
        {
            "q": "Which FICO score do mortgage lenders use for medical debt?",
            "a": "Most mortgage lenders still use FICO 5 (Equifax), FICO 4 (TransUnion), and FICO 2 (Experian). These are older models that treat medical collections almost the same as other collections. Fannie Mae and Freddie Mac began transitioning to FICO 10T in 2025, which ignores paid medical collections and weighs unpaid medical debt less harshly. Ask your lender which model they use before applying.",
        },
        {
            "q": "Can I get an FHA loan with unpaid medical debt?",
            "a": "Yes. FHA does not require you to pay off medical collections to qualify for a loan. FHA guidelines specifically state that medical collections are excluded from the calculation of outstanding collections that would otherwise require a payment plan or payoff. However, during manual underwriting, the underwriter may ask for a letter of explanation about large medical debts and may consider them as a compensating factor.",
        },
    ],
    "body": f"""
<p class="lead">You want to buy a house, but you have medical debt. Good news: the rules have changed dramatically. Since 2023, medical collections under $500 no longer appear on credit reports. Since April 2023, paid medical collections are removed entirely. And the CFPB proposed removing all medical debt from credit reports &mdash; though that rule was struck down in 2025. Here&rsquo;s exactly how medical debt affects your mortgage application today, which loan programs are most forgiving, and how to position yourself for approval.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#timeline">The 2022&ndash;2026 medical debt credit report timeline</a></li>
        <li><a href="#what-lenders-see">What mortgage lenders actually see</a></li>
        <li><a href="#dti-ratio">DTI ratio: the hidden impact of medical debt</a></li>
        <li><a href="#loan-types">FHA, VA, and conventional loan differences</a></li>
        <li><a href="#pay-off-decision">Should you pay off medical debt before applying?</a></li>
        <li><a href="#explanation-letter">Letter of explanation for medical debt</a></li>
        <li><a href="#negotiation-strategies">Negotiation strategies before your mortgage</a></li>
        <li><a href="#state-protections">State protections that help homebuyers</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="timeline">1. The 2022&ndash;2026 medical debt credit report timeline</h2>

<p>The rules governing how medical debt appears on credit reports have shifted multiple times since 2022. Each change has direct consequences for mortgage applicants. Here is the chronological breakdown of every major change and its current status.</p>

<table>
    <thead>
        <tr>
            <th>Date</th>
            <th>Change</th>
            <th>Impact on Homebuyers</th>
            <th>Status (Feb 2026)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>July 2022</td>
            <td>Three bureaus remove paid medical collections from reports</td>
            <td>Paying a medical collection now triggers removal &mdash; no more 7-year mark</td>
            <td>Active</td>
        </tr>
        <tr>
            <td>July 2022</td>
            <td>Medical debt reporting waiting period extended from 180 days to 12 months</td>
            <td>New medical debt cannot appear on your report for a full year &mdash; more time to resolve before mortgage application</td>
            <td>Active</td>
        </tr>
        <tr>
            <td>April 2023</td>
            <td>Medical collections under $500 removed from all reports</td>
            <td>Small medical debts no longer drag down your mortgage score</td>
            <td>Active</td>
        </tr>
        <tr>
            <td>January 2025</td>
            <td>CFPB finalizes rule banning all medical debt from credit reports</td>
            <td>Would have eliminated $49 billion in reported medical debt for 15 million Americans</td>
            <td>Struck down (July 2025)</td>
        </tr>
        <tr>
            <td>July 2025</td>
            <td>Federal court strikes down CFPB rule in <em>AHA v. CFPB</em></td>
            <td>Unpaid medical debt over $500 (12+ months old) remains reportable at federal level</td>
            <td>Final &mdash; no appeal</td>
        </tr>
        <tr>
            <td>2025&ndash;2026</td>
            <td>10+ states enact medical debt credit reporting laws</td>
            <td>Homebuyers in CO, CA, NY, and other states get additional protection</td>
            <td>Active (state-by-state)</td>
        </tr>
    </tbody>
</table>

<p>The bottom line for 2026 mortgage applicants: paid medical collections are gone from your report. Debts under $500 are gone. But unpaid medical debt over $500 that is more than 12 months old can still appear &mdash; and still hurt your mortgage score &mdash; unless your state has passed additional protections. For the full breakdown of what&rsquo;s currently reportable, see our companion guide on <a href="/guides/medical-debt-credit-report-2026/">medical debt and your credit report in 2026</a>.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>The 2022&ndash;2023 bureau changes are the most important for homebuyers. Paid medical collections are removed. Debts under $500 are removed. You have 12 months before new medical debt can appear. These three rules alone eliminate the majority of medical debt that previously blocked mortgage approvals.</p>
</div>

<h2 id="what-lenders-see">2. What mortgage lenders actually see</h2>

<p>Understanding what your lender sees when they pull your credit is critical. The scoring model matters enormously &mdash; and mortgage lenders use older models that treat medical debt more harshly than the scores you see on free monitoring apps.</p>

<p><strong>The mortgage FICO problem:</strong> Most mortgage lenders still pull FICO 5 (Equifax), FICO 4 (TransUnion), and FICO 2 (Experian). These are legacy scoring models that treat medical collections nearly the same as other types of collections. The free VantageScore you see on Credit Karma or your bank&rsquo;s app ignores paid medical collections and weighs unpaid medical debt less &mdash; but that is not what your mortgage lender is using.</p>

<table>
    <thead>
        <tr>
            <th>Scoring Model</th>
            <th>Used By</th>
            <th>Paid Medical Collections</th>
            <th>Unpaid Medical Collections</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>FICO 2, 4, 5 (mortgage scores)</td>
            <td>Most mortgage lenders (2026)</td>
            <td>Off report &mdash; no impact (bureau policy)</td>
            <td>Full negative impact (similar to other collections)</td>
        </tr>
        <tr>
            <td>FICO 8</td>
            <td>Credit cards, auto loans</td>
            <td>Off report &mdash; no impact (bureau policy)</td>
            <td>Full negative impact (reduced weight vs. FICO 2/4/5)</td>
        </tr>
        <tr>
            <td>FICO 9</td>
            <td>Some newer mortgage products</td>
            <td>Ignored entirely by scoring model</td>
            <td>Reduced weight vs. non-medical collections</td>
        </tr>
        <tr>
            <td>FICO 10T</td>
            <td>Fannie Mae / Freddie Mac (transitioning)</td>
            <td>Ignored entirely by scoring model</td>
            <td>Reduced weight; uses trended data</td>
        </tr>
        <tr>
            <td>VantageScore 4.0</td>
            <td>Free monitoring apps (not used for mortgages)</td>
            <td>Ignored entirely</td>
            <td>Significantly reduced weight</td>
        </tr>
    </tbody>
</table>

<p><strong>Do lenders see removed debt?</strong> No. If medical debt has been removed from your credit report under bureau policies (paid, under $500, or less than 12 months old), lenders cannot see it. The data is not on the report they pull. There is no hidden record or secondary database that reveals removed medical collections to mortgage lenders.</p>

<p><strong>The FICO 10T transition:</strong> Fannie Mae and Freddie Mac mandated that lenders begin transitioning to FICO 10T in 2025. FICO 10T ignores paid medical collections at the scoring model level (in addition to bureau-level removal) and weighs unpaid medical debt less harshly. However, adoption is uneven &mdash; many lenders still pull legacy FICO 2/4/5 scores. Ask your lender which version they use <em>before</em> you apply.</p>

<p>For a deeper understanding of how these scoring models work, see our guide on <a href="/guides/medical-debt-credit-report-2026/">medical debt and credit reports in 2026</a>.</p>

<h2 id="dti-ratio">3. DTI ratio: the hidden impact of medical debt</h2>

<p>Your credit score is only half the equation. Mortgage lenders also calculate your debt-to-income (DTI) ratio &mdash; the percentage of your gross monthly income going to debt payments. Most conventional loans require a DTI below 43%. FHA loans may allow up to 50% with compensating factors. This is where medical debt can hurt even if it is not on your credit report.</p>

<p><strong>When medical debt affects DTI:</strong> If you have active payment plans with hospitals, clinics, or collection agencies, those monthly payments count toward your DTI if the lender discovers them. A $200/month hospital payment plan on a $40,000 income adds 6 percentage points to your DTI &mdash; potentially enough to disqualify you.</p>

<p><strong>How lenders discover medical payment plans:</strong></p>
<ul>
    <li><strong>Bank statements:</strong> Most lenders request 2&ndash;3 months of bank statements. Regular payments to a hospital or collection agency will be visible.</li>
    <li><strong>Manual underwriting:</strong> FHA manual underwriters are required to consider any known recurring debts, even those not on the credit report.</li>
    <li><strong>Asset verification:</strong> Large, recent payments to medical providers may be flagged during asset review.</li>
    <li><strong>Direct questions:</strong> Some loan applications ask whether you have any outstanding debts not shown on your credit report.</li>
</ul>

<p><strong>How to handle this:</strong> If you have a medical payment plan, factor those payments into your DTI calculation before applying. If the payment plan pushes your DTI above qualifying thresholds, consider negotiating a lump-sum settlement (see Section 7) to eliminate the monthly obligation before your mortgage application. A one-time settlement payment is not a recurring debt and does not affect DTI.</p>

<p><a href="/scan">Upload your medical bills to BillKarma</a> to check for errors first &mdash; if the original charges were wrong, you may owe less than you think, which means a smaller settlement and better DTI.</p>

<h2 id="loan-types">4. FHA, VA, and conventional loan differences</h2>

<p>Not all mortgage programs treat medical debt the same way. The type of loan you apply for determines how much your medical debt matters during underwriting.</p>

<table>
    <thead>
        <tr>
            <th>Loan Type</th>
            <th>Medical Collections Policy</th>
            <th>DTI Limit</th>
            <th>Best For</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Conventional (Fannie/Freddie)</td>
            <td>Score-driven &mdash; medical collections affect FICO; no separate medical debt review</td>
            <td>43&ndash;45%</td>
            <td>Borrowers with 660+ score, no large unpaid medical debt</td>
        </tr>
        <tr>
            <td>FHA</td>
            <td>Medical collections explicitly excluded from outstanding collection calculation; manual underwriting may review large debts</td>
            <td>43% (up to 50% with compensating factors)</td>
            <td>Borrowers with 580+ score, medical debt in collections</td>
        </tr>
        <tr>
            <td>VA</td>
            <td>Most lenient &mdash; medical collections generally not counted against borrower; residual income test used instead of strict DTI</td>
            <td>41% guideline (flexible)</td>
            <td>Eligible veterans with any amount of medical debt</td>
        </tr>
        <tr>
            <td>USDA</td>
            <td>Similar to FHA &mdash; medical collections may be excluded; manual underwriting considers all debts</td>
            <td>41%</td>
            <td>Rural buyers with moderate medical debt</td>
        </tr>
    </tbody>
</table>

<p><strong>FHA&rsquo;s medical debt exception:</strong> This is the most important detail for homebuyers with medical debt. FHA Handbook 4000.1 specifically states that medical collections are excluded when calculating total outstanding collections. For conventional loans, if you have more than $2,000 in total collections, the lender must either verify a payment plan or use 5% of the balance as a monthly DTI obligation. FHA exempts medical debt from this calculation entirely.</p>

<p><strong>VA&rsquo;s residual income approach:</strong> VA loans use a residual income test instead of relying solely on DTI ratios. This means the VA looks at how much money you have left after all expenses &mdash; not just the ratio of debt to income. Medical payment plans reduce your residual income but are treated more leniently than other debts. Combined with the VA&rsquo;s overall borrower-friendly guidelines, this makes VA loans the most forgiving option for buyers with medical debt.</p>

<div class="case-study">
    <h3>Case study: FHA approval with $8,200 in medical collections</h3>
    <p>A BillKarma user in Houston had $8,200 in medical collections from a 2023 hospitalization. His FICO 5 score was 612. He applied for an FHA loan with a 3.5% down payment. Under FHA guidelines, the $8,200 in medical collections was excluded from his outstanding collection calculation. The underwriter asked for a letter of explanation (see Section 6) but did not require him to pay off or establish payment plans for the medical debt.</p>
    <p>Before applying, he <a href="/scan">uploaded his hospital bills to BillKarma</a> and found $1,400 in billing errors (duplicate lab charges and an upcoded ER visit). He disputed the errors with the hospital, reducing the true balance to $6,800. The FHA loan was approved. His mortgage payment was $1,340/month on a $210,000 home.</p>
    <p><strong>Key lesson:</strong> FHA explicitly excludes medical collections from the calculation that would otherwise require payoff. But always check the underlying bills for errors &mdash; reducing the true balance strengthens your application.</p>
</div>

<h2 id="pay-off-decision">5. Should you pay off medical debt before applying?</h2>

<p>This is the most common question homebuyers with medical debt ask. The answer depends on the amount, the timing, and whether the debt appears on your credit report.</p>

<p><strong>If the debt is under $500:</strong> It is already off your credit report. Paying it will not change your credit score. Do not rush to pay it before a mortgage application &mdash; it is invisible to lenders. Focus your cash on your down payment and closing costs instead.</p>

<p><strong>If the debt is over $500 and unpaid:</strong> Negotiate before paying. Collectors bought the debt for 4&ndash;7 cents on the dollar. Use the strategies in Section 7 to <a href="/guides/settle-medical-debt-collections/">settle for 30&ndash;50% of the balance</a>. Once you pay (even a settlement), the bureau policy removes the paid collection from your report. Time your payment at least 45&ndash;60 days before your mortgage application to allow the bureau update to process.</p>

<p><strong>If the debt is in collections and you want it deleted fast:</strong> Negotiate a <a href="/guides/pay-for-delete-medical-debt/">pay-for-delete agreement</a>. While paid medical collections are already removed under bureau policy, a pay-for-delete adds a written guarantee and may speed up removal. Some mortgage lenders can also request a &ldquo;rapid rescore&rdquo; through their credit reporting provider, which updates your score within 3&ndash;5 business days after you provide proof of payment.</p>

<p><strong>If the debt is in a payment plan:</strong> Consider settling the remaining balance with a lump sum before applying. A monthly payment plan counts toward your DTI ratio, but a settled debt does not. If you have $3,000 remaining on a $150/month plan, settling for $1,200 eliminates the $150/month DTI hit &mdash; which could be the difference between approval and denial.</p>

<p><strong>Timing matters:</strong> Changes to your credit report take time to propagate. If you pay off or settle a medical collection, allow 30&ndash;60 days for the bureaus to update before applying for your mortgage. If you are already in the application process, ask your loan officer about a rapid rescore, which can reflect the change within 3&ndash;5 business days.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Do not deplete your savings to pay off medical debt before a mortgage application. If the debt is under $500, it is already invisible. If it is over $500, negotiate a settlement at 30&ndash;50% and time the payment 45&ndash;60 days before your application. Preserving cash for your down payment and closing costs is often more important than eliminating a medical collection. Use our <a href="/guides/settle-medical-debt-collections/">settlement guide</a> to negotiate the lowest possible amount.</p>
</div>

<h2 id="explanation-letter">6. Letter of explanation for medical debt</h2>

<p>If your lender asks about medical debt during underwriting &mdash; especially during FHA or VA manual underwriting &mdash; you will need to submit a letter of explanation (LOE). This letter frames your medical debt as a one-time hardship rather than a pattern of financial irresponsibility. Here is how to write one that works.</p>

<p><strong>When lenders ask for an LOE:</strong></p>
<ul>
    <li>FHA manual underwriting on loans with credit scores below 620</li>
    <li>Any loan with large medical collections (typically over $5,000)</li>
    <li>When bank statements show regular payments to medical providers or collectors</li>
    <li>When the underwriter identifies medical debt during the verification process</li>
</ul>

<p><strong>What to include in your letter:</strong></p>
<ul>
    <li><strong>The medical event:</strong> Briefly describe the illness, injury, or procedure. You do not need to share detailed medical information &mdash; a general description is sufficient.</li>
    <li><strong>The financial impact:</strong> Explain how the medical event created unexpected costs. Mention if you were uninsured, underinsured, or if the bill was significantly higher than expected.</li>
    <li><strong>What you&rsquo;ve done about it:</strong> Describe steps taken &mdash; payment plans, settlement negotiations, financial assistance applications, bill disputes.</li>
    <li><strong>Your current financial stability:</strong> Emphasize current income stability, savings, and ability to handle the mortgage payment. Show that the medical event was an isolated incident, not an ongoing financial pattern.</li>
</ul>

<p><strong>Template language:</strong></p>
<blockquote>
    <p>&ldquo;In [month/year], I [or my dependent] required [brief medical description &mdash; e.g., emergency surgery, hospitalization, cancer treatment]. The total charges were $[amount], of which $[amount] was not covered by insurance. I have since [negotiated a settlement / established a payment plan / applied for financial assistance / disputed billing errors]. This was an isolated medical event and does not reflect my ongoing financial management. My current income is $[amount] per month, and I have $[amount] in savings. I am fully capable of meeting my mortgage obligations.&rdquo;</p>
</blockquote>

<p><strong>What NOT to say:</strong> Do not apologize. Do not suggest you are financially unstable. Do not say &ldquo;I can&rsquo;t afford&rdquo; anything. Frame the medical debt as a resolved or resolving situation, not an ongoing crisis. The goal is to reassure the underwriter that you are creditworthy despite a medical hardship.</p>

<h2 id="negotiation-strategies">7. Negotiation strategies before your mortgage</h2>

<p>If you have medical debt that could affect your mortgage application, the weeks before you apply are the time to act. Here are the strategies that produce the best results for homebuyers.</p>

<p><strong>Strategy 1: Settle collections for less.</strong> Collectors purchased your medical debt for pennies. Offer 30&ndash;40% of the balance as a lump-sum settlement. Once paid, the collection is removed from your credit report under bureau policy. See our full guide on <a href="/guides/settle-medical-debt-collections/">settling medical debt in collections</a> for scripts and letter templates.</p>

<p><strong>Strategy 2: Get a pay-for-delete agreement.</strong> While paying any medical collection triggers removal under bureau policy, a <a href="/guides/pay-for-delete-medical-debt/">written pay-for-delete agreement</a> provides an additional guarantee and may expedite the process. Get the agreement in writing before sending any payment.</p>

<p><strong>Strategy 3: Dispute inaccurate reporting.</strong> Pull your credit reports from all three bureaus. If any medical collection violates current rules (paid collections still showing, debts under $500, debts less than 12 months old), dispute them immediately. Bureau disputes must be resolved within 30 days. This alone can remove entries that should not be there.</p>

<p><strong>Strategy 4: Check the underlying bill for errors.</strong> <a href="/scan">Upload your original medical bill to BillKarma</a> before settling with a collector. If the original bill contained errors &mdash; duplicate charges, upcoding, unbundling &mdash; the collection amount is wrong. You may owe significantly less than the collector claims. BillKarma&rsquo;s analysis shows 38% of medical bills in collections contain billing errors.</p>

<p><strong>Strategy 5: Request a rapid rescore.</strong> If you pay off or settle a medical collection during the mortgage process, ask your loan officer to request a rapid rescore through their credit reporting provider. A rapid rescore updates your FICO score within 3&ndash;5 business days, compared to the 30&ndash;60 days a normal bureau update takes. This can save weeks in your home-buying timeline.</p>

<p><strong>Strategy 6: Apply for financial assistance.</strong> If the underlying hospital is a nonprofit (60% of US hospitals), you may qualify for charity care or financial assistance that reduces or eliminates the debt entirely. See our guide on <a href="/guides/medical-debt-forgiveness-programs/">medical debt forgiveness programs</a> for eligibility details and application steps.</p>

<h2 id="state-protections">8. State protections that help homebuyers</h2>

<p>With the federal CFPB rule struck down in 2025, state-level protections have become the most powerful shield for homebuyers with medical debt. If you live in one of these states, medical debt may not appear on your credit report at all &mdash; meaning it has zero impact on your mortgage score.</p>

<p><strong>States that ban all medical debt from credit reports:</strong></p>
<ul>
    <li><strong>California</strong> (SB 1061, 2025) &mdash; No medical debt on credit reports, statewide</li>
    <li><strong>New York</strong> (Medical Debt Protection Act, 2025) &mdash; No medical debt on reports; also caps interest at 2% and restricts wage garnishment</li>
    <li><strong>Washington</strong> (HB 1531, 2025) &mdash; No medical debt reporting; restricts collection lawsuits</li>
    <li><strong>Minnesota</strong> (HF 2127, 2026) &mdash; No medical debt reporting; caps interest at 0%</li>
</ul>

<p><strong>States with elevated protection thresholds:</strong></p>
<ul>
    <li><strong>Colorado</strong> (HB 22-1285, expanded 2025) &mdash; Medical debt under $2,500 excluded from reports; 120-day notice required before collections</li>
    <li><strong>Nevada</strong> (AB 307, 2025) &mdash; Medical debt under $2,500 excluded; financial hardship screening required</li>
    <li><strong>Connecticut</strong> (SB 1004, 2025) &mdash; Medical debt under $1,000 excluded; 180-day notice before collection</li>
</ul>

<p><strong>States with income-based protections:</strong></p>
<ul>
    <li><strong>Illinois</strong> (Patient Billing Act amendments, 2025) &mdash; No reporting for patients under 400% FPL</li>
    <li><strong>Oregon</strong> (SB 490, 2025) &mdash; No reporting for patients under 400% FPL; 240-day notice before collections</li>
    <li><strong>Maryland</strong> (Medical Debt Protection Act, 2024) &mdash; Restricts credit reporting and collection for patients under 300% FPL</li>
</ul>

<p><strong>What this means for homebuyers:</strong> If you live in California, New York, Washington, or Minnesota, medical debt cannot appear on your credit report under state law &mdash; regardless of the amount. In Colorado or Nevada, debts under $2,500 are protected. If you&rsquo;re buying a home in one of these states and a medical collection appears on your report, dispute it immediately and cite the specific state statute. For detailed state-by-state rules, see our guide on <a href="/guides/medical-debt-credit-report-2026/">medical debt and credit reports in 2026</a>.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Can I get a mortgage with medical debt on my credit report?</h3>
        <p>Yes. Medical debt under $500 no longer appears on credit reports, and paid medical collections are removed entirely. If you have unpaid medical debt over $500 on your report, it may lower your FICO score, but many mortgage programs &mdash; especially FHA and VA &mdash; allow approval even with medical collections. FHA specifically excludes medical collections from the outstanding collection calculation that would otherwise require payoff or a payment plan.</p>
    </div>

    <div class="faq-item">
        <h3>Do mortgage lenders see medical debt that was removed from my credit report?</h3>
        <p>No. Removed medical debt is not visible to lenders. If the debt was excluded under the 2022&ndash;2023 bureau policies, it does not appear on the credit report the lender pulls. However, during manual underwriting, lenders may ask you to disclose all outstanding debts &mdash; and if you have active hospital payment plans visible on your bank statements, those may come up during asset verification.</p>
    </div>

    <div class="faq-item">
        <h3>Does medical debt affect my debt-to-income ratio for a mortgage?</h3>
        <p>Medical debt that is not on your credit report generally does not affect your DTI calculation. However, if you have active payment plans with hospitals or collectors, those monthly payments may be counted toward your DTI during manual underwriting. Consider settling the remaining balance with a lump sum before applying to eliminate the recurring monthly obligation from your DTI.</p>
    </div>

    <div class="faq-item">
        <h3>Should I pay off medical collections before applying for a mortgage?</h3>
        <p>If the debt is under $500, do not pay it to improve your credit &mdash; it is already off your report. If it is over $500, negotiate a settlement at 30&ndash;50% of the balance and pay at least 45&ndash;60 days before your application. Do not deplete your down payment savings to pay off medical debt. For FHA and VA loans, medical collections are treated more leniently than other debts, so paying them off may be less urgent than preserving cash.</p>
    </div>

    <div class="faq-item">
        <h3>Which FICO score do mortgage lenders use for medical debt?</h3>
        <p>Most mortgage lenders use FICO 5 (Equifax), FICO 4 (TransUnion), and FICO 2 (Experian) &mdash; older models that treat medical collections almost the same as other collections. Fannie Mae and Freddie Mac began transitioning to FICO 10T in 2025, which is more forgiving. The VantageScore you see on free apps is not used for mortgages. Ask your lender which model they pull before you apply.</p>
    </div>

    <div class="faq-item">
        <h3>Can I get an FHA loan with unpaid medical debt?</h3>
        <p>Yes. FHA Handbook 4000.1 explicitly excludes medical collections from the outstanding collection calculation. You do not need to pay off medical collections to qualify for an FHA loan. During manual underwriting, the underwriter may ask for a letter of explanation about large medical debts, but medical collections alone will not disqualify you. FHA loans require a minimum FICO of 580 with 3.5% down, or 500 with 10% down.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.consumerfinance.gov/about-us/newsroom/cfpb-finalizes-rule-to-remove-medical-debt-from-credit-reports/" target="_blank" rel="noopener">CFPB &mdash; Final Rule to Remove Medical Debt from Credit Reports (January 2025)</a></li>
    <li><a href="https://www.consumerfinance.gov/data-research/research-reports/medical-debt-burden-in-the-united-states/" target="_blank" rel="noopener">CFPB &mdash; Medical Debt Burden in the United States (Research Report)</a></li>
    <li><a href="https://www.myfico.com/credit-education/credit-scores/fico-score-versions" target="_blank" rel="noopener">myFICO &mdash; FICO Score Versions and How They Treat Medical Debt</a></li>
    <li><a href="https://www.hud.gov/sites/dfiles/OCHCO/documents/4000.1hsgh-112422.pdf" target="_blank" rel="noopener">FHA Handbook 4000.1 &mdash; Single Family Housing Policy Handbook (Section on Collections)</a></li>
    <li><a href="https://www.va.gov/housing-assistance/home-loans/" target="_blank" rel="noopener">VA Home Loans &mdash; Eligibility and Underwriting Guidelines</a></li>
    <li><a href="https://www.equifax.com/newsroom/all-news/equifax-experian-transunion-support-consumers-with-changes-to-medical-collection-debt-reporting/" target="_blank" rel="noopener">Equifax, Experian, TransUnion &mdash; Joint Announcement on Medical Collection Reporting Changes (2022)</a></li>
    <li><a href="https://www.annualcreditreport.com" target="_blank" rel="noopener">AnnualCreditReport.com &mdash; Free Weekly Credit Reports</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/the-burden-of-medical-debt-in-the-united-states/" target="_blank" rel="noopener">KFF &mdash; The Burden of Medical Debt in the United States</a></li>
</ul>
""",
})
