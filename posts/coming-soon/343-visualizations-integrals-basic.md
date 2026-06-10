---
title: integrals
description: Shows a definite integral as a Riemann-sum approximation with rectangles whose count increases toward a limit, highlighting dx as the rectangle width. The lower panel shows the indefinite integral as an antiderivative family F(x)+C, and animates the Fundamental Theorem of Calculus by comparing F(b) and F(a) so their difference matches the accumulated area.
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
permalink: /visualizations/integrals-basic/
---

[← ~/visualizations](/visualizations/)

# integrals

Shows a definite integral as a Riemann-sum approximation with rectangles whose count increases toward a limit, highlighting dx as the rectangle width. The lower panel shows the indefinite integral as an antiderivative family F(x)+C, and animates the Fundamental Theorem of Calculus by comparing F(b) and F(a) so their difference matches the accumulated area.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Compute areas/accumulated change from sampled rates (physics: distance from velocity)
- 02.Numerical integration via Riemann sums/rectangles (engineering approximations)
- 03.Solve differential relationships by finding antiderivatives (control systems, growth models)

## technical notes

Pure Canvas2D. Responsive scaling via scale=min(w,h)/240 and grid snapping for a blocky look. Time-based animation cycles: N ramps 4→32 for Riemann rectangles; a sweeping highlight shows dx. Antiderivative family uses multiple curves with animated constant C; FTC panel animates b sliding and displays F(b)-F(a).

[← nash-equilibrium](/visualizations/nash-equilibrium/)[lagrange-multipliers →](/visualizations/lagrange-multipliers/)
