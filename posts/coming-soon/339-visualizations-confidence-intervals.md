---
title: confidence-intervals
description: 'Animates repeated sampling: each new sample produces a point estimate θ̂ and a confidence interval θ̂ ± z·se(θ̂). Intervals stack over time and are colored by whether they cover the true parameter θ, illustrating that the method has a long-run coverage rate (not that any single interval has a 95% probability of containing θ).'
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
permalink: /visualizations/confidence-intervals/
---

[← ~/visualizations](/visualizations/)

# confidence-intervals

Animates repeated sampling: each new sample produces a point estimate θ̂ and a confidence interval θ̂ ± z·se(θ̂). Intervals stack over time and are colored by whether they cover the true parameter θ, illustrating that the method has a long-run coverage rate (not that any single interval has a 95% probability of containing θ).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Reporting uncertainty around an estimated mean/proportion (A/B tests, surveys)
- 02.Communicating precision of model parameters (regression coefficients, effects)
- 03.Quality control and experimentation: deciding if measurements are consistent with a target θ

## technical notes

Uses a lightweight deterministic PRNG + Box–Muller to simulate θ̂ ~ Normal(θ, se). New intervals emit every ~0.42s; older ones fade. Canvas coordinates are snapped to a grid for a blocky aesthetic; responsive scaling via scale = min(w,h)/240. True θ is a vertical line; hit/miss intervals use GREEN\_DIM/GREEN.

[← divide-and-conquer](/visualizations/divide-conquer/)[trees →](/visualizations/trees/)
