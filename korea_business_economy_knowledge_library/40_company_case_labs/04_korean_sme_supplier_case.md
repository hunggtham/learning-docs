# Korean SME Supplier Case Lab — customer concentration, bargaining power và cash conversion

Case này dùng một **doanh nghiệp giả lập** để mô phỏng cấu trúc thường gặp trong manufacturing supply chain Hàn Quốc. Dùng company giả lập giúp ta tập trung vào mechanism mà không biến bài học thành nhận xét về một SME cụ thể.

Giả sử `Hanbit Precision (한빛정밀)` sản xuất precision metal/plastic modules cho hai khách hàng lớn trong automotive/electronics. Công ty có công nghệ process riêng ở mức vừa phải, nhưng drawing/specification chủ yếu do customer quyết định. Revenue tăng khá nhanh vì customer volume tăng, trong khi payment term dài và annual price-down tạo pressure lên margin.

Đây là case để hiểu một nghịch lý: **supplier có thể tăng revenue và accounting profit nhưng cash vẫn xấu đi**.

## 1. Economic position trong value chain

Hanbit không bán trực tiếp cho end consumer. Demand của nó là derived demand:

```text
End-market demand
→ OEM production
→ Tier-1 order
→ Hanbit order
```

Mỗi layer có thể truyền shock xuống supplier. Nếu OEM giảm production 10%, supplier có thể giảm hơn 10% nếu customer destock inventory.

Supplier còn chịu asymmetric bargaining power: customer lớn có nhiều sourcing options hơn supplier có customer options.

## 2. Revenue driver

Simplified:

\[
Revenue = Customer\ Production\ Volume \times Content\ per\ Unit \times Unit\ Price
\]

Growth có ba nguồn:

```text
customer volume tăng
content per unit tăng
new customer / new program win
```

Unit price thường không phải growth engine mạnh vì customer có annual cost-down negotiation.

Nếu revenue tăng chỉ vì một customer mở plant mới, concentration risk có thể tăng cùng lúc với growth.

## 3. Annual price-down và productivity race

Giả sử customer yêu cầu price giảm 3% mỗi năm. Supplier chỉ giữ margin nếu productivity/cost reduction ít nhất bù được phần đó.

```text
Year 1 unit price = 100
Year 2 price-down 3% → 97
```

Nếu process improvement làm cost giảm từ 90 xuống 86:

```text
Year 1 spread = 10
Year 2 spread = 11
```

Margin vẫn tốt hơn dù selling price giảm.

Nhưng nếu labor/material cost tăng làm cost thành 92:

```text
Year 2 spread = 5
```

Revenue có thể vẫn tăng nhờ volume, trong khi margin per unit collapse.

Đây là lý do supplier analysis phải tách **volume growth** khỏi **economic value per unit**.

## 4. Customer concentration

Giả định revenue mix:

```text
Customer A = 55%
Customer B = 25%
Others = 20%
```

Top-2 = 80%. Điều này tạo dependency không chỉ ở sales mà còn ở tooling, quality standard, engineering team và plant location.

Nếu Customer A yêu cầu supplier xây line mới gần factory của họ, supplier có thể bỏ CAPEX trước khi volume fully guaranteed.

Concentration risk nên được nhìn qua:

```text
revenue concentration
receivable concentration
program concentration
geographic concentration
technology/spec concentration
```

Một supplier có 10 customers nhưng 70% revenue vẫn đến từ một platform/model thì diversification thực tế thấp.

## 5. Working capital: nơi growth hút cash

Giả sử payment term là 90 ngày nhưng supplier phải trả labor và nhiều materials trong 30 ngày.

Growth chain:

```text
new order
→ buy materials
→ build WIP
→ ship product
→ record revenue/receivable
→ wait 90 days
→ collect cash
```

Accounting profit xuất hiện trước cash collection.

Working-capital approximation:

\[
Cash\ Conversion\ Cycle = DIO + DSO - DPO
\]

Nếu DIO = 45 ngày, DSO = 90 ngày và DPO = 40 ngày:

\[
CCC = 45 + 90 - 40 = 95\ days
\]

Company phải finance gần ba tháng operating cycle.

## 6. Worked growth example

Year A:

```text
Revenue = 10,000
Operating margin = 8%
Operating profit = 800
Receivable = 2,000
Inventory = 1,200
Payable = 900
```

Year B order boom:

```text
Revenue = 13,000 (+30%)
Operating margin = 7%
Operating profit = 910
Receivable = 3,500
Inventory = 1,900
Payable = 1,100
```

Profit tăng 110. Nhưng net operating working capital tăng:

```text
Year A = 2,000 + 1,200 - 900 = 2,300
Year B = 3,500 + 1,900 - 1,100 = 4,300
Increase = 2,000
```

Company tạo thêm 110 operating profit nhưng cần thêm khoảng 2,000 working capital. Nếu không có cash reserve, supplier phải vay.

Đây là lý do “growth company” có thể đồng thời tăng leverage.

## 7. Tooling và customer-specific CAPEX

Supplier thường mua mold, die, jig, machine hoặc inspection equipment cho program cụ thể. Câu hỏi accounting là ai sở hữu tooling và cost được recover thế nào.

Possible structures:

```text
customer pays tooling upfront
supplier owns and depreciates tooling
cost embedded in unit price
cost reimbursed after milestone
```

Nếu supplier bỏ CAPEX nhưng program volume thấp hơn forecast, depreciation vẫn tồn tại. Project có thể profitable trên quote nhưng underperform ở realized volume.

## 8. Raw-material pass-through

Nếu metal/resin price tăng, supplier có thể hoặc không thể pass-through.

Ba cases:

```text
full pass-through → margin relatively protected
lagged pass-through → temporary working-capital/margin pressure
no pass-through → supplier absorbs shock
```

Contract language và bargaining power quyết định economics. Vì vậy commodity price exposure không thể suy ra chỉ từ material type.

## 9. Quality failure và hidden tail risk

Manufacturing supplier có thể chịu claim lớn nếu defect làm customer line stop hoặc recall.

Expected-loss structure:

```text
scrap/rework
+ expedited shipping
+ customer chargeback
+ line-stop compensation
+ recall exposure
+ future order loss
```

Một defect nhỏ về unit count có thể gây economic loss lớn nếu component nằm sâu trong assembled product.

Quality metrics vì vậy là leading indicator của finance.

## 10. Labor và subcontracting

SME supplier thường có labor constraint mạnh hơn chaebol. Wage inflation, overtime, foreign labor availability và subcontracting ảnh hưởng unit cost.

Nếu company tăng subcontractor ratio để đáp ứng peak demand, variable flexibility tăng nhưng quality/control và unit cost có thể xấu.

Khi đọc SG&A/manufacturing cost, cố gắng hiểu headcount, overtime, outsourced process và automation investment.

## 11. Customer relocation và overseas expansion

Khi Korean OEM mở plant ở Vietnam, US, Mexico hoặc Europe, supplier có thể bị yêu cầu follow customer.

Decision tree:

```text
Follow customer abroad?
├─ Yes → CAPEX + local hiring + FX + execution risk
└─ No  → risk losing future program
```

FDI của supplier vì vậy không chỉ là growth opportunity; đôi khi là **defensive investment để giữ customer relationship**.

Đây là connection trực tiếp giữa [23_foreign_invested_companies_and_korea_entry](../23_foreign_invested_companies_and_korea_entry.md) và SME economics.

## 12. Debt capacity

Bank có thể finance working capital và equipment, nhưng supplier cash flow biến động theo customer orders.

Theo dõi:

```text
short-term borrowings
interest coverage
receivable-backed lending
maturity concentration
customer concentration
collateral
```

Một company có low accounting leverage cuối năm nhưng dùng seasonal borrowing lớn trong năm vẫn có liquidity risk.

## 13. Scenario lab — customer loss

Giả định Customer A = 55% revenue và mất 40% order volume.

Không giảm cost theo tỷ lệ revenue ngay vì fixed labor, rent, depreciation và dedicated equipment vẫn tồn tại.

```text
Revenue shock
→ utilization ↓
→ fixed cost/unit ↑
→ margin ↓ mạnh
→ inventory/WIP write-down risk ↑
→ covenant / debt pressure ↑
```

Nếu customer-specific equipment không dùng cho customer khác được, asset impairment có thể xuất hiện.

## 14. Scenario lab — rapid growth

Giả định new EV program làm revenue +50% nhưng customer payment term 120 ngày.

Positive income statement có thể đi cùng:

```text
inventory ↑
receivable ↑↑
CAPEX ↑
short-term borrowing ↑
interest expense ↑
```

Nếu program ramp chậm, company có cả excess inventory lẫn debt.

Growth stress test vì vậy quan trọng không kém downturn stress test.

## 15. Supplier moat

Supplier moat không nhất thiết là brand. Nó có thể là:

```text
process know-how
low defect rate
qualification history
co-design capability
fast engineering response
location/logistics integration
switching/qualification cost
patents/proprietary material
```

Nhưng relationship lâu năm không tự động là moat nếu customer có thể dual-source dễ dàng.

Hãy hỏi: **customer mất gì nếu đổi supplier?** Nếu answer gần bằng zero, bargaining power của supplier yếu.

## 16. Forensic checks

Red flags đáng chú ý:

```text
receivable tăng nhanh hơn revenue
inventory tăng trong khi customer production giảm
CFO thấp hơn net income nhiều năm
frequent short-term refinancing
related-party sales/purchases lớn
CAPEX tăng nhưng utilization thấp
customer advances giảm trong khi backlog narrative mạnh
```

Một red flag không chứng minh fraud. Nó là nơi cần investigation.

## 17. Valuation logic

SME supplier thường không nên được valued chỉ bằng growth rate. Quality of revenue quan trọng hơn:

```text
customer diversification
margin durability
cash conversion
technology ownership
balance-sheet resilience
program visibility
```

Revenue +30% với negative FCF và rising concentration có thể có quality thấp hơn revenue +8% với strong cash conversion và diversified customers.

## 18. Bài tập cuối case

Tạo một supplier scorecard không dùng điểm số tổng hợp. Chỉ ghi evidence theo sáu dimensions:

| Dimension | Evidence cần tìm |
|---|---|
| Customer power | top-customer %, contract, price-down |
| Technology | qualification, patent/process, switching cost |
| Cash conversion | DSO, DIO, DPO, CFO/net income |
| CAPEX | dedicated vs reusable assets |
| Funding | short-term debt, maturity, interest coverage |
| Downside | customer loss, defect, relocation |

Mục tiêu không phải xếp hạng supplier mà là biết **risk nằm ở đâu và truyền vào cash như thế nào**.

## Liên kết

Đọc cùng [06_sme_mid_sized_and_subcontracting_ecosystem](../06_sme_mid_sized_and_subcontracting_ecosystem.md), [02_trade_export_and_global_value_chains](../02_trade_export_and_global_value_chains.md), [23_foreign_invested_companies_and_korea_entry](../23_foreign_invested_companies_and_korea_entry.md) và [36_credit_ratings_bonds_default_and_restructuring](../36_credit_ratings_bonds_default_and_restructuring.md).