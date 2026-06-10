---
title: Clustering
description: K-means, hierarchical clustering. Unsupervised grouping.
date: '2026-07-01'
scheduled: '2027-01-19'
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
inspiration_url: https://templeton.host/tech-tree/clustering/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/clustering/](https://templeton.host/tech-tree/clustering/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Clustering

Machine LearningDifficulty: ★★★★☆Depth: 9Unlocks: 0

K-means, hierarchical clustering. Unsupervised grouping.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Cluster: a set of data points grouped because they are mutually more similar (closer) than to points in other clusters, as defined by a chosen distance/similarity
- -K-means objective: partition data into k clusters by minimizing the sum of squared distances from points to their cluster centroids (within-cluster variance)
- -Hierarchical clustering: produce a nested tree (dendrogram) of clusters by iteratively merging (agglomerative) or splitting (divisive) clusters using a linkage rule

## Key Symbols & Notation

k (number of clusters)mu\_j (centroid or prototype of cluster j)

## Essential Relationships

- -The chosen distance/similarity drives membership and structure: clustering algorithms operationalize this by either optimizing an objective (k-means: alternate nearest-centroid assignment and centroid-as-mean updates to reduce sum-of-squares) or by repeatedly merging/splitting based on pairwise distances and a linkage rule (hierarchical)

## Prerequisites (2)

[Machine Learning Introduction5 atoms](/tech-tree/ml-intro/)[Norms6 atoms](/tech-tree/norms/)

## Referenced by (3)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (3)

[customer segmentationBusiness

Customer segmentation is the canonical business application of clustering algorithms - K-means, hierarchical clustering, and density-based methods partition customers into groups by behavioral and demographic features](/business/customer-segmentation/)[target audienceBusiness

Target audience identification is fundamentally a segmentation problem - partitioning a population into groups by shared attributes. Clustering (k-means, hierarchical) is the direct mathematical technique for discovering these natural groupings in customer data.](/business/target-audience/)[targeted marketingBusiness

K-means and hierarchical clustering are the core mathematical techniques for customer segmentation - grouping customers into behaviorally or demographically similar clusters that can then be targeted with tailored marketing](/business/targeted-marketing/)

Advanced Learning Details

### Graph Position

123

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

9

Chain Length

### Cognitive Load

6

Atomic Elements

58

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (28)

- - k-means clustering as an algorithm that partitions data into k clusters by iteratively assigning points to centroids and updating centroids
- - centroid: the mean (arithmetic average) vector representing a cluster
- - assignment step (Lloyd's algorithm): assigning each point to the nearest centroid
- - update step (Lloyd's algorithm): recomputing each centroid as the mean of assigned points
- - k-means objective / within-cluster sum of squares (WCSS, inertia): the sum of squared distances from points to their cluster centroids
- - convergence behavior of k-means: monotonic decrease of the objective and convergence to a (local) optimum, not necessarily global
- - sensitivity to initialization and the need for good initialization methods
- - k-means++ initialization: a probabilistic initialization that spreads initial centroids using distance-proportional sampling
- - choice of k (number of clusters) as a model selection problem
- - elbow method for choosing k: plotting inertia vs k and looking for diminishing returns
- - silhouette score concept: per-point measure combining intra-cluster cohesion and nearest-cluster separation
- - hierarchical clustering: building a hierarchy of clusters instead of a flat partition
- - agglomerative (bottom-up) hierarchical clustering: start with points as clusters and iteratively merge
- - divisive (top-down) hierarchical clustering: start with all data in one cluster and iteratively split
- - dendrogram: tree representation of hierarchical clustering showing merge/split sequence and heights
- - linkage criteria (cluster-to-cluster distance definitions): single, complete, average, Ward
- - single linkage: cluster distance defined by the minimum pairwise distance between members
- - complete linkage: cluster distance defined by the maximum pairwise distance between members
- - average linkage: cluster distance defined by the average pairwise distance between members
- - Ward's linkage: merging chosen to minimize increase in total within-cluster variance (SSE)
- - cutting a dendrogram at a given height to obtain a flat clustering with a chosen number of clusters
- - k-medoids (PAM) and medoid concept: cluster representative is an actual data point (robust to outliers)
- - difference between centroid-based (k-means) and medoid-based (k-medoids) approaches regarding robustness
- - soft / fuzzy clustering concept (e.g., fuzzy c-means): points have fractional membership in multiple clusters
- - cluster validity indices beyond silhouette (examples and purpose): Davies–Bouldin index, Calinski–Harabasz index
- - assumptions and limitations of k-means: preference for roughly spherical, similarly sized clusters and sensitivity to outliers
- - effect of distance metric and linkage choice on resulting cluster shapes and structure
- - computational complexity / scalability considerations of common clustering algorithms (k-means, hierarchical)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

When you don’t have labels, clustering is the workhorse tool for discovering structure: it tries to answer “which points belong together?” using only a notion of similarity (distance).

TL;DR:

Clustering groups data points so that points in the same group are more similar than points in different groups. K-means does this by minimizing within-cluster squared distances to centroids μⱼ (fast, simple, but assumes roughly spherical clusters and needs k). Hierarchical clustering builds a dendrogram by repeatedly merging clusters using a linkage rule (more flexible shapes, but slower; you choose a cut level instead of k). Distance choice, scaling, initialization, and validation (e.g., silhouette) determine whether clusters are meaningful.

## What Is Clustering?

Clustering is an **unsupervised** learning task: you’re given data points **x**₁,…,**x**ₙ (no labels), and you want to group them into “clusters” so that points in the same group are “similar,” and points in different groups are “dissimilar.”

The key idea is that *clustering is not a single problem*—it’s a family of problems defined by choices you make:

1) **Representation**: what is a data point? (a vector **x** ∈ ℝᵈ? a document? an image embedding?)

2) **Similarity / distance**: how do we measure “close”? (‖**x**−**y**‖₂, cosine distance, etc.)

3) **Cluster model**: what does a cluster “look like”? (a centroid-based ball, a connected component, a hierarchy)

4) **Objective / procedure**: what criterion do we optimize or what rule do we follow?

A practical definition you can use:

- •A **cluster** is a set of points grouped because, under a chosen distance/similarity, they are more similar to one another than to points outside the set.

Notice what’s missing: there is no universal “correct” clustering without extra assumptions. Two different distance metrics can yield different but equally defensible clusterings.

### Why clustering is useful

Clustering shows up in many places because it provides structure without labels:

- •**Exploration**: discover subpopulations (customer segments, gene expression patterns)
- •**Compression / summarization**: represent many points by a few prototypes (centroids)
- •**Preprocessing**: create features like “cluster ID,” or initialize other models
- •**Anomaly detection**: points far from any cluster can be suspicious

### The geometry intuition

If your data are vectors in ℝᵈ, distance-based clustering is fundamentally geometric.

- •With Euclidean distance, clustering often assumes that “togetherness” means points form compact blobs.
- •But real data may have elongated, varying-density, or nested structures.

This is why we study **multiple clustering paradigms**. In this lesson, we’ll focus on two core methods:

- •**K-means** (centroid-based, objective-driven)
- •**Hierarchical clustering** (tree-building, linkage-driven)

We’ll also treat clustering as a pipeline: choose distance + scale features, run algorithm, then validate and interpret.

### Notation we’ll use

- •Data points: **x**ᵢ ∈ ℝᵈ, i = 1,…,n
- •Number of clusters: k
- •Cluster index: j = 1,…,k
- •Centroid (prototype) of cluster j: **μ**ⱼ ∈ ℝᵈ
- •Assignment of point i: cᵢ ∈ {1,…,k}

The major theme: clustering is about **optimizing or constructing** a grouping consistent with your similarity notion—and knowing when that grouping is trustworthy.

## Core Mechanic 1: K-means as an Optimization Problem

K-means is the classic centroid-based clustering algorithm. It is popular because it is simple, fast, and often surprisingly effective.

## Why K-means works (motivation first)

Suppose you believe each cluster can be summarized by a “typical” point—its centroid—and that points should belong to the cluster whose centroid is closest.

This belief translates into an objective: choose k centroids and assignments so that points are close to their assigned centroid.

## The K-means objective

Given assignments cᵢ and centroids **μ**ⱼ, the within-cluster sum of squares (WCSS) is:

J(c, μ) = ∑ᵢ ‖**x**ᵢ − **μ**\_{cᵢ}‖₂²

K-means solves:

minimize over assignments cᵢ and centroids **μ**ⱼ:

min J(c, μ) = ∑ᵢ ‖**x**ᵢ − **μ**\_{cᵢ}‖₂²

This is sometimes described as “minimizing within-cluster variance.”

### Why squared Euclidean distance?

- •Squaring strongly penalizes far-away points.
- •It yields a clean centroid update: the best centroid is the mean.
- •It leads to efficient alternating minimization.

But it also implies a geometric assumption: clusters are roughly **spherical** (balls) in Euclidean space.

## The two-step alternating minimization

K-means uses an iterative procedure (often called Lloyd’s algorithm):

1) **Assignment step (E-step-like):**

Fix centroids **μ**ⱼ. Assign each point to the nearest centroid:

cᵢ ← argminⱼ ‖**x**ᵢ − **μ**ⱼ‖₂²

2) **Update step (M-step-like):**

Fix assignments cᵢ. Update each centroid to the mean of points in that cluster:

**μ**ⱼ ← (1 / |Cⱼ|) ∑\_{i: cᵢ = j} **x**ᵢ

These steps repeat until assignments stop changing or the objective decreases only slightly.

### Show-your-work: why the centroid is the mean

Focus on one cluster j with points {**x**ᵢ : cᵢ = j}. We want **μ** that minimizes:

f(**μ**) = ∑\_{i: cᵢ=j} ‖**x**ᵢ − **μ**‖₂²

Expand using dot products:

‖**x**ᵢ − **μ**‖₂² = (**x**ᵢ − **μ**)·(**x**ᵢ − **μ**)

= **x**ᵢ·**x**ᵢ − 2 **x**ᵢ·**μ** + **μ**·**μ**

So

f(**μ**) = ∑ (**x**ᵢ·**x**ᵢ) − 2 ∑(**x**ᵢ·**μ**) + ∑(**μ**·**μ**)

Let m = |Cⱼ|. Note ∑(**μ**·**μ**) = m(**μ**·**μ**).

Take the gradient with respect to **μ**:

∇ f(**μ**) = -2 ∑ **x**ᵢ + 2 m **μ**

Set ∇ f(**μ**) = **0**:

-2 ∑ **x**ᵢ + 2 m **μ** = **0**

⇒ m **μ** = ∑ **x**ᵢ

⇒ **μ** = (1/m) ∑ **x**ᵢ

So the centroid update is not a heuristic—it is the exact minimizer of the squared-distance objective given fixed assignments.

## Convergence (what it guarantees and what it doesn’t)

Each iteration:

- •The assignment step does not increase J.
- •The update step does not increase J.

So J decreases monotonically and the algorithm converges in finitely many steps to a **local minimum**.

But:

- •The solution depends on initialization.
- •K-means can get stuck in poor local minima.

## Initialization and k-means++

Random initialization (choose k random points as initial **μ**ⱼ) can be unstable.

**k-means++** improves this by spreading initial centroids apart:

1) Pick one centroid uniformly from the data.

2) For each point **x**, compute D(**x**) = distance to nearest chosen centroid.

3) Choose next centroid with probability proportional to D(**x**)².

4) Repeat until k centroids are chosen.

This tends to reduce bad starts and usually improves results with minimal overhead.

## Choosing k (model selection)

K-means requires k upfront, which is often the hardest practical choice.

Common heuristics:

- •**Elbow method**: plot WCSS(k) = ∑ᵢ ‖**x**ᵢ − **μ**\_{cᵢ}‖₂² vs k. Look for a point where improvements diminish (“elbow”).
- •**Silhouette score**: compares within-cluster tightness vs separation.

### Silhouette score (intuition)

For a point i:

- •aᵢ = average distance to points in its own cluster
- •bᵢ = minimum (over other clusters) of average distance to that cluster

Silhouette:

sᵢ = (bᵢ − aᵢ) / max(aᵢ, bᵢ)

- •sᵢ ≈ 1: well-clustered
- •sᵢ ≈ 0: on the boundary
- •sᵢ < 0: possibly misassigned

Average sᵢ over i gives a score for k.

## Scaling features (often the make-or-break detail)

K-means uses Euclidean distance, so feature scaling matters.

If one feature has a large numeric range, it dominates distances.

Typical fix: standardize each feature:

x' = (x − mean) / std

Without scaling, you may cluster by “units” rather than by actual structure.

## When K-means is a good fit

- •Clusters are compact and roughly spherical in Euclidean geometry.
- •Similar cluster sizes and densities.
- •You want speed on large n.

## When K-means struggles

- •Non-spherical clusters (rings, spirals).
- •Unequal densities (dense + sparse).
- •Outliers (can drag centroids).
- •Categorical features without a meaningful Euclidean embedding.

K-means is a sharp tool—but it’s sharp in a particular shape. Next we’ll study hierarchical clustering, which often provides more flexibility and interpretability via a dendrogram.

## Core Mechanic 2: Hierarchical Clustering and Linkage Rules

Hierarchical clustering builds a **nested family of clusters** rather than committing to a single partition with a fixed k.

## Why hierarchical clustering (motivation)

Sometimes you don’t believe the data has one “correct” k. Instead, you might believe there are multiple meaningful scales:

- •At a coarse level: 2–3 big groups.
- •At a fine level: subtypes within each group.

Hierarchical clustering captures this by producing a **dendrogram** (a tree) that shows how clusters merge (or split) as you change the similarity threshold.

There are two main variants:

- •**Agglomerative** (bottom-up): start with each point as its own cluster, repeatedly merge.
- •**Divisive** (top-down): start with all points in one cluster, repeatedly split.

Agglomerative clustering is more common in practice, so we’ll focus on it.

## The agglomerative algorithm (conceptual steps)

1) Start with n clusters: { {1}, {2}, …, {n} }

2) Compute distances between clusters using a **linkage rule**

3) Merge the two closest clusters

4) Update distances and repeat until one cluster remains

The output is a dendrogram. To get a final clustering, you **cut** the dendrogram at a chosen height (distance threshold) or choose a number of clusters.

## Distances between clusters: linkage

Hierarchical clustering needs a distance between sets of points (clusters), not just between individual points.

Let A and B be two clusters.

Common linkage rules:

| Linkage | Cluster distance d(A,B) | Behavior / bias |
| --- | --- | --- |
| Single | min\_{**x**∈A, **y**∈B} ‖**x**−**y**‖ | Can create “chains”; finds elongated shapes |
| Complete | max\_{**x**∈A, **y**∈B} ‖**x**−**y**‖ | Prefers compact clusters; sensitive to outliers |
| Average | (1/( | A |  | B | )) ∑\_{**x**∈A}∑\_{**y**∈B} ‖**x**−**y**‖ | Balanced; less extreme |
| Ward | increase in within-cluster SSE after merge | Similar spirit to k-means; prefers spherical clusters |

### Ward’s linkage (connection to variance minimization)

Ward’s method chooses the merge that causes the smallest increase in total within-cluster sum of squares.

If you define the within-cluster SSE for a cluster C with centroid **μ**\_C:

SSE(C) = ∑\_{**x**∈C} ‖**x** − **μ**\_C‖₂²

Ward chooses to merge A and B that minimize:

Δ(A,B) = SSE(A∪B) − SSE(A) − SSE(B)

This makes hierarchical clustering feel more “k-means-like,” but it still yields a full hierarchy.

## Reading a dendrogram (what it actually tells you)

In a dendrogram:

- •Leaves are individual points.
- •A merge happens at a certain height h representing distance (or dissimilarity) at which the merge occurs.

A “natural” clustering often appears as:

- •many merges at low heights (tight subclusters)
- •then a noticeable jump to higher heights (merging distinct groups)

Cutting the tree at a height between those regimes yields a partition.

## Complexity and scaling

Hierarchical clustering is typically more expensive than k-means:

- •Naive implementations can be O(n³).
- •Common optimized implementations are around O(n²) time and O(n²) memory due to the distance matrix.

So it’s often used for:

- •smaller datasets (n up to a few tens of thousands, depending on memory)
- •scenarios where interpretability of the dendrogram is valuable

## Distance metrics still matter

Hierarchical clustering can use many distances:

- •Euclidean: ‖**x**−**y**‖₂
- •Manhattan: ‖**x**−**y**‖₁
- •Cosine distance: 1 − (**x**·**y**) / (‖**x**‖₂ ‖**y**‖₂)

Different distances can change the dendrogram dramatically. Scaling features is still crucial whenever numeric ranges differ.

## Strengths and weaknesses vs K-means

Hierarchical clustering:

- •does not require choosing k upfront
- •can reveal multi-scale structure
- •can work with many distance measures

But:

- •is slower and heavier in memory
- •can be sensitive to noise/outliers (especially complete linkage)
- •once a merge is done, it can’t be undone (greedy)

K-means:

- •scales well
- •is simple

But:

- •requires k upfront
- •assumes centroid-like clusters

You’ll often try both: use hierarchical clustering to understand structure (choose k), then run k-means for a scalable final partition.

## Application/Connection: A Practical Clustering Workflow (and How to Trust It)

Clustering algorithms always produce *some* grouping—even on random noise. The real skill is building a workflow that makes clusters meaningful and defensible.

## 1) Clarify the goal

Different goals imply different choices:

- •**Segmentation** (e.g., customers): interpretability matters; stable clusters matter.
- •**Compression** (e.g., vector quantization): objective value matters.
- •**Exploration** (e.g., embeddings): you want clusters that align with semantic neighborhoods.

Ask: what would count as a “good” cluster in your domain?

## 2) Choose a representation

Raw features might not reflect similarity.

Examples:

- •Text: TF-IDF vectors or embedding vectors
- •Images: CNN embeddings
- •Graph nodes: node embeddings

Clustering works best when your representation makes “similarity” meaningful geometrically.

## 3) Scale / normalize

If using Euclidean distance, scale each feature to comparable units.

Typical options:

| Method | Formula | When to use |
| --- | --- | --- |
| Standardization | x' = (x − mean)/std | Most common; good default |
| Min-max scaling | x' = (x − min)/(max − min) | When bounds matter |
| L2 normalization | **x**' = **x**/‖**x**‖₂ | For cosine-like comparisons on direction |

## 4) Pick an algorithm and distance

A useful mental map:

| If your clusters are… | Try… |
| --- | --- |
| compact blobs | K-means or Ward hierarchical |
| possibly elongated / connected | Single/average linkage hierarchical |
| you want multi-scale structure | hierarchical clustering |
| very large n | K-means (with k-means++) |

(There are other families like DBSCAN, GMMs, spectral clustering, but this node focuses on K-means + hierarchical.)

## 5) Choose k or a cut

### For K-means

- •Try several k values.
- •Use elbow + silhouette.
- •Check stability across random seeds.

### For hierarchical

- •Cut at a height where merges start jumping.
- •Or choose number of clusters by cutting to k leaves.

## 6) Validate: internal, stability, and external checks

Validation is not just a single number.

### Internal metrics (no labels)

- •**Silhouette**: compares cohesion vs separation.
- •**Davies–Bouldin**: lower is better (cluster scatter vs separation).

Internal metrics can be misleading if your distance metric doesn’t match your semantic goal.

### Stability checks

Run clustering under perturbations:

- •different random seeds (k-means)
- •bootstrap samples
- •small noise added to features

If cluster assignments drastically change, the structure may be weak.

### External checks (domain-based)

Even without labels, you can often check:

- •Are clusters interpretable? (summary statistics)
- •Do clusters correlate with known attributes? (e.g., geography, device type)
- •Are clusters actionable? (different behaviors, different outcomes)

## 7) Interpret clusters

For each cluster j, compute:

- •size |Cⱼ|
- •centroid **μ**ⱼ
- •feature means / medians
- •representative points (closest to **μ**ⱼ)

Interpretation is often the main product of clustering.

## 8) Common failure modes (so you can detect them)

- •**Scaling failure**: one feature dominates distance.
- •**Wrong k**: k too small merges distinct groups; k too large fragments groups.
- •**Outliers**: centroids pulled; complete linkage distorted.
- •**Non-spherical geometry**: K-means splits one curved cluster into multiple.
- •**High-dimensional distance concentration**: distances become similar; clusters less distinct.

A practical mitigation in high dimensions is to reduce dimension first (e.g., PCA) for clustering—carefully, because projections can also distort structure.

## Connection between K-means and hierarchical (a useful mental bridge)

- •K-means optimizes a fixed-k objective (SSE).
- •Ward hierarchical greedily merges clusters to control SSE increases.

So if you think “variance within clusters” is the right notion, both methods can align:

- •Use Ward dendrogram to pick k.
- •Then run K-means with that k for scalability.

The core professional habit: treat clustering as *an iterative scientific process*, not a one-click algorithm.

## Worked Examples (3)

### K-means on a tiny 2D dataset (one full iteration, with real numbers)

Data points in ℝ²:

**x**₁=(1,1), **x**₂=(1,2), **x**₃=(4,4), **x**₄=(5,4)

Choose k=2. Initialize centroids:

**μ**₁=(1,1), **μ**₂=(5,4). Use squared Euclidean distance.

1. Assignment step: compute ‖**x**ᵢ−**μ**ⱼ‖₂².

   For **x**₁=(1,1):

   ‖(1,1)−(1,1)‖² = 0

   ‖(1,1)−(5,4)‖² = (−4)²+(−3)² = 16+9 = 25

   ⇒ c₁=1.

   For **x**₂=(1,2):

   ‖(1,2)−(1,1)‖² = 0²+1² = 1

   ‖(1,2)−(5,4)‖² = (−4)²+(−2)² = 16+4 = 20

   ⇒ c₂=1.

   For **x**₃=(4,4):

   ‖(4,4)−(1,1)‖² = 3²+3² = 9+9 = 18

   ‖(4,4)−(5,4)‖² = (−1)²+0² = 1

   ⇒ c₃=2.

   For **x**₄=(5,4):

   ‖(5,4)−(1,1)‖² = 4²+3² = 16+9 = 25

   ‖(5,4)−(5,4)‖² = 0

   ⇒ c₄=2.
2. Update step: recompute centroids as the mean of assigned points.

   Cluster 1 has **x**₁, **x**₂:

   **μ**₁ ← ( (1,1) + (1,2) ) / 2 = ( (2,3) ) / 2 = (1, 1.5)

   Cluster 2 has **x**₃, **x**₄:

   **μ**₂ ← ( (4,4) + (5,4) ) / 2 = ( (9,8) ) / 2 = (4.5, 4)
3. Objective after update (optional check):

   J = ∑ᵢ ‖**x**ᵢ − **μ**\_{cᵢ}‖²

   For cluster 1 with **μ**₁=(1,1.5):

   ‖(1,1)−(1,1.5)‖² = 0²+(−0.5)² = 0.25

   ‖(1,2)−(1,1.5)‖² = 0²+(0.5)² = 0.25

   For cluster 2 with **μ**₂=(4.5,4):

   ‖(4,4)−(4.5,4)‖² = (−0.5)²+0² = 0.25

   ‖(5,4)−(4.5,4)‖² = (0.5)²+0² = 0.25

   Total J = 1.0

**Insight:** K-means alternates between “nearest centroid” assignments and “mean of assigned points” updates. The arithmetic mean appears because it exactly minimizes the sum of squared Euclidean distances within each cluster.

### Why feature scaling changes the clustering (distance domination example)

Two features: height (cm) and income (USD). Consider two people:

A: (170 cm, 50,000)

B: (180 cm, 50,500)

C: (171 cm, 120,000)

Use Euclidean distance on raw features vs standardized features.

1. Raw distances:

   Between A and B:

   Δheight=10, Δincome=500

   ‖A−B‖₂ = √(10² + 500²) = √(100 + 250,000) = √250,100 ≈ 500.10

   Between A and C:

   Δheight=1, Δincome=70,000

   ‖A−C‖₂ = √(1² + 70,000²) ≈ 70,000.00
2. Observation: income dwarfs height.

   Even a 10 cm difference barely matters compared to $500.

   So clustering will be driven almost entirely by income scale, not necessarily by what you intend.
3. Standardize each feature (conceptually):

   Let height'=(height−mean)/std\_height and income'=(income−mean)/std\_income.

   After standardization, typical variations in height and income become comparable (unitless).
4. Resulting effect:

   Distances become sensitive to both features.

   Now A is close to C in height, but far in income; whether A clusters with B or C depends on relative standardized differences, not raw units.

**Insight:** Clustering is only as meaningful as your distance metric—and Euclidean distance is extremely sensitive to feature scale. Standardization is often not optional; it defines what “similar” means.

### Agglomerative hierarchical clustering by hand (single linkage on 1D points)

Points on a line (ℝ¹): {0, 2, 3, 10}. Use single linkage with Euclidean distance. Build the merge sequence and interpret a dendrogram cut.

1. Start with singleton clusters:

   {0}, {2}, {3}, {10}

   Pairwise point distances:

   |0−2|=2, |0−3|=3, |0−10|=10

   |2−3|=1, |2−10|=8

   |3−10|=7
2. Single linkage distance between clusters is the minimum pairwise distance.

   Closest pair is {2} and {3} with distance 1.

   Merge:

   C₁ = {2,3} at height 1.

   Now clusters: {0}, {2,3}, {10}
3. Compute distances:

   d({0},{2,3}) = min(|0−2|,|0−3|)=min(2,3)=2

   d({10},{2,3}) = min(|10−2|,|10−3|)=min(8,7)=7

   d({0},{10}) = 10

   Closest is {0} and {2,3} at distance 2.

   Merge:

   C₂ = {0,2,3} at height 2.

   Now clusters: {0,2,3}, {10}
4. Final merge:

   d({0,2,3},{10}) = min(|10−0|,|10−2|,|10−3|)=min(10,8,7)=7

   Merge at height 7.

   Dendrogram heights: 1, 2, 7.
5. Interpretation by cutting:

   If you cut at height between 2 and 7 (e.g., 4), you get 2 clusters:

   {0,2,3} and {10}.

   If you cut below 2 (e.g., 1.5), you get 3 clusters:

   {0}, {2,3}, {10}.

**Insight:** Hierarchical clustering gives you a *family* of clusterings. The linkage rule controls the geometry: single linkage tends to merge via nearest neighbors, which can produce chained clusters.

## Key Takeaways

- ✓

  Clustering is defined by a triangle of choices: representation, distance/similarity, and clustering objective/procedure.
- ✓

  K-means minimizes J = ∑ᵢ ‖**x**ᵢ − **μ**\_{cᵢ}‖₂² via alternating assignment (nearest centroid) and update (**μ**ⱼ = mean of assigned points).
- ✓

  K-means converges to a local minimum; initialization matters (k-means++ is a strong default).
- ✓

  Feature scaling often determines the result because Euclidean distance is scale-sensitive.
- ✓

  Hierarchical clustering builds a dendrogram via greedy merges; you choose a cut (height or number of clusters) after seeing the structure.
- ✓

  Linkage rules (single/complete/average/Ward) encode different biases about what clusters should look like.
- ✓

  Validation should include more than a single metric: combine silhouette/elbow with stability and domain interpretability checks.
- ✓

  No clustering is ‘correct’ without assumptions; the goal is a useful, stable grouping aligned with your notion of similarity.

## Common Mistakes

- ✗

  Running K-means on unscaled features and interpreting the output as meaningful structure.
- ✗

  Assuming the algorithm discovered “true categories” rather than a partition induced by your distance metric and model assumptions.
- ✗

  Choosing k by eyeballing one run instead of checking multiple initializations and using a validation approach (silhouette, stability).
- ✗

  Using hierarchical clustering on very large n without considering O(n²) memory/time costs (distance matrix blow-up).

## Practice

easy

You have points **x**₁=(0,0), **x**₂=(0,1), **x**₃=(5,5), **x**₄=(6,5). Run one full K-means iteration with k=2 starting from **μ**₁=(0,0), **μ**₂=(6,5). Give assignments and updated centroids.

**Hint:** Compute squared distances to each centroid, assign each point to the closer one, then average points in each cluster to update **μ**ⱼ.

Show solution

Assignments by squared distance:

**x**₁ to **μ**₁ (0 vs large)

**x**₂ to **μ**₁ (1 vs large)

**x**₃ to **μ**₂ (distance to (6,5) is 1; to (0,0) is 50)

**x**₄ to **μ**₂ (0 vs 61)

Updated centroids:

**μ**₁ = ((0,0)+(0,1))/2 = (0, 0.5)

**μ**₂ = ((5,5)+(6,5))/2 = (5.5, 5)

medium

For hierarchical clustering, explain (in 2–4 sentences) how single linkage and complete linkage can produce different cluster shapes. Then give one scenario where single linkage is a poor choice.

**Hint:** Think about min vs max distances between points across clusters, and how a single ‘bridge’ point can connect groups.

Show solution

Single linkage uses d(A,B)=min distance between points, so clusters can merge through nearest-neighbor chains and form long, thin shapes. Complete linkage uses d(A,B)=max distance, which discourages merges that would create large diameters and thus prefers compact clusters. Single linkage is a poor choice when noise points create ‘bridges’ between two real groups, causing them to chain together into one cluster.

hard

Derive the K-means centroid update: show that **μ** that minimizes f(**μ**) = ∑\_{i=1}^m ‖**x**ᵢ − **μ**‖₂² is the mean (1/m)∑ᵢ **x**ᵢ.

**Hint:** Expand the squared norm, take ∇ with respect to **μ**, set it to **0**, and solve for **μ**.

Show solution

f(**μ**) = ∑ᵢ (**x**ᵢ−**μ**)·(**x**ᵢ−**μ**) = ∑ᵢ (**x**ᵢ·**x**ᵢ) − 2∑ᵢ(**x**ᵢ·**μ**) + ∑ᵢ(**μ**·**μ**).

Let m be the number of points. Then ∑ᵢ(**μ**·**μ**) = m(**μ**·**μ**).

Take gradient:

∇f(**μ**) = -2∑ᵢ **x**ᵢ + 2m**μ**.

Set ∇f(**μ**) = **0**:

-2∑ᵢ **x**ᵢ + 2m**μ** = **0** ⇒ m**μ** = ∑ᵢ **x**ᵢ ⇒ **μ** = (1/m)∑ᵢ **x**ᵢ.

## Connections

[Machine Learning Introduction](/tech-tree/ml-intro/)

[Norms](/tech-tree/norms/)

[Principal Component Analysis (PCA)](/tech-tree/pca/)

[Gaussian Mixture Models](/tech-tree/gmm/)

[DBSCAN](/tech-tree/dbscan/)

[Silhouette Score and Cluster Validation](/tech-tree/cluster-validation/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
