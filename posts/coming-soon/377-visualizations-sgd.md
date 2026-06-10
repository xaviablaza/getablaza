---
title: stochastic-gradient-descent
description: Shows SGD as repeated parameter updates on a 2D loss surface using a noisy mini-batch gradient estimate g^_t. The true (full-data) gradient direction is shown alongside the stochastic estimate; mini-batch size cycles to demonstrate variance reduction and the unbiased expectation E[g^_t] = ∇f(θ_t).
date: '2026-07-01'
scheduled: '2027-07-12'
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
inspiration_url: https://templeton.host/visualizations/sgd/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/sgd/](https://templeton.host/visualizations/sgd/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# stochastic-gradient-descent

Shows SGD as repeated parameter updates on a 2D loss surface using a noisy mini-batch gradient estimate g^\_t. The true (full-data) gradient direction is shown alongside the stochastic estimate; mini-batch size cycles to demonstrate variance reduction and the unbiased expectation E[g^\_t] = ∇f(θ\_t).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Training neural networks efficiently on large datasets
- 02.Online/streaming learning where data arrives continuously
- 03.Optimization when full gradients are expensive (large n), using mini-batches for a speed/variance trade-off

## technical notes

Implements a simple convex quadratic loss with an unbiased per-example gradient = true gradient + noise. g^\_t is computed by averaging batchSize samples (variance ~ 1/sqrt(batchSize)), then θ is updated once per stepTime. Rendering uses snapped 4px grid alignment for a retro blocky look; animation interpolates θ between discrete updates using the provided ease(t) function.

[← cooperative-games](/visualizations/cooperative-games/)[diffusion-models →](/visualizations/diffusion-models/)
