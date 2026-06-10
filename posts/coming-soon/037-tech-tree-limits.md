---
title: Limits
description: Value a function approaches as input approaches a point. Foundation of calculus.
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
permalink: /tech-tree/limits/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Limits

CalculusDifficulty: ★★☆☆☆Depth: 1Unlocks: 113

Value a function approaches as input approaches a point. Foundation of calculus.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Input approaches a point (the variable tends toward a specified value, not necessarily reaching it)
- -Function outputs approach a single number (there is a target value the function values get arbitrarily close to)
- -Limit depends on values arbitrarily near the point, not on the function's value at the point

## Key Symbols & Notation

lim\_{x -> a} f(x) = L

## Essential Relationships

- -A two-sided limit exists iff the left-hand limit and the right-hand limit (approaches from each side) are equal

## Prerequisites (2)

[Functions6 atoms](/tech-tree/functions-basic/)[Coordinate Systems6 atoms](/tech-tree/coordinate-plane/)

## Unlocks (4)

[Derivativeslvl 2](/tech-tree/derivatives-basic/)[Big O Notationlvl 2](/tech-tree/big-o/)[Law of Large Numberslvl 3](/tech-tree/law-large-numbers/)[Continuitylvl 2](/tech-tree/continuity/)

Advanced Learning Details

### Graph Position

17

Depth Cost

113

Fan-Out (ROI)

46

Bottleneck Score

1

Chain Length

### Cognitive Load

5

Atomic Elements

30

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (13)

- - Limit (intuitive): the value a function approaches as the input approaches a specific point
- - Formal epsilon-delta definition of limit
- - One-sided limits (left-hand limit and right-hand limit)
- - Limit existence criterion: a (two-sided) limit exists only if left and right one-sided limits exist and are equal
- - Limits at infinity: behavior of a function as the input grows without bound
- - Infinite limits: function values grow without bound as input approaches a finite point (vertical asymptote behavior)
- - Removable discontinuity: limit exists at a point but the function is undefined there or has a different value
- - Jump discontinuity: left and right one-sided limits exist but are different
- - Indeterminate forms (e.g., 0/0, ∞/∞) that require further analysis rather than direct substitution
- - Squeeze (sandwich) theorem for establishing limits by bounding
- - Limit laws: rules for limits of sums, differences, products, quotients, constant multiples, powers and roots
- - Evaluation techniques for limits (direct substitution when valid, algebraic simplification such as factoring or rationalizing, bounding/sandwich)
- - Concept that a limit depends only on values arbitrarily close to the approach point (not on the function value at the point)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Calculus begins when you stop asking “what is the value at x?” and start asking “what happens as x gets close to a?” Limits formalize that idea: they capture the *trend* of a function near a point, even when the function is messy, undefined, or unhelpful exactly at that point.

TL;DR:

A limit lim\_{x → a} f(x) = L means: by taking x sufficiently close to a (not necessarily equal), you can make f(x) as close to L as you want. Limits depend on values *near* a, not the value *at* a. One-sided limits and “infinite limits” handle edges and blow-ups.

## What Is a Limit?

### Why limits exist (motivation)

When you evaluate a function f(x), you plug in a number x and get an output. That works well when the function behaves nicely everywhere. But many important questions are about **behavior near a point**, not at the point:

- •What height does a curve *approach* as x gets close to 2?
- •What slope does a curve *approach* as you zoom in (derivatives)?
- •What constant does a sequence of averages *approach* as sample size grows (law of large numbers)?
- •How does runtime grow as input size grows (Big O)?

The common pattern: **we care about what happens as the input approaches something**.

### The intuitive definition

We write

lim\_{x → a} f(x) = L

and read it as:

> “As x approaches a, f(x) approaches L.”

This means the outputs f(x) can be made **arbitrarily close** to L by choosing x **sufficiently close** to a.

Two key ideas are hidden in this sentence:

1) **x approaches a** does *not* mean x = a. In fact, x might never equal a.

2) The limit depends on f(x) values **near** a, not on what happens **at** a.

### “Approach” as a distance idea

Because you know the distance formula, it helps to translate “approaches” into distance:

- •“x approaches a” means the distance |x − a| becomes very small.
- •“f(x) approaches L” means the distance |f(x) − L| becomes very small.

So limits connect two distances:

- •small |x − a| ⇒ small |f(x) − L|

### What limits are *not*

Limits are often confused with:

- •**Substitution**: f(a) is just plugging in x = a.
- •**Value at a point**: f(a) could be undefined or different from the limit.
- •**A guarantee about far away behavior**: a limit only describes behavior near a.

### A quick picture in words

Imagine a function with a hole at x = 2, but the curve around it sits near y = 5. You might have f(2) undefined (a hole), yet

lim\_{x → 2} f(x) = 5.

That is not a contradiction: limits ignore the single point x = 2 and care about points arbitrarily close to 2.

### The formal (ε–δ) meaning, gently

You don’t need full formalism yet, but the core idea is worth stating:

lim\_{x → a} f(x) = L means:

For every ε > 0, there exists δ > 0 such that if 0 < |x − a| < δ, then |f(x) − L| < ε.

Interpretation:

- •ε controls how close you want f(x) to be to L.
- •δ tells you how close you must take x to a to achieve that.
- •The condition 0 < |x − a| excludes x = a, reinforcing that the limit doesn’t depend on f(a).

Even if you never write ε–δ proofs, this definition explains the “arbitrarily close” nature of limits.

## Core Mechanic 1: Evaluating Limits (Substitution, Algebra, and “Near a Point” Thinking)

### Why evaluation methods matter

A limit is a behavioral claim. But in practice, you want to *compute* limits efficiently. The big strategy is:

1) Try direct substitution.

2) If substitution fails (often because of 0/0), simplify the function without changing its behavior near a.

3) If it still fails, use alternative viewpoints (graphs, tables, special limit facts, or more advanced tools later).

### Method A: Direct substitution (when it works)

If f is “well-behaved” at a (no division by 0, no discontinuity), then the limit usually equals the function value:

lim\_{x → a} f(x) = f(a).

Example pattern:

- •If f(x) = x² + 3x, then lim\_{x → 2} f(x) = 2² + 3·2 = 10.

This is *not* the definition of a limit; it’s a consequence for continuous functions (a concept you’ll unlock soon).

### Method B: The indeterminate form 0/0 (a sign to simplify)

A common situation:

lim\_{x → a} \frac{g(x)}{h(x)}

where g(a) = 0 and h(a) = 0. Direct substitution gives 0/0, which is **indeterminate**: it does not mean the limit is 0, undefined, or anything by itself.

The point is: near x = a, the expression might simplify.

#### Classic tool: factoring and canceling

Suppose

f(x) = \frac{x² − 4}{x − 2}.

At x = 2, both numerator and denominator are 0. But:

x² − 4 = (x − 2)(x + 2)

So for x ≠ 2,

\frac{x² − 4}{x − 2} = \frac{(x − 2)(x + 2)}{x − 2} = x + 2.

Now the behavior near 2 is the same as the simpler function x + 2 (except at the single point x = 2).

So:

lim\_{x → 2} \frac{x² − 4}{x − 2}

= lim\_{x → 2} (x + 2)

= 4.

Notice what happened: we never needed f(2). In fact, the original expression is undefined at x = 2, yet the limit exists.

### Method C: Rationalizing (when roots cause 0/0)

If you see something like:

\frac{√(x + c) − √(a + c)}{x − a}

direct substitution often yields 0/0. A standard move is to multiply by the conjugate.

Example structure:

(√u − √v)(√u + √v) = u − v.

That difference of squares is what removes the radical.

### “Limit depends on near values, not the point” (a concept check)

Consider a function:

f(x) =

- •3x + 1, for x ≠ 2
- •100, for x = 2

Then:

lim\_{x → 2} f(x) = lim\_{x → 2} (3x + 1) = 7.

Even though f(2) = 100, the limit is 7 because all x values near 2 (but not equal to 2) use 3x + 1.

This is one of the most important limit intuitions: **a single point does not control a limit**.

### A quick comparison table of evaluation approaches

| Situation at x = a | What substitution gives | Typical tool | What it means |
| --- | --- | --- | --- |
| f(a) defined, no “weirdness” | a number | Substitute | Limit usually equals that number |
| Division with h(a) = 0, g(a) ≠ 0 | ±∞ or undefined | One-sided check | Limit might diverge or not exist |
| 0/0 | indeterminate | factor/cancel, rationalize | Simplify to reveal near behavior |
| Jump or mismatch from left/right | two different numbers | compute one-sided limits | two-sided limit does not exist |

## Core Mechanic 2: One-Sided Limits, Non-Existence, and Infinite Limits

### Why one-sided limits are necessary

Sometimes “approach a” is ambiguous because the function behaves differently from the left and from the right. To capture that, we define:

- •Left-hand limit: lim\_{x → a⁻} f(x)
- •Right-hand limit: lim\_{x → a⁺} f(x)

The two-sided limit exists **only if both one-sided limits exist and are equal**:

If lim\_{x → a⁻} f(x) = L and lim\_{x → a⁺} f(x) = L,

then lim\_{x → a} f(x) = L.

If they differ, the limit does not exist.

### Example: a jump discontinuity

Define:

f(x) =

- •0, for x < 0
- •1, for x ≥ 0

Then:

lim\_{x → 0⁻} f(x) = 0

lim\_{x → 0⁺} f(x) = 1

Since 0 ≠ 1,

lim\_{x → 0} f(x) does not exist.

This is not about being “undefined”; f(0) exists (it’s 1). The limit fails because there is no single output value the function approaches from both sides.

### Infinite limits (blowing up)

Some functions grow without bound as x approaches a point. We express this with ±∞:

lim\_{x → a} f(x) = ∞

This does **not** mean the limit is a real number. It means f(x) becomes arbitrarily large.

Example:

f(x) = 1/x².

As x → 0, 1/x² → ∞ from both sides (because x² is always positive).

So:

lim\_{x → 0} 1/x² = ∞.

But with f(x) = 1/x:

lim\_{x → 0⁻} 1/x = −∞

lim\_{x → 0⁺} 1/x = ∞

The one-sided behaviors disagree, so:

lim\_{x → 0} 1/x does not exist.

### Limits at boundaries and “approaching infinity”

Sometimes you approach a boundary point of the domain (like x → 0⁺ for √x), or you study end behavior:

lim\_{x → ∞} f(x), lim\_{x → −∞} f(x).

These are still limits: “x grows without bound” is another form of “input approaches a target” (the target is not a finite number).

Example:

lim\_{x → ∞} \frac{1}{x} = 0.

Interpretation: you can make 1/x as close to 0 as you want by taking x sufficiently large.

### A practical checklist for “does the limit exist?”

When asked about lim\_{x → a} f(x):

1) Check if both sides are relevant (is the function defined near a on both sides?).

2) Compute lim\_{x → a⁻} f(x) and lim\_{x → a⁺} f(x).

3) If they match to a finite L, the limit is L.

4) If they both go to ∞ (or both to −∞), describe it as an infinite limit.

5) If they disagree, the limit does not exist.

This checklist prevents a common error: assuming “a limit exists unless something is undefined.”

## Applications and Connections: Why Limits Are the Foundation

### Derivatives: slope from “secant” to “tangent”

A derivative is defined using a limit. The slope of the secant line between x = a and x = a + h is:

m\_secant = \frac{f(a + h) − f(a)}{h}.

The instantaneous slope (tangent slope) is what this approaches as h → 0:

f′(a) = lim\_{h → 0} \frac{f(a + h) − f(a)}{h}.

Notice the same theme: we can’t just plug in h = 0 because that gives 0/0. Limits tell us what the expression approaches.

### Continuity: “no breaks” is really “limit equals value”

A function is continuous at a (informally) if the graph doesn’t tear there. Formally, one key condition is:

lim\_{x → a} f(x) = f(a).

So continuity is not separate from limits; it’s built from them.

### Big O notation: limits as asymptotic comparison

In algorithm analysis, we care about growth as n → ∞. Limits formalize “dominates” comparisons. A classic comparison is:

lim\_{n → ∞} \frac{n}{n²} = lim\_{n → ∞} \frac{1}{n} = 0.

Interpretation: n grows much more slowly than n²; in asymptotic terms, n is negligible compared to n².

Even if Big O has its own formal definition, limit intuition is a huge help for understanding it.

### Law of Large Numbers: convergence is a limit idea

In probability, you’ll meet statements like:

As n → ∞, the sample mean \bar{X}\_n approaches the expected value μ.

That is a limit/convergence claim: a sequence of random quantities gets arbitrarily close to μ with high probability (formal versions use probability language, but the “approach” idea is the same).

### Unifying idea: local vs global information

Limits are how math turns “zooming in” (local behavior near a point) into reliable statements. Many advanced concepts are just refinements of this:

- •derivatives (local slope)
- •integrals (limit of sums)
- •series (limit of partial sums)
- •asymptotics (limit comparisons)

If you understand limits as *controlled approach*, you’ll recognize the same pattern everywhere.

## Worked Examples (3)

### A removable discontinuity: canceling a factor

Compute lim\_{x → 3} (x² − 9)/(x − 3).

1. Direct substitution gives (3² − 9)/(3 − 3) = 0/0, which is indeterminate.
2. Factor the numerator:

   x² − 9 = (x − 3)(x + 3).
3. Rewrite for x ≠ 3:

   (x² − 9)/(x − 3) = (x − 3)(x + 3)/(x − 3) = x + 3.
4. Now take the limit of the simplified expression:

   lim\_{x → 3} (x + 3) = 6.

**Insight:** The original expression is undefined at x = 3, but the limit still exists because limits depend on values arbitrarily near 3. Canceling reveals the nearby behavior.

### A piecewise function: one-sided limits decide existence

Let f(x) = { x + 2 if x < 1; 4 − x if x ≥ 1 }. Find lim\_{x → 1} f(x) and f(1).

1. Compute the left-hand limit:

   lim\_{x → 1⁻} f(x) = lim\_{x → 1⁻} (x + 2) = 3.
2. Compute the right-hand limit:

   lim\_{x → 1⁺} f(x) = lim\_{x → 1⁺} (4 − x) = 3.
3. Since both one-sided limits exist and are equal, the two-sided limit exists:

   lim\_{x → 1} f(x) = 3.
4. Now compute the function value at 1. Because x = 1 uses the second rule:

   f(1) = 4 − 1 = 3.

**Insight:** Two-sided limits are agreements between the left and right behaviors. Piecewise definitions often make this explicit and easy to check.

### Rationalizing to remove 0/0

Compute lim\_{x → 0} (√(x + 9) − 3)/x.

1. Direct substitution gives (√9 − 3)/0 = 0/0, indeterminate.
2. Multiply numerator and denominator by the conjugate:

   (√(x + 9) − 3)/x · (√(x + 9) + 3)/(√(x + 9) + 3).
3. Simplify the numerator using difference of squares:

   (√(x + 9) − 3)(√(x + 9) + 3) = (x + 9) − 9 = x.
4. Now the expression becomes:

   x / ( x(√(x + 9) + 3) ) = 1/(√(x + 9) + 3), for x ≠ 0.
5. Take the limit:

   lim\_{x → 0} 1/(√(x + 9) + 3) = 1/(3 + 3) = 1/6.

**Insight:** Rationalizing converts a root difference into a linear factor that cancels with x, revealing a stable nearby value.

## Key Takeaways

- ✓

  lim\_{x → a} f(x) = L means f(x) can be made arbitrarily close to L by taking x sufficiently close to a (not necessarily equal).
- ✓

  Limits depend on values near a; changing f(a) alone does not change the limit.
- ✓

  Direct substitution works when the function behaves nicely at a, but 0/0 signals you should simplify first.
- ✓

  Factor-and-cancel and rationalizing are standard algebraic tools to evaluate limits that appear indeterminate.
- ✓

  One-sided limits lim\_{x → a⁻} and lim\_{x → a⁺} must agree for the two-sided limit to exist.
- ✓

  Infinite limits (→ ∞ or → −∞) describe unbounded growth near a; they are not real-number limits.
- ✓

  Limits underpin derivatives (h → 0), continuity (limit equals value), asymptotics (n → ∞), and convergence ideas in probability.

## Common Mistakes

- ✗

  Treating 0/0 as an answer instead of an indeterminate form that requires simplification.
- ✗

  Assuming lim\_{x → a} f(x) = f(a) even when f(a) is undefined or the function has a jump.
- ✗

  Forgetting to check left-hand and right-hand limits before claiming a two-sided limit exists.
- ✗

  Thinking an infinite limit (∞) is a normal number rather than a statement of unbounded growth.

## Practice

easy

Compute lim\_{x → 5} (x² − 25)/(x − 5).

**Hint:** Factor x² − 25 as a difference of squares, then cancel (x − 5).

Show solution

x² − 25 = (x − 5)(x + 5). For x ≠ 5,

(x² − 25)/(x − 5) = x + 5.

So lim\_{x → 5} (x² − 25)/(x − 5) = 10.

medium

Let f(x) = { 2x if x < 2; x + 1 if x ≥ 2 }. Does lim\_{x → 2} f(x) exist? If so, find it.

**Hint:** Compute lim\_{x → 2⁻} and lim\_{x → 2⁺} separately.

Show solution

Left-hand: lim\_{x → 2⁻} 2x = 4.

Right-hand: lim\_{x → 2⁺} (x + 1) = 3.

Since 4 ≠ 3, lim\_{x → 2} f(x) does not exist.

hard

Compute lim\_{x → 0} (√(1 + x) − 1)/x.

**Hint:** Multiply by the conjugate √(1 + x) + 1 to eliminate the square root in the numerator.

Show solution

(√(1 + x) − 1)/x · (√(1 + x) + 1)/(√(1 + x) + 1)

= ((1 + x) − 1) / ( x(√(1 + x) + 1) )

= x / ( x(√(1 + x) + 1) )

= 1/(√(1 + x) + 1), for x ≠ 0.

Taking x → 0 gives 1/(1 + 1) = 1/2.

## Connections

Next nodes you can unlock with this:

- •[Derivatives](/tech-tree/derivatives-basic/) — defined as a limit of difference quotients as h → 0.
- •[Continuity](/tech-tree/continuity/) — continuity at a is essentially lim\_{x → a} f(x) = f(a).
- •[Big O Notation](/tech-tree/big-o/) — asymptotic comparisons often use limits as n → ∞.
- •[Law of Large Numbers](/tech-tree/law-large-numbers/) — convergence statements are limit ideas for sequences (often as n → ∞).

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
