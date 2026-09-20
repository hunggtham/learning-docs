# Coupang — e-commerce, fulfillment density, membership và logistics economics

Case này dùng Coupang như một laboratory để hiểu một loại Korean company khác hẳn chaebol truyền thống. Company được hình thành trong venture/digital era nhưng business model cuối cùng lại rất **physical-infrastructure intensive**: fulfillment centers, inventory, delivery network, technology, customer service và last-mile operations cùng hoạt động như một system.

Điểm học quan trọng là: gọi một company là “tech” không cho biết economics. Analyst phải tìm production function thực sự.

Xem [17_platform_telecom_content_retail_services](../17_platform_telecom_content_retail_services.md), [33_logistics_ports_and_distribution_networks](../33_logistics_ports_and_distribution_networks.md) và [07_startups_venture_and_scaleups](../07_startups_venture_and_scaleups.md).

## 1. E-commerce revenue không phải một engine duy nhất

Một commerce ecosystem có thể có first-party retail, marketplace, fulfillment/logistics services, membership, advertising và adjacent services.

Các engines có accounting khác nhau.

Trong **1P retail**, company mua inventory rồi bán lại. Gross merchandise value và reported revenue có thể gần nhau hơn vì company là principal.

Trong **3P marketplace**, merchant bán cho customer và platform lấy commission/service fee. GMV có thể rất lớn nhưng reported revenue chỉ là take rate hoặc service revenue tùy arrangement.

Vì vậy:

\[
GMV \neq Revenue \neq Gross\ Profit \neq Cash\ Flow
\]

Đây là distinction đầu tiên phải giữ.

## 2. Customer value proposition và flywheel

Commerce platform có thể tạo flywheel:

```text
More assortment + faster delivery
→ better customer experience
→ more orders
→ higher route / warehouse density
→ lower cost per order
→ better price/service
→ more customers
```

Nhưng flywheel chỉ tồn tại nếu cost per order thực sự giảm khi density tăng. Nếu growth chỉ đến từ subsidy/discount, network có thể lớn nhưng economic moat yếu.

> **Mental Model:** logistics density là một dạng network effect vật lý. Nhiều orders trong cùng geography có thể làm fixed infrastructure và route cost được spread hiệu quả hơn.

## 3. Density economics

Giả sử một delivery route có fixed daily cost 300,000 won.

Nếu route giao 100 packages:

\[
Fixed\ Route\ Cost/Package = 3,000\ won
\]

Nếu density tăng lên 200 packages với route cost chỉ tăng nhẹ lên 360,000 won:

\[
Cost/Package = 1,800\ won
\]

Đây là stylized example, không phải company data. Nó minh họa vì sao order density có thể tạo operating leverage.

Nhưng khi expansion vào low-density region, economics có thể đảo lại.

## 4. Fulfillment center là inventory machine, không chỉ warehouse

Fulfillment center economics phụ thuộc:

```text
Throughput
× pick/pack productivity
× automation
× utilization
× inventory placement accuracy
```

Nếu inventory được đặt gần demand, delivery nhanh và transport cost giảm. Nhưng nếu forecast sai, inventory bị stranded ở wrong location và cần transfer/markdown.

Do đó logistics advantage cần data/forecasting kết hợp physical assets.

## 5. Inventory turns và negative working capital

Retail có thể có favorable working capital nếu collect customer cash nhanh nhưng pay suppliers sau.

Simplified cash conversion cycle:

\[
CCC = DIO + DSO - DPO
\]

E-commerce consumer sales thường có low receivable days; nếu supplier payment terms dài, business có thể tạo working-capital funding.

Nhưng inventory build quá nhanh có thể hút cash và tăng markdown risk.

Revenue growth vì vậy phải được đọc cùng inventory growth.

## 6. Gross margin không đủ — fulfillment cost nằm ở đâu?

Hai retailers có cùng gross margin nhưng fulfillment economics khác nhau.

Analyst cần hiểu classification:

```text
Product cost
Fulfillment labor
Delivery cost
Payment cost
Customer service
Marketing
Technology
```

Nếu một company classify nhiều fulfillment costs below gross profit, gross margin không thể so trực tiếp với company classify khác.

Unit economics nên đi xuống contribution level:

\[
Contribution\ per\ Order = Revenue\ per\ Order - Variable\ Product/Fulfillment/Delivery\ Cost
\]

rồi mới xét fixed corporate/technology cost.

## 7. Membership: revenue nhỏ có thể tạo economics lớn

Membership fee có thể không phải largest revenue line nhưng ảnh hưởng behavior:

```text
Membership
→ lower perceived marginal delivery cost
→ order frequency ↑
→ retention ↑
→ density ↑
→ logistics efficiency ↑
```

Nhưng free/fast shipping làm company absorb delivery cost. Membership chỉ tạo value nếu higher frequency/retention và ecosystem monetization bù được service cost.

Không nên value membership chỉ bằng `members × annual fee`.

## 8. Retention và cohort economics

Aggregate active-customer growth có thể che churn.

Cohort analysis hỏi:

```text
Customers acquired in period T
→ how many remain after 3/6/12/24 months?
→ spending per retained customer?
→ contribution after fulfillment?
```

Nếu older cohorts spend more over time mà acquisition cost không tăng quá nhanh, unit economics mạnh hơn headline user growth.

Nếu growth phụ thuộc liên tục vào expensive acquisition, scale có thể không self-reinforcing.

## 9. Marketplace economics và merchant incentives

3P marketplace có asset-light characteristics hơn 1P retail, nhưng merchant quality, take rate, advertising, fulfillment service và competition quyết định value.

Higher take rate tăng revenue per GMV nhưng có thể làm merchants multi-home hoặc tăng prices.

Do đó pricing power có limit:

```text
Platform value to merchant
- fees
- fulfillment cost
- alternative channel economics
= merchant surplus
```

Nếu merchant surplus quá thấp, ecosystem phản ứng.

## 10. Last-mile labor và service promise

Fast delivery promise tạo customer value nhưng làm operations khó hơn.

Cutoff time, overnight sorting, delivery windows và returns đều cần capacity buffer. System tối ưu không phải 100% utilization mọi lúc; cần slack để absorb peaks và maintain service level.

Đây là một important operations insight:

> Maximum utilization không đồng nghĩa maximum economic efficiency khi service-level failure rất đắt.

## 11. CAPEX: tech company nhưng vẫn cần physical capital

Fulfillment center, automation, vehicles/equipment và IT infrastructure tạo CAPEX/depreciation.

Growth phase có thể có:

```text
CAPEX today
→ capacity tomorrow
→ utilization ramp later
→ depreciation begins
→ cash payback even later
```

Do đó FCF có thể lag accounting operating improvement.

Analyst cần hỏi new capacity có density path đủ để earn acceptable return không.

## 12. Geographic expansion và transferability của moat

Một network mạnh ở Korea không tự động copy sang market khác.

Moat transfer phụ thuộc:

```text
Population density
Urban form
Labor cost
Customer expectation
Existing competitors
Payment infrastructure
Regulation
Real-estate/logistics cost
```

Strategy có thể đúng ở Seoul metropolitan density nhưng không economic ở low-density geography.

Do đó international expansion phải được modeled như new market, không chỉ multiply domestic success.

## 13. Competition: price, convenience và assortment

Commerce competition không chỉ price. Customer chooses bundle:

```text
Price
+ assortment
+ delivery speed/reliability
+ returns
+ trust
+ membership benefits
```

Company có thể tolerate slightly higher product price nếu convenience advantage lớn, nhưng switching cost trong commerce thường thấp hơn enterprise software. Moat phải được continuously earned through service.

## 14. Macro transmission

Consumer slowdown truyền vào commerce qua basket size, discretionary mix và frequency. Inflation có mixed effect: nominal GMV có thể tăng vì price, nhưng real volume/mix xấu.

Labor cost tăng ảnh hưởng fulfillment. Fuel/transport cost ảnh hưởng delivery. Rates ảnh hưởng consumer demand và cost of capital for logistics expansion.

Causal chain:

```text
Household real income ↓
→ discretionary basket ↓
→ mix shifts to essentials
→ GMV/revenue mix changes
→ merchant advertising demand changes
→ fulfillment volume/density changes
```

## 15. Scenario model

### Density-improvement scenario

```text
Active customers +8%
Orders/customer +10%
Same-region density ↑
Cost/order -7%
Contribution margin ↑
CAPEX grows slower than orders
FCF improves
```

### Growth-without-economics scenario

```text
GMV +20%
Heavy promotion
Low-density expansion
Fulfillment cost/order flat/up
CAPEX +30%
FCF remains weak
```

Hai scenarios có cùng attractive topline narrative nhưng shareholder economics rất khác.

## 16. Valuation

Commerce/platform hybrid không nên được valued chỉ bằng revenue multiple.

Useful decomposition:

```text
Core retail contribution
+ marketplace/ads economics
+ membership ecosystem value
+ adjacent businesses/options
- corporate overhead
- required logistics reinvestment
```

Reverse valuation hỏi current enterprise value imply long-run contribution margin và reinvestment rate nào.

High growth chỉ valuable khi incremental growth earns return above cost of capital.

## 17. Common misconceptions

### “E-commerce là asset-light tech”

Không nhất thiết. Fulfillment-led model có thể rất capital intensive.

### “GMV growth = revenue growth = profit growth”

Sai vì principal/agent accounting, take rate, mix và fulfillment cost.

### “Fast delivery càng nhanh càng tốt”

Chỉ nếu willingness-to-pay/retention benefit vượt incremental service cost.

### “Membership fee là lợi nhuận gần như 100%”

Sai vì membership tạo service obligations và thay đổi customer behavior/cost.

## 18. Research workbook

| Driver | Y-4 | Y-3 | Y-2 | Y-1 | Y0 |
|---|---:|---:|---:|---:|---:|
| Active customers | | | | | |
| Revenue/customer | | | | | |
| Revenue | | | | | |
| Gross / contribution margin | | | | | |
| Inventory | | | | | |
| CFO | | | | | |
| CAPEX | | | | | |
| FCF | | | | | |

Nếu disclosure không có exact orders/density, dùng proxy nhưng phải label inference rõ ràng.

## Mental Model cuối

> Fulfillment-led e-commerce là **software-coordinated physical network**. Technology giúp forecast và orchestrate; economic moat chỉ xuất hiện khi customer density, inventory placement và operational execution làm cost/service curve tốt hơn đối thủ một cách bền vững.

Đọc tiếp [10_korean_construction_pf_case.md](./10_korean_construction_pf_case.md) để thấy một asset/project-heavy model nơi cash-flow timing và guarantees còn quan trọng hơn reported revenue.