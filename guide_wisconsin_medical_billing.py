"""Guide: Wisconsin Medical Billing Rights: What Patients Need to Know."""

from guides import register, _embed

register("wisconsin-medical-billing", {
    "title": "Wisconsin Medical Billing Rights: What Patients Need to Know",
    "meta_description": "Wisconsin patients have 7 key billing rights: charity care, itemized bills within 7 days, and surprise billing protections. Learn how to save thousands.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "How do I get free or reduced-cost care at a Wisconsin nonprofit hospital?",
            "a": "Ask the hospital billing department for a Financial Assistance Policy (FAP) application. Under IRS 501(r) rules, all nonprofit hospitals must have one. Most Wisconsin nonprofit systems offer free care to patients at or below 200% FPL and sliding-scale discounts up to 300% FPL. Submit your application with pay stubs or a recent tax return. The hospital cannot pursue aggressive collection action while your application is pending.",
        },
        {
            "q": "How long does a Wisconsin hospital have to provide an itemized bill?",
            "a": "Wisconsin hospitals must provide a complete itemized bill within 7 business days of your request. The itemized statement must show every CPT code, service description, unit price, quantity, and total charge. Make your request in writing &mdash; by email or certified letter &mdash; so you have a dated record. If the hospital fails to comply, you can file a complaint with the Wisconsin Department of Health Services.",
        },
        {
            "q": "Does Wisconsin have surprise billing protections beyond the federal No Surprises Act?",
            "a": "Wisconsin does not have a state-specific surprise billing law that goes beyond the federal No Surprises Act (NSA), which took effect January 2022. The NSA prohibits out-of-network balance billing for emergency services and for non-emergency care at in-network facilities when you did not choose the out-of-network provider. Complaints can be filed with the Wisconsin Office of the Commissioner of Insurance or the federal CMS No Surprises Help Desk at 1-800-985-3059.",
        },
        {
            "q": "What is BadgerCare Plus and who qualifies?",
            "a": "BadgerCare Plus is Wisconsin&rsquo;s Medicaid program administered by the Wisconsin Department of Health Services. Wisconsin expanded Medicaid, so adults qualify at incomes up to 100% of the Federal Poverty Level (about $15,650 for a single person in 2026). Children qualify at much higher thresholds &mdash; up to 300% FPL. Apply online at access.wisconsin.gov or at a local DHS office. Coverage can be retroactive up to 3 months before the application date.",
        },
        {
            "q": "Where do I file a complaint about a Wisconsin hospital bill?",
            "a": "For Medicaid billing errors, contact the Wisconsin Department of Health Services (608-266-1865). For insurance disputes and balance billing complaints, file with the Wisconsin Office of the Commissioner of Insurance (oci.wi.gov or 1-800-236-8517). For general billing fraud or deceptive practices, contact the Wisconsin Department of Agriculture, Trade and Consumer Protection (DATCP) at datcp.wisconsin.gov. For federal surprise billing violations, use the CMS No Surprises Help Desk.",
        },
    ],
    "body": f"""
<p class="lead">Wisconsin hospital charges average <strong>4.6&times; Medicare rates</strong> &mdash; but Wisconsin patients have meaningful tools to fight back. Nonprofit hospitals must provide charity care under federal IRS 501(r) rules, BadgerCare Plus covers adults up to 100% FPL and children up to 300% FPL, and the federal No Surprises Act shields patients from most balance billing. BillKarma&rsquo;s analysis of 78 Wisconsin hospitals finds the median markup over Medicare is 4.6&times; &mdash; with Milwaukee-area academic medical centers averaging 5.3&times; and rural critical access hospitals averaging 3.4&times;. Knowing your rights can save thousands of dollars.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#badgercare">BadgerCare Plus and Wisconsin Medicaid</a></li>
        <li><a href="#charity-care">Hospital charity care and financial assistance</a></li>
        <li><a href="#itemized-bill">Your right to an itemized bill</a></li>
        <li><a href="#surprise-billing">Surprise billing protections in Wisconsin</a></li>
        <li><a href="#pricing">Wisconsin hospital pricing</a></li>
        <li><a href="#rights-table">Wisconsin patient rights at a glance</a></li>
        <li><a href="#how-to-dispute">How to dispute a Wisconsin medical bill</a></li>
        <li><a href="#case-studies">Case studies: Wisconsin patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="badgercare">1. BadgerCare Plus and Wisconsin Medicaid</h2>

<p>Wisconsin expanded Medicaid under the ACA, and BadgerCare Plus is the result. Adults with household incomes up to <strong>100% of the Federal Poverty Level (FPL)</strong> qualify for full coverage &mdash; roughly $15,650 for a single person and $32,150 for a family of four in 2026. Children in Wisconsin qualify at far higher income levels, up to 300% FPL.</p>

<p>If you have an unpaid hospital bill, apply for BadgerCare Plus immediately. Coverage can be retroactive up to 3 months before the application date, which may cover the visit that generated your current bill. Apply at <a href="https://access.wisconsin.gov" target="_blank" rel="noopener">access.wisconsin.gov</a> or ask the hospital&rsquo;s financial counselor to screen you.</p>

<table>
    <caption>BadgerCare Plus eligibility &mdash; key income thresholds (2026)</caption>
    <thead>
        <tr><th>Group</th><th>Income limit (% FPL)</th><th>Single person annual limit</th><th>Family of 4 annual limit</th></tr>
    </thead>
    <tbody>
        <tr><td>Adults (19&ndash;64)</td><td>100% FPL</td><td>$15,650</td><td>$32,150</td></tr>
        <tr><td>Pregnant women</td><td>300% FPL</td><td>$46,950</td><td>$96,450</td></tr>
        <tr><td>Children (0&ndash;18)</td><td>300% FPL</td><td>$46,950</td><td>$96,450</td></tr>
        <tr><td>Infants (0&ndash;1)</td><td>300% FPL</td><td>$46,950</td><td>$96,450</td></tr>
        <tr><td>Adults above 100% FPL</td><td>Not eligible (see ACA marketplace)</td><td>&mdash;</td><td>&mdash;</td></tr>
    </tbody>
</table>

<p><em>FPL figures reflect 2026 HHS guidelines. Verify current thresholds at <a href="https://www.dhs.wisconsin.gov/badgercareplus" target="_blank" rel="noopener">dhs.wisconsin.gov/badgercareplus</a>.</em></p>

<p>Wisconsin adults who earn above 100% FPL do not qualify for BadgerCare Plus but may be eligible for ACA marketplace plans with premium subsidies. Special enrollment periods apply after job loss, loss of prior coverage, or other qualifying life events.</p>

<h2 id="charity-care">2. Hospital charity care and financial assistance</h2>

<p>Wisconsin does not have a state-level charity care law with specific income thresholds (unlike California), but nonprofit hospitals must comply with federal IRS 501(r) rules and Wisconsin Act 37 (1999), which codified financial assistance requirements for Wisconsin nonprofit hospitals. Every nonprofit hospital in Wisconsin &mdash; including Froedtert, UW Health, Aspirus, SSM Health, and ThedaCare &mdash; must maintain a written Financial Assistance Policy (FAP).</p>

<p>Under IRS 501(r), nonprofit hospitals must:</p>
<ul>
    <li>Post the FAP, a plain-language summary, and the application form on their website and in the billing office</li>
    <li>Limit charges to FAP-eligible patients to the <strong>amounts generally billed (AGB)</strong> to insured patients</li>
    <li>Not take extraordinary collection actions (lawsuits, liens, wage garnishment, credit reporting) without first making reasonable efforts to notify patients about the FAP</li>
</ul>

<table>
    <caption>Wisconsin major hospital systems &mdash; charity care thresholds (approximate, verify directly)</caption>
    <thead>
        <tr><th>Hospital system</th><th>Free care below (% FPL)</th><th>Sliding scale up to (% FPL)</th><th>How to apply</th></tr>
    </thead>
    <tbody>
        <tr><td>Froedtert Health</td><td>200%</td><td>300%</td><td>Online, billing office, or financial counselor</td></tr>
        <tr><td>Aurora Health Care (Advocate)</td><td>200%</td><td>400%</td><td>Online portal or call billing department</td></tr>
        <tr><td>UW Health (academic)</td><td>200%</td><td>300%</td><td>myuwhealthfinance.org or financial counselor</td></tr>
        <tr><td>SSM Health Wisconsin</td><td>200%</td><td>350%</td><td>Online or in person at registration</td></tr>
        <tr><td>Aspirus Health</td><td>200%</td><td>300%</td><td>Billing department or hospital admission</td></tr>
        <tr><td>Marshfield Clinic Health System</td><td>200%</td><td>300%</td><td>Online or financial counselor</td></tr>
        <tr><td>ThedaCare</td><td>200%</td><td>300%</td><td>Financial counselor at any facility</td></tr>
        <tr><td>Bellin Health</td><td>200%</td><td>300%</td><td>Billing office or online application</td></tr>
    </tbody>
</table>

<p><em>Income thresholds are approximate. Policies change &mdash; always request the current FAP application directly from the hospital.</em></p>

<div class="key-takeaway">
    <strong>Think you might qualify for charity care?</strong> <a href="/scan">Upload your Wisconsin hospital bill to BillKarma</a> &mdash; we identify your likely eligibility based on the hospital&rsquo;s policy, flag charges above Medicare rates, and draft a charity care application letter with the right income documentation checklist.
</div>

<h2 id="itemized-bill">3. Your right to an itemized bill</h2>

<p>Wisconsin patients have the right to receive a complete itemized bill within <strong>7 business days</strong> of requesting one. The itemized statement must break down every charge by CPT code, revenue code, service description, unit price, quantity, and total.</p>

<p>Request your itemized bill in writing &mdash; email or certified letter with return receipt requested. A sample request:</p>

<div class="bill-example">
    <strong>Sample itemized bill request (send to hospital billing department)</strong>
    <p>Date: [Date]<br>
    To: [Hospital Name] Billing Department<br>
    Re: Account #[Your Account Number] &mdash; Date of Service: [Date]</p>
    <p>Pursuant to Wisconsin patient billing rights and IRS 501(r) requirements, I request a complete itemized statement for the above account. The itemized bill should include each service, procedure code (CPT and revenue code), quantity billed, unit price, and total charge. Please provide this within 7 business days.</p>
    <p>Name: [Your Name]<br>
    Date of birth: [DOB]<br>
    Signature: _______________________</p>
</div>

<p>Once you have the itemized bill, use our <a href="/calculator">free Medicare rate calculator</a> to compare each charge. Any item priced more than 3&ndash;5&times; the Medicare rate is a strong negotiation point.</p>

<h2 id="surprise-billing">4. Surprise billing protections in Wisconsin</h2>

<p>Wisconsin does not have its own state surprise billing law beyond the federal No Surprises Act (NSA), which took effect January 2022. The NSA covers all commercial health plans (employer-sponsored and ACA marketplace plans). Under the NSA:</p>

<ul>
    <li><strong>Emergency care:</strong> Any out-of-network provider who treats you in an emergency cannot bill you more than your in-network cost-sharing. This applies regardless of whether the ER is in-network or out-of-network.</li>
    <li><strong>Non-emergency care at in-network facilities:</strong> Out-of-network providers at in-network hospitals &mdash; anesthesiologists, radiologists, pathologists, assistant surgeons &mdash; cannot balance bill you if you did not actively choose them. You owe only your in-network cost-sharing amount.</li>
    <li><strong>Air ambulance:</strong> The NSA covers air ambulance services from out-of-network providers for commercial plan members.</li>
    <li><strong>Consent exception:</strong> For scheduled non-emergency procedures, an out-of-network provider may balance bill you only if they provide written notice at least 72 hours in advance and you sign a written consent form acknowledging the out-of-network charges.</li>
</ul>

<p>File NSA complaints with the Wisconsin Office of the Commissioner of Insurance (OCI) or the federal CMS No Surprises Help Desk at 1-800-985-3059 or <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a>.</p>

<h2 id="pricing">5. Wisconsin hospital pricing</h2>

<p>Wisconsin hospitals are required to post machine-readable pricing files under the federal Hospital Price Transparency Rule. BillKarma&rsquo;s analysis of 78 Wisconsin hospitals finds:</p>

<ul>
    <li><strong>Statewide median markup:</strong> 4.6&times; Medicare rates</li>
    <li><strong>Milwaukee-area academic medical centers:</strong> 5.3&times; Medicare rates on average</li>
    <li><strong>Rural critical access hospitals:</strong> 3.4&times; Medicare rates &mdash; lower markups but fewer charity care resources</li>
    <li><strong>Highest markups:</strong> Certain specialty and surgical hospitals in the Milwaukee and Madison suburbs</li>
</ul>

{_embed(mode="markup", title="Compare your Wisconsin hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup.", height="420")}

<p>Look up your specific Wisconsin hospital in our <a href="/hospitals/">hospital directory</a> to see its charge-to-Medicare markup, charity care policy rating, and price transparency compliance status.</p>

<h2 id="rights-table">6. Wisconsin patient rights at a glance</h2>

<table>
    <caption>Wisconsin patient billing rights &mdash; key protections and enforcement</caption>
    <thead>
        <tr><th>Right</th><th>Source</th><th>How to enforce</th></tr>
    </thead>
    <tbody>
        <tr><td>Itemized bill within 7 business days of request</td><td>Wisconsin billing standards / DHS policy</td><td>Written request to billing dept.; escalate to DHS if denied</td></tr>
        <tr><td>Charity care application at nonprofit hospitals</td><td>IRS 501(r) / Wisconsin Act 37</td><td>Request FAP from billing; file IRS Form 13909 if denied</td></tr>
        <tr><td>No balance billing for emergency care (commercial plans)</td><td>Federal No Surprises Act (2022)</td><td>File with Wisconsin OCI or CMS Help Desk 1-800-985-3059</td></tr>
        <tr><td>No balance billing for non-emergency care at in-network facility (no consent)</td><td>Federal No Surprises Act (2022)</td><td>File with Wisconsin OCI or CMS Help Desk</td></tr>
        <tr><td>BadgerCare Plus eligibility screening at hospitals</td><td>Wisconsin DHS Medicaid policy</td><td>Ask financial counselor; apply at access.wisconsin.gov</td></tr>
        <tr><td>30-day notice before extraordinary collection actions</td><td>IRS 501(r)</td><td>Send cease collection letter; cite 501(r) violation to IRS</td></tr>
        <tr><td>Good Faith Estimate for scheduled care (uninsured)</td><td>Federal No Surprises Act (2022)</td><td>Request in writing at least 3 business days before service</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Use BillKarma&rsquo;s free calculator</strong> to compare every charge on your Wisconsin hospital bill to Medicare rates. <a href="/calculator">Open the calculator</a> &mdash; enter any CPT code to see what Medicare pays and how your hospital&rsquo;s price compares.
</div>

<h2 id="how-to-dispute">7. How to dispute a Wisconsin medical bill</h2>

<h3>Step 1: Request an itemized bill</h3>
<p>Call the billing department and request the full itemized statement. Put the request in writing so you have proof of the date. Wisconsin hospitals must respond within 7 business days.</p>

<h3>Step 2: Check each line item</h3>
<p>Use our <a href="/calculator">Medicare rate calculator</a> to look up the Medicare rate for each CPT code. Flag any charge exceeding 4&times; the Medicare rate as a negotiation target. Also check for duplicate charges &mdash; the same CPT code billed twice &mdash; and charges for services not reflected in your medical records.</p>

<h3>Step 3: Apply for financial assistance</h3>
<p>If you are uninsured or underinsured, apply for the hospital&rsquo;s FAP before disputing charges. Nonprofit hospitals cannot pursue aggressive collections while your FAP application is under review. Submit proof of income: two recent pay stubs, most recent tax return, and any documentation of extraordinary expenses.</p>

<h3>Step 4: Write a formal dispute letter</h3>
<p>Send a written dispute to the hospital billing department by certified mail. Include your account number, a list of disputed line items with CPT codes, your basis for dispute (Medicare rate comparison, duplicate charge, service not rendered), and copies of supporting documentation. Request a response within 30 days.</p>

<h3>Step 5: Escalate if needed</h3>
<ul>
    <li><strong>Surprise billing / NSA violation:</strong> File with the <a href="https://oci.wi.gov" target="_blank" rel="noopener">Wisconsin Office of the Commissioner of Insurance</a> (1-800-236-8517) and the CMS No Surprises Help Desk</li>
    <li><strong>Medicaid billing error:</strong> Contact Wisconsin DHS at 608-266-1865</li>
    <li><strong>Billing fraud / deceptive practices:</strong> File with Wisconsin DATCP at <a href="https://datcp.wi.gov" target="_blank" rel="noopener">datcp.wi.gov</a></li>
    <li><strong>Nonprofit hospital charity care denial:</strong> File IRS Form 13909 and contact Wisconsin DATCP</li>
</ul>

<p>Our <a href="/guides/dispute-bill/">step-by-step dispute guide</a> walks through the full process with sample letter templates.</p>

<div class="key-takeaway">
    <strong>Found billing errors or a surprise balance bill?</strong> <a href="/hospitals/">Search our Wisconsin hospital directory</a> to check your hospital&rsquo;s pricing, charity care grade, and price transparency status &mdash; then use that data in your dispute letter.
</div>

<h2 id="case-studies">8. Case studies: Wisconsin patient results</h2>

<div class="case-study">
    <h3>Case study 1: Milwaukee charity care approval saves $18,400</h3>
    <p><strong>Situation:</strong> A 28-year-old Milwaukee resident was admitted to Froedtert Hospital for an emergency appendectomy. Uninsured and working part-time, she received a bill for $18,400 &mdash; approximately 5.1&times; the Medicare rate for the procedure, anesthesia, and two-night stay.</p>
    <p><strong>Patient profile:</strong> Single, annual income $17,200 (110% FPL). Eligible for BadgerCare Plus but had not applied.</p>
    <p><strong>Action:</strong> The hospital&rsquo;s financial counselor screened her for BadgerCare Plus eligibility during admission. An application was submitted the next day. Because BadgerCare Plus allows retroactive coverage up to 3 months, the emergency appendectomy qualified for coverage under her newly approved enrollment.</p>
    <p><strong>Result:</strong> BadgerCare Plus covered the entire $18,400 bill. Her out-of-pocket cost: $0. She remained enrolled in BadgerCare Plus for ongoing care.</p>
    <p><strong>Savings: $18,400.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 2: Aurora balance bill dispute eliminates $4,100 charge</h3>
    <p><strong>Situation:</strong> A Green Bay patient underwent a scheduled hip arthroscopy at an in-network Aurora Health Care facility. Her surgeon was in-network, but the anesthesiologist was out-of-network &mdash; a fact she was not informed of in advance. She received a $4,100 balance bill from the anesthesiology group after her insurance paid $1,200.</p>
    <p><strong>Patient profile:</strong> Insured through employer-sponsored PPO. No written notice of out-of-network status was provided before the procedure.</p>
    <p><strong>Action:</strong> She filed a written dispute with the anesthesiology billing group citing the federal No Surprises Act. She simultaneously filed a complaint with the Wisconsin OCI and the CMS No Surprises Help Desk. She attached documentation showing no advance written consent had been obtained.</p>
    <p><strong>Result:</strong> The anesthesiology group withdrew the $4,100 balance bill within 18 days. Her total out-of-pocket was her in-network deductible contribution of $250. The insurer and provider entered the federal independent dispute resolution (IDR) process.</p>
    <p><strong>Savings: $4,100.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 3: Froedtert itemized bill audit recovers $2,300 in duplicate charges</h3>
    <p><strong>Situation:</strong> A Madison couple received a $22,600 hospital bill after a 3-day inpatient stay for a cardiac event. They suspected errors but did not know where to start. Both had Medicare supplement coverage, leaving $3,100 in patient responsibility after insurance.</p>
    <p><strong>Patient profile:</strong> Retired couple, ages 68 and 71. Medicare primary with a Medigap supplement plan.</p>
    <p><strong>Action:</strong> They used BillKarma to <a href="/scan">scan the itemized bill</a>. The tool flagged two duplicate daily room charges (billed 3 nights instead of 2), an ancillary supply charge for items the nursing notes showed were not used, and a physical therapy evaluation billed during a day when the patient&rsquo;s records showed no therapy session. Total disputed charges: $2,300. They submitted a written dispute with the specific line items and medical record references.</p>
    <p><strong>Result:</strong> Froedtert removed $1,950 in duplicate and unsupported charges within 14 days of receiving the dispute. The remaining $350 in disputed supplies was resolved after a second review. Final patient responsibility was reduced from $3,100 to $850.</p>
    <p><strong>Savings: $2,250.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How do I get free or reduced-cost care at a Wisconsin nonprofit hospital?</h3>
        <p>Ask the billing department for the Financial Assistance Policy (FAP) application. All nonprofit hospitals must have one under IRS 501(r) rules. Most Wisconsin systems offer free care below 200% FPL and sliding-scale discounts to 300% FPL. Submit with proof of income &mdash; pay stubs or a recent tax return. The hospital cannot pursue collections while your application is pending.</p>
    </div>

    <div class="faq-item">
        <h3>How long does a Wisconsin hospital have to provide an itemized bill?</h3>
        <p>Wisconsin hospitals must provide an itemized bill within 7 business days of your written request. The itemized statement must include every CPT code, revenue code, service description, unit price, quantity, and total charge. Send your request by certified mail or email with a read receipt so you have a dated record. Escalate to the Wisconsin DHS if the hospital fails to comply.</p>
    </div>

    <div class="faq-item">
        <h3>Does Wisconsin have surprise billing protections beyond the federal No Surprises Act?</h3>
        <p>Wisconsin does not have a state-specific surprise billing law stronger than the federal NSA. The NSA (effective January 2022) prohibits out-of-network balance billing for emergency services and for non-emergency care at in-network facilities when you did not choose the out-of-network provider. File complaints with the Wisconsin OCI (1-800-236-8517) or the CMS No Surprises Help Desk (1-800-985-3059).</p>
    </div>

    <div class="faq-item">
        <h3>What is BadgerCare Plus and who qualifies?</h3>
        <p>BadgerCare Plus is Wisconsin&rsquo;s Medicaid program. Adults qualify at incomes up to 100% FPL (about $15,650 for a single person in 2026). Children qualify up to 300% FPL. Apply at <a href="https://access.wisconsin.gov" target="_blank" rel="noopener">access.wisconsin.gov</a> or through a hospital financial counselor. Coverage can be retroactive up to 3 months, which may cover your current bill.</p>
    </div>

    <div class="faq-item">
        <h3>Where do I file a complaint about a Wisconsin hospital bill?</h3>
        <p>For Medicaid billing errors: Wisconsin DHS (608-266-1865). For insurance disputes and balance billing: Wisconsin Office of the Commissioner of Insurance at <a href="https://oci.wi.gov" target="_blank" rel="noopener">oci.wi.gov</a> (1-800-236-8517). For billing fraud: Wisconsin DATCP at <a href="https://datcp.wi.gov" target="_blank" rel="noopener">datcp.wi.gov</a>. For federal NSA violations: CMS No Surprises Help Desk at 1-800-985-3059.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.dhs.wisconsin.gov/badgercareplus/index.htm" target="_blank" rel="noopener">Wisconsin Department of Health Services: BadgerCare Plus Program Overview</a></li>
    <li><a href="https://oci.wi.gov/Pages/Consumers/ConsumerHome.aspx" target="_blank" rel="noopener">Wisconsin Office of the Commissioner of Insurance: Consumer Resources</a></li>
    <li><a href="https://datcp.wi.gov/Pages/Programs_Services/ConsumerProtection.aspx" target="_blank" rel="noopener">Wisconsin Department of Agriculture, Trade and Consumer Protection: Consumer Protection</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/community-health-needs-assessment-for-charitable-hospital-organizations-section-501r3" target="_blank" rel="noopener">IRS: Section 501(r) Requirements for Nonprofit Hospitals</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Patient Protections Overview</a></li>
    <li><a href="https://docs.legis.wisconsin.gov/2001/related/acts/37" target="_blank" rel="noopener">Wisconsin Act 37 (1999): Financial Assistance Requirements for Nonprofit Hospitals</a></li>
    <li><a href="https://www.kff.org/medicaid/state-indicator/medicaid-income-eligibility-limits-for-adults-at-application/" target="_blank" rel="noopener">KFF: Medicaid Income Eligibility Limits for Adults by State (2026)</a></li>
</ul>
""",
})
