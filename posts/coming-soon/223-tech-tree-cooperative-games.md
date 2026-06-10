---
title: Cooperative Games
description: Coalition formation, Shapley value. Fair allocation.
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
inspiration_url: https://templeton.host/tech-tree/cooperative-games/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/cooperative-games/](https://templeton.host/tech-tree/cooperative-games/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Cooperative Games

Game TheoryDifficulty: ★★★★★Depth: 5Unlocks: 0

Coalition formation, Shapley value. Fair allocation.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Coalition: an indivisible subset of players that can coordinate and act together
- -Characteristic function (transferable utility): assigns a real total value to every coalition (value of cooperation)
- -Marginal contribution: the incremental value a player adds when joining a specific coalition (v(S union {i}) - v(S))

## Key Symbols & Notation

v (characteristic function mapping coalitions to real numbers)phi\_i (Shapley value - the payoff allocated to player i)

## Essential Relationships

- -Shapley value representation: phi\_i(v) equals the average (expected) marginal contribution of player i over all orderings (permutations) of players

## Prerequisites (2)

[Game Theory Introduction6 atoms](/tech-tree/game-theory-intro/)[Expected Value5 atoms](/tech-tree/expected-value/)

## Referenced by (12)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (12)

[BankruptcyBusiness

The 'bankruptcy problem' (dividing an insufficient estate among creditors with unequal claims) is a canonical example in cooperative game theory; Shapley value and nucleolus provide formal fair-allocation solutions directly applicable to creditor priority and recovery-rate disputes](/business/bankruptcy/)[cost sharingBusiness

Shapley value and coalition theory are the exact mathematical tools for computing fair cost allocations among parties in joint projects, mergers, and shared infrastructure](/business/cost-sharing/)[binding agreementsBusiness

Cooperative game theory is the direct mathematical formalization of binding agreements - characteristic functions define coalition values, the Shapley value allocates pooled payoffs fairly, and the core describes stable allocations no subcoalition would defect from](/business/binding-agreements/)[surplusBusiness

Direct mathematical formalization of surplus division - Shapley value answers exactly 'how should the extra 7 be split' using axiomatic fairness (efficiency, symmetry, additivity, null player)](/business/surplus/)[BargainingBusiness

Nash bargaining solution derives from cooperative game theory axioms (Pareto efficiency, symmetry, IIA) and Shapley value governs coalition surplus division](/business/bargaining/)[consortiumBusiness

Coalition formation and Shapley value directly model consortium economics - which companies join, how to fairly allocate shared infrastructure costs and benefits among members](/business/consortium/)[mergersBusiness

Directly formalizes merger fairness: coalition value functions, Shapley value for fair surplus allocation, and core stability conditions that determine when a merged group holds together vs. splinters](/business/mergers/)[marginal contributionBusiness

Marginal contribution is the foundational primitive of cooperative game theory. The Shapley value is defined as the expected marginal contribution of a player averaged over all coalition orderings.](/business/marginal-contribution/)[Shapley valueBusiness

Shapley value is the central solution concept of cooperative game theory; this node is the direct mathematical foundation for coalition-based fair allocation](/business/shapley-value/)[weighted votingBusiness

Weighted voting games are the canonical example of cooperative games; Shapley value and Banzhaf power index are the solution concepts whose polynomial-time computability is the central question](/business/weighted-voting/)[public goodBusiness

Coalition formation to fund a public good IS cooperative game theory - Shapley value determines each country's fair cost share, core stability determines which coalitions hold together, and the characteristic function maps coalition membership to public good provision levels](/business/public-good/)[Holding CompanyBusiness

Shapley value directly applies to allocating shared services costs and synergy value fairly across portfolio companies - the mathematical framework for answering 'how much of the holdco overhead does each subsidiary bear'](/business/holding-company/)

Advanced Learning Details

### Graph Position

59

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

5

Chain Length

### Cognitive Load

6

Atomic Elements

53

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (21)

- - Cooperative (coalitional) game in characteristic-function form (transferable utility): a model where value can be freely redistributed among members of any coalition and each coalition S has a value v(S)
- - Player set (grand coalition) N and its size n = |N|
- - Coalition: any subset S ⊆ N
- - Characteristic function v: 2^N → R that assigns a worth/value to every coalition S
- - Grand coalition: the coalition N containing all players and its value v(N)
- - Allocation (payoff vector) x ∈ R^n: a proposed division of v(N) among players
- - Imputation: an allocation that is efficient (sums to v(N)) and individually rational (each player's payoff ≥ their singleton value)
- - Efficiency (group rationality): the requirement Σ\_{i∈N} x\_i = v(N)
- - Individual rationality (participation constraint): requirement x\_i ≥ v({i}) for every i
- - Coalitional rationality (no-blocking): requirement that no coalition S can obtain strictly more by splitting off; formalized in core constraints
- - Core of a cooperative game: set of imputations x such that for every coalition S, Σ\_{i∈S} x\_i ≥ v(S) (no coalition can improve)
- - Possibility of an empty core (instability): some games have no allocation satisfying all coalitional constraints
- - Marginal contribution of player i to coalition S: v(S ∪ {i}) − v(S)
- - Shapley value: a specific single-valued allocation rule giving each player a payoff based on average marginal contributions
- - Permutation/ordering interpretation: compute each player's marginal contribution when players join in some order; Shapley value averages over all orders
- - Shapley axioms as normative fairness principles: Efficiency, Symmetry (anonymity), Dummy player property, Additivity
- - Dummy player: a player i with zero marginal contribution to every coalition (v(S∪{i}) = v(S) for all S)
- - Additivity of games: combining two games by pointwise addition of their characteristic functions and the corresponding additive behavior of the Shapley value
- - Balancedness (brief): a property of a game related to weighted covers of coalitions that is necessary and sufficient for a nonempty core (Bondareva–Shapley theorem)
- - Convex (supermodular) cooperative games: games where marginal contributions are increasing with coalition size; convexity implies a nonempty core and that the Shapley value lies in the core
- - Interpretation of Shapley value as a fair allocation rule satisfying the axioms (uniqueness result)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

When cooperation creates value, conflict shifts from “how do we win?” to “how do we split?” Cooperative game theory is the toolkit for turning coalition power into fair, stable allocations—especially when many different groups could form and generate different amounts of value.

TL;DR:

A cooperative (TU) game assigns each coalition S ⊂ N a value v(S). The central question is allocation: choose payoffs (x₁,…,xₙ) that split v(N). The Shapley value φᵢ is a principled “fair” allocation defined as a player’s expected marginal contribution when players join in a random order. It satisfies axioms (efficiency, symmetry, dummy, additivity) and can be computed by averaging marginal contributions across permutations or by a closed-form subset formula.

## What Is a Cooperative Game?

### Why this concept exists (motivation first)

In many real systems, value is produced by **groups**, not isolated individuals:

- •A set of companies shares infrastructure and reduces costs.
- •A team of sensors triangulates a target better than any single sensor.
- •Multiple ML models ensemble to improve accuracy.
- •Countries form trade blocs.

In these settings, the core strategic issue is not “Which action do I pick in a payoff matrix?” but:

1. 1)**Which coalitions can form?**
2. 2)**What value can each coalition create?**
3. 3)**How should we divide the total value of cooperation among individuals?**

Cooperative game theory abstracts away the internal bargaining process and focuses on the *outcome space* of cooperation.

### Players and coalitions

Let N = {1,2,…,n} be the set of players. A **coalition** is any subset S ⊂ N. Think of S as a group that can coordinate and act as a unit.

Two immediate observations:

- •There are 2ⁿ coalitions (including ∅ and N). This combinatorial explosion is why computation becomes hard at difficulty 5.
- •We often care most about the **grand coalition** N, because it typically produces the most total value—but only if the split is acceptable.

### Transferable Utility (TU) and the characteristic function

In a **transferable utility** (TU) cooperative game, coalitions can generate a single real-valued “pie” that can be freely redistributed among coalition members. The game is defined by a **characteristic function**:

- •v: 2ᴺ → ℝ
- •v(S) = total value coalition S can guarantee for itself

Common conventions:

- •v(∅) = 0
- •Sometimes monotonicity is assumed: if S ⊂ T then v(S) ≤ v(T), but this is not required.

Intuition: v(S) is the best total payoff S can secure by coordinating internally (and possibly acting against outsiders).

### The allocation problem

An **allocation** (also called an imputation in some contexts) is a vector x = (x₁,…,xₙ) that assigns each player i a payoff xᵢ.

Two baseline requirements often appear:

1. 1)**Efficiency** (budget balance):

∑ᵢ xᵢ = v(N)

2. 2)**Individual rationality** (participation):

xᵢ ≥ v({i}) for all i

Efficiency says we split the entire grand-coalition value. Individual rationality says nobody should get less than they can guarantee alone.

But these are not enough. There are usually many efficient allocations, and many individually rational ones. We need a principle for fairness and/or stability.

### Marginal contribution as the atomic unit

A central primitive is the **marginal contribution** of player i to a coalition S (not containing i):

- •Δᵢ(S) = v(S ∪ {i}) − v(S)

This measures the incremental value created when i joins S.

Why this matters: any reasonable allocation rule must “pay attention” to contributions across different contexts. A player might be crucial when paired with certain others, and irrelevant elsewhere. Cooperative game theory gives a systematic way to aggregate these context-dependent contributions into a single number φᵢ.

### What cooperative games are *not*

It’s easy to confuse cooperative games with “players cooperate in a matrix game.” Cooperative games (in this TU characteristic-function form) do not specify:

- •A timeline of moves
- •Strategies
- •Detailed bargaining

They specify *coalition values* and then analyze *allocation rules* and *stability concepts* (like the core, which we’ll connect to later).

## Core Mechanic 1: Coalition Values and What “Fair” Could Mean

### Why fairness is tricky

If v(N) is large, you might think forming N is automatic. But if a subgroup S believes it can do better on its own, it can threaten to break away.

That creates two intertwined design goals:

- •**Stability:** no coalition wants to deviate.
- •**Fairness:** allocation reflects contributions in a principled way.

These are not always compatible. Some games have no stable split that satisfies all coalitions (empty core), but still have a well-defined fair split (e.g., Shapley value).

### Superadditivity and synergy

A common (not mandatory) assumption is **superadditivity**:

- •For disjoint S,T ⊂ N: v(S ∪ T) ≥ v(S) + v(T)

This expresses synergy: merging coalitions doesn’t destroy value.

If superadditivity holds broadly, the grand coalition is socially attractive. But even then, the division is contentious.

### The idea of “value created by a player” depends on context

In cooperative games, contributions are not fixed numbers like “player i is worth 5.” Instead:

- •Player i might add a lot to a small coalition but little to a large one.
- •Two players might be substitutes (either one is enough), or complements (both needed).

This is why marginal contribution Δᵢ(S) depends on S.

### A quick contrast of allocation philosophies

Here are some common allocation ideas and why Shapley stands out.

| Approach | Core idea | Upside | Downside |
| --- | --- | --- | --- |
| Equal split | xᵢ = v(N)/n | Simple | Ignores contributions; unfair in asymmetric games |
| Standalone-based | start from v({i}) then split surplus | Respects individual rationality | Still ambiguous; ignores coalition structure |
| Bargaining solutions | model negotiation | Behaviorally grounded | Requires extra assumptions, solution can vary |
| **Shapley value** | average marginal contribution over random arrival orders | Axiomatic fairness; unique under axioms | Computationally heavy for large n; not always stable |

Shapley’s key move is to treat “who joins first” as a source of *symmetry* and average across it.

### The permutation viewpoint (intuition)

Imagine players enter a room one by one in a random order. When player i enters, they join the set of players already present S, and the coalition value increases from v(S) to v(S ∪ {i}).

The increment:

- •v(S ∪ {i}) − v(S)

is credited to i for that arrival order.

Fairness idea: since no arrival order is privileged, we average i’s credited increments over all n! possible orders.

This is exactly the Shapley value.

### The subset-weight viewpoint (how the same idea becomes a formula)

For a fixed player i, each subset S ⊂ N \ {i} can appear as “the set of players who arrived before i” in many permutations.

If |S| = k, then:

- •S’s members can be ordered in k! ways before i
- •the remaining (n − k − 1) players can be ordered after i in (n − k − 1)! ways
- •total permutations: n!

So the probability that “exactly S arrives before i” under a uniform random permutation is:

- •k! (n − k − 1)! / n!

This produces a closed form:

φᵢ(v) = ∑\_{S ⊂ N\{i}} [ |S|! (n − |S| − 1)! / n! ] · ( v(S ∪ {i}) − v(S) )

This is the same averaging idea, just regrouped by subset rather than enumerating permutations.

### What makes an allocation rule convincing?

Shapley value is often taught via axioms because axioms clarify *what kind of fairness you are buying*. The standard axioms are:

1. 1)**Efficiency:** ∑ᵢ φᵢ = v(N)
2. 2)**Symmetry:** if players i and j contribute identically to every coalition, they get the same payoff
3. 3)**Dummy (null player):** if v(S ∪ {i}) = v(S) for all S, then φᵢ = 0
4. 4)**Additivity:** for two games v and w, φᵢ(v + w) = φᵢ(v) + φᵢ(w)

A remarkable theorem (Shapley, 1953): **There is a unique allocation rule satisfying these axioms.** That unique rule is φ.

At difficulty 5, it’s worth pausing on additivity: it says if total value is the sum of two independent “sources” of value, then the allocated payoff should sum as well. This linearity becomes powerful for decomposition and computation, and it’s one reason Shapley shows up in ML feature attribution.

### A short derivation sketch: why the subset weights look like factorials

Let n = |N|. Fix i. Consider a subset S not containing i.

Number of permutations π where S is exactly the set before i:

- •Arrange S before i: |S|!
- •Arrange remaining N \ (S ∪ {i}) after i: (n − |S| − 1)!

So count = |S|! (n − |S| − 1)!

Uniform over n! permutations ⇒ weight:

w(S) = |S|! (n − |S| − 1)! / n!

Then:

φᵢ = ∑\_{S ⊂ N\{i}} w(S) · (v(S ∪ {i}) − v(S))

This shows exactly how combinatorics encodes the “random order” fairness principle.

## Core Mechanic 2: Shapley Value Deep Dive (Axioms, Computation, and Structure)

### Why the axioms matter (before the math)

Many allocation rules sound plausible until you test them against edge cases:

- •What if two players are indistinguishable in every coalition? (symmetry)
- •What if someone adds no value anywhere but still demands a share? (dummy)
- •What if value comes from two independent projects and you’re splitting both at once? (additivity)

The Shapley axioms are designed to remove these ambiguities.

### The Shapley value definition (two equivalent forms)

Let N be the player set, n = |N|.

**Permutation form**

Let Π be the set of all permutations of N. For a permutation π, define Preᵢ(π) as the set of players appearing before i.

Then:

φᵢ(v) = (1 / n!) · ∑\_{π ∈ Π} [ v(Preᵢ(π) ∪ {i}) − v(Preᵢ(π)) ]

**Subset form**

φᵢ(v) = ∑\_{S ⊂ N\{i}} \frac{|S|! (n − |S| − 1)!}{n!} ( v(S ∪ {i}) − v(S) )

### Efficiency proof (showing the work)

A key sanity check: do the φᵢ sum to v(N)? Yes.

Using the permutation form, sum over i:

∑\_{i ∈ N} φᵢ

= ∑\_{i ∈ N} (1/n!) ∑\_{π ∈ Π} [ v(Preᵢ(π) ∪ {i}) − v(Preᵢ(π)) ]

Swap sums:

= (1/n!) ∑\_{π ∈ Π} ∑\_{i ∈ N} [ v(Preᵢ(π) ∪ {i}) − v(Preᵢ(π)) ]

Now fix a permutation π = (i₁,i₂,…,iₙ). The inner sum telescopes:

Let S₀ = ∅

S₁ = {i₁}

S₂ = {i₁,i₂}

…

Sₙ = N

Then the increments are:

v(S₁) − v(S₀)

- •v(S₂) − v(S₁)
- •…
- •v(Sₙ) − v(S\_{n−1})

Telescoping gives:

= v(Sₙ) − v(S₀) = v(N) − v(∅) = v(N)

So for each π, the inner sum equals v(N). Therefore:

∑\_{i ∈ N} φᵢ

= (1/n!) ∑\_{π ∈ Π} v(N)

= (1/n!) · (n!) · v(N)

= v(N)

That’s efficiency.

### Symmetry and dummy (intuitions)

- •**Symmetry:** If i and j have identical marginal contributions for all S, then averaging over orders cannot distinguish them, so φᵢ = φⱼ.
- •**Dummy:** If i never changes v(S), then every marginal term is 0, so φᵢ = 0.

### Additivity (why it’s a big deal)

Suppose v describes profit from “Project A” and w from “Project B”, and the combined situation is (v + w)(S) = v(S) + w(S).

Then for any coalition S:

(v + w)(S ∪ {i}) − (v + w)(S)

= [v(S ∪ {i}) + w(S ∪ {i})] − [v(S) + w(S)]

= [v(S ∪ {i}) − v(S)] + [w(S ∪ {i}) − w(S)]

Averaging preserves sums, so φᵢ(v + w) = φᵢ(v) + φᵢ(w).

This linearity means you can often decompose a complex value function into simpler components (when structure is available), compute Shapley on each, and sum.

### Computational reality: exact Shapley is expensive

The subset formula includes all S ⊂ N\{i}: that’s 2^{n−1} subsets per player, and n players.

- •Naïve exact cost: Θ(n 2ⁿ)

For n = 30, 2ⁿ is already ~1 billion.

So in large systems, people use approximations:

- •**Monte Carlo permutations:** sample K random orders, average marginal contributions.
- •**Structure exploitation:** if v has special form (e.g., weighted voting), compute φ via dynamic programming.

A useful Monte Carlo estimator:

φᵢ ≈ (1/K) ∑\_{k=1}^K [ v(Preᵢ(πₖ) ∪ {i}) − v(Preᵢ(πₖ)) ]

By the law of large numbers, this converges to φᵢ as K grows.

### Weighted voting games (an important class)

A weighted voting game is often written as:

- •players have weights wᵢ ≥ 0
- •quota q
- •coalition S is “winning” if ∑\_{i∈S} wᵢ ≥ q

Characteristic function typically:

v(S) = 1 if S is winning, else 0

Shapley value here becomes the **Shapley–Shubik power index**: the probability a player is pivotal (their addition turns a losing coalition into a winning one) under a random order.

This bridges cooperative games to political science and reliability theory.

### Relation to stability: the core (preview)

The **core** is the set of allocations x such that:

- •∑ᵢ xᵢ = v(N)
- •For all coalitions S: ∑\_{i∈S} xᵢ ≥ v(S)

This says no coalition S can do better by leaving, because the members of S already receive at least v(S) in total.

Shapley value is not guaranteed to lie in the core. When it does, you get an allocation that is both fair (axiomatic) and stable (coalition-proof).

At difficulty 5, it’s helpful to keep the conceptual separation:

- •Shapley: fairness by averaging contributions.
- •Core: stability by blocking deviations.

They answer different “why should I accept this split?” questions.

## Application/Connection: Fair Allocation in Practice (Cost Sharing, Power, and ML Attribution)

### Why cooperative-game allocations show up everywhere

Any time you can measure the value of a group, you can ask how to assign credit or cost:

- •**Cost sharing:** how to split a shared network bill.
- •**Joint ventures:** how to divide profit from collaboration.
- •**Political power:** how much influence a voting member has.
- •**ML explainability:** how to attribute a prediction to features.

The same mathematics appears under different names.

### Cost sharing example (intuition)

Suppose several departments share a cloud contract. Coalition value might represent *savings* compared to buying alone. Then Shapley assigns each department an expected marginal savings contribution, producing a principled discount allocation.

A key modeling step is deciding what v(S) means:

- •v(S) could be negative cost (so higher is better), or
- •v(S) could be “savings” relative to baseline.

The Shapley math works as long as v is consistent; interpretation changes with sign.

### Power in committees: pivotality

In a weighted voting game with v(S) ∈ {0,1}, φᵢ is the probability that i is pivotal in a random order.

This can diverge sharply from weight share. A player with moderate weight can have outsized power if they frequently “complete” winning coalitions.

### ML connection: Shapley as feature attribution

In many ML explanation methods (e.g., SHAP), features are treated like “players,” and v(S) is the model’s expected prediction when only features in S are “present.” Then:

- •φᵢ ≈ contribution of feature i to the prediction

The axioms (efficiency, symmetry, dummy, additivity) become desiderata for explanations:

- •Efficiency: contributions sum to the difference between prediction and baseline.
- •Dummy: irrelevant features get 0.

This is not a coincidence: SHAP is explicitly built from Shapley values.

### Choosing between fairness and stability (when they conflict)

In some applications, you might prioritize:

- •**Fairness:** choose Shapley even if some coalition could object.
- •**Stability:** choose a core allocation (if core is nonempty), even if it deviates from Shapley.

A practical perspective:

| Goal | Typical tool | Question answered |
| --- | --- | --- |
| Fair split by contribution | Shapley value | “What is each participant’s expected marginal impact?” |
| No coalition wants to leave | Core (or nucleolus) | “Can any subgroup do better by breaking away?” |
| Both | Shapley-in-the-core (when possible) | “Is there a split that is fair *and* stable?” |

### Modeling warnings (what can break the interpretation)

- •TU assumes the coalition’s value is a transferable scalar. Some settings have nontransferable utility (NTU), requiring different tools.
- •v(S) must reflect *what S can do on its own*. If it instead reflects something like “market value with outsiders cooperating,” the stability interpretation changes.
- •In ML, the definition of “feature missing” is subtle; different baselines change v(S), changing φ.

### Where this node fits in the tech tree

Cooperative games sit at a crossroads:

- •From basic game theory, you bring rational agents and incentives.
- •From probability/expected value, you bring averaging over random orders.
- •Next, you can branch into stability concepts (core), solution refinements (nucleolus), computational methods, or ML explanation frameworks.

A useful mental model: **Shapley is expected marginal contribution under a symmetry assumption (random order).** If you remember that, you can re-derive the formulas whenever needed.

## Worked Examples (3)

### Compute Shapley values in a 3-player synergy game

Let N = {1,2,3}. Define v(∅)=0 and:

- •v({1})=1, v({2})=1, v({3})=0
- •v({1,2})=3, v({1,3})=1, v({2,3})=1
- •v({1,2,3})=4

Compute φ₁, φ₂, φ₃.

1. List all permutations of (1,2,3):

   (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1).
2. For each permutation, compute each player’s marginal contribution when they arrive.

   Permutation (1,2,3):

   - •Player 1 joins ∅: v({1})−v(∅)=1−0=1
   - •Player 2 joins {1}: v({1,2})−v({1})=3−1=2
   - •Player 3 joins {1,2}: v({1,2,3})−v({1,2})=4−3=1

   Permutation (1,3,2):

   - •1 joins ∅: 1
   - •3 joins {1}: v({1,3})−v({1})=1−1=0
   - •2 joins {1,3}: v({1,2,3})−v({1,3})=4−1=3

   Permutation (2,1,3):

   - •2 joins ∅: v({2})−0=1
   - •1 joins {2}: v({1,2})−v({2})=3−1=2
   - •3 joins {1,2}: 4−3=1

   Permutation (2,3,1):

   - •2 joins ∅: 1
   - •3 joins {2}: v({2,3})−v({2})=1−1=0
   - •1 joins {2,3}: v({1,2,3})−v({2,3})=4−1=3

   Permutation (3,1,2):

   - •3 joins ∅: v({3})−0=0
   - •1 joins {3}: v({1,3})−v({3})=1−0=1
   - •2 joins {1,3}: 4−1=3

   Permutation (3,2,1):

   - •3 joins ∅: 0
   - •2 joins {3}: v({2,3})−v({3})=1−0=1
   - •1 joins {2,3}: 4−1=3
3. Average each player’s marginal contributions across the 6 permutations.

   Player 1 contributions: 1, 1, 2, 3, 1, 3

   Sum = 11 ⇒ φ₁ = 11/6

   Player 2 contributions: 2, 3, 1, 1, 3, 1

   Sum = 11 ⇒ φ₂ = 11/6

   Player 3 contributions: 1, 0, 1, 0, 0, 0

   Sum = 2 ⇒ φ₃ = 2/6 = 1/3
4. Sanity check efficiency:

   φ₁+φ₂+φ₃ = 11/6 + 11/6 + 1/3

   = 22/6 + 2/6

   = 24/6

   = 4 = v(N).

**Insight:** Players 1 and 2 are symmetric and share the large complementarity (the jump from 1+1 to 3). Player 3 adds value only when joining {1,2}, so it receives a smaller share even though it is needed to reach v(N)=4.

### Shapley–Shubik power index in a weighted voting game

Let N={A,B,C}. Weights: w\_A=2, w\_B=1, w\_C=1. Quota q=3. Define v(S)=1 if total weight ≥3 else 0. Compute Shapley values (power indices).

1. Enumerate permutations (A,B,C), (A,C,B), (B,A,C), (B,C,A), (C,A,B), (C,B,A).
2. A player is pivotal if adding them turns the running coalition from losing (0) to winning (1). Track cumulative weights.

   Permutation (A,B,C):

   - •Start 0
   - •Add A (2): still losing (2<3) ⇒ A not pivotal
   - •Add B (+1 →3): winning ⇒ B pivotal
   - •Add C: already winning ⇒ C not pivotal

   Permutation (A,C,B):

   - •Add A (2): losing ⇒ A not pivotal
   - •Add C (+1→3): winning ⇒ C pivotal
   - •Add B: not pivotal

   Permutation (B,A,C):

   - •Add B (1): losing
   - •Add A (+2→3): winning ⇒ A pivotal

   Permutation (B,C,A):

   - •Add B (1): losing
   - •Add C (+1→2): losing
   - •Add A (+2→4): winning ⇒ A pivotal

   Permutation (C,A,B):

   - •Add C (1): losing
   - •Add A (+2→3): winning ⇒ A pivotal

   Permutation (C,B,A):

   - •Add C (1): losing
   - •Add B (+1→2): losing
   - •Add A (+2→4): winning ⇒ A pivotal
3. Count pivotal events:

   - •A pivotal in 4 permutations
   - •B pivotal in 1 permutation
   - •C pivotal in 1 permutation
4. Convert to Shapley values by dividing by 6:

   φ\_A = 4/6 = 2/3

   φ\_B = 1/6

   φ\_C = 1/6
5. Interpretation:

   Even though A has only half the total weight (2 out of 4), it has 2/3 of the power because it frequently completes a winning coalition.

**Insight:** In voting games, Shapley value measures pivotal probability, not weight share. Power depends on how often you are the “swing” member across coalition-building orders.

### Compute Shapley via the subset-weight formula (n=4) with structured v

Let N={1,2,3,4}. Define v(S)=|S|² (so value depends only on coalition size). Compute φ₁ (and infer all φᵢ by symmetry).

1. By symmetry, all players must have equal Shapley value:

   φ₁=φ₂=φ₃=φ₄.

   So if we find one, we get all.
2. Compute v(N)=v({1,2,3,4})=4²=16.

   Efficiency requires:

   φ₁+φ₂+φ₃+φ₄=16

   ⇒ 4φ₁=16

   ⇒ φ₁=4.

   So each player gets 4.
3. Verify directly using subset formula for player 1 as a consistency check.

   Here n=4. Consider S ⊂ {2,3,4}.

   We need weights w(S)=|S|!(3−|S|)!/4! and marginal Δ₁(S)=v(S∪{1})−v(S).

   Case |S|=0: S=∅

   w=0!·3!/24=6/24=1/4

   Δ=1²−0²=1

   Contribution: 1/4·1=1/4

   Case |S|=1: there are 3 such S

   w=1!·2!/24=2/24=1/12

   For any |S|=1:

   Δ=(2²−1²)=(4−1)=3

   Total from all size-1 sets:

   3 sets · (1/12·3)=3·(3/12)=9/12=3/4

   Case |S|=2: there are 3 such S

   w=2!·1!/24=2/24=1/12

   Δ=(3²−2²)=(9−4)=5

   Total:

   3 · (1/12·5)=15/12=5/4

   Case |S|=3: S={2,3,4}

   w=3!·0!/24=6/24=1/4

   Δ=(4²−3²)=(16−9)=7

   Contribution: 1/4·7=7/4
4. Sum contributions:

   φ₁ = 1/4 + 3/4 + 5/4 + 7/4

   = (1+3+5+7)/4

   = 16/4

   = 4

**Insight:** When v(S) depends only on coalition size, symmetry plus efficiency almost solves the game instantly. The subset formula then acts as a check, and it reveals a pattern: Shapley averages the increments from sizes 0→1→2→3→4.

## Key Takeaways

- ✓

  A TU cooperative game is defined by a characteristic function v: 2ᴺ → ℝ that assigns a total value to every coalition S ⊂ N.
- ✓

  The marginal contribution Δᵢ(S)=v(S ∪ {i})−v(S) is the basic local notion of “what i adds,” but it depends on context S.
- ✓

  The Shapley value φᵢ is the expected marginal contribution of player i under a uniformly random arrival order of players.
- ✓

  Shapley’s subset formula weights each S ⊂ N\{i} by |S|!(n−|S|−1)!/n!, the probability S is exactly the set arriving before i.
- ✓

  Shapley value is uniquely characterized by efficiency, symmetry, dummy, and additivity axioms.
- ✓

  Exact Shapley computation is Θ(n2ⁿ) in general; Monte Carlo over random permutations is a common scalable approximation.
- ✓

  In weighted voting games, Shapley value equals the probability of being pivotal (Shapley–Shubik power index), which can differ dramatically from weight share.
- ✓

  Fairness (Shapley) and stability (core) are different objectives; Shapley need not lie in the core.

## Common Mistakes

- ✗

  Confusing cooperative TU games with “cooperation” inside a normal-form payoff matrix; TU games summarize coalition capabilities via v(S).
- ✗

  Treating marginal contribution as a single number per player; in reality Δᵢ(S) varies with S and must be aggregated.
- ✗

  Forgetting efficiency: any claimed Shapley vector must satisfy ∑ᵢ φᵢ = v(N).
- ✗

  Assuming Shapley allocations are always stable (in the core); they are fairness-based and may be blocked by some coalition.

## Practice

medium

Let N={1,2,3}. Define v(∅)=0, v({1})=0, v({2})=0, v({3})=0, v({1,2})=0, v({1,3})=2, v({2,3})=2, v({1,2,3})=2. Compute (φ₁,φ₂,φ₃).

**Hint:** Use the permutation definition. In each order, only the player who completes a coalition containing player 3 with one of {1,2} may create value; check each arrival order carefully.

Show solution

List permutations and marginal contributions.

(1,2,3):

- •1: v({1})−v(∅)=0
- •2: v({1,2})−v({1})=0
- •3: v({1,2,3})−v({1,2})=2−0=2

(1,3,2):

- •1: 0
- •3: v({1,3})−v({1})=2−0=2
- •2: v({1,2,3})−v({1,3})=2−2=0

(2,1,3):

- •2: 0
- •1: 0
- •3: 2

(2,3,1):

- •2: 0
- •3: v({2,3})−v({2})=2
- •1: 2−2=0

(3,1,2):

- •3: v({3})−0=0
- •1: v({1,3})−v({3})=2−0=2
- •2: 2−2=0

(3,2,1):

- •3: 0
- •2: v({2,3})−v({3})=2
- •1: 2−2=0

Average contributions:

φ₁: (0+0+0+0+2+0)/6 = 2/6 = 1/3

φ₂: (0+0+0+0+0+2)/6 = 2/6 = 1/3

φ₃: (2+2+2+2+0+0)/6 = 8/6 = 4/3

Check: 1/3+1/3+4/3 = 2 = v(N).

easy

Show using the permutation (telescoping) argument that for any TU game with v(∅)=0, the Shapley values satisfy efficiency: ∑ᵢ φᵢ = v(N).

**Hint:** Fix a permutation π=(i₁,…,iₙ). Write the running coalitions S₀=∅, S₁={i₁}, …, Sₙ=N, and sum the increments v(S\_k)−v(S\_{k−1}).

Show solution

By definition:

φᵢ = (1/n!) ∑\_{π∈Π} [v(Preᵢ(π)∪{i}) − v(Preᵢ(π))].

Sum over i and swap sums:

∑ᵢ φᵢ = (1/n!) ∑\_{π∈Π} ∑ᵢ [v(Preᵢ(π)∪{i}) − v(Preᵢ(π))].

For a fixed π=(i₁,…,iₙ), define S\_k={i₁,…,i\_k}. Then the inner sum equals:

[v(S₁)−v(S₀)] + [v(S₂)−v(S₁)] + … + [v(Sₙ)−v(S\_{n−1})]

which telescopes to v(Sₙ)−v(S₀)=v(N)−v(∅)=v(N).

Therefore:

∑ᵢ φᵢ = (1/n!) ∑\_{π∈Π} v(N) = v(N).

hard

Weighted voting game: N={A,B,C,D}, weights (2,2,1,1), quota q=4, v(S)∈{0,1}. Compute the Shapley–Shubik index for player A.

**Hint:** Use pivotal probability. Instead of listing all 24 permutations blindly, count when A is pivotal by looking at the total weight of players before A. A is pivotal when the weight before A is <4 but becomes ≥4 after adding A’s weight 2.

Show solution

A is pivotal iff the weight before A is in {2,3}:

- •If weight before A is 0 or 1: adding 2 gives 2 or 3 (still losing).
- •If weight before A is 2: adding 2 gives 4 (winning).
- •If weight before A is 3: adding 2 gives 5 (winning).
- •If weight before A is ≥4: already winning.

Players other than A: {B,C,D} with weights 2,1,1.

Possible subsets before A and their weights:

- •{B}: weight 2
- •{C,D}: weight 2
- •{B,C}: weight 3
- •{B,D}: weight 3

Count permutations where each subset S is exactly before A.

For n=4, if |S|=k, number of permutations with exactly S before A is k!(3−k)!.

Compute:

1) S={B}, k=1 ⇒ count = 1!·2! = 2

2) S={C,D}, k=2 ⇒ count = 2!·1! = 2

3) S={B,C}, k=2 ⇒ count = 2

4) S={B,D}, k=2 ⇒ count = 2

Total pivotal permutations for A = 2+2+2+2 = 8.

Total permutations = 4! = 24.

So φ\_A = 8/24 = 1/3.

## Connections

Next nodes you can study:

- •[Nash Equilibrium](/tech-tree/nash-equilibrium/) (contrast noncooperative stability with cooperative allocation)
- •[The Core of a Cooperative Game](/tech-tree/core-cooperative-games/) (coalition-proof stability)
- •[Nucleolus](/tech-tree/nucleolus/) (stability-oriented “most balanced” allocation)
- •[Mechanism Design Basics](/tech-tree/mechanism-design-basics/) (design incentives rather than just analyze splits)
- •[Shapley Values in ML (SHAP)](/tech-tree/shapley-ml/) (feature attribution and expected marginal contributions)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
