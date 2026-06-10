---
title: combinations
description: Visualizes choosing k distinct items from n when order does not matter. The animation first builds an ordered pick (a k-permutation), then rapidly cycles through the k! different orderings of the same chosen items and collapses them into a single unordered subset token, reinforcing that combinations are permutations with order factored out. The bottom panel ties this to the formulas C(n,k)=n!/(k!(n-k)!) and C(n,k)=P(n,k)/k! with a numeric example (n=5,k=3).
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
permalink: /visualizations/combinations/
---

[← ~/visualizations](/visualizations/)

# combinations

Visualizes choosing k distinct items from n when order does not matter. The animation first builds an ordered pick (a k-permutation), then rapidly cycles through the k! different orderings of the same chosen items and collapses them into a single unordered subset token, reinforcing that combinations are permutations with order factored out. The bottom panel ties this to the formulas C(n,k)=n!/(k!(n-k)!) and C(n,k)=P(n,k)/k! with a numeric example (n=5,k=3).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Counting possible teams/committees chosen from a group (order irrelevant)
- 02.Computing probabilities in card/dice problems using binomial coefficients
- 03.Feature subset selection and search-space sizing in algorithms/ML (choose k items from n)

## technical notes

Pure Canvas2D, retro blocky rendering via grid snapping. Time-based 4.2s cycle split into 3 eased segments (pick ordered -> forget order -> show formula/count). Includes a tiny 3x5 pixel font for consistent green-on-black labeling without external fonts.

[← randomized-algorithms](/visualizations/randomized-algorithms/)[channel-capacity →](/visualizations/channel-capacity/)
