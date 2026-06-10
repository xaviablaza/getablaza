---
title: predicate-logic
description: 'Visualizes first-order predicate logic by animating: (1) a domain of discourse D as a set of elements, (2) an interpretation I mapping symbols to meaning (constants to elements, P to a subset of D, R to a subset of D×D), (3) a variable assignment g(x) that moves across the domain, (4) term denotation ⟦x⟧ and ⟦b⟧, (5) atomic formula satisfaction for P(x) and R(x,b), and (6) quantified truth for ∀x P(x) vs ∃x P(x) by scanning the domain.'
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
permalink: /visualizations/predicate-logic/
---

[← ~/visualizations](/visualizations/)

# predicate-logic

Visualizes first-order predicate logic by animating: (1) a domain of discourse D as a set of elements, (2) an interpretation I mapping symbols to meaning (constants to elements, P to a subset of D, R to a subset of D×D), (3) a variable assignment g(x) that moves across the domain, (4) term denotation ⟦x⟧ and ⟦b⟧, (5) atomic formula satisfaction for P(x) and R(x,b), and (6) quantified truth for ∀x P(x) vs ∃x P(x) by scanning the domain.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Understanding model-theoretic semantics (interpretations, assignments, satisfaction)
- 02.Explaining how database relations correspond to predicates and how queries resemble ∀/∃ reasoning
- 03.Building intuition for SMT/verification specs: when formulas become true/false under an interpretation

## technical notes

Pure Canvas2D. Uses a 4-stage loop (≈4.2s) with ease() for smooth transitions. Blocky 6px-scaled snap grid, green-on-black palette. Domain nodes show unary predicate P; directed arrows show binary relation R. Variable token 'x' animates across elements; quantifier stage scans the domain to illustrate ranging.

[← variational-autoencoders](/visualizations/vae/)[support-vector-machines →](/visualizations/svm/)
