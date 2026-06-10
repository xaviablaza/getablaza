---
title: Gradients
description: Vector of partial derivatives. Direction of steepest ascent.
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
permalink: /tech-tree/gradients/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Gradients

CalculusDifficulty: ★★★☆☆Depth: 5Unlocks: 66

Vector of partial derivatives. Direction of steepest ascent.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Gradient is the vector of partial derivatives of a scalar function (one component per variable).
- -Gradient points in the direction of steepest ascent; its magnitude equals the maximal rate of increase.
- -Gradient is orthogonal (normal) to the function's level sets (contours/surfaces).

## Key Symbols & Notation

nabla (del) operator written as 'nabla f' (aka 'grad f')

## Essential Relationships

- -Directional derivative in unit direction u equals the dot product of the gradient with u: D\_u f = (grad f) dot u.

## Prerequisites (2)

[Multivariable Calculus6 atoms](/tech-tree/multivariable-calculus/)[Vectors Introduction6 atoms](/tech-tree/vectors-intro/)

## Unlocks (7)

[Optimization Introductionlvl 3](/tech-tree/optimization-intro/)[Gradient Descentlvl 3](/tech-tree/gradient-descent/)[Convex Functionslvl 3](/tech-tree/convexity/)[Jacobianlvl 3](/tech-tree/jacobian/)[Matrix Calculuslvl 4](/tech-tree/matrix-calculus/)[Lagrange Multiplierslvl 4](/tech-tree/lagrange-multipliers/)[Multivariable Chain Rulelvl 3](/tech-tree/chain-rule-multivar/)

Advanced Learning Details

### Graph Position

50

Depth Cost

66

Fan-Out (ROI)

23

Bottleneck Score

5

Chain Length

### Cognitive Load

5

Atomic Elements

25

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (10)

- - Gradient as a single object: the gradient ∇f of a scalar multivariable function is a vector formed from its partial derivatives
- - Gradient as a vector field: at each point in the domain the gradient assigns a vector (depends on position)
- - Direction of steepest ascent: the gradient vector at a point indicates the direction in which the function increases most rapidly
- - Magnitude as maximal rate: the length (norm) of the gradient equals the maximal instantaneous rate of increase of the function
- - Steepest descent: the negative of the gradient gives the direction of steepest decrease
- - Gradient orthogonality to level sets: the gradient at a point is perpendicular (normal) to the level set (contour) of the function through that point
- - Directional derivative via gradient: directional derivatives can be computed using the gradient and a direction vector
- - Stationary/critical points via gradient: points where the gradient equals the zero vector are candidates for local extrema or saddle points
- - First-order linear approximation (differential) using the gradient: the gradient defines the best linear approximation to the function at a point
- - Use in iterative optimization: the gradient provides the update direction in gradient-based optimization methods (e.g., gradient descent/ascent)

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

When you change a single-variable function f(x), the derivative f′(x) tells you “which way is uphill” and “how steep.” For a function of many variables f(x, y, z, …), the gradient ∇f plays that role: it’s the single object that tells you the uphill direction in the full space.

TL;DR:

The gradient ∇f(**x**) is the vector of partial derivatives. It points in the direction of steepest increase of f, its magnitude ‖∇f‖ is the maximum directional rate of increase, and it is perpendicular (normal) to level sets f(**x**) = c.

## What Is Gradient? (∇f) — Definition with Intuition

### Why we need a new “derivative” in many dimensions

In 1D, the derivative f′(x) answers two questions at once:

1) **Direction:** If f′(x) > 0, moving right increases f; if f′(x) < 0, moving right decreases f.

2) **Rate:** |f′(x)| tells how quickly f changes per unit step.

In multiple dimensions, you can move in infinitely many directions. A single number can’t encode “uphill direction” anymore. We need a **vector** that:

- •has one component per input variable
- •changes predictably with direction
- •recovers the ordinary derivative when we move along a line

That vector is the **gradient**.

### Definition

Let f: ℝⁿ → ℝ be a differentiable scalar function, and let **x** = (x₁, …, xₙ). The gradient of f at **x** is

∇f(**x**) = (∂f/∂x₁, ∂f/∂x₂, …, ∂f/∂xₙ).

We will write gradients as **vectors** (bold): ∇f(**x**) is a vector in ℝⁿ.

### What each component means

The i-th component ∂f/∂xᵢ is the slope of f if you move **only** along the xᵢ axis, holding all other variables constant.

So the gradient collects all “axis-aligned slopes” into a single object. But the real power is that it also tells you what happens when you move in **any** direction, not just along coordinate axes.

### A concrete picture (2D)

For f(x, y):

- •∂f/∂x tells how f changes if you nudge x while keeping y fixed.
- •∂f/∂y tells how f changes if you nudge y while keeping x fixed.

Then

∇f(x, y) = (∂f/∂x, ∂f/∂y).

At a point (x, y), this vector points “uphill” on the surface z = f(x, y). But to make that statement precise, we need directional derivatives.

### Notation: nabla (∇)

The symbol ∇ (“nabla” or “del”) behaves like a vector of partial-derivative operators:

∇ = (∂/∂x₁, …, ∂/∂xₙ).

Applying it to a scalar function f gives ∇f.

### Units sanity check

If f has units (say, meters) and xᵢ has units (say, seconds), then ∂f/∂xᵢ has units meters/second. So ∇f is a vector of “rates per coordinate unit.” This becomes important when different coordinates have different scales (a common source of mistakes in optimization).

## Core Mechanic 1: Directional Derivatives and “Steepest Ascent”

### Why directional derivatives matter

Partial derivatives tell you slopes along coordinate axes. But most interesting motion is not axis-aligned: you might move diagonally in (x, y), or along an arbitrary direction in ℝⁿ.

The **directional derivative** formalizes “rate of change if I move in direction **u**.”

### Directional derivative definition

Let **u** be a **unit vector** (‖**u**‖ = 1). The directional derivative of f at **x** along **u** is

D\_**u** f(**x**) = lim\_{h→0} [f(**x** + h**u**) − f(**x**)] / h.

This is just the ordinary derivative of the 1D function g(h) = f(**x** + h**u**) at h = 0.

### The key identity: directional derivative is a dot product

If f is differentiable, then

D\_**u** f(**x**) = ∇f(**x**) · **u**.

This is the bridge between “vector of partial derivatives” and “change in any direction.”

### Showing the work (derivation sketch in ℝ²)

Let f(x, y) be differentiable and **u** = (u₁, u₂) with ‖**u**‖ = 1. Consider

g(h) = f(x + h u₁, y + h u₂).

By the chain rule,

g′(h) = (∂f/∂x)(x + h u₁, y + h u₂)·u₁ + (∂f/∂y)(x + h u₁, y + h u₂)·u₂.

At h = 0,

D\_**u** f(x, y) = g′(0)

= (∂f/∂x)(x, y)·u₁ + (∂f/∂y)(x, y)·u₂

= (∂f/∂x, ∂f/∂y) · (u₁, u₂)

= ∇f(x, y) · **u**.

The same reasoning extends to ℝⁿ.

### Steepest ascent: why the gradient points uphill

Now that directional change is a dot product, we can ask:

Among all unit directions **u** (‖**u**‖ = 1), which maximizes D\_**u** f(**x**) = ∇f(**x**) · **u**?

Use the Cauchy–Schwarz inequality:

∇f · **u** ≤ ‖∇f‖‖**u**‖ = ‖∇f‖.

Because ‖**u**‖ = 1, we get

D\_**u** f(**x**) ≤ ‖∇f(**x**)‖.

Equality holds exactly when **u** points in the same direction as ∇f:

**u** = ∇f / ‖∇f‖ (when ∇f ≠ **0**).

So:

- •**Direction of steepest ascent**: ∇f(**x**)
- •**Maximum rate of increase**: ‖∇f(**x**)‖
- •**Direction of steepest descent**: −∇f(**x**)

### What about critical points?

If ∇f(**x**) = **0**, then every directional derivative is 0:

D\_**u** f(**x**) = ∇f(**x**) · **u** = 0.

That doesn’t automatically mean a maximum or minimum (it could be a saddle). But it does mean the function has no first-order preference for any direction at that point.

### Local linear approximation (the “first-order model”)

Differentiability implies a local linear model:

f(**x** + **h**) ≈ f(**x**) + ∇f(**x**) · **h** (for small **h**).

This is the multivariable analog of

f(x + h) ≈ f(x) + f′(x)h.

This approximation is what makes gradients so useful in optimization: you can predict how f changes under a small step **h**, then choose **h** to increase or decrease f.

## Core Mechanic 2: Gradients Are Orthogonal to Level Sets

### Why level sets are the right geometric object

For f: ℝ² → ℝ, you often visualize the function using **contours** (level curves):

f(x, y) = c.

For f: ℝ³ → ℝ, you get **level surfaces**:

f(x, y, z) = c.

These describe “where the function value stays constant.” If you walk along a contour, f does not change.

So the key question becomes:

If I move tangent to a level set, why does the gradient end up perpendicular to that motion?

### Tangent directions have zero directional derivative

Suppose you are at a point **x** on the level set f(**x**) = c. Consider a small step **t** that stays on the level set (to first order). Along such a step, f doesn’t change, so the directional derivative in that tangent direction should be 0.

Using the dot-product identity:

0 = D\_**u** f(**x**) = ∇f(**x**) · **u**

for any unit tangent direction **u**.

A vector whose dot product with every tangent direction is 0 must be **normal** to the level set. Therefore:

∇f(**x**) is orthogonal to the level set f(**x**) = c at **x** (when ∇f(**x**) ≠ **0**).

### Showing the work with an implicit curve (ℝ²)

Let the level curve be given implicitly by f(x, y) = c. Suppose it can be parameterized as (x(t), y(t)) staying on the curve. Then

f(x(t), y(t)) = c.

Differentiate both sides with respect to t:

d/dt f(x(t), y(t)) = 0.

Apply the chain rule:

(∂f/∂x)·x′(t) + (∂f/∂y)·y′(t) = 0.

Rewrite in dot-product form:

(∂f/∂x, ∂f/∂y) · (x′(t), y′(t)) = 0

So:

∇f · **r**′(t) = 0,

meaning ∇f is perpendicular to the tangent vector **r**′(t).

### Practical consequence: contour plots + gradient arrows

If you see a contour map of f(x, y):

- •The gradient points **across** the contours, not along them.
- •Where contours are close together, ‖∇f‖ is large (steeper change).

This is a powerful intuition for optimization: to decrease f fastest, move opposite the gradient, cutting across contours as directly as possible.

### The gradient as a normal vector for constraints

This orthogonality is also the reason gradients appear in constrained optimization. If you constrain **x** to live on a level set g(**x**) = 0, then ∇g(**x**) is normal to the constraint surface. At an optimum, the objective’s gradient must align with the constraint’s normal direction (Lagrange multipliers formalize this).

### Summary of the geometric picture

You can hold three ideas in your head simultaneously:

1) ∇f is built from partial derivatives.

2) ∇f gives first-order change: f(**x** + **h**) ≈ f(**x**) + ∇f · **h**.

3) Level sets are perpendicular to ∇f, and the steepest-ascent direction is ∇f itself.

These are not separate facts—they are the same fact seen through different lenses.

## Application / Connection: Optimization, ML, and Beyond

### Why gradients are the workhorse of optimization

Most optimization problems can be phrased as

minimize f(**x**) or maximize f(**x**).

The gradient tells you the direction that increases f most. So to decrease f, you go the other way.

A basic iterative method is **gradient descent**:

**x**ₖ₊₁ = **x**ₖ − α ∇f(**x**ₖ),

where α > 0 is the step size (learning rate).

This update is directly motivated by the linear approximation:

f(**x** + **h**) ≈ f(**x**) + ∇f(**x**) · **h**.

If you pick **h** = −α ∇f, then

∇f · **h** = ∇f · (−α ∇f) = −α ‖∇f‖² ≤ 0,

so the first-order prediction says the objective should go down (for small enough α).

### Gradients in machine learning

In supervised learning, you often minimize a loss function like

L(**w**) = (1/m) ∑ᵢ ℓ(ŷᵢ(**w**), yᵢ),

where **w** are model parameters.

The gradient ∇L(**w**) tells you how to change parameters to reduce loss. Backpropagation is essentially an efficient way to compute these partial derivatives for neural networks.

### Relationship to Jacobian and Hessian

Gradients are the “scalar-output” case of more general derivative objects.

| Object | Maps | Output | Meaning |
| --- | --- | --- | --- |
| Gradient ∇f | f: ℝⁿ → ℝ | vector in ℝⁿ | slopes of scalar function |
| Jacobian J | **F**: ℝⁿ → ℝᵐ | m×n matrix | linear map of first-order changes |
| Hessian ∇²f | f: ℝⁿ → ℝ | n×n matrix | curvature / second derivatives |

If **F** has components Fⱼ, then the Jacobian rows are gradients:

J(**x**) has row j equal to (∇Fⱼ(**x**))ᵀ.

The Hessian shows up when the gradient alone is not enough (e.g., Newton’s method uses curvature to choose better steps).

### Coordinate scaling and geometry (important in practice)

A subtle but practical point: the gradient depends on your coordinate system and scaling.

If one feature is measured in kilometers and another in millimeters, a unit step in each coordinate means wildly different real-world changes. Then “steepest” under the usual Euclidean norm might not align with what you intend.

This is why feature scaling (standardization) matters in ML: it changes the geometry so gradient-based methods behave well.

### Level sets, constraints, and Lagrange multipliers (preview)

If you maximize f(**x**) subject to g(**x**) = 0, the feasible directions are tangent to the level set g(**x**) = 0. At an optimum, moving in any tangent direction can’t improve f, so ∇f must be orthogonal to the tangent space—i.e., it must be parallel to ∇g.

This becomes the condition

∇f(**x**\*) = λ ∇g(**x**\*),

which is the heart of Lagrange multipliers.

### Mental model to carry forward

When you see ∇f in later topics, interpret it as:

- •the best local linear summary of a scalar function’s behavior
- •a direction (where to move)
- •a normal vector (what surfaces look like)
- •the engine for optimization algorithms

## Worked Examples (3)

### Compute a gradient and use it to predict change

Let f(x, y) = x²y + 3y. Compute ∇f(x, y). Then at (x, y) = (2, 1), predict the change in f for a small step **h** = (0.1, −0.05) using the linear approximation.

1. Compute partial derivatives:

   ∂f/∂x = ∂/∂x (x²y + 3y)

   = 2xy.

   ∂f/∂y = ∂/∂y (x²y + 3y)

   = x² + 3.
2. Assemble the gradient:

   ∇f(x, y) = (2xy, x² + 3).
3. Evaluate at (2, 1):

   ∇f(2, 1) = (2·2·1, 2² + 3)

   = (4, 7).
4. Use the first-order approximation:

   Δf ≈ ∇f(2, 1) · **h**

   = (4, 7) · (0.1, −0.05)

   = 4(0.1) + 7(−0.05)

   = 0.4 − 0.35

   = 0.05.

**Insight:** The gradient converts a small vector step **h** into an approximate scalar change via a dot product. The sign comes from alignment: the step had a small component against the y-gradient (−0.05 versus +7), nearly canceling the x increase.

### Steepest ascent direction and maximum increase rate

Let f(x, y) = x eʸ. At the point (0, 0), find (1) the unit direction **u** of steepest ascent and (2) the maximum directional derivative value.

1. Compute the gradient:

   ∂f/∂x = eʸ.

   ∂f/∂y = x eʸ.

   So ∇f(x, y) = (eʸ, x eʸ).
2. Evaluate at (0, 0):

   ∇f(0, 0) = (e⁰, 0·e⁰)

   = (1, 0).
3. Direction of steepest ascent is the normalized gradient:

   **u** = ∇f / ‖∇f‖.

   Here ‖∇f(0,0)‖ = √(1² + 0²) = 1.

   So **u** = (1, 0).
4. Maximum directional derivative equals ‖∇f‖:

   max\_{‖**u**‖=1} D\_**u** f(0,0) = ‖∇f(0,0)‖ = 1.

**Insight:** At (0,0), changing y does nothing to first order because the y-slope is proportional to x. The gradient correctly captures that the only immediate increase comes from moving in +x.

### Gradient is orthogonal to a level set (circle example)

Consider f(x, y) = x² + y². Show that ∇f is perpendicular to the level set f(x, y) = 1 at a point (x, y) on the circle.

1. Compute the gradient:

   ∇f(x, y) = (∂f/∂x, ∂f/∂y)

   = (2x, 2y).
2. Parameterize the level set f(x, y) = 1 by

   **r**(t) = (cos t, sin t).

   Then **r**′(t) = (−sin t, cos t), which is tangent to the circle.
3. Evaluate ∇f on the circle:

   At **r**(t), ∇f = (2cos t, 2sin t).
4. Check orthogonality using a dot product:

   ∇f · **r**′(t)

   = (2cos t, 2sin t) · (−sin t, cos t)

   = 2cos t(−sin t) + 2sin t(cos t)

   = −2sin t cos t + 2sin t cos t

   = 0.

**Insight:** For circles centered at the origin, ∇f points radially outward while tangents go around the circle. “Radial” and “tangent” directions are perpendicular—this is the level-set orthogonality principle in a familiar shape.

## Key Takeaways

- ✓

  ∇f(**x**) is the vector of partial derivatives: one component per input variable.
- ✓

  Directional derivatives satisfy D\_**u** f(**x**) = ∇f(**x**) · **u** for any unit direction **u**.
- ✓

  The steepest-ascent direction is ∇f/‖∇f‖ (when ∇f ≠ **0**), and the maximal increase rate is ‖∇f‖.
- ✓

  The first-order approximation is f(**x** + **h**) ≈ f(**x**) + ∇f(**x**) · **h** for small **h**.
- ✓

  ∇f is orthogonal to level sets f(**x**) = c (it is a normal vector to contours/surfaces).
- ✓

  If ∇f(**x**) = **0**, then all first-order directional changes vanish; this identifies critical points (not necessarily minima).
- ✓

  In optimization and ML, gradients drive iterative updates like **x** ← **x** − α∇f(**x**).

## Common Mistakes

- ✗

  Forgetting to evaluate the gradient at the point of interest (carrying around ∇f(x, y) but never plugging in (x₀, y₀)).
- ✗

  Using a non-unit direction in a directional derivative without accounting for its length (D\_**u** assumes ‖**u**‖ = 1 when interpreting “rate per unit distance”).
- ✗

  Confusing “orthogonal to level sets” with “points toward the origin” (true for x² + y² but not general).
- ✗

  Assuming ∇f = **0** implies a minimum; it could be a maximum or saddle without second-order analysis.

## Practice

easy

Let f(x, y) = 3x² − 2xy + y². Compute ∇f(x, y) and evaluate it at (1, 2).

**Hint:** Differentiate with respect to x holding y constant, then with respect to y holding x constant.

Show solution

∂f/∂x = 6x − 2y.

∂f/∂y = −2x + 2y.

So ∇f(x, y) = (6x − 2y, −2x + 2y).

At (1, 2): ∇f(1, 2) = (6·1 − 4, −2·1 + 4) = (2, 2).

medium

For f(x, y) = x² + 4y², find the unit direction **u** at (1, 1) that gives the fastest decrease, and compute the corresponding directional derivative value.

**Hint:** Fastest decrease is in direction −∇f/‖∇f‖. The minimum directional derivative over unit vectors equals −‖∇f‖.

Show solution

∇f(x, y) = (2x, 8y). So ∇f(1, 1) = (2, 8).

‖∇f(1,1)‖ = √(2² + 8²) = √(4 + 64) = √68 = 2√17.

Fastest decrease unit direction:

**u** = −(2, 8)/√68 = (−2/√68, −8/√68).

The corresponding directional derivative:

D\_**u** f = ∇f · **u** = −‖∇f‖ = −2√17.

medium

Let f(x, y) = x + y. Consider the level set f(x, y) = 5 (a line). Show that ∇f is orthogonal to this level set by computing a tangent direction and taking a dot product.

**Hint:** A level set x + y = 5 can be parameterized by (t, 5 − t).

Show solution

∇f(x, y) = (1, 1) everywhere.

Parameterize the level set: **r**(t) = (t, 5 − t).

Then **r**′(t) = (1, −1), which is tangent.

Dot product: ∇f · **r**′(t) = (1, 1) · (1, −1) = 1 − 1 = 0.

So ∇f is orthogonal to the level set.

## Connections

[Optimization Introduction](/tech-tree/optimization-intro/)

[Gradient Descent](/tech-tree/gradient-descent/)

[Convex Functions](/tech-tree/convexity/)

[Jacobian](/tech-tree/jacobian/)

[Matrix Calculus](/tech-tree/matrix-calculus/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
