---
title: Auction Theory
description: Designing and analyzing auction mechanisms. Revenue equivalence.
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
permalink: /tech-tree/auction-theory/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Auction Theory

Game TheoryDifficulty: ★★★★★Depth: 9Unlocks: 0

Designing and analyzing auction mechanisms. Revenue equivalence.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Auction mechanism as allocation and payment functions (the mechanism maps bid profiles to who receives the good and what each bidder pays)
- -Independent private-value, risk-neutral, single-parameter model (each bidder has a privately drawn valuation v\_i)
- -Revenue Equivalence Theorem: under the above model, identical allocation rules and a common normalization yield the same expected payments (seller revenue) across all incentive-compatible auctions

## Key Symbols & Notation

v\_i (bidder i's private valuation)x\_i(b) and p\_i(b) (allocation probability/function and payment for bidder i as functions of the bid profile b)

## Essential Relationships

- -Incentive-compatibility/envelope link: Bayes-Nash incentive-compatibility implies allocation monotonicity and fixes payments from the allocation rule (payments are determined up to a constant by the allocation), hence expected payments - and revenue - depend only on the allocation rule and the chosen normalization (this is the core reason for revenue equivalence)

## Prerequisites (2)

[Mechanism Design11 atoms](/tech-tree/mechanism-design/)[Bayesian Inference5 atoms](/tech-tree/bayesian-inference/)

## Referenced by (8)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (8)

[RevenueBusiness

Ad revenue maximization with privately-known bidder values IS auction theory - Myerson optimal auctions, reserve prices, and revenue equivalence are the exact mathematical tools for this problem.](/business/revenue/)[risk-neutralBusiness

The formula ui = v\_i x\_i(b) - p\_i(b) is the standard quasi-linear bidder utility from auction theory. Risk-neutral bidders are the baseline assumption enabling revenue equivalence and optimal auction design results.](/business/risk-neutral/)[ad slotsBusiness

Online ad slot allocation (Google Ads GSP, programmatic RTB) is the single largest real-world application of auction theory; second-price and generalized second-price mechanisms directly govern how billions in ad spend clear daily](/business/ad-slots/)[bidBusiness

Auction theory directly formalizes bid mechanics: how rational agents set bids, winner determination rules (first-price, second-price), revenue equivalence across formats, and the winner's curse - all governing the single-winner competitive allocation that defines a bid](/business/bid/)[auctionBusiness

Direct mathematical foundation: revenue equivalence theorem, optimal reserve prices, first-price vs second-price analysis, and winner's curse - the formal toolkit for designing and analyzing the auction formats described](/business/auction/)[commodity marketsBusiness

Commodity exchanges (futures pits, electronic matching engines) are literal auction mechanisms; revenue equivalence, bidder strategies, and clearing price formation from auction theory are the direct mathematical foundation for how commodity markets allocate goods and discover prices.](/business/commodity-markets/)[ExternalityBusiness

VCG auctions are the canonical application of Clarke pivot payments. In a second-price auction the winner pays the externality they impose on the second-highest bidder - the simplest instance of the general rule.](/business/externality/)[Efficient AllocationBusiness

The single-item special case of VCG is the Vickrey (second-price sealed-bid) auction; understanding VCG requires seeing how it generalizes second-price logic to multi-item combinatorial settings with Clarke pivot payments](/business/efficient-allocation/)

Advanced Learning Details

### Graph Position

145

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

9

Chain Length

### Cognitive Load

6

Atomic Elements

49

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (25)

- - First-price sealed-bid auction (each bidder submits one sealed bid; highest bid wins and pays own bid)
- - Second-price (Vickrey) sealed-bid auction (highest bidder wins but pays the second-highest bid)
- - English (ascending) auction (open, price rises until one bidder remains)
- - Dutch (descending) auction (price falls until a bidder accepts)
- - Private values vs common values (whether each bidder's value is their own private number or there is a common underlying value)
- - Independent private values (IPV) model (each bidder's value drawn independently from a distribution)
- - Affiliated/correlated values (signals/values across bidders are statistically positively related)
- - Bayesian-Nash equilibrium (BNE) as the solution concept used in auctions (bidders choose bidding strategies given beliefs about others)
- - Bidding strategy / bidding function β(v) (a mapping from a bidder's valuation to the bid they submit)
- - Bid shading (strategic lowering of bids below true valuation in first-price-style auctions)
- - Order statistics of valuations (notation and use of the highest, second-highest, etc., valuations to compute outcomes)
- - Allocation rule x\_i(·) (probability the item is awarded to bidder i as a function of reported/true types)
- - Payment rule p\_i(·) (payment made by bidder i as a function of reported/true types or bids)
- - Interim vs ex post vs ex ante perspectives (expected payoffs/IC/IR computed at different information timings)
- - Revenue Equivalence Theorem (RET) - statement that, under specific assumptions, all standard auctions that always allocate to the highest valuation and give the same payoff to the lowest type produce the same expected revenue)
- - Monotonicity/implementability condition for allocation rules (allocation must be nondecreasing in type to be implementable by an incentive-compatible payment rule)
- - Payment formula derived from a monotone allocation (payment determined by integral of allocation probabilities up to a constant)
- - Virtual valuation φ(v) = v - (1-F(v))/f(v) (transformation of values used to compute marginal revenue)
- - Myerson's optimal auction (design that maximizes expected virtual surplus, possibly via reserve prices and allocation based on φ)
- - Reserve price (a minimum acceptable price set by seller; can be optimized using virtual valuations)
- - Ironing (flattening non-monotone regions of virtual valuation to restore implementability in the optimal auction)
- - Winner's curse (in common-value settings, the winner tends to overestimate the value leading bidders to shade bids)
- - Symmetric bidders assumption (identical distributional assumptions used to derive symmetric equilibria)
- - Role of risk preferences in auctions (how risk neutrality vs risk aversion changes equilibrium bids and revenue comparisons)
- - Revenue ranking of formats conditional on assumptions (how expected revenue of first-price, second-price, English, Dutch compare under different assumptions)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Why do wildly different auction formats (first-price, second-price, all-pay, etc.) so often produce the same expected revenue—at least on paper? Auction theory explains when this “doesn’t matter” result is true, exactly what assumptions make it true, and what changes when those assumptions fail.

TL;DR:

In the standard independent private-values, risk-neutral, single-item, single-parameter model, any two Bayesian incentive-compatible auctions with the same allocation rule (who wins for each bid/valuation profile) and the same payment normalization deliver the same expected payments for every bidder and thus the same expected seller revenue. This is the Revenue Equivalence Theorem. The key technical tool is the payment identity: once an allocation rule xᵢ(vᵢ) is fixed (monotone), incentive compatibility pins down payments up to a constant.

## What Is Auction Theory?

Auction theory is the study of **mechanisms** for allocating scarce resources—often a single item—to agents with private information, and of the strategic behavior those mechanisms induce.

At the core of modern auction theory is a mechanism-design viewpoint:

- •An **auction** is not “a set of rules people follow informally.”
- •It is a **mechanism**: a precise mapping from reported information (bids) to outcomes.

### The mechanism view: allocation + payments

In a single-item auction with n bidders, each bidder i submits a bid bᵢ. The mechanism specifies:

- •**Allocation function** xᵢ(**b**) ∈ [0,1]: the probability bidder i receives the item (0/1 for deterministic auctions). Here **b** = (b₁,…,bₙ) is the bid profile.
- •**Payment function** pᵢ(**b**) ≥ 0: how much bidder i pays.

Think of xᵢ(**b**) as the “who gets it” rule and pᵢ(**b**) as the “who pays what” rule. Together, they fully define the auction.

### Values, types, and utilities

In the canonical model for revenue equivalence, each bidder i has a privately known valuation vᵢ for receiving the item. The bidder’s utility is quasi-linear:

uᵢ = vᵢ · xᵢ(**b**) − pᵢ(**b**).

This form matters because it lets us separate “value from allocation” from “cost of payment” and use calculus-like envelope arguments.

### The standard assumptions behind revenue equivalence

Revenue equivalence is powerful—but it is not magic. It relies on a carefully chosen environment:

1) **Single item (or single-parameter allocation)**

- •Each bidder’s private information can be summarized by a single number vᵢ.

2) **Independent private values (IPV)**

- •vᵢ is drawn independently from a distribution Fᵢ, and vᵢ is bidder i’s own value.
- •Bidder i’s value does not directly depend on others’ signals.

3) **Risk neutral**

- •Bidders maximize expected utility E[uᵢ].

4) **Bayesian setting**

- •Bidders know the distributions Fⱼ but not realized vⱼ.

5) **Incentive compatibility and equilibrium focus**

- •We study mechanisms where truth-telling is optimal (Bayesian incentive compatibility) or analyze Bayes–Nash equilibria of common formats.

### Why this perspective matters

Many real auctions look different on the surface:

- •First-price: winner pays their bid.
- •Second-price: winner pays the second-highest bid.
- •All-pay: everyone pays their bid, winner gets the item.

Yet in the IPV, risk-neutral, symmetric setting with appropriate equilibrium behavior, expected revenue often coincides. Auction theory explains **why**: once you fix the probability with which each type wins, incentive compatibility forces a unique expected payment schedule up to an additive constant.

So auction theory is fundamentally about:

- •**Design**: choosing xᵢ and pᵢ to optimize a goal (revenue, efficiency, fairness).
- •**Analysis**: predicting equilibrium bids and outcomes.
- •**Robustness**: understanding which conclusions survive when assumptions change (risk aversion, correlated values, budgets, multi-dimensional types).

In this lesson, we’ll build toward the Revenue Equivalence Theorem (RET) as a central organizing principle—then connect it to concrete auction formats and to the limits of equivalence.

## Core Mechanic 1: Modeling Auctions as Allocation and Payment Functions

The key to understanding revenue equivalence is to stop thinking in terms of “first-price vs second-price” and start thinking in terms of **(x, p)**.

### Direct vs indirect mechanisms

A **direct mechanism** asks agents to report their type (here, valuation) directly. Formally:

- •Bidder i reports rᵢ (intended to be vᵢ).
- •Mechanism outputs xᵢ(**r**) and pᵢ(**r**).

An “ordinary” auction (like first-price) is an **indirect mechanism**: it asks for bids bᵢ, which are strategic actions rather than types. But the Revelation Principle says:

> If an outcome can be achieved by some equilibrium of some mechanism, then there exists a direct mechanism that achieves the same outcome with truthful reporting.

So when proving general results like RET, it’s convenient to reason about direct, truthful mechanisms.

### Bayesian Incentive Compatibility (BIC)

In a direct mechanism, bidder i with true value vᵢ chooses a report rᵢ to maximize expected utility:

Uᵢ(vᵢ; rᵢ) = E\_{v\_{−i}}[ vᵢ · xᵢ(rᵢ, v\_{−i}) − pᵢ(rᵢ, v\_{−i}) ].

The mechanism is **Bayesian incentive compatible** if truthful reporting is optimal:

Uᵢ(vᵢ; vᵢ) ≥ Uᵢ(vᵢ; rᵢ) for all vᵢ, rᵢ.

Define the interim allocation and interim payment (expectations over others’ values):

xᵢ(vᵢ) = E\_{v\_{−i}}[ xᵢ(vᵢ, v\_{−i}) ]

pᵢ(vᵢ) = E\_{v\_{−i}}[ pᵢ(vᵢ, v\_{−i}) ].

Then the interim expected utility under truthful reporting is:

Uᵢ(vᵢ) = vᵢ · xᵢ(vᵢ) − pᵢ(vᵢ).

This “interim” view is crucial: RET is a statement about expected payments, and these expected payments are pinned down by interim allocation probabilities.

### Monotonicity as the heart of implementability

In single-parameter settings, a foundational insight is:

- •For a mechanism to be incentive compatible, higher valuations must not lead to lower chances of winning.

Formally, **xᵢ(vᵢ)** must be non-decreasing in vᵢ.

Intuition:

- •If higher types were less likely to win, a high type could pretend to be low to get a better allocation, breaking incentive compatibility.

This monotonicity is not just a “nice property.” In single-parameter domains, it is close to being the whole story.

### Normalizations and participation constraints

Payments are only pinned down “up to a constant.” That constant is determined by a boundary condition such as:

- •**Individual rationality (IR)**: participating yields non-negative expected utility.
- •A standard normalization: the lowest type gets zero utility.

Common choice:

Uᵢ(0) = 0.

With that normalization (and assuming vᵢ has a lower bound 0), we can solve for pᵢ(vᵢ) uniquely.

### Comparing common auction formats via (x, p)

It helps to see how familiar auctions fit into xᵢ(**b**) and pᵢ(**b**) language:

| Auction format | Allocation xᵢ(**b**) | Payment pᵢ(**b**) | Notes |
| --- | --- | --- | --- |
| First-price | 1 if bᵢ is highest, else 0 | winner pays bᵢ | Indirect; equilibrium shading |
| Second-price (Vickrey) | 1 if bᵢ is highest, else 0 | winner pays 2nd-highest bid | Truthful in dominant strategies under IPV |
| All-pay | 1 if bᵢ is highest, else 0 | everyone pays bᵢ | Strong incentives; rent dissipation |

Notice: in all three, the allocation rule (deterministic) is the same—highest bid wins. What differs is the payment rule and therefore equilibrium behavior.

Revenue equivalence will say: if (in equilibrium) these mechanisms induce the same allocation probabilities for each type and satisfy the same normalization, then their expected revenues coincide.

At this point, we have the key objects:

- •Allocation rule xᵢ
- •Payment rule pᵢ
- •Incentive compatibility constraints (truthful or equilibrium-induced)

Next we’ll derive the payment identity: the formula that makes revenue equivalence inevitable once you accept incentive compatibility and single-parameter structure.

## Core Mechanic 2: The Payment Identity and the Revenue Equivalence Theorem

Revenue equivalence is ultimately a consequence of one fact:

> In single-parameter, quasi-linear environments, incentive compatibility forces expected utility to satisfy an envelope condition, which pins down payments from allocations.

We’ll go step by step and keep the “why” in view.

## 1) Why payments are determined by allocations

Suppose we fix an interim allocation rule xᵢ(vᵢ). Imagine you are the auction designer.

- •If you give higher types a higher chance to win (monotone xᵢ), you must charge them appropriately.
- •If you charge too little, high types get huge rents.
- •If you charge too much, they will misreport downward.

So the payment schedule pᵢ(vᵢ) is tightly constrained by incentive compatibility.

## 2) Deriving the envelope condition (intuition first)

Let Uᵢ(v) be the maximum expected utility type v can obtain by choosing the best report:

Uᵢ(v) = max\_{r} [ v · xᵢ(r) − pᵢ(r) ].

This is the maximum over a family of linear functions in v (each r defines a line with slope xᵢ(r)). The maximum of linear functions is convex and has a subgradient. Under standard regularity, we get an “envelope”:

Uᵢ′(v) = xᵢ(v) (almost everywhere).

Interpretation:

- •When your value v increases slightly, your utility increases by approximately the probability you get the item.
- •The mechanism cannot make your marginal utility depend on anything else without breaking incentive compatibility.

## 3) Turning the envelope into a payment formula

Start from the truthful interim utility:

Uᵢ(v) = v · xᵢ(v) − pᵢ(v).

Differentiate both sides with respect to v (where differentiable):

Uᵢ′(v) = xᵢ(v) + v · xᵢ′(v) − pᵢ′(v).

But envelope says Uᵢ′(v) = xᵢ(v). Therefore:

xᵢ(v) = xᵢ(v) + v · xᵢ′(v) − pᵢ′(v)

Cancel xᵢ(v) on both sides:

0 = v · xᵢ′(v) − pᵢ′(v)

So:

pᵢ′(v) = v · xᵢ′(v).

Now integrate from 0 to v:

pᵢ(v) − pᵢ(0) = ∫₀ᵛ t · xᵢ′(t) dt.

Integrate by parts to rewrite in the more standard “payment identity” form.

Let:

- •u = t ⇒ du = dt
- •d w = xᵢ′(t) dt ⇒ w = xᵢ(t)

Then:

∫₀ᵛ t · xᵢ′(t) dt

= [ t · xᵢ(t) ]₀ᵛ − ∫₀ᵛ 1 · xᵢ(t) dt

= v · xᵢ(v) − ∫₀ᵛ xᵢ(t) dt.

So:

pᵢ(v) = v · xᵢ(v) − ∫₀ᵛ xᵢ(t) dt + pᵢ(0).

Equivalently, in utility form:

Uᵢ(v) = Uᵢ(0) + ∫₀ᵛ xᵢ(t) dt.

This is the central identity.

### What is the “constant”?

The term pᵢ(0) (or Uᵢ(0)) is a boundary condition:

- •If we normalize Uᵢ(0) = 0 (lowest type gets zero utility), then pᵢ(0) = 0 and payments are fully determined.

In general, two mechanisms with the same xᵢ(v) can differ only by a constant shift in utilities/payments, as long as they remain feasible (e.g., no negative payments if not allowed).

## 4) Revenue Equivalence Theorem (statement)

Here is a standard version:

**Revenue Equivalence Theorem (RET).**

In an independent private-values, risk-neutral, single-parameter environment, consider two BIC mechanisms (x, p) and (x, p̃) that implement the same interim allocation rule xᵢ(vᵢ) for each bidder i and satisfy the same normalization (e.g., Uᵢ(0) = 0 for all i). Then for every i and every vᵢ:

pᵢ(vᵢ) = p̃ᵢ(vᵢ),

and therefore the expected seller revenue is the same:

E[ ∑ᵢ pᵢ(vᵢ) ] = E[ ∑ᵢ p̃ᵢ(vᵢ) ].

### Why the theorem is “almost inevitable”

Once you accept:

1) Single-parameter + quasi-linear utility

2) Incentive compatibility

3) A fixed allocation rule xᵢ(vᵢ)

…the payment identity shows pᵢ(vᵢ) is determined up to a constant. With a shared boundary condition, the constant matches—so payments match.

## 5) What RET does and does not say

RET is often paraphrased as “all standard auctions have the same revenue.” That’s too strong.

RET actually says:

- •If two auctions produce the same allocation rule in equilibrium (in terms of who wins as a function of types) and have the same normalization, then they have the same expected revenue.

So we still need to check:

- •Are we in the IPV + risk-neutral regime?
- •Are the mechanisms incentive compatible / do they have an equilibrium with the needed properties?
- •Do they indeed have the same allocation rule (e.g., highest value wins with the same probability)?

When those match, the revenue comparison becomes trivial—because it is already fixed by x.

In the next section, we will connect this to concrete auction formats and show how to compute payments and revenues using the identity.

## Application/Connection: Using Revenue Equivalence to Analyze Auction Formats (and When It Breaks)

Revenue equivalence becomes practical when you can argue that different auction formats induce the same allocation probabilities and satisfy the same boundary condition.

## 1) Symmetric IPV single-item auctions

Assume:

- •n bidders
- •vᵢ i.i.d. from F on [0, v̄]
- •risk neutral
- •efficient allocation: highest v wins

In many standard auctions, equilibrium behavior is such that the highest value bidder wins (monotone bidding strategies). Then the interim allocation probability for type v is:

x(v) = P(v is the highest) = P(v ≥ maxⱼ≠i vⱼ) = F(v)^{n−1}.

If we also normalize U(0) = 0, then payments are pinned down:

p(v) = v · F(v)^{n−1} − ∫₀ᵛ F(t)^{n−1} dt.

This formula is astonishingly general: it gives the expected payment of a type v bidder in *any* BIC mechanism (or equilibrium outcome) that allocates efficiently.

### From expected payments to expected revenue

Expected seller revenue is:

Rev = E[∑ᵢ pᵢ(vᵢ)].

In symmetric settings, you can compute for one bidder and multiply by n:

Rev = n · E[p(V)] where V ∼ F.

You can also derive revenue via order statistics (expected second-highest value for second-price auctions), and RET guarantees agreement.

## 2) First-price vs second-price through RET

- •In a second-price auction, truthful bidding is dominant, allocation is efficient, and payments equal the second-highest bid.
- •In a first-price auction, bidders shade bids, but equilibrium allocation is still efficient (highest v submits highest bid) under standard regularity.

Thus both auctions share the same x(v) = F(v)^{n−1} and the same U(0) = 0, so their expected revenues match.

RET saves you from solving the first-price equilibrium bid function just to compute expected revenue (though solving it is still useful for other reasons).

## 3) What about all-pay auctions?

All-pay auctions look very different: everyone pays.

But in the symmetric IPV model, the equilibrium allocation is still efficient (higher types bid more). If normalization aligns (lowest type gets zero expected utility), RET implies expected revenue matches again.

The distribution of payments differs (who pays and when), but expected seller revenue matches.

## 4) Where revenue equivalence breaks

RET is fragile in the best possible way: it tells you exactly which modeling choices matter.

### (a) Risk aversion

If bidders are risk-averse, first-price and second-price auctions no longer have the same revenue in general.

- •First-price: payment is “certain conditional on winning” (you pay your bid), which can be less risky than second-price where payment depends on others.
- •Risk preferences change bidding and thus expected payments.

### (b) Interdependent values / common values

In common-value environments (oil drilling, spectrum with uncertain market size), bidders’ signals are correlated and values depend on others’ information.

- •Winner’s curse changes bidding.
- •Allocation and payment relationships no longer reduce to single-parameter envelope formulas in the same way.

### (c) Multi-dimensional types

If each bidder has a vector type (e.g., value for multiple items, or value and budget), there is no single monotone allocation curve x(v) that pins down payments.

RET is fundamentally a single-parameter phenomenon.

### (d) Different allocation rules

Even under IPV risk-neutrality, if auctions allocate differently, revenues can differ.

Example: a reserve price changes x(v): low types are less likely to win (possibly nobody wins). This can increase revenue by trading off efficiency for extracting surplus.

### (e) Different normalizations / participation constraints

Two mechanisms with identical x(v) can still differ if:

- •one gives the lowest type positive utility (a subsidy),
- •or one imposes entry fees,
- •or one has different outside options.

RET requires a shared normalization like U(0)=0.

## 5) Connection to optimal auction design

RET is not the end of auction theory; it’s the starting point.

- •If all “reasonable” auctions yield the same revenue under strong assumptions, the designer must look for places to improve revenue: reserves, ironing, discrimination across bidders, information design.

Myerson’s optimal auction theory uses the same single-parameter machinery (monotonicity + payment identity) but optimizes expected revenue by choosing the allocation rule to maximize a virtual surplus objective.

RET teaches you this mindset:

- •**Pick x first** (allocation rule)
- •then **payments follow** from incentive compatibility

This allocation-first view is one of the most important conceptual upgrades mechanism design offers.

## Worked Examples (3)

### Compute the payment function from an allocation rule (general payment identity)

Single bidder i in a direct BIC mechanism (interim view). Value v ∈ [0,1]. Suppose the interim allocation probability is x(v) = v (higher values win with higher probability). Normalize U(0)=0. Find p(v).

1. Start with the payment identity (with U(0)=0):

   p(v) = v · x(v) − ∫₀ᵛ x(t) dt.
2. Plug in x(v)=v:

   p(v) = v · v − ∫₀ᵛ t dt

   = v² − [ t²/2 ]₀ᵛ

   = v² − v²/2.
3. Simplify:

   p(v) = v²/2.
4. Check utility:

   U(v) = v · x(v) − p(v)

   = v · v − v²/2

   = v²/2.

   Also U(v) = ∫₀ᵛ x(t) dt = ∫₀ᵛ t dt = v²/2, consistent.

**Insight:** Once x(v) is fixed and monotone, incentive compatibility determines payments (up to a constant). You can treat the mechanism as “choose x, then compute p.”

### Revenue equivalence for uniform values: expected payment of type v when highest value wins

n bidders, i.i.d. values V ∼ Uniform[0,1], risk neutral. Consider any BIC auction that allocates the item to the highest valuation (efficient allocation) and satisfies U(0)=0. Compute the interim expected payment p(v) for a bidder of type v.

1. Efficient allocation implies a type v wins iff it is the highest among n values. So the interim allocation probability is:

   x(v) = P(V\_{−i} ≤ v) = F(v)^{n−1}.
2. For Uniform[0,1], F(v)=v. Thus:

   x(v) = v^{n−1}.
3. Use the payment identity (U(0)=0):

   p(v) = v · x(v) − ∫₀ᵛ x(t) dt

   = v · v^{n−1} − ∫₀ᵛ t^{n−1} dt

   = v^n − [ t^n / n ]₀ᵛ

   = v^n − v^n/n.
4. Simplify:

   p(v) = (1 − 1/n) v^n

   = ((n−1)/n) v^n.

**Insight:** This p(v) must hold in expectation for every auction that (in equilibrium or truthfully) implements efficient allocation with the same normalization—first-price, second-price, all-pay, etc. The payment rule may differ ex post, but interim expected payments coincide.

### Expected seller revenue for Uniform[0,1] using revenue equivalence

Continue the previous setting: n bidders, i.i.d. Uniform[0,1], efficient allocation, U(0)=0. Compute expected revenue Rev = E[∑ᵢ p(Vᵢ)].

1. From the previous example, one bidder with value V has expected payment:

   p(V) = ((n−1)/n) V^n.
2. Compute E[V^n] for V ∼ Uniform[0,1]:

   E[V^n] = ∫₀¹ v^n dv

   = [ v^{n+1}/(n+1) ]₀¹

   = 1/(n+1).
3. Therefore:

   E[p(V)] = ((n−1)/n) · 1/(n+1).
4. Total expected revenue is n times that (symmetry):

   Rev = n · E[p(V)]

   = n · ((n−1)/n) · 1/(n+1)

   = (n−1)/(n+1).

**Insight:** You computed expected revenue without solving equilibrium bids in first-price (or handling second-highest order statistics in second-price). RET lets you compute revenue from the allocation rule alone.

## Key Takeaways

- ✓

  An auction mechanism is fully described by allocation functions xᵢ(**b**) and payment functions pᵢ(**b**).
- ✓

  In the IPV, risk-neutral, single-parameter model, Bayesian incentive compatibility implies monotonicity: xᵢ(vᵢ) must be non-decreasing in vᵢ.
- ✓

  The payment identity: pᵢ(v) = v · xᵢ(v) − ∫₀ᵛ xᵢ(t) dt + pᵢ(0). A normalization like Uᵢ(0)=0 (often implying pᵢ(0)=0) removes the constant.
- ✓

  Revenue Equivalence Theorem: with the same interim allocation rule and the same normalization, all BIC auctions yield the same interim expected payments and the same expected revenue.
- ✓

  RET compares auctions through their induced allocation rule x(·), not through surface rules like “pay your bid” vs “pay second price.”
- ✓

  RET does not say all auctions always have equal revenue; it depends on assumptions (IPV, risk neutrality, single-parameter types) and on matching allocation rules and normalizations.
- ✓

  RET guides optimal design thinking: choose allocation to optimize the objective; payments follow from incentive compatibility.

## Common Mistakes

- ✗

  Misstating RET as “first-price and second-price always have the same revenue” without checking assumptions (risk neutrality, IPV, efficient allocation in equilibrium, same participation normalization).
- ✗

  Forgetting the boundary condition: payments are determined only up to an additive constant unless you fix something like U(0)=0 or an explicit participation/outside option.
- ✗

  Mixing ex post payment rules with interim expected payments: RET is fundamentally about expected payments given types (interim), not necessarily pointwise equality of payments in each realized bid profile.
- ✗

  Assuming monotonicity is automatic: some allocation rules are not implementable; if x(v) is not non-decreasing, no incentive-compatible payment rule can fix it in a single-parameter setting.

## Practice

medium

Let values be i.i.d. with CDF F on [0, v̄], risk neutral, single item. Suppose an auction is BIC and allocates efficiently (highest value wins). (a) Write x(v). (b) Using U(0)=0, derive p(v) in terms of F.

**Hint:** Efficient allocation means you win iff all other n−1 values are ≤ v. Then use the payment identity p(v)=v x(v)−∫₀ᵛ x(t)dt.

Show solution

(a) x(v) = P(V\_{−i} ≤ v) = F(v)^{n−1}.

(b) With U(0)=0:

p(v) = v · F(v)^{n−1} − ∫₀ᵛ F(t)^{n−1} dt.

easy

Assume n bidders with i.i.d. Uniform[0,1] values and efficient allocation. Using RET, compute the expected revenue for n=2 and n=3. Then compare to the expected second-highest value in each case.

**Hint:** Use Rev = (n−1)/(n+1) for Uniform[0,1]. For comparison, the expected second-highest order statistic for n bidders has a known formula: E[V\_(n−1)] = (n−1)/(n+1).

Show solution

Using Rev = (n−1)/(n+1):

- •n=2: Rev = 1/3.
- •n=3: Rev = 2/4 = 1/2.

In a second-price auction with truthful bidding, revenue equals the expected second-highest value. For Uniform[0,1], E[V\_(n−1)] = (n−1)/(n+1), matching the above revenues.

medium

Consider a BIC mechanism with interim allocation x(v)=v² on v∈[0,1]. (a) Compute p(v) under normalization U(0)=0. (b) What is U(v)? (c) Verify the envelope condition U′(v)=x(v).

**Hint:** Use p(v)=v x(v)−∫₀ᵛ x(t)dt and U(v)=∫₀ᵛ x(t)dt when U(0)=0.

Show solution

(a) p(v) = v·v² − ∫₀ᵛ t² dt = v³ − [t³/3]₀ᵛ = v³ − v³/3 = (2/3) v³.

(b) U(v) = v x(v) − p(v) = v·v² − (2/3)v³ = v³/3. Also U(v)=∫₀ᵛ t² dt = v³/3.

(c) U′(v) = (d/dv)(v³/3) = v² = x(v).

## Connections

Prerequisites you’re using here:

- •[Mechanism Design](/tech-tree/mechanism-design/) — incentive compatibility, Revelation Principle, direct mechanisms
- •[Bayesian Inference](/tech-tree/bayesian-inference/) — priors over types, expectations over others’ values

Natural next nodes:

- •[Myerson’s Optimal Auction](/tech-tree/myerson-optimal-auction/) — virtual values, optimal reserve prices, revenue maximization
- •[VCG Mechanisms](/tech-tree/vcg-mechanisms/) — efficient allocation in more general settings, payments as externalities
- •[Bayes–Nash Equilibrium](/tech-tree/bayes-nash-equilibrium/) — equilibrium analysis of indirect auctions like first-price
- •[Interdependent Values & Winner’s Curse](/tech-tree/interdependent-values/) — where revenue equivalence breaks dramatically

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
