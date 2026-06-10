---
title: computational-complexity-theory
description: 'Visualizes three core complexity resources/models: (1) space as bounded Turing-machine workspace via a live space meter (SPACE(f(n))), (2) non-uniform Boolean circuit families with size/depth cues, and (3) pseudorandom generators PRG: {0,1}^s → {0,1}^m replacing true randomness. The animation cycles through: randomized computation using coin flips, PRG expansion that ‘fools’ a target circuit class, and derandomization by enumerating all seeds to simulate the randomized algorithm deterministically.'
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
inspiration_url: https://templeton.host/visualizations/computational-complexity/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/computational-complexity/](https://templeton.host/visualizations/computational-complexity/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# computational-complexity-theory

Visualizes three core complexity resources/models: (1) space as bounded Turing-machine workspace via a live space meter (SPACE(f(n))), (2) non-uniform Boolean circuit families with size/depth cues, and (3) pseudorandom generators PRG: {0,1}^s → {0,1}^m replacing true randomness. The animation cycles through: randomized computation using coin flips, PRG expansion that ‘fools’ a target circuit class, and derandomization by enumerating all seeds to simulate the randomized algorithm deterministically.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Explaining why strong PRGs imply derandomization results (e.g., BPP-style simulations for restricted models)
- 02.Teaching resource tradeoffs: space bounds vs. other measures like circuit size/depth
- 03.Building intuition for non-uniform models and why ‘fooling’ a class is the key condition for replacing randomness

## technical notes

Pure Canvas2D, time-based 4.2s loop segmented into three stages. Uses responsive scaling (scale = min(w,h)/240), grid snapping for a blocky aesthetic, and eased stage transitions to fade between true randomness and PRG output. No external dependencies.

[← mcmc](/visualizations/mcmc/)[matrix-decomposition →](/visualizations/matrix-decomposition/)
