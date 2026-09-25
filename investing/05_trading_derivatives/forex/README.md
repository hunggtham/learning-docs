# Forex — Foreign Exchange Learning Path

Forex (foreign exchange, **thị trường ngoại hối**, tiếng Hàn: **외환**) là một nhánh con của `05_trading_derivatives/`. Phần này không được tổ chức như một bộ mẹo giao dịch hay danh sách indicator. Mục tiêu là xây mental model hoàn chỉnh từ **market structure → quote/P&L → leverage/risk → macro → execution → price/regime → strategy research → portfolio → microstructure/options → context pháp lý Korea/Vietnam → institutional funding/policy connections → practice/review → historical stress regimes**.

Forex cần được học như giao điểm của nhiều lớp:

```text
Macroeconomics
+ Interest Rates
+ Cross-border Capital Flows
+ Market Microstructure
+ Derivatives
+ Leverage / Margin
+ Risk Management
+ Execution
+ Statistical Research
+ Jurisdiction / Regulation
+ Funding / Basis / Intervention / Valuation
```

Nếu chỉ biết đọc chart nhưng không hiểu các lớp này, người học có thể mô tả chuyển động giá nhưng khó giải thích vì sao exposure tồn tại, vì sao cùng một setup thay đổi theo regime, hoặc vì sao một chiến lược có vẻ tốt trên chart nhưng thất bại sau spread, financing, slippage và margin.

## Vị trí trong Investing library

```text
investing/
└── 05_trading_derivatives/
    ├── 00_MASTER_TRADING_FOREX_RISK.md
    ├── ...
    └── forex/
        ├── README.md
        ├── COVERAGE_AUDIT.md
        ├── 01_MARKET_STRUCTURE_AND_INSTRUMENTS.md
        ├── 02_QUOTES_PIPS_LOTS_AND_PNL.md
        ├── 03_LEVERAGE_MARGIN_POSITION_SIZING.md
        ├── 04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md
        ├── 05_EXECUTION_BROKERS_COSTS_AND_RISK.md
        ├── 06_PRICE_ACTION_TREND_RANGE_AND_VOLATILITY_REGIMES.md
        ├── 07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md
        ├── 08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md
        ├── 09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md
        ├── 10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md
        ├── 11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md
        ├── 12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md
        ├── 13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md
        ├── 14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md
        ├── 15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md
        ├── 80_case_studies/
        ├── 90_connections/
        └── 90_labs/
```

File `00_MASTER_TRADING_FOREX_RISK.md` ở thư mục cha vẫn là bản đồ tổng quan của Trading & Derivatives. Folder này đi sâu riêng vào Forex để tránh làm file master phình to và tránh duplicate nội dung options, derivatives hay systematic trading đã có ở nhánh cha.

# Phase A — Mechanics và survival

## 01 — Market structure and instruments

[01_MARKET_STRUCTURE_AND_INSTRUMENTS.md](./01_MARKET_STRUCTURE_AND_INSTRUMENTS.md)

Bắt đầu từ câu hỏi **“Forex market thực sự là thị trường nào?”** Phân biệt spot FX, retail OTC/rolling products, forward, FX swap, currency swap, futures và options; giải thích OTC, interdealer/dealer-client markets, liquidity provider, settlement và vì sao không có một global order book duy nhất.

## 02 — Quotes, pips, lots and P/L

[02_QUOTES_PIPS_LOTS_AND_PNL.md](./02_QUOTES_PIPS_LOTS_AND_PNL.md)

Đọc currency pair từ first principles: base/quote currency, bid/ask, spread, pip, contract size, lot, notional, cross rate, pip value và account-currency conversion. Mục tiêu là tự tính P/L thay vì phụ thuộc broker calculator.

## 03 — Leverage, margin and position sizing

[03_LEVERAGE_MARGIN_POSITION_SIZING.md](./03_LEVERAGE_MARGIN_POSITION_SIZING.md)

Tách ba khái niệm thường bị trộn:

```text
Notional Exposure
≠ Margin Requirement
≠ Amount at Risk
```

Đi sâu equity, used/free margin, margin level, liquidation/stop-out, portfolio heat, gap risk và sizing từ invalidation.

## 04 — Macro drivers, rates, carry and sessions

[04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)

Currency pair là relative price nên phải phân tích hai economies và hai expected rate paths. Chương nối central-bank reaction function, inflation, growth, real yields, carry, balance of payments, capital flows, sessions và positioning vào causal chain.

## 05 — Execution, brokers, costs and operational risk

[05_EXECUTION_BROKERS_COSTS_AND_RISK.md](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)

Giải thích pipeline từ signal tới actual fill: order types, spread, slippage, rollover, dealer/agency models, legal entity, broker due diligence, platform/API failures và transaction-cost analysis.

# Phase B — Chart và signal nhưng không thần bí hóa indicator

## 06 — Price action, trend, range and volatility regimes

[06_PRICE_ACTION_TREND_RANGE_AND_VOLATILITY_REGIMES.md](./06_PRICE_ACTION_TREND_RANGE_AND_VOLATILITY_REGIMES.md)

Price action được xử lý như **description trước prediction**. Trend, range, breakout, pullback, support/resistance, SMC/ICT vocabulary, candlestick và Fibonacci chỉ có giá trị nghiên cứu khi được formalize thành deterministic rule có invalidation và có thể backtest.

## 07 — Technical indicators as data transformations

[07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md](./07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md)

Giải thích SMA/EMA, momentum, RSI, MACD, stochastic, Bollinger, ATR, ADX, Donchian, z-score từ công thức và information content. Trọng tâm là nhận ra indicator phần lớn là transformations của cùng price data và tránh “nhiều indicator đồng thuận = nhiều bằng chứng độc lập”.

# Phase C — Fundamental và strategy research

## 08 — Fundamental and event-driven FX analysis

[08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md](./08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md)

Xây event analysis từ `consensus → actual → surprise → policy repricing → rates → FX`, dùng official central-bank/statistical sources, phân biệt first reaction/follow-through và xử lý revisions, vintage data, timestamp/DST.

## 09 — Carry, momentum, value and macro FX strategies

[09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md](./09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md)

Học strategy families thay vì các setup rời rạc: carry, time-series/cross-sectional momentum, value/PPP, macro directional, event, mean reversion, relative value và volatility. Mỗi family được nối với mechanism, return source, tail risk và portfolio construction.

## 10 — Backtesting and point-in-time FX data

[10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md](./10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)

Đây là lớp chống tự lừa mình: point-in-time/vintage data, bid/ask, bar conventions, fill model, financing, margin accounting, look-ahead, data snooping, walk-forward, purging/embargo, multiple testing, parameter surfaces, Monte Carlo và backtest-to-live gap.

# Phase D — Portfolio, review và institutional depth

## 11 — Portfolio FX risk, correlation and factor exposure

[11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md](./11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)

Tách ticket khỏi true exposure: currency decomposition, broad-USD/carry/rates/commodity factors, covariance, stress correlation, VaR/Expected Shortfall, volatility targeting, risk contribution, basis risk và portfolio heat.

## 12 — Trading journal, review and performance attribution

[12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md](./12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md)

Biến journal thành research database. Tách process khỏi outcome, R/MAE/MFE, signal P/L khỏi spread/slippage/financing, strategy/currency-factor attribution, rule violations, model drift và pre-defined pause/kill criteria.

## 13 — Advanced FX microstructure and order flow

[13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md](./13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md)

Đi vào dealer inventory, adverse selection, fragmentation, depth/resilience, internalization, last look, information leakage, order flow, stop clusters, futures proxy, latency, fixing flows, markout và TCA. Luôn ghi rõ rằng một venue/feed chỉ là subset của global FX.

## 14 — FX options, volatility and hedging

[14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md](./14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md)

Đưa Forex sang payoff phi tuyến: implied vs realized volatility, Delta/Gamma/Theta/Vega, skew/smile, risk reversals, event vol, gamma hedging, barriers, forward-vs-option hedge và option backtesting. Chapter này cross-link với options chuyên sâu ở thư mục cha thay vì duplicate toàn bộ.

# Phase E — Context Korea / Vietnam

## 15 — Korea / Vietnam FX market context and regulations

[15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md](./15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md)

Chapter time-sensitive được research lại từ nguồn chính thức. Korea: Seoul FX market reform, RFI, extended hours, USD/KRW, KOFIA FX-margin framework và intermediary requirements. Vietnam: SBV-authorized FX institutions, domestic FX framework, USD/VND regime, foreign-exchange controls, IFC-specific 2025 rules và Korea–Vietnam corporate exposures.

# Institutional connections — đọc sau core route khi cần institutional depth

[`90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md`](./90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md) nối spot với forward points, covered interest parity, FX swaps, cross-currency basis, dealer balance-sheet constraints, synthetic funding, NDF, fixing và onshore/offshore segmentation. Mục tiêu là phân biệt **directional FX** với **funding/hedging economics**.

[`90_connections/01_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md`](./90_connections/01_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md) nối PPP/REER, NIIP, reserves, sterilized/unsterilized intervention, exchange-rate regimes và valuation-model uncertainty. Mục tiêu là tránh dùng “currency cheap”, reserve headline hay intervention như automatic trading signals.

Hai connection files không mở thêm linear `16/17`; chúng là bridge vào institutional FX và cross-link Economics/Derivatives để giữ canonical route gọn.

# Phase F — Practice và review

Lý thuyết `01–15` cùng institutional connections được chuyển thành bài tập tại [90_labs/README.md](./90_labs/README.md):

```text
Lab 00 — quote / pip / P&L / margin / position sizing
Lab 01 — event-driven FX analysis without hindsight
Lab 02 — point-in-time backtest and robustness
Lab 03 — portfolio FX factor risk
Lab 04 — Korea/Vietnam FX context and regulatory verification
```

Các lab yêu cầu tạo artifact có thể review, không phải trả lời quiz ghi nhớ.

# Phase G — Historical stress regimes

[80_case_studies/README.md](./80_case_studies/README.md) dùng các regime cực đoan để stress-test mental model thay vì học lịch sử như timeline:

```text
1992 ERM / sterling
→ exchange-rate commitment vs domestic-policy constraint

1997 Asian Financial Crisis
→ currency mismatch + short-term foreign funding + banking feedback loop

2015 CHF floor removal
→ policy floor + liquidity discontinuity + stop/broker risk

2020 global USD funding stress
→ offshore dollar shortage + FX swaps/basis + central-bank swap lines
```

Sau khi đọc case, quay lại [COVERAGE_AUDIT.md](./COVERAGE_AUDIT.md) để phân biệt phần đã có theory/practice/case/connection depth với các extension thực sự còn thiếu.

# Milestone kiểm tra kiến thức

Sau Phase A, phải tự tính và giải thích được P/L, pip/lot/notional, margin, effective leverage, relative macro và all-in execution cost.

Sau Phase B, phải nhìn chart/indicator như dữ liệu có thể formalize, không coi pattern/indicator là nguyên nhân tự thân.

Sau Phase C, phải viết được hypothesis có mechanism, signal, point-in-time data, execution model, cost và out-of-sample validation.

Sau Phase D, phải tổng hợp risk theo currency/factor/strategy, biết attribution P/L và hiểu giới hạn của order-flow/volatility data.

Sau Phase E, phải biết rằng **product access và market structure phụ thuộc jurisdiction**; không suy từ broker marketing rằng một route hợp pháp hoặc có cùng investor protection ở Korea/Vietnam.

Sau institutional connections, phải phân biệt spot direction với forward/funding economics; hiểu NDF/onshore-offshore segmentation; đọc reserves/intervention/REER theo regime và model assumptions thay vì như single-variable signals.

Sau Phase F, phải có ít nhất một bộ output hoàn chỉnh từ `position-risk sheet → event study → backtest report → portfolio-risk dashboard → regulatory verification checklist`.

Sau Phase G, phải có thể giải thích vì sao **low historical volatility, policy commitment hoặc diversified-looking positions vẫn có thể che giấu jump/funding/factor risk**.

## Nguyên tắc an toàn nghiên cứu

Forex có thể sử dụng đòn bẩy lớn. Tài liệu phục vụ **học cơ chế, phân tích và quản trị rủi ro**, không đưa ra personalized buy/sell signals hay hứa hẹn lợi nhuận.

Đối với retail OTC/FX-margin products, broker/intermediary/legal entity là một phần của risk model. Regulatory details phải được re-check tại thời điểm sử dụng, đặc biệt chapter 15.

## Nguồn nền xuyên suốt

- Bank for International Settlements (BIS), 2025 Triennial Central Bank Survey và research về FX/funding markets.
- CFTC retail FX risk and registration guidance.
- IMF/BIS/central-bank materials cho exchange-rate regimes, reserves, intervention và effective exchange rates.
- Federal Reserve, ECB, Bank of Korea và các central banks/statistical agencies tương ứng.
- Korea Financial Investment Association (KOFIA) cho FX-margin investor guidance tại Korea.
- State Bank of Vietnam và official legal databases cho Vietnam FX rules.
- Historical case studies ưu tiên central-bank, IMF, BIS và official contemporary documentation.

Với số liệu hoặc quy định theo thời điểm, luôn ghi ngày/kỳ dữ liệu và source. Không biến một snapshot hoặc historical regime thành quy luật vĩnh viễn.
