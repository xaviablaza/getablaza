---
title: Decision Trees
description: Tree-structured classifiers. Information gain, Gini impurity.
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
inspiration_url: https://templeton.host/tech-tree/decision-trees/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/decision-trees/](https://templeton.host/tech-tree/decision-trees/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Decision Trees

Machine LearningDifficulty: ★★★★☆Depth: 9Unlocks: 1

Tree-structured classifiers. Information gain, Gini impurity.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Tree structure and recursive partitioning: internal decision nodes apply feature-based tests; splits are applied recursively until leaves are formed
- -Node impurity: a scalar function of the class distribution at a node quantifying heterogeneity (e.g., entropy or Gini)
- -Leaf prediction: a leaf assigns a class label based on the leaf's class distribution (typically the majority class)

## Key Symbols & Notation

I(node) : impurity of a nodeDelta I(split) : impurity reduction = I(parent) - weighted average I(children)

## Essential Relationships

- -Split selection: the preferred split at a node is the one that maximizes Delta I (largest impurity reduction)

## Prerequisites (2)

[Entropy5 atoms](/tech-tree/entropy/)[Machine Learning Introduction5 atoms](/tech-tree/ml-intro/)

## Unlocks (1)

[Ensemble Methodslvl 4](/tech-tree/ensemble-methods/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[TriageBusiness

A 'fever? yes/no' split is literally the first node of a decision tree - recursive binary partitioning on the most informative feature](/business/triage/)[decision treeBusiness

Direct conceptual analog - the personal finance flowchart is a hand-crafted decision tree where each node splits on a financial condition (has emergency fund? employer match available? debt above 7%?) and leaves are actions, paralleling tree-structured classifiers](/business/decision-tree/)

Advanced Learning Details

### Graph Position

117

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

9

Chain Length

### Cognitive Load

6

Atomic Elements

31

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (14)

- - Decision tree as a hierarchical, tree-structured classifier: recursive partitioning of the input sample set into nodes (root, internal nodes, leaves).
- - Node types and roles: root node (all data), internal (decision) nodes that test a feature and split data, and leaf nodes that produce a class prediction.
- - Split (partition) at a node: choosing a feature (and for continuous features a threshold) to divide the node's sample set into child subsets.
- - Binary vs multi-way splits: splits may produce two children (common) or multiple children (for categorical features).
- - Information gain (as a split criterion): the reduction in entropy produced by a candidate split, used to rank candidate splits.
- - Gini impurity (as an alternative split criterion): impurity measure defined by class frequencies within a node, used to evaluate splits.
- - Weighted impurity of a split: the impurity of child nodes combined by weighting each child by its fraction of the parent samples.
- - Split selection rule: pick the split that maximizes information gain (or equivalently minimizes the weighted impurity after the split).
- - Leaf prediction rule: predict the majority class at a leaf; represent predictive uncertainty by class frequency distribution at the leaf.
- - Recursive tree induction: repeatedly apply split selection top-down until stopping criteria are met (pure node, depth limit, min samples, etc.).
- - Stopping criteria and pruning: constraints (max depth, min samples per node, minimum impurity decrease) and post-pruning to avoid overfitting.
- - Overfitting/underfitting trade-off specific to trees: tree complexity (depth, number of leaves) controls variance and bias.
- - Purity conditions: a node is pure (impurity = 0) when all samples in the node belong to a single class.
- - Handling continuous and categorical features during splitting: search thresholds for continuous features; group or branch by categories for categorical.

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Decision trees are the “flowcharts” of machine learning: they turn data into a sequence of simple questions (“Is age ≥ 30?”) that ends in an easily explained prediction. The power comes from choosing each question to make the data at the next step as pure (single-class) as possible.

TL;DR:

A decision tree classifier recursively partitions the feature space using feature-based tests. At each node, it chooses a split that maximizes impurity reduction ΔI(split) = I(parent) − ∑ (nᵢ/n) I(childᵢ), where I(·) is an impurity measure (commonly entropy or Gini). Leaves predict using the class distribution at that leaf (often majority class).

## What Is a Decision Tree?

A **decision tree** is a supervised learning model that predicts a class label by routing an input example through a tree of questions.

### The intuition (why trees feel natural)

Humans often make decisions by asking a sequence of questions:

- •“Is the email from someone I know?”
- •“Does it contain urgent language?”
- •“Is there an attachment?”

Each answer narrows possibilities. A decision tree does the same, but it **learns** which questions to ask from labeled data.

### The structure (internal nodes, edges, leaves)

A classification decision tree consists of:

- •**Root node**: contains the whole training set.
- •**Internal decision nodes**: apply a test on a feature (e.g., xⱼ ≤ t).
- •**Edges/branches**: correspond to outcomes of the test.
- •**Leaf nodes**: store a prediction rule, usually a class label (and often class probabilities).

So the model is a **recursive partitioning** of the feature space: each split partitions the current region into subregions, and those can be split again.

### Notation you’ll see throughout

Assume K classes. At a node v:

- •n = number of training examples at node v
- •nₖ = number of examples of class k at node v
- •pₖ = nₖ / n is the empirical class distribution at node v

We define a scalar impurity:

- •I(v) : impurity of node v (heterogeneity of its class distribution)

For a proposed split s that produces children v₁, …, v\_m:

- •ΔI(s) = I(parent) − ∑ᵢ (nᵢ/n) I(vᵢ)

This ΔI(s) is the **impurity reduction** (also called information gain when using entropy).

### What a leaf predicts

A leaf summarizes the class distribution of the training samples that reached it. Two common outputs:

1) **Hard label** (majority vote):

- •ŷ = argmaxₖ pₖ

2) **Probabilities**:

- •P(y = k | leaf) ≈ pₖ

Trees are attractive because this is both **interpretable** (you can print the rules) and **fast at inference** (a handful of comparisons).

### A key mental model: partitioning the space

If your input is a feature vector **x** ∈ ℝᵈ, each internal node applies a constraint like xⱼ ≤ t. These constraints carve the space into axis-aligned rectangles (for continuous features). Each leaf corresponds to one region, and the tree assigns that region a label.

This is a big deal: decision trees are a way to build **piecewise-constant** decision boundaries without explicitly writing down complex formulas.

## Core Mechanic 1: Node Impurity (Entropy and Gini)

A tree learns by repeatedly asking: “If I split here, will the child nodes be more pure?” To answer that, we need a number that measures impurity.

## Why impurity matters

At a node where the classes are mixed (say 50/50), prediction is uncertain. At a node that is almost all one class (say 99/1), prediction is easy.

So we want a function I(v) that is:

- •**0 when pure** (all examples in one class)
- •**larger when mixed**
- •symmetric across classes

Two classic choices are **entropy** and **Gini impurity**.

## Entropy impurity

Given class probabilities p₁, …, p\_K at a node:

H(v) = − ∑ₖ pₖ log₂ pₖ

Properties:

- •H = 0 when one pₖ = 1
- •maximum when distribution is uniform (pₖ = 1/K)

When you use entropy in a tree, the split criterion is often called **information gain**.

### Information gain from a split

Suppose parent node has entropy H(parent). A split produces children with entropies H(vᵢ). Let nᵢ be child counts.

Weighted child entropy:

H(children) = ∑ᵢ (nᵢ/n) H(vᵢ)

Information gain:

IG(split) = H(parent) − H(children)

Notice this matches the general form:

ΔI(split) = I(parent) − ∑ᵢ (nᵢ/n) I(childᵢ)

with I = H.

## Gini impurity

For class probabilities p₁, …, p\_K:

G(v) = 1 − ∑ₖ pₖ²

Interpretation:

- •∑ₖ pₖ² is the probability that two independent draws from the node have the **same** class.
- •So 1 − ∑ₖ pₖ² is the probability they are **different**.

For binary classification with p = P(class=1) and (1−p) = P(class=0):

G = 1 − (p² + (1−p)²)

Derive it explicitly:

G = 1 − (p² + (1 − 2p + p²))

= 1 − (1 − 2p + 2p²)

= 2p − 2p²

= 2p(1 − p)

So Gini is a simple parabola peaking at p = 0.5.

## Entropy vs Gini (what’s the difference?)

They behave similarly: both are 0 at purity, both peak at maximum mixing. In practice:

- •Gini is slightly cheaper to compute (no logs).
- •Entropy can be slightly more “sensitive” near extremes because of the log.

Most libraries let you choose. Either is fine as long as you understand the weighted impurity reduction idea.

| Criterion | Impurity I(v) | Split score | Notes |
| --- | --- | --- | --- |
| Entropy | H = −∑ p log₂ p | IG = H(parent) − ∑ (nᵢ/n)H(childᵢ) | Classic ID3/C4.5 framing |
| Gini | G = 1 − ∑ p² | ΔG = G(parent) − ∑ (nᵢ/n)G(childᵢ) | Default in CART; fast |

## Breathing room: what impurity is NOT

Impurity is not “error rate.” A node could have majority class 60% (so error rate 40%) and still have a certain entropy or Gini. Impurity measures **heterogeneity**, not misclassification under a fixed rule.

This distinction matters because impurity functions are designed to make greedy splitting work well.

## Core Mechanic 2: Choosing Splits via Impurity Reduction (Greedy Recursive Partitioning)

A decision tree is usually trained with a greedy algorithm: at each node, choose the split that maximizes impurity reduction, then recurse.

## Why greedy splitting?

The global problem—finding the best possible tree of a given size—is combinatorial and generally intractable for large datasets. Greedy splitting is a practical compromise:

1) At the current node, evaluate many candidate splits.

2) Pick the best local split (largest ΔI).

3) Recurse on children until a stopping rule.

This is why impurity functions matter so much: they are the local objective that guides the whole structure.

## Candidate splits

### For numeric (continuous) features

A common split form:

- •xⱼ ≤ t (left child)
- •xⱼ > t (right child)

Candidates t are often chosen from sorted unique feature values (or midpoints between them). If the sorted values are a₁ ≤ a₂ ≤ … ≤ a\_M, midpoints are:

tᵣ = (aᵣ + aᵣ₊₁)/2

Each candidate threshold produces a partition; compute ΔI and choose max.

### For categorical features

Common choices:

- •Multiway split: one branch per category.
- •Binary split: category ∈ S vs category ∉ S (CART typically prefers binary splits).

Binary splits over categories can be expensive if there are many categories (many possible subsets S).

## Impurity reduction formula (the core computation)

At node v, with impurity I(v), consider split s producing children v₁,…,v\_m.

Let nᵢ be the number of training examples going to child i, and n be parent size.

Weighted child impurity:

I\_after(s) = ∑ᵢ (nᵢ/n) I(vᵢ)

Impurity reduction:

ΔI(s) = I(v) − I\_after(s)

Choose:

s\* = argmax\_s ΔI(s)

This is the tree’s “learning signal.”

## A useful interpretation: weighted average purity

Because the child impurities are weighted by nᵢ/n, the split prefers:

- •children that are **pure**, and
- •splits that don’t isolate a tiny pure group while leaving a large messy group (unless the improvement is still large).

## Stopping conditions (when do we stop splitting?)

If you always split until every leaf is pure, you usually overfit. Common stopping rules:

- •Max depth: stop when depth reaches D
- •Min samples per leaf: stop if a child would have < m samples
- •Min impurity decrease: stop if best ΔI(s\*) < ε
- •Pure node: stop if I(v) = 0

These constraints control complexity.

## Leaf prediction (revisited, with probabilities)

At a leaf ℓ with counts nₖ:

pₖ = nₖ / n

Hard prediction:

ŷ = argmaxₖ pₖ

Probability output:

P(y = k | **x** in leaf ℓ) ≈ pₖ

Many implementations also apply smoothing (e.g., Laplace) to avoid 0 probabilities:

pₖ = (nₖ + α) / (n + Kα)

## Computational note: how training scales

At a high level:

- •For each node, you scan candidate splits for each feature.
- •For numeric features, sorting once per feature can help compute many thresholds efficiently.

Practical implementations optimize heavily, but conceptually the cost is tied to:

- •number of features d
- •number of candidate thresholds per feature
- •number of nodes created

## Breathing room: what the tree is really doing

It’s easy to get lost in formulas. Keep the picture:

- •Each split is a question.
- •Each question aims to produce child groups that are closer to “single-class.”
- •The process repeats.

The impurity reduction formula is just the arithmetic that turns “closer to single-class” into a number the algorithm can maximize.

## Application/Connection: Strengths, Weaknesses, and Why Trees Lead to Ensembles

Decision trees are popular because they’re simple to explain and surprisingly powerful. But their weaknesses are exactly why ensemble methods (random forests, boosting) are so important.

## Strengths of decision trees

### 1) Interpretability

A tree yields explicit rules:

- •If x₂ ≤ 1.7 and x₅ ∈ {A, C} then predict class 1.

You can inspect paths, feature usage, and thresholds.

### 2) Minimal preprocessing

- •No need to normalize features.
- •Works with mixed feature types (numeric + categorical) in many implementations.
- •Can handle nonlinear boundaries via multiple splits.

### 3) Captures interactions

A split on x₁ followed by a split on x₂ naturally represents feature interactions:

- •“x₂ matters only when x₁ is large.”

Linear models require explicit interaction terms; trees get them structurally.

## Weaknesses (and the motivations for fixes)

### 1) High variance (instability)

Small changes in the data can change early splits, which changes the entire tree.

This makes a single tree prone to overfitting, especially when allowed to grow deep.

### 2) Greedy splitting is myopic

Each split is locally optimal, not globally optimal. The tree can commit early to a split that seems good now but blocks better structure later.

### 3) Axis-aligned splits can be inefficient

A single split is xⱼ ≤ t. If the true boundary is diagonal, the tree may need many splits to approximate it.

## Regularization strategies (before ensembles)

To tame overfitting, we control tree complexity:

- •**Pre-pruning**: stop early (max depth, min samples per leaf, min ΔI).
- •**Post-pruning**: grow a large tree, then prune back using a validation set or cost-complexity pruning.

### Cost-complexity pruning (high-level idea)

You trade off fit and size:

Objective ≈ training\_loss(tree) + λ · (#leaves)

Pruning removes subtrees that don’t justify their complexity.

## Why trees unlock ensembles

Trees are strong “base learners” because:

- •They can fit complex patterns.
- •They are cheap to evaluate.

But because they are high variance, averaging many trees (bagging) stabilizes them.

### Connection to Random Forests (preview)

Random forests reduce correlation between trees by:

- •Training each tree on a bootstrap sample (bagging)
- •Considering only a random subset of features at each split

The end result is a much more robust predictor.

### Connection to Boosting (preview)

Boosting builds trees sequentially, where each tree focuses on correcting the errors of the previous ones. The trees are often shallow (stumps or small depth), and the ensemble forms a powerful model.

## When to use a single decision tree

A single tree can be the right choice when:

- •Interpretability and rule extraction matter.
- •You need a quick baseline.
- •The dataset is small-to-medium and you can carefully regularize.

If predictive performance is the main goal, ensembles built from trees are often the next step.

## Worked Examples (3)

### Compute Gini impurity and impurity reduction for a binary split

At a parent node v, there are n = 10 samples with class counts: n₀ = 6, n₁ = 4. So p₀ = 0.6 and p₁ = 0.4.

A candidate split s produces two children:

- •Left child v\_L has n\_L = 4 samples with counts (n₀=4, n₁=0)
- •Right child v\_R has n\_R = 6 samples with counts (n₀=2, n₁=4)

Use Gini impurity I(v) = 1 − ∑ pₖ² and compute ΔI(s).

1. Compute parent Gini:

   p₀ = 6/10 = 0.6

   p₁ = 4/10 = 0.4

   G(parent) = 1 − (0.6² + 0.4²)

   = 1 − (0.36 + 0.16)

   = 1 − 0.52

   = 0.48
2. Compute left child Gini:

   Left has (4,0) so p₀ = 1, p₁ = 0

   G(L) = 1 − (1² + 0²)

   = 0
3. Compute right child Gini:

   Right has (2,4) out of 6:

   p₀ = 2/6 = 1/3

   p₁ = 4/6 = 2/3

   G(R) = 1 − ((1/3)² + (2/3)²)

   = 1 − (1/9 + 4/9)

   = 1 − 5/9

   = 4/9

   ≈ 0.4444
4. Compute weighted child impurity:

   n\_L/n = 4/10 = 0.4

   n\_R/n = 6/10 = 0.6

   G\_after = 0.4·G(L) + 0.6·G(R)

   = 0.4·0 + 0.6·(4/9)

   = 0.6·4/9

   = 2.4/9

   = 0.2666…
5. Compute impurity reduction:

   ΔG(s) = G(parent) − G\_after

   = 0.48 − 0.2666…

   = 0.2133…

**Insight:** Even though the right child is still mixed, making the left child perfectly pure and reducing impurity in the larger right group creates a substantial weighted improvement. The weighting by child sizes is crucial: it prevents tiny pure splits from dominating unless they meaningfully improve the overall purity.

### Information gain with entropy for a 3-class node and a multiway split

A node v has n = 12 samples across 3 classes (A,B,C) with counts (6,3,3). Consider a split that produces 3 children (a multiway split) with counts:

- •Child 1: (4,0,0) n₁=4
- •Child 2: (2,3,0) n₂=5
- •Child 3: (0,0,3) n₃=3

Compute entropy H(v) in bits (log₂), the weighted child entropy, and the information gain IG.

1. Compute parent probabilities:

   p\_A = 6/12 = 0.5

   p\_B = 3/12 = 0.25

   p\_C = 3/12 = 0.25
2. Compute parent entropy:

   H(parent) = −[0.5 log₂(0.5) + 0.25 log₂(0.25) + 0.25 log₂(0.25)]

   Use log₂(0.5) = −1 and log₂(0.25) = −2:

   H(parent) = −[0.5(−1) + 0.25(−2) + 0.25(−2)]

   = −[−0.5 −0.5 −0.5]

   = 1.5 bits
3. Compute child entropies:

   Child 1: (4,0,0) ⇒ probabilities (1,0,0)

   H₁ = 0

   Child 2: (2,3,0) out of 5 ⇒ (0.4, 0.6, 0)

   H₂ = −[0.4 log₂(0.4) + 0.6 log₂(0.6)]

   Compute approximately:

   log₂(0.4) ≈ −1.3219

   log₂(0.6) ≈ −0.73697

   H₂ ≈ −[0.4(−1.3219) + 0.6(−0.73697)]

   ≈ −[−0.52876 −0.44218]

   ≈ 0.97094 bits

   Child 3: (0,0,3) ⇒ probabilities (0,0,1)

   H₃ = 0
4. Compute weighted child entropy:

   Weights: n₁/n = 4/12 = 1/3

   n₂/n = 5/12

   n₃/n = 3/12 = 1/4

   H(children) = (1/3)·0 + (5/12)·0.97094 + (1/4)·0

   = (5/12)·0.97094

   ≈ 0.40456 bits
5. Compute information gain:

   IG = H(parent) − H(children)

   = 1.5 − 0.40456

   ≈ 1.09544 bits

**Insight:** Multiway splits can produce very pure children (here, two children have entropy 0). Entropy makes the gain interpretable as “bits of uncertainty removed” about the class label after you know which branch the example follows.

### From a trained leaf distribution to predictions and probabilities (and why it matters)

A leaf ℓ contains n = 20 training samples with class counts: (class 0: 7, class 1: 13).

1) What hard class label does the leaf predict?

2) What probability estimate does it output?

3) If you apply Laplace smoothing with α = 1 for K = 2 classes, what are the smoothed probabilities?

1. Compute empirical probabilities:

   p₀ = 7/20 = 0.35

   p₁ = 13/20 = 0.65
2. Hard label (majority class):

   ŷ = argmax(p₀, p₁) = 1
3. Probability output without smoothing:

   P(y=0 | ℓ) ≈ 0.35

   P(y=1 | ℓ) ≈ 0.65
4. Laplace smoothing with α=1 and K=2:

   p₀' = (n₀ + α) / (n + Kα)

   = (7 + 1) / (20 + 2)

   = 8/22

   ≈ 0.3636

   p₁' = (n₁ + α) / (n + Kα)

   = (13 + 1) / (22)

   = 14/22

   ≈ 0.6364

**Insight:** Leaves store distributions, not just labels. That distribution becomes a probability model (often used for calibration, decision thresholds, and downstream costs). Smoothing matters most when leaves are small, preventing 0/1 probabilities that can be overconfident.

## Key Takeaways

- ✓

  A decision tree classifier routes an input **x** through feature tests until it reaches a leaf, which predicts using the leaf’s class distribution.
- ✓

  Training is usually greedy recursive partitioning: at each node, choose the split maximizing impurity reduction ΔI(split) = I(parent) − ∑ (nᵢ/n) I(childᵢ).
- ✓

  Node impurity I(v) quantifies class heterogeneity; common choices are entropy H = −∑ p log₂ p and Gini G = 1 − ∑ p².
- ✓

  The weighting (nᵢ/n) in the split criterion is essential: it balances purity improvements against how many samples are affected.
- ✓

  Stopping rules (max depth, min samples per leaf, min ΔI) and pruning are key to controlling overfitting in single trees.
- ✓

  Trees naturally capture nonlinear decision boundaries and feature interactions, with little feature scaling or preprocessing.
- ✓

  Single trees are high-variance learners; ensembles (random forests, boosting) are the standard way to get strong performance from tree-based models.

## Common Mistakes

- ✗

  Confusing impurity with misclassification error: impurity is a smooth measure of heterogeneity used for optimization, not just the fraction of wrong labels.
- ✗

  Overgrowing without regularization: a deep tree can memorize training data, producing brittle decision rules and poor generalization.
- ✗

  Ignoring class imbalance: impurity criteria can prefer splits that optimize overall purity while neglecting minority class performance; consider class weights or alternative metrics.
- ✗

  Assuming thresholds are “meaningful” causally: a tree’s split xⱼ ≤ t is predictive, not necessarily causal, and can shift with small data changes.

## Practice

easy

A node has class counts (9 positive, 3 negative). Compute (a) Gini impurity and (b) entropy in bits (log₂).

**Hint:** Use p₊ = 9/12 and p₋ = 3/12. G = 1 − (p₊² + p₋²). H = −[p₊ log₂ p₊ + p₋ log₂ p₋].

Show solution

p₊ = 9/12 = 0.75, p₋ = 0.25.

(a) G = 1 − (0.75² + 0.25²)

= 1 − (0.5625 + 0.0625)

= 1 − 0.625

= 0.375.

(b) H = −[0.75 log₂(0.75) + 0.25 log₂(0.25)].

log₂(0.25) = −2.

log₂(0.75) ≈ −0.4150.

So H ≈ −[0.75(−0.4150) + 0.25(−2)]

≈ −[−0.3113 −0.5]

≈ 0.8113 bits.

medium

A parent node has 30 samples with class counts (18, 12). A candidate split produces:

- •Left child: 10 samples with counts (9, 1)
- •Right child: 20 samples with counts (9, 11)

Compute the Gini impurity reduction ΔG.

**Hint:** Compute G(parent), G(left), G(right), then G\_after = (10/30)G(left) + (20/30)G(right), then subtract.

Show solution

Parent probabilities: p₁ = 18/30 = 0.6, p₂ = 12/30 = 0.4.

G(parent) = 1 − (0.6² + 0.4²) = 1 − (0.36 + 0.16) = 0.48.

Left: (9,1) ⇒ p = 0.9 and 0.1.

G(L) = 1 − (0.9² + 0.1²) = 1 − (0.81 + 0.01) = 0.18.

Right: (9,11) out of 20 ⇒ p = 0.45 and 0.55.

G(R) = 1 − (0.45² + 0.55²)

= 1 − (0.2025 + 0.3025)

= 1 − 0.505

= 0.495.

Weighted child impurity:

G\_after = (10/30)·0.18 + (20/30)·0.495

= (1/3)·0.18 + (2/3)·0.495

= 0.06 + 0.33

= 0.39.

Impurity reduction:

ΔG = 0.48 − 0.39 = 0.09.

hard

You are training a tree and at some node you have two candidate splits s₁ and s₂. The node has n = 100 samples.

- •Split s₁ creates children with (n₁=90, impurity=0.30) and (n₂=10, impurity=0.00).
- •Split s₂ creates children with (n₁=50, impurity=0.20) and (n₂=50, impurity=0.20).

Assuming the parent impurity is I(parent)=0.32, which split is chosen by impurity reduction? Show the computation.

**Hint:** Compute I\_after(s) as the weighted average of child impurities, then ΔI(s) = 0.32 − I\_after(s).

Show solution

For s₁:

I\_after(s₁) = (90/100)·0.30 + (10/100)·0.00

= 0.27 + 0

= 0.27.

ΔI(s₁) = 0.32 − 0.27 = 0.05.

For s₂:

I\_after(s₂) = (50/100)·0.20 + (50/100)·0.20

= 0.10 + 0.10

= 0.20.

ΔI(s₂) = 0.32 − 0.20 = 0.12.

Since ΔI(s₂) > ΔI(s₁), the algorithm chooses s₂.

Interpretation: even though s₁ creates one perfectly pure small child, s₂ substantially reduces impurity for half the data and yields a larger overall weighted improvement.

## Connections

Next, decision trees become the building block for ensembles:

- •[Ensemble Methods](/tech-tree/ensemble-methods/) — bagging and boosting turn high-variance trees into state-of-the-art predictors.

Related prerequisites and helpful refreshers:

- •[Entropy](/tech-tree/entropy/) — entropy as uncertainty; used directly in information gain.
- •[Machine Learning Introduction](/tech-tree/machine-learning-introduction/) — supervised learning framing, train/test generalization.

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
