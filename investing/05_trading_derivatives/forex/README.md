# Forex — Foreign Exchange lộ trình học (learning path / 학습 경로)

Forex (foreign exchange, **thị trường ngoại hối**, tiếng Hàn: **외환**) là một nhánh con của `05_trading_derivatives/`. Phần này không được tổ chức như một bộ mẹo giao dịch hay danh sách indicator. Mục tiêu là xây mô hình tư duy (mental model / 사고 모델) hoàn chỉnh từ **thị trường (market / 시장) cấu trúc (structure / 구조) → quote/P&L → leverage/rủi ro (risk / 위험) → macro → thực thi (execution / 실행) → price/regime → chiến lược (strategy / 전략) research → portfolio → microstructure/options → ngữ cảnh (context / 맥락) pháp lý Korea/Vietnam → institutional funding/chính sách (policy / 정책) → corporate/institutional hedging → practice/rà soát (review / 검토) → historical stress regimes → systematic hiện thực (implementation / 구현)**.

> **Mạch đọc:** Đọc Forex theo chuỗi **thị trường (market / 시장) cấu trúc (structure / 구조) → rủi ro (risk / 위험)/macro → thực thi (execution / 실행)/research → institutional cases → historical stress → systematic hiện thực (implementation / 구현)**. Mỗi phase dùng bất biến (invariant / 불변식) của phase trước; vì vậy hãy quay lại chapter nền khi một trường hợp (case / 사례) hoặc lab dùng thuật ngữ mà chưa giải thích lại.

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
+ Corporate / Institutional Treasury
```

Nếu chỉ biết đọc chart nhưng không hiểu các lớp này, người học có thể mô tả chuyển động giá nhưng khó giải thích vì sao exposure tồn tại, vì sao cùng một setup thay đổi theo regime, hoặc vì sao một chiến lược có vẻ tốt trên chart nhưng thất bại sau spread, financing, slippage và margin.

## Vị trí trong Investing thư viện (library / 라이브러리)

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
        ├── 60_institutional_hedging_cases/
        ├── 70_systematic_project/
        ├── 80_case_studies/
        ├── 90_connections/
        └── 90_labs/
```

Tệp (file / 파일) `00_MASTER_TRADING_FOREX_RISK.md` ở thư mục cha vẫn là bản đồ tổng quan của Trading & Derivatives. Folder này đi sâu riêng vào Forex để tránh làm tệp (file / 파일) master phình to và tránh duplicate nội dung options, derivatives hay systematic trading đã có ở nhánh cha.

# Phase A — Mechanics và survival

## 01 — thị trường (market / 시장) cấu trúc (structure / 구조) and instruments

[01_MARKET_STRUCTURE_AND_INSTRUMENTS.md](./01_MARKET_STRUCTURE_AND_INSTRUMENTS.md)

Bắt đầu từ câu hỏi **“Forex thị trường (market / 시장) thực sự là thị trường nào?”** Phân biệt spot FX, retail OTC/rolling products, forward, FX swap, currency swap, futures và options; giải thích OTC, interdealer/dealer-client markets, liquidity provider, settlement và vì sao không có một toàn cục (global / 전역) thứ tự (order / 순서) book duy nhất.

## 02 — Quotes, pips, lots and P/L

[02_QUOTES_PIPS_LOTS_AND_PNL.md](./02_QUOTES_PIPS_LOTS_AND_PNL.md)

Đọc currency pair từ nguyên lý nền tảng (first principles / 제일 원리): cơ sở (base / 기반)/quote currency, bid/ask, spread, pip, đặc tả hợp đồng (contract / 계약) kích thước (size / 크기), lot, notional, cross tỷ lệ (rate / 비율), pip giá trị (value / 값) và account-currency conversion. Mục tiêu là tự tính P/L thay vì phụ thuộc broker calculator.

## 03 — Leverage, margin and position sizing

[03_LEVERAGE_MARGIN_POSITION_SIZING.md](./03_LEVERAGE_MARGIN_POSITION_SIZING.md)

Tách ba khái niệm thường bị trộn:

```text
Notional Exposure
≠ Margin Requirement
≠ Amount at Risk
```

Đi sâu equity, used/free margin, margin mức (level / 수준), liquidation/stop-out, portfolio heat, gap rủi ro (risk / 위험) và sizing từ vô hiệu hóa (invalidation / 무효화).

## 04 — Macro drivers, rates, carry and sessions

[04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)

Currency pair là relative price nên phải phân tích hai economies và hai expected tỷ lệ (rate / 비율) paths. Chương nối central-bank reaction hàm (function / 함수), inflation, growth, real yields, carry, balance of payments, capital flows, sessions và positioning vào chuỗi nhân quả (causal chain / 인과 사슬).

## 05 — thực thi (execution / 실행), brokers, costs and operational rủi ro (risk / 위험)

[05_EXECUTION_BROKERS_COSTS_AND_RISK.md](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)

Giải thích chuỗi xử lý (pipeline / 파이프라인) từ tín hiệu (signal / 신호) tới actual fill: thứ tự (order / 순서) types, spread, slippage, rollover, dealer/agency các mô hình (models / 모델들), legal thực thể (entity / 엔터티), broker due diligence, nền tảng (platform / 플랫폼)/API failures và transaction-cost phân tích (analysis / 분석).

# Phase B — Chart và tín hiệu (signal / 신호) nhưng không thần bí hóa indicator

## 06 — Price hành động (action / 동작), trend, phạm vi (range / 범위) and volatility regimes

[06_PRICE_ACTION_TREND_RANGE_AND_VOLATILITY_REGIMES.md](./06_PRICE_ACTION_TREND_RANGE_AND_VOLATILITY_REGIMES.md)

Price hành động (action / 동작) được xử lý như **description trước prediction**. Trend, phạm vi (range / 범위), breakout, pullback, hỗ trợ (support / 지원)/resistance, SMC/ICT vocabulary, candlestick và Fibonacci chỉ có giá trị nghiên cứu khi được formalize thành deterministic quy tắc (rule / 규칙) có vô hiệu hóa (invalidation / 무효화) và có thể backtest.

## 07 — Technical indicators as dữ liệu (data / 데이터) transformations

[07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md](./07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md)

Giải thích SMA/EMA, momentum, RSI, MACD, stochastic, Bollinger, ATR, ADX, Donchian, z-score từ công thức và thông tin (information / 정보) content. Trọng tâm là nhận ra indicator phần lớn là transformations của cùng price dữ liệu (data / 데이터) và tránh “nhiều indicator đồng thuận = nhiều bằng chứng độc lập”.

# Phase C — Fundamental và chiến lược (strategy / 전략) research

## 08 — Fundamental and event-driven FX phân tích (analysis / 분석)

[08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md](./08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md)

Xây sự kiện (event / 이벤트) phân tích (analysis / 분석) từ `consensus → actual → surprise → policy repricing → rates → FX`, dùng official central-bank/statistical sources, phân biệt first reaction/follow-through và xử lý revisions, vintage dữ liệu (data / 데이터), timestamp/DST.

## 09 — Carry, momentum, giá trị (value / 값) and macro FX strategies

[09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md](./09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md)

Học chiến lược (strategy / 전략) families thay vì các setup rời rạc: carry, time-series/cross-sectional momentum, giá trị (value / 값)/PPP, macro directional, sự kiện (event / 이벤트), mean reversion, relative giá trị (value / 값) và volatility. Mỗi family được nối với cơ chế (mechanism / 메커니즘), return nguồn (source / 소스), tail rủi ro (risk / 위험) và portfolio construction.

## 10 — Backtesting and point-in-time FX dữ liệu (data / 데이터)

[10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md](./10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)

Đây là lớp chống tự lừa mình: point-in-time/vintage dữ liệu (data / 데이터), bid/ask, bar conventions, fill mô hình (model / 모델), financing, margin accounting, look-ahead, dữ liệu (data / 데이터) snooping, walk-forward, purging/embargo, multiple testing, parameter surfaces, Monte Carlo và backtest-to-live gap.

# Phase D — Portfolio, rà soát (review / 검토) và institutional độ sâu (depth / 깊이)

## 11 — Portfolio FX rủi ro (risk / 위험), correlation and factor exposure

[11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md](./11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)

Tách ticket khỏi true exposure: currency decomposition, broad-USD/carry/rates/commodity factors, covariance, stress correlation, VaR/Expected Shortfall, volatility targeting, rủi ro (risk / 위험) contribution, basis rủi ro (risk / 위험) và portfolio heat.

## 12 — Trading journal, rà soát (review / 검토) and hiệu năng (performance / 성능) attribution

[12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md](./12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md)

Biến journal thành research cơ sở dữ liệu (database / 데이터베이스). Tách tiến trình (process / 프로세스) khỏi kết quả (outcome / 결과), R/MAE/MFE, tín hiệu (signal / 신호) P/L khỏi spread/slippage/financing, chiến lược (strategy / 전략)/currency-factor attribution, quy tắc (rule / 규칙) violations, mô hình (model / 모델) drift và pre-defined pause/kill criteria.

## 13 — Advanced FX microstructure and thứ tự (order / 순서) luồng (flow / 흐름)

[13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md](./13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md)

Đi vào dealer inventory, adverse selection, fragmentation, độ sâu (depth / 깊이)/resilience, internalization, last look, thông tin (information / 정보) leakage, thứ tự (order / 순서) luồng (flow / 흐름), stop clusters, futures proxy, độ trễ (latency / 지연 시간), fixing flows, markout và TCA. Luôn ghi rõ rằng một venue/feed chỉ là subset của toàn cục (global / 전역) FX.

## 14 — FX options, volatility and hedging

[14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md](./14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md)

Đưa Forex sang payoff phi tuyến: implied vs realized volatility, Delta/Gamma/Theta/Vega, skew/smile, rủi ro (risk / 위험) reversals, sự kiện (event / 이벤트) vol, gamma hedging, barriers, forward-vs-option hedge và option backtesting. Chapter này cross-link với options chuyên sâu ở thư mục cha thay vì duplicate toàn bộ.

# Phase E — ngữ cảnh (context / 맥락) Korea / Vietnam

## 15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) and regulations

[15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md](./15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md)

Chapter time-sensitive được research lại từ nguồn chính thức. Korea: Seoul FX thị trường (market / 시장) reform, RFI, extended hours, USD/KRW, KOFIA FX-margin khung phần mềm (framework / 프레임워크) và intermediary requirements. Vietnam: SBV-authorized FX institutions, domestic FX khung phần mềm (framework / 프레임워크), USD/VND regime, foreign-exchange controls, IFC-specific 2025 rules và Korea–Vietnam corporate exposures.

# Institutional connections — đọc sau cốt lõi (core / 핵심) tuyến (route / 경로) khi cần institutional độ sâu (depth / 깊이)

[`90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md`](./90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md) nối spot với forward points, covered interest parity, FX swaps, cross-currency basis, dealer balance-sheet các ràng buộc (constraints / 제약조건들), synthetic funding, NDF, fixing và onshore/offshore segmentation. Mục tiêu là phân biệt **directional FX** với **funding/hedging economics**.

[`90_connections/01_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md`](./90_connections/01_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md) nối PPP/REER, NIIP, reserves, sterilized/unsterilized intervention, exchange-rate regimes và valuation-model bất định (uncertainty / 불확실성). Mục tiêu là tránh dùng “currency cheap”, reserve headline hay intervention như automatic trading signals.

[`90_connections/02_ECONOMIC_HEDGE_VS_HEDGE_ACCOUNTING.md`](./90_connections/02_ECONOMIC_HEDGE_VS_HEDGE_ACCOUNTING.md) tách economic hedge khỏi accounting designation, documentation, qualifying effectiveness, rebalancing và discontinuation. Đây là ranh giới (boundary / 경계) mô-đun (module / 모듈) dựa trên IFRS 9; không thay thế K-IFRS/local-policy, tax, legal hoặc auditor judgment.

[`90_connections/03_FX_SETTLEMENT_PVP_NETTING_AND_LIQUIDITY.md`](./90_connections/03_FX_SETTLEMENT_PVP_NETTING_AND_LIQUIDITY.md) đi từ trade capture, matching và SSI tới netting, funding cut-off, PvP/gross bilateral settlement, finality, thất bại (fail / 실패) management và intraday-liquidity controls. Mục tiêu là không nhầm **giảm principal rủi ro (risk / 위험)** với **loại bỏ toàn bộ settlement, liquidity, replacement-cost, operational và legal rủi ro (risk / 위험)**.

Bốn liên kết (connection / 연결) files không mở thêm tuyến tính (linear / 선형) `16/17/18/19`; chúng là cầu nối (bridge / 브리지) vào institutional FX và cross-link Economics/Derivatives/financial reporting/payment hạ tầng (infrastructure / 인프라) để giữ chuẩn gốc (canonical / 정본) tuyến (route / 경로) gọn.

# Institutional hedging cases — từ thị trường (market / 시장) exposure sang balance-sheet rủi ro (risk / 위험)

[60_institutional_hedging_cases/README.md](./60_institutional_hedging_cases/README.md) áp dụng Forex vào treasury và asset management:

```text
Korean exporter
→ USD receivable, natural hedge, layered forward, forecast/over-hedge risk

Korean importer
→ USD payable, procurement margin, forward/option, payment-timing risk

Global asset manager
→ local-asset return + FX return, hedge ratio, roll/carry, benchmark and collateral

Cross-currency funding
→ debt currency transformation, FX/CCS, basis, collateral, rollover and counterparty risk
```

Điểm kiểm tra không phải hedge derivative “lãi hay lỗ”, mà là **underlying exposure + hedge + funding/carry + residual rủi ro (risk / 위험)** có đạt mục tiêu (objective / 목표) của balance sheet hay không.

# Phase F — Practice và rà soát (review / 검토)

Lý thuyết `01–15` cùng institutional connections được chuyển thành bài tập tại [90_labs/README.md](./90_labs/README.md):

```text
Lab 00 — quote / pip / P&L / margin / position sizing
Lab 01 — event-driven FX analysis without hindsight
Lab 02 — point-in-time backtest and robustness
Lab 03 — portfolio FX factor risk
Lab 04 — Korea/Vietnam FX context and regulatory verification
Lab 05 — FX options pricing, Greeks, scenarios and delta-hedging attribution
Lab 06 — Vietnam FX-management stress, reserve decomposition and hedge cash-flow lab
Lab 07 — cross-regime stress synthesis, balance-sheet transmission and reverse stress
Lab 08 — hedge-accounting documentation, ineffectiveness and control workflow
```

Các lab yêu cầu tạo sản phẩm tạo ra (artifact / 산출물) có thể rà soát (review / 검토), không phải trả lời quiz ghi nhớ.

# Phase G — Historical stress regimes

[80_case_studies/README.md](./80_case_studies/README.md) dùng các regime cực đoan để stress-test mô hình tư duy (mental model / 사고 모델) thay vì học lịch sử như timeline:

```text
1992 ERM / sterling
→ exchange-rate commitment vs domestic-policy constraint

1997 Asian Financial Crisis
→ currency mismatch + short-term foreign funding + banking feedback loop

2008 Korea USD funding stress
→ exporter forward hedges + short-term rollover + basis stress + USD liquidity backstop

2015 CHF floor removal
→ policy floor + liquidity discontinuity + stop/broker risk

2020 global USD funding stress
→ offshore dollar shortage + FX swaps/basis + central-bank swap lines

2022–2023 Vietnam FX-management stress
→ managed flexibility + reserve drawdown + band widening + policy trade-off

2022–2024 JPY rate divergence and intervention
→ policy divergence + carry positioning + import-cost pressure + official FX operations
```

# Phase H — Systematic hiện thực (implementation / 구현) dự án (project / 프로젝트)

[70_systematic_project/README.md](./70_systematic_project/README.md) biến lý thuyết (theory / 이론), institutional connections và research thành một hệ thống (system / 시스템) có thể kiểm tra (audit / 감사):

```text
01 Data pipeline & time normalization
→ point-in-time data, UTC/DST, bid/ask, macro vintage, validation, lineage

02 Backtest engine & execution model
→ causal event loop, order state, executable fills, cost, financing, margin ledger

03 Portfolio risk & attribution engine
→ currency legs, factors, stress, margin, hedge quality, P/L attribution

04 Forward test, monitoring & kill switch
→ paper/small-live gates, reconciliation, drift, safety controls, retirement rules
```

Dự án (project / 프로젝트) này không nhằm tạo bot tự động sinh lợi; mục tiêu là nối `data → research → execution → portfolio risk → forward test → safe failure` thành một tiến trình (process / 프로세스) reproducible.

Sau Phase H, quay lại [COVERAGE_AUDIT.md](./COVERAGE_AUDIT.md) để phân biệt phần đã có lý thuyết (theory / 이론)/liên kết (connection / 연결)/hedging/practice/trường hợp (case / 사례)/hiện thực (implementation / 구현) độ sâu (depth / 깊이) với extension thực sự còn thiếu.

# Milestone kiểm tra kiến thức

Sau Phase A, phải tự tính và giải thích được P/L, pip/lot/notional, margin, effective leverage, relative macro và all-in thực thi (execution / 실행) chi phí (cost / 비용).

Sau Phase B, phải nhìn chart/indicator như dữ liệu có thể formalize, không coi mẫu (pattern / 패턴)/indicator là nguyên nhân tự thân.

Sau Phase C, phải viết được hypothesis có cơ chế (mechanism / 메커니즘), tín hiệu (signal / 신호), point-in-time dữ liệu (data / 데이터), mô hình thực thi (execution model / 실행 모델), chi phí (cost / 비용) và out-of-sample kiểm tra hợp lệ (validation / 검증).

Sau Phase D, phải tổng hợp rủi ro (risk / 위험) theo currency/factor/chiến lược (strategy / 전략), biết attribution P/L và hiểu giới hạn của order-flow/volatility dữ liệu (data / 데이터).

Sau Phase E, phải biết rằng **sản phẩm (product / 제품) truy cập (access / 접근) và thị trường (market / 시장) cấu trúc (structure / 구조) phụ thuộc jurisdiction**; không suy từ broker marketing rằng một tuyến (route / 경로) hợp pháp hoặc có cùng investor protection ở Korea/Vietnam.

Sau institutional connections, phải phân biệt spot direction với forward/funding economics; hiểu NDF/onshore-offshore segmentation; đọc reserves/intervention/REER theo regime và mô hình (model / 모델) các giả định (assumptions / 가정들) thay vì như single-variable signals.

Sau institutional hedging cases, phải map được **nghiệp vụ (business / 비즈니스)/asset cash luồng (flow / 흐름) → currency exposure → hedge mục tiêu (objective / 목표) → instrument/tenor/ratio → carry/collateral → residual rủi ro (risk / 위험) → combined attribution**, và không đánh giá hedge bằng derivative P/L riêng lẻ.

Sau Phase F, phải có ít nhất một bộ đầu ra (output / 출력) hoàn chỉnh từ `position-risk sheet → event study → backtest report → portfolio-risk dashboard → regulatory verification checklist`.

Sau Phase G, phải có thể giải thích vì sao **low historical volatility, chính sách (policy / 정책) commitment hoặc diversified-looking positions vẫn có thể che giấu jump/funding/factor rủi ro (risk / 위험)**.

Sau Phase H, phải có thể dấu vết (trace / 추적) một live/paper trade từ **raw point-in-time dữ liệu (data / 데이터) → tín hiệu (signal / 신호) → thứ tự (order / 순서)/fill → margin/rủi ro (risk / 위험) → P/L attribution → monitoring quyết định (decision / 결정)**, và hệ thống (system / 시스템) phải có safe-state/kill-switch ngữ nghĩa (semantics / 의미론) rõ ràng.

## Nguyên tắc an toàn nghiên cứu

Forex có thể sử dụng đòn bẩy lớn. Tài liệu phục vụ **học cơ chế, phân tích và quản trị rủi ro**, không đưa ra personalized buy/sell signals hay hứa hẹn lợi nhuận.

Đối với retail OTC/FX-margin products, broker/intermediary/legal thực thể (entity / 엔터티) là một phần của rủi ro (risk / 위험) mô hình (model / 모델). Regulatory details phải được re-check tại thời điểm sử dụng, đặc biệt chapter 15.

## Nguồn nền xuyên suốt

- Bank for International Settlements (BIS), 2025 Triennial Central Bank Survey và research về FX/funding markets.
- CFTC retail FX rủi ro (risk / 위험) and registration guidance.
- IMF/BIS/central-bank materials cho exchange-rate regimes, reserves, intervention và effective exchange rates.
- Federal Reserve, ECB, Bank of Korea và các central banks/statistical agencies tương ứng.
- Korea Financial Investment Association (KOFIA) cho FX-margin investor guidance tại Korea.
- trạng thái (state / 상태) Bank of Vietnam và official legal databases cho Vietnam FX rules.
- Historical trường hợp (case / 사례) studies ưu tiên central-bank, IMF, BIS và official contemporary documentation.

Với số liệu hoặc quy định theo thời điểm, luôn ghi ngày/kỳ dữ liệu và nguồn (source / 소스). Không biến một snapshot hoặc historical regime thành quy luật vĩnh viễn.
