# Sách 2 — Nhập môn đầu tư chứng khoán (learning edition)

Route này chuyển phần knowledge-bearing của `증권투자기초/raw/sach2.md` thành một đường học tiếng Việt. Source OCR hiện có tên và đoạn văn bị nhiễu ở nhiều trang; vì vậy các thuật ngữ, công thức và quan hệ chỉ được khẳng định khi còn đọc được trong source. Những chỗ không thể đọc chắc được giữ trong [bản đồ coverage](./SOURCE_COVERAGE_BOOK2.md) dưới trạng thái `SOURCE_AMBIGUITY`, không được lấp bằng kiến thức ngoài sách.

## Câu hỏi trung tâm

Một người mới cần nối được bốn lớp: nền kinh tế tạo điều kiện cho thị trường, doanh nghiệp tạo dòng tiền, giá phản ánh kỳ vọng, và trái phiếu chuyển lãi suất–tín dụng–thời hạn thành lợi suất và rủi ro. Route này trả lời câu hỏi đó theo thứ tự học, không theo số trang.

## Mạch đọc

```text
01 Nền tảng và phân tích kinh tế–tài chính
→ 02 Định giá cổ phiếu và quyết định theo dòng tiền
→ 03 Phân tích kỹ thuật: dữ liệu giá, khối lượng, mẫu hình
→ 04 Chiến lược đầu tư và chỉ số thị trường
→ 05 Công cụ trái phiếu và sản phẩm lai
→ 06 Lợi suất, đường cong, duration, tín dụng và chỉ số trái phiếu
```

Các file 01–04 là lớp cầu nối cho Sách 2. Khi cần độ sâu về báo cáo tài chính, DCF, danh mục, vi cấu trúc hoặc Forex, đi theo owner canonical trong [`investing/README.md`](../../investing/README.md), đặc biệt [phân tích doanh nghiệp](../../investing/03_company_analysis/README.md), [nhóm tài sản](../../investing/02_asset_classes/README.md), [kinh tế học](../../investing/04_economics/README.md) và [giao dịch](../../investing/05_trading_derivatives/README.md).

## Các bài học

1. [Nền tảng đầu tư, chứng khoán và chỉ báo kinh tế](./01_SECURITIES_MACRO_AND_FINANCIAL_ANALYSIS.md) — khái niệm đầu tư, chứng khoán, chu kỳ kinh doanh, GDP, CPI, CSI/BSI, tỷ giá, kế toán và IFRS.
2. [Định giá cổ phiếu: lợi suất, dòng tiền và multiples](./02_EQUITY_VALUATION_AND_MULTIPLES.md) — CAPM, NPV/PVGO, FCFE/FCFF, EVA, PER, PBR–ROE, PSR–margin và EV/EBITDA.
3. [Phân tích kỹ thuật và giới hạn của tín hiệu](./03_TECHNICAL_ANALYSIS.md) — biểu đồ, xu hướng, moving average, mẫu hình, candlestick, MACD/RSI/stochastic, Bollinger, OBV/VR, Dow và Elliott.
4. [Chiến lược đầu tư và chỉ số thị trường](./04_INVESTMENT_STRATEGIES_AND_INDICES.md) — buy-and-hold, bình quân giá, cổ tức, stock split, hiệu ứng quy mô, danh mục, benchmark và stock-price index.
5. [Trái phiếu và sản phẩm thu nhập cố định](./05_BONDS_AND_FIXED_INCOME_INSTRUMENTS.md) — cấu trúc trái phiếu, coupon, maturity, định giá, convertible, warrant, exchangeable, ABS, floating-rate, preferred và structured notes.
6. [Lợi suất, tín dụng, duration và thị trường trái phiếu](./06_BOND_YIELDS_RISK_DURATION_AND_INDICES.md) — discount rate, YTM/IRR, term structure theories, credit rating, duration, convexity, repo, bond index và total-return index.

## Phạm vi nguồn và ngày kiểm tra

Source được kiểm tra trong checkout ngày 2026-10-04 tại `증권투자기초/raw/sach2.md` (7.960 dòng, OCR). Đường dẫn `증권투자기초/raw_md/sach2.md` được nêu trong yêu cầu chưa tồn tại; không tạo bản sao giả để thay thế. `prompt/BOOK_MD_TO_LEARNING_DOCS_PROMPT.md` cũng không có trong checkout; contract đang dùng là yêu cầu dán trong task và `prompt/COMMON_PROMPT.md`.

Đây là textbook-state, không phải tư vấn hay bản cập nhật luật/thuế/thị trường. Các claim hiện tại cần được kiểm tra theo nguồn chính thức trước khi dùng để ra quyết định thật.

