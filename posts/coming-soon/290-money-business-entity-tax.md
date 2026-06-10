---
title: Business Entity Tax
description: LLC, S-Corp, C-Corp, sole proprietorship. Pass-through deduction (QBI). S-Corp salary vs distribution split. When and why to structure business income.
date: '2026-07-01'
scheduled: '2027-04-16'
tags:
- p-and-l-engineering
- coming-soon
- money
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/money/business-entity-tax/
inspiration_category: money
---

> Source-copy draft imported from [https://templeton.host/money/business-entity-tax/](https://templeton.host/money/business-entity-tax/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Personal Finance](/money/)

[inventory](/money/inventory/)[graph](/money/graph/)

Personal Finance

# Business Entity Tax

Tax StrategyDifficulty: ★★★★★

LLC, S-Corp, C-Corp, sole proprietorship. Pass-through deduction (QBI). S-Corp salary vs distribution split. When and why to structure business income.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Prerequisites (2)

[Tax Bracketslvl 2](/money/tax-brackets/)[Capital Gainslvl 3](/money/capital-gains-planning/)

## Referenced by Business (6)

Where this personal-finance concept shows up inside the operating-finance graph.

[Sole ProprietorBusiness

Sole proprietorship is the simplest business entity - no corporate veil, all income and liabilities pass through to the individual. Understanding why the owner personally owes the $50K in taxes (no entity shield) is the core of business entity selection.](/business/sole-proprietor/)[binding agreementsBusiness

Forming an LLC or partnership is literally executing a binding agreement (operating agreement) among owners to pool capital and labor, then reallocate the resulting payoffs (profits, losses, distributions) according to negotiated terms](/business/binding-agreements/)[Tax AssessmentsBusiness

Entity structure (S-Corp salary/distribution split, pass-through vs C-Corp) directly determines exposure to assessments from misclassification, QBI disputes, and reasonable compensation challenges](/business/tax-assessments/)[pre-tax vs post-taxBusiness

Pre-tax vs post-tax optimization at entity scale: S-Corp salary/distribution splits, QBI deductions, and entity selection are the same 'when do I pay taxes' decision applied to business income instead of personal retirement contributions](/business/pre-tax-vs-post-tax/)[tax strategyBusiness

Entity structure (LLC, S-Corp, C-Corp, QBI deduction) is the individual-scale expression of business tax strategy - choosing the wrapper that minimizes total tax burden](/business/tax-strategy/)[Holding CompanyBusiness

Holding company is the corporate-scale version of entity structure choice - LLC vs S-Corp vs C-Corp at individual scale maps to holdco vs opco vs subsidiary structuring for tax efficiency and liability isolation](/business/holding-company/)

Many business owners pay an extra 10-20% of their profits in avoidable taxes without realizing it. Small structural choices can cost or save tens of thousands of dollars per year.

TL;DR:

Business entity tax is the mapping of business income to tax treatments - choosing between **sole proprietorship**, **LLC**, **S-Corp**, and **C-Corp** affects payroll taxes, pass-through deduction (QBI), and double taxation, and understanding trade-offs can change after-tax cash by roughly 5-25%.

## The Problem - What Goes Wrong When Structure Is Ignored

Many business owners treat entity choice as a legal formality. That mistake costs money. For example, a sole proprietor with $200,000 net profit commonly pays roughly 15.3% self-employment tax plus ordinary income tax at marginal rates, producing total federal tax exposure often north of 30% to 35% after deductions. If that same owner converts to an **S-Corp** and reports $80,000 as salary and $120,000 as distributions, the payroll tax base shrinks and employer/employee payroll taxes apply only to salary, which can reduce payroll-tax-like costs by about $6,000 to $12,000 in that scenario. Those are concrete numbers - not theoretical small percentages. Another frequent mistake is treating a **C-Corp** like a personal passthrough. A C-Corp faces a federal rate of 21% on earnings and later taxes dividends at qualified dividend rates, often producing combined federal tax near 32% to 40% when dividends are paid. That double layer matters when the business intends to distribute profits to owners. Meanwhile QBI - the **Qualified Business Income** deduction - can reduce taxable income for eligible pass-through owners by up to 20%, but it phases out above taxable income thresholds roughly $170,000 to $340,000 depending on filing status and is limited by W-2 wages and qualified property for higher incomes. Failing to consider QBI rules can forfeit a 20% slice of taxable income on $100,000 to $300,000 of profit, which is roughly a $4,000 to $12,000 federal tax swing for single filers at typical marginal rates. IF a business owner ignores payroll-tax mechanics AND expects to maximize after-tax distributions, THEN their take-home might be 5-25% lower than possible BECAUSE payroll taxes and entity-level taxes compound. This section starts from concrete dollars to make obvious what goes wrong. It also highlights that administrative cost for an S-Corp or electing corporate status often ranges from $500 to $3,000 per year in compliance, so any tax savings must exceed those costs to be worthwhile.

## How It Actually Works - Mechanics, Formulas, and Rules

This section explains the tax plumbing with formulas and numbers. First define the entities. **Sole proprietorship** and **single-member LLC** taxed as a sole prop: net business income flows to Schedule C, subject to ordinary income tax and self-employment tax at about 15.3% on net earnings up to the Social Security wage base, with an income-tax deduction equal to half of self-employment tax. **Partnerships and multi-member LLCs** are pass-throughs with K-1 reporting. **S-Corporation** is an entity-level election where profit flows to owners but owners who work must receive a "reasonable salary" subject to payroll taxes; remaining profit can be distributed as non-wage distributions. **C-Corporation** pays corporate tax at 21% federally, and later distributions face shareholder tax at qualified dividend rates (commonly 15% to 20%), producing double taxation. Key formulas: - Self-employed net income tax obligation approximately $SEtax = 0.153 \times NetProfit (up to wage base) - Employer-equivalent deduction taken on Form 1040 equals $0.5 \times SEtax - S-Corp payroll tax on salary equals Payroll=0.062×Salary(SocialSecurityemployee)+0.0145×Salary(Medicareemployee)+employermatchofroughlythesame,socombinedpayrollisaboutPayroll = 0.062 \times Salary (Social Security employee) + 0.0145 \times Salary (Medicare employee) + employer match of roughly the same, so combined payroll is about Payroll=0.062×Salary(SocialSecurityemployee)+0.0145×Salary(Medicareemployee)+employermatchofroughlythesame,socombinedpayrollisaboutPayrollTotal \approx 0.153 \times Salary for Social Security up to the wage base plus 2.9% Medicare on all wages. - Total cash available for owner distributions in S-Corp roughly Dist=NetProfit−Salary−EmployerPayrollTaxes−BusinessExpenses.QBIdeductionformulainsimpleform:Dist = NetProfit - Salary - EmployerPayrollTaxes - BusinessExpenses. QBI deduction formula in simple form: Dist=NetProfit−Salary−EmployerPayrollTaxes−BusinessExpenses.QBIdeductionformulainsimpleform:QBI\_{deduction} = 0.20 \times QualifiedBusinessIncomesubjecttotaxableincomephaseoutsandwages/propertylimitsforincomesabovethresholds.Numericalexamplesclarifyinteraction.IF subject to taxable income phaseouts and wages/property limits for incomes above thresholds. Numerical examples clarify interaction. IF subjecttotaxableincomephaseoutsandwages/propertylimitsforincomesabovethresholds.Numericalexamplesclarifyinteraction.IFNetProfit = $200,000 AND the owner takes Salary = $80,000, THEN payroll taxes apply to $80,000 only and distributions of $120,000 escape payroll taxes BECAUSE S-Corp rules tax only wages for employment taxes. That produces payroll-tax-like savings of roughly $0.153 \times $120,000 = $18,360 if distributions were otherwise wages, but only about $9,000 to $12,000 in practical savings after accounting for employer share and Medicare; exact savings depend on whether the owner would have otherwise paid self-employment tax on all profit. For C-Corps consider retained earnings. IF the business keeps $300,000 inside the C-Corp for three years for growth, THEN the immediate federal layer is $0.21 \times $300,000 = $63,000 BECAUSE corporate tax applies at entity level; distributions later add another layer. Finally, note S-Corp "reasonable salary" lacks a bright-line formula. Typical reasonable salary ranges from 30% to 60% of total distributable profit for many service businesses, but industry data and similar employee comparables drive IRS scrutiny. IF salary is set too low relative to comparable wages AND distributions are high, THEN IRS audit risk rises and back payroll taxes plus penalties may apply BECAUSE the IRS enforces reasonable-compensation rules to prevent payroll-tax avoidance.

## The Decision Framework - IF / THEN / BECAUSE Rules to Choose Structure

Problem-first: owners often chase tax-minimization without weighing administrative costs, audit risk, and long-term plans. This framework gives conditional rules with numbers and ranges to guide trade-offs. Rule cluster 1 - low-profit and minimal complexity. IF net annual profit is under $40,000 and the owner values simplicity and low compliance costs, THEN a sole proprietorship or single-member LLC taxed as a sole prop may be preferable BECAUSE annual accounting and payroll compliance costs of $500 to $3,000 likely exceed potential tax savings from formal S-Corp election. Rule cluster 2 - middle profits where payroll tax optimization matters. IF net annual profit lies between $40,000 and $250,000 AND the owner plans to extract most profits as personal income, THEN electing S-Corp status may reduce payroll-like taxes BECAUSE distributions avoid self-employment taxes while a reasonable salary covers payroll obligations. Practical conditional: choose a salary equal to 30% to 60% of total economic profit, then run the numbers. Example formula: compare total tax burden as a sole prop TaxSP=IncomeTax(NetProfit−0.5×SEtax)+SEtaxTax\_{SP} = IncomeTax(NetProfit - 0.5 \times SEtax) + SEtaxTaxSP​=IncomeTax(NetProfit−0.5×SEtax)+SEtax versus S-Corp TaxSC=IncomeTax(Salary+Distributions−EligibleDeductions)+PayrollTaxes(Salary)+CorporateLevelTax(usually0)Tax\_{SC} = IncomeTax(Salary + Distributions - EligibleDeductions) + PayrollTaxes(Salary) + CorporateLevelTax(usually 0)TaxSC​=IncomeTax(Salary+Distributions−EligibleDeductions)+PayrollTaxes(Salary)+CorporateLevelTax(usually0), and pick the lower after adding compliance costs of CadminC\_{admin}Cadmin​ between $500 and $3,000. Rule cluster 3 - high profit or growth-oriented companies. IF expected retained earnings exceed $300,000 per year for multi-year growth, THEN C-Corp structure may be attractive BECAUSE the flat 21% corporate rate can be lower than combined individual rates when profits are reinvested instead of distributed; however plan for eventual dividend taxation which creates combined tax rates commonly between 32% and 40% on distributed profits. Rule cluster 4 - QBI-focused decision. IF taxable income after deductions is under roughly $170,000 for single filers or $340,000 for married filing jointly, THEN pass-through entities may secure up to a 20% QBI deduction BECAUSE phaseouts do not apply below those ranges; for incomes above those thresholds use the W-2 wage and qualified-property formulas to test eligibility. Finally, include risk controls. IF the owner takes unusually low salary relative to market AND their business is profitable, THEN audit risk is material and retroactive payroll taxes plus interest often equal 12% to 30% of the disputed distributions BECAUSE the IRS reclassifies distributions as wages and assesses back taxes and penalties. This decision framework is conditional, numeric, and explicit about compliance costs and audit trade-offs.

## Edge Cases and Limitations - When This Framework Breaks Down

This framework omits or underweights several real-world situations. Limitation 1 - state and local tax variation. Many states tax S-Corps, LLCs, and C-Corps differently; for example, some states impose entity-level franchise taxes of $800 to $10,000 or substitute higher rates. IF the business operates in a high-tax state with an $800 minimum franchise tax, THEN the apparent federal savings from an S-Corp may evaporate BECAUSE state fees add fixed costs that reduce net benefit. Limitation 2 - fringe benefits and retirement planning. Employer-provided health insurance and retirement plan contributions interact with entity type and taxable wages. IF owners want pre-tax employer retirement contributions of $20,500 to $66,000 combined with profit-sharing, THEN C-Corp or S-Corp payroll treatment of wages can change the deductible calculation BECAUSE employer contributions often attach to W-2 wages. Limitation 3 - investor preferences and capital structure. Venture-backed companies typically prefer C-Corp status for stock classes and investor-friendly exit mechanics. IF the company plans to raise institutional capital or pursue an IPO, THEN electing C-Corp early may be preferable BECAUSE investors commonly demand C-Corp stock structure and qualified small business stock exceptions. Limitation 4 - multi-owner complications. Partnership allocations and Section 199A QBI splits become complex when partners have different involvement levels. IF ownership percentages shift or some owners are passive while others are active, THEN QBI allocation and wage limits may produce uneven tax outcomes BECAUSE the deduction calculation depends on the character of each owner's income. Limitation 5 - international and cross-border tax rules. This framework ignores foreign tax credits, Subpart F, global intangible low-taxed income, and treaty effects. IF the business has non-U.S. income over $50,000 or foreign subsidiaries, THEN entity choice analysis must include international tax regimes BECAUSE those rules can alter effective tax rates by 5% to 25% or more. Finally, note areas of uncertainty. IRS guidance on reasonable salary and certain QBI interpretations leaves room for audit. Treat savings estimates as ranges - for example payroll tax savings often range from 3% to 12% of gross profit, not a single point estimate. This section explicitly documents failures and where more specialized modeling is required.

## Worked Examples (3)

### Sole Proprietor vs S-Corp for $200,000 Net Profit

Net business profit = $200,000. Owner-operator will extract all profits. Marginal federal income tax rate approx 24% for the relevant income segment. Social Security wage base exceed the salary amounts used. Ignore state tax for simplicity.

1. Sole Proprietor calculation: SE tax = 0.153 \times $200,000 = $30,600. Deduction for half SE tax = $15,300. Taxable income for income tax = $200,000 - $15,300 = $184,700. Income tax estimate at 24% marginal on the top portion approximates $44,328 (this is a blended amount; use 24% for the high segment to illustrate). Total federal tax approx $30,600 + $44,328 = $74,928.
2. S-Corp option with Salary = $80,000 and Distribution = $120,000. Payroll taxes for salary - combined employer and employee components approximate 15.3% of $80,000 = $12,240. Owner income tax base = Salary $80,000 + Distribution $120,000 = $200,000 (same taxable income ignoring retirement and SE tax differences). However S-Corp avoids SE tax on distributions. Income-tax deduction differences: owner cannot deduct half SE tax, but employer payroll taxes are deductible to the corporation, and the owner still pays income tax on distributions. Approx total federal tax = payroll taxes $12,240 + income tax (using same blended 24% on $200,000) $44,328 = $56,568. Compare to sole prop total $74,928.
3. Net federal tax savings approx $74,928 - $56,568 = $18,360. Subtract additional compliance costs of $1,500 per year leads to net savings approx $16,860. Note this example assumes the IRS accepts the $80,000 salary as reasonable.
4. Sensitivity: If the IRS recharacterizes some distributions as wages later and imposes back payroll tax plus 20% penalties and interest, the apparent $16,860 saving could reverse and become a $30,000 to $50,000 cost. So audit-risk adjustments matter.

**Insight:** The largest tax driver here is whether profit is subject to self-employment tax or only to payroll taxes on a reasonable salary. S-Corp structure can yield ~$16,000 net annual federal savings on $200,000 profit under these assumptions, but audit risk and compliance costs materially affect net benefit.

### C-Corp for High-Retention Growth vs Pass-Through Distribution

Company earns $500,000 in pre-tax profit and plans either to: A) retain all earnings in a C-Corp for reinvestment; or B) pass profits through to a 1-owner S-Corp/sole prop and distribute. Ignore state taxes and assume qualified dividends taxed at 15% when later distributed.

1. C-Corp immediate tax: corporate tax = 0.21 \times $500,000 = $105,000. After-tax retained earnings = $395,000 available for reinvestment now.
2. If later the owner distributes $395,000 as qualified dividends, additional tax = 0.15 \times $395,000 = $59,250. Combined federal tax on original $500,000 = $105,000 + $59,250 = $164,250, which is an effective combined rate of $164,250 / $500,000 = 32.85%.
3. Pass-through option: assume S-Corp with Salary = $150,000 and Distribution = $350,000. Payroll taxes on salary (employer + employee) approx 15.3% of $150,000 = $22,950. Income tax on total personal income depends on marginal rates but for simplicity assume a blended federal rate equal to 24% on top slices, producing income tax approx $120,000. Total federal tax approx $22,950 + $120,000 = $142,950, effective rate 28.59%.
4. Comparison shows C-Corp plus later distribution yields roughly 33% effective federal tax, while immediate pass-through distribution yields roughly 29% under these assumptions. However C-Corp allows full reinvestment without requiring distributions, which might enable faster growth; if growth returns exceed the tax-cost spread by, say, 5-10% annualized, C-Corp retention could be economically superior.

**Insight:** C-Corp suits scenarios where retained capital produces higher expected returns than the tax penalty for double taxation. If reinvested growth returns exceed the 3% to 10% tax-adjusted spread, then C-Corp retention may make financial sense.

### QBI Deduction Phaseout Example for $300,000 Taxable Income

Owner of a pass-through business reports Qualified Business Income (QBI) of $250,000. Taxable income before QBI is $300,000 for a married filing jointly return. W-2 wages paid by the business equal $40,000. Assume phaseout thresholds approximately $340,000 for married filing jointly.

1. Because taxable income $300,000 is below the rough threshold $340,000, the owner qualifies for the full 20% QBI deduction on qualified income, subject to other limitations. Compute preliminary QBI deduction = 0.20 \times $250,000 = $50,000.
2. Taxable income after QBI deduction = $300,000 - $50,000 = $250,000. This reduces taxable income by $50,000, which at a blended marginal rate of 24% saves approximately $12,000 in federal income tax.
3. If taxable income had been $360,000 instead, the owner enters the phaseout zone and must apply the W-2 wage and qualified property limit. The wage limit equals the greater of (50% of W-2 wages) or (25% of W-2 wages + 2.5% of qualified property). Here 50% of W-2 wages = $20,000, which becomes the tentative cap. The final QBI deduction might be reduced to about $20,000 in that case, saving only $4,800 at 24% marginal, instead of $12,000.
4. Thus moving from $300,000 to $360,000 taxable income could reduce QBI benefit by $30,000 and raise federal tax by roughly $7,200 to $8,000, depending on marginal rates.

**Insight:** The QBI deduction provides up to 20% benefit, but the practical value falls rapidly across a narrow income band. Small increases in taxable income near $340,000 can remove $10,000 to $30,000 of QBI benefits, which makes tax planning around deductions and salary timing valuable.

## Key Takeaways

- ✓

  If net profit is under $40,000, the expected administrative cost of S-Corp election ($500 to $3,000 annually) often outweighs payroll-tax savings; prioritize simplicity.
- ✓

  If net profit is between $40,000 and $250,000, estimate an S-Corp salary of 30% to 60% of profit and compare total tax plus compliance; expected payroll-tax savings often fall between 3% and 12% of gross profit.
- ✓

  If profits will be retained and reinvested for multi-year growth exceeding expected tax-adjusted return spreads of 3% to 10%, then C-Corp retention can be economically reasonable despite potential 32% to 40% combined eventual taxation on distributions.
- ✓

  QBI can reduce taxable income up to 20% for pass-through owners when taxable income is under approximately $170,000 (single) or $340,000 (MFJ); above those thresholds wage and property limits frequently curtail the benefit.
- ✓

  Set an S-Corp salary using industry comparables - commonly 30% to 60% of distributable earnings - because setting it too low creates audit risk plus back payroll taxes and penalties that can exceed earlier savings.
- ✓

  Always model after-tax cash flows including compliance costs of $500 to $3,000 and state-level taxes or franchise fees when comparing entity choices.

## Common Mistakes

- ✗

  Treating S-Corp salary as a free lever. This is wrong because unreasonable low salaries invite IRS reclassification, back payroll taxes, and penalties which often exceed initial tax savings.
- ✗

  Ignoring state taxes and fixed franchise fees. Many analyses only model federal taxes; this is wrong because state franchise taxes of $800 to $10,000 per year can erase federal savings for small businesses.
- ✗

  Assuming QBI always gives a straight 20% cut. That is wrong because QBI phases out above taxable-income thresholds and can be limited by W-2 wages and qualified property rules.
- ✗

  Using point estimates rather than ranges. A single-number savings claim is misleading because payroll-tax savings commonly vary between 3% and 12% of profit depending on salary choice, Social Security wage caps, and Medicare surcharges.

## Practice

easy

Easy: You run a single-member LLC with $75,000 net profit. Estimate whether S-Corp election might be worth considering given compliance cost of $1,200 per year. Assume rough payroll tax rate 15.3% and marginal federal rate 22%. Use Salary = $35,000 option for the S-Corp.

**Hint:** Compute sole prop tax = SE tax + income tax. Compute S-Corp payroll taxes on salary and income tax on full amount, then subtract compliance cost.

Show solution

Sole prop: SE tax = 0.153 \times $75,000 = $11,475. Half SE deduction = $5,737. Taxable income approx $75,000 - $5,737 = $69,263. Income tax at 22% top slice approximates $15,238. Total federal tax approx $11,475 + $15,238 = $26,713. S-Corp: Salary = $35,000, Distribution = $40,000. Payroll taxes approx 0.153 \times $35,000 = $5,355. Income tax on $75,000 (salary + distribution) similar approx $15,238. Total federal tax approx $5,355 + $15,238 = $20,593. Subtract compliance cost $1,200 gives net 1-year tax position $21,793. Net saving vs sole prop = $26,713 - $21,793 = $4,920. Conclusion: S-Corp may be worth considering since estimated first-year net savings ~ $4,900, exceeding $1,200 compliance cost. Remember ranges and audit risk.

medium

Medium: Compare a C-Corp that earns $300,000 and retains all earnings for reinvestment for the year versus an S-Corp that distributes all earnings. Compute immediate federal tax effect and combined federal tax if the C-Corp later distributes the retained earnings as qualified dividends. Assume corporate tax rate 21% and qualified dividend tax 15%. Ignore state tax and payroll taxes for the S-Corp owner.

**Hint:** Compute corporate tax first, then dividend tax on remaining amount.

Show solution

C-Corp immediate: corporate tax = 0.21 \times $300,000 = $63,000. After-tax retained = $237,000. If later distributed as qualified dividends, dividend tax = 0.15 \times $237,000 = $35,550. Combined federal tax = $63,000 + $35,550 = $98,550, which is 32.85% of $300,000. S-Corp distributing all earnings to owner: owner pays income tax at individual rates; ignoring payroll taxes and using a blended income-tax estimate of 24% gives tax = 0.24 \times $300,000 = $72,000. Comparison: S-Corp distribution leads to lower immediate combined federal tax (24% vs 32.85%), but C-Corp may be preferable if retained capital produces returns exceeding the tax-adjusted difference.

hard

Hard: A married couple filing jointly has taxable income before QBI deduction of $360,000. Their pass-through business reports QBI of $200,000 and W-2 wages paid of $60,000. Estimate the approximate QBI deduction using the wage limit test: QBI deduction limited to the greater of (50% of W-2 wages) or (25% of W-2 wages + 2.5% of qualified property). Use the 50%-of-wages figure for simplicity.

**Hint:** Compute 50% of W-2 wages, then the QBI deduction is the lesser of 20% of QBI and that wage-based limit when in phaseout.

Show solution

50% of W-2 wages = 0.50 \times $60,000 = $30,000. 20% of QBI = 0.20 \times $200,000 = $40,000. Because taxable income $360,000 exceeds the rough MFJ threshold $340,000, the wage limit applies. The QBI deduction is limited to $30,000. Therefore taxable income after QBI deduction = $360,000 - $30,000 = $330,000. Relative to the full 20% deduction, the owner loses $10,000 of deduction, which at a 24% marginal rate increases federal tax by approximately $2,400 compared to the full QBI outcome.

## Connections

This lesson builds on the prerequisite "Tax Brackets" (/money/tax-brackets) where marginal versus effective rates were explained, and on "Capital Gains" (/money/capital-gains) which covered qualified dividends and long-term rates. Mastering business entity tax unlocks deeper planning topics such as "Retirement Plan Design for Business Owners" (/money/retirement-plans-business), "Business Sale Tax Planning and Section 1202" (/money/business-sale-tax), and "Advanced Entity-Level International Tax" (/money/international-tax). These downstream areas require understanding how entity choice affects taxable income, payroll wages, and timing of taxable events.

**Disclaimer:** This content is for educational and informational purposes only and does not constitute financial, investment, tax, or legal advice. It is not a recommendation to buy, sell, or hold any security or financial product. You should consult a qualified financial advisor, tax professional, or attorney before making financial decisions. Past performance is not indicative of future results. The author is not a registered investment advisor, broker-dealer, or financial planner.

[← back to tree](/money/)[browse all →](/money/inventory/)
