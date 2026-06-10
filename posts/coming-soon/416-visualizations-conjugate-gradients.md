---
title: conjugate-gradient-methods
description: 'Shows CG as iterative minimization of an SPD quadratic: left panel draws elliptical level sets and the step-by-step path using A-conjugate search directions (contrasted with a preconditioned variant). Right panel tracks residual norms ||r_k|| and a meter for the A-conjugacy condition p_k^T A p_{k-1}≈0, illustrating independent 1-D minimizations over expanding Krylov subspaces.'
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
permalink: /visualizations/conjugate-gradients/
---

[← ~/visualizations](/visualizations/)

# conjugate-gradient-methods

Shows CG as iterative minimization of an SPD quadratic: left panel draws elliptical level sets and the step-by-step path using A-conjugate search directions (contrasted with a preconditioned variant). Right panel tracks residual norms ||r\_k|| and a meter for the A-conjugacy condition p\_k^T A p\_{k-1}≈0, illustrating independent 1-D minimizations over expanding Krylov subspaces.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Solving large sparse SPD linear systems from PDEs (Poisson, diffusion, FEM stiffness matrices)
- 02.Least-squares and ridge-regularized problems via normal equations (when appropriate)
- 03.Training/solving quadratic models and using preconditioners to accelerate iterative solvers in scientific computing

## technical notes

Implements a fixed 2D SPD quadratic (A,b) and precomputes a few CG/PCG iterates. Animation interpolates along the current segment (eased) and alternates highlighting CG vs PCG each half-cycle. Contours are drawn via coarse grid sampling for a retro blocky look; all geometry is snapped to a pixel grid sized from scale.

[← rlhf](/visualizations/rlhf/)[activation-functions →](/visualizations/activation-functions/)
