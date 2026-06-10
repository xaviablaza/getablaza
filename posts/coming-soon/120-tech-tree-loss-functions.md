---
title: Loss Functions
description: Measuring model error. MSE, cross-entropy, hinge loss, custom losses.
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
inspiration_url: https://templeton.host/tech-tree/loss-functions/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/loss-functions/](https://templeton.host/tech-tree/loss-functions/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Loss Functions

Machine LearningDifficulty: ★★★★☆Depth: 9Unlocks: 2

Measuring model error. MSE, cross-entropy, hinge loss, custom losses.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Pointwise loss: a scalar function L(y, y\_hat) that measures error for a single example.
- -Empirical risk: the average of pointwise losses over a dataset, which serves as the training objective to minimize.
- -Differentiability/subdifferentiability of the loss: existence of gradients or subgradients so optimization methods can update parameters.

## Key Symbols & Notation

L(y, y\_hat) - pointwise loss function (true label y, prediction y\_hat).R\_hat(theta) - empirical risk = (1/n) sum\_i L(y\_i, f(x\_i; theta))

## Essential Relationships

- -R\_hat(theta) is the dataset average of the pointwise loss L(y, y\_hat).
- -When L is differentiable or has a subgradient, the (sub)gradient of R\_hat with respect to model parameters gives the direction for parameter updates (optimization).

## Prerequisites (3)

[Machine Learning Introduction5 atoms](/tech-tree/ml-intro/)[Cross-Entropy5 atoms](/tech-tree/cross-entropy/)[Convex Functions4 atoms](/tech-tree/convexity/)

## Unlocks (2)

[RLHFlvl 5](/tech-tree/rlhf/)[Task Discretizationlvl 5](/tech-tree/task-discretization/)

## Referenced by (4)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (4)

[pipelineBusiness

The OBJECTIVE panel of the pipeline maps directly to loss functions - the formal specification of what the model is trying to minimize](/business/pipeline/)[Utility FunctionBusiness

ML's operationalization of a utility function (inverted) - MSE, cross-entropy, and custom losses each encode a different definition of what 'good' means for a model](/business/utility-function/)[competitive moatBusiness

Loss functions are the mathematical formalization of verifiers - they define what 'good' means for a model. The moat-in-verifiers thesis is essentially that defining and computing the right loss (evaluation criteria, domain-specific quality gates) is harder and more defensible than optimizing against it](/business/competitive-moat/)[Quality SystemsBusiness

Defining 'quality' for an AI system means choosing a loss function - what errors cost, which failure modes matter more, how to weight precision vs recall. Quality metrics are domain-specific loss functions.](/business/quality-systems/)

Advanced Learning Details

### Graph Position

133

Depth Cost

2

Fan-Out (ROI)

2

Bottleneck Score

9

Chain Length

### Cognitive Load

7

Atomic Elements

47

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (19)

- - Loss function: a nonnegative scalar-valued function ℓ(y, ŷ) that measures error for one example (true label y, prediction ŷ)
- - Per-example vs aggregate loss: distinction between a single-example loss and an aggregated dataset objective
- - Empirical risk (training loss): average loss on the training set, used as the optimization objective
- - Expected (population) risk: the expectation of the per-example loss under the true data distribution
- - Empirical Risk Minimization (ERM): training principle of minimizing empirical risk to learn model parameters
- - Mean Squared Error (MSE) loss: squared-difference loss commonly used for regression
- - Absolute (L1) loss: absolute-difference loss, less sensitive to outliers than MSE
- - Hinge loss: margin-based loss (used in SVMs) that penalizes examples within or on the wrong side of the margin
- - 0–1 loss: indicator loss that equals 1 for misclassification and 0 otherwise (nonconvex, non-differentiable)
- - Surrogate losses: convex/differentiable losses (e.g., hinge, cross-entropy) used in place of 0–1 loss for tractable optimization
- - Margin: the signed quantity y·f(x) measuring confidence/distance to decision boundary in binary classification
- - Differentiability (of a loss) and its practical impact: whether gradients exist and how that affects use of gradient-based optimizers
- - Subgradients and nondifferentiable losses: concept of subgradient methods for optimizing nondifferentiable objectives
- - Regularized objective: combining loss with a penalty (e.g., λ·R(θ)) to control model complexity
- - Custom loss design: constructing loss functions to handle class imbalance, asymmetric costs, robustness, or domain-specific criteria
- - Robustness of loss functions: how different losses respond to outliers (e.g., MSE sensitive, L1 more robust)
- - Batch vs. per-sample optimization: computing gradients/updates using single examples, mini-batches, or full-batch averages
- - Loss as (negative) log-likelihood under model assumptions: interpreting certain losses as arising from probabilistic noise models (e.g., MSE from Gaussian noise)
- - Surrogate vs target metric gap: training loss may differ from evaluation metric (e.g., optimizing cross-entropy while evaluating accuracy)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Training a model is mostly the art of turning “what we want” into a single number we can minimize. That single number is built from a loss function.

TL;DR:

A loss function L(y, ŷ) measures error on one example; empirical risk R̂(θ) averages it over data. Good losses encode the right behavior (e.g., calibrated probabilities vs large margins), match output types (real-valued vs probabilities), and are differentiable or subdifferentiable so gradient-based optimization can work. Common choices: MSE for regression, cross-entropy for probabilistic classification, hinge loss for margin-based classifiers, plus custom losses when the task metric isn’t directly optimizable.

## What Is a Loss Function?

### Why we need a loss at all

A learning algorithm needs a feedback signal: given a prediction ŷ and a true target y, how bad was the prediction? In machine learning we usually want something we can:

1. 1)**Compute per example** (so we can aggregate over a dataset)
2. 2)**Differentiate** (so we can update parameters θ via gradients)
3. 3)**Optimize** (ideally with stable, predictable behavior)

A **pointwise loss** is a scalar function

L(y, ŷ) ∈ ℝ

that measures the error on a **single** example.

Given a dataset {(xᵢ, yᵢ)}ᵢ₌₁ⁿ and a model f(x; θ) producing ŷᵢ = f(xᵢ; θ), the training objective is typically the **empirical risk**:

R̂(θ) = (1/n) ∑ᵢ L(yᵢ, f(xᵢ; θ))

This turns learning into an optimization problem:

θ\* = argmin\_θ R̂(θ)

### Loss vs metric (don’t conflate them)

A **metric** is what you care about at evaluation time (accuracy, F1, BLEU, AUC, etc.). A **loss** is what you minimize during training. They often differ because many metrics are:

- •discontinuous (accuracy jumps when you cross a threshold)
- •non-differentiable
- •unstable for gradient descent

Loss functions are usually **surrogates**: smooth (or piecewise smooth) objectives that correlate with the metric but are easier to optimize.

### The “shape” of a loss encodes behavior

Losses don’t just say “wrong or right”; they encode *how* wrong. For example:

- •Squared error heavily punishes large mistakes.
- •Cross-entropy punishes confident wrong probabilities extremely.
- •Hinge loss encourages a **margin**, not just correctness.

The choice of loss is therefore a modeling decision, not a minor detail.

### Differentiability and subdifferentiability

Most modern training uses gradients. For that, we want ∂L/∂ŷ to exist (at least almost everywhere). Some useful losses are not differentiable everywhere (e.g., hinge, absolute error). For convex piecewise-linear losses, we can use **subgradients**.

A quick mental model:

- •**Differentiable**: you can compute a gradient ∇θ R̂(θ) and use gradient descent/Adam.
- •**Subdifferentiable**: you can compute a subgradient and still optimize with subgradient methods (or autodiff handles piecewise definitions).

Even in deep learning, many “non-smooth” losses are fine because the non-differentiable points form a set of measure zero; optimization typically proceeds with valid gradients almost everywhere.

## Core Mechanic 1: Pointwise Loss → Empirical Risk (and Gradients)

### Why this decomposition matters

It’s tempting to see training as “minimize a big function.” In practice, the *big function* is built from many small ones.

- •The **pointwise loss** L(yᵢ, ŷᵢ) tells you how one example contributes.
- •The **empirical risk** aggregates these contributions.

This structure enables mini-batch training: you estimate the full gradient using a small subset of examples.

### From loss to gradient: the chain rule pipeline

Suppose the model output is ŷ = f(x; θ). Then

R̂(θ) = (1/n) ∑ᵢ L(yᵢ, f(xᵢ; θ))

Differentiate w.r.t. θ:

∇θ R̂(θ)

= ∇θ ( (1/n) ∑ᵢ L(yᵢ, f(xᵢ; θ)) )

= (1/n) ∑ᵢ ∇θ L(yᵢ, f(xᵢ; θ))

Now apply the chain rule for each term:

∇θ L(yᵢ, f(xᵢ; θ))

= (∂L/∂ŷᵢ) · ∇θ f(xᵢ; θ)

So losses matter because they determine **∂L/∂ŷ**, the “error signal” that gets backpropagated.

### Mini-batches: stochastic empirical risk

For a mini-batch B of size m, we use:

R̂\_B(θ) = (1/m) ∑ᵢ∈B L(yᵢ, f(xᵢ; θ))

and update parameters using ∇θ R̂\_B(θ). This is an unbiased estimate of the full gradient when B is sampled uniformly.

### Output type drives loss choice

Before picking a loss, identify what ŷ represents:

- •**Regression**: ŷ ∈ ℝ (or ℝᵈ)
- •**Binary probability**: ŷ ∈ (0, 1)
- •**Multiclass probability**: **p̂** ∈ Δᵏ (simplex: p̂ⱼ ≥ 0, ∑ⱼ p̂ⱼ = 1)
- •**Logits**: **z** ∈ ℝᵏ (unnormalized scores); softmax converts logits to probabilities

Loss functions are often defined in terms of probabilities, but implemented with logits for numerical stability.

### A comparison table (what you optimize changes what you get)

| Task / Output | Common loss L | What it encourages | Typical model output |
| --- | --- | --- | --- |
| Regression (real-valued) | MSE: (1/2)(ŷ − y)² | Mean prediction; large errors costly | ŷ ∈ ℝ |
| Regression (robust) | MAE: | ŷ − y |  | Median prediction; less sensitive to outliers | ŷ ∈ ℝ |
| Binary classification (probabilistic) | Logistic / BCE | Calibrated probabilities | logit z or p̂ |
| Multiclass classification (probabilistic) | Cross-entropy | Correct class probability → 1 | logits **z**, softmax |
| Margin-based classification | Hinge | Large margin separation | score s or **w**ᵀ**x** |

The same dataset can yield qualitatively different models depending on whether you optimize probability calibration (cross-entropy) or margins (hinge).

## Core Mechanic 2: Canonical Losses (MSE, Cross-Entropy, Hinge) and Their Geometry

### 1) Mean Squared Error (MSE)

#### Why MSE is so common

MSE makes sense when:

- •targets are real-valued
- •noise is roughly Gaussian
- •you want to punish large deviations strongly

Pointwise MSE is often written with a 1/2 for cleaner derivatives:

L(y, ŷ) = (1/2)(ŷ − y)²

Derivative wrt prediction:

∂L/∂ŷ

= ∂/∂ŷ [ (1/2)(ŷ − y)² ]

= (1/2) · 2(ŷ − y)

= (ŷ − y)

This is a very clean error signal: “prediction minus truth.”

For vector-valued regression y ∈ ℝᵈ, you often use:

L(**y**, **ŷ**) = (1/2)‖**ŷ** − **y**‖²

with gradient:

∇\_{**ŷ**} L = **ŷ** − **y**

#### What can go wrong

If your data has heavy-tailed noise or outliers, squared error can over-focus on a few extreme points. A robust alternative is MAE or Huber loss.

---

### 2) Cross-Entropy (Log Loss)

You already know cross-entropy conceptually (H(p, q) = H(p) + KL(p‖q)). Here we connect it directly to the training loss and its gradients.

#### Binary cross-entropy (BCE)

For y ∈ {0, 1} and predicted probability p̂ ∈ (0, 1):

L(y, p̂) = −[ y log(p̂) + (1 − y) log(1 − p̂) ]

This is the negative log-likelihood of a Bernoulli model.

If the model outputs a logit z ∈ ℝ with p̂ = σ(z) = 1/(1 + e^(−z)), the BCE gradient wrt z has a beautifully simple form:

First, note:

∂L/∂p̂ = −( y/p̂ − (1 − y)/(1 − p̂) )

and

∂p̂/∂z = p̂(1 − p̂)

Chain rule:

∂L/∂z

= (∂L/∂p̂)(∂p̂/∂z)

= −( y/p̂ − (1 − y)/(1 − p̂) ) · p̂(1 − p̂)

= −( y(1 − p̂) − (1 − y)p̂ )

= p̂ − y

So for logistic regression / binary classification:

∂L/∂z = p̂ − y

This mirrors MSE’s “prediction minus truth,” but in probability space.

#### Multiclass cross-entropy

Let y be a one-hot vector over K classes, and **p̂** = softmax(**z**) where:

p̂ⱼ = exp(zⱼ) / ∑ₖ exp(zₖ)

Cross-entropy loss:

L(**y**, **p̂**) = −∑ⱼ yⱼ log(p̂ⱼ)

If y is one-hot with true class c, this simplifies to:

L = −log(p̂\_c)

A key gradient identity (used constantly in deep learning):

∂L/∂zⱼ = p̂ⱼ − yⱼ

That is: **softmax + cross-entropy** yields a stable gradient of “predicted distribution minus target distribution.”

#### Geometry: why it punishes confident mistakes

If the true class is c but p̂\_c is tiny, then −log(p̂\_c) is huge. That’s exactly the point: the loss is extremely sensitive to *confident wrong* predictions.

---

### 3) Hinge Loss (Margin-Based)

#### Why hinge exists

Sometimes you don’t care about calibrated probabilities; you care about a decision boundary with a safety buffer. Hinge loss is a convex surrogate for 0–1 classification loss that promotes a **margin**.

For binary labels y ∈ {−1, +1} and a score s (often s = **w**ᵀ**x** + b):

L(y, s) = max(0, 1 − y s)

Interpretation:

- •If y s ≥ 1, the point is correctly classified with margin ≥ 1 → loss 0
- •If 0 < y s < 1, correct but too close to boundary → positive loss
- •If y s ≤ 0, misclassified → even larger loss

#### Subgradient

Hinge is not differentiable at y s = 1, but it is subdifferentiable.

For the score s:

If 1 − y s < 0 ⇒ L = 0 ⇒ ∂L/∂s = 0

If 1 − y s > 0 ⇒ L = 1 − y s ⇒ ∂L/∂s = −y

At 1 − y s = 0 ⇒ subgradient set includes values between 0 and −y

This piecewise behavior is what creates the “support vectors”: only points violating the margin contribute gradients.

---

### Choosing between cross-entropy and hinge (a practical comparison)

| Criterion | Cross-entropy | Hinge |
| --- | --- | --- |
| Output interpretation | Probabilities (calibration-friendly) | Scores / margins |
| Loss on very wrong confident predictions | Very large | Linear in violation |
| Optimization landscape | Smooth (with softmax/sigmoid) | Piecewise-linear (subgradients) |
| Typical use | Neural nets, probabilistic models | SVMs, margin-focused classifiers |

Cross-entropy usually wins in deep learning because it works naturally with probabilistic outputs and backprop, but hinge can be useful when margin is the primary concern.

## Application/Connection: Designing and Customizing Losses

### Why custom losses are common

Real tasks rarely match “plain regression” or “plain classification.” You may have:

- •class imbalance
- •different costs for false positives vs false negatives
- •multiple objectives (accuracy + fairness + latency)
- •structured outputs (sequences, boxes, graphs)
- •a metric that is non-differentiable (F1, IoU, BLEU)

Custom losses are how you encode these realities into optimization.

### Weighted losses (cost-sensitive learning)

Suppose binary classification where positive examples are rare. A standard BCE might be minimized by predicting “negative” too often.

Weighted BCE:

L(y, p̂) = −[ α y log(p̂) + β (1 − y) log(1 − p̂) ]

- •α > β emphasizes recall on positives
- •β > α emphasizes precision / avoiding false positives

For multiclass, use class weights w\_c:

L = − w\_c log(p̂\_c)

This is simple and effective, but you must tune weights carefully; extreme weights can destabilize training.

### Label smoothing (a small tweak, big effect)

Instead of one-hot targets, use a softened target distribution:

ỹⱼ = (1 − ε) yⱼ + ε / K

Then train with cross-entropy to ỹ. Benefits:

- •reduces overconfidence
- •improves calibration
- •can improve generalization

It changes the gradient target from **y** to **ỹ**, preventing the model from pushing logits to extreme values.

### Robust regression: Huber loss

To interpolate between MSE (sensitive) and MAE (robust), use Huber with threshold δ:

Let r = ŷ − y.

L(r) =

- •(1/2) r² if |r| ≤ δ
- •δ(|r| − (1/2)δ) if |r| > δ

Derivative wrt ŷ (i.e., wrt r):

∂L/∂ŷ =

- •r if |r| ≤ δ
- •δ · sign(r) if |r| > δ

So small errors behave like MSE, but large errors have bounded influence like MAE.

### Multi-task losses: weighted sums

If your model predicts multiple outputs (say classification + bounding box regression), you may use:

L\_total = λ₁ L₁ + λ₂ L₂

This is easy to write, but hard to tune. If λ₂ is too large, the model may ignore task 1.

A useful checklist:

- •Are losses on comparable scales?
- •Do gradients from each task have similar magnitudes?
- •Do you need dynamic weighting (learned λ’s or normalization)?

### When the metric is non-differentiable

Many “true” metrics are not differentiable. Common strategies:

1. 1)**Surrogate loss** (most common)

- •Use cross-entropy instead of accuracy
- •Use smooth IoU approximations for segmentation

2. 2)**Reinforcement learning / policy gradients**

- •Optimize expected reward E[R]
- •Used in sequence generation and RLHF

3. 3)**Direct search / black-box optimization**

- •Not typical for deep nets, but used in some hyperparameter or prompt tuning loops

### Numerical stability: implement losses carefully

Cross-entropy with softmax can overflow if you compute exp(z) naively. In practice you compute:

log softmax(z\_c) = z\_c − log(∑ⱼ exp(zⱼ))

using the log-sum-exp trick:

log(∑ⱼ exp(zⱼ))

= a + log(∑ⱼ exp(zⱼ − a))

where a = maxⱼ zⱼ.

Similarly, binary cross-entropy is best computed from logits directly (many libraries provide a “BCEWithLogits” function).

### Connection to empirical risk minimization (ERM)

At a high level, “training” is ERM: minimize R̂(θ). The loss is your stand-in for what you actually care about.

A good loss should be:

- •aligned with the task goal (or a good surrogate)
- •stable for optimization (smooth enough, well-scaled gradients)
- •consistent with output interpretation (probabilities vs scores)
- •compatible with your optimizer (differentiable or subdifferentiable)

Loss choice is one of the few levers that directly changes what gradients you get, and therefore what model you end up with.

## Worked Examples (3)

### MSE for linear regression: compute empirical risk and gradient

We have a 1D linear model ŷ = w x (no bias for simplicity). Dataset: (x₁, y₁) = (1, 2), (x₂, y₂) = (2, 3). Use pointwise MSE L = (1/2)(ŷ − y)². Compute R̂(w) and dR̂/dw at w = 1.

1. Model predictions at w = 1:

   ŷ₁ = w x₁ = 1·1 = 1

   ŷ₂ = w x₂ = 1·2 = 2
2. Pointwise losses:

   L₁ = (1/2)(ŷ₁ − y₁)² = (1/2)(1 − 2)² = (1/2)·1 = 0.5

   L₂ = (1/2)(ŷ₂ − y₂)² = (1/2)(2 − 3)² = (1/2)·1 = 0.5
3. Empirical risk:

   R̂(w=1) = (1/2)(L₁ + L₂) = (1/2)(0.5 + 0.5) = 0.5
4. Differentiate R̂(w):

   R̂(w) = (1/n) ∑ᵢ (1/2)(w xᵢ − yᵢ)²

   So

   dR̂/dw = (1/n) ∑ᵢ (1/2)·2(w xᵢ − yᵢ)·xᵢ

   = (1/n) ∑ᵢ (w xᵢ − yᵢ)xᵢ
5. Evaluate at w = 1:

   dR̂/dw = (1/2)[(1·1 − 2)·1 + (1·2 − 3)·2]

   = (1/2)[(−1)·1 + (−1)·2]

   = (1/2)(−3)

   = −1.5

**Insight:** The gradient is negative, so increasing w will decrease the loss—exactly what you’d expect since both predictions were too small. Notice how MSE yields a clean residual (ŷ − y) that scales the update.

### Binary cross-entropy from logits: compute loss and gradient signal

Single example with label y = 1. Model outputs a logit z = −1. Compute p̂ = σ(z), BCE loss L(y, p̂), and ∂L/∂z.

1. Convert logit to probability:

   p̂ = σ(z) = 1/(1 + e^(−z))

   With z = −1:

   p̂ = 1/(1 + e^(1)) ≈ 1/(1 + 2.718) ≈ 0.2689
2. Binary cross-entropy:

   L = −[ y log(p̂) + (1 − y) log(1 − p̂) ]

   With y = 1:

   L = −log(p̂) = −log(0.2689) ≈ 1.313
3. Gradient wrt logit uses the identity ∂L/∂z = p̂ − y:

   ∂L/∂z = 0.2689 − 1 = −0.7311
4. Interpretation of the sign:

   Negative gradient means increasing z will reduce loss.

   Increasing z increases p̂, moving probability toward the correct label y = 1.

**Insight:** Cross-entropy creates a strong gradient when the model is confidently wrong. Here the model assigned low probability to the true class, so ∂L/∂z is large in magnitude.

### Hinge loss: identify support vectors and subgradients

Binary labels y ∈ {−1, +1}. Scores are s = w x (assume w is absorbed into s). We have three examples with (y, s): (1, 2.0), (1, 0.2), (−1, 0.3). Compute hinge losses and ∂L/∂s (subgradient) where applicable.

1. Recall hinge loss:

   L(y, s) = max(0, 1 − y s)
2. Example A: (y, s) = (1, 2.0)

   1 − y s = 1 − 1·2.0 = −1.0

   L = max(0, −1.0) = 0

   Gradient signal: ∂L/∂s = 0 (margin satisfied)
3. Example B: (y, s) = (1, 0.2)

   1 − y s = 1 − 1·0.2 = 0.8

   L = 0.8

   Since 1 − y s > 0, use ∂L/∂s = −y = −1
4. Example C: (y, s) = (−1, 0.3)

   Compute y s = (−1)·0.3 = −0.3

   1 − y s = 1 − (−0.3) = 1.3

   L = 1.3

   Again 1 − y s > 0, so ∂L/∂s = −y = −(−1) = +1

**Insight:** Only points inside the margin (or misclassified) produce non-zero gradients. This is the core reason SVMs depend on “support vectors”: many points are ignored once they are comfortably correct.

## Key Takeaways

- ✓

  A **pointwise loss** L(y, ŷ) measures error on one example; **empirical risk** R̂(θ) = (1/n)∑ᵢ L(yᵢ, f(xᵢ; θ)) is the training objective.
- ✓

  Loss choice determines the backpropagated error signal ∂L/∂ŷ (or ∂L/∂logit), which strongly affects what the model learns.
- ✓

  MSE L = (1/2)(ŷ − y)² yields gradient ∂L/∂ŷ = (ŷ − y) and heavily penalizes large errors; it’s natural for Gaussian-like noise.
- ✓

  Cross-entropy is the negative log-likelihood for classification; with logits it gives a clean gradient: for softmax/BCE, the signal is (p̂ − y).
- ✓

  Hinge loss L = max(0, 1 − y s) encourages large margins and uses subgradients; only margin-violating points contribute to updates.
- ✓

  Custom losses (weights, label smoothing, Huber, multi-task sums) encode real-world constraints like imbalance, robustness, and multiple objectives.
- ✓

  Many evaluation metrics are non-differentiable; losses are often smooth surrogates chosen for optimization stability and alignment with the metric.
- ✓

  Numerical stability matters: compute cross-entropy from logits (log-sum-exp) to avoid overflow/underflow.

## Common Mistakes

- ✗

  Optimizing a loss that doesn’t match the model output type (e.g., applying MSE to logits for classification without thinking about probability interpretation).
- ✗

  Assuming the evaluation metric and training loss must be identical; often you need a surrogate loss to get usable gradients.
- ✗

  Ignoring scaling: combining multiple losses without λ weights (or with poorly tuned λ) can cause one objective to dominate.
- ✗

  Implementing cross-entropy naively with softmax(exp(z)) and log, causing numerical overflow; prefer stable “from logits” implementations.

## Practice

easy

You have a regression target y ∈ ℝ and predictions ŷ. (a) Write the pointwise MSE and MAE losses. (b) For each, compute ∂L/∂ŷ (use subgradient for MAE).

**Hint:** MSE is quadratic; MAE is absolute value. Remember d|r|/dr = sign(r) for r ≠ 0, and subgradient at 0 is [−1, 1].

Show solution

(a)

MSE: L = (1/2)(ŷ − y)²

MAE: L = |ŷ − y|

(b)

For MSE:

∂L/∂ŷ = (ŷ − y)

For MAE, let r = ŷ − y:

If r > 0: ∂L/∂ŷ = +1

If r < 0: ∂L/∂ŷ = −1

If r = 0: subgradient ∂L/∂ŷ ∈ [−1, 1]

medium

Multiclass cross-entropy: Suppose K = 3, logits **z** = (2, 0, −1). (a) Compute softmax probabilities **p̂**. (b) If the true class is c = 2 (1-indexed), compute L = −log(p̂\_c).

**Hint:** Compute exp(zⱼ), divide by the sum. You can factor out max(zⱼ) = 2 for stability: exp(zⱼ − 2).

Show solution

(a)

Let a = max(z) = 2.

Compute exp(z − a):

exp(2−2)=exp(0)=1

exp(0−2)=exp(−2)≈0.1353

exp(−1−2)=exp(−3)≈0.0498

Sum ≈ 1 + 0.1353 + 0.0498 = 1.1851

So

p̂₁ ≈ 1/1.1851 ≈ 0.8438

p̂₂ ≈ 0.1353/1.1851 ≈ 0.1142

p̂₃ ≈ 0.0498/1.1851 ≈ 0.0420

(b)

True class c = 2 ⇒ L = −log(p̂₂)

L ≈ −log(0.1142) ≈ 2.170

medium

Hinge loss and margins: For y ∈ {−1, +1} and s = **w**ᵀ**x**, consider three points with (y, s): (1, 1.2), (−1, −0.4), (−1, 2.0). (a) Compute hinge loss for each. (b) Identify which points contribute non-zero subgradients.

**Hint:** Compute 1 − y s. If it’s ≤ 0, loss is 0 and gradient is 0.

Show solution

(a) L = max(0, 1 − y s)

Point 1: y s = 1·1.2 = 1.2 ⇒ 1 − y s = −0.2 ⇒ L = 0

Point 2: y s = (−1)·(−0.4) = 0.4 ⇒ 1 − y s = 0.6 ⇒ L = 0.6

Point 3: y s = (−1)·(2.0) = −2.0 ⇒ 1 − y s = 3.0 ⇒ L = 3.0

(b) Non-zero subgradients occur when 1 − y s > 0:

Point 2 and Point 3 contribute; Point 1 does not.

## Connections

Next steps and related nodes:

- •[RLHF](/tech-tree/rlhf/) — reward models use losses (often cross-entropy-style ranking losses or regression losses) to fit human preference signals, then policy optimization optimizes expected reward.
- •[Task Discretization](/tech-tree/task-discretization/) — designing measurable sub-objectives is largely about designing losses or reward functions that reflect progress.

Useful background refreshers:

- •[Cross-Entropy](/tech-tree/cross-entropy/)
- •[Convex Functions](/tech-tree/convex-functions/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
