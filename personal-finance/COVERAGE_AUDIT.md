# Personal Finance — Coverage & Depth Audit

**Last reviewed:** 2026-09-30  
**Scope:** `personal-finance/` canonical learning route 01–19 plus `case-studies/`

## Mục đích

Audit này trả lời ba câu hỏi: core financial literacy đã được bao phủ tới đâu, phần nào cần giữ ở mức concept vì phụ thuộc jurisdiction/time, và expansion tiếp theo có thật sự lấp khoảng trống hay chỉ làm library phình ra.

Tiêu chí không phải số lượng file. Một topic được coi là đủ core khi người đọc hiểu được **problem → mechanism → trade-off → failure mode → decision connection**, đồng thời biết khi nào phải chuyển sang canonical owner khác.

## Trạng thái coverage

### 01–04 — Money, Banking, Interest, Inflation

**Trạng thái: core strong.**

Các chapter đã tạo mental model về flow/stock, liquidity, payment/deposit layer, time value of money, nominal/real value và household inflation. General monetary/macro theory không tiếp tục mở rộng ở đây vì owner là [Economics](../economics/README.md).

Depth gate hiện tại đã đủ cho việc đọc tiếp credit/debt và các quyết định lớn. Chỉ nên thêm mathematical appendix nếu sau này có nhu cầu tính annuity, effective rate hoặc inflation-adjusted cash flow sâu hơn; không cần tách thêm file chỉ vì công thức.

### 05–06 — Credit, Loans & Debt

**Trạng thái: core strong.**

Đã bao phủ credit as borrowing capacity, pricing, score/reporting concept, revolving/installment debt, amortization, secured/unsecured debt, DTI, payoff trade-off và debt structure.

Jurisdiction-specific credit bureau rules, legal interest cap, collections, insolvency hoặc consumer procedure không thuộc core universal. Hàn Quốc cross-link sang [`korea_law_civic_life/08_banking_credit_and_financial_consumer.md`](../korea_law_civic_life/08_banking_credit_and_financial_consumer.md); Việt Nam cần official/legal source hiện hành khi có use case cụ thể.

### 07–08 — Insurance & Taxes

**Trạng thái: conceptual strong; implementation intentionally external/time-sensitive.**

Insurance đã có pooling, premium, deductible, coverage, exclusion, liability và risk-transfer logic. Taxes đã có gross/net, marginal/effective rate, withholding, tax-advantaged/deferred concept và jurisdiction boundary.

Không nên biến `08-taxes.md` thành Korean/Vietnamese tax handbook. Rate, deduction, residency tests, filing deadline và product tax treatment thay đổi theo thời gian; chỉ thêm khi có effective date, official source và review owner rõ.

### 09–10 — Housing & Car Finance

**Trạng thái: core strong + application depth added.**

Đã bao phủ total cost of ownership, financing, leverage, depreciation, maintenance, transaction cost, liquidity lock-up và buy/rent reasoning. Korea-specific `월세/전세/보증금` legal mechanics được chuyển sang Korea Law/Civic Life thay vì duplicate.

Application layer hiện có cả [Korea housing structure](./case-studies/02-korea-housing-choice.md), [home leverage](./case-studies/07-home-purchase-leverage.md) và [car affordability](./case-studies/05-car-purchase-income-rise.md). Vì vậy không cần mở thêm catalog xe hoặc bất động sản theo thị trường.

### 11–12 — Retirement & Emergency Fund

**Trạng thái: core strong + cross-border application added.**

Retirement đã có pension layers, compounding, longevity, sequence risk và contribution/withdrawal boundaries. Emergency fund đã có self-insurance logic, sizing range, tiering, sinking fund distinction, debt interaction, refill rule và currency/location risk.

Country-specific pension eligibility/refund/portability là time-sensitive. Korea/Vietnam source routing nằm ở chapter 16–17; [cross-border retirement case](./case-studies/09-cross-border-retirement.md) dùng portability/accessibility như application mà không hard-code entitlement rule.

### 13 — Financial Scams

**Trạng thái: strong and current-mechanism oriented.**

Chapter ưu tiên social-engineering mechanism, payment irreversibility, phishing, remote access, impersonation, investment/recovery scam, account takeover, response workflow và data minimization thay vì catalog scam trend.

[Scam incident case](./case-studies/06-financial-scam-incident.md) đã bổ sung containment/recovery layer. Đây là hướng đúng vì kịch bản lừa đảo thay đổi nhanh; không biến canonical chapter thành news feed.

### 14 — Personal Balance Sheet

**Trạng thái: integration strong.**

Đây là system accounting layer: assets, liabilities, net worth, liquid net worth, cash-flow bridge, savings/debt-service/emergency coverage/leverage ratios, dashboard và decision journal.

Chapter không nên tiến sâu thành accounting course. Financial statements doanh nghiệp thuộc [Investing — Company Analysis](../investing/03_company_analysis/README.md).

### 15 — Financial Resilience

**Trạng thái: advanced integration complete for core.**

Chapter thêm missing system property: household có sống sót qua income/expense/rate/FX/operational shock không. Nó nối cash-flow margin, liquidity, insurance, debt structure và redundancy bằng stress test.

Đây là layer cần thiết trước Investing vì net worth cao không tự đồng nghĩa household có risk capacity cao.

### 16 — Korea–Vietnam Practical Map

**Trạng thái: routing/compare layer complete.**

Chapter không duplicate luật mà định tuyến concept → jurisdiction → official owner/source → contract. Nó nêu rõ Korea-specific canonical owners trong repo và framework tương ứng cho Việt Nam.

Khi mở rộng về Việt Nam sau này, nên ưu tiên tạo một domain civic/legal Vietnam riêng nếu scope đủ lớn, thay vì dồn legal procedure vào Personal Finance.

### 17 — Cross-Border Personal Finance

**Trạng thái: advanced practical core complete.**

Đã bao phủ functional currency mental model, household FX exposure, currency buckets, remittance total cost, transferability, banking/KYC friction, tax-residency boundary, pension portability, emergency access, family support obligation và cross-border balance-sheet review.

Forex trading/hedging instrument mechanics vẫn thuộc [`investing/05_trading_derivatives/forex/`](../investing/05_trading_derivatives/forex/README.md).

### 18 — Case Studies

**Trạng thái: application layer strong.**

Case route hiện bao phủ hai lớp.

Operational/near-term:

```text
01 job loss
02 Korea housing structure
03 KRW income / VND obligations
04 debt vs investing
05 car affordability
06 scam incident
```

Life-cycle/advanced:

```text
07 home purchase leverage
08 family + child
09 cross-border retirement
10 death/incapacity continuity
```

Các case không tạo universal rule. Chúng dùng explicit assumptions, adverse scenarios, trade-off và decision boundary để buộc người đọc nối nhiều canonical concepts trong cùng một tình huống.

### 19 — Annual Financial Review

**Trạng thái: operating loop complete.**

Chapter 19 biến library từ syllabus thành system có cadence. Nó reconcile cash flow, liquidity, debt, insurance, housing/car, retirement, balance sheet, resilience, fraud/account security, cross-border assumptions, continuity và investable-surplus gate.

Annual review còn định nghĩa off-cycle triggers như job loss/change, marriage/divorce, birth/death, country move, major housing/debt transaction hoặc fraud incident. Vì vậy knowledge route hiện có cả learning loop lẫn operational maintenance loop.

## Canonical ownership boundaries

Library này chỉ bền nếu giữ ownership rõ:

```text
Personal Finance
→ household cash flow, debt, insurance, major purchases,
  retirement planning, liquidity, resilience, cross-border household exposure,
  life-cycle financial decisions and household operating review

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

Nếu một file mới không có owner rõ hoặc lặp hơn nửa nội dung từ owner khác, ưu tiên cross-link thay vì tạo file.

## Time-sensitive content policy

Các dữ liệu sau không nên hard-code như “kiến thức vĩnh viễn” nếu không có effective date và source:

- tax rates, deductions, brackets và filing deadlines;
- deposit-insurance limits;
- credit-score thresholds hoặc lender eligibility rules;
- legal interest caps;
- pension contribution/benefit/refund country lists;
- social-insurance eligibility theo nationality/visa;
- mortgage/consumer-loan regulatory ratios;
- government subsidies và housing programs;
- scam hotline/procedure nếu cơ quan đã thay đổi.

Khi buộc phải đưa số hiện hành vào learning doc:

```text
official source
+ jurisdiction
+ effective date
+ population/product scope
+ last-reviewed date
```

Nếu thiếu một trong các field này, ưu tiên giải thích mechanism và link owner thay vì ghi con số.

## Repo-wide connections còn cần giữ

Personal Finance nên có internal links theo mechanism, không chỉ ở README:

- opportunity cost, inflation, interest → [Economics](../economics/README.md);
- investable surplus, asset allocation, securities, Forex → [Investing](../investing/README.md);
- Korean housing/tax/banking procedure → [Korea Law, Civic & Everyday Life](../korea_law_civic_life/README.md);
- scam/social engineering → có thể cross-link [Psychology](../psychology/README.md) khi cần behavioral mechanism sâu hơn;
- probability/risk/expected value → nên nối sang `thinking/` khi domain này trở thành canonical trên `main`.

Không tạo broken link tới branch-only domain khác cho đến khi path đó tồn tại trong cùng merge set hoặc trên main.

## Expansion candidates sau core

Core và application loop hiện đã khá hoàn chỉnh. Chỉ mở thêm domain/chapter nếu có demand rõ.

### Household governance sâu hơn

Case 08 đã có joint/separate/hybrid account logic, one-income stress và dependent risk. Một chapter riêng chỉ đáng tạo nếu cần đi sâu financial communication, shared responsibility, household contracts hoặc multi-generational support.

### Career and income risk

Job-loss case đã cover acute shock. Một chapter riêng có thể có giá trị nếu cần compensation/benefit reading, income diversification, career breaks, self-employment volatility và human-capital risk. Nên cross-link labor economics/career docs nếu repo có owner phù hợp.

### Estate / inheritance / incapacity planning

Case 10 đã cover operational continuity và single-person dependency. Will, inheritance, power of attorney, probate và beneficiary law vẫn rất jurisdiction-dependent; chỉ mở legal-depth content khi có canonical legal owner rõ.

### Education and caregiving finance

Case 08 mới cover child-related household transition ở mức system. Tuition, long-term education funding, eldercare và extended-family support có thể được bổ sung khi có use case thực tế.

### Self-employment / small-business boundary

Cần tách personal cash flow với business cash flow, tax reserve, liability và working capital. Chỉ mở nếu repo chưa có business-finance owner phù hợp.

## Những thứ không nên thêm vào `personal-finance/`

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

## Completion gate hiện tại

Library có thể coi là structurally complete khi:

```text
README chứa 01–19
→ 14 handoff sang 15, 15 → 16 → 17 → 18 → 19
→ case-studies/ có index và canonical back-links
→ mọi internal link trong personal-finance resolve
→ jurisdiction-specific rule có boundary/source rõ
→ không duplicate Economics/Investing/Korea Law
→ annual review xác định investable-surplus handoff
→ coverage audit được cập nhật khi thêm major chapter
```

Sau gate này, ưu tiên **link validation, prose/terminology consistency, reverse cross-links và merge readiness** hơn tiếp tục tăng số file.

## Nguồn định hướng coverage

- OECD Financial Education: https://www.oecd.org/en/topics/financial-education.html
- OECD/INFE Toolkit for Measuring Financial Literacy and Financial Inclusion 2026.
- OECD Consumer Finance Risk Monitor 2026.
- Khan Academy Financial Literacy: https://www.khanacademy.org/college-careers-more/financial-literacy
- CFPB Consumer Tools: https://www.consumerfinance.gov/consumer-tools/
