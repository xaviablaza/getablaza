---
title: Bayes Theorem
description: P(A|B) = P(B|A)P(A)/P(B). Updating beliefs with evidence.
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
permalink: /tech-tree/bayes-theorem/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Bayes Theorem

Probability & StatisticsDifficulty: ★★☆☆☆Depth: 3Unlocks: 19

P(A|B) = P(B|A)P(A)/P(B). Updating beliefs with evidence.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Prior: probability of a hypothesis before seeing the new evidence
- -Likelihood: probability of the observed evidence assuming the hypothesis is true
- -Evidence (marginal probability): total probability of the observed evidence (normalizing constant)
- -Posterior: updated probability of the hypothesis after incorporating the evidence

## Essential Relationships

- -Bayes rule: Posterior = (Likelihood \* Prior) / Evidence ; symbolically: P(A|B) = P(B|A) \* P(A) / P(B)

## Prerequisites (1)

[Conditional Probability6 atoms](/tech-tree/conditional-probability/)

## Unlocks (1)

[Bayesian Inferencelvl 4](/tech-tree/bayesian-inference/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[Full-Cycle RecruitingBusiness

Each recruiting stage (screen, phone, onsite, reference) is a Bayesian update on candidate-role fit. Strong recruiters implicitly run P(good hire | signal) calculations, updating priors from resume through final round. This framing explains why structured interviews (better likelihoods) outperform unstructured ones.](/business/full-cycle-recruiting/)

### From Money (1)

[Pre-Tax vs Post-TaxMoney

Update tax rate expectations as career evidence accumulates](/money/pre-tax-vs-post-tax/)

Advanced Learning Details

### Graph Position

23

Depth Cost

19

Fan-Out (ROI)

10

Bottleneck Score

3

Chain Length

### Cognitive Load

5

Atomic Elements

19

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (9)

- - Bayes' theorem as a rule for computing posterior probabilities from likelihoods and priors
- - Prior probability (P(A)): degree of belief in hypothesis A before seeing evidence
- - Likelihood (P(B|A)): probability of observing evidence B assuming hypothesis A is true
- - Evidence / marginal likelihood (P(B)): overall probability of the observed evidence under all hypotheses; serves as a normalizing constant
- - Posterior probability (interpretive): treating P(A|B) as the updated belief about A after observing B
- - Role distinction: interpreting one event/variable as hypothesis (unknown) and the other as observed data/evidence
- - Normalization: the denominator ensures the posterior is a valid probability (sums/integrates to 1 across hypotheses)
- - Marginalization / total probability for computing P(B): combining likelihoods and priors over a partition of hypotheses
- - Sequential (iterative) Bayesian updating: using the posterior from one update as the prior for the next

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

If you know how to compute P(A|B), Bayes’ Theorem teaches you how to “turn it around” into P(B|A)—and, more importantly, how to update beliefs about a hypothesis when new evidence arrives.

TL;DR:

Bayes’ Theorem is

P(A|B) = P(B|A)P(A)/P(B).

Interpretation:

- •P(A) is the prior belief about A.
- •P(B|A) is the likelihood of seeing evidence B if A were true.
- •P(B) is the evidence (normalizer): how likely B is overall.
- •P(A|B) is the posterior belief after seeing B.

It is a rule for rational belief-updating under uncertainty.

## What Is Bayes’ Theorem?

### Why this concept exists (motivation)

In real problems you often face the direction mismatch:

- •You *can* estimate how likely some evidence is **given** a hypothesis (e.g., “if a patient has the disease, how likely is a positive test?”).
- •But you *want* the reverse: how likely the hypothesis is **given** evidence (e.g., “given a positive test, how likely is disease?”).

Bayes’ Theorem bridges this gap. It’s also the mathematical backbone of “updating beliefs with evidence”: start with an initial belief (a *prior*), observe data (the *evidence*), and compute an updated belief (the *posterior*).

### The statement

For events A and B, with P(B) > 0:

P(A|B) = P(B|A)P(A) / P(B)

You’ll see several names for each term:

- •**Prior**: P(A)
- •**Likelihood**: P(B|A)
- •**Posterior**: P(A|B)
- •**Evidence / marginal likelihood / normalizer**: P(B)

Even if the formula feels simple, the meaning is subtle: *probability is redistributed* across hypotheses when evidence arrives.

### Where it comes from (definition-level derivation)

Bayes’ Theorem is not a “special trick”—it is a direct consequence of the definition of conditional probability.

Start with the definition:

P(A|B) = P(A ∩ B) / P(B)

Also:

P(B|A) = P(A ∩ B) / P(A)

Solve the second equation for P(A ∩ B):

P(A ∩ B) = P(B|A)P(A)

Plug into the first equation:

P(A|B)

= P(A ∩ B) / P(B)

= [P(B|A)P(A)] / P(B)

That’s Bayes’ Theorem.

### Intuition in one sentence

Posterior = (how well A predicts the evidence) × (how plausible A was) ÷ (how surprising the evidence is overall).

### A note about language: hypothesis vs evidence

Often we treat:

- •A = “hypothesis is true”
- •B = “we observed some evidence”

But the theorem is symmetric: you can swap roles depending on what you’re trying to compute.

### When it’s most useful

Bayes is most useful when:

1) You can model P(B|A) (data given hypothesis) more easily than P(A|B).

2) You have multiple competing hypotheses (A₁, A₂, …) and want to update which is most plausible.

3) Base rates matter (priors), and ignoring them would lead to bad conclusions.

## Core Mechanic 1: Priors, Likelihoods, and Posteriors (Belief Updating)

### Why separate probability into these pieces?

When you write P(A|B) directly, it can hide structure. Bayes explicitly factors the update into:

- •What you believed before (prior)
- •How compatible the evidence is with the hypothesis (likelihood)
- •A normalization step so everything sums to 1 (evidence)

This decomposition is powerful because each piece comes from a different source:

- •Priors can come from historical rates, domain knowledge, or earlier data.
- •Likelihood comes from a measurement model (sensor accuracy, test sensitivity/specificity).
- •Evidence comes from total probability over all ways B could happen.

### The “belief update” view

Suppose A is a hypothesis and B is a newly observed fact.

Bayes:

P(A|B) ∝ P(B|A)P(A)

Read “∝” as “proportional to.” This is the key intuition:

- •Start with P(A) (prior mass).
- •Multiply by P(B|A) (compatibility with evidence).
- •Then renormalize so probabilities sum to 1.

This proportionality form is often how you reason informally:

1) Hypotheses that better predict the evidence get boosted.

2) Hypotheses that poorly predict the evidence get penalized.

3) Priors still matter—rare things stay rare unless the evidence is very strong.

### Discrete hypotheses: odds-style thinking

Imagine two hypotheses A and ¬A (not A). Using Bayes on both:

P(A|B) = P(B|A)P(A)/P(B)

P(¬A|B) = P(B|¬A)P(¬A)/P(B)

Take the ratio (posterior odds):

P(A|B) / P(¬A|B)

= [P(B|A)P(A)] / [P(B|¬A)P(¬A)]

This shows:

Posterior odds = Likelihood ratio × Prior odds

Where likelihood ratio = P(B|A) / P(B|¬A).

This is useful because the annoying P(B) cancels, and you can see the “strength of evidence” as a ratio.

### What each term means (carefully)

Let’s tie each term to an interpretation you can check:

- •**Prior P(A)**: Before seeing B, how probable is A?
- •**Likelihood P(B|A)**: If A were true, how often would we see B?
- •**Posterior P(A|B)**: After seeing B, how probable is A?
- •**Evidence P(B)**: In the whole world (across all hypotheses), how often would we see B?

A common conceptual trap is to confuse P(B|A) with P(A|B). They can be wildly different.

### A miniature numeric example (no full story yet)

Suppose:

- •P(A) = 0.01 (A is rare)
- •P(B|A) = 0.90 (evidence is common if A is true)
- •P(B|¬A) = 0.05 (false alarm rate)

We’ll compute P(A|B), but first note: we need P(B). That’s not optional.

Using total probability:

P(B) = P(B|A)P(A) + P(B|¬A)P(¬A)

Compute:

P(B)

= 0.90·0.01 + 0.05·0.99

= 0.009 + 0.0495

= 0.0585

Now Bayes:

P(A|B)

= (0.90·0.01) / 0.0585

= 0.009 / 0.0585

≈ 0.1538

Even with strong evidence, a rare prior can keep the posterior moderate.

### Summary table: “parts of Bayes”

| Name | Symbol | Meaning | Typical source |
| --- | --- | --- | --- |
| Prior | P(A) | Belief before seeing B | Base rate, historical data |
| Likelihood | P(B | A) | Evidence frequency if A true | Measurement/test model |
| Evidence | P(B) | Overall chance of evidence | Computed via total probability |
| Posterior | P(A | B) | Updated belief after B | Result of Bayes |

## Core Mechanic 2: Computing the Evidence with the Law of Total Probability

### Why P(B) is the “normalizing constant”

Bayes’ Theorem divides by P(B). This ensures that the posterior is a valid probability.

If you compute unnormalized weights:

w(A) = P(B|A)P(A)

then the normalized posterior is:

P(A|B) = w(A) / ∑ₖ w(Aₖ)

Where {Aₖ} are mutually exclusive, exhaustive hypotheses.

So P(B) is exactly:

P(B) = ∑ₖ P(B|Aₖ)P(Aₖ)

That is the Law of Total Probability.

### Two-hypothesis case: A vs ¬A

If hypotheses are A and ¬A:

P(B)

= P(B|A)P(A) + P(B|¬A)P(¬A)

This formula is the workhorse behind medical-test and spam-filter calculations.

### Multi-class case: A₁, A₂, …, Aₙ

If you have n hypotheses:

- •Aᵢ ∩ Aⱼ = ∅ for i ≠ j
- •∪ᵢ Aᵢ is the whole sample space

Then:

P(B) = ∑ᵢ P(B|Aᵢ)P(Aᵢ)

And Bayes becomes:

P(Aᵢ|B) = P(B|Aᵢ)P(Aᵢ) / ∑ⱼ P(B|Aⱼ)P(Aⱼ)

### Why this matters conceptually

The evidence term answers: “How often would we see B *regardless of which hypothesis is true*?”

- •If B is very common overall, then seeing it doesn’t tell you much (posterior stays close to prior).
- •If B is rare overall, then seeing it is informative, and posteriors can shift dramatically.

This matches everyday reasoning: a surprising clue carries more information than a mundane one.

### A common technique: compute numerator and denominator separately

When doing Bayes problems by hand:

1) Compute the numerator: P(B|A)P(A).

2) Compute P(B) using total probability.

3) Divide.

This prevents mistakes like forgetting the ¬A term or miscomputing complements.

### Visualization intuition: probability mass reallocation

Think of the prior probabilities across hypotheses as “mass” that sums to 1.

- •Multiplying by P(B|Aᵢ) shrinks/expands each mass depending on how consistent that hypothesis is with the evidence.
- •Dividing by P(B) rescales so the total mass returns to 1.

This is the essence of Bayesian updating.

### Small checklist for correctness

Before finalizing a Bayes calculation:

- •Are your hypotheses mutually exclusive and exhaustive?
- •Did you compute P(B) as a weighted sum over hypotheses?
- •Does your posterior stay in [0, 1]?
- •If evidence is uninformative (P(B|A) ≈ P(B|¬A)), does posterior stay near prior?

## Application/Connection: Interpreting Tests, Filters, and Simple Classification

### Why Bayes shows up everywhere

Bayes’ Theorem is the simplest formal model of learning from data:

- •You have uncertainty about a hidden state (disease / spam / which class).
- •You observe a noisy signal (test result / words / sensor output).
- •You infer the hidden state.

Even many modern ML systems can be described as “compute something proportional to likelihood × prior, then normalize.”

### Medical testing (base rate matters)

Medical test problems are the classic Bayes showcase because humans often ignore priors.

Key terms you’ll see:

- •Sensitivity = P(positive | disease)
- •Specificity = P(negative | no disease)
- •False positive rate = P(positive | no disease) = 1 − specificity

What you usually want is:

P(disease | positive)

That is Bayes with A = disease, B = positive.

The important lesson: even a highly accurate test can yield many false positives when the disease is rare.

### Spam filtering / text classification (discrete version)

Suppose:

- •A = “email is spam”
- •B = “email contains the word ‘free’”

Then Bayes says:

P(spam | contains ‘free’)

= P(contains ‘free’ | spam)P(spam) / P(contains ‘free’)

This is the skeleton of naïve Bayes classifiers (where B is many word-features). You will later learn more advanced versions, but the core update logic is identical.

### Sensor fusion / robotics (belief update repeated over time)

In tracking problems:

- •Prior represents your belief about a robot’s position before the latest sensor reading.
- •Likelihood represents sensor noise (how likely a reading is for each position).
- •Posterior is your updated belief.

Repeated Bayes updates over time lead to filters like the Kalman filter and particle filter (conceptually Bayesian, though implementation details differ).

### Bayes as the gateway to Bayesian inference

Bayes’ Theorem for events is the entry point to Bayes for distributions.

Event version:

P(A|B) = P(B|A)P(A)/P(B)

Distribution version (preview):

p(θ|D) ∝ p(D|θ)p(θ)

Where:

- •θ is a parameter (a continuous hypothesis)
- •D is data
- •p(·) are probability densities

This node unlocks that next step.

### Quick comparison: Frequentist vs Bayesian (high-level)

| Aspect | Frequentist (very rough) | Bayesian (very rough) |
| --- | --- | --- |
| Probability means | Long-run frequency | Degree of belief (coherent with axioms) |
| Parameters | Fixed unknown constants | Random variables with priors |
| Output | Point estimates, confidence intervals | Posterior distributions, credible intervals |

You don’t need to “choose a side” to use Bayes’ Theorem; you just need to be clear about what probabilities represent in your problem.

## Worked Examples (3)

### Medical test: compute P(disease | positive)

A disease affects 1% of the population. A test has sensitivity 99% and specificity 95%.

Let:

- •A = disease
- •B = positive test

Given:

P(A) = 0.01

P(B|A) = 0.99

Specificity = P(negative|¬A) = 0.95 ⇒ P(positive|¬A) = P(B|¬A) = 0.05

Goal: compute P(A|B).

1. Compute the complement prior:

   P(¬A) = 1 − P(A)

   = 1 − 0.01

   = 0.99
2. Compute evidence via total probability:

   P(B) = P(B|A)P(A) + P(B|¬A)P(¬A)

   = 0.99·0.01 + 0.05·0.99

   = 0.0099 + 0.0495

   = 0.0594
3. Apply Bayes’ Theorem:

   P(A|B) = P(B|A)P(A) / P(B)

   = (0.99·0.01) / 0.0594

   = 0.0099 / 0.0594

   ≈ 0.1667
4. Interpretation:

   Even with a good test, the posterior is ≈ 16.7%, not ≈ 99%, because false positives among the many healthy people are substantial when the disease is rare.

**Insight:** The base rate (prior) can dominate. A positive result is evidence, but it’s not the same as near-certainty unless the test is extremely specific or the disease is common.

### Factory defects: infer which machine produced an item

A factory has two machines making the same part.

- •Machine 1 makes 70% of parts and has a 2% defect rate.
- •Machine 2 makes 30% of parts and has a 5% defect rate.

Let:

A₁ = “part came from Machine 1”

A₂ = “part came from Machine 2”

B = “part is defective”

Given:

P(A₁)=0.70, P(A₂)=0.30

P(B|A₁)=0.02, P(B|A₂)=0.05

Goal: compute P(A₂|B) (probability it came from Machine 2 given defect).

1. Compute evidence (defect probability overall):

   P(B) = P(B|A₁)P(A₁) + P(B|A₂)P(A₂)

   = 0.02·0.70 + 0.05·0.30

   = 0.014 + 0.015

   = 0.029
2. Apply Bayes for Machine 2:

   P(A₂|B) = P(B|A₂)P(A₂) / P(B)

   = (0.05·0.30) / 0.029

   = 0.015 / 0.029

   ≈ 0.5172
3. Optional: compute P(A₁|B) as a sanity check:

   P(A₁|B) = (0.02·0.70)/0.029

   = 0.014/0.029

   ≈ 0.4828

   And indeed 0.5172 + 0.4828 = 1.

**Insight:** Even though Machine 2 produces fewer parts (lower prior), a defect strongly shifts probability toward it because its likelihood of defect is higher.

### Evidence as a normalizer: compute posteriors from unnormalized weights

You have three hypotheses about a coin:

A₁: fair (P(heads)=0.5)

A₂: biased toward heads (P(heads)=0.8)

A₃: biased toward tails (P(heads)=0.2)

Your prior beliefs are:

P(A₁)=0.6, P(A₂)=0.2, P(A₃)=0.2

You flip once and observe B = “heads”.

Goal: compute P(Aᵢ|heads) for i=1..3 using weights and normalization.

1. Compute unnormalized weights w(Aᵢ)=P(B|Aᵢ)P(Aᵢ):

   w(A₁) = 0.5·0.6 = 0.30

   w(A₂) = 0.8·0.2 = 0.16

   w(A₃) = 0.2·0.2 = 0.04
2. Compute evidence as the sum of weights:

   P(B) = ∑ᵢ w(Aᵢ)

   = 0.30 + 0.16 + 0.04

   = 0.50
3. Normalize to get posteriors:

   P(A₁|heads)=0.30/0.50=0.60

   P(A₂|heads)=0.16/0.50=0.32

   P(A₃|heads)=0.04/0.50=0.08
4. Interpretation:

   One heads result increases belief in the heads-biased coin and decreases belief in the tails-biased coin, while the fair coin remains most probable due to its strong prior.

**Insight:** Computing Bayes via “weights then normalize” generalizes cleanly to many hypotheses and avoids repeatedly recomputing P(B) from scratch.

## Key Takeaways

- ✓

  Bayes’ Theorem is derived directly from conditional probability: P(A|B) = P(B|A)P(A)/P(B).
- ✓

  Interpret Bayes as belief updating: posterior ∝ likelihood × prior.
- ✓

  P(B) (evidence) is computed using the Law of Total Probability and acts as a normalizing constant.
- ✓

  P(B|A) and P(A|B) are not interchangeable; confusing them is a major source of errors.
- ✓

  Rare hypotheses (small priors) require strong evidence (large likelihood ratio) to become likely.
- ✓

  For multiple hypotheses A₁…Aₙ: P(Aᵢ|B)=P(B|Aᵢ)P(Aᵢ)/∑ⱼ P(B|Aⱼ)P(Aⱼ).
- ✓

  Posterior odds = likelihood ratio × prior odds is often the cleanest way to interpret “strength of evidence.”

## Common Mistakes

- ✗

  Mixing up directions: treating P(B|A) as if it were P(A|B).
- ✗

  Forgetting to compute P(B) using all relevant hypotheses (e.g., omitting the ¬A term).
- ✗

  Using an incorrect complement: writing P(¬A)=1−P(B) or similar mismatches of events.
- ✗

  Interpreting likelihood as “probability the hypothesis is true”; likelihood is about evidence given the hypothesis.

## Practice

easy

A spam filter flags an email if it contains the word “winner”. Suppose:

P(spam)=0.2,

P(“winner”|spam)=0.6,

P(“winner”|not spam)=0.05.

Compute P(spam|“winner”).

**Hint:** Compute P(“winner”) = P(“winner”|spam)P(spam) + P(“winner”|¬spam)P(¬spam), then apply Bayes.

Show solution

Let A=spam, B=contains “winner”.

P(A)=0.2, P(¬A)=0.8.

P(B)=0.6·0.2 + 0.05·0.8

=0.12 + 0.04

=0.16.

P(A|B)=P(B|A)P(A)/P(B)

=(0.6·0.2)/0.16

=0.12/0.16

=0.75.

medium

Two coins are in a box. Coin 1 is fair. Coin 2 lands heads with probability 0.9. You pick a coin uniformly at random and flip it once; it shows heads. What is P(you picked Coin 2 | heads)?

**Hint:** Use hypotheses A₁ (fair) and A₂ (biased). Priors are 0.5 and 0.5. Evidence is heads.

Show solution

Let A₂=Coin 2 chosen, B=heads.

P(A₂)=0.5, P(A₁)=0.5.

P(B|A₂)=0.9, P(B|A₁)=0.5.

P(B)=0.9·0.5 + 0.5·0.5

=0.45 + 0.25

=0.70.

P(A₂|B)=0.9·0.5 / 0.70

=0.45/0.70

≈ 0.6429.

hard

A test for a condition has sensitivity 0.97 and specificity 0.98. The condition prevalence is 0.4%. If a person tests positive, compute P(condition | positive). Then explain in one or two sentences why the result is not close to 97%.

**Hint:** Convert specificity to false positive rate: P(positive|¬condition)=1−0.98. Use P(condition)=0.004.

Show solution

Let A=condition, B=positive.

P(A)=0.004, P(¬A)=0.996.

P(B|A)=0.97.

Specificity=0.98 ⇒ P(B|¬A)=0.02.

P(B)=0.97·0.004 + 0.02·0.996

=0.00388 + 0.01992

=0.02380.

P(A|B)=0.97·0.004 / 0.02380

=0.00388/0.02380

≈ 0.1630 (≈ 16.3%).

Explanation: although the test is sensitive, the condition is rare, so false positives among the many healthy people contribute heavily to positive results.

## Connections

Next you’ll generalize this event-based rule to distributions and parameters in [Bayesian Inference](/tech-tree/bayesian-inference/).

Related foundations:

- •Conditional Probability (prerequisite)

Related applications (later nodes often build on Bayes):

- •Naïve Bayes classification
- •Bayesian networks
- •Kalman filtering / probabilistic state estimation

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
