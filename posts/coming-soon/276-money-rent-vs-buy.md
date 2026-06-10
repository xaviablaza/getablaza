---
title: Rent vs Buy
description: Total cost of ownership (mortgage, taxes, insurance, maintenance, opportunity cost of down payment) vs renting and investing the difference. Break-even analysis.
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
inspiration_url: https://templeton.host/money/rent-vs-buy/
inspiration_category: money
---

> Source-copy draft imported from [https://templeton.host/money/rent-vs-buy/](https://templeton.host/money/rent-vs-buy/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Personal Finance](/money/)

[inventory](/money/inventory/)[graph](/money/graph/)

Personal Finance

# Rent vs Buy

Real EstateDifficulty: ★★★☆☆

Total cost of ownership (mortgage, taxes, insurance, maintenance, opportunity cost of down payment) vs renting and investing the difference. Break-even analysis.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Prerequisites (2)

[Mortgage Mathlvl 3](/money/mortgage-basics/)[Asset Allocationlvl 3](/money/asset-allocation/)

## Unlocks (1)

[Rental Property Mathlvl 4](/money/rental-property-math/)

## Referenced by Business (15)

Where this personal-finance concept shows up inside the operating-finance graph.

[selling costsBusiness

Selling costs (5-6% agent commission alone) are a major hidden input that shifts the buy-vs-rent break-even by years - understanding selling cost structure directly changes the time horizon calculation](/business/selling-costs/)[real estateBusiness

The consumer-side decision that creates demand for RE as a business - understanding the buy/rent margin is understanding your customer](/business/real-estate/)[CommissionsBusiness

Commissions (5-6% on sale) are one of the largest transaction costs in the buy-vs-rent break-even analysis, creating a minimum holding period before buying beats renting](/business/commissions/)[rent-vs-buy decisionBusiness

Direct personal-scale analog: housing rent-vs-buy is this exact problem with added variables (maintenance, appreciation, opportunity cost of down payment). Break-even horizon analysis is identical.](/business/rent-vs-buy-decision/)[Closing AdjustmentsBusiness

Closing adjustments (5-30%) are a major transaction friction in rent-vs-buy break-even analysis; they set the minimum holding period needed for ownership to beat renting by reducing net sale proceeds.](/business/closing-adjustments/)[appraised valueBusiness

The selling cost haircut (netting only 70-95% of appraised value) is the key friction that makes short holding periods favor renting - break-even analysis depends directly on how long you must hold for appreciation to exceed this transaction cost wedge](/business/appraised-value/)[break-evenBusiness

Rent vs buy explicitly uses break-even analysis - at what holding period does total cost of ownership equal cumulative rent? Same threshold logic at personal scale.](/business/break-even/)[Capital BudgetingBusiness

Rent-vs-buy is personal-scale capital budgeting: a major irreversible investment evaluated via total cost of ownership, break-even analysis, and opportunity cost of deployed capital (down payment). Same DCF-style go/no-go framework.](/business/capital-budgeting/)[illiquid assetsBusiness

Homes are the canonical illiquid asset for individuals; the break-even analysis must account for the 5-6% selling costs and time-on-market that drive the liquidation discount](/business/illiquid-assets/)[SaaSBusiness

SaaS is renting software capability vs building/buying it yourself - identical TCO framework (subscription cost vs build cost, opportunity cost of capital, break-even horizon) applied at business scale instead of housing scale](/business/saas/)[Build, Buy, or HireBusiness

The direct individual-scale analog: own the asset (build/buy) vs pay for ongoing access (hire/rent). Same tradeoff of upfront investment and control vs flexibility and lower commitment.](/business/build-buy-or-hire/)[winner's curseBusiness

Housing bidding wars are the most common personal-finance encounter with the winner's curse - competing buyers in a hot market each estimate the home's true value with noise, and the winning bid systematically overpays relative to common value](/business/winner-s-curse/)[DepreciationBusiness

Depreciation's net-rate test is the business-scale version of rent-vs-buy: if the asset depreciates faster than it appreciates (models), rent/subscribe; if it appreciates (proprietary data), own it. Same break-even logic, different asset.](/business/depreciation/)[down paymentBusiness

The down payment is the central liquidity event that differentiates buying from renting; this concept captures the specific condition under which the cash outflow makes buying inadvisable](/business/down-payment/)[Net Present ValueBusiness

Rent vs buy is personal-scale NPV analysis - total cost of ownership, break-even timelines, and comparing cash flow streams under different scenarios are the same discounted cash flow framework.](/business/net-present-value/)

Most people overpay by tens of thousands of dollars because they compare monthly rent to mortgage payment and stop there.

TL;DR:

**Rent vs Buy** compares the **Total Cost of Ownership** of buying - including mortgage, taxes, insurance, maintenance, and opportunity cost of a down payment - against renting and investing the difference to find a break-even horizon and an evidence-based housing decision.

## The Problem - What Goes Wrong

People often compare only monthly housing cash flows and miss larger costs and benefits. A typical error is equating a $1,800 monthly rent with a $1,800 monthly mortgage payment and declaring them equal. That ignores at least four numbered items: 1) property tax typically 0.5 to 2.5% of home value annually, 2) homeowners insurance roughly $600 to $2,000 per year for a $300,000 home, 3) maintenance averaging 1 to 3% of home value per year, and 4) the opportunity cost of a down payment typically 3 to 7% real return if invested.

Example that goes wrong: assume a $300,000 house, 20% down payment of $60,000, 30-year mortgage at 4.5% producing a $1,216 principal-and-interest payment. Someone says $1,216 versus $1,800 rent and picks buying. That choice misses annual property tax of $3,000 to $7,500, insurance $800, and maintenance $3,000 to $9,000. It also hides that the $60,000 down payment could earn 5-7% real return, which is $3,000 to $4,200 per year in forgone gains.

Consequences in dollars: over 10 years the missed comparison can change net wealth by $50,000 to $200,000 depending on home appreciation and investment returns. IF a buyer assumes home price growth of 3-5% annually AND ignores opportunity cost, THEN they may overestimate buying as a wealth-builder BECAUSE equity accumulation is not the same as net return after costs and foregone investments.

This problem ties directly to Mortgage Math, which covered amortization, PMI, and prepayment and to Asset Allocation, which governs the expected 3-7% real returns for a diversified stock/bond portfolio. Without integrating those prerequisites, decisions use partial data and create biased outcomes. The remainder of this lesson converts those missing pieces into formulas, a decision framework, and limitations to make a defensible choice.

## How It Actually Works - Mechanics and Formulas

Start with a clear definition. **Total Cost of Ownership** is the annualized net cost of home ownership including mortgage interest, property tax, insurance, maintenance, and the **Opportunity Cost** of the down payment. Renting has a comparable number: rent plus renters insurance plus transaction costs and the investment return on the rent-difference.

Core formula for annual net cost to owner: TCOowner=I+T+H+M+OC−G\text{TCO}\_\text{owner} = I + T + H + M + OC - GTCOowner​=I+T+H+M+OC−G where

- •III = annual mortgage interest paid (year-specific from amortization),
- •TTT = annual property tax (percent of home price),
- •HHH = homeowners insurance annually,
- •MMM = maintenance and repairs annually (1 to 3% of home price recommended),
- •OCOCOC = opportunity cost of down payment = d×rid \times r\_id×ri​ where ddd is down payment and rir\_iri​ is expected after-tax real return, and
- •GGG = annual tax benefits or mortgage interest deduction estimate, if applicable (0 to 25% of interest depending on filing status and itemization).

Core formula for annual net cost to renter: TCOrenter=R+Rins+C−Iinv\text{TCO}\_\text{renter} = R + R\_{ins} + C - I\_{inv}TCOrenter​=R+Rins​+C−Iinv​ where

- •RRR = annual rent,
- •RinsR\_{ins}Rins​ = renters insurance (usually $100 to $300 per year),
- •CCC = transaction and relocation costs averaged per year (security deposits, moving every 3 to 7 years may cost $2,000 to $7,000 total), and
- •IinvI\_{inv}Iinv​ = investment return on the rent-difference invested (annualized).

Break-even horizon calculation makes this comparable over NNN years. Compute cumulative net wealth for buying versus renting.

Wealth if buying after NNN years: WB(N)=E(N)+Hsale(N)−LB(N)W\_B(N) = E(N) + H\_{sale}(N) - L\_B(N)WB​(N)=E(N)+Hsale​(N)−LB​(N) where

- •E(N)E(N)E(N) = equity built from amortization and principal payments (exact schedule from Mortgage Math),
- •Hsale(N)H\_{sale}(N)Hsale​(N) = home price growth minus selling costs = P0(1+g)N−sP\_0 (1+g)^N - sP0​(1+g)N−s, with ggg expected home appreciation rate (commonly 0 to 3% real) and sss selling costs 5 to 8% of sale price,
- •LB(N)L\_B(N)LB​(N) = cumulative owner costs paid over NNN years = ∑t=1N(It+Tt+Ht+Mt+OCt−Gt)\sum\_{t=1}^{N} (I\_t + T\_t + H\_t + M\_t + OC\_t - G\_t)∑t=1N​(It​+Tt​+Ht​+Mt​+OCt​−Gt​).

Wealth if renting after NNN years: WR(N)=I0+∑t=1N(Iinv,t)−CR(N)W\_R(N) = I\_0 + \sum\_{t=1}^{N} (I\_{inv,t}) - C\_R(N)WR​(N)=I0​+∑t=1N​(Iinv,t​)−CR​(N) where

- •I0I\_0I0​ = initial investable cash including the would-be down payment ddd,
- •Iinv,tI\_{inv,t}Iinv,t​ = annual investment returns on savings from renting versus buying, typically 3-7% real for diversified portfolios depending on Asset Allocation,
- •CR(N)C\_R(N)CR​(N) = cumulative rent and transaction costs over NNN years.

Break-even horizon is smallest NNN such that WB(N)≥WR(N)W\_B(N) \ge W\_R(N)WB​(N)≥WR​(N). Use scenario ranges: run ggg between -1% and 3% real, investment return rir\_iri​ between 3% and 7% real, and annual maintenance 1 to 3% of price. IF expected home appreciation ggg is low, say 0 to 1% real, AND expected investment return rir\_iri​ is high, say 5-7% real, THEN renting and investing the down payment may outperform buying within 5 to 15 years BECAUSE the opportunity cost and maintenance drag outweigh equity buildup and modest appreciation.

Small formulas can help decisions: present value approach uses NPV=WB(N)−WR(N)NPV = W\_B(N) - W\_R(N)NPV=WB​(N)−WR​(N). Use Monte Carlo or sensitivity tables with ranges to capture uncertainty. That method connects directly to Mortgage Math amortization schedules and Asset Allocation expected returns to quantify outcomes.

## The Decision Framework - IF/THEN/BECAUSE Rules

Problem statement: people want a rule of thumb such as "buy if planning to stay 5 years" without quantifying costs. That produces frequent errors worth $10,000 to $100,000 across scenarios.

Rule 1 - Down payment trade-off. IF down payment is large relative to liquid savings, say 20% or more of home price equals 6 to 12 months of emergency savings, THEN delaying purchase to raise liquidity may reduce financial risk BECAUSE emergency shortfalls force high-cost borrowing or liquidation at poor prices.

Rule 2 - Break-even horizon. IF expected time in the house is less than 5 years AND transaction costs are 5 to 8% of price, THEN renting may be cheaper over that horizon BECAUSE buying incurs up-front closing costs 2 to 5% and selling costs 5 to 8% that need time to amortize.

Rule 3 - Opportunity cost. IF the down payment ddd can be invested with expected after-tax real return rir\_iri​ of 4-7% AND mortgage interest rate minus tax benefit is 2-4% net, THEN investing instead of buying may produce higher net wealth over 7 to 15 years BECAUSE compound returns at higher rates beat the slower principal paydown when ggg is modest.

Rule 4 - Consumption value. IF homeownership provides non-financial value measured at vvv dollars per year, with typical estimates vvv = $2,000 to $10,000 per year for stability and customization, THEN lower financial dominance thresholds by vvv when comparing WB(N)W\_B(N)WB​(N) and WR(N)W\_R(N)WR​(N) BECAUSE part of the choice is consumption utility not captured in pure returns.

Operational decision tree to apply: 1) Calculate annual owner costs using the TCO\_owner formula with your exact mortgage amortization from Mortgage Math. 2) Calculate renter scenario assuming investable difference grows at your Asset Allocation expected real return between 3% and 7%. 3) Run break-even for horizons 3, 5, 10, and 15 years under conservative and aggressive assumptions. 4) Adjust for personal liquidity needs and a consumption value vvv.

IF your sensitivity table shows buying beats renting across most realistic ranges for ggg and rir\_iri​ for your horizon, THEN buying may make financial sense for you BECAUSE the net present value of owner wealth is higher even after costs. The framework forces explicit trade-offs and quantifies uncertainty ranges rather than a single rule of thumb.

## Edge Cases and Limitations - Where the Model Breaks Down

Start with two big limitations. First, local housing market microstructure matters. In some cities a 5-7% annual nominal price appreciation is common for long stretches. That rate translates to 3-5% real after inflation and can flip the break-even point. Second, this framework assumes steady rents and investment returns in a range of 3-7% real. Short-term volatility can produce outcomes outside those ranges and change optimal choices for 1 to 3 year horizons.

Specific scenarios where the model fails or needs extension: 1) Highly illiquid markets - if home sale can take 6 to 18 months, then transaction timing risk raises effective selling costs by 1 to 3 percentage points and can lengthen break-even horizons by 2 to 5 years. 2) Neighborhood-level shocks - if local employment collapses or a major new employer leaves, home values may decline 10% to 40% over several years. The model does not predict such tail risks unless a stress test with -10% to -40% scenarios is included.

Other limitations: 1) Behavioral factors are hard to quantify. If owning reduces household turnover probability from 30% to 10% annually, that consumption value can be worth $1,000 to $6,000 per year, and must be approximated as vvv. 2) Tax code complexity - mortgage interest deduction is phased and itemization drops as standard deduction rises; the framework uses a simplified GGG estimate typically between 0 and 25% of interest but real values may vary widely by filer. 3) Home improvements - major renovations can change after-tax basis and resale value by tens of thousands of dollars, but returns on renovations vary from negative to positive 10-20% depending on work and market timing.

IF local appreciation is expected above 5% nominal annually AND transaction costs remain 5 to 8% of price, THEN buying is more likely to win within 3 to 7 years BECAUSE rapid price growth compounds equity faster than a diversified portfolio returns at 3-7% real. IF your job has high relocation probability, say 30% in 3 years, THEN renting is likely to dominate BECAUSE relocation costs of $5,000 to $15,000 and selling frictions reduce net owner wealth.

Documented limitations summary: 1) Does not forecast macro shocks or tail events explicitly, 2) simplifies tax rules into a single parameter GGG, 3) treats home appreciation ggg and investment returns rir\_iri​ as uncertain ranges without a full probabilistic model unless you build one. Use stress tests with -10% to +7% ranges to check robustness.

## Worked Examples (2)

### Short-Stay Suburban Example

30-year mortgage on $300,000 house, 20% down $60,000, mortgage 4.5% fixed, annual property tax 1.2% ($3,600), insurance $900, maintenance 1.5% ($4,500), selling costs 6%, expected home growth 2% nominal (0.5% real). Rent alternative $1,800/month increasing 2%/year. Invest difference at 5% real.

1. Compute annual mortgage payment using Mortgage Math: P&I = $1,216/month = $14,592/year.
2. Year 1 interest portion approx 4.5% of $240,000 = $10,800; principal paid = $3,792.
3. Annual owner costs year 1: I $10,800 + T $3,600 + H $900 + M $4,500 = $19,800. Add opportunity cost of down payment: $60,000 \* 5% = $3,000. Total owner cost year 1 = $22,800.
4. Annual renter cost year 1: rent $21,600 + renters insurance $150 = $21,750. The investable difference year 1 = owner cost minus renter cost = -$1,050, so renter spends $1,050 more year 1. Over time rent increases and mortgage interest declines, compute cumulative wealth over N = 5 and 10 years using amortization and assumed returns.
5. Compute net wealth difference at year 10 using amortization schedule: equity built roughly $35,000 after 10 years. Home sale price: $300,000\*(1+0.02)^10 = $365,000. Selling costs 6% = $21,900. Net sale proceeds ~ $343,100. Subtract remaining mortgage balance ~ $210,000 gives net equity ~ $133,100. Subtract cumulative owner costs approx $200,000 over 10 years yields net owner wealth ~ -$66,900 relative to original assets. Renter scenario: invest initial $60,000 and annual savings where applicable; with 5% return grow to approx $100,000 to $140,000 depending on annual contributions. Compare results; renting wins in most modeled ranges for 5 to 10 years.
6. Insight: This example shows that for a 5 to 10 year horizon in a modest appreciation market 2% nominal, renting and investing the down payment often yields higher net wealth because maintenance and opportunity cost eat into the apparent savings of mortgage payments.

**Insight:** Shows how maintenance, taxes, and opportunity cost of a $60,000 down payment shift the crossover point beyond a simple monthly-payment comparison. Renting often wins in 5 to 10 year windows when appreciation is low and investment returns are 4-6% real.

### Long-Hold Urban Example with Strong Appreciation

$500,000 condo, 10% down $50,000, mortgage 30-year at 3.5% (after points), HOA $350/month, property tax 1.0% ($5,000), insurance $1,200, maintenance 1% ($5,000), expected home growth 5% nominal (3% real), rent alternative $2,500/month growing 3%/year, invest difference at assumed 4% real.

1. Mortgage principal = $450,000. Monthly P&I approximately $2,020 = $24,240/year using Mortgage Math formula for 3.5% and 30 years.
2. Year 1 interest approx 3.5% of $450,000 = $15,750; principal ~ $8,490.
3. Annual owner costs year 1: I $15,750 + T $5,000 + H $1,200 + M $5,000 + HOA $4,200 = $31,150. Opportunity cost of down payment $50,000 \* 4% = $2,000. Total owner cost year 1 = $33,150.
4. Annual renter cost year 1: rent $30,000 + renters insurance $150 = $30,150. Invest difference year 1 = owner cost minus renter cost = $1,000 more to own. But high expected home growth 5% nominal compounds. After 15 years home price = $500,000\*(1+0.05)^15 ≈ $1,039,000. Selling costs 6% = $62,340; net sale ~ $976,660. Remaining mortgage balance after 15 years roughly $338,000. Net equity from sale ~ $638,660 minus original principal balance considerations and cumulative costs.
5. Compute renter wealth: invest $50,000 initial plus annual savings when owner is cheaper; with 4% real return, the invested assets after 15 years range $110,000 to $200,000 depending on cash flows. Compare to owner net equity ~ $638,660 less cumulative owner costs ~ $400,000 leaving significant positive owner wealth.
6. Insight: In markets with 3% real annual appreciation and low mortgage rates like 3.5% and HOA not excessive, long-hold buying over 10 to 20 years can outperform renting even after accounting for costs and opportunity cost.

**Insight:** Illustrates that when expected real home appreciation exceeds expected real investment returns after accounting for mortgage interest and costs, buying can dominate over a 10 to 20 year horizon.

## Key Takeaways

- ✓

  **Total Cost of Ownership** equals mortgage interest plus taxes, insurance, maintenance, and the opportunity cost of the down payment; quantify it with numbers before deciding.
- ✓

  Run a break-even horizon using ranges: use home growth g between -1% and 3% real and investment return r\_i between 3% and 7% real to check 3, 5, 10, and 15 year outcomes.
- ✓

  IF expected holding period is under 5 years AND transaction costs are 5 to 8% of price, THEN renting often costs less BECAUSE up-front closing and selling costs are amortized slowly.
- ✓

  IF local expected real appreciation exceeds expected portfolio real returns by 1-3 percentage points for 10+ years, THEN buying may build more net wealth BECAUSE compound home appreciation plus principal paydown outpaces investable returns.
- ✓

  Include a consumption value v between $2,000 and $10,000 per year when personal utility affects the choice; financial parity should be adjusted by that number.

## Common Mistakes

- ✗

  Comparing only monthly payments. Why this is wrong: monthly P&I excludes taxes, insurance, maintenance, and opportunity cost that commonly add 20% to 60% more annual cost for owners.
- ✗

  Assuming home always appreciates at historical highs. Why this is wrong: many markets experience real returns between -1% and 3% annually; using 5-7% without evidence overstates buyer advantage by tens of thousands of dollars.
- ✗

  Ignoring the opportunity cost of the down payment. Why this is wrong: a $50,000 down payment invested at 4-6% real yields $4,000 to $6,000 per year in foregone returns, which compounds and alters break-even by several years.
- ✗

  Treating tax benefits as guaranteed. Why this is wrong: mortgage interest benefit ranges from 0% to about 25% of interest paid depending on filing status; recent tax law raises the standard deduction and reduces itemization for many filers.

## Practice

easy

Easy: Compare buying a $250,000 house with 20% down versus renting at $1,600/month for 3 years. Use mortgage 4.0% 30-year, property tax 1.2%, insurance $900/year, maintenance 1.5% of price, invest difference at 5% real. What scenario has higher net wealth after 3 years?

**Hint:** Compute year-by-year owner costs: interest from amortization, taxes, insurance, maintenance, and opportunity cost on $50,000 down payment. Compute renter costs and growth of invested $50,000 at 5% plus yearly saved cashflows.

Show solution

Owner first-year P&I ≈ $954/month = $11,448/year. Year 1 interest ≈ 4% of $200,000 = $8,000. Year 1 owner costs: I $8,000 + T $3,000 + H $900 + M $3,750 = $15,650 plus opportunity cost $50,000*5% = $2,500 → $18,150. Renter year 1: rent $1,600*12=$19,200 + insurance $150 = $19,350. Year 1 renter spends $1,200 more. Over 3 years amortization builds small equity ≈ $6,000 to $8,000 total. Investing $50,000 at 5% for 3 years yields ≈ $57,625. Net: renting likely slightly better or similar after 3 years in most assumptions because transaction costs and opportunity cost outweigh modest equity. Conclusion: renting wins for this 3-year horizon under these parameters.

medium

Medium: You can put 10% down on a $400,000 house ($40,000) with mortgage rate 3.75% 30-year or rent for $2,400/month. HOA none. Property tax 1.1%, insurance $1,000, maintenance 1.2%. Compare 10-year outcomes assuming home growth 2% nominal and invest returns 5% real. Which wins and what is the break-even horizon?

**Hint:** Use the TCO formulas for both paths. For buyer include PMI until equity reaches 20%. Estimate PMI cost at 0.5% to 1% of original loan until LTV <80%. Compute amortization or use approximate equity accrual numbers for 10 years.

Show solution

Loan = $360,000. Monthly P&I ≈ $1,667 = $20,004/year. Year 1 interest ≈ 3.75% of $360,000 = $13,500. Year 1 owner costs: I $13,500 + T $4,400 + H $1,000 + M $4,800 = $23,700. PMI estimate 0.75% of loan = $2,700/year until LTV<80%; for 10% down, PMI lasts roughly 3 to 5 years. Opportunity cost of down payment $40,000 at 5% = $2,000/year. Year 1 total $28,400. Renter year 1: $28,800 + renters insurance $150 = $28,950. Early years renting slightly more expensive but PMI and opportunity cost change timing. After 10 years, equity built roughly $50,000 to $75,000 depending on amortization. Home sale price $400,000\*(1.02)^10 ≈ $487,000; selling costs 6% = $29,220. Net sale ~ $457,780 minus remaining mortgage balance ~ $300,000 → equity ≈ $157,780. Subtract cumulative owner costs ~ $260,000 gives net owner wealth ≈ -$102,220 relative to starting assets. Renter investing initial $40,000 at 5% over 10 years grows to ≈ $65,155 and annual extra savings variably contribute. Likely renting wins for 10 years here. Break-even horizon likely beyond 12 to 15 years under these assumptions.

hard

Hard: Synthesize with Mortgage Math. You have the option to buy a $350,000 house with 5% down ($17,500), a 15-year mortgage at 3.0% or a 30-year mortgage at 4.0%. Compare buying with 15-year mortgage, buying with 30-year mortgage, and renting at $1,900/month across 10 and 20 years. Use property tax 1.1%, insurance $1,200, maintenance 1.2%, investable returns 4% real. Discuss how mortgage term affects break-even and liquidity risk.

**Hint:** Compute amortization schedules precisely for both mortgage terms. 15-year has higher monthly P&I but much lower total interest and faster equity build. Compare TCO\_owner including opportunity cost of larger monthly payment in the 15-year case.

Show solution

30-year loan principal after 5% down = $332,500. 30-year at 4.0% P&I ≈ $1,587/month = $19,044/year. 15-year at 3.0% P&I ≈ $2,427/month = $29,124/year. Year 1 interest: 30-year ≈ 4.0%*$332,500=$13,300; 15-year ≈ 3.0%*$332,500=$9,975. Year 1 principal paid: 30-year ~$5,744; 15-year ~$19,149. After 10 years equity: 15-year equity roughly $170,000; 30-year equity roughly $65,000 (estimates from amortization). Owner costs year 1 30-year: I $13,300 + T $3,850 + H $1,200 + M $4,200 = $22,550 + opportunity cost $17,500*4%=$700 => $23,250. 15-year owner costs year 1: I $9,975 + T $3,850 + H $1,200 + M $4,200 = $19,225 + opportunity cost $700 => $19,925, but monthly cash flow burden is $10,080 higher annually versus 30-year, which reduces liquidity and investable contributions. Renting year 1: $1,900*12=$22,800 + insurance $150 = $22,950. Over 10 years, 15-year mortgage produces much higher equity ($~170,000) and lower cumulative interest paid, making it more likely to beat renting by year 10 in many reasonable appreciation scenarios. However liquidity risk is real: the 15-year mortgage requires $10,080 more cash flow per year which could otherwise be invested at 4% real; that opportunity cost over 10 years is significant. After 20 years the 15-year mortgage typically eliminates principal, giving ownership a large advantage if homeowner stays. Conclusion: IF the household can afford the higher monthly payment without sacrificing emergency liquidity - keep 3 to 6 months of expenses saved - THEN the 15-year mortgage accelerates break-even and increases net wealth over 10 to 20 years BECAUSE it reduces total interest and speeds equity accumulation. IF liquidity or job risk is high, THEN the 30-year mortgage or renting may dominate because higher monthly obligations create higher downside risk.

## Connections

Prerequisites used: Mortgage Math is required for accurate amortization and PMI schedules. Link: /money/mortgage-math. Asset Allocation is required to pick realistic investable return ranges 3-7% real. Link: /money/asset-allocation. What this unlocks downstream: Retirement planning models and withdrawal sequence analyses rely on housing decision effects on investable capital - see /money/retirement-planning. Advanced real estate strategies like buy-to-rent economics and portfolio-level property allocation use this framework - see /money/real-estate-portfolio.

**Disclaimer:** This content is for educational and informational purposes only and does not constitute financial, investment, tax, or legal advice. It is not a recommendation to buy, sell, or hold any security or financial product. You should consult a qualified financial advisor, tax professional, or attorney before making financial decisions. Past performance is not indicative of future results. The author is not a registered investment advisor, broker-dealer, or financial planner.

[← back to tree](/money/)[browse all →](/money/inventory/)
