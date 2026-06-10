---
title: jacobian
description: 'Shows a 2D nonlinear map y=f(x) as a warped grid (right) compared to the original grid (left). A draggable point x0 highlights the Jacobian matrix Df(x0) as the best local linear approximation: the animated dx vector in x-space is mapped to y-space both by the true change f(x0+dx)-f(x0) and the linear prediction Df(x0)·dx. A small square around x0 illustrates local area scaling by |det(Df(x0))| (and orientation flip when det<0).'
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
source_format: html
inspiration_url: https://templeton.host/visualizations/jacobian/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/jacobian/](https://templeton.host/visualizations/jacobian/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# jacobian

Shows a 2D nonlinear map y=f(x) as a warped grid (right) compared to the original grid (left). A draggable point x0 highlights the Jacobian matrix Df(x0) as the best local linear approximation: the animated dx vector in x-space is mapped to y-space both by the true change f(x0+dx)-f(x0) and the linear prediction Df(x0)·dx. A small square around x0 illustrates local area scaling by |det(Df(x0))| (and orientation flip when det<0).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Change of variables in double integrals: dA transforms by |det(Df)|
- 02.Linearization for multivariable Newton’s method and local error estimates
- 03.Local distortion/area scaling in graphics, robotics kinematics, and flow maps

## technical notes

Pure Canvas2D. Two panels render grids: identity on the left and the mapped grid on the right. Pointer events on ctx.canvas let the learner drag x0. The visualization animates a rotating dx and overlays the true mapped increment with the linearized increment Df(x0)·dx. Grid-aligned snap (4–8px) enforces a blocky aesthetic; scaling uses scale=Math.min(w,h)/240.

[← topological-sort](/visualizations/topological-sort/)[matrix-calculus →](/visualizations/matrix-calculus/)
