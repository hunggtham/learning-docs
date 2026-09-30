# Doanh nghiệp và kinh tế Hàn Quốc — kiểm toán phạm vi

> **Mạch đọc:** Đọc tệp này sau [`README.md`](./README.md). README trình bày đường đi từ lịch sử và thể chế tới doanh nghiệp, kế toán, nguồn vốn và ngành; audit này trả lời: **coverage hiện đã đủ tới đâu, dữ kiện nào phải có provenance theo thời điểm, và các case/company chapter cần dùng cùng một khung reasoning như thế nào để so sánh được?**

**Ngày rà soát:** 2026-09-29.

## 1. Phạm vi sở hữu

Domain này sở hữu lớp ứng dụng của kinh tế và doanh nghiệp Hàn Quốc: lịch sử phát triển, thể chế, điều kiện vĩ mô, cấu trúc ngành, hành vi doanh nghiệp, kế toán/dòng tiền, tài trợ, quản trị, thị trường vốn và company/sector cases.

Lý thuyết kinh tế tổng quát và econometrics thuộc [Economics](../economics/README.md); portfolio/investment decision thuộc [Investing](../investing/README.md); chronology Hàn Quốc thuộc [Korean History](../korean_history/README.md); xã hội/văn hóa công sở thuộc [Korean Culture](../korean_culture/README.md); quyền/thủ tục pháp lý hiện hành thuộc [Korea Law/Civic Life](../korea_law_civic_life/README.md).

Ranh giới này giúp domain trả lời “cơ chế đó biểu hiện trong doanh nghiệp và ngành Hàn Quốc ra sao?” thay vì viết lại theory hoặc chuyển thành khuyến nghị mua/bán tài sản.

## 2. Coverage hiện đã mạnh

Mạch root hiện có kiến trúc nhân quả hợp lý:

```text
lịch sử
→ thể chế
→ vốn / lao động / công nghệ
→ cấu trúc ngành
→ hành vi doanh nghiệp
→ kế toán / dòng tiền
→ tài trợ / quản trị
→ giá trị thị trường và rủi ro
```

Coverage đã rộng ở công nghiệp hóa, macro/business cycle, thương mại và chuỗi giá trị; chaebol, SME/startup, ownership/control; DART/KIND, accounting/disclosure; ngân hàng, trái phiếu, credit/restructuring; labor/organization; và nhiều ngành từ semiconductor, auto/battery, shipbuilding, construction/PF tới platform, finance, energy, logistics, biohealth và cloud/IT services.

Vì độ rộng đã lớn, giá trị của vòng tiếp theo nằm ở **chất lượng bằng chứng, khả năng so sánh và kỷ luật cập nhật**, không phải thêm thật nhiều sector chapter mới.

## 3. Hợp đồng reasoning cho company/sector chapter

Một chapter doanh nghiệp/ngành nên nối được:

```text
ràng buộc thị trường/thể chế
→ business model
→ volume / price / unit economics
→ capacity + utilization
→ working capital + capex
→ accounting statement
→ cash flow
→ funding + liquidity
→ ownership + control
→ downside/failure mode
→ observable evidence
```

Nếu giải thích macro tác động đến doanh nghiệp, không nên dừng ở “GDP/lãi suất/xuất khẩu tăng hay giảm”. Cần chỉ ra transmission path tới revenue, cost, balance sheet, funding hoặc cash flow nhạy với valuation.

## 4. Dữ kiện nhạy theo thời gian

Market share, ranking, doanh thu/lợi nhuận/dòng tiền, ownership stake, group structure, listing/index membership, policy/subsidy/tax, lãi suất, tỷ giá, credit rating, capacity/utilization, export mix và management guidance đều là dữ kiện động.

Khi dùng các fact này, phải truy ngược được:

```text
entity/metric
→ reporting period hoặc as-of date
→ source
→ accounting/statistical definition
→ revision/restatement risk
```

Mechanism chapter có thể bền lâu; current company/market fact thì không. Không ghi “Samsung chiếm X%” hoặc “debt ratio là Y” như chân lý không có ngày.

## 5. Ranh giới dễ nhầm

**Korea-specific application và Economics:** theory về monetary transmission, market structure, causal inference hay trade model nên link sang Economics; domain này cho thấy theory đó đi qua institution/sector/company Hàn Quốc như thế nào.

**Company analysis và investment advice:** có thể phân tích earnings quality, leverage, capital allocation, valuation inputs và risk; không biến thư viện thành “nên mua cổ phiếu nào”.

**Business culture và Korean Culture:** reporting/approval/decision right/incentive thuộc đây khi liên quan trực tiếp tới vận hành doanh nghiệp; nền xã hội rộng hơn bàn giao sang Korean Culture.

**Regulation và legal procedure:** domain này giải thích regulation ảnh hưởng economics của ngành/doanh nghiệp ra sao; quyền và thủ tục cá nhân thuộc Korea Law/Civic Life.

## 6. Khoảng trống ưu tiên

### P1 — Company evidence sheet dùng chung

Cần một template để case khác nhau có thể so sánh:

```text
business model
→ segment/geography
→ revenue drivers
→ cost structure
→ capacity/utilization
→ working capital
→ capex/depreciation
→ balance-sheet risk
→ cash conversion
→ ownership/control
→ disclosure sources
→ key uncertainties
```

Template này không ép một valuation model; nó ép người viết làm rõ evidence và mechanism trước khi kết luận.

### P1 — Workflow DART/KIND và provenance

Cần một route tái sử dụng:

```text
filing period
→ consolidated vs separate
→ segment definition
→ accounting policy
→ footnotes / related parties
→ cash-flow reconciliation
→ restatement/comparability check
```

Mục tiêu là đọc disclosure như bằng chứng, không chỉ biết cách mở portal.

### P1 — So sánh chu kỳ giữa các ngành

Semiconductor, auto/battery, shipbuilding, construction/PF, platform/service và financial institution phản ứng khác nhau với cùng một shock. Một route chung nên dùng lens:

```text
order/backlog
→ capacity
→ inventory/working capital
→ pricing
→ margin
→ capex
→ financing
→ recovery lag
```

So sánh theo cùng mechanism giúp người đọc thấy “cyclical” không phải một nhãn giống nhau cho mọi ngành.

### P1 — Economic control và related-party evidence

Cần nối legal entity với economic control:

```text
shareholding
→ voting/control rights
→ affiliates/related parties
→ intra-group transaction/guarantee
→ consolidation scope
→ minority-interest consequence
```

Đây là vùng đặc biệt quan trọng khi đọc chaebol, vì ownership percentage đơn lẻ chưa mô tả đầy đủ quyền kiểm soát kinh tế.

### P2 — Macro surprise tới company exposure

Nên nối observed macro data → interpretation → transmission channel → firm exposure → already-priced expectation → scenario/update condition. Portfolio action tiếp tục bàn giao sang Investing.

### P2 — Failure/restructuring case

Các case nên theo operating stress → liquidity stress → refinancing/covenant problem → funding/rating response → asset sale/equity injection/workout → stakeholder outcome. Khi đi hết chuỗi, người đọc mới thấy accounting, cash flow và capital structure tương tác thế nào trong khủng hoảng.

## 7. Quy trình review

Khi sửa nội dung lớn:

```text
owner
→ mechanism
→ Korea-specific institution/context
→ accounting/statistical definition
→ source + as-of date
→ transmission path
→ alternative explanation
→ company/sector evidence
→ boundary với Economics/Investing/Law/Culture
→ internal links
```

Với company, market hoặc policy claim hiện hành, provenance và date là bắt buộc hơn prose kể chuyện.

## 8. Kết luận và bàn giao

Độ rộng, tích hợp lịch sử–thể chế, accounting/funding và sector coverage hiện **mạnh**. Gap có giá trị cao nhất là evidence sheet thống nhất, DART/KIND workflow, cross-sector cycle comparison và freshness governance.

Sau audit này, nếu câu hỏi chuyển từ company/sector evidence sang portfolio action, bàn giao sang [`../investing/`](../investing/README.md). Nếu câu hỏi cần theory tổng quát hơn, quay sang [`../economics/`](../economics/README.md).