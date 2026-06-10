---
title: KKT Conditions
description: Karush-Kuhn-Tucker. Optimization with inequality constraints.
date: '2026-07-01'
scheduled: '2026-11-21'
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
inspiration_url: https://templeton.host/tech-tree/kkt-conditions/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/kkt-conditions/](https://templeton.host/tech-tree/kkt-conditions/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# KKT Conditions

OptimizationDifficulty: ★★★★☆Depth: 9Unlocks: 1

Karush-Kuhn-Tucker. Optimization with inequality constraints.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Stationarity (gradient of the Lagrangian equals zero)
- -Primal feasibility (all problem constraints satisfied at the solution)
- -Complementary slackness (each inequality multiplier is zero unless its constraint is active)

## Key Symbols & Notation

mu\_i (multiplier for inequality constraint i; mu\_i >= 0)

## Essential Relationships

- -Stationarity equation: grad\_x L(x,lambda,mu) = 0
- -Complementary slackness equation: for each i, mu\_i \* g\_i(x) = 0

## Prerequisites (2)

[Lagrange Multipliers5 atoms](/tech-tree/lagrange-multipliers/)[Convex Optimization5 atoms](/tech-tree/convex-optimization/)

## Unlocks (1)

[Lagrangian Dualitylvl 5](/tech-tree/duality/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[marginal valueBusiness

A minimum-capacity requirement is an inequality constraint (capacity >= minimum), so the proper generalization from equality-constrained Lagrange multipliers to inequality constraints via KKT complementary slackness determines when the shadow price is positive vs zero](/business/marginal-value/)

Advanced Learning Details

### Graph Position

81

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

9

Chain Length

### Cognitive Load

6

Atomic Elements

35

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (13)

- - inequality constraint (function) g\_i(x) ≤ 0 as a type of constraint distinct from equality constraints
- - dual variables (Lagrange multipliers) associated specifically with inequality constraints
- - dual feasibility: multipliers for inequality constraints must be nonnegative
- - complementary slackness: product of each inequality multiplier and its constraint value equals zero
- - active set (binding constraints): the subset of inequality constraints that hold with equality at a point
- - slack variables s\_i ≥ 0 used to convert inequalities into equalities (g\_i(x) + s\_i = 0)
- - KKT conditions as a packaged set of conditions (stationarity, primal feasibility, dual feasibility, complementary slackness)
- - constraint qualifications (e.g., LICQ, MFCQ) - extra regularity conditions required for KKT necessity
- - Slater's condition - a sufficient condition in convex problems that guarantees strong duality and KKT sufficiency
- - Lagrangian dual problem (constructing a dual function from the Lagrangian and optimizing over multipliers)
- - duality gap: difference between primal and dual optimal objective values
- - interpretation of multipliers as sensitivities or 'shadow prices' (how optimal value changes with constraint bounds)
- - active-set reasoning/strategy: treat active inequalities as equalities to solve for candidate optima

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

You already know the equality-constraint story: at an optimum, the objective’s gradient is a linear combination of constraint gradients. KKT conditions are the inequality-constraint version of that same geometric idea—plus one extra “switch” (complementary slackness) that decides which inequalities actually matter at the solution.

TL;DR:

KKT conditions characterize optimal solutions of constrained problems with inequalities by combining (1) stationarity of the Lagrangian gradient, (2) primal feasibility, (3) dual feasibility (μᵢ ≥ 0), and (4) complementary slackness (μᵢ·gᵢ(x\*) = 0). In convex problems (with mild constraint qualifications), KKT is necessary and sufficient, and it’s the gateway to duality and many algorithms.

## What Is KKT? (And Why Inequalities Change the Game)

### The problem KKT solves

In many real optimization problems, constraints are not equalities like h(x)=0h(x)=0h(x)=0; they’re **inequalities** like “stay inside a region” or “don’t exceed a budget.” A standard form is:

min⁡x∈Rnf(x)s.t.gi(x)≤0,i=1,…,mhj(x)=0,j=1,…,p\begin{aligned}
\min\_{\mathbf{x} \in \mathbb{R}^n} \quad & f(\mathbf{x}) \\
\text{s.t.} \quad & g\_i(\mathbf{x}) \le 0, \quad i=1,\dots,m \\
& h\_j(\mathbf{x}) = 0, \quad j=1,\dots,p
\end{aligned}x∈Rnmin​s.t.​f(x)gi​(x)≤0,i=1,…,mhj​(x)=0,j=1,…,p​

You already know the equality-only case: if we had only hj(x)=0h\_j(\mathbf{x})=0hj​(x)=0, then at a solution x∗\mathbf{x}^\*x∗ we often get

∇f(x∗)+∑j=1pλj∇hj(x∗)=0.\nabla f(\mathbf{x}^\*) + \sum\_{j=1}^p \lambda\_j \nabla h\_j(\mathbf{x}^\*) = \mathbf{0}.∇f(x∗)+j=1∑p​λj​∇hj​(x∗)=0.

That says: the objective gradient is “balanced” by constraint gradients.

### Why inequalities are different

With inequalities, some constraints matter **only when they’re tight**. If the constraint is loose (you are strictly inside the feasible region), it shouldn’t influence the optimum condition.

Example intuition: Suppose you must minimize a function over a disk. If the unconstrained minimizer lies inside the disk, then the boundary constraint shouldn’t push back—you just choose the unconstrained minimizer. But if the minimizer wants to leave the disk, the boundary becomes “active” and exerts a force.

KKT conditions encode exactly this:

- •when an inequality constraint is **active** (gi(x∗)=0g\_i(\mathbf{x}^\*)=0gi​(x∗)=0), it can influence stationarity via a multiplier μi\mu\_iμi​;
- •when it’s **inactive/slack** (gi(x∗)<0g\_i(\mathbf{x}^\*)<0gi​(x∗)<0), its multiplier must be zero.

This “either active or multiplier is zero” rule is **complementary slackness**.

### The Lagrangian with inequalities

For the inequality constraints gi(x)≤0g\_i(\mathbf{x}) \le 0gi​(x)≤0, we introduce multipliers μi\mu\_iμi​ with the restriction μi≥0\mu\_i \ge 0μi​≥0.

The Lagrangian is

L(x,μ,λ)=f(x)+∑i=1mμigi(x)+∑j=1pλjhj(x).\mathcal{L}(\mathbf{x},\boldsymbol{\mu},\boldsymbol{\lambda}) = f(\mathbf{x}) + \sum\_{i=1}^m \mu\_i g\_i(\mathbf{x}) + \sum\_{j=1}^p \lambda\_j h\_j(\mathbf{x}).L(x,μ,λ)=f(x)+i=1∑m​μi​gi​(x)+j=1∑p​λj​hj​(x).

The sign restriction μi≥0\mu\_i\ge 0μi​≥0 is not decoration—it is what prevents the Lagrangian from “rewarding” constraint violation. If gi(x)>0g\_i(\mathbf{x})>0gi​(x)>0 (violated), then a nonnegative μi\mu\_iμi​ increases L\mathcal{L}L, penalizing violation.

### The KKT conditions (full set)

At a candidate optimum x∗\mathbf{x}^\*x∗ (under suitable constraint qualifications), there exist multipliers μi∗\mu\_i^\*μi∗​ and λj∗\lambda\_j^\*λj∗​ such that:

1) **Stationarity**

∇xL(x∗,μ∗,λ∗)=0.\nabla\_{\mathbf{x}} \mathcal{L}(\mathbf{x}^\*,\boldsymbol{\mu}^\*,\boldsymbol{\lambda}^\*) = \mathbf{0}.∇x​L(x∗,μ∗,λ∗)=0.

2) **Primal feasibility**

gi(x∗)≤0    ∀i,hj(x∗)=0    ∀j.g\_i(\mathbf{x}^\*) \le 0 \;\;\forall i, \qquad h\_j(\mathbf{x}^\*)=0 \;\;\forall j.gi​(x∗)≤0∀i,hj​(x∗)=0∀j.

3) **Dual feasibility**

μi∗≥0∀i.\mu\_i^\* \ge 0 \quad \forall i.μi∗​≥0∀i.

4) **Complementary slackness**

μi\\* gi(x∗)=0∀i.\mu\_i^\\*\, g\_i(\mathbf{x}^\*) = 0 \quad \forall i.μi\\*​gi​(x∗)=0∀i.

Take a moment to parse condition (4): a product equals zero, so for each inequality constraint iii, at least one must be zero:

- •either gi(x∗)=0g\_i(\mathbf{x}^\*) = 0gi​(x∗)=0 (constraint tight/active), and then μi∗\mu\_i^\*μi∗​ may be positive;
- •or μi∗=0\mu\_i^\*=0μi∗​=0 (no “force”), and then gi(x∗)g\_i(\mathbf{x}^\*)gi​(x∗) must be strictly negative or possibly zero.

### Geometric picture: level sets and an active boundary

In two dimensions, imagine sliding a contour line of fff until it first touches the feasible set. At a smooth touching point on an active constraint boundary, the contour is tangent to the boundary, so the objective gradient is parallel to the boundary normal.

Below is a simple ASCII-style diagram (conceptual, not to scale):

```
     objective level set
        (lower is better)
           ______
         /        \
        /          \
       |     x*     |   <-- first touching point
        \          /
         \________/
             |
             |  ∇g(x*) (normal to boundary)
             v
   ---------------------------  constraint boundary g(x)=0
   feasible region is one side (g(x)≤0)
```

KKT makes that “first touch” precise: ∇f(x∗)\nabla f(\mathbf{x}^\*)∇f(x∗) is balanced by a nonnegative combination of active constraint normals.

### Inline SVG diagram 1: objective level set touching feasible boundary

```
<svg xmlns="http://www.w3.org/2000/svg" width="560" height="240" viewBox="0 0 560 240">
  <rect width="560" height="240" fill="white"/>

  <!-- Feasible half-plane (g(x) <= 0) -->
  <polygon points="60,200 520,120 520,230 60,230" fill="#e8f3ff" stroke="none"/>

  <!-- Boundary line g(x)=0 -->
  <line x1="60" y1="200" x2="520" y2="120" stroke="#1f4e79" stroke-width="3"/>
  <text x="420" y="110" font-family="Arial" font-size="14" fill="#1f4e79">g(x)=0 (active boundary)</text>

  <!-- Level set ellipse -->
  <ellipse cx="260" cy="145" rx="110" ry="55" fill="none" stroke="#444" stroke-width="2"/>
  <text x="150" y="70" font-family="Arial" font-size="14" fill="#444">objective level set f(x)=c</text>

  <!-- Touch point x* -->
  <circle cx="340" cy="130" r="5" fill="#d62728"/>
  <text x="350" y="135" font-family="Arial" font-size="14" fill="#d62728">x*</text>

  <!-- Normal vector to boundary (∇g) -->
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1f4e79"/>
    </marker>
  </defs>
  <line x1="340" y1="130" x2="310" y2="70" stroke="#1f4e79" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="235" y="75" font-family="Arial" font-size="14" fill="#1f4e79">∇g(x*)</text>

  <!-- Gradient of f (∇f) opposite direction -->
  <line x1="340" y1="130" x2="370" y2="190" stroke="#444" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="380" y="195" font-family="Arial" font-size="14" fill="#444">∇f(x*)</text>

  <!-- Feasible label -->
  <text x="70" y="225" font-family="Arial" font-size="14" fill="#0b3d91">feasible region (g(x)≤0)</text>
</svg>
```

Interpretation: at the touching point x∗\mathbf{x}^\*x∗, stationarity becomes roughly ∇f(x∗)+μ∗∇g(x∗)=0\nabla f(\mathbf{x}^\*) + \mu^\* \nabla g(\mathbf{x}^\*) = 0∇f(x∗)+μ∗∇g(x∗)=0 with μ∗≥0\mu^\*\ge 0μ∗≥0.

### What KKT gives you

KKT conditions are:

- •a **certificate** of optimality (especially in convex problems),
- •a bridge to **duality** (you’ll use them constantly in [Lagrangian Duality](/tech-tree/duality/)),
- •and a foundation for algorithms (active-set methods, primal-dual methods, interior-point methods).

## Core Mechanic 1: Stationarity + Feasibility (How the Lagrangian Extends)

### Start from the equality case you know

With equality constraints, Lagrange multipliers say: at x∗\mathbf{x}^\*x∗,

∇f(x∗)+∑jλj∇hj(x∗)=0.\nabla f(\mathbf{x}^\*) + \sum\_j \lambda\_j \nabla h\_j(\mathbf{x}^\*) = \mathbf{0}.∇f(x∗)+j∑​λj​∇hj​(x∗)=0.

That arises from the idea that you can’t move in any feasible direction without increasing fff.

### Add inequalities: the new Lagrangian is still the right object

For inequalities, define

L(x,μ,λ)=f(x)+∑i=1mμigi(x)+∑j=1pλjhj(x).\mathcal{L}(\mathbf{x},\boldsymbol{\mu},\boldsymbol{\lambda}) = f(\mathbf{x}) + \sum\_{i=1}^m \mu\_i g\_i(\mathbf{x}) + \sum\_{j=1}^p \lambda\_j h\_j(\mathbf{x}).L(x,μ,λ)=f(x)+i=1∑m​μi​gi​(x)+j=1∑p​λj​hj​(x).

Then **stationarity** is the same-looking condition:

∇xL(x∗,μ∗,λ∗)=0.\nabla\_{\mathbf{x}} \mathcal{L}(\mathbf{x}^\*,\boldsymbol{\mu}^\*,\boldsymbol{\lambda}^\*) = \mathbf{0}.∇x​L(x∗,μ∗,λ∗)=0.

Let’s expand it explicitly (this “show your work” step matters because it tells you what vectors are being balanced):

∇xL(x,μ,λ)=∇f(x)+∑i=1mμi∇gi(x)+∑j=1pλj∇hj(x).\begin{aligned}
\nabla\_{\mathbf{x}} \mathcal{L}(\mathbf{x},\boldsymbol{\mu},\boldsymbol{\lambda})
&= \nabla f(\mathbf{x}) + \sum\_{i=1}^m \mu\_i \nabla g\_i(\mathbf{x}) + \sum\_{j=1}^p \lambda\_j \nabla h\_j(\mathbf{x}).
\end{aligned}∇x​L(x,μ,λ)​=∇f(x)+i=1∑m​μi​∇gi​(x)+j=1∑p​λj​∇hj​(x).​

So stationarity at x∗\mathbf{x}^\*x∗ means

∇f(x∗)+∑i=1mμi∗∇gi(x∗)+∑j=1pλj∗∇hj(x∗)=0.\nabla f(\mathbf{x}^\*) + \sum\_{i=1}^m \mu\_i^\* \nabla g\_i(\mathbf{x}^\*) + \sum\_{j=1}^p \lambda\_j^\* \nabla h\_j(\mathbf{x}^\*) = \mathbf{0}.∇f(x∗)+i=1∑m​μi∗​∇gi​(x∗)+j=1∑p​λj∗​∇hj​(x∗)=0.

This is a **vector equation** in Rn\mathbb{R}^nRn.

### Primal feasibility: you must actually be allowed to stand there

KKT always includes the obvious requirement:

- •gi(x∗)≤0g\_i(\mathbf{x}^\*) \le 0gi​(x∗)≤0 for all inequalities,
- •hj(x∗)=0h\_j(\mathbf{x}^\*) = 0hj​(x∗)=0 for all equalities.

It’s easy to overlook because it’s “just the constraints,” but it’s doing a lot of work: if you solve stationarity without feasibility, you can easily get points outside the feasible set.

### Dual feasibility: why μᵢ ≥ 0 is not optional

For each inequality, KKT requires

μi∗≥0.\mu\_i^\* \ge 0.μi∗​≥0.

Think of μi\mu\_iμi​ as a **penalty weight** on constraint violation gi(x)g\_i(\mathbf{x})gi​(x). If you let μi\mu\_iμi​ be negative, then violating the constraint (making gi(x)g\_i(\mathbf{x})gi​(x) positive) could *reduce* the Lagrangian. That breaks the interpretation of L\mathcal{L}L as objective + penalties.

Geometrically, μi∇gi(x∗)\mu\_i \nabla g\_i(\mathbf{x}^\*)μi​∇gi​(x∗) is a push in the direction of the constraint normal. A negative μi\mu\_iμi​ would pull you *into* the infeasible region.

### How stationarity “selects” a boundary

One inequality constraint (for intuition):

min⁡f(x)  s.t. g(x)≤0.\min f(\mathbf{x}) \; \text{s.t. } g(\mathbf{x}) \le 0.minf(x)s.t. g(x)≤0.

If the optimum is interior (g(x∗)<0g(\mathbf{x}^\*)<0g(x∗)<0), then there’s no reason to have μ∗>0\mu^\*>0μ∗>0, because the constraint isn’t binding. KKT will force μ∗=0\mu^\*=0μ∗=0 (via complementary slackness, coming next), and stationarity reduces to ∇f(x∗)=0\nabla f(\mathbf{x}^\*)=0∇f(x∗)=0.

If the optimum lies on the boundary (g(x∗)=0g(\mathbf{x}^\*)=0g(x∗)=0), stationarity becomes

∇f(x∗)+μ∗∇g(x∗)=0⇒∇f(x∗)=−μ∗∇g(x∗).\nabla f(\mathbf{x}^\*) + \mu^\* \nabla g(\mathbf{x}^\*) = 0
\quad\Rightarrow\quad
\nabla f(\mathbf{x}^\*) = -\mu^\* \nabla g(\mathbf{x}^\*).∇f(x∗)+μ∗∇g(x∗)=0⇒∇f(x∗)=−μ∗∇g(x∗).

So ∇f(x∗)\nabla f(\mathbf{x}^\*)∇f(x∗) is parallel to ∇g(x∗)\nabla g(\mathbf{x}^\*)∇g(x∗), with nonnegative scaling (μ∗≥0\mu^\*\ge 0μ∗≥0). That is the inequality analog of the equality “parallel gradients” picture.

### Multiple active inequalities: cones, not just lines

With several inequalities, you do **not** generally have ∇f\nabla f∇f parallel to a single constraint normal. Instead, you get a nonnegative combination:

∇f(x∗)=−∑i∈Aμi∗∇gi(x∗),μi∗≥0.\nabla f(\mathbf{x}^\*) = -\sum\_{i \in \mathcal{A}} \mu\_i^\* \nabla g\_i(\mathbf{x}^\*), \qquad \mu\_i^\* \ge 0.∇f(x∗)=−i∈A∑​μi∗​∇gi​(x∗),μi∗​≥0.

Here A\mathcal{A}A is the **active set**: constraints with gi(x∗)=0g\_i(\mathbf{x}^\*)=0gi​(x∗)=0.

This means −∇f(x∗)-\nabla f(\mathbf{x}^\*)−∇f(x∗) lies in the **cone** generated by the active constraint normals.

A quick two-constraint picture: if two boundaries meet at a corner, then the outward normals span a wedge-shaped cone. KKT says the objective gradient must point into that cone for the corner to be optimal.

### Constraint qualifications (why KKT sometimes “fails”)

KKT conditions are not magical; they’re guaranteed under mild regularity assumptions called **constraint qualifications** (CQs). A common one you’ll see in convex optimization is **Slater’s condition**:

- •If the problem is convex (convex fff, convex gig\_igi​) and there exists a strictly feasible point x~\tilde{\mathbf{x}}x~ with gi(x~)<0g\_i(\tilde{\mathbf{x}}) < 0gi​(x~)<0 for all iii and hj(x~)=0h\_j(\tilde{\mathbf{x}})=0hj​(x~)=0, then KKT conditions are necessary and (with convexity) sufficient.

You don’t need to memorize every CQ right now; the practical lesson is:

- •In convex problems, if you can get **strict feasibility**, KKT is the right target.
- •In nonconvex problems, KKT is often necessary for local optima but not sufficient.

We’ll keep this in the background as we focus on the mechanics you’ll actually use: stationarity + feasibility + complementary slackness.

## Core Mechanic 2: Complementary Slackness (Active vs. Slack as a Switch)

### The new ingredient you didn’t need for equalities

Equalities are always “active” because hj(x)=0h\_j(\mathbf{x})=0hj​(x)=0 must hold exactly. Inequalities are different: they can be tight or loose.

KKT encodes that with:

μi∗ gi(x∗)=0,μi∗≥0,gi(x∗)≤0.\mu\_i^\*\, g\_i(\mathbf{x}^\*) = 0, \quad \mu\_i^\* \ge 0, \quad g\_i(\mathbf{x}^\*) \le 0.μi∗​gi​(x∗)=0,μi∗​≥0,gi​(x∗)≤0.

This trio is worth reading as a **logic rule**:

- •If gi(x∗)<0g\_i(\mathbf{x}^\*) < 0gi​(x∗)<0 (strictly feasible / slack), then necessarily μi∗=0\mu\_i^\* = 0μi∗​=0.
- •If μi∗>0\mu\_i^\* > 0μi∗​>0, then necessarily gi(x∗)=0g\_i(\mathbf{x}^\*) = 0gi​(x∗)=0 (active).
- •If gi(x∗)=0g\_i(\mathbf{x}^\*) = 0gi​(x∗)=0, then μi∗\mu\_i^\*μi∗​ can be 0 or positive (depending on whether the constraint truly matters in the stationarity balance).

This is why people describe μi\mu\_iμi​ as a “force”: it only pushes when you’re at the wall.

### The active set viewpoint

Define the active set at a feasible point x\mathbf{x}x:

A(x)={i:gi(x)=0}.\mathcal{A}(\mathbf{x}) = \{ i : g\_i(\mathbf{x}) = 0 \}.A(x)={i:gi​(x)=0}.

Complementary slackness implies:

μi∗=0for all i∉A(x∗).\mu\_i^\* = 0 \quad \text{for all } i \notin \mathcal{A}(\mathbf{x}^\*).μi∗​=0for all i∈/A(x∗).

So stationarity effectively reduces to a smaller set of constraints:

∇f(x∗)+∑i∈A(x∗)μi∗∇gi(x∗)+∑j=1pλj∗∇hj(x∗)=0.\nabla f(\mathbf{x}^\*) + \sum\_{i \in \mathcal{A}(\mathbf{x}^\*)} \mu\_i^\* \nabla g\_i(\mathbf{x}^\*) + \sum\_{j=1}^p \lambda\_j^\* \nabla h\_j(\mathbf{x}^\*) = \mathbf{0}.∇f(x∗)+i∈A(x∗)∑​μi∗​∇gi​(x∗)+j=1∑p​λj∗​∇hj​(x∗)=0.

This is the conceptual engine behind **active-set methods**: guess which constraints are active, solve the equality-constrained problem, then check consistency.

### Inline SVG diagram 2: complementary slackness schematic

```
<svg xmlns="http://www.w3.org/2000/svg" width="560" height="210" viewBox="0 0 560 210">
  <rect width="560" height="210" fill="white"/>
  <text x="20" y="28" font-family="Arial" font-size="16" fill="#222">Complementary slackness: μᵢ gᵢ(x*) = 0</text>

  <!-- Two columns: slack vs active -->
  <rect x="30" y="50" width="240" height="130" rx="10" fill="#f2f2f2" stroke="#999"/>
  <rect x="290" y="50" width="240" height="130" rx="10" fill="#e8f3ff" stroke="#1f4e79"/>

  <text x="110" y="75" font-family="Arial" font-size="15" fill="#333">Slack constraint</text>
  <text x="370" y="75" font-family="Arial" font-size="15" fill="#1f4e79">Active constraint</text>

  <text x="55" y="105" font-family="Arial" font-size="14" fill="#333">gᵢ(x*) &lt; 0</text>
  <text x="55" y="130" font-family="Arial" font-size="14" fill="#333">⇒ μᵢ = 0</text>
  <text x="55" y="155" font-family="Arial" font-size="14" fill="#333">No contribution to stationarity</text>

  <text x="315" y="105" font-family="Arial" font-size="14" fill="#1f4e79">gᵢ(x*) = 0</text>
  <text x="315" y="130" font-family="Arial" font-size="14" fill="#1f4e79">μᵢ ≥ 0 (often &gt; 0)</text>
  <text x="315" y="155" font-family="Arial" font-size="14" fill="#1f4e79">May contribute: μᵢ∇gᵢ(x*)</text>

  <!-- Switch arrow -->
  <defs>
    <marker id="arrow2" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#555"/>
    </marker>
  </defs>
  <line x1="270" y1="115" x2="290" y2="115" stroke="#555" stroke-width="3" marker-end="url(#arrow2)"/>
  <text x="245" y="100" font-family="Arial" font-size="12" fill="#555">tighten</text>
  <text x="245" y="130" font-family="Arial" font-size="12" fill="#555">to</text>
  <text x="245" y="160" font-family="Arial" font-size="12" fill="#555">activate</text>
</svg>
```

### Economic interpretation (helps you remember the sign)

In many applications, gi(x)≤0g\_i(\mathbf{x}) \le 0gi​(x)≤0 is a resource limit (e.g., “cost − budget ≤ 0”). Then μi∗\mu\_i^\*μi∗​ behaves like a **shadow price**: how much the optimal objective value would improve if you relaxed the constraint slightly.

If a constraint is slack, relaxing it doesn’t change the solution locally, so the shadow price is zero: μi∗=0\mu\_i^\*=0μi∗​=0.

If a constraint is binding, relaxing it can help, so the shadow price can be positive: μi∗>0\mu\_i^\*>0μi∗​>0.

### KKT as a checklist (how you use it in practice)

For a candidate x∗\mathbf{x}^\*x∗:

1. 1)Check primal feasibility: are all gi(x∗)≤0g\_i(\mathbf{x}^\*) \le 0gi​(x∗)≤0 and hj(x∗)=0h\_j(\mathbf{x}^\*)=0hj​(x∗)=0?
2. 2)Identify active constraints: those with gi(x∗)=0g\_i(\mathbf{x}^\*)=0gi​(x∗)=0.
3. 3)Enforce complementary slackness: set μi=0\mu\_i=0μi​=0 for slack constraints.
4. 4)Solve stationarity for x∗\mathbf{x}^\*x∗ and remaining multipliers.
5. 5)Check dual feasibility: μi≥0\mu\_i \ge 0μi​≥0.

In convex problems (plus a CQ like Slater), if you find (x∗,μ∗,λ∗)(\mathbf{x}^\*,\boldsymbol{\mu}^\*,\boldsymbol{\lambda}^\*)(x∗,μ∗,λ∗) satisfying KKT, you are done: it’s globally optimal.

### Breathing room: what KKT is not

- •KKT does **not** automatically tell you which constraints are active—you must infer it (often by case analysis or algorithmically).
- •In nonconvex problems, KKT points can be minima, maxima, or saddles.
- •If the constraint gradients are degenerate (constraint qualification fails), an optimum might exist but multipliers might not behave nicely.

Still: in the convex setting you already know, KKT is one of the most powerful “solve-by-conditions” tools you can learn.

## Application/Connection: How KKT Leads to Duality (and Algorithms)

### Why KKT is the doorway to duality

You’re about to unlock [Lagrangian Duality](/tech-tree/duality/). KKT conditions are the bridge between:

- •the **primal** problem (choose x\mathbf{x}x), and
- •the **dual** problem (choose multipliers μ,λ\boldsymbol{\mu},\boldsymbol{\lambda}μ,λ).

The central object is the Lagrangian:

L(x,μ,λ)=f(x)+∑iμigi(x)+∑jλjhj(x).\mathcal{L}(\mathbf{x},\boldsymbol{\mu},\boldsymbol{\lambda}) = f(\mathbf{x}) + \sum\_i \mu\_i g\_i(\mathbf{x}) + \sum\_j \lambda\_j h\_j(\mathbf{x}).L(x,μ,λ)=f(x)+i∑​μi​gi​(x)+j∑​λj​hj​(x).

For fixed multipliers, you can minimize over x\mathbf{x}x to get the **dual function**:

q(μ,λ)=inf⁡xL(x,μ,λ).q(\boldsymbol{\mu},\boldsymbol{\lambda}) = \inf\_{\mathbf{x}} \mathcal{L}(\mathbf{x},\boldsymbol{\mu},\boldsymbol{\lambda}).q(μ,λ)=xinf​L(x,μ,λ).

The dual then maximizes qqq subject to μi≥0\mu\_i \ge 0μi​≥0.

KKT conditions are exactly the “meeting point” where:

- •x∗\mathbf{x}^\*x∗ is optimal for the primal,
- •(μ∗,λ∗)(\boldsymbol{\mu}^\*,\boldsymbol{\lambda}^\*)(μ∗,λ∗) is optimal for the dual,
- •and the **duality gap** is zero (under strong duality).

### Strong duality and KKT in convex problems

In convex optimization, if Slater’s condition holds, then:

- •strong duality holds, and
- •there exist multipliers that satisfy KKT.

This turns KKT into a **necessary and sufficient** optimality characterization.

### Algorithmic consequence: primal-dual thinking

Many algorithms iteratively update both:

- •primal variables x\mathbf{x}x (trying to satisfy constraints and reduce fff), and
- •dual variables μ\boldsymbol{\mu}μ (trying to penalize violations and satisfy μ≥0\mu\ge 0μ≥0).

Complementary slackness becomes a target condition: at convergence, each inequality is either tight with positive multiplier, or slack with zero multiplier.

### Guided prompt for the interactive canvas (tie-in to Example 2)

If your tech-tree interface has an interactive 2D canvas:

1. 1)Plot the feasible region for Example 2 (a disk/ball constraint).
2. 2)Plot objective contours (circles centered at the unconstrained minimizer).
3. 3)Drag the contour level down until it just touches the feasible boundary.
4. 4)At the touching point x∗\mathbf{x}^\*x∗, draw two arrows: ∇f(x∗)\nabla f(\mathbf{x}^\*)∇f(x∗) and ∇g(x∗)\nabla g(\mathbf{x}^\*)∇g(x∗).

Prompt to answer while exploring: \*\*“Is ∇f(x∗)\nabla f(\mathbf{x}^\*)∇f(x∗) exactly opposite to ∇g(x∗)\nabla g(\mathbf{x}^\*)∇g(x∗)? What changes when the unconstrained minimizer moves inside the disk?”\*\*

This visual experiment is the cleanest way to feel the difference between interior solutions (μ=0\mu=0μ=0) and boundary solutions (μ>0\mu>0μ>0).

### Quick comparison table: equality vs inequality constraints

| Feature | Equality h(x)=0h(\mathbf{x})=0h(x)=0 | Inequality g(x)≤0g(\mathbf{x})\le 0g(x)≤0 |
| --- | --- | --- |
| Multiplier sign | λ\lambdaλ free (any real) | μ≥0\mu \ge 0μ≥0 |
| Always active? | Yes | No (active only if g(x∗)=0g(\mathbf{x}^\*)=0g(x∗)=0) |
| Extra condition | none beyond feasibility | complementary slackness μg(x∗)=0\mu g(\mathbf{x}^\*)=0μg(x∗)=0 |
| Geometry | gradient balance on manifold | gradient balance using active boundary normals |

### Where you’ll see KKT immediately

- •Support Vector Machines (hinge loss + margin constraints)
- •Portfolio optimization (risk objective with budget and bound constraints)
- •Projection problems (closest point in a convex set)
- •Regularization with constraints (e.g., norm constraints)

As you move to duality, you’ll repeatedly use KKT to go from a constrained primal to a dual problem you can solve more easily—or to certify optimality of a proposed solution.

## Worked Examples (3)

### Example 1: A 1D inequality constraint (see complementary slackness in action)

Solve

\n\n$$

\begin{aligned}

\min\_{x \in \mathbb{R}} \quad & f(x) = (x-2)^2 \\

\text{s.t.} \quad & g(x)= -x \le 0 \;\;\; (\text{equivalently } x \ge 0)

\end{aligned}

This is convex: $f$ is convex, and the feasible set $x\ge 0$ is convex.

1. Step 1: Write the Lagrangian.

   \nWe have one inequality constraint g(x)=−x≤0g(x)=-x\le 0g(x)=−x≤0 with multiplier μ ≥ 0:

   \n$$

   \mathcal{L}(x,\mu) = (x-2)^2 + \mu(-x).
2. Step 2: Stationarity (derivative w.r.t. x equals 0).

   \nCompute:

   \n$$

   \frac{\partial \mathcal{L}}{\partial x} = 2(x-2) - \mu.

   \nSet to zero at optimum:
   \n$$
   2(x^\*-2) - \mu^\* = 0 \quad\Rightarrow\quad \mu^\* = 2(x^\*-2).
3. Step 3: Primal feasibility.

   \nConstraint is −x∗≤0⇒x∗≥0-x^\*\le 0 \Rightarrow x^\*\ge 0−x∗≤0⇒x∗≥0.
4. Step 4: Dual feasibility.

   \nμ\* ≥ 0.
5. Step 5: Complementary slackness.

   \n$$

   \mu^ *g(x^*) = \mu^*(-x^*) = 0.

   Soeither(a)μ∗=0or(b)x∗=0.So either (a) μ\* = 0 or (b) x\* = 0.Soeither(a)μ∗=0or(b)x∗=0.
6. Step 6: Case analysis.

   \nCase A: μ\* = 0.

   Then stationarity gives 0 = 2(x*-2) ⇒ x* = 2.

   Check feasibility: x\* = 2 ≥ 0 (OK).

   Check g(x*) = -2 < 0, so constraint is slack, consistent with μ*=0.

   \nCase B: x\* = 0.

   Then stationarity gives μ *= 2(0-2) = -4, which violates μ* ≥ 0.

   So Case B is impossible.
7. Step 7: Conclude solution.

   \n$$

   x^ *= 2, \quad \mu^*=0.

**Insight:** Because the unconstrained minimizer x=2 is already feasible (it lies in x≥0), the inequality constraint is slack at optimum, so complementary slackness forces μ\*=0 and KKT reduces to the unconstrained condition ∇f=0.

### Example 2: Projection onto a disk (geometry + KKT multipliers)

Solve the constrained minimization (a projection problem):

\n$$

\begin{aligned}

\min\_{\mathbf{x}\in\mathbb{R}^2} \quad & f(\mathbf{x}) = \tfrac12\lVert \mathbf{x} - \mathbf{a} \rVert^2 \\

\text{s.t.}\quad & g(\mathbf{x}) = \lVert \mathbf{x} \rVert^2 - 1 \le 0

\end{aligned}

where \(\mathbf{a}\in\mathbb{R}^2\) is given. This finds the closest point in the unit disk to \(\mathbf{a}\).

1. Step 1: Build the Lagrangian.

   \nWe have one inequality constraint with μ ≥ 0:

   \n$$

   \mathcal{L}(\mathbf{x},\mu)=\tfrac12\lVert \mathbf{x}-\mathbf{a}\rVert^2 + \mu(\lVert \mathbf{x}\rVert^2 - 1).
2. Step 2: Compute the gradient w.r.t. **x** and apply stationarity.

   \nFirst expand gradients carefully:

   \n- For 12∥x−a∥2\tfrac12\lVert \mathbf{x}-\mathbf{a}\rVert^221​∥x−a∥2, we have

   ∇x12∥x−a∥2=x−a.\nabla\_{\mathbf{x}} \tfrac12\lVert \mathbf{x}-\mathbf{a}\rVert^2 = \mathbf{x}-\mathbf{a}.∇x​21​∥x−a∥2=x−a.

   - •For ∥x∥2−1\lVert \mathbf{x}\rVert^2 - 1∥x∥2−1, we have

   ∇x(∥x∥2−1)=2x.\nabla\_{\mathbf{x}}(\lVert \mathbf{x}\rVert^2 - 1)=2\mathbf{x}.∇x​(∥x∥2−1)=2x.

   So

   \n$$

   \nabla\_{\mathbf{x}}\mathcal{L}(\mathbf{x},\mu) = (\mathbf{x}-\mathbf{a}) + \mu(2\mathbf{x}).

   Stationarity at optimum:
   \n$$
   (\mathbf{x}^\* - \mathbf{a}) + 2\mu^\*\mathbf{x}^\* = \mathbf{0}
   \quad\Rightarrow\quad
   (1+2\mu^\*)\mathbf{x}^\* = \mathbf{a}.

   Thus

   \n$$

   \mathbf{x}^ *= \frac{1}{1+2\mu^*}\,\mathbf{a}.
3. Step 3: Primal feasibility.

   \nConstraint: ∥x∗∥2−1≤0\lVert \mathbf{x}^\*\rVert^2 - 1 \le 0∥x∗∥2−1≤0 i.e. ∥x∗∥≤1\lVert\mathbf{x}^\*\rVert \le 1∥x∗∥≤1.
4. Step 4: Complementary slackness.

   \n$$

   \mu^*(\lVert\mathbf{x}^*\rVert^2 - 1)=0.

   So either μ\*=0 (interior) or $\lVert\mathbf{x}^\*\rVert=1$ (boundary).
5. Step 5: Case A (interior): μ\* = 0.

   \nThen

   \n$$

   \mathbf{x}^\* = \mathbf{a}.

   Feasibility requires $\lVert\mathbf{a}\rVert \le 1$.
   So if \*\*a\*\* is inside the disk, the solution is just \*\*a\*\* itself.
6. Step 6: Case B (boundary): ∥x∗∥=1\lVert\mathbf{x}^\*\rVert=1∥x∗∥=1 with μ\* ≥ 0.

   \nWe have x∗=a/(1+2μ∗)\mathbf{x}^\* = \mathbf{a}/(1+2\mu^\*)x∗=a/(1+2μ∗), so

   \n$$

   \lVert\mathbf{x}^*\rVert = \frac{\lVert\mathbf{a}\rVert}{1+2\mu^*} = 1

   \quad\Rightarrow\quad

   1+2\mu^\* = \lVert\mathbf{a}\rVert.

   Thus
   \n$$
   \mu^\* = \tfrac12(\lVert\mathbf{a}\rVert - 1).

   Dual feasibility μ\* ≥ 0 implies ∥a∥≥1\lVert\mathbf{a}\rVert \ge 1∥a∥≥1.

   Then

   \n$$

   \mathbf{x}^\* = \frac{1}{\lVert\mathbf{a}\rVert}\,\mathbf{a}.
7. Step 7: Summarize solution.

   \n$$

   \mathbf{x}^\* =

   \begin{cases}

   \mathbf{a}, & \lVert\mathbf{a}\rVert \le 1 \\

   \mathbf{a}/\lVert\mathbf{a}\rVert, & \lVert\mathbf{a}\rVert > 1

   \end{cases}

   And
   \n$$
   \mu^\* =
   \begin{cases}
   0, & \lVert\mathbf{a}\rVert \le 1 \\
   \tfrac12(\lVert\mathbf{a}\rVert - 1), & \lVert\mathbf{a}\rVert > 1.
   \end{cases}

**Insight:** This is a perfect KKT geometry example: if **a** lies inside the disk, the constraint is slack and μ\*=0, so the minimizer is interior. If **a** lies outside, the optimum occurs on the boundary where the objective’s level set first touches the disk. Stationarity becomes a balance of the objective gradient (**x**−**a**) with the boundary normal 2**x**, and μ\*>0 measures how strongly the boundary pushes back.

### Example 3: Two inequalities (active-set reasoning at a corner)

Solve

\n$$

\begin{aligned}

\min\_{x,y} \quad & f(x,y) = x + y \\

\text{s.t.}\quad & g\_1(x,y)= -x \le 0 \;(x\ge 0)\\

& g\_2(x,y)= -y \le 0 \;(y\ge 0)

\end{aligned}

Thisislinearobjectiveoverthefirstquadrant.Theminimumisvisuallyattheorigin,butwe’llcertifyitviaKKT.This is linear objective over the first quadrant. The minimum is visually at the origin, but we’ll certify it via KKT.Thisislinearobjectiveoverthefirstquadrant.Theminimumisvisuallyattheorigin,butwe’llcertifyitviaKKT.

1. Step 1: Lagrangian.

   \n$$

   \mathcal{L}(x,y,\mu\_1,\mu\_2)= x+y + \mu\_1(-x) + \mu\_2(-y).

   withμ1,μ2≥0.with μ₁, μ₂ ≥ 0.withμ1​,μ2​≥0.
2. Step 2: Stationarity.

   \nCompute partial derivatives:

   \n$$

   \frac{\partial \mathcal{L}}{\partial x}=1-\mu\_1=0 \Rightarrow \mu\_1^\*=1,

   \frac{\partial \mathcal{L}}{\partial y}=1-\mu\_2=0 \Rightarrow \mu\_2^\*=1.
3. Step 3: Primal feasibility.

   \nWe need x *≥ 0 and y* ≥ 0.
4. Step 4: Complementary slackness.

   \n$$

   \mu\_1^*(-x^*)=0 \Rightarrow 1\cdot (-x^*)=0 \Rightarrow x^*=0.

   Similarly,
   \n$$
   \mu\_2^\*(-y^\*)=0 \Rightarrow y^\*=0.
5. Step 5: Dual feasibility.

   \nμ₁*=1 ≥ 0, μ₂*=1 ≥ 0 (OK).
6. Step 6: Conclude.

   \n$$

   (x^*,y^*)=(0,0)

   withmultipliersμ1∗=μ2∗=1.with multipliers μ₁\*=μ₂\*=1.withmultipliersμ1​∗=μ2​∗=1.

**Insight:** At the optimum, both inequalities are active (x*=0, y*=0). The objective gradient is (1,1). KKT says −∇f must lie in the cone spanned by ∇g₁=(−1,0) and ∇g₂=(0,−1) with nonnegative weights—exactly what μ₁=μ₂=1 provides.

## Key Takeaways

- ✓

  KKT extends Lagrange multipliers to inequality constraints by adding nonnegative multipliers μᵢ and the complementary slackness rule μᵢ gᵢ(x\*) = 0.
- ✓

  The full KKT system is: stationarity (∇ₓL=0), primal feasibility (gᵢ≤0, hⱼ=0), dual feasibility (μᵢ≥0), and complementary slackness.
- ✓

  Complementary slackness is a per-constraint “switch”: slack constraint ⇒ μᵢ=0; positive μᵢ ⇒ constraint is active (tight).
- ✓

  At an optimum, −∇f(x\*) lies in the cone generated by normals of active inequality constraints (plus equality constraint normals with free multipliers).
- ✓

  In convex optimization with a suitable constraint qualification (e.g., Slater’s condition), KKT conditions are necessary and sufficient for global optimality.
- ✓

  KKT conditions are the practical gateway to duality: at optimality (under strong duality), primal and dual variables satisfy KKT simultaneously.
- ✓

  Active-set reasoning (guess active constraints, solve, then verify) is often the most straightforward way to solve small KKT problems by hand.

## Common Mistakes

- ✗

  Forgetting dual feasibility: allowing μᵢ < 0 for constraints written as gᵢ(x) ≤ 0 (sign conventions matter).
- ✗

  Applying complementary slackness incorrectly (it is μᵢ·gᵢ(x*)=0, not μᵢ=0 or gᵢ(x*)=0 for all i).
- ✗

  Treating KKT as sufficient in nonconvex problems without checking convexity/constraint qualifications (a KKT point can be a saddle or maximum).
- ✗

  Mixing constraint forms (e.g., writing x ≥ 0 but using μ≥0 as if it were g(x)≤0 without converting to a consistent g(x)≤0 representation).

## Practice

easy

Solve using KKT:

min⁡xx2s.t.x−1≤0\begin{aligned}
\min\_x \quad & x^2 \\
\text{s.t.}\quad & x - 1 \le 0
\end{aligned}xmin​s.t.​x2x−1≤0​

**Hint:** The unconstrained minimizer is x=0. Check if it is feasible. Use complementary slackness to decide μ.

Show solution

Constraint is x ≤ 1, so x=0 is feasible and should be optimal.

Lagrangian: L(x,μ)=x^2+μ(x-1), μ≥0.

Stationarity: dL/dx=2x+μ=0 ⇒ μ=−2x.

At x*=0 ⇒ μ*=0.

Primal feasibility: 0−1≤0 OK. Complementary slackness: μ*(x*−1)=0·(−1)=0 OK.

Thus x*=0, μ*=0.

medium

Solve using KKT:

min⁡x,y(x−1)2+(y−1)2s.t.x≥0,  y≥0\begin{aligned}
\min\_{x,y} \quad & (x-1)^2 + (y-1)^2 \\
\text{s.t.}\quad & x \ge 0,\; y \ge 0
\end{aligned}x,ymin​s.t.​(x−1)2+(y−1)2x≥0,y≥0​

**Hint:** Convert to g₁=−x≤0, g₂=−y≤0. The unconstrained minimizer is (1,1). Which constraints are active there?

Show solution

Unconstrained minimizer is (1,1), which is feasible (x≥0,y≥0). So the solution is interior with both constraints slack.

KKT: μ₁=μ₂=0 by complementary slackness since g₁(1,1)=−1<0 and g₂(1,1)=−1<0.

Stationarity reduces to ∇f=0, which holds at (1,1).

Thus (x*,y*)=(1,1), μ₁*=μ₂*=0.

hard

Projection with a radius constraint: for given **a** ∈ ℝⁿ, solve

min⁡x12∥x−a∥2s.t.∥x∥≤R\begin{aligned}
\min\_{\mathbf{x}} \quad & \tfrac12\lVert \mathbf{x} - \mathbf{a} \rVert^2 \\
\text{s.t.}\quad & \lVert \mathbf{x} \rVert \le R
\end{aligned}xmin​s.t.​21​∥x−a∥2∥x∥≤R​

Give **x** *and the multiplier μ* as a function of **a** and R.

**Hint:** Use g(x)=||x||^2 − R^2 ≤ 0. Repeat Example 2 but keep R symbolic. Watch the gradient of ||x||^2.

Show solution

Let g(\mathbf{x})=\lVert\mathbf{x}\rVert^2−R^2≤0, μ≥0.

L(\mathbf{x},μ)=\tfrac12||\mathbf{x}-\mathbf{a}||^2+μ(||\mathbf{x}||^2−R^2).

Stationarity: (\mathbf{x}-\mathbf{a})+2μ\mathbf{x}=0 ⇒ (1+2μ)\mathbf{x}=\mathbf{a} ⇒ \mathbf{x}=\mathbf{a}/(1+2μ).

Complementary slackness: μ(||\mathbf{x}||^2−R^2)=0.

Case 1 (interior): μ=0 ⇒ \mathbf{x}=\mathbf{a}. Feasible if ||\mathbf{a}||≤R.

Case 2 (boundary): ||\mathbf{x}||=R and μ≥0. Then ||\mathbf{a}||/(1+2μ)=R ⇒ 1+2μ=||\mathbf{a}||/R ⇒ μ=\tfrac12(||\mathbf{a}||/R−1) (requires ||\mathbf{a}||≥R).

Then \mathbf{x}=\mathbf{a}/(||\mathbf{a}||/R)=R\,\mathbf{a}/||\mathbf{a}||.

Final:

\n$$

\mathbf{x}^\*=

\begin{cases}

\mathbf{a}, & ||\mathbf{a}||\le R \\

R\,\mathbf{a}/||\mathbf{a}||, & ||\mathbf{a}||>R

\end{cases}

\quad\text{and}\quad

\mu^\*=

\begin{cases}

0, & ||\mathbf{a}||\le R \\

\tfrac12(||\mathbf{a}||/R-1), & ||\mathbf{a}||>R.

\end{cases}

## Connections

Next steps and related nodes:

- •[Lagrangian Duality](/tech-tree/duality/): Use KKT to derive dual problems, understand weak/strong duality, and interpret μᵢ as shadow prices.

Reinforces prerequisites:

- •Equality-only multipliers: KKT reduces to standard Lagrange multipliers when there are no inequalities (or when all active inequalities are treated like equalities).
- •Convex optimization: In convex problems with Slater’s condition, KKT becomes a complete characterization of global optimality.

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
