---
title: Continuity
description: Functions without breaks. Limit equals function value.
date: '2026-07-01'
scheduled: '2026-12-26'
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
inspiration_url: https://templeton.host/tech-tree/continuity/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/continuity/](https://templeton.host/tech-tree/continuity/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Continuity

CalculusDifficulty: ★★☆☆☆Depth: 2Unlocks: 0

Functions without breaks. Limit equals function value.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Function value at the point exists (f(a) is defined)
- -Limit of f(x) as x approaches the point exists (left and right limits agree)
- -The limit equals the function value at that point (lim\_{x->a} f(x) = f(a))

## Key Symbols & Notation

lim\_{x->a} f(x)

## Essential Relationships

- -f is continuous at a if and only if lim\_{x->a} f(x) = f(a) (which requires f(a) to be defined and the limit to exist)

## Prerequisites (1)

[Limits5 atoms](/tech-tree/limits/)

Advanced Learning Details

### Graph Position

22

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

2

Chain Length

### Cognitive Load

5

Atomic Elements

19

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (6)

- - Continuity at a point: the function is 'unbroken' at x=a (intuitively no hole, jump, or asymptote at that point)
- - Formal continuity criterion: lim\_{x→a} f(x) equals f(a) (and f(a) must be defined)
- - Continuity on an interval/domain: function is continuous at every point of that interval/domain
- - One-sided continuity: continuity from the left or right using one-sided limits
- - Discontinuity as a concept (a point where continuity fails)
- - Types of discontinuities: removable (hole), jump (left and right limits differ), infinite/essential (unbounded behavior)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Calculus only works when “nearby inputs give nearby outputs” in a predictable way. Continuity is the rule that formalizes that idea: no surprise jumps at the point you care about.

TL;DR:

A function f is continuous at x = a when (1) f(a) is defined, (2) lim₍ₓ→ₐ₎ f(x) exists, and (3) lim₍ₓ→ₐ₎ f(x) = f(a). Continuity is a local property (point-by-point) that lets you safely evaluate limits by substitution and is the gateway to derivatives and integrals behaving nicely.

## What Is Continuity?

### Why continuity matters (intuition first)

When you use a function to model something real—position over time, temperature over distance, probability over a parameter—you often assume there are no “teleportations.” If you nudge the input slightly, the output shouldn’t suddenly jump to a completely different value.

Continuity captures this “no breaks” idea **at a specific point**. Importantly, continuity is not about what happens far away; it’s about what happens **arbitrarily close** to a point.

### The formal definition (three conditions)

A function f(x) is **continuous at x = a** if all three of the following are true:

1) **Function value exists:** f(a) is defined.

2) **Limit exists:** lim₍ₓ→ₐ₎ f(x) exists (the left-hand and right-hand limits agree).

3) **They match:** lim₍ₓ→ₐ₎ f(x) = f(a).

Written compactly, continuity at a is:

lim₍ₓ→ₐ₎ f(x) = f(a)

…but only after you’ve checked that both sides actually exist.

### “Limit equals function value” is the heart of it

Think of lim₍ₓ→ₐ₎ f(x) as the value the function is **trying** to take as x gets close to a. Think of f(a) as the value the function **actually** takes at x = a.

Continuity says: the “trying” and the “actually” are the same.

### Continuity is local

A function can be continuous at some points and not others. For example, piecewise functions often behave well on each piece, but fail at the boundaries.

### A note on vectors

Later in calculus you’ll study vector-valued functions like **r**(t). Continuity extends naturally: **r**(t) is continuous at t = a if each component is continuous at a. We won’t need vector techniques here, but the concept scales.

## Core Mechanic 1: Limits from Both Sides (Does the limit exist?)

### Why the limit is the first “gate”

Continuity depends on a limit, so the first thing to check is whether lim₍ₓ→ₐ₎ f(x) exists. Many discontinuities are simply cases where the function approaches **different values** from the left and right.

### Left-hand and right-hand limits

We define:

- •Left-hand limit: lim₍ₓ→ₐ⁻₎ f(x)
- •Right-hand limit: lim₍ₓ→ₐ⁺₎ f(x)

The two-sided limit exists exactly when:

lim₍ₓ→ₐ⁻₎ f(x) = lim₍ₓ→ₐ⁺₎ f(x)

If they are unequal, the two-sided limit does not exist, and **continuity is impossible** at that point.

### Common “limit failure” patterns

| Pattern | What you see near x = a | What it means for lim₍ₓ→ₐ₎ f(x) | Typical name |
| --- | --- | --- | --- |
| Jump | Approaches L from left, R from right, L ≠ R | Does not exist | Jump discontinuity |
| Infinite blow-up | Values grow without bound (→ ∞ or → −∞) | Does not exist as a finite number | Infinite discontinuity |
| Wild oscillation | Values keep oscillating, never settling | Does not exist | Oscillatory discontinuity |

At Difficulty 2, the most common is the **jump** created by a piecewise definition.

### If the limit exists, continuity still might fail

Even when lim₍ₓ→ₐ₎ f(x) exists, the function may still not be continuous if:

- •f(a) is not defined, or
- •f(a) is defined but not equal to the limit.

That leads to a very important type: a **removable discontinuity**, where the graph has a “hole” that could be fixed by redefining f(a).

### Breathing room: what you should internalize

To decide if f is continuous at a, don’t jump straight to substitution. Instead, mentally run a checklist:

1) Can I compute lim₍ₓ→ₐ₎ f(x)?

2) Is f(a) actually defined?

3) Do those two numbers match?

This checklist is the backbone of everything that follows.

## Core Mechanic 2: The Three-Condition Continuity Test (and types of discontinuities)

### Why a three-part test?

The definition lim₍ₓ→ₐ₎ f(x) = f(a) is elegant, but it hides “existence checks.” If f(a) doesn’t exist, the equation is meaningless. If the limit doesn’t exist, you can’t compare.

So we use the practical three-condition test:

**f is continuous at a** ⇔

1) f(a) exists

2) lim₍ₓ→ₐ₎ f(x) exists

3) lim₍ₓ→ₐ₎ f(x) = f(a)

### Worked logic: what failure looks like

Let’s label the values:

- •A = f(a) (the function’s defined value)
- •L = lim₍ₓ→ₐ₎ f(x) (the approached value)

Continuity at a means: both exist and L = A.

If continuity fails, it’s because at least one of these is true:

- •A doesn’t exist (the function isn’t defined at a)
- •L doesn’t exist (left/right mismatch, blow-up, oscillation)
- •L exists and A exists, but L ≠ A

### Types of discontinuities you’ll meet most often

#### 1) Removable discontinuity (“hole”)

This is the situation:

- •L = lim₍ₓ→ₐ₎ f(x) exists
- •But either f(a) is undefined, or f(a) ≠ L

You can “remove” the discontinuity by defining a new function g that matches f everywhere except at a, where you set g(a) = L.

#### 2) Jump discontinuity

This is the situation:

lim₍ₓ→ₐ⁻₎ f(x) ≠ lim₍ₓ→ₐ⁺₎ f(x)

The graph has a step/jump. There is no single value L for the two-sided limit, so continuity is impossible.

#### 3) Infinite discontinuity

The function grows without bound near a (often due to division by zero):

lim₍ₓ→ₐ₎ f(x) = ∞ or −∞ (not a finite limit)

At this level, the key idea is: if the output “blows up,” it does not settle to a finite real number, so continuity fails.

### Continuity on an interval

- •Continuous on (a, b) means continuous at every point inside.
- •Continuous on [a, b] means continuous on (a, b) **and** right-continuous at a and left-continuous at b.

You don’t need heavy formalism here, but it’s useful vocabulary because many calculus theorems assume continuity on a closed interval.

### A powerful consequence: substitution

If f is continuous at a, then:

lim₍ₓ→ₐ₎ f(x) = f(a)

So you can evaluate the limit by direct substitution. This is one of the main reasons continuity is so valuable: it converts a “nearby behavior” question (a limit) into an “at the point” computation.

## Application/Connection: Why Continuity Is the Gateway to Calculus

### Why continuity shows up everywhere

Continuity is the quiet assumption behind many “nice” behaviors in calculus.

1) **Derivatives require continuity** (in most standard settings)

If f is differentiable at a, then f is continuous at a. (The converse is not always true: continuous does not imply differentiable.)

This matters because it sets expectations:

- •If you see a jump or hole, you can immediately say “not differentiable there.”

2) **Integrals behave well for continuous functions**

Continuous functions on [a, b] are guaranteed to be integrable (in the Riemann sense). This is a major reason textbooks love continuous examples.

3) **The Intermediate Value Theorem (IVT)**

A famous theorem (you’ll likely learn soon) says: if f is continuous on [a, b], then f takes every value between f(a) and f(b).

Intuitively: you can’t go from one height to another without passing through all intermediate heights—**if there are no breaks**.

This powers root-finding logic: if f(a) and f(b) have opposite signs and f is continuous, then there exists c ∈ (a, b) such that f(c) = 0.

### Continuity as “compatibility” between algebra and limits

A major theme in calculus is: certain operations preserve continuity.

- •Polynomials are continuous everywhere.
- •Rational functions are continuous wherever the denominator ≠ 0.
- •Many elementary functions (sin, cos, exp, ln) are continuous on their domains.

So if you build a function from continuous pieces using addition, multiplication, and composition, you often inherit continuity automatically—meaning you can evaluate limits by substitution at most points.

### Small connection to machine learning

Loss functions and activation functions are often designed to be continuous (and preferably differentiable), because optimization methods like gradient descent rely on smooth local behavior. Discontinuities can cause unstable training dynamics or undefined gradients.

Even when models include non-smooth parts (like ReLU), continuity is still often preserved (ReLU is continuous, though not differentiable at 0). That’s a practical example of “continuous but not differentiable,” which mirrors the theoretical distinction.

### The mental model to keep

Continuity is a promise:

As x approaches a,

f(x) approaches f(a).

It’s the bridge between “nearby” and “at the point,” and that bridge is what makes the rest of calculus work.

## Worked Examples (3)

### Example 1: Checking continuity of a piecewise function (jump vs match)

Let f(x) = { x + 1 if x < 2; 5 if x ≥ 2 }. Determine whether f is continuous at x = 2.

1. Step 1: Compute the left-hand limit.

   For x < 2, f(x) = x + 1.

   So:

   lim₍ₓ→2⁻₎ f(x) = lim₍ₓ→2⁻₎ (x + 1)

   = 2 + 1

   = 3
2. Step 2: Compute the right-hand limit.

   For x ≥ 2, f(x) = 5 (a constant).

   So:

   lim₍ₓ→2⁺₎ f(x) = lim₍ₓ→2⁺₎ 5

   = 5
3. Step 3: Compare left and right limits.

   We have:

   lim₍ₓ→2⁻₎ f(x) = 3

   lim₍ₓ→2⁺₎ f(x) = 5

   Since 3 ≠ 5, the two-sided limit lim₍ₓ→2₎ f(x) does not exist.
4. Step 4: Apply the continuity test.

   Because lim₍ₓ→2₎ f(x) does not exist, f cannot be continuous at x = 2.

   (We don’t even need f(2), but for completeness: f(2) = 5.)

**Insight:** Continuity fails immediately if the left and right limits disagree. Piecewise functions often create jump discontinuities at boundary points.

### Example 2: A removable discontinuity and how to “fix” it

Define f(x) = (x² − 1)/(x − 1) for x ≠ 1, and suppose f(1) is not defined. Is f continuous at x = 1? If not, how can we redefine it to make it continuous?

1. Step 1: Identify the issue at x = 1.

   At x = 1, the denominator x − 1 = 0, so the given formula does not define f(1). Thus condition (1) fails: f(1) does not exist.
2. Step 2: Compute the limit lim₍ₓ→1₎ f(x).

   Start by factoring the numerator:

   x² − 1 = (x − 1)(x + 1)

   So for x ≠ 1:

   f(x) = (x² − 1)/(x − 1)

   = ((x − 1)(x + 1))/(x − 1)

   = x + 1
3. Step 3: Now take the limit using the simplified expression.

   lim₍ₓ→1₎ f(x) = lim₍ₓ→1₎ (x + 1)

   = 1 + 1

   = 2
4. Step 4: Classify the discontinuity.

   The limit exists and equals 2, but f(1) is undefined.

   So this is a removable discontinuity (a “hole” at x = 1).
5. Step 5: Redefine the function to make it continuous.

   Define a new function g such that:

   - •g(x) = f(x) for x ≠ 1
   - •g(1) = 2

   Then lim₍ₓ→1₎ g(x) = 2 and g(1) = 2, so g is continuous at x = 1.

**Insight:** A removable discontinuity happens when the limit exists but the function value is missing (or wrong). Continuity can often be restored by redefining the function at a single point to match the limit.

### Example 3: Continuity via substitution (polynomial case)

Let f(x) = 3x³ − 2x + 7. Evaluate lim₍ₓ→−1₎ f(x) and justify using continuity.

1. Step 1: Recognize the function type.

   f(x) is a polynomial. Polynomials are continuous for all real x.
2. Step 2: Use the continuity rule.

   Because f is continuous at x = −1:

   lim₍ₓ→−1₎ f(x) = f(−1)
3. Step 3: Compute f(−1).

   f(−1) = 3(−1)³ − 2(−1) + 7

   = 3(−1) + 2 + 7

   = −3 + 2 + 7

   = 6
4. Step 4: Conclude.

   Therefore:

   lim₍ₓ→−1₎ (3x³ − 2x + 7) = 6

**Insight:** Continuity often turns a limit problem into straightforward evaluation. Knowing which function families are continuous saves time and reduces errors.

## Key Takeaways

- ✓

  Continuity at x = a means: f(a) exists, lim₍ₓ→ₐ₎ f(x) exists, and lim₍ₓ→ₐ₎ f(x) = f(a).
- ✓

  The two-sided limit exists only if lim₍ₓ→ₐ⁻₎ f(x) = lim₍ₓ→ₐ⁺₎ f(x).
- ✓

  If the limit exists but f(a) is missing or not equal to the limit, the discontinuity is removable (a “hole”).
- ✓

  Jump discontinuities come from mismatched left/right limits; they cannot be fixed by redefining a single point.
- ✓

  Polynomials are continuous everywhere; rational functions are continuous wherever the denominator ≠ 0.
- ✓

  If f is continuous at a, you can evaluate lim₍ₓ→ₐ₎ f(x) by direct substitution: f(a).
- ✓

  Differentiability implies continuity, so any discontinuity rules out a derivative at that point.

## Common Mistakes

- ✗

  Assuming lim₍ₓ→ₐ₎ f(x) exists without checking left-hand and right-hand limits separately for piecewise functions.
- ✗

  Thinking “f(a) is defined” automatically implies continuity; you still need the limit to exist and to match f(a).
- ✗

  Canceling factors like (x − 1) and then plugging in x = 1 into the original function (which was undefined there) without stating the domain restriction x ≠ 1.
- ✗

  Believing continuous ⇒ differentiable; many functions are continuous but have corners/cusps where the derivative does not exist.

## Practice

easy

Determine whether f(x) = { 2x if x ≤ 1; x + 1 if x > 1 } is continuous at x = 1.

**Hint:** Compute lim₍ₓ→1⁻₎ f(x), lim₍ₓ→1⁺₎ f(x), and compare them to f(1).

Show solution

Left-hand limit: for x ≤ 1, f(x) = 2x, so lim₍ₓ→1⁻₎ f(x) = 2·1 = 2.

Right-hand limit: for x > 1, f(x) = x + 1, so lim₍ₓ→1⁺₎ f(x) = 1 + 1 = 2.

Thus lim₍ₓ→1₎ f(x) exists and equals 2.

Function value: f(1) = 2·1 = 2.

Since lim₍ₓ→1₎ f(x) = f(1) = 2, f is continuous at x = 1.

medium

Let f(x) = (x² − 4)/(x − 2) for x ≠ 2, and define f(2) = 10. Is f continuous at x = 2? If not, what value should f(2) be to make it continuous?

**Hint:** Factor x² − 4 and simplify for x ≠ 2, then compute lim₍ₓ→2₎ f(x).

Show solution

For x ≠ 2:

(x² − 4)/(x − 2) = ((x − 2)(x + 2))/(x − 2) = x + 2.

So lim₍ₓ→2₎ f(x) = lim₍ₓ→2₎ (x + 2) = 4.

But f(2) is defined as 10, so lim₍ₓ→2₎ f(x) = 4 ≠ 10 = f(2).

Therefore f is not continuous at x = 2.

To make it continuous, redefine f(2) = 4.

hard

Find all values of k such that f(x) = { kx + 3 if x < 0; x² + 3 if x ≥ 0 } is continuous at x = 0.

**Hint:** Continuity at 0 requires lim₍ₓ→0⁻₎ f(x) = lim₍ₓ→0⁺₎ f(x) and both equal f(0).

Show solution

Compute the left-hand limit:

For x < 0, f(x) = kx + 3.

lim₍ₓ→0⁻₎ f(x) = lim₍ₓ→0⁻₎ (kx + 3) = k·0 + 3 = 3.

Compute the right-hand limit:

For x ≥ 0, f(x) = x² + 3.

lim₍ₓ→0⁺₎ f(x) = lim₍ₓ→0⁺₎ (x² + 3) = 0² + 3 = 3.

They already match (both are 3) for any k.

Now check f(0): since 0 ≥ 0, f(0) = 0² + 3 = 3.

Thus lim₍ₓ→0₎ f(x) = 3 = f(0) regardless of k.

So f is continuous at x = 0 for all real k.

## Connections

Next nodes you’ll likely want:

- •[Limits](/tech-tree/limits/)
- •[Derivatives (Intro)](/tech-tree/derivatives-intro/)
- •[Intermediate Value Theorem](/tech-tree/intermediate-value-theorem/)
- •[Piecewise Functions](/tech-tree/piecewise-functions/)
- •[Differentiability vs Continuity](/tech-tree/differentiability-vs-continuity/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
