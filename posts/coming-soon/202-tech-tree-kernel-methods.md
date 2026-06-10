---
title: Kernel Methods
description: Implicit feature spaces via kernel functions. Kernel trick.
date: '2026-07-01'
scheduled: '2027-01-18'
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
inspiration_url: https://templeton.host/tech-tree/kernel-methods/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/kernel-methods/](https://templeton.host/tech-tree/kernel-methods/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Kernel Methods

Machine LearningDifficulty: ★★★★☆Depth: 10Unlocks: 0

Implicit feature spaces via kernel functions. Kernel trick.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Kernel function evaluates the inner product between implicit feature mappings of two inputs.
- -Existence of an implicit feature mapping phi(x) that represents inputs in a (possibly infinite-dimensional) feature space.
- -Positive-semidefiniteness (Mercer condition): valid kernels yield positive semidefinite Gram matrices and thus correspond to inner products.

## Key Symbols & Notation

k(x, x') - kernel function (inner-product evaluator)phi(x) - implicit feature mapping of input x

## Essential Relationships

- -k(x, x') = <phi(x), phi(x')>, so any algorithm that uses only dot products can replace them with k(x, x') (the kernel trick) to operate in feature space without computing phi explicitly.

## Prerequisites (2)

[Support Vector Machines6 atoms](/tech-tree/svm/)[Dot Product5 atoms](/tech-tree/dot-product/)

Advanced Learning Details

### Graph Position

92

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

44

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (19)

- - feature map φ: a map φ(x) that sends inputs into a (possibly high- or infinite-dimensional) feature space
- - kernel function k(x, x'): a function that returns an inner product in feature space without computing φ explicitly
- - Gram (kernel) matrix K: matrix with entries K\_ij = k(x\_i, x\_j) computed on a dataset
- - positive semidefinite (PSD) kernel: kernels whose Gram matrices are symmetric and positive semidefinite
- - Mercer’s theorem (kernel existence / eigenexpansion): condition linking PSD kernels to an eigenfunction expansion / implicit feature space
- - reproducing kernel Hilbert space (RKHS): the Hilbert space of functions associated with a kernel
- - reproducing property: evaluation f(x) equals the inner product of f with the kernel section k(x, ·) in the RKHS
- - representer theorem: regularized empirical-risk minimizers admit representations as finite kernel expansions over training points
- - dual (α) representation of solutions: model parameters expressed as coefficients α on kernel evaluations at training points
- - kernel PCA: PCA performed in feature space using eigen-decomposition of the centered kernel matrix
- - kernel ridge regression (kernelized Tikhonov): regression solved in dual form using the kernel matrix (involves (K + λI)^{-1})
- - common kernel families and their behavior: Gaussian/RBF, polynomial, sigmoid (and their characteristic properties)
- - kernel hyperparameters: bandwidth (σ or γ) for RBF, degree d and offset c for polynomial, scale/slope for sigmoid
- - implicit infinite-dimensional feature spaces: some kernels (e.g., RBF) correspond to infinite-dimensional φ
- - closure properties of kernels: sums, products, and positive scalings of kernels remain valid kernels
- - centering a kernel matrix: making the kernel correspond to zero-mean features in feature space (necessary for kernel PCA, etc.)
- - kernel as a similarity measure distinct from raw Euclidean distance - encodes similarity via feature-space inner products
- - computational scaling and storage tradeoffs: kernel methods depend on n (number of examples) via the n×n Gram matrix
- - kernel approximations (brief concept): methods (e.g., Nyström, random features) to reduce kernel computational cost

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Kernel methods let you act like you mapped your data into a huge (even infinite-dimensional) feature space—without ever computing those features explicitly. You keep working with dot products, but you replace “dot product in input space” with “dot product in feature space” via a kernel function k(x, x′).

TL;DR:

A kernel k(x, x′) is a function that behaves like an inner product ⟨φ(x), φ(x′)⟩ in some feature space. If k is a valid (Mercer) kernel, then for any dataset the Gram matrix K with Kᵢⱼ = k(xᵢ, xⱼ) is positive semidefinite. Many algorithms (SVMs, ridge regression, PCA) can be rewritten to depend only on dot products, so swapping ⟨x, x′⟩ for k(x, x′) gives nonlinear models with the same machinery.

## What Is Kernel Methods?

### Why kernels exist at all (motivation)

Many ML algorithms are built from *similarity* computations. In linear models, the similarity is the dot product ⟨x, x′⟩. But linear similarity is limited: it can’t express “two points are similar if they match on a nonlinear pattern,” such as an XOR-like structure.

A common fix is **feature engineering**: hand-design a mapping

- •φ(x) = (features of x)

so the problem becomes linear in the new features. For example, you might add quadratic features x₁², x₁x₂, x₂².

The obstacle: φ(x) can explode in size.

- •With d input dimensions, all degree-2 monomials already cost O(d²).
- •With higher degrees, it grows combinatorially.
- •Some useful feature spaces are *infinite-dimensional* (e.g., certain radial basis function features).

Kernel methods solve this by focusing on what many algorithms actually need: **inner products** in feature space.

### The central definition

A **kernel function** is a function

- •k(x, x′)

that returns what *would have been* the inner product in a feature space:

- •k(x, x′) = ⟨φ(x), φ(x′)⟩

Here:

- •x, x′ are inputs in the original space (often ℝᵈ)
- •φ(x) is an (often implicit) mapping to a feature space ℋ
- •⟨·,·⟩ is an inner product in ℋ

If you can compute k(x, x′) directly, you can run algorithms that only depend on dot products without ever writing down φ(x).

This is the **kernel trick**:

- •Replace every ⟨x, x′⟩ with k(x, x′)
- •Obtain a model that is linear in φ(x) but nonlinear in x

### “Kernel methods” as a family

Kernel methods are not one algorithm; they’re a pattern:

1. 1)Start with an algorithm expressible using dot products.
2. 2)Rewrite it so it depends only on dot products between training points.
3. 3)Swap in a kernel k.

Canonical examples:

- •Support Vector Machines (you’ve seen kernels there)
- •Kernel Ridge Regression
- •Kernel PCA
- •Gaussian Processes (kernel/covariance functions)

### A geometric picture (intuition)

Think of φ(x) as moving x into a new space where linear separators are more powerful.

- •In input space, your data may not be separable by a hyperplane.
- •In feature space ℋ, the mapped points φ(x) might become separable.

But ℋ might be very large. Kernels let you compute angles and lengths in ℋ indirectly, because inner products determine geometry:

- •‖φ(x)‖² = ⟨φ(x), φ(x)⟩ = k(x, x)
- •Distance in feature space:

‖φ(x) − φ(x′)‖²

= ⟨φ(x) − φ(x′), φ(x) − φ(x′)⟩

= ⟨φ(x), φ(x)⟩ + ⟨φ(x′), φ(x′)⟩ − 2⟨φ(x), φ(x′)⟩

= k(x, x) + k(x′, x′) − 2k(x, x′)

So k doesn’t just give “similarity”; it defines a full geometry.

### Two crucial caveats (breathing room)

1) **Not every similarity function is a kernel.**

A function that “feels like similarity” might not correspond to an inner product in any Hilbert space.

2) **Validity matters because algorithms assume inner-product structure.**

If k is not valid, the math behind convexity, distances, projections, and optimization can break.

That brings us to the Mercer / positive-semidefinite condition.

## Core Mechanic 1: The Kernel Trick and Implicit Feature Spaces

### Why the kernel trick works

A lot of learning algorithms produce predictors of the form

- •f(x) = **w** · φ(x)

where **w** is a weight vector in feature space. The trick is that **w** often ends up being a combination of training feature vectors:

- •**w** = ∑ᵢ αᵢ φ(xᵢ)

This is not magic—it’s a consequence of optimization in a space spanned by training points (you may know this from SVM duality). Plugging that into f(x):

f(x)

= **w** · φ(x)

= (∑ᵢ αᵢ φ(xᵢ)) · φ(x)

= ∑ᵢ αᵢ ⟨φ(xᵢ), φ(x)⟩

= ∑ᵢ αᵢ k(xᵢ, x)

So the predictor depends only on kernel evaluations between x and training points.

### A concrete example: polynomial features without writing them

Take x ∈ ℝ²: x = (x₁, x₂).

Consider degree-2 polynomial features (including cross terms). One possible mapping is:

- •φ(x) = (x₁², √2 x₁x₂, x₂²)

Then the feature-space dot product is:

⟨φ(x), φ(x′)⟩

= x₁² x′₁² + 2 x₁x₂ x′₁x′₂ + x₂² x′₂²

= (x₁x′₁ + x₂x′₂)²

= (⟨x, x′⟩)²

So the kernel

- •k(x, x′) = (⟨x, x′⟩)²

computes an inner product in a 3D feature space—without explicitly building 3 features.

In d dimensions, the degree-2 feature space has O(d²) dimensions, but the kernel evaluation is still O(d).

More generally, the degree-p polynomial kernel

- •k(x, x′) = (⟨x, x′⟩ + c)ᵖ

corresponds to all monomials up to degree p (depending on c), with a particular scaling.

### The “implicit” part matters

When you use an RBF (Gaussian) kernel,

- •k(x, x′) = exp(−‖x − x′‖² / (2σ²))

the corresponding feature space is infinite-dimensional (for typical domains). Yet k(x, x′) is cheap to compute.

This is the deep promise of kernel methods:

- •you get “linear model power” in a huge space
- •while paying only for kernel evaluations

### Kernelized algorithms tend to look the same

After kernelization, the model typically takes the form:

- •f(x) = ∑ᵢ αᵢ k(xᵢ, x) + b

Interpretation:

- •each training point xᵢ acts like a “basis function center”
- •αᵢ is its learned weight
- •k(xᵢ, x) measures how much x resembles xᵢ under the kernel geometry

This is why kernel methods can be seen as flexible, data-adaptive similarity-based models.

### Computation trade-off (important pacing point)

Kernels avoid explicit high-dimensional φ(x), but they often replace it with dependence on the number of training points n.

Two regimes:

| Approach | Cost driver | Typical form |
| --- | --- | --- |
| Explicit features + linear model | feature dimension D | compute φ(x) then dot products |
| Kernel method | number of samples n | compute/store Gram matrix K (n×n) |

If n is large (e.g., millions), classic kernel methods can become expensive due to O(n²) memory/time for the Gram matrix.

So kernel methods are powerful, but they come with a scaling story you must understand.

### Kernel distance and similarity are not the same as Euclidean distance

Because kernels define geometry in feature space, they may treat two points as “close” even when they are far in Euclidean space (and vice versa). This is a feature, not a bug.

Using the identity:

‖φ(x) − φ(x′)‖² = k(x, x) + k(x′, x′) − 2k(x, x′)

you can see that for normalized kernels with k(x, x)=1, distance is controlled entirely by k(x,x′).

This is one reason the RBF kernel is popular: it makes similarity decay smoothly with Euclidean distance.

But again: only if k is a valid kernel does this correspond to a true squared distance in some inner-product space.

## Core Mechanic 2: Valid Kernels and Positive Semidefinite Gram Matrices (Mercer Condition)

### Why “kernel validity” is the gatekeeper

If k(x, x′) really equals ⟨φ(x), φ(x′)⟩ for some φ, then it inherits a key property of inner products: **positive semidefiniteness**.

This isn’t a technicality. Many guarantees in kernelized optimization (convexity, existence of solutions, geometric interpretations) rely on it.

### The Gram matrix viewpoint

Given data points x₁, …, xₙ, define the **Gram matrix** K ∈ ℝⁿˣⁿ by

- •Kᵢⱼ = k(xᵢ, xⱼ)

If k is an inner product in some feature space, then K must be **positive semidefinite (PSD)**:

- •∀ **c** ∈ ℝⁿ, **c**ᵀ K **c** ≥ 0

Why? Because K can be written as ΦΦᵀ if you stack feature vectors.

Let Φ be the matrix whose rows are φ(xᵢ)ᵀ (so Φ ∈ ℝⁿˣᴰ if the feature dimension is D, possibly infinite but conceptually similar). Then:

Kᵢⱼ = ⟨φ(xᵢ), φ(xⱼ)⟩

So

K = Φ Φᵀ

Now compute **c**ᵀK**c**:

**c**ᵀ K **c**

= **c**ᵀ (Φ Φᵀ) **c**

= (Φᵀ **c**)ᵀ (Φᵀ **c**)

= ‖Φᵀ **c**‖²

≥ 0

This derivation is the heart of PSD.

### Mercer condition (practical statement)

In many ML texts, a (symmetric) function k is called a **valid kernel** if for any finite set of points, the Gram matrix K is PSD.

So to check validity:

1) Symmetry: k(x, x′) = k(x′, x)

2) PSD Gram matrices: K ⪰ 0 for all datasets

In functional analysis, “Mercer’s theorem” gives conditions under which continuous kernels correspond to expansions in eigenfunctions, but for practical ML the PSD Gram condition is the usable criterion.

### What PSD implies (interpretations that help you reason)

If K is PSD, then:

- •all eigenvalues of K are ≥ 0
- •quadratic forms are nonnegative
- •you can interpret k as an inner product in a Hilbert space

This means algorithms like SVM dual optimization remain convex, because the Hessian-like pieces built from K behave well.

### Closure properties: how to build new kernels safely

Rather than proving PSD from scratch each time, use known closure rules. If k₁ and k₂ are valid kernels, then so are:

| Construction | New kernel |
| --- | --- |
| Nonnegative scaling | a k₁, for a ≥ 0 |
| Sum | k₁ + k₂ |
| Product | k₁ k₂ |
| Feature concatenation | k(x,x′)=⟨[φ₁(x);φ₂(x)], [φ₁(x′);φ₂(x′)]⟩ = k₁+k₂ |
| Kernel over transformed inputs | k(x,x′)=k₁(g(x), g(x′)) |
| Exponential of PSD with care | exp(k₁) is not always valid, but exp(−γ‖x−x′‖²) is |

A particularly important family:

- •Linear kernel: k(x,x′)=⟨x,x′⟩
- •Polynomial: (⟨x,x′⟩+c)ᵖ
- •RBF/Gaussian: exp(−‖x−x′‖²/(2σ²))
- •Laplacian: exp(−‖x−x′‖₁/σ)

### Centering in feature space (subtle but useful)

Some algorithms (e.g., kernel PCA) require centered features: mean(φ(xᵢ)) = 0.

But you never have φ explicitly.

You can still center via K.

Let **1** be the all-ones vector in ℝⁿ and H = I − (1/n)**1****1**ᵀ.

Then the centered Gram matrix is:

- •K\_c = H K H

This corresponds to computing inner products after subtracting the feature-space mean.

### When things go wrong: “indefinite kernels”

Sometimes practitioners use similarity functions that are not PSD. Then K has negative eigenvalues.

Consequences can include:

- •non-convex optimization in SVM-like objectives
- •distances ‖φ(x)−φ(x′)‖² becoming negative (not meaningful)

There are heuristics (eigenvalue clipping, shifting the spectrum), but conceptually you’ve left the safe “inner product” world.

### Key checkpoint

A kernel method is not merely “use a fancy similarity.”

It is: **choose k so that there exists φ with k(x,x′)=⟨φ(x),φ(x′)⟩**.

PSD Gram matrices are the operational test that you’re still doing geometry in some feature space.

## Application/Connection: Kernelized Learning Algorithms in Practice

### Why kernels appear across ML

Once you accept “replace dot products with kernels,” you start seeing the same template in multiple algorithms.

The payoff: you can reuse linear-algebraic learning ideas in nonlinear form.

Below are a few core examples and how they connect back to k and φ.

---

## 1) Kernel Ridge Regression (KRR)

### Why it matters

Linear regression can underfit nonlinear patterns. Polynomial features help, but can be huge. KRR gives you nonlinear regression with a clean closed form.

### Primal (feature space) view

In feature space, ridge regression solves:

minimize over **w**: ∑ᵢ (yᵢ − **w**·φ(xᵢ))² + λ‖**w**‖²

The solution lives in span{φ(xᵢ)}, so write **w** = ∑ⱼ αⱼ φ(xⱼ).

Predictor:

f(x) = ∑ⱼ αⱼ k(xⱼ, x)

### Dual / kernel form

Let K be the Gram matrix. Then the coefficients satisfy:

- •**α** = (K + λ I)⁻¹ **y**

So training reduces to solving a linear system in ℝⁿ.

Trade-off:

- •Pros: simple, convex, closed-form
- •Cons: O(n³) naive solve, O(n²) storage for K

---

## 2) Kernel PCA

### Why it matters

PCA finds directions of maximum variance—but only linear structure in input space.

Kernel PCA finds principal components in feature space, revealing nonlinear manifolds.

Key idea:

- •PCA can be written using dot products between centered data.
- •Replace dot products with centered kernel values.

Operationally:

1) Build K (n×n)

2) Center it: K\_c = H K H

3) Eigen-decompose K\_c

The resulting eigenvectors give coordinates of points along nonlinear components in ℋ.

---

## 3) SVM (connection you already know)

SVM dual depends on dot products between inputs. The kernelized decision function is:

f(x) = ∑ᵢ αᵢ yᵢ k(xᵢ, x) + b

Only support vectors have αᵢ ≠ 0.

Kernel validity (PSD) ensures the dual is a convex quadratic program.

---

## 4) Gaussian Processes (GPs) as “kernel methods with uncertainty”

GPs use a kernel as a covariance function:

- •cov(f(x), f(x′)) = k(x, x′)

PSD is required because covariance matrices must be PSD.

This is the same Gram-matrix condition from Mercer, now interpreted probabilistically.

---

## Choosing a kernel: a practical guide

Kernel choice encodes assumptions about smoothness and similarity.

| Kernel | k(x,x′) | Inductive bias | Key hyperparameters |
| --- | --- | --- | --- |
| Linear | ⟨x,x′⟩ | linear functions | none (maybe regularization) |
| Polynomial | (⟨x,x′⟩+c)ᵖ | global interactions up to degree p | p, c |
| RBF/Gaussian | exp(−‖x−x′‖²/(2σ²)) | smooth, local similarity | σ (or γ=1/(2σ²)) |
| Laplacian | exp(−‖x−x′‖₁/σ) | less smooth than RBF, robust | σ |

Practical pacing note: kernel methods can be *very* sensitive to scaling.

- •For RBF, feature scaling changes ‖x−x′‖² and thus similarity.
- •Standardization (zero mean, unit variance per feature) is often essential.

---

## Scaling and approximation (when n is big)

Classic kernel methods often require O(n²) kernel evaluations.

When n is large, you’ll see approximations:

- •Nyström approximation (approximate K using a subset of columns)
- •Random Fourier Features (approximate RBF kernels with explicit randomized φ̂(x))
- •Sparse Gaussian Processes (inducing points)

These methods keep the “kernel idea” but reduce compute.

---

## A unifying mental model

A kernel method typically learns a function inside a hypothesis class tied to k.

In many settings:

- •smoother kernels ⇒ smoother functions
- •more local kernels ⇒ more local influence of points
- •larger feature spaces ⇒ more expressive models, but higher risk of overfitting (controlled by regularization)

So kernel methods are best understood as a three-way trade:

1) kernel choice (geometry / similarity)

2) regularization strength

3) computational budget (n×n kernels vs approximations)

Keep returning to the core identity:

- •k(x, x′) = ⟨φ(x), φ(x′)⟩

It’s the bridge connecting geometry, optimization, and computation.

## Worked Examples (3)

### Example 1: Verify a Gram Matrix is PSD and interpret it as inner products

Let x₁ = (1, 0), x₂ = (0, 1), x₃ = (1, 1) in ℝ². Use the polynomial kernel k(x, x′) = (⟨x, x′⟩)². Compute the Gram matrix K and show it is PSD by checking eigenvalues or a PSD criterion.

1. Compute pairwise dot products:

   ⟨x₁,x₁⟩=1, ⟨x₁,x₂⟩=0, ⟨x₁,x₃⟩=1

   ⟨x₂,x₂⟩=1, ⟨x₂,x₃⟩=1

   ⟨x₃,x₃⟩=2
2. Apply k(x,x′)=(⟨x,x′⟩)²:

   k(x₁,x₁)=1²=1

   k(x₁,x₂)=0²=0

   k(x₁,x₃)=1²=1

   k(x₂,x₂)=1²=1

   k(x₂,x₃)=1²=1

   k(x₃,x₃)=2²=4
3. Form the Gram matrix (rows/cols correspond to x₁,x₂,x₃):

   K = [

   [1, 0, 1],

   [0, 1, 1],

   [1, 1, 4]

   ]
4. Check PSD by computing principal minors (sufficient for 3×3 symmetric matrices):

   Top-left 1×1 minor: 1 ≥ 0

   Top-left 2×2 minor: det([[1,0],[0,1]]) = 1 ≥ 0

   Full determinant:

   det(K)

   = 1·det([[1,1],[1,4]]) − 0 + 1·det([[0,1],[1,1]])·(−1)^{1+3}

   = 1·(1·4−1·1) + 1·(+1)·det([[0,1],[1,1]])

   = (4−1) + det([[0,1],[1,1]])

   = 3 + (0·1 − 1·1)

   = 3 − 1

   = 2 ≥ 0
5. Since all leading principal minors are nonnegative and K is symmetric, K is PSD (indeed positive definite here).

**Insight:** You never wrote φ(x), but K behaves exactly like inner products between feature vectors. PSD of K is the operational fingerprint that k is acting like ⟨φ(x),φ(x′)⟩ on this dataset.

### Example 2: Kernel Ridge Regression prediction via kernels only

Suppose you have two training points x₁=0, x₂=1 (in ℝ¹) with targets y₁=0, y₂=1. Use an RBF kernel k(x,x′)=exp(−(x−x′)²/(2σ²)) with σ=1 and ridge λ=0.1. Compute α = (K+λI)⁻¹ y and predict f(0.5).

1. Compute kernel values:

   k(0,0)=exp(0)=1

   k(1,1)=1

   k(0,1)=exp(−(1)²/2)=exp(−1/2)

   Let r = exp(−1/2). Numerically r ≈ 0.60653.
2. Form Gram matrix:

   K = [[1, r],

   [r, 1]]
3. Add λI:

   K+λI = [[1+0.1, r],

   [r, 1+0.1]]

   = [[1.1, r],[r,1.1]]
4. Invert the 2×2 matrix. For A=[[a,b],[b,a]], A⁻¹ = (1/(a²−b²))[[a,−b],[−b,a]].

   Here a=1.1, b=r.

   So (K+λI)⁻¹ = (1/(1.1²−r²)) [[1.1, −r], [−r, 1.1]].
5. Multiply by y=[0,1]ᵀ:

   **α** = (K+λI)⁻¹ **y**

   = (1/(1.21−r²)) [ (1.1·0 + (−r)·1), ((−r)·0 + 1.1·1) ]ᵀ

   = (1/(1.21−r²)) [ −r, 1.1 ]ᵀ
6. Compute denominator: r² ≈ (0.60653)² ≈ 0.36788

   So 1.21 − r² ≈ 1.21 − 0.36788 = 0.84212
7. Thus α₁ ≈ −0.60653 / 0.84212 ≈ −0.7203

   and α₂ ≈ 1.1 / 0.84212 ≈ 1.3061
8. Predict at x=0.5:

   f(0.5) = α₁ k(0,0.5) + α₂ k(1,0.5)

   Compute k(0,0.5)=exp(−0.5²/2)=exp(−0.125) ≈ 0.88250

   Compute k(1,0.5)=exp(−0.5²/2)=same ≈ 0.88250
9. So f(0.5) ≈ (−0.7203)(0.8825) + (1.3061)(0.8825)

   = (0.5858)(0.8825)

   ≈ 0.517

**Insight:** KRR learns coefficients on training points, not on explicit features. The prediction is a weighted sum of similarities to training points, with smoothness controlled by σ and overfitting controlled by λ.

### Example 3: Compute feature-space distance using only a kernel

Let k be the RBF kernel k(x,x′)=exp(−‖x−x′‖²/(2σ²)) with σ=2. For x=(0,0) and x′=(2,0), compute ‖φ(x)−φ(x′)‖² using only k.

1. Use the identity:

   ‖φ(x)−φ(x′)‖² = k(x,x) + k(x′,x′) − 2k(x,x′).
2. Compute k(x,x)=exp(0)=1 and k(x′,x′)=1.
3. Compute ‖x−x′‖² = ‖(−2,0)‖² = 4.
4. Compute k(x,x′)=exp(−4/(2·2²))=exp(−4/8)=exp(−0.5)≈0.60653.
5. Thus:

   ‖φ(x)−φ(x′)‖² = 1 + 1 − 2(0.60653)

   = 2 − 1.21306

   ≈ 0.78694

**Insight:** Even though φ is infinite-dimensional for the RBF kernel, distances in that space are easy to compute. Kernel values define the geometry.

## Key Takeaways

- ✓

  A kernel function k(x,x′) is an inner-product evaluator: k(x,x′)=⟨φ(x),φ(x′)⟩ for some (possibly infinite-dimensional) feature map φ.
- ✓

  The kernel trick works because many algorithms can be rewritten to depend only on dot products between examples; replace dot products with k(x,x′).
- ✓

  Kernelized predictors often have the form f(x)=∑ᵢ αᵢ k(xᵢ,x)+b, a weighted similarity to training points.
- ✓

  Kernel validity is not optional: a valid kernel produces PSD Gram matrices K for any dataset, guaranteeing consistent inner-product geometry.
- ✓

  PSD means ∀ **c**, **c**ᵀK**c**≥0, equivalently K has no negative eigenvalues; this underpins convexity in SVM/KRR and validity as covariance in GPs.
- ✓

  You can compute norms and distances in feature space using only k, e.g., ‖φ(x)−φ(x′)‖² = k(x,x)+k(x′,x′)−2k(x,x′).
- ✓

  Kernel choice encodes inductive bias (smoothness, locality, interactions) and must be paired with regularization and good input scaling.
- ✓

  Kernel methods trade explicit high-dimensional features for n×n Gram-matrix computation; approximations exist when n is large.

## Common Mistakes

- ✗

  Treating any similarity score as a kernel: if the Gram matrix is not PSD, you may break convexity/geometry assumptions.
- ✗

  Forgetting to scale/standardize inputs before using distance-based kernels (RBF/Laplacian), leading to meaningless similarities.
- ✗

  Confusing feature-space linearity with input-space linearity: kernel methods are linear in φ(x) but generally nonlinear in x.
- ✗

  Ignoring computational scaling: storing K is O(n²) and naive training can be O(n³), which can be infeasible for large n.

## Practice

easy

Given points x₁=(1,2), x₂=(2,1) in ℝ² and the kernel k(x,x′)=(⟨x,x′⟩)², compute the 2×2 Gram matrix K and verify it is PSD.

**Hint:** Compute ⟨x₁,x₁⟩, ⟨x₁,x₂⟩, ⟨x₂,x₂⟩, then square them. For a 2×2 symmetric matrix [[a,b],[b,c]], PSD iff a≥0, c≥0, and ac−b²≥0.

Show solution

Dot products:

⟨x₁,x₁⟩=1²+2²=5

⟨x₂,x₂⟩=2²+1²=5

⟨x₁,x₂⟩=1·2+2·1=4

Kernel values:

k(x₁,x₁)=25, k(x₂,x₂)=25, k(x₁,x₂)=16

So K=[[25,16],[16,25]].

Check PSD:

Determinant = 25·25 − 16² = 625 − 256 = 369 ≥ 0 and diagonal entries are positive, so K is PSD (indeed positive definite).

medium

Show that the function d²(x,x′)=k(x,x)+k(x′,x′)−2k(x,x′) equals ‖φ(x)−φ(x′)‖² whenever k(x,x′)=⟨φ(x),φ(x′)⟩. Then compute d² for the linear kernel k(x,x′)=⟨x,x′⟩ and interpret the result.

**Hint:** Expand ‖φ(x)−φ(x′)‖² using bilinearity of inner products. For the linear kernel, φ(x)=x.

Show solution

Derivation:

‖φ(x)−φ(x′)‖²

= ⟨φ(x)−φ(x′), φ(x)−φ(x′)⟩

= ⟨φ(x),φ(x)⟩ + ⟨φ(x′),φ(x′)⟩ − 2⟨φ(x),φ(x′)⟩

= k(x,x) + k(x′,x′) − 2k(x,x′)

So d²(x,x′)=‖φ(x)−φ(x′)‖².

For the linear kernel k(x,x′)=⟨x,x′⟩:

d²(x,x′)=⟨x,x⟩+⟨x′,x′⟩−2⟨x,x′⟩=‖x−x′‖².

Interpretation: with the linear kernel, feature space equals input space, so kernel distance is ordinary Euclidean squared distance.

hard

You are given a symmetric 3×3 matrix K as a candidate Gram matrix:

K = [[1, 2, 0],

[2, 1, 0],

[0, 0, 1]].

Is K PSD? What does your answer imply about whether it can come from a valid kernel on three points?

**Hint:** Check eigenvalues or a principal minor that becomes negative. The top-left 2×2 block already reveals something.

Show solution

Consider the top-left 2×2 block B=[[1,2],[2,1]].

Its determinant is det(B)=1·1−2²=1−4=−3 < 0, so B is not PSD.

A principal submatrix of a PSD matrix must be PSD; since B is not, K cannot be PSD.

Therefore K is indefinite (has at least one negative eigenvalue). Implication: K cannot be a Gram matrix Kᵢⱼ=⟨φ(xᵢ),φ(xⱼ)⟩ for any feature map φ, so it cannot arise from a valid kernel evaluated on three points.

## Connections

- •[Support Vector Machines](/tech-tree/support-vector-machines/)
- •[Convex Optimization Basics](/tech-tree/convex-optimization-basics/)
- •[Ridge Regression](/tech-tree/ridge-regression/)
- •[Principal Component Analysis](/tech-tree/pca/)
- •[Gaussian Processes](/tech-tree/gaussian-processes/)
- •[Random Fourier Features](/tech-tree/random-fourier-features/)
- •[Nyström Method](/tech-tree/nystrom-method/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
