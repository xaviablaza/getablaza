---
title: Reinforcement Learning Introduction
description: Learning from interaction. States, actions, rewards, policies.
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
permalink: /tech-tree/rl-intro/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Reinforcement Learning Introduction

Machine LearningDifficulty: ★★★★☆Depth: 6Unlocks: 4

Learning from interaction. States, actions, rewards, policies.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Markov Decision Process (MDP): the formal sequential-decision model (states, actions, transitions, rewards)
- -Policy: a (possibly stochastic) mapping from states to action choices
- -Value functions: state-value and action-value as measures of long-run return

## Key Symbols & Notation

pi(a | s) - policy (probability of action a in state s)P(s' | s, a) - transition probability to next state s' given state s and action a

## Essential Relationships

- -Value V^pi(s) or Q^pi(s,a) = expected (possibly discounted) cumulative future rewards when following policy pi, computed using MDP transitions P(s'|s,a)

## Prerequisites (2)

[Markov Chains6 atoms](/tech-tree/markov-chains/)[Expected Value5 atoms](/tech-tree/expected-value/)

## Unlocks (1)

[Markov Decision Processeslvl 5](/tech-tree/mdp/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[Feedback LoopBusiness

Reinforcement learning is the canonical formalization of feedback loops in ML: agent acts → environment returns state and reward → agent updates policy → agent acts again. The concept of a feedback loop is essentially the RL interaction cycle.](/business/feedback-loop/)

Advanced Learning Details

### Graph Position

93

Depth Cost

4

Fan-Out (ROI)

2

Bottleneck Score

6

Chain Length

### Cognitive Load

6

Atomic Elements

69

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (27)

- - Agent vs environment (interactive loop where an agent selects actions and the environment returns new states and rewards)
- - Actions and action space (set of choices available to the agent)
- - Reward signal (scalar feedback from the environment as the objective)
- - Reward function as a stochastic mapping r(s,a,s') or R\_{t+1} (reward associated with a transition)
- - Return (cumulative reward), i.e., sum of future rewards from a time step
- - Discount factor gamma (γ) that weights future rewards relative to immediate rewards
- - Policy (π): a mapping from states to actions or to distributions over actions
- - Deterministic vs stochastic policies (π(s)=a vs π(a|s) probability distributions)
- - State-value function V^π(s) (expected return from a state under policy π)
- - Action-value function Q^π(s,a) (expected return from taking action a in state s then following π)
- - Optimal policy (π\*) and optimal value functions V\* and Q\*
- - Bellman expectation relation (basis for policy evaluation)
- - Bellman optimality relation (basis for optimal control)
- - Model-based vs model-free distinction (whether the agent knows/uses transition and reward models)
- - Planning (using a model to compute/improve a policy without additional real interactions)
- - Learning from samples (estimating values/policies from observed transitions)
- - Monte Carlo vs temporal-difference (TD) approaches (sample-returns vs bootstrapped updates)
- - Temporal-difference error (TD error) as the instantaneous learning signal for bootstrapping
- - Bootstrapping (updating estimates using current estimates of future value)
- - Q-learning (an off-policy TD control algorithm for learning Q\*)
- - Policy evaluation and policy improvement (the iterative loop used in policy/policy-iteration methods)
- - Value iteration (iteratively applying Bellman optimality to converge to V\*)
- - Exploration vs exploitation trade-off (need to try suboptimal actions to discover better ones)
- - Exploration strategies (e.g., ε-greedy) and their role in learning
- - Learning rate / step-size (α) controlling incremental updates
- - Episodic vs continuing tasks (episodes with terminal states vs infinite-horizon problems)
- - Transition dynamics conditioned on actions P(s'|s,a) (action-dependent transitions, distinct from passive Markov chains)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Supervised learning learns from labeled examples. Reinforcement learning (RL) learns from consequences: an agent takes actions, the world responds, and the agent updates its behavior to get more reward over time. The feedback is delayed, noisy, and depends on your choices—so you must reason about sequences, not single predictions.

TL;DR:

Reinforcement learning models interaction as an MDP: states s, actions a, transition probabilities P(s′ | s, a), and rewards. A policy π(a | s) chooses actions. The goal is to maximize expected return (long-run cumulative reward). Value functions Vπ(s) and Qπ(s, a) quantify “how good” states and actions are under a policy, enabling planning and learning via Bellman-style recursions.

## What Is Reinforcement Learning Introduction?

### Why RL exists (motivation)

Many problems are not “predict the right label once.” They are “make a sequence of choices where today’s choice changes tomorrow’s situation.”

Examples:

- •A robot chooses torques now; that changes its position later.
- •A recommender chooses what to show; that changes user behavior and future data.
- •A game-playing agent moves a piece; that changes the board and future options.

The core difficulty: **you do not get direct labels** for the best action. Instead, you get **rewards** that may be delayed and may depend on long-term consequences.

### RL in one sentence

**Reinforcement learning** is the study of how an agent can learn a behavior (a **policy**) that maximizes expected long-run reward by interacting with an environment.

### The minimal loop

At each time step t:

1. 1)The agent observes a **state** sₜ.
2. 2)The agent picks an **action** aₜ (possibly randomly).
3. 3)The environment transitions to a new state sₜ₊₁.
4. 4)The agent receives a **reward** rₜ₊₁.

Over time, the agent should choose actions that lead to higher total reward.

### Key ingredients (conceptual vocabulary)

- •**State (s):** A summary of “what matters now.” In a clean formulation, it contains enough information to predict the future (in distribution) given an action.
- •**Action (a):** A choice available to the agent.
- •**Reward (r):** A scalar feedback signal indicating immediate desirability.
- •**Policy (π):** A rule for choosing actions; often written π(a | s).
- •**Return (G):** The total reward accumulated into the future (often discounted).

### What makes RL distinct

RL combines:

- •**Uncertainty** (transitions and rewards may be stochastic)
- •**Control** (your actions influence what data you see)
- •**Long horizons** (credit assignment across time)

A helpful comparison:

| Setting | Data source | Output | Feedback timing | Main challenge |
| --- | --- | --- | --- | --- |
| Supervised learning | fixed dataset (x, y) | predictor f(x) | immediate | generalization |
| Bandits | actions only, no state transitions | action selection | immediate-ish | exploration vs exploitation |
| RL (MDP) | interactive, sequential | policy π(a | s) | delayed | planning + exploration + credit assignment |

### Relationship to prerequisites

You already know **Markov chains**: P(s′ | s). RL generalizes this by adding actions: P(s′ | s, a). The agent’s policy π(a | s) effectively **induces** a Markov chain over states (because actions are chosen as a function of the current state).

You also know **expected value**. RL objectives are expectations over random trajectories:

- •randomness from the environment transitions
- •randomness from stochastic policies

So the core RL question becomes: **Which policy π maximizes expected return?**

## Core Mechanic 1: MDP Thinking — States, Actions, Rewards, and Dynamics

### Why we need a formal model

If you want to reason about long-term consequences, you need a framework that says:

- •what information you have now (state)
- •what choices you can make (actions)
- •how the world responds (transition probabilities)
- •how success is measured (rewards)

That framework is the **Markov Decision Process (MDP)**.

### The MDP components

An MDP is commonly specified by (S, A, P, R, γ):

- •S: set of states
- •A: set of actions
- •P(s′ | s, a): probability of next state s′ given current state s and action a
- •R: reward signal (often R(s, a, s′) or expected reward r(s, a))
- •γ ∈ [0, 1): discount factor

Even if the environment is deterministic, P(s′ | s, a) can encode that by putting probability 1 on the deterministic next state.

### The Markov property (what “state” really means)

The Markov property says that the future depends on the past only through the present state:

P(sₜ₊₁ | s₀, a₀, …, sₜ, aₜ) = P(sₜ₊₁ | sₜ, aₜ)

Intuition: sₜ must contain **all decision-relevant information** from history.

This is not always true for raw observations (e.g., pixels). In practice, RL often deals with partial observability, but this intro node focuses on the MDP setting.

### Rewards vs. goals

Rewards are a design choice (or a measurement) that encodes what we want. A reward is not the same as a goal:

- •A **goal** might be “win the game.”
- •A **reward** might be +1 for winning, 0 otherwise.

Reward shaping can make learning easier but can also change the optimal behavior if done carelessly.

### Return: what RL actually maximizes

Immediate reward is not enough because actions can have long-term effects. We define the **return** from time t:

Gₜ = rₜ₊₁ + γ rₜ₊₂ + γ² rₜ₊₃ + … = ∑\_{k=0}^{∞} γ^k rₜ₊₁₊k

- •γ close to 0 emphasizes immediate rewards.
- •γ close to 1 emphasizes long-term rewards.

Why discounting helps:

- •mathematically: makes infinite sums finite under mild conditions
- •practically: encodes preference for sooner rewards and reduces variance

### Trajectories and expectations

A trajectory is a random sequence:

s₀, a₀, r₁, s₁, a₁, r₂, s₂, …

Given a policy π(a | s) and dynamics P(s′ | s, a), the return Gₜ becomes a random variable. RL optimizes an **expected** return:

J(π) = Eπ[ G₀ ]

The expectation Eπ[·] is taken over:

- •actions drawn from π(a | s)
- •next states drawn from P(s′ | s, a)
- •rewards drawn from the reward distribution (if stochastic)

### From policy to induced Markov chain

With a fixed policy π, the probability of transitioning from state s to s′ becomes:

Pπ(s′ | s) = ∑\_{a∈A} π(a | s) P(s′ | s, a)

This is exactly a Markov chain transition rule—so your Markov chain knowledge applies.

### Deterministic vs stochastic policies

A policy can be:

- •**Deterministic:** a = μ(s) (always choose the same action in s)
- •**Stochastic:** π(a | s) gives probabilities

Stochastic policies matter because:

- •exploration: you sometimes need randomness to discover better outcomes
- •optimality: in some MDPs (especially with partial observability or certain constraints), stochasticity can be beneficial

### A concrete mini-example: “two routes”

Imagine a commute with two actions:

- •a = Safe: always get reward 1
- •a = Risky: get reward 3 with probability 0.5, else reward 0

If this were a one-step problem, you’d compare expected reward:

E[Risky] = 0.5·3 + 0.5·0 = 1.5, so Risky is better.

But with state transitions and long horizons, the best choice depends on how today’s action changes tomorrow’s state distribution. That’s the RL leap from bandits to MDPs.

### What you should internalize

MDP thinking is a discipline:

- •Clearly separate **what you control** (actions via π)
- •From **what you don’t** (P and reward stochasticity)
- •And define success as **expected return** over time

## Core Mechanic 2: Policies and Value Functions — Measuring Long-Run Desirability

### Why value functions are the central tool

The agent’s goal is global: maximize expected return over a long horizon.

But decision-making is local: at state s, you must pick an action now.

A **value function** bridges this gap by summarizing the long-term consequences of being in a state or taking an action.

### State-value and action-value

Given a policy π:

**State-value function** (how good is state s under π?):

Vπ(s) = Eπ[ Gₜ | sₜ = s ]

**Action-value function** (how good is taking action a in s under π?):

Qπ(s, a) = Eπ[ Gₜ | sₜ = s, aₜ = a ]

These expectations are over future actions from π and transitions from P.

### The “one-step lookahead” idea

Start from the definition of return:

Gₜ = rₜ₊₁ + γ Gₜ₊₁

Now take expectations to relate values across time.

#### Deriving the Bellman expectation equation for Vπ

By definition:

Vπ(s) = Eπ[ Gₜ | sₜ = s ]

Substitute Gₜ = rₜ₊₁ + γ Gₜ₊₁:

Vπ(s)

= Eπ[ rₜ₊₁ + γ Gₜ₊₁ | sₜ = s ]

= Eπ[ rₜ₊₁ | sₜ = s ] + γ Eπ[ Gₜ₊₁ | sₜ = s ]

But Gₜ₊₁ depends on sₜ₊₁, and future actions follow π, so:

Eπ[ Gₜ₊₁ | sₜ = s ] = Eπ[ Vπ(sₜ₊₁) | sₜ = s ]

So:

Vπ(s) = Eπ[ rₜ₊₁ + γ Vπ(sₜ₊₁) | sₜ = s ]

Write the expectation explicitly over actions and next states:

Vπ(s) = ∑\_{a∈A} π(a | s) ∑\_{s′∈S} P(s′ | s, a) [ r(s, a, s′) + γ Vπ(s′) ]

This is a **Bellman expectation equation**: a self-consistency condition.

#### Bellman expectation equation for Qπ

Similarly:

Qπ(s, a) = ∑\_{s′} P(s′ | s, a) [ r(s, a, s′) + γ ∑\_{a′} π(a′ | s′) Qπ(s′, a′) ]

Interpretation:

- •choose a
- •environment moves to s′ and gives reward
- •then you continue following π

### Advantage: comparing actions in the same state

Often you care about which action is better than the policy’s average behavior.

Define the **advantage**:

Aπ(s, a) = Qπ(s, a) − Vπ(s)

- •Aπ(s, a) > 0: better than average under π
- •Aπ(s, a) < 0: worse than average under π

This will matter later when learning policies.

### Optimal value functions (preview)

RL is usually about finding an optimal policy π\*.

Define optimal state value:

V\*(s) = maxπ Vπ(s)

and optimal action value:

Q\*(s, a) = maxπ Qπ(s, a)

These satisfy Bellman **optimality** equations (you’ll go deeper in the MDP node you unlock):

V*(s) = max\_{a} ∑\_{s′} P(s′ | s, a) [ r(s, a, s′) + γ V*(s′) ]

and

Q*(s, a) = ∑\_{s′} P(s′ | s, a) [ r(s, a, s′) + γ max\_{a′} Q*(s′, a′) ]

Important pacing point: you do not need to solve these yet; you need to recognize what they *mean*:

- •**V** answers “How good is this state?”
- •**Q** answers “How good is this action here?”
- •Bellman equations formalize “reward now + value later.”

### Value functions as fixed points

A subtle but powerful view: Bellman equations define a mapping (an operator) whose fixed point is Vπ.

Why that matters later:

- •We can compute values by repeated updates (dynamic programming)
- •Or estimate them from samples (TD learning)

### On-policy vs off-policy (terminology you’ll meet)

- •**On-policy:** evaluate/improve the same policy you use to collect data
- •**Off-policy:** learn about a target policy while behaving differently (e.g., exploratory behavior)

You can already see the need: if π is deterministic and suboptimal, you might never see better actions. Stochasticity and off-policy ideas help address that.

## Application/Connection: From Interaction Data to Better Decisions

### Two big families: planning vs learning

Once you have MDP + value functions, there are two broad approaches.

| Approach | What you assume you know | Main operation | Typical algorithms |
| --- | --- | --- | --- |
| Planning (model-based) | P(s′ | s, a) and reward model | compute values/policies by sweeps | value iteration, policy iteration |
| Learning (model-free) | only samples (s, a, r, s′) | estimate values/policies from experience | TD learning, Q-learning, policy gradients |

This node is an intro, so focus on the *shape* of the problems.

### Exploration vs exploitation (the unavoidable tension)

If you always take the best-known action, you may miss a better one.

If you explore too much, you waste reward.

This tension is sharper in MDPs because:

- •exploration changes which states you visit
- •some rewards are only reachable after sequences of correct actions

A policy π(a | s) that is stochastic can encode exploration directly.

### Credit assignment (why delayed reward is hard)

Suppose reward arrives only at the end of an episode (e.g., win/loss). Which earlier actions deserve credit?

Value functions address this by propagating reward information backward through the Bellman structure:

- •if s′ is valuable, then actions leading to s′ become valuable
- •states leading to those actions become valuable, etc.

### Episodes, continuing tasks, and termination

Some environments have terminal states (games), others run forever (control systems).

- •**Episodic:** return is finite sum until termination
- •**Continuing:** often use discounting γ < 1, or average-reward formulations

In episodic tasks with terminal state s\_T, it’s common to define V(s\_T) = 0 (no future reward after terminal).

### Where vectors show up (a preview of function approximation)

In small MDPs, you can store V(s) in a table.

But real problems have huge state spaces. Then we approximate:

- •V(s) ≈ V(s; **w**) where **w** is a parameter vector
- •π(a | s) ≈ π(a | s; **θ**)

Even though this node is conceptual, it helps to see why vectors matter:

- •learning becomes optimization over **w** or **θ**
- •generalization becomes crucial

### Connection to the next node: Markov Decision Processes

This intro has emphasized *what* the objects are:

- •MDP components (S, A, P, R, γ)
- •policies π(a | s)
- •values Vπ and Qπ

The next node will go deeper on:

- •Bellman equations as linear systems / fixed points
- •how to solve for Vπ given π and P
- •how to compute optimal policies

Think of this node as learning the language and the “units of thought” you’ll use later.

## Worked Examples (3)

### Evaluate a simple policy in a 2-state MDP (compute Vπ by solving equations)

States: S = {A, B}. Actions: in each state you may choose Left or Right.

Discount: γ = 0.9.

Transitions and rewards:

- •From A:
- •Left: go to A with prob 1, reward 0
- •Right: go to B with prob 1, reward 1
- •From B:
- •Left: go to A with prob 1, reward 0
- •Right: go to B with prob 1, reward 2

Policy π is stochastic:

- •At A: π(Right | A) = 0.5, π(Left | A) = 0.5
- •At B: π(Right | B) = 1, π(Left | B) = 0

Compute Vπ(A) and Vπ(B).

1. Write Bellman expectation equations:

   Vπ(A) = ∑\_{a} π(a | A) [ r(A,a) + γ Vπ(s′) ]

   Vπ(B) = ∑\_{a} π(a | B) [ r(B,a) + γ Vπ(s′) ]
2. Expand Vπ(A).

   At A:

   - •Left: reward 0, next A
   - •Right: reward 1, next B

   So:

   Vπ(A)

   = 0.5 [ 0 + 0.9 Vπ(A) ] + 0.5 [ 1 + 0.9 Vπ(B) ]
3. Expand Vπ(B).

   At B policy always chooses Right.

   - •Right from B: reward 2, next B

   So:

   Vπ(B) = 1 · [ 2 + 0.9 Vπ(B) ]
4. Solve for Vπ(B):

   Vπ(B) = 2 + 0.9 Vπ(B)

   Vπ(B) − 0.9 Vπ(B) = 2

   0.1 Vπ(B) = 2

   Vπ(B) = 20
5. Plug Vπ(B)=20 into Vπ(A):

   Vπ(A) = 0.5(0.9 Vπ(A)) + 0.5(1 + 0.9·20)

   Vπ(A) = 0.45 Vπ(A) + 0.5(1 + 18)

   Vπ(A) = 0.45 Vπ(A) + 0.5·19

   Vπ(A) = 0.45 Vπ(A) + 9.5
6. Solve for Vπ(A):

   Vπ(A) − 0.45 Vπ(A) = 9.5

   0.55 Vπ(A) = 9.5

   Vπ(A) = 9.5 / 0.55 = 17.2727… ≈ 17.27

**Insight:** This is policy evaluation: once π is fixed, the MDP becomes a Markov reward process, and Vπ is the fixed point of a linear Bellman system. Notice how the high self-loop reward at B (reward 2 forever) dominates both values through discounting.

### Compute Qπ(s, a) and advantage Aπ(s, a) in the same MDP

Use the MDP and Vπ values from the previous example (Vπ(A) ≈ 17.27, Vπ(B)=20). Compute:

1) Qπ(A, Left), Qπ(A, Right)

2) Aπ(A, Left), Aπ(A, Right)

Assume rewards depend only on (s, a) here: r(A,Left)=0, r(A,Right)=1, r(B,Left)=0, r(B,Right)=2.

1. Use the definition:

   Qπ(s, a) = ∑\_{s′} P(s′ | s, a) [ r(s,a) + γ Vπ(s′) ]

   Because transitions are deterministic here, the sum over s′ collapses to the single next state.
2. Compute Qπ(A, Left).

   Left from A → A with reward 0.

   Qπ(A, Left) = 0 + 0.9 Vπ(A)

   = 0.9 · 17.2727…

   = 15.5454… ≈ 15.55
3. Compute Qπ(A, Right).

   Right from A → B with reward 1.

   Qπ(A, Right) = 1 + 0.9 Vπ(B)

   = 1 + 0.9 · 20

   = 1 + 18

   = 19
4. Check consistency with Vπ(A).

   Vπ(A) should equal the policy-weighted average:

   Vπ(A) = 0.5 Qπ(A, Left) + 0.5 Qπ(A, Right)

   = 0.5(15.5454…) + 0.5(19)

   = 7.7727… + 9.5

   = 17.2727… (matches).
5. Compute advantages:

   Aπ(A, Left) = Qπ(A, Left) − Vπ(A)

   = 15.5454… − 17.2727…

   = −1.7273… ≈ −1.73

   Aπ(A, Right) = Qπ(A, Right) − Vπ(A)

   = 19 − 17.2727…

   = 1.7273… ≈ 1.73

**Insight:** Qπ separates action quality within a state. Vπ is the policy’s average outcome; advantage tells you which actions are better or worse than what π typically does. Policy improvement methods often push probability mass toward positive-advantage actions.

### From a stochastic policy to an induced Markov chain Pπ(s′ | s)

Consider a 3-state MDP with states S = {0, 1, 2} and actions A = {a, b}.

Policy:

- •π(a | 0)=0.2, π(b | 0)=0.8
- •π(a | 1)=0.6, π(b | 1)=0.4
- •π(a | 2)=1, π(b | 2)=0

Transitions:

- •For action a: P(1 | 0,a)=1; P(2 | 1,a)=1; P(2 | 2,a)=1
- •For action b: P(2 | 0,b)=1; P(0 | 1,b)=1; P(1 | 2,b)=1

Compute Pπ(s′ | s).

1. Use the mixture rule:

   Pπ(s′ | s) = ∑\_{action∈{a,b}} π(action | s) P(s′ | s, action)
2. From s=0:

   - •If action a (prob 0.2): next is 1
   - •If action b (prob 0.8): next is 2

   So:

   Pπ(1 | 0)=0.2, Pπ(2 | 0)=0.8, Pπ(0 | 0)=0
3. From s=1:

   - •If action a (prob 0.6): next is 2
   - •If action b (prob 0.4): next is 0

   So:

   Pπ(2 | 1)=0.6, Pπ(0 | 1)=0.4, Pπ(1 | 1)=0
4. From s=2:

   π(a|2)=1 so always take a, next is 2.

   So:

   Pπ(2 | 2)=1, Pπ(0 | 2)=0, Pπ(1 | 2)=0
5. Write the induced transition matrix with state order (0,1,2):

   Pπ =

   [ Pπ(0|0) Pπ(1|0) Pπ(2|0)

   Pπ(0|1) Pπ(1|1) Pπ(2|1)

   Pπ(0|2) Pπ(1|2) Pπ(2|2) ]

   =

   [ 0 0.2 0.8

   0.4 0 0.6

   0 0 1 ]

**Insight:** Fixing π collapses control into randomness: the MDP becomes a Markov chain over states with transition matrix Pπ. This is the key bridge from Markov chains to RL—actions disappear into the policy probabilities.

## Key Takeaways

- ✓

  RL is learning to choose actions to maximize **expected return** from interaction, not from labeled examples.
- ✓

  An MDP formalizes sequential decision-making with states s, actions a, transitions P(s′ | s, a), rewards, and discount γ.
- ✓

  A policy π(a | s) can be deterministic or stochastic; with fixed π, the state dynamics become an induced Markov chain Pπ(s′ | s).
- ✓

  The discounted return is Gₜ = ∑\_{k=0}^{∞} γ^k rₜ₊₁₊k, capturing delayed consequences and making infinite horizons manageable.
- ✓

  Value functions Vπ(s) and Qπ(s, a) measure long-run desirability under π and satisfy Bellman expectation equations.
- ✓

  Bellman equations encode the core recursion: value = (reward now) + γ·(value later), averaged over policy and dynamics.
- ✓

  Advantage Aπ(s, a) = Qπ(s, a) − Vπ(s) compares actions within a state and foreshadows policy improvement.
- ✓

  Planning assumes you know P and rewards; model-free learning estimates values/policies from sampled transitions.

## Common Mistakes

- ✗

  Confusing the **reward** rₜ with the **return** Gₜ: RL optimizes expected return, not immediate reward alone.
- ✗

  Treating observations as states without checking the Markov property (missing hidden information breaks MDP assumptions).
- ✗

  Forgetting that expectations are over both the environment randomness P(s′ | s, a) and the policy randomness π(a | s).
- ✗

  Mixing up Vπ(s) and Qπ(s, a): V is state quality under π; Q is action quality in a state under π.

## Practice

easy

A one-state continuing task has a single state s and two actions a₁, a₂. Taking a₁ gives reward 1 and returns to s. Taking a₂ gives reward 2 and returns to s. Discount γ = 0.5. (i) Compute Vπ(s) if π chooses a₁ with prob 0.7 and a₂ with prob 0.3. (ii) Compute Qπ(s, a₁) and Qπ(s, a₂).

**Hint:** With one state, Vπ(s) must satisfy V = E[r] + γV. And Q(s,a) = r(a) + γV.

Show solution

Compute expected immediate reward:

E[r] = 0.7·1 + 0.3·2 = 0.7 + 0.6 = 1.3

Solve V = 1.3 + 0.5V ⇒ 0.5V = 1.3 ⇒ V = 2.6.

Then:

Qπ(s,a₁) = 1 + 0.5·2.6 = 1 + 1.3 = 2.3

Qπ(s,a₂) = 2 + 0.5·2.6 = 2 + 1.3 = 3.3

medium

Consider an episodic MDP with terminal state T where Vπ(T)=0. From state S, action Go deterministically transitions to T with reward 5. Action Stay deterministically transitions to S with reward 1. Discount γ=0.9. (i) Compute Qπ(S,Go) and Qπ(S,Stay) in terms of Vπ(S). (ii) If π always chooses Stay, solve for Vπ(S).

**Hint:** Use Qπ(s,a) = r + γVπ(s′). If π always Stay, then Vπ(S)=Qπ(S,Stay).

Show solution

(i)

Go: next T, so Qπ(S,Go) = 5 + 0.9·Vπ(T) = 5 + 0 = 5.

Stay: next S, so Qπ(S,Stay) = 1 + 0.9·Vπ(S).

(ii) If π always chooses Stay, then Vπ(S) = Qπ(S,Stay) = 1 + 0.9Vπ(S).

So Vπ(S) − 0.9Vπ(S) = 1 ⇒ 0.1Vπ(S)=1 ⇒ Vπ(S)=10.

hard

You are given a policy π and dynamics P(s′ | s, a) for a finite MDP. Describe how to compute the induced Markov chain transition matrix Pπ(s′ | s). Then explain (in 2–4 sentences) why this shows that policy evaluation is closely related to Markov chains.

**Hint:** Pπ is a policy-weighted mixture of action-conditioned transitions. Under a fixed π, actions are random variables determined by s.

Show solution

To compute Pπ(s′ | s), combine transitions across actions using the policy probabilities:

Pπ(s′ | s) = ∑\_{a∈A} π(a | s) P(s′ | s, a).

This defines a Markov chain over states because the next-state distribution depends only on the current state s (via the mixture), not on earlier history. Therefore, once π is fixed, state visitation and long-run behavior can be analyzed with Markov chain tools, and value functions become expectations over trajectories of that induced chain with rewards.

## Connections

Unlocks: [Markov Decision Processes](/tech-tree/mdp/)

Related next steps:

- •[Dynamic Programming for RL](/tech-tree/dp-rl/)
- •[Temporal Difference Learning](/tech-tree/td-learning/)
- •[Q-Learning](/tech-tree/q-learning/)
- •[Policy Gradients](/tech-tree/policy-gradients/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
