---
title: Sequence Masking (causal and padding masks)
description: Techniques for masking positions in sequence models to prevent attention to padded elements or future tokens (causal masking) during autoregressive generation; includes mask construction and integration with attention score computation. Masks are crucial for correct training and inference in Transformers.
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
permalink: /tech-tree/sequence-masking/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Sequence Masking (causal and padding masks)

Machine LearningDifficulty: ★★★★☆Depth: 1Unlocks: 1

Techniques for masking positions in sequence models to prevent attention to padded elements or future tokens (causal masking) during autoregressive generation; includes mask construction and integration with attention score computation. Masks are crucial for correct training and inference in Transformers.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Attention mask: a binary matrix indicating, for each query position, which key positions may be attended to (1 = allow, 0 = block).
- -Mask types: causal masking (blocks future tokens for autoregressive decoding) and padding masking (blocks padded/invalid tokens so they do not contribute).

## Key Symbols & Notation

M: binary mask matrix of shape (num\_queries, num\_keys) with entries 1 (allow) or 0 (block).

## Essential Relationships

- -Mask integration: apply the mask by adding a large negative value (e.g., negative infinity) to logits where M=0, then apply softmax so masked positions get (near) zero attention weight.
- -Causal and padding patterns: causal masks follow a triangular rule (for query index i, keys j>i are masked); padding masks mark specific key positions and are broadcast across all queries so padded keys receive no attention.

## Prerequisites (4)

[Softmax Function6 atoms](/tech-tree/softmax-function/)[Softmax and Logits5 atoms](/tech-tree/softmax-and-logits/)[Affine Transformations (Linear Layers)5 atoms](/tech-tree/affine-transformations/)[Token Embeddings6 atoms](/tech-tree/token-embeddings/)

## Unlocks (1)

[Transformerslvl 5](/tech-tree/transformers/)

Advanced Learning Details

### Graph Position

27

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

1

Chain Length

### Cognitive Load

5

Atomic Elements

31

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (14)

- - Padding mask: a per-token binary/boolean mask marking padded (non-data) positions so the model ignores them in attention
- - Causal (autoregressive) mask: a lower-triangular mask that prevents each position i from attending to positions j > i (future tokens)
- - Mask construction types: boolean masks, float/additive masks (with large negative values), and multiplicative masks (0/1 multiplication)
- - Additive masking (logit biasing): applying a mask by adding a large negative value (approx. -∞) to logits for masked positions before softmax
- - Multiplicative masking (zeroing): applying a mask by multiplying logits or attention weights by 0/1 and why it is usually less appropriate for logits
- - Mask broadcasting / shape alignment: the need to expand/reshape masks (e.g., from [B, S] to [B, H, S\_q, S\_k]) so they align with attention-score tensors
- - Triangular causal-mask construction: building the causal mask as a lower-triangular matrix (e.g., via tril or index comparisons j ≤ i)
- - Combining masks: logically combining padding and causal masks (e.g., AND) into a single mask applied to attention logits
- - Mask dtype and numerical-stability concerns: boolean vs float masks, using large negative constants (e.g., -1e9) instead of literal -∞ for softmax stability
- - Key-vs-query masking semantics: masking is applied to keys (K / K-axis of attention) to prevent attending to certain key positions (padding/future), not to queries
- - Where to apply the mask in the attention pipeline: apply after computing scaled logits (QK^T / sqrt(d\_k)) and before softmax
- - Effect on softmax outputs: masked logits become (numerically) zero-probability entries after softmax
- - Masking in encoder-decoder architectures: using separate masks (encoder padding mask, decoder self-attention causal mask, and decoder→encoder mask) appropriately on different attention modules
- - Incremental (cached) decoding mask behavior: during autoregressive inference with cached K/V, causal masking is enforced by only providing past keys/values or by a dynamic mask that only exposes previous positions

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Attention is only “correct” if it looks at the right places. In real Transformer training/inference, two kinds of “wrong places” appear constantly: (1) padding tokens that are not real data, and (2) future tokens that the model must not peek at during autoregressive generation. Sequence masking is the practical mechanism that prevents both failures—by editing attention scores before softmax so disallowed positions receive (almost) zero probability.

TL;DR:

An attention mask is a binary allow/block matrix M (1 = allow, 0 = block) applied to attention logits before softmax, typically via adding a large negative number (≈ −∞) where M=0. Padding masks block attention to padded keys (and sometimes padded queries). Causal masks block attention to future keys (k > q) for autoregressive decoding. In practice you broadcast masks to (B,H,Lq,Lk) and combine them with logical AND (or additive −∞) before computing softmax.

## What Is Sequence Masking (causal and padding masks)?

### Why masking exists (motivation)

In attention, every query position qqq produces a distribution over key positions kkk:

Attn(Q,K,V)=softmax(S) V,S=QK⊤dk\text{Attn}(Q,K,V) = \text{softmax}(S)\,V, \quad S = \frac{QK^\top}{\sqrt{d\_k}}Attn(Q,K,V)=softmax(S)V,S=dk​​QK⊤​

The softmax turns each row of scores Sq,:S\_{q,:}Sq,:​ into weights that sum to 1. That “sum to 1” is the core reason masking matters: if your sequence contains *invalid* tokens (padding) or *forbidden* tokens (future positions during autoregressive decoding), softmax will still allocate some probability mass to them unless you explicitly prevent it.

Masking is the standard way to encode **structural constraints** into attention: “these keys may be attended to, those keys must not.”

### Definition

An **attention mask** is a matrix MMM with entries:

- •Mq,k=1M\_{q,k} = 1Mq,k​=1 means attention from query position qqq to key position kkk is allowed.
- •Mq,k=0M\_{q,k} = 0Mq,k​=0 means it is blocked.

Shape-wise, the *conceptual* mask is often (Lq×Lk)(L\_q \times L\_k)(Lq​×Lk​), where:

- •LqL\_qLq​ = number of query positions
- •LkL\_kLk​ = number of key positions

In self-attention, typically Lq=Lk=LL\_q = L\_k = LLq​=Lk​=L.

### How a mask actually affects softmax

Masks are applied to the attention *logits* (scores) before the softmax. The most common implementation is **additive masking**:

Sq,k′={Sq,k,Mq,k=1−∞,Mq,k=0S'\_{q,k} = \begin{cases}
S\_{q,k}, & M\_{q,k}=1\\
-\infty, & M\_{q,k}=0
\end{cases}Sq,k′​={Sq,k​,−∞,​Mq,k​=1Mq,k​=0​

Then

Aq,:=softmax(Sq,:′)A\_{q,:} = \text{softmax}(S'\_{q,:})Aq,:​=softmax(Sq,:′​)

Because exp⁡(−∞)=0\exp(-\infty)=0exp(−∞)=0, masked positions get zero probability.

In real code, you don’t literally use −∞-\infty−∞; you use a large negative constant like −104-10^4−104 or −109-10^9−109 (depending on dtype and stability). The concept is “so negative that softmax assigns ~0.”

### The two mask families

1. 1)**Padding mask** (data validity): blocks keys that are padding tokens.
2. 2)**Causal mask** (information flow): blocks keys that are to the *right* of the query (future positions), enforcing autoregressive behavior.

They solve different problems and are often combined.

### A first mental model: “mask edits the graph”

Think of attention as a directed weighted graph from queries to keys. Masking removes edges before normalization.

- •Padding mask removes edges that point into padded (fake) nodes.
- •Causal mask removes edges that point forward in time.

That’s it: masking is not a learned component; it’s a rule baked into the computation.

## Core mechanic 1: Causal masking (the triangular mask) and autoregressive decoding

### Why causal masking is needed

In autoregressive language modeling, at position ttt the model must predict token xtx\_txt​ using only past context x<tx\_{<t}x<t​.

Self-attention without constraints would let position ttt attend to *future* tokens x>tx\_{>t}x>t​ during training (because they are present in the same sequence). That creates **label leakage**: the model can “cheat” by looking at the answer.

Causal masking prevents this by allowing attention only to the **prefix**.

### The causal rule

For a sequence length LLL with 0-indexed positions:

- •Query position qqq may attend to key positions k≤qk \le qk≤q.
- •Keys with k>qk > qk>q are blocked.

So the mask is lower-triangular.

### Inline diagram: the (L×L) causal triangle

Let L=6L=6L=6 and write 1=allow, 0=block. Rows are queries qqq, columns are keys kkk.

```
Causal mask M_causal (L=6):

      k: 0 1 2 3 4 5
q=0      1 0 0 0 0 0
q=1      1 1 0 0 0 0
q=2      1 1 1 0 0 0
q=3      1 1 1 1 0 0
q=4      1 1 1 1 1 0
q=5      1 1 1 1 1 1
```

This is the “causal triangle.” It encodes “no looking ahead.”

### Construction in math

A clean definition is:

Mq,kcausal=1[k≤q]M^{\text{causal}}\_{q,k} = \mathbf{1}[k \le q]Mq,kcausal​=1[k≤q]

where 1[⋅]\mathbf{1}[\cdot]1[⋅] is the indicator function.

If you use an *additive* mask BBB that adds −∞-\infty−∞ where blocked:

Bq,kcausal={0,k≤q−∞,k>qB^{\text{causal}}\_{q,k} = \begin{cases}
0, & k \le q\\
-\infty, & k > q
\end{cases}Bq,kcausal​={0,−∞,​k≤qk>q​

Then you compute S′=S+BS' = S + BS′=S+B.

### Self-attention vs cross-attention

- •**Decoder self-attention** in an autoregressive Transformer uses a causal mask.
- •**Encoder self-attention** typically does *not* use a causal mask (it’s bidirectional).
- •**Decoder cross-attention** (decoder queries attending to encoder keys) typically does *not* use a causal mask, because encoder outputs are not “future tokens” of the decoder timeline; they’re a separate source sequence.

### Subtlety: “causal” depends on the task

Causal masking is a *task constraint*, not a Transformer requirement.

- •Autoregressive generation: causal = required.
- •Masked language modeling (BERT-like): no causal mask; instead you hide tokens in input.
- •Prefix-LM (sometimes used in instruction tuning): allow full attention inside prefix, causal afterwards (a block-structured mask).

### Practical detail: training vs inference

- •**Training**: you usually compute attention for all positions in parallel, so the causal mask is essential to ensure the parallel computation matches the autoregressive factorization.
- •**Inference**: if you generate token-by-token with KV caching, causal structure is implicit (the query is only for the current step and keys are only past). But many implementations still keep a causal mask for correctness and simplicity.

## Core mechanic 2: Padding masking and combining masks (causal ∧ padding)

### Why padding masking is needed

Real batches contain sequences with different lengths. To form a rectangular tensor, shorter sequences are padded to a common length LLL.

Padding tokens are not real data. If attention can attend to them, several things go wrong:

- •Probability mass gets wasted on “nothing.”
- •Values at padded positions can pollute representations.
- •Gradients can flow through padding in ways that destabilize training.

Padding masks ensure padded keys do not receive attention.

### Key idea: padding mask is usually about **keys**

In attention, the output at query qqq is a weighted sum over values at keys kkk.

If key kkk is padding, then value **v**ₖ is meaningless; we must prevent it from contributing.

So most padding masks are applied along the **key dimension**: for each query, block the same set of padded key positions.

### From per-token validity to a (Lq×Lk) mask

Often you start with a 1D “valid tokens” vector for each sequence:

- •pk=1p\_k = 1pk​=1 if position kkk is a real token
- •pk=0p\_k = 0pk​=0 if position kkk is padding

This is shape (Lk)(L\_k)(Lk​) (or (B,Lk)(B, L\_k)(B,Lk​) for a batch).

To turn that into an attention mask you broadcast across queries:

Mq,kpad=pkM^{\text{pad}}\_{q,k} = p\_kMq,kpad​=pk​

So each row is identical: any query cannot attend to padded keys.

### Inline diagram: combined (causal ∧ padding) mask over a padded sequence

Suppose we have a batch element with length 4 padded to L=6L=6L=6:

Positions: 0 1 2 3 4 5

Tokens: A B C D <pad> <pad>

Validity: 1 1 1 1 0 0

Padding-only mask (1=allow, 0=block) applied on keys:

```
M_pad (allow real keys only):

      k: 0 1 2 3 4 5
q=0      1 1 1 1 0 0
q=1      1 1 1 1 0 0
q=2      1 1 1 1 0 0
q=3      1 1 1 1 0 0
q=4      1 1 1 1 0 0
q=5      1 1 1 1 0 0
```

Causal mask (from earlier):

```
M_causal:

      k: 0 1 2 3 4 5
q=0      1 0 0 0 0 0
q=1      1 1 0 0 0 0
q=2      1 1 1 0 0 0
q=3      1 1 1 1 0 0
q=4      1 1 1 1 1 0
q=5      1 1 1 1 1 1
```

Combined mask uses logical AND (allow only if both allow):

Mcombined=Mcausal∧MpadM^{\text{combined}} = M^{\text{causal}} \wedge M^{\text{pad}}Mcombined=Mcausal∧Mpad

Result:

```
M_combined = M_causal AND M_pad:

      k: 0 1 2 3 4 5
q=0      1 0 0 0 0 0
q=1      1 1 0 0 0 0
q=2      1 1 1 0 0 0
q=3      1 1 1 1 0 0
q=4      1 1 1 1 0 0
q=5      1 1 1 1 0 0
```

Notice how:

- •Causality blocks “future” keys.
- •Padding blocks keys 4 and 5 for *every* query.
- •Even though the causal mask would allow (q=5, k=5), padding still blocks it.

### Do we also mask padded queries?

There are two related concerns:

1. 1)**Keys/values padding**: must be masked so they don’t contribute.
2. 2)**Queries padding**: if query positions are padding, their outputs are meaningless. Some systems:

- •compute them anyway but ignore them in the loss, or
- •explicitly zero them out afterward, or
- •prevent attention computation for them via masking.

In practice, padding keys is non-negotiable; padding queries is optional but can save compute and avoid odd numerical artifacts.

### Combining masks: additive form is usually easiest

If your implementation uses additive masks BBB (0 for allow, −∞ for block), then combining is simple:

Bcombined=Bcausal+BpadB^{\text{combined}} = B^{\text{causal}} + B^{\text{pad}}Bcombined=Bcausal+Bpad

Because:

- •if either term is −∞, the sum is −∞ (blocked)
- •if both are 0, the sum is 0 (allowed)

This “sum of additive masks” is a very common pattern in Transformer codebases.

## Application/Connection: How masks integrate with attention computation (shapes, broadcasting, stability)

### Where the mask goes in scaled dot-product attention

For one batch element and one head, attention typically follows:

1) Compute scores:

S=QK⊤dkshape (Lq×Lk)S = \frac{QK^\top}{\sqrt{d\_k}} \quad \text{shape } (L\_q \times L\_k)S=dk​​QK⊤​shape (Lq​×Lk​)

2) Apply mask to get masked logits S′S'S′.

3) Softmax over keys:

Aq,:=softmax(Sq,:′)A\_{q,:} = \text{softmax}(S'\_{q,:})Aq,:​=softmax(Sq,:′​)

4) Weighted sum of values:

O=AVshape (Lq×dv)O = AV \quad \text{shape } (L\_q \times d\_v)O=AVshape (Lq​×dv​)

Masking must happen **before** softmax. Masking after softmax is not equivalent because the distribution would no longer be normalized correctly.

### Shape/broadcasting schematic (most common source of bugs)

In multi-head attention with batching, you commonly work with these shapes:

- •QQQ: (B, H, Lq, d)
- •KKK: (B, H, Lk, d)
- •VVV: (B, H, Lk, d)
- •Scores S=QK⊤S = QK^\topS=QK⊤: (B, H, Lq, Lk)

You want a mask that can broadcast to (B, H, Lq, Lk).

Here are typical mask shapes and how they broadcast:

```
Target scores S:      (B, H, Lq, Lk)

Causal mask:          (1, 1, Lq, Lk)   or (Lq, Lk)
Padding key mask:     (B, 1, 1,  Lk)   from (B, Lk)
Combined mask:        (B, 1, Lq, Lk)   after broadcast AND/add
```

Key principle:

- •Causal depends on (Lq, Lk) only (same for every batch element).
- •Padding depends on which tokens are real for each batch element (varies with B), but is usually identical across heads and queries.

### Table: common mask representations

| Representation | Allowed? | Typical values | Combine rule | Pros | Cons |
| --- | --- | --- | --- | --- | --- |
| Binary allow mask MMM | 1=allow | {0,1} or {False,True} | AND | Conceptually clear | You still need to convert to additive for logits |
| Additive bias mask BBB | 0=allow | {0, −∞} (or large negative) | add | Directly added to scores | Must choose safe negative constant |

### Numerical stability: why “−∞” must be chosen carefully

Softmax is typically computed using a stabilized form:

softmax(s)i=exp⁡(si−m)∑jexp⁡(sj−m)where m=max⁡jsj\text{softmax}(\mathbf{s})\_i = \frac{\exp(s\_i - m)}{\sum\_j \exp(s\_j - m)}\quad \text{where } m = \max\_j s\_jsoftmax(s)i​=∑j​exp(sj​−m)exp(si​−m)​where m=jmax​sj​

If masked positions are very negative, exp⁡(very negative)≈0\exp(\text{very negative}) \approx 0exp(very negative)≈0, which is what you want.

But two pitfalls:

1. 1)If **all** positions in a row are masked, you get softmax over all −∞, which can produce NaNs.
2. 2)With low-precision dtypes (fp16/bf16), extremely negative constants can underflow in unexpected ways.

Typical engineering fixes:

- •Ensure every query has at least one unmasked key (e.g., for causal masks, diagonal is allowed).
- •If some queries correspond to padding, avoid computing loss on them and/or force a safe attention pattern.
- •Use library attention kernels that handle masking robustly.

### Worked integration: masked attention logits

Let SSS be scores and MMM be a binary mask.

Convert MMM to an additive mask:

B=(1−M)⋅(−∞)B = (1 - M) \cdot (-\infty)B=(1−M)⋅(−∞)

Then apply:

S′=S+BS' = S + BS′=S+B

Then:

A=softmax(S′)A = \text{softmax}(S')A=softmax(S′)

Finally output:

O=AVO = AVO=AV

### Connection to Transformers

Masks are a “plumbing” idea that becomes crucial in:

- •**Decoder-only Transformers** (GPT-like): causal mask is central.
- •**Encoder-decoder Transformers** (T5-like):
- •encoder self-attention uses padding mask,
- •decoder self-attention uses causal + padding,
- •decoder cross-attention uses padding mask for encoder keys.

Once you can build and broadcast these masks correctly, multi-head attention and full Transformers become much easier to implement without silent correctness bugs.

## Worked Examples (3)

### Example 1: Apply an additive causal mask to attention scores and compute the resulting weights

We have a single-head self-attention with L=3. Scores (already scaled by 1/√d) are:

S =

[ [ 2.0, 1.0, 0.0 ],

[ 1.0, 3.0, 2.0 ],

[ 0.0, 1.0, 4.0 ] ]

We want causal attention: query q can attend only to keys k ≤ q. Use additive mask with −∞ for blocked positions.

1. Step 1: Write the causal binary mask M (1=allow, 0=block) for L=3:

   M =

   [ [1,0,0],

   [1,1,0],

   [1,1,1] ]
2. Step 2: Convert to additive mask B (0 for allow, −∞ for block):

   B =

   [ [0, −∞, −∞],

   [0, 0, −∞],

   [0, 0, 0] ]
3. Step 3: Add B to scores: S' = S + B:

   S' =

   [ [ 2.0, −∞, −∞ ],

   [ 1.0, 3.0, −∞ ],

   [ 0.0, 1.0, 4.0 ] ]
4. Step 4: Softmax each row.

   Row q=0: softmax([2.0, −∞, −∞]) = [1, 0, 0]

   Row q=1: softmax([1.0, 3.0, −∞])

   Compute stabilized:

   max = 3.0

   exp([1−3, 3−3, −∞]) = exp([−2, 0, −∞]) = [e^(−2), 1, 0]

   Sum = e^(−2) + 1

   So weights = [ e^(−2)/(1+e^(−2)), 1/(1+e^(−2)), 0 ]

   Numerically e^(−2)≈0.1353 ⇒ weights ≈ [0.1192, 0.8808, 0]

   Row q=2: softmax([0.0, 1.0, 4.0])

   max = 4.0

   exp([−4, −3, 0]) = [e^(−4), e^(−3), 1] ≈ [0.0183, 0.0498, 1]

   Sum ≈ 1.0681

   weights ≈ [0.0171, 0.0466, 0.9363]

**Insight:** Masking changes the probability simplex that softmax operates on: it removes forbidden keys before normalization. Notice q=1 would have put some mass on k=2 without masking (because score 2.0 is high), but causal masking forces that mass to be redistributed among allowed keys.

### Example 2: Build and broadcast a combined (causal ∧ padding) mask to (B,H,Lq,Lk)

We have B=2 sequences padded to L=5, and we run H=4 heads of decoder self-attention (so we need causal masking).

Sequence lengths: [3, 5]

So valid tokens p (1=real, 0=pad) are:

- •batch 0: [1,1,1,0,0]
- •batch 1: [1,1,1,1,1]

We want a final additive mask B\_combined broadcastable to scores S of shape (B,H,L,L).

1. Step 1: Start with padding validity p of shape (B,L):

   p =

   [ [1,1,1,0,0],

   [1,1,1,1,1] ] shape (2,5)
2. Step 2: Convert padding validity into a key-mask over attention scores.

   We want shape (B,1,1,Lk) so it broadcasts across heads and queries.

   M\_pad\_key[b,1,1,k] = p[b,k]

   So M\_pad\_key has shape (2,1,1,5).
3. Step 3: Build causal mask once for L=5.

   Binary causal mask M\_causal has shape (1,1,Lq,Lk) = (1,1,5,5):

   For q,k in 0..4:

   M\_causal[1,1,q,k] = 1 if k ≤ q else 0.
4. Step 4: Combine binary masks with AND via broadcasting:

   M\_combined = M\_causal AND M\_pad\_key

   Broadcast reasoning:

   - •M\_causal: (1,1,5,5)
   - •M\_pad\_key: (2,1,1,5)

   Result: (2,1,5,5)

   Then it can broadcast to (2,4,5,5) across heads.
5. Step 5: Convert to additive mask B\_combined.

   A common conversion is:

   B\_combined = (1 − M\_combined) \* (−C)

   where C is a large constant like 1e9 (float32) or 1e4 (fp16).

   Shape is (2,1,5,5), broadcastable to (2,4,5,5).
6. Step 6: Apply to scores.

   If scores S are (B,H,L,L) = (2,4,5,5), then masked logits are:

   S' = S + B\_combined

   Because B\_combined broadcasts over H, every head uses the same structural constraint.

**Insight:** Most masking bugs are shape bugs. If you remember two canonical shapes—causal as (1,1,L,L) and padding-as-keys as (B,1,1,L)—then “AND then broadcast to (B,H,L,L)” becomes almost mechanical.

### Example 3: Detect and fix the “all masked row” NaN failure mode

Suppose in a batch you include sequences with length 0 after truncation (or you mistakenly treat all positions as padding). For one batch element, the padding validity is p=[0,0,0,0]. You build M\_pad and apply it to attention logits, then softmax returns NaNs.

1. Step 1: Observe what happens to one query row.

   If all keys are masked, then masked logits look like:

   S'\_{q,:} = [−∞, −∞, −∞, −∞]
2. Step 2: Softmax is undefined in this case.

   Stabilized softmax subtracts max, but max is −∞, leading to indeterminate forms like exp(−∞ − (−∞)). Many kernels output NaN.
3. Step 3: Fix options.

   Option A (data hygiene): never create length-0 sequences; filter them out.

   Option B (force at least one allowed key): if a row would be fully masked, unmask a safe position (often k=0) just to avoid NaNs.

   Option C (mask padded queries): don’t compute attention outputs for padded query positions (or set their outputs to 0) and ensure loss ignores them.
4. Step 4: Preferred fix in Transformers.

   Most training pipelines ensure each example has at least 1 real token. Additionally, they ignore padded positions in the loss, so padded queries don’t matter.

**Insight:** Masking is a correctness constraint, but it can create undefined softmax rows if you accidentally mask everything. Robust systems treat this as an invariant: every query row must have at least one valid key, or the query itself is ignored.

## Key Takeaways

- ✓

  Sequence masking edits attention logits before softmax so disallowed positions receive ~0 probability.
- ✓

  Causal masks enforce autoregressive behavior via a lower-triangular (L×L) structure: allow k ≤ q, block k > q.
- ✓

  Padding masks block attention to padded keys; they usually start from a (B,L) validity vector and broadcast to (B,1,1,Lk).
- ✓

  Masks are commonly implemented as additive biases: 0 for allowed, −∞ (or a large negative) for blocked; combined masks add together.
- ✓

  Correct broadcasting targets scores of shape (B,H,Lq,Lk); typical causal mask is (1,1,Lq,Lk).
- ✓

  Masking keys/values is essential; masking queries is optional but can prevent NaNs and wasted compute when queries are padding.
- ✓

  Watch out for the “all keys masked” row, which can cause NaNs in softmax.

## Common Mistakes

- ✗

  Applying the mask after softmax (this breaks normalization and still allows masked positions to influence the distribution indirectly).
- ✗

  Using the wrong mask orientation (masking queries instead of keys, or transposing (Lq×Lk) so the triangle points the wrong way).
- ✗

  Broadcasting to the wrong shape (e.g., (B,L) added directly to (B,H,L,L) without expanding dims), causing silent incorrect masking.
- ✗

  Accidentally masking all keys for some queries (often due to length bugs), leading to NaNs.

## Practice

easy

Construct the binary causal mask M for L=4 (1=allow, 0=block). Then indicate which entries are blocked for query q=2.

**Hint:** Causal means allow k ≤ q. Write a 4×4 lower-triangular matrix of ones.

Show solution

For L=4 (q,k ∈ {0,1,2,3}):

M =

[ [1,0,0,0],

[1,1,0,0],

[1,1,1,0],

[1,1,1,1] ]

For query q=2, keys k=3 is blocked (M[2,3]=0). Keys 0,1,2 are allowed.

medium

You have a batch with B=3 sequences padded to L=6. Their lengths are [6, 2, 4]. Build the padding validity matrix p of shape (B,L) using 1 for real tokens and 0 for pads. Then state the shape you would broadcast it to for masking keys in attention scores of shape (B,H,L,L).

**Hint:** Each row has 'length' ones followed by zeros. Key masking typically becomes (B,1,1,L).

Show solution

Validity p (B=3, L=6):

- •length 6: [1,1,1,1,1,1]
- •length 2: [1,1,0,0,0,0]
- •length 4: [1,1,1,1,0,0]

So

p =

[ [1,1,1,1,1,1],

[1,1,0,0,0,0],

[1,1,1,1,0,0] ]

To mask keys for scores (B,H,L,L), broadcast to (B,1,1,L) = (3,1,1,6).

hard

Given attention logits for one query row s = [5, 1, 0] and a binary mask m = [1, 0, 1] (so key 1 is blocked), compute the masked softmax weights exactly in terms of exponentials, and approximately as decimals.

**Hint:** Set the blocked logit to −∞, then softmax over the remaining two positions. Use stabilization by subtracting max=5.

Show solution

Masking gives s' = [5, −∞, 0].

Softmax weights:

- •w₀ = exp(5) / (exp(5) + exp(0))
- •w₁ = 0
- •w₂ = exp(0) / (exp(5) + exp(0))

Stabilize by subtracting 5:

Denominator = exp(0) + exp(−5) = 1 + e^(−5)

So

w₀ = 1 / (1 + e^(−5))

w₂ = e^(−5) / (1 + e^(−5))

Numerically e^(−5)≈0.006737:

w₀≈ 1 / 1.006737 ≈ 0.993307

w₁=0

w₂≈ 0.006693

## Connections

Next, use masking inside full attention blocks and architectures:

- •[Transformers](/tech-tree/transformers/)

Related ideas you’ll likely encounter alongside masking:

- •KV caching in autoregressive decoding (causal constraint becomes implicit per-step)
- •Prefix-LM / block masks (partially bidirectional attention)
- •FlashAttention-style kernels (efficient masked attention computation)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
