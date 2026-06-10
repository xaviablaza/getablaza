---
title: diffusion-models
description: 'Shows the diffusion workflow in three stages: (1) a forward time-indexed Gaussian noising Markov chain that gradually corrupts a simple blocky “image” according to a noise schedule, (2) a learned denoiser/score model εθ(x_t,t) visualized as a vector field acting on the noisy sample, and (3) the reverse iterative generative process that uses εθ to denoise step-by-step from pure noise back to data.'
date: '2026-07-01'
scheduled: '2027-07-13'
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
inspiration_url: https://templeton.host/visualizations/diffusion-models/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/diffusion-models/](https://templeton.host/visualizations/diffusion-models/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# diffusion-models

Shows the diffusion workflow in three stages: (1) a forward time-indexed Gaussian noising Markov chain that gradually corrupts a simple blocky “image” according to a noise schedule, (2) a learned denoiser/score model εθ(x\_t,t) visualized as a vector field acting on the noisy sample, and (3) the reverse iterative generative process that uses εθ to denoise step-by-step from pure noise back to data.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Text-to-image generation (DDPM/latent diffusion sampling loop)
- 02.Audio or signal generation via iterative denoising
- 03.Image editing/inpainting by noising then reversing with conditioning

## technical notes

Pure Canvas2D. Uses a deterministic pseudo-random function for stable “Gaussian-like” noise per cell and time step. Animation cycles through forward→learn→reverse in ~4.2s using provided cubic ease(). Grid-aligned snapping and rectangular pixels enforce a blocky retro aesthetic; green highlights indicate the active time step t and stage.

[← stochastic-gradient-descent](/visualizations/sgd/)[token-embeddings →](/visualizations/token-embeddings/)
