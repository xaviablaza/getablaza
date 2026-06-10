---
title: arrays
description: Shows an array as one contiguous row of memory cells. The animation moves a cursor to A[i] and highlights how the element address is computed as base + i * element_size (constant-time random access), contrasted with a small scanning animation representing O(n) search.
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
source_format: html
inspiration_url: https://templeton.host/visualizations/arrays/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/arrays/](https://templeton.host/visualizations/arrays/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# arrays

Shows an array as one contiguous row of memory cells. The animation moves a cursor to A[i] and highlights how the element address is computed as base + i \* element\_size (constant-time random access), contrasted with a small scanning animation representing O(n) search.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Fast random access by index (tables, buffers, images)
- 02.Storing fixed-size records contiguously for cache-friendly iteration
- 03.Building blocks for higher-level structures (stacks, heaps, dynamic arrays)

## technical notes

Time-based index cycling (900ms) drives the highlight and cursor interpolation. The address formula is drawn in monospace with a stepped highlight of base/index/size/result. All geometry is scale-responsive and snapped to a coarse grid for a retro blocky aesthetic.

[← trees](/visualizations/trees/)[sequences →](/visualizations/sequences/)
