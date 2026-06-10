---
title: Channel Capacity
description: Maximum reliable transmission rate. Shannon's theorem.
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
permalink: /tech-tree/channel-capacity/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Channel Capacity

Information TheoryDifficulty: ★★★★★Depth: 8Unlocks: 0

Maximum reliable transmission rate. Shannon's theorem.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Channel as a probabilistic mapping: a channel is specified by its transition law p(y|x) (input-to-output conditional distribution).
- -Channel capacity: a single-number property of a channel that denotes the maximum reliable transmission rate (bits per channel use).

## Key Symbols & Notation

C (channel capacity)p(y|x) (channel transition probability)

## Essential Relationships

- -Shannon noisy-channel coding theorem: C = sup\_{p(x)} I(X;Y) for the given p(y|x); for any rate R < C there exist codes with vanishing error probability (achievability) and rates R > C are not reliably achievable (converse).

## Prerequisites (2)

[Mutual Information5 atoms](/tech-tree/mutual-information/)[Entropy5 atoms](/tech-tree/entropy/)

Advanced Learning Details

### Graph Position

100

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

8

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

### All Concepts (13)

- - Channel as a conditional probability model p(y|x) (Discrete Memoryless Channel, DMC)
- - Channel use and n-length block codes (encoder, decoder, codebook)
- - Message set size M as number of distinct messages to send
- - Transmission rate R = (1/n) log M (bits per channel use)
- - Error probability Pe (probability the decoder output ≠ sent message)
- - Reliability defined asymptotically: Pe → 0 as block length n → ∞
- - Channel capacity as the supremum of all reliably achievable rates
- - Capacity formula for a DMC: C = max\_{p(x)} I(X;Y)
- - Achievability (direct) part of Shannon’s channel coding theorem: any R < C is achievable
- - Converse part of Shannon’s theorem: any R > C is not reliably achievable
- - Optimization over input distributions p(x) is part of finding capacity
- - Operational vs. information-theoretic view of capacity (capacity as an operational maximum equals an information optimization)
- - Additivity for memoryless channels: n uses behave like n independent uses so capacity is a per-use quantity (n uses ≈ n·C total)

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Why can your Wi‑Fi stream video reliably even though the air is noisy, while a slightly higher bitrate suddenly collapses into glitches? Channel capacity is the sharp boundary that explains this: below a certain rate you can drive error probability arbitrarily close to 0 with good codes; above it you cannot, no matter what you do.

TL;DR:

A channel is a probabilistic mapping p(y|x). Its capacity C is the maximum mutual information between input and output over all input distributions: C = max\_{p(x)} I(X;Y) (bits per channel use). Shannon’s noisy-channel coding theorem says: if R < C, there exist codes with vanishing error; if R > C, reliable communication is impossible. For common channels: BSC(p): C = 1 − H₂(p); AWGN with power P and noise N₀/2: C = (1/2) log₂(1 + P/σ²) per real use (or B log₂(1 + SNR) bits/s for bandwidth B).

## What Is Channel Capacity?

## The problem capacity answers

Communication over a noisy medium has two competing forces:

1. 1)**You want to send information quickly** (high rate).
2. 2)**Noise corrupts symbols** (errors accumulate).

Before Shannon, it wasn’t clear whether noise merely *degrades* performance smoothly, or whether there is a crisp limit. Shannon’s insight is that, for a broad class of channels, there is a single number **C** that acts as a boundary.

- •If you transmit at rate **R < C**, then (with sufficiently long block codes) you can make the probability of error as small as you like.
- •If you transmit at rate **R > C**, then no coding scheme can make the error probability go to 0.

Capacity is therefore the **maximum reliable transmission rate**.

## Channels as probabilistic mappings p(y|x)

You already know random variables, entropy, and mutual information. A **channel** formalizes how an input symbol becomes an output symbol **stochastically**:

- •Input alphabet: 𝒳
- •Output alphabet: 𝒴
- •Channel law: **p(y|x)** for each x ∈ 𝒳 and y ∈ 𝒴

A single channel use is:

- •The sender chooses X ∼ p(x)
- •The channel produces Y ∼ p(y|X)

So the induced joint distribution is:

p(x,y) = p(x)p(y|x)

and the output marginal is:

p(y) = ∑ₓ p(x)p(y|x)

This is the exact setting in which mutual information I(X;Y) is defined.

## What “rate” means: bits per channel use

A block code of length n uses the channel n times.

- •Number of messages: M
- •Rate: R = (1/n) log₂ M (bits per channel use)

A communication system is **reliable** if it can send one of M messages with small error probability. For a given channel, capacity C is the supremum of rates R for which reliable communication is possible.

## The single-letter capacity formula

For a **discrete memoryless channel (DMC)**, Shannon’s capacity has a remarkably clean expression:

C = max\_{p(x)} I(X;Y)

where I(X;Y) is computed under p(x,y) = p(x)p(y|x).

This is deep because it turns a problem about *codes* (combinatorial objects over long blocks) into a problem about choosing a good *input distribution* p(x) for a single use of the channel.

## Intuition: why mutual information appears

Mutual information measures how many bits the output reveals about the input:

I(X;Y) = H(X) − H(X|Y)

- •H(X) is how much information you try to inject.
- •H(X|Y) is the uncertainty that remains after observing the noisy output.

So I(X;Y) is the net information delivered through the noise in one channel use. If you can design the input distribution, you can maximize this delivered information.

## A note on units and variants

- •For discrete alphabets: C is in **bits per channel use**.
- •For continuous channels (e.g., AWGN), the same idea holds but with differential entropy and power constraints; the final capacity is still expressed in bits per use or bits/s depending on normalization.

We’ll focus on the conceptual heart: why C = max I(X;Y), what the theorem says, and how to compute C in key examples.

## Core Mechanic 1: Mutual Information as “Information Flow” Through a Channel

## Why we need a maximum over p(x)

The channel law p(y|x) is fixed by physics. But the **input distribution** p(x) is (often) under your control: you can choose how frequently to use each symbol.

Different p(x) produce different joint distributions p(x,y), and therefore different I(X;Y). Some choices waste the channel.

Example intuition:

- •If a channel transmits one symbol perfectly and randomizes the other, you should avoid the randomized symbol.
- •If a channel is symmetric, uniform inputs tend to be optimal.

Capacity captures the best you can do:

C = max\_{p(x)} I(X;Y)

## Expanding I(X;Y) in channel terms

Start from:

I(X;Y) = ∑ₓ∑ᵧ p(x,y) log₂( p(x,y) / (p(x)p(y)) )

Substitute p(x,y) = p(x)p(y|x):

I(X;Y)

= ∑ₓ∑ᵧ p(x)p(y|x) log₂( p(x)p(y|x) / (p(x)p(y)) )

= ∑ₓ∑ᵧ p(x)p(y|x) log₂( p(y|x) / p(y) )

So:

I(X;Y) = 𝔼[ log₂( p(Y|X) / p(Y) ) ]

This is a clean “information gain” form: how surprising Y is under the unconditional distribution p(y), compared to the conditional distribution p(y|x) when you know the input.

## Another useful decomposition: H(Y) − H(Y|X)

Using identities:

I(X;Y) = H(Y) − H(Y|X)

For a fixed channel law:

H(Y|X) = ∑ₓ p(x) H(Y|X=x)

where H(Y|X=x) depends only on the row p(y|x) in the channel transition matrix.

So changing p(x):

- •changes H(Y) (the output spread)
- •changes the weighting in H(Y|X)

Capacity is the best tradeoff: produce outputs that are as distinguishable as possible while accounting for noise.

## Symmetry and why uniform often wins

Many important channels are **symmetric**: roughly, every input symbol “looks the same” from the channel’s perspective up to a permutation of outputs. For such channels:

- •H(Y|X=x) is the same for all x
- •The maximizing p(x) is uniform

This matters because it turns an optimization into a direct formula.

### Example: Binary Symmetric Channel (BSC)

BSC(p): input bit flips with probability p.

Because both inputs are treated identically by noise, uniform p(x=0)=p(x=1)=1/2 is optimal.

We’ll compute C explicitly later.

## Capacity vs. mutual information for a fixed distribution

It’s important to separate two ideas:

- •**I(X;Y)**: how much information *your chosen signaling scheme* sends through.
- •**C**: the best possible I(X;Y) over all signaling schemes.

A channel might have large capacity, but you can still operate far below it if your p(x) is poorly chosen.

## Operational meaning: bits you can make reliable

Capacity is not merely a number you compute from p(y|x). It corresponds to a coding statement.

To appreciate why this is nontrivial, notice:

- •Noise introduces uncertainty each use.
- •Yet coding across many uses can average out uncertainty.
- •The theorem says mutual information is the correct “budget” to compare against rate.

This sets up the next core mechanism: Shannon’s coding theorem, with achievability and converse.

## Core Mechanic 2: Shannon’s Noisy-Channel Coding Theorem (Achievability + Converse)

## The big picture

Shannon’s theorem has two halves:

1. 1)**Achievability**: for any R < C, there exist codes (for large blocklength n) with error probability → 0.
2. 2)**Converse**: for any R > C, error probability is bounded away from 0 for all sufficiently large n (in strong forms, it even tends to 1 under some criteria).

This is why capacity is a **knife-edge**.

We’ll avoid full measure-theoretic proofs, but we will outline the logic, because the *structure* of the argument is as important as the formulas.

## Setup: codes, decoding, and error

A length-n code consists of:

- •Message set: {1,…,M}
- •Encoder: maps message m → codeword xⁿ(m) ∈ 𝒳ⁿ
- •Decoder: maps received yⁿ → estimate m̂

The channel is memoryless:

p(yⁿ|xⁿ) = ∏\_{i=1}^n p(yᵢ|xᵢ)

Error probability (average over messages):

Pₑ = (1/M) ∑\_{m=1}^M Pr[m̂ ≠ m | m sent]

Rate:

R = (1/n) log₂ M

## Why coding across many uses helps: typicality intuition

For large n, sequences behave “typically”:

- •The empirical frequencies of symbols concentrate near their probabilities.
- •The log-likelihood of sequences concentrates near entropy rates.

This is the engine behind compression and also channel coding.

In channel coding, the idea is:

- •Each codeword produces a “cloud” of likely outputs (a typical set conditioned on that codeword).
- •If codewords are far enough apart (in a probabilistic sense), these clouds overlap rarely.

Then decoding can pick the unique codeword whose cloud contains the received output.

## Achievability in one page (random coding)

Shannon’s achievability proof uses **random coding**:

1. 1)Pick an input distribution p(x).
2. 2)Generate M codewords xⁿ(m) i.i.d. ∼ ∏ p(xᵢ).
3. 3)Use a decoding rule like maximum likelihood or typicality decoding.

Then show: if R < I(X;Y) (for that chosen p(x)), the expected error probability (averaged over the random codebook) goes to 0 as n → ∞.

Because the average over random codes is small, there must exist at least one deterministic code with small error.

Finally, maximize over p(x) to get rates up to C = max I(X;Y).

### The key inequality shape

The random coding analysis typically yields a bound like:

Pₑ ≤ 2^{−n·E(R)}

for some positive error exponent E(R) when R < I(X;Y). The exact exponent requires more machinery, but the important message is: below mutual information, overlaps become exponentially rare.

## Converse: why you can’t beat C

The converse often starts from **Fano’s inequality**, relating decoding error to conditional entropy:

H(M|Yⁿ) ≤ 1 + Pₑ log₂ M

Rearrange to connect the message entropy H(M) = log₂ M to mutual information:

I(M;Yⁿ) = H(M) − H(M|Yⁿ)

≥ log₂ M − (1 + Pₑ log₂ M)

So if Pₑ is small, then I(M;Yⁿ) must be close to log₂ M.

Next, use data processing and memorylessness:

M → Xⁿ → Yⁿ

so:

I(M;Yⁿ) ≤ I(Xⁿ;Yⁿ)

and for a memoryless channel:

I(Xⁿ;Yⁿ) ≤ ∑\_{i=1}^n I(Xᵢ;Yᵢ)

Finally, each I(Xᵢ;Yᵢ) ≤ C (by definition of capacity as a max over input distributions). Hence:

I(Xⁿ;Yⁿ) ≤ nC

Combine:

log₂ M ≈ I(M;Yⁿ) ≤ nC

Divide by n:

R = (1/n)log₂ M ≤ C

This shows: if you want vanishing error, your rate cannot exceed capacity.

### A more explicit derivation sketch

Assume Pₑ → 0. Then from Fano:

H(M|Yⁿ) ≤ 1 + Pₑ log₂ M

Compute:

I(M;Yⁿ)

= H(M) − H(M|Yⁿ)

≥ log₂ M − 1 − Pₑ log₂ M

= (1 − Pₑ) log₂ M − 1

But also:

I(M;Yⁿ) ≤ I(Xⁿ;Yⁿ)

For a memoryless channel, one can show (using chain rule and conditioning reduces entropy):

I(Xⁿ;Yⁿ)

= ∑\_{i=1}^n I(Xⁿ;Yᵢ|Y^{i−1})

≤ ∑\_{i=1}^n I(Xᵢ;Yᵢ)

≤ ∑\_{i=1}^n C

= nC

Thus:

(1 − Pₑ) log₂ M − 1 ≤ nC

Divide by n and let n → ∞, Pₑ → 0:

R ≤ C

That’s the converse.

## What the theorem does and does not say

The theorem is asymptotic:

- •It guarantees existence of codes as n → ∞.
- •It does not tell you the best finite-length code for your constraints.

In practice, modern codes (LDPC, Turbo, Polar) approach capacity with manageable complexity, but there is still a gap due to finite blocklength and decoding limits.

This is why “capacity” is simultaneously:

- •a clean theoretical limit
- •a guiding benchmark for real systems

Next we’ll compute C for canonical channels to make the definition concrete.

## Application/Connection: Computing Capacity for Canonical Channels (and Why It Shapes Systems)

## 1) Binary Symmetric Channel (BSC)

### Channel definition

BSC(p): 𝒳 = {0,1}, 𝒴 = {0,1}

- •Pr[Y = X] = 1 − p
- •Pr[Y ≠ X] = p

### Compute I(X;Y) for uniform input

Let X ∼ Bern(1/2). Then Y is also Bern(1/2) by symmetry.

Compute:

I(X;Y) = H(Y) − H(Y|X)

First:

H(Y) = 1 (bit)

Next, Y|X=x is a flip with probability p, so:

H(Y|X=x) = H₂(p)

where H₂(p) = −p log₂ p − (1−p) log₂(1−p).

Therefore:

H(Y|X) = ∑ₓ p(x)H(Y|X=x) = H₂(p)

So:

I(X;Y) = 1 − H₂(p)

For a BSC, uniform input is optimal, hence:

C = 1 − H₂(p)

Interpretation:

- •p=0 ⇒ C=1 (perfect bit pipe)
- •p=1/2 ⇒ C=0 (pure noise)

## 2) Binary Erasure Channel (BEC)

BEC(ε): output is either the input bit or an erasure symbol ⊥.

- •Pr[erasure] = ε
- •Otherwise received correctly.

For uniform input:

- •When not erased, you learn the bit perfectly.
- •When erased, you learn nothing.

So:

C = 1 − ε

This clean form is why BEC is a favorite theoretical sandbox.

## 3) AWGN (Additive White Gaussian Noise) channel

### The model

A standard real-valued AWGN channel use:

Y = X + Z

where Z ∼ 𝒩(0, σ²) independent of X.

To avoid infinite capacity (you could send arbitrarily large amplitudes), impose an average power constraint:

𝔼[X²] ≤ P

### Shannon’s result

The capacity (per real channel use) is:

C = (1/2) log₂(1 + P/σ²)

If you model a continuous-time bandlimited channel of bandwidth B (Hz) with noise spectral density N₀/2, the famous form is:

C = B log₂(1 + SNR) bits/s

where SNR = P/(N₀B) depending on conventions.

### Why Gaussian inputs are optimal

The maximizing input distribution under a variance constraint is Gaussian:

X ∼ 𝒩(0, P)

Reason (high-level): among all distributions with fixed variance, the Gaussian has maximum differential entropy. Since:

I(X;Y) = h(Y) − h(Y|X)

and h(Y|X) = h(Z) is fixed, maximizing I is maximizing h(Y). With Y = X + Z, variance(Y) = P + σ². The Gaussian achieves the largest h(Y) given that variance.

## 4) How capacity shapes system design

### Capacity as a benchmark

Engineers compare practical schemes to capacity:

- •Modulation + coding yields a spectral efficiency (bits/s/Hz).
- •Shannon capacity gives an upper bound.

If a design is far from capacity, you ask:

- •Are we power-limited or bandwidth-limited?
- •Is the code too short?
- •Is decoding complexity constrained?

### The “waterfall” phenomenon

Modern codes often show a sharp transition: as SNR increases past a threshold, BER suddenly drops dramatically. This mirrors the capacity boundary (though shifted by finite-length effects).

### Capacity per unit cost and constraints

Real channels have constraints beyond average power:

- •peak power constraints
- •discrete constellations (QAM)
- •fading (random p(y|x,h))

Capacity generalizes, but the core idea remains: maximize mutual information subject to constraints.

## 5) A compact comparison table

| Channel | Model | Constraint | Capacity C | Optimal p(x) |
| --- | --- | --- | --- | --- |
| BSC(p) | bit flips | none | 1 − H₂(p) | uniform |
| BEC(ε) | erasures | none | 1 − ε | uniform |
| AWGN | Y=X+Z, Z∼𝒩(0,σ²) | 𝔼[X²]≤P | (1/2)log₂(1+P/σ²) | Gaussian |

## 6) Connecting back to the definition

In every case:

1. 1)You compute I(X;Y) under a chosen input distribution.
2. 2)You optimize over p(x) (or over distributions satisfying constraints).
3. 3)The maximum is capacity.

Shannon’s theorem then turns that maximum into an operational promise: **the channel can be made to behave like an almost noiseless bit pipe of rate C**, if you code across long blocks.

## Worked Examples (3)

### Compute the capacity of a BSC(p) and interpret edge cases

Channel: BSC with crossover probability p. Find C and sanity-check p=0 and p=1/2.

1. Use the capacity formula for a DMC:

   C = max\_{p(x)} I(X;Y).
2. For a BSC, by symmetry, the maximizing input is uniform:

   Pr[X=0]=Pr[X=1]=1/2.
3. Compute I(X;Y)=H(Y)−H(Y|X).
4. Find H(Y): with uniform input and symmetric flipping,

   Pr[Y=0]=Pr[Y=1]=1/2 ⇒ H(Y)=1.
5. Find H(Y|X): for any x, Y is flipped with probability p, so

   H(Y|X=x)=H₂(p).

   Because this does not depend on x,

   H(Y|X)=∑ₓ p(x)H(Y|X=x)=H₂(p).
6. Therefore

   I(X;Y)=1−H₂(p).
7. Conclude capacity:

   C = 1 − H₂(p) bits/use.
8. Edge checks:

   - •If p=0, then H₂(0)=0 ⇒ C=1 (a perfect bit each use).
   - •If p=1/2, then H₂(1/2)=1 ⇒ C=0 (output is independent of input, no reliable bits).

**Insight:** Capacity falls as noise increases, but not linearly; the binary entropy H₂(p) captures how uncertainty from flips eats away at the 1 bit/use available in a noiseless binary channel.

### AWGN capacity per real channel use from I(X;Y)=h(Y)−h(Y|X)

Real AWGN channel: Y = X + Z with Z ∼ 𝒩(0, σ²). Constraint: 𝔼[X²] ≤ P. Derive C = (1/2)log₂(1+P/σ²).

1. Start from mutual information:

   I(X;Y)=h(Y)−h(Y|X).
2. Given Y=X+Z and Z independent of X,

   Y|X=x is just x+Z, so its differential entropy equals that of Z:

   h(Y|X)=h(Z).
3. So maximizing I(X;Y) over inputs subject to 𝔼[X²]≤P is equivalent to maximizing h(Y) because h(Z) is fixed:

   max I(X;Y) = max h(Y) − h(Z).
4. Compute variance of Y:

   Var(Y)=Var(X+Z)=Var(X)+Var(Z) (independence)

   = 𝔼[X²] + σ² ≤ P + σ².
5. Use the maximum-entropy fact: among all real-valued distributions with a fixed variance, the Gaussian has the largest differential entropy.
6. So choose X ∼ 𝒩(0,P). Then Y is Gaussian with variance P+σ²:

   Y ∼ 𝒩(0, P+σ²).
7. Compute differential entropies (in bits):

   h(𝒩(0, s²)) = (1/2) log₂(2πe s²).
8. Thus:

   h(Y) = (1/2)log₂(2πe(P+σ²))

   h(Z) = (1/2)log₂(2πeσ²).
9. Subtract:

   I(X;Y) = h(Y) − h(Z)

   = (1/2)log₂(2πe(P+σ²)) − (1/2)log₂(2πeσ²)

   = (1/2)log₂((P+σ²)/σ²)

   = (1/2)log₂(1 + P/σ²).
10. Because Gaussian X is optimal under the power constraint, capacity is:

    C = (1/2)log₂(1 + P/σ²) bits per real channel use.

**Insight:** For AWGN, noise contributes a fixed entropy h(Z). The only lever is how “spread out” the output Y can be under the power constraint, and Gaussian signaling maximizes that spread in the entropy sense.

### A small DMC capacity computation by direct maximization (2×2 asymmetric channel)

Let 𝒳={0,1}, 𝒴={0,1} with transition law:

Pr[Y=1|X=0]=0.1, Pr[Y=1|X=1]=0.6.

Compute I(X;Y) as a function of q=Pr[X=1], then (numerically) find the maximizing q and capacity.

1. Parameterize the input distribution by q:

   Pr[X=1]=q, Pr[X=0]=1−q.
2. Compute the output probability of Y=1:

   Pr[Y=1] = Pr[Y=1|X=0]Pr[X=0] + Pr[Y=1|X=1]Pr[X=1]

   = 0.1(1−q) + 0.6q

   = 0.1 + 0.5q.

   Let r = 0.1 + 0.5q.
3. Compute H(Y):

   H(Y)=H₂(r).
4. Compute H(Y|X):

   H(Y|X)= (1−q)H₂(0.1) + qH₂(0.6).
5. Thus mutual information is:

   I(q) = H₂(0.1+0.5q) − (1−q)H₂(0.1) − qH₂(0.6).
6. Compute constants:

   H₂(0.1) ≈ −0.1log₂0.1 −0.9log₂0.9 ≈ 0.469.

   H₂(0.6) ≈ 0.971.
7. Now evaluate I(q) at a few q values to locate the maximum:

   - •q=0 ⇒ r=0.1 ⇒ H₂(r)=0.469 ⇒ I(0)=0.469−0.469=0.
   - •q=1 ⇒ r=0.6 ⇒ H₂(r)=0.971 ⇒ I(1)=0.971−0.971=0.
   - •q=0.5 ⇒ r=0.35 ⇒ H₂(0.35)≈0.934.

   H(Y|X)=0.5·0.469 + 0.5·0.971=0.720.

   I(0.5)=0.934−0.720=0.214 bits/use.

   - •q=0.4 ⇒ r=0.1+0.2=0.3 ⇒ H₂(0.3)≈0.881.

   H(Y|X)=0.6·0.469 + 0.4·0.971=0.670.

   I(0.4)=0.881−0.670=0.211.

   - •q=0.6 ⇒ r=0.1+0.3=0.4 ⇒ H₂(0.4)≈0.971.

   H(Y|X)=0.4·0.469 + 0.6·0.971=0.770.

   I(0.6)=0.971−0.770=0.201.
8. The maximum from these samples is near q≈0.5 with I≈0.214 bits/use.

   So capacity is approximately:

   C ≈ 0.214 bits/use, achieved near q≈0.5.

**Insight:** Unlike symmetric channels, an asymmetric channel may require a non-uniform input to maximize I(X;Y). Here, extremes q=0 or 1 convey zero information because the output distribution becomes fixed; mixing inputs makes outputs more distinguishable.

## Key Takeaways

- ✓

  A channel is specified by its transition law p(y|x); it is a probabilistic mapping from inputs to outputs.
- ✓

  Channel capacity C is the maximum reliable rate (bits per channel use): C = max\_{p(x)} I(X;Y) for a DMC.
- ✓

  Mutual information can be written as I(X;Y)=H(Y)−H(Y|X)=𝔼[log₂(p(Y|X)/p(Y))], making its “information flow” meaning explicit.
- ✓

  Shannon’s noisy-channel coding theorem: if R < C, there exist codes with Pₑ → 0; if R > C, reliable communication is impossible.
- ✓

  Achievability is shown via random coding and typicality/packing arguments; the converse uses Fano’s inequality plus information inequalities to upper-bound rate by C.
- ✓

  For symmetric channels (e.g., BSC, BEC), uniform inputs achieve capacity; symmetry removes the need for optimization.
- ✓

  Canonical capacities: BSC(p): 1−H₂(p); BEC(ε): 1−ε; AWGN (power P, noise σ²): (1/2)log₂(1+P/σ²) per real use.

## Common Mistakes

- ✗

  Confusing I(X;Y) for a particular input distribution with capacity C; capacity requires maximizing over p(x) (and respecting constraints like power).
- ✗

  Thinking capacity is a guarantee at finite blocklength: Shannon’s theorem is asymptotic; finite-length systems need overhead and have nonzero error.
- ✗

  Forgetting constraints in continuous channels: without an average/peak power constraint, an AWGN channel would have unbounded capacity.
- ✗

  Misinterpreting “bits per channel use” vs “bits per second”: converting requires accounting for symbol rate, bandwidth, and the channel model normalization.

## Practice

easy

BEC(ε): Show that C = 1 − ε bits/use by computing I(X;Y) for uniform X and arguing optimality.

**Hint:** Use I(X;Y)=H(X)−H(X|Y). When Y is not erased, X is known exactly; when erased, X remains uniform.

Show solution

Let X ∼ Bern(1/2) so H(X)=1. For BEC(ε), Y ∈ {0,1,⊥}. If Y∈{0,1}, then X is determined ⇒ H(X|Y∈{0,1})=0. If Y=⊥ (probability ε), then X is still Bern(1/2) ⇒ H(X|Y=⊥)=1. Thus:

H(X|Y)= (1−ε)·0 + ε·1 = ε.

So I(X;Y)=H(X)−H(X|Y)=1−ε. The BEC is symmetric, so uniform X is capacity-achieving ⇒ C=1−ε.

medium

Consider a BSC with p=0.11. Compute C numerically (in bits/use).

**Hint:** Use C = 1 − H₂(p). Compute H₂(0.11) = −0.11log₂0.11 −0.89log₂0.89.

Show solution

H₂(0.11)=−0.11log₂(0.11)−0.89log₂(0.89).

log₂(0.11)≈−3.184, so −0.11log₂(0.11)≈0.350.

log₂(0.89)≈−0.168, so −0.89log₂(0.89)≈0.150.

Thus H₂(0.11)≈0.500 and C≈1−0.500=0.500 bits/use (about 0.50).

hard

Real AWGN: Y = X + Z, Z∼𝒩(0,1). Power constraint 𝔼[X²]≤9. Compute capacity per real channel use and compare to the noiseless 1-bit BSC intuition.

**Hint:** Use C = (1/2)log₂(1 + P/σ²) with σ²=1, P=9.

Show solution

C=(1/2)log₂(1+9/1)=(1/2)log₂(10).

log₂(10)≈3.322, so C≈(1/2)·3.322≈1.661 bits per real channel use.

This can exceed 1 bit/use because the AWGN input is not restricted to binary symbols; with higher SNR and continuous amplitudes, one channel use can convey more than one bit reliably (with appropriate coding and modulation), consistent with Shannon’s theorem.

## Connections

Related nodes:

- •[Mutual Information](/tech-tree/mutual-information/)
- •[Entropy](/tech-tree/entropy/)
- •[KL Divergence](/tech-tree/kl-divergence/)
- •[Typical Sets and AEP](/tech-tree/typical-sets-aep/)
- •[Error-Correcting Codes](/tech-tree/error-correcting-codes/)
- •[AWGN Channel Model](/tech-tree/awgn-channel/)
- •[Fano’s Inequality](/tech-tree/fanos-inequality/)
- •[Data Processing Inequality](/tech-tree/data-processing-inequality/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
