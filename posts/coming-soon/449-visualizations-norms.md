---
title: norms
description: 'Visualizes vector norms by morphing the 2D Lp unit ball (L1 diamond, L2 circle, L∞ square) and cycling through the three norm axioms: absolute homogeneity (scaling αv), triangle inequality (u+v head-to-tail vs ||u||+||v||), and positive-definiteness (vector shrinking to zero). A side panel shows the key formulas and live numeric values for ||v||1, ||v||2, and ||v||∞.'
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
permalink: /visualizations/norms/
---

[← ~/visualizations](/visualizations/)

# norms

Visualizes vector norms by morphing the 2D Lp unit ball (L1 diamond, L2 circle, L∞ square) and cycling through the three norm axioms: absolute homogeneity (scaling αv), triangle inequality (u+v head-to-tail vs ||u||+||v||), and positive-definiteness (vector shrinking to zero). A side panel shows the key formulas and live numeric values for ||v||1, ||v||2, and ||v||∞.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Measuring distances in ML/optimization (L1 vs L2 regularization)
- 02.Bounding errors and proving convergence using triangle inequality
- 03.Choosing metrics for geometry/search (Manhattan, Euclidean, Chebyshev)

## technical notes

Uses a grid-snapped, green-on-black style. The Lp unit ball is drawn via a superellipse approximation with exponent 2/p (p≈16 for ∞) and smoothly interpolated between shapes. Animations are time-based with ease(), and panels are responsive via scale = min(w,h)/240.

[← kkt-conditions](/visualizations/kkt-conditions/)[amortized-analysis →](/visualizations/amortized-analysis/)
