# 07 — Bài tập tích hợp (Integrated Case Studies)

Đây là phần tổng hợp cuối (capstone) của toàn bộ thư viện đầu tư. Các phần trước dạy từng lớp riêng như hệ thống tài chính, nhóm tài sản, phân tích doanh nghiệp, kinh tế học, giao dịch và thị trường Hàn Quốc/Việt Nam. Ở đây, mục tiêu là nối tất cả thành một quy trình nghiên cứu hoàn chỉnh.

Mỗi tình huống không được viết như “đáp án lịch sử” hoặc công thức dự báo. Nó được xây như một bài tập tư duy có thể tái sử dụng cho tình huống mới:

```text
Cú sốc / Câu hỏi
→ Thị trường đã phản ánh điều gì vào giá?
→ Kênh truyền dẫn vĩ mô
→ Lãi suất / Tỷ giá / Tín dụng
→ Kinh tế ngành
→ Lợi nhuận doanh nghiệp
→ Định giá
→ Tác động tới danh mục
→ Phòng vệ / Thực thi
→ Phân rã kết quả
→ Cập nhật luận điểm
```

## Thứ tự đọc

[01_INFLATION_SHOCK_FROM_CPI_TO_PORTFOLIO.md](./01_INFLATION_SHOCK_FROM_CPI_TO_PORTFOLIO.md) bắt đầu từ một mức CPI gây bất ngờ so với kỳ vọng (CPI surprise), rồi theo dõi toàn bộ chuỗi từ cấu phần lạm phát → hàm phản ứng của ngân hàng trung ương → đường cong lợi suất/lợi suất thực → USD/KRW/VND → duration của cổ phiếu → biên lợi nhuận doanh nghiệp → định giá → phòng vệ danh mục → đánh giá sau sự kiện.

[02_CREDIT_LIQUIDITY_CRISIS_TRANSMISSION.md](./02_CREDIT_LIQUIDITY_CRISIS_TRANSMISSION.md) phân tích căng thẳng thanh khoản và tín dụng từ tài sản thế chấp/ký quỹ → nguồn vốn → bảng cân đối ngân hàng → chênh lệch tín dụng → giảm đòn bẩy cưỡng bức → lợi nhuận → phản ứng chính sách → thanh khoản danh mục. Tình huống này giúp phân biệt thiếu thanh khoản, mất khả năng thanh toán và chu kỳ co hẹp tín dụng do suy thoái.

[03_SEMICONDUCTOR_CYCLE_KOREA_CASE.md](./03_SEMICONDUCTOR_CYCLE_KOREA_CASE.md) dùng hệ sinh thái bán dẫn/HBM Hàn Quốc để nối chi tiêu AI toàn cầu, cung–cầu bộ nhớ, tồn kho, giá bán bình quân (ASP), công suất sử dụng, capex, nhà cung cấp thiết bị/vật liệu, KRW, điều chỉnh dự báo lợi nhuận, định giá theo chu kỳ và quy mô vị thế.

[04_VIETNAM_PROPERTY_BANK_CREDIT_CASE.md](./04_VIETNAM_PROPERTY_BANK_CREDIT_CASE.md) dùng chuỗi bất động sản–ngân hàng–chứng khoán–thanh khoản tại Việt Nam để học cách lập bản đồ tiến độ pháp lý, bán trước, trái phiếu doanh nghiệp, mức phơi nhiễm của ngân hàng, NPL/dự phòng, thanh khoản margin, dư địa chính sách của SBV, định giá và khả năng sống sót của bảng cân đối.

Trước khi làm capstone cuối, hoàn thành ít nhất một vòng trong [Advanced Practice Workbook](../ADVANCED_PRACTICE_WORKBOOK.md). Workbook buộc người học tạo IPS, ma trận tài sản, mô hình doanh nghiệp, bảng nowcast, báo cáo backtest và dashboard Korea/Vietnam thay vì chỉ đọc case study.

[05_FULL_INVESTMENT_PROCESS_FROM_THESIS_TO_REVIEW.md](./05_FULL_INVESTMENT_PROCESS_FROM_THESIS_TO_REVIEW.md) là capstone cuối cùng. File này nối câu hỏi nghiên cứu → nguồn dữ liệu → giả định → macro/sector/company model → định giá → phân phối lợi suất kỳ vọng → quy mô vị thế → thực thi → theo dõi → phân rã kết quả → post-mortem. Đây là bài kiểm tra xem người đọc đã có thể vận hành toàn bộ thư viện như một hệ thống nghiên cứu hay chưa.

## Cách sử dụng tình huống

Không đọc như một câu chuyện để ghi nhớ hướng giá. Hãy dừng trước từng bước và tự trả lời ba câu hỏi:

1. Nếu chỉ biết thông tin tới đây, những kênh truyền dẫn nào có thể xảy ra?
2. Dữ liệu nào có thể xác nhận hoặc bác bỏ giả thuyết?
3. Thị trường đã phản ánh bao nhiêu kỳ vọng vào giá trước sự kiện?

Sau đó mới đọc phần tiếp theo.

## Ghi chú nên tạo sau mỗi tình huống

```text
Giả thuyết ban đầu
Dữ kiện chính
Điều thị trường đã phản ánh vào giá
Cây động lực
Kịch bản cơ sở / tích cực / tiêu cực
Mức phơi nhiễm danh mục
Kế hoạch thực thi
Điều kiện vô hiệu hóa
Phân rã kết quả sau sự kiện
Bài học rút ra
```

Với capstone cuối, mở rộng thành một hồ sơ đầu tư hoàn chỉnh gồm cả nguồn dữ liệu, mô hình, định giá, sizing, execution, monitoring và post-mortem template.

## Liên kết với các lĩnh vực trước

Các bài tập giả định bạn đã đọc ít nhất:

- [01 — Nền tảng đầu tư](../01_foundations/README.md)
- [02 — Các nhóm tài sản](../02_asset_classes/README.md)
- [03 — Phân tích doanh nghiệp](../03_company_analysis/README.md)
- [04 — Kinh tế học và vĩ mô](../04_economics/README.md)

Nếu tình huống có giao dịch hoặc phòng vệ, xem thêm [05 — Giao dịch và phái sinh](../05_trading_derivatives/README.md). Nếu liên quan Hàn Quốc/Việt Nam, xem [06 — Thị trường Hàn Quốc và Việt Nam](../06_markets_korea_vietnam/README.md).

Nếu muốn học theo lớp nâng cao thay vì theo domain, sử dụng [Advanced Depth Path](../ADVANCED_DEPTH_PATH.md).

## Tiêu chuẩn hoàn thành

Không coi một case là “đã học” nếu chỉ đọc hết file. Tối thiểu phải tự tạo:

```text
Một giả thuyết có thể bị bác bỏ
Một bảng kịch bản
Một điều kiện vô hiệu hóa
Một phép kiểm thử bảng cân đối / thanh khoản
Một đánh giá định giá hoặc lợi suất kỳ vọng
Một quy tắc sizing
Một kế hoạch theo dõi
Một post-mortem template
```

## Mục tiêu cuối cùng

Sau phần này, khi nhìn một tin mới, người đọc không nên hỏi ngay “mua hay bán gì?”, mà đi theo chuỗi:

```text
Điều gì vừa thay đổi?
→ So với kỳ vọng nào?
→ Truyền qua bảng cân đối và dòng tiền nào?
→ Ai hưởng lợi, ai chịu thiệt và vào thời điểm nào?
→ Phần nào đã phản ánh vào giá?
→ Nên nhận bao nhiêu rủi ro?
→ Quyết định sẽ được đánh giá lại như thế nào?
```

Đó là bước chuyển từ “biết kiến thức đầu tư” sang có một hệ thống vận hành nghiên cứu (research operating system).