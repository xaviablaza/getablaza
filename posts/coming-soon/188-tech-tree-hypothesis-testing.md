---
title: Hypothesis Testing
description: Testing claims about populations using sample data. p-values, significance.
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
permalink: /tech-tree/hypothesis-testing/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Hypothesis Testing

Probability & StatisticsDifficulty: ★★★☆☆Depth: 7Unlocks: 0

Testing claims about populations using sample data. p-values, significance.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Null and alternative hypotheses (precise competing statements about a population parameter)
- -Test statistic (a single function of the sample that summarizes evidence against the null)
- -Null distribution of the test statistic (sampling distribution assuming the null is true)
- -p-value (probability, computed under the null, quantifying how extreme the observed evidence is)
- -Significance level and decision rule (alpha: pre-specified threshold for rejecting the null)

## Key Symbols & Notation

H0 / Ha (labels for null and alternative hypotheses)p (p-value)alpha (significance level)

## Essential Relationships

- -Compute the test statistic from the sample and compare it to its null distribution.
- -The p-value is the probability, under H0, of observing a test statistic at least as extreme as the observed value.
- -Reject H0 when p-value <= alpha (otherwise fail to reject H0).

## Prerequisites (2)

[Central Limit Theorem6 atoms](/tech-tree/central-limit-theorem/)[Common Distributions6 atoms](/tech-tree/common-distributions/)

## Referenced by (8)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (8)

[Exit CriteriaBusiness

Formalizes the discipline of defining pass/fail thresholds (alpha, power) before evaluating evidence - the statistical foundation of pre-committed acceptance gates](/business/exit-criteria/)[decision ruleBusiness

Decision rules (reject/fail to reject based on p vs α) are the core operational mechanism of hypothesis testing; this node teaches the full statistical framework in which decision rules operate](/business/decision-rule/)[backtestingBusiness

Backtesting is hypothesis testing applied to sequential protocols - you formulate H0 (strategy has no edge), replay historical data, and assess whether observed performance is statistically distinguishable from chance](/business/backtesting/)[quality gateBusiness

A quality gate is structurally a hypothesis test: observe stochastic output, compare against a deterministic threshold, emit a binary pass/fail decision. Hypothesis testing formalizes this as setting a significance level (the gate threshold) and applying a deterministic rejection rule to stochastic data.](/business/quality-gate/)[Quality SystemsBusiness

Statistical process control - the backbone of quality systems - is hypothesis testing applied to production metrics. Control charts test whether a process has shifted out of statistical control.](/business/quality-systems/)[Spot-CheckBusiness

Spot-checking is sampling-based inference - drawing conclusions about overall system quality from a small sample. Understanding sample size, significance, and error rates (Type I/II) determines whether a spot-check regime actually catches failures or gives false confidence.](/business/spot-check/)[auditingBusiness

Auditing formalizes as hypothesis testing - the null is 'model output is correct/safe,' and each audit check (automated or human) is a test that may reject that null with some significance level](/business/auditing/)[Exception ReviewBusiness

Exception review is applied hypothesis testing: define 'normal' as null hypothesis, set a significance threshold, flag items that reject it for human review. The exception threshold IS the significance level.](/business/exception-review/)

Advanced Learning Details

### Graph Position

73

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

7

Chain Length

### Cognitive Load

11

Atomic Elements

46

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (18)

- - Null hypothesis (H0) as a specific claim about a population parameter to be tested
- - Alternative hypothesis (Ha or H1) as the rival claim (one-sided or two-sided)
- - Test statistic: a standardized summary of sample data used to assess H0
- - Null (sampling) distribution of the test statistic: distribution assumed when H0 is true
- - p-value: probability of observing data at least as extreme as observed given H0 is true
- - Significance level (α): pre-chosen threshold for deciding to reject H0
- - Rejection region / critical value(s): region(s) of the test statistic that lead to rejecting H0
- - Type I error: rejecting H0 when H0 is true (false positive)
- - Type II error: failing to reject H0 when Ha is true (false negative)
- - Power of a test: probability of correctly rejecting H0 when a specified alternative is true (1 − β)
- - One-sided (directional) vs two-sided (non-directional) tests
- - t-distribution (Student's t) and degrees of freedom for tests when population SD is unknown
- - Z-test vs t-test: choice of null distribution depending on known/unknown variance
- - Effect size: magnitude of the difference from H0 that is practically important
- - Standard error (as the estimated standard deviation of the estimator used in the test)
- - Decision rule: compare p-value to α or compare test statistic to critical value to accept/reject H0
- - Connection between confidence intervals and two-sided hypothesis tests (CI exclusion implies rejection)
- - Interpretation caveats: p-value is not the probability H0 is true; statistical significance ≠ practical significance

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

You run an A/B test and see Variant B converts 2% better than A. Is that real—or just random luck in the sample? Hypothesis testing is the machinery that turns that question into a repeatable decision procedure.

TL;DR:

Hypothesis testing compares two precise claims (H₀ vs Hₐ) about a population parameter using a test statistic and its null distribution. A p-value is the probability (computed assuming H₀ is true) of seeing evidence at least as extreme as what you observed. You reject H₀ when p ≤ α, where α is a pre-chosen significance level that controls the long-run false-rejection rate.

## What Is Hypothesis Testing?

Hypothesis testing is a structured way to use sample data to evaluate a claim about a population.

The core difficulty is that samples vary. Even if nothing is changing in the population, random sampling will produce different means, proportions, and counts. Hypothesis testing acknowledges this uncertainty and asks:

- •If the null claim were true, **how surprising** would our sample evidence be?
- •Is it surprising enough that we’re willing to reject the null?

### The competing statements: H₀ and Hₐ

A hypothesis test always starts with **two competing hypotheses** about a population parameter (a fixed but unknown number like μ, p, or λ).

- •**Null hypothesis (H₀):** the “status quo” or “no effect / no difference” claim. It is the claim we test *as if it were true*.
- •**Alternative hypothesis (Hₐ):** what we consider if the data provide strong evidence against H₀.

Example (mean):

- •H₀: μ = 100
- •Hₐ: μ ≠ 100

Example (proportion):

- •H₀: p = 0.10
- •Hₐ: p > 0.10

Notice that both hypotheses are statements about the **population**, not the sample. The sample is our window.

### One-sided vs two-sided: the direction matters

The alternative hypothesis encodes what “extreme evidence” means.

- •**Two-sided test:** Hₐ: parameter ≠ value. Extremes are large deviations in either direction.
- •**Right-tailed test:** Hₐ: parameter > value. Extremes are unusually large values of the test statistic.
- •**Left-tailed test:** Hₐ: parameter < value. Extremes are unusually small values.

This choice is not cosmetic. It determines which tail(s) of the null distribution count as “as extreme or more extreme.”

### The workflow in one sentence

1) Choose H₀/Hₐ → 2) compute a test statistic from the sample → 3) compare it to its **null distribution** → 4) compute a p-value → 5) reject or fail to reject using α.

### A visual mental model (keep this in your head)

Under H₀, your test statistic has a distribution. You mark either:

- •a **rejection region** whose total area is α (fixed in advance), or
- •the **p-value region**: area in the tail(s) at least as extreme as the observed statistic.

Both are just shaded areas under the same “null curve.”

#### Static diagram: rejection region (two-sided)

Below is a generic null distribution (often approximately Normal). The two critical values cut off α/2 in each tail.

```
              Null distribution of test statistic (under H₀)

                       /
                      /  \
                     /    \
          __________/      \__________
         /                                \
--------|----|------------------|----|---------> t
      -c    0                  +c
     α/2                        α/2
   (reject)                   (reject)

Decision rule (two-sided): reject H₀ if t ≤ -c or t ≥ +c
```

#### Static diagram: p-value shading (right-tailed)

Here the alternative is “greater than,” so only the right tail counts.

```
              Null distribution of test statistic (under H₀)

                       /
                      /  \
                     /    \
          __________/      \__________
         /                                \
--------|-------------------|\\\\\\\\\\\-> t
       0                 t_obs   p-value area

p-value = P(T ≥ t_obs | H₀)
```

These pictures are the backbone of hypothesis testing. Everything else is computation.

## Core Mechanic 1: Test Statistic and Null Distribution (Where the p-value comes from)

### Why we need a test statistic

A dataset is many numbers. A hypothesis test needs a single number that summarizes the evidence against H₀.

That number is the **test statistic**: a function of the sample.

Common patterns:

- •Sample mean x̄ (or a standardized version)
- •Sample proportion p̂ (or standardized)
- •Count in a Poisson process

But the raw statistic (like x̄) is hard to interpret without scale. We typically convert it into a standardized form that answers:

> “How many standard errors away from the null value is the observed estimate?”

That’s what z-scores and t-scores do.

### Standard error: the scale of sampling noise

If you repeatedly sample n observations from a fixed population, the statistic varies. Its standard deviation is the **standard error (SE)**.

A key CLT-driven idea (you already know CLT) is:

- •For a mean, if σ is the population standard deviation,

Xˉ≈N(μ,σ2n)\bar X \approx \mathcal N\left(\mu, \frac{\sigma^2}{n}\right)Xˉ≈N(μ,nσ2​)

so SE(Xˉ)=σ/n\text{SE}(\bar X) = \sigma/\sqrt{n}SE(Xˉ)=σ/n​.

- •For a proportion, with true proportion p,

p^≈N(p,p(1−p)n)\hat p \approx \mathcal N\left(p, \frac{p(1-p)}{n}\right)p^​≈N(p,np(1−p)​)

so SE(p^)=p(1−p)/n\text{SE}(\hat p) = \sqrt{p(1-p)/n}SE(p^​)=p(1−p)/n​.

### Null distribution: “what we’d see if H₀ were true”

The **null distribution** is the sampling distribution of the test statistic *assuming H₀ is true*.

If H₀ specifies μ = μ₀, then under H₀:

- •Xˉ\bar XXˉ is centered at μ₀ (approximately)
- •the standardized statistic is centered at 0

A canonical z-test statistic for a mean with known σ is:

Z=Xˉ−μ0σ/nZ = \frac{\bar X - \mu\_0}{\sigma/\sqrt{n}}Z=σ/n​Xˉ−μ0​​

Under H₀ (and with CLT / Normal assumptions),

Z∼N(0,1).Z \sim \mathcal N(0,1).Z∼N(0,1).

That last line is crucial: it tells you how to turn an observed Z into a tail probability.

### “Extreme” depends on Hₐ

Once you have the null distribution, “extreme” means “in the tail(s) consistent with Hₐ.”

Let T be your test statistic with observed value t\_obs.

- •Right-tailed (Hₐ: parameter > …):

p-value=P(T≥tobs∣H0)p\text{-value} = P(T \ge t\_{\text{obs}} \mid H\_0)p-value=P(T≥tobs​∣H0​)

- •Left-tailed (Hₐ: parameter < …):

p-value=P(T≤tobs∣H0)p\text{-value} = P(T \le t\_{\text{obs}} \mid H\_0)p-value=P(T≤tobs​∣H0​)

- •Two-sided (Hₐ: parameter ≠ …):

p-value=P(∣T∣≥∣tobs∣∣H0)p\text{-value} = P(|T| \ge |t\_{\text{obs}}| \mid H\_0)p-value=P(∣T∣≥∣tobs​∣∣H0​)

For symmetric null distributions (like Normal), the two-sided p-value is often:

p-value=2 P(T≥∣tobs∣∣H0)p\text{-value} = 2\,P(T \ge |t\_{\text{obs}}| \mid H\_0)p-value=2P(T≥∣tobs​∣∣H0​)

### Rejection regions and α: deciding before seeing data

The p-value measures evidence; α is a decision threshold.

- •**Significance level (α):** a pre-set probability of rejecting H₀ when H₀ is true (long-run).

Decision rule:

- •Reject H₀ if p ≤ α
- •Otherwise, fail to reject H₀

This is equivalent to using **critical values**.

For example, in a two-sided z-test with α = 0.05:

- •critical values are ±1.96
- •reject H₀ if |Z| ≥ 1.96

This equivalence is worth seeing explicitly.

If Z∼N(0,1)Z \sim \mathcal N(0,1)Z∼N(0,1) under H₀, and α = 0.05 two-sided, we choose c so that:

P(∣Z∣≥c)=0.05P(|Z| \ge c) = 0.05P(∣Z∣≥c)=0.05

By symmetry:

P(Z≥c)=0.025P(Z \ge c) = 0.025P(Z≥c)=0.025

So c≈1.96c \approx 1.96c≈1.96.

Then:

- •If z\_obs = 2.3, it lies in the rejection region → p < 0.05 → reject.
- •If z\_obs = 1.2, it lies in the non-rejection region → p > 0.05 → fail to reject.

### What a p-value is (and what it is not)

A p-value is:

- •A probability computed **under H₀**
- •Of seeing a test statistic **at least as extreme** as observed

It is not:

- •The probability that H₀ is true
- •The probability that the result is “due to chance”
- •A measure of effect size

A small p-value means: “If H₀ were true, this would be rare.” It does not, by itself, tell you whether the effect is practically important.

## Core Mechanic 2: One-Sided vs Two-Sided Tests, α Splitting, and Tail Logic (Make the pictures match the rules)

The biggest source of confusion in hypothesis testing is mixing up:

- •the direction of Hₐ
- •the location of the rejection region
- •how the p-value is shaded
- •whether α is split

This section focuses on making the tail logic visual and automatic.

### Step 1: Choose Hₐ first; it defines “extreme”

You should be able to answer: “Which sample outcomes would convince me H₀ is wrong?”

- •If only unusually large values would convince you, use a right-tailed test.
- •If only unusually small values would convince you, use a left-tailed test.
- •If either unusually large or unusually small would convince you, use a two-sided test.

This is not something you should decide after seeing data.

### Step 2: α is area in the rejection region

Think of α as “how much tail area we’re willing to label as ‘reject’ when H₀ is true.”

Here are the three standard rejection-region pictures.

#### Right-tailed test (α all on the right)

```
              Null distribution under H₀

                       /
                      /  \
                     /    \
          __________/      \__________
         /                                \
--------|--------------------|\\\\\\\\\\\-> t
       0                    c
                        α (reject)

Reject if t ≥ c
```

#### Left-tailed test (α all on the left)

```
              Null distribution under H₀

                       /
                      /  \
                     /    \
          __________/      \__________
         /                                \
\\\\\\\\\\\|--------------------|---------> t
       c                    0
  α (reject)

Reject if t ≤ c
```

#### Two-sided test (α split into α/2 + α/2)

```
              Null distribution under H₀

                       /
                      /  \
                     /    \
          __________/      \__________
         /                                \
\\\\\\\|----|------------------|----|\\\\\\\-> t
      -c    0                  +c
     α/2                        α/2

Reject if t ≤ -c or t ≥ +c
```

### Step 3: p-value shading matches the same tail(s)

The p-value is not “α in the tail.” It is the **observed tail area beyond your observed statistic**, using the appropriate tail rule.

If you remember one sentence, use this:

> p-value = shaded area in the tail(s) of the null distribution beyond the observed statistic, in the direction(s) specified by Hₐ.

Examples of shading:

- •Right-tailed: shade to the right of t\_obs
- •Left-tailed: shade to the left of t\_obs
- •Two-sided: shade both tails beyond ±|t\_obs|

### A quick table to prevent tail mistakes

| Test type | Hₐ form | Rejection region area | p-value computed as |
| --- | --- | --- | --- |
| Right-tailed | parameter > value | α in right tail | P(T≥tobs∣H0)P(T ≥ t\_{obs} \mid H₀)P(T≥tobs​∣H0​) |
| Left-tailed | parameter < value | α in left tail | P(T≤tobs∣H0)P(T ≤ t\_{obs} \mid H₀)P(T≤tobs​∣H0​) |
| Two-sided | parameter ≠ value | α/2 each tail | $P( | T | ≥ | t\_{obs} | \mid H₀)$ |

### Connecting p-values to critical values (explicitly)

Suppose we do a right-tailed z-test at α = 0.05.

- •Critical value c is defined by:

P(Z≥c∣H0)=0.05P(Z ≥ c \mid H₀) = 0.05P(Z≥c∣H0​)=0.05

So c≈1.645c ≈ 1.645c≈1.645.

Now compare two observed z-values:

1) z\_obs = 1.2

- •p-value = P(Z ≥ 1.2) ≈ 0.115
- •Since 0.115 > 0.05, fail to reject.

2) z\_obs = 2.0

- •p-value = P(Z ≥ 2.0) ≈ 0.0228
- •Since 0.0228 < 0.05, reject.

The rule “reject if p ≤ α” and the rule “reject if z\_obs ≥ 1.645” always agree because they are the same geometric comparison under the null curve.

### A note on “fail to reject” language

When p > α, we say **fail to reject H₀**, not “accept H₀.”

Why? Because the test is asymmetric:

- •It is designed to control false rejections (Type I error) at rate α.
- •It is not designed to certify H₀ is true.

Large p-values can happen because:

- •H₀ is true, or
- •H₀ is false but the effect is small, or
- •the sample size is too small / noise is high.

## Application/Connection: How Hypothesis Testing Shows Up in Practice (and what it can’t tell you)

Hypothesis testing is a reusable template. Once you internalize the tail logic, you can apply it across many settings.

### Common real-world uses

1) **A/B testing (proportions)**

- •H₀: conversion rate p\_B − p\_A = 0
- •Hₐ: p\_B − p\_A > 0 (or ≠ 0)
- •Test statistic: standardized difference in sample proportions

2) **Quality control (means)**

- •H₀: μ = target weight
- •Hₐ: μ < target weight (underfilling is the concern)

3) **Healthcare / experiments**

- •H₀: mean outcome difference between treatment and control is 0
- •Hₐ: difference ≠ 0

In each case:

- •Choose a parameter
- •Encode claims as H₀/Hₐ
- •Pick a statistic whose null distribution is known or approximable
- •Compute p-value, compare to α

### What α controls (long-run behavior)

α is the probability of rejecting H₀ when H₀ is true:

α=P(reject H0∣H0 true)\alpha = P(\text{reject } H\_0 \mid H\_0 \text{ true})α=P(reject H0​∣H0​ true)

That is a **guarantee about a procedure**, not about a single dataset. If you repeatedly run the same testing procedure in a world where H₀ is actually true, about α fraction of runs will (incorrectly) reject.

This motivates why α should be chosen before looking at the data: it’s part of the design of the decision rule.

### Practical significance vs statistical significance

A tiny effect can be statistically significant if n is huge (SE becomes small). Conversely, a meaningful effect can fail to be significant if n is small.

Because the standardized statistic is often of the form:

test statistic≈estimated effectstandard error\text{test statistic} \approx \frac{\text{estimated effect}}{\text{standard error}}test statistic≈standard errorestimated effect​

Increasing n shrinks SE like $1/\sqrt{n}$, making it easier for a fixed effect to appear “many SEs away.”

In practice, you should pair hypothesis tests with:

- •effect size estimates (difference in means/proportions)
- •confidence intervals (often more interpretable)

### Interpreting p-values responsibly

A correct interpretation template:

- •“Assuming H₀ is true, the probability of observing evidence at least as extreme as what we saw is p.”

Avoid:

- •“There is a p chance H₀ is true.” (That’s Bayesian territory, not what p-values mean.)
- •“p is the probability the result is random.” (Randomness is already in the model.)

### Where this connects next

Hypothesis testing is closely tied to other core stats tools:

- •**Confidence intervals:** dual view of the same sampling logic; a two-sided α test corresponds to whether a (1−α) CI contains the null value.
- •**Power and sample size:** how likely you are to detect an effect when Hₐ is true.
- •**Multiple testing:** running many tests inflates false positives unless corrected.

Even if you don’t go deep into theory, the tail diagrams and “null distribution + shaded area” mental model will transfer directly.

## Worked Examples (3)

### Worked Example 1: One-sample z-test for a mean (two-sided) with p-value and rejection-region view

A factory claims its bolts have mean length μ = 10.0 cm. You sample n = 36 bolts and measure sample mean x̄ = 10.3 cm. Assume the population standard deviation is known: σ = 0.9 cm. Test at significance level α = 0.05.

Hypotheses:

- •H₀: μ = 10.0
- •Hₐ: μ ≠ 10.0 (two-sided)

Test statistic:

Z=Xˉ−μ0σ/nZ = \frac{\bar X - \mu\_0}{\sigma/\sqrt{n}}Z=σ/n​Xˉ−μ0​​

1. Compute the standard error:

   SE = σ/√n = 0.9/√36 = 0.9/6 = 0.15
2. Compute the observed z-value:

   z\_obs = (x̄ − μ₀)/SE

   = (10.3 − 10.0)/0.15

   = 0.3/0.15

   = 2.0
3. Compute the two-sided p-value:

   p = P(|Z| ≥ |2.0| | H₀)

   = 2·P(Z ≥ 2.0)

   Using standard normal tables (or known value): P(Z ≥ 2.0) ≈ 0.0228

   So p ≈ 2·0.0228 = 0.0456
4. Decision using p-value:

   Since p ≈ 0.0456 ≤ α = 0.05, reject H₀.
5. Same decision using rejection region (critical values):

   For α = 0.05 two-sided, critical values are ±1.96.

   Reject if |z\_obs| ≥ 1.96.

   Here |2.0| ≥ 1.96, so reject.

**Insight:** Two equivalent lenses: (1) compare p to α (shaded tail area beyond ±|z\_obs|), or (2) compare z\_obs to critical values (fixed α/2 tails). Both are literally the same geometry under the null distribution.

### Worked Example 2: One-sample z-test for a proportion (right-tailed) and tail shading

A website historically has conversion rate p = 0.10. After a UI change, you observe n = 400 visitors with x = 52 conversions, so p̂ = 52/400 = 0.13. Test if conversion increased at α = 0.01.

Hypotheses:

- •H₀: p = 0.10
- •Hₐ: p > 0.10 (right-tailed)

Approximate (CLT) test statistic:

Z=p^−p0p0(1−p0)/nZ = \frac{\hat p - p\_0}{\sqrt{p\_0(1-p\_0)/n}}Z=p0​(1−p0​)/n​p^​−p0​​

Under H₀, Z ≈ N(0,1).

1. Compute p̂:

   p̂ = 52/400 = 0.13
2. Compute the standard error under H₀:

   SE = √(p₀(1−p₀)/n)

   = √(0.10·0.90/400)

   = √(0.09/400)

   = √(0.000225)

   = 0.015
3. Compute the observed z-value:

   z\_obs = (p̂ − p₀)/SE

   = (0.13 − 0.10)/0.015

   = 0.03/0.015

   = 2.0
4. Compute the right-tailed p-value:

   p = P(Z ≥ 2.0 | H₀) ≈ 0.0228
5. Decision:

   Compare p to α:

   0.0228 > 0.01, so fail to reject H₀.

   Rejection-region equivalent:

   For a right-tailed test at α = 0.01, the critical value is about 2.326.

   Since 2.0 < 2.326, z\_obs is not in the rejection region, so fail to reject.

**Insight:** Same z\_obs can be ‘significant’ at α=0.05 but not at α=0.01. Tightening α shrinks the rejection region (less shaded tail area), making rejection harder.

### Worked Example 3: Same data, different alternative (two-sided vs one-sided) changes the p-value

Re-use Example 1 where z\_obs = 2.0 from testing μ₀ = 10.0.

Consider two different alternatives:

A) Hₐ: μ > 10.0 (right-tailed)

B) Hₐ: μ ≠ 10.0 (two-sided)

Compute the p-values and compare.

1. Right-tailed p-value (μ > 10):

   p\_right = P(Z ≥ 2.0 | H₀) ≈ 0.0228
2. Two-sided p-value (μ ≠ 10):

   p\_two = P(|Z| ≥ 2.0 | H₀)

   = 2·P(Z ≥ 2.0)

   ≈ 2·0.0228

   = 0.0456
3. Interpretation:

   The two-sided p-value is (for symmetric nulls) twice the one-sided p-value because it counts extremes in both tails.

**Insight:** This is why you must choose one- vs two-sided before seeing the data: you’re defining what counts as “as extreme.” The diagram literally changes from one shaded tail to two shaded tails.

## Key Takeaways

- ✓

  A hypothesis test compares two precise population claims: H₀ (baseline) vs Hₐ (the direction/shape of deviation you care about).
- ✓

  A test statistic compresses the sample into one number that measures evidence against H₀, often as “estimate minus null value, measured in standard errors.”
- ✓

  The null distribution is the sampling distribution of the test statistic assuming H₀ is true; it’s the reference curve you shade areas under.
- ✓

  The p-value is a probability computed under H₀: the tail area at least as extreme as the observed statistic, in the direction(s) specified by Hₐ.
- ✓

  α is chosen in advance and is the total area of the rejection region under the null curve; in two-sided tests it splits into α/2 per tail.
- ✓

  The rules “reject if p ≤ α” and “reject if statistic is beyond critical value(s)” are equivalent views of the same geometry.
- ✓

  Failing to reject H₀ is not the same as proving H₀; it may reflect low power, small effects, or high noise.
- ✓

  Statistical significance (small p) is not the same as practical importance; always consider effect size and uncertainty (e.g., confidence intervals).

## Common Mistakes

- ✗

  Interpreting the p-value as P(H₀ is true) instead of P(data as-or-more-extreme | H₀).
- ✗

  Choosing one-sided vs two-sided after looking at the data, which silently changes the tail area you count as ‘extreme.’
- ✗

  Forgetting to split α into α/2 and α/2 for two-sided tests, leading to wrong critical values and wrong conclusions.
- ✗

  Saying “accept H₀” when p > α; the correct language is “fail to reject H₀,” because the test is not designed to confirm the null.

## Practice

easy

A machine fills bottles with target mean μ₀ = 500 ml. You sample n = 64 bottles and get x̄ = 497 ml. Assume σ = 16 ml is known. Test H₀: μ = 500 vs Hₐ: μ < 500 at α = 0.05. Compute z\_obs and the p-value, and decide.

**Hint:** Use SE = σ/√n, then z = (x̄ − μ₀)/SE. Since Hₐ is left-tailed, p = P(Z ≤ z\_obs).

Show solution

SE = 16/√64 = 16/8 = 2.

z\_obs = (497 − 500)/2 = −3/2 = −1.5.

Left-tailed p-value: p = P(Z ≤ −1.5) ≈ 0.0668.

Since 0.0668 > 0.05, fail to reject H₀ (not enough evidence at α=0.05 that the mean is below 500).

medium

A support team claims their on-time rate is p₀ = 0.95. In a week, they handle n = 200 tickets and 184 are on time (p̂ = 0.92). Test H₀: p = 0.95 vs Hₐ: p ≠ 0.95 at α = 0.05 using a normal approximation. Compute z\_obs and decide.

**Hint:** Two-sided: p = 2·P(Z ≥ |z\_obs|). Use SE under H₀: √(p₀(1−p₀)/n).

Show solution

p̂ = 184/200 = 0.92.

SE = √(0.95·0.05/200) = √(0.0475/200) = √(0.0002375) ≈ 0.01541.

z\_obs = (0.92 − 0.95)/0.01541 ≈ −0.03/0.01541 ≈ −1.947.

Two-sided p-value: p = 2·P(Z ≥ 1.947).

P(Z ≥ 1.947) ≈ 0.0257, so p ≈ 0.0514.

Since 0.0514 > 0.05, fail to reject H₀ (barely).

hard

You compute a test statistic with observed value t\_obs = 2.4. Under H₀, T ∼ N(0,1). (a) Find the right-tailed p-value. (b) Find the two-sided p-value. (c) For α = 0.05, state reject/fail-to-reject for each alternative.

**Hint:** Use standard normal tail probabilities. Two-sided p is twice the one-sided tail beyond |t\_obs|.

Show solution

(a) Right-tailed: p\_right = P(Z ≥ 2.4) ≈ 0.0082.

(b) Two-sided: p\_two = 2·P(Z ≥ 2.4) ≈ 2·0.0082 = 0.0164.

(c) At α=0.05:

- •Right-tailed Hₐ: parameter > value → reject (0.0082 ≤ 0.05).
- •Two-sided Hₐ: parameter ≠ value → reject (0.0164 ≤ 0.05).

## Connections

[Central Limit Theorem](/tech-tree/central-limit-theorem/)

[Confidence Intervals](/tech-tree/confidence-intervals/)

[Type I and Type II Errors, Power](/tech-tree/statistical-power/)

[Multiple Hypothesis Testing](/tech-tree/multiple-testing/)

[A/B Testing](/tech-tree/ab-testing/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
