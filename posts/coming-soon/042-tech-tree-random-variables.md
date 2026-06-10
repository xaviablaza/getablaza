---
title: Random Variables
description: Variables whose values are outcomes of random phenomena. Discrete vs continuous.
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
permalink: /tech-tree/random-variables/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Random Variables

Probability & StatisticsDifficulty: ★★☆☆☆Depth: 2Unlocks: 75

Variables whose values are outcomes of random phenomena. Discrete vs continuous.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Random variable: a function mapping each outcome in the sample space to a real number (it is a rule, not a single value).
- -Cumulative distribution as the distributional summary: F\_X(x) = P(X <= x), which fully characterizes the probabilities associated with the random variable.
- -Discrete vs continuous distinction: discrete RVs place probability mass on countable values (described by a PMF); continuous RVs are described by a density (PDF) and probabilities are given by integrals (point probabilities are zero).

## Key Symbols & Notation

X (capital letter) denotes the random variable (the mapping).F\_X(x) denotes the cumulative distribution function of X, F\_X(x) = P(X <= x).

## Essential Relationships

- -Probabilities from the CDF: for any a<b, P(a < X <= b) = F\_X(b) - F\_X(a); equivalently, this equals the sum of PMF values over the interval for discrete RVs or the integral of the PDF over the interval for continuous RVs.

## Prerequisites (2)

[Basic Probability6 atoms](/tech-tree/probability-basic/)[Functions6 atoms](/tech-tree/functions-basic/)

## Unlocks (2)

[Expected Valuelvl 2](/tech-tree/expected-value/)[Common Distributionslvl 2](/tech-tree/common-distributions/)

## Referenced by (5)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (5)

[Expected ValueBusiness

Expected value is defined as a property of a random variable; understanding discrete vs continuous random variables and their probability mass/density functions is the direct prerequisite for computing E[X].](/business/expected-value/)[SecurityBusiness

A security's future price and return are modeled as random variables with probability distributions over possible outcomes - this is the foundational abstraction for any quantitative reasoning about security valuation, risk, or portfolio construction.](/business/security/)[Asset ClassBusiness

The abstraction that makes 'same math, different asset class' work: modeling each asset class's returns as a random variable lets you apply identical probabilistic machinery (expected value, variance, distributions, correlation) regardless of the underlying asset](/business/asset-class/)[Single-Period ReturnsBusiness

A single-period return is modeled as a random variable with a distribution over possible outcomes, which is the formal foundation for all return analysis](/business/single-period-returns/)[Investment InstrumentBusiness

The concept's core claim - each opportunity has a 'return distribution' - is precisely the definition of a random variable: a variable whose values are outcomes of a random phenomenon, discrete or continuous, with an associated probability distribution over possible returns.](/business/investment-instrument/)

Advanced Learning Details

### Graph Position

24

Depth Cost

75

Fan-Out (ROI)

29

Bottleneck Score

2

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

### All Concepts (12)

- - Random variable: a variable defined as a function that maps outcomes of a random experiment (the sample space) to real numbers
- - Realization/value of a random variable: the actual numeric output produced by the random variable (usually written as a lowercase x)
- - Discrete random variable: a random variable that takes a countable set of values (e.g., finite or countably infinite)
- - Continuous random variable: a random variable that takes values from intervals or other uncountable sets
- - Probability distribution of a random variable: the rule that assigns probabilities to values or sets of values of the random variable
- - Probability mass function (pmf): the function p(x) = P(X = x) that gives probabilities for each value of a discrete random variable
- - Probability density function (pdf): the function f(x) used for continuous random variables where probabilities of intervals are given by integrals of f
- - Cumulative distribution function (CDF): F(x) = P(X ≤ x), a function that applies to discrete and continuous variables and describes cumulative probability up to x
- - Support of a random variable: the set of values that have nonzero probability (pmf>0) or nonzero density (pdf>0)
- - Normalization property for distributions: pmf values sum to 1 (Σ p(x) = 1); pdf integrates to 1 (∫ f(x) dx = 1 over the whole domain)
- - Point probabilities differ for discrete vs continuous: discrete values can have P(X = x) > 0; for continuous variables P(X = x) = 0 and probability is only meaningful for intervals
- - Realization vs variable distinction in usage: uppercase symbols denote the random variable as a mapping, lowercase denotes particular observed values

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

When you roll a die, “randomness” lives in the outcome. A random variable is the bridge that turns that outcome into a number you can analyze—so you can compute probabilities, averages, and compare different random phenomena using a shared language.

TL;DR:

A random variable X is a function from outcomes ω in a sample space Ω to real numbers: X: Ω → ℝ. Its distribution can be summarized completely by the cumulative distribution function F\_X(x) = P(X ≤ x). Discrete random variables use a PMF (probability mass function) and sums; continuous random variables use a PDF (density) and integrals, with P(X = x) = 0 for any single point.

## What Is a Random Variable?

### Why we need the concept

In basic probability, you often talk directly about outcomes: heads/tails, die faces 1–6, card suits, etc. But most questions you care about are *numerical*:

- •“How many heads did we get?”
- •“What’s the total on two dice?”
- •“How long until a web request returns?”

Outcomes themselves can be messy objects (a full sequence of flips, a shuffled deck order, a user session log). A random variable lets you *extract a number* from each outcome so that probability tools can focus on the number.

### Definition (the key idea)

A **random variable** is not “a random number floating around.” It is a *rule* (a function).

Let Ω be a sample space, and let ω ∈ Ω be an outcome. A random variable is a function

X: Ω → ℝ

meaning: for every outcome ω, the random variable outputs a real number X(ω).

- •**X** (capital) names the *function / mapping*.
- •A lowercase value like x is a *possible output* of that function.

### Intuition via examples

**Example A: one die roll**

- •Sample space: Ω = {1, 2, 3, 4, 5, 6}
- •Random variable: X(ω) = ω (just “the face value”)

Here X is almost trivial—but it sets the pattern.

**Example B: two coin flips**

- •Sample space: Ω = {HH, HT, TH, TT}
- •Define X(ω) = number of heads in ω

Then:

- •X(HH) = 2
- •X(HT) = 1
- •X(TH) = 1
- •X(TT) = 0

Notice what happened: multiple outcomes map to the same number. That’s normal and important.

### Random variables as a compression of outcomes

Often Ω is huge, but your question depends on a small numeric summary. The random variable is that summary.

For learning probability, keep this mental model:

- •Outcomes ω are what *happened*.
- •X(ω) is the numeric feature you *measure* from what happened.

Once you have X, you can ask probability questions about X without constantly referring to ω.

## From a Random Variable to a Distribution: The CDF F\_X(x)

### Why the CDF matters

If X is a function, you still need to know: “How likely is each possible value?”

There are multiple ways to describe this “likeliness,” but the most universal is the **cumulative distribution function (CDF)**. It works for discrete and continuous cases, and it fully characterizes the distribution.

### Definition of the CDF

For a random variable X, the cumulative distribution function is

F\_X(x) = P(X ≤ x)

Read it as: “the probability that X takes a value at most x.”

### What makes the CDF powerful

1. 1)**It’s one function that encodes all probability information.**

If you know F\_X(x) for all real x, you can recover probabilities of intervals like P(a < X ≤ b).

2. 2)**It works for both discrete and continuous RVs.**

PMFs and PDFs differ, but CDFs behave consistently.

### Using the CDF to compute probabilities

For any real numbers a < b:

P(a < X ≤ b) = F\_X(b) − F\_X(a)

Derivation (showing the idea):

- •Event {X ≤ b} can be split into two disjoint parts:
- •{X ≤ a}
- •{a < X ≤ b}

So

P(X ≤ b) = P(X ≤ a) + P(a < X ≤ b)

Rearrange:

P(a < X ≤ b) = P(X ≤ b) − P(X ≤ a) = F\_X(b) − F\_X(a)

### Basic properties you should internalize

A valid CDF F\_X(x) must satisfy:

- •**Non-decreasing:** if x₁ ≤ x₂ then F\_X(x₁) ≤ F\_X(x₂)
- •**Limits:**
- •lim\_{x→−∞} F\_X(x) = 0
- •lim\_{x→+∞} F\_X(x) = 1
- •**Right-continuous:** the function can “jump” at points (discrete mass), but it is continuous from the right.

### A quick picture in words

- •For a **discrete** RV, the CDF looks like a staircase: flat segments with upward jumps.
- •For a **continuous** RV, the CDF increases smoothly (no jumps).
- •For a **mixed** RV, it can do both (though mixed is beyond today’s focus).

### CDF versus “probability at a point”

Be careful with language:

- •CDF gives probabilities of the form P(X ≤ x).
- •It does *not* directly mean “the probability at x.”

Later you’ll see that in discrete distributions you can use differences of the CDF to get point probabilities, while in continuous distributions differences give interval probabilities (and point probabilities are 0).

## Discrete Random Variables: PMF and Probability Mass

### Why the discrete case is special

A random variable X is **discrete** if it takes values in a countable set, like {0, 1, 2, 3, …} or a finite set like {1, …, 6}.

In a discrete world, probability is stored as **mass** placed on individual points.

### PMF (probability mass function)

For a discrete random variable, the **PMF** is

p\_X(x) = P(X = x)

It assigns a probability to each value x that X can take.

Two must-know conditions:

1) p\_X(x) ≥ 0 for all x

2) ∑ over all possible x of p\_X(x) = 1

### From PMF to CDF

If X is discrete, the CDF is a sum of masses up to x:

F\_X(x) = P(X ≤ x) = ∑\_{t ≤ x} p\_X(t)

This is why the CDF looks like steps: each time you pass a value with mass, the CDF jumps.

### From CDF to PMF

If X is integer-valued (common case), you can recover point probabilities by differences:

p\_X(k) = P(X = k) = F\_X(k) − F\_X(k − 1)

More generally, for any point x:

P(X = x) = F\_X(x) − lim\_{t↑x} F\_X(t)

(That “left limit” is what captures the jump size at x.)

### Example idea: counting heads

Let Ω = {HH, HT, TH, TT} with equal probability 1/4 each.

Define X = number of heads.

Then X takes values {0, 1, 2}.

Compute the PMF:

- •P(X = 0) = P(TT) = 1/4
- •P(X = 1) = P(HT or TH) = 2/4 = 1/2
- •P(X = 2) = P(HH) = 1/4

That’s a full description of the discrete distribution.

### Discrete probability is “sum-based”

Any probability question becomes a sum.

For example:

P(X ≥ 1) = P(X = 1) + P(X = 2)

And using the CDF:

P(X ≥ 1) = 1 − P(X ≤ 0) = 1 − F\_X(0)

You’re already seeing two equivalent perspectives: point masses (PMF) and cumulative probabilities (CDF).

## Continuous Random Variables: PDF, Density, and Integrals

### Why continuous RVs need a different tool

Some quantities aren’t naturally countable:

- •time
- •distance
- •temperature
- •voltage

You might model such a quantity as a **continuous** random variable. Here, probability is not concentrated on points. Instead, it is spread smoothly over intervals.

### The key conceptual shift: probability at a point is zero

For a continuous random variable X:

P(X = x) = 0 for any single real number x

This is not a bug—it’s a consequence of having uncountably many possible values. Probability lives on intervals.

### PDF (probability density function)

A continuous random variable is described by a **probability density function (PDF)** f\_X(x) such that:

P(a ≤ X ≤ b) = ∫ from a to b f\_X(x) dx

And the total probability is 1:

∫\_{−∞}^{∞} f\_X(x) dx = 1

Also f\_X(x) ≥ 0.

Important: f\_X(x) is a **density**, not a probability.

- •f\_X(x) can be greater than 1.
- •Only an integral of f\_X over an interval is a probability.

### CDF in the continuous case

The CDF is still

F\_X(x) = P(X ≤ x)

and it relates to the PDF by an integral:

F\_X(x) = ∫\_{−∞}^{x} f\_X(t) dt

If f\_X is nice enough (continuous), then differentiation recovers the PDF:

f\_X(x) = d/dx F\_X(x)

### Interval probabilities via the CDF

Same rule as always:

P(a < X ≤ b) = F\_X(b) − F\_X(a)

This is one reason the CDF is the “universal” summary: it works without caring whether X is discrete or continuous.

### A concrete continuous example: Uniform(0, 1)

Suppose X is uniformly distributed on [0, 1]. Intuitively: every equal-length interval inside [0, 1] has equal probability.

PDF:

f\_X(x) = 1 for 0 ≤ x ≤ 1, and 0 otherwise.

CDF:

- •If x < 0: F\_X(x) = 0
- •If 0 ≤ x ≤ 1: F\_X(x) = ∫\_{0}^{x} 1 dt = x
- •If x > 1: F\_X(x) = 1

Notice:

- •P(X = 0.3) = 0
- •But P(0.2 ≤ X ≤ 0.5) = ∫\_{0.2}^{0.5} 1 dx = 0.3

### Continuous probability is “integral-based”

In discrete settings you sum masses.

In continuous settings you integrate density.

A useful comparison table:

| Concept | Discrete RV | Continuous RV |
| --- | --- | --- |
| Values X can take | countable | uncountable interval(s) |
| Point probability | P(X = x) can be > 0 | P(X = x) = 0 |
| Main descriptor | PMF p\_X(x) | PDF f\_X(x) |
| Normalization | ∑ p\_X(x) = 1 | ∫ f\_X(x) dx = 1 |
| Interval probability | ∑ over x in interval | ∫ over interval |
| CDF | staircase | smooth (no jumps) |

If you remember only one line: **discrete = mass on points, continuous = density over intervals**.

## Application/Connection: Turning Real Problems into Random Variables

### Why this matters beyond definitions

Random variables are the entry point to almost everything in probability and statistics:

- •expectation (long-run averages)
- •variance (spread)
- •distributions (Bernoulli, binomial, normal, …)
- •modeling noise in machine learning

But the *first* modeling step is always the same:

1) Identify the sample space Ω (what outcomes are possible?)

2) Define a random variable X: Ω → ℝ (what number do you care about?)

3) Describe its distribution (PMF/PDF/CDF)

### Modeling patterns you’ll reuse

Below are common ways to define X.

#### Pattern 1: Indicator random variables

An indicator is a random variable that turns an event into 0/1.

Let A be an event. Define

X(ω) = 1 if ω ∈ A, else 0.

This seems simple, but it becomes a building block for counting.

#### Pattern 2: Counts and totals

You can count something in the outcome:

- •number of heads
- •number of customers arriving
- •number of errors in a day

Or sum values:

- •total of dice
- •total price in a basket

These lead naturally to discrete distributions.

#### Pattern 3: Measurements with units

Time-to-complete, response latency, measurement noise: these are naturally continuous.

### How CDF thinking helps in practice

Even when you don’t know a neat PMF/PDF, you can often reason in terms of CDFs:

- •“What fraction of requests finish within 200 ms?” is P(X ≤ 200) = F\_X(200).
- •Service-level objectives are CDF thresholds.

### Where you’re going next

This node unlocks two big next steps:

1) **Expected Value** [Expected Value](/tech-tree/expected-value/)

Once X is defined, you can compute E[X] as a weighted average (sum/integral). This turns a distribution into a single representative number.

2) **Common Distributions** [Common Distributions](/tech-tree/common-distributions/)

Many random variables you define match standard families (Bernoulli, binomial, uniform, normal). Learning those families gives you ready-made PMFs/PDFs/CDFs.

### Final mental checklist

When someone says “Let X be a random variable…”, train yourself to ask:

- •What is Ω?
- •What is the mapping rule X(ω)?
- •Is X discrete or continuous?
- •What distribution information do I have: PMF, PDF, or at least CDF?

If you can answer those, you’re in control of the randomness.

## Worked Examples (3)

### Discrete RV from coin flips: build PMF and CDF

Flip two fair coins. Let Ω = {HH, HT, TH, TT} with each outcome probability 1/4. Define the random variable X(ω) = number of heads in ω. Find p\_X(x) and F\_X(x).

1. List X(ω) for each outcome:

   - •X(HH) = 2
   - •X(HT) = 1
   - •X(TH) = 1
   - •X(TT) = 0
2. Compute the PMF p\_X(x) = P(X = x):

   - •P(X = 0) = P(TT) = 1/4
   - •P(X = 1) = P(HT or TH) = 2/4 = 1/2
   - •P(X = 2) = P(HH) = 1/4
3. Write the CDF F\_X(x) = P(X ≤ x):

   - •If x < 0: F\_X(x) = 0
   - •If 0 ≤ x < 1: F\_X(x) = P(X = 0) = 1/4
   - •If 1 ≤ x < 2: F\_X(x) = P(X = 0 or 1) = 1/4 + 1/2 = 3/4
   - •If x ≥ 2: F\_X(x) = 1
4. Check via differences (sanity check):

   - •Jump at 0 is 1/4 ⇒ P(X = 0) = 1/4
   - •Jump at 1 is 1/2 ⇒ P(X = 1) = 1/2
   - •Jump at 2 is 1/4 ⇒ P(X = 2) = 1/4

**Insight:** The random variable merges multiple outcomes into the same value (HT and TH both map to 1). The CDF shows this as jumps: each jump size equals the probability mass at that point.

### Continuous RV with Uniform(0, 1): compute probabilities from PDF and CDF

Let X be Uniform(0, 1): f\_X(x) = 1 for 0 ≤ x ≤ 1, otherwise 0. Compute (1) F\_X(x), (2) P(0.2 ≤ X ≤ 0.5), and (3) P(X = 0.3).

1. Compute the CDF F\_X(x) = ∫\_{−∞}^{x} f\_X(t) dt by cases.
2. Case 1: x < 0.

   Then f\_X(t) = 0 for all t ≤ x, so

   F\_X(x) = ∫\_{−∞}^{x} 0 dt = 0.
3. Case 2: 0 ≤ x ≤ 1.

   Then

   F\_X(x) = ∫\_{−∞}^{0} 0 dt + ∫\_{0}^{x} 1 dt

   = 0 + [t]\_{0}^{x}

   = x.
4. Case 3: x > 1.

   Then

   F\_X(x) = ∫\_{−∞}^{0} 0 dt + ∫\_{0}^{1} 1 dt + ∫\_{1}^{x} 0 dt

   = 0 + 1 + 0

   = 1.
5. Compute the interval probability:

   P(0.2 ≤ X ≤ 0.5) = ∫\_{0.2}^{0.5} 1 dx

   = [x]\_{0.2}^{0.5}

   = 0.5 − 0.2

   = 0.3.
6. Compute the point probability:

   P(X = 0.3) = 0 (continuous RVs assign zero probability to any single point).

**Insight:** For continuous RVs, f\_X(x) is not a probability—it’s a density. Probabilities come from areas (integrals), and the CDF is the accumulated area up to x.

### Same outcome space, different random variables: total vs maximum on two dice

Roll two fair six-sided dice. The sample space is pairs (d₁, d₂) with 36 equally likely outcomes. Define two random variables:

S(d₁, d₂) = d₁ + d₂ (sum), and M(d₁, d₂) = max(d₁, d₂) (maximum). Compute P(S = 7) and P(M ≤ 3).

1. Compute P(S = 7): count outcomes (d₁, d₂) such that d₁ + d₂ = 7.

   The pairs are:

   (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)

   There are 6 favorable outcomes out of 36 total.

   So P(S = 7) = 6/36 = 1/6.
2. Compute P(M ≤ 3): this means both dice are ≤ 3, because max(d₁, d₂) ≤ 3 ⇔ d₁ ≤ 3 and d₂ ≤ 3.

   Number of outcomes with d₁ ∈ {1,2,3} and d₂ ∈ {1,2,3} is 3 · 3 = 9.

   So P(M ≤ 3) = 9/36 = 1/4.

**Insight:** The randomness is the same (two dice), but the *question* changes the mapping X(ω). Different random variables on the same Ω lead to different distributions and probabilities.

## Key Takeaways

- ✓

  A random variable X is a function X: Ω → ℝ mapping each outcome ω to a real number X(ω).
- ✓

  Capital letters (X) denote the random variable (the mapping); lowercase (x) denotes a realized/possible value.
- ✓

  The CDF F\_X(x) = P(X ≤ x) fully characterizes the distribution and works for both discrete and continuous RVs.
- ✓

  Discrete random variables have a PMF p\_X(x) = P(X = x) and probabilities are computed with sums.
- ✓

  Continuous random variables have a PDF f\_X(x) and probabilities are computed with integrals: P(a ≤ X ≤ b) = ∫\_a^b f\_X(x) dx.
- ✓

  For continuous RVs, P(X = x) = 0 for any single point; only intervals can have positive probability.
- ✓

  You can compute interval probabilities using the CDF: P(a < X ≤ b) = F\_X(b) − F\_X(a).

## Common Mistakes

- ✗

  Thinking a random variable is a single random outcome, rather than a function that assigns a number to each outcome.
- ✗

  Confusing PDF values with probabilities (e.g., treating f\_X(0.3) as P(X = 0.3)).
- ✗

  Forgetting that continuous point probabilities are zero and trying to compute P(X = x) via the PDF directly.
- ✗

  Mixing up the roles of X and x: writing P(x ≤ 3) instead of P(X ≤ 3).

## Practice

easy

A fair die is rolled. Define X as the indicator that the outcome is even: X = 1 if the roll is even, else 0. Find (1) P(X = 1), (2) F\_X(x) for all x.

**Hint:** Even outcomes are {2,4,6}. For the CDF, consider ranges: x < 0, 0 ≤ x < 1, x ≥ 1.

Show solution

We have P(X = 1) = P(even) = 3/6 = 1/2.

CDF:

- •If x < 0: F\_X(x) = P(X ≤ x) = 0.
- •If 0 ≤ x < 1: F\_X(x) = P(X ≤ x) = P(X = 0) = 1/2.
- •If x ≥ 1: F\_X(x) = 1.

medium

Let X be a discrete RV with PMF: p\_X(0)=0.2, p\_X(1)=0.5, p\_X(3)=0.3. Compute (1) F\_X(1), (2) P(0 < X ≤ 3), (3) P(X = 2).

**Hint:** F\_X(1) = P(X ≤ 1). For P(0 < X ≤ 3), use either summation over allowed values or F\_X(3) − F\_X(0).

Show solution

(1) F\_X(1) = P(X ≤ 1) = p\_X(0)+p\_X(1) = 0.2+0.5 = 0.7.

(2) P(0 < X ≤ 3) includes X=1 or X=3 (since 2 is not possible here): 0.5+0.3 = 0.8.

Equivalently: F\_X(3) − F\_X(0) = 1 − 0.2 = 0.8.

(3) P(X = 2) = 0 because 2 is not in the support (not assigned any mass).

hard

Let X be continuous with PDF f\_X(x) = 2x for 0 ≤ x ≤ 1 (and 0 otherwise). Compute (1) F\_X(x) for 0 ≤ x ≤ 1, and (2) P(0.5 ≤ X ≤ 1).

**Hint:** Integrate: F\_X(x) = ∫\_0^x 2t dt. Then use either an integral over [0.5,1] or CDF differences.

Show solution

(1) For 0 ≤ x ≤ 1:

F\_X(x) = ∫\_{−∞}^{x} f\_X(t) dt = ∫\_{0}^{x} 2t dt = [t²]\_{0}^{x} = x².

(2) P(0.5 ≤ X ≤ 1) = F\_X(1) − F\_X(0.5) = 1² − (0.5)² = 1 − 0.25 = 0.75.

## Connections

Next nodes:

- •[Expected Value](/tech-tree/expected-value/)
- •[Common Distributions](/tech-tree/common-distributions/)

Related refreshers:

- •[Basic Probability](/tech-tree/basic-probability/)
- •[Functions](/tech-tree/functions/)

Later connections:

- •[Variance](/tech-tree/variance/)
- •[Law of Large Numbers](/tech-tree/law-of-large-numbers/)
- •[Joint Random Variables](/tech-tree/joint-random-variables/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
