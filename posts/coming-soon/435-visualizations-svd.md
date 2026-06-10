---
title: singular-value-decomposition
description: Shows the geometric meaning of SVD by animating the unit circle in the domain as it is transformed step-by-step by Vᵀ (rotation), then Σ (nonnegative axis scaling by singular values), then U (rotation) into an ellipse. The left panel displays right singular vectors (columns of V) on the unit circle; the right panel displays the resulting ellipse with its principal axes aligned to left singular vectors (columns of U) and lengths proportional to σ₁ and σ₂. A step strip reinforces A = UΣVᵀ and the relationship σᵢ = √λᵢ for eigenvalues of AᵀA.
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
permalink: /visualizations/svd/
---

[← ~/visualizations](/visualizations/)

# singular-value-decomposition

Shows the geometric meaning of SVD by animating the unit circle in the domain as it is transformed step-by-step by Vᵀ (rotation), then Σ (nonnegative axis scaling by singular values), then U (rotation) into an ellipse. The left panel displays right singular vectors (columns of V) on the unit circle; the right panel displays the resulting ellipse with its principal axes aligned to left singular vectors (columns of U) and lengths proportional to σ₁ and σ₂. A step strip reinforces A = UΣVᵀ and the relationship σᵢ = √λᵢ for eigenvalues of AᵀA.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Low-rank approximation and compression (PCA-style dimensionality reduction)
- 02.Solving least squares problems and computing pseudoinverses
- 03.Stability/conditioning analysis via singular values and spectral norm

## technical notes

Pure Canvas2D, responsive scaling via scale=min(w,h)/240 and grid snapping for a blocky look. Uses a guaranteed 2×2 example matrix built from chosen U, Σ, V to ensure an exact SVD. The animation interpolates between partial transforms (I→Vᵀ→ΣVᵀ→UΣVᵀ) over a 4.2s cycle using the provided cubic ease(t).

[← logistic-regression](/visualizations/logistic-regression/)[convex-optimization →](/visualizations/convex-optimization/)
