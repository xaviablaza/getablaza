---
title: binary-search-trees
description: 'Visualizes the BST ordering invariant (left keys < key(node) < right keys), then animates a comparison-guided search for a target key by highlighting the visited path and showing each comparison/decision. Finally, it demonstrates a local update via insertion: a new node slides into the correct null position and a single parent->child link is attached, emphasizing how the invariant is preserved by local pointer changes.'
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
permalink: /visualizations/bst/
---

[← ~/visualizations](/visualizations/)

# binary-search-trees

Visualizes the BST ordering invariant (left keys < key(node) < right keys), then animates a comparison-guided search for a target key by highlighting the visited path and showing each comparison/decision. Finally, it demonstrates a local update via insertion: a new node slides into the correct null position and a single parent->child link is attached, emphasizing how the invariant is preserved by local pointer changes.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Fast lookup/insert/delete in ordered sets/maps (e.g., TreeMap-style structures)
- 02.Maintaining sorted data for range queries and in-order traversal output
- 03.Building index structures and symbol tables where ordering matters

## technical notes

Responsive tree layout computed each frame; blocky grid snapping (6px\*scale) for retro look. Animation cycles through SEARCH/INVARIANT/INSERT over ~4.2s using time-based phases and cubic easing. Highlights are drawn with green/green-dim strokes on black and elbow links for a blocky aesthetic.

[← minimum-spanning-trees](/visualizations/minimum-spanning-trees/)[linear-programming →](/visualizations/linear-programming/)
