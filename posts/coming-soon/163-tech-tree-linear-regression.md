---
title: Linear Regression
description: Predicting continuous values. Least squares, normal equations.
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
inspiration_url: https://templeton.host/tech-tree/linear-regression/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/linear-regression/](https://templeton.host/tech-tree/linear-regression/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Linear Regression

Machine LearningDifficulty: ★★★☆☆Depth: 9Unlocks: 4

Predicting continuous values. Least squares, normal equations.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Linear predictive model: outputs are a linear combination of input features (include intercept as a constant feature).
- -Least-squares fitting: choose coefficients that minimize the sum of squared residuals (SSE).

## Key Symbols & Notation

X (design matrix: examples x features, include column of ones for intercept)beta (parameter/coefficients vector)y (target/response vector of observed continuous values)

## Essential Relationships

- -Normal equations: setting the SSE gradient to zero gives (X^T X) \* beta = X^T \* y, the linear condition that characterizes the least-squares solution.

## Prerequisites (2)

[Machine Learning Introduction5 atoms](/tech-tree/ml-intro/)[Projections6 atoms](/tech-tree/projections/)

## Unlocks (1)

[Time Series Foundationslvl 3](/tech-tree/time-series-foundations/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[real estateBusiness

Hedonic pricing models (price = f(sqft, beds, location, age)) are the canonical RE valuation tool - automated valuation models are literally multivariate regression](/business/real-estate/)

Advanced Learning Details

### Graph Position

150

Depth Cost

4

Fan-Out (ROI)

1

Bottleneck Score

9

Chain Length

### Cognitive Load

6

Atomic Elements

39

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (14)

- - linear prediction model: hypothesis h\_θ(x) = θ^T x (prediction as a linear combination of features)
- - bias / intercept term (handled by augmenting feature vector with a constant 1)
- - design matrix X (matrix whose rows or rows/columns collect all training feature vectors)
- - parameter vector θ (coefficients to be estimated)
- - predicted outputs vector ŷ (y-hat) defined as ŷ = X θ
- - residuals vector r defined as r = y - ŷ
- - mean squared error cost function J(θ) written in ML form (often (1/2m) Σ (h\_θ(x\_i) - y\_i)^2 or (1/2m) ||Xθ - y||^2)
- - normal equations: the closed-form condition for least-squares minimizer (X^T X θ = X^T y)
- - closed-form solution via matrix inverse θ = (X^T X)^{-1} X^T y (when X^T X is invertible)
- - Moore–Penrose pseudoinverse solution θ = X^+ y for singular or rank-deficient cases
- - hat matrix H = X (X^T X)^{-1} X^T that maps y to predictions ŷ
- - orthogonality condition for least squares: residuals are orthogonal to each column of X (X^T r = 0)
- - full column rank condition: X^T X invertible if and only if columns of X are linearly independent
- - interpretation of linear regression as projecting the target vector y onto the column space of X

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Linear regression is the “hello world” of predicting numbers: you pick a linear rule, compare its predictions to real outcomes, and adjust the rule to make the squared errors as small as possible. Under the hood, it’s an elegant geometry problem about projecting **y** onto the column space of **X**.

TL;DR:

Linear regression predicts a continuous target by ŷ = **X**β. We fit β by minimizing the sum of squared residuals ‖**y** − **X**β‖². The solution satisfies the normal equations **X**ᵀ**X**β = **X**ᵀ**y** (when **X**ᵀ**X** is invertible) and geometrically corresponds to projecting **y** onto the subspace spanned by the columns of **X**.

## What Is Linear Regression?

### The goal

In supervised learning for **continuous** outputs, you want a model that maps an input feature vector to a real number:

- •Input (features): a vector **x** ∈ ℝᵈ
- •Output (target): y ∈ ℝ

Linear regression is the simplest widely useful choice:

- •**Model**: predict with a linear function of features.

### The linear predictive model

For one example with features **x**, linear regression predicts

ŷ = β₀ + β₁x₁ + β₂x₂ + … + β\_d x\_d

To keep notation clean, we fold the intercept into the feature vector by adding a constant feature:

- •Define x₀ = 1
- •Define β = [β₀, β₁, …, β\_d]ᵀ
- •Define **x** = [x₀, x₁, …, x\_d]ᵀ

Then the prediction becomes a dot product:

ŷ = **x**ᵀβ

### From one example to a dataset

Suppose you have n training examples. Stack them into a design matrix **X**:

- •**X** ∈ ℝⁿˣᵖ where p = d+1 if you included the intercept column of ones
- •Each row i is **x**ᵢᵀ

Also stack targets into a vector:

- •**y** ∈ ℝⁿ

Predictions for all examples at once:

**ŷ** = **X**β

This compact form is the main reason linear regression is such a good “bridge” topic: it connects machine learning, linear algebra, geometry, and optimization.

### Why the squared error?

You need a rule for choosing β. Linear regression chooses β to make predictions close to **y**.

Define residuals:

**r** = **y** − **X**β

A natural idea is to minimize total error. But we need a scalar objective. Squared error is the classic choice:

SSE(β) = ∑ᵢ (yᵢ − ŷᵢ)² = ‖**y** − **X**β‖²

Why square?

- •It penalizes large mistakes more than small ones.
- •It yields a smooth, convex objective (one global minimum).
- •It leads to closed-form solutions via linear algebra.

### What you should keep in mind

Linear regression is not “the true relationship is linear.” It’s:

- •“I will approximate the relationship with a linear function of chosen features.”

You can include nonlinear transformations as features (e.g., x², log x), and the model is still *linear in β*.

## Core Mechanic 1: Least-Squares Fitting (Minimizing ‖y − Xβ‖²)

### The optimization problem

Least squares fitting means choosing β to minimize squared residual length:

minimize over β: J(β) = ‖**y** − **X**β‖²

This is a geometry problem wearing an optimization costume.

- •**X**β is restricted to lie in the column space of **X** (all linear combinations of columns).
- •You want the point **X**β in that subspace that is closest to **y**.

So the fitted predictions **X**β̂ are the **orthogonal projection** of **y** onto Col(**X**).

### Expanding the objective (so we can take derivatives)

Write J(β) as a quadratic form:

J(β) = (**y** − **X**β)ᵀ(**y** − **X**β)

Expand carefully:

J(β)

= (**y**ᵀ − βᵀ**X**ᵀ)(**y** − **X**β)

= **y**ᵀ**y** − **y**ᵀ**X**β − βᵀ**X**ᵀ**y** + βᵀ**X**ᵀ**X**β

Note that **y**ᵀ**X**β is a scalar, and equals its transpose:

**y**ᵀ**X**β = ( **y**ᵀ**X**β )ᵀ = βᵀ**X**ᵀ**y**

So the middle two terms combine:

J(β) = **y**ᵀ**y** − 2βᵀ**X**ᵀ**y** + βᵀ**X**ᵀ**X**β

This makes it clear J(β) is a convex quadratic function in β.

### The gradient and the normal equations

To minimize J(β), set its gradient to zero.

Using standard matrix calculus results:

∂/∂β (βᵀ**A**β) = (**A** + **A**ᵀ)β, and when **A** is symmetric: = 2**A**β

Here **A** = **X**ᵀ**X**, which is symmetric.

Compute the gradient:

∇β J(β)

= ∇β( **y**ᵀ**y** − 2βᵀ**X**ᵀ**y** + βᵀ**X**ᵀ**X**β )

= 0 − 2**X**ᵀ**y** + 2**X**ᵀ**X**β

Set ∇β J(β) = **0**:

2**X**ᵀ**X**β − 2**X**ᵀ**y** = **0**

Divide by 2:

**X**ᵀ**X**β = **X**ᵀ**y**

These are the **normal equations**.

### Solving for β̂

If **X**ᵀ**X** is invertible (full column rank), then

β̂ = (**X**ᵀ**X**)⁻¹ **X**ᵀ **y**

This is the classic closed-form least squares solution.

If **X**ᵀ**X** is not invertible (e.g., perfectly collinear features), there are infinitely many solutions that achieve the same minimum SSE. A common choice is the minimum-norm solution via the Moore–Penrose pseudoinverse:

β̂ = **X**⁺ **y**

### The projection viewpoint (link to prerequisites)

At the optimum, residual **r** = **y** − **X**β̂ is orthogonal to the column space of **X**.

In algebra:

**X**ᵀ(**y** − **X**β̂) = **0**

which rearranges to the normal equations.

So you can read the normal equations as:

- •“Residuals are perpendicular to every column of **X**.”

That is exactly the condition for an orthogonal projection.

### What least squares is really doing

Least squares chooses β to balance tradeoffs across all points.

- •You generally can’t make all residuals zero unless **y** lies in Col(**X**) (perfectly representable).
- •Instead, you choose the closest representable vector **X**β to **y**.

This is why linear regression is both:

- •An optimization algorithm: minimize SSE
- •A linear algebra operation: projection onto a subspace

## Core Mechanic 2: Intercept, Geometry, and When the Normal Equations Behave

### The intercept as a constant feature

Including an intercept means adding a column of ones:

**X** = [ **1** | feature columns ]

This matters because without an intercept, the model is forced to go through the origin in feature space (in 1D, the line must pass through (0,0)). In real data, that constraint is often unjustified and increases error.

### Shapes and dimensions (so you don’t get lost)

It helps to keep a mental “type system” for linear regression:

- •**X**: n × p (n examples, p features including intercept)
- •β: p × 1
- •**y**: n × 1
- •**X**β: n × 1
- •**X**ᵀ**X**: p × p
- •**X**ᵀ**y**: p × 1

If you ever feel stuck, check dimensions first.

### Geometry: column space and projections

The set of all predictions the model can make is

{ **X**β : β ∈ ℝᵖ } = Col(**X**)

That is a subspace of ℝⁿ (or an affine subspace if you treat the intercept differently; with the column-of-ones trick, it’s still a linear subspace in ℝⁿ).

The fitted predictions are

**ŷ** = **X**β̂ = Proj\_{Col(**X**)}(**y**)

The residual vector

**r** = **y** − **ŷ**

is orthogonal to Col(**X**).

### When does (**X**ᵀ**X**)⁻¹ exist?

(**X**ᵀ**X**) is invertible iff the columns of **X** are linearly independent (full column rank). Practically, it can fail for several reasons:

- •**Perfect multicollinearity**: one feature is an exact linear combination of others.
- •**Too many features**: p > n guarantees rank ≤ n < p, so not invertible.
- •**Redundant intercept**: e.g., you accidentally include two constant columns.

Even if it exists, it can be numerically unstable if **X**ᵀ**X** is ill-conditioned.

### Practical numerical note: don’t literally invert

Although the formula β̂ = (**X**ᵀ**X**)⁻¹**X**ᵀ**y** is conceptually important, computing the inverse explicitly is usually a bad idea numerically.

Common stable approaches:

| Approach | Idea | Pros | Cons |
| --- | --- | --- | --- |
| QR decomposition | **X** = **Q****R**, solve **R**β = **Q**ᵀ**y** | Stable, standard | More linear algebra machinery |
| SVD / pseudoinverse | **X** = **U**Σ**V**ᵀ | Best for rank-deficient cases | Slower |
| Gradient-based optimization | minimize J(β) iteratively | Scales, works with huge data | Needs learning rate / iterations |

This lesson focuses on the conceptual math; just remember that implementations often use QR/SVD under the hood.

### Centering and scaling (feature preprocessing)

Least squares itself doesn’t require scaling, but conditioning and interpretation improve when you:

- •center features (subtract mean)
- •scale features (divide by standard deviation)

Centering also interacts with the intercept:

- •If each non-intercept feature has mean 0, then β₀ becomes the mean of y (when the model includes only intercept) and is often more interpretable.

### A note on “linear”

Linear regression is linear in parameters β, not necessarily linear in raw input.

Example: If you use features [1, x, x²], predictions are

ŷ = β₀ + β₁x + β₂x²

This is a quadratic curve in x, but still a linear regression model because it is a linear combination of features with coefficients β.

## Application/Connection: Prediction, Evaluation, and Why It’s a Foundation for ML

### Using the model to predict

After fitting β̂, predictions for a new example **x**ₙₑw are

ŷₙₑw = **x**ₙₑwᵀ β̂

For a batch of new examples **X**ₙₑw:

**ŷ**ₙₑw = **X**ₙₑw β̂

### Interpreting coefficients (carefully)

If feature xⱼ increases by 1 (holding other features fixed), the prediction changes by βⱼ.

That “holding fixed” clause is crucial: in correlated data, changing one feature while keeping others constant may describe a scenario that doesn’t naturally occur.

### Common evaluation metrics

Since the training objective is SSE, related metrics are common:

- •MSE = (1/n)‖**y** − **X**β̂‖²
- •RMSE = √MSE
- •MAE = (1/n)∑ᵢ |yᵢ − ŷᵢ| (not the training objective here, but popular)

### R² as “variance explained” (intuition)

Define:

- •SSE = ∑ᵢ (yᵢ − ŷᵢ)²
- •SST = ∑ᵢ (yᵢ − ȳ)² where ȳ is mean of y

Then

R² = 1 − SSE/SST

Interpretation:

- •R² = 0 means “no better than predicting the mean.”
- •R² = 1 means perfect fit.

Be cautious: R² always (weakly) increases when you add features, even useless ones. This is one reason regularization (like ridge regression) matters later.

### Overfitting and generalization

Linear regression can still overfit when:

- •you add too many features
- •you add high-degree polynomial features
- •you have limited data with noisy targets

Least squares will chase patterns in the sample even if they are not stable.

The usual fix is to evaluate on held-out data (validation/test) and/or add regularization.

### Why linear regression is foundational

Linear regression is a gateway to many later ideas:

- •**Gradient descent**: minimizing a convex objective
- •**Regularization**: ridge/lasso as modified least squares
- •**Probabilistic modeling**: with Gaussian noise assumptions, least squares becomes maximum likelihood
- •**Generalized linear models**: logistic regression changes the output link but keeps linear predictors
- •**Neural networks**: last layer often is linear; training uses similar principles

If you understand linear regression deeply—especially the projection view—you’re set up to understand a lot of ML with much less memorization.

## Worked Examples (3)

### Fit a line in 1D with an intercept (compute β̂ via normal equations)

Data: (x, y) = (0, 1), (1, 2), (2, 2). Use an intercept by setting features **x** = [1, x]ᵀ. Compute β̂ = [β₀, β₁]ᵀ.

1. Build the design matrix **X** (n = 3, p = 2):

   **X** = [ [1, 0],

   [1, 1],

   [1, 2] ]
2. Build the target vector:

   **y** = [1, 2, 2]ᵀ
3. Compute **X**ᵀ**X**:

   **X**ᵀ**X** = [ [1,1,1],

   [0,1,2] ] · [ [1,0],

   [1,1],

   [1,2] ]

   = [ [3, 3],

   [3, 5] ]
4. Compute **X**ᵀ**y**:

   **X**ᵀ**y** = [ [1,1,1],

   [0,1,2] ] · [1,2,2]ᵀ

   = [ 1+2+2,

   0·1 + 1·2 + 2·2 ]ᵀ

   = [5, 6]ᵀ
5. Solve the normal equations (**X**ᵀ**X**)β = **X**ᵀ**y**:

   [ [3, 3],

   [3, 5] ] · [β₀, β₁]ᵀ = [5, 6]ᵀ
6. Solve the linear system:

   From 3β₀ + 3β₁ = 5 ⇒ β₀ + β₁ = 5/3

   From 3β₀ + 5β₁ = 6

   Subtract the first equation (scaled by 3):

   (3β₀ + 5β₁) − (3β₀ + 3β₁) = 6 − 5

   2β₁ = 1 ⇒ β₁ = 1/2

   Then β₀ = 5/3 − 1/2 = 10/6 − 3/6 = 7/6
7. Write the fitted model:

   ŷ = β₀ + β₁x = 7/6 + (1/2)x
8. Compute fitted values and residuals:

   For x=0: ŷ=7/6, residual = 1 − 7/6 = −1/6

   For x=1: ŷ=7/6+1/2=7/6+3/6=10/6=5/3, residual = 2 − 5/3 = 1/3

   For x=2: ŷ=7/6+1=13/6, residual = 2 − 13/6 = −1/6

**Insight:** Even in this tiny dataset, the best line is not the one that hits the most points exactly; it’s the one whose residual vector has minimal length ‖**r**‖ and is orthogonal to the column space of **X**.

### Verify the orthogonality condition \*\*X\*\*ᵀ(\*\*y\*\* − \*\*X\*\*β̂) = \*\*0\*\* for the fitted line

Use the previous example’s β̂ with **X** and **y**. Compute residual **r** = **y** − **X**β̂ and check **X**ᵀ**r** = **0**.

1. Recall:

   **X** = [ [1,0],

   [1,1],

   [1,2] ], **y** = [1,2,2]ᵀ, β̂ = [7/6, 1/2]ᵀ
2. Compute predictions **ŷ** = **X**β̂:

   Row 1: [1,0]·β̂ = 7/6

   Row 2: [1,1]·β̂ = 7/6 + 1/2 = 5/3

   Row 3: [1,2]·β̂ = 7/6 + 1 = 13/6

   So **ŷ** = [7/6, 5/3, 13/6]ᵀ
3. Compute residuals **r** = **y** − **ŷ**:

   **r** = [1 − 7/6,

   2 − 5/3,

   2 − 13/6]ᵀ

   = [−1/6,

   1/3,

   −1/6]ᵀ
4. Compute **X**ᵀ**r**:

   **X**ᵀ**r** = [ [1,1,1],

   [0,1,2] ] · [−1/6, 1/3, −1/6]ᵀ
5. First component (dot with column of ones):

   (−1/6) + (1/3) + (−1/6)

   = −1/6 + 2/6 − 1/6

   = 0
6. Second component (dot with x column):

   0·(−1/6) + 1·(1/3) + 2·(−1/6)

   = 1/3 − 2/6

   = 2/6 − 2/6

   = 0
7. Therefore **X**ᵀ(**y** − **X**β̂) = **X**ᵀ**r** = **0**, confirming the projection/normal-equation condition.

**Insight:** The normal equations are not arbitrary algebra: they encode the geometric fact that the residual is perpendicular to every feature column, meaning you can’t move within the model’s subspace to get any closer to **y**.

### Multiple features: compute β̂ for a tiny 2-feature design matrix

Let **X** include an intercept and two features:

**X** = [ [1, 1, 0],

[1, 0, 1],

[1, 1, 1] ],

**y** = [1, 2, 2]ᵀ.

Compute β̂ by solving **X**ᵀ**X**β = **X**ᵀ**y**.

1. Write columns of **X**:

   Intercept column **c**₀ = [1,1,1]ᵀ

   Feature 1 column **c**₁ = [1,0,1]ᵀ

   Feature 2 column **c**₂ = [0,1,1]ᵀ
2. Compute **X**ᵀ**X** using dot products of columns:

   **X**ᵀ**X** = [ [**c**₀ᵀ**c**₀, **c**₀ᵀ**c**₁, **c**₀ᵀ**c**₂],

   [**c**₁ᵀ**c**₀, **c**₁ᵀ**c**₁, **c**₁ᵀ**c**₂],

   [**c**₂ᵀ**c**₀, **c**₂ᵀ**c**₁, **c**₂ᵀ**c**₂] ]
3. Compute each dot product:

   **c**₀ᵀ**c**₀ = 1+1+1 = 3

   **c**₀ᵀ**c**₁ = 1+0+1 = 2

   **c**₀ᵀ**c**₂ = 0+1+1 = 2

   **c**₁ᵀ**c**₁ = 1+0+1 = 2

   **c**₁ᵀ**c**₂ = (1·0)+(0·1)+(1·1) = 1

   **c**₂ᵀ**c**₂ = 0+1+1 = 2
4. So:

   **X**ᵀ**X** = [ [3, 2, 2],

   [2, 2, 1],

   [2, 1, 2] ]
5. Compute **X**ᵀ**y** by dotting columns with **y**:

   **X**ᵀ**y** = [ **c**₀ᵀ**y**, **c**₁ᵀ**y**, **c**₂ᵀ**y** ]ᵀ
6. Compute:

   **c**₀ᵀ**y** = 1+2+2 = 5

   **c**₁ᵀ**y** = 1·1 + 0·2 + 1·2 = 3

   **c**₂ᵀ**y** = 0·1 + 1·2 + 1·2 = 4

   So **X**ᵀ**y** = [5, 3, 4]ᵀ
7. Solve the system:

   [ [3, 2, 2],

   [2, 2, 1],

   [2, 1, 2] ] · [β₀, β₁, β₂]ᵀ = [5, 3, 4]ᵀ
8. One solution path (elimination):

   From equation (2): 2β₀ + 2β₁ + β₂ = 3

   From equation (3): 2β₀ + β₁ + 2β₂ = 4

   Subtract (3) − (2): (2β₀ cancels)

   (β₁ + 2β₂) − (2β₁ + β₂) = 4 − 3

   (−β₁ + β₂) = 1 ⇒ β₂ = β₁ + 1
9. Use equation (1): 3β₀ + 2β₁ + 2β₂ = 5

   Substitute β₂:

   3β₀ + 2β₁ + 2(β₁ + 1) = 5

   3β₀ + 4β₁ + 2 = 5

   3β₀ + 4β₁ = 3
10. Use equation (2): 2β₀ + 2β₁ + β₂ = 3

    Substitute β₂ = β₁ + 1:

    2β₀ + 2β₁ + (β₁ + 1) = 3

    2β₀ + 3β₁ + 1 = 3

    2β₀ + 3β₁ = 2
11. Solve the 2×2 system:

    3β₀ + 4β₁ = 3

    2β₀ + 3β₁ = 2

    Multiply the second by 3: 6β₀ + 9β₁ = 6

    Multiply the first by 2: 6β₀ + 8β₁ = 6

    Subtract: (6β₀+9β₁) − (6β₀+8β₁) = 6 − 6

    β₁ = 0

    Then 2β₀ + 3·0 = 2 ⇒ β₀ = 1

    Then β₂ = β₁ + 1 = 1
12. So β̂ = [1, 0, 1]ᵀ and the model is:

    ŷ = 1 + 0·x₁ + 1·x₂ = 1 + x₂

**Insight:** Even with multiple features, the workflow is the same: build **X**, compute **X**ᵀ**X** and **X**ᵀ**y**, then solve. Thinking in terms of column dot products makes **X**ᵀ**X** feel less mysterious.

## Key Takeaways

- ✓

  Linear regression predicts with **ŷ** = **X**β, where **X** includes a column of ones to represent the intercept.
- ✓

  Least squares chooses β̂ to minimize SSE = ‖**y** − **X**β‖², a convex quadratic objective with a unique minimum when **X** has full column rank.
- ✓

  The normal equations **X**ᵀ**X**β̂ = **X**ᵀ**y** come directly from setting the gradient ∇β‖**y** − **X**β‖² to zero.
- ✓

  Geometrically, **X**β̂ is the orthogonal projection of **y** onto Col(**X**); the residual **r** = **y** − **X**β̂ is orthogonal to every column of **X**.
- ✓

  (**X**ᵀ**X**) may be singular if features are redundant or if p > n; then use a pseudoinverse or a different solver (QR/SVD).
- ✓

  The intercept prevents the model from being forced through the origin and usually improves fit unless you have strong reasons to omit it.
- ✓

  Metrics like MSE/RMSE connect directly to SSE; R² measures improvement over predicting the mean but can be misleading when adding many features.

## Common Mistakes

- ✗

  Forgetting the intercept (not adding the column of ones), which silently forces predictions to pass through the origin.
- ✗

  Trying to compute (**X**ᵀ**X**)⁻¹ explicitly in code; solving linear systems (QR/SVD) is typically more stable.
- ✗

  Mixing up shapes (e.g., using **X****X**ᵀ instead of **X**ᵀ**X**) and getting dimension errors or incorrect equations.
- ✗

  Assuming coefficients are always causal or always directly interpretable even when features are correlated or confounded.

## Practice

easy

Given data points (x, y) = (1, 1), (2, 2), (3, 2). Fit a 1D linear regression with intercept using normal equations. Report β̂ and the predicted values ŷ for x = 1,2,3.

**Hint:** Use **X** = [[1,1],[1,2],[1,3]] and β̂ = (**X**ᵀ**X**)⁻¹**X**ᵀ**y** (or solve the 2×2 normal equations directly).

Show solution

Let **X** = [ [1,1], [1,2], [1,3] ] and **y** = [1,2,2]ᵀ.

Compute **X**ᵀ**X** = [ [3, 6], [6, 14] ].

Compute **X**ᵀ**y** = [ 1+2+2, 1·1+2·2+3·2 ]ᵀ = [5, 11]ᵀ.

Solve [ [3,6],[6,14] ] [β₀,β₁]ᵀ = [5,11]ᵀ.

From 3β₀+6β₁=5 and 6β₀+14β₁=11.

Multiply the first by 2: 6β₀+12β₁=10. Subtract from second: 2β₁=1 ⇒ β₁=1/2.

Then 3β₀+6(1/2)=5 ⇒ 3β₀+3=5 ⇒ β₀=2/3.

So β̂ = [2/3, 1/2]ᵀ.

Predictions: x=1: ŷ=2/3+1/2=7/6; x=2: ŷ=2/3+1=5/3; x=3: ŷ=2/3+3/2=13/6.

medium

Show that at the least-squares optimum β̂, the residual **r** = **y** − **X**β̂ is orthogonal to every column of **X**. (Derive the condition, don’t just state it.)

**Hint:** Start from J(β) = ‖**y** − **X**β‖². Expand and take ∇β, then set it equal to **0**.

Show solution

Let J(β) = (**y** − **X**β)ᵀ(**y** − **X**β).

Expand:

J(β) = **y**ᵀ**y** − 2βᵀ**X**ᵀ**y** + βᵀ**X**ᵀ**X**β.

Take gradient:

∇β J(β) = −2**X**ᵀ**y** + 2**X**ᵀ**X**β.

At optimum β̂: ∇β J(β̂) = **0** ⇒ **X**ᵀ**X**β̂ = **X**ᵀ**y**.

Rearrange:

**X**ᵀ**y** − **X**ᵀ**X**β̂ = **0**

⇒ **X**ᵀ(**y** − **X**β̂) = **0**

⇒ **X**ᵀ**r** = **0**.

This means each column **c**ⱼ of **X** satisfies **c**ⱼᵀ**r** = 0, i.e., **r** is orthogonal to every feature column.

hard

Suppose you have two features where the second is exactly double the first for all examples (x₂ = 2x₁), and you include an intercept. What does this imply about **X**ᵀ**X** and the uniqueness of β̂? What would you do in practice?

**Hint:** Think about linear dependence among columns of **X** and what that means for invertibility. Consider pseudoinverse or removing a redundant feature.

Show solution

If x₂ = 2x₁ for all examples, then the column for feature 2 equals 2 times the column for feature 1. Therefore the columns of **X** are linearly dependent, so **X** does not have full column rank. Then **X**ᵀ**X** is singular (not invertible).

Least squares still has minimizers, but β̂ is not unique: many coefficient vectors produce the same predictions **X**β (because changing β₁ and β₂ along the dependent direction leaves **X**β unchanged).

In practice you can (1) drop one of the redundant features, restoring full rank; (2) use a pseudoinverse solution β̂ = **X**⁺**y** (which selects a minimum-norm β̂ among all minimizers); or (3) add regularization (e.g., ridge regression) to make the problem well-posed.

## Connections

- •[Machine Learning Introduction](/tech-tree/ml-intro/)
- •[Projections](/tech-tree/projections/)
- •[Gradient Descent](/tech-tree/gradient-descent/)
- •[Ridge Regression](/tech-tree/ridge-regression/)
- •[Logistic Regression](/tech-tree/logistic-regression/)
- •[Bias-Variance Tradeoff](/tech-tree/bias-variance/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
