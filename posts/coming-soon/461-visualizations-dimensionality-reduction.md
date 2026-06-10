---
title: dimensionality-reduction
description: 'Shows a set of points in a simulated high-dimensional space (left) being mapped by f: R^D → R^d into a low-dimensional embedding (right). The animation cycles through different preservation criteria (variance, pairwise distances, neighborhood structure) and highlights how choosing a linear vs nonlinear mapping changes what structure can be preserved under the constraint d << D.'
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
permalink: /visualizations/dimensionality-reduction/
---

[← ~/visualizations](/visualizations/)

# dimensionality-reduction

Shows a set of points in a simulated high-dimensional space (left) being mapped by f: R^D → R^d into a low-dimensional embedding (right). The animation cycles through different preservation criteria (variance, pairwise distances, neighborhood structure) and highlights how choosing a linear vs nonlinear mapping changes what structure can be preserved under the constraint d << D.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Compressing features before training models (faster, less overfitting)
- 02.2D/3D visualization of high-dimensional datasets for exploration
- 03.Manifold learning/representation learning for downstream tasks (clustering, retrieval)

## technical notes

Self-contained canvas 2D rendering with a deterministic synthetic manifold dataset. The mapping f blends between a linear projection and a nonlinear ‘unfolding’ warp. The visualization cycles criteria every ~3.6s, highlights a probe point and neighbors, and displays a simple criterion-specific score. Uses grid-snapped drawing for a blocky green-on-black aesthetic and time-based easing for smooth motion.

[← modular-arithmetic](/visualizations/modular-arithmetic/)[policy-gradient-methods →](/visualizations/policy-gradient/)
