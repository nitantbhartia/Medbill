"""Guide: BillKarma vs Goodbill."""

from guides import register, _embed

register("billkarma-vs-goodbill-medical-bills", {
    "title": "BillKarma vs Goodbill: Hospital Bill Services Compared",
    "meta_description": "Goodbill takes 20% of savings (max $1,000), nothing upfront. BillKarma charges $29-$149 flat, refunded if not reduced in 45 days. Which fits your bill.",
    "published": "2026-11-11",
    "author": "BillKarma Team",
    "category": "Negotiating Bills",
    "faqs": [
        {
            "q": "What is the main difference between BillKarma and Goodbill?",
            "a": "Goodbill negotiates your hospital bill and charges 20% of the savings, capped at $1,000, only if a settlement is reached. BillKarma checks every charge against Medicare rates and sends a written dispute for a flat $29 to $149, refunded if the bill isn't reduced within 45 days.",
        },
        {
            "q": "Does Goodbill charge anything upfront?",
            "a": "No. Goodbill's help center says it charges a fee only if an offer is negotiated with the hospital, and a patient can decline the offer at no cost. BillKarma charges its flat fee when it sends the dispute and refunds it if the bill isn't reduced within 45 days.",
        },
        {
            "q": "What bills does Goodbill not handle?",
            "a": "Goodbill says it handles hospital bills only, and that it doesn't help with bills that have gone to collections or bills you have already paid. If your bill is in collections, see our guide to medical debt in collections.",
        },
        {
            "q": "Which costs less, BillKarma or Goodbill?",
            "a": "BillKarma on each example bill, because its fee is flat. Goodbill can be cheaper when the savings are small: on a bill in BillKarma's $49 tier, Goodbill's 20% is lower if the savings are under $245. On large bills Goodbill's $1,000 cap narrows the gap.",
        },
        {
            "q": "Can I use both?",
            "a": "You can run BillKarma's free check first to see which charges are duplicates or far above Medicare, then decide whether to send a dispute yourself, use BillKarma, or hand the bill to a negotiator.",
        },
    ],
    "body": f"""
<p class="lead"><strong>Short answer:</strong> <a href="https://www.goodbill.com" target="_blank" rel="noopener">Goodbill</a> suits you if you want a company to negotiate a hospital bill and you don't want to pay anything unless it gets an offer. BillKarma suits you if you want every charge checked and a written dispute sent for a flat fee you can see in advance.</p>

<p>We make BillKarma, so read this with that in mind. Every fact about Goodbill below comes from Goodbill's own help center, checked in November 2026, and we say plainly where Goodbill is the better choice.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#side-by-side">Side by side</a></li>
        <li><a href="#cost">What each costs on real bill sizes</a></li>
        <li><a href="#goodbill-better">When Goodbill is the better choice</a></li>
        <li><a href="#billkarma-better">When BillKarma is the better choice</a></li>
        <li><a href="#neither">When you need neither</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="side-by-side">1. Side by side</h2>

<table>
    <thead>
        <tr><th></th><th>Goodbill</th><th>BillKarma</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>How it works</strong></td><td>Analyzes the hospital bill for coding errors and pricing gaps, then negotiates with the hospital</td><td>Checks every line against Medicare rates, writes a dispute letter, sends it by certified mail, follows up</td></tr>
        <tr><td><strong>Bills it takes</strong></td><td>Hospital bills only; not bills in collections or already paid</td><td>Hospital and facility bills of any size</td></tr>
        <tr><td><strong>Fee</strong></td><td>20% of savings, capped at $1,000</td><td>Flat: $29 (under $1k), $49 ($1k&ndash;$5k), $99 ($5k&ndash;$20k), $149 (over $20k)</td></tr>
        <tr><td><strong>Paid when</strong></td><td>Only if an offer is negotiated with the hospital</td><td>When the dispute is sent</td></tr>
        <tr><td><strong>If nothing is saved</strong></td><td>No fee</td><td>Fee refunded if not reduced within 45 days</td></tr>
        <tr><td><strong>What you provide</strong></td><td>Authorization for your hospital records, plus insurance and medical record details</td><td>A photo or PDF of the itemized bill</td></tr>
        <tr><td><strong>Follow-up</strong></td><td>Negotiation by Goodbill</td><td>Automatic follow-ups on days 7, 14, 30, 45</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Find out what's wrong first.</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; the check is free and shows which charges are duplicates or far above Medicare, whichever service you use next.
</div>

<h2 id="cost">2. What each costs on real bill sizes</h2>

<p>These use each company's published prices. The savings figures are examples to show the math, not predictions of what either service will win.</p>

<table>
    <thead>
        <tr><th>Bill</th><th>Example savings</th><th>Goodbill fee</th><th>BillKarma fee</th></tr>
    </thead>
    <tbody>
        <tr><td>$2,400 ER visit</td><td>$900</td><td>$180</td><td>$49</td></tr>
        <tr><td>$8,000 outpatient surgery</td><td>$3,000</td><td>$600</td><td>$99</td></tr>
        <tr><td>$12,000 surgery</td><td>$4,000</td><td>$800</td><td>$99</td></tr>
        <tr><td>$40,000 inpatient stay</td><td>$15,000</td><td>$1,000 (20% would be $3,000; capped)</td><td>$149</td></tr>
    </tbody>
</table>

<p>BillKarma's fee is lower on all four. Goodbill's cap keeps its fee from growing past $1,000, which is why its price is competitive on large bills. The difference that matters more than the fee is who does the work and what they can win. Goodbill says savings average 20% to 60%. We don't publish an average, because the result depends on the bill. For every major service's prices, see <a href="/guides/medical-bill-negotiation-service-cost/">what medical bill negotiation services cost</a>.</p>

{_embed(mode="markup", title="How far above Medicare is your charge?", subtitle="Enter a billing code and the amount charged.", height="420")}

<h2 id="goodbill-better">3. When Goodbill is the better choice</h2>

<ul>
    <li><strong>You want to risk nothing.</strong> Goodbill charges only if it reaches an offer, and you can decline the offer without paying. BillKarma's fee is paid up front and refunded after 45 days if the bill isn't reduced.</li>
    <li><strong>You want a company to do the negotiating.</strong> Goodbill negotiates with the hospital for you. BillKarma sends written disputes and follow-ups; it doesn't negotiate by phone.</li>
    <li><strong>The overcharge isn't a clear error.</strong> If the case rests on pricing and negotiation, not a duplicate or wrong quantity, a negotiator is the closer fit.</li>
</ul>

<div class="key-takeaway">
    <strong>Know your hospital before you start.</strong> Check our <a href="/hospitals/">hospital directory</a> &mdash; the billing phone number, financial assistance policy and how far its prices run above Medicare.
</div>

<h2 id="billkarma-better">4. When BillKarma is the better choice</h2>

<ul>
    <li><strong>You want to see the problems.</strong> BillKarma shows each charge next to the Medicare rate for the same code, so you know what is being disputed and why.</li>
    <li><strong>Clear errors.</strong> Duplicate lines, wrong quantities or services you didn't receive. A written dispute fixes these without a negotiator.</li>
    <li><strong>A fixed price.</strong> You know the fee before you start, and it doesn't grow with the savings: a $3,000 reduction costs $99.</li>
    <li><strong>A paper trail.</strong> Every request is in writing and dated, which helps if the bill later goes to collections.</li>
</ul>

<h2 id="neither">5. When you need neither</h2>

<p>If your income is under the hospital's limit and it's a nonprofit hospital, apply for <a href="/guides/hospital-financial-assistance-charity-care/">financial assistance</a> first. It can erase the bill for free, and the nonprofit Dollar For will help you apply at no cost. If the bill is already with a collector, neither service fits; read <a href="/guides/medical-debt-collections-rights/">your rights when a medical debt is in collections</a>. You can also <a href="/guides/how-to-dispute-a-medical-bill/">dispute a medical bill yourself</a> for the price of a stamp.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the main difference between BillKarma and Goodbill?</h3>
        <p>Goodbill negotiates your hospital bill and charges 20% of the savings, capped at $1,000, only if a settlement is reached. BillKarma checks every charge against Medicare rates and sends a written dispute for a flat $29 to $149, refunded if the bill isn't reduced within 45 days.</p>
    </div>
    <div class="faq-item">
        <h3>Does Goodbill charge anything upfront?</h3>
        <p>No. Goodbill's help center says it charges a fee only if an offer is negotiated with the hospital, and a patient can decline the offer at no cost. BillKarma charges its flat fee when it sends the dispute and refunds it if the bill isn't reduced within 45 days.</p>
    </div>
    <div class="faq-item">
        <h3>What bills does Goodbill not handle?</h3>
        <p>Goodbill says it handles hospital bills only, and that it doesn't help with bills that have gone to collections or bills you have already paid. If your bill is in collections, see our guide to <a href="/guides/medical-debt-collections-rights/">medical debt in collections</a>.</p>
    </div>
    <div class="faq-item">
        <h3>Which costs less, BillKarma or Goodbill?</h3>
        <p>BillKarma on each example bill, because its fee is flat. Goodbill can be cheaper when the savings are small: on a bill in BillKarma's $49 tier, Goodbill's 20% is lower if the savings are under $245. On large bills Goodbill's $1,000 cap narrows the gap.</p>
    </div>
    <div class="faq-item">
        <h3>Can I use both?</h3>
        <p>You can run BillKarma's free check first to see which charges are duplicates or far above Medicare, then decide whether to send a dispute yourself, use BillKarma, or hand the bill to a negotiator.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://help.goodbill.com/en/articles/254209" target="_blank" rel="noopener">Goodbill help center: How much does it cost? (20% of savings, $1,000 cap, checked Nov 2026)</a></li>
    <li><a href="https://help.goodbill.com/en/articles/334657" target="_blank" rel="noopener">Goodbill help center: Frequently asked questions (bill types, collections, 20&ndash;60% average savings, checked Nov 2026)</a></li>
    <li><a href="https://www.goodbill.com/faq" target="_blank" rel="noopener">Goodbill: FAQ, how Goodbill makes money (checked Nov 2026)</a></li>
    <li><a href="https://triagecancer.org/dollar-for-charity-care" target="_blank" rel="noopener">Triage Cancer: Dollar For's free charity care help</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/financial-assistance-policies-faps" target="_blank" rel="noopener">IRS: Financial assistance policies for nonprofit hospitals (Section 501(r))</a></li>
</ul>
""",
})
