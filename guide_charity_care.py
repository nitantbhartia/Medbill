"""Guide: Hospital Financial Assistance and Charity Care."""

from guides import register, _embed

register("hospital-financial-assistance-charity-care", {
    "title": "Hospital Charity Care: Do You Qualify for Free or Reduced Bills?",
    "meta_description": "Most nonprofit hospitals must offer free or reduced-cost care by law. Check income limits, get the application steps, and see what your hospital offers.",
    "published": "2026-02-20",
    "author": "BillKarma Team",
    "category": "Taking Action",
    "faqs": [
        {
            "q": "Can I apply for financial assistance after I already received my hospital bill?",
            "a": "Yes. Most hospitals accept financial assistance applications for up to 240 days after the first post-discharge billing statement. Some hospitals extend this window even further. You can apply even if you have already made partial payments or set up a payment plan. The key is to apply before the bill goes to collections.",
        },
        {
            "q": "Does charity care or financial assistance affect my credit score?",
            "a": "No. Receiving financial assistance from a hospital does not appear on your credit report and has no effect on your credit score. It is not a loan or a line of credit. It is a discount or write-off applied directly to your hospital account. As of 2023, the three major credit bureaus no longer include medical debt under $500 on credit reports, and paid medical collections are removed entirely.",
        },
        {
            "q": "Can I get financial assistance if I have health insurance?",
            "a": "Yes. Many hospital financial assistance policies cover the patient responsibility portion of a bill, including deductibles, coinsurance, and copays. If your insurance left you with a large out-of-pocket balance and your income qualifies, you can apply for financial assistance on the amount you owe after insurance has paid its share.",
        },
        {
            "q": "What if my hospital is for-profit? Can I still get help?",
            "a": "For-profit hospitals are not legally required to offer financial assistance under IRS Section 501(r), but many still have hardship programs or discount policies. Call the billing department and ask about self-pay discounts, hardship programs, or payment plans. You can also negotiate directly using Medicare rates as a benchmark.",
        },
        {
            "q": "How long does the financial assistance application process take?",
            "a": "Most hospitals process financial assistance applications within 30 to 45 days. Some hospitals provide a preliminary decision within two weeks. During the review period, your account should be placed on hold so it does not go to collections. If you have not heard back within 30 days, call the patient financial services department for a status update.",
        },
        {
            "q": "What happens if my financial assistance application is denied?",
            "a": "You have the right to appeal. Ask for the denial reason in writing, then submit additional documentation that addresses the reason. Common reasons for denial include incomplete applications or missing documents. If the appeal is also denied, you can escalate to the hospital patient advocate, contact your state attorney general consumer protection division, or apply for a payment plan at the reduced rate the hospital offers.",
        },
    ],
    "body": f"""
<p class="lead">Nonprofit hospitals in the United States provided <strong>$28 billion</strong> in charity care in 2022, but billions more go unclaimed every year because patients don&rsquo;t know they can apply. If you earn under $62,400 as an individual or $128,800 as a family of four, you may qualify for free or deeply discounted hospital care&mdash;even after you&rsquo;ve already received the bill. Financial assistance is a legal right at most hospitals, not a handout. Here&rsquo;s how to claim it.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-financial-assistance">What is hospital financial assistance (charity care)?</a></li>
        <li><a href="#who-qualifies">Who qualifies?</a></li>
        <li><a href="#find-your-hospital">How to find out if your hospital offers financial assistance</a></li>
        <li><a href="#how-to-apply">How to apply &mdash; step by step</a></li>
        <li><a href="#annotated-example">Annotated example: what a successful application looks like</a></li>
        <li><a href="#what-hospitals-dont-tell-you">What hospitals don&rsquo;t want you to know</a></li>
        <li><a href="#case-studies">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-financial-assistance">1. What is hospital financial assistance (charity care)?</h2>

<p>Hospital financial assistance&mdash;also called <strong>charity care</strong> or <strong>indigent care</strong>&mdash;is a program that reduces or eliminates hospital bills for patients who cannot afford to pay. These are all names for the same thing: a discount or write-off applied to your hospital bill based on your income.</p>

<p>Under <strong>IRS Section 501(r)</strong>, every nonprofit hospital in the United States is legally required to have a written <strong>Financial Assistance Policy (FAP)</strong>. About 60% of all US hospitals are nonprofit, which means the majority of hospitals must offer this program. It is not optional&mdash;it is a condition of their tax-exempt status.</p>

<p>Here&rsquo;s what financial assistance typically covers:</p>

<ul>
    <li><strong>Inpatient stays</strong> &mdash; surgeries, overnight hospitalizations, ICU care</li>
    <li><strong>Outpatient procedures</strong> &mdash; same-day surgeries, diagnostic tests, infusions</li>
    <li><strong>Emergency room visits</strong> &mdash; regardless of whether you were admitted</li>
    <li><strong>Physician fees</strong> &mdash; some hospitals extend assistance to doctor charges billed through the hospital (though not always)</li>
</ul>

<div class="key-takeaway">
    <strong>This is a right, not a favor.</strong> Nonprofit hospitals receive billions of dollars in tax exemptions every year. In exchange, they are required to provide financial assistance to patients who qualify. If a hospital fails to maintain a compliant financial assistance program, it can lose its tax-exempt status entirely. You are not asking for charity&mdash;you are claiming a benefit that the hospital is legally obligated to provide.
</div>

<p>Financial assistance can be applied <strong>retroactively</strong>. That means you can apply even if you&rsquo;ve already received the bill, already made partial payments, or already been contacted by the hospital&rsquo;s billing department. Most hospitals accept applications for up to 240 days after the first billing statement.</p>

<h2 id="who-qualifies">2. Who qualifies?</h2>

<p>Eligibility is based primarily on your household income relative to the <strong>Federal Poverty Level (FPL)</strong>. The FPL is a number set by the government each year that defines the income threshold for various assistance programs. Each hospital sets its own cutoffs, but most follow a similar pattern:</p>

<table>
    <thead>
        <tr><th>Income Level (% of FPL)</th><th>Individual Income (2026)</th><th>Family of 4 Income (2026)</th><th>Typical Assistance</th></tr>
    </thead>
    <tbody>
        <tr><td>Below 200% FPL</td><td>Under $31,200</td><td>Under $64,400</td><td>100% free care &mdash; entire bill written off</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$31,200&ndash;$46,800</td><td>$64,400&ndash;$96,600</td><td>50&ndash;80% discount</td></tr>
        <tr><td>300&ndash;400% FPL</td><td>$46,800&ndash;$62,400</td><td>$96,600&ndash;$128,800</td><td>25&ndash;50% discount</td></tr>
    </tbody>
</table>

<p><strong>Important:</strong> These are typical thresholds. Some hospitals are more generous. Major health systems like Kaiser Permanente, Providence, and CommonSpirit offer assistance up to 400% FPL or higher. A few hospitals extend partial discounts up to 500% FPL. Always check your specific hospital&rsquo;s policy.</p>

<div class="key-takeaway">
    <strong>Not sure what your hospital offers?</strong> Browse our <a href="/hospitals/">hospital directory</a> &mdash; every listing shows the hospital&rsquo;s nonprofit status, income thresholds, and financial assistance policy details so you know exactly what you&rsquo;re eligible for before you apply.
</div>

<p>Beyond income, hospitals may also consider:</p>

<ul>
    <li><strong>Asset tests</strong> &mdash; Some hospitals look at savings and assets, but many do not. If your hospital does count assets, primary residences and retirement accounts are usually excluded.</li>
    <li><strong>Special circumstances</strong> &mdash; Recent job loss, divorce, a new major illness, existing medical debt, or other financial hardships can strengthen your application even if your income is slightly above the threshold.</li>
    <li><strong>Medical debt burden</strong> &mdash; If your existing medical bills exceed a certain percentage of your income (often 10&ndash;25%), some hospitals will qualify you even at higher income levels.</li>
    <li><strong>Insurance status</strong> &mdash; Being uninsured is not required. Insured patients can apply for assistance on their out-of-pocket costs (deductibles, coinsurance, copays).</li>
</ul>

<p>Use our calculator to see how your charges compare to what Medicare pays&mdash;this helps you understand what a &ldquo;fair&rdquo; price looks like before you apply:</p>

{_embed(mode="markup", title="Compare your bill to Medicare rates", subtitle="Enter a CPT code and amount from your bill to see the benchmark.", height="420")}

<h2 id="find-your-hospital">3. How to find out if your hospital offers financial assistance</h2>

<p>Start by checking whether your hospital is nonprofit. About 60% of US hospitals are&mdash;including most of the largest health systems in the country. You can look up your hospital in our <a href="/hospitals/">hospital directory</a> to see its nonprofit status and pricing data.</p>

<p>Every nonprofit hospital is required to:</p>

<ul>
    <li>Post its Financial Assistance Policy (FAP) on its website</li>
    <li>Provide a plain-language summary of the policy</li>
    <li>Make paper copies available upon request</li>
    <li>Inform patients about the policy before collection actions</li>
</ul>

<p>Here&rsquo;s what to look for in the policy:</p>

<table>
    <thead>
        <tr><th>Policy Element</th><th>What It Should Tell You</th><th>Red Flag If Missing</th></tr>
    </thead>
    <tbody>
        <tr><td>Eligibility criteria</td><td>Income thresholds (as % of FPL), family size adjustments, asset limits if any</td><td>Yes &mdash; required by IRS</td></tr>
        <tr><td>Covered services</td><td>Which services qualify (inpatient, outpatient, ER, physician fees)</td><td>Yes &mdash; required by IRS</td></tr>
        <tr><td>Application process</td><td>How to apply, what documents are needed, where to submit</td><td>Yes &mdash; required by IRS</td></tr>
        <tr><td>Billing limits</td><td>Whether qualifying patients are charged no more than Medicare or similar rates</td><td>May indicate ACA provision applies</td></tr>
        <tr><td>Collection protections</td><td>What actions the hospital will and will not take against qualifying patients</td><td>Yes &mdash; required by IRS</td></tr>
    </tbody>
</table>

<p><strong>How to find the policy:</strong></p>

<ol>
    <li><strong>Hospital website:</strong> Search for &ldquo;financial assistance,&rdquo; &ldquo;charity care,&rdquo; or &ldquo;patient financial services.&rdquo; The policy is often under the &ldquo;Billing&rdquo; or &ldquo;Patients &amp; Visitors&rdquo; section.</li>
    <li><strong>Call the billing department:</strong> Ask for the financial assistance application directly. They are required to provide it.</li>
    <li><strong>BillKarma hospital directory:</strong> <a href="/hospitals/">Search our directory</a> to find your hospital&rsquo;s nonprofit status and links to their financial assistance information.</li>
</ol>

<h2 id="how-to-apply">4. How to apply &mdash; step by step</h2>

<h3>Step 1: Find the financial assistance application</h3>

<p>Check the hospital&rsquo;s website under &ldquo;billing&rdquo; or &ldquo;patient financial services.&rdquo; You can also call the billing department at the number on your statement and say: &ldquo;I&rsquo;d like to apply for financial assistance. Can you send me the application?&rdquo; They are required to provide it. Many hospitals also have patient financial counselors who can walk you through the process in person.</p>

<h3>Step 2: Gather your documentation</h3>

<p>Most applications require:</p>

<ul>
    <li><strong>Proof of income</strong> &mdash; Two to three recent pay stubs, or your most recent tax return (Form 1040). If you are unemployed, a letter from your last employer or unemployment benefits statement.</li>
    <li><strong>Tax return</strong> &mdash; Most recent federal tax return (Form 1040). Some hospitals accept just pages 1 and 2.</li>
    <li><strong>Bank statements</strong> &mdash; One to three months of statements for checking and savings accounts. Not all hospitals require this.</li>
    <li><strong>Proof of hardship</strong> (if applicable) &mdash; Layoff notice, divorce decree, other medical bills, disability determination letter, or any documentation of a financial change.</li>
    <li><strong>Household information</strong> &mdash; Number of people in your household, as the FPL thresholds change with family size.</li>
</ul>

<h3>Step 3: Complete the application</h3>

<p>Fill out every field. Incomplete applications are the most common reason for delays and denials. If a question doesn&rsquo;t apply, write &ldquo;N/A&rdquo; rather than leaving it blank. Include a brief cover letter explaining your situation in one or two sentences: &ldquo;I am requesting financial assistance for my hospital stay on [date]. My annual household income is $[amount] for a family of [number].&rdquo;</p>

<h3>Step 4: Submit and follow up</h3>

<p>Submit the application by the method the hospital specifies&mdash;usually mail, fax, email, or in person at the patient financial services office. Keep copies of everything you submit. Call to confirm receipt within 5 business days. Ask for a reference number and the name of the person handling your case. Ask the hospital to place your account on hold during the review so it does not go to collections.</p>

<h3>Step 5: Appeal if denied</h3>

<p>If your application is denied:</p>

<ol>
    <li><strong>Request the denial reason in writing.</strong> Common reasons include: incomplete application, income above their threshold, or missing documents.</li>
    <li><strong>Fix the issue and resubmit.</strong> If documents were missing, add them. If income is borderline, include documentation of special circumstances (other medical debt, recent job loss, ongoing treatment costs).</li>
    <li><strong>Escalate if needed.</strong> Contact the hospital&rsquo;s patient advocate. If that fails, file a complaint with your <strong>state attorney general&rsquo;s</strong> consumer protection division&mdash;they investigate hospitals that fail to comply with financial assistance obligations.</li>
</ol>

<div class="key-takeaway">
    <strong>Ready to take the first step on your bill?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we flag overcharges, identify CPT codes billed above Medicare rates, and give you a prioritized list of issues to raise when you submit your financial assistance application.
</div>

<h2 id="annotated-example">5. Annotated example: what a successful application looks like</h2>

<p>Here&rsquo;s a real-world example of how financial assistance works from start to finish. A patient had an emergency appendectomy (surgical removal of the appendix) and received this bill:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Community Medical Center &mdash; Date of Service: 12/08/2025</div>
    <div class="line-item">
        <span>44960 &mdash; Appendectomy</span>
        <span>$18,400.00</span>
    </div>
    <div class="line-item">
        <span>99223 &mdash; Initial Hospital Care, High Complexity</span>
        <span>$2,800.00</span>
    </div>
    <div class="line-item">
        <span>99232 &mdash; Subsequent Hospital Care (x2 days)</span>
        <span>$1,600.00</span>
    </div>
    <div class="line-item">
        <span>74177 &mdash; CT Abdomen/Pelvis with Contrast</span>
        <span>$3,200.00</span>
    </div>
    <div class="line-item">
        <span>36556 &mdash; Central Venous Catheter</span>
        <span>$1,850.00</span>
    </div>
    <div class="line-item">
        <span>96374 &mdash; IV Push, Antibiotics (x4)</span>
        <span>$1,400.00</span>
    </div>
    <div class="line-item">
        <span>80053 &mdash; Comprehensive Metabolic Panel</span>
        <span>$490.00</span>
    </div>
    <div class="line-item">
        <span>85025 &mdash; Complete Blood Count</span>
        <span>$260.00</span>
    </div>
    <div class="line-item">
        <span>Revenue Code 0250 &mdash; Pharmacy/Anesthesia</span>
        <span>$2,000.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$32,000.00</span>
    </div>
</div>

<p><strong>Patient&rsquo;s situation:</strong></p>

<ul>
    <li>Single individual, no dependents</li>
    <li>Annual income: $38,000</li>
    <li>Income as percentage of FPL: 245% (between 200% and 300%)</li>
    <li>Uninsured</li>
</ul>

<p><strong>Hospital&rsquo;s financial assistance policy:</strong></p>

<ul>
    <li>Below 200% FPL: 100% free care</li>
    <li>200&ndash;300% FPL: 65% discount</li>
    <li>300&ndash;400% FPL: 40% discount</li>
</ul>

<p><strong>Result:</strong></p>

<ul>
    <li>Original bill: <strong>$32,000</strong></li>
    <li>Financial assistance discount (65%): <strong>&minus;$20,800</strong></li>
    <li>Adjusted bill: <strong>$11,200</strong></li>
    <li>Payment plan: $467/month for 24 months, zero interest</li>
</ul>

<p>The patient saved <strong>$20,800</strong> by filling out a single application. The entire process took 22 days from submission to approval.</p>

<p>Want to see how your bill compares to Medicare rates before you apply? <a href="/scan">Upload your bill to BillKarma</a> for an instant audit.</p>

<h2 id="what-hospitals-dont-tell-you">6. What hospitals don&rsquo;t want you to know</h2>

<p>Hospitals are required to have financial assistance programs, but they are not always proactive about telling patients. Here are the facts most billing departments won&rsquo;t volunteer:</p>

<h3>You can apply AFTER receiving the bill</h3>

<p>Many patients assume financial assistance is something you arrange before treatment. That&rsquo;s not true. Under IRS rules, hospitals must accept applications for at least 240 days after the first billing statement. Some hospitals accept them even later. If you received a bill weeks or months ago, you can still apply.</p>

<h3>You can apply even if you have insurance</h3>

<p>Financial assistance is not just for the uninsured. If your insurance left you with a large deductible, coinsurance, or copay, you can apply for assistance on the <strong>patient responsibility portion</strong>. This is especially valuable for patients with high-deductible health plans who face $3,000&ndash;$8,000 in out-of-pocket costs.</p>

<h3>Some hospitals must limit charges to Medicare rates</h3>

<p>Under the Affordable Care Act (ACA) and IRS Section 501(r), nonprofit hospitals cannot charge patients who qualify for financial assistance more than the <strong>amounts generally billed (AGB)</strong> to insured patients. In practice, this often means qualifying patients are charged at or near Medicare rates&mdash;which can be 50&ndash;80% less than the chargemaster price. This applies even if you only qualify for a partial discount.</p>

<h3>Hospitals that fail to comply can lose tax-exempt status</h3>

<p>A nonprofit hospital&rsquo;s tax exemption is worth millions of dollars per year. If the IRS finds that a hospital is not complying with 501(r) requirements&mdash;including properly administering its financial assistance program&mdash;the hospital risks losing that exemption. This gives you leverage. If a hospital is not following its own policy, a complaint to the IRS or state attorney general carries real weight.</p>

<h3>You can appeal a denial&mdash;and escalate</h3>

<p>A denial is not the final answer. You can appeal with additional documentation, escalate to the patient advocate, or file a complaint with your state attorney general&rsquo;s consumer protection division. Hospitals take state AG inquiries seriously because they can trigger broader investigations into billing practices.</p>

<h2 id="case-studies">7. Real patient results</h2>

<div class="key-takeaway">
    <strong>Want to know your hospital&rsquo;s track record before you apply?</strong> Our <a href="/hospitals/">hospital directory</a> includes transparency grades, average charity care spending, and reported income thresholds so you can walk into the process knowing what to expect.
</div>

<div class="case-study">
    <h3>Case study 1: $45,000 hospital stay reduced to $9,000</h3>
    <p><strong>Situation:</strong> A patient was hospitalized for 5 days with severe pneumonia, including 2 days in the ICU. Total bill: <strong>$45,000</strong>.</p>
    <p><strong>Patient profile:</strong> Single individual earning $35,000/year (225% of FPL). Uninsured.</p>
    <p><strong>Action:</strong> Applied for financial assistance at the nonprofit hospital. Income fell in the 200&ndash;300% FPL range, qualifying for an 80% discount under this hospital&rsquo;s policy.</p>
    <p><strong>Result:</strong> Hospital wrote off $36,000 (80%). Remaining balance: $9,000, set up on a 24-month zero-interest payment plan ($375/month).</p>
    <p><strong>Savings: $36,000.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 2: $4,000 deductible reduced to $1,600 (insured patient)</h3>
    <p><strong>Situation:</strong> A patient visited the ER for chest pain. Total bill: <strong>$8,200</strong>. Insurance covered $4,200, leaving the patient responsible for a $4,000 deductible.</p>
    <p><strong>Patient profile:</strong> Married with two children, household income $52,000/year (335% of FPL). Had insurance through employer but with a $4,000 deductible.</p>
    <p><strong>Action:</strong> Applied for financial assistance on the patient responsibility portion ($4,000). The hospital&rsquo;s policy offered a 60% discount for patients at 300&ndash;400% FPL.</p>
    <p><strong>Result:</strong> Patient responsibility reduced from $4,000 to $1,600.</p>
    <p><strong>Savings: $2,400.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 3: $12,500 surgery bill completely eliminated</h3>
    <p><strong>Situation:</strong> A patient needed outpatient surgery to repair a hernia. Total bill: <strong>$12,500</strong>.</p>
    <p><strong>Patient profile:</strong> Single individual earning $24,000/year (154% of FPL). Uninsured.</p>
    <p><strong>Action:</strong> Applied for financial assistance. Income was well below the hospital&rsquo;s 200% FPL threshold for free care.</p>
    <p><strong>Result:</strong> Entire bill written off as charity care. Patient owed $0.</p>
    <p><strong>Savings: $12,500.</strong></p>
</div>

<p>Think you might qualify? Start by <a href="/scan">uploading your bill to BillKarma</a> for a free audit, then check your hospital&rsquo;s financial assistance policy in our <a href="/hospitals/">hospital directory</a>.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Can I apply for financial assistance after I already received my hospital bill?</h3>
        <p>Yes. Most hospitals accept financial assistance applications for up to 240 days after the first billing statement. You can apply even if you have already made partial payments. The key is to apply before the bill goes to collections. Contact the billing department and request the application&mdash;they are required to provide it.</p>
    </div>

    <div class="faq-item">
        <h3>Does charity care or financial assistance affect my credit score?</h3>
        <p>No. Receiving financial assistance does not appear on your credit report. It is not a loan&mdash;it is a discount applied to your hospital account. As of 2023, the three major credit bureaus no longer include medical debt under $500 on credit reports, and paid medical collections are removed entirely.</p>
    </div>

    <div class="faq-item">
        <h3>Can I get financial assistance if I have insurance?</h3>
        <p>Yes. Many hospital financial assistance policies cover the patient responsibility portion of a bill&mdash;including deductibles, coinsurance, and copays. If your insurance left you with a large out-of-pocket balance and your income qualifies, apply for assistance on the amount you owe after insurance has paid.</p>
    </div>

    <div class="faq-item">
        <h3>What if my hospital is for-profit?</h3>
        <p>For-profit hospitals are not legally required to offer financial assistance under IRS Section 501(r), but many still have hardship or discount programs. Call the billing department and ask. You can also <a href="/guides/how-to-negotiate-medical-bills">negotiate your bill directly</a> using Medicare rates as your benchmark, or offer a lump-sum settlement for less than the full amount.</p>
    </div>

    <div class="faq-item">
        <h3>How long does the financial assistance application process take?</h3>
        <p>Most hospitals process applications within 30 to 45 days. Ask the hospital to place your account on hold during the review so it does not go to collections. If you have not received a decision within 30 days, call patient financial services for a status update and reference your application date.</p>
    </div>

    <div class="faq-item">
        <h3>What if my application is denied?</h3>
        <p>Request the denial reason in writing. The most common reasons are incomplete applications or missing documents&mdash;both fixable. Resubmit with the missing information. If denied again, escalate to the hospital patient advocate, or file a complaint with your state attorney general&rsquo;s consumer protection division. You can also <a href="/guides/how-to-dispute-a-medical-bill">dispute specific charges</a> on the bill separately from the financial assistance process.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.irs.gov/charities-non-profits/financial-assistance-policy-and-emergency-medical-care-policy-section-501r4" target="_blank" rel="noopener">IRS Section 501(r)(4): Financial Assistance Policy Requirements for Charitable Hospitals</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/charitable-hospitals-financial-assistance-and-community-benefits/" target="_blank" rel="noopener">KFF: Charitable Hospital Financial Assistance and Community Benefits</a></li>
    <li><a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">ASPE/HHS Federal Poverty Level Guidelines (2026)</a></li>
    <li><a href="https://www.consumerfinance.gov/about-us/newsroom/cfpb-publishes-report-on-medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt and Credit Reporting Changes</a></li>
    <li><a href="https://oag.ca.gov/consumers/general/hospital-fair-pricing" target="_blank" rel="noopener">California Attorney General: Hospital Fair Pricing Policies (example of state enforcement)</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2020.00893" target="_blank" rel="noopener">Health Affairs: Hospital Charge-to-Cost Ratios and Charity Care Spending (2022)</a></li>
</ul>
""",
})
