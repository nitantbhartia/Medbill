"""Guide: ACL Surgery Cost."""

from guides import register, _embed

register("acl-surgery-cost", {
    "title": "ACL Surgery Cost in 2026: Full Price Breakdown",
    "meta_description": "ACL reconstruction costs $20,000-$40,000 without insurance. With insurance, expect $2,000-$6,000. See costs by graft type, setting, and how to save.",
    "published": "2026-04-04",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does ACL surgery cost without insurance?",
            "a": "ACL reconstruction (CPT 29888) costs $20,000-$40,000 without insurance at a hospital. This includes the surgeon's fee ($3,000-$6,000), anesthesia ($1,500-$3,000), facility charges ($10,000-$20,000), and the graft. At an ambulatory surgery center, total costs drop to $12,000-$22,000.",
        },
        {
            "q": "How much does ACL surgery cost with insurance?",
            "a": "With insurance, most patients pay $2,000-$6,000 out of pocket for ACL reconstruction, depending on their deductible and coinsurance. If you have a high-deductible plan ($3,000+), you may pay your full deductible plus coinsurance. Many patients hit their out-of-pocket maximum with the surgery plus months of physical therapy.",
        },
        {
            "q": "Does insurance cover ACL surgery?",
            "a": "Yes, ACL reconstruction is almost always covered by private insurance and Medicare when medically necessary (documented ACL tear with instability). Prior authorization may be required. Insurance may prefer that you complete a course of physical therapy (prehab) before approving surgery.",
        },
        {
            "q": "What is the difference in cost between autograft and allograft ACL surgery?",
            "a": "Autograft (using your own tissue, typically patellar tendon or hamstring) adds minimal cost since the tissue is free. Allograft (donor tissue) adds $2,000-$5,000 for the graft itself. Autograft has slightly lower re-tear rates in younger athletes. Allograft has a faster early recovery. Clinical outcomes are similar for most patients over 30.",
        },
        {
            "q": "How much does physical therapy cost after ACL surgery?",
            "a": "Post-ACL physical therapy typically runs $3,000-$8,000 for 6-9 months of sessions (2-3x per week initially, tapering to 1x). With insurance, copays of $30-75 per visit add up to $1,500-$4,500 over the full course. PT is essential for recovery and shouldn't be skipped to save money.",
        },
    ],
    "body": f"""
<p class="lead">An ACL tear is one of the most common sports injuries, and reconstruction surgery costs <strong>$20,000&ndash;$40,000</strong> at a hospital before insurance. Add 6&ndash;9 months of physical therapy, and total costs can reach <strong>$28,000&ndash;$48,000</strong>. But choosing the right setting and understanding your graft options can save thousands. Here&rsquo;s the complete breakdown.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-breakdown">Full cost breakdown</a></li>
        <li><a href="#graft-types">Graft types and costs</a></li>
        <li><a href="#insurance">Cost with vs. without insurance</a></li>
        <li><a href="#hospital-vs-asc">Hospital vs. surgery center</a></li>
        <li><a href="#pt-costs">Physical therapy recovery costs</a></li>
        <li><a href="#lower-bill">5 ways to lower your ACL surgery bill</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-breakdown">1. Full cost breakdown</h2>

<table>
    <thead>
        <tr><th>Component</th><th>CPT Code</th><th>Hospital Charge</th><th>ASC Charge</th><th>Medicare Rate</th></tr>
    </thead>
    <tbody>
        <tr><td>Surgeon&rsquo;s fee (ACL reconstruction)</td><td>29888</td><td>$3,000&ndash;$6,000</td><td>$2,500&ndash;$4,500</td><td>~$1,200&ndash;$1,600</td></tr>
        <tr><td>Anesthesia (2&ndash;3 hours)</td><td>01382</td><td>$1,500&ndash;$3,000</td><td>$1,000&ndash;$2,000</td><td>~$600&ndash;$900</td></tr>
        <tr><td>Facility fee</td><td>&mdash;</td><td>$10,000&ndash;$20,000</td><td>$5,000&ndash;$10,000</td><td>Varies</td></tr>
        <tr><td>Allograft tissue (if used)</td><td>&mdash;</td><td>$2,000&ndash;$5,000</td><td>$2,000&ndash;$4,000</td><td>Bundled or separate</td></tr>
        <tr><td>Pre-op MRI</td><td>73721</td><td>$1,000&ndash;$3,000</td><td>&mdash;</td><td>~$250&ndash;$500</td></tr>
        <tr><td>Post-op brace</td><td>L1845</td><td>$200&ndash;$800</td><td>$200&ndash;$600</td><td>~$100&ndash;$250</td></tr>
        <tr><td>Post-op medications</td><td>Various</td><td>$50&ndash;$300</td><td>$50&ndash;$300</td><td>Part D</td></tr>
    </tbody>
</table>

{_embed(mode="cost", cpt="29888", title="Look Up ACL Surgery Cost", subtitle="See Medicare rates for CPT 29888 in your area.")}

<h2 id="graft-types">2. Graft types and costs</h2>

<table>
    <thead>
        <tr><th>Graft Type</th><th>Source</th><th>Added Cost</th><th>Re-tear Rate</th><th>Best For</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Patellar tendon autograft</strong></td><td>Your own kneecap tendon</td><td>$0 (included)</td><td>~3&ndash;5%</td><td>Young athletes, high-demand sports</td></tr>
        <tr><td><strong>Hamstring autograft</strong></td><td>Your own hamstring tendon</td><td>$0 (included)</td><td>~5&ndash;7%</td><td>Less anterior knee pain, recreational athletes</td></tr>
        <tr><td><strong>Quadriceps tendon autograft</strong></td><td>Your own quad tendon</td><td>$0 (included)</td><td>~4&ndash;6%</td><td>Revision surgery, larger graft needed</td></tr>
        <tr><td><strong>Allograft (donor tissue)</strong></td><td>Cadaver tissue</td><td>$2,000&ndash;$5,000</td><td>~8&ndash;12% (higher in young athletes)</td><td>Older patients, lower-demand activities, revision</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>For athletes under 25:</strong> Autograft (your own tissue) has significantly lower re-tear rates. Allograft is associated with higher failure rates in young, active patients. The cost savings of avoiding allograft ($2,000&ndash;$5,000) are a bonus.
</div>

<h2 id="insurance">3. Cost with vs. without insurance</h2>

<table>
    <thead>
        <tr><th>Coverage</th><th>Surgery Cost</th><th>Your Out-of-Pocket (surgery only)</th></tr>
    </thead>
    <tbody>
        <tr><td>Employer PPO</td><td>$20,000&ndash;$40,000 billed</td><td>$2,000&ndash;$6,000</td></tr>
        <tr><td>High-deductible (HDHP)</td><td>$20,000&ndash;$40,000 billed</td><td>$3,000&ndash;$8,000 (may hit OOP max)</td></tr>
        <tr><td>Medicare</td><td>~$8,000&ndash;$12,000 (Medicare rate)</td><td>$1,676 deductible + 20% coinsurance</td></tr>
        <tr><td>Uninsured (hospital)</td><td>$25,000&ndash;$45,000</td><td>Full amount (negotiate 40&ndash;60% off)</td></tr>
        <tr><td>Uninsured (ASC)</td><td>$12,000&ndash;$22,000</td><td>Full amount</td></tr>
    </tbody>
</table>

<div class="case-study">
    <h3>College athlete saves $14,000 by choosing an ASC</h3>
    <p>A 20-year-old college soccer player in Texas tore her ACL. Her parents&rsquo; high-deductible insurance plan had a $5,000 deductible. The hospital quoted $36,000; a sports medicine ASC quoted $18,500 for the same surgeon. At the hospital, she&rsquo;d pay $5,000 deductible + 20% of $31,000 = ~$11,200. At the ASC, she paid $5,000 deductible + 20% of $13,500 = ~$7,700. <strong>Savings: $3,500</strong> out of pocket, and her insurer saved $17,500.</p>
</div>

<h2 id="hospital-vs-asc">4. Hospital vs. surgery center</h2>

<table>
    <thead>
        <tr><th>Factor</th><th>Hospital</th><th>ASC</th></tr>
    </thead>
    <tbody>
        <tr><td>Total cost</td><td>$20,000&ndash;$40,000</td><td>$12,000&ndash;$22,000</td></tr>
        <tr><td>Savings</td><td>&mdash;</td><td>35&ndash;45%</td></tr>
        <tr><td>Typical stay</td><td>Same-day or 1 night</td><td>Same-day (go home 2&ndash;4 hours after)</td></tr>
        <tr><td>Complication rates</td><td>Comparable</td><td>Comparable</td></tr>
    </tbody>
</table>

<p>ACL reconstruction is one of the most commonly performed procedures at orthopedic ASCs. Find one near you: <a href="/surgery-centers/">BillKarma Surgery Center Directory</a>.</p>

<h2 id="pt-costs">5. Physical therapy recovery costs</h2>

<p>PT is the biggest post-surgical expense and is non-negotiable for a full recovery:</p>

<table>
    <thead>
        <tr><th>Phase</th><th>Timeline</th><th>Frequency</th><th>Cost per Session</th><th>Subtotal</th></tr>
    </thead>
    <tbody>
        <tr><td>Phase 1: Protection</td><td>Weeks 1&ndash;6</td><td>2&ndash;3x/week</td><td>$130&ndash;$200</td><td>$1,560&ndash;$3,600</td></tr>
        <tr><td>Phase 2: Strengthening</td><td>Weeks 6&ndash;16</td><td>2x/week</td><td>$130&ndash;$200</td><td>$2,600&ndash;$4,000</td></tr>
        <tr><td>Phase 3: Sport-specific</td><td>Months 4&ndash;9</td><td>1&ndash;2x/week</td><td>$130&ndash;$200</td><td>$2,600&ndash;$4,800</td></tr>
    </tbody>
</table>

<p><strong>Total PT cost: $3,000&ndash;$8,000</strong> (50&ndash;70 sessions over 6&ndash;9 months). With insurance copays of $30&ndash;$75/visit, expect $1,500&ndash;$4,500 out of pocket for PT alone. See our <a href="/guides/physical-therapy-billing">physical therapy billing guide</a> for tips on reducing PT costs.</p>

<h2 id="lower-bill">6. 5 ways to lower your ACL surgery bill</h2>

<h3>a) Choose an ASC</h3>
<p>Saves 35&ndash;45% on the facility fee. Most ACL reconstructions are done outpatient anyway.</p>

<h3>b) Choose autograft over allograft</h3>
<p>Saves $2,000&ndash;$5,000 in graft costs and has lower re-tear rates for young athletes.</p>

<h3>c) Get your MRI at a freestanding imaging center</h3>
<p>A knee MRI costs $1,000&ndash;$3,000 at a hospital but $300&ndash;$700 at a freestanding imaging center. Same machine, same quality. See our <a href="/imaging/">imaging center directory</a>.</p>

<h3>d) Time surgery strategically</h3>
<p>If you&rsquo;ve already met your deductible this year (from the ER visit or MRI), schedule surgery in the same calendar year. If not, consider whether January surgery (fresh deductible but 12 months of PT in one plan year) or late-year surgery makes more sense.</p>

<h3>e) Audit the bill</h3>
<p>Common ACL billing errors: duplicate charges for disposable arthroscopic instruments, inflated brace charges, and separate billing for procedures bundled in the primary CPT code. <a href="/scan">Upload to BillKarma</a> to catch these.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does ACL surgery cost without insurance?</h3>
        <p>$20,000&ndash;$40,000 at a hospital, $12,000&ndash;$22,000 at an ASC. Add $3,000&ndash;$8,000 for 6&ndash;9 months of physical therapy.</p>
    </div>

    <div class="faq-item">
        <h3>How much does ACL surgery cost with insurance?</h3>
        <p>$2,000&ndash;$6,000 for the surgery, plus $1,500&ndash;$4,500 in PT copays over 6&ndash;9 months. Many patients hit their out-of-pocket maximum.</p>
    </div>

    <div class="faq-item">
        <h3>Does insurance cover ACL surgery?</h3>
        <p>Yes, when medically necessary (documented tear with instability). Prior authorization may be required. Some plans require prehab PT before approving surgery.</p>
    </div>

    <div class="faq-item">
        <h3>What is the cost difference between autograft and allograft?</h3>
        <p>Allograft adds $2,000&ndash;$5,000 for donor tissue. Autograft (your own tissue) is included in the surgery cost. For athletes under 25, autograft has lower re-tear rates and is cheaper.</p>
    </div>

    <div class="faq-item">
        <h3>How much does physical therapy cost after ACL surgery?</h3>
        <p>$3,000&ndash;$8,000 total for 50&ndash;70 sessions over 6&ndash;9 months. With insurance copays of $30&ndash;$75/visit, expect $1,500&ndash;$4,500 out of pocket.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener noreferrer">CMS: Medicare Physician Fee Schedule (CPT 29888)</a></li>
    <li><a href="https://www.aaos.org/quality/quality-programs/acl-reconstruction/" target="_blank" rel="noopener noreferrer">AAOS: ACL Reconstruction Clinical Practice Guidelines</a></li>
    <li><a href="https://www.hcup-us.ahrq.gov/" target="_blank" rel="noopener noreferrer">AHRQ HCUP: Hospital Costs for Knee Procedures</a></li>
    <li><a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener noreferrer">PubMed: Autograft vs. Allograft ACL Outcomes Meta-analyses</a></li>
    <li><a href="https://www.apta.org/" target="_blank" rel="noopener noreferrer">APTA: Physical Therapy Guidelines for ACL Rehabilitation</a></li>
</ul>
""",
})
