---
title: Conjugate Gradient Methods
description: Efficient optimization for quadratic functions. Preconditioning.
date: '2026-07-01'
scheduled: '2027-02-02'
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
inspiration_url: https://templeton.host/tech-tree/conjugate-gradients/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/conjugate-gradients/](https://templeton.host/tech-tree/conjugate-gradients/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Conjugate Gradient Methods

OptimizationDifficulty: ★★★★★Depth: 8Unlocks: 0

Efficient optimization for quadratic functions. Preconditioning.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Quadratic objective <-> linear system for SPD A (gradient = A x - b)
- -A-conjugacy: directions mutually A-orthogonal (p\_i^T A p\_j = 0) enabling independent 1-D minimizations and finite-step exactness
- -Preconditioning: SPD transform/approximation M that changes the inner product/conditioning to accelerate CG convergence

## Key Symbols & Notation

A (symmetric positive-definite matrix defining the quadratic and linear system)

## Essential Relationships

- -Conjugate Gradient performs iterative minimization of the quadratic over expanding Krylov subspaces using short (three-term) recurrences to produce A-conjugate search directions and orthogonal residuals

## Prerequisites (2)

[Gradient Descent6 atoms](/tech-tree/gradient-descent/)[Systems of Linear Equations6 atoms](/tech-tree/linear-systems/)

Advanced Learning Details

### Graph Position

83

Depth Cost

0

Fan-Out (ROI)

0

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

### All Concepts (18)

- - Quadratic objective function form: f(x) = 1/2 x^T A x - b^T x + c (special structure exploited by CG)
- - Symmetric positive-definite (SPD) matrix requirement for CG
- - Energy (A-)norm: ||v||\_A = sqrt(v^T A v)
- - A-inner-product: <u,v>\_A = u^T A v
- - Conjugacy (A-orthogonality) of search directions: concept that directions can be mutually A-orthogonal
- - Residual specific to linear system/quadratic: r\_k = b - A x\_k (equals negative gradient for quadratic f)
- - Krylov subspace: K\_k(A,r0) = span{r0, A r0, A^2 r0, ...}
- - Finite termination property: exact solution obtained in at most n steps in exact arithmetic
- - Optimality property of CG: at step k, x\_k minimizes f over x0 + K\_k(A,r0)
- - Three-term recurrence structure for updating iterates, residuals, and directions
- - Closed-form step length (line search) for quadratics (alpha\_k chosen exactly to minimize along a search direction)
- - Specific update (beta) that constructs new conjugate direction from residual and previous direction
- - Preconditioning: replacing A with a transformed system via a preconditioner M≈A to improve convergence
- - Left/right/symmetric preconditioning variants (transformations of original system to apply CG)
- - Condition number κ(A) as a key predictor of CG convergence behavior
- - Polynomial approximation viewpoint: CG finds the best degree-k polynomial in A that reduces error
- - Orthogonality relations among residuals (mutual residual orthogonality in exact arithmetic)
- - Sensitivity to finite-precision arithmetic (loss of orthogonality and practical remedies)

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Conjugate Gradient (CG) is what you use when “gradient descent feels right” but you can’t afford to be slow: it keeps the simplicity of iterative descent, but exploits the structure of symmetric positive-definite (SPD) quadratics to converge in dramatically fewer steps—often without ever forming a matrix inverse, and sometimes without even storing the matrix explicitly.

TL;DR:

For the SPD linear system A x = b (equivalently minimizing f(x)=½xᵀAx−bᵀx), CG builds a sequence of search directions that are mutually A-orthogonal (A-conjugate). Each step does an exact 1-D line minimization, and in exact arithmetic it reaches the exact solution in at most n steps. In practice, convergence depends on the condition number κ(A); preconditioning replaces the geometry with an easier one (via an SPD M≈A) to accelerate convergence.

## What Is Conjugate Gradient Methods?

### The problem CG is built for

CG is not a general-purpose optimizer. It is **specialized** for a very important class of problems:

1) **Solve a linear system**

A x=bA\,\mathbf{x} = \mathbf{b}Ax=b

2) where **A is symmetric positive-definite (SPD)**:

- •Symmetric: A=A⊤A = A^\topA=A⊤
- •Positive-definite: z⊤Az>0\mathbf{z}^\top A\mathbf{z} > 0z⊤Az>0 for all nonzero **z**

This single assumption (SPD) is what makes CG fast, stable, and geometric.

### Quadratic optimization ↔ linear systems

The key equivalence is that solving Ax=bA\mathbf{x}=\mathbf{b}Ax=b is the same as minimizing a strictly convex quadratic:

f(x)=12x⊤Ax−b⊤xf(\mathbf{x}) = \tfrac{1}{2}\mathbf{x}^\top A\mathbf{x} - \mathbf{b}^\top \mathbf{x}f(x)=21​x⊤Ax−b⊤x

Compute the gradient (showing the work):

∇f(x)=∇(12x⊤Ax)−∇(b⊤x)\nabla f(\mathbf{x}) = \nabla\left(\tfrac{1}{2}\mathbf{x}^\top A\mathbf{x}\right) - \nabla\left(\mathbf{b}^\top\mathbf{x}\right)∇f(x)=∇(21​x⊤Ax)−∇(b⊤x)

For symmetric AAA,

∇(12x⊤Ax)=Ax\nabla\left(\tfrac{1}{2}\mathbf{x}^\top A\mathbf{x}\right) = A\mathbf{x}∇(21​x⊤Ax)=Ax

and

∇(b⊤x)=b\nabla\left(\mathbf{b}^\top\mathbf{x}\right) = \mathbf{b}∇(b⊤x)=b

So

∇f(x)=Ax−b\nabla f(\mathbf{x}) = A\mathbf{x} - \mathbf{b}∇f(x)=Ax−b

Setting ∇f(x∗)=0\nabla f(\mathbf{x}^\*)=\mathbf{0}∇f(x∗)=0 gives Ax∗=bA\mathbf{x}^\* = \mathbf{b}Ax∗=b. So the minimizer and the linear-system solution coincide.

### Why gradient descent isn’t enough

If you already know gradient descent, you might propose:

xk+1=xk−αk∇f(xk)=xk−αk(Axk−b)\mathbf{x}\_{k+1} = \mathbf{x}\_k - \alpha\_k\nabla f(\mathbf{x}\_k) = \mathbf{x}\_k - \alpha\_k(A\mathbf{x}\_k - \mathbf{b})xk+1​=xk​−αk​∇f(xk​)=xk​−αk​(Axk​−b)

That works, but on ill-conditioned problems it “zig-zags” along narrow valleys (elliptical level sets). Convergence becomes painfully slow because the best step size is constrained by the largest eigenvalue while progress is governed by the smallest.

CG fixes this by changing the question from “which way is steepest right now?” to:

> “Which direction lets me make progress without undoing what I already fixed?”

### Two geometric lenses (keep both in mind)

CG is easiest to understand using two complementary pictures:

1) **Residual view (linear algebra):**

- •Define the residual **r**ₖ as

rk=b−Axk\mathbf{r}\_k = \mathbf{b} - A\mathbf{x}\_krk​=b−Axk​

- •Note that rk=−∇f(xk)\mathbf{r}\_k = -\nabla f(\mathbf{x}\_k)rk​=−∇f(xk​).

2) **Energy/inner-product view (geometry):**

- •SPD AAA defines an inner product

⟨u,v⟩A=u⊤Av\langle \mathbf{u},\mathbf{v}\rangle\_A = \mathbf{u}^\top A\mathbf{v}⟨u,v⟩A​=u⊤Av

- •And an induced norm ∥u∥A=u⊤Au\|\mathbf{u}\|\_A = \sqrt{\mathbf{u}^\top A\mathbf{u}}∥u∥A​=u⊤Au​.

CG chooses directions that are orthogonal under this AAA-inner-product (called **A-conjugate**), which is the right notion of “independent directions” for this quadratic.

### Anchor visualization (static SVG)

**Suggested SVG anchor for this node:** `/images/cg-geometry.svg`

**What it should depict (single figure with labeled layers):**

- •2D ellipsoidal level sets of f(x)f(\mathbf{x})f(x)
- •iterates **x**₀, **x**₁, **x**₂…
- •residual vectors **r**₀, **r**₁ at those points (steepest descent directions)
- •search directions **p**₀, **p**₁, **p**₂ (CG directions)
- •annotations showing:
- •**r**ᵢ ⟂ **r**ⱼ (Euclidean orthogonality of residuals)
- •**p**ᵢ ⟂ₐ **p**ⱼ (A-orthogonality / conjugacy)

Even if learners skip interactivity, this one image should connect “ellipses” ↔ “residuals” ↔ “conjugate directions.”

## Core Mechanic 1: A‑Conjugacy, Krylov Subspaces, and Why CG Makes Finite Progress

### The key idea: don’t reuse the same curvature direction

For the quadratic f(x)=12x⊤Ax−b⊤xf(\mathbf{x})=\tfrac12\mathbf{x}^\top A\mathbf{x}-\mathbf{b}^\top\mathbf{x}f(x)=21​x⊤Ax−b⊤x, curvature is encoded by AAA. If you move along direction **p**, the second derivative along that line is p⊤Ap\mathbf{p}^\top A\mathbf{p}p⊤Ap. So if two directions are “independent with respect to curvature,” they should satisfy:

pi⊤Apj=0(i≠j)\mathbf{p}\_i^\top A\mathbf{p}\_j = 0\quad (i\neq j)pi⊤​Apj​=0(i=j)

This is **A-conjugacy** (also called **A-orthogonality**).

Why it matters: if you minimize the quadratic along **p**₀ and then later move along some other direction **p**₁ that is A-conjugate to **p**₀, you do **not** spoil the minimization you already achieved along **p**₀ in the quadratic’s geometry.

### CG as “Gram–Schmidt, but with A in the middle”

In Euclidean space, we make directions orthogonal using dot products u⊤v\mathbf{u}^\top\mathbf{v}u⊤v. For CG, the orthogonality condition is instead u⊤Av\mathbf{u}^\top A\mathbf{v}u⊤Av.

Conceptually, CG is building an A-orthogonal basis of directions

{p0,p1,… }\{\mathbf{p}\_0,\mathbf{p}\_1,\dots\}{p0​,p1​,…}

and doing an exact line minimization along each.

### The Krylov subspace view (the “growth” story)

A second major structural fact is that CG iterates live in expanding **Krylov subspaces**.

Let the initial residual be **r**₀ = **b** − A**x**₀.

Define the Krylov subspace of order k:

Kk(A,r0)=span{r0, Ar0, A2r0, …, Ak−1r0}\mathcal{K}\_k(A,\mathbf{r}\_0) = \text{span}\{\mathbf{r}\_0,\,A\mathbf{r}\_0,\,A^2\mathbf{r}\_0,\,\dots,\,A^{k-1}\mathbf{r}\_0\}Kk​(A,r0​)=span{r0​,Ar0​,A2r0​,…,Ak−1r0​}

CG chooses **x**ₖ from the affine space

xk∈x0+Kk(A,r0).\mathbf{x}\_k \in \mathbf{x}\_0 + \mathcal{K}\_k(A,\mathbf{r}\_0).xk​∈x0​+Kk​(A,r0​).

This matters because:

- •Each iteration adds **one new dimension** of freedom.
- •CG chooses the best point in that expanding space under the quadratic objective.

This is the conceptual reason for the celebrated finite-step property:

> In exact arithmetic, CG finds the exact solution in at most n iterations (n = dimension), because after n steps the Krylov subspace can span the whole space.

In practice, roundoff and “near dependence” mean you often stop earlier based on tolerance.

### Residual orthogonality (a different orthogonality)

A surprising and useful property (for exact arithmetic) is:

ri⊤rj=0(i≠j)\mathbf{r}\_i^\top\mathbf{r}\_j = 0\quad (i\neq j)ri⊤​rj​=0(i=j)

Residuals are mutually orthogonal in the standard dot product, even though search directions are A-orthogonal.

This is one of the best places to use visualization.

### Interactive visualization plan (explicitly targets the weak spot)

**Interactive canvas suggestion (two linked panels):**

**Panel A: Level sets + directions (geometry)**

- •Show ellipsoidal contours of fff in 2D.
- •Display **x**ₖ, **r**ₖ, and **p**ₖ.
- •Toggle overlays:

1) “Residual orthogonality”: draw **r**₀, **r**₁, **r**₂ from a common origin and show right-angle markers for **r**ᵢ ⟂ **r**ⱼ.

2) “A-conjugacy”: draw **p**ᵢ and show right-angle markers in the **A-metric** (see below).

**Panel B: Krylov subspace growth (algebra)**

- •Show basis vectors being added:
- •start with span{**r**₀}
- •then span{**r**₀, A**r**₀}
- •then add A²**r**₀, etc.
- •In 2D, show the subspace as a line that rotates/expands into the plane.
- •Show that **x**ₖ is the minimizer restricted to that subspace (a projection onto the solution in the A-norm).

**How to visualize A-orthogonality concretely:**

A-orthogonality is Euclidean orthogonality after a change of variables. Since A is SPD, write A=C⊤CA = C^\top CA=C⊤C (e.g., Cholesky). Then

pi⊤Apj=(Cpi)⊤(Cpj).\mathbf{p}\_i^\top A\mathbf{p}\_j = (C\mathbf{p}\_i)^\top(C\mathbf{p}\_j).pi⊤​Apj​=(Cpi​)⊤(Cpj​).

So **p**ᵢ ⟂ₐ **p**ⱼ means transformed vectors C**p**ᵢ are orthogonal in Euclidean space. The canvas can show both **p** and C**p**.

### A small but important mental model

CG is not “steepest descent with a fancy step size.” It is closer to:

- •Build a low-dimensional model space where the solution lives (Krylov)
- •Find the best point in that space (exact minimization)
- •Expand the space by one dimension with a direction that is independent under A

That combination produces fast progress on SPD problems.

## Core Mechanic 2: The CG Recurrence (α, β), Residual Updates, and What Each Quantity Means

### Start from the simplest objects

We track three sequences:

- •iterate **x**ₖ (current solution estimate)
- •residual **r**ₖ = **b** − A**x**ₖ (negative gradient)
- •search direction **p**ₖ (A-conjugate directions)

Initialize:

x0 given\mathbf{x}\_0\ \text{given}x0​ given

r0=b−Ax0\mathbf{r}\_0 = \mathbf{b} - A\mathbf{x}\_0r0​=b−Ax0​

p0=r0\mathbf{p}\_0 = \mathbf{r}\_0p0​=r0​

The first direction equals steepest descent. After that, directions become “corrected” to maintain conjugacy.

### Step 1: exact line search to get αₖ

We move along **p**ₖ:

xk+1=xk+αkpk\mathbf{x}\_{k+1} = \mathbf{x}\_k + \alpha\_k\mathbf{p}\_kxk+1​=xk​+αk​pk​

Choose αk\alpha\_kαk​ to minimize f(xk+αpk)f(\mathbf{x}\_k + \alpha\mathbf{p}\_k)f(xk​+αpk​).

Compute it explicitly. Let ϕ(α)=f(xk+αpk)\phi(\alpha)=f(\mathbf{x}\_k+\alpha\mathbf{p}\_k)ϕ(α)=f(xk​+αpk​).

Start expanding:

ϕ(α)=12(xk+αpk)⊤A(xk+αpk)−b⊤(xk+αpk)\phi(\alpha)=\tfrac12(\mathbf{x}\_k+\alpha\mathbf{p}\_k)^\top A(\mathbf{x}\_k+\alpha\mathbf{p}\_k) - \mathbf{b}^\top(\mathbf{x}\_k+\alpha\mathbf{p}\_k)ϕ(α)=21​(xk​+αpk​)⊤A(xk​+αpk​)−b⊤(xk​+αpk​)

Differentiate w.r.t. α:

ϕ′(α)=pk⊤A(xk+αpk)−b⊤pk\phi'(\alpha) = \mathbf{p}\_k^\top A(\mathbf{x}\_k+\alpha\mathbf{p}\_k) - \mathbf{b}^\top\mathbf{p}\_kϕ′(α)=pk⊤​A(xk​+αpk​)−b⊤pk​

Group terms:

ϕ′(α)=pk⊤(Axk−b)+α pk⊤Apk\phi'(\alpha)= \mathbf{p}\_k^\top(A\mathbf{x}\_k-\mathbf{b}) + \alpha\,\mathbf{p}\_k^\top A\mathbf{p}\_kϕ′(α)=pk⊤​(Axk​−b)+αpk⊤​Apk​

Recall Axk−b=−rkA\mathbf{x}\_k-\mathbf{b}=-\mathbf{r}\_kAxk​−b=−rk​:

ϕ′(α)=−pk⊤rk+α pk⊤Apk\phi'(\alpha)= -\mathbf{p}\_k^\top\mathbf{r}\_k + \alpha\,\mathbf{p}\_k^\top A\mathbf{p}\_kϕ′(α)=−pk⊤​rk​+αpk⊤​Apk​

Set ϕ′(α)=0\phi'(\alpha)=0ϕ′(α)=0:

αk=pk⊤rkpk⊤Apk\alpha\_k = \frac{\mathbf{p}\_k^\top\mathbf{r}\_k}{\mathbf{p}\_k^\top A\mathbf{p}\_k}αk​=pk⊤​Apk​pk⊤​rk​​

In standard CG (with **p**ₖ built from **r**ₖ), one can show pk⊤rk=rk⊤rk\mathbf{p}\_k^\top\mathbf{r}\_k = \mathbf{r}\_k^\top\mathbf{r}\_kpk⊤​rk​=rk⊤​rk​, giving the commonly used formula:

αk=rk⊤rkpk⊤Apk\alpha\_k = \frac{\mathbf{r}\_k^\top\mathbf{r}\_k}{\mathbf{p}\_k^\top A\mathbf{p}\_k}αk​=pk⊤​Apk​rk⊤​rk​​

### Step 2: update residual cheaply

Rather than recompute **r**ₖ₊₁ = **b** − A**x**ₖ₊₁ from scratch, use:

rk+1=b−A(xk+αkpk)=(b−Axk)−αkApk\mathbf{r}\_{k+1} = \mathbf{b} - A(\mathbf{x}\_k+\alpha\_k\mathbf{p}\_k) = (\mathbf{b}-A\mathbf{x}\_k) - \alpha\_k A\mathbf{p}\_krk+1​=b−A(xk​+αk​pk​)=(b−Axk​)−αk​Apk​

So

rk+1=rk−αkApk\mathbf{r}\_{k+1} = \mathbf{r}\_k - \alpha\_k A\mathbf{p}\_krk+1​=rk​−αk​Apk​

This highlights the computational core: each iteration needs one matrix-vector product ApkA\mathbf{p}\_kApk​.

### Step 3: build the next search direction via βₖ

We want **p**ₖ₊₁ to be in the span of the new residual plus the previous direction, but also maintain A-conjugacy:

pk+1=rk+1+βkpk\mathbf{p}\_{k+1} = \mathbf{r}\_{k+1} + \beta\_k\mathbf{p}\_kpk+1​=rk+1​+βk​pk​

Choose βk\beta\_kβk​ so that

pk+1⊤Apk=0\mathbf{p}\_{k+1}^\top A\mathbf{p}\_k = 0pk+1⊤​Apk​=0

Compute:

(rk+1+βkpk)⊤Apk=0(\mathbf{r}\_{k+1} + \beta\_k\mathbf{p}\_k)^\top A\mathbf{p}\_k = 0(rk+1​+βk​pk​)⊤Apk​=0

rk+1⊤Apk+βkpk⊤Apk=0\mathbf{r}\_{k+1}^\top A\mathbf{p}\_k + \beta\_k\mathbf{p}\_k^\top A\mathbf{p}\_k = 0rk+1⊤​Apk​+βk​pk⊤​Apk​=0

So

βk=−rk+1⊤Apkpk⊤Apk\beta\_k = -\frac{\mathbf{r}\_{k+1}^\top A\mathbf{p}\_k}{\mathbf{p}\_k^\top A\mathbf{p}\_k}βk​=−pk⊤​Apk​rk+1⊤​Apk​​

With additional CG identities, this becomes the well-known Fletcher–Reeves-style expression:

βk=rk+1⊤rk+1rk⊤rk\beta\_k = \frac{\mathbf{r}\_{k+1}^\top\mathbf{r}\_{k+1}}{\mathbf{r}\_k^\top\mathbf{r}\_k}βk​=rk⊤​rk​rk+1⊤​rk+1​​

(For SPD quadratics and exact arithmetic, these are consistent. In numerical practice, variants exist.)

### Putting it together (vanilla CG algorithm)

Given SPD A, **b**, and **x**₀:

1) **r**₀ = **b** − A**x**₀

2) **p**₀ = **r**₀

3) For k = 0, 1, 2, … until converged:

- •αk=(rk⊤rk)/(pk⊤Apk)\alpha\_k = (\mathbf{r}\_k^\top\mathbf{r}\_k)/(\mathbf{p}\_k^\top A\mathbf{p}\_k)αk​=(rk⊤​rk​)/(pk⊤​Apk​)
- •**x**ₖ₊₁ = **x**ₖ + αₖ **p**ₖ
- •**r**ₖ₊₁ = **r**ₖ − αₖ A**p**ₖ
- •βk=(rk+1⊤rk+1)/(rk⊤rk)\beta\_k = (\mathbf{r}\_{k+1}^\top\mathbf{r}\_{k+1})/(\mathbf{r}\_k^\top\mathbf{r}\_k)βk​=(rk+1⊤​rk+1​)/(rk⊤​rk​)
- •**p**ₖ₊₁ = **r**ₖ₊₁ + βₖ **p**ₖ

### What convergence means here

CG is typically stopped when the residual is small:

∥rk∥2∥b∥2≤ε\frac{\|\mathbf{r}\_k\|\_2}{\|\mathbf{b}\|\_2} \le \varepsilon∥b∥2​∥rk​∥2​​≤ε

Because **r**ₖ is the gradient (up to sign), small residual also means near-stationary for the quadratic.

### A note on complexity and when CG shines

CG is attractive when:

- •A is large and sparse
- •you can compute AvA\mathbf{v}Av fast without forming dense matrices
- •you cannot afford O(n3)O(n^3)O(n3) factorization

Per iteration cost is dominated by one ApkA\mathbf{p}\_kApk​ product plus a handful of dot products and axpy operations.

Memory is small: a few vectors (often 4–6) of length n.

This is why CG is the workhorse for PDE discretizations, large least-squares normal equations (carefully), and many kernel / Gaussian process subproblems.

## Application/Connection: Preconditioning and the Geometry of Faster Convergence

### Why preconditioning exists

In exact arithmetic, CG solves in ≤ n steps. So why do people obsess over convergence speed?

Because in realistic problems:

- •n may be millions
- •roundoff means you won’t see exact n-step termination
- •you stop when residual is “good enough,” long before n

So the practical question becomes:

> How many iterations to reach tolerance?

This is governed largely by the **condition number**

κ(A)=λmax⁡(A)λmin⁡(A)\kappa(A) = \frac{\lambda\_{\max}(A)}{\lambda\_{\min}(A)}κ(A)=λmin​(A)λmax​(A)​

When κ(A) is large, the ellipsoids are extremely stretched, and CG must work hard to correct error components along small-eigenvalue directions.

A classic bound (informal but insightful) is that the A-norm error decreases like:

∥xk−x∗∥A∥x0−x∗∥A≤2(κ−1κ+1)k\frac{\|\mathbf{x}\_k-\mathbf{x}^\*\|\_A}{\|\mathbf{x}\_0-\mathbf{x}^\*\|\_A} \le 2\left(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\right)^k∥x0​−x∗∥A​∥xk​−x∗∥A​​≤2(κ​+1κ​−1​)k

You don’t need to memorize this; the message is:

- •convergence depends on √κ
- •reducing κ can massively reduce iterations

### Preconditioning: change the problem without changing the solution

A **preconditioner** is an SPD matrix M that approximates A but is easier to invert (or solve with).

We want to solve

Ax=bA\mathbf{x}=\mathbf{b}Ax=b

but instead run CG on a transformed system with better conditioning.

There are multiple equivalent views.

#### View 1: Left-preconditioning

Solve

M−1Ax=M−1bM^{-1}A\mathbf{x} = M^{-1}\mathbf{b}M−1Ax=M−1b

This does not preserve symmetry in the usual Euclidean inner product, but it can be handled carefully (see View 3).

#### View 2: Symmetric preconditioning (the clean SPD story)

Use M=C⊤CM = C^\top CM=C⊤C (Cholesky of M). Define y=Cx\mathbf{y} = C\mathbf{x}y=Cx.

Start with:

Ax=bA\mathbf{x}=\mathbf{b}Ax=b

Substitute x=C−1y\mathbf{x}=C^{-1}\mathbf{y}x=C−1y:

AC−1y=bA C^{-1}\mathbf{y} = \mathbf{b}AC−1y=b

Multiply by C−⊤C^{-\top}C−⊤:

C−⊤AC−1y=C−⊤bC^{-\top} A C^{-1}\mathbf{y} = C^{-\top}\mathbf{b}C−⊤AC−1y=C−⊤b

Now the matrix

A~=C−⊤AC−1\tilde{A} = C^{-\top}AC^{-1}A~=C−⊤AC−1

is SPD, and hopefully has a much smaller condition number than A.

Run standard CG on A~y=b~\tilde{A}\mathbf{y}=\tilde{\mathbf{b}}A~y=b~ and map back x=C−1y\mathbf{x}=C^{-1}\mathbf{y}x=C−1y.

#### View 3: “Preconditioned inner product” (most intuitive)

Preconditioned CG (PCG) can be seen as running CG where the notion of orthogonality is changed by M.

Instead of using raw residual **r**ₖ, define a “preconditioned residual” **z**ₖ:

zk=M−1rk\mathbf{z}\_k = M^{-1}\mathbf{r}\_kzk​=M−1rk​

Think: **z**ₖ is what you get after cheaply solving Mzk=rkM\mathbf{z}\_k=\mathbf{r}\_kMzk​=rk​.

Then PCG uses dot products like rk⊤zk\mathbf{r}\_k^\top\mathbf{z}\_krk⊤​zk​ to measure progress.

### PCG algorithm (practical form)

Given SPD A, SPD M, **b**, **x**₀:

- •**r**₀ = **b** − A**x**₀
- •Solve Mz0=r0M\mathbf{z}\_0 = \mathbf{r}\_0Mz0​=r0​
- •**p**₀ = **z**₀

For k = 0, 1, 2, …:

- •αk=rk⊤zkpk⊤Apk\alpha\_k = \dfrac{\mathbf{r}\_k^\top\mathbf{z}\_k}{\mathbf{p}\_k^\top A\mathbf{p}\_k}αk​=pk⊤​Apk​rk⊤​zk​​
- •**x**ₖ₊₁ = **x**ₖ + αₖ **p**ₖ
- •**r**ₖ₊₁ = **r**ₖ − αₖ A**p**ₖ
- •Solve Mzk+1=rk+1M\mathbf{z}\_{k+1} = \mathbf{r}\_{k+1}Mzk+1​=rk+1​
- •βk=rk+1⊤zk+1rk⊤zk\beta\_k = \dfrac{\mathbf{r}\_{k+1}^\top\mathbf{z}\_{k+1}}{\mathbf{r}\_k^\top\mathbf{z}\_k}βk​=rk⊤​zk​rk+1⊤​zk+1​​
- •**p**ₖ₊₁ = **z**ₖ₊₁ + βₖ **p**ₖ

Compared to CG, you add one extra operation: apply M−1M^{-1}M−1 (implemented as solving with M).

### What makes a “good” preconditioner?

A good M satisfies a three-way tradeoff:

| Goal | What you want | Why it matters |
| --- | --- | --- |
| Accurate | M ≈ A (spectrally) | Reduces κ of the preconditioned system |
| Cheap | Solve M **z** = **r** fast | Each iteration must remain inexpensive |
| Stable | M SPD and numerically well-behaved | Ensures PCG theory + avoids breakdown |

Common choices:

- •**Jacobi / diagonal**: M=diag(A)M = \mathrm{diag}(A)M=diag(A) (cheap, modest gains)
- •**Incomplete Cholesky (IC)**: sparse approximation of Cholesky (often excellent for PDEs)
- •**SSOR / Gauss–Seidel variants**: classical iterative preconditioners
- •**Multigrid preconditioners**: often near-optimal for elliptic PDEs

### Visualization: preconditioning as “making ellipses rounder”

Preconditioning’s geometric effect is easier than its algebra:

- •Original problem has level sets shaped by A (possibly very elongated ellipses).
- •After the change of variables induced by M, those ellipses become closer to circles.

**Interactive canvas suggestion (add-on mode):**

- •Show original ellipsoids in x-space.
- •Let user choose M (diagonal, IC(0), or a toy exact M=A).
- •Show transformed coordinates y where A~=C−⊤AC−1\tilde{A}=C^{-\top}AC^{-1}A~=C−⊤AC−1.
- •Show how κ changes and how many CG steps are needed.

This makes the “conditioning → iteration count” link tangible.

### Connection to least squares and normal equations (careful)

Many problems arrive as least squares:

min⁡x∥Bx−c∥22\min\_{\mathbf{x}} \|B\mathbf{x}-\mathbf{c}\|\_2^2xmin​∥Bx−c∥22​

Normal equations yield SPD system:

B⊤Bx=B⊤cB^\top B\mathbf{x} = B^\top\mathbf{c}B⊤Bx=B⊤c

You *can* run CG on A=B⊤BA=B^\top BA=B⊤B, but note:

- •conditioning squares: κ(B⊤B)=κ(B)2\kappa(B^\top B)=\kappa(B)^2κ(B⊤B)=κ(B)2
- •can be significantly worse numerically

Often better: use methods like LSQR / LSMR (Krylov methods tailored to least squares), or precondition aggressively.

### What you should leave with

CG is a bridge between optimization and linear algebra:

- •optimization perspective: exact line searches on a quadratic in cleverly chosen directions
- •linear algebra perspective: Krylov method minimizing error in A-norm
- •numerical perspective: preconditioning is everything

## Worked Examples (3)

### CG on a 2×2 SPD system: see α, residual orthogonality, and fast termination

Solve A x = b with

A = [[4, 1], [1, 3]] (SPD), b = [1, 2]^T, start x0 = [0, 0]^T.

We will compute two CG iterations and observe that in 2D it reaches the exact solution in ≤ 2 steps (in exact arithmetic).

1. 1) Initialize

   x0 = [0, 0]^T

   r0 = b - A x0 = b = [1, 2]^T

   p0 = r0 = [1, 2]^T
2. 2) Compute α0

   First compute A p0:

   A p0 = [[4,1],[1,3]] [1,2]^T = [4*1+1*2, 1*1+3*2]^T = [6, 7]^T

   Now compute dot products:

   r0^T r0 = 1^2 + 2^2 = 5

   p0^T A p0 = p0^T (A p0) = [1,2]·[6,7] = 1*6 + 2*7 = 20

   So α0 = (r0^T r0)/(p0^T A p0) = 5/20 = 1/4
3. 3) Update x1 and r1

   x1 = x0 + α0 p0 = [0,0] + (1/4)[1,2] = [1/4, 1/2]

   r1 = r0 - α0 A p0 = [1,2] - (1/4)[6,7] = [1 - 6/4, 2 - 7/4] = [-1/2, 1/4]
4. 4) Check residual orthogonality (r1 ⟂ r0)

   r0^T r1 = [1,2]·[-1/2, 1/4] = -1/2 + 2\*(1/4) = -1/2 + 1/2 = 0

   So r0 ⟂ r1 in Euclidean inner product (as theory predicts).
5. 5) Compute β0 and p1

   r1^T r1 = (-1/2)^2 + (1/4)^2 = 1/4 + 1/16 = 5/16

   β0 = (r1^T r1)/(r0^T r0) = (5/16)/5 = 1/16

   p1 = r1 + β0 p0 = [-1/2, 1/4] + (1/16)[1,2]

   = [-1/2 + 1/16, 1/4 + 2/16]

   = [(-8+1)/16, (4+2)/16] = [-7/16, 6/16] = [-7/16, 3/8]
6. 6) Compute α1

   Compute A p1:

   A p1 = [[4,1],[1,3]] [-7/16, 3/8]^T

   First component: 4*(-7/16) + 1*(3/8) = -28/16 + 6/16 = -22/16 = -11/8

   Second component: 1*(-7/16) + 3*(3/8) = -7/16 + 9/8 = -7/16 + 18/16 = 11/16

   Now compute:

   r1^T r1 = 5/16 (already)

   p1^T A p1 = p1^T (A p1) = [-7/16, 3/8]·[-11/8, 11/16]

   = (-7/16)*(-11/8) + (3/8)*(11/16)

   = 77/128 + 33/128 = 110/128 = 55/64

   So α1 = (r1^T r1)/(p1^T A p1) = (5/16)/(55/64) = (5/16)\*(64/55) = 20/55 = 4/11
7. 7) Update x2 and r2

   x2 = x1 + α1 p1

   = [1/4, 1/2] + (4/11)[-7/16, 3/8]

   Compute the increment:

   (4/11)\*(-7/16) = -28/176 = -7/44

   (4/11)\*(3/8) = 12/88 = 3/22

   So x2 = [1/4 - 7/44, 1/2 + 3/22]

   Convert:

   1/4 = 11/44, so 11/44 - 7/44 = 4/44 = 1/11

   1/2 = 11/22, so 11/22 + 3/22 = 14/22 = 7/11

   Thus x2 = [1/11, 7/11]

   Now residual:

   r2 = r1 - α1 A p1

   = [-1/2, 1/4] - (4/11)[-11/8, 11/16]

   Increment:

   (4/11)\*(-11/8) = -44/88 = -1/2

   (4/11)\*(11/16) = 44/176 = 1/4

   So r2 = [-1/2 - (-1/2), 1/4 - 1/4] = [0, 0]

**Insight:** In 2D, CG terminates in at most 2 steps (exact arithmetic) because it constructs two A-conjugate directions spanning the space. The residuals became orthogonal (r0 ⟂ r1), and after the second step the residual is exactly zero, meaning A x2 = b. The solution is x\* = [1/11, 7/11].

### Why preconditioning helps: compare κ before/after on a diagonal SPD system

Consider A = diag(1, 100) and b arbitrary. This is SPD but ill-conditioned: κ(A)=100. We show how a simple preconditioner makes the problem perfectly conditioned.

We focus on the geometry/conditioning rather than running many iterations.

1. 1) Compute condition number

   Eigenvalues of A are 1 and 100.

   So κ(A) = 100/1 = 100.

   Level sets of f(x)=½ x^T A x - b^T x are very elongated ellipses (narrow valley).
2. 2) Choose a preconditioner M ≈ A

   Let M = diag(1, 100) = A itself (an “ideal” but usually impractical preconditioner).

   Then M is SPD and easy to invert here.
3. 3) Form the symmetrically preconditioned matrix

   Take C such that M = C^T C. Since M is diagonal with positive entries, pick C = diag(1, 10).

   Then

   Â = C^{-T} A C^{-1}.

   But A = M = C^T C, so:

   Â = C^{-T} (C^T C) C^{-1} = (C^{-T} C^T)(C C^{-1}) = I.
4. 4) Condition number after preconditioning

   κ(Â) = κ(I) = 1.

   So in transformed coordinates, the quadratic has spherical level sets and CG converges in essentially one step (again, in idealized exact arithmetic).
5. 5) Interpret for realistic M

   In real problems, M is not exactly A, but if M captures most of A’s spectral shape, Â’s eigenvalues cluster more tightly and κ(Â) drops dramatically—leading to far fewer CG iterations.

**Insight:** Preconditioning is best understood as changing the metric so the ellipsoids become closer to circles. CG’s iteration count is controlled by the spread of eigenvalues; reducing that spread (lower κ) is the direct route to faster convergence.

### PCG step mechanics: compute α and β using rᵀz (not rᵀr)

Use the same system as Example 1 but apply a simple Jacobi preconditioner M = diag(A) = diag(4,3).

We show one iteration of PCG to see how z = M^{-1} r enters the formulas.

A = [[4,1],[1,3]], b = [1,2]^T, x0=[0,0]^T.

1. 1) Initialize

   r0 = b - A x0 = [1,2]^T

   Solve M z0 = r0 with M=diag(4,3):

   z0 = [1/4, 2/3]^T

   p0 = z0
2. 2) Compute α0

   Compute A p0:

   A p0 = [[4,1],[1,3]] [1/4, 2/3]^T

   First component: 4*(1/4) + 1*(2/3) = 1 + 2/3 = 5/3

   Second component: 1*(1/4) + 3*(2/3) = 1/4 + 2 = 9/4

   Compute dot products:

   r0^T z0 = [1,2]·[1/4,2/3] = 1/4 + 4/3 = (3/12 + 16/12)=19/12

   p0^T A p0 = [1/4,2/3]·[5/3,9/4] = (1/4)(5/3) + (2/3)(9/4) = 5/12 + 18/12 = 23/12

   So α0 = (r0^T z0)/(p0^T A p0) = (19/12)/(23/12) = 19/23
3. 3) Update x1 and r1

   x1 = x0 + α0 p0 = (19/23)[1/4,2/3] = [19/92, 38/69]

   r1 = r0 - α0 A p0 = [1,2] - (19/23)[5/3,9/4]

   Compute components:

   First: 1 - (19/23)(5/3) = 1 - 95/69 = (69-95)/69 = -26/69

   Second: 2 - (19/23)(9/4) = 2 - 171/92 = (184-171)/92 = 13/92
4. 4) Compute z1 and β0

   Solve M z1 = r1:

   z1 = [(-26/69)/4, (13/92)/3] = [-26/276, 13/276] = [-13/138, 13/276]

   Compute β0 = (r1^T z1)/(r0^T z0)

   First compute r1^T z1:

   r1^T z1 = [-26/69, 13/92]·[-13/138, 13/276]

   = (-26/69)(-13/138) + (13/92)(13/276)

   = 338/(9522) + 169/(25392)

   Simplify:

   338/9522 = 169/4761

   Now common denominator 4761*? Note 25392 = 4761*(25392/4761) not integer; keep numeric:

   169/4761 ≈ 0.03550

   169/25392 ≈ 0.00666

   So r1^T z1 ≈ 0.04216

   r0^T z0 = 19/12 ≈ 1.5833

   Thus β0 ≈ 0.04216 / 1.5833 ≈ 0.0266
5. 5) Update p1

   p1 = z1 + β0 p0

   This shows PCG mixes the new preconditioned residual with the previous direction, analogous to CG but using M-weighted inner products.

**Insight:** In PCG, the key scalar is rᵀz where z=M^{-1}r. This is the natural measure of residual size in the preconditioned geometry, and it replaces rᵀr throughout the recurrence.

## Key Takeaways

- ✓

  CG is designed for SPD systems A x = b, equivalently minimizing the strictly convex quadratic f(x)=½xᵀAx−bᵀx.
- ✓

  Residuals **r**ₖ = **b** − A**x**ₖ are negative gradients; CG uses them to build improved search directions.
- ✓

  CG search directions are **A-conjugate**: pᵢᵀ A pⱼ = 0 for i≠j, enabling independent progress on the quadratic’s curvature.
- ✓

  Each iteration performs an exact 1-D minimization along **p**ₖ, with αₖ = (rₖᵀrₖ)/(pₖᵀA pₖ) in standard CG.
- ✓

  In exact arithmetic, CG reaches the exact solution in at most n steps because it searches over expanding Krylov subspaces Kₖ(A,r₀).
- ✓

  Practical convergence depends strongly on conditioning; iteration counts track eigenvalue spread and κ(A).
- ✓

  Preconditioning (PCG) introduces an SPD M≈A, using z=M^{-1}r and replacing rᵀr with rᵀz, often reducing iterations dramatically.
- ✓

  The most useful visual intuition: CG builds new dimensions (Krylov growth) while keeping directions independent under the A-metric (conjugacy).

## Common Mistakes

- ✗

  Applying CG to non-SPD matrices (indefinite or nonsymmetric) and expecting it to work; use MINRES/GMRES or reformulate.
- ✗

  Using normal equations A=BᵀB without considering conditioning (κ squares) and then blaming CG for slow convergence.
- ✗

  Choosing a preconditioner M that is not SPD (or implemented inconsistently), which can break PCG assumptions and cause instability.
- ✗

  Stopping based only on small step sizes or objective decrease rather than monitoring the residual norm (relative ||r||/||b||).

## Practice

easy

Show that minimizing f(x)=½xᵀAx−bᵀx with SPD A has a unique minimizer x *and that it satisfies A x* = b.

**Hint:** Compute ∇f(x). Use SPD to argue strict convexity and uniqueness.

Show solution

Compute the gradient:

∇f(x)=A x − b (since A is symmetric).

A critical point satisfies A x\*=b.

Because A is SPD, f is strictly convex (Hessian ∇²f=A ≻ 0), so the critical point is unique and is the global minimizer.

medium

Run one full CG iteration for A = [[2,0],[0,8]], b=[2,8]^T, x0=[0,0]^T. Compute r0, p0, α0, x1, r1, and verify r0ᵀr1=0.

**Hint:** Because A is diagonal, A p0 is easy. Use α0=(r0ᵀr0)/(p0ᵀA p0).

Show solution

r0=b−Ax0=b=[2,8]^T. p0=r0.

A p0 = [2*2, 8*8]^T = [4,64]^T.

r0ᵀr0 = 2^2+8^2=68.

p0ᵀA p0 = [2,8]·[4,64]=8+512=520.

α0=68/520=17/130.

x1=x0+α0p0=(17/130)[2,8]=[34/130, 136/130]=[17/65, 68/65].

r1=r0−α0A p0=[2,8]−(17/130)[4,64]=[2−68/130, 8−1088/130]

= [ (260−68)/130, (1040−1088)/130 ] = [192/130, −48/130] = [96/65, −24/65].

Check orthogonality:

r0ᵀr1 = [2,8]·[96/65, −24/65] = 192/65 − 192/65 = 0.

hard

Consider preconditioning A=diag(1,100,10000) with M=diag(1,100,10000). Compute κ(A) and κ(C^{-T}AC^{-1}) where M=CᵀC. Explain in one sentence what this predicts about CG iteration count.

**Hint:** For diagonal SPD, eigenvalues are diagonal entries. If M=A then the symmetrically preconditioned matrix becomes I.

Show solution

Eigenvalues of A are {1,100,10000}, so κ(A)=10000/1=10000.

With M=A and C=diag(1,10,100), we get C^{-T}AC^{-1}=I, so κ=1.

Prediction: preconditioning collapses the eigenvalue spread, so CG should converge in dramatically fewer iterations (in the ideal case, essentially immediately).

## Connections

Next nodes you may want:

- •[Krylov Subspace Methods](/tech-tree/krylov-subspace-methods/)
- •[Condition Number and Numerical Stability](/tech-tree/condition-number/)
- •[Preconditioning Techniques (Incomplete Factorizations, Multigrid)](/tech-tree/preconditioning/)
- •[Least Squares and Normal Equations](/tech-tree/least-squares-normal-equations/)
- •[GMRES and MINRES for Non-SPD Systems](/tech-tree/gmres-minres/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
