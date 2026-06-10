---
title: Automation NPV
description: Calculate the NPV of an AI automation investment. Compare to hiring, SaaS, or status quo. CFO math for knowledge work.
date: '2026-07-01'
scheduled: '2026-07-29'
tags:
- p-and-l-engineering
- coming-soon
- tools
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/tools/automation-npv/
inspiration_category: tools
---

> Source-copy draft imported from [https://templeton.host/tools/automation-npv/](https://templeton.host/tools/automation-npv/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← AI Operations Tools](/tools/)

# Automation NPV

[Stage 2Characterize](/thesis/#stage-2)

Every automation has two numbers that matter: what it costs to construct, and the risk-adjusted value of the process it creates. The spread between them is the entire investment thesis.

## The [Construction Spread](/lexicon/construction-spread/)

A factory costs $X to build and generates $Y/year in risk-adjusted value. The spread Y/X tells you how fast the asset pays for itself and where it ranks against alternatives. Knowledge assets work the same way - with the added property that the value stream can appreciate rather than decay.

# construction spread

S = (annual\_value × P(success)) / build\_cost

# deploy capital where S is highest

rank = sort(candidates, by=S, descending)

You can only allocate that which has been assessed. Assess the spread on each opportunity individually, then rank to decide where the next dollar goes.

Start with a scenario

Quick win

Low build cost, high volume, fast payback

Enterprise deployment

High upfront, steady multi-year value

Speculative R&D

Low success probability, long horizon

Steady-state operations

Moderate everything, predictable returns

Product CategorizationCompliance LabelingContract Review

Medium volume, high error cost. The verifier investment is expensive but the compliance risk justifies it. Data moat appreciates as regulatory knowledge accumulates.

Customize financial inputsBuild: $80.0k | Vol: 10,000/mo | Horizon: 3 yr▾

## The Spread

Construction Cost

$80.0k

Risk-Adjusted Annual Value

$36.0k

$48.0k × 75%

Construction Spread

0.45x

Slow payback - check assumptions

## Valuation

NPV

$-1.6k

IRR

11%

Payback

30mo

ROI

22%

Annual Cash Flows (risk-adjusted savings, drift-adjusted)

Y0

Y1

Y2

Y3

Net asset drift:-5%/yr(depreciating - model decay outpaces learning)

Download JPEGCopy ImageCopy URLEmbed

## Compare Candidates

Save

Assess each [soft spot](/lexicon/soft-spot/) individually, save it, then compare. The ranking tells you where the next dollar goes.

## The Physical Capital Mapping

Purchase price

Often lower than physical, but hidden costs in verification design

Build cost (dev + integration + verifier)

Operating cost

Scales sub-linearly (unlike physical). Marginal cost approaches zero.

Compute + API + verification labor per item

Revenue / savings

Quantifiable via Tools 1-2. Not a guess.

Labor cost displaced - AI cost - error cost

Risk adjustment

Physical assets have construction risk too. Knowledge assets have an additional axis: will the AI actually work?

P(success) - probability the system reaches target performance

Depreciation

Often cliff-shaped, not gradual. Major version releases reset the curve.

Model drift + competitive erosion

Appreciation

The unique property of knowledge assets. Physical assets almost never appreciate.

Data moat + verifier learning + process knowledge

Salvage value

Can exceed original build cost. The data outlives the model.

Transferable training data + learned verifiers

Replacement cost

This IS the moat. Models are commodity. Data and verifiers are not.

Cost for a competitor to replicate your data + verifiers

## The Punchline

The construction spread is the same metric a PE fund uses to rank deals: risk-adjusted return on deployed capital. The only difference is the asset class. A warehouse robot depreciates from day one. A knowledge asset with a strong data moat appreciates.

The model depreciates like a truck. The data and verifiers appreciate like land under the depot. **Invest in the appreciating side.**

Use commodity models (they're the truck - replaceable, depreciating). Build proprietary verifiers and data pipelines (they're the land - typically unique, compounding). The [Quadrant Shifting](/tools/quadrant-shifting/) playbook tells you what to build. The construction spread tells you whether it pencils out and where it ranks.

## When to Use This

### Use when

- +You can bound error rates, rework costs, and an adoption curve
- +A status-quo baseline exists (current labor spend, incumbent tool cost)
- +You are ranking three or more competing automation candidates
- +The investment is reversible enough to commit capital against a forecast

### Skip when

- -The value is mostly optionality, not recurring cash flow
- -Adoption risk dominates - users will reject it regardless of ROI
- -Both costs and savings are fuzzy enough to span a 10x range
- -Regulatory or compliance bright-lines override the cash math

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

A DCF for an operating instrument. Inputs are build cost, runtime cost, volume, and the dual curve (model depreciation vs verifier appreciation). Output is NPV at the firm's cost of capital.](/positions/allocator/)[Operator

The answer to "is this automation worth it?" beyond gut feel. Populate the inputs from real numbers - the team's actual unit cost, the real error rate - and get a go/no-go.](/positions/operator/)[Builder

The spreadsheet that prevents you from building something cool that loses money. If the NPV is negative you shouldn't ship it, however elegant the solution.](/positions/builder/)[Scientist

A discounted-cash-flow model with stochastic inputs. Sensitivity analysis (partial derivatives with respect to each input) identifies which assumptions actually matter.](/positions/scientist/)

## See also

[Lexicon

Construction Spread →](/lexicon/#construction-spread)[Lexicon

Dual Curve →](/lexicon/#dual-curve)[Position

Allocator →

Which bets to make. Capital allocation, M&A due diligence, portfolio construction.](/positions/allocator/)[Position

Operator →

How to execute at scale. Multi-brand portfolio, turnarounds, P&L ownership.](/positions/operator/)[Position

Builder →

Builds it, ships it, owns it. Solo full-stack, DevOps, production systems.](/positions/builder/)[Position

Scientist →

Proves it, models it, publishes it. Mathematical modeling, Bayesian frameworks.](/positions/scientist/)

See also: [Verification Quadrant](/tools/verification-quadrant/) · [Dollarized Confusion Matrix](/tools/dollarized-confusion-matrix/) · [Quadrant Shifting](/tools/quadrant-shifting/) · [All Tools](/tools/)
