---
title: strongly-connected-components
description: Shows directed-path reachability (u ->* v) by animating highlighted paths, then flips direction to demonstrate mutual reachability. Finally, it outlines SCCs as equivalence classes (a partition of vertices), making the “maximal strongly connected sets” visually explicit.
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
permalink: /visualizations/strongly-connected/
---

[← ~/visualizations](/visualizations/)

# strongly-connected-components

Shows directed-path reachability (u ->\* v) by animating highlighted paths, then flips direction to demonstrate mutual reachability. Finally, it outlines SCCs as equivalence classes (a partition of vertices), making the “maximal strongly connected sets” visually explicit.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Finding cycles/feedback loops in dependency graphs (build systems, package managers)
- 02.Deadlock detection and analysis in wait-for/resource graphs
- 03.Program analysis and optimization (control-flow graphs, call graphs, component condensation DAG)

## technical notes

Uses a fixed small directed graph with 3 SCCs. Each cycle (~4.2s) animates BFS-derived shortest paths for u ->\* v then v ->\* u, and finally draws bounding boxes per SCC. Grid snapping and square nodes/arrows create a blocky green-on-black aesthetic; scale is responsive via Math.min(w,h)/baseSize.

[← proof-techniques](/visualizations/proof-techniques/)[rate-distortion-theory →](/visualizations/rate-distortion/)
