"""Guide: Medigap Medicare Supplement Insurance"""

from guides import register, _embed

register("medigap-medicare-supplement-guide", {
    "title": "Medigap Guide 2026: Plans, Costs, and When to Enroll",
    "meta_description": "Medigap (Medicare Supplement) plans cover the 20% Medicare doesn't pay. Compare Plans A, B, C, D, F, G, K, L, M, N&mdash;costs, coverage, and the best enrollment window for 2026.",
    "published": "2026-04-10",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What is the best Medigap plan in 2026?",
            "a": "Plan G is the most comprehensive Medigap plan available to new enrollees in 2026 (Plan F was eliminated for new Medicare enrollees after January 1, 2020). Plan G covers the Part B coinsurance, Part A deductible, Part A coinsurance, skilled nursing facility coinsurance, and foreign travel emergencies. You pay only the $257 annual Part B deductible. For most beneficiaries with ongoing medical needs, Plan G provides the most complete protection.",
        },
        {
            "q": "What is the difference between Medigap Plan F and Plan G?",
            "a": "Plan F covers the Part B deductible ($257 in 2026) in addition to everything Plan G covers. Plan F is no longer available to people who became Medicare-eligible after January 1, 2020. If you are already enrolled in Plan F, you can keep it. For new enrollees, Plan G is the most comprehensive option and typically costs less than Plan F premiums.",
        },
        {
            "q": "When is the best time to enroll in Medigap?",
            "a": "The best time is during your six-month Medigap Open Enrollment Period, which starts the month you turn 65 AND are enrolled in Medicare Part B. During this window, insurers cannot deny coverage or charge you more due to pre-existing conditions. Once this window closes, you may face medical underwriting in most states.",
        },
        {
            "q": "Are Medigap plans standardized?",
            "a": "Yes. The federal government standardizes Medigap benefits across 10 plan types (A, B, C, D, F, G, K, L, M, N). A Plan G from Humana covers exactly the same benefits as a Plan G from AARP/UnitedHealthcare. The only difference between insurers is the monthly premium and customer service quality. Shop on price once you pick your plan letter.",
        },
        {
            "q": "Does Medigap cover prescription drugs?",
            "a": "No. Medigap plans do not cover outpatient prescription drugs. If you want drug coverage, you need to enroll separately in a Medicare Part D plan. Medigap only covers cost-sharing for services covered by Medicare Parts A and B.",
        },
    ],
    "body": f"""<article>
<div class="answer-box"><strong>Quick Answer:</strong> Medigap (Medicare Supplement) insurance fills the gaps Original Medicare leaves&mdash;primarily the unlimited 20% Part B coinsurance and the Part A deductible. There are 10 standardized plan types. Plan G is the best choice for most new enrollees in 2026. Enroll during your six-month open enrollment window when you turn 65 to avoid medical underwriting. Monthly premiums average $100&ndash;$400.</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-medigap-covers">What Medigap Covers</a></li>
        <li><a href="#10-plans">The 10 Standardized Plan Types</a></li>
        <li><a href="#plan-g-vs-f">Plan G vs. Plan F</a></li>
        <li><a href="#when-to-enroll">When to Enroll</a></li>
        <li><a href="#guaranteed-issue">Guaranteed Issue Rights</a></li>
        <li><a href="#costs">Average Monthly Costs</a></li>
        <li><a href="#what-medigap-doesnt-cover">What Medigap Doesn't Cover</a></li>
        <li><a href="#shopping">How to Shop for Medigap</a></li>
    </ol>
</nav>

<h2 id="what-medigap-covers">What Medigap Covers</h2>

<p>Medigap plans are sold by private insurers to supplement Original Medicare (Parts A and B). They do not work with Medicare Advantage plans&mdash;you can only use Medigap if you have Original Medicare.</p>

<p>The potential cost-sharing gaps that Medigap can cover include:</p>
<ul>
    <li><strong>Medicare Part B coinsurance:</strong> The 20% you owe on all covered outpatient services, with no cap. This is the most valuable Medigap benefit for most enrollees.</li>
    <li><strong>Medicare Part A deductible:</strong> $1,676 per benefit period in 2026. With multiple hospitalizations per year, this adds up fast.</li>
    <li><strong>Medicare Part A coinsurance:</strong> $419/day for hospital days 61&ndash;90; $838/day for lifetime reserve days.</li>
    <li><strong>Skilled nursing facility coinsurance:</strong> $209.50/day for days 21&ndash;100 of a SNF stay.</li>
    <li><strong>Part B excess charges:</strong> The 15% above Medicare's approved amount that non-participating providers can charge (Plans F and G cover this).</li>
    <li><strong>Foreign travel emergencies:</strong> 80% of emergency care costs outside the U.S. after a $250 deductible (Plans C, D, F, G, M, N).</li>
    <li><strong>Part B deductible:</strong> $257 in 2026. Only Plan F (not available to new enrollees) covers this.</li>
</ul>

<h2 id="10-plans">The 10 Standardized Plan Types</h2>

<p>Federal law standardizes Medigap benefits into 10 plan letters. Every insurer selling a given plan letter must offer identical benefits. Not all plan letters are available in all states (Massachusetts, Minnesota, and Wisconsin have their own Medigap systems).</p>

<table>
    <thead>
        <tr><th>Benefit</th><th>A</th><th>B</th><th>C*</th><th>D</th><th>F*</th><th>G</th><th>K</th><th>L</th><th>M</th><th>N</th></tr>
    </thead>
    <tbody>
        <tr><td>Part A coinsurance</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
        <tr><td>Part B coinsurance</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>50%</td><td>75%</td><td>✓</td><td>✓†</td></tr>
        <tr><td>Blood (first 3 pints)</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>50%</td><td>75%</td><td>✓</td><td>✓</td></tr>
        <tr><td>Part A deductible</td><td>—</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>50%</td><td>75%</td><td>50%</td><td>✓</td></tr>
        <tr><td>Part B deductible</td><td>—</td><td>—</td><td>✓</td><td>—</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
        <tr><td>Part B excess charges</td><td>—</td><td>—</td><td>—</td><td>—</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
        <tr><td>SNF coinsurance</td><td>—</td><td>—</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>50%</td><td>75%</td><td>✓</td><td>✓</td></tr>
        <tr><td>Foreign travel emergency</td><td>—</td><td>—</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>✓</td><td>✓</td></tr>
    </tbody>
</table>
<p><small>* Plans C and F not available to new Medicare enrollees (eligible on or after Jan 1, 2020). † Plan N has copays: up to $20 for office visits and up to $50 for ER visits.</small></p>

<h2 id="plan-g-vs-f">Plan G vs. Plan F: The Key Comparison</h2>

<p>For most people comparing Medigap plans, the decision comes down to Plan G vs. Plan F (for those who can still get F) or Plan G vs. Plan N.</p>

<h3>Plan F vs. Plan G</h3>
<p>The only difference is that Plan F covers the $257 annual Part B deductible and Plan G does not. This means Plan F covers $257/year more than Plan G. However, Plan F premiums are typically $30&ndash;$60/month higher than Plan G. At $30/month higher, Plan F costs an extra $360/year to cover a $257 benefit&mdash;making Plan G the better financial deal for most enrollees.</p>

<p>Plan F is also only available to people who became Medicare-eligible before January 1, 2020. If you first became eligible on or after that date, Plan F is not an option.</p>

<h3>Plan G vs. Plan N</h3>
<p>Plan N is the lower-cost alternative to Plan G. The tradeoff:</p>
<ul>
    <li>Plan N does not cover Part B excess charges (the extra 15% non-participating providers can charge)</li>
    <li>Plan N has a copay of up to $20 for office visits and up to $50 for ER visits not resulting in admission</li>
    <li>Plan N premiums are typically $30&ndash;$80/month less than Plan G</li>
</ul>
<p>Plan N works well if you primarily see Medicare-participating providers (who cannot charge excess charges) and don't use the ER frequently. If you see non-participating specialists, Plan G's excess charge coverage can be valuable.</p>

<h2 id="when-to-enroll">When to Enroll</h2>

<p>Timing your Medigap enrollment correctly is one of the most important Medicare decisions you'll make.</p>

<p><strong>Your six-month open enrollment window</strong> starts the first day of the month in which you are both (1) age 65 or older AND (2) enrolled in Medicare Part B. During this window, any insurer selling Medigap in your state must:</p>
<ul>
    <li>Sell you any plan they offer</li>
    <li>Cannot deny you for any pre-existing condition</li>
    <li>Cannot charge you more because of your health</li>
</ul>

<p>This is the only time in most states when you have this unconditional right. Once the six-month window closes, insurers can reject your application or charge you substantially higher premiums based on your health history.</p>

<div class="key-takeaway">
    <strong>Don't delay your Part B enrollment to save on premiums.</strong> If you delay Part B (e.g., because you have employer coverage), your six-month Medigap open enrollment window starts when you eventually enroll in Part B&mdash;not at age 65. This is actually fine; just enroll in Medigap promptly once you activate Part B.
</div>

<h2 id="guaranteed-issue">Guaranteed Issue Rights</h2>

<p>Outside your open enrollment window, you may still have <strong>guaranteed issue rights</strong> in specific circumstances. These allow you to buy certain Medigap plans without medical underwriting:</p>

<ul>
    <li>You lose employer or union coverage and you have Medicare</li>
    <li>Your Medicare Advantage plan leaves your area or stops accepting Medicare</li>
    <li>You move out of your Medicare Advantage plan's service area</li>
    <li>Your Medigap insurer goes bankrupt or violates your contract</li>
    <li>You enrolled in Medicare Advantage for the first time and within your first year you decide to return to Original Medicare</li>
</ul>

<p>Guaranteed issue rights typically apply to Plans A, B, C, F, K, and L (specific available plans vary by situation). Always check with your state insurance commissioner for the exact plans available under your guaranteed issue right.</p>

{_embed("cost", title="Estimate Medigap Savings", subtitle="See how much Medigap could save on your expected Medicare costs.")}

<h2 id="costs">Average Monthly Costs</h2>

<p>Medigap premiums vary significantly by plan type, your age, your location, the insurer's pricing method, and whether you smoke. General ranges for 2026:</p>

<table>
    <thead>
        <tr><th>Plan</th><th>Typical Monthly Premium (Age 65)</th><th>Best For</th></tr>
    </thead>
    <tbody>
        <tr><td>Plan A</td><td>$80&ndash;$150</td><td>Lowest cost; minimal gap coverage</td></tr>
        <tr><td>Plan B</td><td>$100&ndash;$180</td><td>Adds Part A deductible coverage</td></tr>
        <tr><td>Plan G</td><td>$130&ndash;$300</td><td>Most popular; comprehensive coverage</td></tr>
        <tr><td>Plan G (High Deductible)</td><td>$40&ndash;$80</td><td>Lower premium with $2,800 deductible</td></tr>
        <tr><td>Plan K</td><td>$60&ndash;$120</td><td>Lower premium; 50% coverage with $7,220 OOP cap</td></tr>
        <tr><td>Plan N</td><td>$100&ndash;$220</td><td>Lower premium; office/ER copays</td></tr>
    </tbody>
</table>

<p>Insurers use three pricing methods that significantly affect long-term costs:</p>
<ul>
    <li><strong>Community-rated:</strong> Same premium for everyone in the area, regardless of age. Premiums don't increase just because you get older. Generally best long-term value.</li>
    <li><strong>Issue-age-rated:</strong> Premiums are based on your age when you buy the policy and don't increase as you age. Good long-term value if you enroll young.</li>
    <li><strong>Attained-age-rated:</strong> Premiums start low but increase as you age. The most common pricing method. Can become very expensive in your 80s.</li>
</ul>

<h2 id="what-medigap-doesnt-cover">What Medigap Doesn't Cover</h2>

<p>Even the most comprehensive Medigap plan doesn't cover everything:</p>
<ul>
    <li>Prescription drugs (need Part D)</li>
    <li>Dental, vision, and hearing care</li>
    <li>Long-term care</li>
    <li>Private-duty nursing</li>
    <li>Medicare Advantage plan costs</li>
</ul>

<h2 id="shopping">How to Shop for Medigap</h2>

<ol>
    <li><strong>Decide on a plan letter first.</strong> For most people: Plan G if you want comprehensive coverage, Plan N if you want lower premiums and see mostly participating providers.</li>
    <li><strong>Compare prices from multiple insurers.</strong> Because benefits are standardized, price is your only differentiator. Use Medicare.gov's Medigap plan finder or a licensed Medicare broker.</li>
    <li><strong>Ask about the pricing method.</strong> Community-rated and issue-age-rated plans tend to be cheaper long-term than attained-age-rated plans.</li>
    <li><strong>Check insurer financial stability.</strong> Look up the insurer's AM Best rating. You want an insurer with an A or better rating.</li>
    <li><strong>Enroll before your window closes.</strong> Don't wait until you have a health event. By then it may be too late to get coverage without medical underwriting.</li>
</ol>

<ul class="sources-list">
    <li><a href="https://www.medicare.gov/supplements-other-insurance/whats-medicare-supplement-insurance-medigap" target="_blank" rel="noopener">Medicare.gov &mdash; What Is Medigap?</a></li>
    <li><a href="https://www.cms.gov/medicare/health-plans/medigap" target="_blank" rel="noopener">CMS &mdash; Medigap Policies</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/medigap-enrollment-and-consumer-protections-vary-across-states/" target="_blank" rel="noopener">KFF &mdash; Medigap Enrollment and Consumer Protections</a></li>
    <li><a href="https://www.naic.org/documents/topics_plain_language_medigap.pdf" target="_blank" rel="noopener">NAIC &mdash; Medigap Shopper's Guide</a></li>
</ul>
</article>""",
})
