"""Guide: How Much Does a Blood Test Cost? (2026 Price Guide)."""

from guides import register, _embed

register("how-much-does-blood-test-cost", {
    "title": "How Much Does a Blood Test Cost? (2026 Price Guide)",
    "meta_description": "Blood tests cost $10-$3,000 depending on the test. A basic panel is $100-$300 without insurance. See costs for 15 common tests and where to get them cheapest.",
    "published": "2026-04-04",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does a blood test cost without insurance?",
            "a": "Without insurance, a basic blood test like a CBC costs $15-$30 at an independent lab or $120-$250 at a hospital. A comprehensive metabolic panel runs $25-$50 at Quest or LabCorp vs. $280-$500 at a hospital outpatient lab. Direct-to-consumer services like Walk-In Lab or Ulta Lab Tests offer panels for $25-$80 with no doctor's order required.",
        },
        {
            "q": "Why does the same blood test cost $30 at Quest and $500 at a hospital?",
            "a": "Hospital outpatient labs bill from their Chargemaster, an unregulated internal price list that includes overhead for the entire facility. Independent labs like Quest and LabCorp operate high-volume, low-cost facilities dedicated to lab work. They negotiate bulk rates on reagents and run thousands of tests daily. The test itself is identical regardless of where it is processed.",
        },
        {
            "q": "Are blood tests covered by insurance?",
            "a": "Most blood tests are covered by insurance when ordered by a doctor. Preventive screenings like cholesterol panels and glucose tests are covered at 100% with no cost-sharing under the ACA when performed as part of a preventive visit. Diagnostic blood tests (ordered because you have symptoms) are subject to your deductible and coinsurance. Always confirm the test is coded as preventive to avoid unexpected charges.",
        },
        {
            "q": "Which blood tests are free under the ACA?",
            "a": "The ACA requires insurers to cover certain preventive screenings at no cost. These include cholesterol screening (lipid panel, CPT 80061) for adults over 40, blood glucose/diabetes screening for adults with high blood pressure, and hepatitis B and C screening. The key is that the test must be coded as preventive, not diagnostic. If your doctor orders the same test to investigate symptoms, it may be billed as diagnostic and subject to your deductible.",
        },
        {
            "q": "Can I order blood tests without a doctor?",
            "a": "Yes, in most states. Direct-to-consumer lab services like Walk-In Lab, Ulta Lab Tests, and Request A Test let you order blood work online, visit a local draw site, and receive results in 1-3 days. Prices are typically 50-80% less than hospital pricing. Some states (New York, New Jersey, Rhode Island) restrict direct-to-consumer lab ordering and require a physician's order.",
        },
    ],
    "body": f"""
<p class="lead">A simple blood draw can cost anywhere from <strong>$10 to $3,000+</strong> depending on where you get it, what tests are ordered, and whether you have insurance. A basic panel like a CBC or metabolic panel costs <strong>$100&ndash;$300 without insurance</strong> at a hospital&mdash;but as little as $15&ndash;$40 at an independent lab. The difference isn&rsquo;t the science; it&rsquo;s the billing. This guide breaks down what 15 common blood tests actually cost, why prices vary so wildly, and how to pay the lowest possible price.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-table">What 15 common blood tests cost</a></li>
        <li><a href="#where-to-go">Hospital vs. lab vs. direct-to-consumer pricing</a></li>
        <li><a href="#why-prices-vary">Why the same test costs $30 at Quest and $500 at a hospital</a></li>
        <li><a href="#insurance-coverage">Insurance coverage and preventive screening rules</a></li>
        <li><a href="#free-tests">When blood tests are free under the ACA</a></li>
        <li><a href="#save-money">5 ways to save on blood work</a></li>
        <li><a href="#case-studies">Real-world examples</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-table">1. What 15 common blood tests cost</h2>

<p>The table below shows the CPT code, Medicare reimbursement rate, and typical price ranges for the 15 most commonly ordered blood tests. The Medicare rate represents what the federal government has determined is a fair price for each test. Hospital charges are typically 5&ndash;30x higher.</p>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Test Name</th><th>Medicare Rate</th><th>Independent Lab (Self-Pay)</th><th>Hospital Outpatient Lab</th></tr>
    </thead>
    <tbody>
        <tr><td>85025</td><td>Complete Blood Count (CBC) with Differential</td><td>$11</td><td>$15&ndash;$30</td><td>$120&ndash;$250</td></tr>
        <tr><td>80053</td><td>Comprehensive Metabolic Panel (CMP)</td><td>$16</td><td>$25&ndash;$45</td><td>$280&ndash;$500</td></tr>
        <tr><td>80048</td><td>Basic Metabolic Panel (BMP)</td><td>$14</td><td>$20&ndash;$40</td><td>$250&ndash;$400</td></tr>
        <tr><td>80061</td><td>Lipid Panel (Cholesterol)</td><td>$18</td><td>$20&ndash;$35</td><td>$150&ndash;$300</td></tr>
        <tr><td>84443</td><td>TSH (Thyroid-Stimulating Hormone)</td><td>$28</td><td>$25&ndash;$45</td><td>$150&ndash;$350</td></tr>
        <tr><td>83036</td><td>Hemoglobin A1C (Diabetes Marker)</td><td>$14</td><td>$18&ndash;$35</td><td>$100&ndash;$200</td></tr>
        <tr><td>86900</td><td>Blood Typing (ABO)</td><td>$7</td><td>$10&ndash;$25</td><td>$50&ndash;$150</td></tr>
        <tr><td>84439</td><td>Free Thyroxine (Free T4)</td><td>$15</td><td>$20&ndash;$40</td><td>$100&ndash;$250</td></tr>
        <tr><td>84153</td><td>PSA (Prostate-Specific Antigen)</td><td>$28</td><td>$25&ndash;$50</td><td>$120&ndash;$300</td></tr>
        <tr><td>82306</td><td>Vitamin D, 25-Hydroxy</td><td>$40</td><td>$35&ndash;$65</td><td>$200&ndash;$450</td></tr>
        <tr><td>84436</td><td>Total Thyroxine (T4)</td><td>$12</td><td>$15&ndash;$30</td><td>$80&ndash;$200</td></tr>
        <tr><td>82728</td><td>Ferritin (Iron Stores)</td><td>$19</td><td>$20&ndash;$40</td><td>$100&ndash;$250</td></tr>
        <tr><td>85610</td><td>Prothrombin Time (PT/INR)</td><td>$6</td><td>$10&ndash;$20</td><td>$50&ndash;$150</td></tr>
        <tr><td>82947</td><td>Glucose (Blood Sugar)</td><td>$6</td><td>$8&ndash;$15</td><td>$40&ndash;$120</td></tr>
        <tr><td>82746</td><td>Folic Acid (Folate)</td><td>$21</td><td>$20&ndash;$40</td><td>$100&ndash;$250</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The pattern is clear:</strong> Medicare rates for routine blood tests range from $6 to $40. Independent labs charge close to those rates. Hospital outpatient labs charge 5&ndash;30x more for the identical test processed on the same equipment using the same reagents. The difference is pure facility markup.
</div>

<p>Look up the cost of any blood test by CPT code:</p>

{_embed(mode="cost", cpt="80053", title="Look Up Blood Test Cost", subtitle="Enter the CPT code from your lab order.")}

<h2 id="where-to-go">2. Hospital vs. lab vs. direct-to-consumer pricing</h2>

<p>Where you get your blood drawn has a bigger impact on cost than what test is ordered. Here&rsquo;s how the three main options compare for a common panel of tests (CBC + CMP + lipid panel):</p>

<table>
    <thead>
        <tr><th>Option</th><th>Cost for CBC + CMP + Lipid Panel</th><th>Doctor&rsquo;s Order Required?</th><th>Results Turnaround</th><th>Best For</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Hospital outpatient lab</strong></td><td>$550&ndash;$1,050</td><td>Yes</td><td>Same day&ndash;3 days</td><td>Patients already at the hospital or needing specialized tests</td></tr>
        <tr><td><strong>Independent lab</strong> (Quest, LabCorp)</td><td>$60&ndash;$110</td><td>Yes</td><td>1&ndash;3 days</td><td>Anyone with a doctor&rsquo;s order who wants fair pricing</td></tr>
        <tr><td><strong>Direct-to-consumer</strong> (Walk-In Lab, Ulta Lab Tests)</td><td>$40&ndash;$80</td><td>No</td><td>1&ndash;3 days</td><td>Uninsured patients, health monitoring, no doctor visit needed</td></tr>
    </tbody>
</table>

<p>Direct-to-consumer services partner with the same national labs (Quest, LabCorp) but offer pre-negotiated cash prices. You order online, walk into a local draw site, and get results sent to your email. No doctor&rsquo;s visit, no facility fee, no surprise bill.</p>

<div class="key-takeaway">
    <strong>The hospital lab is almost never the cheapest option for routine blood work.</strong> Unless your doctor needs results within hours or the test requires specialized hospital equipment, an independent lab or direct-to-consumer service will save you 80&ndash;95%. Always ask your doctor: &ldquo;Can you send this order to Quest or LabCorp instead?&rdquo;
</div>

<h2 id="why-prices-vary">3. Why the same test costs $30 at Quest and $500 at a hospital</h2>

<p>The price variation in blood tests is not about quality, accuracy, or speed. It comes down to three structural factors:</p>

<p><strong>Facility overhead allocation.</strong> Hospital labs are part of a larger facility with emergency departments, operating rooms, and administrative staff. Hospitals spread these overhead costs across all departments, including the lab. When you pay $300 for a CMP at a hospital, you&rsquo;re subsidizing the cost of running a 24/7 emergency department&mdash;not paying for a more accurate blood test.</p>

<p><strong>Chargemaster pricing.</strong> Hospitals set prices via their Chargemaster&mdash;an internal, unregulated price list. These prices are not based on cost, market rates, or what Medicare pays. They&rsquo;re set by hospital administrators and are primarily used as a starting point for insurance negotiations. Uninsured patients who don&rsquo;t negotiate get the full Chargemaster price. Learn more in our <a href="/guides/why-lab-test-bills-are-so-high">guide to why lab test bills are so high</a>.</p>

<p><strong>Volume economics.</strong> Quest Diagnostics processes over <strong>500 million tests per year</strong> across dedicated lab facilities optimized for throughput. Their cost per test is a fraction of a hospital lab that processes a few hundred tests daily alongside patient care. This scale advantage gets passed to consumers in the form of lower pricing.</p>

<div class="case-study">
    <h3>Case study: Same test, 17x price difference</h3>
    <p><strong>Situation:</strong> Maria needed a comprehensive metabolic panel (CPT 80053) and CBC (CPT 85025) as part of an annual physical. Her doctor&rsquo;s office sent the order to the affiliated hospital outpatient lab without asking her preference.</p>
    <p><strong>Hospital bill:</strong> CMP: $420. CBC: $185. Total: <strong>$605</strong>.</p>
    <p><strong>What she would have paid at Quest (self-pay):</strong> CMP: $29. CBC: $17. Total: <strong>$46</strong>.</p>
    <p><strong>Difference: $559</strong>&mdash;for identical tests processed on the same type of analyzer. Maria called the hospital, asked for the self-pay rate, and negotiated the bill down to $180. She now asks her doctor to route all lab orders to Quest. <strong>Annual savings: $1,200+.</strong></p>
</div>

<h2 id="insurance-coverage">4. Insurance coverage and preventive screening rules</h2>

<p>How much you pay for blood tests depends heavily on whether the test is classified as <strong>preventive</strong> or <strong>diagnostic</strong>:</p>

<table>
    <thead>
        <tr><th>Classification</th><th>What It Means</th><th>Your Cost</th><th>Example</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Preventive</strong></td><td>Routine screening with no symptoms</td><td>$0 (covered 100% under ACA)</td><td>Annual cholesterol panel for a 45-year-old with no heart disease</td></tr>
        <tr><td><strong>Diagnostic</strong></td><td>Ordered to investigate symptoms or monitor a condition</td><td>Subject to deductible + coinsurance</td><td>Lipid panel ordered because your cholesterol was high last time</td></tr>
    </tbody>
</table>

<p>The exact same test&mdash;a lipid panel (CPT 80061)&mdash;can be free or cost you $200+ depending on how your doctor codes the visit. If the visit is coded as a <strong>preventive exam</strong> (ICD-10 code Z00.00), the lab work is covered at 100%. If the visit is coded as a <strong>follow-up for hyperlipidemia</strong> (ICD-10 code E78.5), the lab work becomes diagnostic and hits your deductible.</p>

<div class="key-takeaway">
    <strong>Ask your doctor before the visit:</strong> &ldquo;Will this lab work be coded as preventive?&rdquo; If your doctor says yes, confirm with the billing office that the visit will carry a preventive diagnosis code. This one question can save you $100&ndash;$500. Learn more in our <a href="/guides/preventive-care-billing">guide to preventive care billing</a>.
</div>

<h2 id="free-tests">5. When blood tests are free under the ACA</h2>

<p>The Affordable Care Act requires all non-grandfathered health plans to cover certain preventive services at <strong>no cost-sharing</strong>&mdash;no copay, no deductible, no coinsurance. For blood tests, the key covered screenings include:</p>

<ul>
    <li><strong>Cholesterol screening</strong> (lipid panel, CPT 80061) &mdash; for adults at elevated risk, typically age 40+ or with risk factors</li>
    <li><strong>Blood glucose / diabetes screening</strong> &mdash; for adults aged 35&ndash;70 who are overweight or obese</li>
    <li><strong>Hepatitis B screening</strong> &mdash; for adolescents and adults at increased risk</li>
    <li><strong>Hepatitis C screening</strong> &mdash; for all adults aged 18&ndash;79</li>
    <li><strong>HIV screening</strong> &mdash; for all adults aged 15&ndash;65</li>
    <li><strong>Lead screening</strong> &mdash; for children at risk</li>
    <li><strong>Syphilis screening</strong> &mdash; for adults at increased risk</li>
    <li><strong>Iron deficiency anemia screening</strong> &mdash; for pregnant women</li>
</ul>

<p>If you were charged for a preventive blood test, the problem is usually one of two things: the visit was coded as diagnostic instead of preventive, or the lab is out-of-network. Both are fixable. Call your doctor&rsquo;s billing office to request a coding correction, or call your insurer to dispute the charge.</p>

<div class="case-study">
    <h3>Case study: Preventive lab work billed as diagnostic&mdash;$340 overcharge</h3>
    <p><strong>Situation:</strong> James, age 50, went for his annual physical. His doctor ordered routine blood work including a CBC, CMP, and lipid panel as part of the preventive exam. Three weeks later, James received a bill for $340.</p>
    <p><strong>What went wrong:</strong> The doctor&rsquo;s office coded the visit as a diagnostic visit (ICD-10 code R73.09, &ldquo;abnormal glucose&rdquo;) instead of a preventive visit (Z00.00) because James had borderline glucose on his previous labs. This turned the entire panel from preventive (free) to diagnostic (subject to his $2,500 deductible).</p>
    <p><strong>Resolution:</strong> James called the doctor&rsquo;s office and asked them to recode the visit as a preventive exam with incidental findings. The office resubmitted the claim with the preventive diagnosis code. Insurance reprocessed it as preventive screening. <strong>New patient cost: $0. Savings: $340.</strong></p>
</div>

<h2 id="save-money">6. Five ways to save on blood work</h2>

<ol>
    <li><strong>Use an independent lab instead of a hospital lab.</strong> Ask your doctor to route orders to Quest, LabCorp, or a local reference lab. Savings: 80&ndash;95% vs. hospital pricing. The results are identical.</li>
    <li><strong>Try direct-to-consumer lab services.</strong> If you don&rsquo;t need a doctor&rsquo;s order, services like Walk-In Lab and Ulta Lab Tests offer pre-negotiated cash prices. A comprehensive wellness panel (CBC + CMP + lipid + thyroid + A1C) typically costs $60&ndash;$100.</li>
    <li><strong>Confirm preventive coding before your visit.</strong> Ask your doctor: &ldquo;Will this visit and lab work be coded as preventive?&rdquo; Preventive labs are free under the ACA. One wrong diagnosis code can turn a $0 lab visit into a $400 bill.</li>
    <li><strong>Ask for the self-pay rate.</strong> If you&rsquo;re uninsured or your deductible is high, tell the lab you want to pay the cash/self-pay rate. Hospital labs typically offer 40&ndash;60% off their Chargemaster price for self-pay patients. You can also use an HSA or FSA to pay&mdash;see our <a href="/guides/hsa-fsa-pay-medical-bills">HSA/FSA guide</a>.</li>
    <li><strong>Audit your lab bill for errors.</strong> Lab bills are among the most error-prone in medical billing. Check for duplicate charges, unbundled panel codes, and tests you didn&rsquo;t order. <a href="/scan">Upload your bill to BillKarma</a> to check every line item automatically.</li>
</ol>

<div class="key-takeaway">
    <strong>Bottom line:</strong> The biggest single savings move is switching from a hospital outpatient lab to an independent lab. For a patient who gets blood work twice a year, this change alone saves $500&ndash;$2,000 annually&mdash;with zero difference in test quality or accuracy.
</div>

<div class="case-study">
    <h3>Case study: $2,800 lab bill reduced to $90</h3>
    <p><strong>Situation:</strong> Priya, uninsured, visited an urgent care clinic for fatigue. The doctor ordered a battery of blood tests: CBC, CMP, lipid panel, TSH, free T4, vitamin D, ferritin, and hemoglobin A1C. The urgent care sent the labs to a hospital outpatient facility.</p>
    <p><strong>Total bill: $2,800</strong> for eight tests. The Medicare rate for all eight tests combined: <strong>$163</strong>.</p>
    <p><strong>What Priya did:</strong> She called the hospital billing department and requested the self-pay discount. They offered 50% off: $1,400. She then cited the Medicare rates for each test and asked to pay the Medicare rate plus a 50% margin. The hospital agreed to <strong>$245</strong>. Finally, she set up the same tests through Walk-In Lab for future monitoring at <strong>$90 total</strong>.</p>
    <p><strong>Lesson:</strong> Never accept the first number on a hospital lab bill. The Chargemaster price has no relationship to the actual cost of the test. Negotiate using Medicare rates as your benchmark.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does a blood test cost without insurance?</h3>
        <p>Without insurance, a basic blood test like a CBC costs $15&ndash;$30 at an independent lab (Quest, LabCorp) or $120&ndash;$250 at a hospital outpatient lab. A comprehensive metabolic panel runs $25&ndash;$50 at an independent lab vs. $280&ndash;$500 at a hospital. Direct-to-consumer services offer the lowest prices: $25&ndash;$80 for common panels with no doctor&rsquo;s order required. Always compare prices before your blood draw.</p>
    </div>

    <div class="faq-item">
        <h3>Why does the same blood test cost $30 at Quest and $500 at a hospital?</h3>
        <p>Hospital outpatient labs bill from their Chargemaster&mdash;an unregulated internal price list that includes overhead for the entire facility (ER, operating rooms, administration). Independent labs like Quest and LabCorp run dedicated, high-volume facilities optimized for testing, with dramatically lower overhead. The test itself&mdash;the reagents, the equipment, the methodology&mdash;is identical. You&rsquo;re paying for the building, not the science.</p>
    </div>

    <div class="faq-item">
        <h3>Are blood tests covered by insurance?</h3>
        <p>Most blood tests are covered when ordered by a doctor. Preventive screenings (cholesterol, diabetes, hepatitis) are covered at 100% with no cost-sharing under the ACA. Diagnostic tests ordered to investigate symptoms are subject to your deductible and coinsurance. The critical factor is how the visit is coded&mdash;preventive vs. diagnostic. Ask your doctor before the visit to confirm the coding.</p>
    </div>

    <div class="faq-item">
        <h3>Which blood tests are free under the ACA?</h3>
        <p>The ACA mandates free coverage for preventive screenings including cholesterol (lipid panel) for at-risk adults, blood glucose and diabetes screening for overweight adults 35&ndash;70, hepatitis B and C screening, HIV screening for ages 15&ndash;65, and certain other risk-based tests. The test must be coded as preventive (not diagnostic) and performed at an in-network lab to qualify for $0 cost-sharing.</p>
    </div>

    <div class="faq-item">
        <h3>Can I order blood tests without a doctor?</h3>
        <p>Yes, in most states. Direct-to-consumer services like Walk-In Lab, Ulta Lab Tests, and Request A Test let you order blood work online at pre-negotiated cash prices. You visit a local Quest or LabCorp draw site and receive results in 1&ndash;3 days. Prices are 50&ndash;80% below hospital rates. Note: New York, New Jersey, and Rhode Island restrict direct-to-consumer ordering and require a physician&rsquo;s order.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/clinical-laboratory" target="_blank" rel="noopener noreferrer">CMS Clinical Laboratory Fee Schedule (2026)</a></li>
    <li><a href="https://www.healthcare.gov/coverage/preventive-care-benefits/" target="_blank" rel="noopener noreferrer">HealthCare.gov: Preventive Care Benefits</a></li>
    <li><a href="https://www.uspreventiveservicestaskforce.org/uspstf/recommendation-topics" target="_blank" rel="noopener noreferrer">U.S. Preventive Services Task Force: Recommended Screenings</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2019.01019" target="_blank" rel="noopener noreferrer">Health Affairs: Variation in Prices Paid for Lab Tests</a></li>
    <li><a href="https://www.gao.gov/products/gao-14-131" target="_blank" rel="noopener noreferrer">GAO: Medicare Lab Test Payment Rates</a></li>
    <li><a href="https://kffhealthnews.org/news/article/hospital-outpatient-lab-tests-expensive/" target="_blank" rel="noopener noreferrer">KFF Health News: Hospital Outpatient Labs Among the Priciest</a></li>
</ul>
""",
})
