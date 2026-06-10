---
title: Softmax and Logits
description: The softmax function converts raw model outputs (logits) into a probability distribution over classes, and is central to attention weight computation and classification losses. Familiarity with numerical stability tricks (log-sum-exp) and interpreting logits/probabilities is included.
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
permalink: /tech-tree/softmax-and-logits/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Softmax and Logits

Machine LearningDifficulty: ★★★☆☆Depth: 0Unlocks: 2

The softmax function converts raw model outputs (logits) into a probability distribution over classes, and is central to attention weight computation and classification losses. Familiarity with numerical stability tricks (log-sum-exp) and interpreting logits/probabilities is included.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Logits: model outputs as unnormalized real-valued scores for each class
- -Softmax: exponentiate logits and normalize to produce a probability distribution
- -Numerical-stability (log-sum-exp): compute softmax by subtracting max logit before exponentiating to avoid overflow/underflow

## Key Symbols & Notation

z (vector of logits)

## Essential Relationships

- -Softmax(z) yields nonnegative values that sum to 1 and depends only on differences between logits (adding a constant to all z\_i does not change the result)

## Unlocks (2)

[Sequence Masking (causal and padding masks)lvl 4](/tech-tree/sequence-masking/)[Transformerslvl 5](/tech-tree/transformers/)

Advanced Learning Details

### Graph Position

5

Depth Cost

2

Fan-Out (ROI)

1

Bottleneck Score

0

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

### All Concepts (11)

- - Logits: raw model outputs / pre-softmax scores (real-valued numbers produced by a model for each class or candidate)
- - Softmax function: mapping a vector of logits to a probability distribution via exponentiation and normalization
- - Probability simplex: softmax outputs are non-negative and sum to 1 (valid probability distribution)
- - Log-sum-exp (LSE): the quantity log(sum\_j exp(z\_j)) that appears as the normalization constant for softmax
- - Numerical-stability trick for softmax: subtracting the maximum logit (or using stable LSE) before exponentiation to avoid overflow/underflow
- - Interpretation of logits vs probabilities: logits as unnormalized log-probabilities (log p up to an additive constant)
- - Shift-invariance of softmax: adding the same constant to all logits does not change the output probabilities
- - Sharpness / extreme behavior: when one logit is much larger than others, softmax yields near one-hot probabilities; when logits are similar, outputs are more uniform
- - Softmax as weighting mechanism: using softmax outputs as normalized attention weights (convex weights applied to value vectors)
- - Softmax combined with classification loss: using softmax outputs (or their logs) inside cross-entropy loss for training
- - Log-probability form: expressing log probability of class i as z\_i minus the log-sum-exp

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

A model often outputs any real numbers it wants—positive, negative, huge, tiny. Softmax is the bridge that turns those raw scores (logits) into a clean probability distribution you can interpret, train with, and reuse inside attention.

TL;DR:

Logits are unnormalized scores **z** ∈ ℝᴷ (one per class). Softmax converts them into probabilities pᵢ = exp(zᵢ) / ∑ⱼ exp(zⱼ). Softmax is invariant to adding a constant to all logits, so you compute it stably by subtracting max(**z**) before exponentiating (the log-sum-exp trick). Logits encode relative preference via differences: pᵢ/pⱼ = exp(zᵢ − zⱼ).

## What Is Softmax (and What Are Logits)?

### Why you should care first

Most models do not naturally output probabilities. A neural network layer typically outputs a vector of real numbers with no constraints:

- •They don’t sum to 1.
- •They can be negative.
- •Their magnitudes can be extremely large.

But in classification (and in attention), we *want* a probability distribution: numbers between 0 and 1 that sum to 1.

That’s what **softmax** does.

### Logits: “scores before probabilities”

Suppose you have K classes. The model outputs a vector of logits

- •**z** = (z₁, z₂, …, z\_K) ∈ ℝᴷ

Interpretation:

- •zᵢ is a *score* for class i.
- •Higher zᵢ ⇒ the model “leans toward” class i.
- •Only *relative* values matter (differences). The absolute scale has meaning mainly through confidence (more on that later).

Logits are not probabilities. They are better thought of as: “how much evidence do we have for each class?”

### Softmax: turning scores into a distribution

Softmax maps logits to probabilities:

pᵢ = softmax(**z**)ᵢ = exp(zᵢ) / ∑ⱼ exp(zⱼ)

Key properties:

1) 0 < pᵢ < 1 for all i (because exp(·) > 0)

2) ∑ᵢ pᵢ = 1 (because you divide by the sum)

3) If zᵢ is bigger, pᵢ tends to be bigger (monotonic relationship)

So softmax turns an unconstrained vector in ℝᴷ into a point on the probability simplex.

### “Soft” vs “hard” max

- •A hard argmax picks a single class: argmaxᵢ zᵢ.
- •Softmax produces a smooth distribution that *approaches* argmax when one logit dominates.

If one logit is much larger than the others, softmax becomes very “peaky” (high confidence). If logits are close, softmax becomes more uniform (uncertainty).

### A mental model: exponentiate then normalize

Softmax does two intuitive operations:

1) **Exponentiate**: converts differences in logits into multiplicative ratios.

2) **Normalize**: turns those positive weights into probabilities.

This exponential step is why small logit differences can matter a lot.

### The key ratio identity (the real meaning of logits)

Softmax gives a clean relationship:

pᵢ / pⱼ = exp(zᵢ) / exp(zⱼ) = exp(zᵢ − zⱼ)

So:

- •Logit *differences* zᵢ − zⱼ are log-odds ratios.
- •A +1 increase in (zᵢ − zⱼ) multiplies pᵢ/pⱼ by e ≈ 2.718.

This is the core interpretation: logits are “log-probability-like scores” where differences correspond to multiplicative preference.

### Quick 2-class special case (connects to sigmoid)

If K = 2 with logits (a, b), then

p(class 1) = exp(a) / (exp(a)+exp(b))

Divide numerator and denominator by exp(b):

p(class 1) = exp(a−b) / (exp(a−b)+1) = 1 / (1+exp(−(a−b)))

That’s the sigmoid σ(a−b). So softmax generalizes sigmoid.

This also reinforces: only the difference (a−b) matters, not the absolute values.

## Core Mechanic 1: Softmax Geometry, Invariances, and “Temperature”

### Why this matters

Before you worry about numerical stability, you need to understand *what softmax is doing* conceptually:

- •It turns differences into ratios.
- •It ignores uniform shifts.
- •It can be sharpened or softened by scaling logits.

These facts show up constantly in practice: calibration, confidence, attention distributions, and why subtracting max(**z**) is “allowed.”

---

## 1) Shift invariance (adding a constant changes nothing)

Let c be any real number and define z'ᵢ = zᵢ + c.

Compute softmax(**z'**)ᵢ:

softmax(**z'**)ᵢ = exp(zᵢ + c) / ∑ⱼ exp(zⱼ + c)

Now factor out exp(c):

= (exp(c)exp(zᵢ)) / (∑ⱼ exp(c)exp(zⱼ))

= exp(zᵢ) / ∑ⱼ exp(zⱼ)

= softmax(**z**)ᵢ

So adding the same constant to every logit does not change the probabilities.

**Why you care:** this is the mathematical reason you can subtract max(**z**) for stability.

---

## 2) Scale effects: “temperature” and confidence

Now consider scaling logits by a positive scalar α:

**z'** = α**z**

Then:

pᵢ(α) = exp(αzᵢ) / ∑ⱼ exp(αzⱼ)

- •If α is large, the largest logit dominates ⇒ distribution becomes sharper (lower entropy).
- •If α is small (near 0), exp(αzᵢ) ≈ 1 ⇒ distribution approaches uniform.

Often this is expressed as a **temperature** T > 0:

softmax\_T(**z**)ᵢ = exp(zᵢ / T) / ∑ⱼ exp(zⱼ / T)

- •Lower T (T < 1) ⇒ sharper (more confident)
- •Higher T (T > 1) ⇒ softer (more uncertain)

### Small derivation: why large α makes argmax-like behavior

Let m = maxⱼ zⱼ and let k be an index achieving that max.

Consider the ratio for any i ≠ k:

pᵢ / p\_k = exp(α(zᵢ − z\_k))

Since zᵢ − z\_k < 0, as α → ∞:

exp(α(zᵢ − z\_k)) → 0

So p\_k → 1 and all others → 0.

---

## 3) Entropy intuition (softmax as a tradeoff)

Softmax can be motivated (informally) as producing a distribution that:

- •prefers higher logits (higher expected score)
- •but does not collapse instantly (maintains entropy unless forced)

This viewpoint helps when you later see attention: attention weights are softmax over similarity scores. Changing scale (like dividing by √d in Transformers) directly changes entropy/peakedness.

---

## 4) Softmax outputs can be “misleadingly confident”

Because softmax exponentiates, it can output very high probabilities even when the model is wrong.

Example: logits **z** = (10, 9, 0)

- •The top two logits differ by only 1
- •But exp(10) is enormous relative to exp(0)

Softmax will still assign almost all mass to the first two classes, with the third near 0.

This is not a bug in softmax—it’s a reflection of what logits encode. If the model produces large-magnitude logits, it is expressing high confidence.

**Practical takeaway:** to interpret probabilities sensibly, you often need calibration techniques (temperature scaling, etc.). But as a foundational building block, softmax is doing exactly what its math says.

## Core Mechanic 2: Numerical Stability and the Log-Sum-Exp Trick

### Why you need numerical stability

Softmax uses exp(zᵢ). Exponentials grow (and shrink) extremely fast.

In floating-point arithmetic (like float32), this causes two common problems:

- •**Overflow:** exp(1000) becomes ∞.
- •**Underflow:** exp(−1000) becomes 0.

Even when the *final* softmax probabilities are well-defined, naive computation can blow up.

---

## 1) Stable softmax via subtracting the max logit

Because softmax is shift-invariant, choose:

m = maxᵢ zᵢ

Define shifted logits:

z̃ᵢ = zᵢ − m

Then compute:

softmax(**z**)ᵢ = exp(z̃ᵢ) / ∑ⱼ exp(z̃ⱼ)

Now:

- •The largest shifted logit is 0
- •All others are ≤ 0
- •So exp(z̃ᵢ) ∈ (0, 1]

This prevents overflow and keeps values in a sane numeric range.

### Quick equivalence derivation

Start from the original softmax:

pᵢ = exp(zᵢ) / ∑ⱼ exp(zⱼ)

Subtract m:

exp(zᵢ) = exp(zᵢ − m)exp(m)

So:

pᵢ = exp(zᵢ − m)exp(m) / ∑ⱼ exp(zⱼ − m)exp(m)

Cancel exp(m):

pᵢ = exp(zᵢ − m) / ∑ⱼ exp(zⱼ − m)

---

## 2) log-sum-exp: stable computation of log(∑ exp(z))

Often you don’t just need softmax; you need the log of its denominator:

log ∑ⱼ exp(zⱼ)

This appears in:

- •cross-entropy / negative log-likelihood
- •log-softmax
- •computing normalized log-probabilities

The stable identity is:

log ∑ⱼ exp(zⱼ) = m + log ∑ⱼ exp(zⱼ − m)

where m = maxⱼ zⱼ.

### Derivation step-by-step

Let S = ∑ⱼ exp(zⱼ). Factor out exp(m):

S = ∑ⱼ exp(zⱼ)

= ∑ⱼ exp((zⱼ − m) + m)

= ∑ⱼ exp(zⱼ − m)exp(m)

= exp(m) ∑ⱼ exp(zⱼ − m)

Now take log:

log S = log( exp(m) ∑ⱼ exp(zⱼ − m) )

= log exp(m) + log ∑ⱼ exp(zⱼ − m)

= m + log ∑ⱼ exp(zⱼ − m)

Now all exponentials are exp(≤ 0), so you avoid overflow.

---

## 3) Log-softmax is often better than softmax

Many training losses require log probabilities:

log pᵢ = log softmax(**z**)ᵢ

Naively:

log pᵢ = log(exp(zᵢ) / ∑ⱼ exp(zⱼ))

= zᵢ − log ∑ⱼ exp(zⱼ)

This is great because it avoids forming tiny probabilities directly.

Use log-sum-exp for stability:

log pᵢ = zᵢ − (m + log ∑ⱼ exp(zⱼ − m))

### Why this matters in practice

- •If the correct class has extremely small probability, pᵧ might underflow to 0.
- •Then log(pᵧ) becomes log(0) = −∞.
- •Training becomes unstable.

Computing log-softmax directly avoids this.

---

## 4) A table of “what to compute”

| Goal | Naive expression | Stable expression | Typical use |
| --- | --- | --- | --- |
| Softmax probs | exp(zᵢ)/∑ exp(z) | exp(zᵢ−m)/∑ exp(z−m) | inference, attention weights |
| log-sum-exp | log ∑ exp(z) | m + log ∑ exp(z−m) | normalization constants |
| log-softmax | log softmax(z) | zᵢ − logsumexp(z) | cross-entropy training |

When implementing or debugging ML code, it’s useful to ask: “Do I need probs, or only log-probs?” If you only need log-probs, prefer log-softmax.

## Application/Connection: Classification Losses and Attention Weights

### Why connect softmax to real systems

Softmax is not an isolated formula. It sits at two of the most important junctions in modern ML:

1) **Multiclass classification** (via cross-entropy)

2) **Transformer attention** (via softmax-normalized similarity scores)

Understanding what softmax is doing in these contexts makes later nodes (masking, Transformers) much easier.

---

## 1) Softmax + cross-entropy (multiclass classification)

You have:

- •logits **z** ∈ ℝᴷ
- •true label y ∈ {1,…,K}
- •predicted probabilities pᵢ = softmax(**z**)ᵢ

The negative log-likelihood (cross-entropy with a one-hot target) is:

L = −log p\_y

Substitute softmax:

L = −log( exp(z\_y) / ∑ⱼ exp(zⱼ) )

Now simplify:

L = −( z\_y − log ∑ⱼ exp(zⱼ) )

= log ∑ⱼ exp(zⱼ) − z\_y

This form is the reason log-sum-exp is central: it’s literally inside the loss.

### Intuition

- •To reduce L, you can increase z\_y (raise the true class score)
- •Or decrease other zⱼ (reduce competing class scores)

### Key conceptual point: cross-entropy cares about relative differences

If you add a constant c to all logits:

z'\_j = z\_j + c

Then:

L' = log ∑ⱼ exp(zⱼ + c) − (z\_y + c)

= log( exp(c)∑ⱼ exp(zⱼ) ) − z\_y − c

= (c + log ∑ⱼ exp(zⱼ)) − z\_y − c

= L

So the loss is shift-invariant too.

---

## 2) Gradient shape (why softmax is learnable)

Even without doing a full backprop derivation, one famous result explains a lot:

For cross-entropy with softmax, the gradient w.r.t. logits is:

∂L/∂zᵢ = pᵢ − 𝟙[i = y]

Meaning:

- •For the correct class y: ∂L/∂z\_y = p\_y − 1 (negative if p\_y < 1), so gradient pushes z\_y up.
- •For incorrect classes i ≠ y: ∂L/∂zᵢ = pᵢ (positive), so gradient pushes them down.

This elegant “p − y\_onehot” structure is one reason softmax + cross-entropy is standard.

---

## 3) Attention: softmax as a normalized weighting mechanism

In Transformers, attention scores are computed (simplified) as:

scoresᵢ = ( **q** · **kᵢ** ) / √d

Then attention weights are:

αᵢ = softmax(scores)ᵢ

And the output is a weighted sum:

**o** = ∑ᵢ αᵢ **vᵢ**

Here softmax ensures:

- •αᵢ ≥ 0
- •∑ᵢ αᵢ = 1

So attention becomes a convex combination of value vectors. This is essential for stability and interpretability.

### Why scaling by √d matters

Dot products grow with dimension d. If scores become too large in magnitude, softmax becomes too peaky (near one-hot), harming learning.

Dividing by √d reduces score scale and keeps the softmax in a healthier regime.

---

## 4) Where masking will plug in (next node)

In attention, you often must prevent attending to certain positions (padding or future tokens). The standard trick is:

scoresᵢ ← scoresᵢ + maskᵢ

where maskᵢ is:

- •0 for allowed positions
- •a large negative number (≈ −∞) for disallowed positions

Then softmax assigns ~0 probability to masked positions because exp(−∞) ≈ 0.

This works *because* softmax converts large negative logits into near-zero probability.

So when you learn [Sequence Masking (causal and padding masks)](/tech-tree/sequence-masking/), you’ll essentially be learning how to engineer logits before applying softmax.

---

## 5) Interpreting logits vs probabilities in practice

A few practical guidelines:

- •**Use logits for computation**, probabilities for presentation.
- •Differences in logits are meaningful: zᵢ − zⱼ.
- •Softmax probabilities can saturate at 0 or 1; log-probabilities are safer numerically.
- •Calibration (like temperature scaling) adjusts the scale of logits to better match empirical correctness.

Softmax is simple—but its behavior under shifts, scales, and masking is the backbone of many modern architectures.

## Worked Examples (3)

### Compute softmax probabilities and interpret logit differences

A 3-class classifier outputs logits **z** = (2, 1, 0). Compute softmax(**z**) and interpret the ratio p₁/p₂.

1. Write the definition:

   pᵢ = exp(zᵢ) / (exp(z₁)+exp(z₂)+exp(z₃))
2. Compute exponentials:

   exp(2) ≈ 7.389

   exp(1) ≈ 2.718

   exp(0) = 1
3. Compute the normalization constant:

   S = 7.389 + 2.718 + 1 = 11.107
4. Compute probabilities:

   p₁ = 7.389 / 11.107 ≈ 0.665

   p₂ = 2.718 / 11.107 ≈ 0.245

   p₃ = 1 / 11.107 ≈ 0.090
5. Interpret the ratio using logit differences:

   p₁/p₂ = exp(z₁ − z₂) = exp(2 − 1) = exp(1) ≈ 2.718

   Check numerically:

   0.665 / 0.245 ≈ 2.714 (close, rounding differences)

**Insight:** Softmax turns additive differences in logits into multiplicative differences in probabilities. A 1-point advantage in logits means about 2.7× higher probability *relative to a competitor*, all else equal.

### Stable softmax with a huge logit (avoid overflow)

Compute softmax(**z**) for **z** = (1000, 1001, 999) using a numerically stable method.

1. Identify the maximum logit:

   m = max(1000, 1001, 999) = 1001
2. Shift logits:

   z̃ = **z** − m = (1000−1001, 1001−1001, 999−1001) = (−1, 0, −2)
3. Exponentiate shifted logits (these are safe):

   exp(−1) ≈ 0.3679

   exp(0) = 1

   exp(−2) ≈ 0.1353
4. Normalize:

   S = 0.3679 + 1 + 0.1353 = 1.5032

   p₁ = 0.3679 / 1.5032 ≈ 0.2447

   p₂ = 1 / 1.5032 ≈ 0.6652

   p₃ = 0.1353 / 1.5032 ≈ 0.0900
5. Explain why the naive way fails:

   Naively you’d compute exp(1000), exp(1001), exp(999), which overflow in float32, producing ∞ and undefined ratios.

   Subtracting m uses shift invariance so the final probabilities are unchanged.

**Insight:** Stable softmax is not a heuristic—it’s mathematically identical to naive softmax, but keeps the exponentials in a safe range by exploiting shift invariance.

### Compute cross-entropy loss from logits using log-sum-exp

A 4-class model outputs logits **z** = (3, 1, −2, 0). The true class is y = 2 (the logit 1). Compute L = −log p\_y stably.

1. Use the stable loss form:

   L = log ∑ⱼ exp(zⱼ) − z\_y
2. Compute m = max(zⱼ):

   m = max(3, 1, −2, 0) = 3
3. Compute shifted exponentials:

   z − m = (0, −2, −5, −3)

   exp(0)=1

   exp(−2)≈0.1353

   exp(−5)≈0.0067

   exp(−3)≈0.0498
4. Compute the shifted sum:

   S̃ = 1 + 0.1353 + 0.0067 + 0.0498 = 1.1918
5. Compute log-sum-exp:

   log ∑ⱼ exp(zⱼ) = m + log S̃ = 3 + log(1.1918)

   log(1.1918) ≈ 0.1755

   So log ∑ⱼ exp(zⱼ) ≈ 3.1755
6. Subtract the true logit z\_y = 1:

   L ≈ 3.1755 − 1 = 2.1755

**Insight:** Cross-entropy from logits naturally involves log-sum-exp. Computing it stably avoids ever forming tiny probabilities like p\_y directly.

## Key Takeaways

- ✓

  Logits **z** ∈ ℝᴷ are unnormalized real-valued scores; softmax converts them into a probability distribution.
- ✓

  Softmax is pᵢ = exp(zᵢ)/∑ⱼ exp(zⱼ), so differences in logits become probability ratios: pᵢ/pⱼ = exp(zᵢ − zⱼ).
- ✓

  Softmax is shift-invariant: softmax(**z** + c·**1**) = softmax(**z**). This enables stable computation.
- ✓

  Compute softmax stably with m = max(**z**) and exp(zᵢ−m); compute log-sum-exp as m + log ∑ exp(zⱼ−m).
- ✓

  For training, prefer log-softmax / log-sum-exp forms; they avoid underflow and give stable cross-entropy.
- ✓

  Scaling logits changes distribution sharpness; temperature T controls how peaky or uniform softmax becomes.
- ✓

  In attention, softmax turns similarity scores into nonnegative weights that sum to 1, enabling weighted sums of value vectors.
- ✓

  Masking works by adding large negative values to selected logits so softmax assigns them ~0 probability.

## Common Mistakes

- ✗

  Computing exp(zᵢ) directly on large logits (overflow) instead of subtracting max(**z**) first.
- ✗

  Interpreting logits as probabilities (e.g., thinking a negative logit means “negative probability”). Logits are unconstrained scores.
- ✗

  Forgetting that softmax only cares about relative differences; adding the same constant to all logits should not change outputs.
- ✗

  Using softmax probabilities in the loss computation instead of a combined stable cross-entropy-from-logits (leading to log(0) or NaNs).

## Practice

easy

Compute softmax(**z**) for **z** = (0, 0, 0, 0). What is the entropy intuition here?

**Hint:** All exponentials are the same; normalization divides equally among classes.

Show solution

exp(0)=1 for each class, so ∑ exp(zⱼ)=4 and each pᵢ = 1/4 = 0.25. Intuition: identical logits mean no preference, so softmax returns the uniform (maximum-entropy) distribution.

medium

Show that softmax is shift-invariant: prove softmax(**z**) = softmax(**z** − m·**1**) for any scalar m.

**Hint:** Factor exp(−m) out of numerator and denominator (or exp(m) depending on direction).

Show solution

Let z'ᵢ = zᵢ − m. Then softmax(**z'**)ᵢ = exp(zᵢ − m)/∑ⱼ exp(zⱼ − m) = (exp(zᵢ)exp(−m)) / (∑ⱼ exp(zⱼ)exp(−m)) = exp(zᵢ)/∑ⱼ exp(zⱼ) = softmax(**z**)ᵢ. So shifting all logits by the same m does not change the distribution.

hard

Given logits **z** = (5, 2, 1) and true class y = 1 (the first entry), compute the cross-entropy loss L = log ∑ⱼ exp(zⱼ) − z\_y using a stable log-sum-exp step.

**Hint:** Let m = max(**z**)=5, compute ∑ exp(zⱼ−m), then add m and subtract z\_y.

Show solution

m=5. Shifted logits: (0, −3, −4). Exponentials: exp(0)=1, exp(−3)≈0.0498, exp(−4)≈0.0183. Sum S̃≈1.0681. logsumexp ≈ 5 + log(1.0681). log(1.0681)≈0.0659, so logsumexp≈5.0659. With y=1, z\_y=5, so L≈5.0659−5=0.0659.

## Connections

Next, softmax becomes a tool you *control* by editing logits before normalization:

- •[Sequence Masking (causal and padding masks)](/tech-tree/sequence-masking/) — add −∞ (large negative) to disallowed logits so softmax assigns ~0 probability.
- •[Transformers](/tech-tree/transformers/) — attention weights are softmax over scaled dot-product scores; temperature-like scaling (÷√d) controls sharpness and training stability.

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
