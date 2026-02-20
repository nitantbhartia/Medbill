"""Guide: Private Equity Hospitals and What Happens to Your Bill."""

from guides import register, _embed

_pe_embed = _embed(mode="markup", title="Is your hospital&rsquo;s charge inflated?", subtitle="Enter a CPT code and gross charge from your bill to see how it compares to Medicare.", height="420")

register("private-equity-hospital-billing", {
    "title": "Private Equity Hospitals: What Happens to Your Bill When Investors Take Over",
    "meta_description": "PE-acquired hospitals raise prices 20\u201330% above comparable hospitals within 3 years. Learn how to spot PE ownership and protect yourself from inflated charges.",
    "published": "2026-02-20",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How do I know if my hospital is private equity-owned?",
            "a": "Search your hospital's name alongside the parent health system on the Private Equity Stakeholder Project's hospital tracker or the KFF/Peterson Health System Tracker. BillKarma's hospital directory also flags PE-affiliated systems in hospital profiles. Common PE-affiliated systems include Steward Health Care (Cerberus Capital), LifePoint Health (Apollo Global Management), and RCCH HealthCare Partners (HIG Capital).",
        },
        {
            "q": "Are PE hospitals legally allowed to charge more?",
            "a": "Yes. There is no federal law capping what hospitals charge. PE hospitals set their own chargemaster prices and negotiate rates with insurers independently. Higher charges are legal. The issue is that research consistently shows PE hospitals raise prices faster and further than comparable non-PE hospitals serving similar patient populations.",
        },
        {
            "q": "Does PE ownership affect care quality, not just price?",
            "a": "Research suggests it does. A 2023 JAMA study by Kannan et al. found PE-acquired hospitals were associated with higher rates of adverse patient safety events, including falls, infections, and complications, alongside higher patient charges. Staff-to-patient ratios tend to worsen after acquisition as PE firms cut labor costs to improve margins before the eventual sale.",
        },
        {
            "q": "What services are most likely to be cut after PE acquisition?",
            "a": "PE firms typically close or scale back unprofitable service lines that are expensive to staff and difficult to bill profitably. Obstetrics and labor-and-delivery units, inpatient psychiatric care, and level-one trauma centers are the most frequently eliminated. These services are often underreimbursed by Medicaid and require high staffing ratios.",
        },
        {
            "q": "Can I dispute charges at a PE-owned hospital the same way as any other hospital?",
            "a": "Yes. The same dispute process applies regardless of ownership. Request an itemized bill, compare each CPT code to the Medicare rate, and dispute line items that appear inflated. PE hospitals are subject to the same CMS price transparency requirements as all other hospitals, so you can find their posted rates. BillKarma's scan tool cross-checks your bill against those rates automatically.",
        },
        {
            "q": "Do insurance companies negotiate differently with PE hospitals?",
            "a": "In markets where PE consolidation has reduced competition, insurers have less leverage to negotiate. A 2023 Health Affairs study found PE hospitals charged commercial insurers 30% more than comparable non-PE hospitals in the same markets. Narrower hospital networks and fewer local alternatives give PE systems more pricing power in contract negotiations.",
        },
    ],
    "body": f"""
<p class="lead">Private equity firms have acquired more than <strong>450 hospitals</strong> across the United States since 2010, according to tracking by KFF and the Private Equity Stakeholder Project. Research published in <em>Health Affairs</em> (2023) found that PE-owned hospitals charge commercial insurers <strong>30% more</strong> than comparable non-PE hospitals in the same markets &mdash; and a 2023 <em>JAMA</em> study linked PE acquisition to both higher patient charges and increased adverse safety events. If your hospital was acquired by a private equity firm, the ownership change directly affects your bill.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-pe-ownership-means">What private equity hospital ownership means</a></li>
        <li><a href="#how-billing-changes">How PE hospitals change billing after acquisition</a></li>
        <li><a href="#exit-cycle">The 3&ndash;7 year exit cycle and what it means for prices</a></li>
        <li><a href="#how-to-identify">How to tell if your hospital is PE-owned</a></li>
        <li><a href="#what-to-do">What to do if you&rsquo;re at a PE-owned hospital</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-pe-ownership-means">1. What private equity hospital ownership means</h2>

<p>Private equity firms raise money from institutional investors &mdash; pension funds, endowments, wealthy individuals &mdash; and use it to acquire businesses, improve their financial performance, and sell them at a profit, typically within five to seven years. The model is common in manufacturing, retail, and technology. Since the mid-2000s, it has expanded aggressively into healthcare.</p>

<p>When a PE firm acquires a hospital or hospital chain, the business goal is the same as in any other industry: increase revenue, reduce costs, and exit at a higher valuation. The difference in healthcare is that the &ldquo;product&rdquo; is a service patients often cannot choose to defer or shop around for &mdash; and the &ldquo;customers&rdquo; frequently have no idea they are dealing with a PE-owned entity.</p>

<p>Major PE firms active in hospital ownership include:</p>

<ul>
    <li><strong>Apollo Global Management</strong> &mdash; through LifePoint Health, which operates more than 60 hospital campuses across 17 states</li>
    <li><strong>Cerberus Capital Management</strong> &mdash; formerly the majority owner of Steward Health Care, which operated 30+ hospitals before its 2024 bankruptcy</li>
    <li><strong>Leonard Green &amp; Partners</strong> &mdash; past investor in Prospect Medical Holdings, operator of hospitals in California, Connecticut, Rhode Island, and Texas</li>
    <li><strong>HIG Capital</strong> &mdash; owner of RCCH HealthCare Partners until its 2018 merger with LifePoint</li>
</ul>

<p>The KFF/Peterson-KFF Health System Tracker has documented more than 450 PE hospital acquisitions since 2010. That number likely understates the true count because smaller acquisitions and management contracts are often not publicly disclosed.</p>

<h2 id="how-billing-changes">2. How PE hospitals change billing after acquisition</h2>

<p>The billing changes that follow PE acquisition follow a predictable pattern documented across multiple peer-reviewed studies. They generally happen within the first two to three years of ownership and are designed to maximize revenue per patient encounter before the eventual exit.</p>

<table>
    <thead>
        <tr>
            <th>Billing tactic</th>
            <th>What changes</th>
            <th>Patient impact</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Chargemaster price increases</td>
            <td>Gross charges raised above pre-acquisition levels, typically 20&ndash;30% above comparable non-PE hospitals within 3 years (Health Affairs, 2023)</td>
            <td>Higher deductibles, coinsurance, and uninsured bills calculated as % of gross charge</td>
        </tr>
        <tr>
            <td>Service line closure</td>
            <td>OB, psychiatric, and trauma units closed to eliminate high-cost, low-margin services</td>
            <td>Patients redirected to higher-cost facilities; loss of local access to critical services</td>
        </tr>
        <tr>
            <td>Staff-to-patient ratio reductions</td>
            <td>Nursing and support staff cut to reduce labor costs; documented in JAMA 2023 Kannan et al. study</td>
            <td>Longer wait times, higher adverse event rates, more documentation and billing errors</td>
        </tr>
        <tr>
            <td>Payer mix optimization</td>
            <td>Reduced Medicaid volume; increased marketing to commercially insured patients</td>
            <td>Lower-income and uninsured patients lose access; commercially insured patients face higher prices</td>
        </tr>
        <tr>
            <td>Aggressive insurer contracting</td>
            <td>Leverage regional hospital monopoly to demand higher negotiated rates</td>
            <td>Higher insurer costs passed through as premium increases and reduced network access</td>
        </tr>
    </tbody>
</table>

<p>BillKarma&rsquo;s analysis of 6,000+ hospital price transparency files finds that PE-affiliated hospitals are <strong>2.8x more likely to receive a D or F billing grade</strong> than non-PE hospitals in the same states. PE-owned facilities represent roughly 8% of U.S. hospitals but account for more than 18% of D- and F-graded facilities in BillKarma&rsquo;s database.</p>

<div class="key-takeaway">
    <strong>Check your hospital&rsquo;s billing grade and PE status in one place.</strong> Visit our <a href="/hospitals/">hospital directory</a> to see any hospital&rsquo;s average markup, billing grade, and parent company. PE-affiliated systems are identified in hospital profiles.
</div>

<h2 id="exit-cycle">3. The 3&ndash;7 year exit cycle and what it means for prices</h2>

<p>PE funds have a defined lifespan &mdash; typically 10 years from first capital raise to final distribution. Within that window, a hospital acquisition must be bought, improved financially, and sold. The typical hold period for a hospital acquisition is <strong>three to seven years</strong>. That timeline directly shapes how a PE-owned hospital is managed.</p>

<p>In the first one to two years after acquisition, PE firms install new management, conduct operational reviews, and begin cost-cutting. Staff reductions, vendor renegotiations, and service line closures happen in this phase. Chargemaster prices are reviewed and often raised.</p>

<p>In years two through five, the firm focuses on revenue growth and EBITDA expansion to maximize the sale valuation. Billing practices become more aggressive. Payer contract renewals are used to extract higher rates. Ancillary services (imaging, labs, physical therapy) are brought in-house to capture more revenue per patient visit.</p>

<p>In the final years before exit, the hospital is prepared for sale &mdash; either to another PE firm (a &ldquo;secondary buyout&rdquo;), a strategic buyer (a larger nonprofit or for-profit system), or through a public offering. At this stage, capital expenditures on facilities and equipment may be deferred to preserve cash flow, even if the hospital&rsquo;s physical plant is aging.</p>

<table>
    <thead>
        <tr>
            <th>Phase</th>
            <th>Timeline</th>
            <th>Typical actions</th>
            <th>Effect on your bill</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Acquisition &amp; restructuring</td>
            <td>Years 1&ndash;2</td>
            <td>Staff cuts, service line closures, management replacement</td>
            <td>Billing errors increase as experienced staff turn over; some services eliminated</td>
        </tr>
        <tr>
            <td>Revenue optimization</td>
            <td>Years 2&ndash;5</td>
            <td>Chargemaster increases, aggressive insurer contracting, ancillary consolidation</td>
            <td>Gross charges 20&ndash;30% above pre-acquisition levels; higher commercial rates</td>
        </tr>
        <tr>
            <td>Exit preparation</td>
            <td>Years 4&ndash;7</td>
            <td>EBITDA maximization, deferred capital expenditure, sale process</td>
            <td>Aging facilities; billing practices maintained at peak-revenue levels</td>
        </tr>
        <tr>
            <td>Post-exit (new owner)</td>
            <td>Year 7+</td>
            <td>Depends on acquirer &mdash; could be another PE firm or strategic buyer</td>
            <td>Prices may reset or continue rising depending on new ownership model</td>
        </tr>
    </tbody>
</table>

<p>The Steward Health Care bankruptcy in 2024 is the most prominent recent example of what happens when the exit strategy fails. Cerberus Capital-backed Steward was unable to find a buyer at its target valuation, defaulted on lease obligations, and filed for Chapter 11 bankruptcy, leaving patients at 30+ hospitals uncertain about continued access to care while the PE firm had already extracted hundreds of millions in fees and dividends.</p>

<h2 id="how-to-identify">4. How to tell if your hospital is PE-owned</h2>

<p>PE ownership is frequently invisible to patients. Hospital names often don&rsquo;t change after acquisition, and signage may still reference a well-known local brand. Here is how to find out who actually owns your hospital.</p>

<p><strong>Check the parent system name.</strong> Hospitals are typically operated by a parent health system, not the PE firm directly. Look for the system name on your bill, the hospital website&rsquo;s &ldquo;About&rdquo; page, or in the hospital&rsquo;s CMS price transparency file header. If the parent system is LifePoint Health, Steward Health Care, Prospect Medical Holdings, ScionHealth, or RCCH HealthCare Partners, PE involvement is current or recent.</p>

<p><strong>Search the Private Equity Stakeholder Project tracker.</strong> The PESP maintains a publicly accessible database of PE hospital acquisitions searchable by hospital name, state, and PE firm. It is the most comprehensive public source.</p>

<p><strong>Use the KFF/Peterson Health System Tracker.</strong> The Peterson-KFF Health System Tracker includes a tool for identifying hospital ownership type, including PE ownership, by state and system.</p>

<p><strong>Check BillKarma&rsquo;s hospital directory.</strong> BillKarma&rsquo;s <a href="/hospitals/">hospital directory</a> displays parent company information alongside billing grade and markup data. PE-affiliated systems are identified in hospital profiles so you can see both ownership structure and pricing behavior in one place.</p>

<p><strong>Look up the hospital&rsquo;s 990 or corporate registration.</strong> Nonprofit hospitals file IRS Form 990s that list parent organizations. For-profit hospitals are registered with state corporate registries &mdash; searching the registered agent often reveals PE ownership through holding company structures.</p>

<div class="key-takeaway">
    <strong>Already received a bill and want to know if the charges are inflated?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we&rsquo;ll compare every line item against Medicare rates, flag high-markup charges, and identify coding errors worth disputing, regardless of who owns the hospital.
</div>

<h2 id="what-to-do">5. What to do if you&rsquo;re at a PE-owned hospital</h2>

<p><strong>Before a planned procedure:</strong> If you have a scheduled, non-emergency procedure, check your hospital&rsquo;s billing grade and ownership before confirming the booking. If the hospital is PE-owned and carries a D or F billing grade, ask your physician whether an equivalent facility in your network has a better grade. For elective procedures, the price difference between a D-grade and B-grade hospital can be $3,000&ndash;$8,000 on a single admission, even with insurance.</p>

<p><strong>At the time of service:</strong> Ask the admissions or billing department for an estimate of your total charges before any non-emergency service. Under CMS rules, hospitals must provide a good-faith cost estimate for scheduled services. PE hospitals are required to comply with price transparency rules the same as all others &mdash; if they resist, that is a data point worth noting.</p>

<p><strong>After you receive the bill:</strong> Request a complete itemized bill listing every CPT code and charge individually. Do not accept a summary statement. Use the BillKarma calculator or the CMS Medicare fee schedule to look up the Medicare rate for each code. Flag any charge that exceeds 5x Medicare as a priority dispute item.</p>

<p><strong>Dispute specific line items:</strong> Call the billing department and dispute individual high-markup charges with the Medicare rate as your reference. The phrase &ldquo;I see CPT [code] has a 2026 Medicare rate of $[amount]. Your charge of $[amount] is [X]x that rate. I would like to request an adjustment to the negotiated rate&rdquo; is direct and effective.</p>

<p><strong>Request financial assistance:</strong> Even PE-owned for-profit hospitals often have financial assistance programs, either by policy or by state requirement. Ask specifically: &ldquo;What is your financial assistance program income threshold?&rdquo; Many programs reduce or eliminate balances for patients at 200&ndash;400% of the Federal Poverty Level.</p>

<p><strong>File a price transparency complaint:</strong> If the hospital&rsquo;s posted price transparency file is incomplete, non-machine-readable, or missing required data, you can file a complaint with CMS. Hospitals face fines of up to $300 per day for non-compliance. CMS has escalated enforcement since 2023.</p>

<h2 id="case-studies">6. Case studies</h2>

<div class="key-takeaway">
    <strong>Unsure whether your charges are typical for a PE-owned hospital?</strong> Use our <a href="/calculator">Medicare rate calculator</a> &mdash; enter any CPT code from your bill to see the 2026 Medicare benchmark and calculate the markup you&rsquo;re being charged.
</div>

<div class="case-study">
    <h3>Emergency department visit: PE hospital charged 11x Medicare for chest X-ray</h3>
    <p>A patient in rural Tennessee visited the emergency department of a hospital owned by a PE-backed regional system (BillKarma grade: F, average markup 9.4x Medicare) after chest pain. The visit included a Level 5 ED evaluation (CPT 99285), a two-view chest X-ray (CPT 71046), and a troponin lab test (CPT 84484). Her insurance applied a $3,500 deductible before covering anything.</p>
    <div class="bill-example">
        <div class="bill-header">Emergency Department Bill &mdash; PE-owned hospital (F grade)</div>
        <div class="line-item error">
            <span>99285 &mdash; ED Level 5 evaluation &nbsp; &#10060; <em>Medicare rate: $227 &mdash; billed: $2,380 (10.5x)</em></span>
            <span>$2,380</span>
        </div>
        <div class="line-item error">
            <span>71046 &mdash; Chest X-ray, 2 views &nbsp; &#10060; <em>Medicare rate: $13 &mdash; billed: $143 (11.0x)</em></span>
            <span>$143</span>
        </div>
        <div class="line-item flagged">
            <span>84484 &mdash; Troponin lab test &nbsp; &#9888; <em>Medicare rate: $14 &mdash; billed: $98 (7.0x)</em></span>
            <span>$98</span>
        </div>
        <div class="line-total">
            <span>Total billed</span>
            <span>$2,621</span>
        </div>
        <div class="line-total">
            <span>Total at 3x Medicare (reasonable benchmark)</span>
            <span>$762</span>
        </div>
        <div class="line-total">
            <span>Overcharge vs. 3x Medicare benchmark</span>
            <span>$1,859</span>
        </div>
    </div>
    <p>The patient uploaded her bill to BillKarma, which flagged all three line items. She contacted the billing department citing Medicare rates for each CPT code and requested an adjustment. The hospital reduced the ED evaluation charge to $1,200 and wrote off the X-ray charge entirely. <strong>Total recovered: $1,323 off the final balance.</strong></p>
</div>

<div class="case-study">
    <h3>Knee replacement: researching PE ownership before scheduling saved $5,200</h3>
    <p>A patient in Florida needed a total knee replacement (CPT 27447, Medicare facility rate: $1,576) and had three in-network hospitals available. His orthopedic surgeon had privileges at all three. Using BillKarma&rsquo;s hospital directory, he found that the closest facility was PE-owned (LifePoint Health, Apollo Global Management) and carried a D billing grade with an average markup of 7.1x Medicare. The second hospital was a nonprofit with a C grade (4.3x). The third was a community hospital with a B grade (2.8x).</p>
    <p>His plan applied 20% coinsurance after a $2,000 deductible. The PE-owned hospital listed CPT 27447 at $11,190 (7.1x Medicare). The B-grade community hospital listed the same procedure at $4,413 (2.8x Medicare). His coinsurance difference between the two facilities was $1,355, plus the remaining deductible impact. Scheduling at the B-grade hospital rather than the PE-owned D-grade facility saved him approximately $2,600 in direct out-of-pocket costs &mdash; and reduced the total amount billed to his insurer by $6,777. <strong>Estimated total savings accounting for premium and cost-sharing impact: $5,200.</strong></p>
</div>

<div class="case-study">
    <h3>Post-acquisition billing surge: same hospital, two different bills two years apart</h3>
    <p>A patient in Ohio had a CT scan of the abdomen and pelvis with contrast (CPT 74177, Medicare rate: $187) at a regional community hospital in 2021 and again at the same facility in 2023. Between those two visits, the hospital was acquired by a PE-backed system. In 2021, the gross charge for CPT 74177 was $1,840 (9.8x Medicare). In 2023, the same CPT code at the same facility showed a gross charge of $2,640 (14.1x Medicare) &mdash; a 43% increase in gross charges over two years, during a period when the hospital&rsquo;s name, location, and medical staff were largely unchanged.</p>
    <p>The patient&rsquo;s insurance plan had also changed to a higher-deductible design over the same period. Her 2021 cost-sharing for the scan: $184. Her 2023 cost-sharing for the identical scan at the same facility: $412. <strong>A 124% increase in out-of-pocket cost for the same procedure at the same location.</strong> She successfully negotiated the 2023 bill down by $280 by requesting the hospital&rsquo;s &ldquo;self-pay discount&rdquo; rate applied to her cost-sharing obligation.</p>
</div>

{_pe_embed}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How do I know if my hospital is private equity-owned?</h3>
        <p>Search your hospital&rsquo;s parent system name on the Private Equity Stakeholder Project&rsquo;s hospital tracker or the KFF/Peterson Health System Tracker. BillKarma&rsquo;s <a href="/hospitals/">hospital directory</a> also shows parent company information alongside billing grade data. Common PE-affiliated systems include LifePoint Health (Apollo Global), Steward Health Care (formerly Cerberus Capital), and Prospect Medical Holdings (Leonard Green &amp; Partners).</p>
    </div>
    <div class="faq-item">
        <h3>Are PE hospitals legally allowed to charge more?</h3>
        <p>Yes. No federal law caps what hospitals charge. PE hospitals set their own chargemaster prices and negotiate rates with insurers independently. Higher charges are legal. Research consistently shows PE hospitals raise prices faster and further than comparable non-PE hospitals in the same markets, which is why ownership type matters when evaluating your bill.</p>
    </div>
    <div class="faq-item">
        <h3>Does PE ownership affect care quality, not just price?</h3>
        <p>Research suggests it does. A 2023 <em>JAMA</em> study by Kannan et al. found PE-acquired hospitals were associated with higher rates of adverse patient safety events &mdash; falls, infections, and complications &mdash; alongside higher patient charges. Staff-to-patient ratios tend to worsen after acquisition as PE firms reduce labor costs to improve margins before the eventual sale.</p>
    </div>
    <div class="faq-item">
        <h3>What services are most likely to be cut after PE acquisition?</h3>
        <p>PE firms typically close or scale back unprofitable service lines that are expensive to staff and difficult to bill profitably. Obstetrics and labor-and-delivery units, inpatient psychiatric care, and level-one trauma centers are the most frequently eliminated. These services are often underreimbursed by Medicaid and require high staffing ratios that compress margins under the PE cost-cutting model.</p>
    </div>
    <div class="faq-item">
        <h3>Can I dispute charges at a PE-owned hospital the same way as any other hospital?</h3>
        <p>Yes. The same dispute process applies regardless of ownership: request an itemized bill, compare each CPT code to the Medicare rate, and dispute line items that appear inflated. PE hospitals are subject to the same CMS price transparency requirements as all other hospitals. <a href="/scan">Upload your bill to BillKarma</a> to run an automated line-by-line comparison against Medicare rates.</p>
    </div>
    <div class="faq-item">
        <h3>Do insurance companies negotiate differently with PE hospitals?</h3>
        <p>In markets where PE consolidation has reduced competition, insurers have less leverage to negotiate lower rates. A 2023 <em>Health Affairs</em> study found PE hospitals charged commercial insurers 30% more than comparable non-PE hospitals in the same markets. Fewer local hospital alternatives give PE systems more pricing power in contract negotiations, which ultimately flows through to patients as higher premiums and out-of-pocket costs. Learn more about how hospital billing grades relate to ownership in our <a href="/guides/hospital-billing-grades-explained">hospital billing grades guide</a>.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://jamanetwork.com/journals/jama/fullarticle/2810742" target="_blank" rel="noopener">Kannan S, et al. &ldquo;Private Equity Acquisition of Hospitals and Patient Outcomes.&rdquo; <em>JAMA</em>, 2023. Found PE acquisition associated with higher patient charges and adverse events.</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2022.01361" target="_blank" rel="noopener">Health Affairs (2023): PE hospitals had 30% higher prices than non-PE hospitals in comparable markets.</a></li>
    <li><a href="https://www.bmj.com/content/382/bmj-2023-075814" target="_blank" rel="noopener">BMJ (2023): PE ownership associated with increased adverse events and higher patient charges &mdash; systematic review.</a></li>
    <li><a href="https://www.healthsystemtracker.org/brief/private-equity-and-hospitals/" target="_blank" rel="noopener">KFF/Peterson-KFF Health System Tracker: Tracking PE hospital acquisitions &mdash; 450+ since 2010.</a></li>
    <li><a href="https://pestakeholder.org/reports/private-equity-hospitals/" target="_blank" rel="noopener">Private Equity Stakeholder Project: PE Hospital Acquisition Tracker &mdash; staff cuts, service line closures, and financial outcomes.</a></li>
    <li><a href="https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency" target="_blank" rel="noopener">CMS: Hospital Price Transparency Rule &mdash; requirements and enforcement data showing PE hospital markups.</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/hospital-outpatient" target="_blank" rel="noopener">CMS: Outpatient Prospective Payment System (OPPS) &mdash; 2026 Final Rule (source for Medicare benchmark rates).</a></li>
</ul>
""",
})
