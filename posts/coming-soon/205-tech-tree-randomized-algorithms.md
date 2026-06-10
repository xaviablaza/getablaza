---
title: Randomized Algorithms
description: Using randomness for efficiency. Las Vegas vs Monte Carlo.
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
permalink: /tech-tree/randomized-algorithms/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Randomized Algorithms

AlgorithmsDifficulty: ★★★★☆Depth: 4Unlocks: 0

Using randomness for efficiency. Las Vegas vs Monte Carlo.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Randomized algorithm: an algorithm that uses internal random bits so its output and running time are distributions rather than single values
- -Las Vegas vs Monte Carlo distinction: Las Vegas algorithms always return a correct result but have randomized running time (typically analyzed by expectation); Monte Carlo algorithms run within a (deterministic) time bound but return a correct result only with some probability (bounded error)
- -Amplification (error reduction): independent repetitions (and simple aggregation like majority) reduce Monte Carlo error exponentially while increasing cost linearly

## Key Symbols & Notation

A(x; r) -- algorithm A as a function of input x and random bits rPr[·] -- probability operator (probability taken over the algorithm's random bits)

## Essential Relationships

- -Random bits induce distributions and classify guarantees: A(x; r) with r uniform induces a distribution over outputs and runtimes (expressed using Pr[·]); Monte Carlo vs Las Vegas describe whether correctness or runtime is the randomized quantity, and independent repetitions of r give exponential error reduction for Monte Carlo.

## Prerequisites (2)

[Expected Value5 atoms](/tech-tree/expected-value/)[Big O Notation6 atoms](/tech-tree/big-o/)

Advanced Learning Details

### Graph Position

57

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

33

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (15)

- - Randomized algorithm: an algorithm that makes random choices (internal coin flips or random bits) as part of its logic
- - Source of randomness: using random bits or a random number generator as an algorithmic resource
- - Runtime as a random variable: the algorithm's running time T is itself random and has a distribution
- - Success/correctness probability: the probability that a randomized algorithm returns a correct answer on a given input
- - Error probability (failure probability): the probability the algorithm returns an incorrect answer (often denoted by ε)
- - Las Vegas algorithm: a randomized algorithm that always returns a correct answer but whose running time is random (performance metric often is expected running time)
- - Monte Carlo algorithm: a randomized algorithm with (typically) bounded running time but only returns a correct answer with some probability (may err with probability ε)
- - One-sided error: a Monte Carlo algorithm that can err only in one direction (e.g., only false positives or only false negatives)
- - Two-sided (bounded) error: a Monte Carlo algorithm that can err in both directions but with a bounded error probability (e.g., ≤ 1/3)
- - Bounded-error algorithms / bounded-error probability: the class of algorithms with error probability upper-bounded by a fixed constant < 1/2
- - Amplification (error reduction by repetition): repeating independent runs (and combining outputs via majority/OR/etc.) to reduce error probability exponentially
- - Trade-off between runtime and error probability: reducing error (via repetition or stronger randomness) typically increases total runtime
- - Derandomization: techniques and the idea of converting randomized algorithms into deterministic ones (or simulating randomness deterministically)
- - Randomized algorithm performance metrics: expected running time, worst-case running-time distribution, and success probability as separate analysis targets
- - Complexity-class view of randomness (informal): categories of decision problems based on allowed randomness and error/expected-time guarantees (e.g., RP, BPP, ZPP)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Deterministic algorithms commit to one path. Randomized algorithms flip coins to explore many possible paths—often making the algorithm dramatically simpler or faster. The price is that the algorithm’s behavior becomes a distribution: its running time and/or its correctness depends on random bits.

TL;DR:

A randomized algorithm is A(x; r): on the same input x, different random bits r can change the execution. Las Vegas algorithms are always correct but have random running time (analyzed via E[T]). Monte Carlo algorithms have a fixed time bound but may err with probability ≤ δ. You can reduce Monte Carlo error exponentially by repeating independently and aggregating (amplification), while cost grows only linearly.

## What Is a Randomized Algorithm?

### Why randomness is a useful resource

In many algorithmic problems, the hardest part is **worst-case structure**: an adversarial input can force a deterministic algorithm to take a very slow or very complicated path.

Randomness is a way to avoid being “predictable.” Instead of choosing a specific pivot, a specific sample, or a specific hash function deterministically, we choose it **at random**. This can:

- •Break ties and symmetries cleanly.
- •Avoid inputs crafted to exploit a fixed strategy.
- •Give excellent **expected** performance even when worst-case performance is bad.
- •Make design simpler: “try a random thing; if it doesn’t work, try again.”

Randomized algorithms appear everywhere: quicksort with random pivots, randomized hashing, randomized load balancing, randomized primality testing, and many streaming/sketching methods.

### Formal definition: A(x; r)

A deterministic algorithm is a function A(x) that maps an input x to an output y.

A **randomized** algorithm is better viewed as a function of **two** inputs:

- •x: the actual input instance
- •r: a string of random bits (the algorithm’s internal coin flips)

We write:

- •**A(x; r)**

For a fixed input x, as r varies uniformly over {0,1}ᵏ (for however many bits are used), the output and runtime become random variables.

### Output and runtime become distributions

Let:

- •Y = output of A(x; r)
- •T = running time of A(x; r)

Then for a fixed x:

- •Y has a probability distribution (different r can yield different outputs)
- •T has a probability distribution (different r can take different execution paths)

We use the probability operator **Pr[·]** to indicate probability over the algorithm’s random bits:

- •Pr[ A(x; r) outputs y ]
- •Pr[ T ≥ t ]

The key point: randomness moves us from single-value statements to **probabilistic guarantees**.

### Two major kinds of guarantees

Randomized algorithms are typically analyzed by answering one (or both) of these questions:

1. 1)**How fast is it?**

- •Usually via expected time E[T] or high-probability bounds like Pr[T ≤ c · f(n)] ≥ 1 − δ.

2. 2)**How correct is it?**

- •Usually via error probability Pr[output is wrong] ≤ δ.

Different randomized algorithms put the “randomness” on different sides (runtime vs correctness). That’s exactly what the Las Vegas vs Monte Carlo distinction captures.

### A mental model: randomness as choosing a deterministic algorithm from a family

Another helpful viewpoint is:

- •A randomized algorithm is like a distribution over deterministic algorithms.

Each random string r selects a deterministic behavior Aᵣ(x) = A(x; r). Then analysis is about the average (or tail) behavior over r.

This viewpoint is extremely useful when you reason about adversaries: if an adversary fixes x first, and then you sample r, you can often guarantee good performance in expectation over r (even if some r are “bad”).

### Summary table (preview)

Here’s the core distinction we’ll build up carefully:

| Type | Time bound | Correctness | Typical analysis |
| --- | --- | --- | --- |
| Las Vegas | Random variable | Always correct | E[T], or Pr[T ≤ …] |
| Monte Carlo | Deterministic bound (or high-probability bound) | Error ≤ δ | Pr[error] ≤ δ, amplification |

We’ll now study each category in depth and learn how amplification turns “somewhat reliable” Monte Carlo answers into “overwhelmingly reliable” ones.

## Core Mechanic 1: Las Vegas vs Monte Carlo

### Why we separate them

Not all randomness is used for the same purpose.

- •Sometimes randomness is used to **speed up** the algorithm while preserving perfect correctness.
- •Sometimes randomness is used to get an answer **quickly** with a tiny chance of being wrong.

Those are qualitatively different tradeoffs, so we name them.

### Las Vegas algorithms

A **Las Vegas** randomized algorithm satisfies:

1. 1)**Correctness is guaranteed** for every run:

- •For all x and all random strings r, the output is correct.

2. 2)**Running time is random**:

- •Different r values yield different T.

So the algorithm might sometimes take longer, but it never lies.

#### How Las Vegas is analyzed

The most common guarantee is expected time:

- •E[T(x; r)] ≤ O(f(n))

where n = |x| is input size.

Sometimes we also want tail bounds, e.g.:

- •Pr[T ≤ c · f(n)] ≥ 0.99

But expectation is the classic baseline.

#### Common patterns for Las Vegas design

1. 1)**Random sampling / randomized pivot selection**

- •Example: randomized quicksort (correct always; time random)

2. 2)**Randomized search with restart**

- •“Try random choices until a certificate is found.”

The key property is that the algorithm can *verify* correctness of what it outputs, or it’s built so it cannot output an incorrect answer.

### Monte Carlo algorithms

A **Monte Carlo** randomized algorithm satisfies:

1. 1)**Running time is bounded** (often deterministically):

- •T(x; r) ≤ O(f(n)) for all r

2. 2)**Correctness is probabilistic**:

- •Pr[ A(x; r) is correct ] ≥ 1 − δ

Equivalently:

- •Pr[error] ≤ δ

Here δ is an error probability you can often tune.

#### One-sided vs two-sided error

Monte Carlo algorithms come in two flavors:

- •**One-sided error**: the algorithm can be wrong only in one direction.
- •Example structure: If it says “YES” it’s definitely YES; if it says “NO” it might be wrong (or vice versa).
- •**Two-sided error**: it can be wrong in either direction, but with small probability.

One-sided error is often easier to amplify because the “safe” answer is always trustworthy.

### Comparing them clearly

| Feature | Las Vegas | Monte Carlo |
| --- | --- | --- |
| Output correctness | Always correct | Correct w.p. ≥ 1 − δ |
| Runtime | Random variable | Usually fixed upper bound |
| Main knob | Expected time | Error probability δ |
| Typical use when… | You can verify correctness or ensure correctness structurally | Verification is expensive; approximate/decision is OK |

### A careful look at probabilities and expectations

Let’s write this with the node’s symbols.

For a randomized algorithm **A(x; r)**:

- •Correctness probability:
- •Pr[ A(x; r) is correct ]
- •Running time expectation:
- •E[ T(x; r) ]

#### Las Vegas formal condition

For all x:

- •Pr[ A(x; r) is correct ] = 1

and the analysis is about E[T(x; r)].

#### Monte Carlo formal condition

For all x:

- •T(x; r) ≤ c · f(n) for all r (or at least with very high probability)
- •Pr[ A(x; r) is correct ] ≥ 1 − δ

The analysis is about δ.

### Subtle but important: “randomized time bound” is not the same as “Monte Carlo”

Sometimes people casually say: “This randomized algorithm runs in O(n) time with high probability.” That statement alone doesn’t classify the algorithm.

To classify it, you must ask:

- •Is it **always correct**? If yes → Las Vegas (even if time is random)
- •Is the runtime always bounded but correctness is probabilistic? → Monte Carlo

It’s possible to have an algorithm where **both** runtime and correctness are probabilistic. In practice, we often convert such algorithms into one of the two standard forms by enforcing timeouts (turning it into Monte Carlo) or repeating-until-success with verification (turning it into Las Vegas).

### Example intuition without details (we’ll do full examples later)

- •Randomized quicksort:
- •Always outputs a correctly sorted array.
- •Runtime depends on how pivots split.
- •⇒ Las Vegas.

- •Randomized primality test (e.g., Miller–Rabin):
- •Always runs in time poly(log n).
- •Might declare “prime” for a composite number with small probability.
- •⇒ Monte Carlo (one-sided error, depending on variant).

You now have the taxonomy. Next we’ll learn the most powerful tool for Monte Carlo algorithms: amplification.

## Core Mechanic 2: Amplification (Error Reduction) for Monte Carlo Algorithms

### Why amplification matters

A Monte Carlo algorithm typically gives a guarantee like:

- •Pr[error] ≤ 1/3

At first, 1/3 sounds uncomfortably large. But this is the key idea:

> If you can run the algorithm multiple times with **independent** random bits, you can drive the error probability down **exponentially** while increasing time only **linearly**.

That tradeoff is one of the main reasons Monte Carlo algorithms are so useful.

### Setup: an algorithm with constant error

Assume we have a Monte Carlo algorithm A(x; r) that outputs a decision bit (YES/NO).

Let one run have error probability:

- •Pr[A is wrong] ≤ p

Usually p < 1/2 (e.g., p = 1/3).

We run A independently k times using fresh random bits r₁, r₂, …, r\_k.

Let the outputs be:

- •Z₁, Z₂, …, Z\_k

Define an aggregated answer Z\*.

Two common aggregations:

1. 1)**Majority vote** (for two-sided error)
2. 2)**OR/AND rules** (for one-sided error)

### Majority vote (two-sided error)

If each run is correct with probability ≥ 1 − p and p < 1/2, then the majority of k runs is wrong only if **more than half** the runs are wrong.

Let Xᵢ be the indicator random variable that run i is wrong:

- •Xᵢ = 1 if run i is wrong
- •Xᵢ = 0 if run i is correct

Then:

- •Pr[Xᵢ = 1] ≤ p
- •Total wrong runs: S = ∑ᵢ Xᵢ

Majority vote fails if:

- •S ≥ ⌈k/2⌉

A standard result (Chernoff/Hoeffding bounds) implies:

- •Pr[ S ≥ k/2 ] ≤ exp(−Ω(k))

So to get error ≤ δ, it suffices to take:

- •k = O(log(1/δ))

Even without proving the exact bound here, the intuition is strong: if each run is biased toward correctness, the probability that **most** runs are wrong drops exponentially.

### One-sided error amplification: simpler and even cleaner

Suppose A has one-sided error of this form:

- •If the correct answer is NO, A outputs NO always (never a false YES)
- •If the correct answer is YES, A outputs YES with probability ≥ 1 − p

Then you can amplify by repeating and taking **OR**:

- •Run k times; if any run says YES, output YES; else NO.

Why does this work?

- •On NO instances, all runs say NO (guaranteed), so no error.
- •On YES instances, error happens only if **all** k runs fail.

If each run fails with probability ≤ p, and runs are independent:

- •Pr[all k runs fail] ≤ pᵏ

So error becomes pᵏ.

To achieve error ≤ δ:

- •Choose k such that pᵏ ≤ δ

Solve:

pᵏ ≤ δ

⇒ k · log p ≤ log δ

⇒ k ≥ log(δ) / log(p)

Because 0 < p < 1, log(p) is negative, so this is:

- •k ≥ log(1/δ) / log(1/p)

Again, k = O(log(1/δ)).

### Cost of amplification

If one run costs time O(f(n)), then k repetitions cost:

- •O(k · f(n))

If k = O(log(1/δ)), then total time is:

- •O(f(n) · log(1/δ))

This is the core tradeoff:

- •**Error decreases exponentially** in k
- •**Time increases linearly** in k

### Independence is not optional

Amplification relies on the runs being independent (or close enough).

If you reuse the same random bits, you can get perfectly correlated outcomes:

- •Either all runs succeed or all fail → no improvement.

So when we say “repeat independently,” we mean:

- •fresh random bits r₁, …, r\_k

### Choosing δ in practice

Algorithm papers often present a Monte Carlo algorithm with a “constant error” like 1/3 because:

- •1/3 is convenient for proofs
- •amplification can reduce it to 2⁻⁶⁴ or 10⁻⁹ or 1/n² as needed

A common target is δ = 1/nᶜ for some constant c, so that a union bound across many algorithmic events still yields high overall success probability.

### Quick reference table: amplification recipes

| Error type | Single-run guarantee | Repeat k times | Combine outputs | New error |
| --- | --- | --- | --- | --- |
| One-sided (false negatives only) | Pr[miss] ≤ p | independent runs | OR | ≤ pᵏ |
| One-sided (false positives only) | Pr[false alarm] ≤ p | independent runs | AND | ≤ pᵏ |
| Two-sided | Pr[wrong] ≤ p < 1/2 | independent runs | Majority | ≤ exp(−Ω(k)) |

Amplification is the main “engineering knob” for Monte Carlo algorithms. Next we’ll connect these ideas to real algorithmic uses and how to reason about expected time vs bounded time.

## Application/Connection: How Randomized Algorithms Are Used (and Analyzed)

### Why randomized algorithms show up so often

Randomness is not just a trick—it’s a systematic way to obtain:

- •Simpler algorithms
- •Better average/expected performance
- •Robustness against adversarial patterns

But using randomness responsibly means being precise about what is guaranteed.

### Common application patterns

#### 1) Randomization to avoid worst-case structure (performance)

Example: choosing a pivot randomly in quicksort.

- •Deterministic pivot rules can be forced into Θ(n²) on structured inputs.
- •Random pivots make it extremely unlikely to keep making bad splits.

This yields a Las Vegas algorithm:

- •Always correct sorting
- •Expected time O(n log n)

#### 2) Randomization to avoid collisions/adversaries (data structures)

Example: randomized hashing.

Instead of a fixed hash function that an adversary can exploit, select a hash function at random from a family.

Then performance guarantees are in probability over the choice of hash function (which is effectively r).

This connects to the “distribution over deterministic algorithms” view.

#### 3) Randomization to cheaply estimate/decide (correctness tradeoff)

Example: primality testing.

- •Deterministic primality is possible, but randomized tests are far simpler and fast.
- •You accept a tiny error probability (Monte Carlo), then amplify until it’s astronomically small.

#### 4) Random sampling and sketching (sublinear/streaming)

Many streaming algorithms rely on random sampling to estimate counts, norms, or heavy hitters.

These are often Monte Carlo: they provide approximate answers with high probability.

### How to read claims in papers and implementations

When you see a claim, categorize it:

1. 1)**Expected-time claim**

- •“Runs in expected O(n log n)”
- •Usually Las Vegas (or at least time analysis is in expectation)

2. 2)**High-probability time bound**

- •“Runs in O(n) time with probability ≥ 1 − 1/n²”
- •Still about time; check correctness separately.

3. 3)**Bounded error**

- •“Outputs the correct answer with probability ≥ 0.999”
- •Monte Carlo unless correctness is 1.

A good habit is to explicitly write:

- •Pr\_r[correct] ≥ 1 − δ
- •E\_r[T] ≤ …

This makes it crystal clear what is random and what’s guaranteed.

### Turning one kind into the other (common transformations)

#### Monte Carlo → “almost Las Vegas” by verification

If you can verify an answer efficiently, you can do:

- •Run the Monte Carlo algorithm
- •Verify the output
- •If verification fails, repeat

Then correctness becomes 1, and time becomes random.

This is a standard way to construct Las Vegas algorithms: *random proposal + deterministic check*.

#### Las Vegas → Monte Carlo by timeout

If a Las Vegas algorithm has a heavy tail (rare long runs), you can:

- •Stop after a fixed time limit
- •Output FAIL or a default answer

Now you have bounded time, but a chance of failure/error.

This can be useful in real-time systems.

### A note on randomness sources

In theory, r is perfectly random. In practice:

- •Use pseudorandom generators (PRGs) or standard PRNGs
- •Ensure different runs are seeded differently (for amplification)

Most randomized algorithm analyses assume truly independent bits; engineering approximates that assumption well enough for most applications.

### Where this node connects next

Randomization is a gateway to several deeper topics:

- •Precise tail bounds (Chernoff/Hoeffding) for “with high probability” statements
- •Hash families and universal hashing
- •Probabilistic primality and number theory
- •Randomized data structures (treaps, skip lists)

The core conceptual toolkit you need is:

- •A(x; r)
- •Pr[·] and E[·]
- •Las Vegas vs Monte Carlo
- •Amplification

Once those are solid, the rest is about applying them in specific domains.

## Worked Examples (3)

### Las Vegas Example: Expected Time of Randomized Quicksort (High-Level Derivation)

We sort n distinct numbers using randomized quicksort: pick a pivot uniformly at random from the current subarray, partition, then recurse. The algorithm is always correct, but the runtime depends on pivot choices.

Goal: show the expected number of comparisons is O(n log n).

1. Define the random variable C = total number of element-to-element comparisons performed by quicksort on the input of size n.
2. Key idea: count comparisons by pairs.

   For each pair of elements (i, j) with i < j in sorted order, define an indicator variable:

   Xᵢⱼ = 1 if elements i and j are ever compared, else 0.

   Then:

   C = ∑\_{i<j} Xᵢⱼ
3. Take expectations:

   E[C] = E[ ∑\_{i<j} Xᵢⱼ ]

   = ∑\_{i<j} E[Xᵢⱼ]

   = ∑\_{i<j} Pr[Xᵢⱼ = 1]
4. Compute Pr[Xᵢⱼ = 1].

   In quicksort, i and j are compared iff the first pivot chosen from the set {i, i+1, …, j} is either i or j.

   Because the pivot is chosen uniformly at random among the elements in that set when that subproblem is first formed:

   Pr[Xᵢⱼ = 1] = 2 / (j − i + 1).
5. Plug back in:

   E[C] = ∑\_{i<j} 2 / (j − i + 1)

   Let d = j − i (distance in sorted order), so j − i + 1 = d + 1.

   For each d ∈ {1, …, n−1}, there are (n − d) pairs at distance d.

   So:

   E[C] = ∑\_{d=1}^{n−1} (n − d) · 2/(d + 1)
6. Upper bound it:

   E[C] = 2 · ∑\_{d=1}^{n−1} (n − d)/(d + 1)

   ≤ 2 · ∑\_{d=1}^{n−1} n/(d + 1)

   = 2n · ∑\_{d=1}^{n−1} 1/(d + 1)

   = 2n · ∑\_{k=2}^{n} 1/k
7. Use the harmonic series estimate:

   ∑\_{k=2}^{n} 1/k = O(log n)

   Therefore:

   E[C] = O(n log n).

**Insight:** This is quintessential Las Vegas analysis: correctness is 1, but performance is random. Instead of tracking complex recursion shapes, we used linearity of expectation on carefully chosen indicator variables.

### Monte Carlo Example: Amplifying a 2/3-Correct Algorithm to Error ≤ 2⁻²⁰

Suppose A(x; r) runs in time O(f(n)) and returns a YES/NO answer with two-sided error:

Pr[A is correct] ≥ 2/3.

We want a new algorithm with error probability ≤ 2⁻²⁰, and we want to compute how many repetitions are needed.

1. Let p = Pr[A is wrong] ≤ 1/3 for a single run.
2. Run A independently k times to get outputs Z₁, …, Z\_k.
3. Return the majority vote Z\*.

   Majority is wrong only if at least ⌈k/2⌉ runs are wrong.
4. Let Xᵢ indicate whether run i is wrong.

   Then S = ∑ᵢ Xᵢ is the number of wrong runs.

   We have E[Xᵢ] ≤ 1/3, so E[S] ≤ k/3.
5. We want Pr[S ≥ k/2].

   This is a large deviation above the mean (k/2 is bigger than k/3). Chernoff bounds imply:

   Pr[S ≥ k/2] ≤ exp(−Ω(k)).

   A common concrete form for p = 1/3 yields:

   Pr[majority wrong] ≤ exp(−k/18)

   (you do not need to memorize the constant; the exponential-in-k behavior is the key).
6. Set exp(−k/18) ≤ 2⁻²⁰.

   Take natural logs:

   −k/18 ≤ ln(2⁻²⁰) = −20 ln 2

   ⇒ k/18 ≥ 20 ln 2

   ⇒ k ≥ 360 ln 2
7. Compute 360 ln 2 ≈ 360 · 0.693 ≈ 249.5.

   So k = 250 repetitions suffice under this bound.
8. Total time becomes O(k · f(n)) = O(f(n) · 250), i.e. only a constant-factor slowdown for astronomically small error.

**Insight:** Amplification converts a constant-bias coin (2/3 correct) into an extremely reliable decision procedure. The time cost is linear in repetitions, while error shrinks exponentially—one of the main reasons Monte Carlo algorithms are practical.

### One-Sided Error Example: OR-Amplification from p = 1/4 to δ = 10⁻⁶

Assume a one-sided Monte Carlo algorithm for a YES/NO property:

- •On NO instances: always outputs NO.
- •On YES instances: outputs YES with probability ≥ 3/4 (so miss probability p ≤ 1/4).

We want overall miss probability ≤ δ = 10⁻⁶.

1. Repeat the algorithm independently k times.
2. Output YES if any run outputs YES (OR rule).
3. On NO instances, the algorithm never outputs YES, so the amplified algorithm is still never wrong on NO instances (error = 0 there).
4. On YES instances, error occurs only if all k runs miss:

   Pr[error] ≤ pᵏ = (1/4)ᵏ.
5. Solve (1/4)ᵏ ≤ 10⁻⁶.

   Take logs base 10:

   k · log₁₀(1/4) ≤ −6.

   Since log₁₀(1/4) = −log₁₀(4) ≈ −0.60206:

   −0.60206 k ≤ −6

   ⇒ k ≥ 6 / 0.60206 ≈ 9.966.
6. So k = 10 repetitions suffice.

   Runtime increases by a factor of 10; error drops to ≤ 10⁻⁶.

**Insight:** For one-sided error, amplification is especially clean: independence plus an OR/AND rule gives error pᵏ exactly (or at least ≤ pᵏ). This is often used in randomized algebra and primality testing.

## Key Takeaways

- ✓

  A randomized algorithm is naturally written as A(x; r): random bits r make output and/or runtime into random variables.
- ✓

  All probabilistic statements are taken over the internal randomness: Pr\_r[·].
- ✓

  Las Vegas algorithms: always correct (Pr[correct] = 1) but have randomized running time; analyze E[T] and sometimes tail bounds.
- ✓

  Monte Carlo algorithms: have a fixed (or tightly bounded) runtime but may be wrong with probability δ; analyze Pr[error] ≤ δ.
- ✓

  Monte Carlo error comes in one-sided and two-sided forms; one-sided error often amplifies via simple OR/AND rules.
- ✓

  Amplification: k independent repetitions reduce error exponentially (≈ pᵏ for one-sided; exp(−Ω(k)) for majority vote), while time increases linearly by a factor k.
- ✓

  Independence of repetitions (fresh random bits) is essential—without it, amplification may provide no benefit.
- ✓

  In practice, many algorithms are presented with constant error (like 1/3) because you can tune δ to be as small as needed with O(log(1/δ)) repetitions.

## Common Mistakes

- ✗

  Confusing Las Vegas and Monte Carlo: Las Vegas never returns an incorrect answer; Monte Carlo may, even if the error is tiny.
- ✗

  Assuming amplification works without independence (e.g., reusing the same seed or correlated randomness).
- ✗

  Treating an expected-time bound E[T] ≤ O(f(n)) as if it were a worst-case bound T ≤ O(f(n)) for every run.
- ✗

  Ignoring what the probability is taken over: Pr[·] here is over random bits r, not over a distribution of inputs unless explicitly stated.

## Practice

easy

Classification practice. For each statement, decide whether it describes (i) Las Vegas, (ii) Monte Carlo, or (iii) insufficient information.

A) “Always outputs a correct minimum spanning tree; expected runtime O(m log n).”

B) “Runs in O(n²) time and outputs the correct answer with probability at least 0.99.”

C) “Runs in expected O(n) time and is correct with probability 0.999.”

**Hint:** Las Vegas: correctness is 1. Monte Carlo: runtime is bounded but correctness < 1. If both are probabilistic, you may not have enough to classify cleanly without more detail.

Show solution

A) Las Vegas (correctness is guaranteed; time analyzed in expectation).

B) Monte Carlo (fixed time bound; probabilistic correctness).

C) Insufficient information / mixed: correctness is not guaranteed (so not Las Vegas), and runtime is only in expectation (so not the clean Monte Carlo template). It’s a randomized algorithm with both time and correctness probabilistic unless more structure is given.

medium

One-sided amplification calculation. A one-sided Monte Carlo algorithm has false-negative probability p = 0.1 (it may miss YES instances), and never has false positives. How many independent repetitions k are needed so that the amplified algorithm (OR of runs) has miss probability ≤ 10⁻⁹?

**Hint:** For OR amplification with one-sided error: Pr[miss] ≤ pᵏ. Solve pᵏ ≤ δ using logs.

Show solution

We need (0.1)ᵏ ≤ 10⁻⁹.

Taking log base 10:

k · log₁₀(0.1) ≤ −9.

But log₁₀(0.1) = −1.

So −k ≤ −9 ⇒ k ≥ 9.

Answer: k = 9 repetitions.

hard

Design choice. You have a Monte Carlo algorithm that runs in time O(n) and returns the correct answer with probability 2/3. You need overall error probability ≤ 1/n³.

Assuming independent repetitions and majority vote, give an asymptotic bound on the total runtime after amplification in terms of n.

**Hint:** You want δ = 1/n³. Majority-vote error drops like exp(−Ω(k)), so k = O(log(1/δ)) = O(log n). Multiply by O(n).

Show solution

Target error δ = 1/n³.

We choose k = O(log(1/δ)) repetitions.

Compute:

log(1/δ) = log(n³) = 3 log n = O(log n).

Each run costs O(n), so total time is:

O(n · k) = O(n log n).

(Any constant factors depend on the specific Chernoff bound constants, but asymptotically it is O(n log n).)

## Connections

- •[Expected Value](/tech-tree/expected-value/)
- •[Concentration Inequalities (Chernoff/Hoeffding)](/tech-tree/concentration-inequalities/)
- •[Randomized Quicksort](/tech-tree/randomized-quicksort/)
- •[Hashing and Universal Hash Families](/tech-tree/universal-hashing/)
- •[Miller–Rabin Primality Test](/tech-tree/miller-rabin/)
- •[Skip Lists and Randomized Data Structures](/tech-tree/skip-lists/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
