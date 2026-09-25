# Investing — Coverage & Depth Audit

`as_of_date: 2026-09-25`

Audit này đánh giá `investing/` ở cấp toàn library. Mục tiêu không phải đếm chapter mà xác định **domain nào đã có canonical depth, capability nào còn thiếu, phần nào time-sensitive, và khi nào không nên tạo thêm theory file**.

## Kết luận hiện tại

Investing hiện đã đạt **core breadth + advanced application depth** trên toàn bộ learning route:

```text
01 Foundations
→ 02 Asset Classes
→ 03 Company Analysis
→ 04 Applied Economics / Macro
→ 05 Trading & Derivatives
→ 06 Korea / Vietnam Markets
→ 07 Integrated Case Studies
```

Mỗi domain `01–06` đều có core chapters và ít nhất một advanced lab/application layer. `07` đã có cross-domain cases và full-process capstone. Forex hiện có thêm dedicated route `01–15`, institutional connections, labs và historical stress cases.

Vì vậy **next priority không phải thêm chapter lý thuyết theo chiều ngang**. Chỉ mở rộng khi tạo thêm một capability thực: point-in-time implementation, empirical case, data pipeline, quantitative lab, jurisdiction refresh hoặc cross-domain decision artifact.

## 1. Coverage matrix

| Domain | Core mechanism | Data / measurement | Risk / failure modes | Practice / case | Trạng thái |
|---|---|---|---|---|---|
| 01 Foundations | money/financial system, allocation, lifecycle, behavior | portfolio analytics, performance, fees/tax | drawdown, covariance, liquidity, behavior, stress | advanced portfolio design lab | **Strong** |
| 02 Asset Classes | stocks/funds, bonds/credit, real assets, factors, cash/private markets | yield curve, spreads, NAV, carry/roll, currency | duration, credit, liquidity, embedded options, private-mark valuation | asset-pricing/portfolio lab | **Strong** |
| 03 Company Analysis | accounting → business quality → valuation → capital allocation | filings, working capital, unit economics, sector KPIs | earnings quality, leverage, governance, dilution, cyclicality | integrated company modeling lab | **Strong** |
| 04 Applied Economics | macro data → policy → rates/liquidity/FX → assets | surprise/revisions, yield curve, credit/funding, nowcast | regime error, policy expectation, liquidity-v-solvency, crisis transmission | macro transmission/nowcasting lab | **Strong, keep boundary with Economics** |
| 05 Trading & Derivatives | payoff, leverage, margin, execution, strategy research, options | point-in-time data, transaction costs, TCA, volatility | look-ahead, overfit, liquidity, collateral, jump/margin risk | system lab + Forex labs/cases | **Strong** |
| 06 Korea / Vietnam | country balance sheet → policy → market access → sector/company | official macro/market/access sources | FX, custody, ownership, tax, liquidity, regulation | Korea/Vietnam thesis lab | **Strong but time-sensitive** |
| 07 Integrated Cases | multi-domain transmission and decision process | case-specific data/model inputs | cross-layer feedback, portfolio loss, invalidation | seven integrated cases + capstone | **Strong integration layer** |

## 2. Domain audit

### 01 — Foundations

Canonical chapters already cover:

```text
money / financial system
portfolio construction
lifecycle allocation
risk measurement
performance attribution
fees / tax / behavior
advanced stress / decision lab
```

This is not a candidate for more introductory portfolio theory. New content is justified only if it adds a missing operational capability such as liability-aware implementation, tax/account wrapper specificity, or a materially new risk framework.

### 02 — Asset Classes

Coverage already includes:

```text
stocks / ETF / funds
bonds / rates / credit
real assets / alternatives
factors / indexing
multi-asset hedging / currency / regime allocation
cash / money markets / structured / private markets
asset-pricing and term-structure lab
```

Do not split every instrument into its own file unless legal payoff, liquidity, valuation or portfolio behavior is genuinely different.

### 03 — Company Analysis

Coverage already forms a complete company-analysis chain:

```text
financial statements
→ business quality / industry
→ DCF / multiples
→ earnings quality / forensics
→ sector-specific drivers
→ governance / capital allocation / M&A
→ integrated model / thesis lab
```

Highest-value future additions are **worked company cases with auditable inputs**, not another generic valuation chapter.

### 04 — Applied Economics / Macro

This layer owns investment application rather than general-purpose economic theory.

Current route covers:

```text
company ↔ macro bridge
macro/global capital flows
macro data playbook
money/liquidity/crisis transmission
historical regimes/crises
fiscal–monetary interaction / debt / demographics / productivity
nowcasting and policy lab
```

General theory and econometric identification belong to [`../economics/`](../economics/README.md). Investing should continue to own **pricing, liquidity, portfolio and company transmission**.

### 05 — Trading & Derivatives

General coverage is already deep in:

```text
contract/payoff mechanics
systematic research
execution / microstructure
strategy robustness
options / volatility
production controls
```

Forex is now a specialization inside this domain rather than a missing topic.

#### Forex specialization

Canonical core remains `05_trading_derivatives/forex/01–15`.

Additional layers:

```text
90_connections/
→ NDF / forward points / FX swaps / cross-currency basis / funding
→ intervention / reserves / exchange-rate regimes / REER / valuation

90_labs/
→ mechanics / event study / point-in-time backtest / portfolio FX risk / regulatory verification

80_case_studies/
→ ERM 1992 / Asian crisis 1997 / CHF 2015 / USD funding stress 2020
```

Do not add indicator, candlestick or “best strategy” encyclopedias. New Forex content needs a new mechanism, dataset, institutional constraint or implementation artifact.

### 06 — Korea / Vietnam Markets

Coverage already includes:

```text
Korea playbook
Vietnam playbook
cross-market shocks
research/data workflow
cross-border investing / FX / tax / custody / access
sector deep dives
country thesis/scenario lab
```

The main risk here is **staleness**, not missing theory. Regulation, settlement, foreign ownership, tax, index classification, market access, central-bank rules and official market structure must be date-stamped and rechecked before practical use.

### 07 — Integrated Case Studies

The case layer now spans:

```text
inflation shock
credit/liquidity crisis
Korea semiconductor cycle
Vietnam property-bank-credit cycle
full investment process capstone
macro-rates-liquidity-company-valuation-portfolio chain
USD funding / FX / Korea-Vietnam cross-border transmission
```

New cases are justified only when they stress a mechanism not already represented. Avoid collecting famous episodes merely for historical breadth.

## 3. Evidence and research contract

Investing should distinguish at least:

```text
Fact
Accounting / pricing identity
Estimate
Model assumption
Empirical relationship
Causal mechanism
Market interpretation
Trading / investment hypothesis
Decision rule
Live evidence
```

Do not let one category silently become another.

Examples:

```text
Current account identity ≠ FX prediction
Forward price ≠ pure future-spot forecast
Backtest ≠ live edge
High ROIC ≠ permanent moat
Low volatility ≠ low tail risk
Cheap valuation ≠ entry timing
Policy commitment ≠ physical guarantee
```

## 4. Point-in-time discipline

The following must preserve observation/publication/effective dates where relevant:

```text
macro releases and revisions
consensus expectations
policy decisions
financial filings
index constituents
market-access rules
tax / settlement / ownership rules
broker/intermediary conditions
FX regulation
reserve/intervention data
```

Backtests and historical cases must not use knowledge unavailable at the decision date unless explicitly labeled retrospective analysis.

## 5. Boundary map

### Economics

[`../economics/`](../economics/README.md) owns general micro/macro/econometrics/economic-history theory.

Investing owns:

```text
market pricing
asset/company transmission
liquidity/funding application
portfolio consequence
hedging/execution
decision artifacts
```

### Korea Business & Economy

[`../korea_business_economy_knowledge_library/`](../korea_business_economy_knowledge_library/README.md) owns Korean corporate/institution/economy knowledge. Investing owns securities/portfolio/valuation/access application.

### Mathematics / Research Methods

Use canonical probability/statistics/research-design material rather than creating isolated statistical mini-textbooks inside trading chapters.

### Data Engineering / Computer Science

If a future systematic project needs ingestion, versioning, data lineage, backtest engine or production monitoring, cross-link those domains rather than turning Investing into a software-engineering library.

## 6. Time-sensitive refresh gates

Highest refresh priority:

1. Korea/Vietnam market access, foreign-room, tax, settlement and regulation.
2. Forex chapter `15` and any current broker/intermediary/legal-entity claims.
3. Current market-size/turnover statistics and index methodology.
4. Macro data sources when statistical methodology changes.
5. Product conventions when benchmark, clearing or settlement standards materially change.

Historical mechanism chapters generally need slower review unless interpretation or source quality changes.

## 7. What should not be added next

Do not prioritize:

- more generic investing definitions;
- indicator/candlestick catalogs;
- lists of famous investors or slogans;
- one file per ETF/product without a new mechanism;
- generic macro theory duplicated from Economics;
- country/company profiles that contain only current facts without an analytical model;
- “best stock / best strategy / best broker” static lists.

These increase maintenance burden faster than learning depth.

## 8. Highest-value future expansions

Only after a concrete use case appears, the strongest candidates are:

### A. Systematic implementation project

```text
point-in-time data contract
→ data lineage/versioning
→ signal engine
→ cost/fill model
→ portfolio aggregation
→ walk-forward/OOS
→ production monitoring
→ attribution/post-mortem
```

### B. Institutional hedging worked cases

Examples:

```text
exporter/importer FX hedge
foreign-asset hedge ratio
bond duration + FX hedge
rolling-forward cost/basis risk
corporate refinancing + currency mismatch
```

### C. Quantitative options lab

Add only if options become an explicit learning target:

```text
vol surface conventions
Greek P/L decomposition
delta-hedged P/L
event IV vs realized
skew/risk-reversal scenarios
```

### D. Point-in-time company case

Use dated filings/consensus/market data to produce:

```text
model
→ valuation range
→ thesis
→ position sizing
→ later attribution
```

This adds more depth than another generic DCF explanation.

## 9. Completion gate

Investing core should be treated as **coverage-complete but continuously refreshable** when the learner can produce these artifacts:

```text
IPS + portfolio stress/rebalancing rules
asset-class comparison / regime map
integrated company model + valuation + invalidation
macro surprise / transmission map
cost-aware OOS strategy report + execution/risk controls
Korea/Vietnam market thesis with access constraints
cross-domain case / capstone with attribution and post-mortem
```

The library is not “finished forever”. Completion means every major learning capability has a canonical owner and a path from concept to application. New files must make one of those capabilities materially deeper.
