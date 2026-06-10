---
title: Nash Equilibrium
description: Strategy profile where no player benefits from unilateral deviation.
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
permalink: /tech-tree/nash-equilibrium/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Nash Equilibrium

Game TheoryDifficulty: ★★★☆☆Depth: 7Unlocks: 12

Strategy profile where no player benefits from unilateral deviation.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Strategy profile: an assignment of one strategy to every player
- -Nash equilibrium: a strategy profile in which no single player can increase their own payoff by unilaterally changing their strategy (mutual best responses)

## Key Symbols & Notation

s, s\_i, s\_-i (strategy profile, player i's strategy, others' strategies); u\_i(s) (player i's payoff)

## Essential Relationships

- -Best-response (inequality): u\_i(s\_i, s\_-i) >= u\_i(s\_i', s\_-i) for all alternative s\_i' (s\_i is a best response to s\_-i)
- -Equilibrium universal condition: for every player i, the chosen s\_i satisfies the best-response inequality (no profitable unilateral deviation)

## Prerequisites (2)

[Game Theory Introduction6 atoms](/tech-tree/game-theory-intro/)[Optimization Introduction5 atoms](/tech-tree/optimization-intro/)

## Unlocks (6)

[Mechanism Designlvl 4](/tech-tree/mechanism-design/)[Bayesian Gameslvl 4](/tech-tree/bayesian-games/)[Zero-Sum Gameslvl 4](/tech-tree/zero-sum-games/)[Repeated Gameslvl 4](/tech-tree/repeated-games/)[Oligopoly Modelslvl 4](/tech-tree/oligopoly-models/)[Mixed Strategieslvl 4](/tech-tree/mixed-strategies/)

## Referenced by (4)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (4)

[Competitive AdvantageBusiness

Formalizes why competitive advantages erode: rational competitors adjust strategies until no one benefits from unilateral deviation, explaining the convergence dynamic where others replicate your capability and margins compress toward equilibrium](/business/competitive-advantage/)[equilibriumBusiness

Nash equilibrium is the formal game-theoretic definition of equilibrium - the strategy profile where no player benefits from unilateral deviation. Understanding this formalization clarifies what it would mean for bids to be derived from an equilibrium model vs. not.](/business/equilibrium/)[Game TheoryBusiness

The central solution concept for analyzing business competition - predicting stable outcomes where no firm can unilaterally improve by changing strategy](/business/game-theory/)[Dominant StrategyBusiness

Dominant strategy equilibrium is a strict refinement of Nash equilibrium - iterated elimination of dominated strategies is the primary technique to reduce the strategy space before solving for Nash, directly implementing the 'reduce search' purpose of dominance checking](/business/dominant-strategy/)

Advanced Learning Details

### Graph Position

95

Depth Cost

12

Fan-Out (ROI)

7

Bottleneck Score

7

Chain Length

### Cognitive Load

5

Atomic Elements

34

Total Elements

L2

Percentile Level

L3

Atomic Level

### All Concepts (12)

- - Strategy profile: a tuple listing one strategy choice for each player (e.g., s = (s1,...,sn))
- - Unilateral deviation: a single player changing their strategy while all other players' strategies are held fixed
- - Nash equilibrium: a strategy profile in which no player can increase their payoff by a unilateral deviation
- - Best response: a strategy (or set of strategies) that maximizes a player's payoff given the other players' strategies
- - Best-response correspondence (mapping): the mapping from opponents' strategy profiles to the set of a player's best responses
- - Pure strategy: choosing one action deterministically (no randomness)
- - Mixed strategy (randomized strategy): a probability distribution over a player's pure strategies
- - Expected payoff under mixed strategies: the expected value of a player's payoff when actions are drawn according to mixed strategies
- - Support of a mixed strategy: the set of pure strategies assigned positive probability in a mixed strategy
- - Mixed-strategy Nash equilibrium: a Nash equilibrium in which one or more players use mixed (probabilistic) strategies
- - Indifference condition for mixed NE: the requirement that any pure action in the support of a player's mixed strategy yields the same expected payoff
- - Best-response dynamics (iterative idea): the conceptual process of players repeatedly playing best responses to others (used for reasoning or algorithms)

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

In many strategic situations—pricing, traffic routing, bidding, or even choosing technologies—your best move depends on what others do. A Nash equilibrium is the “no-regrets if I alone change my mind” point: a stable strategy profile where each player is already doing a best response to everyone else.

TL;DR:

A Nash equilibrium is a strategy profile s = (s₁,…,sₙ) such that for every player i, uᵢ(sᵢ, s₋ᵢ) ≥ uᵢ(sᵢ′, s₋ᵢ) for all alternative strategies sᵢ′. Equivalently, everyone is playing a best response to the others (mutual best responses). It can be pure or mixed; it may be inefficient; and multiple equilibria can exist.

## What Is Nash Equilibrium?

### Why we need the concept (motivation)

In game theory, you rarely choose an action in isolation. Your outcome depends on others’ choices, and theirs depends on yours. So the usual “maximize my payoff” idea becomes intertwined: **your best decision is a function of what you expect others to do**.

We want a notion of **stability**: a predicted outcome that, once reached, doesn’t give any single player an incentive to unilaterally change course. Nash equilibrium formalizes this idea.

### The basic objects

A (normal-form) game has:

- •Players i ∈ {1,…,n}
- •Strategy sets Sᵢ for each player i
- •Payoff functions uᵢ(s) where s is a **strategy profile**

A **strategy profile** is an assignment of one strategy to every player:

- •s = (s₁, s₂, …, sₙ)
- •sᵢ is player i’s strategy
- •s₋ᵢ denotes “everyone except i”:
- •s₋ᵢ = (s₁,…,sᵢ₋₁, sᵢ₊₁,…,sₙ)

So we can write payoffs as uᵢ(sᵢ, s₋ᵢ).

### Definition (pure-strategy Nash equilibrium)

A strategy profile s\* is a **Nash equilibrium** if **no player can improve their payoff by changing only their own strategy**, holding others fixed.

Formally, s\* is a Nash equilibrium if ∀i and ∀sᵢ′ ∈ Sᵢ,

uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ′, s₋ᵢ\*)

Read it slowly:

- •Others keep playing s₋ᵢ\*
- •Player i compares their equilibrium payoff uᵢ(sᵢ*, s₋ᵢ*)
- •Against any unilateral deviation sᵢ′
- •And finds no profitable deviation.

### Intuition: “no profitable unilateral deviation”

A Nash equilibrium is not necessarily:

- •“The best overall outcome”
- •“Fair”
- •“Socially optimal”

It’s a **self-enforcing** outcome: if everyone believes the equilibrium will be played, it is consistent for each person to stick with their equilibrium strategy.

### Best responses (another way to say the same thing)

Define player i’s **best response set** to others’ strategies s₋ᵢ:

BRᵢ(s₋ᵢ) = { sᵢ ∈ Sᵢ : uᵢ(sᵢ, s₋ᵢ) ≥ uᵢ(sᵢ′, s₋ᵢ) for all sᵢ′ ∈ Sᵢ }

Then s\* is a Nash equilibrium iff:

sᵢ *∈ BRᵢ(s₋ᵢ*) for all i

So a Nash equilibrium is exactly a profile of **mutual best responses**.

### A quick sanity check: what Nash equilibrium is *not*

Nash equilibrium does **not** prevent two or more players from coordinating a deviation that benefits them jointly. It only blocks deviations by a **single** player at a time.

This matters because many “unstable” or “unreasonable” outcomes are eliminated by unilateral deviations, but some inefficient outcomes remain stable because escaping them requires coordination.

### Pure vs mixed (preview)

Often, especially in finite games, a pure-strategy equilibrium might not exist. Nash’s major theorem says that if players can randomize (play **mixed strategies**), at least one Nash equilibrium exists.

We’ll build up to that idea after we understand the mechanics in pure strategies.

## Core Mechanic 1: Best Responses and Checking Equilibria (Pure Strategies)

### Why this mechanic matters

The definition is simple, but applying it requires a practical workflow:

1. 1)Hold others fixed.
2. 2)Compute a player’s best response.
3. 3)Find profiles where everyone is simultaneously best-responding.

In small games (2×2, 2×3), this is often easiest with payoff matrices. In larger games, it resembles an optimization problem: each player solves

maximize over sᵢ ∈ Sᵢ: uᵢ(sᵢ, s₋ᵢ)

### Two-player matrix games

For two players (Row and Column), we represent payoffs as ordered pairs.

Example structure:

|  | C₁ | C₂ |
| --- | --- | --- |
| R₁ | (a, b) | (c, d) |
| R₂ | (e, f) | (g, h) |

A pure Nash equilibrium is a cell where:

- •Row’s payoff is maximal within its column (given Column’s choice)
- •Column’s payoff is maximal within its row (given Row’s choice)

### Algorithm: “underline best responses”

A common manual method:

1. 1)For each column, underline Row’s best payoff (Row’s best response).
2. 2)For each row, underline Column’s best payoff (Column’s best response).
3. 3)Any cell where **both** payoffs are underlined is a pure Nash equilibrium.

This is just the definition made visual.

### Connection to optimization language

Suppose the strategy sets are numeric (e.g., choose a quantity qᵢ ≥ 0). Then a best response is literally an optimizer:

BRᵢ(q₋ᵢ) = argmax\_{qᵢ ≥ 0} uᵢ(qᵢ, q₋ᵢ)

A Nash equilibrium is a fixed point of best responses:

qᵢ *∈ BRᵢ(q₋ᵢ*) for all i

This “fixed point of best-response correspondences” viewpoint is the bridge to existence theorems and to computation methods.

### Multiple equilibria, no equilibria

Two key phenomena appear immediately:

1) **Multiple equilibria**

- •More than one profile can satisfy mutual best responses.
- •Prediction may require refinement (risk dominance, trembling-hand perfection, focal points) or extra context.

2) **No pure equilibrium**

- •Some games have no cell where both players are best-responding.
- •Classic example: Rock–Paper–Scissors.

This motivates mixed strategies.

### Dominated strategies (a useful simplifier)

A strategy sᵢ is **strictly dominated** if there exists another strategy tᵢ such that

uᵢ(tᵢ, s₋ᵢ) > uᵢ(sᵢ, s₋ᵢ) for all s₋ᵢ

A strictly dominated strategy is never a best response, so it cannot be used in any Nash equilibrium. Eliminating dominated strategies can simplify equilibrium search.

### Comparing related “stability” notions

To avoid confusion, here’s a compact comparison:

| Concept | What can deviate? | Stability claim | Typical use |
| --- | --- | --- | --- |
| Nash equilibrium | One player at a time | No profitable unilateral deviation | Baseline prediction in strategic settings |
| Social optimum | A planner chooses | Maximize ∑ᵢ uᵢ(s) | Welfare analysis |
| Pareto efficiency | Any group compares outcomes | No alternative makes someone better without hurting others | Efficiency benchmark |

A Nash equilibrium can be Pareto-inefficient (e.g., Prisoner’s Dilemma). That isn’t a bug—it’s the point: incentives can misalign with collective welfare.

## Core Mechanic 2: Mixed-Strategy Nash Equilibrium (and Why Randomization Helps)

### Why mixed strategies enter the picture

If a game has no pure equilibrium, should we conclude it has no stable outcome? Nash’s insight: allow players to **randomize** over pure actions.

Randomization can make opponents indifferent among their options, removing profitable deviations.

### Mixed strategies as probability distributions

For player i with k pure strategies, a mixed strategy is a probability vector **pᵢ**:

**pᵢ** = (pᵢ1, …, pᵢk) where pᵢj ≥ 0 and ∑ⱼ pᵢj = 1

A mixed-strategy profile is (**p₁**, …, **pₙ**).

Payoffs become **expected payoffs**. In a two-player finite game, the expected payoff to player i is:

E[uᵢ] = ∑\_{a∈A} ∑\_{b∈B} p₁(a) p₂(b) uᵢ(a,b)

(Generalizes to n players with ∑ over all action profiles.)

### Definition (mixed-strategy Nash equilibrium)

A mixed-strategy profile (**p₁**

,…,**pₙ**) is a Nash equilibrium if no player can increase expected payoff by changing only their own distribution.

Formally, for every i and every alternative mixed strategy **qᵢ**,

E[uᵢ(**pᵢ**, **p₋ᵢ**)] ≥ E[uᵢ(**qᵢ**, **p₋ᵢ**)]

This is the same logic as pure strategies, but with expectations.

### The key property: indifference over the support

If player i mixes among multiple pure strategies with positive probability, then in equilibrium those strategies must yield equal expected payoff (otherwise i would shift probability to the better one).

Let Sᵢ⁺ be the support (strategies played with positive probability). Then for any a, a′ ∈ Sᵢ⁺:

E[uᵢ(a, **p₋ᵢ**)] = E[uᵢ(a′, **p₋ᵢ**)]

And any strategy outside the support must do no better:

E[uᵢ(a\_out, **p₋ᵢ**)] ≤ E[uᵢ(a, **p₋ᵢ**)] for a ∈ Sᵢ⁺

This “equalize payoffs” rule is the workhorse for solving 2×2 mixed equilibria.

### Solving a 2×2 mixed equilibrium (template)

Suppose Row has strategies R₁,R₂ and Column has C₁,C₂.

Let Column play C₁ with probability q (and C₂ with 1−q).

Row’s expected payoff from R₁ and R₂ are linear functions of q:

E[u\_R(R₁)] = q·u\_R(R₁,C₁) + (1−q)·u\_R(R₁,C₂)

E[u\_R(R₂)] = q·u\_R(R₂,C₁) + (1−q)·u\_R(R₂,C₂)

If Row mixes between R₁ and R₂ in equilibrium, then set them equal and solve for q.

Similarly, let Row play R₁ with probability p and solve for p by making Column indifferent.

### Why existence is guaranteed (high-level)

For finite games, Nash (1950–51) proved at least one mixed equilibrium exists. Intuitively:

- •Mixed strategies form a compact, convex set (a simplex).
- •Best responses can be seen as a correspondence with a fixed point.

You don’t need the full proof here, but you should internalize the consequence:

**Even when no pure equilibrium exists, the game still has a stable prediction in mixed strategies.**

### Interpreting mixed strategies

Be careful with interpretation:

- •**Randomization** can be literal (a mixed action, a coin flip).
- •Or it can represent uncertainty about types, trembles, or population heterogeneity.

In any case, the equilibrium condition remains: no unilateral change improves expected payoff.

## Application/Connection: Why Nash Equilibrium Matters (and What It Enables)

### Nash equilibrium as a baseline for strategic prediction

In many domains, Nash equilibrium is the default “solution concept”:

- •Oligopoly pricing/quantity competition
- •Network routing and congestion
- •Security games (defender vs attacker allocations)
- •Auctions and bidding (with additional assumptions)

The practical value is that it turns interactive decision-making into a set of consistency constraints: everyone’s strategy must be optimal given the others.

### Efficiency vs incentives (Prisoner’s Dilemma lesson)

A central theme in mechanism design and market design is that Nash equilibria can be inefficient.

Let social welfare be W(s) = ∑ᵢ uᵢ(s).

- •A social planner would choose s maximizing W(s).
- •Players choose strategies leading to Nash equilibria.

The gap between equilibrium welfare and optimal welfare motivates:

- •Changing rules (mechanism design)
- •Adding incentives, taxes, or transfers
- •Designing information and timing

### Connection to Mechanism Design

Mechanism design asks: can we design a game so that desirable outcomes occur in equilibrium?

In a mechanism, the equilibrium concept is often Nash equilibrium (or Bayesian Nash equilibrium when there is private information). The designer wants:

- •Good outcomes (high welfare, fairness, revenue)
- •Incentive compatibility: truthful or intended behavior is a best response

So Nash equilibrium is the “target” condition: the mechanism is successful if the intended outcome is a Nash equilibrium of the induced game.

### Connection to Zero-Sum Games

Zero-sum games are those where u₁(s) = −u₂(s).

- •In zero-sum games, equilibrium has a particularly strong meaning: it coincides with minimax optimal play.
- •Mixed strategies are often essential.

For zero-sum games, the Nash equilibrium value (the game value) is stable and can be found via linear programming.

### Cautionary notes: limitations and refinements

Nash equilibrium is powerful but not the end of the story.

Common limitations:

- •Multiple equilibria: which one is selected?
- •Coordination issues: equilibria may be risk-dominated or fragile.
- •Non-credible threats in dynamic games: Nash may allow unreasonable strategies off the equilibrium path (addressed by subgame perfection).

Still, Nash equilibrium is the foundational equilibrium concept that most refinements build upon.

### Mental model to keep

A good working mental model:

1. 1)Fix everyone else’s strategies s₋ᵢ.
2. 2)Ask: what would I do to maximize uᵢ(sᵢ, s₋ᵢ)?
3. 3)A Nash equilibrium is where this answer is “I would keep doing what I’m already doing,” for every i.

That stable-point idea is what makes Nash equilibrium central across economics, CS, and ML (e.g., multi-agent learning and GAN-like setups).

## Worked Examples (3)

### Example 1: Finding a Pure Nash Equilibrium in Prisoner’s Dilemma

Two players choose C (Cooperate) or D (Defect). Payoffs (Row, Column):

|  | C | D |
| --- | --- | --- |
| C | (3, 3) | (0, 5) |
| D | (5, 0) | (1, 1) |

Find all pure-strategy Nash equilibria and compare to the socially optimal outcome.

1. Step 1: Compute Row’s best responses.

   - •If Column plays C: Row’s payoffs are u\_R(C,C)=3 and u\_R(D,C)=5 ⇒ best response is D.
   - •If Column plays D: Row’s payoffs are u\_R(C,D)=0 and u\_R(D,D)=1 ⇒ best response is D.

   So BR\_R(C)=D and BR\_R(D)=D.
2. Step 2: Compute Column’s best responses.

   - •If Row plays C: Column’s payoffs are u\_C(C,C)=3 and u\_C(C,D)=5 ⇒ best response is D.
   - •If Row plays D: Column’s payoffs are u\_C(D,C)=0 and u\_C(D,D)=1 ⇒ best response is D.

   So BR\_C(C)=D and BR\_C(D)=D.
3. Step 3: Identify mutual best responses.

   The only profile where both are best-responding is (D, D).

   Check the Nash inequalities explicitly:

   - •Given Column plays D, Row compares u\_R(D,D)=1 to u\_R(C,D)=0 ⇒ no profitable deviation.
   - •Given Row plays D, Column compares u\_C(D,D)=1 to u\_C(D,C)=0 ⇒ no profitable deviation.

   Therefore (D,D) is a Nash equilibrium.
4. Step 4: Compare to social welfare.

   Compute W(s)=u\_R(s)+u\_C(s):

   - •W(C,C)=3+3=6
   - •W(D,D)=1+1=2

   So (C,C) is socially better, but it is not a Nash equilibrium because each player can unilaterally deviate to D and increase their own payoff (from 3 to 5).

**Insight:** Nash equilibrium captures incentive stability, not collective optimality. Prisoner’s Dilemma is the canonical demonstration that individually rational behavior can produce inefficient outcomes.

### Example 2: Mixed Nash Equilibrium in Matching Pennies

Two players simultaneously choose H (Heads) or T (Tails). Row wins if the coins match; Column wins if they differ. Payoffs (Row, Column):

|  | H | T |
| --- | --- | --- |
| H | (1, −1) | (−1, 1) |
| T | (−1, 1) | (1, −1) |

Find the mixed-strategy Nash equilibrium.

1. Step 1: Observe no pure equilibrium.

   Check each cell for mutual best response:

   - •If Column plays H, Row prefers H (1 > −1). If Row plays H, Column prefers T (1 > −1).

   So (H,H) fails. Similar reasoning rules out all four cells. Hence no pure Nash equilibrium.
2. Step 2: Let Column mix.

   Let q = P(Column plays H). Then P(Column plays T)=1−q.

   Compute Row’s expected payoff from each pure action:

   E[u\_R(H)] = q·u\_R(H,H) + (1−q)·u\_R(H,T)

   = q·1 + (1−q)·(−1)

   = q − (1−q)

   = 2q − 1

   E[u\_R(T)] = q·u\_R(T,H) + (1−q)·u\_R(T,T)

   = q·(−1) + (1−q)·1

   = −q + 1 − q

   = 1 − 2q
3. Step 3: Make Row indifferent (so Row is willing to mix).

   Set E[u\_R(H)] = E[u\_R(T)]:

   2q − 1 = 1 − 2q

   2q + 2q = 1 + 1

   4q = 2

   q = 1/2

   So Column must play H with probability 1/2.
4. Step 4: By symmetry, make Column indifferent.

   Let p = P(Row plays H). Then:

   E[u\_C(H)] = p·u\_C(H,H) + (1−p)·u\_C(T,H)

   = p·(−1) + (1−p)·1

   = −p + 1 − p

   = 1 − 2p

   E[u\_C(T)] = p·u\_C(H,T) + (1−p)·u\_C(T,T)

   = p·1 + (1−p)·(−1)

   = p − (1−p)

   = 2p − 1

   Set equal:

   1 − 2p = 2p − 1

   1 + 1 = 2p + 2p

   2 = 4p

   p = 1/2

   So Row plays H with probability 1/2.
5. Step 5: State the equilibrium.

   Mixed Nash equilibrium:

   - •Row: (H with 1/2, T with 1/2)
   - •Column: (H with 1/2, T with 1/2)

   Expected payoff to Row is 0 (and to Column is 0), consistent with a fair zero-sum game.

**Insight:** In mixed equilibrium, each player chooses probabilities that make the other player indifferent among their pure actions—removing profitable unilateral deviations.

### Example 3: Two Pure Nash Equilibria in a Coordination Game

Two players choose A or B. They prefer to match, but each equilibrium favors a different convention. Payoffs (Row, Column):

|  | A | B |
| --- | --- | --- |
| A | (2, 2) | (0, 0) |
| B | (0, 0) | (1, 1) |

Find all pure Nash equilibria and interpret them.

1. Step 1: Best responses for Row.

   - •If Column plays A: Row gets 2 from A and 0 from B ⇒ best response is A.
   - •If Column plays B: Row gets 0 from A and 1 from B ⇒ best response is B.
2. Step 2: Best responses for Column (symmetric).

   - •If Row plays A: Column best response is A.
   - •If Row plays B: Column best response is B.
3. Step 3: Identify mutual best responses.

   (A,A) is mutual best response ⇒ Nash equilibrium.

   (B,B) is mutual best response ⇒ Nash equilibrium.

   The off-diagonal outcomes (A,B) and (B,A) are not equilibria because each player wants to switch to match the other.
4. Step 4: Interpretation.

   There are two stable conventions:

   - •(A,A) yields higher payoffs (2,2)
   - •(B,B) yields lower payoffs (1,1)

   Nash equilibrium alone does not select between them; additional criteria (history, expectations, risk dominance, communication) may matter.

**Insight:** Multiple Nash equilibria create an equilibrium selection problem: the theory predicts stability, but not necessarily which stable convention a system will coordinate on.

## Key Takeaways

- ✓

  A strategy profile s = (s₁,…,sₙ) assigns one strategy to every player; s₋ᵢ denotes all strategies except player i’s.
- ✓

  Nash equilibrium means: ∀i, no unilateral deviation improves payoff: uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ′, s₋ᵢ\*) for all sᵢ′.
- ✓

  Equivalently, each player’s equilibrium strategy is a best response: sᵢ *∈ BRᵢ(s₋ᵢ*).
- ✓

  Pure Nash equilibria can be found by checking mutual best responses in payoff matrices; strictly dominated strategies cannot appear in equilibrium.
- ✓

  Some games have no pure Nash equilibrium; allowing mixed strategies (probability distributions) restores existence in finite games.
- ✓

  In mixed equilibrium, any strategy played with positive probability must yield equal expected payoff (indifference over the support).
- ✓

  Nash equilibrium is a stability concept, not an efficiency guarantee—equilibria may be Pareto-inefficient or multiple.
- ✓

  Nash equilibrium is foundational for later topics like mechanism design (designing games with desired equilibria) and zero-sum games (minimax and LP computation).

## Common Mistakes

- ✗

  Confusing Nash equilibrium with “the best outcome” or “social optimum”; Nash is about unilateral incentives, not collective welfare.
- ✗

  Checking only one player’s incentives; an equilibrium requires the no-deviation condition for every player simultaneously.
- ✗

  Assuming mixed strategies mean players are irrational or ‘guessing’; in equilibrium, mixing is an optimal response that removes profitable deviations.
- ✗

  Forgetting that in a mixed equilibrium, only strategies in the support must be equal-payoff; strategies outside the support can be strictly worse.

## Practice

easy

Consider the game:

|  | L | R |
| --- | --- | --- |
| U | (2, 1) | (0, 0) |
| D | (3, 0) | (1, 2) |

Find all pure-strategy Nash equilibria.

**Hint:** Compute best responses: for each Column choice, which Row action maximizes Row’s payoff? For each Row choice, which Column action maximizes Column’s payoff? Intersections are Nash equilibria.

Show solution

Row best responses:

- •If Column plays L: Row payoff U=2, D=3 ⇒ best response D.
- •If Column plays R: Row payoff U=0, D=1 ⇒ best response D.

So Row best response is always D.

Column best responses:

- •If Row plays U: Column payoff at L=1, R=0 ⇒ best response L.
- •If Row plays D: Column payoff at L=0, R=2 ⇒ best response R.

Mutual best response occurs at (D,R) only.

Check: given R, Row prefers D (1 > 0). Given D, Column prefers R (2 > 0). Thus (D,R) is the unique pure Nash equilibrium.

medium

In Matching Pennies, suppose Row gets payoff +2 when matching and −1 when not matching (Column gets the negative). The payoff matrix (Row, Column) is:

|  | H | T |
| --- | --- | --- |
| H | (2, −2) | (−1, 1) |
| T | (−1, 1) | (2, −2) |

Find the mixed-strategy Nash equilibrium probabilities.

**Hint:** Let q = P(Column plays H). Compute Row’s expected payoff from H vs T and set them equal to solve for q. By symmetry you can solve for p = P(Row plays H) similarly.

Show solution

Let q = P(Column plays H).

Row’s expected payoff if playing H:

E[u\_R(H)] = q·2 + (1−q)·(−1)

= 2q − 1 + q

= 3q − 1

Row’s expected payoff if playing T:

E[u\_R(T)] = q·(−1) + (1−q)·2

= −q + 2 − 2q

= 2 − 3q

Set equal for indifference:

3q − 1 = 2 − 3q

3q + 3q = 2 + 1

6q = 3

q = 1/2

So Column plays H with probability 1/2.

Now let p = P(Row plays H). Column’s payoffs are the negative of Row’s, so Column is indifferent when Row makes Row indifferent as well; by symmetry, p = 1/2.

Thus the mixed Nash equilibrium is: Row plays H with 1/2, Column plays H with 1/2.

hard

Show that if a player has a strictly dominant strategy (a strategy that yields higher payoff than any other strategy no matter what others do), then in any Nash equilibrium that player must play a strictly dominant strategy.

**Hint:** Use the definition of Nash equilibrium: at equilibrium, a player’s chosen strategy must be a best response to s₋ᵢ*. Compare the dominant strategy to any alternative at s₋ᵢ*.

Show solution

Let player i have a strictly dominant strategy dᵢ ∈ Sᵢ. By definition, for every alternative sᵢ′ ≠ dᵢ and every s₋ᵢ,

uᵢ(dᵢ, s₋ᵢ) > uᵢ(sᵢ′, s₋ᵢ).

Consider any Nash equilibrium s *= (sᵢ*, s₋ᵢ*). Suppose for contradiction that sᵢ* ≠ dᵢ. Then applying strict dominance at s₋ᵢ\* gives:

uᵢ(dᵢ, s₋ᵢ*) > uᵢ(sᵢ*, s₋ᵢ\*).

But that means player i can unilaterally deviate from sᵢ\* to dᵢ and strictly increase payoff, contradicting the Nash condition:

uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ′, s₋ᵢ\*) for all sᵢ′.

Therefore, in any Nash equilibrium, player i must play the strictly dominant strategy dᵢ.

## Connections

- •[Mechanism Design](/tech-tree/mechanism-design/)
- •[Zero-Sum Games](/tech-tree/zero-sum-games/)
- •[Game Theory Introduction](/tech-tree/game-theory-introduction/)
- •[Optimization Introduction](/tech-tree/optimization-introduction/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
