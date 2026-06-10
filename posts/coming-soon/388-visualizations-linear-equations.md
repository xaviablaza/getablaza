---
title: linear-equations
description: Visualizes y = mx + b as a constant-rate (slope) plus offset (intercept). The animation reveals b as the y-intercept at (0,b), steps along the slope using rise/run to place another point, draws the full line through all points, then demonstrates algebraic isolation to solve for x using inverse operations.
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
source_format: html
inspiration_url: https://templeton.host/visualizations/linear-equations/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/linear-equations/](https://templeton.host/visualizations/linear-equations/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# linear-equations

Visualizes y = mx + b as a constant-rate (slope) plus offset (intercept). The animation reveals b as the y-intercept at (0,b), steps along the slope using rise/run to place another point, draws the full line through all points, then demonstrates algebraic isolation to solve for x using inverse operations.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Convert between units with a fixed rate and offset (e.g., temperature C↔F)
- 02.Model constant-speed motion with a starting position (distance vs time)
- 03.Fit and interpret simple linear trends in data (slope as rate, intercept as baseline)

## technical notes

Pure Canvas2D. Uses a 3.6s staged timeline with ease() for smooth reveals. Grid/geometry are snapped to a 4px\*scale grid for a blocky aesthetic. Responsive scaling via scale = min(w,h)/240 and logical-to-screen coordinate mapping for graphing.

[← covariance-and-correlation](/visualizations/covariance-correlation/)[conditional-probability →](/visualizations/conditional-probability/)
