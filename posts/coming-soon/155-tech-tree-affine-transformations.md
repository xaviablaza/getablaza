---
title: Affine Transformations (Linear Layers)
description: An affine transformation applies a linear map (matrix multiply) followed by a bias shift; in neural models this corresponds to learned linear layers that project inputs into query/key/value spaces. Recognizing affine transforms helps understand how attention inputs are linearly combined and projected.
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
permalink: /tech-tree/affine-transformations/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Affine Transformations (Linear Layers)

Linear AlgebraDifficulty: ★★★☆☆Depth: 0Unlocks: 4

An affine transformation applies a linear map (matrix multiply) followed by a bias shift; in neural models this corresponds to learned linear layers that project inputs into query/key/value spaces. Recognizing affine transforms helps understand how attention inputs are linearly combined and projected.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Linear map: apply a matrix to an input vector to compute weighted sums and mix components (matrix multiplication)
- -Bias (translation): add a constant vector to shift the output independent of the input

## Key Symbols & Notation

W (weight matrix)b (bias vector)

## Essential Relationships

- -Affine formula: output = W times input + b (y = W x + b) - an affine transform is the linear map followed by the bias

## Unlocks (3)

[Attention Mechanismslvl 5](/tech-tree/attention-mechanisms/)[Embeddings (Dense Representations)lvl 4](/tech-tree/embeddings-dense-representations/)[Sequence Masking (causal and padding masks)lvl 4](/tech-tree/sequence-masking/)

Advanced Learning Details

### Graph Position

5

Depth Cost

4

Fan-Out (ROI)

1

Bottleneck Score

0

Chain Length

### Cognitive Load

5

Atomic Elements

32

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (13)

- - Affine transformation as a mathematical object: a linear map followed by a bias (y = A x + b)
- - Linear map / linear transformation implemented by a matrix multiply (A x)
- - Bias shift (translation) implemented by adding a bias vector b after the linear map
- - Learned linear layer: the affine transform inside a neural network whose parameters are trained
- - Query, Key, Value spaces: distinct vector spaces produced by separate learned projections for attention
- - Projection (in the neural-net sense): mapping input vectors into another (possibly lower/higher) feature space via a matrix
- - Linear combination: each output component is a weighted sum of input components
- - Interpreting a matrix as a collection of weight vectors (rows or columns) that produce output coordinates
- - Dimensionality/shape constraints of matrices and vectors (input\_dim, output\_dim) that govern valid multiplication
- - Difference between affine and purely linear maps: presence of bias means the origin is not preserved
- - Composition of affine transforms: chaining layers yields another affine transform (structure and combined bias)
- - Role of parameters (W, b) as learned quantities that change representations during training
- - How affine projections are used in attention: inputs are linearly projected into q/k/v, then combined via attention

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Every time a Transformer turns token vectors into queries, keys, and values, it’s doing the same fundamental operation: take an input vector, mix its components with a matrix, then shift the result with a bias. That simple “mix then shift” move—an affine transformation—is the workhorse behind linear layers.

TL;DR:

An affine transformation maps **x** ↦ W**x** + **b**. The matrix W performs a linear map (rotation/scale/shear/projection and component mixing), and the bias **b** translates (shifts) the output. In neural networks, this is a learned linear layer used to project embeddings into new spaces (like Q/K/V in attention).

## What Is an Affine Transformation (Linear Layer)?

### Why this concept exists

In many systems you want a controllable way to transform a vector of features into a new vector of features. In machine learning, you repeatedly need to:

1. 1)**Combine** input features into new features (weighted sums)
2. 2)**Recenter** or **shift** the output (so “zero input” doesn’t force “zero output”)

A **linear map** does (1). A **bias/translation** does (2). Together they form an **affine transformation**.

### Definition

An **affine transformation** from ℝⁿ to ℝᵐ is a function of the form:

- •**f**(**x**) = W**x** + **b**

where:

- •W ∈ ℝᵐˣⁿ is the **weight matrix**
- •**b** ∈ ℝᵐ is the **bias vector**
- •**x** ∈ ℝⁿ is the input vector
- •**y** = **f**(**x**) ∈ ℝᵐ is the output vector

In neural-network language, this is a **linear layer** (often called “fully connected”), even though mathematically it’s affine unless **b** = **0**.

### Intuition: “mix then shift”

Think of **x** as a column of numbers (features). Multiplying by W creates **weighted sums** of those features—each output component is a mixture of all input components.

Then adding **b** shifts the result by a constant offset independent of **x**.

### Linear vs affine (the key distinction)

A linear map L(**x**) = W**x** has a special property:

- •L(**0**) = **0**

But an affine map A(**x**) = W**x** + **b** generally does not:

- •A(**0**) = W**0** + **b** = **b**

So the bias is exactly what lets the model output something nonzero even when the input is zero.

### Geometry: what affine transforms preserve

Affine transformations preserve **straight lines** and **parallelism**. They do *not* necessarily preserve angles or lengths.

- •Linear part (W) can rotate/scale/shear/project
- •Bias part (**b**) translates everything

A useful mental model:

- •W decides “what directions count” and “how much to stretch them”
- •**b** decides “where is the new origin”

### Shapes (dimensions) matter

In ML you’ll constantly track dimensions. Here’s the standard setup:

- •Input **x** has n features: **x** ∈ ℝⁿ
- •Output **y** has m features: **y** ∈ ℝᵐ
- •Therefore W must be m×n so that W**x** is defined
- •Bias **b** must be length m so it can be added to W**x**

A compact dimension check:

- •W ∈ ℝᵐˣⁿ, **x** ∈ ℝⁿ ⇒ W**x** ∈ ℝᵐ
- •**b** ∈ ℝᵐ ⇒ W**x** + **b** ∈ ℝᵐ

This one rule prevents many mistakes later when you build attention projections.

## Core Mechanic 1 — The Linear Map: Matrix Multiplication as Weighted Sums

### Why start with the matrix part?

If you strip away the bias, the matrix multiplication W**x** is the *mixing engine* of a linear layer. It’s how models learn to combine features: emphasize some, suppress others, and create new features from old ones.

### Row view: each output is a dot product

Let W have rows **w**₁ᵀ, **w**₂ᵀ, …, **w**ₘᵀ (each **w**ᵢ ∈ ℝⁿ). Then:

- •(W**x**)ᵢ = **w**ᵢᵀ **x**

So each output component is a **dot product** between the input and a learned weight vector.

Write this explicitly:

- •**y** = W**x**
- •y₁ = **w**₁ᵀ**x**
- •y₂ = **w**₂ᵀ**x**
- •…
- •yₘ = **w**ₘᵀ**x**

This is why people say a linear layer computes “weighted sums”: each yᵢ is a sum of input components xⱼ multiplied by weights.

### Component form: the summation you’ll see in derivations

If W has entries Wᵢⱼ, then:

- •yᵢ = ∑ⱼ Wᵢⱼ xⱼ

This shows two important things:

1. 1)Each output coordinate can depend on *all* input coordinates.
2. 2)The weights Wᵢⱼ are exactly “how much does xⱼ contribute to yᵢ?”.

### Column view: the output is a linear combination of columns

Let W’s columns be **c**₁, …, **c**ₙ (each **c**ⱼ ∈ ℝᵐ). Then:

- •W**x** = x₁**c**₁ + x₂**c**₂ + … + xₙ**c**ₙ

So the input scalars xⱼ decide how much of each column vector **c**ⱼ is added.

This is a powerful geometric view:

- •the columns of W span the set of outputs you can produce
- •if W is rank-deficient, you’re projecting into a lower-dimensional subspace

### Mixing features: why matrices are more than per-feature scaling

A diagonal matrix scales each coordinate independently:

- •W = diag(s₁,…,sₙ) ⇒ yᵢ = sᵢ xᵢ

But a full matrix creates new features by *mixing*:

- •y₁ might combine x₁ and x₃
- •y₂ might compare x₂ against x₁
- •etc.

In representation learning, this mixing is essential: the model can rotate into a coordinate system where some later operation (like attention scoring) becomes easier.

### A small but crucial property: linearity

For L(**x**) = W**x**:

- •L(α**u** + β**v**) = αL(**u**) + βL(**v**)

You can verify by algebra:

L(α**u** + β**v**)

= W(α**u** + β**v**)

= αW**u** + βW**v**

= αL(**u**) + βL(**v**)

This matters conceptually: the linear part preserves the “add and scale” structure of vectors.

### When does W change dimensionality?

Affine/linear layers are often used to change feature dimension:

| Goal | n → m | Interpretation |
| --- | --- | --- |
| Compression | large n → small m | projection / bottleneck |
| Expansion | small n → large m | lift into richer feature space |
| Same size | n → n | rotation/scale/shear/mixing |

In Transformers, projections often keep the model dimension d the same (d → d) but also create multiple heads (conceptually splitting into h subspaces). Even when the final dimension is the same, W is still doing a learned change of basis.

## Core Mechanic 2 — The Bias: Translation and Changing the “Default Output”

### Why do we add a bias at all?

If you only have **y** = W**x**, then the output is forced to be **0** when **x** = **0**. That’s not always desirable.

In ML terms: without a bias, the model can only represent functions that pass through the origin. A bias lets the model set a **baseline** output.

### Definition and immediate consequence

An affine layer is:

- •**y** = W**x** + **b**

Evaluate at **x** = **0**:

- •**y** = W**0** + **b**
- •**y** = **b**

So **b** is the output the layer produces when given zero input.

### Geometry: translation

The map **x** ↦ W**x** transforms the space around the origin. Adding **b** then shifts every output by the same vector.

If two inputs differ by **Δx**:

- •**y**₁ = W**x**₁ + **b**
- •**y**₂ = W**x**₂ + **b**

Subtract:

- •**y**₂ − **y**₁ = W(**x**₂ − **x**₁)

Notice **b** cancels. This reveals an important geometric fact:

- •**b** does not affect differences; it affects absolute placement.

So W controls how differences are transformed; **b** controls where the transformed cloud sits.

### Bias as an extra feature (homogeneous coordinates idea)

A useful trick is to rewrite the affine map as a pure matrix multiply by augmenting the input with a 1.

Create an extended vector and matrix:

- •**x̄** = [ **x** ; 1 ] ∈ ℝⁿ⁺¹
- •W̄ = [ W **b** ] ∈ ℝᵐˣ(ⁿ⁺¹)

Then:

W̄**x̄**

= [ W **b** ] [ **x** ; 1 ]

= W**x** + **b**·1

= W**x** + **b**

Why this is conceptually helpful:

- •bias is just “weights on a constant feature”
- •it reminds you the bias is learned like other parameters

### Bias and decision boundaries (quick ML connection)

Even before deep learning, linear models use biases.

A linear classifier might compute:

- •s(**x**) = **w**ᵀ**x** + b

The set where s(**x**) = 0 is a hyperplane:

- •**w**ᵀ**x** + b = 0

If b = 0, the hyperplane must pass through the origin. With b ≠ 0, it can shift, greatly increasing what you can represent.

### What about bias in Transformers?

Many Transformer implementations include bias terms in linear projections, though some variants remove them for efficiency or symmetry (and compensate elsewhere). Conceptually, knowing that **b** exists helps you interpret a projection as:

- •“learn a subspace and also choose an offset in that subspace.”

Even if a specific architecture sets **b** = **0**, the affine framework is still the general concept.

## Application/Connection — Affine Layers in Attention (Q, K, V Projections) and Embeddings

### Why affine transformations show up in attention

Attention needs vectors in roles that are *not identical*:

- •Queries ask: “what am I looking for?”
- •Keys advertise: “what do I contain?”
- •Values carry: “what information should be passed along?”

Even if all tokens start as embeddings in the same space ℝᵈ (model dimension d), the model benefits from learning **different projections** for these different roles.

### The standard projections

Given a token representation **x** ∈ ℝᵈ, attention uses learned affine maps:

- •**q** = W\_Q **x** + **b**\_Q
- •**k** = W\_K **x** + **b**\_K
- •**v** = W\_V **x** + **b**\_V

where W\_Q, W\_K, W\_V ∈ ℝᵈˣᵈ (often) and biases are in ℝᵈ.

With sequences, you apply this to every position. If X ∈ ℝˡˣᵈ is a matrix whose rows are token vectors, then:

- •Q = X W\_Qᵀ + **1** **b**\_Qᵀ (conceptually “add bias to every row”)
- •K = X W\_Kᵀ + **1** **b**\_Kᵀ
- •V = X W\_Vᵀ + **1** **b**\_Vᵀ

Here **1** ∈ ℝˡ is a vector of ones. The important idea is: the same affine transform is applied independently to each token vector.

### Multi-head attention as multiple affine projections

In multi-head attention with h heads, each head often uses a smaller per-head dimension d\_head where d = h·d\_head.

One way to view this:

- •W\_Q maps ℝᵈ → ℝᵈ, then you reshape into h blocks of size d\_head

Another view (equivalent conceptually):

- •each head has its own W\_Q^(head) ∈ ℝᵈ\_headˣᵈ (and similarly for K, V)

Either way, the key point is that attention relies on **learned affine maps** to create multiple learned “views” of the same input.

### Why affine (not just linear) matters for interpretation

Suppose you compare two tokens **x**₁ and **x**₂. Their query difference is:

- •**q**₂ − **q**₁ = (W\_Q**x**₂ + **b**\_Q) − (W\_Q**x**₁ + **b**\_Q)
- •**q**₂ − **q**₁ = W\_Q(**x**₂ − **x**₁)

So the bias does not change *relative* geometry, but it does change the *absolute* location. In dot-product attention, absolute location can matter because dot products are not translation-invariant:

- •(**q** + **c**)ᵀ(**k** + **d**) expands into cross-terms involving **c** and **d**

This is one reason biases can subtly affect attention score distributions.

### Connecting to embeddings

Embeddings give you dense vectors **e**(token) ∈ ℝᵈ. On their own they are just coordinates. Affine layers are how the model:

- •re-expresses embeddings in a task-relevant coordinate system
- •compresses or expands dimensions
- •prepares vectors for specific operations (scoring, gating, residual mixing)

In practice, a Transformer block is largely a sequence of affine maps plus nonlinearities and normalization. Recognizing “W**x** + **b**” everywhere helps you read architectures without getting lost.

### Connection to masking (preview)

Masking affects which attention scores are allowed, but the scores themselves come from dot products of affine-projected vectors:

- •score(i,j) ∝ **q**ᵢᵀ **k**ⱼ

So masking is applied *after* affine projections have created Q and K. Understanding affine projections helps you see that masking doesn’t change how Q/K/V are computed; it changes which pairings (i,j) are considered.

### Summary table: where affine transforms appear in a Transformer

| Component | Typical form | Purpose |
| --- | --- | --- |
| Q projection | **q** = W\_Q**x** + **b**\_Q | prepare “search vectors” |
| K projection | **k** = W\_K**x** + **b**\_K | prepare “address vectors” |
| V projection | **v** = W\_V**x** + **b**\_V | prepare “content vectors” |
| Output projection | **o** = W\_O**z** + **b**\_O | mix heads back together |
| Feed-forward layer 1 | **h** = W₁**x** + **b**₁ | expand dimension |
| Feed-forward layer 2 | **y** = W₂φ(**h**) + **b**₂ | compress back |

Once you can fluently interpret each row of W as “a learned feature detector” and **b** as “a learned baseline,” the architecture becomes much more transparent.

## Worked Examples (3)

### Example 1 — Compute an affine transform and interpret the result

Let **x** ∈ ℝ² be **x** = [2; −1]. Let W ∈ ℝ²ˣ² and **b** ∈ ℝ² be:

W = [[1, 3],

[−2, 0]]

**b** = [4; 1]

Compute **y** = W**x** + **b**, and interpret each output coordinate as a weighted sum plus bias.

1. Start with **y** = W**x** + **b**.
2. Compute W**x** using row-by-row dot products.

   First row of W is **w**₁ᵀ = [1, 3].

   So (W**x**)₁ = [1, 3] · [2; −1]

   = 1·2 + 3·(−1)

   = 2 − 3

   = −1.
3. Second row of W is **w**₂ᵀ = [−2, 0].

   So (W**x**)₂ = [−2, 0] · [2; −1]

   = (−2)·2 + 0·(−1)

   = −4 + 0

   = −4.
4. So W**x** = [−1; −4].
5. Add the bias **b**:

   **y** = W**x** + **b**

   = [−1; −4] + [4; 1]

   = [3; −3].

**Insight:** Each output is a learned weighted sum of inputs plus a learned offset. Here y₁ = 1·x₁ + 3·x₂ + 4 and y₂ = (−2)·x₁ + 0·x₂ + 1. The matrix mixes features; the bias shifts the baseline.

### Example 2 — Show that bias cancels in differences, but affects absolute dot products

Consider an affine projection used for queries: **q** = W**x** + **b**. Take two inputs **x**₁ and **x**₂. (1) Derive **q**₂ − **q**₁. (2) Show how a shared bias can still affect a dot-product score **q**ᵀ**k** when both sides have biases.

1. Write the two projected queries:

   **q**₁ = W**x**₁ + **b**

   **q**₂ = W**x**₂ + **b**
2. Subtract:

   **q**₂ − **q**₁

   = (W**x**₂ + **b**) − (W**x**₁ + **b**)

   = W**x**₂ + **b** − W**x**₁ − **b**

   = W(**x**₂ − **x**₁).
3. So the bias **b** does not affect differences between projected vectors; it only shifts them together.
4. Now consider keys also have a bias: **k** = U**x** + **c**.

   A dot-product score between a query and a key is:

   score = **q**ᵀ**k**

   = (W**x** + **b**)ᵀ (U**x'** + **c**).
5. Expand the dot product carefully:

   (W**x** + **b**)ᵀ (U**x'** + **c**)

   = (W**x**)ᵀ(U**x'**) + (W**x**)ᵀ**c** + **b**ᵀ(U**x'**) + **b**ᵀ**c**.
6. Even though biases cancel in differences, they introduce extra terms in absolute dot products: (W**x**)ᵀ**c**, **b**ᵀ(U**x'**), and **b**ᵀ**c**.

**Insight:** Bias doesn’t change relative geometry (differences), but attention scoring depends on absolute dot products, so biases can shift score distributions via additional cross-terms. This is one reason architectural choices about bias can matter in practice.

### Example 3 — Rewrite an affine map as a single matrix multiplication (homogeneous trick)

Let W ∈ ℝ³ˣ² and **b** ∈ ℝ³ define **y** = W**x** + **b**. Construct an augmented matrix W̄ and augmented vector **x̄** so that **y** = W̄**x̄** with no explicit + **b**.

1. Start with **y** = W**x** + **b**, where **x** ∈ ℝ² and **y** ∈ ℝ³.
2. Augment the input by appending 1:

   **x̄** = [ **x** ; 1 ] ∈ ℝ³.
3. Create the augmented matrix by appending **b** as an extra column:

   W̄ = [ W **b** ] ∈ ℝ³ˣ³.
4. Multiply:

   W̄**x̄**

   = [ W **b** ] [ **x** ; 1 ]

   = W**x** + **b**·1

   = W**x** + **b**

   = **y**.

**Insight:** Bias can be treated as weights on a constant feature. This is handy for reasoning and for deriving gradients: affine maps are linear in their parameters.

## Key Takeaways

- ✓

  An affine transformation is **f**(**x**) = W**x** + **b**; it’s the mathematical form of a neural-network “linear layer.”
- ✓

  W ∈ ℝᵐˣⁿ mixes and transforms features; each output coordinate is a dot product with a row of W: yᵢ = **w**ᵢᵀ**x**.
- ✓

  The bias **b** ∈ ℝᵐ translates outputs and sets **f**(**0**) = **b**; without it, the mapping must pass through the origin.
- ✓

  Differences cancel the bias: (**f**(**x**₂) − **f**(**x**₁)) = W(**x**₂ − **x**₁). So W controls relative geometry; **b** controls absolute placement.
- ✓

  Affine maps preserve straight lines and parallelism (they’re linear maps plus translation).
- ✓

  You can encode the bias by augmenting the input with a 1: W**x** + **b** = W̄[**x**; 1].
- ✓

  In Transformers, Q/K/V projections are affine maps applied to token embeddings: **q** = W\_Q**x** + **b**\_Q, etc.

## Common Mistakes

- ✗

  Calling W**x** + **b** “linear” in the strict math sense: it’s affine unless **b** = **0**.
- ✗

  Getting dimensions wrong (e.g., using W ∈ ℝⁿˣᵐ when **x** ∈ ℝⁿ and expecting an ℝᵐ output). Always check W ∈ ℝᵐˣⁿ.
- ✗

  Forgetting that each output is a dot product with a row of W, leading to confusion about how features are mixed.
- ✗

  Assuming the bias never matters in attention because it cancels in differences; dot-product scores depend on absolute vectors and can be affected by biases via cross-terms.

## Practice

easy

Let **x** = [1; 2; −1] ∈ ℝ³, W = [[2, 0, 1], [−1, 3, 2]] ∈ ℝ²ˣ³, and **b** = [0; 5] ∈ ℝ². Compute **y** = W**x** + **b**.

**Hint:** Compute W**x** by row dot products, then add **b**.

Show solution

W**x**:

First row: [2,0,1]·[1;2;−1] = 2·1 + 0·2 + 1·(−1) = 2 − 1 = 1

Second row: [−1,3,2]·[1;2;−1] = (−1)·1 + 3·2 + 2·(−1) = −1 + 6 − 2 = 3

So W**x** = [1; 3].

Add **b**: **y** = [1;3] + [0;5] = [1;8].

medium

Suppose **f**(**x**) = W**x** + **b** with W ∈ ℝᵐˣⁿ. Prove that for any **u**, **v** ∈ ℝⁿ and scalar α, the following holds: **f**(α**u** + (1−α)**v**) = α**f**(**u**) + (1−α)**f**(**v**).

**Hint:** Expand both sides using distributivity of matrix multiplication; watch how the bias terms combine.

Show solution

Left side:

**f**(α**u** + (1−α)**v**) = W(α**u** + (1−α)**v**) + **b**

= αW**u** + (1−α)W**v** + **b**.

Right side:

α**f**(**u**) + (1−α)**f**(**v**)

= α(W**u** + **b**) + (1−α)(W**v** + **b**)

= αW**u** + α**b** + (1−α)W**v** + (1−α)**b**

= αW**u** + (1−α)W**v** + (α + 1−α)**b**

= αW**u** + (1−α)W**v** + **b**.

Both sides match, so the identity holds. (This is a defining “affine” property: it preserves convex combinations.)

medium

You have a Transformer with model dimension d = 512 and number of heads h = 8. If per-head dimension is d\_head = 64, what are the typical shapes of W\_Q, W\_K, W\_V for the combined projection (single matrix per type), and what is the shape of the per-token bias **b**\_Q?

**Hint:** Combined projections usually map ℝᵈ → ℝᵈ, then reshape into (h, d\_head).

Show solution

Since d = h·d\_head = 8·64 = 512, a common design is:

W\_Q ∈ ℝᵈˣᵈ = ℝ⁵¹²ˣ⁵¹² (and similarly W\_K, W\_V).

The bias **b**\_Q is added to each token’s projected query vector, so **b**\_Q ∈ ℝᵈ = ℝ⁵¹².

After computing **q** = W\_Q**x** + **b**\_Q, the result in ℝ⁵¹² is reshaped/split into 8 heads of size 64.

## Connections

Next nodes you can unlock and why they rely on affine maps:

- •[Attention Mechanisms](/tech-tree/attention-mechanisms/): Q/K/V are computed by affine projections **q** = W\_Q**x** + **b**\_Q, etc., and attention scores depend on dot products in these projected spaces.
- •[Embeddings (Dense Representations)](/tech-tree/embeddings-dense-representations/): embeddings become useful when affine layers can rotate/mix/scale them into task-specific features and subspaces.
- •[Sequence Masking (causal and padding masks)](/tech-tree/sequence-masking/): masks alter which attention scores are valid, but those scores come from affine-projected Q and K; understanding projections clarifies what masking does and does not change.

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
