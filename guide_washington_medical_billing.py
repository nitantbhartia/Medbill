"""Guide: Washington State Medical Billing Laws."""

from guides import register, _embed

register("washington-state-medical-billing-laws", {
    "title": "Washington State Medical Billing Laws",
    "meta_description": "Washington has among the strongest surprise billing and charity care protections in the US. Learn your rights under the BBPA, WA Charity Care Act, and how to.",
    "published": "2026-02-28",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Does Washington's Balance Billing Protection Act cover ground ambulance bills?",
            "a": "Yes. Washington is one of the few states that explicitly extends surprise billing protections to ground ambulance services. Under the BBPA (SB 5526), if you are transported by an out-of-network ground ambulance in an emergency, you cannot be balance billed beyond your in-network cost-sharing amount. The ambulance provider must resolve the payment dispute directly with your insurer through the state's arbitration process. This is a rare and significant protection — most states and even the federal No Surprises Act do not cover ground ambulances.",
        },
        {
            "q": "What is the income limit for free charity care at Washington hospitals?",
            "a": "Under the Washington Charity Care Act (RCW 70.170), all hospitals in the state must provide free care to patients at or below 300% of the Federal Poverty Level (FPL) — approximately $46,950 for a single person or $96,450 for a family of four in 2026. Many Washington hospitals, including Providence, Swedish, and MultiCare systems, extend free care up to 300% FPL and sliding-scale discounts up to 400% FPL ($62,600 single / $128,600 family of four). You can apply retroactively, and hospitals must screen you for eligibility before pursuing collections.",
        },
        {
            "q": "What is Washington's statute of limitations on medical debt?",
            "a": "Washington has a 6-year statute of limitations on medical debt, measured from the date of the last payment or the date the debt became delinquent. After 6 years, the debt is time-barred and collectors cannot win a lawsuit. However, making any payment — even a small one — resets the clock. Washington also provides strong wage garnishment protections: 75% of disposable earnings are exempt, which is more protective than the federal minimum of 75%.",
        },
        {
            "q": "How do I file a complaint about a surprise medical bill in Washington?",
            "a": "Washington patients have two primary complaint channels. For insurance-related surprise billing disputes, file with the Washington Office of the Insurance Commissioner (OIC) at insurance.wa.gov — the OIC has enforcement authority and can order refunds. For broader hospital billing complaints or Consumer Protection Act violations, file with the Washington Attorney General's Consumer Protection Division at atg.wa.gov. For federal No Surprises Act violations, you can also file with CMS at 1-800-985-3059.",
        },
        {
            "q": "Does Washington's BBPA apply if I have a self-funded employer health plan?",
            "a": "Washington's BBPA directly covers state-regulated health plans (individual, small group, large group, and Apple Health managed care). Self-funded employer plans (ERISA plans) are primarily governed by the federal No Surprises Act, which provides similar but not identical protections. The key difference is that the federal NSA uses a different arbitration process (independent dispute resolution through CMS) rather than Washington's baseball-style arbitration. If you have a self-funded plan and receive a surprise bill, your protections come from the federal NSA, and you should file complaints with CMS rather than the WA OIC.",
        },
    ],
    "body": f"""
<p class="lead">Washington State has built one of the most comprehensive patient billing protection frameworks in the country. The Balance Billing Protection Act (SB 5526, effective 2020) was among the first state laws to ban surprise bills from out-of-network providers &mdash; and it remains one of the strongest, covering emergency services, non-emergency care at in-network facilities, <em>and</em> ground ambulance transport. Combined with the Washington Charity Care Act (RCW 70.170), which requires every hospital to provide free care to patients below 300% of the Federal Poverty Level, Washington patients have powerful tools to fight unfair medical bills. BillKarma&rsquo;s analysis of 100+ Washington hospitals found that the median markup over Medicare across the state is 3.7&times; &mdash; yet fewer than 1 in 5 eligible patients applied for charity care in 2025. This guide explains every protection available to you and how to use them.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#bbpa">WA Balance Billing Protection Act (BBPA)</a></li>
        <li><a href="#charity-care">WA Charity Care Act (RCW 70.170)</a></li>
        <li><a href="#medical-debt">WA medical debt protections</a></li>
        <li><a href="#apple-health">Apple Health (WA Medicaid)</a></li>
        <li><a href="#pricing-transparency">WA hospital pricing and transparency</a></li>
        <li><a href="#insurance-protections">WA insurance protections</a></li>
        <li><a href="#how-to-dispute">How to dispute a WA hospital bill</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="bbpa">1. WA Balance Billing Protection Act (BBPA)</h2>

<p>Washington&rsquo;s Balance Billing Protection Act (BBPA), enacted as SB 5526 in 2019 and effective January 1, 2020, was one of the first and most comprehensive state surprise billing laws in the nation. It predates the federal No Surprises Act (NSA) by two years and in several respects provides <strong>broader protections</strong> than federal law.</p>

<p>Key provisions of the BBPA:</p>

<ul>
    <li><strong>Emergency services:</strong> Out-of-network providers at any emergency facility cannot balance bill you. You pay only your in-network cost-sharing amount (deductible, copay, coinsurance), regardless of whether the provider or facility is in your plan&rsquo;s network.</li>
    <li><strong>Non-emergency services at in-network facilities:</strong> If you receive care at an in-network hospital or surgical center and an out-of-network provider (anesthesiologist, radiologist, pathologist, neonatologist, or assistant surgeon) treats you, that provider <strong>cannot balance bill you</strong>. You owe only your in-network cost-sharing.</li>
    <li><strong>Ground ambulance transport:</strong> Washington is one of the <strong>few states</strong> that extends surprise billing protections to ground ambulance services. Out-of-network ground ambulance providers cannot balance bill you for emergency transport. This is a rare protection &mdash; the federal No Surprises Act explicitly excludes ground ambulances.</li>
    <li><strong>Baseball-style arbitration:</strong> When the provider and insurer cannot agree on a payment amount, the dispute goes to binding &ldquo;baseball-style&rdquo; arbitration. Each side submits a final offer, and the arbitrator selects one &mdash; no splitting the difference. This incentivizes both sides to propose reasonable amounts.</li>
    <li><strong>Consent requirements:</strong> An out-of-network provider at an in-network facility can only balance bill you for non-emergency services if they provide written notice of their OON status <strong>at least 72 hours before the service</strong> and you sign a consent form agreeing to waive your BBPA protections.</li>
</ul>

<div class="key-takeaway">
    <strong>Washington&rsquo;s BBPA covers ground ambulances &mdash; most states don&rsquo;t.</strong> If you received an emergency ground ambulance bill in Washington from an out-of-network provider, you are protected. You owe only your in-network cost-sharing. <a href="/scan">Upload your ambulance bill to BillKarma</a> to check for balance billing violations and generate a dispute letter.
</div>

<h3>BBPA vs. federal No Surprises Act</h3>

<p>Since January 1, 2022, the federal No Surprises Act also protects patients from surprise bills. Both laws apply simultaneously in Washington, and patients receive the <strong>stronger of the two protections</strong> for any given situation. Here is how they compare:</p>

<table>
    <thead>
        <tr><th>Protection</th><th>WA BBPA (SB 5526)</th><th>Federal No Surprises Act</th></tr>
    </thead>
    <tbody>
        <tr><td>Emergency services</td><td>Covered &mdash; OON balance billing banned</td><td>Covered &mdash; OON balance billing banned</td></tr>
        <tr><td>Non-emergency OON at in-network facility</td><td>Covered &mdash; OON balance billing banned</td><td>Covered &mdash; OON balance billing banned</td></tr>
        <tr><td>Ground ambulance (emergency)</td><td><strong>Covered</strong> &mdash; OON balance billing banned</td><td><strong>Not covered</strong></td></tr>
        <tr><td>Air ambulance</td><td>Not explicitly covered by BBPA</td><td>Covered &mdash; OON balance billing banned</td></tr>
        <tr><td>Arbitration process</td><td>Baseball-style (single final offer selected)</td><td>Independent dispute resolution (IDR) via CMS</td></tr>
        <tr><td>Self-funded (ERISA) plans</td><td>Not covered (state law limitation)</td><td><strong>Covered</strong></td></tr>
        <tr><td>Consent to waive protections</td><td>72-hour advance written notice + signed consent</td><td>72-hour advance written notice + signed consent</td></tr>
        <tr><td>Enforcement agency</td><td>WA Office of the Insurance Commissioner (OIC)</td><td>CMS / HHS</td></tr>
    </tbody>
</table>

<p><em>In practice, Washington patients with state-regulated plans receive BBPA protections (including ground ambulance coverage). Patients with self-funded employer plans receive federal NSA protections. Both groups are shielded from most surprise bills.</em></p>

<h2 id="charity-care">2. WA Charity Care Act (RCW 70.170)</h2>

<p>Washington&rsquo;s Charity Care Act is one of the most protective hospital financial assistance laws in the country. Under RCW 70.170, <strong>every hospital in Washington</strong> &mdash; nonprofit and for-profit alike &mdash; must provide charity care to eligible patients. The Washington State Department of Health sets minimum income thresholds, and many hospital systems exceed them.</p>

<p>Key provisions:</p>

<ul>
    <li><strong>Free care at or below 300% FPL.</strong> Washington law requires hospitals to provide 100% free care to patients whose household income is at or below 300% of the Federal Poverty Level.</li>
    <li><strong>Sliding-scale discounts up to 400% FPL.</strong> Patients between 300% and 400% FPL qualify for discounts on a sliding scale. Many hospitals offer 75% discounts at 350% FPL and 50% at 400% FPL.</li>
    <li><strong>Applies to all hospitals.</strong> Unlike the federal IRS 501(r) rules that only cover nonprofit hospitals, Washington&rsquo;s Charity Care Act applies to every licensed hospital in the state.</li>
    <li><strong>Public reporting.</strong> Every Washington hospital must report its charity care amounts to the Department of Health annually. This data is publicly available, making it possible to compare hospitals&rsquo; charity care generosity.</li>
    <li><strong>Retroactive applications accepted.</strong> You can apply for charity care after receiving your bill &mdash; and even after making partial payments.</li>
    <li><strong>Screening before collections.</strong> Hospitals must screen patients for charity care eligibility before referring accounts to collections.</li>
</ul>

<table>
    <thead>
        <tr><th>Household Size</th><th>100% FPL (2026)</th><th>300% FPL (free care)</th><th>400% FPL (max for discount)</th></tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$15,650</td><td>$46,950</td><td>$62,600</td></tr>
        <tr><td>2 people</td><td>$21,150</td><td>$63,450</td><td>$84,600</td></tr>
        <tr><td>3 people</td><td>$26,650</td><td>$79,950</td><td>$106,600</td></tr>
        <tr><td>4 people</td><td>$32,150</td><td>$96,450</td><td>$128,600</td></tr>
        <tr><td>5 people</td><td>$37,650</td><td>$112,950</td><td>$150,600</td></tr>
    </tbody>
</table>

<p><em>Note: FPL figures are updated annually each February by HHS. The numbers above reflect the 2026 federal poverty guidelines. Confirm current thresholds at <a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">aspe.hhs.gov</a> before applying.</em></p>

<div class="key-takeaway">
    <strong>Washington&rsquo;s charity care income threshold is higher than most states.</strong> Free care at 300% FPL means a single person earning up to $46,950 or a family of four earning up to $96,450 qualifies for a <strong>100% write-off</strong>. Check if you qualify using our <a href="/charity-care">charity care eligibility guide</a>, then look up your hospital&rsquo;s charity care record in our <a href="/hospitals/">hospital directory</a>.
</div>

{_embed(mode="markup", title="Compare your Washington hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup over Medicare.", height="420")}

<h2 id="medical-debt">3. WA medical debt protections</h2>

<p>Washington provides a robust set of protections for patients facing medical debt, combining a strong Consumer Protection Act with protective garnishment rules and hospital-specific collection restrictions.</p>

<h3>Statute of limitations</h3>

<p>Washington&rsquo;s statute of limitations on medical debt is <strong>6 years</strong> (RCW 4.16.040), measured from the date of the last payment or the date the debt became delinquent. After 6 years, the debt is time-barred and a collector cannot win a lawsuit to collect it. However, be aware that any payment &mdash; even a small one &mdash; resets the 6-year clock. For more details, see our <a href="/statute-of-limitations">statute of limitations guide</a>.</p>

<h3>Wage garnishment protections</h3>

<p>Washington State provides some of the most protective wage garnishment rules in the country. Under RCW 6.27, <strong>75% of disposable earnings are exempt from garnishment</strong>. This means a creditor with a court judgment can garnish only 25% of your disposable earnings &mdash; and even that amount is further limited if your earnings are below a threshold tied to the federal minimum wage. This 75% exemption is more generous than the federal minimum (also 75%, but Washington&rsquo;s calculation is often more favorable due to the state&rsquo;s higher minimum wage).</p>

<h3>WA Consumer Protection Act (RCW 19.86)</h3>

<p>Washington&rsquo;s Consumer Protection Act is considered one of the strongest consumer protection statutes in the US. Unlike many states, WA&rsquo;s CPA does not require proof of intent to deceive &mdash; unfair or deceptive practices are sufficient. The Washington Attorney General has used the CPA aggressively to pursue hospitals and collections agencies engaged in improper billing and collections practices. Key CPA protections for medical debt:</p>

<ul>
    <li><strong>Deceptive billing practices are actionable.</strong> Billing for services not rendered, upcoding, and charging significantly more than disclosed are potential CPA violations.</li>
    <li><strong>Aggressive collection tactics are actionable.</strong> Threats, harassment, and collecting debts you do not owe violate the CPA.</li>
    <li><strong>Private right of action.</strong> Patients can sue under the CPA and recover actual damages, attorneys&rsquo; fees, and costs &mdash; a meaningful deterrent for bad actors.</li>
    <li><strong>AG enforcement.</strong> The Washington Attorney General&rsquo;s office actively investigates and sues medical providers engaged in unfair billing. Recent enforcement actions have resulted in multi-million-dollar settlements with hospitals and debt collection agencies.</li>
</ul>

<h3>Medical debt interest caps</h3>

<p>Washington limits prejudgment interest on medical debt to <strong>12% per year</strong> (RCW 19.52.010). Post-judgment interest is set at 12% or 2 percentage points above the federal discount rate, whichever is greater. Some hospital payment plans may charge lower or zero interest &mdash; always negotiate this before agreeing to a plan.</p>

<h3>Limits on hospital collections</h3>

<p>Under WAC 246-453, Washington hospitals face specific restrictions on collections activity:</p>

<ul>
    <li>Hospitals must make reasonable efforts to determine whether a patient qualifies for charity care <strong>before</strong> pursuing collections.</li>
    <li>Hospitals must provide written notice of charity care availability and application instructions.</li>
    <li>If a patient applies for charity care, the hospital must suspend collection activity until the application is reviewed and a determination is made.</li>
</ul>

<h2 id="apple-health">4. Apple Health (WA Medicaid)</h2>

<p>Apple Health is Washington&rsquo;s Medicaid program, administered by the Washington Health Care Authority (HCA). It provides comprehensive health coverage to low-income residents and has some of the broadest eligibility criteria in the nation.</p>

<h3>Eligibility</h3>

<ul>
    <li><strong>Adults:</strong> Up to 138% FPL ($21,597 single / $44,367 family of four in 2026) under the ACA Medicaid expansion.</li>
    <li><strong>Children (Apple Health for Kids):</strong> Up to 312% FPL ($48,828 single child household) under Cover All Kids.</li>
    <li><strong>Pregnant individuals:</strong> Up to 193% FPL with coverage through 12 months postpartum.</li>
</ul>

<h3>Cover All Kids and Cover All People</h3>

<p>Washington has been a national leader in expanding health coverage regardless of immigration status:</p>

<ul>
    <li><strong>Cover All Kids (2023):</strong> Provides Apple Health coverage to all children under 19 in Washington regardless of immigration status, as long as they meet income requirements. This was one of the first such programs in the country.</li>
    <li><strong>Cover All People:</strong> Washington has been phasing in Apple Health coverage for adults regardless of immigration status. As of 2024, adults ages 19&ndash;25 are covered. The state continues to expand eligibility to additional age groups.</li>
</ul>

<h3>Retroactive coverage</h3>

<p>Apple Health provides <strong>up to 3 months of retroactive coverage</strong> from the date of your application. If you received medical care in the 3 months before you applied and are found eligible, Apple Health will cover those services. This is critical for patients who arrive at the ER without insurance and then apply. To claim retroactive coverage, submit your application as soon as possible and provide the dates of service to HCA.</p>

<h3>Impact on hospital billing</h3>

<p>If you qualify for Apple Health, your hospital bill should be covered at Medicaid rates, which are significantly lower than commercial rates. Hospitals cannot bill Apple Health patients for the difference between their chargemaster price and the Medicaid reimbursement rate. If you receive a bill for a service that should be covered by Apple Health, contact HCA directly at 1-800-562-3022.</p>

<h2 id="pricing-transparency">5. WA hospital pricing and transparency</h2>

<p>Washington has invested in hospital pricing transparency through several state-specific initiatives that go beyond the federal requirements.</p>

<h3>WA Health Care Authority cost data</h3>

<p>The Washington Health Care Authority (HCA) publishes claims data, provider reimbursement rates, and cost benchmarks that patients and researchers can access. This data covers both Apple Health (Medicaid) and state employee plans, providing a baseline for what the state considers a fair price for medical services.</p>

<h3>Health Care Cost Analysis Initiative (HCAI)</h3>

<p>Washington&rsquo;s HCAI program, run by the Department of Health, collects detailed discharge and claims data from all Washington hospitals. This data powers publicly available tools that allow patients to compare costs across hospitals for common procedures. The HCAI data includes:</p>

<ul>
    <li>Average charges by diagnosis and procedure</li>
    <li>Length-of-stay statistics</li>
    <li>Payer mix (how much each hospital relies on Medicare, Medicaid, and commercial insurance)</li>
    <li>Charity care amounts provided by each hospital</li>
</ul>

<h3>Federal price transparency compliance</h3>

<p>Under the federal Hospital Price Transparency Rule (effective 2021), all Washington hospitals must publish machine-readable files containing their negotiated rates with every insurer. Compliance among Washington hospitals has been uneven &mdash; CMS enforcement has increased, but many hospitals still publish incomplete or difficult-to-use files. BillKarma&rsquo;s <a href="/hospitals/">hospital directory</a> makes this data accessible by comparing each hospital&rsquo;s charges to Medicare benchmarks for common procedures.</p>

<h2 id="insurance-protections">6. WA insurance protections</h2>

<p>Washington&rsquo;s Office of the Insurance Commissioner (OIC) provides strong regulatory oversight of health insurance plans sold in the state.</p>

<h3>Office of the Insurance Commissioner (OIC)</h3>

<p>The OIC is Washington&rsquo;s primary insurance regulator. It has enforcement authority over all state-regulated health plans (individual, small group, and large group plans). The OIC can:</p>

<ul>
    <li>Investigate billing complaints and order refunds</li>
    <li>Enforce the BBPA against insurers and providers</li>
    <li>Review and approve health insurance rate increases</li>
    <li>Mandate corrective actions for insurers that violate state law</li>
</ul>

<h3>External review</h3>

<p>Washington law gives patients the right to an <strong>independent external review</strong> of any insurance claim denial. If your insurer denies a claim or authorizes less than the full amount, you can request an external review by an independent review organization (IRO). The IRO&rsquo;s decision is binding on the insurer. To request an external review, file through the OIC at <a href="https://www.insurance.wa.gov/" target="_blank" rel="noopener">insurance.wa.gov</a> or call 1-800-562-6900.</p>

<h3>Network adequacy</h3>

<p>The OIC requires health plans to maintain adequate provider networks. If your plan does not have an in-network specialist within a reasonable distance or wait time, the plan must cover out-of-network care at in-network cost-sharing levels. This is an important protection for patients in rural areas of Washington.</p>

<h3>Individual coverage mandate</h3>

<p>While Washington does not have a state-level individual mandate like California or Massachusetts, the state does operate Washington Healthplanfinder (wahealthplanfinder.org), which offers subsidized marketplace plans and automatic enrollment pathways for Apple Health. Open enrollment for 2026 plans ran from November 1, 2025, through January 15, 2026, with special enrollment periods available for qualifying life events.</p>

<h2 id="how-to-dispute">7. How to dispute a WA hospital bill</h2>

<h3>Step 1: Request an itemized bill</h3>

<p>Contact the hospital billing department and request a full itemized statement with CPT codes, revenue codes, quantities, and unit prices for every charge. Washington hospitals are required to provide this upon request. Get the request in writing (email is fine) so you have a dated record.</p>

<h3>Step 2: Compare charges to Medicare rates</h3>

<p>Look up each CPT code on your bill using our <a href="/calculator">free calculator</a>. If any charge exceeds 3&ndash;5&times; the Medicare rate, that is a significant red flag and strong basis for a dispute. BillKarma&rsquo;s analysis shows Washington hospitals charge a median of 3.7&times; Medicare, but some line items can be 8&ndash;12&times; Medicare rates.</p>

<h3>Step 3: Check for BBPA violations</h3>

<p>Review each provider on your bill. If any out-of-network provider treated you at an in-network facility or during an emergency, the balance bill is likely illegal under the BBPA. <a href="/scan">Upload your bill to BillKarma</a> to automatically detect BBPA and No Surprises Act violations.</p>

<h3>Step 4: Apply for charity care</h3>

<p>If your household income is below 400% FPL, request a charity care application from the hospital. Under RCW 70.170, they must provide one. Submit the application with proof of income (pay stubs, tax return, or a signed affidavit). The hospital must suspend collections while your application is pending. For more details, see our <a href="/charity-care">charity care guide</a>.</p>

<h3>Step 5: File a written dispute</h3>

<p>Send a formal dispute letter to the hospital billing department by certified mail. Include your account number, dates of service, the specific line items you dispute, the reason for each dispute, and supporting documentation (Medicare rate comparisons, medical records, EOB from your insurer).</p>

<h3>Step 6: Escalate to regulators if needed</h3>

<ul>
    <li><strong>Surprise billing / insurance disputes:</strong> File a complaint with the <a href="https://www.insurance.wa.gov/file-complaint-or-check-your-complaint-status" target="_blank" rel="noopener">WA Office of the Insurance Commissioner</a> (1-800-562-6900).</li>
    <li><strong>Unfair billing practices:</strong> File a complaint with the <a href="https://www.atg.wa.gov/file-complaint" target="_blank" rel="noopener">WA Attorney General&rsquo;s Consumer Protection Division</a> (1-800-551-4636).</li>
    <li><strong>Charity care denial:</strong> Contact the <a href="https://doh.wa.gov/data-and-statistical-reports/healthcare-washington/hospital-and-patient-data/hospital-financial-data" target="_blank" rel="noopener">WA Department of Health</a> hospital financial data program.</li>
    <li><strong>Federal No Surprises Act violations:</strong> File with the <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS No Surprises Help Desk</a> (1-800-985-3059).</li>
</ul>

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Case study 1: $7,400 ER anesthesiology balance bill eliminated via BBPA arbitration &mdash; Seattle</h3>
    <p><strong>Situation:</strong> A Seattle patient underwent emergency surgery for a ruptured appendix at an in-network hospital. The surgeon and facility were in-network, but the anesthesiologist was out-of-network. The patient received a $9,200 anesthesiology bill, of which insurance paid $1,800, leaving a $7,400 balance bill.</p>
    <p><strong>Action:</strong> The patient filed a complaint with the WA OIC, citing the Balance Billing Protection Act. Because the anesthesiologist provided services at an in-network facility during an emergency, the BBPA prohibited any balance billing. The dispute went to baseball-style arbitration: the insurer offered $3,400 (the median in-network rate) and the anesthesiologist&rsquo;s group submitted $6,100. The arbitrator selected the insurer&rsquo;s offer of $3,400 as the more reasonable amount.</p>
    <p><strong>Result:</strong> The patient&rsquo;s liability was capped at their in-network copay of $250. The $7,400 balance bill was eliminated entirely. The anesthesiologist&rsquo;s group received $3,400 total from the insurer (an additional $1,600 beyond the initial payment).</p>
    <p><strong>Savings: $7,150.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 2: $32,000 hospital bill written off under charity care at Providence &mdash; Spokane</h3>
    <p><strong>Situation:</strong> A single mother in Spokane was hospitalized for 4 days with pneumonia. She was uninsured at the time and received a $32,000 bill from Providence Sacred Heart Medical Center. Her annual household income was $41,000 (family of 2), which placed her at approximately 194% of FPL &mdash; well below the 300% FPL threshold for free charity care in Washington.</p>
    <p><strong>Action:</strong> The patient contacted Providence&rsquo;s financial counseling department and submitted a charity care application with her two most recent pay stubs and a signed income affidavit. Providence confirmed her eligibility within 3 weeks.</p>
    <p><strong>Result:</strong> The entire $32,000 bill was written off as charity care under RCW 70.170. Providence also retroactively applied charity care to a $1,800 outpatient radiology bill from 6 weeks prior. The patient owed $0.</p>
    <p><strong>Savings: $33,800.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 3: Apple Health retroactive coverage saved $14,500 after ER visit &mdash; Tacoma</h3>
    <p><strong>Situation:</strong> A 24-year-old Tacoma resident visited the ER for severe abdominal pain and was admitted for 2 days. He had no insurance at the time and received a combined bill of $14,500 from the hospital and treating physicians. His annual income was $19,000, putting him below the Apple Health eligibility threshold of 138% FPL.</p>
    <p><strong>Action:</strong> A hospital social worker helped him apply for Apple Health within a week of discharge. Because Apple Health provides up to 3 months of retroactive coverage, his ER visit and hospitalization (which occurred within that window) were eligible for coverage.</p>
    <p><strong>Result:</strong> Apple Health approved his application and covered the hospitalization retroactively at Medicaid rates. The hospital accepted the Medicaid reimbursement as payment in full. The patient&rsquo;s out-of-pocket cost was $0.</p>
    <p><strong>Savings: $14,500.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Washington&rsquo;s Balance Billing Protection Act cover ground ambulance bills?</h3>
        <p>Yes. Washington is one of the few states that extends surprise billing protections to ground ambulance services. Under the BBPA, if you are transported by an out-of-network ground ambulance in an emergency, you cannot be balance billed beyond your in-network cost-sharing amount. The ambulance provider must resolve the payment dispute directly with your insurer through the state&rsquo;s arbitration process. This protection does not exist under the federal No Surprises Act, making Washington&rsquo;s law meaningfully stronger for ambulance patients.</p>
    </div>

    <div class="faq-item">
        <h3>What is the income limit for free charity care at Washington hospitals?</h3>
        <p>Under the Washington Charity Care Act (RCW 70.170), all hospitals must provide free care to patients at or below 300% of the Federal Poverty Level &mdash; approximately $46,950 for a single person or $96,450 for a family of four in 2026. Patients between 300% and 400% FPL qualify for sliding-scale discounts. Many major Washington hospital systems (Providence, Swedish, MultiCare) offer discounts at or above these thresholds. You can apply retroactively, and the hospital must screen for eligibility before pursuing collections.</p>
    </div>

    <div class="faq-item">
        <h3>What is Washington&rsquo;s statute of limitations on medical debt?</h3>
        <p>Washington has a 6-year statute of limitations on medical debt (RCW 4.16.040). The clock starts from the date of your last payment or the date the account became delinquent. After 6 years, the debt is time-barred and collectors cannot successfully sue you. Be careful: any payment, even a small one, resets the 6-year clock. Washington also exempts 75% of disposable earnings from wage garnishment, providing additional protection if a creditor obtains a judgment.</p>
    </div>

    <div class="faq-item">
        <h3>How do I file a complaint about a surprise medical bill in Washington?</h3>
        <p>For insurance-related surprise billing disputes, file a complaint with the <a href="https://www.insurance.wa.gov/file-complaint-or-check-your-complaint-status" target="_blank" rel="noopener">Washington Office of the Insurance Commissioner (OIC)</a> at 1-800-562-6900. The OIC has enforcement authority and can order refunds. For broader billing abuses, contact the <a href="https://www.atg.wa.gov/file-complaint" target="_blank" rel="noopener">WA Attorney General&rsquo;s Consumer Protection Division</a> at 1-800-551-4636. For federal No Surprises Act violations, file with CMS at 1-800-985-3059.</p>
    </div>

    <div class="faq-item">
        <h3>Does Washington&rsquo;s BBPA apply if I have a self-funded employer health plan?</h3>
        <p>No. Washington&rsquo;s BBPA covers state-regulated health plans only (individual, small group, large group, Apple Health managed care). Self-funded employer plans (ERISA plans) are governed by the federal No Surprises Act, which provides similar but not identical protections. The key difference: the federal NSA does not cover ground ambulances, and it uses a different arbitration process (CMS independent dispute resolution). If you have a self-funded plan and receive a surprise bill, file your complaint with CMS rather than the WA OIC.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://app.leg.wa.gov/billsummary?BillNumber=5526&Year=2019&Initiative=false" target="_blank" rel="noopener">Washington SB 5526 (2019): Balance Billing Protection Act</a></li>
    <li><a href="https://app.leg.wa.gov/RCW/default.aspx?cite=70.170" target="_blank" rel="noopener">RCW 70.170: Washington Charity Care Act</a></li>
    <li><a href="https://app.leg.wa.gov/RCW/default.aspx?cite=19.86" target="_blank" rel="noopener">RCW 19.86: Washington Consumer Protection Act</a></li>
    <li><a href="https://app.leg.wa.gov/RCW/default.aspx?cite=6.27" target="_blank" rel="noopener">RCW 6.27: Washington Wage Garnishment Exemptions</a></li>
    <li><a href="https://www.insurance.wa.gov/what-you-need-know-about-balance-billing-protection-act" target="_blank" rel="noopener">WA Office of the Insurance Commissioner: Balance Billing Protection Act</a></li>
    <li><a href="https://www.insurance.wa.gov/file-complaint-or-check-your-complaint-status" target="_blank" rel="noopener">WA OIC: File a Complaint</a></li>
    <li><a href="https://www.hca.wa.gov/free-or-low-cost-health-care/apple-health-medicaid-coverage" target="_blank" rel="noopener">Washington Health Care Authority: Apple Health (Medicaid)</a></li>
    <li><a href="https://doh.wa.gov/data-and-statistical-reports/healthcare-washington/hospital-and-patient-data/hospital-financial-data" target="_blank" rel="noopener">WA Department of Health: Hospital Financial Data and Charity Care Reports</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Patient Rights</a></li>
    <li><a href="https://www.atg.wa.gov/consumer-protection" target="_blank" rel="noopener">WA Attorney General: Consumer Protection Division</a></li>
</ul>
""",
})
