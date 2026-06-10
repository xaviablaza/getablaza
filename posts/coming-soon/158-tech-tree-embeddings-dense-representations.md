---
title: Embeddings (Dense Representations)
description: Embeddings are learned low-dimensional continuous vectors that represent discrete items (e.g., tokens) so that semantic relationships are encoded in geometry. Attention operates over these vector representations, so familiarity with embeddings and their properties is important.
date: '2026-07-01'
scheduled: '2026-12-05'
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
inspiration_url: https://templeton.host/tech-tree/embeddings-dense-representations/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/embeddings-dense-representations/](https://templeton.host/tech-tree/embeddings-dense-representations/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Embeddings (Dense Representations)

Machine LearningDifficulty: ★★★★☆Depth: 1Unlocks: 2

Embeddings are learned low-dimensional continuous vectors that represent discrete items (e.g., tokens) so that semantic relationships are encoded in geometry. Attention operates over these vector representations, so familiarity with embeddings and their properties is important.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Embedding: discrete item mapped to a learned low-dimensional continuous vector (in R^d)
- -Geometric semantics: vector geometry (angles/distances/inner products) encodes semantic or relational similarity
- -Embeddings as model parameters: a parameterized set of vectors learned jointly with the model

## Key Symbols & Notation

v\_x : the embedding vector for item x

## Essential Relationships

- -Lookup relation: v\_x is the parameter vector selected/updated for item x (equivalent to a linear map from a one-hot index)
- -Similarity relation: semantic relatedness is measured and used via inner products or distances (e.g., v\_x dot v\_y)

## Prerequisites (1)

[Affine Transformations (Linear Layers)5 atoms](/tech-tree/affine-transformations/)

## Unlocks (1)

[Attention Mechanismslvl 5](/tech-tree/attention-mechanisms/)

Advanced Learning Details

### Graph Position

11

Depth Cost

2

Fan-Out (ROI)

1

Bottleneck Score

1

Chain Length

### Cognitive Load

6

Atomic Elements

18

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (10)

- - Embedding (definition): a learned mapping that assigns each discrete item/token a continuous vector in R^d
- - Embedding matrix & lookup: embeddings stored as a matrix whose rows (or columns) are vectors and are retrieved via an index/lookup operation
- - Low-dimensional continuous representation: embeddings use a relatively small dimensionality d (d << vocabulary size) to represent discrete items
- - Semantic geometry: semantic relationships among items are encoded by geometric relationships in embedding space (proximity, directions, linear offsets)
- - Vector similarity metrics for embeddings: using dot product, cosine similarity, or Euclidean distance to measure closeness/relatedness of embeddings
- - Learned vs fixed embeddings: embeddings are parameters that can be trained/updated (not necessarily fixed prespecified encodings)
- - Embedding as input to attention: embeddings serve as the vector representations over which attention operates
- - Embedding-induced attention effects: properties of embeddings (norms, directions) influence attention scores and downstream behavior
- - Vector arithmetic / analogy effects: linear combinations of embeddings can correspond to semantic analogies or transformations
- - Dimensionality trade-off: choosing embedding dimension balances representational capacity against compression/generalization

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Modern neural networks can’t “look up” meaning directly from discrete IDs like token 1729 or user 4,381,002. They first need a continuous, learnable space where distances and angles can express relationships. Embeddings create that space—and attention operates almost entirely inside it.

TL;DR:

An embedding is a learned function that maps a discrete item x to a dense vector **v**ₓ ∈ ℝᵈ. The embedding table is a parameter matrix E ∈ ℝ^{|V|×d}; selecting an embedding is equivalent to multiplying a one-hot vector by E. Geometry in embedding space (dot products, cosine similarity, norms, and offsets) can encode semantic and relational structure, and these vectors are trained jointly with the rest of the model. Understanding embeddings is essential because attention compares tokens via inner products of learned projections of these embeddings.

## What Is an Embedding (Dense Representation)?

### Why we need embeddings (motivation)

Neural networks are built out of operations like matrix multiplication, addition, and nonlinearities. Those operations expect **numbers**. But many ML inputs are **discrete symbols**:

- •Words/tokens ("cat", token id 1729)
- •Users/items in recommender systems
- •Nodes in a graph
- •Categorical features (country, device type)

A discrete ID by itself has no meaningful arithmetic: token 5 is not “closer” to token 6 than to token 5000. If we fed the raw integer ID into a model, we’d be smuggling in a fake ordering.

A classic alternative is a **one-hot** vector **e**ₓ ∈ {0,1}^{|V|}, where |V| is the vocabulary size. This avoids the fake ordering, but it creates a different problem:

- •It’s extremely **high-dimensional** (|V| can be 50k–500k+).
- •It’s extremely **sparse** (exactly one 1).
- •Similarity is unhelpful: for x ≠ y, **e**ₓ · **e**ᵧ = 0.

We want a representation where:

1. 1)The model can learn **similarity** and **relationships**.
2. 2)The representation is **dense** and **low-dimensional**.
3. 3)The representation is **trainable** as part of the model.

That’s exactly what embeddings provide.

### Definition

An **embedding** is a learned mapping

x ↦ **v**ₓ, where **v**ₓ ∈ ℝᵈ

- •x is a discrete item (a token id, category id, etc.)
- •d is the embedding dimension (e.g., 64, 256, 768, 4096)
- •**v**ₓ is a dense vector of real numbers

We’ll use the key symbol from this node:

- •**v**ₓ : the embedding vector for item x

### Embedding table as parameters

In practice, we store embeddings in a matrix (often called an embedding table):

E ∈ ℝ^{|V|×d}

Row x of E (written E[x, :]) is the embedding for item x:

**v**ₓ = E[x, :]

This is why the node description says “embeddings as model parameters”: the rows of E are trainable parameters just like weights in a linear layer.

### A key equivalence: lookup = linear algebra

Even though implementations often do a fast “lookup”, it is mathematically equivalent to multiplying by a matrix.

Let **e**ₓ be the one-hot vector for item x (length |V|). Then:

**v**ₓ = **e**ₓᵀ E

Check the shapes:

- •**e**ₓᵀ is 1×|V|
- •E is |V|×d
- •result is 1×d (a row vector, i.e., an embedding)

So an embedding layer is essentially a linear layer with a very special input (one-hot), where the computation reduces to selecting a row.

### Dense representation: what “dense” really means

“Dense” means most coordinates are nonzero, and information is distributed across coordinates. This matters because:

- •Similarity can be expressed by overlap across many dimensions.
- •Small changes to parameters can smoothly move **v**ₓ, giving the optimizer (gradient descent) a continuous surface to improve.

Embedding vectors are not “features you interpret one-by-one” in general. They’re coordinates in a learned space.

### A mental picture

Think of each item x as a point in d-dimensional space. The model learns where to place those points so that tasks become easy: similar items end up near each other; items that interact strongly get high dot products; offsets can represent relations.

This geometric picture becomes especially important once you learn attention: attention weights are computed from dot products between learned projections of embeddings. So if you can reason about dot products and angles, you can reason about why attention focuses where it does.

## Core Mechanic 1: Embedding Tables, Indexing, and Training Dynamics

### Why this mechanic matters

Embeddings are “just parameters,” but they behave differently from typical weight matrices:

- •Only a few rows are touched per batch (sparse updates).
- •Each row corresponds to a discrete item, which might be rare.
- •Regularization and initialization strongly affect stability.

Understanding how embeddings are represented and updated helps you debug training, reason about capacity, and understand common modeling choices.

### The embedding layer as a parameter matrix

Let the vocabulary be V with |V| items. The embedding table is

E ∈ ℝ^{|V|×d}

Given an input sequence of token ids (x₁, x₂, …, xₙ), the embedding layer outputs a matrix of vectors:

X =

[ **v**\_{x₁}

**v**\_{x₂}

⋮

**v**\_{xₙ} ] ∈ ℝ^{n×d}

This X is what subsequent layers (like attention) operate on.

### One-hot multiplication viewpoint (useful for gradients)

Write the one-hot matrix for the whole sequence as:

H ∈ {0,1}^{n×|V|}

Each row i is **e**\_{xᵢ}ᵀ. Then:

X = H E

This view makes it clear that embeddings are linear in E.

### How gradients flow to embeddings

Suppose your loss is L. You compute ∂L/∂X from later layers, then backpropagate to E.

From X = H E, using matrix calculus:

∂L/∂E = Hᵀ (∂L/∂X)

What does this mean intuitively?

- •Hᵀ “routes” gradient rows back to the corresponding embedding rows.
- •Only the rows that appear in the batch get nonzero gradient.

If token x never appears, its row E[x, :] never updates.

### Sparse updates and rare tokens

Because updates are sparse:

- •Frequent tokens get many updates → well-trained vectors.
- •Rare tokens get few updates → noisy or undertrained vectors.

This is one reason why tokenization (e.g., subword units) helps: it increases coverage so that even rare words share pieces that appear often.

### Initialization and scale

Embeddings are typically initialized with small random values, e.g.

E[x, j] ~ 𝒩(0, σ²)

Why small?

- •If embeddings are too large, early dot products can explode.
- •In attention, dot products are central; large norms can dominate similarity.

Transformers also use scaling (like dividing by √d in attention) partly to control magnitude. But stable embedding scales still matter.

### Regularization: keeping embeddings “well-behaved”

Because embedding rows are free to drift, it’s common to apply:

- •Weight decay (L2): add λ‖E‖²\_F
- •Norm clipping or max norm constraints: ‖**v**ₓ‖ ≤ c

Why? If some vectors become huge, dot products become dominated by norms rather than directions.

### Parameter count and memory

Embedding tables can dominate parameter count.

Parameter count = |V|×d

Example:

- •|V| = 50,000
- •d = 1,024

Then parameters = 50,000×1,024 = 51,200,000 ≈ 51M parameters.

This affects:

- •GPU memory
- •bandwidth (fetching embeddings)
- •training speed

### Input embeddings vs output embeddings (tying)

In language models, you often have:

- •An input embedding table E\_in ∈ ℝ^{|V|×d}
- •An output weight matrix W\_out ∈ ℝ^{|V|×d} used to produce logits: logits = X W\_outᵀ

A common trick is **weight tying**:

W\_out = E\_in

This reduces parameters and often improves generalization because the model uses a shared notion of token similarity for both reading and writing.

### Summary of the mechanics

An embedding layer is a learned matrix where each row is a vector **v**ₓ. Forward pass is indexing; backward pass updates only rows used in the batch. Scale, regularization, and data frequency strongly affect how good those learned vectors become.

## Core Mechanic 2: Geometric Semantics (Similarity, Dot Products, Cosine, and Relations)

### Why geometry is the point

Once tokens become vectors, the model can compare them using geometry. This is not a metaphor: attention scores are built from inner products of projected embeddings.

So you want to be fluent with the main geometric tools:

- •Dot product **a**·**b**
- •Norm ‖**a**‖
- •Cosine similarity cos(θ)
- •Euclidean distance ‖**a** − **b**‖

### Dot product: alignment + magnitude

For **a**, **b** ∈ ℝᵈ:

**a**·**b** = ∑ⱼ aⱼ bⱼ

It can be decomposed as:

**a**·**b** = ‖**a**‖ ‖**b**‖ cos(θ)

where θ is the angle between vectors.

So a large dot product can happen because:

1. 1)The vectors point in similar directions (cos(θ) large), and/or
2. 2)One or both vectors have large norms.

This matters because many models treat dot products as “similarity.” But dot products mix direction and scale.

### Cosine similarity: pure direction

Cosine similarity removes magnitude:

cos\_sim(**a**, **b**) = (**a**·**b**) / (‖**a**‖ ‖**b**‖)

This lives in [-1, 1] (for nonzero vectors) and measures angular closeness.

In practice:

- •Cosine similarity is common for retrieval / nearest neighbors.
- •Attention uses dot products directly (with scaling), so norms can still matter.

### Euclidean distance and its relation to dot product

A useful identity connects distance and dot product:

‖**a** − **b**‖² = (**a** − **b**)·(**a** − **b**)

= **a**·**a** − 2**a**·**b** + **b**·**b**

= ‖**a**‖² − 2**a**·**b** + ‖**b**‖²

If all vectors are normalized to unit norm (‖**a**‖ = ‖**b**‖ = 1), then:

‖**a** − **b**‖² = 2 − 2(**a**·**b**)

So maximizing dot product is equivalent to minimizing distance when norms are controlled.

### “Semantic similarity” is task-defined

It’s tempting to say “embeddings encode meaning,” but the meaning is shaped by:

- •The training objective (predict next token, classify sentiment, etc.)
- •The model architecture (attention, MLPs)
- •The data distribution

Two words are “similar” in embedding space if the model benefits from treating them similarly for the task.

In language modeling, similarity often reflects:

- •Similar contexts (“cat” and “dog”)
- •Syntactic roles (“is”, “was”)
- •Topical associations (“Paris”, “France”)

### Relationship vectors and offsets (the classic intuition)

Sometimes relations are approximately linear in embedding space. A famous pattern (not a guarantee) is:

**v**\_{king} − **v**\_{man} + **v**\_{woman} ≈ **v**\_{queen}

Interpreting this:

- •The offset **v**\_{king} − **v**\_{man} might represent a “male royalty” relation.
- •Adding **v**\_{woman} shifts toward “female royalty.”

Why can this happen?

If many relationships behave consistently, a linear subspace can represent them efficiently. But remember: this depends on training and is approximate.

### Analogies as nearest-neighbor search

To find “queen” from the analogy, you compute:

**u** = **v**\_{king} − **v**\_{man} + **v**\_{woman}

Then search for the token y whose embedding **v**ᵧ is closest to **u** (often by cosine similarity):

y = argmaxᵧ cos\_sim(**u**, **v**ᵧ)

This is one place where cosine similarity is preferred: it reduces sensitivity to norm differences.

### An important nuance: embedding geometry is not unique

If a downstream layer applies a linear map, then rotating embedding space can preserve behavior.

For example, if you replace embeddings with E′ = E R where R is an orthogonal matrix (RᵀR = I), and adjust the next linear layer accordingly, many computations can remain unchanged.

So individual coordinates rarely have stable “human meanings.” What’s stable is the **relative geometry** that the network uses.

### Comparing similarity measures (table)

| Measure | Formula | Sensitive to norms? | Typical use |
| --- | --- | --- | --- |
| Dot product | **a**·**b** | Yes | Attention scores, matrix factorization |
| Cosine similarity | (**a**·**b**) / (‖**a**‖‖**b**‖) | No | Nearest neighbors, retrieval |
| Euclidean distance | ‖**a** − **b**‖ | Yes (via norms) | Clustering, k-NN (if normalized, aligns with cosine) |

### Takeaway

Geometric semantics means the model learns a space where “useful relationships” become simple geometric relationships—often high dot products, small angles, or consistent offsets. This geometric viewpoint is not optional: it’s the language attention uses.

## Application/Connection: Embeddings as the Substrate for Attention (and Beyond)

### Why embeddings are central to attention

Attention mechanisms don’t operate on token ids. They operate on vectors.

In a Transformer, the pipeline starts with embeddings:

1. 1)Token id xᵢ
2. 2)Embedding lookup → **v**\_{xᵢ} ∈ ℝᵈ
3. 3)Add position information (positional embedding or encoding)
4. 4)Apply linear layers to form queries/keys/values

So if embeddings are poorly trained or poorly scaled, attention has bad raw material.

### How embeddings feed into Q/K/V projections

Let X ∈ ℝ^{n×d} be the stacked token embeddings.

A single attention head uses learned matrices:

W\_Q ∈ ℝ^{d×dₖ}, W\_K ∈ ℝ^{d×dₖ}, W\_V ∈ ℝ^{d×dᵥ}

Then:

Q = X W\_Q

K = X W\_K

V = X W\_V

The attention score between token i and token j is based on a dot product:

score(i, j) = ( **q**ᵢ · **k**ⱼ ) / √dₖ

and attention weights are softmaxed scores.

Notice the chain:

xᵢ → **v**\_{xᵢ} → **q**ᵢ

xⱼ → **v**\_{xⱼ} → **k**ⱼ

So the embedding geometry is transformed, but it strongly influences how easily the model can learn useful dot products.

### Why √dₖ scaling exists (embedding magnitude connection)

If components of **q** and **k** have variance σ², the dot product sums dₖ terms, so its variance grows with dₖ. Roughly:

Var(**q**·**k**) ∝ dₖ

Dividing by √dₖ keeps the scale of scores more stable as dₖ changes, preventing softmax from saturating too early.

Even with scaling, extreme embedding norms can still cause issues upstream. That’s why scale/initialization/normalization choices around embeddings matter.

### Positional embeddings: another embedding table

Tokens alone are insufficient: the sequence order matters.

A common approach is to learn a second embedding table for positions:

P ∈ ℝ^{L×d}

For position i, add:

**h**ᵢ = **v**\_{xᵢ} + **p**ᵢ

Now **h**ᵢ is what the model projects into Q/K/V.

This mirrors the main idea: even “position” is treated as a discrete item that gets a learned dense vector.

### Embeddings in other domains

Embeddings are a general pattern:

- •Recommenders: users and items embedded; dot product predicts affinity.
- •Graphs: node embeddings; proximity predicts edges.
- •Multimodal: text embeddings and image embeddings aligned so that matching pairs have high similarity.

The core idea remains: map discrete or complex objects into a shared vector space where geometry supports the task.

### Learned similarity vs human similarity

In attention, the model learns to create Q/K spaces where dot products reflect “should attend.” This is a task-specific similarity.

For example:

- •A pronoun embedding may attend to a noun not because the words are similar, but because they are coreferent.
- •A comma may attend to syntactic boundaries.

So embeddings are not just about synonyms—they are about making the downstream operations (especially dot products) predictive.

### Practical diagnostics and intuition

When embeddings go wrong, you often see:

- •Slow training: the model struggles to form useful neighborhoods.
- •Instability: exploding norms, attention saturation.
- •Poor generalization for rare tokens.

Interventions often involve:

- •Changing d (capacity)
- •Regularizing norms
- •Better tokenization
- •Weight tying
- •Pretraining (starting from a good embedding space)

### Connection forward

Once embeddings are clear, attention becomes less mysterious: it’s “compare vectors, mix values.” You’ll be ready to reason about attention heads as geometric comparators operating on embedded tokens.

Next node:

- •[Attention Mechanisms](/tech-tree/attention-mechanisms/)

## Worked Examples (3)

### Example 1: Embedding lookup equals one-hot times embedding matrix

Let |V| = 5 items, embedding dimension d = 3. The embedding table is

E =

[ 0.2 -0.1 0.0

0.0 0.3 0.1

-0.2 0.4 0.5

0.7 0.0 -0.3

0.1 0.2 0.2 ]

Assume item x = 4 (1-indexed). Show that selecting the embedding is the same as multiplying a one-hot vector by E.

1. Write the one-hot vector for x = 4 (length 5):

   **e**₄ = [0, 0, 0, 1, 0]ᵀ.
2. Compute **v**₄ by lookup (row selection):

   **v**₄ = E[4, :] = [0.7, 0.0, -0.3].
3. Compute **e**₄ᵀ E explicitly:

   **e**₄ᵀ E = [0, 0, 0, 1, 0]

   ·

   [ 0.2 -0.1 0.0

   0.0 0.3 0.1

   -0.2 0.4 0.5

   0.7 0.0 -0.3

   0.1 0.2 0.2 ]
4. Use the fact that left-multiplying by a one-hot row picks the corresponding row:

   **e**₄ᵀ E = 1·[0.7, 0.0, -0.3] + 0·(other rows)

   = [0.7, 0.0, -0.3].
5. Conclude:

   **v**₄ = **e**₄ᵀ E, so embedding lookup is a special case of a linear layer with one-hot input.

**Insight:** Thinking of embeddings as **E** and inputs as one-hot vectors makes backpropagation intuitive: gradients route to rows of E corresponding to observed tokens.

### Example 2: Dot product vs cosine similarity (same direction, different norms)

Let **a** = [3, 0] and **b** = [1, 0]. Compute **a**·**b**, cos\_sim(**a**, **b**), and explain what each says about similarity.

1. Compute the dot product:

   **a**·**b** = 3·1 + 0·0 = 3.
2. Compute norms:

   ‖**a**‖ = √(3² + 0²) = 3

   ‖**b**‖ = √(1² + 0²) = 1
3. Compute cosine similarity:

   cos\_sim(**a**, **b**) = (**a**·**b**) / (‖**a**‖‖**b**‖)

   = 3 / (3·1)

   = 1.
4. Interpretation:

   - •Dot product = 3 is “large” partly because ‖**a**‖ is large.
   - •Cosine similarity = 1 means they point in exactly the same direction (θ = 0).

**Insight:** Dot product conflates direction and magnitude; cosine isolates direction. Attention uses dot products (with scaling), so vector norms can influence attention even when directions match.

### Example 3: Relating Euclidean distance to dot product (why normalization matters)

Let **u** and **v** be unit vectors (‖**u**‖ = ‖**v**‖ = 1) with **u**·**v** = 0.8. Compute ‖**u** − **v**‖² and ‖**u** − **v**‖. سپس explain the relationship.

1. Start from the identity:

   ‖**u** − **v**‖² = ‖**u**‖² − 2(**u**·**v**) + ‖**v**‖².
2. Plug in ‖**u**‖² = 1, ‖**v**‖² = 1, **u**·**v** = 0.8:

   ‖**u** − **v**‖² = 1 − 2(0.8) + 1

   = 2 − 1.6

   = 0.4.
3. Take the square root:

   ‖**u** − **v**‖ = √0.4 ≈ 0.632.
4. Interpretation:

   When vectors are normalized, larger dot product ⇒ smaller distance in a precise way:

   ‖**u** − **v**‖² = 2 − 2(**u**·**v**).

**Insight:** If you normalize embeddings, dot product similarity and Euclidean distance become directly linked, which simplifies nearest-neighbor reasoning and stabilizes similarity comparisons.

## Key Takeaways

- ✓

  An embedding maps a discrete item x to a learned dense vector **v**ₓ ∈ ℝᵈ.
- ✓

  The embedding layer is a parameter matrix E ∈ ℝ^{|V|×d}; **v**ₓ is simply row x of E.
- ✓

  Embedding lookup is mathematically **v**ₓ = **e**ₓᵀ E, i.e., a linear map applied to a one-hot input.
- ✓

  Only embedding rows that appear in a batch receive gradient updates; rare items learn slowly and can be poorly represented.
- ✓

  Geometry is the core: dot products, norms, angles, and distances define similarity and relational structure used by downstream layers.
- ✓

  Dot product mixes direction and magnitude: **a**·**b** = ‖**a**‖‖**b**‖cos(θ). Cosine similarity removes magnitude effects.
- ✓

  Embedding spaces are not uniquely identifiable (they can be rotated/reparameterized); what matters is relative geometry as used by the network.
- ✓

  Attention relies on these representations: tokens become embeddings, are projected to Q/K/V, and compared via scaled dot products.

## Common Mistakes

- ✗

  Treating token IDs as numeric features (e.g., feeding the integer id directly), which introduces fake ordinality.
- ✗

  Assuming dot product equals “semantic similarity” without considering vector norms; large norms can dominate scores.
- ✗

  Over-interpreting individual embedding coordinates as human-readable features; embeddings are often only meaningful up to rotations and linear transforms.
- ✗

  Ignoring frequency effects: rare items may have noisy embeddings unless you use better tokenization, regularization, or share substructures.

## Practice

easy

You have |V| = 10,000 tokens and choose embedding dimension d = 512.

1) How many embedding parameters are there?

2) If you store them in float32, roughly how many MB is the table (ignore overhead)?

**Hint:** Parameters = |V|×d. float32 is 4 bytes per parameter. Convert bytes to MB by dividing by 1024² (or approximate with 10⁶ for a rough estimate).

Show solution

1) Parameters = 10,000×512 = 5,120,000.

2) Bytes ≈ 5,120,000×4 = 20,480,000 bytes.

In MiB: 20,480,000 / 1024² ≈ 19.5 MiB (about 20 MB).

medium

Let **a**, **b** ∈ ℝᵈ be nonzero. Show algebraically that scaling one vector changes dot product but not cosine similarity:

- •Compare (**a**·(c**b**)) to (**a**·**b**)
- •Compare cos\_sim(**a**, c**b**) to cos\_sim(**a**, **b**) for c > 0

**Hint:** Use linearity of dot product and the fact that ‖c**b**‖ = c‖**b**‖ for c > 0.

Show solution

Dot product:

**a**·(c**b**) = c(**a**·**b**) (it scales linearly with c).

Cosine similarity (c > 0):

cos\_sim(**a**, c**b**) = (**a**·(c**b**)) / (‖**a**‖‖c**b**‖)

= c(**a**·**b**) / (‖**a**‖ (c‖**b**‖))

= (**a**·**b**) / (‖**a**‖‖**b**‖)

= cos\_sim(**a**, **b**).

So cosine similarity is invariant to positive scaling.

hard

Suppose an embedding table E ∈ ℝ^{|V|×d} is used, and a batch contains token ids [2, 2, 5]. Let the upstream gradient for the resulting embeddings X ∈ ℝ^{3×d} be G = ∂L/∂X, where rows are **g**₁, **g**₂, **g**₃.

Describe (in words and formulas) which rows of ∂L/∂E are nonzero and what values they take.

**Hint:** Use X = H E where H is the one-hot matrix. Then ∂L/∂E = Hᵀ G. Repeated ids mean gradients add into the same row.

Show solution

Only rows corresponding to ids 2 and 5 can be nonzero.

Because token id 2 appears twice (positions 1 and 2), its embedding row receives the sum of both gradients:

(∂L/∂E)[2, :] = **g**₁ + **g**₂.

Token id 5 appears once (position 3):

(∂L/∂E)[5, :] = **g**₃.

All other rows x ∉ {2, 5} have:

(∂L/∂E)[x, :] = **0**.

This reflects sparse updates and accumulation for repeated tokens.

## Connections

Prerequisite concept you’ll actively use:

- •[Affine Transformations (Linear Layers)](/tech-tree/affine-transformations-linear-layers/)

This node unlocks:

- •[Attention Mechanisms](/tech-tree/attention-mechanisms/)

Related follow-on ideas (often adjacent in a tech tree):

- •[Softmax](/tech-tree/softmax/)
- •[Vector Norms and Cosine Similarity](/tech-tree/vector-norms-cosine/)
- •[Positional Embeddings](/tech-tree/positional-embeddings/)
- •[Weight Tying](/tech-tree/weight-tying/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
