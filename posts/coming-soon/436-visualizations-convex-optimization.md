---
title: convex-optimization
description: Shows a convex feasible set (highlighted polygon) with convex objective contours inside it. Animated “descent” iterates from multiple starting points converge to the same argmin, illustrating that for convex objectives over convex sets any local minimum is a global minimum. A brief non-convex overlay contrasts this by showing different basins (local minima).
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
permalink: /visualizations/convex-optimization/
---

[← ~/visualizations](/visualizations/)

# convex-optimization

Shows a convex feasible set (highlighted polygon) with convex objective contours inside it. Animated “descent” iterates from multiple starting points converge to the same argmin, illustrating that for convex objectives over convex sets any local minimum is a global minimum. A brief non-convex overlay contrasts this by showing different basins (local minima).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Training machine learning models with convex losses (e.g., logistic regression, SVMs)
- 02.Optimal resource allocation and portfolio optimization under convex constraints
- 03.Signal processing and control (least-squares, LASSO, model predictive control subproblems)

## technical notes

Pure Canvas2D. Uses snapped coordinates for a blocky 4px-grid aesthetic. Contours are approximated by a coarse marching-squares style scan clipped to the convex polygon. Animation is time-phased over ~4.2s with easing; descent paths are simple iterative contractions toward the minimizer (and a two-basin toy dynamic for the non-convex contrast).

[← singular-value-decomposition](/visualizations/svd/)[layer-normalization →](/visualizations/layer-normalization/)
