---
title: Curse of Dimensionality
description: Phenomena that arise in high-dimensional spaces - such as sparse sampling, distance concentration, and exponential growth of volume - that affect modeling, generalization, and optimization of large parameter/tensor spaces in deep learning. Recognizing these effects guides choices in architecture, regularization, and feature handling.
date: '2026-07-01'
scheduled: '2026-11-04'
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
inspiration_url: https://templeton.host/tech-tree/curse-of-dimensionality/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/curse-of-dimensionality/](https://templeton.host/tech-tree/curse-of-dimensionality/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Curse of Dimensionality

Probability & StatisticsDifficulty: ★★★★☆Depth: 0Unlocks: 4

Phenomena that arise in high-dimensional spaces - such as sparse sampling, distance concentration, and exponential growth of volume - that affect modeling, generalization, and optimization of large parameter/tensor spaces in deep learning. Recognizing these effects guides choices in architecture, regularization, and feature handling.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Exponential growth of volume with dimension (volume of a radius-r ball scales roughly like r^d)
- -Sample/data sparsity in high dimensions (a fixed number of samples occupies a vanishing fraction of the space as dimension grows)
- -Distance concentration (pairwise distances and norms become similar; distance contrast vanishes)

## Key Symbols & Notation

d (dimensionality)n (number of independent samples/data points)

## Essential Relationships

- -Exponential volume growth in d makes a fixed n sparse relative to the space; that sparsity produces distance concentration, and together they raise the sample complexity required for reliable learning

## Unlocks (1)

[Deep Learninglvl 5](/tech-tree/deep-learning/)

Advanced Learning Details

### Graph Position

6

Depth Cost

4

Fan-Out (ROI)

2

Bottleneck Score

0

Chain Length

### Cognitive Load

6

Atomic Elements

34

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (13)

- - Ambient (ambient) dimensionality - the number d of coordinates/features that define the space data or parameters live in
- - Exponential growth of volume with dimension - small increases in d produce exponential increases in volume for fixed-radius regions
- - Sampling sparsity in high dimensions - for fixed sample count, the fraction of space covered/represented falls rapidly as d increases
- - Distance (or metric) concentration - pairwise distances between random points become similar as d grows
- - Nearest-neighbor breakdown - nearest and farthest neighbor distances converge so similarity-based methods lose discrimination
- - Sample complexity explosion (data need) - amount of data required for fixed coverage/accuracy grows (often exponentially) with d
- - Curse effects on generalization - higher d increases overfitting risk and degrades generalization for fixed n
- - Curse effects on optimization - large parameter/tensor dimensionality creates many flat/ill-conditioned directions and complicates optimization
- - Intrinsic (manifold) dimension - the lower-dimensional manifold dimension m on which data may actually lie, distinct from ambient d
- - Effective dimensionality - the number of degrees of freedom that actually matter for a model (may be reduced by regularization/architectural constraints)
- - Volume concentration near boundary - in high d, most of a region's volume can lie near its boundary rather than its center
- - Curse-driven failure modes of algorithms - specific algorithm classes (e.g., k-NN, naive density estimators) degrade in high d
- - Mitigation strategies as conceptual tools - dimensionality reduction, feature selection, regularization, parameter sharing, and architecture design (e.g., convolutions) that reduce effective d or parameter count

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Why does a model that works beautifully in 2D fail miserably in 200D—even with “lots” of data? The curse of dimensionality is the collection of geometric and probabilistic surprises that appear when d is large: space gets huge, samples get sparse, and distances stop behaving like useful signals.

TL;DR:

In high dimensions, volume grows exponentially with d, so a fixed n covers a vanishing fraction of the space; and common distance measures concentrate (most pairwise distances become nearly equal). These effects degrade nearest-neighbor intuition, density estimation, generalization, and optimization. Deep learning fights the curse by using inductive bias (architecture), regularization, and learning low-dimensional structure (representations).

## What Is Curse of Dimensionality?

The **curse of dimensionality** is not one single theorem. It’s a name for multiple phenomena that all rhyme:

- •**The space you’re trying to model grows explosively** as the number of dimensions d increases.
- •**Your data become sparse**: even large datasets occupy a tiny, tiny portion of the space.
- •**Distances concentrate**: the notion of “near” vs “far” becomes less informative.

These show up in probability, statistics, geometry, and machine learning. The “curse” is that many algorithms rely on intuitions from 1D/2D/3D—like “local neighborhoods are meaningful” or “I can sample enough points to cover the space”—but those intuitions break in high d.

### Why this matters for modeling

In ML we often treat each feature as a dimension. If you have:

- •a 224×224 RGB image → d = 224·224·3 ≈ 150k
- •a 4096-token embedding sequence with width 1024 → d ≈ 4M
- •a deep network with millions of parameters → optimization happens in a parameter space with huge d

Even when the data lie on some low-dimensional structure, the **ambient dimension** is enormous. The curse explains why:

- •kNN and kernel methods can degrade without careful representation
- •density estimation (like histograms) becomes impossible without assumptions
- •“just add features” can harm generalization
- •regularization and architectural bias are not optional, they’re survival tools

### A helpful mental model

Think of a dataset as n points **x**₁,…,**x**ₙ in ℝᵈ. The curse says:

1) The volume of a “reasonable neighborhood” around a point can be astronomically small compared to the whole space.

2) To keep coverage the same as d grows, n must often grow like cᵈ (exponential).

3) The distribution of ‖**x**ᵢ − **x**ⱼ‖ becomes tight (concentrated), so relative distance contrast shrinks.

We’ll unpack each of these carefully, with concrete calculations.

### Key symbols

- •d: dimensionality (number of coordinates/features)
- •n: number of (independent) samples/data points
- •**x**, **y**: vectors in ℝᵈ
- •‖**x**‖: Euclidean norm

We’ll mainly use Euclidean geometry for clarity, but the same themes recur with other norms and metrics.

## Core Mechanic 1: Exponential Growth of Volume (and Vanishing Coverage)

High-dimensional geometry behaves differently from low-dimensional geometry. The first shock: **volume scales exponentially with dimension**.

## 1) A simple, brutal example: the hypercube

Consider the unit hypercube [0,1]ᵈ.

- •Its volume is 1 (by definition).
- •Now ask: what fraction of the cube is within distance ε of the boundary?

The “interior” points are those with every coordinate in [ε, 1−ε]. That interior is a cube of side length (1−2ε), so its volume is:

Vol(interior) = (1 − 2ε)ᵈ.

So the boundary layer fraction is:

Fraction near boundary = 1 − (1 − 2ε)ᵈ.

If ε = 0.01 and d = 100:

(1 − 2ε)ᵈ = 0.98¹⁰⁰ ≈ e^{100 ln 0.98} ≈ e^{100(−0.0202)} ≈ e^{−2.02} ≈ 0.133.

So about 1 − 0.133 = 0.867 (86.7%) of the volume lies within 0.01 of the boundary. In higher d this approaches ~100% quickly.

**Interpretation:** in high d, “most of the volume” is in places that feel like edges/corners. Geometrically, the typical point is not “deep inside.”

## 2) Balls vs cubes: the ball doesn’t fill the cube

A second classic surprise: the inscribed Euclidean ball inside a cube occupies a vanishing fraction of the cube as d grows.

Take the cube [−1,1]ᵈ. Its volume is:

Vol(cube) = 2ᵈ.

The largest Euclidean ball centered at 0 that fits inside has radius r = 1 (it touches faces). The volume of a d-dimensional ball of radius r is:

Vol(Bᵈ(r)) = V\_d rᵈ,

where V\_d = Vol(Bᵈ(1)) is the unit-ball volume constant.

So the fraction of cube volume occupied by the inscribed ball is:

Fraction = Vol(Bᵈ(1)) / 2ᵈ = V\_d / 2ᵈ.

Even if you don’t memorize V\_d, the key point is: **2ᵈ explodes exponentially**, while V\_d does not keep up (in fact V\_d eventually shrinks to 0 as d increases).

So the fraction goes to 0 rapidly.

**Interpretation:** Euclidean neighborhoods (balls) are “tiny” compared to axis-aligned ranges (cubes) in high d, and vice versa. Your intuition about shape and coverage becomes unreliable.

## 3) Why “rᵈ” is the core scaling

Even without the exact formula for V\_d, the rᵈ factor is the headline:

Vol(Bᵈ(r)) = V\_d rᵈ.

For fixed d, doubling r multiplies volume by 2ᵈ.

For fixed r < 1, rᵈ shrinks exponentially as d grows.

Example: r = 0.9.

rᵈ = 0.9ᵈ.

At d = 100, 0.9¹⁰⁰ ≈ e^{100 ln 0.9} ≈ e^{100(−0.1053)} ≈ e^{−10.53} ≈ 2.7×10⁻⁵.

So a ball with radius 0.9 (which sounds “large” in 2D) covers essentially none of the unit ball’s volume in 100D.

## 4) From volume to sample complexity: why data get sparse

Now connect geometry to statistics.

Suppose you want to “cover” [0,1]ᵈ with a grid such that each cell has side length h. Then you need about:

Number of cells ≈ (1/h)ᵈ.

If you want h = 0.1 resolution, you need 10ᵈ cells.

- •d = 2 → 100 cells
- •d = 10 → 10¹⁰ cells
- •d = 100 → 10¹⁰⁰ cells (absurd)

Any method that implicitly needs local coverage—histograms, naive kernel density estimation, lookup tables, nearest-neighbor with meaningful neighborhoods—runs into this wall.

### A useful “coverage” thought experiment

Let **X** be uniform on [0,1]ᵈ. You take n samples. Consider a small ball around a query point **q** with radius r. The probability a single sample falls in that ball is approximately its volume (ignoring boundary effects):

p ≈ Vol(Bᵈ(r)) = V\_d rᵈ.

Probability that none of n samples land in the ball:

P(no samples in ball) = (1 − p)ⁿ ≈ e^{−np}.

To have a decent chance of at least one neighbor (say ≈ 50%), you want np ≈ O(1). That implies:

n · V\_d rᵈ ≈ 1

⇒ n ≈ 1 / (V\_d rᵈ).

So for fixed r, n must grow roughly like 1/rᵈ (exponential in d).

**Interpretation:** “locality” becomes expensive. If your model depends on local neighborhoods, you pay exponentially.

## 5) Why deep learning can still work

This seems to say learning is hopeless in high d. Yet deep learning often succeeds.

The escape hatch is that real data are rarely uniform in [0,1]ᵈ. They tend to have structure:

- •correlations between features
- •low intrinsic dimensionality (data lie near a manifold)
- •compositional patterns (images have local translation structure)

Deep learning’s architectures and regularizers bake in assumptions that exploit structure, effectively reducing the relevant degrees of freedom. But if you ignore structure and treat the space as generic ℝᵈ, the curse is what you get.

## Core Mechanic 2: Distance Concentration (When “Nearest” ≈ “Farthest”)

A second major phenomenon is **distance concentration**: in high dimensions, the distribution of distances between random points becomes tightly concentrated around its mean. That makes distances less informative.

This is not a universal statement for all data distributions, but it is common for many “spread out” distributions (e.g., independent coordinates, isotropic Gaussians, uniform in a cube).

## 1) Why we care: many algorithms are distance-driven

Distance is a workhorse in ML:

- •kNN classification/regression
- •clustering (k-means relies on squared Euclidean distance)
- •kernel methods (RBF kernel depends on ‖**x**−**y**‖²)
- •anomaly detection (distance from typical set)
- •contrastive learning losses (push/pull based on distances)

If distances become almost equal, then:

- •“nearest neighbor” is not much nearer than a random neighbor
- •kernels become nearly constant (or nearly zero) unless tuned extremely carefully
- •optimization landscapes can change (gradients depend on norms)

## 2) A clean calculation: random points in a hypercube

Let **x**, **y** be independent and uniform in [0,1]ᵈ. Consider squared distance:

‖**x** − **y**‖² = ∑ᵢ₌₁ᵈ (xᵢ − yᵢ)².

Each coordinate difference zᵢ = xᵢ − yᵢ has:

E[zᵢ] = 0,

E[zᵢ²] = Var(zᵢ) = Var(xᵢ) + Var(yᵢ) = 1/12 + 1/12 = 1/6,

since Var(U[0,1]) = 1/12.

So:

E[‖**x** − **y**‖²] = ∑ᵢ E[(xᵢ − yᵢ)²] = d · (1/6) = d/6.

Now, because ‖**x** − **y**‖² is a sum of many (weakly) independent terms, the **law of large numbers** implies:

(1/d)‖**x** − **y**‖² → E[(x₁ − y₁)²] = 1/6

as d → ∞.

That is: ‖**x** − **y**‖² is close to d/6 with high probability.

Taking square roots:

‖**x** − **y**‖ ≈ √(d/6).

So distances scale like √d, but importantly the *relative variability* shrinks.

### Relative variability heuristic

If S\_d = ∑ᵢ tᵢ is a sum of i.i.d. terms with mean μ and variance σ², then:

E[S\_d] = dμ,

Var(S\_d) = dσ²,

Std(S\_d) = √(d)σ.

So the coefficient of variation:

Std(S\_d) / E[S\_d] = (√d σ) / (d μ) = (σ/μ) · 1/√d.

It shrinks like 1/√d.

**Interpretation:** even though distances grow with d, their **relative spread** collapses. That’s distance concentration.

## 3) Norm concentration: ‖**x**‖ is almost constant

A related effect: if **x** has i.i.d. coordinates with finite variance, then ‖**x**‖ concentrates.

Example: **x** ∼ N(0, I\_d). Then:

‖**x**‖² = ∑ᵢ xᵢ².

Each xᵢ² has mean 1, so:

E[‖**x**‖²] = d.

In fact ‖**x**‖² is χ²-distributed with d degrees of freedom, and it concentrates sharply around d. Thus:

‖**x**‖ ≈ √d.

So most Gaussian points lie near a thin shell of radius √d.

**Interpretation:** “typical points” in high d live on a shell. Many geometric intuitions about “mass near the center” fail.

## 4) Distance contrast vanishes

A practical way to state the problem is with **contrast**:

Contrast = (E[max distance] − E[min distance]) / E[min distance]

or similar quantities. For many distributions, as d grows, the ratio between farthest and nearest neighbor distances tends toward 1.

That doesn’t mean nearest neighbors are useless in all cases; it means that **without additional structure**, distance-based ranking can become unstable and sensitive to noise.

## 5) What practitioners see

Here are common symptoms that are distance concentration in disguise:

- •In kNN, accuracy degrades unless you learn a better embedding.
- •In RBF kernels, choosing the bandwidth γ is brittle: too small → all kernels ≈ 0; too large → all kernels ≈ 1.
- •In clustering, points may look equally far from all centroids.

A common fix is not “try harder,” but “change representation”: learn a feature space where relevant variability is low-dimensional and distances reflect semantics.

## Application/Connection: Implications for Deep Learning (Architecture, Regularization, Features)

The curse of dimensionality is often introduced with kNN and density estimation, but it reaches deep learning in several ways: through input dimensionality, parameter space dimensionality, and the geometry of learned representations.

## 1) Input space vs intrinsic structure

Images live in ℝ¹⁵⁰ᵏ, but not all of ℝ¹⁵⁰ᵏ looks like an image. The set of natural images is an extremely tiny subset with strong structure:

- •local correlations (nearby pixels are related)
- •translation equivariance (objects move)
- •compositional patterns (edges → textures → parts → objects)

CNNs exploit this by restricting the hypothesis class:

- •local receptive fields
- •weight sharing
- •pooling / hierarchical composition

This is an **anti-curse strategy**: rather than trying to learn an arbitrary function on ℝᵈ, you learn a structured function class that matches the data.

## 2) Why regularization is not optional

In high dimensions, many different functions can fit the training data equally well (huge hypothesis space). Regularization biases the solution toward simpler or more stable ones.

Common tools:

- •weight decay (L2): encourages smaller ‖**w**‖
- •dropout: discourages reliance on any single feature
- •data augmentation: injects invariances so you don’t need to see every variation
- •early stopping: prevents fitting noise

These reduce effective degrees of freedom or enforce smoothness, which counters sparsity.

## 3) Representation learning as dimension management

Distance concentration says Euclidean distances in the raw space may be meaningless. Deep learning often succeeds because it **learns an embedding** where:

- •semantically similar inputs are close
- •irrelevant directions are collapsed
- •the relevant manifold is “unfolded”

Contrastive learning is explicitly about constructing a geometry where distances are informative.

## 4) Optimization in high-dimensional parameter spaces

Neural nets have millions or billions of parameters. While the curse suggests high-dimensional spaces are hard, optimization is not purely about covering parameter space uniformly. Still, high dimensionality affects:

- •conditioning (some directions have tiny curvature, others huge)
- •flat vs sharp minima (generalization correlations)
- •gradient noise scaling

Many techniques act like geometry management:

- •normalization (BatchNorm, LayerNorm) stabilizes scales
- •adaptive optimizers adjust per-coordinate learning rates
- •careful initialization keeps activations/gradients in reasonable ranges

## 5) A quick comparison table: “curse symptoms” and “deep learning responses”

| Curse phenomenon | What goes wrong | Typical response in deep learning |
| --- | --- | --- |
| Volume grows like rᵈ | Local neighborhoods need exponential data | Inductive bias (CNNs, Transformers), augmentation |
| Data sparsity | Overfitting, unreliable local estimates | Regularization, larger datasets, self-supervision |
| Distance concentration | Nearest/farthest become similar | Learned embeddings, metric learning, normalization |
| Many irrelevant features | Noise dominates signal | Feature selection, attention, sparsity penalties |

## 6) The right mindset

The curse is a warning: **don’t assume generic high-dimensional space is friendly**.

But it’s also a design guide:

- •If you can argue your data live near a low-dimensional structure, build models that exploit that.
- •If you must use distances, learn a metric/representation.
- •If you add features, add bias/regularization to avoid needing exponential data.

Deep learning’s success is partly the story of engineering strong inductive biases plus scalable representation learning—ways to avoid paying the full exponential bill.

## Worked Examples (3)

### Boundary dominates in high d: most points are near the edge of a cube

Let **x** be uniform in [0,1]ᵈ. Define “near the boundary” as: at least one coordinate is within ε of 0 or 1. Compute the probability that **x** is within ε of the boundary, and evaluate for ε = 0.01, d = 100.

1. A point is NOT near the boundary iff every coordinate lies in the interior interval [ε, 1−ε].

   So:

   P(not near boundary) = P(x₁∈[ε,1−ε], …, x\_d∈[ε,1−ε]).
2. Because coordinates are independent under the uniform distribution:

   P(not near boundary) = ∏ᵢ₌₁ᵈ P(xᵢ∈[ε,1−ε]).
3. For a single coordinate xᵢ ∼ U[0,1],

   P(xᵢ∈[ε,1−ε]) = (1−ε) − ε = 1 − 2ε.
4. Therefore:

   P(not near boundary) = (1 − 2ε)ᵈ.
5. So:

   P(near boundary) = 1 − (1 − 2ε)ᵈ.
6. Plug in ε = 0.01, d = 100:

   P(near boundary) = 1 − 0.98¹⁰⁰.

   Compute 0.98¹⁰⁰ ≈ e^{100 ln 0.98} ≈ e^{−2.02} ≈ 0.133.

   Thus P(near boundary) ≈ 1 − 0.133 = 0.867.

**Insight:** In 100 dimensions, a randomly chosen point in the unit cube is very likely to be close to some face. “Most of the space is near the boundary” is a key geometric intuition shift that underlies many curse-of-dimensionality effects.

### Distance concentration in a hypercube: ‖\*\*x\*\*−\*\*y\*\*‖² is tightly concentrated

Let **x**, **y** be independent uniform random vectors in [0,1]ᵈ. Compute E[‖**x** − **y**‖²] and explain why ‖**x** − **y**‖ is close to √(d/6) for large d.

1. Write squared distance as a sum:

   ‖**x** − **y**‖² = ∑ᵢ₌₁ᵈ (xᵢ − yᵢ)².
2. Compute the expectation term-by-term:

   E[‖**x** − **y**‖²] = ∑ᵢ₌₁ᵈ E[(xᵢ − yᵢ)²].
3. For independent xᵢ, yᵢ ∼ U[0,1],

   E[(xᵢ − yᵢ)²] = Var(xᵢ − yᵢ) + (E[xᵢ − yᵢ])².

   But E[xᵢ − yᵢ] = 0, so it’s just Var(xᵢ − yᵢ).
4. Use Var(xᵢ − yᵢ) = Var(xᵢ) + Var(yᵢ) (independence).

   Var(U[0,1]) = 1/12.

   So Var(xᵢ − yᵢ) = 1/12 + 1/12 = 1/6.
5. Therefore:

   E[‖**x** − **y**‖²] = ∑ᵢ₌₁ᵈ (1/6) = d/6.
6. Why concentration happens:

   ‖**x** − **y**‖² is a sum of d similar random terms.

   By the law of large numbers,

   (1/d)‖**x** − **y**‖² → 1/6.

   So ‖**x** − **y**‖² ≈ d/6, and hence ‖**x** − **y**‖ ≈ √(d/6).

**Insight:** In high d, distances between random points become predictable. When most distances are nearly the same, “nearest” is not much different from “typical,” which weakens distance-based reasoning unless the data have strong structure or you learn a better representation.

### How many samples to get a neighbor within radius r? (Exponential dependence on d)

Assume data are uniform in a region where a radius-r ball around a query point has probability mass p ≈ V\_d rᵈ. Estimate n needed so there is about a 50% chance at least one of n samples lands inside the ball.

1. Let p be the probability a single sample lands in the ball.

   Then P(no samples in ball) = (1 − p)ⁿ.
2. We want P(at least one sample in ball) ≈ 0.5.

   That means (1 − p)ⁿ ≈ 0.5.
3. For small p, use (1 − p)ⁿ ≈ e^{−np}.

   So we set e^{−np} ≈ 0.5.
4. Take logs:

   −np ≈ ln(0.5) = −ln 2

   ⇒ np ≈ ln 2.
5. Thus:

   n ≈ (ln 2) / p.
6. Substitute p ≈ V\_d rᵈ:

   n ≈ (ln 2) / (V\_d rᵈ).

**Insight:** Even if you ignore constants like V\_d, the rᵈ term dominates: for fixed radius r < 1, the needed n grows like 1/rᵈ. This is the quantitative heart of “sparsity in high dimensions.”

## Key Takeaways

- ✓

  The curse of dimensionality is a cluster of effects in high d: explosive volume growth, data sparsity, and distance/norm concentration.
- ✓

  Volumes of neighborhoods scale like rᵈ, so keeping “local coverage” as d grows typically requires n that grows exponentially in d.
- ✓

  In [0,1]ᵈ, the fraction of volume near the boundary approaches 1 rapidly: geometry is dominated by edges/corners.
- ✓

  For many distributions with roughly independent coordinates, ‖**x**‖ and ‖**x**−**y**‖ concentrate: most points live on a thin shell and pairwise distances are similar.
- ✓

  Distance concentration reduces the usefulness of naive kNN, clustering, and fixed kernels in raw feature spaces.
- ✓

  Deep learning combats the curse with inductive bias (architecture), regularization, and representation learning that discovers low-dimensional structure.
- ✓

  A practical signal of the curse is brittleness to feature scaling/metric choice and the need for far more data when adding dimensions without structure.
- ✓

  The right response is usually not “more dimensions,” but “better structure”: invariances, embeddings, and constraints.

## Common Mistakes

- ✗

  Assuming “more features always helps”: adding weak/noisy dimensions can worsen generalization because you pay a data/regularization cost.
- ✗

  Treating Euclidean distance in raw high-dimensional space as semantically meaningful without checking concentration, scaling, or representation quality.
- ✗

  Confusing ambient dimension d with intrinsic dimension: data may lie on a low-dimensional manifold even when inputs are high-dimensional.
- ✗

  Thinking the curse implies deep learning can’t work: in practice, structure + inductive bias changes the effective problem dramatically.

## Practice

easy

Let **x** be uniform in [0,1]ᵈ. Show that the probability **x** lies in the interior cube [ε, 1−ε]ᵈ is (1−2ε)ᵈ, and compute this value for ε = 0.05 and d = 20.

**Hint:** Use independence across coordinates: multiply the 1D probability across d dimensions.

Show solution

For one coordinate xᵢ ∼ U[0,1], P(xᵢ∈[ε,1−ε]) = 1−2ε.

Independence gives P(**x**∈[ε,1−ε]ᵈ) = (1−2ε)ᵈ.

With ε=0.05: (1−2ε)=0.9.

So probability = 0.9²⁰ ≈ e^{20 ln 0.9} ≈ e^{20(−0.1053)} ≈ e^{−2.106} ≈ 0.122.

medium

Assume **x**, **y** are independent and uniform in [0,1]ᵈ. Using Var(U[0,1]) = 1/12, derive E[‖**x**−**y**‖²] and give the typical scale of ‖**x**−**y**‖ as d grows.

**Hint:** Expand ‖**x**−**y**‖² into a sum of coordinate-wise squared differences and compute expectations term-by-term.

Show solution

‖**x**−**y**‖² = ∑ᵢ (xᵢ−yᵢ)².

E[(xᵢ−yᵢ)²] = Var(xᵢ−yᵢ) since E[xᵢ−yᵢ]=0.

Var(xᵢ−yᵢ)=Var(xᵢ)+Var(yᵢ)=1/12+1/12=1/6.

Thus E[‖**x**−**y**‖²]=d·(1/6)=d/6.

Typical ‖**x**−**y**‖ is about √(d/6), and relative fluctuations shrink like 1/√d.

hard

You want a radius-r neighborhood around a query point to contain at least one sample with probability ≥ 0.95. Approximate the required n in terms of p = V\_d rᵈ using (1−p)ⁿ ≈ e^{−np}.

**Hint:** Set P(at least one) = 1 − (1−p)ⁿ ≥ 0.95 and solve for n via the exponential approximation.

Show solution

Require 1 − (1−p)ⁿ ≥ 0.95 ⇒ (1−p)ⁿ ≤ 0.05.

Approximate (1−p)ⁿ ≈ e^{−np}.

So e^{−np} ≤ 0.05.

Take logs: −np ≤ ln 0.05.

Multiply by −1 (flip inequality): np ≥ −ln 0.05 = ln(1/0.05) = ln 20.

Thus n ≥ (ln 20)/p ≈ (ln 20)/(V\_d rᵈ).

## Connections

- •Unlocks: [Deep Learning](/tech-tree/deep-learning/)
- •Related ideas you’ll likely want next:
- •[Bias-Variance Tradeoff](/tech-tree/bias-variance-tradeoff/)
- •[Regularization](/tech-tree/regularization/)
- •[Manifolds and Intrinsic Dimension](/tech-tree/intrinsic-dimension/)
- •[Nearest Neighbors and kNN](/tech-tree/knn/)
- •[Kernel Methods](/tech-tree/kernel-methods/)
- •[Representation Learning](/tech-tree/representation-learning/)

Quality: B (4.1/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
