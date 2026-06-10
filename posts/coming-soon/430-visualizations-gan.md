---
title: generative-adversarial-networks
description: 'Shows a GAN training loop as a minimax game: noise z flows into the Generator G to produce fake samples G(z), both real x and fake samples are scored by the Discriminator D(x)=p(real), and the animation alternates between updating D (better separation) and updating G (better imitation). The left panel displays real vs generated points in a 2D data space with a coarse discriminator confidence field; the right panel shows the z→G→D pipeline, probabilities, and which player is being updated each half-cycle.'
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
permalink: /visualizations/gan/
---

[← ~/visualizations](/visualizations/)

# generative-adversarial-networks

Shows a GAN training loop as a minimax game: noise z flows into the Generator G to produce fake samples G(z), both real x and fake samples are scored by the Discriminator D(x)=p(real), and the animation alternates between updating D (better separation) and updating G (better imitation). The left panel displays real vs generated points in a 2D data space with a coarse discriminator confidence field; the right panel shows the z→G→D pipeline, probabilities, and which player is being updated each half-cycle.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Image synthesis and editing (text-to-image, style transfer variants)
- 02.Data augmentation with synthetic samples for rare classes
- 03.Anomaly detection via discriminator/feature-space mismatch

## technical notes

Self-contained Canvas2D draw function with a simple persistent state (gSkill/dSkill) updated each frame. Uses a 4–8px snapped grid for a blocky aesthetic, GREEN/GREEN\_DIM on black, and a 4s cycle alternating D-step and G-step. Discriminator confidence is visualized via a coarse shaded grid; points are deterministic per frame via a lightweight xorshift PRNG for stable animation.

[← concentration-inequalities](/visualizations/concentration-inequalities/)[common-distributions →](/visualizations/common-distributions/)
