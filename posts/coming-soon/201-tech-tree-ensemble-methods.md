---
title: Ensemble Methods
description: Combining multiple models. Bagging, boosting, random forests.
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
inspiration_url: https://templeton.host/tech-tree/ensemble-methods/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/ensemble-methods/](https://templeton.host/tech-tree/ensemble-methods/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Ensemble Methods

Machine LearningDifficulty: ★★★★☆Depth: 10Unlocks: 0

Combining multiple models. Bagging, boosting, random forests.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Ensemble aggregation: combine multiple base learners into a single prediction via voting or averaging
- -Bagging (bootstrap aggregation): train base learners on bootstrap-resampled datasets in parallel to produce diversity and reduce variance by averaging
- -Boosting: sequentially train base learners where each focuses on previous errors and combine them as a weighted sum to reduce bias

## Key Symbols & Notation

H(x) - ensemble predictionh\_i(x) - prediction from the i-th base learner

## Essential Relationships

- -Ensemble as weighted aggregation: H(x) = sum\_i w\_i \* h\_i(x) (special cases: equal weights = averaging; discrete labels -> majority vote)

## Prerequisites (2)

[Decision Trees6 atoms](/tech-tree/decision-trees/)[Bias-Variance Tradeoff6 atoms](/tech-tree/bias-variance/)

Advanced Learning Details

### Graph Position

129

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

10

Chain Length

### Cognitive Load

6

Atomic Elements

60

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (25)

- - Ensemble: a model that combines multiple base learners to produce a single prediction
- - Base learner (base estimator / weak learner): a single model instance used within an ensemble
- - Aggregation rules: methods for combining base-learner outputs (majority voting, averaging, weighted voting/probability averaging)
- - Bagging (bootstrap aggregating): training multiple base learners on bootstrap samples and aggregating their predictions
- - Bootstrap sample: a training set sampled with replacement from the original dataset
- - Out-of-bag (OOB) estimation: using observations not included in a given bootstrap sample to estimate generalization error
- - Random forest: ensemble of decision trees that uses bagging plus random feature selection at split time
- - Feature bagging / random feature selection (mtry): selecting a random subset of features for each tree node (or tree) to decorrelate trees
- - Boosting: sequentially building base learners where each new learner focuses on correcting errors of the ensemble so far
- - Weak learner concept in boosting: a learner that is only slightly better than random but can be combined to form a strong learner
- - Stage-wise additive modeling: building the final model as a sum (additive combination) of successive base learners
- - AdaBoost-specific weighting: reweighting training examples based on previous learners' errors (increasing weight on misclassified examples)
- - Gradient boosting: fitting each new base learner to (an estimate of) the negative gradient of the loss function (residuals) - i.e., stage-wise gradient descent in function space
- - Learning rate / shrinkage: a multiplier (step size) applied to each new base learner's contribution to control learning speed and regularize boosting
- - Subsampled/stochastic gradient boosting: combining row subsampling with gradient boosting for regularization
- - Number of estimators / trees: a hyperparameter controlling how many base learners are combined
- - Tree complexity as base-learner capacity in ensembles: using shallow trees (stumps) or deeper trees as base learners with different bias/variance implications
- - Ensemble diversity: the idea that base learners should make different errors (be uncorrelated) to improve ensemble performance
- - Ensemble weighting: assigning different weights to base learners rather than equal averaging
- - OOB-based variable importance (and other feature-importance measures in forests): measuring a feature's contribution by permuting it or observing OOB error increases
- - Permutation importance: estimating feature importance by measuring performance change when a feature's values are permuted
- - Bootstrap sampling property (~63.2% inclusion): the expected fraction of unique training examples in a bootstrap sample is about 1 - e^{-1} ≈ 0.632
- - Bias vs variance effects specific to ensembles: bagging primarily reduces variance, boosting primarily reduces bias (but may affect variance)
- - Correlation among base learners: a determinant of how much averaging reduces variance
- - Early stopping for boosting: stopping adding learners based on validation/OOB error to prevent overfitting

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

A single decision tree can be brilliant—and also wildly unstable. Ensemble methods tame that instability (and sometimes push accuracy beyond what any single model can reach) by combining many “weak” or “noisy” models into one strong predictor.

TL;DR:

Ensemble methods build a final predictor H(x) by combining base learners hᵢ(x). Bagging trains many models in parallel on bootstrap-resampled data and averages/votes to reduce variance (e.g., random forests). Boosting trains models sequentially, each focusing on previous mistakes, and combines them as a weighted sum to reduce bias (e.g., AdaBoost, Gradient Boosting).

## What Is an Ensemble Method?

### Why ensembles exist (motivation)

Many ML models have a frustrating property: **small changes in the training data can cause large changes in the learned model**. Decision trees are a classic example—if you perturb the dataset slightly, the splits can change, leading to very different trees.

Ensemble methods are a systematic way to convert:

- •**instability → stability**
- •**high variance → lower variance** (often)
- •**weak learners → strong learner** (often)

The core idea is surprisingly simple: instead of trusting one model, train multiple base learners and **aggregate** their predictions.

### Definition

An **ensemble method** constructs a predictor:

- •**Base learners**: h₁(x), h₂(x), …, h\_M(x)
- •**Ensemble**: H(x)

and defines H(x) as an aggregation of the hᵢ(x).

Typical forms:

- •**Regression (averaging):**
- •H(x) = (1/M) ∑ᵢ hᵢ(x)
- •**Classification (majority vote):**
- •H(x) = mode{h₁(x), …, h\_M(x)}
- •**Weighted versions:**
- •H(x) = ∑ᵢ αᵢ hᵢ(x)

### Intuition: “wisdom of the crowd” needs diversity

If every base learner makes the **same** mistakes, the ensemble gains nothing.

Ensembles work when base learners are:

1. 1)**Individually better than random** (even slightly)
2. 2)**Diverse** (errors not perfectly correlated)

A helpful mental model: if each model has some error “noise,” averaging cancels noise—**but only if those noises aren’t identical**.

### A variance-reduction sketch (why averaging helps)

Suppose we do regression and each model predicts:

hᵢ(x) = f(x) + εᵢ

where f(x) is the true target function (or the expected prediction) and εᵢ is a zero-mean error term.

The ensemble average is:

H(x) = (1/M) ∑ᵢ hᵢ(x)

= (1/M) ∑ᵢ (f(x) + εᵢ)

= f(x) + (1/M) ∑ᵢ εᵢ

So the ensemble error is (1/M) ∑ᵢ εᵢ.

If the εᵢ are independent with Var(εᵢ) = σ², then:

Var(H(x) − f(x))

= Var((1/M) ∑ᵢ εᵢ)

= (1/M²) ∑ᵢ Var(εᵢ)

= (1/M²) · M · σ²

= σ² / M

That 1/M is the dream scenario.

If errors are correlated, you don’t get the full 1/M; this is why **creating diversity** is a central design goal.

### Two big families

Ensemble methods mainly fall into two camps:

| Family | Training style | Main goal | Common examples |
| --- | --- | --- | --- |
| Bagging | Parallel (independent) | Reduce variance | Bagging, Random Forests |
| Boosting | Sequential (dependent) | Reduce bias (and sometimes variance) | AdaBoost, Gradient Boosting, XGBoost-style methods |

This lesson focuses on: aggregation, bagging, random forests, and boosting—what they optimize, why they work, and how to reason about their behavior using the bias–variance lens.

## Core Mechanic 1: Ensemble Aggregation (Voting, Averaging, Weighting)

### Why talk about aggregation separately?

Training many models is only half the story. The other half is: **how do we combine them so the result is better than each one?**

Aggregation defines how information flows from base learners hᵢ(x) to the final ensemble H(x). Different choices correspond to different assumptions about:

- •whether predictions are comparable,
- •whether models are equally trustworthy,
- •whether models specialize in different regions.

### Common aggregation rules

#### 1) Regression: simple averaging

If hᵢ(x) outputs a real number (e.g., house price), the default aggregation is:

H(x) = (1/M) ∑ᵢ hᵢ(x)

Why this makes sense:

- •It preserves the scale of the target.
- •It reduces variance when base learners’ errors aren’t perfectly correlated.

#### 2) Classification: majority voting

If each hᵢ(x) outputs a class label in {0,1} (or {1,…,K}), a typical ensemble is:

H(x) = mode{h₁(x), …, h\_M(x)}

Why this can help:

- •A single overfit tree may misclassify a point, but if most other trees classify it correctly, the vote corrects it.

#### 3) Probability averaging (soft voting)

Often, classifiers output estimated probabilities pᵢ(y=k | x). Then you can average probabilities and choose argmax:

p̄(y=k | x) = (1/M) ∑ᵢ pᵢ(y=k | x)

H(x) = argmaxₖ p̄(y=k | x)

Soft voting tends to be more stable than hard voting because it uses confidence information.

#### 4) Weighted combinations

Sometimes models shouldn’t be equal. Boosting is the archetype:

H(x) = sign(∑ᵢ αᵢ hᵢ(x)) (binary classification with hᵢ(x) ∈ {−1, +1})

or for regression:

H(x) = ∑ᵢ αᵢ hᵢ(x)

Here αᵢ is learned from performance (later models may get different weights).

### Diversity: the hidden requirement

Aggregation works best when base learners disagree in useful ways.

How do we create diversity?

- •Different training subsets (bagging)
- •Different feature subsets (random forests)
- •Different training emphasis (boosting reweights data)
- •Different model types (stacking / heterogeneous ensembles—beyond this node)

A key point: **diversity that increases error is not helpful**. We want “decorrelated” errors while keeping each hᵢ(x) reasonably accurate.

### Bias–variance lens for aggregation

You already know the bias–variance tradeoff. Aggregation changes that balance:

- •Averaging many high-variance models tends to **reduce variance**.
- •Combining many weak models sequentially can **reduce bias** by expanding the function class.

A simplified but useful heuristic:

- •**Bagging → variance ↓**
- •**Boosting → bias ↓ (often) and variance can ↑ if overfit**

### A small derivation: averaging with correlated errors

Assume M models, each with error εᵢ, Var(εᵢ)=σ², and pairwise Corr(εᵢ, εⱼ)=ρ for i≠j.

Let H be the average. Then:

Var(H − f)

= Var((1/M) ∑ᵢ εᵢ)

= (1/M²) Var(∑ᵢ εᵢ)

Now expand Var of a sum:

Var(∑ᵢ εᵢ)

= ∑ᵢ Var(εᵢ) + 2∑\_{i<j} Cov(εᵢ, εⱼ)

= Mσ² + 2 · (M(M−1)/2) · (ρσ²)

= Mσ² + M(M−1)ρσ²

So:

Var(H − f)

= (1/M²)[Mσ² + M(M−1)ρσ²]

= (σ²/M) + ( (M−1)/M ) ρσ²

As M → ∞, this approaches ρσ².

Interpretation:

- •If ρ = 0 (independent errors), variance → 0 as M grows.
- •If ρ > 0, there is a floor: you can’t average below the shared correlated component.

This is why random forests deliberately reduce correlation (via feature subsampling), not just train many trees.

## Core Mechanic 2: Bagging (Bootstrap Aggregation) and Random Forests

### Why bagging works

Decision trees are typically:

- •**low bias** (they can fit complex patterns)
- •**high variance** (they change a lot with data perturbations)

Bagging targets that exact profile.

The plan:

1. 1)Create many slightly different datasets via **bootstrap resampling**.
2. 2)Train the same learner on each dataset (often an unpruned tree).
3. 3)Aggregate predictions (vote/average).

You get a “committee” of trees that individually overfit in different ways, and the vote cancels much of that overfitting.

### Bootstrap resampling (the source of diversity)

Given training set D of size N, a bootstrap sample Dᵢ is created by sampling N points **with replacement** from D.

Key facts:

- •Some points appear multiple times.
- •Some points don’t appear at all.

A useful calculation: expected fraction of unique points in a bootstrap sample.

Probability a specific point is not selected in one draw: 1 − 1/N.

Not selected in N draws:

(1 − 1/N)ᴺ ≈ e^{−1} ≈ 0.368

So expected fraction **left out** is ≈ 36.8%, and included is ≈ 63.2%.

Those “left out” points are the **out-of-bag** (OOB) set for that tree.

### Bagging algorithm (conceptual)

For m = 1..M:

- •D\_m ← bootstrap(D)
- •train base model h\_m on D\_m

Return ensemble H(x) = average/vote of h\_m(x)

### Out-of-bag evaluation (a free validation signal)

Because each training point is excluded from about 36.8% of bootstrap samples, you can estimate generalization error without a separate validation set:

- •For each point (xⱼ, yⱼ), collect predictions from trees where xⱼ was OOB.
- •Aggregate those predictions and compare to yⱼ.

This yields an OOB error estimate that is often close to cross-validation for bagged trees.

### Random forests: bagging + feature randomness

Bagging alone reduces variance, but trees can still be correlated because strong predictors dominate splits.

Random forests add a second diversity lever:

- •At each split, consider only a random subset of features.

If there are d features total, you choose m\_try features per split:

- •Classification default: m\_try ≈ √d
- •Regression default: m\_try ≈ d/3

**Why it helps:**

- •Different trees choose different top-level splits.
- •This reduces correlation ρ between tree errors.
- •Lower ρ pushes ensemble variance down (see correlated variance formula earlier).

### Random forest prediction

- •Regression: H(x) = (1/M) ∑ᵢ hᵢ(x)
- •Classification: majority vote or probability averaging

### Interpreting random forests via bias–variance

- •Individual tree: low bias, high variance
- •Bagging/forest: slightly higher bias (sometimes) but much lower variance

Often the net result is **better test performance**.

### Practical hyperparameters (what they do)

| Parameter | Effect on bias | Effect on variance | Notes |
| --- | --- | --- | --- |
| # trees M | ~ no change | ↓ (until plateau) | More trees rarely overfit; cost is compute |
| max depth / min leaf | ↑ when constrained | ↓ | Deep trees benefit from bagging; forests often use deep trees |
| m\_try | can ↑ if too small | ↓ by reducing correlation | Too small may underuse signal |
| bootstrap on/off | small | diversity changes | Some variants use subsampling without replacement |

### Feature importance (connection, but be cautious)

Random forests often report feature importance:

- •Mean decrease in impurity (fast, but biased toward high-cardinality features)
- •Permutation importance (more reliable, but more expensive)

This is a great tool, but not a proof of causality.

### When bagging/forests shine

- •Tabular data with non-linear interactions
- •Mixed feature types
- •Minimal preprocessing
- •Need strong baseline quickly

### When they struggle

- •Extrapolation outside training range (trees are piecewise constant)
- •Very high-dimensional sparse linear problems (linear models may dominate)
- •Tasks requiring smooth function approximation unless many trees

## Core Mechanic 3: Boosting (Sequential Ensembles That Fix Mistakes)

### Why boosting exists (a different failure mode)

Bagging is great when your base learner is already powerful but unstable.

What if your base learner is **too weak** and underfits?

- •High bias
- •Systematic errors

Boosting attacks bias by building an additive model step-by-step, where each new learner focuses on what previous learners got wrong.

### The central idea: additive modeling

Boosting constructs:

H\_M(x) = ∑\_{m=1..M} α\_m h\_m(x)

The sequence matters: hₘ is chosen based on the errors of H\_{m−1}.

Two big boosting views:

1. 1)**Reweighting view (AdaBoost-style)**: focus more on misclassified points.
2. 2)**Gradient view (Gradient Boosting)**: each learner fits the negative gradient (residual-like signal) of a loss function.

We’ll sketch both, because they illuminate the “why.”

---

## AdaBoost intuition (binary classification)

Assume labels y ∈ {−1, +1}, and weak learners output h(x) ∈ {−1, +1}.

AdaBoost maintains a weight distribution over training points:

- •Start with uniform weights wᵢ = 1/N.
- •Train a weak learner h₁ that minimizes weighted classification error.
- •Increase weights on misclassified points so the next learner pays more attention.

At step m, weighted error is:

err\_m = ∑ᵢ wᵢ [h\_m(xᵢ) ≠ yᵢ]

Then compute learner weight:

α\_m = (1/2) ln((1 − err\_m)/err\_m)

Update data weights:

wᵢ ← wᵢ · exp(−α\_m yᵢ h\_m(xᵢ))

Check what this does:

- •If yᵢ = h\_m(xᵢ), then yᵢ h\_m(xᵢ)=+1 ⇒ multiply by exp(−α\_m) (downweight)
- •If yᵢ ≠ h\_m(xᵢ), then yᵢ h\_m(xᵢ)=−1 ⇒ multiply by exp(+α\_m) (upweight)

Finally normalize w so ∑ᵢ wᵢ = 1.

The final classifier:

H(x) = sign(∑ₘ α\_m h\_m(x))

**Why it reduces bias:** each stage targets the “hard” points not yet handled.

**Risk:** if you keep adding learners, you can start fitting noise (variance can rise), especially with very complex base learners.

---

## Gradient Boosting intuition (general loss)

Gradient boosting generalizes boosting to arbitrary differentiable losses.

We want to minimize empirical risk:

L(H) = ∑ᵢ ℓ(yᵢ, H(xᵢ))

We build H as an additive model:

H\_m(x) = H\_{m−1}(x) + η · f\_m(x)

where f\_m is a new base learner (often a small tree), and η ∈ (0,1] is a learning rate.

### Why the “gradient” appears

We want to choose f\_m that most reduces L. In function space, the steepest descent direction is the **negative gradient**.

Define pseudo-residuals:

rᵢ^{(m)} = − ∂ℓ(yᵢ, H(xᵢ)) / ∂H(xᵢ) evaluated at H = H\_{m−1}

Then fit the next learner to these residuals:

- •f\_m(x) ≈ r^{(m)}

So gradient boosting is like:

- •“Compute what direction would reduce loss at each point.”
- •“Fit a model to that direction.”
- •“Take a small step.”

### Example: squared error regression

Let ℓ(y, H) = (1/2)(y − H)².

Compute:

∂ℓ/∂H = ∂(1/2)(y − H)² / ∂H

= (1/2) · 2(y − H) · (−1)

= −(y − H)

So the negative gradient is:

r = −(∂ℓ/∂H) = y − H

That’s exactly the residual.

Thus gradient boosting with squared loss repeatedly fits residuals.

### Why small trees (stumps) are common

Boosting often uses weak learners such as:

- •depth-1 stumps
- •depth-2 or depth-3 trees

They have high bias individually, but the additive combination builds complexity gradually. This helps control overfitting and makes training more stable.

### Regularization knobs in boosting

| Knob | What it does | Typical effect |
| --- | --- | --- |
| Learning rate η | scales each step | smaller η needs more trees but often generalizes better |
| # estimators M | number of steps | too large can overfit unless η small / trees small |
| Tree depth | base learner complexity | deeper trees fit interactions faster but risk overfitting |
| Subsample (stochastic GB) | fit each step on data subsample | reduces variance, adds randomness |

### Bias–variance view

Boosting is often described as:

- •**bias ↓** because the additive model expands expressiveness
- •**variance** can either stay manageable (with regularization) or explode (if overly aggressive)

This is why boosting tends to be powerful but sensitive to tuning.

## Application/Connection: Choosing Between Bagging, Random Forests, and Boosting

### Start from the problem: what’s failing?

Use the bias–variance diagnosis you already know.

- •If your model overfits wildly (high variance): prefer **bagging / random forests**.
- •If your model underfits (high bias): prefer **boosting**.

This is not absolute, but it’s a strong default.

### A decision table

| Situation | Symptoms | Good first choice | Why |
| --- | --- | --- | --- |
| Tree is unstable | train accuracy high, test low; results change with small data changes | Bagging | averaging cancels instability |
| Many features, strong predictors dominate | bagged trees still similar | Random Forest | feature subsampling reduces correlation |
| Need top accuracy on tabular data | linear/logistic underfits; interactions matter | Gradient Boosting | sequential correction builds complex function |
| Need minimal tuning | want strong baseline fast | Random Forest | robust defaults, less sensitive |
| Need calibrated probabilities | raw tree votes not calibrated | GB + calibration | boosting can improve ranking; calibrate separately |

### Interpreting H(x) in practice

Even though an ensemble is “many models,” you still ask:

- •What is H(x) optimizing?
- •Is H(x) stable under resampling?
- •Are base learners too correlated?

For random forests, stability increases with M; for boosting, stability depends on regularization.

### Computational tradeoffs

| Method | Parallelizable? | Typical training cost | Typical inference cost |
| --- | --- | --- | --- |
| Bagging | Yes | M independent fits | M predictions |
| Random Forest | Yes | M independent fits + split feature sampling | M predictions |
| Boosting | Not easily (sequential) | M sequential fits | M predictions |

Boosting’s sequential nature is the price you pay for its targeted bias reduction.

### Connection to “model averaging” beyond trees

Ensembles are not limited to trees.

- •You can bag neural nets.
- •You can average multiple logistic regressions trained on different bootstrap samples.

However, trees are a perfect match because:

- •they’re unstable (bagging helps a lot)
- •they can be weak learners (boosting works well)

### A note on stacking (beyond this node)

Another ensemble family is **stacking**, where a meta-model learns how to combine base learners. It’s powerful, but adds complexity and risks leakage. For this node, focus on the foundational trio: bagging, random forests, boosting.

### Practical checklist

Before choosing/tuning ensembles:

1. 1)Ensure train/test split is correct (time series needs time-aware split).
2. 2)Confirm metric (accuracy vs AUC vs RMSE) matches the goal.
3. 3)For boosting: start with small depth, small η, then increase M.
4. 4)For forests: increase M until performance plateaus; tune m\_try and leaf size.

### Where this node leads

Understanding ensembles unlocks:

- •feature importance and model interpretation techniques
- •modern gradient boosting systems (regularization, shrinkage, column subsampling)
- •uncertainty estimation via ensembles
- •robust baselines for tabular ML pipelines

## Worked Examples (3)

### Example 1: Majority Vote vs Probability Averaging (Why “Soft Voting” Can Differ)

Binary classification with three base learners. Each outputs a probability for class 1 at x. Convert to class labels with threshold 0.5.

Model outputs:

- •p₁ = 0.51
- •p₂ = 0.99
- •p₃ = 0.01

1. Convert each probability to a hard class prediction with threshold 0.5:

   h₁(x) = 1 (since 0.51 ≥ 0.5)

   h₂(x) = 1 (since 0.99 ≥ 0.5)

   h₃(x) = 0 (since 0.01 < 0.5)
2. Hard majority vote:

   Votes for class 1: 2

   Votes for class 0: 1

   So H\_hard(x) = 1
3. Soft voting (average probabilities):

   p̄ = (1/3)(0.51 + 0.99 + 0.01)

   = (1/3)(1.51)

   ≈ 0.5033
4. Apply threshold 0.5 to averaged probability:

   H\_soft(x) = 1 (since 0.5033 ≥ 0.5)
5. Now consider a tiny change: p₁ becomes 0.49 (barely flips).

   Hard predictions become:

   - •h₁(x)=0
   - •h₂(x)=1
   - •h₃(x)=0

   Hard vote ⇒ H\_hard(x)=0 (2 votes for 0).
6. Soft voting with new p₁:

   p̄ = (1/3)(0.49 + 0.99 + 0.01)

   = (1/3)(1.49)

   ≈ 0.4967

   Soft vote ⇒ H\_soft(x)=0 (since 0.4967 < 0.5)

**Insight:** Hard voting is sensitive to thresholding each model first; soft voting uses confidence and can be more stable. In practice, soft voting often performs better when base learners are reasonably calibrated.

### Example 2: How Random Forests Reduce Correlation (Using the Correlated-Error Variance Formula)

Assume each tree’s prediction error (for a fixed x) has variance σ² = 9. Compare two ensembles of M = 100 trees:

A) Bagged trees with high correlation ρ = 0.3

B) Random forest trees with lower correlation ρ = 0.05

Use:

Var(H − f) = (σ²/M) + ((M−1)/M) ρ σ²

1. Compute common quantities:

   M = 100

   σ² = 9

   (σ²/M) = 9/100 = 0.09

   ((M−1)/M) = 99/100 = 0.99
2. Case A (ρ = 0.3):

   Var = 0.09 + 0.99 · 0.3 · 9

   = 0.09 + 0.99 · 2.7

   = 0.09 + 2.673

   = 2.763
3. Case B (ρ = 0.05):

   Var = 0.09 + 0.99 · 0.05 · 9

   = 0.09 + 0.99 · 0.45

   = 0.09 + 0.4455

   = 0.5355
4. Compare:

   2.763 / 0.5355 ≈ 5.16

   So reducing correlation from 0.3 to 0.05 cuts variance by about 5×, even with the same number of trees and same per-tree variance.

**Insight:** Adding more trees helps, but reducing correlation ρ can matter even more. Random forests do exactly this via feature subsampling, especially at high-level splits.

### Example 3: One Step of Gradient Boosting for Squared Error (Residual Fitting)

We have three training points with scalar x and y:

(x₁, y₁) = (0, 1)

(x₂, y₂) = (1, 3)

(x₃, y₃) = (2, 2)

Start with constant model H₀(x) = 2 (already fit somehow). Use squared error ℓ = (1/2)(y − H)².

Compute residuals and fit a simple base learner f₁ that predicts the mean residual (a constant). Use learning rate η = 0.5.

1. Compute residuals rᵢ = yᵢ − H₀(xᵢ):

   r₁ = 1 − 2 = −1

   r₂ = 3 − 2 = +1

   r₃ = 2 − 2 = 0
2. Fit base learner f₁ as a constant equal to mean residual:

   mean(r) = (1/3)(−1 + 1 + 0) = 0

   So f₁(x) = 0 for all x
3. Update the model:

   H₁(x) = H₀(x) + η f₁(x)

   = 2 + 0.5 · 0

   = 2
4. Interpretation:

   The residuals had zero mean, so the best constant step is 0; a constant learner cannot improve H₀.

   If instead f₁ were a stump that split x (e.g., predict different residual means for x < 1.5 vs ≥ 1.5), it could make progress.

**Insight:** Gradient boosting only improves when the base learner can represent the structure in the residuals. This is why small trees (not just constants) are common: they can capture patterns in residuals and reduce loss step-by-step.

## Key Takeaways

- ✓

  An ensemble builds H(x) by aggregating predictions from base learners hᵢ(x) via averaging, voting, or weighted sums.
- ✓

  Averaging reduces variance most effectively when base learner errors are weakly correlated; correlation ρ creates a variance floor.
- ✓

  Bagging creates diversity by training on bootstrap samples; it is especially effective for unstable learners like decision trees.
- ✓

  Out-of-bag (OOB) error provides an efficient internal validation estimate for bagged trees and random forests.
- ✓

  Random forests add feature subsampling at each split to reduce tree correlation, often giving a large additional gain over pure bagging.
- ✓

  Boosting builds an additive model sequentially; each step focuses on previous errors, often reducing bias dramatically.
- ✓

  Gradient boosting can be seen as functional gradient descent: each learner fits pseudo-residuals (negative gradients) of the loss.
- ✓

  Bagging/forests are typically robust and easy to tune; boosting can reach higher accuracy but is more sensitive to hyperparameters and overfitting.

## Common Mistakes

- ✗

  Assuming “more models always helps” without checking correlation: if base learners are too similar, adding more barely improves.
- ✗

  Using boosting with overly deep trees and large learning rate η, leading to fast overfitting and unstable performance.
- ✗

  Comparing methods without controlling evaluation properly (e.g., tuning on test set, ignoring time-aware splits, or mixing leakage into OOB/validation).
- ✗

  Interpreting random forest impurity-based feature importance as causal or as unbiased (it can favor high-cardinality or noisy features).

## Practice

easy

You train 200 bagged trees for regression. Each tree has error variance σ² = 4 and pairwise correlation ρ = 0.2. Use Var(H − f) = (σ²/M) + ((M−1)/M) ρ σ² to compute the ensemble error variance. Then compute the limiting variance as M → ∞.

**Hint:** Compute σ²/M and ((M−1)/M) first. The limit removes the σ²/M term and sets ((M−1)/M) → 1.

Show solution

M = 200, σ² = 4, ρ = 0.2.

σ²/M = 4/200 = 0.02

(M−1)/M = 199/200 = 0.995

Var = 0.02 + 0.995 · 0.2 · 4

= 0.02 + 0.995 · 0.8

= 0.02 + 0.796

= 0.816

As M → ∞:

Var → ρσ² = 0.2 · 4 = 0.8

medium

In a random forest for classification with d = 36 features, compare two settings: m\_try = 36 (no feature subsampling) vs m\_try = √d. What is √d here, and why might it improve test performance even though each split sees fewer features?

**Hint:** Compute √36. Then relate feature subsampling to reduced correlation ρ between trees.

Show solution

√d = √36 = 6.

With m\_try = 36, every split considers all features, so many trees choose the same strong features near the top. Trees become more similar, increasing correlation ρ of their errors.

With m\_try = 6, each split considers only 6 random features. Different trees are forced to explore different top splits, reducing correlation ρ. Even if individual trees become slightly weaker, the ensemble variance can drop enough to improve test performance.

medium

For squared error regression with loss ℓ = (1/2)(y − H)², derive the pseudo-residual r = −∂ℓ/∂H and show it equals the ordinary residual (y − H).

**Hint:** Differentiate (1/2)(y − H)² with respect to H using the chain rule.

Show solution

ℓ(y, H) = (1/2)(y − H)²

∂ℓ/∂H

= (1/2) · 2(y − H) · ∂(y − H)/∂H

= (y − H) · (−1)

= −(y − H)

Therefore the pseudo-residual is:

r = −∂ℓ/∂H = y − H

So for squared loss, gradient boosting fits ordinary residuals.

## Connections

[Decision Trees](/tech-tree/decision-trees/)

[Bias-Variance Tradeoff](/tech-tree/bias-variance-tradeoff/)

[Cross-Validation](/tech-tree/cross-validation/)

[Gradient Descent](/tech-tree/gradient-descent/)

[Regularization](/tech-tree/regularization/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
