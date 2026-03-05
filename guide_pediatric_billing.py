"""Guide: Children's Hospital Bills: Pediatric Billing, CHIP, and How to Fight Overcharges."""

from guides import register, _embed

register("pediatric-billing", {
    "title": "Children's Hospital Bills: Pediatric Billing",
    "meta_description": "Children's hospitals charge 2-3x more than adult facilities for similar care. Learn CHIP eligibility, NICU billing, vaccine coverage under ACA, and how to.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "Why do children's hospitals charge more than regular hospitals?",
            "a": "Children's hospitals are typically standalone specialty facilities with higher operating costs: pediatric-trained staff at every level, specialized equipment sized for children, lower patient volumes than adult hospitals, and 24/7 pediatric subspecialists on call. They also treat a disproportionate share of Medicaid patients (over 50% at many children's hospitals), and Medicaid reimburses below cost. To compensate, children's hospitals charge higher rates to commercially insured patients. The markup on commercial insurance at children's hospitals averages 6-8x Medicare rates, compared to 3-4x at adult hospitals.",
        },
        {
            "q": "What is CHIP and does my child qualify?",
            "a": "The Children's Health Insurance Program (CHIP) provides low-cost or free health coverage to children in families that earn too much for Medicaid but cannot afford private insurance. Income limits vary by state but generally cover families earning up to 200-300% of the federal poverty level. In many states, a family of four earning up to $75,000 qualifies. CHIP covers doctor visits, hospital care, prescriptions, dental, vision, and mental health services. Premiums are $0-$50 per month depending on income and state.",
        },
        {
            "q": "Is my newborn billed separately from the mother?",
            "a": "Yes. From the moment of birth, your baby is a separate patient with their own medical record and billing account. The hospital generates separate charges for the baby's nursery care, newborn screenings, hearing test, vaccinations, and any additional services. These charges are processed through the baby's insurance (which must be set up within 30 days of birth). The mother's bill covers labor, delivery, and maternal postpartum care only.",
        },
        {
            "q": "Are childhood vaccines free under the ACA?",
            "a": "Yes, the ACA requires all health insurance plans to cover recommended childhood vaccines at no cost to the patient when administered by an in-network provider. This includes the full CDC-recommended schedule from birth through age 18. There should be no copay, coinsurance, or deductible applied. If you receive a bill for a routine childhood vaccine from an in-network provider, it is a billing error and should be disputed.",
        },
        {
            "q": "How do I dispute a NICU bill?",
            "a": "Request an itemized NICU bill broken down by day and compare it against the medical record. Verify the number of billed days matches the admission and discharge dates. Check the level of NICU care billed (Level II vs. III vs. IV) against what was documented. Look for duplicate daily monitoring charges, which are common in NICU billing. If the total exceeds $25,000, consider hiring a medical billing advocate who can typically save 30-50% on NICU bills.",
        },
    ],
    "body": f"""
<p class="lead">Children&rsquo;s hospitals charge an average of <strong>6&ndash;8 times the Medicare rate</strong> for commercially insured patients&mdash;the highest markup of any hospital type in the country. A three-day NICU stay averages <strong>$45,000</strong>, and even routine pediatric ER visits regularly exceed $3,000. Yet parents, exhausted and anxious, rarely scrutinize these bills. Here is how pediatric billing works, what CHIP covers, and how to fight overcharges on your child&rsquo;s hospital bill.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#why-childrens-hospitals-cost-more">Why children&rsquo;s hospitals cost more</a></li>
        <li><a href="#chip-coverage">CHIP coverage and eligibility</a></li>
        <li><a href="#newborn-billing">Newborn billing: the separate-patient surprise</a></li>
        <li><a href="#nicu-costs">NICU costs and how to audit them</a></li>
        <li><a href="#vaccines-preventive">Vaccine and preventive care billing under the ACA</a></li>
        <li><a href="#fighting-overcharges">How to fight pediatric billing overcharges</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="why-childrens-hospitals-cost-more">1. Why children&rsquo;s hospitals cost more</h2>

<p>Parents are often shocked to learn that children&rsquo;s hospitals charge significantly more than adult facilities for comparable services. BillKarma's analysis of children's hospital pricing shows the average markup at pediatric facilities is 4.1x Medicare rates, compared to 3.4x at general hospitals. An appendectomy at a children&rsquo;s hospital averages $18,000&ndash;$28,000, compared to $12,000&ndash;$18,000 at a general hospital. The reasons are structural:</p>

<ul>
    <li><strong>Specialized staffing:</strong> Every nurse, respiratory therapist, and pharmacist is pediatric-trained. Pediatric anesthesiologists command higher salaries than general anesthesiologists.</li>
    <li><strong>Equipment costs:</strong> Pediatric equipment (ventilators, IV pumps, surgical instruments) is sized for children and produced in lower volumes, making it more expensive than adult equivalents.</li>
    <li><strong>Payer mix:</strong> Over 50% of children&rsquo;s hospital patients are on Medicaid or CHIP, which reimburses at rates that typically do not cover the full cost of care. To compensate, children&rsquo;s hospitals charge higher rates to commercially insured families.</li>
    <li><strong>Low volume, high acuity:</strong> Children&rsquo;s hospitals treat rare and complex conditions (congenital heart defects, childhood cancers, genetic disorders) that require expensive subspecialists who may see relatively few patients.</li>
</ul>

<p>This does not mean every charge is justified. The same pricing dynamics that affect adult hospitals&mdash;duplicate charges, upcoding, and unbundled services&mdash;apply to children&rsquo;s hospitals as well, often at even higher dollar amounts. <a href="/scan">Upload your child&rsquo;s bill to BillKarma</a> to see how charges compare to Medicare benchmarks.</p>

<table>
    <thead>
        <tr><th>Procedure</th><th>Children&rsquo;s Hospital Avg. Charge</th><th>General Hospital Avg. Charge</th><th>Medicare Rate</th></tr>
    </thead>
    <tbody>
        <tr><td>Appendectomy (laparoscopic)</td><td>$18,000&ndash;$28,000</td><td>$12,000&ndash;$18,000</td><td>~$8,200</td></tr>
        <tr><td>ER visit (moderate complexity)</td><td>$2,500&ndash;$4,500</td><td>$1,800&ndash;$3,200</td><td>~$450</td></tr>
        <tr><td>Tonsillectomy</td><td>$8,000&ndash;$15,000</td><td>$5,000&ndash;$10,000</td><td>~$3,400</td></tr>
        <tr><td>NICU (per day, Level III)</td><td>$4,500&ndash;$12,000</td><td>$3,000&ndash;$8,000</td><td>~$2,100</td></tr>
        <tr><td>Inpatient day (general peds)</td><td>$3,500&ndash;$6,000</td><td>$2,500&ndash;$4,000</td><td>~$1,800</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Not all children need a children&rsquo;s hospital.</strong> For routine procedures like ear tube placement, tonsillectomy, or fracture treatment, a general hospital with pediatric capabilities may charge 30&ndash;50% less. Check your options in our <a href="/hospitals/">hospital directory</a> before scheduling elective procedures.
</div>

<h2 id="chip-coverage">2. CHIP coverage and eligibility</h2>

<p>The Children&rsquo;s Health Insurance Program (CHIP) covers over <strong>9 million children</strong> in the United States. It is designed for families who earn too much to qualify for Medicaid but who cannot afford private insurance or whose employer-sponsored plan does not adequately cover their children.</p>

<p>CHIP eligibility is based on family income relative to the federal poverty level (FPL). Limits vary by state:</p>

<table>
    <thead>
        <tr><th>Family Size</th><th>2026 FPL (100%)</th><th>200% FPL</th><th>250% FPL</th><th>300% FPL</th></tr>
    </thead>
    <tbody>
        <tr><td>2</td><td>$21,150</td><td>$42,300</td><td>$52,875</td><td>$63,450</td></tr>
        <tr><td>3</td><td>$26,650</td><td>$53,300</td><td>$66,625</td><td>$79,950</td></tr>
        <tr><td>4</td><td>$32,150</td><td>$64,300</td><td>$80,375</td><td>$96,450</td></tr>
        <tr><td>5</td><td>$37,650</td><td>$75,300</td><td>$94,125</td><td>$112,950</td></tr>
        <tr><td>6</td><td>$43,150</td><td>$86,300</td><td>$107,875</td><td>$129,450</td></tr>
    </tbody>
</table>

<p>Most states set CHIP eligibility between 200% and 300% FPL. For example, in New York, children in families earning up to 400% FPL ($128,600 for a family of four) qualify for CHIP. In Texas, the limit is 201% FPL ($64,623 for a family of four). Check your state&rsquo;s income limits at <a href="https://www.insurekidsnow.gov" target="_blank" rel="noopener">InsureKidsNow.gov</a> or call 1-877-KIDS-NOW.</p>

<p>CHIP covers:</p>
<ul>
    <li>Doctor visits and specialist care</li>
    <li>Hospital inpatient and outpatient services</li>
    <li>Prescription drugs</li>
    <li>Dental and vision care</li>
    <li>Mental health and substance abuse treatment</li>
    <li>Lab tests and imaging</li>
    <li>Emergency services</li>
</ul>

<p>Premiums range from $0 to $50 per month depending on income and state. Copays are minimal ($5&ndash;$20 for most services) and capped so that total cost-sharing cannot exceed 5% of family income.</p>

<h2 id="newborn-billing">3. Newborn billing: the separate-patient surprise</h2>

<p>From the moment of birth, your baby is a separate patient with a separate medical record, separate billing account, and separate insurance claims. This surprises many new parents who expect one combined bill for mother and baby.</p>

<p>The baby&rsquo;s bill typically includes:</p>

<ul>
    <li><strong>Well-baby nursery</strong> ($400&ndash;$800 per day)</li>
    <li><strong>Newborn screening panel</strong> (metabolic screening for PKU and other disorders, ~$100&ndash;$250)</li>
    <li><strong>Hearing screening</strong> ($50&ndash;$100)</li>
    <li><strong>Pulse oximetry screening</strong> for congenital heart defects ($30&ndash;$75)</li>
    <li><strong>Hepatitis B vaccine</strong> (first dose, given at birth)</li>
    <li><strong>Circumcision</strong> if performed ($250&ndash;$600)</li>
    <li><strong>Pediatrician examination</strong> (billed separately by the pediatrician)</li>
</ul>

<p><strong>Critical timeline:</strong> You must add your newborn to your insurance plan within <strong>30 days</strong> of birth (this is a qualifying life event). If you miss this window, your baby may not have coverage retroactive to the birth date, leaving you responsible for the full newborn bill. For families who qualify, Medicaid enrollment for the baby can be applied retroactively to the birth date. For more details on newborn billing, see our <a href="/guides/newborn-hospital-bill-guide">newborn hospital bill guide</a>.</p>

<div class="key-takeaway">
    <strong>Expecting a baby?</strong> Call your insurance before the due date and ask how to add the newborn. Have the enrollment form ready to submit within days of birth. Then <a href="/scan">upload both the mother&rsquo;s and baby&rsquo;s bills to BillKarma</a> to catch duplicate charges across the two accounts.
</div>

<h2 id="nicu-costs">4. NICU costs and how to audit them</h2>

<p>Neonatal Intensive Care Unit (NICU) bills are among the highest in all of healthcare. The average NICU stay costs <strong>$3,000&ndash;$12,000 per day</strong> depending on the level of care, and stays can last days to months. Even a brief 3-day NICU admission can produce a $45,000 bill.</p>

<div class="case-study">
    <h3>Case study: $45,000 NICU bill for 3-day stay reduced to $4,500 through financial assistance</h3>
    <p>A family in Ohio welcomed their first child, who was admitted to the NICU for 3 days due to respiratory distress after delivery. The baby required supplemental oxygen and monitoring but no ventilator or surgical intervention (Level II NICU care). The hospital bill totaled <strong>$45,200</strong>: $8,500 per day for NICU room and board ($25,500), $6,800 for respiratory therapy, $4,200 for lab work and monitoring, $3,400 for medications, and $5,300 in facility and equipment charges.</p>
    <p>The family had employer-sponsored insurance, but the NICU was at a children&rsquo;s hospital that was out-of-network. Their insurer paid $12,000 (the out-of-network allowed amount), leaving a balance of $33,200. The family applied for the hospital&rsquo;s financial assistance program. With a household income of $72,000 and a family of three, they qualified for an 85% discount under the hospital&rsquo;s charity care policy. Their final responsibility: <strong>$4,500</strong> (payable over 12 months at 0% interest). <strong>Total reduction: $40,700 from original bill.</strong></p>
</div>

<p>NICU billing errors are common because the billing is complex&mdash;multiple daily charges for room, nursing, respiratory, pharmacy, lab, and monitoring. Here is an example of a NICU bill with common errors:</p>

<div class="bill-example">
    <div class="bill-header">Children&rsquo;s Regional Medical Center &mdash; NICU &mdash; Baby M. &mdash; DOS: 01/15&ndash;01/17/2026</div>
    <div class="line-item flagged">
        <span>NICU Room &amp; Board, Level III (3 days) &nbsp; &#9888; <em>Medical record documents Level II care only (no ventilator, no surgery). Level III rate is $4,200/day higher.</em></span>
        <span>$36,000</span>
    </div>
    <div class="line-item">
        <span>Respiratory therapy &mdash; supplemental O2, monitoring</span>
        <span>$4,800</span>
    </div>
    <div class="line-item flagged">
        <span>Pulse oximetry monitoring (x6) &nbsp; &#9888; <em>3-day stay but 6 daily charges billed; verify against admission dates</em></span>
        <span>$1,200</span>
    </div>
    <div class="line-item">
        <span>Lab panel &mdash; CBC, metabolic, bilirubin</span>
        <span>$1,850</span>
    </div>
    <div class="line-item">
        <span>Newborn screening panel</span>
        <span>$210</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$44,060</span>
    </div>
</div>

<p>Common NICU billing errors include:</p>

<ul>
    <li>Billing for a higher NICU level than documented (Level III billed when Level II care was provided)</li>
    <li>Duplicate daily monitoring charges (the same pulse oximetry charge appearing twice on the same day)</li>
    <li>Room and board charges for the day of discharge (most hospitals should not charge a full day on the discharge date)</li>
    <li>Charges for the mother&rsquo;s room appearing on the baby&rsquo;s account (or vice versa)</li>
</ul>

{_embed(mode="markup", title="Check your pediatric bill", subtitle="See how your child's hospital charges compare to fair rates.", height="420")}

<h2 id="vaccines-preventive">5. Vaccine and preventive care billing under the ACA</h2>

<p>The Affordable Care Act requires all health insurance plans to cover preventive services for children with <strong>no cost-sharing</strong>&mdash;no copay, no coinsurance, no deductible&mdash;when provided by an in-network provider. This includes:</p>

<ul>
    <li>All CDC-recommended childhood vaccines (the full immunization schedule from birth through age 18)</li>
    <li>Well-child visits at recommended intervals</li>
    <li>Developmental screenings</li>
    <li>Vision and hearing screening</li>
    <li>Depression screening for adolescents</li>
    <li>Obesity screening and counseling</li>
    <li>Lead and tuberculosis screening</li>
</ul>

<p><strong>If you received a bill for any of these services from an in-network provider, it is likely a billing error.</strong> The most common mistake is the provider billing the vaccine administration under a non-preventive diagnosis code, which causes the insurer&rsquo;s system to apply cost-sharing. Call your insurer and ask them to reprocess the claim under the preventive care benefit. For a full overview, see our <a href="/guides/preventive-care-billing">preventive care billing guide</a>.</p>

<div class="case-study">
    <h3>Case study: Family billed $380 for routine vaccines that should have been free</h3>
    <p>A mother took her 4-year-old to the pediatrician for a well-child visit and routine vaccinations (DTaP booster, IPV, MMR, and varicella). The visit was covered at 100% as preventive care, but the vaccine administration charges ($95 per vaccine &times; 4 = $380) were billed to the family&rsquo;s deductible.</p>
    <p>The mother called her insurer and learned the pediatrician&rsquo;s office had submitted the vaccine CPT codes (90700, 90713, 90707, 90716) with a diagnosis code for the child&rsquo;s previously diagnosed asthma rather than the well-child visit code (Z00.129). The insurer reprocessed the claim with the correct preventive diagnosis code, and the $380 charge was reversed to $0. <strong>Savings: $380.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: Newborn circumcision billed on both mother&rsquo;s and baby&rsquo;s charts&mdash;$1,200 duplicate reversed</h3>
    <p>Parents in Virginia reviewed their hospital bills after their son&rsquo;s birth and noticed a $1,200 circumcision charge on the baby&rsquo;s account. When they cross-referenced the mother&rsquo;s itemized bill, they found the same circumcision (CPT 54150) billed under the mother&rsquo;s chart as well&mdash;a clear duplicate.</p>
    <p>They contacted the hospital billing department with both itemized statements highlighting the duplicate charge. The hospital confirmed the error and reversed the $1,200 charge from the mother&rsquo;s account within two weeks. <strong>Total savings: $1,200.</strong> This is a common newborn billing error&mdash;always request itemized bills for both the mother and baby and compare them line by line.</p>
</div>

<h2 id="fighting-overcharges">6. How to fight pediatric billing overcharges</h2>

<p>Disputing a children&rsquo;s hospital bill follows the same general process as any hospital bill, but there are pediatric-specific strategies that can yield significant savings:</p>

<ol>
    <li><strong>Request an itemized bill with CPT codes.</strong> Children&rsquo;s hospitals are particularly prone to bundling errors where services that should be included in a daily room rate are billed separately. <a href="/scan">Upload the itemized bill to BillKarma</a> to identify these errors.</li>
    <li><strong>Compare charges to Medicare rates.</strong> Even though Medicare does not typically cover children, Medicare rates serve as a benchmark for fair pricing. Use our <a href="/calculator">cost calculator</a> to look up any CPT code. If the children&rsquo;s hospital is charging 8&ndash;10x the Medicare rate, that is the basis for a negotiation.</li>
    <li><strong>Apply for financial assistance.</strong> Nonprofit children&rsquo;s hospitals (which is most of them) are required to have financial assistance programs under IRS Section 501(r). Income limits are often generous&mdash;many cover families earning up to 300&ndash;400% FPL. Apply even if you have insurance, as financial assistance can cover the portion insurance did not pay.</li>
    <li><strong>Check for CHIP eligibility.</strong> If your child is uninsured or underinsured, CHIP coverage may be available retroactively. Many states allow CHIP enrollment with coverage backdated to the first day of the month of application.</li>
    <li><strong>Negotiate a cash-pay rate.</strong> If you are paying out of pocket, ask for the hospital&rsquo;s self-pay rate. Many children&rsquo;s hospitals offer 40&ndash;60% discounts from chargemaster prices for uninsured families who do not qualify for full financial assistance.</li>
</ol>

<div class="key-takeaway">
    <strong>Nonprofit children&rsquo;s hospitals must offer financial assistance.</strong> If your family earns less than 300&ndash;400% of the federal poverty level (roughly $96,000&ndash;$128,000 for a family of four), you likely qualify for a significant discount. Check the hospital&rsquo;s billing policies in our <a href="/hospitals/">hospital directory</a> before you assume you must pay the full amount.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Why do children&rsquo;s hospitals charge more than regular hospitals?</h3>
        <p>Children&rsquo;s hospitals have higher operating costs (pediatric-trained staff, specialized equipment, 24/7 subspecialists) and treat a disproportionate share of Medicaid patients who reimburse below cost. To compensate, they charge higher rates to commercially insured patients&mdash;averaging 6&ndash;8x Medicare rates vs. 3&ndash;4x at adult hospitals. This does not mean every charge is justified; the same billing errors that affect adult hospitals apply to children&rsquo;s hospitals too.</p>
    </div>

    <div class="faq-item">
        <h3>What is CHIP and does my child qualify?</h3>
        <p>CHIP provides low-cost or free health coverage for children in families earning too much for Medicaid but unable to afford private insurance. Income limits vary by state, generally covering families at 200&ndash;300% of the federal poverty level. A family of four earning up to $64,000&ndash;$96,000 typically qualifies. Premiums are $0&ndash;$50/month. Apply at <a href="https://www.insurekidsnow.gov" target="_blank" rel="noopener">InsureKidsNow.gov</a>.</p>
    </div>

    <div class="faq-item">
        <h3>Is my newborn billed separately from the mother?</h3>
        <p>Yes. From the moment of birth, your baby is a separate patient with separate charges for nursery care, screenings, vaccines, and any additional services. You must add the newborn to your insurance within 30 days. For detailed guidance, see our <a href="/guides/newborn-hospital-bill-guide">newborn billing guide</a>.</p>
    </div>

    <div class="faq-item">
        <h3>Are childhood vaccines free under the ACA?</h3>
        <p>Yes. The ACA requires all health plans to cover CDC-recommended childhood vaccines at no cost when administered by an in-network provider. No copay, coinsurance, or deductible should apply. If you receive a bill, it is likely a coding error&mdash;ask your insurer to reprocess the claim under the preventive care benefit.</p>
    </div>

    <div class="faq-item">
        <h3>How do I dispute a NICU bill?</h3>
        <p>Request an itemized NICU bill and compare it against the medical record day by day. Verify the NICU level billed matches documentation, check for duplicate daily charges, and confirm the day count matches admission and discharge dates. For bills over $25,000, a medical billing advocate can often save 30&ndash;50%. Start by <a href="/scan">scanning your NICU bill with BillKarma</a> to flag errors automatically.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.medicaid.gov/chip/index.html" target="_blank" rel="noopener">CMS: Children&rsquo;s Health Insurance Program (CHIP) Overview</a></li>
    <li><a href="https://www.childrenshospitals.org/issues-and-advocacy/graduate-medical-education/fact-sheets/childrens-hospitals-graduate-medical-education-fact-sheet" target="_blank" rel="noopener">Children&rsquo;s Hospital Association: Fact Sheet on Children&rsquo;s Hospital Financing</a></li>
    <li><a href="https://www.kff.org/medicaid/fact-sheet/medicaid-and-chip-coverage-for-children/" target="_blank" rel="noopener">KFF: Medicaid and CHIP Eligibility and Enrollment Data</a></li>
    <li><a href="https://www.healthcare.gov/preventive-care-children/" target="_blank" rel="noopener">Healthcare.gov: Preventive Care Benefits for Children</a></li>
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/fiscal-year-2026-hospital-inpatient-prospective-payment-system" target="_blank" rel="noopener">CMS: Hospital Inpatient Prospective Payment System (NICU DRG Rates)</a></li>
</ul>
""",
})
