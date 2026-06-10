---
title: Derivatives
description: Instantaneous rate of change. Slope of tangent line.
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
permalink: /tech-tree/derivatives-basic/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Derivatives

CalculusDifficulty: ★★☆☆☆Depth: 2Unlocks: 91

Instantaneous rate of change. Slope of tangent line.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Instantaneous rate of change at a point
- -Limit of the difference quotient (defining limit)
- -Slope of the tangent line to the graph at a point

## Key Symbols & Notation

f'(a) (derivative of f at a)

## Essential Relationships

- -f'(a) is defined as the limit as h approaches 0 of (f(a+h)-f(a))/h
- -The value f'(a) equals the slope of the tangent line and thus gives the instantaneous rate of change of f at a

## Prerequisites (2)

[Limits5 atoms](/tech-tree/limits/)[Slope and Rate of Change5 atoms](/tech-tree/slope/)

## Unlocks (8)

[Derivative Ruleslvl 2](/tech-tree/derivative-rules/)[Maximum Likelihood Estimationlvl 3](/tech-tree/mle/)[Convex Functionslvl 3](/tech-tree/convexity/)[Integralslvl 2](/tech-tree/integrals-basic/)[Utility Theorylvl 3](/tech-tree/utility-theory/)[Demand Functionslvl 3](/tech-tree/demand-functions/)[Cost Functionslvl 3](/tech-tree/cost-functions/)[Price Elasticitylvl 3](/tech-tree/price-elasticity/)

## Referenced by (6)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (4)

[Time to ValueBusiness

TTV is governed by the rate of value accrual over time; the derivative of cumulative value with respect to time formalizes whether value delivery is accelerating or stalling, which determines whether TTV is short or long](/business/time-to-value/)[DepreciationBusiness

The 'net rate' that determines investment type is literally a derivative - the instantaneous rate of change of asset value over time. Depreciation is a negative derivative, appreciation is positive, and the investment classification depends on their sum's sign.](/business/depreciation/)[overheadBusiness

Detecting overhead means measuring the marginal gain in downstream performance per added τ, which is literally evaluating a discrete derivative and checking when it approaches zero](/business/overhead/)[Book ValueBusiness

The first derivative of book value over time tells you whether it is compounding (positive, increasing) or depreciating (negative). The second derivative tells you if that trend is accelerating or decelerating - the mathematical formalism for 'is this asset gaining or losing value, and how fast?'](/business/book-value/)

### From Money (2)

[Return on EquityMoney

Marginal return on equity measures the sensitivity of returns to capital redeployment](/money/return-on-equity/)[Options BasicsMoney

Option pricing uses calculus derivatives for sensitivity analysis (the Greeks)](/money/options-basics/)

Advanced Learning Details

### Graph Position

28

Depth Cost

91

Fan-Out (ROI)

33

Bottleneck Score

2

Chain Length

### Cognitive Load

6

Atomic Elements

22

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (8)

- - Instantaneous rate of change (value of the rate of change at a single input)
- - Slope of the tangent line (geometric notion of instantaneous slope)
- - Difference quotient as average rate over an interval: (f(x+h)-f(x))/h
- - Derivative at a point (f'(a)) defined via a limit of the difference quotient
- - Derivative as a function (assigns to each x the instantaneous rate f'(x))
- - Differentiability (existence of the derivative at a point or on an interval)
- - Secant line vs tangent line (secant line slopes approximate tangent slope as interval shrinks)
- - Two-sided limit requirement for the derivative (left and right difference-quotient limits must agree)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

If you zoom in far enough on a smooth curve, it starts to look like a straight line. A derivative is the slope of that “best-fit” line at a single point—capturing an instantaneous rate of change.

TL;DR:

The derivative of fff at aaa, written f′(a)f'(a)f′(a), is the limit of slopes of secant lines through (a,f(a))(a,f(a))(a,f(a)) and nearby points. Formally:

f′(a)=lim⁡h→0f(a+h)−f(a)hf'(a)=\lim\_{h\to 0}\frac{f(a+h)-f(a)}{h}f′(a)=h→0lim​hf(a+h)−f(a)​

If the limit exists, the function is differentiable at aaa and the derivative equals the slope of the tangent line there (and the instantaneous rate of change).

## What Is a Derivative?

### The motivation (why we need a new idea)

You already know **average rate of change**: between two points x=ax=ax=a and x=bx=bx=b, the slope is

f(b)−f(a)b−a\frac{f(b)-f(a)}{b-a}b−af(b)−f(a)​

That’s a *two-point* measurement. But many real questions are *one-point* questions:

- •“How fast is the position changing **right now**?” (instantaneous velocity)
- •“How steep is the curve **at this point**?” (tangent slope)
- •“If I nudge xxx a tiny bit, how much does f(x)f(x)f(x) change?” (sensitivity)

To answer those, we take the average rate of change over a smaller and smaller interval and ask whether it approaches a limiting value.

### Definition (difference quotient → limit)

Fix a point aaa. Consider a nearby point a+ha+ha+h (so hhh is a small horizontal step). The slope of the secant line through

- •P=(a,f(a))P=(a, f(a))P=(a,f(a)) and
- •Q=(a+h,f(a+h))Q=(a+h, f(a+h))Q=(a+h,f(a+h))

is

msec(h)=f(a+h)−f(a)(a+h)−a=f(a+h)−f(a)hm\_{\text{sec}}(h)=\frac{f(a+h)-f(a)}{(a+h)-a}=\frac{f(a+h)-f(a)}{h}msec​(h)=(a+h)−af(a+h)−f(a)​=hf(a+h)−f(a)​

If this slope approaches a single number as h→0h \to 0h→0, we define the derivative:

f′(a)=lim⁡h→0f(a+h)−f(a)hf'(a)=\lim\_{h\to 0}\frac{f(a+h)-f(a)}{h}f′(a)=h→0lim​hf(a+h)−f(a)​

This is the **defining limit** (also called the definition via the difference quotient).

### Two interpretations you should hold at the same time

1) **Geometric:** f′(a)f'(a)f′(a) is the slope of the **tangent line** to the graph at x=ax=ax=a.

2) **Dynamic (rate):** f′(a)f'(a)f′(a) is the **instantaneous rate of change** of fff with respect to xxx at x=ax=ax=a.

Both interpretations come from the same limit.

### Units (a quick reality check)

If xxx is measured in seconds and f(x)f(x)f(x) in meters, then

- •Δx\Delta xΔx has units seconds
- •Δf\Delta fΔf has units meters
- •ΔfΔx\frac{\Delta f}{\Delta x}ΔxΔf​ has units meters/second

So f′(a)f'(a)f′(a) has the same units as a speed. This “units check” is one of the simplest ways to catch mistakes.

### Supporting static diagram (to reduce cognitive load)

**Static diagram to include in the lesson UI**: a coordinate plane with the curve y=f(x)y=f(x)y=f(x), points P=(a,f(a))P=(a,f(a))P=(a,f(a)) and Q=(a+h,f(a+h))Q=(a+h,f(a+h))Q=(a+h,f(a+h)), the secant line through PPP and QQQ, and labels for:

- •horizontal change: hhh
- •vertical change: f(a+h)−f(a)f(a+h)-f(a)f(a+h)−f(a)
- •secant slope: f(a+h)−f(a)h\frac{f(a+h)-f(a)}{h}hf(a+h)−f(a)​

This diagram should remain visible while the definition is introduced so the symbols feel anchored to geometry.

### What the interactive canvas should show (visual layer)

Your interactive canvas should make the limit feel *physical*.

**Canvas scene A: Secant-to-tangent animation**

- •Plot a smooth function, e.g. f(x)=x2f(x)=x^2f(x)=x2.
- •Show point PPP fixed at x=ax=ax=a.
- •Show point QQQ at x=a+hx=a+hx=a+h with a slider for hhh.
- •Draw the secant line PQ‾\overline{PQ}PQ​.
- •Display the numeric value of msec(h)m\_{\text{sec}}(h)msec​(h).
- •As the learner drags h→0h \to 0h→0, animate Q→PQ \to PQ→P and show the secant line rotate toward the tangent line.

**Canvas scene B: One-sided convergence**

- •Add a toggle: “Approach from the right (h→0+h\to 0^+h→0+)” vs “Approach from the left (h→0−h\to 0^-h→0−)”.
- •Show two slopes: msec(h>0)m\_{\text{sec}}(h>0)msec​(h>0) and msec(h<0)m\_{\text{sec}}(h<0)msec​(h<0).
- •Emphasize: differentiable requires both sides approach the same value.

**Canvas scene C: Non-differentiable corner/cusp toggle**

- •Toggle function between:
- •f(x)=∣x∣f(x)=|x|f(x)=∣x∣ (corner at 0)
- •f(x)=x3f(x)=\sqrt[3]{x}f(x)=3x​ (vertical tangent at 0)
- •Keep the same secant-to-tangent mechanics.
- •Show that left and right slopes disagree for ∣x∣|x|∣x∣ and that slopes blow up for x3\sqrt[3]{x}3x​.

These visuals directly support the three atomic concepts: instantaneous rate, defining limit, and tangent slope.

## Core Mechanic 1: From Secant Slopes to the Tangent Slope (The Limit Process)

### Start with what you know: secant slope

Pick two x-values: aaa and a+ha+ha+h.

The secant slope is

msec(h)=f(a+h)−f(a)hm\_{\text{sec}}(h)=\frac{f(a+h)-f(a)}{h}msec​(h)=hf(a+h)−f(a)​

This is an *average* rate of change on the interval [a,a+h][a, a+h][a,a+h].

### Shrink the interval (the key move)

To get a *one-point* notion, we shrink the interval by taking hhh smaller and smaller.

- •If h=1h=1h=1, you’re measuring across a wide interval.
- •If h=0.1h=0.1h=0.1, you’re measuring locally.
- •If h=0.001h=0.001h=0.001, you’re extremely local.

The derivative is the number the secant slopes are heading toward—if they head toward a single number at all.

### Why the limit is necessary (not optional)

You might wonder: why not just set h=0h=0h=0 in

f(a+h)−f(a)h?\frac{f(a+h)-f(a)}{h}?hf(a+h)−f(a)​?

Because you would get

f(a)−f(a)0=00\frac{f(a)-f(a)}{0}=\frac{0}{0}0f(a)−f(a)​=00​

and 00\frac{0}{0}00​ is **indeterminate** (it doesn’t have a single value). The limit process asks: *as we approach* the problematic point, does the expression stabilize?

### One-sided limits and differentiability

A subtle but crucial point: h→0h \to 0h→0 means approaching 0 from both sides.

- •Right-hand derivative:

f+′(a)=lim⁡h→0+f(a+h)−f(a)hf'\_+(a)=\lim\_{h\to 0^+}\frac{f(a+h)-f(a)}{h}f+′​(a)=h→0+lim​hf(a+h)−f(a)​

- •Left-hand derivative:

f−′(a)=lim⁡h→0−f(a+h)−f(a)hf'\_-(a)=\lim\_{h\to 0^-}\frac{f(a+h)-f(a)}{h}f−′​(a)=h→0−lim​hf(a+h)−f(a)​

A function is differentiable at aaa only if both exist and are equal:

f′(a) exists   ⟺  f−′(a)=f+′(a)f'(a) \text{ exists } \iff f'\_-(a)=f'\_+(a)f′(a) exists ⟺f−′​(a)=f+′​(a)

This is exactly what your “one-sided slope convergence” canvas should make obvious: you can *see* when the two sides don’t agree.

### Tangent line equation (once you have the slope)

If you know f′(a)f'(a)f′(a), you know the slope of the tangent line at x=ax=ax=a. The tangent line passes through (a,f(a))(a, f(a))(a,f(a)) with slope f′(a)f'(a)f′(a):

y−f(a)=f′(a)(x−a)y - f(a) = f'(a)(x-a)y−f(a)=f′(a)(x−a)

This is often the fastest way to turn “derivative” into a concrete geometric object.

### Micro-change viewpoint (a preview of linear approximation)

When hhh is small, the change in fff is approximately

f(a+h)−f(a)≈f′(a) hf(a+h)-f(a) \approx f'(a)\,hf(a+h)−f(a)≈f′(a)h

This is the intuition behind many applications: derivatives translate a tiny input change into an approximate output change.

### What the interactive canvas should emphasize here

To reinforce the limit idea (instead of treating it as symbolism):

- •Display a table that updates live as hhh changes:

| h | (f(a+h) − f(a))/h |
| --- | --- |
| 1 | ... |
| 0.5 | ... |
| 0.1 | ... |
| 0.01 | ... |

- •The learner should *notice convergence*: the slope values settle.
- •When switching to a corner/cusp example, the table should *fail to settle* or show two different settling values from left vs right.

## Core Mechanic 2: When Derivatives Do (and Don’t) Exist

### Differentiable vs. continuous (don’t merge these)

A common mental trap is to assume:

- •“If the graph has no jumps, it must have a derivative.”

Not always.

**Facts to keep straight:**

- •If fff is differentiable at aaa, then fff is continuous at aaa.
- •But fff can be continuous at aaa and still *not* differentiable there.

So differentiability is a *stronger* condition.

### Three classic ways differentiability can fail

#### 1) Corner (left and right slopes disagree)

Example: f(x)=∣x∣f(x)=|x|f(x)=∣x∣ at x=0x=0x=0.

- •For x>0x>0x>0, the slope is like the line y=xy=xy=x (slope 1).
- •For x<0x<0x<0, the slope is like the line y=−xy=-xy=−x (slope −1).

Compute using the definition:

For h>0h>0h>0:

∣0+h∣−∣0∣h=∣h∣h=hh=1\frac{|0+h|-|0|}{h}=\frac{|h|}{h}=\frac{h}{h}=1h∣0+h∣−∣0∣​=h∣h∣​=hh​=1

For h<0h<0h<0:

∣h∣h=−hh=−1\frac{|h|}{h}=\frac{-h}{h}=-1h∣h∣​=h−h​=−1

So

f+′(0)=1,f−′(0)=−1f'\_+(0)=1,\quad f'\_-(0)=-1f+′​(0)=1,f−′​(0)=−1

They differ, so f′(0)f'(0)f′(0) does not exist.

**Interactive tie-in:** in your corner toggle, the secant line will approach two different tangent candidates depending on direction.

#### 2) Cusp or vertical tangent (slope blows up)

Example: f(x)=x3f(x)=\sqrt[3]{x}f(x)=3x​ at x=0x=0x=0.

Consider the difference quotient:

h3−0h=h1/3h=h−2/3\frac{\sqrt[3]{h}-0}{h}=\frac{h^{1/3}}{h}=h^{-2/3}h3h​−0​=hh1/3​=h−2/3

As h→0h\to 0h→0, h−2/3→∞h^{-2/3}\to \inftyh−2/3→∞. The slope becomes unbounded (vertical tangent). In many calculus courses, we say the derivative does not exist as a finite number.

**Interactive tie-in:** your slope readout should grow very large in magnitude as hhh shrinks.

#### 3) Discontinuity (jumps or holes)

If fff isn’t continuous at aaa, it cannot be differentiable there.

This is less subtle visually—your curve breaks—so it’s a good “sanity check” case.

### Differentiability is local smoothness

A useful phrase: **differentiable at $a$ means the graph is locally well-approximated by a line near $a$.**

That’s why the “zoom in, it becomes a line” intuition works. A corner never becomes a single line no matter how much you zoom; it keeps its sharpness.

### A quick comparison table

| Feature at x=a | Continuous? | Derivative exists? | What you see |
| --- | --- | --- | --- |
| Smooth curve | Yes | Yes | One clear tangent slope |
| Corner ( | x | ) | Yes | No | Two different one-sided slopes |
| Vertical tangent (∛x) | Yes | No (finite) | Slopes blow up toward ±∞ |
| Jump discontinuity | No | No | Break in graph |

### What the canvas should show in this section

To make “failure modes” memorable:

- •Keep the same point PPP and slider for hhh.
- •Let learners switch functions with a toggle.
- •Show both one-sided secant slopes simultaneously (color-code left vs right).
- •Add a small indicator:
- •“Differentiable here: yes/no”
- •If no, show reason: “left/right mismatch” or “slope unbounded”.

## Application/Connection: What Derivatives Enable

### Derivatives as a sensitivity tool

At a point aaa, the derivative tells you how sensitive the output is to tiny input changes.

If Δx\Delta xΔx is small, then

Δf≈f′(a) Δx\Delta f \approx f'(a)\,\Delta xΔf≈f′(a)Δx

This is the bridge from geometry to practical estimation.

**Example intuition:** If a cost function has derivative 5 dollars/unit at the current production level, then producing one more unit increases cost by about $5.

### Derivatives as slope fields for behavior

Even before learning derivative “rules,” knowing that f′(x)f'(x)f′(x) is slope gives a powerful way to interpret a graph:

- •Where f′(x)>0f'(x)>0f′(x)>0, the function is increasing.
- •Where f′(x)<0f'(x)<0f′(x)<0, the function is decreasing.
- •Where f′(x)=0f'(x)=0f′(x)=0, the tangent is horizontal (possible maxima/minima).

This connects directly to optimization ideas used everywhere (including machine learning).

### Why this node unlocks the next nodes

#### Link to Derivative Rules

The definition is conceptually perfect but computationally slow. The next node ([Derivative Rules](/tech-tree/derivative-rules/)) gives shortcuts (power/product/quotient/chain rules). Those rules are *justified* because they match what the limit definition produces.

#### Link to Maximum Likelihood Estimation (MLE)

In MLE, you maximize a likelihood (or log-likelihood) with respect to parameters. “Maximize” often means “take derivative, set it to zero, solve.” The derivative is what turns “best parameter” into an equation you can solve.

#### Link to Convex Functions

Convexity uses derivatives to formalize “curves that bend upward.” For differentiable functions, one hallmark is that the derivative is increasing. So understanding f′(x)f'(x)f′(x) as slope makes convexity feel natural.

#### Link to Integrals

Integrals and derivatives are paired by the Fundamental Theorem of Calculus. Informally: differentiation measures *instantaneous change*, integration accumulates change. This node provides the “change” half of that story.

### A small, concrete bridge: tangent line approximation

Once you can compute f′(a)f'(a)f′(a), you can approximate fff near aaa by its tangent line:

f(x)≈f(a)+f′(a)(x−a)f(x) \approx f(a) + f'(a)(x-a)f(x)≈f(a)+f′(a)(x−a)

This idea appears constantly later: numerical methods, error estimates, optimization steps, and more.

## Worked Examples (3)

### Compute a derivative from the definition: f(x)=x² at an arbitrary point a

Find f′(a)f'(a)f′(a) for f(x)=x2f(x)=x^2f(x)=x2 using the defining limit.

Goal: turn the limit into algebra and simplify until the limit is easy.

1. Start with the definition:

   f′(a)=lim⁡h→0f(a+h)−f(a)hf'(a)=\lim\_{h\to 0}\frac{f(a+h)-f(a)}{h}f′(a)=h→0lim​hf(a+h)−f(a)​
2. Plug in f(x)=x2f(x)=x^2f(x)=x2:

   f′(a)=lim⁡h→0(a+h)2−a2hf'(a)=\lim\_{h\to 0}\frac{(a+h)^2-a^2}{h}f′(a)=h→0lim​h(a+h)2−a2​
3. Expand (a+h)2(a+h)^2(a+h)2:

   (a+h)2=a2+2ah+h2(a+h)^2=a^2+2ah+h^2(a+h)2=a2+2ah+h2

   So the numerator becomes:

   (a2+2ah+h2)−a2=2ah+h2(a^2+2ah+h^2)-a^2=2ah+h^2(a2+2ah+h2)−a2=2ah+h2
4. Factor out hhh:

   2ah+h2h=h(2a+h)h=2a+h\frac{2ah+h^2}{h}=\frac{h(2a+h)}{h}=2a+hh2ah+h2​=hh(2a+h)​=2a+h

   (For h≠0h\neq 0h=0 this cancellation is valid; the limit cares about values near 0, not at 0.)
5. Now take the limit:

   f′(a)=lim⁡h→0(2a+h)=2af'(a)=\lim\_{h\to 0}(2a+h)=2af′(a)=h→0lim​(2a+h)=2a

**Insight:** The limit definition often works by algebraically canceling the problematic hhh in the denominator. For polynomials like x2x^2x2, the derivative emerges cleanly: f′(a)=2af'(a)=2af′(a)=2a.

### Non-differentiability at a corner: f(x)=|x| at x=0

Show that f′(0)f'(0)f′(0) does not exist for f(x)=∣x∣f(x)=|x|f(x)=∣x∣.

Strategy: compute the right-hand and left-hand derivatives and compare.

1. Start with the difference quotient at a=0a=0a=0:

   f(0+h)−f(0)h=∣h∣−0h=∣h∣h\frac{f(0+h)-f(0)}{h}=\frac{|h|-0}{h}=\frac{|h|}{h}hf(0+h)−f(0)​=h∣h∣−0​=h∣h∣​
2. Right-hand derivative (approach with h>0h>0h>0):

   If h>0h>0h>0, then ∣h∣=h|h|=h∣h∣=h, so

   ∣h∣h=hh=1\frac{|h|}{h}=\frac{h}{h}=1h∣h∣​=hh​=1

   Thus

   f+′(0)=lim⁡h→0+1=1f'\_+(0)=\lim\_{h\to 0^+} 1 = 1f+′​(0)=h→0+lim​1=1
3. Left-hand derivative (approach with h<0h<0h<0):

   If h<0h<0h<0, then ∣h∣=−h|h|=-h∣h∣=−h, so

   ∣h∣h=−hh=−1\frac{|h|}{h}=\frac{-h}{h}=-1h∣h∣​=h−h​=−1

   Thus

   f−′(0)=lim⁡h→0−(−1)=−1f'\_-(0)=\lim\_{h\to 0^-} (-1) = -1f−′​(0)=h→0−lim​(−1)=−1
4. Compare:

   f+′(0)=1≠−1=f−′(0)f'\_+(0)=1 \neq -1 = f'\_-(0)f+′​(0)=1=−1=f−′​(0)

   Therefore, the two-sided limit does not exist, so f′(0)f'(0)f′(0) does not exist.

**Insight:** A corner is exactly the situation where the curve has two competing tangent directions. The derivative requires a single slope; disagreement between one-sided slopes means ‘not differentiable.’

### Tangent line from the derivative: f(x)=x² at x=3

Use the derivative to find the equation of the tangent line to y=x2y=x^2y=x2 at x=3x=3x=3.

You can use the result from Example 1: if f(x)=x2f(x)=x^2f(x)=x2, then f′(x)=2xf'(x)=2xf′(x)=2x (so f′(3)=6f'(3)=6f′(3)=6).

1. Compute the point on the curve:

   f(3)=32=9f(3)=3^2=9f(3)=32=9

   So the point is (3,9)(3,9)(3,9).
2. Compute the slope of the tangent line:

   f′(x)=2x⇒f′(3)=6f'(x)=2x \Rightarrow f'(3)=6f′(x)=2x⇒f′(3)=6
3. Use point-slope form:

   y−9=6(x−3)y-9=6(x-3)y−9=6(x−3)
4. Simplify (optional):

   y−9=6x−18⇒y=6x−9y-9=6x-18 \Rightarrow y=6x-9y−9=6x−18⇒y=6x−9

**Insight:** Once you know the derivative at a point, geometry becomes straightforward: slope + point gives the tangent line immediately.

## Key Takeaways

- ✓

  The derivative at a point aaa is defined by a limit of secant slopes: $f′(a)=lim⁡h→0f(a+h)−f(a)hf'(a)=\lim\_{h\to 0}\frac{f(a+h)-f(a)}{h}f′(a)=limh→0​hf(a+h)−f(a)​$
- ✓

  Geometrically, f′(a)f'(a)f′(a) is the slope of the tangent line to y=f(x)y=f(x)y=f(x) at x=ax=ax=a.
- ✓

  As a rate, f′(a)f'(a)f′(a) measures instantaneous change: small input changes satisfy Δf≈f′(a) Δx\Delta f \approx f'(a)\,\Delta xΔf≈f′(a)Δx.
- ✓

  You cannot compute the derivative by plugging in h=0h=0h=0 directly; the definition requires a limit because the quotient becomes $0/0$.
- ✓

  Differentiability requires left- and right-hand derivatives to exist and match: f−′(a)=f+′(a)f'\_-(a)=f'\_+(a)f−′​(a)=f+′​(a).
- ✓

  Corners (like ∣x∣|x|∣x∣ at 0) and vertical tangents/cusps (like x3\sqrt[3]{x}3x​ at 0) are common reasons a derivative fails to exist.
- ✓

  Given f′(a)f'(a)f′(a), the tangent line is y−f(a)=f′(a)(x−a)y - f(a) = f'(a)(x-a)y−f(a)=f′(a)(x−a).

## Common Mistakes

- ✗

  Trying to evaluate the difference quotient at h=0h=0h=0 (treating $0/0$ as a number) instead of taking a limit.
- ✗

  Assuming ‘continuous’ implies ‘differentiable’—corners and cusps are continuous but not differentiable.
- ✗

  Forgetting that h→0h\to 0h→0 is two-sided; checking only h>0h>0h>0 can miss a corner where one-sided slopes differ.
- ✗

  Mixing up the secant slope (average change over an interval) with the tangent slope (instantaneous change at a point).

## Practice

easy

Use the definition to compute the derivative of f(x)=3x+2f(x)=3x+2f(x)=3x+2 at an arbitrary point aaa.

**Hint:** Compute f(a+h)−f(a)h\frac{f(a+h)-f(a)}{h}hf(a+h)−f(a)​, simplify, then take h→0h\to 0h→0.

Show solution

Start:

f′(a)=lim⁡h→0f(a+h)−f(a)hf'(a)=\lim\_{h\to 0}\frac{f(a+h)-f(a)}{h}f′(a)=h→0lim​hf(a+h)−f(a)​

Compute:

f(a+h)=3(a+h)+2=3a+3h+2f(a+h)=3(a+h)+2=3a+3h+2f(a+h)=3(a+h)+2=3a+3h+2

f(a)=3a+2f(a)=3a+2f(a)=3a+2

Difference quotient:

(3a+3h+2)−(3a+2)h=3hh=3\frac{(3a+3h+2)-(3a+2)}{h}=\frac{3h}{h}=3h(3a+3h+2)−(3a+2)​=h3h​=3

Limit:

f′(a)=lim⁡h→03=3f'(a)=\lim\_{h\to 0}3=3f′(a)=h→0lim​3=3

medium

Find the slope of the tangent line to f(x)=1xf(x)=\frac{1}{x}f(x)=x1​ at x=2x=2x=2 using the definition of the derivative.

**Hint:** Compute 12+h−12h\frac{\frac{1}{2+h}-\frac{1}{2}}{h}h2+h1​−21​​, combine fractions, simplify, then take h→0h\to 0h→0.

Show solution

Definition at a=2a=2a=2:

f′(2)=lim⁡h→012+h−12hf'(2)=\lim\_{h\to 0}\frac{\frac{1}{2+h}-\frac{1}{2}}{h}f′(2)=h→0lim​h2+h1​−21​​

Combine the numerator:

12+h−12=2−(2+h)2(2+h)=−h2(2+h)\frac{1}{2+h}-\frac{1}{2}=\frac{2-(2+h)}{2(2+h)}=\frac{-h}{2(2+h)}2+h1​−21​=2(2+h)2−(2+h)​=2(2+h)−h​

Divide by hhh:

−h2(2+h)h=−h2(2+h)h=−12(2+h)\frac{\frac{-h}{2(2+h)}}{h}=\frac{-h}{2(2+h)h}=-\frac{1}{2(2+h)}h2(2+h)−h​​=2(2+h)h−h​=−2(2+h)1​

Take the limit:

f′(2)=lim⁡h→0(−12(2+h))=−12⋅2=−14f'(2)=\lim\_{h\to 0}\left(-\frac{1}{2(2+h)}\right)=-\frac{1}{2\cdot 2}=-\frac{1}{4}f′(2)=h→0lim​(−2(2+h)1​)=−2⋅21​=−41​

medium

Determine whether f(x)=∣x−1∣f(x)=|x-1|f(x)=∣x−1∣ is differentiable at x=1x=1x=1. Justify using one-sided derivatives (you may use the definition conceptually without heavy algebra).

**Hint:** Shift the |x| corner: ∣x−1∣|x-1|∣x−1∣ has the same shape as ∣x∣|x|∣x∣ but centered at 1. Compare the slope from the left vs right.

Show solution

At x=1x=1x=1, the graph of ∣x−1∣|x-1|∣x−1∣ has a corner (it’s ∣x∣|x|∣x∣ shifted right by 1). For x>1x>1x>1, ∣x−1∣=x−1|x-1|=x-1∣x−1∣=x−1 which has slope 1. For x<1x<1x<1, ∣x−1∣=−(x−1)=1−x|x-1|=-(x-1)=1-x∣x−1∣=−(x−1)=1−x which has slope −1. Since the right-hand derivative is 1 and the left-hand derivative is −1, they do not match. Therefore fff is not differentiable at x=1x=1x=1.

## Connections

- •Next: [Derivative Rules](/tech-tree/derivative-rules/)
- •Optimization tie-in: [Maximum Likelihood Estimation](/tech-tree/mle/)
- •Shape + slopes: [Convex Functions](/tech-tree/convexity/)
- •Dual concept: [Integrals](/tech-tree/integrals-basic/)

Quality: A (4.1/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
