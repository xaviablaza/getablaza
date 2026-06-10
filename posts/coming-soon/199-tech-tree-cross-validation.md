---
title: Cross-Validation
description: Evaluating models on held-out data. K-fold, leave-one-out.
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
permalink: /tech-tree/cross-validation/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Cross-Validation

Machine LearningDifficulty: ★★★★☆Depth: 10Unlocks: 0

Evaluating models on held-out data. K-fold, leave-one-out.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Held-out evaluation: reserve data not used for training to measure model performance on unseen examples
- -Folded resampling: partition dataset into k disjoint subsets and iteratively train on k-1 folds and validate on the remaining fold (k-fold; leave-one-out is k = N)
- -Aggregation estimator: combine per-fold validation losses (typically by averaging) to produce a single estimate of expected generalization error

## Key Symbols & Notation

k (number of folds)L(y, y\_hat) (loss function used to evaluate predictions)

## Essential Relationships

- -Cross-validation approximates expected test loss by averaging per-fold validation losses on held-out data
- -Leave-one-out cross-validation (LOOCV) is the special case of k-fold with k equal to the dataset size (N)

## Prerequisites (2)

[Bias-Variance Tradeoff6 atoms](/tech-tree/bias-variance/)[Maximum Likelihood Estimation6 atoms](/tech-tree/mle/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[backtestingBusiness

Cross-validation is the ML methodological equivalent of backtesting - evaluating a learned model on held-out historical data to verify it generalizes beyond the training set](/business/backtesting/)[Quality GatesBusiness

Cross-validation is the canonical cheap feedback mechanism that enables quality gates on ML models - without held-out evaluation, you cannot gate on generalization and cannot trust predictions](/business/quality-gates/)

Advanced Learning Details

### Graph Position

119

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

10

Chain Length

### Cognitive Load

7

Atomic Elements

33

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (13)

- - held-out data (data withheld from training to test model performance)
- - training set vs validation set vs test set (roles and differences)
- - cross-validation as a resampling-based evaluation procedure
- - k-fold cross-validation (partition data into k disjoint folds, train on k-1, validate on the remaining fold, repeat k times)
- - leave-one-out cross-validation (LOOCV) as the special case of k-fold with k = n)
- - fold (one of the k disjoint subsets created for k-fold CV)
- - out-of-sample (validation) error estimated by cross-validation
- - cross-validated loss / cross-validated risk (the aggregated loss computed across held-out folds)
- - aggregation of fold results (taking mean, and often variance/SD, across fold losses)
- - model selection via cross-validation (choosing hyperparameters or model variants based on CV performance)
- - data leakage / validation-set reuse risk (overfitting to the validation data when reusing folds for selection)
- - computational cost of CV (repeated training runs proportional to number of folds, expensive for LOOCV)
- - bias and variance properties of CV estimators (CV estimate itself has bias/variance that depends on k)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

If you only judge a model on the data it trained on, you’re mostly measuring how well it memorized. Cross-validation is the practical bridge between “fits the past” and “likely to work on new data.”

TL;DR:

Cross-validation (CV) estimates a model’s generalization error by repeatedly training on part of the dataset and evaluating on held-out folds. In k-fold CV, you split data into k disjoint folds, train k times on k−1 folds, validate on the remaining fold, then aggregate the per-fold losses (usually by averaging) to estimate expected test performance. Leave-one-out is k = N. CV is mainly used for model selection and hyperparameter tuning; a final untouched test set is still recommended for the final report.

## What Is Cross-Validation?

### Why we need it (motivation first)

In machine learning, the quantity we actually care about is **generalization**: how well a trained model predicts on new, unseen examples drawn from the same data-generating process. Formally, if (x, y) is a random example and your model predicts ŷ = f(x), then the ideal target is the **expected risk** (generalization error)

R(f) = 𝔼[L(y, f(x))]

where L(y, ŷ) is a loss function (0–1 loss for classification, squared loss for regression, log loss for probabilistic models, etc.).

But we do not have access to the true distribution of (x, y). We only have a finite dataset D = {(xᵢ, yᵢ)}ᵢ₌₁ᴺ, and we need a *procedure* to estimate R(f) using D.

A naive idea is to train on all of D and compute the training loss:

(1/N) ∑ᵢ L(yᵢ, f(xᵢ))

This almost always **underestimates** the true error, because the model has already “seen” those points during fitting. The more flexible the model (higher variance), the worse this optimism can be. That’s the core reason held-out evaluation exists.

### The core definition

**Cross-validation** is a family of resampling-based methods that estimate generalization error by:

1) splitting the dataset into **training** and **validation** parts multiple times,

2) training the model on the training part each time,

3) evaluating on the held-out validation part, and

4) aggregating these validation losses into a single estimate.

The most common form is **k-fold cross-validation**:

- •Partition the dataset indices {1, …, N} into k disjoint subsets (folds) F₁, …, F\_k.
- •For each fold j ∈ {1, …, k}:
- •Train a model on all data except Fⱼ.
- •Validate on Fⱼ.
- •Aggregate the k validation scores.

This gives an estimate of how the *training procedure* (algorithm + hyperparameters + preprocessing choices) performs on new data.

### “Held-out” means “not used for training”

The key rule is **no information leakage** from validation fold into training. In practice this means:

- •Fit preprocessing (scaling, imputation, feature selection, PCA, etc.) using *only* the training folds.
- •Then apply that fitted transform to the validation fold.

You can think of each fold as a tiny “future” dataset that the model hasn’t been allowed to learn from.

### Where CV sits in the bias–variance story

You already know the bias–variance tradeoff. Cross-validation is a tool to *measure* the net effect:

- •Complex models may have low training error but high validation error (overfitting / high variance).
- •Simple models may have high training and validation error (underfitting / high bias).

By comparing validation performance across model complexities or hyperparameters, CV helps you pick a good balance.

### What CV is and isn’t

CV is not (primarily) a way to “get more data.” The training sets in different folds overlap heavily. What CV *does* do is reduce dependence on a single arbitrary train/validation split by averaging performance across multiple splits.

A useful mental model:

- •A single holdout split gives one noisy estimate.
- •k-fold CV gives k correlated but different estimates and averages them, typically reducing variance of the estimate.

### Notation we’ll use

- •N: dataset size
- •k: number of folds
- •Fⱼ: the index set of fold j
- •D\_trainⱼ: all examples not in Fⱼ
- •D\_valⱼ: all examples in Fⱼ
- •f̂ⱼ: model trained on D\_trainⱼ
- •L(y, ŷ): loss

Per-fold validation loss (average over that fold):

ℓⱼ = (1/|Fⱼ|) ∑\_{i ∈ Fⱼ} L(yᵢ, f̂ⱼ(xᵢ))

Cross-validated estimate (simple average):

CV\_k = (1/k) ∑\_{j=1}^k ℓⱼ

If folds are unequal size, a common alternative is a **size-weighted** average:

CV\_k = (1/N) ∑\_{j=1}^k ∑\_{i ∈ Fⱼ} L(yᵢ, f̂ⱼ(xᵢ))

Both mean “average validation loss over all held-out predictions,” just aggregated slightly differently.

### Quick comparison of common evaluation strategies

| Strategy | Train sets | Val/Test sets | Main use | Pros | Cons |
| --- | --- | --- | --- | --- | --- |
| Training error | 1 | 0 | Debugging fit | Easy | Optimistic; not generalization |
| Single holdout | 1 | 1 | Quick estimate | Simple | High variance; split-dependent |
| k-fold CV | k | k | Model selection | Lower variance estimate | More compute; leakage pitfalls |
| Leave-one-out (LOOCV) | N | N | Small datasets | Uses nearly all data for training each time | Very high compute; can be high-variance |

The rest of this lesson focuses on k-fold CV and LOOCV, plus practical issues that matter in real ML pipelines.

## Core Mechanic 1: K-Fold Cross-Validation (Folded Resampling)

### Why k-fold works as a compromise

You want two conflicting things:

1) **Large training set** (to reduce bias of the trained model; many algorithms improve with more data).

2) **Independent evaluation** (to avoid optimistic bias in measured performance).

k-fold CV compromises by training on a fraction (k−1)/k of the data and validating on 1/k, repeated k times so every example gets to be held out once.

As k increases:

- •Training sets get larger (good for bias).
- •Validation sets get smaller (bad for evaluation noise per fold).
- •Total compute increases roughly linearly with k.

This creates a practical sweet spot, often k = 5 or k = 10.

### The algorithm, step-by-step

Given dataset D with N examples and a fixed learning procedure A (algorithm + hyperparameters + preprocessing):

1) **Partition indices into k folds**

Choose a partition {F₁, …, F\_k} such that:

- •Fₐ ∩ F\_b = ∅ for a ≠ b
- •∪ⱼ Fⱼ = {1, …, N}

Typically |Fⱼ| ≈ N/k.

2) **Loop over folds**

For each j = 1…k:

- •Training indices Tⱼ = {1, …, N} \ Fⱼ
- •Fit model f̂ⱼ = A(D[Tⱼ])
- •Compute validation loss on fold j:

ℓⱼ = (1/|Fⱼ|) ∑\_{i ∈ Fⱼ} L(yᵢ, f̂ⱼ(xᵢ))

3) **Aggregate**

Report CV\_k = (1/k) ∑ⱼ ℓⱼ (or a weighted average).

### What exactly is being estimated?

Cross-validation estimates the performance of the **training procedure** when trained on about (k−1)/k of the available data.

That distinction matters:

- •If you later retrain on *all* N points, the final model may perform slightly better than CV suggests (because it had more training data).
- •Still, CV is usually a good proxy for comparing choices (hyperparameters, model classes) because those comparisons tend to preserve ordering.

### K-fold vs repeated random splits

Another family of methods is repeated random subsampling (“Monte Carlo CV”): repeatedly sample a random train/validation split.

k-fold has a nice property: each sample is used exactly once for validation, which tends to be sample-efficient.

### Stratification (especially for classification)

If you have class imbalance, random folding can accidentally create folds with very different class proportions. This can make validation scores unstable or misleading.

**Stratified k-fold** chooses folds so that the class proportions in each fold approximate the overall distribution.

This is not just a convenience; it protects you from evaluating on an unrepresentative validation fold.

### Time series and grouped data: when standard k-fold is wrong

The “i.i.d. examples” assumption (independent and identically distributed) underlies the idea that any subset is a valid proxy for the future. But many datasets violate this:

1) **Time series / temporal drift**

If data is ordered in time, random folds leak future information into training.

Use a **forward-chaining** or blocked CV:

- •Train on past
- •Validate on future

2) **Grouped observations** (e.g., multiple rows per patient/user/device)

If the same person appears in both train and validation folds, leakage occurs through identity-specific patterns.

Use **group k-fold**:

- •All samples from the same group must appear in the same fold.

These variants preserve the core CV principle: validation must simulate the real deployment scenario.

### Choosing k: practical guidance

| k | Training fraction | Compute cost | Typical use | Notes |
| --- | --- | --- | --- | --- |
| 3 | 2/3 | low | quick sanity checks | higher bias in estimate |
| 5 | 80% | moderate | common default | good tradeoff |
| 10 | 90% | higher | common for small/medium N | lower bias, more compute |
| N (LOOCV) | (N−1)/N | very high | very small datasets | can be noisy, expensive |

A common, defensible approach in practice:

- •Start with k = 5 for iteration speed.
- •Move to k = 10 if you need more stable estimates and can afford compute.

### From losses to model selection

Suppose you have hyperparameter λ (like regularization strength). For each λ, you can compute:

CV\_k(λ) = (1/k) ∑\_{j=1}^k ℓⱼ(λ)

Then choose:

λ\* = argmin\_λ CV\_k(λ)

This is the central use of CV in ML: selecting among alternatives using held-out evaluation repeatedly.

### Reporting variability: mean and uncertainty

Per-fold losses {ℓⱼ} vary because each fold is a different sample of held-out points.

You’ll often see:

- •mean CV score: μ = (1/k) ∑ⱼ ℓⱼ
- •sample standard deviation:

s = √( (1/(k−1)) ∑\_{j=1}^k (ℓⱼ − μ)² )

A rough standard error estimate is s/√k. Be cautious: fold scores are not independent in a strict statistical sense (training sets overlap), but these summaries are still useful for sanity checks and comparisons.

### A note on vector notation in models

Many models learn parameter vectors **w** (and bias b). Even though cross-validation is model-agnostic, it’s helpful to remember that in each fold you learn a different parameter vector:

**ŵ**₁, **ŵ**₂, …, **ŵ**\_k

The variability across these learned parameters is one concrete manifestation of variance in the bias–variance tradeoff.

## Core Mechanic 2: LOOCV and Aggregation Estimators (How We Combine Fold Results)

### Leave-One-Out Cross-Validation (LOOCV)

LOOCV is k-fold CV with k = N:

- •Each fold contains exactly 1 example.
- •Each training set contains N−1 examples.

Per-fold loss is simply:

ℓᵢ = L(yᵢ, f̂\_{−i}(xᵢ))

where f̂\_{−i} means “trained on all data except point i.”

LOOCV estimate:

CV\_LOO = (1/N) ∑\_{i=1}^N L(yᵢ, f̂\_{−i}(xᵢ))

### Why LOOCV is tempting

- •Training sets are almost the full dataset, so the trained model is close to what you’d train on all data.
- •You use every point for validation exactly once.

### Why LOOCV can be a bad idea

1) **Compute cost**

You train N models. If N is 100,000 this is impossible for many algorithms.

2) **Potentially higher variance of the estimate**

Each validation fold is a single point. That makes each ℓᵢ extremely noisy.

The average can still be noisy in practice, especially with heavy-tailed losses.

3) **Highly correlated training sets**

LOOCV training sets differ by only one point. This can make the estimate behave oddly and makes standard error formulas less trustworthy.

For many modern ML tasks, 5- or 10-fold is preferred.

### Aggregation: turning k numbers into one estimate

After running CV, you have per-fold losses ℓ₁ … ℓ\_k. The aggregation step looks simple (“just average”), but there are subtleties:

#### 1) Averaging losses vs averaging metrics

- •For losses like squared error or log loss, averaging is straightforward.
- •For some metrics (like F1, AUC), you must decide whether to:
- •compute the metric per fold then average, or
- •collect all out-of-fold predictions and compute one global metric.

These can differ because metrics are non-linear.

A robust pattern:

- •For metrics that can be computed on pooled predictions (e.g., AUC), compute **out-of-fold predictions** for every point, then compute the metric once.
- •For metrics that decompose per example (e.g., log loss), fold-averaging and pooled averaging match when weighted properly.

#### 2) Weighted vs unweighted averaging

If folds have equal size, unweighted mean is fine.

If fold sizes differ, prefer a size-weighted mean:

CV\_k = (1/N) ∑\_{j=1}^k ∑\_{i ∈ Fⱼ} L(yᵢ, f̂ⱼ(xᵢ))

This ensures each example contributes equally, not each fold.

#### 3) Choosing the loss L(y, ŷ)

The loss should match what you care about.

- •Regression: L = (y − ŷ)², |y − ŷ|, Huber
- •Classification: log loss, hinge loss, 0–1 loss

Important: if you use probabilistic models (like logistic regression), log loss evaluates probability calibration, not just accuracy.

### Cross-validation as an estimator (and what it estimates)

Let A be the learning algorithm (including your preprocessing and hyperparameter settings). When you run k-fold CV, you produce an estimator of risk:

R̂\_CV = CV\_k

This estimator has:

- •**Bias**: because training sets are smaller than N.
- •**Variance**: because folds differ.

As k increases:

- •Bias tends to decrease (training sets closer to full N).
- •Variance can increase or decrease depending on the setting, but small validation folds often increase noise.

This is one reason k = 5 or 10 is popular: it tends to deliver stable comparisons without extreme compute.

### Cross-validation for comparing models: paired structure

A key benefit of CV is that comparisons are often **paired**: you evaluate multiple models on the *same folds*.

Suppose model A and model B yield fold losses {ℓⱼᴬ} and {ℓⱼᴮ}. Consider differences dⱼ = ℓⱼᴬ − ℓⱼᴮ. Then:

d̄ = (1/k) ∑\_{j=1}^k dⱼ

If d̄ < 0, A is better on average. Because each dⱼ compares A vs B on the same validation fold, some sources of noise cancel out.

### Nested cross-validation (conceptual preview)

When you tune hyperparameters using CV, you are “using the validation data to choose.” This can lead to an optimistic bias if you then report the same CV score as final performance.

Nested CV addresses this by adding an outer CV loop for evaluation and an inner CV loop for tuning.

We’ll revisit this in the application section, but keep the principle in mind:

- •**CV for selection** is not automatically **CV for unbiased performance reporting**.

### A helpful way to think about CV outputs

Cross-validation produces two useful artifacts:

1) A scalar estimate (mean validation loss).

2) A set of **out-of-fold predictions** (each point predicted by a model that did not train on it).

Those out-of-fold predictions are extremely valuable for:

- •stacking/ensembling
- •error analysis without leakage
- •calibration checks

Even though the node focus is evaluation, this dual viewpoint helps you use CV effectively.

## Application/Connection: Using Cross-Validation in Real ML Workflows

### The standard workflow: train/validation/test with CV

In many projects you want:

- •a way to select hyperparameters (needs validation)
- •a way to report final performance (needs a final untouched test set)

A common workflow:

1) Split data into **train+validation** and **test** (test untouched).

2) On train+validation, run k-fold CV to choose hyperparameters.

3) Retrain the chosen model on all train+validation.

4) Evaluate once on test.

This keeps the test set as an honest proxy for future data.

### When nested CV matters

If you do not have enough data to comfortably hold out a test set, you might use **nested CV**.

Outer loop (evaluation):

- •Split into k\_outer folds.
- •For each outer fold:
- •treat that fold as outer validation/test
- •tune hyperparameters using inner CV on the remaining data
- •train best model on outer-train
- •evaluate on outer-holdout

Then aggregate outer-fold scores.

Why before how:

- •Hyperparameter tuning is a form of learning from validation data.
- •If you tune and evaluate on the same folds, you can overfit the validation procedure.
- •Nested CV reduces that optimism.

### CV and maximum likelihood (connection to prerequisites)

You know MLE: choose parameters θ to maximize likelihood on training data.

θ̂ = argmax\_θ ∑ᵢ log p(yᵢ | xᵢ, θ)

This is “fit.” Cross-validation answers a different question:

- •If we fit θ̂ on one subset, how good is p(y | x, θ̂) on a held-out subset?

In probabilistic models, a natural CV loss is negative log-likelihood:

L(y, ŷ) = −log p(y | x, θ̂)

Then CV estimates the expected out-of-sample negative log-likelihood, aligning evaluation with MLE’s objective.

### Preprocessing and leakage: the pipeline rule

Many evaluation bugs come from doing preprocessing on the full dataset before CV.

Example: standardization

- •Wrong: compute global mean μ and std σ on all N points, then run CV.
- •Right: for each fold j:
- •compute μⱼ, σⱼ on training folds only
- •transform training and validation using μⱼ, σⱼ

Why it matters:

- •Even “unsupervised” transforms can leak information about the validation distribution into training.
- •Leakage can make performance look better than it will be in production.

Practical solution: use an explicit pipeline object (conceptually):

transform = FitTransform(D\_trainⱼ)

model = FitModel(transform(D\_trainⱼ))

validate on transform(D\_valⱼ)

### CV for model comparison and selection criteria

Cross-validation is often used to compare:

- •linear vs non-linear models
- •different regularization strengths
- •feature sets
- •training objectives

But you must align the metric with the decision.

| Goal | Recommended metric | Why |
| --- | --- | --- |
| Pure classification correctness | accuracy (with care) | simple but can mislead under imbalance |
| Imbalanced classification | balanced accuracy, AUROC, AUPRC | reflects ranking and minority class |
| Probabilistic predictions | log loss, Brier score | measures calibration and sharpness |
| Regression robustness | MAE or Huber | less sensitive to outliers |

### Cross-validation in small data vs big data regimes

- •Small data: CV is extremely valuable; single holdout is too noisy.
- •Big data: you might use a single validation set because estimates stabilize with large N, and compute is the bottleneck.

Still, even in big data, CV can be useful for:

- •comparing close contenders
- •diagnosing variance
- •robustly evaluating across slices (e.g., geographic regions)

### Practical heuristics that prevent wasted effort

1) **Use the same folds across experiments**

This creates paired comparisons and reduces noise.

2) **Track fold-by-fold results**

A mean score can hide instability. If one fold collapses, investigate why (distribution shift, leakage, rare class missing).

3) **Do not over-tune**

If you try hundreds of hyperparameter configurations, you can overfit the CV estimate itself. Consider:

- •nested CV
- •a final holdout test
- •limiting search space or using Bayesian optimization with care

### Interpreting CV outcomes

Suppose model A has mean CV error 0.120 and model B has 0.118. Is B better?

You should look at:

- •magnitude of difference vs variability across folds
- •whether the improvement is consistent (most folds better) or driven by one fold
- •whether the metric matches your product goal

CV gives evidence, not certainty.

### Where this node connects next

Cross-validation is foundational for:

- •hyperparameter optimization
- •regularization selection
- •ensembling (stacking uses out-of-fold predictions)
- •model evaluation best practices (nested CV, leakage prevention)

You now have the machinery to evaluate models on held-out data in a principled, repeatable way—and to avoid the most common traps.

## Worked Examples (3)

### Example 1: Compute a k-fold CV estimate from per-fold losses (and weighted vs unweighted)

You ran 5-fold CV for a regression model using squared loss L(y, ŷ) = (y − ŷ)². Fold sizes are not exactly equal. You obtained:

- •Fold 1: |F₁| = 20, mean loss ℓ₁ = 1.20
- •Fold 2: |F₂| = 20, mean loss ℓ₂ = 0.95
- •Fold 3: |F₃| = 20, mean loss ℓ₃ = 1.05
- •Fold 4: |F₄| = 20, mean loss ℓ₄ = 1.10
- •Fold 5: |F₅| = 10, mean loss ℓ₅ = 1.60

Compute (a) unweighted CV mean, (b) size-weighted CV mean.

1. Unweighted mean:

   CV\_5 = (1/5) ∑\_{j=1}^5 ℓⱼ

   = (1/5)(1.20 + 0.95 + 1.05 + 1.10 + 1.60)

   = (1/5)(5.90)

   = 1.18
2. Compute total N:

   N = 20 + 20 + 20 + 20 + 10 = 90
3. Weighted mean (each example equal weight):

   CV\_5 = (1/N) ∑\_{j=1}^5 |Fⱼ| ℓⱼ

   = (1/90)(20·1.20 + 20·0.95 + 20·1.05 + 20·1.10 + 10·1.60)

   = (1/90)(24.0 + 19.0 + 21.0 + 22.0 + 16.0)

   = (1/90)(102.0)

   ≈ 1.1333

**Insight:** The unweighted mean treats each fold equally, so the small but high-loss fold (Fold 5) has disproportionate influence. The weighted mean reflects the average loss over all 90 held-out predictions, which is usually what you want if fold sizes differ.

### Example 2: LOOCV on a tiny dataset (conceptual calculation)

You have N = 4 labeled examples and a learning procedure A. Using LOOCV (k = N), you train 4 times, each time leaving one point out. Suppose the loss values on the left-out points are:

ℓ₁ = 0.2, ℓ₂ = 0.9, ℓ₃ = 0.4, ℓ₄ = 0.5.

Compute CV\_LOO and compare to 2-fold CV if the two fold losses were 0.35 and 0.80.

1. LOOCV estimate:

   CV\_LOO = (1/N) ∑\_{i=1}^N ℓᵢ

   = (1/4)(0.2 + 0.9 + 0.4 + 0.5)

   = (1/4)(2.0)

   = 0.50
2. 2-fold CV estimate:

   CV\_2 = (1/2)(0.35 + 0.80)

   = (1/2)(1.15)

   = 0.575
3. Interpretation:

   - •LOOCV trains on 3 points each time (larger training sets) and validates on 1 point (very noisy per fold).
   - •2-fold trains on 2 points each time (smaller training sets) and validates on 2 points (less noisy per fold).

**Insight:** Even on tiny N, different k values change the balance between training-set size and validation-set size. LOOCV is not automatically “best”; it can be noisy and expensive, even though it uses nearly all data for training each run.

### Example 3: Hyperparameter selection with k-fold CV (regularization strength)

You are tuning a regularization hyperparameter λ for a model. You run 5-fold CV and obtain mean validation losses:

- •λ = 0.01 → CV\_5(λ) = 0.84
- •λ = 0.1 → CV\_5(λ) = 0.79
- •λ = 1.0 → CV\_5(λ) = 0.81

Choose λ\* and explain what CV is estimating.

1. Select the minimizer:

   λ\* = argmin\_λ CV\_5(λ)

   Compare values: 0.84, 0.79, 0.81

   Minimum is 0.79 at λ = 0.1

   So λ\* = 0.1
2. What this means:

   For each λ, you trained 5 models (one per fold) and measured held-out loss.

   CV\_5(λ) estimates expected validation loss when training on about (k−1)/k = 4/5 of the data using λ.
3. Next step in a standard workflow:

   Retrain one final model on all available training data using λ\* = 0.1.

   Then evaluate once on a separate test set if you have one.

**Insight:** Cross-validation is most powerful as a *comparison tool*: it tells you which λ tends to generalize better under repeated held-out evaluation, not just which λ fits the training data best.

## Key Takeaways

- ✓

  Cross-validation estimates generalization error by repeatedly evaluating on held-out data; training loss alone is optimistically biased.
- ✓

  In k-fold CV, you partition the dataset into k disjoint folds, train on k−1 folds, validate on the remaining fold, and aggregate per-fold losses (often by averaging).
- ✓

  Per-fold validation loss can be written as ℓⱼ = (1/|Fⱼ|) ∑\_{i ∈ Fⱼ} L(yᵢ, f̂ⱼ(xᵢ)); the CV estimate is CV\_k = (1/k) ∑ⱼ ℓⱼ (or a size-weighted average).
- ✓

  Leave-one-out (k = N) uses nearly all data for training each run but is computationally expensive and can yield noisy estimates due to single-point validation folds.
- ✓

  Stratified folds (classification), group-aware folds (users/patients), and time-aware splits (time series) are essential to avoid misleading leakage and unrealistic evaluation.
- ✓

  All preprocessing must be fit using only training folds within each CV iteration; otherwise you leak information from validation into training.
- ✓

  CV is primarily for model selection and hyperparameter tuning; a final untouched test set (or nested CV) is recommended for unbiased performance reporting.
- ✓

  Using the same folds across candidate models creates paired comparisons that reduce noise in model selection.

## Common Mistakes

- ✗

  Data leakage: fitting scalers, imputers, feature selection, or PCA on the full dataset before cross-validation, then validating on transformed folds.
- ✗

  Using random k-fold on time series or grouped data, causing “future” information or group identity to appear in both train and validation.
- ✗

  Treating the best cross-validated score after extensive hyperparameter search as an unbiased estimate of final performance (selection-induced optimism).
- ✗

  Averaging non-linear metrics incorrectly (e.g., foldwise F1 vs global F1) or ignoring fold-size weighting when folds are uneven.

## Practice

easy

You run 10-fold CV (equal fold sizes) and get fold losses: 0.40, 0.42, 0.41, 0.39, 0.45, 0.38, 0.43, 0.40, 0.41, 0.39. Compute the mean CV loss and the sample standard deviation s.

**Hint:** Compute μ = (1/10) ∑ℓⱼ, then s = √( (1/(k−1)) ∑(ℓⱼ − μ)² ).

Show solution

Sum = 0.40+0.42+0.41+0.39+0.45+0.38+0.43+0.40+0.41+0.39 = 4.08

Mean μ = 4.08/10 = 0.408

Deviations (ℓⱼ−μ):

-0.008, 0.012, 0.002, -0.018, 0.042, -0.028, 0.022, -0.008, 0.002, -0.018

Squares:

0.000064, 0.000144, 0.000004, 0.000324, 0.001764, 0.000784, 0.000484, 0.000064, 0.000004, 0.000324

Sum squares = 0.00396

s = √(0.00396/9) = √(0.00044) ≈ 0.0210

medium

You have a dataset with 1,000 samples from 100 users (10 samples per user). Explain why standard k-fold CV can be misleading, and describe a correct folding strategy.

**Hint:** What happens if samples from the same user appear in both train and validation?

Show solution

Standard k-fold can place samples from the same user into both training and validation folds. The model can exploit user-specific patterns, making validation performance overly optimistic because the validation examples are not truly “unseen users.” A correct strategy is group k-fold CV: assign folds at the user level so that all samples from any given user belong to exactly one fold. Then each validation fold evaluates generalization to new users (or at least held-out users), matching the intended deployment scenario.

hard

You try 200 hyperparameter configurations and pick the one with the best 5-fold CV score, then report that score as your final performance. What bias can this introduce, and how can you fix it?

**Hint:** Model selection uses information from validation folds.

Show solution

Selecting the best configuration among many uses the validation folds for selection, which can overfit the CV estimate itself (selection-induced optimism). The reported best CV score tends to be biased downward (too good). Fixes include: (1) keep a final untouched test set and evaluate only once after selection; or (2) use nested cross-validation, where an outer CV loop evaluates performance and an inner CV loop performs hyperparameter tuning within each outer training split.

## Connections

Prerequisites and neighbors:

- •[Bias-Variance Tradeoff](/tech-tree/bias-variance-tradeoff/)
- •[Maximum Likelihood Estimation](/tech-tree/maximum-likelihood-estimation/)

Next useful nodes (common unlocks after CV):

- •[Hyperparameter Optimization](/tech-tree/hyperparameter-optimization/)
- •[Regularization](/tech-tree/regularization/)
- •[Model Evaluation Metrics](/tech-tree/model-evaluation-metrics/)
- •[Data Leakage and Proper ML Pipelines](/tech-tree/data-leakage/)
- •[Ensembling and Stacking](/tech-tree/stacking/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
