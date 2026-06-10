---
title: optimization-introduction
description: 'Shows an optimization problem as (1) a feasible set X (hatched region from constraints) and (2) objective contours f(x). A point x moves into the feasible set, then performs projected descent to reduce f(x) while respecting constraints, and finally highlights first-order local optimality: the gradient ∇f is orthogonal to feasible (tangent) directions (no feasible descent direction).'
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
permalink: /visualizations/optimization-intro/
---

[← ~/visualizations](/visualizations/)

# optimization-introduction

Shows an optimization problem as (1) a feasible set X (hatched region from constraints) and (2) objective contours f(x). A point x moves into the feasible set, then performs projected descent to reduce f(x) while respecting constraints, and finally highlights first-order local optimality: the gradient ∇f is orthogonal to feasible (tangent) directions (no feasible descent direction).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Understanding constrained optimization (engineering design under limits)
- 02.Interpreting gradient-based optimizers with projections (ML training with constraints/regularization)
- 03.Visual intuition for local vs global optima and stationarity/KKT conditions

## technical notes

Pure Canvas2D, green-on-black blocky grid hatch. Feasible set is intersection of a halfspace and a disk; objective is a convex quadratic with tilt. Motion uses time-phased segments and simple iterative projection + gradient steps (no external state). Contours are approximated by sampling and drawing near-level pixels for a retro look.

[← permutations](/visualizations/permutations/)[online-algorithms →](/visualizations/online-algorithms/)
