---
title: Online Algorithms
description: Decision-making without future information. Competitive analysis.
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
permalink: /tech-tree/online-algorithms/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Online Algorithms

AlgorithmsDifficulty: ★★★★☆Depth: 4Unlocks: 0

Decision-making without future information. Competitive analysis.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Online decision model: input arrives piecewise; decisions are made irrevocably using only past and current information (no future lookahead).
- -Optimal offline benchmark (OPT): clairvoyant solution that optimizes the objective with full knowledge of the entire input.
- -Competitive ratio: performance measure giving the worst-case multiplicative factor by which an online algorithm's cost/value differs from OPT.

## Key Symbols & Notation

OPT (cost/value of the optimal offline solution)

## Essential Relationships

- -Competitive bound: there exists c >= 1 (and optional additive constant b) such that for every input I, cost(algorithm on I) <= c \* OPT(I) + b; c is the competitive ratio.
- -Worst-case/adversary relation: the competitive ratio is the supremum over all input sequences (an adversary may choose the input), so online performance is measured against worst-case inputs.

## Prerequisites (2)

[Big O Notation6 atoms](/tech-tree/big-o/)[Greedy Algorithms6 atoms](/tech-tree/greedy-algorithms/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[rent-vs-buy decisionBusiness

Ski rental IS the canonical online algorithms problem. Deterministic competitive ratio 2-1/B, randomized e/(e-1). Decision-making without knowing the future duration, analyzed via competitive analysis.](/business/rent-vs-buy-decision/)

Advanced Learning Details

### Graph Position

50

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

4

Chain Length

### Cognitive Load

6

Atomic Elements

32

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (15)

- - Online algorithm: an algorithm that receives its input piece-by-piece over time and must make (usually irrevocable) decisions as each piece arrives, without knowledge of future pieces
- - Request sequence / input sequence: the ordered sequence of requests or inputs revealed to an online algorithm over time
- - Irrevocable decision: a decision made by the online algorithm that cannot be undone later when more input arrives
- - Offline (optimal / clairvoyant) algorithm: hypothetical algorithm that knows the entire input sequence in advance and achieves the best possible cost/performance for that sequence
- - Competitive analysis: the framework for evaluating online algorithms by comparing their performance to the optimal offline algorithm, typically in the worst case
- - Competitive ratio (informal concept): a numeric measure of how well an online algorithm performs relative to the offline optimum (often expressed as a multiplicative factor plus an additive term)
- - Deterministic online algorithm: an online algorithm that makes no random choices
- - Randomized online algorithm: an online algorithm that makes random choices; performance typically measured in expectation
- - Adversary models: formal descriptions of how the input sequence may be chosen relative to the algorithm (e.g., oblivious adversary that fixes the entire input in advance, adaptive adversary that may adapt to algorithm's past random choices)
- - Additive constant in competitive bounds: allowance of a fixed additive term in the comparison between online and offline costs (useful for problems with small OPT)
- - Upper bound (algorithmic) on competitive ratio: proof that a specific online algorithm achieves a certain competitive ratio
- - Lower bound (impossibility) on competitive ratio: proof that no online algorithm can achieve a competitive ratio below a certain threshold
- - Adversary argument / lower-bound construction: technique of designing input sequences (often adaptively) to force any online algorithm to perform poorly
- - Resource augmentation: analysis variant where the online algorithm is given extra resources (e.g., faster processor, larger cache) to obtain better competitive guarantees
- - Expectation as performance measure for randomized algorithms: using expected cost/performance over the algorithm's random choices as the quantity compared to OPT

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Some algorithm problems feel “unfair”: you must act now, but the input will only be revealed later. Online algorithms are the formal way to reason about decision-making under uncertainty—where the adversary controls the future and your choices are (usually) irreversible.

TL;DR:

An online algorithm makes decisions using only the past and present, while OPT is a clairvoyant offline algorithm that knows the whole future. We evaluate online algorithms via competitive analysis: compare ALG to OPT on every input sequence and bound the worst-case ratio (or additive gap). Canonical examples like Ski Rental and Paging show how to design and prove guarantees, often using clean inequality chains or potential functions to “telescope” costs over time.

## What Is an Online Algorithm?

### Why this model exists

In many real systems, you don’t get the whole input upfront.

- •A cache sees a *stream* of memory requests.
- •A router sees packets arrive over time.
- •A ride-sharing platform sees trip requests in real time.
- •A cloud service sees jobs arrive continuously.

If you had the full future sequence, you could compute a globally optimal plan. But in reality, decisions must be made *as the sequence unfolds*.

Online algorithms capture this: **input arrives piecewise**, and the algorithm must decide using only information revealed so far.

### The online decision model (informal → formal)

Think of time steps t=1,2,…t = 1, 2, \dotst=1,2,….

- •At step ttt, an item σt\sigma\_tσt​ arrives (a request, job, price, etc.).
- •The algorithm outputs an action ata\_tat​.
- •Actions can change state (e.g., what’s in cache) and incur cost (e.g., a cache miss).
- •Crucially: **no peeking** at σt+1,σt+2,…\sigma\_{t+1}, \sigma\_{t+2}, \dotsσt+1​,σt+2​,….

Formally, an **online algorithm** is a rule that maps the *prefix* σ1:t\sigma\_{1:t}σ1:t​ to an action:

at=A(σ1:t).a\_t = A(\sigma\_{1:t}).at​=A(σ1:t​).

Often, the action is irrevocable (or at least has irreversible consequences). For example, if you evict a page from cache, you can’t magically have kept it.

### The offline benchmark: OPT

To judge an online algorithm, we need a gold standard.

- •**OPT** is the *optimal offline* algorithm (also called the clairvoyant algorithm).
- •OPT knows the entire input sequence σ1:T\sigma\_{1:T}σ1:T​ in advance.
- •OPT returns the minimum possible cost (or maximum value).

We’ll write:

- •ALG(σ)\mathrm{ALG}(\sigma)ALG(σ) = cost incurred by an online algorithm on sequence σ\sigmaσ.
- •OPT(σ)\mathrm{OPT}(\sigma)OPT(σ) = cost incurred by the optimal offline algorithm on the same sequence.

### Why competitive analysis (instead of probability)

Sometimes you can assume a distribution (average-case). Competitive analysis is different: it’s **worst-case**, and it doesn’t require any distribution.

The mindset:

- •The future could be adversarial.
- •Your guarantee should hold on *every* sequence.

This is a powerful lens for systems where “rare bad cases” are unacceptable.

### An interactive visualization to build intuition (timeline + prefix view)

On an interactive canvas, represent the request sequence as a timeline.

**Visualization idea: Prefix timeline (core mental model)**

- •Draw a horizontal timeline with ticks for t=1..Tt=1..Tt=1..T.
- •At time ttt, only the prefix σ1:t\sigma\_{1:t}σ1:t​ is visible (bright). The suffix σt+1:T\sigma\_{t+1:T}σt+1:T​ is hidden (greyed out).
- •When you click “Next”, one more request is revealed.

**Side-by-side panels**

- •Left: Online algorithm state (what it currently holds/decides).
- •Right: OPT state (shown only for comparison; it “magically” knows the future).

This is not just decoration: it concretizes the asymmetry—ALG must commit with partial info while OPT is clairvoyant.

### Competitive ratio (definition)

There are two common cases:

1) **Cost minimization** (paging, ski rental, scheduling with penalties):

An online algorithm is **$c$-competitive** if there exists a constant α\alphaα such that for all sequences σ\sigmaσ,

ALG(σ)≤c OPT(σ)+α.\mathrm{ALG}(\sigma) \le c\,\mathrm{OPT}(\sigma) + \alpha.ALG(σ)≤cOPT(σ)+α.

2) **Value maximization** (online matching, ad allocation):

An online algorithm is **$c$-competitive** if for all sequences σ\sigmaσ,

ALG(σ)≥1c OPT(σ)−α.\mathrm{ALG}(\sigma) \ge \frac{1}{c}\,\mathrm{OPT}(\sigma) - \alpha.ALG(σ)≥c1​OPT(σ)−α.

In this lesson we’ll mostly use cost minimization.

### Interpreting the constants

- •The multiplicative factor ccc is the main headline.
- •The additive constant α\alphaα often handles “startup effects” (e.g., initial cache warm-up).
- •For long sequences, α\alphaα becomes negligible compared to the total cost.

### A small but important subtlety: adversaries

Competitive analysis can be stated against different adversary models:

| Adversary type | What it can do | Typical use |
| --- | --- | --- |
| Oblivious | Fixes the whole sequence in advance | Standard for randomized algorithms |
| Adaptive | Chooses next request after seeing your past actions | Stronger (harder) |

When we discuss randomized algorithms later, we’ll implicitly assume an **oblivious adversary** unless stated otherwise.

## Core Mechanic 1: Competitive Analysis (How to Prove a Guarantee)

### Why proofs look different online

In offline algorithm analysis, you often prove optimality or approximation via structural arguments (“greedy stays ahead”).

In online algorithms, you frequently prove inequalities of the form:

ALG(σ)≤c OPT(σ)+α.\mathrm{ALG}(\sigma) \le c\,\mathrm{OPT}(\sigma) + \alpha.ALG(σ)≤cOPT(σ)+α.

Because OPT knows the future, you cannot directly compare step-by-step decisions. Instead, you compare **costs** using one of these strategies:

1) **Charging arguments**: charge each online cost to something OPT must also pay.

2) **Partition into phases**: group the sequence into chunks where OPT must pay at least 1 per chunk.

3) **Potential functions**: define a “stored credit” Φ\PhiΦ so that

ΔΦ+(ALG step cost)≤c⋅(OPT step cost).\Delta\Phi + \text{(ALG step cost)} \le c \cdot \text{(OPT step cost)}.ΔΦ+(ALG step cost)≤c⋅(OPT step cost).

Summing over time telescopes the potential.

We’ll use all three.

---

## Canonical Example: Ski Rental

### The problem

You want to ski for an unknown number of days DDD.

- •Renting costs $1$ per day.
- •Buying costs BBB once.
- •If you buy, you pay BBB and then ski for free thereafter.

You must decide each day whether to rent again or buy now, without knowing DDD.

### Offline OPT

If OPT knows DDD:

- •If D<BD < BD<B, rent every day → cost DDD.
- •If D≥BD \ge BD≥B, buy on day 1 → cost BBB.

So:

OPT(D)=min⁡(D,B).\mathrm{OPT}(D) = \min(D, B).OPT(D)=min(D,B).

### A deterministic online algorithm: “Rent until day B, then buy”

Define ALG:

- •Rent for the first B−1B-1B−1 days.
- •If still skiing on day BBB, buy at the start of day BBB.

ALG cost:

- •If D<BD < BD<B: ALG rents DDD days → ALG(D)=D\mathrm{ALG}(D)=DALG(D)=D.
- •If D≥BD \ge BD≥B: ALG rents B−1B-1B−1 days and buys once → ALG(D)=(B−1)+B=2B−1\mathrm{ALG}(D)= (B-1) + B = 2B-1ALG(D)=(B−1)+B=2B−1.

### Competitive ratio proof (clean case split)

We want ALG(D)≤c OPT(D)+α\mathrm{ALG}(D) \le c\,\mathrm{OPT}(D) + \alphaALG(D)≤cOPT(D)+α.

Case 1: D<BD < BD<B

ALG(D)=D=OPT(D).\mathrm{ALG}(D)=D = \mathrm{OPT}(D).ALG(D)=D=OPT(D).

So ratio is 1.

Case 2: D≥BD \ge BD≥B

OPT(D)=B,\mathrm{OPT}(D)=B,OPT(D)=B,

and

ALG(D)=2B−1≤2B.\mathrm{ALG}(D)=2B-1 \le 2B.ALG(D)=2B−1≤2B.

Thus

ALG(D)≤2 OPT(D).\mathrm{ALG}(D) \le 2\,\mathrm{OPT}(D).ALG(D)≤2OPT(D).

So the algorithm is **2-competitive** (and in fact $2 - 1/B$-competitive with tighter arithmetic).

### Why 2 is essentially the best possible deterministically

There is a standard lower bound: no deterministic online algorithm can have competitive ratio < 2 for ski rental.

Intuition:

- •If you buy too early, adversary stops immediately → you overpaid.
- •If you buy too late, adversary keeps going → you should have bought.

A deterministic strategy has a fixed “buy day” kkk. The adversary chooses:

- •D=k−1D=k-1D=k−1 (punish early buying), or
- •D=kD=kD=k or larger (punish late buying)

to force ratio approaching 2.

### Interactive visualization: step-through Ski Rental (ALG vs OPT)

**Canvas layout**

- •Timeline days 1..T.
- •Buttons: “Reveal next day”, “Stop season now”.
- •Two rows:
- •ALG row: shows “rent” or “buy” decisions with cumulative cost.
- •OPT row: shows OPT’s best action given full D.

**Key interaction**

- •Let the learner play adversary: choose when the season ends.
- •Show the ratio ALG(D)/OPT(D)\mathrm{ALG}(D)/\mathrm{OPT}(D)ALG(D)/OPT(D) live.
- •Let learner slide the buy threshold kkk and see worst-case ratio change.

This makes the adversarial nature of competitive analysis tangible.

---

## Competitive analysis checklist (how to structure proofs)

When you face a new online problem, ask:

1) What is the state? What decisions are irreversible?

2) What does OPT do with full knowledge?

3) What is a natural online heuristic? (Often greedy.)

4) How can you lower-bound OPT’s cost on any sequence?

5) How can you upper-bound ALG’s cost and connect it to that lower bound?

This becomes especially important in paging, where the proof technique is more “global”.

## Core Mechanic 2: Paging, Phases, and Potential Functions (Amortized Competitive Proofs)

### The paging (caching) problem

You have a cache that holds kkk pages.

- •Requests arrive as a sequence σ1,σ2,…,σT\sigma\_1, \sigma\_2, \dots, \sigma\_Tσ1​,σ2​,…,σT​.
- •If the requested page is in cache: cost 0 (a hit).
- •Otherwise: cost 1 (a miss), and you must bring it in.
- •If cache is full, you must **evict** some page.

Goal: minimize total misses.

This is a quintessential online problem: you do not know future requests, so eviction is hard.

### OPT for paging

OPT is the optimal offline caching algorithm. A famous optimal offline rule is **Belady’s algorithm**:

- •On a miss, evict the page whose next use is farthest in the future.

You cannot implement this online (it needs the future), but it defines OPT.

---

## Deterministic algorithms: LRU and FIFO

Two classic online strategies:

- •**LRU** (Least Recently Used): evict the page that was used least recently.
- •**FIFO**: evict the page that has been in cache the longest.

Both are simple and widely used.

### The theorem (high-level)

LRU and FIFO are **$k$-competitive** for paging with cache size kkk.

Meaning: for all sequences σ\sigmaσ,

ALG(σ)≤k OPT(σ)+α.\mathrm{ALG}(\sigma) \le k\,\mathrm{OPT}(\sigma) + \alpha.ALG(σ)≤kOPT(σ)+α.

Usually α\alphaα can be taken as kkk or k−1k-1k−1.

We’ll focus on the *proof idea* and a potential-function visualization.

---

## Phase partitioning: a lower bound on OPT

### Why phases are useful

If we can partition the request sequence into chunks where:

- •ALG pays at most kkk per chunk, and
- •OPT must pay at least 1 per chunk,

then ALG is kkk-competitive.

### Define phases (for LRU/FIFO analysis)

A standard definition:

- •Start phase 1 at the first request.
- •Keep extending the phase until you have seen **$k+1$ distinct pages** in the current phase.
- •End the phase *right before* the request that would introduce the (k+1)(k+1)(k+1)-th distinct page.
- •Start a new phase at that request.

So each phase contains requests to at most kkk distinct pages.

### Key facts

1) **ALG incurs ≤ k misses per phase** (for LRU/FIFO).

- •Because each phase has at most kkk distinct pages, after at most kkk misses ALG can load them all.

2) **OPT incurs ≥ 1 miss per phase boundary**.

- •Consider two consecutive phases. Together they involve at least k+1k+1k+1 distinct pages (by construction).
- •OPT has cache size kkk and cannot hold all k+1k+1k+1 pages across the boundary.
- •Therefore at least one request among those must be a miss for OPT.

Thus:

- •If there are PPP phases, ALG has at most kPkPkP misses.
- •OPT has at least P−1P-1P−1 misses (sometimes PPP depending on convention).

So:

ALG(σ)≤k OPT(σ)+k.\mathrm{ALG}(\sigma) \le k\,\mathrm{OPT}(\sigma) + k.ALG(σ)≤kOPT(σ)+k.

This yields **$k$-competitiveness**.

### Interactive visualization: phase segmentation with live counters

**Canvas elements**

- •A scrolling request stream with distinct pages color-coded.
- •A vertical divider marking the current phase.
- •A counter: “distinct pages in phase: d (≤ k)”.

**Step-through behavior**

- •Each request updates the set of distinct pages in the current phase.
- •When a new page would make d=k+1d = k+1d=k+1, flash a “phase ends” event, start next phase.

**Side-by-side miss counts**

- •Track misses for LRU (or FIFO) and show “≤ k per phase” as a bar that fills up to k.
- •Track OPT lower bound as “≥ 1 per phase boundary” as a single token per boundary.

This makes the proof’s core comparison visual: *k tokens vs 1 token* per phase.

---

## Potential functions: making amortized reasoning concrete

Phase arguments are powerful but sometimes too coarse. Potential functions let you prove more refined statements and are reusable.

### The pattern

Define a potential Φt\Phi\_tΦt​ based on the algorithm’s state and OPT’s state at time ttt.

You aim to prove an inequality per step:

(ALG cost at t)+(Φt−Φt−1)≤c⋅(OPT cost at t).\text{(ALG cost at t)} + (\Phi\_t - \Phi\_{t-1}) \le c \cdot \text{(OPT cost at t)}.(ALG cost at t)+(Φt​−Φt−1​)≤c⋅(OPT cost at t).

Then sum over t=1..Tt=1..Tt=1..T:

\begin{align}

\sum\_t \text{ALG}\_t + \sum\_t (\Phi\_t - \Phi\_{t-1}) &\le c \sum\_t \text{OPT}\_t \\

\mathrm{ALG}(\sigma) + (\Phi\_T - \Phi\_0) &\le c\,\mathrm{OPT}(\sigma).

\end{align}

Because the potential telescopes, you get:

ALG(σ)≤c OPT(σ)+Φ0−ΦT.\mathrm{ALG}(\sigma) \le c\,\mathrm{OPT}(\sigma) + \Phi\_0 - \Phi\_T.ALG(σ)≤cOPT(σ)+Φ0​−ΦT​.

If Φ\PhiΦ is always nonnegative, then −ΦT≤0-\Phi\_T \le 0−ΦT​≤0, so the additive term is at most Φ0\Phi\_0Φ0​.

### A potential for paging (conceptual)

For LRU, one classic proof uses a potential related to “how many pages are in OPT’s cache but not in ALG’s cache,” but the full tight potential proof is intricate.

Instead, use potential to *visualize telescoping* on the canvas:

**Visualization: Potential telescope meter**

- •Define Φt=∣OPT cache∖ALG cache∣\Phi\_t = |\text{OPT cache} \setminus \text{ALG cache}|Φt​=∣OPT cache∖ALG cache∣ (size of set difference).
- •Show two cache boxes with page labels.
- •Show a third box labeled “Potential” containing the pages that are in OPT but not ALG.

When a miss happens:

- •ALG brings a page in (may reduce potential if it matches one OPT has).
- •OPT may also miss and change its cache (may increase or decrease potential).

Even if you don’t complete the full rigorous inequality for LRU in this lesson, the visualization teaches the *method*: potential stores “debt/credit” that can go up and down, and the proof is about bounding **cost + Δpotential**.

### Why this matters for later nodes

Potential functions are the online-algorithms cousin of amortized analysis in data structures. The same “telescope” trick appears in splay trees, dynamic arrays, and primal-dual online methods.

---

## Randomization preview (why it helps)

Deterministic paging has a lower bound: no deterministic online paging algorithm can beat competitive ratio kkk.

Randomization can do better:

- •There are randomized algorithms with competitive ratio Hk=1+1/2+⋯+1/k≈ln⁡kH\_k = 1 + 1/2 + \dots + 1/k \approx \ln kHk​=1+1/2+⋯+1/k≈lnk.

You don’t need to master these yet, but keep the principle:

- •**Randomness prevents the adversary from always predicting your evictions.**

If you later study the randomized paging algorithm (e.g., MARK), the phase concept returns, but the expectation is handled carefully.

### Interactive visualization: paging simulator (LRU vs OPT vs Random)

**Core canvas design**

- •Three columns: LRU, FIFO (or Random), OPT.
- •Each column shows a cache of size kkk with page slots.
- •A request stream runs down the center.

**Step controls**

- •Step forward/backward.
- •Toggle “show OPT’s next-use distances” (to illustrate Belady’s rule).

**Metrics**

- •Miss counters.
- •Live ratio estimate: ALG/OPT\mathrm{ALG}/\mathrm{OPT}ALG/OPT.
- •Phase counter and distinct-set display.

The goal: learners see that OPT’s evictions look “weird” locally but are globally optimal because OPT sees the future.

## Applications and Connections: Where Online Algorithms Show Up

### Why online algorithms matter in practice

Competitive analysis is a theory tool, but it maps to real engineering constraints:

- •**Caching** (CPU caches, CDN edge caches): paging is the core abstraction.
- •**Resource provisioning** (cloud autoscaling): you must allocate servers without knowing future demand.
- •**Networking** (packet scheduling, congestion control): decisions are made on streaming inputs.
- •**Auctions and ads** (online allocation): allocate impressions as users arrive.
- •**Robotics** (navigation with unknown terrain): decisions without full map.

### How to choose an online metric

Competitive ratio is worst-case; it can be pessimistic. But it is useful when:

- •You need hard guarantees.
- •Inputs can be adversarial.
- •You want robustness.

In more benign environments, you may combine competitive analysis with:

- •Stochastic assumptions (prophet inequalities, regret bounds).
- •Smoothed analysis.

### A unifying mental model: ALG vs OPT as two “players”

Many proofs become clearer if you imagine:

- •OPT is a player that knows the entire script.
- •ALG is improvising.
- •The analysis is about showing OPT cannot outperform ALG by more than a factor ccc.

### Common proof tools you now have

- •**Lower-bounding OPT** via information constraints (cache size, irrevocability).
- •**Partitioning into phases** to extract “OPT must pay at least 1 here”.
- •**Potential functions** to amortize costs and telescope sums.

### Suggested canvas interactions (explicit conceptual work)

If you are implementing this node in an interactive tech tree UI, these interactions do real teaching work:

1) **Ski rental adversary game**

- •Learner chooses the season end day DDD after seeing ALG’s policy.
- •UI displays worst-case ratio over all DDD for a chosen threshold kkk.

2) **Paging step-through with phase highlights**

- •Each new distinct page increments a “distinct-in-phase” counter.
- •When it hits k+1k+1k+1, the UI visually splits phases and drops a token in OPT’s “must miss” bucket.

3) **Potential telescope meter**

- •Show Φt\Phi\_tΦt​ over time as a bar plot.
- •Show that the proof sums “ALG cost + ΔΦ” and ΔΦ cancels across steps.

These visualizations are not optional decoration—they mirror the structure of the analysis.

## Worked Examples (3)

### Worked Example 1: Ski Rental — Prove 2-Competitiveness of a Threshold Strategy

Rent costs 1/day, buy costs B. Consider the deterministic online algorithm ALG: rent for B−1 days, then if still skiing on day B, buy. Let D be the (unknown) number of skiing days.

1. Compute OPT(D):

   OPT knows D.

   - •If D < B, OPT rents every day → cost D.
   - •If D ≥ B, OPT buys immediately → cost B.

   Therefore:

   OPT(D)=min⁡(D,B).\mathrm{OPT}(D) = \min(D,B).OPT(D)=min(D,B).
2. Compute ALG(D) by cases:

   - •If D < B, ALG never reaches day B, so it rents D days:

   ALG(D)=D.\mathrm{ALG}(D)=D.ALG(D)=D.

   - •If D ≥ B, ALG rents for B−1 days and buys once at day B:

   ALG(D)=(B−1)+B=2B−1.\mathrm{ALG}(D)=(B-1)+B = 2B-1.ALG(D)=(B−1)+B=2B−1.
3. Bound the ratio when D < B:

   Here OPT(D)=D, so

   ALG(D)=D=OPT(D)≤2 OPT(D).\mathrm{ALG}(D)=D = \mathrm{OPT}(D) \le 2\,\mathrm{OPT}(D).ALG(D)=D=OPT(D)≤2OPT(D).
4. Bound the ratio when D ≥ B:

   Here OPT(D)=B, and

   ALG(D)=2B−1≤2B=2 OPT(D).\mathrm{ALG}(D)=2B-1 \le 2B = 2\,\mathrm{OPT}(D).ALG(D)=2B−1≤2B=2OPT(D).
5. Conclude competitiveness:

   For all D,

   ALG(D)≤2 OPT(D).\mathrm{ALG}(D) \le 2\,\mathrm{OPT}(D).ALG(D)≤2OPT(D).

   So ALG is 2-competitive (with additive constant α=0).

**Insight:** This proof works because OPT has only two meaningful behaviors (rent-all or buy-immediately). The online difficulty is exactly at the unknown threshold D≈B, where an adversary can force either regret (buy too early) or regret (buy too late).

### Worked Example 2: Paging — Phase Argument for k-Competitiveness (LRU/FIFO style)

Paging with cache size k. Requests form a sequence σ. Define phases so that each phase contains requests to at most k distinct pages, and the next request would introduce the (k+1)th distinct page, starting a new phase. Consider ALG = LRU or FIFO.

1. Define the phase partition precisely:

   Start phase 1 at t=1.

   Maintain a set S of distinct pages seen in the current phase.

   When processing request σ\_t:

   - •If σ\_t ∉ S and |S| = k, then σ\_t would be the (k+1)th distinct page.
   - •End the current phase at t−1 and start a new phase at t with S = {σ\_t}.

   Thus each phase contains ≤ k distinct pages.
2. Upper-bound ALG’s misses per phase:

   Within a single phase, there are at most k distinct pages.

   ALG can miss at most once per distinct page when it first appears in the phase.

   So misses in a phase ≤ k.

   (After a page is loaded, subsequent requests in the same phase can be hits unless it gets evicted; for LRU/FIFO under this phase definition, the standard argument shows it won’t evict a page needed again within the phase before all k distinct pages have been loaded.)
3. Lower-bound OPT’s misses across phases:

   Consider two consecutive phases i and i+1.

   By construction, phase i has k distinct pages, and phase i+1 starts with a new page not in phase i’s distinct set (otherwise we wouldn’t start a new phase).

   Therefore, across the boundary there are at least k+1 distinct pages that are requested in the union of the two phases.

   OPT’s cache holds only k pages, so it cannot have all k+1 pages resident at the times they are needed.

   Hence OPT must incur at least 1 miss attributable to each phase boundary.
4. Relate totals:

   Let P be the number of phases.

   - •ALG misses ≤ kP.
   - •OPT misses ≥ P−1.

   So:

   ALG(σ)≤kP≤k(OPT(σ)+1)=k OPT(σ)+k.\mathrm{ALG}(\sigma) \le kP \le k(\mathrm{OPT}(\sigma)+1) = k\,\mathrm{OPT}(\sigma) + k.ALG(σ)≤kP≤k(OPT(σ)+1)=kOPT(σ)+k.
5. Conclude k-competitiveness:

   ALG is k-competitive with additive constant α = k.

**Insight:** The phase partition turns a messy streaming process into a counting argument: ALG spends ≤ k “tokens” per phase, while OPT must spend ≥ 1 token per phase boundary. This is the backbone of many competitive proofs: invent a structure where OPT is forced to pay regularly.

### Worked Example 3: Potential-Function Telescoping on a Toy Online Cost Process

You want to understand the telescoping pattern used in online proofs. Suppose an online process has per-step cost a\_t, and you define a potential Φ\_t ≥ 0. You manage to prove for every step t:

at+(Φt−Φt−1)≤c ot,a\_t + (\Phi\_t - \Phi\_{t-1}) \le c\,o\_t,at​+(Φt​−Φt−1​)≤cot​,

where o\_t is OPT’s per-step cost.

1. Write the per-step inequality:

   For each t,

   at+(Φt−Φt−1)≤c ot.a\_t + (\Phi\_t - \Phi\_{t-1}) \le c\,o\_t.at​+(Φt​−Φt−1​)≤cot​.
2. Sum over t = 1..T:

   ∑t=1Tat+∑t=1T(Φt−Φt−1)≤c∑t=1Tot.\sum\_{t=1}^T a\_t + \sum\_{t=1}^T (\Phi\_t - \Phi\_{t-1}) \le c \sum\_{t=1}^T o\_t.t=1∑T​at​+t=1∑T​(Φt​−Φt−1​)≤ct=1∑T​ot​.
3. Recognize the telescope:

   The second sum cancels internally:

   \begin{align}

   \sum\_{t=1}^T (\Phi\_t - \Phi\_{t-1})

   &= (\Phi\_1-\Phi\_0) + (\Phi\_2-\Phi\_1) + \dots + (\Phi\_T-\Phi\_{T-1}) \\

   &= \Phi\_T - \Phi\_0.

   \end{align}
4. Rewrite in total-cost form:

   Let ALG = ∑ a\_t and OPT = ∑ o\_t. Then

   ALG+(ΦT−Φ0)≤c OPT.\mathrm{ALG} + (\Phi\_T - \Phi\_0) \le c\,\mathrm{OPT}.ALG+(ΦT​−Φ0​)≤cOPT.
5. Use nonnegativity of potential:

   If Φ\_T ≥ 0, then

   ALG≤c OPT+Φ0.\mathrm{ALG} \le c\,\mathrm{OPT} + \Phi\_0.ALG≤cOPT+Φ0​.

**Insight:** A potential function is a bookkeeping device that allows you to “move” cost between time steps. The proof succeeds when the potential changes cancel (telescope), leaving only endpoints. A good visualization is literally a stack of blocks that move left/right, showing cancellation as you sum.

## Key Takeaways

- ✓

  Online algorithms act on prefixes: at time t they see only σ₁:t, not the future, and decisions often have irreversible consequences.
- ✓

  OPT is the optimal offline (clairvoyant) benchmark; competitive analysis compares ALG against OPT on every input sequence.
- ✓

  For minimization problems, c-competitiveness typically means ALG(σ) ≤ c·OPT(σ) + α, where α handles small startup effects.
- ✓

  Ski Rental illustrates threshold strategies and adversarial worst-case reasoning; a simple deterministic strategy is 2-competitive and 2 is essentially optimal deterministically.
- ✓

  Paging formalizes caching; LRU/FIFO achieve k-competitive guarantees via phase partitioning and lower-bounding OPT’s unavoidable misses.
- ✓

  Phase arguments convert streaming behavior into counting tokens per chunk (≤ k for ALG, ≥ 1 for OPT), making proofs modular and visualizable.
- ✓

  Potential functions support amortized competitive proofs by bounding (ALG cost + ΔΦ) per step and letting ΔΦ telescope over time.
- ✓

  Interactive step-through simulations (ALG vs OPT, phase boundaries, potential meters) directly mirror the proof structure and improve intuition.

## Common Mistakes

- ✗

  Comparing ALG to OPT step-by-step without acknowledging OPT’s future knowledge; many online proofs must compare via lower bounds, phases, or potential, not local decisions.
- ✗

  Forgetting the additive constant α and claiming a pure multiplicative bound when initialization effects (e.g., empty cache) matter.
- ✗

  Defining phases incorrectly (e.g., ending after k+1 distinct pages rather than before), which breaks the “OPT must miss per boundary” argument.
- ✗

  Using randomization claims without specifying the adversary model (oblivious vs adaptive), which can invalidate the guarantee.

## Practice

medium

Ski Rental variant: Rent costs r per day, buy costs B. Consider the threshold algorithm: rent for ⌈B/r⌉−1 days, then buy. Prove an upper bound on its competitive ratio.

**Hint:** Let m = ⌈B/r⌉. Do a case split on whether D < m. Express OPT(D) = min(rD, B) and compare to ALG(D).

Show solution

Let m = ⌈B/r⌉.

OPT(D) = min(rD, B).

ALG rents for m−1 days and buys on day m if needed.

Case 1: D < m.

ALG(D) = rD = OPT(D), ratio 1.

Case 2: D ≥ m.

ALG(D) = r(m−1) + B.

Since m = ⌈B/r⌉, we have (m−1) < B/r, so r(m−1) < B.

Thus ALG(D) < B + B = 2B = 2·OPT(D) (because OPT(D)=B when D≥m).

So the algorithm is 2-competitive (more tightly, < 2).

easy

Paging warm-up: Let k=2 and consider the request sequence A, B, C, A, B, C, … (repeat). Simulate LRU for the first 9 requests and count misses. What is OPT’s miss count for the same prefix? (You may reason rather than fully compute OPT.)

**Hint:** With k=2, LRU keeps the two most recently used pages. The repeating pattern of 3 distinct pages forces frequent evictions. For OPT, argue a lower bound: cache size 2 cannot hold all 3 pages, so every third request must miss in steady state.

Show solution

LRU simulation (cache shown as most-recently-used order):

1) A miss, cache {A}

2) B miss, cache {B,A}

3) C miss, evict A, cache {C,B}

4) A miss, evict B, cache {A,C}

5) B miss, evict C, cache {B,A}

6) C miss, evict A, cache {C,B}

7) A miss, evict B, cache {A,C}

8) B miss, evict C, cache {B,A}

9) C miss, evict A, cache {C,B}

So LRU misses on all 9 requests.

For OPT with k=2 on a 3-cycle, OPT still must miss frequently because it can only hold 2 of 3 pages. In steady state, at least 1 of each block of 3 requests must miss, giving a lower bound of ≥ 3 misses for 9 requests. In fact, OPT can do no better than 9 as well in this exact alternating-with-3 pattern under k=2? Reason carefully: because every request is to the page not in cache if OPT keeps the other two, OPT will also miss every time. Indeed, whichever 2 pages OPT holds, the next request is the third page at some point, forcing a miss each step in this strict cycle. Thus OPT also has 9 misses on the first 9 requests, so the ratio here is 1.

hard

Phase argument practice: With cache size k, define phases as ‘maximal contiguous blocks containing at most k distinct pages’. Prove: the number of phases P satisfies P−1 ≤ OPT(σ).

**Hint:** Look at two consecutive phases. Show that their union contains at least k+1 distinct pages, and argue that OPT must miss at least once somewhere across the boundary because its cache holds only k pages.

Show solution

Let phases be maximal blocks with ≤ k distinct pages. Consider boundary between phase i and phase i+1. Because phase i is maximal, the first request of phase i+1 is to a page not among the distinct pages of phase i; otherwise, phase i could be extended while still using ≤ k distinct pages.

Therefore, the union of distinct pages in phases i and i+1 has size at least k+1.

OPT’s cache holds only k pages, so it cannot contain all k+1 pages simultaneously at the moments they are requested. Hence, among the requests spanning the boundary (i plus the first request of i+1, and possibly more), OPT must incur at least one miss attributable to the inability to hold all k+1 pages.

Thus each boundary forces ≥ 1 OPT miss. With P phases, there are P−1 boundaries, so P−1 ≤ OPT(σ).

## Connections

Next nodes that commonly build on this:

- •[Amortized Analysis](/tech-tree/amortized-analysis/)
- •[Caching and Replacement Policies](/tech-tree/caching-replacement/)
- •[Randomized Algorithms](/tech-tree/randomized-algorithms/)
- •[Primal-Dual Methods](/tech-tree/primal-dual/)
- •[Online Bipartite Matching](/tech-tree/online-matching/)

Quality: B (4.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
