---
title: Bias-Variance Tradeoff
description: Decomposition of prediction error. Underfitting vs overfitting.
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
inspiration_url: https://templeton.host/tech-tree/bias-variance/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/bias-variance/](https://templeton.host/tech-tree/bias-variance/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Bias-Variance Tradeoff

Machine LearningDifficulty: ★★★★☆Depth: 9Unlocks: 2

Decomposition of prediction error. Underfitting vs overfitting.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Decomposition of prediction error at input x into three parts: irreducible noise + (bias)^2 + variance
- -Bias: the systematic difference between the expected learned prediction and the true function at x
- -Variance: the variability of the learned prediction at x across different training sets

## Key Symbols & Notation

f\_hat(x) - the learned/predicted function at input xf(x) - the true target function at input x

## Essential Relationships

- -As model complexity increases, bias typically decreases and variance typically increases (the bias-variance tradeoff); underfitting corresponds to high bias, overfitting corresponds to high variance

## Prerequisites (2)

[Expected Value5 atoms](/tech-tree/expected-value/)[Machine Learning Introduction5 atoms](/tech-tree/ml-intro/)

## Unlocks (2)

[Cross-Validationlvl 4](/tech-tree/cross-validation/)[Ensemble Methodslvl 4](/tech-tree/ensemble-methods/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[failure modeBusiness

The bias-variance decomposition is the canonical ML framework for taxonomizing failure modes - it decomposes prediction error into two specific, named failure modes (underfitting vs overfitting) and prescribes different interventions for each, which is the mathematical foundation for the practice of identifying and encoding distinct failure modes into corrective frameworks](/business/failure-mode/)

Advanced Learning Details

### Graph Position

112

Depth Cost

2

Fan-Out (ROI)

2

Bottleneck Score

9

Chain Length

### Cognitive Load

6

Atomic Elements

36

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (14)

- - Prediction error (expected test mean squared error): the expected squared difference between true target Y and model prediction f̂(X).
- - Bias (pointwise): the difference between the expected model prediction across training sets and the true target function at X.
- - Squared bias (Bias^2): the square of the pointwise bias, contributing nonnegative systematic error.
- - Variance (pointwise): variability of the model prediction at X across different training sets.
- - Irreducible error (noise): the component of target variability that cannot be reduced by any model (e.g., Var(ε) when Y = f\*(X)+ε).
- - Bias–variance decomposition: the breakdown of expected squared prediction error into squared bias + variance + irreducible error (for squared loss).
- - Underfitting: model behavior characterized by high bias (systematic error), typically yielding high training and test error.
- - Overfitting: model behavior characterized by high variance (sensitive to training set noise), producing low training error but high test error.
- - Model complexity (capacity): a property of hypothesis class or hyperparameters that controls bias and variance (e.g., number of parameters, degree of polynomial).
- - Generalization error vs training error: distinction between error measured on unseen data (generalization/test error) and error measured on the training set.
- - Expectation over training sets: treating the training dataset as random and taking expected predictions across possible datasets to define bias and variance.
- - Dependence of bias and variance on sample size: larger training sets typically reduce variance (but not necessarily bias).
- - Effect of regularization / complexity control: methods that increase bias to reduce variance (and vice versa).
- - Squared-loss specificity: the classic bias–variance decomposition is derived for squared error (MSE); decomposition form depends on loss choice.

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Two models can have the same training error and wildly different test error. The bias–variance tradeoff explains why: learning is a tug-of-war between systematic error (bias) and sensitivity to data (variance), with an unavoidable floor set by noise.

TL;DR:

At a fixed input x, the expected squared prediction error decomposes as

E[(ŷ(x) − y)²] = (Bias[ŷ(x)])² + Var(ŷ(x)) + σ².

Bias measures how far the average learned prediction is from the true function f(x). Variance measures how much the learned prediction changes across different training sets. σ² is irreducible noise from the data-generating process.

## What Is Bias–Variance Tradeoff?

### Why this concept exists

In supervised learning, you don’t just want to fit the data you already saw—you want to predict new data. The uncomfortable part is that *training data is only one random draw* from many possible datasets you could have received. If you trained the same algorithm again on a different sample, you’d typically get a different predictor.

So when you ask “How good is my model?” you really mean something like:

- •If I repeatedly sampled new training sets from the same source…
- •retrained the model each time…
- •and then evaluated predictions at some input x…

what error should I expect?

Bias–variance is the language for answering that. It separates error into:

1. 1)**Noise (irreducible)**: randomness in y that no model can predict perfectly.
2. 2)**Bias (systematic error)**: the model class (and training procedure) tends to miss the true relationship in a consistent direction.
3. 3)**Variance (instability)**: the learned model changes a lot when the training set changes.

This is what people mean by **underfitting vs overfitting**:

- •**Underfitting**: high bias, often low variance. The model is too rigid to capture the true pattern.
- •**Overfitting**: low bias, high variance. The model captures quirks of the sampled training set that don’t generalize.

### The setting (what’s random?)

To make this precise, we assume a data-generating process:

- •Inputs x are drawn from some distribution.
- •Outputs are generated by

y = f(x) + ε

where:

- •f(x) is the *true* (unknown) function.
- •ε is random noise with E[ε] = 0 and Var(ε) = σ².

A learning algorithm takes a training set D and produces a predictor:

f̂\_D(x)

We will often shorten this to f̂(x), but it’s important to remember:

- •f̂(x) is a random variable because it depends on the random training set D.

### What “bias” and “variance” mean at a single x

Fix an input x. Across many possible training sets, you get many learned predictions:

f̂\_D₁(x), f̂\_D₂(x), …

Define:

- •**Expected prediction** at x: E\_D[f̂(x)]
- •**Bias** at x:

Bias(x) = E\_D[f̂(x)] − f(x)

- •**Variance** at x:

Var(x) = Var\_D(f̂(x)) = E\_D[(f̂(x) − E\_D[f̂(x)])²]

Bias is about the *center* of the cloud of possible learned predictions. Variance is about the *spread* of that cloud.

### Big picture: one input x vs overall performance

The classic decomposition is at a fixed x. To get a single number for a model, you typically average over x as well:

E\_x[E\_D[(f̂(x) − y)²]]

But the intuition is cleanest at one x first: bias and variance can differ across regions of input space. A model might be stable (low variance) where data is plentiful and unstable (high variance) near the edges.

### A quick comparison table

| Term | Depends on training set D? | Depends on noise ε? | What it measures | Can we reduce it? |
| --- | --- | --- | --- | --- |
| (Bias(x))² | via E\_D[f̂(x)] | no | systematic mismatch from f(x) | yes (richer model, better features, less regularization) |
| Var(x) | yes | no | sensitivity to dataset sampling | yes (more data, regularization, bagging/ensembles) |
| σ² (noise) | no | yes | inherent randomness in y given x | not without changing measurement process |

Bias–variance tradeoff is the practical reality that many interventions that reduce one can increase the other.

## Core Mechanic 1: The Error Decomposition at Input x

### Why decompose error?

When you measure squared error, it’s hard to tell *why* the error is happening. Is the model too simple? Too wiggly? Is the data noisy? The decomposition tells you how much error comes from each cause—at least conceptually.

We’ll derive the standard result:

E\_D,ε[(f̂(x) − y)²] = (Bias(x))² + Var(x) + σ²

where y = f(x) + ε.

### Step 0: write the prediction error using the data model

Start from:

(f̂(x) − y)²

Substitute y = f(x) + ε:

(f̂(x) − f(x) − ε)²

Now take expectation over both sources of randomness:

- •D (the training set, which affects f̂)
- •ε (the noise in the test label)

So we consider:

E\_D,ε[(f̂(x) − f(x) − ε)²]

### Step 1: separate the noise term

Expand the square:

(f̂(x) − f(x) − ε)²

= (f̂(x) − f(x))² − 2ε(f̂(x) − f(x)) + ε²

Take expectation:

E[(f̂(x) − f(x))²] − 2E[ε(f̂(x) − f(x))] + E[ε²]

Now use two key assumptions:

1. 1)E[ε] = 0
2. 2)ε is independent of D, hence independent of f̂(x) (since f̂ is computed from D)

So:

E[ε(f̂(x) − f(x))] = E[ε] · E[f̂(x) − f(x)] = 0

And E[ε²] = Var(ε) = σ².

Thus:

E\_D,ε[(f̂(x) − y)²] = E\_D[(f̂(x) − f(x))²] + σ²

So the “interesting” part is E\_D[(f̂(x) − f(x))²].

### Step 2: add and subtract the mean predictor

Let μ(x) = E\_D[f̂(x)]. Add and subtract μ(x):

f̂(x) − f(x)

= (f̂(x) − μ(x)) + (μ(x) − f(x))

Square it:

(f̂(x) − f(x))²

= (f̂(x) − μ(x) + μ(x) − f(x))²

Expand:

= (f̂(x) − μ(x))²

- •2(f̂(x) − μ(x))(μ(x) − f(x))
- •(μ(x) − f(x))²

Now take expectation over D.

The last term is constant with respect to D:

E\_D[(μ(x) − f(x))²] = (μ(x) − f(x))²

The first term is the variance definition:

E\_D[(f̂(x) − μ(x))²] = Var\_D(f̂(x))

The middle term disappears because E\_D[f̂(x) − μ(x)] = 0:

E\_D[2(f̂(x) − μ(x))(μ(x) − f(x))]

= 2(μ(x) − f(x)) E\_D[f̂(x) − μ(x)]

= 2(μ(x) − f(x)) · 0

= 0

So we get:

E\_D[(f̂(x) − f(x))²]

= Var\_D(f̂(x)) + (μ(x) − f(x))²

But μ(x) − f(x) is exactly Bias(x). Therefore:

E\_D[(f̂(x) − f(x))²] = Var(x) + (Bias(x))²

### Step 3: combine with noise

Recall:

E\_D,ε[(f̂(x) − y)²] = E\_D[(f̂(x) − f(x))²] + σ²

So:

E\_D,ε[(f̂(x) − y)²]

= (Bias(x))² + Var(x) + σ²

### What this decomposition does (and does not) say

This is a *conceptual* decomposition of expected test error at x. It does not mean you can directly look at your dataset and perfectly measure bias and variance without extra assumptions. But it does tell you:

- •If you’re doing great on training but terrible on test, suspect **high variance**.
- •If you’re doing poorly on both training and test, suspect **high bias**.

### Why squared error matters

This exact decomposition is for squared loss (and closely related losses). The nice algebra comes from expanding squares. For other losses (like 0–1 classification error), there are analogs but not such a clean three-term identity.

### A brief geometric intuition

At fixed x, imagine f̂(x) as a point on the number line that changes with D.

- •Bias is the distance between the mean point μ(x) and the true f(x).
- •Variance is the spread of the points around μ(x).
- •Noise is the fact that even if you predicted f(x) perfectly, y still fluctuates around it.

## Core Mechanic 2: How Model Complexity and Data Control Bias and Variance

### Why a “tradeoff” appears

You might hope to reduce bias and variance simultaneously. Sometimes you can (e.g., better features, more data). But often you face a real tension:

- •Making a model more flexible typically **reduces bias** (it can match f better)
- •but **increases variance** (it can chase idiosyncrasies of the sampled dataset)

This is not a law of nature for every method, but it is a persistent pattern in many learning setups.

### A mental experiment: retraining on different datasets

Fix x. Suppose you repeatedly sample datasets D₁, D₂, … and train the same algorithm.

- •A rigid method (like a constant predictor) yields nearly the same f̂(x) every time → low variance.
- •A highly flexible method might produce very different f̂(x) across datasets → high variance.

But rigidity often means the model cannot represent f well → higher bias.

### Underfitting vs overfitting through the decomposition

It helps to connect the decomposition to the typical learning-curve story.

- •**Underfitting** (high bias):
- •Training error is high.
- •Test error is high.
- •Increasing model capacity often helps.

- •**Overfitting** (high variance):
- •Training error is low.
- •Test error is high.
- •More regularization, more data, or ensembling often helps.

A common misconception is that “overfitting means the model is too complex.” Complexity is one route to variance, but **variance is about sensitivity**, not about complexity alone.

### What knobs change bias and variance?

Below is a practical map. Effects can depend on the algorithm and data regime, but these are reliable first approximations.

| Intervention | Typical effect on Bias | Typical effect on Variance | Notes |
| --- | --- | --- | --- |
| Increase model capacity (more parameters, higher-degree polynomial, deeper tree) | ↓ | ↑ | Lower bias, higher variance risk |
| Increase regularization (L2/L1, pruning, dropout) | ↑ | ↓ | Makes solutions more stable |
| More training data | ↔ or ↓ | ↓ | Usually reduces variance strongly |
| Better features / representation | ↓ | ↔ or ↓ | Can reduce bias without increasing variance much |
| Early stopping (iterative learners) | ↑ | ↓ | Acts like regularization |
| Bagging / averaging multiple models | ↔ | ↓ | Reduces variance by averaging |
| Boosting (often) | ↓ | can ↑ or ↓ | Often reduces bias; variance behavior depends |

### A concrete anchor: k-nearest neighbors (KNN)

KNN is a classic bias–variance illustration.

- •1-NN: prediction depends heavily on the single nearest sample.
- •Bias: low (can fit complicated boundaries)
- •Variance: high (very sensitive to which points were sampled)

- •Large k (say k = 50): prediction averages many neighbors.
- •Bias: higher (over-smooths)
- •Variance: lower (stable)

Here the “complexity knob” is k (smaller k → more flexible).

### Another anchor: polynomial regression

Suppose you fit y as a polynomial of degree d.

- •Small d (e.g., d = 1) may miss curvature → high bias.
- •Large d can match training points closely → low bias but high variance.

If you also add regularization, you can increase d (potentially reduce bias) while controlling variance.

### Why variance falls with averaging (ensembles)

A useful fact: averaging reduces variance when errors are not perfectly correlated.

Let Z₁, …, Z\_M be random predictions (at x) from M models with the same mean and variance.

Define the average prediction:

Z̄ = (1/M) ∑ᵢ Zᵢ

If the Zᵢ are independent with Var(Zᵢ) = v, then:

Var(Z̄) = Var((1/M) ∑ᵢ Zᵢ)

= (1/M²) ∑ᵢ Var(Zᵢ)

= (1/M²) · M · v

= v/M

In practice, models are correlated, so you don’t get v/M, but you still often get a meaningful reduction. This is the core reason bagging and random forests reduce variance.

### Bias and variance vary over x

A final subtlety worth breathing room:

- •Bias(x) and Var(x) can be small in some regions and large in others.
- •Data density matters: where you have fewer samples, the model is more uncertain → higher variance.

This explains why some models behave nicely “in the middle” but become unstable near the boundaries of the input domain.

## Application/Connection: Diagnosing Generalization and Choosing Evaluation Tools

### Why this matters in practice

You rarely get to compute Bias(x), Var(x), or σ² directly. What you *can* do is:

- •Use held-out evaluation to estimate generalization error.
- •Use tools like cross-validation to compare models.
- •Use ensembles and regularization to manage variance.
- •Use feature engineering / representation learning to reduce bias.

Bias–variance tradeoff is a *diagnostic story* that guides which lever to pull next.

### From decomposition to workflow

A common iterative workflow:

1. 1)**Start simple** and get a baseline.
2. 2)Check **training vs validation** error.
3. 3)If both are high → likely high bias.
4. 4)If training is low but validation is high → likely high variance.
5. 5)Adjust:

- •High bias: richer hypothesis class, better features, less regularization.
- •High variance: more data, stronger regularization, ensembling, simpler model.

This is not a proof—just a principled heuristic.

### Where cross-validation fits

Cross-validation (CV) is a way to approximate the expectation over datasets D.

Remember: variance is about how much f̂ changes when D changes. CV does something related:

- •It trains on multiple different subsets of the data.
- •It measures performance on held-out portions.

While CV doesn’t directly compute Var\_D(f̂(x)), it **approximates expected generalization error**, which includes both bias and variance effects.

In other words, CV is your practical handle on the left-hand side:

E\_D,ε[(f̂(x) − y)²]

averaged over x.

### Where ensembles fit

Ensembles (bagging, random forests) are practical tools to reduce variance:

- •If one unstable model overfits due to variance, averaging many such models can stabilize predictions.

This links directly to the variance term in the decomposition.

### The irreducible noise term and “Bayes error” intuition

Even with a perfect predictor f(x), your expected squared error is still σ².

This matters when you’re stuck:

- •If performance stops improving despite lots of tuning, you might be near the noise floor.

In classification, the analogous notion is that if classes overlap intrinsically, there is a minimum achievable error (often called Bayes error). The exact decomposition differs, but the same moral applies: some uncertainty is built into the world.

### A note on squared bias

The decomposition uses (Bias(x))², not Bias(x). This means:

- •Large bias is disproportionately harmful.
- •Removing a systematic offset can yield a big gain.

### Practical signals (imperfect but useful)

| Observation | Likely issue | Typical next move |
| --- | --- | --- |
| Training error high; validation error high | high bias | increase capacity, reduce regularization, improve features |
| Training error low; validation error high | high variance | more data, regularization, bagging/ensemble, simplify |
| Training error low; validation error low | good balance | consider whether noise limits further gains |
| Training error high; validation error lower (rare) | training procedure mismatch | check data leakage, metric, preprocessing, optimization |

### Closing the loop

Bias–variance is not just theory. It’s the bridge between:

- •what your model class can represent (bias)
- •how stable your learning procedure is (variance)
- •what the world allows you to predict (noise)

And it motivates the next nodes you’ll unlock:

- •Cross-validation: estimate generalization reliably.
- •Ensemble methods: reduce variance via averaging.

## Worked Examples (3)

### Example 1: Compute bias², variance, and noise at a single x from repeated training

Suppose the true function value at a particular input is f(x) = 2.

You train the same learning algorithm on many independent training sets, and you observe the learned prediction at this x is a random variable f̂(x) that takes values:

- •1 with probability 1/2
- •3 with probability 1/2

Assume the observation noise in the test label is ε with E[ε] = 0 and Var(ε) = σ² = 1, so y = f(x) + ε.

Compute Bias(x), (Bias(x))², Var(x), and the expected test MSE at x.

1. Compute the expected prediction μ(x) = E\_D[f̂(x)]:

   μ(x) = (1)(1/2) + (3)(1/2)

   = (1/2) + (3/2)

   = 2
2. Compute Bias(x) = μ(x) − f(x):

   Bias(x) = 2 − 2 = 0

   So (Bias(x))² = 0² = 0
3. Compute Var(x) = E[(f̂(x) − μ(x))²]:

   Possible deviations from μ = 2 are:

   - •if f̂ = 1, then (1 − 2)² = 1
   - •if f̂ = 3, then (3 − 2)² = 1

   Thus:

   Var(x) = (1)(1/2) + (1)(1/2) = 1
4. Use the decomposition:

   E[(f̂(x) − y)²] = (Bias(x))² + Var(x) + σ²

   = 0 + 1 + 1

   = 2

**Insight:** Even though the predictor is unbiased at this x (bias = 0), it is unstable (variance = 1). Averaging multiple such predictors (an ensemble) could reduce the variance term and improve test error, but you can’t beat the noise floor σ² = 1.

### Example 2: Derive the decomposition step-by-step (showing where the cross-term vanishes)

Assume y = f(x) + ε with E[ε] = 0 and Var(ε) = σ², and ε is independent of the training set D.

Let f̂(x) be the learned predictor from D.

Show that:

E\_D,ε[(f̂(x) − y)²] = (E\_D[f̂(x)] − f(x))² + Var\_D(f̂(x)) + σ².

1. Start with the test squared error:

   E[(f̂(x) − y)²]

   Substitute y = f(x) + ε:

   E[(f̂(x) − f(x) − ε)²]
2. Expand the square:

   (f̂ − f − ε)²

   = (f̂ − f)² − 2ε(f̂ − f) + ε²

   Take expectation:

   E[(f̂ − f)²] − 2E[ε(f̂ − f)] + E[ε²]
3. Show the middle term is 0:

   Because ε is independent of D (hence of f̂) and E[ε] = 0,

   E[ε(f̂ − f)] = E[ε]·E[f̂ − f] = 0
4. So the expression becomes:

   E[(f̂ − f)²] + E[ε²]

   And E[ε²] = Var(ε) = σ²
5. Now decompose E[(f̂ − f)²] by adding and subtracting μ = E[f̂]:

   Let μ = E\_D[f̂(x)]. Then

   f̂ − f = (f̂ − μ) + (μ − f)

   Square:

   (f̂ − f)² = (f̂ − μ)² + 2(f̂ − μ)(μ − f) + (μ − f)²
6. Take expectation over D:

   E[(f̂ − μ)²] + 2(μ − f)E[f̂ − μ] + (μ − f)²

   But E[f̂ − μ] = 0, so the cross-term vanishes.
7. Recognize terms:

   E[(f̂ − μ)²] = Var\_D(f̂(x))

   (μ − f) = Bias(x)

   So E[(f̂ − f)²] = Var\_D(f̂(x)) + (Bias(x))²
8. Combine with noise:

   E[(f̂ − y)²] = (Bias(x))² + Var\_D(f̂(x)) + σ²

**Insight:** The entire decomposition hinges on two ideas: (1) squared loss lets you expand and regroup terms cleanly, and (2) the cross-term disappears because deviations around the mean have zero expectation.

### Example 3: How averaging two correlated models affects variance

At a fixed x, suppose two learned models produce predictions Z₁ and Z₂ with:

E[Z₁] = E[Z₂] = m,

Var(Z₁) = Var(Z₂) = v,

Corr(Z₁, Z₂) = ρ.

Let the ensemble prediction be Z̄ = (Z₁ + Z₂)/2.

Compute Var(Z̄) in terms of v and ρ.

1. Use the variance formula:

   Var(Z̄) = Var((Z₁ + Z₂)/2)

   = (1/4) Var(Z₁ + Z₂)
2. Expand Var(Z₁ + Z₂):

   Var(Z₁ + Z₂) = Var(Z₁) + Var(Z₂) + 2Cov(Z₁, Z₂)

   = v + v + 2Cov(Z₁, Z₂)

   = 2v + 2Cov(Z₁, Z₂)
3. Convert correlation to covariance:

   Corr(Z₁, Z₂) = ρ = Cov(Z₁, Z₂) / (√v √v) = Cov(Z₁, Z₂) / v

   So Cov(Z₁, Z₂) = ρv
4. Substitute:

   Var(Z₁ + Z₂) = 2v + 2ρv = 2v(1 + ρ)
5. Thus:

   Var(Z̄) = (1/4) · 2v(1 + ρ)

   = (v/2)(1 + ρ)

**Insight:** Averaging helps most when models are less correlated. If ρ = 1 (perfectly correlated), Var(Z̄) = v (no gain). If ρ = 0, Var(Z̄) = v/2. Random forests work partly by reducing correlation between trees, making variance reduction from averaging more effective.

## Key Takeaways

- ✓

  At fixed x, the expected squared prediction error decomposes into (Bias(x))² + Var(x) + σ².
- ✓

  Bias(x) = E\_D[f̂(x)] − f(x) measures systematic mismatch; variance measures sensitivity of f̂(x) to the sampled training set.
- ✓

  σ² is irreducible noise from the data-generating process y = f(x) + ε; even perfect f(x) can’t beat it under squared loss.
- ✓

  Underfitting typically corresponds to high bias; overfitting typically corresponds to high variance.
- ✓

  Increasing model flexibility often decreases bias but increases variance; regularization often does the opposite.
- ✓

  More data usually reduces variance (stabilizes the learned predictor) and can sometimes reduce bias indirectly.
- ✓

  Ensembles reduce variance by averaging, especially when individual models are not highly correlated.
- ✓

  Bias and variance can vary across input space; scarce-data regions often have higher variance.

## Common Mistakes

- ✗

  Treating bias–variance as something you can read off from a single trained model without considering randomness over training sets.
- ✗

  Assuming overfitting is only about model size; the core issue is instability (variance), which can come from many sources (features, noise, training procedure).
- ✗

  Forgetting the noise term σ² and expecting test error to go to 0 even when the labels are inherently noisy.
- ✗

  Mixing up Bias(x) with (Bias(x))² in the decomposition; the squared term is what appears in MSE.

## Practice

easy

At a fixed x, suppose f(x) = 5 and the learned predictor satisfies E\_D[f̂(x)] = 4 with Var\_D(f̂(x)) = 2. The noise variance is σ² = 3. Compute the expected test MSE at x under squared loss.

**Hint:** Use E[(f̂ − y)²] = (E[f̂] − f)² + Var(f̂) + σ².

Show solution

Bias(x) = E[f̂(x)] − f(x) = 4 − 5 = −1

(Bias(x))² = 1

Var(x) = 2

σ² = 3

So expected MSE = 1 + 2 + 3 = 6.

hard

You average M predictors at a fixed x: Z̄ = (1/M)∑ᵢ Zᵢ. Assume each has Var(Zᵢ) = v and pairwise correlation Corr(Zᵢ, Zⱼ) = ρ for i ≠ j. Derive Var(Z̄).

**Hint:** Use Var(∑ Zᵢ) = ∑ Var(Zᵢ) + 2∑\_{i<j} Cov(Zᵢ, Zⱼ) and Cov = ρv.

Show solution

Var(Z̄) = Var((1/M)∑ᵢ Zᵢ) = (1/M²)Var(∑ᵢ Zᵢ)

Var(∑ᵢ Zᵢ) = ∑ᵢ Var(Zᵢ) + 2∑\_{i<j} Cov(Zᵢ, Zⱼ)

= Mv + 2·(number of pairs)·(ρv)

Number of pairs = M(M−1)/2

So Var(∑ᵢ Zᵢ) = Mv + 2·(M(M−1)/2)·ρv = Mv + M(M−1)ρv

Therefore:

Var(Z̄) = (1/M²)[Mv + M(M−1)ρv]

= (v/M) + ((M−1)/M)ρv

= v( (1−ρ)/M + ρ )

Checks: if ρ = 0 → v/M; if ρ = 1 → v.

medium

A learner compares two models A and B. Model A has higher training error but similar validation error compared to B; model B has very low training error but noticeably worse validation error. Using bias–variance language, diagnose A vs B and propose one concrete change to improve each.

**Hint:** Think: high bias shows up as high training and validation error; high variance shows up as low training but high validation error.

Show solution

Model A: higher training error suggests it may be underfitting (higher bias). If validation error is similar to B, A may be too simple or too regularized. Improvement: increase capacity (e.g., more features, deeper model) or reduce regularization.

Model B: very low training error but worse validation error indicates overfitting (higher variance). Improvement: add regularization (e.g., L2, dropout, pruning), simplify the model, gather more data, or use bagging/ensembling.

## Connections

[Cross-Validation](/tech-tree/cross-validation/)

[Ensemble Methods](/tech-tree/ensemble-methods/)

[Regularization (Ridge/Lasso)](/tech-tree/regularization/)

[Learning Curves](/tech-tree/learning-curves/)

[Decision Trees](/tech-tree/decision-trees/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
