---
title: Taylor Series
description: Infinite polynomial approximation of functions around a point.
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
permalink: /tech-tree/taylor-series/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Taylor Series

CalculusDifficulty: ★★★☆☆Depth: 4Unlocks: 0

Infinite polynomial approximation of functions around a point.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Power-series representation: a function expressed (when possible) as an infinite sum of powers about a point a, sum\_{n>=0} c\_n (x-a)^n
- -Derivative-based coefficients: the coefficient of (x-a)^n is given by the nth derivative at the center divided by n!, i.e. c\_n = f^{(n)}(a)/n!
- -Nth-degree Taylor polynomial: the finite truncation of the power series up to n gives the polynomial approximation of degree n
- -Radius of convergence: a (possibly zero or infinite) interval/region around a where the power series converges and may equal the function

## Key Symbols & Notation

Summation (sigma) notation for infinite series: "sum\_{n=0}^infty"

## Essential Relationships

- -Truncation/convergence link: the nth Taylor polynomial equals the truncated series using the derivative-based coefficients, and the remainder (f(x) minus that truncation) tends to zero on points where the full Taylor series converges to f

## Prerequisites (2)

[Derivative Rules5 atoms](/tech-tree/derivative-rules/)[Sequences5 atoms](/tech-tree/sequences/)

Advanced Learning Details

### Graph Position

44

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

4

Chain Length

### Cognitive Load

6

Atomic Elements

35

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (13)

- - Taylor series: representing a function as an infinite power series centered at a point a
- - Maclaurin series: Taylor series specialized to center a = 0
- - Taylor polynomial: the finite partial sum (degree-n polynomial) used as an approximation to the function
- - Power series: an infinite series of powers of (x - a) (family that includes Taylor series)
- - Center of expansion: the point a about which the series is formed
- - Remainder (error) term: the difference between the function and its Taylor polynomial
- - Lagrange form of the remainder (specific formula expressing an error using an (n+1)th derivative at some intermediate point)
- - Radius of convergence: the distance from the center within which the power series converges
- - Interval of convergence: the set of x values for which the series converges (including endpoint behavior)
- - Convergence vs. pointwise equality: distinction between a series converging and the series actually equaling the function
- - Analytic function: a function that equals its Taylor series on some neighbourhood of the center
- - Term-by-term differentiation and integration of power series (valid within radius of convergence)
- - Order of approximation: how the error scales with (x-a) and polynomial degree (e.g., next unused power determines leading error term)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Many functions are complicated globally but simple locally. Taylor series formalize that idea: near a point a, a smooth function behaves like a polynomial whose coefficients are determined entirely by derivatives at a.

TL;DR:

A Taylor series expresses (when possible) a function f(x) as an infinite power series around a center a: f(x) = ∑\_{n=0}^∞ f⁽ⁿ⁾(a)/n! · (x−a)ⁿ. Truncating after n terms gives the nth-degree Taylor polynomial, a practical approximation near a. The series may converge only within a radius of convergence R, and even where it converges it may or may not equal the original function—so you must check convergence and (when needed) remainder/error behavior.

## What Is Taylor Series?

### Why we want it (motivation)

Polynomials are the “friendly” functions of calculus:

- •They’re easy to differentiate and integrate.
- •They’re easy to compute numerically.
- •They behave predictably near a point.

But many important functions are *not* polynomials: eˣ, sin x, cos x, ln x, 1/(1−x), etc. Taylor series is the bridge: it turns a function (near some center a) into an infinite polynomial-like object.

The core idea is *local approximation*: if you zoom in near x = a, a smooth function looks more and more like its tangent line; if you zoom in further, a quadratic improves the fit; then a cubic, and so on.

### Definition (power-series representation)

A **power series about a** is an infinite sum

∑\_{n=0}^∞ cₙ (x−a)ⁿ.

A **Taylor series** is a particular power series for a function f whose coefficients are chosen to match derivatives of f at the center a:

f(x) = ∑\_{n=0}^∞ \[ f⁽ⁿ⁾(a) / n! \] (x−a)ⁿ.

The notation f⁽ⁿ⁾ means the nth derivative: f⁽⁰⁾ = f, f⁽¹⁾ = f′, f⁽²⁾ = f″, etc.

When a = 0, this special case is called a **Maclaurin series**:

f(x) = ∑\_{n=0}^∞ \[ f⁽ⁿ⁾(0) / n! \] xⁿ.

### The “matching derivatives” intuition

A polynomial of degree n can match up to n derivatives at a point. Taylor series pushes this to “match all derivatives,” term by term.

Consider a polynomial approximation Pₙ(x) of degree n around a:

Pₙ(x) = c₀ + c₁(x−a) + c₂(x−a)² + ⋯ + cₙ(x−a)ⁿ.

If we require that Pₙ and f have the same derivatives at a up to order n:

- •Pₙ(a) = f(a)
- •Pₙ′(a) = f′(a)
- •…
- •Pₙ⁽ⁿ⁾(a) = f⁽ⁿ⁾(a)

then the coefficients are forced to be

cₖ = f⁽ᵏ⁾(a)/k!.

This is the fundamental mechanism: **derivatives at the center determine the coefficients**.

### Important subtlety

A Taylor series can exist (all derivatives exist) but still:

1) converge only on a limited interval, and/or

2) converge but not equal the original function.

So the full story has two parts:

- •*Construct* the series from derivatives.
- •*Analyze* where it converges and whether it equals f.

## Core mechanic 1: Derivative-based coefficients and the nth-degree Taylor polynomial

### Why truncation matters

An infinite series is a theoretical object; in computation and estimation, we nearly always use a **finite truncation**.

The **nth-degree Taylor polynomial** of f about a is

Tₙ(x) = ∑\_{k=0}^n \[ f⁽ᵏ⁾(a) / k! \] (x−a)ᵏ.

This is the best polynomial of degree ≤ n that matches derivatives up to order n at x = a.

### How the coefficients appear (showing the mechanism)

Start with the general polynomial form around a:

Tₙ(x) = c₀ + c₁(x−a) + c₂(x−a)² + ⋯ + cₙ(x−a)ⁿ.

Differentiate term-by-term:

Tₙ′(x) = c₁ + 2c₂(x−a) + 3c₃(x−a)² + ⋯ + n cₙ(x−a)ⁿ⁻¹.

Evaluate at x = a (so every (x−a) term becomes 0):

Tₙ′(a) = c₁.

Differentiate again:

Tₙ″(x) = 2c₂ + 3·2 c₃(x−a) + 4·3 c₄(x−a)² + ⋯

Evaluate at x = a:

Tₙ″(a) = 2c₂ ⇒ c₂ = Tₙ″(a)/2!.

Continuing this pattern, the kth derivative at a isolates cₖ multiplied by k!:

Tₙ⁽ᵏ⁾(a) = k! cₖ ⇒ cₖ = Tₙ⁽ᵏ⁾(a)/k!.

If we impose Tₙ⁽ᵏ⁾(a) = f⁽ᵏ⁾(a) for k = 0,…,n, then

cₖ = f⁽ᵏ⁾(a)/k!.

This is where the factorial comes from: repeated differentiation pulls down k·(k−1)·…·1 = k!.

### A practical workflow

To build Tₙ(x) about a:

1) Compute f(a), f′(a), f″(a), …, f⁽ⁿ⁾(a).

2) Plug into

Tₙ(x) = f(a) + f′(a)(x−a) + f″(a)/2! (x−a)² + ⋯ + f⁽ⁿ⁾(a)/n! (x−a)ⁿ.

### Quick comparison table: “Taylor polynomial vs Taylor series”

| Object | Notation | What it is | Used for | Caveat |
| --- | --- | --- | --- | --- |
| Taylor polynomial | Tₙ(x) | Finite sum up to degree n | Approximate f near a | Has error (remainder) |
| Taylor series | ∑\_{n=0}^∞ … | Infinite sum | Exact representation when it converges to f | May converge only for | x−a | < R, may not equal f |

### The remainder (error) idea

Define the remainder after degree n as

Rₙ(x) = f(x) − Tₙ(x).

Taylor’s theorem (in one common form) says that if f has n+1 derivatives near a, then

Rₙ(x) = f⁽ⁿ⁺¹⁾(ξ) / (n+1)! · (x−a)ⁿ⁺¹

for some ξ between a and x.

Even if you don’t use this exact form yet, it communicates a key lesson:

- •The error typically scales like (x−a)ⁿ⁺¹.
- •Higher degree gives rapidly improved accuracy when |x−a| is small.

This explains why Taylor approximations are “local”: the small parameter is (x−a).

## Core mechanic 2: Radius of convergence and when the series equals the function

### Why convergence is the gatekeeper

A Taylor series is an infinite sum. Infinite sums are only meaningful if they converge.

For a power series

∑\_{n=0}^∞ cₙ (x−a)ⁿ,

typically there exists a number R (0 ≤ R ≤ ∞) called the **radius of convergence** such that:

- •The series converges for |x−a| < R.
- •The series diverges for |x−a| > R.
- •At |x−a| = R, convergence may or may not happen (must be checked separately).

So the “region where the series makes sense” is an interval (a−R, a+R) on the real line.

### How we often find R (ratio test intuition)

In many calculus settings, R is found via the ratio test. Consider terms

uₙ(x) = cₙ (x−a)ⁿ.

If

lim\_{n→∞} |uₙ₊₁(x) / uₙ(x)|

= lim\_{n→∞} |cₙ₊₁/cₙ| · |x−a|

= L · |x−a|,

then convergence typically requires L · |x−a| < 1, meaning |x−a| < 1/L. That value is R.

You don’t need every detail of series tests to use Taylor series effectively, but you *do* need the mindset:

- •A Taylor series is not automatically valid “for all x.”
- •Its validity is local to the center a and controlled by R.

### Converging vs representing the function

Even within |x−a| < R, the series sum might not equal f(x) unless f is “nice enough.”

A common sufficient condition (not the only one) is: if the remainder Rₙ(x) → 0 as n → ∞ for x in some interval, then

f(x) = lim\_{n→∞} Tₙ(x) = ∑\_{n=0}^∞ f⁽ⁿ⁾(a)/n! (x−a)ⁿ.

Many standard functions (eˣ, sin x, cos x, ln(1+x) on its interval, rational functions away from poles) behave well.

### Singularities and why they control R (big picture)

A powerful intuition: the radius of convergence is often limited by the nearest point where the function “breaks” (e.g., division by zero or non-analytic behavior).

Example intuition:

- •f(x) = 1/(1−x) centered at 0 has a problem at x = 1, so R = 1.
- •f(x) = 1/(1+x²) centered at 0 has complex singularities at x = ±i, distance 1 from 0 in the complex plane, so R = 1 (even though on the real line the function is perfectly finite everywhere).

You don’t have to master complex analysis here, but this perspective prevents surprises: **the convergence radius is about the function’s analytic obstacles, not just real-valued smoothness**.

### Endpoint checking (common pattern)

If R is finite, you must check x = a ± R separately. It’s common to see:

- •Converges on one endpoint but not the other.
- •Converges on both.
- •Converges on neither.

That endpoint behavior matters when using a series to represent a function on a closed interval.

## Application/Connection: Approximations, computation, and modeling

### Why Taylor series is a workhorse

Taylor series is not just a calculus curiosity. It’s a central tool for:

- •**Approximating** hard functions with polynomials.
- •**Estimating errors** and understanding sensitivity.
- •**Deriving algorithms** (numerical methods, scientific computing).
- •**Modeling** near an operating point (physics, engineering, economics).

### Local linearization and beyond

You may already know the tangent-line approximation:

f(x) ≈ f(a) + f′(a)(x−a).

That is exactly T₁(x). Taylor series generalizes this:

- •T₂ adds curvature (second derivative).
- •T₃ adds asymmetry/inflection behavior.
- •Higher orders capture more local geometry.

Even in multivariable calculus, a closely related idea appears (Taylor expansion with gradients and Hessians). You’ll later see vectors like **x** and **a**, and approximations using ∇f and the Hessian matrix. (In this lesson, we stay 1D, but the conceptual jump is small.)

### Typical “standard expansions” you reuse constantly

Certain Maclaurin series appear everywhere:

1) Exponential:

eˣ = ∑\_{n=0}^∞ xⁿ/n! = 1 + x + x²/2! + x³/3! + ⋯

2) Sine and cosine:

sin x = ∑\_{n=0}^∞ (−1)ⁿ x²ⁿ⁺¹/(2n+1)!

cos x = ∑\_{n=0}^∞ (−1)ⁿ x²ⁿ/(2n)!

3) Geometric series (a gateway to many others):

1/(1−x) = ∑\_{n=0}^∞ xⁿ for |x| < 1.

From (3), many manipulations become possible: integrate term-by-term, differentiate term-by-term, substitute x → −x, etc.

### Numerical computation mindset

Suppose you need sin(0.1). A calculator uses algorithms that reduce to polynomial-like approximations internally.

Using Taylor:

sin x ≈ x − x³/3! + x⁵/5!.

At x = 0.1, higher powers shrink rapidly:

- •0.1³ = 0.001
- •0.1⁵ = 0.00001

So a few terms give high accuracy.

### Modeling: choosing the center a

The center a is not arbitrary—it’s a design decision.

- •If you care about accuracy near x = 2, expand around a = 2.
- •If you care near 0, use Maclaurin.

A good mental model:

- •Taylor polynomial is like a *custom-fit* polynomial built for a neighborhood around a.

### Connection to differential equations and optimization

Later you’ll see:

- •Solving ODEs via power series (assume y = ∑ cₙ(x−a)ⁿ and solve for coefficients).
- •Newton’s method analysis uses Taylor expansion of f near a root.
- •Optimization uses second-order Taylor (quadratic models) to approximate objectives.

Taylor series is one of the main reasons derivatives are so valuable: derivatives are not just slopes—they are **information that determines local function behavior to arbitrary order**.

## Worked Examples (3)

### Build a Taylor polynomial for eˣ around a = 0 (Maclaurin) and approximate e^0.2

We want T₄(x) for f(x) = eˣ at a = 0, then use it to approximate e^0.2.

1. Compute derivatives:

   f(x) = eˣ

   f′(x) = eˣ

   f″(x) = eˣ

   f‴(x) = eˣ

   f⁽⁴⁾(x) = eˣ
2. Evaluate at a = 0:

   f(0) = 1

   f′(0) = 1

   f″(0) = 1

   f‴(0) = 1

   f⁽⁴⁾(0) = 1
3. Form the Taylor polynomial:

   T₄(x) = ∑\_{k=0}^4 f⁽ᵏ⁾(0)/k! · xᵏ

   = 1 + x + x²/2! + x³/3! + x⁴/4!
4. Plug in x = 0.2:

   T₄(0.2) = 1 + 0.2 + 0.2²/2 + 0.2³/6 + 0.2⁴/24

   = 1 + 0.2 + 0.04/2 + 0.008/6 + 0.0016/24

   = 1 + 0.2 + 0.02 + 0.001333… + 0.0000666…

   ≈ 1.2214666…
5. Compare intuition:

   The true value is e^0.2 ≈ 1.221402…

   The approximation is already accurate to about 4 decimal places with only 5 terms.

**Insight:** Because eˣ has derivatives that stay the same and factorials grow fast, the terms xⁿ/n! shrink quickly for modest |x|. That’s why truncations of eˣ are especially effective.

### Derive the Maclaurin series for sin x and build a 5th-degree approximation

We will compute derivatives of sin x at 0, identify the pattern, then write T₅(x) and use it as an approximation near 0.

1. Start with f(x) = sin x and compute derivatives:

   f(x) = sin x

   f′(x) = cos x

   f″(x) = −sin x

   f‴(x) = −cos x

   f⁽⁴⁾(x) = sin x

   f⁽⁵⁾(x) = cos x
2. Evaluate at 0:

   f(0) = sin 0 = 0

   f′(0) = cos 0 = 1

   f″(0) = −sin 0 = 0

   f‴(0) = −cos 0 = −1

   f⁽⁴⁾(0) = sin 0 = 0

   f⁽⁵⁾(0) = cos 0 = 1
3. Write the Taylor polynomial through degree 5:

   T₅(x) = f(0) + f′(0)x + f″(0)/2! x² + f‴(0)/3! x³ + f⁽⁴⁾(0)/4! x⁴ + f⁽⁵⁾(0)/5! x⁵
4. Substitute the values:

   T₅(x) = 0 + 1·x + 0·x² + (−1)/3! x³ + 0·x⁴ + 1/5! x⁵

   = x − x³/6 + x⁵/120
5. Interpretation near 0:

   sin x ≈ x − x³/6 + x⁵/120

   The approximation improves as x gets closer to 0 because higher powers shrink fast.

**Insight:** Only odd powers appear because sin x is an odd function, and the derivatives at 0 alternate between 0, ±1. Symmetry of the function shows up directly in which Taylor coefficients vanish.

### Find the radius of convergence for the series of 1/(1−x) and connect it to the function’s singularity

Consider the geometric series ∑\_{n=0}^∞ xⁿ. We’ll see when it converges and why it equals 1/(1−x) there.

1. Consider partial sums S\_N = 1 + x + x² + ⋯ + xᴺ.
2. Multiply by (1−x):

   (1−x)S\_N = S\_N − xS\_N

   = (1 + x + x² + ⋯ + xᴺ) − (x + x² + ⋯ + xᴺ + xᴺ⁺¹)

   = 1 − xᴺ⁺¹.
3. So for x ≠ 1:

   S\_N = (1 − xᴺ⁺¹)/(1−x).
4. Now take N → ∞. If |x| < 1 then xᴺ⁺¹ → 0, so

   lim\_{N→∞} S\_N = 1/(1−x).
5. If |x| > 1 then xᴺ⁺¹ does not go to 0, so the series diverges.
6. At |x| = 1, check endpoints:

   x = 1 gives 1 + 1 + 1 + ⋯ diverges.

   x = −1 gives 1 − 1 + 1 − 1 + ⋯ does not converge in the usual sense.
7. Therefore the radius of convergence is R = 1, and the series equals 1/(1−x) for |x| < 1.

**Insight:** The function 1/(1−x) has a singularity (division by zero) at x = 1, exactly one unit away from the center 0. That nearest breakdown point matches the radius of convergence R = 1.

## Key Takeaways

- ✓

  A Taylor series is a power series centered at a: f(x) = ∑\_{n=0}^∞ f⁽ⁿ⁾(a)/n! · (x−a)ⁿ (when it converges to f).
- ✓

  The nth-degree Taylor polynomial Tₙ(x) is the truncation up to n; it matches f and its first n derivatives at x = a.
- ✓

  Factorials arise because the kth derivative of (x−a)ᵏ at a equals k!; this forces the coefficient cₖ = f⁽ᵏ⁾(a)/k!.
- ✓

  Taylor approximations are local: accuracy is typically good when |x−a| is small, and improves with higher degree.
- ✓

  Power series have a radius of convergence R: they converge for |x−a| < R and diverge for |x−a| > R; endpoints require separate checks.
- ✓

  Convergence of the Taylor series is not the same as equality to f; to claim representation, you need the remainder Rₙ(x) → 0 (or other analytic guarantees).
- ✓

  Standard expansions (eˣ, sin x, cos x, 1/(1−x), ln(1+x)) are reusable building blocks across calculus and applied math.

## Common Mistakes

- ✗

  Assuming the Taylor series equals the function for all x without checking the radius of convergence (and endpoints).
- ✗

  Forgetting the center a and incorrectly writing powers of x instead of (x−a) when expanding around a ≠ 0.
- ✗

  Dropping the factorial: coefficients are f⁽ⁿ⁾(a)/n!, not just f⁽ⁿ⁾(a).
- ✗

  Using a low-degree polynomial far from a and expecting good accuracy (Taylor is local, not global).

## Practice

medium

Compute the 3rd-degree Taylor polynomial T₃(x) for f(x) = ln(1+x) centered at a = 0.

**Hint:** Differentiate ln(1+x) repeatedly and evaluate at x = 0. Watch the alternating signs and factorials.

Show solution

f(x) = ln(1+x)

Derivatives:

f′(x) = 1/(1+x)

f″(x) = −1/(1+x)²

f‴(x) = 2/(1+x)³

Evaluate at 0:

f(0) = 0

f′(0) = 1

f″(0) = −1

f‴(0) = 2

Taylor polynomial:

T₃(x) = f(0) + f′(0)x + f″(0)/2! x² + f‴(0)/3! x³

= 0 + x + (−1)/2 x² + 2/6 x³

= x − x²/2 + x³/3.

medium

Find the radius of convergence of the power series ∑\_{n=1}^∞ n(x−2)ⁿ.

**Hint:** Use the ratio test on uₙ = n(x−2)ⁿ. Simplify |uₙ₊₁/uₙ|.

Show solution

Let uₙ = n(x−2)ⁿ.

Compute the ratio:

= |(n+1)/n| · |x−2|

= (1 + 1/n) |x−2|.

Take n → ∞:

lim\_{n→∞} |uₙ₊₁/uₙ| = 1 · |x−2| = |x−2|.

Ratio test gives convergence when |x−2| < 1.

So the radius of convergence is R = 1 (center a = 2).

easy

Use the Maclaurin polynomial for sin x up to x⁵ to approximate sin(0.3). Give the numerical value of x − x³/6 + x⁵/120 at x = 0.3.

**Hint:** Compute 0.3³ and 0.3⁵, then apply the coefficients 1/6 and 1/120.

Show solution

Use T₅(x) = x − x³/6 + x⁵/120.

At x = 0.3:

0.3³ = 0.027

0.3⁵ = 0.3²·0.3³ = 0.09·0.027 = 0.00243

Compute:

T₅(0.3) = 0.3 − 0.027/6 + 0.00243/120

= 0.3 − 0.0045 + 0.00002025

= 0.29552025.

So sin(0.3) ≈ 0.29552025 using the 5th-degree Maclaurin approximation.

## Connections

[Power Series Basics](/tech-tree/power-series-basics/)

[Convergence Tests](/tech-tree/convergence-tests/)

[Maclaurin Series (Taylor at 0)](/tech-tree/maclaurin-series/)

[Newton’s Method](/tech-tree/newtons-method/)

[Multivariable Taylor Approximation](/tech-tree/multivariable-taylor/)

[Error Bounds and Taylor’s Theorem](/tech-tree/taylor-remainder/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
