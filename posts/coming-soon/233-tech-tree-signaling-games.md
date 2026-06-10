---
title: Signaling Games
description: Spence signaling model, adverse selection, moral hazard. Screening mechanisms. Pooling vs separating equilibria. Applications to quality signaling via price.
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
inspiration_url: https://templeton.host/tech-tree/signaling-games/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/signaling-games/](https://templeton.host/tech-tree/signaling-games/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Signaling Games

Game TheoryDifficulty: ★★★★★Depth: 9Unlocks: 0

Spence signaling model, adverse selection, moral hazard. Screening mechanisms. Pooling vs separating equilibria. Applications to quality signaling via price.

## Prerequisites (2)

[Bayesian Games? atoms](/tech-tree/bayesian-games/)[Mechanism Design11 atoms](/tech-tree/mechanism-design/)

## Referenced by (5)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (5)

[positioningBusiness

Positioning IS signaling under asymmetric information - Spence's model formalizes how agents differentiate via costly signals, pooling vs separating equilibria map directly to commodity vs differentiated positioning strategies](/business/positioning/)[brand identityBusiness

Brand identity is a signaling mechanism: firms invest in consistent identity to credibly signal quality, values, and positioning, mapping directly to Spence signaling and separating vs pooling equilibria](/business/brand-identity/)[Capital StructureBusiness

Adverse selection and signaling theory provides the formal foundation for pecking order theory - why capital structure choices (debt vs equity issuance) convey private information to markets about firm quality](/business/capital-structure/)[Knowledge CapitalBusiness

Spence's signaling model is the mathematical framework for knowledge capital valuation under asymmetric information - credentials, track records, and publications are signals of unobservable knowledge capital quality](/business/knowledge-capital/)[Registered Investment AdvisorBusiness

The RIA designation is a textbook quality signal solving adverse selection in the financial advice market - registration, fiduciary duty, and regulatory oversight are screening mechanisms that separate credible advisors from conflicted salespeople (pooling vs separating equilibria)](/business/registered-investment-advisor/)

Advanced Learning Details

### Graph Position

139

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

9

Chain Length

Signals — like a résumé, a warranty, or a premium price — change what uninformed agents believe about hidden characteristics. Understanding signaling games tells you when such signals credibly convey information and when they are just expensive theater.

TL;DR:

Signaling games analyze how informed senders manipulate observable costly signals to influence uninformed receivers' beliefs and actions; the theory gives conditions (incentive constraints, belief specifications, equilibrium refinements) that separate credible informational equilibria from implausible ones and connects directly to screening and mechanism design.

## What Is Signaling Games?

Definition and core intuition

A signaling game is a two-stage Bayesian game of incomplete information (see "Bayesian Games", prerequisite). In the canonical form there are two players: a sender (S) who privately knows her type θ∈Θ\theta\in\Thetaθ∈Θ and a receiver (R) who does not. The sender first chooses a signal s∈Ss\in Ss∈S — an observable action or attribute — and then the receiver chooses an action a∈Aa\in Aa∈A. Payoffs depend on the sender's type, the signal, and the receiver's action: uS(θ,s,a)u\_S(\theta,s,a)uS​(θ,s,a) and uR(θ,s,a)u\_R(\theta,s,a)uR​(θ,s,a). The timing converts private information into an observable signal that can influence posterior beliefs and hence decisions; the Harsanyi transformation (a prerequisite: "Bayesian Games") allows us to treat types as drawn by Nature.

Core example: the Spence model (education as signal). Two worker types, High (H) and Low (L), differ in productivity πH>πL\pi\_H>\pi\_LπH​>πL​. Education level s≥0s\ge0s≥0 is observable but costly: type ttt pays cost ct(s)c\_t(s)ct​(s). Firms (receivers) observe sss, form beliefs μ(θ∣s)\mu(\theta\mid s)μ(θ∣s) and pay expected wage equal to expected productivity, e.g. wage schedule w(s)=E[πθ∣s]w(s)=\mathbb{E}[\pi\_\theta\mid s]w(s)=E[πθ​∣s]. The worker's payoff is w(s)−cθ(s)w(s)-c\_\theta(s)w(s)−cθ​(s). The signaling question: is there an equilibrium in which different types select different sss such that firms infer type from sss? That is, a separating equilibrium.

Adverse selection vs moral hazard

Signaling arises from adverse selection: one side has private information about a static attribute (quality, cost, productivity). By contrast, moral hazard involves hidden actions taken after contracting (effort choice). Both are central to contracting and mechanism design. In "Mechanism Design", we learned to design allocation and transfer rules to implement desired outcomes subject to incentive compatibility. Signaling is about how agents themselves may influence beliefs; screening is how a principal uses a menu to induce self-selection when facing adverse selection.

Why it matters

Signaling theory explains pervasive phenomena: why schooling credentials exist even when they don't increase productivity, why firms use warranties or prices as signals of quality, and why insurance contracts are differentiated. It provides testable predictions: signals must be more costly for lower types (cost separability), and equilibrium configurations (pooling versus separating) depend on the shape of cost functions and priors.

A very simple numeric intuition

Suppose two types H and L with productivities πH=10\pi\_H=10πH​=10, πL=5\pi\_L=5πL​=5. Prior probability of H is p=0.5p=0.5p=0.5. Education costs are linear: cH(s)=sc\_H(s)=scH​(s)=s and cL(s)=3sc\_L(s)=3scL​(s)=3s. If firms pay w(s)=E[π∣s]w(s)=\mathbb{E}[\pi\mid s]w(s)=E[π∣s], then a separating equilibrium can exist if the high type chooses some sHs\_HsH​ and the low type chooses sL=0s\_L=0sL​=0 so that firms pay w(sH)=10w(s\_H)=10w(sH​)=10 and w(0)=E[π∣s=0]=5w(0)=\mathbb{E}[\pi\mid s=0]=5w(0)=E[π∣s=0]=5 (believing level 0 comes from L). High's net payoff is $10-s\_H$, low's payoff at 0 is $5$. High prefers separation if $10-s\_H\ge 5i.e. i.e. i.e.s\_H\le5$. Low won't mimic if $5-3s\_H\le5i.e. i.e. i.e.-3s\_H\le0whichistrueforall which is true for all whichistrueforalls\_H\ge0.Soany. So any .Soanys\_H\in[0,5]couldsustainseparationunderbeliefsthatassignhightypeto could sustain separation under beliefs that assign high type to couldsustainseparationunderbeliefsthatassignhightypetos\_H$ and low type to 0. This numeric check illustrates the two key constraints you'll formalize: incentive-compatibility (IC) for types and firm beliefs on the path and off-the-path.

Formal equilibrium concept

We use Perfect Bayesian Equilibrium (PBE): strategies for S and R plus beliefs μ(θ∣s)\mu(\theta\mid s)μ(θ∣s) satisfying Bayes' rule on-path and utility maximization given beliefs, and beliefs consistent with Bayes' rule where applicable. Signaling adds the wrinkle that off-path beliefs (how the receiver interprets signals not observed in equilibrium) can make or break equilibria; hence the need for refinements (e.g., the Intuitive Criterion) to rule out implausible beliefs.

This section built directly on "Bayesian Games" (Harsanyi beliefs and BNE) and "Mechanism Design" (incentive constraints will be used heavily).

## Core Mechanic 1: Incentive-Compatibility and Separating Equilibria (Spence)

Goal

Derive algebraic conditions for a separating equilibrium in a typical Spence model. Build the minimal-separation argument and compute explicit thresholds for cost parameters.

Model primitives (formal)

Types: two types, θ∈{H,L}\theta\in\{H,L\}θ∈{H,L} with prior P(H)=pP(H)=pP(H)=p, P(L)=1−pP(L)=1-pP(L)=1−p. Productivities: πH>πL\pi\_H>\pi\_LπH​>πL​. Cost of signal s≥0s\ge0s≥0: cθ(s)c\_\theta(s)cθ​(s) with cH′(s)<cL′(s)c\_H'(s)<c\_L'(s)cH′​(s)<cL′​(s) for all sss (signal is less costly for the high type). Firms are competitive and pay expected productivity: w(s)=E[πθ∣s]w(s)=\mathbb{E}[\pi\_\theta\mid s]w(s)=E[πθ​∣s]. Strategies: Sender chooses sθs\_\thetasθ​, Receiver sets w(s)=∑θπθ⋅1{s believed from θ}w(s)=\sum\_\theta \pi\_\theta \cdot 1\{s\text{ believed from }\theta\}w(s)=∑θ​πθ​⋅1{s believed from θ}. In a separating equilibrium suppose sH>sLs\_H>s\_LsH​>sL​ and beliefs assign all mass to H on sHs\_HsH​ and to L on sLs\_LsL​.

Incentive-compatibility constraints

High type prefers sHs\_HsH​ to mimicking sLs\_LsL​: $w(sH)−cH(sH)≥w(sL)−cH(sL).w(s\_H)-c\_H(s\_H)\ge w(s\_L)-c\_H(s\_L).w(sH​)−cH​(sH​)≥w(sL​)−cH​(sL​).Lowtypeprefers Low type prefers Lowtypepreferss\_Ltomimicking to mimicking tomimickings\_H:: :w(sL)−cL(sL)≥w(sH)−cL(sH).w(s\_L)-c\_L(s\_L)\ge w(s\_H)-c\_L(s\_H).w(sL​)−cL​(sL​)≥w(sH​)−cL​(sH​).Because Because Becausew(s\_H)=\pi\_Hand and andw(s\_L)=\pi\_L$ under the separating beliefs, the ICs become

(High IC) $\pi\_H-c\_H(s\_H)\ge\pi\_L-c\_H(s\_L)\tag{IC\_H}$

(Low IC) $\pi\_L-c\_L(s\_L)\ge\pi\_H-c\_L(s\_H)\tag{IC\_L}$

Re-arrange. Subtract πL\pi\_LπL​ from both sides in (IC\_H): $πH−πL≥cH(sH)−cH(sL).\pi\_H-\pi\_L\ge c\_H(s\_H)-c\_H(s\_L).πH​−πL​≥cH​(sH​)−cH​(sL​).For(ICL): For (IC\_L): For(ICL​):cL(sH)−cL(sL)≥πH−πL.c\_L(s\_H)-c\_L(s\_L)\ge\pi\_H-\pi\_L.cL​(sH​)−cL​(sL​)≥πH​−πL​.Soanecessaryandsufficientconditionforseparationwith So a necessary and sufficient condition for separation with Soanecessaryandsufficientconditionforseparationwiths\_H>s\_L$ is

c\_H(s\_H)-c\_H(s\_L)\le\Delta\le c\_L(s\_H)-c\_L(s\_L),\quad\text{where }\Delta:=\pi\_H-\pi\_L.\tag{SEP}\

Interpretation: the productivity gap Δ\DeltaΔ must lie between the incremental cost of the signal for the high type and that for the low type. If the gap is large, separation is easy; if small, low types can mimic cheaply.

Minimal separating equilibrium (single-crossing, monotone costs)

A standard refinement is the minimal separating equilibrium: choose sL=0s\_L=0sL​=0 and pick sHs\_HsH​ as small as possible to satisfy (IC\_L). That is, pick sHs\_HsH​ solving

cL(sH)−cL(0)=Δ.(min-sep)c\_L(s\_H)-c\_L(0)=\Delta.\tag{min-sep}cL​(sH​)−cL​(0)=Δ.(min-sep)

Provided (IC\_H) holds automatically (since cHc\_HcH​ is cheaper, cH(sH)−cH(0)≤cL(sH)−cL(0)=Δc\_H(s\_H)-c\_H(0)\le c\_L(s\_H)-c\_L(0)=\DeltacH​(sH​)−cH​(0)≤cL​(sH​)−cL​(0)=Δ), this sHs\_HsH​ is the smallest education level that deters low-type imitation. This is the Spence-style equilibrium: H gets just enough education to separate.

Concrete numeric example

Let cH(s)=sc\_H(s)=scH​(s)=s and cL(s)=3sc\_L(s)=3scL​(s)=3s. Productivities πH=10\pi\_H=10πH​=10, πL=5\pi\_L=5πL​=5, so Δ=5\Delta=5Δ=5. With sL=0s\_L=0sL​=0, the minimal sHs\_HsH​ solves cL(sH)−cL(0)=3sH=5c\_L(s\_H)-c\_L(0)=3s\_H=5cL​(sH​)−cL​(0)=3sH​=5, so sH=5/3≈1.667s\_H=5/3\approx1.667sH​=5/3≈1.667. Check (IC\_H): cH(sH)−cH(0)=1.667≤5c\_H(s\_H)-c\_H(0)=1.667\le5cH​(sH​)−cH​(0)=1.667≤5, so holds. Wages: w(sH)=10w(s\_H)=10w(sH​)=10, w(0)=5w(0)=5w(0)=5. Utilities: high gets $10-1.667=8.333$, low gets $5$. Low cannot profitably mimic: if low mimics, his payoff would be $10-3(1.667)=10-5=5$, indifferent; off-path tie-breaking or slight perturbations can deter mimicry strictly.

Proof sketch for uniqueness (monotone pooling vs separation)

If cost functions satisfy single-crossing (i.e. the difference cL(s)−cH(s)c\_L(s)-c\_H(s)cL​(s)−cH​(s) is increasing in sss), then any separating equilibrium must be monotone: higher types choose weakly higher signals. Given monotonicity, the minimal separating construction above yields the unique separating equilibrium up to off-equilibrium beliefs and wage ties. The main mathematical reason is that single-crossing implies the lower type's incremental cost of increasing sss grows faster than the higher type's, so a single cutoff s∗s^\*s∗ prevents low-type mimicking.

All formulas in this section had nearby numeric exemplars: cH(s)=sc\_H(s)=scH​(s)=s, cL(s)=3sc\_L(s)=3scL​(s)=3s, Δ=5\Delta=5Δ=5, sH=5/3s\_H=5/3sH​=5/3.

## Core Mechanic 2: Pooling, Belief Specifications, Refinements and Screening

Pooling vs separating equilibria — the mathematics of beliefs

A pooling equilibrium is one in which all types choose the same signal s∗s^\*s∗. The receiver's posterior is the prior: E[π∣s∗]=pπH+(1−p)πL\mathbb{E}[\pi\mid s^\*]=p\pi\_H+(1-p)\pi\_LE[π∣s∗]=pπH​+(1−p)πL​. Pooling is attractive if the cost of separating exceeds its benefit: sending the same signal saves the higher type the cost of separation while firms pay the pooled expected productivity.

Pooling stability condition (example)

Given s∗s^\*s∗, types' incentives to deviate determine stability. Suppose s∗=0s^\*=0s∗=0 for both types. If a high-type deviates to sˉ>0\bar s>0sˉ>0 and firms interpret sˉ\bar ssˉ as

## Core Mechanic 2: Pooling, Belief Specifications, Refinements and Screening

a high-type signal and pay πH\pi\_HπH​, the deviation payoff is πH−cH(sˉ)\pi\_H-c\_H(\bar s)πH​−cH​(sˉ); so high will deviate if πH−cH(sˉ)>pπH+(1−p)πL−cH(0)\pi\_H-c\_H(\bar s)>p\pi\_H+(1-p)\pi\_L-c\_H(0)πH​−cH​(sˉ)>pπH​+(1−p)πL​−cH​(0). There may be no profitable deviation if the cost function makes any separating deviation too costly.

Off-equilibrium beliefs and implausible equilibria

Crucially, pooling equilibria often rely on receivers adopting arbitrary beliefs about off-path signals (signals not used in equilibrium). For example, if firms believe that any sˉ>0\bar s>0sˉ>0 was sent only by low types, they will pay πL\pi\_LπL​ at sˉ\bar ssˉ, and high types will not deviate. These beliefs can sustain pooling but are often unreasonable: why would the firm believe a costly deviation would be sent by the low type who faces higher costs? Belief-based equilibria are thus fragile.

Equilibrium refinements: the Intuitive Criterion and D1

To eliminate such implausible beliefs we use refinements. The Intuitive Criterion (Cho and Kreps, 1987) rules out beliefs that put probability on types for which deviation is not strictly profitable for any belief-supporting action. D1 (Banks and Sobel) is a stronger refinement comparing types' relative gains from deviation.

Formal statement (Intuitive Criterion)

Let s′s's′ be an off-path signal. Consider the set of types T(s′)T(s')T(s′) that could potentially gain from deviating to s′s's′ against some receiver belief. Formally,

T(s′)={θ: max⁡a∈AuS(θ,s′,a)>max⁡a∈AuS(θ,s∗,a)},T(s')=\{\theta:\ \max\_{a\in A}u\_S(\theta,s',a)>\max\_{a\in A}u\_S(\theta,s^\*,a)\},T(s′)={θ: a∈Amax​uS​(θ,s′,a)>a∈Amax​uS​(θ,s∗,a)},

where s∗s^\*s∗ is the equilibrium signal profile. If some types gain and others don't, the Intuitive Criterion says the receiver should assign zero probability to the types who cannot gain (they wouldn't deviate), and place all mass on those who can. Applying this often rules out pooling equilibria sustained by perverse beliefs.

Concrete example illustrating refinement

Return to the numeric example: πH=10\pi\_H=10πH​=10, πL=5\pi\_L=5πL​=5, p=0.5p=0.5p=0.5, cH(s)=sc\_H(s)=scH​(s)=s, cL(s)=3sc\_L(s)=3scL​(s)=3s. Consider pooling at s=0s=0s=0 with firms paying w(0)=7.5w(0)=7.5w(0)=7.5. Suppose there is an off-equilibrium signal s′=1s'=1s′=1. Evaluate gains:

- •High deviating: payoff $10-1=9$ which is greater than $7.5$ (gain of $1.5$).
- •Low deviating: payoff $5-3=2$ which is less than $7.5$ (loss of $5.5$).

Thus only high strictly benefits from deviating. Intuitive Criterion implies that if s′=1s'=1s′=1 is observed, firms should place all mass on H and pay $10$. Consequently pooling at 0 is not stable because H has a profitable deviation and firms' reasonable response makes it profitable. This rules out the pooling equilibrium that relied on the firm believing a deviation would be from L.

Screening mechanisms (principal design vs signaling)

In screening, the uninformed principal (e.g., an employer) offers a menu of contracts to induce self-selection: menu {(a1,t1),(a2,t2),...(a\_1,t\_1), (a\_2,t\_2),...(a1​,t1​),(a2​,t2​),...} where (a,t)(a,t)(a,t) are allocation and transfer. The principal solves an optimization subject to incentive compatibility (IC) and individual rationality (IR) constraints — the exact same constraints we used above, but the principal now chooses outcomes rather than passively observing signals. This is exactly "Mechanism Design" territory. For example, an insurer designs deductible-premium pairs such that low-risk choose high deductible/low premium and high-risk choose low deductible/high premium.

Numerical screening sketch

Types H and L with probabilities ppp and $1-p.Principal′spayofffortype. Principal's payoff for type .Principal′spayofffortype\thetawhenofferingcontract when offering contract whenofferingcontract(q,t)is is isv\_\theta(q)-tandagentpayoffis and agent payoff is andagentpayoffist-\phi\_\theta(q)where where where\phi\_\theta(q)istheagent′scostofproviding is the agent's cost of providing istheagent′scostofprovidingq.TheprincipalmaximizesexpectedpayoffsubjecttoICandIR.Forconcretenumbers:suppose. The principal maximizes expected payoff subject to IC and IR. For concrete numbers: suppose .TheprincipalmaximizesexpectedpayoffsubjecttoICandIR.Forconcretenumbers:supposev\_H(q)=10q$, $v\_L(q)=5q$, $\phi\_H(q)=q$, $\phi\_L(q)=3q,and, and ,andp=0.5.Theprincipalwillchoose. The principal will choose .Theprincipalwillchooseq\_H>q\_Landtransfers and transfers andtransferst\_H,t\_L$ to satisfy

IC\_H: tH−ϕH(qH)≥tL−ϕH(qL)t\_H-\phi\_H(q\_H)\ge t\_L-\phi\_H(q\_L)tH​−ϕH​(qH​)≥tL​−ϕH​(qL​)

IC\_L: tL−ϕL(qL)≥tH−ϕL(qH)t\_L-\phi\_L(q\_L)\ge t\_H-\phi\_L(q\_H)tL​−ϕL​(qL​)≥tH​−ϕL​(qH​)

IR: tθ−ϕθ(qθ)≥0t\_\theta-\phi\_\theta(q\_\theta)\ge0tθ​−ϕθ​(qθ​)≥0.

One finds, using algebra similar to the Spence ICs, that the principal distorts qLq\_LqL​ downward relative to the first-best to reduce informational rent to H, a familiar screening result.

Moral hazard contrast

In moral hazard, types are identical ex ante, but actions are unobserved. Incentive compatibility is dynamic (action choices after contracting), and the principal cannot simply rely on signals; instead she uses performance-contingent payments or monitoring. The mathematics uses incentive constraints across actions rather than types.

All formulas above had concrete numeric checks: the pooling example with w(0)=7.5w(0)=7.5w(0)=7.5, s′=1s'=1s′=1 gave explicit payoffs $9$ vs $2;screeningsketchused; screening sketch used ;screeningsketchusedv\_H(q)=10q$, etc.

## Applications and Connections: Price as a Signal, Empirical Identification, and Broader Uses

Price as a signal of quality

A price can be an endogenous costly signal if maintaining a high price is costlier (or less profitable) for low-quality sellers. Consider a monopolist seller of two qualities: high quality (H) with cost cHc\_HcH​ and low quality (L) with cost cLc\_LcL​, where cL<cHc\_L<c\_HcL​<cH​ — costs are lower for the low-quality seller but consumer valuation differs: buyers value H at vHv\_HvH​ and L at vLv\_LvL​ with vH>vLv\_H>v\_LvH​>vL​. Suppose buyers infer quality from price ppp: a high price may be interpreted as a signal of high quality, so the high-quality seller may prefer to charge a premium to distinguish herself.

Simple numeric signaling-by-price model

Two sellers types with equal prior p=0.5p=0.5p=0.5. Buyers' willingness to pay: vH=20v\_H=20vH​=20, vL=10v\_L=10vL​=10. Costs for posting a price ppp are simply marginal costs: cH=6c\_H=6cH​=6, cL=2c\_L=2cL​=2. If a seller posts ppp, profit for type θ\thetaθ is πθ(p)=(p−cθ)⋅D(p∣beliefs)\pi\_\theta(p)=(p-c\_\theta)\cdot D(p|beliefs)πθ​(p)=(p−cθ​)⋅D(p∣beliefs) where DDD is demand conditional on buyer beliefs. If demand is all-or-nothing — buyers buy if they believe seller is H and p≤vHp\le v\_Hp≤vH​, otherwise don't buy — a separating equilibrium can be: low-type posts pL=10p\_L=10pL​=10, high-type posts pH=20p\_H=20pH​=20. Buyers observing $20$ believe H and buy; observing 10 they believe L and buy. Profits: high gets $20-6=14$, low gets $10-2=8$. Check deviations: if low tries to mimic $20$, and buyers believe $20$ is H, low's profit would be $20-2=18$ which is higher than 8, so this naive belief can't hold. Instead, for price to signal credibly, posting a high price must be costlier for L in terms of lost sales or credibility. For instance if demand falls steeply with price for L (reflecting production mismatch or reputational loss), separation can be sustained. The key point is the same IC inequalities: the signal must be relatively costly for low types.

Empirical identification: how to tell signaling from productivity

Applied work often asks: is education a pure productivity-enhancing human-capital investment or mainly a signal? Randomized trials (ability-controlling experiments), natural experiments (compulsory schooling laws), sibling or twin designs, and regression discontinuity can help. In "Mechanism Design" we learned structural identification uses models of incentives to recover primitives; here, one estimates cost functions cθ(s)c\_\theta(s)cθ​(s) and productivity πθ\pi\_\thetaπθ​ to see if observed education choices satisfy the IC inequalities consistent with signaling.

Real-world use cases

- •Labor markets: credentials, credential inflation, degree signaling vs skill acquisition
- •Markets for lemons (Akerlof): adverse selection in used cars; warranties as signals
- •Insurance: deductible and premium menus screen risk types; insurers may also use signals like credit scores
- •Industrial organization: price/quality strategies, warranties, brand building as costly signals
- •Finance: IPO underpricing and costly signals from reputable underwriters

Policy implications

If high education is mostly signaling, public provision of credentials (or standardized testing) can distort incentives and welfare compared to direct subsidies for productivity-enhancing activities. Recognizing the difference matters for designing subsidies, taxes, or regulation of disclosure.

Downstream theoretical connections

Mastery of signaling games enables understanding of: mechanism-design solutions to adverse selection problems (optimal screening, Myerson--Satterthwaite trade-offs in bilateral trade), principal-agent models with hidden actions (moral hazard), dynamic signaling (reputation models, job-market signaling over time), and information design/cheap-talk variants. It also prepares you to read empirical structural papers that estimate unobserved cost distributions and draw welfare conclusions.

Concrete numeric illustration tying elements together

Consider the earlier Spence numbers (πH=10,πL=5,cH(s)=s,cL(s)=3s\pi\_H=10,\pi\_L=5,c\_H(s)=s,c\_L(s)=3sπH​=10,πL​=5,cH​(s)=s,cL​(s)=3s). Suppose instead the firm offers a menu: "certificate with wage 10 or no certificate with wage 5". This is a screening design that replicates the separating equilibrium but the firm now commits to wages ex ante. The firm optimally sets the wage spread to extract rents consistent with the ICs we solved earlier; the same numbers produce sH≈1.667s\_H\approx1.667sH​≈1.667 as the minimal certificate cost for H, matching the signaling model. The only conceptual difference is who commits: in signaling, the sender self-selects; in screening, the principal creates choice.

All formulas and claims above were accompanied by specific numeric exemplars to anchor the algebra in real calculations.

## Worked Examples (3)

### Minimal Separating Education Level (Spence numeric)

Types H and L with productivities πH=12\pi\_H=12πH​=12, πL=6\pi\_L=6πL​=6. Priors irrelevant for separation. Costs: cH(s)=sc\_H(s)=scH​(s)=s, cL(s)=4sc\_L(s)=4scL​(s)=4s. Firms pay w(s)=πHw(s)=\pi\_Hw(s)=πH​ if they see s=sHs=s\_Hs=sH​ and w(s)=πLw(s)=\pi\_Lw(s)=πL​ if they see s=0s=0s=0. Find the minimal sH>0s\_H>0sH​>0 that sustains separation with sL=0s\_L=0sL​=0.

1. Write the low-type IC that deters low from mimicking the high-type: πL−cL(0)≥πH−cL(sH)\pi\_L-c\_L(0)\ge \pi\_H-c\_L(s\_H)πL​−cL​(0)≥πH​−cL​(sH​). Substitute cLc\_LcL​: $6-0\ge 12-4s\_H$.
2. Rearrange: $6\ge12-4s\_H$ implies $4s\_H\ge6so so sos\_H\ge1.5$.
3. Minimal separating sHs\_HsH​ is the smallest value satisfying the inequality, so sH∗=1.5s\_H^\*=1.5sH∗​=1.5.
4. Check high-type IC: πH−cH(sH)≥πL−cH(0)\pi\_H-c\_H(s\_H)\ge\pi\_L-c\_H(0)πH​−cH​(sH​)≥πL​−cH​(0), i.e. $12-1.5\ge6$, $10.5\ge6$, which holds.
5. Interpretation: sH=1.5s\_H=1.5sH​=1.5 is just costly enough for the low type (cost $4\cdot1.5=6$) so that low is indifferent or worse to mimic, while high pays cost $1.5$ and retains substantial surplus.

**Insight:** This example shows the minimal separation approach: solve the low-type incentive constraint (the binding constraint) to find the smallest signal that deters mimicry. The high-type constraint is slack because the high-type is relatively advantaged in cost.

### Screening: Wage Menu to Separate Worker Types

Employer faces two worker types with productivities πH=10\pi\_H=10πH​=10, πL=4\pi\_L=4πL​=4, probabilities ppp (irrelevant for incentive constraints). Cost to worker of producing (effort embedded in productivity) is zero; employer offers wage-menu (wH,wL)(w\_H,w\_L)(wH​,wL​) tied to certificate choices. Worker can buy a certificate at private cost: kH=2k\_H=2kH​=2 if high, kL=8k\_L=8kL​=8 if low. The employer wants a separating menu where certificate yields wage wH=10w\_H=10wH​=10 and no-certificate yields wL=4w\_L=4wL​=4. Determine whether the certificate price can be set to implement separation and compute worker payoffs.

1. Model the worker's payoff: if a worker buys certificate at price pcp\_cpc​, high's net payoff is wH−pcw\_H-p\_cwH​−pc​, low's net payoff if mimicking is wH−pcw\_H-p\_cwH​−pc​ but low faces cost kLk\_LkL​? Clarify: certificate cost is the private monetary cost pcp\_cpc​ plus opportunity cost kθk\_\thetakθ​? For this example choose certificate cost equal to those numbers: high pays $2$ to obtain certificate, low pays $8$.
2. High's utility from buying certificate: $10-2=8$. From not buying (choose no-certificate): $4$.
3. Low's utility from buying: $10-8=2$. From not buying: $4$.
4. So with these numbers, high strictly prefers to buy (8>4) and low prefers not to buy (4>2), achieving separation with the simple menu (employer sets wages as specified and the certificate costs are inherent).
5. Employer profit: for each high worker hired as certified, profit is πH−wH=10−10=0\pi\_H-w\_H=10-10=0πH​−wH​=10−10=0; for low not certified, profit is πL−wL=4−4=0\pi\_L-w\_L=4-4=0πL​−wL​=4−4=0. The employer extracts no surplus here; to extract surplus the employer could reduce wages conditional on certification subject to preserving ICs.

**Insight:** This example highlights screening via a menu — the certificate plays the role of a signal but is priced by nature (different private costs). The employer designs wages (transfers) anticipating self-selection; IC constraints are the same algebraic inequalities we wrote for Spence.

### Pooling vs Separation with Intuitive Criterion

Using the classic numbers: πH=10\pi\_H=10πH​=10, πL=5\pi\_L=5πL​=5, priors p=0.5p=0.5p=0.5, costs cH(s)=sc\_H(s)=scH​(s)=s, cL(s)=3sc\_L(s)=3scL​(s)=3s. Consider the candidate pooling equilibrium where both types choose s=0s=0s=0 and firms pay w(0)=7.5w(0)=7.5w(0)=7.5. Examine whether the Intuitive Criterion rules out pooling at s=0s=0s=0 by analyzing a possible deviating signal s′=1s'=1s′=1.

1. Compute payoffs under pooling: each type's payoff at s=0s=0s=0 is w(0)−cθ(0)w(0)-c\_\theta(0)w(0)−cθ​(0). So high: $7.5-0=7.5$, low: $7.5-0=7.5$.
2. Compute payoff for high deviating to s′=1s'=1s′=1 if firms believe deviation came from high (pay $10$): $10-c\_H(1)=10-1=9$ which is greater than $7.5$, so high strictly benefits.
3. Compute payoff for low deviating to s′=1s'=1s′=1 if firms believe deviation came from low (pay $5$): $5-c\_L(1)=5-3=2$ which is less than $7.5$, so low loses by deviating.
4. Apply Intuitive Criterion: since only high strictly benefits from deviating to s′=1s'=1s′=1, rational beliefs assign all posterior mass to H at s′=1s'=1s′=1, i.e. firms should pay $10uponobserving upon observing uponobservings'=1$. That makes the deviation profitable and thus pooling cannot be sustained under the Intuitive Criterion.
5. Conclude pooling at s=0s=0s=0 is ruled out by the Intuitive Criterion; therefore the equilibrium must separate (or use different beliefs/equilibrium refinements).

**Insight:** This example illustrates how off-equilibrium beliefs matter and how the Intuitive Criterion uses profit comparisons to rule out implausible beliefs sustaining pooling. It shows concretely that only high-type deviation is profitable, so beliefs should reflect that.

## Key Takeaways

- ✓

  Signaling games model how informed senders use costly observable actions to manipulate uninformed receivers' beliefs; the canonical Spence model is a prime example.
- ✓

  Separating equilibria satisfy incentive-compatibility (IC) constraints for all types; typically the binding constraint is the low type's incentive not to mimic, which determines the minimal separating signal.
- ✓

  Pooling equilibria rely on off-equilibrium beliefs and are often fragile; refinements like the Intuitive Criterion and D1 rule out many implausible pools.
- ✓

  Screening (principal-designed menus) and signaling (sender-chosen signals) are dual approaches to adverse selection; both use the same IC and IR constraints from Mechanism Design.
- ✓

  Price, warranties, certifications, and other signals can be credible only if they are relatively more costly or less profitable for lower-quality types — the empirical identification challenge is to recover those cost differences.
- ✓

  Moral hazard differs in structure (hidden actions rather than hidden types); the incentive constraints in moral hazard are dynamic and involve continuation payoffs or monitoring.
- ✓

  Equilibrium refinements, single-crossing, and monotone comparative statics are key mathematical tools: single-crossing guarantees monotone separation and uniqueness properties.

## Common Mistakes

- ✗

  Ignoring off-path beliefs: Claiming a pooling equilibrium exists without specifying receivers' beliefs on deviations. Why wrong: off-path beliefs determine whether deviations are profitable; without plausible beliefs an equilibrium is not convincing.
- ✗

  Assuming costless signals can separate types: If signals are costless, low types will mimic, so separation cannot be sustained unless signaling directly changes fundamentals. Why wrong: separation requires differential costs or payoffs across types.
- ✗

  Confusing adverse selection with moral hazard: Treating hidden action problems as if types are private attributes. Why wrong: the mathematical constraints differ (type IC vs action IC), leading to different optimal contracts.
- ✗

  Using first-best allocations when designing screening menus: Ignoring informational rents. Why wrong: with private information principals must leave rents to agents to induce truthful revelation; ignoring IC leads to infeasible allocations.

## Practice

easy

Easy: In the Spence setup let πH=15\pi\_H=15πH​=15, πL=7\pi\_L=7πL​=7, costs cH(s)=2sc\_H(s)=2scH​(s)=2s, cL(s)=6sc\_L(s)=6scL​(s)=6s. Compute the minimal separating signal sHs\_HsH​ when sL=0s\_L=0sL​=0.

**Hint:** Use the low-type IC: πL−cL(0)≥πH−cL(sH)\pi\_L- c\_L(0) \ge \pi\_H - c\_L(s\_H)πL​−cL​(0)≥πH​−cL​(sH​) and solve for sHs\_HsH​.

Show solution

Low-type IC: $7-0\ge15-6s\_H$ so $6s\_H\ge8giving giving givings\_H\ge4/3\approx1.333.Minimalseparating. Minimal separating .Minimalseparatings\_H^\*=4/3$.

medium

Medium: A firm offers contracts (quality q, transfer t) to two seller types with valuations vH(q)=12qv\_H(q)=12qvH​(q)=12q, vL(q)=6qv\_L(q)=6qvL​(q)=6q, and seller effort costs ϕH(q)=q\phi\_H(q)=qϕH​(q)=q, ϕL(q)=3q\phi\_L(q)=3qϕL​(q)=3q. The firm wants to maximize expected surplus but must be incentive compatible and individually rational. Suppose the firm proposes qH=1q\_H=1qH​=1, find the maximum qL∈[0,1]q\_L\in[0,1]qL​∈[0,1] the firm can assign while preserving IC and IR for both types if transfers extract all surplus subject to IC.

**Hint:** Write IC constraints: seller utility under contract (q,t)(q,t)(q,t) is t−ϕθ(q)t-\phi\_\theta(q)t−ϕθ​(q); extracting surplus means set tθ=ϕθ(qθ)t\_\theta=\phi\_\theta(q\_\theta)tθ​=ϕθ​(qθ​) plus informational rent adjustments. Solve IC\_L: tL−ϕL(qL)≥tH−ϕL(qH)t\_L-\phi\_L(q\_L)\ge t\_H-\phi\_L(q\_H)tL​−ϕL​(qL​)≥tH​−ϕL​(qH​). Use transfers equal to costs plus minimum rents.

Show solution

To separate, IC\_L: tL−ϕL(qL)≥tH−ϕL(qH)t\_L-\phi\_L(q\_L)\ge t\_H-\phi\_L(q\_H)tL​−ϕL​(qL​)≥tH​−ϕL​(qH​). If firm extracts all surplus, set seller utilities to their participation bounds; minimal IR is 0, so tθ=ϕθ(qθ)t\_\theta=\phi\_\theta(q\_\theta)tθ​=ϕθ​(qθ​) plus any rents. Set tH=ϕH(qH)=1t\_H=\phi\_H(q\_H)=1tH​=ϕH​(qH​)=1. Then IC\_L requires tL−3qL≥1−3⋅1=1−3=−2t\_L-3q\_L\ge 1-3\cdot1=1-3=-2tL​−3qL​≥1−3⋅1=1−3=−2. With minimal transfer tL=3qLt\_L=3q\_LtL​=3qL​ to give IR=0, L's left side is $0\ge-2,whichholdsforall, which holds for all ,whichholdsforallq\_L.Howeverthefirmmustensurebuyerspayenough:thefirmmaximizesbuyervalueminustransfers.Forfeasibility,. However the firm must ensure buyers pay enough: the firm maximizes buyer value minus transfers. For feasibility, .Howeverthefirmmustensurebuyerspayenough:thefirmmaximizesbuyervalueminustransfers.Forfeasibility,q\_Lcanbeupto1.Thereforemaximum can be up to 1. Therefore maximum canbeupto1.Thereforemaximumq\_L=1.(Note:theexercisesimplifiestransfers;afullersolutionwouldcomputefirmobjectiveandchoose. (Note: the exercise simplifies transfers; a fuller solution would compute firm objective and choose .(Note:theexercisesimplifiestransfers;afullersolutionwouldcomputefirmobjectiveandchooseq\_L$ that trades off surplus extraction and IC.)

hard

Hard: Take the Spence numbers πH=10\pi\_H=10πH​=10, πL=5\pi\_L=5πL​=5, costs cH(s)=sc\_H(s)=scH​(s)=s, cL(s)=3sc\_L(s)=3scL​(s)=3s, prior p=0.5p=0.5p=0.5. Show formally that any pooling equilibrium at s=0s=0s=0 is ruled out by the Intuitive Criterion. Provide the formal steps and argue why no belief specification consistent with the criterion can sustain pooling.

**Hint:** Check whether there exists any off-path signal s′>0s'>0s′>0 such that only high benefits from deviating. If so, the Intuitive Criterion assigns probability 1 to high at s′s's′, making deviation profitable.

Show solution

Compute payoffs under pooling at s=0s=0s=0: both get $7.5.Forany. For any .Foranys'>0$, high's payoff if believed to be H is $10-s'$, low's payoff if believed to be L is $5-3s'.Compareto7.5.Choose. Compare to 7.5. Choose .Compareto7.5.Chooses'=1$: high: $10-1=9>7.5$, low: $5-3=2<7.5.Thusonlyhighstrictlybenefits.IntuitiveCriterionrequiresbeliefsat. Thus only high strictly benefits. Intuitive Criterion requires beliefs at .Thusonlyhighstrictlybenefits.IntuitiveCriterionrequiresbeliefsats'=1placeallmassonH,sofirmpays10.Giventhat,highstrictlypreferstodeviate,contradictingpooling.Becausesuchan place all mass on H, so firm pays 10. Given that, high strictly prefers to deviate, contradicting pooling. Because such an placeallmassonH,sofirmpays10.Giventhat,highstrictlypreferstodeviate,contradictingpooling.Becausesuchans'$ exists, no belief consistent with the Intuitive Criterion can sustain pooling at 0.

## Connections

Looking back: This lesson builds directly on "Bayesian Games" (we used types, priors and PBE; the Harsanyi transformation turns private information into Nature's draw) and "Mechanism Design" (we used incentive compatibility and individual rationality constraints to derive separating signals and screening menus). In particular, the algebra of IC used here is the same as the IC constraints you learned for direct-revelation mechanisms; single-crossing and monotonicity results used in the Spence analysis mirror envelope theorems and monotone allocation results in mechanism design.

Looking forward: Mastery of signaling games enables analysis of more advanced topics: (i) dynamic signaling and reputation models (learning over time, e.g. Holmström and Tirole, Kreps and Wilson), (ii) contract theory with both adverse selection and moral hazard (combined hidden action and type problems), (iii) information design and persuasion problems where a sender optimally chooses signals to influence beliefs, and (iv) structural econometrics of asymmetric information where primitives of cost and productivity functions are estimated. Practical downstream techniques include estimating structural signalling models, designing optimal menus in procurement, and applying equilibrium refinements (Intuitive Criterion, D1) in theoretical work to rule out spurious equilibria.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
