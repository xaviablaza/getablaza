---
title: RLHF
description: Reinforcement Learning from Human Feedback. Reward modeling, PPO.
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
permalink: /tech-tree/rlhf/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# RLHF

Machine LearningDifficulty: ★★★★★Depth: 10Unlocks: 0

Reinforcement Learning from Human Feedback. Reward modeling, PPO.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Reward model trained from human preference comparisons (maps outputs to scalar rewards)
- -Policy fine-tuning by optimizing expected learned reward (use learned reward as the RL return)
- -KL-based regularization to a reference (pretrained) policy to maintain stability and avoid distributional drift

## Key Symbols & Notation

r\_phi - scalar reward function learned from human feedback (phi = reward-model parameters)pi\_ref - reference (pretrained) policy used in KL penalty/constraint

## Essential Relationships

- -Human preference data -> train r\_phi; r\_phi provides scalar returns used to compute policy gradients; policy updates maximize expected r\_phi subject to a KL(pi\_theta || pi\_ref) penalty/constraint

## Prerequisites (2)

[Policy Gradient Methods6 atoms](/tech-tree/policy-gradient/)[Loss Functions7 atoms](/tech-tree/loss-functions/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[GARPBusiness

RLHF is revealed preference applied to alignment: human pairwise comparisons reveal a latent reward function, exactly as consumer choices reveal utility under GARP. Afriat-style consistency checks could audit whether a reward model is rationalizable.](/business/garp/)[redlineBusiness

Optimizing redline suggestions to achieve ≥0.8 human accept rate is directly the RLHF loop: generate candidate edits, collect human accept/reject signals, update the policy to align suggestions with human judgment](/business/redline/)

Advanced Learning Details

### Graph Position

250

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

10

Chain Length

### Cognitive Load

6

Atomic Elements

39

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (15)

- - Human preference data: collecting pairwise (or ranked) judgments from humans comparing two model outputs for the same prompt
- - Reward model (RM): a learned scalar function that maps a model output (sequence) to a reward signal using human preference data
- - Pairwise preference loss / Bradley–Terry / logistic preference model: training the RM by predicting which of two outputs humans prefer using a logistic/cross-entropy style loss on score differences
- - Supervised fine-tuning (SFT) as initialization: using a pre-trained model further fine-tuned on curated supervised examples to serve as the initial policy/reference
- - Reference policy / pretraining policy (π\_ref): the baseline policy (often the SFT model) used to constrain RL updates
- - Preference dataset (D\_pref): the dataset consisting of prompt + output pairs and human comparison labels used to train the RM
- - Reward normalization / baselining specific to RLHF: scaling or centering RM outputs before computing advantages to stabilize learning
- - PPO-specific surrogate objective (clipped objective): the particular objective used in RLHF to update policy parameters safely
- - Probability/importance ratio for policy updates: the ratio of new-policy to old-policy action probabilities used in the PPO surrogate
- - Clipping parameter (ε) in PPO: the hyperparameter that bounds the importance ratio to limit update magnitude
- - KL penalty / trust-region regularization to reference policy: adding a KL divergence term or early-stopping on KL to keep the RL policy close to the reference/SFT model
- - Reward-model-to-policy pipeline (iterative loop): the operational sequence SFT -> collect comparisons -> train RM -> optimize policy with RM -> collect more comparisons (iterate)
- - Reward model miscalibration and reward hacking (Goodhart effects): the phenomenon where the policy optimizes spurious RM artifacts because the RM is an imperfect proxy
- - Value function trained on RM reward: critic approximating expected cumulative RM reward for advantage estimation in PPO
- - Sampling strategy effects on preference data: how temperature/decoding method used to generate candidate outputs affects the quality/diversity of preference labels

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

RLHF is the engineering bridge between “a powerful language model” and “a model that reliably behaves the way humans want.” It does this by (1) learning a reward function from human preference comparisons, then (2) fine-tuning the policy to maximize that learned reward while staying close to a trusted reference policy.

TL;DR:

RLHF (Reinforcement Learning from Human Feedback) typically has two big stages: (1) train a reward model r\_ϕ from human preference data over model outputs, and (2) optimize a policy π to maximize expected reward r\_ϕ while applying a KL penalty to keep π close to a reference policy π\_ref. In practice, the policy step is often done with PPO on a token-level sequence model, using r\_ϕ as the terminal reward (plus optional shaping) and adding −β·KL(π‖π\_ref) for stability and alignment.

## What Is RLHF?

RLHF (Reinforcement Learning from Human Feedback) is a training recipe for turning a pretrained generative model (the “policy”) into one that better matches human preferences.

Why this exists: supervised fine-tuning (SFT) teaches a model to imitate demonstrations. But in many real tasks—helpfulness, harmlessness, style, honesty, instruction-following—there isn’t a single “correct” output. Instead, there are outputs humans prefer over others. Preferences are comparative and subjective, and they can be inconsistent across people and contexts.

RLHF treats “what humans like” as a reward signal. The catch is that humans don’t provide a numeric reward for every output; they can more reliably answer questions like:

- •“Between response A and response B, which is better?”
- •“Which is safer?”
- •“Which follows the instruction more closely?”

So RLHF usually proceeds in two phases:

1) Reward modeling: learn a scalar reward function r\_ϕ that predicts human preference.

2) Policy optimization: fine-tune the policy π\_θ to maximize expected reward under r\_ϕ.

A third ingredient is crucial in large language models: keep the optimized policy close to a reference policy π\_ref (typically the pretrained or SFT model). If you optimize purely for the learned reward, the policy can drift out of distribution, exploit weaknesses in r\_ϕ (reward hacking), or collapse into repetitive high-reward patterns. The KL term is the stabilizer.

A useful mental picture is:

- •You start with π\_ref: a competent base model.
- •You learn r\_ϕ: a proxy for “human likes this.”
- •You update π\_θ: to get higher r\_ϕ, but with a leash so it doesn’t wander too far from π\_ref.

Key symbols you’ll see throughout:

- •r\_ϕ(y, x): scalar reward model output for response y given prompt x (ϕ are reward model parameters).
- •π\_θ(y|x): current policy distribution over responses given prompt.
- •π\_ref(y|x): reference policy distribution (fixed).
- •KL(π\_θ‖π\_ref): divergence penalty/constraint to control drift.

Although RLHF is often described with “reinforcement learning,” in language modeling it’s sequence-level RL: you sample tokens step-by-step, but the reward might be computed at the end of the sequence from r\_ϕ.

RLHF is not magic. It is a pragmatic approach that works when:

- •You can gather preference data representative of the desired behavior.
- •Your reward model generalizes reasonably.
- •Your policy optimizer is stable (PPO + KL regularization is common).

When those fail, RLHF can produce confident misalignment: behavior that looks good to r\_ϕ but not to humans.

## Core Mechanic 1: Reward Modeling from Human Preferences

Why reward modeling first: humans can’t score every output on a consistent numeric scale. But pairwise comparisons are easier, faster, and often more reliable. Reward modeling turns those comparisons into a scalar function you can optimize.

## Preference data format

A typical dataset contains tuples like:

- •prompt x
- •two candidate responses y₁ and y₂ (generated by a model, possibly different checkpoints)
- •a human label indicating which is preferred: y⁺ ≻ y⁻

You can think of this as teaching a model to assign higher reward to preferred responses.

## A standard probabilistic model (Bradley–Terry / logistic preference)

A common approach assumes the probability that y₁ is preferred over y₂ is a logistic function of the reward difference:

P(y₁ ≻ y₂ | x) = σ(r\_ϕ(x, y₁) − r\_ϕ(x, y₂))

where σ(t) = 1 / (1 + e^(−t)).

This has a nice interpretation: only relative differences matter. If you add a constant c to all rewards, preferences don’t change.

## The reward model loss

Given a labeled pair (x, y⁺, y⁻), maximize log-likelihood:

ℓ(ϕ) = log σ(r\_ϕ(x, y⁺) − r\_ϕ(x, y⁻))

Equivalently, minimize the negative log-likelihood:

L\_RM(ϕ) = − E[(x,y⁺,y⁻)] [ log σ(r\_ϕ(x, y⁺) − r\_ϕ(x, y⁻)) ]

Let Δ = r\_ϕ(x, y⁺) − r\_ϕ(x, y⁻). Then:

L\_RM = −log σ(Δ)

and the gradient pushes Δ upward.

## Architecture: how r\_ϕ is implemented

In LLM RLHF, r\_ϕ is usually a copy of the base transformer with an added scalar “reward head” on top of the final hidden state (often the end-of-sequence token). Conceptually:

- •The transformer produces a representation **h** ∈ ℝᵈ for the sequence (x, y).
- •A linear head maps it to a scalar: r\_ϕ(x, y) = **w**ᵀ **h** + b.

Vectors are bold: **h**, **w**.

## Calibration and identifiability

Because only differences matter, reward values are only defined up to an additive constant. In practice:

- •You may normalize rewards (mean 0, variance 1 on a batch).
- •You may clip rewards to limit extreme values.

This isn’t just cosmetic: PPO stability depends heavily on reward scale.

## Why reward models fail (and why that matters)

Reward modeling is supervised learning under distribution shift.

- •During training, the reward model sees outputs sampled from some policy distribution (often an early SFT policy).
- •During RL optimization, the policy changes. It may generate novel outputs where r\_ϕ extrapolates poorly.

This mismatch creates “reward hacking”: the policy finds outputs that exploit blind spots in r\_ϕ.

Common failure modes:

- •Stylistic proxies: r\_ϕ likes confident tone, so the model becomes overconfident.
- •Length bias: r\_ϕ correlates “longer” with “better,” so outputs bloat.
- •Safe but unhelpful: r\_ϕ penalizes risky content, so the model refuses too often.

This is why the next mechanic (KL to π\_ref) is not optional: it’s a containment strategy.

## A short derivation: from pairwise labels to a margin-like objective

Start with the loss for one example:

L = −log σ(r⁺ − r⁻)

Use σ(t) = 1/(1+e^(−t)):

L = −log( 1/(1+e^(−(r⁺−r⁻))) )

= log(1 + e^(−(r⁺−r⁻)))

= softplus(−(r⁺−r⁻))

So it behaves like a smooth hinge: if r⁺ is already much larger than r⁻, the loss is small; otherwise it pushes them apart.

## Data collection notes (practical)

Human preference datasets are typically built by:

- •Sampling prompts x from real usage or curated sets.
- •Generating multiple candidate responses (beam search, sampling, different temperatures, different model checkpoints).
- •Having labelers rank or compare pairs.

Ranking can be reduced to pairwise comparisons (all pairs, or tournament-style). Pairwise is easiest to train with and scales well.

## Core Mechanic 2: Policy Optimization with PPO + KL Regularization

Why RL at all: once you have r\_ϕ, you want to change the policy π\_θ so that it produces higher-reward outputs. This is not just supervised learning because the “label” depends on what the policy generates.

But vanilla policy gradients are high variance and can take destabilizingly large steps—especially with giant language models and imperfect rewards. PPO (Proximal Policy Optimization) is widely used because it constrains updates to be conservative.

## The objective you actually want (regularized)

A common RLHF objective is a KL-regularized expected reward:

J(θ) = E\_{x∼D, y∼π\_θ(·|x)} [ r\_ϕ(x, y) − β · KL(π\_θ(·|x) ‖ π\_ref(·|x)) ]

Interpretation:

- •r\_ϕ is “human preference proxy.”
- •KL term is a leash to keep behavior near π\_ref.
- •β ≥ 0 sets the tradeoff: bigger β means more conservative.

This can be implemented either as:

- •a penalty: subtract β·KL in the reward, or
- •a constraint: maximize reward subject to KL ≤ δ.

### Penalty vs constraint (why you see β)

In constrained form:

maximize E[r\_ϕ]

subject to E[KL(π\_θ‖π\_ref)] ≤ δ

The penalty form is the Lagrangian relaxation with β as a Lagrange multiplier. Many systems adapt β online to hit a target KL.

## Sequence models: where does the KL come from?

For an autoregressive policy:

π\_θ(y|x) = ∏\_{t=1}^T π\_θ(y\_t | x, y\_{<t})

Then the log-prob decomposes:

log π\_θ(y|x) = ∑\_{t=1}^T log π\_θ(y\_t | x, y\_{<t})

Token-level KL between two autoregressive policies over a sampled trajectory y is often estimated by:

KL(π\_θ‖π\_ref) ≈ ∑\_{t=1}^T ( log π\_θ(y\_t|s\_t) − log π\_ref(y\_t|s\_t) )

where s\_t = (x, y\_{<t}). This is an on-policy sample estimate, not an exact KL over all y, but it’s practical.

## Shaped reward used in practice

Often you define a per-trajectory shaped reward:

R(x, y) = r\_ϕ(x, y) − β · ∑\_{t=1}^T ( log π\_θ(y\_t|s\_t) − log π\_ref(y\_t|s\_t) )

Then you treat R as the return for policy gradient.

Notice something subtle: the penalty contains log π\_θ, which depends on θ. This means you must be careful about what is treated as “reward” vs what is part of the optimization objective. PPO implementations handle this by incorporating the KL term explicitly or by adding it as an extra loss.

## Why PPO (and what it does)

Vanilla policy gradient would update θ proportional to:

∇\_θ E[ R ] = E[ ∇\_θ log π\_θ(y|x) · (R − b(x)) ]

where b(x) is a baseline (value function) to reduce variance.

But if R is large or noisy, the update can be too big, changing π drastically, which:

- •invalidates the reward model’s training distribution
- •destabilizes training (mode collapse)

PPO addresses this with a clipped surrogate objective.

## PPO clipped objective (single-step view)

Let

- •r\_t(θ) = π\_θ(a\_t|s\_t) / π\_{θ\_old}(a\_t|s\_t) = exp( logπ\_θ − logπ\_old )
- •Â\_t be an advantage estimate at time t

Then PPO maximizes:

L\_PPO(θ) = E\_t [ min( r\_t(θ) · Â\_t , clip(r\_t(θ), 1−ε, 1+ε) · Â\_t ) ]

This prevents r\_t from moving too far from 1. ε is typically ~0.1–0.2.

In language modeling, “actions” are tokens y\_t, and trajectories are sequences.

## Advantage estimation in RLHF

A standard actor-critic setup learns a value function V\_ψ(s\_t). You compute:

Â\_t = G\_t − V\_ψ(s\_t)

where G\_t is a return estimate.

If the reward is terminal only (reward model evaluated at end):

- •r\_T = r\_ϕ(x, y)
- •r\_t = 0 for t < T (ignoring KL shaping for the moment)

Then a simple return is:

G\_t = r\_ϕ(x, y)

for all t along the trajectory (or discounted versions).

In practice, you often include per-token KL penalties, making rewards dense:

r\_t = −β (logπ\_θ(y\_t|s\_t) − logπ\_ref(y\_t|s\_t))

and terminal r\_T += r\_ϕ(x, y)

Then you can compute G\_t via discounted sums:

G\_t = ∑\_{k=t}^T γ^(k−t) r\_k

Often γ is near 1; sometimes γ = 1 is used for episodic tasks.

## Putting it together: the total loss

A typical implementation minimizes a weighted sum:

L\_total = L\_actor + c\_v · L\_value + c\_e · L\_entropy + L\_KL(optional)

Where:

- •L\_actor is negative of PPO surrogate (maximize surrogate → minimize −surrogate)
- •L\_value is MSE: (V\_ψ(s\_t) − G\_t)²
- •entropy bonus encourages exploration (helps avoid collapse)
- •KL penalty may be included explicitly to hit a target KL

### Why KL to π\_ref is specifically important in RLHF

You might ask: “Isn’t PPO already conservative?” It is, relative to π\_old. But RLHF needs conservatism relative to a trusted reference distribution π\_ref for two reasons:

1) Reward model validity: r\_ϕ is trained on samples near π\_ref/SFT. Staying close reduces out-of-distribution exploitation.

2) Capability retention: π\_ref encodes broad language competence. Without KL, optimizing narrow preferences can degrade general performance.

A helpful lens is: KL is a regularizer on the function space of policies, not just step size.

## A brief derivation: KL-regularized RL as “reward + log prior”

Consider maximizing:

E\_{y∼π} [ r\_ϕ(x,y) ] − β KL(π‖π\_ref)

Expand KL:

KL(π‖π\_ref) = E\_{y∼π} [ log π(y|x) − log π\_ref(y|x) ]

So the objective becomes:

J = E\_{y∼π} [ r\_ϕ(x,y) ] − β E\_{y∼π}[ log π(y|x) − log π\_ref(y|x) ]

= E\_{y∼π} [ r\_ϕ(x,y) − β log π(y|x) + β log π\_ref(y|x) ]

This shows two things:

- •The term −β log π encourages higher entropy (like maximum entropy RL).
- •The term +β log π\_ref biases the policy toward the reference (a “prior”).

This is one reason RLHF often behaves like: “Prefer what humans like, but among those, choose something plausible under the base model.”

## Application/Connection: The Full RLHF Pipeline, Design Choices, and Failure Modes

This section connects the mechanics into an end-to-end pipeline and highlights the engineering decisions that matter at scale.

## End-to-end pipeline (typical)

A common three-stage setup is:

1) Pretrain a language model on next-token prediction (not RLHF itself).

2) Supervised fine-tuning (SFT) on instruction-following demonstrations.

3) RLHF:

- •collect preference comparisons on model outputs
- •train reward model r\_ϕ
- •fine-tune policy π\_θ with PPO using r\_ϕ and KL to π\_ref

π\_ref is often the SFT model (or a snapshot of the current policy before RL). The choice affects how conservative you are.

## Key design axes (with tradeoffs)

| Decision | Options | Why it matters | Typical choice |
| --- | --- | --- | --- |
| Preference labels | pairwise, ranking, scalar ratings | label noise + ease for humans | pairwise or ranking → pairwise |
| Reward model | separate model, shared backbone, ensemble | generalization + reward hacking | separate RM, sometimes ensemble |
| Policy optimizer | PPO, A2C, DPO/IPO-style direct methods | stability + complexity | PPO for classic RLHF |
| KL control | fixed β, adaptive β, hard constraint | prevents drift | adaptive β targeting KL |
| Reward shaping | terminal only, +per-token KL, +length penalties | variance + behavior | terminal RM + token KL |

## What PPO is optimizing in language model RLHF (concrete)

Each iteration:

- •Sample a batch of prompts x.
- •For each prompt, sample a response y from current π\_{θ\_old}.
- •Compute reward model score r\_ϕ(x, y).
- •Compute token log-probs under π\_{θ\_old} and π\_ref.
- •Form per-token rewards with KL and a terminal reward.
- •Estimate advantages Â\_t.
- •Update policy θ using PPO objective for a few epochs over this batch.
- •Update value network ψ.

Even if you conceptually think “sequence reward,” implementations are token-based because:

- •KL is naturally token-decomposed
- •value function is per-token state V(s\_t)
- •PPO’s ratio r\_t is per-token

## Monitoring: what you watch during RLHF

You typically track:

- •Mean reward model score E[r\_ϕ]
- •Mean KL to π\_ref (global + per-token)
- •Entropy of the policy
- •Response length statistics
- •Human eval on held-out prompts (must-have)

A healthy run often shows:

- •reward increases steadily
- •KL stays near target
- •entropy decreases somewhat but not collapse

## Failure modes (and what causes them)

### 1) Reward hacking

The policy finds outputs that exploit r\_ϕ.

Root cause: r\_ϕ is a learned proxy; it generalizes imperfectly. The optimization is strong and adversarial.

Mitigations:

- •stronger KL constraint
- •reward model ensembles / uncertainty
- •periodically refresh preference data with current policy (active learning)
- •add “anti-cheating” data (adversarial prompts)

### 2) Over-optimization and mode collapse

Symptoms: repetitive outputs, generic safe responses, refusal everywhere.

Root cause: the learned reward landscape may have narrow peaks; PPO can push into them.

Mitigations:

- •entropy bonus
- •KL targeting
- •better preference dataset balancing helpfulness vs safety

### 3) Capability regression

Symptoms: worse factuality, worse reasoning, lower performance on standard NLP benchmarks.

Root cause: RL step optimizes a narrow preference signal; without enough KL or with biased data, the model drifts away from broadly useful behaviors.

Mitigations:

- •stronger KL to π\_ref
- •include “capability anchors” in evaluation (and sometimes in reward)
- •use a higher-quality SFT model as π\_ref

### 4) Miscalibration / “reward likes confidence”

Symptoms: confident wrong answers; refusal patterns.

Root cause: labelers prefer confident style, or comparisons don’t penalize confident errors enough.

Mitigations:

- •preference guidelines emphasizing correctness
- •tasks that explicitly compare calibrated vs uncalibrated answers
- •integrate external verification signals (tool use, factuality checks)

## RLHF vs direct preference optimization (connection)

RLHF (RM + PPO) is not the only way. There are “direct” methods (e.g., DPO-style) that skip explicit RL and use preference data to directly update π.

Why you still learn RLHF:

- •Classic and widely deployed
- •KL-regularized RL perspective is fundamental
- •Helps you reason about stability, exploration, reward hacking

## When KL regularization is not just “nice,” but necessary

If r\_ϕ is even slightly misspecified, the unconstrained optimum can be far from human intent. KL provides a trust region around π\_ref where r\_ϕ is more reliable.

Think of it like this: r\_ϕ is a map of a city drawn from a small neighborhood. KL keeps you from driving into areas where the map is wrong.

## Worked Examples (3)

### Training a reward model from one preference pair (logistic loss + gradient direction)

You have a prompt x and two responses y⁺ (preferred) and y⁻ (rejected). The reward model outputs r⁺ = r\_ϕ(x,y⁺) and r⁻ = r\_ϕ(x,y⁻). Use the standard Bradley–Terry likelihood: P(y⁺ ≻ y⁻|x) = σ(r⁺ − r⁻).

1. Define Δ = r⁺ − r⁻.
2. Negative log-likelihood loss:

   L = −log σ(Δ).
3. Rewrite using σ(Δ) = 1/(1+e^(−Δ)):

   L = −log(1/(1+e^(−Δ)))

   = log(1 + e^(−Δ))

   = softplus(−Δ).
4. Differentiate w.r.t. Δ:

   ∂L/∂Δ = ∂/∂Δ log(1+e^(−Δ))

   = (1/(1+e^(−Δ))) · (−e^(−Δ))

   = − 1/(1+e^(Δ))

   = −σ(−Δ)

   = σ(Δ) − 1.
5. Chain rule to see direction on r⁺ and r⁻:

   ∂L/∂r⁺ = ∂L/∂Δ · ∂Δ/∂r⁺ = (σ(Δ) − 1) · 1

   ∂L/∂r⁻ = ∂L/∂Δ · ∂Δ/∂r⁻ = (σ(Δ) − 1) · (−1) = 1 − σ(Δ).
6. Interpretation:

   - •If Δ is small (model unsure), σ(Δ) ≈ 0.5, so ∂L/∂r⁺ ≈ −0.5 (push r⁺ up) and ∂L/∂r⁻ ≈ +0.5 (push r⁻ down).
   - •If Δ is already large, σ(Δ) ≈ 1, gradients go to 0 (pair is already separated).

**Insight:** The preference loss only cares about relative reward. Training pushes the preferred output’s reward above the rejected output’s reward, with diminishing pressure once the ordering is confidently correct.

### KL-regularized objective expanded into an equivalent “shaped reward” form

You want to optimize: J(θ) = E\_{y∼π\_θ(·|x)}[ r\_ϕ(x,y) − β KL(π\_θ(·|x)‖π\_ref(·|x)) ]. Expand KL to see what signal the policy gradient is getting.

1. Start with the definition:

   KL(π\_θ‖π\_ref) = E\_{y∼π\_θ}[ log π\_θ(y|x) − log π\_ref(y|x) ].
2. Substitute into J:

   J = E\_{y∼π\_θ}[ r\_ϕ(x,y) ] − β E\_{y∼π\_θ}[ log π\_θ(y|x) − log π\_ref(y|x) ].
3. Combine expectations (same sampling distribution π\_θ):

   J = E\_{y∼π\_θ}[ r\_ϕ(x,y) − β log π\_θ(y|x) + β log π\_ref(y|x) ].
4. Interpret each term:

   - •r\_ϕ(x,y): learn to produce outputs humans prefer.
   - •−β log π\_θ(y|x): encourages higher entropy (avoids overly peaky policy).
   - •+β log π\_ref(y|x): pulls probability mass toward what π\_ref already considers likely.
5. Autoregressive decomposition:

   log π\_θ(y|x) = ∑\_{t=1}^T log π\_θ(y\_t|s\_t)

   log π\_ref(y|x) = ∑\_{t=1}^T log π\_ref(y\_t|s\_t)

   So the KL-related terms naturally become token-level sums.

**Insight:** The KL term is not just a ‘penalty’; it turns π\_ref into a probabilistic prior and adds an entropy-like term. This is why RLHF often improves preference without completely destroying fluency—when β is tuned correctly.

### A tiny PPO ratio calculation on one token (why clipping prevents big jumps)

At some token position t with state s\_t, the old policy assigns probability 0.02 to token a, and the new policy assigns probability 0.06. Suppose the advantage estimate is Â\_t = +4 and PPO ε = 0.2.

1. Compute the probability ratio:

   r\_t = π\_new(a|s\_t) / π\_old(a|s\_t) = 0.06 / 0.02 = 3.
2. Unclipped surrogate contribution:

   r\_t · Â\_t = 3 · 4 = 12.
3. Compute clipped ratio:

   clip(r\_t, 1−ε, 1+ε) = clip(3, 0.8, 1.2) = 1.2.
4. Clipped surrogate contribution:

   clip(r\_t,...) · Â\_t = 1.2 · 4 = 4.8.
5. PPO takes the min for positive advantage:

   min(12, 4.8) = 4.8.

   So the objective gain for this token is capped.

**Insight:** Even if the optimizer tries to triple a token probability in one update, PPO’s clipping limits how much that move can improve the objective—reducing destructive, reward-chasing jumps.

## Key Takeaways

- ✓

  RLHF = reward modeling from human preferences + policy optimization to maximize the learned reward.
- ✓

  Reward models r\_ϕ are typically trained on pairwise comparisons using a logistic loss: −log σ(r⁺ − r⁻).
- ✓

  Policy optimization commonly maximizes E[r\_ϕ] while penalizing KL drift from a reference policy π\_ref: −β·KL(π‖π\_ref).
- ✓

  For autoregressive LMs, log-prob and KL decompose as token sums, making per-token PPO updates practical.
- ✓

  PPO’s clipped objective provides conservative policy updates relative to π\_old, improving stability under noisy learned rewards.
- ✓

  KL-to-π\_ref is a containment strategy against reward hacking and capability regression by staying in-distribution.
- ✓

  Reward scale and KL coefficient β strongly affect training dynamics; many systems adapt β to target a desired KL.
- ✓

  Human evaluation remains essential: r\_ϕ is only a proxy and can be exploited or miscalibrated.

## Common Mistakes

- ✗

  Treating r\_ϕ as ground truth: optimizing a learned proxy without strong KL control invites reward hacking.
- ✗

  Ignoring reward/advantage normalization: poor scaling can make PPO unstable or cause collapse.
- ✗

  Confusing KL(π‖π\_ref) with KL(π\_ref‖π): direction matters; RLHF typically penalizes the policy drifting away from the reference.
- ✗

  Collecting preference data from a distribution that doesn’t match deployment prompts: the reward model generalizes poorly and alignment degrades.

## Practice

easy

You observe preference data where (x, y₁) is preferred to (x, y₂). Your reward model currently predicts r\_ϕ(x,y₁)=1.0 and r\_ϕ(x,y₂)=1.5. Compute the probability P(y₁ ≻ y₂|x)=σ(r₁−r₂) and the loss L=−log σ(r₁−r₂).

**Hint:** Compute Δ = r₁ − r₂ and apply σ(Δ)=1/(1+e^(−Δ)).

Show solution

Δ = 1.0 − 1.5 = −0.5.

P = σ(−0.5) = 1/(1+e^(0.5)) ≈ 1/(1+1.6487) ≈ 0.3775.

L = −log(0.3775) ≈ 0.9741.

medium

Show that maximizing E[r\_ϕ(x,y) − β·KL(π\_θ(·|x)‖π\_ref(·|x))] is equivalent to maximizing E[r\_ϕ(x,y) + β log π\_ref(y|x) − β log π\_θ(y|x)] under y∼π\_θ. What conceptual role does β log π\_ref play?

**Hint:** Expand KL(π‖π\_ref) as an expectation of log ratios under π.

Show solution

KL(π\_θ‖π\_ref) = E\_{y∼π\_θ}[log π\_θ(y|x) − log π\_ref(y|x)].

So:

E[r\_ϕ − β KL]

= E[r\_ϕ] − β E[log π\_θ − log π\_ref]

= E[r\_ϕ − β log π\_θ + β log π\_ref].

Conceptually, β log π\_ref acts like a prior term that biases the optimized policy toward outputs that the reference policy already considers likely (helping preserve fluency/capabilities and reducing out-of-distribution drift).

hard

In a PPO step for one token, suppose π\_old(a|s)=0.10, π\_new(a|s)=0.13, ε=0.2, and advantage Â=−3. Compute the unclipped term r·Â and the clipped term clip(r,1−ε,1+ε)·Â, then the PPO contribution min(r·Â, clipped·Â) or max depending on sign. Which one is used and why?

**Hint:** For negative advantages, PPO uses max( r·Â, clip(r,...)·Â ) (equivalently min with sign accounted for) to prevent the update from over-decreasing probability.

Show solution

r = 0.13/0.10 = 1.3.

Unclipped: r·Â = 1.3·(−3) = −3.9.

Clipped ratio: clip(1.3, 0.8, 1.2) = 1.2.

Clipped: 1.2·(−3) = −3.6.

Because Â is negative, PPO takes the max of the two (less negative is better for the objective): max(−3.9, −3.6) = −3.6.

This prevents the optimizer from making the probability change too large in a direction that would excessively reduce the likelihood of the sampled action when the advantage is negative.

## Connections

[Policy Gradient Methods](/tech-tree/policy-gradient-methods/)

[Actor-Critic](/tech-tree/actor-critic/)

[Proximal Policy Optimization (PPO)](/tech-tree/ppo/)

[KL Divergence](/tech-tree/kl-divergence/)

[Preference Learning / Bradley–Terry Models](/tech-tree/preference-learning/)

[Direct Preference Optimization (DPO)](/tech-tree/dpo/)

[Reward Hacking & Specification Gaming](/tech-tree/reward-hacking/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
