---
title: TaskVector
description: Score any task across 9 dimensions to determine if it should be automated. One landmine dimension is a hard no.
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
permalink: /tools/taskvector/
---

[← AI Operations Tools](/tools/)

# TaskVector

[Stage 2Characterize](/thesis/#stage-2)

Status: field-tested at scale across PE portfolio companies. Formal validation pending.

Before automating a task, score it across 9 dimensions. Each dimension measures a structural property that determines whether automation is viable. If any single dimension scores 1, it is a **landmine** - a hard no regardless of the composite score.

Start with a scenario

Invoice processing

Strong automation candidate

Strategic analysis

Landmine on verifiability

Hiring decisions

Landmine on bias risk

Code review drafts

Strong HITL candidate

Customer support drafts

Strong candidate with HITL

Download JPEGCopy ImageCopy URLEmbed

Drag across a row to score that dimension (far left = landmine, far right = strong).

0/9 scored

Score dimensions manually▾

D1Determinism

How predictable is the correct output given the input?

12345

Chaotic, judgment-heavy, creativePerfectly deterministic, rule-based

D2Data Completeness

Does the system have access to everything it needs?

12345

Requires tribal knowledge, undocumented contextAll inputs available, fully documented

D3Frequency

How often does this task occur?

12345

Rare, ad-hoc, one-offHigh volume, continuous, daily

D4Verifiability

How easy is it to check whether the output is correct?

12345

Impossible to verify without redoing the workTrivially verifiable - pass/fail, compiles-or-not

D5Reversibility

If the AI gets it wrong, how bad is the damage?

12345

Irreversible - sent email, deleted data, harmed patientTrivially reversible - draft, suggestion, undo

D6User Acceptability

Will the people affected accept AI doing this?

12345

Users will revolt - emotional, cultural, political weightUsers prefer automation - faster, less tedious

D7Bias Risk

Could automation introduce or amplify systematic bias?

12345

High bias potential - hiring, lending, content moderationNo bias concern - data formatting, calculations

D8Context Dependency

How much surrounding context is needed?

12345

Deep context required - "you had to be there"Context-free - input fully determines output

D9Consequence Severity

What is the worst-case outcome of an error?

12345

Catastrophic - medical, legal, safety, financial ruinTrivial - wrong playlist, bad suggestion, cosmetic

## The Landmine Rule

A task with 5s across the board but a 1 on Consequence Severity - say, “AI decides whether to administer medication” - is not automatable. Period. The composite score is irrelevant when a single dimension represents a structural blocker.

The landmine rule exists because automation failures are not normally distributed. They are fat-tailed. The expected cost of a worst-case error on a landmine dimension dominates all other considerations.

## What Comes Next

TaskVector tells you *whether* to automate. The rest of the toolkit tells you *how*:

[Verification Quadrant](/tools/verification-quadrant/) - plot the task by calculation vs. verification difficulty. Calculate the Ablaza Ratio.

[Dollarized Confusion Matrix](/tools/dollarized-confusion-matrix/) - price the error costs. Compute the optimal threshold.

[The Promotion Protocol](/frameworks/promotion-protocol/) - deploy in HITL, gather evidence, promote to autonomous on statistical proof.

## When to Use This

### Use when

- +Evaluating one specific task for AI deployment, not an entire function
- +You have real examples to score against, not vibes
- +Multiple stakeholders need a shared scoring frame to align
- +You want to surface landmine dimensions before deploying, not after

### Skip when

- -The task is obviously too immature (no data, no users, no rubric)
- -You already have deployment experience with this exact task class
- -Budget is the primary binding constraint - go straight to Automation NPV
- -The scoring itself would take longer than running a small pilot

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

Multi-factor scoring for operating instruments. Analogous to factor models in equities: decompose the task into orthogonal-ish dimensions, score each, rank by composite.](/positions/allocator/)[Operator

A screener for the next hundred tasks on the backlog. Run the vector, sort, work top-down. Keeps the team from optimizing for the loudest project instead of the most automatable.](/positions/operator/)[Builder

A checklist with teeth. Nine questions that usually catch the "sounds automatable, isn't" failure mode before it eats a quarter.](/positions/builder/)[Scientist

A feature vector in R^9 embedding the task. Similarity in this space predicts automation viability. With enough labeled history, a supervised classifier outperforms hand-scoring.](/positions/scientist/)

## See also

[Position

Allocator →

Which bets to make. Capital allocation, M&A due diligence, portfolio construction.](/positions/allocator/)[Position

Operator →

How to execute at scale. Multi-brand portfolio, turnarounds, P&L ownership.](/positions/operator/)[Position

Builder →

Builds it, ships it, owns it. Solo full-stack, DevOps, production systems.](/positions/builder/)[Position

Scientist →

Proves it, models it, publishes it. Mathematical modeling, Bayesian frameworks.](/positions/scientist/)[Answer

Should I automate this specific task? How do I decide? →

TaskVector](/tools/taskvector/)

See also: [AI Operations Tools](/tools/) · [Promotion Protocol](/frameworks/promotion-protocol/) · [Lexicon](/lexicon/)
