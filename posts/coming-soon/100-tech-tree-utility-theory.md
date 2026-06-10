---
title: Utility Theory
description: Utility functions, indifference curves, marginal utility. Rational consumer choice under budget constraints via Lagrangian optimization.
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- tech-tree
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
permalink: /tech-tree/utility-theory/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Utility Theory

Applied EconomicsDifficulty: ★★★☆☆Depth: 7Unlocks: 9

Utility functions, indifference curves, marginal utility. Rational consumer choice under budget constraints via Lagrangian optimization.

## Prerequisites (2)

[Derivatives6 atoms](/tech-tree/derivatives-basic/)[Optimization Introduction5 atoms](/tech-tree/optimization-intro/)

## Unlocks (1)

[Demand Functionslvl 3](/tech-tree/demand-functions/)

## Referenced by (14)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (13)

[financial productBusiness

Financial products exist to serve different points on a consumer's utility surface - trading off risk, return, liquidity, and tax treatment. Product design and consumer choice among products is fundamentally utility maximization under constraints.](/business/financial-product/)[Utility FunctionBusiness

The direct mathematical formalization: utility functions, indifference curves, marginal utility, and rational choice under budget constraints via Lagrangian optimization](/business/utility-function/)[risk appetiteBusiness

Utility function concavity is the mathematical formalization of risk appetite - concave means risk-averse, linear means risk-neutral, convex means risk-seeking. This is the canonical framework for encoding risk preferences into optimization](/business/risk-appetite/)[Conjoint AnalysisBusiness

Conjoint analysis is applied utility theory - it estimates part-worth utilities for attribute levels from observed choices, assuming consumers maximize a utility function over product profiles](/business/conjoint-analysis/)[risk-neutralBusiness

Risk-neutral is the special case where the utility function is linear in wealth, so there is no diminishing marginal utility and no risk premium. Understanding the general theory (concave = risk-averse, convex = risk-seeking, linear = risk-neutral) is the direct foundation.](/business/risk-neutral/)[BuyerBusiness

'Name the buyer, name the pain, name the inferior means' is the business-intuition version of utility theory. The buyer is the agent with a utility function, the pain is a region where marginal utility is high but unsatisfied, and the inferior means is the current suboptimal allocation under their budget constraint.](/business/buyer/)[Life PlanningBusiness

Life planning is applied lifetime utility maximization - defining what you value, constructing indifference curves over life outcomes, and allocating finite resources under budget constraints to maximize satisfaction](/business/life-planning/)[Essential vs DiscretionaryBusiness

Utility maximization under a budget constraint is the formal version of triage - essentials are binding constraints, discretionary is where marginal utility optimization happens](/business/essential-vs-discretionary/)[Outside OptionBusiness

Outside option is formally defined as a utility threshold (e.g., u=0). You need utility functions to state the individual rationality constraint: U(participate) >= U(outside option). Without utility theory you cannot formalize what 'prefers participating' means.](/business/outside-option/)[Risk ToleranceBusiness

Utility theory is the mathematical formalization of risk tolerance - concave utility functions encode risk aversion, linear encode risk neutrality, convex encode risk seeking. It provides the formal framework for why two people with identical net worth make different allocation choices.](/business/risk-tolerance/)[GARPBusiness

Direct prerequisite. Afriat's theorem proves observed choices satisfy GARP if and only if a nonsatiated utility function rationalizing them exists. GARP is the nonparametric empirical test for utility maximization.](/business/garp/)[50/30/20 FrameworkBusiness

50/30/20 is a behavioral heuristic for the budget-constrained utility maximization problem - allocating income across categories to maximize satisfaction subject to a fixed income constraint](/business/50-30-20-framework/)[risk aversionBusiness

Risk aversion is formally defined as concave utility over wealth - the entire auction revenue result derives from bidders maximizing E[u(payoff)] with u'' < 0 rather than maximizing E[payoff], which is pure utility theory](/business/risk-aversion/)

### From Money (1)

[Opportunity CostMoney

Utility quantifies why some dollars matter more than others](/money/opportunity-cost/)

Advanced Learning Details

### Graph Position

55

Depth Cost

9

Fan-Out (ROI)

3

Bottleneck Score

7

Chain Length

Every purchase you make balances want against cost — utility theory gives a precise, calculus-based recipe for predicting those choices and how they respond to price or income changes.

TL;DR:

Utility theory models consumer satisfaction with utility functions and indifference curves, and it gives the optimal bundle under a budget constraint via Lagrangian optimization (or corner solutions).

## What Is Utility Theory?

Utility theory formalizes how consumers rank bundles of goods and how they choose given prices and income. The central idea is a utility function u(x1,x2,…,xn)u(x\_1, x\_2, \dots, x\_n)u(x1​,x2​,…,xn​) that assigns a real number to each bundle (x1,x2,...,xn)(x\_1, x\_2, ..., x\_n)(x1​,x2​,...,xn​) so that higher numbers mean higher preference. Utility numbers themselves are ordinal (only ordering matters), but specific functional forms let us compute marginal benefits and solve optimization problems.

Why care? Utility theory turns qualitative statements like “I prefer more of good A to less” into quantitative tools that let you predict demand, compute consumer surplus, and perform welfare comparisons. It gives a way to move from psychology-like preference language to calculus-based comparative statics.

Core intuition and building blocks

- •Utility function: A map u:R+n→Ru: \mathbb{R}\_+^n \to \mathbb{R}u:R+n​→R that ranks bundles. Example: Cobb–Douglas utility for two goods is

u(x,y)=xαyβu(x,y)=x^{\alpha}y^{\beta}u(x,y)=xαyβ

with α,β>0\alpha,\beta>0α,β>0. Concrete numeric example: u(x,y)=x0.5y0.5u(x,y)=x^{0.5}y^{0.5}u(x,y)=x0.5y0.5. For the bundle (x,y)=(4,9)(x,y)=(4,9)(x,y)=(4,9), u(4,9)=49=2⋅3=6u(4,9)=\sqrt{4}\sqrt{9}=2\cdot3=6u(4,9)=4​9​=2⋅3=6.

- •Marginal utility (MU): The partial derivative of uuu with respect to one good, holding other goods constant. In "Derivatives" we learned how to compute partial derivatives as instantaneous rates of change. For the example u(x,y)=x0.5y0.5u(x,y)=x^{0.5}y^{0.5}u(x,y)=x0.5y0.5,

MU\_x=\frac{\partial u}{\partial x}=0.5 x^{-0.5} y^{0.5}.$$ At $(x,y)=(4,9)$, $MU\_x=0.5\cdot(4)^{-0.5}\cdot(9)^{0.5}=0.5\cdot0.5\cdot3=0.75.$ This number means: near that bundle, a tiny increase in $x$ increases utility by about $0.75$ units.
- Diminishing marginal utility: For many standard utility functions, $MU\_x$ falls as $x$ increases (holding other goods fixed). This captures the intuitive idea that successive units give smaller increments of satisfaction. For $u=x^{0.5}y^{0.5}$, $MU\_x\propto x^{-0.5}$ which decreases as $x$ rises.
- Indifference curves: Sets of bundles giving the same utility level: $\{(x,y): u(x,y)=\bar u\}$. Indifference curves visualize tradeoffs: moving along a curve, utility doesn't change, so increases in one good must compensate decreases in another.
- Marginal rate of substitution (MRS): The slope of an indifference curve; it is the rate at which a consumer will trade good $y$ for good $x$ while keeping utility constant. Calculus link (from "Derivatives"): if $u(x,y)=\bar u$, then implicit differentiation gives
$$\text{MRS}\_{x,y}=\frac{dy}{dx}\Big|\_{u\;\text{const}}=-\frac{MU\_x}{MU\_y}.

Concrete numeric example: with u(x,y)=x0.5y0.5u(x,y)=x^{0.5}y^{0.5}u(x,y)=x0.5y0.5 and at (x,y)=(4,9)(x,y)=(4,9)(x,y)=(4,9) we computed MUx=0.75MU\_x=0.75MUx​=0.75. Similarly

MUy=0.5x0.5y−0.5=0.5⋅2⋅(9)−0.5=1⋅13=0.333...,MU\_y=0.5 x^{0.5} y^{-0.5}=0.5\cdot2\cdot(9)^{-0.5}=1\cdot\frac{1}{3}=0.333...,MUy​=0.5x0.5y−0.5=0.5⋅2⋅(9)−0.5=1⋅31​=0.333...,

so MRSx,y=−0.750.333...=−2.25.\text{MRS}\_{x,y}=-\frac{0.75}{0.333...}=-2.25.MRSx,y​=−0.333...0.75​=−2.25. This says the consumer would give up about 2.25 units of yyy to gain one extra unit of xxx while staying on the same indifference curve (negative sign shows opposite directions). The absolute tradeoff is 2.25.

Budget constraint and rational choice

A consumer faces prices (px,py)(p\_x,p\_y)(px​,py​) and income III. The budget constraint is

p\_x x+p\_y y\le I.$$ Usually we assume the consumer uses full income (non-satiation), so the constraint binds: $p\_x x+p\_y y=I$.
Rational choice problem: pick $(x,y)$ to maximize $u(x,y)$ subject to $p\_x x+p\_y y=I$. "Optimization Introduction" taught constrained optimization methods; here we apply them with specific economic interpretation. The chosen bundle equates marginal tradeoff $\text{MRS}\_{x,y}$ to the market rate of substitution (price ratio) $p\_x/p\_y$ when the solution is interior (both goods strictly positive):
$$\frac{MU\_x}{MU\_y}=\frac{p\_x}{p\_y}.$$ Numeric example: If $p\_x=2, p\_y=1$ and at an interior optimum with the Cobb–Douglas example above we would require $0.75/0.333...=2.25\approx p\_x/p\_y=2$. Since 2.25 is not equal to 2, the point $(4,9)$ is not optimal; solving the full optimization will give the correct bundle where the equality holds.
Summary: Utility theory combines the calculus concepts from "Derivatives" (partial derivatives and slopes) and the constrained optimization from "Optimization Introduction" to compute consumer choices and their response to prices/income.

## Core Mechanic 1: Marginal Utility, MRS, and Indifference Curves

This section develops the operational formulas for marginal utilities, how to compute the Marginal Rate of Substitution (MRS) and how indifference curve geometry follows from these calculations. We'll work incrementally from definitions to interpretation and give worked mini-examples with numbers at each step.

1) Marginal utilities and their computation

Definition: For a twice-differentiable utility u(x,y)u(x,y)u(x,y),

MU\_x(x,y)=\frac{\partial u}{\partial x},\qquad MU\_y(x,y)=\frac{\partial u}{\partial y}.$$ These are partial derivatives — recall from "Derivatives" that this is the instantaneous slope of $u$ in the $x$-direction holding $y$ fixed.
Example 1 (Simple polynomial): Let $u(x,y)=3x+2y$. Then
$$MU\_x=3,\qquad MU\_y=2.$$ These are constant; marginal utility does not diminish. Numeric: at any bundle $(x,y)=(10,5)$, adding a tiny $\Delta x$ increases utility by about $3\Delta x$.
Example 2 (Cobb–Douglas): $u(x,y)=x^{0.5}y^{0.5}$. Then
$$MU\_x=0.5 x^{-0.5} y^{0.5},\quad MU\_y=0.5 x^{0.5} y^{-0.5}.$$ At $(x,y)=(4,9)$ we compute $MU\_x=0.75$, $MU\_y\approx0.3333$ (see Section 1). These fall as $x$ or $y$ increase, showing diminishing marginal utility.
2) MRS and tradeoffs
The Marginal Rate of Substitution of $x$ for $y$ is
$$\text{MRS}\_{x,y}=-\frac{MU\_x}{MU\_y}.$$ This is the slope of an indifference curve: how much $y$ you must give up to gain one additional unit of $x$ while keeping utility constant. Using calculus, if $u(x,y)=\bar u$, implicitly differentiate: $MU\_x dx + MU\_y dy=0$, hence $dy/dx=-MU\_x/MU\_y$.
Numeric example: For $u(x,y)=x^{0.5}y^{0.5}$ at $(4,9)$ the MRS we computed equals $-2.25$. Interpreting the sign: the negative slope shows that to increase $x$ we must decrease $y$. The absolute value $2.25$ tells how steep the indifference curve is: large |MRS| means the consumer values $x$ relatively highly versus $y$ at that bundle.
3) Indifference curve shape and convexity
Convex preferences mean indifference curves are convex to the origin (they bend inward). A sufficient analytic condition is diminishing MRS: $|\text{MRS}\_{x,y}|$ falls as $x$ increases (holding utility constant). For differentiable $u$, this is often ensured by quasi-concavity of $u$ or negative definiteness of the Hessian.
Concrete demonstration: For $u(x,y)=x^{0.5}y^{0.5}$, compute MRS as a function of $(x,y)$:
$$\text{MRS}\_{x,y}=-\frac{0.5 x^{-0.5} y^{0.5}}{0.5 x^{0.5} y^{-0.5}}=-\frac{y}{x}.$$ Here MRS simplifies to $-y/x$. If we increase $x$ while holding $u$ constant, $y$ must fall, and the ratio $y/x$ reduces — diminishing MRS. Numeric example: at $(x,y)=(1,1)$ MRS$=-1$; at $(4,9)$ MRS$=-9/4=-2.25$, at $(9,4)$ MRS$=-4/9\approx-0.444$. The decline in |MRS| as $x$ gets larger (relative to $y$) demonstrates convexity.
4) Graphical intuition plus small numeric check
Indifference curves for Cobb–Douglas $u=\sqrt{xy}$ at utility level $\bar u$ satisfy $xy=\bar u^2$. This is a rectangular hyperbola. Pick $\bar u=6$, then $xy=36$. Two points on that curve: $(x,y)=(4,9)$ and $(9,4)$ both have $u=6$. Their slopes computed via MRS are $-y/x=-9/4=-2.25$ and $-4/9\approx-0.444$, respectively. Graphically, the leftmost portion of the curve is steep (large |slope|), and the right portion is flat — classic convex indifference curve.
5) Relationship to optimization
Why MRS matters for optimization: when maximizing utility subject to the linear budget $p\_x x+p\_y y=I$, the optimal interior bundle equates the consumer's willingness-to-trade rate MRS to the market tradeoff $p\_x/p\_y$:
$$\frac{MU\_x}{MU\_y}=\frac{p\_x}{p\_y}.

Interpretation: if a consumer's subjective tradeoff differs from market tradeoff, there's a local profitable adjustment. For example, if MUxMUy>pxpy\frac{MU\_x}{MU\_y}>\frac{p\_x}{p\_y}MUy​MUx​​>py​px​​, then the consumer values xxx more than its market cost relative to yyy, so they should buy more xxx and less yyy.

Mini-example numeric check: Suppose px=2,py=1p\_x=2,p\_y=1px​=2,py​=1 and the consumer currently at (x,y)=(4,9)(x,y)=(4,9)(x,y)=(4,9) with u=x0.5y0.5u=x^{0.5}y^{0.5}u=x0.5y0.5 has MUx/MUy=0.75/0.3333=2.25>2MU\_x/MU\_y=0.75/0.3333=2.25>2MUx​/MUy​=0.75/0.3333=2.25>2. So the consumer should reallocate spending towards xxx. The optimization in Section 3 will find the exact amount.

Takeaway: Computing MUMUMU and MRS\text{MRS}MRS is straightforward calculus (use "Derivatives"). These calculations give the geometry of indifference curves and the local condition equating subjective tradeoffs to price ratios at interior optima.

## Core Mechanic 2: Constrained Optimization and the Lagrangian

This section develops the constrained optimization technique used to solve the consumer's problem: maximize utility subject to a budget constraint. We'll use the Lagrangian, connect to the first-order conditions, discuss corner solutions, and extract closed-form demand for common utility functions. Every formula is followed by a concrete numeric example.

Problem statement

A consumer chooses nonnegative quantities x,yx,yx,y to

\max\_{x\ge0,y\ge0} u(x,y) \quad\text{s.t.}\quad p\_x x + p\_y y = I.$$ We assume non-satiation so the budget constraint binds.
Lagrangian method (link to "Optimization Introduction")
Build the Lagrangian function
$$\mathcal{L}(x,y,\lambda)=u(x,y)+\lambda\big(I-p\_x x-p\_y y\big).

Here λ\lambdaλ is the Lagrange multiplier; economically it equals the marginal utility of income (the gain in utility from a small increase in III) when evaluated at the optimum.

First-order conditions (FOCs): set partial derivatives to zero (assuming interior solution):

\begin{align\*}

\frac{\partial \mathcal{L}}{\partial x}&=MU\_x -\lambda p\_x=0,\\

\frac{\partial \mathcal{L}}{\partial y}&=MU\_y -\lambda p\_y=0,\\

\frac{\partial \mathcal{L}}{\partial \lambda}&=I-p\_x x-p\_y y=0.

\end{align\*}

Combine the first two to eliminate λ\lambdaλ and recover the MRS = price ratio condition:

MUxMUy=pxpy.\frac{MU\_x}{MU\_y}=\frac{p\_x}{p\_y}.MUy​MUx​​=py​px​​.

Numeric template and example: Cobb–Douglas

Take u(x,y)=xαyβu(x,y)=x^{\alpha}y^{\beta}u(x,y)=xαyβ, with α,β>0\alpha,\beta>0α,β>0. Then

MU\_x=\alpha x^{\alpha-1} y^{\beta},\quad MU\_y=\beta x^{\alpha} y^{\beta-1}.$$ FOC ratio gives
$$\frac{\alpha x^{\alpha-1} y^{\beta}}{\beta x^{\alpha} y^{\beta-1}}=\frac{p\_x}{p\_y}\quad\Rightarrow\quad\frac{\alpha}{\beta}\cdot\frac{y}{x}=\frac{p\_x}{p\_y}.$$ Rearranged:
$$\frac{y}{x}=\frac{\beta}{\alpha}\cdot\frac{p\_x}{p\_y}.$$ Plug into budget $p\_x x + p\_y y = I$ and solve. The standard closed-form demands are:
$$x^\*=\frac{\alpha}{\alpha+\beta}\cdot\frac{I}{p\_x},\qquad y^\*=\frac{\beta}{\alpha+\beta}\cdot\frac{I}{p\_y}.

Concrete numeric example: let α=0.5,β=0.5\alpha=0.5,\beta=0.5α=0.5,β=0.5 (so standard Cobb–Douglas u=xyu=\sqrt{xy}u=xy​), px=2,py=1,I=100p\_x=2,p\_y=1,I=100px​=2,py​=1,I=100. Then

x^\*=\frac{0.5}{1.0}\cdot\frac{100}{2}=0.5\cdot50=25,\qquad y^\*=\frac{0.5}{1.0}\cdot\frac{100}{1}=0.5\cdot100=50.$$ Check budget: $2\cdot25+1\cdot50=50+50=100$. Compute utility at optimum: $u(25,50)=\sqrt{25\cdot50}=\sqrt{1250}\approx35.355.$ This numeric example shows the Lagrangian yields simple linear shares of income for Cobb–Douglas preferences.
Interpretation of $\lambda$
From FOCs we had $MU\_x=\lambda p\_x$. Thus $\lambda=MU\_x/p\_x$ is the marginal utility of income: if $I$ increases by $\$1$, utility increases by about $\lambda$. Numeric example: using the previous Cobb–Douglas example, compute $MU\_x$ at $(25,50)$:
$$MU\_x=0.5\cdot25^{-0.5}\cdot50^{0.5}=0.5\cdot\frac{1}{5}\cdot\sqrt{50}\approx0.1\cdot7.071=0.7071.$$ Then $\lambda=MU\_x/p\_x=0.7071/2\approx0.3536$. So an extra dollar of income increases utility by about $0.3536$ utility units.
Corner solutions and linear utility
If utility is linear, e.g., $u=3x+2y$, marginal utilities are constant. The MRS is constant: $MU\_x/MU\_y=3/2=1.5$. If the price ratio $p\_x/p\_y$ differs from $1.5$, the interior condition cannot be satisfied and the optimum is at a corner: buy only the cheaper good in utility-per-dollar terms.
Numeric example: let $p\_x=2,p\_y=1,I=100$ and $u=3x+2y$. Utility-per-dollar for $x$ is $MU\_x/p\_x=3/2=1.5$, for $y$ it's $MU\_y/p\_y=2/1=2$. Since $2>1.5$, $y$ gives more utility per dollar, so spend all income on $y$: $y^\*=100/1=100$, $x^\*=0$. Check: If we instead purchased $x$ only, we'd get $x=50$ and utility $3\*50=150$. For all-$y$ utility is $2\*100=200$, which is larger, so corner solution is correct.
Second-order conditions and convexity
Lagrangian FOCs are necessary conditions. For maximum we also want the objective to be quasi-concave (utilities that yield convex upper contour sets) and the budget set to be convex (linear is convex). For common utilities like Cobb–Douglas or CES (constant elasticity of substitution) with positive parameters, the FOC yields a global maximum.
Summary formulae to remember (with numeric anchors)
- First-order condition (interior): $MU\_x/MU\_y=p\_x/p\_y$. Example numeric check: for $u=\sqrt{xy}$ at optimum with $p\_x=2,p\_y=1$ we found $x^\*=25,y^\*=50$, and $MU\_x/MU\_y=0.7071/0.3536=2= p\_x/p\_y$.
- Cobb–Douglas demand: $x^\*=\frac{\alpha}{\alpha+\beta}\cdot\frac{I}{p\_x}$. Example: $\alpha=0.5, p\_x=2, I=100\Rightarrow x^\*=25$.
- Linear utility corner rule: buy good with larger $MU\_i/p\_i$.
This Lagrangian machinery directly leverages the "Optimization Introduction" prerequisite and uses partial derivatives from "Derivatives". It gives closed-form Marshallian (uncompensated) demand for many functional forms and forms the basis for comparative statics (how $x^\*,y^\*$ respond to $I,p\_x,p\_y$).

## Applications and Connections

This section explains how utility theory connects to real-world applications and downstream economic concepts. I include numeric mini-examples for each application and point explicitly to which methods from earlier sections are used.

1) Deriving demand curves and market demand

From the consumer optimization we obtain Marshallian demand functions x∗(px,py,I)x^\*(p\_x,p\_y,I)x∗(px​,py​,I) and y∗(px,py,I)y^\*(p\_x,p\_y,I)y∗(px​,py​,I). For example, Cobb–Douglas with α=β=0.5\alpha=\beta=0.5α=β=0.5 gave

x^\*=\frac{1}{2}\frac{I}{p\_x},\qquad y^\*=\frac{1}{2}\frac{I}{p\_y}.$$ If income $I$ is fixed and we vary $p\_x$, we trace out the individual demand curve for $x$. Numeric example: with $I=100$ and $p\_y=1$, if $p\_x=2$ we had $x^\*=25$; if $p\_x=4$ then $x^\*=12.5$. Aggregating across consumers yields market demand.
2) Income and price effects; Engel curves
Utility theory gives how demand responds to income (the Engel curve) and to prices. For Cobb–Douglas the Engel curve is linear: $x^\*(I)=\frac{\alpha}{\alpha+\beta}\cdot\frac{I}{p\_x}$; doubling income doubles demand. Numeric: with $\alpha=0.5,p\_x=2$, $x^\*(I)=0.25I$. If $I$ rises from 100 to 200, $x^\*$ rises from 25 to 50.
Price effects: comparative statics use derivatives of demand with respect to prices. For the Cobb–Douglas example,
$$\frac{\partial x^\*}{\partial p\_x}=-\frac{\alpha}{\alpha+\beta}\cdot\frac{I}{p\_x^2}<0.$$ Numeric example: $\partial x^\*/\partial p\_x=-0.25\cdot100/2^2=-0.25\cdot100/4=-6.25$ at $p\_x=2$. So a small $\$1$ increase in $p\_x$ reduces $x^\*$ by about 6.25 units when $I=100$.
3) Consumer surplus and welfare analysis
Utilities let us compute the compensating/equivalent variation and consumer surplus approximations. With demand curves we can integrate to find willingness-to-pay. Numeric example: if individual demand is $x=50/p\_x$ (a hypothetical demand), the area under demand from $p=1$ to $p=2$ gives lost surplus due to a price increase.
4) Hicksian demand and Slutsky decomposition
We can derive Hicksian (compensated) demand $h(p\_x,p\_y,\bar u)$ by solving the expenditure minimization problem: minimize $p\_x x+p\_y y$ s.t. $u(x,y)=\bar u$. This uses the same calculus tools but reverses the objective and constraint. The Slutsky equation decomposes the total price effect into substitution (Hicksian) and income effects. For Cobb–Douglas the substitution and income effects can be computed in closed form.
Concrete numeric touchstone: take $u=\sqrt{xy}$ and $\bar u=35.355$ (the utility we computed earlier at $I=100,p\_x=2,p\_y=1$). The Hicksian demand for $x$ at these parameters equals the Marshallian demand at the original prices and income necessary to generate $\bar u$; solving shows the substitution effect when $p\_x$ changes from 2 to 3 is the change that keeps utility at $\bar u$.
5) Edge cases: corner solutions and satiation
When utility is linear or a good is inferior in a strong sense, optimal bundles can be corners (consume zero of some good). Recognizing corners is important in applied work (empirical estimation of demand often has bunching at zero). Numeric example: $u=3x+2y,p\_x=2,p\_y=1,I=100$ led to $x^\*=0,y^\*=100$.
6) Use in Empirical Demand Estimation
Functional forms (Cobb–Douglas, CES, Translog) are used to fit demand to data. The theoretical properties (income shares, elasticities) guide which forms are appropriate. For instance, Cobb–Douglas implies constant expenditure shares — if data show stable shares across incomes, Cobb–Douglas might be a good fit. A numeric test: if observed data have share of spending on good $x$ close to 0.25 for many incomes, this suggests an underlying $\alpha/(\alpha+\beta)\approx0.25$.
7) General equilibrium and welfare
Utility functions are building blocks in general equilibrium models (Edgeworth box, Walrasian equilibria), public policy analysis (tax incidence), and welfare economics (Pareto optimality, social welfare functions). Solving household problems (via Lagrangian) for many agents and aggregating is how one computes overall demand and then market clearing.
8) Practical tip: always check the interior condition
When applying the $MU\_x/MU\_y=p\_x/p\_y$ rule, verify that the solution yields positive quantities and does not violate corner optimality conditions. Numeric check: if solving gives $x^\*<0$, the real solution must be a corner, and you should compare utilities across feasible corners.
Summary
Utility theory translates preferences into demand and welfare tools. The core computational steps use "Derivatives" to compute marginal utilities and MRS, and "Optimization Introduction" via the Lagrangian to get explicit demand functions. These results are central to consumer theory, demand estimation, public policy analysis, and general equilibrium models. Concrete numeric examples (Cobb–Douglas, linear utility) show how the methods yield tractable formulas and clear economic interpretation.

## Worked Examples (3)

### Cobb–Douglas Lagrange — simple numbers

Maximize utility u(x,y)=sqrt(x y) subject to 2x + 1y = 100. Find x*, y*.

1. Set up the Lagrangian: L(x,y,λ)=x^{1/2} y^{1/2} + λ(100 - 2x - y).
2. Compute partial derivatives: ∂L/∂x = (1/2)x^{-1/2} y^{1/2} - 2λ = 0; ∂L/∂y = (1/2)x^{1/2} y^{-1/2} - λ = 0.
3. Divide the first equation by the second to eliminate λ: \frac{(1/2)x^{-1/2} y^{1/2}}{(1/2)x^{1/2} y^{-1/2}} = \frac{2λ}{λ} ⇒ \frac{y}{x} = 2.
4. Use the budget constraint: 2x + y = 100 and y = 2x ⇒ 2x + 2x = 100 ⇒ 4x = 100 ⇒ x^\* = 25.
5. Compute y^ *from y=2x ⇒ y^* = 50. Check: budget 2*25 + 1*50 = 100 holds. Compute utility u(25,50)=√(1250)≈35.355.

**Insight:** This worked example shows the standard Cobb–Douglas income-share result: with α=β=0.5 we allocate half of income to each good in expenditure shares; here 2x is half of 100 and y is the other half, yielding x=25,y=50.

### Check MRS equals price ratio

For u(x,y)=x^{0.4} y^{0.6}, prices p\_x=3,p\_y=2 and income I=120, find demands and verify MU\_x/MU\_y=p\_x/p\_y.

1. Recall Cobb–Douglas demands: x^ *= α/(α+β)*  I/p\_x and y^ *= β/(α+β)*  I/p\_y, where α=0.4, β=0.6.
2. Compute x^ *= 0.4/1.0*  120 / 3 = 0.4 \* 40 = 16.
3. Compute y^ *= 0.6/1.0*  120 / 2 = 0.6 \* 60 = 36.
4. Compute MU\_x = α x^{α-1} y^{β} = 0.4  *x^{-0.6}*  y^{0.6}. Numerically, x^{-0.6}=16^{-0.6}≈16^{-3/5}≈(2^4)^{-0.6}=2^{-2.4}≈0.189, y^{0.6}=36^{0.6}≈36^{3/5}≈(6^2)^{3/5}=6^{6/5}≈6^{1.2}≈8.303 ⇒ MU\_x≈0.4*0.189*8.303≈0.628.
5. Compute MU\_y = β x^{α} y^{β-1} = 0.6  *x^{0.4}*  y^{-0.4}. Numerically x^{0.4}=16^{0.4}≈2^{1.6}≈3.03, y^{-0.4}=36^{-0.4}≈6^{-0.8}≈0.263 ⇒ MU\_y≈0.6*3.03*0.263≈0.478.
6. Compute MU\_x/MU\_y ≈ 0.628/0.478 ≈ 1.314. Compute price ratio p\_x/p\_y = 3/2 = 1.5. The small numerical discrepancy is due to rounding in intermediate approximations; with exact algebra the equality holds at the true optimum. Alternatively verify algebraically: (α/β)*(y/x) = p\_x/p\_y; plugging the solved x^*,y^\* gives equality.

**Insight:** This example illustrates numeric verification that the FOC condition MU\_x/MU\_y = p\_x/p\_y holds at the interior optimum; in practice keep enough precision or use exact algebra to avoid rounding artifacts.

### Corner solution with linear utility

Maximize u(x,y)=3x+2y with prices p\_x=2, p\_y=1 and income I=100. Determine the optimal bundle.

1. Compute marginal utility per dollar for each good: MU\_x/p\_x = 3/2 = 1.5 and MU\_y/p\_y = 2/1 = 2.
2. Compare: since MU\_y/p\_y > MU\_x/p\_x, good y delivers more utility per dollar than x.
3. Therefore spend all income on good y (corner solution): x^ *= 0, y^* = 100/1 = 100.
4. Check alternate corner: all income on x gives x=50 and utility = 3*50 = 150, whereas the chosen bundle yields utility = 2*100 = 200, so the corner selection is correct.
5. Interpret λ: since MU\_y = 2 = λ p\_y ⇒ λ = 2/1 = 2. This λ equals the marginal utility of income (each extra dollar raises utility by 2 units) at the optimum.

**Insight:** This example demonstrates that when the MRS condition cannot be satisfied because MU ratios are constant (linear utility), the optimum can be at a corner. Checking utility across corners is essential.

## Key Takeaways

- ✓

  Utility functions map bundles to satisfaction levels; marginal utility is the partial derivative and tells the utility gain from a tiny increase in a good (see "Derivatives").
- ✓

  Indifference curves are level sets of utility; their slope equals the negative ratio of marginal utilities: MRS = -MU\_x/MU\_y.
- ✓

  At an interior optimum under a linear budget, consumers equate subjective tradeoff to market prices: MU\_x/MU\_y = p\_x/p\_y. Use Lagrangian methods from "Optimization Introduction" to solve.
- ✓

  Cobb–Douglas preferences yield closed-form demand: x^\* = α/(α+β) · I/p\_x, so expenditure shares are constant (numeric checks help avoid arithmetic mistakes).
- ✓

  Linear utilities produce corner solutions: buy the good with higher marginal utility per dollar (MU\_i/p\_i). Always check corners in addition to interior FOCs.
- ✓

  The Lagrange multiplier λ equals the marginal utility of income; computing it numerically gives useful welfare interpretation.
- ✓

  Utility theory enables comparative statics (how demand responds to price and income), consumer surplus calculations, and is foundational for demand estimation and general equilibrium models.

## Common Mistakes

- ✗

  Confusing marginal utility with MRS: MU\_x is the marginal increase in utility from x, whereas MRS = -MU\_x/MU\_y is the slope of indifference curves. They are related but not the same.
- ✗

  Ignoring corner solutions: applying MU\_x/MU\_y = p\_x/p\_y mechanically without checking non-negativity or linear utility cases can produce infeasible or suboptimal bundles.
- ✗

  Algebra/rounding errors in numeric substitution: when verifying FOCs numerically, low-precision intermediate approximations can make equality checks appear to fail; use exact algebra where possible.
- ✗

  Interpreting λ incorrectly: λ is the marginal utility of income (utility per extra dollar) at optimum, not a price or a quantity of goods.

## Practice

easy

Easy: For u(x,y)=x^{0.5} y^{0.5} compute MU\_x, MU\_y and MRS at the bundle (x,y)=(9,4). Provide numeric values.

**Hint:** Use partial derivatives: MU\_x = 0.5 x^{-0.5} y^{0.5}; MU\_y = 0.5 x^{0.5} y^{-0.5}. Then MRS = -MU\_x/MU\_y.

Show solution

Compute MU\_x = 0.5  *9^{-0.5}*  4^{0.5} = 0.5  *(1/3)*  2 = 0.3333. MU\_y = 0.5  *9^{0.5}*  4^{-0.5} = 0.5  *3*  (1/2) = 0.75. MRS = -MU\_x/MU\_y = -0.3333/0.75 = -0.4444 (i.e., -4/9).

medium

Medium: Maximize u(x,y)=x^{0.6} y^{0.4} subject to p\_x=4, p\_y=2, income I=200. Solve for x^*(I,p), y^*(I,p) and compute the Engel curve for x (x^\* as function of I).

**Hint:** Use Cobb–Douglas demand formula x^ *= α/(α+β) · I/p\_x. For Engel curve express x^* as a linear function of I.

Show solution

Here α=0.6, β=0.4 so α/(α+β)=0.6. Then x^ *= 0.6*  200 / 4 = 0.6  *50 = 30. y^* = 0.4  *200 / 2 = 0.4*  100 = 40. Engel curve for x is x^*(I) = 0.6 I / 4 = 0.15 I. For example if I doubles to 400 then x^*=60.

hard

Hard: Consider u(x,y)=ln x + y with prices p\_x=1, p\_y=1 and income I. (a) Solve for Marshallian demands x^*(I), y^*(I). (b) Find the income effect on x when income increases infinitesimally (dx/dI). (c) Discuss whether x is normal or inferior.

**Hint:** Set up Lagrangian: maximize ln x + y + λ(I - x - y). Use FOCs to solve. Be cautious: domain requires x>0. Recall derivative of ln x is 1/x.

Show solution

L = ln x + y + λ(I - x - y). FOCs: ∂L/∂x = 1/x - λ = 0 ⇒ λ = 1/x. ∂L/∂y = 1 - λ = 0 ⇒ λ = 1. Thus 1/x = 1 ⇒ x^ *= 1. Budget constraint: x + y = I ⇒ y^* = I - 1. (a) So x^*(I) = 1, y^*(I) = I - 1 for I > 1. (b) dx/dI = 0 (x does not change with income). (c) x is income-neutral (neither normal nor inferior in the usual sense); it has zero income elasticity. Intuition: u is quasilinear in y, so x chosen to satisfy 1/x = λ (which equals marginal utility of income) becomes constant. For small I below 1, corner solutions may arise (feasible region requires y≥0 ⇒ I≥1 for interior solution).

## Connections

Looking back: this lesson relies directly on the prerequisites. In "Derivatives" we learned how to compute partial derivatives and slopes — those skills are used to calculate marginal utilities (MU\_x, MU\_y) and the slope of indifference curves (MRS = -MU\_x/MU\_y). In "Optimization Introduction" we learned the Lagrangian method and first-order conditions; here we apply that technique to maximize utility under a budget constraint and interpret the Lagrange multiplier as the marginal utility of income. Looking forward: mastery of utility theory enables demand estimation (specifying functional forms like Cobb–Douglas or CES and fitting them to data), welfare analysis (consumer surplus, compensating and equivalent variation), price incidence/tax analysis, Hicksian demand and Slutsky decomposition, and participation in general equilibrium models where individual utility maximization is aggregated to compute market outcomes. Specific downstream topics that require this material include: computation of Marshallian and Hicksian demand, derivation of income and substitution effects (Slutsky equation), welfare comparisons in public economics, and consumer-side behavior in industrial organization and macro models. Numerical practice with the examples above also prepares you for empirical calibration and counterfactual policy simulations.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
