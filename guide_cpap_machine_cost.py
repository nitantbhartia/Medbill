"""Guide: CPAP Machine Cost & Insurance Coverage Guide (2026)."""

from guides import register, _embed

register("cpap-machine-cost", {
    "title": "CPAP Machine Cost & Insurance Coverage Guide (2026)",
    "meta_description": "CPAP machines cost $500–$1,500. BiPAP costs $800–$3,000. Insurance usually covers CPAP as DME after a sleep study. See 2026 prices, HCPCS codes, and billing errors to watch for.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does a CPAP machine cost in 2026?",
            "a": "A CPAP machine costs $500 to $1,500 without insurance in 2026. The ResMed AirSense 10 and AirSense 11 are the most widely used models and retail for $700 to $1,100. Auto-adjusting CPAP (APAP) machines cost $600 to $1,800, while BiPAP machines range from $800 to $3,000. Buying directly from an online retailer or CPAP specialty site is typically 30 to 50% less expensive than purchasing through a hospital-affiliated DME supplier.",
        },
        {
            "q": "Does insurance cover CPAP machines?",
            "a": "Most commercial insurance plans and Medicare cover CPAP machines as Durable Medical Equipment (DME) when prescribed following a qualifying sleep study that diagnoses obstructive sleep apnea (OSA). Coverage typically requires an Apnea-Hypopnea Index (AHI) of 5 or greater with symptoms, or AHI of 15 or greater regardless of symptoms. You will pay your DME deductible and coinsurance (usually 20%), and many insurers require a 3-month rental period before purchasing outright.",
        },
        {
            "q": "What HCPCS codes are used for CPAP billing?",
            "a": "The primary HCPCS code for CPAP equipment is E0601 (CPAP device). BiPAP devices use E0470 (BiPAP without backup rate) or E0471 (BiPAP with backup rate). Supplies are billed separately: A7030 (full face mask), A7034 (nasal mask), A7037 (tubing), A7038 (disposable filter), A7039 (non-disposable filter). Check your DME supplier&rsquo;s itemized bill for these codes to verify you are being charged for equipment and supplies you actually received.",
        },
        {
            "q": "How does Medicare cover CPAP machines?",
            "a": "Medicare covers CPAP therapy under Part B as DME when an AHI of 5 or greater is documented in a qualifying sleep study. Medicare pays 80% of the approved amount after the Part B deductible. The initial 3 months are covered as a rental. If you continue using the CPAP as documented, Medicare pays for months 4 through 13, after which you own the machine outright. Medicare&rsquo;s approved monthly rental amount for E0601 is approximately $58 to $70 in 2026.",
        },
        {
            "q": "Should I rent or buy a CPAP machine?",
            "a": "If you have insurance, your plan will likely require a 3-month rental period before you can purchase outright&mdash;this is designed to confirm you actually use the therapy before the insurer pays for the full device. If you are paying cash, buying outright is almost always cheaper than renting long-term. A $900 CPAP machine rented at $75 per month costs $900 after 12 months. Buying it upfront avoids the additional monthly billing and potential supply add-ons that DME suppliers routinely add.",
        },
    ],
    "body": f"""
<div class="answer-box">
    <p><strong>Direct answer:</strong> CPAP machines cost <strong>$500 to $1,500</strong> without insurance. BiPAP devices run <strong>$800 to $3,000</strong>. Insurance covers CPAP as DME after a qualifying sleep study&mdash;most patients pay <strong>20% coinsurance</strong> after their deductible. Medicare covers CPAP when AHI &ge;5. BillKarma data shows DME billing errors affect <strong>23% of sleep-related equipment claims</strong>.</p>
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#device-comparison">CPAP, APAP, and BiPAP cost comparison</a></li>
        <li><a href="#supply-costs">Annual CPAP supply costs</a></li>
        <li><a href="#insurance-coverage">How insurance covers CPAP</a></li>
        <li><a href="#medicare-coverage">Medicare coverage and rental rules</a></li>
        <li><a href="#rent-vs-buy">Rental vs. purchase decision</a></li>
        <li><a href="#without-insurance">Buying CPAP without insurance</a></li>
        <li><a href="#hcpcs-codes">CPAP billing codes (HCPCS) explained</a></li>
        <li><a href="#billing-errors">Common CPAP and DME billing errors</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="device-comparison">1. CPAP, APAP, and BiPAP cost comparison</h2>

<p>Sleep apnea therapy devices fall into three main categories. The right device depends on your diagnosis and your physician&rsquo;s recommendation; the price difference is significant.</p>

<table>
    <thead>
        <tr>
            <th>Device Type</th>
            <th>HCPCS Code</th>
            <th>Cash Price Range</th>
            <th>Popular Models</th>
            <th>Best For</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>CPAP (fixed pressure)</td><td>E0601</td><td>$500&ndash;$1,000</td><td>ResMed AirSense 10, AirMini</td><td>Standard OSA</td></tr>
        <tr><td>APAP (auto-adjusting)</td><td>E0601</td><td>$600&ndash;$1,800</td><td>ResMed AirSense 11, DreamStation 2 Auto</td><td>Pressure variability, titration</td></tr>
        <tr><td>BiPAP (two-pressure)</td><td>E0470</td><td>$800&ndash;$2,500</td><td>ResMed AirCurve 10, DreamStation BiPAP</td><td>High pressure needs, COPD overlap</td></tr>
        <tr><td>BiPAP with backup rate</td><td>E0471</td><td>$1,500&ndash;$3,000</td><td>ResMed AirCurve ST, Trilogy 100</td><td>Central sleep apnea, hypoventilation</td></tr>
    </tbody>
</table>

<p>Note that CPAP and APAP devices share the same HCPCS code (E0601). Insurance and Medicare reimburse them at the same rate regardless of which technology the device uses. If your provider prescribes a standard CPAP but bills E0601 for an APAP at a higher price, the reimbursement rate is identical&mdash;but your coinsurance amount may be higher if the device cost is higher.</p>

<p>Estimate your CPAP setup cost with insurance or Medicare:</p>

{_embed(mode="cost", cpt="94660", title="CPAP Setup Cost", subtitle="94660 – CPAP initiation and management")}

<h2 id="supply-costs">2. Annual CPAP supply costs</h2>

<p>The machine itself is a one-time cost, but CPAP therapy requires ongoing supplies. These supplies are covered by insurance and Medicare on replacement schedules, but billing errors in supply replacement are extremely common&mdash;including billing for supplies not shipped.</p>

<table>
    <thead>
        <tr>
            <th>Supply Item</th>
            <th>HCPCS Code</th>
            <th>Cash Price</th>
            <th>Medicare Replacement Schedule</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Full face mask</td><td>A7030</td><td>$60&ndash;$150</td><td>1 per 3 months</td></tr>
        <tr><td>Nasal mask</td><td>A7034</td><td>$30&ndash;$100</td><td>1 per 3 months</td></tr>
        <tr><td>Nasal pillow mask</td><td>A7044</td><td>$25&ndash;$80</td><td>1 per 3 months</td></tr>
        <tr><td>Mask cushion / seal</td><td>A7031 or A7033</td><td>$10&ndash;$40</td><td>2 per month</td></tr>
        <tr><td>Headgear / straps</td><td>A7035</td><td>$10&ndash;$30</td><td>1 per 6 months</td></tr>
        <tr><td>Tubing (6-foot standard)</td><td>A7037</td><td>$10&ndash;$25</td><td>1 per 3 months</td></tr>
        <tr><td>Disposable filter</td><td>A7038</td><td>$1&ndash;$5 each</td><td>2 per month</td></tr>
        <tr><td>Non-disposable filter</td><td>A7039</td><td>$5&ndash;$15</td><td>1 per 6 months</td></tr>
        <tr><td>Heated humidifier chamber</td><td>A7046</td><td>$15&ndash;$40</td><td>1 per 6 months</td></tr>
    </tbody>
</table>

<p>At full replacement frequency, annual supply costs run <strong>$200 to $500</strong> when paying cash. Through insurance, you pay your coinsurance percentage on each item billed. Many DME suppliers auto-ship supplies on the maximum replacement schedule whether or not you need them&mdash;a source of both waste and billing errors.</p>

<h2 id="insurance-coverage">3. How insurance covers CPAP</h2>

<p>Commercial insurance covers CPAP machines under the Durable Medical Equipment (DME) benefit, which typically has separate deductibles and coinsurance from your medical benefit. Key requirements and considerations:</p>

<ul>
    <li><strong>Qualifying sleep study:</strong> You must have a documented sleep study (polysomnography, CPT 95810, or home sleep test, CPT 95806) diagnosing OSA with AHI &ge;5 with symptoms or AHI &ge;15 without symptoms.</li>
    <li><strong>Written prescription:</strong> Your physician must write a prescription specifying the type of PAP device, the prescribed pressure setting, and the diagnosis code (ICD-10 G47.33 for obstructive sleep apnea).</li>
    <li><strong>DME supplier must be in-network:</strong> Using an out-of-network DME supplier can result in little to no insurance coverage. Always verify your supplier is in-network before accepting equipment.</li>
    <li><strong>Prior authorization:</strong> Most plans require prior authorization for CPAP equipment. Your prescribing physician&rsquo;s office typically initiates this process.</li>
    <li><strong>Compliance requirements:</strong> Many insurers require documented compliance (using the CPAP at least 4 hours per night on 70% of nights over 30 consecutive days) before approving continued coverage or purchase. If you do not meet compliance, the insurer may require you to return the device.</li>
</ul>

<h2 id="medicare-coverage">4. Medicare coverage and rental rules</h2>

<p>Medicare Part B covers CPAP therapy under a specific rental-to-purchase pathway. Understanding this pathway prevents unexpected charges:</p>

<ol>
    <li><strong>Month 1&ndash;3 (initial rental):</strong> Medicare pays 80% of the monthly rental rate for E0601 (~$58&ndash;$70/month). You owe 20% coinsurance, approximately $12 to $14 per month.</li>
    <li><strong>Compliance verification at month 3:</strong> Your DME supplier must obtain documentation from your physician that you are using the CPAP and therapy is benefiting you. If compliance is not documented, rental stops and you may need to return the device.</li>
    <li><strong>Months 4&ndash;13 (continued rental):</strong> If compliance is verified, Medicare continues paying rental through month 13.</li>
    <li><strong>Month 13 (ownership transfer):</strong> After 13 months of covered rental, you own the CPAP outright at no additional charge. Medicare no longer pays rental after this point.</li>
    <li><strong>Ongoing supplies:</strong> After ownership transfers, Medicare continues to cover supplies on the standard replacement schedule (E0601 is no longer billed; supply codes continue).</li>
</ol>

<p>Total Medicare rental cost over 13 months: approximately $750 to $910 billed to Medicare, of which you pay 20% coinsurance ($150 to $182) plus your Part B deductible if not already met.</p>

<h2 id="rent-vs-buy">5. Rental vs. purchase decision</h2>

<p>For patients paying cash (no insurance), the rent-vs-buy decision is straightforward: buying outright is almost always cheaper if you intend to use the therapy long-term.</p>

<table>
    <thead>
        <tr>
            <th>Scenario</th>
            <th>12-Month Cost</th>
            <th>24-Month Cost</th>
            <th>Recommendation</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Buy ResMed AirSense 11 outright (cash)</td><td>$1,100 total</td><td>$1,100 total</td><td>Best if using long-term</td></tr>
        <tr><td>Rent through DME supplier (cash)</td><td>$900&ndash;$1,200</td><td>$1,800&ndash;$2,400</td><td>Only if short-term trial</td></tr>
        <tr><td>With insurance (20% coinsurance)</td><td>$150&ndash;$300</td><td>$150&ndash;$300 (own after yr 1)</td><td>Use insurance if available</td></tr>
        <tr><td>Medicare rental pathway</td><td>$150&ndash;$182</td><td>$150&ndash;$182 (own after mo 13)</td><td>Follow Medicare pathway</td></tr>
    </tbody>
</table>

<p>If you are trying therapy before committing, a 30-day cash rental at $75 to $100 is reasonable. For anyone planning to use CPAP therapy ongoing, purchasing a device directly from an online retailer (CPAP.com, CPAPsupplyusa.com, or similar) saves significantly over DME supplier pricing.</p>

<h2 id="without-insurance">6. Buying CPAP without insurance</h2>

<p>Buying CPAP directly without going through a DME supplier or insurance is legal and can save 30 to 50% on equipment costs. A few key points:</p>

<ul>
    <li><strong>You still need a prescription:</strong> CPAP devices are FDA Class II medical devices and require a physician prescription to purchase, even online.</li>
    <li><strong>Online retailers are significantly cheaper:</strong> The same ResMed AirSense 11 that a hospital DME department might charge $1,400 for retails at $900 to $1,050 on direct-to-consumer sites.</li>
    <li><strong>FSA and HSA funds are eligible:</strong> CPAP equipment and supplies qualify as medical expenses under IRS rules. Pay with your FSA or HSA card to use pre-tax dollars.</li>
    <li><strong>ResMed and Philips recall:</strong> Philips DreamStation 1 (first-generation) devices were recalled in 2021 due to foam degradation concerns. If you are using an affected device, check the recall status at cpaprecall.philips.com. Replacement devices are available. Avoid purchasing first-generation DreamStation units on the secondary market.</li>
</ul>

<h2 id="hcpcs-codes">7. CPAP billing codes (HCPCS) explained</h2>

<p>DME is billed using HCPCS (Healthcare Common Procedure Coding System) Level II codes rather than CPT codes. These codes appear on your DME supplier&rsquo;s itemized bill and your insurance EOB. Here are the key codes to know:</p>

<table>
    <thead>
        <tr>
            <th>HCPCS Code</th>
            <th>Description</th>
            <th>Medicare Monthly Rate (2026)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>E0601</td><td>CPAP device (includes APAP)</td><td>~$58&ndash;$70/month rental</td></tr>
        <tr><td>E0470</td><td>BiPAP without backup rate</td><td>~$120&ndash;$145/month rental</td></tr>
        <tr><td>E0471</td><td>BiPAP with backup rate</td><td>~$200&ndash;$245/month rental</td></tr>
        <tr><td>A7034</td><td>Nasal interface (mask)</td><td>~$65 per unit</td></tr>
        <tr><td>A7030</td><td>Full face mask</td><td>~$95 per unit</td></tr>
        <tr><td>A7037</td><td>Tubing</td><td>~$10 per unit</td></tr>
        <tr><td>A7038</td><td>Disposable filter (2/month)</td><td>~$2 per unit</td></tr>
    </tbody>
</table>

<h2 id="billing-errors">8. Common CPAP and DME billing errors</h2>

<p>BillKarma&rsquo;s data shows that <strong>23% of sleep-related equipment claims</strong> contain billing errors. The most common errors in CPAP billing:</p>

<ol>
    <li><strong>Billing for supplies not delivered:</strong> Auto-ship programs sometimes generate invoices before shipment is confirmed. Request delivery confirmation for any supply shipment billed to your insurance.</li>
    <li><strong>Exceeding replacement frequency:</strong> Billing for masks or tubing more frequently than the Medicare or insurer&rsquo;s replacement schedule allows. Compare billing dates against actual shipment dates.</li>
    <li><strong>Wrong HCPCS code for device class:</strong> Billing E0470 or E0471 (BiPAP) rates when only a CPAP (E0601) was provided. BiPAP reimburses at roughly 2 to 4 times the CPAP rate.</li>
    <li><strong>Continued billing after ownership transfer:</strong> DME suppliers should stop billing E0601 rental after month 13 under Medicare. Continued rental billing after the ownership date is improper.</li>
    <li><strong>Duplicate billing for humidifier:</strong> The heated humidifier integrated into modern CPAP devices (like the ResMed AirSense 11) is included in E0601&mdash;billing separately for an integrated humidifier as an add-on accessory is a billing error.</li>
</ol>

<div class="key-takeaway">
    <strong>Received unexpected CPAP equipment bills or charges for supplies you didn&rsquo;t receive?</strong> <a href="/fight-debt">Use BillKarma&rsquo;s DME dispute tools</a> to audit HCPCS codes, compare supply billing dates against your delivery records, and generate dispute letters for your insurance and DME supplier.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does a CPAP machine cost in 2026?</h3>
        <p>A CPAP machine costs $500 to $1,500 without insurance in 2026. The ResMed AirSense 10 and AirSense 11 retail for $700 to $1,100. Auto-adjusting CPAP (APAP) machines cost $600 to $1,800, while BiPAP machines range from $800 to $3,000. Buying directly from an online retailer is typically 30 to 50% less expensive than purchasing through a hospital-affiliated DME supplier.</p>
    </div>
    <div class="faq-item">
        <h3>Does insurance cover CPAP machines?</h3>
        <p>Most commercial insurance plans and Medicare cover CPAP machines as DME when prescribed following a qualifying sleep study diagnosing OSA. Coverage typically requires an AHI of 5 or greater with symptoms, or 15 or greater without. You will pay your DME deductible and coinsurance (usually 20%), and many insurers require a 3-month rental period before purchasing outright.</p>
    </div>
    <div class="faq-item">
        <h3>What HCPCS codes are used for CPAP billing?</h3>
        <p>The primary HCPCS code for CPAP equipment is E0601. BiPAP devices use E0470 (without backup rate) or E0471 (with backup rate). Supplies are billed separately using A-codes: A7030 (full face mask), A7034 (nasal mask), A7037 (tubing), A7038 (disposable filter), A7039 (non-disposable filter).</p>
    </div>
    <div class="faq-item">
        <h3>How does Medicare cover CPAP machines?</h3>
        <p>Medicare covers CPAP therapy under Part B as DME when AHI &ge;5 is documented. Medicare pays 80% of the approved monthly rental amount after the Part B deductible. After 13 months of covered rental with documented compliance, you own the machine outright at no additional charge.</p>
    </div>
    <div class="faq-item">
        <h3>Should I rent or buy a CPAP machine?</h3>
        <p>If you have insurance, follow your plan&rsquo;s rental pathway&mdash;it leads to ownership after the compliance period at minimal out-of-pocket cost. If paying cash for long-term therapy, buying outright is cheaper. A $900 CPAP rented at $75 per month costs $900 after 12 months anyway, with no ownership benefit unless you have coverage.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/coverage/durable-medical-equipment-dme-coverage" target="_blank" rel="noopener">CMS: Medicare Durable Medical Equipment Coverage</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/durable-medical-equipment" target="_blank" rel="noopener">CMS: DME Fee Schedule 2026</a></li>
    <li><a href="https://www.aasm.org/clinical-resources/coding-reimbursement/" target="_blank" rel="noopener">American Academy of Sleep Medicine: Coding and Reimbursement Resources</a></li>
    <li><a href="https://cpaprecall.philips.com/" target="_blank" rel="noopener">Philips CPAP Recall Information</a></li>
    <li><a href="https://www.sleepfoundation.org/sleep-apnea/cpap" target="_blank" rel="noopener">Sleep Foundation: CPAP Therapy Guide</a></li>
    <li><a href="https://www.irs.gov/publications/p502" target="_blank" rel="noopener">IRS Publication 502: Medical and Dental Expenses (FSA/HSA eligibility)</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2024.00145" target="_blank" rel="noopener">Health Affairs: DME Billing Accuracy in Sleep Therapy</a></li>
</ul>
""",
})
