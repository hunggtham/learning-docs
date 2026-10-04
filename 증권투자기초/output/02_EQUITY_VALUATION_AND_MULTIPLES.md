# 2. Định giá cổ phiếu: lợi suất, dòng tiền và multiples

Bài 1 đã tách quyền sở hữu, dòng tiền và tỷ số hiệu quả. Bài này dùng chúng để giải quyết câu hỏi trung tâm: với rủi ro và thời điểm đã biết, một dòng tiền tương lai đáng giá bao nhiêu hôm nay? Các công thức trong source không phải máy tạo giá mục tiêu; chúng là cách làm lộ giả định về tăng trưởng, rủi ro, tái đầu tư và cấu trúc vốn.

## 1. Lãi kép, suất sinh lợi yêu cầu và CAPM

Một khoản tiền tăng theo lãi kép:

```text
FV = PV × (1 + r)^n
PV = FV / (1 + r)^n
```

Trong đó `PV` là giá trị hiện tại, `FV` là giá trị tương lai, `r` là suất sinh lợi mỗi kỳ và `n` là số kỳ. Ví dụ 100 tăng 10% một năm thành 110 sau một năm và 121 sau hai năm; cộng 10 + 10 sẽ bỏ qua việc năm thứ hai sinh lời trên 110.

CAPM (Capital Asset Pricing Model) trong source viết logic:

```text
E(Rᵢ) = Rf + βᵢ × [E(Rm) − Rf]
```

`Rf` là lãi suất phi rủi ro, `βᵢ` là độ nhạy của tài sản với thị trường, còn `E(Rm) − Rf` là phần bù rủi ro thị trường. CAPM nối rủi ro hệ thống với suất sinh lợi yêu cầu; nó không định lượng rủi ro riêng lẻ, thanh khoản, tail risk hay sai số mô hình. Vì vậy CAPM là một giả định discount rate, không phải mô tả đầy đủ thực tế.

## 2. NPV và PVGO

NPV (Net Present Value) là giá trị hiện tại của dòng tiền vào trừ vốn bỏ ra. Nếu NPV dương dưới cùng bộ giả định, dự án tạo giá trị vượt suất sinh lợi yêu cầu; nếu discount rate, dòng tiền hoặc thời hạn đổi, kết luận cũng đổi. PVGO (Present Value of Growth Opportunities) tách giá trị hiện tại của tài sản đang vận hành khỏi giá trị của cơ hội tăng trưởng. Tách này giúp hỏi đúng: giá đang trả cho lợi nhuận hiện tại hay cho tái đầu tư tương lai?

Đừng nhầm NPV dương với lợi nhuận chắc chắn. NPV là kết quả của mô hình và giả định. Hãy ghi rõ tăng trưởng, biên lợi nhuận, vốn tái đầu tư và discount rate; sau đó kiểm thử kịch bản. Đây là cầu nối sang FCFE/FCFF, nơi cùng một doanh nghiệp được nhìn từ hai nhóm người cung cấp vốn.

## 3. FCFE, FCFF và WACC

FCFE (Free Cash Flow to Equity) là tiền còn lại cho cổ đông sau chi đầu tư, thay đổi vốn lưu động và tài trợ nợ cần thiết. FCFF (Free Cash Flow to Firm) là tiền cho toàn bộ nhà cung cấp vốn trước phân phối giữa nợ và vốn chủ. Source ghi quan hệ khái quát:

```text
FCFF = FCFE + chi phí lãi sau thuế + dòng tiền trả nợ ròng
```

FCFE thường chiết khấu bằng cost of equity; FCFF chiết khấu bằng WACC (Weighted Average Cost of Capital). WACC trộn cost of equity và cost of debt theo trọng số thị trường, đồng thời phản ánh lá chắn thuế của nợ trong mô hình textbook. Dùng FCFF với cost of equity hoặc FCFE với WACC là trộn đối tượng dòng tiền và discount rate.

## 4. EVA, NOPAT, invested capital và ROIC

EVA (Economic Value Added) đo lợi nhuận hoạt động sau thuế vượt chi phí sử dụng vốn:

```text
EVA = NOPAT − (Invested Capital × WACC)
    = Invested Capital × (ROIC − WACC)
```

`NOPAT` là Net Operating Profit After Tax; `Invested Capital` là vốn hoạt động đã đầu tư; `ROIC = NOPAT / Invested Capital`. Khi ROIC lớn hơn WACC, mỗi đồng vốn mới tạo giá trị kinh tế; khi thấp hơn, tăng trưởng có thể phá hủy giá trị dù doanh thu tăng. Đây là cơ chế giải thích vì sao “tăng trưởng” không tự động tốt.

## 5. PER/EPS

PER (Price–Earnings Ratio) là:

```text
PER = giá thị trường mỗi cổ phiếu / EPS
```

EPS (Earnings Per Share) là lợi nhuận quy cho một cổ phiếu theo mẫu số phù hợp. Có thể diễn giải giá = EPS × PER: thị trường vừa định giá mức lợi nhuận, vừa định giá mức multiple cho tăng trưởng và rủi ro. EPS âm, lợi nhuận chu kỳ hoặc một khoản bất thường làm PER kém ổn định; hãy dùng lợi nhuận chuẩn hóa và so sánh với doanh nghiệp cùng mô hình.

## 6. PBR và ROE

PBR (Price-to-Book Ratio) so giá thị trường với BPS (Book Value Per Share):

```text
PBR = giá cổ phiếu / BPS
EPS = BPS × ROE
```

Vì vậy, cùng một PBR có thể hợp lý hoặc đắt tùy ROE và chi phí vốn. PBR thấp không tự động là rẻ: tài sản ghi sổ có thể suy giảm, ROE có thể thấp hơn cost of equity, hoặc doanh nghiệp đang phá hủy giá trị. PBR–ROE là đối chiếu giữa giá trị ghi sổ và khả năng sinh lời, không phải công thức thay thế phân tích tài sản.

## 7. PSR và margin

PSR (Price-to-Sales Ratio) dùng doanh thu trên mỗi cổ phiếu (SPS):

```text
PSR = giá cổ phiếu / SPS
EPS = SPS × biên lợi nhuận
```

Doanh nghiệp biên cao có thể xứng đáng PSR cao hơn doanh nghiệp doanh thu lớn nhưng biên thấp. PSR hữu ích khi lợi nhuận tạm âm, nhưng không thể bỏ qua chi phí để biến doanh thu thành tiền. Source dùng quan hệ PSR–margin như một cảnh báo: nếu biên không cải thiện, doanh thu tăng không đủ tạo EPS.

## 8. EV/EBITDA

EV (Enterprise Value) nhìn giá trị hoạt động cho cả chủ nợ và cổ đông; dạng khái quát `EV = equity value + nợ chịu lãi − tiền và tương đương tiền`. EBITDA (Earnings Before Interest, Tax, Depreciation and Amortization) gần với lợi nhuận hoạt động trước khấu hao, nhưng không phải dòng tiền tự do. `EV/EBITDA` hữu ích để so sánh cấu trúc vốn khác nhau, song dễ sai với doanh nghiệp cần capex lớn, thuê tài sản nhiều hoặc có vốn lưu động biến động.

## 9. Quy trình dùng multiple

Đọc bảng multiple theo bốn bước: (1) xác định numerator và denominator; (2) kiểm tra chất lượng và chu kỳ của denominator; (3) so với nhóm tương đồng; (4) nối multiple với tăng trưởng, biên, ROIC và rủi ro. Không dùng nhiều tỷ số để tạo ảo giác đồng thuận: PER, PBR, PSR và EV/EBITDA có thể cùng sai nếu dự báo dòng tiền sai.

## Chốt và bàn giao

Invariant của bài là “giá trị = dòng tiền hoặc lợi nhuận tương lai được quy đổi theo rủi ro và thời gian”. Ranh giới là mọi công thức phụ thuộc giả định và đối tượng dòng tiền. Bài 3 chuyển từ giá trị nội tại sang dữ liệu giá/khối lượng: tín hiệu kỹ thuật có thể giúp mô tả hành vi thị trường, nhưng không chứng minh doanh nghiệp đáng giá hơn. Xem [Phân tích kỹ thuật](./03_TECHNICAL_ANALYSIS.md).

