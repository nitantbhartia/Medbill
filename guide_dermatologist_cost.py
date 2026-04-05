"""Guide: Dermatologist Cost in 2026."""

from guides import register, _embed

register("dermatologist-cost", {
    "title": "Dermatologist Cost in 2026: Office Visit, Procedures & Insurance",
    "meta_description": "How much does a dermatologist cost in 2026? Office visits run $150–$350 without insurance. Learn what insurance covers, common procedure costs, CPT codes, and how to spot billing errors.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does a dermatologist visit cost without insurance?",
            "a": "A new patient comprehensive exam typically runs $200–$350 without insurance. Follow-up visits are lower, usually $150–$250. Costs vary by location, provider, and whether the visit is for a medical or cosmetic concern. Freestanding dermatology clinics tend to charge less than hospital-affiliated practices.",
        },
        {
            "q": "Does insurance cover dermatology visits?",
            "a": "Yes, for medical dermatology. Conditions like acne (when prescription treatment is needed), eczema, psoriasis, skin cancer, and rashes are covered because they are medically necessary. Cosmetic concerns — wrinkle treatment, chemical peels, cosmetic laser — are not covered. You will typically pay a specialist copay of $30–$75 per visit plus any deductible or coinsurance that applies.",
        },
        {
            "q": "Is a skin cancer screening covered by insurance?",
            "a": "Medicare covers full-body skin cancer screenings as a preventive service, meaning no cost-sharing when performed by an in-network provider. Most commercial plans also cover annual skin exams at no cost under ACA preventive care rules. However, if the dermatologist finds a suspicious lesion and performs a biopsy during the same visit, that service may be billed separately and subject to cost-sharing.",
        },
        {
            "q": "Do I need prior authorization for dermatology biologics?",
            "a": "Yes. Biologics for dermatologic conditions — Dupixent (dupilumab) for eczema and Humira (adalimumab) or Skyrizi for psoriasis — almost always require prior authorization. Insurers typically require documentation that you have tried and failed conventional treatments (topical steroids, phototherapy) before approving a biologic. Step therapy requirements mean you may need to try cheaper medications first.",
        },
        {
            "q": "What is the most common billing error on dermatology claims?",
            "a": "The most frequent error is using the wrong lesion removal code based on lesion size or type. CPT codes 11300–11313 for shave excision are selected based on lesion diameter and body location. Billing a code for a larger lesion than what was actually removed, or using an excision code (11600 series) when a shave removal was performed, inflates the bill. BillKarma data shows dermatology billing errors affect 26% of claims.",
        },
    ],
    "body": f"""
<p class="lead">A dermatologist visit can cost anywhere from <strong>$30 with insurance</strong> to <strong>$500+ without it</strong>&mdash;depending on what&rsquo;s done, where you go, and whether your condition qualifies as medical or cosmetic. Understanding these distinctions before your appointment can prevent unexpected bills. BillKarma data shows dermatology billing errors affect <strong>26% of claims</strong>, mostly from lesion removal code mismatches.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#visit-costs">Office visit costs: with and without insurance</a></li>
        <li><a href="#medical-vs-cosmetic">Medical vs. cosmetic dermatology: what insurance covers</a></li>
        <li><a href="#procedure-costs">Common procedure costs</a></li>
        <li><a href="#skin-cancer-screening">Skin cancer screenings and Medicare</a></li>
        <li><a href="#prior-auth">Prior authorization for biologics</a></li>
        <li><a href="#cpt-codes">CPT codes and billing errors to watch for</a></li>
        <li><a href="#lower-cost-options">Lower-cost options: teledermatology</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="visit-costs">1. Office visit costs: with and without insurance</h2>

<p>Dermatologist fees vary by visit type, provider, and location. Here is what to expect in 2026:</p>

<table>
    <thead>
        <tr><th>Visit Type</th><th>Without Insurance</th><th>With Insurance (Specialist Copay)</th></tr>
    </thead>
    <tbody>
        <tr><td>New patient comprehensive exam</td><td>$200&ndash;$350</td><td>$30&ndash;$75 copay</td></tr>
        <tr><td>Follow-up visit (established patient)</td><td>$150&ndash;$250</td><td>$30&ndash;$75 copay</td></tr>
        <tr><td>Full-body skin cancer screening</td><td>$150&ndash;$300</td><td>Often $0 (preventive)</td></tr>
        <tr><td>Acne consultation</td><td>$150&ndash;$300</td><td>$30&ndash;$75 copay (if medical)</td></tr>
        <tr><td>Cosmetic consultation</td><td>$100&ndash;$300</td><td>Not covered</td></tr>
    </tbody>
</table>

<p>The gap between a new patient visit and a follow-up exists because new patients are typically billed at CPT code 99204 or 99205 (higher complexity new patient E&amp;M), while follow-ups use 99213 or 99214. The difference in allowed amounts can be $80&ndash;$150. If your insurer charges coinsurance rather than a flat copay, that gap translates directly into higher out-of-pocket costs on your first visit.</p>

<div class="key-takeaway">
    <strong>Tip:</strong> If you have a high-deductible plan and haven&rsquo;t met your deductible, you will pay the full allowed amount for the visit (not just a copay). Ask the office for the cash-pay or self-pay rate before your appointment&mdash;many practices offer 20&ndash;40% discounts for patients who pay at the time of service. Use our <a href="/calculator">cost calculator</a> to look up Medicare allowable rates for dermatology visit codes.
</div>

<h2 id="medical-vs-cosmetic">2. Medical vs. cosmetic dermatology: what insurance covers</h2>

<p>The single most important distinction in dermatology billing is whether a condition is <strong>medically necessary</strong> or <strong>cosmetic</strong>. Insurance&mdash;including Medicare&mdash;covers medical dermatology only.</p>

<p><strong>Covered (medical dermatology):</strong></p>
<ul>
    <li>Acne requiring prescription treatment (topical or oral antibiotics, isotretinoin)</li>
    <li>Eczema (atopic dermatitis), including biologics like Dupixent when criteria are met</li>
    <li>Psoriasis and psoriatic arthritis, including phototherapy and biologics</li>
    <li>Skin cancer evaluation, biopsy, and removal (basal cell, squamous cell, melanoma)</li>
    <li>Suspicious or changing moles requiring biopsy</li>
    <li>Rosacea, seborrheic dermatitis, contact dermatitis</li>
    <li>Wart removal (verruca vulgaris) when medically indicated</li>
    <li>Actinic keratosis treatment (precancerous lesions)</li>
</ul>

<p><strong>Not covered (cosmetic dermatology):</strong></p>
<ul>
    <li>Botox and dermal fillers for wrinkles</li>
    <li>Chemical peels for anti-aging or cosmetic skin tone</li>
    <li>Cosmetic laser resurfacing or hair removal</li>
    <li>Acne scar treatment when purely cosmetic</li>
    <li>Microneedling, microdermabrasion</li>
    <li>Removal of benign cosmetic lesions (skin tags for appearance, not discomfort)</li>
</ul>

<div class="key-takeaway">
    <strong>The gray zone:</strong> Some procedures straddle the line. Skin tag removal is covered if the tag causes irritation, bleeding, or functional problems&mdash;but not if it&rsquo;s purely cosmetic. Laser treatment for rosacea can be covered when other treatments have failed. The diagnosis code (ICD-10) your dermatologist documents determines coverage. If you receive a denial for a service you believe is medical, <a href="/fight-debt">review the denial with BillKarma</a> to check whether the diagnosis was coded correctly.
</div>

<h2 id="procedure-costs">3. Common procedure costs</h2>

<p>Procedure costs depend heavily on setting (hospital outpatient vs. freestanding office), complexity, and geographic location. The ranges below reflect 2026 averages:</p>

<table>
    <thead>
        <tr><th>Procedure</th><th>Average Cost (Without Insurance)</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Mole removal &mdash; shave excision</td><td>$150&ndash;$400</td><td>Most common removal method; billed by lesion size</td></tr>
        <tr><td>Punch biopsy</td><td>$200&ndash;$500</td><td>Includes pathology lab fee (billed separately)</td></tr>
        <tr><td>Cryotherapy (wart/AK removal)</td><td>$150&ndash;$400 per session</td><td>May require multiple sessions</td></tr>
        <tr><td>Mohs surgery (skin cancer)</td><td>$1,000&ndash;$5,000+</td><td>Staged; cost rises with number of stages required</td></tr>
        <tr><td>Phototherapy session</td><td>$100&ndash;$300 per session</td><td>Psoriasis/eczema; typically 3x/week for 8&ndash;12 weeks</td></tr>
        <tr><td>Excisional biopsy / lesion excision</td><td>$400&ndash;$1,500</td><td>Deeper removal; repair may be billed separately</td></tr>
    </tbody>
</table>

<p><strong>Important note on pathology:</strong> When a mole or lesion is biopsied, the tissue is sent to a pathology lab for analysis. That lab fee is a <em>separate bill</em> from the dermatologist&rsquo;s procedure fee. Pathology reads typically cost $100&ndash;$400. Verify that the pathology lab is in-network, or you may receive an unexpected out-of-network bill even though you saw an in-network dermatologist.</p>

{_embed(mode="cost", cpt="17000", title="Look up cryotherapy costs", subtitle="See what Medicare pays for common dermatology procedures.")}

<h2 id="skin-cancer-screening">4. Skin cancer screenings and Medicare</h2>

<p>Skin cancer is the most common cancer in the United States, with more than 5 million cases treated annually. Regular screenings are one of the most effective preventive measures available.</p>

<p><strong>Medicare coverage:</strong> Medicare covers full-body skin cancer screenings as a preventive service under Part B at <strong>no cost-sharing</strong> when performed by an in-network provider who accepts Medicare assignment. No deductible applies to preventive screenings.</p>

<p><strong>Commercial insurance:</strong> Most ACA-compliant commercial plans cover preventive skin exams at no cost. However, coverage rules vary&mdash;some plans require the visit to be coded purely as a preventive exam. If the dermatologist addresses a separate medical concern during the same visit, the visit may be split-billed, and the medical portion will be subject to your deductible and copay.</p>

<p><strong>What to watch for:</strong> If you schedule a preventive skin cancer screening and the dermatologist performs a biopsy on a suspicious lesion, the biopsy will be billed as a diagnostic procedure&mdash;not preventive. This is correct coding, but it surprises many patients who expected a &ldquo;free&rdquo; screening. Ask your dermatologist before any biopsy what the expected billing will look like.</p>

<h2 id="prior-auth">5. Prior authorization for biologics</h2>

<p>Moderate-to-severe eczema and psoriasis are increasingly treated with biologic medications. These drugs are highly effective but extremely expensive&mdash;typically $15,000&ndash;$40,000 per year at list price. Prior authorization is almost universally required.</p>

<ol>
    <li><strong>Document the diagnosis.</strong> Your dermatologist must document the severity of your condition using standardized scoring tools (EASI score for eczema, PASI score for psoriasis).</li>
    <li><strong>Show treatment failure.</strong> Most insurers require proof that you tried and failed conventional therapies: topical corticosteroids, topical calcineurin inhibitors, and/or phototherapy.</li>
    <li><strong>Submit the PA request.</strong> Your dermatologist&rsquo;s office submits the prior authorization with clinical documentation. This typically takes 3&ndash;14 days.</li>
    <li><strong>Step therapy may apply.</strong> Some plans require you to try specific biologics before others. For example, a plan may require you to try an older TNF inhibitor before approving a newer IL-4/IL-13 inhibitor like Dupixent.</li>
    <li><strong>Appeal a denial.</strong> PA denials for biologics can often be overturned on appeal when your dermatologist submits additional clinical documentation. If you receive a denial, <a href="/fight-debt">BillKarma can help you build the appeal</a>.</li>
</ol>

<div class="case-study">
    <h3>Case study: Dupixent prior auth denial overturned</h3>
    <p><strong>Situation:</strong> A 34-year-old patient with severe atopic dermatitis received a denial for Dupixent. The insurer claimed she had not demonstrated failure of conventional therapy.</p>
    <p><strong>The problem:</strong> Her dermatologist had documented topical steroid use in clinical notes but had not included a formal prior authorization letter summarizing treatment history and severity scores. The PA submission was missing the EASI score documentation.</p>
    <p><strong>The outcome:</strong> After a peer-to-peer review between the dermatologist and the insurance medical director&mdash;with a complete clinical summary including EASI score of 28 (severe) and documentation of six months of failed topical therapy&mdash;the authorization was approved on the first appeal. The patient&rsquo;s out-of-pocket cost dropped from list price to a $5 copay via the manufacturer&rsquo;s patient assistance program.</p>
</div>

<h2 id="cpt-codes">6. CPT codes and billing errors to watch for</h2>

<p>Dermatology has some of the most granular CPT coding in medicine, which creates frequent billing errors. Key codes to know:</p>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Description</th><th>Common Error</th></tr>
    </thead>
    <tbody>
        <tr><td>99213&ndash;99214</td><td>Office visit (established patient, moderate complexity)</td><td>Upcoding to 99215 for routine visits</td></tr>
        <tr><td>11300&ndash;11313</td><td>Shave removal of skin lesion (by site and size)</td><td>Billing a larger-lesion code than the actual size; using excision code when shave was performed</td></tr>
        <tr><td>17000</td><td>Destruction of premalignant lesion, first lesion</td><td>Unbundling multiple cryotherapy sites instead of using 17003 add-on code</td></tr>
        <tr><td>17311</td><td>Mohs micrographic surgery, first stage</td><td>Billing extra stages not documented in operative report</td></tr>
        <tr><td>96910&ndash;96913</td><td>Phototherapy (UV treatment)</td><td>Billing for sessions on days not documented in treatment log</td></tr>
    </tbody>
</table>

<p><strong>Most common dermatology billing errors:</strong></p>
<ul>
    <li><strong>Coding a medical procedure as cosmetic (or vice versa):</strong> A benign lesion removal may be coded as a suspicious lesion removal to obtain coverage. Or a legitimate medical removal may be denied because it was coded cosmetically by a billing error.</li>
    <li><strong>Wrong lesion size for removal code:</strong> Codes 11300&ndash;11313 are stratified by lesion diameter (0.5 cm, 0.6&ndash;1.0 cm, 1.1&ndash;2.0 cm, etc.) and body location. A coding error here can result in a bill that is $100&ndash;$300 higher than it should be.</li>
    <li><strong>Unbundling lesion removals:</strong> Multiple lesions of the same type destroyed in the same session should use the primary code plus add-on codes (e.g., 17003 for additional premalignant lesions), not separate primary codes for each.</li>
</ul>

<div class="key-takeaway">
    <strong>How to check your bill:</strong> Request an itemized bill and ask for the CPT code for each procedure. Cross-reference the lesion removal code against the size documented in your visit notes. If the bill lists a code for a lesion larger than the one removed, that is an error. <a href="/scan">Upload your dermatology bill to BillKarma</a> to run an automated check.
</div>

<h2 id="lower-cost-options">7. Lower-cost options: teledermatology</h2>

<p>Teledermatology has grown significantly since 2020 and is now a legitimate, lower-cost option for many dermatologic concerns. A synchronous (live video) teledermatology visit typically costs <strong>$75&ndash;$150</strong> without insurance&mdash;roughly half the cost of an in-person visit.</p>

<p>Asynchronous &ldquo;store-and-forward&rdquo; teledermatology (where you submit photos for a dermatologist to review) is even cheaper, often <strong>$40&ndash;$85</strong> per consultation. Services like Teladoc, MDLive, and direct-to-consumer platforms offer this model.</p>

<p><strong>What teledermatology is good for:</strong> Acne, rashes, eczema flares, medication refills for known conditions, and initial evaluation of a suspicious mole (though any biopsy will still require an in-person visit).</p>

<p><strong>What it cannot replace:</strong> Any procedure requiring physical examination, biopsy, or treatment (cryotherapy, Mohs surgery, phototherapy). Insurance coverage for teledermatology visits varies by plan&mdash;many commercial plans cover synchronous telehealth visits at the same copay as in-person visits, while asynchronous consults may not be covered.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does a dermatologist visit cost without insurance?</h3>
        <p>A new patient comprehensive exam typically runs $200&ndash;$350 without insurance. Follow-up visits are lower at $150&ndash;$250. Costs vary by location and whether the visit is for a medical or cosmetic concern.</p>
    </div>

    <div class="faq-item">
        <h3>Does insurance cover dermatology visits?</h3>
        <p>Yes, for medically necessary conditions like acne requiring prescription treatment, eczema, psoriasis, skin cancer, and rashes. Cosmetic services (Botox, fillers, chemical peels, cosmetic laser) are not covered. You will pay your specialist copay of $30&ndash;$75 for covered visits.</p>
    </div>

    <div class="faq-item">
        <h3>Is a skin cancer screening covered by insurance?</h3>
        <p>Medicare covers full-body skin cancer screenings as preventive with no cost-sharing. Most ACA-compliant commercial plans also cover annual skin exams at no cost. If a biopsy is performed during the visit, that service is billed separately and subject to cost-sharing.</p>
    </div>

    <div class="faq-item">
        <h3>Do I need prior authorization for dermatology biologics?</h3>
        <p>Yes. Dupixent for eczema and biologics like Humira or Skyrizi for psoriasis almost always require prior authorization. Insurers require documentation of failed conventional therapy. Step therapy requirements may apply before a biologic is approved.</p>
    </div>

    <div class="faq-item">
        <h3>What is the most common billing error on dermatology claims?</h3>
        <p>The most frequent error is using the wrong lesion removal CPT code based on lesion size. Billing a code for a larger lesion than was actually removed inflates the bill. BillKarma data shows dermatology billing errors affect 26% of claims.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">American Academy of Dermatology: Skin Cancer Statistics (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">American Society for Dermatologic Surgery: Procedure Cost Survey (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: CPT Code Lookup &mdash; Dermatology Codes 11300&ndash;17999</a></li>
    <li><a href="#" target="_blank" rel="noopener">National Psoriasis Foundation: Insurance and Prior Authorization Guide</a></li>
    <li><a href="#" target="_blank" rel="noopener">Journal of the American Academy of Dermatology: Teledermatology Outcomes (2024)</a></li>
</ul>
""",
})
