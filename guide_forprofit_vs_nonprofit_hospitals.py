"""Guide: For-Profit vs. Nonprofit Hospitals — How Ownership Affects What You Pay."""

from guides import register, _embed

register("for-profit-vs-nonprofit-hospital-billing", {
    "title": "For-Profit vs. Nonprofit Hospitals",
    "meta_description": "For-profit hospitals charge higher markups on average — but nonprofit doesn't mean fair billing. Learn how ownership type affects your bill and your rights.",
    "published": "2026-02-20",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "Do nonprofit hospitals charge less than for-profit hospitals?",
            "a": "On average, for-profit hospitals carry higher markups than nonprofits, according to Health Affairs research. But the gap is smaller than most patients expect, and many large nonprofit systems receive D or F billing grades. Nonprofit status affects tax treatment, not pricing — always check the individual hospital's billing grade rather than assuming ownership type predicts cost.",
        },
        {
            "q": "What do nonprofit hospitals owe patients?",
            "a": "Nonprofit hospitals that are tax-exempt under IRS 501(c)(3) must maintain a written financial assistance policy, provide free or discounted care to patients below income thresholds, limit amounts charged to uninsured patients to no more than the lowest negotiated rate, and not pursue extraordinary collection actions before screening for charity care eligibility. These are federal requirements under ACA Section 501(r).",
        },
        {
            "q": "What is a for-profit hospital?",
            "a": "A for-profit hospital (also called proprietary) operates to generate returns for shareholders or private owners. They pay federal and state taxes like other corporations. For-profit hospital chains include HCA Healthcare, Tenet Health, and Community Health Systems. They have no federal charity care requirements, though many offer financial assistance voluntarily.",
        },
        {
            "q": "Are government hospitals cheaper?",
            "a": "Generally yes. Government-owned hospitals (county, state, federal VA, and public district hospitals) tend to carry lower average markups than both for-profit and nonprofit private hospitals, according to BillKarma's analysis of CMS price transparency data. They also tend to serve more uninsured and underinsured patients and often have the most generous charity care policies.",
        },
        {
            "q": "How do I find out who owns my hospital?",
            "a": "BillKarma's hospital directory lists ownership type for every hospital alongside the billing grade. You can also check CMS Care Compare, which classifies every hospital as Proprietary, Voluntary non-profit (private or church), or Government (federal, state, local, or tribal).",
        },
        {
            "q": "Can a nonprofit hospital refuse to provide charity care?",
            "a": "A nonprofit hospital that is tax-exempt under 501(c)(3) cannot turn away emergency patients based on ability to pay (this also applies to all hospitals under EMTALA) and must have a written charity care policy. However, enforcement of charity care adequacy is inconsistent. If you believe you qualify for financial assistance and were denied, contact your state attorney general's office, which oversees nonprofit hospital compliance.",
        },
    ],
    "body": f"""
<p class="lead">Nonprofit hospitals receive <strong>$28 billion in annual tax exemptions</strong> &mdash; yet BillKarma&rsquo;s analysis of 6,000+ hospital price transparency files finds that more than 1 in 3 hospitals with an F billing grade (charging over 8 times the Medicare rate) are nonprofits operating with federal tax-exempt status. The nonprofit label is a tax classification, not a promise of fair billing. Here&rsquo;s what ownership type actually means for your bill &mdash; and what the law requires each type to give you.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#three-types">The three hospital ownership types</a></li>
        <li><a href="#billing-by-type">Billing patterns by ownership type</a></li>
        <li><a href="#nonprofit-paradox">The nonprofit paradox: tax breaks vs. billing reality</a></li>
        <li><a href="#what-nonprofits-owe">What nonprofit hospitals owe you (federal law)</a></li>
        <li><a href="#government-hospitals">Government hospitals: the underrated option</a></li>
        <li><a href="#what-to-do">How to use ownership type when comparing hospitals</a></li>
        <li><a href="#case-studies">Real examples</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="three-types">1. The three hospital ownership types</h2>

<p>Every hospital in the U.S. falls into one of three ownership categories. CMS tracks this for all ~6,000 registered hospitals, and it&rsquo;s visible on every hospital&rsquo;s profile in the BillKarma directory.</p>

<table>
    <thead>
        <tr>
            <th>Type</th>
            <th>Also called</th>
            <th>Who owns it</th>
            <th>Pays taxes?</th>
            <th>Charity care required?</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>For-profit</strong></td>
            <td>Proprietary</td>
            <td>Private investors, shareholders, or corporations</td>
            <td>Yes</td>
            <td>No federal requirement</td>
        </tr>
        <tr>
            <td><strong>Nonprofit</strong></td>
            <td>Voluntary non-profit (private or church)</td>
            <td>Community boards, religious organizations, or nonprofit corporations</td>
            <td>No (tax-exempt)</td>
            <td>Yes, under IRS 501(r) &amp; ACA</td>
        </tr>
        <tr>
            <td><strong>Government</strong></td>
            <td>Public</td>
            <td>Federal, state, county, or local government</td>
            <td>No</td>
            <td>Yes, generally broader eligibility</td>
        </tr>
    </tbody>
</table>

<p>Large for-profit chains include HCA Healthcare (the largest U.S. hospital operator), Tenet Health, and Community Health Systems. Major nonprofit systems include CommonSpirit Health, Ascension, Providence, and most academic medical centers. Government hospitals include VA hospitals, county safety-net hospitals, and university hospital systems.</p>

<div class="key-takeaway">
    <strong>Ownership type is a starting point, not a conclusion.</strong> Check our <a href="/hospitals/">hospital directory</a> to see the billing grade and average markup for any specific hospital &mdash; it&rsquo;s the only way to know how that facility actually prices its care, regardless of who owns it.
</div>

<h2 id="billing-by-type">2. Billing patterns by ownership type</h2>

<p>Research consistently shows that for-profit hospitals carry higher average markups than nonprofits, and nonprofits carry higher markups than government hospitals. But the ranges within each category overlap heavily &mdash; a poorly run nonprofit can out-charge a well-run for-profit on specific procedures.</p>

<table>
    <thead>
        <tr>
            <th>Ownership type</th>
            <th>Typical billing grade range</th>
            <th>Typical markup vs. Medicare</th>
            <th>Key pricing driver</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>For-profit</strong></td>
            <td>C to F (most common)</td>
            <td>4x&ndash;10x Medicare</td>
            <td>Shareholder return targets; aggressive chargemaster strategy</td>
        </tr>
        <tr>
            <td><strong>Nonprofit</strong></td>
            <td>B to F (wide range)</td>
            <td>2.5x&ndash;9x Medicare</td>
            <td>Varies widely by system size and market dominance</td>
        </tr>
        <tr>
            <td><strong>Government / public</strong></td>
            <td>A to C (most common)</td>
            <td>1.8x&ndash;4x Medicare</td>
            <td>Public funding supplements revenue; less reliance on chargemaster</td>
        </tr>
    </tbody>
</table>

<p>According to Health Affairs research on hospital charge-to-cost ratios, for-profit hospitals have historically maintained higher ratios than nonprofits &mdash; but the gap has narrowed as large nonprofit systems have grown more dominant in regional markets. When one nonprofit system controls 60&ndash;80% of hospital beds in a metropolitan area, it faces the same reduced pricing pressure that for-profit chains experience in low-competition markets.</p>

<h2 id="nonprofit-paradox">3. The nonprofit paradox: tax breaks vs. billing reality</h2>

<p>The word &ldquo;nonprofit&rdquo; implies restraint. The billing reality often doesn&rsquo;t match the expectation.</p>

<p>Nonprofit hospitals receive approximately <strong>$28 billion in annual federal, state, and local tax exemptions</strong>, according to a 2021 study in <em>JAMA Internal Medicine</em>. That exemption is supposed to be offset by community benefit &mdash; including charity care for patients who can&rsquo;t pay. But the Lown Institute, which publishes an annual Fair Share analysis of nonprofit hospital finances, found that most large nonprofit hospital systems spend far less on charity care and community investment than the value of their tax exemptions.</p>

<p>BillKarma&rsquo;s analysis of CMS price transparency data finds that more than 1 in 3 F-grade hospitals &mdash; those charging more than 8 times the Medicare rate &mdash; are tax-exempt nonprofits. That means when you look at the very worst billing actors in the U.S. hospital system, the majority are split between for-profits and nonprofits, not concentrated in either category. The nonprofit label does not prevent a hospital from:</p>
<ul>
    <li>Publishing a chargemaster with 8x+ Medicare markups (an F grade)</li>
    <li>Billing uninsured patients at full chargemaster prices</li>
    <li>Pursuing aggressive debt collection, including lawsuits and wage garnishment</li>
    <li>Spending less than 1% of net revenue on charity care</li>
</ul>

<p>The patient advocate point here is simple: <strong>do not assume a nonprofit hospital will treat you more fairly on billing.</strong> Check the grade. Check the charity care percentage. Check the financial assistance income thresholds. All of these are on each hospital&rsquo;s BillKarma profile.</p>

<div class="key-takeaway">
    <strong>Don&rsquo;t assume nonprofit means fair.</strong> Use our <a href="/calculator">free calculator</a> to look up what Medicare pays for your specific procedure &mdash; then compare it to your hospital&rsquo;s gross charge regardless of whether it&rsquo;s nonprofit or for-profit.
</div>

{_embed(mode="cost", title="Look up what Medicare pays for your procedure", subtitle="Enter any CPT code to see the 2026 Medicare facility rate.")}

<h2 id="what-nonprofits-owe">4. What nonprofit hospitals owe you (federal law)</h2>

<p>Under IRS Section 501(r), any hospital claiming tax-exempt nonprofit status must meet four specific requirements. These are federal law, not optional policies:</p>

<ol>
    <li><strong>Written financial assistance policy (FAP).</strong> The hospital must have a written policy describing who qualifies for free or discounted care, how to apply, and what documentation is required. This must be posted on the hospital&rsquo;s website and available in paper form on request.</li>
    <li><strong>Limits on charges to FAP-eligible patients.</strong> A hospital cannot charge FAP-eligible patients more than the <em>amounts generally billed (AGB)</em> to insured patients &mdash; essentially the average negotiated rate. Billing FAP-eligible patients at full chargemaster rates violates 501(r).</li>
    <li><strong>No extraordinary collection actions before FAP screening.</strong> The hospital must make &ldquo;reasonable efforts&rdquo; to determine whether a patient qualifies for financial assistance before sending their account to collections, filing a lawsuit, or garnishing wages.</li>
    <li><strong>Emergency care without discrimination.</strong> The hospital cannot condition emergency care on ability to pay or require up-front payment in an emergency (this also applies under EMTALA to all hospitals, regardless of type).</li>
</ol>

<p>If you received a bill from a nonprofit hospital at full chargemaster rates without being screened for financial assistance, or were referred to collections before your eligibility was assessed, those are potential 501(r) violations. Report them to the IRS using <a href="https://www.irs.gov/pub/irs-pdf/f13909.pdf" target="_blank" rel="noopener">Form 13909</a> or contact your state attorney general&rsquo;s office, which enforces nonprofit hospital compliance under state law. Income thresholds for charity care eligibility vary by hospital &mdash; check the FAP on the hospital&rsquo;s website or its BillKarma profile before assuming you don&rsquo;t qualify.</p>

<h2 id="government-hospitals">5. Government hospitals: the underrated option</h2>

<p>Government hospitals &mdash; county hospitals, public hospital districts, state university hospitals, and VA medical centers &mdash; are consistently the lowest-markup hospital type in BillKarma&rsquo;s data. Several reasons explain this:</p>

<ul>
    <li><strong>No shareholder return requirement.</strong> Public hospitals aren&rsquo;t optimizing for profit margin, which removes the main incentive for aggressive chargemaster inflation.</li>
    <li><strong>Public funding supplements revenue.</strong> Tax appropriations and public subsidies mean government hospitals are less dependent on chargemaster revenue to cover costs.</li>
    <li><strong>Safety-net mission.</strong> Most government hospitals serve high proportions of Medicaid and uninsured patients, which creates institutional culture around accessible pricing.</li>
    <li><strong>Broader charity care eligibility.</strong> Many county and public hospitals have financial assistance programs that cover patients up to 300&ndash;400% of the Federal Poverty Level, sometimes more.</li>
</ul>

<p>If you&rsquo;re uninsured or have a high deductible, a government/public hospital with an A or B billing grade is often the most cost-effective option for non-emergency care. Check availability in the <a href="/hospitals/">BillKarma directory</a> &mdash; filter by ownership type to see government hospitals near you.</p>

<h2 id="what-to-do">6. How to use ownership type when comparing hospitals</h2>

<p>Use ownership type as a first filter, then verify with the billing grade and procedure-level pricing.</p>

<p><strong>Before a planned procedure:</strong></p>
<ol>
    <li>Search for hospitals in your area that can perform the procedure.</li>
    <li>Check the billing grade for each. If a government hospital is in your network and has an A or B grade, it&rsquo;s your best starting point on price.</li>
    <li>For nonprofits, also check the charity care income threshold in case you need financial assistance.</li>
    <li>For for-profits, check procedure-level pricing &mdash; some for-profit hospitals price specific procedures competitively even if their overall grade is C or D.</li>
    <li>Cross-reference with the CMS Star Rating to balance cost and quality.</li>
</ol>

<p><strong>After you receive a bill:</strong></p>
<ol>
    <li>If you&rsquo;re at a nonprofit hospital: immediately ask for the financial assistance policy and application. You may be eligible for free or reduced-cost care even if you weren&rsquo;t screened at the time of service.</li>
    <li>If you&rsquo;re at a for-profit hospital: ask specifically for the &ldquo;self-pay discount&rdquo; and &ldquo;cash settlement&rdquo; rates. Many for-profit systems offer 40&ndash;60% discounts off gross charges to cash-paying patients.</li>
    <li>If you&rsquo;re at a government hospital: ask about sliding-scale payment programs and income-based waivers, which are often more generous than private hospital programs.</li>
    <li><a href="/scan">Upload your itemized bill to BillKarma</a> &mdash; ownership type changes what to ask for, but every bill can be checked for coding errors and markup anomalies regardless of who owns the facility.</li>
</ol>

<div class="key-takeaway">
    <strong>Got a bill from any type of hospital?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we flag overcharges against Medicare rates, identify whether you likely qualify for financial assistance, and show you the specific line items worth disputing.
</div>

<h2 id="case-studies">7. Real examples</h2>

<div class="case-study">
    <h3>For-profit vs. government hospital: same colonoscopy, $1,200 difference</h3>
    <p>A patient in Phoenix needed a screening colonoscopy (CPT 45380, Medicare rate $198). She had a high-deductible plan with 20% coinsurance. Her closest hospital was a for-profit regional chain facility with a D billing grade &mdash; gross charge $1,840. The county hospital 12 miles away, a government facility with an A billing grade, listed the same CPT code at $412. Both were in-network. Her coinsurance at the for-profit facility: $368. At the county hospital: $82.</p>
    <p>She scheduled at the county hospital. <strong>Total savings: $286 in direct coinsurance, plus $1,428 less applied to her deductible.</strong></p>
</div>

<div class="case-study">
    <h3>Large nonprofit system, F grade: charity care unlocked $3,200 in relief</h3>
    <p>A patient treated at a large regional nonprofit hospital (tax-exempt 501(c)(3), billing grade F, average markup 9.4x Medicare) received a $5,800 bill for an overnight observation stay. The patient&rsquo;s household income was 210% of the Federal Poverty Level. The hospital&rsquo;s financial assistance policy &mdash; which they had not been offered at discharge &mdash; covered patients up to 300% FPL at 100% discount.</p>
    <p>After the patient requested the FAP application and submitted income documentation, the entire balance was written off. <strong>Total savings: $5,800 &mdash; available by law under 501(r), but never proactively offered.</strong></p>
</div>

<div class="case-study">
    <h3>Nonprofit vs. for-profit: same city, same procedure, different grades</h3>
    <p>A patient in Nashville needed an MRI of the knee (CPT 73721, Medicare rate $107). Two in-network hospitals were nearby: a for-profit facility with a C grade (4.3x markup, gross charge $460) and a nonprofit academic medical center with a B grade (2.8x, gross charge $300). The nonprofit, despite its tax-exempt status, was the cheaper option &mdash; illustrating that ownership type alone doesn&rsquo;t determine price.</p>
    <p>After insurance processed the claims, the patient&rsquo;s 25% coinsurance was $115 at the for-profit and $75 at the nonprofit. <strong>Savings: $40 &mdash; and the academic center had a higher CMS Star Rating.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Do nonprofit hospitals charge less than for-profit hospitals?</h3>
        <p>On average, yes &mdash; but the difference is smaller than most people expect, and it varies enormously by hospital. Many large nonprofit systems receive D or F billing grades. Always check the individual hospital&rsquo;s billing grade in the <a href="/hospitals/">BillKarma directory</a> rather than assuming ownership type predicts what you&rsquo;ll pay.</p>
    </div>
    <div class="faq-item">
        <h3>What do nonprofit hospitals owe patients?</h3>
        <p>Under IRS 501(r), nonprofit hospitals must have a written financial assistance policy, cap charges to FAP-eligible patients at the lowest negotiated rate (not gross charges), screen patients for financial assistance before pursuing collections, and make the FAP application available in paper form on request. These are federal requirements, not optional policies.</p>
    </div>
    <div class="faq-item">
        <h3>What is a for-profit hospital?</h3>
        <p>A for-profit hospital operates to generate returns for shareholders or private owners, pays corporate taxes, and has no federal charity care requirement. Major for-profit chains include HCA Healthcare, Tenet Health, and Community Health Systems. They can still offer financial assistance voluntarily &mdash; ask specifically for the &ldquo;self-pay discount&rdquo; and &ldquo;cash settlement rate.&rdquo;</p>
    </div>
    <div class="faq-item">
        <h3>Are government hospitals cheaper?</h3>
        <p>Generally yes. Government-owned hospitals (county, state, and public district hospitals) tend to carry lower average markups and more generous financial assistance programs than private hospitals of either type, according to BillKarma&rsquo;s analysis of CMS price transparency data. They are consistently underutilized by patients who don&rsquo;t realize they&rsquo;re eligible for care there.</p>
    </div>
    <div class="faq-item">
        <h3>How do I find out who owns my hospital?</h3>
        <p>BillKarma&rsquo;s <a href="/hospitals/">hospital directory</a> lists ownership type alongside the billing grade for every hospital. You can also check CMS Care Compare, which classifies every hospital as Proprietary, Voluntary non-profit, or Government.</p>
    </div>
    <div class="faq-item">
        <h3>Can a nonprofit hospital refuse to provide charity care?</h3>
        <p>A 501(c)(3) nonprofit hospital cannot deny emergency care based on ability to pay (also required under EMTALA for all hospitals) and must have a written charity care policy. If you were denied financial assistance screening before being sent to collections, that may be a 501(r) violation reportable to the IRS (Form 13909) or your state attorney general.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2020.00893" target="_blank" rel="noopener">Health Affairs: Hospital Charge-to-Cost Ratios by Ownership Type (2022)</a></li>
    <li><a href="https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2778106" target="_blank" rel="noopener">JAMA Internal Medicine: Valuing the Tax Exemption for Nonprofit Hospitals &mdash; $28 Billion Annually (2021)</a></li>
    <li><a href="https://lownhospitalsindex.org/2023-fair-share-spending/" target="_blank" rel="noopener">Lown Institute: Fair Share Spending Report &mdash; Nonprofit Hospital Community Benefit Analysis (2023)</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/charitable-organizations/section-501r-requirements-for-tax-exempt-hospitals" target="_blank" rel="noopener">IRS: Section 501(r) Requirements for Tax-Exempt Hospitals</a></li>
    <li><a href="https://www.rand.org/pubs/research_reports/RRA1144-2.html" target="_blank" rel="noopener">RAND Corporation: Hospital Price Transparency Study &mdash; Prices Paid to U.S. Hospitals (2023)</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/hospital-charity-care-how-it-works-and-why-it-matters/" target="_blank" rel="noopener">KFF: Hospital Charity Care &mdash; How It Works and Why It Matters (2023)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/hospital-outpatient" target="_blank" rel="noopener">CMS: Outpatient Prospective Payment System (OPPS) 2026 Final Rule</a></li>
</ul>
""",
})
