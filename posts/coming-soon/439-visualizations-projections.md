---
title: projections
description: Shows orthogonal projection geometrically (a vector v, a subspace line S, a sliding candidate u∈S, then the minimizing orthogonal projection with residual r ⟂ S) and connects it to least squares via the projection operator P = A(A^T A)^{-1}A^T, highlighting that for orthogonal projections P is symmetric and idempotent (P^2 = P).
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
permalink: /visualizations/projections/
---

[← ~/visualizations](/visualizations/)

# projections

Shows orthogonal projection geometrically (a vector v, a subspace line S, a sliding candidate u∈S, then the minimizing orthogonal projection with residual r ⟂ S) and connects it to least squares via the projection operator P = A(A^T A)^{-1}A^T, highlighting that for orthogonal projections P is symmetric and idempotent (P^2 = P).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Least-squares fitting / regression (Ax̂ is the projection of data b onto Col(A))
- 02.Computing closest points on lines/planes (graphics, robotics, constraints)
- 03.Signal denoising by projecting onto a chosen subspace/basis

## technical notes

Two-panel canvas: left panel renders R^2 geometry with a grid-snapped, blocky style; right panel renders P as a 2×2 matrix (using a 2×1 A so P = uu^T) and animates emphasis of P^2=P and P^T=P. Time is segmented into phases (0–1) using ease() to smoothly transition from sliding u to locking at proj\_S(v) and then to operator/least-squares text.

[← auction-theory](/visualizations/auction-theory/)[multiple-integrals →](/visualizations/multiple-integrals/)
