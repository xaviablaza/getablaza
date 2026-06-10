---
title: Multivariable Calculus
description: Functions of multiple variables. Partial derivatives.
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
permalink: /tech-tree/multivariable-calculus/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Multivariable Calculus

CalculusDifficulty: ★★★☆☆Depth: 4Unlocks: 75

Functions of multiple variables. Partial derivatives.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Multivariable function: a rule f that assigns outputs from inputs with multiple coordinates (f(x1,...,xn))
- -Partial derivative: instantaneous rate of change of f with respect to one coordinate while holding the others fixed
- -Gradient: the vector of all partial derivatives, giving the best linear approximation to change

## Key Symbols & Notation

partial derivative operator written as 'partial/partial x' (denotes differentiation with respect to one variable)

## Essential Relationships

- -Partial derivative = limit of the difference quotient with other variables held fixed
- -Gradient = vector of partial derivatives; first-order change ≈ gradient dot displacement

## Prerequisites (2)

[Derivative Rules5 atoms](/tech-tree/derivative-rules/)[Vectors Introduction6 atoms](/tech-tree/vectors-intro/)

## Unlocks (3)

[Gradientslvl 3](/tech-tree/gradients/)[Joint Distributionslvl 3](/tech-tree/joint-distributions/)[Multiple Integralslvl 3](/tech-tree/multiple-integrals/)

Advanced Learning Details

### Graph Position

45

Depth Cost

75

Fan-Out (ROI)

27

Bottleneck Score

4

Chain Length

### Cognitive Load

6

Atomic Elements

52

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (22)

- - Function of several variables: f(x,y,...) as a mapping from R^n to R (or to R^m)
- - Domain and range in the multivariable context (subsets of R^n and R or R^m)
- - Point in R^n represented as an ordered tuple (x,y,...)
- - Graph of a function of two variables as a surface in R^3
- - Level sets / level curves / contours: sets where f(x,y,...) = c
- - Contour (topographic) maps as 2-D representations of level sets
- - Limit of a multivariable function: (x,y,...) -> (a,b,...) and path dependence
- - Continuity for multivariable functions
- - Partial derivative: derivative with respect to one variable while holding others fixed
- - Partial derivative as slope of tangent to a coordinate cross-section (slice)
- - Higher-order partial derivatives (second partials, etc.)
- - Mixed partial derivatives (e.g., ∂^2 f / ∂x ∂y)
- - Gradient vector (vector of first partial derivatives)
- - Directional derivative: rate of change of f in an arbitrary direction
- - Tangent plane to a surface and linear approximation (linearization) of f
- - Differentiability in the multivariable sense (existence of a linear best approximation)
- - Total derivative / Jacobian as the linear map (matrix) approximating the change in f
- - Chain rule for compositions involving multivariable functions
- - Hessian matrix: matrix of second partial derivatives
- - Critical points for multivariable functions (where gradient = 0)
- - Classification of critical points using second-derivative information (Hessian/eigenvalues or principal minors)
- - Existence-of-partials vs differentiability: partial derivatives can exist without the function being differentiable

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Most real systems don’t depend on just one knob. Temperature depends on latitude and altitude. Profit depends on price and demand. Loss in machine learning depends on thousands of parameters. Multivariable calculus is the language for “how does the output change when I change one coordinate, or many at once?”

TL;DR:

A multivariable function f(x, y, …) maps coordinate inputs to an output. A partial derivative ∂f/∂x measures how f changes as x changes while other variables are held fixed. Collecting all partial derivatives gives the gradient ∇f, a vector pointing in the direction of steepest increase and providing the best linear (first-order) approximation: f(**x** + **h**) ≈ f(**x**) + ∇f(**x**) · **h**.

## What Is Multivariable Calculus?

### Why you should care (before definitions)

Single-variable calculus answers: “If I nudge x, how does f(x) change?”

But many quantities depend on multiple inputs:

- •f(x, y) = height of terrain at (x, y)
- •f(x, y, z) = temperature at a point in space
- •L(w₁, …, wₙ) = loss of a model with parameters w₁…wₙ

Multivariable calculus generalizes *rate of change* and *local approximation* to these settings.

### Multivariable functions

A **multivariable function** takes several coordinates as input and returns a value.

- •Two variables: f(x, y)
- •n variables: f(x₁, x₂, …, xₙ)

A convenient way to package inputs is as a vector:

- •**x** = (x₁, …, xₙ)
- •Then f(**x**) means the same as f(x₁, …, xₙ)

### Geometric intuition

For f(x, y):

- •The input (x, y) lives in the plane.
- •The output f(x, y) is a height.
- •So you can imagine a surface z = f(x, y) floating over the xy-plane.

For f(x₁, …, xₙ) with large n, you can’t visualize the surface, but the *local rules* (derivatives, linear approximations) still work.

### The big three ideas in this node

1. 1)**Partial derivatives**: change with respect to one coordinate while holding others fixed.
2. 2)**Gradient** ∇f: the vector of all partial derivatives.
3. 3)**Linearization**: use ∇f to approximate small changes in f using a dot product.

These three together are the backbone of optimization, physics, and machine learning.

## Core Mechanic 1: Partial Derivatives (One Coordinate at a Time)

### Why partial derivatives exist

If f depends on x and y, you might ask two different questions:

- •“What happens if I increase x but keep y the same?”
- •“What happens if I increase y but keep x the same?”

Those are different nudges, so they generally produce different rates of change.

### Definition (using the limit)

For f(x, y), the partial derivative with respect to x is

∂f/∂x(x, y) = limₕ→0 [f(x + h, y) − f(x, y)] / h

Similarly,

∂f/∂y(x, y) = limₕ→0 [f(x, y + h) − f(x, y)] / h

The key phrase: **hold the other variables fixed**.

### “Treat the others as constants” rule

In practice, to compute ∂f/∂x:

- •Differentiate as if y (and other variables) are constants.

This works because the limit definition is literally examining motion along the x-direction line.

### Geometric picture: slices

For f(x, y), fix y = y₀. Then you get a single-variable function

g(x) = f(x, y₀)

Then

∂f/∂x(x₀, y₀) = g′(x₀)

So a partial derivative is the slope of a **cross-section** of the surface.

### Notation you’ll see

| Meaning | Common notations |
| --- | --- |
| partial derivative w.r.t. x | ∂f/∂x, fₓ |
| second partial w.r.t. x twice | ∂²f/∂x², fₓₓ |
| mixed partial (x then y) | ∂²f/∂y∂x, fₓᵧ |

### Second partials and mixed partials

Once you have ∂f/∂x (a new function of x and y), you can differentiate again.

Example structure:

- •First partial: fₓ(x, y) = ∂f/∂x
- •Second partial: fₓₓ(x, y) = ∂/∂x (fₓ)
- •Mixed partial: fₓᵧ(x, y) = ∂/∂y (fₓ)

For “nice” functions (continuous second partials), the order of mixed partials doesn’t matter:

fₓᵧ = fᵧₓ

This is often called **Clairaut’s theorem** (or Schwarz’s theorem). You don’t need the full theorem proof here—just remember: if the function is smooth enough, mixed partials match.

### Mini-derivation: partial derivative of a polynomial

Let f(x, y) = x²y + 3y.

Compute ∂f/∂x:

- •Treat y as constant.

∂/∂x (x²y) = y · ∂/∂x (x²) = y · 2x = 2xy

∂/∂x (3y) = 0

So

∂f/∂x = 2xy

Compute ∂f/∂y:

∂/∂y (x²y) = x²

∂/∂y (3y) = 3

So

∂f/∂y = x² + 3

### Core intuition checkpoint

A partial derivative is not “the derivative” of f.

It’s **a directional rate of change along a coordinate axis**.

Later, the gradient will combine these coordinate rates into one object that can predict changes in *any* direction.

## Core Mechanic 2: The Gradient and Linear Approximation

### Why the gradient matters

Partial derivatives answer axis-aligned questions: “change x” or “change y.”

But often you change multiple coordinates at once:

- •Walk northeast: x and y both increase.
- •Update model parameters: all weights move together.

You want a single object that:

1. 1)Collects all partial derivatives.
2. 2)Predicts the change in f for a small step in any direction.

That object is the **gradient**.

### Definition

For f(x₁, …, xₙ), define

∇f(**x**) = (∂f/∂x₁, ∂f/∂x₂, …, ∂f/∂xₙ)

For two variables:

∇f(x, y) = (fₓ(x, y), fᵧ(x, y))

Remember the lesson’s vector convention: gradients are vectors, so we’ll treat them as vectors even though we often write them as coordinate tuples.

### Why ∇f predicts change: linearization

Suppose you are at a point **x** and take a small step **h**.

You want to approximate

f(**x** + **h**) − f(**x**)

In single-variable calculus:

f(x + h) ≈ f(x) + f′(x)h

Multivariable calculus generalizes this via the dot product:

f(**x** + **h**) ≈ f(**x**) + ∇f(**x**) · **h**

This is the **first-order Taylor approximation** (also called the **linearization**).

### Show the structure in 2D

Let **h** = (h₁, h₂). Then

∇f(x, y) · **h** = (fₓ, fᵧ) · (h₁, h₂)

Compute the dot product:

∇f(x, y) · **h**

= fₓ(x, y)h₁ + fᵧ(x, y)h₂

So the approximation is:

f(x + h₁, y + h₂) ≈ f(x, y) + fₓ(x, y)h₁ + fᵧ(x, y)h₂

This is incredibly practical: it tells you how much each coordinate’s small change contributes to the total change.

### Directional derivatives: change along a direction

If you move specifically along a direction **u** (a unit vector, ‖**u**‖ = 1) by a small distance t, your step is **h** = t**u**.

Plug into linearization:

f(**x** + t**u**) − f(**x**) ≈ ∇f(**x**) · (t**u**) = t(∇f(**x**) · **u**)

So the instantaneous rate of change in direction **u** is:

D\_**u** f(**x**) = ∇f(**x**) · **u**

This formula explains two famous facts:

1) **Steepest ascent direction**

Because ∇f(**x**) · **u** = ‖∇f(**x**)‖‖**u**‖cosθ and ‖**u**‖ = 1,

D\_**u** f(**x**) = ‖∇f(**x**)‖cosθ

This is maximized when cosθ = 1 ⇒ θ = 0, i.e., **u** points in the same direction as ∇f.

So ∇f points toward the direction of steepest increase.

2) **Maximum slope value**

The maximum directional derivative equals ‖∇f(**x**)‖.

### Level sets and perpendicularity (2D intuition)

A **level set** is the set of points where f(x, y) is constant, like f(x, y) = c.

These are contour lines on a map.

Moving along a level set doesn’t change f, so the directional derivative tangent to the level set is 0.

If **t** is a tangent direction to the level set at a point, then

0 = D\_**t** f = ∇f · **t**

A dot product of zero means perpendicular, so:

∇f is perpendicular to the level set.

This is why gradients are drawn as arrows crossing contour lines at right angles.

### Summary table: partial derivatives vs gradient

| Object | What it measures | Shape | Typical use |
| --- | --- | --- | --- |
| ∂f/∂xᵢ | change along coordinate axis xᵢ | scalar-valued function | sensitivity to one feature/parameter |
| ∇f | best local linear change in any direction | vector-valued function | optimization, steepest ascent/descent, linearization |

This sets up the next nodes: [Gradients](/tech-tree/gradients/) and optimization methods that use them.

## Application/Connection: Sensitivity, Optimization, and Modeling

### Why these tools show up everywhere

Multivariable calculus becomes essential when:

- •A system depends on multiple inputs.
- •You need to understand sensitivity: “which input matters most?”
- •You want to optimize: “how do I change inputs to increase/decrease output?”

### Sensitivity analysis

Suppose f(x, y) measures cost, with x = labor hours and y = material used.

- •∂f/∂x tells you marginal cost per extra labor hour (holding materials fixed).
- •∂f/∂y tells you marginal cost per extra unit material (holding labor fixed).

The gradient combines this into “cost increases fastest if you increase inputs in the gradient direction.”

### Optimization preview (without full algorithms)

If you want to minimize f, a common idea is to step opposite the gradient:

**x**\_{new} = **x**\_{old} − α∇f(**x**\_{old})

where α > 0 is a step size.

You don’t need to master gradient descent here, but notice the logic from linearization:

- •For small **h**, change in f is ≈ ∇f · **h**.
- •To make f decrease, you want ∇f · **h** < 0.
- •Choosing **h** = −α∇f makes ∇f · **h** = −α‖∇f‖² ≤ 0.

That’s a clean “why” grounded in the dot product.

### Connection to joint distributions (probability)

In probability, you often work with functions of multiple random variables:

- •joint density p(x, y)
- •log-likelihood ℓ(θ₁, …, θₙ)

Partial derivatives and gradients measure how sensitive the log-likelihood is to each parameter. This is foundational for estimation and learning.

See: [Joint Distributions](/tech-tree/joint-distributions/)

### Connection to multiple integrals

Derivatives tell you local change; integrals accumulate quantities over regions.

Once you can describe functions f(x, y, z) and their rates of change, the next step is computing totals:

- •area under a surface (double integrals)
- •mass of a 3D object with density ρ(x, y, z) (triple integrals)

See: [Multiple Integrals](/tech-tree/multiple-integrals/)

### A practical mental model to keep

- •Partial derivatives: “If I freeze everything except one coordinate, what’s the slope?”
- •Gradient: “If I move a tiny bit in *any* direction, how does f change?”
- •Linearization: “Near this point, f behaves like a plane (or hyperplane).”

If you can do those three reliably, you’re ready for deeper gradient-based methods and higher-dimensional modeling.

## Worked Examples (3)

### Compute partial derivatives and evaluate them at a point

Let f(x, y) = x²y + 3x − 4y². Find fₓ and fᵧ, then evaluate at (x, y) = (2, −1).

1. Differentiate with respect to x (treat y as constant):

   f(x, y) = x²y + 3x − 4y²

   ∂/∂x (x²y) = y · ∂/∂x (x²) = y · 2x = 2xy

   ∂/∂x (3x) = 3

   ∂/∂x (−4y²) = 0

   So:

   fₓ(x, y) = 2xy + 3
2. Differentiate with respect to y (treat x as constant):

   ∂/∂y (x²y) = x²

   ∂/∂y (3x) = 0

   ∂/∂y (−4y²) = −8y

   So:

   fᵧ(x, y) = x² − 8y
3. Evaluate at (2, −1):

   fₓ(2, −1) = 2·2·(−1) + 3 = −4 + 3 = −1

   fᵧ(2, −1) = (2)² − 8(−1) = 4 + 8 = 12

**Insight:** At (2, −1), increasing x slightly decreases f (since fₓ = −1), while increasing y slightly increases f strongly (since fᵧ = 12). Partial derivatives are local sensitivity numbers.

### Use the gradient to make a linear prediction of change

Let f(x, y) = x² + 2y². Approximate the change in f when moving from (1, 1) to (1.02, 0.97).

1. Compute the gradient:

   fₓ(x, y) = ∂/∂x (x² + 2y²) = 2x

   fᵧ(x, y) = ∂/∂y (x² + 2y²) = 4y

   So:

   ∇f(x, y) = (2x, 4y)
2. Evaluate at the base point (1, 1):

   ∇f(1, 1) = (2, 4)
3. Compute the step **h** from (1, 1) to (1.02, 0.97):

   **h** = (Δx, Δy) = (1.02 − 1, 0.97 − 1) = (0.02, −0.03)
4. Use linearization:

   Δf ≈ ∇f(1, 1) · **h**

   = (2, 4) · (0.02, −0.03)

   = 2(0.02) + 4(−0.03)

   = 0.04 − 0.12

   = −0.08
5. Optional check with exact values (to see approximation quality):

   f(1, 1) = 1² + 2·1² = 3

   f(1.02, 0.97) = (1.02)² + 2(0.97)²

   = 1.0404 + 2(0.9409)

   = 1.0404 + 1.8818

   = 2.9222

   Exact Δf = 2.9222 − 3 = −0.0778, close to −0.08

**Insight:** The gradient turns a small multivariable change into a dot product. It’s the multivariable version of “Δf ≈ f′Δx”.

### Directional derivative from the gradient (steepness along a chosen direction)

Let f(x, y) = 3x + 4y. Find the directional derivative at (0, 0) in the direction **u** = (3/5, 4/5).

1. Compute the gradient:

   fₓ = 3

   fᵧ = 4

   So:

   ∇f(x, y) = (3, 4)

   In particular, ∇f(0, 0) = (3, 4).
2. Use the directional derivative formula:

   D\_**u** f(0, 0) = ∇f(0, 0) · **u**

   = (3, 4) · (3/5, 4/5)

   = 3(3/5) + 4(4/5)

   = 9/5 + 16/5

   = 25/5

   = 5
3. Interpretation:

   Since ‖**u**‖ = 1, this value is the slope per unit distance traveled in that direction.

**Insight:** Because **u** points in the same direction as ∇f (both align with (3,4)), the directional derivative equals ‖∇f‖ = √(3² + 4²) = 5, the maximum possible.

## Key Takeaways

- ✓

  A multivariable function f(x₁, …, xₙ) maps an input vector **x** to an output; in 2D you can picture a surface z = f(x, y).
- ✓

  A partial derivative ∂f/∂xᵢ measures the instantaneous rate of change in the xᵢ direction while holding all other variables fixed.
- ✓

  To compute ∂f/∂x, you can usually “treat y, z, … as constants” and use familiar single-variable rules.
- ✓

  Second partial derivatives include fₓₓ, fᵧᵧ, and mixed partials fₓᵧ; for sufficiently smooth functions, fₓᵧ = fᵧₓ.
- ✓

  The gradient ∇f is the vector of all partial derivatives: ∇f = (∂f/∂x₁, …, ∂f/∂xₙ).
- ✓

  Linearization: for small steps **h**, f(**x** + **h**) ≈ f(**x**) + ∇f(**x**) · **h**.
- ✓

  Directional derivatives are dot products: D\_**u** f = ∇f · **u**, and ∇f points in the direction of steepest ascent with magnitude ‖∇f‖.
- ✓

  These ideas power sensitivity analysis and are prerequisites for gradients in optimization, joint probability models, and multiple integrals.

## Common Mistakes

- ✗

  Forgetting to hold other variables constant when taking a partial derivative (e.g., differentiating y with respect to x).
- ✗

  Mixing up ∇f (a vector) with ‖∇f‖ (a scalar magnitude) or with a directional derivative (a scalar along a chosen direction).
- ✗

  Using a direction vector **u** that is not a unit vector in a directional derivative; D\_**u** f = ∇f · **u** assumes ‖**u**‖ = 1 for “per unit distance” interpretation.
- ✗

  Applying linearization for large steps; the approximation f(**x** + **h**) ≈ f(**x**) + ∇f · **h** is only reliable when **h** is small.

## Practice

easy

Let f(x, y) = x³ − 2xy + y². Compute fₓ and fᵧ.

**Hint:** Differentiate term-by-term; when computing fₓ treat y as constant, and for fᵧ treat x as constant.

Show solution

Compute fₓ:

∂/∂x (x³) = 3x²

∂/∂x (−2xy) = −2y

∂/∂x (y²) = 0

So fₓ(x, y) = 3x² − 2y.

Compute fᵧ:

∂/∂y (x³) = 0

∂/∂y (−2xy) = −2x

∂/∂y (y²) = 2y

So fᵧ(x, y) = −2x + 2y.

medium

Let f(x, y) = e^{xy}. Find ∇f(x, y) and evaluate it at (1, 2).

**Hint:** Use the chain rule: if f = e^{g}, then ∂f/∂x = e^{g} · ∂g/∂x.

Show solution

Let g(x, y) = xy, so f = e^{g}.

Compute partials:

fₓ = e^{xy} · ∂/∂x(xy) = e^{xy} · y

fᵧ = e^{xy} · ∂/∂y(xy) = e^{xy} · x

Thus:

∇f(x, y) = (y e^{xy}, x e^{xy}).

At (1, 2):

∇f(1, 2) = (2e^{2}, 1·e^{2}) = (2e², e²).

hard

Approximate f(2.01, 0.98) for f(x, y) = x² + y³ using linearization around (2, 1).

**Hint:** Compute ∇f(2, 1). Use **h** = (0.01, −0.02). Then f(2,1) + ∇f(2,1) · **h**.

Show solution

Compute f and gradient:

f(x, y) = x² + y³

fₓ = 2x

fᵧ = 3y²

Evaluate at (2, 1):

f(2, 1) = 2² + 1³ = 4 + 1 = 5

∇f(2, 1) = (2·2, 3·1²) = (4, 3)

Step **h** from (2,1) to (2.01,0.98):

**h** = (0.01, −0.02)

Linearization:

f(2.01, 0.98) ≈ f(2, 1) + ∇f(2, 1) · **h**

= 5 + (4, 3) · (0.01, −0.02)

= 5 + [4(0.01) + 3(−0.02)]

= 5 + (0.04 − 0.06)

= 5 − 0.02

= 4.98

## Connections

Next steps in the tech tree:

- •[Gradients](/tech-tree/gradients/): Deepen geometric meaning (steepest ascent), directional derivatives, and optimization connections.
- •[Joint Distributions](/tech-tree/joint-distributions/): Multivariable functions as probability densities and log-likelihoods; partial derivatives for parameter sensitivity.
- •[Multiple Integrals](/tech-tree/multiple-integrals/): Accumulating f(x, y, …) over regions; the integral-side counterpart to partial derivatives.

Quality: A (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
