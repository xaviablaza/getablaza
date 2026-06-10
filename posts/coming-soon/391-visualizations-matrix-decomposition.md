---
title: matrix-decomposition
description: Visualizes matrix factorization by fading between LU (A = L·U, with an optional P pivot hint) and QR (A = Q·R with QᵀQ = I). Animated cell sweeps suggest the stepwise construction of factors, and the bottom pipeline shows how solving A x = b reduces to simple forward/back triangular solves (LU) or projection + backsolve (QR).
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
permalink: /visualizations/matrix-decomposition/
---

[← ~/visualizations](/visualizations/)

# matrix-decomposition

Visualizes matrix factorization by fading between LU (A = L·U, with an optional P pivot hint) and QR (A = Q·R with QᵀQ = I). Animated cell sweeps suggest the stepwise construction of factors, and the bottom pipeline shows how solving A x = b reduces to simple forward/back triangular solves (LU) or projection + backsolve (QR).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Fast solving of many linear systems via triangular factors (numerical simulation, circuit solving)
- 02.Least-squares fitting and regression using QR (overdetermined systems)
- 03.Determinants/inverses and stability improvements via pivoting (P·A = L·U)

## technical notes

Pure Canvas2D, time-based 4s cycle. Matrices are 4×4 blocky grids with triangular masks; values are deterministic pseudo-random fills for texture (not computed decompositions). Uses responsive scale = min(w,h)/240 and pixel/grid snapping for a retro aesthetic; easing controls sweeps and cross-fades.

[← computational-complexity-theory](/visualizations/computational-complexity/)[curse-of-dimensionality →](/visualizations/curse-of-dimensionality/)
