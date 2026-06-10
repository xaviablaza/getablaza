---
title: The Promotion Protocol
description: 'A 3-state progression for safely giving AI more independence. Promote on demonstrated performance, roll back on drift. Formally: Autonomy State Machine.'
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
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/frameworks/promotion-protocol/
inspiration_category: frameworks
---

> Source-copy draft imported from [https://templeton.host/frameworks/promotion-protocol/](https://templeton.host/frameworks/promotion-protocol/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← Frameworks](/frameworks/)

# The Promotion Protocol

[Stage 4Execute](/thesis/#stage-4)

Formally: [Autonomy State Machine](/lexicon/autonomy-state-machine/)

AI earns autonomy through demonstrated performance, just like an employee. You do not deploy it or not deploy it. You promote it through a 3-state progression with statistical graduation criteria at each step - and you roll it back when performance degrades.

Disabled - AI is off; humans do the task manuallyDisabledHuman-in-the-loop - AI drafts, human reviews every outputHITLAutonomous - AI runs unattended with rollback triggersAutonomoussmoke tests passerror < 2%for N consecutive batcheserror > 5% or driftcritical failure2% promote5% rollbackhysteresis gap

Download PNGCopy ImageCopy SVGCopy URLEmbed

Click a state to highlight.

## The Problem

Binary thinking about AI - “it works” vs. “it does not work” - misses the entire middle ground where AI assists but does not decide. Most teams are stuck at one extreme: either they refuse to deploy because they cannot guarantee perfection, or they deploy fully autonomous and pray.

The Promotion Protocol makes the middle ground operational.

## The Three States

Disabled→HITL→Autonomous

State 1: Disabled

AI output is blocked from production entirely. Used for new deployments, post-incident recovery, or when error rates exceed the safety threshold. The system is off.

**Exit criteria:** system passes smoke tests and human review of a sample batch confirms baseline competence.

State 2: Human-in-the-Loop (HITL)

AI produces output. A human verifies every item before it reaches production. The human is the quality gate. This is where most AI deployments should live initially - and where many should stay permanently.

**Promotion criteria:** error rate below acceptance threshold for N consecutive samples. Not one good batch - N consecutive good batches.

State 3: Autonomous

AI output goes directly to production. Humans spot-check only. This state is earned, not assumed - and it's revocable.

**Rollback triggers:** error rate exceeds rollback threshold, distribution shift detected, or [drift detector](/lexicon/drift-detector/) fires. Rollback goes to HITL, not Disabled (unless critical).

## Promotion Criteria

Promotion is earned through statistical evidence, not vibes. The criteria are explicit and measurable:

# Promotion: HITL → Autonomous

error\_rate < acceptance\_threshold

for consecutive\_batches >= graduation\_window

across sample\_size >= graduation\_sample\_size

# Example: <2% error for 500 consecutive items

# across 10 consecutive daily batches

The key word is **consecutive**. One good batch is noise. Ten consecutive good batches is signal. The graduation window prevents promotion on a lucky streak.

## Rollback Triggers

Error spikeError rate exceeds the rollback threshold. Note: the rollback threshold should be higher than the promotion threshold (hysteresis) to prevent oscillation.

Distribution shiftThe input distribution has changed. The model was trained on one world and is operating in another. Even if error rates look fine on old metrics, the underlying data has moved.

DriftThe [drift detector](/lexicon/#drift-detector) fires - operator preferences have shifted and the model is optimizing for the wrong objective.

## Hysteresis

The promotion threshold and the rollback threshold must be different. If they are the same, the system oscillates: promote at 2% error, roll back at 2% error, promote again, roll back again.

# Hysteresis gap

promotion\_threshold = 2% error

rollback\_threshold  = 5% error

# The AI must be excellent to earn autonomy (2%)

# but is only demoted when it is clearly degrading (5%)

# The gap prevents oscillation.

## The Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| acceptance\_threshold | Max error rate for promotion | 2% |
| graduation\_window | Consecutive batches required | 10 batches |
| graduation\_sample\_size | Total items in window | 500 items |
| rollback\_threshold | Error rate triggering demotion | 5% |
| drift\_threshold | Distribution shift sensitivity | KL > 0.1 |

## Worked Example: Invoice Processing

Illustrative scenario. Numbers are constructed to show the protocol, not drawn from a specific deployment.

Week 1: Disabled → HITL

New deployment. Smoke test on 50 sample invoices passes. System promoted to HITL. Every extraction is reviewed by an operator before posting to the ERP.

Weeks 2-5: HITL (accumulating evidence)

500 invoices processed. Error rate: 1.4% (below 2% threshold). Ten consecutive daily batches all below threshold. Graduation criteria met.

Week 6: Promoted to Autonomous

Extractions go directly to ERP. Operator reviews a 10% sample daily. Error rate holds at 1.2%.

Month 3: Rollback to HITL

New vendor with a non-standard invoice format. Distribution shift detected. Error rate spikes to 6.2%. System automatically rolled back to HITL. Operator verifies all output from the new vendor while the model is retrained.

Month 4: Re-promoted

Model retrained on new format. Error rate back to 1.1%. Ten consecutive batches pass. Re-promoted to Autonomous.

## Why “Promote” Not “Deploy”

The metaphor matters. “Deploy” is binary - the system is deployed or it is not. “Promote” implies earned trust, demonstrated competence, and the possibility of demotion.

CTOs present this to boards. Board members understand promotions. “We promoted the AI from supervised to autonomous in the prior review cycle quarter, then rolled it back when drift fired” is a sentence that typically parses for most attendees in the room. “We adjusted the autonomy state machine transition parameters” is not.

## Connection to Other Frameworks

[Quality Hillclimb](/frameworks/quality-hillclimb/) - the HITL review is a quality gate. The graduation criteria are the ratchet mechanism.

[Dollarized Confusion Matrix](/tools/dollarized-confusion-matrix/) - error costs determine the acceptance and rollback thresholds. The cost of a false positive vs. false negative sets the promotion criteria.

[Designed Convergence](/frameworks/designed-convergence/) - the Promotion Protocol is mechanism design for AI autonomy. The incentive structure ensures the system converges toward the right autonomy level.

## When the promotion protocol fails

The protocol generates a *falsifiable prediction*: an agent that has earned promotion at autonomy level *k* will produce fewer material errors at level *k+1* than an agent promoted on tenure or gut feel. If both promotion paths produce the same error rate, the evidence criteria are not load-bearing and the protocol is wrong for this system.

The framework **does not apply** when:

- -**The task distribution is non-stationary.** If the operating environment drifts faster than evidence accumulates, past performance does not predict future autonomy readiness. Pair the protocol with a drift monitor or do not trust the promotion.
- -**Evidence can be gamed.** If the agent can selectively surface its wins and hide its losses (or if the judge is the same entity being evaluated), the signal is adversarial. Require an independent verifier before promotion decisions.
- -**Downside is unbounded.** The protocol assumes errors at level *k+1* are survivable long enough to detect and demote. For catastrophic, irreversible actions (legal, safety, financial), staged autonomy is not enough - use deterministic guardrails instead.
- -**Verification is more expensive than the task.** If checking the agent's work costs more than doing the work, promotion economics collapse. Solve the verification-difficulty problem before staging autonomy.

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

Graduated delegation. Trust is earned through evidence, not vibes. Each state change is a change in the cost of operating the instrument.](/positions/allocator/)[Operator

Staged rollout for agents. You don't turn autonomy on for everyone on day one; you let it prove itself on a slice, then widen the aperture.](/positions/operator/)[Builder

A feature-flag progression with statistical gates instead of hand-wavy confidence. Promote on demonstrated performance, roll back on drift.](/positions/builder/)[Scientist

A finite-state controller with promotion and demotion transitions driven by sequential hypothesis testing. Hysteresis prevents oscillation. Drift detection triggers re-elicitation.](/positions/scientist/)

See also: [Autonomy State Machine](/lexicon/#autonomy-state-machine) · [Dollarized Confusion Matrix](/tools/dollarized-confusion-matrix/) · [TaskVector](/tools/taskvector/)
