---
title: dynamic-programming
description: Visualizes when dynamic programming applies by contrasting naive recursion (repeated calls to the same state n) with memoization (storing and reusing dp[state]). A Fibonacci-style subproblem graph shows optimal substructure via edges (n depends on n-1 and n-2), while the animated cursor highlights overlapping subproblems and the dp table turning repeated work into cache HITs.
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
permalink: /visualizations/dynamic-programming/
---

[← ~/visualizations](/visualizations/)

# dynamic-programming

Visualizes when dynamic programming applies by contrasting naive recursion (repeated calls to the same state n) with memoization (storing and reusing dp[state]). A Fibonacci-style subproblem graph shows optimal substructure via edges (n depends on n-1 and n-2), while the animated cursor highlights overlapping subproblems and the dp table turning repeated work into cache HITs.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Speeding up recursive algorithms by caching subproblem results (memoization)
- 02.Designing tabulation solutions for shortest paths, knapsack, and sequence alignment
- 03.Defining minimal state parameters (dp[state]) to eliminate exponential recomputation

## technical notes

Uses a fixed DAG layout for states n=0..6 and an animated traversal sequence to demonstrate repeated calls. The cycle splits into two modes (naive recursion vs memoization); in memoization mode, rows become 'computed' and later visits display HIT. All geometry is grid-snapped for a blocky aesthetic and scales with Math.min(w,h)/BASE.

[← taylor-series](/visualizations/taylor-series/)[affine-transformations-(linear-layers) →](/visualizations/affine-transformations/)
