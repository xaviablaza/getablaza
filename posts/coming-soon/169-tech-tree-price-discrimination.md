---
title: Price Discrimination
description: First, second, third degree price discrimination. Two-part tariffs, bundling, versioning. Welfare effects by degree.
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
permalink: /tech-tree/price-discrimination/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Price Discrimination

Applied EconomicsDifficulty: ★★★★☆Depth: 10Unlocks: 1

First, second, third degree price discrimination. Two-part tariffs, bundling, versioning. Welfare effects by degree.

## Prerequisites (2)

[Profit Maximization? atoms](/tech-tree/profit-maximization/)[Consumer Surplus? atoms](/tech-tree/consumer-surplus/)

## Unlocks (1)

[Revenue Managementlvl 5](/tech-tree/revenue-management/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[Subscription PricingBusiness

A fixed monthly fee plus a per-unit charge is a two-part tariff - a classic form of second-degree price discrimination. The fixed fee extracts baseline consumer surplus while the usage fee segments heavy vs light users.](/business/subscription-pricing/)

Advanced Learning Details

### Graph Position

66

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

10

Chain Length

Firms from airlines to software vendors routinely charge different customers different prices — understanding how and why lets you predict firm behavior, welfare consequences, and regulatory trade-offs.

TL;DR:

Price discrimination is the set of techniques a firm with market power uses to charge different prices to different buyers (or for different quantities/qualities) to increase profit; the lesson shows the mechanics of first-, second-, and third-degree discrimination, two-part tariffs, bundling and versioning, and their welfare effects.

## What Is Price Discrimination?

Definition and motivation

Price discrimination is any pricing policy that charges different prices to different buyers for essentially the same good or service when differences are not driven by cost differences. For price discrimination to be feasible the firm needs: (i) market power (ability to set price above marginal cost), (ii) the ability to segment markets or observe signals correlated with willingness to pay, and (iii) limited arbitrage (customers cannot easily resell or arbitrage away price differences).

Degrees of price discrimination (core taxonomy)

- •First-degree (perfect) price discrimination: the seller charges each consumer her exact willingness to pay for each unit. This extracts all consumer surplus and, if costs allow, produces the first-best allocation (output where marginal willingness to pay equals marginal cost). It requires extraordinary information — essentially the entire demand curve of each consumer.

- •Second-degree price discrimination: the seller offers a menu of quantity- or quality-contingent prices (nonlinear tariffs) and lets consumers self-select. Examples: block pricing, quantity discounts, versioning of products, two-part tariffs.

- •Third-degree price discrimination: the seller observes an observable characteristic (group membership) correlated with willingness to pay and sets different linear prices for each segment (student discounts, senior fares, geographic pricing).

Core intuition in 1 graph/formula

Start from a standard monopoly demand: P(Q)=a−bQP(Q)=a-bQP(Q)=a−bQ. In "In Profit Maximization, we learned" that monopoly chooses output where marginal revenue equals marginal cost: MR(Q)=a−2bQ=MCMR(Q)=a-2bQ=MCMR(Q)=a−2bQ=MC. Solve for monopoly quantity and price:

QM=a−MC2b,PM=a−bQM=a+MC2.Q\_M=\frac{a-MC}{2b},\qquad P\_M=a-bQ\_M=\frac{a+MC}{2}.QM​=2ba−MC​,PM​=a−bQM​=2a+MC​.

Concrete numeric example: let a=100a=100a=100, b=1b=1b=1, MC=10MC=10MC=10. Then

QM=100−102=45,PM=100−45=55.Q\_M=\frac{100-10}{2}=45,\qquad P\_M=100-45=55.QM​=2100−10​=45,PM​=100−45=55.

Consumer surplus (see "In Consumer Surplus, we learned") is the area between demand and price: here

CS=12(QM)(P(0)−PM)=12×45×(100−55)=12×45×45=1012.5.CS=\frac12(Q\_M)(P(0)-P\_M)=\frac12\times45\times(100-55)=\frac12\times45\times45=1012.5.CS=21​(QM​)(P(0)−PM​)=21​×45×(100−55)=21​×45×45=1012.5.

Why discriminate? Because different customers have different maximum willingness to pay. If the monopolist could charge each consumer her exact willingness to pay (first-degree), output expands to the efficient level where P(Q)=MCP(Q)=MCP(Q)=MC, eliminating deadweight loss and capturing all surplus as profit. In practice, firms use weaker devices (second- and third-degree) to harvest part of that surplus.

When thinking about welfare: price discrimination reallocates surplus from consumers to producers. It can increase total welfare relative to single-price monopoly when discrimination leads to higher aggregate output (reducing deadweight loss), but it can reduce welfare if it lowers output in some segments even while increasing profit.

## Core Mechanic 1 — First- and Third-Degree Price Discrimination, Markups and Welfare

First-degree (perfect) price discrimination (PD)

Mechanics: with perfect information the firm charges each infinitesimal unit at the consumer's marginal willingness to pay, so output is chosen where P(Q)=MCP(Q)=MCP(Q)=MC. Using P(Q)=a−bQP(Q)=a-bQP(Q)=a−bQ, efficiency requires

a−bQ∗=MC⇒Q∗=a−MCb.a-bQ^{\*}=MC\quad\Rightarrow\quad Q^{\*}=\frac{a-MC}{b}.a−bQ∗=MC⇒Q∗=ba−MC​.

Compare to single-price monopoly QM=(a−MC)/(2b)Q\_M=(a-MC)/(2b)QM​=(a−MC)/(2b). The first-degree monopolist doubles output relative to single-price monopoly for a linear demand and captures the entire area under the demand curve up to Q∗Q^\*Q∗ as profit.

Numeric example (continuing earlier): a=100,b=1,MC=10a=100, b=1, MC=10a=100,b=1,MC=10 gives

Q∗=100−101=90,P(Q∗)=10.Q^{\*}=\frac{100-10}{1}=90,\qquad P(Q^{\*})=10.Q∗=1100−10​=90,P(Q∗)=10.

Total welfare under first-degree PD equals the competitive-efficient total surplus: producer profit equals the entire sum of areas under the demand curve minus total cost; consumer surplus is zero.

Third-degree PD (observable groups)

Suppose the monopolist serves two segments 1 and 2 with inverse demands

P1(Q1)=a1−b1Q1,P2(Q2)=a2−b2Q2,P\_1(Q\_1)=a\_1-b\_1Q\_1,\quad P\_2(Q\_2)=a\_2-b\_2Q\_2,P1​(Q1​)=a1​−b1​Q1​,P2​(Q2​)=a2​−b2​Q2​,

and common marginal cost MCMCMC. The firm maximizes profit

max⁡Q1,Q2  ∑i=12[Pi(Qi)Qi−MC Qi].\max\_{Q\_1,Q\_2}\;\sum\_{i=1}^2\left[P\_i(Q\_i)Q\_i-MC\,Q\_i\right].Q1​,Q2​max​i=1∑2​[Pi​(Qi​)Qi​−MCQi​].

First-order conditions (see "In Profit Maximization, we learned") set marginal revenue in each market equal to marginal cost:

MRi(Qi)=ai−2biQi=MC,i=1,2.MR\_i(Q\_i)=a\_i-2b\_iQ\_i=MC,\quad i=1,2.MRi​(Qi​)=ai​−2bi​Qi​=MC,i=1,2.

Therefore

Qi=ai−MC2bi,Pi=ai−biQi=ai+MC2.Q\_i=\frac{a\_i-MC}{2b\_i},\qquad P\_i=a\_i-b\_iQ\_i=\frac{a\_i+MC}{2}.Qi​=2bi​ai​−MC​,Pi​=ai​−bi​Qi​=2ai​+MC​.

Concrete numeric example: take a1=80,b1=1a\_1=80,b\_1=1a1​=80,b1​=1 (high-value market), a2=60,b2=1a\_2=60,b\_2=1a2​=60,b2​=1 (low-value market), and MC=10MC=10MC=10. Then

- •Market 1: Q1=(80−10)/2=35Q\_1=(80-10)/2=35Q1​=(80−10)/2=35, P1=(80+10)/2=45P\_1=(80+10)/2=45P1​=(80+10)/2=45.
- •Market 2: Q2=(60−10)/2=25Q\_2=(60-10)/2=25Q2​=(60−10)/2=25, P2=(60+10)/2=35P\_2=(60+10)/2=35P2​=(60+10)/2=35.

Compare single-price monopoly: aggregate demand is P(Q)=aagg−baggQP(Q)=a\_{agg}-b\_{agg}QP(Q)=aagg​−bagg​Q only if markets identical. With different intercepts we find the single optimal price by aggregating demand horizontally at each price. But commonly third-degree PD produces higher profit because the firm charges higher price where willingness-to-pay is higher.

Markup rule and elasticity

A compact result: the Lerner index generalizes to each segment:

Pi−MCPi=−1εi(Pi),\frac{P\_i-MC}{P\_i}=-\frac{1}{\varepsilon\_i(P\_i)},Pi​Pi​−MC​=−εi​(Pi​)1​,

where εi\varepsilon\_iεi​ is the price elasticity of demand in market iii evaluated at PiP\_iPi​. This follows from MRi=Pi(1+1εi)=MCMR\_i=P\_i\left(1+\frac{1}{\varepsilon\_i}\right)=MCMRi​=Pi​(1+εi​1​)=MC. Example numeric: if ε=−2\varepsilon=-2ε=−2 at the chosen price, then the markup is P−MCP=0.5\frac{P-MC}{P}=0.5PP−MC​=0.5. If MC=10MC=10MC=10 and elasticity -2, then P=2MC=20P=2MC=20P=2MC=20.

Welfare comparisons

- •First-degree PD: output is efficient, no deadweight loss; consumer surplus = 0, producer surplus maximized.
- •Third-degree PD: ambiguous effect on total welfare relative to single-price monopoly. If PD raises total output (for example, because single-price sets price driven by aggregate demand which may be high), DWL can fall; but PD can also lower output in some segments relative to single-price and increase DWL.

A useful rule: when demands across segments are differently elastic, segmenting allows the monopolist to price closer to MC in elastic segments (in absolute terms, smaller markup) and farther above MC in inelastic segments; this can raise total quantity if previously demand in elastic segment was suppressed by a high single price. Always compute aggregate output to compare DWL explicitly.

Concrete welfare calculation (from earlier numeric example): compute CS and PS in each market by area formulas and sum. If the segmented output sum exceeds the single-price output, total DWL falls relative to single-price monopoly; otherwise it may rise.

## Core Mechanic 2 — Second-Degree Price Discrimination, Two-Part Tariffs, Bundling and Versioning

Second-degree PD (menues and self-selection)

Second-degree discrimination offers a menu of nonlinear prices so consumers self-select according to private type (willingness to pay). Typical devices: quantity discounts, block pricing, versioning, and two-part tariffs. To analyze, use mechanism design constraints: incentive compatibility (IC) and individual rationality (IR).

Two-part tariffs (TPT)

A two-part tariff is a price schedule consisting of a fixed fee FFF plus a per-unit price ppp: a consumer buying qqq pays T(q)=F+pqT(q)=F+pqT(q)=F+pq. For identical consumers with downward-sloping demand P(q)P(q)P(q) and zero marginal cost, the profit-maximizing two-part tariff sets p=MCp=MCp=MC to get efficient consumption and FFF equal to the consumer surplus at that price to extract surplus entirely. This relies on "In Profit Maximization, we learned" that marginal price should be set by marginal conditions; and "In Consumer Surplus, we learned" how to compute the consumer surplus to set FFF.

Concrete numeric example: single consumer with inverse demand P(q)=100−qP(q)=100-qP(q)=100−q, MC=0MC=0MC=0. Set p=MC=0p=MC=0p=MC=0 so the consumer consumes q∗=100q^{\*}=100q∗=100. Consumer surplus is

CS=12×100×(100−0)=5000.CS=\frac12\times100\times(100-0)=5000.CS=21​×100×(100−0)=5000.

A monopolist sets F=5000F=5000F=5000 and obtains profit Π=5000\Pi=5000Π=5000 (and the per-unit margin is zero). Consumer surplus is zero; total output is efficient. Against heterogeneous consumers, one cannot extract full surplus from all types with a single FFF; the monopolist trades off participation of low-value types.

Example with two discrete types (numerical): suppose two consumers each have inverse demands Pi(q)=ai−qP\_i(q)=a\_i-qPi​(q)=ai​−q, MC=0MC=0MC=0, and each consumer buys individually. Let aH=120,aL=60,b=1a\_H=120,a\_L=60,b=1aH​=120,aL​=60,b=1. If the monopolist sets p=0p=0p=0, then qH=120,qL=60q\_H=120,q\_L=60qH​=120,qL​=60, and their consumer surpluses are CSH=1/2×120×120=7200CS\_H=1/2\times120\times120=7200CSH​=1/2×120×120=7200, CSL=1/2×60×60=1800CS\_L=1/2\times60\times60=1800CSL​=1/2×60×60=1800. To sell to both, the maximum uniform fee is F=1800F=1800F=1800, so profit =2×1800=3600=2\times1800=3600=2×1800=3600. Alternatively, exclude the low type and charge F=7200F=7200F=7200 to the high type, profit =7200=7200=7200. So the firm may prefer to price so that only high-type participates. This illustrates the trade-off in two-part tariffs with heterogeneity.

Versioning and quality differentiation

Versioning sells multiple versions (qualities) of a product at different prices intended to segment consumers by willingness to pay. The canonical analysis (Mussa–Rosen) models consumers by a one-dimensional willingness-to-pay parameter θ\thetaθ and quality qqq. Utility for a type θ\thetaθ buying quality qqq at price ppp is U(θ,q,p)=θ q−pU(\theta,q,p)=\theta\,q-pU(θ,q,p)=θq−p. Cost is C(q)C(q)C(q) (often linear in qqq). The monopolist offers a menu (q,p)(q,p)(q,p) to maximize profits subject to IC and IR constraints. A key result: the high-type gets an efficient quality choice (no distortion) while lower types are allocated a quality distorted downward to loosen IC constraints and extract surplus. This is a direct application of constrained profit maximization taught in "In Profit Maximization, we learned".

Concrete numeric illustration (sketch): Suppose two types: low θL=6\theta\_L=6θL​=6, high θH=10\theta\_H=10θH​=10, cost C(q)=2qC(q)=2qC(q)=2q, proportion of high types λ=0.5\lambda=0.5λ=0.5. The efficient quality for type θ\thetaθ solves θ=MC(q)\theta=MC(q)θ=MC(q) where MC(q)=2MC(q)=2MC(q)=2, so both types would want positive quality if θ>2\theta>2θ>2. But the optimal contract solves a constrained optimization and typically yields qLq\_LqL​ lower than efficient because the monopolist must prevent high types from pretending to be low.

Bundling

Bundling is selling two (or more) goods together at a package price. Bundling is attractive when consumer valuations for goods are negatively correlated or when individual valuations have high variance: bundling reduces the variance of the total valuation across consumers, allowing a single package price to extract more surplus. For independent uniformly distributed valuations, pure bundling can raise profit versus separate pricing. Concrete numeric example: two goods A and B; consumers have independent uniform valuations on [0,100]. If sold separately, profit per good at monopoly price 50 yields expected profit 50\*Pr(v>50) etc. Bundling sets package price near combined mean (100) and captures more of the mass above that price. Always compute expected revenue to compare.

Welfare implications of second-degree devices

- •Two-part tariffs with p=MCp=MCp=MC are efficient in quantity but redistribute surplus from consumers to producers via the lump-sum fee.
- •Versioning and menus generally retain inefficiencies relative to first-best because of distortions imposed to satisfy IC constraints; welfare is often lower than first-best but higher firm profit.
- •Bundling may increase total output for some consumers (those who purchase a bundle but would not have bought each separate good), thus potentially reducing deadweight loss compared to single-good monopolies; effect depends on correlation of valuations.

## Applications and Connections

Real-world applications (concrete examples)

- •Airlines: third-degree PD across observable segments (advance purchase, student, senior fares) and second-degree PD via fare classes (refundable vs non-refundable). Airlines use dynamic versioning (fare buckets) that approximate first-degree PD in rich data environments.

- •Software and cloud services: two-part tariffs (subscription fee + usage), versioning ("basic", "pro", "enterprise"), and bundling (office suites). For example, a SaaS firm often sets p≈MCp\approx MCp≈MC for marginal usage and extracts consumer surplus via subscription fees.

- •Utilities and telecommunications: block tariffs (increasing block pricing, quantity discounts), off-peak/peak pricing (time-based PD), and connection fees (two-part tariffs).

- •Retail coupons and rebates: second-degree PD by letting consumers self-select into lower prices if they search/clip coupons; third-degree PD where discount code reveals group identity.

Policy and regulation implications

Antitrust and consumer protection: regulators are concerned when PD is used to price discriminate against protected groups or to engage in price squeezing and exclusion. Price parity clauses (e.g., hotels and online platforms) restrict a platform’s ability to employ different prices on different channels. First-degree PD often raises distributional concerns despite improving allocative efficiency (it eliminates consumer surplus), so policy weighs equity versus efficiency.

Welfare nuances to remember

- •First-degree PD achieves allocative efficiency but transfers all surplus to the monopolist. If equity matters, regulators may oppose such practices.
- •Third-degree PD can increase or decrease total welfare relative to single-price monopoly — compute outputs to decide.
- •Two-part tariffs can implement efficiency at the margin (p=MCp=MCp=MC) while allowing complete extraction through the lump-sum fee when consumers are identical; with heterogeneity, selective exclusion may occur.

Downstream connections (what this enables you to analyze next)

Mastering price discrimination is essential for advanced topics in industrial organization and mechanism design. Specific forward-looking areas that build directly on this lesson:

- •Mechanism design and optimal auctions: understanding how to design menus under IC/IR is central to optimal auction theory and optimal monopoly regulation.
- •Dynamic pricing and personalized pricing with learning: first-degree PD approximations emerge when firms can learn individual demand functions from data.
- •Ramsey pricing and regulated monopolies: optimizing welfare subject to revenue constraints (regulation) uses the elasticity–markup tradeoffs seen in third-degree PD.
- •Antitrust analysis: merger and exclusion effects sometimes hinge on the ability to price discriminate across products and segments.

Link back to prerequisites

This lesson builds on "In Profit Maximization, we learned" the necessary MR=MC first-order conditions and constrained optimization logic for IC and IR constraints. It also uses "In Consumer Surplus, we learned" how to compute and interpret areas under demand curves to evaluate welfare changes, consumer surplus, and deadweight loss. When doing numerical exercises below, explicitly solve MR=MC and compute CS areas as you learned in those prerequisites.

## Worked Examples (3)

### Third-degree discrimination across two markets

A monopolist serves two separate markets with inverse linear demands P1(Q1)=80-Q1 and P2(Q2)=60-Q2. Marginal cost is MC=10. Compute the profit-maximizing prices and quantities under third-degree discrimination. Then compute the monopoly single-price solution (firm must charge same price in both markets) and compare profits and total output.

1. For third-degree PD, set MR\_i=MC in each market. For linear inverse demand P\_i(Q\_i)=a\_i-Q\_i, marginal revenue MR\_i=a\_i-2Q\_i. (Reference: In Profit Maximization, we learned MR=MC.)
2. Market 1: a1=80, so MR1=80-2Q1. Set MR1=MC => 80-2Q1=10 => Q1=(80-10)/2=35. Price P1=80-35=45.
3. Market 2: a2=60, so MR2=60-2Q2. Set MR2=MC => 60-2Q2=10 => Q2=(60-10)/2=25. Price P2=60-25=35.
4. Compute profits: Profit = (P1-MC)*Q1 + (P2-MC)*Q2 = (45-10)*35 + (35-10)*25 = 35*35 + 25*25 = 1225 + 625 = 1850.
5. Compute total output under PD: Q\_PD = Q1+Q2 = 35 + 25 = 60.
6. Now compute single-price monopoly: aggregate demand at price p is Q(p)=Q1(p)+Q2(p) where Q1(p)=80-p and Q2(p)=60-p, so Q(p)=140 - 2p => invert to get P(Q)=70 - Q/2. Then MR(Q)=70 - Q. Set MR=MC: 70 - Q = 10 => Q\_single = 60. Price P\_single = 70 - 60/2 = 70 - 30 = 40.
7. Single-price profit: (P\_single - MC)*Q\_single = (40-10)*60 = 30\*60 = 1800.
8. Comparison: Third-degree PD profit = 1850 > Single-price profit = 1800. Total outputs are equal (both 60) in this example; welfare differences come from redistribution: PD charges higher price in market 1 (45) and lower in market 2 (35), but aggregate output stays the same here because demands are linear and intercepts sum in this specific way.

**Insight:** This example shows the mechanics: solve MR\_i=MC for each market (use Profit Maximization). It also illustrates that PD need not change aggregate output in every case; relative intercepts and slopes determine whether total output changes (and hence whether DWL changes). Finally, PD increased profit here because the monopolist exploited heterogeneity.

### Two-part tariff with two consumer types

There are two consumers (H and L) each with inverse demand P\_i(q)=a\_i-q, with a\_H=120, a\_L=60, common marginal cost MC=0. The monopolist can offer a two-part tariff (F,p). Find the optimal uniform per-unit price p and fixed fee F if the monopolist wants to sell to both consumers. Determine whether it is ever optimal to exclude the low type.

1. Under a two-part tariff, consumers choose q solving P\_i(q)=p => q\_i=a\_i-p. For MC=0, profit per unit is (p-0), plus fixed fees.
2. As "In Profit Maximization, we learned", if consumers are identical, the profit-maximizing per-unit price is p=MC=0 to achieve efficient quantity. But here types differ. Consider p=0 first: then q\_H=120, q\_L=60.
3. Compute consumer surplus at p=0 for each type: CS\_i = 1/2  *q\_i*  (a\_i - p) = 1/2  *(a\_i)*  (a\_i) = a\_i^2/2. So CS\_H = 120^2/2 = 7200; CS\_L = 60^2/2 = 1800.
4. If the monopolist sets a uniform fee F and p=0 and wants both to participate, F cannot exceed CS\_L=1800. Profit = 2F + p*(q\_H+q\_L) - cost = 2*1800 + 0 = 3600.
5. Consider excluding the low type: set p=0 and charge F=7200 to the high type only. Profit = 7200, which is greater than 3600. So exclusion dominates selling to both at p=0.
6. Consider alternatives with p>0: raising p reduces per-unit consumption but allows higher fees; but with linear demands and MC=0, the usual result is that for heterogeneous consumers a monopolist may prefer to set p>MC to screen types or exclude some. Checking p=30: q\_H=90,q\_L=30; compute CSs and max feasible F to include both, then compute profit and compare (exercise). In our numbers, exclusion of the low type at p=0 dominates selling to both.
7. Conclusion: the monopolist prefers to target the high-type alone with a high fixed fee rather than sell to both at p=MC in order to extract surplus when types are discrete and sufficiently heterogeneous.

**Insight:** This example demonstrates how two-part tariffs interact with heterogeneity: while p=MC is efficient in quantity, lump-sum extraction and participation constraints can lead the firm to exclude low-value consumers to maximize profit. It shows the direct application of consumer surplus calculations from "In Consumer Surplus, we learned".

### Versioning: Two types and incentive constraints (Mussa–Rosen sketch)

A monopolist sells a product that can be set to quality q at marginal cost c per unit of quality (cost C(q)=cq). There are two consumer types with utilities U=θq-p: type L has θ\_L=6, type H has θ\_H=10. Proportion of H is 1/2. c=2. Design qualities and prices (q\_L,p\_L) and (q\_H,p\_H) to maximize profit subject to incentive compatibility and individual rationality. Show qualitative results and compute the optimal q\_L and q\_H in the binding-IC case.

1. Write the firm’s expected profit as 0.5[(p\_H - c q\_H) + (p\_L - c q\_L)]. Constraints: (i) IR for low: θ\_L q\_L - p\_L >= 0; (ii) IR for high: θ\_H q\_H - p\_H >= 0; (iii) IC high: θ\_H q\_H - p\_H >= θ\_H q\_L - p\_L; (iv) IC low: θ\_L q\_L - p\_L >= θ\_L q\_H - p\_H. Typically IC low is slack; main binding constraints are IC high and IR low.
2. Standard trick: eliminate prices using the binding constraints. Suppose IC high binds and IR low binds. From IR low: p\_L = θ\_L q\_L. From IC high binding: θ\_H q\_H - p\_H = θ\_H q\_L - p\_L => p\_H = θ\_H q\_H - θ\_H q\_L + p\_L = θ\_H(q\_H - q\_L) + θ\_L q\_L = θ\_H q\_H - (θ\_H - θ\_L) q\_L.
3. Substitute p\_H and p\_L into profit: π = 0.5[ p\_H - c q\_H + p\_L - c q\_L ] = 0.5[ θ\_H q\_H - (θ\_H - θ\_L) q\_L - c q\_H + θ\_L q\_L - c q\_L ] = 0.5[ (θ\_H - c) q\_H + ( - (θ\_H - θ\_L) + θ\_L - c ) q\_L ]
4. Simplify coefficient of q\_L: - (θ\_H - θ\_L) + θ\_L - c = -θ\_H + 2θ\_L - c. Plug numbers θ\_H=10, θ\_L=6, c=2 gives coefficient for q\_H: (10-2)=8, coefficient for q\_L: -10 + 12 - 2 = 0. So profit simplifies to π = 0.5*(8 q\_H + 0*q\_L) = 4 q\_H. Thus profit depends only on q\_H when the two constraints bind with these parameters.
5. Optimal q\_H maximizes firm’s profit subject to IC/IR manipulation: since no direct cost of increasing q\_H beyond constraints except marginal cost enters, set derivative of profit w.r.t q\_H equal to zero or check inside constraints. However, the efficient q\_H solves θ\_H = c => 10=2, which is false; so we choose q\_H as high as feasible given consumer IR: p\_H = θ\_H q\_H - (θ\_H - θ\_L) q\_L; but q\_L determined by IR low p\_L = θ\_L q\_L and q\_L must be nonnegative. With our numerical coefficient for q\_L zero, the firm will set q\_L at minimal viable level (often zero) and maximize q\_H subject to IC and IR that keep high type participating.
6. A more careful continuous optimization (beyond sketch) yields the standard Mussa–Rosen result: q\_H is efficient (or nearly so) and q\_L is downward distorted relative to the first-best. Numerically, we find q\_L set low (possibly zero) and q\_H set where marginal willingness-to-pay equals marginal cost adjusted for information rents. The key qualitative takeaway is distortion downwards for low type.

**Insight:** This worked example sketches how incentive compatibility and individual rationality create distortions in versioning. Even with only two types, the low-quality product is typically deliberately starved of quality to prevent high-type mimicry; this is a central constrained-optimization result building on "In Profit Maximization, we learned" about constrained optima.

## Key Takeaways

- ✓

  Price discrimination requires (i) market power, (ii) ability to segment or signal willingness to pay, and (iii) limited arbitrage.
- ✓

  First-degree PD achieves allocative efficiency (P=MC) and extracts all consumer surplus; it increases total output relative to single-price monopoly.
- ✓

  Third-degree PD sets MR\_i=MC in each observable segment and yields markups according to the Lerner rule: (P-MC)/P=-1/ε; welfare effects relative to single-price monopoly are ambiguous and depend on output changes across segments.
- ✓

  Second-degree PD (menus, two-part tariffs, versioning) uses self-selection; two-part tariffs can implement efficiency at the margin (p=MC) but lump-sum fees redistribute surplus; heterogeneity can lead to exclusion.
- ✓

  Versioning solves a constrained optimization (IC and IR): high types often receive nearly efficient quality, low types are distorted downward to prevent imitation.
- ✓

  Bundling can increase a monopolist's revenue by reducing valuation variance (helpful when valuations are negatively correlated or have high variance), but its welfare effects depend on how it changes participation and total quantity.
- ✓

  Always compute MR=MC and consumer surplus (areas) explicitly — the prerequisites "In Profit Maximization, we learned" and "In Consumer Surplus, we learned" are the operational basis for all calculations.

## Common Mistakes

- ✗

  Confusing degrees: treating second-degree mechanisms (menus) as equivalent to third-degree segmentation. Why wrong: second-degree relies on self-selection under private information and requires IC constraints; third-degree uses observed group identifiers and sets simple group prices.
- ✗

  Assuming price discrimination always reduces welfare. Why wrong: first-degree PD is allocatively efficient and can eliminate deadweight loss; third-degree PD can increase output in some segments and reduce DWL relative to single-price monopoly.
- ✗

  Forgetting individual rationality in two-part tariffs and versioning. Why wrong: lump-sum fees cannot exceed a consumer's surplus at the chosen marginal price without causing exit, so ignoring IR yields infeasible contracts.
- ✗

  Setting per-unit price p>MC automatically in two-part tariffs. Why wrong: for identical consumers p=MC is profit-maximizing in quantity terms; p>MC can be used for screening heterogeneous types but trades off efficiency for extractable surplus.

## Practice

easy

Easy — Third-degree pricing: A monopolist serves two markets with demands Q1=100-2P1 and Q2=80-4P2. Marginal cost MC=10. Find the profit-maximizing prices P1 and P2 under third-degree discrimination.

**Hint:** Convert to inverse demand P\_i(Q\_i), compute MR\_i and set MR\_i=MC for each market.

Show solution

Inverse demands: P1=50-0.5Q1, P2=20-0.25Q2. MR1=50-Q1, MR2=20-0.5Q2. Set MR1=MC => 50-Q1=10 => Q1=40 => P1=50-0.5*40=30. MR2=MC => 20-0.5Q2=10 => Q2=20 => P2=20-0.25*20=15.

medium

Medium — Two-part tariff with three consumers: Three consumers have willingness-to-pay intercepts a={120,80,40} with identical unit slope b=1 so each has inverse demand P\_i(q)=a\_i - q. MC=0. The monopolist can set (p,F) uniform across consumers. What p and F maximize profit if the firm wants to sell to the two highest types but exclude the lowest? Compute resulting profit.

**Hint:** To sell to types with a\_i, set p so that each chosen type buys q\_i=a\_i - p. Fee F is at most the smaller consumer surplus of the two targeted types. Consider p=MC=0 as candidate and also p>0 to screen the low type.

Show solution

If p=0, q\_1=120,q\_2=80, CSs are 7200 and 3200; to sell to both F≤3200 so profit=2*3200=6400. If choose p=20, q\_1=100,q\_2=60, CSs: CS1=0.5*100*100=5000, CS2=0.5*60*60=1800 => F≤1800 => profit fees=3600 plus per-unit revenue p*(q1+q2)=20\*160=3200 => total=6800. Thus p=20, F=1800 yields profit 6800 > 6400. So optimal picks p>0 to reduce low-type surplus and extract more from both types.

hard

Hard — Versioning with continuum of types: Consumers have type θ uniformly distributed on [0,1]. Utility from quality q at price p is U=θq - p. Cost of quality per consumer is C(q)=k q where k>0. The seller can offer a continuum menu (q(θ),p(θ)). Derive the first-order condition for the optimal quality schedule q(θ) using the Mirrlees approach (virtual surplus), show whether quality is distorted for low types, and state the condition for no distortion.

**Hint:** Use the revelation principle to restrict to truthful direct mechanisms. The seller’s expected profit is integral of (p(θ)-C(q(θ)))f(θ)dθ subject to IC (which implies envelope theorem: U'(θ)=q(θ)) and IR. Use integration by parts to write profit as expected virtual surplus: maximize ∫[θ q(θ) - C(q(θ)) - (1-F(θ))/f(θ) q(θ)] f(θ)dθ.

Show solution

Under truth-telling, the envelope theorem yields consumer utility U(θ)=U(0)+∫\_0^θ q(t) dt. With U(0) pinned by IR, the seller sets prices from p(θ)=θ q(θ) - U(θ). Expected profit is ∫[p(θ)-C(q(θ))] f(θ)dθ = ∫[θ q(θ) - U(θ) - C(q(θ))] f(θ)dθ. Integrating by parts and simplifying yields profit expressed as ∫[ (θ - (1-F(θ))/f(θ)) q(θ) - C(q(θ)) ] f(θ) dθ + constant. The term φ(θ)=θ - (1-F(θ))/f(θ) is the virtual valuation. The pointwise first-order condition for q(θ) is φ(θ) = C'(q(θ)). For uniform [0,1], f=1, F=θ so φ(θ)=θ - (1-θ)/1 = 2θ -1. So q(θ) satisfies 2θ -1 = k => q(θ) = (2θ -1)/k if positive, zero otherwise. Thus low types with θ < 1/2 produce negative φ(θ) and hence q(θ)=0 (full distortion to zero); types above threshold receive positive quality increasing in θ. No distortion (i.e., q(θ) equal to first-best where θ=C'(q) ) occurs only if φ(θ)=θ for all θ which requires (1-F)/f = 0, not true for a continuous distribution. So distortion is generic: low types receive lower quality than first best; only when the informational rent term (1-F)/f vanishes, e.g. degenerate distribution, would there be no distortion.

## Connections

This lesson builds directly on two prerequisites. "In Profit Maximization, we learned" to set marginal revenue equal to marginal cost and to solve constrained optimization problems; those tools are used repeatedly (MR=MC in each segment for third-degree, FOC derivations for two-part tariffs and menus, and constrained maximization with IC/IR in versioning). "In Consumer Surplus, we learned" how to compute areas under demand curves and evaluate deadweight loss and surplus transfers; computing CS is essential for setting lump-sum fees and evaluating welfare impacts. Looking forward, mastering price discrimination enables correct reasoning in mechanism design (optimal auctions and menus), dynamic/personalized pricing (where firms approach first-degree PD via data), Ramsey pricing and regulated monopoly pricing (elasticity–markup tradeoffs), and antitrust analysis of discriminatory pricing practices. In short: price discrimination is the bridge from static monopoly pricing (Profit Maximization) and welfare accounting (Consumer Surplus) to optimal mechanism design, regulatory economics, and modern data-driven pricing strategies.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
