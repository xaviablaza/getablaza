---
title: Law of Large Numbers
description: Sample mean converges to expected value as sample size grows.
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
inspiration_url: https://templeton.host/tech-tree/law-large-numbers/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/law-large-numbers/](https://templeton.host/tech-tree/law-large-numbers/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Law of Large Numbers

Probability & StatisticsDifficulty: ★★★☆☆Depth: 4Unlocks: 9

Sample mean converges to expected value as sample size grows.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Independent, identically distributed (iid) random variables
- -Convergence in probability (mode of convergence for random variables)

## Key Symbols & Notation

X\_bar (sample mean)

## Essential Relationships

- -X\_bar = (1/n) \* sum\_{i=1}^n X\_i (definition of the sample mean)
- -If X\_1, X\_2, ... are iid with finite expectation E[X], then X\_bar ->\_p E[X] as n -> infinity (Law of Large Numbers)

## Prerequisites (2)

[Expected Value5 atoms](/tech-tree/expected-value/)[Limits5 atoms](/tech-tree/limits/)

## Unlocks (2)

[Central Limit Theoremlvl 3](/tech-tree/central-limit-theorem/)[Monte Carlo Methodslvl 4](/tech-tree/monte-carlo/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[insuranceBusiness

LLN is why insurance works as a business: with enough policyholders, actual aggregate claims converge to E[claims], making the premium predictably sufficient](/business/insurance/)[Quality ControlBusiness

The Law of Large Numbers is the exact theorem that explains why quality-control sampling works: sample means converge to the population mean as n grows, which is precisely why polls, batch sampling, and casino house edges are reliable.](/business/quality-control/)

Advanced Learning Details

### Graph Position

45

Depth Cost

9

Fan-Out (ROI)

4

Bottleneck Score

4

Chain Length

### Cognitive Load

5

Atomic Elements

25

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (9)

- - Sequence of random variables (X1, X2, ..., Xn) as repeated draws from a distribution
- - Independent and identically distributed (i.i.d.) assumption
- - Sample mean (empirical average) as a statistic computed from data
- - Estimator consistency: an estimator that converges to the true parameter as sample size grows
- - Modes of probabilistic convergence (distinct from deterministic limits): convergence in probability
- - Stronger mode: almost sure (a.s.) convergence
- - Probability-of-deviation statements: using probability to quantify how far the sample mean is from the true mean
- - Role of variance in sampling: variability of individual observations affecting the variability of the sample mean
- - Practical interpretation: empirical/frequency interpretation of expectation (long-run average of observed values)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

You flip a coin 10 times and get 8 heads. That doesn’t mean the coin is biased—small samples are noisy. But if you flip it 10,000 times, the fraction of heads becomes very hard to “keep away” from 0.5. The Law of Large Numbers (LLN) is the formal statement of that stabilizing effect: averages of many independent draws tend to settle near the expected value.

TL;DR:

For iid random variables X₁, X₂, … with finite expected value μ = E[X], the sample mean X̄ₙ = (1/n)∑ᵢ₌₁ⁿ Xᵢ converges in probability to μ as n → ∞. Practically: with enough independent data, averages become predictable (even though individual outcomes stay random).

## What Is the Law of Large Numbers?

### The problem it solves (why we need it)

Probability models talk about *expected value* μ = E[X]. But expectation is not something you directly observe in one experiment—you observe outcomes.

So there’s a natural question:

> If I repeatedly sample from a random process, does the average of what I see approach the theoretical expectation?

LLN is the bridge between *theory* (μ) and *data* (sample averages).

### The main object: the sample mean

Let X₁, X₂, … be random variables representing repeated measurements (e.g., repeated coin flips coded as 1=heads, 0=tails; or repeated customer waiting times; or repeated sensor readings).

Define the **sample mean** after n samples:

X̄ₙ = (1/n) ∑ᵢ₌₁ⁿ Xᵢ

This is the quantity you compute from data.

### Informal statement

If X₁, X₂, … are **iid** (independent and identically distributed) and have a finite mean μ, then:

- •for small n, X̄ₙ can vary a lot,
- •for large n, X̄ₙ is very likely to be close to μ.

This is not because randomness “goes away,” but because positive and negative deviations tend to cancel when you average many independent samples.

### Formal statement (Weak Law of Large Numbers)

The most common version used in statistics and ML is the **Weak Law of Large Numbers (WLLN)**:

X̄ₙ → μ **in probability** as n → ∞.

That sentence uses a key convergence idea. Unpacking it:

For every ε > 0,

P(|X̄ₙ − μ| > ε) → 0 as n → ∞.

Interpretation: the probability that the sample mean differs from μ by more than ε becomes tiny for large n.

### What LLN is *not*

LLN does **not** say:

- •“X̄ₙ equals μ for large n.” It says it becomes *likely* to be close.
- •“Individual samples Xᵢ become less random.” Individual draws stay just as random.
- •“Any sequence averages to its expectation.” Conditions matter (especially independence and finite mean).

### A helpful intuition: averaging reduces relative noise

If each Xᵢ has typical fluctuation scale σ (standard deviation), the average X̄ₙ has fluctuation scale roughly σ/√n. That √n in the denominator is the core intuition for why averages stabilize. (This also hints at the Central Limit Theorem you’ll unlock later.)

### Two versions you might hear about

There are multiple LLNs. Two common ones:

| Name | Statement (informal) | Mode of convergence | Typical assumptions |
| --- | --- | --- | --- |
| Weak LLN | X̄ₙ gets close to μ with high probability | In probability | iid, finite variance (one sufficient condition) |
| Strong LLN | X̄ₙ → μ “almost surely” | Almost sure | iid, E[ | X | ] < ∞ (common condition) |

In this node we emphasize **weak LLN** because it connects directly to statistical guarantees and concentration-style reasoning.

## Core Mechanic 1: iid Samples and Why Independence Matters

### Why “identically distributed” matters

“Identically distributed” means every Xᵢ comes from the same distribution:

- •same mean μ,
- •same variance σ² (if it exists),
- •same tail behavior, etc.

This ensures that when you average, you’re averaging *comparable* quantities. If the distribution changes over time (non-stationarity), the “target” expectation might drift, and the average may not settle.

Example of failure without identical distribution:

- •Suppose E[Xᵢ] = i (grows with i). Then X̄ₙ’s expectation also grows, and there is no single μ to converge to.

### Why independence matters

Independence is the cancellation engine.

If Xᵢ are independent, deviations above μ in one sample don’t systematically force deviations above μ in others. Over many draws, positive and negative deviations tend to balance.

If they’re *correlated*, then errors can reinforce instead of cancel.

A quick illustration:

- •If X₁ = X₂ = … = Xₙ (perfect dependence), then X̄ₙ = X₁ for all n.
- •The average does not stabilize with n; you never “get more information” by repeating the same value.

### The variance calculation that explains stabilization

Assume X₁, …, Xₙ are iid with mean μ and variance Var(Xᵢ) = σ² < ∞.

Compute Var(X̄ₙ).

Start with:

X̄ₙ = (1/n) ∑ᵢ₌₁ⁿ Xᵢ

Then:

Var(X̄ₙ)

= Var((1/n) ∑ᵢ₌₁ⁿ Xᵢ)

= (1/n²) Var(∑ᵢ₌₁ⁿ Xᵢ)

Now use independence:

Var(∑ᵢ₌₁ⁿ Xᵢ) = ∑ᵢ₌₁ⁿ Var(Xᵢ) = ∑ᵢ₌₁ⁿ σ² = nσ²

So:

Var(X̄ₙ) = (1/n²)(nσ²) = σ² / n

That is the quantitative form of “averaging reduces noise.” The standard deviation of X̄ₙ is:

SD(X̄ₙ) = √Var(X̄ₙ) = σ/√n

This is why doubling your sample size does **not** halve your error—it shrinks like 1/√n.

### Turning variance shrinkage into a probability guarantee (Chebyshev)

To connect to “converges in probability,” we need a bound on:

P(|X̄ₙ − μ| > ε)

Chebyshev’s inequality says for any random variable Y with finite variance:

P(|Y − E[Y]| ≥ ε) ≤ Var(Y)/ε²

Apply it to Y = X̄ₙ. Note E[X̄ₙ] = μ (linearity of expectation):

P(|X̄ₙ − μ| ≥ ε)

≤ Var(X̄ₙ)/ε²

= (σ²/n)/ε²

= σ²/(nε²)

Now observe what happens as n → ∞:

σ²/(nε²) → 0

Therefore:

P(|X̄ₙ − μ| ≥ ε) → 0

This is exactly:

X̄ₙ → μ in probability.

So one clean path to LLN is:

1) independence ⇒ Var(X̄ₙ) = σ²/n

2) Chebyshev ⇒ probability of large deviation ≤ σ²/(nε²)

3) RHS → 0 ⇒ convergence in probability

### What conditions are actually required?

The derivation above assumes finite variance. LLN can still hold under weaker conditions (e.g., finite mean without finite variance for strong LLN in some forms), but for many practical ML/statistics contexts, “finite variance + iid” is the standard mental model.

A practical checklist:

| Assumption | What it buys you | What breaks without it |
| --- | --- | --- |
| Independence | variances add; cancellation of noise | correlations can prevent shrinkage |
| Identical distribution | stable target μ | drift makes X̄ chase a moving target |
| Finite mean E[X] | defines μ | no meaningful target to converge to |
| Finite variance Var(X) | easy Chebyshev proof + rates | heavy tails can slow/complicate convergence |

## Core Mechanic 2: Convergence in Probability (What the Limit Actually Means)

### Why we need a new kind of “limit”

You already know limits for numbers and functions: aₙ → a means the sequence of numbers gets arbitrarily close to a.

But X̄ₙ is a **random variable**. For each n, X̄ₙ is not a single number—it’s a distribution over possible sample means.

So “X̄ₙ approaches μ” must mean something like:

- •the distribution of X̄ₙ concentrates near μ,
- •large deviations become unlikely.

That is exactly what convergence in probability captures.

### Definition (slow and explicit)

We say Xₙ → c **in probability** if:

∀ ε > 0, P(|Xₙ − c| > ε) → 0 as n → ∞.

Key points:

- •ε is a tolerance you choose (0.1, 0.01, etc.).
- •The event |Xₙ − c| > ε is “we missed by more than ε.”
- •Convergence in probability says that event’s probability goes to zero.

### Connecting to LLN

LLN states:

X̄ₙ → μ in probability.

Meaning:

∀ ε > 0, P(|X̄ₙ − μ| > ε) → 0.

This is the statement you use when you want to justify:

- •“With enough samples, my empirical average is reliable.”

### Visual intuition: shrinking spread

Imagine the sampling distribution of X̄ₙ as n increases:

- •Center stays at μ (since E[X̄ₙ] = μ)
- •Spread shrinks like σ/√n

So the probability mass near μ grows, and the mass far away shrinks.

Even without drawing the picture, you can think: the region (μ − ε, μ + ε) captures more and more probability.

### Convergence in probability vs almost sure (high-level)

Sometimes learners hear “converges almost surely” and assume it’s the same. It’s stronger.

- •In probability: for large n, it is *unlikely* to be far from μ.
- •Almost surely: with probability 1 over the infinite sequence of samples, the realized X̄ₙ(ω) actually approaches μ as a numerical limit.

In this node, the weak LLN is enough to support most statistical reasoning and to motivate Monte Carlo.

### A practical reading: sample size as a knob

Chebyshev gave:

P(|X̄ₙ − μ| ≥ ε) ≤ σ²/(nε²)

Treat it like a design inequality. Want the failure probability ≤ δ?

Require:

σ²/(nε²) ≤ δ

Solve for n:

n ≥ σ²/(δ ε²)

This is not always tight, but it teaches a key scaling law:

- •error tolerance ε appears as 1/ε²
- •confidence (1 − δ) appears as 1/δ
- •variance σ² makes the problem harder

Even if you later use sharper inequalities (Hoeffding, Bernstein), LLN is the conceptual foundation: *more samples ⇒ more reliable averages*.

### A note about vectors (for ML context)

Often in ML you average vectors (e.g., average gradient estimates). If **Xᵢ** are iid random vectors in ℝᵈ with mean **μ** = E[**X**], then a vector-valued LLN holds under similar finite-moment conditions:

**X̄ₙ** = (1/n) ∑ᵢ₌₁ⁿ **Xᵢ** → **μ** (in probability, componentwise).

To measure error you might use a norm like ‖**X̄ₙ** − **μ**‖.

You don’t need the full vector LLN here, but it’s worth seeing how naturally the scalar idea generalizes.

## Application/Connection: Why LLN Powers Statistics, Monte Carlo, and the CLT

### 1) Statistics: why sample averages estimate expectations

Many estimators are averages:

- •sample mean estimates E[X]
- •sample proportion estimates P(event)
- •empirical risk estimates expected loss

If you define a quantity of interest as an expectation:

μ = E[g(X)]

and you can sample X₁, …, Xₙ iid, then you can estimate μ by:

μ̂ₙ = (1/n) ∑ᵢ₌₁ⁿ g(Xᵢ)

LLN says μ̂ₙ → μ in probability (under the same style of assumptions). This is the justification for “plug in the average.”

### 2) Monte Carlo: turning expectations into computation

Monte Carlo methods rely on the identity:

μ = E[g(X)]

When μ is hard to compute analytically (e.g., high-dimensional integrals), you estimate it with samples. LLN is the guarantee that:

(1/n) ∑ g(Xᵢ)

stabilizes as n grows.

Without LLN, Monte Carlo would be a gamble with no convergence story.

### 3) Central Limit Theorem: what LLN doesn’t tell you

LLN tells you *convergence happens*, but it doesn’t describe the *shape* of fluctuations.

The CLT (which you’ll unlock next) refines the picture: roughly,

√n (X̄ₙ − μ)

approaches a normal distribution with variance σ².

So you can build approximate confidence intervals, p-values, and error bars.

Relationship summary:

| Concept | What it answers | Typical output |
| --- | --- | --- |
| LLN | Does X̄ₙ get close to μ? | Convergence guarantee |
| CLT | How does X̄ₙ fluctuate around μ for large n? | Approximate normal distribution |

### 4) ML connection: empirical risk minimization (ERM)

In supervised learning, you often want to minimize expected loss:

R(θ) = E[L(θ; Z)]

But you only have data Z₁, …, Zₙ. You minimize empirical risk:

R̂ₙ(θ) = (1/n) ∑ᵢ₌₁ⁿ L(θ; Zᵢ)

LLN suggests that for a *fixed* θ, R̂ₙ(θ) → R(θ) in probability as n increases.

Caution: learning theory needs uniform convergence over θ, which is a deeper topic (VC dimension, Rademacher complexity). But LLN is the first stepping stone: averages over iid data approximate expectations.

### 5) Why the law is so widely applicable

Because expectations are linear and averaging is simple, LLN becomes a universal tool:

- •physics (average energy)
- •finance (average return)
- •operations (average queue time)
- •A/B testing (difference in sample means)
- •simulation (estimated probability of rare events)

Whenever you see “estimate an expectation by sampling,” LLN is the hidden backbone.

## Worked Examples (3)

### Coin flips as Bernoulli variables (LLN in the simplest case)

Let Xᵢ = 1 if the i-th flip is heads, 0 otherwise. Assume a fair coin: P(Xᵢ = 1) = 0.5. Then μ = E[Xᵢ] = 0.5. The sample mean X̄ₙ is the fraction of heads in n flips.

1. Compute the expectation:

   E[Xᵢ] = 1·P(Xᵢ=1) + 0·P(Xᵢ=0)

   = 1·0.5 + 0·0.5

   = 0.5

   So μ = 0.5.
2. Compute the variance of one flip:

   Var(Xᵢ) = E[Xᵢ²] − (E[Xᵢ])².

   But Xᵢ ∈ {0,1} so Xᵢ² = Xᵢ.

   Therefore E[Xᵢ²] = E[Xᵢ] = 0.5.

   So Var(Xᵢ) = 0.5 − (0.5)² = 0.5 − 0.25 = 0.25.
3. Compute the variance of the sample mean using iid independence:

   Var(X̄ₙ) = Var((1/n)∑ᵢ₌₁ⁿ Xᵢ)

   = (1/n²) Var(∑ᵢ₌₁ⁿ Xᵢ)

   = (1/n²) ∑ᵢ₌₁ⁿ Var(Xᵢ)

   = (1/n²) · n · 0.25

   = 0.25/n.
4. Use Chebyshev to bound the probability of deviating from 0.5:

   For any ε > 0,

   P(|X̄ₙ − 0.5| ≥ ε) ≤ Var(X̄ₙ)/ε² = (0.25/n)/ε² = 0.25/(nε²).
5. See the LLN limit directly:

   As n → ∞, 0.25/(nε²) → 0.

   So P(|X̄ₙ − 0.5| ≥ ε) → 0.

   Hence X̄ₙ → 0.5 in probability.

**Insight:** Even though each flip stays maximally random, the *average of many flips* becomes predictable because its variance shrinks like 1/n. LLN formalizes the everyday belief that “more trials smooth out randomness.”

### Monte Carlo estimation of an expectation (why simulation converges)

Suppose you want μ = E[X²] where X ~ Uniform(0, 1). You can compute it analytically, but pretend you can’t. You sample X₁, …, Xₙ iid ~ Uniform(0,1) and estimate μ by μ̂ₙ = (1/n)∑ Xᵢ².

1. Define the estimator as a sample mean of a transformed variable:

   Let Yᵢ = Xᵢ².

   Then μ̂ₙ = (1/n)∑ᵢ₌₁ⁿ Yᵢ.

   If the Xᵢ are iid, then the Yᵢ are also iid (same transformation applied independently).
2. Compute the true expectation (for reference):

   μ = E[X²] = ∫₀¹ x² dx

   = [x³/3]₀¹

   = 1/3.
3. Check the LLN conditions:

   E[Yᵢ] = E[Xᵢ²] = 1/3 is finite.

   Also Var(Yᵢ) is finite because 0 ≤ Yᵢ ≤ 1.

   So the weak LLN applies.
4. State the LLN conclusion:

   μ̂ₙ = (1/n)∑ Yᵢ → E[Y] = 1/3 in probability as n → ∞.

   Equivalently, for every ε > 0:

   P(|μ̂ₙ − 1/3| > ε) → 0.
5. Optional rate intuition via variance shrinkage:

   Var(μ̂ₙ) = Var(Y)/n.

   So typical error scale is SD(μ̂ₙ) = √Var(Y)/√n.

   This explains why Monte Carlo accuracy improves like 1/√n.

**Insight:** Monte Carlo is not magic—it’s “just” LLN applied to a clever choice of Y = g(X). Once you can sample X, you can estimate E[g(X)] by averaging g(Xᵢ), and LLN guarantees stabilization.

### A dependence counterexample: repeating the same measurement doesn’t average out

Let X be a random variable with E[X] = μ and Var(X) = σ² > 0. Define X₁ = X₂ = … = Xₙ = X (perfect dependence). Consider X̄ₙ.

1. Compute the sample mean:

   X̄ₙ = (1/n)∑ᵢ₌₁ⁿ Xᵢ = (1/n) · nX = X.
2. Compute deviation probability:

   For any ε > 0,

   P(|X̄ₙ − μ| > ε) = P(|X − μ| > ε).

   This probability does not depend on n.
3. Conclude no convergence in probability (unless X is degenerate):

   Since P(|X̄ₙ − μ| > ε) stays constant with n, it does not go to 0.

   Therefore X̄ₙ does not converge to μ in probability.

**Insight:** LLN is not “about large n” alone. It is about *independent information*. If your samples are fully dependent, n is an illusion—you did not actually collect more evidence.

## Key Takeaways

- ✓

  The sample mean is X̄ₙ = (1/n)∑ᵢ₌₁ⁿ Xᵢ; LLN explains why it becomes stable for large n.
- ✓

  Weak LLN: for iid Xᵢ with finite mean μ, X̄ₙ → μ in probability, i.e., ∀ ε > 0, P(|X̄ₙ − μ| > ε) → 0.
- ✓

  Independence is crucial: it allows Var(∑ Xᵢ) = ∑ Var(Xᵢ), leading to Var(X̄ₙ) = σ²/n.
- ✓

  Chebyshev’s inequality converts variance shrinkage into a probability guarantee: P(|X̄ₙ − μ| ≥ ε) ≤ σ²/(nε²).
- ✓

  LLN is the core justification for using averages as estimators (proportions, risks, mean losses).
- ✓

  Monte Carlo methods are LLN in action: estimate E[g(X)] by averaging g(Xᵢ).
- ✓

  LLN guarantees convergence but not the exact distribution of errors; CLT describes the √n-scaled fluctuations.

## Common Mistakes

- ✗

  Thinking LLN says the sample mean becomes exactly equal to μ for large n; it only says deviations become unlikely.
- ✗

  Ignoring dependence (e.g., time series autocorrelation) and applying LLN as if samples were independent.
- ✗

  Assuming “more data” always helps equally; error typically shrinks like 1/√n, so gains diminish.
- ✗

  Forgetting conditions (like finite mean/variance) and being surprised when heavy-tailed data behaves erratically.

## Practice

easy

Let X₁, X₂, … be iid with E[Xᵢ] = 10 and Var(Xᵢ) = 9. Use Chebyshev to find an n such that P(|X̄ₙ − 10| ≥ 1) ≤ 0.05.

**Hint:** Use P(|X̄ₙ − μ| ≥ ε) ≤ σ²/(nε²) with σ² = 9, ε = 1, and set the RHS ≤ 0.05.

Show solution

Chebyshev:

P(|X̄ₙ − 10| ≥ 1) ≤ Var(X̄ₙ)/1².

Var(X̄ₙ) = σ²/n = 9/n.

Require 9/n ≤ 0.05 ⇒ n ≥ 9/0.05 = 180.

So n = 180 suffices (or any larger n).

medium

Let Xᵢ be iid Bernoulli(p): P(Xᵢ=1)=p, P(Xᵢ=0)=1−p. Show that X̄ₙ converges in probability to p using the variance + Chebyshev approach.

**Hint:** Compute E[Xᵢ] and Var(Xᵢ)=p(1−p). Then compute Var(X̄ₙ) and apply Chebyshev.

Show solution

Compute expectation:

E[Xᵢ] = 1·p + 0·(1−p) = p.

So μ = p.

Compute variance:

Since Xᵢ² = Xᵢ,

Var(Xᵢ) = E[Xᵢ²] − (E[Xᵢ])² = E[Xᵢ] − p² = p − p² = p(1−p).

Let σ² = p(1−p).

Variance of the mean (iid independence):

Var(X̄ₙ) = σ²/n = p(1−p)/n.

Chebyshev:

P(|X̄ₙ − p| ≥ ε) ≤ Var(X̄ₙ)/ε² = p(1−p)/(nε²).

As n → ∞, p(1−p)/(nε²) → 0.

Thus P(|X̄ₙ − p| ≥ ε) → 0 for every ε > 0, i.e., X̄ₙ → p in probability.

hard

You collect data from a process with strong positive correlation (e.g., Xᵢ = Z + noiseᵢ where Z is a shared random offset). Explain qualitatively how this can slow or break the stabilization of X̄ₙ compared to the iid case.

**Hint:** Think about what happens if many samples share the same random component; averaging cancels independent noise but not shared noise.

Show solution

If Xᵢ share a common random offset Z, then each sample contains the same source of randomness. Averaging reduces only the independent part (the noiseᵢ), but the shared part Z does not cancel because it appears in every term.

For example, if Xᵢ = Z + εᵢ with E[Z]=0 and εᵢ iid with E[εᵢ]=0, then

X̄ₙ = Z + (1/n)∑ εᵢ.

As n → ∞, (1/n)∑ εᵢ → 0 (by LLN for εᵢ), but Z remains. So X̄ₙ converges to Z, not to 0, and the limiting value is still random. This shows why independence (or at least weak dependence) is crucial for LLN-style stabilization.

## Connections

Next nodes you can study:

- •[Central Limit Theorem](/tech-tree/central-limit-theorem/) — strengthens LLN by describing the *distribution* of √n(X̄ₙ − μ).
- •[Monte Carlo Methods](/tech-tree/monte-carlo/) — uses LLN to justify estimating expectations/integrals via sampling.

Related background nodes to review:

- •[Expected Value](/tech-tree/expected-value/)
- •[Limits](/tech-tree/limits/)
- •[Independent and Identically Distributed (iid)](/tech-tree/iid/)
- •[Convergence in Probability](/tech-tree/convergence-in-probability/)

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
