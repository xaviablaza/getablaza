---
title: Cosine Similarity
description: A measure of similarity between two vectors defined as the cosine of the angle between them (dot product normalized by norms); used as an attention scoring function and for comparing embeddings. It highlights direction-based similarity independent of vector magnitude.
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
permalink: /tech-tree/cosine-similarity/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Cosine Similarity

Linear AlgebraDifficulty: ★★★☆☆Depth: 0Unlocks: 3

A measure of similarity between two vectors defined as the cosine of the angle between them (dot product normalized by norms); used as an attention scoring function and for comparing embeddings. It highlights direction-based similarity independent of vector magnitude.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Vector as an ordered list of numeric components (a point or direction in coordinate space)
- -Dot product: sum of pairwise products of vector components (captures directional alignment)
- -Euclidean norm (vector magnitude): square root of sum of squared components (vector length)

## Key Symbols & Notation

dot(a,b) (dot product of vectors a and b)||a|| (Euclidean norm/magnitude of vector a)

## Essential Relationships

- -cosine\_similarity(a,b) = dot(a,b) / (||a|| \* ||b||), which equals the cosine of the angle between a and b and therefore ranges from -1 to 1

## Unlocks (2)

[Attention Mechanismslvl 5](/tech-tree/attention-mechanisms/)[Vector Embeddingslvl 4](/tech-tree/vector-embeddings/)

Advanced Learning Details

### Graph Position

6

Depth Cost

3

Fan-Out (ROI)

1

Bottleneck Score

0

Chain Length

### Cognitive Load

6

Atomic Elements

25

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (10)

- - cosine similarity (a similarity measure defined as the cosine of the angle between two vectors)
- - dot product / inner product (algebraic product that combines corresponding components of two vectors)
- - vector norm (magnitude of a vector, often written ||v||)
- - angle between vectors (geometric angle θ whose cosine measures directional alignment)
- - normalization by norms (dividing the dot product by the product of vector norms)
- - direction-based similarity / scale invariance (similarity that depends on direction not magnitude)
- - interpretation of cosine values and their range (cosine similarity values lie in [-1,1] with semantic meaning)
- - embeddings (vectors that encode items/words/features to be compared via similarity)
- - attention scoring function (using cosine similarity as a score to determine relevance/weights)
- - cosine function as mapping from angle to similarity (cos(θ) mapping angle to a numeric similarity)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

When you compare two vectors, you often care less about how big they are and more about whether they “point” in the same direction. Cosine similarity is the standard tool for measuring that directional agreement—and it shows up everywhere from search and embeddings to attention scores in transformers.

TL;DR:

Cosine similarity between two nonzero vectors **a** and **b** is

cosSim(a,b)=a⋅b∥a∥ ∥b∥\mathrm{cosSim}(\mathbf{a},\mathbf{b}) = \frac{\mathbf{a}\cdot\mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}cosSim(a,b)=∥a∥∥b∥a⋅b​

It equals the cosine of the angle between them: 1 means same direction, 0 means orthogonal (no directional alignment), −1 means opposite direction. It’s magnitude-invariant (scaling a vector doesn’t change it), which makes it ideal for comparing embeddings and as an attention scoring function. Be careful: both vectors must be nonzero, and “cosine distance = 1 − cosSim” is commonly used but is not a true metric in general (triangle inequality can fail).

## Prerequisites (quick but explicit)

This node is meant to be foundational, but cosine similarity *does* assume a few micro-skills. Here’s a compact checklist.

### You should recognize these ideas

| Concept | Meaning | Formula / Note |
| --- | --- | --- |
| Vector **a** | Ordered list of numbers | **a** = (a₁, a₂, …, aₙ) |
| Dot product | Measures alignment via componentwise multiplication | $a⋅b=∑i=1naibi\mathbf{a}\cdot\mathbf{b}=\sum\_{i=1}^n a\_i b\_ia⋅b=∑i=1n​ai​bi​$ |
| Euclidean norm | Vector “length” (magnitude) | $$\ | \mathbf{a}\ | = \sqrt{\sum\_{i=1}^n a\_i^2}$$ |
| Angle interpretation | In geometry, dot relates to cos(angle) | $$\mathbf{a}\cdot\mathbf{b}=\ | \mathbf{a}\ | \,\ | \mathbf{b}\ | \cos\theta$$ |
| Nonzero requirement | Cosine similarity divides by norms | Need \ | **a**\ | > 0 and \ | **b**\ | > 0 |

### Two common terminology notes

1. 1)**Cosine similarity** is the value cos⁡θ\cos\thetacosθ (range [−1, 1] in general).
2. 2)People often define **cosine distance** as $1 - \mathrm{cosSim}(\mathbf{a},\mathbf{b})$. This is *useful*, but it is **not guaranteed to be a metric** on all vectors because the **triangle inequality can fail**. (It may behave metrically only under additional constraints, e.g., certain normalized nonnegative settings.)

If those boxes feel unfamiliar, you can still proceed—just revisit them when the formulas appear.

## What Is Cosine Similarity?

### Why we need a “direction-only” similarity

Suppose you have two vectors representing items:

- •in search: document embedding vs query embedding
- •in recommendation: user embedding vs item embedding
- •in NLP: token embeddings interacting inside attention

Often, the *direction* encodes the “type” or “meaning,” while the *length* might reflect confidence, frequency, or just the model’s internal scaling.

If we used only the dot product a⋅b\mathbf{a}\cdot\mathbf{b}a⋅b to score similarity, then simply making vectors longer (larger magnitude) would inflate the score—even if the direction stayed the same. That can be undesirable when you want comparisons to be about alignment.

Cosine similarity fixes this by normalizing out the magnitudes.

### Definition

For two **nonzero** vectors **a** and **b** in ℝⁿ, cosine similarity is

cosSim(a,b)=a⋅b∥a∥ ∥b∥.\mathrm{cosSim}(\mathbf{a},\mathbf{b}) = \frac{\mathbf{a}\cdot\mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}.cosSim(a,b)=∥a∥∥b∥a⋅b​.

### Geometric meaning: “cosine of the angle”

There is a key identity connecting dot product and angle:

a⋅b=∥a∥ ∥b∥cos⁡θ,\mathbf{a}\cdot\mathbf{b} = \|\mathbf{a}\|\,\|\mathbf{b}\|\cos\theta,a⋅b=∥a∥∥b∥cosθ,

where θ\thetaθ is the angle between **a** and **b** (in the usual Euclidean geometry). Rearranging gives

cos⁡θ=a⋅b∥a∥ ∥b∥=cosSim(a,b).\cos\theta = \frac{\mathbf{a}\cdot\mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|} = \mathrm{cosSim}(\mathbf{a},\mathbf{b}).cosθ=∥a∥∥b∥a⋅b​=cosSim(a,b).

So cosine similarity literally *is* the cosine of that angle.

### Interpreting the value

Because cosine ranges between −1 and 1:

- •**1**: vectors point the same direction (θ = 0°)
- •**0**: vectors are orthogonal / perpendicular (θ = 90°)
- •**−1**: vectors point in opposite directions (θ = 180°)

In many embedding systems (especially after certain training setups), values are often mostly positive, but mathematically the full range [−1, 1] is possible.

### Important constraint: nonzero vectors

The formula divides by ∥a∥ ∥b∥\|\mathbf{a}\|\,\|\mathbf{b}\|∥a∥∥b∥. If either vector is **0**, then cosine similarity is undefined.

In practice, systems either:

- •ensure embeddings are never zero,
- •add a tiny ε to the denominator, or
- •define a special-case behavior (but this is application-specific).

## Core Mechanic 1: Dot Product as Alignment (and why normalization matters)

### The dot product mixes direction and magnitude

The dot product is

a⋅b=∑i=1naibi.\mathbf{a}\cdot\mathbf{b} = \sum\_{i=1}^n a\_i b\_i.a⋅b=i=1∑n​ai​bi​.

It increases when:

1) components match in sign and are large in magnitude, and

2) the vectors point in similar directions.

But here’s the catch: if you scale **a** by a constant ccc, then

(ca)⋅b=c(a⋅b).(c\mathbf{a})\cdot\mathbf{b} = c(\mathbf{a}\cdot\mathbf{b}).(ca)⋅b=c(a⋅b).

So dot product is *not* scale-invariant.

### A concrete example: same direction, inflated score

Let

- •**a** = (1, 1)
- •**b** = (2, 2)
- •**c** = (100, 100)

These all point in the same direction (45° line). Dot products:

- •**a**·**b** = 1·2 + 1·2 = 4
- •**a**·**c** = 1·100 + 1·100 = 200

The second looks “more similar” by dot product, but **b** and **c** are equally aligned with **a**—they just have different lengths.

### Normalization removes the scale

Cosine similarity divides by both lengths:

cosSim(a,b)=a⋅b∥a∥ ∥b∥.\mathrm{cosSim}(\mathbf{a},\mathbf{b}) = \frac{\mathbf{a}\cdot\mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}.cosSim(a,b)=∥a∥∥b∥a⋅b​.

Now see what happens if we scale **a** by c>0c>0c>0:

\n**Show your work (scale invariance)**

Let **a'** = c**a**.

1) Dot product scales:

a′⋅b=(ca)⋅b=c(a⋅b).\mathbf{a'}\cdot\mathbf{b} = (c\mathbf{a})\cdot\mathbf{b} = c(\mathbf{a}\cdot\mathbf{b}).a′⋅b=(ca)⋅b=c(a⋅b).

2) Norm scales:

∥a′∥=∥ca∥=∣c∣ ∥a∥=c∥a∥(c>0).\|\mathbf{a'}\| = \|c\mathbf{a}\| = |c|\,\|\mathbf{a}\| = c\|\mathbf{a}\| \quad (c>0).∥a′∥=∥ca∥=∣c∣∥a∥=c∥a∥(c>0).

3) Plug into cosine similarity:

cosSim(a′,b)=c(a⋅b)(c∥a∥) ∥b∥=a⋅b∥a∥ ∥b∥.\mathrm{cosSim}(\mathbf{a'},\mathbf{b}) = \frac{c(\mathbf{a}\cdot\mathbf{b})}{(c\|\mathbf{a}\|)\,\|\mathbf{b}\|} = \frac{\mathbf{a}\cdot\mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}.cosSim(a′,b)=(c∥a∥)∥b∥c(a⋅b)​=∥a∥∥b∥a⋅b​.

So cosine similarity does not change when you scale one vector by a positive constant.

### Unit vectors make the idea even clearer

Define normalized (unit-length) vectors:

a^=a∥a∥,b^=b∥b∥.\hat{\mathbf{a}} = \frac{\mathbf{a}}{\|\mathbf{a}\|}, \quad \hat{\mathbf{b}} = \frac{\mathbf{b}}{\|\mathbf{b}\|}.a^=∥a∥a​,b^=∥b∥b​.

Then

cosSim(a,b)=a^⋅b^.\mathrm{cosSim}(\mathbf{a},\mathbf{b}) = \hat{\mathbf{a}}\cdot\hat{\mathbf{b}}.cosSim(a,b)=a^⋅b^.

This is a powerful mental model:

- •cosine similarity = dot product *after* both vectors are projected onto the unit sphere.
- •all comparisons become “angle comparisons” rather than “length comparisons.”

### Range and the Cauchy–Schwarz inequality

A key guarantee is that cosine similarity is always between −1 and 1.

Cauchy–Schwarz says:

∣a⋅b∣≤∥a∥ ∥b∥.|\mathbf{a}\cdot\mathbf{b}| \le \|\mathbf{a}\|\,\|\mathbf{b}\|.∣a⋅b∣≤∥a∥∥b∥.

Divide both sides by ∥a∥ ∥b∥\|\mathbf{a}\|\,\|\mathbf{b}\|∥a∥∥b∥ (nonzero assumption):

∣a⋅b∥a∥ ∥b∥∣≤1.\left|\frac{\mathbf{a}\cdot\mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}\right| \le 1.​∥a∥∥b∥a⋅b​​≤1.

So

−1≤cosSim(a,b)≤1.-1 \le \mathrm{cosSim}(\mathbf{a},\mathbf{b}) \le 1.−1≤cosSim(a,b)≤1.

This boundedness is one reason cosine similarity is numerically and conceptually convenient.

## Core Mechanic 2: Angle, Sign, and What “Similarity” Really Means

### Cosine similarity is fundamentally about *angle*

Because cosSim(a,b)=cos⁡θ\mathrm{cosSim}(\mathbf{a},\mathbf{b}) = \cos\thetacosSim(a,b)=cosθ, it inherits the cosine curve’s behavior:

- •Small angles (θ near 0): cosine near 1 → high similarity
- •Medium angles (θ near 90°): cosine near 0 → “unrelated directions”
- •Large angles (θ near 180°): cosine near −1 → opposite directions

This is slightly different from many intuitive “distance” notions.

### Negative cosine similarity: when opposite directions matter

In some applications, negative similarity has a clear meaning:

- •In sentiment-like axes, one direction might correspond to “positive,” opposite to “negative.”
- •In some factor models, opposite direction can encode opposing preferences.

In other applications (e.g., some retrieval systems), negative values might just be treated as “not similar” and thresholded away.

### Relation to Euclidean distance (when vectors are normalized)

If both vectors are normalized to unit length, then cosine similarity and Euclidean distance are tightly connected.

Let a^\hat{\mathbf{a}}a^ and b^\hat{\mathbf{b}}b^ be unit vectors. Consider squared Euclidean distance:

\n**Show your work**

∥a^−b^∥2=(a^−b^)⋅(a^−b^).\|\hat{\mathbf{a}} - \hat{\mathbf{b}}\|^2 = (\hat{\mathbf{a}} - \hat{\mathbf{b}})\cdot(\hat{\mathbf{a}} - \hat{\mathbf{b}}).∥a^−b^∥2=(a^−b^)⋅(a^−b^).

Expand:

=a^⋅a^−2a^⋅b^+b^⋅b^.= \hat{\mathbf{a}}\cdot\hat{\mathbf{a}} - 2\hat{\mathbf{a}}\cdot\hat{\mathbf{b}} + \hat{\mathbf{b}}\cdot\hat{\mathbf{b}}.=a^⋅a^−2a^⋅b^+b^⋅b^.

Since both are unit length:

a^⋅a^=1,b^⋅b^=1.\hat{\mathbf{a}}\cdot\hat{\mathbf{a}} = 1, \quad \hat{\mathbf{b}}\cdot\hat{\mathbf{b}} = 1.a^⋅a^=1,b^⋅b^=1.

So

∥a^−b^∥2=2−2(a^⋅b^)=2−2 cosSim(a,b).\|\hat{\mathbf{a}} - \hat{\mathbf{b}}\|^2 = 2 - 2(\hat{\mathbf{a}}\cdot\hat{\mathbf{b}}) = 2 - 2\,\mathrm{cosSim}(\mathbf{a},\mathbf{b}).∥a^−b^∥2=2−2(a^⋅b^)=2−2cosSim(a,b).

Rearrange:

cosSim(a,b)=1−12∥a^−b^∥2.\mathrm{cosSim}(\mathbf{a},\mathbf{b}) = 1 - \frac{1}{2}\|\hat{\mathbf{a}} - \hat{\mathbf{b}}\|^2.cosSim(a,b)=1−21​∥a^−b^∥2.

So on the unit sphere, cosine similarity is basically a monotonic transformation of Euclidean distance.

### Cosine distance is common but not a guaranteed metric

A frequently used “distance-like” quantity is

dcos⁡(a,b)=1−cosSim(a,b).d\_{\cos}(\mathbf{a},\mathbf{b}) = 1 - \mathrm{cosSim}(\mathbf{a},\mathbf{b}).dcos​(a,b)=1−cosSim(a,b).

This has nice properties (0 when vectors match in direction, bigger when they differ), but **it is not always a metric** on ℝⁿ. In particular, the **triangle inequality** may fail.

Why that matters:

- •Some algorithms (certain clustering/indexing schemes) assume a true metric.
- •If you plug in a non-metric distance, you can get subtle correctness/performance issues.

Practical takeaway: it’s fine to use $1-\cos$ as a heuristic distance for ranking and optimization, but don’t automatically assume metric guarantees unless you’ve checked the conditions for your specific setting.

### Implementation note: numerical stability

When vectors are very small or nearly zero, the denominator ∥a∥ ∥b∥\|\mathbf{a}\|\,\|\mathbf{b}\|∥a∥∥b∥ can be tiny.

Common fix:

cosSimε(a,b)=a⋅bmax⁡(∥a∥ ∥b∥,ε)\mathrm{cosSim}\_\varepsilon(\mathbf{a},\mathbf{b}) = \frac{\mathbf{a}\cdot\mathbf{b}}{\max(\|\mathbf{a}\|\,\|\mathbf{b}\|,\varepsilon)}cosSimε​(a,b)=max(∥a∥∥b∥,ε)a⋅b​

or add ε inside the product. The exact choice depends on your numerical environment and expectations about zero vectors.

## Application/Connection: Embeddings, Retrieval, and Attention Scoring

### 1) Comparing embeddings (semantic similarity)

Embeddings map discrete objects (words, items, images) to vectors. A core assumption is:

- •**direction** corresponds to “meaning/features”
- •**closeness in angle** corresponds to similarity

Cosine similarity is a natural fit because it ignores overall magnitude. This is especially helpful when vector norms vary due to:

- •frequency effects (common words can have different scales)
- •training dynamics
- •model architecture (some layers output vectors with varying norms)

**Typical retrieval pipeline**

1. 1)Compute embedding for query **q** and for each candidate item **xᵢ**.
2. 2)Score each candidate with cosSim(q,xi)\mathrm{cosSim}(\mathbf{q},\mathbf{x}\_i)cosSim(q,xi​).
3. 3)Return top-k.

Often, systems normalize all embeddings once (store unit vectors), making scoring just a dot product.

### 2) Cosine similarity as an attention score

In attention mechanisms, we produce:

- •queries **q**
- •keys **k**
- •values **v**

A general attention score between a query and key can be any similarity function. One simple option is cosine similarity:

s(q,k)=q⋅k∥q∥ ∥k∥.s(\mathbf{q},\mathbf{k}) = \frac{\mathbf{q}\cdot\mathbf{k}}{\|\mathbf{q}\|\,\|\mathbf{k}\|}.s(q,k)=∥q∥∥k∥q⋅k​.

Then attention weights are typically:

αi=softmax(s(q,ki)).\alpha\_i = \mathrm{softmax}(s(\mathbf{q},\mathbf{k}\_i)).αi​=softmax(s(q,ki​)).

In modern transformers, the most common is **scaled dot-product attention**:

s(q,k)=q⋅kdk.s(\mathbf{q},\mathbf{k}) = \frac{\mathbf{q}\cdot\mathbf{k}}{\sqrt{d\_k}}.s(q,k)=dk​​q⋅k​.

Why not always cosine?

- •Cosine similarity forces magnitude invariance; sometimes magnitude contains useful information.
- •Scaled dot product is cheaper if you already have vectors and don’t want norms.
- •With layer normalization and training, dot-product attention can behave stably.

That said, cosine attention variants exist and can be helpful in some regimes.

### 3) Practical tradeoffs: dot product vs cosine similarity

| Scoring | Formula | Sensitive to vector length? | Common use |
| --- | --- | --- | --- |
| Dot product | **a**·**b** | Yes | Many attention layers; fast retrieval if norms are controlled |
| Cosine similarity | (**a**·**b**)/(\ | **a**\ | \ | **b**\ | ) | No (direction only) | Embedding similarity; some attention variants |
| Euclidean distance | \ | **a**−**b**\ |  | Yes (unless normalized) | Clustering; geometry on unit sphere connects it to cosine |

### 4) A workflow pattern: normalize once, then dot

Because

cosSim(a,b)=a^⋅b^,\mathrm{cosSim}(\mathbf{a},\mathbf{b}) = \hat{\mathbf{a}}\cdot\hat{\mathbf{b}},cosSim(a,b)=a^⋅b^,

a very common engineering trick is:

1) store x^=x/∥x∥\hat{\mathbf{x}} = \mathbf{x}/\|\mathbf{x}\|x^=x/∥x∥ for every embedding

2) compute similarity as a dot product

This can speed up retrieval (especially with vector databases / ANN indices) because dot products are highly optimized.

## Worked Examples (3)

### Compute cosine similarity in 2D (with full arithmetic)

Let **a** = (3, 4) and **b** = (4, 0). Compute cosSim(**a**, **b**) and interpret the result.

1. Compute the dot product:

   \n$a⋅b=3⋅4+4⋅0=12.\mathbf{a}\cdot\mathbf{b} = 3\cdot 4 + 4\cdot 0 = 12.a⋅b=3⋅4+4⋅0=12.$
2. Compute the norms:

   \n$∥a∥=32+42=9+16=5,\|\mathbf{a}\| = \sqrt{3^2 + 4^2} = \sqrt{9+16} = 5,∥a∥=32+42​=9+16​=5,$

   ∥b∥=42+02=16=4.\|\mathbf{b}\| = \sqrt{4^2 + 0^2} = \sqrt{16} = 4.∥b∥=42+02​=16​=4.
3. Plug into cosine similarity:

   \n$cosSim(a,b)=125⋅4=1220=0.6.\mathrm{cosSim}(\mathbf{a},\mathbf{b}) = \frac{12}{5\cdot 4} = \frac{12}{20} = 0.6.cosSim(a,b)=5⋅412​=2012​=0.6.$
4. Interpretation:

   A cosine similarity of 0.6 means the vectors form an acute angle with moderate alignment (since 1 would be perfectly aligned, 0 would be perpendicular). If you want the angle explicitly:

   \n$θ=arccos⁡(0.6)≈53.13∘.\theta = \arccos(0.6) \approx 53.13^\circ.θ=arccos(0.6)≈53.13∘.$

**Insight:** Cosine similarity turned the raw dot product (12) into a bounded, scale-free score (0.6). The value directly corresponds to an angle, which is a clean geometric notion of similarity.

### Magnitude invariance: two vectors with the same direction score equally

Let **q** = (1, 2). Compare **x₁** = (2, 4) and **x₂** = (10, 20) by cosine similarity with **q**.

1. Notice that **x₁** = 2**q** and **x₂** = 10**q**, so all three vectors point in the same direction.
2. Compute cosSim(**q**, **x₁**):

   \nDot:

   q⋅x1=1⋅2+2⋅4=2+8=10.\mathbf{q}\cdot\mathbf{x}\_1 = 1\cdot 2 + 2\cdot 4 = 2 + 8 = 10.q⋅x1​=1⋅2+2⋅4=2+8=10.

   Norms:

   ∥q∥=12+22=5,∥x1∥=22+42=20=25.\|\mathbf{q}\|=\sqrt{1^2+2^2}=\sqrt{5},\quad \|\mathbf{x}\_1\|=\sqrt{2^2+4^2}=\sqrt{20}=2\sqrt{5}.∥q∥=12+22​=5​,∥x1​∥=22+42​=20​=25​.

   Cosine:

   cosSim(q,x1)=10(5)(25)=1010=1.\mathrm{cosSim}(\mathbf{q},\mathbf{x}\_1)=\frac{10}{(\sqrt{5})(2\sqrt{5})}=\frac{10}{10}=1.cosSim(q,x1​)=(5​)(25​)10​=1010​=1.
3. Compute cosSim(**q**, **x₂**) similarly:

   \nDot:

   q⋅x2=1⋅10+2⋅20=10+40=50.\mathbf{q}\cdot\mathbf{x}\_2 = 1\cdot 10 + 2\cdot 20 = 10 + 40 = 50.q⋅x2​=1⋅10+2⋅20=10+40=50.

   Norms:

   ∥x2∥=102+202=500=105.\|\mathbf{x}\_2\|=\sqrt{10^2+20^2}=\sqrt{500}=10\sqrt{5}.∥x2​∥=102+202​=500​=105​.

   Cosine:

   cosSim(q,x2)=50(5)(105)=5050=1.\mathrm{cosSim}(\mathbf{q},\mathbf{x}\_2)=\frac{50}{(\sqrt{5})(10\sqrt{5})}=\frac{50}{50}=1.cosSim(q,x2​)=(5​)(105​)50​=5050​=1.
4. Compare with dot products:

   \n$q⋅x1=10,q⋅x2=50.\mathbf{q}\cdot\mathbf{x}\_1 = 10,\quad \mathbf{q}\cdot\mathbf{x}\_2 = 50.q⋅x1​=10,q⋅x2​=50.$

   Dot product prefers **x₂** purely because it is longer, while cosine similarity treats them as equally aligned.

**Insight:** Cosine similarity answers: “Do these vectors point the same way?” Dot product answers: “Are these vectors aligned and large?” That difference is exactly why cosine is popular for embedding comparisons.

### Zero vector edge case (why the nonzero requirement exists)

Let **a** = (0, 0, 0) and **b** = (1, −2, 3). Try to compute cosSim(**a**, **b**).

1. Compute the dot product:

   \n$a⋅b=0⋅1+0⋅(−2)+0⋅3=0.\mathbf{a}\cdot\mathbf{b} = 0\cdot 1 + 0\cdot (-2) + 0\cdot 3 = 0.a⋅b=0⋅1+0⋅(−2)+0⋅3=0.$
2. Compute the norms:

   \n$∥a∥=02+02+02=0,∥b∥=12+(−2)2+32=14.\|\mathbf{a}\| = \sqrt{0^2+0^2+0^2} = 0,\quad \|\mathbf{b}\| = \sqrt{1^2+(-2)^2+3^2} = \sqrt{14}.∥a∥=02+02+02​=0,∥b∥=12+(−2)2+32​=14​.$
3. Plug into the formula:

   \n$cosSim(a,b)=00⋅14=00,\mathrm{cosSim}(\mathbf{a},\mathbf{b}) = \frac{0}{0\cdot \sqrt{14}} = \frac{0}{0},cosSim(a,b)=0⋅14​0​=00​,$

   which is undefined.
4. Practical resolution:

   If your system might produce zero vectors, you must decide on a policy: reject them, renormalize differently, or use an ε-stabilized denominator.

**Insight:** Cosine similarity is about direction, but the zero vector has no direction. The undefined division is not a nuisance—it reflects a real geometric ambiguity.

## Key Takeaways

- ✓

  Cosine similarity measures directional alignment: $cosSim(a,b)=a⋅b∥a∥ ∥b∥=cos⁡θ.\mathrm{cosSim}(\mathbf{a},\mathbf{b})=\frac{\mathbf{a}\cdot\mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|} = \cos\theta.cosSim(a,b)=∥a∥∥b∥a⋅b​=cosθ.$
- ✓

  It requires **nonzero vectors**; the zero vector has no direction, so cosine similarity is undefined with it.
- ✓

  Cosine similarity is scale-invariant: multiplying a vector by a positive constant does not change the score.
- ✓

  Values interpret cleanly: 1 (same direction), 0 (orthogonal), −1 (opposite direction).
- ✓

  If you normalize vectors to unit length, cosine similarity becomes just a dot product: a^⋅b^\hat{\mathbf{a}}\cdot\hat{\mathbf{b}}a^⋅b^.
- ✓

  Cauchy–Schwarz guarantees the score lies in [−1, 1].
- ✓

  “Cosine distance” defined as $1-\mathrm{cosSim}$ is widely used but is **not guaranteed to be a metric** (triangle inequality may fail).
- ✓

  Cosine similarity is common for comparing embeddings and can serve as an attention scoring function when magnitude should be ignored.

## Common Mistakes

- ✗

  Forgetting the nonzero requirement and attempting to compute cosine similarity with a zero vector (division by zero / undefined direction).
- ✗

  Using dot product as if it were cosine similarity (confusing “large magnitude” with “high similarity”).
- ✗

  Assuming cosine distance $1-\cos$ is always a true metric and using it in algorithms that require triangle inequality guarantees.
- ✗

  Interpreting cosine similarity as a probability or as bounded to [0, 1] without justification (it can be negative).

## Practice

easy

Compute cosSim(**a**, **b**) for **a** = (1, −1, 2) and **b** = (2, 0, 1).

**Hint:** Compute the dot product and each norm separately, then divide. Keep radicals until the end if you want exact form.

Show solution

Dot:

a⋅b=1⋅2+(−1)⋅0+2⋅1=2+0+2=4.\mathbf{a}\cdot\mathbf{b} = 1\cdot 2 + (-1)\cdot 0 + 2\cdot 1 = 2+0+2=4.a⋅b=1⋅2+(−1)⋅0+2⋅1=2+0+2=4.

Norms:

∥a∥=12+(−1)2+22=6,∥b∥=22+02+12=5.\|\mathbf{a}\|=\sqrt{1^2+(-1)^2+2^2}=\sqrt{6},\quad \|\mathbf{b}\|=\sqrt{2^2+0^2+1^2}=\sqrt{5}.∥a∥=12+(−1)2+22​=6​,∥b∥=22+02+12​=5​.

Cosine similarity:

cosSim(a,b)=465=430≈0.7303.\mathrm{cosSim}(\mathbf{a},\mathbf{b}) = \frac{4}{\sqrt{6}\sqrt{5}} = \frac{4}{\sqrt{30}} \approx 0.7303.cosSim(a,b)=6​5​4​=30​4​≈0.7303.

medium

Show that cosSim(**a**, **b**) = cosSim(3**a**, 0.5**b**) for any nonzero vectors **a**, **b**.

**Hint:** Use how dot products and norms scale under scalar multiplication: (c**a**)·(d**b**) and \|c**a**\|.

Show solution

Let **a'** = 3**a** and **b'** = 0.5**b**.

Dot scales:

a′⋅b′=(3a)⋅(0.5b)=1.5(a⋅b).\mathbf{a'}\cdot\mathbf{b'} = (3\mathbf{a})\cdot(0.5\mathbf{b}) = 1.5(\mathbf{a}\cdot\mathbf{b}).a′⋅b′=(3a)⋅(0.5b)=1.5(a⋅b).

Norms scale:

∥a′∥=∥3a∥=3∥a∥,∥b′∥=∥0.5b∥=0.5∥b∥.\|\mathbf{a'}\| = \|3\mathbf{a}\| = 3\|\mathbf{a}\|,\quad \|\mathbf{b'}\| = \|0.5\mathbf{b}\| = 0.5\|\mathbf{b}\|.∥a′∥=∥3a∥=3∥a∥,∥b′∥=∥0.5b∥=0.5∥b∥.

Cosine similarity:

cosSim(a′,b′)=1.5(a⋅b)(3∥a∥)(0.5∥b∥)=1.5(a⋅b)1.5∥a∥ ∥b∥=cosSim(a,b).\mathrm{cosSim}(\mathbf{a'},\mathbf{b'}) = \frac{1.5(\mathbf{a}\cdot\mathbf{b})}{(3\|\mathbf{a}\|)(0.5\|\mathbf{b}\|)} = \frac{1.5(\mathbf{a}\cdot\mathbf{b})}{1.5\|\mathbf{a}\|\,\|\mathbf{b}\|} = \mathrm{cosSim}(\mathbf{a},\mathbf{b}).cosSim(a′,b′)=(3∥a∥)(0.5∥b∥)1.5(a⋅b)​=1.5∥a∥∥b∥1.5(a⋅b)​=cosSim(a,b).

hard

Assume \|**a**\| = \|**b**\| = 1 (unit vectors). If \|**a** − **b**\| = 0.8, compute cosSim(**a**, **b**).

**Hint:** Use the identity \|**a** − **b**\|² = 2 − 2(**a**·**b**) when both vectors are unit length.

Show solution

Given unit vectors, we have:

∥a−b∥2=2−2(a⋅b).\|\mathbf{a}-\mathbf{b}\|^2 = 2 - 2(\mathbf{a}\cdot\mathbf{b}).∥a−b∥2=2−2(a⋅b).

Compute squared distance:

∥a−b∥2=0.82=0.64.\|\mathbf{a}-\mathbf{b}\|^2 = 0.8^2 = 0.64.∥a−b∥2=0.82=0.64.

So:

0.64=2−2(a⋅b).0.64 = 2 - 2(\mathbf{a}\cdot\mathbf{b}).0.64=2−2(a⋅b).

Solve:

\n$$2(\mathbf{a}\cdot\mathbf{b}) = 2 - 0.64 = 1.36,$$

a⋅b=0.68.\mathbf{a}\cdot\mathbf{b} = 0.68.a⋅b=0.68.

Since unit vectors satisfy cosSim(a,b)=a⋅b\mathrm{cosSim}(\mathbf{a},\mathbf{b})=\mathbf{a}\cdot\mathbf{b}cosSim(a,b)=a⋅b,

cosSim(a,b)=0.68.\mathrm{cosSim}(\mathbf{a},\mathbf{b}) = 0.68.cosSim(a,b)=0.68.

## Connections

- •[Vector Embeddings](/tech-tree/vector-embeddings/)
- •[Attention Mechanisms](/tech-tree/attention-mechanisms/)

Related conceptual neighbors you may want next:

- •[Dot Product](/tech-tree/dot-product/)
- •[Vector Norms](/tech-tree/vector-norms/)
- •[Cauchy–Schwarz Inequality](/tech-tree/cauchy-schwarz/)
- •[Euclidean Distance](/tech-tree/euclidean-distance/)

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
