"""Guide: How Drug Formulary Tiers Work."""

from guides import register, _embed

register("how-drug-formulary-tiers-work", {
    "title": "How Drug Formulary Tiers Work & How to Pay Less (2026)",
    "meta_description": "Most insurance plans use a 5-tier drug formulary. Learn what each tier costs, how to request a tier exception, what step therapy means, and why 41% of specialty drug patients overpay.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance & Coverage",
    "faqs": [
        {
            "q": "What is a drug formulary tier?",
            "a": "A formulary tier is a category your insurance plan assigns to each covered drug, determining your cost-sharing. Tier 1 drugs (preferred generics) have the lowest copays ($5&ndash;$15). Tier 5 drugs (specialty) have the highest cost-sharing, often 25&ndash;33% coinsurance. Your plan places each drug in a tier based on its cost to the insurer and whether it has agreed pricing with the manufacturer.",
        },
        {
            "q": "How do I find out what tier my drug is on?",
            "a": "Use your insurance plan&rsquo;s online formulary lookup tool (usually at the member portal on your insurer&rsquo;s website) and enter your drug name. For Medicare Part D, use the Medicare Plan Finder at medicare.gov and enter your specific drugs to compare plans by tier placement and total out-of-pocket cost. Your insurer must provide an up-to-date formulary.",
        },
        {
            "q": "Can I request that my drug be covered at a lower tier?",
            "a": "Yes, through a formulary exception. You or your doctor submits a request showing that the lower-tier alternative is clinically inappropriate for your condition&mdash;for example, you experienced adverse effects, it is contraindicated, or your doctor has evidence that the preferred drug is ineffective for you specifically. If approved, the plan must cover your drug at the lower-tier cost-sharing level.",
        },
        {
            "q": "What is step therapy?",
            "a": "Step therapy (also called &ldquo;fail first&rdquo;) requires you to try a lower-cost, lower-tier drug before your insurer will approve coverage of a higher-tier drug. For example, your plan may require you to try two generic antidepressants before covering a brand-name antidepressant at a lower tier. Step therapy delays treatment and can be bypassed with a documented exception if the lower-tier drug is contraindicated or has already failed.",
        },
        {
            "q": "Does Medicare Part D have formulary tiers?",
            "a": "Yes. Medicare Part D plans use a similar 5-tier structure. However, for six &ldquo;protected drug classes&rdquo; (immunosuppressants, antidepressants, antipsychotics, anticonvulsants, antiretrovirals, and antineoplastics), Medicare requires Part D plans to cover all or substantially all drugs in the class regardless of tier. This prevents insurers from excluding critical medications in these categories.",
        },
    ],
    "body": f"""
<p class="lead">Your insurance plan&rsquo;s formulary is a list of covered drugs with each drug assigned to a &ldquo;tier&rdquo; that determines how much you pay. BillKarma data shows that <strong>41% of patients on specialty drugs pay more than they need to</strong> because they don&rsquo;t know how to request exceptions, use manufacturer assistance, or compare tier placement across plans. Here is exactly how the tier system works and how to use it to your advantage.</p>

<div class="answer-box" style="background:#e8f5e9;border-left:4px solid #2e7d32;padding:1rem 1.25rem;margin:1.5rem 0;border-radius:4px;">
    <strong>The key move most patients miss:</strong> Before filling a prescription, look up your drug&rsquo;s tier in your plan&rsquo;s formulary. If it is Tier 3 or higher, ask your doctor whether a lower-tier equivalent exists. If there is no adequate lower-tier option, ask your doctor to submit a formulary exception or tier exception request. This single step can save hundreds of dollars per month.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#five-tiers">The 5-tier formulary system explained</a></li>
        <li><a href="#how-to-look-up">How to look up your drug&rsquo;s tier</a></li>
        <li><a href="#tier-exceptions">How to request a formulary or tier exception</a></li>
        <li><a href="#step-therapy">Step therapy: what it is and how to bypass it</a></li>
        <li><a href="#medicare-part-d">Medicare Part D formulary rules</a></li>
        <li><a href="#manufacturer-assistance">Manufacturer copay cards and accumulator programs</a></li>
        <li><a href="#goodrx-vs-insurance">GoodRx vs. insurance: when to skip your coverage</a></li>
        <li><a href="#medicare-extra-help">Medicare Extra Help for low-income beneficiaries</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="five-tiers">1. The 5-tier formulary system explained</h2>

<p>Most commercial insurance plans use a five-tier formulary structure. Each tier has a different copay or coinsurance level, and the gap between tiers can be enormous&mdash;especially at the specialty tier:</p>

<table>
    <thead>
        <tr><th>Tier</th><th>Drug Type</th><th>Typical Cost-Sharing</th><th>Examples</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Tier 1</strong></td><td>Preferred generic</td><td>$5&ndash;$15 copay</td><td>Metformin, lisinopril, atorvastatin, amoxicillin</td></tr>
        <tr><td><strong>Tier 2</strong></td><td>Non-preferred generic</td><td>$15&ndash;$40 copay</td><td>Less-common generics, older brand names now generic</td></tr>
        <tr><td><strong>Tier 3</strong></td><td>Preferred brand</td><td>$40&ndash;$80 copay</td><td>Brand drugs with negotiated pricing, preferred biologics</td></tr>
        <tr><td><strong>Tier 4</strong></td><td>Non-preferred brand</td><td>$80&ndash;$150+ copay</td><td>Brand drugs without negotiated pricing</td></tr>
        <tr><td><strong>Tier 5</strong></td><td>Specialty</td><td>25&ndash;33% coinsurance, $500&ndash;$1,000+/month</td><td>Biologics, oncology drugs, MS medications, gene therapies</td></tr>
    </tbody>
</table>

<p><strong>How tiers are set:</strong> Your insurer (or pharmacy benefit manager, PBM) negotiates rebates with drug manufacturers. Drugs that generate larger rebates are often placed in lower, preferred tiers. This means tier placement is not always based on clinical equivalence&mdash;a drug can be in a lower tier because it is more profitable for the insurer, not because it is more effective for you.</p>

<p><strong>Formularies change annually.</strong> Your plan can move drugs between tiers at the start of each plan year. If a drug you take moves from Tier 2 to Tier 4, your costs can increase by $100+ per month with no clinical change in your treatment. Always review your plan&rsquo;s updated formulary during open enrollment.</p>

<h2 id="how-to-look-up">2. How to look up your drug&rsquo;s tier</h2>

<p>You have two main tools:</p>

<ol>
    <li><strong>Your insurer&rsquo;s online formulary tool.</strong> Log into your health insurance member portal and navigate to the drug/formulary section. Enter your drug name (generic or brand) and your plan will show you the tier, the cost-sharing at that tier, any quantity limits, prior authorization requirements, and step therapy requirements.</li>
    <li><strong>Medicare Plan Finder (medicare.gov).</strong> If you have Medicare Part D, go to medicare.gov/plan-compare and enter your specific medications. The tool will show you every Part D plan available in your area, what tier each plan places your drug on, and your estimated annual cost under each plan. This is the single most powerful tool for Medicare beneficiaries to minimize drug costs.</li>
</ol>

<p>When checking your formulary, look for these flags next to your drug:</p>
<ul>
    <li><strong>PA</strong> &mdash; Prior Authorization required before the insurer will cover the drug</li>
    <li><strong>ST</strong> &mdash; Step Therapy required (must try a lower-tier drug first)</li>
    <li><strong>QL</strong> &mdash; Quantity Limit (plan limits how much you can fill per month)</li>
</ul>

{_embed(mode="scan", title="Review your prescription billing", subtitle="Upload an EOB or pharmacy receipt and BillKarma will check for formulary billing errors.")}

<h2 id="tier-exceptions">3. How to request a formulary or tier exception</h2>

<p>If your drug is on a high tier or not covered at all, you or your doctor can request a <strong>formulary exception</strong> (to add a non-covered drug) or a <strong>tier exception</strong> (to cover a drug at a lower tier&rsquo;s cost-sharing level). Here is how to do it:</p>

<ol>
    <li><strong>Identify the basis for the exception.</strong> The strongest grounds are: clinical contraindication to the lower-tier alternative, documented adverse reaction or treatment failure with the preferred drug, or evidence that the specific drug is medically necessary for your condition based on peer-reviewed literature.</li>
    <li><strong>Have your doctor write a letter of medical necessity (LMN).</strong> The letter should state your diagnosis, the specific drug requested, why the preferred lower-tier alternative is not appropriate for you, and cite clinical evidence if possible. Be specific about past trial results if you have already tried the lower-tier drug.</li>
    <li><strong>Submit the exception request.</strong> Your doctor&rsquo;s office can submit directly through your insurer&rsquo;s provider portal, or you can submit with the LMN attached. Most insurers have a formulary exception form on their website.</li>
    <li><strong>Wait for the decision.</strong> Standard requests: 72 hours. Urgent (expedited) requests: 24 hours. If denied, you have the right to appeal. Get the denial in writing and request a peer-to-peer review between your doctor and the insurer&rsquo;s medical director.</li>
    <li><strong>Appeal if denied.</strong> File an internal appeal citing the clinical basis. If that fails, request an external independent review. Under federal law, you have the right to an external reviewer at no cost.</li>
</ol>

<div class="key-takeaway">
    <strong>Tier exceptions are granted more often than patients expect.</strong> When a physician submits a well-documented letter of medical necessity, approval rates are significantly higher than a bare-bones request. The time investment (one doctor visit and a letter) is typically worth it when the drug costs $200+ per month more at its current tier.
</div>

<h2 id="step-therapy">4. Step therapy: what it is and how to bypass it</h2>

<p>Step therapy (also called &ldquo;fail first&rdquo;) requires you to try a lower-cost drug before the insurer will cover your prescribed higher-tier drug. For example, your plan may require trying two generic antidepressants before covering the brand-name drug your psychiatrist prescribed.</p>

<p><strong>When step therapy can be bypassed without going through the steps:</strong></p>
<ul>
    <li>You already tried the required drug and it failed (clinical failure)</li>
    <li>The required drug is contraindicated for you (e.g., drug interaction, allergy)</li>
    <li>You have been stable on the current drug and switching would cause clinical disruption</li>
    <li>The required drug is not available (shortage or discontinuation)</li>
    <li>You are transitioning between plans and were already on the drug under your prior plan</li>
</ul>

<p>Many states have step therapy override laws that require insurers to honor step therapy exemptions in specific circumstances. Submit documentation of any prior failure or contraindication to your insurer as part of a step therapy exception request.</p>

<h2 id="medicare-part-d">5. Medicare Part D formulary rules</h2>

<p>Medicare Part D plans must comply with specific CMS formulary standards, but within those standards there is significant variation between plans. Key rules:</p>

<table>
    <thead>
        <tr><th>Rule</th><th>What It Means for You</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>6 Protected Drug Classes</strong></td><td>Plans must cover &ldquo;all or substantially all&rdquo; drugs in: immunosuppressants, antidepressants, antipsychotics, anticonvulsants, antiretrovirals, antineoplastics</td></tr>
        <tr><td><strong>2 drugs per category minimum</strong></td><td>Most non-protected categories require at least 2 drugs covered per class</td></tr>
        <tr><td><strong>Formulary changes mid-year</strong></td><td>Plans generally cannot remove drugs or increase tiers mid-year for current enrollees (exceptions for safety issues)</td></tr>
        <tr><td><strong>Coverage Gap (Donut Hole)</strong></td><td>Effectively eliminated for 2026 under the IRA; $2,000 out-of-pocket cap on Part D drug costs per year</td></tr>
        <tr><td><strong>Extra Help (LIS)</strong></td><td>Low-income subsidy reduces Part D cost-sharing to near $0 for qualifying beneficiaries</td></tr>
    </tbody>
</table>

<p>The Inflation Reduction Act (IRA) capped annual Medicare Part D out-of-pocket drug costs at <strong>$2,000 in 2025</strong>, eliminating the old donut hole coverage gap. If you take expensive specialty drugs under Medicare, your annual out-of-pocket cost is now capped regardless of tier placement.</p>

<h2 id="manufacturer-assistance">6. Manufacturer copay cards and accumulator programs</h2>

<p>Pharmaceutical manufacturers offer <strong>copay assistance cards</strong> (sometimes called copay cards or patient assistance programs) that cover or reduce your out-of-pocket cost for brand-name drugs. These can reduce your monthly cost from $200+ to $0 at the pharmacy counter. However, many insurers now use <strong>accumulator adjustment programs</strong> that block manufacturer assistance from counting toward your deductible or out-of-pocket maximum.</p>

<p><strong>How accumulators work against you:</strong> Without an accumulator, a manufacturer pays your $300 monthly Tier 3 copay and it counts toward your $4,000 out-of-pocket maximum. With an accumulator, the manufacturer pays your copay but it does NOT count toward your OOP max. When the copay card runs out (usually after 12 months), you still owe the full deductible and OOP max as if you had paid nothing all year.</p>

<p><strong>What you can do:</strong></p>
<ul>
    <li>Call your insurer before using a manufacturer copay card and ask specifically: &ldquo;Does your plan use an accumulator adjustment program?&rdquo;</li>
    <li>If your plan has an accumulator, look for manufacturer patient assistance programs (PAPs) instead, which provide the drug directly rather than through insurance and have no accumulator interaction.</li>
    <li>Several states (including California, Virginia, and others) have passed laws restricting accumulator programs. Check your state&rsquo;s rules.</li>
    <li>For Medicare patients: manufacturer copay cards generally cannot be used for Part D drugs (anti-kickback statute). Use Medicare&rsquo;s Extra Help program or manufacturer PAPs instead.</li>
</ul>

<h2 id="goodrx-vs-insurance">7. GoodRx vs. insurance: when to skip your coverage</h2>

<p>For low-tier generic drugs, GoodRx and similar discount programs sometimes offer prices <em>lower</em> than your insurance copay. This sounds counterintuitive, but it happens because discount programs negotiate cash prices that can undercut even Tier 1 copays for common generics.</p>

<p><strong>When to use GoodRx over insurance:</strong></p>
<ul>
    <li>Your drug is a common generic (metformin, lisinopril, simvastatin, etc.) and GoodRx shows a price below your Tier 1 copay</li>
    <li>You have not yet met your deductible and would pay full price anyway</li>
    <li>You are uninsured</li>
</ul>

<p><strong>When to use insurance over GoodRx:</strong></p>
<ul>
    <li>Your drug is Tier 2 or higher and insurance brings your cost lower than GoodRx</li>
    <li>You want the cost to count toward your deductible and out-of-pocket maximum (GoodRx purchases do NOT count toward insurance accumulators)</li>
    <li>You are close to your out-of-pocket maximum and every dollar of drug spend counts</li>
</ul>

<div class="case-study">
    <h3>Case study: $4,800/year saved by switching tiers at open enrollment</h3>
    <p><strong>Situation:</strong> James takes a Tier 5 specialty biologic for rheumatoid arthritis, costing him $650/month in coinsurance. His insurer uses an accumulator program, so the manufacturer&rsquo;s copay card had no effect on his OOP max.</p>
    <p><strong>What he did:</strong> During open enrollment, he used the Medicare Plan Finder equivalent (his employer plan&rsquo;s formulary comparison tool) and found that a competing employer plan placed the same drug on Tier 4 with a $150/month copay cap. He switched plans during open enrollment.</p>
    <p><strong>Result:</strong> $650 &rarr; $150 per month. <strong>Annual savings: $6,000.</strong> He also found the new plan had no accumulator program, so his manufacturer copay card now counted toward his OOP max. Total benefit: over $8,000/year.</p>
</div>

<h2 id="medicare-extra-help">8. Medicare Extra Help for low-income beneficiaries</h2>

<p>Medicare Extra Help (also called the Low Income Subsidy, or LIS) is a federal program that dramatically reduces Part D prescription drug costs for Medicare beneficiaries with limited income and assets.</p>

<p>With Extra Help in 2026, eligible beneficiaries pay <strong>no more than a few dollars per prescription</strong> for covered Part D drugs, regardless of tier. There is no coverage gap and no deductible. Qualification is based on income (generally up to 150% of the federal poverty level) and asset limits.</p>

<p>To apply, contact Social Security (1-800-772-1213) or apply online at ssa.gov. Medicaid recipients are automatically enrolled. If you or a family member on Medicare struggles with drug costs, Extra Help should be the first call you make.</p>

<div class="cta-box" style="background:#f3f4f6;border:1px solid #d1d5db;padding:1.25rem 1.5rem;margin:2rem 0;border-radius:6px;">
    <strong>Getting a bill for a prescription that seems too high?</strong> <a href="/fight-debt">Upload it to BillKarma</a> and we&rsquo;ll check whether you were charged the right tier amount, whether an accumulator program is eating your OOP max credit, and whether a formulary exception could lower your cost.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is a drug formulary tier?</h3>
        <p>A tier is a category assigned to each covered drug that determines your cost-sharing. Tier 1 generics have the lowest copays ($5&ndash;$15). Tier 5 specialty drugs carry 25&ndash;33% coinsurance, often $500&ndash;$1,000+ per month.</p>
    </div>

    <div class="faq-item">
        <h3>How do I find out what tier my drug is on?</h3>
        <p>Log into your insurer&rsquo;s member portal and use the formulary lookup tool. For Medicare Part D, use the Medicare Plan Finder at medicare.gov. Look for PA, ST, or QL flags that indicate prior auth, step therapy, or quantity limits.</p>
    </div>

    <div class="faq-item">
        <h3>Can I request that my drug be covered at a lower tier?</h3>
        <p>Yes. Submit a formulary or tier exception request with a letter of medical necessity from your doctor explaining why the lower-tier alternative is clinically inappropriate. Standard decisions come within 72 hours.</p>
    </div>

    <div class="faq-item">
        <h3>What is step therapy?</h3>
        <p>Step therapy requires you to try a lower-cost drug before the insurer will cover a higher-tier drug. It can be bypassed if you document that the required drug failed, is contraindicated, or if you were already stable on the current drug.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare Part D have formulary tiers?</h3>
        <p>Yes. Medicare Part D uses a similar 5-tier structure but has special protections: plans must cover all or substantially all drugs in six protected classes (including antidepressants, anticonvulsants, and antiretrovirals). The IRA also capped annual Part D out-of-pocket costs at $2,000.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: Medicare Part D Formulary Requirements</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: Inflation Reduction Act &mdash; Medicare Drug Price Negotiation and Part D Out-of-Pocket Cap</a></li>
    <li><a href="#" target="_blank" rel="noopener">Kaiser Family Foundation: Prescription Drug Cost-Sharing in Marketplace Plans (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Social Security Administration: Medicare Extra Help (Low Income Subsidy)</a></li>
    <li><a href="#" target="_blank" rel="noopener">AHIP: Drug Formulary Management and Step Therapy Guidelines</a></li>
    <li><a href="#" target="_blank" rel="noopener">National Academy for State Health Policy: Accumulator Adjustment Program State Laws (2025)</a></li>
</ul>
""",
})
