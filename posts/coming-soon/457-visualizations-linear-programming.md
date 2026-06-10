---
title: linear-programming
description: 'Shows a 2D linear program: the feasible region as the intersection of linear constraints (a convex polygon), a moving objective direction c that defines iso-objective lines cᵀx = k, and a simplex-like process that pivots along polygon vertices (basic feasible solutions) to improve cᵀx until reaching an optimal extreme point.'
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
inspiration_url: https://templeton.host/visualizations/linear-programming/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/linear-programming/](https://templeton.host/visualizations/linear-programming/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# linear-programming

Shows a 2D linear program: the feasible region as the intersection of linear constraints (a convex polygon), a moving objective direction c that defines iso-objective lines cᵀx = k, and a simplex-like process that pivots along polygon vertices (basic feasible solutions) to improve cᵀx until reaching an optimal extreme point.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Production planning and resource allocation (maximize profit under capacity constraints)
- 02.Diet/blending problems (meet nutrition/spec targets at minimum cost)
- 03.Network flow and logistics (routing with linear costs and constraints)

## technical notes

Feasible polygon is computed by clipping a large box with half-planes (Sutherland–Hodgman). Objective vector c rotates smoothly; the current iso-objective line is drawn through the animated point. A greedy edge-walk selects improving adjacent vertices to mimic simplex pivots. Rendering uses grid-snapped coordinates for a retro blocky green-on-black look and scales with min(w,h)/BASE.

[← binary-search-trees](/visualizations/bst/)[randomized-algorithms →](/visualizations/randomized-algorithms/)
