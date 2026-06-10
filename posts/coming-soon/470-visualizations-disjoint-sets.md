---
title: disjoint-sets
description: Visualizes Union-Find as a forest of parent-pointer trees. The animation walks a find(x) path to the representative (root), then demonstrates path compression rewiring nodes directly to the root, and finally performs a union(a,b) that attaches one root under the other using union-by-rank to keep the trees shallow (near-constant amortized time).
date: '2026-07-01'
scheduled: '2027-10-13'
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
inspiration_url: https://templeton.host/visualizations/disjoint-sets/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/disjoint-sets/](https://templeton.host/visualizations/disjoint-sets/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# disjoint-sets

Visualizes Union-Find as a forest of parent-pointer trees. The animation walks a find(x) path to the representative (root), then demonstrates path compression rewiring nodes directly to the root, and finally performs a union(a,b) that attaches one root under the other using union-by-rank to keep the trees shallow (near-constant amortized time).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Kruskal’s algorithm for Minimum Spanning Tree (cycle detection)
- 02.Dynamic connectivity in graphs (online union/find queries)
- 03.Connected-component labeling / clustering (grouping items by equivalence)

## technical notes

Rebuilds a deterministic Union-Find state each cycle from a scripted sequence of operations, then overlays phase-based animations (find tracer, compression rewires, union link) on top. Layout is recomputed from the current parent[] forest each frame; nodes/edges snap to a coarse grid for a blocky retro aesthetic. Uses GREEN/GREEN\_DIM on black with time-based easing for smooth motion.

[← clustering](/visualizations/clustering/)[numerical-stability-and-conditioning →](/visualizations/numerical-stability/)
