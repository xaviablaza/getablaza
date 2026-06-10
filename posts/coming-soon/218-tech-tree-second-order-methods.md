---
title: Second-Order Optimization
description: Newton's method, BFGS, L-BFGS. Using Hessian information.
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
inspiration_url: https://templeton.host/tech-tree/second-order-methods/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/second-order-methods/](https://templeton.host/tech-tree/second-order-methods/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Second-Order Optimization

OptimizationDifficulty: ★★★★★Depth: 9Unlocks: 0

Newton's method, BFGS, L-BFGS. Using Hessian information.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Second-order local quadratic model (second-order Taylor approximation) as the basis for computing steps
- -Quasi-Newton inverse-Hessian approximation (low-cost matrix or limited-memory representation that approximates H^{-1}, e.g., BFGS/L-BFGS)

## Key Symbols & Notation

H - Hessian matrix (matrix of second derivatives)B - inverse-Hessian approximation (matrix used by quasi-Newton methods)

## Essential Relationships

- -Newton linear system: H p = -grad f (equivalently p = -H^{-1} grad f) - the Newton step minimizes the local quadratic model
- -Quasi-Newton secant condition: B\_{k+1} s\_k = y\_k with s\_k = x\_{k+1}-x\_k and y\_k = grad\_{k+1}-grad\_k, enforcing that B approximates H^{-1}

## Prerequisites (2)

[Matrix Calculus6 atoms](/tech-tree/matrix-calculus/)[Convex Optimization5 atoms](/tech-tree/convex-optimization/)

Advanced Learning Details

### Graph Position

94

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

9

Chain Length

### Cognitive Load

6

Atomic Elements

69

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (30)

- - Newton's method as an iterative root-finding method applied to the gradient (solve ∇f(x)=0) to obtain steps for optimization
- - Newton step/direction: p\_N = -H^{-1} g (solving the linear system H p = -g)
- - Local quadratic model of the objective via second-order Taylor expansion and using its minimizer as a step
- - Newton decrement as a scalar measure of model/trustworthiness and suboptimality (related to g^T H^{-1} g)
- - Quadratic convergence of (pure) Newton under regularity and proximity to optimum
- - Breakdown/indefiniteness issues: when Hessian is indefinite or singular and the Newton direction is not a descent direction
- - Damped/modified Newton strategies (e.g., step length/line search or trust-region to handle nonpositive-definite Hessian)
- - Trust-region subproblem: minimizing the quadratic model subject to ||p|| ≤ Δ and its role vs line-search
- - Levenberg–Marquardt damping: regularizing Hessian by adding λI (or similar) to ensure positive definiteness
- - Hessian-free/Newton–CG approaches: solving the Newton system approximately using iterative methods with Hessian-vector products
- - Quasi-Newton methods: building low-cost approximations to (inverse) Hessian from gradient differences rather than forming H directly
- - Secant equation (quasi-Newton condition): B\_{k+1} s\_k = y\_k (and its inverse form) as the constraint on updates
- - BFGS update as a specific quasi-Newton update that maintains symmetry and positive-definiteness (when curvature condition holds)
- - Inverse BFGS (formula for updating the approximate inverse Hessian directly) and its computational benefits
- - Curvature condition y\_k^T s\_k > 0 required for BFGS to preserve positive-definiteness and stable updates
- - Limited-memory BFGS (L-BFGS): storing a fixed small number m of vector pairs (s,y) instead of full matrices for large-scale problems
- - Two-loop recursion algorithm to apply the L-BFGS inverse-Hessian approximation to a vector efficiently without forming matrices
- - Storage/computational trade-offs: full Hessian storage and inversion vs BFGS O(n^2) vs L-BFGS O(n m) memory and time
- - Strong and weak Wolfe line-search conditions and their role in global convergence and in ensuring the curvature condition for BFGS
- - Superlinear convergence of (standard) quasi-Newton methods like BFGS under suitable assumptions
- - SR1 (symmetric rank-one) and other alternative quasi-Newton updates and their differing properties (e.g., not guaranteed SPD)
- - Gauss–Newton approximation for least-squares: approximating the Hessian by J^T J and when the approximation is valid
- - Relation between Hessian-vector products and efficient large-scale second-order methods (compute Hv without forming H)
- - Preconditioning for iterative solves of Newton systems (improving convergence of CG or other solvers)
- - Damping strategies for BFGS/L-BFGS (e.g., skip or modify updates when curvature condition fails) to maintain stability
- - Practical algorithm components: combining direction computation (Newton/BFGS/L-BFGS) with line-search or trust-region to ensure global convergence
- - Complexity/efficiency considerations: cost per iteration and memory bounds for Newton, BFGS, L-BFGS, and Hessian-free methods
- - Use of m (memory parameter) in L-BFGS and its effect on approximation quality vs memory use
- - Two-loop recursion intermediate scalars (alpha, beta, rho) as part of the L-BFGS application procedure
- - Stopping criteria specific to second-order methods (e.g., size of Newton decrement or small norm of projected gradient)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Gradient methods know which way is downhill. Second-order methods also know how the ground curves—so they can choose steps that are both directional and properly scaled.

TL;DR:

Second-order optimization uses curvature information (the Hessian H or an approximation to H⁻¹) to build a local quadratic model and compute a step that is often far more scale-aware than plain gradient descent. Newton’s method uses H directly (solve H **p** = −∇f). Quasi-Newton methods (BFGS, L-BFGS) avoid forming H by updating an inverse-Hessian approximation B using gradient differences, giving many of Newton’s benefits at much lower cost.

## What Is Second-Order Optimization?

### Why you should care (motivation before formulas)

First-order methods (gradient descent, momentum, Adam) use ∇f(**x**) to pick a direction of improvement. But they do not know how the objective bends. If the landscape is stretched—steep in one direction and flat in another—then a single global learning rate is a compromise: small enough not to explode in steep directions, but then painfully slow in flat directions.

Second-order methods solve this by using curvature: they estimate how f changes for a whole *step vector* **p**, not just for an infinitesimal move. This usually yields steps that are automatically scaled per-direction. In well-behaved problems, this can turn long, zig-zagging trajectories into short, decisive moves.

### The central idea: local quadratic modeling

Second-order methods are built on the second-order Taylor approximation around a point **x**:

f(**x** + **p**) ≈ f(**x**) + ∇f(**x**)ᵀ **p** + ½ **p**ᵀ H(**x**) **p**

- •∇f(**x**) is the gradient (a vector).
- •H(**x**) is the Hessian (a matrix of second derivatives).
- •The term ½ **p**ᵀ H **p** measures curvature along **p**.

This approximation says: “near **x**, the function looks like a quadratic bowl (or saddle).” If we trust that local quadratic, we can choose **p** by minimizing the quadratic model.

### Minimizing the quadratic model gives the Newton step

Define the quadratic model:

m(**p**) = f(**x**) + ∇f(**x**)ᵀ **p** + ½ **p**ᵀ H(**x**) **p**

To minimize m(**p**), differentiate with respect to **p** and set to zero:

∇ₚ m(**p**) = ∇f(**x**) + H(**x**) **p** = **0**

So the step solves:

H(**x**) **p** = −∇f(**x**)

If H is invertible:

**p** = −H(**x**)⁻¹ ∇f(**x**)

This is the Newton step. It is not “just a better direction”; it is a direction *and* a scale determined by curvature.

### When Newton is amazing (and when it isn’t)

Newton can converge extremely fast near a minimizer—often *quadratically*: the number of correct digits can roughly double each iteration in ideal settings. That’s why Newton-like methods are central in classical optimization.

But Newton also has costs and pitfalls:

- •Computing H explicitly costs O(n²) storage and often O(n³) to factor/solve.
- •If H is indefinite (saddle) or poorly conditioned, the Newton step may not be a descent direction.
- •The quadratic model is local; a full Newton step may overshoot unless you damp it (line search / trust region).

Quasi-Newton methods (BFGS, L-BFGS) keep the good idea—use curvature to scale steps—while avoiding explicit Hessians.

### Key symbols in this node

- •H: Hessian matrix, H = ∇²f(**x**)
- •B: inverse-Hessian approximation used by quasi-Newton methods, B ≈ H⁻¹

In practice, many algorithms compute the step as:

**p** = −B ∇f(**x**)

with B updated cheaply from gradient information.

## Core Mechanic 1: Newton’s Method via the Second-Order Taylor Model

### Why Newton’s method is the “natural” second-order step

If you accept the local quadratic approximation as your model, then the Newton step is simply the optimizer of that model. There’s no extra heuristic—Newton is what happens when you *take the quadratic seriously*.

### Derivation with breathing room

Start from the second-order expansion at **x**:

f(**x** + **p**) ≈ f(**x**) + ∇f(**x**)ᵀ **p** + ½ **p**ᵀ H(**x**) **p**

Let g = ∇f(**x**) and H = H(**x**) for short. Then:

m(**p**) = f(**x**) + gᵀ **p** + ½ **p**ᵀ H **p**

Take the gradient with respect to **p**:

∇ₚ m(**p**) = g + H **p**

Set to zero at optimum:

g + H **p** = **0**

Solve:

H **p** = −g

So the update is:

**x**ₖ₊₁ = **x**ₖ + **p**

### Newton as “whitened” gradient descent

Gradient descent uses **p** = −α g. Newton uses **p** = −H⁻¹ g.

You can interpret H⁻¹ as a *preconditioner*: it rescales the gradient by curvature. If the function is steep in one direction, H has large eigenvalues there, and H⁻¹ shrinks the step along that direction. If it is flat, H⁻¹ expands the step.

More explicitly, if H = Q Λ Qᵀ (eigendecomposition with orthonormal Q), then:

H⁻¹ = Q Λ⁻¹ Qᵀ

and

**p** = −Q Λ⁻¹ Qᵀ g

So each eigen-direction is scaled by 1/λᵢ.

### Descent conditions: when is the Newton step safe?

A direction **p** is a descent direction if gᵀ **p** < 0.

For Newton:

**p** = −H⁻¹ g

Compute gᵀ **p**:

gᵀ **p** = gᵀ (−H⁻¹ g) = −gᵀ H⁻¹ g

If H is symmetric positive definite (SPD), then H⁻¹ is SPD and gᵀ H⁻¹ g > 0 for any nonzero g. Therefore gᵀ **p** < 0: Newton is a descent direction.

If H is indefinite (has negative eigenvalues), then gᵀ H⁻¹ g can be negative, and the Newton step can ascend.

### Damping: line search with Newton directions

Even with SPD H, the quadratic model may not be accurate far from **x**. A standard fix is to take:

**x**ₖ₊₁ = **x**ₖ + αₖ **p**ₖ

where **p**ₖ solves Hₖ **p**ₖ = −gₖ, and αₖ is found via line search (e.g., Armijo/Wolfe conditions). This is often called *damped Newton*.

### Trust regions: constrain the step instead of shrinking it

Another fix is to *trust* the quadratic model only within a region ‖**p**‖ ≤ Δ:

minimize m(**p**) subject to ‖**p**‖ ≤ Δ

This changes the step when Newton would take something too large or unstable. Trust-region Newton methods are especially robust when H is indefinite.

### Computational reality: you rarely invert H

You never compute H⁻¹ explicitly. You solve the linear system:

H **p** = −g

using:

- •Cholesky (if H is SPD)
- •LDLᵀ (for symmetric indefinite)
- •Conjugate gradient (CG) if H is large and SPD (uses Hessian-vector products)

The solve is the “real cost” of Newton.

### Newton vs gradient descent (clarity table)

| Aspect | Gradient descent | Newton’s method |
| --- | --- | --- |
| Uses | ∇f | ∇f and H |
| Step | **p** = −α ∇f | Solve H **p** = −∇f |
| Sensitivity to scaling | High | Low (often scale-invariant under affine transforms) |
| Per-iteration cost | Low | High |
| Convergence near optimum | Linear (typical) | Quadratic (ideal conditions) |
| Failure modes | Slow in ill-conditioned valleys | Non-descent if H indefinite; expensive |

### Where Newton shines

- •Medium-dimensional smooth optimization (n up to a few thousands with structure)
- •Problems where high accuracy is needed
- •When Hessian is available or Hessian-vector products are cheap

In large-scale ML (millions of parameters), full Newton is typically too expensive—this is where quasi-Newton, L-BFGS, and approximations enter.

## Core Mechanic 2: Quasi-Newton Methods (BFGS and L-BFGS) as Low-Cost Curvature Learning

### Why quasi-Newton exists

Newton’s method asks for H and a linear solve. Quasi-Newton methods try to approximate the effect of H⁻¹ without ever forming H.

The guiding question is:

> Can we learn a good linear map B that turns gradients into near-Newton steps?

That is, we want:

**p** = −B g

with B ≈ H⁻¹.

### The secant condition (the core constraint)

Let **x**ₖ₊₁ = **x**ₖ + **s**ₖ where **s**ₖ = **x**ₖ₊₁ − **x**ₖ.

Let gₖ = ∇f(**x**ₖ) and gₖ₊₁ = ∇f(**x**ₖ₊₁). Define:

**y**ₖ = gₖ₊₁ − gₖ

For twice-differentiable f, for small steps:

**y**ₖ ≈ Hₖ **s**ₖ

A quasi-Newton method chooses an approximation (either to H or to H⁻¹) that satisfies the *secant equation*:

H̃ₖ₊₁ **s**ₖ = **y**ₖ

or in inverse form:

Bₖ₊₁ **y**ₖ = **s**ₖ

This is the multi-dimensional analogue of matching slopes in 1D.

### BFGS: updating the inverse-Hessian approximation

BFGS maintains Bₖ ≈ Hₖ⁻¹ and updates it using **s** and **y**.

Define ρ = 1 / (**y**ᵀ **s**).

Assuming **y**ᵀ **s** > 0 (curvature condition), the BFGS inverse update is:

Bₖ₊₁ = (I − ρ **s** **y**ᵀ) Bₖ (I − ρ **y** **s**ᵀ) + ρ **s** **s**ᵀ

Key properties:

- •If Bₖ is symmetric positive definite and **y**ᵀ **s** > 0, then Bₖ₊₁ stays SPD.
- •It satisfies the secant condition Bₖ₊₁ **y** = **s**.
- •Among all symmetric updates satisfying the secant condition, BFGS can be derived as a minimal change update under a particular matrix norm (a “closest” update).

### Intuition: what BFGS is really doing

B is a learned preconditioner.

- •**s** tells you what step you actually took.
- •**y** tells you how the gradient changed.
- •If the gradient changes a lot for a small step in some direction, curvature is high there, so H is large and H⁻¹ (hence B) should be small in that direction.

BFGS accumulates this information over iterations, gradually sculpting B to match the inverse curvature.

### Why the curvature condition matters (and how it is enforced)

The condition **y**ᵀ **s** > 0 ensures positive curvature along **s**. With line searches satisfying the (strong) Wolfe conditions, one can guarantee **y**ᵀ **s** > 0 for smooth functions.

If **y**ᵀ **s** ≤ 0, BFGS may lose SPD and produce non-descent steps. Practical implementations may:

- •Skip the update
- •Use damping (Powell damping)
- •Modify **y** to enforce **y**ᵀ **s** > 0

### Cost of full BFGS

B is n×n. Storing and updating it costs O(n²) memory and O(n²) time per iteration—often too expensive for large n.

### L-BFGS: limited-memory BFGS

L-BFGS avoids storing B. Instead, it stores only the last m pairs {(**s**ᵢ, **y**ᵢ)} for i = k−m+1,…,k.

To compute **p** = −Bₖ gₖ, L-BFGS uses the *two-loop recursion*, which applies the implicit Bₖ to a vector in O(mn) time and O(mn) memory.

#### Two-loop recursion (conceptual form)

Given current gradient g, set **q** = g.

Loop backwards over stored pairs:

- •αᵢ = ρᵢ **s**ᵢᵀ **q**
- •**q** ← **q** − αᵢ **y**ᵢ

Apply an initial scaling H₀ (often γ I) to get **r**:

- •**r** ← H₀ **q**

Loop forwards:

- •β = ρᵢ **y**ᵢᵀ **r**
- •**r** ← **r** + **s**ᵢ (αᵢ − β)

Then the search direction is:

**p** = −**r**

Even though no n×n matrix is stored, the resulting **p** behaves like a quasi-Newton direction.

### Choosing the initial scaling H₀

A common choice is:

γₖ = (**s**ₖ₋₁ᵀ **y**ₖ₋₁) / (**y**ₖ₋₁ᵀ **y**ₖ₋₁)

and H₀ = γₖ I.

This roughly matches average curvature magnitude.

### Comparing Newton / BFGS / L-BFGS

| Method | Uses H explicitly? | Stores n×n matrix? | Typical per-iter cost | Strengths | Weaknesses |
| --- | --- | --- | --- | --- | --- |
| Newton | Yes | Often yes (or factorization) | High (solve) | Fast local convergence, accurate steps | Expensive; needs robust globalization |
| BFGS | No | Yes (B) | O(n²) | Very effective for smooth medium-scale problems | Memory/time blow up for large n |
| L-BFGS | No | No (stores m pairs) | O(mn) | Scales to large n; strong practical default | Needs line search; can be sensitive/noisy gradients |

### Practical note for ML

Quasi-Newton methods typically assume deterministic or low-noise gradients. In deep learning with mini-batch noise, L-BFGS can still be used but often requires care (larger batches, stronger line search heuristics, or stochastic quasi-Newton variants).

The conceptual win remains: approximate H⁻¹ well enough to get curvature-aware steps without paying Newton’s full price.

## Application & Connection: Globalization (Line Search / Trust Region), Indefinite Hessians, and Large-Scale Practice

### Why “globalization” is necessary

Second-order methods are fundamentally *local*: they rely on the Taylor approximation being accurate near the current iterate. Far from the solution, that approximation can be wrong in two ways:

1. 1)The quadratic model predicts improvement where the true function increases.
2. 2)The Hessian may be indefinite, reflecting saddles or nonconvex curvature.

Globalization strategies are the standard tools that make Newton-like methods robust in practice.

### Line search with (quasi-)Newton directions

Given a direction **p** (Newton, BFGS, L-BFGS), pick α to ensure sufficient decrease:

**x**ₖ₊₁ = **x**ₖ + α **p**

A common sufficient decrease condition (Armijo) is:

f(**x** + α **p**) ≤ f(**x**) + c₁ α ∇f(**x**)ᵀ **p**

with 0 < c₁ < 1.

To also ensure curvature information behaves well (especially for BFGS), enforce Wolfe (or strong Wolfe) conditions, which include:

∇f(**x** + α **p**)ᵀ **p** ≥ c₂ ∇f(**x**)ᵀ **p**

with c₁ < c₂ < 1.

These conditions help guarantee **y**ᵀ **s** > 0, preserving SPD updates in BFGS/L-BFGS.

### Trust region viewpoint (often more robust for Newton)

Instead of searching along a line, trust region methods solve:

minimize gᵀ **p** + ½ **p**ᵀ H **p**

subject to ‖**p**‖ ≤ Δ

If the Newton step lies inside the region, take it. If not, take a boundary step that balances descent and stability.

In nonconvex problems, trust regions naturally handle indefinite H by restricting step size and allowing directions of negative curvature to be exploited safely.

### Indefinite Hessians and modified Newton steps

When H is not SPD, you may:

- •Add damping: H̃ = H + λ I with λ > 0 (Levenberg–Marquardt / damped Newton)
- •Use a trust region (implicitly similar effect)
- •Use a factorization that detects negative curvature and adjusts the step

Damping connects to the idea that you want a model that is convex enough locally to provide a descent direction.

### Large-scale settings: Hessian-vector products and Newton-CG

Even if you cannot store H, you may be able to compute H **v** efficiently (automatic differentiation can do this). Then you can approximately solve:

H **p** = −g

using conjugate gradient (CG), which needs only matrix-vector products.

This yields *Newton-CG* (also called truncated Newton). It can be seen as a spectrum:

- •More CG iterations → closer to true Newton
- •Fewer CG iterations → cheaper, more like a preconditioned gradient method

### When to use what (rule-of-thumb table)

| Scenario | Recommended tool | Why |
| --- | --- | --- |
| Small n, high accuracy, smooth convex | Newton + line search / trust region | Fast convergence, stable |
| Medium n (10³–10⁵), smooth deterministic | L-BFGS | Excellent cost/benefit |
| Large n, can do H **v**, need high precision | Newton-CG / trust region Newton-CG | Uses curvature without storing H |
| Noisy mini-batch gradients | First-order (Adam/SGD) or specialized stochastic quasi-Newton | Classical line searches can struggle |

### Conceptual connection: second-order methods as “learning geometry”

A deep way to view these methods is that they choose steps using a local metric:

- •Gradient descent uses Euclidean geometry: step proportional to g
- •Newton uses curvature geometry: step proportional to H⁻¹ g
- •BFGS/L-BFGS learn an approximation to that geometry from observed gradients

That perspective connects second-order optimization to:

- •Preconditioning
- •Natural gradient ideas (using Fisher information as curvature)
- •Optimization on manifolds

You now have the two atomic concepts for this node:

1) second-order quadratic modeling (Taylor) ⇒ Newton step via solving H **p** = −g

2) quasi-Newton approximation B ≈ H⁻¹ learned via secant information (**s**, **y**) ⇒ BFGS/L-BFGS

From here, you can build toward robust implementations (line search, trust region) and scalable solvers (CG, Hessian-vector products).

## Worked Examples (3)

### Newton step on a quadratic: one iteration to the minimizer

Minimize f(**x**) = ½ **x**ᵀ A **x** − **b**ᵀ **x**, where A is SPD.

Let A = [[4, 0],[0, 1]] and **b** = [8, 2]ᵀ. Start at **x**₀ = [0, 0]ᵀ.

Compute one Newton step.

1. Compute gradient and Hessian:

   ∇f(**x**) = A **x** − **b**

   H = ∇²f(**x**) = A
2. At **x**₀ = **0**:

   g₀ = ∇f(**x**₀) = A **0** − **b** = −**b** = [−8, −2]ᵀ
3. Newton step solves:

   H **p** = −g₀

   A **p** = −(−**b**) = **b**
4. Solve A **p** = **b**:

   [[4,0],[0,1]] [p₁,p₂]ᵀ = [8,2]ᵀ

   So:

   4 p₁ = 8 ⇒ p₁ = 2

   1 p₂ = 2 ⇒ p₂ = 2

   Therefore **p** = [2,2]ᵀ
5. Update:

   **x**₁ = **x**₀ + **p** = [0,0]ᵀ + [2,2]ᵀ = [2,2]ᵀ
6. Verify optimality (for a quadratic with SPD A, optimum is A **x**⋆ = **b**):

   A **x**₁ = [[4,0],[0,1]] [2,2]ᵀ = [8,2]ᵀ = **b**

   So **x**₁ = **x**⋆

**Insight:** For strictly convex quadratics, Newton’s method reaches the minimizer in one step from any start because the second-order Taylor model is exact (the function really is quadratic).

### Newton on a non-quadratic 1D function: see the Taylor model drive the update

Minimize f(x) = x⁴. Start at x₀ = 1. Compute two Newton iterations.

(Here ∇f = f′ and H = f″.)

1. Compute derivatives:

   f′(x) = 4x³

   f″(x) = 12x²
2. Newton update in 1D:

   xₖ₊₁ = xₖ − f′(xₖ)/f″(xₖ)
3. At x₀ = 1:

   f′(1) = 4

   f″(1) = 12

   So:

   x₁ = 1 − 4/12 = 1 − 1/3 = 2/3
4. At x₁ = 2/3:

   f′(2/3) = 4 (2/3)³ = 4 (8/27) = 32/27

   f″(2/3) = 12 (2/3)² = 12 (4/9) = 16/3
5. Compute step:

   x₂ = x₁ − (32/27)/(16/3)

   = 2/3 − (32/27)·(3/16)

   = 2/3 − (96)/(432)

   = 2/3 − 2/9

   = 4/9

**Insight:** Newton automatically reduces step sizes near flat curvature: as x → 0, f″(x) → 0 too, so the ratio f′/f″ behaves like (4x³)/(12x²) = x/3, giving xₖ₊₁ = (2/3) xₖ. Here convergence is linear because the minimizer is not strongly convex (H at 0 is 0).

### One BFGS inverse update from observed step and gradient change

Suppose at iteration k you have Bₖ = I (2×2 identity).

You took **s** = [1, 0]ᵀ and observed gradient change **y** = [2, 0]ᵀ.

Compute Bₖ₊₁ using the BFGS inverse update.

1. Compute ρ:

   ρ = 1/(**y**ᵀ **s**) = 1/([2,0]·[1,0]) = 1/2
2. Write the update:

   Bₖ₊₁ = (I − ρ **s** **y**ᵀ) Bₖ (I − ρ **y** **s**ᵀ) + ρ **s** **s**ᵀ
3. Compute matrices:

   **s** **y**ᵀ = [[1],[0]] [2,0] = [[2,0],[0,0]]

   So:

   I − ρ **s** **y**ᵀ = I − (1/2) [[2,0],[0,0]] = [[0,0],[0,1]]
4. **y** **s**ᵀ = [[2],[0]] [1,0] = [[2,0],[0,0]]

   So:

   I − ρ **y** **s**ᵀ = [[0,0],[0,1]] as well
5. Since Bₖ = I:

   (I − ρ **s** **y**ᵀ) Bₖ (I − ρ **y** **s**ᵀ)

   = [[0,0],[0,1]] I [[0,0],[0,1]]

   = [[0,0],[0,1]]
6. Compute final term:

   ρ **s** **s**ᵀ = (1/2) [[1],[0]] [1,0] = (1/2) [[1,0],[0,0]] = [[1/2,0],[0,0]]
7. Add them:

   Bₖ₊₁ = [[0,0],[0,1]] + [[1/2,0],[0,0]] = [[1/2,0],[0,1]]

**Insight:** This update learned that curvature along the first coordinate is about 2 (since **y** ≈ H **s**), so the inverse curvature along that direction should be about 1/2. The second coordinate was untouched, so it stayed at 1.

## Key Takeaways

- ✓

  Second-order methods build a local quadratic model: f(**x** + **p**) ≈ f(**x**) + gᵀ **p** + ½ **p**ᵀ H **p**.
- ✓

  Newton’s step is the minimizer of that quadratic model: solve H **p** = −g (don’t compute H⁻¹ explicitly).
- ✓

  If H is SPD, the Newton direction is a descent direction since gᵀ **p** = −gᵀ H⁻¹ g < 0.
- ✓

  Because the Taylor model is local, practical Newton methods use globalization: line search (Armijo/Wolfe) or trust regions.
- ✓

  Quasi-Newton methods replace H⁻¹ with a learned approximation B updated from (**s**, **y**) where **s** = Δ**x** and **y** = Δg.
- ✓

  BFGS updates B with a rank-two formula that preserves symmetry and (with **y**ᵀ **s** > 0) positive definiteness.
- ✓

  L-BFGS scales to large n by storing only the last m curvature pairs and computing **p** = −B g via the two-loop recursion.

## Common Mistakes

- ✗

  Inverting the Hessian explicitly (computing H⁻¹) instead of solving H **p** = −g with a linear solver.
- ✗

  Using Newton/BFGS steps without globalization (no line search / trust region), leading to overshooting or divergence.
- ✗

  Ignoring indefiniteness: treating a nonconvex Hessian as if it were SPD, which can produce ascent directions.
- ✗

  For BFGS/L-BFGS, failing to enforce **y**ᵀ **s** > 0 (e.g., by skipping Wolfe line search), which can break SPD guarantees and destabilize updates.

## Practice

easy

For f(**x**) = ½ **x**ᵀ A **x** with A = [[10,0],[0,1]], compare the gradient descent direction −g and the Newton direction −H⁻¹ g at a general point **x**. What is the qualitative difference in how they scale the two coordinates?

**Hint:** Compute g = A **x** and H = A. Then −H⁻¹ g simplifies a lot.

Show solution

We have g = ∇f(**x**) = A **x** and H = A.

Gradient descent direction (ignoring step size α):

−g = −A **x** = [−10 x₁, −1 x₂]ᵀ

So it is 10× larger in magnitude along coordinate 1.

Newton direction:

−H⁻¹ g = −A⁻¹ (A **x**) = −**x** = [−x₁, −x₂]ᵀ

So Newton cancels the anisotropic scaling of A and treats both coordinates equally (invariant to that scaling).

medium

Show that if H is SPD, then the Newton direction **p** solves gᵀ **p** < 0 whenever g ≠ **0**.

**Hint:** Use **p** = −H⁻¹ g and the fact that vᵀ M v > 0 for SPD M and v ≠ **0**.

Show solution

If H is SPD, then H⁻¹ is also SPD.

Newton direction: **p** = −H⁻¹ g.

Then:

gᵀ **p** = gᵀ (−H⁻¹ g) = −gᵀ H⁻¹ g.

Since H⁻¹ is SPD and g ≠ **0**, we have gᵀ H⁻¹ g > 0.

Therefore gᵀ **p** < 0, so **p** is a descent direction.

hard

Given Bₖ = I, **s** = [1,1]ᵀ, **y** = [3,1]ᵀ, compute ρ = 1/(**y**ᵀ **s**) and verify the secant condition Bₖ₊₁ **y** = **s** for the BFGS inverse update (you may compute Bₖ₊₁ explicitly or reason using known properties).

**Hint:** First compute **y**ᵀ **s**. Then either plug into the BFGS formula or use the theorem that the BFGS inverse update satisfies the secant equation by construction (provided **y**ᵀ **s** ≠ 0).

Show solution

Compute **y**ᵀ **s** = [3,1]·[1,1] = 4, so ρ = 1/4.

For BFGS inverse update:

Bₖ₊₁ = (I − ρ **s** **y**ᵀ) Bₖ (I − ρ **y** **s**ᵀ) + ρ **s** **s**ᵀ.

With Bₖ = I, the update is well-defined since **y**ᵀ **s** = 4 ≠ 0.

A defining property of the BFGS inverse update is that it satisfies the secant condition:

Bₖ₊₁ **y** = **s**.

Therefore, for this (**s**, **y**) pair, Bₖ₊₁ **y** must equal [1,1]ᵀ.

(If you compute Bₖ₊₁ explicitly, you will indeed find a symmetric matrix that maps **y** to **s**, confirming the condition.)

## Connections

Next nodes you can study:

- •[Line Search & Wolfe Conditions](/tech-tree/line-search-wolfe/)
- •[Trust Region Methods](/tech-tree/trust-region-methods/)
- •[Conjugate Gradient & Krylov Solvers](/tech-tree/conjugate-gradient/)
- •[Preconditioning & Conditioning](/tech-tree/preconditioning/)
- •[Natural Gradient & Information Geometry](/tech-tree/natural-gradient/)
- •[Hessian-Vector Products (Automatic Differentiation)](/tech-tree/hvp-autodiff/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
