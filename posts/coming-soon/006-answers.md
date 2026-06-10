---
title: I Have This Problem
description: Have a specific AI deployment problem? Find the right framework, tool, or term. Problem-to-solution index for AI operations.
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- answers
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
permalink: /answers/
---

[← Home](/)

# I Have This Problem

Find the right framework, tool, or vocabulary term for your AI deployment challenge. Each answer links to the full concept with worked examples and the math behind it.

[“I keep hearing "knowledge work is manufacturing" - but how do I tell which kind of factory my line actually is?”

The Factory Typology →Framework

archetype = f(input, process, output). Name your line's signature and inherit a mature physical industry's operations playbook.](/frameworks/factory-typology/)[“My team runs every workflow with the same QC. Why does that keep failing on some lines?”

What Factory Are You? →Tool

Six questions classify your line. Most lines are chains with a curvature sign-flip: screen upstream, control downstream. One posture across the whole thing is wrong.](/tools/factory-typology/)[“We keep shipping improvements and then regressing. How do I make sure quality only goes up?”

Quality Ratchet →Lexicon

A CI-enforced floor that only moves up. Each improvement becomes the new minimum.](/lexicon/#quality-ratchet)[“How do I make AI agents improve over time without writing an improvement plan?”

Quality Hillclimb →Framework

Ratcheted quality gates on stochastic output create emergent ascent. The agent doesn't need a plan.](/frameworks/quality-hillclimb/)[“We deployed AI but we're scared to remove the human. How do we safely give it more independence?”

The Promotion Protocol →Framework

A 3-state progression: Disabled, HITL, Autonomous. Promote on statistical evidence, roll back on drift.](/frameworks/promotion-protocol/)[“Nobody agrees what "good" looks like for this task. How do I define quality?”

The Performance Frontier →Framework

Map the distribution of human performance, find the 99th percentile, compute the gradient toward it.](/frameworks/performance-frontier/)[“My AI keeps doing things I don't want. I can't write a complete spec of what I want.”

The Deity Problem →Framework

Three evidence channels: structured elicitation (conjoint), revealed preference (behavioral observation), and direct query (ask when VOI exceeds attention cost).](/frameworks/deity-problem/)[“Should I automate this specific task? How do I decide?”

TaskVector →Tool

Score across 9 dimensions. If any single dimension is a landmine (1), it's a hard no.](/tools/taskvector/)[“Is this task a good candidate for AI? What is the ROI?”

Verification Quadrant + Ablaza Ratio →Tool

T = time\_to\_do / time\_to\_check. High T = AI creates leverage. Low T = you're doing the work twice.](/tools/verification-quadrant/)[“The AI output looks good but I don't know if it's correct. Checking takes as long as doing it.”

Verification Trap →Lexicon

Easy to generate, hard to verify. T approaches 1. You have added a step without saving time.](/lexicon/#verification-trap)[“How do I brainstorm business ideas that actually match real demand?”

The Demand Field →Framework

Fix demand (immutable), vary means (mutable). Demand is a hidden force on your optimization gradient.](/frameworks/demand-field/)[“How do I guarantee this initiative succeeds instead of hoping?”

Designed Convergence →Framework

Design the game so rational agents converge to your outcome. Finite state + Bayesian search + ratchet = structural guarantee.](/frameworks/designed-convergence/)[“What are the actual dollar costs of AI being wrong?”

Dollarized Confusion Matrix →Tool

Replace accuracy with dollars. Optimal threshold: theta\* = C\_FP / (C\_FP + C\_FN).](/tools/dollarized-confusion-matrix/)[“How do I tell if an AI roadmap idea is actually good before committing to it?”

The DoG Test →Tool

A 60-second Claude prompt. Three checks (strength, surprise, utility). Verdict: GOOD DoG, NEEDS TRAINING, or BAD DoG.](/tools/good-dog/)[“The task is in a bad quadrant. What capital investment moves it to a better one?”

Quadrant Shifting →Tool

Five moves: build a verifier, decompose, enrich inputs, constrain outputs, build a rubric.](/tools/quadrant-shifting/)[“I have 20 projects competing for budget. How do I decide which ones to fund?”

Capital Allocation →Framework

Treat each project as an investment instrument with a return distribution. Rank by Sharpe (not NPV), map risk tolerances, handle correlations, construct the efficient frontier.](/frameworks/capital-allocation/)[“I know this project should be killed but I can't get organizational buy-in to stop it. How do I say no?”

Kill Protocol →Framework

Three decision gates: marginal Sharpe (is it additive to the portfolio?), left-tail survivability (can you absorb the downside?), base rate verification (does the team's P(success) match reality?). Portfolio math gives you the language for "no."](/frameworks/kill-protocol/)[“I have a budget and a set of candidate projects. How do I know which combinations are efficient?”

The Operating Efficient Frontier →Framework

Markowitz (1952) applied to operating investments. The non-dominated set of portfolios at each level of risk. By definition, points below the frontier are dominated - same risk, lower return, or same return, higher risk.](/frameworks/efficient-frontier/)[“Two allocators with the same inputs pick different portfolios. How do I know which is right?”

The Risk Tolerance Map →Framework

Both can be right. The map translates firm-level constraints - cash, runway, covenants, narrative - into the preferred point on the frontier. Without it, two rational allocators diverge on identical inputs.](/frameworks/risk-tolerance/)[“We shipped four projects and they all slipped the same week. How do I plan so that doesn't happen again?”

Correlated Execution Risk →Framework

Shared team, stack, review queue, or narrative means shared failure mode. Operating portfolios aren't sums of independent projects. The covariance matrix is the input that makes Stage 3 different from project-by-project NPV.](/frameworks/correlation/)[“Where is value leaking in my business that nobody has named?”

Directed Graph + Soft Spots →Framework

Your chart of accounts is a directed graph. Walk the edges. The soft spots are where value leaks.](/frameworks/directed-graph/)[“I spend all my time in meetings and firefighting. How do I invest in systems?”

Compile Time vs. Runtime →Lexicon

Compile time: building systems with multiplicative ROI. Runtime: executing tasks with single-period returns.](/lexicon/#compile-time)[“Is this AI automation a wasting asset or a compounder?”

Dual Curve + Knowledge Capital →Lexicon

Models depreciate while data appreciates - the net rate determines the investment type. See also: knowledge-capital framework.](/lexicon/#dual-curve)[“What is the NPV of automating this task? Should I build, buy, or hire?”

Automation NPV →Tool

Calculate NPV, IRR, and payback period against hiring, SaaS, or doing nothing. Same math, different asset class.](/tools/automation-npv/)[“How should I think about AI output I can't observe directly? How does the agent learn what I want?”

Structured Elicitation, Revealed Preference, Direct Query, Drift Detector →Lexicon

The four evidence channels from The Deity Problem: structured-elicitation (conjoint), revealed-preference (behavioral observation), direct-query (ask when worth it), and drift-detector (posterior predictive check). See also: oracle-gradient, designers-seat.](/lexicon/#structured-elicitation)[“How do I infer what the operator actually wants without asking? How do I learn from behavior instead of instructions?”

Revealed Preference →Lexicon

Watch what the operator does, not what they say. Revealed preference theory (Afriat, GARP) applied to AI alignment. Cheapest evidence channel because the operator behaves naturally.](/lexicon/#revealed-preference)[“When should the AI ask the operator a question? How do I avoid over-asking or under-asking?”

Direct Query →Lexicon

Ask only when the expected value of the answer exceeds the cost of the operator's attention. An agent that asks too many questions is poorly calibrated, not diligent.](/lexicon/#direct-query)[“How do I detect when the operator's preferences have changed and the model is stale?”

Drift Detector →Lexicon

A posterior predictive check on recent decisions. When the fraction the model predicted incorrectly exceeds a threshold, trigger re-elicitation. Preferences drift - the system must detect it.](/lexicon/#drift-detector)[“What does "operational alpha" mean? How is it different from just doing a good job?”

Operational Alpha →Lexicon

Excess return on enterprise value generated through systematic identification of mispriced edges. The directed graph finds them. The tools evaluate them.](/lexicon/#operational-alpha)[“What is the AI Sweet Spot? When does AI create the most value?”

AI Sweet Spot + Ablaza Ratio →Lexicon

Hard to do, easy to check - T >> 1. The ablaza-ratio measures the gap, and a high ratio means transformative ROI. The proof-layer and gold-standard define what "correct" means.](/lexicon/#ai-sweet-spot)[“What should I build first - the AI system or the verification instrument?”

Proof Layer + Gold Standard →Lexicon

Build the rubric first. The gold-standard IS the verification instrument - without it, you're measuring with a broken ruler. See: soft-spot for finding where to look.](/lexicon/#proof-layer)[“How do I manage the pull of real demand on my product trajectory?”

Demand Gravity →Lexicon

The inescapable pull of real demand on product trajectories. Map it or crash into it.](/lexicon/#demand-gravity)[“Should I be playing the game or designing it? What is the CTO's real job?”

The Designer's Seat →Lexicon

Design the game so self-interested agents produce the outcome you want. Most engineering is game-playing. Mechanism design is game-designing.](/lexicon/#designers-seat)[“The AI deployment is at autonomy-state-machine HITL state. When do I promote to runtime autonomous?”

Promotion Protocol + Autonomy State Machine →Lexicon

Consecutive batches below acceptance threshold. Not one good batch - N consecutive. The construction-spread is the gap between build cost and operational value.](/lexicon/#autonomy-state-machine)[“How do I measure what I should invest in next for my AI operations portfolio?”

Knowledge Capital + Permutations →Framework

Knowledge work either compounds or depreciates. Invest in the appreciating side: verifiers, data, rubrics. Not the depreciating side: models.](/frameworks/knowledge-capital/)[“Why is a verifier worth building when it costs more than the generator it wraps?”

The Capital Value of Verifiers →Framework

A verifier is one of the only capital assets that appreciates through operating use. Every failure caught is encoded; the next run inherits the catch. Most operating assets depreciate; this one ratchets up.](/frameworks/verifier-capital/)

## The Three Layers

[Frameworks](/frameworks/) tell you *where to look* - strategic models for finding enterprise value.

[Tools](/tools/) tell you *how to evaluate* - interactive calculators for specific decisions.

[Lexicon](/lexicon/) gives you *the language* - vocabulary that travels in meetings you are not in.

See also: [Frameworks](/frameworks/) · [Tools](/tools/) · [Lexicon](/lexicon/)
