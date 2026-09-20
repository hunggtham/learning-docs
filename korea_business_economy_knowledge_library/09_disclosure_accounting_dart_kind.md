# Disclosure, accounting, DART và KIND: cách biến một công ty thành dữ liệu có thể kiểm chứng (기업공시·회계·DART·KIND)

Muốn đi từ “nghe nói company này tốt” sang analysis có thể kiểm chứng, phải biết **company bắt buộc hoặc tự nguyện công bố gì, ở đâu, theo accounting boundary nào và bằng wording pháp lý nào**.

Ở Korea, hai infrastructure quan trọng nhất là **DART (전자공시시스템)** của Financial Supervisory Service và **KIND (한국거래소 기업공시채널)** của Korea Exchange. Đây không chỉ là websites để đọc report; chúng là public information infrastructure của capital market.

## Disclosure tồn tại vì information asymmetry

Management biết nhiều hơn investor, lender, employee, supplier và public. Đây là **information asymmetry / 정보비대칭**.

Nếu outsider không thể verify revenue, debt hay related-party transaction, cost of capital tăng vì uncertainty và adverse-selection risk.

Disclosure reduces this gap by creating:

- standardized filing requirements;
- deadlines;
- legal responsibility;
- audit trails;
- historical comparability;
- machine-readable structures in some datasets.

Disclosure does **not** eliminate fraud or judgment. It creates evidence that can be challenged and reconciled.

> Mental model: filing is not “truth oracle”; it is a structured claim under legal/accounting accountability.

## DART và KIND giải quyết problem khác nhau

**DART** is broad repository for corporate filings under FSS. It is especially useful for business reports, financial statements, ownership changes, financing, M&A, major events and historical filing search.

**KIND** is KRX disclosure channel focused on listed-company market disclosures, listing information, trading-related notices and exchange context.

For listed company research, best workflow is not `DART or KIND`; it is **DART + KIND + company IR**.

DART gives legal/financial depth; KIND gives exchange-event flow; IR gives management narrative.

## Filing hierarchy: document nào trả lời câu hỏi nào?

### 사업보고서 — Annual Business Report

This is the closest thing to an annual company “database snapshot”. It can include:

- company history;
- business segments;
- major products/services;
- sales channels;
- raw materials;
- production capacity;
- subsidiaries;
- employees;
- directors;
- shareholders;
- related parties;
- litigation/contingencies;
- financial statements and notes.

Do not open only financial tables. For industrial company, capacity/raw-material section may explain margin better than headline earnings.

### 반기보고서 / 분기보고서

Half-year and quarterly reports update financial and business data between annual filings.

They are essential for cycle analysis because industrial conditions can move far faster than annual reporting.

### 주요사항보고서 and material disclosures

These can cover material events such as:

- capital increase;
- bond issuance;
- major asset acquisition/disposal;
- M&A;
- restructuring;
- major contracts;
- guarantees or financing events depending on rules.

If company story changes sharply, search material-event filings rather than waiting for annual report.

### Ownership filings

Large-shareholder and officer ownership changes can reveal control changes, succession steps or insider transactions.

Ownership disclosure is especially important for chaebol/group analysis.

## First principle: identify the correct accounting boundary

Before reading any number, ask: **which entity and which scope?**

A group may have:

- standalone/separate statements (별도재무제표);
- consolidated statements (연결재무제표);
- subsidiaries;
- associates under equity method;
- joint ventures.

Same brand can produce multiple valid revenue/profit numbers depending on boundary.

This is not accounting inconsistency. It is different question scope.

## Separate vs consolidated statements

**Separate statements / 별도재무제표** describe one legal entity.

**Consolidated statements / 연결재무제표** treat parent and controlled subsidiaries as one economic reporting group and eliminate intra-group transactions.

Suppose Parent sells components worth 100 to Subsidiary, then Subsidiary sells finished product 150 to external customer.

Naively adding standalone revenue gives 250, but consolidated external revenue should reflect 150 after eliminating internal 100.

This is why consolidated accounting exists.

## Consolidation does not mean parent owns 100%

If Parent owns 70% of Subsidiary but controls it, consolidated statements may include 100% of subsidiary assets/revenue, with outside ownership represented as **Non-Controlling Interest (NCI / 비지배지분)**.

Therefore analyst must distinguish:

- consolidated net income;
- net income attributable to owners of parent;
- net income attributable to NCI.

Using 100% of subsidiary EBITDA while ignoring minority ownership can overstate parent-shareholder value.

## The balance sheet: stock of economic resources and claims

Statement of Financial Position (재무상태표) follows basic identity:

\[
Assets = Liabilities + Equity
\]

But analysis is not about checking equation. Need ask quality of each line.

### Cash

Is cash unrestricted? Is it held at subsidiaries? Does company also have large debt?

Gross cash alone does not equal parent-level free cash.

### Receivables

Receivables rising faster than revenue can mean slower collections, customer stress or aggressive recognition.

Useful metric:

\[
DSO = \frac{Average\ Receivables}{Revenue} \times 365
\]

Compare over time and against business model.

### Inventory

Inventory can be strategic buffer or warning sign.

In semiconductor, inventory build may precede price pressure. In retail, old inventory may require markdown. In shipbuilding, work-in-progress economics differ again.

Need interpret inventory by industry.

### Property, plant and equipment

PP&E shows accumulated physical capacity but not necessarily productive value.

A new fab increases assets and future depreciation. If utilization stays low, same capex can destroy return on capital.

### Intangibles and goodwill

M&A can create goodwill. Goodwill is not automatically bad, but future impairment may reveal acquisition assumptions were too optimistic.

## Income statement: flow of economic performance

A simplified bridge:

```text
Revenue
- Cost of sales
= Gross profit
- Operating expenses
= Operating profit
± Finance / other items
= Profit before tax
- Tax
= Net income
```

Different industries present details differently, but logic remains.

## Revenue growth decomposition

Revenue increase can come from:

\[
Revenue = Volume \times Price \times Mix\ Effect
\]

For platform, replace volume with transactions/users; for bank, revenue logic differs; for construction, recognition depends project progress.

Therefore headline growth needs mechanism.

## Operating profit vs net income

**Operating profit / 영업이익** focuses more on core operations.

**Net income / 당기순이익** includes financing cost, taxes and many non-operating effects.

A company can report high net income from asset sale while operating business weakens.

Conversely high interest expense can depress net income even when operations stable.

Always bridge the two rather than selecting whichever looks better.

## Accrual accounting: profit is not cash by design

Accounting recognizes economic activity when earned/incurred under rules, not only when cash moves.

Suppose product ships today but customer pays after 60 days. Revenue can be recognized before cash arrives, creating accounts receivable.

This is **accrual accounting / 발생주의 회계**.

Accrual is necessary for meaningful period performance, but it creates room for timing and estimation judgments.

## Cash Flow Statement: where liquidity reality appears

Cash flow is grouped into:

- Operating Cash Flow (영업활동현금흐름);
- Investing Cash Flow (투자활동현금흐름);
- Financing Cash Flow (재무활동현금흐름).

Net income and CFO differ because of depreciation, working capital, provisions and non-cash items.

A useful reconciliation mindset:

```text
Net income
+ non-cash expenses
± working-capital changes
± other adjustments
= Operating cash flow
```

If net income grows for years while CFO consistently lags without clear reason, investigate.

## Working capital: growth consumes cash

Fast-growing company often needs inventory and receivables before customer cash arrives.

Cash Conversion Cycle:

\[
CCC = DIO + DSO - DPO
\]

where DIO = inventory days, DSO = receivable days, DPO = payable days.

A company can be profitable but cash-hungry because CCC expands.

This is particularly important for exporters, retailers, manufacturers and project businesses.

## CAPEX and Free Cash Flow

Capital expenditure often appears in investing cash flow.

A simple analyst definition:

\[
FCF \approx CFO - CAPEX
\]

But FCF is not a statutory line and definitions vary.

Need distinguish:

- maintenance CAPEX;
- growth CAPEX.

Negative FCF from growth capex can be healthy if future ROIC strong. Negative FCF from weak operations is different problem.

## Depreciation: non-cash today, but not “free”

Depreciation is non-cash in current period because cash was spent when asset purchased.

But treating depreciation as irrelevant is wrong. It represents consumption of capital asset over time.

Capital-intensive firm that ignores replacement investment can report cash temporarily while productive base ages.

This is why EBITDA alone is dangerous in semiconductor, telecom, utility or heavy industry.

## Segment reporting: consolidated total can hide economics

Large Korean groups often have multiple segments with radically different margins and capital intensity.

Need map:

```text
Segment Revenue
Segment Operating Profit
Segment Assets / CAPEX
Geography
Major customers if disclosed
```

If 30% of revenue creates 70% of profit, that segment is economic engine.

Group-level average can hide both growth business and value-destroying segment.

## Equity-method associates

If investor has significant influence but not control, investment may be accounted using equity method rather than full consolidation.

This affects presentation: investor may recognize share of profit without including associate’s full revenue.

Therefore company can have economically important business not visible in consolidated revenue.

Read notes to avoid missing such exposure.

## Footnotes: where economic risk often lives

Notes may reveal:

- debt maturity;
- guarantees;
- derivatives;
- related-party balances;
- pension obligations;
- litigation;
- lease liabilities;
- commitments;
- construction/PF exposure;
- accounting estimates;
- revenue-recognition policies.

Headline balance sheet can look simple while notes contain substantial contingent obligations.

For construction, guarantees can matter more than recognized borrowing. For exporter, hedge contracts can change FX sensitivity.

## Contingent liability: risk before recognition

A guarantee may not yet be recognized as full debt if trigger has not occurred, but economically it can become future cash obligation.

This creates distinction:

```text
Accounting liability today
        ≠
Maximum economic exposure under stress
```

Stress-test both.

## Revenue recognition in long-duration projects

Construction, shipbuilding and some SI projects recognize revenue over time when accounting criteria are met.

Profit depends on estimates of total cost and progress.

If expected total project cost rises, margin can be revised before delivery.

Therefore contract asset/liability and estimate revisions deserve attention.

## Financial-company accounting requires different mental model

Banks, insurers and securities firms cannot be analyzed with industrial-company template alone.

For banks, loans are earning assets and deposits are funding liabilities. Interest margin, credit loss and capital adequacy matter more than classic inventory/capex.

For insurers, liability duration and investment assets matter.

Use industry-specific accounting rather than forcing one ratio system on all firms.

## Audit opinion: what it means and what it does not

External audit assesses whether financial statements are presented fairly in material respects under applicable accounting framework.

Possible serious signals include qualified, adverse or disclaimer opinions.

But **unqualified opinion does not guarantee business quality or eliminate fraud risk**. Audit provides reasonable assurance, not omniscience.

Also inspect Key Audit Matters where available to see areas requiring significant judgment.

## Restatement / 정정공시

Companies can issue corrected filings.

Never read only latest corrected number and ignore change history. Ask:

- What was corrected?
- Why?
- Is effect material?
- Does correction change trend or covenant?
- Was it clerical, estimation or control failure?

Restatement itself is data about reporting quality.

## DART as database: build query habit

Do not browse DART randomly. Start with a question.

If question is `Who controls company?` → ownership filings + annual report.

If `Why debt jumped?` → financing/major-event filings + notes.

If `What business actually earns profit?` → segment notes.

If `What happened to subsidiary?` → consolidation/subsidiary tables + M&A filings.

Research becomes faster when document choice follows question.

## OPEN DART and XBRL: accounting meets programming

Structured data allows automated analysis.

XBRL (eXtensible Business Reporting Language / 확장성 경영보고언어) tags financial concepts so software can parse them.

This enables:

- time-series extraction;
- cross-company comparison;
- screening;
- anomaly detection;
- automated ratio calculation.

But tag comparability is not perfect. Companies can use extension tags and accounting policies differ.

Programmatic data must still be validated against original filing.

## Korean vs English filing

English disclosure may be useful for access, but Korean filing should be preferred when legal accuracy or nuance matters.

Translation can omit detail or be voluntary in scope. For technical/legal term, check original Korean phrase.

This library therefore often notes Korean keywords alongside English/Vietnamese.

## Filing chronology: event time vs reporting time

A business event happens at time `t`, management may disclose immediately or later depending rule, quarterly financial effect may appear at `t+1`, cash effect may appear later.

Analyst must align timeline.

Example:

```text
Contract signed
   ↓
Material disclosure
   ↓
Production starts
   ↓
Revenue recognized
   ↓
Cash collected
```

Do not equate contract announcement with earnings or cash.

## Practical workflow for a new Korean company

### Step 1 — Resolve identity

Confirm exact Korean legal name, ticker, corporation code, group and consolidation boundary.

### Step 2 — Read latest 사업보고서

Start with business, segments and subsidiaries before financial tables.

### Step 3 — Build 5-year financial bridge

Extract revenue, operating profit, net income, CFO, CAPEX, debt, cash and share count.

### Step 4 — Reconcile profit and cash

Track receivables, inventory and working capital.

### Step 5 — Read notes

Debt maturity, guarantees, related parties, derivatives, commitments.

### Step 6 — Search major-event filings

M&A, financing, capital increase, restructuring, large contracts.

### Step 7 — Use KIND

Check listing/trading/corporate-action context.

### Step 8 — Compare with IR narrative

Treat management presentation as hypothesis and reconcile with filing evidence.

## Red flags that deserve investigation, not automatic conviction

Potential red flags include:

- receivables growing much faster than revenue;
- persistent CFO below earnings;
- large related-party balances;
- repeated capital raises despite claimed profitability;
- frequent accounting corrections;
- opaque guarantees;
- sudden changes in accounting policy;
- inventory build without demand explanation;
- major profit from one-off items;
- large goodwill after aggressive M&A.

None proves fraud. They signal need for deeper work.

## Mental Model

> Disclosure is the **public API of a corporation**. Financial statements are structured outputs; footnotes are metadata; material filings are event logs; audit is a validation layer; DART/KIND are the retrieval infrastructure. Good company analysis is data reconciliation across all layers, not reading one headline ratio.

## Common misconceptions

Revenue growth does not prove cash growth.

Net income is not cash flow.

EBITDA is not free cash flow.

Consolidated cash is not automatically freely available to parent shareholder.

Low recognized debt does not mean low economic leverage if guarantees/commitments are large.

Unqualified audit opinion does not mean company is a good investment.

DART filing is primary evidence, but accounting still contains estimates and judgment.

## Connections

Use [08_corporate_governance_ownership_and_control](./08_corporate_governance_ownership_and_control.md) for ownership/governance questions, [10_capital_markets_kospi_kosdaq_konex](./10_capital_markets_kospi_kosdaq_konex.md) for market interpretation and [20_how_to_analyze_a_korean_company](./20_how_to_analyze_a_korean_company.md) as end-to-end workflow.

### Nguồn thực hành

- DART: https://dart.fss.or.kr/
- English DART: https://englishdart.fss.or.kr/
- KIND: https://kind.krx.co.kr/
