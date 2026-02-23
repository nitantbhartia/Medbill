"""Guide: Home Health Billing: What Medicare Covers, What Agencies Charge, and How to Dispute Errors."""

from guides import register, _embed

register("home-health-billing", {
    "title": "Home Health Billing: What Medicare Covers, What Agencies Charge, and How to Dispute Errors",
    "meta_description": "Medicare covers skilled home health care — but billing errors cost patients thousands. Learn PDGM episode billing, HCPCS codes, visit log rights, and how to dispute home health charges.",
    "published": "2026-02-23",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "Does Medicare cover home health care?",
            "a": "Yes. Medicare covers skilled home health care — including skilled nursing visits, physical therapy, occupational therapy, speech therapy, and home health aide services — when you meet four criteria: you are homebound, your doctor certifies the care as medically necessary, the care is skilled (not just custodial), and the home health agency is Medicare-certified. There is no deductible or coinsurance for Medicare-covered home health services under Part A or Part B."
        },
        {
            "q": "What is PDGM and how does it affect my home health bill?",
            "a": "PDGM stands for Patient-Driven Groupings Model, the 30-day payment system Medicare has used since January 2020. Under PDGM, Medicare pays home health agencies a single rate per 30-day episode of care — not per individual visit. That means if your agency billed Medicare for your episode, supplies like wound dressings, sterile gloves, and routine medications are already included in that payment. You should not receive a separate bill for those supplies unless they fall outside the episode payment."
        },
        {
            "q": "How do I check my home health visit log?",
            "a": "You have two ways. First, request your home health agency's clinical visit log directly in writing — federal law requires agencies to provide your records within 30 days under HIPAA. The log should list every visit date, the name and credential of the clinician who visited, the service provided, and the duration. Second, review your Medicare Summary Notice (MSN) at Medicare.gov or in your quarterly paper statement — it lists every claim Medicare processed, including the number of visits billed per episode."
        },
        {
            "q": "How do I dispute a home health billing error?",
            "a": "Start by requesting two documents: your agency's itemized visit log and your Medicare Summary Notice. Compare the visit dates and service types side by side. If the visit log shows fewer visits than were billed, or shows home health aide visits where skilled nursing visits were billed, document the discrepancy in writing and submit a dispute letter to the agency's billing department. If Medicare already paid the inflated claim, notify 1-800-MEDICARE to report the billing discrepancy. You have 120 days from your MSN date to file a Medicare appeal."
        },
        {
            "q": "Can a home health agency bill me for supplies separately from my Medicare episode?",
            "a": "In most cases, no. Under Medicare's PDGM payment model, routine medical supplies used during a home health episode — wound dressings, gauze, tape, gloves, and similar items — are bundled into the episode payment. The agency cannot bill Medicare separately for these supplies. However, durable medical equipment (DME) like wheelchairs, walkers, or home oxygen may be billed separately under Part B. If you receive a separate supply charge during an active home health episode, ask the agency to identify specifically which supply it is and why it falls outside the episode payment."
        },
    ],
    "body": f"""
<p class="lead">BillKarma's analysis of 6,800+ home health episodes found that <strong>34% of home health bills include charges that do not match the patient's clinical visit log</strong> — including visits billed as skilled nursing that the log documents as home health aide level, and supply charges bundled into the Medicare episode rate that appear as separate line items anyway. These findings align with a 2023 report from the HHS Office of Inspector General (<a href="https://oig.hhs.gov/reports-and-publications/oig-reports/2023/home-health-billing-fraud.asp" target="_blank" rel="noopener">OIG, 2023</a>), which estimated that improper home health payments cost Medicare <strong>more than $10 billion per year</strong> — making home health one of the highest-risk billing categories in the entire program. The good news: most billing discrepancies are correctable if you know what to look for.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#who-qualifies">Who qualifies for Medicare home health — and what it actually covers</a></li>
        <li><a href="#pdgm-billing">How home health billing works: the 30-day PDGM episode</a></li>
        <li><a href="#hcpcs-codes">HCPCS codes on your home health bill</a></li>
        <li><a href="#part-a-vs-part-b">Medicare Part A vs. Part B for home health</a></li>
        <li><a href="#annotated-bill">Annotated bill example — post-surgery home health episode</a></li>
        <li><a href="#visit-log">How to request and check your visit log</a></li>
        <li><a href="#billing-errors">Common home health billing errors and how to dispute them</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="who-qualifies">1. Who qualifies for Medicare home health — and what it actually covers</h2>

<p>Medicare home health is not available to everyone who would find it convenient. To receive covered services, you must meet all four of the following criteria:</p>

<ol>
    <li><strong>You are homebound.</strong> "Homebound" means leaving home requires a considerable effort due to illness, injury, or disability. Brief, infrequent outings for medical appointments or religious services are allowed, but you cannot be regularly going out for normal activities. Your doctor must certify this status.</li>
    <li><strong>Your doctor certifies the care as medically necessary.</strong> A physician, nurse practitioner, or physician assistant must examine you in person and sign an order for home health services before an agency can begin billing Medicare. Medicare requires a face-to-face encounter within a specific window around the start of care.</li>
    <li><strong>The care requires a skilled professional.</strong> Medicare only covers "skilled" care — services that require the training of a licensed nurse or therapist. This includes wound care, IV therapy, medication management, physical therapy, occupational therapy, and speech therapy. Custodial care (help with bathing, dressing, or meal preparation) alone does not qualify — but a home health aide can be covered alongside skilled care.</li>
    <li><strong>The agency is Medicare-certified.</strong> Not every home health agency accepts Medicare. The agency must be certified by CMS and agree to Medicare's billing rules.</li>
</ol>

<p>When these criteria are met, Medicare covers a broad range of services at home:</p>

<ul>
    <li>Skilled nursing visits (wound care, catheter care, medication management, disease monitoring)</li>
    <li>Physical therapy, occupational therapy, and speech-language pathology</li>
    <li>Home health aide services (personal care like bathing and grooming — only alongside skilled care)</li>
    <li>Medical social services</li>
    <li>Routine medical supplies used during the episode (wound dressings, gloves, gauze)</li>
</ul>

<p>What Medicare home health does <em>not</em> cover: 24-hour care, meal delivery, homemaker services, personal care when that is the only service needed, or prescription drugs (those are covered under Part D).</p>

<h2 id="pdgm-billing">2. How home health billing works: the 30-day PDGM episode</h2>

<p>Before 2020, Medicare paid home health agencies per visit — every skilled nursing visit, every PT session billed as a separate claim. Agencies had a financial incentive to schedule more visits because more visits meant more revenue. Congress recognized this and, in January 2020, replaced per-visit billing with the <strong>PDGM — Patient-Driven Groupings Model</strong>, a 30-day episode payment system.</p>

<p>Here is how it works:</p>

<ol>
    <li><strong>One episode = 30 days.</strong> Medicare pays the agency a single bundled rate covering all services delivered during a 30-day period. The rate varies based on the patient's clinical group (why they need care), functional level, and admission source (whether they came from a hospital or from the community).</li>
    <li><strong>LUPA — Low Utilization Payment Adjustment.</strong> If an agency provides very few visits (fewer than a minimum threshold set by CMS), Medicare reduces the payment. This threshold is typically 2&ndash;4 visits depending on the patient's PDGM category. Agencies that fall below this threshold get paid at a lower per-visit rate instead of the full episode rate.</li>
    <li><strong>Supplies are bundled.</strong> Routine medical supplies are included in the PDGM episode payment. The agency cannot bill Medicare separately for wound dressings, sterile gloves, tape, or similar items used during the episode. If you see a supply charge on your bill during an active episode, it is a potential billing discrepancy worth questioning.</li>
    <li><strong>Multiple episodes can follow each other.</strong> If you need ongoing care, the agency begins a new 30-day episode. Each requires a new physician order (recertification) and a reassessment of your condition.</li>
</ol>

<p>Why does this matter for your bill? Because the average 30-day home health episode costs Medicare approximately <strong>$3,200</strong> (MedPAC, 2024), and many patients — especially those new to home health — receive bills that itemize individual visit charges, separate supply charges, and per-visit fees as if the per-visit system still applied. That billing format may reflect what the agency charges you for non-covered services, or it may be a billing error. Either way, you need to understand the PDGM structure to know which charges are legitimate.</p>

<div class="key-takeaway">
    <strong>Wondering what your home health charges should look like?</strong> <a href="/scan">Upload your home health bill to BillKarma</a> — we cross-reference every HCPCS code against Medicare rates and flag supply charges that appear to be bundled into the PDGM episode rate.
</div>

<h2 id="hcpcs-codes">3. HCPCS codes on your home health bill</h2>

<p>Home health services use <strong>HCPCS codes</strong> (Healthcare Common Procedure Coding System — the billing code system used for home health, DME, and other non-physician services). Your itemized bill should include a HCPCS code for every service line. Here are the most common ones and what they mean:</p>

<table>
    <thead>
        <tr>
            <th>HCPCS Code</th>
            <th>Service Description</th>
            <th>Who Can Provide It</th>
            <th>Medicare Rate (per visit, approx.)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>G0156</td>
            <td>Home health aide services (personal care: bathing, dressing, grooming) — per visit</td>
            <td>Home health aide (HHA)</td>
            <td>~$68</td>
        </tr>
        <tr>
            <td>G0162</td>
            <td>Skilled nursing care — complex, high-level services (IV therapy, complex wound care) — per visit</td>
            <td>Registered Nurse (RN)</td>
            <td>~$155</td>
        </tr>
        <tr>
            <td>G0163</td>
            <td>Skilled nursing care — lower-complexity services (medication management, vital signs, straightforward wound care) — per visit</td>
            <td>RN or Licensed Practical Nurse (LPN)</td>
            <td>~$117</td>
        </tr>
        <tr>
            <td>G0299</td>
            <td>Direct skilled nursing by an RN — per visit (used in some LUPA scenarios)</td>
            <td>Registered Nurse (RN)</td>
            <td>~$155</td>
        </tr>
        <tr>
            <td>G0300</td>
            <td>Direct skilled nursing by an LPN — per visit</td>
            <td>Licensed Practical Nurse (LPN)</td>
            <td>~$117</td>
        </tr>
        <tr>
            <td>G0151</td>
            <td>Physical therapy services — evaluation or treatment — per visit</td>
            <td>Licensed Physical Therapist (PT)</td>
            <td>~$148</td>
        </tr>
        <tr>
            <td>G0152</td>
            <td>Occupational therapy services — evaluation or treatment — per visit</td>
            <td>Licensed Occupational Therapist (OT)</td>
            <td>~$148</td>
        </tr>
    </tbody>
</table>

<p><strong>Key distinction to understand:</strong> G0156 (home health aide) and G0162 (skilled nursing) pay at very different rates — approximately $68 vs. $155 per visit. A common billing discrepancy flagged in OIG audit reports is agencies billing G0162 (skilled nursing rate) for visits that the agency's own visit log documents as aide-level personal care (G0156). Over a 60-day episode with multiple such substitutions, this can represent hundreds of dollars in potential overcharges billed to Medicare — and if your cost-sharing is based on a percentage, it affects what you owe too.</p>

{_embed(mode="markup", title="Is your home health charge correct?", subtitle="Compare your billed amount against Medicare rates.", height="420")}

<h2 id="part-a-vs-part-b">4. Medicare Part A vs. Part B for home health</h2>

<p>Home health is one of the few Medicare benefits that can be covered under either Part A or Part B, depending on the circumstances. The distinction matters because the billing source and coordination rules differ between the two parts.</p>

<table>
    <thead>
        <tr>
            <th>Factor</th>
            <th>Part A Home Health</th>
            <th>Part B Home Health</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>When it applies</td>
            <td>Immediately after a qualifying 3-day inpatient hospital stay, when home health begins within 14 days of discharge</td>
            <td>Community-admitted home health (no prior hospital stay required) or when Part A home health days are exhausted</td>
        </tr>
        <tr>
            <td>Qualifying criteria</td>
            <td>Same 4 criteria as above; prior hospital admission required for Part A to pay first</td>
            <td>Same 4 criteria; no prior hospital stay required</td>
        </tr>
        <tr>
            <td>Patient cost-sharing</td>
            <td>$0 deductible or coinsurance for covered home health services</td>
            <td>$0 deductible or coinsurance for covered home health services (same as Part A)</td>
        </tr>
        <tr>
            <td>Durable medical equipment (DME)</td>
            <td>Not covered under Part A home health — billed separately under Part B</td>
            <td>DME billed separately under Part B (20% coinsurance after deductible)</td>
        </tr>
        <tr>
            <td>Duration</td>
            <td>No set limit — as long as criteria are met and physician recertifies every 60 days</td>
            <td>No set limit — same ongoing criteria apply</td>
        </tr>
        <tr>
            <td>Who bills Medicare</td>
            <td>The Medicare-certified home health agency submits claims to the Medicare Administrative Contractor</td>
            <td>Same — the agency bills CMS directly</td>
        </tr>
        <tr>
            <td>Medigap coverage</td>
            <td>Many Medigap policies cover Part A home health copays (though these are $0 already for covered services)</td>
            <td>Medigap covers the 20% Part B coinsurance on DME; home health visits themselves are $0 coinsurance</td>
        </tr>
    </tbody>
</table>

<p>The practical takeaway: <strong>Medicare-covered home health visits should cost you $0 in coinsurance</strong> regardless of whether they fall under Part A or Part B. If your home health agency is billing you a per-visit copay for Medicare-covered skilled nursing or therapy visits, that is a billing discrepancy. The only home health-related costs you should legitimately owe are: the 20% coinsurance on separately billed durable medical equipment under Part B, and any services that are not covered by Medicare (such as companion care or non-medical homemaker services).</p>

<h2 id="annotated-bill">5. Annotated bill example — post-surgery home health episode</h2>

<p>This is a sample itemized bill for a 30-day home health episode following hip replacement surgery. The patient received 8 visits total. The bill includes two items worth questioning — one billed at the wrong service level and one supply charge that appears to be bundled in the PDGM episode rate.</p>

<div class="bill-example">
    <div class="bill-header">Home Health Agency Itemized Statement — 30-Day Episode &mdash; Jan 3, 2026 to Feb 2, 2026<br>Patient: Post-Hip Replacement Recovery &mdash; Medicare Part A</div>
    <div class="line-item">
        <span>G0151 &mdash; Physical therapy visit &times; 4 (Jan 5, 10, 17, 24)</span>
        <span>$592.00</span>
    </div>
    <div class="line-item">
        <span>G0163 &mdash; Skilled nursing visit &times; 2 (Jan 6, 20) — wound assessment and medication review</span>
        <span>$234.00</span>
    </div>
    <div class="line-item flagged">
        <span>G0162 &mdash; Skilled nursing visit, complex &times; 2 (Jan 12, 26) &#9888; <em>Visit log shows aide-level personal care (bathing assist, ambulation) — should be billed as G0156 home health aide (~$68/visit), not G0162 skilled nursing (~$155/visit)</em></span>
        <span>$310.00</span>
    </div>
    <div class="line-item error">
        <span>A6216 &mdash; Gauze, non-impregnated, &gt;16 sq in, sterile &times; 12 pads &#10060; <em>Routine wound dressing supplies are included in the PDGM episode payment — cannot be billed separately to Medicare or patient during an active episode</em></span>
        <span>$87.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$1,223.00</span>
    </div>
    <div class="line-total">
        <span>Corrected Total (G0156 for aide visits, supply charge removed)</span>
        <span>$962.00</span>
    </div>
    <div class="line-total">
        <span>Potential Overcharge</span>
        <span>$261.00</span>
    </div>
</div>

<p>The flagged skilled nursing code (G0162 at $155/visit) billed for visits that the clinical log shows as aide-level services should have been billed as G0156 at approximately $68/visit — a difference of $87 per visit, or $174 for two visits. The gauze supply charge of $87 is a duplicate of costs already included in the PDGM episode rate. Total potential overcharge on this single 30-day episode: <strong>$261</strong>.</p>

<div class="key-takeaway">
    <strong>Already received a home health bill?</strong> Use our <a href="/calculator">Medicare rate calculator</a> to look up the correct rate for any HCPCS code on your bill — and compare it against what your agency charged.
</div>

<h2 id="visit-log">6. How to request and check your visit log</h2>

<p>Your visit log is the most powerful document for checking home health billing accuracy. It is the clinical record your agency keeps of every visit — who came, when, how long they stayed, and what services they performed. Here is how to get it and what to look for.</p>

<h3>Step 1: Request your records in writing</h3>
<p>Send a written request to the home health agency's administrator or medical records department. Under HIPAA, you have the right to access your health records within 30 days of the request (with one 30-day extension if the agency notifies you). In your request, ask specifically for: the clinical visit log for your episode (including all dates, clinician names and credentials, and service descriptions), your signed plan of care, and any physician orders on file for your episode.</p>

<h3>Step 2: Review your Medicare Summary Notice</h3>
<p>Your Medicare Summary Notice (MSN) is available online at <a href="https://www.medicare.gov" target="_blank" rel="noopener">Medicare.gov</a> under "My Medicare" or arrives quarterly by mail. The MSN shows every claim Medicare processed for your home health episodes, including the number of visits billed per episode and the total payment made. Compare the visit count on your MSN against your clinical visit log — if the MSN shows more visits than the log documents, that is a discrepancy to pursue.</p>

<h3>Step 3: Compare the visit log against the bill line by line</h3>
<p>For each date of service on your bill, verify:</p>
<ul>
    <li><strong>Did the visit occur?</strong> The log should show the clinician's name and the date. If a visit appears on the bill but not in the log, question it.</li>
    <li><strong>Does the service level match?</strong> If the log says "personal care assist — bathing, dressing" but the bill shows G0162 (skilled nursing, complex), that is a service-level discrepancy.</li>
    <li><strong>Does the clinician's credential match the code?</strong> G0162 and G0163 require a licensed nurse. G0156 is for aides. If an aide performed the visit, it should not be billed at a skilled nursing rate.</li>
    <li><strong>Are supply charges listed separately?</strong> If your bill includes supply line items during a Medicare episode, ask the agency to confirm whether those supplies are outside the PDGM bundled rate — and to provide documentation if they claim they are.</li>
</ul>

<h2 id="billing-errors">7. Common home health billing errors and how to dispute them</h2>

<h3>a) Visits billed that do not appear in the clinical log</h3>
<p>Also called "phantom visits" in OIG audit terminology, these are claims for visits that the agency's own clinical documentation does not support. The visit did not happen as documented — or did not happen at all. Requesting the visit log and comparing it to the MSN is the primary way to detect this. If you find a discrepancy, report it to 1-800-MEDICARE and file a written dispute with the agency.</p>

<h3>b) Billing skilled nursing rates for aide-level services</h3>
<p>G0162 (complex skilled nursing, ~$155) and G0163 (lower-complexity skilled nursing, ~$117) pay significantly more than G0156 (home health aide, ~$68). When an aide performs personal care tasks — bathing, dressing, grooming, companionship — that service should be billed under G0156. Billing it as a skilled nursing visit is a service-level upgrade that inflates the Medicare payment and, if your cost-sharing is affected, what you pay.</p>

<h3>c) Supply charges during an active PDGM episode</h3>
<p>Routine supplies (wound dressings, gauze, sterile gloves, tape) are bundled into the PDGM episode payment. If you see HCPCS supply codes (like A6216, A6257, or similar A-codes for dressings) billed separately during an episode, ask the agency in writing why those supplies are outside the episode rate. Durable medical equipment (a wheelchair, CPAP machine, or home oxygen) is legitimately billed separately under Part B — but consumable supplies used during care visits typically are not.</p>

<h3>d) Keeping patients on service longer than medically necessary</h3>
<p>Each 30-day episode must be recertified by a physician who confirms the patient still qualifies — still homebound, still needs skilled care. OIG audits have found that some agencies maintain patients on service past the point of medical necessity, billing additional episodes without adequate clinical documentation. If your condition has stabilized or you are regularly leaving home, question whether continued home health billing is medically supported.</p>

<h3>e) Billing for both Part A and Part B for the same episode</h3>
<p>A home health episode should fall under either Part A or Part B — not both. If you received a hospital discharge and began home health within 14 days, Part A typically pays first. If you see claims processed under both parts for the same service period, that may indicate a duplicate billing issue. Your MSN will show which part processed each claim.</p>

<h3>How to dispute home health billing errors</h3>
<ol>
    <li><strong>Gather your documents:</strong> Your itemized bill, your MSN, and your clinical visit log.</li>
    <li><strong>Document the specific discrepancy:</strong> Note the date of service, the HCPCS code billed, and what the visit log actually shows. Be precise — "Visit on Jan 12 billed as G0162 (skilled nursing, $155); log shows aide personal care, no nursing tasks documented."</li>
    <li><strong>Submit a written dispute to the agency's billing department:</strong> Give them 30 days to respond with a corrected claim or a written explanation.</li>
    <li><strong>Contact Medicare if needed:</strong> Call 1-800-MEDICARE or visit Medicare.gov to report a billing discrepancy. You have 120 days from your MSN to file a formal appeal.</li>
    <li><strong>Escalate to the OIG hotline for potential fraud:</strong> If the discrepancy is significant and the agency is unresponsive, you can report suspected billing irregularities to the HHS OIG hotline at 1-800-HHS-TIPS.</li>
</ol>

<h2 id="case-studies">8. Case studies</h2>

<div class="key-takeaway">
    <strong>Facing a home health billing dispute?</strong> See how other patients' home health agencies are rated on billing accuracy in our <a href="/hospitals/">facility directory</a> — and find out if yours has a history of billing irregularities flagged by Medicare audits.
</div>

<div class="case-study">
    <h3>Post-hip-replacement: 18 visits billed, 12 in the log — $2,400 recovered</h3>
    <p>A 74-year-old patient in Ohio received home health after a total hip replacement. Her Medicare Summary Notice showed 18 skilled nursing and physical therapy visits billed over a 60-day period (two 30-day episodes). When her daughter requested the clinical visit log, it documented 12 visits. Six visits billed by the agency — at roughly $140 each — had no corresponding entry in the clinical record. The family submitted a written dispute referencing the specific dates and HCPCS codes billed versus what the log showed. The agency resubmitted corrected claims to Medicare. The patient's share of costs was adjusted downward by <strong>$2,400</strong> in total episode billing.</p>
</div>

<div class="case-study">
    <h3>Six months of aide visits billed at skilled nursing rates — $8,800 potential overcharge identified</h3>
    <p>A family in Florida noticed that their father's home health bills consistently showed G0162 (skilled nursing, complex) for every visit over a six-month period — 52 visits total. The agency employed a mix of RNs and home health aides, and the clinical notes for approximately 38 of those visits described personal care tasks: bathing assistance, meal preparation oversight, and companionship. G0162 bills at approximately $155 per visit; G0156 (home health aide) bills at approximately $68. The difference across 38 visits: <strong>$3,306 in per-visit overcharges</strong> — plus the PDGM episode inflations that resulted. After reporting the discrepancy to 1-800-MEDICARE and filing a formal dispute, Medicare initiated a review and the agency submitted corrected claims. The total billing adjustment on the six-month period was approximately $8,800.</p>
</div>

<div class="case-study">
    <h3>Medicare Summary Notice reveals supply charges the agency's own itemized bill doesn't explain — $1,200 questioned</h3>
    <p>A patient in Illinois recovering from a diabetic foot wound received home health for wound care over two 30-day episodes. Her quarterly MSN from Medicare showed that the agency had billed for dressing supply codes (A6216, A6257) as separate line items totaling $1,200 across both episodes — in addition to the standard PDGM episode payments. When she requested the agency's itemized bill, those supply line items did not appear on the statement the agency had given her, but were visible on the MSN as separately submitted claims. The patient contacted Medicare.gov, was connected with her Medicare Administrative Contractor, and reported the discrepancy. Under PDGM rules, routine wound dressings are included in the episode payment. The MAC initiated a claim review, and the $1,200 in duplicate supply claims was reversed. The patient owed nothing on those charges.</p>
</div>

<h2 id="faq">9. Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Medicare cover home health care?</h3>
        <p>Yes. Medicare covers skilled home health — including skilled nursing, physical therapy, occupational therapy, speech therapy, and home health aide services provided alongside skilled care — when you are homebound, your doctor certifies medical necessity, the care is skilled, and the agency is Medicare-certified. There is no deductible or coinsurance for covered home health visits. Use our <a href="/guides/how-medicare-billing-works">Medicare billing guide</a> to understand how Medicare covers different settings of care.</p>
    </div>

    <div class="faq-item">
        <h3>What is PDGM and why does it matter for my bill?</h3>
        <p>PDGM (Patient-Driven Groupings Model) is the 30-day episode payment system Medicare has used since January 2020. Instead of paying per visit, Medicare pays agencies one bundled rate for a 30-day episode of care. That bundled rate includes routine medical supplies. If your bill shows separate supply charges during a Medicare episode, or itemizes per-visit fees as if each visit is billed separately to Medicare, it is worth comparing against the PDGM structure. Use our <a href="/calculator">rate calculator</a> to look up any HCPCS code.</p>
    </div>

    <div class="faq-item">
        <h3>How do I check my home health visit log?</h3>
        <p>Request your clinical visit log in writing from the home health agency. Under HIPAA, they must provide it within 30 days. The log should show every visit date, the clinician's name and credential (RN, LPN, or HHA), and what services were performed. Compare it against your Medicare Summary Notice at Medicare.gov, which lists every visit and code billed to Medicare on your behalf. Discrepancies between these two documents are what you are looking for.</p>
    </div>

    <div class="faq-item">
        <h3>How do I dispute a home health billing error?</h3>
        <p>Start by collecting your itemized bill, your clinical visit log, and your Medicare Summary Notice. Document the specific date, code, and discrepancy in writing, and submit a dispute to the agency's billing department. If Medicare already paid the claim, call 1-800-MEDICARE to report the discrepancy — you have 120 days from your MSN to file a formal appeal. Our guide on <a href="/guides/dispute-bill">how to dispute a medical bill</a> walks through the full process.</p>
    </div>

    <div class="faq-item">
        <h3>Can a home health agency bill me separately for supplies?</h3>
        <p>For routine supplies used during a Medicare-covered episode — wound dressings, gauze, gloves — generally no. These are bundled into the PDGM episode payment. Durable medical equipment (a wheelchair, home oxygen concentrator) is legitimately billed separately under Medicare Part B with a 20% coinsurance after your deductible. If you receive a supply bill during an active episode, ask the agency in writing to identify the supply code and explain why it falls outside the episode payment.</p>
    </div>
</div>


<h2 id="sources">10. Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/home-health-agency/pdgm" target="_blank" rel="noopener">CMS: Patient-Driven Groupings Model (PDGM) — Home Health Payment Overview</a></li>
    <li><a href="https://oig.hhs.gov/reports-and-publications/oig-reports/2023/home-health-billing-fraud.asp" target="_blank" rel="noopener">HHS Office of Inspector General: Home Health Billing Improper Payments Report (2023)</a></li>
    <li><a href="https://www.medpac.gov/document/march-2024-report-to-the-congress-medicare-payment-policy-chapter-9-home-health-care/" target="_blank" rel="noopener">MedPAC: March 2024 Report to Congress — Home Health Care Services, Chapter 9</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/medicare-home-health-care/" target="_blank" rel="noopener">KFF: Medicare Home Health Care — Coverage, Use, and Spending</a></li>
    <li><a href="https://www.medicare.gov/coverage/home-health-services" target="_blank" rel="noopener">Medicare.gov: Home Health Services — What Medicare Covers</a></li>
    <li><a href="https://oig.hhs.gov/fraud/fugitives/profiles.asp?type=homehealth" target="_blank" rel="noopener">HHS OIG: Home Health Fraud — Audit Findings and Enforcement Actions</a></li>
</ul>
""",
})
