---
title: Zero-Sum Games
description: One player's gain is another's loss. Minimax theorem.
date: '2026-07-01'
scheduled: '2026-11-24'
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
inspiration_url: https://templeton.host/tech-tree/zero-sum-games/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/zero-sum-games/](https://templeton.host/tech-tree/zero-sum-games/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Zero-Sum Games

Game TheoryDifficulty: ★★★★☆Depth: 8Unlocks: 1

One player's gain is another's loss. Minimax theorem.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Zero-sum payoff structure: the game is captured by a single payoff (one player's gain equals the other's loss).
- -Mixed strategies and expected payoff: players may randomize and payoffs are evaluated by the expected value under strategy probability distributions.
- -Value and optimality (minimax/saddle point): the game has a value v and there exist strategies that guarantee at least (row) or at most (column) that value.

## Key Symbols & Notation

A (payoff matrix; A\_ij is payoff to Row, Column's payoff = -A\_ij)

## Essential Relationships

- -Expected payoff under mixed strategies is p^T A q, and the minimax theorem states max\_p min\_q p^T A q = min\_q max\_p p^T A q = v, with optimal strategies securing that value.

## Prerequisites (2)

[Nash Equilibrium5 atoms](/tech-tree/nash-equilibrium/)[Linear Programming6 atoms](/tech-tree/linear-programming/)

## Unlocks (1)

[Generative Adversarial Networkslvl 5](/tech-tree/gan/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[Zero-sum GameBusiness

Direct mathematical formalization: minimax theorem, saddle points, and proof that optimal mixed strategies exist for all finite zero-sum games](/business/zero-sum-game/)

Advanced Learning Details

### Graph Position

117

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

8

Chain Length

### Cognitive Load

5

Atomic Elements

31

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (13)

- - Zero-sum game: a strategic game in which the sum of players' payoffs is zero for every outcome (one player's gain equals the other's loss).
- - Single payoff-matrix representation for two-player zero-sum games: a matrix A encoding the row player's payoffs, with the column player's payoffs given by -A.
- - Mixed strategy as a probability vector specific to zero-sum analysis: row-player vector p and column-player vector q over pure actions.
- - Expected payoff of mixed strategies: the scalar p^T A q giving the row player's expected payoff (and -p^T A q for the column player).
- - Value of the game (v): the guaranteed expected payoff both players can secure when playing optimal (possibly mixed) strategies.
- - Maximin strategy (row player): a strategy that maximizes the minimum expected payoff the row player can guarantee.
- - Minimax strategy (column player): a strategy that minimizes the maximum expected payoff the row player can obtain (equivalently maximizes the column player's guarantee when payoffs negated).
- - Saddle point (in pure or mixed strategies): a strategy pair that simultaneously attains the maximin and minimax payoffs; it yields the game's value.
- - Security level (guarantee): the payoff level a player can force regardless of the opponent's actions (the player's maximin/minimax value).
- - Minimax theorem (von Neumann): the theorem that max\_p min\_q p^T A q = min\_q max\_p p^T A q and that optimal mixed strategies achieving this equality exist.
- - Interchangeability and uniqueness-of-value property: although multiple equilibria (strategy pairs) may exist, they all yield the same game value v and can be interchanged without changing expected payoff.
- - Support-property of optimal mixes: in an optimal mixed strategy, every pure action assigned positive probability yields the same expected payoff (otherwise probability could be shifted).
- - Relation to linear programming for computation: optimal mixed strategies and the value can be computed by solving a pair of dual linear programs (LP formulation tailored to zero-sum structure).

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Many competitive situations feel like tug-of-war: every point you gain is a point your opponent loses. Zero-sum games are the mathematical model of that intuition—and the minimax theorem tells you exactly what “playing optimally” means when both sides are smart and adversarial.

TL;DR:

A zero-sum game can be represented by a single payoff matrix A where Row receives Aᵢⱼ and Column receives −Aᵢⱼ. Players may use mixed strategies (probability distributions over actions). The minimax theorem guarantees the game has a value v and optimal strategies (**p**, **q**) such that maxₚ min\_q **p**ᵀA**q** = min\_q maxₚ **p**ᵀA**q** = v. Finding optimal strategies is equivalent to solving a linear program (and its dual).

## What Is a Zero-Sum Game?

### Why this concept exists

Game theory has many types of interaction: cooperation, coordination, bargaining, and pure competition. Zero-sum games isolate the **pure competition** part.

In a zero-sum game, the players’ interests are perfectly opposed: whatever Row gains, Column loses by the same amount. That makes the analysis unusually clean: there is a single notion of “the payoff,” and strategic reasoning becomes a search for **guarantees** rather than compromise.

### Formal definition (matrix form)

A **finite two-player zero-sum game** is specified by a payoff matrix A ∈ ℝ^(m×n).

- •Row chooses an action i ∈ {1,…,m}
- •Column chooses an action j ∈ {1,…,n}
- •Row’s payoff is Aᵢⱼ
- •Column’s payoff is −Aᵢⱼ

So the game is “captured by one matrix.” If you know A, you know both players’ payoffs.

### Pure strategies vs mixed strategies

A **pure strategy** is a single action (choose i deterministically).

A **mixed strategy** is a probability distribution over actions:

- •Row’s mixed strategy: **p** ∈ ℝ^m with pᵢ ≥ 0 and ∑ᵢ pᵢ = 1
- •Column’s mixed strategy: **q** ∈ ℝ^n with qⱼ ≥ 0 and ∑ⱼ qⱼ = 1

We’ll write these sets as simplices:

- •Δ\_m = { **p** : **p** ≥ 0, ∑ᵢ pᵢ = 1 }
- •Δ\_n = { **q** : **q** ≥ 0, ∑ⱼ qⱼ = 1 }

### Expected payoff under randomization

If Row plays **p** and Column plays **q**, the expected payoff to Row is

E[payoff] = ∑ᵢ ∑ⱼ pᵢ Aᵢⱼ qⱼ = **p**ᵀA**q**.

This bilinear form **p**ᵀA**q** is the central object of zero-sum theory.

### Intuition: adversarial uncertainty

A key mindset shift is this:

- •In probabilistic modeling, uncertainty might be “nature.”
- •In zero-sum games, uncertainty is often an **opponent** trying to hurt you.

So instead of maximizing expected value against a fixed distribution, you often maximize a **worst-case** expected value.

That leads directly to minimax reasoning.

## Core Mechanic 1: Mixed Strategies and Expected Payoff

### Why randomize at all?

If you play deterministically in an adversarial setting, you can become predictable—and predictability can be exploited.

Classic example: Rock–Paper–Scissors has no good pure strategy. Any pure move can be countered for a loss. Randomization is not “noise”; it is a **strategic tool**.

### Expected payoff as a weighted average

Fix Row’s mixed strategy **p**. Consider what happens against each pure column j. The expected payoff if Column plays pure j is

uⱼ(**p**) = ∑ᵢ pᵢ Aᵢⱼ.

This can be seen as the j-th component of the vector **p**ᵀA.

Similarly, fix Column’s mixed strategy **q**. Against Row’s pure i, the expected payoff is

wᵢ(**q**) = ∑ⱼ Aᵢⱼ qⱼ,

i.e., the i-th component of A**q**.

Now if both mix, the expected payoff is the average of these:

**p**ᵀA**q** = ∑ⱼ qⱼ (∑ᵢ pᵢ Aᵢⱼ) = ∑ⱼ qⱼ uⱼ(**p**).

### Best responses in a zero-sum setting

Given Column plays **q**, Row chooses **p** to maximize **p**ᵀA**q**.

But for any fixed **q**, the function **p** ↦ **p**ᵀA**q** is linear in **p**. Linear functions over a simplex achieve maxima at extreme points. That means:

- •A best response to **q** is always achievable by a **pure** row i that maximizes (A**q**)ᵢ.

Similarly, a best response to **p** for Column (who wants to minimize Row’s payoff) can be taken as a pure column j that minimizes (**p**ᵀA)ⱼ.

So why do we need mixed strategies if best responses are pure? Because the equilibrium concept is not “best response to a fixed opponent strategy,” but “mutually stable.” The stability can require mixing so that the opponent becomes indifferent among multiple pure best responses.

### Dominated strategies (a quick pruning tool)

A row i is **strictly dominated** by row k if

Aᵢⱼ < A\_kⱼ for all j.

Then Row should never play i (it is worse regardless of Column’s choice). Similarly, Column can delete dominated columns.

This matters because it can reduce the game size before you do heavier computation (LP or solving equations).

### Geometric intuition: mixing as hedging

Think of each pure row i as a vector of payoffs across columns: (Aᵢ1, …, Aᵢn). When Row mixes, **p** forms a convex combination of these vectors.

- •The set { **p**ᵀA : **p** ∈ Δ\_m } is the convex hull of the row payoff vectors.

Row can choose a point in this convex set; Column then picks the coordinate (a column) that hurts Row most. Row’s problem becomes: pick a convex combination that maximizes the minimum coordinate.

That is already “minimax” in geometric clothing.

## Core Mechanic 2: Value, Saddle Points, and the Minimax Theorem

### Why “value” matters

In many non-zero-sum games, equilibrium can mean multiple outcomes, negotiation, and mutual gain. In a zero-sum game, optimal play has a sharper promise:

- •Row can guarantee a certain payoff no matter what Column does.
- •Column can guarantee Row does not exceed a certain payoff no matter what Row does.

If these guarantees meet, the meeting point is the **value of the game**.

### Maximin and minimax quantities

Define Row’s guaranteed payoff (maximin):

v\_maximin = max\_{**p**∈Δ\_m} min\_{**q**∈Δ\_n} **p**ᵀA**q**.

Interpretation:

1) Row chooses **p** first.

2) Column, knowing **p**, chooses **q** to minimize Row’s payoff.

3) Row selects **p** to maximize the resulting worst-case.

Define Column’s guaranteed bound (minimax):

v\_minimax = min\_{**q**∈Δ\_n} max\_{**p**∈Δ\_m} **p**ᵀA**q**.

Interpretation:

1) Column chooses **q** first.

2) Row responds to maximize payoff.

3) Column chooses **q** to make that best-case as small as possible.

A general inequality always holds:

max\_{**p**} min\_{**q**} **p**ᵀA**q** ≤ min\_{**q**} max\_{**p**} **p**ᵀA**q**.

Why? Because for any fixed (**p**, **q**):

min\_{**q**} **p**ᵀA**q** ≤ **p**ᵀA**q** ≤ max\_{**p**} **p**ᵀA**q**

and taking max on the left expression and min on the right preserves the inequality.

So Row’s guarantee can’t exceed Column’s guarantee. The miracle is that in finite zero-sum games, they are actually equal.

### Saddle points (pure and mixed)

A **saddle point** is a strategy pair (**p**⋆, **q**⋆) such that

**p**ᵀA**q**⋆ ≤ (**p**⋆)ᵀA**q**⋆ ≤ (**p**⋆)ᵀA**q**

for all **p** ∈ Δ\_m and **q** ∈ Δ\_n.

Interpretation:

- •Given **q**⋆, Row cannot improve by deviating from **p**⋆.
- •Given **p**⋆, Column cannot reduce Row’s payoff by deviating from **q**⋆.

In a zero-sum game, a saddle point is exactly a Nash equilibrium (for the two-player zero-sum setting) because one player’s utility is the negative of the other’s.

If the saddle point occurs at pure strategies (i⋆, j⋆), then A\_{i⋆j⋆} is simultaneously:

- •the minimum in Row i⋆ across columns
- •the maximum in Column j⋆ across rows

This is sometimes called a **pure saddle point**.

### The minimax theorem (von Neumann)

For finite two-player zero-sum games:

max\_{**p**∈Δ\_m} min\_{**q**∈Δ\_n} **p**ᵀA**q** = min\_{**q**∈Δ\_n} max\_{**p**∈Δ\_m} **p**ᵀA**q** = v.

Moreover, there exist optimal mixed strategies (**p**⋆, **q**⋆) achieving this value v.

This theorem does three jobs at once:

1) **Existence**: an equilibrium in mixed strategies exists.

2) **Equality of guarantees**: the order of max and min can be swapped.

3) **Operational meaning**: v is the payoff under optimal play.

### Interpreting v

- •If v > 0, Row has an advantage: Row can force positive expected payoff.
- •If v < 0, Column has an advantage: Column can force Row’s payoff negative.
- •If v = 0, the game is “fair” under optimal play.

### Indifference principle (useful equilibrium property)

At equilibrium, any pure strategy used with positive probability must be a best response.

Concretely:

- •If Row’s equilibrium mix **p**⋆ assigns pᵢ⋆ > 0 to row i, then that row must achieve the same expected payoff v against **q**⋆ (otherwise Row would shift probability mass).
- •If Column’s equilibrium mix **q**⋆ assigns qⱼ⋆ > 0 to column j, then that column must yield the same expected payoff v against **p**⋆ (otherwise Column would shift mass).

This gives a practical method for small games: set certain expected payoffs equal and solve.

## Core Mechanic 3: Solving Zero-Sum Games via Linear Programming (and Duality)

### Why LP shows up here

The minimax theorem is not only about existence—it’s computational.

Row’s problem is:

maximize\_{**p**∈Δ\_m} min\_{j} ∑ᵢ pᵢ Aᵢⱼ

because Column’s best response to **p** can be taken as a pure column j that minimizes (**p**ᵀA)ⱼ.

That “maximize a minimum of linear functions” can be converted into an LP by introducing a variable v representing the guaranteed payoff.

### Row player LP (primal)

Row wants the largest v such that every column j gives expected payoff ≥ v.

Variables: **p** ∈ ℝ^m, v ∈ ℝ

LP:

maximize v

subject to

- •∑ᵢ pᵢ Aᵢⱼ ≥ v for all columns j = 1,…,n
- •∑ᵢ pᵢ = 1
- •pᵢ ≥ 0 for all i

This is linear because v appears linearly and constraints are linear inequalities.

### Column player LP (dual perspective)

Similarly, Column wants to minimize Row’s payoff. Column chooses **q** to make every row’s expected payoff ≤ v.

Variables: **q** ∈ ℝ^n, v ∈ ℝ

minimize v

subject to

- •∑ⱼ Aᵢⱼ qⱼ ≤ v for all rows i = 1,…,m
- •∑ⱼ qⱼ = 1
- •qⱼ ≥ 0 for all j

The minimax theorem corresponds to strong duality: both LPs share the same optimal value v.

### Making the LP look “standard”

Some textbooks require A to be strictly positive to avoid sign issues when transforming to canonical forms. Practically, you can always shift payoffs by a constant c:

A' = A + c·1·1ᵀ

where 1 is the all-ones vector. Then

**p**ᵀA'**q** = **p**ᵀA**q** + c

So the optimal strategies (**p**⋆, **q**⋆) do not change, and the value shifts by +c.

This is a useful trick when converting to alternative LP formulations (like minimizing ∑ xᵢ subject to Aᵀ**x** ≥ 1).

### Complementary slackness = equilibrium structure

At optimality:

- •If Column assigns qⱼ⋆ > 0, then the corresponding constraint for Row is tight:

∑ᵢ pᵢ⋆ Aᵢⱼ = v.

- •If Row assigns pᵢ⋆ > 0, then the corresponding constraint for Column is tight:

∑ⱼ Aᵢⱼ qⱼ⋆ = v.

This matches the indifference principle: actions in the support of a mixed strategy yield equal expected payoff.

### Practical comparison: methods to solve

| Method | Best for | How it works | Tradeoffs |
| --- | --- | --- | --- |
| Indifference / solving equations | 2×2, small 3×3 | Make opponent indifferent across support | Requires guessing support; fragile at scale |
| Dominated strategy elimination | Preprocessing | Remove rows/cols that are never optimal | Not always applicable |
| Linear programming | General finite games | Solve Row’s LP or Column’s LP | Needs LP solver; numerical considerations |
| Specialized algorithms (e.g., simplex variants, subgradient) | Larger games | Exploit structure / sparsity | More advanced |

Since you already know LP, the key conceptual leap is: **“optimal play” is an LP feasibility + optimization problem.**

## Application/Connection: From Zero-Sum Games to GANs (Minimax in ML)

### Why this matters beyond game theory

Zero-sum games formalize adversarial optimization: one side tries to minimize a quantity while the other tries to maximize it. That pattern appears in:

- •Robust optimization (model vs worst-case perturbation)
- •Security (defender vs attacker)
- •Online learning (learner vs adversary)
- •Generative Adversarial Networks (generator vs discriminator)

### GANs as a minimax game (high-level)

In a vanilla GAN, we have two models:

- •Generator G: produces fake samples
- •Discriminator D: tries to distinguish real from fake

Training is often written as

min\_G max\_D V(D, G)

This is not always a strict zero-sum game in the clean matrix sense (continuous strategies, non-convex objectives, approximation, etc.), but the *conceptual* backbone is minimax: one player improves by making the other worse.

### What transfers directly from zero-sum theory

1) **Value thinking**: Instead of “did my loss go down,” ask “what can I guarantee against an improving opponent?”

2) **Mixed strategies as distributions**: In GANs, stochasticity and diversity in generation can be understood as mixing over outputs; in more theoretical treatments, one may consider mixed strategies over model parameters.

3) **No-regret dynamics → equilibrium** (preview idea): In many zero-sum settings, if both sides use algorithms with vanishing regret, the time-averaged strategies converge to minimax equilibrium. This is a bridge to modern ML training dynamics.

### What does *not* transfer cleanly

- •Finite matrix games are convex–concave; deep networks are not.
- •Minimax theorem relies on compactness/convexity assumptions that fail in many ML parameterizations.

Still, the zero-sum framework gives you the correct mental model for adversarial objectives: equilibrium is about **balance**, not unilateral improvement.

### A useful habit: write the payoff explicitly

Whenever you see “minimize a loss that depends on an adversary,” try to rewrite it as:

payoff = **p**ᵀA**q** (finite case)

or more generally as an expectation under two distributions. Then ask:

- •What is the maximizing player’s best response?
- •What is the minimizing player’s best response?
- •Is there a value v? Under what assumptions?

That’s the zero-sum mindset you’ll reuse in GANs and robust ML.

## Worked Examples (3)

### Example 1: Solve a 2×2 zero-sum game by indifference (find \*\*p\*\*⋆, \*\*q\*\*⋆, and v)

Payoff matrix to Row:

A = [ [ 2, −1 ],

[ 0, 1 ] ]

Row chooses a row; Column chooses a column. Column’s payoff is the negative.

1. Let Row mix: **p** = (p, 1−p). Column will choose the column that minimizes Row’s expected payoff.
2. Compute expected payoff if Column plays column 1:

   u₁(p) = p·2 + (1−p)·0

   = 2p
3. Compute expected payoff if Column plays column 2:

   u₂(p) = p·(−1) + (1−p)·1

   = −p + 1 − p

   = 1 − 2p
4. Row wants to maximize min(u₁(p), u₂(p)). The best p occurs where the two are equal (so Column is indifferent):

   2p = 1 − 2p

   4p = 1

   p = 1/4
5. So Row’s optimal mix is **p**⋆ = (1/4, 3/4). The value is the common payoff:

   v = 2p = 2·(1/4) = 1/2

   (check: 1 − 2p = 1 − 1/2 = 1/2).
6. Now solve for Column’s mix **q** = (q, 1−q) by making Row indifferent between rows (since Row must be willing to randomize):
7. Expected payoff of Row choosing row 1 against **q**:

   r₁(q) = 2q + (−1)(1−q)

   = 2q − 1 + q

   = 3q − 1
8. Expected payoff of Row choosing row 2 against **q**:

   r₂(q) = 0·q + 1·(1−q)

   = 1 − q
9. Indifference: r₁(q) = r₂(q)

   3q − 1 = 1 − q

   4q = 2

   q = 1/2
10. Thus Column’s optimal mix is **q**⋆ = (1/2, 1/2). Verify value:

    (**p**⋆)ᵀA**q**⋆ = 1/2.

**Insight:** In a 2×2 zero-sum game without a pure saddle point, optimal mixing makes the opponent indifferent across the actions they might choose. Equilibrium equalizes payoffs on the support.

### Example 2: Detect a pure saddle point (no mixing needed)

Payoff matrix to Row:

A = [ [ 3, 1, 2 ],

[ 4, 0, −1 ],

[ 2, 2, 1 ] ]

1. Compute Row’s minimum payoff in each row (Row assumes Column will pick the worst column):

   Row 1 min = min(3,1,2) = 1

   Row 2 min = min(4,0,−1) = −1

   Row 3 min = min(2,2,1) = 1
2. Row’s maximin over pure rows is max(1, −1, 1) = 1. Candidate rows: row 1 or row 3.
3. Compute Column’s maximum payoff (to Row) in each column (Column assumes Row will pick the best row):

   Col 1 max = max(3,4,2) = 4

   Col 2 max = max(1,0,2) = 2

   Col 3 max = max(2,−1,1) = 2
4. Column’s minimax over pure columns is min(4,2,2) = 2.
5. Since maximin (1) ≠ minimax (2), there is no pure-strategy saddle point. But we can still check if any entry is simultaneously a row-min and column-max (saddle condition):
6. Row minima occur at (row 1, col 2) value 1 and (row 3, col 3) value 1 (also row 3 col 1/2 are 2,2 not minima).
7. Column maxima: col 2 has max 2 (at row 3), col 3 has max 2 (at row 1). No entry equals both a row-min and a column-max.
8. Conclusion: no pure saddle point → optimal play requires mixed strategies (minimax theorem guarantees existence).

**Insight:** Pure saddle points are rare. The quick diagnostic is: compare max over row-minima vs min over column-maxima. If they differ, mixing is necessary.

### Example 3: Set up the LP for Row and interpret constraints as guarantees

Use the game from Example 1:

A = [ [ 2, −1 ],

[ 0, 1 ] ]

We’ll build Row’s LP and read it as “choose **p** to guarantee v against every column.”

1. Let **p** = (p₁, p₂) with p₁ + p₂ = 1 and p₁, p₂ ≥ 0. Introduce value variable v.
2. For each column j, require expected payoff ≥ v.
3. Column 1 constraint:

   p₁·2 + p₂·0 ≥ v

   2p₁ ≥ v
4. Column 2 constraint:

   p₁·(−1) + p₂·1 ≥ v

   −p₁ + p₂ ≥ v
5. Add probability simplex constraint:

   p₁ + p₂ = 1

   p₁, p₂ ≥ 0
6. Optimization objective:

   maximize v
7. Solve quickly by substituting p₂ = 1 − p₁:

   Constraints become

   2p₁ ≥ v

   −p₁ + (1 − p₁) ≥ v ⇒ 1 − 2p₁ ≥ v

   So v ≤ min(2p₁, 1 − 2p₁). Maximizing v sets them equal:

   2p₁ = 1 − 2p₁ ⇒ p₁ = 1/4 ⇒ v = 1/2.
8. Thus the LP reproduces the minimax solution and makes the guarantee explicit: Row picks p₁ = 1/4 to ensure at least v = 1/2 no matter which column is chosen.

**Insight:** Each LP constraint corresponds to an adversarial scenario (a column choice). Maximizing v finds the strongest payoff you can guarantee uniformly across all scenarios.

## Key Takeaways

- ✓

  A finite two-player zero-sum game is fully described by a single payoff matrix A; Column’s payoff is −Aᵢⱼ.
- ✓

  Mixed strategies are probability vectors **p** ∈ Δ\_m and **q** ∈ Δ\_n; the expected payoff is **p**ᵀA**q**.
- ✓

  Row’s conservative objective is max\_{**p**} min\_{**q**} **p**ᵀA**q** (maximin); Column’s is min\_{**q**} max\_{**p**} **p**ᵀA**q** (minimax).
- ✓

  The minimax theorem guarantees equality of these quantities and the existence of optimal mixed strategies; the common value is v.
- ✓

  A saddle point (**p**⋆, **q**⋆) is a Nash equilibrium in zero-sum games and yields payoff v under optimal play.
- ✓

  At equilibrium, actions played with positive probability must yield equal expected payoff (indifference / complementary slackness).
- ✓

  Computing optimal strategies reduces to linear programming; strong duality mirrors minimax equality.
- ✓

  Minimax thinking generalizes to adversarial ML objectives (e.g., GANs), even when assumptions differ.

## Common Mistakes

- ✗

  Confusing “randomizing because you’re unsure” with “randomizing to be unexploitable.” In zero-sum games, mixing is strategic, not merely epistemic.
- ✗

  Assuming Nash equilibrium always means pure strategies. Many zero-sum games (e.g., Rock–Paper–Scissors) have no pure equilibrium.
- ✗

  Forgetting that shifting all payoffs by a constant changes v but does not change optimal strategies.
- ✗

  Mixing up the directions of inequalities when writing LP constraints (Row uses ≥ v for each column; Column uses ≤ v for each row).

## Practice

easy

Solve the zero-sum game by indifference:

A = [ [ 1, −1 ],

[ −2, 2 ] ]

Find optimal mixed strategies (**p**⋆, **q**⋆) and the value v.

**Hint:** Let Row use **p** = (p, 1−p). Compute u₁(p), u₂(p) for the two columns and set them equal. Then make Row indifferent to solve for **q**.

Show solution

Let **p** = (p, 1−p).

Column 1 payoff: u₁(p) = p·1 + (1−p)·(−2) = p − 2 + 2p = 3p − 2.

Column 2 payoff: u₂(p) = p·(−1) + (1−p)·2 = −p + 2 − 2p = 2 − 3p.

Equalize: 3p − 2 = 2 − 3p ⇒ 6p = 4 ⇒ p = 2/3.

Value: v = 3(2/3) − 2 = 2 − 2 = 0.

Now Column: **q** = (q, 1−q).

Row 1 payoff: r₁(q) = 1·q + (−1)(1−q) = q − 1 + q = 2q − 1.

Row 2 payoff: r₂(q) = (−2)q + 2(1−q) = −2q + 2 − 2q = 2 − 4q.

Equalize: 2q − 1 = 2 − 4q ⇒ 6q = 3 ⇒ q = 1/2.

So **p**⋆ = (2/3, 1/3), **q**⋆ = (1/2, 1/2), v = 0.

medium

Formulate Row’s linear program (variables and constraints) for a general m×n payoff matrix A. Explain in one sentence what each family of constraints means.

**Hint:** Introduce v and require that every pure column action yields expected payoff ≥ v against **p**.

Show solution

Variables: **p** ∈ ℝ^m, v ∈ ℝ.

maximize v

subject to:

1) For each column j = 1,…,n: ∑ᵢ pᵢ Aᵢⱼ ≥ v.

2) ∑ᵢ pᵢ = 1.

3) pᵢ ≥ 0 for all i.

Meaning: (1) enforces that Row’s mixed strategy **p** guarantees at least v even if Column chooses the worst column; (2)-(3) enforce that **p** is a valid probability distribution.

hard

Consider the game

A = [ [ 0, 1, −1 ],

[ −1, 0, 1 ],

[ 1, −1, 0 ] ]

(a cyclic win/lose structure). Show that **p** = (1/3, 1/3, 1/3) and **q** = (1/3, 1/3, 1/3) is a saddle point and find v.

**Hint:** Compute **p**ᵀA and A**q** when **p** and **q** are uniform. Use symmetry to argue no player can do better by deviating.

Show solution

Let **u** = (1/3, 1/3, 1/3).

Compute **u**ᵀA. Each component is the average of a column:

- •Column 1 entries: 0, −1, 1 sum to 0 ⇒ average 0.
- •Column 2 entries: 1, 0, −1 sum to 0 ⇒ average 0.
- •Column 3 entries: −1, 1, 0 sum to 0 ⇒ average 0.

So **u**ᵀA = (0, 0, 0).

Thus for any **q**, **u**ᵀA**q** = (0,0,0)·**q** = 0.

So if Row plays **u**, Row guarantees at least 0.

Similarly compute A**u**. Each component is the average of a row:

- •Row 1: 0 + 1 − 1 = 0 ⇒ average 0.
- •Row 2: −1 + 0 + 1 = 0 ⇒ average 0.
- •Row 3: 1 − 1 + 0 = 0 ⇒ average 0.

So A**u** = (0,0,0)ᵀ.

Thus for any **p**, **p**ᵀA**u** = **p**ᵀ(0,0,0)ᵀ = 0.

So if Column plays **u**, Column ensures Row’s payoff is at most 0.

Therefore max\_{**p**} min\_{**q**} **p**ᵀA**q** = min\_{**q**} max\_{**p**} **p**ᵀA**q** = 0, and (**u**, **u**) is a saddle point with value v = 0.

## Connections

Next: [Generative Adversarial Networks](/tech-tree/gan/)

Related prior knowledge: [Nash Equilibrium](/tech-tree/nash-equilibrium/), [Linear Programming](/tech-tree/linear-programming/)

Helpful follow-ons (if present in your tree): [Duality in Linear Programming](/tech-tree/lp-duality/), [No-Regret Learning](/tech-tree/no-regret-learning/), [Convex–Concave Optimization](/tech-tree/convex-concave/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
