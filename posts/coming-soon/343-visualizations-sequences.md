---
title: sequences
description: 'Visualizes a sequence as an indexed ordered list (n → a_n). The animation steps through terms and highlights the rule that generates the next term: arithmetic sequences add a constant difference d each step, while geometric sequences multiply by a constant ratio r each step. Recurrence and explicit formulas are shown side-by-side to connect “process” and “closed form.”'
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
inspiration_url: https://templeton.host/visualizations/sequences/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/sequences/](https://templeton.host/visualizations/sequences/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# sequences

Visualizes a sequence as an indexed ordered list (n → a\_n). The animation steps through terms and highlights the rule that generates the next term: arithmetic sequences add a constant difference d each step, while geometric sequences multiply by a constant ratio r each step. Recurrence and explicit formulas are shown side-by-side to connect “process” and “closed form.”

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Modeling linear growth like saving a fixed amount each week (arithmetic)
- 02.Modeling exponential growth/decay like doubling bacteria or compound interest (geometric)
- 03.Recognizing patterns in data streams and predicting the next value from constant difference/ratio

## technical notes

Time-based stepping animates from a\_n to a\_{n+1} with eased interpolation. The visualization alternates modes every ~2.1s (arithmetic/geometric) and uses snapped coordinates for a blocky grid aesthetic. Pure Canvas 2D API; responsive scaling via scale = min(w,h)/baseSize.

[← arrays](/visualizations/arrays/)[nash-equilibrium →](/visualizations/nash-equilibrium/)
