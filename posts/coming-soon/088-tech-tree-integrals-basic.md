---
title: Integrals
description: Area under a curve. Antiderivatives and Riemann sums.
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
permalink: /tech-tree/integrals-basic/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Integrals

CalculusDifficulty: ★★☆☆☆Depth: 3Unlocks: 7

Area under a curve. Antiderivatives and Riemann sums.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Definite integral as the limit of Riemann sums (precise accumulation/limit definition)
- -Indefinite integral as an antiderivative (a family of functions differing by a constant)
- -Fundamental Theorem of Calculus linking antiderivatives and definite integrals

## Key Symbols & Notation

Definite integral notation: "∫\_a^b f(x) dx"Differential symbol: "dx" (the integration variable/infinitesimal width)

## Essential Relationships

- -Fundamental Theorem: ∫\_a^b f(x) dx = F(b) - F(a) where F'(x) = f(x)

## Prerequisites (1)

[Derivatives6 atoms](/tech-tree/derivatives-basic/)

## Unlocks (5)

[Consumer Surpluslvl 3](/tech-tree/consumer-surplus/)[Fundamental Theorem of Calculuslvl 2](/tech-tree/fundamental-theorem/)[Multiple Integralslvl 3](/tech-tree/multiple-integrals/)[Measure Theorylvl 5](/tech-tree/measure-theory/)[Stochastic Processeslvl 4](/tech-tree/stochastic-processes/)

Advanced Learning Details

### Graph Position

34

Depth Cost

7

Fan-Out (ROI)

5

Bottleneck Score

3

Chain Length

### Cognitive Load

6

Atomic Elements

33

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (15)

- - Definite integral as the net (signed) area under a curve between x = a and x = b
- - Indefinite integral as the family of antiderivatives of a function
- - Antiderivative: a function F whose derivative F' equals the integrand f
- - Riemann sum: approximation of area by summing areas of rectangles over a partition
- - Partition of an interval and subinterval width (Δx) as basis for Riemann sums
- - Sample point (x\_i\*): the chosen x-value in each subinterval whose function value gives rectangle height
- - Limit of Riemann sums (as number of subintervals increases) giving the exact definite integral
- - Evaluation theorem (FTC part 2): computing a definite integral by evaluating an antiderivative at the endpoints
- - Accumulation function A(x)=∫\_a^x f(t) dt and its interpretation as accumulated quantity
- - Fundamental connection (FTC part 1): the derivative of the accumulation function equals the integrand
- - Constant of integration (C) and its role in the indefinite integral
- - Linearity of the integral (constants pull out; sums split)
- - Additivity of integrals over adjacent intervals (splitting intervals)
- - Sign rule for bounds: reversing integration limits changes the sign of the integral
- - Signed vs absolute area distinction (integral gives net signed area; absolute area requires |f|)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Derivatives tell you how something changes at an instant. Integrals tell you what those tiny changes add up to over time or over a range. If derivatives are “speed right now,” integrals are “distance traveled.”

TL;DR:

A **definite integral** ∫ₐᵇ f(x) dx is the limit of Riemann sums and measures net accumulation (often area). An **indefinite integral** ∫ f(x) dx is an antiderivative F(x) + C. The **Fundamental Theorem of Calculus** links them: if F′(x) = f(x), then ∫ₐᵇ f(x) dx = F(b) − F(a).

## What Is an Integral?

### Why integrals exist (motivation)

Derivatives answer questions like:

- •“How fast is a quantity changing at x?”
- •“What is the slope of the curve y = f(x) right here?”

But many real questions are *about accumulation*:

- •If you know velocity v(t), how far did you travel from t = a to t = b?
- •If you know a rate r(x) (cost per unit, density per meter, probability density), what is the *total* over an interval?

These questions all share the same pattern:

1. 1)Break the interval into tiny pieces.
2. 2)Approximate the contribution on each piece.
3. 3)Add them up.
4. 4)Take a limit as the pieces become infinitely fine.

That “add up tiny contributions and take a limit” is the central idea of integration.

### Two integrals that are related but distinct

There are two closely related notions:

1) **Definite integral** (a number):

- •Notation: ∫ₐᵇ f(x) dx
- •Output: a single value (net accumulation from a to b)

2) **Indefinite integral** (a family of functions):

- •Notation: ∫ f(x) dx
- •Output: F(x) + C where F′(x) = f(x)

It’s common to say “the integral is the area under the curve,” but that’s only fully accurate when f(x) ≥ 0. In general, a definite integral measures **signed area** (area above the x-axis counts positive, below counts negative).

### What does dx mean?

In ∫ₐᵇ f(x) dx:

- •x is the variable you integrate with respect to.
- •**dx** suggests a tiny width in x.

In Riemann-sum language, dx corresponds to Δx in the limit as Δx → 0.

A key habit: treat f(x) as the “height” and dx as the “infinitesimal width,” so f(x) dx is an infinitesimal “slice of area/accumulation.”

### A first geometric picture

Imagine approximating the region under y = f(x) from x = a to x = b by rectangles.

- •Each rectangle has width Δx.
- •Height is sampled from f at some point in the subinterval.
- •Sum of rectangle areas approximates the total.

As Δx gets smaller, this approximation improves. The limit (if it exists) is the definite integral.

## Core Mechanic 1: Definite Integrals as Limits of Riemann Sums

### Why a limit definition matters

If we only said “area under a curve,” we’d be stuck with vague pictures. The power of calculus is that it turns pictures into precise computations.

The definite integral is defined as a limit of sums, which makes it:

- •**Precise** (no handwaving)
- •**Flexible** (works for many kinds of accumulation)

### Partitioning the interval

Take an interval [a, b] and split it into n subintervals.

- •For simplicity (uniform partition):
- •Δx = (b − a) / n
- •Points: x₀ = a, x₁ = a + Δx, …, xₙ = b

Now, on each subinterval [xᵢ₋₁, xᵢ], pick a sample point xᵢ\*.

Common choices:

- •Left endpoint: xᵢ\* = xᵢ₋₁
- •Right endpoint: xᵢ\* = xᵢ
- •Midpoint: xᵢ\* = (xᵢ₋₁ + xᵢ)/2

### The Riemann sum

The approximate accumulated value is:

∑ᵢ₌₁ⁿ f(xᵢ\*) Δx

Think “height × width” for each rectangle, then add them.

### The limit definition of the definite integral

If the limit exists as n → ∞ (and thus Δx → 0), we define:

∫ₐᵇ f(x) dx = limₙ→∞ ∑ᵢ₌₁ⁿ f(xᵢ\*) Δx

This is the **definite integral**.

### Signed area and interpretation

- •If f(x) ≥ 0 on [a, b], the integral equals the usual geometric area.
- •If f dips below the x-axis, the integral subtracts that area.

So a better mental model is:

- •**Definite integral = net accumulation**.

Examples of “net accumulation”:

- •Net change in position from velocity
- •Total mass from density
- •Total probability from a probability density function

### Properties you can trust (and why they’re reasonable)

These follow naturally from sums and limits:

1) **Linearity**

∫ₐᵇ (αf(x) + βg(x)) dx = α∫ₐᵇ f(x) dx + β∫ₐᵇ g(x) dx

Why: sums distribute over addition and scalar multiplication.

2) **Additivity over intervals**

If a < c < b, then:

∫ₐᵇ f(x) dx = ∫ₐᶜ f(x) dx + ∫ᶜᵇ f(x) dx

Why: splitting an interval splits the corresponding sum.

3) **Reversing bounds flips sign**

∫ᵇₐ f(x) dx = −∫ₐᵇ f(x) dx

Why: you’re “accumulating backward,” so net accumulation reverses.

### A note on existence (at this level)

Most functions you meet early on (polynomials, exponentials, trig functions, continuous functions) are integrable on closed intervals. You don’t need the advanced theory yet—just know the Riemann-sum definition is what makes everything precise.

## Core Mechanic 2: Indefinite Integrals as Antiderivatives (and the +C)

### Why antiderivatives matter

Riemann sums are conceptually foundational, but not a practical way to compute integrals by hand.

So we look for a function whose derivative gives the integrand.

If F′(x) = f(x), then F is an **antiderivative** of f.

### Indefinite integral definition

We write:

∫ f(x) dx = F(x) + C

where:

- •F′(x) = f(x)
- •C is an arbitrary constant

### Why the constant C must be there

If F′(x) = f(x), then (F(x) + C)′ = F′(x) + 0 = f(x).

So there isn’t just one antiderivative—there’s a whole family of them.

Geometrically, adding C shifts a graph up or down without changing slopes.

### Common antiderivative patterns (starter kit)

You already know derivative rules; integration reverses them.

| f(x) | One antiderivative F(x) | Check by differentiating |
| --- | --- | --- |
| xⁿ (n ≠ −1) | xⁿ⁺¹/(n+1) | d/dx [xⁿ⁺¹/(n+1)] = xⁿ |
| 1/x | ln | x |  | d/dx [ln | x | ] = 1/x |
| eˣ | eˣ | derivative stays eˣ |
| cos(x) | sin(x) | (sin x)′ = cos x |
| sin(x) | −cos(x) | (−cos x)′ = sin x |

### The “dx” in indefinite integrals

In ∫ f(x) dx, the dx tells you:

- •which variable is being accumulated over
- •what variable the antiderivative should be a function of

Example:

- •∫ (3t²) dt = t³ + C
- •∫ (3x²) dx = x³ + C

Same pattern, different variable.

### Quick sanity check habit

After you integrate, differentiate your answer.

If you don’t get back the integrand, something went wrong.

This is especially useful because integration has more “gotchas” than differentiation (constants, absolute values for ln|x|, etc.).

## Application/Connection: The Fundamental Theorem of Calculus (FTC)

### Why the FTC is the bridge

So far we have two stories:

- •Definite integral: a limit of sums (accumulation)
- •Indefinite integral: antiderivative (reverse of differentiation)

The Fundamental Theorem of Calculus says these are not separate topics—they are two sides of one idea.

### FTC (evaluation form)

If f is continuous on [a, b] and F is any antiderivative of f (so F′(x) = f(x)), then:

∫ₐᵇ f(x) dx = F(b) − F(a)

This is the main computational tool for definite integrals.

### Why this makes sense (intuition before algebra)

Think of accumulation as “total change.”

If F′(x) = f(x), then f describes how F changes.

So accumulating f from a to b should give the net change in F from a to b.

That net change is F(b) − F(a).

### Mini-derivation sketch (connecting to Riemann sums)

Start with a partition a = x₀ < x₁ < … < xₙ = b.

Because F′ = f, changes in F over each subinterval are approximately:

F(xᵢ) − F(xᵢ₋₁) ≈ f(xᵢ\*) (xᵢ − xᵢ₋₁)

Now add over i = 1…n:

∑ᵢ₌₁ⁿ (F(xᵢ) − F(xᵢ₋₁)) ≈ ∑ᵢ₌₁ⁿ f(xᵢ\*) Δxᵢ

The left side *telescopes*:

(F(x₁) − F(x₀)) + (F(x₂) − F(x₁)) + … + (F(xₙ) − F(xₙ₋₁))

= F(xₙ) − F(x₀)

= F(b) − F(a)

As the partition gets finer (max Δxᵢ → 0), the approximation becomes exact, and the right side becomes the integral:

F(b) − F(a) = ∫ₐᵇ f(x) dx

That’s the FTC in action.

### Practical workflow for computing a definite integral

1) Find an antiderivative F(x) of f(x).

2) Evaluate F(b) − F(a).

### Interpreting results

- •If f is velocity, ∫ₐᵇ f(t) dt is displacement.
- •If f is speed (nonnegative), the integral is distance traveled.
- •If f is a rate of accumulation, the integral is total accumulated quantity.

### Looking ahead

This idea generalizes:

- •Multiple integrals accumulate over areas/volumes.
- •Measure theory formalizes “accumulation” for very irregular sets and functions.

But the core intuition stays the same: **add up infinitesimal contributions**.

## Worked Examples (3)

### Riemann sum → definite integral for f(x) = x on [0, 1]

Compute ∫₀¹ x dx from the limit definition using a right-endpoint Riemann sum.

1. Partition [0, 1] into n equal pieces.

   Δx = (1 − 0)/n = 1/n

   xᵢ = i/n (right endpoints)
2. Form the Riemann sum:

   ∑ᵢ₌₁ⁿ f(xᵢ) Δx = ∑ᵢ₌₁ⁿ (xᵢ)(1/n)

   = ∑ᵢ₌₁ⁿ (i/n)(1/n)

   = ∑ᵢ₌₁ⁿ i / n²
3. Use the formula ∑ᵢ₌₁ⁿ i = n(n+1)/2:

   ∑ᵢ₌₁ⁿ i / n² = (1/n²) · n(n+1)/2

   = (n(n+1)) / (2n²)

   = (n+1)/(2n)
4. Take the limit:

   limₙ→∞ (n+1)/(2n)

   = limₙ→∞ (1/2)(1 + 1/n)

   = 1/2
5. Therefore:

   ∫₀¹ x dx = 1/2

**Insight:** The “area under y = x from 0 to 1” is a triangle with area 1/2, and the Riemann-sum limit matches the geometry. The limit definition turns that geometric fact into a general computation method.

### Indefinite integral as an antiderivative (and checking by differentiation)

Find ∫ (6x² − 4x + 5) dx and verify by differentiating.

1. Integrate term-by-term using linearity:

   ∫ (6x² − 4x + 5) dx

   = ∫ 6x² dx − ∫ 4x dx + ∫ 5 dx
2. Apply the power rule for integrals (reverse of derivative power rule):

   ∫ 6x² dx = 6 · x³/3 = 2x³

   ∫ 4x dx = 4 · x²/2 = 2x²

   ∫ 5 dx = 5x
3. Combine and add the constant:

   ∫ (6x² − 4x + 5) dx = 2x³ − 2x² + 5x + C
4. Check by differentiating:

   d/dx [2x³ − 2x² + 5x + C]

   = 6x² − 4x + 5 + 0

   = 6x² − 4x + 5

   Matches the integrand.

**Insight:** Indefinite integration is “find a function whose slope is the given function.” The +C is not optional; it represents the whole family of functions with the same derivative.

### Using the FTC to evaluate a definite integral quickly

Compute ∫₂⁵ (3x² − 1) dx using an antiderivative.

1. Find an antiderivative:

   ∫ (3x² − 1) dx

   = ∫ 3x² dx − ∫ 1 dx

   = x³ − x + C
2. Apply FTC:

   ∫₂⁵ (3x² − 1) dx = [x³ − x]₂⁵

   = (5³ − 5) − (2³ − 2)
3. Compute:

   (125 − 5) − (8 − 2)

   = 120 − 6

   = 114

**Insight:** Riemann sums define the definite integral, but the FTC is what makes it practical: convert a “limit of sums” into “evaluate an antiderivative at endpoints.”

## Key Takeaways

- ✓

  A definite integral ∫ₐᵇ f(x) dx is defined as a limit of Riemann sums ∑ f(xᵢ\*) Δx (net accumulation).
- ✓

  The symbol dx corresponds to an infinitesimal width in the integration variable; in sums it’s the Δx that goes to 0.
- ✓

  Definite integrals measure **signed area**: parts below the x-axis contribute negatively.
- ✓

  An indefinite integral ∫ f(x) dx is the set of all antiderivatives: F(x) + C where F′(x) = f(x).
- ✓

  The constant C is required because derivatives erase constants, so antiderivatives are never unique.
- ✓

  Linearity holds: integrals distribute over addition and pull out constants.
- ✓

  Fundamental Theorem of Calculus: if F′ = f, then ∫ₐᵇ f(x) dx = F(b) − F(a), connecting accumulation with net change.

## Common Mistakes

- ✗

  Forgetting the +C in an indefinite integral (losing the whole family of antiderivatives).
- ✗

  Treating ∫ₐᵇ f(x) dx as “area” even when f(x) is negative (it’s signed area / net accumulation).
- ✗

  Mixing up variables and differentials (e.g., writing ∫ f(x) dt without changing the function to f(t)).
- ✗

  Using FTC without evaluating at both endpoints (computing F(b) but forgetting −F(a)).

## Practice

easy

Compute ∫₀² (x + 1) dx and interpret it as net area.

**Hint:** Find an antiderivative F(x) and use F(2) − F(0).

Show solution

Antiderivative: ∫ (x + 1) dx = x²/2 + x + C.

Evaluate:

∫₀² (x + 1) dx = [x²/2 + x]₀² = (4/2 + 2) − 0 = 2 + 2 = 4.

Since x + 1 ≥ 0 on [0, 2], this equals the ordinary area under the curve.

medium

Find the most general antiderivative: ∫ (1/x + 2cos(x)) dx.

**Hint:** Use ln|x| for ∫ 1/x dx and remember ∫ cos(x) dx = sin(x).

Show solution

∫ (1/x + 2cos(x)) dx = ∫ 1/x dx + 2∫ cos(x) dx

= ln|x| + 2sin(x) + C.

hard

Use a right-endpoint Riemann sum with n subintervals to compute ∫₀¹ x² dx (set it up and take the limit).

**Hint:** With Δx = 1/n and xᵢ = i/n, the sum becomes (1/n)∑ (i/n)². Use ∑ i² = n(n+1)(2n+1)/6.

Show solution

Partition [0, 1] into n equal parts: Δx = 1/n, right endpoints xᵢ = i/n.

Riemann sum:

∑ᵢ₌₁ⁿ f(xᵢ)Δx = ∑ᵢ₌₁ⁿ (i/n)² (1/n)

= (1/n³) ∑ᵢ₌₁ⁿ i².

Use ∑ᵢ₌₁ⁿ i² = n(n+1)(2n+1)/6:

(1/n³) · n(n+1)(2n+1)/6

= (n+1)(2n+1) / (6n²).

Take the limit:

limₙ→∞ (n+1)(2n+1)/(6n²)

= limₙ→∞ (2n² + 3n + 1)/(6n²)

= 2/6

= 1/3.

Therefore ∫₀¹ x² dx = 1/3.

## Connections

- •Next: [Fundamental Theorem of Calculus](/tech-tree/fundamental-theorem/)
- •Extends to higher dimensions: [Multiple Integrals](/tech-tree/multiple-integrals/)
- •Rigorous foundations and generalized integration: [Measure Theory](/tech-tree/measure-theory/)
- •Review prerequisite: [Derivatives](/tech-tree/derivatives/)

Quality: B (4.1/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
