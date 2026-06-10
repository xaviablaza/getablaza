---
title: variational-autoencoders
description: 'Shows the VAE pipeline as an animated, blocky graph: an input x is encoded into variational parameters (μ_φ(x), σ_φ(x)) for q_φ(z|x), sampled via the reparameterization z=μ+σ⊙ε, then decoded through p_θ(x|z) to generate x~. A bottom panel animates the ELBO/KL decomposition as a stacked bar to emphasize that maximizing ELBO tightens the bound by reducing the KL gap.'
date: '2026-07-01'
scheduled: '2027-10-09'
tags:
- p-and-l-engineering
- coming-soon
- visualizations
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/visualizations/vae/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/vae/](https://templeton.host/visualizations/vae/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# variational-autoencoders

Shows the VAE pipeline as an animated, blocky graph: an input x is encoded into variational parameters (μ\_φ(x), σ\_φ(x)) for q\_φ(z|x), sampled via the reparameterization z=μ+σ⊙ε, then decoded through p\_θ(x|z) to generate x~. A bottom panel animates the ELBO/KL decomposition as a stacked bar to emphasize that maximizing ELBO tightens the bound by reducing the KL gap.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Generate new samples similar to training data (images, audio, embeddings)
- 02.Learn compressed latent representations for clustering/interpolation
- 03.Semi-supervised learning and anomaly detection via reconstruction + KL regularization

## technical notes

Pure Canvas2D; responsive scaling via scale=min(w,h)/240 and snapped grid g for a retro aesthetic. Animation cycles ~4.2s through encoder→reparam→decoder→ELBO focus. A small particle system (closure state) visualizes ε flowing into z then into decoder output, reinforcing the reparameterization trick and gradient path.

[← basis-and-dimension](/visualizations/basis-dimension/)[predicate-logic →](/visualizations/predicate-logic/)
