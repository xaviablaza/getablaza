---
title: curse-of-dimensionality
description: 'Three synchronized panels animate how increasing dimensionality d (with fixed sample count n) changes geometry and learning: (1) volume scales like r^d so “central” mass collapses quickly, (2) the same n samples occupy a vanishing fraction of exponentially many coarse bins (sparsity), and (3) pairwise distances concentrate as relative spread shrinks ~1/√d, reducing distance contrast and raising sample complexity.'
date: '2026-07-01'
scheduled: '2027-07-29'
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
inspiration_url: https://templeton.host/visualizations/curse-of-dimensionality/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/curse-of-dimensionality/](https://templeton.host/visualizations/curse-of-dimensionality/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# curse-of-dimensionality

Three synchronized panels animate how increasing dimensionality d (with fixed sample count n) changes geometry and learning: (1) volume scales like r^d so “central” mass collapses quickly, (2) the same n samples occupy a vanishing fraction of exponentially many coarse bins (sparsity), and (3) pairwise distances concentrate as relative spread shrinks ~1/√d, reducing distance contrast and raising sample complexity.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Explaining why high-dimensional feature spaces need regularization and/or dimensionality reduction
- 02.Building intuition for why nearest-neighbor and distance-based methods degrade in high dimensions
- 03.Motivating architectural choices (bottlenecks, embeddings) and data requirements for deep models

## technical notes

Uses responsive scaling (scale=min(w,h)/240), grid snapping for a retro blocky look, and a 4.2s ease-timed cycle that sweeps d from 1..12. Sparsity uses an occupancy approximation bins\*(1-exp(-n/bins)) for bins=2^d; distance concentration uses analytic mean d/6 and std sqrt(d\*7/180) for uniform [0,1]^d distances, visualized as a narrowing band and a shrinking contrast meter.

[← matrix-decomposition](/visualizations/matrix-decomposition/)[network-flow →](/visualizations/network-flow/)
