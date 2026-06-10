---
title: Policy Gradient Methods
description: Direct policy optimization. REINFORCE, actor-critic.
date: '2026-07-01'
scheduled: '2026-11-27'
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
inspiration_url: https://templeton.host/tech-tree/policy-gradient/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/policy-gradient/](https://templeton.host/tech-tree/policy-gradient/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Policy Gradient Methods

Machine LearningDifficulty: ★★★★★Depth: 9Unlocks: 1

Direct policy optimization. REINFORCE, actor-critic.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Parameterized stochastic policy as a differentiable mapping (pi\_theta(a|s)) that defines behavior and can be optimized
- -Objective is the expected (discounted) return J(theta) = E[sum of rewards under the policy]
- -Policy gradient theorem (score-function estimator): provides an unbiased, sample-based expression for the gradient of J(theta) enabling direct optimization

## Key Symbols & Notation

pi\_theta(a|s) (parameterized stochastic policy)J(theta) (expected return objective)

## Essential Relationships

- -grad\_theta J(theta) = E\_{trajectories~pi\_theta}[grad\_theta log pi\_theta(a|s) \* (return or advantage)] (policy gradient theorem; forms the basis for REINFORCE and actor-critic)

## Prerequisites (2)

[Markov Decision Processes6 atoms](/tech-tree/mdp/)[Stochastic Gradient Descent5 atoms](/tech-tree/sgd/)

## Unlocks (1)

[RLHFlvl 5](/tech-tree/rlhf/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[trading ordersBusiness

Policy gradient methods are the standard RL technique for continuous action spaces; they output parameterized distributions over actions (e.g., Gaussian over order size and limit price), making them the direct method for learning trading order policies](/business/trading-orders/)

Advanced Learning Details

### Graph Position

195

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

9

Chain Length

### Cognitive Load

6

Atomic Elements

43

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (16)

- - parameterized stochastic policy: π\_θ(a|s) - policy represented by parameters θ that outputs action distributions
- - policy objective J(θ): expected (discounted) return under π\_θ treated as a function of θ
- - trajectory τ: sequence (s0,a0,r0,s1,a1,r1,...) sampled from π\_θ
- - return G\_t: the (discounted) sum of future rewards from time t used as a Monte Carlo target
- - score-function / likelihood-ratio estimator: using ∇\_θ log p\_θ(·) to move gradient inside expectation
- - policy gradient theorem: closed-form expectation expression for ∇\_θ J(θ) in terms of π\_θ and value/Q
- - REINFORCE: Monte Carlo policy-gradient algorithm that uses sampled returns as unbiased gradient estimates
- - baseline for variance reduction: any function b(s) subtracted from the return that does not bias the gradient
- - advantage function A^π(s,a) = Q^π(s,a) − V^π(s) used to center policy updates
- - actor-critic architecture: 'actor' updates π\_θ, 'critic' learns a value (or Q) estimator to provide targets/advantages
- - TD error δ\_t = r\_t + γ V(s\_{t+1}) − V(s\_t) as a bootstrapped estimate usable by the actor
- - bootstrapping vs Monte Carlo tradeoff: bootstrapped (TD) estimates introduce bias but reduce variance; MC is unbiased but high variance
- - on-policy sampling requirement: gradients/estimators assume trajectories sampled from the current policy (π\_θ)
- - variance–bias tradeoff in gradient estimation and the role of baselines/critics to manage it
- - entropy regularization (optional): adding policy entropy to the objective to encourage exploration
- - importance-sampling correction (off-policy): reweighting samples by π/μ to use data from a behavior policy (introduces high variance)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Value-based RL learns “how good states/actions are,” then acts greedily. Policy gradient methods flip that: they directly learn “how to act” by adjusting a differentiable, stochastic policy πθ(a|s) to increase expected return—using gradients estimated from sampled trajectories.

TL;DR:

Policy gradients optimize J(θ)=Eτ[∑γᵗrₜ] directly by ascending an unbiased gradient estimator: ∇θJ(θ)=E[∑∇θ log πθ(aₜ|sₜ)·(return/advantage)]. REINFORCE uses Monte Carlo returns (high variance). Actor-critic replaces returns with learned value baselines (lower variance) and uses advantages (A=Q−V), often with bootstrapping and GAE.

## What Is a Policy Gradient Method?

### Why this family exists

In an MDP, you ultimately care about *behavior*: which actions you take in each state. A **policy** is the object that produces that behavior. In **policy gradient** methods, the policy is **parameterized** and **differentiable**, so we can change it continuously and aim those changes toward higher return.

Instead of learning a value function first and deriving a policy from it, we optimize a policy **directly**:

- •Policy: πθ(a∣s)\pi\_\theta(a\mid s)πθ​(a∣s), a distribution over actions given a state.
- •Objective: expected discounted return under that policy.

A standard episodic objective is

J(θ)  =  Eτ∼πθ[∑t=0T−1γtrt]J(\theta) \;=\; \mathbb{E}\_{\tau\sim \pi\_\theta}\left[\sum\_{t=0}^{T-1} \gamma^t r\_t\right]J(θ)=Eτ∼πθ​​[t=0∑T−1​γtrt​]

where a trajectory (rollout) is

τ=(s0,a0,r0,s1,a1,r1,… )\tau = (s\_0,a\_0,r\_0,s\_1,a\_1,r\_1,\dots)τ=(s0​,a0​,r0​,s1​,a1​,r1​,…)

and the trajectory distribution is induced by the environment dynamics and the policy:

Pθ(τ)=ρ(s0)∏t=0T−1πθ(at∣st) P(st+1∣st,at)P\_\theta(\tau) = \rho(s\_0)\prod\_{t=0}^{T-1}\pi\_\theta(a\_t\mid s\_t)\,P(s\_{t+1}\mid s\_t,a\_t)Pθ​(τ)=ρ(s0​)t=0∏T−1​πθ​(at​∣st​)P(st+1​∣st​,at​)

The key point: **θ controls the probability of your actions**, and that changes which states you visit and which rewards you obtain.

### What “differentiable policy” means in practice

Typically, θ parameterizes a neural network that outputs either:

- •**Discrete actions**: logits → softmax → categorical distribution.
- •**Continuous actions**: mean (and maybe log-std) of a Gaussian.

Example (discrete):

πθ(a∣s)=softmax(fθ(s))a\pi\_\theta(a\mid s)=\mathrm{softmax}(f\_\theta(s))\_aπθ​(a∣s)=softmax(fθ​(s))a​

Example (continuous, diagonal Gaussian):

πθ(a∣s)=N(a ; μθ(s),diag(σθ(s)2))\pi\_\theta(a\mid s)=\mathcal{N}(a\,;\,\mu\_\theta(s),\mathrm{diag}(\sigma\_\theta(s)^2))πθ​(a∣s)=N(a;μθ​(s),diag(σθ​(s)2))

We then perform **stochastic gradient ascent** on J(θ)J(\theta)J(θ):

θ←θ+α ∇θJ(θ)^\theta \leftarrow \theta + \alpha\,\widehat{\nabla\_\theta J(\theta)}θ←θ+α∇θ​J(θ)​

### The conceptual leap: “credit assignment” through log-probability

In supervised learning, you get a target label. In RL, you get rewards *after* decisions. The policy gradient trick ties the final outcome back to earlier action probabilities via

- •how probable the action was (log⁡πθ(a∣s)\log \pi\_\theta(a\mid s)logπθ​(a∣s)), and
- •how good the outcome was (returns or advantages).

Intuition to hold onto:

> If an action led to better-than-expected outcomes, increase its probability in that state. If it led to worse-than-expected outcomes, decrease it.

Policy gradient methods operationalize that intuition with a precise gradient estimator.

### Visualization plan (interactive canvas)

To make this idea tangible, your canvas can show a tiny 2-state MDP and a 2-action policy.

**Canvas panel A: “Policy sliders”**

- •Let θ be a single scalar controlling a Bernoulli policy:
- •πθ(a=1∣s)=σ(θs)\pi\_\theta(a=1\mid s)=\sigma(\theta\_s)πθ​(a=1∣s)=σ(θs​) for each state s.
- •Show two sliders (θ for state 0 and state 1).
- •As the learner drags θ, animate action probabilities (bar chart) shifting.

**Canvas panel B: “Trajectory outcomes”**

- •Sample rollouts under the current policy.
- •Show the returns GtG\_tGt​ next to each time step.

**Canvas panel C: “Gradient arrows”**

- •For each visited (sₜ,aₜ), display
- •∇θlog⁡πθ(at∣st)\nabla\_\theta \log \pi\_\theta(a\_t\mid s\_t)∇θ​logπθ​(at​∣st​) as an arrow on θ.
- •Multiply the arrow by an advantage estimate and show the scaled update.

This directly externalizes the algebra: gradient = (score) × (signal).

## Core Mechanic 1: The Policy Gradient Theorem (REINFORCE via the Score Function)

### Why we need a special gradient identity

We want ∇θJ(θ)\nabla\_\theta J(\theta)∇θ​J(θ), but JJJ is an expectation over trajectories whose distribution depends on θ. Differentiating “through” sampling is awkward because trajectories are discrete random objects.

The **score-function** (a.k.a. log-derivative) trick gives a way to move the gradient inside an expectation without differentiating the environment dynamics.

The identity to remember:

∇θEx∼pθ[f(x)]=Ex∼pθ[f(x)∇θlog⁡pθ(x)]\nabla\_\theta \mathbb{E}\_{x\sim p\_\theta}[f(x)]
= \mathbb{E}\_{x\sim p\_\theta}\left[f(x)\nabla\_\theta \log p\_\theta(x)\right]∇θ​Ex∼pθ​​[f(x)]=Ex∼pθ​​[f(x)∇θ​logpθ​(x)]

This works whenever pθ(x)p\_\theta(x)pθ​(x) is differentiable in θ and f(x)f(x)f(x) is integrable.

### Derivation (showing the work)

Start from:

J(θ)=∑τPθ(τ) R(τ)J(\theta)=\sum\_\tau P\_\theta(\tau)\,R(\tau)J(θ)=τ∑​Pθ​(τ)R(τ)

where R(τ)=∑t=0T−1γtrtR(\tau)=\sum\_{t=0}^{T-1}\gamma^t r\_tR(τ)=∑t=0T−1​γtrt​.

Differentiate:

∇θJ(θ)=∑τ∇θPθ(τ) R(τ)\nabla\_\theta J(\theta)
= \sum\_\tau \nabla\_\theta P\_\theta(\tau)\,R(\tau)∇θ​J(θ)=τ∑​∇θ​Pθ​(τ)R(τ)

Use ∇P=P∇log⁡P\nabla P = P\nabla \log P∇P=P∇logP:

∇θJ(θ)=∑τPθ(τ) ∇θlog⁡Pθ(τ) R(τ)\nabla\_\theta J(\theta)
= \sum\_\tau P\_\theta(\tau)\, \nabla\_\theta \log P\_\theta(\tau)\,R(\tau)∇θ​J(θ)=τ∑​Pθ​(τ)∇θ​logPθ​(τ)R(τ)

Recognize the expectation:

∇θJ(θ)=Eτ∼πθ[R(τ) ∇θlog⁡Pθ(τ)]\nabla\_\theta J(\theta)
= \mathbb{E}\_{\tau\sim \pi\_\theta}\left[R(\tau)\,\nabla\_\theta \log P\_\theta(\tau)\right]∇θ​J(θ)=Eτ∼πθ​​[R(τ)∇θ​logPθ​(τ)]

Now expand log⁡Pθ(τ)\log P\_\theta(\tau)logPθ​(τ). From

Pθ(τ)=ρ(s0)∏t=0T−1πθ(at∣st) P(st+1∣st,at)P\_\theta(\tau) = \rho(s\_0)\prod\_{t=0}^{T-1}\pi\_\theta(a\_t\mid s\_t)\,P(s\_{t+1}\mid s\_t,a\_t)Pθ​(τ)=ρ(s0​)t=0∏T−1​πθ​(at​∣st​)P(st+1​∣st​,at​)

take logs:

log⁡Pθ(τ)=log⁡ρ(s0)+∑t=0T−1log⁡πθ(at∣st)+∑t=0T−1log⁡P(st+1∣st,at)\log P\_\theta(\tau)
= \log \rho(s\_0) + \sum\_{t=0}^{T-1}\log \pi\_\theta(a\_t\mid s\_t) + \sum\_{t=0}^{T-1}\log P(s\_{t+1}\mid s\_t,a\_t)logPθ​(τ)=logρ(s0​)+t=0∑T−1​logπθ​(at​∣st​)+t=0∑T−1​logP(st+1​∣st​,at​)

Differentiate w.r.t. θ. Only the policy terms depend on θ (environment dynamics are fixed):

∇θlog⁡Pθ(τ)=∑t=0T−1∇θlog⁡πθ(at∣st)\nabla\_\theta \log P\_\theta(\tau)
= \sum\_{t=0}^{T-1}\nabla\_\theta \log \pi\_\theta(a\_t\mid s\_t)∇θ​logPθ​(τ)=t=0∑T−1​∇θ​logπθ​(at​∣st​)

So:

∇θJ(θ)=Eτ[R(τ)∑t=0T−1∇θlog⁡πθ(at∣st)]\nabla\_\theta J(\theta)
= \mathbb{E}\_{\tau}\left[R(\tau)\sum\_{t=0}^{T-1}\nabla\_\theta \log \pi\_\theta(a\_t\mid s\_t)\right]∇θ​J(θ)=Eτ​[R(τ)t=0∑T−1​∇θ​logπθ​(at​∣st​)]

This already yields an unbiased estimator: sample a trajectory, compute R(τ)R(\tau)R(τ), and push the log-prob gradients in the direction of R(τ)R(\tau)R(τ).

### Reward-to-go (better credit assignment)

Using the same return R(τ)R(\tau)R(τ) for every time step credits early and late actions equally, even though late actions cannot affect early rewards.

A standard improvement is the **reward-to-go**:

Gt=∑k=tT−1γk−trkG\_t=\sum\_{k=t}^{T-1}\gamma^{k-t}r\_kGt​=k=t∑T−1​γk−trk​

Then the estimator becomes:

∇θJ(θ)=E[∑t=0T−1∇θlog⁡πθ(at∣st) Gt]\nabla\_\theta J(\theta)
= \mathbb{E}\left[\sum\_{t=0}^{T-1}\nabla\_\theta\log\pi\_\theta(a\_t\mid s\_t)\,G\_t\right]∇θ​J(θ)=E[t=0∑T−1​∇θ​logπθ​(at​∣st​)Gt​]

This is still unbiased, but typically has lower variance.

### REINFORCE algorithm (Monte Carlo policy gradient)

At a high level:

1. 1)Collect trajectories using current πθ\pi\_\thetaπθ​.
2. 2)For each time step, compute GtG\_tGt​.
3. 3)Update θ by ascending the sampled gradient.

A common minibatch form:

∇θJ^=1N∑i=1N∑t=0Ti−1∇θlog⁡πθ(at(i)∣st(i)) Gt(i)\widehat{\nabla\_\theta J} = \frac{1}{N}\sum\_{i=1}^N\sum\_{t=0}^{T\_i-1}\nabla\_\theta\log\pi\_\theta(a\_t^{(i)}\mid s\_t^{(i)})\,G\_t^{(i)}∇θ​J​=N1​i=1∑N​t=0∑Ti​−1​∇θ​logπθ​(at(i)​∣st(i)​)Gt(i)​

### The geometry of the update (what the gradient *does*)

For a softmax policy, you can interpret ∇θlog⁡π\nabla\_\theta\log\pi∇θ​logπ as:

- •increasing parameters that make the taken action more likely,
- •decreasing parameters that make competing actions likely.

Then multiplying by GtG\_tGt​ decides **direction**:

- •If GtG\_tGt​ is large (good), increase probability of those actions.
- •If GtG\_tGt​ is small/negative (bad), decrease probability.

### Visualization: “Score × Return” microscope

Add a per-time-step breakdown:

- •Display log⁡πθ(at∣st)\log\pi\_\theta(a\_t\mid s\_t)logπθ​(at​∣st​).
- •Show ∇θlog⁡πθ(at∣st)\nabla\_\theta\log\pi\_\theta(a\_t\mid s\_t)∇θ​logπθ​(at​∣st​) as a vector arrow (or scalar bar if θ is 1D).
- •Multiply by GtG\_tGt​ and animate the resulting parameter step.

Learners should *see* that the policy gradient update is not magic—it’s a weighted push on log-probability.

## Core Mechanic 2: Variance Reduction — Baselines, Advantages, and Actor-Critic

### Why REINFORCE struggles

REINFORCE is unbiased, but its Monte Carlo returns can have enormous variance:

- •randomness in the environment,
- •randomness in the policy,
- •long horizons with discounting.

High variance means you need many trajectories (or tiny learning rates) to make stable progress.

The central theme of modern policy gradients is:

> Keep the estimator (approximately) unbiased while reducing variance.

### Baselines: subtract something that doesn’t change the expectation

Key fact: for any function b(st)b(s\_t)b(st​) that does not depend on ata\_tat​,

Eat∼πθ(⋅∣st)[∇θlog⁡πθ(at∣st) b(st)]=0\mathbb{E}\_{a\_t\sim \pi\_\theta(\cdot\mid s\_t)}\left[\nabla\_\theta\log\pi\_\theta(a\_t\mid s\_t)\,b(s\_t)\right]=0Eat​∼πθ​(⋅∣st​)​[∇θ​logπθ​(at​∣st​)b(st​)]=0

So we can subtract b(st)b(s\_t)b(st​) inside the gradient estimator without changing its expectation:

∇θJ(θ)=E[∑t∇θlog⁡πθ(at∣st) (Gt−b(st))]\nabla\_\theta J(\theta)=\mathbb{E}\left[\sum\_t \nabla\_\theta\log\pi\_\theta(a\_t\mid s\_t)\,(G\_t - b(s\_t))\right]∇θ​J(θ)=E[t∑​∇θ​logπθ​(at​∣st​)(Gt​−b(st​))]

This can drastically reduce variance when b(st)b(s\_t)b(st​) approximates the “typical” return from sts\_tst​.

### The most useful baseline: the value function

Choose b(st)=Vπ(st)b(s\_t)=V^\pi(s\_t)b(st​)=Vπ(st​), where

Vπ(s)=E[∑k=0∞γkrt+k∣st=s]V^\pi(s)=\mathbb{E}\left[\sum\_{k=0}^{\infty}\gamma^k r\_{t+k}\mid s\_t=s\right]Vπ(s)=E[k=0∑∞​γkrt+k​∣st​=s]

Then Gt−Vπ(st)G\_t - V^\pi(s\_t)Gt​−Vπ(st​) is an estimate of the **advantage**:

Aπ(st,at)=Qπ(st,at)−Vπ(st)A^\pi(s\_t,a\_t)=Q^\pi(s\_t,a\_t)-V^\pi(s\_t)Aπ(st​,at​)=Qπ(st​,at​)−Vπ(st​)

Advantage answers a very specific question:

> Was this action better or worse than my policy’s average behavior in this state?

This is exactly the signal you want for improving a stochastic policy.

### Actor-critic: two function approximators with different jobs

Actor-critic methods maintain:

- •**Actor**: the policy πθ(a∣s)\pi\_\theta(a\mid s)πθ​(a∣s) (parameters θ)
- •**Critic**: a value function estimate Vϕ(s)V\_\phi(s)Vϕ​(s) or action-value Qϕ(s,a)Q\_\phi(s,a)Qϕ​(s,a) (parameters φ)

The critic provides a low-variance learning signal; the actor uses it to update the policy.

A common actor update uses an estimated advantage A^t\widehat{A}\_tAt​:

∇θJ^=E[∑t∇θlog⁡πθ(at∣st) A^t]\widehat{\nabla\_\theta J} = \mathbb{E}\left[\sum\_t \nabla\_\theta\log\pi\_\theta(a\_t\mid s\_t)\,\widehat{A}\_t\right]∇θ​J​=E[t∑​∇θ​logπθ​(at​∣st​)At​]

### Bootstrapping: trading bias for lower variance

Instead of Monte Carlo GtG\_tGt​, we can use TD-style targets.

One-step TD error (for value critic):

δt=rt+γVϕ(st+1)−Vϕ(st)\delta\_t = r\_t + \gamma V\_\phi(s\_{t+1}) - V\_\phi(s\_t)δt​=rt​+γVϕ​(st+1​)−Vϕ​(st​)

A simple advantage estimate is A^t=δt\widehat{A}\_t=\delta\_tAt​=δt​.

This introduces some bias (because VϕV\_\phiVϕ​ is approximate), but variance often drops dramatically and learning becomes faster.

### Generalized Advantage Estimation (GAE)

GAE blends multi-step TD errors with an additional parameter λ that controls bias/variance.

Define TD residuals δt\delta\_tδt​ as above, then

A^tGAE(γ,λ)=∑l=0∞(γλ)l δt+l\widehat{A}\_t^{\text{GAE}(\gamma,\lambda)} = \sum\_{l=0}^{\infty}(\gamma\lambda)^l\,\delta\_{t+l}AtGAE(γ,λ)​=l=0∑∞​(γλ)lδt+l​

- •λ = 0: very low variance, more bias (pure 1-step TD)
- •λ → 1: less bias, more variance (approaches Monte Carlo advantage)

### Critic learning objective

If the critic is a value function Vϕ(s)V\_\phi(s)Vϕ​(s), a typical squared-error loss is:

LV(ϕ)=E[(Vϕ(st)−V^t)2]\mathcal{L}\_V(\phi)=\mathbb{E}\left[\left(V\_\phi(s\_t) - \widehat{V}\_t\right)^2\right]LV​(ϕ)=E[(Vϕ​(st​)−Vt​)2]

where V^t\widehat{V}\_tVt​ might be:

- •Monte Carlo return GtG\_tGt​
- •TD target rt+γVϕ(st+1)r\_t + \gamma V\_\phi(s\_{t+1})rt​+γVϕ​(st+1​)
- •λ-return (related to GAE)

### Comparison table (variance and bias intuition)

| Method | Signal used in actor update | Bias | Variance | Typical use |
| --- | --- | --- | --- | --- |
| REINFORCE | GtG\_tGt​ | low (unbiased) | high | small problems, pedagogical baseline |
| REINFORCE + baseline | Gt−b(st)G\_t - b(s\_t)Gt​−b(st​) | low | medium | still Monte Carlo but improved |
| Actor-critic (TD) | δt\delta\_tδt​ or learned AAA | medium | low | common practical choice |
| Actor-critic + GAE | A^tGAE\widehat{A}\_t^{\text{GAE}}AtGAE​ | tunable | tunable | modern on-policy systems (e.g., PPO) |

### Visualization: “Variance comparison panel”

To address the visualization weakness explicitly, build a panel that runs *the same fixed policy* for many rollouts and shows the distribution of gradient estimates.

**Panel design**

- •Fix θ for a small MDP.
- •Sample K trajectories (e.g., K=200) and compute gradient estimates for a chosen parameter component.
- •Plot three histograms (or violin plots):

1. 1)REINFORCE with GtG\_tGt​
2. 2)Baseline with Gt−V(st)G\_t - V(s\_t)Gt​−V(st​)
3. 3)GAE with chosen λ

**What learners should observe**

- •REINFORCE histogram is wide (noisy updates).
- •Baseline narrows distribution around the same mean.
- •GAE can further narrow, depending on λ.

Add a slider for λ (0→1) and animate the histogram tightening/loosening. That makes bias/variance tradeoff visible, not just stated.

## Application/Connection: From Vanilla Policy Gradient to Actor-Critic Systems (and Why This Unlocks RLHF/PPO)

### Why actor-critic is the stepping stone to modern algorithms

Many practical deep RL systems used today (including those in RLHF pipelines) rely on three ideas:

1. 1)**Policy gradient objective** (optimize π directly)
2. 2)**Advantage-based updates** (baseline/value function)
3. 3)**Stabilization constraints** (trust regions, clipping, KL penalties)

This node focuses on (1) and (2), which are foundational for PPO and RLHF.

### A canonical on-policy actor-critic training loop

A common structure (simplified):

1. 1)Collect T steps of experience with current πθ\pi\_\thetaπθ​.
2. 2)Fit VϕV\_\phiVϕ​ to predict returns (or λ-returns).
3. 3)Compute advantages A^t\widehat{A}\_tAt​ (often GAE).
4. 4)Update actor by maximizing:

Lactor(θ)=E[log⁡πθ(at∣st) A^t]\mathcal{L}\_{\text{actor}}(\theta)=\mathbb{E}\left[\log\pi\_\theta(a\_t\mid s\_t)\,\widehat{A}\_t\right]Lactor​(θ)=E[logπθ​(at​∣st​)At​]

Equivalently, minimize −Lactor-\mathcal{L}\_{\text{actor}}−Lactor​.

5. 5)(Often) add an entropy bonus to encourage exploration:

L(θ)=Lactor(θ)+β E[H(πθ(⋅∣st))]\mathcal{L}(\theta)=\mathcal{L}\_{\text{actor}}(\theta) + \beta\,\mathbb{E}[\mathcal{H}(\pi\_\theta(\cdot\mid s\_t))]L(θ)=Lactor​(θ)+βE[H(πθ​(⋅∣st​))]

### Where PPO fits (preview-level connection)

PPO is still a policy gradient method, but it modifies the objective so updates do not change the policy too abruptly.

A typical PPO objective uses the probability ratio

ρt(θ)=πθ(at∣st)πθold(at∣st)\rho\_t(\theta)=\frac{\pi\_\theta(a\_t\mid s\_t)}{\pi\_{\theta\_{\text{old}}}(a\_t\mid s\_t)}ρt​(θ)=πθold​​(at​∣st​)πθ​(at​∣st​)​

and then clips it to avoid overly large updates. Notice how everything here assumes you already understand:

- •πθ(a∣s)\pi\_\theta(a\mid s)πθ​(a∣s) as a differentiable stochastic policy
- •advantage estimates A^t\widehat{A}\_tAt​
- •log-probability gradients (since ratios become differences of logs)

That’s exactly why mastering policy gradients unlocks PPO and thus RLHF.

### RLHF connection (conceptual)

In RLHF, you often:

- •Train a reward model from human preferences.
- •Use an RL algorithm (commonly PPO) to optimize the language model policy to maximize that learned reward, subject to constraints (e.g., KL to a reference model).

Even if the “environment” is text generation and the “reward” comes from a reward model, the policy gradient core remains:

- •actions are tokens,
- •states are partial sequences,
- •∇θlog⁡πθ\nabla\_\theta \log \pi\_\theta∇θ​logπθ​ is computed by backprop through the transformer,
- •advantage estimation stabilizes learning.

### Visualization: “Tiny MDP → PPO-like constraint” (bridge)

Add a simple toggle in the canvas:

- •**Vanilla PG mode**: Δθ∝∇log⁡π⋅A^\Delta\theta \propto \nabla\log\pi \cdot \widehat{A}Δθ∝∇logπ⋅A
- •**Constrained mode** (toy PPO): if the KL between old and new policy exceeds a threshold, scale down the update.

Even if you don’t implement full clipping, just showing “unconstrained step” vs “KL-limited step” prepares learners for PPO’s motivation.

### Summary of what you should be able to do after this node

- •Write down the objective J(θ)J(\theta)J(θ) and the trajectory distribution.
- •Derive/recognize the score-function policy gradient estimator.
- •Implement REINFORCE with reward-to-go.
- •Add a baseline and explain why it doesn’t bias the gradient.
- •Build an actor-critic update with TD/GAE advantages.

Those are the conceptual and mathematical prerequisites for modern on-policy deep RL.

## Worked Examples (3)

### Worked Example 1: REINFORCE on a Tiny 1-State Bandit (Exact Gradient vs Sample Estimate)

Consider a 1-state bandit with two actions a∈{0,1}. Reward is r=1 if a=1, and r=0 if a=0. Let the policy be Bernoulli with parameter p=σ(θ): πθ(a=1)=p, πθ(a=0)=1−p. There is one step per episode, so return R(τ)=r.

Goal: compute ∇θJ(θ) exactly, then match it to the REINFORCE estimator.

1. 1) Write the expected return:

   J(θ)=E[r]=P(a=1)·1 + P(a=0)·0 = p.
2. 2) Differentiate J(θ)=p=σ(θ):

   ∇θJ(θ)=dp/dθ = σ(θ)(1−σ(θ)) = p(1−p).
3. 3) Compute the REINFORCE gradient form:

   ∇θJ(θ)=E[∇θ log πθ(a) · r].

   We will compute ∇θ log πθ(a) for each action.
4. 4) For a=1:

   log πθ(1)=log p.

   ∂/∂θ log p = (1/p)·dp/dθ = (1/p)·p(1−p)=1−p.
5. 5) For a=0:

   log πθ(0)=log(1−p).

   ∂/∂θ log(1−p) = (1/(1−p))·(−dp/dθ) = (1/(1−p))·(−p(1−p))=−p.
6. 6) Take the expectation:

   E[∇θ log πθ(a)·r]

   = P(a=1)·(1−p)·1 + P(a=0)·(−p)·0

   = p(1−p).

   This matches the exact gradient in step (2).
7. 7) Interpretation:

   - •If you sampled a=1 and got r=1, the update uses (1−p) > 0, increasing θ (and thus p).
   - •If you sampled a=0 and got r=0, the update is zero (no learning signal), which is a limitation in sparse reward settings.

**Insight:** This bandit shows the core mechanism cleanly: REINFORCE is an unbiased estimator of the true gradient, and ∇θ log πθ(a) tells you how to change θ to increase the probability of the sampled action.

### Worked Example 2: Baseline Does Not Change the Expected Gradient (But Reduces Variance)

We use the same 1-state Bernoulli bandit as Example 1, but now consider adding a constant baseline b (which is allowed since it does not depend on the action). Show that E[∇θ log πθ(a)·(r−b)] equals the original gradient, for any b.

1. 1) Start with the baseline gradient estimator:

   E[∇θ log πθ(a)·(r−b)] = E[∇θ log πθ(a)·r] − b·E[∇θ log πθ(a)].
2. 2) We already computed E[∇θ log πθ(a)·r] = p(1−p).
3. 3) Now compute E[∇θ log πθ(a)]:

   E[∇θ log πθ(a)]

   = P(a=1)·(1−p) + P(a=0)·(−p)

   = p(1−p) + (1−p)(−p)

   = p(1−p) − p(1−p)

   = 0.
4. 4) Therefore:

   E[∇θ log πθ(a)·(r−b)] = p(1−p) − b·0 = p(1−p).
5. 5) Variance intuition (qualitative):

   Choosing b close to E[r]=p makes (r−b) smaller-magnitude on average, which shrinks the spread of sample gradient values, stabilizing learning.

**Insight:** Baselines work because the expected score function is zero: E[∇θ log πθ(a|s)]=0. You can subtract any action-independent term to reduce variance without biasing the gradient.

### Worked Example 3: Actor-Critic with TD Advantage on a Two-Step Episode

Consider an episodic problem with two time steps t=0,1 and discount γ. You collect one trajectory (s0,a0,r0,s1,a1,r1,terminal). You have a value critic Vφ(s) that outputs V0=Vφ(s0) and V1=Vφ(s1). Construct the TD residuals δ0, δ1 and a simple advantage estimate, then write the actor update direction.

1. 1) One-step TD residual at t=1 (terminal next state):

   Because the episode ends after r1, we treat Vφ(s2)=0.

   δ1 = r1 + γ·0 − V1 = r1 − V1.
2. 2) One-step TD residual at t=0:

   δ0 = r0 + γ V1 − V0.
3. 3) Use δt as an advantage estimate:

   Â1 = δ1,

   Â0 = δ0.
4. 4) Write the sampled policy gradient (one trajectory):

   ĝ = ∇θ log πθ(a0|s0)·Â0 + ∇θ log πθ(a1|s1)·Â1.
5. 5) Interpret signs:

   - •If δ0>0, the outcome from s0 was better than V0 predicted, so increase log-prob of a0 in s0.
   - •If δ1<0, the final reward was worse than V1 predicted, so decrease log-prob of a1 in s1.
6. 6) Critic update targets (one-step):

   A standard critic regression would move V0 toward (r0 + γ V1) and move V1 toward r1.

**Insight:** Actor-critic turns long-horizon Monte Carlo credit assignment into local prediction errors (δt). The critic learns to predict returns; the actor uses the critic’s surprise as the learning signal.

## Key Takeaways

- ✓

  Policy gradient methods optimize a differentiable stochastic policy πθ(a|s) directly, rather than deriving a policy from value estimates.
- ✓

  The objective is expected (discounted) return: J(θ)=Eτ[∑γᵗrₜ], where τ is sampled under πθ and the environment.
- ✓

  The score-function (log-derivative) trick yields an unbiased estimator: ∇θJ=E[∑∇θ log πθ(aₜ|sₜ)·(return/advantage)].
- ✓

  Reward-to-go Gₜ improves credit assignment by only attributing future rewards to an action at time t.
- ✓

  Baselines b(sₜ) do not change the expected gradient if they are action-independent, but can greatly reduce variance.
- ✓

  Using b(s)=V(s) leads to advantage learning: A(s,a)=Q(s,a)−V(s), which answers “better or worse than average?”
- ✓

  Actor-critic methods learn a critic (value function) to provide low-variance advantage estimates, often via TD residuals δₜ.
- ✓

  GAE provides a tunable bias/variance tradeoff for advantage estimation and is a core ingredient of modern on-policy methods like PPO.

## Common Mistakes

- ✗

  Using a baseline that depends on the sampled action aₜ (this can bias the gradient unless handled carefully).
- ✗

  Forgetting discounting or mixing definitions of return (e.g., using undiscounted Gₜ with a discounted critic target).
- ✗

  Not detaching/stop-gradient through advantage targets when updating the actor (can cause unintended coupling and instability).
- ✗

  Confusing maximizing J(θ) with minimizing a loss: sign errors are common (e.g., descending when you meant to ascend).

## Practice

medium

Derive the reward-to-go policy gradient from the trajectory-level form:

∇θJ = E[ R(τ) ∑ₜ ∇θ log πθ(aₜ|sₜ) ].

Show the steps that justify replacing R(τ) with Gₜ inside the sum.

**Hint:** Condition on the history up to time t and use the fact that actions at time t cannot affect rewards before time t.

Show solution

Start from E[∑ₜ ∇ log π(aₜ|sₜ) · R(τ)]. For a fixed t, decompose R(τ)= (∑\_{k=0}^{t-1} γ^k r\_k) + (γ^t ∑\_{k=t}^{T-1} γ^{k-t} r\_k). The first term depends only on rewards before t, which are independent of aₜ given the past; its expectation multiplied by ∇ log π(aₜ|sₜ) is zero (score-function property). The remaining term is proportional to the future return from t, i.e., reward-to-go. After adjusting for γ factors, you obtain E[∑ₜ ∇ log π(aₜ|sₜ) · Gₜ].

easy

In a discrete-action softmax policy with logits z=fθ(s) and π(a|s)=exp(z\_a)/∑\_j exp(z\_j), compute ∂/∂z\_k log π(a|s).

**Hint:** Write log π(a|s)=z\_a − log(∑\_j exp(z\_j)) and differentiate.

Show solution

log π(a|s)=z\_a − log(∑\_j exp(z\_j)). Then ∂/∂z\_k log π(a|s)=1[k=a] − exp(z\_k)/∑\_j exp(z\_j)=1[k=a] − π(k|s).

medium

GAE computation practice: given δ0=1.0, δ1=0.5, δ2=−0.2, γ=0.9, compute Â0 for λ=0 and for λ=1 (assume episode ends after t=2 so no further terms).

**Hint:** Use Â0=∑\_{l=0}^{2} (γλ)^l δ\_l.

Show solution

For λ=0: Â0 = (γ·0)^0 δ0 + (γ·0)^1 δ1 + (γ·0)^2 δ2 = δ0 = 1.0. For λ=1: Â0=δ0 + (γ)^1 δ1 + (γ)^2 δ2 = 1.0 + 0.9·0.5 + 0.9^2·(−0.2) = 1.0 + 0.45 − 0.162 = 1.288.

## Connections

Next nodes and related concepts:

- •[RLHF](/tech-tree/rlhf/) — uses PPO-style policy gradients with advantage estimation and KL constraints.
- •[Markov Decision Processes](/tech-tree/mdp/) — trajectory distributions and return definitions live here.
- •[Stochastic Gradient Descent](/tech-tree/sgd/) — policy gradient updates are SGD/ascent on sampled estimates.

Suggested prior/parallel reinforcement learning nodes (if present in your tech tree):

- •[Value Functions and Bellman Equations](/tech-tree/value-functions/)
- •[Temporal Difference Learning](/tech-tree/td-learning/)
- •[Advantage Estimation and GAE](/tech-tree/gae/)
- •[Proximal Policy Optimization (PPO)](/tech-tree/ppo/)

Quality: A (4.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
