---
title: multivariable-chain-rule
description: 'Shows a concrete composition f: R²→R² feeding into g: R²→R², tracks a moving input point x, evaluates the Jacobians Df(x) and Dg(f(x)), then animates the chain rule by highlighting the row/column used in the matrix product to form D(g∘f)(x). Emphasizes “evaluate Dg at f(x)” and “compose linear maps = multiply matrices.”'
date: '2026-07-01'
scheduled: '2027-07-09'
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
inspiration_url: https://templeton.host/visualizations/chain-rule-multivar/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/chain-rule-multivar/](https://templeton.host/visualizations/chain-rule-multivar/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# multivariable-chain-rule

Shows a concrete composition f: R²→R² feeding into g: R²→R², tracks a moving input point x, evaluates the Jacobians Df(x) and Dg(f(x)), then animates the chain rule by highlighting the row/column used in the matrix product to form D(g∘f)(x). Emphasizes “evaluate Dg at f(x)” and “compose linear maps = multiply matrices.”

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Backpropagation in neural networks (Jacobian products through layers)
- 02.Change of variables and sensitivity analysis in physics/engineering models
- 03.Robotics/kinematics: composing coordinate transforms and their derivatives

## technical notes

Pure Canvas2D; responsive scale via min(w,h)/baseSize and 6px-ish grid snapping for a blocky aesthetic. Uses time-phased animation (3 steps over ~3.6s) plus moving packets on arrows and per-entry row/column highlighting to illustrate Jacobian matrix multiplication.

[← linear-independence](/visualizations/linear-independence/)[orthogonality →](/visualizations/orthogonality/)
