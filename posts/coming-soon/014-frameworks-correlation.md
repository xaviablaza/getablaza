---
title: Correlated Execution Risk
description: Operating investments that share a team, stack, review queue, or failure mode aren't independent. Sums of individual NPVs understate tail risk.
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
permalink: /frameworks/correlation/
---

[← Frameworks](/frameworks/)

# Correlated Execution Risk

[Stage 3Construct](/thesis/#stage-3)

Two operating investments that share a team, a stack, a review queue, or a failure mode are not statistically independent. When the shared dependency fails, both fail together. Sharpe ratios can't be summed; NPVs can't be added without an adjustment. Correlation is the input that makes Stage 3 different from Stage 2 - it is why portfolio construction beats project-by-project selection.

Two projects, equal E[R] and σ. Portfolio risk depends on ρ.ρ = -1perfect hedgeσ\_p = 0(theoretical)ρ = 0independentdiversificationσ\_p = σ/√2ρ = +1shared team,shared stack,shared reviewσ\_p = σ(most ops default)Lower bars mean lower portfolio risk. Higher correlation = higher portfolio risk = tighter capacity.

## Where Correlation Comes From

**Shared team.** Two projects staffed from the same team share the same risk of that team getting reorganized, losing a key member, or being pulled to a fire. A 50% shared roster implies meaningful positive correlation.

**Shared stack.** Two automations built on the same model version, the same data pipeline, or the same verifier share the same risk of that stack failing. When the stack breaks, both projects break.

**Shared review queue.** Two projects whose throughput depends on the same human reviewer are correlated in time - the reviewer’s attention is the shared resource. Slippage in one compresses capacity for the other.

**Shared narrative.** If two projects are both pitched as evidence for the same strategic thesis, the failure of one undermines the other even if they are technically independent. The correlation is in the audience’s mind, and that is still real.

## Why the covariance matrix is the hard part

For N instruments, the covariance matrix has N(N−1)/2 off-diagonal entries. For 20 candidate instruments, that is 190 pairwise correlations. In public equities, these are estimated from long historical return series. In operating investments, they must be estimated from execution-dependency structure - which teams, which stacks, which review queues, which narratives.

A common failure mode: treat projects as independent because correlation is hard to estimate. The portfolio looks well-diversified on paper; the actual portfolio has a handful of shared failure modes that make it concentrated. The calibration of the covariance matrix - not the solution of the optimization - is where the [operational alpha](/lexicon/operational-alpha/) of Stage 3 actually comes from.

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

Why portfolio construction beats project-by-project selection. Two instruments with identical E[R] and sigma can have wildly different portfolio effects depending on correlation. Positive correlation amplifies tail risk; negative dampens it. Sharpe ratios don't sum.](/positions/allocator/)[Operator

The reason "we shipped four things and they all slipped the same week" isn't an accident. Shared team, shared stack, shared review queue, shared narrative - shared failure mode. Plan like the projects are correlated because they're.](/positions/operator/)[Builder

Shared execution dependencies are the default, not the exception. Same repo, same infra, same deploy pipeline means same failure surface. Independence has to be engineered - not assumed.](/positions/builder/)[Scientist

The covariance matrix is the input that distinguishes portfolio construction from individual NPV. For N instruments, N(N-1)/2 off-diagonal entries. Typically estimated with high variance; the known hazard of mean-variance optimization (Chopra & Ziemba, 1993).](/positions/scientist/)

## Related

- [Efficient Frontier](/frameworks/efficient-frontier/) - the shape of the frontier depends on the covariance matrix.
- [Risk Tolerance Map](/frameworks/risk-tolerance/) - firms select a point on the frontier based on tolerance; correlation determines which points exist.
- [Capital Allocation](/frameworks/capital-allocation/) - the Stage 3 spine.
- [Kill Protocol](/frameworks/kill-protocol/) - Gate 1 (marginal Sharpe) is a correlation test in disguise.

## Falsifiable prediction

A *falsifiable prediction* from this framework: portfolios constructed by summing individual NPVs without a correlation adjustment will systematically understate realized tail variance over a 4-to-8-quarter window. If realized portfolio variance tracks the independence-assumption model (i.e., shared dependencies don't show up in the variance), the framework is wrong for that operating environment - either the dependencies weren't actually shared, or the failure modes were independent despite the surface coupling.

See also: [Frameworks](/frameworks/) · [Thesis](/thesis/) · [Tools](/tools/)
