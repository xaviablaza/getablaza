---
title: Mixed Strategies
description: Mixed strategy Nash equilibria. Support conditions, indifference principle. Maximin strategies and safety levels. Existence theorems.
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
permalink: /tech-tree/mixed-strategies/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Mixed Strategies

Game TheoryDifficulty: ★★★★☆Depth: 8Unlocks: 0

Mixed strategy Nash equilibria. Support conditions, indifference principle. Maximin strategies and safety levels. Existence theorems.

## Prerequisites (2)

[Nash Equilibrium5 atoms](/tech-tree/nash-equilibrium/)[Common Distributions6 atoms](/tech-tree/common-distributions/)

Advanced Learning Details

### Graph Position

106

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

8

Chain Length

When players randomize deliberately, they can secure outcomes that no pure strategy achieves — mixed strategies are the hidden leverage behind many strategic puzzles, from auctions to security patrols.

TL;DR:

Mixed-strategy Nash equilibria are probability distributions over pure actions that satisfy support and indifference conditions; they yield safety levels (maximin values) in zero-sum settings and always exist for finite games via fixed-point theorems.

## What Is Mixed Strategy? — Definition, motivation, and intuition

Definition and basic idea

A mixed strategy for a player in a finite game is a probability distribution over that player's pure strategies. If player i has a finite set of pure actions A\_i = {a\_1, ..., a\_m}, a mixed strategy is a vector p = (p\_1, ..., p\_m) with p\_j >= 0 and \sum\_j p\_j = 1. A mixed-strategy profile is a tuple of such distributions, one per player. A mixed-strategy Nash equilibrium is a profile of mixed strategies such that no player can increase her expected payoff by unilaterally switching her distribution.

Why randomize? Motivation and examples

Randomization can be strategically necessary when no pure Nash equilibrium exists or when mixing raises a player's worst-case guarantee. Two canonical motivations:

1) Indifference and unpredictability. In zero-sum or adversarial environments, making yourself unpredictable prevents opponents from exploiting you. Matching Pennies has no pure Nash equilibrium, but mixing p = (1/2, 1/2) for both players is an equilibrium.

Numeric example: Matching Pennies. Payoff matrix to row player (column gets negative):

- •If row plays Heads (H) and column plays Heads (H): row gets +1.
- •H vs Tails (T): row gets -1.
- •T vs H: row gets -1.
- •T vs T: row gets +1.

If row plays H with probability p and column plays H with probability q, row's expected payoff is

urow(p,q)=(2q−1)(2p−1)u\_{row}(p,q) = (2q-1)(2p-1)urow​(p,q)=(2q−1)(2p−1)

(You can compute directly: u = p q  *1 + p(1-q)*  (-1) + (1-p)q  *(-1) + (1-p)(1-q)*  1.)

Setting p = q = 1/2 yields expected payoff 0 to both; unilateral deviation doesn't improve payoff, so it's a mixed Nash equilibrium.

2) Safety levels and maximin strategies. In competitive settings, mixing is used to maximize the minimum (safety) payoff, also called the maximin value. In zero-sum games the maximin strategy of a player coincides with the Nash strategy and is found by solving a minimax problem.

Support and the indifference principle: core intuitions

Two central concepts for mixed equilibria are support and the indifference principle. The support of a mixed strategy is the set of pure strategies assigned positive probability. In a mixed-strategy equilibrium, every pure strategy in a player's support must yield the same expected payoff against the opponents' mixed strategies; otherwise the player would shift probability mass to the better strategy. This is the indifference principle.

Concretely: suppose player 1 mixes over actions a and b with positive probabilities in equilibrium against opponents' mixed profile s\_{-1}. Then

u1(a,s−1)=u1(b,s−1)=v1,u\_1(a, s\_{-1}) = u\_1(b, s\_{-1}) = v\_1,u1​(a,s−1​)=u1​(b,s−1​)=v1​,

where v\_1 is the equilibrium expected payoff to player 1. Any pure action outside the support must yield a payoff no greater than v\_1; otherwise it would enter the support.

Formal existence (preview)

In finite games, mixed-strategy Nash equilibria always exist (Nash's theorem). The existence proof constructs a continuous best-response map on the compact, convex set of mixed profiles and applies Brouwer or Kakutani fixed-point theorems. A consequence: even when pure equilibria fail, mixing salvages equilibrium.

What this section prepares you to do

After this section you should: (i) know the definition of a mixed strategy and mixed Nash equilibrium, (ii) understand why supports and indifference matter, and (iii) appreciate the role of mixed strategies in guaranteeing safety levels in adversarial settings. In the next sections we will convert these intuitive statements into algebraic conditions you can solve to find equilibria and maximin strategies.

Connection with prerequisites

In "Nash Equilibrium (d3)" we learned the idea that no player benefits from unilateral deviation; here we extend that to probability distributions over actions. In "Common Distributions (d2)" you have the calculus of probability distributions — we will use discrete distributions for finite games and continuous distributions for auctions/examples.

## Core Mechanic 1: Support conditions and the indifference principle (solving for mixed equilibria)

Statement of the indifference principle

Let player i have k pure strategies indexed 1..k and let the opponents' mixed profile be s\_{-i}. If player i places positive probability on a subset S (the support), then for all a in S,

ui(a,s−i)=Viu\_i(a, s\_{-i}) = V\_iui​(a,s−i​)=Vi​

for some constant V\_i (player i's equilibrium payoff). For any a \notin S, we must have

ui(a,s−i)≤Vi.u\_i(a, s\_{-i}) \le V\_i.ui​(a,s−i​)≤Vi​.

Thus the support yields linear equalities and inequalities that pin down the opponents' probabilities.

Solving two-player games: linear equations

In two-player finite games, solving for a mixed equilibrium reduces to solving linear equations that enforce indifference across the support. Consider a 2x2 game where row has actions R1,R2 and column has actions C1,C2. Let row mix with probability p on R1 (so 1-p on R2), and column mix with q on C1 (1-q on C2). Suppose both players mix (support includes both pure actions). Then indifference gives two linear equations:

Row indifferent: u\_row(R1, q) = u\_row(R2, q)

Column indifferent: u\_col(p, C1) = u\_col(p, C2)

Example: Battle of the Sexes

Payoff matrix (row, column), numbers listed as (row payoff, column payoff):

- •(Opera, Opera): (2,1)
- •(Opera, Football): (0,0)
- •(Football, Opera): (0,0)
- •(Football, Football): (1,2)

Let row play Opera with probability p, column play Opera with probability q. Compute expected payoffs.

Row's expected payoff of Opera: u\_row(Opera,q) = 2q + 0(1-q) = 2q.

Row's expected payoff of Football: u\_row(Football,q) = 0 q + 1(1-q) = 1 - q.

Indifference for Row (if mixing both): 2q = 1 - q => 3q = 1 => q = 1/3. Numeric example: q = 1/3 means Column plays Opera with probability 1/3.

Column's expected payoff of Opera: u\_col(p, Opera) = 1 p + 0 (1-p) = p.

Column's expected payoff of Football: u\_col(p, Football) = 0 p + 2 (1-p) = 2(1 - p).

Indifference for Column: p = 2(1 - p) => 3p = 2 => p = 2/3. Numeric example: Row plays Opera with probability p = 2/3.

So the unique mixed-strategy Nash equilibrium (where both mix) is p = 2/3, q = 1/3, giving expected payoffs V\_row = 2q = 2/3 and V\_col = p = 2/3.

Support enumeration and elimination

A systematic method to find mixed equilibria in small games is support enumeration: enumerate candidate supports (combinations of actions with positive probability), solve indifference equalities to obtain probability distributions, and check inequality constraints for excluded actions. For an n-action player, a support of size s yields s-1 independent equalities (normalization provides the last equation), so unknown probabilities are determined by solving linear systems. This is why algorithmic equilibrium solvers like Lemke-Howson enumerate supports.

Concrete algebraic worked mini-example: Matching Pennies (again, 2x2 zero-sum)

Row payoff matrix (same as section 1): +1 on matching, -1 on mismatch. Suppose row mixes p on Heads; column mixes q on Heads. Row's expected payoff of Heads is

u\_{row}(H,q) = q \cdot 1 + (1-q) \cdot (-1) = 2q - 1.$$ Row's expected payoff of Tails is
$$u\_{row}(T,q) = q \cdot (-1) + (1-q) \cdot 1 = 1 - 2q.$$ Indifference 2q - 1 = 1 - 2q => 4q = 2 => q = 1/2. Symmetrically p = 1/2.
This demonstrates typical algebra: equate expected payoffs of actions in the support and solve linear equations.
Why supports can be small
In equilibrium supports are often small relative to the full set of actions. For two-player games, a player who mixes over s actions forces the opponent to solve s indifference equalities, usually determining the opponent's mixed strategy uniquely. This constraint is why many equilibrium supports are small and why mixed equilibria are tractable by linear algebra in small games.
Edge cases and degenerate games
If a player's indifference equalities lead to negative probabilities or probabilities >1, that candidate support is infeasible. If equalities leave free parameters, there may be a continuum of equilibria (e.g., games with payoff ties or dominance relations). If only one pure action survives the inequalities, the equilibrium is pure.
What you should be able to do
Given a small two-player game, set up indifference equations for candidate supports, solve the resulting linear system, and verify inequality constraints for excluded actions.

## Core Mechanic 2: Maximin strategies, zero-sum games, and existence theorems

Maximin strategies and safety levels (definitions)

For player i, a maximin strategy maximizes the player's minimum payoff against any opponents' strategies. Formally, for a two-player game with row player R and column player C, R's maximin value is

max⁡p∈Δ(AR)min⁡q∈Δ(AC)uR(p,q).\max\_{p \in \Delta(A\_R)} \min\_{q \in \Delta(A\_C)} u\_R(p,q).p∈Δ(AR​)max​q∈Δ(AC​)min​uR​(p,q).

A strategy p^ *achieving this value is a maximin strategy and guarantees the safety level V\_R = \min\_q u\_R(p^*,q).

In zero-sum games, u\_C = -u\_R, and von Neumann's minimax theorem states:

max⁡pmin⁡quR(p,q)=min⁡qmax⁡puR(p,q).\max\_p \min\_q u\_R(p,q) = \min\_q \max\_p u\_R(p,q).pmax​qmin​uR​(p,q)=qmin​pmax​uR​(p,q).

Thus the maximin equals the minimax, and furthermore both players have mixed strategies achieving those values.

Numeric example: simple zero-sum 2x2

Payoff to row:

\begin{array}{c|cc}

& C1 & C2 \\

\hline

R1 & 2 & -1 \\

R2 & 0 & 1 \\

\end{array}

Find row's maximin strategy. Let row mix p on R1. For a given column pure C1, row's expected payoff is 2p + 0(1-p) = 2p. Against C2 it's -1 p + 1(1-p) = 1 - 2p. The worst-case payoff (as column can pick best response to minimize row's payoff) is

w(p) = \min\{2p, 1 - 2p\}.$$ To maximize w(p), set 2p = 1 - 2p => 4p = 1 => p = 1/4. Then the safety value is w(1/4) = 2\*(1/4) = 1/2.
Hence row's maximin strategy is p = 1/4, guaranteeing 1/2. Equation solving here mirrors indifference: equate the payoffs against the column's pure strategies to raise the lowest of them.
Maximin vs Nash in general-sum games
In general-sum games, a player's maximin strategy need not be a Nash strategy. Maximin focuses on worst-case guarantees while Nash involves mutual best responses. However, in two-player zero-sum games the maximin strategy for each player is a Nash equilibrium strategy because the opponent's best reply is to minimize the player's payoff and that is exactly what the minimax theorem addresses.
Proof sketch of existence of mixed Nash equilibria (finite games)
Nash's theorem (finite version): Every finite game has at least one mixed-strategy Nash equilibrium.
Sketch via Brouwer: Let X be the product of simplices of mixed strategies for each player; X is compact and convex. Define a continuous 'better-response' map f: X -> X that, for each player, takes the current profile and reassigns probabilities by shifting weight toward best replies (e.g., use a smoothized best-response like the logit or a projection of best-reply payoffs). By Brouwer fixed-point theorem, f has a fixed point s\*. At s\*, each player's current mixed strategy coincides with the response generated by f, meaning no profitable unilateral deviation exists — hence s\* is a Nash equilibrium.
Sketch via Kakutani: define the best-response correspondence B: X => X mapping each profile to the set of best-responses. B is non-empty, convex-valued, and has a closed graph; Kakutani's fixed-point theorem guarantees a fixed point, which is a Nash equilibrium.
Concrete numeric intuition: Why continuity and convexity matter
Consider the product simplex for two players: two-dimensional square for 2x2 games. Best-response sets are closed convex subsets of the simplex. Fixed points correspond to intersections of best responses — exactly Nash equilibria. In matching pennies the best-response graphs intersect only at the interior point (1/2,1/2).
Computing maximin strategies via linear programming
For larger zero-sum games, compute the maximin strategy by solving an LP. For row player with payoff matrix A (m x n), solve:
maximize v
subject to p^T A >= v 1^T
\sum\_j p\_j = 1, p\_j >= 0.
Numeric example: previous 2x2 example corresponds to solving maximize v s.t.
2 p + 0 (1-p) >= v, -1 p + 1(1-p) >= v, p in [0,1]. Solving gives p = 1/4, v = 1/2.
What this section gives you
You now know how to compute safety levels (maximin), understand their equivalence with Nash strategies in zero-sum games via the minimax theorem, and have a sketch of the existence proof for mixed equilibria in finite games. In practice this lets you compute robust strategies and reason about equilibrium existence in finite strategic settings.

## Applications and Connections — where mixed strategies matter and where they lead

Auctions: bidding strategies as mixed equilibria

In many auction formats, especially first-price sealed-bid auctions with symmetric private values, bidders randomize in equilibrium. Consider n bidders, each with value v drawn independently from Uniform[0,1]. A symmetric Bayes–Nash equilibrium bidding function in the first-price auction is

b(v)=n−1nv.b(v) = \frac{n-1}{n} v.b(v)=nn−1​v.

Numeric example: for n=2, b(v) = v/2. If a bidder's valuation is v = 0.6, she bids b = 0.3.

Derivation sketch (why this is a mixed-continuous equilibrium): A bidder choosing a bid b given value v trades off increasing bid (raising chance to win) and paying more if she wins. Symmetric equilibrium leads to an ODE solved by straightforward calculus; the solution for uniform [0,1] yields the closed-form above. The continuous bidding function induces a distribution over bids (a continuous mixed strategy).

Security games and patrols

Defenders in security settings often randomize patrols across locations to avoid being predictable. Suppose there are two targets T1 and T2 with values x1 and x2 to the attacker; defender chooses a probability p to cover T1. The attacker then chooses the less-protected target. The defender's indifference condition sets p so that attacker is indifferent. Numeric example: if targets worth (10,6) and defender's coverage prevents attack, defender sets p so expected value of attacking either target is equal — yielding a specific p computed from those numbers.

Evolutionary dynamics and mixed equilibria

In evolutionary game theory, mixed Nash equilibria correspond to population states in which strategies co-exist in stable proportions. The indifference principle appears as equal average fitness across strategies in the support. Rock-Paper-Scissors (RPS) has a symmetric mixed NE p = (1/3, 1/3, 1/3). Numeric example: payoffs for RPS standard are 0 for ties, +1 for wins, -1 for losses. The symmetric uniform mix yields expected payoff 0 for every pure strategy, satisfying indifference.

Mechanism design and implementation

Mixed strategies feature in equilibrium constructs for mechanism design: designers must account for the possibility that agents randomize (e.g., mixed-strategy equilibria in matching markets, entry deterrence via mixed strategies). Knowledge of mixed-equilibrium existence is crucial when checking implementability.

Algorithmic game theory and complexity

From a computational perspective, computing a mixed Nash equilibrium for two-player games can be reduced to solving a linear complementarity problem; the Lemke–Howson algorithm finds one for bimatrix games. More broadly, finding Nash equilibria is PPAD-complete for games with >2 players or general bimatrix games — so while existence is guaranteed, computation can be hard.

Correlated equilibrium and refinement

Correlated equilibria generalize mixed equilibria by allowing a mediator to correlate players' strategies. Mixed equilibria are a subset of correlated equilibria. Mixed strategies set the stage: understanding support and indifference helps when analyzing correlated signals that induce the same indifference conditions.

Learning in games: fictitious play and regret minimization

Learning dynamics often converge to mixed equilibria or to sets that contain them. In two-player zero-sum games, no-regret algorithms converge (in average play) to the set of minimax strategies. Practical systems employing online learning (e.g., in security resource allocation) therefore effectively play mixed strategies.

Concrete applied example: network security patrol

Suppose a defender must patrol two segments of a network; attacks yield losses L1 = 100 and L2 = 40. If coverage prevents attack completely, defender chooses p to cover segment 1 with probability p so that attacker's expected payoff from attacking either segment is equal:

Attacker payoff when attacking 1: (1 - p) \* 100.

Attacker payoff when attacking 2: (1 - (1 - p))  *40 = p*  40.

Indifference (if attacker is indifferent): (1 - p) 100 = p 40 => 100 - 100 p = 40 p => 140 p = 100 => p = 100/140 = 5/7 ≈ 0.714. Numeric result: defender covers segment 1 ~71.4% of the time.

Where this leads you next

Mastering mixed strategies opens the door to Bayesian games (private information and continuous mixed strategies), auctions (bidding functions and equilibrium distributions), evolutionary stability (ESS vs mixed NE), correlated equilibria, learning algorithms and their convergence properties, and computational complexity of equilibrium computation (PPAD). Each of those directions depends on support/indifference reasoning and maximin thinking cultivated here.

## Worked Examples (3)

### Matching Pennies (2x2)

Row/Column both choose Heads (H) or Tails (T). Row gets +1 for matching, -1 for mismatch. Find mixed Nash equilibrium probabilities.

1. Let row play Heads with probability p (so Tails with 1-p). Let column play Heads with probability q (Tails with 1-q).
2. Compute row's expected payoff for Heads: u\_row(H,q) = q*1 + (1-q)*(-1) = 2q - 1. For Tails: u\_row(T,q) = q*(-1) + (1-q)*1 = 1 - 2q.
3. Impose indifference if row mixes (both actions in support): 2q - 1 = 1 - 2q => 4q = 2 => q = 1/2.
4. By symmetry, column's indifference gives p = 1/2. So the equilibrium is (p,q) = (1/2,1/2).
5. Expected payoff to each player is 0: u\_row(1/2,1/2) = 0.

**Insight:** This example shows the indifference principle in its simplest form: mixing equalizes opponents' incentives, and in zero-sum games the equilibrium often has uniform mixing when payoffs are symmetric.

### Battle of the Sexes (2x2) — mixed equilibrium

Payoffs: (Opera,Opera)=(2,1), (Opera,Football)=(0,0), (Football,Opera)=(0,0), (Football,Football)=(1,2). Find mixed Nash equilibrium where both players randomize.

1. Let row play Opera with probability p; column play Opera with probability q.
2. Row's expected payoff for Opera: u\_row(Opera,q) = 2q. For Football: u\_row(Football,q) = 1 - q.
3. If row mixes, indifference: 2q = 1 - q => 3q = 1 => q = 1/3. Numeric result: column plays Opera with prob 1/3.
4. Column's expected payoff for Opera: u\_col(p,Opera) = p. For Football: u\_col(p,Football) = 2(1 - p). Indifference: p = 2(1 - p) => 3p = 2 => p = 2/3.
5. Thus the mixed-strategy Nash equilibrium is p = 2/3 (row Opera), q = 1/3 (column Opera). Each player's expected payoff is 2/3.

**Insight:** This example shows solving two indifference equalities simultaneously; note how supports (both pure actions) lead to unique interior probabilities.

### First-price sealed-bid auction (symmetric Bayes–Nash equilibrium)

n bidders, independent private values v ~ Uniform[0,1]. Each bidder submits a bid; highest wins and pays her bid. Find the symmetric equilibrium bidding function b(v).

1. Assume a symmetric equilibrium where every other bidder uses bidding function b(·), strictly increasing. A bidder with value v who bids b wins iff her bid exceeds the maximum of the other n-1 bids. Since others use b, the probability of winning with bid b(x) when your bid corresponds to value x is Pr(max of others' values <= x) = x^{n-1} (because values are iid Uniform[0,1]).
2. Consider a bidder with true valuation v who deviates to bid b(x), where x is the hypothetical value corresponding to that bid; expected payoff is (v - b(x)) x^{n-1}. In equilibrium, truthful bidding mapping b(v) must maximize this expression at x = v.
3. Take derivative wrt x and set to zero at x = v: derivative of (v - b(x)) x^{n-1} equals (v - b(x)) (n-1) x^{n-2} - b'(x) x^{n-1}. Evaluate at x = v and set equal to zero:

   (v−b(v))(n−1)vn−2−b′(v)vn−1=0.(v - b(v)) (n-1) v^{n-2} - b'(v) v^{n-1} = 0.(v−b(v))(n−1)vn−2−b′(v)vn−1=0.
4. Rearrange to ODE form:

   b′(v)=n−1v(v−b(v)).b'(v) = \frac{n-1}{v} (v - b(v)).b′(v)=vn−1​(v−b(v)).
5. Solve the linear first-order ODE. Rewrite as

   b'(v) + \frac{n-1}{v} b(v) = n - 1.$$ The integrating factor is v^{n-1}. Multiply both sides and integrate:
   $$\frac{d}{dv} [v^{n-1} b(v)] = (n-1) v^{n-1}.$$ Integrate from 0 to v:
   $$v^{n-1} b(v) = \int\_0^v (n-1) t^{n-1} dt = v^n.$$ Hence
   $$b(v) = \frac{v^n}{v^{n-1}} = \frac{n-1}{n} v.
6. Hence symmetric equilibrium bidding function is b(v) = (n-1)/n \* v. Numeric example: for n = 2, b(v) = v/2; for v = 0.6, b = 0.3.

**Insight:** This worked example shows continuous mixed strategies (a distribution induced by a bid function) and how calculus/differential equations produce closed-form equilibria in auctions. It uses the prerequisite "Common Distributions (d2)" for uniform distribution properties.

## Key Takeaways

- ✓

  A mixed strategy is a probability distribution over pure actions; a mixed Nash equilibrium is a profile of such distributions with no profitable unilateral deviation.
- ✓

  Support and the indifference principle: in equilibrium every pure action played with positive probability must yield equal expected payoff against the opponents' mixed strategies.
- ✓

  In two-player games, interior mixed equilibria are found by solving linear indifference equalities; supports must be checked for feasibility (probabilities within [0,1]).
- ✓

  In zero-sum games maximin strategies coincide with Nash equilibrium strategies by the minimax theorem; compute them via indifference or linear programming.
- ✓

  Every finite game has at least one mixed Nash equilibrium (Nash's theorem) via fixed-point arguments (Brouwer/Kakutani).
- ✓

  Mixed strategies are essential in auctions, security/resource allocation, evolutionary dynamics, and algorithmic game theory; they can be continuous (e.g., bid distributions) or discrete.
- ✓

  Computationally, enumeration of supports and linear/algebraic methods can solve small games; larger games may require LP, Lemke–Howson, or face computational hardness (PPAD).

## Common Mistakes

- ✗

  Assuming that every action must give the same payoff — only actions in the support must yield equal payoffs; excluded actions may give strictly lower payoffs.
- ✗

  Confusing maximin with Nash: in general-sum games a maximin strategy maximizes worst-case payoff but is not necessarily a Nash strategy; equality holds in zero-sum games only.
- ✗

  Solving indifference equations without checking feasibility: you must verify the solution yields probabilities in [0,1] and that excluded actions are not better.
- ✗

  Thinking mixed strategies are mere random noise: they are deliberate strategic choices that enforce indifference and can be computed analytically.

## Practice

easy

Easy: Consider the 2x2 zero-sum game with payoff matrix to row: [[1,-2],[-1,2]]. Find the row player's maximin strategy p (probability on first row) and the safety value.

**Hint:** Let row play first row with probability p. Compute payoff against column pure strategies and equate them to maximize the minimum.

Show solution

Let p be prob of R1. Payoff against C1: 1*p + (-1)*(1-p) = 2p -1. Against C2: -2*p + 2*(1-p) = 2 -4p. Worst-case is min{2p-1, 2-4p}. Equate 2p -1 = 2 -4p => 6p = 3 => p = 1/2. Safety value = 2p -1 = 0.

medium

Medium: For the following 2x2 game (row payoffs listed): (R1,C1)=3, (R1,C2)=0, (R2,C1)=0, (R2,C2)=2. Column's payoffs are different but irrelevant here. Find the mixed-strategy Nash equilibrium where both players mix, using indifference.

**Hint:** Let row mix p on R1, column mix q on C1. Use indifference on both players (you need column payoffs — assume column gets 1 at (R1,C1), 2 at (R1,C2), 0 at (R2,C1), 3 at (R2,C2)).

Show solution

Row's expected payoff: u\_row(R1,q)=3q+0(1-q)=3q; u\_row(R2,q)=0 q + 2(1-q)=2-2q. Indifference for row: 3q = 2 - 2q => 5q = 2 => q = 2/5. Column's expected payoffs: u\_col(p,C1)=1 p + 0(1-p)=p; u\_col(p,C2)=2 p + 3(1-p)=3 - p. Indifference: p = 3 - p => 2p = 3 => p = 3/2 which is infeasible. Therefore the assumption that column mixes over both actions is invalid; check pure best responses. If column plays C2 pure (q=0), row best response is R2 (gives 2 vs 0), so equilibrium is (R2, C2) pure. Thus no interior mixed equilibrium exists; the mixed attempt failed feasibility check.

hard

Hard: Derive the symmetric Bayes–Nash equilibrium bidding function for n=3 bidders in the first-price sealed-bid auction when values are iid Uniform[0,1]. Then compute the bid for v=0.9.

**Hint:** Use the ODE derived in the worked example: b'(v) = (n-1)/v (v - b(v)). For n=3 solve the ODE and substitute v=0.9.

Show solution

For n=3 the ODE is b'(v) = 2/v (v - b(v)). Rewrite as b'(v) + (2/v) b(v) = 2. Integrating factor is v^2. Then d/dv[v^2 b(v)] = 2 v^2. Integrate: v^2 b(v) = (2/3) v^3 + C. At v=0, b(0)=0 implies C=0. So b(v) = (2/3) v. For v=0.9, b = (2/3)\*0.9 = 0.6.

## Connections

Looking back: In "Nash Equilibrium (d3)" we learned that equilibrium is a profile with no profitable unilateral deviations; mixed equilibria extend that same notion to probability distributions over pure strategies. The indifference principle is directly derived from the definition in that when a player randomizes across actions in equilibrium, those actions must be best responses (hence equal expected payoffs). From "Common Distributions (d2)" we used properties of the Uniform distribution to derive closed-form bidding functions in auctions and to compute probabilities of order statistics (e.g., x^{n-1} for the maximum of n-1 iid Uniform[0,1] draws).

Looking forward: Mastery of mixed strategies is prerequisite for Bayesian games (private information and continuous strategy distributions), mechanism design (incentive compatibility under potential mixed play), correlated equilibrium (which generalizes mixed strategies and uses similar indifference constraints), evolutionary game theory (population mixes and ESS calculations), and algorithmic game theory (computational methods for equilibrium like Lemke–Howson, LP-based solvers, and complexity classes such as PPAD). It also underpins practical applications such as auction design, security resource allocation, and equilibrium learning algorithms (fictitious play, regret minimization) that rely on the concept of mixing to guarantee unpredictability and robustness.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
