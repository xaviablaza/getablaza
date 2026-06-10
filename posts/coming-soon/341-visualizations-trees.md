---
title: trees
description: Shows a rooted tree (connected and acyclic) with a distinguished root A. The animation cycles through non-root nodes x, highlights the unique edge from parent(x) to x, and marks leaves (no children) and the root to clarify parent-child direction.
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
inspiration_url: https://templeton.host/visualizations/trees/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/trees/](https://templeton.host/visualizations/trees/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# trees

Shows a rooted tree (connected and acyclic) with a distinguished root A. The animation cycles through non-root nodes x, highlights the unique edge from parent(x) to x, and marks leaves (no children) and the root to clarify parent-child direction.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Representing hierarchies (file systems, org charts)
- 02.Parsing and syntax trees in compilers/interpreters
- 03.Search structures (decision trees, game trees)

## technical notes

Uses a fixed small rooted tree layout with grid-snapped, orthogonal polylines for a blocky aesthetic. Time-based cycling selects a node x every ~900ms; easing/pulsing highlights the unique parent(x) edge. Responsive scaling via scale = min(w,h)/baseSize and a faint grid background.

[← confidence-intervals](/visualizations/confidence-intervals/)[arrays →](/visualizations/arrays/)
