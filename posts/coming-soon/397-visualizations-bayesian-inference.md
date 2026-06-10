---
title: bayesian-inference
description: 'Visualizes a full Bayes update over a parameter θ in [0,1]: a Beta prior p(θ), a Binomial likelihood p(x|θ) from animated data (n trials, k successes), and the resulting posterior p(θ|x). The animation phases highlight the conceptual pipeline (prior → likelihood → multiply → normalize by evidence), while the equation and evidence term are shown in a HUD box.'
date: '2026-07-01'
scheduled: '2027-08-01'
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
inspiration_url: https://templeton.host/visualizations/bayesian-inference/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/bayesian-inference/](https://templeton.host/visualizations/bayesian-inference/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# bayesian-inference

Visualizes a full Bayes update over a parameter θ in [0,1]: a Beta prior p(θ), a Binomial likelihood p(x|θ) from animated data (n trials, k successes), and the resulting posterior p(θ|x). The animation phases highlight the conceptual pipeline (prior → likelihood → multiply → normalize by evidence), while the equation and evidence term are shown in a HUD box.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Updating a coin-bias estimate as flips arrive (A/B testing conversion rates)
- 02.Bayesian parameter estimation and uncertainty quantification in ML models
- 03.Online decision-making: continually revising beliefs as new measurements come in

## technical notes

Renders prior/likelihood/posterior as blocky histograms on a θ-grid with green-on-black styling. Uses Beta-Binomial conjugacy for posterior (Beta(a+k,b+n−k)) and approximates evidence via discrete integration of prior·likelihood. Animation is time-phased over a 4s cycle with easing; data k updates discretely to show how posterior reacts.

[← np-completeness](/visualizations/np-completeness/)[ensemble-methods →](/visualizations/ensemble-methods/)
