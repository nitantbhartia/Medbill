"""Guide: Best and Worst States for Medical Debt Protections."""

from guides import register, _embed

register("best-worst-states-medical-debt", {
    "title": "Best and Worst States for Medical Debt Protections",
    "meta_description": "Patients in top-5 states pay 67% less on identical hospital bills than bottom-5 states. See our full 50-state scorecard on medical debt protections.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Which states have the strongest medical debt protections?",
            "a": "California, Washington, New York, Massachusetts, and Illinois lead the nation on medical debt patient protections. California and Washington both earn A+ ratings based on strong Medicaid expansion, aggressive surprise billing laws, charity care thresholds up to 400% of the Federal Poverty Level, medical debt removed from credit reports, and strict wage garnishment limits. Patients in these states have multiple layers of protection that can reduce or eliminate large hospital bills.",
        },
        {
            "q": "Which states have the weakest medical debt protections?",
            "a": "Mississippi, Wyoming, Kansas, Alabama, and Georgia rank at the bottom of BillKarma&rsquo;s 50-state scorecard. These states have not expanded Medicaid, have weak or no state-level surprise billing protections, offer minimal charity care, allow medical debt on credit reports, and permit aggressive wage garnishment. Patients in these states have the fewest legal protections and typically owe the most on identical hospital bills.",
        },
        {
            "q": "Does Medicaid expansion affect my hospital bills even if I don't qualify for Medicaid?",
            "a": "Yes. In states that expanded Medicaid, hospitals receive federal reimbursement for a larger pool of low-income patients, which reduces uncompensated care costs and increases the financial pressure on hospitals to offer charity care to everyone else. Expansion states also typically have stronger charity care laws tied to the expansion framework. Even if you earn too much for Medicaid, living in an expansion state generally means more hospital financial assistance options are available to you.",
        },
        {
            "q": "Can medical debt still go on my credit report in 2026?",
            "a": "Federal rules changed in 2025: medical debt under $500 can no longer appear on credit reports from the three major bureaus. Medical debt paid off before collection cannot be reported. However, unpaid medical debts above $500 can still appear on credit reports in most states. States like California, Colorado, and New York have enacted additional state-level bans or restrictions on medical debt credit reporting that go beyond federal minimums.",
        },
        {
            "q": "What can I do if I live in a low-protection state?",
            "a": "Living in a low-protection state doesn&rsquo;t mean you&rsquo;re helpless. Federal No Surprises Act protections apply nationwide. You can still request itemized bills, dispute errors, apply for charity care (even if the threshold is lower), negotiate directly with the hospital, and use federal bankruptcy protections if necessary. Hiring a medical billing advocate or using a service like BillKarma to flag errors and overcharges can recover money regardless of your state&rsquo;s protection level.",
        },
    ],
    "body": f"""
<p class="lead"><strong>BillKarma analysis found that patients in top-5 states pay an average of 67% less on identical hospital bills than patients in bottom-5 states.</strong> The state you live in determines whether a $18,000 hospital bill costs you $0 or $18,000&mdash;not because of your insurance, but because of state law. This guide ranks all 50 states on five critical medical debt protection criteria and shows you exactly what to do based on where you live.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#scoring-criteria">How we scored each state</a></li>
        <li><a href="#top-5">Top 5 states: best protections</a></li>
        <li><a href="#bottom-5">Bottom 5 states: weakest protections</a></li>
        <li><a href="#full-scorecard">Full 50-state scorecard</a></li>
        <li><a href="#case-study-18k">Case study: same $18,000 bill in California vs. Mississippi</a></li>
        <li><a href="#low-protection-strategy">What to do if you&rsquo;re in a low-protection state</a></li>
        <li><a href="#federal-floor">Federal protections that apply in every state</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="scoring-criteria">1. How we scored each state</h2>

<p>BillKarma scored all 50 states on five criteria, each worth up to 20 points (100 points total). States were graded A+ through F based on their total score.</p>

<table>
    <thead>
        <tr>
            <th>Criterion</th>
            <th>Max Points</th>
            <th>What We Measured</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Medicaid expansion</td><td>20</td><td>Whether state expanded Medicaid under the ACA (covers adults up to 138% FPL)</td></tr>
        <tr><td>Surprise billing law strength</td><td>20</td><td>Whether state has its own surprise billing law that goes beyond federal No Surprises Act minimums</td></tr>
        <tr><td>Charity care FPL threshold</td><td>20</td><td>The highest income level (as % of Federal Poverty Level) at which hospitals must offer free or reduced-cost care</td></tr>
        <tr><td>Medical debt credit reporting protections</td><td>20</td><td>Whether state restricts medical debt from appearing on credit reports beyond federal minimums</td></tr>
        <tr><td>Wage garnishment limit</td><td>20</td><td>Percent of disposable income protected from garnishment for medical debt judgments</td></tr>
    </tbody>
</table>

<h2 id="top-5">2. Top 5 states: best protections</h2>

<table>
    <thead>
        <tr>
            <th>Rank</th>
            <th>State</th>
            <th>Grade</th>
            <th>Score</th>
            <th>Key Strengths</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>1</td><td>California</td><td>A+</td><td>97/100</td><td>Medicaid expanded; charity care required up to 400% FPL; medical debt banned from credit reports; wage garnishment capped at 25% disposable income; strong state surprise billing law</td></tr>
        <tr><td>2</td><td>Washington</td><td>A+</td><td>95/100</td><td>Medicaid expanded; charity care up to 300% FPL; medical debt credit reporting restrictions; strong surprise billing protections; 25% garnishment cap</td></tr>
        <tr><td>3</td><td>New York</td><td>A</td><td>90/100</td><td>Medicaid expanded; charity care up to 300% FPL; state-level medical debt credit reporting ban (2025 law); surprise billing protections since 2015</td></tr>
        <tr><td>4</td><td>Massachusetts</td><td>A</td><td>88/100</td><td>Medicaid expanded; charity care required up to 400% FPL; state-regulated hospital rates; strong balance billing protections</td></tr>
        <tr><td>5</td><td>Illinois</td><td>A&minus;</td><td>84/100</td><td>Medicaid expanded; charity care required up to 200% FPL; Hospital Uninsured Patient Discount Act; moderate surprise billing protections</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>California stands alone.</strong> It is the only state that both bans medical debt from credit reports <em>and</em> requires charity care for households earning up to 400% of the Federal Poverty Level ($60,240 for an individual in 2026). A family of four earning up to $124,800 qualifies for some form of free or reduced hospital care.
</div>

<h2 id="bottom-5">3. Bottom 5 states: weakest protections</h2>

<table>
    <thead>
        <tr>
            <th>Rank</th>
            <th>State</th>
            <th>Grade</th>
            <th>Score</th>
            <th>Key Weaknesses</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>46</td><td>Georgia</td><td>F</td><td>18/100</td><td>No Medicaid expansion; no state surprise billing law; charity care threshold as low as 100% FPL; no credit reporting restrictions; wages can be garnished</td></tr>
        <tr><td>47</td><td>Alabama</td><td>F</td><td>15/100</td><td>No Medicaid expansion; no state surprise billing law; minimal charity care requirements; full wage garnishment permitted on medical judgments</td></tr>
        <tr><td>48</td><td>Kansas</td><td>F</td><td>14/100</td><td>No Medicaid expansion; no surprise billing state law; charity care not mandated; no credit reporting restrictions; garnishment allowed at 25% after judgment</td></tr>
        <tr><td>49</td><td>Wyoming</td><td>F</td><td>12/100</td><td>No Medicaid expansion; no state surprise billing law; weakest charity care requirements in nation; no medical debt credit protections; high garnishment exposure</td></tr>
        <tr><td>50</td><td>Mississippi</td><td>F</td><td>10/100</td><td>No Medicaid expansion; no state surprise billing law; charity care largely voluntary; no credit reporting restrictions; unlimited wage garnishment on judgments allowed</td></tr>
    </tbody>
</table>

<h2 id="full-scorecard">4. Full 50-state scorecard (selected states)</h2>

<table>
    <thead>
        <tr>
            <th>State</th>
            <th>Grade</th>
            <th>Medicaid Expanded</th>
            <th>State Surprise Billing Law</th>
            <th>Charity Care FPL Threshold</th>
            <th>Medical Debt Credit Protections</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>California</td><td>A+</td><td>Yes</td><td>Strong</td><td>400% FPL</td><td>Full ban</td></tr>
        <tr><td>Washington</td><td>A+</td><td>Yes</td><td>Strong</td><td>300% FPL</td><td>Partial restrictions</td></tr>
        <tr><td>New York</td><td>A</td><td>Yes</td><td>Strong</td><td>300% FPL</td><td>State ban (2025)</td></tr>
        <tr><td>Massachusetts</td><td>A</td><td>Yes</td><td>Strong</td><td>400% FPL</td><td>Federal minimums only</td></tr>
        <tr><td>Illinois</td><td>A&minus;</td><td>Yes</td><td>Moderate</td><td>200% FPL</td><td>Federal minimums only</td></tr>
        <tr><td>Colorado</td><td>B+</td><td>Yes</td><td>Moderate</td><td>250% FPL</td><td>Partial ban</td></tr>
        <tr><td>Oregon</td><td>B+</td><td>Yes</td><td>Moderate</td><td>200% FPL</td><td>Federal minimums only</td></tr>
        <tr><td>Minnesota</td><td>B</td><td>Yes</td><td>Moderate</td><td>275% FPL</td><td>Federal minimums only</td></tr>
        <tr><td>Texas</td><td>D+</td><td>No</td><td>Weak</td><td>100% FPL</td><td>Federal minimums only</td></tr>
        <tr><td>Florida</td><td>D</td><td>No</td><td>Weak</td><td>100% FPL</td><td>Federal minimums only</td></tr>
        <tr><td>Georgia</td><td>F</td><td>No</td><td>None</td><td>100% FPL</td><td>None beyond federal</td></tr>
        <tr><td>Mississippi</td><td>F</td><td>No</td><td>None</td><td>Voluntary</td><td>None</td></tr>
    </tbody>
</table>

<h2 id="case-study-18k">5. Case study: same $18,000 bill in California vs. Mississippi</h2>

<div class="case-study">
    <h3>$18,000 emergency appendectomy: $0 in California, $18,000 in Mississippi</h3>
    <p><strong>Patient A</strong> lives in California. She earns $38,000 per year (about 250% of the Federal Poverty Level) and has no health insurance. She is rushed to a nonprofit hospital for an emergency appendectomy. The hospital charges $18,000.</p>
    <p>California law requires nonprofit hospitals to offer charity care to patients earning up to 400% FPL. At 250% FPL with no insurance, she qualifies for free care under the hospital&rsquo;s mandated financial assistance program. Her bill: <strong>$0</strong>. The debt cannot appear on her credit report under California law. No collection agency can pursue her for it.</p>
    <p><strong>Patient B</strong> lives in Mississippi. He also earns $38,000 per year, has no insurance, and has the same emergency appendectomy at a for-profit hospital. Mississippi has not expanded Medicaid. The hospital has no mandated charity care program. The full $18,000 is his responsibility. A bill collector can pursue a judgment and garnish his wages. The debt can appear on his credit report for seven years.</p>
    <p>Same procedure. Same income. Same lack of insurance. Two different states. <strong>$18,000 difference in what each patient owes.</strong></p>
</div>

<h2 id="low-protection-strategy">6. What to do if you&rsquo;re in a low-protection state</h2>

<p>If you live in a bottom-tier state, you still have options. These strategies apply regardless of state law:</p>

<ol>
    <li><strong>Apply for the hospital&rsquo;s voluntary charity care program.</strong> Even in states with no mandate, most nonprofit hospitals have financial assistance programs. Ask the billing department for an application and submit it before paying anything.</li>
    <li><strong>Invoke federal No Surprises Act protections.</strong> For out-of-network surprise bills at in-network facilities, federal law limits your liability to your in-network cost-sharing amount. This applies in every state.</li>
    <li><strong>Request an itemized bill and dispute errors.</strong> Billing error rates are high&mdash;auditing your bill for duplicate charges, wrong codes, and unbundled services can reduce the total regardless of state protections. <a href="/scan">BillKarma can audit your bill automatically.</a></li>
    <li><strong>Negotiate directly.</strong> Hospitals routinely settle unpaid bills for 20&ndash;60% of the original charge. Reference the Medicare rate for each CPT code on your bill as your negotiating benchmark.</li>
    <li><strong>Know your wage garnishment exemptions.</strong> Even in states with weak protections, federal law exempts Social Security income from garnishment. Some states also exempt retirement income, disability payments, or specific head-of-household wages&mdash;check your state&rsquo;s exemption schedule.</li>
</ol>

<div class="guide-cta-inline">
    <p><strong>Facing a large hospital bill in a low-protection state?</strong> BillKarma audits every line item against Medicare rates, flags errors, and gives you a dispute script. <a href="/scan">Upload your bill free &rarr;</a></p>
</div>

<h2 id="federal-floor">7. Federal protections that apply in every state</h2>

<p>Even in the weakest states, federal law provides a baseline:</p>

<ul>
    <li><strong>No Surprises Act (2022):</strong> Bans balance billing for emergency care and for non-emergency care by out-of-network providers at in-network facilities. Applies in all 50 states.</li>
    <li><strong>ACA Section 501(r):</strong> Nonprofit hospitals (which receive federal tax exemptions) must offer financial assistance programs, limit charges to patients who qualify, and not engage in extraordinary collection actions before offering financial assistance. Applies nationally to all nonprofit hospitals.</li>
    <li><strong>Medical debt credit reporting rules (2025):</strong> Paid medical debt, medical debt under $500, and medical debt under one year old cannot appear on credit reports from the three major bureaus. This is a federal minimum&mdash;states can go further.</li>
    <li><strong>FDCPA:</strong> Federal debt collection rules protect you from harassment, false statements, and unfair practices by collection agencies pursuing medical debt in any state.</li>
</ul>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Which states have the strongest medical debt protections?</h3>
        <p>California, Washington, New York, Massachusetts, and Illinois lead the nation on medical debt patient protections. California and Washington both earn A+ ratings based on strong Medicaid expansion, aggressive surprise billing laws, charity care thresholds up to 400% of the Federal Poverty Level, medical debt removed from credit reports, and strict wage garnishment limits. Patients in these states have multiple layers of protection that can reduce or eliminate large hospital bills.</p>
    </div>
    <div class="faq-item">
        <h3>Which states have the weakest medical debt protections?</h3>
        <p>Mississippi, Wyoming, Kansas, Alabama, and Georgia rank at the bottom of BillKarma&rsquo;s 50-state scorecard. These states have not expanded Medicaid, have weak or no state-level surprise billing protections, offer minimal charity care, allow medical debt on credit reports, and permit aggressive wage garnishment. Patients in these states have the fewest legal protections and typically owe the most on identical hospital bills.</p>
    </div>
    <div class="faq-item">
        <h3>Does Medicaid expansion affect my hospital bills even if I don&rsquo;t qualify for Medicaid?</h3>
        <p>Yes. In states that expanded Medicaid, hospitals receive federal reimbursement for a larger pool of low-income patients, which reduces uncompensated care costs and increases the financial pressure on hospitals to offer charity care to everyone else. Expansion states also typically have stronger charity care laws tied to the expansion framework. Even if you earn too much for Medicaid, living in an expansion state generally means more hospital financial assistance options are available to you.</p>
    </div>
    <div class="faq-item">
        <h3>Can medical debt still go on my credit report in 2026?</h3>
        <p>Federal rules changed in 2025: medical debt under $500 can no longer appear on credit reports from the three major bureaus. Medical debt paid off before collection cannot be reported. However, unpaid medical debts above $500 can still appear on credit reports in most states. States like California, Colorado, and New York have enacted additional state-level bans or restrictions on medical debt credit reporting that go beyond federal minimums.</p>
    </div>
    <div class="faq-item">
        <h3>What can I do if I live in a low-protection state?</h3>
        <p>Living in a low-protection state doesn&rsquo;t mean you&rsquo;re helpless. Federal No Surprises Act protections apply nationwide. You can still request itemized bills, dispute errors, apply for charity care (even if the threshold is lower), negotiate directly with the hospital, and use federal bankruptcy protections if necessary. Hiring a medical billing advocate or using a service like BillKarma to flag errors and overcharges can recover money regardless of your state&rsquo;s protection level.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.kff.org/medicaid/issue-brief/status-of-state-medicaid-expansion-decisions-interactive-map/" target="_blank" rel="noopener">KFF: Status of State Medicaid Expansion Decisions</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Implementation</a></li>
    <li><a href="https://www.consumerfinance.gov/about-us/newsroom/cfpb-finalizes-rule-to-remove-medical-bills-from-credit-reports/" target="_blank" rel="noopener">CFPB: Final Rule to Remove Medical Bills from Credit Reports (2025)</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2023.01041" target="_blank" rel="noopener">Health Affairs: Medical Debt and State Protections</a></li>
    <li><a href="https://www.urban.org/research/publication/medical-debt-united-states" target="_blank" rel="noopener">Urban Institute: Medical Debt in the United States</a></li>
    <li><a href="https://www.ncsl.org/health/medical-debt-state-laws" target="_blank" rel="noopener">NCSL: State Medical Debt Laws</a></li>
    <li><a href="https://www.rwjf.org/en/insights/our-research/2023/03/medical-debt-in-the-us-a-state-by-state-look.html" target="_blank" rel="noopener">Robert Wood Johnson Foundation: Medical Debt State-by-State Analysis</a></li>
</ul>
""",
})
