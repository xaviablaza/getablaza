---
title: support-vector-machines
description: 'Two-panel, green-on-black blocky visualization of SVMs: (left) input space with the maximum-margin separating hyperplane and its ±1 margin lines (canonical scaling, margin = 1/||w||), highlighting that only support vectors (α_i>0) touch/define the margin; (right) the dual/kernelized decision function showing a nonlinear boundary produced by an RBF kernel K(x,x''). The animation morphs from linear to kernel behavior while pulsing the active (nonzero α) points to emphasize sparsity.'
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
permalink: /visualizations/svm/
---

[← ~/visualizations](/visualizations/)

# support-vector-machines

Two-panel, green-on-black blocky visualization of SVMs: (left) input space with the maximum-margin separating hyperplane and its ±1 margin lines (canonical scaling, margin = 1/||w||), highlighting that only support vectors (α\_i>0) touch/define the margin; (right) the dual/kernelized decision function showing a nonlinear boundary produced by an RBF kernel K(x,x'). The animation morphs from linear to kernel behavior while pulsing the active (nonzero α) points to emphasize sparsity.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Text categorization / spam filtering with linear SVMs (high-dimensional sparse features)
- 02.Image classification with kernel SVMs on engineered features
- 03.Outlier/novelty-related pipelines (conceptual link: margins and support vectors)

## technical notes

Self-contained Canvas2D draw function. Uses a small synthetic dataset and pre-chosen sparse dual coefficients to illustrate support vectors. Computes w = Σ α\_i y\_i x\_i for linear margin lines and renders a blocky decision field by sampling f(x) on a coarse grid; smoothly mixes linear score with kernel score over a ~4.2s cycle. RBF kernel K(x,x')=exp(-γ||x-x'||^2) with mildly animated γ for intuition. Grid snapping and rect-based “pixel” circles create the retro block aesthetic; responsive scaling via scale=Math.min(w,h)/baseSize.

[← predicate-logic](/visualizations/predicate-logic/)[clustering →](/visualizations/clustering/)
