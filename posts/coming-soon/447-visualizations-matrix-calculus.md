---
title: matrix-calculus
description: Visualizes the differential as a linear operator Df(X) acting on a matrix perturbation dX, then shows how matrix derivatives are stored as a Jacobian acting on vec(dX) to produce vec(dY). The animation steps through (1) selecting a component of vec(dX), (2) a Jacobian row performing a dot-product, (3) the resulting component of vec(dY), and (4) the chain rule as composition (Jacobian multiplication). The bottom panel highlights Hessian symmetry by mirroring entries and depicts the quadratic-form view vᵀHv for second differentials after vectorization.
date: '2026-07-01'
scheduled: '2027-09-20'
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
inspiration_url: https://templeton.host/visualizations/matrix-calculus/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/matrix-calculus/](https://templeton.host/visualizations/matrix-calculus/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# matrix-calculus

Visualizes the differential as a linear operator Df(X) acting on a matrix perturbation dX, then shows how matrix derivatives are stored as a Jacobian acting on vec(dX) to produce vec(dY). The animation steps through (1) selecting a component of vec(dX), (2) a Jacobian row performing a dot-product, (3) the resulting component of vec(dY), and (4) the chain rule as composition (Jacobian multiplication). The bottom panel highlights Hessian symmetry by mirroring entries and depicts the quadratic-form view vᵀHv for second differentials after vectorization.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Backpropagation and chain rule implementation in deep learning (Jacobian products)
- 02.Deriving gradients for matrix objectives (trace/inner-product conventions)
- 03.Second-order optimization and curvature diagnostics using Hessians/approximations

## technical notes

Pure Canvas2D rendering with snapped grid geometry for a retro block aesthetic. Time-based animation uses step phases (≈3.6s per 4-step cycle) and easing for smooth sweeps. No external dependencies; responsive scaling via scale = min(w,h)/baseSize; all elements drawn with simple rects/lines for 60fps.

[← jacobian](/visualizations/jacobian/)[relations →](/visualizations/relations/)
