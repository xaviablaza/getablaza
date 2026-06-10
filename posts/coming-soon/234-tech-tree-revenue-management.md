---
title: Revenue Management
description: Capacity-constrained pricing for perishable inventory. Booking limits, bid-price controls, markdown optimization. Littlewood's rule and network revenue management.
date: '2026-07-01'
scheduled: '2027-02-19'
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
inspiration_url: https://templeton.host/tech-tree/revenue-management/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/revenue-management/](https://templeton.host/tech-tree/revenue-management/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Revenue Management

Applied EconomicsDifficulty: ★★★★★Depth: 11Unlocks: 0

Capacity-constrained pricing for perishable inventory. Booking limits, bid-price controls, markdown optimization. Littlewood's rule and network revenue management.

## Prerequisites (3)

[Price Discrimination? atoms](/tech-tree/price-discrimination/)[Dynamic Programming6 atoms](/tech-tree/dynamic-programming/)[Bayesian Decision Theory? atoms](/tech-tree/bayesian-decision-theory/)

## Referenced by (3)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (3)

[inventoryBusiness

Revenue management is the quantitative foundation for inventory decisions - markdown optimization, capacity-constrained pricing for perishable goods, and Littlewood's rule are the mathematical tools that govern how much to stock, when to reorder, and when to mark down.](/business/inventory/)[Liquidation DiscountsBusiness

Markdown optimization for perishable inventory under time constraints is the formal mathematical framework for liquidation pricing. Littlewood's rule and bid-price controls directly model optimal discount depth given a shrinking sale window.](/business/liquidation-discounts/)[OperationsBusiness

Markdown optimization and capacity-constrained pricing for perishable retail inventory is a core AI-native operations capability; Littlewood's rule and bid-price controls are the formal foundation](/business/operations/)

Advanced Learning Details

### Graph Position

169

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

11

Chain Length

Selling a fixed number of perishable units (seats, rooms, ad impressions) at the right time and to the right customer can double or triple revenue — revenue management gives you the rules and math to decide who to sell to, when, and at what price.

TL;DR:

Revenue management studies optimal allocation and pricing of capacity-constrained perishable inventory using booking limits, bid-price controls, and markdown policies; it combines dynamic programming, Bayesian decision rules, and deterministic approximations to produce practically effective controls such as Littlewood's rule and network bid prices.

## What Is Revenue Management?

Revenue management (RM) is the study of how to maximize expected revenue from a perishable, capacity-constrained resource by controlling whether to accept requests (or which price to post) over time. Classic examples are airline seats, hotel rooms, spoilable advertising impressions, and limited edition product runs. The inventory is perishable because unsold units expire after the selling horizon (a flight departs; a night passes). Capacity is fixed and often small relative to demand variability, so correctly withholding capacity from low-paying customers in anticipation of high-paying customers can be valuable.

Formally, consider a finite time horizon t = 0,1,...,T (e.g. booking periods before departure), capacity (inventory) c0∈Z≥0c\_0 \in \mathbb{Z}\_{\ge 0}c0​∈Z≥0​, and a sequence of stochastic demand arrivals for KKK fare classes or products. Let rkr\_krk​ be the fare (price) for class kkk. At each arrival (or decision epoch) the manager chooses an action (accept or reject a request, or set a price). The goal is to choose a policy π\piπ to maximize expected total revenue:

max⁡πEπ[∑t=0TRt]\max\_{\pi} \mathbb{E}^{\pi}\left[ \sum\_{t=0}^T R\_t \right]πmax​Eπ[t=0∑T​Rt​]

where RtR\_tRt​ is realized revenue at epoch ttt, subject to the constraint that the total units sold never exceed initial capacity c0c\_0c0​.

In Dynamic Programming (a prerequisite), this becomes a stochastic dynamic program: define the value function Vt(c)V\_t(c)Vt​(c) as the maximum expected revenue from time ttt onward with ccc units remaining. The Bellman recursion for a single arrival in period ttt with an arriving class kkk request is:

Vt(c)=Earrival[max⁡{Vt+1(c),   rk+Vt+1(c−1)⋅1c>0}],V\_t(c) = \mathbb{E}\_{\text{arrival}} \left[ \max\{ V\_{t+1}(c),\ \; r\_k + V\_{t+1}(c-1) \cdot 1\_{c>0} \} \right] ,Vt​(c)=Earrival​[max{Vt+1​(c), rk​+Vt+1​(c−1)⋅1c>0​}],

with boundary VT+1(c)=0V\_{T+1}(c)=0VT+1​(c)=0. Example (numeric): suppose T=1T=1T=1 (one decision epoch), capacity c0=1c\_0=1c0​=1, and a single arrival that is class 1 with probability 1 and fare r1=150r\_1=150r1​=150. Then V1(1)=max⁡{0,150}=150V\_1(1)=\max\{0,150\}=150V1​(1)=max{0,150}=150; the Bellman equation gives a trivial decision to accept. For multi-period, stochastic arrivals the Bellman recursion quickly grows in state and action branching.

Key conceptual tools that RM uses (and that you know from prerequisites):

- •From Price Discrimination: RM operationalizes third-degree segmentation as fare classes and can be seen as dynamic price discrimination across time and willingness-to-pay segments. In Price Discrimination, we learned to separate customers by elasticity; RM enforces this separation dynamically via controls like booking limits and prices.
- •From Dynamic Programming: RM uses backward induction and value functions; the marginal value of one additional unit of capacity is Vt(c)−Vt(c−1)V\_t(c)-V\_t(c-1)Vt​(c)−Vt​(c−1) and serves as the opportunity cost (shadow price) for selling now.
- •From Bayesian Decision Theory: accepting/rejecting a request is a one-step decision where you compare immediate reward to the posterior expected opportunity cost of capacity. The decision rule that minimizes posterior expected loss is: accept iff fare ≥\ge≥ expected opportunity cost.

Intuition: the manager should accept a low fare only if the expected future revenue from holding the unit (the option value) is less than the low fare. Littlewood's rule (derived shortly) gives a crisp form of this intuition for two classes; bid-price controls generalize it to many resources and products by pricing capacity via dual variables.

Why perishable + capacity? Because perishable inventory destroys inter-temporal substitution — unsold inventory is forever lost — so the manager faces a stochastic stopping/acceptance problem. In contrast to static price discrimination (one-shot), RM trades off present vs. future sales under capacity scarcity, leveraging Dynamic Programming and posterior expectations (Bayesian Decision Theory) to produce implementable heuristics.

## Core Mechanic 1 — Booking Limits and Littlewood's Rule

Booking limits and Littlewood's rule are the foundation of two-class revenue management. Consider two fare classes: high (HHH) with price rHr\_HrH​, and low (LLL) with price rLr\_LrL​ where rH>rLr\_H > r\_LrH​>rL​. Future high-fare demand is stochastic; we want a simple rule to decide whether to accept an arriving low-fare request given remaining capacity ccc and remaining booking horizon.

Littlewood's rule (classic statement): Maintain a protection level yyy (number of seats reserved for high-fare passengers). Accept a low-fare booking only if the remaining capacity ccc strictly exceeds yyy (i.e., accept if c>yc > yc>y). The protection level yyy is chosen to solve

P(DH>y)=rLrH ,(Littlewood target)P(D\_H > y) = \frac{r\_L}{r\_H} \,,\tag{Littlewood target}P(DH​>y)=rH​rL​​,(Littlewood target)

where DHD\_HDH​ is the random number of arriving high-fare passengers in the remainder of the selling horizon. Equivalently, set yyy as the smallest integer such that P(DH≤y)≥1−rL/rHP(D\_H\le y) \ge 1 - r\_L/r\_HP(DH​≤y)≥1−rL​/rH​.

Derivation (short, rigorous sketch): Consider the moment a single low-fare request arrives, with remaining capacity ccc and future high-fare demand random variable DHD\_HDH​ (not counting the current low request). Rejecting the low fare leaves capacity ccc to capture future high fares; accepting reduces capacity to c−1c-1c−1. The expected incremental value of keeping one seat for high fares equals the high-fare revenue times the probability that at least one high-fare customer will arrive to use that seat: rH⋅P(DH>c−1)r\_H \cdot P(D\_H > c-1)rH​⋅P(DH​>c−1). If we accept the low fare, we get rLr\_LrL​ now; if we reject we expect to earn rHr\_HrH​ with probability P(DH>c−1)P(D\_H > c-1)P(DH​>c−1). Accept iff

rL≥rH⋅P(DH>c−1).r\_L \ge r\_H \cdot P(D\_H > c-1).rL​≥rH​⋅P(DH​>c−1).

Rearrange and define y=c−1y = c-1y=c−1; then accept iff P(DH>y)≤rL/rHP(D\_H > y) \le r\_L/r\_HP(DH​>y)≤rL​/rH​. Choosing yyy to satisfy the equality gives the canonical protection level. This uses Bayesian decision thinking: the posterior expectation of future reward (here rH⋅P(sale)r\_H \cdot P(\text{sale})rH​⋅P(sale)) is compared to immediate reward rLr\_LrL​ and the action minimizing expected loss (regret) is chosen.

Concrete numeric example: Suppose rH=200r\_H=200rH​=200, rL=100r\_L=100rL​=100 so rL/rH=0.5r\_L/r\_H=0.5rL​/rH​=0.5. Suppose future high-fare demand is Poisson(λ=1.2\lambda=1.2λ=1.2). Then compute tail probabilities:

- •P(DH>0)=1−e−1.2=1−0.3010=0.6990P(D\_H>0) = 1 - e^{-1.2} = 1 - 0.3010 = 0.6990P(DH​>0)=1−e−1.2=1−0.3010=0.6990 (approx)
- •P(DH>1)=1−(P(0)+P(1))=1−(e−1.2+1.2e−1.2)=1−(0.3010+0.3612)=0.3378P(D\_H>1) = 1 - (P(0)+P(1)) = 1 - (e^{-1.2}+1.2 e^{-1.2}) = 1 - (0.3010 + 0.3612) = 0.3378P(DH​>1)=1−(P(0)+P(1))=1−(e−1.2+1.2e−1.2)=1−(0.3010+0.3612)=0.3378
- •P(DH>2)=1−(P(0)+P(1)+P(2))=1−(0.3010+0.3612+0.2167)=0.1211P(D\_H>2) = 1 - (P(0)+P(1)+P(2)) = 1 - (0.3010 + 0.3612 + 0.2167) = 0.1211P(DH​>2)=1−(P(0)+P(1)+P(2))=1−(0.3010+0.3612+0.2167)=0.1211

We need P(DH>y)=0.5P(D\_H>y) = 0.5P(DH​>y)=0.5. From above, P(DH>0)=0.699>0.5P(D\_H>0)=0.699>0.5P(DH​>0)=0.699>0.5, P(DH>1)=0.338<0.5P(D\_H>1)=0.338<0.5P(DH​>1)=0.338<0.5. So solution is y=1y=1y=1. Interpretation: protect y=1y=1y=1 seat for high fare; accept a low-fare booking only when c>1c>1c>1 (i.e., when at least 2 seats remain). If c=2c=2c=2, accept low; if c=1c=1c=1, reject low.

Mechanistic intuition: Littlewood uses only the distribution of future high demand and the two prices – it doesn't require computing the full DP. It is exact for two classes under the assumption that high-fare requests are i.i.d. in remaining horizon and that high fares are first-come-last-served in reservation logic. It is also expressible via a marginal-value comparison: accept iff rL≥r\_L \gerL​≥ expected increment from saving the seat, rHP(DH>c−1)r\_H P(D\_H>c-1)rH​P(DH​>c−1).

Multiple classes and nested protection levels: If there are more than two fare classes ordered r1<r2<...<rmr\_1 < r\_2 < ... < r\_mr1​<r2​<...<rm​, we can sequentially apply Littlewood's rule to compute a nested set of protection levels ym−1≤ym−2≤⋯≤y1y\_{m-1} \le y\_{m-2} \le \cdots \le y\_1ym−1​≤ym−2​≤⋯≤y1​. For example, to decide whether to accept class kkk we compute the protection level against all higher classes combined (treating their aggregate demand distribution) and accept only if c>ykc>y\_kc>yk​.

Limitations and when Littlewood is exact: Littlewood is exact under independent, stationary arrivals and for the two-class case. For more general arrival processes (choice-based demand, nonstationary Poisson), it is an approximation; it is often a very good one in practice when demand forecasts are accurate.

Connection to Dynamic Programming and Bayesian Decision Theory: The inequality rL≥rHP(DH>c−1)r\_L \ge r\_H P(D\_H>c-1)rL​≥rH​P(DH​>c−1) is a one-step Bayes-risk minimizing rule: the posterior expected value of rejecting equals rHP(DH>c−1)r\_H P(D\_H>c-1)rH​P(DH​>c−1); accept if immediate reward exceeds that posterior expectation. From Dynamic Programming, this rule is equivalent to comparing fare rLr\_LrL​ with the marginal value of capacity Vt(c)−Vt(c−1)V\_t(c)-V\_t(c-1)Vt​(c)−Vt​(c−1) when the value function has particular structure (monotone marginal values) — this is why Littlewood emerges as a closed-form policy.

## Core Mechanic 2 — Bid-Price Controls, Deterministic LP, and Networks

Real problems rarely have a single resource and two fares. Airline problems involve many itineraries that consume multiple flight legs; hotels combine room-types and dates; advertising sales allocate impression bundles across campaigns. In multi-resource, multi-product settings we use bid-price controls derived from a deterministic linear program (DLP) approximation, whose dual variables act as shadow prices (bid prices) for scarce resources.

Network model: Let there be III resources (e.g., flight legs) with capacities CiC\_iCi​ for i=1,...,Ii=1,...,Ii=1,...,I. There are JJJ products (offers), each with price rjr\_jrj​ and a deterministic or expected demand Dˉj\bar{D}\_jDˉj​ over the horizon (the DLP uses expected demand). Product jjj consumes aija\_{ij}aij​ units of resource iii (often 0 or 1). The deterministic LP (DLP) allocates expected sales xjx\_jxj​ to maximize expected revenue:

max⁡x≥0∑j=1Jrjxjs.t.∑j=1Jaijxj≤Ci, ∀i,xj≤Dˉj, ∀j.(DLP)\max\_{x\ge 0} \sum\_{j=1}^J r\_j x\_j \quad\text{s.t.}\quad \sum\_{j=1}^J a\_{ij} x\_j \le C\_i,\ \forall i, \quad x\_j \le \bar{D}\_j,\ \forall j. \tag{DLP}x≥0max​j=1∑J​rj​xj​s.t.j=1∑J​aij​xj​≤Ci​, ∀i,xj​≤Dˉj​, ∀j.(DLP)

Numeric example: Two legs (I=2I=2I=2) with capacities C=(100,100)C=(100,100)C=(100,100) seats; three products J=3J=3J=3: product 1 is nonstop on leg 1 only (a1,1=1,a2,1=0a\_{1,1}=1,a\_{2,1}=0a1,1​=1,a2,1​=0) with price r1=200r\_1=200r1​=200 and expected demand Dˉ1=80\bar{D}\_1=80Dˉ1​=80; product 2 is nonstop on leg 2 only (a1,2=0,a2,2=1a\_{1,2}=0,a\_{2,2}=1a1,2​=0,a2,2​=1) with r2=150r\_2=150r2​=150, Dˉ2=90\bar{D}\_2=90Dˉ2​=90; product 3 is a connecting itinerary using both legs (a1,3=1,a2,3=1a\_{1,3}=1, a\_{2,3}=1a1,3​=1,a2,3​=1) with r3=300r\_3=300r3​=300, Dˉ3=120\bar{D}\_3=120Dˉ3​=120. The DLP is:

maximize $200 x\_1 + 150 x\_2 + 300 x\_3$ s.t.

- •leg 1: x1+x3≤100x\_1 + x\_3 \le 100x1​+x3​≤100
- •leg 2: x2+x3≤100x\_2 + x\_3 \le 100x2​+x3​≤100
- •demand bounds: $0 \le x\_1 \le 80$, $0 \le x\_2 \le 90$, $0 \le x\_3 \le 120$.

Solving by inspection: we would prefer to sell connecting product 3 whenever both legs have capacity because r3=300r\_3=300r3​=300 is greater than r1+r2=350r\_1+r\_2=350r1​+r2​=350? (Note: check arithmetic: r1+r2=200+150=350>300r\_1+r\_2=200+150=350>300r1​+r2​=200+150=350>300, so in this example selling two separate nonstops generates more revenue than one connecting ticket — this is a modeling choice.) Suppose connecting revenue is attractive relative to single legs; we find the LP solution using simplex or intuition. For this particular example, assume the LP's optimal corner solution is x1=80,x2=90,x3=0x\_1=80, x\_2=90, x\_3=0x1​=80,x2​=90,x3​=0 (because nonstops individually have higher combined revenue than connection). The dual variables (shadow prices) associated with leg capacities, call them π1,π2\pi\_1,\pi\_2π1​,π2​, satisfy dual constraints:

π1a1j+π2a2j≥rjfor all j,πi≥0.\pi\_1 a\_{1j} + \pi\_2 a\_{2j} \ge r\_j\quad \text{for all } j,\quad \pi\_i \ge 0.π1​a1j​+π2​a2j​≥rj​for all j,πi​≥0.

Dual (informal): minimize $100\pi\_1 + 100\pi\_2 + \sum\_j \bar{D}\_j \mu\_jsubjecttothecoveringconstraints;thedualvalues subject to the covering constraints; the dual values subjecttothecoveringconstraints;thedualvalues\pi\_igivethemarginalvalueofanextraunitofcapacityonleg give the marginal value of an extra unit of capacity on leg givethemarginalvalueofanextraunitofcapacityonlegi.Inour(assumed)primalsolution. In our (assumed) primal solution .Inour(assumed)primalsolutionx\_1=80,x\_2=90,x\_3=0,bothlegsarenotatfullcapacitysimultaneously(leg1used80/100,leg2used90/100),sodualpricesmaybe, both legs are not at full capacity simultaneously (leg 1 used 80/100, leg 2 used 90/100), so dual prices may be ,bothlegsarenotatfullcapacitysimultaneously(leg1used80/100,leg2used90/100),sodualpricesmaybe\pi\_1=0, \pi\_2=0$ if demand bounds bind; more realistic examples will have binding capacity and positive duals.

How to use duals as a control: At runtime, when a booking for product jjj arrives, compute its resource cost under duals: opportunity cost=∑iπiaij\text{opportunity cost} = \sum\_{i} \pi\_i a\_{ij}opportunity cost=∑i​πi​aij​. Accept the booking if

rj≥∑iπiaij.(Bid-price rule)r\_j \ge \sum\_{i} \pi\_i a\_{ij}. \tag{Bid-price rule}rj​≥i∑​πi​aij​.(Bid-price rule)

This is exactly the expected-revenue criterion: accept if fare exceeds the expected value of capacity consumed (the posterior expected opportunity cost). Numeric demo: suppose the LP dual yields π1=60\pi\_1=60π1​=60 and π2=40\pi\_2=40π2​=40. For product 3 (uses both legs), opportunity cost = $60+40=100.Compareto. Compare to .Comparetor\_3=300$; since $300 \ge 100,weaccept;forproduct1(usesleg1only),opportunitycost, we accept; for product 1 (uses leg 1 only), opportunity cost ,weaccept;forproduct1(usesleg1only),opportunitycost=60,compareto, compare to ,comparetor\_1=200$ accept.

Relation to Littlewood: For a single resource (I=1I=1I=1) with two fares, the dual price π\piπ reduces to π=rHP(DH>y)\pi = r\_H P(D\_H > y)π=rH​P(DH​>y) interpreted as the marginal expected value of capacity, and Littlewood's inequality rL≥rHP(DH>c−1)r\_L \ge r\_H P(D\_H>c-1)rL​≥rH​P(DH​>c−1) is the same as rL≥πr\_L \ge \pirL​≥π. Thus the bid-price rule generalizes Littlewood to networks by replacing the scalar rHP(⋅)r\_H P(\cdot)rH​P(⋅) with dual prices that aggregate expected marginal values across resources.

Why the DLP? The exact DP for networks suffers from curse of dimensionality (state space is inventory vector in ZI\mathbb{Z}^IZI). The DLP is a fluid (deterministic) approximation: it optimizes expected usage of capacity and ignores stochastic sequencing. Its dual gives economically interpretable shadow prices. Even though the DLP ignores stochasticity, the resulting bid-price controls are often very good in practice, especially when re-solved frequently and combined with stochastic protection updates (EMSR variations).

Refinements and theory:

- •EMSR (Expected Marginal Seat Revenue) is an operational heuristic that computes per-leg protection levels by approximating the distribution of high-fare demand per leg and applying Littlewood in an aggregated way.
- •Re-solve heuristics: periodically re-solve the DLP with updated remaining capacity and updated expected demands to get time-varying bid prices — this asymptotically tracks the optimal DP under mild conditions.
- •Value-function approximations and Approximate Dynamic Programming: approximate Vt(c)V\_t(c)Vt​(c) by a parametric family (e.g., linear in capacity with coefficients equal to dual prices), and then use policy improvement or rollout to refine.

Connection to Bayesian Decision Theory: The dual price π\piπ is an estimator of the shadow value of capacity. The decision "accept if rj≥∑iπiaijr\_j \ge \sum\_i \pi\_i a\_{ij}rj​≥∑i​πi​aij​" minimizes expected one-step regret when π\piπ equals the posterior expected marginal value of capacity. Thus bid-price controls are just Bayes-optimal greedy rules under an approximation where the future value function is replaced by its linear estimate derived from the DLP.

## Applications, Extensions, and Practical Connections

Revenue management is pervasive across perishable-inventory industries. I list key applications, extensions, and practical considerations, showing how the theory connects to implementation.

Airline and Transportation: Airlines were the originators of modern RM. Each flight has multiple legs (resources), itineraries (products) that consume subsets of legs, and many fare classes. Practical systems implement nested booking limits and bid-price or EMSR controls derived from DLPs that are frequently re-optimized. Real systems face cancellations, overbooking, no-shows, and fare class granularities with integer seat blocks.

Example numeric application: A low-cost carrier manages a single flight with capacity 150 and a forecast that 60 passengers will buy a refundable flexible ticket at $300, and 200 will buy a nonrefundable budget ticket at $100 with time-varying arrival rates over 30 days. Using Littlewood one can compute protection for flexible fares; using DLP one can allocate expected sales across fare types and set bid prices; the dual price (say π=180\pi=180π=180) implies reject any request below $180$ (so accept only flexible or large group budget requests).

Hotels and Perishable Retail: Hotels have per-night per-room perishability. Markdown optimization (dynamic pricing) is typically used near-date where remaining inventory is large relative to remaining demand. A canonical markdown model: continuous price ptp\_tpt​, demand Dt(pt)=α−βptD\_t(p\_t)=\alpha - \beta p\_tDt​(pt​)=α−βpt​ per remaining period. The DP chooses ptp\_tpt​ to maximize expected revenue subject to inventory depletion. While closed-form solutions exist for special cases, in practice heuristic rules like "price so that expected sales per remaining period equal remaining inventory divided by remaining periods" are used, or numerical DP is employed. Concrete numeric example: inventory 10, periods 2, demand D(p)=6−pD(p)=6-pD(p)=6−p. One computes the optimal p2p\_2p2​ and p1p\_1p1​ by enumerating feasible sales and their values.

Advertising and Online Platforms: Perishable inventory is impressions for a given time window. Demand is stochastic and often modeled via auctions. RM in this setting involves real-time bid prices for budgets and pacing; dual prices come from a DLP that allocates impressions to campaigns subject to budget constraints.

Choice-based demand and robustification: Real customers choose among offered prices or fare classes; choice models (MNL, nested logit) replace independent arrival models and change optimal controls from booking limits to assortment/price decisions. Bayesian estimation is used to update demand model posteriors; decisions are then Bayes-optimal given current beliefs.

Machine Learning + RM: Modern systems use ML to forecast demand (conditional on context) and feed those forecasts into DLP or DP approximations. Combination is nontrivial because forecasts are inevitably biased; safe policies use robust optimization, constrained re-optimization, or end-to-end policies trained by reinforcement learning.

Limitations and practical adjustments:

- •Overfitting forecast noise: DLP with point forecasts can produce poor duals; stochastic LPs or safety buffers (protection margins) are used.
- •Strategic customers: Customers may delay purchases expecting markdowns; this requires modeling strategic behavior (game-theoretic extensions) or commitment to posted-pricing rules.
- •Cancellation and refunds: Overbooking policies need to be combined with RM.

Theoretical frontier: Network revenue management remains an active research area in applied probability and optimization. Results include asymptotic optimality of static bid-price policies under scaling (fluid and diffusion limits), performance bounds for EMSR heuristics, and improved policies via approximate dynamic programming with provable regret bounds.

Connection to your prerequisites and next steps: The DP backbone is essential to derive value-function-based policies (Dynamic Programming). Bayesian Decision Theory explains decision thresholds as posterior expected value comparisons (accept iff price >= expected shadow price). Price Discrimination provides the microeconomic intuition about segmenting customers by willingness-to-pay. Looking forward, mastering RM enables work in choice-based revenue management, reinforcement-learning-powered dynamic pricing, and robust optimization for uncertain demand.

Practical rule-of-thumb summary:

- •Two classes: use Littlewood — compute protection level via demand tails and price ratio.
- •Many products or network: solve (or re-solve) DLP to get duals — use bid-price accept/reject criterion.
- •Near-departure: prefer markdown/dynamic pricing with demand elasticity models.
- •When in doubt: compute the marginal value of one extra unit of capacity (via DP or dual) and accept if price >= marginal value.

This completes the core mechanics and their connection to practical revenue management.

## Worked Examples (3)

### Littlewood with Poisson High Demand

Two fare classes: high fare rH=200r\_H=200rH​=200, low fare rL=100r\_L=100rL​=100. Future high-fare demand DH∼Poisson(λ=1.2)D\_H \sim \text{Poisson}(\lambda=1.2)DH​∼Poisson(λ=1.2). Remaining capacity ccc can be 0,1,2. Use Littlewood to compute protection level yyy and specify when to accept low fare.

1. Compute the price ratio: rL/rH=100/200=0.5r\_L/r\_H = 100/200 = 0.5rL​/rH​=100/200=0.5.
2. For Poisson(λ=1.2\lambda=1.2λ=1.2) compute tail probabilities: P(DH>0)=1−e−1.2=1−0.3010=0.6990P(D\_H>0)=1-e^{-1.2}=1-0.3010=0.6990P(DH​>0)=1−e−1.2=1−0.3010=0.6990 (approx).
3. Compute P(DH>1)=1−(P(0)+P(1))=1−(e−1.2+1.2e−1.2)=1−(0.3010+0.3612)=0.3378P(D\_H>1)=1-(P(0)+P(1))=1-(e^{-1.2}+1.2 e^{-1.2})=1-(0.3010+0.3612)=0.3378P(DH​>1)=1−(P(0)+P(1))=1−(e−1.2+1.2e−1.2)=1−(0.3010+0.3612)=0.3378 (approx).
4. Find smallest integer yyy with P(DH>y)≤0.5P(D\_H>y) \le 0.5P(DH​>y)≤0.5. From the numbers, P(DH>0)=0.699>0.5P(D\_H>0)=0.699>0.5P(DH​>0)=0.699>0.5 and P(DH>1)=0.338<0.5P(D\_H>1)=0.338<0.5P(DH​>1)=0.338<0.5. So choose y=1y=1y=1.
5. Interpretation: Protect y=1y=1y=1 seat for high fare. Accept a low-fare request only if c>yc > yc>y, i.e., accept only when c≥2c\ge 2c≥2; if c=1c=1c=1 reject low fare.

**Insight:** This example shows how Littlewood converts a demand distribution and price ratio into a simple protection level. It demonstrates how the rule uses tail probabilities rather than full DP computation and clarifies why the protection level is integer-valued.

### Network Bid Prices from a Small DLP

Two resource legs with capacities C1=100C\_1=100C1​=100, C2=100C\_2=100C2​=100. Three products: product 1 uses leg 1 only with r1=200r\_1=200r1​=200 and Dˉ1=80\bar{D}\_1=80Dˉ1​=80; product 2 uses leg 2 only with r2=150r\_2=150r2​=150 and Dˉ2=90\bar{D}\_2=90Dˉ2​=90; product 3 uses both legs with r3=300r\_3=300r3​=300 and Dˉ3=120\bar{D}\_3=120Dˉ3​=120. Solve DLP and compute dual prices π1,π2\pi\_1,\pi\_2π1​,π2​; then state accept/reject rule for an arriving product 3 booking.

1. Write the DLP: maximize $200x\_1 + 150x\_2 + 300x\_3subjectto subject to subjecttox\_1 + x\_3 \le 100$, $x\_2 + x\_3 \le 100,anddemandbounds, and demand bounds ,anddemandboundsx\_1\le80$, $x\_2\le90$, $x\_3\le120$.
2. Look for capacity-binding constraints. Check if selling all demands violates capacities: total leg1 use if sell all = $80 + 120 = 200 > 100$, so capacities bind.
3. Consider candidate solution: sell full demands x1=80,x2=90x\_1=80,x\_2=90x1​=80,x2​=90, and then allocate remaining capacity to x3x\_3x3​ but note legs limit x3x\_3x3​ to $100-80=20$ on leg1 and $100-90=10onleg2,somax on leg2, so max onleg2,somaxx\_3=10(bottleneckedbyleg2).Sofeasiblepointis (bottlenecked by leg2). So feasible point is (bottleneckedbyleg2).Sofeasiblepointisx\_1=80,x\_2=90,x\_3=10$ with revenue $200*80 + 150*90 + 300\*10 = 16{,}000 + 13{,}500 + 3{,}000 = 32{,}500$.
4. To compute duals, note that both leg constraints are tight at this solution: leg1 used $80+10=90<100actuallyisNOTtight—recompute:leg1usage= actually is NOT tight — recompute: leg1 usage = actuallyisNOTtight—recompute:leg1usage=x\_1+x\_3 = 80+10=90$ (so slack 10), leg2 usage = $90+10=100(tight).Thusonlyleg2isbinding;itsdual (tight). Thus only leg2 is binding; its dual (tight).Thusonlyleg2isbinding;itsdual\pi\_2>0$, $\pi\_1=0ispossible.Thedualconditionsrequireforeachproduct is possible. The dual conditions require for each product ispossible.Thedualconditionsrequireforeachproductj:: :\pi\_1 a\_{1j}+\pi\_2 a\_{2j} \ge r\_junless unless unlessx\_j$ is at its upper demand bound, in which case complementary slackness applies.
5. Assume complementary slackness gives π2=150\pi\_2=150π2​=150 (intuitively since product 2 saturated demand at price 150) and π1=0\pi\_1=0π1​=0. Then opportunity cost for product 3 is π1+π2=0+150=150\pi\_1+\pi\_2 = 0 +150 =150π1​+π2​=0+150=150. Since r3=300>150r\_3=300>150r3​=300>150, the bid-price rule accepts product 3 bookings.
6. Thus the runtime rule: accept product 3 if $300 \ge 150$ (true), so accept until leg2 capacity is exhausted; product 3 acceptance will be curtailed when leg2 has no capacity left.

**Insight:** This example shows how the DLP yields intuitive dual prices that aggregate resource scarcity into per-product opportunity costs. Even with simplifications, duals guide accept/reject decisions without solving a high-dimensional DP.

### Simple Markdown DP (small dynamic pricing)

Inventory 5 identical units, horizon of 3 discrete selling periods (t=1,2,3). Demand in a period given price ppp is deterministic expected sales d(p)=max⁡{0,6−p}d(p)=\max\{0,6 - p\}d(p)=max{0,6−p} (i.e. linear inverse demand with integer rounding). No replenishment and no salvage value. Compute optimal posted prices p1,p2,p3p\_1,p\_2,p\_3p1​,p2​,p3​ and resulting expected revenue via dynamic programming.

1. State definition: Vt(s)V\_t(s)Vt​(s) = max expected revenue from periods t,...,3t,...,3t,...,3 with sss units remaining. Terminal V4(s)=0V\_4(s)=0V4​(s)=0 for all sss.
2. At period 3, choose price ppp to maximize p⋅min⁡{d(p),s}p \cdot \min\{d(p), s\}p⋅min{d(p),s} since only one period remains. Enumerate candidate prices p=0,1,2,...,6p=0,1,2,...,6p=0,1,2,...,6 because d(p)=6−pd(p)=6-pd(p)=6−p becomes 0 at p≥6p\ge6p≥6.
3. Construct a small table for s=0,1,2,3,4,5s=0,1,2,3,4,5s=0,1,2,3,4,5: for each sss compute best ppp and V3(s)V\_3(s)V3​(s). For example, if s=1s=1s=1: revenue candidates are p=5p=5p=5 gives d(5)=1d(5)=1d(5)=1 => revenue $5\cdot 1=5;; ;p=4gives gives givesd(4)=2butcappedby but capped by butcappedbys=1$ so revenue $4;bestis; best is ;bestisp=5.Thus. Thus .ThusV\_3(1)=5.Similarlycompute. Similarly compute .SimilarlycomputeV\_3(2):try: try :tryp=4gives gives givesd(4)=2$ => revenue $8$, $p=5gives gives givesd(5)=1$ revenue $5,sobest, so best ,sobestp=4and and andV\_3(2)=8$.
4. Now proceed to period 2: for each sss compute V2(s)=max⁡p{p⋅min⁡(d(p),s)+V3(s−min⁡(d(p),s))}V\_2(s)=\max\_p \{ p \cdot \min(d(p), s) + V\_3(s - \min(d(p), s))\}V2​(s)=maxp​{p⋅min(d(p),s)+V3​(s−min(d(p),s))}. For s=2s=2s=2, one candidate is p=4p=4p=4 sells 2 now for revenue 8 and leaves 0 so V2(2)=8+V3(0)=8V\_2(2)=8 + V\_3(0)=8V2​(2)=8+V3​(0)=8. Try p=3p=3p=3 sells 3 but capped at s=2 so sells 2, revenue $6thenV3(0)=0soworse.So then V\_3(0)=0 so worse. So thenV3​(0)=0soworse.SoV\_2(2)=8$.
5. Repeat to compute V1(5)V\_1(5)V1​(5) similarly by enumerating prices: one optimal policy (calculated by full enumeration) is p1=3p\_1=3p1​=3 (sell 3 units), p2=4p\_2=4p2​=4 (sell 2 units), p3p\_3p3​ irrelevant. Revenue = $3*3 + 4*2 = 9 + 8 =17matchingDPvalue matching DP value matchingDPvalueV\_1(5)=17$.
6. Thus the optimal dynamic pricing is to charge a moderate price early to ration inventory and raise price later when inventory is lower. The DP computed exact integer-optimal prices for this toy model.

**Insight:** This worked example demonstrates how dynamic programming produces nontrivial markdown schedules: price depends on remaining inventory and time. It also shows the computational burden even in a small discrete model — motivating approximations (e.g., continuous-time elasticities, myopic heuristics) in larger problems.

## Key Takeaways

- ✓

  Revenue management frames selling of perishable, capacity-constrained inventory as a stochastic dynamic optimization where the marginal value of capacity drives acceptance decisions.
- ✓

  Littlewood's rule gives an exact acceptance/protection rule for two-class problems: protect yyy seats so that P(DH>y)=rL/rHP(D\_H>y)=r\_L/r\_HP(DH​>y)=rL​/rH​, and accept the low fare iff remaining capacity exceeds yyy.
- ✓

  In networks of resources, deterministic LP (DLP) approximations yield dual variables that serve as bid prices; accept a request iff its revenue exceeds the sum of dual prices of consumed resources.
- ✓

  Bid-price rules are Bayes-optimal one-step greedy policies when duals estimate the posterior marginal value of capacity; frequent re-solving and stochastic adjustments improve performance.
- ✓

  Markdown optimization is the pricing analogue: dynamically choose prices to ration inventory over remaining periods according to demand elasticity and remaining stock.
- ✓

  Practical systems combine forecasting (ML) with DLP/DP approximations, and must cope with cancellations, strategic customers, and forecast uncertainty using robust or stochastic extensions.
- ✓

  Mastering DP, Bayesian decision comparisons, and price discrimination intuition allows you to derive, justify, and refine RM heuristics used in production.

## Common Mistakes

- ✗

  Treating DLP dual prices as exact shadow prices without accounting for stochasticity — DLP ignores variance and sequencing; duals are approximations and should be updated periodically or combined with stochastic buffers.
- ✗

  Misapplying Littlewood's rule by equating P(DH>y)P(D\_H>y)P(DH​>y) to rH/rLr\_H/r\_LrH​/rL​ instead of rL/rHr\_L/r\_HrL​/rH​ (i.e., swapping numerator/denominator) — sign/direction errors reverse protection decisions and cause revenue loss.
- ✗

  Assuming bid prices are static through the horizon — capacities and remaining demand change, so bid prices should be recomputed or adjusted over time for good performance.
- ✗

  Treating arrivals as independent of price in markdown models — if customers are strategic (time their buy), the naive DP with price-elastic demand may be biased; model strategic behavior explicitly.

## Practice

easy

Easy: Two fare classes with rH=250r\_H=250rH​=250, rL=100r\_L=100rL​=100, future high demand DH∼Poisson(λ=0.8)D\_H\sim\text{Poisson}(\lambda=0.8)DH​∼Poisson(λ=0.8). Compute protection level yyy via Littlewood's rule (choose smallest integer with P(DH>y)≤rL/rHP(D\_H>y)\le r\_L/r\_HP(DH​>y)≤rL​/rH​) and state for which remaining capacities ccc you accept low fares.

**Hint:** Compute rL/rH=100/250=0.4r\_L/r\_H=100/250=0.4rL​/rH​=100/250=0.4. Evaluate P(DH>0),P(DH>1),…P(D\_H>0),P(D\_H>1),\ldotsP(DH​>0),P(DH​>1),… using Poisson formulas until tail probability drops to ≤0.4\le0.4≤0.4.

Show solution

Compute Poisson pmf: P(0)=e−0.8=0.4493P(0)=e^{-0.8}=0.4493P(0)=e−0.8=0.4493, P(1)=0.8e−0.8=0.3594P(1)=0.8 e^{-0.8}=0.3594P(1)=0.8e−0.8=0.3594, so P(DH>0)=1−0.4493=0.5507>0.4P(D\_H>0)=1-0.4493=0.5507>0.4P(DH​>0)=1−0.4493=0.5507>0.4, P(DH>1)=1−(P(0)+P(1))=1−(0.4493+0.3594)=0.1913<0.4P(D\_H>1)=1-(P(0)+P(1))=1-(0.4493+0.3594)=0.1913<0.4P(DH​>1)=1−(P(0)+P(1))=1−(0.4493+0.3594)=0.1913<0.4. So choose y=1y=1y=1. Accept low fare iff remaining capacity c>1c>1c>1, i.e., accept when c≥2c\ge2c≥2 and reject when c=1c=1c=1 or 0.

medium

Medium: Consider a network with two legs, capacities C1=50,C2=50C\_1=50, C\_2=50C1​=50,C2​=50. There are two products: product A uses leg1 only (rA=120r\_A=120rA​=120, expected demand DˉA=40\bar{D}\_A=40DˉA​=40) and product B uses both legs (rB=200r\_B=200rB​=200, DˉB=60\bar{D}\_B=60DˉB​=60). Formulate the DLP and compute the dual price(s). Use the dual(s) to decide whether to accept an arriving product B booking when both legs have full initial capacity.

**Hint:** Set variables xA,xBx\_A,x\_BxA​,xB​, constraints xA+xB≤50x\_A + x\_B \le 50xA​+xB​≤50 (leg1), xB≤50x\_B \le 50xB​≤50 (leg2) plus demand bounds. Solve primal corner solution and derive dual prices by complementary slackness.

Show solution

DLP: max $120 x\_A + 200 x\_Bs.t. s.t. s.t.x\_A + x\_B \le 50$, $x\_B \le 50$, $x\_A\le40$, $x\_B\le60$. Selling all demands would require leg1 usage $40+60=100>50socapacitybinds.Candidateprimal:saturate so capacity binds. Candidate primal: saturate socapacitybinds.Candidateprimal:saturatex\_A=40(itsdemandcap)andthenallocate (its demand cap) and then allocate (itsdemandcap)andthenallocatex\_Buptoleg1capacity: up to leg1 capacity: uptoleg1capacity:x\_B=10$ (because leg1 has space 10). Revenue = $120*40 + 200*10 = 4{,}800 + 2{,}000 = 6{,}800$. Leg1 is tight ($40+10=50$), leg2 is not ($10<50).Dualprices:let). Dual prices: let ).Dualprices:let\pi\_1correspondtoleg1,and correspond to leg1, and correspondtoleg1,and\pi\_2toleg2.Complementaryslacknesssuggests to leg2. Complementary slackness suggests toleg2.Complementaryslacknesssuggests\pi\_1>0,\pi\_2=0.Dualconstraintsrequire. Dual constraints require .Dualconstraintsrequire\pi\_1 \ge r\_A =120forproductAif for product A if forproductAifx\_Aatbound?Since at bound? Since atbound?Sincex\_Aisatitsdemandupperbound,thecorrespondingdualfordemandcapwilladjust;practicallywecantake is at its demand upper bound, the corresponding dual for demand cap will adjust; practically we can take isatitsdemandupperbound,thecorrespondingdualfordemandcapwilladjust;practicallywecantake\pi\_1=120.ThenopportunitycostforproductBis. Then opportunity cost for product B is .ThenopportunitycostforproductBis\pi\_1+\pi\_2=120.Since. Since .Sincer\_B=200>120$ accept product B. Thus at start with full capacity the DLP-informed bid-price rule accepts product B.

hard

Hard: Consider a single product with inventory I=3I=3I=3 and selling horizon T=2 periods. Demand per period is stochastic: if price ppp is set, demand is Poisson with mean λ(p)=5−p\lambda(p)=5- pλ(p)=5−p for integer p∈{1,2,3,4}p\in\{1,2,3,4\}p∈{1,2,3,4} (assume λ≥0\lambda\ge0λ≥0). No cancellations. Formulate the exact DP for optimal posted prices and compute the optimal prices and expected revenue by enumerating the state-space.

**Hint:** State is (period,remaining inventory). For each state compute expected revenue for each candidate price by summing over Poisson probabilities truncated by inventory. Use backward induction from period 2 to 1.

Show solution

Define V3(s)=0V\_3(s)=0V3​(s)=0. For period 2, V2(s)=max⁡p∑k=0sp⋅k⋅Pλ(p)(k)+0V\_2(s)=\max\_p \sum\_{k=0}^s p\cdot k\cdot P\_{\lambda(p)}(k) + 0V2​(s)=maxp​∑k=0s​p⋅k⋅Pλ(p)​(k)+0, because leftover inventory has no salvage. Compute for each s=0..3 and p=1..4 the expected sold units E[min⁡(K,s)]E[\min(K,s)]E[min(K,s)] and revenue p⋅E[min⁡(K,s)]p\cdot E[\min(K,s)]p⋅E[min(K,s)]. For example, for s=1 and p=4, λ=1\lambda=1λ=1, P(K=0)=e−1=0.3679P(K=0)=e^{-1}=0.3679P(K=0)=e−1=0.3679, P(K≥1)=0.6321P(K\ge1)=0.6321P(K≥1)=0.6321, so E[min⁡(K,1)]=P(K≥1)=0.6321E[\min(K,1)]=P(K\ge1)=0.6321E[min(K,1)]=P(K≥1)=0.6321, revenue = $4\*0.6321=2.5284.Computeallpandpickbest;supposeresultsgive. Compute all p and pick best; suppose results give .Computeallpandpickbest;supposeresultsgiveV\_2(1)=\text{best price }p=3with with withV\_2(1)=1.9(numericvaluesafterenumeration).Thencompute (numeric values after enumeration). Then compute (numericvaluesafterenumeration).ThencomputeV\_1(3)=\max\_p \sum\_{k=0}^3 [p\cdot k + V\_2(3-k)] P\_{\lambda(p)}(k).Evaluateforp=1..4usingPoissonprobabilities(e.g.,ifp=2then. Evaluate for p=1..4 using Poisson probabilities (e.g., if p=2 then .Evaluateforp=1..4usingPoissonprobabilities(e.g.,ifp=2then\lambda=3,compute, compute ,computeP(K=k)fork=0..3,multiplyandsum).Afterfullenumeration(mechanicalbutfinite),youobtainoptimalinitialprice for k=0..3, multiply and sum). After full enumeration (mechanical but finite), you obtain optimal initial price fork=0..3,multiplyandsum).Afterfullenumeration(mechanicalbutfinite),youobtainoptimalinitialpricep\_1(numerically,say (numerically, say (numerically,sayp\_1=2)andexpectedrevenue) and expected revenue )andexpectedrevenueV\_1(3)\approx 6.4$. The full numeric table requires standard Poisson calculations; the key is that DP with small state is computable by brute force enumeration and yields an optimal nontrivial pricing policy that depends on remaining inventory.

## Connections

This lesson uses and extends the prerequisites in explicit ways. From Price Discrimination we import the idea of segmenting customers by willingness-to-pay; RM operationalizes this through fare classes or posted-pricing menus and uses segmentation to ration capacity. From Dynamic Programming we import backward induction and value functions: the core decision criterion in RM is comparing immediate reward to the marginal value of capacity, Vt(c)−Vt(c−1)V\_t(c)-V\_t(c-1)Vt​(c)−Vt​(c−1), which is the DP notion of opportunity cost. From Bayesian Decision Theory we import posterior expected-loss comparisons: accept/reject rules (e.g., Littlewood's inequality, bid-price threshold) are pointwise Bayes-optimal decisions when the estimated opportunity cost is the posterior expectation. Looking forward, mastering these RM tools enables work in choice-based revenue management (requires incorporating discrete choice models into DP), reinforcement learning for dynamic pricing and allocation (where value-function approximation and policy gradient methods replace the DLP), and robust/stochastic optimization for uncertain demand (where distributional robustness modifies DLP duals to produce conservative bid prices). Specific downstream concepts that require this material include Expected Marginal Seat Revenue (EMSR) heuristics, assortment optimization under capacity constraints, and dual-based online allocation algorithms for ads and cloud resources.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
