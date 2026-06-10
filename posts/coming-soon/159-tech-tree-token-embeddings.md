---
title: Token Embeddings
description: Representation of discrete tokens (words, subwords, tokens) as continuous vectors used as input to neural models; includes learned embeddings and embedding lookup/initialization. Understanding embeddings covers dimensionality, lookup tables, and basic properties like semantic similarity in vector space.
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
inspiration_url: https://templeton.host/tech-tree/token-embeddings/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/token-embeddings/](https://templeton.host/tech-tree/token-embeddings/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Token Embeddings

Machine LearningDifficulty: ★★★☆☆Depth: 0Unlocks: 2

Representation of discrete tokens (words, subwords, tokens) as continuous vectors used as input to neural models; includes learned embeddings and embedding lookup/initialization. Understanding embeddings covers dimensionality, lookup tables, and basic properties like semantic similarity in vector space.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Embedding lookup: discrete token ID is mapped to a continuous vector via an embedding table (lookup).
- -Embeddings are model parameters: vectors are initialized and learned/updated during model training.
- -Embedding dimensionality: each token vector has fixed length d that sets representational capacity.

## Key Symbols & Notation

E (embedding matrix)d (embedding dimensionality)

## Essential Relationships

- -Lookup relationship: token index i -> row E[i], which is a vector in R^d.

## Unlocks (2)

[Sequence Masking (causal and padding masks)lvl 4](/tech-tree/sequence-masking/)[Transformerslvl 5](/tech-tree/transformers/)

Advanced Learning Details

### Graph Position

6

Depth Cost

2

Fan-Out (ROI)

1

Bottleneck Score

0

Chain Length

### Cognitive Load

6

Atomic Elements

30

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (11)

- - Discrete token: a vocabulary item (word/subword/token) treated as an atomic symbol
- - Token embedding: representing a discrete token as a continuous vector
- - Embedding matrix / lookup table: a table of vectors indexed by token id
- - Learned embeddings: embedding vectors that are model parameters updated during training
- - Embedding dimensionality: the vector length (number of features) used for each token
- - One-hot representation as an index into embeddings: using a one-hot vector or integer index to select an embedding
- - Embedding initialization: common ways to initialize embedding vectors (random, pretrained)
- - Subword tokens and shared embeddings: using subword units (BPE/wordpiece) and sharing vectors across subword types
- - Out-of-vocabulary (OOV) handling: strategies for tokens not present in the vocabulary (UNK token, subword decomposition)
- - Semantic geometry: interpretability of vector relationships (similarity, analogies) in the embedding space
- - Embedding as input feature: embeddings serve as the continuous input to subsequent neural network layers

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Neural networks don’t naturally understand discrete symbols like “cat”, “##ing”, or token ID 50256. Token embeddings are the bridge: they turn a token into a continuous vector **v** ∈ ℝᵈ that a model can compute with.

TL;DR:

A token embedding is a learned vector representation for each token in a vocabulary. All embeddings live in an embedding matrix E ∈ ℝ^(V×d). Given a token ID i, the model retrieves the i-th row E[i] (an embedding lookup) to produce **eᵢ** ∈ ℝᵈ, which becomes the input to downstream layers (e.g., attention/Transformer blocks). Embeddings are parameters: they’re initialized, updated by backprop, and their dimensionality d controls capacity and compute.

## What Is Token Embedding?

### Why we need embeddings (motivation before formulas)

Neural networks are built to process numbers: vectors, matrices, and tensors. But language (and many discrete domains) start as symbols:

- •Words: “apple”, “bank”
- •Subwords: “un”, “##able”
- •Characters: “a”, “b”
- •Generic tokens: IDs produced by a tokenizer

A token by itself has **no natural numeric geometry**. Token ID 7 isn’t “closer” to token ID 8 than to token ID 9000, yet a neural network will treat raw numbers that way.

So we introduce a representation that:

1) Is numeric (so the model can compute),

2) Has a geometry (so “similar” tokens can end up close),

3) Is learnable (so it adapts to the training data).

That representation is the **token embedding**.

### Definition

Let the vocabulary size be V (number of distinct tokens) and let the embedding dimensionality be d.

We store an **embedding matrix**:

- •E ∈ ℝ^(V×d)

Each token i (an integer ID in {0, …, V−1}) is assigned the i-th row of E:

- •**eᵢ** = E[i] ∈ ℝᵈ

This is a **lookup table**: you don’t compute E[i] by multiplying all of E by something dense; you directly retrieve a row.

### Intuition: embeddings as “coordinates”

You can think of embeddings as placing each token at a point in a d-dimensional space. During training, the model moves these points around to make its predictions better.

- •If two tokens behave similarly in context, training often moves their vectors closer.
- •If two tokens are used differently, their vectors drift apart.

This doesn’t guarantee a perfect semantic map, but it gives the model a flexible continuous “surface” on which to build meaning.

### What embeddings are *not*

- •Not one-hot vectors: one-hot is sparse and high-dimensional (dimension V), and doesn’t express similarity.
- •Not fixed unless you choose them to be: E is typically learned from scratch or fine-tuned.
- •Not necessarily interpretable coordinate-by-coordinate: meaning is distributed across dimensions.

### Where embeddings appear in a model

In a typical language model pipeline:

1) Text → tokenizer → token IDs (integers)

2) Token IDs → embedding lookup in E → vectors **e₁**, **e₂**, …

3) Vectors → Transformer (or other neural network) → predictions

So token embeddings are often the **first learned layer** of a modern NLP model.

## Core Mechanic 1: Embedding Lookup via the Matrix E

### Why lookup matters

A token ID is discrete. The model must map it to a continuous vector **e** ∈ ℝᵈ *efficiently*.

If V is large (e.g., 50k, 200k, 1M), you cannot afford to treat the input as a dense V-dimensional vector at every step. The embedding matrix lets you:

- •store V vectors once,
- •retrieve only the ones you need.

### One-hot view (conceptual bridge)

Conceptually, you can represent token i as a one-hot vector **xᵢ** ∈ {0,1}^V with a 1 at position i.

Then embedding lookup can be written as a matrix product:

- •**eᵢ** = **xᵢ**ᵀ E

Let’s check shapes:

- •**xᵢ**ᵀ has shape (1×V)
- •E has shape (V×d)
- •product has shape (1×d) → a vector in ℝᵈ

This multiplication selects exactly one row of E, because all entries of **xᵢ** are 0 except at i.

### Why implementations don’t multiply

Even though **xᵢ**ᵀ E is a nice equation, real implementations do an index operation:

- •**eᵢ** = E[i]

Because multiplying by a V-length one-hot vector would waste memory and compute.

### Batching and sequences

In practice you have a batch of sequences:

- •Batch size: B
- •Sequence length: T
- •Token IDs: X ∈ {0,…,V−1}^(B×T)

Embedding lookup produces:

- •Embeddings: H ∈ ℝ^(B×T×d)

So each position t in each sequence b gets a vector:

- •**h**[b,t] = E[ X[b,t] ]

### A careful note about “row vectors” vs “column vectors”

Different sources use different conventions. You might see embeddings as rows E[i] or columns. The key invariant is:

- •Each token corresponds to a length-d vector.

In this lesson we treat E as V rows, each row is **eᵢ** ∈ ℝᵈ.

### Parameter count and memory

Embeddings can dominate parameter count.

- •Number of parameters in E: V·d

Example:

- •V = 50,000
- •d = 768

Parameters = 50,000 · 768 = 38,400,000

That’s 38.4M parameters just for token embeddings.

### Basic similarity geometry

Once tokens are vectors, you can measure similarity.

Two common measures:

1) Dot product:

- •sim(**a**, **b**) = **a**·**b** = ∑ⱼ aⱼ bⱼ

2) Cosine similarity:

- •cos(**a**, **b**) = (**a**·**b**) / (‖**a**‖ ‖**b**‖)

Cosine similarity compares direction, not magnitude. Many embedding analyses use cosine similarity to focus on relational structure.

### Why similarity emerges at all

Embeddings are optimized to help the model predict correct outputs. If the model benefits from treating two tokens similarly (because they appear in similar contexts), gradient descent tends to push their embeddings in similar directions.

This is not magic; it’s just shared pressure from the loss function across many training examples.

## Core Mechanic 2: Embeddings Are Learned Parameters (Initialization and Updates)

### Why embeddings must be learnable

You could assign each token a random vector and never change it. The model would then have to learn everything in later layers, with no ability to shape the input representation.

Learnable embeddings let the model:

- •allocate representational capacity where needed,
- •encode frequent patterns early,
- •reduce burden on deeper layers.

Formally, E is part of the model parameters θ.

### Initialization

Common initialization strategies:

- •Random normal: E[i,j] ∼ 𝒩(0, σ²)
- •Xavier/Glorot or Kaiming style scaling (depending on architecture)

A typical goal is to keep activations at reasonable scale early in training.

If σ is too large:

- •early activations can explode

If σ is too small:

- •signals and gradients can vanish

### How the embedding row gets updated (the key idea)

Suppose in one training step you see token i at some position. The forward pass retrieves **eᵢ** = E[i]. The loss L depends on that vector through downstream computations.

Backprop computes the gradient:

- •∂L/∂E

But importantly:

- •Only the rows of E corresponding to tokens that appeared in the batch get nonzero gradients.

This matches the lookup behavior: you only “touch” the embeddings you used.

### A small derivation: gradient for a simple downstream linear layer

Consider a toy model:

1) Lookup: **eᵢ** = E[i]

2) Linear: **z** = W**eᵢ** + **b**

3) Loss L depends on **z**

Let’s compute ∂L/∂**eᵢ**.

We use chain rule:

- •∂L/∂**eᵢ** = (∂**z**/∂**eᵢ**)ᵀ (∂L/∂**z**)

But **z** = W**eᵢ** + **b**, so:

- •∂**z**/∂**eᵢ** = W

Thus:

- •∂L/∂**eᵢ** = Wᵀ (∂L/∂**z**)

And since **eᵢ** is the i-th row of E, the gradient for E[i] is exactly ∂L/∂**eᵢ**.

Finally, a gradient descent update (learning rate η):

- •E[i] ← E[i] − η (∂L/∂E[i])

Every time token i appears, its vector is nudged to reduce loss.

### Frequency effects

Tokens that appear more often get updated more often.

This can be good (more data) but also can cause imbalance:

- •very frequent tokens may dominate training dynamics
- •rare tokens may remain undertrained

Some tokenization strategies (subwords) help reduce the number of truly rare tokens by composing words out of more frequent pieces.

### Embedding tying (brief but important)

In many language models, the input embedding matrix E is tied (shared) with the output projection matrix used to predict token logits.

If output logits are computed as:

- •logits = H Eᵀ

then E serves two roles:

- •mapping token IDs to vectors (input)
- •mapping hidden states back to vocabulary scores (output)

This reduces parameters and often improves performance, but it couples constraints: the same geometry must serve both input and output.

### Pretrained embeddings vs learned from scratch

You can initialize E using pretrained vectors (word2vec/GloVe) or from a pretrained transformer.

Comparing options:

| Approach | Pros | Cons | When used |
| --- | --- | --- | --- |
| Train E from scratch | Simple; fully task-adapted | Needs lots of data; slow to learn semantics | New domains, sufficient data |
| Initialize from pretrained | Faster convergence; better semantics early | May mismatch tokenizer/vocab; can bake in biases | Many NLP tasks |
| Freeze pretrained E | Stable; fewer trainable params | Limits adaptation; can hurt performance | Low-data or constrained training |

Even when using pretrained embeddings, fine-tuning (updating E) is common.

## Embedding Dimensionality d: Capacity, Generalization, and Cost

### Why d matters

The embedding dimensionality d is the length of each token vector **eᵢ** ∈ ℝᵈ.

Choosing d is a trade-off between:

- •**capacity**: how many distinctions the model can encode at the token level
- •**generalization**: whether the model learns robust patterns vs memorizing
- •**compute/memory**: E has V·d parameters, and embeddings flow through the whole network

### Capacity intuition

With larger d, each token has more degrees of freedom.

- •Small d (e.g., 32, 64): forces compression; may be insufficient for complex tasks
- •Medium d (e.g., 256, 512, 768): common in transformers
- •Large d (e.g., 1024, 2048+): higher capacity but expensive

But “bigger d” isn’t automatically better. If you don’t have enough data or model structure to use it, the extra dimensions can become noisy.

### Memory and compute scaling

Parameters in E scale linearly in d:

- •params(E) = V·d

The embedding activations for a batch scale as:

- •activation size ≈ B·T·d

So increasing d increases both parameter memory and the size of tensors passed through attention/MLP blocks.

### Matching d to model hidden size

In transformers, token embeddings are usually produced in the same dimension as the model’s hidden size (often called d\_model).

That way, you can add other vectors (like positional encodings) and pass embeddings directly into attention blocks without extra projections.

### A geometric view: dot products and norms

Many downstream operations depend on dot products.

For random vectors with independent components, dot products tend to grow with d unless normalized. This is one reason initialization and normalization layers matter.

If **a**, **b** have typical component scale σ, then expected magnitude:

- •‖**a**‖ ≈ √d · σ

So as d grows, norms grow unless σ shrinks. Good initialization tries to keep these scales stable.

### Practical heuristics

Common rules of thumb (not laws):

- •For small vocabularies and simple tasks, smaller d can work well.
- •For large language models, d is typically tied to architecture size.
- •If V is extremely large (e.g., millions), you may need smaller d or specialized techniques (adaptive embeddings, hashing, etc.).

The key is: d is a design knob controlling representational bandwidth at the input.

## Application/Connection: Embeddings as the Input Layer to Transformers (and What Comes Next)

### Where embeddings sit in the Transformer pipeline

A simplified Transformer input step:

1) Token IDs X ∈ {0,…,V−1}^(B×T)

2) Token embeddings: H\_tok[b,t] = E[X[b,t]]

3) Add positional information: H₀ = H\_tok + P

4) Pass through stacked attention + MLP blocks

The crucial point: attention doesn’t operate on token IDs; it operates on vectors.

### Positional information and why it’s separate

Token embeddings alone do not encode order. The tokens “dog bites man” vs “man bites dog” would be the same multiset of embeddings.

Transformers typically add a positional encoding/embedding P ∈ ℝ^(T×d) (or learned position embeddings) so each position t has its own vector **pₜ**.

Then:

- •**h₀,ₜ** = **e\_{xₜ}** + **pₜ**

This simple addition works because both are in ℝᵈ.

### Masking connection (why you’ll need it soon)

Once you have embeddings and pass them into attention, the model computes attention scores between positions.

But you often must prevent attention to:

- •padding tokens (so the model doesn’t treat padding as data)
- •future tokens in autoregressive models (causal masking)

Masking operates on attention score matrices, not on E directly—but embeddings are what make attention possible in the first place.

### Embeddings beyond language

The same idea applies broadly:

- •Recommender systems: user ID → embedding, item ID → embedding
- •Graphs: node ID → embedding
- •Multimodal: discretized image patches or code tokens → embeddings

Whenever you have a discrete symbol set, an embedding matrix is a standard first tool.

### What to watch for when you implement

A minimal checklist:

- •Ensure your token IDs are in range [0, V−1]
- •Decide how to handle padding tokens (often reserve an ID for PAD)
- •Decide whether PAD’s embedding is learned or fixed to **0**
- •Confirm embedding dimension d matches the model’s expected hidden size

These decisions will directly affect training stability and correctness.

## Worked Examples (3)

### Example 1: Embedding lookup as row selection (and the one-hot equivalence)

Let V = 5 and d = 3. Suppose the embedding matrix is

E =

[ [ 1, 0, 2],

[ 0, 1, 0],

[-1, 1, 1],

[ 2, 2, 2],

[ 0, -1, 3] ]

Token ID i = 2 (0-indexed). Compute **e₂** via lookup and via one-hot multiplication.

1. Lookup definition:

   **e₂** = E[2]

   So **e₂** = [−1, 1, 1].
2. Construct one-hot **x₂** ∈ ℝ^5:

   **x₂** = [0, 0, 1, 0, 0].
3. Compute **x₂**ᵀ E:

   **x₂**ᵀ E = 0·E[0] + 0·E[1] + 1·E[2] + 0·E[3] + 0·E[4]

   = E[2]

   = [−1, 1, 1].
4. Conclusion:

   The matrix formula **eᵢ** = **xᵢ**ᵀ E is exactly row selection in disguise.

**Insight:** Thinking in one-hot form explains the math, but thinking in lookup form explains the efficiency: only one row is needed, so gradients and updates also stay sparse over rows.

### Example 2: One gradient update to an embedding row

Toy model: **z** = W**eᵢ** (ignore bias). Let d = 2 and W =

[ [2, 0],

[0, 1] ]

Assume token i appears, with current embedding **eᵢ** = [1, −1]. Suppose backprop gives ∂L/∂**z** = [3, 4]. Compute ∂L/∂**eᵢ** and do one gradient step with η = 0.1.

1. We have **z** = W**eᵢ**. By chain rule:

   ∂L/∂**eᵢ** = Wᵀ (∂L/∂**z**).
2. Compute Wᵀ. Here W is diagonal-like, so Wᵀ = W:

   Wᵀ =

   [ [2, 0],

   [0, 1] ].
3. Multiply:

   ∂L/∂**eᵢ** = Wᵀ [3, 4]ᵀ

   = [ 2·3 + 0·4,

   0·3 + 1·4 ]

   = [6, 4].
4. Gradient descent update:

   **eᵢ** ← **eᵢ** − η (∂L/∂**eᵢ**)

   = [1, −1] − 0.1·[6, 4]

   = [1 − 0.6, −1 − 0.4]

   = [0.4, −1.4].
5. Interpretation:

   Only the embedding for token i is updated by this example; other token rows E[j] for j ≠ i are unchanged (for this single-token toy batch).

**Insight:** Embedding training is ordinary parameter learning; the only special feature is sparsity over vocabulary rows: you update the rows you looked up.

### Example 3: Measuring semantic similarity with cosine similarity

Suppose you have two token embeddings:

**a** = [2, 0, 1]

**b** = [1, 1, 0]

Compute dot product and cosine similarity.

1. Dot product:

   **a**·**b** = 2·1 + 0·1 + 1·0 = 2.
2. Norms:

   ‖**a**‖ = √(2² + 0² + 1²) = √(4 + 0 + 1) = √5.

   ‖**b**‖ = √(1² + 1² + 0²) = √2.
3. Cosine similarity:

   cos(**a**, **b**) = (**a**·**b**) / (‖**a**‖‖**b**‖)

   = 2 / (√5 · √2)

   = 2 / √10

   ≈ 0.632.

**Insight:** Cosine similarity normalizes away vector length, which is useful because embedding norms can vary for reasons unrelated to meaning (frequency, training dynamics, regularization).

## Key Takeaways

- ✓

  Token embeddings map discrete token IDs to continuous vectors **eᵢ** ∈ ℝᵈ that neural networks can process.
- ✓

  All token vectors live in an embedding matrix E ∈ ℝ^(V×d); lookup retrieves a row: **eᵢ** = E[i].
- ✓

  The one-hot equation **eᵢ** = **xᵢ**ᵀ E is conceptually helpful, but implementations use efficient indexing (no dense V-dimensional one-hot).
- ✓

  Embeddings are model parameters: they are initialized (often randomly) and updated by backprop; only rows used in a batch receive gradients.
- ✓

  Embedding dimensionality d controls representational capacity, parameter count (V·d), and activation/compute cost (B·T·d).
- ✓

  Vector-space similarity (dot product, cosine similarity) provides a way to analyze learned relations between tokens, though it’s not guaranteed to be purely “semantic.”
- ✓

  In Transformers, token embeddings are the first step; they’re typically combined with positional information before attention layers.

## Common Mistakes

- ✗

  Treating token IDs as numeric features (e.g., feeding raw IDs into a network) instead of using an embedding lookup.
- ✗

  Mismatching dimensions: choosing embedding d that doesn’t match the model’s expected hidden size (or forgetting a projection layer if you intentionally differ).
- ✗

  Forgetting special tokens: not reserving IDs for PAD/UNK/BOS/EOS or accidentally allowing PAD embeddings to influence training without masking.
- ✗

  Assuming embedding similarity always equals human-interpretable semantic similarity; training objective and data distribution strongly shape the geometry.

## Practice

easy

You have vocabulary size V = 10,000 and embedding dimensionality d = 256.

1) How many parameters are in E?

2) If parameters are stored as 32-bit floats, about how many megabytes does E take (ignore overhead)?

**Hint:** params = V·d. Memory ≈ params · 4 bytes. 1 MB ≈ 10⁶ bytes (roughly).

Show solution

1) params(E) = 10,000 · 256 = 2,560,000.

2) Memory ≈ 2,560,000 · 4 = 10,240,000 bytes ≈ 10.24 MB (about 10 MB).

medium

Let E ∈ ℝ^(4×2) be

E =

[ [ 0, 1],

[ 2, 0],

[−1, 3],

[ 4, −2] ]

A sequence of token IDs is [3, 1, 1, 0]. Write down the corresponding embedding vectors in order, and identify which rows of E are reused.

**Hint:** Lookup means E[i] is the i-th row. Reuse happens when the same ID appears multiple times.

Show solution

Embeddings:

ID 3 → E[3] = [4, −2]

ID 1 → E[1] = [2, 0]

ID 1 → E[1] = [2, 0]

ID 0 → E[0] = [0, 1]

Row reuse: row 1 is reused (appears twice).

hard

Suppose you are training a model and you notice that very rare tokens have poorly learned embeddings.

Give two strategies (modeling or preprocessing) that can help, and briefly explain why each helps.

**Hint:** Think about how often a token gets gradient updates and how tokenization affects frequency. Also consider parameter sharing or regularization.

Show solution

Two helpful strategies:

1) Use subword tokenization (BPE/WordPiece): rare words are decomposed into more frequent pieces, so the model learns embeddings for pieces with more updates, improving generalization to rare words.

2) Tie embeddings or use pretrained initialization: tying input/output embeddings shares statistical strength; pretrained embeddings (or starting from a pretrained LM) give rare tokens a better starting position in vector space, reducing the amount of task data needed to shape them.

(Other valid ideas include increasing data, using adaptive/hashed embeddings, or regularizing/averaging embeddings for low-frequency tokens.)

## Connections

- •Next: [Sequence Masking (causal and padding masks)](/tech-tree/sequence-masking/) — once tokens become vectors and enter attention, masking controls which positions are allowed to interact.
- •Next: [Transformers](/tech-tree/transformers/) — token embeddings (plus positional information) form the inputs that attention layers transform.
- •Related concept: [Vector Norms and Cosine Similarity](/tech-tree/vector-norms-cosine/) — useful for analyzing embedding geometry and semantic similarity.
- •Related concept: [Softmax and Cross-Entropy](/tech-tree/softmax-cross-entropy/) — the loss that often drives embedding learning in language models.

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
