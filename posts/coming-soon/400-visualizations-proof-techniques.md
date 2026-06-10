---
title: proof-techniques
description: 'Cycles through three proof strategies and shows how each transforms the original goal into a different logical task: (1) Direct proof builds a chain of implications from premises to the goal, (2) Contradiction assumes the negated goal and animates the derivation of an explicit contradiction (⟂) to conclude the original goal, and (3) Induction breaks a universal claim (∀n) into a base case and an inductive step (n→n+1), then highlights the resulting universal conclusion.'
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
permalink: /visualizations/proof-techniques/
---

[← ~/visualizations](/visualizations/)

# proof-techniques

Cycles through three proof strategies and shows how each transforms the original goal into a different logical task: (1) Direct proof builds a chain of implications from premises to the goal, (2) Contradiction assumes the negated goal and animates the derivation of an explicit contradiction (⟂) to conclude the original goal, and (3) Induction breaks a universal claim (∀n) into a base case and an inductive step (n→n+1), then highlights the resulting universal conclusion.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Choosing an appropriate proof strategy for implications and algebraic properties
- 02.Proving impossibility statements by contradiction (e.g., irrationality, non-existence)
- 03.Proving correctness and invariants of iterative/recursive algorithms using induction

## technical notes

Uses a 4px snap-to-grid helper for a blocky aesthetic, time-based cycling (4.2s) across the three modes, and easing-driven progress bars. Draws only with Canvas 2D primitives (rects, strokes, monospace text) in a green-on-black palette; includes pulsing highlights and moving tokens to emphasize the active logical transformation.

[← spectral-graph-theory](/visualizations/spectral-graph-theory/)[strongly-connected-components →](/visualizations/strongly-connected/)
