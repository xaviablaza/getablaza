---
title: Quadrant Shifting
description: Capital investments that move AI tasks to better quadrant positions. The playbook for turning "do not automate" into "automate now."
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- tools
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
permalink: /tools/quadrant-shifting/
---

[← AI Operations Tools](/tools/)

# Quadrant Shifting

[Stage 5Compound](/thesis/#stage-5)

The [Verification Quadrant](/tools/verification-quadrant/) is not destiny. Capital investments can move tasks to better positions. These are the five moves that change where a task sits on the grid.

Start with a scenario

Verification trap

Easy calc, hard check - build a verifier

Avoid zone

Hard both ways - decompose the task

Hard calculation

Expensive compute - enrich inputs

Fuzzy verification

Subjective checks - constrain outputs

Download JPEGCopy ImageCopy URLEmbed

Drag the before-dot to reposition the task. Pick a shift below to see where it moves.

Customize shiftStart: (8, 8) | Move: none▾

## The Grid

Select an investment type below to see how it shifts tasks on the quadrant.

Verification Difficulty →

Verification Trap

Do Not Automate

Automate Now

AI Sweet Spot

Calculation Difficulty →

## The Five Moves

↓ Build a VerifierShifts tasks downward

Do Not Automate / Verification Trap → AI Sweet Spot / Automate Now

↙ Decompose the TaskShifts tasks left and down

Do Not Automate → Multiple smaller tasks in better quadrants

← Enrich InputsShifts tasks left

High calculation difficulty → Lower calculation difficulty

↓ Constrain OutputsShifts tasks down

High verification difficulty → Lower verification difficulty

↓ Build a RubricShifts tasks down

Subjective "is this good?" verification → Structured scoring against criteria

## The Capital Allocation Frame

Each of these five moves is a capital investment. The same questions you would ask about buying a machine apply here:

NPVWhat is the present value of all future labor savings minus the investment cost? Example: a verifier that saves 40 hours/week at $50/hour is worth $104k/year before discounting.

DEPRECIATIONModels depreciate (distribution shift, competitive catch-up). But verifiers and data moats can appreciate - each failure case makes them smarter. The net rate determines whether this is a wasting asset or a compounding one.

RISK-ADJUSTEDThe [Dollarized Confusion Matrix](/tools/dollarized-confusion-matrix/) gives you the variance. High cost asymmetry means high variance in outcomes. Risk-adjusted return = E[NPV] - λ × Var[NPV].

MOATWhat does it cost a competitor to replicate your position? Models: low moat (commodity). Data from operations: high moat. Custom verifiers encoding institutional knowledge: highest moat.

DUAL CURVEPhysical assets depreciate. Knowledge assets have a [dual curve](/lexicon/dual-curve/): the model depreciates (like a truck) but the data and verifiers appreciate (like land under the depot). Invest in the appreciating side.

## The Decision Sequence

These tools form a workflow:

1.**DIAGNOSE** - Plot the task on the [Verification Quadrant](/tools/verification-quadrant/). Calculate the Ablaza Ratio.

2.**CALIBRATE** - Use the [Dollarized Confusion Matrix](/tools/dollarized-confusion-matrix/) to set the right threshold from error costs.

3.**INVEST** - Choose which shift moves the task to a better quadrant. Evaluate the investment using capital allocation math.

4.**VALUE** - Calculate the [NPV of the automation](/tools/automation-npv/) to compare against physical alternatives. Same math, different asset class.

## When to Use This

### Use when

- +A task sits in a hard quadrant and you are willing to spend capital to move it
- +You can estimate the cost of reducing calculation or verification difficulty
- +Task volume is large enough to pay back the shift investment
- +You are choosing between making the task easier vs trying harder at it

### Skip when

- -The task is already in the sweet spot - no shift is needed
- -Shift cost exceeds the NPV of the shifted task (run Automation NPV first)
- -The difficulty is intrinsic (adversarial input, ambiguous ground truth)
- -You have not yet diagnosed the quadrant (use Verification Quadrant first)

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

CapEx for OpEx leverage. Spend once on a verifier or a constraint; the task moves to a cell where automation has positive NPV forever after.](/positions/allocator/)[Operator

The move where you invest in tooling so next quarter's version of the same decision is cheaper. Makes the work easier to scale without growing headcount.](/positions/operator/)[Builder

Building the test infrastructure, the constraint language, the decomposition, the rubric. Each move shifts a stubborn task into a cell you can actually automate.](/positions/builder/)[Scientist

A structural intervention on the cost function. Instead of optimizing over the existing quadrant, you change which quadrant the task occupies - a change of measure in cost-space.](/positions/scientist/)

## See also

[Lexicon

Quadrant Shifting →](/lexicon/#quadrant-shifting)[Position

Allocator →

Which bets to make. Capital allocation, M&A due diligence, portfolio construction.](/positions/allocator/)[Position

Operator →

How to execute at scale. Multi-brand portfolio, turnarounds, P&L ownership.](/positions/operator/)[Position

Builder →

Builds it, ships it, owns it. Solo full-stack, DevOps, production systems.](/positions/builder/)[Position

Scientist →

Proves it, models it, publishes it. Mathematical modeling, Bayesian frameworks.](/positions/scientist/)[Answer

The task is in a bad quadrant. What capital investment mo... →

Quadrant Shifting](/tools/quadrant-shifting/)

See also: [Verification Quadrant](/tools/verification-quadrant/) · [Dollarized Confusion Matrix](/tools/dollarized-confusion-matrix/) · [All Tools](/tools/)
