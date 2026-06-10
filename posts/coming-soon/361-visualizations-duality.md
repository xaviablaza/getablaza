---
title: lagrangian-duality
description: Visualizes how the Lagrangian L(x,λ)=f(x)+λg(x) combines objective and constraints, how the dual function d(λ)=inf_x L(x,λ) produces a lower bound on the primal optimum (weak duality), and how dual ascent updates λ using the constraint residual g(x*(λ)) to maximize d(λ). The left plot shows f(x) and L(x,λ) for a changing multiplier, with horizontal lines for d(λ) and p*. The right panel displays the key equations and live values.
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
permalink: /visualizations/duality/
---

[← ~/visualizations](/visualizations/)

# lagrangian-duality

Visualizes how the Lagrangian L(x,λ)=f(x)+λg(x) combines objective and constraints, how the dual function d(λ)=inf\_x L(x,λ) produces a lower bound on the primal optimum (weak duality), and how dual ascent updates λ using the constraint residual g(x\*(λ)) to maximize d(λ). The left plot shows f(x) and L(x,λ) for a changing multiplier, with horizontal lines for d(λ) and p\*. The right panel displays the key equations and live values.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Deriving dual problems to get computable lower bounds for minimization (certificates of suboptimality)
- 02.Designing algorithms like dual ascent / subgradient methods and projected updates for constrained optimization
- 03.Understanding KKT conditions and when strong duality lets you solve the primal via the dual

## technical notes

Uses a 1D convex quadratic objective with a single inequality constraint so L(x,λ) and d(λ) are explicit. The animation cycles through three stages and, in the final stage, runs a projected dual-ascent update λ←max(0,λ+α g(x\*(λ)) dt). Rendering is grid-snapped for a blocky aesthetic and scaled via scale=Math.min(w,h)/baseSize.

[← pigeonhole-principle](/visualizations/pigeonhole-principle/)[kl-divergence →](/visualizations/kl-divergence/)
