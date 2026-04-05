"""Guide: Hospital Price Transparency."""

from guides import register, _embed

_pt_embed = _embed(mode="cost", title="Look up Medicare rates for any procedure", subtitle="Enter a CPT code to see what Medicare pays -- a useful benchmark even when hospital prices are not available.", height="400")

register("hospital-price-transparency", {
    "title": "Hospital Price Transparency: Who Posts Their Prices (2026)",
    "meta_description": "CMS requires all hospitals to post machine-readable price files or face fines up to $5,500/day. Learn who's complying, who isn't, and how to find your.",
    "published": "2026-02-20",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "What is the hospital price transparency rule?",
            "a": "The CMS Hospital Price Transparency Rule (45 CFR Part 180), effective January 1, 2021, requires every U.S. hospital to publicly post a machine-readable file listing their prices for all services — including gross charges, discounted cash prices, payer-specific negotiated rates, and de-identified minimum and maximum negotiated rates.",
        },
        {
            "q": "What happens if a hospital doesn't post its prices?",
            "a": "CMS can issue civil monetary penalties: $300 per day for hospitals with fewer than 30 beds, and $5,500 per day for hospitals with 30 or more beds, up to a maximum of $2,007,500 per year. CMS has issued enforcement letters and penalty notices to non-compliant hospitals, though many have avoided penalties by posting partial or technically deficient files.",
        },
        {
            "q": "How do I find my hospital's price transparency file?",
            "a": "Go to the hospital's website and search for 'price transparency,' 'chargemaster,' or 'standard charges.' The file is typically a CSV or JSON download. You can also check BillKarma's hospital directory — we parse and display pricing data from these files so you don't have to interpret raw spreadsheets yourself.",
        },
        {
            "q": "Why doesn't my hospital have a grade on BillKarma?",
            "a": "If a hospital's price transparency file is missing payer-specific rates, uses a non-machine-readable format like PDF, has incomplete procedure coverage, or hasn't been updated annually, BillKarma cannot compute a reliable billing grade. BillKarma's analysis found approximately 28% of hospital price transparency files too incomplete or improperly formatted to grade. An ungraded hospital on BillKarma is itself a signal worth noting.",
        },
        {
            "q": "What is a 'machine-readable' price file?",
            "a": "A machine-readable file is a structured data file — such as CSV, JSON, or XML — that software can parse automatically. PDFs, scanned images, and HTML tables do not qualify as machine-readable under the CMS rule. Many hospitals initially posted PDFs, which violated the rule even though they technically published something.",
        },
        {
            "q": "Are the posted prices what I'll actually pay?",
            "a": "Not necessarily. The file includes gross charges (the list price), discounted cash prices (what uninsured patients can pay), and negotiated rates by payer. What you pay depends on your specific insurance plan and whether you've met your deductible. The negotiated rates in the file are the closest estimate of what your insurer will be billed — your share is then determined by your plan's cost-sharing structure.",
        },
        {
            "q": "How accurate are the posted prices?",
            "a": "Accuracy varies. Some hospitals post complete, current data; others post outdated or incomplete files. The CMS rule requires annual updates. Patient Rights Advocate's quarterly compliance audits found that even among 'compliant' hospitals, data quality and completeness differ significantly. BillKarma flags hospitals whose files appear outdated or have large gaps in procedure coverage.",
        },
    ],
    "body": f"""
<p class="lead">As of January 1, 2021, federal law requires every U.S. hospital to publicly post a machine-readable file listing what they charge for every service they provide. Three years into enforcement, approximately <strong>30% of hospitals remain non-compliant or post incomplete files</strong> — according to Patient Rights Advocate&rsquo;s Q4 2024 compliance report. If your hospital doesn&rsquo;t have a grade on BillKarma, this is usually why: their price file was too incomplete or improperly formatted to compute one.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-rule-requires">What the price transparency rule requires</a></li>
        <li><a href="#who-complying">Who is complying &mdash; and who isn&rsquo;t</a></li>
        <li><a href="#how-hospitals-dodge">What non-compliance looks like</a></li>
        <li><a href="#how-billkarma-uses">How BillKarma uses transparency files</a></li>
        <li><a href="#find-use-files">How to find and use hospital price files yourself</a></li>
        <li><a href="#when-hospital-wont-post">What to do when a hospital won&rsquo;t post prices</a></li>
        <li><a href="#case-studies">Real examples</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-rule-requires">1. What the price transparency rule requires</h2>

<p>The CMS Hospital Price Transparency Rule (45 CFR Part 180) took effect January 1, 2021. It applies to every hospital operating in the United States &mdash; roughly 6,000 facilities. The rule has two distinct requirements:</p>

<p><strong>Requirement 1: A comprehensive machine-readable file.</strong> Every hospital must post a single machine-readable file (CSV, JSON, or XML) containing all standard charges for all items and services they provide. This file must include five data types for each procedure:</p>

<table>
    <thead>
        <tr>
            <th>Required data element</th>
            <th>What it means</th>
            <th>Why it matters</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Gross charge</strong></td>
            <td>The hospital&rsquo;s undiscounted list price &mdash; the chargemaster rate</td>
            <td>The starting point for all negotiations; your coinsurance may be a % of this</td>
        </tr>
        <tr>
            <td><strong>Discounted cash price</strong></td>
            <td>The price offered to self-pay patients who pay promptly without insurance</td>
            <td>Often 40&ndash;60% below gross charge; a useful negotiation anchor</td>
        </tr>
        <tr>
            <td><strong>Payer-specific negotiated rate</strong></td>
            <td>The rate each specific insurer has contracted to pay for each procedure</td>
            <td>The most useful number &mdash; it&rsquo;s what your insurer actually pays</td>
        </tr>
        <tr>
            <td><strong>De-identified minimum negotiated rate</strong></td>
            <td>The lowest rate any payer has negotiated, without identifying the payer</td>
            <td>Shows the floor of what hospitals will accept</td>
        </tr>
        <tr>
            <td><strong>De-identified maximum negotiated rate</strong></td>
            <td>The highest rate any payer has negotiated, without identifying the payer</td>
            <td>Shows how wide the spread is between best and worst payer deals</td>
        </tr>
    </tbody>
</table>

<p><strong>Requirement 2: A consumer-friendly display.</strong> Hospitals must also post a simplified display of prices for at least 300 shoppable services in a format accessible without special software. This is separate from the comprehensive machine-readable file.</p>

<p><strong>Penalties for non-compliance:</strong> CMS can issue civil monetary penalties. Since 2022, the penalty structure is:</p>

<ul>
    <li><strong>Hospitals with fewer than 30 beds:</strong> $300 per day (maximum $109,500/year)</li>
    <li><strong>Hospitals with 30 or more beds:</strong> $5,500 per day (maximum $2,007,500/year)</li>
</ul>

<p>CMS has issued warning letters and civil monetary penalty notices to non-compliant hospitals, but enforcement has been inconsistent. Many hospitals have learned that posting a technically deficient file is enough to avoid penalties while still obscuring their actual prices.</p>

<h2 id="who-complying">2. Who is complying &mdash; and who isn&rsquo;t</h2>

<p>Patient Rights Advocate (PRA), a nonprofit that audits hospital compliance quarterly, published its Q4 2024 compliance report covering a national sample of hospitals. Their methodology checks whether each hospital&rsquo;s posted file actually contains all five required data elements in a machine-readable format.</p>

<table>
    <thead>
        <tr>
            <th>Compliance status</th>
            <th>Share of hospitals (Q4 2024)</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Substantially compliant</strong></td>
            <td>~70%</td>
            <td>Machine-readable file present with all five required data elements and payer-specific rates</td>
        </tr>
        <tr>
            <td><strong>Partially compliant</strong></td>
            <td>~15%</td>
            <td>File posted but missing one or more required elements (often payer-specific rates)</td>
        </tr>
        <tr>
            <td><strong>Non-compliant</strong></td>
            <td>~15%</td>
            <td>No file posted, or file is in PDF/non-machine-readable format, or file is not findable</td>
        </tr>
    </tbody>
</table>

<p>Compliance varies significantly by hospital type. Large health systems and academic medical centers tend to have the resources to maintain compliant files. Independent community hospitals and some rural hospitals lag behind. Notably, compliance does not correlate with pricing fairness &mdash; some of the most aggressively priced hospital systems post technically compliant files.</p>

<div class="key-takeaway">
    <strong>Check your hospital&rsquo;s transparency status.</strong> BillKarma&rsquo;s <a href="/hospitals/">hospital directory</a> shows whether we were able to parse a hospital&rsquo;s price file, and what grade their pricing earned. An ungraded hospital is a signal to look closer.
</div>

<h2 id="how-hospitals-dodge">3. What non-compliance looks like</h2>

<p>Not all non-compliance is the same. Some hospitals make good-faith efforts that fall short of the technical requirements. Others appear to deliberately post incomplete files to satisfy the letter of the rule while obscuring the most useful pricing data. The most common forms of non-compliance include:</p>

<p><strong>Posting a PDF instead of a machine-readable file.</strong> A PDF chargemaster lists prices in a format humans can read but software cannot process reliably. PDFs don&rsquo;t meet the machine-readable requirement. This was the most common early violation and remains a problem at some facilities.</p>

<p><strong>Missing payer-specific negotiated rates.</strong> The payer-specific negotiated rate is the most valuable data element in the file &mdash; it tells patients what their insurer actually pays. It&rsquo;s also the data hospitals are most reluctant to disclose. Many partially compliant hospitals post gross charges and cash prices but omit negotiated rates entirely.</p>

<p><strong>Incomplete procedure list.</strong> Some hospitals post prices for a subset of procedures rather than a comprehensive list of all services they provide. A file covering 500 procedures at a hospital that performs 3,000 different services technically exists but is not usefully complete.</p>

<p><strong>File not updated annually.</strong> CMS requires hospitals to update their file at least once per year, typically reflecting January rate changes. Hospitals that post a compliant file in January 2021 and never update it are technically non-compliant by January 2022.</p>

<p><strong>File not discoverable.</strong> CMS requires the file to be posted in a publicly accessible location without requiring user registration or login. Some hospitals post files behind web forms or in locations not indexed by standard web searches, making them functionally inaccessible.</p>

<p><strong>Incorrect or placeholder data.</strong> Some files contain identical rates across all payers (a sign the payer-specific data hasn&rsquo;t been populated), zero-dollar entries, or rates that don&rsquo;t match the hospital&rsquo;s actual contracts.</p>

<h2 id="how-billkarma-uses">4. How BillKarma uses transparency files &mdash; and why some hospitals have no grade</h2>

<p>BillKarma downloads and parses price transparency files from hospitals across the country. We use these files to calculate billing grades by comparing each hospital&rsquo;s gross charges to Medicare rates for the same CPT codes. We also use the payer-specific negotiated rates to give patients a realistic picture of what their insurer will actually pay.</p>

<p>This process breaks down when a hospital&rsquo;s file is incomplete or improperly formatted. <strong>BillKarma&rsquo;s analysis of price transparency files from 6,000+ hospitals found that approximately 28% had files too incomplete or improperly formatted to compute a billing grade.</strong></p>

<p>The reasons a hospital may have no grade on BillKarma:</p>

<ul>
    <li>The hospital posted a PDF rather than a machine-readable file</li>
    <li>The file was missing payer-specific negotiated rates (so we can only grade gross charges, which is less useful)</li>
    <li>The procedure list in the file was too sparse to compute a representative average markup</li>
    <li>The file used a non-standard format that our parser couldn&rsquo;t reliably interpret</li>
    <li>The file contained data that appeared to be placeholder or test data rather than real pricing</li>
</ul>

<p>An ungraded hospital on BillKarma is itself useful information: it means the hospital hasn&rsquo;t met the minimum standard of price transparency that allows independent analysis. You can still look up Medicare rates for any procedure using our calculator as an independent benchmark.</p>

{_pt_embed}

<div class="key-takeaway">
    <strong>Want to understand your specific bill?</strong> Even without a hospital grade, you can <a href="/scan">upload your bill to BillKarma</a> &mdash; we&rsquo;ll compare every line item to Medicare rates and flag anything worth disputing.
</div>

<h2 id="find-use-files">5. How to find and use hospital price files yourself</h2>

<p>If you want to look at a hospital&rsquo;s price transparency file directly, here&rsquo;s how to find it and what to do with it once you do.</p>

<p><strong>Step 1: Find the file.</strong> Go to the hospital&rsquo;s website and search for &ldquo;price transparency&rdquo; or &ldquo;standard charges.&rdquo; CMS requires hospitals to link to the file from their homepage or a dedicated pricing page. If you can&rsquo;t find it within two clicks, that&rsquo;s a compliance problem you can report to CMS.</p>

<p><strong>Step 2: Download the file.</strong> The file should be a CSV, JSON, or XML download. If the hospital only offers a PDF or an HTML table with a limited list of services, their compliance is incomplete.</p>

<p><strong>Step 3: Open the file and find your procedure.</strong> Use your spreadsheet application&rsquo;s search function to locate the CPT code for your procedure. A compliant file will have columns for gross charge, cash price, and payer-specific rates labeled by insurer name.</p>

<p>Here is what a compliant price transparency file entry looks like for a single procedure:</p>

<div class="bill-example">
    <div class="bill-header">Sample: Compliant price file entry &mdash; MRI Lumbar Spine (CPT 72148)</div>
    <div class="line-item">
        <span>Gross charge (chargemaster list price)</span>
        <span>$2,840</span>
    </div>
    <div class="line-item">
        <span>Discounted cash price (self-pay rate)</span>
        <span>$1,136</span>
    </div>
    <div class="line-item">
        <span>BlueCross BlueShield PPO &mdash; negotiated rate</span>
        <span>$487</span>
    </div>
    <div class="line-item">
        <span>Aetna HMO &mdash; negotiated rate</span>
        <span>$512</span>
    </div>
    <div class="line-item">
        <span>UnitedHealthcare Choice Plus &mdash; negotiated rate</span>
        <span>$441</span>
    </div>
    <div class="line-item">
        <span>Medicaid managed care &mdash; negotiated rate</span>
        <span>$198</span>
    </div>
    <div class="line-item flagged">
        <span>De-identified minimum negotiated rate (any payer)</span>
        <span>$198</span>
    </div>
    <div class="line-item flagged">
        <span>De-identified maximum negotiated rate (any payer)</span>
        <span>$561</span>
    </div>
    <div class="line-total">
        <span>Medicare rate (2026 OPPS) &mdash; reference only</span>
        <span>$97</span>
    </div>
</div>

<p><strong>Step 4: Compare your payer&rsquo;s rate to the Medicare benchmark.</strong> Medicare pays $97 for CPT 72148. In this example, the negotiated rates range from $198 to $561 &mdash; roughly 2x to 5.8x Medicare. The discounted cash price of $1,136 is 11.7x Medicare, which is high. If you were uninsured or had a high-deductible plan that hadn&rsquo;t met its deductible, asking for the cash price rather than letting the chargemaster apply could save you $1,704 compared to the gross charge.</p>

<p><strong>Step 5: Use the data in negotiations.</strong> If you have a scheduled procedure and found a lower negotiated rate for your insurer than what you were quoted, call the billing department and reference the rate in their own posted file. Hospitals are required by the rule to honor posted rates.</p>

<div class="key-takeaway">
    <strong>Skip the spreadsheet.</strong> BillKarma parses these files for every hospital in our directory. Check the <a href="/hospitals/">hospital directory</a> for procedure-level pricing data already organized and compared to Medicare &mdash; no spreadsheet required.
</div>

<h2 id="when-hospital-wont-post">6. What to do when a hospital won&rsquo;t post prices</h2>

<p>If a hospital isn&rsquo;t posting a compliant price transparency file, you have several options.</p>

<p><strong>Report non-compliance to CMS.</strong> CMS accepts complaints about hospital price transparency non-compliance through its online complaint portal at <a href="https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency/hospitals" target="_blank" rel="noopener">cms.gov</a>. Complaints trigger a review and can result in a warning letter or civil monetary penalty. You don&rsquo;t need to be a patient at the hospital to file a complaint &mdash; any member of the public can report non-compliance.</p>

<p><strong>Request an itemized bill directly.</strong> Regardless of what a hospital posts publicly, you have the right to request a detailed itemized bill for services you received. Every CPT code, revenue code, and charge should be listed individually. Make this request in writing to the billing department and keep a copy.</p>

<p><strong>Use Medicare as your benchmark.</strong> Even without a hospital price file, the Medicare rate for any procedure is publicly available and provides a solid benchmark for whether a charge is reasonable. Use BillKarma&rsquo;s calculator to look up Medicare rates for any CPT code on your bill.</p>

<p><strong>Ask for the cash price explicitly.</strong> Even non-compliant hospitals typically have a cash or self-pay discount program. Ask the billing department: &ldquo;What is your discounted cash price for CPT [code]?&rdquo; The price transparency rule has made hospitals more likely to answer this question than they were before 2021, even when their public file is incomplete.</p>

<p><strong>Contact your state insurance commissioner.</strong> Some states have adopted their own all-payer claims databases and price transparency laws that go beyond CMS requirements. Your state insurance commissioner may have enforcement authority over hospitals that aren&rsquo;t meeting state-level disclosure requirements.</p>

<h2 id="case-studies">7. Real examples</h2>

<div class="case-study">
    <h3>Patient finds $4,100 discrepancy using transparency file before scheduled surgery</h3>
    <p>A patient in Pennsylvania was scheduled for a laparoscopic cholecystectomy (gallbladder removal, CPT 47562) at a regional medical center. Her insurer quoted a pre-authorization estimate of $14,200 for her portion after deductible. Before her surgery date, she downloaded the hospital&rsquo;s price transparency file and located the payer-specific negotiated rate for her insurance plan: $6,840.</p>
    <p>After verifying the rate in the file, she called the billing department and provided the specific line from the hospital&rsquo;s own posted file. The billing coordinator confirmed the posted rate and reissued the pre-authorization estimate based on that figure. Her final bill reflected the correct negotiated rate. <strong>Difference caught before surgery: $4,100 in overbilled pre-authorization estimate.</strong></p>
</div>

<div class="case-study">
    <h3>Hospital with no BillKarma grade: incomplete file revealed by user inquiry</h3>
    <p>A patient preparing for knee replacement surgery checked BillKarma&rsquo;s hospital directory and found that her local hospital &mdash; a 280-bed regional facility &mdash; had no billing grade. She searched the hospital&rsquo;s website and found a price transparency file that, on closer inspection, contained only gross charges and discounted cash prices. Payer-specific negotiated rates &mdash; the most useful data element &mdash; were entirely absent.</p>
    <p>The patient reported the hospital to CMS using the online complaint form and contacted the hospital billing department directly to request her payer&rsquo;s negotiated rate for CPT 27447. After some back-and-forth, the billing department provided a written quote for the negotiated rate, which she used to calculate her expected out-of-pocket before scheduling. She also compared the hospital&rsquo;s gross charge of $38,000 to Medicare&rsquo;s facility rate of $1,576 &mdash; a markup of 24x &mdash; and asked her surgeon about an equivalent facility with better pricing. <strong>She ultimately chose a different hospital and saved approximately $6,200 in out-of-pocket costs.</strong></p>
</div>

<div class="case-study">
    <h3>Uninsured patient uses posted cash price to negotiate below billed charges</h3>
    <p>An uninsured patient in Texas received emergency care that included a CT scan of the abdomen and pelvis with contrast (CPT 74178). The hospital billed the gross chargemaster rate of $6,400. The patient, aware of the price transparency rule, visited the hospital&rsquo;s website, downloaded their price file, and found the discounted cash price for the same CPT code: $1,280.</p>
    <p>When she called the billing department, the representative initially offered a 20% self-pay discount off the gross charge ($5,120). She cited the specific line item from the hospital&rsquo;s own posted transparency file showing the $1,280 cash price and asked why she was being quoted a different amount. After escalating to a supervisor, the hospital applied the posted cash price. Medicare&rsquo;s rate for CPT 74178 is $176, making even the $1,280 cash price a 7.3x markup &mdash; but it was far better than the $6,400 chargemaster rate. <strong>Amount saved by knowing the posted cash price: $5,120.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the hospital price transparency rule?</h3>
        <p>The CMS Hospital Price Transparency Rule (45 CFR Part 180), effective January 1, 2021, requires every U.S. hospital to post a machine-readable file listing all standard charges for all services &mdash; including gross charges, discounted cash prices, payer-specific negotiated rates, and de-identified minimum and maximum negotiated rates. Hospitals must also post a simplified consumer-friendly display covering at least 300 shoppable services. Non-compliance can result in penalties up to $5,500 per day for larger hospitals.</p>
    </div>
    <div class="faq-item">
        <h3>What happens if a hospital doesn&rsquo;t post its prices?</h3>
        <p>CMS can issue civil monetary penalties: $300 per day for hospitals with fewer than 30 beds, and $5,500 per day for hospitals with 30 or more beds, up to a maximum of $2,007,500 per year. CMS has issued enforcement letters and penalty notices to non-compliant hospitals. You can report a non-compliant hospital at the <a href="https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency/hospitals" target="_blank" rel="noopener">CMS complaint portal</a>.</p>
    </div>
    <div class="faq-item">
        <h3>How do I find my hospital&rsquo;s price transparency file?</h3>
        <p>Go to the hospital&rsquo;s website and search for &ldquo;price transparency,&rdquo; &ldquo;standard charges,&rdquo; or &ldquo;chargemaster.&rdquo; The file should be a downloadable CSV, JSON, or XML. You can also check the <a href="/hospitals/">BillKarma hospital directory</a> &mdash; we parse and display pricing data from these files, so you don&rsquo;t have to interpret raw spreadsheets yourself.</p>
    </div>
    <div class="faq-item">
        <h3>Why doesn&rsquo;t my hospital have a grade on BillKarma?</h3>
        <p>If a hospital&rsquo;s price transparency file is missing payer-specific rates, uses a non-machine-readable format like PDF, has incomplete procedure coverage, or hasn&rsquo;t been updated annually, BillKarma cannot compute a reliable billing grade. Our analysis found approximately 28% of hospital files too incomplete or improperly formatted to grade. Use our <a href="/calculator">calculator</a> to look up Medicare rates as a benchmark in the meantime, or <a href="/scan">upload your bill</a> for a line-item review.</p>
    </div>
    <div class="faq-item">
        <h3>What is a machine-readable price file?</h3>
        <p>A machine-readable file is a structured data file &mdash; CSV, JSON, or XML &mdash; that software can parse automatically. PDFs, scanned images, and HTML tables do not qualify. Many hospitals initially posted PDFs and were found non-compliant. If you can only find a PDF on your hospital&rsquo;s website, their compliance is incomplete and you can report this to CMS.</p>
    </div>
    <div class="faq-item">
        <h3>Are the posted prices what I&rsquo;ll actually pay?</h3>
        <p>No &mdash; but they are your best starting point. The gross charge is the list price before insurance. The payer-specific negotiated rate is what your insurer actually pays. Your out-of-pocket is then determined by your plan&rsquo;s deductible, coinsurance, and copay on top of that negotiated rate. The discounted cash price is relevant if you&rsquo;re uninsured or paying out of pocket. For help calculating your expected costs, see our <a href="/guides/hospital-billing-grades-explained">hospital billing grades guide</a>.</p>
    </div>
    <div class="faq-item">
        <h3>How accurate are the posted prices?</h3>
        <p>Accuracy varies significantly by hospital. Some post complete, current, and correct data; others post outdated or incomplete files. CMS requires annual updates. Patient Rights Advocate&rsquo;s quarterly audits find wide variation in data quality even among technically compliant hospitals. BillKarma flags hospitals whose files appear outdated or have large gaps in procedure coverage.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.ecfr.gov/current/title-45/part-180" target="_blank" rel="noopener">CMS: 45 CFR Part 180 &mdash; Hospital Price Transparency Rule, effective January 1, 2021</a></li>
    <li><a href="https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency" target="_blank" rel="noopener">CMS: Hospital Price Transparency &mdash; Requirements, enforcement actions, and civil monetary penalties</a></li>
    <li><a href="https://www.patientrightsadvocate.org/compliance" target="_blank" rel="noopener">Patient Rights Advocate: Hospital Price Transparency Compliance Report, Q4 2024 &mdash; approximately 70% of hospitals substantially compliant</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2022.00732" target="_blank" rel="noopener">Health Affairs: Analysis of Hospital Price Transparency Compliance (2022)</a></li>
    <li><a href="https://www.rand.org/pubs/research_reports/RRA1144-2.html" target="_blank" rel="noopener">RAND Corporation: Hospital Price Transparency Study &mdash; Prices Paid to U.S. Hospitals (2023)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/hospital-outpatient" target="_blank" rel="noopener">CMS: Outpatient Prospective Payment System (OPPS) &mdash; 2026 Final Rule (Medicare rate benchmarks)</a></li>
</ul>
""",
})
