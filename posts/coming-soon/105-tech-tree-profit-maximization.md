---
title: Profit Maximization
description: MR=MC first-order conditions. Monopoly pricing, constrained profit optimization with capacity or regulatory constraints. Second-order sufficiency.
date: '2026-07-01'
scheduled: '2026-10-13'
tags:
- p-and-l-engineering
- coming-soon
- tech-tree
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/tech-tree/profit-maximization/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/profit-maximization/](https://templeton.host/tech-tree/profit-maximization/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Profit Maximization

Applied EconomicsDifficulty: ★★★★☆Depth: 9Unlocks: 5

MR=MC first-order conditions. Monopoly pricing, constrained profit optimization with capacity or regulatory constraints. Second-order sufficiency.

## Prerequisites (3)

[Demand Functions? atoms](/tech-tree/demand-functions/)[Cost Functions? atoms](/tech-tree/cost-functions/)[Lagrange Multipliers5 atoms](/tech-tree/lagrange-multipliers/)

## Unlocks (3)

[Price Discriminationlvl 4](/tech-tree/price-discrimination/)[Oligopoly Modelslvl 4](/tech-tree/oligopoly-models/)[Dynamic Pricinglvl 5](/tech-tree/dynamic-pricing/)

## Referenced by (14)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (14)

[P&L ownershipBusiness

MR=MC first-order conditions, constrained optimization with capacity or regulatory constraints, and second-order sufficiency are the formal mathematical framework for the decisions a P&L owner makes daily - pricing, volume, cost structure tradeoffs across brands.](/business/p-l-ownership/)[PricingBusiness

MR=MC first-order conditions are THE mathematical framework for finding optimal price; constrained profit optimization with capacity or regulatory constraints maps directly to real pricing problems](/business/pricing/)[CFOBusiness

MR=MC first-order conditions and constrained profit optimization formalize the CFO's core decision problem: maximize returns subject to capital, capacity, and regulatory constraints.](/business/cfo/)[private equityBusiness

PE operational value creation maps directly to constrained profit optimization - MR=MC under capacity, regulatory, and capital structure constraints. A PE CTO's mandate (cost reduction via AI, margin expansion, operational efficiency) is applied profit maximization with second-order sufficiency checks.](/business/private-equity/)[Revenue LineBusiness

MR=MC first-order conditions are the mathematical foundation for optimizing a revenue line - the point where an additional unit of cost-center spend no longer generates incremental revenue, which is exactly how you decide resource allocation across revenue lines.](/business/revenue-line/)[PE-BackedBusiness

PE value creation is constrained profit maximization - MR=MC first-order conditions under capacity and covenant constraints, with a fixed exit horizon imposing time-bounded optimization that maps directly to the math of how PE operating partners drive portfolio company performance](/business/pe-backed/)[EBITDABusiness

EBITDA optimization is literally constrained profit maximization at the operating level - MR=MC conditions, capacity constraints, and second-order sufficiency formalize cost program decisions and exit timing.](/business/ebitda/)[turnaroundsBusiness

P&L ownership is literally constrained profit maximization - MR=MC first-order conditions, capacity constraints, and second-order sufficiency checks are the mathematical foundation of deciding where a turnaround can extract margin](/business/turnarounds/)[PE Portfolio OperationsBusiness

PE portfolio ops is constrained profit maximization - MR=MC conditions, capacity constraints, and regulatory constraints are the direct mathematical formulation of operational improvement decisions](/business/pe-portfolio-operations/)[Operating ValueBusiness

MR=MC first-order conditions are the mathematical framework for locating where operations create maximum value, including constrained optimization with capacity or regulatory constraints](/business/operating-value/)[EBITDA OptimizationBusiness

EBITDA optimization is constrained profit maximization - MR=MC conditions, capacity constraints, and second-order sufficiency checks all apply directly to sizing and sequencing cost programs](/business/ebitda-optimization/)[Multi-Brand PortfolioBusiness

P&L ownership at each brand requires independent MR=MC reasoning - the multi-brand operator runs N parallel profit maximization problems](/business/multi-brand-portfolio/)[Exit SequencingBusiness

EBITDA optimization is constrained profit maximization - MR=MC conditions applied to each cost program, with organizational capacity and time-to-exit as binding constraints. Second-order conditions matter when programs interact.](/business/exit-sequencing/)[OperatorBusiness

MR=MC under capacity and regulatory constraints is the mathematical formalization of what operators do daily - maximize profit subject to real-world constraints across business units.](/business/operator/)

Advanced Learning Details

### Graph Position

60

Depth Cost

5

Fan-Out (ROI)

3

Bottleneck Score

9

Chain Length

Profit-maximization rules how firms set output and price; small mistakes in applying MR=MC or mis-handling constraints change predicted price, welfare, and regulatory answers dramatically.

TL;DR:

Profit maximization uses the first-order condition MR=MC (with second-order checks) and Kuhn–Tucker/KKT logic for constraints to determine monopoly output, price, shadow values of capacity/regulation, and welfare implications.

## What Is Profit Maximization?

Profit maximization is the decision rule a firm uses to choose output and price to maximize profit (π). For a single-product firm facing a downward-sloping inverse demand function p(q)p(q)p(q) and producing at cost C(q)C(q)C(q), profit is

π(q)=R(q)−C(q)=p(q)q−C(q).\pi(q)=R(q)-C(q)=p(q)q-C(q).π(q)=R(q)−C(q)=p(q)q−C(q).

The core first-order condition (FOC) equates marginal revenue (MR) to marginal cost (MC):

FOC: MR(q)=MC(q),where MR(q)=dRdq=p(q)+p′(q)q.\text{FOC: }MR(q)=MC(q),\quad\text{where }MR(q)=\frac{dR}{dq}=p(q)+p'(q)q.FOC: MR(q)=MC(q),where MR(q)=dqdR​=p(q)+p′(q)q.

Concrete numeric example: If p(q)=100−2qp(q)=100-2qp(q)=100−2q and C(q)=20qC(q)=20qC(q)=20q so MC(q)=20MC(q)=20MC(q)=20, then

MR(q)=100−4q.MR(q)=100-4q.MR(q)=100−4q.

Setting MR=MCMR=MCMR=MC gives $100-4q=20\Rightarrow q^*=20$, and price $p^*=100-2\cdot20=60.Profitis. Profit is .Profitis\pi=(60-20)\cdot20=800$.

Why MR=MC? In marginal terms, producing one extra unit yields additional revenue MRMRMR and additional cost MCMCMC. Profit increases when MR>MCMR>MCMR>MC and decreases when MR<MCMR<MCMR<MC; at an interior optimum these are equal. This builds directly on the prerequisites: in Demand Functions we learned how p(q)p(q)p(q) arises from consumer behavior and how elasticity matters; in Cost Functions we learned fixed/variable separation and how MCMCMC behaves; and in Lagrange Multipliers we learned how to impose equality constraints.

Several important caveats and refinements:

- •MR differs from price whenever the firm faces a non-flat demand curve: MR=p+qp′(q)MR=p+q p'(q)MR=p+qp′(q). For a linear demand p=qp=qp=q slope negative, MR has twice the slope. Concrete numeric: with p(q)=100−2qp(q)=100-2qp(q)=100−2q, p′(q)=−2p'(q)=-2p′(q)=−2, so MR=100−4qMR=100-4qMR=100−4q (twice the slope).

- •The FOC is necessary but not sufficient. We must check the second-order condition (SOC) for a local maximum:

π′′(q)=R′′(q)−C′′(q)=MR′(q)−MC′(q)<0.\pi''(q)=R''(q)-C''(q)=MR'(q)-MC'(q)<0.π′′(q)=R′′(q)−C′′(q)=MR′(q)−MC′(q)<0.

Numeric check: for p=100−2qp=100-2qp=100−2q, MR′(q)=−4MR'(q)=-4MR′(q)=−4; if C(q)=20qC(q)=20qC(q)=20q then MC′(q)=0MC'(q)=0MC′(q)=0, so π′′(q)=−4<0\pi''(q)=-4<0π′′(q)=−4<0, confirming a maximum at q∗=20q^\*=20q∗=20.

- •There are corner solutions. If the unconstrained FOC yields an infeasible quantity (e.g., negative qqq or exceeding capacity), the optimum may be at a boundary. Handling these requires the Kuhn–Tucker conditions (inequality constraints) introduced in the Lagrange Multipliers prerequisite. We will treat those in Section 3.

- •Elasticity matters. The markup over marginal cost depends inversely on the price elasticity of demand ε\varepsilonε (defined below), so more elastic demand forces lower markups and prices, all else equal.

Finally, profit maximization underpins much of industrial organization, regulatory economics, and public policy: price-setting, capacity investment, and welfare analysis are all derived from MR=MC logic (plus constraints and welfare weights). The rest of this lesson turns that logic into operational tools, demonstrates constrained optimization with binding capacity or regulatory caps, and shows how to verify second-order sufficiency.

## Core Mechanic 1: MR=MC, Markups, and Second-Order Conditions

Derivation of MR and the standard rule. Start with revenue R(q)=p(q)qR(q)=p(q)qR(q)=p(q)q. Differentiate:

MR(q)=ddq[p(q)q]=p(q)+p′(q)q.MR(q)=\frac{d}{dq}[p(q)q]=p(q)+p'(q)q.MR(q)=dqd​[p(q)q]=p(q)+p′(q)q.

Concrete numeric example: with p(q)=200−5qp(q)=200-5qp(q)=200−5q, p′(q)=−5p'(q)=-5p′(q)=−5, so

MR(q)=200−10q.MR(q)=200-10q.MR(q)=200−10q.

Set MR=MCMR=MCMR=MC to solve for interior solutions. If MCMCMC is constant at 40, then $200-10q=40\Rightarrow q^*=16$, $p^*=200-5\cdot16=120$.

Elasticity and the Lerner index. Use the price elasticity of demand ε(p)=dqdppq\varepsilon(p)=\frac{dq}{dp}\frac{p}{q}ε(p)=dpdq​qp​ (note ε<0\varepsilon<0ε<0 if demand slopes down). Transform MR using elasticity. Start from MR=p+qp′(q)MR=p+q p'(q)MR=p+qp′(q) and recall p′(q)=1/(dq/dp)p'(q)=1/(dq/dp)p′(q)=1/(dq/dp); algebra yields the compact form:

MR(p)=p(1+1ε(p)).MR(p)=p\Big(1+\frac{1}{\varepsilon(p)}\Big).MR(p)=p(1+ε(p)1​).

Concrete numeric example: Suppose at the candidate price p=120p=120p=120 the elasticity is ε=−4\varepsilon=-4ε=−4. Then MR=120(1+1/(−4))=120(1−0.25)=90MR=120(1+1/(-4))=120(1-0.25)=90MR=120(1+1/(−4))=120(1−0.25)=90. If MC=90MC=90MC=90 at that output, MR=MC holds.

From MR=MCMR=MCMR=MC we obtain the Lerner index, which expresses the monopoly markup relative to price:

p−MCp=−1ε.\frac{p-MC}{p}=-\frac{1}{\varepsilon}.pp−MC​=−ε1​.

Numeric example: If elasticity ε=−5\varepsilon=-5ε=−5 and MC=10MC=10MC=10, then

p−10p=15⇒p=101−1/5=104/5=12.5.\frac{p-10}{p}=\frac{1}{5}\Rightarrow p=\frac{10}{1-1/5}=\frac{10}{4/5}=12.5.pp−10​=51​⇒p=1−1/510​=4/510​=12.5.

Interpretation: a less elastic demand (|ε| small) permits a larger markup; extremely elastic demand drives the markup down.

Second-order conditions. For a local maximum we require

π′′(q)=ddq(MR−MC)=MR′(q)−MC′(q)<0.\pi''(q)=\frac{d}{dq}(MR-MC)=MR'(q)-MC'(q)<0.π′′(q)=dqd​(MR−MC)=MR′(q)−MC′(q)<0.

Since MR′(q)=p′(q)+p′(q)+p′′(q)q=2p′(q)+p′′(q)qMR'(q)=p'(q)+p'(q)+p''(q)q=2p'(q)+p''(q)qMR′(q)=p′(q)+p′(q)+p′′(q)q=2p′(q)+p′′(q)q, for many standard demand specifications (linear, isoelastic) MR′MR'MR′ is negative. If MC′MC'MC′ is nonnegative (convex costs), the SOC usually holds.

Concrete SOC checks:

- •Linear demand: p(q)=a−bq⇒MR(q)=a−2bqp(q)=a-bq\Rightarrow MR(q)=a-2bqp(q)=a−bq⇒MR(q)=a−2bq, so MR′=−2bMR'=-2bMR′=−2b. If b>0b>0b>0 and MC′(q)≥0MC'(q)\ge0MC′(q)≥0, then π′′=−2b−MC′(q)<0\pi''=-2b-MC'(q)<0π′′=−2b−MC′(q)<0. Example: a=100,b=2a=100,b=2a=100,b=2, MC′(q)=0MC'(q)=0MC′(q)=0 gives π′′=−4<0\pi''=-4<0π′′=−4<0.

- •Quadratic cost: C(q)=cq+d2q2⇒MC=c+dqC(q)=cq+\frac{d}{2}q^2\Rightarrow MC=c+dqC(q)=cq+2d​q2⇒MC=c+dq, so MC′=dMC'=dMC′=d. For d>0d>0d>0 the SOC becomes more strongly negative.

Edge cases and non-standard shapes. If demand is such that MR′(q)≥MC′(q)MR'(q)\ge MC'(q)MR′(q)≥MC′(q) (e.g., increasing marginal revenue, which requires bizarre shapes), the FOC might be a minimum or inflection. Check the bordered Hessian for constrained problems (next section) or verify global concavity of π(q)\pi(q)π(q).

Summary of actionable steps when solving standard monopoly problems:

1. 1)Compute MR(q)=p(q)+p′(q)qMR(q)=p(q)+p'(q)qMR(q)=p(q)+p′(q)q. Include a numeric evaluation at trial qqq.
2. 2)Compute MC(q)MC(q)MC(q) from C(q)C(q)C(q) and evaluate.
3. 3)Solve MR=MCMR=MCMR=MC for q∗q^\*q∗, then compute p∗=p(q∗)p^\*=p(q^\*)p∗=p(q∗) and π∗=p∗q∗−C(q∗)\pi^\*=p^\*q^\*-C(q^\*)π∗=p∗q∗−C(q∗).
4. 4)Verify SOC: compute π′′(q∗)\pi''(q^\*)π′′(q∗) numerically; if negative, you have a local maximum. If positive or zero, reconsider corner solutions.

Concrete worked micro-example: Let p(q)=100−2qp(q)=100-2qp(q)=100−2q and C(q)=10q+0.5q2C(q)=10q+0.5q^2C(q)=10q+0.5q2. Then MR=100−4qMR=100-4qMR=100−4q, MC=10+qMC=10+qMC=10+q. Solve $100-4q=10+q\Rightarrow 90=5q\Rightarrow q^*=18$. Price $p^*=100-36=64.Profit. Profit .Profit\pi=64\cdot18-(180+0.5\cdot324)=1152-342=810.CheckSOC:. Check SOC: .CheckSOC:MR'=-4$, $MC'=1,so, so ,so\pi''=-5<0$ confirming a maximum.

These procedures and checks are immediate applications of the Demand Functions and Cost Functions prerequisites, and they make the MR=MC rule operational and robust to pathological cases.

## Core Mechanic 2: Constrained Profit Optimization (Capacity and Regulation)

Real firms often face constraints: a capacity limit, regulatory price caps, or quantity mandates. These create inequality constraints that change both the chosen output and the valuation of relaxing constraints (shadow prices). The correct mathematical framework is Kuhn–Tucker (KKT) conditions: extend Lagrangians for inequality constraints and interpret multipliers.

Capacity constraint: consider q≤Kq\le Kq≤K where KKK is a fixed capacity. The firm's problem is

max⁡q≥0  π(q)=p(q)q−C(q)s.t. q≤K.\max\_{q\ge0}\;\pi(q)=p(q)q-C(q)\quad\text{s.t. } q\le K.q≥0max​π(q)=p(q)q−C(q)s.t. q≤K.

Set up the Lagrangian with multiplier λ≥0\lambda\ge0λ≥0:

L(q,λ)=p(q)q−C(q)+λ(K−q).\mathcal{L}(q,\lambda)=p(q)q-C(q)+\lambda(K-q).L(q,λ)=p(q)q−C(q)+λ(K−q).

KKT conditions:

1. 1)Stationarity: ∂L∂q=MR(q)−MC(q)−λ=0\frac{\partial \mathcal{L}}{\partial q}=MR(q)-MC(q)-\lambda=0∂q∂L​=MR(q)−MC(q)−λ=0.
2. 2)Complementary slackness: λ(K−q)=0\lambda(K-q)=0λ(K−q)=0.
3. 3)Primal feasibility: q≤Kq\le Kq≤K, q≥0q\ge0q≥0.
4. 4)Dual feasibility: λ≥0\lambda\ge0λ≥0.

Interpretation: if constraint non-binding (q<Kq<Kq<K), then λ=0\lambda=0λ=0 and the usual MR=MCMR=MCMR=MC holds. If binding (q=Kq=Kq=K), then λ=MR(K)−MC(K)≥0\lambda=MR(K)-MC(K)\ge0λ=MR(K)−MC(K)≥0 — the shadow value equals the amount MR exceeds MC at the constrained quantity. Intuitively, the marginal value of relaxing capacity by one unit equals the extra profit that that unit would generate (MR-MC) at the current binding level.

Concrete numeric example: with p(q)=100−2qp(q)=100-2qp(q)=100−2q and C(q)=20qC(q)=20qC(q)=20q (so MC=20MC=20MC=20), we found unconstrained q∗=20q^\*=20q∗=20. Suppose capacity K=15K=15K=15 binds. Then the firm sets q=15q=15q=15. Price is p(15)=100−30=70p(15)=100-30=70p(15)=100−30=70, profit is (70−20)⋅15=750(70-20)\cdot15=750(70−20)⋅15=750. The multiplier is \(\lambda=MR(15)-MC(15)\). Calculate: MR(15)=100−4⋅15=40MR(15)=100-4\cdot15=40MR(15)=100−4⋅15=40, so λ=40−20=20\lambda=40-20=20λ=40−20=20. That means increasing capacity by one unit increases profit by 20.

Regulatory price cap: suppose regulator imposes p≤pˉp\le \bar pp≤pˉ​. Under a price cap the firm faces a maximum feasible price; demand that is consistent with that price is qd(pˉ)q\_d(\bar p)qd​(pˉ​) from the inverse demand. If pˉ\bar ppˉ​ is above the unconstrained profit-maximizing price p∗p^\*p∗, the cap is non-binding. If pˉ<p∗\bar p<p^\*pˉ​<p∗, then the firm cannot charge p∗p^\*p∗; instead, if the cap is binding and quantity is unconstrained (firm can supply any demanded q at pˉ\bar ppˉ​), the firm behaves as a price-taker at pˉ\bar ppˉ​ and supplies the demanded q(pˉ)q(\bar p)q(pˉ​) such that p(q(pˉ))=pˉp(q(\bar p))=\bar pp(q(pˉ​))=pˉ​. Its profit is π=(pˉ−MC(q))q(pˉ)\pi=(\bar p - MC(q))q(\bar p)π=(pˉ​−MC(q))q(pˉ​).

Concrete numeric example: with p(q)=100−2qp(q)=100-2qp(q)=100−2q, MC=20MC=20MC=20, unconstrained p∗=60p^\*=60p∗=60. If the regulator sets pˉ=50<p∗\bar p=50<p^\*pˉ​=50<p∗, demand is q(50)=(100−50)/2=25q(50)=(100-50)/2=25q(50)=(100−50)/2=25. Profit then is (50−20)⋅25=750(50-20)\cdot25=750(50−20)⋅25=750. Notice this is the same numerical profit as the capacity example above — different constraints can produce identical outcomes.

More generally, when both capacity and price cap exist (or other constraints), form a Lagrangian with multipliers for each active inequality and write KKT conditions. The multipliers are interpretable: marginal welfare of relaxing the corresponding constraint or the marginal transfer value embedded in regulation.

Second-order sufficiency with constraints. For inequality-constrained problems, a sufficient condition for a local maximum is concavity of the objective function π(q)\pi(q)π(q) (or, for multi-dimensional problems, that the Hessian of π\piπ is negative-definite on the tangent cone of active constraints). Practically, if π(q)\pi(q)π(q) is concave (e.g., RRR concave and CCC convex), any point satisfying KKT is a global maximum. Check numerically by verifying π′′(q)≤0\pi''(q)\le0π′′(q)≤0 for single-dimension problems.

Worked symbolic relation for shadow price under binding capacity: If capacity binds at q=Kq=Kq=K, then

λ=MR(K)−MC(K).\lambda=MR(K)-MC(K).λ=MR(K)−MC(K).

Concrete numeric: earlier, with K=15K=15K=15, λ=40−20=20\lambda=40-20=20λ=40−20=20, so marginal value of capacity is 20.

Edge cases worth noting:

- •If the capacity is very tight so q=Kq=Kq=K but MR(K)<MC(K)MR(K)<MC(K)MR(K)<MC(K), then λ\lambdaλ would be negative which violates dual feasibility. That case would mean the capacity constraint cannot be binding at an optimum — rather, the true optimum would be interior or another constraint.

- •If regulatory caps are expressed in quantities or revenues rather than prices, the Lagrangian must incorporate those transformed constraints; always map constraints through the inverse demand or direct demand to the chosen decision variable.

This constrained optimization machinery is directly built on Lagrange Multipliers (the prerequisite). It produces not only optimal choices (output, price) but also shadow prices that tell regulators how binding constraints affect firms' incentives and how much welfare could be gained from marginally relaxing a constraint.

## Applications and Connections

Profit maximization and MR=MC are used in many applied settings. Below are several concrete applications, each with short analytical descriptions and numerical notes that show how the MR=MC logic is applied and extended.

1) Welfare and deadweight loss. Monopoly pricing generates deadweight loss relative to competitive pricing (p=MCp=MCp=MC). Compute consumer and producer surplus changes using numeric examples. For p(q)=100−2qp(q)=100-2qp(q)=100−2q and MC=20MC=20MC=20, monopoly sets q∗=20q^\*=20q∗=20, p∗=60p^\*=60p∗=60. Competitive output solves p=MC⇒100−2qc=20⇒qc=40p=MC\Rightarrow100-2q^{c}=20\Rightarrow q^{c}=40p=MC⇒100−2qc=20⇒qc=40, so competitive price pc=20p^{c}=20pc=20. Deadweight loss is the triangular area between demand and marginal cost from q∗=20q^\*=20q∗=20 to qc=40q^{c}=40qc=40,

DWL=12(p∗−MC)(qc−q∗)=12(60−20)(40−20)=12⋅40⋅20=400.DWL=\frac{1}{2}(p^\*-MC)(q^c-q^\*)=\frac{1}{2}(60-20)(40-20)=\frac{1}{2}\cdot40\cdot20=400.DWL=21​(p∗−MC)(qc−q∗)=21​(60−20)(40−20)=21​⋅40⋅20=400.

Concrete interpretation: the firm’s markup produces a welfare loss of 400 in the same monetary units used for prices and quantities.

2) Ramsey pricing (regulatory second-best). When a regulator must allow a firm to cover fixed costs but wants to minimize welfare loss, the regulator solves a constrained optimization that uses Lagrange multipliers across multiple products. The conditions resemble a generalized Lerner formula where the weighted markup equals a scaled inverse elasticity. For two goods, numbers matter: suppose goods have elasticities ε1=−2\varepsilon\_1=-2ε1​=−2, ε2=−4\varepsilon\_2=-4ε2​=−4 and the regulator uses weights proportional to demand quantities; the optimal markups will allocate more markups to the less elastic market.

3) Multi-product monopoly and cross-price effects. For two products with prices (p1,p2)(p\_1,p\_2)(p1​,p2​) and demands qi(p1,p2)q\_i(p\_1,p\_2)qi​(p1​,p2​), the FOC generalizes to a vector equality:

MRi=MCi,i=1,2,MR\_i=MC\_i,\quad i=1,2,MRi​=MCi​,i=1,2,

where MRi=∂R/∂qi=pi+∑jqj∂pj∂qiMR\_i=\partial R/\partial q\_i= p\_i+\sum\_j q\_j \frac{\partial p\_j}{\partial q\_i}MRi​=∂R/∂qi​=pi​+∑j​qj​∂qi​∂pj​​ (or written in inverse demand form). Numeric examples typically require specifying a demand matrix; solve for both prices jointly using linear algebra.

4) Price discrimination. Under first-degree (perfect) discrimination, a firm can capture all consumer surplus by setting ppp equal to each consumer’s willingness to pay; output equates to competitive output (no DWL). Under third-degree discrimination across segments with different elasticities, each segment satisfies the Lerner rule separately with its own elasticity. Numeric example: segment A with εA=−2\varepsilon\_A=-2εA​=−2 and MC=10 implies markup 0.5 of price: (pA−10)/pA=0.5⇒pA=20(p\_A-10)/p\_A=0.5\Rightarrow p\_A=20(pA​−10)/pA​=0.5⇒pA​=20. Segment B with εB=−4\varepsilon\_B=-4εB​=−4 gives (pB−10)/pB=0.25⇒pB≈13.33(p\_B-10)/p\_B=0.25\Rightarrow p\_B\approx13.33(pB​−10)/pB​=0.25⇒pB​≈13.33.

5) Empirical application: structural estimation of demand and cost. Econometricians estimate demand (Demand Functions prerequisite) and cost parameters to compute MR and MC and simulate policy changes. Concrete numbers are used to compute markups and counterfactual prices under regulation.

6) Industrial organization and strategic interaction. The MR=MC condition is the firm-level rule for price-setting in monopoly; in oligopoly (Cournot), each firm sets MRi=MCiMR\_i=MC\_iMRi​=MCi​ treating rivals’ outputs as fixed (best-response condition). Numeric Cournot examples use linear demands to produce closed-form equilibria.

7) Investment and capacity choice. When capacity is costly and dynamic, the shadow price of capacity (the Lagrange multiplier) derived above enters the investment decision: expand capacity until the marginal cost of capacity equals its discounted shadow benefit. Numeric dynamic models calibrate those multipliers to determine optimal investment paths.

Each of these applications relies on the primitives covered in the prerequisites: Demand Functions for mapping price ↔ quantity and elasticity, Cost Functions for MC and convexity, and Lagrange Multipliers for incorporating constraints and interpreting shadow values. Looking forward, mastering constrained profit maximization enables work on regulatory design, dynamic pricing, auction design, and empirical IO counterfactuals (e.g., mergers).

## Worked Examples (3)

### Linear Monopoly (unconstrained)

Inverse demand p(q)=100−2qp(q)=100-2qp(q)=100−2q, cost C(q)=20qC(q)=20qC(q)=20q. Find profit-maximizing q, p, and profit, and verify SOC.

1. Write revenue: R(q)=p(q)q=(100−2q)q=100q−2q2R(q)=p(q)q=(100-2q)q=100q-2q^2R(q)=p(q)q=(100−2q)q=100q−2q2.
2. Compute marginal revenue: MR(q)=dR/dq=100−4qMR(q)=dR/dq=100-4qMR(q)=dR/dq=100−4q. Numerically, for q=10, MR(10)=100-40=60 (example evaluation).
3. Compute marginal cost: MC(q)=dC/dq=20MC(q)=dC/dq=20MC(q)=dC/dq=20. Constant at 20.
4. Solve FOC: $100-4q=20\Rightarrow 4q=80\Rightarrow q^\*=20$.
5. Compute price: p∗=100−2⋅20=60p^\*=100-2\cdot20=60p∗=100−2⋅20=60. Compute profit: π=p∗q∗−C(q∗)=60⋅20−20⋅20=1200−400=800\pi=p^\*q^\*-C(q^\*)=60\cdot20-20\cdot20=1200-400=800π=p∗q∗−C(q∗)=60⋅20−20⋅20=1200−400=800.
6. Check SOC: MR′(q)=−4MR'(q)=-4MR′(q)=−4, MC′(q)=0MC'(q)=0MC′(q)=0, so π′′(q)=−4<0\pi''(q)=-4<0π′′(q)=−4<0 confirming a maximum.

**Insight:** This example shows the mechanical steps: compute MR, set MR=MC, compute price and profit, and verify second-order condition numerically.

### Capacity Constrained Monopoly

Same demand p(q)=100−2qp(q)=100-2qp(q)=100−2q and cost C(q)=20qC(q)=20qC(q)=20q. Capacity is K=15K=15K=15 (binding). Compute chosen q, p, profit, and the Lagrange multiplier λ\lambdaλ.

1. Unconstrained optimum from previous example is q∗=20q^\*=20q∗=20 which exceeds capacity K=15K=15K=15, so capacity binds.
2. Firm chooses q=K=15q=K=15q=K=15 and sets price to market-clearing price p(15)=100−2⋅15=70p(15)=100-2\cdot15=70p(15)=100−2⋅15=70.
3. Compute profit: π=(70−20)⋅15=50⋅15=750\pi=(70-20)\cdot15=50\cdot15=750π=(70−20)⋅15=50⋅15=750.
4. Form Lagrangian: L=p(q)q−C(q)+λ(K−q)\mathcal{L}=p(q)q-C(q)+\lambda(K-q)L=p(q)q−C(q)+λ(K−q). Stationarity condition: MR(q)−MC(q)−λ=0MR(q)-MC(q)-\lambda=0MR(q)−MC(q)−λ=0. At q=15q=15q=15, compute MR(15)=100−4⋅15=40MR(15)=100-4\cdot15=40MR(15)=100−4⋅15=40, MC(15)=20MC(15)=20MC(15)=20. So λ=MR−MC=40−20=20\lambda=MR-MC=40-20=20λ=MR−MC=40−20=20.
5. Interpretation: λ=20\lambda=20λ=20 means relaxing capacity by one unit increases profit by 20; numerically, if K→16, firm would produce q=16; price p(16)=100-32=68 and incremental profit roughly MR(15)-MC(15)=20.

**Insight:** This example teaches KKT logic: binding inequality implies a positive multiplier that equals MR-MC at the boundary. Multipliers have a clear economic interpretation as marginal profit of relaxing the constraint.

### Monopoly with Increasing Marginal Costs and SOC check

Demand p(q)=100−2qp(q)=100-2qp(q)=100−2q, cost C(q)=10q+0.5q2C(q)=10q+0.5q^2C(q)=10q+0.5q2 (so MC(q)=10+qMC(q)=10+qMC(q)=10+q). Solve for optimum, price, profit, and verify SOC.

1. Compute revenue R(q)=p(q)q=100q−2q2R(q)=p(q)q=100q-2q^2R(q)=p(q)q=100q−2q2 and MR(q)=100−4qMR(q)=100-4qMR(q)=100−4q.
2. Compute marginal cost: MC(q)=10+qMC(q)=10+qMC(q)=10+q. Evaluate: e.g., at q=10, MC(10)=20.
3. Solve FOC: $100-4q=10+q\Rightarrow 90=5q\Rightarrow q^\*=18$.
4. Compute price: p∗=100−2⋅18=64p^\*=100-2\cdot18=64p∗=100−2⋅18=64. Compute profit: π=64⋅18−(10⋅18+0.5⋅182)=1152−(180+162)=1152−342=810\pi=64\cdot18 - (10\cdot18 +0.5\cdot18^2)=1152-(180+162)=1152-342=810π=64⋅18−(10⋅18+0.5⋅182)=1152−(180+162)=1152−342=810.
5. Check SOC: MR′(q)=−4MR'(q)=-4MR′(q)=−4, MC′(q)=1MC'(q)=1MC′(q)=1, so π′′=−5<0\pi''=-5<0π′′=−5<0. Thus a local maximum. Also compute deadweight loss vs competition: competitive q\_c solves p=MC⇒100−2q=10+q⇒90=3q⇒qc=30p=MC\Rightarrow100-2q=10+q\Rightarrow90=3q\Rightarrow q\_c=30p=MC⇒100−2q=10+q⇒90=3q⇒qc​=30; DWL area numeric = 0.5*(p*-MC at q*)(q\_c - q*) = 0.5*(64-28)*(30-18)=0.5*36*12=216.

**Insight:** This example shows increasing marginal costs change the optimal q and lower markup relative to constant MC. The numeric SOC check demonstrates how cost curvature strengthens concavity of profit.

## Key Takeaways

- ✓

  The fundamental necessary condition for an interior profit-maximizing monopoly is MR=MC, where MR=p(q)+p′(q)qMR=p(q)+p'(q)qMR=p(q)+p′(q)q; always compute MR explicitly from the inverse demand. Example: p=100−2q⇒MR=100−4qp=100-2q\Rightarrow MR=100-4qp=100−2q⇒MR=100−4q.
- ✓

  Price markup over marginal cost is governed by the Lerner index: (p−MC)/p=−1/ε(p-MC)/p=-1/\varepsilon(p−MC)/p=−1/ε. More elastic demand implies smaller markups (concrete: ε=−5\varepsilon=-5ε=−5 gives markup 20% if MC known).
- ✓

  Second-order sufficiency requires π′′(q)=MR′(q)−MC′(q)<0\pi''(q)=MR'(q)-MC'(q)<0π′′(q)=MR′(q)−MC′(q)<0. For common specifications (linear demand, convex costs) this holds; always check numerically (e.g., MR′=−4MR'=-4MR′=−4, MC′=1MC'=1MC′=1 gives π′′=−5\pi''=-5π′′=−5).
- ✓

  Inequality constraints (capacity q≤Kq\le Kq≤K, price caps p≤pˉp\le\bar pp≤pˉ​) are handled with Kuhn–Tucker conditions: if the constraint binds, the multiplier equals MR−MCMR-MCMR−MC at the binding quantity and measures the marginal gain from relaxing the constraint. Example: capacity K=15K=15K=15 gave multiplier λ=20\lambda=20λ=20.
- ✓

  Corner solutions exist: if unconstrained q∗q^\*q∗ infeasible, optimum is at boundary. In price-cap cases, the firm becomes price-taker at pˉ\bar ppˉ​ and supplies demand q(pˉ)q(\bar p)q(pˉ​). Example: cap pˉ=50\bar p=50pˉ​=50 yields q=25q=25q=25 for p=100−2qp=100-2qp=100−2q.
- ✓

  MR and MC are primitives for wider analyses: welfare (deadweight loss), Ramsey pricing (regulatory second-best), multi-product pricing, price discrimination, Cournot best responses — all build on MR=MC logic applied to expanded settings.

## Common Mistakes

- ✗

  Confusing MR=MC with price equals MC. In monopoly, price usually exceeds MC. The correct FOC is MR=MCMR=MCMR=MC, not p=MCp=MCp=MC. Numeric counterexample: p=60p=60p=60, MC=20MC=20MC=20 with MR=20MR=20MR=20.
- ✗

  Forgetting to verify the second-order condition. Satisfying MR=MC can be a minimum or inflection if π′′≥0\pi''\ge0π′′≥0. Always compute MR′MR'MR′ and MC′MC'MC′ at the candidate point. Example failure: if MR′=−1MR'=-1MR′=−1 and MC′=2MC'=2MC′=2, then π′′=−3<0\pi''= -3<0π′′=−3<0 is ok, but if signs reversed check more carefully.
- ✗

  Applying equality-constrained Lagrange logic to inequality constraints without Kuhn–Tucker: when a constraint might not bind, you must include complementary slackness. Treating a potentially binding constraint as equality can produce infeasible multipliers (e.g., negative λ\lambdaλ).
- ✗

  Misinterpreting the multiplier: the Lagrange multiplier on q≤Kq\le Kq≤K equals MR(K)−MC(K)MR(K)-MC(K)MR(K)−MC(K) when binding. It is not an accounting profit; it's the marginal profit of increasing capacity by one unit. Interpreting it as average profit is incorrect.

## Practice

easy

Easy: Given inverse demand p(q)=80−4qp(q)=80-4qp(q)=80−4q and constant marginal cost MC=8MC=8MC=8, find the monopoly output q*, price p*, and profit. Verify SOC.

**Hint:** Compute MR from p(q)qp(q)qp(q)q and set equal to 8. Check second derivative of profit.

Show solution

Revenue R=80q−4q2R=80q-4q^2R=80q−4q2, so MR=80−8qMR=80-8qMR=80−8q. Set MR=MCMR=MCMR=MC: $80-8q=8\Rightarrow8q=72\Rightarrow q^*=9$. Price $p^*=80-4\cdot9=44.Profit. Profit .Profit\pi=(44-8)\cdot9=36\cdot9=324.SOC:. SOC: .SOC:MR'=-8$, $MC'=0so so so\pi''=-8<0$ confirms maximum.

medium

Medium: Demand p(q)=120−3qp(q)=120-3qp(q)=120−3q, cost C(q)=30q+q2C(q)=30q+q^2C(q)=30q+q2 (so MC=30+2qMC=30+2qMC=30+2q). There is a capacity limit K=12K=12K=12. Find the unconstrained optimum, check if capacity binds, and if it does find the multiplier λ\lambdaλ and the new profit.

**Hint:** Compute unconstrained MR, solve MR=MC. If q\*>K, set q=K and compute lambda=MR(K)-MC(K).

Show solution

Compute R=120q−3q2R=120q-3q^2R=120q−3q2, so MR=120−6qMR=120-6qMR=120−6q. MC=30+2q. Solve $120-6q=30+2q\Rightarrow90=8q\Rightarrow q^*=11.25$. Since $q^*=11.25<K=12,capacitydoesnotbind.Soq=11.25,p=120−3⋅11.25=120−33.75=86.25.Profit, capacity does not bind. So q=11.25, p=120-3\cdot11.25=120-33.75=86.25. Profit ,capacitydoesnotbind.Soq=11.25,p=120−3⋅11.25=120−33.75=86.25.Profit\pi=pq-C=86.25\cdot11.25-(30\cdot11.25+11.25^2)=969.84375-(337.5+126.5625)=969.84375-464.0625=505.78125.IfKwere11instead,itwouldbind:thenatK=11,. If K were 11 instead, it would bind: then at K=11, .IfKwere11instead,itwouldbind:thenatK=11,MR(11)=120-66=54$, $MC(11)=30+22=52,so, so ,so\lambda=2andprofitatq=11wouldbe and profit at q=11 would be andprofitatq=11wouldbe(p(11)-C'(??))computeprofit:p(11)=120−33=87, compute profit: p(11)=120-33=87, computeprofit:p(11)=120−33=87,\pi=(87\cdot11)-(30\cdot11+11^2)=957-(330+121)=506$. (Note small rounding differences.)

hard

Hard: Two-segment third-degree price discrimination. Segment A demand qA=100−2pAq\_A=100-2p\_AqA​=100−2pA​, segment B demand qB=80−4pBq\_B=80-4p\_BqB​=80−4pB​. Marginal cost is constant MC=10MC=10MC=10. The monopolist can set different prices pA,pBp\_A,p\_BpA​,pB​ for each segment. Find the optimal prices and quantities and compute aggregate profit.

**Hint:** Write revenue for each segment, compute MRA=MCMR\_A=MCMRA​=MC and MRB=MCMR\_B=MCMRB​=MC separately because segments are independent. Use inverse demand: pA=(100−qA)/2p\_A=(100-q\_A)/2pA​=(100−qA​)/2, pB=(80−qB)/4p\_B=(80-q\_B)/4pB​=(80−qB​)/4 or work directly with p(q)p(q)p(q) forms.

Show solution

Work with inverse demand: For A, pA=50−0.5qAp\_A=50-0.5q\_ApA​=50−0.5qA​ since qA=100−2pA⇒pA=(100−qA)/2=50−0.5qAq\_A=100-2p\_A\Rightarrow p\_A=(100-q\_A)/2=50-0.5q\_AqA​=100−2pA​⇒pA​=(100−qA​)/2=50−0.5qA​. Then RA=pAqA=50qA−0.5qA2R\_A=p\_A q\_A=50q\_A-0.5q\_A^2RA​=pA​qA​=50qA​−0.5qA2​ so MRA=50−qAMR\_A=50-q\_AMRA​=50−qA​. Set MRA=MC=10⇒qA∗=40MR\_A=MC=10\Rightarrow q\_A^\*=40MRA​=MC=10⇒qA∗​=40, price pA∗=50−0.5⋅40=30p\_A^\*=50-0.5\cdot40=30pA∗​=50−0.5⋅40=30. For B, qB=80−4pB⇒pB=20−0.25qBq\_B=80-4p\_B\Rightarrow p\_B=20-0.25q\_BqB​=80−4pB​⇒pB​=20−0.25qB​. Revenue RB=20qB−0.25qB2R\_B=20q\_B-0.25q\_B^2RB​=20qB​−0.25qB2​, so MRB=20−0.5qBMR\_B=20-0.5q\_BMRB​=20−0.5qB​. Set MRB=10⇒20−0.5qB=10⇒qB∗=20MR\_B=10\Rightarrow 20-0.5q\_B=10\Rightarrow q\_B^\*=20MRB​=10⇒20−0.5qB​=10⇒qB∗​=20, price pB∗=20−0.25⋅20=15p\_B^\*=20-0.25\cdot20=15pB∗​=20−0.25⋅20=15. Aggregate profit: π=(pA−10)qA+(pB−10)qB=(30−10)⋅40+(15−10)⋅20=20⋅40+5⋅20=800+100=900\pi=(p\_A-10)q\_A+(p\_B-10)q\_B= (30-10)\cdot40 + (15-10)\cdot20=20\cdot40 +5\cdot20=800+100=900π=(pA​−10)qA​+(pB​−10)qB​=(30−10)⋅40+(15−10)⋅20=20⋅40+5⋅20=800+100=900.

## Connections

Looking back: This lesson builds directly on three prerequisites. In Demand Functions we learned how to derive inverse demand p(q)p(q)p(q) and compute elasticities ε\varepsilonε, which are essential for writing MRMRMR as p(1+1/ε)p(1+1/\varepsilon)p(1+1/ε) and for computing Lerner markups. In Cost Functions we learned how to compute marginal cost MC(q)=C′(q)MC(q)=C'(q)MC(q)=C′(q) and examine convexity (MC′MC'MC′), which is required for the SOC and for interpreting how costs affect the markup. In Lagrange Multipliers we learned how to impose equality constraints; here we extended that machinery to inequality constraints using Kuhn–Tucker/KKT conditions and interpreted multipliers as shadow prices.

Looking forward: mastering profit maximization and constrained optimization enables several downstream topics. Industrial Organization (IO) uses MR=MC and constrained optimization in analyzing mergers, price discrimination, and Cournot/Bertrand oligopoly models. Regulatory economics uses the KKT shadow prices and Ramsey pricing rules to design tariffs and price caps; knowing how multipliers equal MR-MC at binding constraints is essential for regulatory counterfactuals. Structural estimation in empirical IO estimates demand and cost primitives so you can compute MR and MC on real data; this lesson supplies the formulas for constructing counterfactual prices and welfare. Topics in mechanism design and auction theory also leverage marginal revenue concepts (e.g., Myerson’s virtual valuations are a transformed MR concept). In short, MR=MC plus the KKT interpretation of constraints is a cornerstone that unlocks welfare analysis, pricing strategy, regulatory design, and empirical policy evaluation.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
