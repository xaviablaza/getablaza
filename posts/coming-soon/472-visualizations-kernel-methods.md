---
title: kernel-methods
description: Shows how a kernel function k(x,x') replaces explicit inner products <phi(x),phi(x')> to operate in an implicit feature space. The animation alternates between (1) selecting two input points A,B and evaluating similarity via k(A,B) instead of computing phi, and (2) constructing a small Gram matrix and checking positive-semidefiniteness to illustrate Mercer’s condition for valid kernels.
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
inspiration_url: https://templeton.host/visualizations/kernel-methods/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/kernel-methods/](https://templeton.host/visualizations/kernel-methods/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# kernel-methods

Shows how a kernel function k(x,x') replaces explicit inner products <phi(x),phi(x')> to operate in an implicit feature space. The animation alternates between (1) selecting two input points A,B and evaluating similarity via k(A,B) instead of computing phi, and (2) constructing a small Gram matrix and checking positive-semidefiniteness to illustrate Mercer’s condition for valid kernels.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Kernel SVMs: learn nonlinear decision boundaries using k(x,x') instead of explicit features
- 02.Kernel ridge regression / Gaussian processes: compute predictions from Gram matrices built by k
- 03.Spectral methods / kernel PCA: perform dimensionality reduction in implicit feature space

## technical notes

Pure Canvas2D, grid-snapped blocky drawing with green-on-black palette. Uses time-based phases (4.2s cycle) and an animated scan to depict Gram-matrix construction. Demonstrates PSD vs non-PSD by toggling between an RBF kernel (valid) and an intentionally indefinite similarity (RBF minus constant) and checks PSD via principal minors of a 3x3 Gram matrix.

[← numerical-stability-and-conditioning](/visualizations/numerical-stability/)[derivative-rules →](/visualizations/derivative-rules/)
