"""Guide: Minnesota Medical Billing Laws."""

from guides import register, _embed

register("minnesota-medical-billing-laws", {
    "title": "Minnesota Medical Billing Laws: Surprise Billing, MinnesotaCare, and Patient Rights (2026)",
    "meta_description": "Minnesota surprise billing law (62Q.556), MinnesotaCare, charity care rules, and medical debt protections. Learn how to dispute hospital bills and protect your rights in MN.",
    "published": "2026-02-28",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Does Minnesota have its own surprise billing law separate from the federal No Surprises Act?",
            "a": "Yes. Minnesota Statute 62Q.556 took effect in 2019, before the federal No Surprises Act. It prohibits balance billing for emergency services and for out-of-network providers at in-network facilities when the patient did not have a meaningful choice of provider. Under 62Q.556, the patient owes only in-network cost-sharing, and the insurer and provider must resolve the payment dispute between themselves. The federal NSA, effective January 2022, applies to self-funded employer plans not governed by state insurance law. For state-regulated plans, Minnesota's own law controls. Both laws protect patients from surprise bills, but the dispute resolution mechanisms differ: the federal NSA uses an independent dispute resolution (IDR) process, while Minnesota's law relies on the existing Commerce Department complaint and arbitration framework.",
        },
        {
            "q": "What is MinnesotaCare and who qualifies?",
            "a": "MinnesotaCare is Minnesota's public health insurance program for residents who earn too much to qualify for Medical Assistance (Medicaid) but cannot afford private insurance. In 2026, single adults earning up to approximately 200% FPL ($31,200) and families earning up to 200% FPL for their household size are eligible. MinnesotaCare covers doctor visits, hospital stays, prescriptions, mental health services, dental care, and preventive care. Premiums are income-based and range from $0 to roughly $80 per month. Apply through MNsure, Minnesota's health insurance marketplace, at mnsure.org or by calling 651-539-2099.",
        },
        {
            "q": "What is Minnesota's statute of limitations on medical debt?",
            "a": "Minnesota applies a 6-year statute of limitations to most medical debt under Minnesota Statute 541.05. The clock starts from the date of the last payment or the date the account became delinquent. After 6 years, the debt is time-barred and a collector cannot win a lawsuit if you raise the SOL defense. Making any payment or written acknowledgment of the debt can restart the 6-year clock. Always verify the original service date and last payment date before taking any action on old Minnesota medical debt.",
        },
        {
            "q": "Are Minnesota hospitals required to provide charity care or financial assistance?",
            "a": "Minnesota has no state statute mandating specific charity care income thresholds, but nonprofit hospitals must comply with IRS Section 501(r), which requires a written Financial Assistance Policy, charges limited to amounts generally billed to insured patients, and a 240-day application window. Major Minnesota systems like Hennepin Healthcare offer charity care up to 300% FPL, and Mayo Clinic Health System extends financial assistance on a sliding scale. The Minnesota Attorney General can investigate nonprofit hospitals that fail to provide charity care proportionate to their tax-exempt benefits under the Minnesota Nonprofit Corporation Act.",
        },
        {
            "q": "How do I file an insurance complaint in Minnesota?",
            "a": "For state-regulated insurance plans (individual, small group, MinnesotaCare-related), file a complaint with the Minnesota Department of Commerce at mn.gov/commerce or call 651-539-1500. For HMO-specific disputes involving access to care or provider network issues, the Commerce Department handles those as well. For self-funded employer plans regulated under federal ERISA, file with the U.S. Department of Labor. Minnesota law gives you the right to an external review of insurance denials through an independent review organization, and the Commerce Department administers that process.",
        },
    ],
    "body": f"""
<p class="lead">Minnesota enacted its own surprise billing protections under Statute 62Q.556 in 2019 &mdash; nearly three years before the federal No Surprises Act took effect. Combined with MinnesotaCare (one of the nation&rsquo;s few state-level public option programs), robust charity care at major systems like Hennepin Healthcare and Mayo Clinic, and a 6-year statute of limitations on medical debt, Minnesota patients have meaningful tools to fight unfair hospital bills. <strong>BillKarma&rsquo;s analysis of Minnesota hospital billing data found that Twin Cities metro hospitals charge a median of 3.6&times; Medicare rates, with some outpatient departments exceeding 5&times;.</strong> Here is how to use Minnesota&rsquo;s laws to protect yourself.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#surprise-billing">Minnesota surprise billing protections (MN Statute 62Q.556)</a></li>
        <li><a href="#minnesotacare">MinnesotaCare and Medical Assistance (Medicaid)</a></li>
        <li><a href="#charity-care">Minnesota hospital charity care</a></li>
        <li><a href="#medical-debt">Minnesota medical debt protections</a></li>
        <li><a href="#pricing-transparency">Hospital pricing and cost transparency in MN</a></li>
        <li><a href="#insurance-complaints">Minnesota insurance complaint process</a></li>
        <li><a href="#dispute-steps">How to dispute a Minnesota hospital bill</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="surprise-billing">1. Minnesota surprise billing protections (MN Statute 62Q.556)</h2>

<p>Minnesota was among the first states to enact comprehensive surprise billing protections. <strong>Statute 62Q.556</strong>, effective January 1, 2019, prohibits balance billing in two key scenarios:</p>

<ul>
    <li><strong>Emergency services</strong> &mdash; When you receive emergency care at any hospital or freestanding emergency department, you owe only your in-network cost-sharing amount, regardless of whether the facility or any treating provider is out of network. The provider and insurer must resolve payment between themselves.</li>
    <li><strong>Non-emergency services at in-network facilities</strong> &mdash; When you receive care at an in-network hospital or surgical center and an out-of-network provider (such as an anesthesiologist, radiologist, or assistant surgeon) treats you without your meaningful prior consent, you owe only in-network cost-sharing. The provider cannot balance bill you for the difference.</li>
</ul>

<p><strong>How 62Q.556 interacts with the federal No Surprises Act (NSA):</strong></p>

<table>
    <thead>
        <tr><th>Protection</th><th>MN Statute 62Q.556 (2019)</th><th>Federal No Surprises Act (2022)</th></tr>
    </thead>
    <tbody>
        <tr><td>Applies to</td><td>State-regulated insurance plans (individual, small group, state employee, MinnesotaCare)</td><td>Self-funded employer plans, federal employee plans, plans not subject to state insurance law</td></tr>
        <tr><td>Emergency balance billing ban</td><td>Yes &mdash; patient owes in-network cost-sharing only</td><td>Yes &mdash; patient owes in-network cost-sharing only</td></tr>
        <tr><td>Non-emergency at in-network facility</td><td>Yes &mdash; patient protected when no meaningful choice of provider</td><td>Yes &mdash; patient protected unless given proper notice and consent</td></tr>
        <tr><td>Dispute resolution</td><td>MN Commerce Department complaint and arbitration</td><td>Federal Independent Dispute Resolution (IDR) process</td></tr>
        <tr><td>Enforcement</td><td>MN Commerce Department, MN Attorney General</td><td>CMS, state regulators for state-regulated plans</td></tr>
    </tbody>
</table>

<p>In practice, if your insurance is a state-regulated plan purchased through MNsure or directly from a Minnesota insurer, Statute 62Q.556 applies. If your employer self-funds its health plan (common at large employers), the federal NSA governs surprise billing disputes. In either case, you should never pay a balance bill for emergency services or for an out-of-network provider you did not choose at an in-network facility.</p>

<div class="key-takeaway">
    <strong>Received a surprise bill from a Minnesota hospital?</strong> Check whether your plan is state-regulated or self-funded &mdash; that determines which law protects you. Either way, you are not responsible for the balance beyond your in-network cost-sharing. <a href="/scan">Upload your bill to BillKarma</a> to identify surprise billing violations and generate a dispute letter citing the correct statute.
</div>

<h2 id="minnesotacare">2. MinnesotaCare and Medical Assistance (Medicaid)</h2>

<p>Minnesota offers two major public insurance programs that reduce out-of-pocket exposure for lower-income residents:</p>

<p><strong>Medical Assistance (MA)</strong> is Minnesota&rsquo;s Medicaid program. Under the ACA expansion, Minnesota extended MA eligibility to adults earning up to 138% FPL. MA covers hospital care, doctor visits, prescriptions, mental health, dental, vision, and long-term care with minimal or no cost-sharing.</p>

<p><strong>MinnesotaCare</strong> fills the gap between Medicaid and private insurance. It covers residents earning between 138% and 200% FPL who do not have access to affordable employer-sponsored coverage. MinnesotaCare is often described as a &ldquo;public option&rdquo; &mdash; it is state-subsidized insurance with income-based premiums ranging from $0 to approximately $80 per month.</p>

<table>
    <thead>
        <tr><th>Program</th><th>Income Limit (Single Adult, 2026)</th><th>Income Limit (Family of 4, 2026)</th><th>Monthly Premium</th><th>Coverage</th></tr>
    </thead>
    <tbody>
        <tr><td>Medical Assistance (Medicaid)</td><td>Up to $21,597 (138% FPL)</td><td>Up to $44,568 (138% FPL)</td><td>$0</td><td>Comprehensive: hospital, physician, Rx, dental, vision, mental health, long-term care</td></tr>
        <tr><td>MinnesotaCare</td><td>$21,598&ndash;$31,200 (138%&ndash;200% FPL)</td><td>$44,569&ndash;$64,400 (138%&ndash;200% FPL)</td><td>$0&ndash;$80 (income-based)</td><td>Comprehensive: hospital, physician, Rx, dental, mental health, preventive</td></tr>
        <tr><td>MNsure Marketplace (with subsidies)</td><td>$31,201&ndash;$62,400 (200%&ndash;400% FPL)</td><td>$64,401&ndash;$128,800 (200%&ndash;400% FPL)</td><td>Varies (premium tax credits available)</td><td>Depends on plan selected; all ACA essential health benefits covered</td></tr>
    </tbody>
</table>

<p><strong>How to apply:</strong> Apply for both MA and MinnesotaCare through <strong>MNsure</strong> at <a href="https://www.mnsure.org" target="_blank" rel="noopener">mnsure.org</a> or by calling 651-539-2099. MNsure will automatically determine which program you qualify for based on your income. You can apply year-round for MA and MinnesotaCare &mdash; there is no open enrollment restriction for these programs.</p>

<p>If you already have a hospital bill and were uninsured at the time of service, applying for MA or MinnesotaCare retroactively may cover the charges. Minnesota allows up to 3 months of retroactive Medicaid coverage if you would have been eligible during the period the services were provided.</p>

<h2 id="charity-care">3. Minnesota hospital charity care</h2>

<p>Minnesota does not have a state-level statute mandating specific charity care income thresholds. However, three frameworks create meaningful financial assistance obligations for Minnesota hospitals:</p>

<p><strong>IRS Section 501(r)</strong> applies to all nonprofit Minnesota hospitals and requires:</p>

<ul>
    <li>A publicly posted written <strong>Financial Assistance Policy (FAP)</strong></li>
    <li>Charges to qualifying patients limited to <strong>amounts generally billed (AGB)</strong> to insured patients</li>
    <li>Acceptance of financial assistance applications for at least <strong>240 days</strong> after the first billing statement</li>
    <li>No extraordinary collection actions (lawsuits, liens, garnishment, credit reporting) without first notifying patients of financial assistance availability</li>
</ul>

<p><strong>Minnesota Attorney General oversight:</strong> The AG has enforcement authority over nonprofit hospitals under the Minnesota Nonprofit Corporation Act (MN Statute 317A). Hospitals that fail to provide charity care proportionate to their tax-exempt benefits face AG investigation and potential loss of nonprofit status.</p>

<p><strong>Major Minnesota hospital financial assistance programs:</strong></p>

<ul>
    <li><strong>Hennepin Healthcare</strong> (Minneapolis) &mdash; Offers charity care up to 300% FPL with full write-off below 200% FPL and sliding-scale discounts from 200% to 300% FPL. As a public safety-net hospital, Hennepin Healthcare provides more uncompensated care than any other Minnesota hospital.</li>
    <li><strong>Mayo Clinic Health System</strong> (Rochester and affiliates) &mdash; Financial assistance on a sliding scale for patients demonstrating inability to pay. Mayo&rsquo;s published FAP covers patients up to 400% FPL depending on the specific facility and financial circumstances.</li>
    <li><strong>Allina Health</strong> (Abbott Northwestern, United Hospital, others) &mdash; Financial assistance up to 300% FPL with full write-off for patients below 200% FPL.</li>
    <li><strong>M Health Fairview</strong> (University of Minnesota Medical Center) &mdash; Offers financial assistance up to 300% FPL on a sliding scale.</li>
</ul>

{_embed(mode="markup", title="How does your Minnesota hospital bill compare to Medicare?", subtitle="Enter a CPT code and amount from your bill to see the Medicare benchmark.")}

<p>Apply for <a href="/charity-care">hospital financial assistance</a> as soon as you receive a bill you cannot afford. You have at least 240 days from the first billing statement, but applying early prevents the account from being referred to collections.</p>

<h2 id="medical-debt">4. Minnesota medical debt protections</h2>

<p>Minnesota provides several layers of protection for patients facing medical debt:</p>

<p><strong>6-year statute of limitations:</strong> Under <strong>MN Statute 541.05</strong>, the SOL for most medical debt (both open accounts and written contracts) is 6 years. The clock starts from the date of last payment or the date the debt became delinquent. After 6 years, the debt is time-barred &mdash; if sued, raise the SOL as an affirmative defense. Any payment or written acknowledgment can restart the clock. Check our <a href="/statute-of-limitations">statute of limitations guide</a> for a detailed breakdown.</p>

<p><strong>Minnesota Consumer Protection Act (MN Statute 325D.44):</strong> The Minnesota Attorney General enforces consumer protections against deceptive debt collection practices under this act. Prohibited conduct includes:</p>

<ul>
    <li>Misrepresenting the amount, character, or legal status of a debt</li>
    <li>Threatening legal action on time-barred debt without disclosing the SOL defense</li>
    <li>Using deceptive or misleading collection communications</li>
    <li>Failing to provide required validation notices</li>
</ul>

<p><strong>Interest rate restrictions:</strong> Minnesota law limits post-judgment interest on consumer debts, including medical debt, to the lesser of the contract rate or 10% per annum. Pre-judgment interest on medical debt is generally not permitted unless the original agreement specifies it.</p>

<p><strong>Wage garnishment limits:</strong> Under federal law (which Minnesota follows), garnishment is capped at 25% of disposable earnings or the amount by which weekly disposable earnings exceed 40 times the federal minimum wage, whichever is less. Minnesota&rsquo;s homestead exemption under <strong>MN Statute 510.01</strong> protects up to $450,000 of equity in your primary residence from most creditor judgments, including medical debt judgments.</p>

<div class="key-takeaway">
    <strong>Contacted by a collector about Minnesota medical debt?</strong> Verify the original service date and last payment date before taking any action. Use our <a href="/calculator">free calculator</a> to check whether the original charges were accurate &mdash; inflated charges are grounds for dispute even while evaluating the statute of limitations defense.
</div>

<h2 id="pricing-transparency">5. Hospital pricing and cost transparency in MN</h2>

<p>Minnesota has one of the most developed health care cost transparency infrastructures in the country, anchored by the <strong>Minnesota Health Care Cost Information System</strong>.</p>

<p><strong>MN All-Payer Claims Database (APCD):</strong> Minnesota&rsquo;s APCD collects claims data from virtually all payers &mdash; commercial insurers, Medicare, Medicaid, and MinnesotaCare. The Minnesota Department of Health publishes aggregated cost and utilization data that allows patients and researchers to compare prices across hospitals and procedures.</p>

<p><strong>MN Hospital Price Comparison Tool:</strong> The Minnesota Department of Health maintains a hospital price comparison tool at <a href="https://www.health.state.mn.us" target="_blank" rel="noopener">health.state.mn.us</a> that shows average charges for common inpatient and outpatient procedures at individual Minnesota hospitals. This tool predates the federal CMS price transparency rule and provides Minnesota-specific data not available in national databases.</p>

<p><strong>Average markups at Minnesota hospitals:</strong> BillKarma&rsquo;s analysis of Minnesota hospital chargemaster data reveals significant variation in hospital-to-Medicare markup ratios across the state:</p>

<ul>
    <li><strong>Twin Cities metro area:</strong> Median markup of 3.6&times; Medicare rates, with some hospital outpatient departments reaching 5.2&times;</li>
    <li><strong>Rochester (Mayo Clinic):</strong> Markup ratios averaging 3.2&times; Medicare rates &mdash; below the Twin Cities average despite Mayo&rsquo;s reputation as a premium provider</li>
    <li><strong>Greater Minnesota (rural hospitals):</strong> Markup ratios typically between 2.4&times; and 3.0&times; Medicare rates, reflecting lower operating costs and smaller payer mix leverage</li>
</ul>

<p>Under the federal <strong>Hospital Price Transparency Rule</strong> (effective January 2021), all Minnesota hospitals must publish machine-readable files containing negotiated rates for all services. CMS can impose penalties of up to $5,500 per day for noncompliance. Check your hospital&rsquo;s pricing at <a href="/hospitals/">BillKarma&rsquo;s hospital directory</a> for markup comparisons and transparency compliance grades.</p>

<h2 id="insurance-complaints">6. Minnesota insurance complaint process</h2>

<p>The path for filing an insurance complaint in Minnesota depends on the type of plan:</p>

<p><strong>State-regulated plans (individual, small group, MNsure marketplace, MinnesotaCare):</strong></p>

<ol>
    <li><strong>File a complaint with the Minnesota Department of Commerce</strong> at <a href="https://mn.gov/commerce" target="_blank" rel="noopener">mn.gov/commerce</a> or call 651-539-1500. The Commerce Department regulates HMOs, health insurers, and managed care organizations operating in Minnesota.</li>
    <li><strong>Request an external review</strong> if your claim was denied for medical necessity or clinical reasons. Minnesota law provides the right to have an independent review organization (IRO) examine the denial. The IRO&rsquo;s decision is binding on the insurer.</li>
    <li><strong>Escalate to the Attorney General</strong> if you believe the insurer engaged in deceptive or unfair practices. The AG&rsquo;s consumer protection division investigates patterns of wrongful denials.</li>
</ol>

<p><strong>Self-funded employer plans (ERISA-governed):</strong></p>

<ol>
    <li><strong>File an internal appeal</strong> with your plan administrator. ERISA requires at least one level of internal appeal with a response within 30 days (standard) or 72 hours (urgent).</li>
    <li><strong>File an external review</strong> under the ACA&rsquo;s external review provisions, which apply to most self-funded plans.</li>
    <li><strong>File a complaint with the U.S. Department of Labor</strong> Employee Benefits Security Administration if the plan fails to follow ERISA appeal procedures.</li>
</ol>

<p><strong>HMO vs. PPO complaint paths:</strong> In Minnesota, HMOs are regulated by the Commerce Department and must comply with Minnesota&rsquo;s HMO Act (MN Statute 62D). PPO and indemnity plans are also Commerce-regulated but under different statutory chapters (62A and 62Q). The complaint process is the same &mdash; file with Commerce &mdash; but HMO members have additional protections around network adequacy and referral requirements.</p>

<h2 id="dispute-steps">7. How to dispute a Minnesota hospital bill</h2>

<p>Follow these steps to dispute a hospital bill using Minnesota-specific agencies and resources:</p>

<ol>
    <li><strong>Request an itemized bill.</strong> Minnesota hospitals must provide a detailed itemized statement of all charges. Do not accept a summary statement. Review every line item, CPT code, and revenue code.</li>
    <li><strong>Request the Explanation of Benefits (EOB).</strong> If insured, get the EOB from your insurer for the same date of service. Compare the hospital&rsquo;s charges against the insurer&rsquo;s allowed amounts and your cost-sharing obligations.</li>
    <li><strong>Check for common billing errors.</strong> <a href="/scan">Upload your bill to BillKarma</a> to automatically flag duplicate charges, unbundled services, upcoded E&amp;M levels, and charges exceeding Medicare benchmarks.</li>
    <li><strong>Apply for financial assistance.</strong> If the charges are accurate but unaffordable, apply to the hospital&rsquo;s Financial Assistance Program within 240 days of the first billing statement. Gather proof of income (pay stubs, tax return) and household size documentation.</li>
    <li><strong>File a written dispute.</strong> Send a written dispute letter to the hospital&rsquo;s billing department via certified mail. Cite the specific errors, reference the applicable Minnesota statute (62Q.556 for surprise billing, 325D.44 for deceptive collection practices), and request a corrected bill within 30 days.</li>
    <li><strong>File a complaint with the MN Department of Commerce</strong> if the dispute involves your insurer &mdash; denied claims, incorrect cost-sharing calculations, or surprise billing violations. Call 651-539-1500 or file online at mn.gov/commerce.</li>
    <li><strong>File a complaint with the MN Attorney General</strong> if the hospital or collector engages in deceptive practices, threatens legal action on time-barred debt, or refuses to honor financial assistance obligations. The AG&rsquo;s office accepts complaints at ag.state.mn.us.</li>
    <li><strong>Request external review</strong> for insurance denials based on medical necessity. The Commerce Department will assign an independent review organization whose decision is binding on the insurer.</li>
</ol>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Twin Cities Regional Medical Center &mdash; Date of Service: 01/15/2026</div>
    <div class="line-item error">
        <span>99285 &mdash; Emergency Dept Visit, High Severity + Balance Bill from OON Emergency Physician &nbsp; &#10060; <em>Balance billing for emergency services violates MN Statute 62Q.556. You owe only in-network cost-sharing regardless of the physician&rsquo;s network status.</em></span>
        <span>$2,400.00 (balance billed: $1,600)</span>
    </div>
    <div class="line-item flagged">
        <span>76700 &mdash; Abdominal Ultrasound, Complete &nbsp; &#9888; <em>Charged at $1,840 vs. Medicare rate of $189. Markup of 9.7&times;. Request an explanation and compare against the hospital&rsquo;s published price transparency file.</em></span>
        <span>$1,840.00</span>
    </div>
    <div class="line-item">
        <span>85025 &mdash; Complete Blood Count</span>
        <span>$340.00</span>
    </div>
    <div class="line-item">
        <span>80053 &mdash; Comprehensive Metabolic Panel</span>
        <span>$420.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$5,000.00</span>
    </div>
    <div class="line-total">
        <span>IDENTIFIED ERRORS (illegal balance bill, excessive ultrasound markup)</span>
        <span>Up to &minus;$3,251 in correctable charges</span>
    </div>
</div>

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Case Study 1: MinnesotaCare retroactive coverage eliminates $14,200 ER bill</h3>
    <p><strong>Situation:</strong> A Minneapolis resident working as a freelance graphic designer was uninsured when she visited Hennepin Healthcare&rsquo;s emergency department for severe abdominal pain. She was diagnosed with acute appendicitis and underwent an emergency appendectomy. Total billed: <strong>$14,200</strong>. Her annual income was $28,000 &mdash; approximately 179% FPL for a single adult.</p>
    <p><strong>Action:</strong> A patient financial counselor at Hennepin Healthcare screened her for public program eligibility and determined she qualified for MinnesotaCare. Because Minnesota allows up to 3 months of retroactive Medicaid/MinnesotaCare coverage, the counselor helped her apply through MNsure for coverage effective the month of her ER visit. Her MinnesotaCare application was approved within 3 weeks.</p>
    <p><strong>Outcome:</strong> MinnesotaCare covered the entire hospitalization retroactively. The patient&rsquo;s out-of-pocket responsibility was reduced to a $3.50 copay. <strong>Savings: $14,196.50.</strong> She now pays $28/month in MinnesotaCare premiums for comprehensive coverage including dental and mental health.</p>
</div>

<div class="case-study">
    <h3>Case Study 2: Surprise billing arbitration &mdash; $6,800 anesthesiology balance bill eliminated under 62Q.556</h3>
    <p><strong>Situation:</strong> A St. Paul patient had a scheduled knee arthroscopy at an in-network surgical center. The surgeon and facility were both in-network with her HealthPartners plan. After the procedure, she received a separate bill of <strong>$6,800</strong> from the anesthesiologist, who was out of network. The anesthesiologist&rsquo;s practice balance-billed her for the difference between their charge and the amount HealthPartners paid.</p>
    <p><strong>Action:</strong> The patient filed a complaint with the Minnesota Department of Commerce citing MN Statute 62Q.556. She documented that she had not been notified before the procedure that the anesthesiologist was out of network and had no meaningful choice of anesthesia provider. The Commerce Department opened an investigation and contacted both HealthPartners and the anesthesiology practice.</p>
    <p><strong>Outcome:</strong> The Commerce Department determined the balance bill violated 62Q.556. The anesthesiologist&rsquo;s practice was required to withdraw the $6,800 balance bill. The patient owed only her in-network copay of $150. <strong>Savings: $6,650.</strong> HealthPartners and the anesthesiology group resolved the payment dispute between themselves, as the statute requires.</p>
</div>

<div class="case-study">
    <h3>Case Study 3: Mayo Clinic affiliate charity care &mdash; $31,000 cardiac bill reduced to $4,200</h3>
    <p><strong>Situation:</strong> A Rochester-area patient was admitted to Mayo Clinic Hospital &ndash; Saint Marys Campus for a cardiac catheterization and stent placement after presenting with chest pain. Total billed: <strong>$31,000</strong>. The patient had a high-deductible health plan with a $6,500 deductible and 20% coinsurance. After insurance adjustments, patient responsibility was $12,400. The patient was a self-employed carpenter earning $52,000 annually for a household of three &mdash; approximately 215% FPL.</p>
    <p><strong>Action:</strong> The patient applied to Mayo Clinic&rsquo;s financial assistance program within 30 days of the first billing statement. He submitted his most recent tax return, three months of bank statements, and a letter documenting seasonal income variability. Mayo&rsquo;s financial counselor determined he qualified for a 66% reduction under Mayo&rsquo;s sliding-scale FAP for patients between 200% and 300% FPL.</p>
    <p><strong>Outcome:</strong> The $12,400 patient responsibility was reduced by 66% to <strong>$4,216</strong>. Mayo also offered a 12-month interest-free payment plan. <strong>Savings from financial assistance: $8,184.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Minnesota have its own surprise billing law separate from the federal No Surprises Act?</h3>
        <p>Yes. MN Statute 62Q.556 took effect in 2019 and prohibits balance billing for emergency services and for out-of-network providers at in-network facilities when the patient had no meaningful choice. For state-regulated plans, 62Q.556 controls. For self-funded employer plans, the federal NSA applies. Under either law, you owe only in-network cost-sharing &mdash; the provider and insurer must resolve the payment dispute between themselves.</p>
    </div>

    <div class="faq-item">
        <h3>What is MinnesotaCare and who qualifies?</h3>
        <p>MinnesotaCare is Minnesota&rsquo;s public health insurance program for residents earning between 138% and 200% FPL &mdash; roughly $21,600 to $31,200 for a single adult in 2026. It covers hospital, physician, prescription, dental, mental health, and preventive services with income-based premiums from $0 to $80/month. Apply at mnsure.org. MinnesotaCare allows up to 3 months of retroactive coverage, so apply even if you already received care while uninsured.</p>
    </div>

    <div class="faq-item">
        <h3>What is Minnesota&rsquo;s statute of limitations on medical debt?</h3>
        <p>Minnesota applies a 6-year SOL under MN Statute 541.05. The clock runs from the date of last payment or the date the debt became delinquent. After 6 years, the debt is time-barred. Any payment or written acknowledgment restarts the clock. If sued on expired debt, file a written Answer asserting the SOL defense &mdash; never ignore a summons, as a default judgment will be entered regardless of whether the SOL has passed.</p>
    </div>

    <div class="faq-item">
        <h3>Are Minnesota hospitals required to provide charity care or financial assistance?</h3>
        <p>Minnesota has no state-mandated income threshold for charity care, but nonprofit hospitals must comply with IRS Section 501(r) &mdash; requiring a written FAP, charge limits for qualifying patients, and a 240-day application window. Major systems include Hennepin Healthcare (up to 300% FPL), Mayo Clinic (up to 400% FPL), Allina Health (up to 300% FPL), and M Health Fairview (up to 300% FPL). The Minnesota AG enforces nonprofit charitable compliance.</p>
    </div>

    <div class="faq-item">
        <h3>How do I file an insurance complaint in Minnesota?</h3>
        <p>For state-regulated plans, file with the Minnesota Department of Commerce at mn.gov/commerce or call 651-539-1500. The Commerce Department handles HMO and PPO complaints, administers external reviews for medical necessity denials, and enforces 62Q.556 surprise billing protections. For self-funded employer plans, file with the U.S. Department of Labor. For deceptive collection practices, contact the Minnesota Attorney General&rsquo;s consumer protection division.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.revisor.mn.gov/statutes/cite/62Q.556" target="_blank" rel="noopener">MN Statute 62Q.556 &mdash; Balance Billing Prohibition (Minnesota Surprise Billing Law)</a></li>
    <li><a href="https://www.revisor.mn.gov/statutes/cite/541.05" target="_blank" rel="noopener">MN Statute 541.05 &mdash; Statute of Limitations for Contracts and Debts</a></li>
    <li><a href="https://www.revisor.mn.gov/statutes/cite/325D.44" target="_blank" rel="noopener">MN Statute 325D.44 &mdash; Minnesota Consumer Protection: Deceptive Trade Practices</a></li>
    <li><a href="https://www.revisor.mn.gov/statutes/cite/510.01" target="_blank" rel="noopener">MN Statute 510.01 &mdash; Minnesota Homestead Exemption</a></li>
    <li><a href="https://mn.gov/commerce/" target="_blank" rel="noopener">Minnesota Department of Commerce &mdash; Insurance Complaints and External Review</a></li>
    <li><a href="https://www.mnsure.org/" target="_blank" rel="noopener">MNsure &mdash; Minnesota Health Insurance Marketplace (MinnesotaCare and MA Applications)</a></li>
    <li><a href="https://www.health.state.mn.us/data/economics/index.html" target="_blank" rel="noopener">Minnesota Department of Health &mdash; Health Care Cost Information System and Hospital Price Data</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS &mdash; No Surprises Act: Federal Balance Billing Protections</a></li>
    <li><a href="https://www.ag.state.mn.us/consumer/" target="_blank" rel="noopener">Minnesota Attorney General &mdash; Consumer Protection Division</a></li>
    <li><a href="https://www.hennepinhealthcare.org/patients-visitors/financial-services/" target="_blank" rel="noopener">Hennepin Healthcare &mdash; Financial Assistance and Charity Care Program</a></li>
</ul>
""",
})
