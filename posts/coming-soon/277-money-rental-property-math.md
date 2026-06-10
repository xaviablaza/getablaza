---
title: Rental Property Math
description: 'Net operating income, cap rate, cash-on-cash return, DSCR, the 1% rule. Underwriting a deal: purchase price, rehab, rent, expenses, financing.'
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- money
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/money/rental-property-math/
inspiration_category: money
---

> Source-copy draft imported from [https://templeton.host/money/rental-property-math/](https://templeton.host/money/rental-property-math/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Personal Finance](/money/)

[inventory](/money/inventory/)[graph](/money/graph/)

Personal Finance

# Rental Property Math

Real EstateDifficulty: ★★★★☆

Net operating income, cap rate, cash-on-cash return, DSCR, the 1% rule. Underwriting a deal: purchase price, rehab, rent, expenses, financing.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Prerequisites (1)

[Rent vs Buylvl 3](/money/rent-vs-buy/)

## Unlocks (2)

[Return on Equitylvl 4](/money/return-on-equity/)[Real Estate Leveragelvl 4](/money/real-estate-leverage/)

## Referenced by Business (11)

Where this personal-finance concept shows up inside the operating-finance graph.

[real estateBusiness

Individual-scale underwriting (NOI, cap rate, cash-on-cash) is the same math as commercial RE, just smaller deals](/business/real-estate/)[UnderwritingBusiness

Individual-scale deal underwriting - NOI, cap rate, cash-on-cash, DSCR are the same mechanics used in business-scale ROI underwriting and M&A due diligence, just applied to a single property](/business/underwriting/)[Financial RatiosBusiness

NOI, cap rate, DSCR, and cash-on-cash return are financial ratio analysis applied at individual property scale - same analytical framework businesses use across their entire operations](/business/financial-ratios/)[CFOBusiness

NOI, cap rate, cash-on-cash return, and DSCR are CFO-style underwriting metrics applied to individual real estate. Same math the CFO uses to evaluate a factory acquisition.](/business/cfo/)[ROI underwritingBusiness

Individual-scale ROI underwriting: NOI, cap rate, cash-on-cash return, DSCR are the same discipline applied to a single deal that institutional underwriting applies to M&A targets and portfolio companies](/business/roi-underwriting/)[M&A due diligenceBusiness

Individual-scale deal underwriting: NOI, cap rate, cash-on-cash return analysis is the same due diligence discipline as M&A target evaluation (DCF, multiples, synergy modeling) applied to a single property instead of a company](/business/m-a-due-diligence/)[Physical CapitalBusiness

Rental property is literal physical capital at individual scale - NOI, cap rates, depreciation schedules, and maintenance-vs-replacement decisions are the same math a CFO runs on factory equipment](/business/physical-capital/)[production linesBusiness

Both are capital assets underwritten by the same math: purchase price, operating costs, revenue, financing, and cash-on-cash return. A production line is evaluated like a rental property - capex in, cash flow out, same NOI and cap rate logic at industrial scale.](/business/production-lines/)[Operating ValueBusiness

NOI and cap rate are operating value frameworks at individual asset scale - cap rate literally prices the operating value of a property, and NOI is the operating value itself before financing](/business/operating-value/)[Internal Rate of ReturnBusiness

Cap rate, cash-on-cash return, and NOI are individual-scale IRR/NPV applied to real estate - same discounted cash flow framework, different asset class](/business/internal-rate-of-return/)[LBO ModelingBusiness

NOI, DSCR, cap rate, and cash-on-cash return are the same underwriting metrics used in LBO models, applied at single-property scale instead of enterprise scale](/business/lbo-modeling/)

Investors pay too much for cash flow they never actually see. Small mistakes in underwriting can turn a $10,000 NOI into a $2,000 annual loss.

TL;DR:

Rental Property Math ties **Net Operating Income**, **Cap Rate**, **Cash-on-Cash Return**, **DSCR**, and the **1% rule** into a quantitative framework that reveals whether a deal produces cash, builds equity, or risks default.

## What Goes Wrong

People buy properties using a headline rent or a gut feel. That produces three common failures with concrete dollar consequences. First, owners treat gross rent as cash flow. A $1,800 monthly rent on paper creates $21,600 yearly rent. If vacancy is 8% and operating expenses are 40% of effective income, the real cash for operations falls to about $10,600 per year. That difference of $11,000 changes a projected 7% return into a 2% loss on cash invested. Second, buyers chase low monthly mortgage payments without testing debt coverage. A $150,000 loan at 4.5% on a 30-year term costs about $9,000 per year. If the property delivers $10,600 NOI, the DSCR equals $10,600 / $9,000 = 1.18. That margin is narrow relative to repair risk, since a single major roof claim costing $8,000 can flip annual cash flow from positive to negative. Third, buyers apply simple heuristics like the **1% rule** blindly. The 1% rule says monthly rent should be at least 1% of purchase price. For a $200,000 house, 1% equals $2,000 monthly. If a market yields $1,600 rent instead, that rule signals rejection. But the rule ignores local taxes, insurance, and capex needs that might make a $2,000 rent still unprofitable after 50% total deductions. IF a buyer relies only on gross rent, AND the property has typical vacancies of 5-10% and operating costs of 35-55%, THEN their cash flow estimate may be overstated by 30-60% BECAUSE gross rent neglects real expenses and downtime. This section highlights why headline numbers fail and which specific figures cause the largest mistakes. Refer back to Rent vs Buy (d3) where total cost comparisons used mortgage, taxes, insurance, maintenance, and opportunity costs; those same categories reappear here with rental income replacing owner-occupied saved rent.

## How It Actually Works

Start with definitions. **Net Operating Income (NOI)** equals effective gross income minus operating expenses. Write it as NOI=EGI−OENOI = EGI - OENOI=EGI−OE. Effective Gross Income equals gross scheduled rent times (1−vacancyextrate)(1 - vacancy ext{ rate})(1−vacancyextrate) plus other income. Example formula: EGI=GrossRentimes(1−v)+OtherIncomeEGI = GrossRent imes (1 - v) + OtherIncomeEGI=GrossRentimes(1−v)+OtherIncome. Operating expenses normally include property tax, insurance, maintenance, management, utilities, and reserves for capital expenditures. Use typical ranges: vacancy 5-10%, management 6-10% of gross, maintenance 8-12% of gross, insurance and tax variable by jurisdiction but often 1-2% and 0.5-2% of property value annually respectively. **Cap Rate** measures return on property without financing. CapRate = rac{NOI}{PurchasePrice}. For a $200,000 purchase producing $NOI = $10,600, cap rate equals $10,600 / $200,000 = 5.3%.∗∗Cash−on−CashReturn∗∗measuresinvestorcashyieldbeforetaxes.. \*\*Cash-on-Cash Return\*\* measures investor cash yield before taxes. .∗∗Cash−on−CashReturn∗∗measuresinvestorcashyieldbeforetaxes.CoC = rac{CashFlow\_{pre-tax}}{CashInvested}.Cashinvestedusuallyequalsdownpaymentplusrehabplusclosingcosts.∗∗DebtServiceCoverageRatio(DSCR)∗∗equals. Cash invested usually equals down payment plus rehab plus closing costs. \*\*Debt Service Coverage Ratio (DSCR)\*\* equals .Cashinvestedusuallyequalsdownpaymentplusrehabplusclosingcosts.∗∗DebtServiceCoverageRatio(DSCR)∗∗equalsNOI / AnnualDebtService.LendersoftenrequireDSCRbetween1.20and1.35forconventionalloans,and1.25isacommonunderwritingthreshold.Annualdebtserviceequalsthesumof12monthlymortgagepayments.Monthlymortgagepaymentsfollowthestandardannuityformula. Lenders often require DSCR between 1.20 and 1.35 for conventional loans, and 1.25 is a common underwriting threshold. Annual debt service equals the sum of 12 monthly mortgage payments. Monthly mortgage payments follow the standard annuity formula .LendersoftenrequireDSCRbetween1.20and1.35forconventionalloans,and1.25isacommonunderwritingthreshold.Annualdebtserviceequalsthesumof12monthlymortgagepayments.MonthlymortgagepaymentsfollowthestandardannuityformulaM = P rac{r(1+r)^n}{(1+r)^n - 1}where where whererismonthlyinterestand is monthly interest and ismonthlyinterestandn$ is months. For a $150,000 loan at 4.5% over 360 months, r=0.045/12=0.00375r = 0.045/12 = 0.00375r=0.045/12=0.00375 and monthly $M
oughly $756, producing annual debt service about $9,072. Combine these pieces in a table mentally: EGI, subtract OE to get NOI, subtract annual debt service to get pre-tax cash flow, then divide by cash invested for CoC. IF a property has NOI that covers debt service by less than 1.1, AND expected vacancy plus capex risk is on the higher side of typical ranges, THEN financing increases the chance of negative cash flow BECAUSE the debt obligations are fixed while rents and expenses vary. The **1% rule** is a quick filter: rent >= 1% of purchase price indicates possible cash flow. But write that as a filter only. For a $120,000 house, 1% equals $1,200 monthly. If actual rent is $1,300, it passes the filter but still needs NOI and DSCR tests. This section supplies all formulas and variable ranges required for rigorous underwriting.

## The Decision Framework

What decisions matter at underwriting time? Break them into IF/THEN/BECAUSE steps that admit trade-offs. Step 1 - Accept or reject a deal based on cap rate and local yield targets. IF cap rate < 4.0% for single-family in suburban markets, AND long-term appreciation expectations are only 2-4% real, THEN the buy is unlikely to meet investor return targets of 8-12% total return BECAUSE low initial yield requires outsized appreciation to reach target returns. Step 2 - Test servicing risk with DSCR. IF DSCR<1.20DSCR < 1.20DSCR<1.20 AND financing has adjustable rates within the first 5 years, THEN financing creates higher default risk BECAUSE rent growth of 1-3% annually might not cover rising payments. Step 3 - Cash flow sensitivity. Build a 3-scenario cash flow model - base, downside, and stress. Use ranges: rent growth 0-3% annual in base, -5% to 0% in downside; vacancy 5-10% typical; capex reserve 5-10% of annual rent. IF downside scenario produces negative pre-tax cash flow for more than 1 year, AND cash reserves cover only 3 months of mortgage payments, THEN either renegotiate price or increase reserves BECAUSE insufficient buffers magnify minor revenue shocks into solvency problems. Step 4 - Evaluate cash-on-cash relative to alternative uses. IF CoC < 4% AND the investor's alternative is a taxable bond yielding 3-5% real, THEN equity deployment to this property may offer smaller risk-adjusted returns BECAUSE leverage and management time add risk that simple bonds do not carry. Practical application requires numeric thresholds customized to goals. For a small investor seeking 8-12% blended returns, targets could be cap rate 6-8% for single-family, CoC 8%+, DSCR 1.25+ if leverage is used, and reserves covering 3-6 months mortgage payments plus a 2-5% annual capex reserve. These numbers are ranges, not absolutes. Every trade-off has consequences: paying a higher price raises cap rate pressure but may lower vacancy in stronger neighborhoods.

## Edge Cases and Limitations

This framework does not capture every real-world contingency. First limitation - tax effects and depreciation timing. The formulas above omit tax benefits like depreciation and 1031 exchanges that can create effective after-tax returns 2-5% higher in some scenarios. IF tax sheltering is material to the investor, AND holding period exceeds 5-10 years, THEN after-tax returns can diverge substantially from pre-tax CoC BECAUSE depreciation front-loads paper losses and defers tax. Second limitation - market liquidity and price discovery. For thin markets with price swings of 10-30% in 12 months, valuation-based metrics like cap rate may be misleading. IF comparable sales are older than 3 months, AND the local market exhibits price volatility of 10%+, THEN underwritten purchase prices may be off by significant amounts BECAUSE the comps do not reflect current demand. Third limitation - single-event shocks like large unexpected capex. The model usually assumes capex reserves of 2-5% of property value annually or 5-10% of gross rent. IF a major structural issue emerges costing $20,000-40,000, AND the investor lacks access to emergency capital, THEN short-term solvency risk increases because debt service obligations remain fixed. Fourth limitation - behavioral costs and time. Management intensity for single-family vs 5+ units differs by a factor of 2-4 in hours per month, which translates into either management fees of 6-10% of gross or implicit opportunity costs. This framework does not price personal time. Use it as a model for first-order underwriting. Expand with tax modeling, market liquidity analysis, and scenario-based Monte Carlo methods for decisions that require precision beyond the 5-10% level.

## Worked Examples (3)

### Single-Family Rehab Flip to Rent

Purchase price $200,000, rehab $20,000, closing $3,000. Monthly rent $1,600. Vacancy 8%. Operating expenses 40% of effective gross income. Financing 25% down ($50,000), loan $150,000, interest 4.5% fixed, 30-year amortization.

1. Calculate annual gross rent: $1,600  times 12 = $19,200.
2. Effective Gross Income: $EGI = 19,200  times (1 - 0.08) = $17,664.
3. Operating expenses: $OE = 0.40  times 17,664 = $7,066 (rounded).
4. NOI: $NOI = 17,664 - 7,066 = $10,598.
5. Cap rate: $CapRate = 10,598 / 200,000 = 0.0530  i.e. about 5.3%.
6. Monthly mortgage: for $150,000 at 4.5% over 360 months monthly payment roughly $756, so annual debt service about $9,072.
7. DSCR: $DSCR = 10,598 / 9,072 = 1.17.
8. Pre-tax cash flow: $10,598 - 9,072 = $1,526 annually.
9. Cash invested: down payment $50,000 + rehab $20,000 + closing $3,000 = $73,000.
10. Cash-on-cash return: $CoC = 1,526 / 73,000 = 0.0209 or about 2.1%.

**Insight:** A property that looks attractive by rent still yields only about 2.1% cash-on-cash return under these assumptions. IF the investor needs immediate cash yield of at least 7-8% AND financing terms remain similar, THEN this deal likely fails that goal BECAUSE most cash flow is consumed by debt service and operating costs.

### Small Multifamily Leveraged Purchase

Purchase price $500,000 for a 5-unit building. Monthly rents $900 each, total monthly rent $4,500. Vacancy 5%. Operating expenses 50% of effective gross income. Financing 25% down ($125,000), loan $375,000, interest 5.0% fixed, 25-year amortization.

1. Annual gross rent: $4,500  times 12 = $54,000.
2. EGI: $EGI = 54,000  times (1 - 0.05) = $51,300.
3. Operating expenses: $OE = 0.50  times 51,300 = $25,650.
4. NOI: $NOI = 51,300 - 25,650 = $25,650.
5. Cap rate: $CapRate = 25,650 / 500,000 = 0.0513 or 5.13%.
6. Monthly mortgage: for $375,000 at 5.0% over 300 months monthly payment about $2,200, so annual debt service about $26,400.
7. DSCR: $DSCR = 25,650 / 26,400 = 0.97, below typical lender thresholds.
8. Pre-tax cash flow: $25,650 - 26,400 = -$750 annually.
9. Cash invested: down payment $125,000 + closing $5,000 = $130,000.
10. Cash-on-cash return: $CoC = -750 / 130,000 = -0.58%.

**Insight:** Leverage here creates a negative cash flow despite a reasonable cap rate of about 5.1%. IF a lender requires DSCR 1.25, THEN either the purchase price must fall or debt terms must change BECAUSE the debt obligation exceeds income under current assumptions.

### 1% Rule Filter Example

Property price $120,000. Market rent for similar units $1,300 monthly. Operating expenses and vacancy expected to total 45% of gross. Financing not considered in this filter.

1. 1% rule threshold: 1% of $120,000 equals $1,200 monthly.
2. Monthly rent $1,300 is greater than $1,200, so the property passes the 1% filter.
3. Annual gross rent: $1,300  times 12 = $15,600.
4. Estimated effective income after 45% combined vacancy and expenses: $15,600  times (1 - 0.45) = $8,580.
5. NOI in this simplified filter is about $8,580, which on a $120,000 purchase equals cap rate $8,580 / 120,000 = 7.15%.

**Insight:** Passing the 1% rule can coincide with a healthy cap rate. IF actual operating costs rise above 45% or vacancy increases to 10%, THEN the effective yield could drop below 5% BECAUSE the 1% rule ignores expense structure and downtime.

## Key Takeaways

- ✓

  Calculate **NOI = EGI - OperatingExpenses** first. Use vacancy 5-10% and expected OE 35-55% to stress-test results.
- ✓

  Use Cap Rate to compare unlevered returns: $CapRate = NOI / PurchasePrice. Target ranges vary by market: 4-8% typical.
- ✓

  Compute DSCR = NOI / AnnualDebtService. A DSCR below 1.20 commonly increases refinancing or default risk.
- ✓

  Cash-on-Cash Return equals pre-tax cash flow divided by cash invested. Include down payment, rehab, and closing costs.
- ✓

  Apply the 1% rule only as a quick filter. IF rent  / purchase price >= 1% THEN proceed to NOI and DSCR checks BECAUSE rent alone omits expenses.
- ✓

  Always run base, downside, and stress scenarios with reserve estimates of 3-6 months mortgage plus 2-5% annual capex.

## Common Mistakes

- ✗

  Using gross rent as cash flow. That mistake neglects vacancy and operating expenses and overstates cash by 30-60%.
- ✗

  Ignoring debt service risk. Counting on appreciation while DSCR < 1.10 introduces short-term solvency risk, not wealth creation.
- ✗

  Applying the 1% rule without expense modeling. The 1% rule can produce false positives if OE and vacancy exceed 40-50%.
- ✗

  Equating cap rate with cash yield. Cap rate ignores financing structure and initial cash invested, so CoC can be much lower or negative.

## Practice

easy

Easy: Calculate NOI, cap rate, annual debt service, DSCR, and cash-on-cash for a $180,000 purchase. Rent $1,500 monthly. Vacancy 7%. Operating expenses 42% of EGI. Financing 20% down, loan $144,000, interest 4.0%, 30-year amortization. Closing and rehab combined $6,000.

**Hint:** Compute EGI = gross rent  times (1 - vacancy). Use the annuity formula for monthly mortgage, or approximate monthly payment for $144,000 at 4.0% over 360 months as about $688.

Show solution

Annual gross rent = $1,500  times 12 = $18,000. EGI = 18,000  times (1 - 0.07) = $16,740. OE = 0.42  times 16,740 = $7,031. NOI = 16,740 - 7,031 = $9,709. Cap rate = 9,709 / 180,000 = 5.39%. Monthly mortgage approx $688, annual debt service = $8,256. DSCR = 9,709 / 8,256 = 1.18. Pre-tax cash flow = 9,709 - 8,256 = $1,453. Cash invested = down payment $36,000 + closing/rehab $6,000 = $42,000. Cash-on-cash = 1,453 / 42,000 = 3.46%.

medium

Medium: Compare two deals. Deal A: $220,000 price, rent $1,900, vacancy 8%, OE 40%, 25% down, 4.75% interest 30-year. Deal B: $165,000 price, rent $1,450, vacancy 8%, OE 45%, 25% down, 4.0% interest 30-year. Compute NOI, cap rate, cash-on-cash. Which offers higher CoC assuming closing+rehab $4,000 each?

**Hint:** Compute EGI then OE then NOI for each. Approximate monthly mortgage using standard ratios: for Deal A loan $165,000 at 4.75% monthly payment roughly $860; for Deal B loan $123,750 at 4.0% monthly payment roughly $592.

Show solution

Deal A: Annual gross rent = 1,900  times 12 = 22,800. EGI = 22,800  times 0.92 = 20,976. OE = 0.40  times 20,976 = 8,390. NOI = 20,976 - 8,390 = 12,586. Cap rate = 12,586 / 220,000 = 5.72%. Loan = 165,000, monthly payment ~ $860, annual debt service ~ $10,320. Pre-tax cash flow = 12,586 - 10,320 = $2,266. Cash invested = down 55,000 + closing 4,000 = $59,000. CoC = 2,266 / 59,000 = 3.84%. Deal B: Annual gross rent = 1,450  times 12 = 17,400. EGI = 17,400  times 0.92 = 16,008. OE = 0.45  times 16,008 = 7,203. NOI = 16,008 - 7,203 = 8,805. Cap rate = 8,805 / 165,000 = 5.34%. Loan = 123,750, monthly payment ~ $592, annual debt service ~ $7,104. Pre-tax cash flow = 8,805 - 7,104 = $1,701. Cash invested = down 41,250 + closing 4,000 = $45,250. CoC = 1,701 / 45,250 = 3.76%. Comparison: Deal A yields CoC about 3.84% and Deal B about 3.76%, so Deal A slightly higher by roughly 0.08 percentage points under these assumptions.

hard

Hard: Stress test a $300,000 multifamily purchase with $2,900 monthly gross rent. Vacancy 7%, operating expenses 48% of EGI, financing 30% down, loan $210,000 at 5.25% fixed for 25 years. Calculate NOI, DSCR, and determine the maximum percentage rent drop that would reduce DSCR below 1.0. Assume other variables constant.

**Hint:** Compute current NOI and annual debt service. Solve for rent multiplier x such that DSCR = 1: (NOI  times x) / Debt = 1. Rearrange x = Debt / NOI\_current. The rent drop percentage equals 1 - x.

Show solution

Annual gross rent = 2,900  times 12 = 34,800. EGI = 34,800  times (1 - 0.07) = 32,364. OE = 0.48  times 32,364 = 15,534. NOI = 32,364 - 15,534 = 16,830. Loan $210,000 at 5.25% for 25 years has monthly payment about $1,244, annual debt service about $14,928. Current DSCR = 16,830 / 14,928 = 1.128. To find rent multiplier x that makes DSCR = 1, set (NOI  times x) / 14,928 = 1, so x = 14,928 / 16,830 = 0.887. That implies rents can drop to about 88.7% of current levels before DSCR hits 1.0. Percentage rent drop = 1 - 0.887 = 0.113 or about 11.3%.

## Connections

Prerequisite: Rent vs Buy (d3) at /money/Rent\_vs\_Buy\_d3 explains total cost of ownership and opportunity cost of down payments, which this lesson uses when comparing Cash-on-Cash to alternative investments. Downstream: mastering Rental Property Math unlocks portfolio scaling and financing strategy topics like /money/MultiPropertyScaling\_d5 where DSCR and CoC determine acquisition sequencing, and tax-efficient strategies like /money/Tax\_Strategies\_Real\_Estate\_d5 where depreciation and 1031 timing materially change after-tax returns.

**Disclaimer:** This content is for educational and informational purposes only and does not constitute financial, investment, tax, or legal advice. It is not a recommendation to buy, sell, or hold any security or financial product. You should consult a qualified financial advisor, tax professional, or attorney before making financial decisions. Past performance is not indicative of future results. The author is not a registered investment advisor, broker-dealer, or financial planner.

[← back to tree](/money/)[browse all →](/money/inventory/)
