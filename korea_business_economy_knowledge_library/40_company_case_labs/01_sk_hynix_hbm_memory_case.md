# SK hynix Case Lab — HBM, memory cycle và economics của capacity allocation

SK hynix là case phù hợp để học cách một company vẫn thuộc ngành memory semiconductor nhưng economic mix có thể thay đổi mạnh khi AI infrastructure làm HBM trở nên quan trọng hơn. Phân tích tốt phải tránh hai cực: coi memory hoàn toàn là commodity cũ, hoặc coi HBM là một business miễn nhiễm với cycle.

SK hynix bán DRAM và NAND cùng các memory solutions liên quan. FY2025 là một snapshot đặc biệt mạnh: công ty công bố revenue khoảng KRW 97.1 trillion và operating profit khoảng KRW 47.2 trillion, với HBM và high-value AI memory là động lực quan trọng. Chính vì profitability ở mức rất cao, case này đặc biệt hữu ích để học **normalization**: peak/current earnings không được tự động extrapolate vô hạn.

## 1. Bắt đầu từ demand architecture, không bắt đầu từ ticker

Memory demand là derived demand. Người dùng không mua DRAM vì muốn sở hữu DRAM; memory được kéo bởi server, accelerator, PC, mobile, storage và các systems khác.

Với AI infrastructure, chain có thể viết:

```text
AI workload
→ accelerator / compute deployment
→ memory bandwidth requirement
→ HBM content per accelerator/system
→ HBM demand
→ wafer + packaging capacity requirement
→ shipment / ASP / mix
→ revenue and margin
```

Mỗi arrow có thể fail. AI model growth không tự động chuyển 1:1 thành SK hynix revenue nếu customer qualification, packaging capacity hoặc competitive supply thay đổi.

## 2. HBM không chỉ là “DRAM đắt hơn”

HBM tạo economic differentiation qua bandwidth, stacking, advanced packaging, thermal/power constraints, yield và qualification. Vì product phức tạp hơn, value capture có thể cao hơn conventional memory trong một giai đoạn.

Nhưng analyst phải hỏi bốn câu:

**Capacity:** bao nhiêu wafer và packaging capacity có thể chuyển sang HBM?

**Yield:** good output trên input wafer/stack là bao nhiêu?

**Qualification:** customer đã approve product ở generation nào?

**Mix:** HBM tăng có cannibalize/constrain conventional DRAM supply và làm industry pricing thay đổi không?

Điểm cuối rất quan trọng. Capacity allocation cho HBM có thể tác động cả economics của conventional DRAM thông qua opportunity cost.

## 3. Driver tree của memory producer

Một model tối giản:

\[
Revenue = \sum_i BitShipment_i \times ASP_i
\]

với `i` là HBM, server DRAM, mobile DRAM, NAND/eSSD và các product categories khác.

Cost không chỉ là raw material. Semiconductor có:

```text
wafer/process cost
+ depreciation
+ packaging/test
+ yield loss
+ engineering/R&D
+ power/utilities
```

Cost per bit thường giảm nhờ node migration, density và yield improvement. Nhưng transition ban đầu có thể làm yield thấp hoặc equipment/depreciation tăng trước khi cost advantage xuất hiện.

## 4. Capacity allocation là capital-allocation problem ở cấp fab

Giả sử một lượng wafer capacity có thể dùng cho product A hoặc B. Company không chỉ hỏi product nào có ASP cao hơn mà phải hỏi contribution sau yield, packaging bottleneck, qualification và long-term customer relationship.

Stylized example:

```text
Conventional DRAM:
Revenue equivalent / wafer = 100
Variable + conversion cost = 60
Contribution = 40

HBM:
Potential revenue / wafer = 190
Higher process/packaging/yield cost = 105
Contribution = 85
```

Nếu HBM contribution cao hơn, chuyển wafer sang HBM có vẻ hợp lý. Nhưng nếu yield thực tế thấp làm cost tăng thêm 40, contribution chỉ còn 45. Vì vậy product headline không thay thế manufacturing execution.

## 5. HBM mix và operating leverage

Khi high-value product mix tăng, blended ASP và margin có thể tăng nhanh hơn bit shipment. Điều này khiến analyst dễ kết luận rằng historical cycle đã biến mất.

Cần tách:

```text
Structural effect: AI memory content tăng dài hạn
Cyclical effect: supply-demand tightness đẩy ASP/margin lên cao
Execution effect: company có yield/qualification tốt hơn competitor
```

Ba effect cùng xuất hiện trong earnings nhưng valuation implication khác nhau. Structural advantage có thể bền; cyclical scarcity thường thu hút capacity và competition; execution edge cần tiếp tục được chứng minh qua generation mới.

## 6. NAND và eSSD không được bỏ qua

Khi narrative thị trường tập trung vào HBM, NAND có thể bị analyst xem như phần phụ. Nhưng NAND vẫn ảnh hưởng inventory, asset utilization, cash flow và consolidated profitability.

AI data center cũng có storage demand, nhưng NAND economics khác DRAM/HBM. Hãy theo enterprise SSD mix, layer transition, industry supply discipline và inventory.

Một company có HBM rất mạnh vẫn có thể chịu drag nếu một memory segment khác rơi vào severe downturn.

## 7. CAPEX: growth hay replacement?

Không phải toàn bộ CAPEX đều tạo capacity mới. Một phần dùng cho technology migration, equipment replacement, cleanroom/infrastructure và packaging.

Khi đọc disclosure, cố gắng phân loại:

```text
Maintenance / replacement CAPEX
Technology migration CAPEX
Capacity expansion CAPEX
Advanced packaging CAPEX
Strategic geographic CAPEX
```

Sau đó hỏi return source của từng bucket.

Một fab investment lớn có thể cần nhiều năm trước khi full utilization. Vì vậy model phải có time lag giữa cash outflow và earnings contribution.

## 8. Cash-flow normalization ở năm lợi nhuận cao

Khi margin tăng mạnh, CFO có thể tăng rất nhanh. Nhưng memory producer thường phải quyết định giữa:

```text
future CAPEX
+ balance-sheet strengthening
+ debt reduction
+ dividends / buybacks / treasury-share cancellation
+ strategic investment
```

FY2025 SK hynix là ví dụ hữu ích vì công ty đồng thời nói về future investment, financial stability và shareholder return. Analytical question không phải “return shareholder hay invest, cái nào tốt hơn”, mà là **marginal return on each use of cash**.

Nếu future HBM capacity tạo ROIC cao, underinvestment cũng có opportunity cost. Nếu cycle gần peak và capacity expansion quá aggressive, overinvestment có thể phá value.

## 9. Worked cycle example

Giả định blended business:

```text
Year A:
Bit shipment = 100
Blended ASP = 1.00
Cost/bit = 0.65

Year B:
Bit shipment = 115
HBM mix ↑
Blended ASP = 1.20
Cost/bit = 0.62
```

Revenue tăng từ `100` lên `138`. Approximate spread contribution tăng từ:

\[
100 \times (1.00 - 0.65) = 35
\]

thành:

\[
115 \times (1.20 - 0.62) = 66.7
\]

Revenue +38% nhưng contribution gần gấp đôi. Đây là operating leverage + mix effect.

Bây giờ stress Year C:

```text
Bit shipment +10%
ASP -25%
Cost/bit -8%
```

Ngay cả khi volume tiếp tục tăng, spread có thể co rất mạnh. Đây là lý do valuation phải stress ASP và mix, không chỉ bit growth.

## 10. Customer concentration và qualification

HBM gắn chặt với accelerator/platform roadmap. Qualification delay vài tháng có thể dịch revenue giữa quarter hoặc generation, đồng thời làm inventory/capacity utilization khác kỳ vọng.

Câu hỏi cần hỏi:

```text
Customer concentration bao nhiêu?
Product generation nào đã qualified?
Volume commitment có binding hay forecast-based?
Packaging bottleneck nằm ở đâu?
Customer có dual-source không?
Next-generation transition có giữ được position không?
```

Không cần biết mọi confidential detail. Chỉ cần nhận ra rằng customer roadmap là một part của production economics.

## 11. Inventory là tín hiệu, không phải kết luận

Inventory tăng có thể xấu nếu demand yếu và price sắp giảm. Nhưng inventory tăng trước product ramp hoặc để phục vụ committed demand có interpretation khác.

Do đó dùng triangle:

```text
Inventory growth
vs Revenue growth
vs ASP / demand commentary
```

Nếu inventory tăng nhanh hơn revenue trong khi management nói demand strong, hãy kiểm tra product mix, WIP, finished goods và transition timing trước khi kết luận.

## 12. Macro và geopolitics

Memory company chịu tác động của global electronics demand, hyperscaler CAPEX, FX, interest-rate-sensitive tech spending, equipment/export controls, geographic manufacturing policy và energy/infrastructure availability.

Không biến geopolitics thành slogan. Hãy map nó vào một trong năm channel:

```text
market access
customer access
equipment access
production location/cost
required duplicated CAPEX
```

Chỉ khi xác định channel mới có thể translate sang financial model.

## 13. Scenario lab

### Bear scenario

```text
AI infrastructure growth chậm lại
HBM supply tăng nhanh
HBM ASP premium co lại
Conventional DRAM ASP -20%
NAND recovery yếu
CAPEX commitments vẫn cao trong 12 tháng đầu
```

Trace:

```text
blended ASP ↓
→ gross margin ↓
→ CFO ↓
→ CAPEX/CFO ↑
→ FCF ↓
→ shareholder-return flexibility ↓
```

### Structural-strength scenario

```text
AI memory content/system tiếp tục tăng
next-generation qualification đúng lịch
HBM mix ↑
yield cải thiện
conventional memory supply discipline giữ được
```

Khi đó earnings growth đến từ cả volume, mix và cost. Nhưng analyst vẫn phải hỏi market valuation đã price-in bao nhiêu phần của scenario này.

## 14. Reverse valuation

Thay vì hỏi “P/E bao nhiêu là hợp lý?”, hãy hỏi current enterprise/equity value cần normalized earnings nào để hợp lý.

Nếu valuation chỉ hợp lý khi current peak margin kéo dài nhiều năm, thesis phụ thuộc vào assumption mạnh. Nếu valuation vẫn hợp lý khi ASP/margin normalize đáng kể, downside architecture khác.

Reverse valuation buộc bạn tách:

```text
current earnings
normalized earnings
structural growth premium
cycle premium/discount
```

## 15. Thesis breakers

Một positive thesis có thể bị phá bởi qualification failure, yield lag, competitor HBM ramp nhanh, customer concentration shock, industry oversupply hoặc CAPEX return thấp. Một negative thesis có thể bị phá bởi stronger-than-expected AI memory content, supply constraints kéo dài, superior execution hoặc cost decline nhanh.

Case này dạy một nguyên tắc quan trọng:

> **HBM có thể thay đổi shape của memory cycle, nhưng không xóa economics của capacity, yield, price, CAPEX và competition.**

## 16. Bài tập

Tạo bảng năm năm gồm revenue, operating margin, CFO, CAPEX, net cash/debt và inventory. Sau đó viết ba dòng cho mỗi năm: `cycle`, `mix`, `execution`. Mục tiêu là giải thích earnings change bằng ba layer thay vì chỉ copy management commentary.

## Liên kết

Đọc cùng [14_semiconductors_electronics_display](../14_semiconductors_electronics_display.md), [21_economy_to_company_transmission](../21_economy_to_company_transmission.md), [36_credit_ratings_bonds_default_and_restructuring](../36_credit_ratings_bonds_default_and_restructuring.md) và [39_practical_company_analysis_workbook_and_case_patterns](../39_practical_company_analysis_workbook_and_case_patterns.md).