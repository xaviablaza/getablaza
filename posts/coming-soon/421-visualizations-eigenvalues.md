---
title: eigenvalues-and-eigenvectors
description: Shows how a 2D linear transform A warps the unit square and sends a vector v to Av. A rotating vector gradually snaps to an invariant direction (an eigenspace line), where Av becomes collinear with v and the scaling factor λ is highlighted. A side panel animates det(A−λI) while scanning λ, marking roots (eigenvalues) where the determinant hits 0.
date: '2026-07-01'
scheduled: '2027-08-25'
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
inspiration_url: https://templeton.host/visualizations/eigenvalues/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/eigenvalues/](https://templeton.host/visualizations/eigenvalues/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# eigenvalues-and-eigenvectors

Shows how a 2D linear transform A warps the unit square and sends a vector v to Av. A rotating vector gradually snaps to an invariant direction (an eigenspace line), where Av becomes collinear with v and the scaling factor λ is highlighted. A side panel animates det(A−λI) while scanning λ, marking roots (eigenvalues) where the determinant hits 0.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Stability analysis of dynamical systems (growth/decay along eigendirections)
- 02.PCA / dimensionality reduction (principal eigenvectors of covariance matrices)
- 03.Differential equations and vibrations (modes and natural frequencies)

## technical notes

Uses a fixed 2×2 matrix with real eigenvalues; eigenvalues computed from trace/determinant, eigenvectors from (A−λI)v=0. Blocky aesthetic via snapped DDA pixel-lines on a 4–8px grid. Animation cycles ~4.2s for v→eigenvector and ~2.8s for λ scanning; includes a direction-match meter using normalized dot(v,Av).

[← bayesian-optimization](/visualizations/bayesian-optimization/)[embeddings-(dense-representations) →](/visualizations/embeddings-dense-representations/)
