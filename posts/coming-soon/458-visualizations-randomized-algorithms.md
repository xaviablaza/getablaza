---
title: randomized-algorithms
description: 'Visualizes how internal random bits r turn an algorithm A(x; r) into distributions over outputs and runtimes (shown as shifting histograms). Contrasts Las Vegas (always correct, random runtime with an evolving runtime histogram and estimated E[T]) versus Monte Carlo (fixed time, probabilistic correctness). Demonstrates amplification by independent repetitions and majority vote: more runs increase cost linearly while the displayed effective error probability drops exponentially.'
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
inspiration_url: https://templeton.host/visualizations/randomized-algorithms/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/randomized-algorithms/](https://templeton.host/visualizations/randomized-algorithms/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# randomized-algorithms

Visualizes how internal random bits r turn an algorithm A(x; r) into distributions over outputs and runtimes (shown as shifting histograms). Contrasts Las Vegas (always correct, random runtime with an evolving runtime histogram and estimated E[T]) versus Monte Carlo (fixed time, probabilistic correctness). Demonstrates amplification by independent repetitions and majority vote: more runs increase cost linearly while the displayed effective error probability drops exponentially.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Randomized quicksort/selection: expected fast runtime (Las Vegas-style analysis of time)
- 02.Primality testing (e.g., Miller–Rabin): bounded-error Monte Carlo with amplification
- 03.Hashing/sketching and streaming algorithms: probabilistic correctness with tight time bounds

## technical notes

Pure Canvas2D, green-on-black blocky rendering via grid snapping. Uses time-cycled story steps (distribution → Las Vegas → Monte Carlo amplification). Monte Carlo repetitions are re-sampled periodically with a seeded LCG for stable visuals; Las Vegas runtime histogram accumulates samples over time and shows an online mean. Easing-based pulsing highlights the active concept.

[← linear-programming](/visualizations/linear-programming/)[combinations →](/visualizations/combinations/)
