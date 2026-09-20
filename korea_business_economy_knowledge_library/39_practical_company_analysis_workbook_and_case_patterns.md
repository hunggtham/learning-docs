# Practical Company Analysis Workbook — từ filing tới thesis, scenario và decision (실전 기업분석 워크북)

Các chapter trước giải thích lịch sử, macro, industry, accounting, governance và funding. File này biến toàn bộ knowledge đó thành một **workbook thực hành**. Mục tiêu là khi gặp một Korean company mới, bạn có thể mở DART/KIND/IR, tự dựng economic model, phát hiện missing questions và viết một research note có thể kiểm chứng.

Đây không phải checklist để tick cho xong. Nó là sequence giúp chuyển dữ liệu rời rạc thành causal model.

## 1. Output cuối cùng của một company analysis nên là gì?

Một analysis tốt không cần dài hàng trăm trang. Nó cần trả lời rõ năm câu:

1. Company thật sự kiếm tiền bằng engine nào?
2. Những variable nào quyết định profit và cash?
3. Balance sheet có chịu nổi downside không?
4. Governance/capital allocation có giữ value cho shareholder/creditor không?
5. Điều kiện nào khiến view hiện tại sai?

Nếu không trả lời được năm câu này, việc thu thập thêm data có thể chỉ tăng information mà không tăng understanding.

## 2. Tạo một one-page identity sheet

Trước khi model, ghi:

```text
Legal name:
Ticker:
Group / parent:
Main subsidiaries:
Main segments:
Main geography:
Top customers if disclosed:
Key inputs:
Key competitors:
Listing market:
Reporting perimeter:
Fiscal year:
```

Đừng bắt đầu bằng valuation. Sai legal entity sẽ làm toàn bộ analysis sau đó sai.

## 3. Viết company trong một câu

Cố gắng viết:

> Công ty X kiếm tiền bằng cách ___ cho ___, profitability chủ yếu phụ thuộc vào ___ và balance-sheet risk lớn nhất là ___.

Ví dụ generic:

> Một memory-chip producer kiếm tiền bằng bán DRAM/NAND cho device/cloud customers; profit phụ thuộc ASP × bit shipment × cost per bit, còn risk lớn là cycle + CAPEX + technology transition.

Nếu câu này vẫn mơ hồ, bạn chưa hiểu business đủ sâu.

## 4. Vẽ economic engine

Một template chung:

```text
Demand driver
    ↓
Volume / activity
    ×
Price / monetization
    ↓
Revenue
    - variable cost
    - fixed cost
    ↓
Operating profit
    ± working capital
    - capex
    ↓
Cash flow
```

Sau đó thay variables theo industry.

## 5. Case Pattern A — Semiconductor

Một semiconductor model nên đi từ:

```text
End demand
→ bit demand
→ supply growth / capacity
→ utilization
→ ASP
→ revenue
→ gross margin
→ CAPEX / depreciation
→ FCF
```

### Key questions

**Demand:** AI/server/mobile/PC mix thay đổi ra sao?

**Supply:** competitors thêm capacity bao nhiêu và yield thế nào?

**Technology:** node/process/product transition ảnh hưởng cost per bit ra sao?

**Pricing:** contract/spot direction có sustain không?

**CAPEX:** company đang invest counter-cyclical hay chase peak demand?

### Simple scenario

Base:

```text
Bit shipment +15%
ASP +5%
Cost/bit -10%
```

Bear:

```text
Bit shipment +5%
ASP -20%
Cost/bit -5%
```

Do fixed cost/depreciation lớn, operating profit có thể move mạnh hơn revenue.

Đây là operating leverage.

Xem [`14_semiconductors_electronics_display.md`](./14_semiconductors_electronics_display.md).

## 6. Case Pattern B — Automotive

Auto company economics:

```text
Units sold
× ASP / mix
= Revenue
- materials
- labor
- incentives
- warranty
= Automotive operating profit
+/- finance affiliate economics
```

### Không chỉ nhìn units

Một company bán ít xe hơn nhưng mix chuyển SUV/luxury có thể tăng margin.

Ngược lại, volume tăng nhờ incentives mạnh có thể làm margin giảm.

### Variables

- global unit sales;
- ASP/mix;
- incentives;
- utilization;
- raw materials;
- FX;
- warranty/recall;
- captive-finance credit losses;
- EV transition CAPEX.

### Stress test

```text
Units -10%
Incentive +2% of ASP
KRW strengthens 8%
Warranty cost +30%
```

Trace tới operating margin, cash và finance subsidiary.

Xem [`15_automotive_battery_mobility.md`](./15_automotive_battery_mobility.md).

## 7. Case Pattern C — Platform / Internet

Platform model cần tránh chỉ nhìn MAU.

Economic chain:

```text
Users
× engagement
× transactions/ad inventory
× monetization rate
= Revenue
- traffic acquisition
- content / fulfillment / payment / cloud cost
- R&D / sales
= Operating profit
```

### Questions

- user growth hay monetization growth?
- retention?
- take rate tăng có gây merchant/user backlash?
- network effect thật hay multi-homing dễ?
- regulation ảnh hưởng ads/payment/data thế nào?
- new businesses đang subsidized bởi core cash engine bao lâu?

### Red flag

Revenue growth cao nhưng marketing spend phải tăng nhanh hơn để giữ growth có thể chỉ là paid growth, không phải strengthening network effect.

Xem [`17_platform_telecom_content_retail_services.md`](./17_platform_telecom_content_retail_services.md).

## 8. Case Pattern D — SI/SM và enterprise IT

Đây là model quan trọng với Korean enterprise ecosystem.

SI/SM company thường có mix:

```text
System Integration (SI)
+ System Management / Maintenance (SM)
+ Cloud / managed service
+ software/license/data/AI projects
```

### Revenue engine

Project SI:

\[
Revenue \approx Billable\ Resources \times Utilization \times Billing\ Rate
\]

hoặc fixed-price contract theo milestones.

SM/maintenance có recurring component ổn định hơn.

### Key economics

- internal/captive group demand;
- external customer ratio;
- developer utilization;
- subcontractor ratio;
- fixed-price vs time-and-material;
- backlog;
- contract asset;
- labor cost inflation;
- cloud migration mix;
- high-margin software/IP contribution.

### Project margin trap

Fixed-price project estimate 100 revenue, 85 cost → margin 15.

Nếu scope creep làm cost thành 105, entire project economics đảo sign.

Do đó SI company cần đọc contract assets, provisions, outsourced labor và project loss reserves.

### Career layer

Nếu phân tích company để ứng tuyển, thêm:

```text
Core dev hay coordination?
Captive project hay external client?
SI build hay SM maintenance?
Tech stack modern hay legacy?
Subcontracting layer?
Decision authority?
Promotion / evaluation?
```

Company economics và career economics liên quan nhưng không giống nhau.

Xem [`34_digital_fintech_cloud_and_it_services.md`](./34_digital_fintech_cloud_and_it_services.md), [`12_labor_titles_compensation_and_workplace.md`](./12_labor_titles_compensation_and_workplace.md) và [`13_business_culture_decision_making_and_communication.md`](./13_business_culture_decision_making_and_communication.md).

## 9. Case Pattern E — SME supplier

Một Korean SME supplier có thể profitable nhưng bargaining power thấp.

Model:

```text
Customer production volume
× supplier content per unit
× price
= revenue
- raw materials
- labor
- depreciation
= operating profit
± payment terms
= cash flow
```

### Questions

- top customer % revenue?
- single-source hay replaceable?
- annual price-down pressure?
- raw-material pass-through?
- tooling/capex burden?
- payment terms?
- technology ownership?
- customer relocation risk?

### Key insight

Supplier revenue growth có thể tốt nhưng working-capital need tăng nhanh nếu customer payment term dài.

Growth có thể consume cash.

Xem [`06_sme_mid_sized_and_subcontracting_ecosystem.md`](./06_sme_mid_sized_and_subcontracting_ecosystem.md).

## 10. Case Pattern F — Construction / PF

Construction company cần tách core construction margin và contingent PF exposure.

```text
Orders
→ backlog
→ construction progress
→ revenue recognition
→ contract assets/receivables
→ cash collection
```

Parallel:

```text
Developer / SPV funding
→ guarantee / credit support
→ refinancing
→ presales
```

A healthy order book không neutralize guarantee risk.

### Stress

- presales slow;
- project cost +15%;
- refinancing spread +300bp;
- completion delayed 6 months;
- guarantee crystallizes.

Xem [`18_construction_real_estate_and_project_finance.md`](./18_construction_real_estate_and_project_finance.md).

## 11. Case Pattern G — Financial company

Không dùng industrial FCF cho bank/insurer như bình thường.

### Bank

```text
Loan/deposit base
× NIM
- operating cost
- credit loss
= earnings
```

### Securities company

```text
Brokerage fees
+ IB fees
+ trading/structured result
- funding/operating cost
- credit loss
```

### Insurer

```text
Premium/service result
+ investment result
- claims/expenses
```

Always pair return with capital adequacy.

Xem [`35_financial_sector_securities_insurance_asset_management.md`](./35_financial_sector_securities_insurance_asset_management.md).

## 12. Five-year financial table

Tạo bảng riêng thay vì đọc từng annual report rời rạc:

| Metric | Y-4 | Y-3 | Y-2 | Y-1 | Y0 |
|---|---:|---:|---:|---:|---:|
| Revenue | | | | | |
| Operating Profit | | | | | |
| Operating Margin | | | | | |
| Net Income | | | | | |
| CFO | | | | | |
| CAPEX | | | | | |
| FCF | | | | | |
| Debt | | | | | |
| Cash | | | | | |
| Shares | | | | | |

Đánh dấu event bên cạnh: acquisition, spin-off, factory launch, crisis, major customer win/loss.

Pattern nhiều năm quan trọng hơn snapshot.

## 13. Build driver tree

Mỗi company nên có một driver tree.

Ví dụ:

```text
Operating Profit
├─ Revenue
│  ├─ Volume
│  └─ Price / Mix
└─ Cost
   ├─ Variable cost
   ├─ Labor
   ├─ Depreciation
   └─ Other fixed cost
```

Sau đó map macro variable vào driver.

```text
KRW → export ASP/margin
Rate → interest + demand
Oil → logistics/material
China demand → volume
```

Đây là bridge giữa [`21_economy_to_company_transmission.md`](./21_economy_to_company_transmission.md) và company model.

## 14. Build bull/base/bear scenario

Scenario không phải forecast precision. Nó là test dependency.

| Driver | Bear | Base | Bull |
|---|---:|---:|---:|
| Volume | -10% | +3% | +10% |
| Price | -8% | 0% | +5% |
| Margin | 5% | 8% | 11% |
| CAPEX | high | normal | controlled |

Khi scenario chạy, observe FCF, debt và valuation.

## 15. Không dùng scenario vô lý

Bear case không phải “mọi thứ cùng xấu 50%”.

Scenario cần causal coherence.

Ví dụ semiconductor downturn có thể đi với ASP giảm và utilization giảm, nhưng lower demand cũng có thể khiến CAPEX cut sau một lag.

A coherent scenario kể được câu chuyện kinh tế.

## 16. Sensitivity table

Nếu valuation phụ thuộc mạnh vào margin và growth, tạo matrix thay vì một target price.

```text
             Margin
Growth       6%   8%   10%
  1%         ...  ...  ...
  3%         ...  ...  ...
  5%         ...  ...  ...
```

Mục tiêu là biết assumption nào dominate value.

## 17. Reverse-engineer market expectations

Thay vì chỉ forecast, hỏi current valuation imply gì.

Ví dụ nếu market cap chỉ justified khi margin tăng 5% → 12% trong ba năm, analyst phải tìm evidence company có path thực tế tới 12%.

Đây là **reverse valuation / 역산 가치평가**.

## 18. Thesis architecture

Một thesis tốt có structure:

```text
Observation
→ Mechanism
→ Evidence
→ Financial impact
→ What market may be missing
→ Catalyst / timeline
→ Thesis breaker
```

Không viết:

> “Company tốt vì AI growth.”

Viết:

> AI demand tăng HBM volume; nếu yield và capacity ramp đạt X, mix shift nâng blended ASP/margin. Thesis fail nếu qualification delay hoặc competitor supply tăng nhanh hơn demand.

Mechanism giúp thesis falsifiable.

## 19. Evidence hierarchy

Tag mỗi note:

- **F — Fact:** audited filing/regulatory filing.
- **M — Management Claim:** IR, earnings call.
- **I — Inference:** analyst reasoning.
- **E — External:** industry/government/third-party evidence.

Ví dụ:

```text
[F] CAPEX = 5T
[M] Management expects new line to improve competitiveness
[I] At <60% utilization, project ROIC likely below target
```

Tagging này chống việc biến management narrative thành fact.

## 20. Build source log

Research note nên có source log:

| Date | Source | What it supports | Confidence |
|---|---|---|---|
| | DART annual report | debt maturity | High |
| | IR deck | management target | Medium |
| | Industry source | market growth | Medium |

Nếu conclusion quan trọng nhưng source weak, đó là research gap.

## 21. Read DART theo sequence

Đừng đọc annual report từ page 1 tới cuối như novel.

Một efficient order:

```text
1. Company/segment overview
2. Consolidated financial statements
3. Cash flow
4. Segment note
5. Debt/maturity
6. Related parties
7. Commitments/guarantees
8. Major contracts / capex
9. Shareholder/control
10. Auditor/corrections
```

Sau đó quay lại accounting policy nơi cần.

## 22. Read footnote bằng question, không bằng patience

Không cần memorize mọi note.

Nếu CFO weak → mở receivable/inventory/contract asset.

Nếu debt high → mở maturity/covenant/guarantee.

Nếu acquisition lớn → goodwill/PPA.

Nếu group complex → related parties/subsidiaries.

Question-driven reading hiệu quả hơn linear reading.

## 23. Forensic cross-check

Dùng [`38_forensic_accounting_red_flags_and_earnings_quality.md`](./38_forensic_accounting_red_flags_and_earnings_quality.md) để kiểm tra:

```text
Earnings vs CFO
Revenue vs receivables
Sales vs inventory
CFO vs payables
Adjusted profit vs audited profit
Debt vs guarantees
Buyback vs net share count
```

Single red flag không đủ; cluster mới đáng chú ý.

## 24. Credit cross-check

Dùng [`36_credit_ratings_bonds_default_and_restructuring.md`](./36_credit_ratings_bonds_default_and_restructuring.md):

```text
Debt amount
→ maturity ladder
→ interest rate
→ rating/spread
→ covenant
→ liquidity sources
→ downside scenario
```

Equity thesis tốt nhưng liquidity không survive bear case là dangerous thesis.

## 25. Corporate-action cross-check

Nếu company đang merger/split/issue shares:

- ownership before/after;
- issue/exchange ratio;
- related party;
- use of proceeds;
- share count;
- debt;
- minority shareholder effect.

Xem [`37_corporate_actions_mna_mergers_spin_offs_and_capital_actions.md`](./37_corporate_actions_mna_mergers_spin_offs_and_capital_actions.md).

## 26. Write a risk register

Không dùng generic list “competition, regulation, macro”.

Risk register nên link mechanism:

| Risk | Trigger | Financial transmission | Leading indicator |
|---|---|---|---|
| Customer loss | contract not renewed | volume↓, utilization↓ | customer concentration |
| Rate shock | refinancing | interest↑, FCF↓ | maturity/spread |
| Scope creep | project delay | labor cost↑ | contract asset/provision |

Risk tốt là measurable.

## 27. Thesis breakers

Thesis breaker phải cụ thể:

```text
Utilization < 60% for 4 quarters
Top customer share drops by half
Net debt/EBITDA > 4x
FCF negative despite normalized cycle
New product fails qualification
```

Nếu breaker xảy ra, re-underwrite thesis từ đầu.

## 28. Pre-mortem

Giả sử ba năm sau investment/job/company view sai hoàn toàn.

Viết trước 5 plausible causes.

Ví dụ SI company:

1. captive demand giảm;
2. cloud shift commoditizes legacy SI;
3. labor cost rises faster than billing rate;
4. fixed-price projects incur losses;
5. key engineers leave.

Pre-mortem bắt bạn nhìn beyond current narrative.

## 29. Career decision workbook

Khi company analysis phục vụ career, thêm matrix:

| Dimension | Questions |
|---|---|
| Business quality | stable/growing? |
| Team importance | core or support? |
| Skill accumulation | portable skills? |
| Project type | build/maintenance/coordination? |
| Decision rights | ownership or execution only? |
| Compensation | fixed/bonus/overtime? |
| Promotion | criteria/timing? |
| Organizational risk | restructuring/outsourcing? |

Một company mạnh không guarantee role mạnh. Role-level economics phải được model riêng.

## 30. Supplier/partner decision workbook

Nếu company là vendor/customer:

- payment terms;
- creditworthiness;
- concentration;
- contract duration;
- SLA/penalty;
- bargaining power;
- switching cost;
- data/IP ownership;
- dependency on key person.

Company analysis phục vụ commercial decision khác stock analysis.

## 31. Research note template hoàn chỉnh

```markdown
# Company — Research Note

## 1. One-sentence economic identity
## 2. Legal entity / group map
## 3. Historical origin
## 4. Revenue engine
## 5. Driver tree
## 6. Value chain / customers / suppliers
## 7. Unit economics
## 8. Moat / competitive position
## 9. 5-year financial bridge
## 10. Earnings quality
## 11. Balance sheet / liquidity / credit
## 12. Governance / related parties
## 13. Corporate actions
## 14. Capital allocation
## 15. Macro exposure
## 16. Bear / Base / Bull scenarios
## 17. Valuation / implied expectations
## 18. Risk register
## 19. Thesis breakers
## 20. Pre-mortem
## 21. Career / supplier view if relevant
## 22. Source log
```

## 32. Minimum viable analysis trong 30–60 phút

Khi không có nhiều thời gian, làm version rút gọn:

```text
10 min — entity + segments + group
10 min — financial trend + cash
10 min — debt + ownership + major risk
10 min — industry drivers
10 min — valuation / scenario
10 min — write what you still don't know
```

Quan trọng nhất là cuối session phải có **unknowns list**.

## 33. Deep analysis trong nhiều ngày

Deep work khác ở độ evidence, không phải số lượng headings.

Bạn sẽ:

- rebuild 5–10 year data;
- compare peers;
- read multiple filings;
- reconstruct corporate actions;
- normalize cycle;
- scenario test;
- review external industry sources;
- challenge thesis.

## 34. Unknowns list

Research tốt kết thúc bằng questions chưa trả lời.

Ví dụ:

```text
How much of growth is price vs volume?
What % capex is maintenance?
Is customer concentration increasing?
What is actual hedge ratio?
How much cash is restricted?
What is parent-level debt maturity?
```

Unknowns list quyết định research tiếp theo.

## 35. Stop condition

Bạn không cần know everything.

Analysis có thể dừng khi:

1. economic engine rõ;
2. main sensitivities rõ;
3. downside survivability được test;
4. valuation/job/commercial decision assumptions explicit;
5. remaining unknowns không material hoặc đã bounded.

Without stop condition, research dễ biến thành collection trivia.

## 36. Final one-page decision memo

Sau deep dive, viết lại chỉ một page:

```text
What company is
Why economics work
3 key drivers
3 key risks
Balance-sheet view
Governance view
Base scenario
Bear scenario
What current expectations seem to assume
3 thesis breakers
Open questions
```

Nếu không compress được analysis về một page causal logic, bạn có thể đang giữ quá nhiều facts nhưng chưa có model.

## Mental Model

> Practical company analysis là quá trình **nén hàng nghìn dòng disclosure thành một vài causal equations và decision-relevant risks**.

Flow chuẩn:

```text
Entity
→ Business engine
→ Drivers
→ Financial statements
→ Cash conversion
→ Funding
→ Governance
→ Scenario
→ Expectations
→ Decision
```

Điểm cuối không phải “biết nhiều về company”, mà là biết **variable nào cần theo dõi để biết view của mình còn đúng hay đã sai**.

## Common mistakes khi thực hành

**Đọc news trước filing.** News cho narrative, filing cho base facts.

**Model revenue trước khi hiểu unit economics.** Forecast sẽ chỉ là extrapolation.

**Dùng một valuation metric cho mọi industry.** Bank, semiconductor và SaaS không có cùng economics.

**Chỉ có base case.** Không biết downside nghĩa là chưa biết risk.

**Không track share count/debt.** Company growth không đồng nghĩa per-share value growth.

**Không viết thesis breakers.** View sẽ dễ bị confirmation bias giữ lại quá lâu.

## Liên kết học tiếp

- [`19_major_groups_case_studies.md`](./19_major_groups_case_studies.md) — group-level patterns.
- [`20_how_to_analyze_a_korean_company.md`](./20_how_to_analyze_a_korean_company.md) — framework tổng quát.
- [`21_economy_to_company_transmission.md`](./21_economy_to_company_transmission.md) — macro transmission.
- [`35_financial_sector_securities_insurance_asset_management.md`](./35_financial_sector_securities_insurance_asset_management.md) — financial companies.
- [`36_credit_ratings_bonds_default_and_restructuring.md`](./36_credit_ratings_bonds_default_and_restructuring.md) — credit.
- [`37_corporate_actions_mna_mergers_spin_offs_and_capital_actions.md`](./37_corporate_actions_mna_mergers_spin_offs_and_capital_actions.md) — corporate actions.
- [`38_forensic_accounting_red_flags_and_earnings_quality.md`](./38_forensic_accounting_red_flags_and_earnings_quality.md) — earnings quality.