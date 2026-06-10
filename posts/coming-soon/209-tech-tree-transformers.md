---
title: Transformers
description: Attention-based architecture. Multi-head attention, positional encoding.
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
permalink: /tech-tree/transformers/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Transformers

Machine LearningDifficulty: ★★★★★Depth: 14Unlocks: 0

Attention-based architecture. Multi-head attention, positional encoding.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Scaled dot-product self-attention implemented with learnable linear projections (queries, keys, values) to compute contextual token-to-token weighting across a sequence
- -Multi-head attention: multiple parallel attention heads applied to different linear projections whose outputs are concatenated to model multiple representation subspaces
- -Transformer layer: a repeatable block that applies multi-head attention and a position-wise feed-forward network, each wrapped by residual connection plus layer normalization, and stacked to form encoder/decoder (decoder adds masked self-attention and encoder-decoder cross-attention)

## Key Symbols & Notation

d\_model (model hidden dimension)h (number of attention heads)d\_k (per-head key/query dimension)

## Essential Relationships

- -d\_model = h \* d\_k (model dimension split across heads)
- -Multi-head attention = Concatenate(head\_1,...,head\_h) \* W\_O, where head\_i = Attention(Q W\_Qi, K W\_Ki, V W\_Vi)
- -Each sublayer uses residual + LayerNorm: output = LayerNorm(x + Sublayer(x)) (applied to attention and feed-forward)

## Prerequisites (7)

[Attention Mechanisms6 atoms](/tech-tree/attention-mechanisms/)[Layer Normalization6 atoms](/tech-tree/layer-normalization/)[Positional Encoding6 atoms](/tech-tree/positional-encoding/)[Token Embeddings6 atoms](/tech-tree/token-embeddings/)[Softmax and Logits5 atoms](/tech-tree/softmax-and-logits/)[Residual (Skip) Connections5 atoms](/tech-tree/residual-connections/)[Sequence Masking (causal and padding masks)5 atoms](/tech-tree/sequence-masking/)

Advanced Learning Details

### Graph Position

290

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

14

Chain Length

### Cognitive Load

9

Atomic Elements

45

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (15)

- - Queries, Keys, Values (Q, K, V) as specific linear projections of inputs used in attention computation
- - Scaled dot-product attention: computing attention scores via Q K^T, scaling by 1/sqrt(d\_k), applying softmax, then weighting V
- - Multi-head attention: running multiple independent attention 'heads' in parallel, each with its own projections, then concatenating results
- - Head splitting and per-head dimensionality: splitting the model dimension into h heads with per-head dimensions d\_k and d\_v (typically d\_k = d\_v = d\_model / h)
- - Final output projection after concatenating heads (linear layer W^O that maps concatenated head outputs back to d\_model)
- - Position-wise feed-forward network (FFN): two-layer MLP applied independently to each sequence position (same parameters for all positions) with a nonlinearity (e.g., ReLU or GELU)
- - Transformer layer/block structure: attention sublayer followed by residual connection + normalization, then FFN sublayer followed by residual connection + normalization (the 'Add & Norm' pattern as used in Transformers)
- - Encoder stack: repeated identical encoder layers (self-attention + FFN) forming the encoder
- - Decoder stack: repeated identical decoder layers where each layer performs masked self-attention, encoder–decoder (cross) attention, then FFN in that order
- - Masked (causal) self-attention inside the decoder as an implementation detail: using masks so decoder queries cannot attend to future positions
- - Application of attention masks via additive masking to logits (e.g., adding large negative values to masked score positions before softmax)
- - Embedding scaling practice: scaling token embeddings by sqrt(d\_model) (or similar) before adding positional encodings to stabilize magnitudes
- - Typical Transformer hyperparameters as design choices to learn (d\_model, d\_ff, h, number of layers N) and their role in model capacity
- - Motivation/benefit of multi-head attention: different heads can attend to different representation subspaces or patterns simultaneously
- - Shape and batching conventions implicit in Transformer computations (e.g., attention score matrix shape [seq\_len\_q, seq\_len\_k] per head and per batch)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Transformers are the first widely successful neural architecture where the main “engine” is not recurrence or convolution, but a learned, content-based routing system: attention. Once you understand the exact mechanics of scaled dot-product attention, multi-head attention, and the Transformer block (attention + feed-forward + residual + layer norm), most modern language and vision models become variations on a single theme.

TL;DR:

A Transformer processes a sequence by projecting token representations into queries, keys, and values, computing attention weights via softmax(QKᵀ/√d\_k) (with masks as needed), mixing values with those weights, and then applying a position-wise MLP—each sublayer wrapped with residual connections and layer normalization. Multi-head attention repeats attention in parallel with different projections, concatenates head outputs, and mixes them back to d\_model. Stacking these blocks yields encoders and decoders; decoders add causal masking and cross-attention to an encoder output.

## What Is a Transformer?

### Why Transformers exist (motivation)

Before Transformers, sequence modeling was dominated by RNNs/LSTMs/GRUs and CNN-based sequence models. Those families have two persistent pain points:

1) **Long-range dependencies are hard.** Even with gating, recurrent models struggle to move information across hundreds or thousands of steps.

2) **Parallelism is limited.** Recurrence is inherently sequential: to compute step t, you need step t−1. That slows training.

Transformers address both by making the core operation **all-to-all token interaction** in a single layer: every token can “look at” every other token (subject to masking). This interaction is differentiable, learnable, and highly parallelizable on GPUs/TPUs.

### The Transformer idea in one sentence

A Transformer layer repeatedly does:

- •**Mix information across tokens** using **self-attention** (content-based weighted averaging).
- •**Transform each token independently** using a **position-wise feed-forward network** (an MLP applied to each position).

Crucially, both steps are wrapped in **residual connections** and **layer normalization** for stable optimization.

### What a token representation looks like

Assume a sequence length L and model width d\_model.

- •Input embeddings form a matrix **X** ∈ ℝ^{L×d\_model}
- •Row i, written **xᵢ**, is the vector for token i.

Because attention has no inherent sense of order, we add **positional information**:

- •**X₀ = E + P**, where E are token embeddings and P are positional encodings (sinusoidal or learned).

### The two canonical Transformer families

| Family | Primary use | Blocks | Key masking |
| --- | --- | --- | --- |
| Encoder-only (e.g., BERT-style) | Understanding, classification, bidirectional context | self-attn + FFN | Padding mask only (no causal mask) |
| Decoder-only (e.g., GPT-style) | Autoregressive generation | masked self-attn + FFN | Causal + padding masks |
| Encoder–decoder (original) | Seq2seq (translation, summarization) | encoder: self-attn + FFN; decoder: masked self-attn + cross-attn + FFN | Decoder uses causal; cross-attn uses padding mask on encoder side |

This lesson focuses on the core mechanics that all of these share: scaled dot-product attention, multi-head attention, and the Transformer layer structure.

## Core Mechanic 1: Scaled Dot-Product Self-Attention (Q, K, V)

### Why attention is “routing”

Suppose token i needs information from token j (e.g., a pronoun needs its antecedent). Attention lets token i compute a **weighted mixture** of other tokens’ information.

The key design choice is: **weights depend on content** (learned similarity), not just distance.

### Queries, keys, values (the roles)

Each token representation **xᵢ** is linearly projected into three vectors:

- •**qᵢ** (query): what token i is looking for
- •**kᵢ** (key): what token i offers / how it can be matched
- •**vᵢ** (value): the information token i will contribute if attended to

In matrix form for a whole sequence **X** ∈ ℝ^{L×d\_model}:

- •**Q = XW\_Q**
- •**K = XW\_K**
- •**V = XW\_V**

where W\_Q, W\_K, W\_V are learned matrices.

Typically:

- •W\_Q ∈ ℝ^{d\_model×d\_k}
- •W\_K ∈ ℝ^{d\_model×d\_k}
- •W\_V ∈ ℝ^{d\_model×d\_v}

In most standard implementations, **d\_v = d\_k = d\_model / h** per head.

### Attention scores and why we scale by √d\_k

The raw similarity between token i and token j is the dot product:

- •score(i, j) = **qᵢ · kⱼ**

In matrix form, the score matrix is:

- •**S = QKᵀ** where S ∈ ℝ^{L×L}

If q and k components have roughly unit variance, then the dot product grows with dimension:

- •Var(**qᵢ · kⱼ**) ≈ d\_k

Large magnitudes push softmax into saturation, giving tiny gradients. To keep logits in a reasonable range, we scale:

- •**Ŝ = (QKᵀ) / √d\_k**

This is “scaled dot-product attention.”

### Softmax to turn scores into weights

For each query position i, we take a softmax over j:

- •**A = softmax(Ŝ)**

So Aᵢⱼ ≥ 0 and ∑ⱼ Aᵢⱼ = 1.

Interpretation: row i of **A** is a probability distribution over which tokens i will attend to.

### Masking (padding and causal)

Masks are incorporated by adding −∞ (or a very negative number) to disallowed positions before softmax.

Let **M** ∈ ℝ^{L×L} where:

- •Mᵢⱼ = 0 if attention from i to j is allowed
- •Mᵢⱼ = −∞ if disallowed

Then:

- •**A = softmax( (QKᵀ)/√d\_k + M )**

Two common masks:

1) **Padding mask**: disallow attending to padding tokens.

2) **Causal mask** (decoder): disallow attending to future tokens, i.e., j > i.

### Weighted sum of values

Finally, the output at each position i is a weighted sum of values:

- •**oᵢ = ∑ⱼ Aᵢⱼ vⱼ**

In matrix form:

- •**O = AV**

Where O ∈ ℝ^{L×d\_v}.

### Putting it together (single-head self-attention)

The full formula:

- •**Attention(X) = softmax( (XW\_Q)(XW\_K)ᵀ / √d\_k + M ) (XW\_V)**

### A geometric intuition

Dot products measure alignment. If **qᵢ** points in a similar direction to **kⱼ**, token i will attend more to token j. But because W\_Q and W\_K are learned, the model can invent similarity notions that match the task (syntax, coreference, topic, etc.).

### Complexity note (why long context is expensive)

Self-attention builds an L×L matrix of scores. That’s:

- •Time: O(L² d\_k)
- •Memory: O(L²)

This quadratic dependence is why long-context Transformers require approximations or architectural tricks—but the core mechanism remains the same.

## Core Mechanic 2: Multi-Head Attention (MHA)

### Why one attention “view” isn’t enough

A single attention map must decide one set of weights per token. But language often requires multiple simultaneous relationships:

- •One head might track **coreference** (pronouns → nouns).
- •Another might track **syntactic dependencies** (verbs → objects).
- •Another might focus on **local context** (previous few tokens).

Multi-head attention lets the model compute **multiple attention distributions in parallel**, each in its own learned subspace.

### The shape story: d\_model, h, d\_k

Let:

- •d\_model = model width
- •h = number of heads
- •d\_k = per-head query/key width

Commonly:

- •d\_k = d\_model / h

Example: d\_model = 768, h = 12 ⇒ d\_k = 64.

### Per-head projections

For head r ∈ {1,…,h}, we have separate projection matrices:

- •W\_Q^{(r)} ∈ ℝ^{d\_model×d\_k}
- •W\_K^{(r)} ∈ ℝ^{d\_model×d\_k}
- •W\_V^{(r)} ∈ ℝ^{d\_model×d\_v}

Compute:

- •**Q^{(r)} = XW\_Q^{(r)}**
- •**K^{(r)} = XW\_K^{(r)}**
- •**V^{(r)} = XW\_V^{(r)}**

Then each head output:

- •**O^{(r)} = softmax( Q^{(r)} (K^{(r)})ᵀ / √d\_k + M ) V^{(r)}**

### Concatenate and mix

Concatenate head outputs along the feature dimension:

- •**O\_concat = [O^{(1)} | O^{(2)} | … | O^{(h)}]**

If each O^{(r)} ∈ ℝ^{L×d\_v} and d\_v = d\_k, then O\_concat ∈ ℝ^{L×(h d\_k)} = ℝ^{L×d\_model}.

Then apply a final learned output projection:

- •**Y = O\_concat W\_O** where W\_O ∈ ℝ^{d\_model×d\_model}

This final mixing matters: it lets the model combine information across heads.

### Self-attention vs cross-attention inside MHA

Multi-head attention is a *pattern*, and it can be used in different places:

- •**Self-attention**: Q, K, V come from the same X.
- •**Cross-attention**: Q comes from decoder states X\_dec; K and V come from encoder states X\_enc.

Cross-attention formula:

- •**Attention(X\_dec, X\_enc) = softmax( (X\_dec W\_Q)(X\_enc W\_K)ᵀ / √d\_k + M ) (X\_enc W\_V)**

Here the decoder learns to retrieve information from the encoded source sequence.

### Practical interpretation of heads

A helpful mental model:

- •Each head defines its own “matching function” (via W\_Q and W\_K)
- •and its own “payload space” (via W\_V)

So attention isn’t only *where to look*; it’s also *what to bring back*.

### A note on head dimension choice

Holding d\_model fixed, increasing h decreases d\_k. There is a trade-off:

| Choice | Benefit | Cost |
| --- | --- | --- |
| More heads (higher h) | More parallel subspaces | Smaller d\_k per head (less capacity per head), overhead |
| Fewer heads | More capacity per head | Fewer distinct attention patterns |

Empirically, standard settings (8–32 heads depending on width) work well, but variants exist (multi-query, grouped-query attention) to reduce memory/compute during decoding.

## Core Mechanic 3: The Transformer Layer (Sublayers, Residuals, LayerNorm, FFN)

### Why the Transformer is a *stack* of simple blocks

A single attention layer can mix tokens once, but deep language understanding requires multiple rounds of:

- •gathering context
- •transforming it
- •gathering again at a higher abstraction

So Transformers stack identical blocks. The stability of deep stacking relies on **residual connections** and **layer normalization**.

### The canonical encoder layer

An encoder layer has two sublayers:

1) Multi-head self-attention (MHA)

2) Position-wise feed-forward network (FFN)

Each sublayer is wrapped by residual + layer norm. There are two common normalization conventions:

| Convention | Pattern | Notes |
| --- | --- | --- |
| Post-LN (original 2017) | X + Sublayer(X) → LN | Can be harder to optimize at great depth |
| Pre-LN (common today) | X → LN → Sublayer → X + … | Typically more stable for deep stacks |

We’ll write **pre-LN**, since it’s widely used.

### Pre-LN encoder layer equations

Let **X** ∈ ℝ^{L×d\_model} be the layer input.

**(1) Attention sublayer**

- •**U = LN(X)**
- •**A = MHA(U, U, U; M\_padding)**
- •**X′ = X + Dropout(A)**

**(2) Feed-forward sublayer**

- •**V = LN(X′)**
- •**F = FFN(V)**
- •**Y = X′ + Dropout(F)**

Output is **Y**.

### What “position-wise FFN” means

The FFN is the same MLP applied independently to each position.

Typical form:

- •**FFN(x) = W₂ σ(W₁ x + b₁) + b₂**

Where:

- •W₁ ∈ ℝ^{d\_model×d\_ff}
- •W₂ ∈ ℝ^{d\_ff×d\_model}
- •σ is a nonlinearity (ReLU, GELU, SwiGLU variants)
- •d\_ff is often 4× d\_model (e.g., 3072 for 768)

Even though FFN doesn’t mix tokens, it adds substantial capacity: it can reshape and recombine features within each token vector.

### The decoder layer

A decoder layer adds one more attention sublayer:

1) **Masked** multi-head self-attention (causal)

2) Cross-attention over encoder outputs (optional in encoder–decoder)

3) Feed-forward network

Pre-LN decoder (encoder–decoder) sketch:

- •**X₁ = X + MHA(LN(X), LN(X), LN(X); M\_causal)**
- •**X₂ = X₁ + MHA(LN(X₁), K\_enc, V\_enc; M\_enc\_padding)**
- •**Y = X₂ + FFN(LN(X₂))**

If it’s decoder-only (GPT-style), you omit the cross-attention term.

### Why residual connections matter (conceptual)

Residuals let the model learn modifications rather than complete rewrites.

If a sublayer initially does something unhelpful, the residual path preserves the input:

- •**X\_out = X\_in + ε**

This makes gradients flow more directly through many layers. In deep Transformers (dozens to hundreds of layers), residual pathways are essential.

### Why layer normalization is placed around sublayers

Layer norm stabilizes the scale of activations, making training less sensitive to initialization and learning rate.

Layer norm operates per token vector **xᵢ**:

- •μ = (1/d\_model) ∑ₖ xᵢₖ
- •σ² = (1/d\_model) ∑ₖ (xᵢₖ − μ)²
- •LN(**xᵢ**) = γ ⊙ (**xᵢ** − μ)/√(σ² + ϵ) + β

(You already know LN; here it matters because attention logits and FFN activations can drift in magnitude as depth increases.)

### Where positional encoding enters

Positional information is usually added once at the bottom:

- •**X₀ = Emb(tokens) + PosEnc(positions)**

Then all layers operate on X₀, X₁, …, X\_N.

However, there are alternatives (relative position bias, rotary embeddings), but the principle remains: attention needs a way to distinguish positions.

## Application/Connection: How Transformers Are Used (Encoder, Decoder, Training Objectives, and Practical Concerns)

### Encoder-only Transformers (bidirectional)

Use case: classification, retrieval, tagging, masked language modeling.

Mechanics:

- •Full self-attention over the entire sequence (no causal mask).
- •Output is a sequence of contextual embeddings.

To classify, you might pool:

- •use a special [CLS] token representation **y\_cls**
- •or mean-pool: **y\_pool = (1/L) ∑ᵢ yᵢ**

### Decoder-only Transformers (autoregressive)

Use case: text generation, code generation, next-token prediction.

Mechanics:

- •Causal mask enforces that token i can only attend to tokens ≤ i.

Training objective (next-token):

- •Given tokens t₁…t\_L, model predicts t\_{i+1} from context t₁…t\_i.

If logits at position i are **zᵢ** ∈ ℝ^{|Vocab|}, then:

- •p(t\_{i+1} | t\_{≤i}) = softmax(**zᵢ**)

Loss is cross-entropy summed across positions.

### Encoder–decoder Transformers (seq2seq)

Use case: translation, summarization, speech-to-text.

Mechanics:

- •Encoder produces memory **H\_enc**.
- •Decoder uses masked self-attention for partial output and cross-attention to read from **H\_enc**.

### Practical issues that shape real implementations

#### 1) KV caching during decoding

Autoregressive decoding generates one token at a time. Recomputing attention over the whole prefix is expensive. Instead, store previous keys/values.

At time step t:

- •compute K\_t, V\_t for the new token
- •append to cache
- •attend with Q\_t against all cached K\_{≤t}

This reduces per-step cost from O(t²) to roughly O(t) for attention score computation (still linear in context length per step).

#### 2) Attention masks are not optional

If you forget masking:

- •the model may attend to padding and learn spurious correlations
- •a decoder may “cheat” by attending to future tokens during training

Mechanically, masks must be added **before** softmax.

#### 3) Initialization and normalization choices

Deep Transformers are sensitive to:

- •pre-LN vs post-LN
- •residual scaling
- •dropout placement

These details often decide whether training is stable.

#### 4) Why positional encoding is central

Self-attention is permutation-invariant without positional signals:

If you permute tokens, QKᵀ permutes correspondingly, producing the same pattern up to permutation. Positional encoding breaks this symmetry, enabling order-sensitive tasks.

### Connecting the mechanics to behavior

When you inspect trained models, attention heads often develop recognizable patterns:

- •local heads: attend strongly to nearby tokens
- •delimiter heads: attend to separators (commas, periods)
- •induction heads: copy patterns like “A … A”

Not every head is interpretable, and attention weights are not the whole story (FFN and residual streams matter), but the routing intuition remains useful.

### Summary of the full forward pass (encoder-only)

Given tokens → embeddings + positions:

- •**X₀ = Emb(t) + PosEnc(pos)**

For ℓ = 1…N layers:

- •**X\_ℓ = TransformerEncoderLayer(X\_{ℓ−1})**

Final outputs **X\_N** feed task heads (classification, MLM head, etc.).

For decoder-only, the same structure holds, but with causal masking and an output projection to vocabulary logits.

## Worked Examples (3)

### Worked Example 1: Compute single-head scaled dot-product attention by hand (tiny numbers)

We will compute attention for a sequence of L = 2 tokens with d\_k = d\_v = 2. Use no mask. Let

Q = [[1, 0],

[0, 1]]

K = [[1, 0],

[1, 1]]

V = [[1, 2],

[3, 4]]

All matrices are in row-major form: each row corresponds to a token position.

1. Step 1: Compute raw score matrix S = QKᵀ.

   Kᵀ = [[1, 1],

   [0, 1]]

   S = QKᵀ = [[1, 0],

   [0, 1]] [[1, 1],

   [0, 1]]

   = [[1⋅1 + 0⋅0, 1⋅1 + 0⋅1],

   [0⋅1 + 1⋅0, 0⋅1 + 1⋅1]]

   = [[1, 1],

   [0, 1]]
2. Step 2: Scale by √d\_k. Here d\_k = 2, so √d\_k = √2.

   Ŝ = S / √2 = [[1/√2, 1/√2],

   [0/√2, 1/√2]]

   = [[0.7071, 0.7071],

   [0, 0.7071]] (approx)
3. Step 3: Apply softmax row-wise to get attention weights A.

   Row 1: softmax([0.7071, 0.7071]) = [0.5, 0.5]

   Row 2: softmax([0, 0.7071])

   Compute exp values:

   exp(0) = 1

   exp(0.7071) ≈ 2.028

   Sum ≈ 3.028

   So row 2 ≈ [1/3.028, 2.028/3.028] ≈ [0.330, 0.670]

   Thus

   A ≈ [[0.5, 0.5],

   [0.33, 0.67]]
4. Step 4: Compute output O = AV.

   O₁ = 0.5⋅[1,2] + 0.5⋅[3,4] = [2,3]

   O₂ = 0.33⋅[1,2] + 0.67⋅[3,4]

   = [0.33 + 2.01, 0.66 + 2.68]

   = [2.34, 3.34] (approx)

   So

   O ≈ [[2.00, 3.00],

   [2.34, 3.34]]

**Insight:** Each output token becomes a convex combination of value vectors. Token 1 averaged both tokens equally; token 2 leaned more heavily on token 2 because q₂ aligned better with k₂ than k₁.

### Worked Example 2: Shapes and parameterization of multi-head attention (sanity-checking dimensions)

Let d\_model = 8, number of heads h = 2. Then per-head dimension d\_k = d\_v = d\_model / h = 4. Let sequence length L = 3. We will track tensor shapes through MHA self-attention and the output projection.

1. Step 1: Start with input X ∈ ℝ^{L×d\_model} = ℝ^{3×8}.
2. Step 2: Project into per-head Q, K, V.

   For each head r:

   W\_Q^{(r)} ∈ ℝ^{8×4}, W\_K^{(r)} ∈ ℝ^{8×4}, W\_V^{(r)} ∈ ℝ^{8×4}.

   Thus:

   Q^{(r)} = XW\_Q^{(r)} ∈ ℝ^{3×4}

   K^{(r)} = XW\_K^{(r)} ∈ ℝ^{3×4}

   V^{(r)} = XW\_V^{(r)} ∈ ℝ^{3×4}
3. Step 3: Compute attention scores per head.

   For head r:

   S^{(r)} = Q^{(r)} (K^{(r)})ᵀ.

   Shapes: (3×4)(4×3) = 3×3.

   Scaling by √d\_k keeps shape 3×3.

   Softmax row-wise yields A^{(r)} ∈ ℝ^{3×3}.
4. Step 4: Mix values.

   O^{(r)} = A^{(r)} V^{(r)}.

   Shapes: (3×3)(3×4) = 3×4.

   So each head returns 3×4.
5. Step 5: Concatenate heads.

   O\_concat = [O^{(1)} | O^{(2)}] ∈ ℝ^{3×8}.

   Because concatenation along features gives 4 + 4 = 8.
6. Step 6: Output projection.

   W\_O ∈ ℝ^{8×8}.

   Y = O\_concat W\_O ∈ ℝ^{3×8}.

   So MHA maps ℝ^{L×d\_model} → ℝ^{L×d\_model}, enabling residual addition X + Y.

**Insight:** Most Transformer components are designed so inputs and outputs share the same shape (L×d\_model). That single design choice makes deep stacking with residual connections straightforward.

### Worked Example 3: Building a causal mask for a 4-token decoder self-attention

We want a mask M for L = 4 such that position i can attend only to positions j ≤ i. We will express M as 0 for allowed and −∞ for disallowed entries, to be added to logits before softmax.

1. Step 1: Write the allowed pattern.

   Row i shows which columns j are visible.

   i=1: can see [1]

   i=2: can see [1,2]

   i=3: can see [1,2,3]

   i=4: can see [1,2,3,4]
2. Step 2: Create the matrix with −∞ above the diagonal.

   M =

   [[ 0, −∞, −∞, −∞],

   [ 0, 0, −∞, −∞],

   [ 0, 0, 0, −∞],

   [ 0, 0, 0, 0]]
3. Step 3: Use it in attention.

   A = softmax( (QKᵀ)/√d\_k + M )

   Because softmax(exp(−∞)) = 0, all forbidden future positions get exactly zero probability.
4. Step 4: Add padding masking if needed.

   If token 4 were padding, you would also set the entire column j=4 to −∞ (except possibly where you want padding to never be attended at all).

   In practice, frameworks combine causal and padding masks by addition.

**Insight:** Masking is mathematically simple—just add −∞ before softmax—but conceptually essential: it encodes the information constraints that define the task (bidirectional understanding vs left-to-right generation).

## Key Takeaways

- ✓

  Self-attention mixes token information using learnable content-based weights: A = softmax(QKᵀ/√d\_k + M), output O = AV.
- ✓

  Queries, keys, and values are linear projections of token states; they let the model learn what to match (Q/K) and what information to transmit (V).
- ✓

  The √d\_k scaling keeps attention logits in a healthy range so softmax does not saturate as dimension grows.
- ✓

  Multi-head attention runs several attention mechanisms in parallel on different learned subspaces, concatenates their outputs, then applies an output projection back to d\_model.
- ✓

  A Transformer layer is (attention → FFN), each wrapped with residual connections and layer normalization; stacking layers yields powerful hierarchical context building.
- ✓

  Decoder self-attention requires a causal mask so position i cannot attend to any future position j > i; padding masks prevent attending to padding tokens.
- ✓

  Encoder–decoder models add cross-attention where decoder queries attend to encoder keys/values to retrieve source information.
- ✓

  The main computational bottleneck of vanilla self-attention is O(L²) memory/time in sequence length.

## Common Mistakes

- ✗

  Forgetting to add the mask before softmax (or applying it after softmax), which breaks causality or allows attending to padding.
- ✗

  Mixing up tensor shapes: QKᵀ should produce an L×L score matrix; dimension mismatches often come from incorrect transposes or head reshaping.
- ✗

  Omitting the √d\_k scaling, causing attention logits to grow with dimension and making training unstable due to softmax saturation.
- ✗

  Assuming attention weights alone “explain” model behavior; the residual stream and FFN can carry and transform information even when attention looks diffuse.

## Practice

easy

Given L = 3 and d\_k = 1, suppose Q = [[2],[0],[1]], K = [[1],[3],[−1]], V = [[10],[20],[30]]. Compute S = QKᵀ, then A = softmax(S) row-wise (no scaling needed because √d\_k = 1), then O = AV.

**Hint:** Sᵢⱼ = qᵢ kⱼ. Compute each row’s softmax separately. Keep results as exact exponentials if you prefer: softmax([a,b,c]) = [eᵃ, eᵇ, eᶜ]/(eᵃ+eᵇ+eᶜ).

Show solution

S = QKᵀ gives a 3×3 matrix.

Row 1 (q₁=2): [2⋅1, 2⋅3, 2⋅(−1)] = [2, 6, −2]

Row 2 (q₂=0): [0, 0, 0]

Row 3 (q₃=1): [1, 3, −1]

So S = [[2,6,−2],[0,0,0],[1,3,−1]].

A row-wise:

Row 1: softmax([2,6,−2]) = [e², e⁶, e^{−2}] / (e² + e⁶ + e^{−2}).

Row 2: softmax([0,0,0]) = [1/3,1/3,1/3].

Row 3: softmax([1,3,−1]) = [e¹, e³, e^{−1}] / (e¹ + e³ + e^{−1}).

O = AV where V = [10,20,30]ᵀ applied as weighted sum per row:

O₁ = 10A₁₁ + 20A₁₂ + 30A₁₃

O₂ = (10+20+30)/3 = 20

O₃ = 10A₃₁ + 20A₃₂ + 30A₃₃

medium

You have a Transformer with d\_model = 1024 and h = 16 heads. (a) What is d\_k if you split evenly? (b) What are the shapes of W\_Q, W\_K, W\_V per head? (c) What is the shape of the attention score matrix for a sequence length L = 128 in a single head?

**Hint:** Use d\_k = d\_model / h. Remember score matrix is QKᵀ with Q ∈ ℝ^{L×d\_k} and K ∈ ℝ^{L×d\_k}.

Show solution

(a) d\_k = 1024 / 16 = 64.

(b) Per head, W\_Q^{(r)} ∈ ℝ^{1024×64}, W\_K^{(r)} ∈ ℝ^{1024×64}, W\_V^{(r)} ∈ ℝ^{1024×64} (assuming d\_v = d\_k).

(c) For L = 128, Q and K are 128×64, so QKᵀ is (128×64)(64×128) = 128×128.

hard

Consider a decoder-only Transformer generating tokens left-to-right. Explain, using the attention formula, exactly where and how the causal mask changes the computation. Then describe what failure mode occurs if you omit the causal mask during training but keep it during inference.

**Hint:** Point to the logits matrix QKᵀ/√d\_k and the additive mask M. Think about the model seeing future tokens during teacher forcing training.

Show solution

Causal masking modifies attention logits before softmax:

A = softmax( QKᵀ/√d\_k + M\_causal ).

M\_causal has entries Mᵢⱼ = −∞ for j > i and 0 otherwise, forcing Aᵢⱼ = 0 for all future positions.

If you omit M\_causal during training with teacher forcing, the model can attend to future ground-truth tokens to predict the next token. It learns a “cheating” solution that relies on information that will not be available at inference.

At inference, when you reintroduce the causal mask, those information paths disappear, causing a sharp performance drop: perplexity increases and generation quality degrades because the model’s learned dependencies are misaligned with the constraints at test time.

## Connections

[Attention Mechanisms](/tech-tree/attention-mechanisms/)

[Positional Encoding](/tech-tree/positional-encoding/)

[Layer Normalization](/tech-tree/layer-normalization/)

[Residual (Skip) Connections](/tech-tree/residual-connections/)

[Sequence Masking (causal and padding masks)](/tech-tree/sequence-masking/)

[Softmax and Logits](/tech-tree/softmax-logits/)

[Token Embeddings](/tech-tree/token-embeddings/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
