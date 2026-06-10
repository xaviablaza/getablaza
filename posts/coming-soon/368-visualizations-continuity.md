---
title: continuity
description: 'Shows continuity at x=a as a 3-item checklist: (1) f(a) is defined (filled point), (2) the limit exists (left/right approach markers agree), and (3) the limit equals the function value. The animation cycles through broken cases (a hole or a jump) and then smoothly fixes them so lim_{x->a} f(x)=f(a).'
date: '2026-07-01'
scheduled: '2027-07-03'
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
inspiration_url: https://templeton.host/visualizations/continuity/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/continuity/](https://templeton.host/visualizations/continuity/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# continuity

Shows continuity at x=a as a 3-item checklist: (1) f(a) is defined (filled point), (2) the limit exists (left/right approach markers agree), and (3) the limit equals the function value. The animation cycles through broken cases (a hole or a jump) and then smoothly fixes them so lim\_{x->a} f(x)=f(a).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Diagnose discontinuities in piecewise functions (holes vs jumps).
- 02.Understand when limit computations actually tell you the function’s value.
- 03.Justify when calculus rules (like plugging in for polynomials) apply because the function is continuous.

## technical notes

Pure Canvas2D. Uses a snapped grid for a blocky aesthetic, time-based phases to highlight the three continuity conditions, and alternates between removable/jump discontinuities before easing into a corrected continuous function. Responsive scaling via scale = min(w,h)/baseSize.

[← hypothesis-testing](/visualizations/hypothesis-testing/)[tries →](/visualizations/tries/)
