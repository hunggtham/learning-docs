# Forex — Coverage Audit

## Kết luận hiện tại

Forex hiện có canonical learning path đủ sâu từ retail/instrument mechanics tới institutional FX. Path không được coi là “hoàn thành” chỉ vì có nhiều chapter; completion gate là người học phải nối được **instrument → funding → macro → execution → data → strategy → portfolio → jurisdiction** mà không biến chart pattern hoặc macro headline thành causal rule.

Sau institutional depth pass mới nhất, hai khoảng trống quan trọng trước đây đã được lấp:

- `16` nối NDF, forward points, FX swaps, cross-currency basis, funding và capital-control wedges;
- `17` nối intervention, reserves, exchange-rate regime, REER/PPP và currency valuation.

## Canonical route

```text
01 Market Structure & Instruments
02 Quotes, Pips, Lots & P/L
03 Leverage, Margin & Position Sizing
04 Macro Drivers, Rates, Carry & Sessions
05 Execution, Brokers, Costs & Risk
06 Price Action, Trend, Range & Volatility Regimes
07 Technical Indicators as Data Transformations
08 Fundamental & Event-Driven FX Analysis
09 Carry, Momentum, Value & Macro FX Strategies
10 Backtesting & Point-in-Time FX Data
11 Portfolio FX Risk, Correlation & Factor Exposure
12 Trading Journal, Review & Performance Attribution
13 Advanced FX Microstructure & Order Flow
14 FX Options, Volatility & Hedging
15 Korea / Vietnam FX Market Context & Regulations
16 NDF, Forward Points, Basis & Funding
17 Intervention, Reserves, REER & Currency Valuation
```

## Coverage matrix

| Layer | Trạng thái | Nội dung đã có | Next-depth nếu cần |
|---|---|---|---|
| Market mechanics | Strong | OTC structure, spot/forward/swap/futures/options/CFD, settlement, counterparty, CLS, quotes/pips/lots | prime brokerage/credit lines nếu cần institutional specialization |
| Risk & leverage | Strong | notional vs margin vs amount-at-risk, liquidation, position sizing, portfolio heat | margin optimization across venues |
| Macro | Strong | rates, reaction functions, yields, carry, BOP/capital flows, terms of trade, sessions | cross-asset macro factor estimation |
| Execution | Strong | spread/slippage/rollover, broker due diligence, order types, TCA, operational risk | algorithmic execution benchmark design |
| Technical analysis | Strong boundary | price action as description; indicators as transformations; formalization/backtest requirement | no need to add indicator encyclopedia |
| Strategy research | Strong | carry/momentum/value/event/mean reversion, point-in-time data, OOS/walk-forward, multiple testing | advanced statistical learning only if research use-case exists |
| Portfolio | Strong | currency-factor decomposition, covariance/stress correlation, VaR/ES, attribution | dynamic hedging optimization |
| Microstructure | Strong | fragmentation, inventory, adverse selection, last look, order flow, fixing, markout | venue-specific empirical data if available |
| Options | Strong bridge | vol/skew/smile, Greeks, event vol, hedging | advanced FX option conventions/exotics only if needed |
| Korea/Vietnam | Current + time-sensitive | onshore/offshore context, access/regulatory boundaries, corporate exposure | recurring regulatory refresh, not static expansion |
| Funding/NDF | **Strong after depth pass** | forward points, CIP, basis, FX swaps, NDF fixing, onshore/offshore wedges, collateral/funding | empirical basis/NDF case study if point-in-time data available |
| Valuation/policy | **Strong after depth pass** | REER/PPP, NIIP, reserves, intervention, regimes, BEER/FEER intuition | historical intervention case studies with source/version control |

## Depth gates

### Gate 1 — Product identity

Before any strategy, learner must distinguish:

```text
deliverable spot
forward
FX swap
NDF
futures
options
retail rolling FX / CFD
```

Ticker similarity does not imply same legal/economic product.

### Gate 2 — P/L and funding

Must be able to decompose:

```text
spot movement
+ forward/carry/financing
+ spread/commission/slippage
+ hedge/basis effects
= realized economics
```

### Gate 3 — Risk

Must separate:

```text
notional exposure
margin requirement
loss-at-risk
portfolio factor exposure
```

Leverage is a balance-sheet multiplier, not an edge.

### Gate 4 — Macro evidence

Must avoid rules such as:

```text
rate hike → currency up
trade surplus → currency up
high yield → free carry
intervention → guaranteed reversal
cheap REER → buy now
```

Every macro claim needs expectations, relative side, regime, risk premium and positioning context.

### Gate 5 — Research integrity

Backtest must state:

```text
point-in-time inputs
signal timestamp
execution timestamp
bid/ask/cost model
financing
margin
sample selection
model-selection process
OOS validation
reproducibility
```

### Gate 6 — Institutional plumbing

Advanced learner must understand:

```text
CIP
forward points
FX swaps
cross-currency basis
NDF fixing
settlement risk / CLS
collateral / dealer balance sheet
reserves / intervention
onshore-offshore segmentation
```

### Gate 7 — Jurisdiction

Access, product classification and investor protection are jurisdiction-specific. Chapter `15` is time-sensitive and must be rechecked before practical decisions.

## Anti-duplication contract

Forex stays a child of Investing.

- [`../../../../economics/`](../../../../economics/README.md) owns general macroeconomic theory and econometrics.
- [`../`](../README.md) owns general derivatives/options/systematic trading and execution concepts shared across asset classes.
- Forex owns currency-specific market structure, funding, strategy implementation, microstructure and jurisdiction context.
- [`../../06_markets_korea_vietnam/`](../../06_markets_korea_vietnam/README.md) owns broader Korea/Vietnam investing and market-access application.

Cross-link instead of copying entire macro/options chapters.

## Evidence contract

Forex content should distinguish:

```text
Accounting / pricing identity
Empirical tendency
Causal mechanism
Trading hypothesis
Backtest evidence
Live execution evidence
Regulatory fact
```

A pricing identity is not a profit guarantee. A historical factor return is not a future edge. A backtest is not live evidence. A broker's product page is not regulatory authority.

## Time-sensitive content

The most time-sensitive chapter is `15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md`.

Refresh triggers include:

- Korean FX-market access/hours/RFI changes;
- KOFIA/FSC/FSS rules for retail FX-margin/intermediaries;
- SBV foreign-exchange circular/decree changes;
- Vietnam IFC scope/rules;
- material market-structure changes affecting data/backtests.

Record source, publication/effective date and retrieval date.

## What should **not** be added next

Do not expand by creating:

- dozens of candlestick-pattern files;
- indicator-by-indicator chapters;
- “best strategy” lists;
- broker rankings without a current shopping/compliance need;
- deterministic macro trading rules;
- duplicated general options/economics theory.

These increase file count without increasing causal/market understanding.

## Next legitimate depth candidates

Only expand when a concrete learning need appears. Highest-value candidates are:

1. an empirical **FX funding/basis crisis case study** using documented point-in-time data;
2. an **intervention/regime-change case study** showing reserve, rates, spot/forward and policy timeline together;
3. an **end-to-end FX research lab** from hypothesis to data lineage, backtest, execution assumptions and live attribution;
4. advanced **FX option market conventions/exotics** only if options become a real study goal.

Until then, priority should be QA, cross-links, regulatory freshness and exercises rather than more theory chapters.
