---
title: The Deity Problem
description: 'Your AI cannot read your mind. Three evidence channels for learning operator preferences: elicitation, revealed preference, and direct query.'
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- frameworks
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
permalink: /frameworks/deity-problem/
---

[← Frameworks](/frameworks/)

# The Deity Problem

[Stage 4Execute](/thesis/#stage-4)

The best way to think about AI systems as of 2026 is that you're a deity to them. It's trying to serve you, but it can't read your mind. It can only observe what you tell it and what you show it. The question is not whether AI will perfectly understand your preferences - it will not. The question is how it gathers evidence about what you actually want.

Operator U\* (latent)Passive observation of prior decisions - free but noisyRevealed Preference"scripture"Cost: 0 / Info: lowStructured interview - best info per dollarStructured Elicitation"sacrament"Cost: med / Info: highAsk every time - expensive, fragile to phrasingDirect Query"prayer"Cost: high / Info: medAgent belief P(U\*)Drift Detection

Download PNGCopy ImageCopy SVGCopy URLEmbed

Click a channel to highlight.

## Why “Deity”

Think about the structural relationship between you and your AI system. You have goals, preferences, and a utility function that determines what “good” means. The AI cannot observe any of this directly. It can only watch your behavior, listen to your instructions, and ask you questions - then try to infer what you actually want.

This is the same dynamic that exists between a deity and a follower in every religious tradition. The follower cannot read the deity's mind. They can only study what was said, observe what happens, and occasionally ask for guidance. The parallel is not doctrinal - it is structural. It happens to be a useful mental model because most readers already have an intuition for it.

The standard approach to AI alignment tries to hardcode your utility function at design time. This fails for three reasons: you cannot articulate what you want upfront (preferences are latent), your priorities drift over time, and complete specification would take months and still be wrong. The Deity Problem treats your utility function as a latent variable to be estimated through interaction, not specified through documentation.

## The Belief Model

The agent maintains a posterior belief over your utility function:

P(U | evidence\_1, ..., evidence\_n)

This starts as a diffuse prior - the agent does not know what you want. It sharpens as evidence accumulates through three channels. Early on, uncertainty is large and behavior is naturally exploratory. Over time, the posterior tightens and the agent confidently pursues what it has learned you want.

## Channel 1: [Structured Elicitation](/lexicon/structured-elicitation/)

Conjoint Analysis(the “sacrament”)

Design experiments that directly probe your preferences with maximum information per question.

The agent designs pairwise comparisons, best-worst scaling, or adaptive choice-based conjoint. It uses D-optimal experiment design - choosing the pair that maximizes expected information gain about your preference weights.

# Example elicitation

“Would you prefer:

(A) Ship feature X by Friday with known edge case bug

(B) Ship feature X by next Wednesday, fully tested”

# One comparison reveals the speed-vs-quality tradeoff

# in the operator's utility function.

Highest info per queryRequires operator attentionAgent controls the experiment

## Channel 2: [Revealed Preference](/lexicon/revealed-preference/)

Behavioral Observation(the “scripture”)

Watch what the operator actually does and infer preferences from behavior, not from what they say.

Based on Afriat's theorem: if observed choices satisfy the Generalized Axiom of Revealed Preference (GARP), there exists a utility function that rationalizes all of them. The agent logs every decision you make or approve, models them as choices from feasible sets, and runs consistency checks.

This channel captures what you *actually value*, not what you say you value. It is the cheapest evidence channel because you are doing what you would do anyway - the agent just watches.

# Revealed preference in practice

Operator overrides thermostat to 74F three evenings in a row

# Revealed: prefers warmer than the model predicted

Operator skips jazz playlist 60% of weekday evenings

# Revealed: jazz preference is contextual, not universal

Cheapest per observationNoisiest signalPassive - zero operator cost

## Channel 3: [Direct Query](/lexicon/direct-query/)

Ask When It Is Worth It(the “prayer”)

Ask the operator a natural-language question - but only when the expected improvement in decision quality exceeds the cost of their attention.

**An agent that asks too many questions is not diligent - it is just poorly calibrated.**

# The query threshold

VOI(question) = E[improvement in policy from answer]

c\_query = cost of operator's attention

Only ask when: VOI(question) > c\_query

The agent simulates: “If I ask this question and get each possible answer, how much better would my policy be?” If the answer is “not much,” do not ask.

Highest latencyResolves ambiguitiesExplicit attention cost

## Channel Selection

| Criterion | Structured Elicitation | Revealed Preference | Direct Query |
| --- | --- | --- | --- |
| Info per query | Highest | Lowest | Medium |
| Operator cost | Medium | Zero (passive) | High (interrupt) |
| Precision | High (controlled) | Low (noisy behavioral) | Medium (depends on translation) |
| Best for | Discovering new preferences | Confirming behavioral patterns | Resolving specific ambiguities |

## Drift Detection

Preferences aren't static. You change your mind, priorities shift, new constraints emerge. The agent must detect when its model of your preferences has gone stale. This is done via posterior predictive checking - the agent periodically audits its own predictions against your actual decisions.

# Drift score (the “heresy detector”)

drift = (1/N) \* sum(predicted\_choice != actual\_choice)

# Response levels:

drift < 0.1   Model tracking well. Continue observing.

drift 0.1-0.3 Some shift. Schedule an elicitation session.

drift > 0.3   Major shift. Widen posterior. Re-elicit.

In the deity analogy: the agent notices that you changed your mind. The response is proportional to the magnitude of the change - a small drift gets gentle re-calibration, a large one triggers a full re-elicitation across all preference dimensions.

## Worked Example: Home Automation Agent

Structured elicitation (onboarding)

20 pairwise comparisons: warm vs cool lighting, high vs low automation, jazz vs ambient. Result: estimated part-worths for lighting warmth, temperature, music genre, automation level.

Revealed preference (ongoing)

Operator overrides thermostat to 74F repeatedly - revealed preference for warmer. Skips jazz on weekdays - contextual preference. Turns lights to max when cooking - activity-dependent. GARP check: needs a context variable (activity type) to rationalize.

Direct query (targeted)

High uncertainty on “guest mode” dimension. VOI > attention cost. Agent asks: “When friends come over, should I switch to guest mode automatically?” Answer: “Auto is fine, but do not change the music.” Update: automation\_level = high for environment, low for entertainment.

Drift detection (month 3)

Drift score rises to 0.22. Investigation: a baby was born. Preferences shifted - quieter music, warmer temperature, dimmer lights in the evening. Structural break detected. Agent widens prior, runs new elicitation session on changed dimensions. Re-converges within a week.

## Properties

No spec neededDeploy on day one with a diffuse prior. The agent learns through interaction, not months of requirements gathering.

Handles driftThe [drift detector](/lexicon/drift-detector/) catches preference changes. The re-elicitation mechanism responds. The agent updates continuously.

Explicit costEvery elicitation and query has a measurable cost. The agent optimizes the information-to-attention ratio. It interrupts only when it is worth it.

FalsifiableThe learned model predicts future choices. If predictions are wrong, the model is updated. No unfalsifiable “the model knows what you want.”

DecomposableEach preference dimension has its own posterior. Drift in one dimension does not contaminate others. Re-elicitation is targeted.

## The Shorthand

For quick reference, the three channels and drift detector have religious nicknames that map to the deity analogy. These are mnemonics, not the primary terminology:

Sacrament = structured elicitation

Scripture = revealed preference

Prayer = direct query

Heresy = drift detection

## Connection to Other Frameworks

[The Performance Frontier](/frameworks/performance-frontier/) - your utility function U\* is itself a frontier the agent navigates toward. The three evidence channels are how it estimates the frontier's location.

[Designed Convergence](/frameworks/designed-convergence/) - The Deity Problem is mechanism design where the mechanism is preference learning. The system converges to your true preferences.

[Quality Hillclimb](/frameworks/quality-hillclimb/) - the quality gates can be informed by the learned preference model. What counts as “good” is defined by the posterior over U\*.

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

The principal problem. The agent is trying to serve the principal; the question is how the principal reveals preferences without spending the attention budget. Allocation of operator attention is itself an allocation decision.](/positions/allocator/)[Operator

The daily question when working with an agent: do I have to tell it what I want every time, or does it learn? The three channels (elicitation, revealed preference, direct query) are how you get out of the perpetual-onboarding trap.](/positions/operator/)[Builder

The information architecture for agent context. Observe the user's actions, ask when expected value exceeds cost, run a structured experiment when the question is high-stakes. Three pipes, one posterior.](/positions/builder/)[Scientist

Inverse reinforcement learning with three observation channels. Revealed preference (Afriat, GARP) is the cheapest; structured elicitation (conjoint analysis) is highest information per query; direct query is the escape hatch. Combine via Bayesian updating.](/positions/scientist/)

See also: [Structured Elicitation](/lexicon/#structured-elicitation) · [Revealed Preference](/lexicon/#revealed-preference) · [Direct Query](/lexicon/#direct-query) · [Drift Detector](/lexicon/#drift-detector)
