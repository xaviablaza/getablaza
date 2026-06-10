---
title: Logistic Regression
description: Binary classification. Sigmoid function, cross-entropy loss.
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
permalink: /tech-tree/logistic-regression/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Logistic Regression

Machine LearningDifficulty: ★★★☆☆Depth: 9Unlocks: 12

Binary classification. Sigmoid function, cross-entropy loss.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Linear predictor (score): weighted sum of features plus bias, i.e. the model's raw score for an input
- -Sigmoid (logistic) function: maps a real-valued score to a probability in [0,1]
- -Binary cross-entropy loss: negative log-likelihood for Bernoulli labels (per-example loss)

## Key Symbols & Notation

w - parameter (weight) vector (including bias)

## Essential Relationships

- -Predicted probability p is sigmoid of the linear score: p = sigmoid(w dot x)
- -Per-example loss is the negative log-likelihood (cross-entropy): L = -[ y\*log(p) + (1-y)\*log(1-p) ]

## Prerequisites (3)

[Machine Learning Introduction5 atoms](/tech-tree/ml-intro/)[Maximum Likelihood Estimation6 atoms](/tech-tree/mle/)[Gradient Descent6 atoms](/tech-tree/gradient-descent/)

## Unlocks (1)

[Neural Networkslvl 4](/tech-tree/neural-networks/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[Credit UtilizationBusiness

FICO models are logistic regressions where utilization ratio is a key feature; understanding how a continuous ratio maps through a sigmoid to a probability of default clarifies why utilization thresholds (30%, 10%) produce nonlinear score impacts.](/business/credit-utilization/)[ChurnBusiness

Churn prediction is the canonical binary classification problem. Logistic regression (sigmoid output = P(churn | features), cross-entropy loss, decision threshold) is the textbook first model taught for churn and remains a production baseline.](/business/churn/)

Advanced Learning Details

### Graph Position

112

Depth Cost

12

Fan-Out (ROI)

5

Bottleneck Score

9

Chain Length

### Cognitive Load

6

Atomic Elements

35

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (14)

- - Sigmoid (logistic) function as a squashing map σ(z)=1/(1+e^{-z}) that converts a real-valued score to a probability in (0,1)
- - Linear predictor (score) z = w^T x + b (or w^T x when bias implicit) that combines inputs with parameters
- - Probabilistic binary model p(y=1 | x; w) = σ(w^T x) (Bernoulli conditional model parametrized by w)
- - Per-example Bernoulli likelihood for binary labels under the sigmoid model
- - Cross-entropy loss (negative log-likelihood) for a single example: ℓ(x,y;w) = -[y log p + (1-y) log(1-p)] where p = σ(w^T x)
- - Overall empirical loss / cost J(w) as the average (or sum) of per-example cross-entropies over the dataset
- - Decision rule for classification from predicted probability (e.g., predict class 1 if p≥0.5)
- - Decision boundary: the geometric set where the model is indifferent (w^T x + b = 0) - a linear separator in input space
- - Log-odds (logit): log(p/(1-p)) equals the linear predictor w^T x + b - interpretation linking linear score to odds
- - Interpretation of weights: a unit change in a feature shifts the log-odds by the corresponding weight
- - Vectorized notation for model predictions and loss using data matrix X and label vector y (e.g., σ(Xw), J(w) = -∑[y log σ(Xw) + (1-y) log(1-σ(Xw))])
- - Sigmoid derivative identity σ'(z) = σ(z) (1 - σ(z)), used in computing gradients
- - Analytic form of the gradient for one example: ∂ℓ/∂w = (σ(w^T x) - y) x (and analogous vectorized form)
- - Convexity of the logistic (cross-entropy) loss with respect to parameters w (so optimization has no non-global local minima)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Logistic regression is the “hello world” of modern classification: a linear score turned into a probability, trained by a loss that directly matches how Bernoulli (yes/no) data is generated. It’s simple enough to fully understand, but rich enough to connect straight into neural networks.

TL;DR:

Logistic regression models P(y = 1 | **x**) = σ(**w**·**x** + b). Train **w** (and b) by minimizing binary cross-entropy (negative log-likelihood). The gradient has a clean form: ∇ = (ŷ − y)**x** (and bias gradient ŷ − y), making it easy to optimize with gradient descent.

## What Is Logistic Regression?

### The problem it solves

In **binary classification**, each example has features **x** ∈ ℝᵈ and a label y ∈ {0, 1}. You want a model that, given **x**, outputs a *probability* that the label is 1:

- •Output near 1 ⇒ “very likely positive”
- •Output near 0 ⇒ “very likely negative”

Many models can produce a hard decision (0/1), but logistic regression is designed to produce a **calibrated probability** in [0, 1].

### Why we don’t just use linear regression

A linear model like **w**·**x** + b can be any real number: negative, > 1, etc. That’s not a valid probability.

We need two ingredients:

1. 1)A **linear predictor (score)**:

z = **w**·**x** + b

This is the raw “evidence” for the positive class.

2. 2)A **squashing function** that maps ℝ → [0, 1].

Logistic regression chooses the **sigmoid (logistic) function**:

σ(z) = 1 / (1 + e^(−z))

So the model is:

ŷ = P(y = 1 | **x**) = σ(**w**·**x** + b)

### Intuition: score → probability

The score z measures where **x** lies relative to a hyperplane.

- •Decision boundary is where z = 0

**w**·**x** + b = 0

- •If z is large and positive, σ(z) ≈ 1
- •If z is large and negative, σ(z) ≈ 0

So logistic regression is a **linear classifier** in geometry, but a **probabilistic model** in output.

### Odds and log-odds (why sigmoid is a natural choice)

A key reason logistic regression is so standard is that it models the **log-odds** as linear.

Define odds:

odds = P(y=1|**x**) / P(y=0|**x**) = p / (1 − p)

Log-odds (logit):

logit(p) = log(p / (1 − p))

Logistic regression assumes:

log(p / (1 − p)) = **w**·**x** + b

Solve for p:

Let z = **w**·**x** + b.

p / (1 − p) = e^z

p = e^z (1 − p)

p = e^z − e^z p

p + e^z p = e^z

p(1 + e^z) = e^z

p = e^z / (1 + e^z) = 1 / (1 + e^(−z)) = σ(z)

This shows sigmoid isn’t arbitrary: it’s what you get when you say “log-odds are linear in features.”

### Notation note: include bias in **w**

Sometimes we fold the bias into the weight vector by adding a constant feature x₀ = 1.

Define extended feature vector **x̃** = [1, x₁, …, x\_d] and **w̃** = [b, w₁, …, w\_d]. Then:

z = **w̃**·**x̃**

This can simplify implementations and derivations.

### Summary

Logistic regression is:

- •A linear scoring function z = **w**·**x** + b
- •A probabilistic output ŷ = σ(z)
- •A training objective that matches Bernoulli labels via maximum likelihood

## Core Mechanic 1: Linear Predictor and the Sigmoid

### Why start with a linear predictor?

The linear predictor is the simplest way to combine features:

z = **w**·**x** + b = ∑ⱼ wⱼ xⱼ + b

Motivation:

- •It’s **interpretable**: each feature contributes additively.
- •It’s **scalable**: works well in high dimensions.
- •It’s a strong baseline: many problems are close to linearly separable after good feature engineering.

### Geometry: a hyperplane decision boundary

The set of points where the model is indifferent (predicts 0.5) is where ŷ = 0.5.

Since σ(0) = 0.5, we have:

ŷ = 0.5 ⇔ z = 0 ⇔ **w**·**x** + b = 0

That equation describes a hyperplane.

- •**w** is perpendicular (normal) to the hyperplane.
- •b shifts the hyperplane.

Predicted class often uses a threshold:

predict 1 if ŷ ≥ 0.5 (equivalently z ≥ 0)

### Why the sigmoid specifically?

We want a function with:

- •Output in (0, 1)
- •Smooth, differentiable (for gradient descent)
- •Monotonic increasing (higher score ⇒ higher probability)

Sigmoid has these properties.

Key values:

- •σ(0) = 1/2
- •σ(z) → 1 as z → +∞
- •σ(z) → 0 as z → −∞

### Sensitivity: sigmoid derivative

Training needs gradients. Sigmoid has a famously convenient derivative.

Let p = σ(z) = 1 / (1 + e^(−z)).

Differentiate:

p = (1 + e^(−z))^(−1)

∂p/∂z = −1 · (1 + e^(−z))^(−2) · ∂/∂z (1 + e^(−z))

∂/∂z (1 + e^(−z)) = −e^(−z)

So:

∂p/∂z = (1 + e^(−z))^(−2) · e^(−z)

Now rewrite in terms of p:

p = 1 / (1 + e^(−z))

1 − p = e^(−z) / (1 + e^(−z))

Therefore:

p(1 − p) = [1 / (1 + e^(−z))] · [e^(−z) / (1 + e^(−z))] = e^(−z) / (1 + e^(−z))²

Thus:

∂p/∂z = p(1 − p)

This compact form is one reason logistic regression is so convenient.

### Interpretability: weight signs and magnitudes

Because log-odds are linear:

log(p/(1−p)) = **w**·**x** + b

Each weight wⱼ has a direct interpretation:

- •Increasing xⱼ by 1 increases log-odds by wⱼ (holding others fixed).
- •If wⱼ > 0, that feature pushes toward class 1.
- •If wⱼ < 0, it pushes toward class 0.

Caution: interpretation depends on feature scaling. If one feature is measured in large units, its weight will tend to be smaller.

### A tiny comparison table

| Component | Linear regression (for y ∈ ℝ) | Logistic regression (for y ∈ {0,1}) |
| --- | --- | --- |
| Score | **w**·**x** + b | **w**·**x** + b |
| Output | ŷ = score | ŷ = σ(score) ∈ (0,1) |
| Typical loss | squared error | binary cross-entropy |
| Probabilistic meaning | Gaussian noise assumption | Bernoulli likelihood |

This sets up the next step: choosing a loss that matches Bernoulli labels.

## Core Mechanic 2: Binary Cross-Entropy as Negative Log-Likelihood

### Why we need a special loss

For classification, we don’t just want “close numeric values.” We want:

- •confident correct predictions to be rewarded
- •confident wrong predictions to be punished strongly
- •a probabilistic interpretation (so “0.9” means something)

Binary cross-entropy (BCE) comes directly from **maximum likelihood estimation** for a Bernoulli model.

### Bernoulli model for labels

Assume for each input **x**, the label y is drawn as:

P(y = 1 | **x**) = p

P(y = 0 | **x**) = 1 − p

with p = σ(z) and z = **w**·**x** + b.

The Bernoulli probability mass function can be written compactly as:

P(y | **x**) = pʸ (1 − p)^(1−y)

because:

- •if y = 1 ⇒ p¹(1−p)⁰ = p
- •if y = 0 ⇒ p⁰(1−p)¹ = 1−p

### Likelihood for a dataset

Given N i.i.d. examples {(**xᵢ**, yᵢ)}:

L(**w**, b) = ∏ᵢ pᵢ^(yᵢ) (1 − pᵢ)^(1−yᵢ)

where pᵢ = σ(**w**·**xᵢ** + b).

Maximizing a product is awkward, so take logs:

log L = ∑ᵢ [ yᵢ log pᵢ + (1 − yᵢ) log(1 − pᵢ) ]

Maximum likelihood is equivalent to minimizing negative log-likelihood:

J(**w**, b) = − log L = − ∑ᵢ [ yᵢ log pᵢ + (1 − yᵢ) log(1 − pᵢ) ]

Often we average over N:

J = (1/N) ∑ᵢ ℓᵢ

with per-example loss:

ℓ = −[ y log p + (1 − y) log(1 − p) ]

That is the **binary cross-entropy loss**.

### Why BCE behaves the way we want

Consider one example.

- •If y = 1, the loss is ℓ = −log p
- •If p = 0.9 ⇒ ℓ ≈ 0.105
- •If p = 0.01 ⇒ ℓ ≈ 4.605 (large penalty)

- •If y = 0, the loss is ℓ = −log(1 − p)
- •If p = 0.1 ⇒ ℓ ≈ 0.105
- •If p = 0.99 ⇒ ℓ ≈ 4.605

So BCE strongly penalizes confident mistakes.

### Gradient: the clean “prediction minus label” form

This is the workhorse result that makes training simple.

For one example:

p = σ(z), z = **w**·**x** + b

ℓ = −[ y log p + (1 − y) log(1 − p) ]

We compute ∂ℓ/∂z.

Step 1: derivative of ℓ with respect to p:

∂ℓ/∂p = −[ y · (1/p) + (1 − y) · (−1/(1 − p)) ]

∂ℓ/∂p = − y/p + (1 − y)/(1 − p)

Step 2: chain rule with ∂p/∂z = p(1 − p):

∂ℓ/∂z = (∂ℓ/∂p)(∂p/∂z)

∂ℓ/∂z = ( − y/p + (1 − y)/(1 − p) ) · p(1 − p)

Distribute p(1 − p):

∂ℓ/∂z = −y(1 − p) + (1 − y)p

∂ℓ/∂z = −y + yp + p − yp

∂ℓ/∂z = p − y

So the derivative w.r.t. the score is:

∂ℓ/∂z = (p − y) = (ŷ − y)

Now apply z = **w**·**x** + b:

∂z/∂**w** = **x**

∂z/∂b = 1

Thus:

∇\_**w** ℓ = (ŷ − y)**x**

∂ℓ/∂b = (ŷ − y)

For the full dataset (averaged):

∇\_**w** J = (1/N) ∑ᵢ (ŷᵢ − yᵢ)\*\*xᵢ

∂J/∂b = (1/N) ∑ᵢ (ŷᵢ − yᵢ)

This is the key computational loop: predict p, compute error (p − y), accumulate gradients.

### Convexity (a practical perk)

For standard logistic regression (no hidden layers), the BCE objective is **convex** in (**w**, b). That means:

- •there is a single global minimum
- •gradient descent won’t get trapped in bad local minima (though it can still be slow)

This is a major difference from neural networks, where the objective is non-convex.

## Application/Connection: Training, Decision Thresholds, and the Bridge to Neural Networks

### Training with gradient descent (putting the pieces together)

A typical training step:

1. 1)Compute zᵢ = **w**·**xᵢ** + b
2. 2)Compute ŷᵢ = σ(zᵢ)
3. 3)Compute gradients:

- •g\_**w** = (1/N) ∑ᵢ (ŷᵢ − yᵢ)\*\*xᵢ
- •g\_b = (1/N) ∑ᵢ (ŷᵢ − yᵢ)

4. 4)Update parameters (learning rate η):

**w** ← **w** − η g\_**w**

b ← b − η g\_b

Because you already know gradient descent, the main learning here is: BCE + sigmoid makes the gradient become “prediction minus label.”

### Decision thresholds and costs

The model outputs a probability ŷ. Turning it into a label requires a threshold t.

- •Default: t = 0.5
- •Predict 1 if ŷ ≥ t

But in many real applications, false positives and false negatives have different costs.

Examples:

- •Medical screening: prefer fewer false negatives ⇒ lower threshold
- •Spam filtering: prefer fewer false positives ⇒ higher threshold

So logistic regression naturally supports *probability-based decision-making*.

### Evaluation metrics (quick orientation)

Accuracy is not always enough, especially with class imbalance.

Common choices:

- •Precision, recall, F1
- •ROC curve and AUC
- •Log loss (the same BCE, on held-out data)

BCE is a natural metric because it evaluates probability quality, not just hard labels.

### Regularization (brief but important)

To reduce overfitting, add a penalty on **w**.

L2 regularization (ridge):

J\_reg = J + (λ/2)‖**w**‖²

Gradient adds:

∇\_**w** J\_reg = ∇\_**w** J + λ**w**

(Usually the bias b is not regularized.)

L1 regularization (lasso) encourages sparsity, but its gradient uses subgradients and optimization needs more care.

### Numerical stability: logits and “BCE with logits”

Directly computing log(σ(z)) can cause issues when z is very large in magnitude.

In practice, libraries use a stable form often called **binary cross-entropy with logits**, where you pass z (the logit) directly.

This is a practical detail, but it matters for robust training.

### Connection to neural networks

Logistic regression is a 1-layer neural network:

- •Input: **x**
- •Linear layer: z = **w**·**x** + b
- •Activation: σ(z)
- •Loss: BCE

When you later learn neural networks, you’ll generalize the linear layer to multiple layers and nonlinearities. The final layer for binary classification often remains a sigmoid (or a 2-class softmax), and the loss remains cross-entropy.

So mastering logistic regression means you already understand:

- •linear layers
- •activations
- •cross-entropy objectives
- •gradient-based training

You’re standing right at the entrance to [Neural Networks](/tech-tree/neural-networks/).

## Worked Examples (3)

### Compute a prediction and interpret it (score → probability → decision)

Let **w** = (0.8, −0.4), b = −0.2. For input **x** = (2, 1), compute z, ŷ = σ(z), and the predicted class with threshold 0.5.

1. Compute the linear score:

   z = **w**·**x** + b

   = (0.8)(2) + (−0.4)(1) + (−0.2)

   = 1.6 − 0.4 − 0.2

   = 1.0
2. Map score to probability:

   ŷ = σ(z) = 1 / (1 + e^(−1.0))

   ≈ 1 / (1 + 0.3679)

   ≈ 0.7311
3. Apply threshold t = 0.5:

   ŷ ≈ 0.7311 ≥ 0.5 ⇒ predict class 1

**Insight:** The decision boundary is z = 0. Here z = 1 is on the positive side, and sigmoid turns that margin into a probability (about 73%).

### Compute binary cross-entropy loss for one example

Suppose the model predicts ŷ = 0.9 for an example whose true label is y = 1. Then compute the per-example BCE loss. Repeat for a confident wrong prediction ŷ = 0.01 when y = 1.

1. If y = 1, BCE loss is:

   ℓ = −[ y log ŷ + (1 − y) log(1 − ŷ) ]

   = −[ 1 · log(0.9) + 0 · log(0.1) ]

   = −log(0.9)

   ≈ 0.1053
2. For ŷ = 0.01 with y = 1:

   ℓ = −log(0.01)

   ≈ 4.6052

**Insight:** BCE is gentle when you’re confidently correct, but extremely harsh when you’re confidently wrong—exactly what you want for probabilistic classification.

### One gradient descent step on a single example (see the (ŷ − y)\*\*x\*\* pattern)

Single training example: **x** = (3, −1), y = 0. Start with **w** = (0, 0), b = 0. Use learning rate η = 0.1. Do one gradient descent update.

1. Compute score:

   z = **w**·**x** + b = 0

   So ŷ = σ(0) = 0.5
2. Compute gradients for one example:

   ∇\_**w** ℓ = (ŷ − y)**x**

   Here (ŷ − y) = 0.5 − 0 = 0.5

   So:

   ∇\_**w** ℓ = 0.5 · (3, −1) = (1.5, −0.5)

   Bias gradient:

   ∂ℓ/∂b = (ŷ − y) = 0.5
3. Update parameters:

   **w** ← **w** − η ∇\_**w** ℓ

   = (0, 0) − 0.1(1.5, −0.5)

   = (−0.15, 0.05)

   b ← b − η(∂ℓ/∂b)

   = 0 − 0.1(0.5)

   = −0.05

**Insight:** Because y = 0 but ŷ = 0.5 is too high, (ŷ − y) is positive, so the update moves **w** and b in a direction that reduces the score z on this example next time.

## Key Takeaways

- ✓

  Logistic regression uses a linear score z = **w**·**x** + b and converts it to a probability with the sigmoid σ(z).
- ✓

  The decision boundary ŷ = 0.5 corresponds to z = 0, a hyperplane with normal vector **w**.
- ✓

  The Bernoulli likelihood leads directly to binary cross-entropy: ℓ = −[ y log ŷ + (1 − y) log(1 − ŷ) ].
- ✓

  A crucial simplification: ∂ℓ/∂z = ŷ − y, giving ∇\_**w** ℓ = (ŷ − y)**x** and ∂ℓ/∂b = ŷ − y.
- ✓

  Logistic regression’s objective is convex, making optimization more reliable than many non-convex models.
- ✓

  Thresholds can be adjusted away from 0.5 to reflect unequal error costs; probabilities enable this flexibility.
- ✓

  Regularization like (λ/2)‖**w**‖² is commonly added to reduce overfitting and improves generalization.
- ✓

  Logistic regression is effectively a single-neuron neural network: linear layer + sigmoid + cross-entropy.

## Common Mistakes

- ✗

  Using mean squared error instead of binary cross-entropy, which usually yields worse probabilistic behavior and gradients for classification.
- ✗

  Forgetting the bias term b (or forgetting to include x₀ = 1 when folding bias into **w**), which can severely limit the decision boundary.
- ✗

  Interpreting weights without considering feature scaling; weights are only comparable when features are on comparable scales.
- ✗

  Computing log(σ(z)) and log(1−σ(z)) naively for large |z|, leading to numerical instability instead of using a stable “BCE with logits” formulation.

## Practice

easy

Given **w** = (1, −2), b = 0.5, and **x** = (1, 2), compute z, ŷ = σ(z), and the predicted label using threshold 0.5.

**Hint:** Compute z = 1·1 + (−2)·2 + 0.5, then apply σ(z). If z < 0 then ŷ < 0.5.

Show solution

z = (1)(1) + (−2)(2) + 0.5 = 1 − 4 + 0.5 = −2.5.

ŷ = σ(−2.5) = 1/(1+e^(2.5)) ≈ 1/(1+12.182) ≈ 0.0759.

Since ŷ < 0.5, predict label 0.

medium

Show that for BCE with sigmoid output, the derivative with respect to the logit z is ∂ℓ/∂z = ŷ − y.

**Hint:** Use ℓ = −[ y log ŷ + (1 − y) log(1 − ŷ) ], then chain rule: (∂ℓ/∂ŷ)(∂ŷ/∂z). Recall ∂σ/∂z = ŷ(1 − ŷ).

Show solution

Let ŷ = σ(z).

ℓ = −[ y log ŷ + (1 − y) log(1 − ŷ) ].

Compute:

∂ℓ/∂ŷ = −[ y(1/ŷ) + (1 − y)(−1/(1 − ŷ)) ] = −y/ŷ + (1 − y)/(1 − ŷ).

Also ∂ŷ/∂z = ŷ(1 − ŷ).

So:

∂ℓ/∂z = (−y/ŷ + (1 − y)/(1 − ŷ))·ŷ(1 − ŷ)

= −y(1 − ŷ) + (1 − y)ŷ

= −y + yŷ + ŷ − yŷ

= ŷ − y.

hard

One-step update with two examples (mini-batch): Start **w** = (0, 0), b = 0, η = 0.2. Examples: (**x₁**=(1,0), y₁=1) and (**x₂**=(0,1), y₂=0). Use the average gradient over the two examples to update **w** and b once.

**Hint:** With **w** = 0 and b = 0, both logits are 0 so both predictions are 0.5. Compute (ŷ − y) for each example, then average gradients: (1/N)∑(ŷ − y)**x**.

Show solution

Initial: z₁ = 0, z₂ = 0 ⇒ ŷ₁ = ŷ₂ = 0.5.

Errors:

(ŷ₁ − y₁) = 0.5 − 1 = −0.5

(ŷ₂ − y₂) = 0.5 − 0 = 0.5

Average weight gradient:

∇\_**w** J = (1/2)[(−0.5)(1,0) + (0.5)(0,1)]

= (1/2)[(−0.5, 0) + (0, 0.5)]

= (−0.25, 0.25)

Average bias gradient:

∂J/∂b = (1/2)[(−0.5) + (0.5)] = 0

Update:

**w** ← **w** − η∇\_**w**J = (0,0) − 0.2(−0.25, 0.25) = (0.05, −0.05)

b ← 0 − 0.2(0) = 0.

## Connections

- •Next: [Neural Networks](/tech-tree/neural-networks/)
- •Related foundations you used here:
- •[Maximum Likelihood Estimation](/tech-tree/maximum-likelihood-estimation/)
- •[Gradient Descent](/tech-tree/gradient-descent/)
- •Often paired with:
- •[Feature Scaling and Normalization](/tech-tree/feature-scaling/)
- •[Regularization](/tech-tree/regularization/)
- •[Model Evaluation Metrics](/tech-tree/classification-metrics/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
