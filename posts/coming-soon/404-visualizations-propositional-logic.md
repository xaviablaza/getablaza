---
title: propositional-logic
description: Animated truth-functional evaluation of a well-formed formula via a parse tree. The visualization cycles through all truth assignments for atomic propositions p and q, computes each subformula bottom-up (including ¬ and ->), and highlights the corresponding truth-table row to illustrate satisfiability (exists a true row) and validity (all rows true).
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
permalink: /visualizations/propositional-logic/
---

[← ~/visualizations](/visualizations/)

# propositional-logic

Animated truth-functional evaluation of a well-formed formula via a parse tree. The visualization cycles through all truth assignments for atomic propositions p and q, computes each subformula bottom-up (including ¬ and ->), and highlights the corresponding truth-table row to illustrate satisfiability (exists a true row) and validity (all rows true).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Building and debugging boolean conditions in software and hardware
- 02.SAT solving / constraint checking in verification workflows
- 03.Reasoning about entailment and validity in formal methods (specs, proofs, model checking)

## technical notes

Pure Canvas2D, green-on-black blocky UI with grid snapping. Cycles through 4 assignments (p,q) on a fixed WFF (p->q)->(¬p->q). Uses staged easing within each step to animate bottom-up semantics and row highlighting; computes satisfiable/valid from the full truth table each frame.

[← fundamental-theorem-of-calculus](/visualizations/fundamental-theorem/)[determinants →](/visualizations/determinants/)
