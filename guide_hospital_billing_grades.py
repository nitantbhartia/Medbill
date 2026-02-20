"""Guide: Hospital Billing Grades Explained."""

from guides import register, _embed

register("hospital-billing-grades-explained", {
    "title": "Hospital Billing Grades Explained: What A Through F Means for Your Bill",
    "meta_description": "BillKarma grades every hospital A–F based on how much they charge vs. Medicare. Learn what each grade means, how it's calculated, and how to use it before your next visit.",
    "published": "2026-02-20",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "What does a hospital billing grade mean?",
            "a": "A billing grade reflects how aggressively a hospital prices its services compared to what Medicare pays for the same procedures. An A-grade hospital charges 2x Medicare or less. An F-grade hospital charges more than 8x. BillKarma calculates grades using each hospital's CMS-mandated price transparency file.",
        },
        {
            "q": "Does a higher billing grade mean better care?",
            "a": "No. Billing grade and care quality are independent metrics. Some of the highest-rated hospitals by CMS quality stars also receive C or D billing grades, and some A-grade hospitals have average quality scores. Always check both when comparing hospitals.",
        },
        {
            "q": "Why is Medicare used as the benchmark?",
            "a": "Medicare pays a nationally standardized rate for every medical procedure based on actual resource costs. It's publicly available, updated annually by CMS, and is the standard reference point used by researchers, payers, and the RAND Corporation for measuring hospital pricing. A hospital charging 3x Medicare applies a 200% markup above that baseline.",
        },
        {
            "q": "Can a nonprofit hospital get an F grade?",
            "a": "Yes. Nonprofit tax status does not restrict how much a hospital charges. Many large nonprofit systems receive D or F grades because nonprofit status affects tax treatment, not billing practices. Always check the grade regardless of ownership type.",
        },
        {
            "q": "What if my hospital doesn't have a grade?",
            "a": "Some hospitals have incomplete or non-machine-readable price transparency files, which prevents BillKarma from calculating a grade. CMS requires all hospitals to post machine-readable pricing files annually — an ungraded hospital is worth noting. Use our calculator to look up Medicare rates as an independent benchmark in the meantime.",
        },
        {
            "q": "How often are hospital billing grades updated?",
            "a": "Grades are recalculated when a hospital updates its CMS price transparency file, required annually each January. BillKarma also pulls updated Medicare rates when CMS publishes the annual Outpatient Prospective Payment System (OPPS) update.",
        },
    ],
    "body": f"""
<p class="lead">Your hospital has a billing grade — A through F — based on how much it charges compared to what Medicare pays for the same procedures. According to BillKarma&rsquo;s analysis of 6,000+ hospital price transparency files, the average U.S. hospital charges <strong>3.4 times</strong> the Medicare rate, which puts most hospitals in the C range. An A-grade hospital charges 2x Medicare or less. An F-grade hospital charges more than 8x &mdash; that&rsquo;s a $12,800 bill for a procedure Medicare values at $1,600.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-grade-measures">What the billing grade measures</a></li>
        <li><a href="#grade-scale">The A&ndash;F grade scale</a></li>
        <li><a href="#why-medicare">Why Medicare is the benchmark</a></li>
        <li><a href="#grade-vs-quality">Billing grade vs. care quality</a></li>
        <li><a href="#real-dollar-impact">The real dollar impact by grade</a></li>
        <li><a href="#how-to-use">How to use a hospital&rsquo;s grade</a></li>
        <li><a href="#stuck-bad-grade">What to do when you&rsquo;re stuck with a bad-grade hospital</a></li>
        <li><a href="#case-studies">Real examples</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-grade-measures">1. What the billing grade measures</h2>

<p>Every U.S. hospital must publish a machine-readable price file listing what it charges for hundreds of procedures. BillKarma downloads and parses these files, then compares each hospital&rsquo;s gross charge (the list price before any discounts or insurance) to the Medicare facility rate for the same CPT code.</p>

<p>The result is a <strong>markup ratio</strong>: how many times the Medicare rate the hospital charges. A 3.0x markup means the hospital charges three times what Medicare pays. BillKarma averages this ratio across all procedures in the hospital&rsquo;s file and converts it to a letter grade.</p>

<div class="key-takeaway">
    <strong>The grade is based on gross charges, not what you actually pay.</strong> Insurance companies negotiate discounts off the gross charge. But your deductible, coinsurance, and any uninsured bill are often calculated as a percentage of that gross charge &mdash; so a high-markup hospital still costs you more, even with insurance.
</div>

<h2 id="grade-scale">2. The A&ndash;F grade scale</h2>

<table>
    <thead>
        <tr>
            <th>Grade</th>
            <th>Average markup vs. Medicare</th>
            <th>What it means</th>
            <th>Typical hospital types</th>
        </tr>
    </thead>
    <tbody>
        <tr><td><strong>A</strong></td><td>2.0x or less</td><td>Fair pricing &mdash; charges close to Medicare&rsquo;s resource-based rate</td><td>Critical access hospitals, safety-net hospitals, some rural hospitals</td></tr>
        <tr><td><strong>B</strong></td><td>2.1x&ndash;3.0x</td><td>Reasonable &mdash; in line with the national median for community hospitals</td><td>Community hospitals, some academic medical centers</td></tr>
        <tr><td><strong>C</strong></td><td>3.1x&ndash;5.0x</td><td>Elevated &mdash; notably above Medicare, common among large regional systems</td><td>Regional health systems, suburban hospitals</td></tr>
        <tr><td><strong>D</strong></td><td>5.1x&ndash;8.0x</td><td>High &mdash; aggressive pricing that warrants scrutiny of every line item</td><td>Large for-profit systems, high-cost urban markets</td></tr>
        <tr><td><strong>F</strong></td><td>More than 8.0x</td><td>Very aggressive &mdash; markups far above the national norm</td><td>Some large for-profit chains, specialty hospitals in low-competition markets</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>See where your hospital ranks.</strong> Check our <a href="/hospitals/">hospital directory</a> &mdash; search by name or city to find any hospital&rsquo;s billing grade, average markup, and procedure-level pricing compared to Medicare.
</div>

<h2 id="why-medicare">3. Why Medicare is the benchmark</h2>

<p>Medicare doesn&rsquo;t just set arbitrary rates. Every procedure code in the Medicare fee schedule is assigned a value based on the time, skill, and overhead required to perform it. These are called <strong>Relative Value Units (RVUs)</strong>, and they&rsquo;re adjusted for local market costs through a Geographic Practice Cost Index (GPCI).</p>

<p>This makes Medicare rates the most reliable, nationally consistent measure of what a procedure actually costs to deliver. The RAND Corporation, Health Affairs, and academic researchers use Medicare as the standard benchmark for exactly this reason. A markup of 2x Medicare means the hospital charges twice what the federal government has determined the procedure is worth, based on a detailed cost analysis.</p>

<p>Commercial insurance companies negotiate rates that typically land between Medicare (the floor) and the hospital&rsquo;s gross charge (the ceiling). According to the RAND 2023 hospital pricing study, the average commercial insurance pays hospitals <strong>254% of Medicare rates</strong> &mdash; roughly a 2.5x markup &mdash; after negotiation.</p>

<h2 id="grade-vs-quality">4. Billing grade vs. care quality</h2>

<p>A hospital&rsquo;s billing grade and its care quality are two completely separate things. Do not use one as a proxy for the other.</p>

<table>
    <thead>
        <tr>
            <th>What the billing grade measures</th>
            <th>What it does NOT measure</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>How aggressively the hospital prices its chargemaster</td><td>Clinical outcomes or survival rates</td></tr>
        <tr><td>Average markup across hundreds of procedure codes</td><td>Staff-to-patient ratios</td></tr>
        <tr><td>How transparent the hospital&rsquo;s price file is</td><td>Readmission rates</td></tr>
        <tr><td>How your costs compare to a federal benchmark</td><td>Infection rates or complication rates</td></tr>
    </tbody>
</table>

<p>For quality, look at the <strong>CMS Hospital Star Rating</strong> (1&ndash;5 stars, available at <a href="https://www.medicare.gov/care-compare/" target="_blank" rel="noopener">Medicare Care Compare</a>) and the hospital&rsquo;s HCAHPS patient satisfaction scores. BillKarma displays both alongside the billing grade on every hospital profile page.</p>

<h2 id="real-dollar-impact">5. The real dollar impact by grade</h2>

<p>The difference between an A-grade and F-grade hospital can be thousands of dollars on a single procedure, even with the same insurance plan.</p>

<p>Here&rsquo;s the same four procedures at hospitals in each grade tier, using Medicare rates from the 2026 Outpatient Prospective Payment System:</p>

<div class="bill-example">
    <div class="bill-header">MRI Lumbar Spine (CPT 72148) &mdash; Medicare rate: $97</div>
    <div class="line-item">
        <span>A-grade hospital (2.0x markup)</span>
        <span>$194</span>
    </div>
    <div class="line-item">
        <span>B-grade hospital (2.7x markup)</span>
        <span>$262</span>
    </div>
    <div class="line-item flagged">
        <span>C-grade hospital (4.2x markup) &nbsp; &#9888; <em>Above national median</em></span>
        <span>$407</span>
    </div>
    <div class="line-item flagged">
        <span>D-grade hospital (6.5x markup) &nbsp; &#9888; <em>High markup</em></span>
        <span>$631</span>
    </div>
    <div class="line-item error">
        <span>F-grade hospital (10x markup) &nbsp; &#10060; <em>Very aggressive</em></span>
        <span>$970</span>
    </div>
    <div class="line-total">
        <span>Difference: A-grade vs. F-grade</span>
        <span>$776</span>
    </div>
</div>

<p>Scale that to a knee replacement (CPT 27447, Medicare rate: $1,576) and the gap is dramatic:</p>

<div class="bill-example">
    <div class="bill-header">Total Knee Replacement (CPT 27447) &mdash; Medicare rate: $1,576</div>
    <div class="line-item">
        <span>A-grade hospital (2.0x)</span>
        <span>$3,152</span>
    </div>
    <div class="line-item">
        <span>B-grade hospital (2.7x)</span>
        <span>$4,255</span>
    </div>
    <div class="line-item flagged">
        <span>C-grade hospital (4.2x) &nbsp; &#9888;</span>
        <span>$6,619</span>
    </div>
    <div class="line-item flagged">
        <span>D-grade hospital (6.5x) &nbsp; &#9888;</span>
        <span>$10,244</span>
    </div>
    <div class="line-item error">
        <span>F-grade hospital (10x) &nbsp; &#10060;</span>
        <span>$15,760</span>
    </div>
    <div class="line-total">
        <span>Difference: A-grade vs. F-grade</span>
        <span>$12,608</span>
    </div>
</div>

<div class="key-takeaway">
    <strong>Check what Medicare pays for your procedure.</strong> Use our <a href="/calculator">free calculator</a> &mdash; enter any CPT code from your bill to see the Medicare benchmark rate and calculate what a fair markup looks like for your hospital&rsquo;s grade.
</div>

{_embed(mode="markup", title="How does your hospital&rsquo;s charge compare?", subtitle="Enter the CPT code and the gross charge from your bill.", height="420")}

<h2 id="how-to-use">6. How to use a hospital&rsquo;s grade</h2>

<p><strong>Before a planned procedure:</strong> If you have a non-emergency surgery or imaging study scheduled, check your hospital&rsquo;s grade first. If it&rsquo;s a D or F, ask your doctor whether an equivalent hospital with a better grade is available in your area. For elective procedures, switching from a D-grade to a B-grade hospital can reduce your out-of-pocket costs by 30&ndash;60%.</p>

<p><strong>After you receive a bill:</strong> If you were treated at a C, D, or F-grade hospital, upload your bill for a line-by-line review. High-markup hospitals are more likely to also have coding errors, duplicate charges, and unbundling issues on top of the baseline markup.</p>

<p><strong>When you don&rsquo;t have a choice:</strong> Emergencies, network restrictions, and specialist availability all limit hospital choice. In that case, the grade still helps you know what to expect and what to dispute. See section 7 below.</p>

<p><strong>When comparing two nearby hospitals:</strong> Grade alone isn&rsquo;t the only factor. Also check:</p>
<ul>
    <li>CMS star rating (quality)</li>
    <li>Whether the hospital is in your insurance network</li>
    <li>Whether the specific procedure you need is priced better or worse than the hospital&rsquo;s average grade suggests (use BillKarma&rsquo;s procedure-level pricing data on each hospital page)</li>
    <li>Cash price, if you&rsquo;re paying out of pocket &mdash; some high-grade hospitals offer cash discounts that are competitive with lower-grade hospitals&rsquo; insured prices</li>
</ul>

<h2 id="stuck-bad-grade">7. What to do when you&rsquo;re stuck with a bad-grade hospital</h2>

<p>If you were treated at a D or F-grade hospital &mdash; whether by necessity or before you knew the grade &mdash; the grade tells you to look harder at your bill. Higher-markup hospitals are statistically more likely to have billing errors and inflated individual line items on top of their elevated baseline prices.</p>

<p><strong>Step 1: Get an itemized bill.</strong> Request a complete itemized bill from the billing department (not just the summary statement). Every CPT code and charge should be listed individually.</p>

<p><strong>Step 2: Compare each charge to Medicare.</strong> Use the BillKarma calculator to look up the Medicare rate for each CPT code. Flag any charge that exceeds the hospital&rsquo;s grade-implied markup. A D-grade hospital charging 12x Medicare on a specific procedure is more anomalous than its average suggests.</p>

<p><strong>Step 3: Dispute line items, not the total.</strong> Call the billing department and dispute specific line items with the Medicare rate as your reference point. Phrasing: &ldquo;I can see that CPT 72148 has a Medicare rate of $97. You&rsquo;ve billed $1,200, which is 12.4x the Medicare rate. I&rsquo;d like to discuss an adjustment.&rdquo;</p>

<p><strong>Step 4: Ask about financial assistance.</strong> All nonprofit hospitals and many for-profit hospitals have financial assistance programs. Ask specifically: &ldquo;What is your charity care income threshold?&rdquo; Many programs cover patients up to 400% of the Federal Poverty Level.</p>

<p><strong>Step 5: Negotiate the cash settlement.</strong> If you have an outstanding balance, offer a cash settlement at 30&ndash;50% of the remaining bill. Hospitals routinely accept this, especially on self-pay balances, because they know the actual cost of the procedure is far below the chargemaster price.</p>

<div class="key-takeaway">
    <strong>Already got the bill?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we&rsquo;ll cross-check every line item against Medicare rates, flag charges above the hospital&rsquo;s own grade tier, and identify any coding errors worth disputing.
</div>

<h2 id="case-studies">8. Real examples</h2>

<div class="case-study">
    <h3>Planned MRI: Choosing by grade saved $740</h3>
    <p>A patient in suburban Ohio needed an MRI of the lumbar spine (CPT 72148) ordered by her primary care doctor. Her nearest hospital was a D-grade facility that listed the procedure at $874. She checked the BillKarma directory and found a B-grade hospital 8 miles away listing the same code at $134 &mdash; both in her insurance network. She scheduled at the B-grade facility.</p>
    <p>After insurance processed both facilities&rsquo; estimates, her estimated out-of-pocket at the D-grade hospital was $812 (her plan used gross charges to calculate coinsurance). At the B-grade hospital, her out-of-pocket was $72. <strong>Total savings: $740 on one imaging study.</strong></p>
</div>

<div class="case-study">
    <h3>ER visit at F-grade hospital: line-item dispute recovered $1,100</h3>
    <p>After a weekend ER visit at a hospital BillKarma grades F (average markup 9.2x Medicare), a patient received a $3,840 bill for a Level 4 ER visit (CPT 99284), chest X-ray (CPT 71046), and basic metabolic panel (CPT 80048). The Medicare rates for those three codes total $361. The hospital&rsquo;s bill implied markups of 8&ndash;12x across individual line items, with the chest X-ray billed at $420 against a Medicare rate of $13.</p>
    <p>The patient disputed the chest X-ray and lab charges specifically, citing Medicare rates. The hospital adjusted both down to their median negotiated rate. <strong>Total recovered: $1,100 off the final bill.</strong></p>
</div>

<div class="case-study">
    <h3>Knee replacement: grade research before scheduling saved $4,800</h3>
    <p>A patient in Texas with a high-deductible insurance plan needed a total knee replacement (CPT 27447). His surgeon had privileges at three hospitals: an F-grade facility (average markup 10.2x, gross charge $16,100), a C-grade facility (4.8x, gross charge $7,576), and a B-grade facility (2.6x, gross charge $4,098). All three were in-network. Medicare&rsquo;s facility rate is $1,576.</p>
    <p>His plan applied 20% coinsurance after deductible. Choosing the B-grade over the F-grade hospital reduced his coinsurance by $2,400 and reduced the amount applying toward his deductible by $12,002. <strong>Total savings on out-of-pocket costs: approximately $4,800.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What does a hospital billing grade mean?</h3>
        <p>A billing grade reflects how aggressively a hospital prices its services compared to what Medicare pays for the same procedures. An A-grade hospital charges 2x Medicare or less. An F-grade charges more than 8x. Grades are calculated from each hospital&rsquo;s CMS-mandated price transparency file and updated when the hospital posts new data. Check your hospital&rsquo;s grade in the <a href="/hospitals/">BillKarma hospital directory</a>.</p>
    </div>
    <div class="faq-item">
        <h3>Does a higher billing grade mean better care?</h3>
        <p>No. Billing grade and clinical quality are independent. A hospital can be an excellent clinical performer and still price aggressively &mdash; or vice versa. Always check both the billing grade and the CMS Star Rating. BillKarma displays both on every hospital profile.</p>
    </div>
    <div class="faq-item">
        <h3>Why is Medicare used as the benchmark?</h3>
        <p>Medicare rates are nationally standardized, publicly available, and based on a detailed cost analysis using Relative Value Units (RVUs). The RAND Corporation, Health Affairs, and CMS itself use Medicare as the standard reference for hospital pricing benchmarks. A 3x Medicare markup means the hospital charges three times the federal government&rsquo;s cost-based rate.</p>
    </div>
    <div class="faq-item">
        <h3>Can a nonprofit hospital get an F grade?</h3>
        <p>Yes. Nonprofit status affects tax treatment, not billing practices. Many large nonprofit hospital systems receive D or F grades. Always check the grade regardless of whether a hospital is listed as nonprofit or for-profit.</p>
    </div>
    <div class="faq-item">
        <h3>What if my hospital doesn&rsquo;t have a grade?</h3>
        <p>An ungraded hospital typically means its price transparency file was incomplete, non-machine-readable, or hasn&rsquo;t been parsed yet. CMS requires all hospitals to post machine-readable files annually. Use our <a href="/calculator">calculator</a> to look up Medicare rates as an independent benchmark while we process the hospital&rsquo;s data.</p>
    </div>
    <div class="faq-item">
        <h3>How often are hospital billing grades updated?</h3>
        <p>Grades are recalculated when a hospital updates its CMS price transparency file (required annually, typically in January). BillKarma also updates Medicare rate benchmarks when CMS publishes the annual OPPS and physician fee schedule updates each fall.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.rand.org/pubs/research_reports/RRA1144-2.html" target="_blank" rel="noopener">RAND Corporation: Hospital Price Transparency Study &mdash; Prices Paid to U.S. Hospitals (2023)</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2020.00893" target="_blank" rel="noopener">Health Affairs: Hospital Charge-to-Cost Ratios, 2020&ndash;2022 (2022)</a></li>
    <li><a href="https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency" target="_blank" rel="noopener">CMS: Hospital Price Transparency Rule &mdash; Requirements and Enforcement (2026)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/hospital-outpatient" target="_blank" rel="noopener">CMS: Outpatient Prospective Payment System (OPPS) &mdash; 2026 Final Rule</a></li>
    <li><a href="https://www.medicare.gov/care-compare/" target="_blank" rel="noopener">Medicare Care Compare: Hospital Quality Star Ratings</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/how-much-more-than-medicare-do-private-insurers-pay-a-review-of-the-literature/" target="_blank" rel="noopener">KFF: How Much More Than Medicare Do Private Insurers Pay? (2023)</a></li>
</ul>
""",
})
