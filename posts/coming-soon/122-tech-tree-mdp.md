---
title: Markov Decision Processes
description: Formal framework for sequential decision-making. Bellman equations.
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
permalink: /tech-tree/mdp/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Markov Decision Processes

Machine LearningDifficulty: ★★★★★Depth: 7Unlocks: 3

Formal framework for sequential decision-making. Bellman equations.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Markov decision epoch: a state and chosen action determine a probability distribution over the next state (the Markov property)
- -Reward function: an immediate scalar feedback assigned to transitions (or state-action pairs)
- -Policy: a decision rule (possibly stochastic) mapping states to actions
- -Value function: the expected discounted sum of future rewards from a state (or state-action) under a policy

## Key Symbols & Notation

gamma (discount factor: scalar 0<=gamma<=1 that weights future rewards)

## Essential Relationships

- -Bellman equation: a recursive identity that relates a value to the immediate expected reward plus gamma times the expected next-state value under a policy; replacing the policy expectation by a max gives the Bellman optimality equation

## Prerequisites (3)

[Reinforcement Learning Introduction6 atoms](/tech-tree/rl-intro/)[Markov Chains6 atoms](/tech-tree/markov-chains/)[Dynamic Programming6 atoms](/tech-tree/dynamic-programming/)

## Unlocks (2)

[Policy Gradient Methodslvl 5](/tech-tree/policy-gradient/)[Task Discretizationlvl 5](/tech-tree/task-discretization/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[Time HorizonBusiness

MDPs formalize time horizon mathematically via finite vs infinite horizon planning, discount factors encoding time preference, and Bellman equations for sequential decision-making - the exact mathematical framework underlying business time horizon analysis.](/business/time-horizon/)[Discount FactorBusiness

Bellman equations formally define the discount factor gamma that weights future rewards, making MDPs the mathematical framework where this concept is rigorously grounded and applied.](/business/discount-factor/)

Advanced Learning Details

### Graph Position

146

Depth Cost

3

Fan-Out (ROI)

2

Bottleneck Score

7

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

### All Concepts (15)

- - Formal MDP definition as a 5-tuple specifying the decision problem (states, actions, transition dynamics, rewards, discounting)
- - Action-conditioned transition dynamics (transition kernel) P(s' | s, a) distinct from Markov-chain transitions
- - Reward specification as part of the model (immediate reward function or reward distribution r or R(s,a, s'))
- - Discount factor γ as an explicit model parameter controlling present value of future rewards
- - Return (cumulative discounted reward) G\_t defined over a trajectory
- - State-value function V^π(s) (expected return from state s under policy π)
- - Action-value function Q^π(s,a) (expected return after taking action a in state s then following π)
- - Optimal value functions V\*(s) and Q\*(s,a) (values under an optimal policy)
- - Bellman expectation equation (recursive identity for V^π and Q^π)
- - Bellman optimality equation (recursive max-based identity for V\* and Q\*)
- - Bellman (backup) operator(s) T^π and T\* as operators mapping value functions to updated value functions
- - Value iteration and policy iteration as DP algorithms that use Bellman backups to compute optimal values/policies
- - Definition of an optimal policy π\* and how it relates to V\* and Q\* (policy extraction)
- - Finite-horizon vs. infinite-horizon (continuing) formulation distinction and how discounting/termination interacts with returns
- - Stochastic vs deterministic policies in the MDP formalism (π(a|s) as a distribution vs a mapping)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Markov Decision Processes (MDPs) are the “assembly language” of reinforcement learning: once you can express a problem as an MDP, you can derive Bellman equations, prove what an optimal policy means, and justify algorithms like value iteration, policy iteration, and actor-critic methods.

TL;DR:

An MDP formalizes sequential decision-making with (S, A, P, R, γ). A policy π(a|s) induces a Markov reward process, which defines value functions V^π(s) and Q^π(s,a) as expected discounted return. Bellman expectation equations describe V^π and Q^π recursively. Bellman optimality equations define V*(s) and Q*(s,a) via a max over actions. Dynamic programming uses these equations to compute optimal policies when P and R are known.

## What Is a Markov Decision Process?

### Why we need a formalism

In reinforcement learning, you interact with an environment over time. The key difficulty is **credit assignment across time**: an action now may cause a good or bad outcome many steps later. To reason about this cleanly, we want a model that:

1. 1)Separates what the agent controls (actions, policy) from what the environment does (stochastic transitions).
2. 2)Encodes **time** and **uncertainty**.
3. 3)Is simple enough to yield recursive equations (so dynamic programming applies).

An **MDP** is the standard model that accomplishes this.

### Definition

A (finite) **Markov Decision Process** is a tuple:

- •**S**: set of states
- •**A**: set of actions (sometimes A(s) depends on the state)
- •**P**: transition dynamics, where

P(s′ | s, a) = Pr(Sₜ₊₁ = s′ | Sₜ = s, Aₜ = a)

- •**R**: reward function. Common choices:
- •R(s, a): expected immediate reward after taking action a in state s
- •R(s, a, s′): expected reward for the transition (s, a, s′)
- •**γ** (gamma): discount factor, 0 ≤ γ ≤ 1

### The Markov decision epoch (Markov property)

The “atomic step” of an MDP is a **decision epoch**:

- •You are in state s
- •You choose an action a (possibly stochastically)
- •The environment samples the next state s′ from P(·|s,a)
- •You receive a reward r governed by R

The **Markov property** means the future depends on the past **only through the current state** (and chosen action):

Pr(Sₜ₊₁ = s′ | S₀, A₀, …, Sₜ = s, Aₜ = a) = Pr(Sₜ₊₁ = s′ | Sₜ = s, Aₜ = a)

This assumption is what lets us write Bellman equations: it provides the “optimal substructure” for sequential decisions.

### Trajectories and return

A trajectory is a sequence (S₀, A₀, R₁, S₁, A₁, R₂, …). The (discounted) **return** from time t is:

Gₜ = ∑ₖ₌₀^∞ γᵏ Rₜ₊ₖ₊₁

- •If γ is near 0, you care mostly about immediate reward.
- •If γ is near 1, you care strongly about long-term reward (but need conditions to keep the sum finite).

### What γ really does (motivation before math)

Discounting is not just a mathematical trick. It does three practical jobs:

1. 1)**Preference for sooner rewards** (time preference).
2. 2)**Convergence**: if rewards are bounded, discounting ensures ∑ γᵏ R converges.
3. 3)**Effective horizon**: roughly, rewards more than ~1/(1−γ) steps away contribute little.

### Relationship to Markov chains and dynamic programming

An MDP generalizes a Markov chain:

- •A Markov chain has P(s′|s).
- •An MDP has P(s′|s,a), because the agent’s action influences transitions.

An MDP also sets up dynamic programming:

- •The value of a state can be written in terms of the value of successor states.
- •That recursion is exactly what DP exploits.

### A quick taxonomy (to orient you)

| Object | What it specifies | What you can do with it |
| --- | --- | --- |
| Markov chain | P(s′ | s) | Study long-run state distribution |
| Markov reward process | P(s′ | s), R(s) | Evaluate long-run returns |
| MDP | P(s′ | s,a), R, γ | Choose actions to maximize return |

The rest of this lesson builds the two central ingredients: **policies** and **value functions**, and then shows how Bellman equations connect them.

## Core Mechanic 1: Policies Induce Value Functions

### Why policies come first

An MDP by itself is just a world model. To talk about “expected return,” we must specify **how actions are selected**. That’s the role of a **policy**.

### Policies (deterministic and stochastic)

A **policy** π is a decision rule mapping states to actions.

- •Deterministic: a = π(s)
- •Stochastic: π(a|s) = Pr(Aₜ = a | Sₜ = s)

Stochastic policies matter even when the environment is fully known:

- •They can represent uncertainty or exploration.
- •In some settings (e.g., partial observability), randomization can be essential.

### From an MDP + policy to a Markov reward process

Once you fix π, the agent is no longer “choosing” actions freely; actions are sampled from π. The resulting state process becomes a Markov chain with transition matrix:

P^π(s′|s) = ∑ₐ π(a|s) P(s′|s,a)

If rewards depend on (s,a) (or (s,a,s′)), you also get an induced reward model, e.g.:

R^π(s) = ∑ₐ π(a|s) R(s,a)

This reduction is conceptually important: **policy evaluation** is “just” analyzing the Markov reward process induced by π.

### Value function: expected discounted return

Now we define the central predictive quantities.

**State-value function**:

V^π(s) = 𝔼\_π[ Gₜ | Sₜ = s ] = 𝔼\_π[ ∑ₖ₌₀^∞ γᵏ Rₜ₊ₖ₊₁ | Sₜ = s ]

**Action-value function**:

Q^π(s,a) = 𝔼\_π[ Gₜ | Sₜ = s, Aₜ = a ]

Intuition:

- •V^π(s) tells you how good it is to be in s, if you commit to following π.
- •Q^π(s,a) tells you how good it is to take action a in s, and then follow π.

### Advantage function (useful later)

A closely related quantity is the **advantage**:

A^π(s,a) = Q^π(s,a) − V^π(s)

It measures how much better/worse an action is compared to the policy’s average behavior at s.

### Bellman expectation equations (the key recursion)

#### Why a recursion exists

Because of the Markov property, the future after the next step depends only on the next state (and the policy). So the return decomposes into:

Gₜ = Rₜ₊₁ + γ Gₜ₊₁

Take conditional expectation under π.

#### Deriving the Bellman expectation equation for V^π

Start from the definition:

V^π(s) = 𝔼\_π[ Gₜ | Sₜ = s ]

Substitute Gₜ = Rₜ₊₁ + γ Gₜ₊₁:

V^π(s)

= 𝔼\_π[ Rₜ₊₁ + γ Gₜ₊₁ | Sₜ = s ]

= 𝔼\_π[ Rₜ₊₁ | Sₜ = s ] + γ 𝔼\_π[ Gₜ₊₁ | Sₜ = s ]

Now expand the next-step expectation by conditioning on Aₜ and Sₜ₊₁:

𝔼\_π[ Rₜ₊₁ + γ V^π(Sₜ₊₁) | Sₜ = s ]

= ∑ₐ π(a|s) ∑\_{s′} P(s′|s,a) \big( R(s,a,s′) + γ V^π(s′) \big)

So:

V^π(s) = ∑ₐ π(a|s) ∑\_{s′} P(s′|s,a) ( R(s,a,s′) + γ V^π(s′) )

This is the **Bellman expectation equation** for V^π.

#### Bellman expectation equation for Q^π

Similarly:

Q^π(s,a) = ∑\_{s′} P(s′|s,a) ( R(s,a,s′) + γ 𝔼\_{a′∼π(·|s′)}[ Q^π(s′,a′) ] )

Or equivalently:

Q^π(s,a) = ∑\_{s′} P(s′|s,a) ( R(s,a,s′) + γ ∑\_{a′} π(a′|s′) Q^π(s′,a′) )

### Vector/matrix form (finite state MRP view)

When π is fixed, you can write the state-value Bellman equation in linear algebra form.

Let **V**^π ∈ ℝ^{|S|} be a vector with entries V^π(s). Define:

- •**P**^π ∈ ℝ^{|S|×|S|}, with entries P^π(s′|s)
- •**r**^π ∈ ℝ^{|S|}, with entries r^π(s) = 𝔼\_π[Rₜ₊₁|Sₜ=s]

Then:

**V**^π = **r**^π + γ **P**^π **V**^π

Rearrange:

( **I** − γ **P**^π ) **V**^π = **r**^π

If ( **I** − γ **P**^π ) is invertible (it is under standard discounted assumptions), then:

**V**^π = ( **I** − γ **P**^π )⁻¹ **r**^π

This “closed form” is conceptually useful: policy evaluation becomes solving a linear system. Practically, DP and iterative methods are often preferred.

### A note on terminal states and episodic tasks

Many tasks end (episode termination). A common modeling choice:

- •Add terminal absorbing state s\_T with P(s\_T|s\_T,a)=1 and reward 0 thereafter.
- •Or define V(s\_T)=0 by convention.

Either way, Bellman equations remain valid with appropriate boundary conditions.

## Core Mechanic 2: Optimality and the Bellman Optimality Equations

### Why “optimality” is subtle

Once you define V^π and Q^π, it’s tempting to say “pick the action with highest value.” But value depends on the policy itself: if you change actions now, future actions may also change.

So we define optimality in a fixed point sense: an **optimal policy** is one whose value dominates all others.

### Optimal value functions

Define the optimal state-value function:

V\*(s) = max\_π V^π(s)

and optimal action-value function:

Q\*(s,a) = max\_π Q^π(s,a)

These exist for finite discounted MDPs.

### Bellman optimality equation for V\*

Start from: if you are in s, and you act optimally, you choose the best action a, then the environment transitions, and you continue optimally from s′.

That gives:

V*(s) = maxₐ ∑\_{s′} P(s′|s,a) ( R(s,a,s′) + γ V*(s′) )

This is the **Bellman optimality equation**.

### Bellman optimality equation for Q\*

Similarly, for Q\* you commit to the first action a, then behave optimally afterward:

Q*(s,a) = ∑\_{s′} P(s′|s,a) ( R(s,a,s′) + γ max\_{a′} Q*(s′,a′) )

### Greedy policies and extracting an optimal policy

Once you have Q\*(s,a), you can define a greedy policy:

π*(s) ∈ argmaxₐ Q*(s,a)

This π\* is optimal (ties may yield multiple optimal policies).

### Policy improvement theorem (why greedy helps)

A key piece of theory is that being greedy with respect to a value function improves (or at least does not worsen) the policy.

Let π be any policy, and define a new policy π′ such that for all s:

π′(s) ∈ argmaxₐ Q^π(s,a)

Then:

V^{π′}(s) ≥ V^π(s) for all s

This theorem justifies **policy iteration**: evaluate π to get V^π (or Q^π), improve greedily to get π′, repeat.

### Contraction view (why the Bellman operator converges)

Define the Bellman optimality operator T acting on a value function V:

(TV)(s) = maxₐ ∑\_{s′} P(s′|s,a) ( R(s,a,s′) + γ V(s′) )

Then V\* is the unique fixed point:

V *= T V*

Under the max norm ‖·‖∞, T is a γ-contraction:

‖T V − T W‖∞ ≤ γ ‖V − W‖∞

This matters because:

- •Repeatedly applying T (value iteration) converges to V\*.
- •The rate depends on γ: as γ → 1, convergence slows.

Even if you don’t prove the contraction fully, the intuition is strong: discounting shrinks the influence of future differences by γ each step.

### Comparing the “three Bellman equations”

| Equation type | Recursion | Unknown | Use |
| --- | --- | --- | --- |
| Expectation (policy evaluation) | V^π = r^π + γ P^π V^π | V^π | Evaluate a fixed π |
| Optimality (planning) | V *= T V* | V\* | Find optimal values |
| Q-optimality | Q *= T\_Q Q* | Q\* | Extract greedy optimal π\* |

### Where the reward function fits

A common confusion: “Is reward tied to states or transitions?” In general, reward can depend on (s,a,s′). For many derivations, we use its expectation:

R̄(s,a) = 𝔼[ Rₜ₊₁ | Sₜ=s, Aₜ=a ] = ∑\_{s′} P(s′|s,a) R(s,a,s′)

Then Bellman optimality for V\* can be written:

V*(s) = maxₐ \big( R̄(s,a) + γ ∑\_{s′} P(s′|s,a) V*(s′) \big)

It’s the same idea—just less notation.

### Deterministic vs stochastic optimal policies

In finite discounted MDPs, there always exists an optimal **deterministic stationary** policy (depends only on s, not time). That’s a powerful simplification:

- •You don’t need to search over time-dependent policies.
- •You don’t need randomness to be optimal (though it may still be useful for learning).

This fact is part of why MDPs are such a clean framework.

## Application/Connection: Solving MDPs with Dynamic Programming (Planning) and How This Enables Modern RL

### Why dynamic programming applies

Dynamic programming works when:

- •The problem has **optimal substructure**: optimal decisions from state s depend on optimal solutions of successor states.
- •Subproblems overlap: many trajectories revisit the same state.

The Bellman optimality equation is precisely the DP recursion.

### Value iteration

Value iteration applies the optimality operator repeatedly.

Initialize V₀(s) arbitrarily (often 0). Then iterate:

V\_{k+1}(s) = maxₐ ∑\_{s′} P(s′|s,a) ( R(s,a,s′) + γ V\_k(s′) )

After convergence to V\*, extract:

π*(s) ∈ argmaxₐ ∑\_{s′} P(s′|s,a) ( R(s,a,s′) + γ V*(s′) )

What’s happening conceptually:

- •Early iterations propagate reward information one step outward.
- •Each iteration increases the “planning horizon” by roughly one step.

### Policy iteration

Policy iteration alternates between evaluation and improvement.

1) **Policy evaluation**: solve for V^π via:

V^π(s) = ∑ₐ π(a|s) ∑\_{s′} P(s′|s,a) ( R(s,a,s′) + γ V^π(s′) )

In matrix form:

( **I** − γ **P**^π ) **V**^π = **r**^π

2) **Policy improvement**:

π\_new(s) ∈ argmaxₐ ∑\_{s′} P(s′|s,a) ( R(s,a,s′) + γ V^π(s′) )

Repeat until the policy stops changing.

### Value iteration vs policy iteration

| Method | Main idea | Pros | Cons |
| --- | --- | --- | --- |
| Value iteration | Update V toward V\* directly | Simple, memory-light | Many iterations when γ≈1 |
| Policy iteration | Evaluate π exactly/approximately, then improve | Often fewer iterations | Evaluation can be expensive |
| Modified policy iteration | Partial evaluation + improvement | Flexible tradeoff | More moving parts |

### Where “learning” begins (model-free RL)

DP assumes you know P and R. In many RL problems you don’t; you only observe samples.

But the MDP framing still matters because:

- •TD learning methods approximate Bellman expectation equations using samples.
- •Q-learning approximates the Bellman optimality equation using samples.
- •Actor-critic methods tie policy optimization to value estimation (advantage functions).

This is the bridge from MDP theory to modern RL.

### Connection to policy gradients (unlock)

Policy gradient methods optimize π\_θ directly. The objective is typically:

J(θ) = 𝔼\_{τ∼π\_θ}[ ∑ₜ γᵗ Rₜ₊₁ ]

Even though policy gradients do not require an explicit model P, they still rely on the MDP structure:

- •Trajectories τ are generated by the MDP transitions.
- •The return Gₜ is defined by the same discounted sum.
- •Baselines often use V^π(s) to reduce variance, introducing the advantage A^π(s,a).

So understanding Bellman equations makes actor-critic updates feel motivated rather than magical.

### Connection to task discretization (unlock)

When you discretize a continuous or ill-defined task (common in LLM agent systems), you often create:

- •A discrete state representation S (milestones, tool states, memory summaries)
- •A discrete action set A (tool calls, subtask choices)
- •A reward signal R (success metrics, latency penalties, correctness scores)

If the resulting system approximately satisfies a Markov property (state summarizes relevant history), you can treat it as an MDP and apply planning/evaluation ideas:

- •Estimate values of subtasks (states)
- •Compare strategies (policies)
- •Reason about long-horizon tradeoffs via γ

Even if the environment is only approximately Markov, the MDP lens provides a disciplined way to debug and improve the design.

### Beyond the basics (what to keep in mind at difficulty 5)

MDPs are clean, but real RL systems introduce complications:

- •**Large/continuous state spaces**: V and Q must be approximated.
- •**Partial observability**: the Markov property fails for raw observations (POMDPs).
- •**Average-reward vs discounted**: some continuing tasks use average reward instead of γ.
- •**Off-policy learning**: evaluating/improving a target policy while behaving with another.

Still, the MDP + Bellman equations remain the conceptual backbone.

## Worked Examples (3)

### Compute V^π for a tiny MDP by solving Bellman expectation equations

States S = {A, B}. Actions are irrelevant because the policy is fixed and the transition is policy-induced.

Dynamics under π:

- •From A: go to B with probability 1, reward = +2
- •From B: stay at B with probability 1, reward = +1 each step

Discount γ = 0.9

Find V^π(A) and V^π(B).

1. Write Bellman equations.

   V^π(A) = 𝔼[R|A] + γ 𝔼[V^π(S′)|A]

   V^π(B) = 𝔼[R|B] + γ 𝔼[V^π(S′)|B]
2. Substitute the deterministic transitions and rewards.

   From A: reward 2, next state B.

   V^π(A) = 2 + 0.9 V^π(B)

   From B: reward 1, next state B.

   V^π(B) = 1 + 0.9 V^π(B)
3. Solve for V^π(B) first.

   V^π(B) = 1 + 0.9 V^π(B)

   V^π(B) − 0.9 V^π(B) = 1

   0.1 V^π(B) = 1

   V^π(B) = 10
4. Plug into V^π(A).

   V^π(A) = 2 + 0.9 · 10

   V^π(A) = 2 + 9

   V^π(A) = 11

**Insight:** Bellman expectation equations often let you solve values with simple algebra. Notice how a self-loop with constant reward creates a geometric series; the Bellman equation encodes that series compactly.

### Derive V\* and an optimal policy in a 2-action MDP (Bellman optimality)

Single nonterminal state s, plus terminal state T with V(T)=0.

At state s you can choose:

- •Action a₁: reward = 5, transition to T with probability 1
- •Action a₂: reward = 1, transition back to s with probability 1

Discount γ = 0.8

Compute V*(s), Q*(s,a₁), Q\*(s,a₂), and the optimal action.

1. Write Q\* for each action using the Q Bellman optimality equation.

   Q*(s,a) = ∑\_{s′} P(s′|s,a) ( R(s,a,s′) + γ max\_{a′} Q*(s′,a′) )
2. Compute Q\*(s,a₁).

   Taking a₁ leads to terminal T with reward 5.

   Q*(s,a₁) = 5 + 0.8 · V*(T)

   V\*(T) = 0

   So Q\*(s,a₁) = 5
3. Compute Q\*(s,a₂).

   Taking a₂ gives reward 1 and returns to s.

   Q*(s,a₂) = 1 + 0.8 · max\_{a′} Q*(s,a′)

   But max\_{a′} Q*(s,a′) is exactly V*(s). So:

   Q*(s,a₂) = 1 + 0.8 V*(s)
4. Relate V*(s) to Q*.

   V*(s) = max( Q*(s,a₁), Q\*(s,a₂) )

   = max( 5, 1 + 0.8 V\*(s) )
5. Check which action is optimal by solving the fixed point.

   If a₁ is optimal, then V\*(s)=5.

   Then Q\*(s,a₂)=1+0.8·5=1+4=5.

   So a₂ ties with a₁; both give value 5.
6. Confirm the tie is consistent.

   If V\*(s)=5, then max(5, 1+0.8·5)=max(5,5)=5, consistent.

   Therefore V\*(s)=5 and both actions are optimal.

   Final:

   Q\*(s,a₁)=5

   Q\*(s,a₂)=5

   V\*(s)=5

**Insight:** Bellman optimality can produce ties and multiple optimal policies. Here, a₂ is a “delayed gratification loop” whose discounted infinite sum matches the immediate terminal payoff.

### Policy improvement step using Q^π (one-step lookahead)

MDP with states S={s₁,s₂}, actions A={L,R}. Discount γ=0.5.

Transitions and rewards:

- •From s₁:
- •L: go to s₂ with prob 1, reward 0
- •R: go to s₂ with prob 1, reward 2
- •From s₂:
- •L: stay in s₂ with prob 1, reward 1
- •R: stay in s₂ with prob 1, reward 0

Current policy π chooses L everywhere.

Compute Q^π(s₁,L), Q^π(s₁,R) and improve π at s₁.

1. Evaluate V^π(s₂) under π (which picks L at s₂).

   Bellman:

   V^π(s₂) = 1 + 0.5 V^π(s₂)

   V^π(s₂) − 0.5 V^π(s₂) = 1

   0.5 V^π(s₂) = 1

   V^π(s₂) = 2
2. Compute Q^π(s₁,L).

   Taking L in s₁ gives reward 0 then goes to s₂.

   Q^π(s₁,L) = 0 + 0.5 V^π(s₂)

   = 0.5 · 2

   = 1
3. Compute Q^π(s₁,R).

   Taking R in s₁ gives reward 2 then goes to s₂.

   Q^π(s₁,R) = 2 + 0.5 V^π(s₂)

   = 2 + 1

   = 3
4. Improve policy greedily at s₁.

   argmax\_a Q^π(s₁,a) = R because 3 > 1.

   So set π′(s₁)=R (keeping π′(s₂)=L if only improving at s₁).

**Insight:** Policy improvement is local but principled: compare actions by their Q^π values (immediate reward plus discounted value of the next state). This is the core move behind policy iteration and many RL control methods.

## Key Takeaways

- ✓

  An MDP is defined by (S, A, P, R, γ) and models sequential decisions where (state, action) determine a distribution over next states (Markov property).
- ✓

  A policy π(a|s) turns an MDP into a Markov reward process with induced transition P^π(s′|s)=∑ₐ π(a|s)P(s′|s,a).
- ✓

  Value functions V^π(s) and Q^π(s,a) are expectations of the discounted return Gₜ=∑ₖ γᵏRₜ₊ₖ₊₁ under π.
- ✓

  Bellman expectation equations recursively define V^π and Q^π using one-step dynamics plus discounted continuation value.
- ✓

  Optimal value functions V *and Q* satisfy Bellman optimality equations with a max over actions; greedy policies w.r.t. Q\* are optimal.
- ✓

  Discount γ controls effective planning horizon and ensures contraction/convergence for standard discounted settings.
- ✓

  Dynamic programming methods (value iteration, policy iteration) solve known MDPs by repeatedly applying Bellman operators or alternating evaluation and improvement.
- ✓

  MDP/Bellman structure underlies modern model-free RL (TD learning, Q-learning) and policy gradient methods (via baselines and advantage).

## Common Mistakes

- ✗

  Confusing V^π and V*: V^π evaluates a specific policy; V* is the best achievable over all policies.
- ✗

  Forgetting to condition on the policy when computing expectations (e.g., using max where ∑ₐ π(a|s) is required, or vice versa).
- ✗

  Mishandling terminal states: not setting V(terminal)=0 (or not modeling absorbing transitions), leading to incorrect recursions.
- ✗

  Treating γ as optional without consequences: changing γ changes the objective (time preference and effective horizon), not just numerical stability.

## Practice

easy

Consider an MDP with states {0,1}. From state 0, action a keeps you in 0 with prob 1 and reward 1 each step. From state 1, the episode terminates with reward 0. Suppose the policy keeps taking a in state 0 and you never reach state 1. With γ=0.9, compute V^π(0).

**Hint:** Write V^π(0) = 1 + γ V^π(0) and solve.

Show solution

V^π(0) = 1 + 0.9 V^π(0)

V^π(0) − 0.9 V^π(0) = 1

0.1 V^π(0) = 1

V^π(0) = 10

medium

Let an MDP have two states s₁,s₂ and one action per state (so it’s a Markov reward process). Transitions: s₁→s₂ with prob 1 and reward 0; s₂→s₂ with prob 1 and reward 2. With γ=0.5, compute V(s₁), V(s₂) using Bellman equations.

**Hint:** Solve V(s₂)=2+γV(s₂) first, then plug into V(s₁)=0+γV(s₂).

Show solution

V(s₂)=2+0.5V(s₂)

V(s₂)−0.5V(s₂)=2

0.5V(s₂)=2

V(s₂)=4

V(s₁)=0+0.5V(s₂)=0.5·4=2

hard

In a finite discounted MDP, define the Bellman optimality operator (TV)(s)=maxₐ ∑\_{s′} P(s′|s,a)(R(s,a,s′)+γV(s′)). Show that if you have two value functions V and W, then |(TV)(s) − (TW)(s)| ≤ γ max\_{s′}|V(s′)−W(s′)| for every state s.

**Hint:** Use that maxₐ fₐ − maxₐ gₐ ≤ maxₐ (fₐ−gₐ), then apply triangle inequality and the fact that probabilities sum to 1.

Show solution

Let Δ = max\_{x} |V(x)−W(x)|.

For a fixed s and action a define:

F\_a = ∑\_{s′} P(s′|s,a)(R(s,a,s′)+γV(s′))

G\_a = ∑\_{s′} P(s′|s,a)(R(s,a,s′)+γW(s′))

Then F\_a−G\_a = γ ∑\_{s′} P(s′|s,a)(V(s′)−W(s′)).

So |F\_a−G\_a| ≤ γ ∑\_{s′} P(s′|s,a) |V(s′)−W(s′)| ≤ γ ∑\_{s′} P(s′|s,a) Δ = γΔ.

Now,

(TV)(s)=max\_a F\_a, (TW)(s)=max\_a G\_a.

Use the inequality |max\_a F\_a − max\_a G\_a| ≤ max\_a |F\_a−G\_a|.

Therefore |(TV)(s)−(TW)(s)| ≤ max\_a γΔ = γΔ = γ max\_{s′}|V(s′)−W(s′)|.

## Connections

- •Next: [Policy Gradient Methods](/tech-tree/policy-gradient/)
- •Also unlocks: [Task Discretization](/tech-tree/task-discretization/)
- •Review if needed: [Markov Chains](/tech-tree/markov-chains/)
- •Review if needed: [Dynamic Programming](/tech-tree/dynamic-programming/)
- •Earlier foundation: [Reinforcement Learning Introduction](/tech-tree/rl-intro/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
