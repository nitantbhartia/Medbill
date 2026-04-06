"""Guide: Air Ambulance Bills."""

from guides import register, _embed

register("air-ambulance-bills", {
    "title": "Air Ambulance Bills: $50,000+ Costs and How to Fight Back",
    "meta_description": "Air ambulance bills average $36,400 and can exceed $100,000. Learn how the No Surprises Act protects you, plus 5 strategies to reduce or eliminate air.",
    "published": "2026-03-01",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does an air ambulance ride cost?",
            "a": "The average air ambulance flight costs $36,400, but bills regularly range from $12,000 to over $100,000 depending on distance, medical crew, and the provider. The base rate alone is typically $15,000&ndash;$30,000 before mileage, medical crew, and supply charges are added. Medicare pays approximately $6,500 for a helicopter transport, meaning the gap between what providers charge and what insurers pay is enormous.",
        },
        {
            "q": "Does insurance cover air ambulance bills?",
            "a": "Most insurance plans cover air ambulance transport when it is medically necessary, but many air ambulance companies are out-of-network. Before the No Surprises Act, this meant patients could be balance billed tens of thousands of dollars. Since January 1, 2022, the No Surprises Act prohibits air ambulance providers from balance billing insured patients beyond their in-network cost-sharing amount, regardless of network status.",
        },
        {
            "q": "Does the No Surprises Act cover air ambulance?",
            "a": "Yes. The No Surprises Act fully protects insured patients from air ambulance balance billing as of January 1, 2022. If you receive an air ambulance bill for more than your in-network copay, coinsurance, or deductible, the provider is violating federal law. File a complaint with CMS and your state insurance commissioner. Note that the NSA does not apply to ground ambulance, which has a separate regulatory process.",
        },
        {
            "q": "Are air ambulance membership programs worth it?",
            "a": "Air ambulance memberships cost $50&ndash;$100 per year and cover the balance after insurance pays. They are worth considering if you live in a rural area more than 30 minutes from a trauma center, participate in backcountry recreation, or have a medical condition that could require emergency air transport. However, since the No Surprises Act now prohibits balance billing for insured patients, memberships are most valuable for uninsured individuals or for coverage of non-emergency transfers.",
        },
        {
            "q": "Can I negotiate an air ambulance bill?",
            "a": "Yes. Uninsured patients or those with bills predating the No Surprises Act can negotiate directly with the air ambulance company. Request the Medicare rate as your benchmark&mdash;Medicare pays approximately $6,500 for a helicopter transport versus the $30,000&ndash;$50,000 typically billed. Many companies will accept 20&ndash;40% of the billed amount, especially if you apply for their charity care or financial hardship program.",
        },
        {
            "q": "What should I do if I get an air ambulance bill I cannot afford?",
            "a": "First, verify whether the No Surprises Act applies to your flight (insured, after January 2022). If it does, you should only owe your in-network cost-sharing. If you are uninsured, request an itemized bill, compare charges against Medicare rates using a cost calculator, apply for the provider&rsquo;s financial assistance or charity care program, and negotiate a reduced lump-sum payment. Many air ambulance companies will reduce bills by 50&ndash;80% for patients who demonstrate financial hardship.",
        },
    ],
    "body": f"""
<p class="lead">A helicopter lands, paramedics stabilize you, and 45 minutes later you&rsquo;re at a trauma center. Then the bill arrives: <strong>$40,000&ndash;$100,000</strong> for a single flight. Air ambulance transport is one of the most expensive services in American healthcare, averaging <strong>$36,400</strong> per flight &mdash; and before federal protections took effect in 2022, patients routinely received balance bills of $20,000 or more after insurance. Here&rsquo;s what air ambulance flights actually cost, why the prices are so extreme, and how to fight back whether you&rsquo;re insured or not.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-much-cost">How much air ambulance flights actually cost</a></li>
        <li><a href="#why-so-expensive">Why air ambulance bills are so high</a></li>
        <li><a href="#no-surprises-act">How the No Surprises Act changed air ambulance billing</a></li>
        <li><a href="#what-to-do">What to do if you get an air ambulance bill</a></li>
        <li><a href="#membership-programs">Air ambulance membership programs: are they worth it?</a></li>
        <li><a href="#how-to-dispute">How to dispute an air ambulance bill</a></li>
        <li><a href="#insurance-coverage">When your insurance must pay</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="how-much-cost">1. How much air ambulance flights actually cost</h2>

<p>Air ambulance bills are built from multiple components: a base rate, per-mile charges, medical crew fees, and supply charges. Each line item is billed separately, and the total adds up fast.</p>

<table>
    <thead>
        <tr><th>Component</th><th>Typical Charge</th><th>Medicare Rate</th></tr>
    </thead>
    <tbody>
        <tr><td>Base rate (rotary-wing/helicopter)</td><td>$15,000&ndash;$30,000</td><td>~$6,515</td></tr>
        <tr><td>Base rate (fixed-wing/airplane)</td><td>$20,000&ndash;$40,000</td><td>~$3,753</td></tr>
        <tr><td>Mileage (per loaded air mile)</td><td>$100&ndash;$400</td><td>~$16&ndash;$30</td></tr>
        <tr><td>Medical crew (flight nurse, paramedic)</td><td>$2,000&ndash;$5,000</td><td>Included in base</td></tr>
        <tr><td>Supplies and medications</td><td>$500&ndash;$3,000</td><td>Included in base</td></tr>
    </tbody>
</table>

<p>A 2022 GAO report found the median air ambulance charge for privately insured patients was <strong>$36,400</strong> for a helicopter transport. Bills exceeding $100,000 are not uncommon for long-distance fixed-wing transfers or flights requiring specialty medical teams. By comparison, a ground ambulance ride averages $1,200&ndash;$2,500.</p>

<table>
    <thead>
        <tr><th>Transport Type</th><th>Average Billed Amount</th><th>Average Medicare Payment</th><th>Typical Patient Balance (Pre-NSA)</th></tr>
    </thead>
    <tbody>
        <tr><td>Ground ambulance (BLS)</td><td>$1,200&ndash;$2,500</td><td>~$450</td><td>$750&ndash;$2,050</td></tr>
        <tr><td>Ground ambulance (ALS)</td><td>$1,500&ndash;$3,000</td><td>~$550</td><td>$950&ndash;$2,450</td></tr>
        <tr><td>Air ambulance (helicopter)</td><td>$30,000&ndash;$50,000</td><td>~$6,515</td><td>$20,000&ndash;$43,500</td></tr>
        <tr><td>Air ambulance (fixed-wing)</td><td>$25,000&ndash;$75,000</td><td>~$3,753</td><td>$21,000&ndash;$71,000</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The markup is staggering.</strong> Air ambulance companies charge 4&ndash;8x what Medicare pays for the same service. A helicopter flight that Medicare reimburses at $6,515 is routinely billed at $30,000&ndash;$50,000. Use our <a href="/calculator">free calculator</a> to compare what you were charged against the Medicare rate for your transport.
</div>

<h2 id="why-so-expensive">2. Why air ambulance bills are so high</h2>

<p>Air ambulance pricing is driven by a combination of market structure, regulatory gaps, and the economics of maintaining flight-ready medical helicopters.</p>

<h3>Limited competition and consolidation</h3>

<p>Three companies &mdash; Air Methods, Global Medical Response (which includes Air Evac Lifeteam and REACH), and PHI Air Medical &mdash; control roughly 75% of the U.S. air ambulance market. In most regions, only one provider serves a given area. When you call 911, you have no choice in which helicopter responds, and no ability to compare prices. This lack of competition allows providers to set prices without market pressure.</p>

<h3>No historical price regulation</h3>

<p>Unlike ground ambulance services, which are often subject to state or municipal rate-setting, air ambulance companies have historically been shielded from state price regulation by the Airline Deregulation Act of 1978. Federal courts have ruled that states cannot cap air ambulance rates because air ambulances are classified as &ldquo;air carriers.&rdquo; This regulatory gap meant providers could charge whatever the market would bear &mdash; and in an emergency, the market will bear almost anything.</p>

<h3>High operating costs (but not as high as the bills)</h3>

<p>Operating a medical helicopter is genuinely expensive. Fuel, aircraft maintenance, flight crew salaries, medical equipment, insurance, and 24/7 readiness at base stations cost an estimated $2&ndash;$3 million per helicopter per year. However, industry analyses show that actual operating costs per flight average $10,000&ndash;$15,000 &mdash; far below the $30,000&ndash;$50,000 typically billed. The gap between cost and price reflects market power, not operating expenses.</p>

<h3>Out-of-network billing as a business model</h3>

<p>Before the No Surprises Act, many air ambulance companies deliberately remained out-of-network with most insurers. By staying out-of-network, they could bill patients directly for the difference between their full charge and whatever the insurer paid &mdash; a practice known as balance billing. A 2019 Yale study found that <strong>77% of air ambulance transports</strong> were out-of-network, and the average balance bill was $21,698.</p>

<div class="key-takeaway">
    <strong>Why didn&rsquo;t competition bring prices down?</strong> You cannot shop for an air ambulance during an emergency. Providers know this. Combined with federal preemption blocking state price regulation and deliberate out-of-network strategies, air ambulance companies operated in a market with zero price discipline &mdash; until the No Surprises Act changed the rules in 2022.
</div>

<h2 id="no-surprises-act">3. How the No Surprises Act changed air ambulance billing</h2>

<p>The <a href="/guides/no-surprises-act-explained">No Surprises Act</a> (NSA), effective January 1, 2022, fundamentally changed air ambulance billing for insured patients. Here&rsquo;s what it does and does not cover.</p>

<h3>What the NSA protects</h3>

<ul>
    <li><strong>No balance billing.</strong> Air ambulance providers cannot bill insured patients more than their in-network cost-sharing (copay, coinsurance, or deductible) &mdash; even if the provider is out-of-network.</li>
    <li><strong>In-network cost-sharing applies.</strong> Your insurer must calculate your cost-sharing as if the air ambulance were in-network. Out-of-network charges cannot be applied to a separate, higher out-of-network deductible.</li>
    <li><strong>Independent dispute resolution (IDR).</strong> If the provider and insurer cannot agree on payment, either party can use the federal IDR process. The patient is not involved &mdash; the dispute is between the provider and the insurer.</li>
</ul>

<h3>What the NSA does NOT cover</h3>

<ul>
    <li>Uninsured patients (no insurance at all) are not covered by the NSA&rsquo;s air ambulance provisions, though they can request a Good Faith Estimate.</li>
    <li>Ground ambulance is excluded from the NSA&rsquo;s balance billing protections entirely. See our <a href="/guides/how-to-fight-an-ambulance-bill">ground ambulance guide</a> for details.</li>
    <li>Non-emergency, pre-scheduled air transfers where the patient had time to choose a provider may have different rules.</li>
    <li>Flights before January 1, 2022 are not retroactively covered.</li>
</ul>

<div class="key-takeaway">
    <strong>If you received an air ambulance bill after January 1, 2022 and you have insurance:</strong> You should only owe your in-network cost-sharing amount. If the provider is billing you more, they are violating the No Surprises Act. File a complaint with CMS at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a> and your state insurance commissioner. <a href="/scan">Upload your bill to BillKarma</a> to check whether your charges comply with NSA protections.
</div>

<h2 id="what-to-do">4. What to do if you get an air ambulance bill</h2>

<p>Follow this step-by-step action plan whether you are insured or uninsured.</p>

<p><strong>Step 1 &mdash; Request an itemized bill.</strong> Call the air ambulance company and request a complete itemized statement with HCPCS codes, loaded air miles, crew charges, and supply charges. Do not pay anything until you have reviewed the itemized bill.</p>

<p><strong>Step 2 &mdash; Verify the date of service.</strong> If your flight occurred on or after January 1, 2022 and you have insurance, the No Surprises Act applies. You should only owe your in-network cost-sharing. Skip to Step 5 if the provider is billing you more than that amount.</p>

<p><strong>Step 3 &mdash; Compare charges against Medicare rates.</strong> Use the <a href="/calculator">BillKarma calculator</a> to look up the Medicare rate for your transport type (A0436 for helicopter, A0431 for fixed-wing). Medicare pays approximately $6,515 for a helicopter base rate and $16&ndash;$30 per loaded air mile. If your bill is 5&ndash;10x the Medicare rate, you have strong grounds to negotiate.</p>

<p><strong>Step 4 &mdash; Check for billing errors.</strong> Common errors include inflated mileage (verify against the actual flight distance between pickup and hospital), charges for medical crew already included in the base rate, duplicate supply charges, and incorrect service codes.</p>

<p><strong>Step 5 &mdash; File complaints if the NSA applies.</strong> If you have insurance and the provider is balance billing you beyond your in-network cost-sharing for a post-2022 flight, file complaints with CMS, your state insurance commissioner, and the CFPB.</p>

<p><strong>Step 6 &mdash; Negotiate or apply for financial assistance.</strong> If you are uninsured or the flight predates the NSA, negotiate directly using the Medicare rate as your benchmark. Apply for the provider&rsquo;s charity care or financial hardship program. See Section 6 for detailed dispute strategies.</p>

{_embed(mode="cost", title="Look up your air ambulance code", subtitle="Enter the HCPCS code from your bill to see what Medicare pays.")}

<div class="key-takeaway">
    <strong>Do not ignore an air ambulance bill.</strong> Air ambulance companies are aggressive debt collectors. If you need time, call immediately to request a hold on collections while you review the bill and explore your options. Most providers will grant 30&ndash;60 days. <a href="/scan">Upload your bill to BillKarma</a> to identify errors and get a Medicare comparison for every line item.
</div>

<h2 id="membership-programs">5. Air ambulance membership programs: are they worth it?</h2>

<p>Several air ambulance companies offer membership programs that cover balance billing &mdash; the amount left after insurance pays. Here&rsquo;s how the major programs compare.</p>

<table>
    <thead>
        <tr><th>Program</th><th>Annual Cost</th><th>Coverage</th><th>Network</th></tr>
    </thead>
    <tbody>
        <tr><td>AMCN (Air Medical Group Holdings)</td><td>$65&ndash;$85/year</td><td>Covers balance after insurance for emergency flights</td><td>AirEvac Lifeteam, Med-Trans, REACH</td></tr>
        <tr><td>Air Methods Community Benefit Plan</td><td>$59&ndash;$89/year</td><td>Covers patient responsibility after insurance</td><td>Air Methods fleet only</td></tr>
        <tr><td>AirMedCare Network</td><td>$85/year (household)</td><td>No out-of-pocket cost for covered flights</td><td>320+ bases across 38 states</td></tr>
        <tr><td>Hospital-based programs</td><td>Varies ($50&ndash;$150/year)</td><td>Typically covers flights to affiliated hospital only</td><td>Single hospital system</td></tr>
    </tbody>
</table>

<h3>When memberships make sense</h3>

<ul>
    <li>You live in a rural area more than 30 minutes from a Level I or II trauma center.</li>
    <li>You or family members participate in backcountry activities (hiking, skiing, off-road vehicles) in remote areas.</li>
    <li>You have a chronic condition (cardiac, neurological) that could require emergency air transport.</li>
    <li>You are uninsured &mdash; memberships are one of the few protections available outside the NSA.</li>
</ul>

<h3>When memberships may not be necessary</h3>

<ul>
    <li>You have insurance and your flight occurred after January 1, 2022 &mdash; the NSA already prohibits balance billing.</li>
    <li>You live in an urban area with multiple trauma centers within ground ambulance range.</li>
    <li>Your health plan already includes air ambulance as an in-network benefit (check your Summary of Benefits).</li>
</ul>

<div class="key-takeaway">
    <strong>Since the No Surprises Act:</strong> Memberships are most valuable for uninsured individuals and for non-emergency inter-facility transfers that may not be covered by the NSA. If you have insurance, verify that the NSA applies to your situation before paying for a membership. For help understanding your coverage, see our guide on <a href="/guides/how-to-negotiate-medical-bills">how to negotiate medical bills</a>.
</div>

<h2 id="how-to-dispute">6. How to dispute an air ambulance bill</h2>

<p>Disputing an air ambulance bill requires different strategies depending on whether you are insured, uninsured, or dealing with a pre-2022 bill. For a full walkthrough of medical bill disputes, see our <a href="/guides/how-to-negotiate-medical-bills">negotiation guide</a>.</p>

<h3>Strategy 1 &mdash; Invoke the No Surprises Act (insured, post-2022)</h3>

<p>If you have insurance and the flight occurred after January 1, 2022, send a written letter to the air ambulance company stating that under the No Surprises Act (Public Law 116-260, Division BB, Title I), they are prohibited from balance billing you beyond your in-network cost-sharing amount. Include your insurance information and the Explanation of Benefits (EOB) showing what your insurer paid. Request that the provider bill only your in-network cost-sharing and close the account.</p>

<h3>Strategy 2 &mdash; Medicare rate comparison (any patient)</h3>

<p>Look up the Medicare rate for your transport code using our <a href="/calculator">calculator</a>. Present the comparison to the billing department: &ldquo;Medicare pays $6,515 for a helicopter base rate. You have billed $42,000. I am requesting a reduction to a rate that reflects actual costs.&rdquo; Many providers will negotiate to 2&ndash;3x the Medicare rate when confronted with the data.</p>

<h3>Strategy 3 &mdash; Charity care and financial hardship programs</h3>

<p>Most air ambulance companies have financial assistance programs, though they do not always advertise them. Request a financial hardship application. Provide proof of income (pay stubs, tax return). Patients earning below 300&ndash;400% of the federal poverty level often qualify for full write-offs or reductions of 70&ndash;90%. If you <a href="/guides/cant-afford-medical-bill">can&rsquo;t afford your medical bill</a>, this is often the most effective path.</p>

<h3>Strategy 4 &mdash; State attorney general complaint</h3>

<p>If the provider refuses to comply with the NSA or engages in aggressive collection practices, file a complaint with your state attorney general&rsquo;s consumer protection division. AG offices have successfully forced air ambulance companies to rescind improper balance bills.</p>

<h3>Strategy 5 &mdash; CMS and CFPB complaints</h3>

<p>For NSA violations, file a formal complaint with CMS at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a>. If the provider has sent the bill to collections or is engaging in unfair debt collection, file a complaint with the Consumer Financial Protection Bureau (CFPB).</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; SkyMed Air Ambulance &mdash; Date of Service: 06/12/2025</div>
    <div class="line-item flagged">
        <span>A0436 &mdash; Rotary-wing air transport, base rate &nbsp; &#9888; <em>Medicare base rate is ~$6,515</em></span>
        <span>$28,500.00</span>
    </div>
    <div class="line-item flagged">
        <span>A0436 &mdash; Loaded air miles (62 miles &times; $285/mile) &nbsp; &#9888; <em>Medicare mileage rate is ~$16&ndash;$30/mile</em></span>
        <span>$17,670.00</span>
    </div>
    <div class="line-item">
        <span>Flight nurse and paramedic crew</span>
        <span>$4,200.00</span>
    </div>
    <div class="line-item">
        <span>Medical supplies (IV, medications, cardiac monitoring)</span>
        <span>$1,850.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$52,220.00</span>
    </div>
</div>

<p><strong>Medicare comparison for this flight:</strong> Medicare would reimburse approximately $6,515 (base) + $1,488 (62 miles &times; ~$24/mile) = <strong>$8,003</strong>. The billed amount of $52,220 represents a <strong>552% markup</strong> over what Medicare pays.</p>

<div class="case-study">
    <h3>NSA dispute: $47,000 balance bill eliminated</h3>
    <p>A 34-year-old construction worker in Montana was airlifted to a trauma center after a worksite accident in August 2023. His insurer paid $8,200 toward the $55,200 bill. The air ambulance company billed him $47,000 for the balance. He submitted a written dispute citing the No Surprises Act, noting that as an insured patient transported in an emergency after January 2022, the provider could not balance bill him beyond his in-network deductible and coinsurance.</p>
    <p>After reviewing the claim, the air ambulance company confirmed the NSA applied and reduced his patient responsibility to his $2,500 deductible plus 20% coinsurance on the insurer&rsquo;s allowed amount &mdash; a total of $4,140. <strong>Savings: $42,860.</strong></p>
</div>

<div class="case-study">
    <h3>Charity care: $39,000 bill reduced to $0</h3>
    <p>An uninsured 58-year-old woman in rural Arizona was airlifted after a cardiac event in 2024. The air ambulance company billed $39,400. She applied for the company&rsquo;s financial hardship program, providing her tax return showing household income of $31,000 (approximately 250% of the federal poverty level). The company approved a full write-off under its charity care policy, reducing the bill to <strong>$0</strong>. She was never sent to collections.</p>
    <p><strong>Key lesson:</strong> Always ask for financial assistance before assuming you must pay. Most major air ambulance companies have charity care programs for patients below 300&ndash;400% of the federal poverty level.</p>
</div>

<h2 id="insurance-coverage">7. When your insurance must pay</h2>

<p>Understanding when your insurer is obligated to cover air ambulance transport &mdash; and what you actually owe &mdash; is critical to avoiding overpayment.</p>

<h3>In-network air ambulance</h3>

<p>If the air ambulance provider is in-network with your health plan, standard in-network cost-sharing applies: your copay, coinsurance, and deductible. The insurer pays the remainder directly to the provider. You owe nothing beyond your cost-sharing amount.</p>

<h3>Out-of-network air ambulance (post-NSA)</h3>

<p>Since January 1, 2022, even out-of-network air ambulance providers are subject to the No Surprises Act. Your insurer must treat the claim as in-network for cost-sharing purposes. The provider and insurer resolve any payment dispute through the federal IDR process. You are not responsible for the gap.</p>

<h3>Emergency exceptions</h3>

<p>Air ambulance transport is almost always classified as an emergency service. The NSA&rsquo;s emergency protections apply when a &ldquo;prudent layperson&rdquo; would reasonably believe the situation required immediate medical attention. You do not need prior authorization for emergency air transport, and your insurer cannot deny the claim solely because you did not get pre-approval.</p>

<h3>When insurers push back</h3>

<p>Some insurers attempt to deny air ambulance claims by arguing the transport was not &ldquo;medically necessary&rdquo; &mdash; that ground transport would have been sufficient. If your insurer denies coverage:</p>

<ol>
    <li>Request the denial in writing with the specific reason and denial code.</li>
    <li>Obtain a letter of medical necessity from the treating physician documenting why air transport was required (distance, time sensitivity, patient condition, terrain).</li>
    <li>File an internal appeal within the insurer&rsquo;s deadline (typically 180 days).</li>
    <li>If the internal appeal fails, request an independent external review. The external reviewer&rsquo;s decision is binding on the insurer under the ACA.</li>
</ol>

<div class="key-takeaway">
    <strong>Your insurer cannot make you pay more than in-network cost-sharing for emergency air ambulance after January 2022.</strong> If your Explanation of Benefits shows the claim was processed as out-of-network with higher cost-sharing, call your insurer and cite the No Surprises Act. If they refuse to reprocess, file a complaint with your state insurance commissioner and with CMS. For help reading your EOB, see our <a href="/guides/no-surprises-act-explained">No Surprises Act guide</a>.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does an air ambulance ride cost?</h3>
        <p>The average air ambulance flight costs $36,400, but bills regularly range from $12,000 to over $100,000 depending on distance, crew, and provider. Medicare pays approximately $6,515 for a helicopter transport base rate. Use our <a href="/calculator">cost calculator</a> to compare your bill against Medicare rates.</p>
    </div>

    <div class="faq-item">
        <h3>Does insurance cover air ambulance bills?</h3>
        <p>Most plans cover medically necessary air transport. Since January 1, 2022, the No Surprises Act prohibits air ambulance providers from balance billing insured patients beyond in-network cost-sharing, regardless of network status. If your insurer denied the claim, appeal with a letter of medical necessity from the treating physician.</p>
    </div>

    <div class="faq-item">
        <h3>Does the No Surprises Act cover air ambulance?</h3>
        <p>Yes. The NSA fully protects insured patients from air ambulance balance billing as of January 1, 2022. If a provider bills you more than your in-network copay, coinsurance, or deductible for a post-2022 emergency flight, they are violating federal law. File complaints with CMS and your state insurance commissioner. Note that ground ambulance is <em>not</em> covered by the NSA.</p>
    </div>

    <div class="faq-item">
        <h3>Are air ambulance membership programs worth it?</h3>
        <p>Since the No Surprises Act now covers insured patients, memberships are most valuable for uninsured individuals or those in rural areas far from trauma centers. Programs cost $50&ndash;$100 per year and cover the patient&rsquo;s balance after insurance. If you are insured and your flight occurred after January 2022, a membership may be unnecessary.</p>
    </div>

    <div class="faq-item">
        <h3>Can I negotiate an air ambulance bill?</h3>
        <p>Yes. Uninsured patients and those with pre-2022 bills can negotiate directly. Use the Medicare rate ($6,515 helicopter base rate) as your benchmark. Many air ambulance companies accept 20&ndash;40% of the billed amount, especially through their financial hardship programs. Always get settlement agreements in writing.</p>
    </div>

    <div class="faq-item">
        <h3>What should I do if I get an air ambulance bill I cannot afford?</h3>
        <p>First, check whether the No Surprises Act applies (insured, post-January 2022). If so, you should only owe in-network cost-sharing. If uninsured, request an itemized bill, compare against Medicare rates, and apply for the provider&rsquo;s charity care or financial hardship program. Many providers write off 70&ndash;100% of bills for patients below 300&ndash;400% of the federal poverty level. See our <a href="/guides/cant-afford-medical-bill">guide on affording medical bills</a> for more options.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.gao.gov/products/gao-22-105078" target="_blank" rel="noopener">GAO &mdash; Air Ambulance: Available Data Show Privately-Insured Patients Are at Financial Risk (2022)</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS &mdash; No Surprises Act: Air Ambulance Protections and Complaint Process</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/ambulance" target="_blank" rel="noopener">CMS &mdash; Medicare Ambulance Fee Schedule (2026)</a></li>
    <li><a href="https://jamanetwork.com/journals/jama/article-abstract/2730520" target="_blank" rel="noopener">JAMA &mdash; Air Ambulance Billing and Out-of-Network Charges (2019 Yale Study)</a></li>
    <li><a href="https://www.kff.org/private-insurance/issue-brief/air-ambulance-services/" target="_blank" rel="noopener">Kaiser Family Foundation &mdash; Air Ambulance Services: Understanding the Charges and Protections</a></li>
    <li><a href="https://www.consumerfinance.gov/ask-cfpb/what-is-the-no-surprises-act-en-2123/" target="_blank" rel="noopener">CFPB &mdash; What Is the No Surprises Act?</a></li>
    <li><a href="https://kffhealthnews.org/news/article/air-ambulance-bills-no-surprises-act-balance-billing/" target="_blank" rel="noopener">KFF Health News &mdash; Air Ambulance Bills and the No Surprises Act</a></li>
</ul>
""",
})
