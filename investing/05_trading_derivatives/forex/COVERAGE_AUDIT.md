# Forex Coverage Audit

`as_of_date: 2026-09-25`

File này kiểm tra coverage của nhánh `investing/05_trading_derivatives/forex/` để tránh hai lỗi ngược nhau: thiếu nền tảng quan trọng hoặc tiếp tục tạo chapter mới chỉ để lặp lại nội dung đã có.

Canonical route vẫn là `01–15`. Các file trong `90_connections/` là bridge nâng cao để nối Forex với funding, open-economy macro và institutional market plumbing; chúng **không mở thêm linear chapter 16/17**. Practice vẫn nằm ở `90_labs/`.

## 1. Coverage map

| Area | Canonical chapter | Depth status | Practice |
|---|---|---|---|
| FX market structure, OTC, spot/forward/swap/futures/options | `01_MARKET_STRUCTURE_AND_INSTRUMENTS.md` | Deep foundation | Lab 04 context comparison |
| Quote, base/quote, pip, lot, cross-rate, P/L | `02_QUOTES_PIPS_LOTS_AND_PNL.md` | Deep foundation | Lab 00 |
| Leverage, margin, sizing, portfolio heat | `03_LEVERAGE_MARGIN_POSITION_SIZING.md` | Deep foundation | Lab 00, Lab 03 |
| Rates, central banks, carry, BOP, flows, sessions | `04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md` | Deep foundation | Lab 01, Lab 04 |
| Orders, broker/dealer, spread, slippage, financing, operational risk | `05_EXECUTION_BROKERS_COSTS_AND_RISK.md` | Deep foundation | Lab 01, Lab 02 |
| Trend/range/volatility, support/resistance, breakout/pullback, SMC/ICT framing | `06_PRICE_ACTION_TREND_RANGE_AND_VOLATILITY_REGIMES.md` | Deep | Lab 02 |
| MA/EMA, RSI, MACD, ATR, Bollinger, indicator normalization | `07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md` | Deep | Lab 02 |
| Macro-event research, expectations, surprise, transmission | `08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md` | Deep | Lab 01 |
| Carry, momentum, value, macro strategy families | `09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md` | Deep | Lab 02 |
| Point-in-time data, bias, cost, robustness, walk-forward | `10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md` | Deep | Lab 02 |
| Currency-factor aggregation, correlation, stress, hedging | `11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md` | Deep | Lab 03 |
| Journal, attribution, MAE/MFE, process review | `12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md` | Deep | integrated across labs |
| Dealer flow, liquidity, venue fragmentation, order flow | `13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md` | Advanced | partial via Labs 01/03 |
| FX options, IV, skew, Greeks, hedging | `14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md` | Advanced bridge | exercise extension needed only if options becomes a separate learning target |
| Korea/Vietnam FX context and current regulation | `15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md` | Context-specific deep | Lab 04 |
| Forward points, CIP, FX swaps, NDF, basis, funding, onshore/offshore segmentation | `90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md` | Advanced institutional bridge | future case/lab only if point-in-time funding data are available |
| Intervention, reserves, exchange-rate regimes, PPP/REER, valuation uncertainty | `90_connections/01_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md` | Advanced macro-policy bridge | future regime/intervention case study if needed |

## 2. What is intentionally not duplicated

Các nội dung sau đã có canonical depth ở phần khác của `investing/` và Forex chỉ cross-link:

```text
General derivatives mechanics
→ ../01_DERIVATIVES_FUTURES_OPTIONS_CFD.md

Systematic research methodology
→ ../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md

Execution and market microstructure
→ ../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md

Strategy robustness / portfolio of strategies
→ ../04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md

Advanced options / volatility surface / Greeks
→ ../05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md

Trading system production controls
→ ../06_TRADING_SYSTEM_DESIGN_RISK_AND_EXECUTION_LAB.md
```

General open-economy macro theory, monetary policy, exchange-rate crises và econometric identification vẫn thuộc [`../../../../economics/`](../../../../economics/README.md). `90_connections/` chỉ giữ **FX-specific implementation and interpretation**: forward/NDF/basis/funding plumbing và cách reserves/intervention/REER đi vào currency analysis.

Không tạo lại các chapter Forex có cùng nội dung chỉ đổi ví dụ từ stock/futures sang EUR/USD nếu không có FX-specific mechanics mới.

## 3. Institutional connection coverage

Institutional bridge hiện bao phủ hai lớp trước đây chỉ xuất hiện rải rác trong core chapters.

### Funding / forward / NDF layer

`90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md` nối:

```text
spot
→ relative rates
→ forward points
→ FX swap
→ cross-currency basis
→ collateral / dealer balance sheet
→ NDF / fixing
→ onshore-offshore segmentation
```

Depth gate là phân biệt **directional FX view** với **hedging/funding flow**, và hiểu rằng capital-control wedge hoặc basis deviation không tự động là exploitable arbitrage.

### Policy / valuation layer

`90_connections/01_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md` nối:

```text
PPP / REER
→ external balance / NIIP
→ reserves
→ intervention
→ exchange-rate regime
→ valuation model
→ catalyst / invalidation
```

Depth gate là hiểu **valuation ≠ timing**, **reserve change ≠ intervention amount**, và **intervention ≠ guaranteed reversal**.

## 4. Practice coverage

Practice layer hiện có:

```text
Lab 00 — mechanics, P/L, margin, position sizing
Lab 01 — macro event analysis without hindsight
Lab 02 — point-in-time backtest and robustness
Lab 03 — portfolio FX factor risk
Lab 04 — Korea/Vietnam context and regulatory verification
```

Các lab được thiết kế để tạo artifact reviewable thay vì quiz ghi nhớ.

Institutional connections chưa cần lab riêng chỉ để đủ số lượng. Chỉ tạo lab/case khi có data phù hợp để kiểm tra fixing, forward curve, basis, reserves hoặc intervention theo point-in-time convention.

## 5. Remaining optional extensions

Các phần dưới đây **không phải gap nền tảng**. Chỉ mở rộng nếu có mục tiêu học cụ thể:

### A. FX options quantitative lab

Có thể thêm khi cần thực hành:

```text
Delta / Gamma / Vega P&L decomposition
Risk reversal / butterfly quote conventions
Volatility surface interpolation
Delta-hedged option P/L
Event implied-vs-realized volatility
```

### B. Systematic FX coding project

Có thể thêm khi cần implementation bằng code:

```text
point-in-time data pipeline
session/DST normalization
transaction-cost model
walk-forward engine
portfolio exposure aggregator
research notebook → production spec
```

Đây nên nằm ở bridge giữa Forex và Computer Science/Data Engineering thay vì biến toàn bộ Forex library thành coding tutorial.

### C. Historical FX crisis / regime case studies

Có thể thêm một folder case studies nếu muốn học sâu history/regime:

```text
1992 ERM crisis
1997 Asian Financial Crisis
2015 CHF floor removal
2020 USD funding stress
2022 JPY / global rate divergence
selected KRW/VND stress episodes
```

Case study phải tập trung vào mechanism, funding, market structure, policy constraint và liquidity; không chỉ kể diễn biến giá.

### D. Institutional hedging case studies

Có thể mở rộng bằng application artifacts:

```text
exporter hedge
importer hedge
foreign-asset manager hedge
rolling forward hedge
hedge-ratio / basis-risk analysis
```

Cross-currency funding theory không còn là gap; bridge `90_connections/00` đã sở hữu phần đó. Case mới chỉ nên thêm khi có concrete balance-sheet/data example.

## 6. Quality risks to monitor

Khi update về sau, kiểm tra các lỗi sau:

```text
Indicator explanation turns into trading signal promise
SMC/ICT terminology presented as proven mechanism without test
Current market statistics treated as timeless facts
US retail-forex regulation copied to Korea/Vietnam
Broker marketing terminology treated as standardized legal category
Backtest ignores bid/ask, financing or timestamp availability
Pair-level risk treated as independent portfolio risk
FX options content duplicates parent options chapter
Forward price presented as pure future-spot forecast
Basis / NDF wedge presented as risk-free arbitrage without access constraints
Reserve change presented as direct intervention amount
REER/PPP valuation presented as entry timing signal
```

## 7. Review cadence

Các chapter mechanics có thể review chậm hơn. Các phần sau phải review khi regulation/market convention thay đổi:

```text
01 market structure where current statistics are cited
05 broker/regulatory execution context
15 Korea/Vietnam FX market context and regulations
90_connections/00 when benchmark/funding/market conventions materially change
90_connections/01 when regime/intervention methodology or source conventions change
```

Chapter `15` phải giữ `as_of_date` hoặc nguồn có ngày rõ ràng cho rule hiện hành.

## 8. Current conclusion

Nhánh Forex đã đạt coverage từ **beginner mechanics → macro/strategy research → portfolio/microstructure/options → jurisdiction context → institutional funding/policy connections**, đồng thời đã có practice layer đủ để kiểm tra hiểu biết.

Canonical linear route vẫn dừng ở `01–15`. `90_connections/` tăng institutional depth mà không biến library thành chuỗi `16, 17, 18...`; `90_labs/` giữ practice. Bước tiếp theo không nên là tạo thêm theory chapter chỉ để tăng số lượng.

Ưu tiên tiếp theo, nếu cần, là **historical regime/funding case study, implementation project hoặc quantitative options lab** — chỉ khi chúng tạo evidence/practice mới thay vì duplicate theory.
