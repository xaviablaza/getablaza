---
title: activation-functions
description: Visualizes an activation function as an elementwise mapping a=f(z) and its local gradient f'(z) used in backprop. The animation scans z across the input range while cycling through ReLU, sigmoid, and tanh, showing how saturation (small f') causes vanishing gradients and how different nonlinearities change forward outputs and training dynamics.
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
permalink: /visualizations/activation-functions/
---

[← ~/visualizations](/visualizations/)

# activation-functions

Visualizes an activation function as an elementwise mapping a=f(z) and its local gradient f'(z) used in backprop. The animation scans z across the input range while cycling through ReLU, sigmoid, and tanh, showing how saturation (small f') causes vanishing gradients and how different nonlinearities change forward outputs and training dynamics.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Choosing activations (ReLU vs tanh/sigmoid) based on gradient flow and saturation behavior
- 02.Diagnosing vanishing gradients by recognizing when f'(z) is near zero for typical z ranges
- 03.Explaining why nonlinear activations are required for deep networks to model non-linear relationships

## technical notes

Pure Canvas2D; responsive scale via baseSize. Uses a step-based cycle (ReLU/sigmoid/tanh) and an eased scanner that moves z across [-4,4]. Plots are drawn as low-resolution polylines with snapped coordinates for a blocky aesthetic; saturation regions are shaded and backprop signal is shown as g\_out = g\_in \* f'(z).

[← conjugate-gradient-methods](/visualizations/conjugate-gradients/)[bayesian-optimization →](/visualizations/bayesian-optimization/)
