---
title: Softmax Function
description: A function that converts a vector of real values into a probability distribution by exponentiating and normalizing each entry; commonly used to produce attention weights. Understanding softmax behavior, numerical stability, and temperature scaling is important for interpreting attention scores.
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
permalink: /tech-tree/softmax-function/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Softmax Function

Probability & StatisticsDifficulty: ★★★☆☆Depth: 0Unlocks: 4

A function that converts a vector of real values into a probability distribution by exponentiating and normalizing each entry; commonly used to produce attention weights. Understanding softmax behavior, numerical stability, and temperature scaling is important for interpreting attention scores.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Exponentiate-and-normalize: softmax computes exp(x\_i)/sum\_j exp(x\_j) to convert a real-valued vector into a probability distribution
- -Shift-invariance and numerical-stability trick: subtracting max(x) from all logits before exponentiation preserves outputs while preventing overflow/underflow
- -Temperature scaling: dividing logits by a temperature T (or multiplying by 1/T) controls distribution sharpness (low T => more peaked, high T => flatter)

## Key Symbols & Notation

softmax(x)\_i (i-th output of softmax on vector x)T (temperature scalar)

## Essential Relationships

- -Outputs are nonnegative and sum to 1 (softmax maps R^n to a probability simplex)

## Unlocks (3)

[Attention Mechanismslvl 5](/tech-tree/attention-mechanisms/)[Sequence-to-Sequence Modelinglvl 4](/tech-tree/sequence-to-sequence-modeling/)[Sequence Masking (causal and padding masks)lvl 4](/tech-tree/sequence-masking/)

Advanced Learning Details

### Graph Position

6

Depth Cost

4

Fan-Out (ROI)

1

Bottleneck Score

0

Chain Length

### Cognitive Load

6

Atomic Elements

42

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (15)

- - Softmax function as a map from a real vector (logits) to a probability vector
- - Logits: the raw real-valued inputs to softmax
- - Exponentiation of each logit before normalization
- - Normalization by the sum of exponentials to produce probabilities
- - Output properties: nonnegativity and components summing to one (probability distribution)
- - Shift invariance: adding the same constant to all logits does not change softmax outputs
- - Numerical stability trick: subtracting the maximum logit before exponentiating
- - Temperature parameter (τ or T) for scaling logits before softmax
- - Effect of temperature on sharpness/peakedness of the output distribution
- - Soft-argmax interpretation: softmax as a differentiable approximation to argmax
- - Log-sum-exp (LSE) as the log-domain normalization constant
- - Interpretation of softmax outputs as attention weights or categorical probabilities
- - Sensitivity/peakedness: how relative differences between logits control output concentration
- - Reduction to binary case: two-entry softmax is equivalent to a sigmoid of the logit difference
- - Jacobian/derivative structure of softmax outputs with respect to logits

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Whenever a model needs to turn “scores” into “choices”, it needs a bridge from arbitrary real numbers to probabilities. Softmax is that bridge: it takes a vector of real-valued logits and returns a probability distribution—smoothly, differentiably, and with behavior you can control (via shifting for stability and temperature for sharpness).

TL;DR:

Softmax maps a vector **x** ∈ ℝⁿ to probabilities by exponentiating and normalizing: softmax(**x**)ᵢ = exp(xᵢ)/∑ⱼ exp(xⱼ). It’s shift-invariant (adding a constant to all logits changes nothing), so we can subtract max(**x**) for numerical stability. Temperature scaling softmax(**x**/T) controls how peaked the distribution is: low T → more confident/peaked; high T → flatter/more uniform.

## What Is Softmax Function?

### Why we need it (motivation)

In many ML systems, we compute **scores** for several options: which class is present, which token to attend to, which action to take. Those scores often live in ℝ: they can be negative, huge, and not constrained to sum to 1.

But downstream we often want a **probability distribution**:

- •**Nonnegative** values (so they can represent probabilities)
- •**Sum to 1** (so they distribute total mass)
- •**Smooth** and **differentiable** (so gradient-based learning works)

Softmax is the standard way to convert a vector of real-valued scores (“logits”) into a probability distribution.

### Definition

Let **x** = (x₁, x₂, …, xₙ) be a vector of real numbers (logits).

The softmax function returns a vector **p** = softmax(**x**) where each component is

softmax⁡(x)i=exi∑j=1nexj.\operatorname{softmax}(\mathbf{x})\_i = \frac{e^{x\_i}}{\sum\_{j=1}^{n} e^{x\_j}}.softmax(x)i​=∑j=1n​exj​exi​​.

### Intuition: “exponentiate then normalize”

Softmax does two simple things:

1. 1)**Exponentiate** each logit: xi↦exix\_i \mapsto e^{x\_i}xi​↦exi​

- •This makes everything positive.
- •It also makes differences matter: a logit that’s larger by 2 becomes e2≈7.39e^2 \approx 7.39e2≈7.39 times bigger after exponentiation.

2. 2)**Normalize** by the sum: divide by ∑ⱼ e^{xⱼ}

- •This forces the outputs to sum to 1.

So softmax turns relative score gaps into **relative probability mass**.

### A quick sanity check: it’s a probability distribution

For each i:

- •exi>0e^{x\_i} > 0exi​>0 ⇒ softmax(**x**)ᵢ > 0
- •Summation property:

∑i=1nsoftmax⁡(x)i=∑i=1nexi∑j=1nexj=∑i=1nexi∑j=1nexj=1.\sum\_{i=1}^n \operatorname{softmax}(\mathbf{x})\_i = \sum\_{i=1}^n \frac{e^{x\_i}}{\sum\_{j=1}^n e^{x\_j}} = \frac{\sum\_{i=1}^n e^{x\_i}}{\sum\_{j=1}^n e^{x\_j}} = 1.i=1∑n​softmax(x)i​=i=1∑n​∑j=1n​exj​exi​​=∑j=1n​exj​∑i=1n​exi​​=1.

So softmax(**x**) lies on the probability simplex (the set of all probability vectors).

### Terminology you’ll see

- •**Logits**: the input scores **x**.
- •**Probabilities**: the output softmax(**x**).
- •**Attention weights**: in attention, softmax converts similarity scores into weights over tokens.

Softmax is simple to write down, but its behavior (and pitfalls) matter a lot in real models—especially numerical stability and temperature scaling, which we’ll build up next.

## Core Mechanic 1: Behavior of Exponentiate-and-Normalize

### Why exponentials?

Exponentials have two key effects:

1. 1)**Positivity**: exie^{x\_i}exi​ is always positive.
2. 2)**Multiplicative amplification**: differences in logits turn into ratios.

A crucial identity is the ratio form:

softmax⁡(x)isoftmax⁡(x)k=exiexk=exi−xk.\frac{\operatorname{softmax}(\mathbf{x})\_i}{\operatorname{softmax}(\mathbf{x})\_k} = \frac{e^{x\_i}}{e^{x\_k}} = e^{x\_i - x\_k}.softmax(x)k​softmax(x)i​​=exk​exi​​=exi​−xk​.

This says softmax compares logits via their **differences**. If xix\_ixi​ exceeds xkx\_kxk​ by Δ, then i gets eΔe^{\Delta}eΔ times more probability than k.

### Two-class case: softmax becomes sigmoid

If n = 2 with logits (a, b), then

p1=eaea+eb=11+eb−a.p\_1 = \frac{e^a}{e^a + e^b} = \frac{1}{1 + e^{b-a}}.p1​=ea+ebea​=1+eb−a1​.

That’s exactly a sigmoid in the logit difference (a − b). This is a nice mental model:

- •softmax is the “multi-class sigmoid.”

### Invariance to units? Not quite.

Softmax is **not** invariant to scaling of logits. If you multiply logits by a constant c, softmax typically becomes more or less peaked (we’ll formalize this with temperature later).

### Peakedness: how “winner-take-most” emerges

Consider three logits: **x** = (2, 1, 0).

Compute exponentials:

- •e² ≈ 7.39
- •e¹ ≈ 2.72
- •e⁰ = 1

Sum ≈ 11.11

So probabilities ≈ (0.665, 0.245, 0.090).

A gap of 1 between logits becomes a factor of e ≈ 2.72 in weight; a gap of 2 becomes e² ≈ 7.39. This is why softmax can produce strong preferences even from modest logit gaps.

### Geometric view: softmax outputs live on the simplex

For n = 3, the output probabilities (p₁, p₂, p₃) satisfy p₁ + p₂ + p₃ = 1 and each pᵢ ≥ 0. That set is a 2D triangle (a simplex) embedded in 3D.

Here’s an ASCII simplex diagram to orient you:

```
          p3=1
           ▲
          / \
         /   \
        /  •  \   • interior points: all p_i in (0,1)
       /       \
      /         \
     /___________\
 p1=1             p2=1
```

- •Vertices correspond to “certain” distributions like (1,0,0).
- •The center corresponds to uniform (1/3,1/3,1/3).

Softmax maps any logits vector **x** to some point inside this triangle.

### Visualization: temperature effect on a 2-option softmax curve

For two options, softmax probability of option 1 depends on the logit difference d = x₁ − x₂:

p1(d;T)=11+e−d/T.p\_1(d;T) = \frac{1}{1 + e^{-d/T}}.p1​(d;T)=1+e−d/T1​.

Below is an inline diagram showing how changing T changes the curve. The horizontal axis is d, vertical is p₁.

```
p1
1.0 |                         ............  T=0.5 (sharper)
    |                    .....
0.8 |               .....
    |           ....
0.6 |        ...                    _________  T=1 (baseline)
    |     ...                 _____
0.5 |-----+-------------------+----------------------------- d
    |     ...             ____
0.4 |        ...      ____                 - - - - - - - -  T=2 (flatter)
    |           ....__
0.2 |               .....
    |                    .....
0.0 |                         ............
      -6   -4   -2    0    2    4    6
```

Interpretation:

- •**Lower T**: transitions faster from 0 to 1 → more “confident.”
- •**Higher T**: transitions slower → more “uncertain.”

We’ll connect this to attention weights: low temperature makes attention concentrate on a few tokens; high temperature spreads it out.

### Practical note: softmax is often applied row-wise

In attention, you’ll see softmax applied to a vector of scores for a given query over all keys. If you have a matrix of scores, softmax is applied **per row** (or per last dimension), producing a distribution over positions for each query.

This first mechanic—exponentiate then normalize—gives the core behavior. Next we’ll cover the crucial property that makes softmax usable in real systems: shift invariance and numerical stability.

## Core Mechanic 2: Shift-Invariance and Numerical Stability (the max trick)

### Why this matters

Exponentials can overflow or underflow:

- •e1000e^{1000}e1000 is astronomically large (overflow in float32/float64).
- •e−1000e^{-1000}e−1000 is essentially 0 (underflow).

Yet logits in neural nets can easily reach magnitudes where naive exp() is unsafe. So we need a stable way to compute softmax.

### Key property: shift-invariance

Softmax is unchanged if you add the same constant c to every logit:

softmax⁡(x+c1)=softmax⁡(x).\operatorname{softmax}(\mathbf{x} + c\mathbf{1}) = \operatorname{softmax}(\mathbf{x}).softmax(x+c1)=softmax(x).

**Derivation (showing work):**

Let yi=xi+cy\_i = x\_i + cyi​=xi​+c.

softmax⁡(y)i=eyi∑jeyj=exi+c∑jexj+c=ecexiec∑jexj=exi∑jexj=softmax⁡(x)i.\operatorname{softmax}(\mathbf{y})\_i = \frac{e^{y\_i}}{\sum\_j e^{y\_j}}
= \frac{e^{x\_i + c}}{\sum\_j e^{x\_j + c}}
= \frac{e^c e^{x\_i}}{e^c \sum\_j e^{x\_j}}
= \frac{e^{x\_i}}{\sum\_j e^{x\_j}}
= \operatorname{softmax}(\mathbf{x})\_i.softmax(y)i​=∑j​eyj​eyi​​=∑j​exj​+cexi​+c​=ec∑j​exj​ecexi​​=∑j​exj​exi​​=softmax(x)i​.

So adding a constant doesn’t change the output probabilities.

### The numerical-stability trick: subtract max

Because of shift-invariance, we can choose c conveniently. The most common choice is

c=−max⁡ixi.c = -\max\_i x\_i.c=−imax​xi​.

Define m=max⁡ixim = \max\_i x\_im=maxi​xi​ and zi=xi−mz\_i = x\_i - mzi​=xi​−m.

Then max⁡izi=0\max\_i z\_i = 0maxi​zi​=0, so every zi≤0z\_i \le 0zi​≤0.

Now compute softmax using z:

softmax⁡(x)i=exi−m∑jexj−m.\operatorname{softmax}(\mathbf{x})\_i = \frac{e^{x\_i - m}}{\sum\_j e^{x\_j - m}}.softmax(x)i​=∑j​exj​−mexi​−m​.

This is stable because:

- •The largest exponent is e0=1e^0 = 1e0=1 (safe).
- •Others are enegative∈(0,1]e^{\text{negative}} \in (0,1]enegative∈(0,1] (also safe).

### Simple example: stability without changing meaning

Suppose **x** = (1000, 1001, 999).

Naively, e^{1001} overflows.

Use max trick: m = 1001

- •z = (-1, 0, -2)

Exponentials:

- •e^{-1} ≈ 0.3679
- •e^{0} = 1
- •e^{-2} ≈ 0.1353

Sum ≈ 1.5032

Probabilities ≈ (0.2447, 0.6652, 0.0900)

These are perfectly reasonable—no overflow.

### Visualization: shifting logits moves nothing on the simplex

Shifting logits by a constant slides **x** along the direction **1** = (1,1,1,…). Softmax “forgets” that direction completely.

For n=3, imagine two different logit vectors:

- •**x** = (2, 1, 0)
- •**x'** = (2+10, 1+10, 0+10) = (12, 11, 10)

They map to the exact same point (p₁, p₂, p₃) on the simplex triangle.

Here’s a conceptual diagram combining both ideas—shift vs. scale:

```
Simplex (n=3 probabilities)

          (0,0,1)
             ▲
            / \
           /   \
          /  A  \        A = softmax(x)
         /       \       softmax(x + 10·1) = A  (shift: unchanged)
        /    •    \      softmax(x / T) moves toward vertex or center (scale)
       /___________\
 (1,0,0)           (0,1,0)

- Shift logits: stay at the same point A.
- Scale logits (or change T): slide along a path toward a vertex (peaked) or toward center (uniform).
```

### Implementation note (what you should do in code)

Always compute softmax as:

1) m=max⁡ixim = \max\_i x\_im=maxi​xi​

2) zi=xi−mz\_i = x\_i - mzi​=xi​−m

3) pi=exp⁡(zi)/∑jexp⁡(zj)p\_i = \exp(z\_i) / \sum\_j \exp(z\_j)pi​=exp(zi​)/∑j​exp(zj​)

This gives identical results in exact math, and far better results in floating-point.

### A related stable quantity: log-softmax

Often you want log probabilities (e.g., for cross-entropy). Use:

log⁡softmax⁡(x)i=xi−log⁡(∑jexj).\log \operatorname{softmax}(\mathbf{x})\_i = x\_i - \log\left(\sum\_j e^{x\_j}\right).logsoftmax(x)i​=xi​−log(j∑​exj​).

Stably, compute:

- •m=max⁡jxjm = \max\_j x\_jm=maxj​xj​
- •log⁡∑jexj=m+log⁡∑jexj−m\log\sum\_j e^{x\_j} = m + \log\sum\_j e^{x\_j - m}log∑j​exj​=m+log∑j​exj​−m (this is the **log-sum-exp trick**)

Even if you don’t implement it now, it’s important conceptually: stability is not optional when exponentials are involved.

Next we’ll look at temperature scaling, which is like a *controlled scaling* of logits that changes the softness/hardness of the distribution.

## Core Mechanic 3: Temperature Scaling (Controlling Sharpness)

### Why introduce temperature?

Sometimes you want probabilities that are:

- •**Sharper** (more peaked) so the model strongly prefers one option.
- •**Flatter** (more spread out) so the model remains uncertain or explores alternatives.

Temperature scaling gives a single knob T > 0 that controls this.

### Definition

Given logits **x**, temperature-scaled softmax is

softmax⁡T(x)i=exi/T∑jexj/T.\operatorname{softmax}\_T(\mathbf{x})\_i = \frac{e^{x\_i/T}}{\sum\_j e^{x\_j/T}}.softmaxT​(x)i​=∑j​exj​/Texi​/T​.

Equivalent viewpoint: dividing by T is like multiplying logits by α=1/T\alpha = 1/Tα=1/T.

- •T = 1 → standard softmax.
- •T < 1 → logits are effectively magnified → sharper.
- •T > 1 → logits are effectively shrunk → flatter.

### Limiting behavior (important intuition)

Let **p**(T) = softmax(**x**/T).

1) As T → 0⁺:

- •The largest logit dominates.
- •**p** approaches a one-hot distribution at argmax.

2) As T → ∞:

- •All logits become tiny relative to T.
- •Exponentials become similar.
- •**p** approaches uniform: pi→1/np\_i → 1/npi​→1/n.

You can see this via differences: ratios are

pipk=e(xi−xk)/T.\frac{p\_i}{p\_k} = e^{(x\_i-x\_k)/T}.pk​pi​​=e(xi​−xk​)/T.

- •If T is small, (xᵢ − x\_k)/T is large in magnitude ⇒ ratios explode ⇒ one option dominates.
- •If T is large, (xᵢ − x\_k)/T ≈ 0 ⇒ ratios near 1 ⇒ uniform-ish.

### Temperature in attention

In dot-product attention, scores often look like

si=q⋅kid.s\_i = \frac{\mathbf{q} \cdot \mathbf{k}\_i}{\sqrt{d}}.si​=d​q⋅ki​​.

Then attention weights are

ai=softmax⁡(s)i.a\_i = \operatorname{softmax}(\mathbf{s})\_i.ai​=softmax(s)i​.

The $1/\sqrt{d}$ factor plays a temperature-like role: it prevents dot products from growing too large with dimension d (which would make softmax too peaked too early).

### Visual: how T moves you on the simplex (n=3)

Take logits **x** = (2, 1, 0). Consider three temperatures.

Compute probabilities:

- •T = 2: softmax( (1, 0.5, 0) )
- •exp: (2.718, 1.649, 1)
- •sum: 5.367
- •p ≈ (0.506, 0.307, 0.186) (flatter)

- •T = 1: softmax( (2, 1, 0) )
- •p ≈ (0.665, 0.245, 0.090)

- •T = 0.5: softmax( (4, 2, 0) )
- •exp: (54.598, 7.389, 1)
- •sum: 62.987
- •p ≈ (0.867, 0.117, 0.016) (peaked)

On the simplex triangle, these three points lie along a path from the center-ish region toward the vertex (1,0,0) as T decreases.

### Calibration note (probabilities vs confidence)

Temperature scaling is also used for **calibration**: you can adjust T (often on a validation set) so predicted probabilities better match empirical accuracy.

- •If a classifier is overconfident, increasing T (T > 1) can reduce peakiness.
- •If underconfident, decreasing T can sharpen predictions.

This is a big reason softmax is interpreted carefully: the raw logits contain information beyond just the top class.

At this point you know:

- •What softmax is.
- •How to compute it stably.
- •How temperature changes its behavior.

Next we connect it directly to attention mechanisms, masking, and how to interpret attention scores.

## Application/Connection: Softmax in Attention, Masking, and Interpretation

### Softmax as “attention allocator”

In attention, you compute a score for each key/value relative to a query. These scores are logits **s**.

Softmax turns them into weights **a** that sum to 1:

ai=softmax⁡(s)i.a\_i = \operatorname{softmax}(\mathbf{s})\_i.ai​=softmax(s)i​.

Then the attention output is a weighted sum:

Attn(q)=∑iaivi.\text{Attn}(\mathbf{q}) = \sum\_i a\_i \mathbf{v}\_i.Attn(q)=i∑​ai​vi​.

So softmax is the mechanism that converts similarities into a convex combination of values.

### How to read attention weights

Because ai≥0a\_i \ge 0ai​≥0 and ∑ᵢ aᵢ = 1:

- •Each aᵢ is a **fraction of attention mass**.
- •The output is inside the convex hull of the value vectors.

But interpret carefully:

- •Attention weights reflect **relative** importance under the model’s scoring function.
- •Small changes in logits can cause large changes in weights when the distribution is already sharp (especially at low T).

### Masking: forcing probabilities to ignore some positions

In sequence models you often must prevent attending to:

- •padding tokens (padding mask)
- •future tokens (causal mask)

The standard technique: add a large negative number (−∞ in math; a big negative constant in practice) to masked logits before softmax.

Let mask mᵢ be 0 for allowed, and −∞ for disallowed. Define

si′=si+mi.s'\_i = s\_i + m\_i.si′​=si​+mi​.

Then

- •if mᵢ = −∞ ⇒ esi′=0e^{s'\_i} = 0esi′​=0 ⇒ probability becomes 0.
- •allowed positions renormalize to sum to 1.

This works because softmax only cares about exponentials; setting a logit to −∞ removes it from the sum.

### Numerical detail: choose a safe “−∞”

In floating point, you use something like −1e9 (float32) or a framework-provided mask fill value.

- •Too small in magnitude: masked positions may still get nonzero probability.
- •Too large in magnitude: can cause NaNs if combined with other operations (less common if you use stable softmax).

### Connection to cross-entropy and learning signals

Softmax is commonly paired with cross-entropy loss.

If the true class is k and predicted probabilities are pᵢ, then

L=−log⁡pk.\mathcal{L} = -\log p\_k.L=−logpk​.

When the model assigns low probability to the correct class, the loss is large.

A key internal quantity is log-sum-exp:

pk=exk∑jexj⇒−log⁡pk=−xk+log⁡(∑jexj).p\_k = \frac{e^{x\_k}}{\sum\_j e^{x\_j}} \quad\Rightarrow\quad -\log p\_k = -x\_k + \log\left(\sum\_j e^{x\_j}\right).pk​=∑j​exj​exk​​⇒−logpk​=−xk​+log(j∑​exj​).

This is one reason stable log-softmax implementations are so common.

### Interpreting logits vs probabilities

Logits contain “un-normalized evidence.” Softmax converts them to probabilities, but:

- •Probabilities can saturate near 0 or 1 (especially at low T), hiding meaningful logit differences.
- •Comparing logits across different contexts can be tricky; softmax probabilities are context-dependent because the denominator includes all options.

### Summary of when softmax is the right tool

Use softmax when you need:

- •a distribution over mutually exclusive categories, or
- •nonnegative weights summing to 1 (attention, mixture weights).

Avoid or reconsider when you need:

- •independent multi-label probabilities (use sigmoid per label instead), or
- •hard argmax choices during training (softmax gives a smooth proxy).

With these connections, you’re ready to use softmax as a dependable building block for attention mechanisms, masking, and sequence-to-sequence models.

## Worked Examples (3)

### Compute softmax probabilities (and see how gaps matter)

Let **x** = (2, 1, 0). Compute softmax(**x**) exactly as exponentiate-and-normalize.

1. Write the definition:

   softmax(**x**)ᵢ = exp(xᵢ) / (exp(2) + exp(1) + exp(0)).
2. Compute exponentials:

   exp(2) ≈ 7.389,

   exp(1) ≈ 2.718,

   exp(0) = 1.
3. Sum them:

   S = 7.389 + 2.718 + 1 = 11.107.
4. Normalize each component:

   p₁ = 7.389 / 11.107 ≈ 0.665,

   p₂ = 2.718 / 11.107 ≈ 0.245,

   p₃ = 1 / 11.107 ≈ 0.090.
5. Check the distribution sums to 1 (up to rounding):

   0.665 + 0.245 + 0.090 = 1.000.

**Insight:** Softmax cares about differences: (2 vs 1 vs 0) becomes roughly (0.665, 0.245, 0.090). A 1-point logit gap turns into a factor of e ≈ 2.72 in probability mass before normalization.

### Numerical stability: naive softmax overflows, max-shifted softmax works

Let **x** = (1000, 1001, 999). Show why naive computation fails and compute softmax stably using the max trick.

1. Naive approach would require exp(1000), exp(1001), exp(999).

   In float32/float64, exp(1001) overflows (becomes ∞), making the result undefined (∞/∞).
2. Use shift-invariance:

   Let m = max(**x**) = 1001.

   Define zᵢ = xᵢ − m, so **z** = (-1, 0, -2).
3. Compute exponentials safely:

   exp(-1) ≈ 0.3679,

   exp(0) = 1,

   exp(-2) ≈ 0.1353.
4. Sum:

   S = 0.3679 + 1 + 0.1353 = 1.5032.
5. Normalize:

   p₁ = 0.3679 / 1.5032 ≈ 0.2447,

   p₂ = 1 / 1.5032 ≈ 0.6652,

   p₃ = 0.1353 / 1.5032 ≈ 0.0900.

**Insight:** Subtracting max(**x**) doesn’t change softmax outputs, but it bounds the largest exponent at 1, preventing overflow and improving precision.

### Temperature scaling changes sharpness without changing the argmax

Let **x** = (2, 1, 0). Compute softmax(**x**/T) for T = 2, 1, 0.5 and compare.

1. Case T = 2:

   **x**/2 = (1, 0.5, 0).

   exp values: (2.718, 1.649, 1).

   Sum S ≈ 5.367.

   Probabilities: (0.506, 0.307, 0.186).
2. Case T = 1:

   Already computed: (0.665, 0.245, 0.090).
3. Case T = 0.5:

   **x**/0.5 = (4, 2, 0).

   exp values: (54.598, 7.389, 1).

   Sum S ≈ 62.987.

   Probabilities: (0.867, 0.117, 0.016).
4. Compare:

   As T decreases, p₁ increases and the distribution becomes more peaked.

   The argmax remains index 1 for all T > 0 (since scaling by 1/T preserves order).

**Insight:** Temperature doesn’t change which logit is largest, but it strongly affects how much probability mass concentrates on the top options—critical for attention sharpness and calibration.

## Key Takeaways

- ✓

  Softmax converts logits **x** ∈ ℝⁿ into probabilities: softmax(**x**)ᵢ = exp(xᵢ)/∑ⱼ exp(xⱼ).
- ✓

  Softmax outputs are always positive and sum to 1, so they lie on the probability simplex.
- ✓

  Softmax depends on logit differences: softmax(**x**)ᵢ / softmax(**x**)ₖ = exp(xᵢ − xₖ).
- ✓

  Shift-invariance: adding the same constant to all logits leaves softmax unchanged; this enables the stable max-subtraction trick.
- ✓

  For stable computation, use **z** = **x** − max(**x**) before exponentiating to avoid overflow/underflow.
- ✓

  Temperature scaling softmax(**x**/T) controls sharpness: low T → peaked; high T → flat; T → ∞ approaches uniform.
- ✓

  In attention, softmax turns similarity scores into attention weights; masking is implemented by adding −∞ (or a large negative value) to disallowed logits before softmax.

## Common Mistakes

- ✗

  Computing softmax as exp(xᵢ)/∑exp(xⱼ) without subtracting max(**x**), leading to overflow, underflow, or NaNs.
- ✗

  Confusing shift-invariance with scale-invariance: adding a constant changes nothing, but multiplying/dividing logits (including temperature) changes the distribution.
- ✗

  Using softmax for multi-label problems where labels are independent; sigmoid per label is usually appropriate there.
- ✗

  Interpreting softmax probabilities as absolute confidence without considering temperature, calibration, or the set of competing logits in the denominator.

## Practice

easy

Compute softmax(**x**) for **x** = (0, 0, 0, 0). What distribution do you get and why?

**Hint:** All exponentials are equal; normalize by their sum.

Show solution

exp(0)=1 for each entry, sum = 4, so each probability is 1/4. Softmax returns the uniform distribution when all logits are equal.

medium

Show (algebraically) that softmax is shift-invariant: softmax(**x** + c**1**) = softmax(**x**).

**Hint:** Factor e^c out of numerator and denominator.

Show solution

Let yᵢ = xᵢ + c. Then softmax(**y**)ᵢ = e^{xᵢ+c}/∑ⱼ e^{xⱼ+c} = (e^c e^{xᵢ})/(e^c ∑ⱼ e^{xⱼ}) = e^{xᵢ}/∑ⱼ e^{xⱼ} = softmax(**x**)ᵢ.

hard

Let **x** = (3, 1, -1). Compute softmax(**x**/T) for T = 1 and T = 2 (use the max trick if you want). Which is more peaked? Explain using ratios.

**Hint:** Compare p₁/p₂ = exp((x₁-x₂)/T).

Show solution

For T=1: exponentials are (e^3, e^1, e^{-1}) ≈ (20.085, 2.718, 0.368). Sum ≈ 23.171. So p ≈ (0.867, 0.117, 0.016).

For T=2: logits are (1.5, 0.5, -0.5). exponentials ≈ (4.482, 1.649, 0.607). Sum ≈ 6.738. So p ≈ (0.665, 0.245, 0.090).

T=1 is more peaked. Ratio explanation: p₁/p₂ = exp((3-1)/T) = exp(2/T). For T=1 ratio is e^2≈7.39; for T=2 ratio is e^1≈2.72, so the top class dominates more at lower T.

## Connections

- •[Attention Mechanisms](/tech-tree/attention-mechanisms/)
- •[Sequence-to-Sequence Modeling](/tech-tree/sequence-to-sequence-modeling/)
- •[Sequence Masking (causal and padding masks)](/tech-tree/sequence-masking/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
