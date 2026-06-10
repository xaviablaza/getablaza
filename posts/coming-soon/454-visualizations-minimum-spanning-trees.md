---
title: minimum-spanning-trees
description: Visualizes MST construction using the cut property (safe edge is the lightest crossing a cut) and the cycle property (the heaviest edge on a cycle cannot be in any MST). The animation alternates between a greedy “safe-edge” selection view and a cycle-based exclusion view, highlighting why Kruskal/Prim work.
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
permalink: /visualizations/minimum-spanning-trees/
---

[← ~/visualizations](/visualizations/)

# minimum-spanning-trees

Visualizes MST construction using the cut property (safe edge is the lightest crossing a cut) and the cycle property (the heaviest edge on a cycle cannot be in any MST). The animation alternates between a greedy “safe-edge” selection view and a cycle-based exclusion view, highlighting why Kruskal/Prim work.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Designing low-cost network wiring (fiber/roads/power) while keeping everything connected
- 02.Clustering and image segmentation (graph-based clustering uses MST variants)
- 03.Reducing graph complexity for routing/visualization by keeping a minimum-cost backbone

## technical notes

Self-contained Canvas2D render. Uses a fixed small weighted graph for clarity, precomputes Kruskal MST offline, then animates step-by-step safe-edge selection by computing a cut from the current partial MST and highlighting the minimum crossing edge. Cycle property view traces a specific cycle and marks its heaviest edge as excluded. Blocky Manhattan-routed edges and snapped coordinates maintain a retro grid aesthetic; animation phases run on a 4.5s loop with easing.

[← machine-learning-introduction](/visualizations/ml-intro/)[binary-search-trees →](/visualizations/bst/)
