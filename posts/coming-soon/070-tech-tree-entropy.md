---
title: Entropy
description: Measure of uncertainty/information content. H(X) = -sum p log p.
date: '2026-07-01'
scheduled: '2026-09-08'
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
inspiration_url: https://templeton.host/tech-tree/entropy/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/entropy/](https://templeton.host/tech-tree/entropy/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Entropy

Information TheoryDifficulty: ★★★☆☆Depth: 6Unlocks: 14

Measure of uncertainty/information content. H(X) = -sum p log p.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Surprisal (information content) of a single outcome: -log p(x)
- -Entropy as the expected surprisal (average information/uncertainty) of a random variable

## Key Symbols & Notation

H(X) - entropy of random variable XI(x) - surprisal of outcome x, I(x) = -log p(x)

## Essential Relationships

- -H(X) = E[I(X)] = - sum\_x p(x) log p(x) (entropy equals the expectation of surprisal)

## Prerequisites (2)

[Expected Value5 atoms](/tech-tree/expected-value/)[Common Distributions6 atoms](/tech-tree/common-distributions/)

## Unlocks (7)

[KL Divergencelvl 4](/tech-tree/kl-divergence/)[Mutual Informationlvl 3](/tech-tree/mutual-information/)[Cross-Entropylvl 4](/tech-tree/cross-entropy/)[Decision Treeslvl 4](/tech-tree/decision-trees/)[Rate-Distortion Theorylvl 5](/tech-tree/rate-distortion/)[Channel Capacitylvl 5](/tech-tree/channel-capacity/)[Information-Theoretic Boundslvl 5](/tech-tree/information-theoretic-lower-bounds/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[Tribal KnowledgeBusiness

Tribal knowledge is high-entropy information by definition - it carries high surprise value precisely because it is rare, undocumented, and not redundant with any written source. Understanding Shannon entropy clarifies why tribal knowledge is disproportionately valuable per bit](/business/tribal-knowledge/)

Advanced Learning Details

### Graph Position

45

Depth Cost

14

Fan-Out (ROI)

8

Bottleneck Score

6

Chain Length

### Cognitive Load

5

Atomic Elements

39

Total Elements

L2

Percentile Level

L3

Atomic Level

### All Concepts (17)

- - Entropy as a measure of uncertainty/information content of a random variable
- - Self-information (surprisal) of an outcome: i(x) = -log p(x)
- - Entropy as the expected self-information: H(X) = E[i(X)] = -sum\_x p(x) log p(x)
- - Entropy depends only on the probability distribution of X (not on the numeric labels of outcomes)
- - Units of information determined by log base (bits for log\_2, nats for ln)
- - Entropy of a deterministic variable is zero
- - Maximum entropy for a given alphabet occurs at the uniform distribution
- - Range/bound: 0 ≤ H(X) ≤ log |X| (where |X| is the number of possible outcomes)
- - Joint entropy H(X,Y) as uncertainty of a pair of variables
- - Conditional entropy H(X|Y) as remaining uncertainty about X given Y
- - Chain rule for entropy: total joint uncertainty decomposes into marginal + conditional
- - Subadditivity (and additivity in special case): H(X,Y) ≤ H(X) + H(Y), with equality if X and Y are independent
- - Mutual information I(X;Y) as reduction in uncertainty about X due to knowledge of Y
- - Mutual information non-negativity (I(X;Y) ≥ 0)
- - Entropy as a property of distributions relevant to optimal coding (average minimum code length) - coding interpretation
- - Permutation invariance: relabeling outcomes does not change entropy
- - Concavity of entropy as a function of the probability distribution (mixing increases entropy)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Why does a fair coin flip feel like “one bit” of uncertainty, while a coin that lands heads 99% of the time feels like almost none? Entropy is the mathematical tool that turns that intuition into a precise number—and it becomes the currency for compression, prediction, and learning.

TL;DR:

Entropy H(X) measures the average uncertainty (average “surprise”) of a random variable X. For discrete X with probabilities p(x), surprisal is I(x) = −log p(x), and entropy is the expected surprisal: H(X) = E[I(X)] = −∑ₓ p(x) log p(x). The log base sets the unit (base 2 → bits, base e → nats). Entropy is maximized by the uniform distribution and minimized (0) when outcomes are certain.

## What Is Entropy?

### Why we need a new quantity (motivation)

Probability tells you what tends to happen. But often you want a single number answering a different question:

- •**How uncertain am I before I observe X?**
- •**How much information do I gain when I learn the outcome?**
- •**How many bits do I need (on average) to encode outcomes of X?**

A single event can be “surprising” or “unsurprising.” If something was already likely, learning it doesn’t teach you much. If it was unlikely, you learn a lot.

Entropy formalizes this by:

1) defining **surprisal** for one outcome, then

2) averaging surprisal according to the distribution.

### Surprisal: information content of one outcome

Let X be a discrete random variable taking values x with probability p(x).

We define the **surprisal** (also called self-information) of outcome x as:

I(x) = −log p(x)

Intuition:

- •If p(x) is large (close to 1), then log p(x) is close to 0, so I(x) is close to 0 ⇒ not surprising.
- •If p(x) is small, log p(x) is very negative, so −log p(x) is large ⇒ very surprising.

The **log base** chooses units:

- •log₂ ⇒ units are **bits**
- •ln ⇒ units are **nats**
- •log₁₀ ⇒ units are **hartleys/dits**

Changing base just rescales:

log\_b p = (log\_a p) / (log\_a b)

### Entropy: expected surprisal

Surprisal is about one outcome. Entropy is about the whole random variable.

Definition (discrete entropy):

H(X) = E[I(X)]

= ∑ₓ p(x) I(x)

= ∑ₓ p(x) (−log p(x))

= −∑ₓ p(x) log p(x)

This is the canonical formula you see in information theory.

### Intuition check with extremes

- •**Certain outcome:** Suppose P(X = a) = 1. Then

H(X) = −1 · log 1 = 0

Zero uncertainty, zero information gained by observing.

- •**Uniform over n outcomes:** If p(x) = 1/n for each outcome,

H(X) = −∑ₓ (1/n) log(1/n)

= −n · (1/n) · (−log n)

= log n

This grows as the number of equally likely possibilities grows.

### What entropy is (and is not)

Entropy is:

- •a measure of **uncertainty** in X before observing it
- •a measure of **average information** you learn by observing X
- •the theoretical limit (in bits/symbol) for **lossless compression** of outcomes from X

Entropy is not:

- •“randomness” in the colloquial sense for a single sequence (entropy is about a distribution)
- •a guarantee that any one outcome is surprising (it’s an average)

Keep the mental model: **entropy is average surprise**.

## Core Mechanic 1: Surprisal and the Log

### Why does information grow like a log?

If an outcome has probability p, the “number of yes/no questions” you need to identify it (in the best case) behaves like log₂(1/p). This is because each binary question can cut the remaining possibilities roughly in half.

The log is the unique (up to scaling) function that turns multiplication into addition:

- •Independent probabilities multiply.
- •Independent information should add.

Concretely, if two independent events happen: A with p(A) and B with p(B), then:

p(A ∩ B) = p(A) p(B)

Surprisal of the joint event should be:

I(A ∩ B) = −log(p(A)p(B))

= −(log p(A) + log p(B))

= (−log p(A)) + (−log p(B))

= I(A) + I(B)

So the −log choice makes “information from independent events” add up cleanly.

### Practical meanings of surprisal

If we use log₂:

- •p(x) = 1/2 ⇒ I(x) = 1 bit
- •p(x) = 1/4 ⇒ I(x) = 2 bits
- •p(x) = 1/8 ⇒ I(x) = 3 bits

Each halving of probability adds one bit of surprisal.

### From surprisal to entropy: averaging with expected value

You already know expected value:

E[g(X)] = ∑ₓ p(x) g(x)

Entropy is simply that with g(x) = −log p(x):

H(X) = E[−log p(X)]

A key pacing idea: entropy is not mysterious new machinery—it’s “expected value” applied to the random variable “surprisal.”

### Units and interpretation (bits vs nats)

If you compute with log₂, H(X) is in bits.

If you compute with ln, H(X) is in nats.

Conversion:

H\_bits(X) = H\_nats(X) / ln 2

This matters because in machine learning, losses often use ln (because calculus is cleaner), but we still conceptually speak in bits.

### The shape of uncertainty for a Bernoulli variable

Let X ∈ {0,1} with P(X=1)=p and P(X=0)=1−p.

H(X) = −p log p − (1−p) log(1−p)

This function has a distinctive shape:

- •H(X)=0 at p=0 or p=1 (certainty)
- •Maximum at p=1/2 (most uncertain)

If logs are base 2, the maximum is 1 bit.

### A small table: how surprisal behaves

| Probability p(x) | Surprisal I(x)=−log₂ p(x) | Interpretation |
| --- | --- | --- |
| 1 | 0 | No surprise |
| 1/2 | 1 | One bit of info |
| 1/4 | 2 | Two bits |
| 0.1 | ≈ 3.322 | More than 3 yes/no questions on average |
| 0.01 | ≈ 6.644 | Very surprising |

Takeaway: surprisal is a smooth measure that grows rapidly as p(x) shrinks.

## Core Mechanic 2: Properties of Entropy (and Why They Matter)

Entropy is useful partly because it obeys clean, predictable rules. These rules let you reason about coding, uncertainty, and learning systems without re-deriving everything.

### Property A: Non-negativity

Because 0 ≤ p(x) ≤ 1, we have log p(x) ≤ 0, hence −p(x) log p(x) ≥ 0 for each term.

So:

H(X) = −∑ₓ p(x) log p(x) ≥ 0

Entropy can’t be negative.

### Property B: Entropy is 0 iff X is certain

If X always takes one value with probability 1, then H(X)=0.

Conversely, if H(X)=0, all terms −p(x) log p(x) must be 0. For any p(x) in (0,1), log p(x) < 0 and the term is positive, so the only way all terms vanish is when one outcome has probability 1 and the rest 0.

So entropy captures “no uncertainty.”

### Property C: Maximum entropy for fixed support is uniform

Suppose X can take n outcomes.

- •The maximum of H(X) occurs when p(x)=1/n for all x.
- •The maximum value is H(X)=log n.

Why this matters: if you know only that there are n possible outcomes, “most uncertain” means “assume uniform.”

### Property D: Chain rule (entropy of joint variables)

Let (X,Y) be a pair of discrete random variables.

The chain rule says:

H(X,Y) = H(X) + H(Y|X)

Interpretation:

- •First you learn X: cost H(X)
- •Then you learn Y given X: extra cost H(Y|X)

This mirrors how you might actually encode (X,Y): encode X, then encode Y using a code adapted to the conditional distribution P(Y|X).

A brief derivation sketch (using definitions):

H(X,Y)

= −∑ₓ ∑ᵧ p(x,y) log p(x,y)

= −∑ₓ ∑ᵧ p(x,y) log( p(x) p(y|x) )

= −∑ₓ ∑ᵧ p(x,y) [log p(x) + log p(y|x)]

= −∑ₓ ∑ᵧ p(x,y) log p(x) − ∑ₓ ∑ᵧ p(x,y) log p(y|x)

For the first term:

−∑ₓ ∑ᵧ p(x,y) log p(x)

= −∑ₓ log p(x) ∑ᵧ p(x,y)

= −∑ₓ log p(x) p(x)

= H(X)

For the second term, by definition that is H(Y|X).

### Property E: Conditioning reduces entropy

You should expect that knowing more can’t increase uncertainty:

H(X|Y) ≤ H(X)

Interpretation: if you observe Y, you can only become more certain (or equally uncertain) about X.

This idea is a cornerstone for later nodes like mutual information:

I(X;Y) = H(X) − H(X|Y)

### Property F: Entropy and “effective number of outcomes”

If H(X)=log n, it behaves like you have n equally likely outcomes.

This motivates the notion of “perplexity” used in language modeling:

perplexity(X) = 2^{H\_bits(X)}

If H=10 bits, perplexity is 1024: it’s as if, on average, there are ~1024 equally plausible next tokens.

### When entropy is the right tool

Entropy answers questions like:

- •“How unpredictable is this source?”
- •“How many bits/symbol do I need to encode it?”
- •“How much does observing Y reduce uncertainty about X?”

And importantly, it does so with algebraic rules that compose well across systems.

## Application/Connection: Compression, Learning, and Decision-Making

### Entropy as a limit for lossless compression

Imagine X generates symbols with distribution p(x). If you design an optimal prefix-free code (e.g., Huffman coding), the expected code length L̄ satisfies:

H(X) ≤ L̄ < H(X) + 1

Interpretation:

- •You can’t beat entropy on average (without loss).
- •You can get within 1 bit/symbol of it with classical coding methods.

So entropy is not just “an abstract uncertainty”—it’s a concrete benchmark for storage and transmission.

### Why entropy shows up in machine learning losses

In classification, we often model a distribution q over labels given features, and reality follows p. The **cross-entropy**:

H(p,q) = −∑ₓ p(x) log q(x)

is the expected surprisal when you use q but the world is p.

This decomposes as:

H(p,q) = H(p) + KL(p‖q)

So minimizing cross-entropy (common in neural nets) is equivalent to minimizing KL divergence because H(p) is fixed.

Even if you don’t yet know KL deeply, you can see the story:

- •entropy H(p): irreducible uncertainty in labels
- •extra penalty: mismatch between your model and reality

### Decision trees: entropy as an impurity measure

Decision trees choose splits that reduce uncertainty about the label Y.

At a node, compute entropy of labels:

H(Y) = −∑ᵧ p(y) log p(y)

After splitting on feature X, you get conditional entropy:

H(Y|X) = ∑ₓ p(x) H(Y|X=x)

Information gain is:

IG = H(Y) − H(Y|X)

So trees pick the feature that maximizes IG (largest reduction in label uncertainty).

### Entropy as “how many questions remain?”

If you use log₂, entropy is measured in bits, and a bit is literally one yes/no question.

So H(X)=3 bits means: with optimal questioning, you need about 3 binary questions on average to identify X.

This mental model helps you sanity-check:

- •Doubling the number of equally likely possibilities adds 1 bit.
- •When one outcome dominates, the average number of questions drops sharply.

### Connections you’re about to unlock

Once entropy feels natural, several powerful concepts become almost inevitable:

- •**KL divergence:** measures the extra surprisal from using the wrong distribution.
- •**Mutual information:** the reduction in entropy from knowing another variable.
- •**Cross-entropy:** the training objective for probabilistic classifiers.
- •**Rate-distortion theory:** how entropy changes when you allow controlled loss.

Entropy is the hub: it’s the “energy unit” in the economy of information.

## Worked Examples (3)

### Entropy of a Bernoulli(p): why the maximum is at p = 1/2

Let X ∈ {0,1} with P(X=1)=p and P(X=0)=1−p. Compute H(X) (base 2), and verify it is maximized at p=1/2.

1. Start from the definition:

   H(X) = −∑ₓ p(x) log₂ p(x)
2. Plug in the two outcomes:

   H(p) = −p log₂ p − (1−p) log₂(1−p)
3. Check a few values for intuition:

   - •p=0 ⇒ H=0
   - •p=1 ⇒ H=0
   - •p=1/2 ⇒ H = −(1/2)log₂(1/2) − (1/2)log₂(1/2)

   = −(1/2)(−1) − (1/2)(−1)

   = 1 bit
4. To verify the maximum location, it is easier to differentiate using ln and convert later.

   Define h(p) = −p ln p − (1−p) ln(1−p). (This is entropy in nats.)
5. Differentiate:

   ∂h/∂p = −(ln p + 1) − [−ln(1−p) − 1]

   = −ln p − 1 + ln(1−p) + 1

   = ln((1−p)/p)
6. Set derivative to 0:

   ln((1−p)/p) = 0

   ⇒ (1−p)/p = 1

   ⇒ 1−p = p

   ⇒ p = 1/2
7. Second derivative check:

   ∂²h/∂p² = ∂/∂p [ln(1−p) − ln p]

   = −1/(1−p) − 1/p

   < 0 for p ∈ (0,1)

   So p=1/2 is a maximum.
8. Convert back to bits if needed:

   H\_bits(p) = h(p) / ln 2, and at p=1/2 we get 1 bit.

**Insight:** Entropy is maximized when outcomes are as balanced as possible. For a binary variable, “most uncertain” means “fair coin,” giving exactly 1 bit of average information.

### Entropy of a 4-symbol source and the ‘effective number of outcomes’

Let X take values {A,B,C,D} with probabilities p = (1/2, 1/4, 1/8, 1/8). Compute H(X) in bits and compute perplexity 2^{H(X)}.

1. Write the entropy:

   H(X) = −∑ p(x) log₂ p(x)
2. Compute each surprisal:

   I(A)=−log₂(1/2)=1

   I(B)=−log₂(1/4)=2

   I(C)=−log₂(1/8)=3

   I(D)=−log₂(1/8)=3
3. Average them with probabilities:

   H(X) = (1/2)·1 + (1/4)·2 + (1/8)·3 + (1/8)·3
4. Compute:

   (1/2)·1 = 0.5

   (1/4)·2 = 0.5

   (1/8)·3 = 0.375

   (1/8)·3 = 0.375
5. Sum:

   H(X) = 0.5 + 0.5 + 0.375 + 0.375 = 1.75 bits
6. Compute perplexity:

   perplexity = 2^{H} = 2^{1.75}

   = 2^{1} · 2^{0.75}

   = 2 · 2^{3/4}

   ≈ 2 · 1.6818

   ≈ 3.36

**Insight:** Although there are 4 possible outcomes, the distribution is skewed, so uncertainty behaves like having only ~3.36 equally likely outcomes.

### Entropy reduction after observing a feature (information gain preview)

A dataset has a binary label Y with P(Y=1)=3/4 and P(Y=0)=1/4. A binary feature X splits the data: when X=0 (prob 1/2), P(Y=1|X=0)=1; when X=1 (prob 1/2), P(Y=1|X=1)=1/2. Compute H(Y), H(Y|X), and the entropy reduction H(Y)−H(Y|X) (base 2).

1. Compute the initial label entropy:

   H(Y) = −(3/4)log₂(3/4) − (1/4)log₂(1/4)
2. Use known logs:

   log₂(1/4)=−2

   log₂(3/4)=log₂ 3 − log₂ 4 = log₂ 3 − 2 ≈ 1.585 − 2 = −0.415
3. Plug in:

   H(Y) = −(3/4)(−0.415) − (1/4)(−2)

   = (3/4)(0.415) + (1/4)(2)

   ≈ 0.311 + 0.5

   ≈ 0.811 bits
4. Compute conditional entropy via the split:

   H(Y|X) = ∑ₓ p(x) H(Y|X=x)

   = (1/2)H(Y|X=0) + (1/2)H(Y|X=1)
5. For X=0, P(Y=1|X=0)=1 so the label is certain:

   H(Y|X=0)=0
6. For X=1, P(Y=1|X=1)=1/2 so it is a fair coin:

   H(Y|X=1)=1 bit
7. Therefore:

   H(Y|X) = (1/2)·0 + (1/2)·1 = 0.5 bits
8. Entropy reduction (information gain idea):

   H(Y) − H(Y|X) ≈ 0.811 − 0.5 = 0.311 bits

**Insight:** A feature is useful when it makes the label distribution more certain. Here, X removes about 0.311 bits of uncertainty about Y on average—exactly the quantity decision trees try to maximize.

## Key Takeaways

- ✓

  Surprisal measures information in a single outcome: I(x) = −log p(x). Rare events carry more information.
- ✓

  Entropy is average surprisal: H(X) = E[−log p(X)] = −∑ₓ p(x) log p(x).
- ✓

  The log base sets units: log₂ → bits, ln → nats; changing base rescales by a constant factor.
- ✓

  H(X) ≥ 0, and H(X)=0 exactly when X is deterministic (no uncertainty).
- ✓

  For a fixed number of outcomes n, entropy is maximized by the uniform distribution and equals log n.
- ✓

  The chain rule H(X,Y)=H(X)+H(Y|X) explains how uncertainty composes across multiple variables.
- ✓

  Conditioning reduces uncertainty: H(X|Y) ≤ H(X), paving the way to mutual information.
- ✓

  In coding and ML, entropy is a benchmark: it is the lower bound on average lossless code length and a building block for cross-entropy/KL losses.

## Common Mistakes

- ✗

  Forgetting the negative sign: ∑ p log p is ≤ 0, so entropy is defined with a minus to make it nonnegative.
- ✗

  Mixing log bases mid-calculation (e.g., using ln in one step and log₂ in another) and getting inconsistent units.
- ✗

  Interpreting entropy as a property of a particular observed sequence rather than of the underlying probability distribution.
- ✗

  Confusing entropy H(X) with cross-entropy H(p,q): entropy uses the true p inside both p and log; cross-entropy uses p outside and q inside the log.

## Practice

easy

Compute the entropy (in bits) of a fair six-sided die roll. Then compute the entropy if the die is loaded so that P(1)=1/2 and P(2)=P(3)=P(4)=P(5)=P(6)=1/10.

**Hint:** Uniform over n outcomes has H=log₂ n. For the loaded die, compute −∑ p log₂ p and reuse that −log₂(1/2)=1 and −log₂(1/10)=log₂ 10 ≈ 3.322.

Show solution

Fair die: H = log₂ 6 ≈ 2.585 bits.

Loaded die:

H = −(1/2)log₂(1/2) − 5·(1/10)log₂(1/10)

= (1/2)·1 + 5·(1/10)·log₂ 10

= 0.5 + 0.5·3.322

≈ 0.5 + 1.661

≈ 2.161 bits.

medium

Let X take values {a,b,c} with probabilities (1/2, 1/3, 1/6). Compute H(X) in bits.

**Hint:** Compute each term p(x)·(−log₂ p(x)). You may use log₂ 3 ≈ 1.585 and log₂ 6 = log₂(2·3)=1+log₂ 3 ≈ 2.585.

Show solution

H(X)= −(1/2)log₂(1/2) − (1/3)log₂(1/3) − (1/6)log₂(1/6)

Compute surprisals:

−log₂(1/2)=1

−log₂(1/3)=log₂ 3 ≈ 1.585

−log₂(1/6)=log₂ 6 ≈ 2.585

Average:

H ≈ (1/2)·1 + (1/3)·1.585 + (1/6)·2.585

≈ 0.5 + 0.528 + 0.431

≈ 1.459 bits.

medium

Suppose X and Y are independent and each is a fair coin flip. Compute H(X), H(Y), and H(X,Y). Verify the chain rule H(X,Y)=H(X)+H(Y|X).

**Hint:** Fair coin entropy is 1 bit. Independence implies H(Y|X)=H(Y). Joint distribution has 4 equally likely outcomes.

Show solution

H(X)=1 bit and H(Y)=1 bit.

Because X and Y are independent, knowing X does not change uncertainty about Y, so H(Y|X)=H(Y)=1 bit.

The pair (X,Y) has 4 equally likely outcomes, so:

H(X,Y)=log₂ 4 = 2 bits.

Chain rule check:

H(X)+H(Y|X) = 1 + 1 = 2 = H(X,Y).

## Connections

Next nodes you can study:

- •[KL Divergence](/tech-tree/kl-divergence/) — measures extra average surprisal from using the wrong distribution.
- •[Cross-Entropy](/tech-tree/cross-entropy/) — expected surprisal under a model q when reality is p; standard classification loss.
- •[Mutual Information](/tech-tree/mutual-information/) — reduction in uncertainty: I(X;Y)=H(X)−H(X|Y).
- •[Decision Trees](/tech-tree/decision-trees/) — information gain uses entropy reduction to pick splits.
- •[Rate-Distortion Theory](/tech-tree/rate-distortion/) — compression when some distortion is allowed; entropy is the baseline.

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
