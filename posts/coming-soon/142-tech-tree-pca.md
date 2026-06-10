---
title: Principal Component Analysis
description: Dimensionality reduction via eigenvectors of covariance.
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
permalink: /tech-tree/pca/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Principal Component Analysis

Linear AlgebraDifficulty: ★★★★☆Depth: 8Unlocks: 1

Dimensionality reduction via eigenvectors of covariance.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Principal component = an orthogonal direction (axis) in feature space that maximizes the variance of data when projected onto it.
- -Eigen-decomposition of the data covariance matrix produces those orthogonal principal axes and associated variances.
- -Dimensionality reduction by projecting data onto the top-k principal components yields the best k-dimensional linear approximation in terms of captured variance.

## Key Symbols & Notation

v (principal component vector, an eigenvector of the covariance matrix)lambda (eigenvalue: the variance captured by its corresponding v)

## Essential Relationships

- -Covariance \* v = lambda \* v, so each eigenvector v is an orthogonal principal axis and its eigenvalue lambda equals the variance of data projected onto v; sorting lambda orders components by explained variance.

## Prerequisites (2)

[Singular Value Decomposition6 atoms](/tech-tree/svd/)[Covariance and Correlation6 atoms](/tech-tree/covariance-correlation/)

## Unlocks (1)

[Dimensionality Reductionlvl 4](/tech-tree/dimensionality-reduction/)

Advanced Learning Details

### Graph Position

164

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

8

Chain Length

### Cognitive Load

6

Atomic Elements

43

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (19)

- - Principal component: a direction (unit vector) in feature space onto which data is projected to form a new variable
- - Principal axes / principal directions: the ordered set of eigenvectors of the data covariance that define the new coordinate system
- - Principal component score (or score): the coordinate of a data point along a principal component (projection value)
- - Loadings: the coefficients (elements of an eigenvector) that define a principal component as a linear combination of original variables
- - Explained variance: the variance of the data along a principal component (numerical measure of its importance)
- - Explained variance ratio: the fraction of total variance accounted for by a particular principal component (λ\_i / Σ\_j λ\_j)
- - Ordering of components: principal components are sorted by descending explained variance (eigenvalues)
- - Dimensionality reduction by truncation: approximating data by retaining only the top-k principal components
- - Reconstruction from components: reconstructing an approximation of the original data from retained scores and loadings
- - Mean-centering: subtracting the variable-wise mean from data before applying PCA (required for covariance-based PCA)
- - Eigendecomposition of covariance: representing the covariance matrix as P Λ P^T where columns of P are eigenvectors and Λ is diagonal of eigenvalues
- - Orthogonality of components: principal components (eigenvectors) are mutually orthogonal and form an orthonormal basis
- - Uncorrelatedness of component scores: projections onto different principal components have zero covariance
- - Variance-maximization formulation: each principal component is the direction that maximizes projected variance subject to orthogonality constraints to previous components
- - Least-squares / reconstruction-optimality: choosing the top-k eigenvectors minimizes squared reconstruction error among all k-dimensional linear subspaces
- - Total variance equals sum of eigenvalues: global variance of the dataset equals trace of covariance matrix (Σ\_i λ\_i)
- - Scree plot / cumulative explained variance: graphical/aggregate criteria to choose number k (visualizing λ\_i or Σ\_{i<=k} λ\_i / Σ\_j λ\_j)
- - Whitening (optional PCA variant): scaling projected components by 1/sqrt(λ\_i) to produce uncorrelated unit-variance features
- - Principal components are linear combinations of original variables (interpretability via loadings)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

You have a dataset with 200 features. You suspect only a few underlying “directions” actually matter (e.g., lighting vs pose in images, or overall size vs shape in tabular data). PCA is the classic tool for discovering those directions—purely from geometry—and then compressing the data while losing as little information as possible (in a precise sense).

TL;DR:

Principal Component Analysis (PCA) finds orthogonal directions **v**₁, **v**₂, … (eigenvectors of the data covariance) that capture maximum variance. Projecting onto the top-k components gives the best k-dimensional linear approximation: it maximizes captured variance and equivalently minimizes squared reconstruction error. PCA can be computed via covariance eigen-decomposition or via SVD of the centered data matrix.

## What Is Principal Component Analysis?

PCA is a **linear dimensionality reduction** method. It replaces your original coordinate system (your original features) with a new coordinate system whose axes are:

- •**Orthogonal** (perpendicular) directions in feature space
- •Ordered by how much **variance** of the data they capture when you project onto them

Those axes are called **principal components**.

### The geometric picture

Imagine your data points as a cloud in ℝᵈ (d features). If that cloud is stretched out more in one direction than others, there’s a “long axis” through the cloud. Projecting onto that axis preserves a lot of the spread (variance) of the data. PCA finds that axis, then the next-most-informative orthogonal axis, and so on.

### Conventions (define them early)

We’ll set up notation carefully so you don’t have to guess later.

- •Data matrix: X∈Rn×dX \in \mathbb{R}^{n \times d}X∈Rn×d with rows xiT\mathbf{x}\_i^TxiT​ (each xi∈Rd\mathbf{x}\_i \in \mathbb{R}^dxi​∈Rd is one sample).
- •Sample mean:

μ=1n∑i=1nxi\boldsymbol{\mu} = \frac{1}{n}\sum\_{i=1}^n \mathbf{x}\_iμ=n1​i=1∑n​xi​

- •Centered data matrix:

Xc=X−1μTX\_c = X - \mathbf{1}\boldsymbol{\mu}^TXc​=X−1μT

where 1∈Rn\mathbf{1} \in \mathbb{R}^{n}1∈Rn is the all-ones column vector.

- •Covariance matrix. Two common conventions:
- •Population-style: Σ=1nXcTXc\Sigma = \frac{1}{n} X\_c^T X\_cΣ=n1​XcT​Xc​
- •Unbiased sample-style: Σ=1n−1XcTXc\Sigma = \frac{1}{n-1} X\_c^T X\_cΣ=n−11​XcT​Xc​

For PCA, **the eigenvectors are the same under both** (they differ only by a scalar factor in eigenvalues). In this lesson, we’ll mostly use

Σ=1nXcTXc\Sigma = \frac{1}{n} X\_c^T X\_cΣ=n1​XcT​Xc​

to keep algebra clean.

### What PCA outputs

PCA produces:

- •Principal component directions: **v**₁, …, **v**ᵈ (unit vectors in ℝᵈ), collected in a matrix V=[v1 ⋯ vd]V = [\mathbf{v}\_1\ \cdots\ \mathbf{v}\_d]V=[v1​ ⋯ vd​].
- •Corresponding eigenvalues: λ1≥λ2≥⋯≥λd≥0\lambda\_1 \ge \lambda\_2 \ge \cdots \ge \lambda\_d \ge 0λ1​≥λ2​≥⋯≥λd​≥0.

Interpretation:

- •**v**ⱼ is a direction (axis) in feature space.
- •λj\lambda\_jλj​ is the variance of the data when projected onto **v**ⱼ.

### Two equivalent “best” statements

When you keep only the top-k components, PCA gives the best k-dimensional linear approximation in two equivalent ways:

1) **Maximum captured variance** among all k-dimensional subspaces.

2) **Minimum squared reconstruction error** among all rank-k linear projections.

We’ll prove both—but slowly, with checkpoints.

---

#### Checkpoint summary

- •PCA is a change of basis to orthogonal directions ordered by variance.
- •Compute PCA from the covariance eigenvectors (or from SVD).
- •Keeping top-k components gives an optimal k-dimensional linear representation.

#### Micro-exercise (30 seconds)

If you scale your covariance by 1/(n−1) instead of 1/n, what changes?

Answer: eigenvectors (principal directions) do not change; eigenvalues scale by nn−1\frac{n}{n-1}n−1n​.

## Core Mechanic 1: The First Principal Component as a Variance Maximizer (Rayleigh Quotient → Eigenvector)

PCA starts with a very specific optimization question:

> Among all unit directions **v** in feature space, which direction makes the projected data have the largest variance?

That direction will be **v**₁, the first principal component.

### Step 1: Define projection and projected variance

Take a unit vector **v** ∈ ℝᵈ with ∥v∥2=1\|\mathbf{v}\|\_2 = 1∥v∥2​=1.

Project a centered data point x\mathbf{x}x onto **v**:

- •Scalar coordinate along **v**: z=vTxz = \mathbf{v}^T \mathbf{x}z=vTx.

For a random centered vector **x** (think of drawing a row from XcX\_cXc​), the variance of zzz is:

Var(z)=Var(vTx).\mathrm{Var}(z) = \mathrm{Var}(\mathbf{v}^T \mathbf{x}).Var(z)=Var(vTx).

Using Cov(x)=Σ\mathrm{Cov}(\mathbf{x}) = \SigmaCov(x)=Σ and standard covariance rules:

Var(vTx)=vTΣv.\mathrm{Var}(\mathbf{v}^T \mathbf{x}) = \mathbf{v}^T \Sigma \mathbf{v}.Var(vTx)=vTΣv.

So we want to maximize vTΣv\mathbf{v}^T \Sigma \mathbf{v}vTΣv subject to ∥v∥2=1\|\mathbf{v}\|\_2 = 1∥v∥2​=1.

### Step 2: The optimization problem

max⁡v∈Rd vTΣvs.t.vTv=1.\max\_{\mathbf{v} \in \mathbb{R}^d} \ \mathbf{v}^T \Sigma \mathbf{v} \quad \text{s.t.} \quad \mathbf{v}^T \mathbf{v} = 1.v∈Rdmax​ vTΣvs.t.vTv=1.

The expression

R(v)=vTΣvvTvR(\mathbf{v}) = \frac{\mathbf{v}^T \Sigma \mathbf{v}}{\mathbf{v}^T \mathbf{v}}R(v)=vTvvTΣv​

is the **Rayleigh quotient**. Under the unit-norm constraint, maximizing vTΣv\mathbf{v}^T\Sigma\mathbf{v}vTΣv is the same as maximizing R(v)R(\mathbf{v})R(v).

### Step 3: Solve with Lagrange multipliers (show work)

Set up the Lagrangian:

L(v,α)=vTΣv−α(vTv−1).\mathcal{L}(\mathbf{v},\alpha) = \mathbf{v}^T \Sigma \mathbf{v} - \alpha(\mathbf{v}^T\mathbf{v} - 1).L(v,α)=vTΣv−α(vTv−1).

Differentiate w.r.t. **v** and set to zero:

1) Gradient of quadratic form: ∇v(vTΣv)=2Σv\nabla\_{\mathbf{v}} (\mathbf{v}^T \Sigma \mathbf{v}) = 2\Sigma\mathbf{v}∇v​(vTΣv)=2Σv (since Σ\SigmaΣ is symmetric)

2) Gradient of constraint term: ∇v(vTv)=2v\nabla\_{\mathbf{v}} (\mathbf{v}^T\mathbf{v}) = 2\mathbf{v}∇v​(vTv)=2v

So:

∇vL=2Σv−2αv=0\nabla\_{\mathbf{v}}\mathcal{L} = 2\Sigma\mathbf{v} - 2\alpha\mathbf{v} = 0∇v​L=2Σv−2αv=0

Divide by 2:

Σv=αv.\Sigma\mathbf{v} = \alpha\mathbf{v}.Σv=αv.

That is exactly the **eigenvector equation**.

So any optimum must be an eigenvector of Σ\SigmaΣ.

To see which eigenvector gives the maximum, plug an eigenvector **v** with eigenvalue λ\lambdaλ into the objective:

vTΣv=vT(λv)=λvTv=λ.\mathbf{v}^T \Sigma \mathbf{v} = \mathbf{v}^T (\lambda \mathbf{v}) = \lambda \mathbf{v}^T \mathbf{v} = \lambda.vTΣv=vT(λv)=λvTv=λ.

Under the unit constraint, the value equals its eigenvalue. Therefore, the maximum is attained by the eigenvector with the **largest eigenvalue**.

So:

- •**v**₁ = eigenvector of Σ\SigmaΣ with largest eigenvalue λ1\lambda\_1λ1​
- •Captured variance along **v**₁ is λ1\lambda\_1λ1​

### Step 4: The next components (orthogonality emerges)

After choosing **v**₁, we want **v**₂ to maximize variance **subject to being orthogonal** to **v**₁:

max⁡∥v∥=1, v⊥v1vTΣv.\max\_{\|\mathbf{v}\|=1,\ \mathbf{v} \perp \mathbf{v}\_1} \mathbf{v}^T\Sigma\mathbf{v}.∥v∥=1, v⊥v1​max​vTΣv.

The solution is the eigenvector with the next-largest eigenvalue, and so on. Because Σ\SigmaΣ is symmetric positive semidefinite, it has an orthonormal eigenbasis, so the eigenvectors can be chosen orthogonal.

---

#### Checkpoint summary

- •Projected variance along **v** is vTΣv\mathbf{v}^T\Sigma\mathbf{v}vTΣv.
- •Maximizing this under ∥v∥=1\|\mathbf{v}\|=1∥v∥=1 gives an eigenvector problem.
- •The best direction is the eigenvector with largest eigenvalue.

#### Micro-exercise (1 minute)

Let Σ=[2001]\Sigma = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}Σ=[20​01​]. Which unit vector maximizes vTΣv\mathbf{v}^T\Sigma\mathbf{v}vTΣv?

Solution sketch: eigenvalues are 2 and 1 with eigenvectors [1,0]ᵀ and [0,1]ᵀ. Max is along [1,0]ᵀ with value 2.

## Core Mechanic 2: From One Direction to k Dimensions + Variance ↔ Reconstruction Error

Finding **v**₁ is only the beginning. PCA’s power comes from selecting a whole **k-dimensional subspace** that best represents the data.

There are two common ways to describe what “best” means:

1) **Keep as much variance as possible** (information-as-spread viewpoint)

2) **Reconstruct with minimal squared error** (compression viewpoint)

A key learning goal is to see why these are actually the same objective.

## Part A: Projecting onto the top-k components

Let Vk=[v1 ⋯ vk]∈Rd×kV\_k = [\mathbf{v}\_1\ \cdots\ \mathbf{v}\_k] \in \mathbb{R}^{d \times k}Vk​=[v1​ ⋯ vk​]∈Rd×k with orthonormal columns (VkTVk=IkV\_k^T V\_k = I\_kVkT​Vk​=Ik​).

Given a centered data point **x**, its coordinates in the PCA subspace are:

z=VkTx∈Rk.\mathbf{z} = V\_k^T \mathbf{x} \in \mathbb{R}^k.z=VkT​x∈Rk.

The projection back to ℝᵈ (the rank-k approximation of **x**) is:

x^=Vkz=VkVkTx.\hat{\mathbf{x}} = V\_k \mathbf{z} = V\_k V\_k^T \mathbf{x}.x^=Vk​z=Vk​VkT​x.

So the projection matrix is Pk=VkVkTP\_k = V\_k V\_k^TPk​=Vk​VkT​.

## Part B: Captured variance in k dimensions

The variance captured by projecting onto the k-dimensional subspace is the expected squared norm of the projected vector:

E[∥VkTx∥22].\mathbb{E}[\|V\_k^T \mathbf{x}\|\_2^2].E[∥VkT​x∥22​].

Compute it:

\[\begin{aligned}

\mathbb{E}[\|V\_k^T \mathbf{x}\|\_2^2]

&= \mathbb{E}[ (V\_k^T \mathbf{x})^T (V\_k^T \mathbf{x}) ] \\

&= \mathbb{E}[ \mathbf{x}^T V\_k V\_k^T \mathbf{x} ] \\

&= \mathrm{tr}(\mathbb{E}[ \mathbf{x}\mathbf{x}^T ] V\_k V\_k^T) \quad \text{(cyclic trace)} \\

&= \mathrm{tr}(\Sigma V\_k V\_k^T).

\end{aligned}\]

If VkV\_kVk​ is made of eigenvectors of Σ\SigmaΣ, then:

tr(ΣVkVkT)=∑j=1kλj.\mathrm{tr}(\Sigma V\_k V\_k^T) = \sum\_{j=1}^k \lambda\_j.tr(ΣVk​VkT​)=j=1∑k​λj​.

So the top-k PCA subspace captures variance equal to the sum of the top k eigenvalues.

### Explained variance ratio

A common diagnostic is:

ExplainedVarianceRatio(k)=∑j=1kλj∑j=1dλj.\text{ExplainedVarianceRatio}(k) = \frac{\sum\_{j=1}^k \lambda\_j}{\sum\_{j=1}^d \lambda\_j}.ExplainedVarianceRatio(k)=∑j=1d​λj​∑j=1k​λj​​.

This tells you what fraction of total variance you keep.

---

#### Checkpoint summary

- •The rank-k projection is x^=VkVkTx\hat{\mathbf{x}} = V\_k V\_k^T \mathbf{x}x^=Vk​VkT​x.
- •Variance captured by that subspace is ∑j=1kλj\sum\_{j=1}^k \lambda\_j∑j=1k​λj​.
- •Explained variance ratio guides k selection.

#### Micro-exercise (45 seconds)

If eigenvalues are [5, 2, 1, 1, 1], what k gives ≥80% explained variance?

Solution: total = 10. k=1 gives 50%, k=2 gives 70%, k=3 gives 80% → k=3.

## Part C: Reconstruction error and why PCA is optimal

Now we switch viewpoints: you want to **compress** data by keeping only k numbers per sample (the coordinates **z**) and then reconstruct.

For a point **x**, reconstruction error is:

∥x−x^∥22=∥x−VkVkTx∥22.\|\mathbf{x} - \hat{\mathbf{x}}\|\_2^2 = \|\mathbf{x} - V\_k V\_k^T \mathbf{x}\|\_2^2.∥x−x^∥22​=∥x−Vk​VkT​x∥22​.

Consider expected reconstruction error over the data distribution:

E[∥x−VkVkTx∥22].\mathbb{E}[\|\mathbf{x} - V\_k V\_k^T \mathbf{x}\|\_2^2].E[∥x−Vk​VkT​x∥22​].

### Key identity: energy splits into kept + lost

Because VkVkTV\_k V\_k^TVk​VkT​ is an orthogonal projector,

- •the kept component is x^\hat{\mathbf{x}}x^
- •the residual is r=x−x^\mathbf{r} = \mathbf{x} - \hat{\mathbf{x}}r=x−x^
- •and x^⊥r\hat{\mathbf{x}} \perp \mathbf{r}x^⊥r

So by Pythagoras:

∥x∥22=∥x^∥22+∥r∥22.\|\mathbf{x}\|\_2^2 = \|\hat{\mathbf{x}}\|\_2^2 + \|\mathbf{r}\|\_2^2.∥x∥22​=∥x^∥22​+∥r∥22​.

Rearrange:

∥r∥22=∥x∥22−∥x^∥22.\|\mathbf{r}\|\_2^2 = \|\mathbf{x}\|\_2^2 - \|\hat{\mathbf{x}}\|\_2^2.∥r∥22​=∥x∥22​−∥x^∥22​.

Take expectation:

\[\begin{aligned}

\mathbb{E}[\|\mathbf{x} - V\_k V\_k^T \mathbf{x}\|\_2^2]

&= \mathbb{E}[\|\mathbf{x}\|\_2^2] - \mathbb{E}[\|V\_k V\_k^T \mathbf{x}\|\_2^2] \\

&= \mathbb{E}[\|\mathbf{x}\|\_2^2] - \mathbb{E}[\|V\_k^T \mathbf{x}\|\_2^2].

\end{aligned}\]

The first term E[∥x∥22]\mathbb{E}[\|\mathbf{x}\|\_2^2]E[∥x∥22​] is constant with respect to the choice of subspace. So:

> Minimizing reconstruction error is equivalent to maximizing captured projected energy/variance.

So the same VkV\_kVk​ that maximizes E[∥VkTx∥2]\mathbb{E}[\|V\_k^T \mathbf{x}\|^2]E[∥VkT​x∥2] also minimizes reconstruction error.

### What is the minimum error value?

If you choose VkV\_kVk​ as top-k eigenvectors, the variance you *don’t* capture is the sum of remaining eigenvalues:

E[∥x−x^∥22]=∑j=k+1dλj.\mathbb{E}[\|\mathbf{x} - \hat{\mathbf{x}}\|\_2^2] = \sum\_{j=k+1}^d \lambda\_j.E[∥x−x^∥22​]=j=k+1∑d​λj​.

This gives a clean interpretation:

- •Eigenvalues are “energy per principal axis.”
- •Dropping axes j>k loses exactly that energy.

---

#### Checkpoint summary

- •Reconstruction error = total energy − captured energy.
- •PCA maximizes captured energy, therefore minimizes reconstruction error.
- •Minimum achievable expected squared error after keeping k comps is ∑j>kλj\sum\_{j>k} \lambda\_j∑j>k​λj​.

#### Micro-exercise (1 minute)

Eigenvalues are [10, 3, 2]. If you keep k=1, what is expected reconstruction error (in variance units)?

Solution: drop eigenvalues 3 and 2 → error = 5.

## Part D: Best rank-k approximation (matrix view)

So far we reasoned per-vector. PCA also gives the best **rank-k matrix approximation** of the centered data matrix XcX\_cXc​ in Frobenius norm.

Let XcX\_cXc​ have SVD:

Xc=UΣsVTX\_c = U\Sigma\_s V^TXc​=UΣs​VT

(where we’ll call the diagonal of singular values Σs\Sigma\_sΣs​ to avoid confusing it with covariance).

The Eckart–Young theorem says the best rank-k approximation is:

Xc,k=UkΣs,kVkT.X\_{c,k} = U\_k \Sigma\_{s,k} V\_k^T.Xc,k​=Uk​Σs,k​VkT​.

This is exactly what PCA is doing in matrix form.

Connecting to covariance:

\[\begin{aligned}

\frac{1}{n} X\_c^T X\_c

&= \frac{1}{n} (V \Sigma\_s U^T)(U \Sigma\_s V^T) \\

&= \frac{1}{n} V \Sigma\_s^2 V^T.

\end{aligned}\]

So:

- •The PCA eigenvectors are the right singular vectors VVV.
- •The PCA eigenvalues are λj=σj2n\lambda\_j = \frac{\sigma\_j^2}{n}λj​=nσj2​​ where σj\sigma\_jσj​ is singular value j.

That’s why PCA can be computed without explicitly forming the covariance matrix, especially when d is large.

---

#### Checkpoint summary

- •PCA is equivalent to truncated SVD of centered data.
- •Eigenvalues relate to singular values via λj=σj2/n\lambda\_j = \sigma\_j^2/nλj​=σj2​/n.
- •Best rank-k approximation in Frobenius norm matches the best k-dimensional subspace story.

## Application/Connection: How PCA Is Used (and How to Do It Correctly)

PCA is simple to state but easy to misuse in practice. This section focuses on how PCA is applied, what choices matter, and how it connects to the tools you already know.

## A practical PCA workflow

### Step 0: Decide the goal

Common goals:

- •Visualization (k=2 or 3)
- •Compression / speed-up downstream models
- •Denoising
- •Preprocessing for regression/classification (sometimes helps, sometimes hurts)

### Step 1: Preprocess (centering is non-negotiable)

PCA assumes the data is centered.

- •Compute mean μ\boldsymbol{\mu}μ over training set.
- •Subtract it from all training points.

If you forget this, the first component can point mostly toward the mean rather than describing variation.

### Step 2: Scaling / standardization (depends on units)

If features have different units/scales, covariance will be dominated by high-variance features.

| Choice | What you compute PCA on | When it’s appropriate | Effect |
| --- | --- | --- | --- |
| Covariance PCA | Centered XcX\_cXc​ | Features share comparable units/scales | Preserves natural variance magnitudes |
| Correlation PCA | Standardized data (z-scores) | Mixed units (e.g., dollars + seconds), different scales | Treats each feature as equally scaled |

Standardization: xij←(xij−μj)/sjx\_{ij} \leftarrow (x\_{ij} - \mu\_j)/s\_jxij​←(xij​−μj​)/sj​ where sjs\_jsj​ is std dev.

### Step 3: Compute PCA (covariance eigendecomp or SVD)

Two equivalent computation paths:

**Path A: Covariance eigen-decomposition** (good when d is modest):

1. 1)Σ=1nXcTXc\Sigma = \frac{1}{n} X\_c^T X\_cΣ=n1​XcT​Xc​
2. 2)Eigen-decompose: Σ=VΛVT\Sigma = V\Lambda V^TΣ=VΛVT

**Path B: SVD of centered data** (often better numerically and when d is large):

1. 1)Xc=UΣsVTX\_c = U\Sigma\_s V^TXc​=UΣs​VT
2. 2)Columns of VVV are principal directions, and eigenvalues are λj=σj2/n\lambda\_j = \sigma\_j^2/nλj​=σj2​/n.

### Step 4: Choose k

Typical heuristics:

- •Keep enough components for 90–99% explained variance
- •Scree plot “elbow”
- •Cross-validate downstream task performance

### Step 5: Transform and (optionally) reconstruct

Transform (encode):

Z=XcVk∈Rn×kZ = X\_c V\_k \in \mathbb{R}^{n \times k}Z=Xc​Vk​∈Rn×k

Reconstruct (decode):

X^=ZVkT+1μT\hat{X} = Z V\_k^T + \mathbf{1}\boldsymbol{\mu}^TX^=ZVkT​+1μT

(remember to add the mean back).

---

#### Checkpoint summary

- •Always center using training mean.
- •Consider standardization if feature scales differ.
- •Use SVD when d is large or for stability.

#### Micro-exercise (1 minute)

Why must you apply the *training* mean and scaling to the test set (not recompute them on test)?

Solution: recomputing uses test information (data leakage) and changes the coordinate system; transformed features wouldn’t be comparable.

## PCA as “rotation + truncation”

When VVV is orthonormal, multiplying by VVV is a rotation/reflection (distance-preserving). PCA can be thought of as:

1) Rotate into the eigenvector basis: y=VTx\mathbf{y} = V^T \mathbf{x}y=VTx

2) Drop the last d−k coordinates (small-variance directions)

This makes clear why PCA often denoises: if noise is roughly isotropic, it spreads across many directions and tends to be captured by small eigenvalues.

## Whitening (optional but common)

Sometimes you want the transformed variables to have unit variance and be uncorrelated. PCA already makes them uncorrelated; whitening also rescales.

Let Λk\Lambda\_kΛk​ be diagonal with top-k eigenvalues. PCA coordinates are:

z=VkTx.\mathbf{z} = V\_k^T \mathbf{x}.z=VkT​x.

Whitened coordinates:

zwhite=Λk−1/2VkTx.\mathbf{z}\_{\text{white}} = \Lambda\_k^{-1/2} V\_k^T \mathbf{x}.zwhite​=Λk−1/2​VkT​x.

Caution: whitening can amplify noise in low-variance directions (because you divide by small λ\lambdaλ).

## Connections to SVD (tying back to prerequisite)

Since you already know SVD, here’s the clean link you can reuse:

- •Compute SVD: Xc=UΣsVTX\_c = U\Sigma\_s V^TXc​=UΣs​VT
- •Principal components are columns of VVV
- •Scores (projected coordinates) are Z=XcVk=UkΣs,kZ = X\_c V\_k = U\_k\Sigma\_{s,k}Z=Xc​Vk​=Uk​Σs,k​

This last identity is handy: you can get the k-dimensional representation directly as UkΣs,kU\_k\Sigma\_{s,k}Uk​Σs,k​ without forming VkV\_kVk​ explicitly in some streaming/large-scale settings.

## When PCA is not the right tool

PCA is linear. It fails when structure is nonlinear.

- •A “Swiss roll” manifold in 3D is not well represented by a plane.
- •Clusters separated nonlinearly might need kernel PCA, t-SNE/UMAP for visualization, or autoencoders for nonlinear compression.

Still, PCA is often the baseline: fast, interpretable, and a strong first step.

---

#### Final checkpoint summary

- •PCA is optimal among linear k-dimensional subspaces.
- •Implementation requires centering, and often scaling.
- •SVD is typically the computational workhorse.
- •PCA is a baseline; nonlinear methods are for nonlinear structure.

## Worked Examples (3)

### Example 1: Compute PCA from a 2D covariance matrix (directions + explained variance)

Suppose your centered 2D data has covariance

Σ=[4223].\Sigma = \begin{bmatrix} 4 & 2 \\ 2 & 3 \end{bmatrix}.Σ=[42​23​].

Find the principal components and how much variance the first component explains.

1. Compute eigenvalues from det(Σ − λI)=0:

   \n$det⁡[4−λ223−λ]=(4−λ)(3−λ)−4\det\begin{bmatrix}4-\lambda & 2\\2 & 3-\lambda\end{bmatrix}=(4-\lambda)(3-\lambda)-4det[4−λ2​23−λ​]=(4−λ)(3−λ)−4$

   \nExpand:

   \n$(4−λ)(3−λ)−4=12−4λ−3λ+λ2−4=λ2−7λ+8.(4-\lambda)(3-\lambda)-4 = 12 -4\lambda -3\lambda + \lambda^2 -4 = \lambda^2 -7\lambda + 8.(4−λ)(3−λ)−4=12−4λ−3λ+λ2−4=λ2−7λ+8.$
2. Solve the quadratic:

   \n$λ2−7λ+8=0\lambda^2 - 7\lambda + 8 = 0λ2−7λ+8=0$

   \n$λ=7±49−322=7±172.\lambda = \frac{7 \pm \sqrt{49-32}}{2} = \frac{7 \pm \sqrt{17}}{2}.λ=27±49−32​​=27±17​​.$
3. Order them:

   \n$λ1=7+172≈5.561,\lambda\_1 = \frac{7+\sqrt{17}}{2} \approx 5.561,λ1​=27+17​​≈5.561,$

   λ2=7−172≈1.439.\lambda\_2 = \frac{7-\sqrt{17}}{2} \approx 1.439.λ2​=27−17​​≈1.439.
4. Find eigenvector for λ₁ by solving (Σ − λ₁I)**v**=0:

   \n$[4−λ1223−λ1][v1v2]=0.\begin{bmatrix}4-\lambda\_1 & 2\\2 & 3-\lambda\_1\end{bmatrix}\begin{bmatrix}v\_1\\v\_2\end{bmatrix}=\mathbf{0}.[4−λ1​2​23−λ1​​][v1​v2​​]=0.$
5. Use the first row: (4−λ₁)v₁ + 2v₂ = 0 ⇒ 2v₂ = (λ₁−4)v₁.

   \nSo ratio:

   \n$v2v1=λ1−42.\frac{v\_2}{v\_1} = \frac{\lambda\_1-4}{2}.v1​v2​​=2λ1​−4​.$
6. Plug λ₁ ≈ 5.561:

   \n$v2v1≈1.5612≈0.7805.\frac{v\_2}{v\_1} \approx \frac{1.561}{2} \approx 0.7805.v1​v2​​≈21.561​≈0.7805.$
7. Choose a convenient vector proportional to [1, 0.7805]ᵀ and normalize:

   \nNorm ≈ √(1² + 0.7805²) = √(1 + 0.609) = √1.609 ≈ 1.268.

   \nSo

   \n$v1≈[0.7880.615].\mathbf{v}\_1 \approx \begin{bmatrix}0.788\\0.615\end{bmatrix}.v1​≈[0.7880.615​].$
8. Similarly, **v**₂ is orthogonal to **v**₁ (or solve for λ₂). One orthonormal choice is approximately:

   \n$v2≈[−0.6150.788].\mathbf{v}\_2 \approx \begin{bmatrix}-0.615\\0.788\end{bmatrix}.v2​≈[−0.6150.788​].$
9. Compute explained variance ratio for k=1:

   \nTotal variance = tr(Σ)=4+3=7 = λ₁+λ₂.

   \n$EVR(1)=λ1λ1+λ2=λ17≈5.5617≈0.794.\text{EVR}(1)=\frac{\lambda\_1}{\lambda\_1+\lambda\_2}=\frac{\lambda\_1}{7} \approx \frac{5.561}{7} \approx 0.794.EVR(1)=λ1​+λ2​λ1​​=7λ1​​≈75.561​≈0.794.$

**Insight:** Eigenvectors give the principal directions; eigenvalues literally are the variances along those directions. The explained variance ratio is just “how much of the trace you keep.”

### Example 2: PCA via SVD on centered data (and the λ = σ²/n connection)

Let centered data matrix be

Xc=[2001−200−1]∈R4×2.X\_c = \begin{bmatrix}
2 & 0\\
0 & 1\\
-2 & 0\\
0 & -1
\end{bmatrix} \in \mathbb{R}^{4\times 2}.Xc​=​20−20​010−1​​∈R4×2.

Compute the covariance, its eigenvalues, and relate them to singular values of X\_c.

1. Compute covariance using Σ = (1/n) X\_cᵀ X\_c with n=4:

   \nFirst compute X\_cᵀ X\_c:

   \n$XcTXc=[20−20010−1][2001−200−1].X\_c^T X\_c = \begin{bmatrix}2&0&-2&0\\0&1&0&-1\end{bmatrix}\begin{bmatrix}2&0\\0&1\\-2&0\\0&-1\end{bmatrix}.XcT​Xc​=[20​01​−20​0−1​]​20−20​010−1​​.$
2. Multiply:

   \n- (1,1) entry: 2² + 0² + (−2)² + 0² = 8

   - •(2,2) entry: 0² + 1² + 0² + (−1)² = 2
   - •off-diagonals are 0 (columns are orthogonal)

   \nSo

   \n$XcTXc=[8002].X\_c^T X\_c = \begin{bmatrix}8 & 0\\0 & 2\end{bmatrix}.XcT​Xc​=[80​02​].$
3. Now scale by 1/n = 1/4:

   \n$Σ=14[8002]=[2000.5].\Sigma = \frac{1}{4}\begin{bmatrix}8&0\\0&2\end{bmatrix} = \begin{bmatrix}2&0\\0&0.5\end{bmatrix}.Σ=41​[80​02​]=[20​00.5​].$
4. Eigenvalues of Σ are clearly λ₁=2, λ₂=0.5 with eigenvectors e₁=[1,0]ᵀ and e₂=[0,1]ᵀ.
5. Now connect to singular values. By definition, singular values satisfy:

   \n$XcTXc=VΣs2VT.X\_c^T X\_c = V \Sigma\_s^2 V^T.XcT​Xc​=VΣs2​VT.$
6. Here X\_cᵀ X\_c is diagonal with entries 8 and 2, so the singular values are:

   \n$σ1=8=22,σ2=2.\sigma\_1 = \sqrt{8} = 2\sqrt{2},\quad \sigma\_2 = \sqrt{2}.σ1​=8​=22​,σ2​=2​.$
7. Check the PCA relationship λⱼ = σⱼ²/n:

   \n$σ12n=84=2=λ1,\frac{\sigma\_1^2}{n} = \frac{8}{4}=2=\lambda\_1,nσ12​​=48​=2=λ1​,$

   σ22n=24=0.5=λ2.\frac{\sigma\_2^2}{n} = \frac{2}{4}=0.5=\lambda\_2.nσ22​​=42​=0.5=λ2​.

**Insight:** SVD of centered data is PCA in disguise: right singular vectors are principal directions, and eigenvalues are just scaled squared singular values.

### Example 3: Reconstruction error equals dropped eigenvalues (numeric check)

Assume a 3D centered dataset has covariance eigenvalues

λ1=6, λ2=2, λ3=1.\lambda\_1=6,\ \lambda\_2=2,\ \lambda\_3=1.λ1​=6, λ2​=2, λ3​=1.

Compare expected reconstruction error for k=1 vs k=2.

1. Total variance (total expected squared norm) is:

   \n$∑j=13λj=6+2+1=9.\sum\_{j=1}^3 \lambda\_j = 6+2+1=9.∑j=13​λj​=6+2+1=9.$
2. For k=1, you keep λ₁ and drop λ₂, λ₃:

   \nExpected reconstruction error:

   \n$∑j=23λj=2+1=3.\sum\_{j=2}^3 \lambda\_j = 2+1=3.∑j=23​λj​=2+1=3.$
3. For k=2, you keep λ₁+λ₂ and drop λ₃:

   \nExpected reconstruction error:

   \n$λ3=1.\lambda\_3 = 1.λ3​=1.$
4. Consistency check via 'total − captured':

   \n- Captured (k=1): 6 ⇒ error 9−6=3

   - •Captured (k=2): 8 ⇒ error 9−8=1

**Insight:** Once you’re in the PCA basis, reconstruction error is literally the energy in the discarded coordinates. That’s why eigenvalues are such a direct diagnostic.

## Key Takeaways

- ✓

  A principal component **v** is a unit direction maximizing projected variance; it is an eigenvector of the covariance matrix.
- ✓

  Eigenvalues λ\lambdaλ quantify variance captured along their eigenvectors; ordering by λ1≥λ2≥⋯\lambda\_1 \ge \lambda\_2 \ge \cdotsλ1​≥λ2​≥⋯ orders importance.
- ✓

  Projecting onto top-k components uses x^=VkVkTx\hat{\mathbf{x}} = V\_k V\_k^T \mathbf{x}x^=Vk​VkT​x (for centered data).
- ✓

  PCA’s top-k subspace maximizes captured variance ∑j=1kλj\sum\_{j=1}^k \lambda\_j∑j=1k​λj​ and equivalently minimizes expected squared reconstruction error ∑j=k+1dλj\sum\_{j=k+1}^d \lambda\_j∑j=k+1d​λj​.
- ✓

  PCA can be computed via eigen-decomposition of Σ=(1/n)XcTXc\Sigma = (1/n)X\_c^T X\_cΣ=(1/n)XcT​Xc​ or via SVD Xc=UΣsVTX\_c=U\Sigma\_s V^TXc​=UΣs​VT; eigenvalues satisfy λj=σj2/n\lambda\_j=\sigma\_j^2/nλj​=σj2​/n.
- ✓

  Centering is essential; scaling (standardization) is often essential when features have different units.
- ✓

  Explained variance ratio is a practical way to choose k, but task-driven cross-validation is often better for predictive goals.

## Common Mistakes

- ✗

  Forgetting to center the data (PCA then captures mean offsets rather than variation).
- ✗

  Mixing scaling conventions unintentionally (covariance PCA vs correlation PCA) and misinterpreting components because feature units differ.
- ✗

  Choosing k solely from explained variance without checking downstream performance or the effect of noise/outliers.
- ✗

  Recomputing mean/standard deviation on the test set (data leakage; inconsistent coordinate system).

## Practice

easy

Let Σ=[3113]\Sigma = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}Σ=[31​13​]. Find eigenvalues and an orthonormal set of principal components.

**Hint:** This matrix has the form a on diagonal and b off-diagonal; eigenvectors are along [1,1] and [1,−1].

Show solution

Compute eigenvalues: solve det(Σ−λI)=0.

det⁡[3−λ113−λ]=(3−λ)2−1=0\det\begin{bmatrix}3-\lambda & 1\\1 & 3-\lambda\end{bmatrix}=(3-\lambda)^2-1=0det[3−λ1​13−λ​]=(3−λ)2−1=0

So (3−λ)=±1(3-\lambda)=\pm 1(3−λ)=±1 ⇒ λ1=4\lambda\_1=4λ1​=4, λ2=2\lambda\_2=2λ2​=2.

Eigenvector for λ₁=4: (3−4)v₁ + 1 v₂ = 0 ⇒ −v₁+v₂=0 ⇒ v₂=v₁ ⇒ direction [1,1]. Normalize: **v**₁ = (1/√2)[1,1].

Eigenvector for λ₂=2: (3−2)v₁ + 1 v₂ =0 ⇒ v₁+v₂=0 ⇒ direction [1,−1]. Normalize: **v**₂ = (1/√2)[1,−1].

medium

Show that for any orthonormal VkV\_kVk​, the expected reconstruction error satisfies

E[∥x−VkVkTx∥22]=E[∥x∥22]−E[∥VkTx∥22].\mathbb{E}[\|\mathbf{x} - V\_k V\_k^T \mathbf{x}\|\_2^2] = \mathbb{E}[\|\mathbf{x}\|\_2^2] - \mathbb{E}[\|V\_k^T \mathbf{x}\|\_2^2].E[∥x−Vk​VkT​x∥22​]=E[∥x∥22​]−E[∥VkT​x∥22​].

**Hint:** Use that VkVkTV\_k V\_k^TVk​VkT​ is an orthogonal projector and apply Pythagoras: projected part is orthogonal to residual.

Show solution

Let x^=VkVkTx\hat{\mathbf{x}} = V\_k V\_k^T \mathbf{x}x^=Vk​VkT​x and residual r=x−x^\mathbf{r}=\mathbf{x}-\hat{\mathbf{x}}r=x−x^.

Because VkVkTV\_k V\_k^TVk​VkT​ is an orthogonal projector, x^\hat{\mathbf{x}}x^ lies in the span of columns of VkV\_kVk​, while r\mathbf{r}r lies in the orthogonal complement. Therefore x^Tr=0\hat{\mathbf{x}}^T \mathbf{r}=0x^Tr=0.

So

∥x∥22=∥x^+r∥22=∥x^∥22+∥r∥22.\|\mathbf{x}\|\_2^2 = \|\hat{\mathbf{x}} + \mathbf{r}\|\_2^2 = \|\hat{\mathbf{x}}\|\_2^2 + \|\mathbf{r}\|\_2^2.∥x∥22​=∥x^+r∥22​=∥x^∥22​+∥r∥22​.

Rearrange:

∥r∥22=∥x∥22−∥x^∥22.\|\mathbf{r}\|\_2^2 = \|\mathbf{x}\|\_2^2 - \|\hat{\mathbf{x}}\|\_2^2.∥r∥22​=∥x∥22​−∥x^∥22​.

Now note ∥x^∥22=∥VkVkTx∥22=∥VkTx∥22\|\hat{\mathbf{x}}\|\_2^2 = \|V\_k V\_k^T \mathbf{x}\|\_2^2 = \|V\_k^T \mathbf{x}\|\_2^2∥x^∥22​=∥Vk​VkT​x∥22​=∥VkT​x∥22​ because VkV\_kVk​ is orthonormal. Take expectation of both sides to obtain the identity.

hard

You have centered data Xc∈Rn×dX\_c \in \mathbb{R}^{n\times d}Xc​∈Rn×d with SVD Xc=UΣsVTX\_c=U\Sigma\_s V^TXc​=UΣs​VT. Prove that the covariance matrix Σ=(1/n)XcTXc\Sigma=(1/n)X\_c^T X\_cΣ=(1/n)XcT​Xc​ has eigenvectors equal to columns of V and eigenvalues λj=σj2/n\lambda\_j=\sigma\_j^2/nλj​=σj2​/n.

**Hint:** Compute XcTXcX\_c^T X\_cXcT​Xc​ using the SVD and simplify using UTU=IU^T U = IUTU=I.

Show solution

Start with SVD: Xc=UΣsVTX\_c=U\Sigma\_s V^TXc​=UΣs​VT.

Compute:

\[\begin{aligned}

X\_c^T X\_c

&= (U\Sigma\_s V^T)^T (U\Sigma\_s V^T) \\

&= (V \Sigma\_s^T U^T)(U\Sigma\_s V^T) \\

&= V \Sigma\_s^T (U^T U) \Sigma\_s V^T \\

&= V \Sigma\_s^T \Sigma\_s V^T.

\end{aligned}\]

Since Σs\Sigma\_sΣs​ is diagonal with nonnegative singular values, ΣsTΣs=Σs2\Sigma\_s^T\Sigma\_s = \Sigma\_s^2ΣsT​Σs​=Σs2​.

Thus:

XcTXc=VΣs2VT.X\_c^T X\_c = V \Sigma\_s^2 V^T.XcT​Xc​=VΣs2​VT.

Scale by 1/n:

Σ=1nXcTXc=V(1nΣs2)VT.\Sigma = \frac{1}{n} X\_c^T X\_c = V \left(\frac{1}{n}\Sigma\_s^2\right) V^T.Σ=n1​XcT​Xc​=V(n1​Σs2​)VT.

This is an eigen-decomposition with eigenvectors given by columns of V and eigenvalues λj=σj2/n\lambda\_j = \sigma\_j^2/nλj​=σj2​/n.

## Connections

Next steps and related nodes:

- •[Dimensionality Reduction](/tech-tree/dimensionality-reduction/)

Useful prerequisites to revisit as needed:

- •[Singular Value Decomposition](/tech-tree/svd/)
- •[Covariance and Correlation](/tech-tree/covariance-correlation/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
