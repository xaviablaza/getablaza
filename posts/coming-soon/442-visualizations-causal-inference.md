---
title: causal-inference
description: Side-by-side animated DAGs contrast observational conditioning P(Y|X=x) with intervention P(Y|do(X=x)). A confounder U creates a backdoor path that biases observation; the do-operator visually cuts incoming arrows into X, leaving only the causal effect X→Y. The visualization also hints at identification via backdoor adjustment when U is observed.
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
permalink: /visualizations/causal-inference/
---

[← ~/visualizations](/visualizations/)

# causal-inference

Side-by-side animated DAGs contrast observational conditioning P(Y|X=x) with intervention P(Y|do(X=x)). A confounder U creates a backdoor path that biases observation; the do-operator visually cuts incoming arrows into X, leaving only the causal effect X→Y. The visualization also hints at identification via backdoor adjustment when U is observed.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Estimating treatment effects from observational data (e.g., medicine, policy)
- 02.Diagnosing confounding and choosing adjustment sets with DAGs
- 03.Deciding when observational correlations can identify causal effects (do-calculus/backdoor)

## technical notes

Pure Canvas2D, retro grid-snapped primitives. Two panels crossfade every ~4.2s; animated particles flow along causal edges, with confounder-to-X flow suppressed under intervention. Blocky elbow edges and rectangular arrowheads maintain the homebrew aesthetic; responsive scaling uses scale = min(w,h)/240 with grid size derived from scale.

[← monte-carlo-methods](/visualizations/monte-carlo/)[mechanism-design →](/visualizations/mechanism-design/)
