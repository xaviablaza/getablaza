---
title: Optimization Introduction
description: Minimizing or maximizing objective functions. Constraints.
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
inspiration_url: https://templeton.host/tech-tree/optimization-intro/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/optimization-intro/](https://templeton.host/tech-tree/optimization-intro/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Optimization Introduction

OptimizationDifficulty: ★★★☆☆Depth: 6Unlocks: 61

Minimizing or maximizing objective functions. Constraints.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Objective: a scalar-valued function that maps a decision vector to a value to be minimized or maximized
- -Feasible set: the set of decision vectors that satisfy all problem constraints (equalities and inequalities)
- -Optimality: what an optimal solution is (local vs global) and the first-order stationarity notion that characterizes local optima

## Key Symbols & Notation

f(x) and x (objective function and decision-variable vector)

## Essential Relationships

- -Optimization statement and stationarity: choose x in the feasible set to extremize f(x); at a local optimum the gradient of f is orthogonal to feasible directions (equivalently, gradients balance via Lagrange multipliers for constrained problems)

## Prerequisites (1)

[Gradients5 atoms](/tech-tree/gradients/)

## Unlocks (7)

[Gradient Descentlvl 3](/tech-tree/gradient-descent/)[Nash Equilibriumlvl 3](/tech-tree/nash-equilibrium/)[Lagrange Multiplierslvl 4](/tech-tree/lagrange-multipliers/)[Utility Theorylvl 3](/tech-tree/utility-theory/)[Cost Functionslvl 3](/tech-tree/cost-functions/)[Linear Programminglvl 4](/tech-tree/linear-programming/)[Bayesian Decision Theorylvl 4](/tech-tree/bayesian-decision-theory/)

## Referenced by (17)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (7)

[personal financeBusiness

Opportunity cost is the shadow price of a binding constraint - every dollar-allocation decision in personal finance is a constrained optimization problem](/business/personal-finance/)[budgetingBusiness

Budgeting is constrained optimization - maximize outcomes subject to finite resource constraints, the formal framing taught here](/business/budgeting/)[Capital InvestmentBusiness

Capital investment is constrained optimization: allocate a limited capital budget across possible improvements to maximize the total positional gain of tasks. The mathematical foundation for reasoning about where capital does the most good.](/business/capital-investment/)[Capital AllocationBusiness

Capital allocation is constrained optimization: maximize total return subject to a budget constraint. The entire discipline - from factory capex to AI automation spend - is 'maximize f(x) subject to sum(x\_i) <= B.'](/business/capital-allocation/)[capital investmentsBusiness

Allocating a finite capital budget across competing investments to maximize total quadrant improvement is a constrained optimization problem](/business/capital-investments/)[tax strategyBusiness

Tax strategy is literally constrained optimization - minimize tax liability subject to legal rules, cash flow needs, and entity structure constraints](/business/tax-strategy/)[OperationsBusiness

Operations management is applied constrained optimization - minimizing cost subject to service levels, maximizing throughput subject to capacity, balancing inventory holding cost against stockout risk](/business/operations/)

### From Money (10)

[BudgetingMoney

Budget allocation is a constrained optimization problem - fixed income, competing categories](/money/budget-basics/)[Debt AvalancheMoney

Minimizing total interest paid is an optimization objective](/money/debt-avalanche/)[Max Your 401kMoney

Maximizing tax-advantaged space is a constrained optimization](/money/401k-beyond-match/)[Asset AllocationMoney

Allocation is a mean-variance optimization problem](/money/asset-allocation/)[RebalancingMoney

Rebalancing restores target allocation after drift - a constrained optimization](/money/rebalancing/)[Rent vs BuyMoney

Total cost minimization over expected time horizon](/money/rent-vs-buy/)[Capital GainsMoney

Tax-efficient selling order is an optimization problem](/money/capital-gains-planning/)[Tax-Loss HarvestingMoney

Harvesting optimizes after-tax returns subject to wash sale constraints](/money/tax-loss-harvesting/)[Business Entity TaxMoney

Entity selection optimizes tax treatment given business characteristics and income level](/money/business-entity-tax/)[Charitable Giving StrategyMoney

DAF timing and deduction bunching optimize the after-tax value of charitable giving](/money/charitable-giving-strategy/)

Advanced Learning Details

### Graph Position

55

Depth Cost

61

Fan-Out (ROI)

23

Bottleneck Score

6

Chain Length

### Cognitive Load

5

Atomic Elements

50

Total Elements

L4

Percentile Level

L3

Atomic Level

### All Concepts (23)

- - Objective function: the function f(x) to be minimized or maximized
- - Optimization problem statement: minimize (or maximize) f(x) subject to constraints
- - Feasible region / feasible set: set of x that satisfy the problem's constraints
- - Optimal solution (x\*): a feasible x that attains the best objective value
- - Optimal value (f\*): the value of the objective at an optimal solution
- - argmin / argmax: the argument(s) x that achieve the minimum/maximum
- - Local minimum / local maximum: optimum relative to a neighborhood of x
- - Global minimum / global maximum: optimum over the entire feasible set
- - Stationary point / critical point: point where first-order necessary condition holds (gradient zero or undefined)
- - Saddle point: stationary point that is neither a local min nor max
- - Equality constraint: constraint of form h(x) = 0
- - Inequality constraint: constraint of form g(x) ≤ 0 (or ≥ 0)
- - Active (binding) constraint: a constraint that holds with equality at a candidate solution
- - Inactive (non-binding) constraint: a constraint that is not tight at the candidate solution
- - Lagrangian function: combined function L(x, λ) that incorporates objective and constraints
- - Lagrange multiplier (λ): parameter introduced per constraint in the Lagrangian
- - Hessian matrix: matrix of second partial derivatives (∇^2 f) used for second-order tests
- - Second-order optimality conditions: use of Hessian definiteness to classify stationary points
- - Karush–Kuhn–Tucker (KKT) conditions: first-order necessary conditions for problems with inequality/equality constraints
- - Complementary slackness: condition linking inequality multipliers to constraint tightness
- - Dual variables / dual feasibility: sign requirements (e.g., λ ≥ 0) for multipliers associated with inequality constraints
- - Convex function and convex feasible set: structure that guarantees global optimality from local conditions
- - Optimality vs feasibility distinction: feasibility checks constraints, optimality checks objective

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Nearly every “smart” system—training a neural network, fitting a line to data, scheduling deliveries, designing a bridge—can be framed as: pick a decision vector **x** that makes a single number f(**x**) as small (or large) as possible, while respecting the rules of the problem.

TL;DR:

Optimization is the study of choosing a decision vector **x** to minimize or maximize an objective f(**x**) over a feasible set defined by constraints. Unconstrained local optima satisfy the first-order stationarity condition ∇f(**x**\*) = **0**; constraints change what “no improving direction” means and motivate tools like projection, Lagrange multipliers, and linear programming.

## What Is Optimization Introduction?

### Why optimization shows up everywhere

Optimization is a *language* for decision-making. Whenever you can:

1) describe what “good” means with a single number, and

2) describe what choices are allowed,

you can write an optimization problem.

A canonical form is:

- •**Decision variable (vector)**: **x** ∈ ℝⁿ (your choice)
- •**Objective**: f(**x**) ∈ ℝ (score/cost to minimize or reward to maximize)
- •**Constraints**: rules restricting **x**

A typical minimization problem:

minimize f(**x**)

subject to **x** ∈ 𝒳

where 𝒳 is the **feasible set** (the set of all choices that satisfy the constraints).

### The core atoms: objective, feasible set, optimality

You’ll see these three pieces repeatedly:

#### 1) Objective (a scalar-valued function)

An **objective** is a function f that maps a decision vector to a scalar:

f: ℝⁿ → ℝ, **x** ↦ f(**x**)

- •If f(**x**) is a cost/error/loss, we **minimize**.
- •If f(**x**) is a utility/return/accuracy proxy, we **maximize**.

Maximization is equivalent to minimization by sign flip:

maximize f(**x**) ⇔ minimize (−f(**x**))

So in many courses and libraries, “optimization” is taught largely as *minimization*.

#### 2) Feasible set (what choices are allowed)

Constraints carve out which **x** are permitted. A common description:

𝒳 = { **x** ∈ ℝⁿ : gᵢ(**x**) ≤ 0 for i = 1,…,m and hⱼ(**x**) = 0 for j = 1,…,p }

- •Inequalities gᵢ(**x**) ≤ 0: limits, budgets, capacities
- •Equalities hⱼ(**x**) = 0: conservation laws, exact relationships

If there are **no** constraints, then 𝒳 = ℝⁿ and the problem is **unconstrained**.

#### 3) Optimality (what does “best” mean?)

An optimizer is any feasible point **x**⋆ whose objective is minimal among the candidates.

- •**Global minimizer**: f(**x**⋆) ≤ f(**x**) for all **x** ∈ 𝒳
- •**Local minimizer**: f(**x**⋆) ≤ f(**x**) for all feasible **x** in a *neighborhood* around **x**⋆

Local vs global matters because many objectives (especially in ML) are **nonconvex**: they can have multiple valleys. Algorithms like gradient descent typically aim for a *local* optimum or even just a “good enough” point.

### Vocabulary you’ll use constantly

Here’s a compact glossary.

| Term | Meaning | Example intuition |
| --- | --- | --- |
| Decision variable **x** | What you control | model parameters, schedule, portfolio weights |
| Objective f(**x**) | What you measure | error, cost, negative log-likelihood |
| Feasible set 𝒳 | Allowed choices | budget constraints, box bounds, equality laws |
| Minimizer **x**⋆ | Best choice (local/global) | lowest loss parameters |
| Argmin | The set of minimizers | argmin f(**x**) can contain multiple points |

### A note on dimensions and geometry

Because **x** is a vector, optimization is inherently geometric:

- •f(**x**) defines a “landscape” over ℝⁿ.
- •Constraints define a region 𝒳 in that space.
- •The solution is the lowest point *within that region*.

Your prerequisite—**gradients**—already gives you a powerful geometric tool: ∇f(**x**) points in the direction of steepest ascent, and −∇f(**x**) points downhill the fastest (locally). This will become your default “direction of improvement” in unconstrained optimization.

## Core Mechanic 1: Objective Landscapes and Stationarity (Unconstrained Problems)

### Why we need an optimality condition

Even if you can write down f(**x**), directly checking “is **x**⋆ global?” by comparing against *all* **x** is impossible in continuous spaces. So optimization uses *conditions* that any optimum must satisfy.

For unconstrained problems:

minimize f(**x**) over **x** ∈ ℝⁿ

the first condition you learn is a **first-order necessary condition**: at a local minimizer, there should be no infinitesimal direction you can move that decreases f.

### From “no improving direction” to ∇f(**x**⋆) = **0**

Assume f is differentiable. Consider a candidate point **x**⋆, and take a small step along a direction **d** with step size ε:

**x**(ε) = **x**⋆ + ε **d**

Define the 1D function φ(ε) = f(**x**⋆ + ε**d**). If **x**⋆ is a local minimizer, then for small ε around 0, ε = 0 should be a local minimum of φ.

Compute the derivative at 0:

φ′(0) = d/dε f(**x**⋆ + ε**d**) |\_{ε=0}

By the chain rule:

φ′(0) = ∇f(**x**⋆)ᵀ **d**

For **x**⋆ to be a local minimizer, we need φ′(0) = 0 for *all* directions **d** (otherwise choose a direction where it’s negative and decrease f).

So we require:

∇f(**x**⋆)ᵀ **d** = 0 for all **d**

The only vector orthogonal to all directions **d** is the zero vector. Therefore:

∇f(**x**⋆) = **0**

This is **first-order stationarity**.

### What stationarity does (and does not) guarantee

Stationary points include:

- •local minima
- •local maxima
- •saddle points

So ∇f(**x**⋆) = **0** is **necessary** for a differentiable unconstrained local optimum, but not sufficient.

A second-order view uses the Hessian H(**x**) = ∇²f(**x**) (a matrix). If H(**x**⋆) is positive definite, then **x**⋆ is a strict local minimizer. But many practical algorithms still start from first-order information because:

- •gradients are often cheap (via backprop/automatic differentiation)
- •Hessians can be expensive to compute/store

### Intuition: gradients as “slope in every direction”

The dot product ∇f(**x**)ᵀ **d** is the directional derivative: the instantaneous rate of change of f if you move in direction **d**.

- •If ∇f(**x**) ≠ **0**, then choosing **d** = −∇f(**x**) gives:

∇f(**x**)ᵀ (−∇f(**x**)) = −‖∇f(**x**)‖² < 0

So you can immediately decrease f by moving a little along −∇f.

- •If ∇f(**x**) = **0**, then the *linear* term in every direction is zero. You need higher-order terms to know if you go up, down, or flat.

### Level sets and valleys

A helpful geometric picture:

- •A **level set** is { **x** : f(**x**) = c }.
- •The gradient ∇f(**x**) is perpendicular (normal) to the level set at **x**.

At a local minimum, level sets form nested curves/surfaces around the minimizer. Stationarity means the “best local place” has no downhill direction.

### A tiny but important warning about non-differentiability

Some objectives are not differentiable everywhere (e.g., absolute value |x| at 0, ReLU). Then “∇f(**x**) = **0**” is not the right tool at kink points; you use subgradients. For this node, keep the main idea: *optimality means no direction improves the objective*, and gradients formalize that when differentiable.

## Core Mechanic 2: Feasible Sets and Constraints (Constrained Problems)

### Why constraints change the meaning of “no improving direction”

In unconstrained optimization, any direction **d** is allowed. With constraints, you can’t necessarily step in the direction you want.

Instead, you must stay inside the feasible set 𝒳.

So the key question becomes:

> Is there a *feasible* direction you can move that decreases f?

If the answer is “no,” you are (at least) locally optimal *with respect to the constraints*.

### Writing constraints explicitly

A common constrained optimization problem:

minimize f(**x**)

subject to gᵢ(**x**) ≤ 0, i = 1,…,m

hⱼ(**x**) = 0, j = 1,…,p

Feasible set:

𝒳 = { **x** : gᵢ(**x**) ≤ 0 ∀i, hⱼ(**x**) = 0 ∀j }

### Examples of feasible sets (build intuition)

Constraints define geometry:

1) **Box constraints**: ℓ ≤ **x** ≤ u (componentwise)

- •𝒳 is an axis-aligned rectangle (2D) / box (nD)

2) **Ball constraint**: ‖**x**‖ ≤ R

- •𝒳 is a disk/ball

3) **Simplex**: **x** ≥ **0**, ∑ᵢ xᵢ = 1

- •𝒳 is a triangle (2D) / simplex (nD)

4) **Linear inequalities**: A**x** ≤ **b**

- •𝒳 is a polyhedron (a polygon in 2D)

The shape of 𝒳 often determines which algorithms are natural:

- •“Nice” sets (boxes, balls, simplices) support projections.
- •Linear constraints lead to linear programming.
- •Equality constraints lead to Lagrange multipliers.

### Local optimality on the boundary

A crucial difference from the unconstrained case:

- •The optimum may lie **on the boundary** of 𝒳.
- •At such a point, the unconstrained stationarity condition ∇f(**x**⋆) = **0** typically fails.

Example intuition: minimize f(x) = x over the constraint x ≥ 0.

- •Unconstrained, f decreases by going left forever.
- •Constrained, the best feasible point is x⋆ = 0 on the boundary.
- •But f′(0) = 1 ≠ 0.

So what replaces “gradient is zero”?

### Feasible directions and the tangent idea

At a feasible point **x**⋆, a direction **d** is a **feasible direction** if for small ε > 0, **x**⋆ + ε**d** remains feasible.

Local optimality can be phrased as:

∇f(**x**⋆)ᵀ **d** ≥ 0 for all feasible directions **d**

Interpretation: every allowed infinitesimal move is non-decreasing; you can’t go downhill while staying feasible.

For equality constraints h(**x**) = **0**, feasible directions must satisfy the linearized constraint:

h(**x**⋆ + ε**d**) ≈ h(**x**⋆) + ε ∇h(**x**⋆)ᵀ **d** = 0

Since h(**x**⋆) = 0, this requires:

∇h(**x**⋆)ᵀ **d** = 0

Meaning: **d** lies in the tangent space of the constraint surface.

This is the doorway to **Lagrange multipliers**: at an optimum, the gradient of f must be orthogonal to all tangent directions, so it must lie in the span of constraint normals.

### Constraints as a trade: freedom vs realism

Constraints make the problem more realistic but often harder:

- •They can make the feasible set nonconvex (many disconnected regions).
- •They can create sharp corners where derivatives don’t tell the whole story.
- •They can force solutions onto boundaries where unconstrained intuition breaks.

But constraints also add *structure* that can make some problems easier:

- •Linear constraints + linear objective ⇒ linear programming with strong theory and algorithms.
- •Convex constraints + convex objective ⇒ globally solvable efficiently (in many cases).

### Comparing problem classes (big-picture map)

| Class | Objective | Constraints | Typical guarantee |
| --- | --- | --- | --- |
| Unconstrained smooth | differentiable f | none | local stationarity ∇f = 0 at local optima |
| Equality-constrained | differentiable f | h(**x**) = 0 | Lagrange multipliers / KKT-style conditions |
| Inequality-constrained | differentiable f | g(**x**) ≤ 0 | active-set / KKT conditions |
| Linear programming | linear cᵀ**x** | A**x** ≤ **b** | global optimum at a vertex (if bounded) |

You don’t need all the machinery yet; the goal is to internalize that **constraints redefine what “can’t improve” means**.

## Application/Connection: How Optimization Powers ML, Games, and Algorithms

### Machine learning: training as minimization

In supervised learning, you choose parameters **w** to minimize average loss:

minimize (1/N) ∑\_{i=1}^{N} ℓ( model(**w**, **x**ᵢ), yᵢ ) + λ R(**w**)

- •Objective: data fit + regularization
- •Decision vector: **w** (possibly millions of parameters)
- •Constraints: often none explicitly, but regularization shapes the landscape; sometimes constraints appear (e.g., nonnegativity, norm bounds)

This directly unlocks **gradient descent**, which iteratively updates:

**w** ← **w** − α ∇f(**w**)

### Games: best responses and Nash equilibrium

In a game, each player solves an optimization problem given others’ strategies.

Player k chooses strategy **x**ₖ to maximize payoff uₖ(**x**ₖ, **x**\_{−k}) subject to **x**ₖ ∈ 𝒳ₖ.

A **Nash equilibrium** is a strategy profile where no player can improve by unilateral deviation—an optimality condition across multiple coupled optimization problems.

So optimization vocabulary (objective, feasible set, optimality) is the foundation for equilibrium concepts.

### Equality constraints: physics, geometry, and Lagrange multipliers

When you must satisfy h(**x**) = 0 exactly, the best point often occurs where the objective gradient is “balanced” by constraint gradients.

Lagrange multipliers formalize the idea:

∇f(**x**⋆) + ∑ⱼ λⱼ ∇hⱼ(**x**⋆) = **0**

This is a precise way to express: *at optimum, you cannot move along the constraint surface to decrease f*.

### Linear programming: structure can beat calculus

Not all optimization is calculus-based. In linear programming:

minimize cᵀ**x**

subject to A**x** ≤ **b**

- •The feasible set is a polyhedron.
- •The objective is a plane (or hyperplane) sweeping across it.
- •If the problem is bounded, the optimum occurs at a vertex.

This structural fact enables algorithms like simplex and interior-point methods.

### Choosing the right viewpoint

Optimization problems are often described in different but equivalent ways:

- •**Minimize over a set**: minimize f(**x**) subject to **x** ∈ 𝒳
- •**Constraints as functions**: gᵢ(**x**) ≤ 0, hⱼ(**x**) = 0
- •**Penalty form (soft constraints)**: minimize f(**x**) + ρ · penalty(constraint violation)

These transformations are not just algebra—they determine algorithm choices.

### What you should be able to do after this node

Given a new scenario, you should be able to:

1) Identify the decision vector **x**.

2) Write a scalar objective f(**x**).

3) Specify the feasible set 𝒳 using constraints.

4) Say what “optimal” means (local vs global).

5) For unconstrained differentiable problems, use ∇f(**x**⋆) = **0** as a necessary condition.

That’s the core toolkit you’ll use immediately in gradient descent, and later in Lagrange multipliers and linear programming.

## Worked Examples (3)

### Unconstrained minimization: find stationary points and classify (quickly)

Minimize f(**x**) = x₁² + 2x₂² − 4x₁ − 8x₂ over **x** = (x₁, x₂) ∈ ℝ².

1. Compute the gradient:

   ∇f(**x**) = (∂f/∂x₁, ∂f/∂x₂)

   ∂f/∂x₁ = 2x₁ − 4

   ∂f/∂x₂ = 4x₂ − 8

   So ∇f(**x**) = (2x₁ − 4, 4x₂ − 8).
2. Set the first-order stationarity condition:

   ∇f(**x**⋆) = **0**

   ⇒ 2x₁ − 4 = 0 and 4x₂ − 8 = 0

   ⇒ x₁ = 2, x₂ = 2

   So **x**⋆ = (2, 2).
3. Check that it’s a (global) minimum by completing the square:

   f(**x**) = (x₁² − 4x₁) + 2(x₂² − 4x₂)

   = (x₁² − 4x₁ + 4) − 4 + 2[(x₂² − 4x₂ + 4) − 4]

   = (x₁ − 2)² − 4 + 2(x₂ − 2)² − 8

   = (x₁ − 2)² + 2(x₂ − 2)² − 12.
4. Since (x₁ − 2)² ≥ 0 and 2(x₂ − 2)² ≥ 0 for all **x**, we have:

   f(**x**) ≥ −12

   and equality occurs at **x** = (2, 2).

   Therefore **x**⋆ is the unique global minimizer and f(**x**⋆) = −12.

**Insight:** Stationarity gave the candidate quickly; rewriting the function as a sum of squares showed there’s only one valley bottom, so the stationary point is global.

### Constrained minimization on a boundary: gradient not zero at the optimum

Minimize f(x) = (x − 2)² subject to x ≥ 0.

1. First, solve the unconstrained problem:

   f′(x) = 2(x − 2)

   Set f′(x) = 0 ⇒ x = 2.

   This candidate is feasible because 2 ≥ 0.
2. Compare with the boundary intuition anyway:

   The feasible set is 𝒳 = [0, ∞).

   The unconstrained minimizer x = 2 lies inside 𝒳, so it is also the constrained minimizer.

   Compute value: f(2) = 0.
3. Modify slightly to see the boundary effect: minimize g(x) = (x + 1)² subject to x ≥ 0.

   Unconstrained: g′(x) = 2(x + 1) ⇒ stationary at x = −1 (infeasible).

   So the constrained optimum must occur at the closest feasible point to −1, which is the boundary x⋆ = 0.
4. Check the gradient at the constrained optimum:

   g′(0) = 2(0 + 1) = 2 ≠ 0.

   Yet x⋆ = 0 is optimal because any feasible move must have ε ≥ 0:

   For x ≥ 0, g(x) = (x + 1)² is increasing for x ≥ 0, so x = 0 is best among feasible points.

**Insight:** With constraints, “no improving direction” means no improving *feasible* direction. At a boundary optimum, the derivative/gradient can be nonzero because the decreasing direction points outside the feasible set.

### Feasible set from constraints: turn words into math, then reason about optimality

You choose a 2D decision vector **x** = (x₁, x₂) representing amounts of two resources. You must (i) stay nonnegative, (ii) keep total under 10. Objective: maximize utility u(**x**) = 3x₁ + x₂.

1. Write constraints:

   (i) nonnegative ⇒ x₁ ≥ 0, x₂ ≥ 0

   (ii) budget ⇒ x₁ + x₂ ≤ 10

   So feasible set:

   𝒳 = { **x** ∈ ℝ² : x₁ ≥ 0, x₂ ≥ 0, x₁ + x₂ ≤ 10 }.

   This is a triangle (a 2-simplex scaled by 10).
2. Convert maximization to minimization (optional):

   maximize 3x₁ + x₂ ⇔ minimize f(**x**) = −(3x₁ + x₂).

   But we can reason directly about maximization.
3. Use linear objective intuition:

   Because u(**x**) is linear and 𝒳 is a polygon, the maximum occurs at a vertex of 𝒳 (a cornerstone fact for linear programming).

   Vertices are:

   A = (0, 0)

   B = (10, 0)

   C = (0, 10).
4. Evaluate u at vertices:

   u(A) = 0

   u(B) = 3·10 + 0 = 30

   u(C) = 3·0 + 10 = 10

   So the maximizer is **x**⋆ = (10, 0) with utility 30.

**Insight:** Even before learning simplex, you can often solve small linear programs by: (1) writing the feasible set, (2) listing vertices, (3) checking the objective on vertices.

## Key Takeaways

- ✓

  An optimization problem is: choose a decision vector **x** to minimize or maximize a scalar objective f(**x**) over a feasible set 𝒳.
- ✓

  Constraints (equalities/inequalities) define the feasible set 𝒳; they can force the solution onto the boundary where ∇f(**x**⋆) ≠ **0**.
- ✓

  Global optimality compares against all feasible points; local optimality compares within a neighborhood of **x**⋆ inside 𝒳.
- ✓

  For unconstrained differentiable problems, any local minimizer **x**⋆ must satisfy first-order stationarity: ∇f(**x**⋆) = **0**.
- ✓

  Directional derivatives ∇f(**x**)ᵀ**d** formalize “can I improve by moving along **d**?”; with constraints, only feasible directions matter.
- ✓

  Maximization problems can be converted to minimization by negating the objective: maximize f ⇔ minimize −f.
- ✓

  Problem structure matters: linear objective + linear constraints leads to linear programming; equality constraints motivate Lagrange multipliers; smooth unconstrained problems motivate gradient descent.

## Common Mistakes

- ✗

  Assuming ∇f(**x**⋆) = **0** at constrained optima; boundary solutions often have nonzero gradients.
- ✗

  Confusing local and global optima (especially in nonconvex landscapes): stationarity does not imply global optimality.
- ✗

  Forgetting to define the feasible set precisely (e.g., missing nonnegativity or mixing up ≤ vs ≥), which changes the solution.
- ✗

  Treating maximization and minimization as fundamentally different rather than using the sign-flip equivalence.

## Practice

easy

Write the optimization problem (objective + feasible set) for: “Choose **x** = (x₁, x₂) to minimize cost f(**x**) = (x₁ − 1)² + (x₂ + 2)² subject to x₁ ≥ 0 and x₂ ≥ 0.” Is the unconstrained minimizer feasible?

**Hint:** First find the unconstrained minimizer by minimizing each squared term, then check the constraints.

Show solution

Feasible set: 𝒳 = { **x** ∈ ℝ² : x₁ ≥ 0, x₂ ≥ 0 }.

Unconstrained minimizer occurs at x₁ = 1 and x₂ = −2, i.e., **x** = (1, −2).

This is not feasible because x₂ = −2 < 0.

medium

For f(**x**) = x₁² + x₂², find all stationary points and decide whether they are local/global minima, maxima, or saddle points (unconstrained).

**Hint:** Compute ∇f(**x**) and set it to **0**. Then use geometry: f(**x**) = ‖**x**‖².

Show solution

∇f(**x**) = (2x₁, 2x₂). Stationarity gives x₁ = 0 and x₂ = 0, so the only stationary point is **0**.

Since f(**x**) = ‖**x**‖² ≥ 0 for all **x** and f(**0**) = 0, **0** is a global (and strict local) minimum. There is no maximum because f(**x**) → ∞ as ‖**x**‖ → ∞.

medium

Consider minimize f(x) = x subject to −1 ≤ x ≤ 2. Identify the feasible set, the global minimizer, and check whether f′(x⋆) = 0 at the solution.

**Hint:** A linear function over an interval is minimized at an endpoint.

Show solution

Feasible set: 𝒳 = [−1, 2]. Since f(x) = x increases with x, the minimum occurs at the smallest feasible x: x⋆ = −1.

Derivative f′(x) = 1, so f′(x⋆) = 1 ≠ 0. This is a boundary optimum, so unconstrained stationarity does not apply.

## Connections

[Gradient Descent](/tech-tree/gradient-descent/) builds directly on the idea that −∇f(**x**) is a local improvement direction for unconstrained minimization.

[Lagrange Multipliers](/tech-tree/lagrange-multipliers/) formalizes constrained optimality for equality constraints by relating ∇f(**x**⋆) to constraint gradients.

[Linear Programming](/tech-tree/linear-programming/) specializes optimization to linear objectives and linear constraints, where geometry (vertices of polyhedra) becomes central.

[Nash Equilibrium](/tech-tree/nash-equilibrium/) uses optimization as a building block: each player’s strategy is optimal given others’ strategies, forming a coupled set of optimality conditions.

Quality: A (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
