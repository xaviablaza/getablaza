---
title: modular-arithmetic
description: Shows integers reduced to residues 0..n−1 on a modular ring, illustrating congruence (a == b (mod n) iff n divides a−b) and how residue classes partition the integers. In inverse mode it animates multiples of a on the ring to demonstrate that an inverse exists exactly when gcd(a,n)=1 (and highlights a^-1 where a·a^-1 == 1 (mod n)).
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
permalink: /visualizations/modular-arithmetic/
---

[← ~/visualizations](/visualizations/)

# modular-arithmetic

Shows integers reduced to residues 0..n−1 on a modular ring, illustrating congruence (a == b (mod n) iff n divides a−b) and how residue classes partition the integers. In inverse mode it animates multiples of a on the ring to demonstrate that an inverse exists exactly when gcd(a,n)=1 (and highlights a^-1 where a·a^-1 == 1 (mod n)).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Clock arithmetic/time calculations with wrap-around
- 02.Hashing/bucketing values into fixed ranges (residues)
- 03.Public-key cryptography basics (modular inverses in RSA/ECC)

## technical notes

Pure Canvas2D, green-on-black blocky UI with snapped grid units. Includes pointer/touch interaction via event listeners attached once to the canvas (stored on the canvas object). Uses time-based cycling to animate wrap-around reduction and inverse search via multiples k·a mod n; extended Euclidean algorithm computes a^-1 when gcd(a,n)=1.

[← sequence-masking-(causal-and-padding-masks)](/visualizations/sequence-masking/)[dimensionality-reduction →](/visualizations/dimensionality-reduction/)
