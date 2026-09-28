# Forex Coverage kiểm tra (audit / 감사)

`as_of_date: 2026-09-28`

> **Mạch đọc:** kiểm tra (audit / 감사) này đứng sau lộ trình học (learning path / 학습 경로) Forex: dùng nó để kiểm tra đơn vị sở hữu (owner / 오너), ranh giới (boundary / 경계) và bằng chứng (evidence / 증거) của từng phase, rồi quay lại chapter hoặc trường hợp (case / 사례) cụ thể để lấp gap thay vì tạo thêm tệp (file / 파일) rời.

Tệp (file / 파일) này kiểm tra coverage của nhánh `investing/05_trading_derivatives/forex/` để tránh hai lỗi ngược nhau: thiếu nền tảng quan trọng hoặc tiếp tục tạo chapter mới chỉ để lặp lại nội dung đã có.

Chuẩn gốc (canonical / 정본) tuyến (route / 경로) vẫn là `01–15`. `60_institutional_hedging_cases/` giữ balance-sheet applications, `70_systematic_project/` giữ hiện thực (implementation / 구현) cầu nối (bridge / 브리지), `80_case_studies/` giữ historical stress regimes, `90_connections/` giữ institutional bridges và `90_labs/` giữ practice. Cách tổ chức này tăng độ sâu (depth / 깊이) mà không biến thư viện (library / 라이브러리) thành chuỗi chapter tuyến tính chỉ để tăng số lượng.

## 1. Coverage map

| Area | chuẩn gốc (canonical / 정본) chapter | độ sâu (depth / 깊이) status | Practice / trường hợp (case / 사례) / hiện thực (implementation / 구현) độ sâu (depth / 깊이) |
|---|---|---|---|
| FX thị trường (market / 시장) cấu trúc (structure / 구조), OTC, spot/forward/swap/futures/options | `01_MARKET_STRUCTURE_AND_INSTRUMENTS.md` | Deep foundation | Lab 04; ERM/CHF cases |
| Quote, cơ sở (base / 기반)/quote, pip, lot, cross-rate, P/L | `02_QUOTES_PIPS_LOTS_AND_PNL.md` | Deep foundation | Lab 00; systematic thực thi (execution / 실행) ledger |
| Leverage, margin, sizing, portfolio heat | `03_LEVERAGE_MARGIN_POSITION_SIZING.md` | Deep foundation | Lab 00, Lab 03; CHF trường hợp (case / 사례); rủi ro (risk / 위험) engine |
| Rates, central banks, carry, BOP, flows, sessions | `04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md` | Deep foundation | Lab 01, Lab 04; all historical cases |
| Orders, broker/dealer, spread, slippage, financing, operational rủi ro (risk / 위험) | `05_EXECUTION_BROKERS_COSTS_AND_RISK.md` | Deep foundation | Lab 01, Lab 02; CHF trường hợp (case / 사례); thực thi (execution / 실행)/monitoring modules |
| Trend/phạm vi (range / 범위)/volatility, hỗ trợ (support / 지원)/resistance, breakout/pullback, SMC/ICT framing | `06_PRICE_ACTION_TREND_RANGE_AND_VOLATILITY_REGIMES.md` | Deep | Lab 02 |
| MA/EMA, RSI, MACD, ATR, Bollinger, indicator normalization | `07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md` | Deep | Lab 02; feature-pipeline ngữ nghĩa (semantics / 의미론) |
| Macro-event research, expectations, surprise, transmission | `08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md` | Deep | Lab 01; historical cases; point-in-time sự kiện (event / 이벤트) dữ liệu (data / 데이터) |
| Carry, momentum, giá trị (value / 값), macro chiến lược (strategy / 전략) families | `09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md` | Deep | Lab 02; Asian-crisis/CHF tail-risk ngữ cảnh (context / 맥락) |
| Point-in-time dữ liệu (data / 데이터), độ lệch (bias / 편향), chi phí (cost / 비용), robustness, walk-forward | `10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md` | Deep | Lab 02; regime-break cases; full systematic dự án (project / 프로젝트) |
| Currency-factor aggregation, correlation, stress, hedging | `11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md` | Deep | Lab 03; institutional hedging cases; rủi ro (risk / 위험)/attribution engine |
| Journal, attribution, MAE/MFE, tiến trình (process / 프로세스) rà soát (review / 검토) | `12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md` | Deep | labs/cases; attribution/forward-test modules |
| Dealer luồng (flow / 흐름), liquidity, venue fragmentation, thứ tự (order / 순서) luồng (flow / 흐름) | `13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md` | Advanced | CHF/2020 cases; mô hình thực thi (execution model / 실행 모델) |
| FX options, IV, skew, Greeks, hedging | `14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md` | Advanced cầu nối (bridge / 브리지) | exporter/importer option comparison; Lab 05 quantitative decomposition |
| Korea/Vietnam FX ngữ cảnh (context / 맥락) and hiện tại (current / 현재) regulation | `15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md` | Context-specific deep | Labs 04/06; Korea 2008 and Vietnam 2022–2023 cases |
| Forward points, CIP, FX swaps, NDF, basis, funding, onshore/offshore segmentation | `90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md` | Advanced institutional cầu nối (bridge / 브리지) | 2008 Korea and 2020 USD-funding cases; cross-currency funding trường hợp (case / 사례) |
| Intervention, reserves, exchange-rate regimes, PPP/REER, valuation bất định (uncertainty / 불확실성) | `90_connections/01_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md` | Advanced macro-policy cầu nối (bridge / 브리지) | ERM/Asian/CHF, JPY 2022–2024 and Vietnam 2022–2023 cases |
| Economic hedge vs hedge accounting, designation, documentation and effectiveness ranh giới (boundary / 경계) | `90_connections/02_ECONOMIC_HEDGE_VS_HEDGE_ACCOUNTING.md` | Advanced reporting/quản trị (governance / 거버넌스) cầu nối (bridge / 브리지) | all institutional hedging cases; Lab 08 documentation/điều khiển (control / 제어) workflow |
| Settlement vòng đời (lifecycle / 생명주기), PvP, netting, SSI, cut-offs, fails and intraday liquidity | `90_connections/03_FX_SETTLEMENT_PVP_NETTING_AND_LIQUIDITY.md` | Advanced post-trade/treasury cầu nối (bridge / 브리지) | settlement exposure map, liquidity ladder, thất bại (fail / 실패) controls and reverse stress |
| Corporate/asset-manager giao dịch (transaction / 트랜잭션) and funding hedging | `60_institutional_hedging_cases/` | Applied institutional độ sâu (depth / 깊이) | exporter, importer, asset manager, cross-currency funding |

## 2. What is intentionally not duplicated

Các nội dung sau đã có chuẩn gốc (canonical / 정본) độ sâu (depth / 깊이) ở phần khác của `investing/` và Forex chỉ cross-link:

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

General open-economy macro lý thuyết (theory / 이론), monetary chính sách (policy / 정책), exchange-rate crises và econometric identification vẫn thuộc [`../../../economics/`](../../../economics/README.md). `90_connections/` chỉ giữ **FX-specific hiện thực (implementation / 구현) and interpretation**: forward/NDF/basis/funding plumbing và cách reserves/intervention/REER đi vào currency phân tích (analysis / 분석).

`70_systematic_project/` chỉ giữ **FX-specific hiện thực (implementation / 구현) ngữ nghĩa (semantics / 의미론)**: bid/ask, session/DST, macro vintage, rollover, account-currency conversion, margin, currency-factor aggregation, execution-aware backtest và live reconciliation. Generic software/cơ sở dữ liệu (database / 데이터베이스)/cloud kỹ thuật (engineering / 엔지니어링) vẫn thuộc lĩnh vực (domain / 도메인) computing tương ứng.

`60_institutional_hedging_cases/` không thay thế corporate-finance/accounting/legal documentation. Nó tập trung economic exposure, instrument payoff, carry/basis, collateral, timing/volume mismatch và combined hedge attribution.

Không tạo lại các chapter Forex có cùng nội dung chỉ đổi ví dụ từ stock/futures sang EUR/USD nếu không có FX-specific mechanics mới.

## 3. Institutional liên kết (connection / 연결) coverage

### Funding / forward / NDF tầng (layer / 계층)

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

Độ sâu (depth / 깊이) gate là phân biệt **directional FX view** với **hedging/funding luồng (flow / 흐름)**, và hiểu rằng capital-control wedge hoặc basis deviation không tự động là exploitable arbitrage.

### Chính sách (policy / 정책) / valuation tầng (layer / 계층)

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

Độ sâu (depth / 깊이) gate là hiểu **valuation ≠ timing**, **reserve thay đổi (change / 변경) ≠ intervention amount**, và **intervention ≠ guaranteed reversal**.

### Hedge-accounting ranh giới (boundary / 경계)

`90_connections/02_ECONOMIC_HEDGE_VS_HEDGE_ACCOUNTING.md` nối:

```text
business exposure
→ economic hedge objective
→ eligible item/instrument
→ designation and documentation
→ economic relationship / credit-risk / hedge-ratio criteria
→ ineffectiveness, rebalancing and discontinuation
```

Độ sâu (depth / 깊이) gate là hiểu **economic hedge ≠ qualifying accounting relationship**, đồng thời không biến accounting designation thành bằng chứng rằng nghiệp vụ (business / 비즈니스) rủi ro (risk / 위험) đã được loại bỏ. cục bộ (local / 로컬) K-IFRS, tax, legal và journal-entry hiện thực (implementation / 구현) vẫn phải được verify ngoài chapter.

### Settlement / PvP / netting tầng (layer / 계층)

`90_connections/03_FX_SETTLEMENT_PVP_NETTING_AND_LIQUIDITY.md` nối:

```text
trade capture
→ confirmation / matching / SSI
→ bilateral or multilateral netting
→ currency funding and market cut-offs
→ PvP or gross bilateral settlement
→ finality, fail management and reconciliation
```

Độ sâu (depth / 깊이) gate là hiểu **PvP loại bỏ principal settlement rủi ro (risk / 위험) cho phần giao dịch được bảo vệ, không loại bỏ mọi FX rủi ro (risk / 위험)**; **netting giảm gross obligation, không tự tạo legal enforceability hay liquidity chắc chắn**. Replacement-cost, intraday-liquidity, operational, legal và residual counterparty risks vẫn phải được đo và stress riêng.

## 4. Institutional hedging coverage

Folder `60_institutional_hedging_cases/` đã chuyển institutional lý thuyết (theory / 이론) thành balance-sheet applications:

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

Độ sâu (depth / 깊이) gate là đánh giá **underlying exposure + hedge + carry/funding + giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) + residual rủi ro (risk / 위험)**, không đánh giá hedge instrument bằng standalone derivative P/L.

Các trường hợp (case / 사례) cũng tách giao dịch (transaction / 트랜잭션) exposure khỏi economic exposure và funding/liquidity rủi ro (risk / 위험); một forward đúng direction vẫn có thể thất bại (fail / 실패) operationally vì timing, volume, collateral hoặc counterparty mismatch.

## 5. Practice coverage

Practice tầng (layer / 계층) hiện có:

```text
Lab 00 — mechanics, P/L, margin, position sizing
Lab 01 — macro event analysis without hindsight
Lab 02 — point-in-time backtest and robustness
Lab 03 — portfolio FX factor risk
Lab 04 — Korea/Vietnam context and regulatory verification
Lab 05 — FX options pricing, Greeks, scenarios and delta-hedging attribution
Lab 06 — Vietnam FX-management stress, reserve decomposition and hedge cash-flow analysis
Lab 07 — cross-regime mechanism comparison, balance-sheet transmission and reverse stress
Lab 08 — hedge-accounting designation, ineffectiveness, rebalance/discontinuation and close controls
```

Các lab được thiết kế để tạo sản phẩm tạo ra (artifact / 산출물) reviewable thay vì quiz ghi nhớ.

Institutional connections/hedging cases chưa cần lab riêng chỉ để đủ số lượng. Lab 05 có dữ liệu (data / 데이터)/payoff tác vụ (task / 작업) cụ thể: option pricing, volatility-surface conventions, delta-hedging ledger và implied-versus-realized attribution. Lab 06 có regime/payoff tác vụ (task / 작업) cụ thể: reserve decomposition, band scenario, chính sách (policy / 정책) sự đánh đổi (trade-off / 트레이드오프), importer/exporter cash-flow và publication-lag discipline. Lab 07 đóng gap synthesis bằng cách buộc so sánh vulnerability, trigger, amplifier, thị trường (market / 시장) thất bại (failure / 실패) và chính sách (policy / 정책) ràng buộc (constraint / 제약조건) trên cả bảy historical cases. Lab 08 chuyển hedge-accounting ranh giới (boundary / 경계) thành exposure register, designation memo, ineffectiveness phân tích (analysis / 분석) và month-end điều khiển (control / 제어) artifacts.

## 6. Historical case-study coverage

Folder `80_case_studies/` đã bổ sung độ sâu (depth / 깊이) theo regime/cơ chế (mechanism / 메커니즘):

```text
1992 ERM / sterling
→ exchange-rate commitment vs domestic policy constraint

1997 Asian Financial Crisis
→ currency mismatch + short-term foreign funding + banking feedback loop

2008 Korea USD funding stress
→ exporter forward hedges + foreign-bank-branch rollover + basis stress + USD liquidity backstop

2015 CHF floor removal
→ policy floor + discontinuous liquidity + stop/broker risk

2020 global USD funding stress
→ offshore dollar shortage + FX swaps/basis + central-bank swap lines

2022–2023 Vietnam FX-management stress
→ managed flexibility + reserve drawdown + band widening + policy trade-off

2022–2024 JPY rate divergence and intervention
→ monetary-policy divergence + carry positioning + import-cost pressure + official FX operations
```

Trường hợp (case / 사례) studies không nhằm tạo historical mẫu (pattern / 패턴) để trade. Chúng dùng để stress mô hình tư duy (mental models / 사고 모델들) của các chapter `01–15` và institutional connections dưới những regime cực đoan.

## 7. Systematic hiện thực (implementation / 구현) coverage

Folder `70_systematic_project/` đã triển khai cầu nối (bridge / 브리지) từ research sang hệ thống (system / 시스템) có thể kiểm tra (audit / 감사):

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

Dự án (project / 프로젝트) intentionally stops at specification/kiến trúc (architecture / 아키텍처) độ sâu (depth / 깊이). Nó không duplicate generic programming tutorials; hiện thực (implementation / 구현) ngôn ngữ (language / 언어) có thể là Python, Java, SQL hoặc ngăn xếp (stack / 스택) khác nếu ngữ nghĩa (semantics / 의미론) vẫn giống nhau và reproducible.

## 8. Remaining optional extensions

Các phần dưới đây **không phải gap nền tảng**. Chỉ mở rộng nếu có mục tiêu học cụ thể.

### A. FX options quantitative lab — completed

`90_labs/05_FX_OPTIONS_QUANTITATIVE_LAB.md` đã chuyển extension này thành bài tập có sản phẩm tạo ra (artifact / 산출물) reviewable:

```text
Delta / Gamma / Vega P&L decomposition
Risk reversal / butterfly quote conventions
Volatility surface interpolation
Delta-hedged option P/L
Event implied-vs-realized volatility
Barrier/event gap scenarios vẫn là phần mở rộng trong lab, chưa phải claim coverage đầy đủ cho mọi exotic payoff.
```

### B. Additional historical/regime cases

Không còn historical-regime candidate bắt buộc trong kiểm tra (audit / 감사) hiện tại. Chỉ thêm trường hợp (case / 사례) mới nếu nó tạo cơ chế (mechanism / 메커니즘) khác biệt, không chỉ thêm một sự kiện (event / 이벤트) nổi tiếng.

### C. Full executable codebase

Chỉ nên tạo nếu mục tiêu chuyển repository từ thư viện kiến thức (knowledge library / 지식 라이브러리) sang dự án (project / 프로젝트)/mã (code / 코드) deliverable. Khi đó mã (code / 코드) cần đặt ranh giới (boundary / 경계) rõ với `computer_science/`, `data_engineering/`, `sql/` và triển khai (deployment / 배포) domains thay vì để Forex documentation chứa một khung phần mềm (framework / 프레임워크) software độc lập.

### D. Accounting / legal hiện thực (implementation / 구현) — ranh giới (boundary / 경계) added

`90_connections/02_ECONOMIC_HEDGE_VS_HEDGE_ACCOUNTING.md` và `90_labs/08_HEDGE_ACCOUNTING_DOCUMENTATION_BOUNDARY_LAB.md` đã bổ sung conceptual ranh giới (boundary / 경계), IFRS 9 qualifying gate và documentation/điều khiển (control / 제어) workflow. Journal entries, cục bộ (local / 로컬) K-IFRS adoption, tax, collateral documentation và legal enforceability vẫn chỉ nên được thêm khi có phạm vi (scope / 범위) riêng, facts cụ thể và standards hiện hành.

## 9. chất lượng (quality / 품질) risks to monitor

Khi cập nhật (update / 업데이트) về sau, kiểm tra các lỗi sau:

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
PvP is presented as eliminating all FX, liquidity or operational risk
Netting benefit is assumed without enforceability, eligibility or cut-off constraints
```

## 10. rà soát (review / 검토) cadence

Các chapter mechanics có thể rà soát (review / 검토) chậm hơn. Các phần sau phải rà soát (review / 검토) khi regulation/thị trường (market / 시장) convention thay đổi:

```text
01 market structure where current statistics are cited
05 broker/regulatory execution context
15 Korea/Vietnam FX market context and regulations
90_connections/00 when funding/benchmark/market conventions materially change
90_connections/01 when regime/intervention methodology or source conventions materially change
90_connections/02 when IFRS 9 hedge-accounting requirements, interpretations or local adoption materially change
90_connections/03 when settlement-cycle, PvP eligibility, currency coverage, market cut-off or legal-netting conventions materially change
70_systematic_project when product/account/data semantics materially change
60_institutional_hedging_cases when market-access, product or collateral conventions are used as current facts
```

Chapter `15` phải giữ `as_of_date` hoặc nguồn có ngày rõ ràng cho quy tắc (rule / 규칙) hiện hành.

Historical cases không cần refresh vì chronology thay đổi, nhưng nguồn (source / 소스) links và interpretation nên được rà soát (review / 검토) nếu thêm research mới hoặc sửa cơ chế (mechanism / 메커니즘).

Systematic-project specs cần rà soát (review / 검토) nếu margin, financing, broker thực thi (execution / 실행), API ngữ nghĩa (semantics / 의미론) hoặc data-source convention thay đổi.

## 11. hiện tại (current / 현재) conclusion

Nhánh Forex hiện có bảy tầng (layer / 계층):

```text
Theory / mechanism        → chapters 01–15
Institutional hedging     → 60_institutional_hedging_cases/
Systematic implementation → 70_systematic_project/
Historical regime depth   → 80_case_studies/
Institutional bridges     → 90_connections/
Practice                  → 90_labs/
Coverage governance       → COVERAGE_AUDIT.md
```

Coverage đã đi từ **beginner mechanics → macro/chiến lược (strategy / 전략) research → portfolio/microstructure/options → jurisdiction ngữ cảnh (context / 맥락) → institutional funding/chính sách (policy / 정책) → corporate/asset-manager hedging → practical ứng dụng (application / 애플리케이션) → historical stress regimes → reproducible systematic hiện thực (implementation / 구현) ngữ nghĩa (semantics / 의미론)**.

Bước tiếp theo không nên là tạo thêm tuyến tính (linear / 선형) lý thuyết (theory / 이론), historical trường hợp (case / 사례) không có cơ chế (mechanism / 메커니즘) mới hoặc generic coding tutorial. Coverage nền tảng và synthesis đã đủ; mở rộng tiếp chỉ hợp lý khi có phạm vi (scope / 범위) rõ cho executable hiện thực (implementation / 구현) hoặc accounting/legal documentation với nguồn (source / 소스) chuẩn.
