"""Guide: Oregon Medical Billing Rights."""

from guides import register, _embed

register("oregon-medical-billing", {
    "title": "Oregon Medical Billing Rights: Patient Protections Explained",
    "meta_description": "Oregon bans surprise billing, requires charity care up to 400% FPL, and offers free patient advocates. Learn Oregon's medical billing laws and how to use them.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Does Oregon have surprise billing protections?",
            "a": "Yes. Oregon&rsquo;s surprise billing ban (ORS 743B.524) predates the federal No Surprises Act and covers both emergency and non-emergency out-of-network billing at in-network facilities. Oregon patients also benefit from the federal No Surprises Act for any gaps. File complaints with the Oregon Insurance Division at oregoninsurance.org.",
        },
        {
            "q": "How do I get free help disputing a medical bill in Oregon?",
            "a": "Oregon runs a free Consumer Assistance Program (CAP) through the Oregon Health Authority (OHA). CAP advocates can help you understand your rights, file complaints, and negotiate with hospitals at no cost. Call 1-888-877-4894 or apply online at oregonhealthcare.gov/cap.",
        },
        {
            "q": "What income qualifies for Oregon hospital charity care?",
            "a": "Oregon nonprofit hospitals must provide free care to patients under 200% of the federal poverty level (about $29,160 for a single person in 2026) and discounted care on a sliding scale up to 400% FPL. Some hospitals like OHSU offer assistance up to 500% FPL. Ask for the hospital&rsquo;s Financial Assistance Policy (FAP) when you receive your bill.",
        },
        {
            "q": "How do I file a complaint about a hospital bill in Oregon?",
            "a": "For insurance and balance billing disputes, contact the Oregon Insurance Division at 1-888-877-4894. For hospital charity care denials and billing practices, file with the Oregon Health Authority. For billing fraud or consumer protection violations, contact the Oregon DOJ Consumer Protection Hotline at 1-877-877-9392.",
        },
        {
            "q": "Are Oregon hospital prices public?",
            "a": "Yes. All Oregon hospitals must comply with CMS price transparency rules and post machine-readable price files. Oregon also requires hospitals to publish their Financial Assistance Policies on their websites. The Oregon Health Authority publishes an annual Hospital Quality Report with cost and quality data.",
        },
    ],
    "body": f"""
<p class="lead">Oregon has some of the nation&rsquo;s strongest patient billing protections &mdash; a surprise billing ban (ORS 743B.524) that predates federal law, mandatory charity care up to 400% FPL at most nonprofit hospitals, and a <strong>free Consumer Assistance Program</strong> that provides billing advocates at no cost to Oregon patients. Yet BillKarma&rsquo;s analysis of 62 Oregon hospitals finds median hospital charges still average 4.2&times; the Medicare rate. Knowing Oregon&rsquo;s laws can save you thousands.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#surprise-billing">Oregon surprise billing law</a></li>
        <li><a href="#charity-care">Charity care requirements and how to apply</a></li>
        <li><a href="#real-bill">Annotated Oregon hospital bill</a></li>
        <li><a href="#consumer-assistance">Oregon Consumer Assistance Program (free advocates)</a></li>
        <li><a href="#major-hospitals">Oregon hospital systems and billing data</a></li>
        <li><a href="#complaints">How to file a complaint in Oregon</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="surprise-billing">1. Oregon surprise billing law</h2>

<p>Oregon enacted ORS 743B.524 years before the federal No Surprises Act took effect. The law prohibits out-of-network providers from billing Oregon patients more than their in-network cost-sharing when services are provided at an in-network facility &mdash; for both emergency and non-emergency care.</p>

<p>Under Oregon law, if you receive a surprise bill from an out-of-network provider at an in-network facility, you have the right to:</p>

<ul>
    <li>Pay only your in-network cost-sharing amount</li>
    <li>Have the insurer and provider resolve the payment difference through negotiation or arbitration</li>
    <li>File a complaint with the Oregon Insurance Division if the provider continues to bill you</li>
</ul>

<p>Oregon also requires providers to give patients a plain-language notice of their balance billing rights before scheduling non-emergency services at an in-network facility with potential out-of-network providers.</p>

<div class="key-takeaway">
    <strong>Received a surprise bill in Oregon?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we flag out-of-network charges and balance billing violations that may be protected under Oregon&rsquo;s surprise billing law.
</div>

<h2 id="charity-care">2. Charity care requirements and how to apply</h2>

<p>Oregon requires all nonprofit hospitals to provide financial assistance under both IRS 501(r) rules and Oregon state law (ORS 441.025). Oregon&rsquo;s rules are stronger than federal minimums &mdash; hospitals must notify patients of financial assistance availability, cannot require patients to apply for Medicaid as a condition of receiving charity care, and must respond to applications within 14 days.</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single (2026)</th><th>Family of Four (2026)</th><th>Typical Discount</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 200% FPL</td><td>Under $29,160</td><td>Under $60,000</td><td>100% (free care)</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$29,160&ndash;$43,740</td><td>$60,000&ndash;$90,000</td><td>50&ndash;75% discount</td></tr>
        <tr><td>300&ndash;400% FPL</td><td>$43,740&ndash;$58,320</td><td>$90,000&ndash;$120,000</td><td>25&ndash;50% discount</td></tr>
        <tr><td>Over 400% FPL</td><td>Over $58,320</td><td>Over $120,000</td><td>Varies by hospital</td></tr>
    </tbody>
</table>

<p><strong>To apply:</strong> Contact the hospital&rsquo;s financial counseling department and ask for a Financial Assistance Application. Oregon hospitals must respond within 14 days. You&rsquo;ll need proof of income, Oregon residency, and your itemized bill. If your application is denied, you have the right to appeal to the Oregon Health Authority.</p>

<h2 id="real-bill">3. Annotated Oregon hospital bill</h2>

<p>Here&rsquo;s a sample bill from an Oregon hospital for a patient who had a scheduled knee MRI followed by a cortisone injection, with an out-of-network radiologist reading the scan.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Providence St. Vincent Medical Center &mdash; Date of Service: 03/20/2026</div>
    <div class="line-item">
        <span>73721 &mdash; MRI knee without contrast</span>
        <span>$3,100</span>
    </div>
    <div class="line-item flagged">
        <span>26770 &mdash; Radiology interpretation (out-of-network radiologist) &nbsp; &#9888; <em>Provider billed $680; protected under ORS 743B.524 &mdash; you owe in-network rate only</em></span>
        <span>$680</span>
    </div>
    <div class="line-item">
        <span>20610 &mdash; Aspiration/injection, large joint (knee)</span>
        <span>$890</span>
    </div>
    <div class="line-item flagged">
        <span>J3301 &mdash; Triamcinolone injection &nbsp; &#9888; <em>Charged $215; average acquisition cost $4 &mdash; markup 54x</em></span>
        <span>$215</span>
    </div>
    <div class="line-item error">
        <span>99213 &mdash; Office visit, established patient &nbsp; &#10060; <em>Office visit billed separately; should be bundled with injection code 20610</em></span>
        <span>$180</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$5,065</span>
    </div>
</div>

<p>This bill has three issues: an out-of-network radiology charge protected by Oregon&rsquo;s surprise billing law, an extreme drug markup, and an unbundled office visit. Disputing all three could reduce this bill by $700&ndash;$1,200 depending on insurance.</p>

{_embed(mode="markup", title="Check your Oregon hospital charge", subtitle="Enter a CPT code and charged amount to compare against the Medicare rate.", height="420")}

<h2 id="consumer-assistance">4. Oregon Consumer Assistance Program (free advocates)</h2>

<p>Oregon is one of the few states that funds free patient advocates through the Oregon Health Authority&rsquo;s <strong>Consumer Assistance Program (CAP)</strong>. CAP navigators can:</p>

<ul>
    <li>Review your medical bills and EOBs for errors</li>
    <li>File insurance complaints on your behalf</li>
    <li>Help you apply for charity care or appeal a denial</li>
    <li>Negotiate directly with providers and insurers</li>
</ul>

<p>The service is free for all Oregon residents. Call <strong>1-888-877-4894</strong> or visit oregonhealthcare.gov/cap. Services are available in English, Spanish, and other languages through interpreter services.</p>

<div class="key-takeaway">
    <strong>Want to know if your bill was overcharged?</strong> Use our <a href="/calculator">free calculator</a> to look up what Medicare pays for any CPT code on your Oregon bill &mdash; then bring that data to your CAP advocate for a stronger negotiation.
</div>

<h2 id="major-hospitals">5. Oregon hospital systems and billing data</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care Max FPL</th></tr>
    </thead>
    <tbody>
        <tr><td>OHSU Health</td><td>Portland</td><td>5.1&times;</td><td>500% FPL sliding scale</td></tr>
        <tr><td>Legacy Health</td><td>Portland Metro</td><td>4.3&times;</td><td>400% FPL sliding scale</td></tr>
        <tr><td>Providence Health &amp; Services</td><td>Statewide</td><td>4.4&times;</td><td>400% FPL sliding scale</td></tr>
        <tr><td>PeaceHealth</td><td>Eugene/Springfield</td><td>3.9&times;</td><td>400% FPL sliding scale</td></tr>
        <tr><td>Adventist Health</td><td>Portland/Tillamook</td><td>4.0&times;</td><td>300% FPL sliding scale</td></tr>
        <tr><td>Samaritan Health Services</td><td>Mid-Willamette Valley</td><td>3.7&times;</td><td>400% FPL sliding scale</td></tr>
    </tbody>
</table>

<p>BillKarma&rsquo;s analysis of 62 Oregon hospitals finds the median markup over Medicare is 4.2&times;, with OHSU (academic medical center) at 5.1&times; and community hospitals averaging 3.8&times;. Use our <a href="/hospitals/">hospital directory</a> to see grades and markup data for specific Oregon hospitals near you.</p>

<h2 id="complaints">6. How to file a complaint in Oregon</h2>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing / balance billing</td><td>Oregon Insurance Division</td><td>oregoninsurance.org &mdash; 1-888-877-4894</td></tr>
        <tr><td>Insurance claim denial</td><td>Oregon Insurance Division</td><td>File online at oregoninsurance.org</td></tr>
        <tr><td>Charity care denial</td><td>Oregon Health Authority</td><td>oregon.gov/oha</td></tr>
        <tr><td>Consumer billing fraud</td><td>Oregon DOJ Consumer Protection</td><td>1-877-877-9392</td></tr>
        <tr><td>Oregon Health Plan (Medicaid)</td><td>Oregon Health Authority</td><td>1-800-273-0557</td></tr>
    </tbody>
</table>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Portland ER surprise bill eliminated under ORS 743B.524</h3>
    <p>A Portland patient treated at an in-network hospital ER received a $3,200 bill from an out-of-network emergency physician. The patient&rsquo;s insurer had paid $420 (the in-network rate); the provider billed the patient for the $2,780 difference. This is prohibited under ORS 743B.524.</p>
    <p>The patient filed a complaint with the Oregon Insurance Division. The complaint was resolved in 18 days, with the provider required to write off the balance. <strong>Total savings: $2,780.</strong></p>
</div>

<div class="case-study">
    <h3>OHSU charity care approved for Eugene resident</h3>
    <p>An uninsured Eugene resident earning $38,000/year (261% FPL) received a $22,400 bill after surgery at OHSU for a ruptured appendix. The patient applied for OHSU&rsquo;s financial assistance program, which provides sliding-scale discounts up to 500% FPL.</p>
    <p>At 261% FPL, the patient qualified for a 65% discount. <strong>Bill reduced from $22,400 to $7,840 &mdash; savings of $14,560.</strong></p>
</div>

<div class="case-study">
    <h3>Out-of-network specialist dispute resolved via Oregon CAP</h3>
    <p>A Salem patient received non-emergency knee surgery at an in-network Legacy Health facility. An out-of-network assistant surgeon billed $1,850 beyond the patient&rsquo;s in-network cost-sharing. The patient contacted Oregon CAP for free advocacy assistance.</p>
    <p>The CAP advocate filed a complaint under ORS 743B.524 and negotiated directly with the provider. <strong>Patient owed only their $250 in-network specialist copay &mdash; savings of $1,600.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Oregon have surprise billing protections?</h3>
        <p>Yes. Oregon&rsquo;s surprise billing ban (ORS 743B.524) predates the federal No Surprises Act and covers both emergency and non-emergency out-of-network billing at in-network facilities. File complaints with the Oregon Insurance Division at oregoninsurance.org or 1-888-877-4894.</p>
    </div>
    <div class="faq-item">
        <h3>How do I get free help disputing a medical bill in Oregon?</h3>
        <p>Oregon runs a free Consumer Assistance Program (CAP) through the Oregon Health Authority. CAP advocates can help you understand your rights, file complaints, and negotiate with hospitals at no cost. Call 1-888-877-4894 or apply online at oregonhealthcare.gov/cap.</p>
    </div>
    <div class="faq-item">
        <h3>What income qualifies for Oregon hospital charity care?</h3>
        <p>Oregon nonprofit hospitals must provide free care under 200% FPL (about $29,160 for a single person in 2026) and discounted care up to 400% FPL on a sliding scale. Some hospitals like OHSU go up to 500% FPL. Ask for the hospital&rsquo;s Financial Assistance Policy when you receive your bill.</p>
    </div>
    <div class="faq-item">
        <h3>How do I file a complaint about a hospital bill in Oregon?</h3>
        <p>For insurance and balance billing disputes, contact the Oregon Insurance Division at 1-888-877-4894. For charity care denials, file with the Oregon Health Authority. For billing fraud, contact the Oregon DOJ Consumer Protection Hotline at 1-877-877-9392.</p>
    </div>
    <div class="faq-item">
        <h3>Are Oregon hospital prices public?</h3>
        <p>Yes. All Oregon hospitals must comply with CMS price transparency rules and post machine-readable price files. Oregon also requires hospitals to publish their Financial Assistance Policies online. Use BillKarma&rsquo;s <a href="/hospitals/">hospital directory</a> to compare Oregon hospital billing grades and markups.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.oregonlegislature.gov/bills_laws/ors/ors743B.html" target="_blank" rel="noopener">Oregon Revised Statutes 743B.524: Surprise Billing Ban</a></li>
    <li><a href="https://www.oregonlegislature.gov/bills_laws/ors/ors441.html" target="_blank" rel="noopener">Oregon Revised Statutes 441.025: Hospital Financial Assistance</a></li>
    <li><a href="https://oregonhealthcare.gov/cap" target="_blank" rel="noopener">Oregon Health Authority: Consumer Assistance Program</a></li>
    <li><a href="https://www.cms.gov/hospital-price-transparency" target="_blank" rel="noopener">CMS Hospital Price Transparency Rule</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/surprise-medical-bills-new-protections-for-consumers-in-effect-in-2022/" target="_blank" rel="noopener">KFF: Surprise Medical Bill Protections</a></li>
    <li><a href="https://www.healthcare.gov/glossary/federal-poverty-level-fpl/" target="_blank" rel="noopener">HHS: 2026 Federal Poverty Level Guidelines</a></li>
</ul>
""",
})
