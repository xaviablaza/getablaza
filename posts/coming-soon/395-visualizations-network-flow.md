---
title: network-flow
description: Visualizes a directed capacitated graph with flows f(u,v) on edges (solid) and the residual network (dashed). The animation steps through Ford–Fulkerson augmenting paths, pushing flow by the bottleneck residual capacity. In the final step it highlights the residual-reachable set S, the induced s–t cut (S,T), and the cut capacity, illustrating max-flow min-cut and the fact that a flow is maximum iff no augmenting path exists.
date: '2026-07-01'
scheduled: '2027-07-30'
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
inspiration_url: https://templeton.host/visualizations/network-flow/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/network-flow/](https://templeton.host/visualizations/network-flow/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# network-flow

Visualizes a directed capacitated graph with flows f(u,v) on edges (solid) and the residual network (dashed). The animation steps through Ford–Fulkerson augmenting paths, pushing flow by the bottleneck residual capacity. In the final step it highlights the residual-reachable set S, the induced s–t cut (S,T), and the cut capacity, illustrating max-flow min-cut and the fact that a flow is maximum iff no augmenting path exists.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Traffic / data routing with bandwidth limits
- 02.Bipartite matching and assignment problems (via flow reduction)
- 03.Project selection, circulation with demands, and feasibility checking in networks

## technical notes

Uses a small fixed graph. Each ~0.9s step animates a packet along a chosen augmenting path, then applies augmentation once mid-step. Residual edges are generated from current flows (forward: c-f, backward: f). Minimum cut is computed by BFS reachability from s in the residual graph; cut capacity sums capacities of edges from S to T.

[← curse-of-dimensionality](/visualizations/curse-of-dimensionality/)[np-completeness →](/visualizations/np-completeness/)
