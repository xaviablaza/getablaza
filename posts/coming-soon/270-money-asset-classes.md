---
title: Asset Classes
description: Stocks, bonds, cash, real assets, commodities. Risk and return characteristics of each. Equities for growth, bonds for stability, cash for liquidity.
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
inspiration_url: https://templeton.host/money/asset-classes/
inspiration_category: money
---

> Source-copy draft imported from [https://templeton.host/money/asset-classes/](https://templeton.host/money/asset-classes/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Personal Finance](/money/)

[inventory](/money/inventory/)[graph](/money/graph/)

Personal Finance

# Asset Classes

InvestingDifficulty: ★★★☆☆

Stocks, bonds, cash, real assets, commodities. Risk and return characteristics of each. Equities for growth, bonds for stability, cash for liquidity.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Prerequisites (2)

[Compound Interestlvl 1](/money/compound-interest/)[Opportunity Costlvl 1](/money/opportunity-cost/)

## Unlocks (4)

[Index Fundslvl 3](/money/index-funds/)[Diversificationlvl 3](/money/diversification/)[Capital Gainslvl 3](/money/capital-gains-planning/)[Options Basicslvl 4](/money/options-basics/)

## Referenced by Business (9)

Where this personal-finance concept shows up inside the operating-finance graph.

[financial productBusiness

Financial products are the concrete instruments within each asset class - stocks, bonds, CDs, mutual funds, ETFs. Understanding asset classes is understanding the taxonomy of financial products.](/business/financial-product/)[SecurityBusiness

Securities are the fundamental tradable instruments that comprise asset classes - stocks are equity securities, bonds are debt securities, and understanding what a security is precedes understanding the asset classes they form.](/business/security/)[Asset ClassBusiness

Direct individual-scale counterpart: stocks, bonds, cash, real assets, commodities and their risk/return profiles are the personal-finance view of the same asset class taxonomy the business concept generalizes over](/business/asset-class/)[net worthBusiness

Net worth = assets minus liabilities; understanding what counts as an asset (stocks, bonds, real estate, cash) is essential to computing and growing the assets side of the equation](/business/net-worth/)[alternative investmentsBusiness

Alternatives are defined as everything outside traditional asset classes (stocks, bonds, cash). Understanding the traditional taxonomy is prerequisite to understanding what makes an investment 'alternative' and why the risk/return/correlation profile differs.](/business/alternative-investments/)[commodity marketsBusiness

Commodities are explicitly one of the major asset classes individuals allocate to; understanding commodity markets as auction-driven price discovery explains why commodity returns behave differently from stocks and bonds in a personal portfolio.](/business/commodity-markets/)[Financial InstrumentsBusiness

Asset classes node covers stocks, bonds, cash, real assets, and commodities with their risk and return characteristics from the individual investor perspective - the same instruments ranked by risk-adjusted return at the business level](/business/financial-instruments/)[Return DistributionBusiness

Asset classes are defined by their return distributions - stocks (wide, right-skewed), bonds (narrow, symmetric), cash (near-zero variance). Choosing asset classes is choosing which return distribution to accept.](/business/return-distribution/)[CFABusiness

CFA curriculum formally categorizes and values the same asset classes (equities, fixed income, alternatives) that personal finance introduces for individual portfolios](/business/cfa/)

Many investors treat all money the same. That mistake can turn $100,000 into $150,000 or into $60,000 over 20 years.

TL;DR:

Asset classes are the building blocks of portfolios - understanding their risk, return, and liquidity trade-offs lets you match money to goals and likely outcomes.

## What Goes Wrong

People often mix goals and choices. That creates bad outcomes with clear dollar consequences. Example one. Someone keeps $100,000 in **cash** paying 0.5% while inflation averages 2.5% per year. Real value falls roughly 2.0% per year. After 20 years the inflation-adjusted value becomes about $100,000 \times (1-0.02)^{20} \approx $67,000. Example two. Another investor puts $100,000 into 100% equities before retirement with a 7% expected return and 16% annual volatility. If sequence of returns gives early 30% drops, a 4% withdrawal plan can deplete the portfolio in 15-20 years rather than lasting indefinitely. Both errors come from treating all money as fungible across time horizons and liquidity needs. The core problem is misaligning the right **asset class** with the right objective. When that alignment fails - growth money sits in low-return cash, stable needs sit in volatile equities - the results are predictable and measurable. IF a sum of money is earmarked for spending within 1-3 years AND it is placed in equities with 10-20% annual volatility, THEN the probability of a >20% nominal drop before spending may be 20-40% over that window BECAUSE short horizons amplify the chance a large downturn happens before you need the cash. IF long-term growth money is held in cash paying 0-1% while expected stock real returns are 5-7%, THEN forgone compounded gains may be large BECAUSE compound growth rates multiply over decades. This section identifies the mistake. The rest of the lesson shows how the different asset classes behave and how to assign them to goals with numbers and formulas.

## How It Actually Works

Start with definitions. **Stocks** or **equities** represent ownership claims on companies. Long run real returns often range 5-8% per year, with annual volatility commonly 12-18%. **Bonds** are debt instruments; investment-grade bonds often show real returns near 0-3% with volatility 3-8%. **Cash** includes savings accounts and short-term Treasury bills; real returns commonly -1% to +1% after inflation and volatility near 0-1%, with immediate liquidity. **Real assets** such as real estate or infrastructure typically generate 2-6% real returns plus rental yields of 2-5%, volatility 8-15%, and partial inflation linkage. **Commodities** like oil or metals have low long-run returns 0-3%, high short-term volatility 20-40%, and can act as an inflation or supply-shock hedge. Quantitatively combine assets using weighted averages and variance formulas. Expected portfolio return is E[Rp]=∑iwiE[Ri]E[R\_p] = \sum\_i w\_i E[R\_i]E[Rp​]=∑i​wi​E[Ri​]. For two assets, portfolio variance is σp2=wA2σA2+wB2σB2+2wAwBCovA,B\sigma\_p^2 = w\_A^2 \sigma\_A^2 + w\_B^2 \sigma\_B^2 + 2 w\_A w\_B \text{Cov}\_{A,B}σp2​=wA2​σA2​+wB2​σB2​+2wA​wB​CovA,B​. Example numeric calculation. Suppose equities expected return E[RE]=7%E[R\_E]=7\%E[RE​]=7% with σE=16%\sigma\_E=16\%σE​=16%, bonds E[RB]=2%E[R\_B]=2\%E[RB​]=2% with σB=6%\sigma\_B=6\%σB​=6%, correlation ρE,B=0.2\rho\_{E,B}=0.2ρE,B​=0.2. For a 60/40 portfolio wE=0.6w\_E=0.6wE​=0.6, wB=0.4w\_B=0.4wB​=0.4. Then E[Rp]=0.6×7%+0.4×2%=5.0%E[R\_p]=0.6\times7\% + 0.4\times2\% = 5.0\%E[Rp​]=0.6×7%+0.4×2%=5.0%. Variance computes to σp2=0.62(0.16)2+0.42(0.06)2+2(0.6)(0.4)(0.2)(0.16)(0.06)\sigma\_p^2 = 0.6^2(0.16)^2 + 0.4^2(0.06)^2 + 2(0.6)(0.4)(0.2)(0.16)(0.06)σp2​=0.62(0.16)2+0.42(0.06)2+2(0.6)(0.4)(0.2)(0.16)(0.06). That equals roughly $0.00922variance,so variance, so variance,so\sigma\_p\approx 9.6\%.Sharperatiois. Sharpe ratio is .Sharperatiois(E[R\_p]-R\_f)/\sigma\_p.Ifrisk−freecash. If risk-free cash .Ifrisk−freecashR\_f=1\%,Sharpeapprox, Sharpe approx ,Sharpeapprox(5.0\%-1\%)/9.6\%\approx0.42$. These formulas explain trade-offs. Higher expected returns often come with higher volatility and larger potential drawdowns. Equities historically provide growth and compound returns over long horizons. Bonds provide income and reduce volatility. Cash provides liquidity and safety of nominal principal. IF planning horizon is long and one can tolerate 15-20% year-to-year swings, THEN allocating a larger equity weight may increase expected terminal wealth BECAUSE higher expected returns compound over decades according to Compound Interest and the Rule of 72. IF capital must be spent within months, THEN cash or short-term bonds may be preferable BECAUSE they offer near 0% price volatility and immediate access.

## The Decision Framework

What to do instead of rules of thumb. Step 1 - match time horizon to asset class. Short horizon 0-3 months, medium 3 months-5 years, long 5+ years. Step 2 - quantify liquidity need. Emergency fund target commonly 3-6 months of expenses, with ranges 3-9 months for higher income volatility. Step 3 - measure risk capacity versus risk tolerance. Risk capacity is numerical - how many years of expenses your portfolio covers and your replacement income; risk tolerance is behavioral. Step 4 - select mix using IF/THEN/BECAUSE logic. IF money is needed in 0-3 months AND you value access over return, THEN hold it in cash or Treasury bills BECAUSE nominal principal risk is near zero and withdrawals are immediate. IF money is needed in 1-5 years AND you want some return without large drawdowns, THEN favor short-term bonds or a 20-40% equity allocation BECAUSE bonds reduce volatility and equities offer modest upside for medium-term horizons. IF money is for 10+ years AND you can accept 20% drawdowns, THEN shift toward 60-90% equities BECAUSE expected extra 3-5 percentage points in annual return compounds powerfully as shown in Compound Interest. Use rebalancing math and thresholds. Rebalancing maintains target risk exposures. One method is calendar rebalancing annually. Another is threshold rebalancing where you rebalance when an asset's weight crosses plus or minus 5 percentage points from target. Example formula for rebalancing threshold: trigger if ∣wi−wi,target∣>δ|w\_i - w\_{i,target}| > \delta∣wi​−wi,target​∣>δ where δ\deltaδ is 0.03-0.07. Consider taxes. IF holding municipal bonds in a 24% tax bracket, THEN tax-equivalent yield matters BECAUSE a 3% muni yield roughly equals a 3\% / (1-0.24) \approx 3.95\% taxable yield. Also weigh fees and liquidity. Real assets and private equity may offer higher expected returns but require lockups of 5-10 years and fees of 1-2% or more, which reduce net returns. This framework gives decisions, not mandates. It frames trade-offs numerically so choices map to goals and constraints.

## Edge Cases and Limitations

This framework works often but breaks in specific scenarios. Limitation one - changing return regimes. Expected returns are estimates with uncertainty ±2-4 percentage points. IF equity returns happen to be 0-2% real for a decade, THEN heavy equity allocations may underperform historical expectations BECAUSE forward returns can deviate materially from past averages. Limitation two - correlation breakdowns during crises. Many diversification benefits assume correlations around 0.2-0.4. In severe stress, correlations often rise toward 0.7-1.0, increasing portfolio drawdowns. Limitation three - illiquidity and forced selling. Real assets and private investments can be hard to sell quickly. IF an investor needs cash during a market crash AND holdings are illiquid, THEN they may be forced to sell at depressed prices BECAUSE secondary markets can freeze and buyers withdraw. Limitation four - behavioral risk and sequence of returns for retirees. The model does not predict psychology; withdrawal strategies like systematic withdrawals can fail when early returns are poor. Limitations specific to taxes and fees also matter. Municipal tax advantages, capital gains timing, and fund expense ratios can change net returns by 0.5-2.0 percentage points annually. Finally, model inputs are estimates. The math uses point inputs like 7% equity return and 2% bond return, but real outcomes follow distributions. Treat outputs as ranges not certainties. The framework also does not include extreme tail events frequency modeling. IF a once-in-50-year shock occurs, THEN simple mean-variance allocations may misstate true risk BECAUSE tail dependencies and liquidity freezes dominate mean statistics. Documenting these limitations clarifies where to be conservative and where to accept risk.

## Worked Examples (3)

### 30-Year Growth: Cash Versus 70/30 Portfolio

Investor A has $100,000 to invest for 30 years. Option 1: all cash earning 0.5% nominal, inflation 2.0% (real return -1.5%). Option 2: 70% equities (7% nominal expected), 30% bonds (2% nominal expected), inflation 2.0%.

1. Compute real returns. For Option 1 real = 0.5% - 2.0% = -1.5% per year.
2. Option 1 after 30 years: $100,000\times(1-0.015)^{30}\approx $100,000 \times 0.637 \approx $63,700.
3. Option 2 expected portfolio nominal return = 0.7\times7\% + 0.3\times2\% = 5.5\%. Real return = 5.5\% - 2.0\% = 3.5\%.
4. Option 2 after 30 years expected: $100,000\times(1+0.035)^{30} \approx $100,000 \times 2.81 \approx $281,000.
5. Compare outcomes: Option 1 inflation-adjusted value $63,700; Option 2 expected real terminal $281,000. The gap is $217,300.

**Insight:** For long horizons, small differences in annual real return create large differences in terminal wealth via compounding, as shown in Compound Interest.

### Retirement Withdrawals: 60/40 Versus 30/70

Retiree B has $600,000, needs $30,000/year (5% initial withdrawal). Compare Portfolio X 60/40 (E[R]=5.0\%, \sigma\approx9.6\%) and Portfolio Y 30/70 (E[R]=3.5\%, \sigma\approx6.5\%). Assume inflation 2.0% and withdrawals adjusted for inflation.

1. Initial safe withdrawal check. At 5% initial, longevity risks rise if expected real returns are near or below 3%.
2. Portfolio X expected real return = 5.0\% - 2.0\% = 3.0\%. Portfolio Y expected real return = 3.5\% - 2.0\% = 1.5\%.
3. If withdrawals are fixed in real terms, portfolio X expected return roughly matches withdrawal rate, while Y may erode principal over time.
4. Monte Carlo style insight: With volatility 9.6\%, sequence-of-returns risk means a 30\% drawdown in year 1 can reduce sustainable withdrawal to roughly 3.5\% versus 5\% originally, depending on recovery.

**Insight:** Higher equity weight increases expected returns and the chance of sustaining a 5% withdrawal, but also increases short-term volatility and sequence risk.

### Using Bonds for Stability and Cash for Liquidity

Household C has $50,000 emergency fund need and $200,000 medium-term goal in 4 years. They currently hold $250,000 in equities.

1. Allocate emergency fund $50,000 to high-yield savings paying 1.0%, giving immediate liquidity.
2. For $200,000 medium-term goal in 4 years, choose short-term bond ladder yielding 2.0% average with expected volatility 3-4%. Expected nominal in 4 years: $200,000\times(1.02)^4 \approx $216,490.
3. Leave the remainder $0 in equities if those funds are strictly for the 4-year goal. If some of the $200,000 can shift to 5+ year horizon, consider 20-40% equities for additional expected return.
4. Rebalance to maintain emergency cash and match horizon.

**Insight:** Matching liquidity needs to cash and short-duration bonds reduces the risk of needing to sell equities at a loss.

## Key Takeaways

- ✓

  Match horizon to asset class: short-term cash (0-3 months), medium-term bonds (3 months-5 years), long-term equities (5+ years).
- ✓

  Expected real returns ranges: equities 5-8% annually, investment-grade bonds 0-3%, cash -1 to +1% after inflation.
- ✓

  Use formulas: portfolio expected return E[Rp]=∑wiE[Ri]E[R\_p]=\sum w\_i E[R\_i]E[Rp​]=∑wi​E[Ri​] and variance σp2=wA2σA2+wB2σB2+2wAwBCovA,B\sigma\_p^2=w\_A^2\sigma\_A^2+w\_B^2\sigma\_B^2+2w\_Aw\_B\text{Cov}\_{A,B}σp2​=wA2​σA2​+wB2​σB2​+2wA​wB​CovA,B​ to quantify trade-offs.
- ✓

  IF funds are needed within 1-3 years AND preserving nominal principal matters, THEN hold cash or short bonds BECAUSE volatility can produce large nominal losses in equities.
- ✓

  Rebalance using thresholds like +/-3-7 percentage points to control drift and lock in disciplined buys and sells.

## Common Mistakes

- ✗

  Treating all money as fungible. This ignores different horizons and liquidity needs and leads to selling growth assets at market bottoms.
- ✗

  Overestimating diversification when correlations spike. Correlations can move from 0.2 to 0.8 in crises, reducing expected volatility benefits.
- ✗

  Ignoring tax-equivalent yields. A 3% municipal bond yield may equal roughly 3.95% taxable yield in a 24% tax bracket, changing relative attractiveness.
- ✗

  Chasing past high returns without adjusting risk. High recent returns increase the chance of mean reversion; allocating based on recent winners raises risk of timing losses.

## Practice

easy

Easy: You have $20,000 you will need in 18 months. Cash pays 1.0% annually. Short-term bonds pay 2.0% annually with 3% chance of a 4% principal loss within 18 months. Which is more aligned financially and why? Compute expected value of bond option.

**Hint:** Compare guaranteed accumulation versus expected value including loss probability.

Show solution

Cash after 18 months: $20,000\times(1+0.01)^{1.5} \approx $20,303. Short-term bonds expected nominal return over 1.5 years = 2.0% annual -> (1.02)^{1.5} \approx 1.0303. Without losses value = $20,606. Expected loss scenario: 3% chance of 4% principal loss -> in loss case value = $20,606\times0.96 \approx $19,782. Expected bond value = 0.97\times$20,606 + 0.03\times$19,782 \approx $20,560. Compare $20,560 expected vs $20,303 cash. IF avoiding principal loss is top priority AND liquidity is immediate, THEN cash may be preferable BECAUSE its nominal principal is nearly certain; otherwise expected value mildly favors bonds.

medium

Medium: You have $150,000. Option A: 60/40 portfolio with expected returns 7% equities, 2% bonds. Option B: 80/20 portfolio. Compute expected nominal returns for both and estimate 30-year terminal values.

**Hint:** Compute weighted expected returns then compound for 30 years without inflation adjustment.

Show solution

Option A expected = 0.6\times7\% + 0.4\times2\% = 4.6\%. Terminal = $150,000\times(1+0.046)^{30} \approx $150,000\times3.77 \approx $565,500. Option B expected = 0.8\times7\% + 0.2\times2\% = 5.8\%. Terminal = $150,000\times(1.058)^{30} \approx $150,000\times5.96 \approx $894,000. Trade-off: Option B higher expected terminal wealth but higher volatility and larger potential drawdowns.

hard

Hard: You are retiring with $800,000 and want 4% initial withdrawal ($32,000) adjusted for 2% inflation. Compare two portfolios: 50/50 (E=4.5\%, sigma=8.5\%) and 30/70 (E=3.0\%, sigma=6.0\%). Estimate whether each portfolio's expected real return covers withdrawals, and discuss sequence-of-returns risk implications.

**Hint:** Compute expected real return = E - inflation. Consider that if expected real return < withdrawal rate, principal likely declines absent positive sequence. Comment qualitatively on volatility impact.

Show solution

Portfolio 50/50 expected real = 4.5\% - 2.0\% = 2.5\%, less than 4% withdrawal so principal likely declines on average. Portfolio 30/70 expected real = 3.0\% - 2.0\% = 1.0\%, making decline steeper. Therefore neither portfolio's expected real return fully covers a 4% inflation-adjusted withdrawal. Sequence-of-returns risk: higher volatility in 50/50 raises the chance of early large drawdowns that reduce sustainable withdrawals, but higher expected return gives better long-run recovery odds. IF the retiree values longevity of principal over upside, THEN a lower withdrawal rate or higher bond allocation may be necessary BECAUSE expected real returns under the two mixes are below 4%.

## Connections

This lesson builds on Compound Interest (/money/compound-interest) and Opportunity Cost (/money/opportunity-cost) for the compounding and trade-off logic. Mastery here unlocks Asset Allocation (/money/asset-allocation), Portfolio Construction (/money/portfolio-construction), and Retirement Withdrawal Strategies (/money/retirement-withdrawals), because those topics require matching asset-class behavior to cash flow timing, tax treatments, and risk tolerance.

**Disclaimer:** This content is for educational and informational purposes only and does not constitute financial, investment, tax, or legal advice. It is not a recommendation to buy, sell, or hold any security or financial product. You should consult a qualified financial advisor, tax professional, or attorney before making financial decisions. Past performance is not indicative of future results. The author is not a registered investment advisor, broker-dealer, or financial planner.

[← back to tree](/money/)[browse all →](/money/inventory/)
