---
title: vector-spaces
description: Animated, step-by-step view of a vector space as an additive abelian group of vectors (showing 0, inverses, and vector addition) together with a field F whose scalars act on vectors via scalar multiplication. The final scene presents a commutative-diagram style check of a compatibility axiom (distributivity), emphasizing that scalar action respects vector addition.
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
permalink: /visualizations/vector-spaces/
---

[← ~/visualizations](/visualizations/)

# vector-spaces

Animated, step-by-step view of a vector space as an additive abelian group of vectors (showing 0, inverses, and vector addition) together with a field F whose scalars act on vectors via scalar multiplication. The final scene presents a commutative-diagram style check of a compatibility axiom (distributivity), emphasizing that scalar action respects vector addition.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Understanding why linear combinations work (core to solving linear systems)
- 02.Interpreting scaling and addition in graphics/physics as structure-preserving operations
- 03.Recognizing the role of fields F (e.g., real numbers) in defining valid scalar multiplication rules

## technical notes

Uses a 4-scene loop (4s total) with cubic easing for smooth transitions. Layout is responsive via scale = min(w,h)/240 and all geometry is snapped to a small grid for a retro blocky aesthetic. Draws vectors with arrowheads and a faint grid; shows the field-action relationship with an action arrow and a distributivity diagram.

[← affine-transformations-(linear-layers)](/visualizations/affine-transformations/)[information-bottleneck →](/visualizations/information-bottleneck/)
