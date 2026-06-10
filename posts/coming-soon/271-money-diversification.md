---
title: Diversification
description: Correlation between assets. Risk reduction through breadth. The only free lunch in finance - owning everything beats picking winners.
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
permalink: /money/diversification/
---

[←Back to Personal Finance](/money/)

[inventory](/money/inventory/)[graph](/money/graph/)

Personal Finance

# Diversification

InvestingDifficulty: ★★★☆☆

Correlation between assets. Risk reduction through breadth. The only free lunch in finance - owning everything beats picking winners.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Prerequisites (1)

[Asset Classeslvl 3](/money/asset-classes/)

## Unlocks (2)

[Asset Allocationlvl 3](/money/asset-allocation/)[Options Basicslvl 4](/money/options-basics/)

## Referenced by Business (15)

Where this personal-finance concept shows up inside the operating-finance graph.

[Market DownturnBusiness

Diversification is the individual-scale defense against market downturns - owning uncorrelated assets so a 30-50% drop in one sector doesn't produce a 30-50% drop in your portfolio](/business/market-downturn/)[Execution RiskBusiness

Diversification reduces risk through low correlation between assets; execution risk teaches the same principle inverted - shared teams CREATE correlation, the opposite of diversification's free lunch](/business/execution-risk/)[VarianceBusiness

Diversification exists precisely because variance matters - two portfolios with the same expected return but different variance are not equivalent, and combining uncorrelated assets reduces variance without sacrificing expected return](/business/variance/)[Standard DeviationBusiness

Diversification reduces portfolio standard deviation - at the individual scale, combining uncorrelated assets lowers sigma on returns, which is the same principle as lower sigma on cost estimates producing tighter return distributions at the business scale](/business/standard-deviation/)[Markowitz Portfolio TheoryBusiness

Markowitz (1952) is the mathematical proof that diversification works: when asset correlations are less than 1, portfolio variance falls below the weighted average of individual variances. The personal finance node's 'only free lunch in finance' is exactly Markowitz's insight applied at individual scale.](/business/markowitz-portfolio-theory/)[diminishing returnsBusiness

Portfolio diversification follows the same diminishing returns curve - the first few uncorrelated assets dramatically reduce variance, but each additional asset class barely moves the needle, producing an 'elbow' in risk reduction vs number of holdings](/business/diminishing-returns/)[Long TailBusiness

Diversification captures value from the aggregate of many small, uncorrelated positions rather than concentrating on a few large bets - the same structural insight as the long tail, where collective value of many low-volume items exceeds the head](/business/long-tail/)[Sharpe RatioBusiness

Diversification is the individual-scale mechanism for improving Sharpe ratio - combining uncorrelated assets reduces portfolio sigma without proportionally reducing E[R], which is exactly why it's called 'the only free lunch in finance'](/business/sharpe-ratio/)[Operating InvestmentsBusiness

Diversification IS Markowitz at individual scale - the insight that portfolio risk depends on correlations between assets, not just individual risks, so owning the broad basket beats picking winners](/business/operating-investments/)[Risk-Adjusted ReturnBusiness

Diversification is the individual-scale practice of exploiting correlations between assets to reduce portfolio risk - the 'only free lunch' is a direct consequence of the correlation math taught here](/business/risk-adjusted-return/)[PortfolioBusiness

Diversification is the core Markowitz insight at individual scale - correlation between assets reducing risk is exactly the off-diagonal covariance terms that make portfolio variance less than weighted-average variance](/business/portfolio/)[Efficient FrontierBusiness

The efficient frontier exists because combining imperfectly correlated assets produces portfolios with better risk-return tradeoffs than any single asset alone - it is the mathematical proof that diversification works](/business/efficient-frontier/)[index fundsBusiness

Index funds are the primary vehicle for implementing diversification - owning the whole market rather than picking winners. The 'only free lunch in finance' argument is why index funds exist.](/business/index-funds/)[Investment PortfolioBusiness

Diversification is the core portfolio principle that owning uncorrelated assets reduces variance without sacrificing expected return - the 'only free lunch' is Markowitz at the intuitive level](/business/investment-portfolio/)[Multi-Brand PortfolioBusiness

Multi-brand portfolio reduces concentration risk through brand breadth and uncorrelated demand cycles, same logic as owning uncorrelated asset classes](/business/multi-brand-portfolio/)

Holding five winning stocks can feel clever until a single sector drop cuts your $100,000 nest egg by 40% in one year. Broad ownership can smooth that volatility and protect long-term compounding.

TL;DR:

Diversification is the deliberate spread of capital across low-correlated assets so that overall portfolio volatility falls by more than expected, and understanding it can raise long-run geometric returns by several percentage points per year.

## The Problem - What Goes Wrong Without Diversification

Many investors focus on picking winners. That often creates concentration. For example, a $100,000 portfolio concentrated 80% in five tech stocks can lose 40-60% in a single year if that sector falls 30-50%. That outcome reduces capital from $100,000 to roughly $40,000-$60,000 in a year. In contrast, a broadly diversified portfolio might drop 15-25% over the same period, leaving $75,000-$85,000. The gap matters because compounding amplifies differences: a 40% loss requires a 67% gain to breakeven, while a 20% loss needs only 25% to recover. That is the core failure mode. People underestimate the drag that volatility imposes on long-term returns. If two portfolios have the same arithmetic mean return of 8% but volatilities of 30% and 12%, then the approximate geometric returns differ by about 3.8 percentage points per year. The math uses the volatility tax approximation: rgeo≈rarith−0.5σ2r\_{geo} \approx r\_{arith} - 0.5 \sigma^{2}rgeo​≈rarith​−0.5σ2. Plugging numbers gives $8\% - 0.5(0.30^{2}) = 3.5\%$ versus $8\% - 0.5(0.12^{2}) = 7.3\%$. That gap converts to very different balances over decades. IF an investor holds concentrated positions AND has a long horizon, THEN reducing concentration may increase expected geometric wealth over 10-30 years MAY be likely BECAUSE lower volatility reduces volatility tax on compounding. Concentration also creates behavioral risks. Large drawdowns of 40-60% raise the probability of panic selling; empirical data show roughly 30-60% of investors sell after big losses. That behavior can lock in permanent losses. Finally, correlation is the hidden multiplier. Two assets each volatile at 20% can create portfolio volatility near 28% if correlation is 0.8, or near 9% if correlation is 0.0. Not accounting for correlation often misprices the benefit of diversification and leads to overconfident position sizing.

## How It Actually Works - Mechanics, Formulas, and Numbers

Start with the core math for two assets. Portfolio variance is Var(Rp)=w12σ12+w22σ22+2w1w2ρ12σ1σ2\mathrm{Var}(R\_p)=w\_{1}^{2}\sigma\_{1}^{2}+w\_{2}^{2}\sigma\_{2}^{2}+2w\_{1}w\_{2}\rho\_{12}\sigma\_{1}\sigma\_{2}Var(Rp​)=w12​σ12​+w22​σ22​+2w1​w2​ρ12​σ1​σ2​. For example, w1=0.6w\_{1}=0.6w1​=0.6, σ1=15%\sigma\_{1}=15\%σ1​=15%, w2=0.4w\_{2}=0.4w2​=0.4, σ2=5%\sigma\_{2}=5\%σ2​=5%, and ρ12=0.2\rho\_{12}=0.2ρ12​=0.2 gives variance $0.6^{2}(0.15^{2})+0.4^{2}(0.05^{2})+2(0.6)(0.4)(0.2)(0.15)(0.05)=0.0052.Thatimplies. That implies .Thatimplies\sigma\_{p}=\sqrt{0.0052}=7.2\%$. The same weighted arithmetic average of volatilities would be $0.6\cdot15\%+0.4\cdot5\%=11\%,sodiversificationloweredvolatilityfrom11, so diversification lowered volatility from 11% to 7.2% because correlation was low. For equal-weighted portfolios of ,sodiversificationloweredvolatilityfrom11nassetswithidenticalvolatility assets with identical volatility assetswithidenticalvolatility\sigmaandaveragepairwisecorrelation and average pairwise correlation andaveragepairwisecorrelation\bar{\rho},acompactresultappears:, a compact result appears: ,acompactresultappears:\mathrm{Var}(R\_p)=\sigma^{2}\left(\frac{1}{n}+\frac{n-1}{n}\bar{\rho}\right).Plugging. Plugging .Plugging\sigma=20\%$, $\bar{\rho}=0.25and and andn=20yields yields yields\mathrm{Var}=0.20^{2}(0.05+0.2375)=0.04(0.2875)=0.0115,so, so ,so\sigma\_{p}=10.7\%.Thatisanear46. That is a near 46% reduction in volatility from a single asset volatility of 20%. Breadth delivers risk reduction at diminishing marginal returns. Adding the 2nd to the 10th uncorrelated asset often cuts variance sharply. Adding the 21st to the 40th usually yields only incremental reductions of a few tenths of a percentage point. IF average pairwise correlation is high, say 0.8, AND .Thatisanear46nis20,THEN is 20, THEN is20,THEN\mathrm{Var}=\sigma^{2}(1/20+19/20\cdot0.8)=\sigma^{2}(0.05+0.76)=\sigma^{2}(0.81)$, so portfolio volatility remains about 90% of single-asset volatility, MAY be poor diversification BECAUSE high correlation moves assets together in stress. Correlation is not fixed. Empirical studies show cross-asset correlations rise from historical averages of 0.1-0.3 to 0.6-0.9 during crises lasting 3-18 months. That time-varying behavior means static diversification estimates understate tail risk. Practical metrics to monitor include weighted average correlation, equal-weighted effective number of bets, and marginal contribution to portfolio variance. Using these, an investor can estimate whether adding an asset meaningfully reduces portfolio variance by at least 0.5-1.0 percentage points in annualized volatility.

## The Decision Framework - IF/THEN/BECAUSE Rules for Applying Diversification

Problem-first rule making helps trade decisions. In Asset Classes (d3) we labeled equities for growth and bonds for stability. Combine that taxonomy with correlation to build allocations. IF horizon is short less than 3 years AND liquidity needs are high, THEN tilt toward cash and short-term bonds in the range 50-90% MAY reduce probability of forced sales BECAUSE lower volatility assets historically have annualized sigma of 0.5-3.0% versus 15-25% for equities. IF horizon is long 10-30 years AND the goal is long-term wealth growth, THEN broad exposure to equities across 3-6 regions and to 4-6 sectors in multiples of at least 20-30 holdings MAY increase expected geometric return BECAUSE cross-sectional diversification often reduces volatility by 30-60% and preserves compounding. For the tactical decision of adding an asset, use a marginal benefit test. IF an asset reduces portfolio variance by more than 0.25-0.5 percentage points in annualized volatility after costs, THEN adding it may be justified BECAUSE governance and trading costs then leave a net benefit. Costs matter. If an ETF costs 0.05% per year and an active fund costs 1.25% per year, then the active fund needs to improve expected return or lower volatility by roughly 1.2 percentage points per year to break even. Tax effects matter too. IF adding an asset triggers taxable events at 15-23% capital gains tax and immediate taxes exceed 0.5-1.0% of portfolio value, THEN after-tax benefit may be negative in the short run BECAUSE taxes reduce initial capital available for compounding. Rebalancing is part of the framework. IF rebalancing is done quarterly to maintain target weights within 3-6% bands, THEN it may harvest 0.5-1.5% additional return annually via systematic buy-low sell-high in volatile markets BECAUSE selling relative winners and buying losers captures volatility-driven gains, net of trading costs. Every decision contains trade-offs - more breadth reduces idiosyncratic risk and may lower expected arithmetic return by adding low-return assets, often by 0.0-2.0 percentage points, but can raise geometric return by reducing volatility drag by several tenths to several percentage points per year.

## Edge Cases and Limitations - Where the Framework Breaks Down

Diversification is not a panacea. First, correlations spike during crises. Empirical evidence shows cross-asset correlations rising from 0.2-0.4 in calm periods to 0.7-0.95 in stressed months. IF a portfolio relies on low correlations AND the next crisis elevates correlations to 0.8-0.95, THEN expected volatility reduction may evaporate quickly MAY causing returns to fall by 10-40% in months BECAUSE tail co-movement causes simultaneous draws across assets. Second, liquidity and implementation costs can negate theoretical gains. Buying less-liquid bonds or small-cap alternatives may incur spreads of 0.25-2.0% per trade and ongoing market impact costs of 0.1-1.0% annually. IF an investor adds illiquid assets without adjusting allocation sizes AND needs occasional withdrawals, THEN the portfolio may face forced selling at unfavorable prices MAY producing realized losses exceeding 5-20% BECAUSE thin markets widen bid-ask spreads under stress. Third, estimation error and overfitting undermine naive optimization. Historical covariance matrices estimated from 36-120 months of returns have sampling error that can produce unstable allocations varying by 10-50% across re-estimations. IF mean and covariance estimates are noisy AND optimization is used without regularization, THEN allocations may concentrate unintentionally MAY increasing risk BECAUSE the optimizer exploits estimation noise as if it were signal. Fourth, taxation and legal constraints can limit implementable diversification. Taxable investors who hold appreciated assets with 15-23% capital gains exposure may face after-tax tradeoffs that change the marginal benefit threshold by 0.5-2.0 percentage points. Finally, certain risks are non-diversifiable. Systemic inflation shocks, regulatory seizures, or currency regime changes can wipe out real purchasing power or access to assets. IF the scenario involves extreme macro shocks AND holdings are highly exposed to that shock, THEN diversification across financial assets may not protect principal MAY requiring alternative hedges BECAUSE all financial assets can correlate to macro stress when cash flows are impaired. This framework does not account for behavioral biases, human capital exposure, or private business concentration exceeding 30-60% of net worth. It also does not model path-dependent withdrawal sequences precisely, such as required minimum distributions during large drawdowns.

## Worked Examples (3)

### Two-Asset Portfolio Volatility Calculation

Investor has $100,000. Wants 60% equities and 40% bonds. Equity mean return 7% and sigma 15%. Bond mean return 2% and sigma 5%. Correlation is 0.2.

1. Compute portfolio expected return: E[Rp]=0.6⋅7%+0.4⋅2%=4.2%+0.8%=5.0%E[R\_p]=0.6\cdot7\%+0.4\cdot2\%=4.2\%+0.8\%=5.0\%E[Rp​]=0.6⋅7%+0.4⋅2%=4.2%+0.8%=5.0%.
2. Compute variance using formula Var=0.62(0.152)+0.42(0.052)+2(0.6)(0.4)(0.2)(0.15)(0.05)Var=0.6^{2}(0.15^{2})+0.4^{2}(0.05^{2})+2(0.6)(0.4)(0.2)(0.15)(0.05)Var=0.62(0.152)+0.42(0.052)+2(0.6)(0.4)(0.2)(0.15)(0.05).
3. Calculate terms: $0.6^{2}(0.15^{2})=0.36\cdot0.0225=0.0081$; $0.4^{2}(0.05^{2})=0.16\cdot0.0025=0.0004$; cross-term $2\cdot0.6\cdot0.4\cdot0.2\cdot0.15\cdot0.05=0.00072$.
4. Sum variance: $0.0081+0.0004+0.00072=0.00922;takesquareroot:; take square root: ;takesquareroot:\sigma\_{p}=\sqrt{0.00922}=9.6\%$.
5. Interpretation: With σp=9.6%\sigma\_{p}=9.6\%σp​=9.6% and E[Rp]=5.0%E[R\_p]=5.0\%E[Rp​]=5.0%, the portfolio volatility is materially lower than a 100% equity sigma of 15\%.

**Insight:** Adding a 40% bond sleeve reduced volatility from 15% to 9.6% while lowering expected arithmetic return by 2 percentage points. That decline in volatility can raise geometric returns by roughly 0.5-1.5 percentage points annually, depending on the true return distribution.

### Breadth Benefit with 20 Equal Stocks

Investor has $200,000 to split equally across 20 stocks. Assume each stock has sigma 20% and average pairwise correlation 0.25. Compute portfolio sigma.

1. Use equal-weighted variance formula: Var=σ2(1/n+(n−1)/n⋅ρˉ)Var=\sigma^{2}(1/n+(n-1)/n\cdot\bar{\rho})Var=σ2(1/n+(n−1)/n⋅ρˉ​).
2. Plug numbers: σ2=0.202=0.04\sigma^{2}=0.20^{2}=0.04σ2=0.202=0.04, n=20n=20n=20, ρˉ=0.25\bar{\rho}=0.25ρˉ​=0.25 so $1/n=0.05$, $(n-1)/n\cdot\bar{\rho}=0.95\cdot0.25=0.2375$.
3. Compute variance: $0.04(0.05+0.2375)=0.04\cdot0.2875=0.0115$.
4. Compute sigma: σp=0.0115=10.72%\sigma\_{p}=\sqrt{0.0115}=10.72\%σp​=0.0115​=10.72%.
5. Compare: Single-stock sigma 20% versus portfolio sigma 10.72% shows nearly 46% reduction in volatility.

**Insight:** With modest average correlation of 0.25, breadth across 20 names halves volatility and substantially reduces the volatility tax on compounding.

### Concentration Versus Diversification Over 10 Years

Two portfolios both have arithmetic mean return 8% annually. Portfolio A sigma 30%. Portfolio B sigma 12%. Start with $100,000 and hold 10 years.

1. Approximate geometric return with volatility drag: rgeo≈rarith−0.5σ2r\_{geo}\approx r\_{arith}-0.5\sigma^{2}rgeo​≈rarith​−0.5σ2.
2. Portfolio A: rgeo,A=8%−0.5(0.302)=8%−4.5%=3.5%r\_{geo,A}=8\%-0.5(0.30^{2})=8\%-4.5\%=3.5\%rgeo,A​=8%−0.5(0.302)=8%−4.5%=3.5%.
3. Portfolio B: rgeo,B=8%−0.5(0.122)=8%−0.72%=7.28%r\_{geo,B}=8\%-0.5(0.12^{2})=8\%-0.72\%=7.28\%rgeo,B​=8%−0.5(0.122)=8%−0.72%=7.28%.
4. Project values: A grows to $100,000(1+0.035)^{10}=100,000\cdot1.411\approx$ $141,100$; B grows to $100,000(1+0.0728)^{10}=100,000\cdot2.002\approx$ $200,200$.
5. Difference in terminal wealth is about $59,100 or 42% more for the diversified profile.

**Insight:** Lower volatility applied to the same arithmetic return can materially increase terminal wealth over a decade because of geometric compounding. Reducing sigma from 30% to 12% raised terminal wealth by roughly 40-60% in this example.

## Key Takeaways

- ✓

  Diversification is the deliberate spread across low-correlated assets to reduce portfolio volatility; typical reductions range from 30-60% when going from single-asset to 15-30 diversified holdings with average pairwise correlation 0.1-0.3.
- ✓

  Portfolio variance combines weights, variances, and correlations via Var=w⊤ΣwVar=w^{\top}\Sigma wVar=w⊤Σw; for equal weights, variance scales like σ2(1/n+(n−1)/nρˉ)\sigma^{2}(1/n+(n-1)/n\bar{\rho})σ2(1/n+(n−1)/nρˉ​).
- ✓

  Low correlation is the lever. If average pairwise correlation moves from 0.2 to 0.7, the same breadth can lose most of its benefit, raising portfolio sigma by 50-100%.
- ✓

  Practical decision rule - add an instrument only if it reduces portfolio annualized volatility by at least 0.25-0.5 percentage points after fees and taxes, since smaller gains are often eaten by costs.
- ✓

  Diversification reduces idiosyncratic risk but not systemic risk; expect crisis correlations of 0.6-0.95 for 3-18 months and plan liquidity buffers of 3-6 months expenses accordingly.

## Common Mistakes

- ✗

  Confusing the number of holdings with diversification depth. Holding 50 names with average correlation 0.7 often gives as little benefit as holding 5 names with correlation 0.2. That mistake ignores correlation, which drives marginal benefit.
- ✗

  Relying on historical correlations as fixed inputs. Historical averages over 36-120 months commonly understate crisis correlations by 0.3-0.7, which misprices tail risk and can produce unexpected drawdowns.
- ✗

  Neglecting implementation costs and taxes. Buying a 1.25% expense active fund expecting a 1% volatility improvement usually produces worse after-fee outcomes than a 0.05% index ETF that reduces volatility similarly.
- ✗

  Optimizing blindly on estimated means and covariances. Sample noise can cause optimizer overconcentration shifts of 10-50% between re-estimations, which increases realized tracking error and risk.

## Practice

easy

Easy: Calculate portfolio volatility for $100,000 split 50% equities and 50% bond fund. Equities: mean 8%, sigma 16%. Bonds: mean 3%, sigma 4%. Correlation 0.15. Compute expected return and portfolio sigma.

**Hint:** Use E[Rp]=w1μ1+w2μ2E[R\_p]=w\_1\mu\_1+w\_2\mu\_2E[Rp​]=w1​μ1​+w2​μ2​ and two-asset variance formula Var=w12σ12+w22σ22+2w1w2ρσ1σ2Var=w\_1^{2}\sigma\_1^{2}+w\_2^{2}\sigma\_2^{2}+2w\_1w\_2\rho\sigma\_1\sigma\_2Var=w12​σ12​+w22​σ22​+2w1​w2​ρσ1​σ2​.

Show solution

Expected return E[Rp]=0.5⋅8%+0.5⋅3%=4%+1.5%=5.5%E[R\_p]=0.5\cdot8\%+0.5\cdot3\%=4\%+1.5\%=5.5\%E[Rp​]=0.5⋅8%+0.5⋅3%=4%+1.5%=5.5%. Variance =0.52(0.162)+0.52(0.042)+2⋅0.5⋅0.5⋅0.15⋅0.16⋅0.04=0.25⋅0.0256+0.25⋅0.0016+0.015⋅0.0064=0.0064+0.0004+0.000096=0.006896=0.5^{2}(0.16^{2})+0.5^{2}(0.04^{2})+2\cdot0.5\cdot0.5\cdot0.15\cdot0.16\cdot0.04=0.25\cdot0.0256+0.25\cdot0.0016+0.015\cdot0.0064=0.0064+0.0004+0.000096=0.006896=0.52(0.162)+0.52(0.042)+2⋅0.5⋅0.5⋅0.15⋅0.16⋅0.04=0.25⋅0.0256+0.25⋅0.0016+0.015⋅0.0064=0.0064+0.0004+0.000096=0.006896. Sigma =0.006896=8.31%=\sqrt{0.006896}=8.31\%=0.006896​=8.31%.

medium

Medium: You have $150,000 to allocate between a domestic equity ETF (sigma 18%) and an international equity ETF (sigma 20%). You consider two allocations: A) 70% domestic, 30% international, B) 50%/50%. If correlation between them is 0.6 and expected returns both 8%, which allocation yields lower portfolio sigma? Compute both sigmas and pick the lower one.

**Hint:** Use two-asset variance formula and compare σp\sigma\_pσp​ for each weighting.

Show solution

Allocation A weights w1=0.7, w2=0.3. Variance A = 0.7^{2}0.18^{2}+0.3^{2}0.20^{2}+2\cdot0.7\cdot0.3\cdot0.6\cdot0.18\cdot0.20. Calculate terms: 0.49\cdot0.0324=0.015876; 0.09\cdot0.04=0.0036; cross-term 0.42\cdot0.6\cdot0.036=0.42\cdot0.0216=0.009072. Sum =0.028548. Sigma\_A = sqrt(0.028548)=16.9%. Allocation B weights 0.5/0.5. Variance B =0.25\cdot0.0324+0.25\cdot0.04+2\cdot0.5\cdot0.5\cdot0.6\cdot0.18\cdot0.20=0.0081+0.01+0.054\cdot0.036? Recompute cross-term: 2*0.5*0.5=0.5; 0.5*0.6*0.036=0.5\*0.0216=0.0108. Sum =0.0081+0.01+0.0108=0.0289. Sigma\_B = sqrt(0.0289)=17.0%. Lower sigma is Allocation A at 16.9% by a tiny margin.

hard

Hard: You own a concentrated small business valued at $300,000 that represents 60% of your $500,000 net worth. You can diversify by selling 30% of the business for $90,000 and buying a diversified equity ETF. Transaction costs and tax on gains total 18% of sale proceeds. Demonstrate whether selling reduces portfolio volatility if the business has sigma 40% and the ETF sigma 18% with correlation 0.3. Compute initial portfolio sigma and post-sale sigma, and account for the 18% tax reducing reinvested proceeds.

**Hint:** Model portfolio as two assets: business and financial portfolio. After selling, financial portfolio increases and weight of business drops. Remember to reduce proceeds by tax: $90,000\cdot(1-0.18)=73,800 reinvested.

Show solution

Initial net worth 500,000. Business 300,000 (w\_b=0.6), financial assets 200,000 (w\_f=0.4) with sigma\_b=40% and sigma\_f=18%, rho=0.3. Initial variance =0.6^{2}0.4^{2}+0.4^{2}0.18^{2}+2\cdot0.6\cdot0.4\cdot0.3\cdot0.4\cdot0.18. Compute terms: 0.36\cdot0.16=0.0576; 0.16\cdot0.0324=0.005184; cross-term 0.48\cdot0.3\cdot0.072=0.48\cdot0.0216=0.010368. Sum variance =0.0576+0.005184+0.010368=0.073152. Sigma\_initial = sqrt(0.073152)=27.05%. After selling 30% of business, business value becomes 210,000. Proceeds before tax 90,000, after tax reinvested 73,800. New financial assets value =200,000+73,800=273,800. New total net worth =210,000+273,800=483,800. New weights: w\_b=210,000/483,800=0.434, w\_f=0.566. Variance new =0.434^{2}0.4^{2}+0.566^{2}0.18^{2}+2\cdot0.434\cdot0.566\cdot0.3\cdot0.4\cdot0.18. Compute terms: 0.1884\cdot0.16=0.030144; 0.320\cdot0.0324=0.010368; cross-term 0.491\cdot0.3\cdot0.072=0.491\cdot0.0216=0.010606. Sum variance =0.030144+0.010368+0.010606=0.051118. Sigma\_new = sqrt(0.051118)=22.61%. Net volatility dropped from 27.05% to 22.61%, a reduction of about 4.4 percentage points. After-tax proceeds reduced reinvested capital by 18%, but diversification still materially lowered portfolio sigma. Note final net worth is down by $16,200 due to tax; that reduces total capital available but still achieves risk reduction.

## Connections

This lesson builds on Asset Classes (d3) where equities, bonds, cash, real assets, and commodities were defined with typical risk-return profiles. Understanding diversification enables later topics such as Portfolio Optimization and Mean-Variance theory (/money/d7), Risk Parity and Volatility Targeting strategies (/money/d8), and Tax-Aware Rebalancing workflows (/money/d12). Specifically, Portfolio Optimization (/money/d7) uses the variance formulas here to set weights, while Tax-Aware Rebalancing (/money/d12) uses the trade-off rules about taxes and transaction costs explained in the Decision Framework section.

**Disclaimer:** This content is for educational and informational purposes only and does not constitute financial, investment, tax, or legal advice. It is not a recommendation to buy, sell, or hold any security or financial product. You should consult a qualified financial advisor, tax professional, or attorney before making financial decisions. Past performance is not indicative of future results. The author is not a registered investment advisor, broker-dealer, or financial planner.

[← back to tree](/money/)[browse all →](/money/inventory/)
