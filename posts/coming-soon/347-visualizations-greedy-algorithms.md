---
title: greedy-algorithms
description: Visualizes greedy selection on an interval-scheduling timeline (using argmin(finish)) while showing the feasibility boundary after each choice. A dependency diagram highlights that the greedy-choice property relies on optimal substructure, and that each greedy step must preserve feasibility so the remaining subproblem stays valid.
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
permalink: /visualizations/greedy-algorithms/
---

[← ~/visualizations](/visualizations/)

# greedy-algorithms

Visualizes greedy selection on an interval-scheduling timeline (using argmin(finish)) while showing the feasibility boundary after each choice. A dependency diagram highlights that the greedy-choice property relies on optimal substructure, and that each greedy step must preserve feasibility so the remaining subproblem stays valid.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Interval scheduling / resource allocation with non-overlap constraints
- 02.Minimum spanning tree (Kruskal/Prim) greedy edge selection
- 03.Shortest paths with nonnegative weights (Dijkstra) via greedy frontier expansion

## technical notes

Time-based cycle animates discrete greedy steps and a feasibility boundary; a second cycle highlights conceptual dependencies with pulsing arrows. All drawing is grid-snapped for a blocky aesthetic and uses only Canvas 2D primitives with GREEN/GREEN\_DIM on black.

[← approximation-algorithms](/visualizations/approximation-algorithms/)[independence →](/visualizations/independence/)
