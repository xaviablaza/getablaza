---
title: orthogonality
description: Shows two vectors whose angle oscillates through 90°, with a live dot-product bar that hits zero exactly at perpendicularity. In the same orthonormal (axis-aligned) basis, a moving vector v is decomposed into components c1 and c2 using dot products (c_i = e_i·v), and a tiny 2×2 Kronecker-delta grid reinforces e_i·e_j = δ_ij.
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
permalink: /visualizations/orthogonality/
---

[← ~/visualizations](/visualizations/)

# orthogonality

Shows two vectors whose angle oscillates through 90°, with a live dot-product bar that hits zero exactly at perpendicularity. In the same orthonormal (axis-aligned) basis, a moving vector v is decomposed into components c1 and c2 using dot products (c\_i = e\_i·v), and a tiny 2×2 Kronecker-delta grid reinforces e\_i·e\_j = δ\_ij.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Checking perpendicular directions in geometry/physics (work = force·displacement).
- 02.Projecting signals onto orthonormal bases (Fourier/orthogonal transforms).
- 03.Extracting coordinates in an orthonormal basis for graphics, robotics, and numerical linear algebra.

## technical notes

Single-loop time-based animation (3.8–4.2s cycles) with eased highlight when |u·v|≈0. Uses snap-to-grid (4–6px) for a blocky aesthetic, green-on-black palette, and pure Canvas2D drawing (no dependencies).

[← multivariable-chain-rule](/visualizations/chain-rule-multivar/)[cooperative-games →](/visualizations/cooperative-games/)
