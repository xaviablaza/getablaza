---
title: taylor-series
description: Shows a function f(x)=1/(1-x) (dim) and its Taylor polynomial P_N(x)=Σ_{k=0..N} x^k (bright). N increases over time to illustrate truncation approaching the full power series near the center a=0. A shaded band marks the radius of convergence |x-a|<1, and a moving probe displays the remainder magnitude |R_N(x)|=|f(x)-P_N(x)| to connect convergence with diminishing error where the series matches the function.
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
permalink: /visualizations/taylor-series/
---

[← ~/visualizations](/visualizations/)

# taylor-series

Shows a function f(x)=1/(1-x) (dim) and its Taylor polynomial P\_N(x)=Σ\_{k=0..N} x^k (bright). N increases over time to illustrate truncation approaching the full power series near the center a=0. A shaded band marks the radius of convergence |x-a|<1, and a moving probe displays the remainder magnitude |R\_N(x)|=|f(x)-P\_N(x)| to connect convergence with diminishing error where the series matches the function.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Approximating functions locally for fast computation (e.g., sin, exp, rational approximations)
- 02.Deriving and reasoning about numerical methods and error bounds (remainders)
- 03.Analyzing convergence behavior of power series solutions in physics/engineering (ODEs, generating functions)

## technical notes

Pure Canvas2D; blocky grid snapping and pixel-style DDA lines. Animation cycles N discretely with eased blending between successive polynomials for smooth transitions. Uses a known series with finite radius of convergence (1/(1-x), R=1) to make convergence region and divergence visually clear; avoids plotting near the singularity at x=1 for stability.

[← law-of-large-numbers](/visualizations/law-large-numbers/)[dynamic-programming →](/visualizations/dynamic-programming/)
