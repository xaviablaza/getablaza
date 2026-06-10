---
title: Frameworks
description: The operating system for capital allocation. Find mispriced edges, price instruments, construct the portfolio, execute, compound.
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- frameworks
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
permalink: /frameworks/
---

[← Home](/)

# Frameworks

Conceptual models for running the allocation cycle. Grouped by stage of the cycle - see the [thesis](/thesis/) for the full lattice.

Stage 1

## Find

· Where are the mispriced edges in the operating graph?

[The Factory Typology →

Knowledge work is manufacturing - but which factory? The archetype to borrow from is a function of your input, process, and output signature. Name it and inherit a mature industry's operations playbook. Work in progress, building in public.](/frameworks/factory-typology/)[![Your Chart of Accounts Is a Directed Graph](/img/templeton/frameworks/directed-graph.svg)

Your Chart of Accounts Is a Directed Graph →

Every cost and revenue line is a node. Every causal relationship is an edge. Walk the graph and find the mispriced edges where value is leaking.](/frameworks/directed-graph/)[![The Performance Frontier](/img/templeton/frameworks/performance-frontier.svg)

The Performance Frontier →

A protocol for locating where excellence lives when nobody agrees what good looks like. Map the distribution, find the 99th percentile, compute the gradient toward it.](/frameworks/performance-frontier/)[![The Demand Field](/img/templeton/frameworks/demand-field.svg)

The Demand Field →

Demand is a force field on your optimization landscape. It is fixed, hidden, and acts on your product whether you measure it or not. Map it or crash into it.](/frameworks/demand-field/)

Stage 3

## Construct

· Which instruments, in what combination, given risk tolerance?

[![Capital Allocation](/img/templeton/frameworks/capital-allocation.svg)

Capital Allocation →

Every operating decision is a capital allocation decision. Rank instruments by risk-adjusted return, map your tolerances, handle correlations, and construct the portfolio. Markowitz (1952) applied to operating investments.](/frameworks/capital-allocation/)[![Kill Protocol](/img/templeton/frameworks/kill-protocol.svg)

Kill Protocol →

The most important allocator skill is saying no. Three decision gates for identifying dominated instruments - marginal Sharpe, left-tail survivability, base rate verification - and reallocating the slot.](/frameworks/kill-protocol/)[The Operating Efficient Frontier →

Markowitz (1952) applied to operating investments. The set of portfolios that maximize expected return at each level of risk. By definition, points below the frontier are dominated; the question is which point the firm wants.](/frameworks/efficient-frontier/)[The Risk Tolerance Map →

The function that maps firm-level constraints - cash, runway, covenants, narrative - into the preferred point on the efficient frontier. Two firms with identical inputs pick different points. Both can be correct.](/frameworks/risk-tolerance/)[Correlated Execution Risk →

Operating portfolios are not sums of individual NPVs. Two projects that share a team, stack, or review queue share a failure mode. Correlation is the input that makes Stage 3 different from Stage 2.](/frameworks/correlation/)

Stage 4

## Execute

· How do you realize the returns?

[![Designed Convergence](/img/templeton/frameworks/designed-convergence.svg)

Designed Convergence →

Design the game so that convergence to the desired outcome is a structural guarantee, not a hope. Mechanism design meets Bayesian ratchet search.](/frameworks/designed-convergence/)[![The Deity Problem](/img/templeton/frameworks/deity-problem.svg)

The Deity Problem →

Your AI is trying to serve you but cannot read your mind. Three evidence channels for learning what the operator actually wants: structured elicitation, revealed preference, and direct query.](/frameworks/deity-problem/)[![Quality Hillclimb](/img/templeton/frameworks/quality-hillclimb.svg)

Quality Hillclimb →

Apply ratcheted quality gates to stochastic agent output. The agent doesn't need a plan - the gates create ascent. Rejection sampling with a monotone ratchet.](/frameworks/quality-hillclimb/)[![The Promotion Protocol](/img/templeton/frameworks/promotion-protocol.svg)

The Promotion Protocol →

A 3-state progression for safely giving AI more independence. Promote on demonstrated performance, roll back on drift. Formally: Autonomy State Machine.](/frameworks/promotion-protocol/)

Stage 5

## Compound

· How do you build the appreciating asset?

[![Knowledge Work as Capital](/img/templeton/frameworks/knowledge-capital.svg)

Knowledge Work as Capital →

Every piece of knowledge work either compounds or depreciates. Models decay. Data appreciates. Verifiers learn. The dual curve determines where to invest.](/frameworks/knowledge-capital/)[![The Capital Value of Verifiers](/img/templeton/frameworks/verifier-capital.svg)

The Capital Value of Verifiers →

The verifier is one of the only capital assets that appreciates through operating use. Every failure it catches gets encoded; the next run inherits the catch. Use raises the floor instead of lowering it.](/frameworks/verifier-capital/)

## Frameworks find it, tools evaluate it

Frameworks tell you *where to look* for enterprise value. Once you find a [soft spot](/lexicon/soft-spot/), the [AI Operations Tools](/tools/) tell you what to do about it - diagnose, calibrate, invest, value.

The [Lexicon](/lexicon/) defines the shared vocabulary that makes the whole system teachable.

See also: [AI Operations Tools](/tools/) · [Lexicon](/lexicon/)
