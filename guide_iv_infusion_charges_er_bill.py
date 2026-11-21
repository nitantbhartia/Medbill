"""Guide: IV Charges on an ER Bill: Hydration, Push and Infusion Codes."""

from guides import register

register("iv-infusion-charges-er-bill", {
    "title": "IV Charges on an ER Bill: Hydration, Push and Infusion Codes",
    "meta_description": "IV charges on an ER bill use codes 96360 to 96376. Learn what hydration, push and infusion codes mean, Medicare’s time rules, and how to spot errors.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "What do 96360, 96365 and 96374 mean on my ER bill?",
            "a": "They are the three main “initial” IV codes. 96360 is IV hydration (fluids to treat or prevent dehydration) lasting 31 minutes to 1 hour. 96365 is an IV infusion of a drug for therapy or diagnosis, up to 1 hour. 96374 is an IV push, a single drug given quickly. Medicare’s coding rules allow only one “initial” code per encounter unless separate IV sites were medically necessary.",
        },
        {
            "q": "Can a hospital bill for IV fluids that ran less than 30 minutes?",
            "a": "Not as hydration under Medicare’s rules. Medicare contractor guidance says not to report IV hydration of 30 minutes or less. Fluid used only to keep the IV line open, or to carry a drug into the vein, is also not separately reportable as hydration.",
        },
        {
            "q": "Why is the IV fluid charged on a separate line from the IV code?",
            "a": "The administration codes (96360 to 96376) pay for giving the fluid or drug. The fluid or drug itself is a separate item, often listed under a pharmacy revenue code such as 0258 (IV solutions) or 0636 (drugs requiring detailed coding), sometimes with a J-code. Seeing both is normal. Seeing the same drug twice, or a drug your records do not show, is worth asking about.",
        },
        {
            "q": "What if my records show an IV start time but no stop time?",
            "a": "Medicare contractor guidance expects both start and stop times to be documented. One contractor article says that if the stop time is missing, it should be possible to work it out from the fluid volume, start time and drip rate. If neither the times nor the rate support the hours billed, ask the billing office to explain the add-on hours.",
        },
    ],
    "body": f"""
<p class="lead">IV lines on an ER bill usually come in two parts: a code for <em>giving</em> the fluid or drug (CPT codes 96360 to 96376) and a separate line for the fluid or drug itself. They are billed right when there is only one &ldquo;initial&rdquo; IV code per IV site, the add-on codes match the minutes in your medication record, and hydration that ran at the same time as another drug is not charged separately.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#code-families">The three IV code families</a></li>
        <li><a href="#initial-vs-additional">Initial vs. additional, sequential and concurrent</a></li>
        <li><a href="#time-rules">The time rules</a></li>
        <li><a href="#drug-lines">The fluid and drug lines</a></li>
        <li><a href="#example">Example: checking the math</a></li>
        <li><a href="#common-errors">Common IV billing errors</a></li>
        <li><a href="#what-to-do">What to do: check your bill against your records</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="code-families">1. The three IV code families</h2>

<p>A CPT code (the standard billing code for a medical service) tells the insurer what was done. For IV care, there are three families. Below are the descriptors Medicare contractors publish, in plain words.</p>

<table>
    <thead>
        <tr>
            <th>Code</th>
            <th>What it means</th>
            <th>Type</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>96360</td><td>IV hydration (fluids), initial, 31 minutes to 1 hour</td><td>Initial</td></tr>
        <tr><td>96361</td><td>IV hydration, each additional hour; also used for hydration given after a different initial service</td><td>Add-on</td></tr>
        <tr><td>96365</td><td>IV infusion of a drug for therapy, prevention or diagnosis, initial, up to 1 hour</td><td>Initial</td></tr>
        <tr><td>96366</td><td>IV infusion, each additional hour</td><td>Add-on</td></tr>
        <tr><td>96367</td><td>Additional sequential infusion of a new drug, up to 1 hour</td><td>Add-on</td></tr>
        <tr><td>96368</td><td>Concurrent infusion (a second drug running at the same time)</td><td>Add-on</td></tr>
        <tr><td>96374</td><td>IV push, single or initial drug</td><td>Initial</td></tr>
        <tr><td>96375</td><td>Each additional sequential IV push of a new drug</td><td>Add-on</td></tr>
        <tr><td>96376</td><td>Each additional sequential IV push of the same drug, facilities only</td><td>Add-on</td></tr>
    </tbody>
</table>

<p><strong>Hydration</strong> means fluids like saline given to treat or prevent dehydration. <strong>Infusion</strong> means a drug dripped in over time, such as an IV antibiotic. A <strong>push</strong> is a drug given quickly by syringe. Medicare contractor guidance defines a push as an injection where the nurse or doctor stays with you the whole time, or any infusion of 15 minutes or less.</p>

<p>On an ER visit, these codes belong on the <em>hospital</em> (facility) bill. Medicare&rsquo;s National Correct Coding Initiative (NCCI) manual, the federal rulebook for which codes can be billed together, says doctors should not report these codes for care in a hospital outpatient or emergency department; the hospital reports them. A separate ER doctor bill may show the visit level instead (see <a href="/guides/er-level-5-charge-99285/">what a level 5 ER charge means</a>).</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Count the &ldquo;initial&rdquo; codes on your bill: 96360, 96365 and 96374 (plus the chemotherapy codes 96409 and 96413). If more than one appears for the same visit, ask whether you had two separate IV sites. You can <a href="/scan">check your bill free at BillKarma</a> to see every line compared with what Medicare pays.</p>
</div>

<h2 id="initial-vs-additional">2. Initial vs. additional, sequential and concurrent</h2>

<p>Every IV visit starts with one <strong>initial</strong> service. The NCCI manual (revised January 1, 2026) says only one initial code may be reported per encounter unless it was medically necessary to give drugs through separate IV sites. In that case the hospital adds a modifier (a two-character tag on the code) to the second initial code.</p>

<p>Medicare&rsquo;s Claims Processing Manual (Chapter 4, section 230.2) says hospitals report only one initial drug administration service <em>per vascular access site per encounter</em>, even when an observation stay runs past midnight. A double-lumen catheter (one line with two channels) still counts as one site, so it supports only one initial code.</p>

<h3>Which service counts as &ldquo;initial&rdquo; at a hospital?</h3>

<p>For facility billing, the initial code is not simply whatever happened first. A Medicare contractor billing article from Palmetto GBA says that for facilities, infusion comes first in the order, IV pushes next, and hydration last. So an antibiotic drip can be the initial service even if it came after a push.</p>

<h3>Sequential vs. concurrent</h3>
<ul>
    <li><strong>Sequential</strong> means a new drug given after the initial service, through the same IV (codes 96367, 96375, 96361).</li>
    <li><strong>Concurrent</strong> means a new drug running at the same time as another one (code 96368).</li>
    <li><strong>Hydration at the same time as another drug</strong> is not separately reportable, according to the NCCI manual. If saline ran alongside your antibiotic, the overlap should not appear as a separate hydration charge.</li>
</ul>

<h2 id="time-rules">3. The time rules</h2>

<p>IV codes are based on minutes, so the clock matters. These rules come from Medicare contractor guidance:</p>

<ul>
    <li><strong>Hydration needs more than 30 minutes.</strong> Noridian, a Medicare contractor, says not to report IV hydration of 30 minutes or less. The initial hydration code 96360 covers 31 minutes to 1 hour.</li>
    <li><strong>An infusion needs more than 15 minutes.</strong> Palmetto GBA says that for facility coding, an infusion must be more than 15 minutes. A drug that ran 15 minutes or less is a push.</li>
    <li><strong>An extra hour needs more than 30 extra minutes.</strong> The add-on hour codes (96361 for hydration, 96366 for infusion) can be reported only when the time runs more than 30 minutes past the hour mark. A 75-minute drip is one hour; a 91-minute drip is one hour plus one add-on hour.</li>
    <li><strong>&ldquo;Keep open&rdquo; fluids don&rsquo;t count.</strong> The NCCI manual says add-on hours should not be reported for &ldquo;keep open&rdquo; infusions (a slow drip that keeps the IV line working). Fluid used only for that, or to carry a drug into the vein, is &ldquo;incidental hydration&rdquo; and is not reported separately.</li>
    <li><strong>Times should be written down.</strong> Palmetto GBA expects start and stop times to be documented; a missing stop time should be calculable from the volume, start time and drip rate.</li>
</ul>

<p>Hydration also has to be medically necessary. Noridian says your record should show the signs or symptoms that called for it.</p>

<h2 id="drug-lines">4. The fluid and drug lines</h2>

<p>The 96360&ndash;96376 codes pay for the work of giving the IV. The drug or fluid itself is billed on its own line. On a UB-04 hospital bill (the standard hospital claim form), look for the revenue code, a four-digit number that tells you which department charged it:</p>

<ul>
    <li><strong>0258 &ndash; IV solutions</strong> (saline, dextrose and similar fluids), part of the 025X pharmacy group.</li>
    <li><strong>0636 &ndash; Drugs requiring detailed coding</strong>, often used for injectable drugs listed with a HCPCS code.</li>
    <li><strong>026X &ndash; IV therapy</strong>, which some hospitals use for IV supplies or pump charges.</li>
</ul>

<p>Drug lines often carry a J-code, a HCPCS code for a specific drug and dose. For example, J7030 is &ldquo;Infusion, normal saline solution, 1000 cc.&rdquo; Check that the units match the amount you got: one liter of saline is one unit of J7030, not three. For more on these numbers, see <a href="/guides/hospital-revenue-codes-explained/">hospital revenue codes explained</a> and <a href="/guides/hospital-drug-charges/">hospital drug charges</a>.</p>

<h2 id="example">5. Example: checking the math</h2>

<p><strong>Example:</strong> This is an illustration, not a real patient. One IV in the left arm. The medication administration record (MAR), the nurse&rsquo;s log of every drug and fluid with times, shows:</p>

<ul>
    <li>10:05&ndash;10:45: IV antibiotic infusion (40 minutes)</li>
    <li>10:50: anti-nausea drug by IV push</li>
    <li>10:55&ndash;12:05: 1,000 mL normal saline for dehydration (70 minutes)</li>
</ul>

<table>
    <thead>
        <tr>
            <th>Service</th>
            <th>Lines on the bill</th>
            <th>What the rules support</th>
            <th>Why</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Antibiotic, 40 min</td><td>96365 x1</td><td>96365 x1</td><td>Infusion ranks first for facilities; over 15 minutes, under 1 hour</td></tr>
        <tr><td>Anti-nausea push</td><td>96374 x1</td><td>96375 x1</td><td>A second initial code on the same IV site; this is a sequential push of a new drug</td></tr>
        <tr><td>Saline, 70 min</td><td>96360 x1, 96361 x2</td><td>96361 x1</td><td>Hydration after a different initial service uses 96361. 70 minutes is 1 hour plus 10 minutes, and 10 is not more than 30, so no extra hour</td></tr>
        <tr><td>Saline fluid itself</td><td>0258, J7030 x1</td><td>0258, J7030 x1</td><td>1,000 mL = 1 unit</td></tr>
    </tbody>
</table>

<p>Add up the administration units. The bill shows 1 + 1 + 1 + 2 = 5 units (96365, 96374, 96360 and two of 96361). The record supports 1 + 1 + 1 = 3 units (96365, 96375 and one 96361). That leaves 2 units to question: the extra initial code (96360) and the second hydration hour. The push stays on the bill, but as 96375 instead of 96374.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>You cannot check IV codes without the times. Ask the hospital for an itemized bill and your medication administration record together, then line up each IV code with a start and stop time. Here is <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a>.</p>
</div>

<h2 id="common-errors">6. Common IV billing errors</h2>

<p>Each of these may have an explanation in your chart, so raise them as questions.</p>

<ol>
    <li><strong>More than one initial code.</strong> Two or three of 96360, 96365 and 96374 on one visit with one IV site.</li>
    <li><strong>Hydration billed during another infusion.</strong> Saline running alongside an antibiotic, with the overlap billed as 96360 or 96361.</li>
    <li><strong>Extra hours without the minutes.</strong> 96361 or 96366 billed when the time past the hour was 30 minutes or less, or when no stop time was recorded.</li>
    <li><strong>&ldquo;Keep open&rdquo; drips billed as hydration.</strong> A slow drip to keep the line working is not a hydration service.</li>
    <li><strong>A short drip billed as an infusion.</strong> A drug given in 15 minutes or less should be a push code, not 96365.</li>
    <li><strong>A separate charge for starting the IV.</strong> The NCCI manual says placing a regular (peripheral) IV is part of the infusion or injection codes and is not reported separately.</li>
    <li><strong>Drug unit errors.</strong> J-code units that don&rsquo;t match the dose or volume in your MAR, or a drug listed twice.</li>
</ol>

<p>For other patterns hospitals sometimes get wrong, see <a href="/guides/common-hospital-billing-errors/">common hospital billing errors</a>.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>If your IV codes don&rsquo;t match your medication record, put the question in writing and quote the times. Our <a href="/guides/medical-bill-dispute-letter/">medical bill dispute letter guide</a> shows how to list each line, what the record shows, and what you are asking the hospital to correct.</p>
</div>

<h2 id="what-to-do">7. What to do: check your bill against your records</h2>

<ol>
    <li><strong>Get the itemized bill.</strong> Ask for one with CPT/HCPCS codes, revenue codes and units.</li>
    <li><strong>Request your medication administration record.</strong> Under HIPAA you have the right to a copy of your medical records. Ask for the ER nursing notes and MAR or infusion flowsheet.</li>
    <li><strong>List every IV code.</strong> Write down each code from 96360 to 96376 and how many units were billed.</li>
    <li><strong>Count the initial codes.</strong> More than one of 96360, 96365 or 96374? Check whether the record shows two IV sites.</li>
    <li><strong>Do the time math.</strong> For each drip, subtract the start time from the stop time. Hydration needs more than 30 minutes. An extra hour needs more than 30 minutes past the hour.</li>
    <li><strong>Look for overlaps.</strong> If saline and another drug ran at the same time, the overlapping hydration should not be billed separately.</li>
    <li><strong>Match the drug lines.</strong> Each J-code or 0258/0636 line should match a drug and amount in the MAR.</li>
    <li><strong>Call billing, then follow up in writing.</strong> Ask about specific lines and note who you spoke with. If a bill has gone to collections or a collector has taken you to court, consider talking to a consumer attorney or legal aid.</li>
</ol>

<p>These are Medicare&rsquo;s rules, the clearest public standard for IV coding. Private insurers may apply their own policies, but the CPT codes are the same.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What do 96360, 96365 and 96374 mean on my ER bill?</h3>
        <p>They are the three main &ldquo;initial&rdquo; IV codes. 96360 is IV hydration (fluids to treat or prevent dehydration) lasting 31 minutes to 1 hour. 96365 is an IV infusion of a drug for therapy or diagnosis, up to 1 hour. 96374 is an IV push, a single drug given quickly. Medicare&rsquo;s coding rules allow only one &ldquo;initial&rdquo; code per encounter unless separate IV sites were medically necessary.</p>
    </div>
    <div class="faq-item">
        <h3>Can a hospital bill for IV fluids that ran less than 30 minutes?</h3>
        <p>Not as hydration under Medicare&rsquo;s rules. Medicare contractor guidance says not to report IV hydration of 30 minutes or less. Fluid used only to keep the IV line open, or to carry a drug into the vein, is also not separately reportable as hydration.</p>
    </div>
    <div class="faq-item">
        <h3>Why is the IV fluid charged on a separate line from the IV code?</h3>
        <p>The administration codes (96360 to 96376) pay for giving the fluid or drug. The fluid or drug itself is a separate item, often listed under a pharmacy revenue code such as 0258 (IV solutions) or 0636 (drugs requiring detailed coding), sometimes with a J-code. Seeing both is normal. Seeing the same drug twice, or a drug your records do not show, is worth asking about.</p>
    </div>
    <div class="faq-item">
        <h3>What if my records show an IV start time but no stop time?</h3>
        <p>Medicare contractor guidance expects both start and stop times to be documented. One contractor article says that if the stop time is missing, it should be possible to work it out from the fluid volume, start time and drip rate. If neither the times nor the rate support the hours billed, ask the billing office to explain the add-on hours.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c04.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 4, Section 230.2: Coding and Payment for Drug Administration</a></li>
    <li><a href="https://www.cms.gov/files/document/11-chapter11a-ncci-medicare-policy-manual-2026-final.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare NCCI Policy Manual, Chapter XI: Medicine (revised January 1, 2026)</a></li>
    <li><a href="https://www.cms.gov/medicare-coverage-database/view/article.aspx?articleId=53778" target="_blank" rel="noopener">Palmetto GBA (CMS Medicare Coverage Database) &mdash; Billing and Coding: Infusion, Injection and Hydration Services (A53778)</a></li>
    <li><a href="https://med.noridianmedicare.com/web/jea/topics/drugs-biologicals-injections/hydration" target="_blank" rel="noopener">Noridian Medicare JE Part A &mdash; Hydration</a></li>
    <li><a href="https://med.noridianmedicare.com/web/jeb/topics/drugs-biologicals-injections/chemotherapy-and-nonchemotherapy-bundling-and-unbundling-of-services-and-supplies" target="_blank" rel="noopener">Noridian Medicare JE Part B &mdash; Chemotherapy and Nonchemotherapy: Bundling and Unbundling of Services and Supplies</a></li>
    <li><a href="https://www.cms.gov/Outreach-and-Education/MLN/WBT/MLN7388180-MLN-WBT-1450/1450/lesson05/13/index.html" target="_blank" rel="noopener">CMS MLN &mdash; Medicare Billing: CMS-1450 and 837I, Revenue Codes</a></li>
    <li><a href="https://www.hca.wa.gov/assets/billers-and-providers/hca-rev-grid-20250103.pdf" target="_blank" rel="noopener">Washington State Health Care Authority &mdash; Revenue Code Grid (UB-04 revenue code descriptions)</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/transmittals/2017downloads/r237bp.pdf" target="_blank" rel="noopener">CMS &mdash; Transmittal 237, Pub. 100-02 (HCPCS J7030 descriptor)</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.524" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 164.524, Access of individuals to protected health information</a></li>
</ul>
""",
})
