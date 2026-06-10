---
title: Backdoor Roth
description: 'Standard backdoor: nondeductible Traditional IRA contribution then convert. Mega backdoor: after-tax 401k contributions then in-plan Roth conversion. Pro-rata rule.'
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- money
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
permalink: /money/backdoor-roth/
---

[←Back to Personal Finance](/money/)

[inventory](/money/inventory/)[graph](/money/graph/)

Personal Finance

# Backdoor Roth

Tax StrategyDifficulty: ★★★★☆

Standard backdoor: nondeductible Traditional IRA contribution then convert. Mega backdoor: after-tax 401k contributions then in-plan Roth conversion. Pro-rata rule.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Prerequisites (2)

[Traditional vs Roth IRAlvl 3](/money/traditional-vs-roth-ira/)[Max Your 401klvl 3](/money/401k-beyond-match/)

High earners often discover they cannot contribute directly to a Roth IRA, yet a set of tax-code workarounds can still move money into tax-free growth.

TL;DR:

A Backdoor Roth uses a nondeductible Traditional IRA then a conversion to Roth, while a Mega Backdoor uses after-tax 401k contributions then an in-plan or distribution Roth conversion; understanding the pro-rata rule reveals the immediate tax cost and when each path is attractive.

## The Problem - What Goes Wrong Without This Knowledge

Many savers with $150,000 - $500,000 in annual income face a concrete barrier. The IRS phases out direct Roth IRA contributions for many filers in recent years, which blocks direct Roth contributions above roughly $150,000 - $220,000 of modified adjusted gross income depending on filing status and year. The practical result: the tax-advantaged vehicle known as a **Roth IRA** becomes inaccessible for $7,000 of annual contributions per person in 2024 without a workaround. That loss matters because a Roth offers tax-free qualified withdrawals and no required minimum distributions in retirement. People often react by simply increasing taxable brokerage investing, which yields taxable dividends and capital gains and creates future tax drag roughly 0.5% - 1.5% per year in realistic scenarios. A second failure mode appears when someone tries the simple workaround incorrectly. Contribute $7,000 to a nondeductible Traditional IRA, then convert to Roth, and assume the conversion has zero tax. That assumption breaks if the taxpayer has any pre-tax IRA balances. The **Pro-rata rule** causes some or all of the conversion to be taxable. Imagine an investor with $100,000 in pre-tax IRAs and a new $7,000 nondeductible contribution. Converting $7,000 to Roth will make approximately $6,543 taxable immediately under pro-rata math, not $0. That creates a surprise tax bill equal to roughly $1,500 - $1,800 at marginal rates of 22% - 28%. A third failure arises when employers do not permit after-tax 401k contributions or in-service conversions. Many plans lack either feature. That blocks the **Mega Backdoor Roth** route entirely. IF an investor ignores plan rules AND assumes any after-tax 401k is convertible, THEN they may expect tax-free Roth funding that does not happen BECAUSE plan paperwork often segregates after-tax accounts but forbids conversions or distributions. This section emphasizes the real-dollar stakes. Missing $7,000 - $66,000 of Roth funding per year can change lifetime tax exposure by tens of thousands of dollars under normal growth assumptions of 5% - 7% real returns over 20 - 30 years. The right knowledge reduces surprise taxes and preserves $1,000s in tax savings over decades.

## How It Actually Works - Mechanics, Formulas, and Rules

**Backdoor Roth** mechanics are straightforward in isolation. Step one: make a nondeductible Traditional IRA contribution up to $7,000 in 2024 per person. Step two: file Form 8606 to record basis. Step three: convert the account to a Roth IRA. IF the taxpayer has zero pre-tax IRA balances at conversion time, THEN the converted amount is effectively tax-free BECAUSE the basis equals the conversion amount. The taxable portion under general circumstances follows the **Pro-rata rule**. The formula is taxable\_amount = conversion\_amount  *(pre-tax\_balance / total\_IRA\_balance) where total\_IRA\_balance = pre-tax\_balance + after-tax\_basis. Example math: with $100,000 pre-tax and $7,000 after-tax basis, taxable fraction = 100,000 / 107,000 = 0.9346. So converting $7,000 yields taxable\_amount = $7,000*  0.9346 = $6,542. That becomes ordinary income taxed at the marginal rate, for example 24% leading to tax ~$1,570. The key administrative point: Form 8606 must be filed for every year there is a nondeductible IRA contribution. Failing to file yields IRS penalties and messy basis tracking. The **Mega Backdoor Roth** uses employer plan features rather than IRAs. Two conditions are required: the plan must allow after-tax contributions beyond the standard $23,500 elective deferral limit, and it must allow either an in-plan Roth conversion or in-service distribution of after-tax amounts. The combined defined contribution limit across employee deferrals, employer match, and after-tax contributions has been $66,000 - $73,500 in recent years depending on age and year. Practically, IF a plan allows $30,000 of after-tax contributions and immediately permits in-plan Roth conversions, THEN most or all of that $30,000 can move into Roth in the same calendar year BECAUSE the conversion treats the after-tax basis as non-taxable and only taxes any earnings between contribution and conversion. The formula for Mega Backdoor taxable portion is taxable\_on\_conversion = earnings\_since\_contribution which is usually small if conversion is prompt. If the plan instead requires distribution and the distribution contains pre-tax and after-tax components, pro-rata-like rules at the 401k level may apply unless the plan segregates subaccounts. Contrast with IRAs - pro-rata blends all IRAs from the same owner across institutions. Finally note transaction timing matters. Converting immediately reduces taxable earnings to near zero. Delays of months can generate earnings of 0.1% - 5% depending on investments, producing small but measurable taxes on conversion.

## The Decision Framework - IF/THEN/BECAUSE Rules for Action

Start by checking two numerics: (A) total pre-tax IRA balance across Traditional IRAs and SEP/SIMPLE IRAs, call it I;(B)plancapabilitytoacceptafter−taxcontributionsandpermitin−planRothconversions.Decisionnode1−StandardBackdoor:IFI; (B) plan capability to accept after-tax contributions and permit in-plan Roth conversions. Decision node 1 - Standard Backdoor: IF I;(B)plancapabilitytoacceptafter−taxcontributionsandpermitin−planRothconversions.Decisionnode1−StandardBackdoor:IFI = $0 AND taxable income is currently not expected to fall below current marginal rate by more than 3% - 6% in retirement, THEN performing a standard backdoor may make sense BECAUSE immediate conversion avoids taxable pro-rata leakage and locks in tax-free growth. Numeric example: with $I = $0 and conversion amount $7,000, taxable\_amount = $0 and present-value savings equal roughly $7,000  *(1 + r)^{n} times saved tax on withdrawals. Decision node 2 - Pro-rata exposure: IF $I > $0, THEN calculate taxable\_fraction = $I / (I + basis) and taxable\_amount = conversion\_amount*  taxable\_fraction BECAUSE the IRS treats all IRAs as one for basis allocation. A numeric threshold helps: if taxable\_fraction > 0.80, then roughly 80% of any attempted $7,000 backdoor becomes taxable; at a 24% marginal rate this implies $7,000  *0.80*  0.24 ≈ $1,344 immediate tax, which may exceed the expected lifetime tax savings from Roth status. Decision node 3 - Mega Backdoor feasibility: IF your employer plan allows after-tax contributions up to the plan aggregated limit of $66,000 - $73,500 and permits in-service Roth conversions, THEN consider allocating additional dollars into after-tax 401k up to that limit BECAUSE that route can move $10,000 - $60,000 per year into Roth without IRA pro-rata problems and with minimal conversion tax if done promptly. Decision node 4 - Tax-rate arbitrage: IF current marginal tax rate is much lower than expected retirement marginal rate by a margin of >4% - 8%, THEN Roth conversions become more attractive BECAUSE you pay tax now at a lower rate and avoid higher future taxes. Conversely, IF current marginal rate is higher than expected future retirement rate, THEN favor pre-tax contributions or delay large conversions.

## Edge Cases and Limitations - Where This Framework Breaks Down

This framework omits at least four important real-world constraints. First limitation - state tax and IRMAA interactions. Large conversions increase adjusted gross income by $5,000 - $500,000 and can push a filer into Medicare IRMAA surcharges or higher state income tax brackets, potentially raising recurring Medicare premiums by $50 - $400 per month or state taxes by 2% - 6% on incremental income. IF a conversion raises AGI above an IRMAA threshold, THEN the indirect cost can exceed the tax saved BECAUSE premiums are recalculated on modified adjusted gross income. Second limitation - legislative risk. The rules that permit Backdoor Roth behavior have been subject to proposals to restrict them; a 3-5 year policy horizon is uncertain. IF Congress changes the law within that window, THEN conversions already performed generally remain valid but future opportunities may close BECAUSE tax law is prospective and retroactive changes are rare but possible on administrative details. Third limitation - employer plan variability. Many 401k plans either do not accept after-tax contributions or do not permit in-plan Roth conversions. IF the plan lacks both, THEN the Mega Backdoor route is unavailable BECAUSE neither after-tax corridors nor distributions provide the mechanism to isolate basis from pre-tax dollars. Fourth limitation - account aggregation at rollover time. Rolling IRAs into a current employer plan can eliminate pro-rata problems, but many plans reject roll-ins or limit roll-in amounts. IF a taxpayer can roll $100,000 of pre-tax IRA into an employer 401k that accepts roll-ins, THEN pro-rata exposure on a $7,000 backdoor can drop to near zero BECAUSE the pre-tax amount moves out of the IRA aggregation pool. This approach depends on plan rules and again requires numeric checking. Finally note behavioral and timing risk: market swings of 10% - 30% between contribution and conversion materially change tax consequences if conversion is delayed. This framework ignores short-term market variance and assumes prompt conversions or protections against tax surprises.

## Worked Examples (3)

### Simple Backdoor Roth with No Existing IRAs

Single filer contributes $7,000 nondeductible Traditional IRA in 2024, has $0 pre-tax IRA balances, 24% marginal tax rate.

1. Step 1: Contribute $7,000 nondeductible Traditional IRA. Basis = $7,000.
2. Step 2: Immediately convert the $7,000 to a Roth IRA. Total IRA balance at conversion = $7,000; pre-tax balance = $0.
3. Step 3: Apply pro-rata formula taxable\_amount = conversion\_amount  *(pre-tax\_balance / total\_IRA\_balance) = $7,000*  (0 / 7,000) = $0.
4. Step 4: File Form 8606 for the tax year to document the nondeductible contribution and conversion.
5. Step 5: Result - no immediate tax; $7,000 grows tax-free. If invested and grows at 6% real for 25 years, future value ≈ $7,000\*(1.06)^{25} ≈ $30,000 tax-free.

**Insight:** IF there are truly zero pre-tax IRA balances AND conversions occur promptly, THEN the backdoor yields effectively tax-free Roth funding of $7,000 per year BECAUSE the basis equals the converted amount and pro-rata produces zero taxable portion.

### Backdoor Roth with Existing Pre-tax IRA - Pro Rata Hit

Married filing jointly taxpayer has $100,000 pre-tax IRA balance, contributes $7,000 nondeductible Traditional IRA, then converts $7,000 to Roth. Marginal tax rate 24%.

1. Step 1: Total IRA balances at conversion = pre-tax $100,000 + after-tax basis $7,000 = $107,000.
2. Step 2: Taxable fraction = pre-tax\_balance / total\_balance = 100,000 / 107,000 ≈ 0.9346.
3. Step 3: Taxable\_amount = conversion\_amount  *taxable\_fraction = $7,000*  0.9346 ≈ $6,542.
4. Step 4: Immediate tax due on conversion = taxable\_amount  *marginal\_rate ≈ $6,542*  0.24 ≈ $1,570.
5. Step 5: File Form 8606 to record basis. Net after-tax Roth contribution effectively equals $7,000 - $1,570 ≈ $5,430 in present-day dollars.

**Insight:** IF pre-tax IRA balances dominate basis, THEN most of a $7,000 attempted backdoor becomes taxable immediately BECAUSE the IRS allocates conversions proportionally across all IRA dollars using the pro-rata rule.

### Mega Backdoor Roth via After-tax 401k and In-plan Conversion

Employee age 40 with $250,000 salary contributes $23,500 pre-tax 401k and $30,000 after-tax into the 401k plan in the same year. Plan permits immediate in-plan Roth conversion of after-tax dollars. Earnings on after-tax bucket before conversion = $500. Tax rate on earnings 24%.

1. Step 1: Make $30,000 after-tax contributions into the 401k after reaching $23,500 elective deferral limit.
2. Step 2: Immediately convert the $30,000 after-tax account to the Roth 401k or Roth IRA via in-plan conversion. Basis = $30,000; earnings = $500.
3. Step 3: Taxable portion = earnings = $500. Tax due = $500 \* 0.24 = $120.
4. Step 4: Result - $30,000 moved into Roth with only $120 tax cost; the $30,000 will grow tax-free thereafter.

**Insight:** IF the employer plan supports after-tax contributions AND allows prompt conversions, THEN moving large sums like $20,000 - $60,000 per year into Roth becomes feasible with minimal immediate tax BECAUSE only earnings between contribution and conversion are taxable.

## Key Takeaways

- ✓

  The **Backdoor Roth** uses a nondeductible Traditional IRA up to $7,000 per person per year then converts to Roth; success requires Form 8606 and ideally zero pre-tax IRA balances.
- ✓

  The **Pro-rata rule** allocates conversions across all IRAs: taxable\_fraction = pre-tax\_balance / total\_IRA\_balance, so existing pre-tax IRAs can make conversions mostly taxable.
- ✓

  The **Mega Backdoor Roth** can move $10,000 - $60,000 per year into Roth if the 401k plan permits after-tax contributions and immediate in-plan Roth conversions; only earnings are taxable if conversion is prompt.
- ✓

  IF pre-tax IRA balances > 0 AND plan roll-in to 401k is feasible, THEN rolling pre-tax IRAs into an employer 401k may eliminate pro-rata exposure BECAUSE the roll-in moves pre-tax dollars out of IRA aggregation.
- ✓

  Consider indirect costs: large conversions can increase MAGI and possibly raise Medicare IRMAA or state tax bills by $50 - $400 per month or 2% - 6% on marginal state tax, so model those effects numerically.

## Common Mistakes

- ✗

  Assuming a backdoor conversion is tax-free when any pre-tax Traditional IRA exists. Why wrong: the **Pro-rata rule** forces proportional taxation; even a $7,000 conversion can be >80% taxable if pre-tax balances dominate.
- ✗

  Not filing Form 8606 after a nondeductible contribution. Why wrong: absence of Form 8606 obscures basis, creating IRS penalties and effectively taxes that basis on future distributions.
- ✗

  Expecting every 401k plan to support Mega Backdoor mechanics. Why wrong: many plans lack after-tax lanes or forbid in-service conversions; assuming availability can block expected Roth funding of $10,000 - $60,000 per year.
- ✗

  Delaying conversion without modeling market movement. Why wrong: if account value rises 10% between contribution and conversion, taxable earnings increase and so does the immediate tax bill; prompt conversion limits this risk.

## Practice

easy

Easy: Single filer with $0 pre-tax IRA balance makes a $7,000 nondeductible Traditional IRA contribution and immediately converts it to Roth. Marginal tax rate 22%. What is the taxable amount and immediate tax owed?

**Hint:** Use pro-rata formula with pre-tax\_balance = 0.

Show solution

Taxable\_amount = $7,000 \* (0 / 7,000) = $0. Immediate tax owed = $0.

medium

Medium: Taxpayer has $50,000 pre-tax IRA balance and contributes $7,000 nondeductible IRA, then converts $7,000 to Roth. Marginal tax rate 24%. Calculate the taxable portion and the tax due.

**Hint:** Compute total IRA = 50,000 + 7,000 then taxable\_fraction = 50,000 / total.

Show solution

Total\_IRA = $57,000. Taxable\_fraction = 50,000 / 57,000 ≈ 0.8772. Taxable\_amount ≈ $7,000  *0.8772 ≈ $6,140. Tax\_due ≈ $6,140*  0.24 ≈ $1,474.

hard

Hard: Employee maxes pre-tax 401k at $23,500, has employer match of $6,500, and wants to place an additional $25,000 after-tax into the 401k this year. The plan allows in-plan Roth conversion the same day. Earnings on after-tax bucket before conversion = $1,200. What is the taxable amount on conversion and the tax due at 32%? Also compute how much Roth principal gets preserved net of tax.

**Hint:** Only earnings are taxable if after-tax basis is converted promptly. Roth principal equals after-tax contribution amount since basis is not taxed.

Show solution

Taxable\_amount = earnings = $1,200. Tax\_due = $1,200 \* 0.32 = $384. Roth principal preserved = $25,000 (the $25,000 basis is not taxed). Net immediate cost = $384; converted Roth principal = $25,000.

## Connections

Prerequisites referenced: Traditional vs Roth IRA (/money/123) where contribution limits ($7,000/yr) and deductibility were covered, and Max Your 401k (/money/456) which discussed elective deferral $23,500 and employer match mechanics. Mastery of this Backdoor Roth lesson unlocks downstream topics: Tax-efficient retirement withdrawals and sequencing (/money/789) because Roth buckets change withdrawal order and RMD planning, and Medicare and benefit phase-in planning (/money/321) because large conversions can affect IRMAA and means-tested benefits. Specific follow-ups that require this lesson include converting pre-tax buckets into employer plans to avoid pro-rata exposure, and modeling lifetime tax trade-offs for Roth versus pre-tax contributions.

**Disclaimer:** This content is for educational and informational purposes only and does not constitute financial, investment, tax, or legal advice. It is not a recommendation to buy, sell, or hold any security or financial product. You should consult a qualified financial advisor, tax professional, or attorney before making financial decisions. Past performance is not indicative of future results. The author is not a registered investment advisor, broker-dealer, or financial planner.

[← back to tree](/money/)[browse all →](/money/inventory/)
