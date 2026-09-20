# Hyundai Motor Case Lab — units, mix, captive finance và transition economics

Hyundai Motor là case để học rằng automotive company không thể được model chỉ bằng “số xe bán ra”. Profitability hình thành từ **units × price/mix**, nhưng sau đó còn bị quyết định bởi incentives, utilization, raw materials, FX, warranty, logistics và captive finance. EV/software transition làm bài toán khó hơn vì company phải tài trợ tương lai trong khi vẫn tối ưu ICE/hybrid cash engine hiện tại.

FY2025 là một snapshot hữu ích: Hyundai Motor công bố khoảng 4.1 triệu xe bán toàn cầu, revenue khoảng KRW 186.3 trillion và operating profit khoảng KRW 11.47 trillion. Những số này chỉ dùng để định vị scale; case tập trung vào mechanism, không extrapolate FY2025 như trạng thái vĩnh viễn.

## 1. Revenue không bằng units

Automotive revenue có thể viết gần đúng:

\[
Automotive\ Revenue \approx Units \times ASP + Other\ Revenue
\]

Nhưng ASP là output của mix:

```text
region mix
× model mix
× trim/options
× powertrain mix
× incentives
× FX translation
```

Một năm units flat nhưng SUV/Genesis/premium mix tăng có thể làm revenue và margin tăng. Ngược lại, units tăng nhờ discount lớn có thể tạo revenue growth yếu và margin giảm.

Vì vậy first driver table nên có:

| Driver | Câu hỏi |
|---|---|
| Units | tăng ở region/model nào? |
| ASP | tăng do price thật hay mix/FX? |
| Incentive | phải trả bao nhiêu để clear inventory? |
| Utilization | plant đang chạy gần capacity hay underutilized? |
| Warranty | quality cost có tăng không? |

## 2. Production economics và operating leverage

Auto plant có fixed cost lớn. Khi utilization giảm, fixed manufacturing cost được spread trên ít units hơn. Điều này làm margin giảm nhanh hơn revenue trong downturn.

Stylized example:

```text
Plant fixed cost = 1,000
Variable cost/car = 20
ASP/car = 30
```

Nếu sản xuất 100 cars:

```text
Revenue = 3,000
Variable cost = 2,000
Fixed cost = 1,000
Operating contribution = 0
```

Nếu mix/price nâng ASP lên 33 mà volume giữ nguyên, contribution = 300. Nếu volume giảm còn 80 nhưng fixed cost gần như không đổi, economics deteriorate nhanh.

Đây là lý do inventory và plant utilization quan trọng hơn một headline sales number.

## 3. Inventory: wholesale, retail và dealer channel

Automaker có thể report wholesale shipment trong khi end-customer retail demand yếu hơn. Nếu dealer inventory tăng, company có thể phải tăng incentive sau đó.

Causal chain:

```text
Production > retail demand
→ dealer inventory ↑
→ days supply ↑
→ incentive ↑
→ ASP/margin ↓
→ production cuts later
→ utilization ↓
```

Vì vậy khi units mạnh nhưng incentive cũng tăng, cần hỏi growth có phải demand thật hay channel loading.

## 4. FX không phải one-line benefit

Hyundai có global production và sales footprint. KRW yếu có thể làm foreign revenue dịch sang KRW cao hơn và hỗ trợ export economics, nhưng company cũng mua imported inputs, sản xuất ở nước ngoài và có natural hedges.

Không dùng:

```text
KRW weak → Hyundai profit up
```

Hãy dùng:

```text
currency of sales
- currency of production/input
± hedging
= net FX exposure
```

Exposure còn thay đổi theo region mix và localization.

## 5. Captive finance: bán xe và bán credit là hai economic engines

Automotive group thường dùng finance/leasing để hỗ trợ purchase. Finance business có thể tăng affordability và dealer conversion, nhưng nó đưa credit risk, funding cost và residual-value risk vào consolidated picture.

Simplified finance engine:

\[
Finance\ Income \approx Earning\ Assets \times Spread - Credit\ Loss - Operating\ Cost
\]

Khi rates tăng, customer monthly payment tăng và auto demand có thể yếu. Đồng thời funding cost của finance arm tăng. Nếu used-car price giảm, residual value của leased vehicles có thể chịu pressure.

Do đó rate shock có hai đường truyền:

```text
Rate ↑ → vehicle affordability ↓ → units/incentives xấu đi
Rate ↑ → finance funding cost ↑ → finance margin/risk xấu đi
```

## 6. Warranty và quality: accounting lag của engineering problem

Quality issue có thể xuất hiện trước khi full financial cost được biết. Warranty provision là estimate dựa trên expected future claims.

Nếu recall lớn xuất hiện, analyst cần phân biệt:

```text
cash paid today
provision recognized today
future service/repair cash outflow
brand/reputation effect
```

Một quarter có provision spike không có nghĩa toàn bộ cash đã ra trong quarter đó.

Đây là ví dụ tốt về accrual accounting: economic event, accounting recognition và cash timing khác nhau.

## 7. EV transition là dual-system capital allocation

Automaker không thể tắt ICE/hybrid hôm nay rồi chuyển toàn bộ capital sang EV/software ngày mai. Company phải duy trì current platforms, factories, suppliers và service network đồng thời đầu tư battery, EV architecture, software-defined vehicle và new manufacturing.

```text
Current cash engine: ICE + hybrid + existing platforms
             ↓ funds
Future architecture: EV + battery + software + autonomy
```

Risk có hai chiều. Invest quá chậm → mất technology/market position. Invest quá nhanh trong khi EV utilization thấp → depreciation và fixed cost đè margin.

Câu hỏi đúng không phải “EV tốt hay xấu” mà là:

\[
Incremental\ ROIC_{EV/software} > Cost\ of\ Capital?
\]

và company có đủ cash/balance sheet để chịu ramp period không.

## 8. Battery economics và vertical coordination

Battery cost là phần lớn EV bill of materials. Automaker có thể dùng long-term sourcing, joint ventures, localization hoặc chemistry mix để giảm supply risk.

Nhưng vertical coordination không đồng nghĩa free economics. JV/factory vẫn cần capital, qualification, utilization và raw-material management.

Khi đọc announcement về battery plant, luôn hỏi:

```text
ownership %?
capital commitment?
capacity/GWh?
customer/offtake?
expected utilization?
subsidy dependency?
start-of-production timing?
```

## 9. Worked margin bridge

Giả định Year A:

```text
Units = 100
ASP = 30
Revenue = 3,000
Operating margin = 8%
Operating profit = 240
```

Year B:

```text
Units -5% → 95
ASP +8% nhờ mix → 32.4
Revenue = 3,078
```

Revenue vẫn tăng khoảng 2.6%. Nhưng nếu incentive, warranty và EV underutilization làm cost tăng 180, operating profit có thể giảm dù revenue tăng.

Bài học: **revenue growth không nói đủ về auto economics**.

## 10. Geographic mix và policy exposure

Automotive là ngành policy-sensitive: tariffs, emissions rules, local-content incentives, safety regulation và industrial subsidies có thể thay đổi production location economics.

Không dừng ở câu “tariff x%”. Trace:

```text
Tariff
→ landed cost
→ company absorbs hay raises price?
→ demand elasticity
→ localization response
→ new CAPEX
→ margin / cash-flow timing
```

Một tariff shock có thể làm short-term margin xấu nhưng thúc đẩy localization investment, tạo long-term fixed-cost/capacity structure mới.

## 11. Scenario lab

### Demand slowdown + rate stress

Giả định:

```text
Global units -8%
Incentive +2 percentage points of ASP
Finance funding cost +150bp
Used-car residual values -10%
KRW strengthens 7%
EV plant utilization thấp hơn plan
```

Trace ít nhất năm channel:

```text
units ↓
ASP net of incentive ↓
plant utilization ↓
finance spread / credit risk xấu
FX tailwind mất
```

Sau đó xem CFO, inventory, receivable/finance assets, CAPEX và net debt.

### Mix-strength scenario

```text
Units flat
SUV/Genesis/hybrid mix ↑
Incentive controlled
quality cost stable
finance losses normal
EV investment disciplined
```

Case này cho thấy volume không cần tăng mạnh để profit cải thiện nếu mix và cost tốt.

## 12. Valuation: cyclicality + finance + transition

P/E đơn thuần có thể bỏ qua auto cycle và finance balance sheet. EV transition cũng làm current earnings và future CAPEX lệch nhau.

Một analytical decomposition:

```text
Normalized automotive earning power
+ finance earning power adjusted for credit cycle
+ strategic/new-business optionality
- transition CAPEX burden
- quality / policy / governance risks
```

Không cần ép mọi component thành SOTP target price. Mục tiêu là biết market đang trả tiền cho engine nào.

## 13. DART/IR reading mission

Tìm:

```text
vehicle sales by region
revenue / operating profit
inventory
warranty provisions
finance receivables/assets
borrowings and funding maturity
CAPEX / investment plan
related-party transactions
shareholder return
major policy / tariff disclosures
```

Đặc biệt so sánh automotive debt với finance-company funding thay vì gom mọi debt thành một con số không context.

## 14. Thesis breakers

Positive thesis có thể fail nếu incentive tăng nhanh, quality/warranty shock, EV capacity underutilized kéo dài, finance credit loss tăng hoặc policy làm cost structure xấu hơn. Negative thesis có thể fail nếu premium/hybrid mix mạnh, localization giảm tariff burden, cost discipline tốt và software/EV investment tạo return nhanh hơn dự kiến.

## 15. Bài tập cuối case

Viết một margin bridge:

```text
Prior-year operating profit
+ volume effect
+ price/mix effect
+ FX effect
- incentive effect
- raw material/labor effect
- warranty effect
- transition cost
= current operating profit
```

Không cần số hoàn hảo. Việc buộc earnings change vào bridge giúp bạn phân biệt narrative với mechanism.

## Liên kết

Đọc cùng [15_automotive_battery_mobility](../15_automotive_battery_mobility.md), [35_financial_sector_securities_insurance_asset_management](../35_financial_sector_securities_insurance_asset_management.md), [21_economy_to_company_transmission](../21_economy_to_company_transmission.md) và [39_practical_company_analysis_workbook_and_case_patterns](../39_practical_company_analysis_workbook_and_case_patterns.md).