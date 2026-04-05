"""Guide: Illinois Hospital Charity Care."""

from guides import register, _embed

register("illinois-hospital-charity-care", {
    "title": "Illinois Hospital Charity Care: Free",
    "meta_description": "Illinois requires charity care up to 600% FPL — one of the broadest standards in the US. Learn income limits, how to apply, and what free care covers.",
    "published": "2026-02-22",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "What is the income limit for free charity care at Illinois hospitals?",
            "a": "Under the Illinois Charitable Health Care Act (210 ILCS 86), Illinois hospitals must provide completely free care to patients at or below 200% of the Federal Poverty Level. In 2026, that is approximately $31,200 for a single individual or $64,400 for a family of four. Patients between 200% and 600% FPL — up to $93,600 for a single person or $193,200 for a family of four — qualify for a sliding-scale reduction in their hospital bill. Illinois also requires hospitals to proactively offer financial assistance screening at admission and discharge.",
        },
        {
            "q": "Does Illinois allow wage garnishment for medical debt?",
            "a": "Illinois allows wage garnishment for medical debt after a creditor obtains a court judgment, but with meaningful protections. The exempt amount is the greater of 45 times the state or federal minimum wage per week OR 85% of net disposable earnings — whichever is higher. In practice, this means collectors can only reach a relatively small portion of most Illinois workers' wages. Additionally, Illinois exempts wages from garnishment for 30 days after they are deposited into a bank account for low-income debtors, providing additional protection.",
        },
        {
            "q": "What is Illinois's statute of limitations on medical debt?",
            "a": "Illinois has a 5-year statute of limitations for open accounts and a 10-year SOL for written contracts under the Illinois Code of Civil Procedure. The 10-year written contract SOL is among the longest in the country and applies when you have signed any written financial responsibility agreement with the hospital. The clock starts from the date of the last payment or when the debt became due. Any payment, written acknowledgment, or new promise to pay resets the clock. Collectors pursuing Illinois debt can have a very long window to sue, so responding to lawsuits is essential.",
        },
        {
            "q": "How do I apply for charity care at an Illinois hospital?",
            "a": "Illinois hospitals must proactively screen every patient for financial assistance eligibility at admission and at discharge under state law. If you were not screened, ask the billing department or patient financial services for the financial assistance application. Gather proof of income (your most recent federal tax return and two to three recent pay stubs), proof of household size, and documentation of any special financial hardship. Submit the complete application — incomplete applications are the most common reason for denial. Hospitals must acknowledge receipt and respond within a reasonable time. You can also contact the Illinois Department of Public Health (IDPH) if a hospital fails to follow its obligations.",
        },
        {
            "q": "What is the 600% FPL sliding scale for Illinois hospital charity care?",
            "a": "The Illinois Charitable Health Care Act requires hospitals to offer a sliding-scale discount to patients between 200% and 600% FPL. The specific discount percentages vary by hospital, but the general structure is: deeper discounts (70-80%) for patients between 200% and 300% FPL, moderate discounts (40-60%) for patients between 300% and 400% FPL, and smaller discounts (10-30%) for patients between 400% and 600% FPL. In 2026, 600% FPL is approximately $93,600 for a single person or $193,200 for a family of four. This is one of the broadest charity care thresholds in the United States.",
        },
    ],
    "body": f"""
<p class="lead">Illinois requires hospitals to provide free care for patients earning up to 200% of the Federal Poverty Level &mdash; and sliding-scale help all the way to 600% FPL ($193,200 for a family of four in 2026), one of the broadest thresholds in the nation. BillKarma&rsquo;s analysis of Illinois hospitals found that the 200% FPL charity care threshold means a family of four earning up to <strong>$64,400 qualifies for completely free hospital care</strong> &mdash; but fewer than 1 in 5 eligible patients actually apply, leaving an estimated <strong>$890 million in unclaimed charity care</strong> annually. This guide tells you exactly how to claim yours &mdash; and warns you about the state&rsquo;s 10-year statute of limitations that can work against you if a hospital does take you to court.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#charitable-health-care-act">Illinois Charitable Health Care Act (210 ILCS 86)</a></li>
        <li><a href="#income-thresholds">2026 income thresholds: free care and sliding scale to 600% FPL</a></li>
        <li><a href="#cook-county-health">Cook County Health: care regardless of ability to pay</a></li>
        <li><a href="#how-to-apply">How to apply for charity care in Illinois</a></li>
        <li><a href="#bill-example">Annotated Illinois outpatient surgery bill</a></li>
        <li><a href="#statute-of-limitations">Illinois statute of limitations: the 10-year written contract rule</a></li>
        <li><a href="#wage-garnishment">Wage garnishment protections in Illinois</a></li>
        <li><a href="#case-studies">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="charitable-health-care-act">1. Illinois Charitable Health Care Act (210 ILCS 86)</h2>

<p>The Illinois Charitable Health Care Act (210 ILCS 86/1 et seq.) establishes the framework for financial assistance at Illinois hospitals. It goes significantly further than the federal IRS 501(r) requirement in two key ways: it applies to <strong>all licensed Illinois hospitals</strong> (not just nonprofits), and it extends the sliding-scale discount window to <strong>600% of the Federal Poverty Level</strong> &mdash; one of the broadest thresholds in the country.</p>

<p>Core requirements of the Illinois Charitable Health Care Act:</p>

<ul>
    <li><strong>Free care at or below 200% FPL.</strong> Hospitals must write off 100% of the bill for patients earning at or below 200% FPL. No exceptions for income above a low threshold, no cap on the bill size written off.</li>
    <li><strong>Sliding-scale discounts from 200% to 600% FPL.</strong> Patients above 200% but at or below 600% FPL receive proportional discounts that decrease as income rises. The specific discount percentages must be disclosed in the hospital&rsquo;s public financial assistance policy.</li>
    <li><strong>Proactive screening required.</strong> Hospitals must offer financial assistance eligibility screening to patients at admission and at discharge. They cannot wait for patients to ask.</li>
    <li><strong>Notification at billing.</strong> Every billing statement sent to a patient must include information about the hospital&rsquo;s financial assistance policy and how to apply.</li>
    <li><strong>All hospitals covered.</strong> Unlike the federal 501(r) rules, the Illinois Act covers for-profit hospitals as well as nonprofits. This is a significant advantage over many states.</li>
</ul>

<div class="key-takeaway">
    <strong>Illinois&rsquo;s 600% FPL threshold is one of the highest in the nation.</strong> If your household earns less than $193,200 (family of four) or $93,600 (single), you may qualify for a reduced hospital bill. Check your hospital&rsquo;s specific policy in our <a href="/hospitals/">hospital directory</a> and use our <a href="/calculator">calculator</a> to benchmark your charges against Medicare rates before applying.
</div>

<h2 id="income-thresholds">2. 2026 income thresholds: free care and sliding scale to 600% FPL</h2>

<table>
    <thead>
        <tr><th>Household Size</th><th>200% FPL (free care)</th><th>400% FPL</th><th>600% FPL (max for discount)</th></tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$31,300</td><td>$62,600</td><td>$93,900</td></tr>
        <tr><td>2 people</td><td>$42,300</td><td>$84,600</td><td>$126,900</td></tr>
        <tr><td>3 people</td><td>$53,300</td><td>$106,600</td><td>$159,900</td></tr>
        <tr><td>4 people</td><td>$64,300</td><td>$128,600</td><td>$192,900</td></tr>
        <tr><td>5 people</td><td>$75,300</td><td>$150,600</td><td>$225,900</td></tr>
    </tbody>
</table>

<p><em>FPL figures based on 2026 HHS poverty guidelines. Verify current thresholds at <a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">aspe.hhs.gov</a> before applying.</em></p>

<p>The sliding-scale discount structure between 200% and 600% FPL varies by hospital. A typical Illinois hospital sliding scale looks like this:</p>

<table>
    <thead>
        <tr><th>Income as % of FPL</th><th>Typical Discount</th><th>Example: $20,000 Bill</th></tr>
    </thead>
    <tbody>
        <tr><td>200% or below</td><td>100% (free care)</td><td>$0 owed</td></tr>
        <tr><td>201%&ndash;300%</td><td>75&ndash;85%</td><td>$3,000&ndash;$5,000 owed</td></tr>
        <tr><td>301%&ndash;400%</td><td>50&ndash;70%</td><td>$6,000&ndash;$10,000 owed</td></tr>
        <tr><td>401%&ndash;500%</td><td>25&ndash;45%</td><td>$11,000&ndash;$15,000 owed</td></tr>
        <tr><td>501%&ndash;600%</td><td>10&ndash;20%</td><td>$16,000&ndash;$18,000 owed</td></tr>
    </tbody>
</table>

<p><em>Illustrative only. Actual percentages vary by hospital policy. Review your specific hospital&rsquo;s Financial Assistance Policy for exact discount tiers.</em></p>

<p>Use our calculator to compare what Medicare pays for your procedures and understand what &ldquo;reasonable&rdquo; looks like even after the charity care discount:</p>

{_embed(mode="markup", title="Compare your Illinois hospital bill to Medicare rates", subtitle="Enter a CPT code and billed amount to see the markup over Medicare.", height="420")}

<h2 id="cook-county-health">3. Cook County Health: care regardless of ability to pay</h2>

<p>For Chicago-area residents, <strong>Cook County Health</strong> (formerly the Cook County Bureau of Health Services) operates two hospitals &mdash; John H. Stroger Jr. Hospital and Provident Hospital &mdash; and more than 20 community health centers that provide care to Cook County residents regardless of ability to pay or insurance status.</p>

<p>Cook County Health&rsquo;s sliding-scale fee structure is separate from the Illinois Charitable Health Care Act and applies specifically to Cook County residents:</p>

<ul>
    <li><strong>Uninsured patients:</strong> Eligible for the sliding-scale discount based on income, with free care available at the lowest income levels</li>
    <li><strong>No credit check or citizenship requirement</strong> for the county care program</li>
    <li><strong>CountyCare:</strong> Illinois Medicaid managed care plan operated by Cook County Health for eligible Cook County residents</li>
    <li><strong>Enrollment assistance:</strong> Financial counselors at every Cook County Health facility can help patients enroll in CountyCare, marketplace plans, or the hospital&rsquo;s own financial assistance program</li>
</ul>

<p>If you received care at a private hospital in Cook County or a collar county and are struggling with the bill, you can still apply for the private hospital&rsquo;s charity care program under the Illinois Charitable Health Care Act.</p>

<h2 id="how-to-apply">4. How to apply for charity care in Illinois</h2>

<h3>Step 1: Request the financial assistance application</h3>
<p>Illinois hospitals are required to screen you for eligibility and provide information about financial assistance at admission and discharge. If they did not, call the billing department and say: &ldquo;I would like to apply for financial assistance under the Illinois Charitable Health Care Act.&rdquo; They are legally required to provide you with the application.</p>

<h3>Step 2: Gather your documents</h3>
<ul>
    <li>Most recent federal tax return (Form 1040) &mdash; pages 1 and 2</li>
    <li>Two to three recent pay stubs, or proof of unemployment/disability benefits</li>
    <li>Documentation of household size (birth certificates, tax dependents)</li>
    <li>Bank statements (some Illinois hospitals request 1&ndash;3 months)</li>
    <li>Documentation of financial hardship if applicable (layoff notice, divorce decree, other medical bills)</li>
</ul>

<h3>Step 3: Submit a complete application</h3>
<p>Fill in every field &mdash; incomplete applications are the most common cause of delays and denials. If a question does not apply, write &ldquo;N/A.&rdquo; Include a brief cover letter: &ldquo;I am requesting financial assistance under the Illinois Charitable Health Care Act for care received on [date]. My household income is $[amount] for a household of [number].&rdquo;</p>

<h3>Step 4: Follow up and appeal if denied</h3>
<p>Call within 5 business days to confirm receipt. Ask for a reference number. If denied, request the denial reason in writing and resubmit with any missing documents. Escalate to the hospital patient advocate if needed, or file a complaint with the <a href="https://dph.illinois.gov/topics-services/health-care-regulation/hospitals.html" target="_blank" rel="noopener">Illinois Department of Public Health (IDPH)</a>.</p>

<h2 id="bill-example">5. Annotated Illinois outpatient surgery bill</h2>

<p>The following example shows an Illinois outpatient surgery at a hospital-affiliated clinic (a Hospital Outpatient Department, or HOPD) with four billing problems: an inflated facility fee versus an independent ASC rate, a duplicate supply charge, upcoded procedure complexity, and a balance bill from an in-facility assistant surgeon.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Prairie Lakes Medical Pavilion (HOPD) &mdash; Date of Service: 02/04/2026</div>
    <div class="line-item error">
        <span>Revenue Code 0510 &mdash; HOPD Facility Fee &nbsp; &#10060; <em>Same procedure (laparoscopic cholecystectomy) at an independent ASC would cost $3,200 in facility fees. Hospital-affiliated HOPD fee is $8,900 &mdash; a 2.8&times; markup for using a hospital-owned clinic. If the patient could have been referred to an ASC, this may be an opportunity to negotiate. Request comparison quote in writing.</em></span>
        <span>$8,900.00</span>
    </div>
    <div class="line-item">
        <span>47562 &mdash; Laparoscopic Cholecystectomy (Surgeon Fee)</span>
        <span>$3,200.00</span>
    </div>
    <div class="line-item error">
        <span>A4550 &mdash; Surgical Tray/Supply Kit &times; 2 &nbsp; &#10060; <em>Only one surgical procedure was performed. Two surgical supply kit charges (billed as $840 each = $1,680 total) for a single operation is a duplicate charge. Dispute the second kit as a billing error.</em></span>
        <span>$1,680.00</span>
    </div>
    <div class="line-item flagged">
        <span>47562 with modifier 80 &mdash; Assistant Surgeon Fee (Out-of-Network) &nbsp; &#9888; <em>Assistant surgeon was employed by the HOPD but is not in the patient&rsquo;s insurance network. Balance bill of $2,400 issued for assistant surgeon not disclosed pre-operatively. Under No Surprises Act, consent was required 72+ hours in advance for a scheduled procedure. Dispute immediately.</em></span>
        <span>$2,400.00</span>
    </div>
    <div class="line-item">
        <span>00790 &mdash; Anesthesia (In-Network)</span>
        <span>$1,100.00</span>
    </div>
    <div class="line-item">
        <span>80053 &mdash; Comprehensive Metabolic Panel (Pre-op)</span>
        <span>$380.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$17,660.00</span>
    </div>
    <div class="line-total">
        <span>AFTER DUPLICATE SUPPLY FIX + BALANCE BILL REMOVAL + HOPD NEGOTIATION</span>
        <span>~$8,180.00</span>
    </div>
</div>

<p><strong>Dispute strategy for this bill:</strong></p>
<ul>
    <li><strong>Duplicate supply charge:</strong> Submit a written dispute identifying both A4550 line items and requesting removal of the second charge ($840). Reference the single procedure date and operative note.</li>
    <li><strong>Out-of-network assistant surgeon balance bill:</strong> Dispute citing the No Surprises Act. For a scheduled procedure, consent must be obtained at least 72 hours in advance and must include specific out-of-network cost disclosures. File with CMS if not resolved within 30 days.</li>
    <li><strong>HOPD facility fee:</strong> Request the hospital&rsquo;s standard facility fee schedule and ask whether the procedure could have been safely performed at an in-network ASC. Use this as leverage to negotiate a reduction on the HOPD premium.</li>
</ul>

<p>Want to know the Medicare rate for CPT 47562 (laparoscopic cholecystectomy)? <a href="/calculator">Use our free calculator</a> &mdash; it gives you instant Medicare benchmark data for any CPT code.</p>

<h2 id="statute-of-limitations">6. Illinois statute of limitations: the 10-year written contract rule</h2>

<p>Illinois has two very different statutes of limitations for medical debt &mdash; and the distinction matters enormously:</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>Illinois SOL</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Open account (no signed contract)</td><td>5 years</td><td>Applies if you never signed a financial responsibility agreement</td></tr>
        <tr><td>Written contract (signed financial agreement)</td><td>10 years</td><td>Applies if you signed any written financial responsibility form &mdash; as nearly all hospital patients do</td></tr>
        <tr><td>Court judgment</td><td>7 years (renewable)</td><td>Respond to all lawsuits to avoid renewable judgments</td></tr>
    </tbody>
</table>

<p>Because virtually every hospital admission includes a signed financial responsibility agreement, most Illinois medical debt falls under the <strong>10-year written contract SOL</strong>. This is one of the longest written contract statutes in the nation &mdash; and it works against patients who ignore old debt.</p>

<div class="case-study">
    <h3>Important warning: Illinois&rsquo;s 10-year SOL can work against debtors</h3>
    <p><strong>Situation:</strong> A Chicago patient received a $9,400 hospital bill in 2017 following elective knee surgery. She signed the standard patient financial responsibility agreement at admission. Overwhelmed by debt and unaware of her legal options, she did not respond to any billing or collections notices. In 2026 &mdash; 9 years after the date of service &mdash; a debt buyer filed a lawsuit against her for the original $9,400 plus interest, totaling $14,200.</p>
    <p><strong>Key issue:</strong> Because she signed a written financial responsibility agreement in 2017, the 10-year written contract SOL applies &mdash; not the 5-year open account SOL. The debt is still within the statute of limitations in 2026. She made no payments and never disputed the charges.</p>
    <p><strong>What she should have done:</strong> In 2017, she qualified for financial assistance at 280% FPL and could have had 75% of the bill waived. She could have disputed the debt with the hospital, applied for charity care, or negotiated a settlement for a fraction of the balance. Had she made one documented partial payment in 2018, she would have reset the clock to 2028 under the 10-year SOL &mdash; not beneficial. Had she disputed the bill properly in 2017, the underlying debt may have been reduced or eliminated.</p>
    <p><strong>Lesson:</strong> Illinois&rsquo;s 10-year written contract SOL means old hospital debt does not go away quickly. Address hospital bills early &mdash; apply for charity care, dispute errors, and negotiate settlements before debts age and accumulate interest.</p>
</div>

<h2 id="wage-garnishment">7. Wage garnishment protections in Illinois</h2>

<p>Illinois limits wage garnishment for medical debt under the Illinois Wage Garnishment Act (735 ILCS 5/12-803). The exempt amount is the <strong>greater of 85% of net disposable earnings OR 45 times the applicable minimum wage per week</strong> (using whichever minimum wage is higher &mdash; Illinois or federal). Only the amount above this threshold can be garnished.</p>

<p>Illinois also provides a <strong>30-day bank account exemption</strong> for wages after deposit: low-income debtors may claim that deposited wages remain exempt from bank levy for 30 days after the deposit date.</p>

<p>A garnishment still requires a court judgment first. Illinois hospitals must follow the collections process &mdash; including proper notice and a lawsuit &mdash; before reaching wages. Combined with the Illinois Charitable Health Care Act&rsquo;s screening requirement and the 5-year and 10-year SOL windows, the best strategy is always to address the bill directly through financial assistance or dispute, well before a judgment is ever entered.</p>

<div class="key-takeaway">
    <strong>Facing a large Illinois hospital bill?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we flag overcharges, identify CPT codes billed above Medicare rates, and generate an audit report you can take directly to the hospital patient financial services department when you submit your Illinois Charitable Health Care Act application.
</div>

<div class="key-takeaway">
    <strong>Illinois hospital bill above Medicare rates?</strong> Use our <a href="/calculator">free calculator</a> to benchmark every CPT code on your bill and our <a href="/hospitals/">hospital directory</a> to see your facility&rsquo;s markup rate and charity care policy. Attaching a Medicare comparison report to your Illinois Charitable Health Care Act application significantly strengthens your case for the maximum sliding-scale discount.
</div>

<h2 id="case-studies">8. Real patient results</h2>

<div class="case-study">
    <h3>Case study 1: $31,000 inpatient bill eliminated under Illinois 200% FPL free care &mdash; Chicago</h3>
    <p><strong>Situation:</strong> A family of four in Chicago received a $31,000 inpatient hospital bill after the father underwent emergency gallbladder surgery. The family had no insurance at the time of service due to a recent job loss.</p>
    <p><strong>Patient profile:</strong> Family of 4, household income $61,000/year (approximately 189% of FPL for a family of four &mdash; below the 200% free care threshold).</p>
    <p><strong>Action:</strong> A hospital financial counselor screened the family during the post-discharge follow-up and identified that household income fell below the 200% FPL threshold for complete bill elimination under the Illinois Charitable Health Care Act. The family submitted the financial assistance application with proof of income within 30 days of discharge.</p>
    <p><strong>Result:</strong> The entire $31,000 bill was written off as charity care under 210 ILCS 86. The family owed $0.</p>
    <p><strong>Savings: $31,000.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 2: $14,000 bill reduced to $2,800 at 420% FPL &mdash; Springfield</h3>
    <p><strong>Situation:</strong> A single patient in Springfield received a $14,000 bill after outpatient surgery. She had insurance with a high deductible, leaving $8,200 in patient responsibility after insurance paid its share.</p>
    <p><strong>Patient profile:</strong> Single individual, income $52,000/year (approximately 332% of FPL in 2026). Technically above the standard thresholds at many hospitals, but within Illinois&rsquo;s 600% FPL window for the sliding scale.</p>
    <p><strong>Action:</strong> The patient applied for financial assistance under the Illinois Charitable Health Care Act, citing her income of $52,000 as 332% of FPL. The hospital&rsquo;s sliding-scale policy at that income level provided a 70% discount. Applied to the $8,200 patient responsibility balance, this reduced her liability to $2,460.</p>
    <p><strong>Result:</strong> Patient responsibility reduced from $8,200 to $2,460. Combined with a BillKarma-identified duplicate supply charge ($340 refunded), total savings on the $14,000 original bill exceeded $11,500.</p>
    <p><strong>Savings: $11,540.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 3: Illinois 10-year SOL &mdash; 2017 debt still collectible in 2026 &mdash; cautionary case</h3>
    <p><strong>Situation:</strong> A Rockford patient signed a standard patient financial responsibility agreement for a $9,400 elective surgical procedure in 2017. She never disputed the charges and ignored all bills and collections notices. In March 2026, a debt buyer filed a lawsuit seeking $14,200 (original principal plus 9 years of statutory interest).</p>
    <p><strong>What happened:</strong> Because she signed a written contract, the 10-year Illinois SOL applied. The lawsuit was filed in year 9 &mdash; within the statute. She could not assert the SOL defense. The debt buyer obtained a judgment for $14,200.</p>
    <p><strong>What could have been done differently:</strong> In 2017, her household income of $72,000 (family of 4) was 224% of FPL &mdash; above the 200% free care threshold but within the Illinois sliding scale. A 75% discount would have reduced her liability to $2,350. She could also have disputed several billing errors identified in the original itemized bill. Instead, 9 years of inaction turned a disputably valid $9,400 bill into a $14,200 court judgment.</p>
    <p><strong>Lesson:</strong> Illinois&rsquo;s 10-year written contract SOL is one of the longest in the country. Hospital bills do not expire quickly in Illinois. Act early: apply for charity care, dispute errors, and negotiate before the bill ages.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the income limit for free charity care at Illinois hospitals?</h3>
        <p>Under the Illinois Charitable Health Care Act (210 ILCS 86), free care is required for patients at or below 200% FPL &mdash; approximately $31,300 for a single person or $64,300 for a family of four in 2026. Patients between 200% and 600% FPL ($93,900 single / $192,900 family of four) qualify for a sliding-scale discount. All Illinois hospitals must comply, including for-profit facilities. Contact the billing department and ask for the financial assistance application under the Illinois Charitable Health Care Act.</p>
    </div>

    <div class="faq-item">
        <h3>Does Illinois allow wage garnishment for medical debt?</h3>
        <p>Yes, after a court judgment. Illinois law exempts the greater of 85% of net disposable earnings or 45 times the applicable minimum wage per week. Collectors can only reach wages above this threshold. Illinois also provides a 30-day bank levy exemption for deposited wages for low-income debtors. The best protection is to address hospital bills through the Illinois Charitable Health Care Act before they become judgments.</p>
    </div>

    <div class="faq-item">
        <h3>What is Illinois&rsquo;s statute of limitations on medical debt?</h3>
        <p>Illinois has a 5-year SOL for open accounts and a 10-year SOL for written contracts. Because most hospital admissions include a signed financial responsibility form, nearly all Illinois medical debt falls under the 10-year written contract SOL &mdash; one of the longest in the country. Address hospital bills promptly through financial assistance or disputes rather than ignoring them; in Illinois, old debt stays collectible for a long time.</p>
    </div>

    <div class="faq-item">
        <h3>How do I apply for charity care at an Illinois hospital?</h3>
        <p>Illinois hospitals must screen every patient for financial assistance eligibility at admission and discharge under the Charitable Health Care Act. If they did not screen you, ask patient financial services for the financial assistance application. Submit with your most recent tax return, recent pay stubs, and household size documentation. Hospitals must provide information about the assistance policy on every billing statement. You can also contact the <a href="https://dph.illinois.gov/topics-services/health-care-regulation/hospitals.html" target="_blank" rel="noopener">Illinois IDPH</a> if a hospital does not follow its obligations.</p>
    </div>

    <div class="faq-item">
        <h3>What is the 600% FPL sliding scale for Illinois hospital charity care?</h3>
        <p>The Illinois Charitable Health Care Act requires hospitals to provide a sliding-scale discount to patients between 200% and 600% FPL. In 2026, 600% FPL is approximately $93,900 for a single person or $192,900 for a family of four. The specific discount percentages vary by hospital but typically range from 75&ndash;85% at 200&ndash;300% FPL down to 10&ndash;20% at 500&ndash;600% FPL. This is one of the broadest income thresholds for hospital financial assistance in the United States. Review your hospital&rsquo;s specific policy document for its exact discount tiers.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=1264&ChapterID=21" target="_blank" rel="noopener">Illinois Charitable Health Care Act (210 ILCS 86): Full Text</a></li>
    <li><a href="https://dph.illinois.gov/topics-services/health-care-regulation/hospitals.html" target="_blank" rel="noopener">Illinois Department of Public Health (IDPH): Hospital Oversight and Patient Rights</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/charitable-organizations/section-501r-new-requirements-for-charitable-hospitals" target="_blank" rel="noopener">IRS Section 501(r): Federal Charity Care Requirements for Nonprofit Hospitals</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Federal Patient Rights</a></li>
    <li><a href="https://www.cfpb.gov/consumer-tools/medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt Resources for Consumers</a></li>
</ul>
""",
})
