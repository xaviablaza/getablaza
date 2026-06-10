---
title: Price Elasticity
description: Own-price, cross-price, and income elasticity of demand. Elastic vs inelastic regions. Log-log demand models and constant-elasticity forms.
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- tech-tree
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
generated_by: templeton-deep-copy-import
permalink: /tech-tree/price-elasticity/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Price Elasticity

Applied EconomicsDifficulty: ★★★☆☆Depth: 9Unlocks: 1

Own-price, cross-price, and income elasticity of demand. Elastic vs inelastic regions. Log-log demand models and constant-elasticity forms.

## Prerequisites (2)

[Demand Functions? atoms](/tech-tree/demand-functions/)[Derivatives6 atoms](/tech-tree/derivatives-basic/)

## Unlocks (1)

[Competitive Pricinglvl 5](/tech-tree/competitive-pricing/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[PricingBusiness

Elasticity is the core measurement tool for pricing - you cannot set price without understanding how demand responds to price changes, and log-log demand models are the workhorse of applied pricing](/business/pricing/)

Advanced Learning Details

### Graph Position

55

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

9

Chain Length

Price elasticities tell you how buyers react to price, substitute prices, and income — the single most practical set of numbers for pricing, forecasting, and policy. Get them wrong and you mis-price products, misestimate tax revenue, or mis-predict market responses.

TL;DR:

Price elasticity measures percent-response of demand to percent-changes in prices or income; you can compute point elasticities with derivatives and estimate constant elasticities with log–log models for clear economic interpretation.

## What Is Price Elasticity?

Definition and core intuition

Price elasticity of demand summarizes how much quantity demanded changes when an economic variable (price, other price, or income) changes, measured in percent terms. Because it is a percent change, elasticity is unit-free and comparable across goods and contexts.

There are three standard elasticities:

- •Own-price elasticity (often written εp\varepsilon\_{p}εp​ or εq,p\varepsilon\_{q,p}εq,p​): percent change in quantity demanded for a 1% change in the good's own price.
- •Cross-price elasticity (εq,p′\varepsilon\_{q,p'}εq,p′​): percent change in demand for good A for a 1% change in the price of good B.
- •Income elasticity (εq,y\varepsilon\_{q,y}εq,y​): percent change in demand for a 1% change in income.

Formal (point) definition uses calculus and the derivative — recall from "Derivatives (d2)" how to compute instantaneous rates of change. If demand is q(q)q(q)q(q) written as a function of price ppp (a Marshallian demand from "Demand Functions (d3)"), the point own-price elasticity is

εp=dqdp⋅pq.\varepsilon\_{p} = \frac{dq}{dp} \cdot \frac{p}{q}.εp​=dpdq​⋅qp​.

Concrete numeric example: Suppose q(p)=100−2pq(p)=100-2pq(p)=100−2p. Then dq/dp=−2dq/dp=-2dq/dp=−2. At p=10p=10p=10, q(10)=100−20=80q(10)=100-20=80q(10)=100−20=80. So

εp=−2⋅1080=−0.25.\varepsilon\_{p} = -2 \cdot \frac{10}{80} = -0.25.εp​=−2⋅8010​=−0.25.

Interpretation: a 1% increase in price (~$0.10 increase at p=10p=10p=10) reduces quantity by 0.25% (about 0.2 units), so demand is inelastic at that point.

Signs and classification

- •Own-price elasticity is typically negative for normal goods (higher price reduces demand). We often drop the sign and speak of elasticity magnitude: |\varepsilon|. If |\varepsilon|>1, demand is "elastic"; if |\varepsilon|<1, demand is "inelastic".
- •Cross-price elasticity is positive for substitutes, negative for complements. Example numeric: if qA=30−2pA+0.5pBq\_A=30-2p\_A+0.5p\_BqA​=30−2pA​+0.5pB​ then ∂qA/∂pB=0.5\partial q\_A/\partial p\_B=0.5∂qA​/∂pB​=0.5, so cross-price elasticity at pB=20,qA=10p\_B=20, q\_A=10pB​=20,qA​=10 is $0.5\cdot 20/10 =1.0$.
- •Income elasticity >0 indicates a normal good, <0 an inferior good.

Why percent changes? Percent measures are scale-free and align with economic behavior (many responses are multiplicative). For small changes, percent changes are approximated by derivatives, which ties directly to calculus from "Derivatives (d2)".

Elastic vs inelastic regions

Elasticity can vary along a demand curve. For linear demand q=100−2pq=100-2pq=100−2p, elasticity depends on ppp because dq/dpdq/dpdq/dp is constant but qqq changes with ppp. At p=10p=10p=10 we found ε=−0.25\varepsilon=-0.25ε=−0.25 (inelastic); at p=40p=40p=40, q=20q=20q=20 so ε=−2⋅40/20=−4\varepsilon=-2\cdot40/20=-4ε=−2⋅40/20=−4 (elastic). Thus, the same linear demand is inelastic at low prices (high quantities) and elastic at high prices (low quantities). This matters for pricing decisions: raising price increases revenue when demand is inelastic, but decreases revenue when elastic (numeric demonstration follows in later sections).

Connection to prerequisites

In "Demand Functions (d3)" we derived Marshallian demand functions from utility maximization; those functions are the input to elasticity formulas. In "Derivatives (d2)" we learned how to compute dq/dpdq/dpdq/dp; that derivative is essential to the point-elasticity formula above. The rest of this lesson builds directly on those tools.

## Core Mechanic 1 — Computing Elasticities (own, cross, income)

Formulas and step-by-step calculations

We compute point elasticities using partial derivatives of the demand function. Suppose a demand for good i is qi(pi,pj,y)q\_i(p\_i, p\_j, y)qi​(pi​,pj​,y) where pip\_ipi​ is its price, pjp\_jpj​ other prices, and yyy income. The standard formulas are:

- •Own-price elasticity:

εi,pi=∂qi∂pi⋅piqi.\varepsilon\_{i,p\_i} = \frac{\partial q\_i}{\partial p\_i} \cdot \frac{p\_i}{q\_i}.εi,pi​​=∂pi​∂qi​​⋅qi​pi​​.

Numeric example: Let q(p)=120−3pq(p)=120-3pq(p)=120−3p. Then ∂q/∂p=−3\partial q/\partial p=-3∂q/∂p=−3. At p=10p=10p=10, q=120−30=90q=120-30=90q=120−30=90, so ε=−3⋅10/90=−0.333...\varepsilon=-3\cdot10/90=-0.333...ε=−3⋅10/90=−0.333... (inelastic).

- •Cross-price elasticity with respect to pjp\_jpj​:

εi,pj=∂qi∂pj⋅pjqi.\varepsilon\_{i,p\_j} = \frac{\partial q\_i}{\partial p\_j} \cdot \frac{p\_j}{q\_i}.εi,pj​​=∂pj​∂qi​​⋅qi​pj​​.

Numeric example: If qA=50−2pA+0.4pBq\_A=50-2p\_A+0.4p\_BqA​=50−2pA​+0.4pB​ and at (pA,pB)=(10,20)(p\_A,p\_B)=(10,20)(pA​,pB​)=(10,20) we have qA=50−20+8=38q\_A=50-20+8=38qA​=50−20+8=38, then ∂qA/∂pB=0.4\partial q\_A/\partial p\_B=0.4∂qA​/∂pB​=0.4 and

εA,pB=0.4⋅2038≈0.2105.\varepsilon\_{A,p\_B}=0.4\cdot\frac{20}{38}\approx0.2105.εA,pB​​=0.4⋅3820​≈0.2105.

Interpretation: a 1% increase in pBp\_BpB​ raises qAq\_AqA​ by 0.21% (they are substitutes).

- •Income elasticity:

εi,y=∂qi∂y⋅yqi.\varepsilon\_{i,y} = \frac{\partial q\_i}{\partial y} \cdot \frac{y}{q\_i}.εi,y​=∂y∂qi​​⋅qi​y​.

Numeric example: If q=5+0.2y−1.5pq=5+0.2y-1.5pq=5+0.2y−1.5p and (y,p)=(100,10)(y,p)=(100,10)(y,p)=(100,10) then q=5+20−15=10q=5+20-15=10q=5+20−15=10, ∂q/∂y=0.2\partial q/\partial y=0.2∂q/∂y=0.2, so εy=0.2⋅100/10=2.0\varepsilon\_{y}=0.2\cdot100/10=2.0εy​=0.2⋅100/10=2.0, a luxury good (income-elastic >1).

Arc elasticity for finite changes

Point elasticities describe infinitesimal changes. For large discrete changes, use arc elasticity (midpoint formula):

εarc=Δq/qˉΔp/pˉ=q2−q1(q1+q2)/2/p2−p1(p1+p2)/2.\varepsilon\_{arc} = \frac{\Delta q/\bar q}{\Delta p/\bar p} = \frac{q\_2-q\_1}{(q\_1+q\_2)/2} \bigg/ \frac{p\_2-p\_1}{(p\_1+p\_2)/2}.εarc​=Δp/pˉ​Δq/qˉ​​=(q1​+q2​)/2q2​−q1​​/(p1​+p2​)/2p2​−p1​​.

Numeric example: Price goes from p1=10p\_1=10p1​=10 to p2=15p\_2=15p2​=15 for a demand where q1=80,q2=50q\_1=80,q\_2=50q1​=80,q2​=50. Then

εarc=50−80(80+50)/2/15−10(10+15)/2=−30/655/12.5=−0.4615/0.4=−1.1538.\varepsilon\_{arc} = \frac{50-80}{(80+50)/2} \bigg/ \frac{15-10}{(10+15)/2} = \frac{-30/65}{5/12.5} = -0.4615 / 0.4 = -1.1538.εarc​=(80+50)/250−80​/(10+15)/215−10​=5/12.5−30/65​=−0.4615/0.4=−1.1538.

Sign conventions and intuition

- •A negative own-price elasticity means a price increase reduces demand. We typically report the absolute value for magnitude comparisons.
- •If |\varepsilon|>1 demand is elastic: percent change in quantity exceeds percent change in price.
- •If |\varepsilon|<1 demand is inelastic: quantity responds less than proportionately.

Revenue consequences (numerical rule)

Total revenue R(p)=p⋅q(p)R(p)=p\cdot q(p)R(p)=p⋅q(p). Take derivative using product rule:

dRdp=q+pdqdp=q(1+pqdqdp)=q(1+εp).\frac{dR}{dp}=q + p\frac{dq}{dp} = q\left(1+\frac{p}{q}\frac{dq}{dp}\right)=q(1+\varepsilon\_{p}).dpdR​=q+pdpdq​=q(1+qp​dpdq​)=q(1+εp​).

So:

- •If εp<−1\varepsilon\_{p}<-1εp​<−1 (elastic), dR/dp<0dR/dp<0dR/dp<0: raising price reduces revenue.
- •If εp>−1\varepsilon\_{p}>-1εp​>−1 (inelastic), dR/dp>0dR/dp>0dR/dp>0: raising price increases revenue.

Numeric example: For q=120−3pq=120-3pq=120−3p at p=10p=10p=10 we found ε=−0.333...\varepsilon=-0.333...ε=−0.333.... Then dR/dp=q(1+ε)=90(0.6667)=60>0dR/dp=q(1+\varepsilon)=90(0.6667)=60>0dR/dp=q(1+ε)=90(0.6667)=60>0, so raising price increases revenue locally.

Connection to "Derivatives (d2)" and "Demand Functions (d3)"

All point elasticity formulas rely on computing partial derivatives from the demand function (as in "Derivatives (d2)"), and the demand function itself may be derived from utility maximization (Marshallian demand) as studied in "Demand Functions (d3)". If you have a Marshallian demand, apply these derivative formulas to get the economic elasticities.

## Core Mechanic 2 — Log–log (constant-elasticity) demand models

Motivation and algebra

Empirically and theoretically, it is common to model demand in "log–log" form because coefficients directly equal elasticities. A log–log model writes demand as:

ln⁡q=α+βln⁡p+γln⁡y+∑kδkln⁡pk+ε,\ln q = \alpha + \beta \ln p + \gamma \ln y + \sum\_k \delta\_k \ln p\_k + \varepsilon,lnq=α+βlnp+γlny+k∑​δk​lnpk​+ε,

where β\betaβ is the own-price elasticity, γ\gammaγ the income elasticity, and each δk\delta\_kδk​ is a cross-price elasticity. If the error term ε\varepsilonε is small or mean-zero, point estimates of β\betaβ give constant elasticities across observations.

Equivalently, exponential form (constant-elasticity functional form) is:

q=A⋅pβ⋅yγ⋅∏kpkδk⋅eε,q = A \cdot p^{\beta} \cdot y^{\gamma} \cdot \prod\_k p\_k^{\delta\_k} \cdot e^{\varepsilon},q=A⋅pβ⋅yγ⋅k∏​pkδk​​⋅eε,

where A=eαA=e^{\alpha}A=eα.

Concrete numeric example: Suppose empirical estimates give α=3.912,β=−1.5,γ=0.8\alpha=3.912, \beta=-1.5, \gamma=0.8α=3.912,β=−1.5,γ=0.8. Then the model implies

q=e3.912⋅p−1.5⋅y0.8.q= e^{3.912} \cdot p^{-1.5} \cdot y^{0.8}.q=e3.912⋅p−1.5⋅y0.8.

Compute a concrete number: take p=10,y=100p=10, y=100p=10,y=100. Then e3.912≈49.98e^{3.912}\approx 49.98e3.912≈49.98 and

q≈49.98⋅10−1.5⋅1000.8=49.98⋅0.03162⋅63.0957≈99.7.q\approx49.98\cdot10^{-1.5}\cdot100^{0.8} =49.98\cdot0.03162\cdot63.0957\approx99.7.q≈49.98⋅10−1.5⋅1000.8=49.98⋅0.03162⋅63.0957≈99.7.

Interpretation: a 1% increase in ppp reduces qqq by 1.5% exactly, at all points.

Why constant elasticity is useful

- •Interpretability: coefficients equal elasticities directly without multiplication by p/q.
- •Estimation: regressions of ln⁡q\ln qlnq on ln⁡p\ln plnp yield coefficient estimates that are standard errors and hypothesis-testable.
- •Multiplicative effects: percentage impacts add when variables change multiplicatively.

From log–log to numerical elasticity

If you estimate β^=−1.5\hat\beta=-1.5β^​=−1.5, then at any observed point the own-price elasticity is −1.5-1.5−1.5. Numeric check: if ppp rises by 2%, predicted qqq falls by 3%.

Revenue and optimization in constant-elasticity form

If demand is q=Apβq=A p^{\beta}q=Apβ (ignore income for simplicity) then revenue is

R(p)=p⋅Apβ=Apβ+1.R(p)=p\cdot A p^{\beta}=A p^{\beta+1}.R(p)=p⋅Apβ=Apβ+1.

Revenue-maximizing price occurs when dR/dp=0dR/dp=0dR/dp=0, but monotonicity depends on β+1\beta+1β+1. If β<−1\beta<-1β<−1, revenue decreases with price; if β>−1\beta>-1β>−1, revenue increases. However, for monopoly with constant marginal cost ccc the profit-maximizing price uses the Lerner formula (requires elasticity):

p−cp=−1εp.\frac{p-c}{p} = -\frac{1}{\varepsilon\_{p}}.pp−c​=−εp​1​.

Numeric example: If εp=−2\varepsilon\_{p}=-2εp​=−2 and c=10c=10c=10, then (p−10)/p=0.5(p-10)/p=0.5(p−10)/p=0.5, so p=20p=20p=20.

Estimation notes and small-change approximation

For small price changes Δp/p\Delta p/pΔp/p the percent change in quantity is approximately εp⋅Δp/p\varepsilon\_{p}\cdot \Delta p/pεp​⋅Δp/p. Numeric example: with ε=−1.5\varepsilon=-1.5ε=−1.5, a 2% price rise implies a 3% fall in quantity.

Every formula must link to a numeric example: the algebra above applied α,β,γ\alpha,\beta,\gammaα,β,γ to p=10,y=100p=10,y=100p=10,y=100 to compute q≈99.7q\approx99.7q≈99.7.

Limitations and edge cases

- •Log–log requires strictly positive variables (prices, quantities, income). If zeros occur, you must use alternative specifications or add small constants (with caveats).
- •Constant elasticity is an approximation; real demand may vary with income and prices in non-constant ways. Compare constant-elasticity prediction to a linear demand numeric example: linear q=100−2pq=100-2pq=100−2p at p=10p=10p=10 gave elasticity -0.25, but no single constant matches the whole curve.

Connection to prerequisites

You use "Derivatives (d2)" implicitly when differentiating ln⁡q\ln qlnq to show the elasticity equals the slope: $dln⁡qdln⁡p=β.\frac{d\ln q}{d\ln p}=\beta.dlnpdlnq​=β.Also,if Also, if Also,ifq(p)$ stems from a Marshallian demand in "Demand Functions (d3)", you can log-transform that demand and interpret estimated coefficients as elasticities if the functional form fits.

## Applications and Connections

Practical uses for elasticities

1) Pricing strategy and revenue forecasting

Firms use price elasticity to decide whether to raise or lower price. The rule (numeric) is: if local |\varepsilon|<1 (inelastic), raising price increases revenue; if |\varepsilon|>1 (elastic), lowering price increases revenue. Example numeric: demand q=120−3pq=120-3pq=120−3p at p=10p=10p=10 had |\varepsilon|=0.333 so a price hike increases revenue.

2) Monopoly pricing and markups (Lerner index)

Monopolists set price using elasticity: $p−MCp=−1ε.\frac{p-MC}{p}=-\frac{1}{\varepsilon}.pp−MC​=−ε1​.$

Numeric example: with constant marginal cost MC=5MC=5MC=5 and elasticity ε=−2\varepsilon=-2ε=−2, the markup fraction is 0.5, so p=10p=10p=10.

3) Tax incidence and welfare analysis

Elasticity governs how much of a per-unit tax is passed to consumers vs producers. If demand is perfectly inelastic (|\varepsilon|=0), consumers bear full tax; if perfectly elastic (|\varepsilon|=\infty), producers bear it. Numeric illustration: small tax ttt with linear demand and supply changes quantity; compute pass-through using elasticities.

4) Cross-price effects and product relationships

Cross-price elasticities tell whether goods are substitutes or complements and by how much. Example numeric: a cross-elasticity of 0.8 between two beverages implies a 10% price increase for B raises A’s demand by 8%.

5) Income elasticity for forecasting and product classification

Income elasticity distinguishes luxuries (elasticity>1), necessities (0<elasticity<1), and inferior goods (elasticity<0). Example numeric: gasoline income elasticity 0.2 implies a 10% income rise increases demand by 2%.

Empirical estimation and data issues

- •When estimating elasticities from data, log–log regressions give constant elasticity estimates. Example numerical regression output: ln⁡q=3.9−1.5ln⁡p+0.8ln⁡y\ln q = 3.9 -1.5\ln p + 0.8\ln ylnq=3.9−1.5lnp+0.8lny implies own-price elasticity -1.5.
- •Beware of endogeneity: price may be correlated with unobserved demand shocks. Instrumental variables are often required.
- •For bounded or zero quantities, log specifications are problematic; consider linear or Poisson pseudo-maximum-likelihood variants.

Downstream connections (what this enables)

Elasticities are inputs to:

- •Welfare analysis (consumer surplus change): small-change approximation uses ΔCS≈−∫pdq\Delta CS \approx -\int p dqΔCS≈−∫pdq, which simplifies using elasticity in constant-elasticity models.
- •General equilibrium and policy analysis: elasticities feed into CGE models to simulate tax or subsidy effects.
- •Industrial organization: demand elasticities are central to merger simulation, mark-up models, and demand estimation.

Numeric policy example: If demand for cigarettes has price elasticity -0.4, a 10% tax increase (raising price by 10%) reduces demand by 4% and increases tax revenue roughly by 6% (because demand is inelastic).

Summary

Price elasticities translate derivative information from "Derivatives (d2)" into economically meaningful percent changes. They rely on demand functions derived in "Demand Functions (d3)" and feed into pricing, tax policy, welfare calculations, and empirical demand estimation. Constant-elasticity (log–log) forms make interpretation straightforward and are widely used in applied work, but always check fit and consider endogeneity and zero observations.

## Worked Examples (3)

### Own-price elasticity for a linear demand

Demand q(p)=150 - 5p. Compute the own-price elasticity at p=20 and determine whether demand is elastic or inelastic there.

1. Compute the derivative: dq/dp = -5 (from "Derivatives (d2)").
2. Evaluate quantity at p=20: q(20)=150 - 5\*20 = 150 - 100 = 50.
3. Apply point-elasticity formula: ε\_p = (dq/dp)  *(p/q) = -5*  (20/50).
4. Compute numerical value: -5 \* 0.4 = -2.0.
5. Interpretation: |ε| = 2.0 > 1, so demand is elastic at p=20; a 1% price increase reduces demand by 2%.

**Insight:** A constant slope linear demand can have very different elasticity at different prices; despite a constant derivative, the p/q ratio changes elasticity along the curve.

### Cross-price and income elasticity in a linear system

Two-good linear Marshallian demand: q\_A = 40 - 1.5 p\_A + 0.6 p\_B + 0.25 y. Evaluate cross-price elasticity of q\_A with respect to p\_B and income elasticity at (p\_A,p\_B,y)=(8,12,50).

1. Compute partial derivatives: ∂q\_A/∂p\_B = 0.6 and ∂q\_A/∂y = 0.25.
2. Evaluate q\_A at the point: q\_A = 40 - 1.5*8 + 0.6*12 + 0.25\*50 = 40 - 12 + 7.2 + 12.5 = 47.7.
3. Cross-price elasticity: ε\_{A,p\_B} = 0.6  *(p\_B/q\_A) = 0.6*  (12/47.7) ≈ 0.6 \* 0.2516 ≈ 0.15096.
4. Income elasticity: ε\_{A,y} = 0.25  *(y/q\_A) = 0.25*  (50/47.7) ≈ 0.25 \* 1.0484 ≈ 0.2621.
5. Interpretation: q\_A and p\_B are substitutes (positive cross-elasticity ≈ 0.15); income elasticity ≈ 0.26 indicates a necessity (positive but <1).

**Insight:** Linear additive models produce constant partial derivatives, but elasticities vary with the evaluation point through the p/q ratio. Cross-price elasticity magnitude helps classify the closeness of substitutes quantitatively.

### Log–log demand, elasticity, and monopoly markup

Suppose ln q = 4.5 - 1.8 ln p + 0.6 ln y (no other prices). Take y=200 (income fixed). Marginal cost MC = 8. Compute (a) predicted q at p=12, (b) confirm elasticity, and (c) compute monopoly optimal price given constant MC.

1. Convert coefficients to multiplicative form: A = e^{4.5} ≈ 90.017. So q = 90.017  *p^{-1.8}*  y^{0.6}.
2. Compute q at p=12, y=200: y^{0.6} = 200^{0.6} ≈ e^{0.6 ln 200} ≈ e^{0.6*5.2983} ≈ e^{3.17898} ≈ 24.01. p^{-1.8} = 12^{-1.8} = e^{-1.8 ln 12} ≈ e^{-1.8*2.4849} ≈ e^{-4.4728} ≈ 0.0114.
3. So q ≈ 90.017  *0.0114*  24.01 ≈ 90.017 \* 0.2737 ≈ 24.64.
4. Elasticity check: coefficient on ln p is -1.8, so own-price elasticity is -1.8 at every point. A 1% price increase reduces q by 1.8%.
5. Monopoly pricing: Lerner index (p-MC)/p = -1/ε = -1/(-1.8) = 0.5556. So p = MC/(1 - 1/ε) = MC/(1 - (-1/1.8)) but simpler: p = MC / (1 - (-1/1.8)) compute numerically: (p - 8)/p = 0.5556 => p(1 - 0.5556) = 8 => 0.4444 p = 8 => p ≈ 18.
6. Conclude: a monopolist with MC=8 and elasticity -1.8 sets p≈18, which is higher than MC consistent with positive markup.

**Insight:** Log–log specification gives constant elasticity making the Lerner-rule application trivial. The numeric steps show how to compute actual q and the monopoly price from estimated elasticities.

## Key Takeaways

- ✓

  Point elasticity formula: ε = (∂q/∂p) \* (p/q) converts derivatives from "Derivatives (d2)" into percent responses.
- ✓

  Own-price, cross-price, and income elasticities differ only by which partial derivative you use; each is unit-free and interpretable as percent-change responses.
- ✓

  Elastic vs inelastic is determined by magnitude: |ε|>1 is elastic (quantity very responsive), |ε|<1 is inelastic (quantity relatively unresponsive).
- ✓

  Linear demand has constant slope but variable elasticity along the curve; log–log (constant-elasticity) models have constant elasticities at all points.
- ✓

  Log–log regression coefficients equal elasticities directly; numeric example: ln q = α + β ln p ⇒ β is own-price elasticity.
- ✓

  Elasticities drive pricing and policy: revenue effects, monopoly markups via Lerner index p−MC / p = −1/ε, tax incidence, and welfare calculations.
- ✓

  Be careful with zeros and endogeneity in empirical work; log specifications require positive values and instruments often required for causal elasticity estimates.

## Common Mistakes

- ✗

  Confusing slope with elasticity: slope (dq/dp) has units and is not comparable across goods; elasticity multiplies slope by p/q to be unit-free. For example, dq/dp = -2 vs elasticity at p=10,q=80 gives -0.25.
- ✗

  Using log–log with zeros or negatives: taking ln(0) is undefined. If data have zeros, do not blindly log-transform; consider alternative models or justified small-value adjustments.
- ✗

  Interpreting regression coefficient as causal without checking endogeneity: price may be endogenous (correlated with shocks to demand). Instrumental variables may be required to recover causal elasticities.
- ✗

  Reporting elasticity sign incorrectly: own-price elasticities are usually negative; reporting their signless value without stating the sign can lead to confusion about direction of change.

## Practice

easy

Easy: For demand q=200 - 4p, compute the own-price elasticity at p=30 and state whether demand is elastic or inelastic there.

**Hint:** Use ε = (dq/dp) \* (p/q). Compute q at p first.

Show solution

dq/dp = -4. q(30) = 200 - 120 = 80. ε = -4 \* (30/80) = -1.5. |ε|>1 so demand is elastic at p=30.

medium

Medium: You estimate ln q = 2.5 - 0.9 ln p + 0.4 ln y. If price rises by 3% and income rises by 2% simultaneously, approximately what percent change in q do you predict? Show numeric calculation.

**Hint:** Use linearity in logs: Δ ln q ≈ β Δ ln p + γ Δ ln y where percent change ≈ Δ ln (variable).

Show solution

Δ ln q ≈ -0.9  *0.03 + 0.4*  0.02 = -0.027 + 0.008 = -0.019. So q falls by about 1.9%.

hard

Hard: Consider demand q = 80 - 2p + 0.5z where z is the price of a close substitute. At current (p,z)=(20,30) a per-unit tax t of 2 is imposed on the good (increasing its price to p+t if fully passed on). Compute the approximate change in quantity if the producer passes the full tax to consumers, and compute the point elasticity at the new price. Then discuss how partial pass-through would change the numeric result. (Requires combining elasticity computation with substitution effect.)

**Hint:** First compute q before and after tax assuming full pass-through. Then compute elasticity at new price using dq/dp and p/q. For partial pass-through α in [0,1], the price change is α t.

Show solution

Initial q = 80 - 2*20 + 0.5*30 = 80 - 40 + 15 = 55. If full pass-through, p becomes 22 so q' = 80 - 2*22 + 0.5*30 = 80 - 44 + 15 = 51. Change in quantity = -4. Point elasticity at p'=22: dq/dp = -2, q'=51 so ε = -2  *(22/51) ≈ -0.8627 (inelastic). If pass-through is partial α (price increases by α*2), the quantity change is Δq = -2  *(α*2) = -4α, and new elasticity ε(α) = -2  *( (20+2α) / (55 -4α) ). Thus partial pass-through reduces the absolute change in quantity linearly in α; pass-through also slightly changes elasticity because p/q changes. If α=0.5, Δq=-2, q=53, ε≈ -2*(21/53)≈ -0.792.

## Connections

Looking back: this lesson applies tools from "Demand Functions (d3)" — the Marshallian demand functions you learned provide the q(p, p\' , y) inputs used in elasticity formulas — and from "Derivatives (d2)" — computing ∂q/∂p is exactly the derivative operation you practiced. Looking forward: elasticities are foundational inputs for welfare analysis (consumer and producer surplus changes), tax incidence and public finance models, industrial-organization topics like monopoly pricing and merger simulation, and empirical demand estimation (including IV techniques and panel methods). For instance, computing deadweight loss after a tax requires the price elasticity of demand; designing optimal taxes uses income and cross-price elasticities; and many IO models require own- and cross-price elasticities to form demand systems used in merger or pricing counterfactuals. Understanding elasticity also prepares you for advanced estimation choices (e.g., when to use log–log vs linear specifications) and for micro-econometric concerns such as endogeneity and censoring.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
