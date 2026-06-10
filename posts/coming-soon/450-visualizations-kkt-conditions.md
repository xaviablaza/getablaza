---
title: kkt-conditions
description: 'Visualizes KKT for an inequality-constrained optimization: a point x moves toward the feasible set (inside a circle). The left panel shows the feasible region and vectors for -∇f (unconstrained descent), μ∇g (constraint push), and the stationarity residual ∇f+μ∇g shrinking near the solution. The right panel is a live KKT checklist with gauges for primal feasibility g(x)≤0, multiplier μ≥0, and complementary slackness μ·g(x)=0.'
date: '2026-07-01'
scheduled: '2027-09-23'
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
inspiration_url: https://templeton.host/visualizations/kkt-conditions/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/kkt-conditions/](https://templeton.host/visualizations/kkt-conditions/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# kkt-conditions

Visualizes KKT for an inequality-constrained optimization: a point x moves toward the feasible set (inside a circle). The left panel shows the feasible region and vectors for -∇f (unconstrained descent), μ∇g (constraint push), and the stationarity residual ∇f+μ∇g shrinking near the solution. The right panel is a live KKT checklist with gauges for primal feasibility g(x)≤0, multiplier μ≥0, and complementary slackness μ·g(x)=0.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Checking optimality conditions in constrained ML/regularized problems (e.g., SVM, L1/L2 constraints)
- 02.Deriving dual problems and interpreting multipliers (shadow prices) in operations research
- 03.Implementing/understanding constrained solvers (SQP, interior-point) and diagnosing active constraints

## technical notes

Uses a simple 2D toy problem with one inequality constraint g(x)=x1^2+x2^2−1≤0. The animated point follows a preset path and is smoothly projected to the boundary when outside to illustrate feasibility. μ is computed each frame via least-squares stationarity μ\* = −(∇f·∇g)/||∇g||^2 clamped to μ≥0; complementary slackness is shown as the product μ·g(x). All drawing is grid-snapped for a blocky aesthetic and scales with canvas size.

[← zero-sum-games](/visualizations/zero-sum-games/)[norms →](/visualizations/norms/)
