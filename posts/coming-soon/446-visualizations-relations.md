---
title: relations
description: Visualizes a binary relation R as a highlighted subset of the Cartesian product A×A (grid of ordered pairs) alongside an equivalent directed-graph view. The animation cycles through the defining properties - reflexive (add diagonal pairs/loops), symmetric (mirror pairs across the diagonal / opposite arrows), and transitive (add implied “shortcut” pairs from length-2 paths) - ending with the idea of an equivalence relation requiring all three.
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
permalink: /visualizations/relations/
---

[← ~/visualizations](/visualizations/)

# relations

Visualizes a binary relation R as a highlighted subset of the Cartesian product A×A (grid of ordered pairs) alongside an equivalent directed-graph view. The animation cycles through the defining properties - reflexive (add diagonal pairs/loops), symmetric (mirror pairs across the diagonal / opposite arrows), and transitive (add implied “shortcut” pairs from length-2 paths) - ending with the idea of an equivalence relation requiring all three.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Modeling “is related to” connections (e.g., friendship, reachability, preferences) as a set of ordered pairs
- 02.Verifying whether a relation defines an equivalence relation to form partitions/quotient sets
- 03.Understanding closures (reflexive/symmetric/transitive closure) used in graph algorithms and data consistency rules

## technical notes

Single self-contained Canvas2D draw function. Uses time-based phases (4.2s loop) with provided cubic ease for smooth transitions. Left panel renders A×A as a snapped grid with highlighted cells for pairs in R; right panel renders the same pairs as arrows between blocky node boxes. Transitivity stage animates a witness path a→b→c and the implied shortcut a→c, then adds additional implied pairs.

[← matrix-calculus](/visualizations/matrix-calculus/)[zero-sum-games →](/visualizations/zero-sum-games/)
