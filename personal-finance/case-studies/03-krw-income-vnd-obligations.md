# Case 03 — Thu nhập KRW, nghĩa vụ VND: household cross-border phải quản lý gì?

## Bối cảnh

Một người sống và làm việc tại Hàn Quốc, nhận salary bằng KRW nhưng có các nghĩa vụ thường xuyên tại Việt Nam:

```text
Korea
- rent, utilities, food, transport bằng KRW
- emergency spending chủ yếu bằng KRW

Vietnam
- hỗ trợ gia đình hàng tháng bằng VND
- một khoản mục tiêu lớn trong 18 tháng tới bằng VND
- một phần savings đang nằm tại ngân hàng Việt Nam
```

Case không dự đoán tỷ giá. Mục tiêu là hiểu **currency mismatch**: income được tạo bằng một currency nhưng một phần liabilities/goals nằm ở currency khác.

## 1. Chọn functional currency

Để quản lý household, nên chọn một đồng tiền báo cáo chính — functional currency — thường là currency của phần lớn daily obligations.

Nếu sống ở Hàn Quốc và phần lớn expense tháng bằng KRW, KRW có thể là functional currency cho dashboard. Nhưng điều này không biến VND obligations thành không quan trọng.

Balance sheet nên giữ cả hai lớp:

```text
Native currency value
+
Converted reporting value
```

Ví dụ:

```text
Vietnam family obligation: 12m VND/month
Report also as KRW equivalent at review date
```

Không hard-code exchange rate trong document. Tỷ giá phải được ghi với ngày nếu dùng cho quyết định thực tế.

## 2. FX exposure nằm ở cash flow, không chỉ investment

Nhiều người nghĩ foreign-exchange risk chỉ liên quan Forex trading. Với household, FX exposure xuất hiện tự nhiên:

```text
KRW income
→ VND family obligation
```

Nếu VND mạnh lên tương đối so với KRW, cùng một nghĩa vụ VND cần nhiều KRW hơn. Household purchasing power giảm dù salary KRW không đổi.

Đó là household FX risk, không phải trading position chủ động.

## 3. Đo nghĩa vụ theo tỷ lệ income

Thay vì chỉ nhìn số tiền transfer, đo burden:

```text
Cross-border obligation ratio
= KRW-equivalent required transfers / take-home income
```

Nếu take-home income là 4.5m KRW và required transfer bình thường tương đương 0.7m KRW, burden khoảng 15.6% income.

Nếu FX shock làm equivalent tăng lên 0.9m KRW:

```text
0.9 / 4.5 = 20%
```

Không có threshold universal. Điều quan trọng là household nhìn thấy obligation đang ăn vào cash-flow margin nhanh thế nào.

## 4. Transfer cost không chỉ là fee hiển thị

Một remittance có total cost gồm:

```text
explicit fee
+ FX spread
+ intermediary fee nếu có
+ receiving fee nếu có
+ delay / timing cost
```

Hai service đều quảng cáo “fee thấp” có thể có all-in cost khác nhau vì exchange rate.

Khi so, dùng cùng:

```text
same source amount
same timestamp/window
same destination currency
same receiving amount basis
```

Không so fee của service A với FX rate của service B ở thời điểm khác.

## 5. Emergency fund phải match currency và location

Nếu daily life ở Seoul cần KRW, toàn bộ emergency fund nằm ở Việt Nam bằng VND không phải equivalent hoàn hảo vì:

- cần convert;
- cần transfer;
- có cut-off/weekend/delay;
- account có thể gặp verification friction;
- FX có thể bất lợi đúng lúc cần tiền.

Do đó có thể tách:

```text
Korea emergency layer — KRW, immediately accessible
Vietnam obligation layer — VND, near upcoming VND needs
Secondary reserve — cross-border transferable assets/cash
```

Tỷ lệ exact tùy household. Nguyên tắc là **liability matching**: near-term obligation nên có liquidity gần đúng currency và jurisdiction cần dùng.

## 6. Goal 18 tháng tại Việt Nam

Giả sử cần một khoản VND lớn sau 18 tháng. Nếu toàn bộ goal asset được giữ bằng KRW đến sát deadline, household đang chấp nhận FX uncertainty trên toàn bộ target.

Một cách quản lý không cần dự đoán currency winner là chuyển dần risk profile khi deadline đến gần:

```text
early stage
→ more flexibility

near target date
→ progressively match more of required VND liability
```

Đây là duration/liability matching trong personal finance. Không phải recommendation mua bán currency cụ thể.

## 7. Không dùng Forex trading để “hedge” một household chưa hiểu exposure

Một lỗi nguy hiểm:

```text
"Tôi có nghĩa vụ VND nên tôi sẽ trade Forex để hedge."
```

Nếu không hiểu contract size, leverage, rollover, margin, basis và tax/regulatory issues, trading có thể tạo risk lớn hơn exposure ban đầu.

Household hedging tự nhiên thường bắt đầu từ đơn giản hơn:

```text
match part of near-term liabilities with same currency
→ stagger transfers
→ maintain buffers on both sides
→ reduce timing pressure
```

Nếu cần derivatives/FX trading mechanics, owner là [Investing — Forex](../../investing/05_trading_derivatives/forex/README.md).

## 8. Thuế và residency không được suy từ nơi đặt bank account

Có tài khoản ở Việt Nam, sống ở Hàn Quốc hoặc nhận income từ một quốc gia không tự động quyết định tax residency cho mọi trường hợp.

Cross-border tax analysis cần ít nhất:

```text
jurisdiction
income type
residency status
source of income
relevant treaty/rules
reporting requirement
period concerned
```

Chapter [08 Taxes](../08-taxes.md) giữ framework; rule cụ thể phải kiểm tra source chính thức hiện hành.

## 9. Stress test household FX

Giả sử current monthly structure:

```text
Take-home income             4.5m KRW
Korea essential spending     2.3m
Vietnam required transfer    0.7m equivalent
Debt                         0.3m
--------------------------------
Margin                        1.2m
```

Stress simultaneously:

```text
income -10%
Korea living cost +10%
VND obligation equivalent +20%
```

Khi đó:

```text
Income = 4.05m
Korea = 2.53m
Vietnam = 0.84m
Debt = 0.3m
Margin = 0.38m
```

Household vẫn positive cash flow nhưng resilience giảm mạnh. Đây là lý do không đánh giá each risk riêng lẻ.

## 10. Dashboard cross-border tối giản

Có thể thêm vào monthly dashboard:

```text
KRW take-home income
KRW essential burn
Required VND obligations
KRW-equivalent VND obligations
KRW emergency months
VND near-term reserve
Next large VND goal + date
Transfer all-in cost
Assets by currency
Liabilities/goals by currency
```

Mục tiêu không phải theo dõi FX mỗi giờ. Mục tiêu là thấy **mismatch có đủ lớn để phá household plan hay không**.

## Kết luận

Một household Hàn–Việt không chỉ có “hai bank account”. Nó có một balance sheet đa currency và đa jurisdiction. Rủi ro chính là **income, asset và obligation không cùng currency, location và timing**.

Đọc [15 Financial Resilience](../15-financial-resilience.md), [16 Korea–Vietnam Practical Map](../16-korea-vietnam-practical-map.md) và [17 Cross-Border Personal Finance](../17-cross-border-personal-finance.md) để nối case về framework gốc.