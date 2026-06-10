---
title: limits
description: Shows x approaching a from the left and right while f(x) approaches a single value L, even when the function’s value at x=a is different (a hole at (a,L) and a filled point at (a,f(a))). The animation slows near a to emphasize “arbitrarily close” without reaching the point, and highlights that the two-sided limit exists when left- and right-hand limits match.
date: '2026-07-01'
scheduled: '2027-05-27'
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
inspiration_url: https://templeton.host/visualizations/limits/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/limits/](https://templeton.host/visualizations/limits/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# limits

Shows x approaching a from the left and right while f(x) approaches a single value L, even when the function’s value at x=a is different (a hole at (a,L) and a filled point at (a,f(a))). The animation slows near a to emphasize “arbitrarily close” without reaching the point, and highlights that the two-sided limit exists when left- and right-hand limits match.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Checking continuity and identifying removable discontinuities
- 02.Reasoning about behavior near singularities or breakpoints in models
- 03.Foundation for defining derivatives and integrals in calculus

## technical notes

Renders a piecewise visualization with an open circle at (a,L) and a filled square at (a,f(a)); two animated markers approach a from both sides using cubic easing. Uses grid-snapped coordinates for a blocky aesthetic, green-on-black palette, and responsive scaling via baseSize.

[← slope-and-rate-of-change](/visualizations/slope/)[functions →](/visualizations/functions-basic/)
