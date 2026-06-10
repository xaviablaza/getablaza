---
title: second-order-optimization
description: 'Shows how Newton’s method builds a local quadratic model and computes the Newton step by solving H p = −∇f, alongside how quasi-Newton methods (BFGS/L-BFGS) approximate the inverse Hessian via the secant condition B_{k+1} s_k = y_k. The animation cycles through: local model formation, linear-system solve/step, then a B update that makes B s match y, and finally compares Newton vs quasi-Newton step directions.'
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
permalink: /visualizations/second-order-methods/
---

[← ~/visualizations](/visualizations/)

# second-order-optimization

Shows how Newton’s method builds a local quadratic model and computes the Newton step by solving H p = −∇f, alongside how quasi-Newton methods (BFGS/L-BFGS) approximate the inverse Hessian via the secant condition B\_{k+1} s\_k = y\_k. The animation cycles through: local model formation, linear-system solve/step, then a B update that makes B s match y, and finally compares Newton vs quasi-Newton step directions.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Faster convergence near optima in smooth optimization (e.g., logistic regression, least squares)
- 02.Training and fine-tuning ML models when first-order methods stall (ill-conditioned problems)
- 03.Large-scale optimization with L-BFGS where storing/solving full Hessians is too expensive

## technical notes

Uses a 2D quadratic f(x)=0.5 x^T H x + c^T x to render contours and compute ∇f and the Newton step via a 2×2 linear solve. Quasi-Newton is depicted by interpolating B from a scaled identity toward H^{-1} while visualizing the secant vectors s, y=Hs, and the residual ||Bs−y||. Grid-snapped drawing (4px) with green-on-black styling and time-based phase easing.

[← recurrence-relations](/visualizations/recurrence-relations/)[markov-decision-processes →](/visualizations/mdp/)
