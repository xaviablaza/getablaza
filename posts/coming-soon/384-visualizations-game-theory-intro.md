---
title: game-theory-introduction
description: Shows a 2×2 payoff matrix u_i(s) for two rational players. Animated scans highlight each player’s best responses (holding the other’s strategy fixed). Cells where both best-response markers overlap pulse to indicate a Nash equilibrium - no player can unilaterally deviate to improve payoff.
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
permalink: /visualizations/game-theory-intro/
---

[← ~/visualizations](/visualizations/)

# game-theory-introduction

Shows a 2×2 payoff matrix u\_i(s) for two rational players. Animated scans highlight each player’s best responses (holding the other’s strategy fixed). Cells where both best-response markers overlap pulse to indicate a Nash equilibrium - no player can unilaterally deviate to improve payoff.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Explaining payoff matrices and strategy profiles in introductory game theory
- 02.Demonstrating best-response reasoning and how Nash equilibria are identified
- 03.Comparing outcomes like cooperation vs. defection and why equilibria can differ from socially optimal results

## technical notes

Pure Canvas2D, green-on-black blocky UI with snapped geometry. Best responses are computed from the payoff table each frame; animation cycles through column/row best-response scans then pulses equilibrium. Responsive scaling via scale = min(w,h)/baseSize; minimal shapes/text for 60fps.

[← positional-encoding](/visualizations/positional-encoding/)[covariance-and-correlation →](/visualizations/covariance-correlation/)
