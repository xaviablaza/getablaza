---
title: Spectral Graph Theory
description: Graph properties from eigenvalues of adjacency/Laplacian matrices.
date: '2026-07-01'
scheduled: '2027-01-26'
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
inspiration_url: https://templeton.host/tech-tree/spectral-graph-theory/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/spectral-graph-theory/](https://templeton.host/tech-tree/spectral-graph-theory/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Spectral Graph Theory

Graph TheoryDifficulty: ★★★★☆Depth: 5Unlocks: 0

Graph properties from eigenvalues of adjacency/Laplacian matrices.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Adjacency and degree matrices as linear encodings of a graph's structure
- -Graph Laplacian (combinatorial): L = D - A as the central matrix for cuts/flows
- -Spectrum: the multiset of eigenvalues (and associated eigenvectors) of those graph matrices as descriptive invariants

## Key Symbols & Notation

A (adjacency matrix)L (graph Laplacian, L = D - A)

## Essential Relationships

- -For L, the multiplicity of the eigenvalue 0 equals the number of connected components; in particular the second-smallest eigenvalue (the algebraic connectivity) is >0 iff the graph is connected

## Prerequisites (2)

[Eigenvalues and Eigenvectors6 atoms](/tech-tree/eigenvalues/)[Graph Representations6 atoms](/tech-tree/graph-representations/)

Advanced Learning Details

### Graph Position

74

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

5

Chain Length

### Cognitive Load

6

Atomic Elements

51

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (18)

- - Degree matrix D: diagonal matrix with vertex degrees on the diagonal
- - Combinatorial Laplacian L = D - A (matrix capturing graph connectivity via degree minus adjacency)
- - Normalized Laplacians: symmetric normalized Laplacian L\_sym = I - D^{-1/2} A D^{-1/2} and random-walk Laplacian L\_rw = I - D^{-1} A
- - Spectrum of a graph: the multiset of eigenvalues of a graph-associated matrix (e.g., A, L, L\_sym)
- - Spectral radius ρ(A): the largest (by magnitude) eigenvalue of the adjacency matrix
- - Algebraic connectivity (Fiedler value): the second-smallest eigenvalue λ2 of the combinatorial Laplacian
- - Fiedler vector: the eigenvector corresponding to the Laplacian's λ2
- - Spectral gap: difference between selected eigenvalues (e.g., λ2 and λ1 or between largest and second-largest adjacency eigenvalues), used as a measure of connectivity/mixing
- - Multiplicity of eigenvalues as structural indicator (e.g., multiplicity of 0 for Laplacian)
- - Conductance (also called edge expansion) φ(S) of a vertex set S and graph conductance Φ(G) as a measure of bottlenecks
- - Matrix-Tree Theorem (spectral form): counting spanning trees from Laplacian eigenvalues/cofactors
- - Spectral clustering / spectral partitioning: using eigenvectors of graph matrices (typically Laplacian) to find graph cuts/communities
- - Cospectral graphs: non-isomorphic graphs that share the same spectrum for a chosen graph matrix
- - Eigenvalue interlacing: the interleaving relationship between eigenvalues of a matrix and those of principal submatrices (used for subgraphs/quotients)
- - Relationship between matrix powers and walks: entries of A^k count walks and traces of A^k relate to sums of eigenvalue powers
- - Random-walk transition matrix P = D^{-1} A and its spectral interpretation for mixing and stationary distribution
- - Bounds linking eigenvalues and degree statistics (e.g., sum/traces of eigenvalues, bounds of λ\_max by degrees)
- - Symmetry properties of the adjacency spectrum for special graph classes (e.g., bipartite graphs produce symmetric spectra about zero)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Graphs look discrete—just nodes and edges—but many of their most important properties become visible only when you translate the graph into a matrix and study its eigenvalues. Spectral graph theory is the toolkit that makes that translation precise: connectivity, expansion, random-walk mixing, and good graph partitions all leave signatures in the spectrum of the adjacency matrix and (especially) the graph Laplacian.

TL;DR:

Encode a graph with matrices like the adjacency matrix A and Laplacian L = D − A (or normalized variants). Because these matrices are symmetric for undirected graphs, their eigenvalues are real and their eigenvectors form an orthonormal basis. The smallest Laplacian eigenvalues describe connected components and “how connected” the graph is (algebraic connectivity), while specific eigenvectors (Fiedler vector) guide spectral partitioning. For expansion, the normalized Laplacian spectrum relates to conductance via Cheeger-type inequalities. Random walks connect through the random-walk Laplacian and Markov chain stationary distributions.

## Prerequisites and where they will be used (read this first)

This node assumes you already know basic eigenvalues/eigenvectors (Av=λvA\mathbf{v}=\lambda\mathbf{v}Av=λv) and graph representations. For spectral graph theory, a few extra prerequisites matter a lot; this section makes them explicit and flags where each appears.

## Linear algebra prerequisites

1) **Symmetric eigendecomposition** (for real symmetric matrices)

- •Fact: If MMM is real symmetric, it has real eigenvalues and an orthonormal eigenbasis. You can write M=QΛQ⊤M = Q\Lambda Q^\topM=QΛQ⊤.
- •Where used: All core matrices for **undirected** graphs (adjacency AAA, Laplacian LLL, normalized Laplacian L\mathcal{L}L) are symmetric, so we can order eigenvalues and reason variationally.

2) **Quadratic forms** and **positive semidefinite (PSD)** matrices

- •Fact: MMM is PSD iff x⊤Mx≥0\mathbf{x}^\top M\mathbf{x} \ge 0x⊤Mx≥0 for all **x**.
- •Where used: LLL and L\mathcal{L}L are PSD; this underpins why eigenvalues are nonnegative and why minimization problems make sense.

3) **Rayleigh quotient** and the **min–max principle**

- •Rayleigh quotient: RM(x)=x⊤Mxx⊤xR\_M(\mathbf{x}) = \frac{\mathbf{x}^\top M\mathbf{x}}{\mathbf{x}^\top \mathbf{x}}RM​(x)=x⊤xx⊤Mx​.
- •Min–max (informal): eigenvalues can be characterized as constrained minima/maxima of Rayleigh quotients.
- •Where used: We interpret eigenvalues as “best possible” values of energy objectives, and connect λ2\lambda₂λ2​ to cuts/partitions.

## Graph theory prerequisites

1) **Undirected vs directed**, **unweighted vs weighted** graphs

- •Many results here assume **undirected** graphs. Weighted edges are allowed but must be symmetric: wij=wjiw\_{ij}=w\_{ji}wij​=wji​.
- •Where used: Definitions of AAA, DDD, LLL, and properties like symmetry/PSD depend on undirectedness.

2) **Connected components**

- •You should know what it means for a graph to have kkk connected components.
- •Where used: Multiplicity of the eigenvalue 0 of the Laplacian equals the number of components.

3) **Cuts** and **volumes**

- •Cut: edges crossing between SSS and Sˉ\bar SSˉ.
- •Volume: vol(S)=∑i∈Sdi\mathrm{vol}(S)=\sum\_{i\in S} d\_ivol(S)=∑i∈S​di​.
- •Where used: Conductance/expansion, Cheeger inequalities, and spectral partitioning.

## Probability / Markov chain prerequisites (for the random-walk parts)

1) **Markov chains** on graphs: transition matrix PPP

- •Standard random walk: from node iii, move to neighbor jjj with probability wij/diw\_{ij}/d\_iwij​/di​.
- •Where used: The random-walk Laplacian and mixing relate to eigenvalues.

2) **Stationary distribution**

- •For an undirected connected graph, stationary distribution is πi=di/vol(V)\pi\_i = d\_i/\mathrm{vol}(V)πi​=di​/vol(V).
- •Where used: Normalization choices and conductance definitions rely on this measure.

If any of these are shaky, it’s worth a quick review before continuing—spectral graph theory is powerful, but it’s also picky about definitions (especially which Laplacian and which conductance).

## What Is Spectral Graph Theory?

Spectral graph theory studies graphs through the eigenvalues and eigenvectors (the **spectrum**) of matrices that encode graph structure.

At a high level, the workflow is:

1) Start with a graph G=(V,E)G=(V,E)G=(V,E) (possibly weighted).

2) Build a matrix representation like the adjacency matrix AAA or a Laplacian.

3) Analyze eigenvalues/eigenvectors of that matrix.

4) Translate spectral facts back into graph properties: connectivity, clustering, expansion, random-walk behavior, and more.

Why this is even plausible: eigenvectors provide “global coordinates” on the vertices. If a graph has two clusters with sparse connections between them, there tends to exist a vector **x** that is roughly constant on each cluster but differs between clusters. When you apply a graph matrix to **x**, the result changes little if edges mostly connect equal values. This idea becomes a quadratic form: edges penalize differences.

## The main matrices

### Adjacency matrix AAA

For a graph with nnn vertices (labeled 1…n),

- •Unweighted: Aij=1A\_{ij}=1Aij​=1 if (i,j)∈E(i,j)\in E(i,j)∈E, else 0.
- •Weighted: Aij=wijA\_{ij}=w\_{ij}Aij​=wij​.

For undirected graphs, AAA is symmetric.

Adjacency spectra are great for: regular graphs, counting walks, and global “density/structure” signals. But for cuts, flows, and random walks, Laplacians are often more natural.

### Degree matrix DDD

DDD is diagonal with Dii=di=∑jAijD\_{ii}=d\_i=\sum\_j A\_{ij}Dii​=di​=∑j​Aij​ (weighted degree if weighted).

### Combinatorial Laplacian LLL

L=D−A.L = D - A.L=D−A.

This is the central object for many connectivity and cut problems.

### Normalized Laplacian L\mathcal{L}L (important!)

There are two common Laplacians beyond LLL:

1) **Symmetric normalized Laplacian**

L=D−1/2LD−1/2=I−D−1/2AD−1/2.\mathcal{L} = D^{-1/2} L D^{-1/2} = I - D^{-1/2} A D^{-1/2}.L=D−1/2LD−1/2=I−D−1/2AD−1/2.

This is symmetric (for undirected graphs with positive degrees).

2) **Random-walk Laplacian**

Lrw=D−1L=I−D−1A=I−P,L\_{\text{rw}} = D^{-1}L = I - D^{-1}A = I - P,Lrw​=D−1L=I−D−1A=I−P,

where P=D−1AP=D^{-1}AP=D−1A is the random-walk transition matrix. LrwL\_{\text{rw}}Lrw​ is generally not symmetric, but it is similar to L\mathcal{L}L and thus shares eigenvalues.

## What “spectrum” means

The **spectrum** of a matrix is the multiset of its eigenvalues:

- •For LLL, we typically order them: $0=\lambda\_1 \le \lambda\_2 \le \cdots \le \lambda\_n$.
- •For L\mathcal{L}L: $0=\nu\_1 \le \nu\_2 \le \cdots \le \nu\_n \le 2$.

Eigenvectors matter too, especially for algorithms: the eigenvector associated with λ2\lambda\_2λ2​ (or ν2\nu\_2ν2​) often reveals a good partition.

A key mindset shift: spectral information is not just a “summary.” Many graph optimization problems (like finding a minimum cut under balance constraints) are hard combinatorial problems. Spectral methods relax them into continuous problems solvable by eigenvectors.

## Core mechanic 1: Laplacian energy, PSD-ness, and what eigenvalues measure

The combinatorial Laplacian L=D−AL=D-AL=D−A is more than a definition—it encodes a geometry on the graph.

## Laplacian as an “edge difference” operator

Take any vector **x** ∈ ℝⁿ assigning a scalar xix\_ixi​ to each vertex iii. Consider the quadratic form:

x⊤Lx.\mathbf{x}^\top L\mathbf{x}.x⊤Lx.

Expand it step by step (undirected, weighted case; assume Aij=wij=wjiA\_{ij}=w\_{ij}=w\_{ji}Aij​=wij​=wji​):

\begin{align\*}

\mathbf{x}^\top L\mathbf{x}

&= \mathbf{x}^\top (D-A)\mathbf{x}\\

&= \mathbf{x}^\top D\mathbf{x} - \mathbf{x}^\top A\mathbf{x}\\

&= \sum\_i d\_i x\_i^2 - \sum\_{i,j} w\_{ij} x\_i x\_j.

\end{align\*}

Now rewrite the second term using symmetry:

\begin{align\*}

\sum\_{i,j} w\_{ij} x\_i x\_j

&= \sum\_{i<j} w\_{ij}(x\_i x\_j + x\_j x\_i) + \sum\_i w\_{ii}x\_i^2\\

&= 2\sum\_{i<j} w\_{ij}x\_i x\_j \quad (\text{usually } w\_{ii}=0).

\end{align\*}

Also note:

∑idixi2=∑i(∑jwij)xi2=∑i,jwijxi2.\sum\_i d\_i x\_i^2 = \sum\_i \left(\sum\_j w\_{ij}\right)x\_i^2 = \sum\_{i,j} w\_{ij} x\_i^2.i∑​di​xi2​=i∑​(j∑​wij​)xi2​=i,j∑​wij​xi2​.

So

\begin{align\*}

\mathbf{x}^\top L\mathbf{x}

&= \sum\_{i,j} w\_{ij} x\_i^2 - \sum\_{i,j} w\_{ij} x\_i x\_j\\

&= \frac{1}{2}\sum\_{i,j} w\_{ij}(x\_i^2 - 2x\_i x\_j + x\_j^2)\\

&= \frac{1}{2}\sum\_{i,j} w\_{ij}(x\_i - x\_j)^2.

\end{align\*}

**Interpretation:** x⊤Lx\mathbf{x}^\top L\mathbf{x}x⊤Lx is the total “edge disagreement energy.” It’s small when neighboring vertices have similar values.

## PSD and nonnegative eigenvalues

From

x⊤Lx=12∑i,jwij(xi−xj)2≥0,\mathbf{x}^\top L\mathbf{x} = \frac{1}{2}\sum\_{i,j} w\_{ij}(x\_i-x\_j)^2 \ge 0,x⊤Lx=21​i,j∑​wij​(xi​−xj​)2≥0,

we immediately get: LLL is PSD, hence all eigenvalues satisfy λi≥0\lambda\_i\ge 0λi​≥0.

## Why the smallest eigenvalue is 0

If **x** is constant, say xi=cx\_i=cxi​=c for all iii, then every difference xi−xj=0x\_i-x\_j=0xi​−xj​=0, so

L1=0,λ1=0.L\mathbf{1}=\mathbf{0}, \quad \lambda\_1=0.L1=0,λ1​=0.

Thus 0 is always an eigenvalue with eigenvector **1**.

## Connected components and multiplicity of 0

If the graph has kkk connected components, you can build kkk linearly independent vectors that are constant on one component and 0 elsewhere. Each has zero energy, so each lies in the nullspace of LLL.

**Theorem:** The multiplicity of eigenvalue 0 of LLL equals the number of connected components.

This is one of the cleanest examples of “graph property ↔ eigenvalues.”

## Algebraic connectivity and the Fiedler value

The second-smallest eigenvalue λ2\lambda\_2λ2​ (for a connected graph) is called the **algebraic connectivity**.

- •If λ2\lambda\_2λ2​ is **tiny**, the graph is “almost disconnected”: there exists a vector **x** orthogonal to **1** that changes little across edges, suggesting a sparse cut.
- •If λ2\lambda\_2λ2​ is **large**, every non-constant assignment must pay energy across many edges, suggesting strong connectivity.

Variationally,

λ2=min⁡x≠0, x⊥1x⊤Lxx⊤x.\lambda\_2 = \min\_{\mathbf{x}\neq 0,\ \mathbf{x}\perp \mathbf{1}} \frac{\mathbf{x}^\top L\mathbf{x}}{\mathbf{x}^\top \mathbf{x}}.λ2​=x=0, x⊥1min​x⊤xx⊤Lx​.

This is where Rayleigh quotient/min–max enters: λ2\lambda\_2λ2​ is the best (smallest) achievable energy among vectors orthogonal to constants.

## Normalized Laplacian energy (why normalization matters)

Combinatorial LLL treats every vertex value equally in the denominator x⊤x\mathbf{x}^\top \mathbf{x}x⊤x. But for irregular graphs, high-degree vertices can dominate behavior.

The symmetric normalized Laplacian L=D−1/2LD−1/2\mathcal{L}=D^{-1/2}LD^{-1/2}L=D−1/2LD−1/2 has quadratic form

y⊤Ly=12∑i,jwij(yidi−yjdj)2.\mathbf{y}^\top \mathcal{L}\mathbf{y} = \frac{1}{2}\sum\_{i,j} w\_{ij}\left(\frac{y\_i}{\sqrt{d\_i}}-\frac{y\_j}{\sqrt{d\_j}}\right)^2.y⊤Ly=21​i,j∑​wij​(di​​yi​​−dj​​yj​​)2.

This makes “differences” comparable relative to degrees. Many expansion and random-walk results (including Cheeger-type inequalities) are stated for L\mathcal{L}L.

A practical rule:

- •Use **$L$** for physics-style diffusion on uniformly weighted nodes, some cut relaxations, and when degrees are comparable.
- •Use **$\mathcal{L}$** (or LrwL\_{\text{rw}}Lrw​) when degrees vary a lot, or when your objective is tied to random walks / conductance.

## Core mechanic 2: Cuts, conductance, and spectral partitioning (with the correct Cheeger setting)

A central algorithmic use of spectral graph theory is to find a “good” partition of the vertices: two groups with few edges between them but each group not too small.

## From cuts to an optimization problem

For a subset S⊂VS \subset VS⊂V (nonempty, not all vertices), define:

- •Cut weight:

cut(S,Sˉ)=∑i∈S, j∈Sˉwij.\mathrm{cut}(S,\bar S)=\sum\_{i\in S,\ j\in \bar S} w\_{ij}.cut(S,Sˉ)=i∈S, j∈Sˉ∑​wij​.

- •Volume:

vol(S)=∑i∈Sdi.\mathrm{vol}(S)=\sum\_{i\in S} d\_i.vol(S)=i∈S∑​di​.

A widely used balanced-separation score is **conductance**:

ϕ(S)=cut(S,Sˉ)min⁡{vol(S), vol(Sˉ)}.\phi(S)=\frac{\mathrm{cut}(S,\bar S)}{\min\{\mathrm{vol}(S),\ \mathrm{vol}(\bar S)\}}.ϕ(S)=min{vol(S), vol(Sˉ)}cut(S,Sˉ)​.

And the graph conductance is

ϕ(G)=min⁡Sϕ(S).\phi(G)=\min\_{S} \phi(S).ϕ(G)=Smin​ϕ(S).

This definition is the one that matches the standard Cheeger inequality for the **normalized Laplacian**.

## Why normalization appears

If you use a raw cut size cut(S,Sˉ)\mathrm{cut}(S,\bar S)cut(S,Sˉ) alone, you can get trivial answers: isolate a single low-degree vertex. Conductance normalizes by volume, which corresponds to probability mass under the random-walk stationary distribution πi=di/vol(V)\pi\_i=d\_i/\mathrm{vol}(V)πi​=di​/vol(V).

## Indicator vectors and the relaxation idea

Suppose you want a cut. A discrete way is an indicator vector **f** where

- •fi=1f\_i = 1fi​=1 if i∈Si\in Si∈S
- •fi=0f\_i = 0fi​=0 if i∉Si\notin Si∈/S.

But optimizing over such discrete vectors is hard. Spectral methods **relax** the problem: allow **f** to be real-valued, solve a continuous minimization, then “round” back to a set by thresholding.

This is where eigenvectors enter: the minimizing relaxed vector is an eigenvector.

## The normalized Laplacian and the second eigenvalue

Let $0=\nu\_1\le \nu\_2\le\cdots\le\nu\_nbeeigenvaluesof be eigenvalues of beeigenvaluesof\mathcal{L}$.

- •ν2\nu\_2ν2​ is small when there exists a set with small conductance.
- •ν2\nu\_2ν2​ is large when every set has large conductance (graph is an expander-like object).

### Cheeger inequality (normalized Laplacian version)

For the conductance definition above and L\mathcal{L}L:

ν22≤ϕ(G)≤2ν2.\frac{\nu\_2}{2} \le \phi(G) \le \sqrt{2\nu\_2}.2ν2​​≤ϕ(G)≤2ν2​​.

Important clarifications:

- •This statement is for the **normalized Laplacian** L\mathcal{L}L (equivalently the random-walk matrix PPP).
- •There are variants with slightly different constants depending on conventions.
- •The left inequality says: if ν2\nu\_2ν2​ is small, the graph must have a sparse cut.
- •The right inequality says: from the eigenvector of ν2\nu\_2ν2​, you can find a cut with conductance at most about ν2\sqrt{\nu\_2}ν2​​ (via a sweep/thresholding procedure).

## The Fiedler vector and sweep cuts

Let **u**₂ be an eigenvector for ν2\nu\_2ν2​ of L\mathcal{L}L (or equivalently for the second-largest eigenvalue of PPP). The spectral partitioning recipe:

1) Compute **u**₂.

2) Sort vertices by their coordinate in **u**₂ (or by u2,i/diu\_{2,i}/\sqrt{d\_i}u2,i​/di​​ depending on implementation).

3) Consider prefix sets SkS\_kSk​ consisting of the first kkk vertices in that order.

4) Compute conductance ϕ(Sk)\phi(S\_k)ϕ(Sk​) for each; choose the best.

This “sweep” is the rounding step that turns a continuous eigenvector into a discrete cut.

## Intuition: why the second eigenvector separates clusters

If the graph has two clusters weakly connected:

- •Values of **u**₂ tend to be nearly constant inside each cluster (low internal disagreement).
- •Values differ between clusters (to satisfy orthogonality constraints).

Thresholding separates the two sign/level regions.

## Adjacency spectrum vs Laplacian spectrum for clustering

Adjacency eigenvectors can also show community structure, especially in stochastic block models. But Laplacians are generally more robust for irregular degrees because they directly encode “difference across edges” and integrate naturally with random-walk normalization.

A useful comparison:

| Goal | Typical matrix | Why |
| --- | --- | --- |
| Connectivity / components | LLL or L\mathcal{L}L | Nullspace reveals components |
| Balanced sparse cut / expansion | L\mathcal{L}L | Cheeger inequality + conductance |
| Random walk mixing | PPP, LrwL\_{\text{rw}}Lrw​, L\mathcal{L}L | Markov chain eigenvalues control convergence |
| Regular graphs structure | AAA | Counts walks; eigenvalues relate to expansion in regular case |

Takeaway: when you see conductance/Markov chains, think **normalized** objects.

## Application/Connection: Random walks, mixing, and diffusion; plus a map of the landscape

Spectral graph theory isn’t just about partitions. The same matrices govern diffusion, random walks, and learning algorithms.

## Random walks and the transition matrix

For an undirected weighted graph, define

P=D−1A.P = D^{-1}A.P=D−1A.

Then Pij=wij/diP\_{ij}=w\_{ij}/d\_iPij​=wij​/di​ is the probability of moving from iii to jjj in one step.

- •PPP is row-stochastic (rows sum to 1).
- •If the graph is connected and non-bipartite (aperiodic), powers PtP^tPt converge to a rank-1 stationary behavior.

The stationary distribution is

πi=di∑kdk=divol(V).\pi\_i = \frac{d\_i}{\sum\_k d\_k} = \frac{d\_i}{\mathrm{vol}(V)}.πi​=∑k​dk​di​​=vol(V)di​​.

This is why volumes (sums of degrees) appear in conductance: they’re the natural “mass” under the walk.

## Spectral connection: PPP and L\mathcal{L}L share eigenvalues

Even though PPP is not symmetric, it is similar to a symmetric matrix:

D1/2PD−1/2=D1/2(D−1A)D−1/2=D−1/2AD−1/2.D^{1/2} P D^{-1/2} = D^{1/2}(D^{-1}A)D^{-1/2} = D^{-1/2} A D^{-1/2}.D1/2PD−1/2=D1/2(D−1A)D−1/2=D−1/2AD−1/2.

So PPP has real eigenvalues (for undirected graphs) and they match those of D−1/2AD−1/2D^{-1/2}AD^{-1/2}D−1/2AD−1/2.

Also,

L=I−D−1/2AD−1/2.\mathcal{L} = I - D^{-1/2} A D^{-1/2}.L=I−D−1/2AD−1/2.

So if μi\mu\_iμi​ are eigenvalues of D−1/2AD−1/2D^{-1/2}AD^{-1/2}D−1/2AD−1/2, then eigenvalues of L\mathcal{L}L are νi=1−μi\nu\_i = 1 - \mu\_iνi​=1−μi​.

## Mixing time and spectral gap (high-level)

Let $1=\mu\_1 \ge \mu\_2 \ge \cdots \ge \mu\_n \ge -1beeigenvaluesof be eigenvalues of beeigenvaluesofP(forconnectedgraphs, (for connected graphs, (forconnectedgraphs,\mu\_1=1$).

The **spectral gap** is often $1-\mu\_2(forlazywalksyouavoidnegativeeigenvaluesissues).Since (for lazy walks you avoid negative eigenvalues issues). Since (forlazywalksyouavoidnegativeeigenvaluesissues).Since\nu\_2 = 1-\mu\_2$, the second normalized Laplacian eigenvalue is exactly that gap.

Intuition:

- •If μ2\mu\_2μ2​ is close to 1 (small gap), the walk mixes slowly—there’s a bottleneck set with low conductance.
- •If μ2\mu\_2μ2​ is much smaller than 1 (large gap), mixing is fast—no severe bottlenecks.

This is the random-walk mirror of Cheeger: bottlenecks ↔ small ν2\nu\_2ν2​ ↔ slow mixing.

## Diffusion and Laplacian dynamics

In continuous-time diffusion on graphs, a common model is

dx(t)dt=−Lx(t).\frac{d\mathbf{x}(t)}{dt} = -L\mathbf{x}(t).dtdx(t)​=−Lx(t).

Solution uses the matrix exponential:

x(t)=e−tLx(0).\mathbf{x}(t)=e^{-tL}\mathbf{x}(0).x(t)=e−tLx(0).

Eigenvectors of LLL are the diffusion “modes”:

- •Small eigenvalues correspond to slow-decaying modes (large-scale structure).
- •Large eigenvalues decay quickly (fine-scale oscillations).

This perspective explains why low-frequency eigenvectors are used for embedding and clustering: they capture coarse geometry.

## A small “map” of related spectral objects

You’ll see several related matrices in practice:

| Object | Formula | Notes |
| --- | --- | --- |
| Adjacency | AAA | Symmetric for undirected; counts walks via AkA^kAk |
| Combinatorial Laplacian | L=D−AL=D-AL=D−A | PSD; components ↔ zero eigenvalues |
| Symmetric normalized Laplacian | L=I−D−1/2AD−1/2\mathcal{L}=I-D^{-1/2}AD^{-1/2}L=I−D−1/2AD−1/2 | Spectrum in [0,2][0,2][0,2]; Cheeger inequality |
| Random-walk matrix | P=D−1AP=D^{-1}AP=D−1A | Markov chain; eigenvalues relate to mixing |
| Random-walk Laplacian | Lrw=I−PL\_{\text{rw}}=I-PLrw​=I−P | Similar to L\mathcal{L}L |

## Where this shows up in ML and systems

- •**Spectral clustering**: compute a few eigenvectors of L\mathcal{L}L, embed nodes, run k-means.
- •**Graph embeddings**: Laplacian eigenmaps (manifold learning viewpoint).
- •**Network science**: expansion, robustness, community structure.
- •**Numerical methods**: solving linear systems in LLL (graph-based preconditioners), effective resistance.

Spectral graph theory is a hub: once you can move between graphs ↔ matrices ↔ eigen-objects, many results become variations on the same theme—energy minimization under constraints.

## Worked Examples (3)

### Compute L and its spectrum for a simple path graph on 3 vertices

Let G be the unweighted path 1—2—3. Build A, D, L = D − A, then compute eigenvalues to see how connectivity appears spectrally.

1. Adjacency matrix:

   A = [[0,1,0],

   [1,0,1],

   [0,1,0]]
2. Degrees: d₁=1, d₂=2, d₃=1 so

   D = diag(1,2,1).
3. Laplacian:

   L = D − A = [[ 1,-1, 0],

   [-1, 2,-1],

   [ 0,-1, 1]].
4. Check the always-true fact L**1**=0:

   L[1,1,1]ᵀ = [1−1+0, −1+2−1, 0−1+1]ᵀ = [0,0,0]ᵀ.

   So λ₁=0.
5. Compute remaining eigenvalues by characteristic polynomial det(L−λI)=0.

   L−λI = [[1−λ, -1, 0],

   [ -1, 2−λ, -1],

   [ 0, -1, 1−λ]].
6. Determinant expansion (use the first row):

   det(L−λI) = (1−λ)  *det([[2−λ, -1],[-1, 1−λ]]) − (−1)*  det([[-1, -1],[0, 1−λ]]).
7. Compute the 2×2 determinants:

   det([[2−λ, -1],[-1, 1−λ]]) = (2−λ)(1−λ) − 1.

   det([[-1, -1],[0, 1−λ]]) = (−1)(1−λ) − 0 = −(1−λ).
8. So:

   det(L−λI) = (1−λ)[(2−λ)(1−λ) − 1] + (1)[−(1−λ)]

   = (1−λ)[(2−λ)(1−λ) − 2].
9. Expand (2−λ)(1−λ)=2−3λ+λ².

   Then [(2−λ)(1−λ) − 2] = (2−3λ+λ²) − 2 = λ² − 3λ.
10. Thus det(L−λI) = (1−λ)(λ²−3λ) = (1−λ)λ(λ−3).
11. Eigenvalues are {0, 1, 3}.

    Because the graph is connected, 0 has multiplicity 1 (one component). The second eigenvalue λ₂=1 reflects nontrivial connectivity; if we made the middle edge very weak, λ₂ would drop toward 0.

**Insight:** Even in a tiny graph, λ₁=0 encodes components, and λ₂ (algebraic connectivity) quantifies how hard it is to separate the graph. The eigenvalues come from an energy perspective: vectors that vary across the single bottleneck edge pay disagreement energy.

### From the normalized Laplacian eigenvector to a sweep cut (conceptual walk-through)

You have computed the second eigenvector **u**₂ of the symmetric normalized Laplacian 𝓛 for an undirected graph. Show how to obtain a cut and how conductance is evaluated during the sweep.

1. Assume degrees are all positive so 𝓛 is well-defined: 𝓛 = I − D^{-1/2} A D^{-1/2}.
2. Compute (or are given) the eigenvector **u**₂ corresponding to ν₂, the second-smallest eigenvalue of 𝓛.
3. Convert to a degree-aware ordering statistic. A common choice is:

   score(i) = u₂,i / √d\_i.

   (This aligns with the fact that 𝓛’s geometry weights by degree.)
4. Sort vertices so that score(v₁) ≤ score(v₂) ≤ ... ≤ score(v\_n).
5. For each k = 1,...,n−1 define S\_k = {v₁,...,v\_k}.
6. For each S\_k compute:

   cut(S\_k, \bar S\_k) = ∑\_{i∈S\_k, j∉S\_k} w\_{ij}.

   vol(S\_k) = ∑\_{i∈S\_k} d\_i.

   vol(\bar S\_k) = vol(V) − vol(S\_k).
7. Compute conductance:

   φ(S\_k) = cut(S\_k, \bar S\_k) / min{vol(S\_k), vol(\bar S\_k)}.
8. Return the k with minimum φ(S\_k). This is the sweep cut produced by the eigenvector.
9. Cheeger (normalized Laplacian setting) guarantees: if ν₂ is small, there exists some k whose φ(S\_k) is O(√ν₂), more precisely φ(G) ≤ √(2ν₂) and the sweep procedure can achieve comparable bounds.

**Insight:** The eigenvector gives a 1D embedding where nearby coordinates tend to be densely connected. Sweeping thresholds searches for the best place to ‘cut’ that line, translating a continuous relaxation back to a discrete set with provable guarantees (for 𝓛 and conductance defined via volumes).

### Show L is PSD and identify its nullspace structure

Prove two foundational facts for an undirected weighted graph: (1) L is PSD, and (2) the nullspace corresponds to connected components.

1. Start from L = D − A with symmetric weights w\_{ij}=w\_{ji}.
2. For any vector **x**, expand the quadratic form:

   **x**ᵀ L **x** = **x**ᵀ D **x** − **x**ᵀ A **x**.
3. Rewrite each term:

   **x**ᵀ D **x** = ∑\_i d\_i x\_i² = ∑\_{i,j} w\_{ij} x\_i².

   **x**ᵀ A **x** = ∑\_{i,j} w\_{ij} x\_i x\_j.
4. Combine:

   **x**ᵀ L **x** = ∑\_{i,j} w\_{ij}(x\_i² − x\_i x\_j)

   = (1/2)∑\_{i,j} w\_{ij}(x\_i² − 2x\_i x\_j + x\_j²)

   = (1/2)∑\_{i,j} w\_{ij}(x\_i − x\_j)² ≥ 0.
5. Therefore L is PSD and all its eigenvalues are nonnegative.
6. Now characterize when **x**ᵀ L **x** = 0. Since it’s a sum of nonnegative terms, it equals 0 iff for every edge (i,j) with w\_{ij}>0, we have x\_i = x\_j.
7. Thus, on each connected component, x\_i must be constant (because along any path values must agree). Different components may have different constants.
8. So the nullspace consists exactly of vectors that are constant on each connected component. If there are k components, the nullspace dimension is k, meaning eigenvalue 0 has multiplicity k.

**Insight:** The Laplacian is a discrete smoothness operator. Zero energy means perfectly smooth—no variation across any edge—so the only allowed variation is between disconnected components. This is the clean algebraic reason eigenvalue-0 multiplicity equals the number of components.

## Key Takeaways

- ✓

  Undirected graphs map to symmetric matrices (A, L, 𝓛), so eigenvalues are real and eigenvectors form an orthonormal basis—this is the foundation for spectral reasoning.
- ✓

  The Laplacian quadratic form is an edge disagreement energy: **x**ᵀ L **x** = (1/2)∑\_{i,j} w\_{ij}(x\_i − x\_j)², making L PSD with nonnegative eigenvalues.
- ✓

  Eigenvalue 0 of L always exists (L**1**=0), and its multiplicity equals the number of connected components.
- ✓

  The second-smallest Laplacian eigenvalue (λ₂ for L or ν₂ for 𝓛) measures how well-connected the graph is; small values signal near-disconnectivity and potential good cuts.
- ✓

  For expansion/balanced cuts you typically want the normalized Laplacian 𝓛 and conductance defined using volumes; this is the setting of the standard Cheeger inequality.
- ✓

  Cheeger inequality (normalized Laplacian): ν₂/2 ≤ φ(G) ≤ √(2ν₂), linking spectral gap to best conductance cut (up to constants).
- ✓

  The second eigenvector (Fiedler vector) enables spectral partitioning: sort vertices by eigenvector coordinate and sweep thresholds to find a low-conductance cut.
- ✓

  Random walks connect through P=D^{-1}A; its eigenvalues relate to 𝓛 via ν\_i = 1 − μ\_i, tying spectral gaps to mixing behavior.

## Common Mistakes

- ✗

  Mixing Laplacian variants without noticing: statements about conductance/Cheeger usually refer to the normalized Laplacian 𝓛, not the combinatorial L.
- ✗

  Using an ambiguous conductance definition (edge-count vs volume-normalized). Always specify φ(S)=cut(S,\bar S)/min{vol(S),vol(\bar S)} when quoting Cheeger bounds.
- ✗

  Forgetting assumptions needed for symmetry/real spectra: adjacency and Laplacian are symmetric only for undirected graphs with symmetric weights.
- ✗

  Interpreting λ₂ or ν₂ without conditioning on connectedness: if the graph is disconnected, λ₂=0 and you should reason in terms of component structure first.

## Practice

easy

Let G be two disconnected triangles (two copies of K₃ with no edges between them). What is the multiplicity of eigenvalue 0 of the combinatorial Laplacian L? Explain without computing the full spectrum.

**Hint:** Use the theorem relating components to the nullspace of L.

Show solution

The graph has k=2 connected components (each triangle is connected, and there are two of them). The multiplicity of eigenvalue 0 of L equals the number of connected components, so 0 has multiplicity 2.

medium

For an undirected weighted graph, show directly that L = D − A is PSD by deriving **x**ᵀL**x** = (1/2)∑\_{i,j} w\_{ij}(x\_i − x\_j)². State clearly where you use symmetry of weights.

**Hint:** Expand **x**ᵀ(D−A)**x** and then symmetrize the double sum.

Show solution

Expand: **x**ᵀL**x** = ∑\_i d\_i x\_i² − ∑\_{i,j} w\_{ij}x\_i x\_j. Replace d\_i with ∑\_j w\_{ij} to get ∑\_{i,j} w\_{ij}x\_i² − ∑\_{i,j} w\_{ij}x\_i x\_j = ∑\_{i,j} w\_{ij}(x\_i² − x\_i x\_j). Now use symmetry w\_{ij}=w\_{ji} to average terms (i,j) and (j,i):

∑\_{i,j} w\_{ij}(x\_i² − x\_i x\_j) = (1/2)∑\_{i,j} w\_{ij}(x\_i² − 2x\_i x\_j + x\_j²) = (1/2)∑\_{i,j} w\_{ij}(x\_i − x\_j)² ≥ 0. Hence L is PSD.

hard

You are given ν₂, the second-smallest eigenvalue of the normalized Laplacian 𝓛, equals 0.02. Using Cheeger’s inequality (in the 𝓛 + conductance-by-volume setting), give an interval of possible values for φ(G).

**Hint:** Use ν₂/2 ≤ φ(G) ≤ √(2ν₂).

Show solution

Cheeger (normalized Laplacian) gives

Lower bound: φ(G) ≥ ν₂/2 = 0.02/2 = 0.01.

Upper bound: φ(G) ≤ √(2ν₂) = √(0.04) = 0.2.

So 0.01 ≤ φ(G) ≤ 0.2.

## Connections

- •[Eigenvalues & Eigenvectors](/tech-tree/eigenvalues-eigenvectors/)
- •[Rayleigh Quotient and Min–Max Principle](/tech-tree/rayleigh-quotient-minmax/)
- •[Graph Laplacian Basics](/tech-tree/graph-laplacian/)
- •[Markov Chains on Graphs](/tech-tree/markov-chains-graphs/)
- •[Spectral Clustering](/tech-tree/spectral-clustering/)
- •[Cheeger Inequality and Expansion](/tech-tree/cheeger-inequality-expansion/)

Quality: B (4.1/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
