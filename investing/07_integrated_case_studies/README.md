# 07 — Bài tập tích hợp (Integrated case Studies)

> **Mạch đọc:** Đọc **07 — Bài tập tích hợp (Integrated case Studies)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Thứ tự đọc** sang **Coverage map của trường hợp (case / 사례) study**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Đây là phần tổng hợp cuối (capstone) của toàn bộ thư viện đầu tư. Các phần trước dạy từng lớp riêng như hệ thống tài chính, nhóm tài sản, phân tích doanh nghiệp, kinh tế học, giao dịch và thị trường Hàn Quốc/Việt Nam. Ở đây, mục tiêu là nối tất cả thành một quy trình nghiên cứu hoàn chỉnh.

Mỗi tình huống không được viết như “đáp án lịch sử” hoặc công thức dự báo. Nó được xây như một bài tập tư duy có thể tái sử dụng cho tình huống mới:

```text
Cú sốc / Câu hỏi
→ Thị trường đã phản ánh điều gì vào giá?
→ Macro
→ Rates / Yield Curve
→ Liquidity / Credit / Funding
→ FX
→ Industry economics
→ Company driver / Cash flow
→ Valuation
→ Portfolio exposure
→ Hedge / Execution
→ Attribution / Review
```

Một trường hợp (case / 사례) dừng ở “macro tốt/xấu cho ngành” chưa được xem là hoàn chỉnh. trường hợp (case / 사례) phải chỉ ra **dữ liệu (data / 데이터) → interpretation → rủi ro (risk / 위험) → dạng thất bại (failure mode / 실패 모드)** ở từng tầng.

## Thứ tự đọc

[01_INFLATION_SHOCK_FROM_CPI_TO_PORTFOLIO.md](./01_INFLATION_SHOCK_FROM_CPI_TO_PORTFOLIO.md) bắt đầu từ một mức CPI gây bất ngờ so với kỳ vọng (CPI surprise), rồi theo dõi toàn bộ chuỗi từ cấu phần lạm phát → hàm phản ứng của ngân hàng trung ương → đường cong lợi suất/lợi suất thực → USD/KRW/VND → duration của cổ phiếu → biên lợi nhuận doanh nghiệp → định giá → phòng vệ danh mục → đánh giá sau sự kiện.

[02_CREDIT_LIQUIDITY_CRISIS_TRANSMISSION.md](./02_CREDIT_LIQUIDITY_CRISIS_TRANSMISSION.md) phân tích căng thẳng thanh khoản và tín dụng từ tài sản thế chấp/ký quỹ → nguồn vốn → bảng cân đối ngân hàng → chênh lệch tín dụng → giảm đòn bẩy cưỡng bức → lợi nhuận → phản ứng chính sách → thanh khoản danh mục. Tình huống này giúp phân biệt thiếu thanh khoản, mất khả năng thanh toán và chu kỳ co hẹp tín dụng do suy thoái.

[03_SEMICONDUCTOR_CYCLE_KOREA_CASE.md](./03_SEMICONDUCTOR_CYCLE_KOREA_CASE.md) dùng hệ sinh thái bán dẫn/HBM Hàn Quốc để nối chi tiêu AI toàn cầu, cung–cầu bộ nhớ, tồn kho, giá bán bình quân (ASP), công suất sử dụng, capex, nhà cung cấp thiết bị/vật liệu, KRW, điều chỉnh dự báo lợi nhuận, định giá theo chu kỳ và quy mô vị thế.

[04_VIETNAM_PROPERTY_BANK_CREDIT_CASE.md](./04_VIETNAM_PROPERTY_BANK_CREDIT_CASE.md) dùng chuỗi bất động sản–ngân hàng–chứng khoán–thanh khoản tại Việt Nam để học cách lập bản đồ tiến độ pháp lý, bán trước, trái phiếu doanh nghiệp, mức phơi nhiễm của ngân hàng, NPL/dự phòng, thanh khoản margin, dư địa chính sách của SBV, định giá và khả năng sống sót của bảng cân đối.

[06_MACRO_RATES_LIQUIDITY_COMPANY_VALUATION_PORTFOLIO_CASE.md](./06_MACRO_RATES_LIQUIDITY_COMPANY_VALUATION_PORTFOLIO_CASE.md) là worked trường hợp (case / 사례) có số liệu giả định đi trọn `macro → rates → liquidity/credit → semiconductor equipment industry → company revenue/EBIT/FCF → WACC/valuation → portfolio stress`. trường hợp (case / 사례) buộc người học tính duration, refinancing chi phí (cost / 비용), operating leverage, terminal-value sensitivity và stress mất mát (loss / 손실) của danh mục, đồng thời kiểm tra dạng thất bại (failure mode / 실패 모드) của hedge.

[07_USD_FUNDING_FX_KOREA_VIETNAM_CROSS_BORDER_CASE.md](./07_USD_FUNDING_FX_KOREA_VIETNAM_CROSS_BORDER_CASE.md) dùng cú sốc USD funding để so Hàn Quốc và Việt Nam trên cùng một khung: Fed/US rates → KRW/VND → BOK/SBV → domestic liquidity/credit → ngành → hai doanh nghiệp giả định → valuation → base-currency return → FX hedge → cross-border portfolio attribution.

Trước khi làm capstone cuối, hoàn thành ít nhất một vòng trong [Advanced Practice Workbook](../ADVANCED_PRACTICE_WORKBOOK.md). Workbook buộc người học tạo IPS, ma trận tài sản, mô hình doanh nghiệp, bảng nowcast, báo cáo backtest và dashboard Korea/Vietnam thay vì chỉ đọc trường hợp (case / 사례) study.

[05_FULL_INVESTMENT_PROCESS_FROM_THESIS_TO_REVIEW.md](./05_FULL_INVESTMENT_PROCESS_FROM_THESIS_TO_REVIEW.md) là capstone cuối cùng. tệp (file / 파일) này nối câu hỏi nghiên cứu → nguồn dữ liệu → giả định → macro/sector/company mô hình (model / 모델) → định giá → phân phối lợi suất kỳ vọng → quy mô vị thế → thực thi → theo dõi → phân rã kết quả → post-mortem. Đây là bài kiểm tra xem người đọc đã có thể vận hành toàn bộ thư viện như một hệ thống nghiên cứu hay chưa.


Bảng coverage dưới đây cho biết mỗi case đã đi qua những tầng nào của hệ thống nghiên cứu. Hãy đọc nó như bản đồ điều hướng: dấu ✓ chỉ có giá trị khi bên trong case có cơ chế, dữ liệu, cách diễn giải và failure mode tương ứng.

| Case | Macro | Rates | Liquidity/Credit | Industry | Company | Valuation | Portfolio | Korea/Vietnam |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 CPI Shock | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 02 Credit/Liquidity Crisis | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | một phần |
| 03 Korea Semiconductor | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Korea |
| 04 Vietnam thuộc tính (property / 속성)/Bank | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Vietnam |
| 06 Macro→Portfolio Worked trường hợp (case / 사례) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Korea example |
| 07 USD Funding/FX Cross-Border | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Korea + Vietnam |
| 05 Full tiến trình (process / 프로세스) Capstone | tùy trường hợp (case / 사례) | tùy trường hợp (case / 사례) | tùy trường hợp (case / 사례) | ✓ | ✓ | ✓ | ✓ | tùy trường hợp (case / 사례) |

Bảng này dùng để kiểm tra (audit / 감사) coverage, không phải checklist hình thức. Mỗi dấu ✓ phải có **cơ chế, dữ liệu, interpretation và dạng thất bại (failure mode / 실패 모드)** tương ứng trong trường hợp (case / 사례).


> **Chuyển mạch:** Từ **Coverage map của trường hợp (case / 사례) study**, ta sang **Cách sử dụng tình huống** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cách sử dụng tình huống

Không đọc như một câu chuyện để ghi nhớ hướng giá. Hãy dừng trước từng bước và tự trả lời:

1. Nếu chỉ biết thông tin tới đây, những kênh truyền dẫn nào có thể xảy ra?
2. Dữ liệu nào có thể xác nhận hoặc bác bỏ giả thuyết?
3. Thị trường đã phản ánh bao nhiêu kỳ vọng vào giá trước sự kiện?
4. dạng thất bại (failure mode / 실패 모드) nào khiến quan hệ lịch sử không còn đúng?
5. Nếu thesis đúng nhưng giá đi ngược, biến nào khác có thể đang chi phối?

Sau đó mới đọc phần tiếp theo.


> **Chuyển mạch:** Từ **Cách sử dụng tình huống**, ta sang **Ghi chú nên tạo sau mỗi tình huống** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Ghi chú nên tạo sau mỗi tình huống

Sau khi đọc hoặc tự chạy một case, hãy chuyển hiểu biết thành một ghi chú ngắn có thể xem lại. Việc ghi theo cùng một cấu trúc giúp so sánh các cú sốc khác nhau và phát hiện phần nào trong quy trình của mình còn bỏ trống.

```text
Giả thuyết ban đầu
Dữ kiện chính
Ước tính
Giả định
Điều thị trường đã phản ánh vào giá
Cây truyền dẫn macro → rates → liquidity → industry → company
Kịch bản cơ sở / tích cực / tiêu cực
Failure mode / counterfactual
Mức phơi nhiễm danh mục
Kế hoạch thực thi / hedge
Điều kiện vô hiệu hóa theo từng tầng
Phân rã kết quả sau sự kiện
Bài học rút ra
```

Với capstone cuối, mở rộng thành một hồ sơ đầu tư hoàn chỉnh gồm cả nguồn dữ liệu, mô hình, định giá, sizing, thực thi (execution / 실행), monitoring và post-mortem template.


> **Chuyển mạch:** Từ **Ghi chú nên tạo sau mỗi tình huống**, ta sang **Liên kết với các lĩnh vực trước** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Liên kết với các lĩnh vực trước

Các bài tập giả định bạn đã đọc ít nhất:

- [01 — Nền tảng đầu tư](../01_foundations/README.md)
- [02 — Các nhóm tài sản](../02_asset_classes/README.md)
- [03 — Phân tích doanh nghiệp](../03_company_analysis/README.md)
- [04 — Kinh tế học và vĩ mô](../04_economics/README.md)

Nếu tình huống có giao dịch hoặc phòng vệ, xem thêm [05 — Giao dịch và phái sinh](../05_trading_derivatives/README.md). Nếu liên quan Hàn Quốc/Việt Nam, xem [06 — Thị trường Hàn Quốc và Việt Nam](../06_markets_korea_vietnam/README.md).

Nếu muốn học theo lớp nâng cao thay vì theo lĩnh vực (domain / 도메인), sử dụng [Advanced Depth Path](../ADVANCED_DEPTH_PATH.md).


> **Chuyển mạch:** Từ **Liên kết với các lĩnh vực trước**, ta sang **Tiêu chuẩn hoàn thành** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tiêu chuẩn hoàn thành

Không coi một trường hợp (case / 사례) là “đã học” nếu chỉ đọc hết tệp (file / 파일). Tối thiểu phải tự tạo:

```text
Một giả thuyết có thể bị bác bỏ
Một bảng fact / estimate / assumption
Một bảng kịch bản
Một transmission map
Một failure-mode map
Một kiểm thử bảng cân đối / thanh khoản
Một đánh giá định giá hoặc lợi suất kỳ vọng
Một portfolio stress test
Một quy tắc sizing / hedge
Một kế hoạch theo dõi
Một attribution / post-mortem template
```

Với worked trường hợp (case / 사례) 06 và 07, phải tự thay ít nhất ba giả định và tính lại kết quả. Nếu chỉ đọc số có sẵn, bài chưa đạt.


> **Chuyển mạch:** Từ **Tiêu chuẩn hoàn thành**, ta sang **Mục tiêu cuối cùng** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mục tiêu cuối cùng

Sau phần này, khi nhìn một tin mới, người đọc không nên hỏi ngay “mua hay bán gì?”, mà đi theo chuỗi:

```text
Điều gì vừa thay đổi?
→ So với kỳ vọng nào?
→ Rates / liquidity / FX thay đổi thế nào?
→ Truyền qua ngành và bảng cân đối nào?
→ Earnings / FCF thay đổi bao nhiêu?
→ Valuation thay đổi do cash flow hay discount rate?
→ Portfolio đang trùng factor nào?
→ Failure mode của thesis / hedge là gì?
→ Quyết định sẽ được đánh giá lại như thế nào?
```

Đó là bước chuyển từ “biết kiến thức đầu tư” sang có một hệ thống vận hành nghiên cứu (research operating system).
