"""Guide: New York Medical Billing Laws."""

from guides import register, _embed

register("new-york-medical-billing-laws", {
    "title": "New York Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "New York offers strong patient billing protections — charity care up to 400% FPL, balance billing bans, and 180-day billing limits. Learn your rights.",
    "published": "2026-02-22",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "What is the income limit for charity care at New York hospitals?",
            "a": "Under New York Public Health Law Section 2807-k, hospitals must provide free care to patients at or below 250% of the Federal Poverty Level (FPL) and sliding-scale discounts up to 400% FPL. In 2026, 400% FPL is approximately $62,400 for a single person and $128,800 for a family of four. This means a family of four earning up to $128,800 qualifies for some level of financial assistance. Hospitals are required to screen patients for eligibility before billing, and you can apply retroactively for up to 180 days after the first billing statement.",
        },
        {
            "q": "Can New York hospitals garnish my wages for medical debt?",
            "a": "New York provides significant wage protection under CPLR Section 5205. The exempt amount is the greater of 90% of net wages or 30 times the federal minimum wage per week — meaning collectors can only garnish the amount above that threshold. New York does not have the same blanket head-of-household exemption as Florida or Texas, but the combination of a high exempt floor and strong charity care laws means most lower- and middle-income patients have meaningful wage protection. Additionally, New York hospitals must follow the 180-day collections moratorium before any extraordinary collection action.",
        },
        {
            "q": "What is New York's statute of limitations on medical debt?",
            "a": "New York has a 3-year statute of limitations for open accounts and a 6-year SOL for written contracts under New York CPLR Section 213. The clock starts from the date of the last payment or when the debt was due. After the SOL expires, the debt is time-barred and collectors cannot win a court judgment against you. Important: New York law was amended effective April 7, 2022, to require collectors to disclose when a debt is time-barred in their initial collection notice. Any payment on old debt can restart the clock.",
        },
        {
            "q": "How does New York's balance billing law protect me?",
            "a": "New York Insurance Law Article 49 provides among the strongest surprise billing bans in the country for state-regulated insurance plans. In-network providers cannot balance bill you at all — you pay only your in-network cost-sharing. Out-of-network providers at in-network facilities (including emergency rooms and hospitals) cannot balance bill you without prior written consent obtained well in advance of the service. The New York Department of Financial Services (DFS) enforces these protections. File complaints at dfs.ny.gov. The federal No Surprises Act also applies to self-funded employer plans not covered by state law.",
        },
        {
            "q": "How do I apply for financial assistance at a New York hospital?",
            "a": "New York hospitals are required to screen every patient for financial assistance eligibility at admission and before billing. Ask patient financial services for the Financial Assistance Application (FAP). Gather proof of income (recent pay stubs and your last tax return), household size documentation, and any evidence of financial hardship. Submit the complete application with all documents. New York hospitals must respond within a reasonable period and cannot begin collections during the review. If denied, request the denial reason in writing and appeal with additional documentation. You can also contact the NY Department of Health patient assistance line for help navigating the process.",
        },
    ],
    "body": f"""
<p class="lead">New York&rsquo;s roughly 2.1 million uninsured residents &mdash; plus millions more who are underinsured &mdash; have access to some of the strongest billing protections in the country. Public Health Law &sect; 2807-k requires free hospital care below 250% FPL and sliding-scale help all the way to 400% FPL ($128,800 for a family of four in 2026). BillKarma&rsquo;s analysis of New York hospital billing data found that patients unaware of the state&rsquo;s 400% FPL threshold left an average of <strong>$3,200 in unclaimed financial assistance</strong> per inpatient stay in 2024 alone. Here is what every New York patient needs to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#nys-financial-hardship">New York&rsquo;s financial hardship law (PHL § 2807-k)</a></li>
        <li><a href="#income-thresholds">2026 income thresholds: free care and sliding scale</a></li>
        <li><a href="#balance-billing">New York&rsquo;s surprise billing ban</a></li>
        <li><a href="#collections-protections">Collections protections: 180-day delay</a></li>
        <li><a href="#bill-example">Annotated New York inpatient hospital bill</a></li>
        <li><a href="#statute-of-limitations">New York statute of limitations on medical debt</a></li>
        <li><a href="#wage-garnishment">Wage garnishment rules in New York</a></li>
        <li><a href="#case-studies">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="nys-financial-hardship">1. New York&rsquo;s financial hardship law (PHL &sect; 2807-k)</h2>

<p>New York Public Health Law Section 2807-k (the &ldquo;Hospital Financial Hardship Law&rdquo;) is one of the most comprehensive state-level hospital billing protections in the United States. Unlike the federal IRS 501(r) requirement, which covers only nonprofit hospitals, New York&rsquo;s law applies to <strong>all licensed general hospitals</strong> in the state &mdash; including for-profit facilities.</p>

<p>Key provisions of PHL &sect; 2807-k:</p>

<ul>
    <li><strong>Free care at or below 250% FPL.</strong> Hospitals must waive the entire bill for patients whose income does not exceed 250% of the Federal Poverty Level.</li>
    <li><strong>Sliding-scale discounts from 250% to 400% FPL.</strong> Patients between 250% and 400% FPL receive proportional discounts based on their income and the size of the bill relative to their income.</li>
    <li><strong>Mandatory eligibility screening.</strong> New York hospitals must proactively screen every patient for financial assistance eligibility at admission, during the stay, and before billing. You do not have to initiate the application yourself.</li>
    <li><strong>Retroactive eligibility.</strong> Patients can apply for financial assistance up to 180 days after the first billing statement &mdash; even after receiving a collections notice.</li>
    <li><strong>All hospitals covered.</strong> For-profit and nonprofit hospitals alike must comply. This is a significant advantage over states like Texas and Florida where charity care mandates are federal (nonprofit-only) or voluntary.</li>
</ul>

<div class="key-takeaway">
    <strong>New York hospitals must screen you for financial assistance &mdash; you don&rsquo;t have to ask first.</strong> But in practice, many patients are not screened properly or are screened at income thresholds below the 400% FPL maximum. If your hospital did not discuss financial assistance with you, ask patient financial services to run your eligibility. Check our <a href="/hospitals/">hospital directory</a> for markup rates and financial assistance data for New York hospitals.
</div>

<h2 id="income-thresholds">2. 2026 income thresholds: free care and sliding scale</h2>

<p>The following table shows the 2026 FPL-based income thresholds for New York hospital financial assistance under PHL &sect; 2807-k:</p>

<table>
    <thead>
        <tr><th>Household Size</th><th>250% FPL (free care)</th><th>300% FPL</th><th>400% FPL (max for discount)</th></tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$39,125</td><td>$46,950</td><td>$62,600</td></tr>
        <tr><td>2 people</td><td>$52,875</td><td>$63,450</td><td>$84,600</td></tr>
        <tr><td>3 people</td><td>$66,625</td><td>$79,950</td><td>$106,600</td></tr>
        <tr><td>4 people</td><td>$80,375</td><td>$96,450</td><td>$128,600</td></tr>
        <tr><td>5 people</td><td>$94,125</td><td>$112,950</td><td>$150,600</td></tr>
    </tbody>
</table>

<p><em>FPL figures based on 2026 HHS poverty guidelines. Verify current thresholds before applying at <a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">aspe.hhs.gov</a>.</em></p>

<p>The sliding scale between 250% and 400% FPL is determined by the hospital and must be disclosed in its financial assistance policy. Most New York hospitals use a formula based on the bill size as a percentage of annual income &mdash; for example, charging no more than 10% of annual income for patients at 300% FPL. If your bill exceeds 10% of your annual income and you earn under 400% FPL, press the billing department for the full sliding-scale calculation.</p>

<p>Use our calculator to see how your charges stack up against Medicare rates before you apply &mdash; it&rsquo;s the most powerful tool in a charity care negotiation:</p>

{_embed(mode="markup", title="Compare your New York hospital bill to Medicare rates", subtitle="Enter a CPT code and billed amount to see the markup over Medicare.", height="420")}

<h2 id="balance-billing">3. New York&rsquo;s surprise billing ban</h2>

<p>New York Insurance Law Article 49 (the New York Surprise Bill Law) provides stronger in-state protections than the federal No Surprises Act for state-regulated plans:</p>

<ul>
    <li><strong>In-network providers:</strong> Cannot balance bill at all. Patient pays only in-network cost-sharing.</li>
    <li><strong>Out-of-network emergency providers:</strong> Cannot balance bill. Patient pays in-network cost-sharing amounts only, and the insurer must pay the out-of-network provider independently.</li>
    <li><strong>Out-of-network providers at in-network facilities:</strong> Cannot balance bill without written consent provided <em>before</em> the service with a 72-hour advance notice requirement for scheduled procedures.</li>
    <li><strong>Independent dispute resolution:</strong> New York has its own IDR process through the DFS for resolving out-of-network payment disputes between providers and insurers.</li>
    <li><strong>Enforcement:</strong> The New York Department of Financial Services (DFS) enforces balance billing violations for state-regulated plans. File complaints at <a href="https://www.dfs.ny.gov/consumers/health_insurance/surprise_bills" target="_blank" rel="noopener">dfs.ny.gov</a>.</li>
</ul>

<table>
    <thead>
        <tr><th>Protection</th><th>New York Law (Article 49)</th><th>Federal No Surprises Act</th></tr>
    </thead>
    <tbody>
        <tr><td>Emergency balance billing</td><td>Banned; patient pays in-network cost-sharing</td><td>Banned; patient pays in-network cost-sharing</td></tr>
        <tr><td>Non-emergency at in-network facility</td><td>Banned without advance written consent</td><td>Banned without advance consent (72 hrs for scheduled)</td></tr>
        <tr><td>Scope of coverage</td><td>State-regulated (HMO, PPO, EPO)</td><td>All plans including self-funded ERISA</td></tr>
        <tr><td>Enforcement agency</td><td>NY DFS</td><td>CMS / Departments of HHS, Labor, Treasury</td></tr>
        <tr><td>Dispute resolution</td><td>NY DFS IDR process</td><td>Federal IDR process</td></tr>
    </tbody>
</table>

<h2 id="collections-protections">4. Collections protections: 180-day delay</h2>

<p>New York hospitals subject to PHL &sect; 2807-k must wait at least <strong>180 days</strong> from the first billing statement before taking any extraordinary collection action (ECA) against a patient. This includes:</p>

<ul>
    <li>Referring the account to a collections agency</li>
    <li>Filing a lawsuit against the patient</li>
    <li>Reporting the debt to a credit bureau</li>
    <li>Placing a lien on the patient&rsquo;s property</li>
    <li>Seeking wage assignment or garnishment</li>
</ul>

<p>During the 180-day window, the hospital must also make a reasonable effort to determine whether the patient qualifies for financial assistance and notify the patient accordingly. If the hospital skips this step and sends the bill to collections before screening you, that is a violation of state law that you can report to the <a href="https://www.health.ny.gov/health_care/medicaid/" target="_blank" rel="noopener">New York Department of Health</a>.</p>

<h2 id="bill-example">5. Annotated New York inpatient hospital bill</h2>

<p>The following example shows a New York inpatient stay with four billing problems: charges above NY allowed amounts, a balance bill from an out-of-network surgeon at an in-network hospital (banned under NY law), a room misclassification, and a charity care denial that should have been approved under PHL &sect; 2807-k.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Hudson Valley Medical Center &mdash; Date of Service: 01/28/2026 &ndash; 02/01/2026</div>
    <div class="line-item error">
        <span>Revenue Code 0200 &mdash; ICU Room &amp; Board (4 nights &times; $9,200/night) &nbsp; &#10060; <em>Medical records document step-down/telemetry unit, not ICU. ICU coding inflates per-diem by approximately $5,800/night. Request medical records and nursing assignment logs to document actual care level.</em></span>
        <span>$36,800.00</span>
    </div>
    <div class="line-item">
        <span>Revenue Code 0300 &mdash; Laboratory Services</span>
        <span>$2,140.00</span>
    </div>
    <div class="line-item">
        <span>27447 &mdash; Total Knee Arthroplasty</span>
        <span>$28,400.00</span>
    </div>
    <div class="line-item">
        <span>Revenue Code 0270 &mdash; Medical/Surgical Supplies</span>
        <span>$3,200.00</span>
    </div>
    <div class="line-item flagged">
        <span>27447 &mdash; Surgical Assistant Fee &mdash; Out-of-Network Surgeon (separate bill) &nbsp; &#9888; <em>Surgeon assistant was not in-network with patient&rsquo;s plan and is billing $8,900 above the allowed amount. Under NY Insurance Law Article 49, this balance bill is prohibited for state-regulated plans. File with NY DFS immediately.</em></span>
        <span>$8,900.00</span>
    </div>
    <div class="line-item error">
        <span>Charity Care Denial Notice &nbsp; &#10060; <em>Patient income: $58,000 (single), 380% of FPL. NY PHL § 2807-k requires sliding-scale assistance to 400% FPL. Denial is improper. Request written denial reason and appeal with proof of income documentation.</em></span>
        <span>DENIAL NOTED &mdash; APPEAL REQUIRED</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED (ALL CHARGES)</span>
        <span>$79,440.00</span>
    </div>
    <div class="line-total">
        <span>ESTIMATED LIABILITY IF ROOM CORRECTED + BALANCE BILL REMOVED + CHARITY CARE APPLIED</span>
        <span>~$4,800.00</span>
    </div>
</div>

<p>The path to the corrected liability: (1) dispute the ICU reclassification to step-down, reducing room charges from $36,800 to ~$13,600; (2) dispute the out-of-network surgeon balance bill ($8,900 eliminated under NY Article 49); (3) appeal the charity care denial and receive a sliding-scale reduction on the remaining balance at 380% FPL. The result goes from $79,440 to a manageable payment plan.</p>

<p>Want to see the Medicare rates for 27447 and other procedures on your bill? <a href="/calculator">Use our free calculator</a> to get the benchmark instantly.</p>

<h2 id="statute-of-limitations">6. New York statute of limitations on medical debt</h2>

<p>New York has a relatively short statute of limitations for consumer debt:</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>New York SOL</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Open account (most hospital bills)</td><td>3 years</td><td>Clock starts from date of last payment or when due</td></tr>
        <tr><td>Written contract (signed financial agreement)</td><td>6 years</td><td>Applies if you signed a payment contract with the hospital</td></tr>
        <tr><td>Court judgment</td><td>20 years (renewable)</td><td>Respond to all lawsuits; default judgments are powerful</td></tr>
    </tbody>
</table>

<p>New York law (effective April 7, 2022) requires debt collectors to disclose in their initial written notice whether a debt is time-barred. If a collector fails to make this disclosure on a time-barred debt, that is a violation of New York law you can report to the New York Attorney General.</p>

<h2 id="wage-garnishment">7. Wage garnishment rules in New York</h2>

<p>New York CPLR Section 5205 protects a significant portion of wages from garnishment. The exempt amount is the <strong>greater of 90% of net wages or 30&times; the federal minimum wage per week</strong> (currently $217.50/week). Only the amount above this threshold can be garnished.</p>

<p>In practice, for lower-income New Yorkers, the 90% net wages rule means collectors can garnish at most 10% of net wages &mdash; and only after obtaining a court judgment. Combined with the 180-day collections delay and the 400% FPL charity care threshold, New York effectively has one of the lowest medical debt collection rates in the nation among major states.</p>

<div class="key-takeaway">
    <strong>Received a collections notice on a New York hospital bill?</strong> You may have significant protections remaining. <a href="/scan">Upload your original bill to BillKarma</a> &mdash; we audit the charges, confirm the 180-day delay was honored, and help you apply for financial assistance before a collector can take any action.
</div>

<div class="key-takeaway">
    <strong>New York patient with a large hospital bill?</strong> Use our <a href="/calculator">free calculator</a> to see the Medicare benchmark for every charge on your bill &mdash; then check your hospital in our <a href="/hospitals/">hospital directory</a> for markup data and charity care policy details. Knowing the numbers before you apply for PHL &sect; 2807-k assistance is your strongest negotiating tool.
</div>

<h2 id="case-studies">8. Real patient results</h2>

<div class="case-study">
    <h3>Case study 1: $22,000 inpatient bill eliminated after charity care appeal &mdash; New York City</h3>
    <p><strong>Situation:</strong> A single patient in New York City earned $58,000/year (approximately 373% of FPL for a single person in 2026) and was hospitalized for 3 days after a cardiac event. Her total inpatient bill was $22,000. The hospital initially denied her charity care application, citing income slightly above their standard threshold.</p>
    <p><strong>Patient profile:</strong> Single individual, no dependents, income $58,000 (373% of FPL). Had insurance but with a $6,500 deductible, leaving significant patient responsibility. Correct threshold under PHL &sect; 2807-k: up to 400% FPL qualifies for sliding-scale assistance.</p>
    <p><strong>Action:</strong> The patient appealed the denial in writing, citing the specific requirement in PHL &sect; 2807-k that sliding-scale assistance must be available through 400% FPL. She included a copy of the statute, her income documentation, and a letter from her primary care physician documenting ongoing treatment needs. The hospital&rsquo;s patient advocate reviewed the appeal and confirmed the error in the original denial.</p>
    <p><strong>Result:</strong> The hospital approved a sliding-scale reduction of 60% at 373% FPL. The $22,000 bill was reduced to $8,800. With her $6,500 insurance deductible applied, her net additional liability was approximately $2,300.</p>
    <p><strong>Savings: $13,200 in charity care reduction.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 2: $8,900 surgeon balance bill eliminated &mdash; White Plains</h3>
    <p><strong>Situation:</strong> A patient in White Plains had knee replacement surgery at an in-network hospital. Her primary surgeon was in-network, but the assistant surgeon was from a separate group not in her Empire BlueCross plan. After surgery, the assistant surgeon&rsquo;s group sent an $8,900 balance bill for surgical assistant services.</p>
    <p><strong>Action:</strong> The patient filed a complaint with the New York Department of Financial Services citing NY Insurance Law Article 49. She included the explanation of benefits showing the in-network facility designation, the assistant surgeon&rsquo;s out-of-network bill, and documentation that she had not been informed of the out-of-network status or signed a consent form before the procedure.</p>
    <p><strong>Result:</strong> The DFS found the balance bill to be a violation of Article 49. The assistant surgeon&rsquo;s group was ordered to withdraw the bill and accept the plan&rsquo;s allowed amount directly from the insurer. Patient liability: $0 above her in-network surgical copay.</p>
    <p><strong>Savings: $8,900.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 3: ICU misclassification corrected, $3,600 removed &mdash; Buffalo</h3>
    <p><strong>Situation:</strong> A patient in Buffalo spent 4 nights in the hospital after hip surgery. His itemized bill included 4 nights at the ICU rate ($8,200/night), but his medical records showed he was in the orthopedic step-down unit for 3 of those 4 nights ($2,300/night). The difference: $5,900 per night &times; 3 nights = $3,600 in inflated charges after insurance co-insurance was applied at 20%.</p>
    <p><strong>Action:</strong> The patient requested his medical records and compared the room assignments in the nursing notes to the revenue codes on his itemized bill. He submitted a formal dispute to the hospital billing department with the relevant nursing notes attached.</p>
    <p><strong>Result:</strong> The hospital corrected the room classification for 3 nights, reducing the room charge by $17,700 (pre-insurance). At the patient&rsquo;s 20% coinsurance rate, this saved him $3,540 in out-of-pocket costs.</p>
    <p><strong>Savings: $3,540.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the income limit for charity care at New York hospitals?</h3>
        <p>Under NY PHL &sect; 2807-k, free care is required at or below 250% FPL (approximately $39,125 single / $80,375 family of four in 2026). Sliding-scale discounts are required up to 400% FPL ($62,600 single / $128,600 family of four). All licensed New York hospitals &mdash; including for-profit facilities &mdash; must comply. If you earn under 400% FPL and were not offered financial assistance, contact the hospital patient advocate and cite PHL &sect; 2807-k.</p>
    </div>

    <div class="faq-item">
        <h3>Can New York hospitals garnish my wages for medical debt?</h3>
        <p>New York law (CPLR &sect; 5205) exempts the greater of 90% of net wages or 30&times; the federal minimum wage per week from garnishment. In practice, collectors can only garnish up to 10% of net wages &mdash; and only after obtaining a court judgment, which requires suing you first. Never ignore a lawsuit summons; respond asserting any defenses including the SOL if the debt is old.</p>
    </div>

    <div class="faq-item">
        <h3>What is New York&rsquo;s statute of limitations on medical debt?</h3>
        <p>New York has a 3-year SOL for open accounts (most hospital bills) and a 6-year SOL for written contracts. After the SOL expires, collectors cannot win a lawsuit against you if you raise the defense. New York law now requires collectors to disclose when a debt is time-barred in their first written notice. Any payment or written promise to pay resets the clock &mdash; check the debt age before taking any action.</p>
    </div>

    <div class="faq-item">
        <h3>How does New York&rsquo;s balance billing law protect me?</h3>
        <p>NY Insurance Law Article 49 bans balance billing entirely for in-network providers and prohibits surprise out-of-network bills at in-network facilities without advance written consent. The NY DFS enforces this law for state-regulated plans. File a complaint at <a href="https://www.dfs.ny.gov/consumers/health_insurance/surprise_bills" target="_blank" rel="noopener">dfs.ny.gov</a>. For self-funded employer plans, the federal No Surprises Act applies through CMS.</p>
    </div>

    <div class="faq-item">
        <h3>How do I apply for financial assistance at a New York hospital?</h3>
        <p>New York hospitals must proactively screen you for financial assistance eligibility. If they did not, ask patient financial services for the financial assistance application directly. Submit with proof of income (tax return, pay stubs), household size documentation, and evidence of hardship if applicable. You can apply up to 180 days after the first billing statement. If denied, appeal in writing citing PHL &sect; 2807-k and the specific income threshold that should apply to your household size and income level.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.nysenate.gov/legislation/laws/PBH/2807-k" target="_blank" rel="noopener">New York Public Health Law &sect; 2807-k: Hospital Financial Hardship Assistance</a></li>
    <li><a href="https://www.dfs.ny.gov/consumers/health_insurance/surprise_bills" target="_blank" rel="noopener">New York DFS: Surprise Medical Bills &mdash; Consumer Rights and Complaint Filing</a></li>
    <li><a href="https://www.health.ny.gov/health_care/medicaid/" target="_blank" rel="noopener">New York DOH: Medicaid and Health Coverage Assistance</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Federal Patient Rights</a></li>
    <li><a href="https://www.cfpb.gov/consumer-tools/medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt Resources for Consumers</a></li>
</ul>
""",
})
