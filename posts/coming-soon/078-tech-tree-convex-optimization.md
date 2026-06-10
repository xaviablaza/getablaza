---
title: Convex Optimization
description: Optimization where local minimum is global. Efficient algorithms.
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
permalink: /tech-tree/convex-optimization/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Convex Optimization

OptimizationDifficulty: ★★★★☆Depth: 8Unlocks: 11

Optimization where local minimum is global. Efficient algorithms.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Convex set
- -Convex function
- -Convex optimization problem (minimize a convex function over a convex set)

## Key Symbols & Notation

argmin (argument of the minimizer)

## Essential Relationships

- -Convex objective on a convex feasible set implies any local minimum is a global minimum

## Prerequisites (2)

[Convex Functions4 atoms](/tech-tree/convexity/)[Gradient Descent6 atoms](/tech-tree/gradient-descent/)

## Unlocks (5)

[Regularizationlvl 4](/tech-tree/regularization/)[KKT Conditionslvl 4](/tech-tree/kkt-conditions/)[Support Vector Machineslvl 4](/tech-tree/svm/)[Bayesian Optimizationlvl 5](/tech-tree/bayesian-optimization/)[Second-Order Optimizationlvl 5](/tech-tree/second-order-methods/)

## Referenced by (6)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (6)

[Markowitz Portfolio TheoryBusiness

Mean-variance portfolio optimization is a convex quadratic program (minimize quadratic variance subject to linear return and budget constraints). The efficient frontier is its Pareto-optimal solution set.](/business/markowitz-portfolio-theory/)[Risk-Adjusted ReturnBusiness

Markowitz mean-variance portfolio construction is a quadratic program (minimize w'Σw subject to return and weight constraints) - a canonical convex optimization problem whose efficient frontier maps directly to this concept](/business/risk-adjusted-return/)[Efficient FrontierBusiness

Computing the efficient frontier is a quadratic (convex) optimization: minimize portfolio variance w^T Σ w subject to a target return constraint and weight constraints](/business/efficient-frontier/)[trading ordersBusiness

Optimal trade execution - minimizing market impact and transaction costs subject to fill constraints - is typically formulated as constrained convex optimization over continuous order parameters](/business/trading-orders/)[Investment PortfolioBusiness

Mean-variance portfolio optimization (Markowitz) is the canonical convex quadratic program - minimize portfolio variance subject to return and weight constraints on the efficient frontier](/business/investment-portfolio/)[AllocatorBusiness

Portfolio construction is constrained optimization (Markowitz mean-variance) - maximize expected return subject to risk budget, capital constraints, and diversification requirements](/business/allocator/)

Advanced Learning Details

### Graph Position

70

Depth Cost

11

Fan-Out (ROI)

6

Bottleneck Score

8

Chain Length

### Cognitive Load

5

Atomic Elements

46

Total Elements

L3

Percentile Level

L3

Atomic Level

### All Concepts (19)

- - Convex optimization problem: formulation as 'minimize f(x) subject to x ∈ C' where f is convex and C is a convex feasible set
- - Feasible set / convex constraint set: set of points satisfying constraints (must be convex for convex optimization)
- - Global vs. local minimum in optimization (and the significance that, in convex problems, any local minimum is a global minimum)
- - Optimal value (the minimum objective value) and optimizer/solution set (argmin)
- - Lagrangian function L(x, λ) for constrained problems
- - Dual problem (Lagrange dual) and the dual variables (multipliers) λ
- - Duality concepts: primal problem, dual problem, dual function, and duality gap
- - Slater's condition (a convex constraint qualification ensuring strong duality)
- - Karush–Kuhn–Tucker (KKT) conditions as optimality conditions in convex constrained problems
- - Strong (and strict) convexity and its implications (e.g., uniqueness of minimizer, faster convergence)
- - Subgradient and subdifferential for nondifferentiable convex functions
- - Projected gradient methods (projection onto the feasible set after a gradient step)
- - Projection onto a convex set (nearest-point operator onto C)
- - Proximal operator and proximal algorithms (proximal point, ISTA, FISTA, etc.)
- - Interior-point methods as an efficient family of algorithms for many convex problems
- - Subgradient methods for nonsmooth convex optimization
- - Standard convex problem classes and examples (linear programming, quadratic programming, semidefinite programming)
- - Epigraph reformulation (representing convex problems via the epigraph) and other convex reformulations
- - Convergence rates and complexity statements commonly used in convex optimization (qualitative and quantitative rates)

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Many optimization problems in ML feel like hiking in fog: you follow the steepest downhill direction and hope you’re heading toward the right valley. Convex optimization is the rare case where the landscape is shaped so kindly that every local valley is the same valley—once you get low enough, you can be confident you’ve reached the global minimum. That single geometric guarantee is why convex optimization sits at the core of reliable, scalable learning algorithms.

TL;DR:

A convex optimization problem minimizes a convex objective over a convex feasible set. Its defining superpower is: any local minimizer is a global minimizer. This enables strong guarantees (existence/uniqueness under conditions, duality, certificates of optimality) and efficient algorithms (projected gradient, interior-point, proximal methods).

## What Is Convex Optimization?

### The motivation (why we care)

In general optimization, you can easily get stuck in a **local** minimum that isn’t the **global** minimum. That uncertainty forces you to rely on heuristics, restarts, and luck.

Convex optimization is the opposite: it’s a mathematical setting where the geometry of the problem rules out “bad” local minima. When you solve a convex optimization problem, you get a solution you can trust—and you can often quantify how close you are to optimal at every step.

This is why convex optimization underpins so many standard ML models: ridge regression, LASSO, logistic regression (with convex losses), SVMs, and many regularized empirical risk minimization problems.

### Definition (the core object)

A **convex optimization problem** has the form

minimize f(x)

subject to x ∈ C

where:

- •f is a **convex function**
- •C is a **convex set** (the feasible region)

A point x⋆ is an optimizer if it attains the smallest objective value among feasible points:

x⋆ ∈ argmin\_{x ∈ C} f(x)

Here, **argmin** (“argument of the minimizer”) returns the set of points that minimize f over C. (There can be multiple minimizers.)

### The defining property: local = global

If f is convex and C is convex, then:

- •Any **local minimizer** is a **global minimizer**.

Intuitively: convexity prevents the objective from dipping down and then rising and dipping again in a way that would create a “fake” valley.

More formally, if x̂ is feasible and there exists a neighborhood around x̂ where f(x̂) ≤ f(x) for all feasible x in that neighborhood, then convexity implies f(x̂) ≤ f(x) for all x ∈ C.

### Geometry picture you should hold in your head

Think of two ingredients:

1) **Convex set C**: if you pick any two feasible points x₁, x₂ ∈ C, then the entire line segment is feasible:

∀t ∈ [0, 1], t x₁ + (1 − t) x₂ ∈ C

2) **Convex function f**: the value at a mixture is no more than the mixture of values:

f(t x₁ + (1 − t) x₂) ≤ t f(x₁) + (1 − t) f(x₂)

Those two combine into a landscape with no “hidden basins.”

### Standard forms (so you can recognize them)

Most convex problems are written using inequalities and equalities:

minimize f₀(x)

subject to fᵢ(x) ≤ 0 for i = 1,…,m

A x = b

If f₀ is convex, each fᵢ is convex, and A x = b is affine, then the feasible set is convex and the whole problem is convex.

### What convex optimization is not

- •It is **not** “always easy.” Some convex problems can be large-scale and require careful numerical methods.
- •It is **not** “only quadratic.” Quadratic programs are one class; many others exist (LP, SOCP, SDP, etc.).
- •It is **not** “gradient descent only.” Gradient descent is one tool; convexity enables a broad toolbox with guarantees.

### A quick taxonomy

Here are common convex problem families you’ll see in ML and systems:

| Problem class | Objective / constraints | Notes |
| --- | --- | --- |
| LP (Linear Program) | linear objective, linear inequalities | extremely well-studied; piecewise-linear geometry |
| QP (Quadratic Program) | convex quadratic objective, linear constraints | includes least squares + constraints |
| SOCP | second-order cone constraints | norms like ‖A x + b‖₂ ≤ cᵀx + d |
| SDP | semidefinite constraints X ⪰ 0 | powerful but heavier computationally |
| Unconstrained smooth convex | just minimize f(x) | gradient methods shine |
| Composite convex | f(x) = g(x) + h(x) | g smooth, h nonsmooth (e.g., L1) → proximal methods |

Convex optimization is the umbrella that organizes these into one coherent theory.

## Core Mechanic 1: Optimality Conditions (First-Order, Subgradients, and Geometry)

### Why optimality conditions matter

In optimization, you want a **certificate** that a candidate solution is optimal.

- •For general nonconvex problems, even ∇f(x) = 0 doesn’t guarantee a minimum.
- •For convex problems, first-order information becomes much more powerful.

Optimality conditions become both:

1) conceptual tools (understanding solutions), and

2) algorithmic stopping criteria (when to stop iterating).

---

## Unconstrained, differentiable case: ∇f(x⋆) = 0 is enough

Suppose f is convex and differentiable on ℝⁿ. Then x⋆ minimizes f over ℝⁿ if and only if

∇f(x⋆) = 0.

### Why this is true (the key inequality)

Convexity implies the **first-order condition**:

f(y) ≥ f(x) + ∇f(x)ᵀ (y − x) for all x, y.

This says the tangent hyperplane at x underestimates the function everywhere.

Now plug x = x⋆. If ∇f(x⋆) = 0, then for any y:

f(y) ≥ f(x⋆) + 0ᵀ (y − x⋆) = f(x⋆).

So x⋆ is globally optimal.

---

## Constrained case: gradients meet geometry (normal cones)

Now consider minimize f(x) subject to x ∈ C, where C is convex and closed.

Even if ∇f(x⋆) ≠ 0, x⋆ can be optimal because the constraint blocks descent directions.

### Feasible directions

A direction **d** is feasible at x⋆ if small steps stay in C:

∃ε > 0 such that x⋆ + t **d** ∈ C for all t ∈ [0, ε].

If x⋆ is optimal, you should not be able to decrease f by moving in any feasible direction.

For differentiable f, the directional derivative is

( d/dt ) f(x⋆ + t **d**) |\_{t=0} = ∇f(x⋆)ᵀ **d**.

Optimality requires

∇f(x⋆)ᵀ **d** ≥ 0 for all feasible directions **d**.

Geometrically: the gradient points “out of” the feasible set.

### Normal cone condition (clean convex statement)

Define the **normal cone** of C at x⋆:

N\_C(x⋆) = { **g** : **g**ᵀ (x − x⋆) ≤ 0 for all x ∈ C }.

Then x⋆ solves min\_{x∈C} f(x) (with differentiable convex f) iff

−∇f(x⋆) ∈ N\_C(x⋆).

This is the geometric version of constrained optimality.

---

## Nonsmooth convex functions: subgradients

Many important convex functions are not differentiable:

- •absolute value |x|
- •L1 norm ‖x‖₁
- •hinge loss max(0, 1 − y wᵀx)

Convex optimization still works because we generalize gradients.

### Subgradient definition

A vector **g** is a subgradient of convex f at x if

f(y) ≥ f(x) + **g**ᵀ (y − x) for all y.

The set of all subgradients is the **subdifferential**:

∂f(x) = { **g** : **g** is a subgradient at x }.

If f is differentiable at x, then ∂f(x) = {∇f(x)}.

### Optimality with subgradients

Unconstrained case: x⋆ minimizes convex f over ℝⁿ iff

**0** ∈ ∂f(x⋆).

Constrained case: x⋆ minimizes f over C iff

**0** ∈ ∂f(x⋆) + N\_C(x⋆).

This is a bridge to KKT conditions (which you’ll learn next as an unlocked node): KKT is essentially an explicit form of “subgradient + normal cone = 0” for inequality/equality constraints.

---

## Strong convexity and uniqueness (why you sometimes get one answer)

Convexity ensures global minima are well-behaved, but not necessarily unique.

A function is **µ-strongly convex** if for all x, y and t ∈ [0,1]:

f(t x + (1−t) y) ≤ t f(x) + (1−t) f(y) − (µ/2) t(1−t) ‖x−y‖₂².

Equivalent (when twice differentiable):

∇²f(x) ⪰ µ I.

Strong convexity implies:

- •the minimizer is unique (over a convex set, assuming feasibility)
- •gradient methods converge faster and more predictably

In ML, adding L2 regularization (λ/2)‖**w**‖₂² often makes objectives strongly convex.

---

## A quick mental checklist for “is this convex optimization?”

To decide if a problem is convex, verify:

1) Objective f₀ is convex.

2) Each inequality constraint fᵢ(x) ≤ 0 has fᵢ convex.

3) Equality constraints are affine.

4) Domain restrictions (like x > 0) define a convex set.

Once those hold, you gain the full power of convex optimality conditions and duality-based certificates.

## Core Mechanic 2: Algorithms with Guarantees (Projected Gradient, Proximal Methods, Interior-Point Intuition)

### Why convexity changes algorithms

You already know **gradient descent**: iterate

x\_{k+1} = x\_k − α\_k ∇f(x\_k).

In nonconvex landscapes, this can converge to saddle points or poor local minima.

In convex optimization, algorithms are designed around two privileges:

1) **Any stationary point is globally optimal** (with the right notion of stationarity).

2) We can measure progress via **optimality gaps** f(x\_k) − f(x⋆).

This section focuses on three algorithmic ideas you’ll see constantly.

---

## 1) Projected Gradient Descent (PGD)

### When you use it

When you want to minimize a smooth convex f over a simple convex set C (box constraints, ball constraints, simplex, etc.).

### The core update

Take a gradient step, then project back to feasibility:

x\_{k+1} = Π\_C( x\_k − α\_k ∇f(x\_k) )

where Π\_C(z) = argmin\_{x∈C} ‖x − z‖₂.

### Why projection is the right repair

If you take an unconstrained step, you might leave C. Projection finds the closest feasible point in Euclidean distance.

The projection itself is a convex optimization problem, but for many sets it has a closed form:

| Set C | Projection Π\_C(z) |
| --- | --- |
| Box [ℓ, u] | clip each coordinate to [ℓᵢ, uᵢ] |
| ℓ₂ ball {x: ‖x‖₂ ≤ r} | if ‖z‖₂ ≤ r then z else r z / ‖z‖₂ |
| Simplex {x ≥ 0, ∑ xᵢ = 1} | sort + threshold (O(n log n)) |

### Convergence (high-level)

If ∇f is L-Lipschitz (smooth), and α ∈ (0, 1/L], PGD achieves

f(x\_k) − f(x⋆) = O(1/k)

and with strong convexity you can get linear convergence.

---

## 2) Composite objectives and Proximal Gradient

### Why you need it

Many ML objectives are sums:

minimize g(x) + h(x)

where:

- •g is convex and smooth (easy gradient)
- •h is convex but possibly nonsmooth (e.g., λ‖x‖₁)

Plain gradient descent struggles with nonsmooth terms because ∇h may not exist.

### Proximal operator

Define the proximal operator of h:

prox\_{α h}(z) = argmin\_x ( 1/(2α) ‖x − z‖₂² + h(x) ).

Then proximal gradient updates:

x\_{k+1} = prox\_{α h}( x\_k − α ∇g(x\_k) ).

This looks like “gradient step on g” followed by a structured correction that handles h.

### Key example: soft-thresholding for L1

If h(x) = λ‖x‖₁, then prox has a closed form coordinatewise:

[prox\_{αλ‖·‖₁}(z)]ᵢ = sign(zᵢ) · max(|zᵢ| − αλ, 0).

That single formula is the engine behind efficient sparse learning (LASSO, sparse logistic regression).

### Convergence (high-level)

For convex g+h with g smooth:

f(x\_k) − f(x⋆) = O(1/k)

and accelerated variants (FISTA) achieve O(1/k²).

---

## 3) Interior-point methods (intuition, not implementation)

### Why they matter

Interior-point methods are among the most powerful general-purpose solvers for many convex problems (LP, QP, SOCP, SDP) at moderate scale.

They’re less common in very large-scale ML training loops (where first-order methods dominate), but they’re essential for:

- •high-accuracy solutions
- •problems with complex constraints
- •building dual certificates

### The central idea: barrier functions

Suppose you have inequality constraints fᵢ(x) ≤ 0. An interior method solves a sequence of unconstrained problems:

minimize f₀(x) + (1/t) ∑\_{i=1}^m ϕ(−fᵢ(x))

where ϕ is a barrier like −log(·), and t increases over time.

As t → ∞, the barrier weight 1/t → 0, and solutions approach the constrained optimum while staying strictly feasible.

### Why convexity makes this stable

The barrier-augmented objective remains convex (sum of convex functions), and Newton-type steps behave predictably.

---

## Choosing an algorithm (practical comparison)

| Situation | Best-fit method | Why |
| --- | --- | --- |
| Smooth f, simple constraint set C | Projected gradient / accelerated PGD | projection is cheap; scales well |
| g smooth + h nonsmooth with simple prox | Proximal gradient / FISTA | handles L1, hinge-like terms efficiently |
| Medium-scale constrained LP/QP/SOCP/SDP | Interior-point solver | high accuracy, robust, strong theory |
| Huge data, streaming, noisy gradients | (Stochastic) gradient / variance-reduced methods | cheap iterations; convexity still gives guarantees |

The unifying theme is that convexity provides a **progress metric** (optimality gap) and often a **certificate** (duality/KKT) that your algorithm has succeeded.

## Application/Connection: Duality, Certificates, and ML Models (Regularization, SVMs, and Beyond)

### Why duality is the natural next step

Convex optimization is not just about finding x⋆. It’s also about knowing you’ve found it.

Duality gives:

- •lower bounds on the optimal value (so you can bound suboptimality)
- •alternative problem formulations (sometimes easier to solve)
- •interpretability (shadow prices, margins)

This node unlocks **KKT conditions** because KKT is the language that connects primal feasibility, dual feasibility, and complementary slackness into a single optimality certificate.

---

## Primal vs dual: the idea in one paragraph

For many constrained convex problems, you form a Lagrangian

L(x, λ, ν) = f₀(x) + ∑\_{i=1}^m λᵢ fᵢ(x) + νᵀ(Ax − b)

with λ ≥ 0.

The **dual function** is

g(λ, ν) = inf\_x L(x, λ, ν).

Then the **dual problem** is

maximize g(λ, ν)

subject to λ ≥ 0.

Weak duality always holds: dual optimum ≤ primal optimum.

In convex optimization, strong duality often holds under mild conditions (e.g., Slater’s condition), meaning the dual optimum equals the primal optimum—giving a tight certificate.

---

## Connection to Regularization (unlocked node)

Regularization commonly produces convex objectives.

### L2 (ridge) regularization

Example objective:

minimize (1/n) ∑\_{i=1}^n (yᵢ − **w**ᵀ **x**ᵢ)² + (λ/2) ‖**w**‖₂²

- •The squared loss is convex in **w**.
- •The L2 term is convex and makes the objective strongly convex.

Practical meaning:

- •unique minimizer
- •stable training
- •better-conditioned problems

### L1 (LASSO) regularization

minimize (1/n) ∑ (yᵢ − **w**ᵀ **x**ᵢ)² + λ‖**w**‖₁

This is convex but nonsmooth. Proximal methods solve it efficiently, and the nonsmoothness is what enables sparsity.

---

## Connection to Support Vector Machines (unlocked node)

The classic soft-margin SVM can be written as a convex optimization problem.

One common primal form:

minimize (1/2)‖**w**‖₂² + C ∑\_{i=1}^n ξᵢ

subject to yᵢ(**w**ᵀ **x**ᵢ + b) ≥ 1 − ξᵢ

ξᵢ ≥ 0

This is a convex QP:

- •quadratic objective with PSD Hessian (from ‖**w**‖₂²)
- •linear constraints

The dual form reveals:

- •only inner products **x**ᵢᵀ **x**ⱼ matter (gateway to kernels)
- •support vectors correspond to active constraints

This is a perfect example of how convex optimization structures an ML model end-to-end: formulation → algorithm → certificate → interpretation.

---

## Connection to Second-Order Optimization (unlocked node)

Convexity interacts beautifully with Hessian-based methods.

If f is twice differentiable convex, then ∇²f(x) ⪰ 0 everywhere. This means:

- •Newton steps are well-defined (Hessian not indefinite)
- •locally, the quadratic approximation is trustworthy

Interior-point methods essentially rely on Newton-like steps on barrier-augmented convex objectives.

Meanwhile, quasi-Newton methods (BFGS, L-BFGS) are often effective on convex problems because they build PSD curvature approximations.

---

## Connection to Bayesian Optimization (unlocked node)

Bayesian optimization targets global optimization of expensive black-box functions, typically nonconvex.

So why does convex optimization matter?

- •Many acquisition functions (or subproblems inside Bayesian optimization) are solved with convex relaxations.
- •Convex optimization provides baselines and certificates: if your expensive objective is convex (rare but possible), Bayesian optimization is overkill.
- •Convex modeling ideas (convex surrogates, convex constraints) often appear when designing safe exploration.

---

## A final “systems” viewpoint: convex optimization as a modeling language

Convex optimization is often less about calculus and more about **modeling**:

- •express goals and constraints in a way that preserves convexity
- •choose a solver that exploits structure
- •interpret solutions via dual variables and KKT

Once you start thinking this way, many problems become: “Can I rewrite this to be convex (or approximately convex)?” That’s a major professional skill in ML, operations research, and control.

## Worked Examples (3)

### Example 1: Projection onto an ℓ₂ Ball (building block for Projected Gradient Descent)

Compute Π\_C(**z**) where C = {**x** ∈ ℝⁿ : ‖**x**‖₂ ≤ r} and **z** is given. This projection is used in constrained convex optimization like min f(**x**) s.t. ‖**x**‖₂ ≤ r.

1. We want the closest feasible point:

   Π\_C(**z**) = argmin\_{‖**x**‖₂ ≤ r} ‖**x** − **z**‖₂.
2. Case 1: **z** is already feasible.

   If ‖**z**‖₂ ≤ r, then choosing **x** = **z** yields objective 0, which is minimal.

   So Π\_C(**z**) = **z**.
3. Case 2: ‖**z**‖₂ > r.

   The solution must lie on the boundary ‖**x**‖₂ = r (otherwise we could move toward **z** and reduce distance).
4. Use the fact that the closest point on a sphere to **z** lies on the ray from the origin through **z**.

   So let **x** = α **z** with α ≥ 0.
5. Impose feasibility:

   ‖α **z**‖₂ = α ‖**z**‖₂ = r ⇒ α = r / ‖**z**‖₂.
6. Therefore the projection is:

   Π\_C(**z**) = r **z** / ‖**z**‖₂ when ‖**z**‖₂ > r.

**Insight:** Projections encode constraints as geometry. For many convex sets used in ML, Π\_C has a simple closed form—making projected gradient methods practical at scale.

### Example 2: Solve a Strongly Convex Quadratic and Identify argmin

Minimize f(**x**) = 1/2 **x**ᵀQ**x** + **c**ᵀ**x** over ℝⁿ where Q ⪰ µI for some µ > 0 (so Q is positive definite). Find argmin and explain why it’s unique.

1. Because Q ⪰ µI with µ > 0, f is µ-strongly convex. Strong convexity implies the minimizer is unique.
2. Compute the gradient:

   ∇f(**x**) = ∇(1/2 **x**ᵀQ**x**) + ∇(**c**ᵀ**x**)

   = Q**x** + **c**.
3. Set first-order optimality condition (unconstrained convex):

   ∇f(**x**⋆) = **0** ⇒ Q**x**⋆ + **c** = **0**.
4. Solve the linear system:

   Q**x**⋆ = −**c**

   ⇒ **x**⋆ = −Q⁻¹ **c**.
5. Therefore:

   argmin\_{**x**∈ℝⁿ} f(**x**) = { −Q⁻¹ **c** } (a singleton set).

**Insight:** For convex quadratics, optimization reduces to solving linear systems. Strong convexity (Q ≻ 0) upgrades “a minimizer exists” to “the minimizer is unique,” which is crucial for stability in learning.

### Example 3: Proximal Operator of λ‖·‖₁ (Soft-Thresholding)

Compute prox\_{α λ‖·‖₁}(**z**) for **z** ∈ ℝⁿ. This is the key step in LASSO and sparse logistic regression.

1. By definition:

   prox\_{α λ‖·‖₁}(**z**) = argmin\_{**x**} (1/(2α))‖**x** − **z**‖₂² + λ‖**x**‖₁.
2. The objective separates by coordinates because both terms are sums:

   (1/(2α))∑(xᵢ − zᵢ)² + λ∑|xᵢ|

   = ∑ [ (1/(2α))(xᵢ − zᵢ)² + λ|xᵢ| ].
3. So we can minimize each coordinate independently:

   xᵢ⋆ = argmin\_{x} (1/(2α))(x − zᵢ)² + λ|x|.
4. Consider the 1D subgradient optimality condition.

   For x ≠ 0, derivative is:

   (1/α)(x − zᵢ) + λ sign(x) = 0.
5. If x > 0:

   (1/α)(x − zᵢ) + λ = 0 ⇒ x = zᵢ − αλ.

   This is consistent with x > 0 only if zᵢ > αλ.
6. If x < 0:

   (1/α)(x − zᵢ) − λ = 0 ⇒ x = zᵢ + αλ.

   This is consistent with x < 0 only if zᵢ < −αλ.
7. If |zᵢ| ≤ αλ, the optimum is x = 0 (you can verify using subgradients of |x| at 0, which is [−1, 1]).
8. Combine cases:

   xᵢ⋆ = sign(zᵢ) · max(|zᵢ| − αλ, 0).

**Insight:** The prox step doesn’t merely “nudge” parameters—it can set them exactly to 0. That discrete sparsity effect comes from convex but nonsmooth geometry, not from any heuristic.

## Key Takeaways

- ✓

  A convex optimization problem minimizes a convex function over a convex set; its hallmark guarantee is that any local minimum is global.
- ✓

  argmin returns the set of minimizers; convex problems may have multiple solutions unless the objective is strongly convex.
- ✓

  First-order convexity inequality: f(y) ≥ f(x) + ∇f(x)ᵀ(y−x) is the engine behind many proofs and algorithms.
- ✓

  Unconstrained differentiable convex minimization: x⋆ is optimal iff ∇f(x⋆) = **0**.
- ✓

  With constraints, optimality is geometric: −∇f(x⋆) lies in the normal cone N\_C(x⋆); equivalently **0** ∈ ∂f(x⋆) + N\_C(x⋆) for nonsmooth cases.
- ✓

  Projected gradient handles simple convex constraints via x\_{k+1} = Π\_C(x\_k − α∇f(x\_k)).
- ✓

  Proximal gradient handles composite objectives g + h where h is nonsmooth but has an efficient prox (e.g., L1 soft-thresholding).
- ✓

  Duality (and then KKT) turns optimality into a verifiable certificate and often yields alternative, more efficient solution pathways (e.g., SVM dual, kernelization).

## Common Mistakes

- ✗

  Assuming “convex” means “differentiable.” Many key convex problems are nonsmooth (L1, hinge loss) and require subgradients or proximal methods.
- ✗

  Checking only the objective for convexity while ignoring constraints. Nonconvex feasible sets break the local=global guarantee even if f is convex.
- ✗

  Treating argmin as a single point by default. Without strong convexity (or other conditions), argmin can be a set.
- ✗

  Using gradient descent on constrained problems without projection (or another constraint-handling method), then misinterpreting infeasible iterates as meaningful.

## Practice

easy

Let f(x) = |x|. Compute ∂f(0) and use it to determine whether x⋆ = 0 is a minimizer of f over ℝ.

**Hint:** Use the subgradient inequality f(y) ≥ f(0) + g(y−0) for all y to find all valid g at 0.

Show solution

We need all g such that |y| ≥ 0 + g y for all y.

For y > 0: |y| = y, inequality becomes y ≥ g y ⇒ 1 ≥ g.

For y < 0: |y| = −y, inequality becomes −y ≥ g y. Divide by y (negative) flips sign: −1 ≤ g.

Thus ∂f(0) = [−1, 1].

Optimality for unconstrained convex minimization is 0 ∈ ∂f(x⋆). Since 0 ∈ [−1,1], x⋆ = 0 is a global minimizer.

medium

Consider minimize f(**x**) = 1/2 ‖A**x** − **b**‖₂² subject to ‖**x**‖₂ ≤ r. Write the projected gradient descent update explicitly (in terms of A, **b**, r).

**Hint:** Compute ∇f(**x**) first, then apply the ℓ₂-ball projection formula from the worked example.

Show solution

We have f(**x**) = 1/2 ‖A**x** − **b**‖₂².

Gradient:

∇f(**x**) = Aᵀ(A**x** − **b**).

A PGD step with step size α is:

**z** = **x**\_k − α Aᵀ(A**x**\_k − **b**).

Then project onto C = {‖**x**‖₂ ≤ r}:

If ‖**z**‖₂ ≤ r, set **x**\_{k+1} = **z**.

Else set **x**\_{k+1} = r **z** / ‖**z**‖₂.

hard

Show that if f is µ-strongly convex on a convex set C, then it has at most one minimizer on C.

**Hint:** Assume there are two distinct minimizers x₁ and x₂ with equal objective value, then apply strong convexity to the midpoint (or general t).

Show solution

Assume for contradiction there exist two distinct minimizers x₁ ≠ x₂ in C such that f(x₁) = f(x₂) = f⋆.

Since C is convex, for any t ∈ (0,1), x\_t = t x₁ + (1−t) x₂ ∈ C.

Strong convexity gives:

f(x\_t) ≤ t f(x₁) + (1−t) f(x₂) − (µ/2) t(1−t) ‖x₁−x₂‖₂².

Substitute f(x₁)=f(x₂)=f⋆:

f(x\_t) ≤ f⋆ − (µ/2) t(1−t) ‖x₁−x₂‖₂².

Because µ > 0, t(1−t) > 0, and ‖x₁−x₂‖₂² > 0, the right-hand side is strictly less than f⋆.

So f(x\_t) < f⋆, contradicting that f⋆ is the minimum value on C.

Therefore, there cannot be two distinct minimizers; the minimizer is unique (argmin is a singleton).

## Connections

- •Next: [KKT Conditions](/tech-tree/kkt-conditions/) — turns convex optimality into explicit primal/dual feasibility plus complementary slackness.
- •Next: [Regularization](/tech-tree/regularization/) — many regularizers yield convex (often strongly convex) objectives; proximal methods become essential.
- •Next: [Support Vector Machines](/tech-tree/svm/) — a classic convex QP whose dual exposes margins, support vectors, and kernels.
- •Next: [Second-Order Optimization](/tech-tree/second-order-methods/) — Newton and quasi-Newton methods are especially well-behaved for convex objectives.
- •Related: [Convex Functions](/tech-tree/convex-functions/) — the prerequisite node that provides the geometric inequality used throughout this lesson.

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
