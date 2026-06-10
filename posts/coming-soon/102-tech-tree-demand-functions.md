---
title: Demand Functions
description: Demand curves derived from utility maximization. Inverse demand, market demand aggregation. Marshallian vs Hicksian demand.
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
permalink: /tech-tree/demand-functions/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Demand Functions

Applied EconomicsDifficulty: ★★★☆☆Depth: 8Unlocks: 8

Demand curves derived from utility maximization. Inverse demand, market demand aggregation. Marshallian vs Hicksian demand.

## Prerequisites (2)

[Utility Theory? atoms](/tech-tree/utility-theory/)[Derivatives6 atoms](/tech-tree/derivatives-basic/)

## Unlocks (3)

[Profit Maximizationlvl 4](/tech-tree/profit-maximization/)[Price Elasticitylvl 3](/tech-tree/price-elasticity/)[Consumer Surpluslvl 3](/tech-tree/consumer-surplus/)

## Referenced by (3)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (3)

[DemandBusiness

Direct mathematical formalization of demand as curves derived from utility maximization - Marshallian vs Hicksian forms, inverse demand, and market aggregation give the hidden force a tractable functional form for optimization](/business/demand/)[Marketing SpendBusiness

Marketing spend exists to shift the demand curve rightward. Understanding demand functions (how price and non-price factors determine quantity demanded) is the mathematical foundation for reasoning about what marketing dollars actually accomplish.](/business/marketing-spend/)[Demand-SideBusiness

Mathematical formalization of demand - deriving demand curves from utility maximization, aggregating market demand, and distinguishing Marshallian vs Hicksian demand gives the quantitative machinery to identify and measure poorly-served demand](/business/demand-side/)

Advanced Learning Details

### Graph Position

55

Depth Cost

8

Fan-Out (ROI)

3

Bottleneck Score

8

Chain Length

Demand functions are the bridge between tastes and market outcomes — they tell you how much people buy when prices and income change, and they underlie everything from pricing to welfare analysis.

TL;DR:

Demand functions map prices and income into optimal quantities; derived either from utility maximization (Marshallian) or expenditure minimization (Hicksian), they let you compute individual and market demand and the inverse demand (price as a function of quantity).

## What Is Demand Functions?

Definition and motivation

A demand function gives the quantity of a good that a consumer chooses as a function of prices and income (or utility). In more formal terms, a consumer with utility function u(x1,x2,…,xn)u(x\_1, x\_2, \dots, x\_n)u(x1​,x2​,…,xn​), facing prices p=(p1,…,pn)p = (p\_1,\dots,p\_n)p=(p1​,…,pn​) and income mmm, solves a constrained optimization problem and selects a bundle x∗(p,m)x^\*(p,m)x∗(p,m). The Marshallian (uncompensated) demand is

xM(p,m)=argmax⁡x≥0{u(x)  :  p⋅x≤m}.x^M(p,m) = \operatorname{argmax}\_{x\ge0} \{ u(x) \;:\; p\cdot x \le m \}.xM(p,m)=argmaxx≥0​{u(x):p⋅x≤m}.

Example: If u(x1,x2)=x112x212u(x\_1,x\_2)=x\_1^{\frac12}x\_2^{\frac12}u(x1​,x2​)=x121​​x221​​ (Cobb–Douglas), prices p1=2p\_1=2p1​=2, p2=1p\_2=1p2​=1, income m=100m=100m=100, then standard Cobb–Douglas algebra gives x1M=αm/p1x\_1^M=\alpha m/p\_1x1M​=αm/p1​ and x2M=(1−α)m/p2x\_2^M=(1-\alpha)m/p\_2x2M​=(1−α)m/p2​ where α=1/2\alpha=1/2α=1/2. Numerically, x1M=0.5⋅100/2=25x\_1^M=0.5\cdot100/2=25x1M​=0.5⋅100/2=25, x2M=0.5⋅100/1=50x\_2^M=0.5\cdot100/1=50x2M​=0.5⋅100/1=50.

Marshallian vs Hicksian: two ways to get demand

- •Marshallian (uncompensated) demand xM(p,m)x^M(p,m)xM(p,m) comes directly from utility maximization under a budget constraint. In "Utility Theory" we used Lagrangian methods to solve problems like this. Use Roy's identity (below) to obtain demands from indirect utility functions.

- •Hicksian (compensated) demand h(p,u)h(p,u)h(p,u) comes from expenditure minimization: given target utility level u0u\_0u0​, the consumer minimizes expenditure to reach that utility:

h(p,u0)=argmin⁡x≥0{p⋅x  :  u(x)≥u0}.h(p,u\_0)=\operatorname{argmin}\_{x\ge0}\{p\cdot x\;:\;u(x)\ge u\_0\}.h(p,u0​)=argminx≥0​{p⋅x:u(x)≥u0​}.

The Hicksian demand isolates substitution effects because income is adjusted to keep utility fixed; the Marshallian contains both substitution and income effects. A numeric illustration: with quasilinear utility u(x1,x2)=v(x1)+x2u(x\_1,x\_2)=v(x\_1)+x\_2u(x1​,x2​)=v(x1​)+x2​ and budget mmm, the Hicksian demand for x1x\_1x1​ at target utility u0u\_0u0​ solves minimizing p1x1+p2x2p\_1 x\_1 + p\_2 x\_2p1​x1​+p2​x2​ s.t. v(x1)+x2≥u0v(x\_1)+x\_2 \ge u\_0v(x1​)+x2​≥u0​. Eliminating x2x\_2x2​ gives the same first-order condition as the Marshallian when income shifts appropriately; we will show explicit numbers later.

Inverse demand and market demand

Inverse demand expresses price as a function of quantity. For a single-good quasilinear problem where utility is u(q)+yu(q)+yu(q)+y and yyy is money numeraire, the first-order condition is u′(q)=pu'(q)=pu′(q)=p so the inverse demand is

p(q)=u′(q).p(q)=u'(q).p(q)=u′(q).

Numeric example: if u(q)=10qu(q)=10\sqrt{q}u(q)=10q​ then u′(q)=5/qu'(q)=5/\sqrt{q}u′(q)=5/q​, so p(q)=5/qp(q)=5/\sqrt{q}p(q)=5/q​. At q=4q=4q=4, p(4)=5/2=2.5p(4)=5/2=2.5p(4)=5/2=2.5.

Market demand is the horizontal sum of individuals' Marshallian demands. If two consumers have demands x1M(p,m1)x^M\_1(p,m\_1)x1M​(p,m1​) and x2M(p,m2)x^M\_2(p,m\_2)x2M​(p,m2​), the market demand is X(p)=x1M(p,m1)+x2M(p,m2)X(p)=x^M\_1(p,m\_1)+x^M\_2(p,m\_2)X(p)=x1M​(p,m1​)+x2M​(p,m2​); for inverse market demand, invert that function where possible.

Why care? Practically every empirical demand estimation, welfare calculation, tax incidence, and monopoly pricing analysis starts from these demand functions. Understanding their derivation from utility ensures you interpret income and substitution effects correctly.

## Core Mechanic 1: Deriving Marshallian Demand (Utility Maximization and Roy's Identity)

Mechanic: Lagrangian optimization and Roy's identity

Start from the utility maximization problem. In "Utility Theory" we solved similar problems using the Lagrangian. For two goods, the Lagrangian is

L(x1,x2,λ)=u(x1,x2)−λ(p1x1+p2x2−m).\mathcal{L}(x\_1,x\_2,\lambda)=u(x\_1,x\_2)-\lambda(p\_1x\_1+p\_2x\_2-m).L(x1​,x2​,λ)=u(x1​,x2​)−λ(p1​x1​+p2​x2​−m).

First-order conditions (assuming interior solution):

ux1−λp1=0,ux2−λp2=0,p1x1+p2x2=m.u\_{x\_1}-\lambda p\_1=0,\qquad u\_{x\_2}-\lambda p\_2=0,\qquad p\_1x\_1+p\_2x\_2=m.ux1​​−λp1​=0,ux2​​−λp2​=0,p1​x1​+p2​x2​=m.

Solving yields Marshallian demand xM(p,m)x^M(p,m)xM(p,m). A shortcut: compute the indirect utility function v(p,m)=max⁡{u(x)  :  p⋅x≤m}v(p,m)=\max\{u(x)\;:\;p\cdot x\le m\}v(p,m)=max{u(x):p⋅x≤m} and use Roy's identity:

xiM(p,m)=−∂v(p,m)/∂pi∂v(p,m)/∂m.x^M\_i(p,m)=-\frac{\partial v(p,m)/\partial p\_i}{\partial v(p,m)/\partial m}.xiM​(p,m)=−∂v(p,m)/∂m∂v(p,m)/∂pi​​.

Numeric worked mini-example (Cobb–Douglas)

Let u(x1,x2)=x1αx21−αu(x\_1,x\_2)=x\_1^{\alpha}x\_2^{1-\alpha}u(x1​,x2​)=x1α​x21−α​ with α=1/2\alpha=1/2α=1/2, p1,p2p\_1,p\_2p1​,p2​ arbitrary, and income mmm. Solve via standard steps (or Roy's identity). The Marshallian demands are:

x1M(p,m)=αmp1,x2M(p,m)=(1−α)mp2.x\_1^M(p,m)=\frac{\alpha m}{p\_1},\qquad x\_2^M(p,m)=\frac{(1-\alpha)m}{p\_2}.x1M​(p,m)=p1​αm​,x2M​(p,m)=p2​(1−α)m​.

Numerical example: α=1/2\alpha=1/2α=1/2, p1=2p\_1=2p1​=2, p2=1p\_2=1p2​=1, m=100m=100m=100 gives x1M=25x\_1^M=25x1M​=25, x2M=50x\_2^M=50x2M​=50, as above.

An alternative: Quasilinear case

If utility is quasilinear in money, u(x,y)=v(x)+yu(x,y)=v(x)+yu(x,y)=v(x)+y where yyy is the numeraire and price of yyy is 1, the consumer maximizes v(x)+yv(x)+yv(x)+y s.t. pxx+y≤mp\_x x+y\le mpx​x+y≤m. Eliminating yyy gives maximize v(x)+m−pxxv(x)+m-p\_x xv(x)+m−px​x, so choose xxx to satisfy

v′(x)=px.v'(x)=p\_x.v′(x)=px​.

This directly yields inverse demand px(x)=v′(x)p\_x(x)=v'(x)px​(x)=v′(x). Numeric example: v(x)=10xv(x)=10\sqrt{x}v(x)=10x​, then v′(x)=5/xv'(x)=5/\sqrt{x}v′(x)=5/x​. If price is px=2.5p\_x=2.5px​=2.5, solve $5/\sqrt{x}=2.5so so so\sqrt{x}=2and and andx=4$.

Roy's identity numeric check

For Cobb–Douglas u=x11/2x21/2u=x\_1^{1/2}x\_2^{1/2}u=x11/2​x21/2​, the indirect utility is v(p,m)=(m2p1p2)v(p,m)=\left(\frac{m}{2\sqrt{p\_1p\_2}}\right)v(p,m)=(2p1​p2​​m​) up to a constant factor (work through substitution). Taking derivatives and applying Roy's identity yields the same x1M,x2Mx\_1^M, x\_2^Mx1M​,x2M​ above. A concrete verification: with p1=2,p2=1,m=100p\_1=2,p\_2=1,m=100p1​=2,p2​=1,m=100, compute v(2,1,100)v(2,1,100)v(2,1,100) numerically and then compute −∂v/∂p1 / (∂v/∂m)-\partial v/\partial p\_1\,/\,(\partial v/\partial m)−∂v/∂p1​/(∂v/∂m) to recover $25$.

## Core Mechanic 2: Hicksian Demand, Shephard's Lemma, and Decomposing Price Effects

Mechanic: expenditure minimization and compensated demand

The Hicksian demand isolates substitution effects by holding utility fixed. The consumer solves

e(p,u0)=min⁡x≥0p⋅xs.t.u(x)≥u0,e(p,u\_0)=\min\_{x\ge0} p\cdot x \quad\text{s.t.}\quad u(x)\ge u\_0,e(p,u0​)=x≥0min​p⋅xs.t.u(x)≥u0​,

and h(p,u0)h(p,u\_0)h(p,u0​) denotes the minimizer. The function e(p,u)e(p,u)e(p,u) is the expenditure function; Shephard's lemma states

∂e(p,u)∂pi=hi(p,u).\frac{\partial e(p,u)}{\partial p\_i}=h\_i(p,u).∂pi​∂e(p,u)​=hi​(p,u).

Numeric example (Cobb–Douglas)

For u(x1,x2)=x11/2x21/2u(x\_1,x\_2)=x\_1^{1/2}x\_2^{1/2}u(x1​,x2​)=x11/2​x21/2​ and target utility u0u\_0u0​, we can solve for h(p,u0)h(p,u\_0)h(p,u0​) analytically. The expenditure function is

e(p1,p2,u0)=2u0p1p2.e(p\_1,p\_2,u\_0)=2u\_0\sqrt{p\_1p\_2}.e(p1​,p2​,u0​)=2u0​p1​p2​​.

Check numerically: let p1=4p\_1=4p1​=4, p2=1p\_2=1p2​=1, and u0=10u\_0=10u0​=10. Then e=2⋅10⋅4⋅1=20⋅2=40e=2\cdot10\cdot\sqrt{4\cdot1}=20\cdot2=40e=2⋅10⋅4⋅1​=20⋅2=40. By Shephard's lemma,

h1(p,u0)=∂e∂p1=2u0⋅12p2p1=u0p2p1.h\_1(p,u\_0)=\frac{\partial e}{\partial p\_1}=2u\_0\cdot\frac{1}{2}\sqrt{\frac{p\_2}{p\_1}}=u\_0\sqrt{\frac{p\_2}{p\_1}}.h1​(p,u0​)=∂p1​∂e​=2u0​⋅21​p1​p2​​​=u0​p1​p2​​​.

Plug in numbers: h1=101/4=10⋅12=5h\_1=10\sqrt{1/4}=10\cdot\tfrac12=5h1​=101/4​=10⋅21​=5. Similarly h2=104/1=20h\_2=10\sqrt{4/1}=20h2​=104/1​=20. Check utility: $5^{1/2}\cdot20^{1/2}=\sqrt{100}=10=u\_0$ and expenditure $4\cdot5+1\cdot20=20+20=40$.

From Hicksian to Marshallian: income makes the difference

Marshallian demand can be obtained by plugging the indirect utility's u∗=v(p,m)u^\*=v(p,m)u∗=v(p,m) into Hicksian demand:

xM(p,m)=h(p,v(p,m)).x^M(p,m)=h\big(p, v(p,m)\big).xM(p,m)=h(p,v(p,m)).

This equation simply says: the Marshallian demand at (p,m)(p,m)(p,m) is the Hicksian demand that achieves the utility level the consumer actually attains at (p,m)(p,m)(p,m).

Slutsky equation (decompose price effects)

For any good iii and price pjp\_jpj​, the total derivative of Marshallian demand splits into substitution (compensated) and income effects:

∂xiM∂pj=∂hi∂pj−∂xiM∂mxjM.\frac{\partial x\_i^M}{\partial p\_j}=\frac{\partial h\_i}{\partial p\_j}-\frac{\partial x\_i^M}{\partial m}x\_j^M.∂pj​∂xiM​​=∂pj​∂hi​​−∂m∂xiM​​xjM​.

Numeric example: use Cobb–Douglas with α=1/2\alpha=1/2α=1/2, x1M=αm/p1x\_1^M=\alpha m/p\_1x1M​=αm/p1​. Compute derivatives: ∂x1M/∂p1=−αm/p12\partial x\_1^M/\partial p\_1=-\alpha m/p\_1^2∂x1M​/∂p1​=−αm/p12​. The income effect term is −(∂x1M/∂m)x1M=−(α/p1)(αm/p1)=−α2m/p12-(\partial x\_1^M/\partial m)x\_1^M = -(\alpha/p\_1)(\alpha m/p\_1)= -\alpha^2 m/p\_1^2−(∂x1M​/∂m)x1M​=−(α/p1​)(αm/p1​)=−α2m/p12​. So the compensated substitution effect equals

∂h1∂p1=∂x1M∂p1+∂x1M∂mx1M=−αm/p12+α2m/p12=−α(1−α)m/p12.\frac{\partial h\_1}{\partial p\_1}=\frac{\partial x\_1^M}{\partial p\_1}+\frac{\partial x\_1^M}{\partial m}x\_1^M = -\alpha m/p\_1^2 + \alpha^2 m/p\_1^2 = -\alpha(1-\alpha)m/p\_1^2.∂p1​∂h1​​=∂p1​∂x1M​​+∂m∂x1M​​x1M​=−αm/p12​+α2m/p12​=−α(1−α)m/p12​.

Plug numbers: α=1/2\alpha=1/2α=1/2, m=100m=100m=100, p1=2p\_1=2p1​=2 gives ∂x1M/∂p1=−0.5⋅100/4=−12.5\partial x\_1^M/\partial p\_1 = -0.5\cdot100/4 = -12.5∂x1M​/∂p1​=−0.5⋅100/4=−12.5, income derivative ∂x1M/∂m=0.5/2=0.25\partial x\_1^M/\partial m = 0.5/2 = 0.25∂x1M​/∂m=0.5/2=0.25, so income effect magnitude is $0.25\cdot25=6.25,andthuscompensatedeffectis, and thus compensated effect is ,andthuscompensatedeffectis-12.5+6.25=-6.25$. This shows the substitution effect is negative (as expected) and smaller in magnitude than the total effect when income effects go in the opposite direction.

Interpretation

- •Hicksian demand and Shephard's lemma let you compute how much expenditure must change when prices change to preserve utility, a building block for compensated price indices and welfare measures (compensating/equivalent variation).

- •The Slutsky decomposition is central to distinguishing consumer surplus changes into substitution vs income channels; numerical examples show how magnitudes arise from functional forms.

## Applications and Connections

Inverse demand and pricing

In many applied problems you know desired quantity and want to know the price that would induce it. For quasilinear utilities inverse demand is immediate: p(q)=v′(q)p(q)=v'(q)p(q)=v′(q). Example: v(q)=10qv(q)=10\sqrt{q}v(q)=10q​ implies p(q)=5/qp(q)=5/\sqrt{q}p(q)=5/q​. This form is widely used in monopoly pricing and public goods provision where marginal willingness to pay drives optimal provision rules.

Market aggregation

If there are NNN consumers with Marshallian demands xiM(p,mi)x^M\_{i}(p,m\_i)xiM​(p,mi​), market demand is

X(p)=∑i=1NxiM(p,mi).X(p)=\sum\_{i=1}^N x^M\_i(p,m\_i).X(p)=i=1∑N​xiM​(p,mi​).

Numeric illustration: two consumers with identical Cobb–Douglas demands xM=αm/px^M=\alpha m/pxM=αm/p but different incomes m1=100,m2=50m\_1=100,m\_2=50m1​=100,m2​=50, α=1/2\alpha=1/2α=1/2, p=2p=2p=2 gives x1M=25x^M\_1=25x1M​=25, x2M=12.5x^M\_2=12.5x2M​=12.5, and market demand X=37.5X=37.5X=37.5. Inverse market demand may not be analytically invertible but can be constructed numerically for aggregate analysis.

Empirical demand estimation and structural interpretation

Estimating demand curves often produces Marshallian demand (observational: prices and incomes vary). To interpret estimated elasticities correctly for welfare or tax incidence you must convert to Hicksian demand using Slutsky if you want substitution-only effects. For instance, consumer surplus approximations using Marshallian demand ignore income effects and can be biased for large price changes.

Welfare analysis: compensating and equivalent variation

Hicksian demand and the expenditure function allow exact welfare measures. Compensating variation (CV) holds prices at new prices and asks how much income change would restore original utility; mathematically CV solves

e(p′,u0)−m,e(p',u\_0)-m,e(p′,u0​)−m,

where u0u\_0u0​ is original utility and p′p'p′ new prices. Numerical computation uses Hicksian demands via Shephard's lemma.

Downstream topics that use these ideas

- •Tax incidence and optimal taxation: requires decomposition of price changes into income and substitution effects and uses Hicksian demands for deadweight loss.

- •Monopolistic pricing and Ramsey pricing: need inverse demand functions derived from consumers' marginal willingness to pay.

- •Empirical demand estimation and identification: linking reduced-form elasticities to underlying preferences uses Roy's identity and the Slutsky matrix.

- •General equilibrium welfare decomposition: aggregate Hicksian demands enter social welfare functions and compensating equivalence calculations.

Concrete example tying pieces together

Consider a small subsidy that lowers p1p\_1p1​ from 2 to 1.5 for the Cobb–Douglas consumer with α=1/2\alpha=1/2α=1/2, m=100m=100m=100. Marshallian demand jumps from x1M=25x\_1^M=25x1M​=25 to x1M=0.5⋅100/1.5≈33.33x\_1^M=0.5\cdot100/1.5\approx33.33x1M​=0.5⋅100/1.5≈33.33. Using Slutsky we can attribute how much of this increase is substitution vs income effect numerically (substitution effect ~6.25 in earlier calculation; income effect ~1.08 here), and compute compensating variation using the expenditure function to find the budget change that would offset the subsidy.

In summary, demand functions are the operational translation of preference and budget constraints into quantities and prices; mastering both Marshallian and Hicksian perspectives enables precise comparative statics, welfare measurement, and aggregation.

## Worked Examples (3)

### Cobb–Douglas Marshallian Demand

Let u(x1,x2)=x11/3x22/3u(x\_1,x\_2)=x\_1^{1/3}x\_2^{2/3}u(x1​,x2​)=x11/3​x22/3​. Prices: p1=3p\_1=3p1​=3, p2=2p\_2=2p2​=2. Income: m=90m=90m=90. Find Marshallian demands x1M,x2Mx\_1^M,x\_2^Mx1M​,x2M​.

1. Write general Cobb–Douglas result: for u=x1αx21−αu=x\_1^{\alpha}x\_2^{1-\alpha}u=x1α​x21−α​, x1M=αm/p1x\_1^M=\alpha m/p\_1x1M​=αm/p1​, x2M=(1−α)m/p2x\_2^M=(1-\alpha)m/p\_2x2M​=(1−α)m/p2​. Here α=1/3\alpha=1/3α=1/3.
2. Plug numbers into formula: x1M=(1/3)⋅90/3x\_1^M=(1/3)\cdot90/3x1M​=(1/3)⋅90/3.
3. Compute x1Mx\_1^Mx1M​: $90/3=30$, $30\cdot(1/3)=10.So. So .Sox\_1^M=10$.
4. Compute x2M=(2/3)⋅90/2x\_2^M=(2/3)\cdot90/2x2M​=(2/3)⋅90/2. First $90/2=45$, then $45\cdot(2/3)=30.So. So .Sox\_2^M=30$.
5. Check budget: $3\cdot10+2\cdot30=30+60=90=m$, consistent.

**Insight:** This example shows the quick route from functional form (Cobb–Douglas) to closed-form demands and verifies feasibility on the budget line.

### Hicksian Demand and Shephard's Lemma

Same utility u(x1,x2)=x11/2x21/2u(x\_1,x\_2)=x\_1^{1/2}x\_2^{1/2}u(x1​,x2​)=x11/2​x21/2​. Target utility u0=8u\_0=8u0​=8. Prices p1=4p\_1=4p1​=4, p2=1p\_2=1p2​=1. Find Hicksian demands h1,h2h\_1,h\_2h1​,h2​ and expenditure using Shephard's lemma.

1. Use the known expenditure function for this utility: e(p,u)=2up1p2e(p,u)=2u\sqrt{p\_1p\_2}e(p,u)=2up1​p2​​.
2. Plug numbers: e=2⋅8⋅4⋅1=16⋅2=32e=2\cdot8\cdot\sqrt{4\cdot1}=16\cdot2=32e=2⋅8⋅4⋅1​=16⋅2=32.
3. Apply Shephard's lemma: h1=∂e/∂p1=2u⋅12p2/p1=up2/p1h\_1=\partial e/\partial p\_1 = 2u\cdot\tfrac12\sqrt{p\_2/p\_1} = u\sqrt{p\_2/p\_1}h1​=∂e/∂p1​=2u⋅21​p2​/p1​​=up2​/p1​​.
4. Compute h1=81/4=8⋅12=4h\_1=8\sqrt{1/4}=8\cdot\tfrac12=4h1​=81/4​=8⋅21​=4.
5. Similarly h2=up1/p2=84/1=8⋅2=16h\_2= u\sqrt{p\_1/p\_2}=8\sqrt{4/1}=8\cdot2=16h2​=up1​/p2​​=84/1​=8⋅2=16. Check utility: 4⋅16=2⋅4=8\sqrt{4}\cdot\sqrt{16}=2\cdot4=84​⋅16​=2⋅4=8 and expenditure $4\cdot4+1\cdot16=16+16=32,matching, matching ,matchinge$.

**Insight:** Shephard's lemma directly gives compensated demand from the expenditure function; numerical checks confirm the preservation of the target utility and cost minimality.

### Inverse Demand from Quasilinear Utility

Utility u(q,y)=10q+yu(q,y)=10\sqrt{q}+yu(q,y)=10q​+y with yyy numeraire. Find inverse demand p(q)p(q)p(q) and evaluate price at q=9q=9q=9.

1. In the quasilinear case, FOC for maximizing $10\sqrt{q}+ysubjectto subject to subjecttopq+y\le m$ reduces to $10\cdot(1/2)q^{-1/2}=pbecause because becausey$ is chosen to exhaust budget.
2. Compute derivative: v′(q)=5q−1/2v'(q)=5 q^{-1/2}v′(q)=5q−1/2, so inverse demand is p(q)=5/qp(q)=5/\sqrt{q}p(q)=5/q​.
3. Plug q=9q=9q=9: p(9)=5/9=5/3≈1.6667p(9)=5/\sqrt{9}=5/3\approx1.6667p(9)=5/9​=5/3≈1.6667.
4. Interpretation: if price is $1.6667,theconsumerisindifferentatchoosing, the consumer is indifferent at choosing ,theconsumerisindifferentatchoosingq=9givenquasilinearpreferences(incomeaffectsonly given quasilinear preferences (income affects only givenquasilinearpreferences(incomeaffectsonlyy$).
5. If a market had two identical consumers, aggregate demand at price ppp would be $2\cdot q(p)=2\cdot(5/p)^2(inverttoget (invert to get (inverttogetq(p)=(5/p)^2).At). At ).Atp=1.6667$, each buys 9 so aggregate is 18.

**Insight:** Quasilinear preferences make inverse demand especially transparent: marginal utility equals price; aggregation is a simple horizontal sum since income effects on the good vanish.

## Key Takeaways

- ✓

  Marshallian demand xM(p,m)x^M(p,m)xM(p,m) comes from utility maximization under a budget; Hicksian demand h(p,u)h(p,u)h(p,u) comes from expenditure minimization holding utility fixed.
- ✓

  Roy's identity recovers Marshallian demand from the indirect utility function: xiM=−vpi/vmx^M\_i=-v\_{p\_i}/v\_mxiM​=−vpi​​/vm​; Shephard's lemma recovers Hicksian demand from the expenditure function: hi=epih\_i=e\_{p\_i}hi​=epi​​.
- ✓

  Inverse demand in quasilinear settings is p(q)=v′(q)p(q)=v'(q)p(q)=v′(q); numerically this gives marginal willingness to pay as a function of quantity.
- ✓

  Market demand is the horizontal sum of individual Marshallian demands; aggregation can change curvature and invertibility properties.
- ✓

  Slutsky decomposition splits total price effects into compensated substitution effects and income effects, crucial for welfare and tax incidence analysis.
- ✓

  Every formula should be checked with a numerical example to ensure algebraic manipulations and corner conditions are handled correctly.

## Common Mistakes

- ✗

  Confusing Marshallian and Hicksian demand: Marshallian varies with income mmm, Hicksian varies with target utility uuu. Using one in place of the other produces wrong substitution/income attributions.
- ✗

  Applying Roy's identity or Shephard's lemma without verifying differentiability or interior solutions: corner solutions invalidate straightforward FOC-based formulas.
- ✗

  Summing inverse demands horizontally: market inverse demand is not the sum of individual inverse demands; inverse demand is the inverse of the horizontal sum of quantities, not the sum of price functions.

## Practice

easy

Easy: For utility u(x1,x2)=x10.6x20.4u(x\_1,x\_2)=x\_1^{0.6}x\_2^{0.4}u(x1​,x2​)=x10.6​x20.4​, prices p1=5p\_1=5p1​=5, p2=2p\_2=2p2​=2, income m=200m=200m=200, compute Marshallian demands x1M,x2Mx\_1^M,x\_2^Mx1M​,x2M​.

**Hint:** Use the Cobb–Douglas formula x1M=αm/p1x\_1^M=\alpha m/p\_1x1M​=αm/p1​ with α=0.6\alpha=0.6α=0.6.

Show solution

Compute x1M=0.6⋅200/5=120/5=24x\_1^M=0.6\cdot200/5=120/5=24x1M​=0.6⋅200/5=120/5=24. Compute x2M=0.4⋅200/2=80/2=40x\_2^M=0.4\cdot200/2=80/2=40x2M​=0.4⋅200/2=80/2=40. Check budget: $5\cdot24+2\cdot40=120+80=200$.

medium

Medium: Given quasilinear utility u(q,y)=8q+yu(q,y)=8\sqrt{q}+yu(q,y)=8q​+y, find the Marshallian demand for qqq as a function of price ppp and income mmm. Then compute the demand at p=2p=2p=2 and m=50m=50m=50.

**Hint:** FOC: set marginal utility $8\cdot(1/2)q^{-1/2}=p$ where interior; check corner cases with budget if needed.

Show solution

FOC gives $4 q^{-1/2}=p,so, so ,soq=(4/p)^2.For. For .Forp=2$, $q=(4/2)^2=2^2=4.Becauseutilityisquasilinear,income. Because utility is quasilinear, income .Becauseutilityisquasilinear,incomemaffectsonly affects only affectsonlyy,not, not ,notq,so, so ,soq=4irrespectiveof irrespective of irrespectiveofm(provided (provided (providedmcanpayforthatquantity,i.e., can pay for that quantity, i.e., canpayforthatquantity,i.e.,pq\le m$). Check budget: $2\cdot4=8\le50$, so feasible.

hard

Hard: A consumer has utility u(x1,x2)=ln⁡x1+x2u(x\_1,x\_2)=\ln x\_1 + x\_2u(x1​,x2​)=lnx1​+x2​ (quasilinear). Prices p1=pp\_1=pp1​=p, p2=1p\_2=1p2​=1, income mmm. (a) Find Marshallian demand x1M(p,m)x\_1^M(p,m)x1M​(p,m). (b) Find Hicksian demand h1(p,u)h\_1(p,u)h1​(p,u) and show the Slutsky identity numerically for p=4p=4p=4, m=20m=20m=20 (compute both sides of the Slutsky decomposition for a small price change).

**Hint:** For (a) quasilinear: set derivative $1/x\_1 = ptogetinteriorsolution;becarefulaboutcornercasewhen to get interior solution; be careful about corner case when togetinteriorsolution;becarefulaboutcornercasewhenp>1/m?For(b)find? For (b) find ?For(b)findh\_1$ by minimizing expenditure subject to utility target using algebra; then compute derivatives numerically for small dp.

Show solution

(a) Utility is ln⁡x1+x2\ln x\_1+x\_2lnx1​+x2​ and budget px1+x2≤mpx\_1+x\_2\le mpx1​+x2​≤m. Eliminating x2x\_2x2​ gives maximize ln⁡x1+m−px1\ln x\_1 + m - p x\_1lnx1​+m−px1​. FOC: $1/x\_1 - p =0so so sox\_1^M=1/p,providedbudgetallows, provided budget allows ,providedbudgetallowsp(1/p)=1\le m,i.e., i.e. ,i.e.m\ge1.If. If .Ifm<1thenthecornersolutionistospendallincomeon then the corner solution is to spend all income on thenthecornersolutionistospendallincomeonx\_2giving giving givingx\_1^M=0$.

(b) Hicksian: minimize px1+x2p x\_1 + x\_2px1​+x2​ s.t. ln⁡x1+x2≥u\ln x\_1 + x\_2 \ge ulnx1​+x2​≥u. Substitute x2=u−ln⁡x1x\_2 = u - \ln x\_1x2​=u−lnx1​ into objective to get px1+u−ln⁡x1p x\_1 + u - \ln x\_1px1​+u−lnx1​. First-order condition: p−1/x1=0p - 1/x\_1 = 0p−1/x1​=0 so x1h=1/px\_1^h=1/px1h​=1/p independent of uuu (again quasilinear). Thus h1(p,u)=1/ph\_1(p,u)=1/ph1​(p,u)=1/p.

Slutsky: For a small change dpdpdp, compute total derivative of Marshallian demand: dx1M/dp=−1/p2dx\_1^M/dp = -1/p^2dx1M​/dp=−1/p2. The compensated derivative ∂h1/∂p=−1/p2\partial h\_1/\partial p = -1/p^2∂h1​/∂p=−1/p2. The income effect term is (∂x1M/∂m)x1M(\partial x\_1^M/\partial m) x\_1^M(∂x1M​/∂m)x1M​. But ∂x1M/∂m=0\partial x\_1^M/\partial m = 0∂x1M​/∂m=0 for interior solutions (quasilinear), so Slutsky identity reads −1/p2=−1/p2−0-1/p^2 = -1/p^2 - 0−1/p2=−1/p2−0, which holds.

Numeric check at p=4,m=20p=4,m=20p=4,m=20: x1M=1/4=0.25x\_1^M=1/4=0.25x1M​=1/4=0.25. dx1M/dp=−1/16=−0.0625dx\_1^M/dp = -1/16=-0.0625dx1M​/dp=−1/16=−0.0625. Compensated derivative ∂h1/∂p=−1/16\partial h\_1/\partial p=-1/16∂h1​/∂p=−1/16. Income effect term ∂x1M/∂m=0\partial x\_1^M/\partial m =0∂x1M​/∂m=0, so decomposition holds numerically.

## Connections

Looking back: In "Utility Theory" we learned to set up Lagrangians and interpret marginal utilities (the FOCs equalize marginal rate of substitution and price ratios). Those techniques give Marshallian demand directly; Roy's identity formalizes converting indirect utility to demand. In "Derivatives" we used slopes and instantaneous rates of change; here we use derivatives of indirect utility, expenditure functions, and demand functions (e.g. ∂x/∂p\partial x/\partial p∂x/∂p) to get elasticities and Slutsky decomposition. Looking forward: mastering demand functions enables rigorous analysis in tax incidence, welfare measurement (compensating/equivalent variation), monopoly pricing (using inverse demand), and empirical structural demand estimation (recovering preferences from observed choices). Specific downstream concepts that require these tools include Slutsky symmetry and negativity proofs (advanced micro), general equilibrium welfare theorems where Hicksian demands show up in compensated demand aggregates, and industrial organization models that use inverse demand for profit maximization and for calibrating willingness-to-pay in empirical IO.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
