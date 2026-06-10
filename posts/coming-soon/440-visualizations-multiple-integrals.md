---
title: multiple-integrals
description: Shows a non-rectangular 2D integration region R partitioned into grid cells (ΔA), highlights a moving differential element dA, and builds the signed volume under z=f(x,y) using Riemann-sum boxes. In the latter part of the animation, a scanning slice illustrates Fubini’s theorem by accumulating the same total via different iterated-integration orders (dx then dy vs dy then dx).
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
permalink: /visualizations/multiple-integrals/
---

[← ~/visualizations](/visualizations/)

# multiple-integrals

Shows a non-rectangular 2D integration region R partitioned into grid cells (ΔA), highlights a moving differential element dA, and builds the signed volume under z=f(x,y) using Riemann-sum boxes. In the latter part of the animation, a scanning slice illustrates Fubini’s theorem by accumulating the same total via different iterated-integration orders (dx then dy vs dy then dx).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Compute volumes and signed volumes under surfaces z=f(x,y) over irregular regions
- 02.Mass/charge totals from density functions over an area or volume
- 03.Change of order / iterated integrals (Fubini) for simpler evaluation in applied problems

## technical notes

Pure Canvas2D rendering with a snapped grid for a retro blocky aesthetic. Uses time-based phases (4.2s loop): partition refinement + Riemann-sum assembly, then Fubini scanline highlighting. Volume is drawn with a lightweight pseudo-3D projection and per-cell extrusion; positive/negative heights use different green intensities to emphasize signed volume.

[← projections](/visualizations/projections/)[monte-carlo-methods →](/visualizations/monte-carlo/)
