---
title: monte-carlo-methods
description: Visualizes expectations as integrals under a target distribution p(x), then approximates E_p[f(X)] with Monte Carlo averages. The animation alternates between direct sampling (X~p) and importance sampling (X~q with weights p/q), while a live error panel shows the characteristic 1/√N accuracy scaling and how variance controls estimator noise.
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
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/visualizations/monte-carlo/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/monte-carlo/](https://templeton.host/visualizations/monte-carlo/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# monte-carlo-methods

Visualizes expectations as integrals under a target distribution p(x), then approximates E\_p[f(X)] with Monte Carlo averages. The animation alternates between direct sampling (X~p) and importance sampling (X~q with weights p/q), while a live error panel shows the characteristic 1/√N accuracy scaling and how variance controls estimator noise.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Estimating integrals that are hard to compute analytically (Bayesian posteriors, high-dimensional integrals)
- 02.Simulation-based forecasting and risk estimation (finance, queueing, reliability)
- 03.Rendering/light transport and probabilistic inference with importance sampling

## technical notes

Pure Canvas2D. Uses a closure to maintain sample state and running variance (Welford). Densities are drawn on [-1,1] with block-snapped geometry for a retro grid aesthetic; samples accumulate over time and the estimator/error panels update each frame. The “true” expectation is approximated via dense quadrature for a stable reference.

[← multiple-integrals](/visualizations/multiple-integrals/)[causal-inference →](/visualizations/causal-inference/)
