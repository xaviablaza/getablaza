---
title: basis-and-dimension
description: 'Two-panel visualization: in R^2 it animates from a single-vector span (a line) to two dependent vectors (still a line) to two independent vectors (fills the plane), emphasizing that a basis is a minimal spanning set. In R^3 it shows that two vectors span only a plane while three independent vectors fill space, reinforcing that dim(V) is the number of vectors in any basis. Pointer movement changes the coefficients in p = a·u (+ b·v) to make span(S) feel interactive.'
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
permalink: /visualizations/basis-dimension/
---

[← ~/visualizations](/visualizations/)

# basis-and-dimension

Two-panel visualization: in R^2 it animates from a single-vector span (a line) to two dependent vectors (still a line) to two independent vectors (fills the plane), emphasizing that a basis is a minimal spanning set. In R^3 it shows that two vectors span only a plane while three independent vectors fill space, reinforcing that dim(V) is the number of vectors in any basis. Pointer movement changes the coefficients in p = a·u (+ b·v) to make span(S) feel interactive.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Choosing a minimal set of features/components (basis) to represent all data in a subspace (e.g., PCA)
- 02.Understanding why you need exactly n independent directions to describe R^n (coordinates, graphics, robotics)
- 03.Detecting redundancy: dependent vectors don’t add span, so they don’t increase dimension

## technical notes

Pure Canvas 2D with a blocky snapped grid (4–8px). Animation cycles through spanning/basis cases in ~4.2s using the provided ease(). A small pointer listener (bound once on the canvas) maps cursor position to coefficients (a,b) to show linear combinations. R^3 is sketched via simple isometric projection and sampled point fills to suggest plane vs volume span.

[← policy-gradient-methods](/visualizations/policy-gradient/)[variational-autoencoders →](/visualizations/vae/)
