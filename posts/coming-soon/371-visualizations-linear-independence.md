---
title: linear-independence
description: Shows two vectors v1 and v2 on a coordinate grid and animates a linear combination c1·v1 + c2·v2. In the independent case, the animated coefficients almost never make the sum land on the zero vector (only the trivial combination does). Then it transitions to a dependent case (v2 = 2·v1) where a nontrivial choice (c1=2, c2=-1) makes the sum exactly 0, illustrating the definition of linear independence via the canonical relation c1·v1 + c2·v2 = 0.
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
permalink: /visualizations/linear-independence/
---

[← ~/visualizations](/visualizations/)

# linear-independence

Shows two vectors v1 and v2 on a coordinate grid and animates a linear combination c1·v1 + c2·v2. In the independent case, the animated coefficients almost never make the sum land on the zero vector (only the trivial combination does). Then it transitions to a dependent case (v2 = 2·v1) where a nontrivial choice (c1=2, c2=-1) makes the sum exactly 0, illustrating the definition of linear independence via the canonical relation c1·v1 + c2·v2 = 0.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Checking whether columns of a matrix form a basis (rank / invertibility intuition)
- 02.Detecting redundancy in feature vectors (ML / signal processing)
- 03.Understanding when systems of linear equations have unique solutions

## technical notes

Responsive scaling via scale=Math.min(w,h)/240 and grid snapping to a block size g for a retro aesthetic. Animation cycles every 3.6s, easing a transition from an independent vector pair to a dependent pair. Linear combination is drawn head-to-tail plus a resulting sum arrow, with a right-side panel showing coefficients and the canonical relation.

[← residual-(skip)-connections](/visualizations/residual-connections/)[multivariable-chain-rule →](/visualizations/chain-rule-multivar/)
