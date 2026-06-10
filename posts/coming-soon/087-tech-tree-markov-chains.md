---
title: Markov Chains
description: Memoryless stochastic processes. Transition matrices, stationary distributions.
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
permalink: /tech-tree/markov-chains/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Markov Chains

Probability & StatisticsDifficulty: ★★★★☆Depth: 5Unlocks: 12

Memoryless stochastic processes. Transition matrices, stationary distributions.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Markov property: memoryless process - next state depends only on current state, not the prior history
- -Transition matrix (stochastic matrix) for finite-state chains: matrix of nonnegative transition probabilities with each row summing to 1

## Key Symbols & Notation

P (transition probability matrix): entry P[i,j] = Pr(next state = j | current state = i)pi (stationary distribution vector): row vector of state probabilities summing to 1 that may be invariant

## Essential Relationships

- -Distribution evolution: if mu\_t is the row vector distribution at time t then mu\_{t+1} = mu\_t P
- -Stationary/invariance condition: pi is stationary iff pi = pi P (pi is a left eigenvector of P with eigenvalue 1 and sums to 1)

## Prerequisites (3)

[Conditional Probability6 atoms](/tech-tree/conditional-probability/)[Matrix Operations6 atoms](/tech-tree/matrix-operations/)[Eigenvalues and Eigenvectors6 atoms](/tech-tree/eigenvalues/)

## Unlocks (6)

[Reinforcement Learning Introductionlvl 4](/tech-tree/rl-intro/)[Markov Decision Processeslvl 5](/tech-tree/mdp/)[MCMClvl 4](/tech-tree/mcmc/)[State-Space Modelslvl 4](/tech-tree/state-space-models/)[Concentration Inequalitieslvl 5](/tech-tree/concentration-inequalities/)[Stochastic Processeslvl 4](/tech-tree/stochastic-processes/)

## Referenced by (3)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (3)

[Pipeline VolumeBusiness

Pipeline stages (prospect → qualified → proposal → closed) are naturally modeled as Markov chains with stage-to-stage transition probabilities driving volume forecasts](/business/pipeline-volume/)[Expansion RevenueBusiness

Customer expansion modeled as state transitions (free → basic → pro → enterprise) with transition probabilities governing upgrade rates - a direct Markov chain application for forecasting expansion revenue](/business/expansion-revenue/)[Value MigrationBusiness

Value migrating between industries, companies, and business models is naturally modeled as state transitions with estimated transition probabilities - backtesting the protocol means estimating these transition matrices from historical data](/business/value-migration/)

Advanced Learning Details

### Graph Position

70

Depth Cost

12

Fan-Out (ROI)

5

Bottleneck Score

5

Chain Length

### Cognitive Load

6

Atomic Elements

56

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (25)

- - Markov property (memoryless property): future state depends only on current state, not full history
- - Discrete-time stochastic process notation X\_n (state at time n)
- - State space S (finite or countable set of possible states)
- - One-step transition probability P\_{ij} = P(X\_{n+1}=j | X\_n=i)
- - Transition matrix P (stochastic matrix whose entries are one-step transition probabilities)
- - Stochastic matrix properties: nonnegative entries and rows sum to 1 (or columns depending on convention)
- - Time-homogeneous vs time-inhomogeneous Markov chains (whether transition probabilities depend on n)
- - n-step transition probabilities and the idea of multiple-step transitions
- - Powers of the transition matrix P^n as the n-step transition matrix
- - Initial distribution (probability vector over states at time 0)
- - Evolution of the distribution over time under a Markov chain
- - Chapman–Kolmogorov equations (composition law for multi-step transitions)
- - Stationary distribution (probability vector invariant under the transition matrix)
- - Limiting distribution / long-run distribution (limit of state distribution as n→∞ when it exists)
- - Reversibility and the detailed balance condition
- - Communicating states and communicating classes (reachability equivalence relation)
- - Irreducibility (single communicating class covering the state space)
- - Periodicity (period of a state based on return-time gcd) and aperiodicity
- - Recurrence vs transience (whether a state is returned to with probability 1 or <1)
- - Absorbing states and absorbing classes (states that, once entered, cannot be left)
- - Ergodicity (informal: conditions guaranteeing convergence to a unique long-run distribution)
- - Hitting (first-passage) probabilities and hitting times
- - Expected return time / mean recurrence time
- - Decomposition of state space into transient and recurrent (ergodic) classes
- - Normalization and probability constraints on distributions (nonnegativity and sum-to-1 in this stochastic context)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Many real systems are complicated—but their *state updates* can be simple: “given where I am now, what’s the probability of where I go next?” Markov chains are the mathematical language for that idea, and they power everything from PageRank to MCMC sampling to reinforcement learning.

TL;DR:

A (time-homogeneous) Markov chain is a stochastic process where the next state depends only on the current state. For finite states, its behavior is encoded by a transition matrix P with nonnegative entries and rows summing to 1. Distributions evolve as πₜ₊₁ = πₜ P. A stationary distribution π satisfies π = πP (a left eigenvector with eigenvalue 1). Structure (communicating classes, irreducibility, periodicity) determines long-run behavior and whether πₜ converges to π.

## What Is a Markov Chain?

### Why this concept exists

Many processes evolve step-by-step with randomness: a web surfer clicks links, a customer moves between product categories, a queue length changes, a robot localizes itself, a sampler proposes a new value. In all these, you often don’t want to model the entire history—because the history is huge.

A Markov chain is the idea that **the present is enough**. If you know the current state, the past doesn’t add extra predictive power for the next step.

### Definition (Markov property)

Let {X₀, X₁, X₂, …} be a sequence of random variables taking values in a finite set of states S = {1, 2, …, n}. It is a (time-homogeneous) **Markov chain** if, for all times t and states i₀, …, iₜ, j,

Pr⁡(Xt+1=j∣Xt=it,Xt−1=it−1,…,X0=i0)=Pr⁡(Xt+1=j∣Xt=it).\Pr(X\_{t+1}=j \mid X\_t=i\_t, X\_{t-1}=i\_{t-1},\dots,X\_0=i\_0)
= \Pr(X\_{t+1}=j \mid X\_t=i\_t).Pr(Xt+1​=j∣Xt​=it​,Xt−1​=it−1​,…,X0​=i0​)=Pr(Xt+1​=j∣Xt​=it​).

This is the **Markov property**: the future depends on the past only through the present.

Time-homogeneous means the transition rule does not change with time:

Pr⁡(Xt+1=j∣Xt=i)=P[i,j](same for all t).\Pr(X\_{t+1}=j \mid X\_t=i) = P[i,j] \quad \text{(same for all } t\text{)}.Pr(Xt+1​=j∣Xt​=i)=P[i,j](same for all t).

### The transition matrix P

For a finite-state chain, we store the dynamics in a matrix P (often called a **stochastic matrix**):

- •P[i,j] ≥ 0
- •Each row sums to 1: ∑ⱼ P[i,j] = 1

Interpretation: if you are currently in state i, the i-th row of P is the probability distribution over the next state.

### State distribution as a vector

Let πₜ be the row vector of state probabilities at time t:

- •πₜ[j] = Pr(Xₜ = j)
- •πₜ has nonnegative entries and sums to 1

Then the evolution is a clean matrix rule:

πt+1=πtP.\pi\_{t+1} = \pi\_t P.πt+1​=πt​P.

This is one of the most important “mechanics” of Markov chains: **random evolution becomes linear algebra**.

### A tiny example (feel the meaning)

Suppose S = {Rainy, Sunny} with

- •If Rainy today: Rainy tomorrow with prob 0.7, Sunny with prob 0.3
- •If Sunny today: Rainy tomorrow with prob 0.4, Sunny with prob 0.6

Using the state order (Rainy=1, Sunny=2):

P=[0.70.30.40.6].P = \begin{bmatrix}
0.7 & 0.3 \\
0.4 & 0.6
\end{bmatrix}.P=[0.70.4​0.30.6​].

If today’s distribution is π₀ = [1, 0] (certainly Rainy), then

π1=π0P=[1,0][0.70.30.40.6]=[0.7,0.3].\pi\_1 = \pi\_0 P = [1,0]\begin{bmatrix}0.7&0.3\\0.4&0.6\end{bmatrix} = [0.7, 0.3].π1​=π0​P=[1,0][0.70.4​0.30.6​]=[0.7,0.3].

You should read that as: “tomorrow is 70% Rainy, 30% Sunny.”

### Two viewpoints (state vs. distribution)

You can think about a chain in two complementary ways:

| Viewpoint | Object | Update rule | Interpretation |
| --- | --- | --- | --- |
| Single trajectory | X₀ → X₁ → X₂ → … | sample using P | one random run of the system |
| Distribution over states | π₀, π₁, π₂, … | πₜ₊₁ = πₜP | how probabilities flow over time |

In machine learning and statistics, the distribution view is often the one that connects directly to convergence, stationarity, and sampling.

### Embedded diagram (state graph)

To make the matrix less abstract, here’s the same chain as a directed graph:

```
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="220" viewBox="0 0 720 220">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L10,3 L0,6 Z" fill="#333" />
    </marker>
  </defs>
  <rect x="0" y="0" width="720" height="220" fill="white"/>
  <circle cx="200" cy="110" r="48" fill="#f4f7ff" stroke="#2b4cff" stroke-width="2"/>
  <text x="200" y="116" text-anchor="middle" font-family="Arial" font-size="16">Rainy (1)</text>
  <circle cx="520" cy="110" r="48" fill="#fff7f0" stroke="#ff7a00" stroke-width="2"/>
  <text x="520" y="116" text-anchor="middle" font-family="Arial" font-size="16">Sunny (2)</text>

  <!-- self loops -->
  <path d="M170,80 C140,40 210,35 225,75" fill="none" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="170" y="42" font-family="Arial" font-size="14">0.7</text>

  <path d="M490,80 C460,40 530,35 545,75" fill="none" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="490" y="42" font-family="Arial" font-size="14">0.6</text>

  <!-- cross edges -->
  <path d="M248,110 C310,70 410,70 472,110" fill="none" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="360" y="78" font-family="Arial" font-size="14">0.3</text>

  <path d="M472,120 C410,160 310,160 248,120" fill="none" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="360" y="172" font-family="Arial" font-size="14">0.4</text>

  <text x="360" y="205" text-anchor="middle" font-family="Arial" font-size="13" fill="#444">
    Diagram: directed edges labeled by transition probabilities P[i,j]
  </text>
</svg>
```

Keep this picture in mind: most structural ideas (reachability, recurrence, period) are statements about paths and cycles in this graph.

## Core Mechanic 1: Evolving Distributions with P (and Why Pᵏ Matters)

### Why distributions matter

A single trajectory is noisy: you might see Rainy→Sunny→Sunny even if long-run Sunny is rare (or common). The distribution πₜ is the “average behavior over many parallel universes,” and it’s what we typically analyze.

### One-step update: πₜ₊₁ = πₜP

Suppose πₜ is a row vector. Then

πt+1[j]=∑iπt[i]  P[i,j].\pi\_{t+1}[j] = \sum\_i \pi\_t[i] \; P[i,j].πt+1​[j]=i∑​πt​[i]P[i,j].

This is just the law of total probability:

- •with probability πₜ[i] you are in i at time t,
- •then you jump to j with probability P[i,j],
- •sum over i.

### Multi-step transitions: Pᵏ

If one step is P, then two steps is P², and in general k steps is Pᵏ:

πt+k=πtPk.\pi\_{t+k} = \pi\_t P^k.πt+k​=πt​Pk.

The entries of Pᵏ have a direct probabilistic meaning:

Pk[i,j]=Pr⁡(Xt+k=j∣Xt=i).P^k[i,j] = \Pr(X\_{t+k}=j \mid X\_t=i).Pk[i,j]=Pr(Xt+k​=j∣Xt​=i).

#### Show your work (why P² works)

Start from the definition:

P2[i,j]=∑mP[i,m]P[m,j].P^2[i,j] = \sum\_{m} P[i,m]P[m,j].P2[i,j]=m∑​P[i,m]P[m,j].

Interpretation:

- •go from i to an intermediate state m in one step, then
- •from m to j in one more step,
- •sum over all possible intermediates.

This is again the law of total probability, but now “conditioning on the middle state.”

### The distribution flow picture (embedded diagram)

The matrix rule can feel symbolic, so here is an explicit visualization of **probability mass moving**.

We use the Rainy/Sunny chain above. Start at π₀ = [1, 0] (certainly Rainy). Compute a few steps:

- •π₁ = [1,0]P = [0.7, 0.3]
- •π₂ = π₁P = [0.7,0.3]P

π2[Rainy]=0.7⋅0.7+0.3⋅0.4=0.49+0.12=0.61\pi\_2[\text{Rainy}] = 0.7\cdot 0.7 + 0.3\cdot 0.4 = 0.49 + 0.12 = 0.61π2​[Rainy]=0.7⋅0.7+0.3⋅0.4=0.49+0.12=0.61

π2[Sunny]=0.7⋅0.3+0.3⋅0.6=0.21+0.18=0.39\pi\_2[\text{Sunny}] = 0.7\cdot 0.3 + 0.3\cdot 0.6 = 0.21 + 0.18 = 0.39π2​[Sunny]=0.7⋅0.3+0.3⋅0.6=0.21+0.18=0.39

- •π₃ = [0.61,0.39]P

π3[Rainy]=0.61⋅0.7+0.39⋅0.4=0.427+0.156=0.583\pi\_3[\text{Rainy}] = 0.61\cdot 0.7 + 0.39\cdot 0.4 = 0.427 + 0.156 = 0.583π3​[Rainy]=0.61⋅0.7+0.39⋅0.4=0.427+0.156=0.583

π3[Sunny]=1−0.583=0.417\pi\_3[\text{Sunny}] = 1 - 0.583 = 0.417π3​[Sunny]=1−0.583=0.417

You can see it drifting.

Here’s a diagram that shows the distribution bars evolving (each bar height is probability):

```
<svg xmlns="http://www.w3.org/2000/svg" width="760" height="260" viewBox="0 0 760 260">
  <rect x="0" y="0" width="760" height="260" fill="white"/>
  <text x="20" y="28" font-family="Arial" font-size="14" fill="#222">Distribution evolution πₜ for Rainy/Sunny chain (starting at Rainy)</text>

  <!-- axes baseline -->
  <line x1="60" y1="220" x2="740" y2="220" stroke="#aaa" stroke-width="1"/>

  <!-- function to draw bar groups manually -->
  <!-- group labels -->
  <text x="90" y="245" font-family="Arial" font-size="12">t=0</text>
  <text x="210" y="245" font-family="Arial" font-size="12">t=1</text>
  <text x="330" y="245" font-family="Arial" font-size="12">t=2</text>
  <text x="450" y="245" font-family="Arial" font-size="12">t=3</text>
  <text x="570" y="245" font-family="Arial" font-size="12">t=4</text>

  <!-- bars: Rainy in blue, Sunny in orange. scale: 180px max -->
  <!-- t=0: [1.00,0.00] -->
  <rect x="70" y="40" width="35" height="180" fill="#2b4cff" opacity="0.8"/>
  <rect x="110" y="220" width="35" height="0" fill="#ff7a00" opacity="0.8"/>

  <!-- t=1: [0.70,0.30] -->
  <rect x="190" y="94" width="35" height="126" fill="#2b4cff" opacity="0.8"/>
  <rect x="230" y="166" width="35" height="54" fill="#ff7a00" opacity="0.8"/>

  <!-- t=2: [0.61,0.39] -->
  <rect x="310" y="110.2" width="35" height="109.8" fill="#2b4cff" opacity="0.8"/>
  <rect x="350" y="149.8" width="35" height="70.2" fill="#ff7a00" opacity="0.8"/>

  <!-- t=3: [0.583,0.417] -->
  <rect x="430" y="115.06" width="35" height="104.94" fill="#2b4cff" opacity="0.8"/>
  <rect x="470" y="144.94" width="35" height="75.06" fill="#ff7a00" opacity="0.8"/>

  <!-- t=4 computed quickly: π4 = π3 P => Rainy = 0.583*0.7 + 0.417*0.4 = 0.4081 + 0.1668 = 0.5749 -->
  <rect x="550" y="116.518" width="35" height="103.482" fill="#2b4cff" opacity="0.8"/>
  <rect x="590" y="145.518" width="35" height="74.482" fill="#ff7a00" opacity="0.8"/>

  <!-- legend -->
  <rect x="640" y="50" width="14" height="14" fill="#2b4cff" opacity="0.8"/>
  <text x="660" y="62" font-family="Arial" font-size="12">Rainy</text>
  <rect x="640" y="72" width="14" height="14" fill="#ff7a00" opacity="0.8"/>
  <text x="660" y="84" font-family="Arial" font-size="12">Sunny</text>

  <text x="380" y="18" text-anchor="middle" font-family="Arial" font-size="12" fill="#444">Diagram: bars show πₜ; repeated multiplication by P shifts mass toward a limiting mix</text>
</svg>
```

When you later learn convergence theorems, this picture is what “converges” means: the bars stabilize.

### Orientation matters: row vs column conventions

Be careful: some textbooks use column vectors and write **p**ₜ₊₁ = Pᵀ **p**ₜ. In this lesson we use **row vectors** πₜ and πₜ₊₁ = πₜP.

A quick consistency check:

- •Rows of P sum to 1 (row-stochastic)
- •Multiplying on the right preserves total probability: if πₜ sums to 1, then so does πₜP.

### The stationary distribution as an “equilibrium” of flow

A distribution π is stationary if evolving one step doesn’t change it:

π=πP.\pi = \pi P.π=πP.

This is a fixed point of the linear map “multiply by P.” Interpreted as flow: the probability leaving each state equals probability entering it (in aggregate, under π).

This equation is also an eigenvector equation: π is a **left eigenvector** of P with eigenvalue 1.

### Existence: why eigenvalue 1 shows up at all

For any row-stochastic matrix P:

- •1 is always an eigenvalue (for the transpose, the all-ones vector is a right eigenvector of Pᵀ).
- •Under mild conditions (finite state), there exists at least one stationary distribution.

But uniqueness and convergence require extra structure (irreducible/aperiodic), which we develop next.

## Core Mechanic 2: Structure of the State Graph (Reachability, Classes, Periodicity)

### Why structure comes before limits

If you ask “what happens as t → ∞?”, the honest answer depends on the *shape* of the chain.

- •If the chain can get trapped, long-run behavior depends on where you start.
- •If the chain alternates deterministically between two sets, it may never settle.

These are not numerical issues—they are **graph properties** of the transition structure.

### Reachability and communication

We say state j is **reachable** from i (write i → j) if there exists some k ≥ 0 such that Pᵏ[i,j] > 0.

- •k is “some number of steps.”
- •The condition Pᵏ[i,j] > 0 means: there is a path with nonzero probability.

Two states **communicate** (i ↔ j) if i → j and j → i. Communication is an equivalence relation, so it partitions the state space into **communicating classes**.

#### Closed classes and absorbing behavior

A communicating class C is **closed** if you cannot leave it:

- •For i ∈ C and j ∉ C, P[i,j] = 0.

A special case: an **absorbing state** a has P[a,a] = 1. Then {a} is a closed class.

Intuition: once probability mass enters a closed class, it never leaves. That’s why closed classes control long-run behavior.

### Irreducibility

A Markov chain is **irreducible** if it has exactly one communicating class (i.e., every state can reach every other).

Why you care:

- •Irreducible chains behave “as one piece.”
- •Stationary distributions (when they exist) are typically unique in irreducible finite chains.

### Periodicity (the subtle oscillation trap)

Even if a chain is irreducible, it might “cycle” in a rigid rhythm.

The **period** of a state i is

d(i)=gcd⁡{t≥1:Pt[i,i]>0}.d(i) = \gcd\{ t \ge 1 : P^t[i,i] > 0 \}.d(i)=gcd{t≥1:Pt[i,i]>0}.

- •If d(i) = 1, the state is **aperiodic**.
- •If d(i) = 2, returns only happen at even times (classic bipartite alternation).

In an irreducible chain, all states share the same period. So we can talk about “the chain’s period.”

#### Why periodicity matters for convergence

If the chain has period 2, the distribution may alternate forever:

- •πₜ might converge along even t to one limit and along odd t to another.
- •But πₜ may not converge to a single vector.

Aperiodicity is the condition that prevents this “synchronization.”

### A concrete periodic example

States {1,2} with

P=[0110].P = \begin{bmatrix}0 & 1\\ 1 & 0\end{bmatrix}.P=[01​10​].

Starting at 1:

- •π₀ = [1,0]
- •π₁ = [0,1]
- •π₂ = [1,0]

It never settles.

Yet it *does* have a stationary distribution:

π=[1/2,1/2],πP=[1/2,1/2].\pi = [1/2, 1/2], \quad \pi P = [1/2, 1/2].π=[1/2,1/2],πP=[1/2,1/2].

So: **existence of a stationary distribution does not automatically imply convergence to it** from an arbitrary start. Periodicity blocks convergence.

### Absorbing vs irreducible vs periodic: a quick comparison

| Property | Graph meaning | Long-run consequence (typical) |
| --- | --- | --- |
| Absorbing state | self-loop with prob 1; closed singleton class | eventual trapping possible |
| Reducible chain | multiple communicating classes | long-run depends on which closed class you enter |
| Irreducible chain | one communicating class | behaves as a single component |
| Periodic chain | returns happen only at multiples of d>1 | distribution may oscillate |
| Aperiodic chain | no forced rhythm | enables convergence of πₜ |

### Stationary distributions in reducible chains (why there can be many)

If there are multiple closed classes, you can build stationary distributions supported on each closed class, and mixtures of those are also stationary.

Example idea:

- •If C₁ and C₂ are disjoint closed classes, and π¹, π² are stationary on each class, then απ¹ + (1−α)π² is stationary for any α ∈ [0,1].

This is one reason uniqueness needs irreducibility.

### “Ergodic” in finite Markov chains

In many applied contexts, “ergodic” (for finite chains) is shorthand for:

- •**irreducible + aperiodic**

This combination is what gives the clean convergence story:

- •a unique stationary distribution π
- •convergence πₜ → π for any starting distribution π₀

We’ll state that more formally in the next section.

## Application/Connection: Stationary Distributions, Convergence, and Why They Power PageRank, RL, and MCMC

### Why stationary distributions matter

A stationary distribution π is a probability distribution that is unchanged by one step of the chain.

In applications, π often represents:

- •long-run fraction of time spent in each state (when convergence/ergodicity holds)
- •the target distribution you want to sample from (MCMC)
- •the “importance” score of nodes in a graph (PageRank)

### Solving for π: the linear system

Stationarity is

π=πP.\pi = \pi P.π=πP.

This gives n equations, but they are not independent because probabilities sum to 1. The standard approach is:

1) solve (Pᵀ − I) **v** = **0** (right-nullspace of Pᵀ − I)

2) normalize so entries sum to 1

Using our row-vector convention, π is a left eigenvector. Computationally, it’s often easier to solve the transpose system.

Also include normalization:

∑jπ[j]=1.\sum\_j \pi[j] = 1.j∑​π[j]=1.

So we solve:

{π(I−P)=0∑jπ[j]=1\begin{cases}
\pi(I - P) = 0 \\
\sum\_j \pi[j] = 1
\end{cases}{π(I−P)=0∑j​π[j]=1​

### Convergence theorem (finite state, high-level)

For a **finite**, **irreducible**, **aperiodic** Markov chain:

- •There exists a **unique** stationary distribution π with π[j] > 0 for all j.
- •For any starting distribution π₀,

πt=π0Pt→πas t→∞.\pi\_t = \pi\_0 P^t \to \pi \quad \text{as } t\to\infty.πt​=π0​Pt→πas t→∞.

This is the core “why Markov chains are useful” result: long-run behavior forgets the initial condition.

### Intuition for why convergence happens (without proving it fully)

Two complementary intuitions:

1) **Mixing / smoothing:** multiplying by P averages across possible next states. Repeated averaging tends to wash out spikes in the distribution.

2) **Spectral gap:** eigenvalue 1 corresponds to the stationary direction. Other eigenvalues have magnitude < 1 (for ergodic chains), so their contributions decay like |λ|ᵗ.

A sketch (not a full proof): if P is diagonalizable,

P=VΛV−1P = V \Lambda V^{-1}P=VΛV−1

then

Pt=VΛtV−1.P^t = V \Lambda^t V^{-1}.Pt=VΛtV−1.

As t grows, λ₁=1 stays, while |λ₂|ᵗ, |λ₃|ᵗ, … shrink to 0, leaving only the stationary component.

### Detailed balance (reversible chains) and a handy sufficient condition

Many chains (especially in MCMC) are designed to satisfy **detailed balance** with respect to a desired π:

π[i]P[i,j]=π[j]P[j,i]∀i,j.\pi[i] P[i,j] = \pi[j] P[j,i] \quad \forall i,j.π[i]P[i,j]=π[j]P[j,i]∀i,j.

If detailed balance holds and the chain is irreducible, then π is stationary.

Show your work (why detailed balance implies stationarity):

Start from stationarity condition for each state j:

∑iπ[i]P[i,j]=?π[j].\sum\_i \pi[i]P[i,j] \stackrel{?}{=} \pi[j].i∑​π[i]P[i,j]=?π[j].

Using detailed balance, rewrite each term:

∑iπ[i]P[i,j]=∑iπ[j]P[j,i]=π[j]∑iP[j,i]=π[j]⋅1=π[j].\sum\_i \pi[i]P[i,j] = \sum\_i \pi[j]P[j,i] = \pi[j] \sum\_i P[j,i] = \pi[j]\cdot 1 = \pi[j].i∑​π[i]P[i,j]=i∑​π[j]P[j,i]=π[j]i∑​P[j,i]=π[j]⋅1=π[j].

So detailed balance is a powerful “design pattern” for constructing chains with a chosen stationary distribution.

### PageRank as a stationary distribution

The web can be viewed as a directed graph; a random surfer follows outgoing links. The transition matrix is built from link structure, often with a “teleport” term to guarantee irreducibility/aperiodicity.

A common form:

P=αPlink+(1−α)1n11TP = \alpha P\_{\text{link}} + (1-\alpha)\frac{1}{n}\mathbf{1}\mathbf{1}^TP=αPlink​+(1−α)n1​11T

(Here written in matrix form; conceptually, with probability 1−α you jump uniformly at random.)

The PageRank vector is the stationary distribution π satisfying π = πP.

Why teleport helps:

- •makes every state reachable from every other (irreducible)
- •introduces self-return possibilities that break periodicity (aperiodic)
- •ensures unique π and convergence

### Markov chains inside reinforcement learning

RL and MDPs assume the environment has the Markov property:

- •next state distribution depends only on current state and action

Even if you haven’t introduced actions yet, pure Markov chains are the “no-action” baseline. Concepts like stationary distribution later become:

- •stationary state distribution under a fixed policy
- •average reward under that distribution

### Markov Chain Monte Carlo (MCMC)

In MCMC, you want samples from a complex target distribution π (e.g., a posterior). You design a Markov chain whose stationary distribution is π, run it, and treat later states as approximate samples.

Key connection:

- •stationarity tells you “π is a fixed point”
- •mixing/convergence tells you how long you must run (burn-in) and how correlated samples are

### What you should be able to do after this node

- •Translate between graph and matrix views.
- •Compute πₜ after k steps via π₀Pᵏ.
- •Solve for stationary distributions via linear algebra.
- •Diagnose when convergence fails (reducible/periodic).
- •Recognize why irreducible + aperiodic is the standard condition.

## Worked Examples (3)

### Example 1: Compute a stationary distribution (solve π = πP)

Consider a 3-state Markov chain with transition matrix

P=[0.50.50.00.20.50.30.10.00.9].P = \begin{bmatrix}
0.5 & 0.5 & 0.0\\
0.2 & 0.5 & 0.3\\
0.1 & 0.0 & 0.9
\end{bmatrix}.P=​0.50.20.1​0.50.50.0​0.00.30.9​​.

Find a stationary distribution π = [π₁, π₂, π₃].

1. Write the stationarity equations π = πP component-wise.

   We compute each coordinate:

   π₁ = 0.5π₁ + 0.2π₂ + 0.1π₃

   π₂ = 0.5π₁ + 0.5π₂ + 0.0π₃

   π₃ = 0.0π₁ + 0.3π₂ + 0.9π₃
2. Bring terms to one side to get linear equations.

   (1) π₁ − 0.5π₁ − 0.2π₂ − 0.1π₃ = 0 ⇒ 0.5π₁ − 0.2π₂ − 0.1π₃ = 0

   (2) π₂ − 0.5π₁ − 0.5π₂ = 0 ⇒ 0.5π₂ − 0.5π₁ = 0 ⇒ π₂ = π₁

   (3) π₃ − 0.3π₂ − 0.9π₃ = 0 ⇒ 0.1π₃ − 0.3π₂ = 0 ⇒ π₃ = 3π₂
3. Use (2) and (3) to express everything in terms of π₁.

   From (2): π₂ = π₁

   From (3): π₃ = 3π₂ = 3π₁
4. Check that equation (1) is consistent.

   Plug in:

   0.5π₁ − 0.2π₂ − 0.1π₃

   = 0.5π₁ − 0.2(π₁) − 0.1(3π₁)

   = 0.5π₁ − 0.2π₁ − 0.3π₁

   = 0

   So it’s consistent (as expected; one equation is redundant).
5. Apply normalization π₁ + π₂ + π₃ = 1.

   π₁ + π₁ + 3π₁ = 5π₁ = 1

   ⇒ π₁ = 1/5

   ⇒ π₂ = 1/5

   ⇒ π₃ = 3/5
6. Conclude:

   π = [1/5, 1/5, 3/5].

**Insight:** Stationarity is an eigenvector condition with a probability normalization. In finite chains, one of the linear equations is typically redundant, so you solve n−1 independent equations plus ∑πᵢ=1.

### Example 2: Diagnose reducibility/periodicity and predict long-run behavior

Consider a 4-state chain with states {1,2,3,4} and transitions:

- •1 → 2 with prob 1
- •2 → 1 with prob 1
- •3 → 4 with prob 1
- •4 → 4 with prob 1

In matrix form (rows are current state):

P=[0100100000010001].P = \begin{bmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&0&1\\
0&0&0&1
\end{bmatrix}.P=​0100​1000​0000​0011​​.

(a) Identify communicating classes and whether they are closed.

(b) Does πₜ converge from an arbitrary start? Explain briefly.

(c) Find all stationary distributions.

1. (a) Find communicating classes.

   - •States 1 and 2 reach each other: 1→2 and 2→1, so {1,2} is a communicating class.
   - •State 3 reaches 4 (3→4), but 4 does not reach 3, so 3 is not in the same class as 4.
   - •State 4 reaches itself (4→4), so {4} is a communicating class.
   - •State 3 alone is also a communicating class? Actually, communication requires mutual reachability; 3 cannot be reached back from 4, and 3 cannot return to itself (no 3→3 path). So {3} is its own (transient) class in the partition sense, but it is not closed.
2. Decide which classes are closed.

   - •From {1,2} you cannot go to 3 or 4 (those transition probabilities are 0), so {1,2} is closed.
   - •{4} is closed because 4→4 with prob 1.
   - •{3} is not closed because it goes to 4.
3. (b) Convergence of πₜ.

   There are two issues:

   1) Reducibility: there are multiple closed classes ({1,2} and {4}). Long-run behavior depends on whether probability mass ends up in {1,2} or in {4}.

   2) Periodicity inside {1,2}: the subchain on {1,2} alternates with period 2.

   So from an arbitrary start, πₜ does not necessarily converge to a single limit vector. If some mass is in {1,2}, that part oscillates forever between states 1 and 2. Mass that reaches 4 stays at 4.
4. (c) Find all stationary distributions.

   A stationary distribution can place mass on any closed class, but must be stationary within each closed class.

   - •On class {4}, the only stationary distribution is δ₄ = [0,0,0,1].
   - •On class {1,2} with P\_sub = [[0,1],[1,0]], the stationary distribution is [1/2,1/2] on {1,2}.

   Therefore any convex combination is stationary:

   π(α) = α[1/2,1/2,0,0] + (1−α)[0,0,0,1]

   = [α/2, α/2, 0, 1−α]

   for α ∈ [0,1].

**Insight:** Closed communicating classes determine where probability can live forever. Multiple closed classes ⇒ non-unique stationary distributions. Periodicity can prevent convergence even when a stationary distribution exists.

### Example 3: Use Pᵏ to compute a multi-step probability

Using the Rainy/Sunny chain

P=[0.70.30.40.6],P = \begin{bmatrix}0.7&0.3\\0.4&0.6\end{bmatrix},P=[0.70.4​0.30.6​],

compute Pr(X₂ = Sunny | X₀ = Rainy).

1. Recognize that this is a 2-step transition probability:

   Pr(X₂=Sunny | X₀=Rainy) = P²[Rainy,Sunny].
2. Compute P² = P·P.

   P2=[0.70.30.40.6][0.70.30.40.6]P^2 = \begin{bmatrix}0.7&0.3\\0.4&0.6\end{bmatrix}
   \begin{bmatrix}0.7&0.3\\0.4&0.6\end{bmatrix}P2=[0.70.4​0.30.6​][0.70.4​0.30.6​]
3. Multiply (showing each entry).

   Top-right entry (Rainy→Sunny in 2 steps):

   P²[1,2] = 0.7·0.3 + 0.3·0.6 = 0.21 + 0.18 = 0.39.
4. Conclude:

   Pr(X₂ = Sunny | X₀ = Rainy) = 0.39.

**Insight:** Pᵏ packages “sum over all length-k paths” into matrix multiplication. Each entry of Pᵏ is exactly a k-step conditional probability.

## Key Takeaways

- ✓

  Markov property: $Pr⁡(Xt+1=j∣Xt=i,history)=Pr⁡(Xt+1=j∣Xt=i).\Pr(X\_{t+1}=j\mid X\_t=i,\text{history}) = \Pr(X\_{t+1}=j\mid X\_t=i).Pr(Xt+1​=j∣Xt​=i,history)=Pr(Xt+1​=j∣Xt​=i).$
- ✓

  For finite chains, the transition matrix P is row-stochastic: P[i,j] ≥ 0 and ∑ⱼ P[i,j] = 1.
- ✓

  Distributions evolve linearly: $πt+1=πtP\pi\_{t+1} = \pi\_t Pπt+1​=πt​Pandmoregenerally and more generally andmoregenerallyπt+k=πtPk.\pi\_{t+k} = \pi\_t P^k.πt+k​=πt​Pk.$
- ✓

  k-step transition probabilities are entries of Pᵏ: $Pk[i,j]=Pr⁡(Xt+k=j∣Xt=i).P^k[i,j] = \Pr(X\_{t+k}=j\mid X\_t=i).Pk[i,j]=Pr(Xt+k​=j∣Xt​=i).$
- ✓

  A stationary distribution satisfies $π=πP\pi = \pi Pπ=πP$ (a left eigenvector with eigenvalue 1 plus normalization).
- ✓

  Graph structure matters: communicating classes and closed classes determine trapping and non-uniqueness.
- ✓

  Irreducible + aperiodic (often called ergodic in finite chains) implies unique stationary distribution and convergence πₜ → π.
- ✓

  Periodicity can prevent convergence even when a stationary distribution exists (e.g., 2-cycle alternation).

## Common Mistakes

- ✗

  Mixing up row-vector vs column-vector conventions (and accidentally using Pᵀ). Always check whether rows or columns sum to 1 and which side you multiply on.
- ✗

  Assuming “stationary distribution exists” ⇒ “πₜ converges to it.” Periodic or reducible chains can have stationary distributions without convergence from arbitrary starts.
- ✗

  Forgetting that reducible chains can have many stationary distributions (mixtures across closed classes).
- ✗

  Computing π from π=πP but forgetting the normalization constraint ∑ᵢ πᵢ = 1 (or accepting negative entries from an un-constrained solve).

## Practice

easy

Let

P=[0.90.10.20.8].P = \begin{bmatrix}
0.9 & 0.1\\
0.2 & 0.8
\end{bmatrix}.P=[0.90.2​0.10.8​].

(a) Solve for the stationary distribution π.

(b) Starting from π₀=[1,0], compute π₁ and π₂.

**Hint:** Use π=πP and π₁+π₂=1. For part (b), multiply row vectors by P.

Show solution

Let π=[a,b]. Stationarity gives:

a = 0.9a + 0.2b

b = 0.1a + 0.8b (redundant)

From first: a − 0.9a = 0.2b ⇒ 0.1a = 0.2b ⇒ a = 2b.

Normalize: a+b=1 ⇒ 2b+b=1 ⇒ b=1/3, a=2/3.

So π=[2/3, 1/3].

(b) π₁ = [1,0]P = [0.9,0.1].

π₂ = π₁P = [0.9,0.1]P:

First component = 0.9·0.9 + 0.1·0.2 = 0.81+0.02=0.83.

Second component = 0.9·0.1 + 0.1·0.8 = 0.09+0.08=0.17.

So π₂=[0.83,0.17].

medium

Consider the 3-state chain with edges 1→2, 2→3, 3→1 each with probability 1.

(a) Is the chain irreducible?

(b) What is its period?

(c) Find a stationary distribution.

(d) Does πₜ converge to that stationary distribution from π₀=[1,0,0]?

**Hint:** This is a deterministic cycle. Think about return times to a state. For stationarity, symmetry is a clue.

Show solution

(a) Yes, it is irreducible: from any state you can reach any other by following the cycle.

(b) The period is 3 because you return to state 1 only at times 3,6,9,… so gcd is 3.

(c) Stationary distribution is uniform: π=[1/3,1/3,1/3] (check: multiplying by P permutes coordinates).

(d) No. Starting from [1,0,0], the distribution is a point mass that rotates: π₁=[0,1,0], π₂=[0,0,1], π₃=[1,0,0]. It does not converge, due to periodicity.

hard

A chain has two closed communicating classes C₁ and C₂, each irreducible and aperiodic on its own. Explain why the overall chain can have infinitely many stationary distributions, and give the general form in words or symbols.

**Hint:** Stationary distributions can be supported entirely on a closed class. Mixtures of stationary distributions are stationary.

Show solution

Let π¹ be the unique stationary distribution supported on C₁ (zero outside C₁), and π² the unique stationary distribution supported on C₂. Because C₁ and C₂ are closed, probability mass never leaves them, so each π¹ and π² is stationary for the full chain. Any convex combination

π(α) = απ¹ + (1−α)π², α ∈ [0,1]

is also stationary (linearity of πP). As α varies continuously, there are infinitely many stationary distributions.

## Connections

Next nodes you can unlock and why they connect:

- •[Reinforcement Learning Introduction](/tech-tree/rl-intro/): RL assumes Markovian state transitions; policies induce Markov chains over states.
- •[Markov Decision Processes](/tech-tree/mdp/): An MDP is a Markov chain controlled by actions; Bellman equations build on transition matrices.
- •[MCMC](/tech-tree/mcmc/): MCMC designs Markov chains with a chosen stationary distribution π and relies on convergence/mixing.
- •[Concentration Inequalities](/tech-tree/concentration-inequalities/): Used to quantify deviations of empirical averages along a Markov chain from expectations (after mixing assumptions).

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
