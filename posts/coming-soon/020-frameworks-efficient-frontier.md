---
title: The Operating Efficient Frontier
description: Markowitz (1952) applied to operating investments. The set of portfolios that maximize expected return for a given level of risk.
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
source_format: html
inspiration_url: https://templeton.host/frameworks/efficient-frontier/
inspiration_category: frameworks
---

> Source-copy draft imported from [https://templeton.host/frameworks/efficient-frontier/](https://templeton.host/frameworks/efficient-frontier/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← Frameworks](/frameworks/)

# The Operating Efficient Frontier

[Stage 3Construct](/thesis/#stage-3)

Given a set of candidate operating instruments with known expected returns, variances, and pairwise correlations, the efficient frontier is the set of portfolio compositions that maximize expected return at each level of risk. By definition, points below the frontier are dominated - for any dominated portfolio, there is at least one frontier portfolio with the same risk and higher return, or the same return and lower risk. Markowitz (1952) proved the construction for securities. The same construction applies to operating investments.

risk (σ)E[R]efficient frontierdominatedefficientsame risk, higher return

## How To Construct It

**Stage 2 feeds Stage 3.** Every operating instrument that passes [verification quadrant](/tools/verification-quadrant/) screening is characterized by four numbers: expected return E[R], standard deviation σ, execution dependencies (which other projects it shares a team, stack, or review queue with), and time-to-payoff. The first three are the inputs to the frontier.

**Solve.** For each target level of risk, find the portfolio composition (weights across instruments) that maximizes expected return. Under Gaussian returns, closed-form via quadratic programming. Under operating returns (non-Gaussian, skewed, bounded), iterative or scenario-based. The output is a curve in (E[R], σ)-space.

**The result is not the answer.** The frontier is a set, not a point. Picking a point requires the [risk tolerance map](/frameworks/risk-tolerance/) that translates firm-level constraints into a preferred position. Two allocators with the same frontier and different firms will pick different portfolios - and both will be correct.

**The real work.** In public equities, you estimate μ and Σ from historical returns. In operating investments, the covariance matrix comes from [correlation analysis](/frameworks/correlation/) on execution dependencies, and the P(success) estimates come from Stage 2 pricing. Both have high estimation error. Solving the frontier is the easy part; getting the inputs right is the work.

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

The classical Markowitz problem, run on operating instruments. The frontier is the non-dominated set of portfolios in (E[R], sigma)-space. Everything below is dominated; the question is which point on the frontier the firm wants, not whether to be on it.](/positions/allocator/)[Operator

The set of possible Q3 plans, each with an expected outcome and a risk profile. Some plans are strictly dominated by others with the same risk and better return. Those are the easy cuts.](/positions/operator/)[Builder

Given a quarter's engineering capacity, the set of build combinations that maximize delivered value at each level of delivery risk. Stop arguing about which feature is best; solve the combination.](/positions/builder/)[Scientist

Mean-variance optimization (Markowitz, 1952). Pareto-efficient boundary in (E[R], sigma)-space. Closed-form under Gaussian assumptions; numerical under operating returns (non-Gaussian, skewed, bounded). The covariance matrix is the hard input.](/positions/scientist/)

## Related

- [Capital Allocation](/frameworks/capital-allocation/) - the Stage 3 spine. The frontier is one component; the full stage also includes risk tolerance mapping and correlation.
- [Risk Tolerance Map](/frameworks/risk-tolerance/) - what lets you select a point on the frontier.
- [Correlation](/frameworks/correlation/) - why operating portfolios are not sums of individual NPVs.
- [Kill Protocol](/frameworks/kill-protocol/) - how to identify instruments that should not be on the frontier at all.

## Falsifiable prediction

A *falsifiable prediction* from this framework: portfolios on the constructed frontier will Pareto-dominate hand-picked portfolios drawn from the same instrument menu, measured over a 4-to-8-quarter realization window. If a hand-picked portfolio matches or beats the frontier composition on both expected return and realized variance, either the inputs were wrong (estimation error masking signal), or the optimization is misspecified for the actual return distribution - fat tails, regime changes, or path-dependent payoffs the mean-variance objective cannot represent.

See also: [Frameworks](/frameworks/) · [Thesis](/thesis/) · [Tools](/tools/)
