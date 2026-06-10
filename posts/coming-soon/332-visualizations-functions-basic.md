---
title: functions
description: 'Shows a function f: A -> B as a mapping from each domain element x in set A to exactly one codomain element y in set B. The animation steps through inputs x1..x5, draws the arrow to its assigned output f(x), and highlights the Range as the subset of B that actually gets hit (some outputs repeat to emphasize Range ⊆ B).'
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
inspiration_url: https://templeton.host/visualizations/functions-basic/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/functions-basic/](https://templeton.host/visualizations/functions-basic/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# functions

Shows a function f: A -> B as a mapping from each domain element x in set A to exactly one codomain element y in set B. The animation steps through inputs x1..x5, draws the arrow to its assigned output f(x), and highlights the Range as the subset of B that actually gets hit (some outputs repeat to emphasize Range ⊆ B).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Reasoning about input/output behavior in programs (functions, APIs)
- 02.Checking whether a relation is a valid function (each input maps to one output)
- 03.Understanding domain/range constraints in math models and data pipelines

## technical notes

Pure Canvas2D. Uses a 4-second cycle; active domain element is highlighted while its arrow is drawn progressively along a blocky polyline. Range elements in B glow when they have been produced. Responsive scaling via scale = min(w,h)/240 with 4px snapping for a retro grid aesthetic.

[← limits](/visualizations/limits/)[expected-value →](/visualizations/expected-value/)
