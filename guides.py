"""Guide articles served at /guides/{slug}.

Each guide is a dict with title, meta_description, published date, and
body (HTML string). Calculators are embedded inline via iframes.
"""

GUIDES = {}


def register(slug: str, guide: dict):
    GUIDES[slug] = {**guide, "slug": slug}


def get_guide(slug: str) -> dict | None:
    return GUIDES.get(slug)


def list_guides() -> list[dict]:
    return sorted(GUIDES.values(), key=lambda g: g.get("published", ""), reverse=True)


def _embed(mode="cost", cpt="", title="", subtitle="", height="380"):
    """Return an iframe snippet for embedding a calculator in article body."""
    params = f"mode={mode}"
    if cpt:
        params += f"&cpt={cpt}"
    if title:
        params += f"&title={title.replace('&', '%26')}"
    if subtitle:
        params += f"&subtitle={subtitle.replace('&', '%26')}"
    return (
        f'<iframe src="/calculator/embed?{params}" '
        f'width="100%" height="{height}" style="border:none; border-radius:18px;" '
        f'loading="lazy" title="{title or "Calculator"}"></iframe>'
    )


# ---------------------------------------------------------------------------
# Guide: How to Read Your Medical Bill
# ---------------------------------------------------------------------------

register("how-to-read-your-medical-bill", {
    "title": "How to Read Your Medical Bill and Spot Overcharges",
    "meta_description": "Learn how to decode every line on a medical bill. Understand CPT codes, Medicare rates, and how to identify billing errors that could save you hundreds.",
    "published": "2026-02-18",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "body": f"""
<p class="lead">Four out of five medical bills contain errors, according to industry estimates. But most patients pay without questioning because the bills are deliberately hard to read. This guide breaks down every section of a medical bill, explains the codes, and shows you exactly how to spot the most common overcharges.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#anatomy">Anatomy of a medical bill</a></li>
        <li><a href="#cpt-codes">Understanding CPT codes</a></li>
        <li><a href="#five-errors">The 5 most common billing errors</a></li>
        <li><a href="#fair-price">How to check if your price is fair</a></li>
        <li><a href="#what-to-do">What to do if you find an error</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="anatomy">1. Anatomy of a medical bill</h2>

<p>A standard hospital bill (also called a UB-04 or itemized statement) has these key sections:</p>

<ul>
    <li><strong>Patient information</strong> &mdash; Your name, account number, date of service, and insurance details.</li>
    <li><strong>Provider information</strong> &mdash; The hospital or clinic name, NPI (National Provider Identifier), and billing address.</li>
    <li><strong>Line items</strong> &mdash; Each service, procedure, or supply you were billed for. This is where errors hide. Each line typically shows a CPT/HCPCS code, a description, quantity, and the charged amount.</li>
    <li><strong>Insurance adjustments</strong> &mdash; What your insurance negotiated off the gross charge. This is the &ldquo;contractual adjustment.&rdquo;</li>
    <li><strong>Patient responsibility</strong> &mdash; Your deductible, copay, and coinsurance. This is what you actually owe.</li>
    <li><strong>Totals</strong> &mdash; Total charged, total adjustments, total insurance paid, and total patient balance.</li>
</ul>

<p><strong>Key rule:</strong> Always request an <em>itemized</em> bill, not just a summary statement. Summary statements lump charges together, making it impossible to audit individual services. Federal law gives you the right to an itemized bill&mdash;just call the billing department and ask.</p>

<h2 id="cpt-codes">2. Understanding CPT codes</h2>

<p>CPT (Current Procedural Terminology) codes are 5-digit numbers that identify every medical service. They&rsquo;re maintained by the AMA and used universally for billing. Here are the most common categories:</p>

<table>
    <thead>
        <tr><th>Code Range</th><th>Category</th><th>Examples</th></tr>
    </thead>
    <tbody>
        <tr><td>99201&ndash;99499</td><td>Evaluation &amp; Management</td><td>Office visits, ER visits, hospital stays</td></tr>
        <tr><td>70000&ndash;79999</td><td>Radiology</td><td>X-rays, CT scans, MRIs, ultrasounds</td></tr>
        <tr><td>80000&ndash;89999</td><td>Lab/Pathology</td><td>Blood tests, urinalysis, biopsies</td></tr>
        <tr><td>90000&ndash;99199</td><td>Medicine</td><td>Vaccines, infusions, ECGs</td></tr>
        <tr><td>10000&ndash;69999</td><td>Surgery</td><td>Any surgical procedure</td></tr>
    </tbody>
</table>

<p><strong>Why this matters:</strong> The CPT code determines what Medicare pays for a service. If the code on your bill is wrong (a higher-level code than what was performed), you&rsquo;re being overcharged. This is called <em>upcoding</em>.</p>

<p>Look up any CPT code from your bill to see what Medicare pays for it in your area:</p>

{_embed(mode="cost", title="Look up a CPT code from your bill", subtitle="See what Medicare pays in your area.")}

<h2 id="five-errors">3. The 5 most common billing errors</h2>

<h3>a) Price markup beyond reasonable rates</h3>

<p>Hospitals set their own prices (the &ldquo;chargemaster&rdquo;), which can be 3x to 10x what Medicare pays for the same service. While some markup is expected, charges above 3&ndash;5x Medicare rates are a red flag. A 2022 study in <em>Health Affairs</em> found that the average hospital charges <a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2020.00893" target="_blank" rel="noopener">3.4x their costs</a>.</p>

<h3>b) Duplicate charges</h3>

<p>The same service billed twice on the same date. This happens more often than you&rsquo;d think, especially with lab panels and medications. Check your bill for identical CPT codes on the same date&mdash;unless you genuinely received the service twice.</p>

<h3>c) Unbundling</h3>

<p>Some services are supposed to be billed as a single &ldquo;bundled&rdquo; code. For example, a Comprehensive Metabolic Panel (CPT 80053) includes all the tests in a Basic Metabolic Panel (CPT 80048). If both appear on your bill, you&rsquo;re being double-charged. The CMS maintains <a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-edits" target="_blank" rel="noopener">NCCI edits</a> that define which codes can&rsquo;t be billed together.</p>

<h3>d) Upcoding</h3>

<p>Being billed for a higher-complexity visit than what occurred. ER visits are coded from Level 1 (99281, minor) to Level 5 (99285, critical). The difference between a Level 3 and Level 5 ER visit can be over $1,000. If you went in for something straightforward, a Level 4 or 5 charge warrants a closer look.</p>

<h3>e) Incorrect quantities</h3>

<p>A supply or medication billed for more units than you received. Common with IV medications, where a partial vial might be billed as a full one.</p>

<h2 id="fair-price">4. How to check if your price is fair</h2>

<p>The simplest benchmark: <strong>compare your charge to the Medicare rate</strong>. Medicare rates are set by CMS (Centers for Medicare &amp; Medicaid Services) and represent what the federal government has determined a service is worth. While private insurance rates are higher, a charge more than 3x the Medicare rate is above typical market pricing.</p>

<p>Two data points to check:</p>

<ol>
    <li><strong>Medicare Physician Fee Schedule (PFS)</strong> &mdash; What Medicare pays the doctor. Varies by geographic locality.</li>
    <li><strong>Hospital Outpatient Prospective Payment (OPPS)</strong> &mdash; The facility fee Medicare pays the hospital. Combined with the PFS rate, this gives you the &ldquo;total Medicare allowable.&rdquo;</li>
</ol>

<p>Enter a procedure from your bill to see how your charge compares:</p>

{_embed(mode="markup", title="Is your charge too high?", subtitle="Enter the CPT code and amount from your bill.", height="420")}

<h2 id="what-to-do">5. What to do if you find an error</h2>

<ol>
    <li><strong>Request an itemized bill</strong> if you don&rsquo;t have one. Call the billing department and ask for a line-by-line statement with CPT codes.</li>
    <li><strong>Compare each line item</strong> against Medicare rates using the calculator above. Flag anything over 3x.</li>
    <li><strong>Check for duplicates</strong> &mdash; same CPT code, same date, same charge appearing twice.</li>
    <li><strong>Write a dispute letter</strong> citing the specific line items, CPT codes, and Medicare rates. Be factual, not emotional. Reference the specific errors you found.</li>
    <li><strong>Send it to the billing department</strong> via certified mail or the hospital&rsquo;s patient portal. Keep copies.</li>
    <li><strong>Follow up in 30 days</strong> if you don&rsquo;t hear back. Escalate to the patient advocate if billing doesn&rsquo;t respond.</li>
</ol>

<p>If this feels like a lot of work, you can <a href="/scan">upload your bill to BillKarma</a> and we&rsquo;ll do the entire audit automatically&mdash;comparing every line item against federal pricing data and generating a dispute letter for you in 30 seconds.</p>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient" target="_blank" rel="noopener">CMS Hospital Outpatient Prospective Payment System (OPPS)</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-edits" target="_blank" rel="noopener">CMS National Correct Coding Initiative (NCCI) Edits</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2020.00893" target="_blank" rel="noopener">Health Affairs: Hospital Charge-to-Cost Ratios (2022)</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">No Surprises Act &mdash; CMS</a></li>
    <li><a href="https://www.ama-assn.org/practice-management/cpt" target="_blank" rel="noopener">AMA CPT Code Information</a></li>
</ul>
""",
})
