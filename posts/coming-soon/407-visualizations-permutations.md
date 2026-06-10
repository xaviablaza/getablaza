---
title: permutations
description: Shows k-permutations as filling ordered slots from a pool without replacement. The animation steps through each slot to emphasize order sensitivity, then highlights the falling product n·(n−1)·…·(n−k+1) and its equivalence to n!/(n−k)!; includes a special case where k=n to show full permutations equal n!.
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
permalink: /visualizations/permutations/
---

[← ~/visualizations](/visualizations/)

# permutations

Shows k-permutations as filling ordered slots from a pool without replacement. The animation steps through each slot to emphasize order sensitivity, then highlights the falling product n·(n−1)·…·(n−k+1) and its equivalence to n!/(n−k)!; includes a special case where k=n to show full permutations equal n!.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Counting possible PIN/password orderings (without repeating characters)
- 02.Enumerating task/job execution orders in scheduling problems
- 03.Counting arrangements in sampling without replacement (e.g., ordered draws from a deck)

## technical notes

Time-based staged animation: each slot fill is a phase, followed by a formula-equivalence fade-in. Uses grid snapping for a blocky aesthetic, responsive scaling via scale=min(w,h)/baseSize, and simple deterministic selection to illustrate "no replacement".

[← determinants](/visualizations/determinants/)[optimization-introduction →](/visualizations/optimization-intro/)
