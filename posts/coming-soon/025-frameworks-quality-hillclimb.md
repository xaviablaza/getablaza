---
title: Quality Hillclimb
description: Apply ratcheted quality gates to stochastic agent output. The agent doesn't need a plan - the gates create ascent. Rejection sampling with a monotone ratchet.
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
generated_by: templeton-deep-copy-import
permalink: /frameworks/quality-hillclimb/
---

[← Frameworks](/frameworks/)

# Quality Hillclimb

[Stage 4Execute](/thesis/#stage-4)

Analogy: stochastic optimization with a ratchet

Quality Hillclimb is a framework for getting stochastic AI agents to improve monotonically without an improvement plan. You wrap the agent in deterministic quality gates plus a ratchet that locks in accepted output. The agent does not need to understand quality - it only needs to keep proposing. The gates create the climb; the ratchet prevents regression.

IterationsQuality ScoreIter 16: score 0.82Floor: 0.82Accepted - floor rises (apex)ratchet floorrejected (below floor)accepted (new floor)The gate rejects. The ratchet locks. Quality is monotonically non-decreasing.

Download PNGCopy ImageCopy SVGCopy URLEmbed

Drag to step through iterations. Iter 16/16: Accepted - floor rises (apex).

## The Insight

AI agents produce stochastic output - given the same input, they generate different results each time. Most teams try to control this by writing better prompts, fine-tuning models, or adding instructions. This is playing the game.

Quality Hillclimb designs the game instead. The agent doesn't need a plan for improvement. It needs **gates that create a one-way valve on quality**. Output that passes the gate and exceeds the current best becomes the new floor. Output that fails is rejected. The agent tries again. Over many iterations, quality ascends.

## How It Works

# The loop

agent produces output (stochastic)

→ gate evaluates (deterministic)

→ if score > current\_best:

ratchet it in (new floor)

→ if score <= current\_best:

reject, agent retries

# Each accepted output is a step uphill.

# The sequence of baselines is monotonically non-decreasing.

## The [Quality Ratchet](/lexicon/quality-ratchet/)

The [Quality Ratchet](/lexicon/#quality-ratchet) is the primitive that makes hillclimbing possible. It is a CI-enforced floor that only moves up. Once a metric reaches a threshold, the system blocks any change that drops below it.

# Formal property

baseline\_{{k+1}} >= baseline\_k   for all k

# The sequence is monotonically non-decreasing.

# No improvement is ever lost. No regression is ever permitted.

The ratchet is the mechanism that prevents downhill steps. Without it, the stochastic process is a random walk. With it, the stochastic process is a hillclimb.

## Gate Design Principles

A good gate has three properties:

Quantitative and deterministic

The gate produces a number, and the same input consistently produces the same number. “Does it feel good?” is not a gate. “Does test coverage exceed 80%?” is a gate.

Cheap relative to generation

If the gate costs as much to evaluate as the agent costs to generate, you are back to T = 1 - the [Verification Trap](/lexicon/#verification-trap). The gate must be orders of magnitude cheaper than generation.

Correlated with actual quality

A gate that measures the wrong thing drives the wrong improvement. Goodhart's Law applies: when a measure becomes a target, it ceases to be a good measure. The gate must be validated against ground truth.

## Why It Works: The Optimization Analogy

For readers who want the optimization analogy: this resembles stochastic search on a quality surface, without ever computing a gradient explicitly.

# The optimization analogy

Quality gates = accept/reject signal

Stochastic agent output = exploration (sampling)

Quality ratchet = monotone floor constraint

Rejection sampling with a one-way ratchet.

The system ascends a quality surface it rarely defines explicitly.

# The gates DEFINE the surface. The stochasticity EXPLORES it.

# The ratchet LOCKS IN each step uphill.

The mechanism is closer to rejection sampling than gradient descent - the gates provide a binary accept/reject signal, not a directional gradient. But the effect is the same: monotone ascent on a surface you rarely write down analytically.

## Practical Example

AI agent writing code

**Gate:** tests pass + coverage >= current floor + linter clean + no security warnings.

**Ratchet:** each PR that passes and exceeds coverage becomes the new floor.

**Result:** over 100 PRs, coverage climbs from 60% to 85%. Lint violations drop from 200 to 12. Zero regression on any metric. No one wrote a “quality improvement plan.” The gates did the work.

## Connection to Other Frameworks

[Designed Convergence](/frameworks/designed-convergence/) - Quality Hillclimb is the single-agent instance. The gates + ratchet are the conditions for convergence.

[The Performance Frontier](/frameworks/performance-frontier/) - the gates define what counts as “uphill.” The frontier is where the hillclimb is heading.

[The Promotion Protocol](/frameworks/promotion-protocol/) - the autonomy graduation criteria are quality gates. The HITL state is a gate the AI must pass to earn autonomy.

[Verification Quadrant](/tools/verification-quadrant/) - gates only work in the Sweet Spot where verification is cheap. The [Ablaza Ratio](/lexicon/#templeton-ratio) determines whether a gate is economically viable.

## Worked example: the ratchet in a visualization grader

In practice, this framework shipped against 182 interactive visualizations scored on six rubric dimensions. No improvement plan was written. The agent was given a floor per dimension, a composite score, and the ability to re-run the grader. The instruction was: don't regress any floor, try to raise the composite.

Specifically, over a single color-expansion pass: concept\_fidelity pass rate moved from 70% to 82% (+12pp) and pedagogical\_scaffolding from 69% to 74% (+5pp). No one explicitly told the agent to improve concept fidelity. The ratchet made the hill it had to climb, and the agent climbed it. When visual\_clarity barely budged (still at 28% pass), that was the next hill - it exposed a layout/text-size problem the color pass could not fix, and pointed the next iteration.

## When the hillclimb breaks

The framework generates a *falsifiable prediction*: with cheap, reliable verification and a monotonic ratchet, average quality will rise without an explicit improvement plan. If it does not rise, one of the preconditions is wrong. The common failure modes:

- -**Verifier is more expensive than the generator.** If checking each attempt costs more than generating it, the ratchet economics flip and the hillclimb halts. Solve verification cost before installing the ratchet.
- -**Goodharted rubric.** A grader that is too legible invites optimization-against-the-proxy. The ratchet will climb, but the thing it climbs is not the thing you wanted. Counter with adversarial evaluation or held-out dimensions.
- -**Local minimum.** If every neighborhood move regresses at least one floor, the ratchet halts before the global optimum. Pair with periodic full-rewrite trials allowed to temporarily break the floor.
- -**Ceiling from below the rubric.** Sometimes the rubric itself tops out before the system is excellent (the visualization case hit a structural ceiling around 30% composite-pass). When that happens, change the rubric - the ratchet is doing its job, but the game is wrong.

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

The mechanism that turns a noisy producer into a monotonically improving asset. The ratchet is the covenant; the floor only goes up. The expected quality path has a non-negative derivative by construction.](/positions/allocator/)[Operator

How you run a team of agents the way you run a team of humans: set the standard, measure against it, promote what clears the bar, send back what doesn't. The gates are the manager.](/positions/operator/)[Builder

Rejection sampling with a monotone ratchet. Generate, evaluate, accept if above floor, reject otherwise. The floor rises with every accepted sample. The agent doesn't need a plan because the gates create ascent.](/positions/builder/)[Scientist

Monte Carlo maximization with a non-decreasing threshold. Under weak regularity conditions the sequence of accepted samples converges to the domain supremum. A martingale-adjacent construction that converts variance into progress.](/positions/scientist/)

See also: [Quality Ratchet](/lexicon/#quality-ratchet) · [Designed Convergence](/frameworks/designed-convergence/) · [AI Operations Tools](/tools/)
