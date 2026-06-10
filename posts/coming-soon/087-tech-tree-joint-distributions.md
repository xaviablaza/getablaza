---
title: Joint Distributions
description: Distributions over multiple random variables. Marginal and conditional.
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
inspiration_url: https://templeton.host/tech-tree/joint-distributions/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/joint-distributions/](https://templeton.host/tech-tree/joint-distributions/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Joint Distributions

Probability & StatisticsDifficulty: ★★★☆☆Depth: 6Unlocks: 11

Distributions over multiple random variables. Marginal and conditional.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Joint distribution: a single function/measure assigning probability or density to each tuple of outcomes for multiple random variables
- -Marginal distribution: the distribution of a subset of variables obtained by summing or integrating out the others
- -Conditional distribution: the distribution of one variable (or subset) given fixed values of the others

## Key Symbols & Notation

p\_{X,Y}(x,y) (joint pmf/pdf)p\_{X|Y}(x|y) (conditional pmf/pdf)

## Essential Relationships

- -Factorization/marginalization identity: p\_{X,Y}(x,y) = p\_{X|Y}(x|y) \* p\_Y(y); marginals obtained by summing/integrating the joint, and Bayes' rule follows by algebraic rearrangement

## Prerequisites (2)

[Common Distributions6 atoms](/tech-tree/common-distributions/)[Multivariable Calculus6 atoms](/tech-tree/multivariable-calculus/)

## Unlocks (2)

[Mutual Informationlvl 3](/tech-tree/mutual-information/)[Covariance and Correlationlvl 3](/tech-tree/covariance-correlation/)

Advanced Learning Details

### Graph Position

85

Depth Cost

11

Fan-Out (ROI)

5

Bottleneck Score

6

Chain Length

### Cognitive Load

6

Atomic Elements

35

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (16)

- - Joint probability mass function (joint PMF): probability assigned to each pair of discrete outcomes (X=x, Y=y).
- - Joint probability density function (joint PDF): density over pairs of continuous values (X=x, Y=y).
- - Joint cumulative distribution function (joint CDF): function giving P(X <= x and Y <= y).
- - Support of a joint distribution: the set of value pairs (x,y) where the joint PMF/PDF is positive or nonzero.
- - Normalization of joint distributions: the sum (discrete) or integral (continuous) of the joint over its support equals 1.
- - Marginal distribution obtained by summing or integrating the joint over the other variable(s) to get the distribution of a subset.
- - Conditional distribution of one variable given another, defined from the joint and marginal (for events with positive marginal probability/density).
- - Marginalization as projection: computing marginals by integrating/summing out unwanted variables (viewed geometrically as projection onto axes).
- - Law of total probability expressed via conditional distributions for computing marginals from conditionals.
- - Bayes rule in the joint/conditional setting: updating between conditional and marginal distributions.
- - Independence of random variables defined in terms of the joint distribution factorizing into the product of marginals.
- - Consequences of independence: conditional equals marginal, factorization test, and simplifications for expectations and variances.
- - Joint distributions over more than two variables and marginalizing over arbitrary subsets (multivariate joint distributions).
- - Expectation of functions of multiple variables: computing E[g(X,Y,...)] via multiple sums/integrals of g times the joint.
- - Relationship between joint CDF and joint PDF/PMF: differentiation (for continuous) or differences (for discrete) produce joint density/mass.
- - Support constraints and conditional support: conditioning can restrict the domain where conditional distributions are defined.

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Most real-world uncertainty is not about one variable at a time. Weather affects demand; demand affects price; price affects sales. Joint distributions are the language that lets you assign probabilities to these tuples of outcomes—and then extract the pieces you care about via marginals and conditionals.

TL;DR:

A joint distribution p\_{X,Y}(x,y) assigns probability (discrete) or density (continuous) to pairs (x,y). Marginals come from summing/integrating out the other variable, e.g. p\_X(x) = ∑\_y p\_{X,Y}(x,y) or f\_X(x) = ∫ f\_{X,Y}(x,y) dy. Conditionals come from “renormalizing a slice,” e.g. p\_{X|Y}(x|y) = p\_{X,Y}(x,y)/p\_Y(y) (when p\_Y(y) > 0). Independence is the special case p\_{X,Y}(x,y) = p\_X(x)p\_Y(y).

## What Is a Joint Distribution?

### Why we need it

Single-variable distributions (Bernoulli, Poisson, Normal, …) answer questions like “How likely is X = 3?” But many systems involve *multiple* random variables simultaneously.

Examples:

- •X = number of visitors to a website, Y = number of purchases.
- •X = a patient’s test result, Y = underlying condition.
- •X = temperature, Y = electricity demand.

To model relationships, we need a distribution over *tuples* of outcomes.

### Definition (discrete)

Let X and Y be discrete random variables. The **joint pmf** is

p\_{X,Y}(x,y) = P(X = x, Y = y).

It must satisfy:

- •Nonnegativity: p\_{X,Y}(x,y) ≥ 0
- •Normalization:

∑\_x ∑\_y p\_{X,Y}(x,y) = 1

Think of p\_{X,Y} as a table: rows are x values, columns are y values, and each cell is the probability of that pair.

### Definition (continuous)

If X and Y are continuous, we use a **joint pdf** f\_{X,Y}(x,y) such that probability is obtained by integrating over regions:

P((X,Y) ∈ A) = ∬\_A f\_{X,Y}(x,y) dx dy.

Requirements:

- •f\_{X,Y}(x,y) ≥ 0
- •∬\_{ℝ²} f\_{X,Y}(x,y) dx dy = 1

Crucial subtlety: For continuous variables, f\_{X,Y}(x,y) is a *density*, not a probability. So P(X = x, Y = y) = 0 for exact points, even though f\_{X,Y}(x,y) can be positive.

### Support (where the mass/density lives)

A joint distribution often only assigns nonzero probability/density on a particular set:

- •Discrete: a set of pairs (x,y)
- •Continuous: a region in the plane

For example, if X is uniform on [0,1] and Y = 1 − X, then (X,Y) lies only on the line y = 1 − x. This is a joint distribution, but it’s not a regular 2D pdf (it’s “singular” on a line). In this lesson we focus on standard pmfs and pdfs where the formulas below apply cleanly.

### Joint CDF as an alternative

Another way to specify the joint distribution is the joint CDF:

F\_{X,Y}(x,y) = P(X ≤ x, Y ≤ y).

For continuous distributions, you can (when differentiable) recover the joint pdf via partial derivatives:

f\_{X,Y}(x,y) = ∂²/∂x∂y F\_{X,Y}(x,y).

This connects joint distributions to multivariable calculus: joint CDFs are like “accumulated volume,” joint pdfs are like “density per unit area.”

### A mental model

- •Joint pmf/pdf: “How likely is each pair (x,y)?”
- •Marginal: “What do I believe about X alone?”
- •Conditional: “Given I learned Y = y, what do I believe about X now?”

Those last two are the real workhorses—and they both come directly from the joint.

## Core Mechanic 1: Marginal Distributions (Sum/Integrate Out Variables)

### Why marginals matter

Even if you build a full model of (X,Y), you frequently need statements about just one variable:

- •“What is the distribution of demand X regardless of price Y?”
- •“What’s the probability Y exceeds a threshold, regardless of X?”

Marginals let you ignore variables by *aggregating over all their possible values*.

### Discrete marginals

Starting from p\_{X,Y}(x,y), the marginal pmfs are

p\_X(x) = ∑\_y p\_{X,Y}(x,y)

p\_Y(y) = ∑\_x p\_{X,Y}(x,y).

Interpretation: Fix x and add up the probabilities of all pairs (x,y) across all y.

This is literally the “row sum” (or “column sum”) of the joint table.

### Continuous marginals

From a joint pdf f\_{X,Y}(x,y), the marginal pdfs are

f\_X(x) = ∫\_{−∞}^{∞} f\_{X,Y}(x,y) dy

f\_Y(y) = ∫\_{−∞}^{∞} f\_{X,Y}(x,y) dx.

Interpretation: Fix x and integrate the density along the vertical line at that x.

### Regions and supports

In practice, the integration limits often come from the support.

Example: Suppose f\_{X,Y}(x,y) = c on the triangle 0 ≤ x ≤ 1, 0 ≤ y ≤ 1 − x (and 0 otherwise). Then

- •For a given x ∈ [0,1], y ranges from 0 to 1 − x.

So

f\_X(x) = ∫\_0^{1−x} c dy = c(1 − x), 0 ≤ x ≤ 1.

The lesson: marginalization is conceptually simple, but you must be careful about the geometry of where the joint density is nonzero.

### A table viewpoint (discrete)

If you have a joint pmf table, marginals are easy bookkeeping.

| x \ y | y₁ | y₂ | y₃ | p\_X(x) |
| --- | --- | --- | --- | --- |
| x₁ | p(x₁,y₁) | p(x₁,y₂) | p(x₁,y₃) | row sum |
| x₂ | p(x₂,y₁) | p(x₂,y₂) | p(x₂,y₃) | row sum |
| p\_Y(y) | col sum | col sum | col sum | 1 |

The bottom-right cell becomes 1 because the whole table sums to 1.

### From marginals to probabilities

Once you have marginals, you can compute 1D probabilities:

- •Discrete: P(X ∈ S) = ∑\_{x∈S} p\_X(x)
- •Continuous: P(a ≤ X ≤ b) = ∫\_a^b f\_X(x) dx

### Marginalization generalizes

For more variables, the idea is identical.

If you have p\_{X,Y,Z}(x,y,z), then

p\_{X,Y}(x,y) = ∑\_z p\_{X,Y,Z}(x,y,z)

and similarly for continuous with integrals.

This “sum/integrate out what you don’t need” pattern will show up everywhere later (Bayes nets, latent-variable models, expectation-maximization, variational inference).

## Core Mechanic 2: Conditional Distributions (Normalize a Slice)

### Why conditionals matter

Information changes beliefs. If you observe Y = y, your uncertainty about X should typically shrink or shift.

Conditional distributions formalize this update.

### Discrete conditional pmf

If p\_Y(y) > 0, define

p\_{X|Y}(x|y) = P(X = x | Y = y) = p\_{X,Y}(x,y) / p\_Y(y).

This is the key identity:

- •The joint splits into “marginal × conditional”:

p\_{X,Y}(x,y) = p\_{X|Y}(x|y) p\_Y(y).

### Continuous conditional density

For continuous variables, we use conditional densities (informally, “density of X given Y = y”):

f\_{X|Y}(x|y) = f\_{X,Y}(x,y) / f\_Y(y), when f\_Y(y) > 0.

And similarly

f\_{X,Y}(x,y) = f\_{X|Y}(x|y) f\_Y(y).

### “Normalize a slice” intuition

Fix y.

- •The function x ↦ f\_{X,Y}(x,y) is a *slice* of the joint density.
- •Its total mass in x is f\_Y(y):

f\_Y(y) = ∫ f\_{X,Y}(x,y) dx.

So dividing by f\_Y(y) forces the slice to integrate to 1:

∫ f\_{X|Y}(x|y) dx

= ∫ f\_{X,Y}(x,y)/f\_Y(y) dx

= (1/f\_Y(y)) ∫ f\_{X,Y}(x,y) dx

= (1/f\_Y(y)) f\_Y(y)

= 1.

That’s what a conditional density is: the renormalized slice.

### Bayes’ rule emerges immediately

Once you accept

p\_{X,Y}(x,y) = p\_{X|Y}(x|y)p\_Y(y) = p\_{Y|X}(y|x)p\_X(x),

you can equate them to get Bayes’ rule:

p\_{X|Y}(x|y) = p\_{Y|X}(y|x) p\_X(x) / p\_Y(y).

And the denominator is just a marginalization:

p\_Y(y) = ∑\_x p\_{Y|X}(y|x)p\_X(x) (discrete)

f\_Y(y) = ∫ f\_{Y|X}(y|x) f\_X(x) dx (continuous).

So “Bayes” is not a separate topic from joint distributions—it’s a rearrangement of the joint.

### Independence as a special structure

X and Y are independent if learning Y tells you nothing about X:

p\_{X|Y}(x|y) = p\_X(x) for all x,y with p\_Y(y) > 0.

Equivalent factorizations:

p\_{X,Y}(x,y) = p\_X(x)p\_Y(y)

f\_{X,Y}(x,y) = f\_X(x)f\_Y(y).

Independence is strong. Many variables are *not* independent, but may still be uncorrelated or weakly dependent. Later nodes (covariance/correlation, mutual information) quantify dependence in different ways.

### Chain rule for more variables

For three variables (X,Y,Z), the joint can be factored as

p\_{X,Y,Z}(x,y,z)

= p\_{X|Y,Z}(x|y,z) p\_{Y|Z}(y|z) p\_Z(z).

More generally, for X₁,…,X\_n:

p(x₁,…,x\_n) = ∏\_{i=1}^n p(x\_i | x₁,…,x\_{i−1}).

This is not “assumptions”—it’s always true when the conditionals exist. Assumptions enter when you simplify the conditionals (e.g., Markov properties).

## Application/Connection: Using Joints to Compute Probabilities, Expectations, and Dependence

### Computing probabilities of events

With a joint distribution, probabilities of events about (X,Y) become sums/integrals over regions.

Discrete:

P((X,Y) ∈ A) = ∑\_{(x,y)∈A} p\_{X,Y}(x,y).

Continuous:

P((X,Y) ∈ A) = ∬\_A f\_{X,Y}(x,y) dx dy.

This is often the cleanest way to solve problems like P(X + Y ≤ 1) or P(X ≤ Y).

### Expectation with a joint

Many quantities of interest are functions g(X,Y). The expected value is

E[g(X,Y)] = ∑\_x ∑\_y g(x,y) p\_{X,Y}(x,y) (discrete)

E[g(X,Y)] = ∬ g(x,y) f\_{X,Y}(x,y) dx dy (continuous).

Special cases:

- •E[X] = ∬ x f\_{X,Y}(x,y) dx dy
- •E[XY] = ∬ xy f\_{X,Y}(x,y) dx dy

A key identity (law of total expectation) links conditionals back to marginals:

E[X] = E[E[X|Y]].

You can see it directly in the discrete case:

E[E[X|Y]]

= ∑\_y E[X|Y=y] p\_Y(y)

= ∑\_y (∑\_x x p\_{X|Y}(x|y)) p\_Y(y)

= ∑\_y ∑\_x x (p\_{X,Y}(x,y)/p\_Y(y)) p\_Y(y)

= ∑\_x ∑\_y x p\_{X,Y}(x,y)

= E[X].

This is one of the most useful “bridge” theorems in probability.

### Dependence: beyond independence

Independence is all-or-nothing. In practice you often ask: “How dependent are X and Y?”

Two major upcoming tools depend on joints:

| Tool | What it measures | Needs from joints |
| --- | --- | --- |
| Covariance/correlation | Linear relationship via E[XY] − E[X]E[Y] | Joint moments like E[XY] |
| Mutual information | Any statistical dependence via KL divergence / entropies | p\_{X,Y}, p\_X, p\_Y |

Joint distributions are the *raw material* those measures are made from.

### A geometric view for continuous joints

For a continuous f\_{X,Y}:

- •High density regions in the (x,y)-plane correspond to likely pairs.
- •Contours (level sets) show the “shape” of dependence.
- •If contours are circular (as in an isotropic Gaussian), dependence is weak.
- •If contours are elongated along a diagonal, X and Y move together.

Even before computing correlation, you can often “see” dependence from the joint density.

### Practical modeling patterns

1) **Start with a generative story** (conditionals):

- •Choose Y ~ p\_Y
- •Then choose X | Y=y ~ p\_{X|Y}(

· | y)

This defines a valid joint via p\_{X,Y}(x,y) = p\_{X|Y}(x|y)p\_Y(y).

2) **Or start with a joint** and derive everything else:

- •Compute p\_Y via marginalization
- •Compute p\_{X|Y} via division

Both are common. In machine learning, you often specify p(y) and p(x|y) (mixture models, Naive Bayes), and marginalize y to get p(x).

### A note on vectors and multivariate distributions

When you have many variables, you often package them into a random vector **X** ∈ ℝᵈ.

- •The “joint distribution of d variables” is exactly the distribution of **X**.
- •A marginal corresponds to selecting some coordinates of **X**.

You’ll later see multivariate normals, covariance matrices, and transformations of random vectors. Joint distributions are the foundation.

## Worked Examples (3)

### Discrete joint pmf → marginals → conditional pmf

Let X ∈ {0,1} and Y ∈ {0,1,2}. Suppose the joint pmf is:

p\_{X,Y}(0,0)=0.10, p(0,1)=0.20, p(0,2)=0.10,

p\_{X,Y}(1,0)=0.05, p(1,1)=0.25, p(1,2)=0.30.

(1) Compute p\_X and p\_Y.

(2) Compute p\_{X|Y}(x|1).

(3) Are X and Y independent?

1. (1) Compute p\_X(x) by summing over y.

   p\_X(0) = p(0,0)+p(0,1)+p(0,2)

   = 0.10 + 0.20 + 0.10

   = 0.40

   p\_X(1) = p(1,0)+p(1,1)+p(1,2)

   = 0.05 + 0.25 + 0.30

   = 0.60
2. (1) Compute p\_Y(y) by summing over x.

   p\_Y(0) = p(0,0)+p(1,0) = 0.10 + 0.05 = 0.15

   p\_Y(1) = p(0,1)+p(1,1) = 0.20 + 0.25 = 0.45

   p\_Y(2) = p(0,2)+p(1,2) = 0.10 + 0.30 = 0.40

   Check: 0.15+0.45+0.40 = 1.00 ✓
3. (2) Compute p\_{X|Y}(x|1) = p\_{X,Y}(x,1)/p\_Y(1).

   p\_{X|Y}(0|1) = p(0,1)/p\_Y(1) = 0.20 / 0.45 = 4/9 ≈ 0.444...

   p\_{X|Y}(1|1) = p(1,1)/p\_Y(1) = 0.25 / 0.45 = 5/9 ≈ 0.555...

   Check: 4/9 + 5/9 = 1 ✓
4. (3) Test independence using p\_{X,Y}(x,y) ?= p\_X(x)p\_Y(y).

   For (x,y)=(0,0):

   Right side = p\_X(0)p\_Y(0) = 0.40·0.15 = 0.06

   Left side = p(0,0) = 0.10

   Not equal ⇒ not independent.

**Insight:** Marginals are just sums of the joint table. Conditionals are a “renormalized column” (fix y) or row (fix x). Independence fails as soon as any joint cell disagrees with the product of marginals.

### Continuous joint pdf on a triangle → find constant and marginals

Let (X,Y) have joint pdf f\_{X,Y}(x,y) = c on the region 0 ≤ x ≤ 1, 0 ≤ y ≤ 1 − x, and 0 otherwise.

(1) Find c.

(2) Find the marginal pdf f\_X(x).

(3) Find P(X ≤ 1/2).

1. (1) Normalize the pdf: ∬ f\_{X,Y}(x,y) dx dy = 1.

   The region is: x from 0 to 1, and for each x, y from 0 to 1−x.

   So:

   1 = ∫\_{x=0}^{1} ∫\_{y=0}^{1−x} c dy dx

   = ∫\_0^1 c(1−x) dx

   = c ∫\_0^1 (1−x) dx

   = c [x − x²/2]\_0^1

   = c (1 − 1/2)

   = c/2

   Therefore c = 2.
2. (2) Compute f\_X(x) = ∫ f\_{X,Y}(x,y) dy.

   For x outside [0,1], f\_X(x)=0.

   For x ∈ [0,1], y ranges 0 to 1−x:

   f\_X(x) = ∫\_0^{1−x} 2 dy

   = 2(1−x), 0 ≤ x ≤ 1.
3. (3) Compute P(X ≤ 1/2) from f\_X.

   P(X ≤ 1/2) = ∫\_0^{1/2} 2(1−x) dx

   = 2 [x − x²/2]\_0^{1/2}

   = 2 (1/2 − (1/4)/2)

   = 2 (1/2 − 1/8)

   = 2 (3/8)

   = 3/4.

**Insight:** In continuous problems, most difficulty is identifying the support correctly. Once the limits match the geometry, marginalization is straightforward calculus.

### Derive a conditional density from a joint and interpret it

Assume a joint pdf f\_{X,Y}(x,y) = 2y for 0 < x < 1 and 0 < y < 1 (and 0 otherwise).

(1) Find f\_Y(y).

(2) Find f\_{X|Y}(x|y).

(3) Are X and Y independent?

1. (1) Marginalize out x:

   f\_Y(y) = ∫\_{x=0}^{1} 2y dx

   = 2y ∫\_0^1 dx

   = 2y, 0 < y < 1.

   Check normalization:

   ∫\_0^1 2y dy = [y²]\_0^1 = 1 ✓
2. (2) Condition on Y=y:

   f\_{X|Y}(x|y) = f\_{X,Y}(x,y)/f\_Y(y)

   = (2y)/(2y)

   = 1, for 0 < x < 1.

   So X|Y=y ~ Uniform(0,1).
3. (3) Test factorization:

   f\_X(x) = ∫\_{y=0}^{1} 2y dy = 1, for 0 < x < 1.

   So f\_X(x)=1 on (0,1).

   Now f\_X(x)f\_Y(y) = 1 · (2y) = 2y.

   This equals f\_{X,Y}(x,y) for 0<x<1, 0<y<1.

   Therefore X and Y are independent.

**Insight:** A joint can look like it “depends on y,” yet still represent independence if it factors cleanly. The conditional f\_{X|Y} revealing a constant 1 is a strong clue: X does not change when you learn Y.

## Key Takeaways

- ✓

  A joint distribution p\_{X,Y}(x,y) or f\_{X,Y}(x,y) assigns probability mass/density to outcome pairs (x,y).
- ✓

  Marginals come from summing/integrating out the other variable: p\_X(x)=∑\_y p\_{X,Y}(x,y) and f\_X(x)=∫ f\_{X,Y}(x,y) dy.
- ✓

  Conditionals are normalized slices: p\_{X|Y}(x|y)=p\_{X,Y}(x,y)/p\_Y(y) (when p\_Y(y)>0), and similarly for densities.
- ✓

  The joint always factors as joint = conditional × marginal: p\_{X,Y}=p\_{X|Y}p\_Y (and also = p\_{Y|X}p\_X).
- ✓

  Bayes’ rule is a direct consequence of two ways to factor the same joint.
- ✓

  Independence is equivalent to factorization: p\_{X,Y}=p\_X p\_Y; equivalently p\_{X|Y}=p\_X.
- ✓

  Probabilities of events about (X,Y) are sums/integrals over regions in the (x,y)-plane.
- ✓

  Future tools like covariance/correlation and mutual information are computed from the joint (plus its marginals/conditionals).

## Common Mistakes

- ✗

  Treating a pdf value f\_{X,Y}(x,y) as a probability; probabilities require integrating over an area, not reading off a point value.
- ✗

  Forgetting to respect the support when integrating (wrong bounds), especially for triangular or otherwise constrained regions.
- ✗

  Dividing by p\_Y(y) or f\_Y(y) without checking it’s positive (conditioning on an event of probability 0 is subtle).
- ✗

  Assuming uncorrelated implies independent; independence is stronger and must be checked via factorization or equivalent criteria.

## Practice

easy

Discrete: Suppose p\_{X,Y}(x,y) is given by

p(0,0)=0.3, p(0,1)=0.1,

p(1,0)=0.2, p(1,1)=0.4.

Compute (a) p\_X, (b) p\_{Y|X}(1|0), (c) P(X=Y).

**Hint:** Marginals are row/column sums. Conditionals divide a joint cell by the corresponding marginal. P(X=Y) adds the diagonal cells.

Show solution

(a) p\_X(0)=0.3+0.1=0.4, p\_X(1)=0.2+0.4=0.6.

Also p\_Y(0)=0.3+0.2=0.5, p\_Y(1)=0.1+0.4=0.5.

(b) p\_{Y|X}(1|0)=p(0,1)/p\_X(0)=0.1/0.4=0.25.

(c) P(X=Y)=p(0,0)+p(1,1)=0.3+0.4=0.7.

medium

Continuous: Let f\_{X,Y}(x,y) = k(x + y) on 0 ≤ x ≤ 1, 0 ≤ y ≤ 1, and 0 otherwise.

(a) Find k.

(b) Find f\_X(x).

(c) Find E[X].

**Hint:** Use ∬ f = 1 to find k. Then f\_X(x)=∫\_0^1 k(x+y) dy. For E[X], use E[X]=∫ x f\_X(x) dx.

Show solution

(a) Normalize:

1 = ∫\_0^1 ∫\_0^1 k(x+y) dy dx

= k ∫\_0^1 ∫\_0^1 (x+y) dy dx.

Compute inner integral:

∫\_0^1 (x+y) dy = [xy + y²/2]\_0^1 = x + 1/2.

Then

1 = k ∫\_0^1 (x+1/2) dx

= k [x²/2 + x/2]\_0^1

= k (1/2 + 1/2)

= k.

So k = 1.

(b) f\_X(x)=∫\_0^1 (x+y) dy = x + 1/2, 0≤x≤1.

(c) E[X]=∫\_0^1 x(x+1/2) dx

= ∫\_0^1 (x² + x/2) dx

= [x³/3 + x²/4]\_0^1

= 1/3 + 1/4

= 7/12.

hard

Independence check: Let X be Uniform(0,1). Given X=x, let Y|X=x be Uniform(0,x).

(a) Write f\_{Y|X}(y|x).

(b) Find the joint density f\_{X,Y}(x,y).

(c) Are X and Y independent?

**Hint:** Use f\_{X,Y}(x,y)=f\_{Y|X}(y|x)f\_X(x). Watch the support: 0<y<x<1. Independence would require factoring into f\_X(x)f\_Y(y).

Show solution

(a) For x∈(0,1), Y|X=x is Uniform(0,x), so

f\_{Y|X}(y|x)=1/x for 0<y<x, else 0.

(b) Since f\_X(x)=1 on (0,1):

f\_{X,Y}(x,y)=f\_{Y|X}(y|x)f\_X(x)= (1/x)·1 = 1/x on the region 0<y<x<1, else 0.

(c) Not independent. Intuitively, if you learn X is small, Y must be even smaller because 0<Y<X. Formally, the support is triangular (0<y<x<1), which already prevents factorization into a product of a function of x and a function of y over the full unit square.

## Connections

Next steps that build directly on this node:

- •[Covariance and Correlation](/tech-tree/covariance-correlation/) — uses E[XY] and the joint to quantify linear dependence.
- •[Mutual Information](/tech-tree/mutual-information/) — uses p\_{X,Y} versus p\_X p\_Y to quantify any dependence.

Helpful refreshers:

- •[Common Distributions](/tech-tree/common-distributions/) — joint models often use familiar marginals/conditionals.
- •[Multivariable Calculus](/tech-tree/multivariable-calculus/) — needed for double integrals and interpreting supports/regions.

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
