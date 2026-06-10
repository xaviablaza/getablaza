---
title: covariance-and-correlation
description: Animated scatterplots show how covariance aggregates the signed products (X-EX)(Y-EY), and how correlation standardizes covariance by sigmaX*sigmaY to produce a unitless value in [-1,1]. The visualization cycles through negative correlation, positive correlation, and a zero-covariance-but-dependent (curved) case to emphasize that Cov=0 does not imply independence.
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
permalink: /visualizations/covariance-correlation/
---

[← ~/visualizations](/visualizations/)

# covariance-and-correlation

Animated scatterplots show how covariance aggregates the signed products (X-EX)(Y-EY), and how correlation standardizes covariance by sigmaX\*sigmaY to produce a unitless value in [-1,1]. The visualization cycles through negative correlation, positive correlation, and a zero-covariance-but-dependent (curved) case to emphasize that Cov=0 does not imply independence.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Detecting linear relationships between features in data analysis and ML feature selection
- 02.Portfolio risk/hedging: understanding co-movement of asset returns (covariance matrix)
- 03.Checking model assumptions and diagnosing multicollinearity using correlation

## technical notes

Generates deterministic pseudo-random samples. Uses correlated Gaussian construction Y=rho\*U+sqrt(1-rho^2)\*V and a dependent zero-covariance example Y=X^2-1. Covariance contributions are visualized via per-point brightness and small deviation-rectangle overlays. Responsive scaling via scale=min(w,h)/260 and grid snapping for a blocky aesthetic.

[← game-theory-introduction](/visualizations/game-theory-intro/)[linear-equations →](/visualizations/linear-equations/)
