---
title: Lagrange Multipliers
description: Optimization with equality constraints. Gradient parallelism.
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
permalink: /tech-tree/lagrange-multipliers/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Lagrange Multipliers

OptimizationDifficulty: ★★★★☆Depth: 7Unlocks: 10

Optimization with equality constraints. Gradient parallelism.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Gradient parallelism at constrained extrema: at a point satisfying the equality constraint, the gradient of the objective is parallel to the gradient of the constraint.
- -Lagrangian function: encode the equality constraint into the objective using a scalar multiplier so first-order conditions can be written as stationary conditions of a single function.

## Key Symbols & Notation

lambda (Lagrange multiplier)

## Essential Relationships

- -Stationary condition (gradient equality): grad f(x) = lambda \* grad g(x) at a constrained stationary point.
- -Feasibility plus stationarity determine the solution: g(x) = 0 together with grad f(x) = lambda \* grad g(x) solve for x and lambda.

## Prerequisites (2)

[Gradients5 atoms](/tech-tree/gradients/)[Optimization Introduction5 atoms](/tech-tree/optimization-intro/)

## Unlocks (4)

[Profit Maximizationlvl 4](/tech-tree/profit-maximization/)[KKT Conditionslvl 4](/tech-tree/kkt-conditions/)[Support Vector Machineslvl 4](/tech-tree/svm/)[Lagrangian Dualitylvl 5](/tech-tree/duality/)

## Referenced by (9)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (9)

[Shadow PriceBusiness

Shadow price is the economic name for the Lagrange multiplier; lambda in the KKT/Lagrangian system directly equals the marginal value of relaxing the associated constraint by one unit](/business/shadow-price/)[Utility MaximizationBusiness

Utility maximization subject to a budget constraint is the canonical application of Lagrange multipliers - setting the gradient of utility proportional to the gradient of the budget constraint to find the optimal consumption bundle](/business/utility-maximization/)[Sensitivity AnalysisBusiness

Shadow prices from LP sensitivity analysis are exactly Lagrange multipliers - the dual variable measures how the optimal objective value changes per unit change in a constraint, giving the mathematical foundation for interpreting sensitivity results](/business/sensitivity-analysis/)[marginal valueBusiness

The marginal value of a constraint IS a Lagrange multiplier - this is the direct mathematical object and its gradient-parallelism interpretation](/business/marginal-value/)[Markowitz Portfolio TheoryBusiness

The efficient frontier is classically derived by minimizing w^T Sigma w subject to w^T mu = r\_target and w^T 1 = 1 using Lagrange multipliers. The two-fund separation theorem falls directly out of the KKT conditions.](/business/markowitz-portfolio-theory/)[marginal dollar allocationBusiness

The Lagrange multiplier on a budget constraint is literally the shadow price of the next dollar - the mathematical formalization of 'what is one more dollar of budget worth if allocated optimally'](/business/marginal-dollar-allocation/)[Operating InvestmentsBusiness

The efficient frontier is derived by minimizing portfolio variance subject to a target return constraint via Lagrange multipliers - the classic constrained optimization that produces the capital allocation line](/business/operating-investments/)[PortfolioBusiness

The efficient frontier is derived by minimizing w^T Sigma w subject to w^T mu = target return and w^T 1 = 1 - a constrained optimization solved directly via Lagrange multipliers](/business/portfolio/)[Efficient FrontierBusiness

The classical Markowitz derivation solves for the frontier analytically using Lagrange multipliers on the equality constraints (target return, weights sum to 1)](/business/efficient-frontier/)

Advanced Learning Details

### Graph Position

60

Depth Cost

10

Fan-Out (ROI)

5

Bottleneck Score

7

Chain Length

### Cognitive Load

5

Atomic Elements

30

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (12)

- - Lagrangian function: forming L(x, λ) (often written L or ℒ) that combines objective and equality constraint(s)
- - Lagrange multiplier: scalar variable λ introduced for each equality constraint to enforce the constraint
- - Stationary condition for the Lagrangian: setting the gradient of L with respect to decision variables to zero (∇\_x L = 0)
- - Constraint-recovery condition from the Lagrangian: partial derivative of L with respect to λ yields the original constraint (∂L/∂λ = 0 ↔ g(x)=0)
- - Gradient parallelism condition: at a constrained extremum the gradient of the objective is a scalar multiple of the gradient of the constraint (∇f = λ ∇g)
- - System-solution approach: solving the coupled equations ∇f = λ ∇g together with g(x)=0 to find candidate optima (and λ)
- - Multiple-constraint extension: one multiplier λ\_i per constraint and the condition ∇f = Σ\_i λ\_i ∇g\_i
- - Geometric/tangent-space view: the feasible directions (tangent space) are orthogonal to the constraint gradient, forcing ∇f to lie in the normal direction
- - Multiplier interpretation as sensitivity (shadow price): λ equals the instantaneous rate of change of the optimal objective value with respect to small changes in the constraint right-hand side
- - First-order necessary condition for constrained extrema: Lagrange conditions provide candidates but are not by themselves sufficient
- - Constraint qualification requirement (regularity): nonzero/linearly independent constraint gradients at the point are required for the method to be valid
- - Second-order (sufficiency) idea for constrained problems: definiteness of the Hessian of L restricted to the tangent space determines whether a candidate is min/max (bordered Hessian concept)

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Many real problems aren’t “optimize freely”; they’re “optimize while obeying a rule.” Lagrange multipliers give a clean geometric and algebraic way to solve equality-constrained optimization by turning “stay on this surface” into a condition about gradients lining up.

TL;DR:

To optimize f(**x**) subject to g(**x**) = c, look for points where ∇f(**x**) = λ ∇g(**x**) and g(**x**) = c. This says: at a constrained optimum, the objective’s gradient is parallel to the constraint’s gradient. Equivalent viewpoint: build the Lagrangian ℒ(**x**, λ) = f(**x**) − λ(g(**x**) − c) and solve ∇**x**ℒ = **0** plus the constraint.

## What Is Lagrange Multipliers?

### The problem it solves (why)

Unconstrained optimization asks:

- •Minimize or maximize f(**x**) over all **x** in ℝⁿ.

But many optimization problems have **equality constraints**:

- •Minimize f(**x**) subject to g(**x**) = c.

The constraint restricts you to a **feasible set**—typically a curve (in 2D), a surface (in 3D), or a manifold/hypersurface (in higher dimensions). On that set, the “best” point is not usually where ∇f(**x**) = **0**, because you’re not allowed to move in all directions.

So we need a different optimality condition that respects the constraint.

### The key idea (intuition)

Imagine you’re walking along the constraint curve g(**x**) = c. At a best feasible point, you can’t move *along the curve* to improve f.

That means:

- •Every **feasible direction** (tangent to the constraint set) must have **zero first-order change** in f.

In gradient language:

- •The gradient ∇f points in the direction of steepest increase.
- •If you project ∇f onto the tangent directions and there’s any component left, you could move along the constraint to increase f.

So at a constrained extremum, ∇f must have **no component in any tangent direction**.

What vectors are orthogonal to every tangent direction? The **normal vector** to the constraint surface.

And what gives a normal vector to the level set g(**x**) = c? The gradient ∇g.

That yields the geometric condition:

- •At a constrained extremum: ∇f(**x**\*) is parallel to ∇g(**x**\*).

Parallel means “same direction up to scaling,” so:

- •∇f(**x**\*) = λ ∇g(**x**\*) for some scalar λ.

λ is the **Lagrange multiplier**.

### The canonical statement

For one equality constraint:

Optimize f(**x**) subject to g(**x**) = c.

If **x**\* is a solution (under regularity conditions like ∇g(**x**\*) ≠ **0**), then there exists λ such that:

- •∇f(**x**\*) = λ ∇g(**x**\*)
- •g(**x**\*) = c

This converts the constrained problem into a system of equations.

### What λ “means”

λ is not just a trick variable. It often measures **sensitivity**: how much the optimal value changes if you relax the constraint slightly.

Define the optimal value function:

- •v(c) = optimum of f(**x**) subject to g(**x**) = c

Under suitable conditions, one can show:

- •dv/dc = λ

Interpretation: λ is the “shadow price” of tightening/loosening the constraint.

### When to use (and when not)

Lagrange multipliers are designed for:

- •Equality constraints (g(**x**) = c)
- •Smooth (differentiable) functions

If you have inequalities (g(**x**) ≤ c), you need the generalized framework: [KKT Conditions](/tech-tree/kkt-conditions/).

### A mental picture to keep

- •g(**x**) = c is a level set.
- •∇g is perpendicular to that level set.
- •At the best point on the level set, ∇f must also be perpendicular to it.
- •Therefore ∇f ∥ ∇g.

That single picture explains the method—and helps you remember why it works.

## Core Mechanic 1: Gradient Parallelism at Constrained Extrema

### Why this condition must hold

Suppose you’re constrained to g(**x**) = c, and you’re at some feasible point **x**.

A **feasible direction** **d** is one that keeps you on the constraint to first order. Using a first-order approximation:

- •g(**x** + ε**d**) ≈ g(**x**) + ε ∇g(**x**)·**d**

To stay feasible (keep g = c) for small ε, we need:

- •∇g(**x**)·**d** = 0

So feasible directions **d** are exactly the vectors orthogonal to ∇g(**x**). These directions form the tangent space to the constraint surface.

Now look at how the objective changes:

- •f(**x** + ε**d**) ≈ f(**x**) + ε ∇f(**x**)·**d**

At a constrained local optimum, we can’t improve f by moving in any feasible direction. That means:

- •∇f(**x**)·**d** = 0 for all **d** such that ∇g(**x**)·**d** = 0

In linear algebra terms:

- •∇f is orthogonal to the entire tangent space.

The orthogonal complement of the tangent space is the span of the normal vector ∇g. Therefore:

- •∇f(**x**\*) ∈ span{∇g(**x**\*)}

So there exists λ such that:

- •∇f(**x**\*) = λ ∇g(**x**\*)

This is the “gradient parallelism” condition.

### What can go wrong (regularity)

If ∇g(**x**\*) = **0**, the constraint surface may not have a well-defined normal at **x**\* (think cusp or degenerate point). Then the simple condition may fail or be incomplete.

A standard regularity assumption for one constraint is:

- •∇g(**x**\*) ≠ **0**

For multiple constraints, you need gradients of constraints to be linearly independent (more later).

### Constrained extrema vs. unconstrained stationary points

Unconstrained optimum: ∇f(**x**\*) = **0**.

Constrained optimum: ∇f(**x**\*) doesn’t need to be **0**. It only needs to have no component tangent to the feasible set.

Geometrically:

- •Unconstrained optimum: level sets of f “close around” **x**\*.
- •Constrained optimum: the level set of f is tangent to the constraint set at **x**\*.

### Turning geometry into equations

If **x** ∈ ℝ² with constraint g(x, y) = c, the method yields:

- •∂f/∂x = λ ∂g/∂x
- •∂f/∂y = λ ∂g/∂y
- •g(x, y) = c

That’s 3 equations in 3 unknowns (x, y, λ).

In ℝⁿ, it becomes n + 1 equations in n + 1 unknowns.

### Multiple equality constraints

If you have m constraints:

- •g₁(**x**) = c₁, …, gₘ(**x**) = cₘ

Then the feasible set is the intersection of m level sets. The tangent space is orthogonal to each ∇gᵢ, so the normal space is spanned by them.

The condition generalizes to:

- •∇f(**x**\*) = ∑ᵢ₌₁ᵐ λᵢ ∇gᵢ(**x**\*)
- •gᵢ(**x**\*) = cᵢ for all i

This is the same “gradient lives in the span of constraint gradients” idea.

### Quick comparison: one constraint vs. many

| Setting | Condition | Unknown multipliers |
| --- | --- | --- |
| 1 constraint g(**x**) = c | ∇f = λ ∇g | λ ∈ ℝ |
| m constraints gᵢ(**x**) = cᵢ | ∇f = ∑ λᵢ ∇gᵢ | **λ** ∈ ℝᵐ |

### What this gives you (and what it doesn’t)

Solving the Lagrange equations gives **candidates**. You still need to:

- •Check feasibility
- •Compare objective values (global optimum) or use second-order tests (local classification)
- •Consider boundary/degenerate cases if assumptions fail

In constrained problems, it’s common to find:

- •Multiple candidate points
- •Some maxima, some minima, some saddle-like points restricted to the constraint

So treat the gradient parallelism equations as a principled way to generate a shortlist of candidates.

## Core Mechanic 2: The Lagrangian Function (Encoding Constraints with λ)

### Why introduce the Lagrangian (motivation)

Gradient parallelism is a geometric statement, but algebraically it’s nicer to express everything as “take derivatives and set them to zero.”

The Lagrangian packages the objective and constraint into one scalar function whose stationary points encode the Lagrange conditions.

For one constraint g(**x**) = c, define:

- •ℒ(**x**, λ) = f(**x**) − λ(g(**x**) − c)

(You’ll also see ℒ = f + λ(g − c). The sign convention doesn’t matter as long as you’re consistent; λ will flip sign.)

### How the stationary conditions reproduce the method

Take partial derivatives:

- •∇**x**ℒ(**x**, λ) = ∇f(**x**) − λ ∇g(**x**)
- •∂ℒ/∂λ = −(g(**x**) − c)

Set them to zero:

1) ∇**x**ℒ = **0** ⇒ ∇f(**x**) − λ ∇g(**x**) = **0** ⇒ ∇f(**x**) = λ ∇g(**x**)

2) ∂ℒ/∂λ = 0 ⇒ g(**x**) − c = 0 ⇒ g(**x**) = c

So stationary points of ℒ correspond exactly to the Lagrange multiplier equations.

### Why λ is “free” to enforce the constraint

Think of λ as adjusting the penalty for violating the constraint. At the solution, λ tunes the trade-off so that a stationary point occurs exactly on the feasible set.

This is different from naive penalty methods like minimizing f(**x**) + ρ(g(**x**) − c)² for a large ρ:

- •Penalty methods approximate constraints.
- •Lagrange multipliers enforce the constraint exactly (in the mathematical conditions).

### Multiple constraints in Lagrangian form

For constraints gᵢ(**x**) = cᵢ:

- •ℒ(**x**, **λ**) = f(**x**) − ∑ᵢ₌₁ᵐ λᵢ (gᵢ(**x**) − cᵢ)

Stationarity gives:

- •∇f(**x**) − ∑ᵢ λᵢ ∇gᵢ(**x**) = **0**
- •gᵢ(**x**) = cᵢ for all i

### Second-order thinking (local min/max classification)

Solving first-order conditions gives candidates. To classify them, you need to understand curvature **along feasible directions**.

A practical approach:

- •Parameterize the constraint locally and check second derivative along that parameter, or
- •Use second-order constrained conditions (bordered Hessian), or
- •In many problems, simply compare objective values across candidates if the feasible set is simple/compact.

At difficulty 4, it’s worth knowing a bit of structure without turning this into a full course:

#### Tangent-space second-order idea

Let **d** be a feasible direction at **x**\*, i.e., ∇g(**x**\*)·**d** = 0.

For a constrained local minimum, you expect:

- •**d**ᵀ ∇²f(**x**\*) **d** ≥ 0 for all feasible **d** (after accounting for curvature of the constraint).

The clean way to incorporate constraint curvature uses the Hessian of the Lagrangian:

- •∇²**x**ℒ(**x***, λ*) = ∇²f(**x***) − λ* ∇²g(**x**\*)

Then you examine **d**ᵀ ∇²**x**ℒ **d** over tangent directions **d**.

You don’t always need this in practice, but it’s the right object to look at: once you’ve “encoded” the constraint in ℒ, the Hessian of ℒ governs local behavior on the manifold.

### Relationship to constrained optimization algorithms

Even if you don’t solve analytically, the Lagrangian viewpoint drives algorithms:

- •Method of multipliers / augmented Lagrangian
- •Sequential quadratic programming (SQP)
- •Dual ascent methods

These will reappear when you study [Lagrangian Duality](/tech-tree/duality/) and [KKT Conditions](/tech-tree/kkt-conditions/).

### Summary of the workflow

1) Write constraint(s) in standard form g(**x**) = c.

2) Form ℒ(**x**, **λ**) = f(**x**) − ∑ λᵢ(gᵢ(**x**) − cᵢ).

3) Solve:

- •∇**x**ℒ = **0**
- •∂ℒ/∂λᵢ = 0

4) Evaluate candidates and pick the correct optimum type.

The method is compact, systematic, and scales naturally to multiple constraints—exactly why it’s a cornerstone for later topics like KKT and duality.

## Application/Connection: From “Math Trick” to ML Optimization (SVMs, KKT, Duality)

### Why Lagrange multipliers matter in machine learning

Many ML training problems are constrained, either explicitly or implicitly:

- •Margin constraints in support vector machines
- •Normalization constraints (e.g., probabilities sum to 1)
- •Conservation constraints in probabilistic models
- •Equality constraints introduced to split variables in optimization (ADMM-style ideas)

Even when the original problem is unconstrained, constraints appear when you derive **dual problems** or enforce structure.

### Support Vector Machines (where you’ll see it next)

In a (hard-margin) linear SVM, you choose a separating hyperplane (**w**, b) that maximizes margin subject to classification constraints.

A common equivalent formulation:

Minimize ½‖**w**‖² subject to

- •yᵢ(**w**·**x**ᵢ + b) ≥ 1 for all i

Those are **inequality** constraints, so the full story uses KKT. But the core pattern is identical:

- •Build a Lagrangian with multipliers
- •Stationarity links primal variables (**w**, b) to multipliers
- •The dual problem emerges by eliminating primal variables

Even before inequalities, the equality-constraint case teaches the essential muscle memory: “Introduce λ, take derivatives, solve stationarity + constraints.”

### KKT conditions: equality constraints are the base case

KKT conditions generalize Lagrange multipliers to include inequalities g(**x**) ≤ 0 via multipliers αᵢ ≥ 0 and complementary slackness:

- •αᵢ gᵢ(**x**) = 0

If you understand equality constraints well, KKT feels like a small extension rather than a new world.

### Lagrangian duality: λ becomes an optimization variable

In equality constraints, we usually solve for λ as part of the stationarity system.

In duality, you instead treat λ as defining a lower bound (for minimization) and optimize that bound:

- •Dual function: q(λ) = inf\_**x** ℒ(**x**, λ)
- •Dual problem: maximize q(λ) over λ

The Lagrangian is the bridge between primal and dual.

### Sensitivity / shadow price interpretation (practical intuition)

Consider a parameterized constraint g(**x**) = c. If λ\* is large in magnitude at the solution, the optimum is very sensitive to changes in c.

A simple mental model:

- •If tightening the constraint slightly makes the objective much worse, |λ| is large.
- •If the constraint doesn’t really “bind” the optimum (or you can adjust with little cost), |λ| is small.

In economics and resource allocation, λ is literally the “value” of an additional unit of resource.

### A concrete ML-adjacent example: normalization constraint

Suppose you optimize over probability vectors **p** ∈ ℝⁿ with constraint ∑ᵢ pᵢ = 1.

That’s an equality constraint. The gradient-parallelism idea says:

- •∇f(**p**) = λ ∇(∑ᵢ pᵢ)

But ∇(∑ᵢ pᵢ) = **1** (the all-ones vector). So the condition becomes:

- •∂f/∂pᵢ = λ for all i

Meaning: at optimum (with only that constraint), all partial derivatives must be equal. This is a powerful structural fact you can reuse.

(If you also require pᵢ ≥ 0, that’s inequality territory → KKT.)

### How to recognize a “Lagrange multipliers problem” quickly

You’re likely in this regime if:

- •The constraint is an equation like x² + y² = 1, or ∑ xᵢ = 1.
- •The constraint defines a smooth curve/surface.
- •The objective is differentiable.
- •You want stationary candidates on that surface.

### One more conceptual connection: projection viewpoint

Another way to interpret Lagrange multipliers:

- •At optimum, the gradient of f projected onto the tangent space is **0**.

Equivalently:

- •∇f lies entirely in the normal space, i.e., span{∇gᵢ}.

This “projection to tangent space” language shows up in manifold optimization and constrained gradient methods.

### Where you go next

- •For inequality constraints and complementarity: [KKT Conditions](/tech-tree/kkt-conditions/)
- •For turning constraints into a dual maximization: [Lagrangian Duality](/tech-tree/duality/)
- •For a flagship ML use case: [Support Vector Machines](/tech-tree/svm/)

Lagrange multipliers are the conceptual seed for all three.

## Worked Examples (3)

### Example 1: Maximize x y subject to x² + y² = 1

Optimize f(x, y) = x y subject to g(x, y) = x² + y² = 1. This is “best product on the unit circle.”

1. Write the gradients:

   ∇f = (∂/∂x (x y), ∂/∂y (x y)) = (y, x)

   ∇g = (∂/∂x (x² + y²), ∂/∂y (x² + y²)) = (2x, 2y)
2. Set the Lagrange condition ∇f = λ ∇g:

   (y, x) = λ(2x, 2y)

   So:

   y = 2λ x

   x = 2λ y
3. Solve the two equations:

   From y = 2λ x, substitute into x = 2λ y:

   x = 2λ(2λ x) = 4λ² x

   ⇒ x(1 − 4λ²) = 0

   So either x = 0 or 1 − 4λ² = 0
4. Case A: x = 0

   Constraint gives: 0² + y² = 1 ⇒ y = ±1

   Then f = x y = 0
5. Case B: 1 − 4λ² = 0 ⇒ λ = ±1/2

   Using y = 2λ x:

   If λ = 1/2, then y = x

   If λ = −1/2, then y = −x
6. Subcase B1: y = x

   Constraint: x² + x² = 1 ⇒ 2x² = 1 ⇒ x = ±1/√2

   So points: (1/√2, 1/√2) and (−1/√2, −1/√2)

   Objective: f = x y = x² = 1/2
7. Subcase B2: y = −x

   Constraint: x² + (−x)² = 1 ⇒ 2x² = 1 ⇒ x = ±1/√2

   Points: (1/√2, −1/√2) and (−1/√2, 1/√2)

   Objective: f = x y = −x² = −1/2
8. Compare objective values:

   Max value is 1/2 at (±1/√2, ±1/√2) with matching signs.

   Min value is −1/2 at (±1/√2, ∓1/√2) with opposite signs.

   The x=0 points give 0, neither max nor min globally.

**Insight:** On the unit circle, the best way to maximize x y is to balance x and y equally (same sign), i.e., sit on the line y = x. The gradients line up exactly at the tangency points between level sets of x y and the circle.

### Example 2: Closest point on a line to the origin (geometry + λ meaning)

Minimize distance to origin subject to a linear equality. Let the constraint be a x + b y = 1 (with constants a, b not both 0). Minimize f(x, y) = x² + y² subject to g(x, y) = a x + b y = 1.

1. Compute gradients:

   ∇f = (2x, 2y)

   ∇g = (a, b)
2. Set ∇f = λ ∇g:

   (2x, 2y) = λ(a, b)

   So:

   2x = λ a ⇒ x = (λ a)/2

   2y = λ b ⇒ y = (λ b)/2
3. Enforce the constraint a x + b y = 1:

   a(λ a/2) + b(λ b/2) = 1

   ⇒ (λ/2)(a² + b²) = 1

   ⇒ λ = 2/(a² + b²)
4. Substitute λ back:

   x\* = (λ a)/2 = ( (2/(a² + b²)) a )/2 = a/(a² + b²)

   y\* = b/(a² + b²)
5. Compute the minimum value:

   f(x*, y*) = x*² + y*²

   = a²/(a² + b²)² + b²/(a² + b²)²

   = (a² + b²)/(a² + b²)²

   = 1/(a² + b²)

**Insight:** The minimizer is the orthogonal projection of the origin onto the line a x + b y = 1. The multiplier λ scales the normal vector (a, b) so that the point lands exactly on the constraint line.

### Example 3: Two constraints in 3D — maximize x + y + z subject to x² + y² + z² = 1 and x − y = 0

Optimize f(x, y, z) = x + y + z subject to g₁(x, y, z) = x² + y² + z² = 1 and g₂(x, y, z) = x − y = 0.

1. Compute gradients:

   ∇f = (1, 1, 1)

   ∇g₁ = (2x, 2y, 2z)

   ∇g₂ = (1, −1, 0)
2. Use the multi-constraint condition:

   ∇f = λ₁ ∇g₁ + λ₂ ∇g₂

   So:

   (1, 1, 1) = λ₁(2x, 2y, 2z) + λ₂(1, −1, 0)
3. Write component equations:

   1 = 2λ₁ x + λ₂

   1 = 2λ₁ y − λ₂

   1 = 2λ₁ z
4. Also apply constraints:

   x² + y² + z² = 1

   x − y = 0 ⇒ x = y
5. Use x = y in the first two component equations:

   1 = 2λ₁ x + λ₂

   1 = 2λ₁ x − λ₂

   Subtract the second from the first:

   0 = 2λ₂ ⇒ λ₂ = 0
6. With λ₂ = 0, we have:

   1 = 2λ₁ x

   1 = 2λ₁ y

   1 = 2λ₁ z

   So x = y = z
7. Let x = y = z = t. Apply the sphere constraint:

   3t² = 1 ⇒ t = ±1/√3
8. Evaluate f:

   If t = 1/√3, then f = 3(1/√3) = √3 (maximum)

   If t = −1/√3, then f = −√3 (minimum)

**Insight:** With two constraints, ∇f must lie in the span of two normals. Here symmetry and the constraint x = y force the optimum to the equal-coordinates direction, then the sphere fixes the magnitude.

## Key Takeaways

- ✓

  Equality-constrained optimization asks for extrema of f(**x**) restricted to the surface g(**x**) = c.
- ✓

  At a regular constrained extremum **x**\* (with ∇g(**x**\*) ≠ **0**), the gradients satisfy ∇f(**x**\*) = λ ∇g(**x**\*): gradient parallelism.
- ✓

  Geometric reason: feasible (tangent) directions **d** satisfy ∇g·**d** = 0, and at optimum you need ∇f·**d** = 0 for all such **d**.
- ✓

  The Lagrangian ℒ(**x**, λ) = f(**x**) − λ(g(**x**) − c) converts the constrained first-order conditions into stationary conditions: ∇**x**ℒ = **0**, ∂ℒ/∂λ = 0.
- ✓

  With multiple equality constraints, the condition becomes ∇f = ∑ λᵢ ∇gᵢ; ∇f lies in the span of constraint gradients.
- ✓

  Solving Lagrange equations gives candidate points; you still must compare objective values or use second-order reasoning to decide max/min.
- ✓

  The multiplier λ often has sensitivity meaning: it relates to how the optimal value changes as the constraint constant c changes.
- ✓

  Lagrange multipliers are the foundation for KKT (inequalities), SVM derivations, and Lagrangian duality.

## Common Mistakes

- ✗

  Forgetting to enforce the constraint after solving ∇f = λ ∇g (you must also satisfy g(**x**) = c).
- ✗

  Assuming every solution to the Lagrange equations is a maximum/minimum without checking (some are minima, maxima, or neither on the constraint).
- ✗

  Ignoring degeneracy: if ∇g(**x**\*) = **0** (or multiple constraints are not independent), the standard conditions may be incomplete or misleading.
- ✗

  Mixing sign conventions in the Lagrangian and then interpreting λ incorrectly (the equations still work, but λ’s sign flips).

## Practice

easy

Find the maximum and minimum of f(x, y) = x² + y² subject to the constraint x + y = 1.

**Hint:** Use ∇f = (2x, 2y) and ∇g = (1, 1). Solve (2x, 2y) = λ(1, 1) plus x + y = 1. Then think about whether a maximum exists on an unbounded line.

Show solution

Let g(x, y) = x + y = 1. Then ∇f = (2x, 2y), ∇g = (1, 1).

Lagrange condition:

(2x, 2y) = λ(1, 1)

⇒ 2x = λ and 2y = λ ⇒ x = y.

Constraint x + y = 1 ⇒ 2x = 1 ⇒ x = 1/2, y = 1/2.

Then f = (1/2)² + (1/2)² = 1/2.

This is the minimum (closest point to origin on the line). There is no maximum because along the line x + y = 1 you can take x → ∞, y = 1 − x → −∞, and x² + y² → ∞.

medium

Maximize f(x, y) = x + 2y subject to x² + y² = 5.

**Hint:** The constraint is a circle. Solve ∇f = λ ∇g, where g(x, y) = x² + y².

Show solution

Let g(x, y) = x² + y² = 5. Then ∇f = (1, 2), ∇g = (2x, 2y).

Set (1, 2) = λ(2x, 2y):

1 = 2λ x ⇒ x = 1/(2λ)

2 = 2λ y ⇒ y = 1/λ

Use constraint:

x² + y² = 5

(1/(2λ))² + (1/λ)² = 5

1/(4λ²) + 1/λ² = 5

(1/4 + 1)/λ² = 5

(5/4)/λ² = 5

1/λ² = 4 ⇒ λ = ±1/2

If λ = 1/2: x = 1, y = 2, f = 1 + 4 = 5 (maximum)

If λ = −1/2: x = −1, y = −2, f = −1 − 4 = −5 (minimum)

hard

Use Lagrange multipliers to find critical points of f(x, y, z) = x y z subject to x² + y² + z² = 3. (You may leave the answer as a set of symmetric points.)

**Hint:** Compute ∇f = (y z, x z, x y) and ∇g = (2x, 2y, 2z). Use y z = 2λ x etc. Look for symmetry cases like x = y = z and sign flips.

Show solution

Constraint: g(x, y, z) = x² + y² + z² = 3, so ∇g = (2x, 2y, 2z).

Objective: f = x y z, so ∇f = (y z, x z, x y).

Lagrange equations:

(y z, x z, x y) = λ(2x, 2y, 2z)

So:

(1) y z = 2λ x

(2) x z = 2λ y

(3) x y = 2λ z

and x² + y² + z² = 3.

Assume x, y, z are all nonzero. Multiply (1)(2)(3):

(y z)(x z)(x y) = (2λ)³ (x y z)

Left side = x² y² z² = (x y z)².

So (x y z)² = 8λ³ (x y z).

Since x y z ≠ 0, divide by x y z:

x y z = 8λ³.

From (1): λ = (y z)/(2x). By symmetry, ratios suggest |x| = |y| = |z|.

Let x = s₁ t, y = s₂ t, z = s₃ t where sᵢ ∈ {−1, +1} and t > 0.

Constraint gives 3 t² = 3 ⇒ t = 1.

So candidates are (x, y, z) = (s₁, s₂, s₃).

These satisfy the Lagrange equations with suitable λ because:

For x = ±1, y = ±1, z = ±1, we have y z = ±1 and 2λ x must match it; choose λ = (y z)/(2x) which is ±1/2 consistently across equations.

Thus the critical points on the sphere are the 8 sign combinations (±1, ±1, ±1).

Their objective values are f = x y z = ±1.

Maxima: points with product +1 (even number of negatives). Minima: product −1 (odd number of negatives).

## Connections

- •Next: [KKT Conditions](/tech-tree/kkt-conditions/) for inequality constraints and complementary slackness.
- •Next: [Lagrangian Duality](/tech-tree/duality/) to turn ℒ(**x**, **λ**) into a dual optimization problem.
- •Application: [Support Vector Machines](/tech-tree/svm/) where Lagrangians and KKT produce the dual and the kernel trick.

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
