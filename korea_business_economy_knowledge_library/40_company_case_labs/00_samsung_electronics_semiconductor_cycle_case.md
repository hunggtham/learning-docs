# Samsung Electronics Case Lab — từ consolidated company tới từng economic engine

Samsung Electronics là case rất tốt để học một lỗi phổ biến trong company analysis: **một legal entity có thể chứa nhiều business có production function hoàn toàn khác nhau**. Nếu chỉ nhìn consolidated revenue, operating profit và P/E, người đọc dễ bỏ qua việc semiconductor, smartphone, display và automotive electronics phản ứng với cycle theo những cách khác nhau.

Theo disclosure của Samsung Electronics, cấu trúc consolidated hiện gồm DX (Device eXperience), DS (Device Solutions), SDC và Harman. DX bao gồm các finished products như smartphone, TV và home appliances; DS gồm Memory, Foundry và System LSI. Vì vậy câu “Samsung earnings tăng” chưa phải explanation. Câu hỏi đúng là **engine nào tạo ra thay đổi, engine đó đang ở phase nào của cycle, và cash flow có bền sau CAPEX hay không**.

> Snapshot để luyện đọc: FY2025 consolidated sales được Samsung công bố ở mức khoảng KRW 333.6 trillion và operating profit khoảng KRW 43.6 trillion. Đây chỉ là mốc lịch sử để luyện decomposition, không phải assumption cho năm sau.

## 1. Entity resolution trước khi model

“Samsung” là group name, còn case này là **Samsung Electronics Co., Ltd.**. Samsung Electronics có subsidiaries được consolidate, nhưng không đồng nghĩa mọi affiliate mang brand Samsung đều nằm trong reporting perimeter của Samsung Electronics.

Đây là lý do bước đầu tiên trên DART phải là kiểm tra legal name, consolidated subsidiaries và segment note. Nếu nhầm group boundary với accounting boundary, analyst có thể gán asset, debt hoặc profit của một affiliate khác cho Samsung Electronics.

Mental model:

```text
Samsung Group
   ├─ Samsung Electronics ← entity đang phân tích
   │    ├─ DX
   │    ├─ DS
   │    ├─ SDC
   │    └─ Harman
   └─ other separate affiliates
```

## 2. Không có một “Samsung margin” duy nhất

DX và DS khác nhau từ gốc. DX bán finished products. Smartphone economics chịu ảnh hưởng của unit shipment, product mix, component cost, marketing, channel inventory và replacement cycle. DS semiconductor lại có fixed-cost intensity rất cao: fab phải gánh depreciation và engineering cost ngay cả khi utilization thấp.

Vì vậy cùng một mức revenue decline có thể tạo profit impact rất khác.

Một decomposition đơn giản cho DX:

\[
Revenue_{DX} \approx Units \times ASP
\]

\[
Operating\ Profit_{DX} \approx Revenue - Components - Manufacturing - Marketing - R\&D - SG\&A
\]

Trong DS Memory:

\[
Revenue_{Memory} \approx Bit\ Shipment \times ASP/bit
\]

\[
Gross\ Profit \approx Revenue - Wafer/Process\ Cost - Depreciation - Other\ Manufacturing\ Cost
\]

Khi ASP giảm nhanh hơn cost per bit, margin có thể collapse dù bit shipment vẫn tăng. Đây là lý do “volume growth” trong semiconductor không tự động nghĩa là earnings growth.

## 3. Memory cycle: từ end demand tới operating profit

Một memory upcycle thường không bắt đầu ở income statement. Nó bắt đầu ở quan hệ giữa demand growth và effective supply growth.

```text
AI / server / mobile / PC demand
        ↓
Bit demand
        ↕
Industry wafer capacity + node migration + yield
        ↓
Supply-demand balance
        ↓
ASP
        ↓
Revenue
        ↓
Utilization + product mix + cost/bit
        ↓
Operating profit
```

Nếu analyst chỉ theo spot price, họ có thể bỏ qua contract pricing, product mix và HBM/DDR/NAND composition. Nếu chỉ theo shipment, họ bỏ qua ASP. Nếu chỉ theo operating profit, họ nhìn quá muộn.

## 4. Foundry không nên được model như Memory

Memory sản xuất standardized products hơn và cycle chịu ảnh hưởng mạnh của industry supply discipline. Foundry là manufacturing service cho chip design customers. Economics phụ thuộc technology node, customer qualification, design win, yield và fab utilization.

Hai fab có cùng nominal capacity nhưng economic output khác rất xa nếu một fab chạy high-yield leading-node product còn fab kia underutilized hoặc yield thấp.

Một simplified foundry model:

\[
Revenue \approx Wafer\ Starts \times Utilization \times Revenue/Wafer
\]

nhưng margin cần thêm yield:

\[
Economic\ Output \propto Good\ Dies = Wafer\ Starts \times Dies/Wafer \times Yield
\]

Do đó khi đọc capex, không hỏi chỉ “Samsung đầu tư bao nhiêu”. Hãy hỏi **capex đó đi vào memory, foundry, advanced packaging hay infrastructure; utilization/yield cần đạt mức nào để ROIC vượt cost of capital**.

## 5. CAPEX, depreciation và FCF: nơi semiconductor story trở thành finance

Semiconductor leadership cần investment trước revenue. Cash ra ở thời điểm equipment/fab được xây; depreciation đi vào accounting profit dần theo useful life.

Điều này tạo ba thời điểm khác nhau:

```text
Investment decision
→ Cash CAPEX
→ Capacity becomes available
→ Production / qualification
→ Revenue
→ Depreciation continues over useful life
```

Một upcycle có thể tạo operating cash flow rất lớn nhưng đồng thời kéo theo CAPEX lớn. Vì vậy nên theo ít nhất:

\[
FCF \approx CFO - CAPEX
\]

và:

\[
CAPEX / Depreciation
\]

Nếu CAPEX liên tục vượt depreciation rất mạnh, company đang mở rộng asset base; analyst cần chứng minh future demand và return, không chỉ gọi đó là “growth investment”.

## 6. Worked example bằng số giả định

Giả sử Memory business có:

```text
Năm 1:
Bit shipment = 100
ASP/bit = 1.00
Cost/bit = 0.75

Năm 2:
Bit shipment +20% → 120
ASP/bit -15% → 0.85
Cost/bit -10% → 0.675
```

Revenue:

\[
100 \times 1.00 = 100
\]

sang:

\[
120 \times 0.85 = 102
\]

Revenue tăng 2%, nhìn bề ngoài ổn. Nhưng unit gross spread thay từ `0.25` xuống `0.175`. Approximate gross contribution:

\[
100 \times 0.25 = 25
\]

sang:

\[
120 \times 0.175 = 21
\]

Volume tăng 20% nhưng contribution giảm. Đây là bài học cốt lõi của commodity-like semiconductor economics: **price-cost spread quan trọng hơn shipment headline**.

## 7. DX: product mix quan trọng hơn unit count đơn thuần

Với smartphone, cùng 100 triệu units nhưng mix flagship cao hơn có thể tạo revenue và margin khác hẳn. Tuy nhiên ASP cao không đủ nếu component cost, promotion hoặc channel incentives tăng mạnh.

Driver tree nên là:

```text
Smartphone demand
→ units
→ premium / mass mix
→ ASP
→ component BOM
→ marketing + channel incentives
→ margin
```

Khi semiconductor price tăng, điều thú vị là Samsung Electronics vừa có thể hưởng lợi ở DS vừa chịu higher component cost ở DX. Consolidation có thể che một phần internal economic offset này.

## 8. SDC và Harman: tại sao diversification cần decomposition

Display có cycle, customer concentration và technology-transition economics riêng. Harman lại gắn nhiều hơn với automotive electronics, infotainment và vehicle production cycle. Hai business này không nên bị coi như “other” nếu contribution trở nên material.

Diversification giúp consolidated company không phụ thuộc duy nhất một cycle, nhưng không xóa cycle. Nó tạo **portfolio of cycles**.

## 9. DART reading mission

Khi mở annual/business report, không đọc từ trang đầu tới cuối. Hãy tìm theo sequence:

```text
1. 사업의 내용 / business overview
2. segment revenue and operating profit
3. inventories
4. property, plant and equipment
5. depreciation
6. cash flow / CAPEX clues
7. commitments
8. related parties
9. shareholder return / treasury shares
10. auditor and accounting-policy changes
```

Sau đó tạo bảng năm năm cho revenue, operating profit, CFO, CAPEX, cash, debt và segment mix. Mục tiêu là nhìn được cycle chứ không phải thuộc một năm.

## 10. Macro transmission

Samsung Electronics là một node nơi nhiều macro variables hội tụ.

KRW yếu có thể hỗ trợ translation/export economics nhưng impact thực phụ thuộc currency mix của revenue và cost. Global rate cao có thể làm electronics demand yếu nhưng đồng thời AI infrastructure spending có thể đi theo cycle riêng. Trade restrictions và export controls có thể ảnh hưởng market access, equipment và customer behavior. Energy cost ảnh hưởng manufacturing; consumer confidence ảnh hưởng devices; hyperscaler CAPEX ảnh hưởng AI memory.

Do đó không dùng rule đơn giản kiểu “KRW yếu = Samsung tốt”. Hãy trace từng variable qua từng segment.

## 11. Scenario lab

Một scenario coherent nên thay đổi driver có quan hệ với nhau.

### Memory-downturn scenario

Giả định:

```text
Conventional memory ASP: -20%
HBM mix: tăng nhưng không đủ offset
Bit shipment: +8%
Utilization: giảm
Cost/bit: -7%
CAPEX: giảm với độ trễ
DX demand: flat
```

Câu hỏi không phải tính target price ngay. Hãy trace:

```text
ASP ↓
→ DS revenue/margin ↓
→ CFO ↓
→ inventory risk ↑
→ CAPEX adjustment lag
→ FCF compression
```

Sau đó hỏi balance sheet có đủ sức tiếp tục strategic CAPEX trong downturn không. Đây là nơi financial strength có thể trở thành competitive advantage: company có thể tiếp tục đầu tư khi weaker competitor phải cut sâu hơn.

## 12. Valuation logic

Không nên áp một multiple duy nhất mà không nghĩ tới segment mix. Peak semiconductor earnings có thể làm P/E nhìn “rẻ” đúng lúc cycle gần peak; trough earnings làm P/E nhìn “đắt” đúng lúc cycle gần đáy.

Một cách tư duy tốt hơn là normalized earnings hoặc sum-of-the-parts như một analytical lens, không nhất thiết để tạo target price:

```text
Normalized DS earning power
+ normalized DX earning power
+ SDC/Harman value
+ net cash / financial assets adjustment
- holding / governance / execution risks if relevant
```

Mục tiêu là tách **cyclical earnings** khỏi **structural earning power**.

## 13. Thesis breakers

Một bullish semiconductor thesis phải có điều kiện bị bác bỏ. Ví dụ: HBM/product qualification chậm, yield không cải thiện, competitor supply tăng nhanh hơn demand, foundry utilization không đủ hấp thụ fixed cost, hoặc CAPEX tăng nhưng ROIC không cải thiện.

Một bearish thesis cũng cần breaker: demand mạnh hơn dự kiến, supply discipline tốt hơn, cost/bit giảm nhanh, mix chuyển sang high-value products hoặc DX tạo cash flow tốt hơn dự kiến.

Không có thesis breaker thì đó là narrative, chưa phải analysis.

## 14. Bài tập cuối case

Tự tạo một memo một trang với đúng sáu heading:

```markdown
## Entity and Reporting Boundary
## Earnings Engines
## Three Dominant Drivers
## Cash and CAPEX
## Downside Stress
## What Evidence Would Change My View?
```

Nếu sáu section này rõ ràng, bạn đã chuyển từ “biết Samsung” sang **có thể phân tích Samsung Electronics như một economic system**.

## Liên kết

Đọc cùng [14_semiconductors_electronics_display](../14_semiconductors_electronics_display.md), [09_disclosure_accounting_dart_kind](../09_disclosure_accounting_dart_kind.md), [21_economy_to_company_transmission](../21_economy_to_company_transmission.md) và [38_forensic_accounting_red_flags_and_earnings_quality](../38_forensic_accounting_red_flags_and_earnings_quality.md).