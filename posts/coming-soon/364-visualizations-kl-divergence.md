---
title: kl-divergence
description: 'Shows two discrete distributions over the same bins: the true distribution P (bright) and a model Q (dim). Samples are drawn from P, and the visualization highlights the per-sample extra log-loss log2(P(X)/Q(X)). A running average and a decomposition into per-bin contributions illustrate that KL divergence is an expectation under P and is always non-negative, reaching 0 only when P and Q match.'
date: '2026-07-01'
scheduled: '2027-06-29'
tags:
- p-and-l-engineering
- coming-soon
- visualizations
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/visualizations/kl-divergence/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/kl-divergence/](https://templeton.host/visualizations/kl-divergence/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# kl-divergence

Shows two discrete distributions over the same bins: the true distribution P (bright) and a model Q (dim). Samples are drawn from P, and the visualization highlights the per-sample extra log-loss log2(P(X)/Q(X)). A running average and a decomposition into per-bin contributions illustrate that KL divergence is an expectation under P and is always non-negative, reaching 0 only when P and Q match.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Measuring how well a probabilistic model Q approximates a true/target distribution P
- 02.Variational inference and VAEs (minimizing D\_KL between approximate and true/posterior distributions)
- 03.Information theory / coding: average extra bits when coding data from P with a code optimized for Q

## technical notes

Uses a discrete-bins approximation: D\_KL(P||Q) ≈ Σ\_i P(i) log(P(i)/Q(i)). Q smoothly shifts/warps away from P over a 4.2s loop. Samples are generated deterministically via a seeded PRNG and inverse-CDF sampling from P, then smoothed with easing for the cursor. All drawing is grid-snapped for a blocky green-on-black aesthetic.

[← lagrangian-duality](/visualizations/duality/)[cross-validation →](/visualizations/cross-validation/)
