---
title: Fundamental Theorem of Calculus
description: Connection between differentiation and integration.
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
permalink: /tech-tree/fundamental-theorem/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Fundamental Theorem of Calculus

CalculusDifficulty: ★★☆☆☆Depth: 4Unlocks: 0

Connection between differentiation and integration.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Definite integral as an accumulation function (F(x) = integral from a to x of f(t) dt, accumulating signed area)
- -Antiderivative (primitive): a function F whose derivative equals f (F' = f)
- -Derivative as instantaneous rate of change (the operation that returns a function's instantaneous slope)

## Key Symbols & Notation

Integral with limits: '∫\_a^x f(t) dt'Derivative operator: 'd/dx'

## Essential Relationships

- -FTC Part 1: d/dx [∫\_a^x f(t) dt] = f(x) for continuous f (derivative of accumulation equals the integrand)
- -FTC Part 2 (Evaluation theorem): If F' = f on [a,b], then ∫\_a^b f(x) dx = F(b) - F(a)

## Prerequisites (1)

[Integrals6 atoms](/tech-tree/integrals-basic/)

Advanced Learning Details

### Graph Position

41

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

4

Chain Length

### Cognitive Load

7

Atomic Elements

24

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (9)

- - Accumulation function defined by a variable upper-limit definite integral: F(x) = ∫\_a^x f(t) dt
- - The derivative of an accumulation function recovers the integrand (FTC Part 1): F'(x) = f(x)
- - Evaluation (Newton–Leibniz) formula (FTC Part 2): a definite integral can be computed as F(b) − F(a) where F is any antiderivative of f
- - The variable of integration is a dummy variable (e.g., t in ∫\_a^x f(t) dt) and can be renamed without changing the value
- - Orientation of integral limits: swapping lower and upper limits changes the sign of the definite integral
- - Differentiating an integral with a variable limit requires the chain rule when the limit is a function g(x): d/dx ∫\_a^{g(x)} f(t) dt = f(g(x))·g'(x)
- - Constants of integration cancel when evaluating definite integrals via antiderivatives (so choice of antiderivative differs only by an additive constant)
- - Continuity condition for FTC: if f is continuous on [a,b] then the accumulation function is differentiable and the FTC statements apply
- - Practical computational role of the FTC: use antiderivatives to evaluate limits of Riemann sums/compute definite integrals efficiently

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

You already know two powerful calculus tools: derivatives (instantaneous rate of change) and definite integrals (accumulated area). The Fundamental Theorem of Calculus (FTC) is the bridge that explains why these two ideas are secretly the same process viewed from opposite directions.

TL;DR:

FTC has two linked parts: (1) If you build an “accumulation function” F(x) = ∫ₐˣ f(t) dt, then F′(x) = f(x). (2) If F is any antiderivative of f, then ∫ₐᵇ f(x) dx = F(b) − F(a). Together they turn hard area problems into endpoint subtraction and explain why antiderivatives matter.

## What Is the Fundamental Theorem of Calculus?

### Why this theorem exists (motivation)

Before FTC, you might experience calculus as two separate worlds:

- •**Derivatives**: turn a function into its instantaneous slope / rate function.
- •**Definite integrals**: turn a function into a single number measuring net accumulation (signed area).

FTC answers a natural question:

> If integration is “adding up tiny pieces,” and differentiation measures the “instantaneous change,” are these operations related?

They are related in the strongest possible way: **integration and differentiation are inverse processes** (up to a constant).

### The statement (two parts)

FTC is commonly presented in two parts.

#### FTC Part 1 (Accumulation → derivative)

Let fff be continuous on an interval containing aaa. Define an accumulation function

F(x)=∫axf(t) dt.F(x) = \int\_a^x f(t)\,dt.F(x)=∫ax​f(t)dt.

Then

F′(x)=f(x).F'(x) = f(x).F′(x)=f(x).

Interpretation: **If $F(x)$ measures “area accumulated up to $x$,” then the rate at which that area grows at position $x$ equals the height of the curve there.**

#### FTC Part 2 (Antiderivative → definite integral)

If fff is continuous on [a,b][a,b][a,b] and FFF is any antiderivative of fff (meaning F′(x)=f(x)F'(x)=f(x)F′(x)=f(x)), then

∫abf(x) dx=F(b)−F(a).\int\_a^b f(x)\,dx = F(b) - F(a).∫ab​f(x)dx=F(b)−F(a).

Interpretation: **Net accumulated change equals the antiderivative’s endpoint difference.**

### A quick “two-way bridge” picture

- •Part 1: Start with an integral that depends on xxx → differentiate → get back f(x)f(x)f(x).
- •Part 2: Start with f(x)f(x)f(x) → find an antiderivative FFF → evaluate at endpoints → get the definite integral.

### Visual intuition (diagram you can map to the interactive canvas)

Imagine the interactive canvas shows the curve y=f(x)y=f(x)y=f(x), a fixed vertical line at x=ax=ax=a, and a movable vertical line at xxx.

As you drag xxx to the right, you shade the region under fff from aaa to xxx. The shaded area is F(x)F(x)F(x).

**Canvas state mapping**:

- •State A: curve fff, left bound aaa, right bound xxx, shaded area.
- •State B: a readout showing F(x)F(x)F(x) as a number.
- •State C: a second plot showing the graph of FFF being traced as you move xxx.

The key claim of Part 1 is that **the slope of the traced $F$ graph at the current $x$ equals the current height $f(x)$.**

That is the heart of FTC: slope-of-area equals height-of-curve.

## Core Mechanic 1: FTC Part 1 — The “Thin Slice” Argument (Accumulation Functions)

### Why Part 1 is true (intuition before formulas)

Think of F(x)=∫axf(t) dtF(x)=\int\_a^x f(t)\,dtF(x)=∫ax​f(t)dt as “net area accumulated.”

If you increase xxx by a tiny amount hhh, you add a **thin vertical slice** of area from xxx to x+hx+hx+h.

If hhh is very small, that slice’s area is approximately a rectangle:

- •width ≈ hhh
- •height ≈ f(x)f(x)f(x) (because fff doesn’t change much over a tiny interval)

So the added area is approximately f(x) hf(x)\,hf(x)h.

But the added area is also exactly F(x+h)−F(x)F(x+h)-F(x)F(x+h)−F(x).

So we expect

F(x+h)−F(x)≈f(x) h,F(x+h)-F(x) \approx f(x)\,h,F(x+h)−F(x)≈f(x)h,

which implies

F(x+h)−F(x)h≈f(x).\frac{F(x+h)-F(x)}{h} \approx f(x).hF(x+h)−F(x)​≈f(x).

Taking the limit as h→0h\to 0h→0 gives F′(x)=f(x)F'(x)=f(x)F′(x)=f(x).

### Inline diagram 1: “thin slice” picture

Use this mental picture even without the canvas.

```
          y
          ^
          |
          |          /\
          |         /  \        curve y=f(x)
          |        /    \
          |_______/______\____________> x
                 a   x  x+h

        Shaded area from a to x is F(x)
        Thin slice from x to x+h has area ≈ f(x)·h
```

**Canvas tie-in:** In an interactive version, the thin slice is the last sliver of shaded region as you nudge xxx to x+hx+hx+h.

### Show the work (a careful derivation)

Start with

F(x)=∫axf(t) dt.F(x) = \int\_a^x f(t)\,dt.F(x)=∫ax​f(t)dt.

Compute the difference:

F(x+h)−F(x)=∫ax+hf(t) dt−∫axf(t) dt=∫xx+hf(t) dt.F(x+h)-F(x)
= \int\_a^{x+h} f(t)\,dt - \int\_a^x f(t)\,dt
= \int\_x^{x+h} f(t)\,dt.F(x+h)−F(x)=∫ax+h​f(t)dt−∫ax​f(t)dt=∫xx+h​f(t)dt.

Now form the difference quotient:

F(x+h)−F(x)h=1h∫xx+hf(t) dt.\frac{F(x+h)-F(x)}{h} = \frac{1}{h}\int\_x^{x+h} f(t)\,dt.hF(x+h)−F(x)​=h1​∫xx+h​f(t)dt.

If fff is continuous, then on the tiny interval [x,x+h][x, x+h][x,x+h], f(t)f(t)f(t) is close to f(x)f(x)f(x).

A standard argument (using the Mean Value Theorem for Integrals) says there exists some c∈[x,x+h]c\in[x,x+h]c∈[x,x+h] such that

∫xx+hf(t) dt=f(c) (h).\int\_x^{x+h} f(t)\,dt = f(c)\,(h).∫xx+h​f(t)dt=f(c)(h).

So

1h∫xx+hf(t) dt=f(c).\frac{1}{h}\int\_x^{x+h} f(t)\,dt = f(c).h1​∫xx+h​f(t)dt=f(c).

As h→0h\to 0h→0, the point c→xc\to xc→x, and by continuity f(c)→f(x)f(c)\to f(x)f(c)→f(x). Therefore

F′(x)=lim⁡h→0F(x+h)−F(x)h=f(x).F'(x) = \lim\_{h\to 0} \frac{F(x+h)-F(x)}{h} = f(x).F′(x)=h→0lim​hF(x+h)−F(x)​=f(x).

### What Part 1 *does not* say

- •It does **not** say ∫f(x) dx=f(x)\int f(x)\,dx = f(x)∫f(x)dx=f(x).
- •It does **not** say “integral cancels derivative” without conditions.

It says something precise:

> If you define FFF as the integral from a constant aaa up to the variable endpoint xxx, then differentiating returns the original integrand.

### A pacing checkpoint: interpret FFF as a new function

When you see

F(x)=∫axf(t) dt,F(x)=\int\_a^x f(t)\,dt,F(x)=∫ax​f(t)dt,

read it as: “FFF is a function whose input is the upper limit.”

So FFF has its own graph, its own slope, and its own values.

In the interactive canvas, you can imagine two linked plots:

- •Plot 1: f(x)f(x)f(x) with shaded area up to xxx.
- •Plot 2: F(x)F(x)F(x) being drawn point-by-point as xxx moves.

FTC Part 1 is the rule that synchronizes these plots: **the slope on Plot 2 equals the height on Plot 1**.

## Core Mechanic 2: FTC Part 2 — Antiderivatives and the Endpoint Rule

### Why Part 2 matters (motivation)

Definite integrals *look* like they should require adding infinitely many tiny rectangles.

But in practice, we almost never compute them that way.

FTC Part 2 is the practical miracle:

> If you can find any antiderivative FFF of fff, then the definite integral is just F(b)−F(a)F(b)-F(a)F(b)−F(a).

This turns an accumulation problem into an **endpoint subtraction problem**.

### Connecting Part 2 to Part 1

Part 1 gives you a way to *create* an antiderivative.

Define

G(x)=∫axf(t) dt.G(x)=\int\_a^x f(t)\,dt.G(x)=∫ax​f(t)dt.

Then Part 1 says G′(x)=f(x)G'(x)=f(x)G′(x)=f(x). So GGG is an antiderivative of fff.

Now evaluate GGG at bbb:

G(b)=∫abf(t) dt.G(b) = \int\_a^b f(t)\,dt.G(b)=∫ab​f(t)dt.

Also, G(a)=∫aaf(t) dt=0G(a)=\int\_a^a f(t)\,dt=0G(a)=∫aa​f(t)dt=0.

So

∫abf(t) dt=G(b)−G(a).\int\_a^b f(t)\,dt = G(b)-G(a).∫ab​f(t)dt=G(b)−G(a).

But any two antiderivatives differ by a constant. If F′(x)=f(x)F'(x)=f(x)F′(x)=f(x), then F(x)=G(x)+CF(x)=G(x)+CF(x)=G(x)+C.

So

F(b)−F(a)=(G(b)+C)−(G(a)+C)=G(b)−G(a)=∫abf(t) dt.F(b)-F(a) = (G(b)+C)-(G(a)+C)=G(b)-G(a)=\int\_a^b f(t)\,dt.F(b)−F(a)=(G(b)+C)−(G(a)+C)=G(b)−G(a)=∫ab​f(t)dt.

That’s Part 2.

### Inline diagram 2: “area-to-antiderivative endpoints”

Think of FFF as a height function whose change equals area under fff.

```
F(x)
^
|            • (b, F(b))
|          /
|        /
|      /
|  • (a, F(a))
+----------------------------> x
   a                          b

Vertical change: F(b)-F(a)
Equals signed area under f from a to b.
```

**Canvas tie-in:** Imagine toggling a mode where instead of shading area under fff, you watch a point move on the graph of an antiderivative FFF. The theorem says the *vertical difference* between the endpoint values equals the shaded area you would have gotten.

### Signed area and orientation

Remember the definite integral is **signed**:

- •Area above the xxx-axis contributes positive.
- •Area below contributes negative.

FTC Part 2 preserves that: if fff is negative on much of [a,b][a,b][a,b], then F(b)−F(a)F(b)-F(a)F(b)−F(a) will reflect a net decrease.

Also note the direction:

∫baf(x) dx=−∫abf(x) dx.\int\_b^a f(x)\,dx = -\int\_a^b f(x)\,dx.∫ba​f(x)dx=−∫ab​f(x)dx.

That matches the endpoint rule:

F(a)−F(b)=−(F(b)−F(a)).F(a)-F(b)=-(F(b)-F(a)).F(a)−F(b)=−(F(b)−F(a)).

### A pacing checkpoint: what you’re allowed to do

FTC Part 2 gives a recipe:

1. 1)Find FFF such that F′(x)=f(x)F'(x)=f(x)F′(x)=f(x).
2. 2)Compute F(b)−F(a)F(b)-F(a)F(b)−F(a).

This is why learning antiderivative patterns (power rule, trig, substitution later) is so valuable.

### Mini table: what changes between Part 1 and Part 2

| Idea | Input | Output | Typical use |
| --- | --- | --- | --- |
| FTC Part 1 | A definite integral with variable top: ∫axf(t)dt\int\_a^x f(t)dt∫ax​f(t)dt | A derivative: f(x)f(x)f(x) | Differentiate an accumulation function |
| FTC Part 2 | A function fff and bounds a,ba,ba,b | A number ∫abf\int\_a^b f∫ab​f | Compute a definite integral via antiderivative |

## Application/Connection: How FTC Powers Real Calculus Work

### 1) Turning geometry/accumulation into algebra

Suppose f(x)f(x)f(x) is a rate:

- •water flowing into a tank (liters/min)
- •velocity (m/s)
- •marginal cost ($/unit)

Then the accumulated total from aaa to bbb is

∫abf(x) dx.\int\_a^b f(x)\,dx.∫ab​f(x)dx.

FTC Part 2 says you can compute that total if you can find an antiderivative.

### 2) The derivative of “area so far” is the current rate

This is FTC Part 1 in words:

> If F(x)F(x)F(x) is total accumulated amount up to time xxx, then F′(x)F'(x)F′(x) is the instantaneous rate at time xxx.

So FTC explains why “total” and “rate” are inverse ideas:

- •Differentiate total → get rate.
- •Integrate rate → get total change.

### 3) Interpreting an integral-defined function without computing it fully

Often you’ll see a function defined by an integral that you cannot evaluate in elementary terms, like

F(x)=∫0xe−t2 dt.F(x)=\int\_0^x e^{-t^2}\,dt.F(x)=∫0x​e−t2dt.

Even if you can’t find a closed-form antiderivative, FTC Part 1 still gives

F′(x)=e−x2.F'(x)=e^{-x^2}.F′(x)=e−x2.

That’s extremely useful for analyzing monotonicity, slopes, and local behavior.

### 4) A common “interactive canvas” mental model

If the canvas had three layers:

- •**Layer 1 (Curve):** plot y=f(x)y=f(x)y=f(x)
- •**Layer 2 (Accumulation):** shaded region from aaa to current xxx
- •**Layer 3 (Accumulation graph):** a point (x,F(x))(x, F(x))(x,F(x)) on the graph of the area function

Then moving xxx produces two simultaneous changes:

- •The shaded area increases by a thin slice.
- •The point on FFF rises by exactly that slice area.

FTC Part 1 says: the *instantaneous* rise-per-run of that point equals the current function height.

### 5) The “constant of integration” appears naturally

Indefinite integrals represent families of antiderivatives:

∫f(x) dx=F(x)+C.\int f(x)\,dx = F(x) + C.∫f(x)dx=F(x)+C.

FTC Part 2 avoids worrying about CCC because subtraction cancels it:

(F(b)+C)−(F(a)+C)=F(b)−F(a).(F(b)+C)-(F(a)+C)=F(b)-F(a).(F(b)+C)−(F(a)+C)=F(b)−F(a).

So definite integrals are often cleaner than indefinite integrals: **the constant disappears automatically**.

### 6) Where this connects next

FTC is a hub concept:

- •It justifies many integration techniques (substitution later feels less like magic).
- •It underlies the idea that integrals solve differential equations by “undoing” derivatives.

If you keep one sentence in mind, make it this:

> Net accumulation over an interval equals antiderivative change across the endpoints.

## Worked Examples (3)

### Example 1 (FTC Part 1): Differentiate an accumulation function

Let

F(x)=∫2x(3t2−4t+1) dt.F(x)=\int\_2^x (3t^2 - 4t + 1)\,dt.F(x)=∫2x​(3t2−4t+1)dt.

Find F′(x).

1. Recognize the structure: F(x) is defined as an integral with variable upper limit x.

   So FTC Part 1 applies directly: if F(x)=∫ₐˣ f(t)dt, then F′(x)=f(x).
2. Identify the integrand as f(t)=3t²−4t+1.

   FTC Part 1 says:

   F′(x)=f(x) with t replaced by x.F'(x)=f(x)\text{ with }t\text{ replaced by }x.F′(x)=f(x) with t replaced by x.
3. Compute:

   F′(x)=3x2−4x+1.F'(x)=3x^2-4x+1.F′(x)=3x2−4x+1.

**Insight:** You don’t need to evaluate the integral first. The derivative of “area up to x” is just the curve height at x.

### Example 2 (FTC Part 2): Compute a definite integral using an antiderivative

Compute

∫13(2x−5) dx.\int\_1^3 (2x - 5)\,dx.∫13​(2x−5)dx.

1. Find an antiderivative F of f(x)=2x−5.

   Use basic rules:

   ∫2x dx = x², and ∫(−5) dx = −5x.

   So one antiderivative is

   F(x)=x2−5x.F(x)=x^2-5x.F(x)=x2−5x.
2. Apply FTC Part 2:

   ∫13(2x−5) dx=F(3)−F(1).\int\_1^3 (2x-5)\,dx = F(3)-F(1).∫13​(2x−5)dx=F(3)−F(1).
3. Evaluate endpoints:

   F(3)=32−5⋅3=9−15=−6F(3)=3^2-5\cdot 3=9-15=-6F(3)=32−5⋅3=9−15=−6

   F(1)=12−5⋅1=1−5=−4F(1)=1^2-5\cdot 1=1-5=-4F(1)=12−5⋅1=1−5=−4
4. Subtract:

   F(3)−F(1)=−6−(−4)=−2.F(3)-F(1)=-6-(-4)=-2.F(3)−F(1)=−6−(−4)=−2.

**Insight:** The result is negative because (2x−5) is below the x-axis on much of [1,3]. FTC preserves signed area automatically.

### Example 3 (Mix of both): Use FTC to differentiate a shifted integral

Let

H(x)=∫0x2sin⁡(t) dt.H(x)=\int\_0^{x^2} \sin(t)\,dt.H(x)=∫0x2​sin(t)dt.

Find H′(x).

1. Notice the upper limit is not x but x². We’ll combine FTC Part 1 with the chain rule.
2. Let G(u)=∫₀ᵘ sin(t) dt. Then by FTC Part 1:

   G′(u)=sin⁡(u).G'(u)=\sin(u).G′(u)=sin(u).
3. Now H(x)=G(x²). Differentiate using the chain rule:

   H′(x)=G′(x2)⋅ddx(x2).H'(x)=G'(x^2)\cdot \frac{d}{dx}(x^2).H′(x)=G′(x2)⋅dxd​(x2).
4. Substitute G′(x²)=sin(x²) and d/dx(x²)=2x:

   H′(x)=sin⁡(x2)⋅2x=2xsin⁡(x2).H'(x)=\sin(x^2)\cdot 2x = 2x\sin(x^2).H′(x)=sin(x2)⋅2x=2xsin(x2).

**Insight:** FTC Part 1 tells you the derivative with respect to the upper limit; the chain rule accounts for how the upper limit depends on x.

## Key Takeaways

- ✓

  FTC connects differentiation and integration as inverse processes (up to a constant).
- ✓

  FTC Part 1: If F(x)=∫ₐˣ f(t)dt, then F′(x)=f(x) (slope of accumulated area equals curve height).
- ✓

  FTC Part 2: If F′=f, then ∫ₐᵇ f(x)dx = F(b)−F(a) (definite integrals become endpoint subtraction).
- ✓

  The “thin slice” view explains Part 1: increasing x by h adds an area ≈ f(x)·h.
- ✓

  Definite integrals are signed; negative results correspond to net area below the x-axis.
- ✓

  You can differentiate many integral-defined functions even when the integral has no elementary closed form.
- ✓

  The constant of integration cancels in F(b)−F(a), which is why definite integrals are often simpler than indefinite ones.

## Common Mistakes

- ✗

  Treating ∫ₐˣ f(t)dt as if it were an indefinite integral and forgetting it defines a new function of x.
- ✗

  Forgetting that FTC Part 1 returns f(x), not the antiderivative of f.
- ✗

  Dropping the chain rule when the upper limit is something like x² or 3x+1.
- ✗

  Confusing signed area with geometric area (expecting a nonnegative answer even when f is negative).

## Practice

easy

Let F(x)=∫₋1ˣ (t³+2) dt. Compute F′(x).

**Hint:** FTC Part 1: derivative of integral from a to x is the integrand evaluated at x.

Show solution

Here f(t)=t³+2, so by FTC Part 1:

F′(x)=x3+2.F'(x)=x^3+2.F′(x)=x3+2.

medium

Compute the definite integral ∫₀² (x² − 4x) dx using FTC Part 2.

**Hint:** Find an antiderivative: ∫x² dx = x³/3 and ∫(−4x) dx = −2x².

Show solution

An antiderivative is

F(x)=x33−2x2.F(x)=\frac{x^3}{3}-2x^2.F(x)=3x3​−2x2.

Then

∫02(x2−4x) dx=F(2)−F(0).\int\_0^2 (x^2-4x)\,dx = F(2)-F(0).∫02​(x2−4x)dx=F(2)−F(0).

Compute:

F(2)=83−2⋅4=83−8=8−243=−163,F(0)=0.F(2)=\frac{8}{3}-2\cdot 4=\frac{8}{3}-8=\frac{8-24}{3}=-\frac{16}{3},
\quad F(0)=0.F(2)=38​−2⋅4=38​−8=38−24​=−316​,F(0)=0.

So the integral is −16/3-16/3−16/3.

hard

Let H(x)=∫₁^{3x} \sqrt{1+t} \,dt. Find H′(x).

**Hint:** Think of H(x)=G(3x) where G(u)=∫₁ᵘ √(1+t) dt. Apply FTC Part 1 then chain rule.

Show solution

Define

G(u)=∫1u1+t dt.G(u)=\int\_1^u \sqrt{1+t}\,dt.G(u)=∫1u​1+t​dt.

By FTC Part 1:

G′(u)=1+u.G'(u)=\sqrt{1+u}.G′(u)=1+u​.

Now H(x)=G(3x)H(x)=G(3x)H(x)=G(3x), so

H′(x)=G′(3x)⋅ddx(3x)=1+3x⋅3=31+3x.H'(x)=G'(3x)\cdot \frac{d}{dx}(3x)=\sqrt{1+3x}\cdot 3=3\sqrt{1+3x}.H′(x)=G′(3x)⋅dxd​(3x)=1+3x​⋅3=31+3x​.

## Connections

[Definite Integrals (Riemann Sums)](/tech-tree/definite-integrals-riemann/)

[Antiderivatives and Indefinite Integrals](/tech-tree/antiderivatives/)

[Chain Rule](/tech-tree/chain-rule/)

[Applications: Accumulation and Net Change](/tech-tree/net-change/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
