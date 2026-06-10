---
title: equivalence-relations
description: Shows how an equivalence relation (~) partitions a set into disjoint equivalence classes, and how that same structure appears as block-diagonal 1s in the relation matrix. The animation alternates between highlighting a class in the partition, querying whether a~b by checking if they lie in the same class, and emphasizing reflexive/symmetric/transitive structure (diagonal, mirror cells, and solid class blocks).
date: '2026-07-01'
scheduled: '2027-08-20'
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
inspiration_url: https://templeton.host/visualizations/equivalence-relations/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/equivalence-relations/](https://templeton.host/visualizations/equivalence-relations/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# equivalence-relations

Shows how an equivalence relation (~) partitions a set into disjoint equivalence classes, and how that same structure appears as block-diagonal 1s in the relation matrix. The animation alternates between highlighting a class in the partition, querying whether a~b by checking if they lie in the same class, and emphasizing reflexive/symmetric/transitive structure (diagonal, mirror cells, and solid class blocks).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Reasoning about congruence classes (e.g., arithmetic mod n) and grouping values by “same remainder”.
- 02.Quotienting data by an equivalence (deduplication/normalization: different representations treated as the same object).
- 03.Building partitions for clustering/connected-components where “equivalent” means “in the same component”.

## technical notes

Pure Canvas2D; responsive via scale=min(w,h)/260 and grid snapping for a blocky aesthetic. Uses a fixed set U={1..8} and a fixed partition to derive the relation matrix (cell=1 iff same class). Cycles through segments (2–5s total) using phase=(t/duration)%1 with ease() for smooth highlights; includes a tiny built-in 3x5 pixel font for labels to avoid external dependencies.

[← decision-trees](/visualizations/decision-trees/)[rlhf →](/visualizations/rlhf/)
