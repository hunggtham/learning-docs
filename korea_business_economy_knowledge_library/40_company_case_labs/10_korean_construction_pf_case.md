# Korean Construction & Project Finance — contractor profit, 시행사, PF guarantees và refinancing risk

Case này không dùng một company duy nhất mà dựng một **stylized Korean construction/PF case** để học một risk structure xuất hiện nhiều trong nền kinh tế Hàn Quốc. Construction company có thể report backlog và accounting profit ổn định trong khi project-finance exposure nằm ở guarantees, bridge loans, unsold units hoặc related SPV.

Vì vậy case này tập trung vào distinction giữa **construction operating business** và **project-finance contingent risk**.

Xem [18_construction_real_estate_and_project_finance](../18_construction_real_estate_and_project_finance.md), [36_credit_ratings_bonds_default_and_restructuring](../36_credit_ratings_bonds_default_and_restructuring.md) và [38_forensic_accounting_red_flags_and_earnings_quality](../38_forensic_accounting_red_flags_and_earnings_quality.md).

## 1. Ai là ai trong một development project?

Người mới thường gọi tất cả là “construction company”, nhưng một project có nhiều economic actors.

**Developer (시행사)** tìm land, structure project, obtain permits, arrange financing và chịu development economics.

**Contractor (시공사)** xây project theo contract. Trong Korea, large contractor có thể đồng thời provide credit enhancement hoặc participate economically sâu hơn pure builder.

**PF lender** cung cấp project financing dựa vào project cash flow/collateral/credit support.

**SPV/PFV** có thể là legal vehicle giữ project assets/liabilities.

**Trust company, securities company, savings bank, insurer hoặc other financial institutions** có thể tham gia funding structure.

Nếu không resolve roles, analyst rất dễ nhầm debt của SPV với contractor debt — hoặc ngược lại bỏ qua guarantee khiến SPV debt cuối cùng quay về contractor.

## 2. Project Finance khác corporate loan

Trong **corporate finance**, lender dựa nhiều vào overall company cash flow/balance sheet.

Trong **project finance (프로젝트 파이낸싱, PF)**, repayment logic tập trung vào project-specific cash flow.

Simplified:

```text
Land / permits
→ bridge financing
→ construction / 본PF
→ presales or leasing
→ completion
→ customer payment / asset sale
→ repay PF
```

Nhưng “non-recourse” trong theory không có nghĩa mọi Korean PF exposure hoàn toàn isolated. Guarantees, debt assumption, completion guarantee hoặc other credit support có thể reconnect project risk với sponsor/contractor.

## 3. Bridge loan — phase rủi ro trước khi project đủ điều kiện 본PF

**Bridge loan (브릿지론)** tài trợ giai đoạn sớm như land acquisition/initial development trước khi project đạt conditions cho main PF.

Risk cao vì:

```text
Permits chưa hoàn tất
Construction chưa bắt đầu
Presales chưa có
Exit phụ thuộc refinancing into 본PF
```

Nếu rates tăng hoặc project feasibility xấu đi, bridge loan có thể không refinance được.

Đây là classic maturity/refinancing risk.

## 4. Presales — 분양 và cash-flow model

Residential development Korea thường có **presale (분양)** structure quan trọng. Buyer commitments/payments có thể support project funding.

Project economics phụ thuộc:

\[
Expected\ Sales = Units \times Expected\ Selling\ Price
\]

nhưng feasibility phải trừ:

```text
Land
Construction
Finance cost
Marketing
Taxes/fees
Contingency
```

Nếu selling price bị capped hoặc demand yếu trong khi construction/interest cost tăng, expected developer margin bị compressed.

## 5. Contractor backlog không phải guarantee of profit

Construction backlog tạo revenue visibility nhưng margin phụ thuộc original bid assumptions và cost inflation.

Ví dụ stylized:

```text
Contract revenue = 1,000
Expected cost at signing = 900
Expected profit = 100
```

Nếu material/labor cost tăng khiến expected total cost thành 1,020, project chuyển từ +100 sang -20.

Long-duration contract vì vậy có **estimate risk**.

Accounting có thể recognize expected loss/provision trước full physical completion tùy standards và facts.

## 6. Percentage of completion và contract assets

Construction revenue thường được recognized theo progress khi criteria được đáp ứng.

Điều này tạo distinction:

```text
Accounting revenue recognized
vs billing issued
vs cash collected
```

Nếu recognized revenue chạy trước billing/cash, **contract asset (계약자산)** có thể tăng.

Contract asset tăng không tự động là red flag; nó có thể normal theo milestone. Nhưng nếu tăng nhanh hơn revenue nhiều periods, cần hỏi assumptions, billing disputes và collectability.

## 7. Guarantee — risk có thể nằm ngoài headline debt

Một contractor có corporate debt 2 trillion won nhưng additionally guarantee PF obligations cho projects. Nếu project fails và guarantee crystallizes, economic debt có thể tăng đột ngột.

Do đó:

\[
Economic\ Leverage \neq Reported\ Borrowings\ Alone
\]

Cần đọc:

```text
Borrowings
+ bonds
+ lease liabilities where relevant
+ guarantees / commitments
+ debt assumption obligations
+ liquidity support
```

không phải cộng tất cả mechanically, mà classify probability và conditions.

## 8. Completion guarantee — 책임준공

**Completion guarantee / 책임준공** có thể yêu cầu contractor hoàn thành construction dù developer gặp difficulty, tùy contract.

Điều này có economic value cho lenders vì giảm completion risk, nhưng transfer một phần risk sang contractor.

Analyst phải đọc exact obligation. Không nên coi mọi 책임준공 giống debt guarantee; legal mechanics khác nhau. Nhưng cũng không nên bỏ qua vì “không phải borrowing”.

## 9. Refinancing spiral

Một PF project có thể rơi vào adverse loop:

```text
Rates ↑ / property demand ↓
→ presales weak
→ project value / feasibility ↓
→ lenders demand higher spread or refuse refinance
→ finance cost ↑
→ feasibility worse
→ sponsor needs more equity/support
→ liquidity pressure spreads
```

Nếu nhiều projects cùng gặp problem, contractor/securities company exposure có thể become systemic.

Đây là connection giữa real estate và financial sector.

## 10. Unsold inventory — 미분양

**Unsold units (미분양)** là key signal nhưng cần context.

Unsold before completion có thể still sell later. Unsold completed units thường more severe vì construction cost đã spent và inventory financing continues.

Risk depends location, price, product quality và leverage.

Không chỉ đếm units; cần hỏi expected selling price có đủ cover remaining debt/cost không.

## 11. Regional divergence

Seoul/core 수도권 housing demand và provincial project economics có thể khác rất lớn.

National average house price có thể che local oversupply.

Project-level analysis cần:

```text
Local population / household formation
Jobs / transport
Competing supply
Presale absorption
Price vs local income
Land cost
```

Construction/PF là một trong những lĩnh vực mà geography trở thành financial variable trực tiếp.

Xem [24_regional_clusters_and_industrial_geography](../24_regional_clusters_and_industrial_geography.md).

## 12. Stylized project case

Giả sử một project:

```text
Expected sales: 1.5T KRW
Land + construction + other cost: 1.2T
Initial expected margin before financing: 0.3T
PF debt: 0.8T
```

Nếu sales price/absorption yếu làm expected sales giảm 10%:

\[
1.5T \times 0.9 = 1.35T
\]

Nếu construction cost đồng thời tăng 8% trên 0.8T construction component, cost tăng thêm 0.064T. Margin buffer bị compress mạnh.

Nếu completion delay làm finance cost tăng thêm, equity cushion có thể gần biến mất.

Điểm học: **small percentage shocks ở revenue và cost có thể destroy thin project equity** vì leverage.

## 13. Contractor stress test

Một coherent stress:

```text
Housing demand weak
→ presale ratio lower
→ project cash inflow delayed
→ PF refinancing spread +300bp
→ developer liquidity weakens
→ contractor provides support under guarantees
→ contractor CFO deteriorates
→ net debt rises
→ rating pressure
→ refinancing cost at corporate level rises
```

Đây là feedback loop giữa project và parent/company balance sheet.

## 14. Securities company/PF connection

PF risk không chỉ ở builders. Securities firms có thể arrange, guarantee, underwrite hoặc hold PF-related exposures.

Do đó real-estate downturn có thể transmit:

```text
Property project
→ developer
→ contractor
→ securities / savings bank / lender
→ short-term funding market
```

Đây là lý do construction chapter phải đọc cùng financial-sector chapter.

## 15. DART reading order cho contractor

```text
1. Segment revenue / backlog
2. Major project list
3. Cost estimates / provisions
4. Contract assets / receivables
5. Inventory / unsold exposure if disclosed
6. Borrowings and maturity
7. Guarantees / contingent liabilities
8. PF-related credit support
9. Related parties / SPVs
10. Cash flow and liquidity
```

Income statement chỉ là điểm bắt đầu.

## 16. Valuation: normalized earnings + contingent risk

P/E thấp của contractor có thể phản ánh cycle hoặc hidden PF concern.

Một simplified analytical bridge:

```text
Normalized construction earnings
+ value of other segments/assets
- net corporate debt
- probability-weighted contingent PF losses
= equity value framework
```

Probability-weighting không cần pretend precision. Mục tiêu là không đặt guarantee exposure bằng 0 hoặc 100% một cách máy móc.

## 17. Common misconceptions

### “Backlog lớn thì contractor an toàn”

Sai vì backlog margin và project financing risk khác nhau.

### “PF debt nằm ở SPV nên parent không liên quan”

Sai nếu có guarantees/support/strategic obligation.

### “Guarantee bằng debt ngay lập tức”

Cũng sai. Guarantee là contingent exposure; cần đọc trigger và probability.

### “House price quốc gia ổn thì mọi PF project ổn”

Sai vì real estate rất local.

## 18. Research workbook

| Driver | Y-4 | Y-3 | Y-2 | Y-1 | Y0 |
|---|---:|---:|---:|---:|---:|
| New orders | | | | | |
| Backlog | | | | | |
| Construction margin | | | | | |
| Contract assets | | | | | |
| Receivables | | | | | |
| Corporate debt | | | | | |
| PF guarantees | | | | | |
| CFO | | | | | |
| Interest expense | | | | | |

Bên cạnh table, lập **project exposure map** riêng thay vì chỉ total guarantees.

## Mental Model cuối

> Korean construction/PF analysis là bài toán **cash-flow timing + thin project equity + contingent recourse**. Contractor có thể trông khỏe trên income statement nhưng yếu nếu nhiều project cùng cần liquidity support. Luôn đi từ project economics → financing structure → legal obligation → corporate liquidity.

Case này hoàn tất một vòng quan trọng của practical layer: từ semiconductor, auto, platform, SME, SI/SM sang bank, battery, defense, commerce/logistics và real-estate finance. Khi gặp company mới, hãy chọn case có production function gần nhất rồi điều chỉnh driver tree thay vì bắt đầu từ zero.