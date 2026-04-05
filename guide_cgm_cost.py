"""Guide: Continuous Glucose Monitor (CGM) Cost & Insurance Coverage (2026)."""

from guides import register, _embed

register("continuous-glucose-monitor-cost", {
    "title": "Continuous Glucose Monitor (CGM) Cost & Insurance Coverage (2026)",
    "meta_description": "CGMs cost $100–$400/month without insurance. Learn what Medicare and commercial plans cover, the 2024 CMS rule change for Type 2 patients, HCPCS codes, and how to appeal a CGM denial.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does a continuous glucose monitor cost without insurance?",
            "a": "Costs vary by brand. The Dexcom G7 runs $299–$400/month for sensors plus a separate receiver. The Abbott FreeStyle Libre 3 costs $100–$150/month and is among the most affordable prescription CGMs. Medtronic Guardian sensor costs are typically bundled with insulin pump supplies. OTC versions (Libre 2 available without a prescription) run approximately $75/month — but insurance will not cover OTC CGMs. Patient assistance programs from Dexcom (ACCESS program) and Abbott (myFreestyle) can reduce out-of-pocket costs significantly for eligible patients.",
        },
        {
            "q": "Does Medicare cover CGMs?",
            "a": "Yes. Medicare Part B covers CGMs as durable medical equipment (DME) for patients with diabetes who are on insulin (Type 1 or Type 2). A major 2024 CMS rule change also extended Medicare CGM coverage to Type 2 patients who are NOT on insulin but are using basal insulin analogs or sulfonylureas — medications that carry a risk of hypoglycemia. This is a significant expansion that benefits millions of Type 2 patients. Medicare covers 80% of the approved amount after the Part B deductible.",
        },
        {
            "q": "What is the difference between therapeutic and non-therapeutic CGMs for Medicare?",
            "a": "A 'therapeutic' CGM is one where the patient uses the CGM readings to make treatment decisions (such as adjusting insulin doses) without confirming the reading with a fingerstick. A 'non-therapeutic' CGM requires the patient to confirm readings with a fingerstick before acting. Medicare's expanded 2024 coverage applies to therapeutic CGMs — meaning the device must be capable of making treatment decisions and must be prescribed by a physician for that purpose. Most modern CGMs (Dexcom G7, Libre 3) qualify as therapeutic.",
        },
        {
            "q": "What HCPCS codes are used for CGMs?",
            "a": "CGM supplies are billed using HCPCS codes under the DME benefit. A9276 is the CGM sensor (per day). A9277 is the CGM transmitter. A9278 is the CGM receiver/monitor. K0553 is used for a therapeutic CGM system. Some suppliers bill K0554 for non-therapeutic systems. Using the wrong HCPCS code for the CGM type is a common billing error — K0553 (therapeutic) reimburses at a higher rate than K0554 (non-therapeutic), and miscoding can result in either underpayment or overbilling.",
        },
        {
            "q": "Can I appeal a CGM insurance denial?",
            "a": "Yes, and you should. BillKarma data shows 44% of initial CGM coverage denials are overturned on appeal — making CGM one of the highest appeal success categories in medical billing. Common denial reasons include 'not medically necessary,' 'step therapy not completed,' or 'documentation insufficient.' Your doctor can submit a letter of medical necessity documenting your diagnosis, medication regimen, history of hypoglycemic events, and why CGM monitoring is clinically indicated.",
        },
    ],
    "body": f"""
<p class="lead">Continuous glucose monitors have transformed diabetes management&mdash;but their cost and insurance coverage remain confusing for millions of patients. The good news: a landmark 2024 CMS rule change significantly expanded Medicare CGM coverage to many Type 2 patients not on insulin. BillKarma data shows <strong>44% of initial CGM denials are overturned on appeal</strong>&mdash;making CGM one of the most worthwhile coverage battles to fight. Here is everything you need to know about CGM costs and coverage in 2026.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#device-costs">CGM devices and what they cost without insurance</a></li>
        <li><a href="#insurance-coverage">Commercial insurance coverage</a></li>
        <li><a href="#medicare-coverage">Medicare coverage and the 2024 CMS rule change</a></li>
        <li><a href="#therapeutic-vs-non">Therapeutic vs. non-therapeutic CGMs</a></li>
        <li><a href="#prior-auth">Prior authorization and step therapy</a></li>
        <li><a href="#hcpcs-billing-errors">HCPCS codes and common billing errors</a></li>
        <li><a href="#lower-cost-options">Lower-cost options and patient assistance programs</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="device-costs">1. CGM devices and what they cost without insurance</h2>

<p>Three major CGM systems dominate the market in 2026. Costs below reflect retail prices without insurance or patient assistance programs:</p>

<table>
    <thead>
        <tr><th>Device</th><th>Monthly Sensor Cost</th><th>Receiver/Reader</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Dexcom G7</strong></td><td>$299&ndash;$400</td><td>$299 (optional; app available)</td><td>10-day wear; FDA approved for Type 1 and Type 2; no fingerstick required</td></tr>
        <tr><td><strong>Abbott FreeStyle Libre 3</strong></td><td>$100&ndash;$150</td><td>Included (reader) or app</td><td>14-day wear; most affordable prescription CGM; widely covered</td></tr>
        <tr><td><strong>Medtronic Guardian 4</strong></td><td>Varies (bundled with pump)</td><td>Integrated with pump</td><td>Primarily used with Medtronic insulin pumps; not commonly prescribed standalone</td></tr>
        <tr><td><strong>Abbott Libre 2 (OTC)</strong></td><td>~$75</td><td>App only</td><td>Available without prescription; insurance will NOT cover OTC purchases</td></tr>
    </tbody>
</table>

<p>Annual CGM costs without insurance can reach <strong>$3,600&ndash;$4,800 for Dexcom G7</strong> or <strong>$1,200&ndash;$1,800 for Libre 3</strong>. These ongoing supply costs are a major burden for uninsured and underinsured patients&mdash;which is why understanding coverage options and patient assistance programs is essential.</p>

<div class="key-takeaway">
    <strong>The OTC trap:</strong> The Abbott FreeStyle Libre 2 became available over the counter in 2023, priced around $75/month without a prescription. While this sounds convenient, purchasing it OTC means your insurance will not cover it&mdash;even if you have diabetes and meet every coverage criterion. To get insurance coverage, you must obtain a prescription from your prescribing physician and purchase from a participating pharmacy or DME supplier.
</div>

<h2 id="insurance-coverage">2. Commercial insurance coverage</h2>

<p>Coverage for CGMs under commercial insurance has expanded significantly from 2020 to 2026, but it remains inconsistent across plans:</p>

<ul>
    <li><strong>Type 1 diabetes:</strong> Covered by virtually all commercial plans. CGMs are considered standard of care for Type 1 diabetes management. Prior authorization is usually required but approvals are routine for established Type 1 patients on insulin.</li>
    <li><strong>Type 2 diabetes on insulin:</strong> Covered by most commercial plans. Documentation of insulin use (basal or multiple daily injections) is typically required. Prior auth required at most plans.</li>
    <li><strong>Type 2 diabetes on non-insulin medications:</strong> Coverage varies significantly by plan. Some plans require step therapy (trial of fingerstick glucose monitoring before approving CGM). Denial rates are higher in this category, but appeal success is also high&mdash;especially since the 2024 CMS guidance has influenced commercial payer policies.</li>
    <li><strong>Prediabetes:</strong> Rarely covered. Considered preventive rather than therapeutic for insurance purposes in most plans.</li>
</ul>

<p>CGMs are covered as a pharmacy benefit on some plans (like a prescription) and as a DME benefit on others. The benefit category matters because your pharmacy deductible and DME deductible may differ. Ask your insurer which benefit category applies to your CGM before ordering.</p>

{_embed(mode="cost", cpt="A9276", title="Look up CGM coverage", subtitle="See Medicare reimbursement rates for CGM supplies.")}

<h2 id="medicare-coverage">3. Medicare coverage and the 2024 CMS rule change</h2>

<p>Medicare Part B covers CGMs as durable medical equipment (DME). Coverage has historically been limited, but a major 2024 rule change dramatically expanded eligibility:</p>

<p><strong>Coverage before 2024:</strong> Medicare covered CGMs only for patients with diabetes who were on intensive insulin therapy (multiple daily injections or insulin pump use). Type 2 patients on basal insulin only, oral medications, or no medications were generally not eligible.</p>

<p><strong>The 2024 CMS rule change:</strong> Effective January 2024, Medicare expanded CGM coverage to include patients with diabetes who are on <strong>any insulin therapy</strong> (including basal insulin) <strong>or on a sulfonylurea</strong>&mdash;a class of oral diabetes medications that can cause hypoglycemia. This is a major shift because:</p>

<ul>
    <li>Millions of Type 2 patients on once-daily basal insulin (glargine, detemir, degludec) who were previously ineligible are now covered.</li>
    <li>Type 2 patients on sulfonylureas (glipizide, glyburide, glimepiride) who are not on insulin at all are now eligible.</li>
    <li>The rationale is that both insulin and sulfonylureas carry hypoglycemia risk&mdash;making real-time glucose monitoring clinically valuable and medically necessary.</li>
</ul>

<table>
    <thead>
        <tr><th>Patient Type</th><th>Medicare CGM Coverage (Pre-2024)</th><th>Medicare CGM Coverage (2024+)</th></tr>
    </thead>
    <tbody>
        <tr><td>Type 1 diabetes (any treatment)</td><td>Covered (with intensive insulin therapy)</td><td>Covered</td></tr>
        <tr><td>Type 2 on multiple daily insulin injections</td><td>Covered</td><td>Covered</td></tr>
        <tr><td>Type 2 on basal insulin only</td><td>Often denied</td><td>Now covered</td></tr>
        <tr><td>Type 2 on sulfonylurea (no insulin)</td><td>Denied</td><td>Now covered</td></tr>
        <tr><td>Type 2 on metformin only (no hypoglycemia risk)</td><td>Denied</td><td>Still denied</td></tr>
        <tr><td>Prediabetes</td><td>Denied</td><td>Still denied</td></tr>
    </tbody>
</table>

<p><strong>Medicare cost-sharing:</strong> Medicare Part B covers 80% of the approved CGM amount after the annual Part B deductible ($257 in 2026). You pay 20%. If you have a Medigap supplement, it typically covers the 20% coinsurance. Medicare Advantage plans may have different cost-sharing rules.</p>

<div class="key-takeaway">
    <strong>If you are a Medicare patient with Type 2 diabetes on basal insulin or a sulfonylurea and were previously denied CGM coverage</strong>, you may now be eligible under the 2024 rule change. Ask your prescribing physician to resubmit a CGM order with documentation of your current medications and diabetes diagnosis. If previously denied, file a new prior authorization request citing the updated CMS coverage criteria.
</div>

<h2 id="therapeutic-vs-non">4. Therapeutic vs. non-therapeutic CGMs</h2>

<p>Medicare distinguishes between two types of CGMs based on clinical use:</p>

<p><strong>Therapeutic CGM:</strong> The patient uses CGM readings to make treatment decisions&mdash;like adjusting insulin doses or deciding to eat something to prevent a low&mdash;without confirming the reading with a fingerstick blood glucose test. Medicare covers therapeutic CGMs at a higher reimbursement rate (HCPCS K0553). Most modern CGMs (Dexcom G7, Abbott Libre 3) are designed and FDA-cleared as therapeutic systems.</p>

<p><strong>Non-therapeutic CGM:</strong> The patient uses the CGM for trend information only, and must confirm all readings with a fingerstick before making treatment decisions. These devices bill under K0554 at a lower rate. Non-therapeutic CGMs are less common in current clinical practice.</p>

<p>The therapeutic designation matters because it directly affects reimbursement. A supplier who bills a therapeutic CGM under the non-therapeutic code (K0554 instead of K0553) will be underpaid by Medicare&mdash;and may pass that underpayment to the patient as a balance bill. Conversely, billing a non-therapeutic device under the therapeutic code is overbilling. Make sure the HCPCS code on your bill matches the actual device prescribed.</p>

<h2 id="prior-auth">5. Prior authorization and step therapy</h2>

<p>Prior authorization is required for CGMs under most commercial insurance plans and Medicare Advantage. Here is the typical process:</p>

<ol>
    <li><strong>Physician prescribes the CGM</strong> with a specific brand and model documented in the order.</li>
    <li><strong>The DME supplier (or pharmacy) submits the PA request</strong> to your insurer with supporting clinical documentation from your prescribing physician.</li>
    <li><strong>Required documentation typically includes:</strong>
        <ul>
            <li>Diabetes diagnosis (Type 1 or Type 2) with ICD-10 code</li>
            <li>Current medication regimen (insulin type/dose, or sulfonylurea name/dose)</li>
            <li>History of hypoglycemic episodes or A1C documentation</li>
            <li>Physician attestation that CGM is needed for treatment management</li>
        </ul>
    </li>
    <li><strong>Step therapy</strong> may be required at some plans: you may need to demonstrate that you used fingerstick glucose monitoring for a defined period (typically 3&ndash;6 months) before the insurer will approve CGM. Document all fingerstick test strip prescriptions and refill history.</li>
    <li><strong>If denied,</strong> your physician can request a peer-to-peer review. Success rates are high, particularly for patients with documented hypoglycemia history or poor A1C control on current regimen.</li>
</ol>

<h2 id="hcpcs-billing-errors">6. HCPCS codes and common billing errors</h2>

<table>
    <thead>
        <tr><th>HCPCS Code</th><th>Description</th><th>Common Error</th></tr>
    </thead>
    <tbody>
        <tr><td>A9276</td><td>CGM sensor (per day)</td><td>Billing above allowed quantity (14-day sensor billed as 14 units of A9276; billing 30 units for one sensor is overbilling)</td></tr>
        <tr><td>A9277</td><td>CGM transmitter</td><td>Billing transmitter replacement more frequently than device lifespan; Dexcom G7 does not have a separate transmitter</td></tr>
        <tr><td>A9278</td><td>CGM receiver/monitor</td><td>Billing new receiver when patient uses smartphone app only</td></tr>
        <tr><td>K0553</td><td>Therapeutic CGM system</td><td>Billing K0553 for a non-therapeutic device; or billing K0554 when the therapeutic K0553 rate applies</td></tr>
        <tr><td>K0554</td><td>Receiver only (non-therapeutic)</td><td>Used incorrectly for therapeutic systems; results in lower reimbursement</td></tr>
    </tbody>
</table>

<p><strong>Supplier upcoding:</strong> A common abuse pattern is DME suppliers billing for CGM components at maximum allowed quantities even when the patient received fewer supplies. For example, billing 30 days of A9276 sensors when only a 14-day supply was dispensed. Review your EOB and compare the quantity billed to what you actually received.</p>

<p><strong>Quantity limits:</strong> Medicare and most insurers set quantity limits for CGM sensors. For a 14-day sensor (like the Libre 3), Medicare allows up to approximately 26 sensors per year (one every two weeks). Billing above these quantity limits is a common denial trigger and audit target.</p>

<div class="key-takeaway">
    <strong>GoodRx for CGM supplies:</strong> If your insurance denies coverage and you are paying out of pocket, GoodRx can significantly reduce the cost of CGM sensors at participating pharmacies. The FreeStyle Libre 3 14-day sensor pack (2 sensors) can often be found for under $100 with GoodRx compared to $150+ retail. This does not apply to sensors purchased through DME suppliers.
</div>

<h2 id="lower-cost-options">7. Lower-cost options and patient assistance programs</h2>

<p>If you are uninsured, underinsured, or facing a coverage denial while awaiting appeal, these options can reduce your CGM costs:</p>

<ul>
    <li><strong>Dexcom ACCESS Program:</strong> Provides free or reduced-cost Dexcom CGM supplies to uninsured and underinsured patients who meet income eligibility requirements. Apply at dexcom.com/access.</li>
    <li><strong>Abbott myFreestyle Program:</strong> Abbott offers patient assistance for FreeStyle Libre sensors. Eligible patients may receive sensors at low or no cost. Apply through your prescribing physician or at freestylelibre.us.</li>
    <li><strong>GoodRx:</strong> Can reduce out-of-pocket costs for CGM sensors dispensed at retail pharmacies. Works best for FreeStyle Libre products available at standard pharmacies.</li>
    <li><strong>FreeStyle Libre 2 OTC (temporary bridge):</strong> If you are waiting for prior auth approval, the OTC Libre 2 (~$75/month without prescription) can serve as a temporary bridge. You will not be reimbursed for OTC purchases, but it provides coverage during the authorization gap.</li>
    <li><strong>State programs:</strong> Some state Medicaid programs have expanded CGM coverage beyond federal Medicare requirements. Check your state&rsquo;s Medicaid coverage policies if you are Medicaid-eligible.</li>
</ul>

<div class="case-study">
    <h3>Case study: CGM denial overturned for Type 2 patient on basal insulin</h3>
    <p><strong>Situation:</strong> A 68-year-old Medicare patient with Type 2 diabetes managed on once-daily glargine (basal insulin) was denied CGM coverage by her Medicare Advantage plan. The denial stated she &ldquo;did not meet criteria for intensive insulin therapy.&rdquo;</p>
    <p><strong>The problem:</strong> Her Medicare Advantage plan had not yet updated its coverage criteria to reflect the 2024 CMS rule change extending coverage to patients on basal insulin. The denial was based on outdated pre-2024 criteria.</p>
    <p><strong>The outcome:</strong> Her endocrinologist submitted an appeal citing the January 2024 CMS coverage determination and her documented A1C of 8.4% with two hypoglycemic episodes in the prior six months. The appeal was approved within 5 business days. Her CGM cost dropped from $130/month out-of-pocket (OTC purchase) to $26/month (20% coinsurance on the Medicare-approved amount). <strong>Annual savings: $1,248.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does a continuous glucose monitor cost without insurance?</h3>
        <p>The Dexcom G7 costs $299&ndash;$400/month. The Abbott FreeStyle Libre 3 runs $100&ndash;$150/month. The OTC Abbott Libre 2 is about $75/month but is not covered by insurance. Patient assistance programs from Dexcom and Abbott can significantly reduce costs for eligible patients.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover CGMs?</h3>
        <p>Yes. Medicare Part B covers CGMs as DME for patients with diabetes on insulin, and since the 2024 CMS rule change, also for Type 2 patients on basal insulin or sulfonylureas. Medicare pays 80% of the approved amount after the $257 Part B deductible. Coverage requires a physician prescription and documentation of diabetes diagnosis and medication regimen.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between therapeutic and non-therapeutic CGMs for Medicare?</h3>
        <p>A therapeutic CGM allows the patient to make treatment decisions based on the reading without a confirmatory fingerstick. A non-therapeutic CGM requires fingerstick confirmation. Medicare covers therapeutic CGMs at a higher rate (K0553). Most modern CGMs (Dexcom G7, Libre 3) qualify as therapeutic.</p>
    </div>

    <div class="faq-item">
        <h3>What HCPCS codes are used for CGMs?</h3>
        <p>A9276 (sensor per day), A9277 (transmitter), A9278 (receiver), K0553 (therapeutic CGM system), K0554 (non-therapeutic). Common errors include wrong code for CGM type, billing quantities above device lifespan, and billing a receiver when the patient uses only a smartphone app.</p>
    </div>

    <div class="faq-item">
        <h3>Can I appeal a CGM insurance denial?</h3>
        <p>Yes, and you should&mdash;44% of initial CGM denials are overturned on appeal. Your doctor should submit a letter of medical necessity documenting your diagnosis, medications, hypoglycemia history, and clinical need. Cite the 2024 CMS rule change if you are a Medicare patient with Type 2 diabetes on basal insulin or sulfonylurea. BillKarma can help you build the appeal.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: CGM Coverage Determination (January 2024)</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: HCPCS Code Lookup &mdash; CGM Supplies A9276&ndash;A9278, K0553&ndash;K0554</a></li>
    <li><a href="#" target="_blank" rel="noopener">American Diabetes Association: Standards of Care in Diabetes (2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Dexcom: ACCESS Program for Uninsured Patients</a></li>
    <li><a href="#" target="_blank" rel="noopener">Abbott: myFreestyle Patient Assistance Program</a></li>
    <li><a href="#" target="_blank" rel="noopener">JAMA: CGM Use in Type 2 Diabetes &mdash; Clinical Evidence Review (2024)</a></li>
    <li><a href="#" target="_blank" rel="noopener">KFF: Diabetes Device Coverage Under Medicare Part B (2025)</a></li>
</ul>
""",
})
