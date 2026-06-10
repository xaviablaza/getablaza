---
title: Measure Theory
description: Rigorous foundation for probability. Sigma-algebras, Lebesgue integration.
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
permalink: /tech-tree/measure-theory/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Measure Theory

Probability & StatisticsDifficulty: ★★★★★Depth: 4Unlocks: 0

Rigorous foundation for probability. Sigma-algebras, Lebesgue integration.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Sigma-algebra (collection of sets closed under complementation and countable unions)
- -Measure (nonnegative, countably additive set function on a sigma-algebra)
- -Lebesgue integral (integration of measurable functions defined with respect to a measure)

## Key Symbols & Notation

mu (measure symbol, written 'mu' in ASCII)

## Essential Relationships

- -Measurability: a function is measurable iff the preimage of every set in the sigma-algebra is in the sigma-algebra on the domain
- -Integration construction: the Lebesgue integral is built from the measure by integrating indicators, extending to nonnegative simple functions, then to nonnegative measurable functions and finally to general measurable functions

## Prerequisites (2)

[Integrals6 atoms](/tech-tree/integrals-basic/)[Sets6 atoms](/tech-tree/sets-basic/)

Advanced Learning Details

### Graph Position

46

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

4

Chain Length

### Cognitive Load

6

Atomic Elements

75

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (32)

- - σ-algebra: a collection of subsets closed under countable union, countable intersection, and complement
- - measurable space: a set equipped with a σ-algebra
- - measure: a nonnegative set function on a σ-algebra satisfying μ(∅)=0 and countable additivity
- - probability measure: a measure with total mass μ(X)=1
- - countable additivity (σ-additivity) vs finite additivity
- - σ-finiteness: decomposition of the space into a countable union of sets with finite measure
- - null (measure zero) sets
- - almost everywhere (a.e.) statements: property holds except on a null set
- - outer measure: an extended set function on all subsets used to construct measures
- - Carathéodory measurability criterion for constructing measures from outer measures
- - Lebesgue measure: the measure of length/area/volume compatible with translation invariance (constructed via outer measure)
- - non-measurable sets (existence, e.g. Vitali sets) showing not all subsets are measurable
- - measurable function: function whose preimages of measurable sets are measurable
- - indicator (characteristic) functions 1\_A or χ\_A
- - simple functions: finite linear combinations of indicator functions used to approximate measurable functions
- - Lebesgue integral for nonnegative measurable functions defined as supremum of integrals of simple functions
- - decomposition of general measurable functions into positive and negative parts and definition of the Lebesgue integral via these parts
- - comparison with Riemann integral: Lebesgue integral extends and generalizes Riemann integral
- - modes of convergence for functions: almost everywhere convergence, convergence in measure, convergence in L^p (norm) and in probability
- - Monotone Convergence Theorem (MCT)
- - Fatou's Lemma
- - Dominated Convergence Theorem (DCT)
- - signed measures and decomposition into positive and negative parts (Hahn decomposition / Jordan decomposition)
- - absolute continuity of measures and Radon–Nikodym derivative (dν/dμ) when ν << μ
- - product σ-algebra and product measure
- - Fubini's and Tonelli's theorems relating integrals over product spaces and iterated integrals
- - pushforward measure (law/distribution) of a measurable function (random variable)
- - expectation as Lebesgue integral of a random variable
- - independence defined via σ-algebras or product measures
- - L^p spaces: equivalence classes of measurable functions with finite p-th power integral
- - norm in L^p: ||f||\_p = (∫ |f|^p dμ)^{1/p}
- - convergence in L^p and its differences from pointwise/a.e. convergence

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Probability looks like “assign a number to an event,” but to do that rigorously you must answer: which subsets count as events, and how do we assign probabilities consistently when there are infinitely many ways to combine events? Measure theory is the framework that makes those questions precise—and it also replaces “area under a curve” with a more flexible notion of integration that works for discontinuous functions, limits of random variables, and continuous distributions.

TL;DR:

Measure theory builds probability from three pieces: (1) a σ-algebra of measurable sets (the events you’re allowed to talk about), (2) a measure μ that assigns sizes to those sets and is countably additive, and (3) the Lebesgue integral ∫ f dμ, defined by approximating a function using simple functions and taking limits. This foundation explains why expectations behave well under limits (monotone/dominated convergence), and why densities are “Radon–Nikodym derivatives.”

## What Is Measure Theory?

### Why you need more than “area” and “length”

In calculus you learned integrals as areas under curves, often via Riemann sums. That’s powerful, but it has friction points:

- •Many important functions aren’t nicely approximated by rectangles on the x-axis (think: wildly discontinuous functions, indicator functions of complicated sets).
- •In probability, you constantly take limits: limits of events, limits of random variables, limits of expectations. You want rules that let you move limits through probabilities and expectations safely.
- •Continuous probability uses “densities” informally: P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx. But what exactly is f, and why does it exist sometimes and not others?

Measure theory addresses these by **separating** two roles that are blended in Riemann integration:

1) **Which subsets are “measurable”?** (Which events can we assign sizes/probabilities to?)

2) **How do we assign a size μ to those subsets?**

Then integration becomes: **sum the values of a function weighted by μ**, generalized via limits.

### The central objects: (Ω, 𝔽, μ)

A measure-theoretic universe is a triple:

- •**Ω**: a set of outcomes (a “sample space” in probability)
- •**𝔽**: a σ-algebra on Ω (the collection of measurable sets / events)
- •**μ**: a measure μ: 𝔽 → [0, ∞]

In probability, μ is usually written P and has P(Ω) = 1. In analysis, μ could be **Lebesgue measure** on ℝ (length), or counting measure, or many others.

### What measure theory gives you conceptually

Measure theory is not just a bag of definitions. It gives a consistent logic for:

- •**Events built by countable operations** (unions/intersections across infinitely many sets)
- •**Sizes that behave well under limits** (continuity of measure)
- •**Integrals that behave well under limits** (monotone and dominated convergence)

These “countable” properties are exactly what probability needs, because sequences of random variables and sequences of events are the bread and butter of convergence and laws of large numbers.

### A quick roadmap

We’ll build up in layers:

1. 1)**σ-algebras**: what counts as a measurable set
2. 2)**Measures**: how to assign sizes to those sets
3. 3)**Measurable functions**: random variables as measurable maps
4. 4)**Lebesgue integral**: define ∫ f dμ via simple functions and limits
5. 5)**Convergence theorems**: why expectations commute with limits under conditions
6. 6)**Probability connections**: densities, Radon–Nikodym, and expectation as an integral

We’ll keep connecting back to probability intuition: “events,” “probabilities,” “expectations.”

## Core Mechanic 1: σ-algebras (What counts as an event?)

### Why σ-algebras exist

Suppose Ω is uncountably infinite (e.g., Ω = ℝ). You might hope to assign a probability to **every** subset of Ω.

But there is a deep obstruction: there exist subsets of ℝ (e.g., Vitali sets) for which no translation-invariant “length” can be consistently defined while preserving natural properties like countable additivity. So we compromise: we choose a rich, well-behaved family of subsets—enough to include all sets we care about in applications—on which a measure can live.

That family is a **σ-algebra**.

### Definition

A collection 𝔽 ⊂ 𝒫(Ω) (a set of subsets of Ω) is a **σ-algebra** if:

1) Ω ∈ 𝔽

2) If A ∈ 𝔽 then Aᶜ ∈ 𝔽

3) If A₁, A₂, … ∈ 𝔽 then ⋃ₙ Aₙ ∈ 𝔽 (closure under countable unions)

From these, you automatically also get closure under:

- •Countable intersections: ⋂ₙ Aₙ ∈ 𝔽 (because ⋂ₙ Aₙ = (⋃ₙ Aₙᶜ)ᶜ)
- •Set difference: A \ B = A ∩ Bᶜ
- •Empty set: ∅ ∈ 𝔽 (since ∅ = Ωᶜ)

### Why “countable” matters

Finite unions are not enough. Many limit operations produce **countable** unions/intersections:

- •lim sup of events: lim sup Aₙ = ⋂ₖ ⋃ₙ≥ₖ Aₙ
- •lim inf of events: lim inf Aₙ = ⋃ₖ ⋂ₙ≥ₖ Aₙ

If your “events” weren’t closed under these, you couldn’t even state many convergence results.

### Examples of σ-algebras

#### 1) Trivial σ-algebra

𝔽 = {∅, Ω}. Too small for most purposes.

#### 2) Power set

𝔽 = 𝒫(Ω). Always a σ-algebra. For uncountable Ω, many interesting measures cannot be defined on all subsets while keeping desired properties.

#### 3) Borel σ-algebra on ℝ

The **Borel σ-algebra** 𝔹(ℝ) is generated by open sets (equivalently intervals). Intuitively, it contains sets you can build from intervals using countable unions/intersections/complements.

Notation: 𝔹(ℝ) = σ(open sets).

This is the standard measurable structure for real-valued random variables.

### Generated σ-algebras (σ(𝒢))

Often you don’t want to specify 𝔽 directly. Instead, you start with “basic” sets 𝒢 (like intervals) and take the smallest σ-algebra containing them.

Formally:

- •σ(𝒢) = ⋂{ 𝔽 : 𝔽 is a σ-algebra and 𝒢 ⊂ 𝔽 }

This intersection is again a σ-algebra (intersection of σ-algebras preserves closure properties).

Why this matters in probability:

- •The σ-algebra generated by a random variable X is σ(X) = {X⁻¹(B) : B ∈ 𝔹(ℝ)}. It represents all events “observable” from X.

### A useful comparison table

| Object | What it is | Closed under | Why it’s used |
| --- | --- | --- | --- |
| Algebra (field) of sets | collection of subsets | complements + **finite** unions | too weak for limit operations |
| σ-algebra | collection of subsets | complements + **countable** unions | supports measure + convergence |
| Topology | collection of “open” sets | arbitrary unions + finite intersections | continuity, not size |
| Borel σ-algebra 𝔹(ℝ) | σ-algebra generated by open sets | countable unions/intersections/complements | standard measurable sets on ℝ |

### Breathing room: what σ-algebras do *not* do

A σ-algebra is not a measure. It does not assign sizes. It only defines which questions (events) are legal.

Think of 𝔽 as the “language” of measurable events; μ will be the “semantics” that assigns numbers.

## Core Mechanic 2: Measures (Assigning size μ to measurable sets)

### Why measures are defined on σ-algebras

Once you commit to a σ-algebra 𝔽, you want μ(A) to behave like “size.” The critical property is that disjoint pieces add up—even if you have countably many of them.

### Definition

A **measure** is a function μ: 𝔽 → [0, ∞] such that:

1) μ(∅) = 0

2) (Countable additivity) If A₁, A₂, … are disjoint sets in 𝔽, then

μ(⋃ₙ Aₙ) = ∑ₙ μ(Aₙ)

A triple (Ω, 𝔽, μ) is a **measure space**.

### Immediate consequences you’ll use constantly

Let A, B ∈ 𝔽.

1) **Monotonicity**: If A ⊂ B then μ(A) ≤ μ(B)

Proof idea:

- •Write B = A ∪ (B\A) as disjoint union
- •Then μ(B) = μ(A) + μ(B\A) ≥ μ(A)

2) **Finite additivity** (a special case of countable additivity)

3) **Subadditivity**: μ(⋃ₙ Aₙ) ≤ ∑ₙ μ(Aₙ)

This holds even without disjointness; you can prove it by converting to disjoint pieces.

### Continuity of measure (limits of sets)

This is one of the big reasons countable additivity matters.

#### Continuity from below

If A₁ ⊂ A₂ ⊂ … (increasing sequence) and A = ⋃ₙ Aₙ, then

μ(A) = limₙ→∞ μ(Aₙ)

Sketch:

- •Define disjoint increments B₁ = A₁, Bₙ = Aₙ \ Aₙ₋₁
- •Then A = ⨆ₙ Bₙ (disjoint union)
- •μ(A) = ∑ₙ μ(Bₙ)
- •μ(Aₙ) = ∑\_{k=1}^n μ(B\_k) → ∑ₙ μ(Bₙ)

#### Continuity from above

If A₁ ⊃ A₂ ⊃ … (decreasing) and μ(A₁) < ∞ and A = ⋂ₙ Aₙ, then

μ(A) = limₙ→∞ μ(Aₙ)

The finiteness condition matters; without it the statement can fail (∞ − ∞ ambiguities).

### Examples of measures

#### 1) Counting measure

Let Ω be any set, 𝔽 = 𝒫(Ω). Define

μ(A) = number of elements in A (possibly ∞).

This makes ∫ f dμ become a sum.

#### 2) Lebesgue measure on ℝ

This is the rigorous notion of “length.” For intervals,

μ((a, b)) = b − a

and it extends to a huge σ-algebra (Lebesgue measurable sets) containing all Borel sets.

Lebesgue measure is the backbone of continuous probability and analysis.

#### 3) Probability measures

A probability space is a measure space (Ω, 𝔽, P) with P(Ω) = 1.

So probability theory is measure theory plus the normalization P(Ω)=1.

### Complete measures and why null sets matter

A set N ∈ 𝔽 is a **null set** if μ(N) = 0.

A measure space is **complete** if every subset of a null set is measurable (i.e., is in 𝔽). This is desirable because “events of probability zero” should not create measurability paradoxes when you take subsets.

Lebesgue measure is complete on the Lebesgue σ-algebra, while the Borel measure on 𝔹(ℝ) is not complete (there are subsets of Borel-null sets that are not Borel).

### Breathing room: how measures differ from intuitions

It’s tempting to think every set has a “size.” Measure theory explicitly rejects that on ℝ.

Instead you pick:

- •A σ-algebra 𝔽 large enough for your needs
- •A measure μ with properties that make limits behave

This is the trade: not every subset is measurable, but everything measurable behaves beautifully.

## Core Mechanic 3: Measurable functions and the Lebesgue integral

### Why integration needs a new definition

Riemann integration partitions the x-axis, then samples f(x). Lebesgue integration flips the perspective:

- •Partition the **y-values** (function values), and measure the size of where the function takes those values.

This is a major advantage when:

- •f has many discontinuities
- •you want convergence theorems (swap limit and integral)
- •you integrate indicator functions 1\_A, which are fundamental in probability

### Measurable functions

Given measurable spaces (Ω, 𝔽) and (S, 𝒮), a function f: Ω → S is **measurable** if

∀B ∈ 𝒮, f⁻¹(B) ∈ 𝔽.

In the common case S = ℝ with 𝒮 = 𝔹(ℝ):

- •f is measurable if {ω : f(ω) ∈ B} is measurable for every Borel set B.

In probability:

- •A real-valued random variable X is exactly a measurable function X: Ω → ℝ.

### Simple functions (the building blocks)

A **simple function** φ is a measurable function that takes only finitely many values:

φ = ∑\_{k=1}^m a\_k 1\_{A\_k}

where a\_k ≥ 0 (often start with nonnegative case) and A\_k ∈ 𝔽 are measurable.

Intuition:

- •Simple functions are “step functions,” but the steps are over arbitrary measurable sets, not just intervals.

### Defining the Lebesgue integral for nonnegative functions

We proceed in layers.

#### Step 1: integral of an indicator

For A ∈ 𝔽,

∫ 1\_A dμ = μ(A)

This aligns perfectly with probability: E[1\_A] = P(A).

#### Step 2: integral of a nonnegative simple function

If φ = ∑\_{k=1}^m a\_k 1\_{A\_k}, define

∫ φ dμ = ∑\_{k=1}^m a\_k μ(A\_k)

You can check this is well-defined (independent of representation) by refining partitions.

#### Step 3: integral of a general nonnegative measurable function

For f: Ω → [0, ∞] measurable,

∫ f dμ = sup{ ∫ φ dμ : 0 ≤ φ ≤ f, φ simple }

This definition is motivated by approximation:

- •Any nonnegative measurable function can be approximated from below by an increasing sequence of simple functions.

Concretely, you can build φ\_n by quantizing values of f into dyadic bins.

### Extending to integrable real-valued functions

For measurable f that can be positive or negative, define positive/negative parts:

f⁺ = max(f, 0),

f⁻ = max(−f, 0),

so f = f⁺ − f⁻ and |f| = f⁺ + f⁻.

Then define:

∫ f dμ = ∫ f⁺ dμ − ∫ f⁻ dμ

provided at least one of ∫ f⁺ dμ, ∫ f⁻ dμ is finite (and for **integrable** functions we require ∫ |f| dμ < ∞).

### Why this definition is powerful

It bakes in limit behavior.

If f\_n ↑ f (pointwise increasing), then the integrals converge:

∫ f\_n dμ ↑ ∫ f dμ

This is not an extra theorem; it is tightly tied to the “sup of simple functions” construction.

### Key convergence theorems (stated carefully)

These are the tools you will constantly use in probability and ML theory.

#### Monotone Convergence Theorem (MCT)

If 0 ≤ f₁ ≤ f₂ ≤ … and f\_n → f pointwise, then

limₙ ∫ f\_n dμ = ∫ f dμ.

#### Fatou’s Lemma

For nonnegative measurable f\_n,

∫ (lim infₙ f\_n) dμ ≤ lim infₙ ∫ f\_n dμ.

#### Dominated Convergence Theorem (DCT)

If f\_n → f pointwise, and there exists an integrable g with |f\_n| ≤ g for all n, then

limₙ ∫ f\_n dμ = ∫ f dμ.

Why DCT is a big deal in probability:

- •It justifies exchanging limit and expectation: if X\_n → X and |X\_n| ≤ Y with E|Y| < ∞, then E[X\_n] → E[X].

### Breathing room: the philosophical shift

Riemann integration asks: “How do we slice the domain into intervals?”

Lebesgue integration asks: “How large is the set of points where the function takes certain values?”

That shift is exactly what you want for probability:

- •Expectation is a weighted average over outcomes ω ∈ Ω, weighted by P.
- •Events are sets; indicator functions reduce integration to measuring sets.

## Application/Connection: Probability, densities, and Radon–Nikodym

### Probability spaces as measure spaces

A probability space is (Ω, 𝔽, P) with P(Ω)=1. Then expectation is just a Lebesgue integral:

E[X] = ∫\_Ω X(ω) dP(ω)

and for events A ∈ 𝔽,

P(A) = ∫ 1\_A dP.

This unifies discrete and continuous cases.

### Discrete vs continuous: same definition, different μ

#### Discrete

If Ω is countable and P({ω}) = p(ω), then for X: Ω → ℝ,

E[X] = ∑\_{ω∈Ω} X(ω) p(ω)

This is exactly ∫ X dP where P is a measure on 𝒫(Ω).

#### Continuous

If Ω = ℝ and P has a density f with respect to Lebesgue measure μ (length), then

P(A) = ∫ 1\_A(x) f(x) dμ(x)

and

E[X] = ∫ x f(x) dμ(x)

But the key phrase is “with respect to.” That is measure-theoretic.

### Absolute continuity and why some distributions have no density

Given two measures ν and μ on the same measurable space, we say

ν ≪ μ (ν is absolutely continuous w.r.t. μ)

if μ(A)=0 ⇒ ν(A)=0.

In probability:

- •If P is absolutely continuous with respect to Lebesgue measure, then P has a density.
- •If P has point masses (atoms), it is not absolutely continuous w.r.t. Lebesgue measure.
- •Mixtures can be partly absolutely continuous and partly singular.

### Radon–Nikodym theorem (the measure-theoretic meaning of “density”)

If ν and μ are σ-finite measures and ν ≪ μ, then there exists a measurable function f such that for all A ∈ 𝔽,

ν(A) = ∫\_A f dμ.

We write f = dν/dμ, the **Radon–Nikodym derivative**.

In probability:

- •If P ≪ μ (Lebesgue measure), then f = dP/dμ is the probability density function.

This is the rigorous replacement for “P has a pdf.”

### Change of measure (a frequent ML/probability maneuver)

If you can write

dν = f dμ,

then integrals transform as:

∫ h dν = ∫ h f dμ.

This is the backbone of importance sampling and likelihood ratios.

### Conditional expectation (preview)

Measure theory also defines conditional expectation as an L²/L¹ projection onto a sub-σ-algebra:

E[X | 𝔾]

where 𝔾 ⊂ 𝔽 is a σ-algebra representing partial information.

While a full treatment is another node, the measure-theoretic framing explains why conditioning is about σ-algebras (information) rather than only about random variables.

### How this enables major probability results

With σ-algebras, measures, and Lebesgue integration, you can state and prove:

- •Laws of large numbers (limit theorems)
- •Central limit theorem (via characteristic functions / tightness)
- •Martingales and optional stopping (conditional expectation)
- •Stochastic processes (filtrations: increasing σ-algebras)

And in ML theory:

- •Rigorous definitions of risk as an expectation
- •Exchanging limits in learning algorithms (e.g., consistency proofs)
- •Information-theoretic quantities as integrals (KL divergence as ∫ log(dP/dQ) dP)

## Worked Examples (3)

### Building a σ-algebra from a partition (finite information → measurable events)

Let Ω = {1,2,3,4}. Suppose you only observe whether the outcome is in A = {1,2} or in Aᶜ = {3,4}. Build the σ-algebra 𝔽 = σ({A}).

1. Start with the generating family 𝒢 = {A}. We need the smallest σ-algebra containing A and Ω.

   So we must include Ω and complements.
2. Include Ω and ∅:

   Ω ∈ 𝔽 by definition of σ-algebra.

   Then ∅ = Ωᶜ ∈ 𝔽.
3. Include A and its complement:

   A = {1,2} ∈ 𝔽.

   Aᶜ = {3,4} ∈ 𝔽.
4. Close under countable unions/intersections.

   But since Ω is finite, countable unions reduce to finite unions.

   The only unions you can form from {∅, A, Aᶜ, Ω} are again one of these four sets.
5. Therefore:

   𝔽 = {∅, {1,2}, {3,4}, Ω}.

**Insight:** A σ-algebra can be seen as the set of all events that are decidable given a limited observation. Here, observing “in A or not” induces exactly four measurable events: impossible, certainly, A, and Aᶜ.

### Measure properties: continuity from below via disjoint increments

Let (Ω, 𝔽, μ) be a measure space. Let A₁ ⊂ A₂ ⊂ … and define A = ⋃ₙ Aₙ. Prove μ(A) = limₙ μ(Aₙ).

1. Define disjoint increments:

   B₁ = A₁

   Bₙ = Aₙ \ Aₙ₋₁ for n ≥ 2

   Then Bₙ are disjoint, and each Bₙ ∈ 𝔽 because σ-algebras are closed under differences.
2. Show the union is A:

   ⋃ₙ Bₙ = A₁ ∪ ⋃\_{n≥2} (Aₙ \ Aₙ₋₁) = ⋃ₙ Aₙ = A.

   (Each new piece adds exactly what was missing before.)
3. Apply countable additivity:

   μ(A) = μ(⋃ₙ Bₙ) = ∑ₙ μ(Bₙ).
4. Express μ(Aₙ) using the same increments:

   Aₙ = ⋃\_{k=1}^n B\_k (disjoint union)

   So μ(Aₙ) = ∑\_{k=1}^n μ(B\_k).
5. Take the limit:

   limₙ μ(Aₙ) = limₙ ∑\_{k=1}^n μ(B\_k) = ∑ₙ μ(Bₙ) = μ(A).

   (The partial sums converge to the full series by definition.)

**Insight:** Continuity from below is really “measure respects growing approximations.” It’s the set-level analog of monotone convergence for integrals.

### Lebesgue integral of a simple function (indicator decomposition)

On Ω = [0,1] with Lebesgue measure μ, define φ(x) = 2·1\_[0,1/4](x) + 5·1\_(1/4,1](x). Compute ∫ φ dμ.

1. Identify the measurable pieces:

   A₁ = [0, 1/4], A₂ = (1/4, 1]

   These are Borel (hence Lebesgue measurable) subsets of [0,1].
2. Compute μ(A₁) and μ(A₂):

   μ(A₁) = 1/4 − 0 = 1/4

   μ(A₂) = 1 − 1/4 = 3/4

   (Endpoints do not affect Lebesgue measure.)
3. Use the simple function integral rule:

   ∫ φ dμ = 2·μ(A₁) + 5·μ(A₂).
4. Plug in values:

   ∫ φ dμ = 2·(1/4) + 5·(3/4)

   = 2/4 + 15/4

   = 17/4.

**Insight:** For step-like functions, Lebesgue integration is literally “value × size of region.” This is the prototype for expectation: E[X] is the average value weighted by probability mass.

## Key Takeaways

- ✓

  A σ-algebra 𝔽 is the collection of sets you are allowed to measure; it is closed under complements and countable unions (hence countable intersections).
- ✓

  A measure μ assigns sizes to sets in 𝔽 and is countably additive over disjoint unions: μ(⨆ₙ Aₙ) = ∑ₙ μ(Aₙ).
- ✓

  Countable additivity implies continuity from below/above, which is essential for reasoning about limits of events.
- ✓

  A random variable is a measurable function X: (Ω, 𝔽) → (ℝ, 𝔹(ℝ)); measurability ensures inverse images of Borel sets are events.
- ✓

  The Lebesgue integral starts with ∫ 1\_A dμ = μ(A), extends to simple functions, then to nonnegative measurable functions via supremum over simple under-approximations.
- ✓

  Monotone convergence, Fatou’s lemma, and dominated convergence are the main tools for exchanging limits and integrals (limits and expectations).
- ✓

  Densities are Radon–Nikodym derivatives: if ν ≪ μ, then dν/dμ exists and ν(A) = ∫\_A (dν/dμ) dμ.
- ✓

  Probability theory is measure theory with μ(Ω)=1; expectation is just a Lebesgue integral with respect to P.

## Common Mistakes

- ✗

  Assuming every subset of ℝ is measurable; in practice you work with Borel or Lebesgue measurable sets to avoid paradoxes.
- ✗

  Confusing an algebra with a σ-algebra: closure under finite unions is not enough for limit constructions like lim sup/lim inf of events.
- ✗

  Treating “pdf” as always existing; distributions with atoms or singular parts may not be absolutely continuous w.r.t. Lebesgue measure.
- ✗

  Using dominated convergence without actually providing an integrable dominating function g with |f\_n| ≤ g.

## Practice

easy

Let Ω = {1,2,3,4,5,6} (a die). Let A = {1,3,5} (odd outcomes). Write out the σ-algebra σ({A}) explicitly and compute P(B) for each B in that σ-algebra assuming a fair die.

**Hint:** A single set A generates {∅, Ω, A, Aᶜ}. Then use P(B) = |B|/6 for a fair die.

Show solution

σ({A}) = {∅, Ω, A, Aᶜ} with A = {1,3,5}, Aᶜ = {2,4,6}.

P(∅)=0, P(Ω)=1, P(A)=3/6=1/2, P(Aᶜ)=3/6=1/2.

medium

Let (Ω, 𝔽, μ) be a measure space and let A, B ∈ 𝔽 with A ⊂ B and μ(B) < ∞. Show that μ(B\A) = μ(B) − μ(A).

**Hint:** Write B as a disjoint union of A and (B\A), then use countable additivity (finite case).

Show solution

Since A ⊂ B, we can write B = A ∪ (B\A) and the union is disjoint.

By additivity: μ(B) = μ(A) + μ(B\A).

Because μ(B) < ∞, subtracting is well-defined, giving μ(B\A) = μ(B) − μ(A).

hard

Define f\_n(x) = 1\_[0,n](x) on ℝ with Lebesgue measure μ. Let f(x) = 1\_[0,∞)(x). Use monotone convergence to compute limₙ ∫ f\_n dμ and compare it to ∫ f dμ.

**Hint:** The sets [0,n] increase to [0,∞). Compute each integral as a measure of an interval, noting it may be infinite.

Show solution

We have 0 ≤ f₁ ≤ f₂ ≤ … and f\_n(x) ↑ f(x) pointwise. By MCT,

limₙ ∫ f\_n dμ = ∫ f dμ.

Compute ∫ f\_n dμ = μ([0,n]) = n.

Thus limₙ ∫ f\_n dμ = limₙ n = ∞.

Also ∫ f dμ = μ([0,∞)) = ∞.

So both sides match (both infinite), illustrating that MCT allows infinite integrals naturally.

## Connections

Next nodes you can unlock or connect:

- •[Probability Spaces](/tech-tree/probability-spaces/)
- •[Random Variables as Measurable Functions](/tech-tree/measurable-random-variables/)
- •[Convergence Theorems (MCT/DCT/Fatou)](/tech-tree/convergence-theorems/)
- •[Radon–Nikodym Theorem and Densities](/tech-tree/radon-nikodym/)
- •[Conditional Expectation and σ-algebras](/tech-tree/conditional-expectation/)
- •[Stochastic Processes and Filtrations](/tech-tree/filtrations/)

Quality: B (4.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
