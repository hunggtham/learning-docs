# 8. Integrated case lab: từ forecast đến quyết định có kiểm soát

> Đây là case học tập tổng hợp các cơ chế đã học trong Sách 3. Số liệu giả định để kiểm tra cách suy luận, không phải khuyến nghị mua bán.

## 1. Bối cảnh và dữ liệu

Một nhà đầu tư có 1 tỷ đồng. Trong đó 700 triệu đang nằm ở cổ phiếu A, 300 triệu là tiền mặt. Cổ phiếu A có expected return 12%, độ lệch chuẩn 20% và beta 1,2. Market expected return là 10%, risk-free rate 4%, nên market risk premium là 6%. Nhà đầu tư dự kiến giữ vị thế một năm nhưng lo thị trường giảm mạnh trong ba tháng tới.

Doanh nghiệp A có FCFF dự báo (đơn vị: tỷ đồng) là 80, 88 và 96 cho ba năm tới. WACC cơ sở là 9%, tăng trưởng dài hạn 3%, nợ ròng 400 tỷ, 100 triệu cổ phiếu lưu hành. Giá thị trường hiện tại là 9.500 đồng/cổ phiếu. Nhà đầu tư cũng được chào một ELS 100 triệu đồng, coupon niêm yết 8%/năm, autocall sáu tháng và barrier 55% trên worst-of của hai chỉ số.

Điểm của case không phải chọn một con số “đúng” ngay lập tức. Người học phải tách bốn câu hỏi: cổ phiếu có đáng giá không, danh mục đang chịu rủi ro nào, hedge bù được phần nào, và ELS đang bán exposure gì để tạo coupon.

## 2. Bước 1 — CAPM chỉ cho required return

CAPM cho cổ phiếu A:

\[
k_e=r_f+\beta(E(r_m)-r_f)=4\%+1,2\times6\%=11,2\%.
\]

Expected return 12% cao hơn required return 11,2% khoảng 0,8 điểm phần trăm. Khoảng chênh này không tự động là alpha có thể kiếm được: forecast return có thể sai, beta có thể thay đổi và giao dịch có chi phí. CAPM đang cung cấp hurdle rate cho quyết định, không phải dự báo chắc chắn giá một năm sau.

Nếu cổ phiếu tăng 12% chỉ vì thị trường tăng 10%, phần lớn kết quả có thể là market exposure chứ không phải stock-picking skill. Muốn gọi là alpha, phải so với return do beta giải thích và kiểm tra cùng benchmark, cùng thời kỳ, sau chi phí.

## 3. Bước 2 — DCF và terminal-value risk

Với FCFF cơ sở:

\[
TV_3=\frac{96\times1,03}{0,09-0,03}=1.648.
\]

Giá trị doanh nghiệp xấp xỉ:

\[
EV=\frac{80}{1,09}+\frac{88}{1,09^2}+\frac{96}{1,09^3}+\frac{1.648}{1,09^3}\approx1.494.
\]

Trừ nợ ròng 400 tỷ, equity value khoảng 1.094 tỷ. Chia cho 100 triệu cổ phiếu, intrinsic value cơ sở khoảng 10.940 đồng/cổ phiếu, cao hơn giá 9.500 đồng khoảng 15%.

Kết quả này chỉ có ý nghĩa nếu ba lớp giả định nhất quán:

1. FCFF là dòng tiền cho cả debt holder và equity holder, nên dùng WACC chứ không dùng cost of equity.
2. Nợ ròng được trừ sau khi tính enterprise value, không trừ hai lần trong FCFF.
3. Tăng trưởng 3% phải phù hợp với reinvestment và ROIC dài hạn; không được kéo dài một năm tăng trưởng cao vô thời hạn.

Stress case cho thấy độ nhạy: với WACC 10% và \(g=2\%\), EV chỉ khoảng 1.137 tỷ, equity value khoảng 737 tỷ, tương đương 7.370 đồng/cổ phiếu. Với WACC 8% và \(g=3\%\), EV xấp xỉ 1.796 tỷ, tương đương khoảng 13.960 đồng/cổ phiếu sau khi trừ nợ. Khoảng 7.370–13.960 đồng cho thấy “upside 15%” là kết quả của giả định, không phải một sự thật quan sát được.

## 4. Bước 3 — Portfolio và hedge futures

Exposure cổ phiếu là 700 triệu. Beta-adjusted market exposure là:

\[
700\text{ triệu}\times1,2=840\text{ triệu}.
\]

Nếu mỗi hợp đồng index futures có notional 100 triệu, hedge ratio lý thuyết là 8,4 hợp đồng bán. Không thể giao dịch 0,4 hợp đồng trong giả định này, nên nhà đầu tư phải chọn 8 hoặc 9 hợp đồng và chấp nhận residual beta; quyết định còn phụ thuộc margin, basis và thời điểm đáo hạn.

Nếu index giảm 10%, beta đơn giản dự báo cổ phiếu giảm khoảng 12%, tức lỗ khoảng 84 triệu trước idiosyncratic shock. Short 8 futures có thể lãi khoảng 80 triệu theo notional, còn lại khoảng 4 triệu cộng basis, sai số beta và phí. Short 9 futures có thể hedge quá mức nếu cổ phiếu giảm ít hơn market. Hedge làm giảm phương sai thị trường; nó không bảo hiểm được scandal riêng của doanh nghiệp A.

Đây là điểm nối giữa CAPM và phái sinh: beta giúp ước lượng quy mô hedge, nhưng payoff futures và dòng tiền margin quyết định hedge có chịu được đường đi của giá hay không. Nếu index giảm nhanh, daily settlement có thể yêu cầu nộp tiền trước khi lãi hedge cổ phiếu được hiện thực hóa.

## 5. Bước 4 — Đọc ELS như một gói option

ELS 100 triệu với coupon 8%/năm không tương đương tiền gửi 8%. Nếu autocall xảy ra sau sáu tháng, coupon gộp theo thời gian chỉ khoảng 4 triệu trước thuế, rồi vốn được trả lại để tái đầu tư. Nếu worst-of chạm barrier và đáo hạn ở 45% giá ban đầu, principal theo điều khoản có thể chỉ còn khoảng 45 triệu, tức lỗ 55 triệu; coupon không xóa được loss này.

Ba risk layer phải được viết riêng:

- **Market/path risk:** worst-of, volatility, correlation và barrier path quyết định nhánh payoff.
- **Liquidity/model risk:** giá bán sớm phụ thuộc issuer spread, hedge cost và mô hình correlation/volatility; không nhất thiết bằng giá trị nội tại đơn giản.
- **Issuer risk:** underlying không giảm vẫn không bảo vệ người mua nếu issuer không thực hiện nghĩa vụ.

Coupon cao hơn thường phản ánh việc nhà đầu tư đang bán một phần downside insurance cho issuer. Vì vậy câu hỏi không phải “coupon bao nhiêu”, mà là “tôi đang short option nào, lỗ tối đa ở nhánh nào, và có chịu được nhánh đó không?”.

## 6. Bước 5 — Quyết định và nhật ký giả định

Một quyết định có kiểm soát có thể ghi như sau:

| Câu hỏi | Kết quả cơ sở | Boundary cần ghi |
|---|---|---|
| A có rẻ không? | DCF 10.940 > 9.500 | WACC, \(g\), FCFF, nợ ròng |
| Rủi ro chính là gì? | beta 1,2 và idiosyncratic risk | beta không cố định, correlation đổi |
| Hedge thế nào? | short khoảng 8–9 futures | basis, margin, hedge ratio rời rạc |
| ELS có thay thế cash không? | Không | barrier, worst-of, issuer, liquidity |
| Cần hành động gì? | tách valuation khỏi hedge | không dùng coupon để che loss tail |

Nhật ký nên lưu cả con số và lý do: forecast nào là dữ kiện, forecast nào là giả định; khoản hedge bảo vệ cash flow nào; ngưỡng nào buộc giảm vị thế; khi nào thesis bị bác bỏ. Nếu chỉ ghi “cổ phiếu có upside” hoặc “ELS coupon cao”, đó là slogan chứ chưa phải investment process.

## 7. Reconstruction test

Sau case này, người học phải dựng lại được chuỗi:

\[
\text{uncertainty}\rightarrow\text{statistics}\rightarrow\text{portfolio beta}\rightarrow\text{CAPM hurdle}\rightarrow\text{DCF value}\rightarrow\text{futures hedge}\rightarrow\text{structured payoff}.
\]

Nếu intrinsic value đổi mạnh khi WACC hoặc terminal growth đổi, phải giảm độ tin cậy của kết luận valuation. Nếu hedge chỉ bù market beta, không được gọi nó là bảo hiểm toàn bộ danh mục. Nếu coupon chỉ xuất hiện vì short barrier/worst-of exposure, không được gọi sản phẩm là lợi suất cố định. Đây là ba boundary quan trọng nhất để chuyển Sách 3 từ công thức sang quyết định.
