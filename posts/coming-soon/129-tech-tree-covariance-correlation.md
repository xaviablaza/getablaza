---
title: Covariance and Correlation
description: Measures of linear relationship between random variables.
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
permalink: /tech-tree/covariance-correlation/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Covariance and Correlation

Probability & StatisticsDifficulty: ★★★☆☆Depth: 7Unlocks: 6

Measures of linear relationship between random variables.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Covariance: the expected product of deviations from the means (Cov(X,Y) = E[(X - E[X]) (Y - E[Y])]).
- -Correlation: the standardized, unitless measure of linear association bounded between -1 and 1.
- -Zero covariance means no linear relationship but does not imply independence in general.

## Key Symbols & Notation

Cov(X,Y)rho\_{X,Y} (correlation coefficient)

## Essential Relationships

- -rho\_{X,Y} = Cov(X,Y) / (sigma\_X \* sigma\_Y) where sigma\_X = sqrt(Var(X)) and sigma\_Y = sqrt(Var(Y)).

## Prerequisites (2)

[Variance5 atoms](/tech-tree/variance/)[Joint Distributions6 atoms](/tech-tree/joint-distributions/)

## Unlocks (2)

[Principal Component Analysislvl 4](/tech-tree/pca/)[Time Series Foundationslvl 3](/tech-tree/time-series-foundations/)

## Referenced by (9)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (8)

[personal financeBusiness

Portfolio diversification is the canonical real-world application of covariance reduction - Markowitz's entire insight was that portfolio risk depends on asset covariance, making this the exact math behind diversification](/business/personal-finance/)[Execution RiskBusiness

Correlated execution risk is literally positive covariance between project failure modes; understanding Cov(X,Y) > 0 when X and Y share an underlying factor (the team) is the mathematical foundation](/business/execution-risk/)[Markowitz Portfolio TheoryBusiness

The covariance matrix of asset returns is the central mathematical object in Markowitz. Portfolio variance equals w^T Sigma w, so understanding covariance structure is prerequisite to constructing the efficient frontier.](/business/markowitz-portfolio-theory/)[Operating InvestmentsBusiness

The entire Markowitz insight is that portfolio variance = w^T Σ w, so risk depends on the covariance matrix between investments, not just individual variances - this is the mathematical core](/business/operating-investments/)[Risk-Adjusted ReturnBusiness

The covariance matrix between asset returns is the core mathematical object for handling correlations and computing portfolio variance (w'Σw) - without this, risk-adjusted return is single-instrument only](/business/risk-adjusted-return/)[PortfolioBusiness

The covariance matrix of asset returns is THE central mathematical object in Markowitz - portfolio variance is w^T Sigma w, and the entire efficient frontier emerges from the structure of Sigma](/business/portfolio/)[Portfolio ConstructionBusiness

Portfolio construction fundamentally depends on the covariance matrix between assets - 'handling correlations' from the definition is precisely what covariance and correlation measure, and the math of portfolio variance reduction through diversification is built on this](/business/portfolio-construction/)[CFABusiness

Markowitz mean-variance portfolio optimization - core CFA Level 1-2 material - requires computing covariance matrices between asset returns](/business/cfa/)

### From Money (1)

[DiversificationMoney

Diversification benefit comes from low or negative correlation between assets](/money/diversification/)

Advanced Learning Details

### Graph Position

91

Depth Cost

6

Fan-Out (ROI)

2

Bottleneck Score

7

Chain Length

### Cognitive Load

6

Atomic Elements

30

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (14)

- - Covariance as a measure of joint variability: expectation of the product of deviations of two variables from their means
- - Sign interpretation of covariance: positive, negative, or zero indicates direction of linear association
- - Magnitude interpretation of covariance: size depends on variable units (not standardized)
- - Alternative algebraic form: covariance can be computed as E[XY] - E[X]E[Y]
- - Covariance as a special-case relation to variance: Cov(X,X) = Var(X)
- - Bilinearity / linear response: covariance scales with multiplicative linear changes to variables
- - Independence implies zero covariance
- - Zero covariance does not imply independence (lack of linear association ≠ no dependence in general)
- - Pearson correlation coefficient: standardized (unitless) version of covariance
- - Interpretation of correlation values: +1/−1 (perfect linear relationship), 0 (no linear relationship)
- - Invariance properties of correlation: unaffected by additive shifts and by scaling magnitude (sign of scaling can flip correlation sign)
- - Sample (empirical) covariance as an estimator of population covariance (including Bessel's correction)
- - Sample Pearson correlation as estimator of population correlation
- - Connection to simple linear regression slope: slope = Cov(X,Y)/Var(X) (population or sample analogue)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

A city analyst plots two monthly time series: ice cream sales and drownings. The scatterplot slopes upward—strongly. A headline writes itself: “Ice cream causes drownings.”

But the analyst pauses. Covariance and correlation can tell you *how tightly two variables move together in a straight-line way*. They cannot, by themselves, tell you *why* (causation), nor whether a relationship is *real* vs driven by a third variable (season/temperature), nor whether a relationship is *nonlinear* (e.g., U-shaped).

In this lesson you’ll learn:

- •what covariance and correlation actually measure,
- •how to compute and interpret them,
- •what “zero covariance” does and does *not* imply,
- •and why covariance is the engine behind PCA.

TL;DR:

Covariance is the expected product of two variables’ deviations from their means: Cov(X,Y) = E[(X−E[X])(Y−E[Y])]. Its sign indicates direction of linear co-movement, and its magnitude depends on units. Correlation ρ₍X,Y₎ standardizes covariance by dividing by σXσY, producing a unitless number in [−1,1] that measures *linear* association. Zero covariance means “no linear relationship” but does not generally mean independence (except in special cases like jointly normal variables).

## What Is Covariance and Correlation?

### The motivation (why we need them)

Variance tells you how a single random variable spreads around its mean. But many real questions are about *pairs* of variables:

- •Do study hours and exam score tend to rise together?
- •Do two sensors drift together over time?
- •If one stock goes up, does another tend to go up as well?

We want a number that captures **co-movement**.

### Covariance: “do deviations move together?”

Covariance looks at whether XXX and YYY are simultaneously above their means or simultaneously below their means.

Define the mean-centered variables:

- •Xc=X−E[X]X\_c = X - E[X]Xc​=X−E[X]
- •Yc=Y−E[Y]Y\_c = Y - E[Y]Yc​=Y−E[Y]

Then covariance is the expected product:

Cov⁡(X,Y)=E[(X−E[X])(Y−E[Y])].\operatorname{Cov}(X,Y) = E\big[(X - E[X])(Y - E[Y])\big].Cov(X,Y)=E[(X−E[X])(Y−E[Y])].

Interpretation by sign:

- •**Positive covariance**: when XXX is above its mean, YYY tends to be above its mean too (and likewise below).
- •**Negative covariance**: when XXX is above its mean, YYY tends to be below its mean.
- •**Near zero covariance**: no *linear* tendency for the deviations to align.

A key subtlety: covariance is **unitful**. If XXX is in dollars and YYY is in seconds, covariance is in dollar·seconds. Changing units (e.g., dollars → cents) scales covariance.

### Correlation: “covariance without units”

To compare relationships across different scales, we standardize by each variable’s standard deviation.

ρX,Y=Corr⁡(X,Y)=Cov⁡(X,Y)σX σY,\rho\_{X,Y} = \operatorname{Corr}(X,Y) = \frac{\operatorname{Cov}(X,Y)}{\sigma\_X\,\sigma\_Y},ρX,Y​=Corr(X,Y)=σX​σY​Cov(X,Y)​,

where σX=Var⁡(X)\sigma\_X = \sqrt{\operatorname{Var}(X)}σX​=Var(X)​ and σY=Var⁡(Y)\sigma\_Y = \sqrt{\operatorname{Var}(Y)}σY​=Var(Y)​.

Correlation is:

- •**unitless**
- •bounded: −1≤ρX,Y≤1-1 \le \rho\_{X,Y} \le 1−1≤ρX,Y​≤1

Interpretation:

- •ρ=1\rho = 1ρ=1: perfect positive *linear* relationship (Y=aX+bY = aX + bY=aX+b with a>0a>0a>0 almost surely)
- •ρ=−1\rho = -1ρ=−1: perfect negative linear relationship (a<0a<0a<0)
- •ρ=0\rho = 0ρ=0: no linear association (but there may be a nonlinear one)

### A concrete picture: centered scatter and “cosine similarity”

If you take paired samples (xi,yi)(xᵢ, yᵢ)(xi​,yi​) and center them, each data point becomes a 2D vector from the mean: zi=[xi−xˉ,  yi−yˉ]\mathbf{z}\_i = [xᵢ-\bar{x},\; yᵢ-\bar{y}]zi​=[xi​−xˉ,yi​−yˉ​].

A helpful geometric intuition is that correlation behaves like a normalized “alignment” between the centered coordinates of XXX and YYY.

Here’s a simple ASCII scatter showing a positive association. The “+” is the mean; arrows suggest centered deviations.

```
Y
^               *
|            *
|         *
|      *
|   *
| +-----------------> X
|   *
|      *
```

When points trend from bottom-left to top-right, products (xi−xˉ)(yi−yˉ)(xᵢ-\bar{x})(yᵢ-\bar{y})(xi​−xˉ)(yi​−yˉ​) are often positive, boosting covariance and correlation.

### What they can and cannot conclude (preview)

Covariance/correlation can:

- •quantify **direction** and **strength** of *linear* relationship
- •feed into models (regression) and decompositions (PCA)

They cannot by themselves:

- •prove **causation** (ice cream doesn’t cause drownings)
- •guarantee **independence** from ρ=0\rho=0ρ=0 (nonlinear dependence exists)
- •detect strong **nonlinear** patterns (U-shapes can yield ρ≈0\rho \approx 0ρ≈0)

## Core Mechanic 1: Computing Covariance (and its key identities)

### Why the definition looks the way it does

We want a measure that’s:

1. 1)**Positive** when both variables tend to be on the same side of their means.
2. 2)**Negative** when they tend to be on opposite sides.
3. 3)Larger when these deviations are larger.

The product (X−E[X])(Y−E[Y])(X-E[X])(Y-E[Y])(X−E[X])(Y−E[Y]) does exactly that:

- •both positive → product positive
- •one positive, one negative → product negative
- •bigger deviations → bigger magnitude

Averaging (expectation) makes it a stable summary.

### Expanding covariance: a very useful formula

Start from the definition:

Cov⁡(X,Y)=E[(X−E[X])(Y−E[Y])].\operatorname{Cov}(X,Y) = E\big[(X - E[X])(Y - E[Y])\big].Cov(X,Y)=E[(X−E[X])(Y−E[Y])].

Expand step-by-step:

Cov⁡(X,Y)=E[XY−X E[Y]−E[X] Y+E[X]E[Y]]=E[XY]−E[Y]E[X]−E[X]E[Y]+E[X]E[Y]=E[XY]−E[X]E[Y].\begin{aligned}
\operatorname{Cov}(X,Y)
&= E\big[XY - X\,E[Y] - E[X]\,Y + E[X]E[Y]\big] \\
&= E[XY] - E[Y]E[X] - E[X]E[Y] + E[X]E[Y] \\
&= E[XY] - E[X]E[Y].
\end{aligned}Cov(X,Y)​=E[XY−XE[Y]−E[X]Y+E[X]E[Y]]=E[XY]−E[Y]E[X]−E[X]E[Y]+E[X]E[Y]=E[XY]−E[X]E[Y].​

So:

Cov⁡(X,Y)=E[XY]−E[X]E[Y].\boxed{\operatorname{Cov}(X,Y) = E[XY] - E[X]E[Y].}Cov(X,Y)=E[XY]−E[X]E[Y].​

This identity is especially handy in calculations.

### Covariance with constants and scaling

These properties matter constantly in modeling:

1) Adding constants doesn’t change covariance:

Cov⁡(X+a, Y+b)=Cov⁡(X,Y).\operatorname{Cov}(X+a,\, Y+b) = \operatorname{Cov}(X,Y).Cov(X+a,Y+b)=Cov(X,Y).

Reason: centering removes constants.

2) Scaling scales covariance:

Cov⁡(cX, dY)=cd Cov⁡(X,Y).\operatorname{Cov}(cX,\, dY) = cd\,\operatorname{Cov}(X,Y).Cov(cX,dY)=cdCov(X,Y).

So if you convert meters to centimeters (×100), covariance changes by ×100 on that variable’s side.

### Relationship to variance

Variance is just covariance with itself:

Var⁡(X)=Cov⁡(X,X).\operatorname{Var}(X) = \operatorname{Cov}(X,X).Var(X)=Cov(X,X).

That makes covariance a true generalization of variance.

### Independence implies zero covariance (but not conversely)

If XXX and YYY are independent, then E[XY]=E[X]E[Y]E[XY] = E[X]E[Y]E[XY]=E[X]E[Y], so:

Cov⁡(X,Y)=0.\operatorname{Cov}(X,Y) = 0.Cov(X,Y)=0.

But the reverse is not generally true: Cov⁡(X,Y)=0\operatorname{Cov}(X,Y)=0Cov(X,Y)=0 does **not** guarantee independence. (We’ll build a concrete counterexample later.)

### Sample covariance: estimating from data

In practice, you usually have samples (xi,yi)(xᵢ, yᵢ)(xi​,yi​) for i=1..ni=1..ni=1..n.

Define sample means:

- •xˉ=1n∑i=1nxi\bar{x} = \frac{1}{n}\sum\_{i=1}^n xᵢxˉ=n1​∑i=1n​xi​
- •yˉ=1n∑i=1nyi\bar{y} = \frac{1}{n}\sum\_{i=1}^n yᵢyˉ​=n1​∑i=1n​yi​

A common estimator (unbiased for i.i.d. samples) is:

sxy=1n−1∑i=1n(xi−xˉ)(yi−yˉ).s\_{xy} = \frac{1}{n-1}\sum\_{i=1}^n (xᵢ-\bar{x})(yᵢ-\bar{y}).sxy​=n−11​i=1∑n​(xi​−xˉ)(yi​−yˉ​).

You may also see 1n\frac{1}{n}n1​ instead of 1n−1\frac{1}{n-1}n−11​; that version is the maximum-likelihood estimator under a normal model but is biased in finite samples.

### Interpreting magnitude: why covariance is hard to compare

Suppose:

- •height in **meters** vs weight in **kg**
- •height in **centimeters** vs weight in **kg**

The relationship is identical, but scaling height by 100 scales covariance by 100. That’s why correlation is so widely used: it removes units.

## Core Mechanic 2: Correlation as Standardized Covariance (and the geometry behind ±1)

### Why standardize?

Covariance answers “do they move together?”, but not “how strong is that co-movement relative to each variable’s natural scale?”

Correlation fixes this by dividing by σXσY\sigma\_X\sigma\_YσX​σY​.

ρX,Y=Cov⁡(X,Y)σXσY.\rho\_{X,Y} = \frac{\operatorname{Cov}(X,Y)}{\sigma\_X\sigma\_Y}.ρX,Y​=σX​σY​Cov(X,Y)​.

Because σX\sigma\_XσX​ has units of XXX and σY\sigma\_YσY​ has units of YYY, the units cancel.

### Correlation is bounded between −1 and 1

This isn’t just a convention—it’s a theorem. One route uses Cauchy–Schwarz.

Let Xc=X−E[X]X\_c = X - E[X]Xc​=X−E[X] and Yc=Y−E[Y]Y\_c = Y - E[Y]Yc​=Y−E[Y].

Apply Cauchy–Schwarz to random variables:

∣E[XcYc]∣≤E[Xc2] E[Yc2].|E[X\_c Y\_c]| \le \sqrt{E[X\_c^2]}\,\sqrt{E[Y\_c^2]}.∣E[Xc​Yc​]∣≤E[Xc2​]​E[Yc2​]​.

But E[Xc2]=Var⁡(X)=σX2E[X\_c^2]=\operatorname{Var}(X)=\sigma\_X^2E[Xc2​]=Var(X)=σX2​ and similarly for YYY.

So:

∣Cov⁡(X,Y)∣≤σXσY.|\operatorname{Cov}(X,Y)| \le \sigma\_X\sigma\_Y.∣Cov(X,Y)∣≤σX​σY​.

Divide both sides by σXσY\sigma\_X\sigma\_YσX​σY​ (assuming nonzero):

∣ρX,Y∣≤1.|\rho\_{X,Y}| \le 1.∣ρX,Y​∣≤1.

### When do we get ±1?

Equality in Cauchy–Schwarz occurs when one variable is an exact scalar multiple of the other (almost surely) after centering.

That means:

- •ρ=1\rho=1ρ=1 iff Y−E[Y]=a(X−E[X])Y - E[Y] = a(X - E[X])Y−E[Y]=a(X−E[X]) with a>0a>0a>0 a.s.
- •ρ=−1\rho=-1ρ=−1 iff same with a<0a<0a<0

Equivalently, Y=aX+bY = aX + bY=aX+b almost surely for some constants a,ba, ba,b.

### A visual: correlation as “angle” between centered coordinates (sample view)

For a dataset, define centered vectors:

- •**x** = (x1−xˉ,…,xn−xˉ)(x₁-\bar{x},\dots,x\_n-\bar{x})(x1​−xˉ,…,xn​−xˉ)
- •**y** = (y1−yˉ,…,yn−yˉ)(y₁-\bar{y},\dots,y\_n-\bar{y})(y1​−yˉ​,…,yn​−yˉ​)

Then the sample correlation is:

r=x⋅y∥x∥ ∥y∥.r = \frac{\mathbf{x}\cdot\mathbf{y}}{\|\mathbf{x}\|\,\|\mathbf{y}\|}.r=∥x∥∥y∥x⋅y​.

That is exactly the cosine of the angle between **x** and **y** in Rn\mathbb{R}^nRn.

- •If **x** and **y** point in the same direction → r≈1r\approx 1r≈1
- •Orthogonal → r≈0r\approx 0r≈0
- •Opposite directions → r≈−1r\approx -1r≈−1

Inline “plot” of the vector-angle intuition:

```
           y (centered)
           ^
          /|
         / |   cos(θ) = r
        /θ |
       +---+----------> x (centered)
```

This is a powerful mental model: **correlation is alignment** between patterns of deviation-from-mean.

### Sample correlation

Using the sample covariance sxys\_{xy}sxy​ and sample standard deviations sx,sys\_x, s\_ysx​,sy​:

r=sxysxsy.r = \frac{s\_{xy}}{s\_x s\_y}.r=sx​sy​sxy​​.

### Correlation is not robust to outliers

Because it depends on products of deviations, a single extreme point can dominate.

Practical note:

- •If you suspect outliers or heavy tails, consider rank-based alternatives like Spearman’s ρ\rhoρ or Kendall’s τ\tauτ (different nodes/topics).

## Application/Connection: What Covariance and Correlation Enable (and what they don’t)

### 1) The “ice cream and drownings” lesson: correlation ≠ causation

A strong correlation can arise from:

- •a direct causal link (X→YX \to YX→Y)
- •reverse causation (Y→XY \to XY→X)
- •a third variable ZZZ driving both (Z→XZ \to XZ→X and Z→YZ \to YZ→Y)
- •coincidence / selection bias / measurement artifacts

In the ice-cream example, temperature (a confounder) increases both ice cream consumption and swimming, which increases drowning risk.

Covariance/correlation *quantify association*; causal claims require additional design/assumptions.

### 2) Zero covariance: what it means, and the classic trap

Cov⁡(X,Y)=0\operatorname{Cov}(X,Y)=0Cov(X,Y)=0 means the linear term in their relationship is absent in a precise sense:

- •If you try to predict YYY using a linear function of XXX, the best linear predictor doesn’t gain anything from XXX (in a mean-square sense) beyond the intercept.

But XXX can still strongly determine YYY nonlinearly.

We’ll show an explicit example in the worked examples: X∼Uniform(−1,1)X \sim \text{Uniform}(-1,1)X∼Uniform(−1,1) and Y=X2Y=X^2Y=X2. Then covariance is 0, yet YYY is completely determined by XXX.

Special case worth knowing: if (X,Y)(X,Y)(X,Y) are **jointly normal**, then zero covariance *does* imply independence. (Not true in general.)

### 3) Covariance matrix: scaling up to many variables

With ddd random variables, stack them into a random vector **X** ∈ Rd\mathbb{R}^dRd.

Define the covariance matrix:

Σ=Cov⁡(X)=E[(X−E[X])(X−E[X])T].\Sigma = \operatorname{Cov}(\mathbf{X}) = E\big[(\mathbf{X}-E[\mathbf{X}])(\mathbf{X}-E[\mathbf{X}])^T\big].Σ=Cov(X)=E[(X−E[X])(X−E[X])T].

Key facts:

- •Diagonal entries: variances (Σjj=Var⁡(Xj)\Sigma\_{jj}=\operatorname{Var}(X\_j)Σjj​=Var(Xj​))
- •Off-diagonals: covariances (Σjk=Cov⁡(Xj,Xk)\Sigma\_{jk}=\operatorname{Cov}(X\_j, X\_k)Σjk​=Cov(Xj​,Xk​))
- •Σ\SigmaΣ is symmetric and positive semidefinite

This matrix is the central object in multivariate statistics.

### 4) Connection to PCA (what this node unlocks)

PCA looks for directions in feature space with maximum variance.

If you have centered data vectors **x** ∈ Rd\mathbb{R}^dRd, PCA finds unit vectors **v** maximizing:

Var⁡(vTX)=vTΣv.\operatorname{Var}(\mathbf{v}^T\mathbf{X}) = \mathbf{v}^T \Sigma \mathbf{v}.Var(vTX)=vTΣv.

The solutions are eigenvectors of the covariance matrix Σ\SigmaΣ.

So learning covariance is not just about pairwise relationships—it’s about understanding the geometry of data clouds and the linear structure PCA extracts.

### 5) A quick “what to use when” table

| Goal | Use covariance? | Use correlation? | Notes |
| --- | --- | --- | --- |
| Keep physical units (e.g., risk in \·days) | ✅ | ❌ | Covariance preserves scale |
| Compare relationships across different units | ❌ | ✅ | Correlation is unitless |
| Build PCA on raw feature scales | ✅ | ❌/✅ | Often you choose covariance PCA or correlation PCA (standardized) |
| Detect any dependence (including nonlinear) | ❌ | ❌ | Need other tools (MI, plots, kernels, etc.) |

## Worked Examples (3)

### Compute covariance and correlation from a small dataset (by hand)

You observe n=5 paired measurements:

X: [1, 2, 3, 4, 5]

Y: [2, 1, 4, 3, 6]

Compute the sample covariance s\_xy (with 1/(n−1)) and sample correlation r.

1. Compute means:

   \bar{x} = (1+2+3+4+5)/5 = 15/5 = 3

   \bar{y} = (2+1+4+3+6)/5 = 16/5 = 3.2
2. Compute centered values and products:

   For each i, compute (xᵢ−\bar{x}), (yᵢ−\bar{y}), and product.

   i=1: x=1 → −2; y=2 → −1.2; product = (−2)(−1.2)= 2.4

   i=2: x=2 → −1; y=1 → −2.2; product = (−1)(−2.2)= 2.2

   i=3: x=3 → 0; y=4 → 0.8; product = 0·0.8= 0

   i=4: x=4 → 1; y=3 → −0.2; product = 1·(−0.2)= −0.2

   i=5: x=5 → 2; y=6 → 2.8; product = 2·2.8= 5.6
3. Sum of products:

   ∑(xᵢ−\bar{x})(yᵢ−\bar{y}) = 2.4+2.2+0−0.2+5.6 = 10.0
4. Sample covariance:

   sxy=1n−1∑(xi−xˉ)(yi−yˉ)=104=2.5.s\_{xy} = \frac{1}{n-1}\sum (xᵢ-\bar{x})(yᵢ-\bar{y}) = \frac{10}{4} = 2.5.sxy​=n−11​∑(xi​−xˉ)(yi​−yˉ​)=410​=2.5.
5. Compute sample standard deviations.

   First compute sums of squares.

   For X:

   (xᵢ−\bar{x})²: 4, 1, 0, 1, 4 → sum = 10

   So s\_x² = 10/(n−1)=10/4=2.5 → s\_x = √2.5

   For Y:

   (yᵢ−\bar{y})²: (−1.2)²=1.44, (−2.2)²=4.84, 0.8²=0.64, (−0.2)²=0.04, 2.8²=7.84

   Sum = 1.44+4.84+0.64+0.04+7.84 = 14.8

   So s\_y² = 14.8/4 = 3.7 → s\_y = √3.7
6. Compute correlation:

   r=sxysxsy=2.52.5 3.7=2.59.25.r = \frac{s\_{xy}}{s\_x s\_y} = \frac{2.5}{\sqrt{2.5}\,\sqrt{3.7}} = \frac{2.5}{\sqrt{9.25}}.r=sx​sy​sxy​​=2.5​3.7​2.5​=9.25​2.5​.

   Numerically, √9.25 ≈ 3.041, so

   r ≈ 2.5 / 3.041 ≈ 0.822.

**Insight:** The covariance (2.5) says X and Y tend to be above/below their means together, but its magnitude depends on X and Y units. The correlation (~0.82) shows a fairly strong positive linear association on a standardized scale.

### Zero covariance but strong dependence: Y = X² on a symmetric interval

Let X ~ Uniform(−1, 1) and define Y = X². Compute Cov(X,Y). Are X and Y independent?

1. Compute expectations.

   By symmetry of Uniform(−1,1), the distribution is symmetric around 0, so

   E[X]=0.E[X] = 0.E[X]=0.
2. Compute E[Y]. Since Y=X²:

   E[Y]=E[X2].E[Y] = E[X^2].E[Y]=E[X2].

   For X ~ Uniform(−1,1) with density f(x)=1/2 on [−1,1]:

   E[X2]=∫−11x2⋅12 dx=12[x33]−11=12(13−(−13))=12⋅23=13.\begin{aligned}
   E[X^2]
   &= \int\_{-1}^{1} x^2 \cdot \frac{1}{2}\,dx \\
   &= \frac{1}{2}\left[\frac{x^3}{3}\right]\_{-1}^{1} \\
   &= \frac{1}{2}\left(\frac{1}{3} - \left(-\frac{1}{3}\right)\right) \\
   &= \frac{1}{2}\cdot \frac{2}{3} = \frac{1}{3}.
   \end{aligned}E[X2]​=∫−11​x2⋅21​dx=21​[3x3​]−11​=21​(31​−(−31​))=21​⋅32​=31​.​
3. Compute E[XY]. Since Y=X², we have XY = X·X² = X³. Then:

   E[XY]=E[X3]=∫−11x3⋅12 dx.E[XY] = E[X^3] = \int\_{-1}^{1} x^3 \cdot \frac{1}{2}\,dx.E[XY]=E[X3]=∫−11​x3⋅21​dx.

   But x³ is an odd function and the interval is symmetric, so the integral is 0:

   E[X3]=0.E[X^3]=0.E[X3]=0.
4. Compute covariance using E[XY] − E[X]E[Y]:

   Cov⁡(X,Y)=E[XY]−E[X]E[Y]=0−(0)(13)=0.\operatorname{Cov}(X,Y) = E[XY] - E[X]E[Y] = 0 - (0)\left(\frac{1}{3}\right) = 0.Cov(X,Y)=E[XY]−E[X]E[Y]=0−(0)(31​)=0.
5. Check independence intuition.

   If X and Y were independent, knowing X would not give information about Y.

   But here Y is determined exactly by X via Y=X². For example:

   - •If X=0, then Y=0 with certainty.
   - •If X=±1, then Y=1 with certainty.

   So Y is not independent of X.

**Insight:** Covariance zero means “no linear association,” not “no relationship.” The relationship here is perfectly nonlinear: the scatter is a U-shape. Covariance and correlation miss that shape even though dependence is complete.

### Correlation is invariant to shifting and positive scaling (but flips sign under negative scaling)

Let X and Y be random variables with Corr(X,Y)=ρ. Define X' = 3X + 10 and Y' = −2Y + 5. Find Corr(X',Y').

1. Use covariance and standard deviation scaling rules.

   Constants don’t affect covariance:

   Cov(X+a, Y+b)=Cov(X,Y).

   Scaling: Cov(cX, dY)=cd Cov(X,Y).
2. Compute Cov(X',Y'):

   X' = 3X+10, Y' = −2Y+5

   Cov⁡(X′,Y′)=Cov⁡(3X+10, −2Y+5)=(3)(−2)Cov⁡(X,Y)=−6Cov⁡(X,Y).\operatorname{Cov}(X',Y') = \operatorname{Cov}(3X+10,\,-2Y+5) = (3)(-2)\operatorname{Cov}(X,Y) = -6\operatorname{Cov}(X,Y).Cov(X′,Y′)=Cov(3X+10,−2Y+5)=(3)(−2)Cov(X,Y)=−6Cov(X,Y).
3. Compute σ\_{X'} and σ\_{Y'}.

   Standard deviation scales by absolute value:

   σ\_{3X+10} = |3|σ\_X = 3σ\_X

   σ\_{−2Y+5} = |−2|σ\_Y = 2σ\_Y
4. Compute correlation:

   Corr⁡(X′,Y′)=Cov⁡(X′,Y′)σX′σY′=−6Cov⁡(X,Y)(3σX)(2σY)=−Cov⁡(X,Y)σXσY=−ρ.\begin{aligned}
   \operatorname{Corr}(X',Y')
   &= \frac{\operatorname{Cov}(X',Y')}{\sigma\_{X'}\sigma\_{Y'}} \\
   &= \frac{-6\operatorname{Cov}(X,Y)}{(3\sigma\_X)(2\sigma\_Y)} \\
   &= -\frac{\operatorname{Cov}(X,Y)}{\sigma\_X\sigma\_Y} \\
   &= -\rho.
   \end{aligned}Corr(X′,Y′)​=σX′​σY′​Cov(X′,Y′)​=(3σX​)(2σY​)−6Cov(X,Y)​=−σX​σY​Cov(X,Y)​=−ρ.​

**Insight:** Correlation ignores shifts and positive rescalings (unit changes), but a negative scaling flips the sign because it reverses one axis.

## Key Takeaways

- ✓

  Covariance measures average *joint deviation*: $Cov⁡(X,Y)=E[(X−E[X])(Y−E[Y])].\operatorname{Cov}(X,Y)=E[(X−E[X])(Y−E[Y])].Cov(X,Y)=E[(X−E[X])(Y−E[Y])].$
- ✓

  A useful identity: $Cov⁡(X,Y)=E[XY]−E[X]E[Y].\operatorname{Cov}(X,Y)=E[XY]−E[X]E[Y].Cov(X,Y)=E[XY]−E[X]E[Y].$
- ✓

  Covariance has units (units of X times units of Y), so its magnitude depends on scaling choices.
- ✓

  Correlation standardizes covariance: $ρX,Y=Cov⁡(X,Y)σXσY,\rho\_{X,Y}=\frac{\operatorname{Cov}(X,Y)}{\sigma\_X\sigma\_Y},ρX,Y​=σX​σY​Cov(X,Y)​,$ producing a unitless number in [−1,1].
- ✓

  Correlation captures *linear* association; strong nonlinear dependence can still yield ρ≈0.
- ✓

  Independence ⇒ zero covariance, but zero covariance ⇏ independence in general (e.g., Y=X² with symmetric X).
- ✓

  In sample form, correlation equals cosine similarity between centered data vectors **x** and **y**.
- ✓

  Covariance matrices generalize covariance to many variables and are the core input to PCA via eigenvectors.

## Common Mistakes

- ✗

  Interpreting correlation as causation (confounding variables can create high correlation).
- ✗

  Assuming ρ=0 implies independence (it only rules out linear association unless extra assumptions like joint normality hold).
- ✗

  Comparing covariance magnitudes across datasets with different units/scales (use correlation or standardize first).
- ✗

  Ignoring outliers: a few extreme points can drastically change covariance/correlation and hide the typical pattern.

## Practice

easy

Let X have E[X]=2, Var(X)=9. Let Y = 5 − 2X. Compute Cov(X,Y) and Corr(X,Y).

**Hint:** Use Cov(X, a+bX) = b Var(X). For correlation, note Y is exactly linear in X.

Show solution

Compute covariance:

Y = 5 − 2X ⇒ Cov(X,Y) = Cov(X, 5 − 2X) = −2 Cov(X,X) = −2 Var(X) = −2·9 = −18.

For correlation, since Y is an exact decreasing linear function of X, Corr(X,Y)=−1.

(You can also compute σ\_Y = |−2|σ\_X = 2·3=6, so Corr = (−18)/(3·6)=−1.)

easy

Suppose E[X]=1, E[Y]=3, and E[XY]=10. Compute Cov(X,Y).

**Hint:** Use Cov(X,Y)=E[XY]−E[X]E[Y].

Show solution

Cov(X,Y) = 10 − (1)(3) = 7.

medium

Let X be Uniform(0,1) and Y = X. Compute Corr(X,Y). Then let Z = X² and reason (without heavy computation) whether Corr(X,Z) is closer to 1, closer to 0, or could be negative.

**Hint:** For Y=X, it’s perfect linear. For Z=X² on (0,1), it’s increasing but nonlinear; think about whether larger X tends to mean larger Z.

Show solution

For Y=X, correlation is 1 because Y is an exact positive linear function of X (Y=1·X+0).

For Z=X² with X∈(0,1), Z is strictly increasing in X, so larger X tends to correspond to larger Z. That suggests a positive covariance and positive correlation. However, because the relationship is nonlinear, Corr(X,Z) will be less than 1 (not a perfect straight line). It cannot be negative here because X and X² move in the same direction on (0,1). So Corr(X,Z) is closer to 1 than to 0, but still < 1.

## Connections

Next steps and related nodes:

- •[Principal Component Analysis](/tech-tree/pca/) — PCA uses eigenvectors of the covariance matrix Σ\SigmaΣ to find high-variance directions.

Helpful background refreshers:

- •Variance and standard deviation (prerequisite): understand σ=Var⁡(X)\sigma=\sqrt{\operatorname{Var}(X)}σ=Var(X)​ since correlation divides by σXσY\sigma\_X\sigma\_YσX​σY​.
- •Joint distributions (prerequisite): covariance depends on the joint behavior via E[XY].E[XY].E[XY].

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
