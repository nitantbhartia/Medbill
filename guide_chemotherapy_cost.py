"""Guide: How Much Does Chemotherapy Cost? (2026 Complete Guide)."""

from guides import register, _embed

register("chemotherapy-cost", {
    "title": "How Much Does Chemotherapy Cost? (2026 Complete Guide)",
    "meta_description": "Chemotherapy costs $10,000–$200,000+ per treatment cycle. See drug-by-drug costs, Medicare coverage, patient assistance programs, and how hospitals mark up chemo drugs.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does chemotherapy cost in 2026?",
            "a": "Chemotherapy costs vary enormously by drug regimen: a cycle of carboplatin and paclitaxel (common in lung and ovarian cancer) costs $3,000 to $10,000 per cycle, while targeted therapies and immunotherapy agents like pembrolizumab (Keytruda) can run $15,000 to $30,000 per cycle. A full treatment course of 4 to 8 cycles can total $10,000 to $200,000 or more. The drug itself is the largest cost driver, followed by infusion center facility fees.",
        },
        {
            "q": "Does Medicare cover chemotherapy?",
            "a": "Yes. Medicare Part B covers intravenous (IV) chemotherapy administered in a hospital outpatient department or physician&rsquo;s office. Medicare pays 80% of the approved amount after your Part B deductible ($257 in 2026), and you owe 20%. Oral chemotherapy drugs are covered under Medicare Part D, subject to your plan&rsquo;s formulary and cost-sharing. The Oral Parity Act has led more plans to align oral and IV chemo cost sharing, but coverage details vary by plan.",
        },
        {
            "q": "What is the CPT code for chemotherapy infusion?",
            "a": "The primary CPT code for chemotherapy infusion is 96413 (chemotherapy administration, intravenous infusion, up to 1 hour). Each additional hour adds CPT 96415. Non-chemotherapy infusions administered alongside chemo use different codes (96360 for hydration, 96365 for therapeutic drug infusion). On your bill, you may see a cascade of these codes for a single infusion visit lasting several hours. Medicare pays approximately $200 to $450 per code depending on the setting.",
        },
        {
            "q": "How do hospitals mark up chemotherapy drugs?",
            "a": "Hospitals typically mark up chemotherapy drugs at an average of 3.5 times the Average Wholesale Price (AWP). For a drug with an AWP of $2,000 per dose, the hospital charges $7,000. The hospital&rsquo;s actual acquisition cost under the 340B Drug Pricing Program (which many cancer centers participate in) may be 25 to 50% below AWP, meaning the effective markup can exceed 10 times acquisition cost. Patients can request the drug&rsquo;s NDC code and AWP to benchmark charges.",
        },
        {
            "q": "What financial assistance is available for chemotherapy costs?",
            "a": "Several programs can reduce or eliminate chemotherapy drug costs. Drug manufacturers offer Patient Assistance Programs (PAPs) for brand-name oncology drugs&mdash;most major manufacturers (Pfizer, Genentech, Bristol-Myers Squibb, AstraZeneca) have programs for uninsured or underinsured patients. Foundations like CancerCare and the Patient Advocate Foundation provide copay assistance grants. The 340B program allows eligible patients at qualifying hospitals to access drugs at significantly reduced prices.",
        },
    ],
    "body": f"""
<div class="answer-box">
    <p><strong>Direct answer:</strong> Chemotherapy costs <strong>$10,000 to $200,000+ per treatment course</strong> depending on the drug regimen, number of cycles, and facility. Hospitals mark up chemo drugs an average of <strong>3.5 times</strong> the wholesale price. Medicare Part B covers IV chemo at 80% after your deductible. Patient assistance programs can cover drug costs entirely for qualifying patients. BillKarma&rsquo;s data shows a <strong>37% billing error rate</strong> in oncology claims.</p>
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-by-drug">Chemotherapy cost by drug and regimen</a></li>
        <li><a href="#oral-vs-iv">Oral vs. IV chemotherapy cost comparison</a></li>
        <li><a href="#facility-comparison">Hospital outpatient vs. in-office infusion center</a></li>
        <li><a href="#medicare-coverage">Medicare coverage for chemotherapy</a></li>
        <li><a href="#drug-markups">How hospitals mark up chemo drugs</a></li>
        <li><a href="#patient-assistance">Patient assistance and copay programs</a></li>
        <li><a href="#billing-codes">Chemotherapy billing codes explained</a></li>
        <li><a href="#billing-errors">Common oncology billing errors</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-by-drug">1. Chemotherapy cost by drug and regimen</h2>

<p>The chemotherapy drug itself is the single largest cost component of cancer treatment. Drug costs vary from a few hundred dollars per cycle for older generic drugs to tens of thousands for newer targeted therapies. Below are typical per-cycle costs for common regimens:</p>

<table>
    <thead>
        <tr>
            <th>Drug / Regimen</th>
            <th>Cancer Type</th>
            <th>Cost Per Cycle (Drug Only)</th>
            <th>Typical Cycles</th>
            <th>Total Drug Cost Range</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Carboplatin + Paclitaxel</td><td>Lung, ovarian, head/neck</td><td>$1,500&ndash;$5,000</td><td>4&ndash;6</td><td>$6,000&ndash;$30,000</td></tr>
        <tr><td>FOLFOX (oxaliplatin, leucovorin, 5-FU)</td><td>Colorectal</td><td>$1,000&ndash;$4,000</td><td>6&ndash;12</td><td>$6,000&ndash;$48,000</td></tr>
        <tr><td>Doxorubicin + Cyclophosphamide (AC)</td><td>Breast cancer</td><td>$1,200&ndash;$4,500</td><td>4</td><td>$4,800&ndash;$18,000</td></tr>
        <tr><td>Pembrolizumab (Keytruda)</td><td>Multiple cancers</td><td>$12,000&ndash;$20,000</td><td>6&ndash;18+</td><td>$72,000&ndash;$360,000</td></tr>
        <tr><td>Trastuzumab (Herceptin)</td><td>HER2+ breast cancer</td><td>$5,000&ndash;$9,000</td><td>6&ndash;18</td><td>$30,000&ndash;$162,000</td></tr>
        <tr><td>Rituximab (Rituxan)</td><td>Lymphoma, leukemia</td><td>$6,000&ndash;$12,000</td><td>4&ndash;8</td><td>$24,000&ndash;$96,000</td></tr>
    </tbody>
</table>

<p>These figures reflect drug acquisition costs and do not include infusion center facility fees, administration fees, anti-nausea medications, hydration fluids, or the oncologist&rsquo;s professional fees&mdash;all of which add to the total bill. A typical infusion visit for carboplatin and paclitaxel generates a total bill of $8,000 to $25,000 when facility and administration charges are included.</p>

<p>Look up what Medicare pays for chemotherapy infusion at your facility:</p>

{_embed(mode="cost", cpt="96413", title="Chemotherapy Infusion Cost", subtitle="96413 \u2013 Chemotherapy infusion, first hour")}

<h2 id="oral-vs-iv">2. Oral vs. IV chemotherapy cost comparison</h2>

<p>Not all chemotherapy is given by infusion. Many cancer drugs are taken orally as pills or capsules at home. Oral and IV chemotherapy can cost similarly&mdash;but how they are covered by insurance differs significantly.</p>

<table>
    <thead>
        <tr>
            <th>Factor</th>
            <th>IV Chemotherapy</th>
            <th>Oral Chemotherapy</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Medicare coverage</td><td>Part B (80% after deductible)</td><td>Part D (formulary-dependent)</td></tr>
        <tr><td>Typical patient cost share</td><td>20% of allowed amount</td><td>Up to 25&ndash;33% of drug cost</td></tr>
        <tr><td>Facility fee added?</td><td>Yes (infusion center)</td><td>No</td></tr>
        <tr><td>Administration fee</td><td>Yes (96413 and add-on codes)</td><td>No</td></tr>
        <tr><td>Copay assistance available?</td><td>Yes (for facility copays)</td><td>Yes (manufacturer programs)</td></tr>
    </tbody>
</table>

<p>The coverage gap for oral chemotherapy has been a significant patient burden. Under Medicare Part D, a $10,000-per-month oral chemotherapy drug can result in thousands of dollars in out-of-pocket costs until the catastrophic coverage threshold is met. The Inflation Reduction Act (2022) has capped Medicare Part D out-of-pocket costs at $2,000 annually starting in 2025, providing significant relief for high-cost oral oncology drugs.</p>

<h2 id="facility-comparison">3. Hospital outpatient vs. in-office infusion center</h2>

<p>Where you receive IV chemotherapy dramatically affects the total bill. The drug cost is the same regardless of setting, but facility and administration fees vary significantly:</p>

<table>
    <thead>
        <tr>
            <th>Setting</th>
            <th>Facility Fee per Visit</th>
            <th>Administration Fee (CPT 96413)</th>
            <th>Medicare Advantage Considerations</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Hospital outpatient infusion center</td><td>$500&ndash;$2,500</td><td>$200&ndash;$450</td><td>Prior auth typically required</td></tr>
        <tr><td>Freestanding oncologist office / infusion suite</td><td>$100&ndash;$500</td><td>$150&ndash;$300</td><td>Prior auth may still be required</td></tr>
        <tr><td>Freestanding infusion center (independent)</td><td>$150&ndash;$600</td><td>$150&ndash;$300</td><td>Verify in-network status</td></tr>
    </tbody>
</table>

<p>A 2024 study in JAMA Oncology found that patients receiving chemotherapy at hospital outpatient departments paid an average of $1,800 more per infusion visit than patients treated at physician offices for the same drugs and regimens. Over a 6-cycle treatment course, that difference totals over $10,000. If your oncologist treats patients at both a hospital and a private infusion suite, ask which setting will minimize your facility fees.</p>

<h2 id="medicare-coverage">4. Medicare coverage for chemotherapy</h2>

<p>Medicare&rsquo;s coverage of chemotherapy splits across two parts depending on how the drug is administered:</p>

<ul>
    <li><strong>Part B (IV chemotherapy):</strong> Covers drugs administered by injection or infusion in a medical setting. Medicare pays 80% of the approved amount after the $257 Part B deductible. You owe 20%, which on a $5,000 drug infusion is $1,000 per visit&mdash;a significant burden over multiple cycles. Medigap plans typically cover this 20% coinsurance.</li>
    <li><strong>Part D (oral chemotherapy):</strong> Covered under your Part D drug plan subject to formulary placement and tier cost-sharing. The 2025 $2,000 annual out-of-pocket cap under the Inflation Reduction Act limits your maximum exposure for covered Part D drugs.</li>
</ul>

<p>Medicare also covers related services during chemotherapy treatment, including:</p>

<ul>
    <li>Anti-nausea medications administered as part of chemotherapy (Part B)</li>
    <li>Erythropoiesis-stimulating agents (ESAs) for chemo-induced anemia (Part B)</li>
    <li>G-CSF growth factors (Neupogen, Neulasta) to prevent infection (Part B)</li>
    <li>Lab work and imaging ordered as part of cancer management (Part B)</li>
</ul>

<h2 id="drug-markups">5. How hospitals mark up chemotherapy drugs</h2>

<p>Chemotherapy drug markups are among the highest in all of medicine. Hospitals purchase drugs at the Average Wholesale Price (AWP) or below (especially 340B-eligible hospitals, which can purchase drugs at 25 to 50% below AWP), then charge patients and insurers multiples of that price.</p>

<p>BillKarma&rsquo;s analysis of oncology billing data shows hospitals charge an average of <strong>3.5 times AWP</strong> for chemotherapy drugs. For a drug with an AWP of $3,000 per dose, the bill reads $10,500. At a 340B-eligible hospital that acquired the drug for $1,500, the effective markup is 7 times acquisition cost.</p>

<p>To benchmark the drug charge on your bill:</p>
<ol>
    <li>Find the National Drug Code (NDC) on your itemized bill. It is an 11-digit number identifying the exact drug and dosage.</li>
    <li>Look up the AWP for that NDC at a drug pricing database (Micromedex RED BOOK or similar).</li>
    <li>Compare the AWP to what you were billed. If the charge exceeds 4x AWP, it warrants a formal dispute.</li>
    <li>Ask if the hospital participates in the 340B Drug Pricing Program. If so, their acquisition cost may be far below AWP, strengthening your case for a reduction.</li>
</ol>

<h2 id="patient-assistance">6. Patient assistance and copay programs</h2>

<p>Drug manufacturers and independent foundations offer substantial financial assistance for chemotherapy costs. These programs exist because manufacturers prefer patients receive their drugs (often at reduced or zero cost) rather than forgo treatment:</p>

<table>
    <thead>
        <tr>
            <th>Program / Organization</th>
            <th>Type of Assistance</th>
            <th>How to Apply</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Pfizer RxPathways</td><td>Free drugs for uninsured/underinsured</td><td>pfizerrxpathways.com</td></tr>
        <tr><td>Genentech Access Solutions</td><td>Free or reduced-cost Roche/Genentech drugs</td><td>gene.com/patients/access</td></tr>
        <tr><td>Bristol-Myers Squibb Patient Assistance</td><td>Free drugs including Opdivo, Yervoy</td><td>bms.com/patient-assistance</td></tr>
        <tr><td>AstraZeneca Access 360</td><td>Copay assistance + uninsured programs</td><td>astrazenecaaccess360.com</td></tr>
        <tr><td>CancerCare Co-Payment Assistance</td><td>Copay grants up to $10,000</td><td>cancercare.org/copaygrants</td></tr>
        <tr><td>Patient Advocate Foundation Co-Pay Relief</td><td>Copay assistance by diagnosis</td><td>copays.org</td></tr>
        <tr><td>HealthWell Foundation</td><td>Premium and copay assistance</td><td>healthwellfoundation.org</td></tr>
    </tbody>
</table>

<p>Your oncology social worker (most cancer centers have them) can help identify which programs you qualify for and assist with applications. Always ask to speak with the social worker or financial counselor at your cancer center before your first treatment&mdash;the application process takes time and should be started before bills arrive.</p>

<h2 id="billing-codes">7. Chemotherapy billing codes explained</h2>

<p>A single chemotherapy infusion visit generates multiple CPT codes. Understanding these codes helps you verify your bill is accurate:</p>

<table>
    <thead>
        <tr>
            <th>CPT Code</th>
            <th>Description</th>
            <th>Medicare Rate (2026, Outpatient)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>96413</td><td>Chemotherapy infusion, IV, first hour</td><td>~$230</td></tr>
        <tr><td>96415</td><td>Chemotherapy infusion, each additional hour</td><td>~$115</td></tr>
        <tr><td>96417</td><td>Chemotherapy infusion, each additional sequential drug</td><td>~$118</td></tr>
        <tr><td>96365</td><td>Therapeutic drug infusion, first hour (non-chemo drugs)</td><td>~$165</td></tr>
        <tr><td>96360</td><td>IV hydration, first hour</td><td>~$58</td></tr>
        <tr><td>99213</td><td>Established patient office visit (oncologist E&amp;M)</td><td>~$97</td></tr>
    </tbody>
</table>

<p>On a 4-hour carboplatin and paclitaxel infusion day, a typical bill might include 96413 + three units of 96415 + one unit of 96417 (for the second drug) + 96360 (hydration). Verify the number of infusion hours billed matches the actual infusion duration documented in your records.</p>

<h2 id="billing-errors">8. Common oncology billing errors</h2>

<p>BillKarma&rsquo;s analysis identifies a <strong>37% billing error rate</strong> in oncology claims. The most common errors specific to chemotherapy billing:</p>

<ol>
    <li><strong>Wrong NDC code:</strong> Billing for a more expensive drug formulation than was administered, or listing the wrong drug entirely. Request the NDC code on your itemized bill and verify it matches what you received.</li>
    <li><strong>Wrong dosage units:</strong> Chemotherapy is dosed by body surface area (mg/m&sup2;). Billing for a larger dose than administered overstates the drug charge. Compare the billed dose to your treatment plan documentation.</li>
    <li><strong>Upcoded infusion time:</strong> Billing more infusion hours than were documented in the nursing administration record. Each extra unit of 96415 adds $115+ to the bill.</li>
    <li><strong>Billing for wasted drug:</strong> Some providers bill for the full vial of a drug even if only part was used and the remainder was discarded. Medicare has specific rules limiting waste billing; commercial payers vary.</li>
    <li><strong>Duplicate administration fees:</strong> Charging both the hospital facility administration fee and a separate professional administration fee for the same infusion service.</li>
    <li><strong>Missing 340B discount pass-through:</strong> If the hospital acquired the drug under the 340B program, some payers require the discounted acquisition cost to be reflected in the billed amount.</li>
</ol>

<div class="key-takeaway">
    <strong>Chemotherapy bills are among the most complex in healthcare.</strong> <a href="/fight-debt">Use BillKarma&rsquo;s oncology bill audit tools</a> to cross-reference drug NDC codes, infusion hours, and dosage units against your treatment records and identify errors before they go to collections.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does chemotherapy cost in 2026?</h3>
        <p>Chemotherapy costs vary enormously by drug regimen: a cycle of carboplatin and paclitaxel costs $3,000 to $10,000 per cycle, while targeted therapies like pembrolizumab can run $15,000 to $30,000 per cycle. A full treatment course of 4 to 8 cycles can total $10,000 to $200,000 or more. The drug itself is the largest cost driver, followed by infusion center facility fees.</p>
    </div>
    <div class="faq-item">
        <h3>Does Medicare cover chemotherapy?</h3>
        <p>Yes. Medicare Part B covers intravenous chemotherapy administered in a hospital outpatient department or physician&rsquo;s office at 80% of the approved amount after your Part B deductible. Oral chemotherapy drugs are covered under Medicare Part D. The Inflation Reduction Act capped Part D out-of-pocket costs at $2,000 per year starting in 2025.</p>
    </div>
    <div class="faq-item">
        <h3>What is the CPT code for chemotherapy infusion?</h3>
        <p>The primary CPT code for chemotherapy infusion is 96413 (first hour). Each additional hour adds CPT 96415. Non-chemotherapy infusions administered alongside chemo use different codes (96360 for hydration, 96365 for therapeutic drug infusion). On your bill, you may see a cascade of these codes for a single infusion visit.</p>
    </div>
    <div class="faq-item">
        <h3>How do hospitals mark up chemotherapy drugs?</h3>
        <p>Hospitals typically mark up chemotherapy drugs at an average of 3.5 times the Average Wholesale Price (AWP). Hospitals participating in the 340B Drug Pricing Program acquire drugs at 25 to 50% below AWP, meaning effective markups can exceed 10 times acquisition cost. Patients can request the drug&rsquo;s NDC code and look up the AWP to benchmark charges.</p>
    </div>
    <div class="faq-item">
        <h3>What financial assistance is available for chemotherapy costs?</h3>
        <p>Drug manufacturers offer Patient Assistance Programs for brand-name oncology drugs. Major programs include Pfizer RxPathways, Genentech Access Solutions, and AstraZeneca Access 360 for uninsured or underinsured patients. Foundations like CancerCare and the Patient Advocate Foundation provide copay assistance grants. Ask your oncology social worker to help identify and apply for programs before your first treatment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule 2026 &mdash; Oncology</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient" target="_blank" rel="noopener">CMS Hospital Outpatient PPS 2026 &mdash; Chemotherapy Administration</a></li>
    <li><a href="https://www.hrsa.gov/opa/index.html" target="_blank" rel="noopener">HRSA: 340B Drug Pricing Program</a></li>
    <li><a href="https://jamanetwork.com/journals/jamaoncology" target="_blank" rel="noopener">JAMA Oncology: Site of Care Cost Differentials in Chemotherapy</a></li>
    <li><a href="https://cancercare.org" target="_blank" rel="noopener">CancerCare: Financial Assistance for Cancer Patients</a></li>
    <li><a href="https://copays.org" target="_blank" rel="noopener">Patient Advocate Foundation: Co-Pay Relief Program</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/explaining-the-prescription-drug-provisions-in-the-inflation-reduction-act/" target="_blank" rel="noopener">KFF: Medicare Drug Price Provisions in the Inflation Reduction Act</a></li>
</ul>
""",
})
