---
title: Bayesian Games
description: Games of incomplete information. Type spaces, beliefs, Bayesian Nash equilibrium. Harsanyi transformation from incomplete to imperfect information.
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
inspiration_url: https://templeton.host/tech-tree/bayesian-games/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/bayesian-games/](https://templeton.host/tech-tree/bayesian-games/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Bayesian Games

Game TheoryDifficulty: ★★★★☆Depth: 8Unlocks: 3

Games of incomplete information. Type spaces, beliefs, Bayesian Nash equilibrium. Harsanyi transformation from incomplete to imperfect information.

## Prerequisites (2)

[Nash Equilibrium5 atoms](/tech-tree/nash-equilibrium/)[Bayesian Inference5 atoms](/tech-tree/bayesian-inference/)

## Unlocks (3)

[Dynamic Gameslvl 5](/tech-tree/dynamic-games/)[Signaling Gameslvl 5](/tech-tree/signaling-games/)[Competitive Pricinglvl 5](/tech-tree/competitive-pricing/)

## Referenced by (6)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (6)

[ValuationBusiness

Valuations are literally the 'types' in the Harsanyi formulation of Bayesian games. The common prior over valuations IS the common prior over types, and independent draws across bidders defines the type space structure that Bayesian Nash equilibrium operates over.](/business/valuation/)[auctionBusiness

Auctions with private valuations are the textbook Bayesian game: each bidder's 'type' is their valuation, beliefs are drawn from a common prior, and equilibrium bidding strategies are Bayesian Nash equilibria - this is the model underlying spectrum and ad auction analysis](/business/auction/)[auction theoryBusiness

Auctions are the canonical Bayesian game: bidders hold private information (valuations), form beliefs about opponents' types, and Bayesian Nash equilibrium is the standard solution concept for analyzing bidding strategies](/business/auction-theory/)[Bid ShadingBusiness

Bid shading is the canonical example of Bayesian Nash equilibrium - bidders choose shade amount based on beliefs about opponents' private valuations (types), and the equilibrium bid function solves for the strategy where no bidder benefits from deviating given their type distribution](/business/bid-shading/)[Vendor NegotiationsBusiness

Vendor's true cost structure and reservation price are private information. Bayesian Nash equilibrium formalizes how you negotiate optimally under this incomplete information, updating beliefs from each round's signals.](/business/vendor-negotiations/)[winner's curseBusiness

Winner's curse is analyzed as a Bayesian game: bidders hold private signals (types) about an unknown common value, and Bayesian Nash equilibrium yields the bid-shading strategies that account for the informational content of winning](/business/winner-s-curse/)

Advanced Learning Details

### Graph Position

128

Depth Cost

3

Fan-Out (ROI)

3

Bottleneck Score

8

Chain Length

Many strategic interactions in economics, politics and engineering occur under uncertainty about others — Bayesian games give you the right language to reason optimally when players have private information.

TL;DR:

A Bayesian game models strategic interaction with incomplete information by assigning player types and beliefs; its solution concept, the Bayesian Nash equilibrium, generalizes Nash equilibrium using expected payoffs given beliefs and can be represented as an extensive-form game via the Harsanyi transformation.

## What Is a Bayesian Game?

Definition and basic components

A Bayesian game (a game of incomplete information) extends the normal-form game by allowing players to hold private information about their own characteristics, preferences, or available actions. Formally, a Bayesian game consists of:

- •A finite set of players I={1,…,n}I=\{1,\dots,n\}I={1,…,n}.
- •For each player iii, a finite set of actions AiA\_iAi​ (pure strategies). Example: A1={C,D}A\_1=\{C,D\}A1​={C,D} where CCC stands for "Cooperate" and DDD for "Defect".
- •For each player iii, a finite set of types TiT\_iTi​ representing private information. Example: T1={H,L}T\_1=\{H,L\}T1​={H,L} meaning high or low valuation.
- •A common prior p(t1,…,tn)p(t\_1,\dots,t\_n)p(t1​,…,tn​) over type profiles in T≡∏iTiT\equiv\prod\_i T\_iT≡∏i​Ti​. This captures ex ante beliefs before types are realized. Example: for two players each with types {H,L}\{H,L\}{H,L}, one might have p(H,H)=0.25,p(H,L)=0.25,p(L,H)=0.25,p(L,L)=0.25p(H,H)=0.25,p(H,L)=0.25,p(L,H)=0.25,p(L,L)=0.25p(H,H)=0.25,p(H,L)=0.25,p(L,H)=0.25,p(L,L)=0.25 (uniform).
- •For each player iii, a payoff function ui(a1,…,an,ti)u\_i(a\_1,\dots,a\_n,t\_i)ui​(a1​,…,an​,ti​) which may depend on the action profile and player iii's own type; sometimes the payoff depends on the entire type profile, ui(a,t)u\_i(a,t)ui​(a,t).

The crucial element is that players know the structure above (including the prior), know their own type ti∈Tit\_i\in T\_iti​∈Ti​, but do not observe other players' types. They form beliefs about others' types via conditional probabilities derived from the common prior using Bayes' rule when possible.

Why this matters: In many economic settings (auctions, contracting, signaling) players have private information that materially affects optimal actions. If you learned Nash equilibrium in "Nash Equilibrium" (a prerequisite), you know how to analyze strategic stability when payoffs are common knowledge. Bayesian games let you extend that analysis to private information by replacing actual payoffs with expected payoffs given beliefs.

Intuition: Replace each player by a collection of type-specific decision-makers. Each type chooses an action possibly contingent on the type. Players choose strategy functions si:Ti→Δ(Ai)s\_i:T\_i\to\Delta(A\_i)si​:Ti​→Δ(Ai​) (possibly mixed) mapping types to distributions over actions. A strategy profile s=(s1,…,sn)s=(s\_1,\dots,s\_n)s=(s1​,…,sn​) is a Bayesian Nash equilibrium if for every player iii and every type tit\_iti​, si(ti)s\_i(t\_i)si​(ti​) maximizes expected payoff conditional on tit\_iti​ given other players' strategies and the prior.

Mathematical expression: Given strategies sss the expected payoff to player iii with type tit\_iti​ when she plays an action aia\_iai​ and others follow s−is\_{-i}s−i​ is

Ui(ai,s−i∣ti)=∑t−ip(t−i∣ti)∑a−i[∏j≠isj(aj∣tj)]ui(ai,a−i,ti,t−i).U\_i(a\_i,s\_{-i}|t\_i)=\sum\_{t\_{-i}} p(t\_{-i}|t\_i)\sum\_{a\_{-i}}\left[\prod\_{j\neq i} s\_j(a\_j|t\_j)\right] u\_i(a\_i,a\_{-i},t\_i,t\_{-i}).Ui​(ai​,s−i​∣ti​)=t−i​∑​p(t−i​∣ti​)a−i​∑​​j=i∏​sj​(aj​∣tj​)​ui​(ai​,a−i​,ti​,t−i​).

Concrete numeric example: Two players 1 and 2; T1={H,L}T\_1=\{H,L\}T1​={H,L}, T2={0}T\_2=\{0\}T2​={0} (player 2 has no private info). Actions: Ai={0,1}A\_i=\{0,1\}Ai​={0,1}. Prior: p(T1=H)=0.6,p(T1=L)=0.4p(T\_1=H)=0.6, p(T\_1=L)=0.4p(T1​=H)=0.6,p(T1​=L)=0.4. Suppose u1(a1,a2,t1)={2if a1=1,a2=1,t1=H0otherwiseu\_1(a\_1,a\_2,t\_1)=\begin{cases}2 &\text{if }a\_1=1,a\_2=1,t\_1=H\\0 &\text{otherwise}\end{cases}u1​(a1​,a2​,t1​)={20​if a1​=1,a2​=1,t1​=Hotherwise​ and u2u\_2u2​ irrelevant. If player 1 of type HHH contemplates a1=1a\_1=1a1​=1 while believing s2(1)=0.5s\_2(1)=0.5s2​(1)=0.5, then

U1(1,s2∣H)=∑t2p(t2∣H)∑a2s2(a2∣t2)u1(1,a2,H)=s2(1)⋅2=0.5⋅2=1.U\_1(1,s\_2|H)=\sum\_{t\_2} p(t\_2|H)\sum\_{a\_2} s\_2(a\_2|t\_2) u\_1(1,a\_2,H)=s\_2(1)\cdot 2=0.5\cdot2=1.U1​(1,s2​∣H)=t2​∑​p(t2​∣H)a2​∑​s2​(a2​∣t2​)u1​(1,a2​,H)=s2​(1)⋅2=0.5⋅2=1.

This shows how conditional beliefs and strategy mappings determine expected payoff.

Relation to incomplete vs imperfect information

A Bayesian game models incomplete information (players have private types). Using the Harsanyi transformation (covered later), one can represent an incomplete-information game as an extensive-form game with imperfect information. This is central: "incomplete information" refers to missing payoff-relevant facts; "imperfect information" refers to players not observing previous moves. Harsanyi’s trick converts uncertainty about types into moves by Nature at the game’s start, turning incomplete into imperfect information while preserving solution concepts.

Comparison to prerequisites

- •In "Nash Equilibrium" we learned that equilibrium requires no profitable unilateral deviation given exact payoffs. In Bayesian games, exact payoffs aren't known to all players; we replace the payoff by the expectation conditional on each type and require no profitable deviation for each type separately.
- •In "Bayesian Inference" we learned to update priors into posteriors using Bayes’ rule. In Bayesian games, conditional beliefs p(t−i∣ti)p(t\_{-i}|t\_i)p(t−i​∣ti​) are computed via Bayes’ rule from the common prior when types are independent or correlated; strategic behavior may cause off-path beliefs that require explicit specification in dynamic/ signaling contexts.

Summary: A Bayesian game formalizes strategic interaction under private information by turning each player's private information into "types" and requiring strategy functions that are best responses in expectation given beliefs derived from a common prior.

## Core Mechanic 1: Bayesian Nash Equilibrium (BNE)

Definition and derivation

A Bayesian Nash equilibrium is the central solution concept for static Bayesian games. It is a profile of type-contingent strategies si∗:Ti→Δ(Ai)s^\*\_i: T\_i\to\Delta(A\_i)si∗​:Ti​→Δ(Ai​) such that for every player iii and every type ti∈Tit\_i\in T\_iti​∈Ti​, si∗(ti)s^\*\_i(t\_i)si∗​(ti​) maximizes expected payoff given other players’ strategies and the conditional distribution over other types:

si∗(ti)∈arg max⁡σi∈Δ(Ai)  Ui(σi,s−i∗∣ti),s^\*\_i(t\_i)\in\operatorname{arg\,max}\_{\sigma\_i\in\Delta(A\_i)} \; U\_i(\sigma\_i,s^\*\_{-i}|t\_i),si∗​(ti​)∈argmaxσi​∈Δ(Ai​)​Ui​(σi​,s−i∗​∣ti​),

where

Ui(σi,s−i∗∣ti)=∑t−ip(t−i∣ti)∑a∈Aσi(ai)∏j≠isj∗(aj∣tj) ui(a,ti,t−i).U\_i(\sigma\_i,s^\*\_{-i}|t\_i)=\sum\_{t\_{-i}}p(t\_{-i}|t\_i)\sum\_{a\in A} \sigma\_i(a\_i)\prod\_{j\neq i}s^\*\_j(a\_j|t\_j)\,u\_i(a,t\_i,t\_{-i}).Ui​(σi​,s−i∗​∣ti​)=t−i​∑​p(t−i​∣ti​)a∈A∑​σi​(ai​)j=i∏​sj∗​(aj​∣tj​)ui​(a,ti​,t−i​).

Concretely, if strategies are pure deterministic, si(ti)∈Ais\_i(t\_i)\in A\_isi​(ti​)∈Ai​, the condition reduces to: for all ai′∈Aia'\_i\in A\_iai′​∈Ai​,

∑t−ip(t−i∣ti) ui(si(ti),s−i(t−i),ti,t−i)≥∑t−ip(t−i∣ti) ui(ai′,s−i(t−i),ti,t−i).\sum\_{t\_{-i}} p(t\_{-i}|t\_i)\,u\_i(s\_i(t\_i),s\_{-i}(t\_{-i}),t\_i,t\_{-i}) \ge \sum\_{t\_{-i}} p(t\_{-i}|t\_i)\,u\_i(a'\_i,s\_{-i}(t\_{-i}),t\_i,t\_{-i}).t−i​∑​p(t−i​∣ti​)ui​(si​(ti​),s−i​(t−i​),ti​,t−i​)≥t−i​∑​p(t−i​∣ti​)ui​(ai′​,s−i​(t−i​),ti​,t−i​).

Numerical toy calculation

Take two players, each with types {H,L}\{H,L\}{H,L}. Actions Ai={0,1}A\_i=\{0,1\}Ai​={0,1}. Prior independent: p1(H)=0.6,p2(H)=0.7p\_1(H)=0.6,p\_2(H)=0.7p1​(H)=0.6,p2​(H)=0.7. Payoffs for player 1 depend on his type only: if type HHH then u1(a1,a2,H)=3u\_1(a\_1,a\_2,H)=3u1​(a1​,a2​,H)=3 if a1=a2=1a\_1=a\_2=1a1​=a2​=1 else $0;iftype; if type ;iftypeLthen then thenu\_1(a\_1,a\_2,L)=1if if ifa\_1=1$ else $0.Supposeplayer2alwaysplays. Suppose player 2 always plays .Supposeplayer2alwaysplaysa\_2=1.Evaluatewhetherplayer1oftype. Evaluate whether player 1 of type .Evaluatewhetherplayer1oftypeHshouldplay should play shouldplaya\_1=1$:

Conditional distribution p(t2∣t1)p(t\_2|t\_1)p(t2​∣t1​) equals p2p\_2p2​ marginal since independence, so p(t2=H∣t1)=0.7p(t\_2=H|t\_1)=0.7p(t2​=H∣t1​)=0.7. The expected payoff from a1=1a\_1=1a1​=1 for type HHH is

U1(1∣H)=∑t2p(t2)⋅u1(1,1,H)=p2(H)⋅3+p2(L)⋅0=0.7⋅3=2.1.U\_1(1|H)=\sum\_{t\_2} p(t\_2) \cdot u\_1(1,1,H)=p\_2(H)\cdot 3 + p\_2(L)\cdot 0 =0.7\cdot3=2.1.U1​(1∣H)=t2​∑​p(t2​)⋅u1​(1,1,H)=p2​(H)⋅3+p2​(L)⋅0=0.7⋅3=2.1.

If instead a1=0a\_1=0a1​=0, payoff is $0$. So playing $1isoptimal.Numericcheck:if is optimal. Numeric check: if isoptimal.Numericcheck:ifp\_2(H)$ were $0.2,then, then ,thenU\_1(1|H)=0.2\cdot3=0.6<0$, so $1$ would not be optimal.

Existence, independence, and correlated types

If types are independent and action spaces are finite, a BNE in mixed strategies always exists by a fixed-point argument similar to Nash existence (Glicksberg). If types are correlated, the same existence results hold for finite games under standard mixed-strategy compactness and continuity conditions.

Derivation for two-player case

Consider two players 1 and 2 with finite type spaces T1,T2T\_1,T\_2T1​,T2​ and actions A1,A2A\_1,A\_2A1​,A2​. A strategy profile s=(s1,s2)s=(s\_1,s\_2)s=(s1​,s2​) is a BNE if for all t1∈T1t\_1\in T\_1t1​∈T1​,

s1(t1)∈arg max⁡σ1∑t2p(t2∣t1)∑a1,a2σ1(a1)s2(a2∣t2)u1(a1,a2,t1,t2).s\_1(t\_1)\in\operatorname{arg\,max}\_{\sigma\_1} \sum\_{t\_2} p(t\_2|t\_1)\sum\_{a\_1,a\_2} \sigma\_1(a\_1)s\_2(a\_2|t\_2) u\_1(a\_1,a\_2,t\_1,t\_2).s1​(t1​)∈argmaxσ1​​t2​∑​p(t2​∣t1​)a1​,a2​∑​σ1​(a1​)s2​(a2​∣t2​)u1​(a1​,a2​,t1​,t2​).

For finite supports, we can compute expected payoff vectors for each type and use linear programming to find best responses. Example: With two actions per player and two types per player, each strategy is a vector of four probabilities. Solve the best response equations using expected payoff formulas. A numeric illustration helps:

Example numeric derivation: Let T1=T2={H,L}T\_1=T\_2=\{H,L\}T1​=T2​={H,L} with p(H,H)=0.3,p(H,L)=0.3,p(L,H)=0.2,p(L,L)=0.2p(H,H)=0.3,p(H,L)=0.3,p(L,H)=0.2,p(L,L)=0.2p(H,H)=0.3,p(H,L)=0.3,p(L,H)=0.2,p(L,L)=0.2. Suppose Ai={0,1}A\_i=\{0,1\}Ai​={0,1}. Let payoffs for player 1 be u1(a1,a2,t)=a1(2a2+1t=H)u\_1(a\_1,a\_2,t)=a\_1(2a\_2+\mathbf{1}\_{t=H})u1​(a1​,a2​,t)=a1​(2a2​+1t=H​) (i.e. payoff increases with matching and with being high type). If player 2 uses pure strategy s2(H)=1,s2(L)=0s\_2(H)=1,s\_2(L)=0s2​(H)=1,s2​(L)=0 (play 1 when H, 0 when L), then for player 1 of type HHH the conditional probability of t2=Ht\_2=Ht2​=H is

p(t2=H∣t1=H)=p(H,H)p1(H)=0.30.6=0.5.p(t\_2=H|t\_1=H)=\frac{p(H,H)}{p\_1(H)}=\frac{0.3}{0.6}=0.5.p(t2​=H∣t1​=H)=p1​(H)p(H,H)​=0.60.3​=0.5.

Expected payoff from a1=1a\_1=1a1​=1 is

U1(1∣H)=0.5⋅(2⋅1+1)+0.5⋅(2⋅0+1)=0.5⋅3+0.5⋅1=2.U\_1(1|H)=0.5\cdot(2\cdot1+1)+0.5\cdot(2\cdot0+1)=0.5\cdot3+0.5\cdot1=2.U1​(1∣H)=0.5⋅(2⋅1+1)+0.5⋅(2⋅0+1)=0.5⋅3+0.5⋅1=2.

From a1=0a\_1=0a1​=0 payoff is $0,so, so ,soa\_1=1isoptimalfortype is optimal for type isoptimalfortypeH$.

Interpretation: BNE demands this optimality for every type simultaneously. In mixed strategies, solving requires equalizing expected payoffs across pure actions used with positive probability. The computations are conceptually identical to those in "Nash Equilibrium" but carried out conditionally for each type.

Belief updating and off-equilibrium path issues

In static Bayesian games with exogenous types and full-support priors, conditional probabilities p(t−i∣ti)p(t\_{-i}|t\_i)p(t−i​∣ti​) are well-defined. In dynamic or signaling games (next section), Bayes' rule is applied to observed actions to update beliefs; if an observed action has zero probability under equilibrium, Bayes' rule does not pin down beliefs and one must specify a solution refinement (e.g., Perfect Bayesian Equilibrium).

## Core Mechanic 2: Harsanyi Transformation and Signaling

Harsanyi transformation: converting incomplete into imperfect information

Harsanyi’s insight (1967–68) is that a game of incomplete information can be modeled as an extensive-form game where Nature moves first and selects a type profile according to the common prior. Each player observes her own type and then plays the rest of the game. Information sets capture that players do not observe others' types. This transformation is mechanical and preserves BNE as the counterpart of Nash equilibrium in the resulting imperfect-information extensive form.

Formal construction

Start with a Bayesian game (I, A\_i, T\_i, p, u\_i). Create an extensive form:

1. 1)Nature (chance node) selects t=(t1,…,tn)t=(t\_1,\dots,t\_n)t=(t1​,…,tn​) with probability p(t)p(t)p(t). Example: for two players, Nature picks (H,L)(H,L)(H,L) with probability 0.25.
2. 2)Player iii is informed of her own type tit\_iti​ but not others. So for each tit\_iti​ there is a decision node for player iii; nodes for different tit\_iti​ are in different information sets (player distinguishes them), but for a fixed tit\_iti​, nodes corresponding to different t−it\_{-i}t−i​ are in the same information set (player cannot distinguish other players' types).
3. 3)Players choose actions and payoffs are ui(a,t)u\_i(a,t)ui​(a,t).

The extensive-form game's Nash equilibria correspond to BNEs of the Bayesian game when strategies are type-contingent actions. Thus, solving BNE reduces to finding Nash equilibria in an imperfect-information extensive form where Nature's move implements the prior.

Concrete numeric Harsanyi example

Two players, T1={H,L}T\_1=\{H,L\}T1​={H,L}, T2={α,β}T\_2=\{\alpha,\beta\}T2​={α,β}, prior: p(H,α)=0.2,p(H,β)=0.3,p(L,α)=0.1,p(L,β)=0.4p(H,\alpha)=0.2, p(H,\beta)=0.3, p(L,\alpha)=0.1, p(L,\beta)=0.4p(H,α)=0.2,p(H,β)=0.3,p(L,α)=0.1,p(L,β)=0.4. Nature draws a profile accordingly. Player 1 observes HHH vs LLL; player 2 observes α\alphaα vs β\betaβ. If player 1 faces HHH, she has decision nodes for (H,α)(H,\alpha)(H,α) and (H,β)(H,\beta)(H,β) but these are in the same information set for her since she doesn't see player 2’s type. The expected payoff calculations in the extensive-form game for a strategy mapping si:Ti→Ais\_i:T\_i\to A\_isi​:Ti​→Ai​ are identical to the BNE formulas earlier.

Signaling games: an important class

A signaling game is a two-stage Harsanyi-style extensive-form game where one informed player (the Sender) moves after Nature selects her type and then an uninformed player (the Receiver) observes Sender's action but not her type, updates beliefs via Bayes' rule, and chooses a response. This models persuasion, job-market signaling, and cheap-talk.

Simple signaling numeric example (job market):

Types: Worker can be High (HHH) or Low (LLL) ability with prior p(H)=0.4,p(L)=0.6p(H)=0.4,p(L)=0.6p(H)=0.4,p(L)=0.6. Sender (worker) chooses education level e∈{0,1}e\in\{0,1\}e∈{0,1}. Education is costless to HHH (cost 0) and costly to LLL (cost 1). Employer observes eee, then sets wage w∈{0,2}w\in\{0,2\}w∈{0,2} equal to expected productivity. The worker's payoff is w−cost(e,t)w-\text{cost}(e,t)w−cost(e,t). If employer uses Bayesian updating and sets w=2w=2w=2 if posterior P(H∣e)≥0.5P(H|e)\ge 0.5P(H∣e)≥0.5 and w=0w=0w=0 otherwise, then calculate whether pooling or separating equilibria exist.

Compute posterior if both types choose e=1e=1e=1 (pooling):

P(H∣e=1)=p(H)⋅P(e=1∣H)p(H)P(e=1∣H)+p(L)P(e=1∣L)=0.4⋅10.4⋅1+0.6⋅1=0.4.P(H|e=1)=\frac{p(H)\cdot P(e=1|H)}{p(H)P(e=1|H)+p(L)P(e=1|L)}=\frac{0.4\cdot1}{0.4\cdot1+0.6\cdot1}=0.4.P(H∣e=1)=p(H)P(e=1∣H)+p(L)P(e=1∣L)p(H)⋅P(e=1∣H)​=0.4⋅1+0.6⋅10.4⋅1​=0.4.

Employer sets w=0w=0w=0, so high type gets $0-0=0$, low type gets $0-1=-1.Butifhighdeviatesto. But if high deviates to .Butifhighdeviatestoe=0,employerstillpays0,sonoprofitabledeviation.Ifhightakes, employer still pays 0, so no profitable deviation. If high takes ,employerstillpays0,sonoprofitabledeviation.Ifhightakese=1$ while employer pays nothing, maybe high can't gain.

Separating candidate: let HHH choose e=1e=1e=1, LLL choose e=0e=0e=0. Then after e=1e=1e=1, posterior P(H∣e=1)=1P(H|e=1)=1P(H∣e=1)=1 so w=2w=2w=2, and after e=0e=0e=0, P(H∣e=0)=0P(H|e=0)=0P(H∣e=0)=0 so w=0w=0w=0. Worker payoffs: HHH gets $2-0=2$, $L$ gets $0-0=0.Lowwon′tmimicbecauseif. Low won't mimic because if .Lowwon′tmimicbecauseifLdeviatesto deviates to deviatestoe=1$, her payoff would be $2-1=1<0$? Wait numeric check: $0$ is better than $1$? Actually $1>0,solowwouldwanttomimic.Sonoseparatingequilibrium.Butifcostfor, so low would want to mimic. So no separating equilibrium. But if cost for ,solowwouldwanttomimic.Sonoseparatingequilibrium.ButifcostforLwere were werec=2$, then deviating yields $2-2=0$ which equals staying; further refinements needed. This numeric manipulation shows how costs and priors determine signals' credibility.

Off-equilibrium beliefs and refinement

Harsanyi transformation makes explicit when Bayes’ rule applies: only on-path signals have beliefs pinned down. In signaling games one often needs refinements (e.g., Perfect Bayesian Equilibrium, Sequential Equilibrium, or the Intuitive Criterion) to rule out equilibria supported by unreasonable beliefs about off-path actions.

Proof sketch that BNE corresponds to Nash equilibrium in Harsanyi game

Given a Bayesian game, take a strategy profile sss mapping TiT\_iTi​ to mixed actions. Treat sss as a strategy in the Harsanyi extensive form where each type's node prescribes the corresponding action distribution. Because Nature’s probabilities are the prior, each type-maximization condition in BNE is exactly the best-response condition in the extensive form given the same beliefs. Hence existence and characterization properties carry over.

## Applications and Connections

Why Bayesian games matter: fields and canonical problems

Bayesian games are foundational in auction theory, mechanism design, contract theory, signaling in labor markets, political economy (e.g., elections with private valuations), cybersecurity (hidden types or states), and negotiation under asymmetric information. Key canonical models built on Bayesian games include:

- •Private-value auctions (first-price, second-price): bidders know their valuations (types) drawn from a common prior; BNE yields bidding functions. Example numeric: valuations iid Uniform[0,1]; in a second-price sealed-bid auction, truthful bidding is a dominant strategy; in a first-price auction the symmetric BNE bidding function is b(v)=n−1nvb(v)=\frac{n-1}{n}vb(v)=nn−1​v. For n=3n=3n=3 and v=0.9v=0.9v=0.9 we have b(0.9)=23⋅0.9=0.6b(0.9)=\frac{2}{3}\cdot0.9=0.6b(0.9)=32​⋅0.9=0.6.

- •Adverse selection: sellers and buyers have private information (e.g., used car market). Market unraveling and the Akerlof lemons model are naturally expressed with types and priors. Numeric illustration: Suppose high-quality cars fraction $0.7$, valuations for buyers depend on type; a pooling price will be set based on expected quality.

- •Mechanism design: Bayesian Incentive Compatibility (BIC) conditions generalize dominant-strategy incentive constraints by requiring truth-telling to maximize expected utility given beliefs over other types. For instance, in auctions revenue-maximization uses BIC constraints: Myerson’s optimal auction solves for virtual values and requires BIC. Numeric illustration: For a single bidder with value distribution F(v)=vF(v)=vF(v)=v on [0,1][0,1][0,1], virtual value is ϕ(v)=v−1−F(v)f(v)=v−1−v1=2v−1\phi(v)=v-\frac{1-F(v)}{f(v)}=v-\frac{1-v}{1}=2v-1ϕ(v)=v−f(v)1−F(v)​=v−11−v​=2v−1. A reserve price solves where ϕ(v)=0\phi(v)=0ϕ(v)=0, i.e., v=0.5v=0.5v=0.5.

Advanced connections: equilibrium selection and refinements

In dynamic Bayesian games with signaling, Perfect Bayesian Equilibrium (PBE) refines BNE by specifying beliefs at every information set and requiring sequential rationality. Sequential Equilibrium further requires consistency of beliefs with strategies via Bayes' rule and limits of perturbed strategies. These refinements are essential when off-path beliefs can sustain multiple spurious equilibria.

Computational aspects

Computing BNE in games with continuous type spaces often reduces to solving functional fixed-point equations (for symmetric equilibria). For example, first-price auction with iid Uniform[0,1] leads to solving an ODE for the symmetric bidding function \(b(v)\). Derivation: Expected payoff for bidder with value vvv bidding bbb and other bidders using b(⋅)b(\cdot)b(⋅) is

U(b∣v)=(v−b) Pr⁡(win with bid b)=(v−b) F(b−1(b))n−1=(v−b) F(β)n−1U(b|v)=(v- b)\,\Pr(\text{win with bid }b)= (v-b)\,F(b^{-1}(b))^{n-1}=(v-b)\,F(\beta)^{n-1}U(b∣v)=(v−b)Pr(win with bid b)=(v−b)F(b−1(b))n−1=(v−b)F(β)n−1

For Uniform[0,1] and symmetric increasing bbb, first-order condition yields b(v)=v−∫0vF(t)n−1dt/F(v)n−1b(v)=v-\int\_0^v F(t)^{n-1}dt/F(v)^{n-1}b(v)=v−∫0v​F(t)n−1dt/F(v)n−1 which simplifies to b(v)=n−1nvb(v)=\frac{n-1}{n}vb(v)=nn−1​v. Numeric: with n=2n=2n=2 bidders and v=0.8v=0.8v=0.8, b=0.4b=0.4b=0.4.

Empirical and experimental applications

Structural estimation: Many empirical studies estimate players’ type distributions and strategy functions from observed behavior by inverting equilibrium conditions (e.g., structural auction estimation). Lab experiments test predictions on signaling or entry under incomplete information.

Practical modeling tips

- •Decide whether types are independent or correlated; correlation can dramatically change equilibrium (common-value vs private-value auctions).
- •Choose common prior carefully; many results depend sensitively on the prior's support.
- •Check on-path vs off-path beliefs: specify how Bayes’ rule applies and which equilibrium refinements are plausible.

Summary: Bayesian games turn private information into a formal object (types) and let you analyze strategic behavior under uncertainty by maximizing expected payoffs conditional on types. The Harsanyi transformation embeds such games into imperfect-information extensive forms, making dynamic analysis and signaling straightforward. This framework underlies auctions, mechanism design, signaling, and inference in strategic settings.

## Worked Examples (3)

### Example 1: Two-player Binary-Types Static Game

Players 1 and 2 each have types T\_i in {H,L}. Prior independent with p1(H)=0.6, p2(H)=0.5. Actions A\_i={0,1}. Payoffs: For player 1, u1(a1,a2,t1)=1 if a1=a2=1 and t1=H; u1=0 otherwise. Player 2 payoff irrelevant. Determine Bayes-Nash optimal action for player 1's each type if player 2 always plays a2=1.

1. Write conditional beliefs: Because types are independent, p(t2=H|t1)=p2(H)=0.5 and p(t2=L|t1)=0.5.
2. Compute expected payoff for player 1 of type H when choosing a1=1: It is u1(1,1,H) times probability that a2=1. Since player 2 plays 1 deterministically, Pr(a2=1)=1. So U1(1|H)=1.
3. Compute expected payoff for player 1 of type H when choosing a1=0: u1(0,a2,H)=0 regardless, so U1(0|H)=0.
4. Therefore type H prefers a1=1 (1>0).
5. For type L, u1(a1,a2,L)=0 for all action profiles by definition, so both actions yield 0. Any action is optimal for type L; pure best responses include a1=0 or a1=1.

**Insight:** This exercise shows how to condition on a player's own type using independence (a simple application of Bayesian Inference) and then compute expected payoffs. It emphasizes that different types may have different best responses and that BNE requires each type to be optimal.

### Example 2: First-price Auction (symmetric BNE)

n=3 bidders. Each bidder's private value V\_i is iid Uniform[0,1]. Determine the symmetric Bayes-Nash equilibrium bidding function b(v) and compute bid for v=0.9.

1. In a symmetric increasing equilibrium, the bidder with value v wins iff her bid is the highest. If others use b(·), the probability a bid b is highest when your value is v equals Pr(others bid ≤ b)=Pr(values ≤ b^{-1}(b))^{n-1}=F(v)^{n-1}. For Uniform[0,1], F(v)=v.
2. Expected payoff from bidding b when your value is v is U(b|v)=(v-b)Pr(win)=(v-b)F(v)^{n-1}. But because b is increasing and you control bid via b=b(x) where x is reported, we look for b that sets the first-order condition when bid equals b(v). Alternatively derive ODE.
3. Derive the symmetric equilibrium by first-order condition or from known formula: For iid Uniform[0,1], b(v)=\frac{n-1}{n}v. For n=3, b(v)=\frac{2}{3}v.
4. Plug v=0.9: b(0.9)=\frac{2}{3}\cdot0.9=0.6.
5. Interpretation: With three bidders, the bidder shades her bid to 60% of her value to trade off higher payment vs winning probability.

**Insight:** This example shows how continuous-type BNE can reduce to solving an ODE or known closed-form expression. It connects to mechanism design and the equilibrium techniques of expected payoff maximization under uncertainty.

### Example 3: Simple Signaling Game — Separating Check

Worker has type H with p=0.4 or L with p=0.6. Education e\in{0,1}. Cost for H is 0, for L is c=1. Employer pays wage w=2 if posterior P(H|e)≥0.5, else w=0. Determine if separating equilibrium where H chooses e=1 and L chooses e=0 can be sustained.

1. Compute posterior after e=1 if only H chooses e=1: P(H|e=1)=1 because only H produce e=1, so employer sets w=2.
2. Compute payoff for H: w - cost = 2 - 0 = 2.
3. Compute payoff for L if she follows strategy e=0: w - cost = 0 - 1 = -1 (since choosing e=0 costs 0 but gives wage 0; cost of 0? Clarify: cost for L for e=0 is 0, so payoff is 0). Correction: Cost for e=0 is 0. So L's payoff from e=0 is 0.
4. If L deviates to e=1, employer’s belief after e=1 becomes P(H|e=1)=p(H)P(e=1|H)/(...) but if deviation occurs, and both types could choose 1, need off-path beliefs. Under the purported separating strategy, employer would infer e=1 implies H with probability 1, so would pay 2. Then L's payoff from deviating is 2 - c = 2 - 1 =1.
5. Since 1>0, L has an incentive to deviate. Therefore the naive separating profile fails. To sustain separation, one needs either greater cost for L (c≥2), or different off-path beliefs or refinements rejecting employers' optimistic beliefs about deviations.

**Insight:** This shows the role of incentive compatibility for different types, how off-path beliefs matter, and why some separating equilibria that look appealing fail because lower types can profitably mimic higher types unless costs deter them sufficiently.

## Key Takeaways

- ✓

  A Bayesian game models incomplete information by introducing type spaces and a common prior; strategies map types to actions and beliefs derive from the common prior using Bayes’ rule.
- ✓

  Bayesian Nash equilibrium requires each type's strategy to be a best response given conditional beliefs about other players’ types — essentially Nash equilibrium applied type-by-type.
- ✓

  Harsanyi transformation converts incomplete-information games into imperfect-information extensive-form games by letting Nature draw types first; BNE corresponds to Nash equilibria of the transformed game.
- ✓

  Signaling games are Harsanyi-style games where an informed sender moves first and an uninformed receiver updates beliefs; off-path beliefs require equilibrium refinements (PBE, Sequential Equilibrium).
- ✓

  Concrete computations: finite-type BNE reduce to solving a system of expected-payoff inequalities for each type; continuous-type symmetric equilibria often reduce to ODEs (e.g., first-price auction bidding function).
- ✓

  Correlation of types, support of priors, and cost structures deeply affect equilibrium existence and selection; careful specification of priors and beliefs is essential.
- ✓

  Many practical fields — auctions, mechanism design, adverse selection, and signaling — are naturally modeled and analyzed within the Bayesian-games framework.

## Common Mistakes

- ✗

  Treating Bayes-Nash equilibrium like Nash equilibrium without conditioning on types: forgetting that each type must individually have no profitable deviation. This leads to incorrect strategy proposals that are not type-wise optimal.
- ✗

  Applying Bayes’ rule on zero-probability events: using Bayes' rule where the conditioning event has zero prior probability or zero likelihood in equilibrium. Off-path beliefs must be justified by refinements, not naive Bayes’ rule.
- ✗

  Confusing incomplete and imperfect information: thinking that missing payoff information (incomplete) is the same as not observing past moves (imperfect). Harsanyi transformation clarifies the conceptual difference.
- ✗

  Assuming independent types without checking: correlation in types can create common-value effects and change incentives — e.g., winner’s curse in auctions arises with interdependent values, not with independent private values.

## Practice

easy

Easy: Two players, each has type H with probability 0.5 independently. Actions {A,B}. Payoffs: player 1 gets 2 if she plays A and player 2 plays A and her type is H; otherwise 0. Player 2 always plays A. What is player 1's best action for each type?

**Hint:** Compute expected payoff for type H and type L separately using independence; recall in "Bayesian Inference" you learned to condition using independence.

Show solution

Because player 2 always plays A, for player 1 type H: payoff from A is 2, from B is 0, so A is best. For type L, payoff is 0 for both actions, so any action is optimal.

medium

Medium: Consider a first-price sealed-bid auction with n=2 bidders, values iid Uniform[0,1]. Derive the symmetric Bayes-Nash bidding function b(v) and compute b(0.8).

**Hint:** Use expected payoff (v - b(v)) times win probability. For symmetric increasing b, win probability when bidding b(v) is F(v)^{n-1}=v^{1}. Use first-order condition or known result b(v)=v/2 for n=2.

Show solution

For n=2, symmetric bidding function solves b(v)=v-\int\_0^v F(t)^{1} dt / F(v)^{1} = v - \int\_0^v t dt / v = v - (v^2/2)/v = v - v/2 = v/2. So b(0.8)=0.4.

hard

Hard: Signaling game. Types H with p=0.3 and L with p=0.7. Cost to choose e=1 is c\_H=0.2 for H and c\_L=0.8 for L. Employer pays w=2 if posterior P(H|e)≥0.5 else w=0. Determine whether a separating equilibrium with H choosing e=1 and L choosing e=0 can be sustained, checking incentive constraints and computing posteriors.

**Hint:** Compute posterior after e=1 assuming only H chooses 1: P(H|e=1)=1. Check payoffs: H gets 2 - 0.2 = 1.8 from separating; would H deviate to e=0? If H deviates to e=0, employer pays 0 so payoff 0. For L, if she deviates to e=1, she'd get 2 - 0.8 = 1.2, compare to staying with e=0 payoff 0. So L can profitably deviate unless c\_L≥2. Be careful and show numbers.

Show solution

Under separating strategy, posterior after e=1 is P(H|e=1)=1, so employer pays w=2. H's payoff following strategy: 2 - 0.2 = 1.8; deviating to e=0 yields 0, so H doesn't deviate. L's payoff from staying at e=0 is 0. If L deviates to e=1, employer pays 2, her payoff would be 2 - 0.8 = 1.2 > 0, so L wants to mimic. Therefore separating equilibrium cannot be sustained. Only if c\_L ≥ 2 would L not want to mimic, in which case separating would be incentive compatible.

## Connections

Looking back: In "Nash Equilibrium" we learned that an equilibrium is a profile where no player benefits from deviating given exact payoffs; Bayesian games adapt that idea by requiring no profitable deviations for each type separately, using conditional expected payoffs. In "Bayesian Inference" we learned to compute posteriors from priors and likelihoods; this operation is used throughout Bayesian games to compute p(t−i∣ti)p(t\_{-i}|t\_i)p(t−i​∣ti​) and to update beliefs after observed actions in signaling games. Looking forward: Mastery of Bayesian games is required for advanced auction theory (deriving bidding strategies and revenue equivalence), mechanism design under private information (Bayesian incentive compatibility and Myerson’s optimal auction), analysis of adverse selection and moral hazard in contract theory, and dynamic signaling models requiring Perfect Bayesian Equilibrium and Sequential Equilibrium refinements. Practical research in empirical IO and structural estimation often builds equilibrium-based models from Bayesian games and estimates priors or type distributions from observed market behavior.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
