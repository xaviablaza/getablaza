---
title: Dimensionality Reduction
description: Reducing feature dimensions. PCA, t-SNE, autoencoders.
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
inspiration_url: https://templeton.host/tech-tree/dimensionality-reduction/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/dimensionality-reduction/](https://templeton.host/tech-tree/dimensionality-reduction/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Dimensionality Reduction

Machine LearningDifficulty: ★★★★☆Depth: 11Unlocks: 0

Reducing feature dimensions. PCA, t-SNE, autoencoders.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Low-dimensional embedding: represent high-dimensional data points as vectors in a much lower-dimensional space
- -Preservation criterion: a single defined property to retain (e.g., variance, pairwise distances, or local neighborhood/manifold structure)
- -Mapping mechanism: an explicit transform (parameterized function or linear projection) that produces the lower-dimensional embedding

## Key Symbols & Notation

f: R^D -> R^d (d << D)

## Essential Relationships

- -Dimensionality reduction = choose f that optimizes the specified preservation criterion under the constraint d << D; the choice of linear vs nonlinear f determines which structures can be preserved

## Prerequisites (2)

[Principal Component Analysis6 atoms](/tech-tree/pca/)[Neural Networks6 atoms](/tech-tree/neural-networks/)

Advanced Learning Details

### Graph Position

220

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

11

Chain Length

### Cognitive Load

5

Atomic Elements

52

Total Elements

L4

Percentile Level

L3

Atomic Level

### All Concepts (21)

- - Dimensionality reduction as mapping high-dimensional data to a lower-dimensional embedding/latent space (an 'embedding' or 'latent representation')
- - Manifold assumption: high-dimensional data lie near a lower-dimensional manifold that meaningful algorithms try to uncover
- - Bottleneck: constraining a representation to fewer dimensions to force compression / abstraction
- - Linear vs nonlinear dimensionality reduction: linear methods (PCA) versus nonlinear methods (t-SNE, autoencoders)
- - Autoencoder architecture: encoder network that maps x -> z and decoder network that maps z -> x̂ (reconstruction)
- - Latent code / latent dimension: the vector z that parametrizes the lower-dimensional representation
- - Reconstruction loss/error: objective measuring how well decoded x̂ matches original x (e.g., MSE, cross-entropy)
- - Undercomplete vs overcomplete autoencoders: bottleneck smaller than input (undercomplete) versus larger (overcomplete) and effect on learning
- - Regularized autoencoders (concepts): denoising autoencoders (train on corrupted inputs), sparse autoencoders (sparsity penalty), contractive autoencoders (Jacobian penalty)
- - Variational autoencoder (VAE) idea: treat latent code probabilistically (an encoder produces a distribution q(z|x)), impose a prior p(z), and learn a generative decoder p(x|z)
- - Evidence lower bound (ELBO): VAE training objective combining reconstruction term and a regularizing KL term
- - Reparameterization trick: a way to sample z from q(z|x) in a way that allows gradients to flow through stochastic sampling (e.g., z = μ + σ ⊙ ε with ε ~ N(0,I))
- - t-SNE core idea: convert pairwise distances into high-dimensional conditional probabilities and find low-D points whose pairwise probabilities match (stochastic neighbor embedding)
- - Perplexity in t-SNE: a scale parameter that controls the effective number of neighbors (controls σ\_i selection for each point)
- - High-dimensional conditional similarity probabilities (p\_{j|i}): probability that j is neighbor of i computed with Gaussian kernel and point-specific bandwidths
- - Symmetrized joint probabilities (p\_{ij}) used as the target distribution in t-SNE
- - Low-dimensional similarity kernel in t-SNE: heavy-tailed Student t (with one degree of freedom) used to compute q\_{ij} in embedding space
- - KL divergence as the t-SNE loss measuring mismatch between high-D and low-D similarity distributions
- - Nonlinear methods focus on preserving local structure (neighborhoods) rather than global variance
- - Optimization properties: objectives are nonconvex, require iterative gradient-based optimization, and results can vary with random initialization and hyperparameters
- - Interpretation cautions: distances/axes in low-D embeddings often lack absolute meaning - embeddings primarily encode relative similarity, especially for visualization

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Modern datasets often live in spaces with hundreds, thousands, or millions of features—but the structure we care about is frequently much simpler. Dimensionality reduction is the art of finding that simpler structure without throwing away what matters.

TL;DR:

Dimensionality reduction learns a mapping f: ℝᴰ → ℝᵈ (with d ≪ D) that embeds high-dimensional points into a lower-dimensional space while preserving a chosen property (variance, distances, neighborhoods, or reconstruction). Linear methods (PCA) preserve global variance; nonlinear methods like t-SNE preserve local neighborhoods for visualization; autoencoders learn task-driven nonlinear embeddings by compressing and reconstructing data.

## What Is Dimensionality Reduction?

### Why it exists (motivation first)

High-dimensional feature spaces create three recurring problems:

1) **Computation and storage**: Many ML algorithms scale poorly with D. Pairwise distances, covariance matrices, nearest-neighbor search, and kernel methods can become expensive.

2) **Generalization and sample efficiency**: With limited data, many degrees of freedom invite overfitting. In broad strokes, if your model can wiggle in D directions, you need enough data to constrain those directions.

3) **Geometry gets weird in high dimensions** (“curse of dimensionality”): Distances concentrate, neighborhoods become sparse, and local density estimation becomes hard. Many intuitive operations (like “find the nearest neighbors”) degrade unless the data truly lies on a lower-dimensional structure.

Dimensionality reduction aims to address these issues by learning an embedding that is lower-dimensional but still useful.

### The core definition

You are given data points **x** ∈ ℝᴰ. Dimensionality reduction chooses a smaller dimension d (typically 2, 3, 10, 50, 256, …) and learns a mapping

f: ℝᴰ → ℝᵈ with d ≪ D

so that the embedding **z** = f(**x**) retains something you care about.

The key phrase is **“retain something you care about.”** Dimensionality reduction is not one algorithm; it is a design pattern:

- •Pick a **preservation criterion** (variance, distances, neighborhoods, reconstructability, label separability, …).
- •Choose a **mapping mechanism** (linear projection, kernel method, stochastic neighbor embedding, neural network encoder, …).
- •Optimize the mapping so the criterion is met.

### Three atomic concepts (the “tech tree” lens)

1) **Low-dimensional embedding**

- •Goal: represent each high-D point **x** as a low-D vector **z**.
- •Interpretation: **z** is a coordinate system for the “intrinsic factors” of the data.

2) **Preservation criterion**

- •You must define what “good” means.
- •Examples:
- •PCA: preserve **maximum variance** (global, linear).
- •Classical MDS: preserve **pairwise distances**.
- •t-SNE / UMAP: preserve **local neighborhood structure**.
- •Autoencoders: preserve **reconstruction ability** under compression.

3) **Mapping mechanism**

- •Linear: **z** = **W**ᵀ(**x** − **μ**) where **W** ∈ ℝᴰ×ᵈ.
- •Nonlinear parametric: **z** = encoder\_θ(**x**) (a neural network).
- •Nonparametric: embeddings only for the training points (classic t-SNE); new points require extra machinery.

### A helpful taxonomy

Dimensionality reduction methods often differ along two axes:

| Axis | Option A | Option B |
| --- | --- | --- |
| Mapping | Parametric (explicit f; can embed new points) | Nonparametric (embeds training set; out-of-sample is nontrivial) |
| Geometry preserved | Global (variance, long-range distances) | Local (neighbors, manifold structure) |

And a third practical axis:

| Goal | Typical method |
| --- | --- |
| Visualization (2D/3D plots) | t-SNE, UMAP, PCA (as baseline) |
| Compression for downstream models | PCA, autoencoders |
| Denoising / representation learning | Denoising autoencoders, contractive autoencoders |
| Preprocessing for clustering / kNN | PCA, UMAP (careful), sometimes random projections |

### What dimensionality reduction is *not*

- •It is not automatically “information-preserving.” If d < D, some information is lost.
- •It is not automatically “better.” A bad embedding can destroy class separability or distort neighborhoods.
- •It is not necessarily interpretable (especially nonlinear embeddings).

The central skill: **match the preservation criterion to your end use.**

## Core Mechanic 1: Preservation Criteria (What are you trying to keep?)

### Why criteria matter

If you only remember one thing: **dimensionality reduction is defined by what it preserves**. Two embeddings with the same d can behave radically differently depending on the criterion.

A useful way to think:

- •You have original points **x**ᵢ in ℝᴰ.
- •You produce embeddings **z**ᵢ in ℝᵈ.
- •You define a loss L({**x**ᵢ}, {**z**ᵢ}) that penalizes “bad” embeddings.

Different algorithms pick different L.

### Criterion A: Preserve variance (PCA-style, global, linear)

Even though you already know PCA, it’s worth anchoring it as the prototypical **global** criterion.

Let centered data be **x̃** = **x** − **μ**.

Pick an orthonormal basis **W** = [**w**₁ … **w**ᵈ] ∈ ℝᴰ×ᵈ with **W**ᵀ**W** = **I**.

Projection:

- •**z** = **W**ᵀ **x̃**
- •Reconstruction (linear): **x̂** = **W** **z** + **μ**

PCA chooses **W** to maximize captured variance:

maximize ∑ᵢ ‖**W**ᵀ **x̃**ᵢ‖²

Equivalently, minimize reconstruction error:

minimize ∑ᵢ ‖**x̃**ᵢ − **W** **W**ᵀ **x̃**ᵢ‖²

Why this matters:

- •PCA tends to preserve large-scale directions.
- •It is excellent for compression when data is approximately linear or when noise is isotropic.
- •It can fail when the “interesting” structure is nonlinear (e.g., a curved manifold).

### Criterion B: Preserve pairwise distances (MDS-style)

Suppose you care about distances between points. Let δᵢⱼ be distances in the original space (often Euclidean):

δᵢⱼ = ‖**x**ᵢ − **x**ⱼ‖

You want:

‖**z**ᵢ − **z**ⱼ‖ ≈ δᵢⱼ

A classic objective (stress) is:

Stress = ∑ᵢ<ⱼ (‖**z**ᵢ − **z**ⱼ‖ − δᵢⱼ)²

This is **global**: it tries to match *all* pairwise distances. In high dimensions, however, global distance preservation in very low d can be impossible, so tradeoffs are inevitable.

### Criterion C: Preserve local neighborhoods (t-SNE/UMAP-style)

Visualization methods often care more about “who is near whom” than exact distances.

t-SNE does this via probability distributions.

1) Convert high-D distances into conditional neighbor probabilities:

pⱼ|ᵢ ∝ exp(−‖**x**ᵢ − **x**ⱼ‖² / (2σᵢ²))

σᵢ is chosen so that each point has a roughly fixed effective number of neighbors (the **perplexity** parameter controls this).

2) Define low-D similarities with a heavy-tailed distribution (Student-t):

qᵢⱼ ∝ (1 + ‖**z**ᵢ − **z**ⱼ‖²)⁻¹

3) Minimize KL divergence so that neighbors in high-D stay neighbors in low-D:

KL(P ‖ Q) = ∑ᵢ ∑ⱼ pᵢⱼ log(pᵢⱼ / qᵢⱼ)

What this criterion buys you:

- •Local clusters become visible.

What it does *not* guarantee:

- •Global distances between clusters are not reliable.
- •Relative cluster sizes can be misleading.

UMAP has a similar “local connectivity” spirit but uses a graph/fuzzy simplicial set objective; practically, it often preserves more global structure than t-SNE, but still primarily optimizes neighborhood relations.

### Criterion D: Preserve reconstructability (autoencoder-style)

If your downstream tasks require information beyond neighborhoods—say, you need a compressed representation that can regenerate the input—then **reconstruction** is a natural criterion.

An autoencoder learns:

- •Encoder: f\_θ: ℝᴰ → ℝᵈ
- •Decoder: g\_φ: ℝᵈ → ℝᴰ

with embedding **z** = f\_θ(**x**) and reconstruction **x̂** = g\_φ(**z**).

Typical loss:

L(θ, φ) = ∑ᵢ ‖**x**ᵢ − g\_φ(f\_θ(**x**ᵢ))‖²

or for images, sometimes cross-entropy / perceptual losses.

This criterion is *task-agnostic* but not “semantics-agnostic”: the learned **z** depends strongly on network architecture, bottleneck size d, regularization, and data.

### Choosing a criterion: a decision table

| If you need… | Preserve… | Typical choice | Notes |
| --- | --- | --- | --- |
| Fast linear compression, denoising, baseline | Variance / reconstruction (linear) | PCA | Strong baseline; interpretable components |
| 2D/3D visualization of clusters | Local neighborhoods | t-SNE, UMAP | Do not over-interpret global geometry |
| Approximate distance geometry | Pairwise distances | MDS / Isomap | Hard in very low d; can distort heavily |
| Nonlinear features for downstream models | Reconstruction + regularization | Autoencoder / VAE | Parametric; can embed new data |

A practical workflow is often: PCA → (optional) t-SNE/UMAP for visualization; or PCA → autoencoder for nonlinear compression.

## Core Mechanic 2: Mapping Mechanisms (How do you produce the embedding?)

### Why mapping mechanisms matter

Two methods can preserve “local neighborhoods,” but one may:

- •produce an explicit function f you can apply to new points,
- •or only provide coordinates for the training set.

This matters whenever you want to deploy an embedding in production, feed it into a classifier, or update it as new data arrives.

### Mechanism A: Linear projections

The simplest parametric mapping:

f(**x**) = **W**ᵀ(**x** − **μ**)

Properties:

- •Fast: O(Dd) per point.
- •Stable and deterministic.
- •Limited expressivity: only rotates/scales along a linear subspace.

When it shines:

- •Data is approximately linear (or you only need a coarse compression).
- •You want interpretability (loadings show feature contributions).

### Mechanism B: Kernel methods (brief positioning)

Kernel PCA (and related methods) implicitly map data to a high-dimensional feature space via a kernel k(**x**, **x′**) and then do PCA there.

It enables nonlinear embeddings while keeping an eigenvector-based formulation.

Tradeoffs:

- •Often nonparametric-ish: embedding new points requires computing kernel values to many training points.
- •Scaling is challenging for large n.

This node focuses on PCA/t-SNE/autoencoders, but kernel ideas explain a common theme: **nonlinear geometry without explicit neural networks**.

### Mechanism C: Nonparametric neighborhood embedding (classic t-SNE)

Classic t-SNE learns {**z**ᵢ} directly for the dataset. There is no explicit f.

Consequences:

- •Great for a one-off visualization.
- •Awkward for production: to embed a new point **x\_new**, you typically:
- •rerun t-SNE with all points (costly), or
- •use approximations (parametric t-SNE, training a regression model from **x** to **z**, etc.).

So, think of t-SNE as: **optimize coordinates, not a function**.

### Mechanism D: Neural network encoders (autoencoders)

An autoencoder defines an explicit parametric mapping f\_θ.

A typical structure:

- •Encoder: **x** → (Dense/Conv layers) → bottleneck **z**
- •Decoder: **z** → (mirrored layers) → reconstruction **x̂**

Because f\_θ is explicit:

- •New data embeddings are easy: **z\_new** = f\_θ(**x\_new**)
- •You can fine-tune or continue training.

But because it is flexible:

- •It may learn “shortcuts” that reconstruct without producing a nice latent space.
- •Regularization becomes important.

### Regularizing the mapping (making embeddings usable)

A pure reconstruction objective can yield embeddings that are hard to use for clustering or interpolation. Common fixes:

1) **Denoising autoencoder**

- •Corrupt input **x** → **x̃** (noise, masking)
- •Train to reconstruct clean **x** from **x̃**

Loss:

L = ∑ᵢ ‖**x**ᵢ − g\_φ(f\_θ(**x̃**ᵢ))‖²

Effect: forces **z** to capture robust structure.

2) **Contractive penalty** (encourage local smoothness)

Penalize Jacobian magnitude:

L = reconstruction + λ ‖∂f\_θ(**x**)/∂**x**‖\_F²

Interpretation: small input changes shouldn’t cause wild latent changes.

3) **Variational autoencoder (VAE)** (probabilistic latent space)

Instead of a point **z**, encoder outputs a distribution q\_θ(**z**|**x**) and regularizes it toward a prior p(**z**) (often 𝒩(0, **I**)).

Objective (ELBO):

maximize ∑ᵢ 𝔼\_{q\_θ(**z**|**x**ᵢ)}[log p\_φ(**x**ᵢ|**z**)] − KL(q\_θ(**z**|**x**ᵢ) ‖ p(**z**))

Effect: more continuous, “organized” latent spaces—useful for generation and interpolation.

### A practical comparison table

| Method | f: ℝᴰ → ℝᵈ explicit? | Preserves | Strength | Weakness |
| --- | --- | --- | --- | --- |
| PCA | Yes (linear) | Global variance / linear reconstruction | Fast, stable, interpretable | Misses nonlinear structure |
| t-SNE | No (classic) | Local neighborhoods | Excellent 2D/3D cluster visualization | Global geometry unreliable; hard out-of-sample |
| Autoencoder | Yes (nonlinear) | Reconstruction (plus whatever regularization encourages) | Parametric, flexible, scalable | Needs tuning; can learn unhelpful latents |

The high-level skill: choose the simplest mapping mechanism that can satisfy your preservation criterion.

## Applications and Connections (How it’s used in real ML pipelines)

### 1) Visualization as a diagnostic tool

A 2D embedding is often used to answer questions like:

- •Are there natural clusters?
- •Do labels separate cleanly?
- •Are there outliers or mislabeled points?
- •Did feature engineering help?

Best practice:

- •Start with PCA to 50–100 dimensions to denoise.
- •Then run t-SNE or UMAP to 2D/3D.

Why the PCA pre-step helps:

- •High-D noise can dominate neighbor computations.
- •t-SNE’s pairwise computations are easier and sometimes more stable after PCA.

Interpretation warnings (especially t-SNE):

- •The distance between clusters is not a trustworthy measure of semantic separation.
- •Cluster “islands” can appear even when there is a continuum.

### 2) Compression for downstream learning

Using **z** as input to a classifier/regressor can:

- •reduce overfitting,
- •reduce training time,
- •improve conditioning.

PCA is common when:

- •features are correlated,
- •you want a quick, reliable dimension reduction,
- •you need a deterministic transform.

Autoencoders are common when:

- •data is high-dimensional and structured (images, audio, text embeddings),
- •linear subspaces are insufficient,
- •you want representations transferable across tasks.

### 3) Nearest-neighbor search and retrieval

Many retrieval systems use embeddings:

- •Learn f(**x**) so that similar items are close in ℝᵈ.
- •Use approximate nearest-neighbor (ANN) indices.

Note: This often becomes **metric learning**, where the preservation criterion is label- or relevance-driven (contrastive/triplet losses). Dimensionality reduction is the geometric core: you still learn f: ℝᴰ → ℝᵈ.

### 4) Denoising and anomaly detection

If you learn a low-dimensional model of “normal” data, anomalies often reconstruct poorly.

Autoencoder anomaly score:

score(**x**) = ‖**x** − g\_φ(f\_θ(**x**))‖

Caveat: Powerful autoencoders can sometimes reconstruct anomalies too well. Regularization and capacity control matter.

### 5) Manifold hypothesis and representation learning

A guiding intuition: real-world data often lies near a manifold of much smaller intrinsic dimension than D.

- •t-SNE/UMAP try to preserve local manifold neighborhoods.
- •Autoencoders try to learn coordinates on that manifold.

But “manifold” is a hypothesis, not a guarantee. Dimensionality reduction is how you test whether a low-dimensional structure exists and is useful.

### 6) How to validate an embedding

Validation depends on your purpose:

- •For visualization: do multiple runs, vary perplexity / random seeds; check stability.
- •For downstream tasks: measure performance (accuracy, AUC, RMSE) using **z**.
- •For reconstruction: track reconstruction error on held-out data.
- •For neighborhood preservation: use metrics like trustworthiness/continuity (conceptually: do neighbors stay neighbors?).

A simple sanity checklist:

1) Standardize or whiten features when appropriate.

2) Fit on train set only; apply transform to validation/test.

3) Don’t select d using test-set performance.

4) For t-SNE: avoid drawing conclusions from global geometry.

Dimensionality reduction is not a one-time trick; it is a model choice that should be evaluated like any other.

## Worked Examples (3)

### Example 1: From PCA variance to reconstruction error (why PCA is a compression method)

You have centered data points {**x̃**ᵢ} in ℝᴰ and choose an orthonormal projection matrix **W** ∈ ℝᴰ×ᵈ (so **W**ᵀ**W** = **I**). Show that maximizing captured variance ∑ᵢ ‖**W**ᵀ**x̃**ᵢ‖² is equivalent to minimizing reconstruction error ∑ᵢ ‖**x̃**ᵢ − **W****W**ᵀ**x̃**ᵢ‖².

1. Define the projection and reconstruction:

   **z**ᵢ = **W**ᵀ **x̃**ᵢ

   **x̂̃**ᵢ = **W** **z**ᵢ = **W****W**ᵀ **x̃**ᵢ
2. Write reconstruction error for one point:

   ‖**x̃**ᵢ − **x̂̃**ᵢ‖² = ‖**x̃**ᵢ − **W****W**ᵀ **x̃**ᵢ‖²
3. Use orthogonal decomposition: since **W****W**ᵀ is the projector onto the span of columns of **W**,

   **x̃**ᵢ = (**W****W**ᵀ**x̃**ᵢ) + ( ( **I** − **W****W**ᵀ ) **x̃**ᵢ )

   The two components are orthogonal.
4. Apply Pythagoras:

   ‖**x̃**ᵢ‖² = ‖**W****W**ᵀ**x̃**ᵢ‖² + ‖( **I** − **W****W**ᵀ )**x̃**ᵢ‖²
5. Notice the reconstruction residual is exactly the orthogonal component:

   ‖**x̃**ᵢ − **W****W**ᵀ**x̃**ᵢ‖² = ‖( **I** − **W****W**ᵀ )**x̃**ᵢ‖²
6. So rearrange:

   ‖**x̃**ᵢ − **W****W**ᵀ**x̃**ᵢ‖² = ‖**x̃**ᵢ‖² − ‖**W****W**ᵀ**x̃**ᵢ‖²
7. Sum over i:

   ∑ᵢ ‖**x̃**ᵢ − **W****W**ᵀ**x̃**ᵢ‖² = ∑ᵢ ‖**x̃**ᵢ‖² − ∑ᵢ ‖**W****W**ᵀ**x̃**ᵢ‖²
8. Use **W**ᵀ**W** = **I** to simplify the retained term:

   ‖**W****W**ᵀ**x̃**ᵢ‖² = ‖**W**ᵀ**x̃**ᵢ‖²

   (because projecting then measuring norm equals norm of coordinates in an orthonormal basis).
9. Final equivalence:

   ∑ᵢ ‖**x̃**ᵢ − **W****W**ᵀ**x̃**ᵢ‖² = constant − ∑ᵢ ‖**W**ᵀ**x̃**ᵢ‖²

   So minimizing reconstruction error is equivalent to maximizing captured variance.

**Insight:** PCA’s “maximize variance” and “minimize squared reconstruction error” are the same problem because orthogonal projection splits each point into a kept part plus an orthogonal residual, and squared norms add cleanly.

### Example 2: What t-SNE is optimizing (local neighborhood preservation via KL divergence)

You have points **x**ᵢ in ℝᴰ and want a 2D embedding **z**ᵢ in ℝ² for visualization. Explain how t-SNE turns distances into probabilities and why the KL(P ‖ Q) objective emphasizes preserving local neighbors.

1. Start from the design goal: keep local neighborhoods.

   Instead of trying to match all distances, define “neighborliness” as a probability distribution.
2. Define conditional probabilities in high-D:

   pⱼ|ᵢ = exp(−‖**x**ᵢ − **x**ⱼ‖² / (2σᵢ²)) / ∑\_{k≠i} exp(−‖**x**ᵢ − **x**\_k‖² / (2σᵢ²))

   Interpretation: points closer to i get higher probability mass.
3. Choose σᵢ to match a target perplexity.

   Perplexity is 2^{H(P\_i)} where H is Shannon entropy; practically, it sets an effective neighbor count so each point adapts to local density.
4. Symmetrize to get joint probabilities:

   pᵢⱼ = (pⱼ|ᵢ + pᵢ|ⱼ) / (2n)

   Now P = {pᵢⱼ} describes neighbor affinities in high-D.
5. Define low-D affinities with a heavy tail:

   qᵢⱼ = (1 + ‖**z**ᵢ − **z**ⱼ‖²)⁻¹ / ∑\_{a≠b} (1 + ‖**z**\_a − **z**\_b‖²)⁻¹

   The Student-t tail prevents distant points from all collapsing together (it combats the “crowding problem”).
6. Optimize with KL divergence:

   KL(P ‖ Q) = ∑ᵢ ∑ⱼ pᵢⱼ log(pᵢⱼ / qᵢⱼ)

   Only pairs with large pᵢⱼ (true neighbors) contribute strongly to the loss.
7. Reason about asymmetry:

   Because it is KL(P ‖ Q), if pᵢⱼ is large but qᵢⱼ is small, the penalty is severe.

   If pᵢⱼ is tiny (non-neighbors) but qᵢⱼ is somewhat large, the penalty is mild.

   So the optimization prioritizes: “don’t lose real neighbors,” rather than “perfectly separate all non-neighbors.”
8. Conclusion:

   t-SNE is engineered to make local structure visually salient (clusters/neighborhoods) even if global distances become distorted.

**Insight:** t-SNE’s choice of KL(P ‖ Q) (not KL(Q ‖ P)) is deliberate: it heavily punishes missing true neighbors, which is exactly what you want for cluster visualization—but it also explains why global geometry is not reliable.

### Example 3: Autoencoder as dimensionality reduction (bottleneck, reconstruction, and why regularization matters)

You want f\_θ: ℝᴰ → ℝᵈ with d ≪ D to compress vectors **x** while keeping enough information for downstream tasks. You train an autoencoder with squared reconstruction loss. Explain what the bottleneck forces the model to do, and why a denoising variant often yields better embeddings.

1. Define the model:

   Encoder: **z** = f\_θ(**x**) ∈ ℝᵈ

   Decoder: **x̂** = g\_φ(**z**) ∈ ℝᴰ
2. Train with reconstruction loss:

   L(θ, φ) = ∑ᵢ ‖**x**ᵢ − g\_φ(f\_θ(**x**ᵢ))‖²
3. Interpret the bottleneck:

   Because d ≪ D, **z** cannot store arbitrary details of **x**.

   The network must learn a compressed code capturing the most predictable/shared factors across the dataset.
4. Identify a failure mode:

   If the network has too much capacity (especially the decoder), it may learn a representation that reconstructs well but is not smooth or meaningful for similarity (e.g., it may encode idiosyncratic details in a brittle way).
5. Apply denoising:

   Sample a corruption process C (Gaussian noise, masking, dropout) and form **x̃** = C(**x**).

   Train:

   L = ∑ᵢ ‖**x**ᵢ − g\_φ(f\_θ(**x̃**ᵢ))‖²
6. Explain why denoising helps:

   To reconstruct clean **x** from **x̃**, the encoder must capture stable structure and ignore noise.

   This tends to produce embeddings **z** that align better with semantic factors and are more robust for downstream tasks.

**Insight:** Autoencoders reduce dimension by forcing information through a bottleneck. Regularization (like denoising) changes what gets preserved: instead of memorizing details, the embedding must capture robust, repeatable structure.

## Key Takeaways

- ✓

  Dimensionality reduction learns an embedding **z** = f(**x**) with f: ℝᴰ → ℝᵈ and d ≪ D; the entire problem is defined by what you choose to preserve.
- ✓

  Preservation criteria differ: PCA preserves global variance (and minimizes squared reconstruction error), while t-SNE prioritizes local neighborhood structure for visualization.
- ✓

  Mapping mechanisms matter operationally: PCA and autoencoders are parametric (easy out-of-sample), while classic t-SNE is nonparametric (great plots, awkward deployment).
- ✓

  Neighborhood-preserving embeddings can distort global geometry; avoid interpreting inter-cluster distances in t-SNE plots as meaningful metrics.
- ✓

  Autoencoders preserve reconstructability, but without regularization they can learn brittle or unhelpful latent spaces; denoising/contractive/VAE-style regularization often improves usefulness.
- ✓

  A strong workflow is to start with simple baselines (standardization + PCA), then escalate to nonlinear methods only if the objective demands it.
- ✓

  Validation must match the purpose: reconstruction error for compression, downstream metrics for features, and neighborhood metrics or stability checks for visualization.

## Common Mistakes

- ✗

  Over-interpreting t-SNE: treating distances between clusters as meaningful, or assuming a 2D layout reflects true global geometry.
- ✗

  Fitting the dimensionality reducer on the full dataset (train + test), which leaks information; always fit on training data and transform held-out data.
- ✗

  Skipping scaling/centering when using PCA on features with incompatible units, causing components to reflect measurement scale rather than structure.
- ✗

  Using an autoencoder with excessive capacity and no regularization, then assuming the latent space is semantically meaningful just because reconstruction loss is low.

## Practice

easy

You need a 2D plot to inspect whether your labeled dataset has separable classes. Which method would you try first: PCA or t-SNE? Explain what each will preserve and what could mislead you in the visualization.

**Hint:** Think: global variance vs local neighborhoods; and what you want to learn from a plot.

Show solution

Start with PCA as a baseline because it is fast, deterministic, and preserves global variance (large-scale directions). If classes separate in the top PCs, that’s strong evidence of linear separability in the original space.

Then try t-SNE if PCA does not show separation but you suspect nonlinear/local structure. t-SNE preserves local neighborhoods, often making clusters visible even when PCA looks mixed.

Misleading aspects: PCA can hide nonlinear separability; t-SNE can invent visually separated clusters and its inter-cluster distances (and relative cluster sizes) are not reliable measures of true global separation.

medium

Suppose you trained a classic (nonparametric) t-SNE embedding on n points and now receive a new point **x\_new**. Why is it nontrivial to compute **z\_new**? Name two practical strategies to handle this situation.

**Hint:** Ask: does t-SNE learn f(**x**) or only {**z**ᵢ}? What does “out-of-sample” mean here?

Show solution

Classic t-SNE optimizes the coordinates {**z**ᵢ} directly; it does not learn an explicit mapping f: ℝᴰ → ℝᵈ. Therefore, there is no built-in way to embed **x\_new** without changing the optimization problem.

Two practical strategies:

1) Rerun (or continue) t-SNE including **x\_new** and all prior points (expensive; may change existing positions).

2) Learn an approximate parametric map after the fact, e.g., train a regression model or neural network to predict **z** from **x** using the existing pairs (**x**ᵢ, **z**ᵢ), or use parametric t-SNE variants that learn an explicit encoder.

hard

You want a nonlinear embedding **z** for downstream classification. You train an autoencoder with very low reconstruction error, but a classifier trained on **z** performs poorly compared to training on the original features. Give two reasons this can happen and one modification to your training that could improve **z**.

**Hint:** Reconstruction ≠ discriminative usefulness. Think about what information the autoencoder is incentivized to keep and how it might ignore label-relevant structure.

Show solution

Two reasons:

1) The autoencoder optimizes reconstruction, not class separation. It may dedicate capacity to reconstructing high-variance nuisance factors (background, lighting, frequent but label-irrelevant details) and compress away subtle label-relevant cues.

2) With high-capacity encoder/decoder, the model can reconstruct well using a latent code that is not smooth or not aligned with semantic similarity; good reconstruction can coexist with a latent space where classes are entangled.

One modification:

Use a regularized or task-informed objective, e.g. a denoising autoencoder (train to reconstruct clean **x** from corrupted **x̃**) to encourage robust features, or add a supervised/contrastive term so that embeddings of same-class points are closer while different-class points are farther. Either changes the preservation criterion from “just reconstruct” toward “reconstruct robustly” or “preserve label structure.”

## Connections

Prerequisites you can lean on:

- •[Principal Component Analysis](/tech-tree/principal-component-analysis/)
- •[Neural Networks](/tech-tree/neural-networks/)

Natural next nodes this unlocks conceptually:

- •[Manifold Learning](/tech-tree/manifold-learning/)
- •[Metric Learning](/tech-tree/metric-learning/)
- •[Representation Learning](/tech-tree/representation-learning/)
- •[Variational Autoencoders](/tech-tree/variational-autoencoders/)
- •[UMAP](/tech-tree/umap/)
- •[Clustering](/tech-tree/clustering/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
