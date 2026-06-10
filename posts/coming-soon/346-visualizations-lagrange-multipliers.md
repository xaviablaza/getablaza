---
title: lagrange-multipliers
description: Shows a moving point constrained to g(x,y)=0 (a circle) while minimizing f(x,y)=x^2+2y^2. At the constrained optimum, the visualization highlights gradient parallelism by drawing ∇f, ∇g, and λ∇g from the same point and displaying the stationarity condition ∇f = λ∇g alongside feasibility g(x)=0.
date: '2026-07-01'
scheduled: '2027-06-11'
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
inspiration_url: https://templeton.host/visualizations/lagrange-multipliers/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/lagrange-multipliers/](https://templeton.host/visualizations/lagrange-multipliers/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# lagrange-multipliers

Shows a moving point constrained to g(x,y)=0 (a circle) while minimizing f(x,y)=x^2+2y^2. At the constrained optimum, the visualization highlights gradient parallelism by drawing ∇f, ∇g, and λ∇g from the same point and displaying the stationarity condition ∇f = λ∇g alongside feasibility g(x)=0.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Constrained optimization in engineering design (e.g., minimize weight subject to strength constraints)
- 02.Economics/utility maximization under budget constraints
- 03.Machine learning optimization with equality constraints (e.g., normalization constraints)

## technical notes

Pure Canvas2D. The point evolves via tangential descent: v = -∇f + λ∇g with λ = (∇f·∇g)/(∇g·∇g) to make v orthogonal to ∇g, then re-projected to the circle to enforce g(x)=0. Contours are polyline approximations snapped to a pixel grid for a blocky aesthetic; animation is time-based with a 3–5s cycle and periodic restarts.

[← integrals](/visualizations/integrals-basic/)[approximation-algorithms →](/visualizations/approximation-algorithms/)
