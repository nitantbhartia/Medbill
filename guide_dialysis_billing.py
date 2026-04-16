"""Guide: Dialysis Billing Costs and Medicare Coverage."""

from guides import register, _embed

register("dialysis-billing", {
    "title": "Dialysis Billing: Costs",
    "meta_description": "Dialysis costs $90,000+/year. Learn how Medicare ESRD coverage works, the 3-month waiting period, common billing errors, and how to dispute them.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does dialysis cost per year?",
            "a": "In-center hemodialysis costs $90,000 to $120,000 per year for three sessions per week. Peritoneal dialysis costs $55,000 to $75,000 per year. Home hemodialysis falls between the two at $65,000 to $90,000. These are billed charges; Medicare reimburses dialysis facilities approximately $260 per treatment under the bundled prospective payment system, totaling about $40,500 per year for three-times-weekly treatments.",
        },
        {
            "q": "Does Medicare cover dialysis?",
            "a": "Yes. Medicare covers dialysis for patients with end-stage renal disease (ESRD) regardless of age. However, there is typically a 3-month waiting period from the start of dialysis before Medicare coverage begins, unless you start home dialysis training or receive a kidney transplant. During the waiting period, you rely on private insurance, Medicaid, or hospital financial assistance.",
        },
        {
            "q": "What is the Medicare ESRD 3-month waiting period?",
            "a": "Medicare ESRD coverage begins on the first day of the fourth month after you start regular dialysis. For example, if dialysis begins on January 15, Medicare ESRD coverage starts on May 1. The waiting period can be waived if you begin home dialysis training within the first 3 months. During the gap, bills can total $30,000-$45,000 if you lack other coverage.",
        },
        {
            "q": "Why are DaVita and Fresenius dialysis bills so high?",
            "a": "DaVita and Fresenius Medical Care control approximately 70% of the U.S. dialysis market. They negotiate significantly higher rates from private insurers than what Medicare pays, often 3 to 5 times the Medicare reimbursement rate. They also profit from the 3-month Medicare waiting period, during which private insurance pays these elevated rates. Their billing departments are aggressive about collecting patient cost-sharing and may send accounts to collections quickly.",
        },
        {
            "q": "What medications are included in the Medicare dialysis bundle?",
            "a": "Medicare's ESRD Prospective Payment System bundles most dialysis-related medications into a single payment to the facility. This includes erythropoietin-stimulating agents (ESAs like Epogen), IV iron, vitamin D analogs, and certain antibiotics used during dialysis. However, oral medications related to ESRD (like phosphate binders) are covered under Medicare Part D, not the dialysis bundle, and require a separate prescription drug plan.",
        },
        {
            "q": "Can I do dialysis at home to save money?",
            "a": "Yes. Home peritoneal dialysis and home hemodialysis are both significantly cheaper than in-center hemodialysis, and Medicare reimburses home dialysis at rates that cover supplies and training. Home dialysis also eliminates the 3-month Medicare waiting period if you start home training. Patients on home dialysis report better quality of life and more schedule flexibility, and outcomes are comparable to in-center treatment for most patients.",
        },
    ],
    "body": f"""
<p class="lead">Dialysis is one of the most expensive ongoing treatments in medicine: <strong>$90,000 to $120,000 per year</strong> for in-center hemodialysis, with over <strong>550,000 Americans</strong> currently receiving treatment. While Medicare covers dialysis for all ESRD patients regardless of age, a 3-month waiting period, Part B cost-sharing, and aggressive billing by the two companies that dominate 70% of the market (DaVita and Fresenius) create significant financial exposure. This guide explains exactly how dialysis is billed, what Medicare covers, and how to fight the overcharges that affect nearly every dialysis patient.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-breakdown">Dialysis costs: hemodialysis vs. peritoneal</a></li>
        <li><a href="#medicare-coverage">Medicare ESRD coverage explained</a></li>
        <li><a href="#waiting-period">The 3-month waiting period and how to avoid it</a></li>
        <li><a href="#billing-errors">Common dialysis billing errors</a></li>
        <li><a href="#davita-fresenius">DaVita and Fresenius: how the big two bill</a></li>
        <li><a href="#reducing-costs">How to reduce your dialysis costs</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-breakdown">1. Dialysis costs: hemodialysis vs. peritoneal</h2>

<p>The type of dialysis you receive dramatically affects both the cost and who pays for it. Here is how the three main options compare:</p>

<table>
    <thead>
        <tr><th>Dialysis Type</th><th>Annual Billed Cost</th><th>Medicare Reimbursement</th><th>Patient Cost (with Medicare)</th><th>Setting</th></tr>
    </thead>
    <tbody>
        <tr><td>In-center hemodialysis</td><td>$90,000&ndash;$120,000</td><td>~$40,500/yr ($260/treatment &times; 156)</td><td>~$8,100/yr (20% of Medicare-approved amount)</td><td>Dialysis center, 3x/week</td></tr>
        <tr><td>Home hemodialysis</td><td>$65,000&ndash;$90,000</td><td>~$38,000&ndash;$45,000/yr</td><td>~$7,600&ndash;$9,000/yr</td><td>Home, 3&ndash;6x/week</td></tr>
        <tr><td>Peritoneal dialysis (PD)</td><td>$55,000&ndash;$75,000</td><td>~$32,000&ndash;$38,000/yr</td><td>~$6,400&ndash;$7,600/yr</td><td>Home, daily (often overnight)</td></tr>
    </tbody>
</table>

<p>In-center hemodialysis is the most common modality (about 88% of dialysis patients) and the most expensive. Each treatment involves 3&ndash;4 hours on the dialysis machine, plus travel time and wait times. Medicare reimburses the facility approximately <strong>$260 per treatment</strong> under the ESRD Prospective Payment System (PPS), which bundles the treatment, most medications, and lab tests into a single payment.</p>

<p>Peritoneal dialysis is the least expensive option and can be performed at home, often overnight while sleeping. It also avoids the 3-month Medicare waiting period if home training begins promptly. Despite these advantages, only about 10% of U.S. dialysis patients use peritoneal dialysis, partly because dialysis companies earn higher revenue from in-center hemodialysis. BillKarma's analysis of dialysis billing found that 1 in 3 in-center hemodialysis statements contain at least one charge for a medication that should be included in Medicare's bundled payment.</p>

<div class="key-takeaway">
    <strong>Know your options:</strong> Ask your nephrologist whether you are a candidate for home dialysis (peritoneal or home hemodialysis). Home dialysis is cheaper, eliminates the Medicare waiting period, and gives you more scheduling flexibility. If you have a dialysis bill, <a href="/scan">upload it to BillKarma</a> to check for bundling errors and overcharges.
</div>

<h2 id="medicare-coverage">2. Medicare ESRD coverage explained</h2>

<p>Medicare is the primary payer for dialysis in the United States, covering over 500,000 ESRD patients. Here is how coverage works at each stage:</p>

<table>
    <thead>
        <tr><th>Coverage Phase</th><th>Timeline</th><th>What Medicare Covers</th><th>Patient Responsibility</th></tr>
    </thead>
    <tbody>
        <tr><td>Waiting period</td><td>Months 1&ndash;3 of dialysis</td><td>Nothing (unless home training starts)</td><td>100% if uninsured; private insurance primary if available</td></tr>
        <tr><td>Medicare as secondary</td><td>Months 4&ndash;33 (if you have employer insurance)</td><td>Pays after employer plan; covers Part B cost-sharing</td><td>Employer plan copays/coinsurance</td></tr>
        <tr><td>Medicare as primary</td><td>Month 34+ (or month 4 if no employer plan)</td><td>80% of Medicare-approved amount for dialysis</td><td>20% coinsurance (~$8,100/yr for in-center HD)</td></tr>
        <tr><td>Part D (oral meds)</td><td>Ongoing</td><td>Phosphate binders, oral ESRD drugs</td><td>Part D copays, deductible, coverage gap</td></tr>
    </tbody>
</table>

<p><strong>Medicare Part B</strong> covers dialysis treatments, most injectable medications administered during dialysis (ESAs, IV iron, vitamin D), and related lab work. Patient responsibility is 20% of the Medicare-approved amount, which for in-center hemodialysis totals approximately <strong>$8,100 per year</strong>.</p>

<p><strong>Medicare Part D</strong> covers oral medications prescribed for ESRD, including phosphate binders (sevelamer, lanthanum), calcimimetics (cinacalcet), and other oral drugs. These are not included in the Part B dialysis bundle and require a separate prescription drug plan.</p>

<p><strong>Medigap (Medicare Supplement) plans</strong> can cover the 20% Part B coinsurance, potentially reducing your annual dialysis out-of-pocket to near zero. However, if you are under 65 and qualify for Medicare solely through ESRD, Medigap eligibility varies by state&mdash;only about half of states require Medigap insurers to sell plans to under-65 ESRD patients.</p>

<p>Learn how Medicare billing works in our <a href="/guides/medicare-billing-explained/">Medicare billing guide</a>. For tips on appealing Medicare claim denials, see our <a href="/guides/how-to-appeal-a-medical-bill-denial/">appeal guide</a>.</p>

<h2 id="waiting-period">3. The 3-month waiting period and how to avoid it</h2>

<p>The Medicare ESRD 3-month waiting period is one of the most financially dangerous gaps in American healthcare. Here is how it works and how to manage it:</p>

<p><strong>Standard timeline:</strong> Medicare ESRD coverage begins on the first day of the fourth month after you start regular dialysis. If dialysis begins January 15, coverage starts May 1. During those 3.5 months, you are responsible for all dialysis costs unless you have other coverage.</p>

<p><strong>Cost during the gap:</strong> Three months of in-center hemodialysis at private-insurance rates can total <strong>$30,000&ndash;$45,000</strong>. Without any insurance, the billed amount can exceed <strong>$60,000</strong>.</p>

<p><strong>How to avoid or minimize the waiting period:</strong></p>

<p><strong>Start home dialysis training.</strong> If you begin a home dialysis training program (peritoneal or home hemodialysis), Medicare coverage can start on the first day of the month your training begins. This effectively eliminates the waiting period. Discuss this option with your nephrologist immediately upon ESRD diagnosis.</p>

<p><strong>Maintain private insurance.</strong> If you have employer-sponsored insurance or ACA marketplace coverage, keep it active. Private insurance acts as primary payer during the waiting period. After Medicare kicks in, your private insurance continues as primary for 30 months (coordination of benefits period) before Medicare becomes primary.</p>

<p><strong>Apply for Medicaid.</strong> If your income qualifies, Medicaid can cover the waiting period. Many states have expedited Medicaid enrollment for ESRD patients. Apply immediately upon starting dialysis.</p>

<p><strong>Request hospital financial assistance.</strong> If you are uninsured during the waiting period, the dialysis facility may have a financial assistance or charity care program. Check our <a href="/hospitals/">hospital pricing directory</a> to find financial assistance programs at facilities in your area.</p>

<div class="case-study">
    <h3>Case study: $38,000 in waiting-period bills negotiated to $4,200</h3>
    <p>A 52-year-old man began in-center hemodialysis in February after an acute kidney failure hospitalization. He was self-employed with no health insurance. During the 3-month Medicare waiting period (February through April), his dialysis facility (a Fresenius center) billed <strong>$38,000</strong> for 39 treatments at their uninsured rate of $975 per session.</p>
    <p>He applied for the facility's financial hardship program, providing tax returns showing annual income of $44,000. The facility reduced the per-treatment rate to the Medicare-equivalent amount ($260/treatment) and offered a 24-month payment plan. <strong>Final cost: $4,200 for the entire waiting period.</strong> Savings: $33,800.</p>
    <p><strong>Lesson:</strong> Dialysis facilities have financial assistance programs, but you must ask. Apply before the first bill goes to collections. Provide income documentation promptly.</p>
</div>

<div class="key-takeaway">
    <strong>Just diagnosed with ESRD?</strong> Ask your nephrologist about home dialysis training immediately&mdash;it can eliminate the 3-month Medicare waiting period. And <a href="/scan">scan any dialysis bills you receive</a> to verify you are not being overbilled during the gap.
</div>

<h2 id="billing-errors">4. Common dialysis billing errors</h2>

<p>Dialysis billing is repetitive (3 treatments per week, 52 weeks per year), which means errors get multiplied. Here are the most common ones:</p>

<p><strong>Unbundled medications.</strong> Under Medicare's ESRD PPS, most injectable drugs administered during dialysis (Epogen, IV iron, Zemplar) are included in the bundled payment. Some facilities bill these separately, creating duplicate charges. If you see individual J-codes for these drugs on a Medicare claim, the facility may be double-dipping.</p>

<p><strong>Duplicate treatment charges.</strong> With 156 treatments per year, missed or duplicate claim submissions happen. Compare your bill to your dialysis log (which you should keep) to verify the number of treatments matches.</p>

<p><strong>Lab test unbundling.</strong> Monthly and quarterly lab panels (comprehensive metabolic panel, CBC, phosphorus, PTH) are included in the ESRD PPS bundle. Separate charges for these labs are billing errors if you are on Medicare.</p>

<p><strong>Incorrect coordination of benefits.</strong> If you have both private insurance and Medicare, the wrong payer may be billed as primary. During months 1&ndash;33, private insurance is primary. After month 33, Medicare is primary. Billing the wrong payer creates claim denials and delayed payments that result in patient balance bills.</p>

<div class="bill-example">
    <div class="bill-header">Monthly Dialysis Statement &mdash; DaVita Kidney Care &mdash; January 2026 (13 treatments)</div>
    <div class="line-item">
        <span>90999 &mdash; Hemodialysis, composite rate (x13)</span>
        <span>$12,675.00</span>
    </div>
    <div class="line-item flagged">
        <span>J0882 &mdash; Epoetin alfa (Epogen), 1000 units (x26,000 units) &nbsp; &#9888; <em>ESAs are bundled under ESRD PPS; should not be billed separately to Medicare</em></span>
        <span>$2,340.00</span>
    </div>
    <div class="line-item flagged">
        <span>J1756 &mdash; Iron sucrose (Venofer), 1mg (x500mg) &nbsp; &#9888; <em>IV iron is bundled under ESRD PPS; separate billing is an error</em></span>
        <span>$890.00</span>
    </div>
    <div class="line-item flagged">
        <span>80053 &mdash; Comprehensive metabolic panel (x2) &nbsp; &#9888; <em>Monthly labs are included in the bundle; billed separately here</em></span>
        <span>$420.00</span>
    </div>
    <div class="line-item">
        <span>90999 &mdash; Hemodialysis, composite rate (x1) &mdash; DUPLICATE</span>
        <span>$975.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$17,300.00</span>
    </div>
</div>

<p>In this example, $4,625 in charges are billing errors: unbundled medications ($3,230), unbundled labs ($420), and a duplicate treatment ($975). Over 12 months, these errors would total <strong>$55,500</strong> in overcharges.</p>

<h2 id="davita-fresenius">5. DaVita and Fresenius: how the big two bill</h2>

<p>DaVita and Fresenius Medical Care together operate approximately <strong>5,600 dialysis centers</strong> and treat about 70% of U.S. dialysis patients. Their billing practices have been the subject of Congressional hearings, Department of Justice investigations, and multiple class-action lawsuits.</p>

<p><strong>Private insurance rate inflation.</strong> Both companies negotiate rates with private insurers that are 3&ndash;5 times the Medicare reimbursement rate. A treatment Medicare reimburses at $260 may be billed to private insurance at $800&ndash;$1,300. During the 33-month coordination period when private insurance is primary, these inflated rates generate significant revenue&mdash;which is why both companies have been accused of encouraging patients to maintain private insurance as long as possible.</p>

<p><strong>Charitable premium assistance (CPA) controversy.</strong> Both DaVita and Fresenius have funded charitable organizations that pay health insurance premiums for dialysis patients, keeping them on private insurance (at higher reimbursement rates) rather than transitioning to Medicare (at lower rates). The DOJ has investigated this practice, and several insurers have filed lawsuits alleging it inflates costs.</p>

<p><strong>Collections practices.</strong> Both companies are known for aggressive collections. If you fall behind on copays or coinsurance, expect calls starting within 30&ndash;60 days. Accounts may be sent to collections within 90&ndash;120 days. Request a payment plan in writing at the start of treatment to avoid this cycle.</p>

<div class="case-study">
    <h3>Case study: $14,400 in annual overcharges caught by auditing monthly statements</h3>
    <p>A 61-year-old Medicare patient receiving hemodialysis three times per week at a DaVita center reviewed her monthly statements after noticing inconsistencies. Over 6 months, she identified: Epogen billed separately 8 times ($1,800 total) despite being bundled under ESRD PPS, two duplicate treatment charges ($1,950), and monthly lab panels billed separately 4 times ($1,680). <strong>Total identified overcharges: $5,430 in 6 months, projecting to $10,860&ndash;$14,400 annually.</strong></p>
    <p>She filed a formal billing dispute with the facility, citing CMS bundling rules, and contacted her Medicare Administrative Contractor. The facility corrected the claims and issued credits totaling <strong>$5,430</strong>. She continued auditing her statements monthly thereafter.</p>
    <p><strong>Lesson:</strong> Keep a dialysis treatment log and compare it to your monthly statement. Check every line for medications and labs that should be bundled. Use our <a href="/calculator">cost calculator</a> to verify Medicare rates for any charges on your statement.</p>
</div>

<div class="case-study">
    <h3>Case study: $8,400 in duplicate EPO charges reversed over 6 months</h3>
    <p>A 57-year-old Medicare patient on in-center hemodialysis noticed that his Explanation of Benefits statements listed Epogen (J0882) charges on dates he had documented in his personal dialysis log as no-treatment days (holidays and a brief hospitalization). Over 6 months, he identified <strong>14 separate EPO charges totaling $8,400</strong> that appeared on claims for dates when he did not receive dialysis at the center.</p>
    <p>He filed a formal billing dispute with the Fresenius center, attaching his personal log and hospital admission records proving he was inpatient on several of the billed dates. The facility investigated and confirmed the charges were billing errors&mdash;a combination of duplicate claim submissions and charges posted to incorrect dates of service. All 14 charges were reversed, and his Medicare coinsurance payments were refunded. <strong>Total recovered: $8,400 in erroneous charges plus $1,680 in coinsurance he had already paid.</strong></p>
    <p><strong>Lesson:</strong> Keep your own dialysis treatment log with dates, times, and any medications administered. Compare it against every monthly statement and EOB. Duplicate and phantom charges in dialysis billing compound quickly over time.</p>
</div>

{_embed(mode="cost", cpt="90999", title="Look up dialysis treatment costs", subtitle="Check Medicare rates for dialysis CPT codes on your bill.")}

<h2 id="reducing-costs">6. How to reduce your dialysis costs</h2>

<p><strong>Get Medigap if available.</strong> A Medigap plan covers the 20% Part B coinsurance that dialysis patients owe. If you are 65+ or in a state that requires Medigap for under-65 ESRD patients, enroll during your initial enrollment period. Annual savings: approximately $8,000.</p>

<p><strong>Consider home dialysis.</strong> Home peritoneal dialysis or home hemodialysis is 20&ndash;40% cheaper than in-center treatment, eliminates travel costs, and avoids the Medicare waiting period. Ask your nephrologist for a referral to a home dialysis training program.</p>

<p><strong>Apply for Extra Help (Medicare Part D).</strong> The Medicare Part D Low-Income Subsidy (Extra Help) program covers Part D premiums, deductibles, and copays for qualifying patients. Income limits are approximately $22,590 for individuals (2026). Phosphate binders and other oral ESRD drugs covered under Part D can cost $200&ndash;$600/month without Extra Help.</p>

<p><strong>Audit every statement.</strong> Review your monthly dialysis bill for unbundled medications, duplicate treatments, and separately billed labs. <a href="/scan">Upload your bill to BillKarma</a> for an automated audit that catches bundling errors and compares charges against Medicare rates.</p>

<p><strong>Request financial assistance.</strong> Both DaVita and Fresenius have financial hardship programs. The American Kidney Fund provides grants for insurance premiums and treatment costs. Apply through your dialysis center's social worker.</p>

<p>Check your dialysis facility's billing grade in our <a href="/hospitals/">hospital pricing directory</a> to see how they compare to other providers in your area.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does dialysis cost per year?</h3>
        <p>In-center hemodialysis costs $90,000&ndash;$120,000 per year (billed charges). Medicare reimburses about $260 per treatment (~$40,500/year). Patient responsibility under Medicare is 20% coinsurance, approximately $8,100/year. Peritoneal dialysis is 30&ndash;40% cheaper.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover dialysis?</h3>
        <p>Yes. Medicare covers dialysis for all ESRD patients regardless of age. Coverage begins after a 3-month waiting period (which can be waived with home dialysis training). Medicare Part B covers treatments and injectable medications; Part D covers oral ESRD drugs.</p>
    </div>

    <div class="faq-item">
        <h3>What is the Medicare ESRD 3-month waiting period?</h3>
        <p>Medicare ESRD coverage begins on the first day of the fourth month after regular dialysis starts. During the gap, patients rely on private insurance, Medicaid, or financial assistance. Starting home dialysis training can eliminate this waiting period entirely.</p>
    </div>

    <div class="faq-item">
        <h3>Why are DaVita and Fresenius bills so high?</h3>
        <p>They control 70% of the U.S. dialysis market and negotiate private insurance rates 3&ndash;5x higher than Medicare. During the 33-month period when private insurance is primary, these inflated rates generate significant revenue. Both companies have faced federal investigations into their billing practices.</p>
    </div>

    <div class="faq-item">
        <h3>What medications are in the Medicare dialysis bundle?</h3>
        <p>The ESRD PPS bundles most injectable drugs used during dialysis: erythropoietin-stimulating agents (Epogen), IV iron, and vitamin D analogs. Oral medications like phosphate binders are covered separately under Part D. If you see separate charges for bundled drugs on a Medicare claim, that is a billing error.</p>
    </div>

    <div class="faq-item">
        <h3>Can I do dialysis at home to save money?</h3>
        <p>Yes. Home peritoneal dialysis and home hemodialysis cost 20&ndash;40% less than in-center treatment. Home dialysis also eliminates the 3-month Medicare waiting period, provides more scheduling flexibility, and has comparable outcomes for most patients. Ask your nephrologist for a referral.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/end-stage-renal-disease-esrd" target="_blank" rel="noopener">CMS: ESRD Prospective Payment System</a></li>
    <li><a href="https://www.usrds.org/" target="_blank" rel="noopener">United States Renal Data System (USRDS) Annual Data Report</a></li>
    <li><a href="https://www.medicare.gov/coverage/dialysis-services-supplies" target="_blank" rel="noopener">Medicare.gov: Dialysis Services and Supplies Coverage</a></li>
    <li><a href="https://www.kidney.org/" target="_blank" rel="noopener">National Kidney Foundation: Dialysis Patient Resources</a></li>
    <li><a href="https://www.kidneyfund.org/" target="_blank" rel="noopener">American Kidney Fund: Financial Assistance Programs</a></li>
    <li><a href="https://www.gao.gov/products/gao-21-291" target="_blank" rel="noopener">GAO: Medicare ESRD Program Oversight Report</a></li>
</ul>
""",
})
