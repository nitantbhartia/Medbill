"""Guide: Hospital Price Transparency in 2026."""

from guides import register, _embed

_calc_embed = _embed(mode="cost", title="Look up Medicare rates for any procedure", subtitle="Enter a CPT code to see what Medicare pays &mdash; your best benchmark for evaluating hospital prices.", height="400")
_markup_embed = _embed(mode="markup", title="Calculate your hospital&rsquo;s markup", subtitle="Enter a CPT code and the amount you were charged to see the markup over Medicare.", height="420")

register("hospital-price-transparency-rules-2026", {
    "title": "Hospital Price Transparency in 2026: How to Use It to Lower Your Bill",
    "meta_description": "Hospitals must publish all prices online or face $2M+ fines. Learn how to find, read, and use hospital price data to negotiate your medical bill down.",
    "published": "2026-02-27",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "What is the hospital price transparency rule?",
            "a": "The CMS Hospital Price Transparency Rule (45 CFR Part 180) requires every U.S. hospital to publish a machine-readable file listing all standard charges, including gross charges, discounted cash prices, payer-specific negotiated rates, and de-identified minimum and maximum rates. Hospitals must also display a consumer-friendly list of at least 300 shoppable services. Non-compliance can result in fines up to $2,007,500 per year.",
        },
        {
            "q": "How do I find my hospital's price transparency file?",
            "a": "Go to the hospital's website and search for 'price transparency,' 'standard charges,' or 'chargemaster.' The file is usually linked from the homepage footer or a dedicated pricing page. You can also try hospital.com/pricing or hospital.com/price-transparency directly. BillKarma's hospital directory parses these files so you can search by procedure without downloading a spreadsheet.",
        },
        {
            "q": "Can I actually use hospital price data to lower my bill?",
            "a": "Yes. If you find that your insurer's negotiated rate in the hospital's file is lower than what you were billed, you can call the billing department and reference the specific rate from their own published data. Hospitals are required to honor the rates they post. Patients have saved thousands by catching discrepancies between billed amounts and posted negotiated rates.",
        },
        {
            "q": "What penalties do hospitals face for not publishing prices?",
            "a": "As of 2025, CMS can fine hospitals up to $5,500 per day for non-compliance, with a maximum annual penalty of $2,007,500. CMS has stepped up enforcement with warning letters, corrective action requests, and civil monetary penalty notices. Any member of the public can report a non-compliant hospital through the CMS online complaint form.",
        },
        {
            "q": "What is the Transparency in Coverage Rule and how is it different?",
            "a": "The Transparency in Coverage Rule applies to health insurers, not hospitals. It requires insurers to publish machine-readable files of their negotiated rates with all in-network providers, and to offer a patient-facing price comparison tool. Together with the hospital rule, patients now have access to pricing data from both sides of the negotiation.",
        },
        {
            "q": "Are hospital price transparency files accurate?",
            "a": "Accuracy varies. Some hospitals post complete, current data updated annually. Others post outdated files, omit payer-specific rates, or include placeholder data. Patient Rights Advocate's audits find significant quality gaps even among technically compliant hospitals. Cross-referencing with your insurer's published rates and Medicare benchmarks helps verify accuracy.",
        },
    ],
    "body": f"""
<p class="lead">Since January 2021, every hospital in America has been required to publish its prices online. Since 2025, CMS can fine hospitals up to <strong>$2 million per year</strong> for non-compliance. Compliance rates have climbed &mdash; roughly 70% of hospitals now post substantially complete files &mdash; but most patients still have no idea this data exists or how to use it. Here&rsquo;s how to actually use hospital price transparency data to negotiate your bill down.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-law-requires">What the law requires</a></li>
        <li><a href="#whats-changed">What&rsquo;s changed in 2025&ndash;2026</a></li>
        <li><a href="#find-prices">How to find your hospital&rsquo;s prices</a></li>
        <li><a href="#read-data">How to read the price data</a></li>
        <li><a href="#negotiate-with-data">Using price data in negotiations</a></li>
        <li><a href="#compliance-reality">Compliance reality: who&rsquo;s still hiding prices</a></li>
        <li><a href="#compare-hospitals">Comparing prices across hospitals</a></li>
        <li><a href="#insurer-transparency">What the insurer transparency rule adds</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-law-requires">1. What the law requires</h2>

<p>The CMS Hospital Price Transparency Rule (45 CFR Part 180) applies to every hospital operating in the United States &mdash; roughly 6,000 facilities. It has two core requirements:</p>

<p><strong>Requirement 1: A comprehensive machine-readable file.</strong> Every hospital must publish a single file in CSV, JSON, or XML format containing all standard charges for all items and services. &ldquo;All&rdquo; means every procedure, every supply item, every room charge &mdash; not just a curated list. The file must include five data elements for each service:</p>

<ul>
    <li><strong>Gross charge</strong> &mdash; the chargemaster list price (what the hospital bills before any discounts)</li>
    <li><strong>Discounted cash price</strong> &mdash; the self-pay rate for patients paying without insurance</li>
    <li><strong>Payer-specific negotiated rates</strong> &mdash; the actual rate each insurer has contracted to pay, listed by payer name and plan</li>
    <li><strong>De-identified minimum negotiated rate</strong> &mdash; the lowest rate any payer has negotiated</li>
    <li><strong>De-identified maximum negotiated rate</strong> &mdash; the highest rate any payer has negotiated</li>
</ul>

<p><strong>Requirement 2: A consumer-friendly shoppable services display.</strong> In addition to the machine-readable file, hospitals must post a simplified display of prices for at least 300 &ldquo;shoppable&rdquo; services &mdash; procedures a patient can schedule in advance. This display must be accessible without downloading special software, and it must include the negotiated rates, cash price, and a plain-language description of each service.</p>

<p>Both requirements have been in effect since January 1, 2021. The file must be updated at least annually, posted without requiring login or registration, and linked from a publicly accessible page on the hospital&rsquo;s website.</p>

<div class="key-takeaway">
    <strong>See how your hospital stacks up.</strong> BillKarma&rsquo;s <a href="/hospitals/">hospital directory</a> parses these price transparency files and grades hospitals on pricing fairness. Search by name or city to see your hospital&rsquo;s profile, complete with procedure-level pricing data.
</div>

<h2 id="whats-changed">2. What&rsquo;s changed in 2025&ndash;2026</h2>

<p>The price transparency landscape in 2026 looks very different from 2021. Several major shifts have reshaped how the rule works in practice:</p>

<p><strong>Increased penalties and enforcement.</strong> CMS raised the maximum penalty to $5,500 per day for hospitals with 30 or more beds, translating to a maximum of <strong>$2,007,500 per year</strong>. More importantly, CMS has moved beyond warning letters to issuing actual civil monetary penalty notices. Multiple hospital systems have received penalty assessments, and several high-profile cases have been publicized to deter non-compliance.</p>

<p><strong>Higher compliance rates.</strong> Patient Rights Advocate&rsquo;s audits show compliance climbing from roughly 36% in 2022 to approximately 70% substantial compliance by late 2024. The remaining 30% are split between partial compliance (file posted but missing key data like payer-specific rates) and outright non-compliance (no file, or a PDF that doesn&rsquo;t meet the machine-readable requirement).</p>

<p><strong>CMS enforcement actions.</strong> CMS has issued corrective action requests to hundreds of hospitals, requiring them to post compliant files within a specified timeframe or face escalating penalties. The agency also published a public list of hospitals that received warning letters, creating reputational pressure beyond the financial penalty.</p>

<p><strong>The Transparency in Coverage Rule.</strong> Since July 2022 (machine-readable files) and January 2023 (patient-facing tools), health insurers have been required to publish their own negotiated rate data. This means pricing information is now available from both sides: the hospital publishes what each insurer pays, and the insurer publishes what it pays each hospital. These two datasets can be cross-referenced to verify accuracy.</p>

<p><strong>State-level requirements.</strong> Several states have enacted their own transparency laws that go beyond the federal rule. Colorado, Maine, and Oregon now require hospitals to provide good-faith price estimates before scheduled services. New York and California have enacted balance billing protections tied to transparency data. These state rules complement the federal rule and close some of its enforcement gaps.</p>

<div class="key-takeaway">
    <strong>Already have a bill you want to check?</strong> <a href="/scan">Upload your bill to BillKarma</a> and we&rsquo;ll compare every line item to Medicare rates and flag charges worth disputing &mdash; no price file reading required.
</div>

<h2 id="find-prices">3. How to find your hospital&rsquo;s prices</h2>

<p>Finding a hospital&rsquo;s price transparency file is straightforward at compliant hospitals and frustrating at non-compliant ones. Here is a step-by-step approach:</p>

<p><strong>Step 1: Try the direct URL.</strong> Many hospitals post their file at a predictable URL. Try these patterns:</p>

<ul>
    <li><code>hospital.com/pricing</code></li>
    <li><code>hospital.com/price-transparency</code></li>
    <li><code>hospital.com/standard-charges</code></li>
    <li><code>hospital.com/chargemaster</code></li>
</ul>

<p><strong>Step 2: Search the hospital&rsquo;s website.</strong> Use the site&rsquo;s search function with terms like &ldquo;price transparency,&rdquo; &ldquo;standard charges,&rdquo; or &ldquo;machine-readable file.&rdquo; The link is often buried in the footer or a &ldquo;Patients &amp; Visitors&rdquo; section.</p>

<p><strong>Step 3: Search Google with a site filter.</strong> Enter <code>site:hospitalname.com price transparency</code> in Google. This often surfaces the page faster than the hospital&rsquo;s own site search.</p>

<p><strong>Step 4: Check BillKarma.</strong> Our <a href="/hospitals/">hospital directory</a> has already located and parsed the price transparency file for thousands of hospitals. You can search by procedure, compare rates across payers, and see the data without downloading a spreadsheet. If a hospital has no grade on BillKarma, it typically means their file was too incomplete or improperly formatted for us to parse.</p>

<p><strong>Step 5: Call the billing department.</strong> If you cannot find the file online, call the hospital and ask: &ldquo;Can you direct me to your machine-readable standard charges file as required by the CMS price transparency rule?&rdquo; Staff may not know the term &ldquo;machine-readable file,&rdquo; so also ask for the &ldquo;chargemaster&rdquo; or &ldquo;published pricing.&rdquo;</p>

<p><strong>What the file looks like when you find it:</strong> A compliant file is a CSV, JSON, or XML download &mdash; typically very large (10,000+ rows). Each row represents one service identified by CPT code, revenue code, or both. Columns include the five required data elements listed in Section 1 above, plus the payer name and plan name for each negotiated rate.</p>

<h2 id="read-data">4. How to read the price data</h2>

<p>The raw price transparency file can be overwhelming &mdash; thousands of rows and dozens of columns. Here is how to decode what matters.</p>

<p><strong>The columns you need:</strong></p>

<table>
    <thead>
        <tr>
            <th>Column</th>
            <th>What it tells you</th>
            <th>How to use it</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>CPT / HCPCS code</strong></td>
            <td>The procedure code that identifies the specific service</td>
            <td>Match this to the CPT codes on your itemized bill or pre-authorization</td>
        </tr>
        <tr>
            <td><strong>Payer name</strong></td>
            <td>The insurance company (e.g., BlueCross, Aetna, UnitedHealthcare)</td>
            <td>Find your insurer to see what they&rsquo;ve negotiated</td>
        </tr>
        <tr>
            <td><strong>Plan name</strong></td>
            <td>The specific plan within that insurer (e.g., PPO, HMO, Choice Plus)</td>
            <td>Match to your exact plan &mdash; rates differ between PPO and HMO at the same insurer</td>
        </tr>
        <tr>
            <td><strong>Negotiated rate</strong></td>
            <td>What your insurer actually pays the hospital for this service</td>
            <td>Compare this to what you were billed &mdash; your bill should not exceed this amount before cost-sharing</td>
        </tr>
        <tr>
            <td><strong>Gross charge</strong></td>
            <td>The chargemaster list price</td>
            <td>The starting point &mdash; no one should pay this amount</td>
        </tr>
        <tr>
            <td><strong>Discounted cash price</strong></td>
            <td>What uninsured or self-pay patients can pay</td>
            <td>Your fallback price if paying out of pocket</td>
        </tr>
    </tbody>
</table>

<p><strong>A real example.</strong> Here is what you might find when you look up a common procedure in a hospital&rsquo;s price file:</p>

<div class="bill-example">
    <div class="bill-header">Sample: Price transparency file entry &mdash; MRI Lumbar Spine (CPT 72148)</div>
    <div class="line-item">
        <span>Gross charge (chargemaster list price)</span>
        <span>$3,200</span>
    </div>
    <div class="line-item">
        <span>Discounted cash price (self-pay)</span>
        <span>$1,280</span>
    </div>
    <div class="line-item">
        <span>BlueCross BlueShield PPO &mdash; negotiated rate</span>
        <span>$510</span>
    </div>
    <div class="line-item">
        <span>Aetna Choice POS &mdash; negotiated rate</span>
        <span>$485</span>
    </div>
    <div class="line-item">
        <span>UnitedHealthcare Choice Plus &mdash; negotiated rate</span>
        <span>$460</span>
    </div>
    <div class="line-item">
        <span>Cigna Open Access Plus &mdash; negotiated rate</span>
        <span>$530</span>
    </div>
    <div class="line-item flagged">
        <span>De-identified minimum negotiated rate</span>
        <span>$205</span>
    </div>
    <div class="line-item flagged">
        <span>De-identified maximum negotiated rate</span>
        <span>$580</span>
    </div>
    <div class="line-total">
        <span>Medicare rate (2026 OPPS) &mdash; reference benchmark</span>
        <span>$97</span>
    </div>
</div>

<p>Notice the spread: the gross charge ($3,200) is <strong>33x the Medicare rate</strong>. The best negotiated rate ($460) is still 4.7x Medicare, but it&rsquo;s 86% below the gross charge. The discounted cash price ($1,280) is 13x Medicare and 60% below gross &mdash; better than the list price, but still far higher than what any insurer pays. This is why knowing the negotiated rate matters: it reveals what the hospital actually accepts as full payment.</p>

{_calc_embed}

<h2 id="negotiate-with-data">5. Using price data in negotiations</h2>

<p>Price transparency data is your strongest negotiation tool because it comes from the hospital&rsquo;s own published file. Here is a real case study showing how one patient used it.</p>

<div class="case-study">
    <h3>Case study: Patient finds negotiated rate 60% lower than billed amount</h3>
    <p>A patient in Ohio received a bill for $4,800 after an outpatient knee arthroscopy (CPT 29881). Her insurer had processed the claim, and after applying her $2,500 deductible, the bill showed she owed $4,800 &mdash; the full gross charge minus nothing, because the claim appeared to have been processed at the chargemaster rate.</p>
    <p>She downloaded the hospital&rsquo;s price transparency file and found the payer-specific negotiated rate for her exact insurer and plan: <strong>$1,920</strong>. The gross charge was $4,800. The hospital&rsquo;s own file showed her insurer had negotiated to pay 60% less than what she was billed.</p>
    <p>She called the billing department and said: &ldquo;I&rsquo;ve reviewed your published price transparency file. The negotiated rate for [Insurer Name] [Plan Name] for CPT 29881 is listed as $1,920. My bill shows $4,800. Can you reprocess this claim at the correct negotiated rate?&rdquo;</p>
    <p>After the billing department verified the rate in their own file, they reprocessed the claim. Her revised patient responsibility &mdash; after her deductible and coinsurance &mdash; dropped from $4,800 to <strong>$1,440</strong>.</p>
    <p><strong>Savings: $3,360 by referencing the hospital&rsquo;s own posted data.</strong></p>
</div>

<p><strong>How to use price data in your own negotiation:</strong></p>

<ol>
    <li><strong>Get your itemized bill with CPT codes.</strong> You need the specific procedure codes to look up in the transparency file. If your bill only shows descriptions, call the billing department and request a fully itemized statement with CPT codes.</li>
    <li><strong>Look up each CPT code in the hospital&rsquo;s transparency file.</strong> Find your specific insurer and plan. Note the negotiated rate for each code.</li>
    <li><strong>Compare the negotiated rate to what you were billed.</strong> If your bill exceeds the negotiated rate, the claim may have been processed incorrectly. This is more common than most patients realize.</li>
    <li><strong>Look up the Medicare rate as a secondary benchmark.</strong> Even if the negotiated rate matches your bill, comparing it to the Medicare rate reveals how aggressive the hospital&rsquo;s pricing is. Use our <a href="/calculator">calculator</a> to look up Medicare rates instantly.</li>
    <li><strong>Call the billing department with specific numbers.</strong> Reference the exact rate from their file, the exact CPT code, and the exact payer and plan name. Vague requests get vague responses; specific data gets results.</li>
</ol>

<p><strong>If you&rsquo;re uninsured or self-pay:</strong> The transparency file gives you powerful leverage. You can see the discounted cash price (what the hospital says self-pay patients should pay), the de-identified minimum negotiated rate (the lowest amount any insurer pays), and the Medicare rate. Offer to pay somewhere between the minimum negotiated rate and the cash price. The hospital knows you can see what insurers pay &mdash; they have less room to justify charging you more.</p>

<div class="key-takeaway">
    <strong>Don&rsquo;t want to dig through spreadsheets?</strong> <a href="/scan">Upload your bill to BillKarma</a> and we&rsquo;ll do the comparison automatically &mdash; every line item checked against Medicare rates and hospital pricing data, with specific flags for overcharges.
</div>

<h2 id="compliance-reality">6. Compliance reality: who&rsquo;s still hiding prices</h2>

<p>Despite rising penalties, a significant share of hospitals remain non-compliant or only partially compliant. Understanding the compliance landscape helps you know what to expect when you go looking for price data.</p>

<table>
    <thead>
        <tr>
            <th>Compliance status</th>
            <th>Share of hospitals (2025&ndash;2026)</th>
            <th>What it means for patients</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Fully compliant</strong></td>
            <td>~70%</td>
            <td>File posted with all five data elements, payer-specific rates, and annual updates</td>
        </tr>
        <tr>
            <td><strong>Partially compliant</strong></td>
            <td>~15%</td>
            <td>File posted but missing payer-specific rates or using incomplete procedure lists</td>
        </tr>
        <tr>
            <td><strong>Non-compliant</strong></td>
            <td>~15%</td>
            <td>No file posted, file is a PDF, file is hidden behind login, or file contains placeholder data</td>
        </tr>
    </tbody>
</table>

<p><strong>Which hospitals are most likely to be non-compliant:</strong></p>

<ul>
    <li><strong>Small and rural hospitals</strong> with limited IT resources to generate and maintain the required files</li>
    <li><strong>For-profit hospital chains</strong> that have calculated the penalty ($2M/year) as a cost of doing business compared to the competitive risk of publishing their negotiated rates</li>
    <li><strong>Hospitals with unusually high markups</strong> that would face public scrutiny if their pricing became easily accessible</li>
</ul>

<p><strong>How to report non-compliance.</strong> CMS accepts complaints through its online portal. You do not need to be a patient at the hospital to file a complaint. Here is the process:</p>

<ol>
    <li>Visit the CMS Hospital Price Transparency page at <a href="https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency/hospitals" target="_blank" rel="noopener">cms.gov</a></li>
    <li>Click the link for reporting a hospital that is not in compliance</li>
    <li>Provide the hospital name, what you searched for, and what you found (or didn&rsquo;t find)</li>
    <li>CMS reviews complaints and issues warning letters or penalty notices as appropriate</li>
</ol>

<p>Filing a complaint takes five minutes and is the single most effective thing individual patients can do to improve compliance. Every complaint triggers a CMS review, and multiple complaints about the same hospital accelerate enforcement action.</p>

<div class="key-takeaway">
    <strong>Check your hospital&rsquo;s transparency status instantly.</strong> The <a href="/hospitals/">BillKarma hospital directory</a> shows whether we were able to parse a hospital&rsquo;s price file and what grade their pricing earned. An ungraded hospital is a red flag. See our <a href="/guides/hospital-billing-grades-explained">hospital billing grades guide</a> for details on how grades are calculated.
</div>

<h2 id="compare-hospitals">7. Comparing prices across hospitals</h2>

<p>Price transparency data makes it possible, for the first time, to comparison-shop for hospital services the same way you would for any other major purchase. For shoppable procedures &mdash; imaging, colonoscopies, joint replacements, outpatient surgeries &mdash; the price differences between hospitals in the same city can be enormous.</p>

<p><strong>How to comparison-shop using transparency data:</strong></p>

<ol>
    <li><strong>Get the CPT code for your procedure.</strong> Ask your doctor&rsquo;s office for the specific codes they plan to bill. For most scheduled procedures, the codes are known in advance.</li>
    <li><strong>Look up prices at multiple hospitals.</strong> Use the <a href="/hospitals/">BillKarma hospital directory</a> to compare prices for the same CPT code across nearby hospitals. Alternatively, download the transparency files from two or three hospitals and compare the negotiated rates for your insurer.</li>
    <li><strong>Compare the negotiated rate, not the gross charge.</strong> Gross charges are arbitrary and vary wildly. The negotiated rate for your specific insurer and plan is what actually determines your out-of-pocket cost.</li>
    <li><strong>Factor in facility fees.</strong> A hospital-based outpatient department may charge a facility fee on top of the procedure fee. An ambulatory surgery center (ASC) performing the same procedure may not. The transparency file should show both components.</li>
    <li><strong>Use the <a href="/shop">BillKarma price shopper</a></strong> to compare procedure prices across facilities near you in a single search, using data pulled directly from hospital transparency files and Medicare benchmarks.</li>
</ol>

<p><strong>Real price variation.</strong> To illustrate how dramatically prices differ, here is what three hospitals in the same metropolitan area charge for a diagnostic colonoscopy (CPT 45378), based on their published transparency files:</p>

<div class="bill-example">
    <div class="bill-header">Price comparison: Diagnostic colonoscopy (CPT 45378) &mdash; same metro area, same insurer</div>
    <div class="line-item">
        <span>Hospital A (academic medical center) &mdash; negotiated rate</span>
        <span>$1,840</span>
    </div>
    <div class="line-item">
        <span>Hospital B (community hospital) &mdash; negotiated rate</span>
        <span>$980</span>
    </div>
    <div class="line-item">
        <span>Hospital C (ambulatory surgery center) &mdash; negotiated rate</span>
        <span>$620</span>
    </div>
    <div class="line-item flagged">
        <span>Price difference: Hospital A vs. Hospital C</span>
        <span>$1,220 (197% more)</span>
    </div>
    <div class="line-total">
        <span>Medicare rate (2026) &mdash; reference benchmark</span>
        <span>$198</span>
    </div>
</div>

<p>If this patient had a $3,000 deductible and hadn&rsquo;t met it, the choice of facility alone would save $1,220 &mdash; for an identical procedure, same insurer, same doctor in some cases. This is the power of price transparency data: it turns hospital pricing from a black box into a comparison table.</p>

{_markup_embed}

<h2 id="insurer-transparency">8. What the insurer transparency rule adds</h2>

<p>The hospital price transparency rule is only half the picture. The <strong>Transparency in Coverage Rule</strong>, which applies to health insurers rather than hospitals, adds a second layer of pricing data that patients can use.</p>

<p><strong>What insurers must publish:</strong></p>

<ul>
    <li><strong>Machine-readable files of negotiated rates</strong> with every in-network provider, for every covered item and service (effective July 2022)</li>
    <li><strong>Machine-readable files of out-of-network allowed amounts</strong> (effective July 2022)</li>
    <li><strong>A patient-facing price comparison tool</strong> that shows personalized cost estimates for covered services, factoring in the patient&rsquo;s specific plan, deductible status, and cost-sharing (effective January 2023)</li>
</ul>

<p><strong>How to access your insurer&rsquo;s price data:</strong></p>

<ol>
    <li><strong>Log into your insurer&rsquo;s member portal.</strong> Look for a &ldquo;cost estimator,&rdquo; &ldquo;price transparency,&rdquo; or &ldquo;find care costs&rdquo; tool. Under the rule, every major insurer must offer this.</li>
    <li><strong>Search by CPT code or procedure name.</strong> The tool should show you your expected out-of-pocket cost at specific providers, accounting for your deductible and coinsurance.</li>
    <li><strong>Compare with the hospital&rsquo;s posted rate.</strong> If the insurer&rsquo;s tool shows a different rate than the hospital&rsquo;s file for the same procedure and plan, note the discrepancy. The lower number is your negotiation starting point.</li>
</ol>

<p><strong>Why both datasets matter.</strong> The hospital file shows what every insurer pays at that specific hospital. The insurer file shows what that insurer pays at every hospital. Used together, they give you a complete picture:</p>

<ul>
    <li>The hospital file tells you whether your insurer got a good deal at that facility compared to other payers</li>
    <li>The insurer file tells you whether that facility is expensive compared to other hospitals your insurer contracts with</li>
    <li>Medicare rates (via our <a href="/calculator">calculator</a>) provide an objective benchmark for whether any of these rates are reasonable</li>
</ul>

<p>For the best overview of your hospital&rsquo;s pricing patterns, check the <a href="/hospitals/">BillKarma hospital directory</a> &mdash; we combine hospital transparency data, Medicare benchmarks, and billing pattern analysis into a single profile page. For a deeper understanding of how hospital price transparency works at a structural level, see our companion guide: <a href="/guides/hospital-price-transparency">Hospital Price Transparency: Which Hospitals Post Their Prices &mdash; and Which Still Don&rsquo;t</a>.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the hospital price transparency rule?</h3>
        <p>The CMS Hospital Price Transparency Rule (45 CFR Part 180) requires every U.S. hospital to publish a machine-readable file listing all standard charges &mdash; including gross charges, discounted cash prices, payer-specific negotiated rates, and de-identified minimum and maximum rates. Hospitals must also display a consumer-friendly list of at least 300 shoppable services. Non-compliance can result in fines up to $2,007,500 per year.</p>
    </div>
    <div class="faq-item">
        <h3>How do I find my hospital&rsquo;s price transparency file?</h3>
        <p>Go to the hospital&rsquo;s website and search for &ldquo;price transparency,&rdquo; &ldquo;standard charges,&rdquo; or &ldquo;chargemaster.&rdquo; Try direct URLs like <code>hospital.com/pricing</code> or <code>hospital.com/price-transparency</code>. You can also use the <a href="/hospitals/">BillKarma hospital directory</a>, which parses these files and displays the data in a searchable format &mdash; no spreadsheet required.</p>
    </div>
    <div class="faq-item">
        <h3>Can I actually use hospital price data to lower my bill?</h3>
        <p>Yes. If the hospital&rsquo;s published negotiated rate for your insurer and plan is lower than what you were billed, you can call the billing department and reference the specific rate from their own file. Hospitals are required to honor their posted rates. Patients have saved thousands by catching discrepancies between billed amounts and published negotiated rates. <a href="/scan">Upload your bill to BillKarma</a> for an automated comparison.</p>
    </div>
    <div class="faq-item">
        <h3>What penalties do hospitals face for not publishing prices?</h3>
        <p>CMS can fine hospitals up to $5,500 per day for non-compliance &mdash; a maximum of $2,007,500 per year for hospitals with 30 or more beds. Smaller hospitals face up to $300 per day. CMS has escalated enforcement with warning letters, corrective action requests, and civil monetary penalty notices. Any member of the public can <a href="https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency/hospitals" target="_blank" rel="noopener">report a non-compliant hospital to CMS</a>.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Transparency in Coverage Rule and how is it different?</h3>
        <p>The Transparency in Coverage Rule applies to health insurers, not hospitals. It requires insurers to publish machine-readable files of their negotiated rates with all in-network providers and to offer a patient-facing price comparison tool. Together with the hospital rule, patients now have pricing data from both sides. Your insurer&rsquo;s member portal should have a cost estimator tool showing personalized estimates for any procedure at any in-network facility.</p>
    </div>
    <div class="faq-item">
        <h3>Are hospital price transparency files accurate?</h3>
        <p>Accuracy varies significantly. Some hospitals post complete, current data updated annually. Others post outdated files, omit payer-specific rates, or include placeholder data. Patient Rights Advocate&rsquo;s quarterly audits find wide variation in quality even among technically compliant hospitals. Cross-reference the hospital&rsquo;s data with your insurer&rsquo;s price tool and <a href="/calculator">Medicare rate benchmarks</a> to verify accuracy.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.ecfr.gov/current/title-45/part-180" target="_blank" rel="noopener">CMS: 45 CFR Part 180 &mdash; Hospital Price Transparency Final Rule (effective January 1, 2021)</a></li>
    <li><a href="https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency" target="_blank" rel="noopener">CMS: Hospital Price Transparency &mdash; Requirements, enforcement actions, and civil monetary penalty structure</a></li>
    <li><a href="https://www.cms.gov/healthplan-price-transparency" target="_blank" rel="noopener">CMS: Transparency in Coverage Rule &mdash; Insurer requirements for publishing negotiated rates and price comparison tools</a></li>
    <li><a href="https://www.patientrightsadvocate.org/compliance" target="_blank" rel="noopener">Patient Rights Advocate: Hospital Price Transparency Compliance Report (quarterly audits, 2022&ndash;2025)</a></li>
    <li><a href="https://www.rand.org/pubs/research_reports/RRA1144-2.html" target="_blank" rel="noopener">RAND Corporation: Prices Paid to Hospitals by Private Health Plans &mdash; Hospital Price Transparency Analysis</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2022.00732" target="_blank" rel="noopener">Health Affairs: Hospital Price Transparency Compliance and Data Quality Analysis (2022&ndash;2024)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/hospital-outpatient" target="_blank" rel="noopener">CMS: Outpatient Prospective Payment System (OPPS) &mdash; 2026 Final Rule (Medicare rate benchmarks)</a></li>
    <li><a href="https://www.federalregister.gov/documents/2020/11/12/2020-24591/transparency-in-coverage" target="_blank" rel="noopener">Federal Register: Transparency in Coverage Final Rule (85 FR 72158) &mdash; insurer machine-readable file and price comparison tool requirements</a></li>
</ul>
""",
})
