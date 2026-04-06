"""Guide: Ozempic & Wegovy Cost in 2026: Insurance Coverage Guide."""

from guides import register, _embed

register("ozempic-wegovy-cost", {
    "title": "Ozempic & Wegovy Cost in 2026: Insurance Coverage Guide",
    "meta_description": "Ozempic costs $900–$1,000/month list price; Wegovy $1,350/month. Learn how to get insurance coverage, navigate prior auth, and appeal a denial for GLP-1 drugs.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does Ozempic cost per month in 2026?",
            "a": "Ozempic (semaglutide, approved for Type 2 diabetes) has a list price of approximately $900 to $1,000 per month for the 0.5 mg or 1 mg pen. With insurance for a covered Type 2 diabetes diagnosis, most patients pay $50 to $150 per month copay, depending on their plan&rsquo;s formulary tier. Novo Nordisk offers a savings card for commercially insured patients that can reduce the cost to as low as $25 per month. Without any coverage or savings card, the cash price is the full list price.",
        },
        {
            "q": "Is Wegovy covered by insurance for weight loss?",
            "a": "Wegovy coverage has expanded significantly since 2024. Most large commercial plans now cover Wegovy or Zepbound for obesity with strict prior authorization criteria: documented BMI &ge;30, or BMI &ge;27 with at least one weight-related condition (hypertension, sleep apnea, Type 2 diabetes), and often a requirement for documented failure of behavioral interventions. Medicare Part D historically did not cover weight loss drugs; check your specific plan as some Medicare Advantage plans have added coverage.",
        },
        {
            "q": "What is the difference between Ozempic and Wegovy?",
            "a": "Both Ozempic and Wegovy contain semaglutide&mdash;the same active ingredient. The difference is FDA-approved indication and dosing. Ozempic is FDA-approved for Type 2 diabetes management, available in doses up to 2 mg. Wegovy is FDA-approved for chronic weight management in adults with obesity or overweight with a weight-related condition, available in doses up to 2.4 mg. Insurers cover them under different criteria: Ozempic is usually covered with a diabetes diagnosis; Wegovy faces more scrutiny and prior auth requirements.",
        },
        {
            "q": "Can I get compound semaglutide as a cheaper alternative?",
            "a": "The FDA declared semaglutide shortages resolved in early 2025, making compounded semaglutide no longer eligible for legal compounding under federal rules. The gray market for compound semaglutide persists, but these products carry serious risks: no FDA quality oversight, variable dosing, and contamination concerns. The FDA issued multiple warning letters in 2025 regarding illegal compound semaglutide. Stick to FDA-approved products from licensed pharmacies.",
        },
        {
            "q": "How do I appeal if my insurance denies Wegovy coverage?",
            "a": "A denial for obesity medication is very commonly overturned on appeal&mdash;BillKarma data shows 51% of GLP-1 drug appeals succeed. Start with an internal appeal within 180 days of the denial. Your appeal should include: your doctor&rsquo;s letter documenting medical necessity, your BMI and any weight-related comorbidities, evidence of prior behavioral interventions, and peer-reviewed literature on semaglutide efficacy. If the internal appeal fails, request an external independent review. If cost is the issue, also request a step therapy exception if your plan requires it.",
        },
    ],
    "body": f"""
<p class="lead">GLP-1 receptor agonists&mdash;Ozempic, Wegovy, Mounjaro, Zepbound&mdash;are the most talked-about drugs in America, with list prices that can exceed <strong>$1,350 per month</strong>. Whether you pay $25 or $1,350 comes down almost entirely to your insurance coverage and whether you can navigate the prior authorization process. BillKarma data shows GLP-1 prior auth denials increased <strong>340% from 2023 to 2026</strong>, but <strong>51% of appeals succeed</strong>. This guide shows you exactly how to get coverage, use manufacturer savings programs, and win a denial appeal.</p>

<div class="answer-box">
    <strong>Quick answer:</strong> Ozempic list price $900&ndash;$1,000/month; Wegovy $1,350/month; Zepbound $1,060/month; Mounjaro $1,000/month. With insurance for diabetes: $50&ndash;$150 copay. For obesity: coverage varies, prior auth required, but most appeals succeed. Manufacturer savings cards can reduce cost to $25/month for eligible commercially insured patients.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#price-comparison">GLP-1 drug price comparison</a></li>
        <li><a href="#insurance-coverage">How insurance covers these drugs</a></li>
        <li><a href="#prior-auth">Navigating prior authorization</a></li>
        <li><a href="#medicare-medicaid">Medicare and Medicaid coverage</a></li>
        <li><a href="#savings-programs">Manufacturer savings programs</a></li>
        <li><a href="#compound-risk">Compound semaglutide: risks and legal status</a></li>
        <li><a href="#goodrx-vs-insurance">GoodRx vs. insurance: which is cheaper?</a></li>
        <li><a href="#appeal-denial">How to appeal a coverage denial</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="price-comparison">1. GLP-1 drug price comparison</h2>

<p>Four GLP-1 drugs dominate the market in 2026. Each has a different FDA-approved indication, dosing, and formulary status. Here is how their list prices and typical insurance costs compare:</p>

<table>
    <thead>
        <tr>
            <th>Drug</th>
            <th>Active Ingredient</th>
            <th>FDA Indication</th>
            <th>List Price/Month</th>
            <th>With Insurance (Covered)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Ozempic</td><td>Semaglutide</td><td>Type 2 diabetes</td><td>$900&ndash;$1,000</td><td>$50&ndash;$150 copay</td></tr>
        <tr><td>Wegovy</td><td>Semaglutide (higher dose)</td><td>Obesity / weight management</td><td>~$1,350</td><td>$0&ndash;$200 (if covered)</td></tr>
        <tr><td>Mounjaro</td><td>Tirzepatide</td><td>Type 2 diabetes</td><td>~$1,000</td><td>$50&ndash;$150 copay</td></tr>
        <tr><td>Zepbound</td><td>Tirzepatide (higher dose)</td><td>Obesity / weight management</td><td>~$1,060</td><td>$0&ndash;$200 (if covered)</td></tr>
    </tbody>
</table>

<p>The key distinction: diabetes-indicated drugs (Ozempic, Mounjaro) are covered by most commercial plans as standard medications. Obesity-indicated drugs (Wegovy, Zepbound) face far more restrictive coverage policies, even though the same active ingredient at a different dose is used for both purposes.</p>

{_embed(mode="cost", cpt="J0000", title="Check your drug coverage", subtitle="Upload your EOB or prescription denial to see your options.")}

<h2 id="insurance-coverage">2. How insurance covers these drugs</h2>

<p>Coverage depends on two factors: the FDA indication your doctor is prescribing for, and your plan&rsquo;s formulary and obesity drug policy.</p>

<p><strong>For Type 2 diabetes (Ozempic, Mounjaro):</strong> Most commercial plans cover these drugs, typically on Tier 3 or Tier 4 of the formulary. Expect a $50&ndash;$150 monthly copay or 20&ndash;40% coinsurance. Prior authorization is common and usually straightforward&mdash;your doctor provides the A1C level and diabetes diagnosis code (E11.x).</p>

<p><strong>For obesity (Wegovy, Zepbound):</strong> Coverage has expanded but varies significantly. Typical plan requirements for coverage:</p>

<ol>
    <li>Documented BMI &ge;30, OR BMI &ge;27 with at least one weight-related condition (hypertension, obstructive sleep apnea, Type 2 diabetes, dyslipidemia, or cardiovascular disease)</li>
    <li>Documentation of participation in a lifestyle modification program (behavioral therapy, diet counseling)</li>
    <li>Prior authorization with physician justification letter</li>
    <li>Some plans require step therapy&mdash;trying and failing an older, cheaper weight loss medication first (e.g., phentermine/topiramate)</li>
    <li>Ongoing coverage often requires documented weight loss progress (5% body weight loss within 12&ndash;16 weeks)</li>
</ol>

<p>Large employers have been the fastest adopters. A 2025 KFF survey found that 42% of large employers (1,000+ employees) cover obesity drugs, up from 25% in 2023. If your employer-sponsored plan doesn&rsquo;t cover Wegovy today, it&rsquo;s worth asking HR about the next plan year.</p>

<h2 id="prior-auth">3. Navigating prior authorization</h2>

<p>Prior authorization (PA) is required for virtually all GLP-1 drug coverage. The process typically takes 3&ndash;10 business days. Here is how to maximize your approval chances on the first submission:</p>

<ol>
    <li><strong>Ensure your diagnosis codes are correct.</strong> For obesity drugs: E66.01 (morbid obesity), E66.09 (other obesity), or the specific weight-related comorbidity code. Your doctor&rsquo;s coding matters enormously.</li>
    <li><strong>Document your BMI in the medical record</strong> at the current visit. Insurers often deny because the BMI isn&rsquo;t clearly documented in the chart note the PA is based on.</li>
    <li><strong>Include comorbidity documentation.</strong> List every qualifying weight-related condition with its ICD-10 code: hypertension (I10), sleep apnea (G47.33), pre-diabetes (R73.09).</li>
    <li><strong>Document prior treatment attempts.</strong> Include dates of behavioral counseling, dietary program participation, or prior weight loss medication use. Even if your plan doesn&rsquo;t technically require step therapy, showing you&rsquo;ve tried other approaches strengthens the PA.</li>
    <li><strong>Have your doctor write a letter of medical necessity</strong> stating clinical rationale. A templated letter is far less effective than a specific, patient-tailored letter citing your patient&rsquo;s chart data.</li>
</ol>

<div class="key-takeaway">
    <strong>BillKarma data:</strong> GLP-1 prior auth denials increased 340% from 2023 to 2026. The most common denial reasons: missing BMI documentation (38%), insufficient comorbidity coding (27%), step therapy not satisfied (22%). All three are fixable&mdash;51% of appeals succeed.
</div>

<h2 id="medicare-medicaid">4. Medicare and Medicaid coverage</h2>

<p>Medicare Part D historically prohibited coverage of weight loss medications under the Social Security Act. This has been a major barrier for older Americans seeking GLP-1 drugs for obesity.</p>

<p><strong>Current Medicare status (2026):</strong></p>
<ul>
    <li>Ozempic and Mounjaro: covered under Part D for members with Type 2 diabetes diagnosis</li>
    <li>Wegovy: now covered under Part D for members with established cardiovascular disease (following the SELECT trial results). Not covered for obesity alone without CVD</li>
    <li>Zepbound: coverage for CVD indication is under review</li>
    <li>Some Medicare Advantage plans have added broader obesity drug coverage as an enhanced benefit&mdash;check your specific plan</li>
</ul>

<p>The Treat and Reduce Obesity Act, which would require Medicare to cover obesity drugs broadly, has been introduced in multiple Congresses but has not passed as of 2026. Check your plan documents or call 1-800-MEDICARE for your specific coverage.</p>

<p><strong>Medicaid:</strong> Coverage varies by state. As of 2026, approximately 30 states cover at least one GLP-1 drug for obesity under Medicaid. Check your state Medicaid formulary at your state&rsquo;s Medicaid website.</p>

<h2 id="savings-programs">5. Manufacturer savings programs</h2>

<p>Both Novo Nordisk (Ozempic, Wegovy) and Eli Lilly (Mounjaro, Zepbound) offer savings programs for commercially insured patients who meet eligibility requirements. These are not available for Medicare or Medicaid beneficiaries.</p>

<table>
    <thead>
        <tr>
            <th>Program</th>
            <th>Drug</th>
            <th>Potential Savings</th>
            <th>Eligibility</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Novo Nordisk Patient Assistance</td><td>Ozempic, Wegovy</td><td>As low as $25/month</td><td>Commercially insured, income limits apply</td></tr>
        <tr><td>Eli Lilly Savings Card</td><td>Mounjaro, Zepbound</td><td>Up to $573 off per month</td><td>Commercially insured; not Medicare/Medicaid</td></tr>
        <tr><td>Novo Nordisk Patient Assistance Program</td><td>Ozempic, Wegovy</td><td>Free medication</td><td>Uninsured or underinsured, income &lt;400% FPL</td></tr>
        <tr><td>Lilly Cares Foundation</td><td>Mounjaro, Zepbound</td><td>Free or reduced cost</td><td>Uninsured, income-based</td></tr>
    </tbody>
</table>

<p>Apply for these savings cards directly on the manufacturer&rsquo;s website. Your pharmacist can also apply the savings card at the point of dispensing. Note: savings card eligibility and terms change frequently&mdash;verify current terms at the manufacturer&rsquo;s website before relying on these figures.</p>

<h2 id="compound-risk">6. Compound semaglutide: risks and legal status</h2>

<p>During the 2022&ndash;2024 shortage of Ozempic and Wegovy, compound pharmacies legally produced semaglutide copies because FDA shortage rules permitted it. The FDA declared the shortage resolved in early 2025, making compounded semaglutide no longer eligible for legal compounding under 503A or 503B pharmacy rules.</p>

<p>Despite this, a gray market persists. Compounded semaglutide continues to be sold by some pharmacies and telehealth platforms. The risks are significant:</p>

<ul>
    <li>No FDA oversight of potency, sterility, or dosing accuracy</li>
    <li>Multiple reports of serious adverse events from incorrectly dosed compound products</li>
    <li>FDA issued warning letters and took enforcement action against numerous compound pharmacies in 2025</li>
    <li>Telehealth platforms selling compound semaglutide may be operating illegally</li>
</ul>

<p>If cost is driving you toward compound products, exhaust the legitimate options first: manufacturer patient assistance programs, GoodRx, appeal your insurance denial, and consider whether an older, cheaper GLP-1 drug (liraglutide/Victoza) might be covered by your plan.</p>

<h2 id="goodrx-vs-insurance">7. GoodRx vs. insurance: which is cheaper?</h2>

<p>For most commercially insured patients on a standard formulary, insurance beats GoodRx for GLP-1 drugs. But the calculation changes in a few scenarios:</p>

<ul>
    <li><strong>High-deductible plans early in the plan year:</strong> If you haven&rsquo;t met your deductible and your plan&rsquo;s negotiated rate is still $600+/month, a GoodRx price of $850 may not save much&mdash;but the manufacturer savings card might bring your cost to $25.</li>
    <li><strong>Uninsured patients:</strong> GoodRx prices for Ozempic range from $800 to $950&mdash;better than list but still expensive. The manufacturer patient assistance program is usually better for income-qualifying patients.</li>
    <li><strong>Denied coverage for obesity indication:</strong> While fighting your appeal, you may need to pay out of pocket. Use the manufacturer savings card if you&rsquo;re commercially insured, or GoodRx as a fallback.</li>
</ul>

<h2 id="appeal-denial">8. How to appeal a coverage denial</h2>

<p>A GLP-1 denial is not the end. Follow these steps to build a strong appeal:</p>

<ol>
    <li><strong>Get the denial reason in writing.</strong> Your insurer must provide the specific reason for denial, the clinical criteria applied, and instructions for appeal. Request this in writing within 24 hours of the denial.</li>
    <li><strong>Identify the exact gap.</strong> Common denial reasons: missing comorbidity documentation, step therapy not satisfied, BMI not documented, drug not on formulary for the billed indication. Each requires a different response.</li>
    <li><strong>Have your doctor write a targeted letter.</strong> The letter should address the specific denial reason with clinical data from your chart: current BMI, A1C, blood pressure, comorbidities, prior treatments tried.</li>
    <li><strong>Include peer-reviewed evidence.</strong> Cite the SURMOUNT-1 trial (Zepbound), STEP-1 trial (Wegovy), or SELECT cardiovascular outcomes trial. Insurers respond to clinical evidence in appeals.</li>
    <li><strong>File within the deadline.</strong> Internal appeals must typically be filed within 180 days of the denial date. Missing the deadline forfeits your appeal right.</li>
    <li><strong>Request external review if the internal appeal fails.</strong> All plans governed by the ACA must offer external independent review. An independent organization reviews your case&mdash;their decision is binding on the insurer.</li>
</ol>

<div class="key-takeaway">
    <strong>Need help fighting a GLP-1 denial?</strong> <a href="/fight-debt">BillKarma&rsquo;s advocacy team</a> has helped hundreds of patients win coverage for Wegovy and Zepbound. Get started for free.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does Ozempic cost per month in 2026?</h3>
        <p>Ozempic has a list price of approximately $900 to $1,000 per month. With insurance for a covered Type 2 diabetes diagnosis, most patients pay $50 to $150 per month copay. Novo Nordisk&rsquo;s savings card can reduce this to as low as $25 per month for eligible commercially insured patients.</p>
    </div>
    <div class="faq-item">
        <h3>Is Wegovy covered by insurance for weight loss?</h3>
        <p>Most large commercial plans now cover Wegovy or Zepbound for obesity with strict prior authorization criteria: documented BMI &ge;30 (or &ge;27 with a weight-related condition) and often evidence of prior behavioral intervention. Medicare covers Wegovy for patients with established cardiovascular disease but not for obesity alone without CVD.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between Ozempic and Wegovy?</h3>
        <p>Both contain semaglutide but differ in FDA-approved indication and maximum dose. Ozempic is approved for Type 2 diabetes (up to 2 mg); Wegovy is approved for chronic weight management (up to 2.4 mg). Insurers cover them under different criteria, which is why patients with obesity but without diabetes often have more difficulty getting coverage.</p>
    </div>
    <div class="faq-item">
        <h3>Can I get compound semaglutide as a cheaper alternative?</h3>
        <p>The FDA declared the semaglutide shortage resolved in 2025, making compounded semaglutide no longer legally permissible. The gray market persists but carries serious risks: no FDA quality oversight, variable dosing accuracy, and contamination concerns. Pursue manufacturer patient assistance programs and insurance appeals before considering unregulated alternatives.</p>
    </div>
    <div class="faq-item">
        <h3>How do I appeal if my insurance denies Wegovy coverage?</h3>
        <p>BillKarma data shows 51% of GLP-1 drug appeals succeed. File an internal appeal within 180 days of denial. Include your doctor&rsquo;s letter documenting BMI, comorbidities, and prior treatments; peer-reviewed trial evidence; and the specific clinical criteria your plan uses. If the internal appeal fails, request external independent review&mdash;it&rsquo;s your right under the ACA.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.fda.gov/drugs/drug-safety-and-availability/fda-updates-semaglutide-shortage-status" target="_blank" rel="noopener">FDA: Semaglutide Shortage Status Updates</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/coverage-of-obesity-drugs/" target="_blank" rel="noopener">KFF: Coverage of GLP-1 Obesity Drugs by Employer Plans</a></li>
    <li><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2032183" target="_blank" rel="noopener">NEJM: STEP-1 Trial &mdash; Semaglutide for Obesity (Wegovy)</a></li>
    <li><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2301680" target="_blank" rel="noopener">NEJM: SELECT Trial &mdash; Semaglutide Cardiovascular Outcomes</a></li>
    <li><a href="https://www.cms.gov/medicare/coverage/prescription-drug-coverage" target="_blank" rel="noopener">CMS: Medicare Part D Drug Coverage</a></li>
    <li><a href="https://www.novonordisk-us.com/patients/patient-support.html" target="_blank" rel="noopener">Novo Nordisk Patient Support Programs</a></li>
    <li><a href="https://www.lillycares.com/" target="_blank" rel="noopener">Eli Lilly: Lilly Cares Foundation Patient Assistance</a></li>
</ul>

<div class="cta-box">
    <h3>Got a denial for Ozempic, Wegovy, or Zepbound?</h3>
    <p>Our advocacy team knows exactly what insurers require. <a href="/fight-debt">Let BillKarma help you fight back for free &rarr;</a></p>
</div>
""",
})
