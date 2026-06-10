---
title: pigeonhole-principle
description: Shows n labeled boxes and m discrete items being assigned (mapped) into exactly one box each. The animation alternates between m=n (items can fit one-per-box) and m=n+1, where the extra item forces a collision so at least one box visibly contains 2+ items, illustrating the pigeonhole implication m>n ⇒ some box has ≥2 items.
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
inspiration_url: https://templeton.host/visualizations/pigeonhole-principle/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/pigeonhole-principle/](https://templeton.host/visualizations/pigeonhole-principle/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# pigeonhole-principle

Shows n labeled boxes and m discrete items being assigned (mapped) into exactly one box each. The animation alternates between m=n (items can fit one-per-box) and m=n+1, where the extra item forces a collision so at least one box visibly contains 2+ items, illustrating the pigeonhole implication m>n ⇒ some box has ≥2 items.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Proving duplicates must exist (e.g., two people share a birthday month in a group of 13)
- 02.Lower-bound arguments in algorithms/data structures (forced collisions in hashing)
- 03.Combinatorics proofs (existence of repeated remainders, equal sums, etc.)

## technical notes

Pure Canvas2D, time-cycled 4.2s loop with two steps (m=n then m=n+1). Items interpolate from a start row into snapped grid slots inside boxes using ease(). Counts per box are computed from a deterministic assignment; the colliding box is highlighted and labeled with a ≥2 badge. Layout is responsive via scale = min(w,h)/240 and 6px-ish snapping for a blocky aesthetic.

[← information-theoretic-bounds](/visualizations/information-theoretic-lower-bounds/)[lagrangian-duality →](/visualizations/duality/)
