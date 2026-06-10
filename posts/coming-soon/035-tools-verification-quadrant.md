---
title: The Verification Quadrant
description: 'The Ablaza Ratio: time_to_do / time_to_check. Map any AI task by calculation difficulty vs. verification difficulty.'
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
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/tools/verification-quadrant/
inspiration_category: tools
---

> Source-copy draft imported from [https://templeton.host/tools/verification-quadrant/](https://templeton.host/tools/verification-quadrant/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← AI Operations Tools](/tools/)

# The Verification Quadrant

[Stage 2Characterize](/thesis/#stage-2)

Based on the [Ablaza Ratio](/lexicon/templeton-ratio/)™

Before automating a task with AI, ask two questions: **How hard is it to do?** and **How hard is it to check?** The ratio between these two numbers - the Ablaza Ratio - determines whether AI will save you time or double it.

Start with a scenario

Drafting an email

Easy to do, easy to check

Writing test cases

Hard calc, cheap verification (sweet spot)

Legal contract review

Easy to do, hard to verify (the trap)

Strategic analysis

Hard to do AND hard to verify (avoid)

Code gen with tests

Hard calc, cheap verification

Download JPEGCopy ImageCopy URLEmbed

Drag the dot in the chart, or open Customize below for sliders.

Customize positionDo: 7 | Check: 2▾

Verification Difficulty →

Verification Trap

Easy to do, hard to check.

Summarization"Compelling" copyTone adjustment

Do Not Automate \*

Hard to do, hard to check.

Strategic analysisLegal contract draftingCreative writingResearch synthesis

Automate Now

Easy to do, easy to check.

Invoice data extractionImage classificationSchema validation

AI Sweet Spot

Hard to do, easy to check.

Code generationProduct descriptionsImage recoloringTranslation

Calculation Difficulty →

EasyHard

Hard to verify

Easy to verify

## The Ablaza Ratio

AI value isn't determined by how impressive the output looks. It is determined by one number: **how much cheaper it is to check than to produce**.

# The Ablaza Ratio

T = time\_to\_do / time\_to\_check

# T = 1 → no value (you are doing the work twice)

# T = 10 → 9x leverage per unit

# T = 100 → transformative (check 100 outputs in the time of 1)

The Verification Quadrant maps the two components of this ratio. Tasks in the [AI Sweet Spot](/lexicon/ai-sweet-spot/) have high T - hard to calculate, easy to verify. This is the P vs NP intuition applied to operations. Generating a solution is expensive but checking it is cheap, and that asymmetry is where automation creates leverage.

The [Verification Trap](/lexicon/verification-trap/) kills more AI pilots than technical failure. The task looks automatable because generation is easy. But "is this output correct?" requires human judgment that scales linearly with volume. T approaches 1. You end up paying for generation *and* review instead of just doing the work once.

## How to Score a Task

### Calculation Difficulty

How hard is it for a human to produce correct output?

Low (0.0 - 0.3)

Lookup, extraction, classification against a known taxonomy. Anyone trained on the format can do it reliably.

High (0.7 - 1.0)

Requires domain expertise, synthesis across sources, or creative judgment. Takes a skilled human meaningful time.

### Verification Difficulty

How hard is it to determine whether the output is correct?

Low (0.0 - 0.3)

Binary pass/fail, compiles-or-not, diff against ground truth, spot-check values. A machine or a quick glance can verify.

High (0.7 - 1.0)

Requires reading carefully, expert judgment, or "is this good?" assessment. Verification takes nearly as long as doing the work.

## Decision Rules

LOW / LOWAutomate for volume - value comes from throughput, not skill replacement, and full autonomy is safe.

HIGH / LOWAutomate aggressively. This is where AI creates transformative ROI. Build quality gates on the cheap verification and scale.

LOW / HIGHDon't automate until you can make verification cheaper. Invest in rubrics, deterministic checks, or decomposition before deploying AI.

HIGH / HIGHDo not automate *yet*. No cheap feedback signal means no quality gates - unless you build one. See below.

[Framework →Stage 5: Compound

## The Capital Value of Verifiers

The quadrant above describes the *current* state of a task; it is not permanent. Build a verifier and you permanently move the task across the diagram - red into blue, amber into green. And unlike almost every other capital asset, the verifier **appreciates through operating use**: every failure caught is encoded, and the next run inherits the catch.

Read the framework: investment math, what counts as a verifier, fail conditions, and why this is the highest-leverage move in an AI operating budget →](/frameworks/verifier-capital/)

## When to Use This

### Use when

- +Triaging a backlog of AI candidates and you need to sort them fast
- +Deciding whether the capital investment is the generator or the verifier
- +Engineering and business need a shared vocabulary for what is hard
- +You want a quick visual before doing the heavier Automation NPV work

### Skip when

- -You need a single number - compute the Ablaza Ratio directly
- -The task is fully deterministic and no AI is involved
- -Both axes are already well understood and the team just needs to ship
- -You are past categorization and into execution (use the Promotion Protocol)

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

A pre-investment underwriting map. The upper-right cell (generation hard, verification cheap) is where deployed capital earns return; the lower-left is a trap dressed as progress.](/positions/allocator/)[Operator

A placement test for any task the team might automate. Plot it before the vendor demo. If the task isn't in "automate now," walk.](/positions/operator/)[Builder

A build-vs-decline map. Generation hard plus verification cheap equals build. Anything else, you're shipping infrastructure that hasn't earned its keep.](/positions/builder/)[Scientist

A partition of task space along two orthogonal cost axes. Each cell implies a distinct optimal policy. Quadrant-shifting is the capex operation that changes cell membership.](/positions/scientist/)

## See also

[Lexicon

Ablaza Ratio →](/lexicon/#templeton-ratio)[Lexicon

Verification Trap →](/lexicon/#verification-trap)[Lexicon

AI Sweet Spot →](/lexicon/#ai-sweet-spot)[Lexicon

Quadrant Shifting →](/lexicon/#quadrant-shifting)[Tool

What Factory Are You? →](/tools/factory-typology/)[Position

Allocator →

Which bets to make. Capital allocation, M&A due diligence, portfolio construction.](/positions/allocator/)

See also: [AI Operations Tools](/tools/)
