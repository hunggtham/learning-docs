# Forex — Foreign Exchange Lộ trình học (learning path / 학습 경로)

Forex (foreign exchange, **thị trường ngoại hối**, tiếng Hàn: **외환**) là một nhánh con của `05_trading_derivatives/`. Phần này không được tổ chức như một bộ mẹo giao dịch hay danh sách indicator. Mục tiêu là xây mô hình tư duy (mental model / 사고 모델) hoàn chỉnh từ **thị trường (market / 시장) cấu trúc (structure / 구조) → quote/P&L → leverage/rủi ro (risk / 위험) → macro → thực thi (execution / 실행) → price/regime → chiến lược (strategy / 전략) research → portfolio → microstructure/options → jurisdiction → institutional funding/valuation**.

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

Xem [`COVERAGE_AUDIT.md`](./COVERAGE_AUDIT.md) để biết độ sâu (depth / 깊이) gate, ranh giới (boundary / 경계) và phần nào **không nên** tiếp tục mở rộng chỉ để tăng số tệp (file / 파일).

## Vị trí trong Investing thư viện (library / 라이브러리)
Phần “Vị trí trong Investing thư viện (library / 라이브러리)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


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
        ├── 16_NDF_FORWARD_POINTS_BASIS_AND_FUNDING.md
        └── 17_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md
```

Tệp (file / 파일) `00_MASTER_TRADING_FOREX_RISK.md` ở thư mục cha vẫn là bản đồ tổng quan của Trading & Derivatives. Folder này đi sâu riêng vào Forex để tránh làm tệp (file / 파일) master phình to và tránh duplicate nội dung options, derivatives hay systematic trading đã có ở nhánh cha.

# Phase A — Mechanics và survival

## 01 — Thị trường (market / 시장) cấu trúc (structure / 구조) and instruments

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

## 05 — Thực thi (execution / 실행), brokers, costs and operational rủi ro (risk / 위험)

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

# Phase D — Portfolio, rà soát (review / 검토) và thị trường (market / 시장) microstructure

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

# Phase E — Ngữ cảnh (context / 맥락) Korea / Vietnam

## 15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) and regulations

[15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md](./15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md)

Chapter time-sensitive được research lại từ nguồn chính thức. Korea: Seoul FX thị trường (market / 시장) reform, RFI, extended hours, USD/KRW, KOFIA FX-margin khung phần mềm (framework / 프레임워크) và intermediary requirements. Vietnam: SBV-authorized FX institutions, domestic FX khung phần mềm (framework / 프레임워크), USD/VND regime, foreign-exchange controls, IFC-specific rules và Korea–Vietnam corporate exposures.

# Phase F — Institutional funding, chính sách (policy / 정책) và valuation

## 16 — NDF, forward points, basis and funding

[16_NDF_FORWARD_POINTS_BASIS_AND_FUNDING.md](./16_NDF_FORWARD_POINTS_BASIS_AND_FUNDING.md)

Đi từ covered-interest-parity intuition sang forward points, FX swaps, cross-currency basis, dealer balance-sheet các ràng buộc (constraints / 제약조건들), collateral, synthetic funding và NDF. Chương này tách onshore/offshore thị trường (market / 시장), fixing convention và capital-control wedge để tránh gọi mọi price gap là arbitrage.

## 17 — Intervention, reserves, REER and currency valuation

[17_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md](./17_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md)

Nối PPP/REER, bên ngoài (external / 외부) balance, NIIP, reserve adequacy, sterilized/unsterilized intervention, exchange-rate regimes, BEER/FEER intuition và mô hình (model / 모델) bất định (uncertainty / 불확실성). Mục tiêu là hiểu valuation như slow anchor, không dùng “currency rẻ” hay reserve headline như automatic trading tín hiệu (signal / 신호).

# Milestone kiểm tra kiến thức

Sau Phase A, phải tự tính và giải thích được P/L, pip/lot/notional, margin, effective leverage, relative macro và all-in thực thi (execution / 실행) chi phí (cost / 비용).

Sau Phase B, phải nhìn chart/indicator như dữ liệu có thể formalize, không coi mẫu (pattern / 패턴)/indicator là nguyên nhân tự thân.

Sau Phase C, phải viết được hypothesis có cơ chế (mechanism / 메커니즘), tín hiệu (signal / 신호), point-in-time dữ liệu (data / 데이터), mô hình thực thi (execution model / 실행 모델), chi phí (cost / 비용) và out-of-sample kiểm tra hợp lệ (validation / 검증).

Sau Phase D, phải tổng hợp rủi ro (risk / 위험) theo currency/factor/chiến lược (strategy / 전략), biết attribution P/L và hiểu giới hạn của order-flow/volatility dữ liệu (data / 데이터).

Sau Phase E, phải biết rằng **sản phẩm (product / 제품) truy cập (access / 접근) và thị trường (market / 시장) cấu trúc (structure / 구조) phụ thuộc jurisdiction**; không suy từ broker marketing rằng một tuyến (route / 경로) hợp pháp hoặc có cùng investor protection ở Korea/Vietnam.

Sau Phase F, phải phân biệt spot direction với forward/funding economics; hiểu NDF/onshore-offshore segmentation; đọc reserves/intervention/REER theo regime và mô hình (model / 모델) các giả định (assumptions / 가정들) thay vì như single-variable signals.

## Nguyên tắc an toàn nghiên cứu

Forex có thể sử dụng đòn bẩy lớn. Tài liệu phục vụ **học cơ chế, phân tích và quản trị rủi ro**, không đưa ra personalized buy/sell signals hay hứa hẹn lợi nhuận.

Đối với retail OTC/FX-margin products, broker/intermediary/legal thực thể (entity / 엔터티) là một phần của rủi ro (risk / 위험) mô hình (model / 모델). Regulatory details phải được re-check tại thời điểm sử dụng, đặc biệt chapter 15.

## Nguồn nền xuyên suốt
Phần “Nguồn nền xuyên suốt” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- Bank for International Settlements (BIS), Triennial Central Bank Survey và research về FX/funding markets.
- CFTC retail FX rủi ro (risk / 위험) and registration guidance.
- IMF/BIS/central-bank materials cho exchange-rate regimes, reserves, intervention và effective exchange rates.
- Federal Reserve, ECB, Bank of Korea và các central banks/statistical agencies tương ứng.
- Korea Financial Investment Association (KOFIA) cho FX-margin investor guidance tại Korea.
- Trạng thái (state / 상태) Bank of Vietnam và official legal databases cho Vietnam FX rules.

Với số liệu hoặc quy định theo thời điểm, luôn ghi ngày/kỳ dữ liệu và nguồn (source / 소스). Không biến một snapshot thành quy luật vĩnh viễn.
