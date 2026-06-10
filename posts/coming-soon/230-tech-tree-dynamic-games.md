---
title: Dynamic Games
description: Extensive form games, subgame perfect equilibrium. Sequential rationality, backward induction. Perfect Bayesian equilibrium.
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
permalink: /tech-tree/dynamic-games/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Dynamic Games

Game TheoryDifficulty: ★★★★★Depth: 9Unlocks: 0

Extensive form games, subgame perfect equilibrium. Sequential rationality, backward induction. Perfect Bayesian equilibrium.

## Prerequisites (2)

[Repeated Games? atoms](/tech-tree/repeated-games/)[Bayesian Games? atoms](/tech-tree/bayesian-games/)

## Referenced by (4)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (4)

[BargainingBusiness

Rubinstein alternating-offer bargaining is the canonical extensive-form game solved by backward induction and subgame perfect equilibrium](/business/bargaining/)[Graduated AutonomyBusiness

Graduated autonomy is a sequential game where each stage's delegation level depends on demonstrated quality at prior stages; subgame perfect equilibrium formalizes why ratcheted gates are credible - the principal's threat to revoke autonomy is sequentially rational, not just a bluff](/business/graduated-autonomy/)[PE portfolio companiesBusiness

The sequential game between PE fund (sets EBITDA targets) and portco management (decides invest-in-AI vs hit-short-term-number) has a subgame perfect equilibrium where rational managers always cut AI - backward induction from exit timeline explains the failure mode formally](/business/pe-portfolio-companies/)[TurnaroundBusiness

Turnarounds are sequential multi-player games (PE sponsor, management, creditors, unions, board) where backward induction from a target exit state drives intervention sequencing and subgame perfect equilibrium determines which stakeholders cooperate at each stage.](/business/turnaround/)

Advanced Learning Details

### Graph Position

175

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

9

Chain Length

Dynamic (extensive-form) games let us model the logic of promises, threats and signals across time — the backbone of bargaining, entry deterrence, signaling and reputation. If you want to judge which threats are credible and how beliefs are updated off the equilibrium path, this topic is essential.

TL;DR:

Dynamic games (extensive form) furnish tools — backward induction, subgame perfect equilibrium, sequential rationality and Perfect Bayesian equilibrium — to analyze sequential decisions with possible imperfect and incomplete information and to distinguish credible strategies from empty threats.

## What Is Dynamic Games?

Dynamic games (extensive-form games) are representations of strategic interaction where the order of moves, the information available at each move, and chance events are explicit. Unlike normal-form games where strategies are chosen simultaneously, an extensive-form game is a labeled rooted tree in which nodes represent decision points, edges represent actions, and terminal nodes produce payoffs. This representation is necessary whenever timing, observation and contingent plans matter.

Formal ingredients: a finite set of players NNN, a finite (or countable) set of histories HHH where each nonterminal history h∈Hh\in Hh∈H has an associated player P(h)∈N∪{c}P(h)\in N\cup\{c\}P(h)∈N∪{c} (where ccc is chance), a set of available actions A(h)A(h)A(h) at hhh, information sets that partition decision nodes for imperfect information, a chance probability function for chance nodes, and payoffs defined on terminal histories. A history is a sequence of actions leading from the root; a terminal history has no continuation. In symbols, the extensive form is a tuple Γ=(N,H,P,A,I,u,π)\Gamma=(N,H,P,A,I,u,\pi)Γ=(N,H,P,A,I,u,π) with III the set of information sets and π\piπ chance probabilities.

Example (concrete): the ultimatum game in extensive form. Player 1 proposes a split x∈{0,1,2}x\in\{0,1,2\}x∈{0,1,2} of a pie of size 2; player 2 either Accept (A) or Reject (R). If 2 accepts, payoffs are (2−x,x)(2-x,x)(2−x,x); if 2 rejects, payoffs are (0,0)(0,0)(0,0). Here HHH are sequences: root, then (propose xxx), then (respond A or R); all nodes are singletons (perfect information). This is a canonical dynamic game with numerically specified payoffs.

Imperfect information and information sets: an information set for player iii groups decision nodes between which iii cannot distinguish; within an information set the available action set must be identical. For example, in a signaling game (see Section 4) the receiver's move may be made without knowing the sender's type; those nodes form an information set for the receiver.

Why dynamic analysis is different from static (normal-form) analysis: strategies in an extensive form specify contingent plans (an action at every information set), not just a single move. This makes Nash equilibrium sometimes permissive, allowing strategies that use incredible threats to sustain behavior. Subgame perfect equilibrium (SPE) refines Nash by requiring that strategies constitute a Nash equilibrium in every subgame — removing noncredible threats. In games with imperfect information and incomplete information, sequential rationality and belief refinement (e.g., Perfect Bayesian equilibrium) are required to ensure consistency of off-path belief updates.

Relation to prerequisites: In "Repeated Games" we learned how history-dependent strategies sustain cooperation when future payoffs matter; an extensive-form game is a single-shot temporal structure where history matters within one play rather than across repeated plays. In "Bayesian Games" we learned about type spaces and Bayes' rule; Perfect Bayesian equilibrium integrates those ideas into dynamic settings by pairing strategies with beliefs over types at information sets and imposing Bayesian updating wherever possible.

Key notions to keep in mind going forward:

- •Strategy: a complete contingent plan assigning an action to every information set of a player.
- •Subgame: a node and all its descendants that form a tree starting at a single decision node and not cutting any information sets. For example, in the ultimatum game the move after a given proposal is a subgame.
- •Backward induction: a constructive method to compute equilibria in finite games with perfect information by solving subgames from the end.
- •Sequential rationality: given beliefs at each information set, players' actions must maximize expected payoff given those beliefs.

Concrete formula with numbers: suppose at a decision node player iii faces two actions a1a\_1a1​ and a2a\_2a2​, and the payoffs from the subsequent terminal nodes are ui(a1)=3u\_i(a\_1)=3ui​(a1​)=3 and ui(a2)=2u\_i(a\_2)=2ui​(a2​)=2. Then sequential rationality requires choosing a1a\_1a1​ because $3>2$. If there is a chance that a downstream chance node yields payoff 3 with probability $0.4$ and payoff $1$ with probability $0.6$, the expected payoff is $0.4\cdot 3+0.6\cdot 1=1.8$; compare numerically to other actions.

This section has set the stage: extensive form = tree + information sets; strategies are contingent plans; SPE and sequential rationality refine Nash to handle sequential moves and beliefs. The remainder will operationalize these notions and show how to solve real problems.

## Core Mechanic 1: Backward Induction and Subgame Perfect Equilibrium

Backward induction is the principal algorithm for solving finite extensive-form games with perfect information. It embodies the idea of sequential rationality: at each decision node, the acting player chooses an action that maximizes her payoff given the continuations (which are already solved because we move from leaves toward the root). The solution produced by backward induction is a subgame perfect equilibrium (SPE).

Definition (subgame): A subgame is a node hhh such that the tree consisting of hhh and all its descendants contains only information sets that are subsets of that tree (i.e., no information set is cut). A proper subgame excludes the root if desired. In games of perfect information every node starts a subgame.

Definition (SPE): A strategy profile s∗s^\*s∗ is a subgame perfect equilibrium if for every subgame G′G'G′ the restriction s∗∣G′s^\*|\_{G'}s∗∣G′​ is a Nash equilibrium of G′G'G′. Equivalently, no player can profitably deviate at any history, taking as given that future play follows s∗s^\*s∗.

The backward induction algorithm (constructive):

1. 1)Identify all terminal nodes and their payoffs.
2. 2)Find a decision node whose immediate successors are terminal. For that node, choose the action that yields the highest payoff for the acting player; record that action and replace the node with the resulting payoff.
3. 3)Repeat: treat the reduced tree similarly until reaching the root. The actions chosen at each step assemble into a strategy profile; this profile is an SPE.

Theorem (Backward induction yields an SPE in finite perfect-information games): For any finite extensive-form game of perfect information, the action choices generated by backward induction define a unique SPE (unique path-of-play under generic payoffs; strategies may be multiple if indifferent choices exist). Proof sketch: solve base nodes to get best responses, then contract these nodes; at each contraction the chosen actions are best replies given future play; since every subgame will be one of these contracted trees, the final profile is a Nash equilibrium in every subgame.

Concrete numeric example (Ultimatum game): Player 1 proposes x∈{0,1,2}x\in\{0,1,2\}x∈{0,1,2} to split a pie of 2. Player 2 accepts or rejects. Payoffs: accept -> (2−x,x)(2-x,x)(2−x,x); reject -> (0,0)(0,0)(0,0). Backward induction: for each xxx, player 2 compares acceptance payoff xxx vs rejection payoff $0;acceptiff; accept iff ;acceptiffx\ge 0.Numerically:if. Numerically: if .Numerically:ifx=0thenaccept(0vs0indifferent;assumeaccept),if then accept (0 vs 0 indifferent; assume accept), if thenaccept(0vs0indifferent;assumeaccept),ifx=1accept(1>0),if accept (1>0), if accept(1>0),ifx=2accept(2>0).Anticipatingthis,player1chooses accept (2>0). Anticipating this, player 1 chooses accept(2>0).Anticipatingthis,player1choosesxmaximizinghispayoffamongthoseaccepted: maximizing his payoff among those accepted: maximizinghispayoffamongthoseaccepted:x=0gives2toplayer1, gives 2 to player 1, gives2toplayer1,x=1gives1, gives 1, gives1,x=2gives0.Soplayer1picks gives 0. So player 1 picks gives0.Soplayer1picksx=0andplayer2accepts—backwardinductionyieldsoutcome(2,0).Thisdemonstrateshowbackwardinductioneliminatesnon−crediblethreats:anyrejectionbyplayer2whenoffered and player 2 accepts — backward induction yields outcome (2,0). This demonstrates how backward induction eliminates non-credible threats: any rejection by player 2 when offered andplayer2accepts—backwardinductionyieldsoutcome(2,0).Thisdemonstrateshowbackwardinductioneliminatesnon−crediblethreats:anyrejectionbyplayer2whenofferedx=0$ would be costly to her and thus non-credible.

Numeric illustration of contract step: at nodes after proposals, the best replies for player 2 are A for x=1x=1x=1 since $1>0,andAfor, and A for ,andAforx=0$ assuming tie-break. Replace those nodes by payoffs. Player 1 then chooses the proposal maximizing his payoff across the replaced nodes.

Remark about uniqueness and tie-breaking: if player 2 is indifferent for some offers (e.g., x=0x=0x=0 gives 0 either way), multiple SPE strategy profiles can exist (tied responses). However the backward induction path (outcome) is unique if payoffs are generic or if tie-breaking is fixed.

Games with imperfect information: backward induction requires perfect information. If there are non-singleton information sets, the notion of subgame is narrower, and backward induction cannot be applied directly across an information set that gets cut. For such games we need richer equilibrium concepts (sequential rationality plus beliefs).

Numeric example with chance: consider a decision node where the player faces two actions leading to chance node with probabilities (0.3,0.7)(0.3,0.7)(0.3,0.7). If action a1a\_1a1​ leads to expected payoff $0.3\cdot 5+0.7\cdot 1=1.5+0.7=2.2and and anda\_2leadstopayoff2,theplayerprefers leads to payoff 2, the player prefers leadstopayoff2,theplayerprefersa\_1$ since $2.2>2.0$.

Backward induction is mechanistic, but it encodes a strong rationality assumption: players will correctly anticipate future rational behavior and use that to plan current moves. In the next section we'll generalize this by making beliefs explicit and imposing sequential rationality in the presence of incomplete information.

## Core Mechanic 2: Sequential Rationality and Perfect Bayesian Equilibrium

When imperfect information or incomplete information is present, backward induction alone is insufficient. We need a refinement that incorporates beliefs about which node within an information set has been reached, and requires that actions maximize expected payoffs given those beliefs. Perfect Bayesian equilibrium (PBE) formalizes this idea by pairing strategies with a belief system and imposing sequential rationality plus Bayes' rule wherever possible.

Assessment: An assessment is a pair ⟨s,μ⟩\langle s,\mu\rangle⟨s,μ⟩ where sss is a strategy profile and μ\muμ assigns to each information set an internal probability distribution over the nodes in that information set (players' beliefs about where they are). The beliefs must satisfy consistency: on the path of play they should be derived from the strategies and nature's probabilities using Bayes' rule; off the path they must be specified but should be justifiable by some limit argument (Kreps-Wilson consistency) to avoid arbitrary beliefs.

Sequential rationality: Given the assessment ⟨s,μ⟩\langle s,\mu\rangle⟨s,μ⟩, at every information set of player iii the strategy sis\_isi​ must specify an action that maximizes iii's expected payoff conditional on the belief μ\muμ and given other players' strategies s−is\_{-i}s−i​. Formally, for each information set III of player iii and each available action aaa at III,

Ui(s∣I)=∑h∈Iμ(h)⋅Ui(s∣h)≥∑h∈Iμ(h)⋅Ui((a,si∣I→a)∣h),U\_i(s|I)=\sum\_{h\in I}\mu(h)\cdot U\_i(s|h)\ge \sum\_{h\in I}\mu(h)\cdot U\_i((a,s\_i|\_{I\to a})|h),Ui​(s∣I)=h∈I∑​μ(h)⋅Ui​(s∣h)≥h∈I∑​μ(h)⋅Ui​((a,si​∣I→a​)∣h),

where si∣I→as\_i|\_{I\to a}si​∣I→a​ denotes the strategy that equals sis\_isi​ except it plays aaa at III. Numeric example: suppose two nodes in III with beliefs μ=(0.6,0.4)\mu=(0.6,0.4)μ=(0.6,0.4). If action aaa yields continuation payoffs $4$ and $1$ respectively, expected payoff is $0.6\cdot 4+0.4\cdot 1=2.4+0.4=2.8.Ifaction. If action .Ifactionb$ yields payoffs $2$ and $3$, expected payoff is $0.6\cdot 2+0.4\cdot 3=1.2+1.2=2.4.Sequentialrationalityrequireschoosing. Sequential rationality requires choosing .Sequentialrationalityrequireschoosinga$ (2.8>2.4).

Bayes' rule: On the equilibrium path, beliefs must satisfy Bayes' rule. If III contains nodes h1,…,hkh\_1,\dots,h\_kh1​,…,hk​ and prior probabilities on types or chance and conditional probabilities induced by strategies give probability p(hj)p(h\_j)p(hj​) to node hjh\_jhj​, then

μ(hj)=p(hj)∑ℓ=1kp(hℓ).\mu(h\_j)=\frac{p(h\_j)}{\sum\_{\ell=1}^k p(h\_\ell)}.μ(hj​)=∑ℓ=1k​p(hℓ​)p(hj​)​.

Numeric example: suppose prior over two types is {θ1:0.7,θ2:0.3}\{\theta\_1:0.7,\theta\_2:0.3\}{θ1​:0.7,θ2​:0.3} and type-dependent sender plays message mmm with probabilities $0.5$ and $0.2respectively;thentheprobabilityof respectively; then the probability of respectively;thentheprobabilityofm$ is $0.7\cdot 0.5+0.3\cdot 0.2=0.35+0.06=0.41.Thereceiver′sbeliefthatthesenderis. The receiver's belief that the sender is .Thereceiver′sbeliefthatthesenderis\theta\_1givenmessage given message givenmessagem$ is $0.35/0.41\approx 0.8537$.

Perfect Bayesian equilibrium (PBE): An assessment ⟨s,μ⟩\langle s,\mu\rangle⟨s,μ⟩ is a PBE if (i) strategies are sequentially rational given beliefs μ\muμ, and (ii) beliefs μ\muμ are Bayes-plausible (obtained from sss and prior by Bayes' rule wherever possible). Often one also asks for the stronger consistency requirement in Kreps and Wilson (1982): beliefs must be the limit of Bayes-updated beliefs induced by a sequence of completely mixed strategies converging to sss.

Examples of PBE concepts:

- •Separating vs. pooling equilibria in signaling games: In separating equilibria different types choose different messages, yielding receiver beliefs that fully reveal type; in pooling equilibria multiple types choose the same message making the receiver's belief a posterior mixing types.
- •Off-path beliefs matter: In signaling games, off-path messages produce a family of possible beliefs for the receiver; only those beliefs that survive a reasonable refinement (e.g., the Intuitive Criterion or D1) are acceptable.

Concrete signaling numeric example: Sender has type H with prob. 0.6 and L with 0.4. If H sends message m\_H with prob 1 and L sends m\_L with prob 1, receiver upon m\_H's occurrence has belief P(H|m\_H)=1. If receiver's best response to m\_H is action a\_H yielding payoff 5 to both sender and receiver when type H, sequential rationality must hold: given belief 1, the receiver chooses a\_H if its expected payoff exceeds alternatives. If instead off-path message m' is observed, the receiver's belief is unspecified by Bayes; one can select beliefs that make certain off-path strategies sequentially rational or not.

Comparison to Bayesian Nash equilibrium: In "Bayesian Games" we learned to pair strategies with beliefs about types and use Bayes' rule to compute expected payoffs. PBE refines this by tracking beliefs at each information set reached in the dynamic game and requiring sequential rationality at every information set (not just before play starts). In other words, PBE = strategy profile + belief system + Bayesian updating + sequential rationality.

Refinements and limitations: PBE does not uniquely resolve all off-path belief selection; refinements like the Intuitive Criterion (Cho-Kreps), D1, and divine equilibrium aim to eliminate implausible beliefs. For dynamic games with perfect information PBE reduces to SPE. For games with signaling and incomplete information PBE is the standard workhorse but must be used with care and often supplemented with plausibility refinements.

## Applications and Connections

Dynamic games and equilibrium refinements are central to economic theory and adjacent fields. They connect closely to contract theory, industrial organization, political economy, mechanism design and behavioral economics where timing, observability and private information shape incentives.

1) Bargaining and negotiations. The Rubinstein alternating-offers model is an extensive-form game with infinite horizon; backward induction (in the limit) and subgame perfection identify unique stationary SPE dividing the surplus according to discount factors. Connection to "Repeated Games": the folk-theorem insights about supporting cooperative outcomes via trigger strategies can be read as an infinite-horizon extension of the logic of credible threats — but in finite-horizon bargaining backward induction collapses cooperation. Numeric illustration: with discount factor δ1=0.9,δ2=0.8\delta\_1=0.9,\delta\_2=0.8δ1​=0.9,δ2​=0.8 the SPE share for player 1 in the stationary solution is $1-\delta\_2/(1-\delta\_1\delta\_2)$ etc. (specific formula derivable from first-order conditions).

2) Industrial organization: entry deterrence and Stackelberg leadership are naturally modeled as extensive-form games. Example: entrant chooses to enter or stay out; incumbent chooses to fight or accommodate. Subgame perfection deletes non-credible threats to fight if fighting is costly. Numeric example: entrant's payoff if enter & fight = −1-1−1, if enter & accommodate = $1$, if stay out = $0$. If incumbent fighting yields negative payoff to the incumbent, a credible deterrent must be supported by an SPE in which the incumbent's strategy after entering is optimal.

3) Signaling and reputation. In games of incomplete information (we studied "Bayesian Games" earlier), dynamic interactions let a long-run player build a reputation; Perfect Bayesian equilibrium is the language to describe reputation equilibria in repeated or long-lived games. Numeric example: firm with private quality type 'good' or 'bad' chooses quality signal; consumers update with Bayes' rule. The work by Milgrom and Roberts and Rubinstein and others connects PBE to reputational dynamics.

4) Mechanism design and dynamic contracting. When agents take sequential actions or have private information that evolves, designers use PBE concepts to ensure incentive compatibility over time. Example: dynamic moral hazard where actions today affect future information; sequential rationality ensures continuation incentives.

5) Empirical industrial organization and experimental economics. Dynamic game models are used to interpret observed deviations from static Nash predictions — e.g., why incumbents fight entry in data (reputation), or why people reject low offers in ultimatum-like settings (social preferences vs. off-path beliefs). Researchers estimate dynamic structural models by computing (or approximating) SPE or PBE and matching to data.

6) Computational aspects. Solving large extensive-form games (e.g., poker) requires equilibrium refinements and computational tools. Counterfactual regret minimization (CFR) and sequence-form representations exploit the extensive structure to compute approximations to Nash and sequential equilibria. Numeric illustration: in heads-up limit poker the game tree has on the order of $10^{10}$ nodes — computational algorithms operate on compressed sequence-form linear programs.

Bringing prerequisites to bear: In "Repeated Games" we used backward induction in finite-horizon repeated settings and folk-theorem logic in infinite horizons; here, backward induction is the local operation inside the single extensive-form tree. In "Bayesian Games" we learned how to form posteriors; PBE operationalizes that logic at every information set. Downstream, dynamic mechanism design, reputation models, and computational game theory build directly on the formalism of extensive forms and PBE.

Concluding numeric note: Suppose a signaling game where sender types are High (H) with prob 0.7 and Low (L) with 0.3. High sends message m\_H costing 2 to produce but yields buyer belief leading to price 10; Low can mimic but net payoff 8-2=6 vs 0 if not. The incentive constraints become inequalities like: For H, 10-2\ge payoff of pooling; if numbers yield 8, inequality numerically holds. Checking such inequalities is the core of constructing separating PBEs.

In sum: dynamic games give precise language and operational tools to analyze sequential strategic interaction. Mastery of backward induction, SPE and PBE — together with the insights from "Repeated Games" and "Bayesian Games" — opens the door to modeling negotiations, signaling, reputation and dynamic contracts at research depth.

## Worked Examples (3)

### Ultimatum Game (finite offers)

Two players. Player 1 proposes split x\in\{0,1,2\} of pie size 2. Player 2 chooses Accept (A) or Reject (R). Payoffs: accept -> (2-x,x); reject -> (0,0). Compute the subgame perfect equilibrium via backward induction.

1. Step 1: Identify subgames. After each proposal x the responder's decision node is a proper subgame (perfect information).
2. Step 2: Solve responder's best responses. For each x compute payoff from Accept and Reject. For x=0: Accept gives player2 payoff 0, Reject gives 0 -> tie. For x=1: Accept gives 1>0 so Accept. For x=2: Accept gives 2>0 so Accept.
3. Step 3: Resolve tie in x=0. Assume tie-break that player 2 Accepts when indifferent. Thus for all x the responder Accepts.
4. Step 4: Anticipate acceptance and choose proposer action. Player 1's payoff from choosing x is 2-x (because acceptance). So for x=0 payoff 2, x=1 payoff 1, x=2 payoff 0. Maximum at x=0.
5. Step 5: Assemble SPE. Player 1 proposes x=0; player 2 Accepts any proposal (or at least Accepts x=0 and accepts others). The equilibrium path is (x=0, Accept) with payoffs (2,0).

**Insight:** This example shows backward induction eliminating non-credible threats: any threat by player 2 to reject low offers is non-credible because rejecting reduces her own payoff. It also demonstrates that strategy multiplicity can arise from indifference at information sets.

### Stackelberg Duopoly (entry and quantity choice)

Two firms. Leader (firm 1) chooses quantity q1\ge0. Follower (firm 2) observes q1 and then chooses q2\ge0. Market price P=10-(q1+q2). Cost per unit is zero. Compute subgame perfect equilibrium quantities and payoffs.

1. Step 1: Follower's best response function. Given q1, firm2 maximizes q2\cdot(10-(q1+q2)). First-order condition: 10-(q1+2q2)=0 => q2 = (10-q1)/2. For example if q1=2 then q2=(10-2)/2=4.
2. Step 2: Leader anticipates follower response. Substitute q2(q1) into leader's profit: \nU1(q1)=q1\cdot(10-(q1+q2(q1)))=q1\cdot(10-q1-(10-q1)/2)=q1\cdot((10-q1)/2). Numeric simplification: U1(q1)=0.5 q1 (10-q1).
3. Step 3: Maximize leader profit. First-order condition: 0.5(10-q1)-0.5 q1 =0 => 5 - q1 =0 => q1^*=5. Check second-order: negative, maximum. Numeric: q1^*=5.
4. Step 4: Compute follower quantity: q2^\*=(10-5)/2=2.5. Compute price P=10-(5+2.5)=2.5.
5. Step 5: Payoffs: U1=5*2.5=12.5; U2=2.5*2.5=6.25. Verify no profitable deviation: follower best-responds by construction; leader optimized anticipating follower. Thus (5,2.5) is SPE.

**Insight:** This shows backward induction in continuous strategy spaces: the follower's reaction function and leader's optimization yield a unique SPE. Numeric calculations illustrate substitution and first-order conditions in equilibrium construction.

### Signaling Game: Separating vs Pooling PBE

Sender (S) has type H with prob 0.6 and L with prob 0.4. Sender chooses message m\in\{m\_H,m\_L\}. Cost of sending m\_H is c\_H for type H and c'\_L for type L. Receiver upon observing message chooses action a\in\{a\_1,a\_2\}. Payoffs: if receiver chooses correctly for H, payoff 10 to both; incorrectly, payoff 0. Suppose c\_H=1, c'\_L=3, and the off-path beliefs are undetermined. Identify a separating PBE if possible.

1. Step 1: Candidate separating profile: type H sends m\_H, type L sends m\_L. Receiver upon m\_H plays a\_1 (best for H), upon m\_L plays a\_2 (best for L).
2. Step 2: Check receiver's sequential rationality on-path: upon m\_H belief P(H|m\_H)=1 so a\_1 yields 10>0 => choose a\_1. Upon m\_L belief P(L|m\_L)=1 so a\_2 yields 10>0 => choose a\_2.
3. Step 3: Check sender incentives. Given receiver responses: type H gets payoff 10-c\_H=10-1=9 by sending m\_H. If H deviated to m\_L he'd get payoff that L gets when sending m\_L, which is 0-c\_H? More precisely if H sends m\_L receiver plays a\_2 giving payoff 0 minus cost of sending m\_L: assume zero cost for m\_L for simplicity then payoff 0. So staying is better (9>0).
4. Step 4: Check type L's incentives. L sending m\_L gets 10-c'\_L=10-3=7. If L deviated to m\_H the receiver upon m\_H would play a\_1 (intended for H) giving 0 minus cost of m\_H (c'\_L=3) so payoff -3. So L prefers m\_L (7>-3).
5. Step 5: Beliefs and off-path adjustments. Bayes' rule holds on-path. Off-path messages need not arise; PBE exists with these beliefs. Thus the separating profile with receiver actions as specified and beliefs P(H|m\_H)=1,P(L|m\_L)=1 is a PBE.

**Insight:** The example demonstrates checking incentive compatibility for each type given receiver actions, and shows how sending costs can support separation. It illustrates the typical structure of constructing PBE: propose strategies, compute beliefs by Bayes' rule on-path, verify sequential rationality for both sender and receiver.

## Key Takeaways

- ✓

  Extensive-form (dynamic) games model timing and information explicitly: strategies are complete contingent plans over information sets, not single moves.
- ✓

  Backward induction solves finite perfect-information games and yields subgame perfect equilibria (SPE) by ensuring optimality in every subgame, eliminating non-credible threats.
- ✓

  Subgame perfect equilibrium refines Nash equilibrium: every restriction of an SPE to a subgame is a Nash equilibrium of that subgame.
- ✓

  Perfect Bayesian equilibrium (PBE) augments strategies with beliefs; it imposes sequential rationality and Bayes' rule (where applicable) and is the standard refinement in dynamic games with imperfect/incomplete information.
- ✓

  Off-path beliefs matter: many equilibria depend on how beliefs are specified at unreached information sets; refinements like the Intuitive Criterion or D1 attempt to single out plausible beliefs.
- ✓

  Numerical checks reduce to verifying incentive constraints and Bayesian updates: compute expected payoffs under beliefs, compare deviations, and ensure Bayes-plausibility on the path.
- ✓

  Applications include bargaining, entry deterrence, signaling, reputation and dynamic mechanism design; computational methods (sequence form, CFR) are crucial for large games.

## Common Mistakes

- ✗

  Confusing Nash equilibrium in the normal form with subgame perfection: a normal-form Nash equilibrium may prescribe non-credible threats at off-path nodes; one must check equilibrium behavior at every subgame.
- ✗

  Applying backward induction when information sets are non-singleton: backward induction requires perfect information; with imperfect information you need beliefs and sequential rationality instead.
- ✗

  Neglecting Bayes' rule on the equilibrium path: beliefs at reached information sets must be consistent with the strategy profile and priors — failing to update properly leads to invalid assessments.
- ✗

  Assuming PBE uniquely pins down off-path beliefs: PBE allows many off-path beliefs; without a refinement these beliefs can be arbitrary, which can make predicted equilibria fragile.

## Practice

easy

Easy: Consider a two-step game. Player 1 chooses L or R. If L, game ends with payoffs (3,1). If R, player 2 chooses U or D: U -> (0,0), D -> (1,2). Find all subgame perfect equilibria.

**Hint:** Solve the subgame at player 2's node first by comparing U and D; then pick player 1's best response anticipating player 2's choice.

Show solution

At player 2's node, U yields 0, D yields 2 so D strictly dominates. So in any SPE player 2 plays D at that node. Anticipating D, player1's payoff from R is 1; from L is 3, so player 1 chooses L. Thus SPE strategy profile: player1 chooses L; player2 chooses D (the action at her information set). Unique SPE outcome (3,1).

medium

Medium: A signaling game: Sender type High (prob 0.5) or Low (0.5). Sender chooses message m or n. Cost of m is 1 for High and 0 for Low; cost of n is 0 for both. Receiver after message chooses Accept (A) or Reject (R). Payoffs: If receiver accepts and type High, sender gets 5-cost; receiver gets 5. If accepts and Low, sender gets 1-cost; receiver gets 1. If reject, both get 0. Find a pooling PBE where both types send n and receiver Rejects, if possible.

**Hint:** Compute receiver's posterior belief given message n under pooling, then check if rejection is optimal. Then check incentive for each type not to deviate to m, considering send costs and receiver's response to m (off-path belief is free but must be plausible).

Show solution

Under pooling on n, Bayes' rule gives P(H|n)=0.5. Receiver's expected payoff from Accept given n is 0.5*5+0.5*1=3, which exceeds 0 from Reject. So the receiver would Accept on-path; hence Reject cannot be part of an equilibrium on-path. Could we have receiver Reject on-path? No. So a pooling PBE with Reject on n does not exist. Alternatively, suppose receiver Accepts on n; then check deviations: High's payoff sending n and being accepted is 5-0=5. If High deviates to m (cost 1), receiver's response to m (off-path) could be Reject, making deviation unprofitable. But because receiver Accepts n, equilibrium is pooling with Accept on n. Thus the only plausible pooling equilibrium must have Accept on n, not Reject.

hard

Hard: Consider a two-period reputation model. A seller may be type Good (prob p) or Bad (1-p). In each period seller chooses High quality (H) or Low quality (L). Producing H costs c\_G=1 for Good and c\_B=4 for Bad. Buyers are short-lived and after observing quality buy in that period for price v=5 if they observe H, price 0 if L. Sequence: nature draws type once; seller moves twice. Buyers don't observe type but observe quality each period and update beliefs for period 2. Characterize PBE where Good separates by playing H in period 1 and Bad plays L, and buyers buy both periods if they saw H in period1. Provide conditions on p and c\_B for this to be an equilibrium.

**Hint:** Check buyers' beliefs via Bayes' rule after observing H in period1; compute continuation payoffs and incentive constraints for both seller types to follow the purported strategies (no profitable deviation in period1).

Show solution

If buyers buy in period2 after observing H in period1, their belief P(type=Good|H1)=1 because Bad would not mimic (assumed separating). Buyers then buy in period2 yielding price v=5. Seller's total payoff for Good playing H1 and H2: period1 payoff v - c\_G =5-1=4; period2 payoff 4 as well (if sells again) total 8. If Good deviates in period1 to L, buyer will see L and likely not buy in period1 and update beliefs, causing buyer to not buy in period2; Good's payoff from deviation is 0 in period1 and potentially 0 in period2 — so deviation is unprofitable. For Bad, playing L in period1 and then possibly mimicking in period2 is considered. If Bad deviates in period1 to H (cost 4), buyer buys period1 giving payoff 5-4=1 for Bad in period1, but buyer then updates belief to think Bad may have produced H; if buyer still buys in period2 expecting H, Bad's period2 payoff would be 5-4=1, total 2. If sticking to L yields 0 total. So Bad prefers to mimic if 2>0, i.e., mimic profitable. To prevent Bad mimicking, we need either that buyers' beliefs after H assign higher probability to Good enough to keep period2 buying but that Bad's cost is too high to make mimicking attractive. More succinctly, require 2<0? That won't hold. Instead enforce that buyers, anticipating possible mimicking, would not buy in period2 unless probability high; Bayes' rule under separating makes P(Good|H)=1, but that requires Bad not to deviate in period1: incentive constraint for Bad is 5-4 + continuation payoff <= 0 + continuation when L. Consolidating yields constraints: for Good no deviation: 4+4 >= 0+0 -> holds. For Bad no deviation: if Bad deviates to H in period1, gets immediate 1 plus continuation value V\_after\_H (buyer buys next period), which equals 5-4=1, total 2. To deter mimicry need 2 <= 0 which is impossible. Therefore separating equilibrium where Bad doesn't mimic cannot exist unless additional punishments or off-path beliefs cause buyers to not buy after H (contradiction). Conclusion: a separating PBE with complete buyer acceptance in period2 requires that Bad's cost c\_B be so large that 2 <= 0, impossible for positive payoffs; hence no such separating PBE without further off-path specifications. More generally, need c\_B > v so Bad never mimics (here c\_B>5), i.e., 4>5 fails. So to have equilibrium require c\_B>v (numerically c\_B>5).

## Connections

Looking back: This lesson builds directly on "Repeated Games" and "Bayesian Games". From "Repeated Games" we inherit methods for dealing with history-dependent strategies and the importance of discounting and punishment for supporting outcomes; backward induction is the finite-horizon analogue of the logic used in repeated interactions. From "Bayesian Games" we inherit type spaces, priors and Bayes' rule; Perfect Bayesian equilibrium explicitly integrates beliefs from Bayesian Games into dynamic settings by assigning beliefs at every information set and requiring Bayesian updating on the equilibrium path. Looking forward: mastery of dynamic games and PBE is necessary for advanced work in reputation models (e.g., Kreps-Wilson reputation effects), dynamic mechanism design (time-consistent contracts, evolving private information), dynamic matching markets, and computational game theory for large extensive-form games (sequence form, CFR algorithms). Applied fields that require this material include industrial organization (entry deterrence, price wars), political economy (dynamic signaling of policy), finance (dynamic contracting and moral hazard), and behavioral game theory (experiments on ultimatum and trust games). Specific downstream techniques that require this topic: construction of incentive-compatible dynamic contracts, proof of folk-theorem variants for stochastic games, and algorithmic equilibrium computation for imperfect-information games (used in AI for games like poker).

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
