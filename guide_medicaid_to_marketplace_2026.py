"""Guide: Lost Medicaid Coverage 2026 - Transition to Marketplace."""

from guides import register, _embed

register("medicaid-to-marketplace-2026", {
    "title": "Lost Medicaid Coverage in 2026? Your Step-by-Step Guide to Staying Insured",
    "meta_description": "Millions are losing Medicaid in 2026 due to work requirements and eligibility checks. Step-by-step guide to marketplace enrollment, subsidies, and alternatives.",
    "published": "2026-03-02",
    "author": "BillKarma Team",
    "category": "Health Insurance",
    "faqs": [
        {
            "q": "Why am I losing my Medicaid coverage in 2026?",
            "a": "Three main reasons: the One Big Beautiful Bill Act's new work requirements (80 hours/month of documented community engagement starting December 2026), more frequent eligibility checks (every 6 months starting January 2027, but some states have started early), and routine redetermination catching income changes. During the 2023-2024 Medicaid unwinding, 69% of disenrollments were procedural (paperwork issues), not because people were actually ineligible.",
        },
        {
            "q": "How do I get marketplace insurance after losing Medicaid?",
            "a": "Losing Medicaid triggers a 60-day Special Enrollment Period on the ACA marketplace. Go to HealthCare.gov (or your state's marketplace), select 'loss of coverage' as your qualifying event, and complete an application. If your income is below 400% FPL, you qualify for premium subsidies. Bronze plans with subsidies can cost under $100/month. Do not wait - your 60-day window starts when your Medicaid ends.",
        },
        {
            "q": "Will I qualify for subsidies on the marketplace?",
            "a": "If your household income is between 100-400% FPL (approximately $15,060-$62,400 for an individual in 2026), you qualify for premium tax credits that reduce your monthly premium. At lower income levels, you may also qualify for cost-sharing reductions that lower your deductible and copays on Silver plans. Use the HealthCare.gov subsidy calculator to see your estimated monthly cost.",
        },
        {
            "q": "What if I can't afford marketplace insurance?",
            "a": "Several options: check if you qualify for Medicaid in your state (income limits vary), apply for your state's Basic Health Plan if available (MN and NY offer plans for people earning 138-200% FPL), check employer coverage options, explore hospital financial assistance programs for when you need care, and use community health centers that serve patients on a sliding fee scale regardless of insurance status.",
        },
        {
            "q": "Can I appeal my Medicaid termination?",
            "a": "Yes. File an appeal within 10 days of receiving the termination notice to maintain coverage during the appeal process. If you file after 10 days but within your state's appeal deadline (usually 30-90 days), you can still appeal but may have a gap in coverage. Common grounds for appeal: you returned paperwork but it wasn't received, your income hasn't changed, or you qualify for an exemption from work requirements.",
        },
        {
            "q": "What happens to my children's coverage if I lose Medicaid?",
            "a": "Children's coverage is separate from adult coverage. CHIP (Children's Health Insurance Program) covers children in families earning up to 200-400% FPL depending on the state, with minimal or zero premiums. Even if you lose your own Medicaid, your children likely still qualify. Apply at InsureKidsNow.gov or through your state Medicaid office. The OBBBA work requirements do not apply to children's Medicaid or CHIP.",
        },
    ],
    "body": f"""
<p class="lead">Millions of Americans are losing Medicaid coverage in 2026 &mdash; through the OBBBA&rsquo;s new work requirements, more frequent eligibility checks, and routine redetermination. The CBO estimates <strong>11.8 million</strong> will lose Medicaid directly from the new law alone. If you just received a termination notice, don&rsquo;t panic. You have a <strong>60-day window</strong> to enroll in marketplace coverage, and subsidies may make it more affordable than you think. Here is exactly what to do, step by step.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#why-losing">Why you&rsquo;re losing Medicaid</a></li>
        <li><a href="#appeal-first">Step 1: Appeal if the termination is wrong</a></li>
        <li><a href="#marketplace">Step 2: Enroll in marketplace coverage</a></li>
        <li><a href="#subsidies">Step 3: Understand your subsidies</a></li>
        <li><a href="#choose-plan">Step 4: Choose the right plan</a></li>
        <li><a href="#alternatives">If you can&rsquo;t afford marketplace coverage</a></li>
        <li><a href="#protect-bills">Protecting yourself from medical bills during the transition</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="why-losing">1. Why you&rsquo;re losing Medicaid</h2>

<p>There are three main pathways pushing people off Medicaid in 2026:</p>

<p><strong>Work requirements (OBBBA).</strong> Starting December 2026, Medicaid expansion enrollees ages 19&ndash;64 must document 80 hours/month of "community engagement" (work, volunteering, education). Failure to document &mdash; even if you are actually working &mdash; means loss of coverage. Arkansas&rsquo;s experience showed 95% of people who lost coverage were working or qualified for exemptions but failed the documentation process. See our <a href="/guides/medicaid-cuts-2026">OBBBA Medicaid cuts guide</a> for details.</p>

<p><strong>Six-month eligibility checks (starting January 2027, some states earlier).</strong> States must now re-verify expansion enrollee eligibility every 6 months instead of 12 months. This doubles the chances of "procedural disenrollment" &mdash; losing coverage because paperwork wasn&rsquo;t returned or processed correctly.</p>

<p><strong>Routine redetermination.</strong> Even before the OBBBA changes, the ongoing Medicaid redetermination process (which began after the pandemic-era continuous enrollment ended) continues to disenroll people whose incomes have risen above the threshold or who fail to respond to renewal notices.</p>

<div class="key-takeaway">
    <strong>Check your mail and your state&rsquo;s Medicaid portal daily.</strong> Medicaid termination notices arrive by mail and through online portals. Missing a notice can mean losing coverage before you even know it&rsquo;s at risk. Set up text or email alerts with your state Medicaid agency if available.
</div>

<h2 id="appeal-first">2. Step 1: Appeal if the termination is wrong</h2>

<p>Before accepting the termination, determine if you should appeal. Common scenarios where an appeal can restore your coverage:</p>

<ul>
    <li>You returned your renewal paperwork but it wasn&rsquo;t received or processed</li>
    <li>Your income hasn&rsquo;t changed and you&rsquo;re still eligible</li>
    <li>You qualify for a work requirement exemption (parent of child under 13, disabled, medical condition, student)</li>
    <li>Your state made an error in processing your redetermination</li>
    <li>You didn&rsquo;t receive the renewal notice (wrong address on file)</li>
</ul>

<p><strong>The 10-day rule:</strong> If you file your appeal within <strong>10 days</strong> of the date on the termination notice, your Medicaid coverage continues during the appeal process. This is critical &mdash; it means no gap in coverage while your appeal is reviewed. If you file after 10 days, you can still appeal but may have a gap.</p>

<p><strong>How to appeal:</strong> Contact your state Medicaid agency by phone and in writing. Request a "fair hearing." Provide documentation: copies of returned paperwork, proof of income, proof of work hours or exemption eligibility. Keep copies of everything.</p>

<h2 id="marketplace">3. Step 2: Enroll in marketplace coverage</h2>

<p>Whether your appeal succeeds or not, start the marketplace enrollment process immediately. You have <strong>60 days from your Medicaid termination date</strong> to enroll in a marketplace plan through the Special Enrollment Period.</p>

<p><strong>How to enroll:</strong></p>

<ol>
    <li>Go to <a href="https://www.healthcare.gov/" target="_blank" rel="noopener">HealthCare.gov</a> (or your state&rsquo;s marketplace if your state runs its own)</li>
    <li>Create an account or log in</li>
    <li>Select "loss of health coverage" as your qualifying life event</li>
    <li>Enter the date your Medicaid ends</li>
    <li>Complete the application with household income information</li>
    <li>Review plan options and subsidies</li>
    <li>Select a plan and confirm enrollment</li>
</ol>

<p><strong>Key dates to know:</strong></p>
<ul>
    <li>Coverage can start as soon as the 1st of the month following your enrollment</li>
    <li>Your 60-day SEP clock starts on the date your Medicaid coverage ends</li>
    <li>If you miss the 60-day window, you must wait until the next open enrollment period (November 1 &mdash; January 15)</li>
</ul>

<h2 id="subsidies">4. Step 3: Understand your subsidies</h2>

<p>Most people losing Medicaid qualify for meaningful marketplace subsidies. The key factor is your income relative to the Federal Poverty Level:</p>

<table>
    <thead>
        <tr><th>Income range (individual)</th><th>% of FPL</th><th>Expected premium (% of income)</th><th>Estimated monthly cost (Silver plan)</th></tr>
    </thead>
    <tbody>
        <tr><td>$15,060&ndash;$18,825</td><td>100&ndash;125% FPL</td><td>0&ndash;2% of income</td><td>$0&ndash;$31</td></tr>
        <tr><td>$18,826&ndash;$22,590</td><td>125&ndash;150% FPL</td><td>2&ndash;4% of income</td><td>$31&ndash;$75</td></tr>
        <tr><td>$22,591&ndash;$30,120</td><td>150&ndash;200% FPL</td><td>4&ndash;6.5% of income</td><td>$75&ndash;$163</td></tr>
        <tr><td>$30,121&ndash;$45,180</td><td>200&ndash;300% FPL</td><td>6.5&ndash;8.5% of income</td><td>$163&ndash;$320</td></tr>
        <tr><td>$45,181&ndash;$60,240</td><td>300&ndash;400% FPL</td><td>8.5% of income</td><td>$320&ndash;$427</td></tr>
        <tr><td>&gt;$60,240</td><td>&gt;400% FPL</td><td>No subsidy</td><td>Full premium ($500&ndash;$800+)</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Cost-sharing reductions (CSRs):</strong> If your income is 100&ndash;250% FPL, choosing a <strong>Silver plan</strong> unlocks cost-sharing reductions that dramatically lower your deductible, copays, and out-of-pocket maximum. At 100&ndash;150% FPL, a CSR Silver plan has a deductible as low as $0&ndash;$75 and an out-of-pocket max of $3,050. CSRs are only available on Silver plans &mdash; not Bronze, Gold, or Platinum. This is the single most important thing former Medicaid enrollees need to know about marketplace coverage.
</div>

<h2 id="choose-plan">5. Step 4: Choose the right plan</h2>

<p>Former Medicaid enrollees transitioning to marketplace coverage should prioritize:</p>

<p><strong>If your income is 100&ndash;250% FPL: Choose Silver.</strong> The cost-sharing reductions make Silver plans the best value by far. Your deductible and copays will be dramatically lower than any other tier. The premium may be slightly higher than Bronze, but the total cost of care will be lower.</p>

<p><strong>If your income is 250&ndash;400% FPL: Compare Bronze and Silver.</strong> Without CSRs, the math depends on how much care you use. Bronze plans have lower premiums but higher deductibles ($7,000+). Silver plans cost more monthly but have moderate deductibles ($3,000&ndash;$5,000). If you expect to use significant medical services, Silver may still save money overall.</p>

<p><strong>Check the provider network.</strong> If you have current doctors you want to keep, verify they are in-network for the plans you&rsquo;re considering. Marketplace plan networks are often narrower than Medicaid networks.</p>

<p><strong>Check the drug formulary.</strong> If you take regular medications, verify they are covered by the plan&rsquo;s formulary before enrolling. Use the plan&rsquo;s drug search tool on HealthCare.gov.</p>

<h2 id="alternatives">6. If you can&rsquo;t afford marketplace coverage</h2>

<p>If marketplace coverage is still too expensive even with subsidies, you have options:</p>

<p><strong>Basic Health Plan (BHP).</strong> Minnesota and New York offer state-funded health plans for people earning 138&ndash;200% FPL. New York&rsquo;s Essential Plan costs $0&ndash;$20/month with minimal cost-sharing. Minnesota&rsquo;s MinnesotaCare covers adults up to 200% FPL. If you live in one of these states and earn too much for Medicaid but not enough for affordable marketplace coverage, BHP is your best option.</p>

<p><strong>Employer coverage.</strong> If your employer offers health insurance, losing Medicaid is a qualifying event that lets you enroll outside of open enrollment. Check with your HR department immediately.</p>

<p><strong>CHIP for children.</strong> Even if you can&rsquo;t afford coverage for yourself, your children likely qualify for CHIP. Income limits range from 200&ndash;400% FPL depending on your state. Apply at <a href="https://www.insurekidsnow.gov/" target="_blank" rel="noopener">InsureKidsNow.gov</a>.</p>

<p><strong>Community health centers.</strong> FQHCs serve patients on a sliding fee scale based on ability to pay. You don&rsquo;t need insurance. Find one at <a href="https://findahealthcenter.hrsa.gov/" target="_blank" rel="noopener">FindAHealthCenter.hrsa.gov</a>.</p>

<p><strong>Hospital financial assistance.</strong> If you need hospital care without insurance, <a href="/charity-care">check your eligibility for charity care</a>. Nonprofit hospitals must offer financial assistance. Many provide free care up to 200% FPL and discounts up to 400% FPL.</p>

<h2 id="protect-bills">7. Protecting yourself from medical bills during the transition</h2>

<p>The gap between losing Medicaid and starting marketplace coverage is your most vulnerable period. Here is how to minimize financial risk:</p>

<ol>
    <li><strong>Time your enrollment carefully.</strong> If your Medicaid ends on March 31, enroll in a marketplace plan by March 31 to start coverage April 1. There should be zero gap.</li>
    <li><strong>Avoid non-urgent care during any gap.</strong> If there is a gap, postpone non-emergency care until your new coverage starts. For urgent needs, go to a community health center (sliding fee scale) rather than the ER.</li>
    <li><strong>Use the Good Faith Estimate.</strong> If you need scheduled care while uninsured, request a written good faith estimate. If the final bill exceeds the estimate by $400+, you can dispute it.</li>
    <li><strong>Ask about self-pay discounts.</strong> Most providers offer 20&ndash;50% discounts for uninsured/self-pay patients. Always ask before receiving services.</li>
    <li><strong>Scan every bill.</strong> Whether insured or not, <a href="/scan">upload your medical bills to BillKarma</a> to check for errors. Billing errors are more costly when you&rsquo;re paying out of pocket.</li>
    <li><strong>Apply for retroactive Medicaid.</strong> In most states, Medicaid can be retroactive up to 3 months before the application date. If you received care while your application was pending or during a gap, retroactive coverage may cover those bills.</li>
</ol>

<div class="case-study">
    <h3>Case study: Smooth Medicaid-to-marketplace transition saves family $6,000</h3>
    <p><strong>Situation:</strong> The Garcia family (income $42,000, 195% FPL for a family of three) lost Medicaid expansion coverage during redetermination. Their two children qualified for CHIP, but the parents needed marketplace coverage.</p>
    <p><strong>What they did:</strong> They enrolled in a Silver plan within the 60-day SEP. At 195% FPL, they qualified for significant cost-sharing reductions: $0 deductible, $10 copays, and a $1,150 out-of-pocket maximum. Their subsidized premium: $78/month for the couple.</p>
    <p><strong>The math:</strong> Without knowing about CSRs, they had initially planned to buy a Bronze plan at $45/month with a $7,000 deductible. When one parent needed minor surgery two months later, the Silver CSR plan paid everything beyond the $10 copay. On the Bronze plan, they would have owed the full $7,000 deductible. <strong>Savings from choosing Silver with CSRs: approximately $6,000.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How long do I have to enroll in marketplace coverage after losing Medicaid?</h3>
        <p>You have a 60-day Special Enrollment Period starting from the date your Medicaid coverage ends. Go to HealthCare.gov, select "loss of coverage" as your qualifying event, and complete your application. Coverage can start as soon as the 1st of the following month. Do not miss this window &mdash; otherwise you must wait until open enrollment (November 1 &mdash; January 15).</p>
    </div>
    <div class="faq-item">
        <h3>Will I qualify for subsidies?</h3>
        <p>If your income is 100&ndash;400% FPL ($15,060&ndash;$60,240 individual), yes. At lower incomes, your premium could be as low as $0&ndash;$31/month. At 100&ndash;250% FPL, Silver plans come with cost-sharing reductions that dramatically lower deductibles and copays. Use the HealthCare.gov calculator to see your specific subsidy amount.</p>
    </div>
    <div class="faq-item">
        <h3>Can I appeal my Medicaid termination?</h3>
        <p>Yes. File within 10 days of the termination notice to maintain coverage during the appeal. Common grounds: paperwork wasn&rsquo;t received, income hasn&rsquo;t changed, you qualify for a work requirement exemption. Contact your state Medicaid agency to request a fair hearing.</p>
    </div>
    <div class="faq-item">
        <h3>What happens to my children&rsquo;s coverage?</h3>
        <p>Children&rsquo;s Medicaid and CHIP are separate from adult coverage. CHIP covers children in families earning up to 200&ndash;400% FPL with minimal or zero premiums. Work requirements do not apply to children. Apply at InsureKidsNow.gov or through your state Medicaid office.</p>
    </div>
    <div class="faq-item">
        <h3>Should I choose a Bronze or Silver plan?</h3>
        <p>If your income is 100&ndash;250% FPL, always choose Silver. Cost-sharing reductions make Silver plans dramatically cheaper in total cost, with deductibles as low as $0 and copays as low as $10. CSRs are only available on Silver plans. If your income is above 250% FPL, compare total expected costs across Bronze and Silver based on how much care you anticipate using.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.healthcare.gov/" target="_blank" rel="noopener">HealthCare.gov: Marketplace Coverage and Special Enrollment Periods</a></li>
    <li><a href="https://www.kff.org/medicaid/issue-brief/medicaid-enrollment-and-unwinding-tracker/" target="_blank" rel="noopener">KFF: Medicaid Enrollment and Unwinding Tracker</a></li>
    <li><a href="https://www.cms.gov/medicaid/eligibility/medicaid-and-chip-enrollment-data" target="_blank" rel="noopener">CMS: Medicaid and CHIP Enrollment Data</a></li>
    <li><a href="https://www.insurekidsnow.gov/" target="_blank" rel="noopener">InsureKidsNow.gov: Children&rsquo;s Health Insurance Program</a></li>
    <li><a href="https://findahealthcenter.hrsa.gov/" target="_blank" rel="noopener">HRSA: Find a Health Center</a></li>
    <li><a href="https://www.americanprogress.org/article/the-implementation-timeline-of-the-one-big-beautiful-bill-act/" target="_blank" rel="noopener">Center for American Progress: OBBBA Implementation Timeline</a></li>
    <li><a href="https://www.propel.app/blog/medicaid-cuts-explained-big-beautiful-bill-updates/" target="_blank" rel="noopener">Propel: Medicaid Cuts Explained</a></li>
</ul>
""",
})
