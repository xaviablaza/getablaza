---
title: Machine Learning Introduction
description: Learning patterns from data. Supervised vs unsupervised learning.
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
permalink: /tech-tree/ml-intro/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Machine Learning Introduction

Machine LearningDifficulty: ★★★☆☆Depth: 8Unlocks: 26

Learning patterns from data. Supervised vs unsupervised learning.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Parameterized model (hypothesis): a function mapping inputs to outputs with learnable parameters
- -Empirical risk (training objective): a scalar loss computed on the dataset that training minimizes
- -Supervised vs unsupervised: presence versus absence of target labels in the data (determines the form of the learning objective)

## Key Symbols & Notation

f(x; theta) - parameterized model (inputs x, parameters theta)

## Essential Relationships

- -Learning = optimizing parameters theta of f(x; theta) to minimize empirical risk computed on the available data; whether the risk uses labels is determined by supervision

## Prerequisites (2)

[Maximum Likelihood Estimation6 atoms](/tech-tree/mle/)[Gradient Descent6 atoms](/tech-tree/gradient-descent/)

## Unlocks (6)

[Logistic Regressionlvl 3](/tech-tree/logistic-regression/)[Bias-Variance Tradeofflvl 4](/tech-tree/bias-variance/)[Loss Functionslvl 4](/tech-tree/loss-functions/)[Decision Treeslvl 4](/tech-tree/decision-trees/)[Linear Regressionlvl 3](/tech-tree/linear-regression/)[Clusteringlvl 4](/tech-tree/clustering/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[pipelineBusiness

The DATA → MODEL → OBJECTIVE pipeline is the canonical supervised learning workflow introduced here: input data, a learnable model, and a loss to optimize](/business/pipeline/)

Advanced Learning Details

### Graph Position

106

Depth Cost

26

Fan-Out (ROI)

11

Bottleneck Score

8

Chain Length

### Cognitive Load

5

Atomic Elements

50

Total Elements

L4

Percentile Level

L3

Atomic Level

### All Concepts (22)

- - Machine learning: algorithms/systems that learn patterns or mappings from data to make predictions or extract structure
- - Supervised learning: learning a mapping from inputs (features) to outputs (labels) using labeled examples
- - Unsupervised learning: discovering patterns or structure in data without labeled outputs
- - Feature (input variable): an individual measurable property or attribute of an example
- - Label / target (output variable): the value to be predicted in supervised learning
- - Training set: subset of data used to fit a model
- - Test set: subset of data held out to evaluate generalization
- - Validation set: subset of data used to tune hyperparameters or select models
- - Generalization: the model's ability to perform well on previously unseen data
- - Overfitting: when a model fits training data very well but performs poorly on new data
- - Underfitting: when a model is too simple to capture underlying patterns and performs poorly on both train and test data
- - Model capacity / complexity: the expressive power of a model family (how flexible it is at fitting patterns)
- - Bias-variance tradeoff: conceptual decomposition of error into bias (systematic error) and variance (sensitivity to training data)
- - Classification: supervised task predicting discrete class labels
- - Regression: supervised task predicting continuous values
- - Clustering: unsupervised task of grouping similar examples
- - Dimensionality reduction: unsupervised task of mapping high-dimensional inputs to a lower-dimensional representation while preserving structure
- - Density estimation (as an unsupervised task): estimating the probability distribution that generated the data
- - Evaluation metrics for supervised tasks (task-specific measures, e.g., accuracy, precision/recall, mean squared error)
- - Evaluation concepts for unsupervised tasks (intrinsic metrics like silhouette score or reconstruction error; extrinsic measures when labels exist)
- - Training vs. inference distinction: using data to learn model parameters (training) vs. using a learned model to make predictions (inference)
- - Hyperparameter: a configuration setting that controls model training or structure and is not learned by standard parameter estimation

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Machine learning is the idea that instead of hand-writing rules (“if the email contains ‘free money’, mark as spam”), we let a program *learn a pattern* from examples. The central move is surprisingly simple: pick a flexible function f(x; θ), define what it means to be wrong with a loss, and use data to find θ that makes the loss small.

TL;DR:

Machine learning = choosing a parameterized model f(x; θ) and fitting parameters θ by minimizing an empirical risk (average loss on a dataset). In supervised learning, data includes labels y so the loss measures prediction error; in unsupervised learning, there are no labels, so the objective captures structure (e.g., clustering, density). Training is optimization (often gradient descent), and generalization is the goal (performing well on new data).

## What Is Machine Learning Introduction?

### Why “learning” at all?

In many problems, writing explicit rules is either too hard or too brittle.

- •**Perception problems**: recognizing handwritten digits, detecting objects in images.
- •**Language problems**: classifying sentiment, translating text.
- •**Forecasting problems**: predicting demand, risk, or sensor readings.

Rules struggle because the mapping from inputs to outputs is complex and full of edge cases. Machine learning changes the workflow:

1. 1)Collect data that represents the problem.
2. 2)Choose a model family (a set of functions) that could plausibly represent the relationship.
3. 3)Define an objective that measures how well a model fits the data.
4. 4)Optimize the objective to find parameters.
5. 5)Evaluate on new (held-out) data to check **generalization**.

### The core abstraction: a parameterized model

A machine learning model is a **parameterized function**:

- •Inputs: typically **x** (often a vector of features)
- •Outputs: a prediction ŷ (could be a number, a class, a probability distribution, an embedding)
- •Parameters: θ (the “knobs” we tune)

We write this as:

f(x; θ)

Examples of what f might represent:

- •**Linear regression**: f(x; θ) = θᵀx
- •**Logistic regression**: f(x; θ) = σ(θᵀx) where σ is the sigmoid
- •**Neural network**: f(x; θ) = composition of affine maps and nonlinearities

The key is that f is *not* a single function until you choose θ. The learning problem is: **find θ from data**.

### Data as a dataset, not a single example

Typically we have n examples. In supervised learning we write:

D = { (xᵢ, yᵢ) }ᵢ₌₁ⁿ

- •xᵢ: input features (often **xᵢ** ∈ ℝᵈ)
- •yᵢ: target label/value (class label, real number, etc.)

In unsupervised learning we usually have only inputs:

D = { xᵢ }ᵢ₌₁ⁿ

### Learning as “fit on data” but “perform in the world”

A common confusion: if we minimize error on the training set, aren’t we done?

Not quite. We care about performance on *new* data from the same underlying process. So we distinguish:

- •**Training**: minimize objective on observed data.
- •**Generalization**: low error on unseen data.

A model can fit training data extremely well yet generalize poorly (overfitting). This lesson sets up the objects we need to discuss that later (e.g., in [Bias-Variance Tradeoff](/tech-tree/bias-variance/)).

### A unifying view

Machine learning problems often look different on the surface (regression vs classification vs clustering), but underneath they share a template:

1. 1)Choose f(x; θ)
2. 2)Choose an objective J(θ)
3. 3)Compute θ̂ = argmin\_θ J(θ)

The rest of the field is largely about better choices for f, better objectives, and better optimization/evaluation procedures.

## Core Mechanic 1: Parameterized Models f(x; θ)

### Why start with parameterized models?

We need a way to turn “patterns in data” into a concrete computational object. A parameterized model does exactly that: it defines a **space of candidate functions** indexed by θ.

Think of θ as coordinates in a “function space.” Each θ picks a specific function f(·; θ).

### Inputs as vectors, parameters as vectors

In many ML settings:

- •**x** ∈ ℝᵈ is a feature vector
- •θ ∈ ℝᵖ is a parameter vector

We often use boldface for vectors: **x**, **w**, **θ**.

A classic example is a linear score function:

s(x; **w**, b) = **w**ᵀ**x** + b

You can fold b into **w** by augmenting the input:

Let x′ = [x; 1] and w′ = [w; b]

Then:

s(x; **w**, b) = (w′)ᵀ x′

This “feature augmentation” is simple, but it’s a good reminder: the choice of representation can simplify everything.

### What does the model output mean?

Different tasks interpret f(x; θ) differently.

| Task type | Output f(x; θ) | Typical interpretation |
| --- | --- | --- |
| Regression | real number ŷ ∈ ℝ | predicted value |
| Binary classification | probability p ∈ [0, 1] | P(y = 1 | x) |
| Multi-class classification | vector **p** ∈ [0,1]ᵏ, ∑ pⱼ = 1 | class distribution |
| Representation learning | embedding **z** ∈ ℝᵐ | learned features |

The same “score” s(x; θ) might be post-processed:

- •Logistic regression: p = σ(s)
- •Softmax regression: pⱼ = exp(sⱼ) / ∑ₗ exp(sₗ)

### Model capacity (informal)

A parameterized model family can be:

- •**Too simple**: cannot represent the true relationship → underfitting.
- •**Very flexible**: can represent many patterns, including noise → risk of overfitting.

You don’t need a formal definition of capacity yet, but you should feel the tradeoff: richer f can fit more, but may generalize worse without regularization or enough data.

### A geometric intuition

For linear models, learning often becomes geometry.

- •**w** defines a direction.
- •**w**ᵀ**x** projects **x** onto **w**.
- •In classification, a hyperplane **w**ᵀ**x** + b = 0 separates space.

Even for non-linear models, optimization still adjusts θ to reshape decision boundaries or function curves.

### Model ≠ algorithm

A subtle but crucial distinction:

- •**Model**: f(x; θ)
- •**Training algorithm**: how you choose θ (e.g., gradient descent)

Different training algorithms can fit the *same* model family. And the same training algorithm can be used for different model families.

This separation is what makes ML modular.

## Core Mechanic 2: Empirical Risk (Training Objective)

### Why we need an objective

To “learn,” we need a quantitative notion of goodness. That means a scalar objective function we can minimize.

In supervised learning, the objective is usually based on a **loss function** ℓ(ŷ, y) that measures how bad a prediction is for one example.

Then we aggregate loss over the dataset.

### Per-example loss → dataset objective

Given D = { (xᵢ, yᵢ) }ᵢ₌₁ⁿ and predictions ŷᵢ = f(xᵢ; θ), define empirical risk:

R̂(θ) = (1/n) ∑ᵢ₌₁ⁿ ℓ(f(xᵢ; θ), yᵢ)

Training typically means:

θ̂ = argmin\_θ R̂(θ)

This is called **Empirical Risk Minimization (ERM)**.

### Why “empirical”?

Because it is computed on the *empirical sample* you observed, not on the full (unknown) data-generating distribution.

If the true distribution of (x, y) is P, then the population (true) risk is:

R(θ) = E₍x,y₎∼P[ ℓ(f(x; θ), y) ]

But we cannot compute R(θ) exactly because P is unknown. We approximate it with R̂(θ).

This is the bridge between data and generalization:

- •We minimize R̂(θ) because it’s available.
- •We hope R̂(θ) is close to R(θ).

### Connection to Maximum Likelihood Estimation (MLE)

You already know MLE. Many ML objectives are MLE in disguise.

Suppose your model defines a conditional distribution p(y | x; θ). The likelihood on data is:

L(θ) = ∏ᵢ₌₁ⁿ p(yᵢ | xᵢ; θ)

MLE chooses:

θ̂ = argmax\_θ ∏ᵢ p(yᵢ | xᵢ; θ)

It is more convenient to maximize log-likelihood:

log L(θ) = ∑ᵢ log p(yᵢ | xᵢ; θ)

Maximizing log-likelihood is equivalent to minimizing negative log-likelihood (NLL):

θ̂ = argmin\_θ −∑ᵢ log p(yᵢ | xᵢ; θ)

Now compare with ERM:

R̂(θ) = (1/n) ∑ᵢ ℓ(f(xᵢ; θ), yᵢ)

If we set:

ℓᵢ(θ) = −log p(yᵢ | xᵢ; θ)

then minimizing empirical risk equals MLE (up to the constant factor 1/n).

So one major story of ML is:

**Choose a probabilistic model p(y|x;θ) ⇒ derive a loss (NLL) ⇒ minimize it.**

### Regularization: adding a preference over θ

Often we train not just by fitting data, but also by discouraging overly complex parameter settings.

A common regularized objective is:

J(θ) = (1/n) ∑ᵢ ℓ(f(xᵢ; θ), yᵢ) + λ Ω(θ)

Where:

- •Ω(θ) might be ‖θ‖² (L2 regularization) or ‖θ‖₁ (L1)
- •λ ≥ 0 controls strength

From a probabilistic view, regularization often corresponds to a prior on θ (MAP estimation), but you don’t need that machinery to use it.

### Optimization: where gradient descent enters

Given J(θ), gradient descent performs updates:

θ ← θ − α ∇θ J(θ)

Because you already know gradient descent, the new idea here is mostly: **what is J?** ML is largely the craft of choosing J so that minimizing it produces useful behavior.

### Training, validation, test (briefly)

To estimate generalization, we split data:

- •training set: fit θ
- •validation set: choose hyperparameters (like λ)
- •test set: final evaluation

The key is to avoid letting the test set influence choices, otherwise your “estimate” of generalization becomes biased.

## Application/Connection: Supervised vs Unsupervised Learning

### Why this distinction matters

“Supervised vs unsupervised” is not just a label—it determines what objective you can write down.

- •If you have targets y, you can directly penalize prediction errors.
- •If you don’t, you must define a proxy objective that captures structure.

This changes evaluation, failure modes, and what “success” even means.

### Supervised learning

**Data**: D = { (xᵢ, yᵢ) }

**Goal**: learn a mapping x → y.

Typical objective (ERM):

R̂(θ) = (1/n) ∑ᵢ ℓ(f(xᵢ; θ), yᵢ)

Common tasks:

- •Regression (y ∈ ℝ): house prices, temperature prediction
- •Classification (y ∈ {1,…,K}): spam vs ham, disease vs no disease

Evaluation is comparatively straightforward:

- •Regression: MSE/MAE on a test set
- •Classification: accuracy, precision/recall, AUC

### Unsupervised learning

**Data**: D = { xᵢ }

**Goal**: discover structure in x.

Because there is no y, the objective can take different forms:

1. 1)**Clustering**: assign cluster IDs cᵢ to minimize within-cluster dispersion.

- •Example objective (k-means style):

min\_{μ₁,…,μ\_k, c₁,…,cₙ} ∑ᵢ ‖xᵢ − μ\_{cᵢ}‖²

2. 2)**Density estimation / generative modeling**: fit p(x; θ).

- •MLE objective:

θ̂ = argmax\_θ ∏ᵢ p(xᵢ; θ)

3. 3)**Dimensionality reduction**: find a low-dimensional representation z = g(x).

- •Objective might preserve variance (PCA) or reconstruction (autoencoders).

Evaluation is trickier because “ground truth” labels may not exist. You often evaluate indirectly:

- •downstream task performance (use learned representation for classification)
- •likelihood on held-out data (for density models)
- •qualitative inspection (clusters, embeddings)

### Semi-supervised and self-supervised (bridge concepts)

Many modern systems mix ideas:

- •**Semi-supervised**: small labeled set + large unlabeled set.
- •**Self-supervised**: create pseudo-labels from the data itself (e.g., predict masked tokens).

These still follow the same template: define f and define an objective J.

### A single table to anchor the big picture

| Learning setting | Data available | Typical objective | What success looks like |
| --- | --- | --- | --- |
| Supervised | (x, y) pairs | minimize prediction loss | low test error on y |
| Unsupervised | x only | clustering / likelihood / reconstruction | meaningful structure; useful representations |
| Semi-supervised | few (x, y) + many x | combined supervised + unsupervised | better than supervised-only with few labels |
| Self-supervised | x only (pseudo y) | predict withheld parts / contrast views | transferable representations |

### Connections to what you’ll learn next

This intro node enables specific, concrete models and deeper theory:

- •[Linear Regression](/tech-tree/linear-regression/): a supervised regression model, often using squared loss.
- •[Logistic Regression](/tech-tree/logistic-regression/): supervised classification with probabilistic interpretation and cross-entropy/NLL.
- •[Loss Functions](/tech-tree/loss-functions/): how choices of ℓ shape learning behavior.
- •[Decision Trees](/tech-tree/decision-trees/): a different model family with different inductive biases.
- •[Bias-Variance Tradeoff](/tech-tree/bias-variance/): why generalization is hard; underfitting vs overfitting.

The through-line: every one of these is still “choose f(x; θ), choose J(θ), optimize.”

## Worked Examples (3)

### From MLE to a supervised training loss (negative log-likelihood)

You have labeled data D = { (xᵢ, yᵢ) }ᵢ₌₁ⁿ. Your model specifies a conditional probability p(y | x; θ). Show how maximizing likelihood becomes minimizing an empirical risk with a per-example loss.

1. Start with the likelihood of the dataset (conditional independence assumption):

   L(θ) = ∏ᵢ₌₁ⁿ p(yᵢ | xᵢ; θ)
2. Take logs to make products into sums:

   log L(θ) = log(∏ᵢ p(yᵢ | xᵢ; θ))

   = ∑ᵢ log p(yᵢ | xᵢ; θ)
3. MLE chooses θ that maximizes log-likelihood:

   θ̂ = argmax\_θ ∑ᵢ log p(yᵢ | xᵢ; θ)
4. Convert to a minimization by multiplying by −1:

   θ̂ = argmin\_θ −∑ᵢ log p(yᵢ | xᵢ; θ)
5. Recognize this as a sum of per-example losses. Define:

   ℓᵢ(θ) = −log p(yᵢ | xᵢ; θ)

   Then the objective is:

   J(θ) = ∑ᵢ ℓᵢ(θ)
6. Optionally average over n (does not change the argmin):

   R̂(θ) = (1/n) ∑ᵢ₌₁ⁿ ℓᵢ(θ)

   This matches ERM with loss ℓ(f(xᵢ; θ), yᵢ) when f induces p(y|x;θ).

**Insight:** A large fraction of supervised ML is just MLE with a convenient parameterization. The “loss function” is often simply the negative log-likelihood of your probabilistic model.

### A tiny supervised ERM example with squared loss

Suppose f(x; θ) = θx (a 1D linear model with one parameter θ). Data: (x₁, y₁) = (1, 2), (x₂, y₂) = (2, 3). Use squared loss ℓ(ŷ, y) = (ŷ − y)². Write the empirical risk and find the minimizing θ by calculus.

1. Write predictions:

   ŷ₁ = f(1; θ) = θ

   ŷ₂ = f(2; θ) = 2θ
2. Write empirical risk (average squared loss):

   R̂(θ) = (1/2)[(θ − 2)² + (2θ − 3)²]
3. Expand the squares:

   (θ − 2)² = θ² − 4θ + 4

   (2θ − 3)² = 4θ² − 12θ + 9
4. Sum and scale:

   R̂(θ) = (1/2)[(θ² − 4θ + 4) + (4θ² − 12θ + 9)]

   = (1/2)[5θ² − 16θ + 13]

   = (5/2)θ² − 8θ + 13/2
5. Differentiate and set to zero:

   ∂R̂/∂θ = 5θ − 8

   Set 5θ − 8 = 0 ⇒ θ = 8/5 = 1.6
6. Check (optional) that it is a minimum:

   ∂²R̂/∂θ² = 5 > 0 ⇒ minimum.

**Insight:** Even this toy problem follows the full ML pattern: define f(x; θ), choose a loss, average it into R̂(θ), then optimize. In higher dimensions you typically use vector calculus and gradient descent rather than solving in closed form.

### Unsupervised objective example: k-means as empirical risk without labels

You have unlabeled points x₁,…,xₙ in ℝᵈ. You want to group them into k clusters. Write the k-means objective and interpret it as empirical risk minimization over latent assignments.

1. Introduce cluster centers μ₁,…,μ\_k where each μⱼ ∈ ℝᵈ.
2. Introduce an assignment cᵢ ∈ {1,…,k} for each data point xᵢ (a latent/hidden variable).
3. Define the distortion (squared distance) for a point to its assigned center:

   lossᵢ = ‖xᵢ − μ\_{cᵢ}‖²
4. Sum over the dataset to get an empirical objective:

   J(μ₁,…,μ\_k, c₁,…,cₙ) = ∑ᵢ₌₁ⁿ ‖xᵢ − μ\_{cᵢ}‖²
5. Interpretation:

   - •The “parameters” are the centers μⱼ.
   - •The “labels” cᵢ are not given; they are chosen to minimize J.
   - •The objective encourages points in the same cluster to be close to their center.
6. Training alternates (informally):

   - •Fix centers, choose assignments cᵢ to nearest μⱼ.
   - •Fix assignments, update each μⱼ to the mean of its assigned points.

   This decreases J each step.

**Insight:** Unsupervised learning still optimizes a scalar objective, but the objective is about structure (compact clusters) rather than matching given targets y. The absence of labels changes both the objective and how you validate results.

## Key Takeaways

- ✓

  Machine learning formalizes “learning from data” as choosing parameters θ of a model f(x; θ).
- ✓

  A parameterized model defines a whole family of functions; training selects one member of that family by optimizing θ.
- ✓

  Empirical risk R̂(θ) = (1/n) ∑ ℓ(f(xᵢ; θ), yᵢ) is the standard supervised training objective (ERM).
- ✓

  Population risk R(θ) = E[ℓ(f(x; θ), y)] is what we actually care about; R̂(θ) is a sample-based approximation.
- ✓

  Many common losses are negative log-likelihoods; minimizing them is equivalent to MLE (up to constants).
- ✓

  Regularization augments the objective with a term like λΩ(θ) to prefer simpler parameter settings and improve generalization.
- ✓

  Supervised learning uses labeled (x, y) data; unsupervised learning uses x only and must define objectives that capture structure (clustering, density, reconstruction).

## Common Mistakes

- ✗

  Confusing the model with the training algorithm: f(x; θ) is the model; gradient descent is just one way to find θ.
- ✗

  Thinking low training loss implies a good model: generalization depends on how well the learned θ performs on unseen data.
- ✗

  Mixing up objectives across settings: using supervised metrics (accuracy) when you don’t have labels, or assuming unsupervised structure guarantees downstream performance.
- ✗

  Treating “loss” and “metric” as the same thing: you might train with cross-entropy but report accuracy; they serve different roles.

## Practice

easy

You have supervised data D = { (xᵢ, yᵢ) }ᵢ₌₁ⁿ and a model f(x; θ). Write the empirical risk for absolute error loss ℓ(ŷ, y) = |ŷ − y|. Is the objective differentiable everywhere?

**Hint:** Write R̂(θ) = (1/n)∑|f(xᵢ;θ) − yᵢ|. Consider what happens when f(xᵢ;θ) = yᵢ.

Show solution

The empirical risk is:

R̂(θ) = (1/n) ∑ᵢ₌₁ⁿ |f(xᵢ; θ) − yᵢ|.

It is not differentiable at points where f(xᵢ; θ) − yᵢ = 0 for some i (the absolute value has a kink at 0). It is subdifferentiable there, and differentiable elsewhere.

medium

Show that minimizing the average loss (1/n)∑ᵢ ℓᵢ(θ) has the same minimizer as minimizing the sum ∑ᵢ ℓᵢ(θ).

**Hint:** Multiplying an objective by a positive constant does not change the argmin.

Show solution

Let J(θ) = ∑ᵢ₌₁ⁿ ℓᵢ(θ) and R̂(θ) = (1/n)J(θ).

For any θ₁, θ₂:

J(θ₁) ≤ J(θ₂) ⇔ (1/n)J(θ₁) ≤ (1/n)J(θ₂)

because 1/n > 0.

Therefore θ that minimizes J also minimizes R̂, so:

argmin\_θ J(θ) = argmin\_θ R̂(θ).

medium

Unsupervised vs supervised identification: For each dataset type below, say whether it is supervised or unsupervised and propose a plausible objective.

(A) 10,000 images each tagged with {cat, dog}

(B) 1,000,000 unlabeled user click sequences

(C) 50,000 house listings with final sale price

**Hint:** Look for whether y is present. If not, think clustering, likelihood, reconstruction, or contrastive objectives.

Show solution

(A) Supervised (classification). Objective: minimize cross-entropy / NLL for p(y|x;θ).

(B) Unsupervised (no labels). Objective examples: maximize likelihood of sequences p(x;θ), or self-supervised next-item prediction / masked prediction loss.

(C) Supervised (regression). Objective: minimize squared loss (ŷ − y)² (possibly with regularization).

## Connections

Next nodes you can study:

- •[Linear Regression](/tech-tree/linear-regression/) — a first supervised model where f(x; θ) is linear and the loss is often squared error.
- •[Logistic Regression](/tech-tree/logistic-regression/) — supervised classification with probabilistic interpretation and cross-entropy (NLL).
- •[Loss Functions](/tech-tree/loss-functions/) — how different choices of ℓ change robustness, calibration, and optimization.
- •[Bias-Variance Tradeoff](/tech-tree/bias-variance/) — why minimizing training loss is not enough; introduces generalization error.
- •[Decision Trees](/tech-tree/decision-trees/) — a different hypothesis class with piecewise-constant predictions and impurity-based objectives.

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
