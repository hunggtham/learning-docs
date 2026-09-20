# Startup, venture và scale-up Hàn Quốc (Startup & Venture / 스타트업·벤처기업·스케일업)

Startup thường bị trộn với SME vì cả hai có thể nhỏ, ít nhân viên và chưa niêm yết. Nhưng logic kinh tế của hai loại rất khác. **SME / 중소기업** là phân loại quy mô hoặc policy/legal category; **startup / 스타트업** là tổ chức đang tìm hoặc mở rộng một business model có khả năng scale nhanh trong điều kiện uncertainty cao.

Một small restaurant có thể là SME nhưng không phải venture startup. Một software company 30 người có thể là startup nếu product có thể phục vụ 100.000 customers mà cost không tăng gần tuyến tính theo headcount.

## Startup là bài toán uncertainty, không chỉ size

Doanh nghiệp truyền thống thường đã biết khá rõ mình bán gì, ai mua và margin khoảng bao nhiêu. Startup thường chưa chắc product, pricing, acquisition channel, customer segment hoặc distribution model nào sẽ work.

Vì vậy early-stage startup ưu tiên **learning speed / 학습속도** hơn optimization tuyệt đối.

Một useful sequence:

```text
Problem hypothesis
      ↓
Prototype / MVP
      ↓
Customer behavior
      ↓
Retention / willingness to pay
      ↓
Product-market fit
      ↓
Repeatable acquisition
      ↓
Scale-up
```

Nếu company scale spending trước khi product-market fit, nó có thể scale acquisition cost và losses thay vì scale value.

## Product-market fit: customer behavior quan trọng hơn founder conviction

**Product-Market Fit (PMF / 제품-시장 적합성)** nghĩa là product giải problem đủ mạnh để customer repeatedly use, pay, recommend hoặc resist switching.

PMF không có một official metric duy nhất. Evidence có thể gồm:

- retention curve flattening;
- repeat purchase;
- organic referrals;
- declining churn;
- strong usage intensity;
- willingness to pay;
- improving sales efficiency.

Downloads hoặc sign-ups chỉ đo curiosity. Startup khỏe phải chứng minh **persistent customer value**.

## MVP: mục tiêu là học, không phải làm product “rẻ”

Minimum Viable Product (MVP / 최소기능제품) thường bị hiểu là “version sơ sài nhất”. Mental model tốt hơn: MVP là **phiên bản nhỏ nhất có thể kiểm tra một uncertainty quan trọng**.

Nếu uncertainty là “customer có trả tiền không?”, MVP phải test payment. Nếu uncertainty là technical feasibility, prototype có thể không cần polished UX.

Do đó MVP design phải bắt đầu từ hypothesis, không phải từ list features.

## Why venture capital exists

Startup có three characteristics làm bank debt less suitable ở early stage:

1. cash flow chưa ổn định;
2. collateral hữu hình ít;
3. distribution outcome rất skewed — many failures, few huge winners.

Bank earns limited upside from loan interest but bears default downside. Venture investor accepts equity risk because upside is uncapped.

Venture capital therefore fits **power-law outcomes / 멱법칙형 수익구조** better than normal lending.

## Equity financing và dilution

When startup issues new shares, old owners' percentage falls unless they invest proportionally.

Nếu founder owns 100%, then two rounds each sell 20% post-money:

\[
1.0 \times 0.8 \times 0.8 = 64\%
\]

Không phải 60%, vì dilution compounds multiplicatively.

Option pool, convertible securities, SAFE-like instruments where applicable, preferred shares và warrants can make fully diluted ownership more complex.

Headline founder stake therefore should be read from **fully diluted cap table**, not basic shares only.

## Pre-money và post-money valuation

Nếu investor invests 20 billion KRW at 80 billion pre-money valuation:

\[
Post\ Money = 80 + 20 = 100
\]

Investor owns roughly:

\[
\frac{20}{100}=20\%
\]

Valuation is an implied transaction price for equity; it is **not cash in the bank**. Company receives only financing amount, not full post-money valuation.

This is one of the most common startup misunderstandings.

## Preferred shares: cùng percentage nhưng rights khác nhau

Venture investors often receive preferred shares with rights such as:

- liquidation preference;
- conversion rights;
- anti-dilution protection;
- information rights;
- veto/consent rights;
- board rights.

Therefore “Investor owns 20%” does not fully describe economics.

At exit, liquidation preference can change payout order. A company may sell for a seemingly high amount but common shareholders receive far less if preference stack is large.

This is why term sheet matters as much as valuation headline.

## Burn rate và runway

**Net burn / 순현금소진** measures how much cash company loses per period after cash inflows.

\[
Runway\ (months) \approx \frac{Cash}{Monthly\ Net\ Burn}
\]

If cash = 12 billion KRW and net burn = 1 billion/month, simple runway ≈ 12 months.

But runway is dynamic. Revenue growth, hiring, marketing, capex and working capital can change burn quickly.

A startup can be “growing fast” and still die because next financing arrives after cash runs out.

## Funding round ≠ business milestone

Seed, Series A, B, C are market conventions, not standardized operating levels.

Series A does not guarantee PMF; Series C does not guarantee profitability. Financing round only proves investors agreed to provide capital under particular terms.

Good analysis separates:

```text
Financing Event ≠ Operating Performance
```

A large round may increase survival time while underlying unit economics remain weak.

## Revenue quality and contribution margin

Startup revenue growth must be decomposed.

For transaction business:

\[
Revenue = Transactions \times Revenue\ per\ Transaction
\]

But revenue is not economic profit. Need subtract variable costs to calculate **contribution margin / 공헌이익**.

A useful ladder:

```text
Revenue
- directly variable COGS
= Gross Profit
- payment / fulfillment / support / incentives
= Contribution Profit
```

If each incremental order has negative contribution margin, scaling increases losses before fixed cost even enters.

## CAC, LTV và payback period

Customer Acquisition Cost:

\[
CAC = \frac{Sales\ and\ Marketing\ Spend}{New\ Customers\ Acquired}
\]

Lifetime Value should be based on contribution profit, not revenue:

\[
LTV \approx Contribution\ Margin\ per\ Period \times Expected\ Customer\ Lifetime
\]

But lifetime cannot be assumed infinite. Churn, cohort behavior and discounting matter.

Useful question is not only `LTV > CAC` but **how long does CAC pay back?** If payback is 36 months and company runs out of cash in 10 months, theoretical LTV does not solve liquidity problem.

## Cohort analysis: average user metrics có thể đánh lừa

Suppose MAU rises every month because marketing brings new users, while old users leave quickly. Aggregate MAU can look healthy even though retention is poor.

Cohort analysis groups users by acquisition month and observes behavior over time.

A retention curve that stabilizes at non-trivial level is often stronger PMF evidence than cumulative downloads.

This is analogous to survival analysis in statistics: we care not only who arrived, but how long they stay.

## Network effects: không phải mọi platform đều có moat

A product has network effect when value to each participant rises as network grows.

Examples include marketplace liquidity, social graph and payment acceptance.

But need distinguish:

- **direct network effect**: more users directly increase value;
- **cross-side effect**: more sellers attract buyers and vice versa;
- **data effect**: usage improves algorithm/product;
- **density effect**: local service improves with route/activity concentration.

Network effect weakens if users can **multi-home / 멀티호밍** easily across multiple platforms.

Therefore user count alone is not proof of defensibility.

## Korea venture ecosystem: why 1997 matters

After Asian Financial Crisis, Korea sought new growth engines beyond traditional chaebol-led expansion. Venture policy, KOSDAQ, broadband infrastructure and IT talent helped internet/game/software companies emerge.

Later smartphone penetration expanded opportunities in fintech, commerce, mobility, content and platforms. Biotech, deep tech and AI added new venture categories.

This historical sequence matters because startup ecosystem is partly a response to mature-economy challenge: **how can new firms create growth when incumbent industrial structure is already concentrated?**

## `벤처기업` can be a legal/policy status

In Korean policy context, `벤처기업` may refer to firms meeting statutory/certification criteria; it is not always identical to colloquial “startup”.

When reading subsidy, tax program or statistics, always check definition. A legal venture company may be relatively mature; a young startup may not hold that specific certification.

This is another example of why business vocabulary must be mapped to exact regulatory context.

## Government support: useful capital but not customer demand

Korea has accelerators, policy funds, TIPS-type programs, credit guarantees, R&D support and government-backed venture vehicles.

These can reduce financing constraint or technology risk.

But subsidy does not create PMF. If customers do not value product, policy capital only delays failure.

Good policy support should ideally solve **market failure** — e.g., externality, information asymmetry or financing gap — rather than permanently subsidize weak unit economics.

## Corporate Venture Capital (CVC)

Large Korean groups invest in startups through CVC or strategic funds.

Strategic investor may bring distribution, manufacturing, data or enterprise customers. But it can also create dependency if startup becomes tied too closely to one corporate ecosystem.

Startup should ask whether corporate investor creates **strategic option** or limits future partners.

## Scale-up: different problem from startup formation

Early startup asks “can product work?” Scale-up asks “can organization grow without breaking?”

At scale, bottleneck moves to:

- management layers;
- hiring senior leaders;
- process standardization;
- security/compliance;
- international sales;
- infrastructure reliability;
- capital efficiency.

Founder intuition alone cannot coordinate hundreds or thousands of employees.

Scale-up is organizational engineering.

## Korea-specific scale-up constraint: domestic market size

Korea has sophisticated consumers but smaller home market than US/China/EU. Some startups can dominate domestic niche and become highly profitable; others must internationalize to reach large TAM.

Internationalization is not translation. Product-market fit must be rediscovered around local regulation, pricing, distribution and culture.

This creates **second PMF problem**.

## Down round and signaling

If new financing occurs below prior valuation, this is a **down round / 다운라운드**.

Effects can include:

- stronger dilution;
- anti-dilution adjustments;
- employee morale issues;
- weaker market signal;
- pressure to reset option strike prices or expectations.

But down round is not necessarily death. If company still has strong underlying business, recapitalization may extend runway and reset unrealistic past pricing.

## IPO, M&A and liquidity

Venture investors eventually need liquidity.

Common routes:

- IPO, often KOSDAQ for growth/technology firms;
- strategic M&A;
- secondary share sale;
- partial liquidity while company stays private.

Exit matters at ecosystem level because returns recycle into new funds and founders/employees become future angel investors.

But founder should not optimize business solely for IPO. IPO is financing/liquidity event, not business model.

## KOSDAQ and the startup–capital-market bridge

KOSDAQ provides public market access to smaller/growth/technology firms. Successful listing can fund expansion and give investor liquidity.

But public market changes governance regime. Quarterly/periodic disclosure, shareholder scrutiny and price volatility increase.

Startup going public shifts from **venture narrative discipline** to **public-market evidence discipline**.

Xem [10_capital_markets_kospi_kosdaq_konex](./10_capital_markets_kospi_kosdaq_konex.md).

## Startup failure: classify before learning

Not all failures mean “bad idea”. Failure can arise from different mechanisms:

- no real customer pain;
- PMF but CAC too high;
- unit economics negative;
- financing mismatch;
- regulation blocks scaling;
- founder/team conflict;
- technical execution failure;
- market timing too early/late;
- competitor with stronger distribution wins.

Learning improves only when failure cause is diagnosed precisely.

## How to analyze a Korean startup

Use a practical sequence:

1. What exact problem is being solved?
2. Who pays and why now?
3. What is retention/repeat behavior?
4. What are gross and contribution margins?
5. CAC, payback and LTV assumptions?
6. Current runway and next funding dependency?
7. Cap table and investor rights?
8. Regulatory/policy dependency?
9. Domestic vs global TAM?
10. What operational capability is required to scale?

For pre-revenue deep tech, replace classic CAC/retention with technical milestones, IP, regulatory path, pilot customers and funding runway.

## Mental Model

> Startup is a machine for converting **uncertainty into evidence**. Venture capital buys time to learn; product-market fit proves customer value; unit economics prove scale can create economic value; organizational capability determines whether scale-up survives.

## Common misconceptions

Startup ≠ young company. Age alone does not imply scalable venture economics.

Valuation ≠ company cash. Valuation is implied equity price; funding amount is actual cash raised.

User growth ≠ moat. Retention, switching cost, network structure and monetization matter.

Revenue growth ≠ healthy growth. Contribution margin and cash burn can deteriorate while revenue rises.

Government funding ≠ business validation. Customer demand remains separate evidence.

## Connections

Read with [06_sme_mid_sized_and_subcontracting_ecosystem](./06_sme_mid_sized_and_subcontracting_ecosystem.md) to contrast SME scaling, [10_capital_markets_kospi_kosdaq_konex](./10_capital_markets_kospi_kosdaq_konex.md) for exit/public markets, [11_banks_finance_and_corporate_funding](./11_banks_finance_and_corporate_funding.md) for financing mechanics and [17_platform_telecom_content_retail_services](./17_platform_telecom_content_retail_services.md) for platform unit economics.
