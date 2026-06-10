---
title: What Factory Are You?
description: Classify a knowledge-work production line into a physical-factory archetype from its input, process, and output signature - then inherit that industry's mature operations playbook. Work in progress, building in public.
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
permalink: /tools/factory-typology/
---

[← AI Operations Tools](/tools/)

# What Factory Are You?

[Stage 1Find](/thesis/#stage-1)

You run some piece of knowledge work over and over - turning out posts, models, decisions, enriched data. Once that line is stable enough to name its inputs, steps, outputs, and defects, you can run it like a factory. The useful question is *which* factory: the physical industry your line most resembles has already solved your quality problem, and you can borrow its playbook where the constraints actually match.

New here? This tool rests on one premise: once AI made *production* cheap, the bottleneck moved to *selection* - judgment and quality control. That is the shift that makes a knowledge-work line behave like a factory at all. If that framing is new, start with [What AI Actually Made Scarce](/writing/scarcity-inversion/), then come back and classify your line.

Answer six questions and you get a *candidate* archetype and the first diagnostics to run - not a final verdict. The match is read off a coarse input / output / value-shape signature (what actually binds you: how cheaply you can test quality, how much waste is in your inputs, how costly a defect is), with one follow-up question where the signature is ambiguous.

When to use this: you have a repeatable knowledge-work line - one stable enough to name its inputs, steps, outputs, and defects - and you want a mature industry's operations playbook to borrow from. Skip it for exploratory research, negotiation, bespoke strategy, or incident response: those are not repeatable lines, the classifier will abstain, and the honest move is to stabilize or decompose the work into a line first.

## Where does the value come from?

The strongest single signal. How is your payoff shaped - by upside breadth, downside control, or both in sequence?

Breadth of attempts

A rare hit pays for many misses. Widening the search helps more than tightening each attempt.

e.g. cold outreach, A/B headline tests, VC dealflow, exploratory prompt search

Downside control

A defect is expensive and fans out. Variance reduction and gates help more than more attempts. (Can be high-volume.)

e.g. payroll runs, the financial close, compliance filings, production deploys

Discovery then production

You search for a winning recipe (breadth), then run it at scale (control). Two factories in series.

e.g. find a winning ad creative, then run it across every market; tune a prompt, then batch-generate

## What does the line actually emit?

Output kind co-varies with archetype; it should not be forced to converge with the others.

A finished artifact

A post, a page, a per-customer deliverable. Consumed once.

e.g. a blog post, a board deck, a signed contract, a rendered report

A function / policy / weights

A recommender, a model, a routing policy. It then runs another line.

e.g. a trained recommender, a routing rule, a pricing model, an agent

A data slate / graph

A knowledge graph, a feed of records, projections of varying grade.

e.g. an enriched CRM, a knowledge graph, a scored lead list

A type / reusable process

A versioned production process or schema. The thing you make is another line.

e.g. a reusable onboarding pipeline, a content-template system, a schema others build on

## What is your raw material?

The front of the line. High-grade input needs no concentration; free low-grade exhaust forces an assay station.

Scarce, expert-grade input

Hand-curated, expensive to acquire, already high-value.

e.g. senior-analyst hours, hand-labeled gold data, partner-level judgment

Mixed-grade, self-generated

You generate your own feedstock at moderate volume (the artisan case).

e.g. your own drafts and notes, mid-tier contractor output, internal docs

Free, abundant, low-grade

Third-party data, logs, scraped exhaust. Near-free per unit; the cost is the join.

e.g. scraped web pages, support tickets, raw event logs

## How much of the input is waste vs. signal?

Signal-to-ore. Extreme variance - a tailings pile with rare seams - forces exhaustive screening plus a cheap pre-filter. Uniform feed needs none.

Mostly signal / uniform

Dependable, uniform input. Little screening or grading needed.

e.g. clean structured records, standardized intake forms

Some waste, some signal

A meaningful fraction is unusable, but not overwhelmingly so.

e.g. inbound leads (some junk, some gold), mixed-quality transcripts

Mostly waste, rare seams

A tailings pile - the value is in finding the rare high-grade seam.

e.g. cold-scraped data, a public tip line, an unfiltered firehose feed

## Is the output a one-off or a reusable recipe?

The mechanism that turns a line into a meta-factory. Distinguish a reusable PLATFORM from a reusable unit OUTPUT - a configurator can be reusable while each unit it emits is a one-off.

A reusable recipe / platform

The recipe or configurator amortizes across many future units, entities, or brands.

e.g. a campaign template you re-run per client, a configurator, a productized service

A bespoke one-off

Each output stands alone; little carries forward to the next.

e.g. a custom board deck for one meeting, a one-time data migration

## Is this high-volume / scaled, or low-volume / bespoke?

Volume and marginal cost are separate (a line can be high-volume yet have real per-unit model/API/review cost). This asks scale; if your per-unit cost is non-trivial, throughput/capacity stay first-order regardless of archetype.

High volume / scaled

Many units. (If copies are near-free, yield binds; if each unit needs a fresh model/API/review pass, capacity also binds.)

e.g. thousands of generated product descriptions, per-user email personalization

Low volume / bespoke

Few units, each significant. Precision is the binding constraint.

e.g. a handful of M&A models a year, a quarterly strategy memo

## The shape of your line

Download JPEGCopy ImageCopy URLEmbed

A neutral schematic for now - it resolves into your line’s curvature once all six are answered. The value-add smile is drawn as a *hypothesis*, not a law - it holds only when the commodity middle can be cheapened without hurting risk-adjusted quality (otherwise the middle is the moat). J just records the order of convex (+) and concave (−) stages; whether it is a meaningful invariant is an open question on the [formalism page](/frameworks/factory-typology/formalism/).

## Classify your line (0 of 6 answered)

No diagnosis yet - the classifier will not commit until all six are answered (it will not treat defaults as your answers). Still to answer: Where does the value come from; What does the line actually emit; What is your raw material; How much of the input is waste vs. signal; Is the output a one-off or a reusable recipe; Is this high-volume / scaled, or low-volume / bespoke. The diagram above is an illustrative example, not your result.

## Known collisions in the current working set

The signature is deliberately coarse, so some archetypes share a six-coordinate projection. When your line lands on one of these, the classifier returns a candidate and the discriminating question rather than a confident label. This list is *not exhaustive* - on a small, internal sample there are likely unlisted collisions; send counterexamples.

Foundry vs single-tenant functionIs the function a shared asset many lines pin, or a single-tenant policy? (consumer count)

Salvage: third-party vs internal exhaustBoth are salvage (a low-value exhaust/waste stream with recoverable rare seams). Third-party vs internal exhaust (logs, tickets, failed generations) changes governance and join cost, not the archetype.

Mass-customization vs uniform commodityDoes each unit carry a late-bound per-unit spec, or are units uniform? (per-unit variety)

Refinery vs batch data jobIs the line a continuous high-volume flow, or a low-volume batch job? (flow mode + volume)

## Classify your own line with an LLM

The six questions above are a compression of a longer elicitation. Paste this *structured elicitation* prompt into a capable model and describe your line in plain language. It is a guided interview, not a deterministic classifier - different models (and borderline lines) can land differently, so it asks the model to report all matched archetypes and its uncertainty rather than forcing one answer.

Copy prompt

```
You are an operations analyst. I will describe a knowledge-work production line.
This is a structured elicitation, not a deterministic classifier - report all matched
archetypes and your uncertainty, and ask for evidence rather than asking me to self-label.

PRECONDITION: first confirm this is a REPEATABLE, stable production line (definable inputs,
transforms, outputs, defects). If it is exploratory, non-repeatable, or environment-shaping
(novel research, negotiation, bespoke strategy, incident response), say the typology does not
apply and stop. NOTE: a repeatable line that produces bespoke one-off UNITS is still fine -
that is the aerospace / job-shop case; the stop condition is non-repeatability of the LINE,
not one-off outputs.

Elicit these six coordinates using behavioral questions (e.g. "does 10x more candidates
help, or does tightening each attempt help?" for curvature; "how many units do you produce
after the recipe is fixed?" for volume). Do NOT ask me to pick a curvature/archetype label.
1. Risk curvature: convex (breadth of attempts pays; rare fat-tailed hit), concave (downside/defect control pays; can be high-volume), or mixed (discovery feeds production).
2. Output kind: artifact | function/policy/weights | data-slate/graph | type/reusable-process.
3. Input grade: ultra-high (scarce expert) | mixed/self-generated | low-abundant (free exhaust).
4. Input variance (signal-to-ore): low (uniform) | mixed | extreme (mostly waste, rare seams).
5. Transferability: reusable-recipe/platform (amortizes) | one-off. (A reusable platform can still emit one-off units.)
6. Volume / scale: scaled-high (many units) vs bespoke-low. (Volume and marginal cost differ - high volume with real per-unit model/API/review cost still binds on capacity.)

Selection rules produce a CANDIDATE, not a verdict. Gates exclude defining-coordinate violations; if none passes, ABSTAIN ("none of these as stated"). Several archetypes then need a second-stage discriminator the six questions do not capture - ask the relevant follow-up to separate the known collision (the output stays a candidate, not a verdict; sometimes more than one follow-up is needed):
- mixed curvature => candidate Vertically Integrated Process Chain. Confirm both halves are load-bearing (else classify the dominant stage). Discovery half is HTS-style only if cheap assayable breadth + fat tail (else a generic convex search); production half by volume+output.
- convex + (mixed/extreme) variance + reusable-recipe + function-ish => HTS.
- convex + low-abundant + extreme variance => Salvage (a low-value exhaust/waste stream with recoverable rare seams; internal exhaust - your own logs, tickets, failed generations - counts too, it just changes governance, not the archetype).
- concave + type-process => Pilot plant. concave + function + scaled => Foundry (candidate - confirm shared-consumer count: many => Foundry, single => single-tenant function deployment). concave + artifact + reusable + scaled => Mass-customization OR Float-glass (confirm per-unit variety: configured => Mass-cust, uniform AND uniform feed => Float-glass, uniform output but heterogeneous feed => neither, re-examine).
- concave + low-abundant + data-slate + scaled => Refinery (candidate - confirm flow mode: continuous => Refinery, batch => batch data job).
- bespoke-low + one-off + concave => Aerospace (candidate - confirm defect consequence: catastrophic => Aerospace doctrine, low => low-stakes bespoke).

Do not commit a first move until any needed follow-up is answered; if unanswered, say "insufficient information - answer [follow-up] first." For the resolved archetype, attach a falsifier and output: archetype, exemplar, what transfers AND what does not, the per-layer QC regime, and the highest-leverage first move tied to observed bottleneck evidence.
```

[Framework →

The Factory Typology

The triple signature, the archetype zoo, the smile curve, and the make-vs-buy boundary - in plain language.](/frameworks/factory-typology/)[Dense →

The Formalism (WIP)

The structural functor, the category error named honestly, and the open obstruction-invariant program.](/frameworks/factory-typology/formalism/)

Changelog9 entries · building in publicshow ↓hide ↑

1. 2026-06-03Legibility + concreteness pass on the six-question diagnostic (Gemini-graded). Larger option-button text, higher-contrast hint and example tiers, more line-height. Every choice now carries a concrete real-world "e.g." line (e.g. "cold outreach, A/B headline tests, VC dealflow" for breadth-of-attempts) so the abstract coordinates are easy to map onto your own line.
2. 2026-06-03Adversary round 9 (gpt-5.5). Fixed the precondition contradiction: the stop condition is non-repeatability of the LINE, not one-off outputs (a repeatable line producing bespoke one-off units is the aerospace / job-shop case, which is in scope). Softened the smile-diagram label ("minimize ownership if it does not hurt end-to-end quality", not "cheap to ~$0").
3. 2026-06-03Adversary round 8 (gpt-5.5). Before all six are answered the diagram is now a NEUTRAL unlabelled schematic - it no longer derives a default-filled classification. Salvage no longer hinges on third-party-vs-internal feed (internal exhaust - logs, tickets, failed generations - is salvage too; the distinction is governance, not archetype). Softened "the one decisive follow-up resolves it" to "separates this known collision; output stays a candidate."
4. 2026-06-03Adversary round 6 (gpt-5.5). Confirmation redirects now check the redirected archetype's own gate - a uniform-output line with heterogeneous feed abstains instead of being mis-labelled float-glass (output-uniformity is not feed-uniformity). Salvage gate now requires extreme variance; aerospace gate drops the input-grade prerequisite so defect-consequence can decide it. Aligned the copyable LLM prompt with the gated + confirm + abstain semantics.
5. 2026-06-03Adversary round 5 (gpt-5.5). Explicit unanswered state: no diagnosis until all six are answered (defaults no longer masquerade as your answers after one click; partial URLs no longer pose as complete). The smile curve in the diagram is labelled a hypothesis (holds only if cheapening the middle does not hurt risk-adjusted quality). Relabelled the volume coordinate so high-volume is not equated with near-zero marginal cost.
6. 2026-06-03Adversary round 4 (gpt-5.5). Progressive confirmation: when a candidate's identity hinges on a coordinate the six questions cannot capture (shared-consumer count, per-unit variety, flow mode, feed source, defect consequence), the classifier no longer commits a primary - it asks the ONE decisive follow-up and resolves on the answer (confirm the candidate, redirect to the paired archetype, or resolve to a non-zoo alternative like single-tenant function / batch data job). Chains require a stage-dominance answer before they are called chains.
7. 2026-06-03Adversary round 3 (gpt-5.5). Replaced additive-only scoring with required gates per archetype: a line that violates an archetype's defining coordinate is excluded, and if nothing is eligible the classifier ABSTAINS ("none of these") instead of forcing a fit. Added an ambiguous-tie state and a "what six questions cannot tell apart" disclosure (the known indistinguishability classes and the follow-up question for each). Canonical cases locked by fixtures (not a claim of full calibration).
8. 2026-06-02Adversary round 2 (gpt-5.5). Result no longer shown as a diagnosis before you answer (labelled example; URL not written until you change an answer). Added a low-confidence state and absolute heuristic scores. Added float-glass, a salvage input-stage in chains, and aerospace as a bespoke production half. Fixed the HTS QC claim and softened universals to candidates.
9. 2026-06-02First public draft. Six-question diagnostic over the (input, process, output) signature; classifier wired to the same source-of-truth used by the strategy doc and the prompt set.

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

A diagnosis of which operations playbook your capital should be buying. The archetype fixes the QC regime, the make-vs-buy boundary, and where margin accrues - so it fixes where the next dollar goes.](/positions/allocator/)[Operator

A placement test for your whole line, not one task. Name your input, process, and output signature and you inherit a mature physical industry's runbook instead of reinventing it. Find the sign-flip and you know where your hardest gate belongs.](/positions/operator/)[Builder

The architecture decision before the architecture. Convex discovery stages want cheap-screen-then-confirm; concave production stages want strict gates and SPC. Build them as separate subsystems with a buffer at the joint.](/positions/builder/)[Scientist

A classifier archetype = f(σ) over a triple signature, falsifiable by a bounded-zoo compression claim: the next independent line should decompose into the same finite atom set, or the typology was overfit.](/positions/scientist/)

## See also

[Framework

The Factory Typology →](/frameworks/factory-typology/)[Tool

The Verification Quadrant →](/tools/verification-quadrant/)[Tool

The Dollarized Confusion Matrix →](/tools/dollarized-confusion-matrix/)

See also: [Verification Quadrant](/tools/verification-quadrant/) · [Knowledge Work as Capital](/frameworks/knowledge-capital/) · [AI Operations Tools](/tools/)
