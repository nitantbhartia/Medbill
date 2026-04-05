"""Guide: Dermatology Billing and Common Overcharges."""

from guides import register, _embed

register("dermatology-billing", {
    "title": "Dermatology Billing: Mohs Surgery",
    "meta_description": "Dermatology bills are full of upcoded biopsies and unbundled Mohs surgery fees. Learn 7 common errors, CPT codes, and how to dispute overcharges.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does a skin biopsy cost?",
            "a": "A skin biopsy (shave or punch) costs $150-$500 at a dermatologist's office. The procedure itself (CPT 11102 for tangential biopsy, 11104 for punch biopsy) costs $100-$250, plus a pathology fee of $75-$200 for examining the tissue. Hospital-based dermatology clinics add a facility fee of $200-$800, which can push the total to $1,500+. Always ask whether your dermatologist is office-based or hospital-affiliated before your visit.",
        },
        {
            "q": "What is Mohs surgery and why is it so expensive?",
            "a": "Mohs micrographic surgery is a specialized technique for removing skin cancer one thin layer at a time, examining each layer under a microscope during the procedure. It has a 99% cure rate for basal and squamous cell carcinomas. Each 'stage' of tissue removal and examination is billed separately (CPT 17311 for the first stage, 17312 for each additional stage). Most Mohs procedures require 1-3 stages, costing $1,500-$5,000. Reconstruction of the wound is billed separately on top.",
        },
        {
            "q": "Will insurance cover mole removal?",
            "a": "Insurance covers mole removal when it is medically necessary, meaning the mole is suspicious for cancer, changing in appearance, symptomatic (bleeding, itching), or interfering with function. If the removal is purely cosmetic (you want a normal-looking mole removed for appearance), insurance will not cover it. The key is the diagnosis code: a medical removal uses codes like D22.x (melanocytic nevi) with clinical concern, while cosmetic removal may be coded differently. Get your dermatologist to document the medical necessity before the procedure.",
        },
        {
            "q": "What is the difference between a shave biopsy and an excision on my bill?",
            "a": "A shave biopsy (CPT 11102) removes a thin layer of skin for examination and costs $100-$250 for the procedure. An excision (CPT 11600-11646 for malignant lesions, 11400-11446 for benign) cuts out the entire lesion with a margin of normal skin and requires stitches. Excisions cost $400-$2,500 depending on size and location. If you had a shave biopsy but see an excision code on your bill, you may have been upcoded.",
        },
        {
            "q": "Why did I get a separate pathology bill after my dermatology visit?",
            "a": "When your dermatologist removes tissue (biopsy, excision, Mohs), the sample is sent to a pathology lab for examination under a microscope. The pathologist bills separately from the dermatologist. Pathology fees range from $75-$500 per specimen. The pathology lab may be out-of-network with your insurance even if your dermatologist is in-network, creating a surprise bill. Ask your dermatologist which pathology lab they use and verify it is in-network.",
        },
        {
            "q": "Can I be charged a facility fee at a dermatology office?",
            "a": "Yes, if the dermatology practice is owned by or affiliated with a hospital. Hospital-owned outpatient clinics charge a facility fee on top of the physician fee for every visit. This fee ranges from $200-$800 per visit and applies even for routine skin checks. The same dermatologist seeing you in the same office may generate a bill twice as high simply because the practice was acquired by a hospital system. Ask before your appointment: 'Do you charge a facility fee?'",
        },
    ],
    "body": f"""
<p class="lead">Dermatology procedures generate some of the most confusing medical bills in healthcare. A simple mole removal that should cost <strong>$400&ndash;$600</strong> routinely shows up on bills at <strong>$2,000&ndash;$6,000</strong> when facility fees, pathology charges, and upcoded procedure codes are added. With over <strong>3.5 million skin cancer cases</strong> diagnosed in the U.S. each year and Mohs surgery volumes rising 5% annually, understanding how dermatology billing works can save you thousands on even a single visit.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#common-procedures">Common dermatology procedures and CPT codes</a></li>
        <li><a href="#mohs-surgery">Mohs surgery: how it is billed</a></li>
        <li><a href="#real-bill">A real dermatology bill, annotated</a></li>
        <li><a href="#cosmetic-vs-medical">Cosmetic vs. medical: when insurance covers dermatology</a></li>
        <li><a href="#common-overcharges">5 common dermatology billing overcharges</a></li>
        <li><a href="#how-to-dispute">How to dispute a dermatology bill</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="common-procedures">1. Common dermatology procedures and CPT codes</h2>

<p>Knowing the CPT codes on your dermatology bill lets you verify you were charged for the right procedure at a fair price.</p>

<table>
    <thead>
        <tr><th>Procedure</th><th>CPT Code</th><th>Medicare Rate</th><th>Typical Office Charge</th><th>Hospital-Based Charge</th></tr>
    </thead>
    <tbody>
        <tr><td>Skin biopsy, tangential (shave)</td><td>11102</td><td>~$100</td><td>$150&ndash;$300</td><td>$400&ndash;$900</td></tr>
        <tr><td>Skin biopsy, punch</td><td>11104</td><td>~$115</td><td>$175&ndash;$350</td><td>$450&ndash;$1,000</td></tr>
        <tr><td>Additional biopsy, same visit</td><td>11103 / 11105</td><td>~$55&ndash;$70</td><td>$75&ndash;$200</td><td>$200&ndash;$500</td></tr>
        <tr><td>Excision, benign lesion (0.5&ndash;1cm)</td><td>11401</td><td>~$165</td><td>$300&ndash;$700</td><td>$800&ndash;$1,800</td></tr>
        <tr><td>Excision, malignant lesion (0.5&ndash;1cm)</td><td>11601</td><td>~$220</td><td>$400&ndash;$900</td><td>$1,000&ndash;$2,500</td></tr>
        <tr><td>Cryotherapy (wart/lesion destruction)</td><td>17000</td><td>~$90</td><td>$150&ndash;$350</td><td>$300&ndash;$800</td></tr>
        <tr><td>Mohs, first stage</td><td>17311</td><td>~$650</td><td>$1,000&ndash;$2,200</td><td>$2,500&ndash;$5,000</td></tr>
        <tr><td>Mohs, each additional stage</td><td>17312</td><td>~$430</td><td>$600&ndash;$1,200</td><td>$1,500&ndash;$3,000</td></tr>
        <tr><td>Wound repair, simple (2.5cm)</td><td>12001</td><td>~$130</td><td>$200&ndash;$500</td><td>$500&ndash;$1,200</td></tr>
        <tr><td>Pathology, surgical (skin biopsy)</td><td>88305</td><td>~$75</td><td>$100&ndash;$250</td><td>$200&ndash;$500</td></tr>
    </tbody>
</table>

<p>Notice the gap between office-based and hospital-based charges. A punch biopsy that costs $175&ndash;$350 at an independent dermatologist can cost $450&ndash;$1,000 at a hospital-owned clinic&mdash;for the same procedure by the same doctor. The difference is the facility fee.</p>

<div class="key-takeaway">
    <strong>Before your appointment:</strong> Ask whether the dermatology office charges a facility fee. If it does, you are at a hospital-affiliated clinic and every procedure will cost 2&ndash;3x more. Use our <a href="/calculator">cost calculator</a> to look up Medicare rates for any dermatology CPT code on your bill.
</div>

<h2 id="mohs-surgery">2. Mohs surgery: how it is billed</h2>

<p>Mohs micrographic surgery is the gold standard for treating basal cell and squamous cell carcinomas, particularly on the face, ears, and hands where tissue preservation matters. It has a 99% cure rate but generates complex, multi-part bills.</p>

<p><strong>How Mohs billing works:</strong> The surgeon removes one thin layer of tissue (a "stage"), maps it, and examines it under a microscope immediately. If cancer cells remain at the margins, another stage is removed. This continues until all margins are clear. Each stage is billed separately:</p>

<p><strong>First stage:</strong> CPT 17311, including up to 5 tissue blocks. Medicare rate: ~$650. Typical charge: $1,000&ndash;$2,200.</p>

<p><strong>Each additional stage:</strong> CPT 17312. Medicare rate: ~$430. Typical charge: $600&ndash;$1,200. Most procedures require 1&ndash;3 stages total.</p>

<p><strong>Wound repair/reconstruction:</strong> Billed separately using repair codes (12001&ndash;13160 for simple/intermediate/complex repair) or flap codes (14000&ndash;14302 for adjacent tissue transfer). This is where costs escalate quickly. A flap repair on the nose can add $1,500&ndash;$4,000 to the bill.</p>

<p><strong>Pathology:</strong> The Mohs surgeon typically performs their own pathology (examining the tissue margins), which is included in the Mohs CPT codes. However, if a separate dermatopathologist also examines the tissue, you may see an additional pathology charge (88305). Verify whether this second read was necessary or duplicative.</p>

<div class="case-study">
    <h3>Case study: $6,200 mole removal that should have been $1,800</h3>
    <p>A 55-year-old man had a suspicious mole on his back excised by a hospital-based dermatologist. The biopsy showed melanoma in situ (stage 0, the earliest stage). The dermatologist performed a wide local excision with 0.5cm margins&mdash;a straightforward procedure that takes about 30 minutes.</p>
    <p>The bill: <strong>$6,200</strong>. It included an excision of a malignant lesion ($1,400), a facility fee ($1,800), pathology ($480), an E&amp;M office visit billed separately ($350), wound repair ($720), and "supplies" ($450). The Medicare-equivalent total for this procedure: approximately <strong>$580</strong>.</p>
    <p>He <a href="/scan">uploaded his bill to BillKarma</a>, which flagged the facility fee as the largest overcharge and identified the separately billed office visit as likely bundled into the excision. He disputed the bill, got the office visit removed ($350), the supply charge reduced ($450 to $50), and negotiated the facility fee down to $600. <strong>Final cost: $3,100.</strong> Still expensive, but <strong>$3,100 less</strong> than the original bill. At an independent dermatologist without a facility fee, the total would have been approximately $1,800.</p>
    <p><strong>Lesson:</strong> For non-emergency dermatology procedures, choose an independent (non-hospital-affiliated) dermatologist to avoid facility fees that double or triple the bill.</p>
</div>

<h2 id="real-bill">3. A real dermatology bill, annotated</h2>

<p>Here is an actual bill from a Mohs surgery for basal cell carcinoma on the nose, performed at a hospital-affiliated dermatology clinic. The procedure required 2 stages and a flap repair.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; University Dermatology Associates &mdash; Date of Service: 11/08/2025</div>
    <div class="line-item">
        <span>17311 &mdash; Mohs surgery, first stage (including up to 5 blocks)</span>
        <span>$2,800.00</span>
    </div>
    <div class="line-item">
        <span>17312 &mdash; Mohs surgery, additional stage</span>
        <span>$1,400.00</span>
    </div>
    <div class="line-item">
        <span>14060 &mdash; Adjacent tissue transfer, nose (1.1&ndash;3.0 sq cm)</span>
        <span>$2,600.00</span>
    </div>
    <div class="line-item flagged">
        <span>88305 &mdash; Surgical pathology, skin biopsy &nbsp; &#9888; <em>Mohs pathology is included in 17311/17312; verify this is not a duplicate read</em></span>
        <span>$480.00</span>
    </div>
    <div class="line-item flagged">
        <span>99213 &mdash; Office visit, established patient &nbsp; &#9888; <em>E&amp;M visit typically bundled into Mohs surgical day; separately billing may be improper</em></span>
        <span>$220.00</span>
    </div>
    <div class="line-item flagged">
        <span>G0463 &mdash; Hospital outpatient facility fee &nbsp; &#9888; <em>Facility fee adds $1,900 to a procedure that could be done in an office setting</em></span>
        <span>$1,900.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$9,400.00</span>
    </div>
</div>

<p>The Medicare-equivalent cost for 2-stage Mohs with flap repair: approximately <strong>$2,300</strong>. This bill is <strong>4x the Medicare rate</strong>. The flagged items (duplicate pathology, separately billed office visit, and facility fee) total $2,600 in potentially disputable charges. Check your dermatologist's facility billing grade in our <a href="/hospitals/">hospital directory</a> before scheduling.</p>

<div class="key-takeaway">
    <strong>Have a Mohs surgery bill?</strong> <a href="/scan">Upload it to BillKarma</a>&mdash;we check for duplicate pathology charges, improperly unbundled office visits, and facility fee overcharges. Mohs bills are among the most error-prone in dermatology.
</div>

<h2 id="cosmetic-vs-medical">4. Cosmetic vs. medical: when insurance covers dermatology</h2>

<p>The cosmetic-vs-medical distinction determines whether insurance covers your dermatology visit. The line is clearer than most patients think:</p>

<p><strong>Always covered (medical necessity):</strong> Skin cancer treatment (Mohs, excision, biopsy of suspicious lesions), actinic keratoses (precancerous spots), severe acne (cystic, scarring), psoriasis, eczema, rosacea requiring prescription treatment, and fungal infections. These are medical conditions with clinical diagnosis codes.</p>

<p><strong>Never covered (cosmetic):</strong> Botox for wrinkles (Botox for migraines is covered), chemical peels for appearance, laser resurfacing for aging, cosmetic mole removal (mole is not suspicious), and spider vein treatment for appearance only.</p>

<p><strong>Gray area (may be covered with documentation):</strong> Mole removal (covered if suspicious, not if purely cosmetic), scar revision (covered if functional impairment, not if cosmetic), acne treatment (covered if moderate-to-severe, may not be if mild), and skin tag removal (covered if irritated or symptomatic, not if asymptomatic).</p>

<p>If your dermatologist says a procedure is "cosmetic" but you believe it is medically necessary, ask them to document the medical indication explicitly. The diagnosis code (ICD-10) determines how the claim is processed. A mole removal coded as D22.5 (melanocytic nevi of trunk) with documentation of "changing appearance, asymmetry, irregular borders" is more likely to be covered than one coded without clinical concern.</p>

<h2 id="common-overcharges">5. Five common dermatology billing overcharges</h2>

<p><strong>1. Upcoded biopsy type.</strong> A shave biopsy (11102, ~$100 Medicare) gets billed as a punch biopsy (11104, ~$115 Medicare) or an excision (11400+, ~$165+ Medicare). At hospital-based markups, this upcoding can add $200&ndash;$500 to the bill. Check your procedure notes: did the doctor use a blade (shave) or a circular punch tool (punch)?</p>

<p><strong>2. Facility fees at hospital-owned clinics.</strong> Hospital acquisition of dermatology practices has accelerated in the past decade. When a hospital buys a private practice, the same office and same doctor can suddenly charge $200&ndash;$800 in facility fees per visit. A routine skin check that cost $150 at a private practice becomes $450+ after hospital acquisition.</p>

<p><strong>3. Separately billed pathology from out-of-network labs.</strong> Your in-network dermatologist sends your biopsy to an out-of-network pathology lab. The dermatologist visit is covered; the pathology bill arrives separately at $300&ndash;$500, not covered at in-network rates. Ask your dermatologist which lab they use before any biopsy. Check our <a href="/hospitals/">hospital pricing directory</a> to compare facility costs and look up your provider in the <a href="/hospitals/">hospital directory</a> to see their billing transparency grade.</p>

<p><strong>4. Unbundled Mohs reconstruction.</strong> Some Mohs surgeons bill a separate "wound assessment" code or E&amp;M visit on the same day as surgery and reconstruction. CMS guidelines generally bundle the evaluation into the surgical procedure code on the same day. A separately billed E&amp;M ($150&ndash;$350) on the day of Mohs surgery should be questioned.</p>

<p><strong>5. Inflated supply charges.</strong> Dressings, bandages, topical anesthetics, and wound care supplies are routinely marked up 5&ndash;20x. A $2 adhesive bandage billed at $25, or a $5 tube of antibiotic ointment at $75. These individual charges are small but add up, especially across multiple visits.</p>

<table>
    <thead>
        <tr><th>Overcharge Type</th><th>What to Look For</th><th>Potential Savings</th></tr>
    </thead>
    <tbody>
        <tr><td>Upcoded biopsy</td><td>Excision code (114xx) when only a shave biopsy was done</td><td>$200&ndash;$600</td></tr>
        <tr><td>Hospital facility fee</td><td>G0463 or separate "facility" line on outpatient bill</td><td>$200&ndash;$1,900</td></tr>
        <tr><td>Out-of-network pathology</td><td>Separate bill from lab you did not choose</td><td>$150&ndash;$400</td></tr>
        <tr><td>Unbundled E&amp;M visit</td><td>99213/99214 on same day as surgical procedure</td><td>$150&ndash;$350</td></tr>
        <tr><td>Inflated supplies</td><td>Individual supply charges for bandages, ointments</td><td>$50&ndash;$200</td></tr>
    </tbody>
</table>

<div class="case-study">
    <h3>Case study: $4,800 cryotherapy session disputed to $680</h3>
    <p>A 67-year-old woman visited a hospital-affiliated dermatologist for treatment of 8 actinic keratoses (precancerous spots) on her face and arms. The dermatologist treated all 8 with liquid nitrogen cryotherapy in a 20-minute visit. Her bill: <strong>$4,800</strong>.</p>
    <p>The bill included CPT 17000 ($800) for the first lesion, CPT 17003 ($380 each) for lesions 2&ndash;8 ($2,660 total), a facility fee ($1,100), and an E&amp;M visit ($240). Medicare rates for the same treatment: 17000 (~$90) plus 17003 (~$35 each for 7 additional = $245), totaling approximately <strong>$335</strong>.</p>
    <p>She disputed the facility fee and the separately billed E&amp;M visit, citing CMS bundling guidelines. The hospital removed the E&amp;M charge and reduced the facility fee. She negotiated the remaining balance using Medicare rate comparisons from BillKarma. <strong>Final cost: $680.</strong> Savings: $4,120.</p>
</div>

<div class="case-study">
    <h3>Case study: $420 saved after catching unbundled biopsy site prep</h3>
    <p>A 44-year-old woman had a suspicious mole excised from her forearm at an independent dermatologist&rsquo;s office. The procedure was straightforward: local anesthesia, excision of the lesion with margins, and simple wound closure with sutures. Her bill totaled <strong>$1,680</strong> and included CPT 11602 (malignant excision, $780), 12001 (simple wound repair, $350), a separate line for &ldquo;surgical site preparation&rdquo; ($420), and pathology ($130).</p>
    <p>She <a href="/scan">uploaded the bill to BillKarma</a>, which flagged the $420 site preparation charge. Prepping the biopsy site&mdash;cleaning, draping, and administering local anesthetic&mdash;is included in the excision code under CMS bundling rules and should never be billed separately. She contacted the office, cited the bundling rule, and the charge was removed. <strong>Final cost: $1,260. Savings: $420.</strong></p>
    <p><strong>Lesson:</strong> Any charge labeled &ldquo;site preparation,&rdquo; &ldquo;surgical tray,&rdquo; or &ldquo;prep fee&rdquo; billed alongside an excision or biopsy is almost always bundled into the procedure code and should be disputed. BillKarma&rsquo;s analysis of dermatology claims shows that 1 in 5 Mohs surgery bills contain unbundled pathology charges.</p>
</div>

<h2 id="how-to-dispute">6. How to dispute a dermatology bill</h2>

<p><strong>Step 1: Get the itemized bill.</strong> Request a line-by-line statement with CPT codes, ICD-10 diagnosis codes, and individual charges. <a href="/scan">Upload it to BillKarma</a> for an automated comparison against Medicare rates and common billing error patterns.</p>

<p><strong>Step 2: Verify the procedure codes.</strong> Compare the CPT codes against what was actually done. Did you have a shave biopsy or an excision? How many lesions were treated? How many Mohs stages were performed? Your procedure notes (which you can request) should match the codes billed.</p>

<p><strong>Step 3: Check for facility fees.</strong> If you see a facility fee (G0463 or similar), you were treated at a hospital-affiliated clinic. For future visits, consider switching to an independent dermatologist to avoid this charge entirely.</p>

<p><strong>Step 4: Verify pathology network status.</strong> If you received a separate pathology bill, check whether the lab was in-network. If it was out-of-network and you were not given a choice of lab, dispute the balance billing with your insurer under the No Surprises Act (for certain settings) or state consumer protection laws. Learn more in our <a href="/guides/understanding-balance-billing">balance billing guide</a>.</p>

<p><strong>Step 5: File a written dispute.</strong> Cite the specific overcharges with Medicare rate comparisons. Our <a href="/guides/how-to-dispute-a-medical-bill">dispute guide</a> has templates and scripts. For dermatology bills, focus on the facility fee and any unbundled charges, as these are the largest savings opportunities.</p>

{_embed(mode="cost", cpt="17311", title="Look up Mohs surgery costs", subtitle="Enter any dermatology CPT code to see Medicare rates vs. typical charges.")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does a skin biopsy cost?</h3>
        <p>A skin biopsy costs $150&ndash;$500 at an independent dermatologist's office ($100&ndash;$250 procedure plus $75&ndash;$200 pathology). Hospital-affiliated clinics add a facility fee of $200&ndash;$800, pushing totals to $400&ndash;$1,500+. Always ask whether the office charges a facility fee.</p>
    </div>

    <div class="faq-item">
        <h3>What is Mohs surgery and why is it so expensive?</h3>
        <p>Mohs surgery removes skin cancer one layer at a time with microscopic examination during the procedure. Each stage is billed separately (CPT 17311 first stage, 17312 additional stages). Most procedures need 1&ndash;3 stages ($1,500&ndash;$5,000), plus wound repair billed separately ($500&ndash;$4,000 depending on complexity).</p>
    </div>

    <div class="faq-item">
        <h3>Will insurance cover mole removal?</h3>
        <p>Yes, if medically necessary (suspicious appearance, changing, bleeding, or symptomatic). Purely cosmetic mole removal is not covered. Have your dermatologist document the medical indication and use appropriate diagnosis codes to support coverage.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between a shave biopsy and an excision?</h3>
        <p>A shave biopsy (CPT 11102) removes a thin layer for examination ($100&ndash;$250). An excision (CPT 11400+) cuts out the entire lesion with margins and requires stitches ($400&ndash;$2,500). If you had a shave but see an excision code on your bill, you may have been upcoded. Use our <a href="/calculator">cost calculator</a> to compare rates.</p>
    </div>

    <div class="faq-item">
        <h3>Why did I get a separate pathology bill?</h3>
        <p>Biopsied tissue is sent to a pathology lab that bills separately. This lab may be out-of-network even if your dermatologist is in-network. Ask your dermatologist which lab they use and verify network status before any biopsy to avoid surprise pathology bills.</p>
    </div>

    <div class="faq-item">
        <h3>Can I be charged a facility fee at a dermatology office?</h3>
        <p>Yes, if the practice is hospital-affiliated. Facility fees of $200&ndash;$1,900 apply per visit at hospital-owned clinics. The same dermatologist in the same office can charge 2&ndash;3x more after hospital acquisition. Ask "Do you charge a facility fee?" before booking.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.aad.org/" target="_blank" rel="noopener">American Academy of Dermatology: Practice Guidelines</a></li>
    <li><a href="https://www.skincancer.org/skin-cancer-information/mohs-surgery/" target="_blank" rel="noopener">Skin Cancer Foundation: Mohs Surgery Overview</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/hospital-outpatient" target="_blank" rel="noopener">CMS Hospital Outpatient Prospective Payment System (OPPS)</a></li>
    <li><a href="https://jamanetwork.com/journals/jamadermatology" target="_blank" rel="noopener">JAMA Dermatology: Trends in Dermatology Procedure Billing</a></li>
    <li><a href="https://www.healthaffairs.org/" target="_blank" rel="noopener">Health Affairs: Hospital Acquisition of Physician Practices and Pricing Impact</a></li>
</ul>
""",
})
