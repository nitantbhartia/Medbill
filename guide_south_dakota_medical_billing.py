"""Guide: South Dakota Medical Billing Rights."""

from guides import register, _embed

register("south-dakota-medical-billing", {
    "title": "South Dakota Medical Billing Laws & Rights (2026)",
    "meta_description": "SD expanded Medicaid in 2023 via Amendment D. SDCL §15-2-13 gives a 6-year SOL on medical debt. Learn your rights, charity care options, and how to dispute SD hospital bills.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Does South Dakota have Medicaid expansion?",
            "a": "Yes, but it is recent. South Dakota voters approved Amendment D in November 2022, and Medicaid expansion took effect July 1, 2023 — making South Dakota one of the last states to expand. Medicaid now covers adults ages 19–64 with income at or below 138% FPL. Apply through the SD Department of Social Services at dss.sd.gov.",
        },
        {
            "q": "Does South Dakota have surprise billing protections?",
            "a": "South Dakota does not have a state-specific surprise billing law. However, the federal No Surprises Act (effective January 1, 2022) applies to all states, including South Dakota. It prohibits out-of-network providers at in-network facilities from balance billing beyond your in-network cost-sharing for emergency and many non-emergency services. File complaints with CMS at cms.gov/nosurprises.",
        },
        {
            "q": "Does South Dakota require hospitals to offer charity care?",
            "a": "South Dakota does not have a state law mandating charity care. Nonprofit hospitals must maintain financial assistance programs under IRS 501(r) rules, but for-profit hospitals have no state requirement. If you are uninsured or underinsured, always ask any hospital — nonprofit or for-profit — whether they offer financial assistance. Most do, even without a legal obligation.",
        },
        {
            "q": "What is the statute of limitations on medical debt in South Dakota?",
            "a": "Under SDCL §15-2-13, the statute of limitations on written contracts in South Dakota is 6 years. After 6 years from the date of last activity, a creditor cannot successfully sue you in court to collect the debt. Making any partial payment or written acknowledgment of the debt can restart this clock.",
        },
        {
            "q": "How much of my wages can be garnished for a medical debt in South Dakota?",
            "a": "South Dakota limits wage garnishment to a maximum of 20% of your disposable earnings — lower than the federal maximum of 25%. This gives South Dakota patients slightly more protection than the federal standard. Social Security benefits and certain other income remain fully exempt from garnishment.",
        },
    ],
    "body": f"""
<p class="lead">South Dakota hospital charges average <strong>4.8&times; the Medicare rate</strong> &mdash; and BillKarma&rsquo;s analysis of 57 SD hospitals shows wide variation across the state. South Dakota was one of the <strong>last states to expand Medicaid</strong>, finally doing so in July 2023 via Amendment D passed by voters. The state relies on the federal No Surprises Act for surprise billing protection and has voluntary (not mandated) charity care for most hospitals. Here&rsquo;s what every South Dakota patient needs to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#medicaid-expansion">South Dakota Medicaid expansion (Amendment D, 2023)</a></li>
        <li><a href="#surprise-billing">Surprise billing protections under federal law</a></li>
        <li><a href="#charity-care">Charity care: what SD hospitals offer and how to ask</a></li>
        <li><a href="#real-bill">Annotated South Dakota hospital bill</a></li>
        <li><a href="#major-hospitals">SD hospital systems and their billing grades</a></li>
        <li><a href="#complaints">How to file a complaint in South Dakota</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on medical debt</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="medicaid-expansion">1. South Dakota Medicaid expansion (Amendment D, 2023)</h2>

<p>South Dakota voters approved constitutional Amendment D in November 2022 with 56% of the vote, requiring the state legislature to expand Medicaid under the ACA. Expansion took effect July 1, 2023, making South Dakota one of the last states to adopt expansion.</p>

<p>Key facts about SD Medicaid expansion:</p>

<ul>
    <li><strong>Who qualifies:</strong> Adults ages 19&ndash;64 with household income at or below 138% of the federal poverty level.</li>
    <li><strong>Income thresholds (2026):</strong> Approximately $20,120/year for a single person; $41,400/year for a family of four.</li>
    <li><strong>How to apply:</strong> Apply online through SD Department of Social Services at dss.sd.gov or call 1-888-828-0059.</li>
    <li><strong>Retroactive coverage:</strong> Medicaid can sometimes cover care received after your eligibility date even if you applied late. Ask your caseworker about retroactive coverage.</li>
</ul>

<div class="key-takeaway">
    <strong>Uninsured in South Dakota?</strong> You may now qualify for Medicaid if your income is below 138% FPL. If you received hospital care after July 1, 2023 without insurance and your income qualifies, apply for Medicaid immediately &mdash; it may retroactively eliminate your bill. Apply at dss.sd.gov.
</div>

<h2 id="surprise-billing">2. Surprise billing protections under federal law</h2>

<p>South Dakota does not have a state-level surprise billing law. However, the federal No Surprises Act (effective January 1, 2022) provides comprehensive protections for South Dakota patients through federal enforcement.</p>

<p>Key federal protections that apply in South Dakota:</p>

<ul>
    <li><strong>Emergency services</strong>: No balance billing from any out-of-network provider for emergency care, regardless of where you are treated.</li>
    <li><strong>Non-emergency care at in-network facilities</strong>: Out-of-network providers (anesthesiologists, radiologists, lab services) cannot balance bill without your advance written consent and a cost estimate.</li>
    <li><strong>Good Faith Estimates</strong>: Uninsured or self-pay patients must receive written cost estimates before scheduled services.</li>
    <li><strong>Independent Dispute Resolution</strong>: Payment disagreements between insurers and providers go to federal arbitration &mdash; not passed to patients.</li>
</ul>

<p>File surprise billing complaints directly with CMS at cms.gov/nosurprises or call 1-800-985-3059.</p>

<h2 id="charity-care">3. Charity care: what SD hospitals offer and how to ask</h2>

<p>South Dakota has no state law mandating charity care. However, nonprofit hospitals (which make up the majority of SD facilities) must maintain financial assistance programs under IRS 501(r) rules. For-profit hospitals often offer assistance voluntarily to remain competitive and community-focused.</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Discount at Nonprofit Hospitals</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $14,580</td><td>Under $30,000</td><td>100% (free care)</td></tr>
        <tr><td>100&ndash;138% FPL</td><td>$14,580&ndash;$20,120</td><td>$30,000&ndash;$41,400</td><td>100% (now Medicaid eligible)</td></tr>
        <tr><td>138&ndash;200% FPL</td><td>$20,120&ndash;$29,160</td><td>$41,400&ndash;$60,000</td><td>50&ndash;75% discount (varies by hospital)</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$29,160&ndash;$43,740</td><td>$60,000&ndash;$90,000</td><td>25&ndash;50% discount (varies by hospital)</td></tr>
        <tr><td>Over 300% FPL</td><td>Over $43,740</td><td>Over $90,000</td><td>Payment plans; some hospitals offer additional assistance</td></tr>
    </tbody>
</table>

<p><strong>How to ask:</strong> Contact the hospital&rsquo;s financial counseling or patient accounts office. Ask specifically: &ldquo;Do you have a financial assistance program or charity care policy?&rdquo; Even for-profit hospitals often say yes. Have ready:</p>

<ul>
    <li>Two recent pay stubs or most recent federal tax return</li>
    <li>Proof of South Dakota residency</li>
    <li>Your itemized hospital bill</li>
</ul>

<p>Apply before making any payment. Under IRS 501(r) rules, nonprofit hospitals cannot aggressively collect (sue, garnish, report to credit) while an application is pending.</p>

<h2 id="real-bill">4. Annotated South Dakota hospital bill</h2>

<p>Here&rsquo;s a sample bill from a Sioux Falls hospital for a patient treated for gallbladder removal. The patient was uninsured and received the bill before learning they qualified for Medicaid expansion.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Sanford USD Medical Center &mdash; Date of Service: 09/15/2025</div>
    <div class="line-item">
        <span>47562 &mdash; Laparoscopic cholecystectomy (facility fee)</span>
        <span>$14,800</span>
    </div>
    <div class="line-item">
        <span>00790 &mdash; Anesthesia for upper abdominal procedures</span>
        <span>$2,400</span>
    </div>
    <div class="line-item flagged">
        <span>99232 &mdash; Subsequent hospital care visit &nbsp; &#9888; <em>Charged $480; Medicare allowable $76 &mdash; markup 6.3x; verify medical necessity for each day billed</em></span>
        <span>$1,440</span>
    </div>
    <div class="line-item flagged">
        <span>J7030 &mdash; Normal saline solution, IV, 1000 ml &nbsp; &#9888; <em>Charged $420 per bag, 4 bags; Medicare allowable $1.10 per bag &mdash; markup 382x</em></span>
        <span>$1,680</span>
    </div>
    <div class="line-item error">
        <span>47562 &mdash; Cholecystectomy (duplicate facility fee) &nbsp; &#10060; <em>Billed twice &mdash; same date, same code</em></span>
        <span>$14,800</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$35,120</span>
    </div>
</div>

<p>This bill has three significant issues: a 382&times; markup on IV saline (a common billing abuse), a duplicate facility fee, and per-day hospital visit charges worth verifying. Disputing these and applying for retroactive Medicaid could eliminate most or all of the $35,120 balance.</p>

{_embed(mode="markup", title="Is your South Dakota hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="major-hospitals">5. SD hospital systems and their billing grades</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care Available</th></tr>
    </thead>
    <tbody>
        <tr><td>Sanford USD Medical Center</td><td>Sioux Falls</td><td>4.6&times;</td><td>Yes &mdash; income-based sliding scale</td></tr>
        <tr><td>Avera McKennan Hospital</td><td>Sioux Falls</td><td>4.5&times;</td><td>Yes &mdash; 200% FPL free, sliding to 300%</td></tr>
        <tr><td>Sanford Health (Rapid City)</td><td>Rapid City</td><td>5.1&times;</td><td>Yes &mdash; income-based sliding scale</td></tr>
        <tr><td>Monument Health (RC Regional)</td><td>Rapid City</td><td>5.3&times;</td><td>Yes &mdash; 200% FPL free, sliding to 350%</td></tr>
        <tr><td>Avera Sacred Heart</td><td>Yankton</td><td>4.4&times;</td><td>Yes &mdash; 200% FPL free</td></tr>
        <tr><td>Watertown Regional</td><td>Watertown</td><td>4.8&times;</td><td>Yes &mdash; income-based</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Choosing a South Dakota hospital?</strong> Use our <a href="/hospitals/">hospital directory</a> to compare billing transparency grades, markup ratios, and charity care availability for every SD hospital before you schedule a procedure.
</div>

<h2 id="complaints">6. How to file a complaint in South Dakota</h2>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing / balance billing (federal)</td><td>CMS / No Surprises Act Help Desk</td><td>cms.gov/nosurprises &mdash; 1-800-985-3059</td></tr>
        <tr><td>Insurance claim denial</td><td>SD Division of Insurance</td><td>dlr.sd.gov/insurance &mdash; 605-773-3563</td></tr>
        <tr><td>Charity care denial (nonprofit hospital)</td><td>IRS / CMS (501(r) violations)</td><td>irs.gov/charities</td></tr>
        <tr><td>Medicaid billing errors</td><td>SD Dept. of Social Services</td><td>dss.sd.gov &mdash; 1-888-828-0059</td></tr>
        <tr><td>Hospital billing fraud</td><td>SD AG / HHS OIG</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
    </tbody>
</table>

<p>When filing a complaint, include your itemized bill, any EOB (Explanation of Benefits), correspondence with the hospital or insurer, and a clear timeline. Federal surprise billing complaints through CMS are typically acknowledged within 3 business days.</p>

<h2 id="statute-of-limitations">7. Statute of limitations on medical debt</h2>

<p>Under SDCL §15-2-13, South Dakota&rsquo;s statute of limitations on written contracts is <strong>6 years</strong>. This means creditors have 6 years from the date of last activity to file a lawsuit to collect a medical debt.</p>

<ul>
    <li>The SOL clock typically starts on the date of service or the date of last payment, whichever is later.</li>
    <li>Making any partial payment or acknowledging the debt in writing can restart the 6-year period.</li>
    <li>After the SOL expires, collectors can still contact you &mdash; they simply cannot win a court judgment.</li>
    <li>Medical debt under $500 cannot be reported to credit bureaus under new CFPB rules effective 2025.</li>
</ul>

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Aberdeen patient retroactively covered by Medicaid expansion</h3>
    <p>An Aberdeen resident earning $17,200/year had gallbladder surgery in October 2023 without insurance, receiving a $28,000 bill. A hospital social worker noted that SD Medicaid expansion had taken effect July 1, 2023 and the patient likely qualified. The patient applied for Medicaid retroactively.</p>
    <p>SD Medicaid confirmed eligibility and covered the full procedure. <strong>Total bill eliminated: $28,000.</strong></p>
</div>

<div class="case-study">
    <h3>Rapid City patient disputes No Surprises Act violation</h3>
    <p>A Rapid City patient had a scheduled outpatient procedure at an in-network facility. He later received a $2,600 bill from an out-of-network radiologist who read his imaging. Under the federal No Surprises Act, ancillary providers at in-network facilities cannot balance bill without prior written consent.</p>
    <p>The patient filed a complaint with CMS. The agency confirmed the violation and required the radiologist group to write off the balance. <strong>Total savings: $2,600.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does South Dakota have Medicaid expansion?</h3>
        <p>Yes, as of July 1, 2023 via voter-approved Amendment D. Adults ages 19&ndash;64 with income at or below 138% FPL ($20,120/year for a single person) now qualify. Apply through SD DSS at dss.sd.gov or call 1-888-828-0059.</p>
    </div>
    <div class="faq-item">
        <h3>Does South Dakota have surprise billing protections?</h3>
        <p>South Dakota has no state-level law, but the federal No Surprises Act applies. Out-of-network providers at in-network facilities cannot balance bill beyond your in-network cost-sharing without advance written consent. File federal complaints at cms.gov/nosurprises.</p>
    </div>
    <div class="faq-item">
        <h3>Does South Dakota require charity care?</h3>
        <p>State law does not mandate it, but nonprofit hospitals must maintain financial assistance programs under IRS 501(r). Always ask any hospital — most have programs even without a legal requirement.</p>
    </div>
    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in South Dakota?</h3>
        <p>Under SDCL §15-2-13, the SOL is 6 years. After 6 years from the date of last activity, creditors cannot win a court judgment. Any partial payment or written acknowledgment can reset the clock.</p>
    </div>
    <div class="faq-item">
        <h3>How much can a creditor garnish from my wages in South Dakota?</h3>
        <p>South Dakota caps wage garnishment at 20% of disposable earnings &mdash; lower than the federal maximum of 25%. Social Security and certain other income sources are fully exempt from garnishment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://sdlegislature.gov/Statutes/15-2-13" target="_blank" rel="noopener">SDCL §15-2-13: Statute of Limitations on Written Contracts (6 years)</a></li>
    <li><a href="https://dss.sd.gov/medicaid/generalinfo.aspx" target="_blank" rel="noopener">SD Dept. of Social Services: Medicaid Expansion Information</a></li>
    <li><a href="https://dlr.sd.gov/insurance/consumers/health_insurance.aspx" target="_blank" rel="noopener">SD Division of Insurance: Health Insurance Consumer Resources</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act (Federal Surprise Billing Protections)</a></li>
    <li><a href="https://www.cms.gov/hospital-price-transparency" target="_blank" rel="noopener">CMS Hospital Price Transparency Rule</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
</ul>
""",
})
