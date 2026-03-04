"""Guide: Ground Ambulance Billing Costs."""

from guides import register, _embed

register("ground-ambulance-billing-costs", {
    "title": "Ground Ambulance Bills: Why They&rsquo;re So Expensive and How to Fight Back",
    "meta_description": "Ground ambulance bills average $1,200-$2,500 for BLS and $2,500+ for ALS. Learn why they're excluded from the No Surprises Act and how to negotiate yours down.",
    "published": "2026-03-04",
    "author": "BillKarma Team",
    "category": "Medical Bills",
    "faqs": [
        {
            "q": "Why are ground ambulance bills so expensive?",
            "a": "Ground ambulance services carry high fixed costs including 24/7 staffing, vehicle maintenance, medical equipment, and liability insurance. Most providers are out-of-network with commercial insurers, so they set their own prices. The absence of price competition (you cannot choose which ambulance responds to 911) allows providers to charge well above Medicare rates. BLS ground transport costs $1,200-$2,500, while ALS runs $2,500 or more.",
        },
        {
            "q": "Does the No Surprises Act cover ground ambulance bills?",
            "a": "No. The No Surprises Act explicitly excluded ground ambulance services from its balance billing protections. Air ambulance is fully covered, but ground ambulance was carved out. Congress created the Ground Ambulance and Patient Billing Advisory Committee (GAPB) to study the issue, but no federal legislation has been enacted as of 2026. Some states have passed their own ground ambulance balance billing laws.",
        },
        {
            "q": "How much does Medicare pay for a ground ambulance ride?",
            "a": "Medicare pays approximately $450-$500 for a BLS emergency transport (code A0429) and $550-$600 for an ALS Level 1 emergency transport (code A0427), plus $8.85 per loaded mile. The GAO found that the median billed amount for a ground ambulance ride is 2.7 times the Medicare rate, and some providers bill 8-10 times Medicare.",
        },
        {
            "q": "Can I negotiate a ground ambulance bill?",
            "a": "Yes. Ground ambulance companies, especially private ones, frequently accept 40-70% of the original billed amount. Start by requesting an itemized bill and the Patient Care Report. Verify the service level (BLS vs. ALS) matches care provided. Offer to pay the Medicare rate or 150-200% of Medicare as a lump sum. Get any agreement in writing before paying.",
        },
        {
            "q": "Which states protect patients from ground ambulance balance billing?",
            "a": "As of 2026, approximately 18 states have enacted some form of ground ambulance balance billing protection. States with strong protections include Colorado, Connecticut, Illinois, Maryland, New York, Oregon, Texas, and Vermont. Protection strength varies: some cap patient liability at in-network cost-sharing, while others require only disclosure. Check your state insurance department website.",
        },
        {
            "q": "What should I do if I receive a ground ambulance bill I cannot afford?",
            "a": "Request an itemized bill and the Patient Care Report to verify accuracy. Check whether your state has balance billing protections. Ask the ambulance company for their uninsured or hardship rate. Offer a lump-sum settlement at the Medicare rate. Request a zero-interest payment plan if you cannot pay in full. Upload your bill to BillKarma to identify overcharges and build negotiation leverage.",
        },
    ],
    "body": f"""
<p class="lead">A ground ambulance ride averages <strong>$1,277 for BLS</strong> (Basic Life Support) and <strong>$2,500+ for ALS</strong> (Advanced Life Support)&mdash;for a trip that typically lasts under 20 minutes. Medicare pays just $450&ndash;$600 for the same ride. The gap between what ambulance companies charge and what insurance pays lands squarely on patients. Worse, ground ambulance is the <strong>only emergency medical service explicitly excluded from the No Surprises Act</strong>. This guide covers why ground ambulance costs are so high, which states offer protections, and exactly how to fight back.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#why-expensive">Why ground ambulance is so expensive</a></li>
        <li><a href="#cost-breakdown">Average costs: BLS vs. ALS vs. critical care</a></li>
        <li><a href="#medicare-vs-billed">Medicare rates vs. billed amounts</a></li>
        <li><a href="#no-surprises-gap">The No Surprises Act gap</a></li>
        <li><a href="#state-protections">Balance billing protections by state</a></li>
        <li><a href="#negotiate-appeal">How to negotiate or appeal your bill</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="why-expensive">1. Why ground ambulance is so expensive</h2>

<p>Ground ambulance billing operates unlike almost any other medical service. When you call 911, you have <strong>zero choice</strong> in which ambulance company responds. The closest available unit is dispatched&mdash;whether it is a municipal fire department, a hospital-based service, or a private company like American Medical Response (AMR). You never see a price list, never consent to a specific charge, and in most states there is no legal cap on what they can bill.</p>

<p>Several factors drive the high costs:</p>

<ul>
    <li><strong>24/7 staffing requirements.</strong> Ambulance crews must be available around the clock, including during low-call-volume hours. Labor accounts for 60&ndash;70% of operating costs.</li>
    <li><strong>Low government reimbursement.</strong> Medicare and Medicaid cover roughly 40&ndash;60% of the actual cost of providing a ground ambulance ride. Providers argue they must charge commercial patients more to make up the shortfall.</li>
    <li><strong>Out-of-network status.</strong> Most ground ambulance services are out-of-network with most insurance plans, so they are not bound by negotiated rates.</li>
    <li><strong>No price competition.</strong> Patients cannot shop for ambulance services in an emergency, eliminating the market pressure that constrains pricing elsewhere.</li>
    <li><strong>Private equity consolidation.</strong> Large private equity-backed ambulance companies now control a significant share of ground ambulance services nationally. The GAO found consolidation has contributed to higher prices, particularly in rural areas with exclusive contracts.</li>
</ul>

<div class="key-takeaway">
    <strong>The core problem:</strong> Ground ambulance is an emergency service where you have no choice, no ability to compare prices, and&mdash;in most states&mdash;no legal protection from surprise bills. This combination allows providers to charge far above what insurance or Medicare pays, leaving patients with the balance.
</div>

<h2 id="cost-breakdown">2. Average costs: BLS vs. ALS vs. critical care</h2>

<p>Ground ambulance billing has two components: a <strong>base rate</strong> (determined by level of care) and a <strong>mileage charge</strong> (per loaded mile&mdash;the distance traveled with the patient onboard).</p>

<table>
    <thead>
        <tr><th>Service Level</th><th>HCPCS Code</th><th>Typical Billed Amount</th><th>Medicare Rate (2026)</th><th>Markup Over Medicare</th></tr>
    </thead>
    <tbody>
        <tr><td>BLS Emergency</td><td>A0429</td><td>$1,200&ndash;$2,500</td><td>~$451</td><td>2.7x&ndash;5.5x</td></tr>
        <tr><td>ALS Level 1 Emergency</td><td>A0427</td><td>$2,500&ndash;$4,500</td><td>~$553</td><td>4.5x&ndash;8.1x</td></tr>
        <tr><td>ALS Level 2 (Critical Care)</td><td>A0433</td><td>$3,000&ndash;$6,000</td><td>~$752</td><td>4.0x&ndash;8.0x</td></tr>
        <tr><td>Mileage (per loaded mile)</td><td>A0425</td><td>$25&ndash;$60/mile</td><td>$8.85/mile</td><td>2.8x&ndash;6.8x</td></tr>
    </tbody>
</table>

<div class="bill-example">
    <div class="bill-header">Sample Ground Ambulance Bill &mdash; Private Provider, 12-Mile Transport</div>
    <div class="line-item flagged">
        <span>A0427 &mdash; ALS Level 1 Emergency Transport &nbsp; &#9888; <em>Medicare pays $553</em></span>
        <span>$3,200</span>
    </div>
    <div class="line-item flagged">
        <span>A0425 &mdash; Mileage, 12 loaded miles &nbsp; &#9888; <em>Medicare pays $106 ($8.85 &times; 12)</em></span>
        <span>$540</span>
    </div>
    <div class="line-item">
        <span>A0398 &mdash; Oxygen administration</span>
        <span>$125</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$3,865</span>
    </div>
</div>

<p>In this example, Medicare would reimburse approximately <strong>$659</strong> for the same transport. The patient&rsquo;s bill is <strong>5.9 times the Medicare rate</strong>. If the insurer pays a negotiated rate of $1,200, the ambulance company may balance bill the patient for the remaining $2,665.</p>

{_embed(mode="cost", title="Look Up Your Ambulance Code", subtitle="Enter the HCPCS code from your ground ambulance bill to see what Medicare pays.")}

<h2 id="medicare-vs-billed">3. Medicare rates vs. billed amounts</h2>

<p>The gap between what ambulance companies charge and what Medicare pays is among the widest in all of healthcare. A 2023 GAO report found:</p>

<ul>
    <li>The <strong>median charge</strong> for a ground ambulance transport was <strong>2.7 times the Medicare rate</strong></li>
    <li>The <strong>75th percentile</strong> charge was <strong>5.2 times Medicare</strong></li>
    <li>Some providers billed <strong>8&ndash;10 times Medicare</strong>, particularly in areas served by a single ambulance company</li>
    <li>Privately insured patients were billed <strong>$450 more on average</strong> than what Medicare would have paid for the same transport</li>
</ul>

<div class="case-study">
    <h3>Example: $4,800 ALS bill vs. $553 Medicare rate</h3>
    <p>A 58-year-old patient in suburban Texas experienced chest pain and called 911. The responding ALS unit transported him 9 miles to the nearest hospital. He was conscious, had stable vital signs, and received an IV line and cardiac monitoring. The ambulance company billed <strong>$4,800</strong>. Medicare would have paid approximately <strong>$633</strong> ($553 base + $80 for 9 loaded miles). The patient&rsquo;s commercial insurer paid $1,100 and the ambulance company balance billed him <strong>$3,700</strong>.</p>
    <p>After <a href="/scan">scanning his bill with BillKarma</a>, the patient identified the 8.7x Medicare markup and negotiated a settlement of $800. <strong>Total savings: $4,000.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Use Medicare as your benchmark.</strong> When negotiating a ground ambulance bill, offering 150&ndash;200% of the Medicare rate is a fair starting point. Use our <a href="/calculator">BillKarma calculator</a> to look up the Medicare rate for the specific HCPCS code on your bill.
</div>

<h2 id="no-surprises-gap">4. The No Surprises Act gap</h2>

<p>When the No Surprises Act took effect on January 1, 2022, it banned balance billing for most emergency services&mdash;including ER visits, air ambulance, and care by out-of-network providers at in-network facilities. But Congress deliberately <strong>excluded ground ambulance</strong>.</p>

<p>The ground ambulance industry lobbied against inclusion, arguing that banning balance billing without increasing government payment rates would drive providers out of business in rural areas. Instead, Congress created the <strong>Ground Ambulance and Patient Billing (GAPB) Advisory Committee</strong>. The committee submitted recommendations in 2023, but as of March 2026, no federal legislation has been enacted.</p>

<table>
    <thead>
        <tr><th>Emergency Service</th><th>No Surprises Act Protection</th><th>Can You Be Balance Billed?</th></tr>
    </thead>
    <tbody>
        <tr><td>Emergency room (facility)</td><td>Yes &mdash; since Jan 2022</td><td>No (limited to in-network cost-sharing)</td></tr>
        <tr><td>Out-of-network ER physician</td><td>Yes &mdash; since Jan 2022</td><td>No</td></tr>
        <tr><td>Air ambulance</td><td>Yes &mdash; since Jan 2022</td><td>No</td></tr>
        <tr><td><strong>Ground ambulance</strong></td><td><strong>No &mdash; explicitly excluded</strong></td><td><strong>Yes (in most states)</strong></td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Do not assume you are protected.</strong> If you received a ground ambulance bill and expected the No Surprises Act to limit your costs, check your state&rsquo;s laws. Federal protection does not apply. See our <a href="/guides/no-surprises-act-explained">No Surprises Act guide</a> for what IS covered.
</div>

<h2 id="state-protections">5. Balance billing protections by state</h2>

<p>Because the federal government did not protect patients from ground ambulance balance billing, a patchwork of state laws determines your rights.</p>

<table>
    <thead>
        <tr><th>Protection Level</th><th>States</th><th>What It Means</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Strong</strong> (patient liability capped at in-network cost-sharing)</td><td>CO, CT, IL, MD, NY, OR, TX, VT, WA</td><td>You pay only your in-network copay/coinsurance. Insurer and ambulance company resolve the rest.</td></tr>
        <tr><td><strong>Moderate</strong> (some limits on balance billing)</td><td>CA, DE, GA, ME, MN, NM, VA</td><td>Varying caps or dispute resolution. You may still owe some balance beyond in-network rates.</td></tr>
        <tr><td><strong>Weak or None</strong></td><td>FL, AZ, NC, SC, AL, MS, TN, KY, IN, MO, WI, and others</td><td>No state protection. You can be balance billed the full difference.</td></tr>
    </tbody>
</table>

<p>Even in states with strong protections, the law typically applies only to <strong>state-regulated insurance plans</strong> (individual, small group, some large group). Self-funded employer plans&mdash;which cover roughly 65% of employer-insured workers&mdash;are regulated under federal ERISA and are generally <strong>not subject</strong> to state balance billing bans.</p>

<p>If your state has <strong>no</strong> ground ambulance protections, your best options are negotiation (Section 6) and <a href="/charity-care">checking charity care eligibility</a> if the ambulance company is affiliated with a nonprofit hospital system.</p>

<h2 id="negotiate-appeal">6. How to negotiate or appeal your bill</h2>

<h3>Step 1: Get the right documents</h3>

<ul>
    <li><strong>Itemized bill.</strong> Shows HCPCS codes, service level, mileage, and add-on charges. Verify every code against what actually happened.</li>
    <li><strong>Patient Care Report (PCR).</strong> The ambulance crew&rsquo;s official record&mdash;documents your condition, interventions, vital signs, and loaded miles. You are legally entitled to a copy.</li>
</ul>

<h3>Step 2: Check for billing errors</h3>

<ul>
    <li><strong>Upcoded service level.</strong> Billed as ALS when only BLS care was provided (no IV medications, no advanced airway, no cardiac monitoring). The PCR shows what interventions were actually performed.</li>
    <li><strong>Inflated mileage.</strong> Loaded miles count only while you are in the ambulance. Some bills include response miles (the drive to your location) or round-trip distance.</li>
    <li><strong>Separately billed supplies.</strong> Basic supplies like oxygen and bandages are typically included in the base rate. Separate line items for these may be duplicate charges.</li>
</ul>

<p><a href="/scan">Upload your ambulance bill to BillKarma</a> to automatically flag upcoding, mileage discrepancies, and overcharges.</p>

<h3>Step 3: Negotiate</h3>

<table>
    <thead>
        <tr><th>Strategy</th><th>Typical Result</th><th>Script</th></tr>
    </thead>
    <tbody>
        <tr><td>Ask for uninsured/hardship rate</td><td>30&ndash;50% off</td><td>&ldquo;I&rsquo;m uninsured. What is your self-pay or hardship rate?&rdquo;</td></tr>
        <tr><td>Offer Medicare rate</td><td>Pay $450&ndash;$750 on a $2,000+ bill</td><td>&ldquo;I&rsquo;d like to settle at the Medicare-allowable rate for these codes.&rdquo;</td></tr>
        <tr><td>Lump-sum offer</td><td>40&ndash;60% of billed amount</td><td>&ldquo;I can pay $X today as full and final settlement.&rdquo;</td></tr>
        <tr><td>Payment plan</td><td>Full amount over 6&ndash;24 months, 0% interest</td><td>&ldquo;Can I set up a monthly payment plan with no interest?&rdquo;</td></tr>
    </tbody>
</table>

<h3>Step 4: Appeal to your insurer</h3>

<p>If your insurer underpaid or denied the claim, file an appeal with:</p>

<ul>
    <li>A <strong>letter of medical necessity</strong> from the treating ER physician</li>
    <li>The <strong>Patient Care Report</strong> documenting your condition and interventions</li>
    <li>An <strong>out-of-network exception request</strong> arguing you had no choice of ambulance provider</li>
</ul>

<p>See our <a href="/guides/how-to-appeal-insurance-denial-and-win">guide to winning insurance appeals</a> for templates and step-by-step instructions.</p>

<div class="case-study">
    <h3>Example: Patient reduces $3,400 ground ambulance bill to $680</h3>
    <p>A patient in North Carolina was transported 10 miles after a car accident. The private ambulance company billed $3,400 (ALS Level 1 + mileage). The insurer paid $900 and the company balance billed $2,500. North Carolina has no ground ambulance balance billing law.</p>
    <p>The patient requested the PCR and found the crew administered only basic care&mdash;no IV medications, no cardiac drugs&mdash;meaning the transport should have been BLS, not ALS. The patient filed a corrected claim with the insurer and offered the ambulance company the Medicare rate ($451 + $89 mileage = $540) as a lump-sum settlement. The company accepted $680.</p>
    <p><strong>Original bill: $3,400. Patient paid: $680. Savings: $2,720 (80%).</strong></p>
</div>

<div class="key-takeaway">
    <strong>Start with your bill, not your wallet.</strong> <a href="/scan">Scan your ground ambulance bill with BillKarma</a> to identify upcoding, mileage inflation, and the Medicare rate for your transport. You&rsquo;ll walk into the negotiation knowing exactly what a fair price looks like.
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.gao.gov/products/gao-23-105676" target="_blank" rel="noopener">GAO: Ground Ambulance Services &mdash; Costs and Medicare Margins Varied (2023)</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/ground-ambulance-rides-and-surprise-medical-bills/" target="_blank" rel="noopener">KFF: Ground Ambulance Rides and Surprise Medical Bills</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/ambulance" target="_blank" rel="noopener">CMS: Medicare Ambulance Fee Schedule (2026)</a></li>
    <li><a href="https://www.nhtsa.gov/emergency-medical-services" target="_blank" rel="noopener">NHTSA: Office of Emergency Medical Services</a></li>
    <li><a href="https://www.cms.gov/nosurprises/consumers" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Information for Consumers</a></li>
    <li><a href="https://www.gao.gov/products/gao-22-105078" target="_blank" rel="noopener">GAO: Air Ambulance &mdash; Available Data Show Privately-Insured Patients Are at Financial Risk (2022)</a></li>
</ul>
""",
})
