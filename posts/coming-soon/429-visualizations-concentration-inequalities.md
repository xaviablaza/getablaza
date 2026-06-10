---
title: concentration-inequalities
description: Shows how exponential Markov turns a tail event P(S≥t) into an optimization over λ of exp(-λt+ψS(λ)). The bottom-left plot animates the exponent f(λ) and highlights the minimizing λ*. The right panel visualizes cumulant-generating functions (ψ) and how independence makes ψ add across summands, while a quadratic (Hoeffding-style) upper bound illustrates the bounded-difference/sub-Gaussian principle that yields exponential tails.
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- visualizations
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
permalink: /visualizations/concentration-inequalities/
---

[← ~/visualizations](/visualizations/)

# concentration-inequalities

Shows how exponential Markov turns a tail event P(S≥t) into an optimization over λ of exp(-λt+ψS(λ)). The bottom-left plot animates the exponent f(λ) and highlights the minimizing λ\*. The right panel visualizes cumulant-generating functions (ψ) and how independence makes ψ add across summands, while a quadratic (Hoeffding-style) upper bound illustrates the bounded-difference/sub-Gaussian principle that yields exponential tails.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Designing high-probability error bounds for randomized algorithms and Monte Carlo estimates
- 02.Deriving sample-complexity guarantees in learning theory (generalization bounds)
- 03.Confidence intervals for sums/averages of bounded independent measurements (A/B tests, sensors)

## technical notes

Pure canvas 2D. Uses time-based sweep to move threshold t and re-optimize λ via coarse-to-fine grid search. CGF uses ψ(λ)=log cosh(aλ) for a bounded Rademacher variable; sum CGF scales with N and demonstrates additivity; quadratic proxy ψ≤λ^2 a^2/2 visualizes Hoeffding-type control. Blocky look via grid snapping and green-on-black palette.

[← markov-decision-processes](/visualizations/mdp/)[generative-adversarial-networks →](/visualizations/gan/)
