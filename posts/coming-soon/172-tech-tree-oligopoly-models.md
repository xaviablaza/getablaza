---
title: Oligopoly Models
description: Cournot quantity competition, Bertrand price competition, Stackelberg leader-follower. Market structure effects on equilibrium prices and quantities.
date: '2026-07-01'
scheduled: '2026-12-19'
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
inspiration_url: https://templeton.host/tech-tree/oligopoly-models/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/oligopoly-models/](https://templeton.host/tech-tree/oligopoly-models/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Oligopoly Models

Game TheoryDifficulty: ★★★★☆Depth: 10Unlocks: 1

Cournot quantity competition, Bertrand price competition, Stackelberg leader-follower. Market structure effects on equilibrium prices and quantities.

## Prerequisites (2)

[Nash Equilibrium5 atoms](/tech-tree/nash-equilibrium/)[Profit Maximization? atoms](/tech-tree/profit-maximization/)

## Unlocks (1)

[Competitive Pricinglvl 5](/tech-tree/competitive-pricing/)

## Referenced by (3)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (3)

[Market ShareBusiness

Cournot quantity competition and Bertrand price competition directly model how firms compete for market share; equilibrium share outcomes depend on whether rivals compete on price vs quantity, which determines whether low tolerance for share loss leads to aggressive pricing or capacity investment](/business/market-share/)[equilibriumBusiness

Cournot and Bertrand are the canonical equilibrium models for pricing and quantity competition. Understanding these specific models clarifies exactly what class of model is being excluded when bids are not equilibrium-derived.](/business/equilibrium/)[OperatorBusiness

Multi-brand portfolios compete in oligopolistic markets. Cournot/Bertrand/Stackelberg dynamics govern how portfolio brands interact with competitors and sometimes with each other.](/business/operator/)

Advanced Learning Details

### Graph Position

100

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

10

Chain Length

Why do two gasoline stations on the same street often charge nearly the same price, while one dominant firm can keep prices high? Oligopoly models explain how strategic interactions among a few firms determine prices, quantities, and profits.

TL;DR:

Oligopoly models (Cournot, Bertrand, Stackelberg) formalize strategic quantity and price competition among a few firms and deliver concrete comparative statics: how equilibrium prices and outputs depend on market structure and timing.

## What Is Oligopoly Models?

# What Is Oligopoly Models?

An oligopoly is a market structure with a small number of firms whose strategic choices (price or quantity) materially affect market outcomes. Oligopoly models formalize these strategic interactions and produce equilibrium predictions about prices, quantities, and profits. They lie at the intersection of microeconomics (profit maximization, marginal analysis) and game theory (Nash equilibrium, strategic reasoning).

Why care? Because many important industries are oligopolistic: airlines, telecommunications, energy generation, and some retail markets. Correctly predicting outcomes in these markets requires reasoning about how rival firms anticipate and react to each other's decisions.

Core intuition, stated upfront:

- •Cournot (quantity competition): Firms simultaneously choose outputs; the strategic variable is quantity. Each firm takes rivals' quantities as given and sets its own output. The equilibrium is a Nash equilibrium in quantities.
- •Bertrand (price competition): Firms simultaneously set prices for homogeneous goods. With constant marginal costs and no capacity constraints, the Bertrand outcome drives price to marginal cost (the Bertrand paradox).
- •Stackelberg (leader-follower): One firm commits to a quantity first (leader); the other firm(s) observe and then choose quantities (followers). The leader obtains a first-mover advantage.

These models are not just alternative formulations; they produce different equilibria and policy implications. To make their predictions precise we rely on two prerequisites:

- •In Nash Equilibrium, we solved for strategy profiles with no profitable unilateral deviation. Here, each firm's strategy is a price or quantity and the equilibrium is a profile of such choices.
- •In Profit Maximization, we use marginal revenue = marginal cost (MR = MC) first-order conditions to find best-responses (and check second-order conditions).

A standard common benchmark demand specification is linear inverse demand

P=a−bQ,a>c,  b>0,P = a - bQ,\qquad a>c,\; b>0,P=a−bQ,a>c,b>0,

where QQQ is total market output, PPP price, and ccc constant marginal cost. A concrete numeric example: take a=100a=100a=100, b=1b=1b=1, c=20c=20c=20. Then P=100−QP=100-QP=100−Q and marginal cost is $20.Iftotaloutputis. If total output is .IftotaloutputisQ=50,then, then ,thenP=100-50=50$ and per-unit margin is $30$.

Every equilibrium concept we use will be constructed as a Nash equilibrium in a game whose strategy sets and timing differ. For Cournot and Bertrand these are simultaneous-move games; Stackelberg is sequential and solved by backward induction (subgame-perfect Nash equilibrium).

Comparative statics and ordering: A key take-away you will see proven below is a typical ordering of market outcomes (for standard linear costs/demand and homogeneous product):

- •Monopoly: highest price, smallest total output.
- •Cournot (duopoly): intermediate price and output.
- •Stackelberg (leader-follower): lower price and higher total output than Cournot; leader enjoys higher profit.
- •Bertrand (homogeneous goods, unconstrained capacity): price equals marginal cost ccc (lowest price), output is largest.

All three models provide different lenses for regulator and manager decisions: antitrust enforcement, entry deterrence, capacity planning, and pricing strategy. In the next sections we'll derive closed-form formulas, compute numeric examples, and expose the mechanisms behind these orderings.

## Core Mechanic 1: Cournot Quantity Competition

# Core Mechanic 1: Cournot Quantity Competition

Cournot models assume firms choose quantities simultaneously and each firm's payoff depends on market price determined by aggregate quantity. Formally, for a duopoly (firms 1 and 2) with inverse demand P=a−bQP=a-bQP=a−bQ and constant marginal cost ccc, firm iii's profit is

πi(qi,qj)=(P−c)qi=(a−b(qi+qj)−c)qi.\pi\_i(q\_i,q\_j) = (P-c)q\_i = \big(a - b(q\_i+q\_j) - c\big)q\_i.πi​(qi​,qj​)=(P−c)qi​=(a−b(qi​+qj​)−c)qi​.

Reference to prerequisites: In Nash Equilibrium, we require that each qiq\_iqi​ is a best response to qjq\_jqj​. In Profit Maximization we apply MR = MC (first-order condition) to get that best response.

Derivation of best-response (duopoly). The firm maximizes πi(qi,qj)\pi\_i(q\_i,q\_j)πi​(qi​,qj​) w.r.t. qiq\_iqi​. Compute the first-order condition (FOC):

∂πi∂qi=a−b(qi+qj)−c−bqi=0.\frac{\partial\pi\_i}{\partial q\_i} = a - b(q\_i+q\_j) - c - b q\_i = 0.∂qi​∂πi​​=a−b(qi​+qj​)−c−bqi​=0.

Collect terms to isolate qiq\_iqi​:

a−c−2bqi−bqj=0⇒qi=a−c−bqj2b.a - c - 2b q\_i - b q\_j = 0 \quad\Rightarrow\quad q\_i = \frac{a-c - b q\_j}{2b}.a−c−2bqi​−bqj​=0⇒qi​=2ba−c−bqj​​.

This is firm iii's reaction (best-response) function:

BRi(qj)=a−c2b−12qj.BR\_i(q\_j) = \frac{a-c}{2b} - \frac{1}{2}q\_j.BRi​(qj​)=2ba−c​−21​qj​.

Numeric example near the formula: with a=100a=100a=100, b=1b=1b=1, c=20c=20c=20, we get

BRi(qj)=100−202⋅1−12qj=40−0.5qj.BR\_i(q\_j) = \frac{100-20}{2\cdot1} - \frac{1}{2}q\_j = 40 - 0.5 q\_j.BRi​(qj​)=2⋅1100−20​−21​qj​=40−0.5qj​.

Interpretation: the more the rival produces, the less you produce; slope −1/2-1/2−1/2.

Solve for symmetric Nash equilibrium (set q1=q2=q∗q\_1=q\_2=q^\*q1​=q2​=q∗). Then

q∗=a−c−bq∗2b  ⇒  2bq∗=a−c−bq∗  ⇒  3bq∗=a−c.q^\* = \frac{a-c - b q^\*}{2b} \;\Rightarrow\; 2b q^\* = a-c - b q^\* \;\Rightarrow\; 3b q^\* = a-c.q∗=2ba−c−bq∗​⇒2bq∗=a−c−bq∗⇒3bq∗=a−c.

So

q∗=a−c3b.q^\* = \frac{a-c}{3b}.q∗=3ba−c​.

Numeric substitution: with a−c=80a-c=80a−c=80, b=1b=1b=1, q∗=80/3≈26.667q^\* = 80/3 \approx 26.667q∗=80/3≈26.667 per firm. Total output QC=2q∗=53.333Q^C = 2q^\* = 53.333QC=2q∗=53.333, price PC=a−bQC=100−53.333=46.667P^C = a - b Q^C = 100 - 53.333 = 46.667PC=a−bQC=100−53.333=46.667. Each firm's profit

πiC=(PC−c)q∗=(46.667−20)×26.667≈711.11.\pi\_i^C = (P^C - c) q^\* = (46.667 - 20)\times 26.667 \approx 711.11.πiC​=(PC−c)q∗=(46.667−20)×26.667≈711.11.

Generalization to nnn identical firms: each firm's symmetric Cournot output is

qi(n)=a−cb(n+1),q\_i^{(n)} = \frac{a-c}{b(n+1)},qi(n)​=b(n+1)a−c​,

so total output is

Q(n)=n(a−c)b(n+1).Q^{(n)} = \frac{n(a-c)}{b(n+1)}.Q(n)=b(n+1)n(a−c)​.

Numeric check: with n=2n=2n=2, qi=(100−20)/(1⋅3)=26.667q\_i=(100-20)/(1\cdot3)=26.667qi​=(100−20)/(1⋅3)=26.667 recovers the duopoly.

Limit as n→∞n\to\inftyn→∞: Q(n)→a−cbQ^{(n)} \to \frac{a-c}{b}Q(n)→ba−c​ and price P→cP\to cP→c. That is, Cournot competition converges to the competitive outcome (price equals marginal cost) as the number of firms grows.

Graphical intuition: plot the two best-response lines in (q1,q2)(q\_1,q\_2)(q1​,q2​) space. Each is downward sloping with slope −1/2-1/2−1/2; the intersection is the Nash equilibrium. As nnn increases, each firm's reaction becomes flatter (less influence of a single firm), pushing equilibrium output higher.

Second-order condition check: ensure profit is concave in qiq\_iqi​. Compute second derivative

∂2πi∂qi2=−2b<0,\frac{\partial^2 \pi\_i}{\partial q\_i^2} = -2b < 0,∂qi2​∂2πi​​=−2b<0,

so the FOC gives a maximum (this uses the Profit Maximization prerequisite).

Comparative statics: if marginal cost ccc increases, each firm's output drops linearly: ∂q∗/∂c=−1/(3b)\partial q^\*/\partial c = -1/(3b)∂q∗/∂c=−1/(3b) for n=2n=2n=2; price increases. If firms differ in marginal cost, the lower-cost firm produces more; closed-form asymmetric solutions exist but require solving linear system of first-order conditions.

Takeaway: Cournot equilibrium is an application of Nash Equilibrium plus Profit Maximization MR=MC, with closed-form solutions under linear demand. It yields intermediate prices between monopoly and perfect competition.

## Core Mechanic 2: Bertrand Price Competition and Stackelberg Leader-Follower

# Core Mechanic 2: Bertrand Price Competition and Stackelberg Leader-Follower

This section contrasts price competition (Bertrand) with sequential quantity competition (Stackelberg). Both highlight how the strategic variable (price vs quantity) and timing (simultaneous vs sequential) change equilibria.

Bertrand (homogeneous goods, unconstrained capacity):

Assume two firms set prices p1,p2p\_1,p\_2p1​,p2​ simultaneously for an identical product and face the market demand function D(p)D(p)D(p) (a decreasing function). Each firm supplies the entire demand if it posts the lowest price; if prices are equal, they split demand. With constant marginal cost ccc and unlimited capacity, the classical Bertrand argument shows the unique Nash equilibrium is p1=p2=cp\_1=p\_2=cp1​=p2​=c.

Reason (sketch): If a firm sets pj>cp\_j>cpj​>c, its rival can slightly undercut by setting pi=pj−εp\_i=p\_j-\varepsilonpi​=pj​−ε (for tiny ε>0\varepsilon>0ε>0) and capture nearly the entire demand at a price strictly above cost, securing positive profit — thus any pj>cp\_j>cpj​>c is not a best response. If one firm sets p=cp=cp=c, the other cannot profitably set any p′<cp'<cp′<c (loss) and any p′>cp'>cp′>c is undercuttable. So p1=p2=cp\_1=p\_2=cp1​=p2​=c is an equilibrium.

Concrete numeric example: demand D(p)=100−pD(p)=100 - pD(p)=100−p (A=100,B=1A=100,B=1A=100,B=1) and c=20c=20c=20. If both set p=20p=20p=20, each gets half the demand D(20)=80D(20)=80D(20)=80, so quantity each =40=40=40 and profit per firm is (20−20)×40=0(20-20)\times 40=0(20−20)×40=0. Any p>20p>20p>20 invites undercutting and positive profit, any p<20p<20p<20 yields losses. Thus equilibrium price pB=20p^B=20pB=20.

This is the Bertrand paradox: with only two firms and no capacity constraints or product differentiation, price equals marginal cost — the competitive outcome. To get prices above ccc, one needs capacity constraints, product differentiation, dynamic considerations, or incomplete information.

Stackelberg (sequential quantities):

Stackelberg duopoly: firm 1 (leader) chooses output q1q\_1q1​ first; firm 2 (follower) observes q1q\_1q1​ and chooses q2q\_2q2​. The game is solved by backward induction. Use the same linear inverse demand P=a−b(q1+q2)P=a-b(q\_1+q\_2)P=a−b(q1​+q2​) and marginal cost ccc.

Step 1 (follower's best response): As in Cournot, firm 2's best response to q1q\_1q1​ is

q2(q1)=a−c−bq12b=a−c2b−12q1.q\_2(q\_1) = \frac{a-c - b q\_1}{2b} = \frac{a-c}{2b} - \frac{1}{2} q\_1.q2​(q1​)=2ba−c−bq1​​=2ba−c​−21​q1​.

Numeric example: with a=100a=100a=100, b=1b=1b=1, c=20c=20c=20, we get q2(q1)=40−0.5q1q\_2(q\_1)=40 - 0.5 q\_1q2​(q1​)=40−0.5q1​.

Step 2 (leader anticipates this reaction): firm 1 chooses q1q\_1q1​ to maximize

π1(q1)=(a−b(q1+q2(q1))−c)q1.\pi\_1(q\_1) = \big(a - b(q\_1 + q\_2(q\_1)) - c\big) q\_1.π1​(q1​)=(a−b(q1​+q2​(q1​))−c)q1​.

Substitute q2(q1)q\_2(q\_1)q2​(q1​):

Total output Q=q1+q2=q1+a−c2b−12q1=12q1+a−c2b.Q = q\_1 + q\_2 = q\_1 + \frac{a-c}{2b} - \frac{1}{2} q\_1 = \frac{1}{2} q\_1 + \frac{a-c}{2b}.Q=q1​+q2​=q1​+2ba−c​−21​q1​=21​q1​+2ba−c​.

So

P=a−bQ=a−b(12q1+a−c2b)=a+c2−b2q1.P = a - bQ = a - b\Big(\frac{1}{2} q\_1 + \frac{a-c}{2b}\Big) = \frac{a+c}{2} - \frac{b}{2} q\_1.P=a−bQ=a−b(21​q1​+2ba−c​)=2a+c​−2b​q1​.

Leader's profit:

π1(q1)=(P−c)q1=(a−c2−b2q1)q1.\pi\_1(q\_1) = (P-c)q\_1 = \Big(\frac{a-c}{2} - \frac{b}{2} q\_1\Big) q\_1.π1​(q1​)=(P−c)q1​=(2a−c​−2b​q1​)q1​.

FOC (maximize w.r.t. q1q\_1q1​):

dπ1dq1=a−c2−bq1=0⇒q1∗=a−c2b.\frac{d\pi\_1}{dq\_1} = \frac{a-c}{2} - b q\_1 = 0 \quad\Rightarrow\quad q\_1^\* = \frac{a-c}{2b}.dq1​dπ1​​=2a−c​−bq1​=0⇒q1∗​=2ba−c​.

Numeric substitution: with a−c=80,b=1a-c=80, b=1a−c=80,b=1, we get q1∗=40q\_1^\* = 40q1∗​=40.

Follower's output at equilibrium:

q2∗=a−c2b−12q1∗=a−c4b.q\_2^\* = \frac{a-c}{2b} - \frac{1}{2} q\_1^\* = \frac{a-c}{4b}.q2∗​=2ba−c​−21​q1∗​=4ba−c​.

Numeric: q2∗=20q\_2^\* = 20q2∗​=20. Total output QS=60Q^S = 60QS=60, price PS=a−bQS=100−60=40P^S = a - bQ^S = 100 - 60 = 40PS=a−bQS=100−60=40. Profits: leader π1S=(40−20)×40=800\pi\_1^S = (40-20)\times 40 = 800π1S​=(40−20)×40=800; follower π2S=(40−20)×20=400\pi\_2^S = (40-20)\times 20 = 400π2S​=(40−20)×20=400.

Compare Cournot and Stackelberg (numbers):

- •Cournot: total QC=53.333Q^C=53.333QC=53.333, price PC=46.667P^C=46.667PC=46.667, each profit ≈711.11\approx711.11≈711.11.
- •Stackelberg: total QS=60Q^S=60QS=60, price PS=40P^S=40PS=40, leader profit $800$, follower profit $400$.

Observations and intuition:

- •The leader produces more than a single Cournot firm ((a−c)/(2b)(a-c)/(2b)(a−c)/(2b) vs (a−c)/(3b)(a-c)/(3b)(a−c)/(3b)) and captures a larger share; this is the first-mover advantage.
- •Total output under Stackelberg is higher and price lower than under Cournot—competition intensifies because the follower reacts to the leader's commitment
- •The leader's choice is equivalent to committing to a production level that incentivizes the follower to adopt a less aggressive response than if both moved simultaneously.

Ordering of outcomes (standard linear model):

PMonopoly>PCournot>PStackelberg>PBertrand=c.P\_{Monopoly} > P\_{Cournot} > P\_{Stackelberg} > P\_{Bertrand}=c.PMonopoly​>PCournot​>PStackelberg​>PBertrand​=c.

Monopoly price: solving the monopoly problem for linear demand gives total monopoly output QM=(a−c)/(2b)Q^M = (a-c)/(2b)QM=(a−c)/(2b) and price PM=(a+c)/2P^M = (a+c)/2PM=(a+c)/2. Numeric check: QM=40Q^M=40QM=40, PM=(100+20)/2=60P^M=(100+20)/2=60PM=(100+20)/2=60.

Bertrand with product differentiation or capacity constraints modifies the paradox: if capacity is limited, Bertrand need not drive price to marginal cost; with differentiated products, firms enjoy some price-setting power and equilibrium prices exceed ccc.

Technical note: Stackelberg equilibrium is a subgame-perfect Nash equilibrium: we used backward induction (solve follower's subgame then leader's problem). This leverages the sequential structure beyond static Nash.

## Applications and Connections

# Applications and Connections

Oligopoly models are central to applied industrial organization, antitrust analysis, and competitive strategy. They connect to regulatory policy, firm behavior, and dynamic strategic considerations.

1) Antitrust and merger analysis

Regulators use oligopoly models to assess how mergers affect prices and welfare. The Cournot model is often used as a benchmark: a merger that reduces the number of Cournot firms increases equilibrium price because each remaining firm's market power rises. For example, with linear demand a=100,b=1,c=20a=100,b=1,c=20a=100,b=1,c=20, reducing duopoly (n=2n=2n=2) to monopoly (n=1n=1n=1) moves total output from $53.333$ to $40$, raising price from $46.667$ to $60$ — a significant consumer harm. Practitioners estimate demand elasticities and marginal costs and compute counterfactual equilibrium outcomes.

2) Capacity planning and supply chains

If firms face capacity constraints, Bertrand competition may not deliver prices equal to marginal cost. Edgeworth cycles (no pure-strategy equilibrium) and mixed-strategy equilibria can arise. For example, if capacity is constrained so a firm cannot serve entire demand when undercutting, the incentive to undercut is limited and equilibrium prices can be above marginal cost.

3) Product differentiation and spatial competition

Differentiated-products models (Hotelling, Salop) convert price competition into outcomes where firms enjoy local market power; prices exceed marginal cost. These extensions bridge Bertrand and Cournot logic: as product differentiation increases, price outcomes move away from the Bertrand benchmark and resemble Cournot-like markup behavior.

4) Dynamic oligopoly, collusion, and repeated games

Repeated interaction allows firms to sustain collusive prices above the one-shot Nash outcomes. Using trigger strategies or Folk Theorem logic, oligopolists can sustain cooperative pricing if future punishment is credible. This requires understanding subgame-perfect equilibria in repeated games—a direct connection to the Nash Equilibrium prerequisite and to dynamic game theory.

5) Entry deterrence and limit pricing

A Stackelberg leader may choose a commitment (capacity or output) to deter entry. Limit pricing arguments model incumbent firms choosing prices or capacities to make entry unappealing. These incorporate strategic commitment and backward induction reasoning similar to Stackelberg analysis.

6) Empirical estimation and structural IO

Structural econometrics uses oligopoly models to estimate demand and cost parameters from observed prices and quantities, then simulates counterfactuals (e.g., the price after a merger). Cournot, Bertrand, and differentiated-product Bertrand models are common structural specifications.

Connections to prerequisites (looking back):

- •In Nash Equilibrium, we studied best-responses and fixed points; Cournot and Bertrand equilibria are explicit applications where each firm's strategy must be a best response.
- •From Profit Maximization, we used MR=MC and second-order conditions to derive best responses and ensure interior maxima.

What this enables (looking forward):

- •Dynamic oligopoly and repeated games: sustaining collusion, trigger strategies, and subgame-perfect equilibrium refinement.
- •Entry/exit models and real options: how firms invest and commit capacity over time.
- •Industrial organization empirical work: using structural models to quantify market power and policy effects.

Practical note for model selection: pick Cournot when firms compete on capacity/quantity (e.g., commodity producers), Bertrand for price-setting (retail), Stackelberg when leadership/commitment or sequential moves matter (a dominant firm sets capacity before smaller rivals). Always test sensitivity: small modeling choices (timing, capacity, product differentiation) materially affect policy-relevant predictions.

In the exercises and worked examples that follow we will compute numerical equilibria for these models, cementing the algebraic derivations above and making clear the economic intuition behind comparative static results.

## Worked Examples (3)

### Cournot duopoly with linear demand

Two identical firms face inverse demand P = 100 - Q (so a=100, b=1). Marginal cost c = 20. Firms choose quantities q1 and q2 simultaneously. Find the Cournot Nash equilibrium quantities, price, and profits.

1. Write each firm's profit: π\_i = (P - c) q\_i = (100 - (q1+q2) - 20) q\_i = (80 - q1 - q2) q\_i.
2. Compute firm 1's FOC treating q2 as given: ∂π1/∂q1 = 80 - 2 q1 - q2 = 0 → best response q1 = (80 - q2)/2 = 40 - 0.5 q2.
3. By symmetry, firm 2's best response is q2 = 40 - 0.5 q1.
4. Solve the two equations simultaneously by setting q1 = q2 = q*: q* = 40 - 0.5 q *→ 1.5 q* = 40 → q\* = 40 / 1.5 = 26.666....
5. Compute totals: total output Q = 2 × 26.666... = 53.333..., price P = 100 - 53.333... = 46.666..., and profit per firm π = (46.666... - 20) × 26.666... = 26.666... × 26.666... = 711.111... (approx).

**Insight:** This example shows how Cournot best-response functions intersect to yield the Nash equilibrium. The numeric values demonstrate that the Cournot price lies between monopoly and marginal-cost levels.

### Bertrand with constant marginal cost

Two firms set prices simultaneously for a homogeneous good. Market demand is D(p) = 100 - p and marginal cost c = 20. Firms have unlimited capacity. Find the Nash equilibrium prices and profits.

1. Consider if a firm sets price p > 20. The rival can set p' = p - ε for tiny ε>0 to capture nearly all demand at p' > 20 and earn positive profit. Hence p > 20 cannot be an equilibrium price.
2. Consider if a firm sets p < 20. That firm makes negative profit on each unit sold (p < c) and could raise price to 20 to improve profit. Hence p < 20 is not equilibrium.
3. Thus any equilibrium must have p\_i ≥ 20 and cannot have p\_i > 20 because of undercutting. Therefore candidate equilibrium is p1 = p2 = 20.
4. Check: at p1 = p2 = 20, demand D(20) = 80, the firms split demand (40 each) and earn profit (20 - 20) × 40 = 0. No unilateral deviation increases profit: lowering price loses money, raising price is undercut by rival.
5. Conclusion: unique Nash equilibrium in pure strategies is p1 = p2 = c = 20, with zero profits.

**Insight:** This demonstrates the Bertrand paradox: price competition with homogeneous goods and unlimited capacity drives price to marginal cost, generating no economic profit despite only two firms.

### Stackelberg leader-follower duopoly

Same demand/cost as above: P = 100 - Q, c = 20. Firm 1 (leader) chooses q1 first; firm 2 observes q1 and chooses q2. Find the Stackelberg subgame-perfect equilibrium quantities, price, and profits.

1. Follower's best response (as in Cournot): q2(q1) = (a - c - b q1)/(2b) = (100 - 20 - 1×q1)/2 = (80 - q1)/2 = 40 - 0.5 q1.
2. Leader anticipates q2(q1) and maximizes π1(q1) = (P - c) q1 with P = 100 - (q1 + q2(q1)). Compute total Q = q1 + q2 = q1 + 40 - 0.5 q1 = 0.5 q1 + 40.
3. Compute P = 100 - Q = 100 - (0.5 q1 + 40) = 60 - 0.5 q1. Then leader's profit π1(q1) = (P - c) q1 = (60 - 0.5 q1 - 20) q1 = (40 - 0.5 q1) q1.
4. FOC: dπ1/dq1 = 40 - q1 = 0 → q1\* = 40. (Second-order derivative negative ensures a maximum.)
5. Compute follower's choice q2 *= 40 - 0.5 q1* = 40 - 0.5×40 = 20. Totals: Q = 60, P = 100 - 60 = 40. Profits: leader π1 = (40 - 20)×40 = 800, follower π2 = (40 - 20)×20 = 400.

**Insight:** This worked example reveals the leader's advantage: the leader produces more than in Cournot and earns higher profit, while total output is higher and price lower than Cournot.

## Key Takeaways

- ✓

  Cournot competition: firms choose quantities simultaneously; best-response functions yield closed-form symmetric equilibrium q\_i = (a-c)/(b(n+1)).
- ✓

  Bertrand competition with homogeneous products and unconstrained capacity leads to p = c (the Bertrand paradox); small modeling changes like capacity or differentiation restore positive markups.
- ✓

  Stackelberg leader-follower: the leader, by committing to output, obtains a first-mover advantage; leader's output equals the monopoly output in the linear example, while total output exceeds Cournot's.
- ✓

  Order of market outcomes (standard linear case): Monopoly price > Cournot price > Stackelberg price > Bertrand price (= c).
- ✓

  These models are concrete applications of Nash Equilibrium and Profit Maximization (MR = MC); Stackelberg additionally uses backward induction to find a subgame-perfect equilibrium.
- ✓

  As the number of Cournot firms increases (n→∞), price converges to marginal cost c — Cournot approximates perfect competition with many firms.
- ✓

  Choice of model matters for policy: antitrust, merger simulation, and capacity decisions require selecting the strategic variable and timing that best represents the industry.

## Common Mistakes

- ✗

  Confusing the strategic variable: Treating Cournot and Bertrand as interchangeable. They are not — choosing price vs quantity yields different equilibria (e.g., Bertrand yields p=c under standard assumptions).
- ✗

  Forgetting second-order conditions: Solving first-order conditions without checking concavity can lead to maxima that are actually minima or saddle points. For linear demand with constant marginal cost, second derivatives are negative (safe), but check generally.
- ✗

  Applying Bertrand logic with capacity constraints: Using the benchmark p=c even when capacity is limited is wrong — capacity constrains undercutting and can raise equilibrium prices.
- ✗

  Mixing timing: Using Cournot formulas for Stackelberg outcomes (or vice versa). Stackelberg requires anticipating followers' responses (backward induction) rather than simultaneous best-response intersection.

## Practice

easy

Easy: Compute the symmetric Cournot equilibrium for n = 3 identical firms with linear inverse demand P = 120 - 2Q and marginal cost c = 30. Give each firm's quantity, total output, price, and profit per firm.

**Hint:** Use the n-firm Cournot formula q\_i = (a - c)/(b (n+1)). Here a=120, b=2.

Show solution

Given a=120, b=2, c=30: a-c = 90. Each firm's quantity q\_i = 90/(2*(3+1)) = 90/8 = 11.25. Total output Q = 3*11.25 = 33.75. Price P = 120 - 2*33.75 = 120 - 67.5 = 52.5. Profit per firm = (P - c) q\_i = (52.5 - 30)*11.25 = 22.5\*11.25 = 253.125.

medium

Medium: Consider a differentiated-product Bertrand duopoly where firm i's demand is q\_i = A - B p\_i + D p\_j with A=100, B=2, D=0.5 and constant marginal cost c=30 for both firms. Firms set prices simultaneously. Find the Nash equilibrium prices and profits. (Solve the first-order conditions.)

**Hint:** Write profit π\_i = (p\_i - c) q\_i. Take derivative ∂π\_i/∂p\_i and solve the two linear equations for p\_1 and p\_2 in symmetric equilibrium p\_1 = p\_2 = p\*.

Show solution

Write q\_i = 100 - 2 p\_i + 0.5 p\_j. Profit π\_i = (p\_i - 30)(100 - 2 p\_i + 0.5 p\_j). FOC: ∂π\_i/∂p\_i = (100 - 2 p\_i + 0.5 p\_j) + (p\_i - 30)(-2) = 0 → 100 - 2 p\_i + 0.5 p\_j -2 p\_i + 60 = 0 → 160 -4 p\_i +0.5 p\_j =0. By symmetry set p\_i=p\_j=p*, so 160 -4 p* +0.5 p *= 0 → 160 -3.5 p* =0 → p *= 160/3.5 = 45.7142857. Demand per firm q* = 100 -2 p *+0.5 p* = 100 -1.5 p *= 100 -1.5×45.7142857 = 100 -68.5714286 = 31.4285714. Profit per firm = (p* - 30) q\* = 15.7142857×31.4285714 ≈ 494.89796.

hard

Hard: Suppose two firms play a one-shot Cournot game with linear demand P=a-bQ and identical marginal cost c. Now suppose one firm can commit to a capacity constraint K before the Cournot game begins, limiting its output to at most K. Describe qualitatively and, if possible, quantitatively, how a binding commitment K < q^\* (the standard Cournot quantity) changes the equilibrium. Use a=100, b=1, c=20 and suppose firm 1 commits to K = 10. Find the equilibrium quantities and price.

**Hint:** If firm 1's capacity is binding at K, it chooses q1 = K; firm 2 best responds: q2 = (a - c - b q1)/(2b). If the commitment is non-binding (K ≥ q1\_Cournot), revert to Cournot.

Show solution

Standard Cournot symmetric q\_i = (a - c)/(3b) = (100 -20)/3 = 26.666.... Since K=10 < 26.666..., firm 1's capacity is binding. So q1 = 10. Follower (firm 2) best response: q2 = (a - c - b q1)/(2b) = (80 -10)/2 = 70/2 = 35. Total Q = 45, Price P = 100 - 45 = 55. Profits: firm1 π1 = (55 -20)×10 = 350. Firm2 π2 = (55 -20)×35 = 35×35 = 1225. The capacity constraint reduces the constrained firm's output and allows the rival to expand beyond the unconstrained Cournot level, raising price relative to the unconstrained Cournot price (which was 46.666...).

## Connections

Looking back, these oligopoly models are direct applications of the prerequisites: in Nash Equilibrium we learned to find strategy profiles with no profitable unilateral deviation; each model's equilibrium (Cournot quantities or Bertrand prices) is exactly such a profile. In Profit Maximization we learned MR=MC and concavity checks: that machinery is used to derive each firm's best response (FOCs and second-order conditions). Looking forward, mastering these models enables analyzing repeated oligopoly (collusion and trigger strategies), dynamic entry and investment games (limit pricing, capacity investment), empirical structural IO (estimating demand and counterfactuals for mergers), and mechanism-design problems where strategic supply responses matter. Specific downstream concepts that build on these models include subgame-perfect equilibria in dynamic oligopoly, mixed-strategy equilibria in Bertrand-Edgeworth settings, and merger-simulation methods used in antitrust cases. Understanding when to use Cournot vs Bertrand vs Stackelberg is crucial: mis-specifying the strategic variable or timing can lead to qualitatively wrong policy or managerial conclusions.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
