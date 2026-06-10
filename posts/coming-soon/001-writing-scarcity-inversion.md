---
title: What AI Actually Made Scarce
description: 'AI made production cheap and revealed the constraint it was hiding: selection. Green dashboards stay green while quality quietly decays. A 30-minute protocol to find your new scarcity.'
date: '2026-06-03'
scheduled: '2026-07-01'
tags:
- p-and-l-engineering
- coming-soon
- writing
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: markdown
inspiration_url: https://templeton.host/writing/scarcity-inversion/
inspiration_category: writing
source_frontmatter:
  pillar: allocator
  status: published
  published_at: 2026-06-03
  position: Allocator, Operator
  position_note: 'Macro thesis: when AI made labor free, your real balance sheet showed up.'
  revision: 1
  draft_id: 199757137
  staged_at: 2026-05-29 15:18
---

> Source-copy draft imported from [https://templeton.host/writing/scarcity-inversion/](https://templeton.host/writing/scarcity-inversion/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

## Prologue: Labor Was Hiding the Real Constraint

# What AI Actually Made Scarce

![A free, abundant proposer feeds a scarce selector: a dense field of cheap emerald proposals converges on a narrow amber gate; only three pass through and become the light squares that ship. AI made proposing free, so selection became the binding constraint.](/images/posts/scarcity-inversion-hero.svg)

The dashboard was green. The catalog ingestion pipeline I run had just dropped from about \$11 per record in human extraction time to about \$0.90 on a model-driven extractor. Volume went up roughly 12x in a quarter. Escalation rates fell 4x. Approval throughput climbed. Everyone in the meeting nodded.

When I pulled the QA acceptance logs, I felt a specific kind of dread: the numbers were too clean.

Either the model was somehow 50x better than the humans it replaced - which is not a thing - or the verifiers had quietly recalibrated. They had. And the failure was non-obvious because nobody made a decision. No reviewer chose to be lazy. The implicit prior - the probability that any given record in the queue was actually broken - had decayed toward zero, and a human cannot sustain hard vigilance against a near-zero prior. You start pattern-matching "looks normal," approving on glance, and the rare genuine defect rides through inside a population so clean it is invisible.

That is the AI win story everybody celebrates. It is also the verifier-collapse story almost nobody is writing down.

The cheap-production half of the win was real. The other half is the story of what AI just made the load-bearing constraint, what got revealed underneath labor, and why the dashboard that says "green" is going to keep saying "green" while the actual quality of your output decays.

That is the shift this essay tracks: from labor as the binding constraint to selection as the binding constraint.

![Pre-AI, PROPOSE is the bottleneck and SELECT free-rides on it; post-AI, AI makes PROPOSE free and SELECT becomes the binding constraint, while the dashboards still measure the old bottleneck.](/images/posts/scarcity-inversion-invariant.svg)

## The thing labor was hiding

For as long as production was scarce, every other input was getting a free ride on the production bottleneck.

A team that could only ingest 500 SKUs a week didn't have to think very hard about whether the ontology defining "good" was the right ontology. The ontology was almost never under load. The bottleneck was the typing. The shape of the work was: someone manually pulled attributes from a vendor file, someone else spot-checked them, and the pipeline moved at the rate the typing could move.

Verification was free-riding on production because production was the constraint. Selection was free-riding on production because there were never enough candidates to challenge the selector. Taste was free-riding on production because the bottleneck of "make it" prevented "evaluate it" from ever being under serious load.

Hiring, capex, project shortlists, capacity planning, deadlines, all of it implicitly assumed production was scarce. The whole operating posture of the last twenty years was about *making more.*

AI removed the production cap. Volume now flows through every downstream input simultaneously. Whichever of them was actually the constraint gets revealed instantly. And the discernment-flavored inputs - verifiers, ontologies, taste, conviction, attention - degrade non-linearly under load in ways the production-bottleneck regime never tested.

This is not a prediction. It is the same pattern the historical record runs every time a friction collapses. Double-entry bookkeeping made counterparty trust cheap and exposed deal-flow as the new scarce input. Limited liability made risk-bearing cheap and exposed operating skill as the new scarce input. The assembly line made physical execution cheap and exposed design, quality, and management as the new scarce inputs. Containerization made cargo-handling cheap and exposed supply-chain orchestration as the new scarce input. The internet made distribution cheap and exposed attention, trust, and curation as the new scarce inputs.

This same pattern is a formal six-step protocol. I ran it across six transitions spanning roughly 700 years in [Any Sufficiently Advanced Technology: A Taxonomy of Magic](/writing/technology-magic-taxonomy/); this essay takes one of its steps - find the new scarcity - to full depth for the AI transition.

In every case, the friction collapse was the visible event. The complementary scarcity that got revealed underneath was the durable one. Operators who named the complementary scarcity early compounded for decades. Operators who kept optimizing the friction that no longer existed got slowly displaced.

![Friction collapses and the scarcity each one revealed underneath: double-entry bookkeeping to deal flow, limited liability to operating skill, the assembly line to design and quality, containerization to supply-chain orchestration, the internet to attention and curation, and cheap AI cognition to selection.](/images/posts/scarcity-inversion-history.svg)

The interesting move now is that the LLM transition is happening fast enough to *feel* in real time. We can run the inversion protocol on our own operations and act on it before the new scarcity becomes obvious.

## The invariant: free proposer, scarce selector

Across every domain where AI has actually displaced labor, the invariant looks the same:

> Pre-AI, **proposing was expensive** and selecting was free-riding on the fact that very little got proposed without being pre-filtered for plausibility.
>
> Post-AI, **proposing is free** and selecting is now the entire job.

The scarce selector is domain-specific. In a retail catalog ingestion pipeline, the selector is the ontology that defines correctness plus the surprise-gated learning loop that decides when a novel value is a new category versus a data error. In a software organization running LLM-driven code generation, the selector is the deterministic quality gate that turns a stochastic proposer into a converging process. In private-equity deal sourcing, where AI now lets a team screen 10x the deal flow, the selector is the conviction - the prior that picks among ten screened theses which one is actually worth underwriting. In customer support, the selector is the escalation taxonomy that decides which 5% of tickets need a human and which 95% can route. In strategic analysis, where any analysis can be generated on demand, the selector is the question - the prior that picks the one analysis that actually moves the call. In personal life, where any name or product or trip can be generated instantly, the selector is your articulated preference - the true utility function the engine is approximating.

Same shape, different selectors. The selector is the new line item on every operator's balance sheet, and almost nobody has named theirs.

Look at the pattern across six domains:

| Domain | Pre-AI scarcity | Post-AI scarcity | What's allocated now |
|---|---|---|---|
| Retail catalog ingestion | Human extraction labor | The ontology that judges correctness | Attention against surprise (>2-sigma novelty gets a human) |
| PE deal sourcing | Analyst bandwidth | Conviction and proprietary access | Principal judgment about which thesis to chase |
| Software engineering | Dev hours | Quality gate / spec / metric topology | Judgment about "good," encoded as deterministic gates |
| Customer support | Tier-1 capacity | Escalation taxonomy | Graduated autonomy per ticket class |
| Strategic analysis | Analyst hours | Question quality | Framing - the prior that picks the analysis that moves a decision |
| Personal life / household | Planning and research time | Articulated preference | True utility-function elicitation |

The architecture is the table. You should be able to look at your own operations and write your own row. The pre-AI column is what labor used to bottleneck. The post-AI column is what is left holding the constraint once labor stopped doing so. The third column is the allocation move that follows.

## The trap

When production was scarce, the cost of slow production was visible and counted. Throughput dashboards measured it. Cost-per-unit reports counted it. Headcount plans optimized against it. The friction was named, instrumented, and on every report.

The cost of weak selectors was invisible because selectors were never under load. A bad ontology didn't matter much when only 500 SKUs flowed through it a week. A miscalibrated reviewer didn't matter much when the queue gave them time to look hard at every record. A vague spec for "good code" didn't matter much when dev hours rate-limited everything anyway.

When production becomes abundant, the visible cost of slow production disappears. That's the win, and the dashboards correctly show it. What the dashboards don't show is that the cost of weak selectors rises non-linearly under the new load. The ontology that handled 500 SKUs a week is now handling 6,000. The reviewer reading at the old base rate of defects now reads against a near-zero base rate. The vague spec for "good code" is now governing 10x the volume of generated code.

The selector failure is silent in two specific ways.

First, the verifier stops verifying without anyone deciding to stop. There is no decision point. There is a slow drift in attention, a gradual recalibration of the implicit prior, and a quiet acceptance of "looks normal" that operates one record at a time. The team is acting in good faith the entire way down. Nobody can point to the moment it broke.

Second, the dashboard celebrates the production win and gets the verifier collapse for free. Approval rates climb because the AI outputs cleanly. Escalation rates fall because reviewers raise fewer flags. End-to-end yield looks better than it has ever looked. Six months later, the customer side shows up with the actual cost: returns rise, complaints land, NPS dips, but by then the win has been celebrated, the bonus has been paid, and the diagnosis is harder because the production-side metrics still look good.

This is the trap that catches everyone. The production win arrives loud. The selector collapse arrives quiet. The diagnostic loop is broken by the time anyone realizes one of them is fake.

![After AI is deployed, reported throughput jumps and stays green while true output quality silently decays; the widening shaded gap between the two lines is the trap.](/images/posts/scarcity-inversion-trap.svg)

If you do not actively reallocate against the new scarcity, AI does not just shift the bottleneck. It actively *de-rates* your operation while raising your reported throughput. That is the inversion that is doing real work right now in operations across every domain it touches.

## The exercise

Stop reading think pieces about The Future of Work. Run the protocol on your own operations this week. It takes about thirty minutes the first time.

**Step one: inventory what AI just made cheap in your domain.** Be specific. Which production task. What fraction of its old cost. What volume change. "AI made my work easier" doesn't count. "The cost of producing X fell by Y in Z weeks" counts. If you cannot answer this for at least one concrete production task, you haven't actually deployed AI yet; you are still in the demo phase.

**Step two: locate the selector that was complementary to that production.** What was downstream of the cheap-now thing that decided whether the production was good enough to ship? Name it. The selector is almost always one of five things: a person, an ontology, a gate, a preference, or a conviction. If you can't name the selector, you don't know what's about to hold your operation up.

**Step three: audit the selector under the new load.** Has it actually held? Or has it quietly de-rated? The failure mode usually shows up as better-looking dashboards with worse downstream outcomes. If you cannot find the worse downstream outcome yet, the selector failure may not be visible at the customer side because there is lag between when the selector fails and when the bad outputs reach the world. The fact that customer impact has not yet shown up is not evidence that the selector is fine. It is evidence that you have time to fix it before the impact arrives.

![The three-step inversion protocol: inventory what AI made cheap, locate the selector it free-rode on, and audit whether that selector held under the new load. Step three is the one almost nobody runs.](/images/posts/scarcity-inversion-protocol.svg)

The third step is the one almost nobody runs. Most teams stop at step one. They notice the win. They publish the deck. They never go back and check whether the win was actually a win on the customer side, because the production-side metrics tell them it was.

Three steps. Thirty minutes. Some of the most expensive failures you can imagine arrive in the form of dashboards that say everything is fine.

## What's next

Two companions develop this further.

The first is the math of selector collapse. There is a precise mechanism by which verifiers degrade under dilution, and it is not what most teams think it is. It is not a calibration problem. It is not a recalibration-lag problem. It is a resolution-and-prevalence problem with implications for how you sample, how you set thresholds, and what you actually need to fix when the selector starts drifting. That post argues, among other things, that you can be perfectly calibrated and useless.

The second is the personal version. The non-GAAP balance sheet that governs an operator's real allocation - first-read slots with the audience, trust capital with named counterparties, time-horizon-to-compound, taste budget, the depreciating right to make mistakes in public, conviction as a shared resource that cross-account drains between work and writing. Fourteen line items that don't appear on any financial statement and that determine almost all of the meaningful allocation decisions I make. The post is a worksheet. You do the exercise yourself.

Beneath the allocation thesis sits a more general claim: this same inversion runs in every technology transition, and it predicts who wins. [Any Sufficiently Advanced Technology: A Taxonomy of Magic](/writing/technology-magic-taxonomy/) is that protocol - the structural reason some operators compound through a transition while others get displaced, and the questions it forces you to ask about your own business.

The allocation thesis runs through all three pieces. Every operating decision is a capital allocation decision. AI didn't change the discipline. It made it sharper, by removing the input that was hiding most of the real allocation constraints behind a single visible bottleneck.

Find your new scarcity. Allocate against it. The teams that name it first will compound. The teams that keep optimizing the friction that no longer exists will spend the next decade on the wrong side of a transition that is already obvious in retrospect.
