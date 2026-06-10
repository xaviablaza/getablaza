---
title: Game Theory Introduction
description: Strategic interaction between rational agents. Payoff matrices.
date: '2026-07-01'
scheduled: '2026-09-10'
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
inspiration_url: https://templeton.host/tech-tree/game-theory-intro/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/game-theory-intro/](https://templeton.host/tech-tree/game-theory-intro/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Game Theory Introduction

Game TheoryDifficulty: ★★★☆☆Depth: 4Unlocks: 14

Strategic interaction between rational agents. Payoff matrices.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Strategy (choice for a player: pure action or probability distribution over actions)
- -Payoff (utility): numerical outcome value for a player resulting from a strategy profile
- -Nash equilibrium: a strategy profile where no player can unilaterally change strategy to increase their payoff

## Key Symbols & Notation

s\_i (strategy of player i; s denotes the full strategy profile)u\_i(s) (payoff/utility to player i given strategy profile s)

## Essential Relationships

- -Nash equilibrium as best-response condition: for every player i, s\_i maximizes u\_i(s\_i, s\_-i) holding others' strategies s\_-i fixed

## Prerequisites (2)

[Expected Value5 atoms](/tech-tree/expected-value/)[Matrix Operations6 atoms](/tech-tree/matrix-operations/)

## Unlocks (2)

[Nash Equilibriumlvl 3](/tech-tree/nash-equilibrium/)[Cooperative Gameslvl 5](/tech-tree/cooperative-games/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[Game TheoryBusiness

Direct mathematical foundation - payoff matrices, dominant strategies, and strategic form representation that business game theory models are built on](/business/game-theory/)[Strategic AnalysisBusiness

Game theory is the mathematical formalization of strategic analysis - modeling rational agents choosing actions given others' strategies](/business/strategic-analysis/)

Advanced Learning Details

### Graph Position

53

Depth Cost

14

Fan-Out (ROI)

8

Bottleneck Score

4

Chain Length

### Cognitive Load

6

Atomic Elements

51

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (20)

- - Player (rational agent) - an agent in the game who chooses strategies to maximize its payoff
- - Strategy (pure) - a single, deterministic action or plan available to a player
- - Mixed strategy - a probability distribution over a player's pure strategies
- - Strategy profile - a tuple of one strategy per player (complete specification of actions)
- - Payoff / utility function - mapping from strategy profiles to a numerical payoff for each player
- - Normal-form (strategic-form) game - representation of a game by listing players, strategy sets, and payoff functions
- - Payoff matrix (two-player normal form) - tabular representation of payoffs for each pure strategy profile
- - Best response - a strategy (or set of strategies) that maximizes a player's payoff given other players' strategies
- - Nash equilibrium (pure) - a strategy profile where every player's chosen strategy is a best response to the others
- - Nash equilibrium (mixed) - a profile of mixed strategies where no player can gain by unilateral deviation
- - Dominant strategy - a strategy that is a best response to every possible strategy profile of the opponents
- - Strictly dominated strategy - a strategy that yields strictly lower payoff than some other strategy against all opponents' choices
- - Weakly dominated strategy - a strategy that yields no higher payoff and sometimes lower payoff than some other strategy
- - Iterated elimination of (strictly) dominated strategies - repeatedly removing dominated strategies to simplify the game
- - Zero-sum game - a game in which the sum of players' payoffs is constant (often normalized to zero), so one player's gain is another's loss
- - Expected payoff under mixed strategies - the expected value of payoffs when players randomize (application of expected value to payoffs)
- - Support of a mixed strategy - the subset of pure strategies played with positive probability
- - Indifference principle in mixed equilibrium - in equilibrium, every pure strategy in the support of a player's mixed strategy must yield the same expected payoff
- - Maxmin / minimax value (in zero-sum games) - the value a player can guarantee by choosing a strategy to maximize their minimum payoff (and the dual minimax)
- - Normal-form vs. strategic intuition - interpreting payoff matrices as simultaneous strategic interactions (not as linear transformations)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

When two “rational” decision-makers interact, your best move depends on what you believe the other will do—and their best move depends on what they believe you will do. Game theory is the math of that interdependence.

TL;DR:

Game theory models strategic interaction using players, strategies, and payoffs uᵢ(s). In normal-form (payoff-matrix) games, each player chooses an action (pure strategy) or a probability distribution over actions (mixed strategy). A Nash equilibrium is a strategy profile s where no player can unilaterally change their strategy and increase their payoff.

## What Is Game Theory Introduction?

### Why game theory exists (motivation)

In many decisions, the outcome depends not just on **your** choice, but on **others’** choices. If you’re choosing a price, an ad budget, a route in traffic, a security policy, or a bid in an auction, you’re not optimizing against nature—you’re optimizing against other optimizers.

This creates a loop:

- •Your payoff depends on their action.
- •Their payoff depends on your action.
- •So your “best” action depends on what you expect them to do.

Game theory provides a language and set of solution ideas for these strategic loops.

### The core objects

A (non-cooperative) game in this node will be described by:

1) **Players**: indexed by i ∈ {1, …, n}.

2) **Strategies**: what each player can choose.

- •A **pure strategy** is a single action (e.g., “Cooperate”, “Defect”).
- •A **mixed strategy** is a probability distribution over actions.

We’ll denote player i’s strategy by sᵢ, and the full **strategy profile** by

s = (s₁, s₂, …, sₙ).

3) **Payoffs (utilities)**: a number for each player given everyone’s chosen strategies.

uᵢ(s) = payoff to player i when the strategy profile is s.

### Normal-form games (payoff matrices)

In many introductory settings, each player chooses simultaneously (or without observing the others’ choices). For two-player games with finite actions, we can represent payoffs in a matrix.

Example format (2 players):

- •Rows = Player 1 actions
- •Columns = Player 2 actions
- •Each cell contains a pair (u₁, u₂)

A payoff matrix is not merely “a table of outcomes.” It encodes a dependency structure: each player’s outcome changes with the other’s choice.

### Rationality (what we assume and what we don’t)

This node uses a simple, standard stance:

- •Players have preferences represented by utilities uᵢ(s).
- •Players choose strategies to maximize expected utility.

We are **not** assuming:

- •that players are morally good,
- •that players have perfect information about the world,
- •or that outcomes will be socially optimal.

We are assuming the decision rule: “choose what maximizes (expected) payoff,” and we’ll see how that can still produce surprising outcomes.

### A key conceptual shift

In single-agent optimization, you often search for an action a that maximizes f(a).

In game theory, you search for a **stable joint choice** s that makes sense given that each player is optimizing:

s is reasonable if each sᵢ is a best response to s₋ᵢ (everyone else’s strategies).

That stability concept is the Nash equilibrium you’ll unlock later in more depth, but we’ll already define and use it in this intro.

## Core Mechanic 1: Strategies (Pure vs Mixed) and Expected Payoff

### Why strategies need probabilities

Suppose you play Rock–Paper–Scissors. If you always play Rock, an opponent who learns this can exploit you by always playing Paper.

So sometimes the best “strategy” is not a single action but a **randomized plan**: choose Rock with probability 1/3, Paper with 1/3, Scissors with 1/3.

Randomization is not (only) about being unpredictable—it can be required for optimality when no pure action is stable.

### Pure strategies

A **pure strategy** picks one action with probability 1.

If Player i has action set Aᵢ = {aᵢ¹, …, aᵢᵏ}, then a pure strategy is an element aᵢ ∈ Aᵢ.

We often blur language and say “strategy” when we mean “action” in simple matrix games.

### Mixed strategies

A **mixed strategy** is a probability distribution over Aᵢ.

Write Player i’s mixed strategy as a vector **p**ᵢ where

- •**p**ᵢ ≥ 0 componentwise
- •∑ⱼ pᵢⱼ = 1

Example: if Aᵢ = {Up, Down}, then **p**ᵢ = (p, 1 − p).

Even though we write vectors, remember: these are probabilities, so the constraints matter.

### Expected payoff under mixed strategies

Because you already know expected value, the key bridge is:

If outcomes are uncertain due to mixed strategies, each player maximizes **expected utility**.

For two players with finite actions:

- •Player 1 chooses **p** (distribution over rows)
- •Player 2 chooses **q** (distribution over columns)

Let U₁ be Player 1’s payoff matrix (numeric entries), where (U₁)ᵣc = u₁(row r, col c).

Then the expected payoff to Player 1 is

E[u₁] = **p**ᵀ U₁ **q**.

This is exactly the “bilinear form” you may recognize from matrix operations.

#### Derivation (showing the expectation explicitly)

Let Player 1 choose row r with probability pᵣ and Player 2 choose column c with probability q\_c.

The joint probability of (r, c) under independent mixing is pᵣ q\_c.

So

E[u₁] = ∑ᵣ ∑\_c (pᵣ q\_c) u₁(r, c)

Now observe that this is precisely the matrix expression **p**ᵀ U₁ **q**.

### Reading a payoff matrix correctly

A payoff matrix lists outcomes (u₁, u₂) per action pair.

But strategically, you should read it as:

- •Fix what the other player does.
- •Ask which of your actions gives the highest payoff.

That leads to the idea of a **best response**.

### Best responses (informal)

Given the other players’ strategies s₋ᵢ, player i’s best responses are the strategies that maximize uᵢ(sᵢ, s₋ᵢ).

If player i has two possible actions, you can often compute a threshold probability at which the player is indifferent between them.

That indifference condition is the workhorse for solving many 2×2 mixed-strategy equilibria later.

### Tiny 2×2 illustration of expected value

Suppose Player 1 has actions Top/Bottom and Player 2 has actions Left/Right.

Let Player 1’s payoff matrix be

U₁ = [ [2, 0],

[1, 3] ].

If Player 1 plays Top with probability p, then **p** = (p, 1 − p).

If Player 2 plays Left with probability q, then **q** = (q, 1 − q).

Compute E[u₁] = **p**ᵀ U₁ **q**:

First compute U₁ **q**:

- •U₁ **q** = [ 2q + 0(1 − q),

1q + 3(1 − q) ]

= [ 2q,

q + 3 − 3q ]

= [ 2q,

3 − 2q ].

Then multiply by **p**ᵀ:

E[u₁] = (p, 1 − p) · (2q, 3 − 2q)

= p(2q) + (1 − p)(3 − 2q)

= 2pq + 3 − 2q − 3p + 2pq

= 3 − 2q − 3p + 4pq.

This is a concrete example of how strategies-as-probabilities translate into expected payoffs.

## Core Mechanic 2: Nash Equilibrium (Stability Under Unilateral Deviation)

### Why we need an equilibrium concept

If each player is rational and chooses best responses, we need a way to describe outcomes that are consistent with that mutual best-response logic.

A naive idea is: “pick the outcome that maximizes total payoff.” But players are not a single coordinated agent, and they may not be able to commit to cooperate.

So game theory often focuses on **stability**:

- •If we announce what everyone will do,
- •would any single player want to change their choice (while others keep theirs)?

If yes, the announced profile is unstable.

### Definition: Nash equilibrium

A strategy profile s *= (s₁*, …, sₙ\*) is a **Nash equilibrium** if for every player i,

uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ\*) for all feasible sᵢ.

Interpretation:

- •Hold everyone else fixed at s₋ᵢ\*.
- •Player i cannot improve by switching unilaterally.

This is a local optimality condition in the space of strategy profiles.

### Best response formulation

Equivalently, define the best response set:

BRᵢ(s₋ᵢ) = { sᵢ : uᵢ(sᵢ, s₋ᵢ) is maximized }.

Then s\* is a Nash equilibrium iff

sᵢ *∈ BRᵢ(s₋ᵢ*) for all i.

This form is extremely practical for matrix games: you can mark best responses and look for intersections.

### Pure-strategy Nash equilibrium in a matrix

For a 2-player matrix:

- •In each column, find Player 1’s best response row(s) (highest u₁).
- •In each row, find Player 2’s best response column(s) (highest u₂).
- •Any cell that is simultaneously a best response for both players is a pure Nash equilibrium.

This can be done visually.

### When no pure equilibrium exists: mixed equilibrium

Some games (e.g., Matching Pennies, Rock–Paper–Scissors) have no pure Nash equilibrium.

In those cases, a mixed Nash equilibrium may exist. In a mixed equilibrium:

- •Each player’s mixing probabilities make the other player indifferent among the pure actions in the support (the actions played with positive probability).

Indifference is key because:

- •If one action yielded strictly higher expected payoff, a rational player would put probability 1 on it.

### Why “unilateral” matters

Nash equilibrium blocks profitable **single-player** deviations.

It does **not** block profitable **joint** deviations. Two players might both prefer to coordinate on a different outcome but can’t trust each other to stick to it without some commitment mechanism.

This distinction sets up later topics:

- •repeated games and reputation,
- •commitment devices,
- •cooperative game theory.

### Efficiency vs stability (important contrast)

A Nash equilibrium can be inefficient.

To name the tension:

- •**Stability**: no one wants to deviate alone.
- •**Efficiency**: could everyone be better off in some other outcome?

These are different axes, and game theory studies the gap.

### A quick comparison table

| Concept | Question it answers | Depends on beliefs? | Typical output |
| --- | --- | --- | --- |
| Best response | “Given others, what should I do?” | Yes (others’ strategies fixed) | Set of strategies |
| Nash equilibrium | “What joint behavior is self-consistent?” | Implicitly (each expects others to play equilibrium) | Strategy profile s\* |
| Social optimum | “What maximizes total welfare ∑ᵢ uᵢ?” | No | Outcome/profile |

Keep this table in mind: confusion between Nash equilibrium and social optimum is one of the most common early mistakes.

## Application/Connection: Canonical Games, Modeling Workflow, and Why Matrices Matter

### Canonical examples (what they teach)

Intro game theory often uses a few “named” games because each highlights a different phenomenon.

#### Prisoner’s Dilemma (conflict between stability and efficiency)

Two players choose Cooperate (C) or Defect (D). A typical payoff matrix is:

|  | C | D |
| --- | --- | --- |
| **C** | (3, 3) | (0, 5) |
| **D** | (5, 0) | (1, 1) |

- •(C, C) is socially better than (D, D).
- •But (D, D) is the Nash equilibrium in this parameterization because D is a best response to both C and D.

Lesson: rationality + no commitment can yield collectively worse outcomes.

#### Coordination game (multiple equilibria)

Example:

|  | Left | Right |
| --- | --- | --- |
| **Up** | (2, 2) | (0, 0) |
| **Down** | (0, 0) | (2, 2) |

There are two pure Nash equilibria: (Up, Left) and (Down, Right).

Lesson: equilibrium selection matters; history, conventions, or communication can pick one.

#### Matching Pennies (no pure equilibrium)

Example (Player 1 wants match; Player 2 wants mismatch):

|  | H | T |
| --- | --- | --- |
| **H** | (1, −1) | (−1, 1) |
| **T** | (−1, 1) | (1, −1) |

There is no pure Nash equilibrium. The mixed equilibrium is both players choosing H with probability 1/2.

Lesson: randomization can be essential.

### A practical modeling workflow

When you face a strategic scenario, a useful disciplined workflow is:

1) **List players**: Who makes decisions?

2) **List actions** (strategy sets Aᵢ): What can each player do?

3) **Define payoffs** uᵢ(s): What does each player value? (profit, time, safety, etc.)

4) **Represent the game**:

- •Normal form (matrix) for simultaneous, discrete actions.
- •(Later) extensive form (game tree) for sequential moves.

5) **Analyze best responses**:

- •Mark dominated strategies (if any).
- •Find pure Nash equilibria.
- •If none, consider mixed strategies.

6) **Interpret**: Is the equilibrium efficient? If not, what mechanism could change incentives?

### Dominated strategies (a quick, useful tool)

A strategy is **strictly dominated** if there is another strategy that yields a strictly higher payoff no matter what the others do.

If sᵢ is strictly dominated by sᵢ′, then for all s₋ᵢ:

uᵢ(sᵢ′, s₋ᵢ) > uᵢ(sᵢ, s₋ᵢ).

Strictly dominated strategies should never be played by a rational payoff-maximizer.

This can simplify payoff matrices before searching for equilibrium.

### Why payoff matrices connect to linear algebra

With mixed strategies, expected payoff becomes a bilinear expression:

E[u₁] = **p**ᵀ U₁ **q**.

So many computations reduce to:

- •multiplying matrices by probability vectors,
- •solving linear equalities from indifference conditions.

That’s why your prerequisites (expected value, matrix operations) are exactly the right foundation.

### Connection to what you’ll learn next

This node gives you the language and baseline equilibrium concept.

Next nodes expand in two directions:

- •**[Nash Equilibrium](/tech-tree/nash-equilibrium)**: existence, computation, best-response dynamics, mixed strategies more systematically.
- •**[Cooperative Games](/tech-tree/cooperative-games)**: what changes when binding agreements and coalition formation are allowed; concepts like the Shapley value.

Keep in mind the central contrast:

- •Non-cooperative: stability without binding commitments.
- •Cooperative: allocations and fairness under possible commitments/coalitions.

## Worked Examples (3)

### Finding a pure-strategy Nash equilibrium by marking best responses

Consider the 2-player game with actions {A, B} for Player 1 (rows) and {X, Y} for Player 2 (columns). Payoffs are (u₁, u₂):

|  | X | Y |
| --- | --- | --- |
| **A** | (2, 1) | (0, 0) |
| **B** | (1, 0) | (1, 2) |

Find all pure-strategy Nash equilibria.

1. Step 1: Compute Player 1’s best responses (maximize u₁) column by column.

   - •If Player 2 plays X: Player 1 gets u₁(A, X) = 2 and u₁(B, X) = 1.

   Best response is A.

   - •If Player 2 plays Y: Player 1 gets u₁(A, Y) = 0 and u₁(B, Y) = 1.

   Best response is B.
2. Step 2: Compute Player 2’s best responses (maximize u₂) row by row.

   - •If Player 1 plays A: Player 2 gets u₂(A, X) = 1 and u₂(A, Y) = 0.

   Best response is X.

   - •If Player 1 plays B: Player 2 gets u₂(B, X) = 0 and u₂(B, Y) = 2.

   Best response is Y.
3. Step 3: Find intersections where both are best-responding.

   - •(A, X): Player 1 best-responds to X with A, and Player 2 best-responds to A with X ⇒ Nash equilibrium.
   - •(B, Y): Player 1 best-responds to Y with B, and Player 2 best-responds to B with Y ⇒ Nash equilibrium.

**Insight:** Pure Nash equilibria are the cells where best-response choices intersect. This game has two equilibria, illustrating equilibrium multiplicity in coordination-like situations.

### Computing a mixed-strategy equilibrium in Matching Pennies via indifference

Matching Pennies payoff matrix (u₁, u₂):

|  | H | T |
| --- | --- | --- |
| **H** | (1, −1) | (−1, 1) |
| **T** | (−1, 1) | (1, −1) |

Let Player 1 play H with probability p, and Player 2 play H with probability q. Find the mixed Nash equilibrium.

1. Step 1: Write Player 1’s expected payoff from choosing a pure action, given Player 2 mixes with probability q on H.

   If Player 1 plays H:

   E[u₁ | H] = 1·q + (−1)·(1 − q)

   = q − (1 − q)

   = 2q − 1.

   If Player 1 plays T:

   E[u₁ | T] = (−1)·q + 1·(1 − q)

   = −q + 1 − q

   = 1 − 2q.
2. Step 2: In a mixed equilibrium where Player 1 randomizes between H and T, Player 1 must be indifferent:

   2q − 1 = 1 − 2q

   ⇒ 2q + 2q = 1 + 1

   ⇒ 4q = 2

   ⇒ q = 1/2.
3. Step 3: Do the symmetric computation for Player 2.

   Player 2’s payoffs are the negative of Player 1’s (zero-sum), but we can still compute indifference.

   If Player 2 plays H, expected u₂ given Player 1 plays H with probability p:

   E[u₂ | H] = (−1)·p + 1·(1 − p)

   = −p + 1 − p

   = 1 − 2p.

   If Player 2 plays T:

   E[u₂ | T] = 1·p + (−1)·(1 − p)

   = p − 1 + p

   = 2p − 1.
4. Step 4: Indifference for Player 2:

   1 − 2p = 2p − 1

   ⇒ 1 + 1 = 2p + 2p

   ⇒ 2 = 4p

   ⇒ p = 1/2.

**Insight:** Each player mixes to make the other indifferent. Here the only stable behavior is randomizing 50/50, because any bias can be exploited by the opponent.

### Expected payoff as a matrix expression: E[u₁] = \*\*p\*\*ᵀ U₁ \*\*q\*\*

Player 1 payoff matrix:

U₁ = [ [4, 0],

[1, 2] ]

Player 1 plays Top with probability p, Player 2 plays Left with probability q. Compute E[u₁] two ways: (1) by explicit expectation, (2) by matrix multiplication.

1. Step 1: Parameterize mixed strategies.

   Player 1: **p** = (p, 1 − p).

   Player 2: **q** = (q, 1 − q).
2. Step 2: Explicit expectation over the four outcomes.

   E[u₁] = u₁(Top, Left)·P(Top, Left)

   - •u₁(Top, Right)·P(Top, Right)
   - •u₁(Bottom, Left)·P(Bottom, Left)
   - •u₁(Bottom, Right)·P(Bottom, Right)

   = 4·(p q) + 0·(p(1 − q)) + 1·((1 − p)q) + 2·((1 − p)(1 − q))

   Now simplify:

   E[u₁] = 4pq + (1 − p)q + 2(1 − p)(1 − q)

   = 4pq + q − pq + 2(1 − p − q + pq)

   = 4pq + q − pq + 2 − 2p − 2q + 2pq

   = (4pq − pq + 2pq) + (q − 2q) + (2 − 2p)

   = 5pq − q + 2 − 2p.
3. Step 3: Matrix method.

   Compute U₁ **q**:

   U₁ **q** = [ 4q + 0(1 − q),

   1q + 2(1 − q) ]

   = [ 4q,

   q + 2 − 2q ]

   = [ 4q,

   2 − q ].

   Now multiply by **p**ᵀ:

   E[u₁] = **p**ᵀ (U₁ **q**)

   = (p, 1 − p) · (4q, 2 − q)

   = 4pq + (1 − p)(2 − q)

   = 4pq + 2 − q − 2p + pq

   = 5pq − q + 2 − 2p.

**Insight:** The matrix form **p**ᵀ U₁ **q** is just expected value written compactly. It scales to larger action sets and makes equilibrium computation feel like linear algebra.

## Key Takeaways

- ✓

  A game models strategic interdependence: your best choice depends on what others do, and vice versa.
- ✓

  A strategy sᵢ can be a pure action or a mixed strategy (a probability distribution over actions).
- ✓

  Payoffs are utilities uᵢ(s) assigned to each player i for every strategy profile s = (s₁, …, sₙ).
- ✓

  Under mixed strategies, players maximize expected payoff; for 2-player finite games E[u₁] = **p**ᵀ U₁ **q**.
- ✓

  A Nash equilibrium s\* is a strategy profile where no player can improve payoff by unilateral deviation.
- ✓

  Pure Nash equilibria in matrices can be found by intersecting best responses.
- ✓

  Some games have no pure Nash equilibrium; mixed equilibria arise when players randomize to make opponents indifferent.
- ✓

  Nash equilibrium is about stability, not necessarily efficiency or fairness.

## Common Mistakes

- ✗

  Confusing Nash equilibrium with the socially best outcome (maximizing ∑ᵢ uᵢ). They can differ dramatically (e.g., Prisoner’s Dilemma).
- ✗

  Treating mixed strategies as “irrational randomness” rather than a deliberate optimal plan to avoid exploitation or ensure stability.
- ✗

  Forgetting the unilateral nature of Nash equilibrium: it blocks single-player deviations, not coordinated deviations by multiple players.
- ✗

  Misreading payoff matrices (mixing up whose payoff is first, or scanning rows/columns incorrectly when identifying best responses).

## Practice

easy

Consider Prisoner’s Dilemma with payoffs:

|  | C | D |
| --- | --- | --- |
| **C** | (3, 3) | (0, 5) |
| **D** | (5, 0) | (1, 1) |

(a) Find Player 1’s best response to C and to D.

(b) Find Player 2’s best response to C and to D.

(c) Identify the Nash equilibrium (or equilibria).

**Hint:** Best response means “higher own payoff holding the other fixed.” Compare numbers within a column for Player 1 and within a row for Player 2.

Show solution

(a) If Player 2 plays C: Player 1 gets 3 from C and 5 from D ⇒ best response is D.

If Player 2 plays D: Player 1 gets 0 from C and 1 from D ⇒ best response is D.

(b) Symmetric reasoning: if Player 1 plays C, Player 2 best response is D (5 > 3). If Player 1 plays D, Player 2 best response is D (1 > 0).

(c) Both players best-respond with D regardless ⇒ (D, D) is the (unique) Nash equilibrium.

medium

In the coordination game:

|  | Left | Right |
| --- | --- | --- |
| **Up** | (2, 2) | (0, 0) |
| **Down** | (0, 0) | (2, 2) |

(a) List all pure Nash equilibria.

(b) Is (Up, Right) a Nash equilibrium? Explain using unilateral deviation.

**Hint:** A pure Nash equilibrium must be a best response for each player at the same cell.

Show solution

(a) (Up, Left) is a Nash equilibrium: given Left, Player 1 prefers Up (2 > 0); given Up, Player 2 prefers Left (2 > 0). Similarly (Down, Right) is a Nash equilibrium.

(b) (Up, Right) is not: given Right, Player 1 prefers Down (2 > 0), so Player 1 can unilaterally deviate and improve.

medium

Let Player 1’s payoff matrix be

U₁ = [ [3, 1],

[0, 2] ]

Player 1 plays Top with probability p and Player 2 plays Left with probability q.

Compute E[u₁] as a simplified expression in p and q.

**Hint:** Use E[u₁] = **p**ᵀ U₁ **q** with **p** = (p, 1 − p), **q** = (q, 1 − q).

Show solution

Compute U₁ **q**:

U₁ **q** = [ 3q + 1(1 − q),

0·q + 2(1 − q) ]

= [ 3q + 1 − q,

2 − 2q ]

= [ 1 + 2q,

2 − 2q ].

Then E[u₁] = (p, 1 − p) · (1 + 2q, 2 − 2q)

= p(1 + 2q) + (1 − p)(2 − 2q)

= p + 2pq + 2 − 2q − 2p + 2pq

= 2 − 2q − p + 4pq.

## Connections

Next, go deeper into equilibrium concepts and computation in [Nash Equilibrium](/tech-tree/nash-equilibrium/). For settings where binding agreements and coalition formation matter, see [Cooperative Games](/tech-tree/cooperative-games/).

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
