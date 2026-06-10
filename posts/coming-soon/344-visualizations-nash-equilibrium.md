---
title: nash-equilibrium
description: 'Shows a 2×2 strategy profile payoff matrix. A moving selection box represents the current strategy profile s=(s1,s2). Animated best-response arrows illustrate unilateral deviations: first Player 1’s best response to s−1, then Player 2’s best response to s−2. When both arrows point back to the selected cell, the panel confirms the Nash equilibrium condition (no profitable unilateral deviation) using the best-response inequalities.'
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
inspiration_url: https://templeton.host/visualizations/nash-equilibrium/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/nash-equilibrium/](https://templeton.host/visualizations/nash-equilibrium/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# nash-equilibrium

Shows a 2×2 strategy profile payoff matrix. A moving selection box represents the current strategy profile s=(s1,s2). Animated best-response arrows illustrate unilateral deviations: first Player 1’s best response to s−1, then Player 2’s best response to s−2. When both arrows point back to the selected cell, the panel confirms the Nash equilibrium condition (no profitable unilateral deviation) using the best-response inequalities.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Predicting stable outcomes in competitive pricing or bidding (no firm wants to change price alone)
- 02.Analyzing strategic choices in cybersecurity/defense where unilateral changes may be exploitable
- 03.Understanding equilibria in mechanism design and auctions (checking for profitable deviations)

## technical notes

Pure Canvas2D. Uses a 4-scene loop (~4s) with ease() for smooth transitions. Best responses are computed from the payoff matrix each frame; arrows and selection are grid-snapped for a blocky aesthetic. Responsive scaling via scale=Math.min(w,h)/baseSize.

[← sequences](/visualizations/sequences/)[integrals →](/visualizations/integrals-basic/)
