---
title: slope-and-rate-of-change
description: Shows two points on a grid, then animates the horizontal run (delta x) and vertical rise (delta y) between them. The visualization computes slope = (delta y)/(delta x), highlights how the sign indicates direction (increasing/decreasing/flat), and demonstrates “rate per 1 unit of x” with a one-grid-step example on the line.
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
permalink: /visualizations/slope/
---

[← ~/visualizations](/visualizations/)

# slope-and-rate-of-change

Shows two points on a grid, then animates the horizontal run (delta x) and vertical rise (delta y) between them. The visualization computes slope = (delta y)/(delta x), highlights how the sign indicates direction (increasing/decreasing/flat), and demonstrates “rate per 1 unit of x” with a one-grid-step example on the line.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Interpreting charts: how fast something is increasing or decreasing over time
- 02.Comparing rates (e.g., speed, cost per item, growth per day) using rise over run
- 03.Checking whether relationships are positive, negative, or constant in data and models

## technical notes

Pure Canvas2D, green-on-black blocky grid snapped to a fixed cell size. A timed cycle places two points, draws the line, animates run/rise as an L-step, then reveals the slope formula and a unit-step rate indicator. Alternates positive/negative/zero slope modes over time; uses provided ease() for smooth transitions.

[← transformer-block](/visualizations/transformer/)[limits →](/visualizations/limits/)
