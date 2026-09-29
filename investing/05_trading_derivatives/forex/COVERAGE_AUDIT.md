# Forex — Coverage Kiểm tra (audit / 감사)

## Kết luận hiện tại

Forex hiện có chuẩn gốc (canonical / 정본) lộ trình học (learning path / 학습 경로) đủ sâu từ retail/instrument mechanics tới institutional FX. Đường dẫn (path / 경로) không được coi là “hoàn thành” chỉ vì có nhiều chapter; completion gate là người học phải nối được **instrument → funding → macro → thực thi (execution / 실행) → dữ liệu (data / 데이터) → chiến lược (strategy / 전략) → portfolio → jurisdiction** mà không biến chart mẫu (pattern / 패턴) hoặc macro headline thành nhân quả (causal / 인과적) quy tắc (rule / 규칙).

Sau institutional độ sâu (depth / 깊이) pass mới nhất, hai khoảng trống quan trọng trước đây đã được lấp:

- `16` nối NDF, forward points, FX swaps, cross-currency basis, funding và capital-control wedges;
- `17` nối intervention, reserves, exchange-rate regime, REER/PPP và currency valuation.

## Chuẩn gốc (canonical / 정본) tuyến (route / 경로)

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

## Coverage ma trận (matrix / 행렬)

| Tầng (layer / 계층) | Trạng thái | Nội dung đã có | Next-depth nếu cần |
|---|---|---|---|
| Thị trường (market / 시장) mechanics | Strong | OTC cấu trúc (structure / 구조), spot/forward/swap/futures/options/CFD, settlement, counterparty, CLS, quotes/pips/lots | prime brokerage/credit lines nếu cần institutional specialization |
| Rủi ro (risk / 위험) & leverage | Strong | notional vs margin vs amount-at-risk, liquidation, position sizing, portfolio heat | margin tối ưu hóa (optimization / 최적화) across venues |
| Macro | Strong | rates, reaction functions, yields, carry, BOP/capital flows, terms of trade, sessions | cross-asset macro factor estimation |
| Thực thi (execution / 실행) | Strong | spread/slippage/rollover, broker due diligence, thứ tự (order / 순서) types, TCA, operational rủi ro (risk / 위험) | algorithmic thực thi (execution / 실행) benchmark thiết kế (design / 설계) |
| Technical phân tích (analysis / 분석) | Strong ranh giới (boundary / 경계) | price hành động (action / 동작) as description; indicators as transformations; formalization/backtest yêu cầu (requirement / 요구사항) | no need to add indicator encyclopedia |
| Chiến lược (strategy / 전략) research | Strong | carry/momentum/giá trị (value / 값)/sự kiện (event / 이벤트)/mean reversion, point-in-time dữ liệu (data / 데이터), OOS/walk-forward, multiple testing | advanced statistical học tập (learning / 학습) only if research use-case exists |
| Portfolio | Strong | currency-factor decomposition, covariance/stress correlation, VaR/ES, attribution | động (dynamic / 동적) hedging tối ưu hóa (optimization / 최적화) |
| Microstructure | Strong | fragmentation, inventory, adverse selection, last look, thứ tự (order / 순서) luồng (flow / 흐름), fixing, markout | venue-specific empirical dữ liệu (data / 데이터) if available |
| Options | Strong cầu nối (bridge / 브리지) | vol/skew/smile, Greeks, sự kiện (event / 이벤트) vol, hedging | advanced FX option conventions/exotics only if needed |
| Korea/Vietnam | Hiện tại (current / 현재) + time-sensitive | onshore/offshore ngữ cảnh (context / 맥락), truy cập (access / 접근)/regulatory boundaries, corporate exposure | recurring regulatory refresh, not static expansion |
| Funding/NDF | **Strong after độ sâu (depth / 깊이) pass** | forward points, CIP, basis, FX swaps, NDF fixing, onshore/offshore wedges, collateral/funding | empirical basis/NDF trường hợp (case / 사례) study if point-in-time dữ liệu (data / 데이터) available |
| Valuation/chính sách (policy / 정책) | **Strong after độ sâu (depth / 깊이) pass** | REER/PPP, NIIP, reserves, intervention, regimes, BEER/FEER intuition | historical intervention trường hợp (case / 사례) studies with nguồn (source / 소스)/phiên bản (version / 버전) điều khiển (control / 제어) |

## Độ sâu (depth / 깊이) gates

### Gate 1 — Sản phẩm (product / 제품) định danh (identity / 식별자)

Before any chiến lược (strategy / 전략), learner must distinguish:

```text
deliverable spot
forward
FX swap
NDF
futures
options
retail rolling FX / CFD
```

Ticker similarity does not imply same legal/economic sản phẩm (product / 제품).

### Gate 2 — P/L and funding

Must be able to decompose:

```text
spot movement
+ forward/carry/financing
+ spread/commission/slippage
+ hedge/basis effects
= realized economics
```

### Gate 3 — Rủi ro (risk / 위험)

Must separate:

```text
notional exposure
margin requirement
loss-at-risk
portfolio factor exposure
```

Leverage is a balance-sheet multiplier, not an edge.

### Gate 4 — Macro bằng chứng (evidence / 증거)

Must avoid rules such as:

```text
rate hike → currency up
trade surplus → currency up
high yield → free carry
intervention → guaranteed reversal
cheap REER → buy now
```

Every macro claim needs expectations, relative side, regime, rủi ro (risk / 위험) premium and positioning ngữ cảnh (context / 맥락).

### Gate 5 — Research integrity

Backtest must trạng thái (state / 상태):

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

Truy cập (access / 접근), sản phẩm (product / 제품) classification and investor protection are jurisdiction-specific. Chapter `15` is time-sensitive and must be rechecked before practical decisions.

## Anti-duplication đặc tả hợp đồng (contract / 계약)

Forex stays a child of Investing.

- [`../../../economics/`](../../../economics/README.md) owns general macroeconomic lý thuyết (theory / 이론) and econometrics.
- [`../`](../README.md) owns general derivatives/options/systematic trading and thực thi (execution / 실행) concepts dùng chung (shared / 공유) across asset classes.
- Forex owns currency-specific thị trường (market / 시장) cấu trúc (structure / 구조), funding, chiến lược (strategy / 전략) hiện thực (implementation / 구현), microstructure and jurisdiction ngữ cảnh (context / 맥락).
- [`../../06_markets_korea_vietnam/`](../../06_markets_korea_vietnam/README.md) owns broader Korea/Vietnam investing and market-access ứng dụng (application / 애플리케이션).

Cross-link instead of copying entire macro/options chapters.

## Bằng chứng (evidence / 증거) đặc tả hợp đồng (contract / 계약)

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

A pricing định danh (identity / 식별자) is not a profit guarantee. A historical factor return is not a future edge. A backtest is not live bằng chứng (evidence / 증거). A broker's sản phẩm (product / 제품) page is not regulatory authority.

## Time-sensitive content

The most time-sensitive chapter is `15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md`.

Refresh triggers include:

- Korean FX-market truy cập (access / 접근)/hours/RFI changes;
- KOFIA/FSC/FSS rules for retail FX-margin/intermediaries;
- SBV foreign-exchange circular/decree changes;
- Vietnam IFC phạm vi (scope / 범위)/rules;
- material market-structure changes affecting dữ liệu (data / 데이터)/backtests.

Bản ghi (record / 레코드) nguồn (source / 소스), publication/effective date and retrieval date.

## What should **not** be added next

Do not expand by creating:

- dozens of candlestick-pattern files;
- indicator-by-indicator chapters;
- “best chiến lược (strategy / 전략)” lists;
- broker rankings without a hiện tại (current / 현재) shopping/compliance need;
- deterministic macro trading rules;
- duplicated general options/economics lý thuyết (theory / 이론).

These increase tệp (file / 파일) count without increasing nhân quả (causal / 인과적)/thị trường (market / 시장) understanding.

## Next legitimate độ sâu (depth / 깊이) candidates

Only expand when a concrete học tập (learning / 학습) need appears. Highest-value candidates are:

1. an empirical **FX funding/basis crisis trường hợp (case / 사례) study** using documented point-in-time dữ liệu (data / 데이터);
2. an **intervention/regime-change trường hợp (case / 사례) study** showing reserve, rates, spot/forward and chính sách (policy / 정책) timeline together;
3. an **end-to-end FX research lab** from hypothesis to dữ liệu (data / 데이터) lineage, backtest, thực thi (execution / 실행) các giả định (assumptions / 가정들) and live attribution;
4. advanced **FX option thị trường (market / 시장) conventions/exotics** only if options become a real study goal.

Until then, priority should be QA, cross-links, regulatory freshness and exercises rather than more lý thuyết (theory / 이론) chapters.
