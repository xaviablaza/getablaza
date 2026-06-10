---
title: Positional Encoding
description: Techniques for injecting sequence order information into token embeddings (e.g., sinusoidal or learned encodings) so models that process tokens in parallel can sense relative or absolute position.
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
permalink: /tech-tree/positional-encoding/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Positional Encoding

Machine LearningDifficulty: ★★★☆☆Depth: 0Unlocks: 1

Techniques for injecting sequence order information into token embeddings (e.g., sinusoidal or learned encodings) so models that process tokens in parallel can sense relative or absolute position.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Purpose: inject explicit sequence-order information into token representations so models that process tokens in parallel can use token order
- -Absolute vs relative positional information: absolute encodings index a token's position; relative encodings represent offsets between token positions
- -Integration mechanism: positions are mapped to vectors and those vectors are combined with token embeddings or applied as attention biases

## Key Symbols & Notation

p (position index)PE(p) (positional encoding vector for position p)

## Essential Relationships

- -PE(p) maps an integer position p (or an offset p\_i-p\_j for relative schemes) to a vector that is combined with token embeddings (e.g., added or concatenated) or injected as attention biases so the model can use order information

## Unlocks (1)

[Transformerslvl 5](/tech-tree/transformers/)

Advanced Learning Details

### Graph Position

6

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

0

Chain Length

### Cognitive Load

6

Atomic Elements

32

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (13)

- - Positional encoding: injecting token position information into embeddings so models can use order
- - Permutation invariance of self-attention: self-attention by itself does not encode token order
- - Absolute positional encoding: a representation that encodes each token's absolute index
- - Learned positional embeddings: a trainable lookup table mapping position index -> vector
- - Sinusoidal positional encoding: fixed, deterministic position vectors built from sin/cosines at multiple frequencies
- - Relative positional encoding: encoding distances or offsets between token positions instead of absolute indices
- - Additive integration of positional encodings: adding positional vectors to token embeddings
- - Concatenative integration of positional encodings: concatenating position vectors with token embeddings
- - Attention-score biasing for relative positions: injecting relative-position information by adding biases to attention logits
- - Frequency interpretation of sinusoidal encodings: embedding dimensions correspond to different sinusoid wavelengths (scales)
- - Extrapolation/generalization behavior: fixed sinusoidal encodings can generalize to longer sequences, learned lookup tables typically cannot
- - Uniqueness / phase encoding property: pairs of sin/cos at multiple frequencies produce position-dependent phase patterns that help recover relative offsets
- - Rotary (multiplicative) positional embeddings (conceptual): applying rotations to queries/keys to encode relative position multiplicatively rather than by addition

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

A Transformer can read every token at once. That’s a superpower—but it also means the model has no built-in sense of “first”, “next”, or “last”. Positional encoding is the trick that gives parallel token processing a usable notion of order.

TL;DR:

Positional encoding maps each position index p to a vector PE(p). You combine PE(p) with a token embedding so the model can use order. Absolute encodings represent “this token is at position p”. Relative encodings represent “token i is k steps away from token j”, often implemented as attention biases. Sinusoidal encodings are deterministic and extrapolate; learned encodings can fit data but may not generalize to longer sequences unless designed carefully.

## What Is Positional Encoding?

### Why do we need it?

Many sequence models (like RNNs) process tokens in order, so **time** is baked into the computation: token 7 can only be seen after token 6. Transformers, in contrast, are designed to process a sequence **in parallel**. Self-attention compares tokens to each other without inherently knowing which token came earlier.

If you hand a Transformer the embeddings for “the cat sat” and “sat cat the”, the *multiset* of token embeddings might look similar. Without extra information, the model has no explicit “slot index” to tell it which token was first.

Positional encoding fixes this by injecting order information into the representation.

### Core definition

Let p be a position index (typically p ∈ {0, 1, …, L−1} for a sequence length L). A positional encoding is a mapping

- •PE : p ↦ PE(p) ∈ ℝᵈ

where d is the model’s embedding dimension.

Each token also has an embedding (from a learned embedding table):

- •E(token) ∈ ℝᵈ

To create the model input at position p, we combine them, often by simple addition:

- •**x**ₚ = E(tokenₚ) + PE(p)

Here **x**ₚ, E(tokenₚ), and PE(p) are vectors in ℝᵈ. (We’ll write vectors in bold: **x**, **v**.)

### What properties do we want?

Positional encoding should make position *usable* for attention and downstream layers. In practice, that means:

1. 1)**Distinctness**: different positions should map to different vectors.
2. 2)**Smoothness / structure**: nearby positions should relate in a learnable way (useful for local patterns).
3. 3)**Generalization**: ideally it should work for sequence lengths longer than those seen in training.
4. 4)**Compatibility with attention**: attention computes dot products like (**q**ᵢ)ᵀ(**k**ⱼ); we want positional info to influence these comparisons.

### Absolute vs relative: the big split

There are two main ways to represent order:

- •**Absolute positional information**: “This token is at position p.” (PE(p) is tied to p.)
- •**Relative positional information**: “Token j is (j−i) steps away from token i.” (Encoding depends on offset.)

Both can work, but they lead to different inductive biases and different generalization behavior.

### How it’s integrated (big picture)

There are two common integration mechanisms:

1. 1)**Add/concatenate to embeddings** (absolute-style):

- •**x**ₚ = E(tokenₚ) + PE(p)

2. 2)**Attention bias / modification** (relative-style):

- •attention score(i, j) = (**q**ᵢ)ᵀ(**k**ⱼ) / √dₖ + b(i, j)
- •where b(i, j) depends on relative position (j−i) or sometimes absolute indices.

A useful mental model:

- •*Absolute encoding* changes “what each token looks like.”
- •*Relative encoding* changes “how tokens compare to each other.”

## Core Mechanic 1: Absolute Positional Encodings (Sinusoidal and Learned)

### Motivation: give every slot an identity

Absolute positional encodings make position a feature of the token representation. If position p has a unique “signature” vector PE(p), then the model can learn rules like:

- •“Attend strongly to position 0 (start token).”
- •“Treat positions near the end differently.”
- •“If token is at position p=1, it’s likely a subject (in some domains).”

The simplest integration is addition:

- •**x**ₚ = E(tokenₚ) + PE(p)

Addition is popular because it preserves dimension d and is parameter-free at the integration step.

### Learned absolute positional embeddings

The most direct approach is to learn a table P ∈ ℝᴸmax×ᵈ, where Lmax is the maximum length during training.

- •PE(p) = P[p]

**Pros**:

- •Very flexible: the model can discover whatever positional geometry helps.

**Cons**:

- •Hard cap at Lmax unless you extend/resize.
- •Often weak extrapolation to longer sequences (positions beyond training are unseen).

### Sinusoidal positional encoding (classic Transformer)

Sinusoidal PE is deterministic and defined by sines and cosines of different frequencies. For embedding dimension d (assume d is even), define for p ≥ 0 and i ∈ {0, 1, …, d/2 − 1}:

- •PE(p)[2i] = sin(p / 10000^(2i/d))
- •PE(p)[2i+1] = cos(p / 10000^(2i/d))

This produces a length-d vector with alternating sine/cosine pairs.

### Why sinusoids?

The key intuition is **multi-scale periodic structure**:

- •Small i (low frequency denominator) varies quickly with p → captures local position changes.
- •Large i varies slowly → captures coarse position.

The encoding gives each position a unique pattern across many frequencies.

### A useful property: relative shifts become linear-ish

A major reason sinusoids were chosen is that relative position relationships can be expressed via trig identities.

Let ωᵢ = 1 / 10000^(2i/d). Then:

- •sin((p+Δ)ωᵢ) = sin(pωᵢ)cos(Δωᵢ) + cos(pωᵢ)sin(Δωᵢ)
- •cos((p+Δ)ωᵢ) = cos(pωᵢ)cos(Δωᵢ) − sin(pωᵢ)sin(Δωᵢ)

So the pair [sin(pωᵢ), cos(pωᵢ)] can be transformed to [sin((p+Δ)ωᵢ), cos((p+Δ)ωᵢ)] by a 2×2 rotation matrix depending only on Δ.

That matters because attention compares vectors via dot products. If your representation contains sinusoidal components, the model can *learn* to detect or use relative offsets.

### Table: absolute options compared

| Method | Parameters | Extrapolates beyond Lmax? | Typical integration | Notes |
| --- | --- | --- | --- | --- |
| Learned absolute embedding | Yes (Lmax×d) | No (without hacks) | Add to token embedding | Strong fit to training length distribution |
| Sinusoidal | No | Often yes | Add to token embedding | Deterministic; good default; classic Transformer |

### Practical details: scaling and dropout

In many implementations, token embeddings are scaled by √d before adding PE:

- •**x**ₚ = √d · E(tokenₚ) + PE(p)

Why? Early in training, learned embeddings may have small variance; scaling can help balance magnitudes so positional info doesn’t dominate (or vanish).

Also, dropout is often applied to the sum:

- •**x**ₚ = Dropout( √d · E(tokenₚ) + PE(p) )

This regularizes reliance on any single dimension or exact positional signature.

### Limitation of pure absolute encoding

Absolute encodings label positions, but attention often cares about *relative* patterns:

- •“Look one token to the left.”
- •“Attend to the previous occurrence.”

Absolute encodings can still learn these behaviors, but it can be less direct, especially when you want translation-invariant rules (“the same rule anywhere in the sequence”). That motivates relative positional mechanisms.

## Core Mechanic 2: Relative Positional Encodings (Offsets and Attention Biases)

### Motivation: attention is about relationships

Self-attention’s core operation for a query position i and key position j is a similarity score:

- •score(i, j) = (**q**ᵢ)ᵀ(**k**ⱼ) / √dₖ

This has no explicit awareness of distance or direction (left vs right). Relative positional encodings inject information about (j−i) directly into the scoring.

A common pattern:

- •score(i, j) = (**q**ᵢ)ᵀ(**k**ⱼ) / √dₖ + b(j−i)

where b(Δ) is a learned scalar bias for offset Δ (possibly clipped to a range).

### Relative position as an embedding

Instead of a scalar bias, we can use a vector embedding R[Δ] ∈ ℝᵈ and incorporate it into attention:

One family of formulations modifies keys/values:

- •score(i, j) = (**q**ᵢ)ᵀ( **k**ⱼ + **r**\_{j−i} ) / √dₖ

Expand this:

- •(**q**ᵢ)ᵀ( **k**ⱼ + **r**\_{j−i} )

= (**q**ᵢ)ᵀ**k**ⱼ + (**q**ᵢ)ᵀ**r**\_{j−i}

So the score becomes content similarity plus an offset-dependent term.

### Why this is powerful

Relative encoding bakes in a helpful inductive bias:

- •If the same local pattern occurs at different absolute locations, the model can reuse it.
- •The model can naturally learn “nearby tokens matter more” or directional rules.

It also often improves generalization to longer sequences because offsets (like Δ = ±1, ±2, …) are length-agnostic.

### Clipping and windowing offsets

In practice, you can’t store embeddings for every possible offset if sequences are long. Typical strategies:

- •Clip Δ into [−K, K]
- •Use a bucket function that maps large distances into coarse bins

So:

- •Δ′ = clip(j−i, −K, K)
- •use b(Δ′) or **r**\_{Δ′}

This trades exact long-range distance for manageable parameters.

### Rotary positional embeddings (RoPE) as a relative-ish approach

Another widely used modern method is to apply a position-dependent rotation to queries and keys so that dot products encode relative offsets.

High-level idea:

- •Split dimensions into 2D pairs.
- •For each position p, rotate each pair by an angle θ(p) that depends on p.
- •Use rotated queries/keys in attention.

For one 2D pair, if **u** = [u₀, u₁]ᵀ, define rotation:

- •R(θ) = [[cos θ, −sin θ],

[sin θ, cos θ]]

Then **u**′ = R(θ) **u**.

If queries and keys are rotated by their positions, the dot product between rotated vectors can become a function of relative angle differences (hence relative position). This tends to generalize well and is popular in LLMs.

### Table: relative vs absolute (conceptual)

| Aspect | Absolute PE | Relative PE |
| --- | --- | --- |
| Represents | “Token is at p” | “Token j is Δ away from i” |
| Typical implementation | Add PE(p) to embeddings | Add bias b(Δ) to attention scores or modify q/k |
| Inductive bias | Position-specific behaviors | Translation-invariant, distance-aware behaviors |
| Long-length generalization | Sinusoidal: decent; Learned: weak | Often strong (offsets/buckets/RoPE) |

### Integration mechanism summary

You can think of positional information entering the model in two places:

1. 1)**Input space**: modify **x**ₚ = E(tokenₚ) + PE(p)
2. 2)**Attention space**: modify score(i, j)

Many strong architectures use both (or a more sophisticated variant) because input position and attention distance can each be useful.

## Application/Connection: Positional Encoding Inside Transformers

### Where it sits in the Transformer pipeline

A simplified Transformer input pipeline looks like:

1. 1)Tokenize text → tokens t₀…t\_{L−1}
2. 2)Embed tokens → E(tₚ) ∈ ℝᵈ
3. 3)Add positional encoding → **x**ₚ = E(tₚ) + PE(p)
4. 4)Feed **x**ₚ into stacked self-attention + MLP blocks

Inside each attention layer (single head for simplicity):

- •**q**ᵢ = **W**\_Q **x**ᵢ
- •**k**ⱼ = **W**\_K **x**ⱼ
- •**v**ⱼ = **W**\_V **x**ⱼ

Attention weights:

- •α(i, j) = softmaxⱼ( score(i, j) )

With basic attention:

- •score(i, j) = (**q**ᵢ)ᵀ(**k**ⱼ) / √dₖ

With relative bias:

- •score(i, j) = (**q**ᵢ)ᵀ(**k**ⱼ) / √dₖ + b(j−i)

Output:

- •**y**ᵢ = ∑ⱼ α(i, j) **v**ⱼ

### What positional encoding enables (concrete behaviors)

Once the model has position information, it can learn:

- •**Word order sensitivity**: “dog bites man” vs “man bites dog”
- •**Syntax patterns**: verbs often follow subjects in English
- •**Local features**: n-gram-like patterns via attention to nearby positions
- •**Segment structure**: headers, lists, code blocks, etc.

### Choosing a method: engineering trade-offs

| Goal | Good default | Reason |
| --- | --- | --- |
| Simple baseline Transformer | Sinusoidal absolute PE | No extra params; decent generalization |
| Fixed max length, plenty of data | Learned absolute PE | Flexible and often strong in-domain |
| Strong long-context behavior | Relative bias / RoPE-style | Better length extrapolation and distance awareness |

### Connection to the next node: Transformers

Positional encoding is one of the key ingredients that make Transformers work on sequences at all. Without it, self-attention is permutation-invariant: it can’t reliably distinguish different orderings. Once you add PE, the attention mechanism becomes sequence-aware.

In the [Transformers](/tech-tree/transformers/) node, you’ll see how multi-head attention and stacked layers exploit this positional information to build hierarchical features—from local dependencies to global structure.

## Worked Examples (3)

### Compute a small sinusoidal positional encoding by hand (d = 4)

Let d = 4 (so we have i = 0, 1). Use the classic sinusoidal formula:

PE(p)[2i] = sin(p / 10000^(2i/d))

PE(p)[2i+1] = cos(p / 10000^(2i/d))

Compute PE(0) and PE(1).

1. Identify the frequencies.

   For i = 0:

   2i/d = 0/4 = 0

   10000^(0) = 1

   So the denominator is 1.

   For i = 1:

   2i/d = 2/4 = 1/2

   10000^(1/2) = √10000 = 100

   So the denominator is 100.
2. Compute PE(0).

   For p = 0:

   PE(0)[0] = sin(0/1) = sin(0) = 0

   PE(0)[1] = cos(0/1) = cos(0) = 1

   PE(0)[2] = sin(0/100) = sin(0) = 0

   PE(0)[3] = cos(0/100) = cos(0) = 1

   So:

   PE(0) = [0, 1, 0, 1].
3. Compute PE(1).

   For p = 1:

   PE(1)[0] = sin(1/1) = sin(1)

   PE(1)[1] = cos(1/1) = cos(1)

   PE(1)[2] = sin(1/100) = sin(0.01)

   PE(1)[3] = cos(1/100) = cos(0.01)

   So:

   PE(1) = [sin(1), cos(1), sin(0.01), cos(0.01)].
4. Optional numeric intuition (radians).

   sin(1) ≈ 0.84, cos(1) ≈ 0.54

   sin(0.01) ≈ 0.01, cos(0.01) ≈ 0.99995

   So:

   PE(1) ≈ [0.84, 0.54, 0.01, 0.99995].

   Notice how the first pair changes a lot between p=0 and p=1, while the second pair changes very little—this is the multi-scale idea.

**Insight:** Different dimensions encode position at different “speeds”. Fast-changing components help with local order; slow-changing components help disambiguate larger positions and give the model coarse location cues.

### See how relative attention bias changes what a token attends to

Consider a single query position i that will attend to three key positions j ∈ {i−1, i, i+1}. Suppose the content-based dot products (already divided by √dₖ) are:

content scores: s\_content = [0.2, 0.2, 0.2]

So without position, all are equally likely.

Now add a relative bias that prefers the previous token:

b(−1)=0.5, b(0)=0.0, b(+1)=−0.5.

Compute the new attention distribution α over j.

1. Write the total scores.

   For Δ = j−i:

   Δ = −1 → score = 0.2 + 0.5 = 0.7

   Δ = 0 → score = 0.2 + 0.0 = 0.2

   Δ = +1 → score = 0.2 − 0.5 = −0.3

   So:

   s\_total = [0.7, 0.2, −0.3].
2. Apply softmax.

   α\_k = exp(s\_total[k]) / ∑ exp(s\_total[m])

   Compute exponentials (approx):

   exp(0.7) ≈ 2.0138

   exp(0.2) ≈ 1.2214

   exp(−0.3) ≈ 0.7408

   Sum ≈ 2.0138 + 1.2214 + 0.7408 = 3.9760
3. Normalize.

   α(Δ=−1) ≈ 2.0138 / 3.9760 ≈ 0.506

   α(Δ=0) ≈ 1.2214 / 3.9760 ≈ 0.307

   α(Δ=+1) ≈ 0.7408 / 3.9760 ≈ 0.186
4. Compare to no-bias case.

   Without bias, all scores were equal, so α would be [1/3, 1/3, 1/3].

   With bias, attention shifts strongly toward the previous token (Δ=−1) even though the content scores were identical.

**Insight:** Relative positional bias directly shapes attention patterns (like “look left”) independently of token content. This is often an easier way for the model to learn local or directional dependencies than relying on absolute position signatures.

### Why adding PE to embeddings makes order detectable (a toy linear view)

Suppose we have two tokens A and B with embeddings E(A)=**a** and E(B)=**b** in ℝᵈ, and positional encodings PE(0)=**p**₀, PE(1)=**p**₁.

Compare the input sets for sequences [A, B] vs [B, A] under addition: **x**₀=E(token₀)+PE(0), **x**₁=E(token₁)+PE(1).

1. Write inputs for [A, B].

   Sequence 1:

   **x**₀ = **a** + **p**₀

   **x**₁ = **b** + **p**₁
2. Write inputs for [B, A].

   Sequence 2:

   **x**′₀ = **b** + **p**₀

   **x**′₁ = **a** + **p**₁
3. Show these are not just a permutation of the same vectors unless special coincidences occur.

   If the model only saw {**a**, **b**} with no position, swapping A and B would just swap the vectors.

   With positions, the actual vectors differ:

   **a** + **p**₀ ≠ **a** + **p**₁ (if **p**₀ ≠ **p**₁)

   So token A at position 0 is representationally different from token A at position 1.
4. Connect to a simple linear detector.

   A linear layer computes **z**ₚ = **W****x**ₚ.

   Then:

   **z**₀ = **W****a** + **W****p**₀

   **z**₁ = **W****b** + **W****p**₁

   So the network can learn **W** such that **W****p**₀ and **W****p**₁ act like learned “position features” that influence downstream behavior.

**Insight:** Even with a simple add operation, positional vectors act like features that downstream layers can read. They turn “token identity” into “token-at-position”, which is enough to break permutation invariance.

## Key Takeaways

- ✓

  Transformers process tokens in parallel, so they need explicit order information; positional encoding supplies it.
- ✓

  A positional encoding is a mapping p ↦ PE(p) ∈ ℝᵈ, combined with token embeddings (commonly by addition: **x**ₚ = E(tokenₚ) + PE(p)).
- ✓

  Absolute encodings identify positions directly (position p has its own vector), while relative encodings represent offsets (j−i) between tokens.
- ✓

  Sinusoidal PE is deterministic, parameter-free, and has trig structure that helps represent relative shifts; it often extrapolates to longer sequences.
- ✓

  Learned absolute positional embeddings are flexible but usually tied to a maximum training length Lmax and may generalize poorly beyond it.
- ✓

  Relative positional methods often enter as attention biases or query/key modifications, directly shaping score(i, j) based on distance and direction.
- ✓

  You can inject position in input space (add to embeddings) or in attention space (bias scores); both approaches make attention order-aware.

## Common Mistakes

- ✗

  Assuming self-attention “naturally” knows token order—without PE or a relative mechanism, it is largely permutation-invariant.
- ✗

  Mixing up absolute and relative: adding PE(p) to embeddings is absolute; adding a term depending on (j−i) to attention is relative.
- ✗

  For learned absolute PE, forgetting the maximum length constraint (Lmax) and being surprised when evaluation sequences exceed it.
- ✗

  Using positional vectors with mismatched scale (e.g., PE dominating token embeddings), leading to unstable training or poor utilization of content.

## Practice

easy

Sinusoidal PE practice: For d = 6 and position p = 2, write the symbolic form of PE(2) (you don’t need decimals).

**Hint:** Use i ∈ {0,1,2}. Denominators are 10000^(2i/d) = 10000^(0), 10000^(2/6), 10000^(4/6).

Show solution

For d=6, i=0,1,2.

Let denom(i) = 10000^(2i/6).

Then:

PE(2)[0] = sin(2 / 10000^(0))

PE(2)[1] = cos(2 / 10000^(0))

PE(2)[2] = sin(2 / 10000^(2/6))

PE(2)[3] = cos(2 / 10000^(2/6))

PE(2)[4] = sin(2 / 10000^(4/6))

PE(2)[5] = cos(2 / 10000^(4/6))

medium

Relative bias reasoning: Suppose an attention head uses score(i, j) = s\_content(i, j) + b(j−i). If b(Δ) is strongly positive for Δ=0 and strongly negative otherwise, what behavior does this encourage? Give one task where this might help and one where it might hurt.

**Hint:** Think about the model preferring to attend to itself (j=i).

Show solution

A large positive b(0) and negative b(Δ≠0) encourages **self-attention to focus on the same position** (j=i), reducing mixing across tokens.

Help: tasks where per-token transformations dominate, e.g., tagging where each token label depends mostly on itself, or when early layers should preserve identity.

Hurt: tasks needing context integration, e.g., coreference, long-range dependencies, or next-token prediction where previous tokens are essential.

hard

Design choice: You need a model to handle sequences up to length 16k at inference, but training is mostly on length ≤ 2k. Which positional strategy (learned absolute vs sinusoidal absolute vs relative bias/RoPE) would you favor and why?

**Hint:** Focus on length extrapolation and what happens to positions not seen during training.

Show solution

Favor a **relative positional method (relative bias or RoPE)**, because it tends to generalize better when inference lengths exceed training lengths: offsets (j−i) remain meaningful regardless of absolute index. Sinusoidal absolute PE can also extrapolate reasonably since it’s defined for any p, but relative mechanisms more directly encode distance and often behave better for long-context attention patterns. Learned absolute PE is the least suitable because positions beyond Lmax are undefined/untrained and typically require resizing/interpolation with uncertain generalization.

## Connections

Next: [Transformers](/tech-tree/transformers/)

Related ideas you’ll encounter soon:

- •Attention scoring and dot products in multi-head attention
- •Sequence length generalization and long-context modeling
- •Embedding geometry (how adding vectors changes what linear layers and attention can express)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
