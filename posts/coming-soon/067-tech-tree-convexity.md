---
title: Convex Functions
description: Functions where line segment between points lies above graph.
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
permalink: /tech-tree/convexity/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Convex Functions

OptimizationDifficulty: ★★★☆☆Depth: 6Unlocks: 15

Functions where line segment between points lies above graph.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Convex combination inequality: for any points x,y and any scalar t in [0,1], f(t x + (1-t) y) <= t f(x) + (1-t) f(y)
- -First-order supporting-hyperplane condition: for differentiable f, for all x,y, f(y) >= f(x) + gradient f(x) dot (y - x)

## Key Symbols & Notation

f (function R^n -> R); t (scalar in [0,1])

## Essential Relationships

- -Equivalence under differentiability: f satisfies the convex combination inequality iff it satisfies the first-order supporting-hyperplane condition when the gradient exists everywhere

## Prerequisites (2)

[Gradients5 atoms](/tech-tree/gradients/)[Derivatives6 atoms](/tech-tree/derivatives-basic/)

## Unlocks (2)

[Convex Optimizationlvl 4](/tech-tree/convex-optimization/)[Loss Functionslvl 4](/tech-tree/loss-functions/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[diminishing returnsBusiness

Diminishing returns means the benefit function is concave (negative second derivative) - the SSE vs k curve is convex decreasing, and identifying the elbow is curvature analysis, finding where the second derivative of improvement approaches zero](/business/diminishing-returns/)[convexityBusiness

Direct mathematical definition: a function is convex when the line segment between any two points lies above the graph (positive second derivative). Business convexity is this property applied to payoff and value functions.](/business/convexity/)

Advanced Learning Details

### Graph Position

54

Depth Cost

15

Fan-Out (ROI)

8

Bottleneck Score

6

Chain Length

### Cognitive Load

4

Atomic Elements

37

Total Elements

L2

Percentile Level

L2

Atomic Level

### All Concepts (13)

- - Convex function (inequality definition): f(tx + (1-t)y) ≤ t f(x) + (1-t) f(y) for all x,y and t∈[0,1]
- - Convex combination: point of the form tx + (1-t)y (or ∑\_i λ\_i x\_i with λ\_i≥0, ∑λ\_i=1)
- - Geometric chord interpretation: the line segment connecting two graph points lies above the graph
- - Strict convexity: inequality is strict for x≠y and t∈(0,1)
- - Strong convexity (µ-strong): convexity with a quadratic lower bound (parameter µ>0)
- - Epigraph of a function: epi(f) = {(x, α) : α ≥ f(x)}
- - Sublevel sets (level sets): sets of the form {x : f(x) ≤ c}
- - Second-order characterization: role of second derivatives/Hessian in convexity (univariate f''≥0, multivariate Hessian PSD)
- - First-order/supporting-hyperplane property: tangent (linear) approximation at a point underestimates the function globally
- - Subgradient: generalization of gradient for nondifferentiable convex functions; subgradient set ∂f(x)
- - Uniqueness of minimizer under strict convexity
- - Relationship between convex functions and convex sets (epi(f) convex ⇔ f convex)
- - Operations that preserve convexity: nonnegative weighted sums, positive scalar multiples, pointwise supremum, affine precomposition

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Convexity is the reason some optimization problems feel “easy”: the landscape has no deceptive valleys. Once you learn the two core convexity inequalities, you can recognize when gradient-based methods are safe, when a loss is well-behaved, and why “local = global” can hold.

TL;DR:

A function f is convex if its value on any line segment is at most the linear interpolation of its endpoint values: f(t **x** + (1−t) **y**) ≤ t f(**x**) + (1−t) f(**y**). If f is differentiable, an equivalent condition is the supporting-hyperplane inequality: f(**y**) ≥ f(**x**) + ∇f(**x**) · (**y** − **x**). These characterizations let you prove convexity, derive bounds, and justify optimization guarantees.

## What Is a Convex Function?

### Why convexity matters (motivation first)

In optimization, we often want to minimize a function f: ℝⁿ → ℝ, like a training loss. The hardest part of minimization isn’t taking derivatives—it’s the geometry of the function.

- •If the function has many “dips,” a gradient method can get stuck in a local minimum that is not the global minimum.
- •If the function is **convex**, that specific failure mode disappears: the surface has a controlled shape that prevents hidden basins.

Convexity is a *global* property. It doesn’t just tell you what happens at one point (like a derivative); it constrains what happens between points.

### The geometric definition (line segment lies above the graph)

A function f is **convex** if, when you pick any two points **x**, **y** in its domain and move between them in a straight line, the function value never rises above the straight-line interpolation of the endpoint function values.

Formally, for all **x**, **y** and all t ∈ [0, 1],

f(t **x** + (1 − t) **y**) ≤ t f(**x**) + (1 − t) f(**y**)

This is the **convex combination inequality**.

- •The input t **x** + (1 − t) **y** is a **convex combination** of **x** and **y**.
- •The output bound t f(**x**) + (1 − t) f(**y**) is the matching convex combination of the outputs.

Intuition:

- •The right-hand side is the value on the chord (the straight line segment) connecting the points (**x**, f(**x**)) and (**y**, f(**y**)).
- •Convexity says the graph of f lies **below** that chord.

### Quick mental picture in 1D

If n = 1, with x, y ∈ ℝ, the inequality becomes:

f(t x + (1 − t) y) ≤ t f(x) + (1 − t) f(y)

When f is convex, its curve is “cup-shaped.” A parabola f(x) = x² is convex: the secant line between two points sits above the curve.

### Three important boundary cases

Convexity must hold for all t ∈ [0,1], including:

- •t = 0: f(**y**) ≤ f(**y**) (equality)
- •t = 1: f(**x**) ≤ f(**x**) (equality)
- •t = 1/2: midpoint convexity

f((**x** + **y**)/2) ≤ (f(**x**) + f(**y**))/2

Midpoint convexity alone is not always enough to guarantee convexity unless you assume regularity (like continuity). The full definition uses all t.

### Convex vs concave vs affine

It helps to separate three related shapes:

| Type | Inequality | Shape intuition | Typical role |
| --- | --- | --- | --- |
| Convex | f(t **x** + (1−t) **y**) ≤ t f(**x**) + (1−t) f(**y**) | “Cup” | Minimization-friendly |
| Concave | f(t **x** + (1−t) **y**) ≥ t f(**x**) + (1−t) f(**y**) | “Cap” | Maximization-friendly |
| Affine | equality for all **x**, **y**, t | perfect plane/line | linear models, constraints |

An affine function is both convex and concave.

### Why the definition is global

Notice the definition compares values at **three** locations: **x**, **y**, and the point in between. A derivative only sees an infinitesimal neighborhood. Convexity is stronger: it bans certain global configurations of the graph.

That’s why convexity buys us strong optimization guarantees later (for example, any local minimum becomes global under convexity).

## Core Mechanic 1: Convex Combination Inequality (Chord Condition)

### Why this inequality is the “entry point”

The convex combination inequality is the most direct way to *use* convexity:

f(t **x** + (1 − t) **y**) ≤ t f(**x**) + (1 − t) f(**y**)

It lets you:

- •Prove that averaging inputs can’t increase the function more than averaging outputs.
- •Derive Jensen-style bounds.
- •Show stability: small mixtures of solutions behave predictably.

### The key object: convex combinations

A point **z** is a convex combination of **x** and **y** if:

**z** = t **x** + (1 − t) **y**, with t ∈ [0,1].

Geometrically, **z** lies on the line segment between **x** and **y**.

In higher dimensions (ℝⁿ), nothing changes conceptually: you still move along a segment, but the segment lives in n-dimensional space.

### A useful rearrangement (making “gap” explicit)

Define the chord interpolation value:

L(t) = t f(**x**) + (1 − t) f(**y**)

Convexity says:

f(t **x** + (1 − t) **y**) − L(t) ≤ 0

The difference f(…) − L(t) is sometimes called the **convexity gap** (it’s ≤ 0 for convex functions under this sign convention).

### Extending from 2 points to many points (Jensen’s inequality)

The 2-point definition generalizes to a finite mixture. Suppose we have points **x**₁, …, **x**ₘ and weights α₁, …, αₘ such that:

αᵢ ≥ 0, and ∑ᵢ αᵢ = 1

Then a convex function satisfies:

f(∑ᵢ αᵢ **x**ᵢ) ≤ ∑ᵢ αᵢ f(**x**ᵢ)

This is a standard form of **Jensen’s inequality** (finite version).

Why mention this here? Because in machine learning and optimization you constantly average:

- •averaging data points
- •averaging gradients
- •averaging model parameters

Convexity tells you how the loss behaves under averaging.

### Examples you can sanity-check quickly

1) f(**x**) = ‖**x**‖² is convex.

- •In 1D, x² is convex.
- •In ℝⁿ, ‖**x**‖² is a bowl.

2) f(x) = eˣ is convex in 1D.

- •It curves upward; chords lie above.

3) f(x) = |x| is convex.

- •It has a “V” shape: still convex though not differentiable at 0.

### Convexity is preserved by common operations

These “closure properties” are practical: they let you build convex functions from known convex pieces.

| Operation | Result | Notes |
| --- | --- | --- |
| Nonnegative weighted sum | convex | If fᵢ convex and cᵢ ≥ 0 then ∑ cᵢ fᵢ is convex |
| Add affine function | convex | f + (**a**·**x** + b) stays convex |
| Pointwise maximum | convex | max(f, g) is convex |
| Composition with affine map | convex | If f convex then g(**x**) = f(A**x** + **b**) is convex |

These are heavily used when designing loss functions and regularizers.

### A note on domains

Convexity is defined on a **convex domain** (a set where line segments stay inside). If the domain isn’t convex, the inequality can fail simply because t **x** + (1 − t) **y** might not be in the domain.

So when you see “f is convex,” it usually implicitly means:

- •the domain of f is convex, and
- •the inequality holds for all points in that domain.

### Connecting to optimization

The chord condition already hints at why minima behave well:

- •If you have two points with low values, every point between them can’t be worse than the chord suggests.
- •This prevents isolated “low pockets” surrounded by higher barriers typical of nonconvex landscapes.

But to connect convexity to gradients (and to optimization algorithms), we need the second core characterization: the first-order supporting-hyperplane condition.

## Core Mechanic 2: First-Order Supporting-Hyperplane Condition (Gradient Inequality)

### Why introduce a gradient-based condition?

The convex combination inequality is geometric and global. Optimization algorithms are local and differential: they use ∇f(**x**).

So we want a condition that:

- •talks directly about ∇f(**x**)
- •is equivalent to convexity (under differentiability)
- •gives linear lower bounds we can use in proofs and algorithms

That condition is the **supporting-hyperplane inequality**.

### Statement (for differentiable functions)

If f is differentiable on a convex domain, then f is convex **iff** for all **x**, **y**:

f(**y**) ≥ f(**x**) + ∇f(**x**) · (**y** − **x**)

Interpretation:

- •The right-hand side is the first-order Taylor approximation at **x** (a tangent hyperplane).
- •Convexity says the function always lies **above** its tangent hyperplanes.

This is the opposite “above/below” direction compared to the chord condition:

- •Chords lie **above** the graph.
- •Tangent planes lie **below** the graph.

Both are signatures of a bowl shape.

### Why it’s called a supporting hyperplane

Define the affine function (a hyperplane in ℝⁿ):

ℓₓ(**y**) = f(**x**) + ∇f(**x**) · (**y** − **x**)

Convexity implies:

ℓₓ(**y**) ≤ f(**y**) for all **y**

So ℓₓ “supports” the epigraph of f (the set of points above the graph). In 2D (n=1), it’s the tangent line touching the curve at x and staying below it.

### A careful derivation sketch: convexity ⇒ gradient inequality

Assume f is convex and differentiable. Fix **x**, **y**. Consider the 1D function along the line segment:

g(t) = f(**x** + t(**y** − **x**)), t ∈ [0,1]

Because f is convex, g is convex as a function of t.

Convexity of g implies (in 1D) that the secant slope is at least the derivative at the left endpoint:

g(1) ≥ g(0) + g′(0)·(1 − 0)

Compute each term:

- •g(1) = f(**y**)
- •g(0) = f(**x**)
- •g′(0) = ∇f(**x**) · (**y** − **x**) (chain rule)

Substitute:

f(**y**) ≥ f(**x**) + ∇f(**x**) · (**y** − **x**)

That is the supporting-hyperplane inequality.

### Reverse direction (gradient inequality ⇒ convexity)

This direction shows the gradient inequality is not just a consequence—it *characterizes* convexity.

Assume for all **x**, **y**:

f(**y**) ≥ f(**x**) + ∇f(**x**) · (**y** − **x**)

We want to show:

f(t **x** + (1 − t) **y**) ≤ t f(**x**) + (1 − t) f(**y**)

One standard route is to apply the gradient inequality twice (once with **x** and once with **y**) to bound f at the mixture point. Let:

**z** = t **x** + (1 − t) **y**

Apply inequality with (**x** as base point, **y** = **z**):

f(**z**) ≥ f(**x**) + ∇f(**x**) · (**z** − **x**)

Similarly with (**y** as base point, **y** = **z**):

f(**z**) ≥ f(**y**) + ∇f(**y**) · (**z** − **y**)

Then, with additional arguments (or integrating along the segment), one can recover the chord inequality. The key idea is: if every tangent plane underestimates f globally, the function cannot bend downward in a way that violates convexity.

For this lesson, the crucial takeaway is operational:

- •**To use convexity in gradient-based reasoning, you reach for the supporting-hyperplane inequality.**

### Consequence: monotonicity of the gradient (useful fact)

For differentiable convex f, the gradient is a **monotone operator**:

(∇f(**x**) − ∇f(**y**)) · (**x** − **y**) ≥ 0

You can derive it by writing the supporting-hyperplane inequality twice:

1) f(**y**) ≥ f(**x**) + ∇f(**x**) · (**y** − **x**)

2) f(**x**) ≥ f(**y**) + ∇f(**y**) · (**x** − **y**)

Add them:

0 ≥ ∇f(**x**) · (**y** − **x**) + ∇f(**y**) · (**x** − **y**)

Rewrite:

0 ≥ (∇f(**x**) − ∇f(**y**)) · (**y** − **x**)

Multiply by −1:

(∇f(**x**) − ∇f(**y**)) · (**y** − **x**) ≥ 0

Equivalently:

(∇f(**x**) − ∇f(**y**)) · (**x** − **y**) ≥ 0

This property underlies convergence proofs for gradient methods and proximal algorithms.

### Optional but important: the Hessian test (when twice differentiable)

If f is twice differentiable, convexity is equivalent to:

∇²f(**x**) ⪰ 0 for all **x**

Meaning the Hessian matrix is positive semidefinite (PSD). In quadratic form language:

∀ **v** ≠ **0**, **v**ᵀ ∇²f(**x**) **v** ≥ 0

This is often the easiest way to check convexity for smooth functions. But the node you’re learning emphasizes the two inequalities (chord and supporting hyperplane), which remain valid even when Hessians are inconvenient or undefined.

### How to choose which characterization to use

| You want to… | Use… | Why |
| --- | --- | --- |
| Prove an averaging bound | Convex combination inequality | It directly compares f at mixtures |
| Prove a linear lower bound | Supporting-hyperplane inequality | It gives global underestimators |
| Check convexity of smooth formula | Hessian PSD test | Mechanical computation |

In optimization, you’ll constantly switch between them depending on what the proof needs.

## Application/Connection: Why Convexity Makes Optimization and Loss Design Work

### Local minima become global minima (the promise)

One of the most valuable theorems in optimization is:

If f is convex, then **every local minimizer is a global minimizer**.

Why? Suppose **x**★ is a local minimizer but not global. Then there exists **y** with f(**y**) < f(**x**★). Consider points on the segment:

**z**(t) = t **y** + (1 − t) **x**★

By convexity:

f(**z**(t)) ≤ t f(**y**) + (1 − t) f(**x**★)

Since f(**y**) < f(**x**★), for small t > 0 the right-hand side is strictly less than f(**x**★), implying points arbitrarily close to **x**★ have smaller value—contradicting local optimality.

This is the geometric “no false basins” idea.

### First-order optimality condition becomes sufficient

In general (nonconvex), ∇f(**x**) = **0** might be a max, min, or saddle.

For differentiable convex f, the condition is stronger:

∇f(**x**★) = **0** ⇒ **x**★ is a global minimizer.

Proof using supporting hyperplane:

f(**y**) ≥ f(**x**★) + ∇f(**x**★) · (**y** − **x**★)

If ∇f(**x**★) = **0**, then:

f(**y**) ≥ f(**x**★)

So nothing beats **x**★.

This is why convexity pairs so well with gradient-based methods: stationary points are safe.

### Convex loss functions in machine learning

Many common losses are convex in the model’s *linear predictions* or in parameters for linear models.

Examples:

- •Mean squared error: (y − ŷ)² is convex in ŷ.
- •Logistic loss: log(1 + e^(−y·s)) is convex in score s.
- •Hinge loss: max(0, 1 − y·s) is convex in score s.

Convexity doesn’t automatically make deep networks convex (they aren’t), but it remains crucial:

- •for convex models (linear / generalized linear)
- •for convex subproblems
- •for analyzing regularizers and surrogate losses

### Regularization as convex function building

Regularizers are often chosen to be convex because they preserve convexity of the overall objective.

If you minimize:

F(**w**) = loss(**w**) + λ·R(**w**)

and both loss and R are convex, then F is convex.

Typical convex regularizers:

- •ℓ₂: R(**w**) = ‖**w**‖²
- •ℓ₁: R(**w**) = ‖**w**‖₁ = ∑ᵢ |wᵢ|

### Practical diagnostic: using tangent lower bounds

The supporting-hyperplane inequality gives a reusable bound:

f(**y**) ≥ f(**x**) + ∇f(**x**)·(**y** − **x**)

In algorithms, you often set **x** to the current iterate and **y** to the optimum (unknown), then manipulate the inequality to bound suboptimality.

It also motivates methods that iteratively minimize a surrogate:

- •Replace f by a linear approximation plus a stabilizing term.
- •Because f lies above its tangent, you control descent.

This idea is a stepping stone to gradient descent analysis and to proximal-gradient methods.

### Connection to what you unlock next

- •**Convex Optimization** will use convexity to justify efficient algorithms, duality, KKT conditions, and convergence rates. Convexity is the “structural assumption” that makes those results true.
- •**Loss Functions** will use convexity as a design criterion: convex surrogates for 0–1 loss, convex penalties for robustness and sparsity, and composition rules for building trainable objectives.

In short: convexity is less about memorizing a definition and more about learning a reliable shape constraint you can exploit everywhere.

## Worked Examples (3)

### Verify convexity of f(x) = x² using the convex combination inequality

Let f(x) = x² on ℝ. Show that for any x, y ∈ ℝ and t ∈ [0,1], f(t x + (1−t) y) ≤ t f(x) + (1−t) f(y).

1. Start from the convexity inequality we want:

   (t x + (1−t) y)² ≤ t x² + (1−t) y².
2. Expand the left-hand side:

   (t x + (1−t) y)²

   = t² x² + 2t(1−t) x y + (1−t)² y².
3. Move everything to the right-hand side (right minus left):

   [t x² + (1−t) y²] − [t² x² + 2t(1−t) x y + (1−t)² y²].
4. Group x² terms and y² terms:

   = (t − t²) x² + ((1−t) − (1−t)²) y² − 2t(1−t) x y.
5. Simplify coefficients:

   (t − t²) = t(1−t)

   ( (1−t) − (1−t)² ) = (1−t)t = t(1−t).
6. So the expression becomes:

   = t(1−t) x² + t(1−t) y² − 2t(1−t) x y

   = t(1−t)(x² − 2xy + y²)

   = t(1−t)(x − y)².
7. Since t ∈ [0,1], we have t(1−t) ≥ 0, and (x−y)² ≥ 0.

   Therefore t(1−t)(x−y)² ≥ 0.
8. Thus [right − left] ≥ 0, which implies:

   (t x + (1−t) y)² ≤ t x² + (1−t) y².

   So f(x) = x² is convex.

**Insight:** This proof shows a common pattern: after expanding, convexity often reduces to a nonnegative square like (x−y)². Convexity is frequently “hidden” nonnegativity.

### Use the supporting-hyperplane inequality for f(\*\*x\*\*) = ‖\*\*x\*\*‖²

Let f(**x**) = ‖**x**‖² on ℝⁿ. Compute ∇f(**x**) and verify f(**y**) ≥ f(**x**) + ∇f(**x**)·(**y**−**x**).

1. Write f explicitly:

   f(**x**) = **x**·**x** = ∑ᵢ xᵢ².
2. Compute the gradient:

   ∇f(**x**) = 2**x**

   (because ∂/∂xᵢ of ∑ⱼ xⱼ² is 2xᵢ).
3. Plug into the supporting-hyperplane inequality:

   Need to show:

   ‖**y**‖² ≥ ‖**x**‖² + (2**x**)·(**y**−**x**).
4. Expand the right-hand side:

   ‖**x**‖² + 2**x**·**y** − 2**x**·**x**

   = ‖**x**‖² + 2**x**·**y** − 2‖**x**‖²

   = 2**x**·**y** − ‖**x**‖².
5. So the inequality becomes:

   ‖**y**‖² ≥ 2**x**·**y** − ‖**x**‖².
6. Bring all terms to the left:

   ‖**y**‖² − 2**x**·**y** + ‖**x**‖² ≥ 0.
7. Recognize the left-hand side as a squared norm:

   ‖**y** − **x**‖² = (**y**−**x**)·(**y**−**x**)

   = ‖**y**‖² − 2**x**·**y** + ‖**x**‖².
8. Thus the inequality is:

   ‖**y** − **x**‖² ≥ 0,

   which is always true.
9. Therefore f(**x**) = ‖**x**‖² satisfies the supporting-hyperplane inequality and is convex.

**Insight:** For squared norm objectives, convexity and many optimization inequalities reduce to the identity ‖**y**−**x**‖² ≥ 0. This is why least-squares problems are so well-behaved.

### Prove convexity of the pointwise maximum: h(x) = max(f(x), g(x))

Assume f and g are convex functions on a convex domain in ℝⁿ. Define h(**x**) = max(f(**x**), g(**x**)). Prove h is convex using the convex combination inequality.

1. Take any **x**, **y** and any t ∈ [0,1]. Let **z** = t **x** + (1−t) **y**.
2. Because f is convex:

   f(**z**) ≤ t f(**x**) + (1−t) f(**y**).
3. Because g is convex:

   g(**z**) ≤ t g(**x**) + (1−t) g(**y**).
4. Take the maximum of the left sides and use that max preserves inequalities:

   max(f(**z**), g(**z**)) ≤ max(t f(**x**) + (1−t) f(**y**), t g(**x**) + (1−t) g(**y**)).
5. Now use a key inequality: for any numbers a₁, a₂, b₁, b₂,

   max(a₁, a₂) ≤ max(b₁, b₂) is not generally true, but here we instead bound the max of two sums by the sum of maxes:

   max(t f(**x**) + (1−t) f(**y**), t g(**x**) + (1−t) g(**y**))

   ≤ t max(f(**x**), g(**x**)) + (1−t) max(f(**y**), g(**y**)).
6. Justification of the previous step:

   - •t f(**x**) ≤ t max(f(**x**), g(**x**)) and t g(**x**) ≤ t max(f(**x**), g(**x**))
   - •(1−t) f(**y**) ≤ (1−t) max(f(**y**), g(**y**)) and similarly for g

   Add the corresponding bounds for each branch, then the maximum of two quantities is ≤ the common upper bound.
7. Substitute h:

   h(**z**) = max(f(**z**), g(**z**))

   ≤ t h(**x**) + (1−t) h(**y**).
8. This matches the convex combination inequality, so h is convex.

**Insight:** Pointwise maxima preserve convexity because “being below a chord” is stable under taking the upper envelope of convex graphs—useful for hinge losses and robust objectives.

## Key Takeaways

- ✓

  Convexity is a global shape constraint: for any **x**, **y**, the graph of f lies below the chord between (f(**x**), f(**y**)).
- ✓

  Formal definition: f(t **x** + (1−t) **y**) ≤ t f(**x**) + (1−t) f(**y**) for all t ∈ [0,1].
- ✓

  If f is differentiable, convexity ⇔ supporting-hyperplane inequality: f(**y**) ≥ f(**x**) + ∇f(**x**)·(**y**−**x**).
- ✓

  Supporting hyperplanes give global linear lower bounds; this is the bridge from convex geometry to gradient-based optimization proofs.
- ✓

  For differentiable convex f, the gradient is monotone: (∇f(**x**)−∇f(**y**))·(**x**−**y**) ≥ 0.
- ✓

  Convexity is preserved under nonnegative sums, adding affine functions, pointwise maxima, and affine changes of variables.
- ✓

  In convex problems, local minima are global; for differentiable convex f, ∇f(**x**★)=**0** is sufficient for global optimality.

## Common Mistakes

- ✗

  Mixing up directions: convex means f at a mixture is ≤ mixture of f values; concave flips the inequality.
- ✗

  Assuming “second derivative ≥ 0” always applies: many convex functions (e.g., |x|) are not twice differentiable everywhere, yet are still convex.
- ✗

  Checking convexity only at t = 1/2 (midpoints) without additional assumptions; full convexity requires all t ∈ [0,1] (or continuity plus midpoint convexity).
- ✗

  Forgetting domain convexity: if the domain isn’t convex, the definition can’t even be applied to all segments.

## Practice

easy

Show that an affine function a(**x**) = **c**·**x** + d is convex on ℝⁿ using the convex combination inequality.

**Hint:** Compute a(t **x** + (1−t) **y**) and compare to t a(**x**) + (1−t) a(**y**). Expect equality.

Show solution

Let a(**x**) = **c**·**x** + d. Then:

a(t **x** + (1−t) **y**)

= **c**·(t **x** + (1−t) **y**) + d

= t (**c**·**x**) + (1−t)(**c**·**y**) + d.

Also:

t a(**x**) + (1−t) a(**y**)

= t(**c**·**x** + d) + (1−t)(**c**·**y** + d)

= t(**c**·**x**) + (1−t)(**c**·**y**) + [t d + (1−t) d]

= t(**c**·**x**) + (1−t)(**c**·**y**) + d.

So a(t **x** + (1−t) **y**) = t a(**x**) + (1−t) a(**y**) for all **x**, **y**, t. Therefore a is convex (and concave).

medium

Let f be differentiable and convex. Prove that if ∇f(**x**★) = **0**, then **x**★ is a global minimizer.

**Hint:** Use the supporting-hyperplane inequality with **x** = **x**★ and arbitrary **y**.

Show solution

Since f is convex and differentiable, for all **y**:

f(**y**) ≥ f(**x**★) + ∇f(**x**★)·(**y** − **x**★).

Given ∇f(**x**★) = **0**, this becomes:

f(**y**) ≥ f(**x**★) + **0**·(**y** − **x**★) = f(**x**★).

Thus no **y** has a smaller value than f(**x**★), so **x**★ is a global minimizer.

medium

Assume f and g are convex on a convex domain. Show that F(**x**) = α f(**x**) + β g(**x**) is convex for α, β ≥ 0.

**Hint:** Apply the convex combination inequality to f and g separately, then multiply by α and β and add.

Show solution

Take any **x**, **y** and t ∈ [0,1]. Since f is convex:

f(t **x** + (1−t) **y**) ≤ t f(**x**) + (1−t) f(**y**).

Similarly for g:

g(t **x** + (1−t) **y**) ≤ t g(**x**) + (1−t) g(**y**).

Multiply the first inequality by α ≥ 0 and the second by β ≥ 0 and add:

α f(t **x** + (1−t) **y**) + β g(t **x** + (1−t) **y**)

≤ t[α f(**x**) + β g(**x**)] + (1−t)[α f(**y**) + β g(**y**)].

The left-hand side is F(t **x** + (1−t) **y**) and the right-hand side is t F(**x**) + (1−t) F(**y**). Therefore F is convex.

## Connections

Next nodes:

- •[Convex Optimization](/tech-tree/convex-optimization/)
- •[Loss Functions](/tech-tree/loss-functions/)

Related background:

- •[Gradients](/tech-tree/gradients/)
- •[Derivatives](/tech-tree/derivatives/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
