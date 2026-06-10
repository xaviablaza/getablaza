---
title: measure-theory
description: Visualizes measurability (preimages of measurable sets) using a blocky domain X mapped by f into codomain Y, highlights the preimage f^{-1}(B) for a moving measurable set B, shows sigma-algebra closure cues (complement/union), and animates the Lebesgue integral construction from indicators to simple functions to limits and signed functions, with mu(A) displayed as a filling measure bar.
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
inspiration_url: https://templeton.host/visualizations/measure-theory/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/measure-theory/](https://templeton.host/visualizations/measure-theory/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# measure-theory

Visualizes measurability (preimages of measurable sets) using a blocky domain X mapped by f into codomain Y, highlights the preimage f^{-1}(B) for a moving measurable set B, shows sigma-algebra closure cues (complement/union), and animates the Lebesgue integral construction from indicators to simple functions to limits and signed functions, with mu(A) displayed as a filling measure bar.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Probability theory foundations (events as measurable sets, probabilities as measures)
- 02.Lebesgue integration for expectations and continuous distributions
- 03.Stochastic processes and advanced statistics (measurability, filtrations, Lp spaces)

## technical notes

Pure Canvas2D; responsive scaling via scale=min(w,h)/240 and 6px grid snapping for a retro block aesthetic. Uses a 4-step 4.2s cycle with easing to highlight (1) indicators, (2) simple functions, (3) monotone limits, (4) signed decomposition. A lightweight particle burst suggests countable unions; all colors are GREEN/GREEN\_DIM on black.

[← complexity-classes](/visualizations/complexity-classes/)[regularization →](/visualizations/regularization/)
