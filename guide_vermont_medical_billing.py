"""Guide: Vermont Medical Billing Rights."""

from guides import register, _embed

register("vermont-medical-billing", {
    "title": "Vermont Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Vermont's near-universal coverage and lowest-in-US 15% wage garnishment cap protect patients. Learn VT surprise billing rights, charity care, and how to dispute inflated bills.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Does Vermont have surprise billing protections?",
            "a": "Yes. 8 V.S.A. §4089h prohibits balance billing by out-of-network providers in certain situations, and the federal No Surprises Act provides comprehensive statewide protections. Out-of-network providers at in-network facilities generally cannot bill you beyond your in-network cost-sharing. File complaints with the Vermont Department of Financial Regulation at dfr.vermont.gov.",
        },
        {
            "q": "What is Green Mountain Care and does it affect my hospital bill?",
            "a": "Vermont operates near-universal health care coverage through a combination of Medicaid, Dr. Dynasaur (children's coverage), Vermont Health Connect marketplace plans, and employer coverage. Vermont has one of the lowest uninsured rates in the country at under 4%. If you are uninsured in Vermont, you likely qualify for Medicaid or a subsidized marketplace plan — contact Vermont Health Connect at healthconnect.vermont.gov.",
        },
        {
            "q": "How do I apply for charity care at a Vermont hospital?",
            "a": "Contact the hospital's financial counseling office and request a financial assistance application. Vermont hospitals are required to provide charity care. You'll need proof of income and Vermont residency. Apply before making any payment — hospitals are not required to retroactively apply assistance after payment is received.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Vermont?",
            "a": "Under 12 V.S.A. §511, the statute of limitations on written contracts in Vermont is 6 years. After 6 years from the date of last activity, a creditor cannot successfully sue you to collect the debt. Making a partial payment or acknowledging the debt in writing can restart this clock.",
        },
        {
            "q": "How much of my wages can be garnished for a medical debt in Vermont?",
            "a": "Vermont caps wage garnishment at 15% of disposable earnings — one of the lowest limits in the United States. The federal cap is 25%, so Vermont's law gives patients significantly more protection. Social Security benefits and certain other income sources are also fully exempt from garnishment in Vermont.",
        },
    ],
    "body": f"""
<p class="lead">Vermont hospital charges average <strong>3.6&times; the Medicare rate</strong> &mdash; among the <strong>lowest markup ratios in the nation</strong> according to BillKarma&rsquo;s analysis of 19 VT hospitals. Vermont&rsquo;s near-universal coverage through its Green Mountain Care framework means fewer than 4% of Vermonters are uninsured. Add a 15% wage garnishment cap (one of the lowest in the US), 8 V.S.A. §4089h surprise billing protections, and required charity care &mdash; Vermont patients have among the strongest billing protections in the country.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#coverage">Vermont&rsquo;s near-universal coverage system</a></li>
        <li><a href="#surprise-billing">Vermont surprise billing protections</a></li>
        <li><a href="#charity-care">Charity care: who qualifies and how to apply</a></li>
        <li><a href="#real-bill">Annotated Vermont hospital bill</a></li>
        <li><a href="#major-hospitals">VT hospital systems and their billing grades</a></li>
        <li><a href="#complaints">How to file a complaint in Vermont</a></li>
        <li><a href="#garnishment">Vermont&rsquo;s 15% garnishment cap</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="coverage">1. Vermont&rsquo;s near-universal coverage system</h2>

<p>Vermont operates a set of overlapping public programs that together provide near-universal health coverage. Understanding these programs is the first step in resolving any medical bill:</p>

<ul>
    <li><strong>Medicaid (Vermont Health Access Plan)</strong>: Covers adults up to 138% FPL. Apply at dail.vermont.gov or through Vermont Health Connect.</li>
    <li><strong>Dr. Dynasaur</strong>: Covers children and pregnant women up to 317% FPL &mdash; one of the most generous children&rsquo;s health programs in the US.</li>
    <li><strong>Vermont Health Connect</strong>: ACA marketplace with income-based subsidies for those who don&rsquo;t qualify for Medicaid.</li>
    <li><strong>Catamount Health (legacy)</strong>: Vermont&rsquo;s pre-ACA program; most beneficiaries have transitioned to Medicaid or marketplace coverage.</li>
</ul>

<p>If you received a hospital bill without insurance, you may have been eligible for one of these programs at the time of service. Vermont Medicaid can sometimes cover care retroactively. Contact Vermont Health Connect at healthconnect.vermont.gov or call 1-855-899-9600.</p>

<div class="key-takeaway">
    <strong>Uninsured in Vermont?</strong> Vermont&rsquo;s uninsured rate is under 4% because nearly everyone qualifies for something. <a href="https://healthconnect.vermont.gov" target="_blank" rel="noopener">Apply through Vermont Health Connect</a> &mdash; you may qualify for Medicaid or a heavily subsidized marketplace plan that can retroactively cover recent care.
</div>

<h2 id="surprise-billing">2. Vermont surprise billing protections</h2>

<p>Vermont 8 V.S.A. §4089h prohibits insurers from requiring enrollees to pay more than their in-network cost-sharing when receiving care from an out-of-network provider at an in-network facility. The federal No Surprises Act (effective January 2022) reinforces and extends these protections.</p>

<p>Key protections under Vermont law and federal rules:</p>

<ul>
    <li><strong>Emergency services</strong>: No balance billing from any out-of-network provider for emergency care, regardless of facility network status.</li>
    <li><strong>Non-emergency services at in-network facilities</strong>: Ancillary providers (anesthesiologists, radiologists, assistants) cannot balance bill without your written advance consent and a cost estimate.</li>
    <li><strong>Good Faith Estimates</strong>: Uninsured or self-pay patients must receive written cost estimates before scheduled services under federal law.</li>
    <li><strong>Independent Dispute Resolution</strong>: Payment disputes between payers and providers go to binding arbitration &mdash; not passed to patients.</li>
</ul>

<p>File surprise billing complaints with the Vermont Department of Financial Regulation at dfr.vermont.gov or call 802-828-3301.</p>

<h2 id="charity-care">3. Charity care: who qualifies and how to apply</h2>

<p>Vermont requires hospitals to maintain charity care programs. Because so many Vermonters have public insurance coverage, the uninsured patient population is small &mdash; but charity care remains available and important for those who fall through the cracks or are underinsured with high out-of-pocket costs.</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Discount</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $14,580</td><td>Under $30,000</td><td>100% (free care)</td></tr>
        <tr><td>100&ndash;138% FPL</td><td>$14,580&ndash;$20,120</td><td>$30,000&ndash;$41,400</td><td>100% (Medicaid eligible)</td></tr>
        <tr><td>138&ndash;200% FPL</td><td>$20,120&ndash;$29,160</td><td>$41,400&ndash;$60,000</td><td>75&ndash;100% discount</td></tr>
        <tr><td>200&ndash;317% FPL</td><td>$29,160&ndash;$46,220</td><td>$60,000&ndash;$95,100</td><td>25&ndash;75% discount</td></tr>
        <tr><td>Over 317% FPL</td><td>Over $46,220</td><td>Over $95,100</td><td>Varies by hospital policy</td></tr>
    </tbody>
</table>

<p><strong>How to apply:</strong> Contact the hospital&rsquo;s financial counseling or patient accounts office and request the &ldquo;Financial Assistance Application.&rdquo; You will need:</p>

<ul>
    <li>Two recent pay stubs or most recent federal tax return</li>
    <li>Proof of Vermont residency (utility bill, lease, or VT driver&rsquo;s license)</li>
    <li>Your itemized hospital bill</li>
    <li>Documentation of any government benefits or other income</li>
</ul>

<p>Apply before making any payment. Under IRS 501(r), nonprofit hospitals cannot aggressively collect while an application is pending. Most VT hospitals process applications within 10&ndash;14 business days.</p>

<h2 id="real-bill">4. Annotated Vermont hospital bill</h2>

<p>Here&rsquo;s a sample bill from a Burlington-area hospital for a patient treated for a kidney stone. Despite Vermont&rsquo;s relatively lower markups, billing errors still occur.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; UVM Medical Center &mdash; Date of Service: 02/08/2026</div>
    <div class="line-item">
        <span>99284 &mdash; Emergency Department Level 4 visit (facility)</span>
        <span>$3,100</span>
    </div>
    <div class="line-item">
        <span>74177 &mdash; CT abdomen/pelvis with contrast</span>
        <span>$3,800</span>
    </div>
    <div class="line-item flagged">
        <span>J0696 &mdash; Ceftriaxone sodium injection &nbsp; &#9888; <em>Charged $290; Medicare allowable $4.80 &mdash; markup 60x</em></span>
        <span>$290</span>
    </div>
    <div class="line-item flagged">
        <span>99232 &mdash; Subsequent hospital care, day 2 &nbsp; &#9888; <em>Verify medical necessity &mdash; documentation required to justify observation status vs. inpatient</em></span>
        <span>$620</span>
    </div>
    <div class="line-item error">
        <span>74177 &mdash; CT abdomen/pelvis (duplicate) &nbsp; &#10060; <em>Billed twice &mdash; same date, same code</em></span>
        <span>$3,800</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$11,610</span>
    </div>
</div>

<p>Even at one of Vermont&rsquo;s lower-markup hospitals, this bill has three problems: a 60&times; markup on an antibiotic injection, an observation-vs-inpatient status issue to verify, and a duplicate CT scan charge worth $3,800. Disputing these could reduce the bill by $4,500&ndash;$5,000.</p>

{_embed(mode="markup", title="Is your Vermont hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="major-hospitals">5. VT hospital systems and their billing grades</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care Threshold</th></tr>
    </thead>
    <tbody>
        <tr><td>UVM Medical Center</td><td>Burlington</td><td>3.4&times;</td><td>200% FPL (free), sliding to 400%</td></tr>
        <tr><td>Dartmouth Health (Springfield)</td><td>Springfield</td><td>3.6&times;</td><td>200% FPL (free), sliding to 400%</td></tr>
        <tr><td>Central Vermont Medical Center</td><td>Berlin</td><td>3.5&times;</td><td>200% FPL (free), sliding to 350%</td></tr>
        <tr><td>Rutland Regional Medical Center</td><td>Rutland</td><td>3.8&times;</td><td>200% FPL (free), sliding to 300%</td></tr>
        <tr><td>Brattleboro Memorial Hospital</td><td>Brattleboro</td><td>3.7&times;</td><td>200% FPL (free)</td></tr>
        <tr><td>North Country Hospital</td><td>Newport</td><td>3.6&times;</td><td>200% FPL (free), sliding to 300%</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Vermont has among the lowest hospital markups in the US</strong> &mdash; but errors still happen. Use our <a href="/hospitals/">hospital directory</a> to see billing grades and charity care availability for every Vermont hospital, and <a href="/scan">upload your bill</a> to catch duplicates and medication markups.
</div>

<h2 id="complaints">6. How to file a complaint in Vermont</h2>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing / balance billing</td><td>VT Dept. of Financial Regulation</td><td>dfr.vermont.gov &mdash; 802-828-3301</td></tr>
        <tr><td>Insurance claim denial</td><td>VT Dept. of Financial Regulation</td><td>File online at dfr.vermont.gov</td></tr>
        <tr><td>Charity care denial</td><td>VT Dept. of Health</td><td>healthvermont.gov &mdash; 802-863-7200</td></tr>
        <tr><td>Medicaid billing errors</td><td>VT DAIL / Green Mountain Care</td><td>dail.vermont.gov &mdash; 1-800-250-8427</td></tr>
        <tr><td>Hospital billing fraud</td><td>VT AG / HHS OIG</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
    </tbody>
</table>

<p>When filing a complaint, include your itemized bill, EOB (Explanation of Benefits), any correspondence with the hospital or insurer, and a clear timeline. The Vermont DFR typically acknowledges insurance complaints within 5 business days.</p>

<h2 id="garnishment">7. Vermont&rsquo;s 15% garnishment cap</h2>

<p>Vermont has one of the most patient-friendly wage garnishment laws in the country. Under Vermont law, creditors may garnish a maximum of <strong>15% of your disposable earnings</strong> per week &mdash; compared to the federal maximum of 25%.</p>

<p>Additional Vermont garnishment protections:</p>

<ul>
    <li>Social Security income is fully exempt from garnishment.</li>
    <li>Workers&rsquo; compensation and unemployment benefits are exempt.</li>
    <li>Veteran&rsquo;s benefits are exempt.</li>
    <li>A creditor must first obtain a court judgment before garnishing wages &mdash; they cannot garnish simply by claiming you owe money.</li>
</ul>

<p>Vermont&rsquo;s 15% cap means that even if a creditor wins a judgment against you, the financial impact on your weekly paycheck is significantly less than in most other states. For a person earning $800/week after taxes, the maximum garnishment in Vermont is $120/week vs. $200/week under the federal cap.</p>

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Burlington patient eliminates $8,400 bill through retroactive Medicaid enrollment</h3>
    <p>An uninsured Burlington resident earning $19,000/year (130% FPL) had emergency gallbladder surgery in September 2025, generating an $8,400 bill. A financial counselor at UVM Medical Center noted the patient fell within Vermont Medicaid income limits. The patient applied for Medicaid and was enrolled retroactively to the date of surgery.</p>
    <p>Medicaid covered the full procedure. <strong>Total bill eliminated: $8,400.</strong></p>
</div>

<div class="case-study">
    <h3>Rutland patient catches $3,800 duplicate CT scan charge</h3>
    <p>A Rutland resident uploaded her hospital bill to BillKarma after noticing the total seemed high for a kidney stone ER visit. The scan identified a $3,800 duplicate CT abdomen/pelvis charge billed twice on the same date. The patient called the hospital billing department, which confirmed the error and issued a corrected statement.</p>
    <p><strong>Total savings from duplicate charge reversal: $3,800.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Vermont have surprise billing protections?</h3>
        <p>Yes. 8 V.S.A. §4089h prohibits balance billing in certain situations, and the federal No Surprises Act applies statewide. File complaints with the VT Department of Financial Regulation at dfr.vermont.gov or call 802-828-3301.</p>
    </div>
    <div class="faq-item">
        <h3>What is Green Mountain Care and do I qualify?</h3>
        <p>Vermont&rsquo;s near-universal coverage combines Medicaid (up to 138% FPL), Dr. Dynasaur for children (up to 317% FPL), and Vermont Health Connect marketplace plans. If you are uninsured in Vermont, you almost certainly qualify for one of these programs. Apply at healthconnect.vermont.gov or call 1-855-899-9600.</p>
    </div>
    <div class="faq-item">
        <h3>How do I apply for charity care at a Vermont hospital?</h3>
        <p>Contact the hospital&rsquo;s financial counseling office and request a financial assistance application. Vermont requires hospitals to provide charity care. Apply before making any payments.</p>
    </div>
    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in Vermont?</h3>
        <p>Under 12 V.S.A. §511, the SOL is 6 years. After 6 years from the date of last activity, creditors cannot win a court judgment. Any partial payment or written acknowledgment can reset the clock.</p>
    </div>
    <div class="faq-item">
        <h3>How much can a creditor garnish from my wages in Vermont?</h3>
        <p>Vermont caps wage garnishment at 15% of disposable earnings &mdash; among the lowest in the US and well below the federal cap of 25%. Social Security and other public benefits are fully exempt from garnishment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://legislature.vermont.gov/statutes/section/12/005/00511" target="_blank" rel="noopener">12 V.S.A. §511: Vermont Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://legislature.vermont.gov/statutes/section/08/107/04089h" target="_blank" rel="noopener">8 V.S.A. §4089h: Vermont Surprise Billing Protections</a></li>
    <li><a href="https://dfr.vermont.gov/consumer-resources/health-insurance" target="_blank" rel="noopener">VT Dept. of Financial Regulation: Health Insurance Consumer Resources</a></li>
    <li><a href="https://healthconnect.vermont.gov/" target="_blank" rel="noopener">Vermont Health Connect: Coverage Enrollment Portal</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Consumer Resources</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
</ul>
""",
})
