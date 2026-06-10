---
title: linear-regression
description: Shows a set of data points with a line model ŷ = β₀ + β₁x. The line smoothly morphs from a poor initial guess to the least-squares fit while residuals and their squared-error “blocks” visualize SSE = Σ(y−ŷ)². A matrix panel depicts X (with a column of ones for the intercept), β, and y, then highlights the normal equations (XᵀX)β = Xᵀy as the condition ∇β SSE = 0.
date: '2026-07-01'
scheduled: '2027-09-26'
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
inspiration_url: https://templeton.host/visualizations/linear-regression/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/linear-regression/](https://templeton.host/visualizations/linear-regression/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# linear-regression

Shows a set of data points with a line model ŷ = β₀ + β₁x. The line smoothly morphs from a poor initial guess to the least-squares fit while residuals and their squared-error “blocks” visualize SSE = Σ(y−ŷ)². A matrix panel depicts X (with a column of ones for the intercept), β, and y, then highlights the normal equations (XᵀX)β = Xᵀy as the condition ∇β SSE = 0.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Predicting continuous values (e.g., house prices from size)
- 02.Modeling trends and forecasting with simple, interpretable coefficients
- 03.As a building block for more advanced models (regularization, GLMs, neural nets)

## technical notes

Self-contained Canvas 2D draw function. Uses deterministic synthetic data, precomputes the closed-form normal-equation solution for 1D + intercept, and animates β by easing between a start vector and β̂. Residuals are drawn as vertical lines plus blocky squares proportional to |residual| to emphasize SSE minimization. Responsive scaling via scale=Math.min(w,h)/240 and grid snapping for a retro aesthetic.

[← amortized-analysis](/visualizations/amortized-analysis/)[machine-learning-introduction →](/visualizations/ml-intro/)
