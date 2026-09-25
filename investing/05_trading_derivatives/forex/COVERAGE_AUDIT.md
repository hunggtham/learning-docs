# Forex Coverage Audit

`as_of_date: 2026-09-25`

File này kiểm tra coverage của nhánh `investing/05_trading_derivatives/forex/` để tránh hai lỗi ngược nhau: thiếu nền tảng quan trọng hoặc tiếp tục tạo chapter mới chỉ để lặp lại nội dung đã có.

Canonical route vẫn là `01–15`. `60_institutional_hedging_cases/` giữ balance-sheet applications, `70_systematic_project/` giữ implementation bridge, `80_case_studies/` giữ historical stress regimes, `90_connections/` giữ institutional bridges và `90_labs/` giữ practice. Cách tổ chức này tăng depth mà không biến library thành chuỗi chapter tuyến tính chỉ để tăng số lượng.

## 1. Coverage map

| Area | Canonical chapter | Depth status | Practice / case / implementation depth |
|---|---|---|---|
| FX market structure, OTC, spot/forward/swap/futures/options | `01_MARKET_STRUCTURE_AND_INSTRUMENTS.md` | Deep foundation | Lab 04; ERM/CHF cases |
| Quote, base/quote, pip, lot, cross-rate, P/L | `02_QUOTES_PIPS_LOTS_AND_PNL.md` | Deep foundation | Lab 00; systematic execution ledger |
| Leverage, margin, sizing, portfolio heat | `03_LEVERAGE_MARGIN_POSITION_SIZING.md` | Deep foundation | Lab 00, Lab 03; CHF case; risk engine |
| Rates, central banks, carry, BOP, flows, sessions | `04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md` | Deep foundation | Lab 01, Lab 04; all historical cases |
| Orders, broker/dealer, spread, slippage, financing, operational risk | `05_EXECUTION_BROKERS_COSTS_AND_RISK.md` | Deep foundation | Lab 01, Lab 02; CHF case; execution/monitoring modules |
| Trend/range/volatility, support/resistance, breakout/pullback, SMC/ICT framing | `06_PRICE_ACTION_TREND_RANGE_AND_VOLATILITY_REGIMES.md` | Deep | Lab 02 |
| MA/EMA, RSI, MACD, ATR, Bollinger, indicator normalization | `07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md` | Deep | Lab 02; feature-pipeline semantics |
| Macro-event research, expectations, surprise, transmission | `08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md` | Deep | Lab 01; historical cases; point-in-time event data |
| Carry, momentum, value, macro strategy families | `09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md` | Deep | Lab 02; Asian-crisis/CHF tail-risk context |
| Point-in-time data, bias, cost, robustness, walk-forward | `10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md` | Deep | Lab 02; regime-break cases; full systematic project |
| Currency-factor aggregation, correlation, stress, hedging | `11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md` | Deep | Lab 03; institutional hedging cases; risk/attribution engine |
| Journal, attribution, MAE/MFE, process review | `12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md` | Deep | labs/cases; attribution/forward-test modules |
| Dealer flow, liquidity, venue fragmentation, order flow | `13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md` | Advanced | CHF/2020 cases; execution model |
| FX options, IV, skew, Greeks, hedging | `14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md` | Advanced bridge | exporter/importer option comparison; quantitative lab optional |
| Korea/Vietnam FX context and current regulation | `15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md` | Context-specific deep | Lab 04; exporter/importer/funding Korea context |
| Forward points, CIP, FX swaps, NDF, basis, funding, onshore/offshore segmentation | `90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md` | Advanced institutional bridge | 2020 USD-funding case; cross-currency funding case |
| Intervention, reserves, exchange-rate regimes, PPP/REER, valuation uncertainty | `90_connections/01_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md` | Advanced macro-policy bridge | ERM/Asian/CHF cases |
| Corporate/asset-manager transaction and funding hedging | `60_institutional_hedging_cases/` | Applied institutional depth | exporter, importer, asset manager, cross-currency funding |

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

`70_systematic_project/` chỉ giữ **FX-specific implementation semantics**: bid/ask, session/DST, macro vintage, rollover, account-currency conversion, margin, currency-factor aggregation, execution-aware backtest và live reconciliation. Generic software/database/cloud engineering vẫn thuộc domain computing tương ứng.

`60_institutional_hedging_cases/` không thay thế corporate-finance/accounting/legal documentation. Nó tập trung economic exposure, instrument payoff, carry/basis, collateral, timing/volume mismatch và combined hedge attribution.

Không tạo lại các chapter Forex có cùng nội dung chỉ đổi ví dụ từ stock/futures sang EUR/USD nếu không có FX-specific mechanics mới.

## 3. Institutional connection coverage

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

## 4. Institutional hedging coverage

Folder `60_institutional_hedging_cases/` đã chuyển institutional theory thành balance-sheet applications:

```text
01 Korean exporter
→ USD receivables, natural hedge, layered forwards, forecast/timing mismatch

02 Korean importer
→ USD payables, procurement margin, forward/options, roll and volume risk

03 Global asset manager
→ local-asset vs reporting-currency return, hedge ratio, roll/carry, benchmark and collateral

04 Cross-currency funding
→ debt currency transformation, CCS/FX swaps, basis, collateral, rollover and counterparty risk
```

Depth gate là đánh giá **underlying exposure + hedge + carry/funding + transaction cost + residual risk**, không đánh giá hedge instrument bằng standalone derivative P/L.

Các case cũng tách transaction exposure khỏi economic exposure và funding/liquidity risk; một forward đúng direction vẫn có thể fail operationally vì timing, volume, collateral hoặc counterparty mismatch.

## 5. Practice coverage

Practice layer hiện có:

```text
Lab 00 — mechanics, P/L, margin, position sizing
Lab 01 — macro event analysis without hindsight
Lab 02 — point-in-time backtest and robustness
Lab 03 — portfolio FX factor risk
Lab 04 — Korea/Vietnam context and regulatory verification
```

Các lab được thiết kế để tạo artifact reviewable thay vì quiz ghi nhớ.

Institutional connections/hedging cases chưa cần lab riêng chỉ để đủ số lượng. Chỉ tạo lab mới khi có data/payoff task cụ thể, ví dụ hedge roll attribution hoặc options-volatility calculation.

## 6. Historical case-study coverage

Folder `80_case_studies/` đã bổ sung depth theo regime/mechanism:

```text
1992 ERM / sterling
→ exchange-rate commitment vs domestic policy constraint

1997 Asian Financial Crisis
→ currency mismatch + short-term foreign funding + banking feedback loop

2015 CHF floor removal
→ policy floor + discontinuous liquidity + stop/broker risk

2020 global USD funding stress
→ offshore dollar shortage + FX swaps/basis + central-bank swap lines
```

Case studies không nhằm tạo historical pattern để trade. Chúng dùng để stress mental models của các chapter `01–15` và institutional connections dưới những regime cực đoan.

## 7. Systematic implementation coverage

Folder `70_systematic_project/` đã triển khai bridge từ research sang system có thể audit:

```text
01 Data pipeline & time normalization
→ point-in-time data, UTC/DST, instrument master, bid/ask, macro vintages, validation and lineage

02 Backtest engine & execution model
→ causal event loop, order state machine, fills, spread/slippage, financing, margin/account ledger

03 Portfolio risk & attribution engine
→ currency legs, factor exposure, stress/reverse stress, risk limits, hedge quality and P/L attribution

04 Forward test, monitoring & kill switch
→ paper/small-live progression, reconciliation, data/execution drift, operational controls, pause/retirement rules
```

Project intentionally stops at specification/architecture depth. Nó không duplicate generic programming tutorials; implementation language có thể là Python, Java, SQL hoặc stack khác nếu semantics vẫn giống nhau và reproducible.

## 8. Remaining optional extensions

Các phần dưới đây **không phải gap nền tảng**. Chỉ mở rộng nếu có mục tiêu học cụ thể.

### A. FX options quantitative lab

Đây hiện là extension có value cao nhất nếu muốn bổ sung quantitative derivatives practice:

```text
Delta / Gamma / Vega P&L decomposition
Risk reversal / butterfly quote conventions
Volatility surface interpolation
Delta-hedged option P/L
Event implied-vs-realized volatility
Barrier/event gap scenarios
```

### B. Additional historical/regime cases

Chỉ thêm nếu tạo mechanism mới chưa được bốn case hiện tại bao phủ. Candidate hợp lý:

```text
2022 JPY / global rate divergence and intervention
2008 Korea USD funding / FX stress
selected Vietnam FX-management stress episode
```

Không thêm chỉ vì một event nổi tiếng.

### C. Full executable codebase

Chỉ nên tạo nếu mục tiêu chuyển repository từ knowledge library sang project/code deliverable. Khi đó code cần đặt boundary rõ với `computer_science/`, `data_engineering/`, `sql/` và deployment domains thay vì để Forex documentation chứa một framework software độc lập.

### D. Accounting / legal implementation

Hedge accounting, documentation, tax, collateral documentation và legal enforceability chỉ nên được thêm nếu có scope riêng và sources/standards hiện hành. Không suy từ economic hedge case thành accounting/legal treatment.

## 9. Quality risks to monitor

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
Historical case is rewritten as deterministic trading pattern
Policy commitment is treated as physical guarantee
Forward price is presented as pure future-spot forecast
Basis / NDF wedge is presented as risk-free arbitrage without access constraints
Reserve change is presented as direct intervention amount
REER/PPP valuation is presented as entry timing signal
Systematic project drifts into generic software tutorial
Live/paper examples imply guaranteed profitability
Hedge is judged by derivative P/L instead of combined exposure
Forecast transaction is hedged as if amount/timing were certain
Cross-currency swap is presented as eliminating funding/collateral risk
```

## 10. Review cadence

Các chapter mechanics có thể review chậm hơn. Các phần sau phải review khi regulation/market convention thay đổi:

```text
01 market structure where current statistics are cited
05 broker/regulatory execution context
15 Korea/Vietnam FX market context and regulations
90_connections/00 when funding/benchmark/market conventions materially change
90_connections/01 when regime/intervention methodology or source conventions materially change
70_systematic_project when product/account/data semantics materially change
60_institutional_hedging_cases when market-access, product or collateral conventions are used as current facts
```

Chapter `15` phải giữ `as_of_date` hoặc nguồn có ngày rõ ràng cho rule hiện hành.

Historical cases không cần refresh vì chronology thay đổi, nhưng source links và interpretation nên được review nếu thêm research mới hoặc sửa mechanism.

Systematic-project specs cần review nếu margin, financing, broker execution, API semantics hoặc data-source convention thay đổi.

## 11. Current conclusion

Nhánh Forex hiện có bảy layer:

```text
Theory / mechanism        → chapters 01–15
Institutional hedging     → 60_institutional_hedging_cases/
Systematic implementation → 70_systematic_project/
Historical regime depth   → 80_case_studies/
Institutional bridges     → 90_connections/
Practice                  → 90_labs/
Coverage governance       → COVERAGE_AUDIT.md
```

Coverage đã đi từ **beginner mechanics → macro/strategy research → portfolio/microstructure/options → jurisdiction context → institutional funding/policy → corporate/asset-manager hedging → practical application → historical stress regimes → reproducible systematic implementation semantics**.

Bước tiếp theo không nên là tạo thêm linear theory hoặc generic coding tutorial. Extension rõ nhất còn thiếu là **FX-options quantitative lab**; sau đó chỉ nên mở rộng theo mục tiêu cụ thể như additional regime case hoặc accounting/legal implementation có source chuẩn.
