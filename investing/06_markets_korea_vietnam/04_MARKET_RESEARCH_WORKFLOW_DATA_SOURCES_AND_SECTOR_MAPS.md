# 04 — Market Research Workflow, Data Sources và Sector Maps cho Hàn Quốc & Việt Nam

> Chapter này biến toàn bộ knowledge library thành một quy trình research lặp lại được. Mục tiêu là khi mở một stock, ETF hoặc sector ở Hàn Quốc hay Việt Nam, bạn biết phải hỏi gì trước, dữ liệu nào là leading/lagging, nguồn nào đáng tin hơn và khi nào một headline thực sự thay đổi thesis. Research tốt không phải đọc thật nhiều tin; nó là giảm uncertainty theo thứ tự hợp lý.

## 1. Research bắt đầu bằng Question Tree

Không nên mở chart rồi cố tìm câu chuyện phù hợp price action. Hãy bắt đầu bằng question tree:

```text
Business kiếm tiền bằng cơ chế nào?
Driver nào quyết định revenue/margin?
Cycle đang ở đâu?
Balance sheet chịu risk gì?
Market đang price expectation nào?
Catalyst nào có thể làm expectation đổi?
Data nào sẽ falsify thesis?
```

Question tree giúp biết data nào cần đọc và data nào chỉ là noise.

## 2. Research có ba tầng

Một stock chịu tác động từ **company**, **sector** và **macro/market structure**. Sai lầm phổ biến là nhảy từ macro headline thẳng tới buy/sell mà không qua transmission channel.

Framework:

```text
Global Macro
→ Country Macro
→ Sector Economics
→ Company Fundamentals
→ Expectations / Valuation
→ Flow / Liquidity
→ Price
```

## 3. Primary Source Hierarchy

Primary sources gồm company filings, exchange disclosures, regulator, central bank và statistical agency. Đây là nơi fact được tạo hoặc công bố chính thức.

Secondary research, media và data vendors giúp tổng hợp/interpret. Social media hữu ích để phát hiện idea nhưng không nên là final confirmation.

## 4. Korea Primary Sources

Một research stack Hàn Quốc thường bắt đầu từ company disclosures/DART, KRX market data, BOK monetary/financial data, Statistics Korea và trade/export releases từ authorities liên quan.

Không cần nhớ mọi portal ngay; cần nhớ source hierarchy: filing trước commentary.

## 5. Vietnam Primary Sources

Với Vietnam, ưu tiên company/exchange disclosures, HOSE/HNX/VNX/VSDC-related information, SSC, SBV và General Statistics Office/trade/public-investment sources tùy data.

Governance/disclosure quality khác nhau giữa companies nên notes và audited statements đặc biệt quan trọng.

## 6. Source Timestamp

Ghi ngày công bố và period của data. “Exports tháng 8 công bố tháng 9” khác “news ngày hôm nay”.

Một dataset có thể revised; research note nên giữ original release và revision khi surprise quan trọng.

## 7. Fact, Estimate và Opinion phải tách riêng

Trong notebook, label ba loại:

```text
Fact: dữ liệu đã công bố.
Estimate: forecast/model của analyst.
Opinion: interpretation/thesis.
```

Nhiều sai lầm xảy ra khi analyst biến opinion thành fact qua repeated narrative.

## 8. Research Notebook là Living Document

Mỗi thesis nên có version date, key assumptions, evidence, counter-evidence và invalidation. Khi data mới tới, update assumption thay vì viết note mới không liên kết.

Versioning giúp tránh hindsight bias.

## 9. Base Rate trước Story

Trước khi tin một turnaround, hỏi historical base rate: bao nhiêu companies trong ngành thực sự phục hồi margin sau capacity boom? Bao nhiêu property projects monetize đúng timeline?

Base rate làm narrative realistic hơn.

## 10. Research Workflow cho Korean Stock

Bắt đầu segment revenue/geography, cost structure và capital intensity. Sau đó đọc 5–10 năm financial/cycle, key KPIs, balance sheet, peer positioning và valuation.

Cuối cùng mới overlay KRW, exports, BOK, China/US cycle và sector flows.

## 11. Research Workflow cho Vietnamese Stock

Ngoài business economics, kiểm ownership, related-party exposure, free float, disclosure consistency, debt maturity và cash conversion sớm hơn.

Với illiquid names, market/liquidity risk là một phần thesis chứ không phải execution detail cuối cùng.

## 12. Company Driver Tree

Ví dụ đơn giản:

```text
Revenue = Volume × Price × Mix × FX
EBIT = Revenue × Margin
FCF = EBIT after tax + D&A - Capex - ΔWorking Capital
```

Mỗi sector cần driver tree riêng. Research tốt cố giảm earnings thành vài variables có causal meaning.

## 13. Leading vs Lagging Indicators

Reported earnings thường lag. Orders, inventory, utilization, pricing, customer traffic hoặc loan delinquency có thể lead.

Mục tiêu không phải tìm một perfect leading indicator mà hiểu sequencing.

## 14. Expectations Matter

Stock phản ứng với surprise relative expectations. Good data đã priced có thể không tăng; mediocre data tốt hơn fear có thể rally.

Research note nên ghi “market likely expects what?” chứ không chỉ “fundamentals good/bad”.

## 15. Consensus và Revisions

Consensus level quan trọng, nhưng earnings **revision direction** thường cho thấy information đang được incorporated.

Theo dõi upward/downward revisions theo sector giúp nhận diện breadth của cycle.

## 16. Valuation Context

Historical average multiple không đủ. Multiple phải đặt cùng rates, cycle, ROIC và growth expectation.

Cyclical P/E thấp ở peak earnings có thể là value trap.

## 17. Relative Valuation

So với peers, own history và alternative assets. Cheap relative peer có thể reflect lower quality or governance.

Valuation gap chỉ là starting question: vì sao market discount?

## 18. Reverse Expectations

Thay vì hỏi fair value là bao nhiêu, hỏi current price đòi revenue/margin/growth nào.

Reverse DCF/earnings bridge hữu ích để biết debate thật nằm ở assumption nào.

## 19. Korea Sector Map

Korea broad market có semiconductor, autos, batteries, shipbuilding/industrials, chemicals/materials, financials, platforms, biotech, consumer và utilities.

Each sector maps differently to global growth, China, USD/KRW and rates.

## 20. Vietnam Sector Map

Vietnam market heavily influenced by banks, property, securities, consumer, industrial parks/manufacturing, materials, utilities/energy and technology.

Domestic credit/liquidity channel thường quan trọng hơn Korea.

## 21. Korea Semiconductor Dashboard

Theo memory/HBM pricing, shipments, inventory, utilization, capex, equipment orders, semiconductor exports, global AI/server capex và customer concentration.

Company stock may turn before reported earnings due expectations.

## 22. Korea Auto Dashboard

Theo global unit sales, incentives, ASP/mix, EV share, inventories, regional market share, USD/KRW, warranty costs và tariff/localization policies.

Volume alone can mislead if incentive cost erodes margin.

## 23. Korea Battery Dashboard

Theo EV demand, cell utilization, raw materials, cathode/anode pricing, customer contracts, policy/subsidies and capacity additions.

Overcapacity can offset structural growth.

## 24. Korea Shipbuilding Dashboard

Order intake, backlog, newbuild prices, vessel mix, steel/labor costs, KRW and delivery schedule matter.

Earnings lag order cycle because construction lasts years.

## 25. Korea Bank Dashboard

BOK rate, deposit competition, NIM, household loans, mortgage/property conditions, delinquency, credit cost, CET1 and shareholder-return policy.

Higher rates help NIM only until funding/credit stress dominates.

## 26. Korea Insurance Dashboard

Premium growth, loss ratio/combined ratio, investment yield, duration mismatch, capital adequacy and accounting/regulatory changes.

Rates affect both assets and long liabilities.

## 27. Korea Platform Dashboard

MAU/DAU, GMV, take rate, ad load, ARPU, cloud/AI capex, competition and regulation.

User growth without monetization quality can destroy unit economics.

## 28. Vietnam Bank Dashboard

Credit growth, NIM, CASA, deposit growth/rates, NPL, Group 2, provision coverage, credit cost, CAR/capital and property/bond exposure.

Profit growth driven by lower provisioning while early delinquencies rise should be treated differently from core improvement.

## 29. Vietnam Property Dashboard

Legal progress, presales, customer advances, handover schedule, inventory quality, debt/bond maturity, interest expense and operating cash flow.

Land bank needs legal and financing path to become value.

## 30. Vietnam Securities Dashboard

Market turnover, brokerage share, margin loans, funding cost, proprietary book, capital adequacy and investment-banking activity.

Sector has high operating/market beta.

## 31. Vietnam Industrial Park Dashboard

Leasable land, occupancy, rental rates, remaining lease term, new approvals, location/infrastructure, customer mix and FDI disbursement.

Registered FDI headline alone is insufficient.

## 32. Vietnam Retail Dashboard

Same-store sales, traffic, ticket, store openings/closures, inventory turns, gross margin, rent/labor and payback on new stores.

Store count growth can hide poor unit economics.

## 33. Vietnam Export Manufacturing Dashboard

Orders, export volumes, customer/geographic concentration, labor cost, FX, freight and raw-material inputs.

US/EU demand and trade policy can dominate local macro.

## 34. Vietnam Power / Utility Dashboard

Demand growth, generation mix, hydrology/fuel, tariff/payment terms, capex/debt and regulatory framework.

Revenue growth does not always translate cash if receivables/payment structure weak.

## 35. Korea Export Data

Exports offer relatively high-frequency view of global industrial cycle. Decompose product/destination and price vs volume when possible.

Semiconductor export value can rise via price even before volume improves.

## 36. Vietnam Trade Data

Exports/imports reveal manufacturing cycle, equipment/raw-material demand and trade balance.

Rising machinery imports may precede capacity expansion and should not automatically be read as negative trade deterioration.

## 37. PMI

PMI diffusion indices show breadth/direction, not exact output growth. New orders, export orders, employment, inventories and prices often matter more than headline 50.

Compare with hard data to avoid survey-only conclusions.

## 38. Inflation

Separate food/energy, housing, goods/services and wage-sensitive components. For Korea/Vietnam, imported inflation and FX can be material.

Headline disinflation from energy has different policy implication than broad service disinflation.

## 39. Credit Growth

Credit expansion can support demand but quality matters. Rapid lending into low-productivity/property collateral can create future NPL.

Track composition, lending standards and delinquency.

## 40. Korea FX Dashboard

USD/KRW relates to US-Korea rates, DXY, exports, oil imports, China/risk sentiment and foreign flows.

No single variable explains all moves; use multi-channel map.

## 41. Vietnam FX Dashboard

USD/VND should be read with SBV framework, interbank/deposit rates, DXY, trade balance, FDI, liquidity and reserves context.

Managed currency requires policy interpretation, not free-float logic copied from KRW.

## 42. Foreign Flow Korea

Foreign flow matters strongly in large caps, especially semiconductors. But distinguish strategic allocation, index rebalance, FX hedge and company-specific information.

One-day net flow rarely proves fundamental thesis.

## 43. Foreign Flow Vietnam

Foreign flow is visible but domestic liquidity can dominate. ETF/index/reclassification mechanics can create technical flows.

Always compare flow with turnover and sector concentration.

## 44. Market Breadth

Track advance/decline, percentage above moving averages, new highs/lows, sector participation and equal-weight vs cap-weight index.

Breadth tells whether index move is broad or mega-cap driven.

## 45. Turnover

Rising turnover confirms participation but can also indicate speculative leverage. Compare turnover with margin debt and sector leadership.

Turnover concentration in few speculative names has different meaning from broad institutional participation.

## 46. Margin / Leverage

Margin increases buying power in up cycle and forced selling in down cycle. Track leverage as amplifier, not standalone timing tool.

In Vietnam price limits can intensify liquidation path.

## 47. Market Microstructure

Spread, depth, auction rules and price limits affect implementation. Fundamental thesis that requires immediate exit in illiquid stock is incomplete risk design.

Position size should reflect stressed liquidity.

## 48. Earnings Season — Before Report

Write consensus, key debate variables, what market price implies and scenarios. This prevents post-hoc interpretation.

For cyclical names, estimate price/mix/utilization rather than only EPS.

## 49. Earnings Season — After Report

Separate headline beat/miss from driver quality. Update model on volume, price, margin, working capital, capex and guidance.

Then inspect market reaction vs expectation/positioning.

## 50. Earnings Call

Compare wording with prior quarters. Note KPI additions/removals, guidance confidence and questions management avoids.

Narrative drift can be an early signal.

## 51. Central-Bank Workflow

Before Fed/BOK or relevant policy event, record current pricing. After decision, read statement, forecasts, press conference and reaction of front-end yields/currency/credit.

The surprise may lie in guidance, not rate decision.

## 52. Fiscal Policy Workflow

Distinguish announced budget, approved budget and actual disbursement. Public-investment theme needs project pipeline and company exposure.

Fiscal multiplier depends timing and supply bottlenecks.

## 53. Regulatory Event Workflow

Bank/property/telecom/platform/healthcare are regulation-sensitive. Map rule change to revenue, cost, capital requirement, competition and timeline.

Do not stop at “regulation positive/negative”.

## 54. Geopolitical Shock Workflow

First identify physical channel: oil/shipping/export control/tariff/cyber/security. Then map country → sector → company balance sheet.

War headline without transmission channel is not analysis.

## 55. Commodity Shock Workflow

Determine supply vs demand shock. Oil up from global boom differs oil up from supply disruption.

Then map input/output price exposure and hedge contracts.

## 56. China Shock Workflow

Separate property/infrastructure, consumer and manufacturing-policy channels. Korea and Vietnam have different beneficiaries/risks.

Second-order competition and FDI relocation can offset first-order demand effect.

## 57. Cross-Market Confirmation

Strong thesis gains confidence when independent data agree: prices/orders/exports/company guidance/peer results.

If only stock price improves while earnings revisions and industry data weaken, flow/valuation may be driving.

## 58. Relative Strength

Compare stock to sector and sector to market. Absolute +5% can be weak if sector +20%.

Relative strength is evidence about information/flow, not proof of future return.

## 59. Credit Confirmation

For leveraged companies/sectors, bond spreads, funding rates or bank credit conditions can confirm equity story.

Equity can stay euphoric while credit starts pricing refinancing risk.

## 60. Revision Breadth

Count how many companies/sectors receive upward vs downward earnings revisions. Broad revision recovery is stronger than index earnings driven by few mega caps.

## 61. Positioning

Flows, short interest, fund positioning and derivatives can affect reaction. Fundamental surprise may create little price move if positioning already extreme.

Positioning explains reaction, not intrinsic value.

## 62. Catalyst Calendar

Maintain events: earnings, product launch, policy meetings, legal approvals, lockup expiry, index rebalance, project handover and debt maturity.

Catalyst is timing mechanism, not thesis by itself.

## 63. Invalidation

Every thesis needs evidence that would make you reduce confidence: margin not recovering by X condition, project approval delayed, credit cost rises, customer lost, etc.

“Institutional investors selling” alone is usually not fundamental invalidation.

## 64. Bear Case

Bear case should describe mechanism, not arbitrary -20%. What breaks? Demand, pricing, leverage, regulation or governance?

Map from driver failure to earnings/cash flow and balance-sheet consequence.

## 65. Bull Case

Bull case should also be causal: utilization rises, premium mix improves, funding cost falls, legal project unlocks, etc.

Avoid bull case made only by assigning higher multiple.

## 66. Research Note Template

```text
Business / Sector
Key Driver Tree
Cycle Position
Balance Sheet / Liquidity
Macro Sensitivities
Valuation / Expectations
Catalysts
Bear / Base / Bull
Invalidation
Data to Monitor
Position Size Logic
Last Updated
```

## 67. Watchlist Design

Watchlist should contain reason and trigger, not only ticker. Classify compounder, cyclical, turnaround, event-driven and speculative research.

Remove names with no question to answer.

## 68. Daily Routine

Daily routine should be light: major price/FX/rates moves, company filings, key scheduled data and portfolio-specific alerts.

Avoid consuming every headline; focus what can change assumptions.

## 69. Weekly Review

Review sector leadership, revisions, foreign flow, breadth, FX/rates and catalysts. Reconcile price move with fundamental change.

Weekly is good cadence for learning without overtrading.

## 70. Monthly Review

Update macro trend, credit, exports, PMI, liquidity and valuation regimes. Re-rank sector attractiveness by expected return/risk.

One data point should rarely rewrite full thesis.

## 71. Quarterly Review

Earnings season and company filings justify deeper model update, governance review and capital allocation assessment.

Compare realized vs prior assumptions to calibrate forecast skill.

## 72. Data Dashboard Design

Dashboard should contain only data tied to decisions. Too many charts create false sense of research.

Every series should answer a question: demand, supply, pricing, funding, valuation or liquidity.

## 73. Data Quality Flags

Mark survey vs hard data, seasonally adjusted vs raw, nominal vs real, YoY vs MoM, preliminary vs final and local currency vs USD.

Many apparent contradictions disappear after metadata check.

## 74. Avoid Double Counting

Exports, company revenue and sector shipment may reflect same underlying event. Treat correlated indicators as one evidence cluster, not three independent confirmations.

## 75. Information Edge vs Analytical Edge

Retail investor rarely has first access to public data. Edge more often comes from better synthesis, longer horizon, discipline and avoiding forced behavior.

Speed is not the only competitive advantage.

## 76. Research Time Allocation

Spend most time on high-impact uncertain assumptions, not facts market already knows. If valuation hinges on margin normalization, research margin driver deeply rather than collect unrelated news.

## 77. Decision Log

Before buy/sell, record reason, expected return driver, alternatives considered and what would prove decision wrong.

Review later to separate luck from process.

## 78. From Research to Position

Good thesis still may deserve small position if liquidity/governance/tail risk high. Research confidence and position size are related but not identical.

Portfolio context determines final allocation.

## 79. Mental Model cuối cùng

```text
Question
→ Primary Data
→ Driver Tree
→ Sector / Macro Context
→ Expectations
→ Valuation
→ Scenario / Invalidation
→ Position Size
→ Monitoring Cadence
→ Attribution / Update
```

Research is not the accumulation of information. It is a repeatable process for turning uncertain information into a decision that can later be reviewed and improved.