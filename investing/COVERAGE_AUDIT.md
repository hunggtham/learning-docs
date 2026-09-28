# Investing — Coverage & độ sâu (depth / 깊이) kiểm tra (audit / 감사)

> **Mạch đọc:** Đặt **Investing — Coverage & độ sâu (depth / 깊이) kiểm tra (audit / 감사)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Kết luận hiện tại** sang **1. Coverage ma trận (matrix / 행렬)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


`as_of_date: 2026-09-25`

Kiểm tra (audit / 감사) này đánh giá `investing/` ở cấp toàn thư viện (library / 라이브러리). Mục tiêu không phải đếm chapter mà xác định **lĩnh vực (domain / 도메인) nào đã có chuẩn gốc (canonical / 정본) độ sâu (depth / 깊이), năng lực (capability / 역량) nào còn thiếu, phần nào time-sensitive, và khi nào không nên tạo thêm lý thuyết (theory / 이론) tệp (file / 파일)**.

## Kết luận hiện tại

Investing hiện đã đạt **cốt lõi (core / 핵심) breadth + advanced ứng dụng (application / 애플리케이션) độ sâu (depth / 깊이)** trên toàn bộ học tập (learning / 학습) tuyến (route / 경로):

```text
01 Foundations
→ 02 Asset Classes
→ 03 Company Analysis
→ 04 Applied Economics / Macro
→ 05 Trading & Derivatives
→ 06 Korea / Vietnam Markets
→ 07 Integrated Case Studies
```

Mỗi lĩnh vực (domain / 도메인) `01–06` đều có cốt lõi (core / 핵심) chapters và ít nhất một advanced lab/ứng dụng (application / 애플리케이션) tầng (layer / 계층). `07` đã có cross-domain cases và full-process capstone. Forex hiện có thêm dedicated tuyến (route / 경로) `01–15`, institutional connections, labs và historical stress cases.

Vì vậy **next priority không phải thêm chapter lý thuyết theo chiều ngang**. Chỉ mở rộng khi tạo thêm một năng lực (capability / 역량) thực: point-in-time hiện thực (implementation / 구현), empirical trường hợp (case / 사례), dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인), quantitative lab, jurisdiction refresh hoặc cross-domain quyết định (decision / 결정) sản phẩm tạo ra (artifact / 산출물).


> **Chuyển mạch:** Từ **Kết luận hiện tại**, ta sang **1. Coverage ma trận (matrix / 행렬)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 1. Coverage ma trận (matrix / 행렬)

| lĩnh vực (domain / 도메인) | cốt lõi (core / 핵심) cơ chế (mechanism / 메커니즘) | dữ liệu (data / 데이터) / đo lường (measurement / 측정) | rủi ro (risk / 위험) / thất bại (failure / 실패) modes | Practice / trường hợp (case / 사례) | Trạng thái |
|---|---|---|---|---|---|
| 01 Foundations | money/financial hệ thống (system / 시스템), allocation, vòng đời (lifecycle / 생명주기), hành vi (behavior / 동작) | portfolio analytics, hiệu năng (performance / 성능), fees/tax | drawdown, covariance, liquidity, hành vi (behavior / 동작), stress | advanced portfolio thiết kế (design / 설계) lab | **Strong** |
| 02 Asset Classes | stocks/funds, bonds/credit, real assets, factors, cash/private markets | yield curve, spreads, NAV, carry/roll, currency | duration, credit, liquidity, embedded options, private-mark valuation | asset-pricing/portfolio lab | **Strong** |
| 03 Company phân tích (analysis / 분석) | accounting → nghiệp vụ (business / 비즈니스) chất lượng (quality / 품질) → valuation → capital allocation | filings, working capital, đơn vị (unit / 단위) economics, sector KPIs | earnings chất lượng (quality / 품질), leverage, quản trị (governance / 거버넌스), dilution, cyclicality | integrated company modeling lab | **Strong** |
| 04 Applied Economics | macro dữ liệu (data / 데이터) → chính sách (policy / 정책) → rates/liquidity/FX → assets | surprise/revisions, yield curve, credit/funding, nowcast | regime lỗi (error / 오류), chính sách (policy / 정책) expectation, liquidity-v-solvency, crisis transmission | macro transmission/nowcasting lab | **Strong, keep ranh giới (boundary / 경계) with Economics** |
| 05 Trading & Derivatives | payoff, leverage, margin, thực thi (execution / 실행), chiến lược (strategy / 전략) research, options | point-in-time dữ liệu (data / 데이터), giao dịch (transaction / 트랜잭션) costs, TCA, volatility | look-ahead, overfit, liquidity, collateral, jump/margin rủi ro (risk / 위험) | hệ thống (system / 시스템) lab + Forex labs/cases | **Strong** |
| 06 Korea / Vietnam | country balance sheet → chính sách (policy / 정책) → thị trường (market / 시장) truy cập (access / 접근) → sector/company | official macro/thị trường (market / 시장)/truy cập (access / 접근) sources | FX, custody, quyền sở hữu (ownership / 소유권), tax, liquidity, regulation | Korea/Vietnam thesis lab | **Strong but time-sensitive** |
| 07 Integrated Cases | multi-domain transmission and quyết định (decision / 결정) tiến trình (process / 프로세스) | case-specific dữ liệu (data / 데이터)/mô hình (model / 모델) inputs | cross-layer phản hồi (feedback / 피드백), portfolio mất mát (loss / 손실), vô hiệu hóa (invalidation / 무효화) | seven integrated cases + capstone | **Strong tích hợp (integration / 통합) tầng (layer / 계층)** |


> **Chuyển mạch:** Từ **1. Coverage ma trận (matrix / 행렬)**, ta sang **2. lĩnh vực (domain / 도메인) kiểm tra (audit / 감사)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. lĩnh vực (domain / 도메인) kiểm tra (audit / 감사)

### 01 — Foundations

Chuẩn gốc (canonical / 정본) chapters already cover:

```text
money / financial system
portfolio construction
lifecycle allocation
risk measurement
performance attribution
fees / tax / behavior
advanced stress / decision lab
```

This is not a candidate for more introductory portfolio lý thuyết (theory / 이론). New content is justified only if it adds a missing operational năng lực (capability / 역량) such as liability-aware hiện thực (implementation / 구현), tax/account wrapper specificity, or a materially new rủi ro (risk / 위험) khung phần mềm (framework / 프레임워크).

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

Do not split every instrument into its own tệp (file / 파일) unless legal payoff, liquidity, valuation or portfolio hành vi (behavior / 동작) is genuinely different.

### 03 — Company phân tích (analysis / 분석)

Coverage already forms a complete company-analysis chuỗi (chain / 사슬):

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

This tầng (layer / 계층) owns investment ứng dụng (application / 애플리케이션) rather than general-purpose economic lý thuyết (theory / 이론).

Hiện tại (current / 현재) tuyến (route / 경로) covers:

```text
company ↔ macro bridge
macro/global capital flows
macro data playbook
money/liquidity/crisis transmission
historical regimes/crises
fiscal–monetary interaction / debt / demographics / productivity
nowcasting and policy lab
```

General lý thuyết (theory / 이론) and econometric identification belong to [`../economics/`](../economics/README.md). Investing should continue to own **pricing, liquidity, portfolio and company transmission**.

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

Forex is now a specialization inside this lĩnh vực (domain / 도메인) rather than a missing topic.

#### Forex specialization

Chuẩn gốc (canonical / 정본) cốt lõi (core / 핵심) remains `05_trading_derivatives/forex/01–15`.

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

Do not add indicator, candlestick or “best chiến lược (strategy / 전략)” encyclopedias. New Forex content needs a new cơ chế (mechanism / 메커니즘), dataset, institutional ràng buộc (constraint / 제약조건) or hiện thực (implementation / 구현) sản phẩm tạo ra (artifact / 산출물).

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

The main rủi ro (risk / 위험) here is **staleness**, not missing lý thuyết (theory / 이론). Regulation, settlement, foreign quyền sở hữu (ownership / 소유권), tax, chỉ mục (index / 인덱스) classification, thị trường (market / 시장) truy cập (access / 접근), central-bank rules and official thị trường (market / 시장) cấu trúc (structure / 구조) must be date-stamped and rechecked before practical use.

### 07 — Integrated trường hợp (case / 사례) Studies

The trường hợp (case / 사례) tầng (layer / 계층) now spans:

```text
inflation shock
credit/liquidity crisis
Korea semiconductor cycle
Vietnam property-bank-credit cycle
full investment process capstone
macro-rates-liquidity-company-valuation-portfolio chain
USD funding / FX / Korea-Vietnam cross-border transmission
```

New cases are justified only when they stress a cơ chế (mechanism / 메커니즘) not already represented. Avoid collecting famous episodes merely for historical breadth.


> **Chuyển mạch:** Từ **2. lĩnh vực (domain / 도메인) kiểm tra (audit / 감사)**, ta sang **3. bằng chứng (evidence / 증거) and research đặc tả hợp đồng (contract / 계약)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. bằng chứng (evidence / 증거) and research đặc tả hợp đồng (contract / 계약)

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


> **Chuyển mạch:** Từ **3. bằng chứng (evidence / 증거) and research đặc tả hợp đồng (contract / 계약)**, ta sang **4. Point-in-time discipline** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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

Backtests and historical cases must not use kiến thức (knowledge / 지식) unavailable at the quyết định (decision / 결정) date unless explicitly labeled retrospective phân tích (analysis / 분석).


> **Chuyển mạch:** Từ **4. Point-in-time discipline**, ta sang **5. ranh giới (boundary / 경계) map** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. ranh giới (boundary / 경계) map

### Economics

[`../economics/`](../economics/README.md) owns general micro/macro/econometrics/economic-history lý thuyết (theory / 이론).

Investing owns:

```text
market pricing
asset/company transmission
liquidity/funding application
portfolio consequence
hedging/execution
decision artifacts
```

### Korea nghiệp vụ (business / 비즈니스) & Economy

[`../korea_business_economy_knowledge_library/`](../korea_business_economy_knowledge_library/README.md) owns Korean corporate/institution/economy kiến thức (knowledge / 지식). Investing owns securities/portfolio/valuation/truy cập (access / 접근) ứng dụng (application / 애플리케이션).

### Mathematics / Research Methods

Use chuẩn gốc (canonical / 정본) xác suất (probability / 확률)/statistics/research-design material rather than creating isolated statistical mini-textbooks inside trading chapters.

### Kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) / Khoa học máy tính (computer science / 컴퓨터 과학)

If a future systematic dự án (project / 프로젝트) needs ingestion, versioning, dữ liệu (data / 데이터) lineage, backtest engine or môi trường vận hành (production / 운영 환경) monitoring, cross-link those domains rather than turning Investing into a software-engineering thư viện (library / 라이브러리).


> **Chuyển mạch:** Từ **5. ranh giới (boundary / 경계) map**, ta sang **6. Time-sensitive refresh gates** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. Time-sensitive refresh gates

Highest refresh priority:

1. Korea/Vietnam thị trường (market / 시장) truy cập (access / 접근), foreign-room, tax, settlement and regulation.
2. Forex chapter `15` and any hiện tại (current / 현재) broker/intermediary/legal-entity claims.
3. hiện tại (current / 현재) market-size/turnover statistics and chỉ mục (index / 인덱스) methodology.
4. Macro dữ liệu (data / 데이터) sources when statistical methodology changes.
5. sản phẩm (product / 제품) conventions when benchmark, clearing or settlement standards materially thay đổi (change / 변경).

Historical cơ chế (mechanism / 메커니즘) chapters generally need slower rà soát (review / 검토) unless interpretation or nguồn (source / 소스) chất lượng (quality / 품질) changes.


> **Chuyển mạch:** Từ **6. Time-sensitive refresh gates**, ta sang **7. What should not be added next** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. What should not be added next

Do not prioritize:

- more generic investing definitions;
- indicator/candlestick catalogs;
- lists of famous investors or slogans;
- one tệp (file / 파일) per ETF/sản phẩm (product / 제품) without a new cơ chế (mechanism / 메커니즘);
- generic macro lý thuyết (theory / 이론) duplicated from Economics;
- country/company profiles that contain only hiện tại (current / 현재) facts without an analytical mô hình (model / 모델);
- “best stock / best chiến lược (strategy / 전략) / best broker” static lists.

These increase maintenance burden faster than học tập (learning / 학습) độ sâu (depth / 깊이).


> **Chuyển mạch:** Từ **7. What should not be added next**, ta sang **8. Highest-value future expansions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 8. Highest-value future expansions

Only after a concrete use trường hợp (case / 사례) appears, the strongest candidates are:

### A. Systematic hiện thực (implementation / 구현) dự án (project / 프로젝트)

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

Add only if options become an tường minh (explicit / 명시적) học tập (learning / 학습) mục tiêu (target / 대상):

```text
vol surface conventions
Greek P/L decomposition
delta-hedged P/L
event IV vs realized
skew/risk-reversal scenarios
```

### D. Point-in-time company trường hợp (case / 사례)

Use dated filings/consensus/thị trường (market / 시장) dữ liệu (data / 데이터) to produce:

```text
model
→ valuation range
→ thesis
→ position sizing
→ later attribution
```

This adds more độ sâu (depth / 깊이) than another generic DCF explanation.


> **Chuyển mạch:** Từ **8. Highest-value future expansions**, ta sang **9. Completion gate** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 9. Completion gate

Investing cốt lõi (core / 핵심) should be treated as **coverage-complete but continuously refreshable** when the learner can produce these artifacts:

```text
IPS + portfolio stress/rebalancing rules
asset-class comparison / regime map
integrated company model + valuation + invalidation
macro surprise / transmission map
cost-aware OOS strategy report + execution/risk controls
Korea/Vietnam market thesis with access constraints
cross-domain case / capstone with attribution and post-mortem
```

The thư viện (library / 라이브러리) is not “finished forever”. Completion means every major học tập (learning / 학습) năng lực (capability / 역량) has a đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자) and a đường dẫn (path / 경로) from concept to ứng dụng (application / 애플리케이션). New files must make one of those capabilities materially deeper.

> **Bàn giao:** Sau **9. Completion gate**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 GLOSSARY FORMULAS AND RESEARCH CONVENTIONS](./00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
