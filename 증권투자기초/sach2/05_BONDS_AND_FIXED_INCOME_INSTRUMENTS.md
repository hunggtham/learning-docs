# 5. Trái phiếu và sản phẩm thu nhập cố định

Trái phiếu là bước chuyển từ quyền sở hữu residual sang quyền đòi hỏi theo hợp đồng. Bài 4 đã nói về cổ phiếu và chỉ số; bài này xây bản đồ payoff của fixed-income securities, để bài 6 có thể giải thích giá–lợi suất, tín dụng và duration mà không lẫn coupon với realized return.

## 1. Cấu trúc trái phiếu

Một trái phiếu thường có mệnh giá (face value), ngày đáo hạn (maturity date), lãi coupon (coupon) và coupon rate. Coupon = face value × coupon rate theo kỳ trả. Zero-coupon/discount bond không trả coupon định kỳ; nhà đầu tư mua dưới mệnh giá và nhận mệnh giá khi đáo hạn. Coupon bond trả dòng tiền định kỳ và mệnh giá ở cuối kỳ. Perpetuity bond không có ngày đáo hạn hữu hạn trong mô hình.

Giá trái phiếu là giá trị hiện tại của coupon và gốc:

```text
P = Σ [C / (1 + y)^t] + [F / (1 + y)^n]
```

`C` là coupon mỗi kỳ, `F` là face value, `y` là lợi suất chiết khấu và `n` là số kỳ. Khi `y` tăng, giá giảm; khi coupon rate bằng lợi suất thị trường, giá gần mệnh giá. Quan hệ ngược này là cơ chế, không phải quy tắc ghi nhớ rời.

## 2. Trái phiếu có quyền chọn hoặc cấu trúc lai

Convertible bond cho người sở hữu quyền chuyển thành cổ phiếu theo điều khoản; giá chịu ảnh hưởng của cả trái phiếu và quyền chọn cổ phiếu. Bond with warrant gắn quyền mua riêng hoặc đi kèm; exchangeable bond cho phép đổi sang chứng khoán của tổ chức khác. Callable bond cho tổ chức phát hành quyền mua lại trước hạn; puttable bond cho nhà đầu tư quyền bán lại. Quyền chọn thay đổi thời hạn dòng tiền và làm duration không còn đơn giản.

## 3. Sản phẩm dựa trên tài sản hoặc chỉ số

ABS (Asset-Backed Securities) và MBS (Mortgage-Backed Securities) gom dòng tiền từ tài sản cơ sở rồi phát hành chứng khoán. Pay-through và pass-through khác nhau ở cách dòng tiền đi qua cấu trúc. CMO (Collateralized Mortgage Obligation) chia dòng tiền thế chấp thành tranche, tạo prepayment và extension risk khác nhau. Floating-rate bond điều chỉnh coupon theo lãi suất tham chiếu; reverse floater có coupon biến động ngược. Indexed bond gắn coupon hoặc gốc với chỉ số; international bond và eurobond liên quan nơi phát hành, tiền tệ và nhà đầu tư, không mặc nhiên loại bỏ rủi ro tỷ giá.

Preferred stock có quyền ưu tiên cổ tức hoặc tài sản so với common stock nhưng thường hạn chế quyền biểu quyết. Catastrophe bond chuyển một phần rủi ro thảm họa sang nhà đầu tư; nếu trigger xảy ra, principal có thể dùng để bù tổn thất. Structured note kết hợp trái phiếu với phái sinh, nên phải đọc payoff, collateral, issuer risk, liquidity và điều kiện trigger thay vì chỉ nhìn coupon quảng cáo.

### So sánh nhanh: cùng là “fixed income” nhưng payoff không giống nhau

Tên nhóm sản phẩm chỉ cho biết lớp tài sản; muốn đánh giá phải xác định ai sở hữu dòng tiền, biến cố nào làm dòng tiền lệch khỏi kế hoạch và rủi ro nào không thể quan sát từ coupon. Bảng dưới đây dùng cùng một bộ câu hỏi để tránh xếp các sản phẩm khác bản chất vào một rổ:

| Sản phẩm | Dòng tiền chính đến từ đâu? | Rủi ro đặc thù cần tách riêng | Câu hỏi kiểm tra trước khi định giá |
| --- | --- | --- | --- |
| Trái phiếu coupon thông thường | Coupon cố định + hoàn gốc | Lãi suất, tín dụng issuer, thanh khoản | YTM dựa trên giá nào và thứ tự ưu tiên khi vỡ nợ ra sao? |
| Zero-coupon | Khoản hoàn gốc duy nhất ở đáo hạn | Duration dài, nhạy với lãi suất, không có dòng tiền giữa kỳ | Khoảng thời gian khóa vốn và giá trị chiết khấu là bao nhiêu? |
| Convertible / warrant | Coupon hoặc gốc + quyền tham gia upside của tài sản cơ sở | Biến động cổ phiếu, dilution, điều khoản chuyển đổi | Quyền chuyển đổi thuộc ai, tỷ lệ chuyển đổi và ngày khóa quyền thế nào? |
| Callable / puttable | Dòng tiền trái phiếu + quyền mua lại/bán lại | Reinvestment risk hoặc extension risk | Ai có quyền kích hoạt, tại mức giá và thời điểm nào? |
| ABS / MBS / CMO | Dòng tiền từ pool tài sản và waterfall | Default pool, prepayment, tranche, pháp lý cấu trúc | Tiền trả theo pass-through hay waterfall; tranche chịu lỗ trước hay sau? |
| Floating-rate / reverse floater | Coupon gắn với benchmark, theo cùng chiều hoặc ngược chiều | Basis risk, reset, leverage coupon | Benchmark, spread, kỳ reset và floor/cap cụ thể là gì? |
| Structured note | Trái phiếu issuer + payoff phái sinh | Issuer risk, barrier/trigger, định giá khó và thanh khoản thấp | Nếu barrier/trigger xảy ra thì mất coupon, gốc hay cả hai? |

Điểm cần nhớ là **nguồn dòng tiền** và **quyền thay đổi dòng tiền** là hai trục khác nhau. Một MBS có thể có tài sản thế chấp nhưng vẫn chịu prepayment; một structured note có thể hứa coupon cao nhưng phần bù nằm ở rủi ro issuer hoặc quyền chọn bán cho nhà đầu tư. Vì thế không nên dùng một chỉ tiêu duy nhất (coupon, rating hay duration) để kết luận sản phẩm “an toàn”.

## 4. Cách đọc một sản phẩm

Trước khi định giá, ghi bảy câu hỏi: ai là issuer; dòng tiền cố định hay biến đổi; gốc trả khi nào; quyền chọn thuộc ai; tài sản bảo đảm và thứ tự ưu tiên ra sao; điều gì làm dòng tiền đổi; và thị trường thứ cấp có thanh khoản không. Hai sản phẩm cùng coupon có thể có duration, default risk và liquidity risk khác hẳn. Đây là mối nối từ classification sang mechanism.

## 5. Boundary của textbook-state

Tên sản phẩm, điều khoản phát hành và luật thuế thay đổi theo jurisdiction và ngày phát hành. Source cung cấp taxonomy, không cung cấp bản cập nhật pháp lý hiện tại. Trước khi mua sản phẩm thật, cần đọc prospectus và nguồn chính thức; không suy ra suitability từ tên gọi “fixed income”.

## 6. Worked bond price

Giả sử trái phiếu mệnh giá 1.000, coupon năm 6% và còn hai năm. Nếu lợi suất thị trường là 8%, giá lý thuyết là:

```text
P = 60/1,08 + (60 + 1.000)/(1,08)^2 ≈ 964,33
```

Giá thấp hơn mệnh giá vì coupon 6% thấp hơn lợi suất yêu cầu 8%. Nếu lợi suất giảm xuống 4%, cùng dòng tiền sẽ có giá cao hơn mệnh giá. Ví dụ này cho thấy coupon rate cố định nhưng market yield thay đổi; không được gọi coupon 6% là “lợi suất chắc chắn” khi mua trên thị trường thứ cấp.

## 7. Payoff map cho sản phẩm lai

Convertible bond có một phần trái phiếu và một quyền chọn chuyển đổi; khi giá cổ phiếu tăng, quyền chọn có thể làm giá sản phẩm tăng nhanh hơn trái phiếu thuần. Callable bond trao quyền cho issuer mua lại khi lãi suất giảm, nên nhà đầu tư bị giới hạn upside và chịu reinvestment risk. Puttable bond trao quyền ngược lại cho nhà đầu tư, thường có giá trị bảo vệ khi lãi suất tăng hoặc credit xấu đi. ABS/MBS thêm prepayment và waterfall risk: dòng tiền có thể đến sớm, đến muộn hoặc bị phân tầng khác dự kiến.

Khi đọc structured note, hãy tách payoff thành trái phiếu nền + quyền chọn + rủi ro issuer + điều kiện trigger. Coupon cao có thể là tiền bán quyền chọn hoặc bù cho thanh khoản thấp, không phải “free yield”. Đây là mental model giúp người học không nhầm tên sản phẩm với mức an toàn.

## Chốt và bàn giao

Invariant là “trái phiếu là gói dòng tiền có thời điểm, ưu tiên và quyền chọn”. Giá phụ thuộc discount rate và xác suất dòng tiền thực sự nhận được. Bài 6 dùng invariant này để giải YTM, đường cong lợi suất, spread, duration và chỉ số trái phiếu. Xem [Lợi suất và rủi ro trái phiếu](./06_BOND_YIELDS_RISK_DURATION_AND_INDICES.md).
