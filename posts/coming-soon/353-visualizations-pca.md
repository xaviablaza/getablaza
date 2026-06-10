---
title: principal-component-analysis
description: Shows a 2D correlated point cloud, computes its covariance matrix, and animates how PCA finds orthogonal eigenvector axes (v1, v2). Points then project onto v1 to illustrate dimensionality reduction, while eigenvalues (λ1, λ2) and a bar chart show explained variance ordering.
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
inspiration_url: https://templeton.host/visualizations/pca/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/pca/](https://templeton.host/visualizations/pca/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# principal-component-analysis

Shows a 2D correlated point cloud, computes its covariance matrix, and animates how PCA finds orthogonal eigenvector axes (v1, v2). Points then project onto v1 to illustrate dimensionality reduction, while eigenvalues (λ1, λ2) and a bar chart show explained variance ordering.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Compressing high-dimensional data for faster training/inference
- 02.Noise reduction by dropping low-variance components
- 03.2D/3D visualization of embeddings or feature vectors

## technical notes

Generates a deterministic elongated dataset, computes 2×2 covariance and analytic eigenvalues/eigenvector, then animates (1) axis rotation toward v1, (2) projection of points onto v1, and (3) k=1 reconstruction line plus explained-variance bars. Uses green-on-black, snapped coordinates for a blocky aesthetic, and time-based easing with a ~4.2s loop.

[← convex-functions](/visualizations/convexity/)[law-of-large-numbers →](/visualizations/law-large-numbers/)
