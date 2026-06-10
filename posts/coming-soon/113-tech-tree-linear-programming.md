---
title: Linear Programming
description: Optimizing linear objective with linear constraints. Simplex method.
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
permalink: /tech-tree/linear-programming/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Linear Programming

OptimizationDifficulty: ★★★★☆Depth: 7Unlocks: 3

Optimizing linear objective with linear constraints. Simplex method.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Feasible region: the intersection of linear constraints, a convex polyhedron of possible solutions
- -Linear objective function: a linear map (c^T x) whose value is to be maximized or minimized over the feasible region
- -Simplex method: an algorithm that moves between basic feasible solutions (vertices) via pivoting to improve the objective until optimality

## Key Symbols & Notation

x (decision variables vector)A, b, c (constraint matrix, right-hand-side vector, objective-coefficient vector)

## Essential Relationships

- -If a finite optimum exists, at least one extreme point (vertex) of the feasible polyhedron - equivalently a basic feasible solution - attains the optimal objective value

## Prerequisites (2)

[Systems of Linear Equations6 atoms](/tech-tree/linear-systems/)[Optimization Introduction5 atoms](/tech-tree/optimization-intro/)

## Unlocks (2)

[Zero-Sum Gameslvl 4](/tech-tree/zero-sum-games/)[Network Flowlvl 4](/tech-tree/network-flow/)

## Referenced by (13)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (12)

[AllocationBusiness

LP is the direct mathematical formalization - the concept description literally names it. Simplex method, feasible regions, objective functions are the formal machinery of allocation](/business/allocation/)[ProfitBusiness

This product-mix problem IS the canonical linear program: maximize c^T x (profit) subject to Ax <= b (labor and material constraints), x >= 0; the simplex method solves it directly](/business/profit/)[BudgetBusiness

Allocating a fixed budget across 20 projects subject to constraints (minimums, dependencies, capacity) is a textbook LP formulation - the mathematical backbone of formal budget optimization](/business/budget/)[budgetingBusiness

Budget allocation across categories with linear constraints (total spend <= income, minimum per category) is literally an LP problem](/business/budgeting/)[resource allocationBusiness

Resource allocation is the canonical LP problem - optimizing a linear objective over linear constraints, with the simplex and interior-point methods as solution machinery](/business/resource-allocation/)[GARPBusiness

Testing GARP and recovering Afriat numbers (utility values and marginal-utility-of-income multipliers) reduces to checking feasibility of a system of linear inequalities, solvable via LP.](/business/garp/)[LaborBusiness

Maximize profit given limited labor and material is the canonical LP problem: linear objective (profit) subject to linear inequality constraints (labor-hours available, material on hand). Shadow prices on the labor constraint quantify the marginal value of one more worker-hour](/business/labor/)[Top-Down AllocationBusiness

Capital allocation across business units subject to budget constraints and return targets is formally an LP: maximize objective (returns) subject to linear constraints (total capital, minimum thresholds, risk limits)](/business/top-down-allocation/)[CFOBusiness

Optimizing factory output, fleet routing, and production line scheduling under capacity and budget constraints are textbook linear programming applications.](/business/cfo/)[OperationsBusiness

The workhorse math behind workforce scheduling, supply chain allocation, store-level inventory positioning, and transportation routing - the canonical operational problems in retail](/business/operations/)[production linesBusiness

Production planning is the canonical LP application - allocating scarce resources (machine hours, labor, materials) across products to maximize output or profit subject to capacity constraints. The simplex method was invented for exactly this class of problem.](/business/production-lines/)[Multi-Brand PortfolioBusiness

Allocating finite capital across N brands with budget, headcount, and operational constraints is a constrained optimization problem](/business/multi-brand-portfolio/)

### From Money (1)

[Asset AllocationMoney

Constraint-based allocation (no shorting, max per asset) is linear programming](/money/asset-allocation/)

Advanced Learning Details

### Graph Position

78

Depth Cost

3

Fan-Out (ROI)

2

Bottleneck Score

7

Chain Length

### Cognitive Load

6

Atomic Elements

67

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (29)

- - Linear program (LP) as a formal optimization problem: maximize or minimize a linear objective subject to linear constraints
- - Standard form of an LP (Ax = b, x ≥ 0) as a canonical representation
- - Slack variables: adding nonnegative variables to convert ≤ constraints to equalities
- - Surplus variables: subtracting variables to convert ≥ constraints to equalities
- - Artificial variables: temporary variables introduced to obtain an initial feasible basis
- - Feasible region of an LP as the intersection of half-spaces (a convex polyhedron / polytope)
- - Extreme point / vertex of the feasible region
- - Basic feasible solution (BFS): solution obtained by selecting a basis and setting nonbasic vars to zero
- - Basis and nonbasic variables: partition of variables into those that define the current solution and those set to zero
- - Basis matrix (B) and nonbasis matrix (N) as the columns of A corresponding to basic/nonbasic vars
- - Representation of a basic solution via x\_B = B^{-1} b
- - Simplex tableau: compact tabular representation of equations, current basic solution, and objective
- - Pivot operation on the tableau (row operations that implement a basis change)
- - Entering variable selection (which nonbasic variable should enter the basis)
- - Leaving variable selection via the minimum ratio test (which basic variable leaves to maintain feasibility)
- - Reduced cost (relative cost) of a nonbasic variable: measure of objective improvement potential
- - Optimality condition in simplex (all reduced costs nonnegative for a maximization problem)
- - Degeneracy: a BFS in which one or more basic variables equal zero
- - Cycling and anti-cycling rules (e.g., Bland's rule) to prevent infinite loops
- - Unboundedness in LP: direction exists that improves objective without bound
- - Infeasibility and detection (no feasible solution exists)
- - Phase I / Phase II simplex method: use of artificial variables to find a feasible basis then optimize
- - Adjacency of vertices: moving along an edge corresponds to exchanging a single basic and nonbasic variable
- - Dual linear program associated with a primal LP
- - Weak duality: dual objective provides a bound on primal objective
- - Strong duality: when both feasible, optimal primal and dual objectives are equal
- - Complementary slackness: conditions relating primal and dual optimality
- - Shadow prices / dual variables interpretation as marginal value of resources
- - Geometric interpretation of simplex: moving between adjacent extreme points to improve objective

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Linear programming (LP) is the rare sweet spot where modeling power meets algorithmic reliability: you can express many real allocation and planning problems with linear constraints and a linear objective—and then solve them efficiently by exploiting geometry (polyhedra) and algebra (pivoting).

TL;DR:

A linear program optimizes a linear objective cᵀx subject to linear constraints (typically Ax ≤ b, plus x ≥ 0). The feasible set is a convex polyhedron; if an optimum exists, there is an optimal vertex (basic feasible solution). The simplex method walks from vertex to vertex by pivoting in a tableau, improving the objective until optimality conditions hold.

## What Is Linear Programming?

## Why LP exists (motivation)

Many decision problems are about **choosing amounts**: how much to produce, ship, invest, schedule, or mix. These decisions interact through **resource limits** (labor hours, budgets, capacities) and **requirements** (demand, minimum levels). When those interactions are well-approximated by **linear relationships**, you get a model that is both expressive and mathematically tractable.

LP is foundational in optimization because it sits at the intersection of:

- •**Modeling clarity**: constraints are readable inequalities.
- •**Geometry**: feasible solutions form a polyhedron, so the optimum lives at a “corner”.
- •**Algorithms**: the simplex method and interior-point methods exploit that structure.

## The formal definition

An LP in common “inequality form” is:

Maximize (or minimize)

- •objective: cᵀx

Subject to

- •Ax ≤ b
- •x ≥ 0

where:

- •**x** ∈ ℝⁿ is the **decision vector** (variables).
- •A ∈ ℝ^{m×n} is the **constraint matrix**.
- •**b** ∈ ℝᵐ is the **right-hand side**.
- •**c** ∈ ℝⁿ are the **objective coefficients**.

You might also see equalities, ≥ inequalities, or variables not restricted to be nonnegative. These are equivalent up to standard transformations (we’ll do those carefully soon).

## Intuition: linear objective + linear constraints

- •A linear constraint like a₁ᵀx ≤ b₁ defines a half-space.
- •The intersection of half-spaces (and possibly equalities) is a **convex polyhedron**.
- •A linear objective cᵀx has level sets that are parallel hyperplanes. As you “slide” the hyperplane in the direction of improvement, it last touches the feasible polyhedron at an **extreme point** (a vertex), unless the optimum is unbounded or the feasible region is empty.

That is the key geometric promise of LP:

> If the feasible region is nonempty and bounded and the objective is linear, then an optimal solution exists at a vertex of the feasible polyhedron.

## A compact vocabulary

Here are the basic terms you will keep using:

| Term | Meaning | How to recognize it |
| --- | --- | --- |
| Feasible solution | Any **x** satisfying all constraints | Ax ≤ b and x ≥ 0 |
| Feasible region | Set of all feasible solutions | Intersection of half-spaces |
| Infeasible LP | No feasible solutions exist | Constraints contradict |
| Unbounded LP | Objective can improve without limit | You can move along a feasible ray increasing cᵀx |
| Optimal solution | Feasible **x** with best objective value | No other feasible point improves cᵀx |
| Vertex / extreme point | “Corner” of polyhedron | Intersection of active constraints |

We’ll now build the mechanics that connect this geometry to the simplex algorithm.

## Core Mechanic 1: Feasible Regions, Vertices, and the “Optimum at a Corner” Principle

## Why geometry matters before algorithms

The simplex method works because it only needs to look at a small subset of points: the **vertices**. To understand why, you need a clear picture of the feasible region and what linear objectives do on convex sets.

## Feasible region as an intersection of half-spaces

Each inequality constraint is a half-space:

- •aᵢᵀx ≤ bᵢ is all points on one side of the hyperplane aᵢᵀx = bᵢ.

The feasible region is:

- •P = { **x** ∈ ℝⁿ : A**x** ≤ **b**, **x** ≥ 0 }

This set P is convex because it is an intersection of convex sets (half-spaces and the nonnegative orthant).

### Convexity (quick but important)

If **x**₁ and **x**₂ are feasible, then for any λ ∈ [0, 1],

- •**x**(λ) = λ**x**₁ + (1 − λ)**x**₂

is also feasible because:

- •A**x**(λ) = A(λ**x**₁ + (1 − λ)**x**₂)

= λA**x**₁ + (1 − λ)A**x**₂

≤ λ**b** + (1 − λ)**b**

= **b**

and **x**(λ) ≥ 0 if **x**₁, **x**₂ ≥ 0.

Convexity is the reason there are no “local maxima” different from the global max for LP; but more importantly, it supports the vertex optimality claim.

## Extreme points / vertices and active constraints

A vertex is a point that cannot be expressed as a nontrivial convex combination of two other feasible points. Operationally in LP, a vertex occurs where enough constraints are **tight** (active) to pin down a unique point.

In ℝ², a vertex is where two non-parallel lines meet (and all constraints hold). In ℝⁿ, you typically need n linearly independent active constraints.

## Why the optimum is at a vertex (intuition)

Consider maximizing cᵀx. The sets {**x** : cᵀx = α} are hyperplanes. Increasing α slides the hyperplane in direction **c**.

- •If the feasible region is bounded, the last contact between those hyperplanes and the feasible set occurs on the boundary.
- •Because the objective is linear, if the last contact happened strictly inside a face (not at a vertex), then every point on that face would share the same objective value. In that case, at least one vertex of that face is also optimal.

So you can search among vertices.

## Degeneracy and multiple optima (important nuance)

Two subtle but common phenomena:

1) **Multiple optimal solutions**

If the objective hyperplane is parallel to a face of the polyhedron, then the last-contact set is a whole edge/face. There are infinitely many optimal solutions, but still at least one optimal vertex.

2) **Degeneracy**

A vertex is degenerate if more than n constraints are active there, causing some basic variables to be zero in simplex form. Degeneracy can make simplex “stall” (no objective improvement on a pivot) and is the source of cycling (rare in practice, but real in theory).

## Standard form as preparation for simplex

The simplex method is most naturally described for **standard form**:

Maximize

- •cᵀx

Subject to

- •A**x** = **b**
- •**x** ≥ 0

How do we convert Ax ≤ b into equalities? Add **slack variables**.

### Slack variables (mechanics)

If you have:

- •aᵢᵀx ≤ bᵢ

introduce slack sᵢ ≥ 0 such that:

- •aᵢᵀx + sᵢ = bᵢ

Stacking all constraints:

- •A**x** + **s** = **b**, with **s** ≥ 0

Now the full variable vector might be **z** = [**x**; **s**] with **z** ≥ 0.

### What a vertex looks like in standard form

In standard form with m equations, a **basic solution** chooses m variables to solve for (the “basic” variables) and sets the rest to 0 (the “nonbasic” variables). If the resulting basic variables are ≥ 0, the solution is a **basic feasible solution (BFS)**, which corresponds to a vertex (under mild non-degeneracy assumptions).

This is the bridge:

- •Geometry: vertices.
- •Algebra: BFS defined by choosing a basis.

Next we’ll make that bridge explicit with simplex pivoting.

## Core Mechanic 2: Simplex Method — Bases, Pivoting, and Optimality Conditions

## Why simplex works (the big idea)

If an optimum exists at a vertex, we can:

1) Start at some vertex (a BFS).

2) Move along edges to adjacent vertices.

3) Improve the objective each step.

4) Stop when no adjacent vertex improves.

The simplex method implements this using linear algebra on a changing set of basic variables.

## Partition variables into basic and nonbasic

Assume standard form:

- •A**x** = **b**, **x** ≥ 0

with A ∈ ℝ^{m×n} and rank m (constraints independent).

Choose an index set B (|B| = m) for basic variables and N for nonbasic variables. Reorder columns so:

- •A = [A\_B A\_N]
- •**x** = [**x**\_B; **x**\_N]

Then constraints become:

- •A\_B **x**\_B + A\_N **x**\_N = **b**

If A\_B is invertible, solve:

- •**x**\_B = A\_B⁻¹(**b** − A\_N **x**\_N)

A **basic solution** sets **x**\_N = 0, giving:

- •**x**\_B = A\_B⁻¹ **b**

This is feasible iff A\_B⁻¹ **b** ≥ 0.

## Objective in terms of nonbasic variables (reduced costs)

Write objective:

- •maximize cᵀx = c\_Bᵀ**x**\_B + c\_Nᵀ**x**\_N

Substitute **x**\_B:

cᵀx = c\_BᵀA\_B⁻¹(**b** − A\_N **x**\_N) + c\_Nᵀ**x**\_N

Work it step-by-step:

= c\_BᵀA\_B⁻¹**b** − c\_BᵀA\_B⁻¹A\_N **x**\_N + c\_Nᵀ**x**\_N

= (c\_BᵀA\_B⁻¹**b**) + (c\_Nᵀ − c\_BᵀA\_B⁻¹A\_N) **x**\_N

Define the **reduced costs**:

- •**r**\_Nᵀ = c\_Nᵀ − c\_BᵀA\_B⁻¹A\_N

Then:

- •objective = constant + **r**\_Nᵀ **x**\_N

### Optimality condition (for maximization)

At a BFS, **x**\_N = 0. If all reduced costs satisfy:

- •**r**\_N ≤ 0 (componentwise)

then increasing any nonbasic variable from 0 cannot increase the objective (because it would contribute **r**ⱼ xⱼ with **r**ⱼ ≤ 0 and xⱼ ≥ 0). Therefore the BFS is optimal.

If some reduced cost is positive, that variable is a candidate to **enter** the basis to improve the objective.

## Pivoting: moving to an adjacent BFS

Suppose variable x\_k (currently nonbasic) has reduced cost r\_k > 0 and we try to increase it. From:

- •**x**\_B = A\_B⁻¹(**b** − A\_k x\_k − …)

the basic variables change linearly with x\_k. To maintain feasibility, we require **x**\_B ≥ 0. This yields a maximum step size (the **ratio test**).

Let **d** = A\_B⁻¹ A\_k be the direction in basic-variable space when x\_k increases by 1. Then:

- •**x**\_B(new) = **x**\_B(old) − **d** · θ

where θ is the amount we increase x\_k.

Feasibility requires:

- •**x**\_B(old) − **d** θ ≥ 0

For components where d\_i > 0:

- •θ ≤ x\_{B,i} / d\_i

So choose:

- •θ\* = min\_{i: d\_i > 0} x\_{B,i} / d\_i

The minimizer index i\* tells you which basic variable hits zero first; that variable **leaves** the basis.

This produces a new basis B′ where x\_k enters and x\_{B,i\*} leaves—an adjacent vertex.

## What about unboundedness?

If for an entering variable x\_k with r\_k > 0 we have d\_i ≤ 0 for all i, then increasing x\_k never makes any basic variable negative. Then θ can grow without bound and the objective increases without bound.

That is the simplex certificate of **unboundedness**.

## Tableau view (operational tool)

In practice simplex is often described via a tableau (a compact way to maintain A\_B⁻¹A and A\_B⁻¹b). Pivot operations perform the basis change without explicitly inverting matrices each step.

Conceptually:

- •Pivot chooses an entering column (improves objective)
- •Pivot chooses a leaving row (ratio test)
- •Row operations update the tableau to represent the new BFS

## Phase I / Phase II (finding a starting BFS)

A hidden requirement so far: we need an initial BFS. If the model is in the form:

- •A**x** = **b**, **x** ≥ 0

and **b** ≥ 0 with slack variables forming an identity matrix, we get a trivial BFS by setting original variables to 0 and slacks to **b**.

But if constraints include:

- •equalities not naturally having slack identity columns,
- •≥ inequalities (need surplus variables),
- •negative b entries,

then a BFS is not obvious.

**Phase I** introduces artificial variables and minimizes their sum to drive them to 0; if the minimum is > 0, the LP is infeasible. If it reaches 0, the resulting basis gives a feasible start for **Phase II**, which optimizes the real objective.

We’ll solidify all of this with worked examples where the algebra and geometry line up clearly.

## Application/Connection: Modeling, Duality Intuition, and Links to Games + Flows

## Why LP modeling is a skill (not just a solver call)

The power of LP comes from turning messy language into:

- •decision variables (what you control),
- •an objective (what “better” means),
- •constraints (what must be true).

A good LP model is:

- •**complete** (captures all real constraints that matter),
- •**linear** (no products of variables, no max/min inside unless linearized),
- •**scaled** (coefficients not wildly different in magnitude).

## Common modeling patterns

### 1) Resource allocation / production planning

Variables: xⱼ = quantity of product j.

Constraints: ∑ aᵢⱼ xⱼ ≤ bᵢ (resource i capacity).

Objective: maximize ∑ pⱼ xⱼ.

### 2) Diet / blending

Variables: xⱼ = amount of ingredient j.

Constraints: nutrition minimums ∑ nᵢⱼ xⱼ ≥ reqᵢ; cost objective.

### 3) Transportation

Variables: x\_{i→j} shipment.

Constraints: supply and demand balance, capacity.

Objective: min cost.

Many of these become special LPs that admit faster algorithms (e.g., network flow), but LP is the unifying language.

## Duality (connection you’ll soon rely on)

Even before a full duality theorem, it helps to internalize the dual’s meaning:

- •The **primal** chooses quantities **x**.
- •The **dual** assigns “prices” **y** to constraints.

For a primal in max form:

Maximize cᵀx

Subject to Ax ≤ b, x ≥ 0

A corresponding dual is:

Minimize bᵀy

Subject to Aᵀy ≥ c, y ≥ 0

Interpretation:

- •yᵢ is the shadow price of resource i.
- •Aᵀy ≥ c means the priced resources cover each product’s profit.
- •bᵀy is the total value of available resources.

Weak duality says:

- •For any feasible **x** and **y**: cᵀx ≤ bᵀy

So the dual provides an upper bound on primal profit (for max problems). At optimum, the bounds meet.

This matters because:

- •It explains optimality conditions.
- •It gives certificates of optimality.
- •It connects LP to game theory (minimax) and to flows (min-cut).

## Connection to Zero-Sum Games

A finite zero-sum game can be written as an LP:

- •Choose a mixed strategy **p** (probabilities) maximizing guaranteed payoff v.

Constraints enforce that expected payoff against each opponent action is ≥ v. That is linear in **p**, and probabilities sum to 1.

Duality aligns with the minimax theorem:

- •max over player A strategies of min payoff = min over player B strategies of max payoff

This is exactly primal-dual equality.

You’ll use LP duality as the algebraic backbone for [Zero-Sum Games](/tech-tree/zero-sum-games/).

## Connection to Network Flow

Max-flow can be expressed as an LP:

- •Variables are flows on edges.
- •Constraints are capacity bounds and flow conservation.
- •Objective is total flow from source to sink.

The dual corresponds to a min-cut-like object. Strong duality yields the max-flow min-cut theorem.

This is why [Network Flow](/tech-tree/network-flow/) feels “LP-shaped” even when solved with specialized algorithms.

## When simplex is used in practice

Despite worst-case exponential examples, simplex is extremely fast on many real problems and remains a workhorse in operations research, often enhanced with:

- •presolve and scaling,
- •advanced pivot rules,
- •sparse linear algebra,
- •warm starts (re-optimizing after small model changes).

For very large, sparse LPs, interior-point methods are also common, but simplex is still essential for sensitivity analysis and re-optimization.

## Worked Examples (3)

### From inequalities to standard form, then identify a basic feasible solution

Consider the LP:

Maximize 3x₁ + 2x₂

Subject to

(1) x₁ + x₂ ≤ 4

(2) 2x₁ + x₂ ≤ 5

x₁ ≥ 0, x₂ ≥ 0

We’ll convert to standard form and find a BFS corresponding to a vertex.

1. Add slack variables s₁, s₂ ≥ 0 to convert ≤ to =:

   x₁ + x₂ + s₁ = 4

   2x₁ + x₂ + s₂ = 5

   Now variables are (x₁, x₂, s₁, s₂) ≥ 0.
2. Write in matrix form A**x** = **b** with **x** = (x₁, x₂, s₁, s₂)ᵀ:

   A = [[1, 1, 1, 0],

   [2, 1, 0, 1]]

   **b** = (4, 5)ᵀ

   Objective coefficients **c** = (3, 2, 0, 0)ᵀ.
3. Find an obvious basis: choose slack variables as basic.

   Take B = {s₁, s₂} and N = {x₁, x₂}. Setting x₁ = x₂ = 0 gives:

   s₁ = 4

   s₂ = 5

   All variables are ≥ 0, so this is a basic feasible solution.
4. Interpret geometrically:

   Setting x₁ = x₂ = 0 corresponds to the origin in the (x₁, x₂) plane.

   At that point, both constraints are slack (not tight): s₁ = 4 and s₂ = 5 represent the distances to the constraint boundaries.

**Insight:** Slack variables do more than “fix” inequalities: they expose an initial BFS (often) and encode which constraints are tight at a vertex (slack = 0) versus loose (slack > 0).

### One simplex pivot by reduced cost + ratio test (numeric walk between vertices)

Use the same LP:

Maximize 3x₁ + 2x₂

s.t. x₁ + x₂ + s₁ = 4

2x₁ + x₂ + s₂ = 5

All variables ≥ 0.

Start at the slack-basis BFS: x₁ = x₂ = 0, s₁ = 4, s₂ = 5.

We’ll perform one improvement step in simplex logic (entering/leaving variables).

1. Current basis B = {s₁, s₂}. Nonbasic N = {x₁, x₂} with x₁ = x₂ = 0.

   Objective value is 0.
2. Compute how increasing a nonbasic variable affects basic variables.

   Because the current basis matrix A\_B is the identity (columns of s₁ and s₂), we have:

   A\_B = [[1, 0],

   [0, 1]]

   So A\_B⁻¹ is also identity, and directions are easy:

   For entering x₁: column A\_{x₁} = (1, 2)ᵀ ⇒ **d** = A\_B⁻¹A\_{x₁} = (1, 2)ᵀ

   For entering x₂: column A\_{x₂} = (1, 1)ᵀ ⇒ **d** = (1, 1)ᵀ
3. Reduced costs in this initial slack basis equal the original objective coefficients because c\_B = (0, 0).

   So r\_{x₁} = 3 and r\_{x₂} = 2.

   Both are positive, so either can enter; pick x₁ (largest reduced cost).
4. Ratio test for x₁:

   Current basic variables are (s₁, s₂) = (4, 5).

   Direction **d** = (1, 2).

   Feasibility requires:

   s₁(new) = 4 − 1·θ ≥ 0 ⇒ θ ≤ 4

   s₂(new) = 5 − 2·θ ≥ 0 ⇒ θ ≤ 5/2

   So θ\* = min(4, 5/2) = 5/2.

   The leaving variable is s₂ (it hits 0 first).
5. Update values at the new BFS:

   Increase x₁ from 0 to θ\* = 5/2.

   Then:

   s₁ = 4 − 1·(5/2) = 3/2

   s₂ = 5 − 2·(5/2) = 0

   x₂ remains 0.

   New BFS: (x₁, x₂, s₁, s₂) = (5/2, 0, 3/2, 0).
6. Objective improvement:

   Old objective = 3·0 + 2·0 = 0

   New objective = 3·(5/2) + 2·0 = 15/2 = 7.5

   So the pivot moved to an adjacent vertex and strictly improved the objective.

**Insight:** A simplex step is exactly: choose an entering variable with positive reduced cost (can improve), then move as far as feasibility allows (ratio test). The leaving variable identifies which constraint becomes tight at the new vertex.

### Detecting unboundedness via simplex logic (feasible ray with improving objective)

Consider:

Maximize x₁ + x₂

Subject to

x₁ − x₂ ≥ 1

x₁, x₂ ≥ 0

We’ll show it’s unbounded by exhibiting a feasible direction that increases the objective forever.

1. Rewrite the constraint:

   x₁ − x₂ ≥ 1

   Equivalently:

   x₁ ≥ 1 + x₂
2. Pick a feasible starting point.

   Let x₂ = 0, then x₁ ≥ 1. Choose (x₁, x₂) = (1, 0). This is feasible.
3. Find a direction **v** that keeps feasibility while increasing objective.

   If we increase both x₁ and x₂ by the same amount t:

   x₁(t) = 1 + t

   x₂(t) = 0 + t

   Check feasibility:

   x₁(t) − x₂(t) = (1 + t) − t = 1 ≥ 1

   So all t ≥ 0 remain feasible.
4. Objective along this ray:

   f(t) = x₁(t) + x₂(t) = (1 + t) + t = 1 + 2t

   As t → ∞, f(t) → ∞.
5. Therefore the LP is unbounded: there is no finite optimal solution.

**Insight:** Unboundedness is not “no constraints”; it means constraints still permit moving along some feasible ray that continually improves cᵀx. Simplex detects this when an entering variable has no limiting ratio test (no positive pivot entries in its direction).

## Key Takeaways

- ✓

  An LP optimizes a linear objective cᵀx over a feasible region defined by linear constraints; the feasible region is a convex polyhedron.
- ✓

  If an optimal solution exists for a bounded feasible LP, at least one optimal solution occurs at a vertex (extreme point).
- ✓

  Converting Ax ≤ b to standard form uses slack variables: aᵢᵀx + sᵢ = bᵢ with sᵢ ≥ 0.
- ✓

  A basic feasible solution (BFS) is obtained by choosing m basic variables (a basis) and setting the remaining nonbasic variables to 0; BFS correspond to vertices.
- ✓

  Simplex improves the objective by pivoting: pick an entering nonbasic variable with positive reduced cost (for maximization), then pick a leaving basic variable via the ratio test to keep feasibility.
- ✓

  Reduced costs **r** tell you whether increasing a nonbasic variable can improve the objective; optimality occurs when all reduced costs are ≤ 0 (maximization).
- ✓

  Simplex can certify unboundedness when a variable can enter (improve objective) but no constraint limits its increase (ratio test has no valid bound).
- ✓

  Phase I/Phase II handles cases where no obvious initial BFS exists; Phase I finds feasibility or proves infeasibility.

## Common Mistakes

- ✗

  Forgetting that simplex needs standard form (equalities + nonnegativity), and mishandling ≥ constraints (which often require surplus + artificial variables).
- ✗

  Assuming the optimum is always unique or always at a single vertex; in LP, an entire edge/face can be optimal when the objective is parallel to that face.
- ✗

  Misapplying the ratio test: only rows with positive direction coefficient (d\_i > 0) constrain the step size; including d\_i ≤ 0 can incorrectly suggest boundedness.
- ✗

  Confusing infeasible with unbounded: infeasible means no point satisfies constraints; unbounded means feasible points exist but objective can improve without limit.

## Practice

easy

Convert to standard form by introducing slack/surplus variables:

Minimize 4x₁ + x₂

Subject to

(1) 3x₁ + x₂ ≥ 6

(2) x₁ + 2x₂ ≤ 8

x₁, x₂ ≥ 0

Write the resulting equality constraints and list all variables with their nonnegativity requirements.

**Hint:** A ≤ constraint gets a +slack. A ≥ constraint becomes an equality by subtracting a surplus variable; to run simplex you would typically add an artificial variable (Phase I), but here just do the structural conversion.

Show solution

For (1) 3x₁ + x₂ ≥ 6, introduce surplus u₁ ≥ 0:

3x₁ + x₂ − u₁ = 6

(If doing simplex Phase I, you would also add an artificial variable a₁ ≥ 0: 3x₁ + x₂ − u₁ + a₁ = 6.)

For (2) x₁ + 2x₂ ≤ 8, introduce slack s₂ ≥ 0:

x₁ + 2x₂ + s₂ = 8

Variables: x₁ ≥ 0, x₂ ≥ 0, u₁ ≥ 0, s₂ ≥ 0 (and optionally a₁ ≥ 0 if building a Phase I starting basis).

medium

Consider the LP:

Maximize 2x₁ + 3x₂

Subject to

x₁ + x₂ ≤ 4

x₁ + 3x₂ ≤ 6

x₁, x₂ ≥ 0

(a) List the corner points (vertices) of the feasible region.

(b) Evaluate the objective at each vertex and identify an optimal solution.

**Hint:** Vertices occur at intersections of constraint boundaries, including with axes: x₁ = 0 or x₂ = 0. Check feasibility for each intersection.

Show solution

(a) Add boundaries:

C1: x₁ + x₂ = 4

C2: x₁ + 3x₂ = 6

Axes: x₁ = 0, x₂ = 0.

Candidate intersections:

1) (0,0) feasible.

2) With x₁ = 0: C1 gives x₂ = 4 ⇒ (0,4) but check C2: 0 + 12 ≤ 6 false, so infeasible. C2 with x₁=0 gives x₂ = 2 ⇒ (0,2) check C1: 0+2 ≤4 ok, feasible.

3) With x₂ = 0: C1 gives x₁ = 4 ⇒ (4,0) check C2: 4 ≤ 6 ok, feasible. C2 gives x₁=6 ⇒ (6,0) but violates C1 (6≤4 false), infeasible.

4) Intersection C1 and C2:

Solve:

x₁ + x₂ = 4

x₁ + 3x₂ = 6

Subtract first from second:

2x₂ = 2 ⇒ x₂ = 1

Then x₁ = 3

So (3,1) is feasible.

Vertices: (0,0), (0,2), (3,1), (4,0).

(b) Objective 2x₁ + 3x₂:

(0,0) → 0

(0,2) → 6

(3,1) → 2·3 + 3·1 = 9

(4,0) → 8

Optimal is (3,1) with value 9.

hard

Unbounded or bounded?

Determine whether the LP is unbounded, infeasible, or has a finite optimum:

Maximize x₁

Subject to

x₁ − x₂ ≤ 1

−x₁ + x₂ ≤ 2

x₁, x₂ ≥ 0

Justify your conclusion using geometry or an improving feasible ray.

**Hint:** Try rewriting the two inequalities as bounds relating x₁ and x₂. Then see if x₁ can grow while maintaining feasibility by increasing x₂ appropriately.

Show solution

Rewrite constraints:

1) x₁ − x₂ ≤ 1 ⇒ x₁ ≤ 1 + x₂

2) −x₁ + x₂ ≤ 2 ⇒ x₂ ≤ 2 + x₁

These imply x₁ is not directly upper-bounded because if x₂ grows with x₁, both can stay feasible.

Construct a feasible ray:

Pick any t ≥ 0 and set x₁ = t, x₂ = t (and note x₁, x₂ ≥ 0).

Check constraints:

1) x₁ − x₂ = t − t = 0 ≤ 1 OK

2) −x₁ + x₂ = −t + t = 0 ≤ 2 OK

Objective is x₁ = t → ∞ as t → ∞.

Therefore the LP is feasible and unbounded.

## Connections

Next nodes you can unlock/apply LP to:

- •[Zero-Sum Games](/tech-tree/zero-sum-games/): game optimal strategies emerge as primal/dual LP solutions (minimax as strong duality).
- •[Network Flow](/tech-tree/network-flow/): max-flow is an LP; min-cut corresponds to a dual certificate.

Helpful background/adjacent nodes:

- •[Systems of Linear Equations](/tech-tree/systems-of-linear-equations/): simplex relies on basis changes, essentially structured Gaussian elimination.
- •[Optimization Introduction](/tech-tree/optimization-introduction/): LP is a key constrained optimization family with especially strong guarantees.

Quality: B (3.9/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
