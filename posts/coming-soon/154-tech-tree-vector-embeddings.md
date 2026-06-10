---
title: Vector Embeddings
description: Continuous vector representations that encode discrete items (words, tokens, or features) into a dense numeric space where geometric relationships reflect semantic or functional similarity. Embeddings are the typical inputs to attention layers and determine how items interact via similarity and projection.
date: '2026-07-01'
scheduled: '2026-12-01'
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
inspiration_url: https://templeton.host/tech-tree/vector-embeddings/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/vector-embeddings/](https://templeton.host/tech-tree/vector-embeddings/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Vector Embeddings

Machine LearningDifficulty: ★★★★☆Depth: 1Unlocks: 2

Continuous vector representations that encode discrete items (words, tokens, or features) into a dense numeric space where geometric relationships reflect semantic or functional similarity. Embeddings are the typical inputs to attention layers and determine how items interact via similarity and projection.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Embedding = a dense continuous vector that represents a discrete item (word, token, or feature)
- -Geometric relations (angle or distance) between embedding vectors encode semantic or functional similarity
- -Embeddings are learned mappings or parameters (e.g., lookup table or neural function) that assign a vector to each item

## Key Symbols & Notation

e\_x - embedding vector for item x (real-valued vector)

## Essential Relationships

- -Similarity(item\_i,item\_j) = sim(e\_i,e\_j) (e.g., cosine or dot): embedding geometry directly determines similarity and interaction

## Prerequisites (1)

[Cosine Similarity6 atoms](/tech-tree/cosine-similarity/)

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

5

Atomic Elements

34

Total Elements

L2

Percentile Level

L3

Atomic Level

### All Concepts (13)

- - Embedding (vector representation): a learned continuous vector that represents a discrete item (token, word, feature).
- - Embedding space: a dense numeric vector space R^d in which embeddings live.
- - Embedding dimensionality (d): the number of components in each embedding vector (a hyperparameter).
- - Embedding matrix / lookup table: a parameter matrix that maps discrete indices (one-hot) to their embedding vectors.
- - Linear projection of embeddings: applying learned linear transforms to embeddings (e.g., to produce queries, keys, values).
- - Query/Key/Value (Q/K/V) mechanism: projected versions of embeddings used inside attention to compute interactions.
- - Scaled dot-product attention basics: computing attention scores from dot products of projected embeddings, scaling, softmaxing, and weighting values.
- - Learned vs. fixed embeddings: embeddings can be trained end-to-end for a task or loaded from pretrained models and optionally fine-tuned.
- - Embedding initialization and training dynamics: embeddings are parameters updated by gradient-based optimization and influenced by task loss and data frequency.
- - Dense vs. sparse representations: embeddings are dense numeric vectors contrasted with sparse one-hot encodings.
- - Semantic geometry in embeddings: semantic or functional similarity is encoded as geometric relations (proximity, direction, subspaces) in the embedding space.
- - Vector arithmetic / linear relations: certain semantic relations can correspond to linear vector operations in embedding space (analogy examples).
- - Normalization of embeddings for similarity comparisons: embeddings are sometimes normalized (unit norm) before using directional similarity measures.

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Modern ML models can’t directly “think” in words, IDs, or categories. They can only compute with numbers—especially vectors. Vector embeddings are the bridge: they turn discrete items into continuous **v** ∈ ℝᵈ so geometry (dot products, angles, distances) becomes a usable language for meaning and function.

TL;DR:

A vector embedding is a learned mapping x ↦ **e**ₓ ∈ ℝᵈ from a discrete item (token/word/category) to a dense vector. Similar items end up with similar directions (high cosine similarity) and often similar positions (small distance). Embeddings are usually implemented as a trainable lookup table (an “embedding matrix”) and are the standard inputs to attention, where dot products between embeddings produce relevance scores.

## What Is Vector Embeddings?

### Why we need them (motivation)

Discrete items—like words, tokens, product IDs, user IDs, categorical features, or graph nodes—don’t naturally live in a space where “closeness” or “similarity” is meaningful.

- •If we label words by integers (cat=17, dog=53), then 53 − 17 = 36 is meaningless.
- •If we use one-hot vectors, the representation is huge and *every* distinct item is orthogonal to every other (cosine similarity 0), so geometry cannot express “cat is closer to dog than to spaceship.”

Embeddings solve this by giving each item a dense vector **e**ₓ ∈ ℝᵈ. Once items are vectors, we can compare them with dot products, cosine similarity, and distances. That makes “interaction” between items (in attention, retrieval, classification, etc.) a simple geometric computation.

### Definition

An **embedding** is a function (often learned) that maps a discrete item x to a continuous vector:

- •x ∈ V (a vocabulary / set of IDs)
- •**e**ₓ ∈ ℝᵈ (a d-dimensional real vector)

We write:

- •**e**ₓ = Emb(x)

In many neural networks, Emb(·) is implemented as a lookup table (a matrix) with one vector per item.

### Intuition: “meaning as location”

The core intuition is not that embeddings store dictionary definitions. Instead:

- •Items that behave similarly in the model’s task get pushed to similar vectors.
- •“Similarity” becomes “close direction” (cosine similarity) or “close point” (distance).

For language, distributional learning yields the classic idea: “You know a word by the company it keeps.” If two words appear in similar contexts, a training objective will encourage their embeddings to become similar.

### Dense vs sparse representations

A one-hot vector **x** ∈ {0,1}^|V| is sparse: exactly one 1 and the rest 0. An embedding **e**ₓ ∈ ℝᵈ is dense: typically all d components are nonzero.

A useful comparison:

| Representation | Dimensionality | Similarity structure | Parameters | Pros | Cons |
| --- | --- | --- | --- | --- | --- |
| Integer ID | 1 | none | 0 | compact | no geometry |
| One-hot |  | V |  | orthogonal | 0 | simple | huge, no similarity |
| Embedding | d (e.g., 128–4096) | learned geometry |  | V | ·d | expressive, compact | must be learned |

Embeddings are “compact but expressive.” They trade fixed semantics (one-hot) for learnable semantics (geometry).

### The key symbol

We’ll use **e**ₓ to denote the embedding vector for item x:

- •**e**ₓ ∈ ℝᵈ

And we’ll often compare embeddings using cosine similarity (prerequisite):

cos(**a**, **b**) = (**a** · **b**) / (‖**a**‖ ‖**b**‖)

Cosine similarity focuses on *direction*, which is often what matters in learned representation spaces.

### What embeddings are not

1. 1)**Not uniquely defined:** Many embedding spaces are equivalent up to rotation/reflection, because objectives depend on dot products and distances.
2. 2)**Not guaranteed “human semantic”:** They capture what helps the training loss, which may include biases or spurious correlations.
3. 3)**Not always global coordinates:** Some models care about relative comparisons (angles/dots) more than absolute axes.

Embeddings are a learned coordinate system designed to make downstream computation easy.

## Core Mechanic 1: The Embedding Matrix (Lookup Table) and How It Learns

### Why a lookup table works

When x is a discrete ID, the simplest parameterization is: assign a trainable vector to each ID. Collect these vectors into a matrix **E**.

Let:

- •Vocabulary size: |V|
- •Embedding dimension: d
- •Embedding matrix: **E** ∈ ℝ^{|V|×d}

Row i of **E** is the embedding for token i:

- •**e**ᵢ = **E**[i]

This is literally a learned table.

### From one-hot to embedding: a clean algebraic view

If **x** is a one-hot vector representing item i, then the embedding lookup is equivalent to matrix multiplication:

- •**x** ∈ {0,1}^{|V|}
- •**E** ∈ ℝ^{|V|×d}

Compute:

**e** = **x**ᵀ **E**

Because **x** has a single 1 at index i, **x**ᵀ **E** selects the i-th row.

This equivalence is useful for understanding gradients: the model updates the row(s) corresponding to the IDs it sees.

### How embeddings get trained (gradient intuition)

Embeddings are learned because they participate in a loss. The loss might come from:

- •Next-token prediction (language modeling)
- •Masked token prediction
- •Contrastive objectives (push positives together, negatives apart)
- •Classification/regression (embedding feeds a predictor)

Regardless of the objective, the embedding vectors are parameters. During backprop, the gradient ∂L/∂**e**ₓ updates **e**ₓ.

A simple mental model:

- •If the model wants x to behave more like y, it nudges **e**ₓ toward **e**ᵧ (in direction).
- •If it wants them distinct, it nudges them apart.

### A concrete training objective: softmax classifier from embeddings

Consider a very common pattern: predict a label y from an embedding **h** (which could be **e**ₓ or a contextual vector). Use a linear layer and softmax:

- •logits: **z** = **W** **h** + **b**
- •probabilities: p = softmax(**z**)

Loss for true class c:

L = −log p\_c

Even if you don’t memorize softmax gradients, the key is:

- •**h** is pushed to increase the logit of the correct class
- •that pressure flows backward into embeddings if **h** depends on them

So embeddings become whatever vectors make the rest of the network succeed.

### Embedding dimension d: capacity vs generalization

Why not make d enormous?

- •Larger d increases capacity: more ways to place items distinctly.
- •But it increases parameters: |V|·d, memory, and risk of overfitting (especially for rare items).

A useful rule of thumb: pick d based on data scale, vocabulary size, and task complexity. In transformers, d often matches the model width so embeddings can be added to positional encodings and fed into attention.

### Weight tying: input embeddings and output embeddings

In language models, there are often two related matrices:

- •Input embeddings: map token IDs → vectors
- •Output weights: map hidden state → vocabulary logits

Sometimes these are tied (shared): output weight matrix **W** is set to **E**ᵀ.

Why tie?

- •Reduces parameters
- •Encourages a consistent geometry: tokens used as inputs live in the same space as tokens being predicted

### Initialization and scale

Embeddings are usually initialized randomly with small variance. Scale matters because dot products and norms affect attention scores and softmax logits.

In attention, if dot products get too large, softmax can saturate (become too peaky). That’s one reason scaled dot-product attention uses 1/√d.

Even before attention, stable embedding scales help optimization.

### Special tokens and feature embeddings

Embeddings aren’t just for words:

- •[CLS], [SEP], [MASK] tokens
- •categorical features (country, device type)
- •discretized numeric bins
- •IDs (user, item)

In all cases, the embedding is a learned vector that becomes a “handle” for the model to condition on.

### Summary of this mechanic

- •Embeddings often live in a matrix **E** ∈ ℝ^{|V|×d}
- •Lookup is row selection (or one-hot × matrix)
- •Training nudges vectors to support a task objective
- •d controls capacity and compute/memory

This gives us the basic object: **e**ₓ. Next we’ll focus on the *geometry* of embeddings—what dot products and angles mean, and why that geometry becomes the substrate for attention.

## Core Mechanic 2: Embedding Geometry—Similarity, Dot Products, and Distance

### Why geometry matters

Once items are vectors, the model can compute interactions with fast linear algebra. The most common interaction is a dot product:

- •**a** · **b** = ∑ᵢ aᵢ bᵢ

Dot products are cheap, differentiable, and deeply connected to angles and lengths. This is why embeddings pair naturally with attention.

But: dot products depend on both direction and magnitude. Cosine similarity removes magnitude to focus on direction:

cos(**a**, **b**) = (**a** · **b**) / (‖**a**‖ ‖**b**‖)

So you should keep two pictures in mind:

1. 1)**Directional similarity** (angle) → cosine similarity
2. 2)**Positional proximity** (distance) → Euclidean distance

### Angle vs distance

For **a**, **b** ∈ ℝᵈ:

- •Euclidean distance: ‖**a** − **b**‖
- •Squared distance: ‖**a** − **b**‖²

Expand squared distance:

‖**a** − **b**‖²

= (**a** − **b**) · (**a** − **b**)

= **a**·**a** − 2**a**·**b** + **b**·**b**

= ‖**a**‖² − 2(**a**·**b**) + ‖**b**‖²

This shows a key link:

- •If norms are similar (‖**a**‖ ≈ ‖**b**‖), then minimizing distance is roughly equivalent to maximizing dot product.

If we L2-normalize embeddings (force ‖**e**ₓ‖ = 1), then:

‖**a** − **b**‖² = 2 − 2(**a**·**b**)

and since **a**·**b** = cos(**a**, **b**) for unit vectors:

‖**a** − **b**‖² = 2 − 2 cos(**a**, **b**)

So for normalized embeddings:

- •maximizing cosine similarity ⇔ minimizing Euclidean distance

This is why many retrieval systems store normalized embeddings.

### What makes embeddings “semantic” (or functional)

Embeddings encode whatever similarity the training process rewards.

- •In word2vec-style objectives, words sharing contexts end up near each other.
- •In recommender systems, users/items that co-occur in interactions become aligned.
- •In supervised tasks, categories that share predictive patterns can cluster.

The geometry becomes a compressed record of these pressures.

### Similarity is task-relative

Two important consequences:

1. 1)If you train embeddings for sentiment classification, “good” and “great” may cluster, but also “awful” and “terrible.” That’s still semantic—but shaped by sentiment.
2. 2)If you train embeddings for code completion, “for” and “while” may cluster functionally.

So “semantic similarity” is better read as **useful similarity under the objective**.

### The dot product as “compatibility”

In many neural modules, the dot product between embeddings stands for compatibility.

- •High **q**·**k** → query and key match
- •High **u**·**v** → user and item match

This is a learned notion of compatibility because **q**, **k**, **u**, **v** come from learned embeddings or learned projections of embeddings.

### Anisotropy and frequency effects

Real embedding spaces often have quirks:

- •**Frequency dominance:** common tokens can become “central,” showing high similarity with many tokens.
- •**Anisotropy:** vectors may cluster in a narrow cone rather than filling the sphere.

These effects can harm retrieval or similarity search because cosine similarities become less discriminative.

Mitigations include:

- •mean-centering embeddings
- •whitening / PCA postprocessing
- •training objectives that encourage uniformity
- •normalization and temperature scaling

### Regularization and constraints

Sometimes we add constraints to shape geometry:

- •L2 regularization encourages small norms
- •normalization encourages unit norms
- •contrastive losses explicitly control angles via margins/temperatures

Each choice changes how dot products translate into probabilities.

### Embeddings as points, but also as basis coordinates

Another way to view embedding components:

- •Each dimension can be seen as a latent feature axis.
- •But axes are not individually interpretable in general; meaning is distributed across dimensions.

You’ll occasionally find interpretable directions (e.g., sentiment), but that’s not guaranteed.

### Summary of this mechanic

- •Similarity usually means cosine similarity or dot product
- •For unit vectors, cosine similarity and Euclidean distance are tightly linked
- •Geometry is shaped by the training objective (functional similarity)
- •Dot products act as compatibility scores, setting up attention and retrieval

## Application/Connection: Embeddings as the Inputs to Attention (and Beyond)

### Why attention needs embeddings

Attention mechanisms operate on vectors. If your input is discrete tokens, you must first map them to vectors—embeddings.

In a transformer, a typical pipeline is:

1. 1)Tokenize text → token IDs x₁, …, xₙ
2. 2)Lookup embeddings → **e**₁, …, **e**ₙ where **e**ᵢ = **e**\_{xᵢ}
3. 3)Add positional information → **h**ᵢ⁽⁰⁾ = **e**ᵢ + **p**ᵢ
4. 4)Apply attention layers to compute contextual vectors

So embeddings are the “raw material” that attention will mix.

### From embeddings to queries/keys/values

Self-attention doesn’t usually compare raw embeddings directly. It projects them:

- •**q**ᵢ = **W**\_Q **h**ᵢ
- •**k**ᵢ = **W**\_K **h**ᵢ
- •**v**ᵢ = **W**\_V **h**ᵢ

Then attention scores use dot products:

score(i, j) = (**q**ᵢ · **k**ⱼ) / √d\_k

and weights are softmax over j.

Even though **q**, **k**, **v** are projected, their *source* is the embedding space. The structure of embeddings strongly influences what the model can learn efficiently:

- •If related tokens begin in reasonable positions, attention can learn useful patterns with fewer updates.
- •If embeddings are poorly trained, attention must compensate by learning more complex projections.

### Embeddings beyond tokens

Transformers also embed:

- •**positions** (positional embeddings)
- •**segments** (token-type embeddings)
- •**patches** in vision transformers
- •**features** in tabular transformers

The concept is the same: a discrete unit becomes a vector so attention can compare and combine units.

### Retrieval and nearest neighbors

Embeddings are also used for retrieval:

- •Encode a query to **q**
- •Encode items/documents to **d**ᵢ
- •Retrieve top-k by cosine similarity or dot product

This is the backbone of semantic search and RAG systems.

If embeddings are normalized, ranking by cosine similarity is equivalent to ranking by dot product.

### Recommendation systems

User and item embeddings are classic:

- •**u** = embedding(user\_id)
- •**v** = embedding(item\_id)

A simple predictor is a dot product:

ŷ = **u** · **v**

If user u likes items similar to v, the training objective increases **u**·**v**, bringing vectors into alignment.

### Practical considerations

**Memory:** embedding tables can dominate parameter count when |V| is large.

- •Parameters: |V|·d
- •Example: |V| = 200k, d = 1024 → ~205 million floats

Common solutions:

- •smaller d
- •vocabulary pruning
- •subword tokenization (reduces |V|)
- •adaptive embeddings / factorization
- •quantization for serving

**OOV and rare items:**

- •Use subwords (BPE, WordPiece)
- •Use hashing tricks for categorical features
- •Use shared embeddings for unknown/rare buckets

**Fine-tuning vs freezing:**

- •Fine-tuning changes embeddings, aligning them to a new task
- •Freezing keeps geometry stable, relying on higher layers

### Connection forward: why this unlocks Attention Mechanisms

Attention is fundamentally about *similarity-weighted mixing*. Similarity is computed by dot products between vectors.

Embeddings provide:

- •a vector per discrete unit
- •an initial geometry where dot products/angles encode useful relationships

Once you have **e**ₓ, attention can form **q**, **k**, **v** and compute relevance.

This is why “Vector Embeddings” is a prerequisite: without vectorization, there is no meaningful similarity computation to drive attention.

Next node: [Attention Mechanisms](/tech-tree/attention-mechanisms/).

## Worked Examples (3)

### Example 1: Embedding lookup as matrix multiplication (one-hot × embedding matrix)

Suppose a tiny vocabulary V = {A, B, C} with |V| = 3 and embedding dimension d = 2. Let the embedding matrix be

**E** = [

[1, 0],

[2, 1],

[0, 3]

] (shape 3×2)

Rows correspond to A, B, C in that order. We want the embedding for token B.

1. Represent token B as a one-hot vector **x** ∈ ℝ³:

   **x** = [0, 1, 0]
2. Compute the embedding as **e** = **x**ᵀ **E**:

   **e** = [0, 1, 0] · [

   [1, 0],

   [2, 1],

   [0, 3]

   ]
3. Multiply:

   **e** = 0·[1, 0] + 1·[2, 1] + 0·[0, 3]

   = [2, 1]
4. So **e**\_B = [2, 1].

**Insight:** An embedding lookup is algebraically “one-hot selection.” In backprop, only the selected row(s) receive gradients, which is why embedding tables train efficiently even for huge vocabularies.

### Example 2: Relating cosine similarity and Euclidean distance for normalized embeddings

Let **a**, **b** ∈ ℝ² be two unit vectors (‖**a**‖ = ‖**b**‖ = 1). Suppose **a**·**b** = 0.8. Compute cos(**a**, **b**) and ‖**a** − **b**‖², and interpret.

1. Because both vectors are unit length, cosine similarity equals the dot product:

   cos(**a**, **b**) = (**a**·**b**) / (‖**a**‖‖**b**‖) = 0.8 / (1·1) = 0.8
2. Compute squared distance using the expansion:

   ‖**a** − **b**‖²

   = ‖**a**‖² − 2(**a**·**b**) + ‖**b**‖²

   = 1 − 2(0.8) + 1
3. Finish:

   ‖**a** − **b**‖² = 2 − 1.6 = 0.4
4. Optionally compute distance:

   ‖**a** − **b**‖ = √0.4 ≈ 0.632

**Insight:** For unit-normalized embeddings, high cosine similarity implies small Euclidean distance (and vice versa). This is why many retrieval systems normalize embeddings: it makes geometry consistent and simplifies ranking.

### Example 3: A tiny attention-like similarity score from embeddings

Suppose you have three token embeddings in ℝ²:

**e**₁ = [1, 0]

**e**₂ = [1, 1]

**e**₃ = [0, 1]

Treat token 2 as a “query” and compute raw dot-product scores sⱼ = **e**₂ · **e**ⱼ for j ∈ {1,2,3}.

1. Compute s₁ = **e**₂ · **e**₁:

   s₁ = [1, 1] · [1, 0] = 1·1 + 1·0 = 1
2. Compute s₂ = **e**₂ · **e**₂:

   s₂ = [1, 1] · [1, 1] = 1 + 1 = 2
3. Compute s₃ = **e**₂ · **e**₃:

   s₃ = [1, 1] · [0, 1] = 0 + 1 = 1
4. Interpretation: token 2 is most similar to itself (score 2) and equally similar to tokens 1 and 3 (score 1).

**Insight:** Attention scoring is built on dot products of vectors. Even before adding projections (**W**\_Q, **W**\_K), the embedding geometry already determines which tokens are “compatible.”

## Key Takeaways

- ✓

  An embedding maps a discrete item x to a dense vector **e**ₓ ∈ ℝᵈ, enabling similarity computations.
- ✓

  A common implementation is an embedding matrix **E** ∈ ℝ^{|V|×d}; lookup selects a row (equivalently one-hot × **E**).
- ✓

  Embedding geometry is shaped by the training objective, so “similarity” means “useful similarity for the task.”
- ✓

  Cosine similarity compares directions: cos(**a**, **b**) = (**a**·**b**) / (‖**a**‖‖**b**‖).
- ✓

  For unit vectors, ‖**a** − **b**‖² = 2 − 2 cos(**a**, **b**), linking distance and cosine similarity tightly.
- ✓

  Dot products serve as learned compatibility scores; this is the core numeric operation behind attention and retrieval.
- ✓

  Embedding tables can dominate parameters (|V|·d), motivating subword tokenization, pruning, factorization, or quantization.

## Common Mistakes

- ✗

  Assuming embedding axes have fixed human-interpretable meaning; in general, meaning is distributed and coordinates are not unique.
- ✗

  Comparing dot products across models or setups without accounting for norms/normalization; magnitudes can distort similarity if not controlled.
- ✗

  Forgetting that embeddings reflect the training objective (and data biases), not an absolute notion of semantic truth.
- ✗

  Choosing an embedding dimension d without considering vocabulary size, data availability, and memory/compute constraints.

## Practice

easy

You have normalized embeddings (‖**a**‖ = ‖**b**‖ = 1). If cos(**a**, **b**) = 0.3, compute ‖**a** − **b**‖² and ‖**a** − **b**‖.

**Hint:** Use ‖**a** − **b**‖² = 2 − 2 cos(**a**, **b**) for unit vectors.

Show solution

‖**a** − **b**‖² = 2 − 2(0.3) = 2 − 0.6 = 1.4.

‖**a** − **b**‖ = √1.4 ≈ 1.183.

medium

Let |V| = 50,000 and d = 768. Approximately how many parameters are in the embedding table? If stored as float32 (4 bytes), about how much memory does it take?

**Hint:** Parameters = |V|·d. Memory = parameters × 4 bytes. Convert to MB or GB.

Show solution

Parameters = 50,000 × 768 = 38,400,000.

Memory ≈ 38.4 million × 4 bytes = 153.6 million bytes.

In MB: 153.6e6 / (1024²) ≈ 146.5 MB (about 150 MB).

medium

Suppose **E** ∈ ℝ^{4×3} is an embedding matrix for tokens {0,1,2,3}. If a training batch contains tokens [1, 1, 3], which rows of **E** receive gradient updates during backprop through an embedding lookup? Explain briefly.

**Hint:** Only looked-up rows are involved in the forward computation; repeated tokens accumulate gradients on the same row.

Show solution

Rows 1 and 3 receive gradient updates. Row 1 appears twice in the batch, so its gradient contributions accumulate (sum) for that row. Rows 0 and 2 receive no update from this batch because they were not looked up.

## Connections

Next: [Attention Mechanisms](/tech-tree/attention-mechanisms/)

Related nodes you may want nearby in the tech tree:

- •[Cosine Similarity](/tech-tree/cosine-similarity/)
- •[Softmax and Cross-Entropy](/tech-tree/softmax-cross-entropy/)
- •[Nearest Neighbor Search](/tech-tree/nearest-neighbor-search/)
- •[Tokenization (BPE/WordPiece)](/tech-tree/tokenization/)
- •[Contrastive Learning](/tech-tree/contrastive-learning/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
