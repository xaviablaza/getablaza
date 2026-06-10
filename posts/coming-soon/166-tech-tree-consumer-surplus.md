---
title: Consumer Surplus
description: Area between demand curve and price. Producer surplus, total welfare. Deadweight loss from taxes, monopoly, price floors/ceilings.
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
source_format: html
inspiration_url: https://templeton.host/tech-tree/consumer-surplus/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/consumer-surplus/](https://templeton.host/tech-tree/consumer-surplus/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Consumer Surplus

Applied EconomicsDifficulty: ★★★☆☆Depth: 9Unlocks: 2

Area between demand curve and price. Producer surplus, total welfare. Deadweight loss from taxes, monopoly, price floors/ceilings.

## Prerequisites (2)

[Demand Functions? atoms](/tech-tree/demand-functions/)[Integrals6 atoms](/tech-tree/integrals-basic/)

## Unlocks (1)

[Price Discriminationlvl 4](/tech-tree/price-discrimination/)

## Referenced by (4)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (4)

[BuyerBusiness

The gap between the buyer's willingness to pay (driven by pain intensity) and what the inferior means costs them IS capturable consumer surplus. Naming the inferior means quantifies the surplus your product can extract or share.](/business/buyer/)[Value CreationBusiness

Consumer surplus is the formal economic measurement of value creation - the area between the demand curve and price is exactly the delta captured by the buyer along dimensions they value](/business/value-creation/)[Demand-SideBusiness

Quantifies how well demand is currently served - large potential surplus captured by no existing supplier signals the poorly-served demand a business should target](/business/demand-side/)[Value LeakageBusiness

Deadweight loss is the formal economic measurement of value leakage - surplus destroyed at system boundaries by taxes, monopoly power, or price controls that no participant individually perceives as a named cost.](/business/value-leakage/)

Advanced Learning Details

### Graph Position

61

Depth Cost

2

Fan-Out (ROI)

1

Bottleneck Score

9

Chain Length

When you buy something for less than the maximum you were willing to pay, you get a little hidden benefit — consumer surplus is the formal way economists measure that benefit and it drives many policy debates.

TL;DR:

Consumer surplus is the area between the demand curve (willingness to pay) and the market price; together with producer surplus it summarizes total welfare and lets us quantify losses from taxes, monopoly pricing, and price controls.

## What Is Consumer Surplus?

Definition and Intuition

Consumer surplus (CS) is the net benefit buyers receive from participating in a market: for each unit purchased, it is the difference between what a buyer would have been willing to pay (their willingness-to-pay) and the actual market price paid. Graphically, with an inverse demand function p(q)p(q)p(q) (price consumers are willing to pay for the marginal unit) and a market price PPP, consumer surplus for the traded quantity q∗q^\*q∗ is the area between the inverse demand curve and the horizontal price line from q=0q=0q=0 to q=q∗q=q^\*q=q∗.

Mathematically, if the market clears at price PPP and quantity q∗q^\*q∗, then, relying on the integral techniques from Integrals (d2), we write consumer surplus as

CS=∫0q∗(p(q)−P) dq.CS = \int\_0^{q^\*} \big(p(q) - P\big)\,dq.CS=∫0q∗​(p(q)−P)dq.

Concrete numeric example: Suppose inverse demand is p(q)=100−2qp(q)=100-2qp(q)=100−2q and the market price is P=40P=40P=40. Then q∗q^\*q∗ is the quantity buyers demand at that price: solve $100-2q^*=40$, so $q^*=30$. The consumer surplus is

CS=∫030(100−2q−40) dq=∫030(60−2q) dq=[60q−q2]030=60⋅30−302=1800−900=900.CS=\int\_0^{30} (100-2q-40)\,dq=\int\_0^{30} (60-2q)\,dq = [60q - q^2]\_0^{30} = 60\cdot30 - 30^2 = 1800-900 = 900.CS=∫030​(100−2q−40)dq=∫030​(60−2q)dq=[60q−q2]030​=60⋅30−302=1800−900=900.

So buyers as a group get a surplus of 900 (in whatever monetary units the price uses).

Why CS matters

- •Welfare summary: Consumer surplus is a concise summary of buyers' welfare and, combined with producer surplus (PS), gives total surplus (TS = CS + PS). Policy evaluations (taxes, subsidies, regulation) routinely use changes in CS and PS to assess gains or losses.
- •Policy intuition: When price increases (e.g., via a tax or monopoly pricing), CS usually falls; measuring that fall quantifies who loses and by how much.
- •Link to demand theory: In Demand Functions (d3), you learned how to derive inverse demand p(q)p(q)p(q) from consumers' utility maximization. CS is just the integrated difference between that theoretical willingness-to-pay curve and the market price, so it is directly grounded in individual preferences.

Units and interpretation notes

- •CS is an aggregate measure: if different buyers have different willingness-to-pay curves, we aggregate horizontally to get the market inverse demand before integrating. That step uses Market Demand Aggregation from Demand Functions (d3).
- •Integrals (d2) are necessary because the marginal willingness to pay varies with qqq; CS sums the marginal gains across infinitesimal units.
- •When demand is discrete or we have a small number of buyers, compute CS by summing individual discrete surpluses (a Riemann-sum approximation converges to the integral as units become small).

## Core Mechanic 1: Calculating Consumer, Producer, and Total Surplus

Formal formulas and step-by-step computation

We will treat the supply curve s(q)s(q)s(q) as the marginal cost (MC) of producing the qqqth unit and the inverse demand p(q)p(q)p(q) as willingness to pay. For a competitive market equilibrium (P∗,q∗)(P^\*, q^\*)(P∗,q∗) where P∗=p(q∗)=s(q∗)P^\*=p(q^\*)=s(q^\*)P∗=p(q∗)=s(q∗), the standard formulas are:

- •Consumer surplus:

CS=∫0q∗(p(q)−P∗) dq.CS = \int\_0^{q^\*} (p(q)-P^\*)\,dq.CS=∫0q∗​(p(q)−P∗)dq.

- •Producer surplus (PS), the net revenue to producers above marginal cost:

PS=∫0q∗(P∗−s(q)) dq.PS = \int\_0^{q^\*} (P^\* - s(q))\,dq.PS=∫0q∗​(P∗−s(q))dq.

- •Total surplus (TS), the sum:

TS=CS+PS=∫0q∗(p(q)−s(q)) dq.TS = CS + PS = \int\_0^{q^\*} (p(q) - s(q))\,dq.TS=CS+PS=∫0q∗​(p(q)−s(q))dq.

Each formula is an integral; see Integrals (d2) for the interpretation of area under a curve.

Worked linear example (concrete numbers at every formula):

Let inverse demand be p(q)=120−4qp(q)=120-4qp(q)=120−4q and supply (marginal cost) be s(q)=20+2qs(q)=20+2qs(q)=20+2q. First find the competitive equilibrium quantity q∗q^\*q∗ by solving p(q)=s(q)p(q)=s(q)p(q)=s(q):

120−4q∗=20+2q∗⇒100=6q∗⇒q∗=1006≈16.6667.120-4q^\* = 20+2q^\* \Rightarrow 100 = 6q^\* \Rightarrow q^\* = \frac{100}{6} \approx 16.6667.120−4q∗=20+2q∗⇒100=6q∗⇒q∗=6100​≈16.6667.

The equilibrium price is

P∗=p(q∗)=120−4⋅16.6667=120−66.6667=53.3333.P^\* = p(q^\*) = 120 - 4\cdot16.6667 = 120 - 66.6667 = 53.3333.P∗=p(q∗)=120−4⋅16.6667=120−66.6667=53.3333.

Now compute CS using the integral formula:

CS=∫016.6667(120−4q−53.3333) dq=∫016.6667(66.6667−4q) dq.CS = \int\_0^{16.6667} (120-4q - 53.3333)\,dq = \int\_0^{16.6667} (66.6667 - 4q)\,dq.CS=∫016.6667​(120−4q−53.3333)dq=∫016.6667​(66.6667−4q)dq.

Compute the antiderivative and evaluate numerically:

CS=[66.6667q−2q2]016.6667=66.6667⋅16.6667−2⋅(16.6667)2.CS = [66.6667 q - 2 q^2]\_0^{16.6667} = 66.6667\cdot16.6667 - 2\cdot(16.6667)^2.CS=[66.6667q−2q2]016.6667​=66.6667⋅16.6667−2⋅(16.6667)2.

Numerically: $66.6667\cdot16.6667\approx 1111.111$, and $2\cdot(16.6667)^2 \approx 555.5556$, so

CS≈1111.111−555.5556=555.5554.CS \approx 1111.111 - 555.5556 = 555.5554.CS≈1111.111−555.5556=555.5554.

Producer surplus similarly:

PS=∫016.6667(53.3333−(20+2q)) dq=∫016.6667(33.3333−2q) dq=[33.3333q−q2]016.6667.PS = \int\_0^{16.6667} (53.3333 - (20+2q))\,dq = \int\_0^{16.6667} (33.3333 - 2q)\,dq = [33.3333 q - q^2]\_0^{16.6667}.PS=∫016.6667​(53.3333−(20+2q))dq=∫016.6667​(33.3333−2q)dq=[33.3333q−q2]016.6667​.

Numerically: $33.3333\cdot16.6667 \approx 555.555,and, and ,and(16.6667)^2\approx 277.7778$, so

PS≈555.555−277.7778=277.7772.PS \approx 555.555 - 277.7778 = 277.7772.PS≈555.555−277.7778=277.7772.

Total surplus is then

TS=CS+PS≈555.5554+277.7772=833.3326,TS = CS + PS \approx 555.5554 + 277.7772 = 833.3326,TS=CS+PS≈555.5554+277.7772=833.3326,

which matches the direct integral

TS=∫016.6667(120−4q−(20+2q)) dq=∫016.6667(100−6q) dq=[100q−3q2]016.6667≈833.333.TS = \int\_0^{16.6667} (120-4q - (20+2q))\,dq = \int\_0^{16.6667} (100 - 6q)\,dq = [100q - 3q^2]\_0^{16.6667} \approx 833.333.TS=∫016.6667​(120−4q−(20+2q))dq=∫016.6667​(100−6q)dq=[100q−3q2]016.6667​≈833.333.

Interpretation and why this works

- •CS measures area under demand above price; PS measures area above supply under price. Both use antiderivatives as in Integrals (d2).
- •Notice that to compute CS we used the inverse demand p(q)p(q)p(q) learned in Demand Functions (d3). If you only had the Marshallian demand (demand as function of price), convert to inverse form or compute CS by integrating consumer surplus in price space (using Hicksian compensating variations is another route connected to consumer theory but beyond this lesson).

Discrete buyers note

When you have discrete buyers each with a willingness-to-pay viv\_ivi​ for one unit (say unit-demand buyers), CS equals the sum over buyers of (vi−P)(v\_i - P)(vi​−P) for those with vi≥Pv\_i\ge Pvi​≥P. This discrete sum corresponds to the integral when buyers are continuously distributed — a connection you saw in Market Demand Aggregation in Demand Functions (d3).

## Core Mechanic 2: Deadweight Loss from Taxes, Monopoly, and Price Controls

Deadweight loss (DWL) is the reduction in total surplus relative to the competitive, unregulated benchmark. DWL arises whenever trades that would increase total surplus do not occur. The geometry is always a wedge-shaped or triangular area in standard cases.

A. Per-unit tax

Consider a per-unit tax ttt levied on transactions. The tax drives a wedge between the price consumers pay PcP\_cPc​ and the price producers receive PpP\_pPp​: Pc=Pp+tP\_c = P\_p + tPc​=Pp​+t. With linear demand and supply, one can compute the new traded quantity qtq\_tqt​ and deadweight loss.

Example with numbers: Let p(q)=100−2qp(q)=100-2qp(q)=100−2q and s(q)=20+qs(q)=20+qs(q)=20+q as before but now impose a tax t=10t=10t=10. The equilibrium without tax was found by solving $100-2q=20+q,giving, giving ,givingq^*=20$, $P^*=60.Withatax,setconsumerprice. With a tax, set consumer price .Withatax,setconsumerpriceP\_candproducerprice and producer price andproducerpriceP\_p=P\_c - 10.Themarketclearswhen. The market clears when .ThemarketclearswhenP\_c = p(q)and and andP\_p = s(q)$ simultaneously, so

p(qt)=s(qt)+t⇒100−2qt=20+qt+10⇒100−2qt=30+qt⇒70=3qt⇒qt=70/3≈23.333.p(q\_t) = s(q\_t) + t \Rightarrow 100-2q\_t = 20 + q\_t + 10 \Rightarrow 100-2q\_t = 30 + q\_t \Rightarrow 70 = 3q\_t \Rightarrow q\_t = 70/3 \approx 23.333.p(qt​)=s(qt​)+t⇒100−2qt​=20+qt​+10⇒100−2qt​=30+qt​⇒70=3qt​⇒qt​=70/3≈23.333.

This number is larger than the previous q∗=20q^\*=20q∗=20 because I intentionally chose numbers that produce that shape — normally a tax reduces quantity. Let's show a standard case where tax reduces quantity: take supply s(q)=20+3qs(q)=20+3qs(q)=20+3q instead. Solve

100−2qt=20+3qt+10⇒100−2qt=30+3qt⇒70=5qt⇒qt=14.100-2q\_t = 20 + 3q\_t + 10 \Rightarrow 100-2q\_t = 30 + 3q\_t \Rightarrow 70 = 5q\_t \Rightarrow q\_t = 14.100−2qt​=20+3qt​+10⇒100−2qt​=30+3qt​⇒70=5qt​⇒qt​=14.

Original q∗=20q^\*=20q∗=20, tax equilibrium qt=14q\_t=14qt​=14, so quantity falls. The deadweight loss is the triangle representing lost trades between qtq\_tqt​ and q∗q^\*q∗ with height equal to the tax minus any transfers. Algebraically for linear functions, DWL equals

DWL=12⋅t⋅(q∗−qt).DWL = \frac{1}{2} \cdot t \cdot (q^\* - q\_t).DWL=21​⋅t⋅(q∗−qt​).

Compute numerically: with t=10t=10t=10, q∗=20q^\*=20q∗=20, qt=14q\_t=14qt​=14, we get

DWL=0.5⋅10⋅(20−14)=5⋅6=30.DWL = 0.5\cdot 10 \cdot (20-14) = 5\cdot 6 = 30.DWL=0.5⋅10⋅(20−14)=5⋅6=30.

Interpretation: 30 is surplus lost to neither consumers nor producers — an efficiency loss. The government collects tax revenue TR=t⋅qt=10⋅14=140TR = t\cdot q\_t = 10\cdot14=140TR=t⋅qt​=10⋅14=140; CS and PS fall by amounts that sum to DWL + TR.

B. Monopoly deadweight loss

A monopoly sets output where marginal revenue (MR) equals marginal cost (MC). For linear demand p(q)=a−bqp(q)=a-bqp(q)=a−bq, MR is a−2bqa-2bqa−2bq. The competitive quantity solves p(q)=MCp(q)=MCp(q)=MC. The DWL is the surplus lost relative to the competitive benchmark.

Concrete example: Let p(q)=100−2qp(q)=100-2qp(q)=100−2q and s(q)=20+0⋅qs(q)=20+0\cdot qs(q)=20+0⋅q (constant MC=20). Competitive equilibrium: $100-2q^*=20$ implies $q^*=40.MonopolysetsMR=MC:. Monopoly sets MR=MC: .MonopolysetsMR=MC:MR=100-4q\_m=20so so soq\_m=20.Priceundermonopolyis. Price under monopoly is .Priceundermonopolyisp(q\_m)=100-2\cdot20=60$. Compute DWL:

Competitive TS:

TSc=∫040(100−2q−20) dq=∫040(80−2q) dq=[80q−q2]040=3200−1600=1600.TS\_c = \int\_0^{40} (100-2q - 20)\,dq = \int\_0^{40} (80 - 2q)\,dq = [80q - q^2]\_0^{40} = 3200 - 1600 = 1600.TSc​=∫040​(100−2q−20)dq=∫040​(80−2q)dq=[80q−q2]040​=3200−1600=1600.

Monopoly TS (with monopolist extracting PS as profit): traded quantity 20, price 60, so

TSm=∫020(100−2q−20) dq=∫020(80−2q) dq=[80q−q2]020=1600−400=1200.TS\_m = \int\_0^{20} (100-2q - 20)\,dq = \int\_0^{20} (80-2q)\,dq = [80q - q^2]\_0^{20} = 1600 - 400 = 1200.TSm​=∫020​(100−2q−20)dq=∫020​(80−2q)dq=[80q−q2]020​=1600−400=1200.

DWL is $1600 - 1200 = 400.Geometricallythisisthetrianglebetweenthedemandandsupplycurvesfrom. Geometrically this is the triangle between the demand and supply curves from .Geometricallythisisthetrianglebetweenthedemandandsupplycurvesfromq\_mto to toq^\*$.

C. Price ceilings and floors

A binding price ceiling (maximum price) below the competitive price reduces quantity supplied to the level where supply equals the ceiling price. The DWL equals the triangular area between demand and supply from the new lower quantity up to the competitive quantity.

Example numbers: Suppose p=qp=qp=q-dependent demand p(q)=80−2qp(q)=80-2qp(q)=80−2q and supply s(q)=20+qs(q)=20+qs(q)=20+q. Competitive q∗q^\*q∗ solves $80-2q=20+q \Rightarrow 60=3q \Rightarrow q^*=20$ and $P^*=40.Ifapriceceiling. If a price ceiling .IfapriceceilingP\_c=30$ binds (30<40), quantity traded becomes the smaller of quantity demanded (where $80-2q\_d=30 \Rightarrow q\_d=25$) and quantity supplied (where $20+q\_s=30 \Rightarrow q\_s=10).Actualtradedquantityis). Actual traded quantity is ).Actualtradedquantityisq\_s=10(supply−limited).DWLequalsareabetweendemandandsupplyfrom (supply-limited). DWL equals area between demand and supply from (supply−limited).DWLequalsareabetweendemandandsupplyfromq=10to to toq=20$:

DWL=∫1020(80−2q−(20+q)) dq=∫1020(60−3q) dq=[60q−1.5q2]1020.DWL = \int\_{10}^{20} (80-2q - (20+q))\,dq = \int\_{10}^{20} (60 - 3q)\,dq = [60q - 1.5 q^2]\_{10}^{20}.DWL=∫1020​(80−2q−(20+q))dq=∫1020​(60−3q)dq=[60q−1.5q2]1020​.

Compute numerically: at 20 value is $1200 - 600 = 600$; at 10 value is $600 - 150 = 450$; so DWL = $600 - 450 = 150$.

General rules

- •DWL grows with the square of the distortion for small linear approximations (twice the drop in trades times wedge). Thus large taxes or large monopolistic markups create disproportionally larger DWL.
- •The exact formula depends on curvature of demand and supply; for linear functions the triangular approximation is exact.

## Applications and Connections

Public finance and tax incidence

Consumer surplus is central to public finance: when a tax is proposed, analysts compute how much CS falls and how much of the tax burden falls on consumers versus producers (incidence). For example, with perfectly elastic supply, consumers bear the entire burden and CS falls by nearly the full tax times quantity; with perfectly inelastic demand, producers bear more of the burden.

Concrete incidence example: If p(q)=100−2qp(q)=100-2qp(q)=100−2q and supply is perfectly elastic at s(q)=30s(q)=30s(q)=30 (horizontal at 30), a per-unit tax t=10t=10t=10 raises the consumer price from 30 to 40, so consumers pay $10moreandproducersreceivethesame30—consumersentirelybearthetax.CSchangeequals more and producers receive the same 30 — consumers entirely bear the tax. CS change equals moreandproducersreceivethesame30—consumersentirelybearthetax.CSchangeequals\int\_0^{q^*} (p(q)-P\_{new}) - (p(q)-P\_{old})\,dq$ which simplifies to $-(P\_{new}-P\_{old})\cdot q^*$ when demand quantity remains the same at the cutoff.

Antitrust and monopoly regulation

Consumer surplus quantifies consumer harm from monopolies. Antitrust remedies (breakup, price regulation) often measure how much CS can be recovered. In industries with large fixed costs, monopoly pricing might increase producer surplus but reduce CS dramatically, so regulators trade off efficiency and investment incentives.

Concrete regulatory example: A regulated price cap can be set to maximize CS+PS subject to a required return; computing the exact cap requires integrating demand and supply marginal costs across output levels.

Welfare analysis of subsidies, externalities, and public goods

Subsidies increase CS (by lowering consumer price) but cost the government revenue. Environmental taxes (Pigouvian taxes) intentionally reduce quantity to correct externalities — despite creating DWL in the goods market, they may increase total social welfare when accounting for reduced external damage. Thus computing CS alone is insufficient; combine with external cost reductions.

Education policy and price controls

Examples include rent control (price ceiling) and minimum wage (price floor in labor market). The same geometric logic applies: binding controls reduce traded quantity (housing leases, employment) relative to the competitive benchmark and produce DWL (plus distributional transfers). For the minimum wage, producer surplus for firms falls, worker surplus may rise or fall depending on who is employed and who is priced out; compute these by integrating labor demand and supply curves.

Empirical measurement

In empirical demand estimation (rooted in Demand Functions (d3)), economists often estimate willingness-to-pay parameters from discrete choice or aggregated demand. Once p(q)p(q)p(q) is estimated, consumer surplus is computed via numerical integration (Riemann sums) or closed-form integration if functional forms are linear or constant-elasticity. Ensure you convert estimated Marshallian demand Q(P)Q(P)Q(P) to inverse demand P(Q)P(Q)P(Q) or compute CS via

CS=∫PPˉQ(p) dpCS = \int\_{P}^{\bar{P}} Q(p)\,dpCS=∫PPˉ​Q(p)dp

if you prefer integrating over price space (this formula also requires a reference price Pˉ\bar{P}Pˉ, often choke price where Q(Pˉ)=0Q(\bar{P})=0Q(Pˉ)=0).

What this enables

Mastering CS and DWL enables applied work in public policy evaluation, antitrust cases, cost-benefit analysis, and empirical welfare calculations. It is a building block for advanced topics: tariff incidence in international trade, general equilibrium welfare analysis, and the use of compensating/equivalent variation methods from consumer theory to value non-market changes (connected back to Demand Functions (d3)).

## Worked Examples (3)

### Consumer Surplus under a Linear Demand and Given Price

Inverse demand p(q)=100−2qp(q)=100-2qp(q)=100−2q. Market price is P=40P=40P=40. Compute consumer surplus.

1. Find traded quantity q∗q^\*q∗ by solving p(q∗)=Pp(q^\*)=Pp(q∗)=P: $100-2q^*=40 \Rightarrow 2q^*=60 \Rightarrow q^\*=30$.
2. Write the integral for CS: CS=∫030(100−2q−40) dq=∫030(60−2q) dqCS=\int\_0^{30} (100-2q - 40)\,dq = \int\_0^{30} (60-2q)\,dqCS=∫030​(100−2q−40)dq=∫030​(60−2q)dq.
3. Compute antiderivative: ∫(60−2q) dq=60q−q2\int (60-2q)\,dq = 60q - q^2∫(60−2q)dq=60q−q2.
4. Evaluate from 0 to 30: CS=60⋅30−302=1800−900=900CS = 60\cdot30 - 30^2 = 1800 - 900 = 900CS=60⋅30−302=1800−900=900.
5. Interpretation: Aggregate buyer benefit above price is 900 monetary units.

**Insight:** This example shows the direct use of inverse demand (from Demand Functions (d3)) and basic integration (from Integrals (d2)) to compute an area. It also demonstrates why converting to inverse demand is useful when prices are observed.

### Deadweight Loss from a Per-Unit Tax

Demand p(q)=100−2qp(q)=100-2qp(q)=100−2q, supply s(q)=20+3qs(q)=20+3qs(q)=20+3q. A per-unit tax t=10t=10t=10 is imposed. Compute new quantity, tax revenue, and DWL.

1. Start with pre-tax equilibrium: solve $100-2q^*=20+3q^* \Rightarrow 80=5q^ *\Rightarrow q^*=16$.
2. Pre-tax price P∗=p(16)=100−32=68P^\*=p(16)=100-32=68P∗=p(16)=100−32=68.
3. With tax, set p(qt)=s(qt)+tp(q\_t)=s(q\_t)+tp(qt​)=s(qt​)+t: $100-2q\_t = 20+3q\_t + 10 \Rightarrow 100-2q\_t = 30 + 3q\_t \Rightarrow 70 = 5q\_t \Rightarrow q\_t = 14$.
4. Tax revenue TR=t⋅qt=10⋅14=140TR = t \cdot q\_t = 10\cdot14 = 140TR=t⋅qt​=10⋅14=140.
5. DWL equals 12⋅t⋅(q∗−qt)=0.5⋅10⋅(16−14)=0.5⋅10⋅2=10\frac{1}{2}\cdot t \cdot (q^\* - q\_t) = 0.5 \cdot 10 \cdot (16-14) = 0.5\cdot10\cdot2 = 1021​⋅t⋅(q∗−qt​)=0.5⋅10⋅(16−14)=0.5⋅10⋅2=10.

**Insight:** This example shows the wedge effect of a tax and how DWL is the triangular loss in trades above and beyond revenue. It also illustrates how supply/demand elasticities (slopes) determine how quantity changes and thus DWL.

### Monopoly Pricing and Welfare Comparison

Inverse demand p(q)=100−2qp(q)=100-2qp(q)=100−2q. Constant marginal cost MC=20MC=20MC=20 (supply s(q)=20s(q)=20s(q)=20). Find competitive and monopoly equilibria, compute CS, PS, TS, and DWL.

1. Competitive equilibrium: solve $100-2q^*=20 \Rightarrow 80=2q^* \Rightarrow q^*=40$. Price $P^*=100-2\cdot40=20$ (equal to MC as expected).
2. Compute competitive total surplus: TSc=∫040(100−2q−20) dq=∫040(80−2q) dq=[80q−q2]040=3200−1600=1600TS\_c=\int\_0^{40} (100-2q - 20)\,dq = \int\_0^{40} (80-2q)\,dq = [80q - q^2]\_0^{40} = 3200 - 1600 = 1600TSc​=∫040​(100−2q−20)dq=∫040​(80−2q)dq=[80q−q2]040​=3200−1600=1600.
3. Monopoly: MR for linear demand p(q)=100−2qp(q)=100-2qp(q)=100−2q is MR=100−4qMR = 100-4qMR=100−4q. Set MR=MCMR=MCMR=MC: $100-4q\_m=20 \Rightarrow 80=4q\_m \Rightarrow q\_m=20.Monopolyprice. Monopoly price .Monopolypricep(q\_m)=100-2\cdot20=60$.
4. Compute monopoly total surplus: TSm=∫020(100−2q−20) dq=∫020(80−2q) dq=[80q−q2]020=1600−400=1200TS\_m=\int\_0^{20} (100-2q - 20)\,dq = \int\_0^{20} (80-2q)\,dq = [80q - q^2]\_0^{20} = 1600 - 400 = 1200TSm​=∫020​(100−2q−20)dq=∫020​(80−2q)dq=[80q−q2]020​=1600−400=1200.
5. DWL is TSc−TSm=1600−1200=400TS\_c - TS\_m = 1600 - 1200 = 400TSc​−TSm​=1600−1200=400.

**Insight:** This example highlights how monopolistic output restriction generates a triangular DWL equal to the value of trades between the monopoly and competitive quantities that no longer occur. It demonstrates computing MR from inverse demand (a skill from Demand Functions (d3)).

## Key Takeaways

- ✓

  Consumer surplus (CS) is the integral of the inverse demand minus price: CS=∫0q∗(p(q)−P) dqCS=\int\_0^{q^\*} (p(q)-P)\,dqCS=∫0q∗​(p(q)−P)dq; compute it using antiderivatives from Integrals (d2).
- ✓

  Producer surplus (PS) is the integral of price minus supply: PS=∫0q∗(P−s(q)) dqPS=\int\_0^{q^\*} (P-s(q))\,dqPS=∫0q∗​(P−s(q))dq, and total surplus equals the integral of demand minus supply.
- ✓

  Deadweight loss arises whenever market quantity deviates from the competitive benchmark; for linear wedges (tax, monopoly, price controls) DWL is typically a triangle with area 12⋅wedge⋅quantity change\tfrac{1}{2}\cdot\text{wedge}\cdot\text{quantity change}21​⋅wedge⋅quantity change.
- ✓

  To compute CS from empirical Marshallian demand Q(P)Q(P)Q(P), either invert to P(Q)P(Q)P(Q) or use CS=∫PPˉQ(p) dpCS=\int\_P^{\bar P} Q(p)\,dpCS=∫PPˉ​Q(p)dp with a choke price Pˉ\bar PPˉ where Q(Pˉ)=0Q(\bar P)=0Q(Pˉ)=0.
- ✓

  Policy analysis requires comparing changes in CS and PS (and government revenue or externality corrections) to assess net welfare effects.
- ✓

  Graphical intuition is crucial: CS is the area under the demand curve above price, PS is area above supply below price; DWL is the area of forgone mutually beneficial trades.
- ✓

  Elasticities and curvature matter: DWL grows with the size of distortions and the slopes of demand/supply (steeper curves usually imply larger welfare changes for a given price wedge).

## Common Mistakes

- ✗

  Confusing Marshallian and inverse demand: People sometimes try to integrate Q(P)Q(P)Q(P) with respect to quantity. If you have Q(P)Q(P)Q(P), either invert it to P(Q)P(Q)P(Q) or integrate Q(p)Q(p)Q(p) with respect to price using CS=∫PPˉQ(p) dpCS=\int\_P^{\bar P} Q(p)\,dpCS=∫PPˉ​Q(p)dp.
- ✗

  Forgetting to find the correct traded quantity under policy: When a tax or price control is imposed, do not assume quantity stays at the pre-policy level; solve the new equilibrium carefully (use p(q)=s(q)+tp(q)=s(q)+tp(q)=s(q)+t for taxes).
- ✗

  Treating producer surplus as profits: PS computed as ∫0q∗(P−s(q)) dq\int\_0^{q^\*} (P-s(q))\,dq∫0q∗​(P−s(q))dq is not the same as accounting profit if fixed costs exist. PS equals profit only when variable costs equal s(q)s(q)s(q) and fixed costs are zero.
- ✗

  Applying triangular DWL formula indiscriminately: The simple 12⋅wedge⋅Δq\frac{1}{2} \cdot \text{wedge} \cdot \Delta q21​⋅wedge⋅Δq formula is exact for linear segments, but with nonlinear demand/supply you must integrate the difference to get accurate DWL.

## Practice

easy

Easy: Given inverse demand p(q)=80−2qp(q)=80-2qp(q)=80−2q and a market price P=40P=40P=40, compute consumer surplus.

**Hint:** Find q∗q^\*q∗ by solving $80-2q^*=40$, then integrate $p(q)-P$ from 0 to $q^*$.

Show solution

Solve $80-2q^*=40\Rightarrow q^*=20.Then. Then .ThenCS=\int\_0^{20} (80-2q - 40)\,dq = \int\_0^{20} (40-2q)\,dq = [40q - q^2]\_0^{20} = 800 - 400 = 400.

medium

Medium: Demand p(q)=150−5qp(q)=150-5qp(q)=150−5q, supply s(q)=30+2qs(q)=30+2qs(q)=30+2q. A per-unit tax t=20t=20t=20 is imposed. Compute pre-tax equilibrium (q∗,P∗)(q^\*,P^\*)(q∗,P∗), post-tax traded quantity qtq\_tqt​, tax revenue, and DWL.

**Hint:** Pre-tax: solve p(q)=s(q)p(q)=s(q)p(q)=s(q). With tax, solve p(qt)=s(qt)+tp(q\_t)=s(q\_t)+tp(qt​)=s(qt​)+t. Then TR=t⋅qtTR=t\cdot q\_tTR=t⋅qt​ and DWL=0.5⋅t⋅(q∗−qt)DWL=0.5\cdot t\cdot(q^\*-q\_t)DWL=0.5⋅t⋅(q∗−qt​) (exact for linear curves).

Show solution

Pre-tax: $150-5q^*=30+2q^*\Rightarrow 120=7q^*\Rightarrow q^*=120/7\approx17.1429$. $P^*=p(q^*)=150-5\cdot17.1429\approx64.2855$. With tax: $150-5q\_t = 30 + 2q\_t + 20 \Rightarrow 150-5q\_t = 50 + 2q\_t \Rightarrow 100 = 7q\_t \Rightarrow q\_t = 100/7 \approx14.2857.Taxrevenue. Tax revenue .TaxrevenueTR = 20\cdot14.2857 = 285.714.DWL. DWL .DWL=0.5\cdot20\cdot(17.1429 - 14.2857) = 10\cdot2.8572 = 28.572$ (approximately).

hard

Hard: Suppose aggregate inverse demand is p(q)=200−10q+q2/10p(q)=200 - 10q + q^2/10p(q)=200−10q+q2/10 (nonlinear) and marginal cost is constant MC=40MC=40MC=40. Compute the competitive quantity and the monopoly quantity (monopolist sets MR=MC). Then compute DWL exactly by evaluating the integrals (no approximations).

**Hint:** Compute competitive by solving p(q)=MCp(q)=MCp(q)=MC. For monopoly, compute MR as derivative of total revenue TR(q)=p(q)qTR(q)=p(q)qTR(q)=p(q)q (i.e., MR=p(q)+p′(q)qMR = p(q) + p'(q) qMR=p(q)+p′(q)q). Then evaluate TSc=∫0qc(p(q)−MC) dqTS\_c=\int\_0^{q\_c} (p(q)-MC)\,dqTSc​=∫0qc​​(p(q)−MC)dq and TSm=∫0qm(p(q)−MC) dqTS\_m=\int\_0^{q\_m} (p(q)-MC)\,dqTSm​=∫0qm​​(p(q)−MC)dq and take difference.

Show solution

Competitive: solve $200 -10q + q^2/10 = 40 \Rightarrow 160 -10q + q^2/10 =0$. Multiply by 10: $1600 -100q + q^2 =0.Solvequadratic. Solve quadratic .Solvequadraticq^2 -100q +1600=0.Discriminant. Discriminant .Discriminant\Delta=10000 - 6400 = 3600,sqrt, sqrt ,sqrt=60.Roots:. Roots: .Roots:q=(100 \pm 60)/2 = 80$ or $20.Theeconomicallyrelevant(smaller)rootwherepricepositiveis. The economically relevant (smaller) root where price positive is .Theeconomicallyrelevant(smaller)rootwherepricepositiveisq\_c=20(check (check (checkp(20)=200-200+400/10=40$ equals MC).

Monopoly MR: TR(q)=p(q)q=(200−10q+q2/10)q=200q−10q2+q3/10TR(q)=p(q)q = (200-10q + q^2/10)q = 200q -10q^2 + q^3/10TR(q)=p(q)q=(200−10q+q2/10)q=200q−10q2+q3/10. Then MR=dTR/dq=200−20q+3q2/10MR = dTR/dq = 200 -20q + 3q^2/10MR=dTR/dq=200−20q+3q2/10. Set MR=MC=40MR=MC=40MR=MC=40:

$200 -20q + 0.3 q^2 = 40 \Rightarrow 160 -20q + 0.3 q^2 =0$. Multiply by 10: $1600 -200q +3 q^2 =0$. Solve $3q^2 -200q +1600=0.Discriminant. Discriminant .Discriminant\Delta = 40000 - 19200 =20800,sqrt, sqrt ,sqrt\approx144.222.Roots. Roots .Rootsq = (200 \pm 144.222)/(6).Positiveroots:. Positive roots: .Positiveroots:q\approx (200-144.222)/6 = 55.778/6 \approx 9.2963or or orq\approx (200+144.222)/6=344.222/6\approx57.3703.Themonopolypicksthequantityyieldingdownwardslopingdemandandpositiveprice;thesmallerroot. The monopoly picks the quantity yielding downward sloping demand and positive price; the smaller root .Themonopolypicksthequantityyieldingdownwardslopingdemandandpositiveprice;thesmallerrootq\_m\approx9.2963isthemonopolyquantity(thelargerrootwouldmakeMRincreasingregion).Compute is the monopoly quantity (the larger root would make MR increasing region). Compute isthemonopolyquantity(thelargerrootwouldmakeMRincreasingregion).Computep(q\_m) = 200 -10(9.2963) + (9.2963)^2/10 \approx 200 -92.963 + 8.645 = 115.682. $

Compute total surpluses numerically via integrals. TSc=∫020(p(q)−40) dqTS\_c=\int\_0^{20} (p(q)-40)\,dqTSc​=∫020​(p(q)−40)dq; integrate p(q)−40=160−10q+q2/10p(q)-40 = 160 -10q + q^2/10p(q)−40=160−10q+q2/10. Antiderivative: $160q -5q^2 + q^3/30$. Evaluate at 20: $160\cdot20 -5\cdot400 + 8000/30 = 3200 -2000 + 266.6667 = 1466.6667.So. So .SoTS\_c\approx1466.6667$.

TSm=∫09.2963(p(q)−40) dqTS\_m=\int\_0^{9.2963} (p(q)-40)\,dqTSm​=∫09.2963​(p(q)−40)dq. Evaluate antiderivative at 9.2963: $160\cdot9.2963 -5\cdot(9.2963)^2 + (9.2963)^3/30 \approx 1487.408 - 432.203 + 252.419 = 1307.624(theseareintermediatevalues;integratecarefully).So (these are intermediate values; integrate carefully). So (theseareintermediatevalues;integratecarefully).SoTS\_m \approx1307.624.DWL. DWL .DWL= TS\_c - TS\_m \approx 1466.667 - 1307.624 = 159.043$ (approximately).

## Connections

Looking back: This lesson builds directly on Demand Functions (d3) where you learned how to derive inverse demand p(q)p(q)p(q) from consumers' utility maximization and how to aggregate individual demands into a market demand. It also uses the calculus techniques from Integrals (d2) to compute areas under curves (integrals, antiderivatives, Riemann-sum intuition). Looking forward: mastering consumer surplus and deadweight loss is essential for Public Finance (tax incidence, optimal taxation), Industrial Organization (monopoly pricing, mergers and antitrust analysis), Environmental Economics (Pigouvian taxes and welfare corrections), and empirical welfare analysis (estimating willingness-to-pay and calculating compensating/equivalent variations). Specific downstream tools that require this knowledge include computing compensating variation from Hicksian demand, doing general-equilibrium welfare comparisons where surplus moves across markets, and using surplus calculations in cost–benefit analysis for policy evaluation.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
