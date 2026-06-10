---
title: Lagrangian Duality
description: Dual problems, weak and strong duality. Dual ascent.
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
permalink: /tech-tree/duality/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Lagrangian Duality

OptimizationDifficulty: ★★★★★Depth: 10Unlocks: 0

Dual problems, weak and strong duality. Dual ascent.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Lagrangian function L(x, lambda, nu) as the scalar combining objective and constraint terms via multipliers
- -Dual object: the dual function d(lambda, nu)=inf\_x L(x,lambda,nu) and the derived dual optimization problem (maximize d over multipliers, with lambda>=0 for inequality constraints)

## Key Symbols & Notation

L(x, lambda, nu)d(lambda, nu) = inf\_x L(x, lambda, nu)

## Essential Relationships

- -Weak and strong duality: for any feasible multipliers, d(lambda,nu) is a lower bound on the primal optimum (weak duality); under convexity plus a constraint qualification (e.g., Slater) the dual optimum equals the primal optimum (strong duality)
- -Dual ascent connection: the (sub)gradient of d w.r.t. multipliers equals the constraint residuals, yielding the iterative update lambda <- projection(lambda + step \* constraint\_violation) to maximize d

## Prerequisites (2)

[KKT Conditions6 atoms](/tech-tree/kkt-conditions/)[Lagrange Multipliers5 atoms](/tech-tree/lagrange-multipliers/)

## Referenced by (3)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (3)

[AllocationBusiness

Dual variables give shadow prices - the marginal value of each scarce resource. Duality bridges the optimization math to the economic interpretation of allocation constraints](/business/allocation/)[Shadow PriceBusiness

Shadow prices are dual variables - understanding Lagrangian duality explains why every primal constraint has a corresponding price and why strong duality makes shadow prices actionable](/business/shadow-price/)[resource allocationBusiness

Primal-dual and dual-ascent methods ARE Lagrangian duality applied - the concept description names these methods directly](/business/resource-allocation/)

Advanced Learning Details

### Graph Position

87

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

10

Chain Length

### Cognitive Load

6

Atomic Elements

36

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (13)

- - Lagrangian (as a function of primal variables x and multiplier vector λ) used to form a lower bound on the primal objective via inequality multipliers
- - Lagrangian dual function q(λ) defined as the infimum (over primal variables) of the Lagrangian: q(λ) = inf\_x L(x,λ)
- - Lagrangian dual problem: maximize q(λ) subject to dual feasibility (λ ≥ 0 for inequality constraints)
- - Duality gap: the nonnegative difference between primal optimal value and dual optimal value
- - Weak duality: the principle that any dual feasible value is a lower bound on the primal objective (so dual optimum ≤ primal optimum)
- - Strong duality: the situation (often under convexity + a constraint qualification such as Slater's condition) where primal and dual optima coincide (zero duality gap)
- - Slater's condition (a sufficient constraint qualification for strong duality in convex problems): existence of a strictly feasible primal point
- - Concavity of the dual function q(λ) in λ (regardless of primal convexity)
- - Dual variables interpreted as shadow prices (economic/interpretational meaning of λ components)
- - Subgradient structure of the dual function: relationship between minimizers of L(x,λ) and subgradients of q
- - Primal recovery via argmin of the Lagrangian: x\*(λ) ∈ argmin\_x L(x,λ) gives candidate primal solutions
- - Dual ascent algorithm: iterative (sub)gradient-ascent on q(λ) to find maximizing λ, alternating minimization in x and multiplier updates
- - Projection onto the nonnegative orthant used in updates to enforce λ ≥ 0

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Constrained optimization feels like juggling: you want to minimize an objective while never dropping the constraints. Lagrangian duality turns that juggling act into a different game—choose prices (multipliers) for constraint violation so that the best “priced” solution automatically respects the constraints. The surprising part: those prices also generate guaranteed lower bounds on the true optimum, and in many important cases the bound becomes exact.

TL;DR:

Given a primal minimization problem with constraints, form the Lagrangian L(x,λ,ν)=f(x)+∑iλigi(x)+∑jνjhj(x)L(x,\lambda,\nu)=f(x)+\sum\_i \lambda\_i g\_i(x)+\sum\_j \nu\_j h\_j(x)L(x,λ,ν)=f(x)+∑i​λi​gi​(x)+∑j​νj​hj​(x) with λ≥0\lambda\ge 0λ≥0. The dual function d(λ,ν)=inf⁡xL(x,λ,ν)d(\lambda,\nu)=\inf\_x L(x,\lambda,\nu)d(λ,ν)=infx​L(x,λ,ν) is always a lower bound on the primal optimum (weak duality). The dual problem maximizes this bound over multipliers. Under conditions like Slater’s condition for convex problems, the bound is tight (strong duality). Dual ascent updates multipliers to improve the bound and can solve large problems by exploiting separability and the structure of inf⁡xL\inf\_x Linfx​L.

## What Is Lagrangian Duality?

### The primal problem (what we start with)

A standard constrained minimization problem (the **primal**) is:

minimizexf(x)subject togi(x)≤0,  i=1,…,mhj(x)=0,  j=1,…,p\begin{aligned}
\text{minimize}\_{x} \quad & f(x) \\
\text{subject to} \quad & g\_i(x) \le 0, \; i=1,\dots,m \\
& h\_j(x) = 0, \; j=1,\dots,p
\end{aligned}minimizex​subject to​f(x)gi​(x)≤0,i=1,…,mhj​(x)=0,j=1,…,p​

Here:

- •xxx is the decision variable (can be scalar, vector, or structured object).
- •f(x)f(x)f(x) is the objective.
- •gi(x)≤0g\_i(x) \le 0gi​(x)≤0 are inequality constraints.
- •hj(x)=0h\_j(x)=0hj​(x)=0 are equality constraints.

You already know KKT conditions and Lagrange multipliers. Duality builds on those ideas but changes the emphasis: instead of directly enforcing constraints, we **price** violations.

### The Lagrangian (the key scalar object)

Define the Lagrangian:

L(x,λ,ν)=f(x)+∑i=1mλigi(x)+∑j=1pνjhj(x)L(x,\lambda,\nu) = f(x) + \sum\_{i=1}^m \lambda\_i g\_i(x) + \sum\_{j=1}^p \nu\_j h\_j(x)L(x,λ,ν)=f(x)+i=1∑m​λi​gi​(x)+j=1∑p​νj​hj​(x)

- •λ∈Rm\lambda \in \mathbb{R}^mλ∈Rm are multipliers for inequalities.
- •ν∈Rp\nu \in \mathbb{R}^pν∈Rp are multipliers for equalities.
- •For inequality constraints, we restrict λ≥0\lambda \ge 0λ≥0 (componentwise). This is not cosmetic—it makes the “pricing” consistent.

Intuition:

- •If gi(x)≤0g\_i(x) \le 0gi​(x)≤0 is satisfied, then λigi(x)≤0\lambda\_i g\_i(x) \le 0λi​gi​(x)≤0 (since λi≥0\lambda\_i \ge 0λi​≥0), so the constraint can only *decrease* (or leave unchanged) the Lagrangian.
- •If gi(x)>0g\_i(x) > 0gi​(x)>0 is violated, then λigi(x)>0\lambda\_i g\_i(x) > 0λi​gi​(x)>0, so the Lagrangian penalizes that violation.

This mirrors a familiar idea: “soft constraints” with penalties. But duality is more precise: the penalties are variables you optimize.

### The dual function: best value of the priced problem

Given multipliers (λ,ν)(\lambda,\nu)(λ,ν), consider minimizing the Lagrangian over xxx:

d(λ,ν)=inf⁡xL(x,λ,ν)d(\lambda,\nu) = \inf\_x L(x,\lambda,\nu)d(λ,ν)=xinf​L(x,λ,ν)

This ddd is called the **dual function**.

Why is it an infimum (not necessarily a minimum)? Because for some multipliers the Lagrangian might not attain a minimizer, or might go to −∞-\infty−∞.

Two important facts (we will prove them carefully soon):

1. 1)For any λ≥0\lambda \ge 0λ≥0, d(λ,ν)d(\lambda,\nu)d(λ,ν) is a **lower bound** on the primal optimum value p∗p^\*p∗.
2. 2)d(λ,ν)d(\lambda,\nu)d(λ,ν) is **concave** in (λ,ν)(\lambda,\nu)(λ,ν), even when the primal problem is not convex.

### The dual problem: maximize the best lower bound

If each (λ,ν)(\lambda,\nu)(λ,ν) gives a lower bound, we should pick the best one:

maximizeλ,νd(λ,ν)subject toλ≥0\begin{aligned}
\text{maximize}\_{\lambda,\nu} \quad & d(\lambda,\nu) \\
\text{subject to} \quad & \lambda \ge 0
\end{aligned}maximizeλ,ν​subject to​d(λ,ν)λ≥0​

This is the **Lagrange dual problem**. Its optimal value is denoted d∗d^\*d∗.

### Why duality is worth learning

Duality is not just “another way to write the same thing.” It gives:

- •**Certificates (bounds):** Any feasible dual point (λ,ν)(\lambda,\nu)(λ,ν) immediately certifies a lower bound on p∗p^\*p∗. This is extremely useful in algorithms and in debugging optimization models.
- •**Alternative computation:** Sometimes the primal is hard, while the dual is simpler (fewer variables, decomposes, or has a closed form).
- •**Structure and insight:** Multipliers often have meaning as *shadow prices* (marginal values of constraints).
- •**Algorithms:** Dual ascent, subgradient methods on the dual, ADMM, and many distributed optimization methods are built from the dual view.

We’ll proceed slowly: first we’ll make the “lower bound” statement completely concrete; then we’ll talk about when the bound becomes tight; then we’ll turn that into an algorithm.

## Core Mechanic 1 — The Dual Function as an Infimum (and Why It Lower-Bounds the Primal)

### Step 1: Fix multipliers and look at L(x,λ,ν)L(x,\lambda,\nu)L(x,λ,ν)

For a fixed (λ,ν)(\lambda,\nu)(λ,ν) with λ≥0\lambda\ge 0λ≥0, the Lagrangian is just a scalar function of xxx:

L(x,λ,ν)=f(x)+∑iλigi(x)+∑jνjhj(x).L(x,\lambda,\nu)= f(x) + \sum\_i \lambda\_i g\_i(x) + \sum\_j \nu\_j h\_j(x).L(x,λ,ν)=f(x)+i∑​λi​gi​(x)+j∑​νj​hj​(x).

Now imagine two categories of xxx:

- •**Feasible**: satisfies gi(x)≤0g\_i(x)\le 0gi​(x)≤0 and hj(x)=0h\_j(x)=0hj​(x)=0.
- •**Infeasible**: violates at least one constraint.

For feasible xxx, we can compare L(x,λ,ν)L(x,\lambda,\nu)L(x,λ,ν) and f(x)f(x)f(x).

### Step 2: For feasible xxx, the Lagrangian never exceeds the objective

If xxx is feasible, then:

- •Each gi(x)≤0g\_i(x)\le 0gi​(x)≤0 and each λi≥0\lambda\_i\ge 0λi​≥0 so λigi(x)≤0\lambda\_i g\_i(x)\le 0λi​gi​(x)≤0.
- •Each hj(x)=0h\_j(x)=0hj​(x)=0 so νjhj(x)=0\nu\_j h\_j(x)=0νj​hj​(x)=0.

Therefore:

L(x,λ,ν)=f(x)+∑iλigi(x)+∑jνjhj(x)≤f(x).L(x,\lambda,\nu) = f(x) + \sum\_i \lambda\_i g\_i(x) + \sum\_j \nu\_j h\_j(x)
\le f(x).L(x,λ,ν)=f(x)+i∑​λi​gi​(x)+j∑​νj​hj​(x)≤f(x).

This inequality is the heart of weak duality.

### Step 3: Take the best (lowest) Lagrangian value over all xxx

By definition,

d(λ,ν)=inf⁡xL(x,λ,ν).d(\lambda,\nu) = \inf\_x L(x,\lambda,\nu).d(λ,ν)=xinf​L(x,λ,ν).

The infimum over *all* xxx is certainly no larger than the value at any particular feasible xxx:

d(λ,ν)≤L(x,λ,ν)≤f(x)for any feasible x.d(\lambda,\nu) \le L(x,\lambda,\nu) \le f(x) \quad \text{for any feasible } x.d(λ,ν)≤L(x,λ,ν)≤f(x)for any feasible x.

Now take the infimum over all feasible xxx on the right-hand side. The best feasible objective value is the primal optimum value p∗p^\*p∗:

d(λ,ν)≤p∗for all λ≥0.d(\lambda,\nu) \le p^\* \quad \text{for all } \lambda\ge 0.d(λ,ν)≤p∗for all λ≥0.

This is **weak duality**.

> Weak duality: For a primal minimization problem, any dual-feasible (λ,ν)(\lambda,\nu)(λ,ν) gives a lower bound on the primal optimal value.

### Pause point #1 (tiny sanity-check)

Before moving on, check that you can literally compute a dual function once.

Consider the 1D problem:

minimizex∈Rx2subject tox≥1\begin{aligned}
\text{minimize}\_{x\in\mathbb{R}} \quad & x^2 \\
\text{subject to} \quad & x \ge 1
\end{aligned}minimizex∈R​subject to​x2x≥1​

Rewrite the constraint as g(x)=1−x≤0g(x)=1-x\le 0g(x)=1−x≤0.

- •Lagrangian: L(x,λ)=x2+λ(1−x)L(x,\lambda)=x^2 + \lambda(1-x)L(x,λ)=x2+λ(1−x) with λ≥0\lambda\ge 0λ≥0.
- •Dual function: d(λ)=inf⁡x(x2+λ(1−x))d(\lambda)=\inf\_x \big(x^2 + \lambda(1-x)\big)d(λ)=infx​(x2+λ(1−x)).

Try computing d(λ)d(\lambda)d(λ) by minimizing over xxx (complete the square or set derivative to zero). Then compare max⁡λ≥0d(λ)\max\_{\lambda\ge 0} d(\lambda)maxλ≥0​d(λ) with the primal optimum p∗=1p^\*=1p∗=1.

(We’ll do a closely related worked example later, but you should attempt this now—this is the first “feel” of inf⁡x\inf\_xinfx​.)

### The duality gap

Define:

- •Primal optimum value: p∗p^\*p∗
- •Dual optimum value: d∗d^\*d∗

Weak duality implies:

d∗≤p∗.d^\* \le p^\*.d∗≤p∗.

The difference p∗−d∗p^\* - d^\*p∗−d∗ is the **duality gap**.

- •If p∗=d∗p^\* = d^\*p∗=d∗, duality is *tight* and we have **strong duality**.
- •If p∗>d∗p^\* > d^\*p∗>d∗, there is a positive gap.

### Why the dual function is concave (important for optimization)

This may feel counterintuitive: d(λ,ν)=inf⁡xL(x,λ,ν)d(\lambda,\nu)=\inf\_x L(x,\lambda,\nu)d(λ,ν)=infx​L(x,λ,ν), an infimum of functions linear in (λ,ν)(\lambda,\nu)(λ,ν). But the infimum of affine functions is concave.

Proof sketch (worth internalizing): for each fixed xxx, define

ϕx(λ,ν)=L(x,λ,ν).\phi\_x(\lambda,\nu)=L(x,\lambda,\nu).ϕx​(λ,ν)=L(x,λ,ν).

As a function of (λ,ν)(\lambda,\nu)(λ,ν), ϕx\phi\_xϕx​ is affine (linear + constant) because it is f(x)+λTg(x)+νTh(x)f(x) + \lambda^T g(x) + \nu^T h(x)f(x)+λTg(x)+νTh(x).

Then

d(λ,ν)=inf⁡xϕx(λ,ν).d(\lambda,\nu) = \inf\_x \phi\_x(\lambda,\nu).d(λ,ν)=xinf​ϕx​(λ,ν).

The pointwise infimum of affine functions is concave. Concretely, for $0\le t\le 1$:

d(t(λ1,ν1)+(1−t)(λ2,ν2))=inf⁡xϕx(t(λ1,ν1)+(1−t)(λ2,ν2))=inf⁡x(tϕx(λ1,ν1)+(1−t)ϕx(λ2,ν2))≥tinf⁡xϕx(λ1,ν1)+(1−t)inf⁡xϕx(λ2,ν2)=td(λ1,ν1)+(1−t)d(λ2,ν2).\begin{aligned}
d(t(\lambda\_1,\nu\_1)+(1-t)(\lambda\_2,\nu\_2))
&= \inf\_x \phi\_x(t(\lambda\_1,\nu\_1)+(1-t)(\lambda\_2,\nu\_2)) \\
&= \inf\_x \left(t\phi\_x(\lambda\_1,\nu\_1)+(1-t)\phi\_x(\lambda\_2,\nu\_2)\right) \\
&\ge t\inf\_x \phi\_x(\lambda\_1,\nu\_1) + (1-t)\inf\_x \phi\_x(\lambda\_2,\nu\_2) \\
&= t d(\lambda\_1,\nu\_1) + (1-t) d(\lambda\_2,\nu\_2).
\end{aligned}d(t(λ1​,ν1​)+(1−t)(λ2​,ν2​))​=xinf​ϕx​(t(λ1​,ν1​)+(1−t)(λ2​,ν2​))=xinf​(tϕx​(λ1​,ν1​)+(1−t)ϕx​(λ2​,ν2​))≥txinf​ϕx​(λ1​,ν1​)+(1−t)xinf​ϕx​(λ2​,ν2​)=td(λ1​,ν1​)+(1−t)d(λ2​,ν2​).​

That inequality step is the key: infimum of a sum is ≥ sum of infima.

### Interactive-canvas moment: visualize “lower bound curves”

If your tech tree platform supports an interactive plot, this is the perfect place to attach it.

Suggested interaction:

- •Pick a simple primal (like minimizing a quadratic with a linear inequality).
- •For each λ≥0\lambda\ge 0λ≥0, compute d(λ)d(\lambda)d(λ).
- •Plot the curve d(λ)d(\lambda)d(λ) and show the horizontal line at p∗p^\*p∗.

What you should see:

- •For small λ\lambdaλ, the penalty is weak; the infimum may be far below p∗p^\*p∗.
- •As λ\lambdaλ changes, d(λ)d(\lambda)d(λ) rises (not necessarily monotonically, but it has a concave “cap” shape).
- •At the maximizing λ∗\lambda^\*λ∗, d(λ∗)d(\lambda^\*)d(λ∗) is the best lower bound; in strong-duality cases it meets p∗p^\*p∗.

This visualization makes the definition d(λ)=inf⁡xL(x,λ)d(\lambda)=\inf\_x L(x,\lambda)d(λ)=infx​L(x,λ) feel less abstract: you are literally pushing up the best guaranteed lower bound by tuning prices.

## Core Mechanic 2 — Strong Duality: When the Lower Bound Becomes Exact

Weak duality always holds, but strong duality is where duality becomes a solving tool, not just a bounding tool.

### Convexity is the enabling assumption

Strong duality is most commonly guaranteed in **convex optimization** problems of the form:

minimizexf(x)subject togi(x)≤0,  i=1,…,mAx=b\begin{aligned}
\text{minimize}\_x \quad & f(x) \\
\text{subject to} \quad & g\_i(x) \le 0, \; i=1,\dots,m \\
& Ax=b
\end{aligned}minimizex​subject to​f(x)gi​(x)≤0,i=1,…,mAx=b​

where:

- •fff is convex,
- •each gig\_igi​ is convex,
- •Ax=bAx=bAx=b is affine.

(Equality constraints more generally can be affine functions hj(x)=0h\_j(x)=0hj​(x)=0; writing them as Ax=bAx=bAx=b is a clean special case.)

Convexity matters because it prevents “hidden” nonconvex geometry that can create a duality gap.

### Slater’s condition (the standard constraint qualification)

A widely used sufficient condition for strong duality is **Slater’s condition**:

For convex problems with inequality constraints gi(x)≤0g\_i(x)\le 0gi​(x)≤0 and affine equalities, if there exists a point x~\tilde{x}x~ such that

- •gi(x~)<0g\_i(\tilde{x}) < 0gi​(x~)<0 for all iii (strict feasibility),
- •and Ax~=bA\tilde{x}=bAx~=b,

then strong duality holds and KKT conditions are necessary and sufficient.

So Slater is an “interior point exists” condition.

Why do we need it? Intuitively:

- •If the feasible set has nonempty interior (relative to the equality constraints), multipliers behave nicely.
- •If feasible points only exist on the boundary in a fragile way, multipliers may blow up or fail to represent the problem tightly.

### What strong duality gives you (operationally)

If strong duality holds:

p∗=d∗.p^\* = d^\*.p∗=d∗.

Moreover, there exist optimal multipliers (λ∗,ν∗)(\lambda^\*,\nu^\*)(λ∗,ν∗) such that:

- •d(λ∗,ν∗)=p∗d(\lambda^\*,\nu^\*) = p^\*d(λ∗,ν∗)=p∗
- •and a primal optimal solution x∗x^\*x∗ together with (λ∗,ν∗)(\lambda^\*,\nu^\*)(λ∗,ν∗) satisfy the KKT conditions:
- •Primal feasibility
- •Dual feasibility (λ∗≥0\lambda^\*\ge 0λ∗≥0)
- •Complementary slackness (λi∗gi(x∗)=0\lambda\_i^\* g\_i(x^\*)=0λi∗​gi​(x∗)=0)
- •Stationarity (∇f(x∗)+∑iλi∗∇gi(x∗)+∑jνj∗∇hj(x∗)=0\nabla f(x^\*) + \sum\_i \lambda\_i^\* \nabla g\_i(x^\*) + \sum\_j \nu\_j^\* \nabla h\_j(x^\*) = 0∇f(x∗)+∑i​λi∗​∇gi​(x∗)+∑j​νj∗​∇hj​(x∗)=0)

In other words, duality explains *why* KKT works: it’s the optimality condition for a saddle point of the Lagrangian.

### Saddle-point picture (a unifying mental model)

Think of the Lagrangian as a two-player game:

- •Player X chooses xxx to minimize L(x,λ,ν)L(x,\lambda,\nu)L(x,λ,ν).
- •Player Λ chooses (λ,ν)(\lambda,\nu)(λ,ν) (with λ≥0\lambda\ge 0λ≥0) to maximize L(x,λ,ν)L(x,\lambda,\nu)L(x,λ,ν).

The primal problem is like:

p∗=inf⁡x feasiblef(x).p^\* = \inf\_{x \text{ feasible}} f(x).p∗=x feasibleinf​f(x).

The dual problem is:

d∗=sup⁡λ≥0,νinf⁡xL(x,λ,ν).d^\* = \sup\_{\lambda\ge 0,\nu} \inf\_x L(x,\lambda,\nu).d∗=λ≥0,νsup​xinf​L(x,λ,ν).

A saddle point (x∗,λ∗,ν∗)(x^\*,\lambda^\*,\nu^\*)(x∗,λ∗,ν∗) satisfies:

L(x∗,λ,ν)≤L(x∗,λ∗,ν∗)≤L(x,λ∗,ν∗)L(x^\*,\lambda,\nu) \le L(x^\*,\lambda^\*,\nu^\*) \le L(x,\lambda^\*,\nu^\*)L(x∗,λ,ν)≤L(x∗,λ∗,ν∗)≤L(x,λ∗,ν∗)

for all feasible multipliers and all xxx.

- •The right inequality says x∗x^\*x∗ minimizes the Lagrangian under optimal multipliers.
- •The left inequality says optimal multipliers make the Lagrangian as large as possible at x∗x^\*x∗.

Strong duality is closely related to the existence of such a saddle point.

### Pause point #2 (Slater sanity-check)

Decide whether Slater’s condition holds.

Problem A:

minimizex∈Rxsubject tox2≤1\begin{aligned}
\text{minimize}\_{x\in\mathbb{R}} \quad & x \\
\text{subject to} \quad & x^2 \le 1
\end{aligned}minimizex∈R​subject to​xx2≤1​

Is there a strictly feasible point? Yes: x=0x=0x=0 gives $0<1$. So Slater holds.

Problem B:

minimizex∈Rxsubject tox2≤0\begin{aligned}
\text{minimize}\_{x\in\mathbb{R}} \quad & x \\
\text{subject to} \quad & x^2 \le 0
\end{aligned}minimizex∈R​subject to​xx2≤0​

Feasible set is only {0}\{0\}{0}. There is no xxx with x2<0x^2<0x2<0, so Slater fails.

Take 30 seconds to reflect: both problems are convex, but B has a “boundary-only” feasible set.

Slater failing does *not* automatically mean strong duality fails, but it removes a key guarantee.

### Strong duality is not universal

For nonconvex problems, duality can be loose:

- •Dual provides a lower bound (still true).
- •But d∗d^\*d∗ can be strictly less than p∗p^\*p∗.

This is why in combinatorial optimization, one often uses duality as a **relaxation**: solve the dual (or a related convex relaxation) to get bounds even if you can’t solve the primal exactly.

### A practical consequence: dual optimality = optimal certificate

When strong duality holds, a dual optimal solution (λ∗,ν∗)(\lambda^\*,\nu^\*)(λ∗,ν∗) is a certificate of optimality:

- •If you have a candidate primal feasible xxx and a dual feasible (λ,ν)(\lambda,\nu)(λ,ν) such that f(x)=d(λ,ν)f(x)=d(\lambda,\nu)f(x)=d(λ,ν), then you have proven global optimality (because d(λ,ν)≤p∗≤f(x)d(\lambda,\nu)\le p^\*\le f(x)d(λ,ν)≤p∗≤f(x)).

This “sandwich” proof is one of the most useful ways to *trust* an optimizer.

## Application/Connection — Dual Ascent and How Duality Becomes an Algorithm

Duality is not only theory; it directly yields optimization methods.

### The dual problem as concave maximization

The dual problem is:

max⁡λ≥0,ν  d(λ,ν)\max\_{\lambda\ge 0,\nu} \; d(\lambda,\nu)λ≥0,νmax​d(λ,ν)

with ddd concave. So we are **maximizing a concave function**, which is the “nice” direction (equivalently, minimizing a convex function −d-d−d).

But there’s a catch: d(λ,ν)d(\lambda,\nu)d(λ,ν) is defined via an infimum over xxx. It may be nonsmooth.

### Computing a subgradient of the dual function

Suppose for given (λ,ν)(\lambda,\nu)(λ,ν) we can find

x(λ,ν)∈arg⁡min⁡xL(x,λ,ν).x(\lambda,\nu) \in \arg\min\_x L(x,\lambda,\nu).x(λ,ν)∈argxmin​L(x,λ,ν).

Then a subgradient of ddd is given by constraint residuals at that minimizing xxx:

- •For inequalities: ∂λid(λ,ν)\partial\_{\lambda\_i} d(\lambda,\nu)∂λi​​d(λ,ν) includes gi(x(λ,ν))g\_i(x(\lambda,\nu))gi​(x(λ,ν)).
- •For equalities: ∂νjd(λ,ν)\partial\_{\nu\_j} d(\lambda,\nu)∂νj​​d(λ,ν) includes hj(x(λ,ν))h\_j(x(\lambda,\nu))hj​(x(λ,ν)).

Intuition:

- •If a constraint is violated (gi(x)>0g\_i(x)>0gi​(x)>0), increasing λi\lambda\_iλi​ should raise the penalty and thus raise the lower bound.
- •If a constraint is satisfied with slack (gi(x)<0g\_i(x)<0gi​(x)<0), increasing λi\lambda\_iλi​ may actually lower ddd (and the optimizer will keep λi\lambda\_iλi​ from growing).

### Dual ascent updates

A basic dual ascent / subgradient method:

1. 1)Given (λk,νk)(\lambda^k,\nu^k)(λk,νk), compute

xk∈arg⁡min⁡xL(x,λk,νk).x^k \in \arg\min\_x L(x,\lambda^k,\nu^k).xk∈argxmin​L(x,λk,νk).

2. 2)Update multipliers using residuals:

λk+1=Πλ≥0(λk+αk g(xk))\lambda^{k+1} = \Pi\_{\lambda\ge 0}\big(\lambda^k + \alpha\_k\, g(x^k)\big)λk+1=Πλ≥0​(λk+αk​g(xk))

νk+1=νk+αk h(xk)\nu^{k+1} = \nu^k + \alpha\_k\, h(x^k)νk+1=νk+αk​h(xk)

Where:

- •g(xk)g(x^k)g(xk) is the vector (g1(xk),…,gm(xk))(g\_1(x^k),\dots,g\_m(x^k))(g1​(xk),…,gm​(xk)).
- •h(xk)h(x^k)h(xk) is the vector (h1(xk),…,hp(xk))(h\_1(x^k),\dots,h\_p(x^k))(h1​(xk),…,hp​(xk)).
- •Πλ≥0\Pi\_{\lambda\ge 0}Πλ≥0​ projects onto the nonnegative orthant (componentwise max with 0).
- •αk\alpha\_kαk​ is a step size.

Why projection only for λ\lambdaλ? Because dual feasibility requires λ≥0\lambda\ge 0λ≥0 for inequalities, but ν\nuν is free.

### How to choose step sizes (briefly)

Subgradient methods are sensitive to step sizes.

Common choices:

- •Constant step size: αk=α\alpha\_k=\alphaαk​=α (often gives a neighborhood around optimum).
- •Diminishing step size: αk→0\alpha\_k \to 0αk​→0 with ∑kαk=∞\sum\_k \alpha\_k=\infty∑k​αk​=∞ (classic convergence conditions for subgradient methods).

In practice, many systems use more advanced variants (accelerations, adaptive rules) or different splitting methods (e.g., ADMM) that are also rooted in the Lagrangian.

### Why dual ascent can be efficient: separability and decomposition

A major payoff occurs when the Lagrangian separates over components of xxx.

Suppose x=(x1,…,xN)x=(x\_1,\dots,x\_N)x=(x1​,…,xN​) and

f(x)=∑n=1Nfn(xn)f(x)=\sum\_{n=1}^N f\_n(x\_n)f(x)=n=1∑N​fn​(xn​)

and constraints couple them only through a simple sum, e.g.

∑n=1NAnxn=b.\sum\_{n=1}^N A\_n x\_n = b.n=1∑N​An​xn​=b.

Then

L(x,ν)=∑n=1Nfn(xn)+νT(∑n=1NAnxn−b)=∑n=1N(fn(xn)+νTAnxn)−νTb.L(x,\nu)=\sum\_{n=1}^N f\_n(x\_n) + \nu^T\left(\sum\_{n=1}^N A\_n x\_n - b\right)
= \sum\_{n=1}^N \left(f\_n(x\_n)+\nu^T A\_n x\_n\right) - \nu^T b.L(x,ν)=n=1∑N​fn​(xn​)+νT(n=1∑N​An​xn​−b)=n=1∑N​(fn​(xn​)+νTAn​xn​)−νTb.

Now the minimization over xxx splits:

inf⁡xL(x,ν)=∑n=1Ninf⁡xn(fn(xn)+νTAnxn)−νTb.\inf\_x L(x,\nu) = \sum\_{n=1}^N \inf\_{x\_n}\left(f\_n(x\_n)+\nu^T A\_n x\_n\right) - \nu^T b.xinf​L(x,ν)=n=1∑N​xn​inf​(fn​(xn​)+νTAn​xn​)−νTb.

So computing d(ν)d(\nu)d(ν) is NNN smaller problems, often parallelizable.

This is the conceptual foundation of distributed optimization: multipliers coordinate many local optimizations.

### Connecting back to KKT

If strong duality holds and the method converges to (λ∗,ν∗)(\lambda^\*,\nu^\*)(λ∗,ν∗) with corresponding x∗x^\*x∗ minimizing L(⋅,λ∗,ν∗)L(\cdot,\lambda^\*,\nu^\*)L(⋅,λ∗,ν∗), then KKT conditions emerge:

- •Stationarity: x∗x^\*x∗ minimizes LLL.
- •Complementary slackness: in the limit, multipliers grow only where constraints are tight.
- •Feasibility: residuals driven toward 0 by multiplier updates.

This is a clean story:

- •KKT describes optimality.
- •Dual ascent is one route to satisfy KKT by iteratively tuning multipliers.

### A second interactive-canvas moment (algorithm intuition)

If you can animate iterations:

- •Show a point xkx^kxk moving in primal space (perhaps unconstrained minimizer of LLL).
- •Show λk\lambda^kλk changing over time.
- •Overlay the constraint boundary g(x)=0g(x)=0g(x)=0.

What learners should observe:

- •If xkx^kxk violates the constraint, λ\lambdaλ increases, “tilting” LLL so the next minimizer is pushed back toward feasibility.
- •If xkx^kxk is strictly feasible, λ\lambdaλ may decrease toward 0.

This makes dual ascent feel like an automatic constraint-enforcement mechanism driven by prices.

## Worked Examples (3)

### Dual function and dual optimum for a 1D quadratic with an inequality

Primal:

minimizex∈Rx2subject tox≥1\begin{aligned}
\text{minimize}\_{x\in\mathbb{R}} \quad & x^2 \\
\text{subject to} \quad & x \ge 1
\end{aligned}minimizex∈R​subject to​x2x≥1​

Rewrite x≥1x\ge 1x≥1 as g(x)=1−x≤0g(x)=1-x\le 0g(x)=1−x≤0.

1. Form the Lagrangian (single multiplier):

   \n$L(x,λ)=x2+λ(1−x),λ≥0.L(x,\lambda)=x^2+\lambda(1-x),\quad \lambda\ge 0.L(x,λ)=x2+λ(1−x),λ≥0.$
2. Compute the dual function:

   \n$d(λ)=inf⁡x(x2−λx+λ).d(\lambda)=\inf\_x \left(x^2-\lambda x + \lambda\right).d(λ)=infx​(x2−λx+λ).$
3. Minimize the quadratic over x by setting derivative to zero:

   \n$ddx(x2−λx+λ)=2x−λ=0⇒x∗(λ)=λ2.\frac{d}{dx}\left(x^2-\lambda x + \lambda\right)=2x-\lambda=0 \Rightarrow x^\*(\lambda)=\frac{\lambda}{2}.dxd​(x2−λx+λ)=2x−λ=0⇒x∗(λ)=2λ​.$
4. Plug back in to get the infimum value:

   \n$$

   \begin{aligned}

   d(\lambda)

   &= \left(\frac{\lambda}{2}\right)^2 - \lambda\left(\frac{\lambda}{2}\right) + \lambda \\

   &= \frac{\lambda^2}{4} - \frac{\lambda^2}{2} + \lambda \\

   &= -\frac{\lambda^2}{4}+\lambda.

   \end{aligned}
5. Solve the dual problem:

   \n$max⁡λ≥0  −λ24+λ.\max\_{\lambda\ge 0}\; -\frac{\lambda^2}{4}+\lambda.maxλ≥0​−4λ2​+λ.$
6. This is a concave parabola. Differentiate:

   \n$ddλ(−λ24+λ)=−λ2+1.\frac{d}{d\lambda}\left(-\frac{\lambda^2}{4}+\lambda\right)=-\frac{\lambda}{2}+1.dλd​(−4λ2​+λ)=−2λ​+1.$
7. Set to zero: −λ/2+1=0⇒λ∗=2-\lambda/2+1=0 \Rightarrow \lambda^\*=2−λ/2+1=0⇒λ∗=2 (and it satisfies λ≥0\lambda\ge 0λ≥0).
8. Compute the dual optimum value:

   \n$d∗=d(2)=−44+2=1.d^\*=d(2)=-\frac{4}{4}+2=1.d∗=d(2)=−44​+2=1.$
9. Compute primal optimum for comparison: constraint forces x≥1x\ge 1x≥1, and x2x^2x2 is minimized at x=1x=1x=1, so p∗=1p^\*=1p∗=1.

**Insight:** Here d∗=p∗d^\*=p^\*d∗=p∗, so strong duality holds (the problem is convex and Slater holds since e.g. x=2x=2x=2 gives strict feasibility $1-2<0).Alsonoticethemeaningof). Also notice the meaning of ).Alsonoticethemeaningof\lambda^*=2$: it is the price that makes the unconstrained minimizer of $L$ land exactly at the boundary $x=1$ (since $x^*(\lambda)=\lambda/2$).

### Deriving the dual of a quadratic program with an equality constraint

Primal (a simple equality-constrained QP):

minimizex∈Rn12xTQx+cTxsubject toAx=b\begin{aligned}
\text{minimize}\_{x\in\mathbb{R}^n} \quad & \frac{1}{2}x^T Q x + c^T x \\
\text{subject to} \quad & Ax=b
\end{aligned}minimizex∈Rn​subject to​21​xTQx+cTxAx=b​

Assume Q≻0Q\succ 0Q≻0 (positive definite), so the objective is strictly convex and the minimizer is unique for each \(\nu\).

1. Form the Lagrangian (only equality multipliers):

   \n$L(x,ν)=12xTQx+cTx+νT(Ax−b).L(x,\nu)=\frac{1}{2}x^TQx + c^T x + \nu^T(Ax-b).L(x,ν)=21​xTQx+cTx+νT(Ax−b).$
2. Compute the dual function:

   \n$d(ν)=inf⁡xL(x,ν).d(\nu)=\inf\_x L(x,\nu).d(ν)=infx​L(x,ν).$
3. Minimize over x by stationarity (differentiate w.r.t. x and set to 0):

   \n$∇xL(x,ν)=Qx+c+ATν=0.\nabla\_x L(x,\nu)=Qx+c+A^T\nu=0.∇x​L(x,ν)=Qx+c+ATν=0.$
4. Solve for the minimizing x as a function of \(\nu\):

   \n$x∗(ν)=−Q−1(c+ATν).x^\*(\nu)=-Q^{-1}(c+A^T\nu).x∗(ν)=−Q−1(c+ATν).$
5. Plug back into the Lagrangian. First expand:

   \n$$

   \begin{aligned}

   L(x,\nu)

   &=\frac{1}{2}x^TQx + (c+A^T\nu)^T x - \nu^T b.

   \end{aligned}
6. Use the standard quadratic minimization identity: for Q≻0Q\succ 0Q≻0,

   \n$inf⁡x(12xTQx+qTx)=−12qTQ−1q,\inf\_x \left(\frac{1}{2}x^TQx + q^T x\right) = -\frac{1}{2} q^T Q^{-1} q,infx​(21​xTQx+qTx)=−21​qTQ−1q,$

   \nattained at x=−Q−1qx=-Q^{-1}qx=−Q−1q.

   Here q=(c+ATν)q=(c+A^T\nu)q=(c+ATν).
7. Therefore:

   \n$$

   \begin{aligned}

   d(\nu)

   &= -\frac{1}{2}(c+A^T\nu)^T Q^{-1}(c+A^T\nu) - \nu^T b.

   \end{aligned}
8. Write the dual problem:

   \n$max⁡ν∈Rp  −12(c+ATν)TQ−1(c+ATν)−νTb.\max\_{\nu\in\mathbb{R}^p}\; -\frac{1}{2}(c+A^T\nu)^T Q^{-1}(c+A^T\nu) - \nu^T b.maxν∈Rp​−21​(c+ATν)TQ−1(c+ATν)−νTb.$
9. Optionally expand into a standard concave quadratic form in \(\nu\):

   \n$$

   \begin{aligned}

   (c+A^T\nu)^T Q^{-1}(c+A^T\nu)

   = c^TQ^{-1}c + 2\nu^T A Q^{-1}c + \nu^T A Q^{-1} A^T \nu.

   \end{aligned}

   So
   \n$$
   \begin{aligned}
   d(\nu)= -\frac{1}{2}\nu^T(AQ^{-1}A^T)\nu - \nu^T(AQ^{-1}c + b) - \frac{1}{2}c^TQ^{-1}c.
   \end{aligned}

**Insight:** This example shows the typical dual pattern: (1) build LLL, (2) compute ddd by eliminating xxx via an infimum, and (3) get a concave maximization over multipliers. The matrix AQ−1ATAQ^{-1}A^TAQ−1AT governs the dual curvature. When the primal is large but ppp (number of equalities) is small, the dual can be much cheaper.

### One iteration of dual ascent for an inequality-constrained problem

Primal:

minimizex∈R(x−3)2subject tox≤1\begin{aligned}
\text{minimize}\_{x\in\mathbb{R}} \quad & (x-3)^2 \\
\text{subject to} \quad & x \le 1
\end{aligned}minimizex∈R​subject to​(x−3)2x≤1​

Rewrite as g(x)=x−1≤0g(x)=x-1\le 0g(x)=x−1≤0. Lagrangian: L(x,λ)=(x−3)2+λ(x−1)L(x,\lambda)=(x-3)^2+\lambda(x-1)L(x,λ)=(x−3)2+λ(x−1), λ≥0\lambda\ge 0λ≥0.

We’ll run one dual-ascent step with step size α=0.5\alpha=0.5α=0.5, starting from λ0=0\lambda^0=0λ0=0.

1. Given λ0=0\lambda^0=0λ0=0, minimize L(x,λ0)L(x,\lambda^0)L(x,λ0) over x:

   \n$L(x,0)=(x−3)2.L(x,0)=(x-3)^2.L(x,0)=(x−3)2.$

   Minimizer is x0=3x^0=3x0=3.
2. Compute constraint residual at x0x^0x0:

   \n$g(x0)=x0−1=2>0,g(x^0)=x^0-1=2>0,g(x0)=x0−1=2>0,$

   so the constraint is violated.
3. Update the multiplier using projected ascent:

   \n$λ1=max⁡{0,λ0+αg(x0)}=max⁡{0,0+0.5⋅2}=1.\lambda^{1}=\max\{0,\lambda^0+\alpha g(x^0)\}=\max\{0,0+0.5\cdot 2\}=1.λ1=max{0,λ0+αg(x0)}=max{0,0+0.5⋅2}=1.$
4. Now (to see the effect), compute the next primal minimizer for λ1=1\lambda^1=1λ1=1:

   \nMinimize L(x,1)=(x−3)2+(x−1)L(x,1)=(x-3)^2 + (x-1)L(x,1)=(x−3)2+(x−1).

   Differentiate:

   \n$ddx((x−3)2+x−1)=2(x−3)+1=2x−5.\frac{d}{dx}\left((x-3)^2+x-1\right)=2(x-3)+1=2x-5.dxd​((x−3)2+x−1)=2(x−3)+1=2x−5.$

   Set to zero: $2x-5=0 \Rightarrow x^1=2.5$.

   Still infeasible, but closer to the constraint boundary x≤1x\le 1x≤1 than 3.

**Insight:** Dual ascent increases λ\lambdaλ when constraints are violated. That increase changes the unconstrained minimizer of LLL, pushing the next xxx toward feasibility. With proper stepsizes (and under convexity/regularity), iterating this can drive residuals down and converge to the constrained optimum.

## Key Takeaways

- ✓

  The Lagrangian L(x,λ,ν)=f(x)+λTg(x)+νTh(x)L(x,\lambda,\nu)=f(x)+\lambda^T g(x)+\nu^T h(x)L(x,λ,ν)=f(x)+λTg(x)+νTh(x) combines objective and constraints using multipliers, with λ≥0\lambda\ge 0λ≥0 for inequalities.
- ✓

  The dual function d(λ,ν)=inf⁡xL(x,λ,ν)d(\lambda,\nu)=\inf\_x L(x,\lambda,\nu)d(λ,ν)=infx​L(x,λ,ν) is always a **lower bound** on the primal optimum value p∗p^\*p∗ when λ≥0\lambda\ge 0λ≥0 (weak duality).
- ✓

  The dual problem max⁡λ≥0,νd(λ,ν)\max\_{\lambda\ge 0,\nu} d(\lambda,\nu)maxλ≥0,ν​d(λ,ν) chooses the tightest lower bound; its value d∗d^\*d∗ satisfies d∗≤p∗d^\*\le p^\*d∗≤p∗.
- ✓

  Even if the primal is nonconvex, the dual function is concave because it is the pointwise infimum of affine functions in (λ,ν)(\lambda,\nu)(λ,ν).
- ✓

  In convex problems, Slater’s condition (existence of a strictly feasible point) is a standard sufficient condition for strong duality and KKT necessity/sufficiency.
- ✓

  When strong duality holds, matching primal/dual values provide a certificate of optimality: d(λ,ν)≤p∗≤f(x)d(\lambda,\nu)\le p^\*\le f(x)d(λ,ν)≤p∗≤f(x), and equality proves optimality.
- ✓

  Dual ascent (subgradient ascent on ddd) updates multipliers using constraint residuals; projection enforces λ≥0\lambda\ge 0λ≥0.
- ✓

  Duality becomes especially powerful when inf⁡xL\inf\_x Linfx​L decomposes across components of xxx, enabling parallel and distributed optimization.

## Common Mistakes

- ✗

  Forgetting the sign restriction λ≥0\lambda\ge 0λ≥0 for inequality constraints, which breaks the lower-bound (weak duality) argument.
- ✗

  Confusing d(λ,ν)=inf⁡xL(x,λ,ν)d(\lambda,\nu)=\inf\_x L(x,\lambda,\nu)d(λ,ν)=infx​L(x,λ,ν) with min⁡xf(x)\min\_x f(x)minx​f(x) or with the constrained minimum—ddd is an unconstrained infimum over xxx of the Lagrangian.
- ✗

  Assuming strong duality always holds; without convexity + a constraint qualification (e.g., Slater), the duality gap can be positive.
- ✗

  Running dual ascent without projection on λ\lambdaλ or with unsuitable step sizes, leading to divergence or oscillation (common with nonsmooth dual functions).

## Practice

easy

Compute the dual function for the problem: minimize x2x^2x2 subject to x≤2x\le 2x≤2. Then find the dual optimum value and compare to the primal optimum.

**Hint:** Write the constraint as g(x)=x−2≤0g(x)=x-2\le 0g(x)=x−2≤0. Form L(x,λ)=x2+λ(x−2)L(x,\lambda)=x^2+\lambda(x-2)L(x,λ)=x2+λ(x−2) with λ≥0\lambda\ge 0λ≥0. Minimize the quadratic in xxx to get d(λ)d(\lambda)d(λ), then maximize over λ≥0\lambda\ge 0λ≥0.

Show solution

Constraint x≤2x\le 2x≤2 means g(x)=x−2≤0g(x)=x-2\le 0g(x)=x−2≤0.

Lagrangian: L(x,λ)=x2+λ(x−2)L(x,\lambda)=x^2+\lambda(x-2)L(x,λ)=x2+λ(x−2).

Dual function:

d(λ)=inf⁡x(x2+λx−2λ).d(\lambda)=\inf\_x (x^2+\lambda x-2\lambda).d(λ)=xinf​(x2+λx−2λ).

Stationarity: $2x+\lambda=0 \Rightarrow x^\*(\lambda)=-\lambda/2$.

Plug in:

d(λ)=(−λ2)2+λ(−λ2)−2λ=λ24−λ22−2λ=−λ24−2λ.\begin{aligned}
d(\lambda)
&= \left(-\frac{\lambda}{2}\right)^2 + \lambda\left(-\frac{\lambda}{2}\right) - 2\lambda \\
&= \frac{\lambda^2}{4}-\frac{\lambda^2}{2}-2\lambda \\
&= -\frac{\lambda^2}{4}-2\lambda.
\end{aligned}d(λ)​=(−2λ​)2+λ(−2λ​)−2λ=4λ2​−2λ2​−2λ=−4λ2​−2λ.​

Maximize over λ≥0\lambda\ge 0λ≥0. This concave parabola is decreasing for λ≥0\lambda\ge 0λ≥0 (derivative −λ/2−2<0-\lambda/2-2<0−λ/2−2<0), so maximum occurs at λ∗=0\lambda^\*=0λ∗=0.

Thus d∗=d(0)=0d^\*=d(0)=0d∗=d(0)=0.

Primal optimum: unconstrained minimizer x=0x=0x=0 is feasible (since $0\le 2),so), so ),sop^\*=0$.

Hence $d^*=p^*=0 (\text{strong duality holds}).

medium

Slater check: Consider minimizing a convex function f(x)f(x)f(x) subject to the single constraint ∥x∥2≤1\|x\|\_2 \le 1∥x∥2​≤1 (in Rn\mathbb{R}^nRn). Does Slater’s condition hold? What if the constraint is ∥x∥2≤0\|x\|\_2 \le 0∥x∥2​≤0?

**Hint:** Slater requires a strictly feasible point for inequalities: find an xxx such that ∥x∥2<1\|x\|\_2 < 1∥x∥2​<1 (or < 0).

Show solution

For ∥x∥2≤1\|x\|\_2 \le 1∥x∥2​≤1, Slater holds because x=0x=0x=0 satisfies ∥0∥2=0<1\|0\|\_2=0<1∥0∥2​=0<1.

For ∥x∥2≤0\|x\|\_2 \le 0∥x∥2​≤0, the feasible set is only {0}\{0\}{0} and there is no xxx with ∥x∥2<0\|x\|\_2<0∥x∥2​<0. So Slater fails.

hard

Dual ascent reasoning: For a problem with one inequality constraint g(x)≤0g(x)\le 0g(x)≤0, suppose at iteration k you find xk∈arg⁡min⁡xL(x,λk)x^k \in \arg\min\_x L(x,\lambda^k)xk∈argminx​L(x,λk) and you observe g(xk)>0g(x^k)>0g(xk)>0. What does the update λk+1=max⁡{0,λk+αg(xk)}\lambda^{k+1}=\max\{0,\lambda^k+\alpha g(x^k)\}λk+1=max{0,λk+αg(xk)} do, and why is that direction sensible for maximizing d(λ)d(\lambda)d(λ)?

**Hint:** Interpret g(xk)g(x^k)g(xk) as a (sub)gradient of ddd at λk\lambda^kλk. Also interpret λ\lambdaλ as a penalty weight on violations.

Show solution

If g(xk)>0g(x^k)>0g(xk)>0, the constraint is violated at the current Lagrangian minimizer. The update increases λ\lambdaλ (since λk+αg(xk)>λk\lambda^k+\alpha g(x^k)>\lambda^kλk+αg(xk)>λk), making future minimizations of L(x,λ)L(x,\lambda)L(x,λ) penalize positive g(x)g(x)g(x) more heavily.

This is sensible because (under mild conditions) g(xk)g(x^k)g(xk) is a subgradient of the concave dual function d(λ)=inf⁡x(f(x)+λg(x))d(\lambda)=\inf\_x \big(f(x)+\lambda g(x)\big)d(λ)=infx​(f(x)+λg(x)). For concave maximization, ascending along a subgradient increases ddd locally. The projection max⁡{0,⋅}\max\{0,\cdot\}max{0,⋅} preserves dual feasibility λ≥0\lambda\ge 0λ≥0, which is required for weak duality and the correctness of the dual problem.

## Connections

Prerequisites you already have: [KKT Conditions](/tech-tree/kkt-conditions/), [Lagrange Multipliers](/tech-tree/lagrange-multipliers/)

Next nodes this supports (typical unlocks):

- •[Convex Optimization: Slater & Duality Theory](/tech-tree/convex-duality/)
- •[Subgradient Methods](/tech-tree/subgradient-methods/)
- •[ADMM (Alternating Direction Method of Multipliers)](/tech-tree/admm/)
- •[Primal-Dual Interior-Point Methods](/tech-tree/primal-dual-interior-point/)
- •[Distributed Optimization via Dual Decomposition](/tech-tree/dual-decomposition/)

Quality: B (4.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
