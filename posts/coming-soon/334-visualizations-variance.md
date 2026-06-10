---
title: variance
description: Shows a set of sample values on a number line with the mean bc marked. For each sample it draws the deviation (X-bc) and a corresponding squared-deviation bar, illustrating variance as E[(X-bc)^2]. The right panel animates a linear transform Y=aX+b and compares measured Var(Y) against the rule Var(aX+b)=a^2Var(X), while also showing c3=sqrt(Var).
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
permalink: /visualizations/variance/
---

[← ~/visualizations](/visualizations/)

# variance

Shows a set of sample values on a number line with the mean bc marked. For each sample it draws the deviation (X-bc) and a corresponding squared-deviation bar, illustrating variance as E[(X-bc)^2]. The right panel animates a linear transform Y=aX+b and compares measured Var(Y) against the rule Var(aX+b)=a^2Var(X), while also showing c3=sqrt(Var).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Comparing how spread out two datasets are (risk/volatility, quality control)
- 02.Understanding standard deviation as a scale of typical error around the mean
- 03.Predicting how scaling a signal (gain) changes noise power via a^2 variance scaling

## technical notes

Deterministic pseudo-random samples are generated once and reused. Animation cycles every ~4s, smoothly adjusting a and b; an active sample index steps to emphasize the expectation/averaging idea. All geometry is grid-snapped for a blocky aesthetic and scales with canvas size using scale=Math.min(w,h)/240.

[← counting-principles](/visualizations/counting-basic/)[multivariable-calculus →](/visualizations/multivariable-calculus/)
