---
title: Repeated Games
description: Finitely and infinitely repeated games. Folk theorem, trigger strategies, grim trigger. Discount factors and cooperation sustainability.
date: '2026-07-01'
scheduled: '2026-12-18'
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
inspiration_url: https://templeton.host/tech-tree/repeated-games/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/repeated-games/](https://templeton.host/tech-tree/repeated-games/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Repeated Games

Game TheoryDifficulty: ★★★★☆Depth: 8Unlocks: 1

Finitely and infinitely repeated games. Folk theorem, trigger strategies, grim trigger. Discount factors and cooperation sustainability.

## Prerequisites (2)

[Nash Equilibrium5 atoms](/tech-tree/nash-equilibrium/)[Dynamic Programming6 atoms](/tech-tree/dynamic-programming/)

## Unlocks (1)

[Dynamic Gameslvl 5](/tech-tree/dynamic-games/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[UpsellBusiness

Upsell is sustained by the repeated-game structure of the customer relationship: satisfaction in prior rounds (purchases) raises the discount-weighted expected value of future cooperation (additional purchases, referrals), exactly the Folk Theorem mechanism that sustains cooperation in infinitely repeated games](/business/upsell/)[Vendor NegotiationsBusiness

Quarterly cadence makes this literally a repeated game. Folk theorem, discount factors, and trigger strategies explain why long-term vendor relationships sustain cooperative pricing that one-shot negotiations cannot.](/business/vendor-negotiations/)

Advanced Learning Details

### Graph Position

142

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

8

Chain Length

Repeated interaction transforms one-shot incentives: cooperation that is impossible in a single play can become stable when players meet again. Understanding repeated games explains collusion, reputation, and long-run enforcement without a central authority.

TL;DR:

Repeated games study how strategic behavior changes when a stage game is played multiple times (finitely or infinitely), and show how trigger strategies and discounting let players sustain cooperation — formalized by the Folk Theorem.

## What Is Repeated Games?

Definition and motivation

A repeated game arises when a base (stage) game G is played multiple times by the same players, with each play called a period. Two canonical settings are:

- •Finitely repeated game: G is played for a known number T of periods.
- •Infinitely repeated game: G is played indefinitely (or with a constant-probability continuation each period). Often modeled with a common discount factor δ∈[0,1)\delta \in [0,1)δ∈[0,1).

Why care? Many real-world strategic interactions are repeated: firms set prices across many periods, countries engage in sequential diplomacy, or sellers build reputations. Repetition changes incentives because the future consequences of today's actions can be used as leverage.

Formal setup

Let the stage game G have players i=1,...,n, action sets AiA\_iAi​, and payoff functions ui(a)u\_i(a)ui​(a) for action profile a=(a1,...,an)a=(a\_1,...,a\_n)a=(a1​,...,an​). A repeated game with discount factor δ\deltaδ gives total payoff to player i the discounted sum

Ui=(1−δ)∑t=0∞δtui(at)U\_i = (1-\delta)\sum\_{t=0}^{\infty} \delta^t u\_i(a^t)Ui​=(1−δ)t=0∑∞​δtui​(at)

where the (1−δ)(1-\delta)(1−δ) normalization is conventional (it makes the infinite sum comparable to a per-period payoff); if you prefer undiscounted present value use ∑t=0∞δtui(at)\sum\_{t=0}^\infty \delta^t u\_i(a^t)∑t=0∞​δtui​(at). Concrete numeric example: Suppose the stage payoff from mutual cooperation is R=3R=3R=3 every period and δ=0.9\delta=0.9δ=0.9. Then the normalized discounted value of perpetual cooperation is

U=(1−0.9)∑t=0∞0.9t⋅3=0.1⋅3⋅11−0.9=3.U = (1-0.9)\sum\_{t=0}^{\infty} 0.9^t \cdot 3 = 0.1 \cdot 3 \cdot \frac{1}{1-0.9} = 3.U=(1−0.9)t=0∑∞​0.9t⋅3=0.1⋅3⋅1−0.91​=3.

Relation to prerequisites

In "Nash Equilibrium" we learned to analyze one-shot games by checking unilateral profitable deviations. In repeated games, we use that concept period-by-period but also condition on future strategies. In "Dynamic Programming" we learned to think in terms of continuation values and Bellman equations; that viewpoint is essential when proving that certain strategy profiles are subgame-perfect equilibria (SPE) by the one-deviation principle or via recursive incentive constraints.

Basic intuition: horizon matters

- •Finitely repeated games often reduce (by backward induction) to playing a stage-game Nash equilibrium every period when the stage game has a unique Nash equilibrium. Example: Prisoner’s Dilemma (PD) with unique stage NE (Defect, Defect) yields universal defection in every period for finite T.

- •Infinitely repeated games can sustain outcomes that are not stage-game Nash equilibria because future punishments (or rewards) change the payoff calculus of deviations. The classic vehicle is a trigger strategy: cooperate as long as history shows cooperation, but if someone defects, switch to a punishment phase.

Concrete stage-game example used throughout

Use the symmetric Prisoner’s Dilemma with payoffs: Temptation T=5T=5T=5, Reward R=3R=3R=3, Punishment P=1P=1P=1, Sucker S=0S=0S=0 with ordering T>R>P>ST>R>P>ST>R>P>S. The one-shot Nash equilibrium is (D,D) giving both players payoff 1. Yet in repeated play, cooperative payoff R=3R=3R=3 per period may be achievable if players are patient enough (i.e., δ\deltaδ large).

## Core Mechanic 1: Finitely Repeated Games and Backward Induction

Finitely repeated games: backward induction

In a finitely repeated game with known horizon T, the standard solution concept is subgame-perfect equilibrium (SPE). We obtain SPE by backward induction (a dynamic programming idea): analyze the last period as a one-shot game, then use the resulting equilibrium payoffs as continuation values for the penultimate period, and iterate backward.

If the stage game has a unique Nash equilibrium (NE), that NE is played in every period of any finite repetition by backward induction. Reason: in the last period, players play the stage-game NE. Knowing play in the last period is independent of earlier choices, there is no future to reward or punish, so in the penultimate period players again have no incentives to deviate from the stage NE, and so on.

Concrete numeric example (T=2, Prisoner’s Dilemma)

Stage game PD: payoffs as before (T,R,P,S)=(5,3,1,0)(T,R,P,S)=(5,3,1,0)(T,R,P,S)=(5,3,1,0). The unique stage NE is (D,D) giving payoff P=1P=1P=1 each. Let T=2 (two periods). Backward induction proceeds:

1. 1)Period 2 (last period): play stage NE (D,D). No future punishment exists.
2. 2)Period 1: anticipating (D,D) in period 2, any attempt to cooperate in period 1 cannot be sustained by future punishment (because period 2 is the last). Therefore, in period 1 players again play D.

Thus SPE: (D,D) in both periods. If the stage game had multiple Nash equilibria, more interesting patterns can occur: cooperation may be supported by choosing a Pareto-superior Nash equilibrium in the last period and sustaining it earlier by threats to switch to a worse Nash in case of deviation.

Connection with "Nash Equilibrium" and limitations

In "Nash Equilibrium" we checked unilateral deviations for a single play. Backward induction applies the same logic recursively to every subgame. The limitation: the finiteness removes the effective enforcement by future punishment because the future eventually ends; this is the classic reason why long-term cooperation can fail when the horizon is known.

Finitely repeated games with incomplete information or with an unknown horizon can sustain cooperation. Example: if players do not know the exact final period (e.g., the game ends each period with small probability), the game becomes strategically akin to the infinite horizon case because there is always some chance of future interaction.

Worked mini-derivation (compact)

Let stage-game unique NE give payoff u∗u^\*u∗ to each player. In period T, equilibrium payoff is u∗u^\*u∗. In period T-1, no action can change future beyond what is determined by period T strategies; hence the unique best response in period T-1 equals the stage NE action and the continuation value is u∗u^\*u∗. Inductively, every period uses stage NE actions. This is the dynamic-programming style backward induction argument familiar from "Dynamic Programming".

Numeric check: If you guessed cooperating in period 1 with payoff 3 and feared defection giving one-time Temptation 5 in period 1 but punishment 1 in period 2, you might check whether 5 (gain) plus 1 (period 2 punishment) beats cooperative path 3+3. But because the last period can't be credibly punished (no future), cooperation unravels: you cannot design a credible threat for the second-to-last period because the punishments themselves would rely on future incentives that don't exist in period T.

Practical consequence

For firms or agents facing a known, short horizon, explicit contracts or external enforcement are necessary to sustain cooperation. If horizon is long or uncertain, repeated-game incentives can be powerful.

## Core Mechanic 2: Infinitely Repeated Games, Discounting, and Trigger Strategies

Infinite horizon and discounting

In infinitely repeated games, the present value of a stream of per-period payoffs xxx is ∑t=0∞δtx=x/(1−δ)\sum\_{t=0}^\infty \delta^t x = x/(1-\delta)∑t=0∞​δtx=x/(1−δ) (without the (1−δ)(1-\delta)(1−δ) normalization). With normalization (1−δ)∑δtx=x(1-\delta)\sum \delta^t x = x(1−δ)∑δtx=x, you can think in per-period terms. The key parameter is the discount factor δ\deltaδ (or equivalently the patience of players).

Trigger strategies: idea and types

Trigger strategies condition current play on past histories. Two canonical triggers:

- •Grim trigger: Start by cooperating. If any player ever defects, play the worst Nash-equilibrium action profile (the Nash-punishment) forever thereafter.
- •Finite-length (N-period) trigger: Cooperate until defection; after defection, punish for N periods (playing the punishment profile), then return to cooperation.

Both exploit the threat of future loss to deter one-shot deviations. The one-deviation principle (from "Dynamic Programming") simplifies SPE verification: it suffices to check that no player has a profitable one-shot deviation from the planned strategy at any history.

Derive condition for grim-trigger sustainability in two-player PD

Consider symmetric PD with stage payoffs (T,R,P,S)(T,R,P,S)(T,R,P,S) where T>R>P>ST>R>P>ST>R>P>S. Suppose both players follow grim trigger: cooperate every period unless someone has defected previously; upon any defection switch permanently to (D,D) giving payoff PPP forever. A unilateral defection in a period gives the deviator immediate payoff TTT that period instead of RRR, and then from next period on receives PPP instead of RRR.

Write the present value (no normalization) of cooperating forever as

VC=∑t=0∞δtR=R1−δ.V\_C = \sum\_{t=0}^\infty \delta^t R = \frac{R}{1-\delta}.VC​=t=0∑∞​δtR=1−δR​.

If you deviate in period 0 (one-shot), you get TTT today plus the present value of punishment from period 1 onward:

VD=T+∑t=1∞δtP=T+δP1−δ.V\_D = T + \sum\_{t=1}^\infty \delta^t P = T + \frac{\delta P}{1-\delta}.VD​=T+t=1∑∞​δtP=T+1−δδP​.

No profitable deviation requires VC≥VDV\_C \ge V\_DVC​≥VD​, i.e.

R1−δ≥T+δP1−δ.\frac{R}{1-\delta} \ge T + \frac{\delta P}{1-\delta}.1−δR​≥T+1−δδP​.

Multiply both sides by $1-\delta$ and rearrange:

R≥(1−δ)T+δP⟹R−T≥δ(P−T)R \ge (1-\delta)T + \delta P \quad\Longrightarrow\quad R - T \ge \delta(P-T)R≥(1−δ)T+δP⟹R−T≥δ(P−T)

Equivalently

δ≥T−RT−P.\delta \ge \frac{T-R}{T-P}.δ≥T−PT−R​.

Concrete numeric example: With (T,R,P,S)=(5,3,1,0)(T,R,P,S)=(5,3,1,0)(T,R,P,S)=(5,3,1,0), the threshold is

δ≥5−35−1=24=0.5.\delta \ge \frac{5-3}{5-1} = \frac{2}{4} = 0.5.δ≥5−15−3​=42​=0.5.

Thus if players are sufficiently patient (δ≥0.5\delta\ge0.5δ≥0.5), grim trigger makes mutual cooperation an SPE. If δ<0.5\delta<0.5δ<0.5, a player prefers to defect.

N-period punishment thresholds

If punishment is only N periods long (N-period trigger) the deviation's future loss is limited. Suppose a defector gets TTT in the deviation period, then receives PPP for N periods (periods 1..N) and returns to cooperation thereafter. The incentive inequality becomes

T+δ∑t=1Nδt−1P+δN+1R1−δ≤R1−δ.T + \delta \sum\_{t=1}^N \delta^{t-1} P + \delta^{N+1} \frac{R}{1-\delta} \le \frac{R}{1-\delta}.T+δt=1∑N​δt−1P+δN+11−δR​≤1−δR​.

Simplify the loss from punishment part: the discounted loss relative to cooperation equals

δ1−δN1−δ(R−P).\delta\frac{1-\delta^N}{1-\delta}(R-P).δ1−δ1−δN​(R−P).

So the inequality simplifies to

T−R≤δ1−δN1−δ(R−P).T-R \le \delta\frac{1-\delta^N}{1-\delta}(R-P).T−R≤δ1−δ1−δN​(R−P).

Concrete numeric example: take (T,R,P,S)=(5,3,1,0)(T,R,P,S)=(5,3,1,0)(T,R,P,S)=(5,3,1,0) and N=2. The right-hand side becomes

δ1−δ21−δ(3−1)=2δ(1+δ).\delta\frac{1-\delta^2}{1-\delta}(3-1) = 2\delta(1+\delta).δ1−δ1−δ2​(3−1)=2δ(1+δ).

We require

2≤2δ(1+δ)⟹1≤δ(1+δ)⟹δ2+δ−1≥0.2 \le 2\delta(1+\delta) \Longrightarrow 1 \le \delta(1+\delta) \Longrightarrow \delta^2 + \delta -1 \ge 0.2≤2δ(1+δ)⟹1≤δ(1+δ)⟹δ2+δ−1≥0.

Solving gives δ≥(5−1)/2≈0.618\delta \ge (\sqrt{5}-1)/2 \approx 0.618δ≥(5​−1)/2≈0.618. So a 2-period punishment requires δ≳0.618\delta\gtrsim0.618δ≳0.618 here, which is stricter than the grim-trigger threshold 0.5. This illustrates the power of permanent punishment: longer punishments relax the patience requirement.

Folk Theorem (informal statement)

The Folk Theorem says that for infinitely repeated games, if players are sufficiently patient (δ\deltaδ close to 1), then any feasible and individually rational payoff vector can be sustained as a subgame-perfect equilibrium payoff. "Feasible" means achievable via convex combinations of stage-payoff profiles; "individually rational" means each player's payoff is at least her minmax (security) value.

Sketch of proof idea

Construct strategies that implement a target payoff by cycling through stage-action profiles and use threats to revert to minmax punishments for deviations. Make punishments severe enough (play the minmax strategy) so the future loss outweighs any short-term gain. Use the one-deviation principle and choose δ\deltaδ close enough to 1 so the inequality holds. (This construction is standard and leverages the same discounted-present-value arithmetic as the PD examples.)

Connection to "Dynamic Programming"

Verifying SPE uses continuation values like value functions in dynamic programming: at any history, the continuation payoff must be consistent with incentives, and the one-deviation principle reduces verification to checking one-period deviations against continuation-plan payoffs.

## Applications and Connections: Collusion, Reputation, and Beyond

Economic and practical applications

1) Collusion in oligopoly: Firms can sustain supra-competitive prices by implicitly colluding with trigger strategies that punish price deviations. Example: two firms that would earn monopoly profit by cooperating can sustain that profit flow if they are sufficiently patient; the math parallels the PD analysis where temptation is the one-shot gain from undercutting.

Numeric illustration: two symmetric firms that get monopoly profit πC=100\pi\_C=100πC​=100 when both keep prices high, and competitive profit πN=30\pi\_N=30πN​=30 if both price low; a deviator gets πT=140\pi\_T=140πT​=140 that period if she undercuts. Grim-trigger sustainability requires

δ≥πT−πCπT−πN=140−100140−30=40110≈0.364.\delta \ge \frac{\pi\_T - \pi\_C}{\pi\_T - \pi\_N} = \frac{140-100}{140-30} = \frac{40}{110} \approx 0.364.δ≥πT​−πN​πT​−πC​​=140−30140−100​=11040​≈0.364.

So moderate patience suffices.

2) Reputation and online markets: Sellers with repeated transactions use reputation as a trigger: a bad review triggers fewer future sales (an endogenous punishment). The repeated-game framework and Folk Theorem explain how even anonymous markets can sustain cooperation when matching is long-lived or search friction gives weight to future trade.

3) Enforcement without a central authority: Smart contracts or decentralized systems use repeated-interaction logic to enforce behavior: validators who misbehave can be blacklisted (permanent punishment) which discourages deviation if future payoffs are valuable.

Connections to more advanced theory (what this enables)

- •Mechanism Design & Dynamic Mechanism Design: Repeated-game incentives underlie many dynamic mechanism-design problems where agents' private information and future incentives matter.
- •Stochastic Games: When the stage game payoffs depend on a state evolving with actions, repeated-game ideas extend to stochastic games; Folk-like theorems exist with state dependence.
- •Evolutionary Game Theory: Long-run dynamics and stable cooperation are often interpreted through repeated-interaction payoffs.

Downstream technical prerequisites that require repeated games

- •Repeated-game Folk Theorem is used in dynamic contract theory and in proving existence of long-run collusion equilibria in industrial organization.
- •Techniques such as automaton strategies and self-generating sets (Abreu, Pearce, Stacchetti) build on repeated-game foundations; understanding these is necessary for advanced analysis of dynamic oligopoly and bargaining problems.

Limitations and refinements

- •The Folk Theorem is existential: it shows many payoffs can be supported, but it does not select among them. Refinements (e.g., renegotiation-proofness, bounded complexity of strategies, or computational cost) are used to pick more plausible equilibria.
- •In finitely repeated games or when discounting is severe (small δ\deltaδ), repeated-game enforcement may fail, requiring external institutions.

Summary

Repeated games show how the shadow of the future reshapes incentives. The key mechanics are discounting, continuation values, and credible punishments encoded in trigger strategies. The Folk Theorem demonstrates the theoretical richness of feasible equilibria when players are patient, and the explicit threshold calculations (as in the PD) reveal when cooperation is feasible in concrete settings.

## Worked Examples (3)

### Grim-trigger threshold in PD (basic)

Stage payoffs (T,R,P,S) = (5,3,1,0). Determine the minimal discount factor delta so that grim-trigger sustains mutual cooperation.

1. Write cooperating forever value: V\_C = R/(1-δ) = 3/(1-δ).
2. Write value after deviating once: V\_D = T + δP/(1-δ) = 5 + δ\*1/(1-δ).
3. Set incentive constraint V\_C ≥ V\_D: 3/(1-δ) ≥ 5 + δ/(1-δ).
4. Multiply both sides by (1-δ): 3 ≥ 5(1-δ) + δ → 3 ≥ 5 -5δ + δ → 3 ≥ 5 -4δ.
5. Rearrange: 4δ ≥ 2 → δ ≥ 0.5.
6. Conclude: δ must be at least 0.5 to sustain cooperation with grim trigger.

**Insight:** This example shows how a single inequality compares the immediate temptation to defect with the present value of future cooperative rents; numbers give intuition about how patient players must be.

### Backward induction in finitely repeated PD (T=3)

Stage PD as before (T=5,R=3,P=1,S=0). Repeated for T=3 periods. Find the unique SPE.

1. Period 3 (last): players play stage-game NE which is (D,D) giving payoff 1 each.
2. Period 2: Knowing period 3 will be (D,D), there is no future punishment to enforce cooperation after period 2. Thus period 2 is equivalent to a one-shot PD and players play (D,D) in period 2.
3. Period 1: Anticipating that periods 2 and 3 will be (D,D), there is no way to credibly threaten punishment that affects period 2 and 3 in a way that deters deviation in period 1. Hence period 1 also uses (D,D).
4. Thus the unique SPE is (D,D) in each of the three periods.
5. Check: Any unilateral deviation in any period gives a higher immediate payoff (e.g., defecting against cooperator), but future cannot be credibly changed to make deviation unprofitable because the final period forces (D,D).

**Insight:** Finite horizon leads to unraveling of cooperation via backward induction. This highlights the difference between finite and infinite horizons.

### Choosing N for minimal patience (N-period punishment)

PD with (T,R,P,S)=(5,3,1,0). You can design an N-period punishment (finite punishment then resume cooperation). For a given δ, find the smallest N that deters deviation, or conversely, for a given N find minimal δ.

1. Incentive inequality: T-R ≤ δ  *(1-δ^N)/(1-δ)*  (R-P). Substitute numbers: 5-3 ≤ δ  *(1-δ^N)/(1-δ)*  (3-1) → 2 ≤ 2δ \* (1-δ^N)/(1-δ).
2. Simplify: 1 ≤ δ \* (1-δ^N)/(1-δ). Note identity (1-δ^N)/(1-δ) = 1+δ+...+δ^{N-1}. So require 1 ≤ δ(1+δ+...+δ^{N-1}).
3. For fixed δ, evaluate the right-hand side for increasing N until inequality holds. For example, let δ=0.6: compute δ(1+δ+...+δ^{N-1}). For N=1: 0.6. N=2: 0.6(1+0.6)=0.96. N=3: 0.6(1+0.6+0.36)=0.6\*1.96=1.176 ≥1. So N=3 suffices at δ=0.6.
4. Alternatively, for fixed N=2, solve 1 ≤ δ(1+δ) → δ^2 + δ -1 ≥ 0 → δ ≥ (\sqrt{5}-1)/2 ≈ 0.618 (as earlier).
5. Conclusion: finite-length punishments can be tuned; longer punishments reduce required patiently δ.

**Insight:** This example shows the trade-off between punishment length and players' patience: if players are less patient (smaller δ), you need longer (or harsher) punishments to deter deviation.

## Key Takeaways

- ✓

  A finitely repeated game with a unique stage-game Nash equilibrium unravels: backward induction yields the stage NE every period.
- ✓

  In infinitely repeated games, future payoffs (discounted by δ) can deter one-shot deviations; the key inequality compares immediate temptation to the discounted value of future punishment.
- ✓

  Grim trigger gives the simplest permanent punishment: cooperation is sustainable if δ≥(T−R)/(T−P)\delta \ge (T-R)/(T-P)δ≥(T−R)/(T−P) in a symmetric PD with payoffs (T,R,P,S). For (5,3,1,0) this threshold is 0.5.
- ✓

  Finite-length punishments produce weaker deterrence; the incentive condition becomes T−R≤δ1−δN1−δ(R−P)T-R \le \delta\frac{1-\delta^N}{1-\delta}(R-P)T−R≤δ1−δ1−δN​(R−P) and yields a trade-off between punishment duration N and patience δ.
- ✓

  The Folk Theorem: for δ near 1, any feasible and individually rational payoff can be supported as an SPE; constructions use threats to minmax and rely on continuation-value arithmetic.
- ✓

  Verification of SPE uses the one-deviation principle and continuation values — techniques tied to Dynamic Programming and Nash Equilibrium analysis.
- ✓

  Practical implications include collusion in oligopoly, reputation mechanisms, decentralized enforcement, and design of long-term contracts.

## Common Mistakes

- ✗

  Confusing finite and infinite horizon results: believing cooperation is sustained in a known finite horizon when the stage game has a unique NE. Why wrong: backward induction removes credible future punishments.
- ✗

  Forgetting to compare present values: checking only per-period payoffs (e.g., R vs T) without discounting ignores the aggregation of future losses from punishment; the correct check uses discounted sums.
- ✗

  Using an overly harsh or impossible punishment: assuming players can be forced below their minmax payoff. Why wrong: punishments must be credible — subgame-perfect punishments can only achieve at least the minmax payoff.
- ✗

  Applying the Folk Theorem without checking individual rationality: the Folk Theorem requires target payoffs exceed each player's minmax value; otherwise they cannot be enforced.

## Practice

easy

Easy: For a PD with (T,R,P,S)=(6,4,2,0), compute the minimal δ so that grim-trigger sustains mutual cooperation.

**Hint:** Use inequality δ ≥ (T-R)/(T-P).

Show solution

Compute (T-R)/(T-P) = (6-4)/(6-2) = 2/4 = 0.5. So δ ≥ 0.5.

medium

Medium: Consider a two-player stage game with two pure Nash equilibria: A (payoffs 4 each) and B (payoffs 1 each). If the stage game is repeated T=3 times, can players sustain action A in an SPE throughout? Explain and construct strategies if possible.

**Hint:** Use backward induction: check last period (period 3) equilibrium multiplicity and how threat to switch to B can serve as punishment.

Show solution

In period 3 (last), players can choose either Nash equilibrium A (4,4) or B (1,1); since A is a NE, cooperation in last period is credible. Knowing that, in period 2 players can threaten to play B in period 3 if someone deviates in period 2; because period 3 has the NE A available, players will follow the threat if the threatened payoff (1) versus staying at A (4) provides the right incentives. Specifically, if a unilateral deviation in period 2 yields immediate gain > cost of being punished (losing 3 in period 3), then the threat may not suffice. But here shifting from A to B in period 3 reduces payoff by 3, so this finite punishment (1 period) might deter deviations in period 2. For period 1, threats to play B in period 2 and 3 (two periods) can deter deviations provided gains are smaller than discounted loss. Therefore, with multiple NE and suitable history-dependent strategies (play A unless deviation, then play B for remaining periods), A can be sustained for T=3 as an SPE. This contrasts with unique-stage-NE settings where unraveling forces the stage NE each period.

hard

Hard: In the PD (5,3,1,0), suppose you are allowed to design a mixed-strategy punishment that reduces the deviator's continuation payoff to the minmax value m. If minmax value for the deviator is m=0.5, what discount factor δ is needed to sustain cooperation under grim-trigger to the minmax punishment (instead of P=1)?

**Hint:** Replace P in the grim-trigger inequality with m and solve δ ≥ (T-R)/(T-m).

Show solution

Use δ ≥ (T-R)/(T-m) = (5-3)/(5-0.5) = 2/4.5 = 0.444... ≈ 0.444. So if you can enforce a harsher minmax punishment m=0.5, cooperation requires only δ ≥ 0.444.

## Connections

Looking back, the repeated-games toolkit directly uses insights from "Nash Equilibrium" (checking unilateral deviations in every subgame) and from "Dynamic Programming" (continuation values, one-deviation principle, and backward induction). The one-deviation principle is a dynamic-programming-flavored result that reduces the verification of subgame-perfection to local checks. Looking forward, mastering repeated games enables work in dynamic mechanism design, stochastic games, reputation models, collusion analysis in industrial organization, and enforcement in decentralized systems. In particular, the Folk Theorem is a building block for dynamic contract theory and for results that characterize equilibrium payoff sets in stochastic games; techniques like automaton constructions and self-generating sets (Abreu-Pearce-Stacchetti) rely on repeated-game foundations.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
