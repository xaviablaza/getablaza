---
title: graph-coloring
description: 'Animated walkthrough of vertex coloring on a triangle graph (K3): it tries k=1 and k=2 colorings and highlights edge conflicts during an edge-by-edge verification sweep, then shows a proper k=3 coloring and the equivalent partition into 3 independent sets, concluding χ(G)=3.'
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
permalink: /visualizations/graph-coloring/
---

[← ~/visualizations](/visualizations/)

# graph-coloring

Animated walkthrough of vertex coloring on a triangle graph (K3): it tries k=1 and k=2 colorings and highlights edge conflicts during an edge-by-edge verification sweep, then shows a proper k=3 coloring and the equivalent partition into 3 independent sets, concluding χ(G)=3.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Exam timetabling / scheduling (conflicting events cannot share a time slot)
- 02.Register allocation in compilers (interference graph coloring)
- 03.Frequency/channel assignment in wireless networks (adjacent transmitters need different channels)

## technical notes

Uses a 3-stage 3.6s cycle (k=1 → k=2 → k=3). Conflict detection is visualized by sweeping through edges and flashing an X on a conflicting checked edge. Coloring is shown both as node labels and as a partition into color-class bins (independent sets). All rendering is canvas 2D with grid-snapped blocky shapes and green-on-black palette; responsive scaling via scale=min(w,h)/240.

[← information-bottleneck](/visualizations/information-bottleneck/)[information-theoretic-bounds →](/visualizations/information-theoretic-lower-bounds/)
