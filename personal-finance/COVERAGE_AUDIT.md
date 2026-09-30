# Personal Finance — Coverage, Depth & Merge-Readiness Audit

**Last reviewed:** 2026-09-30
**Scope:** `personal-finance/` canonical learning route 01–19 + `case-studies/` application layer

## Mục đích

Audit này trả lời bốn câu hỏi:

1. core financial literacy đã được bao phủ tới đâu;
2. phần nào phải giữ ở mức concept vì phụ thuộc jurisdiction/time;
3. phần mở rộng nào thực sự tăng decision skill thay vì chỉ tăng số file;
4. library đã sẵn sàng để xuất hiện trong Study Library và merge vào `main` về mặt cấu trúc hay chưa.

Tiêu chí không phải số lượng chapter. Một topic được coi là đủ core khi người đọc hiểu được:

```text
problem
→ mechanism
→ trade-off
→ failure mode
→ decision connection
→ canonical handoff khi vượt phạm vi
```

## 1. Coverage hiện tại

### 01–04 — Money, Banking, Interest, Inflation

**Trạng thái: core strong.**

Các chapter đã tạo mental model về flow/stock, liquidity, payment/deposit layer, time value of money, nominal/real value và household inflation. General monetary/macroeconomic theory không mở rộng tiếp ở đây vì canonical owner là [Economics](../economics/README.md).

Depth hiện tại đủ để đi tiếp credit/debt và major-life decisions. Mathematical appendix chỉ nên thêm khi có use case rõ như annuity, effective rate hoặc inflation-adjusted cash flow; không cần tách thêm file chỉ vì có thêm công thức.

### 05–06 — Credit, Loans & Debt

**Trạng thái: core strong.**

Đã bao phủ credit as borrowing capacity, pricing, credit-report/score concept, revolving/installment debt, amortization, secured/unsecured debt, DTI, payoff trade-off và debt structure.

Jurisdiction-specific credit-bureau rules, legal interest caps, collections, insolvency hoặc consumer procedure không thuộc core universal. Hàn Quốc được route sang [Korea Law, Civic & Everyday Life — Banking & Credit](../korea_law_civic_life/08_banking_credit_and_financial_consumer.md); Việt Nam phải kiểm tra official/legal source hiện hành khi có use case cụ thể.

### 07–08 — Insurance & Taxes

**Trạng thái: conceptual strong; implementation intentionally external/time-sensitive.**

Insurance đã có pooling, premium, deductible, coverage, exclusion, liability và risk-transfer logic. Taxes đã có gross/net, marginal/effective rate, withholding, tax-deferred/tax-advantaged concept và jurisdiction boundary.

Không biến `08-taxes.md` thành Korean/Vietnamese tax handbook. Tax rate, deduction, residency test, filing deadline và product tax treatment thay đổi theo thời gian; chỉ đưa số hiện hành khi có official source, effective date, scope và review date.

### 09–10 — Housing & Car Finance

**Trạng thái: core strong + application cases.**

Đã bao phủ total cost of ownership, financing, leverage, depreciation, maintenance, transaction cost, liquidity lock-up và buy/rent reasoning.

Korea-specific `월세/전세/보증금` legal mechanics vẫn thuộc [Korea Law, Civic & Everyday Life — Housing](../korea_law_civic_life/06_housing_wolse_jeonse_deposit_and_registration.md). Personal Finance giữ decision layer và đã bổ sung case về Korea housing, home-purchase leverage và car affordability.

### 11–12 — Retirement & Emergency Fund

**Trạng thái: core strong + cross-border application.**

Retirement đã có pension layers, compounding, longevity, sequence risk và contribution/withdrawal boundaries. Emergency fund đã có self-insurance logic, sizing heuristic, tiering, sinking-fund distinction, debt interaction, refill rule và currency/location risk.

Country-specific pension eligibility/refund/portability là time-sensitive. Chapter 16–17 và case 09 chỉ cung cấp routing/reasoning framework; rule hiện hành phải xác minh bằng nguồn chính thức.

### 13 — Financial Scams

**Trạng thái: strong and mechanism-oriented.**

Chapter ưu tiên social-engineering mechanism, payment irreversibility, phishing, remote access, impersonation, investment/recovery scam, account takeover, response workflow và data minimization thay vì catalog scam trend.

Case 06 chuyển từ prevention sang incident response: contain → secure root accounts → preserve evidence → recover liquidity → review controls.

### 14 — Personal Balance Sheet

**Trạng thái: integration strong.**

Đây là household accounting layer: assets, liabilities, net worth, liquid net worth, cash-flow bridge, savings/debt-service/emergency-coverage/leverage ratios, dashboard và decision journal.

Chapter không tiến sâu thành company accounting course. Financial statements doanh nghiệp thuộc [Investing — Company Analysis](../investing/03_company_analysis/README.md).

### 15 — Financial Resilience

**Trạng thái: advanced integration complete for core.**

Chapter thêm system property quan trọng: household có sống sót qua income/expense/rate/FX/operational shock không. Nó nối cash-flow margin, liquidity, insurance, debt structure và redundancy bằng stress test.

Đây là resilience gate trước Investing vì net worth cao không tự đồng nghĩa household có risk capacity cao.

### 16 — Korea–Vietnam Practical Map

**Trạng thái: routing/comparison layer complete.**

Chapter không duplicate luật mà định tuyến:

```text
concept
→ jurisdiction
→ official owner/source
→ contract/individual facts
```

Korea-specific implementation được cross-link sang `korea_law_civic_life/`. Nếu Việt Nam sau này có legal/civic domain đủ lớn, legal procedure nên có canonical owner riêng thay vì dồn vào Personal Finance.

### 17 — Cross-Border Personal Finance

**Trạng thái: advanced practical core complete.**

Đã bao phủ functional currency mental model, household FX exposure, currency buckets, remittance total cost, transferability, banking/KYC friction, tax-residency boundary, pension portability, emergency access, family-support obligation và cross-border balance-sheet review.

Forex trading/hedging instruments vẫn thuộc [Investing — Forex](../investing/05_trading_derivatives/forex/README.md).

### 18 — Case Studies

**Trạng thái: application layer complete for current scope.**

Case studies hiện bao phủ mười tình huống:

```text
01 six-month job loss
02 Korea housing choice
03 KRW income / VND obligations
04 debt vs investing
05 car purchase after income rise
06 financial scam incident
07 home purchase with leverage
08 family finance and childcare
09 cross-border retirement
10 death/incapacity continuity
```

Các case không tạo universal rule. Chúng luyện cùng một invariant:

```text
state
→ constraints
→ cash flow
→ balance sheet
→ liquidity
→ stress scenarios
→ options
→ second-order effects
→ decision boundary
→ review trigger
```

### 19 — Annual Financial Review

**Trạng thái: operating loop complete.**

Chapter 19 biến library từ syllabus thành system có cadence review. Nó nối cash flow, liquidity, debt, insurance, housing/car, retirement, balance sheet, resilience, fraud/security, cross-border assumptions, continuity và goals thành một annual operating loop.

Annual review kết thúc bằng **investable-surplus gate**, sau đó mới handoff sang [Investing](../investing/README.md).

## 2. Canonical ownership boundaries

Library này chỉ bền nếu giữ ownership rõ:

```text
Personal Finance
→ household cash flow, debt, insurance, major purchases,
  retirement planning, liquidity, resilience,
  cross-border household exposure, life-cycle decisions and review loop

Economics
→ general micro/macro mechanism, monetary policy,
  inflation formation, labor/growth/market theory

Investing
→ asset allocation, securities, valuation, portfolio risk,
  stocks, bonds, derivatives, Forex trading/hedging

Korea Law, Civic & Everyday Life
→ Korean legal/procedural implementation for housing,
  tax/social insurance, banking/credit and consumer rights
```

Nếu một file mới không có owner rõ hoặc lặp phần lớn nội dung từ owner khác, ưu tiên cross-link thay vì tạo file.

## 3. Time-sensitive content policy

Các dữ liệu sau không được hard-code như “kiến thức vĩnh viễn” nếu không có metadata thời điểm:

- tax rates, deductions, brackets và filing deadlines;
- deposit-insurance limits;
- credit-score thresholds hoặc lender eligibility rules;
- legal interest caps;
- pension contribution/benefit/refund country lists;
- social-insurance eligibility theo nationality/visa;
- mortgage/consumer-loan regulatory ratios;
- government subsidies và housing programs;
- scam hotline/procedure khi cơ quan hoặc workflow có thể thay đổi.

Khi cần ghi số/rule hiện hành:

```text
official source
+ jurisdiction
+ effective date
+ population/product scope
+ last-reviewed date
```

Nếu thiếu metadata này, ưu tiên mechanism + routing thay vì biến một snapshot thành canonical rule.

## 4. Publication / Study Library audit

Study Library không publish mọi root folder tự động. Canonical publication manifest là [`../learning-library/library.config.json`](../learning-library/library.config.json).

`personal-finance/` hiện đã có prefix publication riêng:

```text
path: personal-finance
category: Personal Finance
language: vi-en-ko
rights: author-confirmed
```

Điều này quan trọng vì build script chỉ discover Markdown khi file nằm trong `allowedPrefixes` hoặc `allowedDocuments`. PDF vẫn cần explicit per-file permission entry theo publishing policy.

Route được đối chiếu với branch tree hiện tại:

```text
README.md
01–19
COVERAGE_AUDIT.md
case-studies/README.md
case-studies/01–10
```

Tất cả các target chính trong learning route hiện có file tương ứng trên branch.

## 5. Internal-link audit

Các nhóm link quan trọng đã được đối chiếu theo canonical path:

```text
01–19 → personal-finance/*
18 → case-studies/README.md + case 01–10
Personal Finance → economics/README.md
Personal Finance → investing/README.md
Personal Finance → korea_law_civic_life/*
17 → investing/05_trading_derivatives/forex/README.md
14 → investing/03_company_analysis/README.md
```

Các owner target trên đều nằm trong prefix đã được Study Library publish. Build script tạo graph bằng cách resolve relative Markdown path trên tập document đã publish; việc thêm `personal-finance` vào manifest vì thế cũng cần thiết để các node/edge của domain xuất hiện trong graph.

## 6. Repo-wide reverse connections

`CATALOG.md` hiện khai báo reciprocal `related` metadata giữa `personal_finance` và ba owner chính:

```text
personal_finance ↔ economics
personal_finance ↔ investing
personal_finance ↔ korea_law_civic_life
```

Ở document level, Personal Finance đã có outbound links trực tiếp sang cả ba domain. Không cần duplicate theory chỉ để tạo thêm reverse prose; khi sửa README của owner khác trong một batch tương lai, có thể thêm contextual back-link nếu nó cải thiện learning route thực tế.

## 7. External-source verification

Các nguồn OECD 2026 dùng trong library đã được kiểm tra lại ngày 2026-09-30 theo trang xuất bản chính thức.

Tên chuẩn cần dùng là:

- OECD, *OECD/INFE Toolkit for Measuring Financial Literacy, Inclusion and Well-Being 2026*.
- OECD, *Consumer Finance Risk Monitor 2026*.

Không dùng biến thể thiếu `Well-Being` trong title của Toolkit.

## 8. Expansion candidates sau core

Core hiện không cần thêm chapter chỉ để tăng breadth. Chỉ mở thêm khi có use case rõ, ví dụ:

### Career and income risk

Income diversification, unemployment transition, compensation/benefit reading hoặc self-employment cash-flow volatility. Nên cross-link labor economics/career docs nếu repo có owner phù hợp.

### Estate / inheritance / incapacity planning

Case 10 đã bao phủ continuity framework. Will, power of attorney, inheritance, beneficiary law và probate vẫn rất jurisdiction-dependent; nếu mở sâu phải có legal owner/boundary rõ.

### Education and caregiving finance

Case 08 đã bao phủ household-capacity logic. Tuition, childcare subsidy, eldercare benefit hoặc country-specific program chỉ nên thêm khi có official/time-sensitive source.

### Self-employment / small-business boundary

Nếu mở, cần tách personal cash flow với business cash flow, tax reserve, liability và working capital; không để Personal Finance biến thành small-business accounting.

## 9. Những thứ không nên thêm vào `personal-finance/`

Không mở rộng library bằng:

- stock picking, ETF catalog, portfolio optimization hoặc market timing;
- Forex strategy/backtest;
- company accounting/valuation;
- macro forecasting;
- full Korean/Vietnamese tax code;
- full housing law handbook;
- danh sách sản phẩm ngân hàng đang bán;
- “top credit card/best loan” recommendation theo thời điểm.

Các nội dung đó thuộc owner khác hoặc thay đổi quá nhanh để làm canonical foundation.

## 10. Completion gate

Về cấu trúc, library đạt gate khi:

```text
README chứa 01–19
→ 14 handoff sang 15, 15 → 16 → 17 → 18 → 19
→ case-studies/ có index và canonical back-links
→ publication manifest chứa personal-finance prefix
→ target chính của internal links tồn tại
→ jurisdiction-specific rule có boundary/source rõ
→ Economics/Investing/Korea Law ownership không bị duplicate
→ annual review xác định investable-surplus handoff
→ coverage audit phản ánh route hiện tại
```

Sau gate này, ưu tiên **prose/terminology polish, build verification và merge review** hơn tiếp tục tăng số file.

## Nguồn định hướng coverage

- OECD Financial Education: https://www.oecd.org/en/topics/financial-education.html
- OECD, *OECD/INFE Toolkit for Measuring Financial Literacy, Inclusion and Well-Being 2026*: https://www.oecd.org/en/publications/oecd-infe-toolkit-for-measuring-financial-literacy-inclusion-and-well-being-2026_92f2d439-en.html
- OECD, *Consumer Finance Risk Monitor 2026*: https://www.oecd.org/en/publications/consumer-finance-risk-monitor-2026_61f7dbe0-en.html
- Khan Academy Financial Literacy: https://www.khanacademy.org/college-careers-more/financial-literacy
- CFPB Consumer Tools: https://www.consumerfinance.gov/consumer-tools/
