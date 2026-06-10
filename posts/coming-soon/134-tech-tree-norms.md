---
title: Norms
description: Vector length/magnitude. L1, L2 (Euclidean), Linf norms.
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
source_format: html
inspiration_url: https://templeton.host/tech-tree/norms/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/norms/](https://templeton.host/tech-tree/norms/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Norms

Linear AlgebraDifficulty: ★★☆☆☆Depth: 3Unlocks: 1

Vector length/magnitude. L1, L2 (Euclidean), Linf norms.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Positive-definiteness: a norm assigns a nonnegative length and is zero iff the vector is the zero vector
- -Absolute homogeneity: scaling a vector scales its norm by the absolute value of the scalar (norm(alpha\*v)=|alpha|\*norm(v))
- -Triangle inequality: the norm of a sum is at most the sum of norms (norm(u+v) <= norm(u)+norm(v))

## Key Symbols & Notation

||v||\_p (norm of vector v; subscript p denotes p-norm)

## Essential Relationships

- -Euclidean (L2) connection: ||v||\_2 = sqrt(v dot v)
- -Lp family formulas (including L1 and Linf): ||v||\_p = (sum\_i |v\_i|^p)^(1/p); in particular ||v||\_1 = sum\_i |v\_i| and ||v||\_infty = max\_i |v\_i|

## Prerequisites (1)

[Dot Product5 atoms](/tech-tree/dot-product/)

## Unlocks (1)

[Clusteringlvl 4](/tech-tree/clustering/)

Advanced Learning Details

### Graph Position

23

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

3

Chain Length

### Cognitive Load

6

Atomic Elements

26

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (11)

- - Norm: a function ||·|| that maps a vector to a nonnegative scalar representing its length/magnitude
- - Positive definiteness of a norm: ||v|| ≥ 0 for all v and ||v|| = 0 iff v = 0
- - Positive homogeneity (absolute scalability): ||a v|| = |a| · ||v|| for scalar a
- - Triangle inequality for norms: ||u + v|| ≤ ||u|| + ||v||
- - L2 (Euclidean) norm: ||v||\_2 = sqrt(sum\_i v\_i^2)
- - L1 (taxicab/Manhattan) norm: ||v||\_1 = sum\_i |v\_i|
- - L∞ (maximum/sup) norm: ||v||\_∞ = max\_i |v\_i|
- - Relationship between L2 norm and dot product: L2 norm equals sqrt(v · v)
- - Normalization / unit vector: dividing a nonzero vector by its norm to get a unit-length vector (v / ||v||)
- - Norm-induced distance: defining distance between vectors as d(u,v) = ||u - v||
- - Lp family (generalization): ||v||\_p = (sum\_i |v\_i|^p)^(1/p) for p ≥ 1 (context for L1 and L2; L∞ is the limit as p→∞)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

If you can measure “how far” a vector is from zero, you can compare directions, choose the nearest point, control model complexity, and reason about geometry. Norms are the standard way to do that—and different norms create different notions of distance and “closeness.”

TL;DR:

A norm ‖**v**‖ assigns a nonnegative length to a vector, with three rules: (1) it’s zero only for the zero vector, (2) scaling scales length by |α|, and (3) it obeys the triangle inequality. The most common are ‖**v**‖₁ (sum of absolute values), ‖**v**‖₂ (Euclidean), and ‖**v**‖∞ (max absolute component). Different norms change geometry and behavior in algorithms like clustering.

## What Is a Norm?

### Why we need “length” beyond pictures

In 2D or 3D, “length” feels obvious: draw an arrow from the origin to a point and measure how long it is. But in computer science and machine learning you constantly work in **higher-dimensional** spaces:

- •a document as a vector of word counts (10,000+ dimensions)
- •an image as a vector of pixel intensities
- •a user profile as a vector of features

In those settings, you still need a rigorous way to answer:

- •How big is a vector **v**?
- •How far is **x** from **y**?
- •Which point is “closest” to a centroid?

A **norm** is the mathematical object that turns these questions into consistent computations.

### Definition (with intuition)

A **norm** is a function that maps a vector to a nonnegative real number:

‖·‖ : ℝⁿ → ℝ

It must satisfy three properties for all vectors **u**, **v** and all scalars α:

1) **Positive-definiteness**

- •‖**v**‖ ≥ 0
- •‖**v**‖ = 0 ⇔ **v** = **0**

Intuition: length can’t be negative; the only vector with zero length is the zero vector.

2) **Absolute homogeneity**

‖α**v**‖ = |α| ‖**v**‖

Intuition: scaling an arrow by 3 makes it 3× longer; scaling by −3 flips direction but length is still 3×.

3) **Triangle inequality**

‖**u** + **v**‖ ≤ ‖**u**‖ + ‖**v**‖

Intuition: taking two steps (first **u**, then **v**) can’t be shorter than the straight-line shortcut by more than the total step lengths.

### Norms vs dot products (and why you need both)

You said you already know the dot product. Great—because in ℝⁿ the Euclidean norm is closely tied to it:

‖**v**‖₂ = √(**v** · **v**)

But norms are more general than dot products: you can have norms that don’t come from dot products (like ‖·‖₁ and ‖·‖∞). That flexibility is useful: different norms encode different ideas of what it means to be “close,” “large,” or “small.”

### From norms to distances

A norm automatically defines a **distance** (a metric) between two vectors:

d(**x**, **y**) = ‖**x** − **y**‖

So if you choose a norm, you also choose a geometry for your space.

### Common p-norms (preview)

The most used family is the **p-norms**:

‖**v**‖ₚ = (∑ᵢ |vᵢ|ᵖ)¹ᐟᵖ, for p ≥ 1

Special cases you’ll use constantly:

- •p = 1 → ‖**v**‖₁ = ∑ᵢ |vᵢ|
- •p = 2 → ‖**v**‖₂ = √(∑ᵢ vᵢ²)
- •p → ∞ → ‖**v**‖∞ = maxᵢ |vᵢ|

Each is a valid norm, satisfies the three properties, and leads to a different notion of “ball” and “nearest.”

## Core Mechanic 1: Computing L1, L2, and L∞ Norms

### Why these three show up everywhere

When you implement algorithms, you want norms that are:

- •easy to compute
- •meaningful in applications
- •stable in high dimensions

‖·‖₁, ‖·‖₂, and ‖·‖∞ are the standard trio because they emphasize different aspects of a vector:

- •‖**v**‖₁: total magnitude across coordinates (robust, encourages sparsity)
- •‖**v**‖₂: geometric length (rotation-invariant, tied to dot product)
- •‖**v**‖∞: worst-case coordinate (useful for constraints and error bounds)

### Formulas (and what they “measure”)

Let **v** = (v₁, v₂, …, vₙ).

**L1 norm**

‖**v**‖₁ = ∑ᵢ |vᵢ|

Interpretation: add up the absolute contributions of every coordinate.

**L2 (Euclidean) norm**

‖**v**‖₂ = √(∑ᵢ vᵢ²) = √(**v** · **v**)

Interpretation: the usual straight-line length.

**L∞ norm**

‖**v**‖∞ = maxᵢ |vᵢ|

Interpretation: how large the largest-magnitude coordinate is.

### A quick comparison table

| Norm | Formula | What it emphasizes | Typical use |
| --- | --- | --- | --- |
| ‖**v**‖₁ | ∑ᵢ | vᵢ |  | overall “mass” across coordinates | sparsity (L1 regularization), Manhattan distance |
| ‖**v**‖₂ | √(∑ᵢ vᵢ²) | geometric length, energy | geometry, least squares, k-means default |
| ‖**v**‖∞ | maxᵢ | vᵢ |  | worst coordinate | constraint bounds, robust tolerances |

### Unit balls: same rule, different geometry

A great way to *feel* norms is to look at their unit balls in 2D: the set of vectors whose norm ≤ 1.

- •‖**v**‖₂ ≤ 1: a circle
- •‖**v**‖₁ ≤ 1: a diamond (rotated square)
- •‖**v**‖∞ ≤ 1: an axis-aligned square

This matters because “closest point” problems (like clustering) depend on the shape of these balls.

### Scaling behavior (absolute homogeneity in action)

If α is a scalar and **v** is a vector, all norms must satisfy:

‖α**v**‖ = |α| ‖**v**‖

For p-norms, you can see it directly:

‖α**v**‖ₚ

= (∑ᵢ |α vᵢ|ᵖ)¹ᐟᵖ

= (∑ᵢ (|α| |vᵢ|)ᵖ)¹ᐟᵖ

= (∑ᵢ |α|ᵖ |vᵢ|ᵖ)¹ᐟᵖ

= (|α|ᵖ ∑ᵢ |vᵢ|ᵖ)¹ᐟᵖ

= |α| (∑ᵢ |vᵢ|ᵖ)¹ᐟᵖ

= |α| ‖**v**‖ₚ

So p-norms automatically obey one of the key norm axioms.

## Core Mechanic 2: The Three Axioms (and How to Reason With Them)

### Why axioms matter (not just definitions)

When you rely on a norm inside an algorithm, you’re often using its properties implicitly:

- •proving a distance is valid
- •bounding an error
- •showing an optimization problem behaves nicely

The three norm axioms are the “license” that lets you do these steps safely.

### 1) Positive-definiteness: “length is never negative”

For p-norms (p ≥ 1), every term |vᵢ|ᵖ is ≥ 0, so the sum is ≥ 0, so the p-th root is ≥ 0.

Also, ‖**v**‖ₚ = 0 implies:

(∑ᵢ |vᵢ|ᵖ)¹ᐟᵖ = 0

⇒ ∑ᵢ |vᵢ|ᵖ = 0

A sum of nonnegative numbers is 0 only if each term is 0:

∀i, |vᵢ|ᵖ = 0 ⇒ |vᵢ| = 0 ⇒ vᵢ = 0

So **v** = **0**.

### 2) Absolute homogeneity: “scaling scales length”

You already saw the derivation in the previous section. This property is what makes norms behave like a geometric length. It also prevents weird measures like “length(2**v**) = length(**v**) + 7.”

### 3) Triangle inequality: the most powerful rule

Triangle inequality is often the hardest to prove, but the easiest to *use*.

It says:

‖**u** + **v**‖ ≤ ‖**u**‖ + ‖**v**‖

A very common corollary is a bound on differences (sometimes called a reverse triangle inequality variant):

|‖**u**‖ − ‖**v**‖| ≤ ‖**u** − **v**‖

This tells you: if two vectors are close, their lengths are close.

Here’s the derivation using triangle inequality twice.

Start with:

**u** = (**u** − **v**) + **v**

Apply triangle inequality:

‖**u**‖ = ‖(**u** − **v**) + **v**‖ ≤ ‖**u** − **v**‖ + ‖**v**‖

Rearrange:

‖**u**‖ − ‖**v**‖ ≤ ‖**u** − **v**‖ (1)

Swap **u** and **v**:

‖**v**‖ − ‖**u**‖ ≤ ‖**v** − **u**‖ = ‖**u** − **v**‖ (2)

Combine (1) and (2):

|‖**u**‖ − ‖**v**‖| ≤ ‖**u** − **v**‖

This inequality is a frequent tool when analyzing iterative algorithms.

### Norm equivalence intuition (why different norms still relate)

In finite-dimensional spaces like ℝⁿ, all norms are “equivalent” in the sense that they bound each other up to constants. Practically: if one norm is small, the others can’t be arbitrarily huge.

For the three norms we care about, these inequalities are especially useful:

1) ‖**v**‖∞ ≤ ‖**v**‖₂ ≤ ‖**v**‖₁

Reasoning (intuition):

- •the max component can’t exceed the root-sum-squares
- •root-sum-squares can’t exceed the sum of magnitudes

2) And with dimension n, you can also bound the other direction:

‖**v**‖₁ ≤ √n ‖**v**‖₂

‖**v**‖₂ ≤ √n ‖**v**‖∞

These tell you a key high-dimensional fact: the gap between norms can grow with √n. So in large n, your choice of norm can meaningfully change distances and nearest neighbors.

### A note about p < 1

You might see “‖**v**‖ₚ” written for p < 1 in some ML contexts (e.g., sparsity). But for p < 1, triangle inequality fails, so it’s not a true norm. People still use it as a penalty, but you lose some guarantees.

## Application/Connection: Norms as Distances in Clustering (and Why Choice Matters)

### Why clustering cares about norms

Clustering groups points by proximity. But “proximity” is defined by a distance, and a distance is often built from a norm:

- •L2 distance: d₂(**x**, **y**) = ‖**x** − **y**‖₂
- •L1 distance: d₁(**x**, **y**) = ‖**x** − **y**‖₁
- •L∞ distance: d∞(**x**, **y**) = ‖**x** − **y**‖∞

Change the norm → change the geometry → change which points are nearest → change the clustering.

### K-means and why it “likes” L2

Classic k-means is typically presented with squared Euclidean distance:

minimize ∑ (over points **x**) ‖**x** − **μ**(cluster(**x**))‖₂²

Why L2²? Because it pairs perfectly with means.

If you take a single cluster and want the best center **c** to minimize:

J(**c**) = ∑ᵢ ‖**x**ᵢ − **c**‖₂²

the minimizer is the componentwise mean. That makes the update step simple and fast.

(If you instead used L1 distance, the best “center” is a **median** per coordinate, leading to k-medians. So the norm choice changes the algorithm’s natural center.)

### L1 distance: robustness and “city block” geometry

With L1, distances add coordinate-wise. This can be more robust to outliers in some settings and can better match data where moving along axes is natural (think grid/city streets).

Geometrically, L1 balls are diamonds in 2D. That tends to create cluster boundaries aligned differently than L2.

### L∞ distance: worst-case deviation

L∞ treats the distance between **x** and **y** as the largest coordinate difference:

‖**x** − **y**‖∞ = maxᵢ |xᵢ − yᵢ|

This is useful when you care about **maximum error** in any feature (e.g., tolerances). In clustering, it makes points “close” if they’re close in every coordinate (no big deviation allowed).

### Practical guidance: choosing a norm

| If your notion of similarity is… | Consider | Why |
| --- | --- | --- |
| straight-line geometric closeness | L2 | rotation-invariant, common default |
| total absolute deviation across features | L1 | robust-ish, encourages axis-aligned structure |
| worst-feature deviation must be small | L∞ | enforces uniform closeness across coordinates |

### Norms, scaling, and feature normalization

Norm-based distances are sensitive to units. If one coordinate is measured in dollars and another in millimeters, the large-scale coordinate can dominate any norm.

A common fix is to normalize features (e.g., z-score standardization). This is not a norm concept by itself, but norms make the need obvious: the distance ‖**x** − **y**‖ depends on coordinate scales.

### Connecting back to dot product

Because ‖**v**‖₂ = √(**v** · **v**), anything that uses dot products often implicitly uses L2 norms. Examples:

- •cosine similarity uses **x** · **y** / (‖**x**‖₂ ‖**y**‖₂)
- •projections and orthogonality rely on L2 geometry

So norms complete the story: dot products measure alignment; norms measure magnitude; together they describe angle and distance.

## Worked Examples (3)

### Compute ‖\*\*v\*\*‖₁, ‖\*\*v\*\*‖₂, and ‖\*\*v\*\*‖∞ for a concrete vector

Let **v** = (3, −4, 12). Compute the L1, L2, and L∞ norms.

1. Compute L1:

   ‖**v**‖₁ = |3| + |−4| + |12|

   = 3 + 4 + 12

   = 19
2. Compute L2:

   ‖**v**‖₂ = √(3² + (−4)² + 12²)

   = √(9 + 16 + 144)

   = √169

   = 13
3. Compute L∞:

   ‖**v**‖∞ = max(|3|, |−4|, |12|)

   = max(3, 4, 12)

   = 12

**Insight:** Each norm answers a different question: L1 totals all coordinate magnitudes (19), L2 gives geometric length (13), and L∞ reports the largest coordinate magnitude (12).

### Use triangle inequality to bound a hard-to-compute norm

Let **u** and **v** be vectors. Suppose ‖**u**‖₂ = 5 and ‖**v**‖₂ = 2. You do not know the angle between them. Bound ‖**u** + **v**‖₂ and also bound the possible values of ‖**u** − **v**‖₂.

1. Upper bound ‖**u** + **v**‖₂ using triangle inequality:

   ‖**u** + **v**‖₂ ≤ ‖**u**‖₂ + ‖**v**‖₂

   = 5 + 2

   = 7
2. Lower bound ‖**u** + **v**‖₂ using the reverse-triangle form:

   |‖**u**‖₂ − ‖**v**‖₂| ≤ ‖**u** + **v**‖₂

   So:

   ‖**u** + **v**‖₂ ≥ |5 − 2| = 3
3. So the combined bound is:

   3 ≤ ‖**u** + **v**‖₂ ≤ 7
4. Now bound ‖**u** − **v**‖₂ similarly.

   Triangle inequality gives:

   ‖**u** − **v**‖₂ ≤ ‖**u**‖₂ + ‖**v**‖₂ = 7
5. Reverse-triangle gives:

   ‖**u** − **v**‖₂ ≥ |‖**u**‖₂ − ‖**v**‖₂| = 3
6. So:

   3 ≤ ‖**u** − **v**‖₂ ≤ 7

**Insight:** Even without knowing directions, the norm axioms let you bound outcomes. In algorithms, these bounds can guarantee stability (values can’t blow up unexpectedly).

### How norm choice changes which point is closer

Let **a** = (2, 0) and **b** = (1, 1). Compare their distances to the origin under L1, L2, and L∞.

1. Compute norms for **a**:

   ‖**a**‖₁ = |2| + |0| = 2

   ‖**a**‖₂ = √(2² + 0²) = √4 = 2

   ‖**a**‖∞ = max(|2|, |0|) = 2
2. Compute norms for **b**:

   ‖**b**‖₁ = |1| + |1| = 2

   ‖**b**‖₂ = √(1² + 1²) = √2 ≈ 1.414

   ‖**b**‖∞ = max(|1|, |1|) = 1
3. Compare:

   - •Under L1: tie (both 2)
   - •Under L2: **b** is closer (≈ 1.414 < 2)
   - •Under L∞: **b** is closer (1 < 2)

**Insight:** Two points can be equally close under one norm and not under another. That’s why changing the norm can change nearest neighbors and therefore clustering results.

## Key Takeaways

- ✓

  A norm ‖**v**‖ is a consistent notion of vector length: nonnegative, zero only at **0**, scales as |α|, and satisfies triangle inequality.
- ✓

  The p-norms (p ≥ 1) are defined by ‖**v**‖ₚ = (∑ᵢ |vᵢ|ᵖ)¹ᐟᵖ; common cases are p = 1, 2, and ∞.
- ✓

  ‖**v**‖₁ measures total absolute magnitude, ‖**v**‖₂ measures Euclidean length, and ‖**v**‖∞ measures the largest coordinate magnitude.
- ✓

  Every norm induces a distance: d(**x**, **y**) = ‖**x** − **y**‖, so choosing a norm chooses your geometry.
- ✓

  Triangle inequality enables powerful bounds like |‖**u**‖ − ‖**v**‖| ≤ ‖**u** − **v**‖, useful for analysis and stability.
- ✓

  In ℝⁿ, norms bound each other (e.g., ‖**v**‖∞ ≤ ‖**v**‖₂ ≤ ‖**v**‖₁), but the gaps can grow with dimension.
- ✓

  Clustering and nearest-neighbor behavior can change significantly depending on whether you use L1, L2, or L∞ distances.

## Common Mistakes

- ✗

  Forgetting absolute values in ‖**v**‖₁ or ‖**v**‖∞ (signs don’t cancel in norms).
- ✗

  Mixing up ‖**v**‖₂ with ∑ᵢ vᵢ² (the L2 norm includes a square root).
- ✗

  Assuming “‖·‖ₚ” is always a norm for any p; for p < 1, triangle inequality fails.
- ✗

  Comparing distances without considering feature scaling; one large-scale coordinate can dominate any norm-based distance.

## Practice

easy

Let **v** = (−1, 2, −2, 4). Compute ‖**v**‖₁, ‖**v**‖₂, and ‖**v**‖∞.

**Hint:** Use absolute values for L1 and L∞. For L2, square first, then sum, then take √.

Show solution

‖**v**‖₁ = |−1|+|2|+|−2|+|4| = 1+2+2+4 = 9.

‖**v**‖₂ = √((−1)²+2²+(−2)²+4²) = √(1+4+4+16) = √25 = 5.

‖**v**‖∞ = max(1,2,2,4) = 4.

medium

Suppose ‖**u**‖₁ = 10 and ‖**v**‖₁ = 6. Give the tightest bounds you can (using only norm axioms) for ‖**u** + **v**‖₁.

**Hint:** Use triangle inequality for an upper bound and the reverse-triangle form for a lower bound.

Show solution

Upper bound: ‖**u**+**v**‖₁ ≤ ‖**u**‖₁ + ‖**v**‖₁ = 16.

Lower bound: |‖**u**‖₁ − ‖**v**‖₁| ≤ ‖**u**+**v**‖₁ ⇒ ‖**u**+**v**‖₁ ≥ |10−6| = 4.

So 4 ≤ ‖**u**+**v**‖₁ ≤ 16.

medium

Find a nonzero vector **v** ∈ ℝ² such that ‖**v**‖₁ = 2 but ‖**v**‖∞ = 1. Then compute ‖**v**‖₂.

**Hint:** You want the max coordinate magnitude to be 1, and the sum of absolute values to be 2.

Show solution

One example is **v** = (1, 1). Then ‖**v**‖₁ = |1|+|1|=2 and ‖**v**‖∞=max(1,1)=1.

Compute L2: ‖**v**‖₂ = √(1²+1²) = √2.

## Connections

Prerequisite reinforcement: [Dot Product](/tech-tree/dot-product/)

Unlocks and next steps: [Clustering](/tech-tree/clustering/)

Related ideas you’ll likely meet soon:

- •[Distances & Metrics](/tech-tree/metrics/)
- •[Cosine Similarity](/tech-tree/cosine-similarity/)
- •[Regularization (L1 vs L2)](/tech-tree/regularization/)

Quality: B (4.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
