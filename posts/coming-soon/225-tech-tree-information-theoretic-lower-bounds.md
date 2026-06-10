---
title: Information-Theoretic Bounds
description: Fundamental limits on algorithm performance.
date: '2026-07-01'
scheduled: '2027-02-10'
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
inspiration_url: https://templeton.host/tech-tree/information-theoretic-lower-bounds/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/information-theoretic-lower-bounds/](https://templeton.host/tech-tree/information-theoretic-lower-bounds/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Information-Theoretic Bounds

AlgorithmsDifficulty: ★★★★★Depth: 7Unlocks: 0

Fundamental limits on algorithm performance.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Minimum information (Shannon entropy) required to specify the problem's solution (i.e., bits needed to distinguish among feasible answers)
- -Mutual information as the amount by which observations can reduce uncertainty about the unknown (information gained from data)
- -Fano's inequality: remaining conditional entropy lower-bounds achievable probability of error for any estimator

## Key Symbols & Notation

I(X;Y) : mutual information between random variables X and Y (bits)

## Essential Relationships

- -Mutual information equals entropy reduction: I(X;Y) = H(X) - H(X|Y)

## Prerequisites (2)

[Entropy5 atoms](/tech-tree/entropy/)[Big O Notation6 atoms](/tech-tree/big-o/)

Advanced Learning Details

### Graph Position

72

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

7

Chain Length

### Cognitive Load

5

Atomic Elements

38

Total Elements

L2

Percentile Level

L3

Atomic Level

### All Concepts (14)

- - Joint entropy H(X,Y): uncertainty of a pair of random variables considered jointly
- - Conditional entropy H(X|Y): residual uncertainty in X after observing Y
- - Mutual information I(X;Y): amount of information Y provides about X
- - Kullback–Leibler divergence D(P||Q): measure of distinguishability (relative entropy) between two distributions
- - Total variation distance TV(P,Q): maximal difference in probabilities assigned by P and Q (used for hypothesis distinguishability)
- - Information-theoretic lower bound (decision/estimation): using information measures to prove a minimum number of queries/samples/bits any algorithm needs
- - Fano's inequality: a bound relating probability of error in decoding/estimation to conditional entropy
- - Le Cam's two-point (or reduction) method: deriving lower bounds by reducing to distinguishing two hypotheses
- - Packing/covering numbers (metric entropy): count of well-separated parameter values used to lower-bound complexity
- - Minimax risk and its information-based lower bounds: worst-case estimation error lower bounds obtained via information measures
- - Data-processing principle in information terms: information cannot increase through a channel/processing step (used to propagate bounds)
- - Sample-complexity via mutual information: bounding how many samples are needed by comparing total information available to information required to identify parameter/value
- - Pinsker-type bounds connecting KL and TV: inequalities that convert divergence bounds into error-probability bounds
- - Product-measure additivity of KL for independent samples: KL between product distributions scales linearly with sample size

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Some algorithmic problems are hard not because we haven’t found the right trick yet, but because the input simply cannot reveal the answer fast enough. Information-theoretic bounds formalize that idea: regardless of cleverness, you need a minimum number of bits from the world to identify the correct output with small error.

TL;DR:

Information-theoretic lower bounds argue that any algorithm must acquire enough information to distinguish among many possible answers. You quantify (1) how much uncertainty the problem initially has via entropy H(X), (2) how much information each observation can provide via mutual information I(X;Y), and (3) how remaining uncertainty forces errors via Fano’s inequality. This yields lower bounds on sample complexity, query complexity, and communication—even for optimal algorithms.

## What Is an Information-Theoretic Bound?

### Why these bounds exist

In many lower-bound arguments, you don’t analyze a specific algorithm—you analyze the *best possible* algorithm. Information-theoretic lower bounds do this by treating the unknown solution as a random variable and asking:

- •How many possible “worlds” (inputs/instances) are consistent with what the algorithm has seen?
- •How many bits must be learned to identify the correct world (or correct answer) with small error?

If the observations do not carry enough information, then *any* estimator/algorithm must fail with nontrivial probability.

This perspective is powerful because it separates two things:

1. 1)**Intrinsic ambiguity of the task**: How many plausible answers exist? (Entropy.)
2. 2)**Information per observation**: How much can one sample/query/bit of communication reduce uncertainty? (Mutual information.)

Then a lower bound follows from a budget argument:

- •You start with uncertainty H(X) bits about the unknown X.
- •After seeing data Y, your remaining uncertainty is H(X|Y).
- •The reduction is I(X;Y) = H(X) − H(X|Y).

If each observation yields at most a small number of bits, you need many observations to shrink uncertainty enough.

### What counts as “information” in algorithms?

Depending on the model, the algorithm obtains information by:

- •**Samples**: i.i.d. draws from a distribution depending on an unknown parameter.
- •**Queries**: comparisons, membership queries, oracle access.
- •**Communication**: bits exchanged between parties.
- •**Probes**: cell-probe/model of memory accesses.

Information-theoretic bounds are most natural when the algorithm’s interaction with the input can be represented as a random variable Y produced from X via some channel p(y|x) (possibly adaptive).

### A canonical setup

Let X be an unknown “instance label” (e.g., which hypothesis is true). The algorithm observes Y (data, transcript, query answers) and outputs an estimate \(\hat{X}\). If the algorithm must succeed with error ≤ δ:

- •We want to show: for any algorithm, if the number of observations m is too small, then P(\(\hat{X} \neq X\)) is bounded below by some constant.

The three core tools in this node are:

- •**Counting/entropy**: bits needed to distinguish answers.
- •**Mutual information**: how much observations can reduce uncertainty.
- •**Fano’s inequality**: converts remaining uncertainty into a lower bound on error.

### Entropy as “bits to specify the answer”

If X is uniform over M possible cases, then

- •H(X) = log₂ M bits.

Even if X isn’t uniform, H(X) captures the average number of bits needed to describe X optimally.

This yields the first intuition: if your observations only reveal, say, ≤ 0.1 bits each on average, you need about (log₂ M)/0.1 observations to identify X reliably.

### What information-theoretic bounds are (and are not)

They are:

- •**Model-agnostic** within a chosen information model (samples, oracle answers, communication).
- •**Often tight** for many statistical estimation tasks.
- •**Non-constructive**: they show limits, not algorithms.

They are not:

- •Always the right tool for *time* lower bounds in the standard RAM model (those are much harder).
- •Automatically tight for every problem: you might get a valid but loose lower bound if your chosen hard instance family is not sharp.

### A quick comparison: information vs. computation

| Question | Information-theoretic view | Computational view |
| --- | --- | --- |
| What limits success? | Not enough bits in observations | Not enough time/operations |
| Typical output | Sample/query/communication lower bound | Time lower bound (rare) |
| Tools | H(·), I(·;·), Fano, data processing | Reductions, circuit complexity, fine-grained |
| Handles randomness/noise? | Naturally | Often awkward |

The rest of this lesson builds the standard pipeline: choose a family of hard instances (a random X), model what algorithm sees (Y), upper-bound I(X;Y), and then invoke Fano to lower-bound error unless m is large.

## Core Mechanic 1: Minimum Information Needed (Entropy + Packing)

### Why entropy appears in lower bounds

Before any observation, the algorithm does not know which instance it is facing. If there are many plausible instances, then the algorithm has large uncertainty.

To turn “many plausible instances” into a number, we choose a random variable X indexing instances. Two common designs:

1. 1)**Finite hypothesis set**: X ∈ {1,2,…,M} uniform.
2. 2)**Packing in a metric space**: choose M well-separated parameters θ₁,…,θ\_M, and let X be uniform over them.

The second is crucial in estimation problems where the unknown is continuous (mean estimation, regression coefficients **w**, etc.). You discretize the space into many separated candidates so that:

- •If an algorithm can estimate θ to small error ε, it can also identify which θ\_i generated the data.

That creates a bridge from estimation accuracy to multi-way hypothesis testing.

### Entropy lower bounds via counting

Suppose the algorithm must output an element of some answer set A (e.g., which of M cases holds). If there are M equally likely answers, then:

- •H(X) = log₂ M.

Interpretation: even with an optimal prefix code, you’d need ~log₂ M bits to specify the answer.

Now connect to observations Y. The maximum information you could possibly gain about X from Y is I(X;Y). If I(X;Y) is much smaller than H(X), then a lot of uncertainty remains.

### The “packing” trick (turning continuous to discrete)

Suppose the goal is to estimate a parameter θ ∈ Θ with error ≤ ε in some metric d(·,·). Build a set {θ₁,…,θ\_M} such that

- •d(θ\_i, θ\_j) ≥ 2ε for all i ≠ j.

This is a 2ε-packing (sometimes also called a separated set). If the estimator outputs \(\hat{θ}\) with d(\(\hat{θ}\), θ) ≤ ε, then \(\hat{θ}\) must be closer to the correct θ\_i than to any other θ\_j. That means from \(\hat{θ}\) we can decode X with zero error.

So:

- •Accurate estimation ⇒ accurate identification of X.

Therefore, if we show identification requires many samples/queries, then estimation also requires many.

### A standard reduction: estimation ⇒ classification

Let X be uniform on {1,…,M}. Conditioned on X=i, the world generates observations Y according to distribution P\_i.

Any estimator/algorithm produces output \(\hat{X}\) from Y. If we can prove that for m observations,

- •for every algorithm, P(\(\hat{X} \neq X\)) ≥ 0.3,

then no algorithm can solve the corresponding estimation problem with high probability at that sample size.

### Mutual information begins the bridge

At this point we have identified the “needed information”: H(X) ≈ log₂ M. Next we need to limit how much the algorithm can learn from its interactions.

But before that, notice a subtlety:

- •H(X) itself does not produce a lower bound unless we can argue I(X;Y) is small.

So entropy is the *demand* (how much must be learned), while mutual information is the *supply* (how much can be learned).

### Practical design choices for hard instances

When selecting {θ\_i} or distributions {P\_i}, you want:

1. 1)**Large M**: many hypotheses ⇒ large H(X).
2. 2)**Small distinguishability per sample**: the distributions P\_i and P\_j should be close, so each observation carries little information about X.

Common closeness measures used to upper-bound I(X;Y) include:

- •KL divergence D(P\_i ‖ P\_j)
- •χ² divergence
- •Total variation (often via Pinsker: TV² ≤ (1/2)KL)

Even though KL is not in the node’s prerequisite list, it appears naturally because mutual information can be upper-bounded by expected KL.

### The core picture

You can think of the process as:

- •X (hidden label) → observations Y (through a noisy channel) → estimate \(\hat{X}\).

If the channel is too noisy, even the optimal decoder cannot recover X reliably.

That statement becomes formal with the next mechanic: mutual information and the data processing inequality.

## Core Mechanic 2: Mutual Information as the Rate of Learning

### Why mutual information is the right accounting tool

An algorithm doesn’t just need to see *data*; it needs to see *data that depends on the unknown*. Mutual information captures exactly how much knowing Y reduces uncertainty about X.

Definition (in bits):

- •I(X;Y) = H(X) − H(X|Y)

Key interpretations:

- •I(X;Y) = 0 means Y tells you nothing about X.
- •I(X;Y) = H(X) means Y fully determines X (in principle).

So if we can upper-bound I(X;Y) by something like m·c (m samples times c bits per sample), then we can relate m to H(X).

### Data processing inequality (DPI)

A universal constraint: information cannot increase by post-processing.

If X → Y → Z is a Markov chain (Z is computed from Y), then

- •I(X;Z) ≤ I(X;Y)

This matters because the algorithm’s internal state, transcript, and final answer \(\hat{X}\) are all functions of observed data. DPI says:

- •I(X; \(\hat{X}\)) ≤ I(X; Y)

So it suffices to bound I(X;Y), even if the algorithm is arbitrarily clever.

### Chain rule: information accumulates over steps

If Y = (Y₁,…,Y\_m) are m observations (possibly dependent), then:

- •I(X;Y) = ∑\_{t=1}^m I(X; Y\_t | Y₁,…,Y\_{t−1})

This is crucial for *adaptive* algorithms: Y\_t may depend on past observations through the algorithm’s choice of query or experiment.

Even then, the chain rule holds, and you can bound each term by the maximum information one step can reveal.

### Bounding per-sample information (a common template)

A typical setup: conditioned on X=i, the observations are i.i.d. from P\_i. Then

- •I(X; Y₁,…,Y\_m) ≤ m · I(X;Y₁)

when Y\_t are conditionally independent given X.

More generally, with adaptivity you often show:

- •I(X;Y\_t | history) ≤ c

for all t, and conclude I(X;Y) ≤ m c.

### Relating mutual information to distinguishability

One standard identity (useful as a bounding technique) is:

- •I(X;Y) = E\_X [ D( P(Y|X) ‖ P(Y) ) ]

where P(Y) is the mixture distribution ∑\_x P(x)P(Y|x).

This expresses information as “how far each conditional distribution is from the mixture.” If all P(Y|X=x) are close to each other, then they are all close to the mixture, giving small I(X;Y).

A common upper bound for finite hypothesis sets with X uniform:

- •I(X;Y) ≤ (1/M²) ∑\_{i,j} D(P\_i ‖ P\_j)

(up to standard variants/inequalities). The exact constant form depends on the lemma used, but the theme is stable: pairwise closeness limits information.

### Small information per sample ⇒ many samples required

At a high level, once you have:

- •H(X) ≈ log₂ M
- •I(X;Y) ≤ m·c

then remaining uncertainty is

- •H(X|Y) = H(X) − I(X;Y) ≥ log₂ M − m·c

If m·c is much smaller than log₂ M, then H(X|Y) remains large. Large conditional entropy means many labels are still plausible after seeing the data.

But to turn that into a concrete *error probability* statement, we need Fano’s inequality.

### Mutual information in query/decision-tree problems

In comparison-based sorting, each comparison yields 1 bit of outcome (less/greater; ignore equality for simplicity). If the hidden object is which permutation is present, then:

- •H(X) = log₂(n!)

If the transcript Y consists of m comparison outcomes, then H(Y) ≤ m bits and thus I(X;Y) ≤ H(Y) ≤ m.

This is the information-theoretic skeleton behind the classic Ω(n log n) comparisons lower bound.

Important nuance: this argument assumes the comparisons are the only information source (no extra structure). It cleanly demonstrates how information per query constrains performance.

## Core Mechanic 3: Fano’s Inequality (Uncertainty Forces Error)

### Why we need Fano

So far we can show that after observing Y, the algorithm still has uncertainty H(X|Y). But an algorithm doesn’t output a distribution; it outputs a single guess \(\hat{X}\). We need a theorem that converts “remaining uncertainty” into “probability of being wrong.”

Fano’s inequality does exactly that for multi-class identification.

### Statement (one common form)

Let X take values in {1,…,M}. Let \(\hat{X}\) be any estimator based on Y. Define error event E = [\(\hat{X} \neq X\)]. Then:

- •H(X|Y) ≤ h₂(P(E)) + P(E)·log₂(M−1)

where h₂(p) = −p log₂ p − (1−p) log₂(1−p) is the binary entropy.

Rearranging yields a lower bound on P(E). A widely used corollary is:

- •P(E) ≥ 1 − ( I(X;Y) + 1 ) / log₂ M

(assuming X is uniform; the “+1” comes from bounding h₂(p) ≤ 1).

So if I(X;Y) is significantly smaller than log₂ M, then the error probability must be bounded away from 0.

### Derivation sketch (showing the work)

The key idea: to describe X given Y, you can describe whether you made an error, and if you did, which wrong label occurred.

Let E be the error indicator. Then:

1) Expand conditional entropy by introducing E:

H(X|Y)

= H(X, E | Y) − H(E | X, Y)

But E is a function of (X, \(\hat{X}\)), and \(\hat{X}\) is a function of Y, so given X and Y, E is determined. Thus:

H(E | X, Y) = 0

So:

H(X|Y) = H(X, E | Y)

2) Use chain rule:

H(X, E | Y)

= H(E | Y) + H(X | E, Y)

3) Bound each term:

- •H(E|Y) ≤ H(E) = h₂(P(E))

For the second term, condition on whether an error happened:

H(X | E, Y)

= P(E=0)·H(X | E=0, Y) + P(E=1)·H(X | E=1, Y)

If E=0, then \(\hat{X}=X\), so X is determined by \(\hat{X}\) and hence by Y, giving:

H(X | E=0, Y) = 0

If E=1, then X can be any of the M−1 wrong labels, so:

H(X | E=1, Y) ≤ log₂(M−1)

Combine:

H(X | E, Y) ≤ P(E)·log₂(M−1)

4) Put it together:

H(X|Y)

≤ h₂(P(E)) + P(E)·log₂(M−1)

This is Fano.

### What Fano is telling you intuitively

- •If you want P(E) to be small, the RHS must be small.
- •That forces H(X|Y) to be small.
- •Small H(X|Y) means I(X;Y) must be close to H(X) ≈ log₂ M.

So: to get low error, you must learn almost all the bits needed to specify X.

### When to use Fano vs simpler counting

If your transcript Y is deterministic and has at most 2^m possible outcomes, you can sometimes argue:

- •2^m ≥ M ⇒ m ≥ log₂ M

That’s a noiseless, worst-case counting bound.

Fano is the noisy/general version:

- •even if transcripts are randomized and overlapping across hypotheses, you still need enough mutual information to drive error down.

This makes it indispensable for sample complexity and noisy query models.

## Application/Connection: Proving Fundamental Limits (Sorting, Estimation, and Beyond)

### A reusable proof template

Most information-theoretic lower bounds follow a pattern:

1. 1)**Choose a hard prior** over instances/parameters: X.
2. 2)**Define observations** Y the algorithm gets after m interactions.
3. 3)**Upper-bound I(X;Y)** using model properties (noise, limited bits per query, limited KL per sample).
4. 4)**Apply Fano** to show that unless m is large, P(error) is large.

This turns “how hard is it?” into “how much can you learn per step?”

### Example domains

#### 1) Comparison sorting

- •Unknown X is the permutation of n distinct keys.
- •H(X) = log₂(n!).
- •Each comparison gives 1 bit (less/greater), so I(X;Y) ≤ m.
- •Need m ≥ log₂(n!) ≈ n log₂ n − 1.44n.

This is a clean information-theoretic bound matching the classical Ω(n log n).

#### 2) Noisy binary search / noisy comparisons

If each comparison is flipped with probability η, then each query conveys < 1 bit of information. You can quantify I(X;Y\_t | history) ≤ 1 − h₂(η) bits (a standard channel capacity fact for a binary symmetric channel). Then:

- •I(X;Y) ≤ m(1 − h₂(η))

So noisy comparisons increase query complexity by a factor ≈ 1/(1 − h₂(η)).

#### 3) Estimating a mean under Gaussian noise

Let the unknown be θ ∈ {−ε, +ε}. Each sample Y\_t = θ + Z\_t where Z\_t ∼ N(0,σ²). One sample provides limited information about which sign is correct. With m samples, I(X;Y) grows like m·(ε²/σ²) for small ε/σ, yielding m = Ω(σ²/ε²) to achieve small error. This matches standard statistical rates.

#### 4) Communication complexity

Let X be split across two parties. The transcript T has length m bits, hence I(X;T) ≤ m. If the function output requires distinguishing among many possibilities, then H(output) is large and you derive m = Ω(H(output)) or stronger.

### Choosing the “right” X: art and engineering

A lower bound is only as strong as the hardest distribution family you pick. Typical strategies:

- •**Uniform over a large finite set**: maximizes H(X).
- •**Nearly indistinguishable distributions**: minimizes I(X;Y) growth.
- •**Symmetry**: makes analysis clean (e.g., random sign vectors, random subsets).

### How these bounds relate to Big-O

Big-O is typically used for upper bounds: algorithm A runs in O(f(n)). Information-theoretic arguments yield Ω(·) lower bounds on resources such as:

- •Ω(m) samples
- •Ω(q) oracle queries
- •Ω(b) bits communicated

In some problems (sorting), this directly yields a time lower bound in a restricted comparison model. In others (statistical estimation), it yields sample complexity lower bounds; computation may be easier or harder depending on the setting.

### A compact “mental checklist”

When you face a new problem and wonder if an information bound applies, ask:

- •Can I model the unknown as a random variable X with many possible values?
- •Can I describe the algorithm’s interaction as observations Y with limited information per step?
- •Can I bound I(X;Y) from above without assuming a particular algorithm?
- •Do I ultimately need an error probability lower bound? (Use Fano.)

If yes, you likely can produce a meaningful information-theoretic lower bound.

## Worked Examples (3)

### Lower bound for comparison sorting via entropy (Ω(n log n) comparisons)

We sort n distinct keys using only pairwise comparisons. Let X be the (unknown) total order/permutation of the n keys, assumed uniform over all n! permutations. The algorithm performs m comparisons and observes transcript Y ∈ {0,1}^m (each bit indicates the comparison outcome). We show m ≥ log₂(n!) comparisons are necessary for zero-error sorting in the comparison model.

1. 1) Model the uncertainty in the input order.

   X ∈ S\_n, uniform.

   H(X) = log₂(n!).
2. 2) Relate the transcript to information gained.

   Each comparison outcome is 1 bit, so the full transcript Y has at most 2^m possible values.

   Thus H(Y) ≤ m.
3. 3) Use the mutual information bound.

   I(X;Y) ≤ H(Y) ≤ m.
4. 4) For a correct sorting algorithm (zero error), Y must determine X’s order uniquely.

   That means H(X|Y) = 0.

   So:

   I(X;Y) = H(X) − H(X|Y) = H(X).
5. 5) Combine.

   H(X) = I(X;Y) ≤ m

   ⇒ m ≥ log₂(n!).
6. 6) Convert log₂(n!) to n log n.

   Using Stirling’s approximation:

   log₂(n!) ≈ n log₂ n − (log₂ e) n + O(log n).

   So m = Ω(n log n).

**Insight:** This is an information budget argument: the unknown permutation contains about n log₂ n bits. Each comparison reveals at most 1 bit, so you need Ω(n log n) comparisons—no algorithmic cleverness can change that in the comparison model.

### Fano’s inequality gives a sample complexity lower bound for identifying a biased coin

Unknown X ∈ {1,…,M} is uniform. Conditioned on X=i, we observe m i.i.d. samples Y\_t from a distribution P\_i. Suppose we can show a per-sample information bound I(X;Y\_t) ≤ α bits (for example because all P\_i are very similar). Derive an m requirement to make error ≤ δ using Fano.

1. 1) Start from Fano’s corollary.

   P(error) ≥ 1 − (I(X;Y) + 1)/log₂ M.
2. 2) Use conditional independence to add information over samples.

   Y = (Y₁,…,Y\_m), with Y\_t i.i.d. given X.

   Then:

   I(X;Y) ≤ ∑\_{t=1}^m I(X;Y\_t) = mα.
3. 3) Plug into Fano.

   P(error) ≥ 1 − (mα + 1)/log₂ M.
4. 4) Require P(error) ≤ δ.

   We need:

   1 − (mα + 1)/log₂ M ≤ δ

   ⇒ (mα + 1)/log₂ M ≥ 1 − δ

   ⇒ mα + 1 ≥ (1 − δ) log₂ M

   ⇒ m ≥ ((1 − δ) log₂ M − 1)/α.
5. 5) Interpret.

   If α is small (each sample is only weakly informative), m must scale like (log M)/α.

**Insight:** Fano turns an information upper bound into an unavoidable error floor. If each sample carries only α bits about which hypothesis is true, you need on the order of log₂ M / α samples to identify the correct hypothesis with small error.

### Noisy 20 questions: lower bound via per-query mutual information

There is an unknown X uniform over {1,…,N}. You may ask yes/no questions adaptively, but each answer is flipped independently with probability η (0 < η < 1/2). Let the transcript be Y = (Y₁,…,Y\_m). Show that m must be at least about log₂ N divided by the per-query information (≈ 1 − h₂(η)) to drive error small.

1. 1) Needed information.

   H(X) = log₂ N.
2. 2) Apply Fano (target error δ).

   δ ≥ P(error) ≥ 1 − (I(X;Y) + 1)/log₂ N

   ⇒ I(X;Y) ≥ (1 − δ) log₂ N − 1.
3. 3) Use chain rule for adaptive queries.

   I(X;Y) = ∑\_{t=1}^m I(X;Y\_t | Y₁,…,Y\_{t−1}).
4. 4) Bound each term by the channel capacity of a noisy yes/no answer.

   Given the true (noise-free) answer A\_t ∈ {0,1}, the observed Y\_t is A\_t flipped with probability η.

   No matter how the question is chosen, Y\_t is A\_t passed through a binary symmetric channel BSC(η), so:

   I(X;Y\_t | history) ≤ I(A\_t;Y\_t | history) ≤ 1 − h₂(η).
5. 5) Sum over m queries.

   I(X;Y) ≤ m(1 − h₂(η)).
6. 6) Combine with step (2).

   m(1 − h₂(η)) ≥ (1 − δ) log₂ N − 1

   ⇒ m ≥ ((1 − δ) log₂ N − 1)/(1 − h₂(η)).

**Insight:** Noise reduces the information per answer from 1 bit to at most 1 − h₂(η) bits. The lower bound is a direct “bits required / bits per query” calculation, formalized through mutual information and Fano.

## Key Takeaways

- ✓

  Information-theoretic lower bounds treat the unknown instance/answer as a random variable X and the algorithm’s observations as Y.
- ✓

  Entropy H(X) quantifies the *minimum information* (in bits) needed to identify the correct hypothesis among many possibilities; for uniform M-way choice, H(X)=log₂ M.
- ✓

  Mutual information I(X;Y)=H(X)−H(X|Y) quantifies how much the observations reduce uncertainty; it is the “rate of learning.”
- ✓

  Data processing inequality ensures post-processing can’t create information: I(X;\hat{X}) ≤ I(X;Y), so you can bound any algorithm by bounding its observation channel.
- ✓

  Chain rule lets you handle adaptivity: I(X;Y)=∑ I(X;Y\_t | history), so a per-step information cap yields a total information cap.
- ✓

  Fano’s inequality converts remaining uncertainty into an unavoidable error probability: if I(X;Y) ≪ log₂ M, then any estimator must err with probability bounded away from 0.
- ✓

  A common strategy for continuous problems is packing: build many well-separated parameters so accurate estimation would imply identifying one of M hypotheses.
- ✓

  These bounds typically yield Ω(sample/query/communication) limits; they can match classical results like Ω(n log n) comparisons for sorting and show noise inflation factors in query models.

## Common Mistakes

- ✗

  Assuming each observation gives 1 bit of information. In noisy or continuous settings, the mutual information per sample can be far smaller (and must be bounded, not guessed).
- ✗

  Forgetting adaptivity: bounding I(X;Y) as m·I(X;Y₁) without checking conditional independence or without using the chain rule correctly.
- ✗

  Using Fano with an M that is too small (weak packing), which yields a valid but loose bound; the choice of hypothesis family is crucial.
- ✗

  Confusing worst-case and average-case: information-theoretic bounds are often proved under a chosen prior over instances; you must state clearly what guarantee (average error vs worst-case) you conclude.

## Practice

easy

You have an unknown X uniform over {1,…,256}. You observe m samples Y₁,…,Y\_m such that for every t, I(X;Y\_t | Y₁,…,Y\_{t−1}) ≤ 0.2 bits. Using Fano’s corollary, give a lower bound on m needed to ensure P(error) ≤ 0.1.

**Hint:** Use log₂ 256 = 8. Bound I(X;Y) by the chain rule, then require I(X;Y) ≥ (1−δ)log₂ M − 1.

Show solution

Here M=256 so log₂ M=8 and δ=0.1.

Fano corollary rearranged:

I(X;Y) ≥ (1−δ)log₂ M − 1 = 0.9·8 − 1 = 7.2 − 1 = 6.2 bits.

Chain rule with per-step cap:

I(X;Y) = ∑\_{t=1}^m I(X;Y\_t | history) ≤ 0.2m.

So 0.2m ≥ 6.2 ⇒ m ≥ 31.

(If m must be an integer, m ≥ 31.)

medium

Comparison sorting with duplicates: Suppose n items contain only k distinct keys (k ≤ n), and the algorithm must output a stable sorted order. Give an information-theoretic lower bound on the number of comparisons in terms of the number of distinct stable outputs.

**Hint:** Let X be the true stable-sorted outcome among M possibilities. Each comparison yields 1 bit, so need at least log₂ M comparisons (up to zero-error assumptions). What is M for multiset permutations with stability?

Show solution

Let the multiset have counts c₁,…,c\_k summing to n. The number of distinct total orders of the multiset (ignoring stability) is n!/∏\_{i=1}^k c\_i!. For a stable sort, the relative order within equal keys is fixed, so the number of possible stable sorted outputs equals the number of possible key sequences consistent with the unknown input arrangement, which is exactly M = n!/∏ c\_i!.

If X is uniform over these M possibilities, then H(X)=log₂ M.

A transcript of m comparisons has at most 2^m outcomes, so m ≥ log₂ M = log₂(n!) − ∑\_{i=1}^k log₂(c\_i!).

This lower bound reduces to Ω(n log n) when all keys are distinct (all c\_i=1), and becomes smaller when many duplicates exist.

hard

Noisy yes/no identification: X is uniform on {1,…,N}. You can ask adaptive yes/no questions, each answer flipped with probability η=0.1. Using the bound m ≥ ((1−δ)log₂ N − 1)/(1 − h₂(η)), estimate m needed for N=1,048,576 (which is 2^20) and δ=0.01.

**Hint:** Compute log₂ N = 20. Compute h₂(0.1) ≈ −0.1 log₂ 0.1 − 0.9 log₂ 0.9 ≈ 0.469. Then 1 − h₂(η) ≈ 0.531.

Show solution

Given N=2^20, log₂ N=20. With δ=0.01:

Required information:

(1−δ)log₂ N − 1 = 0.99·20 − 1 = 19.8 − 1 = 18.8 bits.

Binary entropy at η=0.1:

h₂(0.1) = −0.1 log₂ 0.1 − 0.9 log₂ 0.9

≈ −0.1(−3.3219) − 0.9(−0.1520)

≈ 0.3322 + 0.1368

≈ 0.469.

So per-query info cap ≈ 1 − h₂(0.1) ≈ 0.531.

Thus:

m ≥ 18.8 / 0.531 ≈ 35.4.

So at least about 36 noisy questions are required (by this information-theoretic bound) to get error ≤ 0.01.

## Connections

Next nodes to study:

- •[Mutual Information Basics](/tech-tree/mutual-information-basics/)
- •[KL Divergence and Pinsker’s Inequality](/tech-tree/kl-divergence-pinsker/)
- •[Yao’s Minimax Principle](/tech-tree/yaos-minimax/)
- •[Decision Trees and Comparison Lower Bounds](/tech-tree/decision-tree-lower-bounds/)
- •[Sample Complexity Lower Bounds](/tech-tree/sample-complexity-lower-bounds/)
- •[Communication Complexity: Information Complexity](/tech-tree/information-complexity/)

Quality: B (4.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
