---
title: zero-sum-games
description: 'Interactive zero-sum game view: a 2×2 payoff matrix A (Row’s payoff; Column’s payoff is −A), draggable mixed strategies p and q, and the resulting expected payoff p^T A q. The bottom band visualizes minimax security levels (min_q p^T A q and max_p p^T A q) and how they align at the game value v near equilibrium.'
date: '2026-07-01'
scheduled: '2027-09-22'
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
inspiration_url: https://templeton.host/visualizations/zero-sum-games/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/zero-sum-games/](https://templeton.host/visualizations/zero-sum-games/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# zero-sum-games

Interactive zero-sum game view: a 2×2 payoff matrix A (Row’s payoff; Column’s payoff is −A), draggable mixed strategies p and q, and the resulting expected payoff p^T A q. The bottom band visualizes minimax security levels (min\_q p^T A q and max\_p p^T A q) and how they align at the game value v near equilibrium.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Designing robust strategies in adversarial settings (security, pricing, auctions)
- 02.Understanding Nash equilibrium in competitive games via mixed strategies
- 03.Evaluating guarantees: worst-case performance under an optimal opponent

## technical notes

Pure Canvas2D, green-on-black blocky UI. Pointer-driven bars adjust p(R1) and q(C1) with a damped spring for smoothness; when not dragging, strategies auto-oscillate to demonstrate changing expected value. Uses a fixed 2×2 zero-sum matrix so minimax value is clearly shown (v=0) and responsive scaling via scale=min(w,h)/baseSize with grid snapping.

[← relations](/visualizations/relations/)[kkt-conditions →](/visualizations/kkt-conditions/)
