# Case Study 03 — Korea Semiconductor Cycle: Từ AI Capex tới Earnings và Valuation

> Korean market có trọng số lớn ở semiconductor, nhưng “semiconductor upcycle” không phải một biến duy nhất. Case này học cách tách demand, inventory, ASP, utilization, capex, HBM mix, equipment/material suppliers, FX, earnings revisions và valuation để tránh thesis kiểu “AI tăng → mọi cổ phiếu chip tăng”.

## 1. Bắt đầu từ Value Chain

Một semiconductor ecosystem đơn giản hóa:

```text
End Demand
→ Cloud / AI / PC / Smartphone / Auto
→ Chip Designer / Memory Producer
→ Foundry / Packaging
→ Equipment
→ Materials / Chemicals / Components
→ Distribution / OEM
```

Mỗi node có cycle khác nhau. Memory producer có commodity-like pricing; equipment supplier phụ thuộc capex; materials supplier phụ thuộc wafer starts/utilization; fabless company phụ thuộc design wins và end demand.

## 2. Demand không đồng nhất

“Chip demand” nên tách theo end market:

```text
AI Servers
Traditional Data Center
PC
Smartphone
Automotive
Industrial
Consumer Electronics
```

AI/HBM demand có thể rất mạnh trong khi smartphone/PC recovery yếu. Aggregate semiconductor revenue có thể che sự phân hóa này.

## 3. Bit Demand vs Revenue

Memory business cần tách volume và price:

```text
Revenue ≈ Bit Shipments × ASP
```

Bit demand tăng nhưng ASP giảm nhanh vẫn tạo revenue pressure. Ngược lại supply discipline có thể nâng ASP dù unit demand chỉ tăng vừa phải.

Đây là lý do chỉ nhìn shipment growth không đủ.

## 4. Inventory Cycle

Inventory tồn tại ở nhiều layers:

```text
Producer Inventory
Distributor Inventory
OEM Inventory
Customer Inventory
```

Nếu end demand yếu nhưng customers destock, producer shipments có thể giảm mạnh hơn final demand. Khi destocking kết thúc, shipments có thể rebound trước end-demand boom thực sự.

Inventory cycle vì vậy tạo turning point sớm hơn GDP hoặc reported earnings.

## 5. Leading vs Lagging Indicators

Leading indicators có thể gồm:

```text
Spot / Contract Memory Pricing
Customer Inventory Days
Order Lead Times
Capex Guidance
Utilization Intentions
Equipment Orders
HBM Qualification Progress
Hyperscaler Capex Guidance
```

Lagging indicators gồm reported quarterly revenue, gross margin và EPS.

Stock price thường phản ứng với leading indicators trước accounting data.

## 6. ASP và Supply Discipline

Memory cycle historically biến động vì producers cùng tăng capacity khi pricing tốt.

Nếu demand tăng nhưng supply cũng tăng nhanh hơn, upcycle có thể ngắn.

Key question:

```text
Demand Growth vs Effective Supply Growth
```

Effective supply không chỉ wafer capacity. Yield, process migration, product mix và packaging bottlenecks đều ảnh hưởng.

## 7. HBM khác Commodity Memory thế nào?

HBM có economics khác commodity DRAM truyền thống vì:

- qualification cycles dài hơn;
- advanced packaging quan trọng;
- yield/bonding complexity cao;
- customer concentration lớn;
- product generations thay nhanh;
- capacity allocation constrained.

Do đó HBM premium margin có thể coexist với weak commodity memory, nhưng sustainability phụ thuộc competition và customer qualification.

## 8. Mix Shift

Gross margin improvement có thể đến từ:

```text
Higher ASP
Higher Utilization
Better Product Mix
Yield Improvement
Lower Input Cost
```

Nếu margin tăng chỉ nhờ HBM mix trong khi commodity business vẫn weak, investor nên model mix separately.

## 9. Utilization

Fab utilization có operating-leverage effect. Fixed depreciation/labor overhead spread over more output khi utilization tăng.

Cycle trough:

```text
Low utilization
→ High unit cost
→ Weak margin
```

Recovery:

```text
Inventory normalizes
→ Utilization ↑
→ Unit cost ↓
→ Margin improves faster than revenue
```

Đây là reason earnings can inflect sharply.

## 10. Capex

Capex vừa là signal demand confidence vừa là future supply.

Near term, capex rise benefits equipment/material suppliers. Long term, excessive capex can create oversupply and hurt producer margins.

Do đó:

```text
Producer Capex ↑
→ Supplier Revenue ↑ today
BUT
→ Industry Capacity ↑ later
→ Potential ASP Pressure later
```

## 11. Equipment Suppliers

Equipment supplier earnings thường lead producer capacity expansion. Nhưng exposure khác nhau theo process step:

```text
Deposition
Etch
Lithography
Inspection
Packaging
Testing
```

Technology transition có thể tăng process intensity even without proportional wafer growth.

## 12. Materials Suppliers

Materials demand thường gần utilization/wafer starts hơn equipment capex.

Nếu fab utilization tăng, chemicals/gases/wafers có recurring volume benefit. Nhưng customer concentration và qualification dependency lớn.

Một supplier 70% revenue từ one customer có different risk from diversified global materials company.

## 13. Advanced Packaging

AI/HBM boom làm packaging/back-end bottleneck quan trọng hơn traditional cycle.

Investor cần map:

```text
HBM Stack
Bonding
Interposer / Substrate
Testing
Thermal / Power
Packaging Equipment
```

Không phải mọi supplier được gắn label “AI semiconductor” đều có same content per system.

## 14. Customer Concentration

HBM/AI supply chains often concentrated around few hyperscalers/GPU vendors.

Strong demand từ one customer có thể tạo explosive growth nhưng also bargaining/qualification risk.

Model customer concentration trong bull và bear case.

## 15. KRW Channel

Korean semiconductor producers export globally. KRW depreciation có thể support translated earnings nhưng impact phụ thuộc:

```text
Revenue Currency
Input Currency
Capex Currency
Debt Currency
Hedge Program
```

Do not model USD/KRW as pure profit multiplier.

## 16. Korea Export Data

Semiconductor exports provide high-frequency macro check. Nhưng nominal export growth nên tách price và volume khi possible.

Strong export value do ASP recovery khác strong export growth do unit demand expansion. Sustainability implications khác nhau.

Đọc thêm: [Korea Market Playbook](../06_markets_korea_vietnam/01_KOREA_MARKET_PLAYBOOK.md).

## 17. AI Capex as Upstream Driver

Hyperscaler capex growth can support accelerators, networking, memory, power and cooling.

Nhưng headline capex không map one-to-one tới Korean earnings. Need ask:

```text
What share goes to compute?
Which architecture?
HBM content per accelerator?
Inventory build or end-use deployment?
```

## 18. Demand Quality

Demand quality tốt hơn khi supported by:

```text
Sustainable utilization
Monetizable workloads
Customer cash flow
Broadening customer base
```

Demand quality thấp hơn nếu mostly inventory prebuild, subsidy-driven overcapacity or speculative orders.

## 19. Earnings Revision Cycle

Equity market often trades revisions more than absolute earnings.

Useful sequence:

```text
ASP/Orders Improve
→ Analyst Revenue Estimates ↑
→ Gross Margin Estimates ↑
→ EPS Revisions ↑
→ Target Multiples / Price Update
```

Revision breadth across sector tells whether cycle broadening beyond one leader.

## 20. Peak Earnings Problem

Cyclical stocks can look cheapest on P/E at peak earnings.

Example:

```text
Price = 100
Peak EPS = 20
P/E = 5x
```

Nếu normalized EPS only 8, normalized P/E = 12.5x.

Low trailing P/E can therefore be late-cycle warning, not bargain signal.

## 21. Trough P/E Problem

At trough EPS collapses, P/E may look extremely high or meaningless. Stock can already be bottoming because market expects recovery.

Use normalized earnings, mid-cycle margin, replacement/supply dynamics and forward revisions.

Đọc thêm: [Valuation](../03_company_analysis/03_VALUATION_DCF_AND_MULTIPLES.md).

## 22. Scenario Model

### Base

```text
AI/HBM demand strong
Commodity memory gradual recovery
Supply disciplined
Utilization improves
Margins normalize
```

### Bull

```text
HBM demand exceeds capacity
Qualification/share gains
ASP stronger
Mix shift faster
Equipment bottleneck prolongs pricing power
```

### Bear

```text
Hyperscaler capex slows
Customer inventory rises
New capacity ramps
ASP falls
Utilization drops
HBM premium compresses
```

Each case must translate into revenue, gross margin, capex, FCF and valuation.

## 23. Producer vs Supplier Exposure

Producer often benefits directly from ASP/mix. Equipment supplier benefits capex. Materials supplier benefits utilization. Packaging supplier benefits architecture/content shift.

Thus same cycle stage can favor different parts of value chain.

```text
Early Recovery → Producers / Pricing
Expansion → Equipment / Capex
High Utilization → Materials
Architecture Shift → Packaging / Specialty Suppliers
Late Cycle → Oversupply Risk
```

## 24. Balance Sheet

Cycle survival depends balance sheet.

Questions:

```text
Net Cash / Debt
Capex Commitments
Dividend / Buyback Policy
Debt Maturity
Working Capital
Inventory Write-down Risk
```

Strong balance sheet lets producer continue strategic capex through downturn, potentially gain share.

## 25. Capital Allocation

Semiconductor companies face difficult capital-allocation trade-off:

```text
Invest early → technology leadership, but oversupply risk
Underinvest → protect FCF, but lose node/product position
```

Historical incremental ROIC through cycles matters more than one-year capex intensity.

## 26. Accounting Quality

Watch:

- inventory valuation and write-down/reversal;
- depreciation schedules;
- capitalized development where relevant;
- customer concentration;
- capex vs depreciation;
- government incentives/subsidies;
- receivables during demand slowdown.

Đọc thêm: [Earnings Quality and Forensics](../03_company_analysis/04_EARNINGS_QUALITY_MODELING_AND_FORENSICS.md).

## 27. Valuation Matrix

Useful combinations:

```text
Cycle Trough + Balance Sheet Strong + Revisions Turning Up
Cycle Midpoint + Reasonable Normalized Multiple
Cycle Peak + Capacity Boom + Consensus Extrapolation
```

Valuation must be read against cycle stage, not standalone historical P/E percentile.

## 28. Factor Exposure

Korean semiconductor position can embed:

```text
Korea Country Beta
Global Tech Beta
Growth / Duration
USD/KRW
AI Capex
Memory Cycle
China Demand
Foreign Flow
```

A portfolio holding global tech ETF + Korea semiconductor ETF may be more concentrated than ticker count suggests.

## 29. Flow and Index Effects

Large Korean semiconductor names have meaningful index weight. Foreign flows, futures hedging and global ETF allocation can amplify fundamentals.

Price movement may therefore combine:

```text
Earnings Revision
Multiple Change
FX
Passive / Foreign Flow
Positioning
```

## 30. Risk Event: US Rate Shock

Higher real yields can compress tech multiples even while semiconductor earnings improve.

This creates tension:

```text
EPS ↑
P/E ↓
```

Stock return depends which effect dominates.

This is why macro and company analysis must be connected.

## 31. Risk Event: China Slowdown

China affects end demand, manufacturing, electronics supply chain and geopolitical restrictions.

But exposure differs by company: revenue to China, fab location, end-customer mix and technology node matter.

## 32. Risk Event: Export Controls

Technology controls can constrain equipment/chip sales, force product redesign or accelerate localization competition.

Policy risk is not just revenue loss today; it changes future addressable market and capital allocation.

## 33. Position Sizing

Size should reflect:

```text
Cycle Uncertainty
Single-Customer Risk
Index / Factor Overlap
FX Exposure
Liquidity
Valuation Asymmetry
```

A high-conviction semiconductor thesis can still deserve moderate weight if total portfolio already long global tech/duration.

## 34. Hedge Choices

If concern is Korea market beta, KOSPI futures/index hedge may help but leaves company-specific semiconductor risk.

If concern is USD/KRW, FX hedge changes currency component but not cycle.

If concern is global tech multiple compression, Nasdaq/tech hedge introduces basis risk.

Hedge must match factor being reduced.

## 35. Monitoring Dashboard

Weekly/monthly:

```text
Memory spot/contract prices
Inventory days
Utilization commentary
HBM qualification/share
Hyperscaler capex
Producer capex
Equipment orders/backlog
Export data
USD/KRW
Consensus EPS revisions
Valuation vs normalized earnings
```

## 36. Thesis Invalidation

Possible invalidation:

```text
Customer inventory rebuilding unexpectedly
Capacity additions exceed demand
HBM qualification/share loss
ASP reversal before utilization normalization
Capex boom implies future oversupply
Balance sheet/capex funding deteriorates
```

Price decline alone is not thesis invalidation unless it reflects one of these mechanisms.

## 37. Post-Earnings Attribution

After earnings:

```text
Revenue Beat/Miss
ASP
Bit Shipments
Mix
Gross Margin
Inventory
Capex
Guidance
Consensus Revision
Price Reaction vs Implied Expectation
```

A company can beat reported EPS but fall if forward HBM/capex guidance disappoints relative to priced expectations.

## 38. Reusable Semiconductor Research Template

```text
End Demand
→ Inventory
→ Supply / Capacity
→ ASP
→ Utilization
→ Product Mix
→ Margin
→ Capex
→ Supplier Revenue
→ FCF
→ EPS Revisions
→ Normalized Valuation
→ Position / Hedge
```

## Kết luận

Semiconductor investing is not a simple technology story. Nó là combination của **commodity cycle, technology transition, capacity economics, customer concentration, FX, capex and valuation**. Edge đến từ việc xác định cycle turning point và expectation gap sớm hơn market, không phải chỉ biết ngành đang tăng trưởng dài hạn.