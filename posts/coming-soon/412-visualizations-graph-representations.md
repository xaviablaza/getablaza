---
title: graph-representations
description: Side-by-side animated comparison of adjacency matrix A[i][j] and adjacency list Adj[v]. The animation alternates between (1) checking whether an edge exists (single matrix cell probe vs scanning a vertex’s neighbor list) and (2) iterating neighbors (scanning an entire matrix row vs walking just the adjacency-list entries). A bottom bar morphs graph density to show the Θ(n²) vs Θ(n+m) space tradeoff.
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
permalink: /visualizations/graph-representations/
---

[← ~/visualizations](/visualizations/)

# graph-representations

Side-by-side animated comparison of adjacency matrix A[i][j] and adjacency list Adj[v]. The animation alternates between (1) checking whether an edge exists (single matrix cell probe vs scanning a vertex’s neighbor list) and (2) iterating neighbors (scanning an entire matrix row vs walking just the adjacency-list entries). A bottom bar morphs graph density to show the Θ(n²) vs Θ(n+m) space tradeoff.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Choose adjacency matrix for dense graphs or many fast edge-existence queries (O(1) checks).
- 02.Choose adjacency list for sparse graphs and fast neighbor iteration (Θ(deg(v))).
- 03.Reason about memory usage and algorithm complexity in BFS/DFS, Dijkstra/Prim, and graph analytics pipelines.

## technical notes

Pure Canvas2D, green-on-black blocky layout with snapped coordinates. Uses a fixed 6-node example graph; focus vertex cycles over time. Animation toggles every 2s between edge-check and neighbor-iteration modes. Density bar uses a sinusoid to vary m and compares normalized space for n² vs n+m.

[← central-limit-theorem](/visualizations/central-limit-theorem/)[balanced-trees →](/visualizations/balanced-trees/)
