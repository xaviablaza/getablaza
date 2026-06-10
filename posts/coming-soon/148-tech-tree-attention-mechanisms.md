---
title: Attention Mechanisms
description: Weighted focus on input elements. Self-attention, cross-attention.
date: '2026-07-01'
scheduled: '2026-11-25'
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
inspiration_url: https://templeton.host/tech-tree/attention-mechanisms/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/attention-mechanisms/](https://templeton.host/tech-tree/attention-mechanisms/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Attention Mechanisms

Machine LearningDifficulty: ★★★★★Depth: 13Unlocks: 1

Weighted focus on input elements. Self-attention, cross-attention.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Similarity scoring: compute similarity scores between a query and each key (pairwise relevance measure).
- -Score-to-weight and aggregate: convert raw scores into a probability distribution (typically softmax) and use those weights to form a weighted sum of the corresponding value vectors.
- -Source origin distinction: self-attention uses Q,K,V from the same source; cross-attention uses Q from one source and K,V from another.

## Key Symbols & Notation

Q, K, V (query, key, value matrices or vectors)

## Essential Relationships

- -Attention weights = softmax(similarity(Q, K)) (optionally with a scaling factor).
- -Attention output = attention weights multiplied with V (weighted sum of values per query).

## Prerequisites (8)

[Deep Learning6 atoms](/tech-tree/deep-learning/)[Matrix Calculus6 atoms](/tech-tree/matrix-calculus/)[Softmax Function6 atoms](/tech-tree/softmax-function/)[Cosine Similarity6 atoms](/tech-tree/cosine-similarity/)[Vector Embeddings5 atoms](/tech-tree/vector-embeddings/)[Sequence-to-Sequence Modeling5 atoms](/tech-tree/sequence-to-sequence-modeling/)[Affine Transformations (Linear Layers)5 atoms](/tech-tree/affine-transformations/)[Embeddings (Dense Representations)6 atoms](/tech-tree/embeddings-dense-representations/)

## Unlocks (1)

[Transformerslvl 5](/tech-tree/transformers/)

Advanced Learning Details

### Graph Position

248

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

13

Chain Length

### Cognitive Load

6

Atomic Elements

41

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (16)

- - Query/Key/Value (Q/K/V) abstraction: distinct projected vectors where Query seeks relevant Keys and Values carry the content to be aggregated
- - Raw attention scores: pairwise compatibility measures between a Query and each Key (e.g., unnormalized dot products)
- - Scaled dot‑product attention: dividing dot products by sqrt(d\_k) before normalization to stabilize magnitudes
- - Attention weights as a distribution over keys for each query (application of softmax across keys for each query)
- - Context vector (attention output): the weighted sum of Value vectors using the attention weights for a given Query
- - Self‑attention: Q, K, V all derived from the same sequence so each position attends to other positions in that same sequence
- - Cross‑attention: Queries come from one source (e.g., decoder) while Keys and Values come from another (e.g., encoder), enabling information flow between sequences
- - Attention matrix: the n×n (or n\_query×n\_key) matrix of attention weights / scores representing pairwise interactions across positions
- - Masking in attention: techniques (causal masks, padding masks) that block certain key positions by altering scores before normalization
- - Multi‑head attention: running several parallel attention mechanisms (heads) in different learned subspaces and then combining their outputs
- - Head specialization: each attention head can learn to focus on different syntactic/semantic relations or subspaces
- - Positional encoding necessity: attention is content‑based and permutation‑equivariant, so explicit positional encodings are required to inject order information
- - Computational and memory scaling of attention: attention requires forming pairwise interactions leading to O(n^2) time/memory in sequence length n
- - Differentiable content‑based addressing: attention acts as a soft, differentiable read operation over a set of memory/value vectors
- - Hard vs soft attention distinction: soft attention is differentiable (probabilistic weighting), whereas hard/stochastic attention makes discrete choices and breaks end‑to‑end differentiability
- - Alternative scoring functions: besides dot‑product, attention can use additive (Bahdanau) or other compatibility functions (each has different tradeoffs)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

You’re building a machine translation system. The input is: “The animal didn’t cross the road because it was tired.” When generating “it”, the model must decide: does “it” refer to “animal” or “road”? In classic seq2seq, that decision is buried in a single hidden state bottleneck. Attention fixes this by letting the decoder *look back* and place a weighted focus over the relevant input tokens.

Now a curiosity gap: attention layers can fail in surprisingly silent ways. Two common ones: (1) applying softmax along the wrong axis (your model still trains, but attends across the batch or feature dimension), and (2) mask leakage (future tokens “peek” through due to broadcasting or dtype mistakes). This lesson makes the mechanism precise enough that you can derive the shapes, verify the axes, and catch these bugs quickly.

TL;DR:

Attention computes relevance between a query and many keys, converts relevance scores into weights (softmax), and uses those weights to blend the corresponding value vectors. Self-attention uses Q,K,V from the same sequence; cross-attention uses queries from one sequence (e.g., decoder) and keys/values from another (e.g., encoder). The core formula is: Attention(Q,K,V) = softmax(QKᵀ/√dₖ)V, with masking and batching details crucial in practice.

## What Is Attention Mechanisms?

### Why attention exists (the bottleneck story)

In sequence-to-sequence modeling, we often want an output sequence to depend on *different* parts of the input at *different* times. Translation, summarization, speech recognition, program synthesis—these tasks all have alignment structure:

- •When translating a noun, you want to focus on the source noun phrase.
- •When translating a verb, you might need to look at a different region.
- •When resolving a pronoun (“it”, “they”), you need to find an antecedent that could be far away.

Older encoder–decoder RNNs forced the entire input sequence into one fixed-size vector (or a narrow channel through the final hidden state). This creates an information bottleneck: long sequences degrade because the decoder can’t selectively retrieve what it needs.

Attention removes the bottleneck by turning “memory” into a set of vectors (one per input element) and letting the model compute a *weighted combination* of those vectors each time it needs context.

### The three roles: Query, Key, Value

Attention is easiest to understand by analogy to retrieval:

- •A **query** (Q) encodes what you’re currently looking for.
- •A set of **keys** (K) encodes what each memory item is “about.”
- •A set of **values** (V) encodes the information you will actually retrieve.

The algorithm:

1. 1)Score how similar each key is to the query (relevance).
2. 2)Convert scores into a probability distribution (weights).
3. 3)Use weights to compute a weighted sum of values.

This is not just a metaphor; it’s literally what the math does.

### A minimal single-query definition

Suppose we have one query vector **q** ∈ ℝᵈ, and n keys/values {(**kᵢ**, **vᵢ**)} for i=1..n.

1) Similarity scoring (dot-product attention):

si=q⊤kis\_i = \mathbf{q}^\top \mathbf{k}\_isi​=q⊤ki​

2) Score-to-weight via softmax:

αi=exp⁡(si)∑j=1nexp⁡(sj)\alpha\_i = \frac{\exp(s\_i)}{\sum\_{j=1}^n \exp(s\_j)}αi​=∑j=1n​exp(sj​)exp(si​)​

3) Aggregate values:

o=∑i=1nαi vi\mathbf{o} = \sum\_{i=1}^n \alpha\_i \, \mathbf{v}\_io=i=1∑n​αi​vi​

Here **o** is the attention output (sometimes called the “context vector”).

### Why Q, K, V are usually learned projections

In neural networks, the input tokens already have embeddings **xᵢ**. We *project* them into Q/K/V spaces with learned affine transformations:

- •**q** = **W\_Q** **x**
- •**k** = **W\_K** **x**
- •**v** = **W\_V** **x**

This matters because:

- •the model can learn what “matching” should mean (via **W\_Q**, **W\_K**), and
- •the model can learn what to retrieve (via **W\_V**) even if that differs from what helps matching.

### Self-attention vs cross-attention (source origin distinction)

This node emphasizes a crucial distinction:

- •**Self-attention**: Q, K, V come from the *same* sequence (same source). Each token can attend to other tokens in its own sequence.
- •**Cross-attention**: Q comes from one source (e.g., decoder states), while K and V come from another (e.g., encoder outputs). The decoder queries the encoder memory.

In translation terms:

- •self-attention inside the encoder mixes information among source tokens,
- •self-attention inside the decoder mixes information among generated tokens (with causal masking),
- •cross-attention lets the decoder pull in source information.

### Preview: the axis and mask pitfalls

Attention is easy to write but easy to implement incorrectly.

- •**Softmax axis mistake**: weights must sum to 1 *over keys for each query*. If you normalize over the wrong axis, the layer still outputs something, gradients still flow, but the meaning of “attention” is broken.
- •**Mask leakage**: masks must align with the score matrix shape. Broadcasting mistakes can allow forbidden positions (future tokens or padding) to influence outputs.

We’ll keep returning to shapes and axes so you can debug these confidently.

## Core Mechanic 1: Similarity Scoring (Q·Kᵀ and why scaling matters)

### Why scoring is the heart of attention

If attention is “weighted focus,” then the score function decides *what counts as relevant*. The score is computed between a query and each key.

In practice, the most common scoring rule is **dot-product** similarity because it is fast on GPUs and works well with learned projections.

### From one query to many queries: matrix form

Assume we have:

- •Q ∈ ℝ^(m×dₖ): m queries, each dₖ-dimensional
- •K ∈ ℝ^(n×dₖ): n keys, each dₖ-dimensional
- •V ∈ ℝ^(n×dᵥ): n values, each dᵥ-dimensional

Compute all pairwise query–key scores:

S=QK⊤S = QK^\topS=QK⊤

Shapes:

- •Q is (m×dₖ)
- •Kᵀ is (dₖ×n)
- •S is (m×n)

Interpretation:

- •S\_{ij} is the score between query i and key j.

This “score matrix” is the object you will mask, normalize, and use to weight V.

### Why the scaling factor 1/√dₖ exists

In Transformers, the standard formula is **scaled dot-product attention**:

S=QK⊤dkS = \frac{QK^\top}{\sqrt{d\_k}}S=dk​​QK⊤​

Motivation: dot products grow in magnitude with dimension.

A rough variance argument:

- •Suppose components of **q** and **k** are independent with mean 0 and variance 1.
- •Then **q**ᵀ**k** = ∑\_{t=1}^{dₖ} q\_t k\_t.
- •Each term q\_t k\_t has mean 0, and (under independence) variance ≈ 1.
- •The sum has variance ≈ dₖ.

So typical score magnitudes scale like √dₖ. Large magnitudes push softmax into saturation:

- •one position gets probability ≈ 1
- •others ≈ 0
- •gradients become small for most keys

Dividing by √dₖ keeps the score distribution more stable as dₖ changes.

### Alternative similarity scoring functions

Dot product is not the only option. Historically, early attention used additive scoring.

| Scoring type | Formula (single pair) | Pros | Cons |
| --- | --- | --- | --- |
| Dot-product | s = **q**ᵀ**k** | Fast, simple, GPU-friendly | Can grow with dₖ (needs scaling) |
| Cosine similarity | s = (**q**ᵀ**k**) / ( |  | **q** |  | · |  | **k** |  | ) | Scale-invariant, interpretable | Norm computation adds cost; less common in Transformers |
| Additive (Bahdanau) | s = **w**ᵀ tanh(**W\_q q** + **W\_k k**) | Flexible, can work well with smaller dims | Slower; less parallel-friendly |

Because you already know cosine similarity: note that dot-product attention can *learn* to behave like cosine similarity if the model learns to normalize representations (or learns norm control via layer norm / projection matrices). But in standard Transformers, the scaling is the main explicit normalization.

### Shape discipline (the first line of defense against bugs)

When implementing scoring, always write down:

- •batch size: B
- •number of queries: m (often sequence length L\_q)
- •number of keys: n (often L\_k)
- •feature dimension: dₖ

In a batched setting:

- •Q: (B×m×dₖ)
- •K: (B×n×dₖ)
- •scores S = QKᵀ: (B×m×n)

A common silent bug: transposing the wrong axes so you compute (B×dₖ×dₖ) or normalize over the wrong dimension.

### Causal structure and “who can look at whom”

The score matrix S encodes potential connections:

- •In **encoder self-attention**, typically every token can attend to every token (except padding).
- •In **decoder self-attention**, we must enforce causality: token t cannot attend to tokens > t.

This is done not at the Q/K/V level but by masking the score matrix before softmax.

We’ll treat masking carefully in the next mechanic because it interacts directly with the probability distribution.

## Core Mechanic 2: Score-to-Weight (Softmax), Masking, and Weighted Aggregation

### Why we need a distribution, not raw scores

Raw scores S\_{ij} are unbounded real numbers. To create a “focus,” we need nonnegative weights that sum to 1 across keys for each query.

Softmax does exactly this, turning each query’s score row into a categorical distribution over keys.

### The core formula (matrix form)

Given scores:

S=QK⊤dk∈Rm×nS = \frac{QK^\top}{\sqrt{d\_k}} \quad\in \mathbb{R}^{m\times n}S=dk​​QK⊤​∈Rm×n

Compute attention weights:

A=softmax⁡(S)A = \operatorname{softmax}(S)A=softmax(S)

Important: softmax is applied **row-wise** over the key dimension (size n). That means:

Aij=exp⁡(Sij)∑t=1nexp⁡(Sit)A\_{ij} = \frac{\exp(S\_{ij})}{\sum\_{t=1}^{n} \exp(S\_{it})}Aij​=∑t=1n​exp(Sit​)exp(Sij​)​

Then aggregate values:

O=AVO = AVO=AV

Shapes:

- •A is (m×n)
- •V is (n×dᵥ)
- •O is (m×dᵥ)

Interpretation:

- •output for each query i is a convex combination of the value vectors.

### Masking: forbidding attention to certain positions

Masking modifies S before softmax so forbidden positions get probability ≈ 0.

Two common masks:

1) **Padding mask** (ignore pad tokens)

- •If some keys correspond to padding positions, we must prevent attending to them.

2) **Causal mask** (prevent “future” access in autoregressive decoding)

- •For query position i, keys j > i should be forbidden.

Mechanically, we add a large negative number to masked scores:

S′=S+MS' = S + MS′=S+M

Where M\_{ij} = 0 if allowed, and M\_{ij} = -\infty (or a large negative constant like -10^9) if disallowed.

Then:

A=softmax⁡(S′)A = \operatorname{softmax}(S')A=softmax(S′)

Because exp(-∞) → 0, masked entries get weight 0.

### The surprising failure mode: mask leakage via broadcasting

Masks are often stored with shape (B×1×1×n) or (B×1×m×n) depending on implementation (especially with multi-head attention).

A common bug pattern:

- •scores S has shape (B×h×m×n)
- •mask has shape (B×m×n)
- •you add them and broadcasting *might* align incorrectly

Result: you mask the wrong dimension or the wrong positions. The model may still train but exhibits “cheating” (decoder sees future) or ignores padding improperly.

Practical discipline:

- •assert shapes explicitly
- •test that masked attention weights at forbidden positions are ~0
- •test with tiny sequences where you can print A

### Softmax axis mistake (the other silent bug)

Given S of shape (B×m×n):

- •correct: softmax over n (keys) so each row sums to 1
- •wrong: softmax over m (queries) or over d (features)

If you accidentally normalize over queries, you enforce that *each key distributes probability over queries*, which is not the retrieval interpretation.

A quick invariant check:

- •For correct attention: for each query i, ∑\_{j=1}^n A\_{ij} = 1.

### Numerical stability: subtract max

Softmax can overflow if scores are large. The standard stable computation:

For each row i:

Aij=exp⁡(Sij−max⁡tSit)∑t=1nexp⁡(Sit−max⁡uSiu)A\_{ij} = \frac{\exp(S\_{ij} - \max\_t S\_{it})}{\sum\_{t=1}^{n} \exp(S\_{it} - \max\_u S\_{iu})}Aij​=∑t=1n​exp(Sit​−maxu​Siu​)exp(Sij​−maxt​Sit​)​

This doesn’t change results because subtracting a constant from all logits preserves softmax.

### Temperature and sharpness

Sometimes you’ll see a temperature τ:

A=softmax⁡(S/τ)A = \operatorname{softmax}(S/\tau)A=softmax(S/τ)

- •τ < 1 makes distributions sharper (more peaky)
- •τ > 1 makes them softer (more uniform)

The Transformer’s √dₖ scaling can be interpreted as a kind of dimension-dependent temperature.

### Weighted sum as linear algebra (and why it’s differentiable)

Once you have A, the output is:

O=AVO = AVO=AV

This is a linear combination of V with coefficients from A.

Differentiability:

- •Softmax is differentiable
- •Matrix multiply is differentiable
- •So the whole attention block is end-to-end trainable

To see the dependency explicitly for a single query i:

oi=∑j=1nAij vj\mathbf{o}\_i = \sum\_{j=1}^n A\_{ij}\, \mathbf{v}\_joi​=j=1∑n​Aij​vj​

If A\_{ij} increases, **oᵢ** moves toward **vⱼ**.

### A useful mental model: attention is “content-addressable memory”

Keys provide an address space, queries pick addresses, values store content. The softmax makes it a soft (continuous) lookup rather than a hard index.

This is why attention can represent alignment: it’s literally learning a soft alignment matrix A.

At this point, you have the atomic concepts:

- •similarity scoring (Q vs K)
- •score → weights via softmax
- •weighted sum of V

Next we connect that to the self vs cross distinction in full architectural context.

## Application/Connection: Self-Attention vs Cross-Attention (and how this becomes Transformers)

### Why the “origin of Q,K,V” matters

Attention is a general operator: it maps (Q,K,V) to O. The difference between self- and cross-attention is simply *where these tensors come from*.

This origin choice encodes a modeling decision:

- •Do we want interactions *within* a sequence? (self)
- •Or do we want one sequence to retrieve from another? (cross)

### Self-attention: mixing information inside one sequence

Let X ∈ ℝ^(L×d\_model) be a sequence of L token embeddings (after adding positional information).

We compute:

Q=XWQ,K=XWK,V=XWVQ = XW\_Q, \quad K = XW\_K, \quad V = XW\_VQ=XWQ​,K=XWK​,V=XWV​

Where:

- •W\_Q ∈ ℝ^(d\_model×dₖ)
- •W\_K ∈ ℝ^(d\_model×dₖ)
- •W\_V ∈ ℝ^(d\_model×dᵥ)

Then:

SelfAttn⁡(X)=softmax⁡(QK⊤dk+M)V\operatorname{SelfAttn}(X) = \operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d\_k}} + M\right)VSelfAttn(X)=softmax(dk​​QK⊤​+M)V

Mask M depends on the setting:

- •encoder: padding mask only
- •decoder: padding mask + causal mask

Interpretation: each token representation is updated by blending information from other tokens.

A key property: self-attention can connect tokens at arbitrary distance in one step (unlike RNNs where information must travel sequentially).

### Cross-attention: querying one sequence with another

In an encoder–decoder setup:

- •Encoder outputs memory H ∈ ℝ^(L\_src×d\_model)
- •Decoder has states/representations Y ∈ ℝ^(L\_tgt×d\_model)

Cross-attention uses:

Q=YWQ,K=HWK,V=HWVQ = YW\_Q, \quad K = HW\_K, \quad V = HW\_VQ=YWQ​,K=HWK​,V=HWV​

So each decoder position forms a query based on what it has generated so far, and retrieves relevant source information.

Shape intuition:

- •Q: (L\_tgt×dₖ)
- •K,V: (L\_src×dₖ) and (L\_src×dᵥ)
- •scores: (L\_tgt×L\_src)

This matrix is literally an alignment between target positions and source positions.

### Where multi-head attention fits (high-level, because Transformers unlock next)

This node unlocks Transformers, where attention is typically *multi-head*.

Multi-head attention repeats the attention computation h times with different learned projections:

For head r:

- •Q\_r = XW\_Q^(r)
- •K\_r = XW\_K^(r)
- •V\_r = XW\_V^(r)

Each head produces O\_r, then we concatenate and project:

O=Concat⁡(O1,…,Oh)WOO = \operatorname{Concat}(O\_1, \dots, O\_h) W\_OO=Concat(O1​,…,Oh​)WO​

Why multiple heads helps:

- •different heads can specialize (syntax, coreference, local context, long-range dependency)
- •it increases representational capacity without exploding per-head dimension

But the *atomic mechanism* remains exactly what you learned: score, softmax, weighted sum.

### Deriving the batched, multi-head shapes (to prevent axis errors)

Let:

- •B = batch size
- •L\_q = query length
- •L\_k = key length
- •h = number of heads
- •dₖ = per-head key dimension
- •dᵥ = per-head value dimension

Typical shapes:

- •Q: (B×h×L\_q×dₖ)
- •K: (B×h×L\_k×dₖ)
- •V: (B×h×L\_k×dᵥ)

Scores:

S=QK⊤dk⇒(B×h×Lq×Lk)S = \frac{QK^\top}{\sqrt{d\_k}} \quad \Rightarrow \quad (B\times h\times L\_q\times L\_k)S=dk​​QK⊤​⇒(B×h×Lq​×Lk​)

Softmax over L\_k:

- •for each (B, head, query position), weights over keys sum to 1

Output:

- •O: (B×h×L\_q×dᵥ)

This is where the earlier failure modes live:

- •wrong transpose can swap L\_q and dₖ
- •softmax axis must be L\_k
- •mask must broadcast to (B×h×L\_q×L\_k)

### A concrete debugging checklist (practical connection)

When attention behaves oddly, check invariants:

1) **Row sum invariant** (per query):

- •For unmasked keys: ∑ weights = 1

2) **Mask invariant**:

- •masked positions have weights ≈ 0

3) **Causality invariant** (decoder self-attention):

- •for any query position t, weights on keys > t are ≈ 0

4) **Sanity input test**:

- •if all keys are identical, attention weights should become uniform (modulo mask)
- •if one key is much closer to the query, attention should be peaked there

### How attention connects to the next node (Transformers)

Transformers stack attention layers with:

- •residual connections
- •layer normalization
- •position-wise feed-forward networks
- •positional encodings (to inject order)

But none of those change what attention *is*. They make it trainable, stable, and expressive at scale.

If you can derive the score matrix shape and explain why softmax is row-wise, you’re ready to understand multi-head attention, positional encoding, and full Transformer blocks.

## Worked Examples (3)

### Worked Example 1: Compute attention weights and output by hand (single query)

We have 1 query and 3 key/value pairs. Use unscaled dot-product attention for simplicity.

Let **q** = [1, 0].

Keys:

- •**k₁** = [1, 0]
- •**k₂** = [0, 1]
- •**k₃** = [1, 1]

Values:

- •**v₁** = [10, 0]
- •**v₂** = [0, 10]
- •**v₃** = [5, 5]

Compute scores sᵢ = **q**ᵀ**kᵢ**, weights α via softmax, and output **o** = ∑ αᵢ **vᵢ**.

1. Step 1: Compute dot-product scores

   s₁ = [1,0]·[1,0] = 1

   s₂ = [1,0]·[0,1] = 0

   s₃ = [1,0]·[1,1] = 1
2. Step 2: Softmax normalization

   Compute exp scores:

   exp(s₁)=e¹,

   exp(s₂)=e⁰=1,

   exp(s₃)=e¹

   Sum = e + 1 + e = 2e + 1

   So:

   α₁ = e/(2e+1)

   α₂ = 1/(2e+1)

   α₃ = e/(2e+1)
3. Step 3: Weighted sum of values

   **o** = α₁**v₁** + α₂**v₂** + α₃**v₃**

   = α₁[10,0] + α₂[0,10] + α₃[5,5]

   First component:

   o₁ = 10α₁ + 0α₂ + 5α₃ = 10α₁ + 5α₃

   Second component:

   o₂ = 0α₁ + 10α₂ + 5α₃ = 10α₂ + 5α₃
4. Step 4: Substitute α values

   Because α₁ = α₃ = e/(2e+1):

   o₁ = 10·e/(2e+1) + 5·e/(2e+1) = 15e/(2e+1)

   o₂ = 10·1/(2e+1) + 5·e/(2e+1) = (10 + 5e)/(2e+1)

**Insight:** Even though k₁ and k₃ tie on relevance, the output is not just “pick one”: it blends v₁ and v₃ heavily, with a smaller contribution from v₂. Attention is a soft retrieval mechanism; ties and near-ties naturally produce mixtures.

### Worked Example 2: Self-attention vs cross-attention shapes (and where softmax must apply)

You have an encoder–decoder model.

Encoder sequence length L\_src = 4, decoder length L\_tgt = 3.

Model dimension d\_model = 8.

Single-head attention with dₖ = dᵥ = 8.

Batch size B = 2.

Encoder outputs H have shape (B×L\_src×d\_model) = (2×4×8).

Decoder representations Y have shape (B×L\_tgt×d\_model) = (2×3×8).

Construct Q,K,V and determine the score matrix shape for:

1) encoder self-attention

2) decoder self-attention

3) decoder cross-attention

1. Part A: Encoder self-attention

   Q = HW\_Q, K = HW\_K, V = HW\_V

   So Q,K,V each have shape (2×4×8).

   Scores S = QKᵀ:

   - •Q is (2×4×8)
   - •Kᵀ (over last two dims) is (2×8×4)

   So S is (2×4×4).

   Softmax must be over the last dimension (keys), so over size 4.
2. Part B: Decoder self-attention

   Q,K,V come from Y, so each is (2×3×8).

   Scores S is (2×3×3).

   Softmax over the last dimension (keys) so each of 3 query positions has a distribution over 3 key positions.

   Additionally, apply a causal mask so query position t cannot attend to keys > t.
3. Part C: Decoder cross-attention

   Q comes from Y: Q is (2×3×8).

   K,V come from H: K,V are (2×4×8).

   Scores S = QKᵀ gives shape (2×3×4).

   Softmax must be over the last dimension (keys), so over size 4 (the source positions).

   Padding mask applies to the encoder keys (length 4), not to decoder positions.

**Insight:** The single biggest implementation detail is: softmax normalizes across keys for each query. In cross-attention the key axis is L\_src, not L\_tgt. If you normalize over the wrong length, the model no longer expresses “which source tokens explain this target token?”

### Worked Example 3: Causal masking prevents future leakage (tiny matrix demonstration)

Consider decoder self-attention with L = 3 tokens. We want token 1 (0-indexed) to attend only to keys 0..1.

Suppose scaled scores (already divided by √dₖ) for a single head and single batch item are:

S =

[ [2, 1, 0],

[0, 3, 4],

[1, 1, 1] ]

Apply a causal mask and compute the masked softmax weights for row 1 (the second query).

1. Step 1: Write the causal mask M (0 allowed, -∞ forbidden)

   For L=3:

   M =

   [ [0, -∞, -∞],

   [0, 0, -∞],

   [0, 0, 0] ]
2. Step 2: Mask the scores S' = S + M

   Row 1 (second query) originally: [0, 3, 4]

   After masking (disallow key 2): [0, 3, -∞]
3. Step 3: Softmax row 1 stably

   Compute max = 3

   Subtract max: [0-3, 3-3, -∞] = [-3, 0, -∞]

   Exponentiate: [e^-3, 1, 0]

   Normalize: sum = e^-3 + 1

   So weights are:

   A = [ e^-3/(1+e^-3), 1/(1+e^-3), 0 ]

**Insight:** Without the mask, key 2 would dominate because score 4 is largest. With the mask, its probability is forced to 0. This illustrates why mask correctness is a security property for autoregressive models: a single broadcasting error can re-enable that last entry.

## Key Takeaways

- ✓

  Attention is a differentiable retrieval operation: similarity scoring (Q vs K) → softmax weights → weighted sum of V.
- ✓

  In matrix form: $Attention⁡(Q,K,V)=softmax⁡(QK⊤/dk+M)V\operatorname{Attention}(Q,K,V)=\operatorname{softmax}(QK^\top/\sqrt{d\_k}+M)VAttention(Q,K,V)=softmax(QK⊤/dk​​+M)V$, where softmax is applied over the key dimension.
- ✓

  Self-attention uses Q,K,V from the same source sequence; cross-attention uses Q from one source and K,V from another (e.g., decoder queries encoder memory).
- ✓

  The √dₖ scaling prevents dot-product magnitudes from growing with dimension, keeping softmax from saturating and stabilizing gradients.
- ✓

  Masking is done by adding 0 for allowed positions and −∞ (or a large negative) for forbidden positions before softmax.
- ✓

  Two silent implementation failures are common: softmax along the wrong axis (weights don’t sum over keys) and mask leakage via shape/broadcasting mistakes.
- ✓

  Attention weight matrices can be interpreted as soft alignment matrices (especially in cross-attention), connecting directly to seq2seq alignment intuition.

## Common Mistakes

- ✗

  Applying softmax over the wrong dimension (e.g., over queries instead of keys), which breaks the “distribution over keys per query” interpretation while still producing finite outputs.
- ✗

  Mask shape/broadcasting errors that allow attention to forbidden positions (future tokens or padding), causing leakage that may only show up as suspiciously good training loss.
- ✗

  Forgetting the 1/√dₖ scaling (or mis-scaling), leading to overly peaky softmax and poor gradient flow, especially for larger dₖ.
- ✗

  Mixing up K and V: keys are for matching, values are for retrieval; swapping them can reduce performance or destabilize learning.

## Practice

easy

You have Q ∈ ℝ^(5×16), K ∈ ℝ^(7×16), V ∈ ℝ^(7×32). What are the shapes of the score matrix S, attention weights A, and output O (single head, no batch)? Also: along which axis do you apply softmax?

**Hint:** Compute S = QKᵀ and track dimensions; softmax should normalize over keys for each query.

Show solution

S = QKᵀ has shape (5×7). A = softmax(S) has shape (5×7), with softmax applied over the last dimension of size 7 (the keys) for each of the 5 queries. O = AV has shape (5×32).

medium

Consider a decoder self-attention layer with sequence length L=4. Write the causal mask matrix M (entries 0 or −∞) that prevents attending to future tokens. Which entries are allowed for query position 2 (0-indexed)?

**Hint:** Allowed positions are keys with index ≤ query index.

Show solution

For L=4,

M =

[ [0, −∞, −∞, −∞],

[0, 0, −∞, −∞],

[0, 0, 0, −∞],

[0, 0, 0, 0] ]

For query position 2, allowed keys are {0,1,2}; key 3 is forbidden.

hard

In cross-attention, a decoder has L\_tgt=6 and an encoder has L\_src=10. You compute scores S of shape (B×h×6×10). Suppose you accidentally apply softmax over the length-6 axis instead of length-10. Conceptually, what distribution are you computing, and why is it wrong for retrieval?

**Hint:** Ask: for a fixed query, do weights sum across keys? Or across queries?

Show solution

Softmax over the length-6 axis normalizes across queries (target positions) for each fixed key, producing a distribution like “how much does this source position contribute across different target queries,” rather than “which source positions are relevant for this target query.” Retrieval requires, for each query position, a distribution over keys (length 10). With the wrong axis, each query no longer forms a proper mixture over encoder values, so the mechanism can’t represent alignment from each target token to source tokens.

## Connections

Unlocks and extensions:

- •[Transformers](/tech-tree/transformers/): stacks of self-attention + cross-attention with multi-head structure, residuals, layer norm, and positional encodings.

Related prerequisites and reinforcing nodes:

- •[Softmax Function](/tech-tree/softmax-function/)
- •[Vector Embeddings](/tech-tree/vector-embeddings/)
- •[Sequence-to-Sequence Modeling](/tech-tree/sequence-to-sequence-modeling/)
- •[Affine Transformations (Linear Layers)](/tech-tree/affine-transformations/)
- •[Cosine Similarity](/tech-tree/cosine-similarity/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
