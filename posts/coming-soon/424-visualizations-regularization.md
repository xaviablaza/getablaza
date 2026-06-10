---
title: regularization
description: 'Visualizes regularization as an augmented objective (loss_total = loss_data + λ·penalty) and how different penalties change parameters and generalization: L2 smoothly shrinks weights, L1 drives many weights to exact zeros (sparsity), and Dropout randomly masks units during training to reduce co-adaptation (implicit model averaging).'
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
permalink: /visualizations/regularization/
---

[← ~/visualizations](/visualizations/)

# regularization

Visualizes regularization as an augmented objective (loss\_total = loss\_data + λ·penalty) and how different penalties change parameters and generalization: L2 smoothly shrinks weights, L1 drives many weights to exact zeros (sparsity), and Dropout randomly masks units during training to reduce co-adaptation (implicit model averaging).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Reduce overfitting in linear/logistic regression with L2 weight decay
- 02.Feature selection / sparse models with L1 (LASSO) regularization
- 03.Improve neural network generalization with dropout during training

## technical notes

Time-cycled modes (3s each) animate λ and update a toy weight vector. L2 uses multiplicative shrink; L1 uses soft-thresholding with visual zero snapping; Dropout uses a deterministic per-step RNG mask. All geometry is snapped to a small grid for a blocky green-on-black aesthetic and scales with min(w,h)/240.

[← measure-theory](/visualizations/measure-theory/)[generating-functions →](/visualizations/generating-functions/)
