---
title: numerical-stability-and-conditioning
description: A four-panel, green-on-black animated dashboard showing how finite-precision arithmetic causes (1) catastrophic cancellation that becomes severe under ill-conditioning (high κ), (2) overflow/underflow in exp-based computations via naive softmax contrasted with a stable log-sum-exp shift, and (3) rounding/quantization spacing that grows with |x| in proportion to ε_machine. A cycling checklist highlights common algebraic reformulations and scaling/normalization fixes used in deep learning to keep computations in safe numeric ranges and reduce error amplification.
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
permalink: /visualizations/numerical-stability/
---

[← ~/visualizations](/visualizations/)

# numerical-stability-and-conditioning

A four-panel, green-on-black animated dashboard showing how finite-precision arithmetic causes (1) catastrophic cancellation that becomes severe under ill-conditioning (high κ), (2) overflow/underflow in exp-based computations via naive softmax contrasted with a stable log-sum-exp shift, and (3) rounding/quantization spacing that grows with |x| in proportion to ε\_machine. A cycling checklist highlights common algebraic reformulations and scaling/normalization fixes used in deep learning to keep computations in safe numeric ranges and reduce error amplification.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Implement stable softmax and log-sum-exp in attention, classification heads, and CRFs
- 02.Diagnose NaNs/Infs and training instability from exploding activations/gradients via scaling/normalization
- 03.Recognize ill-conditioned computations (large κ) where small rounding errors or cancellation produce large relative errors

## technical notes

Uses a 2x2 panel layout with grid-snapped rectangles for a blocky aesthetic. Animations are time-based (3.6–4.2s cycles) with provided ease() shaping. Softmax overflow/underflow is illustrated by simulating float32 exp limits (~±88) while stable softmax shifts by max. Rounding visualization uses ε\_machine≈2.22e-16 and shows spacing ~ ε·|x|. No external dependencies; pure Canvas 2D API.

[← disjoint-sets](/visualizations/disjoint-sets/)[kernel-methods →](/visualizations/kernel-methods/)
