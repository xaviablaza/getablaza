---
title: determinants
description: Shows det(A) as the signed area scaling of the unit square under a 2×2 linear map. The animation cycles through elementary row operations (swap, scale, row-add) by left-multiplying with an operation matrix E, while a side panel numerically confirms multiplicativity det(EA)=det(E)·det(A). When the area collapses toward 0, it highlights singularity (non-invertibility).
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
permalink: /visualizations/determinants/
---

[← ~/visualizations](/visualizations/)

# determinants

Shows det(A) as the signed area scaling of the unit square under a 2×2 linear map. The animation cycles through elementary row operations (swap, scale, row-add) by left-multiplying with an operation matrix E, while a side panel numerically confirms multiplicativity det(EA)=det(E)·det(A). When the area collapses toward 0, it highlights singularity (non-invertibility).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Detecting invertibility/singularity of linear systems (det=0 means no unique solution)
- 02.Computing area/volume scaling and orientation change under linear transformations (graphics/physics)
- 03.Change of variables in integrals and probability (Jacobian determinant)

## technical notes

Pure Canvas2D; uses a 2×2 matrix map of the unit square to a parallelogram (area equals det). Scene-based easing (3×1.2s) interpolates row-operation matrices E, computes A=E·A0, and displays det values to illustrate sign flip, scaling, invariance under row-add, and multiplicativity.

[← propositional-logic](/visualizations/propositional-logic/)[permutations →](/visualizations/permutations/)
