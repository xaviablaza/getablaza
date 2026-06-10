---
title: recurrence-relations
description: Visualizes the pipeline from a linear homogeneous constant-coefficient recurrence to its characteristic polynomial P(r), then shows how roots (and multiplicity) map to solution terms r^n and n^j r^n. A built-in example with a repeated root (r=1, multiplicity 2) demonstrates why the general solution gains an extra n factor, and interactive sliders let you change initial conditions x0 and x1 to see how they uniquely determine the linear-combination coefficients (c0, c1) and the resulting sequence values.
date: '2026-07-01'
scheduled: '2027-09-01'
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
inspiration_url: https://templeton.host/visualizations/recurrence-relations/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/recurrence-relations/](https://templeton.host/visualizations/recurrence-relations/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# recurrence-relations

Visualizes the pipeline from a linear homogeneous constant-coefficient recurrence to its characteristic polynomial P(r), then shows how roots (and multiplicity) map to solution terms r^n and n^j r^n. A built-in example with a repeated root (r=1, multiplicity 2) demonstrates why the general solution gains an extra n factor, and interactive sliders let you change initial conditions x0 and x1 to see how they uniquely determine the linear-combination coefficients (c0, c1) and the resulting sequence values.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Solving algorithm time recurrences (e.g., divide-and-conquer) using characteristic roots
- 02.Analyzing linear feedback shift registers and discrete-time systems
- 03.Deriving closed forms for sequences in combinatorics and counting problems

## technical notes

Pure Canvas2D, green-on-black blocky UI with snapped coordinates. Animation cycles through stages (recurrence -> P(r) -> roots -> general solution) over ~4.2s with easing-based reveals and a sweeping cursor over r and n. Optional interactivity: pointer events on the canvas adjust two sliders for initial conditions; coefficients are computed from the displayed recurrence with a repeated root.

[← joint-distributions](/visualizations/joint-distributions/)[second-order-optimization →](/visualizations/second-order-methods/)
