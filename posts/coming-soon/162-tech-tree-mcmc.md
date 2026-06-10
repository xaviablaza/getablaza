---
title: MCMC
description: Markov Chain Monte Carlo. Sampling from complex distributions.
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
permalink: /tech-tree/mcmc/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# MCMC

Probability & StatisticsDifficulty: ★★★★☆Depth: 8Unlocks: 3

Markov Chain Monte Carlo. Sampling from complex distributions.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Construct a Markov chain whose invariant (stationary) distribution equals the desired target distribution.
- -Ergodicity: long-run empirical averages along a single chain converge to expectations under the target distribution.
- -Proposal-and-correction mechanisms (e.g., Metropolis-Hastings acceptance or Gibbs updates) that modify candidate moves to preserve the target as invariant.

## Key Symbols & Notation

pi(x) - target (possibly unnormalized) density to sample from.K(x -> x') - Markov transition kernel giving the probability or density of moving from state x to state x'.

## Essential Relationships

- -If K has pi as an invariant distribution and the chain is ergodic, then time averages over the chain converge to expectations under pi (Markov chain law of large numbers).

## Prerequisites (3)

[Markov Chains6 atoms](/tech-tree/markov-chains/)[Monte Carlo Methods6 atoms](/tech-tree/monte-carlo/)[Bayesian Inference5 atoms](/tech-tree/bayesian-inference/)

## Unlocks (1)

[Hierarchical Bayesian Modelslvl 5](/tech-tree/hierarchical-models/)

Advanced Learning Details

### Graph Position

142

Depth Cost

3

Fan-Out (ROI)

1

Bottleneck Score

8

Chain Length

### Cognitive Load

6

Atomic Elements

42

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (20)

- - Target distribution π(x) treated as the invariant/stationary distribution of a constructed Markov chain (often known only up to a normalizing constant)
- - Transition kernel/operator for MCMC in continuous or large state spaces (K(x, ·) or P(x → y))
- - Proposal distribution q(x' | x) used to suggest moves in state space
- - Acceptance–rejection mechanism that decides whether to move to a proposed state (Metropolis–Hastings rule)
- - Hastings ratio / acceptance ratio r = [π(x') q(x | x')]/[π(x) q(x' | x)] and acceptance probability α = min(1,r)
- - Detailed balance (reversibility) condition as a practical sufficient condition for π to be stationary
- - Use of unnormalized target density ∴π(x) (i.e., π known up to a constant) because ratios cancel normalization
- - Gibbs sampling: special MCMC where one samples sequentially from full conditional distributions
- - Special MCMC variants: random-walk Metropolis, independence sampler, block-Gibbs, component-wise updates
- - Ergodicity for MCMC: conditions (irreducibility, aperiodicity, positive recurrence) that ensure convergence to π
- - Burn-in (warm-up) period: discarding initial samples before the chain reaches stationarity
- - Mixing: how quickly the chain explores the target distribution (speed of convergence / decorrelation)
- - Autocorrelation in MCMC samples (dependence between successive draws)
- - Integrated autocorrelation time τ\_int as a measure of correlation and its effect on variance of estimators
- - Effective sample size (ESS or N\_eff): number of independent-equivalent samples given autocorrelation
- - Thinning: subsampling the chain to reduce autocorrelation (practical trade-offs)
- - Markov-chain Central Limit Theorem / asymptotic normality of ergodic averages for dependent samples
- - Convergence diagnostics and practical checks (e.g., Gelman–Rubin R-hat, trace plots, autocorrelation plots)
- - Tuning proposals (scale/shape) to balance acceptance rate and exploration; typical heuristic acceptance rates (e.g., ~0.234 for high-dim random-walk)
- - Practical implementation details: initialization strategies, multiple chains, blocking, and parameterization for efficiency

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

In Bayesian inference you often know your posterior only up to a constant: π(x) ∝ prior(x)·likelihood(x). That “missing constant” makes direct sampling and normalization hard—exactly where Markov Chain Monte Carlo (MCMC) shines: it builds a Markov chain that spends time in regions proportional to π(x), so you can estimate expectations with samples that come from a single long run.

TL;DR:

MCMC turns sampling into a dynamical process: design a Markov transition kernel K(x → x′) whose stationary distribution is the target π(x). If the chain is ergodic, averages along the chain converge to expectations under π. Metropolis–Hastings and Gibbs sampling are the two core “proposal-and-correction” mechanisms that guarantee π is invariant while remaining practical for complex, high-dimensional targets.

## What Is MCMC?

### The problem MCMC solves

In many real problems you can *evaluate* a target density but can’t easily:

- •**Normalize it** (compute Z = ∫ π̃(x) dx), or
- •**Sample from it directly**.

A canonical case is Bayesian inference. You want the posterior

π(x) = p(x | data) ∝ p(data | x) p(x)

where the proportionality constant is the evidence Z = p(data).

If your goal is an expectation

Eπ[f(X)] = ∫ f(x) π(x) dx,

then plain Monte Carlo would ask you to draw X₁, …, Xₙ i.i.d. from π. But drawing i.i.d. is often the hard part.

### The key MCMC idea

MCMC replaces i.i.d. samples with a *dependent* sequence

X₀, X₁, X₂, …

generated by a Markov chain with transition kernel K(x → x′). You design K so that:

1. 1)**π is invariant (stationary):** if Xₜ ∼ π, then Xₜ₊₁ ∼ π.
2. 2)**The chain is ergodic:** from almost any start, it eventually forgets its initial state and explores the whole relevant support.

Then you estimate expectations by time averages:

f̄ₙ = (1/n) ∑ₜ₌₁ⁿ f(Xₜ) ≈ Eπ[f(X)].

The tradeoff you accept is dependence: samples are correlated, which reduces effective sample size. The payoff is you can sample from extremely complex π—high-dimensional, constrained, or only known up to a constant.

### Vocabulary: target, kernel, invariance

- •**Target density π(x):** the distribution you want. Often you only know an unnormalized form π̃(x) where π(x) = π̃(x)/Z.
- •**Transition kernel K(x → x′):** gives the probability (discrete) or density (continuous) of moving from x to x′.
- •**Invariance / stationarity:** π is stationary if

π(x′) = ∫ π(x) K(x → x′) dx (continuous)

or π = πK (discrete).

In practice, you rarely verify invariance by solving the stationarity equation directly. Instead, you design K to satisfy a stronger and easier-to-check condition: **detailed balance**.

### Detailed balance (reversibility)

A kernel K satisfies detailed balance with π if for all x, x′:

π(x) K(x → x′) = π(x′) K(x′ → x).

If detailed balance holds and K is a valid Markov kernel, then π is invariant:

∫ π(x) K(x → x′) dx

= ∫ π(x′) K(x′ → x) dx

= π(x′) ∫ K(x′ → x) dx

= π(x′).

That last step uses that K(x′ → ·) integrates to 1.

### What “sampling” means in MCMC

Unlike i.i.d. sampling, MCMC has two phases:

1. 1)**Transient / burn-in:** the chain moves from its initial distribution toward π.
2. 2)**Stationary sampling:** once near stationarity, you treat subsequent states as draws (correlated) from π.

When MCMC works well, you get practical access to:

- •Posterior means, variances, quantiles
- •Credible intervals
- •Predictive distributions via forward simulation from sampled parameters

But MCMC is not “press a button.” You must reason about kernel design, ergodicity, and diagnostics. The rest of this lesson builds those pieces carefully.

## Core Mechanic 1: Invariant Distributions via Proposal-and-Correction (Metropolis–Hastings)

### Why proposal-and-correction exists

Suppose you have a target π(x) that is complicated, but you *can*:

- •evaluate π̃(x) ∝ π(x) (unnormalized), and
- •sample from a simpler **proposal** distribution q(x′ | x).

If you naïvely propose X′ ∼ q(· | x) and always accept it, the chain’s stationary distribution will be whatever q induces—not your π.

Metropolis–Hastings (MH) fixes this by adding an **accept/reject correction** that adjusts for the mismatch between proposal dynamics and target probabilities.

### Metropolis–Hastings algorithm

Given current state x:

1. 1)Propose x′ ∼ q(x′ | x)
2. 2)Accept with probability

α(x, x′) = min\{1, [π(x′) q(x | x′)] / [π(x) q(x′ | x)]\}

3. 3)If accepted, set Xₜ₊₁ = x′; else set Xₜ₊₁ = x.

Important: you can replace π with π̃ because the normalizing constant cancels in the ratio.

### The MH transition kernel and detailed balance

Define the *proposal* kernel q(x′ | x) and acceptance α(x, x′). The MH transition has two parts:

- •Move to x′ ≠ x with density: K(x → x′) = q(x′ | x) α(x, x′)
- •Stay at x with remaining probability: K(x → x) = 1 − ∫ q(u | x) α(x, u) du

Now the crucial property: MH is constructed so that detailed balance holds.

Take x ≠ x′. Then:

π(x) K(x → x′)

= π(x) q(x′ | x) α(x, x′)

and with α defined as the min of 1 and a ratio, you can check that

π(x) q(x′ | x) α(x, x′)

= π(x′) q(x | x′) α(x′, x)

= π(x′) K(x′ → x).

Therefore π is invariant.

### Intuition for the acceptance ratio

The MH ratio compares *how much* the proposed move would distort the target:

r(x, x′) = [π(x′) q(x | x′)] / [π(x) q(x′ | x)].

- •If r ≥ 1, the move is “under-proposed” relative to π, so accept.
- •If r < 1, the move is “over-proposed” relative to π, so accept with probability r.

The q terms matter because if your proposal tends to jump into some region too often, MH corrects by rejecting more there.

### Special case: Random-walk Metropolis

A very common choice is a symmetric proposal:

q(x′ | x) = q(x | x′).

For example, in ℝᵈ:

x′ = x + ε, ε ∼ 𝒩(0, σ²I).

Then the acceptance simplifies:

α(x, x′) = min\{1, π(x′)/π(x)\}.

This is simple and broadly applicable, but it can mix slowly in high dimensions or when π has strong correlations.

### Designing proposals: local vs global moves

Proposal choice is the main engineering degree of freedom in MH.

| Proposal style | Typical q(x′ | x) | Pros | Cons |
| --- | --- | --- | --- | --- |
| Random-walk | x′ = x + ε | Simple; needs only π̃(x) | Can mix slowly; tuning σ is critical |
| Independence | q(x′) independent of x | Can make big jumps | Needs good global approximation to π |
| Langevin / gradient-informed | x′ ≈ x + (step)∇log π(x) + noise | Faster mixing on smooth targets | Requires gradients; careful step-size |

Even without going deep into gradient methods, the lesson is: **MH correctness is easy; MH efficiency is hard.**

### Tuning acceptance rate (practical intuition)

If σ is too small in a random-walk proposal, you accept almost everything but explore slowly (high autocorrelation).

If σ is too large, you propose far-away points with tiny π and reject often (stuck chain).

A good proposal balances movement and acceptance. In many problems, you tune σ so that acceptance is neither near 0 nor near 1.

### What MH guarantees—and what it doesn’t

MH guarantees π is invariant *if* the chain is irreducible and aperiodic on the relevant support.

But MH does not guarantee:

- •fast mixing
- •good exploration of multiple separated modes
- •automatic convergence diagnostics

Those depend on proposal quality and the geometry of π.

## Core Mechanic 2: Ergodicity and Why Time Averages Work

### Why ergodicity matters

MCMC’s promise is:

(1/n) ∑ₜ₌₁ⁿ f(Xₜ) → Eπ[f(X)]

even though Xₜ are dependent.

This is not magic; it’s an ergodic theorem for Markov chains. You already know (from prerequisite Markov chains) that a stationary distribution π satisfies π = πK. Ergodicity strengthens this: the chain not only *has* π, it *converges to* π from broad initial conditions.

### The big picture conditions

Different textbooks phrase conditions differently, but the core ideas are:

1. 1)**Irreducibility:** you can reach any region of the support (at least in principle).
2. 2)**Aperiodicity:** you don’t get trapped in deterministic cycles.
3. 3)**Positive recurrence / stability:** the chain doesn’t wander off to infinity when π is proper.

Under these conditions (plus some technical regularity), the chain has a unique stationary distribution π and converges to it.

### What convergence means (distribution vs averages)

There are two related but distinct statements:

1. 1)**Distributional convergence (mixing):** as t → ∞,

Law(Xₜ) → π.

2. 2)**Ergodic averages:** as n → ∞,

(1/n) ∑ₜ₌₁ⁿ f(Xₜ) → Eπ[f(X)] (almost surely, under conditions).

The second is what you use for Monte Carlo estimates.

### Autocorrelation and effective sample size

Because samples are correlated, variance decays slower than 1/n.

Let μ = Eπ[f(X)] and consider the estimator f̄ₙ.

Under standard conditions, a Markov chain CLT gives:

√n (f̄ₙ − μ) ⇒ 𝒩(0, σ²\_f),

where

σ²\_f = Varπ(f(X₀)) + 2 ∑\_{k=1}^∞ Covπ(f(X₀), f(X\_k)).

Define the integrated autocorrelation time:

τ\_int = 1 + 2 ∑\_{k=1}^∞ ρ\_k,

where ρ\_k are autocorrelations. Then roughly:

Var(f̄ₙ) ≈ (Varπ(f)/n) · τ\_int.

This motivates an **effective sample size**:

n\_eff ≈ n / τ\_int.

So MCMC accuracy depends not just on n, but on how quickly the chain forgets (how fast ρ\_k decays).

### Burn-in: when and why

If you start at X₀ far from typical regions of π, early samples are biased toward the initial state. The usual operational fix is to discard the first B iterations.

Conceptually:

- •Burn-in reduces initialization bias.
- •It does not fix poor mixing.

If the chain moves slowly, discarding more samples doesn’t create independence; it just wastes computation.

### Thinning: usually not necessary

Thinning keeps every m-th sample. People do it to “reduce correlation,” but correlation is not removed; you just throw away information.

Thinning can be useful when:

- •storage is expensive
- •evaluating f(x) is cheap but storing x is not

Otherwise, keeping all samples and estimating τ\_int is generally better.

### Diagnostics (the practical side of ergodicity)

Ergodicity is a theorem, but you still need to *check behavior*.

Common checks:

- •**Trace plots:** does the chain move around or stick?
- •**Multiple chains:** do different starts converge to similar regions?
- •**Autocorrelation plots:** does dependence decay quickly?
- •**R̂ (Gelman–Rubin):** compares within-chain vs between-chain variability.

None of these is a proof of convergence, but they catch many failures.

### A warning about multimodality

If π has widely separated modes, a random-walk MH chain may be ergodic in theory but practically non-mixing on feasible timescales.

In such cases you may need:

- •better proposals (tempered transitions, HMC, split-merge moves)
- •reparameterizations
- •parallel tempering

The lesson here: **ergodicity is about infinite time; efficiency is about the time you can afford.**

## Core Mechanic 3: Gibbs Sampling (Conditionals as Perfect Local Moves)

### Why Gibbs exists

Metropolis–Hastings is general but needs a good proposal q(x′ | x). Sometimes you don’t have a good global proposal, but you *do* know and can sample from conditional distributions.

Gibbs sampling exploits a simple idea:

> If you can sample exactly from the conditional of one variable given the others, you can construct a Markov chain that leaves the joint target π invariant.

This is especially common in Bayesian models with conjugacy.

### Setup: a multivariate target

Let x = (x₁, …, x\_d) and target π(x₁, …, x\_d). Suppose you can sample from each full conditional:

π(x\_i | x\_{−i})

where x\_{−i} denotes all coordinates except i.

### Gibbs update rule

A single-site Gibbs step updates one coordinate at a time:

For i = 1, …, d:

x\_i ← draw from π(x\_i | x\_{−i}).

After sweeping through all coordinates, you have one full Gibbs iteration.

### Why Gibbs leaves π invariant (intuition + structure)

Each conditional update is a Markov kernel K\_i that replaces x\_i while leaving the others fixed.

If you start with X ∼ π, and then resample X\_i from π(x\_i | X\_{−i}), the resulting joint distribution is still π.

One way to see this is that π factors as:

π(x) = π(x\_i | x\_{−i}) π(x\_{−i}).

So if x\_{−i} is distributed as π(x\_{−i}) and you sample x\_i from the correct conditional, you reconstruct the correct joint.

Composing kernels K = K\_d ∘ … ∘ K\_1 preserves invariance.

### Gibbs as MH with acceptance = 1

A useful connection: Gibbs is a special case of MH.

If you propose x′ that differs from x only in coordinate i, with proposal density

q(x′ | x) = π(x′\_i | x\_{−i})

then the MH acceptance ratio becomes 1, because the proposal already matches the target’s conditional structure.

So Gibbs is “perfectly corrected” by construction.

### Block Gibbs

Sometimes coordinates are strongly coupled; single-site updates mix slowly.

Block Gibbs updates a subset (a block) **b** at once:

x\_b ← draw from π(x\_b | x\_{−b}).

When you can sample the block conditional, this can greatly reduce autocorrelation.

### When Gibbs is hard

Gibbs requires the ability to sample from conditionals. When conditionals are not standard distributions, you may combine:

- •Gibbs for some variables
- •MH-within-Gibbs for others (use MH to sample a conditional approximately)

This hybrid is extremely common in applied Bayesian computation.

### Practical comparison: MH vs Gibbs

| Aspect | Metropolis–Hastings | Gibbs |
| --- | --- | --- |
| Requires | unnormalized π̃(x) and a proposal q | ability to sample from conditionals |
| Accept/reject | yes | no (acceptance = 1) |
| Tuning | proposal scale/shape | block structure/order |
| Weakness | can reject often | can mix slowly with strong correlations |

The important mental model: **MH is about proposing then correcting; Gibbs is about choosing proposals that need no correction.**

## Application/Connection: MCMC for Bayesian Posterior Estimation (and How to Use Samples)

### Why MCMC is central in Bayesian inference

Bayesian workflows often reduce to computing expectations under the posterior:

- •Posterior mean: E[θ | data]
- •Posterior variance: Var(θ | data)
- •Credible intervals: quantiles of θ | data
- •Posterior predictive: p(y\_new | data) = ∫ p(y\_new | θ) p(θ | data) dθ

If you have samples θ¹, …, θⁿ ∼ (approximately) p(θ | data), then:

- •E[g(θ) | data] ≈ (1/n) ∑ g(θᵗ)
- •Posterior predictive: draw y\_newᵗ ∼ p(y\_new | θᵗ)

MCMC turns integrals into averages.

### A standard workflow

1. 1)**Model specification**

- •Prior p(θ)
- •Likelihood p(data | θ)
- •Posterior π(θ) ∝ p(data | θ)p(θ)

2. 2)**Choose an MCMC kernel**

- •Random-walk MH
- •Gibbs / block Gibbs
- •MH-within-Gibbs

3. 3)**Run multiple chains**

- •Different starting points
- •Enough iterations to assess stability

4. 4)**Check diagnostics**

- •Trace plots, autocorrelation
- •R̂, effective sample size n\_eff

5. 5)**Compute posterior summaries**

- •Means, intervals, posterior predictive

### How to estimate uncertainty of estimates

Because samples are correlated, you should not use i.i.d. standard errors blindly.

Two common approaches:

- •**Batch means:** split the chain into B batches, average within each batch, treat batch means as approximately independent.
- •**Markov chain variance estimators:** estimate τ\_int and use Var(f̄ₙ) ≈ Varπ(f) τ\_int / n.

### Constraints, discrete variables, and complex supports

MCMC is flexible about support constraints.

- •If θ must be positive, you can reparameterize (e.g., φ = log θ) and sample φ ∈ ℝ.
- •For discrete latent variables, Gibbs updates can be exact and efficient.
- •For constrained vectors **v** on a simplex (probabilities that sum to 1), use specialized proposals or reparameterizations.

The key is always the same: define a kernel K that doesn’t leave the support and keeps π invariant.

### A geometric intuition (why reparameterization matters)

If π(θ) has strong correlations, a random-walk proposal in the raw coordinates can be inefficient.

Example: suppose (θ₁, θ₂) posterior mass lies near a tilted ellipse. Proposing independent Gaussian noise in each coordinate moves you orthogonally to the ridge often, causing rejections or slow diffusion.

A reparameterization that “whitens” the posterior (makes it closer to spherical) can drastically reduce τ\_int.

### What this node unlocks

Once you internalize (1) invariance via detailed balance and (2) ergodicity for time averages, you’re ready for:

- •Hamiltonian Monte Carlo (HMC): gradient-informed proposals for continuous targets
- •Variational inference as an optimization alternative (contrasting approximation vs asymptotic exactness)
- •Advanced MCMC: adaptive MH, slice sampling, parallel tempering

But even at this level, you can already implement correct samplers for many Bayesian models and reason about when they will (or won’t) work.

## Worked Examples (3)

### Metropolis–Hastings on a 1D Unnormalized Target (acceptance uses only ratios)

Target on ℝ: π(x) ∝ π̃(x) where π̃(x) = exp(−x⁴ + 2x²). This is not trivial to normalize, but we can evaluate π̃(x) pointwise.

Use a symmetric random-walk proposal: x′ = x + ε, ε ∼ 𝒩(0, σ²).

1. Because the proposal is symmetric, q(x′|x) = q(x|x′), so the MH acceptance probability simplifies:

   α(x, x′) = min{1, π(x′)/π(x)} = min{1, π̃(x′)/π̃(x)}.
2. Compute the unnormalized log density (for numerical stability):

   log π̃(x) = −x⁴ + 2x².
3. Given current x and proposal x′, form the log acceptance ratio:

   log r = log π̃(x′) − log π̃(x)

   = [−(x′)⁴ + 2(x′)²] − [−x⁴ + 2x²].
4. Convert back to an acceptance probability:

   r = exp(log r),

   α = min{1, r}.
5. Decision rule:

   - •Draw u ∼ Uniform(0, 1).
   - •If u ≤ α, accept (next state is x′).
   - •Else reject (next state stays x).
6. Key observation: the normalizing constant Z = ∫ π̃(x) dx never appears. Any π(x) = π̃(x)/Z gives the same acceptance ratio because Z cancels:

   π(x′)/π(x) = [π̃(x′)/Z] / [π̃(x)/Z] = π̃(x′)/π̃(x).

**Insight:** Metropolis–Hastings converts “I can evaluate π̃(x) up to a constant” into “I can sample from π.” The entire correction happens through local ratios, so unknown normalization is not a blocker.

### Deriving the MH Acceptance Ratio from Detailed Balance

You have a proposal kernel q(x′|x). You want to construct a corrected kernel K(x→x′) = q(x′|x)α(x,x′) (for x′≠x) such that detailed balance holds with π.

1. Start from the desired detailed balance condition for x′ ≠ x:

   π(x) q(x′|x) α(x,x′) = π(x′) q(x|x′) α(x′,x).
2. Rearrange to relate α(x,x′) and α(x′,x):

   α(x,x′) / α(x′,x) = [π(x′) q(x|x′)] / [π(x) q(x′|x)] = r(x,x′).
3. We need a choice of α that:

   - •stays in [0,1]
   - •satisfies the ratio constraint above.
4. A standard symmetric construction is:

   α(x,x′) = min{1, r(x,x′)}

   α(x′,x) = min{1, 1/r(x,x′)}.
5. Check the ratio in two cases.

   Case 1: r ≥ 1.

   Then α(x,x′) = 1 and α(x′,x) = 1/r.

   So α(x,x′)/α(x′,x) = 1 / (1/r) = r.

   Case 2: r < 1.

   Then α(x,x′) = r and α(x′,x) = 1.

   So α(x,x′)/α(x′,x) = r / 1 = r.
6. Thus detailed balance holds for x′ ≠ x. Then π is invariant for the full kernel once we include the self-loop probability (the probability of rejecting and staying at x).

**Insight:** The MH acceptance rule is not arbitrary; it is engineered to satisfy detailed balance while keeping α inside [0,1]. This is the simplest general-purpose way to preserve π as invariant.

### Gibbs Sampling in a 2D Gaussian: Conditionals are Gaussian

Let **x** = (x₁, x₂) have a bivariate normal target:

**x** ∼ 𝒩(**0**, Σ), where Σ = [[1, ρ],[ρ, 1]] with |ρ| < 1.

We will derive the full conditionals π(x₁|x₂) and π(x₂|x₁) and describe a Gibbs sampler.

1. For a bivariate normal, the conditional distribution is normal. Specifically:

   x₁ | x₂ ∼ 𝒩( E[x₁|x₂], Var(x₁|x₂) ).
2. Compute conditional mean and variance using standard Gaussian conditioning:

   E[x₁|x₂] = ρ x₂,

   Var(x₁|x₂) = 1 − ρ².

   Similarly:

   E[x₂|x₁] = ρ x₁,

   Var(x₂|x₁) = 1 − ρ².
3. A single Gibbs iteration (a sweep) is:

   1) Sample x₁^{new} ∼ 𝒩(ρ x₂^{old}, 1 − ρ²)

   2) Sample x₂^{new} ∼ 𝒩(ρ x₁^{new}, 1 − ρ²)
4. No accept/reject step is needed: each update draws exactly from the correct conditional.
5. Mixing intuition:

   If |ρ| is close to 1, then 1 − ρ² is small, so each conditional draw is tightly concentrated around ρ times the other variable.

   That makes successive samples highly correlated (slow exploration along the thin ellipse), even though every step is accepted.

**Insight:** Gibbs can be “perfectly accepted” yet still mix slowly when variables are strongly coupled. Correctness (invariance) is separate from efficiency (autocorrelation).

## Key Takeaways

- ✓

  MCMC builds a Markov chain with transition kernel K(x → x′) whose stationary distribution is the target π(x).
- ✓

  Detailed balance, π(x)K(x→x′) = π(x′)K(x′→x), is a convenient sufficient condition for π to be invariant.
- ✓

  Metropolis–Hastings uses a proposal q(x′|x) plus acceptance α(x,x′) = min{1, [π(x′)q(x|x′)]/[π(x)q(x′|x)]} to enforce invariance—even when π is only known up to a constant.
- ✓

  Ergodicity (irreducibility + aperiodicity + stability) is what justifies replacing Eπ[f(X)] with a time average along one long chain.
- ✓

  Correlation reduces information: n samples from MCMC behave like n\_eff ≈ n/τ\_int independent samples, where τ\_int depends on autocorrelation.
- ✓

  Gibbs sampling updates coordinates (or blocks) by drawing from exact conditionals π(x\_i | x\_{−i}); it is MH with acceptance probability 1.
- ✓

  Burn-in addresses initialization bias; it does not fix slow mixing. Thinning usually wastes samples unless constrained by storage or computation.

## Common Mistakes

- ✗

  Assuming a high acceptance rate means good sampling: tiny random-walk steps can accept often but explore very slowly (high autocorrelation).
- ✗

  Forgetting support constraints (e.g., proposing negative values for a positive parameter) which can silently cause near-zero acceptance or invalid evaluations of π̃(x).
- ✗

  Relying on a single chain and no diagnostics: trace plots, multiple initializations, and n\_eff/R̂ are basic checks against non-convergence and multimodal trapping.
- ✗

  Discarding huge burn-in or heavy thinning as a substitute for fixing a poor proposal or bad parameterization.

## Practice

easy

You use Metropolis–Hastings with an independence proposal q(x′) (does not depend on x). Write the acceptance probability α(x,x′). Then simplify it as much as possible.

**Hint:** Start from α(x,x′) = min{1, [π(x′) q(x|x′)]/[π(x) q(x′|x)]}. For independence proposals, q(x′|x)=q(x′) and q(x|x′)=q(x).

Show solution

With independence proposal:

q(x′|x) = q(x′), and q(x|x′) = q(x).

So

α(x,x′) = min{1, [π(x′) q(x)] / [π(x) q(x′)]}.

This form highlights that you accept moves toward regions where π/q is larger.

medium

Suppose you run an MCMC chain and want to estimate μ = Eπ[f(X)]. You compute the empirical mean f̄ₙ. Explain (in 2–4 sentences) why Var(f̄ₙ) is larger than Varπ(f)/n, and name one method to estimate uncertainty correctly.

**Hint:** Think about autocorrelation: Cov(f(X₀), f(X\_k)) terms appear in the variance of the sample mean.

Show solution

Because MCMC samples are correlated, the variance of the average includes lagged covariances:

Var(f̄ₙ) ≈ (Varπ(f)/n) · τ\_int where τ\_int = 1 + 2∑\_{k≥1} ρ\_k.

So the estimator behaves like it had only n\_eff ≈ n/τ\_int independent samples.

One correct uncertainty method is batch means (split the chain into batches and use variability of batch averages), or estimating τ\_int directly and scaling Varπ(f)/n.

hard

Consider a two-variable target π(x₁, x₂). You can sample from π(x₁ | x₂) exactly, but π(x₂ | x₁) is not available in closed form. Propose a valid MCMC scheme that still leaves π invariant.

**Hint:** Mix Gibbs where you can with MH where you can’t: MH-within-Gibbs.

Show solution

Use a hybrid MH-within-Gibbs sampler:

1) Update x₁ by Gibbs: sample x₁′ ∼ π(x₁ | x₂) and set x₁ ← x₁′.

2) Update x₂ by an MH step targeting the conditional π(x₂ | x₁):

- •Propose x₂′ ∼ q(x₂′ | x₂, x₁)
- •Accept with probability

α = min{1, [π(x₁, x₂′) q(x₂ | x₂′, x₁)] / [π(x₁, x₂) q(x₂′ | x₂, x₁)] }

(equivalently using the conditional since x₁ is fixed).

Composing a Gibbs kernel (invariant) with an MH kernel (invariant) yields an overall kernel that preserves π.

## Connections

[Markov Chains](/tech-tree/markov-chains/)

[Monte Carlo Methods](/tech-tree/monte-carlo/)

[Bayesian Inference](/tech-tree/bayesian-inference/)

[Detailed Balance & Reversibility](/tech-tree/detailed-balance/)

[Gibbs Sampling](/tech-tree/gibbs-sampling/)

[Hamiltonian Monte Carlo (HMC)](/tech-tree/hmc/)

[Variational Inference](/tech-tree/variational-inference/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
