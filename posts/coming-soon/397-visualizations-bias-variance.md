---
title: bias-variance-tradeoff
description: Shows f(x) (true function) and multiple learned f_hat(x) curves from different training sets. At a fixed input x, it visualizes bias as the gap between f(x) and E[f_hat(x)], variance as the spread of f_hat(x) across datasets, and a stacked bar for noise + bias^2 + variance. Model complexity animates over time to demonstrate underfitting (high bias) to overfitting (high variance).
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
permalink: /visualizations/bias-variance/
---

[← ~/visualizations](/visualizations/)

# bias-variance-tradeoff

Shows f(x) (true function) and multiple learned f\_hat(x) curves from different training sets. At a fixed input x, it visualizes bias as the gap between f(x) and E[f\_hat(x)], variance as the spread of f\_hat(x) across datasets, and a stacked bar for noise + bias^2 + variance. Model complexity animates over time to demonstrate underfitting (high bias) to overfitting (high variance).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Choosing model capacity/regularization strength (e.g., tree depth, polynomial degree, neural net size)
- 02.Explaining why cross-validation helps estimate generalization error
- 03.Diagnosing underfitting vs overfitting and selecting bias/variance reduction strategies

## technical notes

Deterministically simulates multiple training sets with noisy samples around a fixed true function. A complexity parameter blends a low-variance linear fit with a high-variance kernel smoother; predictions at a fixed x are aggregated to estimate bias and variance. Uses snapped drawing, green-on-black palette, and a 4.2s ping-pong animation cycle.

[← ensemble-methods](/visualizations/ensemble-methods/)[spectral-graph-theory →](/visualizations/spectral-graph-theory/)
