"""Guide: Cataract Surgery Cost."""

from guides import register, _embed

register("cataract-surgery-cost", {
    "title": "Cataract Surgery Cost in 2026: What You'll Actually Pay",
    "meta_description": "Cataract surgery costs $3,500-$7,000 per eye. Medicare covers 80%. See the full breakdown by lens type, hospital vs ASC savings, and how to reduce your bill.",
    "published": "2026-04-04",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does cataract surgery cost per eye?",
            "a": "Standard cataract surgery (CPT 66984) costs $3,500-$7,000 per eye at a hospital, or $2,000-$3,500 at an ambulatory surgery center. This includes the surgeon's fee, facility fee, anesthesia, and a standard monofocal intraocular lens (IOL). If you choose a premium lens (multifocal or toric), add $1,500-$4,000 per eye out of pocket, as insurance and Medicare don't cover the upgrade.",
        },
        {
            "q": "Does Medicare cover cataract surgery?",
            "a": "Yes. Medicare Part B covers standard cataract surgery including a basic monofocal IOL. You pay 20% coinsurance after the $257 annual Part B deductible. At an ASC, your 20% of ~$1,050 is about $210 per eye. At a hospital, 20% of ~$2,100 is about $420 per eye. Medicare does NOT cover premium IOL upgrades\u2014those are 100% out of pocket.",
        },
        {
            "q": "What is the difference between standard and premium cataract lenses?",
            "a": "A standard monofocal IOL ($150-$500, covered by insurance) corrects vision at one distance\u2014you'll likely still need reading glasses. Premium IOLs include: multifocal ($2,000-$4,000, corrects near and far), toric ($1,500-$3,000, corrects astigmatism), and extended depth of focus ($2,500-$3,500). Premium lenses are not covered by insurance or Medicare.",
        },
        {
            "q": "Is cataract surgery cheaper at a surgery center?",
            "a": "Yes, typically 45-55% cheaper. Medicare pays ASCs about $1,050 for cataract surgery vs. $2,100 at hospital outpatient departments. Your 20% coinsurance is calculated on the lower ASC rate, saving you about $210 per eye. Most cataract surgeries are performed at ASCs, and outcomes are equivalent to hospitals.",
        },
        {
            "q": "Should I have both eyes done at the same time?",
            "a": "Most surgeons do one eye at a time, waiting 1-4 weeks between eyes. This is safer (lower infection risk) and lets the first eye heal so the second eye's lens can be optimized. Cost-wise, doing both in the same calendar year means you only meet your deductible once. If you're close to your out-of-pocket max, timing both in the same year saves money.",
        },
    ],
    "body": f"""
<p class="lead">Cataract surgery is the most commonly performed surgery in the United States&mdash;over <strong>4 million procedures per year</strong>. A standard procedure costs <strong>$3,500&ndash;$7,000 per eye</strong> at a hospital, but only <strong>$2,000&ndash;$3,500 at a surgery center</strong>. Medicare covers it, but premium lens upgrades are 100% out of pocket. Here&rsquo;s the full breakdown.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-breakdown">Full cost breakdown</a></li>
        <li><a href="#lens-options">Lens options and costs</a></li>
        <li><a href="#medicare-coverage">Medicare coverage</a></li>
        <li><a href="#hospital-vs-asc">Hospital vs. surgery center</a></li>
        <li><a href="#insurance">Insurance coverage</a></li>
        <li><a href="#both-eyes">Timing: both eyes strategy</a></li>
        <li><a href="#lower-cost">5 ways to lower your cataract surgery cost</a></li>
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
        <tr><td>Surgeon&rsquo;s fee</td><td>66984</td><td>$1,500&ndash;$3,000</td><td>$1,200&ndash;$2,000</td><td>~$650&ndash;$750</td></tr>
        <tr><td>Facility fee</td><td>&mdash;</td><td>$2,000&ndash;$4,000</td><td>$800&ndash;$1,500</td><td>HOPD ~$2,100 / ASC ~$1,050</td></tr>
        <tr><td>Anesthesia (topical + IV sedation)</td><td>00142</td><td>$500&ndash;$1,000</td><td>$300&ndash;$600</td><td>~$200&ndash;$350</td></tr>
        <tr><td>Standard IOL (monofocal)</td><td>V2632</td><td>$150&ndash;$500</td><td>$150&ndash;$400</td><td>Included</td></tr>
        <tr><td>Pre-op testing (biometry, OCT)</td><td>76519/92134</td><td>$200&ndash;$600</td><td>$150&ndash;$400</td><td>~$50&ndash;$100</td></tr>
        <tr><td>Post-op drops</td><td>&mdash;</td><td>$50&ndash;$300</td><td>$50&ndash;$300</td><td>Part D</td></tr>
    </tbody>
</table>

{_embed(mode="cost", cpt="66984", title="Look Up Cataract Surgery Cost", subtitle="See Medicare rates for CPT 66984 in your area.")}

<h2 id="lens-options">2. Lens options and costs</h2>

<p>The intraocular lens (IOL) is the most important decision you&rsquo;ll make. Here&rsquo;s what each type costs:</p>

<table>
    <thead>
        <tr><th>Lens Type</th><th>What It Does</th><th>Extra Cost (per eye)</th><th>Insurance Covers?</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Standard monofocal</strong></td><td>Clear vision at one distance (usually far)</td><td>$0 (included)</td><td>Yes</td></tr>
        <tr><td><strong>Toric</strong></td><td>Corrects astigmatism + one distance</td><td>$1,500&ndash;$3,000</td><td>No</td></tr>
        <tr><td><strong>Multifocal</strong></td><td>Near + far vision (reduces need for glasses)</td><td>$2,000&ndash;$4,000</td><td>No</td></tr>
        <tr><td><strong>Extended depth of focus (EDOF)</strong></td><td>Range of vision from intermediate to far</td><td>$2,500&ndash;$3,500</td><td>No</td></tr>
        <tr><td><strong>Light-adjustable lens (LAL)</strong></td><td>Adjustable after surgery with UV light</td><td>$3,000&ndash;$4,500</td><td>No</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Premium lenses are never covered by insurance or Medicare.</strong> The upgrade cost ($1,500&ndash;$4,500 per eye) is always out of pocket. Many patients do well with standard monofocal lenses and reading glasses. Ask your surgeon whether a premium lens offers meaningful benefit for your specific situation.
</div>

<h2 id="medicare-coverage">3. Medicare coverage</h2>

<p>Medicare Part B covers cataract surgery when cataracts cause significant vision impairment. Here&rsquo;s what you owe:</p>

<table>
    <thead>
        <tr><th>Setting</th><th>Medicare Pays</th><th>You Pay (20% coinsurance)</th></tr>
    </thead>
    <tbody>
        <tr><td>ASC</td><td>~$840</td><td>~$210</td></tr>
        <tr><td>Hospital outpatient (HOPD)</td><td>~$1,680</td><td>~$420</td></tr>
    </tbody>
</table>

<p>Plus the surgeon&rsquo;s fee: Medicare pays ~$650&ndash;$750, you pay 20% (~$130&ndash;$150). <strong>Total out of pocket per eye:</strong> ~$340&ndash;$360 at an ASC, or ~$550&ndash;$570 at a hospital. Add the $257 Part B annual deductible if you haven&rsquo;t met it yet.</p>

<p>If you have Medigap (supplemental), it typically covers the 20% coinsurance, bringing your cost to $0 after the deductible.</p>

<div class="case-study">
    <h3>Medicare patient saves $420 by choosing an ASC</h3>
    <p>A 72-year-old Medicare patient in Ohio needed cataract surgery on both eyes. At the hospital outpatient department, her total out-of-pocket would have been ~$1,140 (2 eyes &times; $570). By having surgery at an ASC across the street, her cost was ~$720 (2 eyes &times; $360). <strong>Savings: $420</strong> for the exact same surgeon and procedure. Her Medigap plan covered the rest.</p>
</div>

<h2 id="hospital-vs-asc">4. Hospital vs. surgery center</h2>

<table>
    <thead>
        <tr><th>Factor</th><th>Hospital (HOPD)</th><th>Surgery Center (ASC)</th></tr>
    </thead>
    <tbody>
        <tr><td>Total charge</td><td>$3,500&ndash;$7,000</td><td>$2,000&ndash;$3,500</td></tr>
        <tr><td>Medicare facility rate</td><td>~$2,100</td><td>~$1,050</td></tr>
        <tr><td>Your 20% coinsurance</td><td>~$420</td><td>~$210</td></tr>
        <tr><td>Procedure time</td><td>15&ndash;30 min</td><td>15&ndash;30 min</td></tr>
        <tr><td>Wait time</td><td>Often longer (shared OR schedule)</td><td>Typically shorter</td></tr>
        <tr><td>Quality/safety</td><td>Comparable</td><td>Comparable</td></tr>
    </tbody>
</table>

<p>Over 80% of cataract surgeries are now performed at ASCs. Find one near you: <a href="/surgery-centers/">BillKarma Surgery Center Directory</a>. For more on ASC savings, see our <a href="/guides/surgery-center-vs-hospital-cost">surgery center vs. hospital guide</a>.</p>

<h2 id="insurance">5. Insurance coverage</h2>

<p>Most private insurance plans cover cataract surgery when cataracts impair daily activities. Typical coverage:</p>

<ul>
    <li><strong>PPO/HMO:</strong> Covered after deductible, with 10&ndash;30% coinsurance. Out-of-pocket typically $500&ndash;$2,000 per eye.</li>
    <li><strong>Medicare:</strong> Part B covers surgery + standard lens. You pay 20% coinsurance.</li>
    <li><strong>Medicare Advantage:</strong> Coverage varies by plan. Some have flat copays ($100&ndash;$500 per eye).</li>
    <li><strong>Medicaid:</strong> Covered with minimal or no copay.</li>
    <li><strong>Not covered:</strong> Premium IOL upgrades, laser-assisted cataract surgery (femtosecond laser adds $1,000&ndash;$2,000), refractive lens exchange for purely refractive purposes.</li>
</ul>

<h2 id="both-eyes">6. Timing: both eyes strategy</h2>

<p>If you need surgery on both eyes, timing matters for your wallet:</p>

<ul>
    <li><strong>Same calendar year:</strong> You meet your deductible once and may hit your out-of-pocket maximum, making the second eye cheaper or free.</li>
    <li><strong>Different calendar years:</strong> You pay two deductibles. Only consider this if your cataracts are at very different stages.</li>
    <li><strong>Typical spacing:</strong> 1&ndash;4 weeks between eyes. This is standard practice for safety.</li>
</ul>

<div class="key-takeaway">
    <strong>Schedule both eyes in the same year if possible.</strong> With a $3,000 deductible, doing eye #2 after you&rsquo;ve met the deductible means you only pay coinsurance (20%) on the second eye instead of deductible + coinsurance.
</div>

<h2 id="lower-cost">7. 5 ways to lower your cataract surgery cost</h2>

<h3>a) Choose an ASC over a hospital</h3>
<p>Saves 45&ndash;55% on the facility fee. Same surgeon, same equipment, same 20-minute procedure.</p>

<h3>b) Stick with a standard lens unless you have a strong reason</h3>
<p>Premium IOLs add $1,500&ndash;$4,500 per eye out of pocket. Many patients are happy with a monofocal lens and reading glasses. Ask your surgeon for an honest assessment of the benefit for your eyes.</p>

<h3>c) Skip laser-assisted surgery unless recommended</h3>
<p>Femtosecond laser adds $1,000&ndash;$2,000 per eye and is not covered by insurance. Studies show comparable outcomes to traditional phacoemulsification for most patients.</p>

<h3>d) Do both eyes in the same calendar year</h3>
<p>Meet your deductible once instead of twice. If you&rsquo;re near your out-of-pocket max, the second eye may be nearly free.</p>

<h3>e) Audit your bill</h3>
<p>Check for duplicate facility charges, bilateral coding errors, and inflated supply costs. <a href="/scan">Upload to BillKarma</a> for an instant review.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does cataract surgery cost per eye?</h3>
        <p>$3,500&ndash;$7,000 at a hospital, $2,000&ndash;$3,500 at an ASC with a standard lens. Premium lenses add $1,500&ndash;$4,000 per eye out of pocket.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover cataract surgery?</h3>
        <p>Yes. Medicare Part B covers standard cataract surgery including a monofocal IOL. You pay 20% coinsurance (~$210 at an ASC, ~$420 at a hospital) plus the Part B deductible. Premium lens upgrades are not covered.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between standard and premium cataract lenses?</h3>
        <p>Standard monofocal lenses (included in coverage) correct one distance. Premium lenses (toric $1,500&ndash;$3,000, multifocal $2,000&ndash;$4,000) correct astigmatism or multiple distances. Premium lenses are never covered by insurance.</p>
    </div>

    <div class="faq-item">
        <h3>Is cataract surgery cheaper at a surgery center?</h3>
        <p>Yes, 45&ndash;55% cheaper. Medicare ASC rate is ~$1,050 vs. ~$2,100 at a hospital. Your coinsurance is proportionally lower too. Over 80% of cataract surgeries are now done at ASCs.</p>
    </div>

    <div class="faq-item">
        <h3>Should I have both eyes done at the same time?</h3>
        <p>Most surgeons do one eye at a time, 1&ndash;4 weeks apart. Do both in the same calendar year to meet your deductible only once.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/ambulatory-surgical-center-asc" target="_blank" rel="noopener noreferrer">CMS: ASC Payment Rates for Cataract Surgery (2026)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient" target="_blank" rel="noopener noreferrer">CMS: Hospital Outpatient PPS Rates (2026)</a></li>
    <li><a href="https://www.aao.org/eye-health/diseases/cataracts-treatment" target="_blank" rel="noopener noreferrer">American Academy of Ophthalmology: Cataract Treatment Overview</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener noreferrer">CMS: Medicare Physician Fee Schedule (CPT 66984)</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/medicare-coverage-of-eye-exams-and-eye-care/" target="_blank" rel="noopener noreferrer">KFF: Medicare Coverage of Eye Care</a></li>
</ul>
""",
})
