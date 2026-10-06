# Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**. Route đi từ signal/position sizing → order book và price formation → execution costs/slippage → portfolio, liquidity và risk limits → transaction-cost analysis, để tín hiệu chuyển thành lợi thế sau chi phí.

> Tín hiệu tốt chưa đủ. Một chiến lược chỉ tạo được lợi thế thật khi lệnh được thực thi với chi phí hợp lý, quy mô vị thế đúng, trạng thái tài khoản chính xác và rủi ro được quản lý ở cấp toàn danh mục. Chương này giải thích bằng tiếng Việt toàn bộ chuỗi từ sổ lệnh tới phân tích chi phí giao dịch; thuật ngữ tiếng Anh chỉ giữ trong ngoặc hoặc dưới dạng viết tắt chuẩn khi cần tra cứu.

# Phần I — Một hệ thống giao dịch có ba lớp

## 1. Tín hiệu, quy mô rủi ro và thực thi

Một hệ thống tối thiểu gồm:

```text
Tạo tín hiệu (signal generation)
→ Xác định quy mô rủi ro (risk sizing)
→ Thực thi lệnh (execution)
```

Nếu kỳ vọng lợi nhuận trước chi phí là `+0,12R` nhưng tổng chênh lệch mua–bán, phí và trượt giá là `0,10R`, phần lớn lợi thế đã biến mất.

Vì vậy thực thi lệnh không phải hậu cần; nó là một phần của kinh tế chiến lược.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **2. Giá quyết định và giá thực thi** nối từ **1. Tín hiệu, quy mô rủi ro và thực thi** sang **3. Sổ lệnh**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Giá quyết định và giá thực thi

Trước khi đo slippage, cần tách giá tại thời điểm strategy quyết định giao dịch khỏi giá thực tế được khớp. Khoảng cách giữa hai mức là phần execution risk mà backtest thường dễ bỏ qua.

**Giá quyết định (decision price)** là mức giá khi chiến lược quyết định giao dịch.

**Giá thực thi (execution price)** là mức giá khớp thật.

Khoảng cách giữa hai mức có thể đến từ:

- chênh lệch mua–bán (spread);
- độ trễ (latency / 지연 시간);
- tác động của chính lệnh lên giá (market impact);
- thời gian chờ;
- lệnh không khớp;
- biến động thị trường trong lúc thực thi.

Đây là nền tảng của **mức thiếu hụt do thực thi (implementation shortfall)**.

# Phần II — Sổ lệnh giới hạn

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **3. Sổ lệnh** nối từ **2. Giá quyết định và giá thực thi** sang **4. Ưu tiên giá–thời gian**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Sổ lệnh

Order book cho thấy thanh khoản đang chờ ở từng mức giá, nhưng không bảo đảm các lệnh đó còn tồn tại khi lệnh của bạn tới. Hãy đọc độ sâu, sự thay đổi hàng chờ và khả năng rút lệnh cùng nhau.

**Sổ lệnh giới hạn (limit order book)** chứa các lệnh mua và bán đang chờ theo từng mức giá.

```text
Giá mua tốt nhất = best bid
Giá bán tốt nhất = best ask
Chênh lệch = best ask - best bid
```

**độ sâu (depth / 깊이)** cho biết khối lượng có sẵn ở nhiều mức giá. Chênh lệch hẹp nhưng độ sâu rất mỏng vẫn có thể gây trượt giá lớn cho lệnh lớn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **4. Ưu tiên giá–thời gian** nối từ **3. Sổ lệnh** sang **5. Vị trí trong hàng chờ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Ưu tiên giá–thời gian

Nhiều sở giao dịch dùng nguyên tắc gần với **ưu tiên giá–thời gian (price-time priority)**:

```text
Giá tốt hơn được ưu tiên trước
→ nếu cùng giá, lệnh vào trước thường được ưu tiên trước
```

Do đó kiểm thử giả định “giá chạm lệnh giới hạn = chắc chắn khớp” thường quá lạc quan.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **5. Vị trí trong hàng chờ** nối từ **4. Ưu tiên giá–thời gian** sang **6. Bên cung cấp và bên lấy thanh khoản**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Vị trí trong hàng chờ

Queue position quyết định xác suất một lệnh limit được khớp trước khi giá rời vùng. Vì vậy, giá đặt đúng chưa đủ; cần biết khối lượng trước mình, tốc độ khớp và khả năng lệnh bị rút.

**Vị trí hàng chờ (queue position)** ảnh hưởng xác suất khớp. Nó phụ thuộc:

- khối lượng lệnh đang đứng trước;
- lệnh bị hủy;
- lệnh thị trường mới đi vào;
- quy tắc của nơi giao dịch;
- thời gian chờ.

Với chiến lược rất ngắn hạn, mô hình hàng chờ có thể quan trọng gần ngang chất lượng tín hiệu.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **6. Bên cung cấp và bên lấy thanh khoản** nối từ **5. Vị trí trong hàng chờ** sang **7. Lệnh thị trường**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Bên cung cấp và bên lấy thanh khoản

Maker và taker chịu trade-off khác nhau giữa phí, xác suất khớp và rủi ro adverse selection. Phân biệt hai vai trò giúp chọn loại lệnh phù hợp với tốc độ mất giá của tín hiệu.

**Bên cung cấp thanh khoản (maker)** thường đặt lệnh chờ. **Bên lấy thanh khoản (taker)** giao dịch chủ động với lệnh đang có sẵn.

Bên cung cấp thanh khoản có thể tiết kiệm chênh lệch nhưng chịu:

- rủi ro không khớp;
- lựa chọn bất lợi (adverse selection);
- chi phí cơ hội.

Bên lấy thanh khoản có khả năng khớp nhanh hơn nhưng trả chênh lệch và có thể gây tác động giá.

# Phần III — Các loại lệnh

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **7. Lệnh thị trường** nối từ **6. Bên cung cấp và bên lấy thanh khoản** sang **8. Lệnh giới hạn có thể khớp ngay**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Lệnh thị trường

Market order ưu tiên certainty of execution hơn certainty of price. Nó phù hợp khi không khớp còn tệ hơn giá xấu, nhưng cần stress spread, depth và gap trước khi dùng.

**Lệnh thị trường (market order)** ưu tiên khả năng được khớp, không bảo đảm mức giá chính xác.

Trong thị trường mỏng hoặc khi có tin lớn, giá khớp có thể xa mức nhìn thấy trước khi gửi lệnh.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **7. Lệnh thị trường** đặt tiêu chí; **8. Lệnh giới hạn có thể khớp ngay** dùng tiêu chí đó để kiểm tra ranh giới, rồi **9. Lệnh giới hạn thụ động** mở rộng hệ quả.

## 8. Lệnh giới hạn có thể khớp ngay

Marketable limit order cố giữ trần giá trong khi vẫn muốn khớp ngay. Cần cân bằng rủi ro không khớp với rủi ro bị adverse selection nếu giá chạm giới hạn rồi đảo chiều.

**Lệnh giới hạn chủ động (marketable limit order)** đi qua chênh lệch hiện tại nhưng vẫn đặt giới hạn cho mức giá tệ nhất chấp nhận được.

Nó giảm nguy cơ khớp cực xấu nhưng có thể chỉ khớp một phần trong thị trường chạy nhanh.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **8. Lệnh giới hạn có thể khớp ngay** đặt tiêu chí; **9. Lệnh giới hạn thụ động** dùng tiêu chí đó để kiểm tra ranh giới, rồi **10. Lệnh dừng** mở rộng hệ quả.

## 9. Lệnh giới hạn thụ động

Passive limit order tiết kiệm spread nhưng đổi lại chịu rủi ro không khớp và bị chọn bất lợi. Nó phù hợp hơn khi tín hiệu có độ bền và nhà giao dịch chấp nhận chờ.

**Lệnh giới hạn thụ động (passive limit order)** kiểm soát giá nhưng có thể không khớp.

Một vấn đề quan trọng là **lựa chọn bất lợi (adverse selection)**: lệnh có thể được khớp nhiều nhất đúng lúc giá sắp tiếp tục đi ngược vị thế.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **9. Lệnh giới hạn thụ động** đặt tiêu chí; **10. Lệnh dừng** dùng tiêu chí đó để kiểm tra ranh giới, rồi **11. Lệnh dừng–giới hạn** mở rộng hệ quả.

## 10. Lệnh dừng

Lệnh dừng (stop order) chỉ kích hoạt sau khi đạt điều kiện. Giá kích hoạt không phải giá khớp được bảo đảm.

Khoảng nhảy giá có thể biến kế hoạch `-1R` thành tổn thất lớn hơn đáng kể.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **10. Lệnh dừng** đặt tiêu chí; **11. Lệnh dừng–giới hạn** dùng tiêu chí đó để kiểm tra ranh giới, rồi **12. Thời hạn hiệu lực của lệnh** mở rộng hệ quả.

## 11. Lệnh dừng–giới hạn

Lệnh dừng–giới hạn (stop-limit) kiểm soát mức giá tệ nhất nhưng có nguy cơ không thoát được nếu thị trường chạy qua vùng giới hạn quá nhanh.

Vì vậy nó không tự động an toàn hơn lệnh dừng thị trường.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **11. Lệnh dừng–giới hạn** đặt tiêu chí; **12. Thời hạn hiệu lực của lệnh** dùng tiêu chí đó để kiểm tra ranh giới, rồi **13. Khớp một phần** mở rộng hệ quả.

## 12. Thời hạn hiệu lực của lệnh

Một số quy ước phổ biến:

- DAY;
- GTC;
- IOC;
- FOK.

**Thời hạn hiệu lực (time-in-force)** là một phần của lô-gic (logic / 논리) thực thi, không chỉ là tùy chọn giao diện.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **13. Khớp một phần** nối từ **12. Thời hạn hiệu lực của lệnh** sang **14. Giao dịch nhiều chân**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Khớp một phần

Nếu lệnh chỉ khớp một phần, mức phơi nhiễm thực tế khác mức dự kiến.

Hệ thống phải theo dõi:

```text
Khối lượng yêu cầu
Khối lượng đã khớp
Khối lượng còn lại
Vị thế thực tế
```

trước khi gửi lệnh thay thế.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **14. Giao dịch nhiều chân** nối từ **13. Khớp một phần** sang **15. Vì sao chênh lệch tồn tại?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Giao dịch nhiều chân

Spread quyền chọn hoặc cấu trúc phòng vệ nhiều chân có thể giao dịch dưới dạng gói hoặc từng chân.

Thực thi từng chân tạo **rủi ro lệch chân (legging risk)**: chân đầu đã khớp nhưng chân sau di chuyển khỏi mức giá dự kiến.

# Phần IV — Chênh lệch mua–bán và thanh khoản

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **15. Vì sao chênh lệch tồn tại?** nối từ **14. Giao dịch nhiều chân** sang **16. Chênh lệch niêm yết và chênh lệch hiệu dụng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Vì sao chênh lệch tồn tại?

Chênh lệch mua–bán bù cho nhà cung cấp thanh khoản các rủi ro như:

- lựa chọn bất lợi;
- rủi ro tồn kho;
- biến động;
- sử dụng vốn;
- phí của nơi giao dịch.

Khi bất định tăng, chênh lệch thường rộng hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **16. Chênh lệch niêm yết và chênh lệch hiệu dụng** nối từ **15. Vì sao chênh lệch tồn tại?** sang **17. Chênh lệch thực giữ được**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Chênh lệch niêm yết và chênh lệch hiệu dụng

Quoted spread là chi phí nhìn thấy; realized spread và execution outcome mới cho biết chi phí thực sự sau khớp, adverse selection và biến động tiếp theo.

**Chênh lệch niêm yết (quoted spread)** là khoảng bid–ask đang hiển thị.

**Chênh lệch hiệu dụng (effective spread)** đo chi phí khớp thực tế so với điểm giữa hoặc mức tham chiếu.

Khớp được giá tốt hơn có thể làm chi phí thấp hơn chênh lệch niêm yết; thị trường biến động nhanh có thể làm chi phí cao hơn.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **17. Chênh lệch thực giữ được** nối từ **16. Chênh lệch niêm yết và chênh lệch hiệu dụng** sang **18. Thanh khoản là khái niệm nhiều chiều**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Chênh lệch thực giữ được

Realized spread giúp tách phần spread còn lại cho liquidity provider khỏi phần giá đi tiếp chống lại lệnh. Đây là bước nối quote quality với chất lượng thực thi và adverse selection.

**Chênh lệch thực giữ được (realized spread)** đo phần chênh lệch còn lại sau một khoảng thời gian, giúp tách:

```text
Thu nhập từ chênh lệch
và
Tổn thất do lựa chọn bất lợi
```

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **18. Thanh khoản là khái niệm nhiều chiều** nối từ **17. Chênh lệch thực giữ được** sang **19. Thanh khoản ẩn và lệnh iceberg**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Thanh khoản là khái niệm nhiều chiều

Cần nhìn cùng:

- chênh lệch;
- độ sâu;
- khả năng hồi phục của sổ lệnh;
- giá trị giao dịch;
- tác động giá;
- số ngày cần để thoát vị thế.

Khối lượng cao không bảo đảm một lệnh lớn có thể thoát với chi phí thấp.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **19. Thanh khoản ẩn và lệnh iceberg** nối từ **18. Thanh khoản là khái niệm nhiều chiều** sang **20. Nơi giao dịch không hiển thị trước lệnh**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Thanh khoản ẩn và lệnh iceberg

Một số lệnh chỉ hiển thị một phần khối lượng. Vì vậy độ sâu nhìn thấy có thể thấp hơn thanh khoản thật.

Ngược lại, thanh khoản đang hiển thị cũng có thể biến mất nhanh; ảnh chụp sổ lệnh không phải cam kết.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **20. Nơi giao dịch không hiển thị trước lệnh** nối từ **19. Thanh khoản ẩn và lệnh iceberg** sang **21. Thị trường phân mảnh theo nhiều nơi giao dịch**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Nơi giao dịch không hiển thị trước lệnh

Dark pool và venue ngoài sở có thể giảm information leakage cho lệnh lớn, nhưng làm price discovery, routing và đánh giá benchmark phức tạp hơn. Lợi ích execution phải được so với độ minh bạch bị mất.

**Dark pool** hoặc nơi giao dịch ngoài sở có thể giảm khả năng lệnh lớn tự tiết lộ ý định trước giao dịch, nhưng làm quá trình khám phá giá và đánh giá chất lượng thực thi phức tạp hơn.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **21. Thị trường phân mảnh theo nhiều nơi giao dịch** nối từ **20. Nơi giao dịch không hiển thị trước lệnh** sang **22. Khám phá giá**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Thị trường phân mảnh theo nhiều nơi giao dịch

Một chứng khoán có thể giao dịch ở nhiều địa điểm. Định tuyến tốt phải cân nhắc:

```text
Giá
Phí / hoàn phí
Hàng chờ
Độ trễ
Xác suất khớp
```

Giá hiển thị tốt nhất chưa chắc tạo kết quả thực tế tốt nhất.

# Phần V — Khám phá giá và phiên đấu giá

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **22. Khám phá giá** nối từ **21. Thị trường phân mảnh theo nhiều nơi giao dịch** sang **23. Đấu giá mở cửa**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Khám phá giá

Price discovery là quá trình thông tin, lệnh và thanh khoản cùng cập nhật giá. Một lệnh lớn có thể vừa phản ánh thông tin vừa tự tạo market impact, nên cần tách alpha khỏi dấu chân thực thi.

**Khám phá giá (price discovery)** là quá trình thông tin mới được phản ánh vào giá.

Tùy thị trường, thông tin có thể xuất hiện trước ở hợp đồng tương lai, ETF, quyền chọn, FX hoặc thị trường cơ sở.

Không nên dùng giá tham chiếu đã cũ như thể đó là giá trị hợp lý hiện tại.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **23. Đấu giá mở cửa** nối từ **22. Khám phá giá** sang **24. Đấu giá đóng cửa**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Đấu giá mở cửa

Đấu giá mở cửa gom thông tin qua đêm và lệnh chờ. Kiểm thử “mua tại giá mở cửa” phải mô hình hóa khoảng nhảy giá và cơ chế đấu giá thực tế.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **24. Đấu giá đóng cửa** nối từ **23. Đấu giá mở cửa** sang **25. Mẫu hình trong ngày**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Đấu giá đóng cửa

Đấu giá đóng cửa thường có khối lượng lớn do:

- quỹ chỉ số;
- danh mục bám chuẩn;
- tái cân bằng;
- dòng lệnh tổ chức.

Giá đóng cửa chính thức không có nghĩa mọi nhà giao dịch đều có thể khớp đúng mức đó.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **25. Mẫu hình trong ngày** nối từ **24. Đấu giá đóng cửa** sang **26. Trượt giá**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Mẫu hình trong ngày

Khối lượng và biến động thường có mẫu hình theo thời gian trong ngày. Cổ phiếu thường sôi động hơn đầu/cuối phiên; FX chịu ảnh hưởng các phiên châu Á, London và New York.

Mô hình chi phí nên phản ánh thời điểm giao dịch.

# Phần VI — Trượt giá và tác động thị trường

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **26. Trượt giá** nối từ **25. Mẫu hình trong ngày** sang **27. Mức thiếu hụt do thực thi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Trượt giá

Slippage là kết quả cuối của spread, queue, depth, volatility, latency và loại lệnh. Đo nó theo từng trạng thái thị trường giúp mô hình cost không bị quá lạc quan.

**Trượt giá (slippage)** là chênh lệch giữa giá kỳ vọng và giá thực thi.

Nó phụ thuộc:

- biến động;
- mức khẩn cấp;
- kích thước lệnh so với độ sâu;
- độ trễ;
- loại lệnh;
- rủi ro sự kiện.

Không nên dùng một con số trượt giá cố định cho mọi chế độ thị trường.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **27. Mức thiếu hụt do thực thi** nối từ **26. Trượt giá** sang **28. Chi phí cơ hội**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Mức thiếu hụt do thực thi

Implementation shortfall đặt toàn bộ chi phí cơ hội và chi phí thực thi cạnh nhau: không giao dịch, trì hoãn, giá khớp, fees và market impact. Nó phù hợp để đánh giá quyết định thực thi ở cấp chiến lược.

**Mức thiếu hụt do thực thi (implementation shortfall)** đo khoảng cách giữa kết quả giả định nếu giao dịch được thực hiện tại giá quyết định và kết quả thật sau thực thi.

Có thể phân rã thành:

```text
Phí
+ chênh lệch mua–bán
+ chi phí trì hoãn
+ tác động thị trường
+ chi phí cơ hội
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **28. Chi phí cơ hội** nối từ **27. Mức thiếu hụt do thực thi** sang **29. Tác động thị trường**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Chi phí cơ hội

Một lệnh thụ động không khớp có thể không mất phí nhưng vẫn tạo chi phí nếu bỏ lỡ một biến động có lợi.

“Không giao dịch được” cũng là một dạng chi phí thực thi.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **29. Tác động thị trường** nối từ **28. Chi phí cơ hội** sang **30. Tác động tạm thời và tác động lâu dài**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Tác động thị trường

Chính lệnh của bạn có thể làm giá di chuyển. Tác động thường tăng khi:

- lệnh lớn so với thanh khoản;
- độ sâu thấp;
- yêu cầu hoàn tất nhanh;
- biến động cao.

**Công suất chiến lược (strategy capacity)** bị giới hạn bởi tác động thị trường, không chỉ bởi số dư tài khoản.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **30. Tác động tạm thời và tác động lâu dài** nối từ **29. Tác động thị trường** sang **31. Tỷ lệ tham gia**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Tác động tạm thời và tác động lâu dài

Tác động tạm thời có thể hồi lại sau khi lệnh hoàn tất. Tác động lâu dài phản ánh thông tin hoặc tín hiệu từ lệnh đã được thị trường hấp thụ.

Thực thi tốt cố giảm phần tác động không cần thiết.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **31. Tỷ lệ tham gia** nối từ **30. Tác động tạm thời và tác động lâu dài** sang **32. Công suất chiến lược**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Tỷ lệ tham gia

Participation rate điều chỉnh tốc độ giao dịch theo volume thị trường. Nó giảm nguy cơ chiếm tỷ lệ quá lớn trong một thời điểm, nhưng có thể kéo dài execution khi thanh khoản giảm hoặc biến động tăng.

```text
Tỷ lệ tham gia
= Khối lượng của mình / Khối lượng thị trường
```

Tỷ lệ cao giúp hoàn tất nhanh hơn nhưng thường làm tăng tác động giá và rủi ro tiết lộ ý định.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **32. Công suất chiến lược** nối từ **31. Tỷ lệ tham gia** sang **33. TWAP**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Công suất chiến lược

Công suất trả lời câu hỏi:

> Có thể triển khai bao nhiêu vốn trước khi chi phí ăn hết lợi thế?

Cần xem vòng quay, giá trị giao dịch trung bình, thời gian nắm giữ, tỷ lệ tham gia và kịch bản thoát khi căng thẳng.

# Phần VII — Thuật toán thực thi

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **33. TWAP** nối từ **32. Công suất chiến lược** sang **34. VWAP**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. TWAP

TWAP chia lệnh tương đối đều theo thời gian. Cách này đơn giản nhưng không thích nghi tốt khi thanh khoản trong ngày thay đổi mạnh.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **34. VWAP** nối từ **33. TWAP** sang **35. POV**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. VWAP

VWAP phân bổ lệnh theo hồ sơ khối lượng dự kiến hoặc thực tế. Đánh bại VWAP chỉ cho biết chất lượng thực thi so với chuẩn đó, không chứng minh quyết định đầu tư ban đầu là đúng.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **35. POV** nối từ **34. VWAP** sang **36. Thuật toán tối ưu mức thiếu hụt do thực thi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. POV

POV duy trì tỷ lệ giao dịch gần cố định so với volume quan sát được. Hãy kiểm tra volume đó có bị phình do event hoặc toxic flow hay không trước khi coi POV là kiểm soát impact.

**Tỷ lệ theo khối lượng (Percentage-of-Volume, POV)** duy trì một tỷ lệ giao dịch gần cố định so với khối lượng thị trường. Nó thích nghi với mức độ hoạt động nhưng có thể giao dịch nhiều hơn đúng lúc biến động tăng.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **36. Thuật toán tối ưu mức thiếu hụt do thực thi** nối từ **35. POV** sang **37. Giá tại thời điểm bắt đầu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. Thuật toán tối ưu mức thiếu hụt do thực thi

Loại thuật toán này cân bằng:

```text
Tác động giá nếu giao dịch nhanh
với
Rủi ro giá nếu chờ lâu
```

Mức khẩn cấp cao thường dẫn tới thực thi nhiều hơn ở đầu khoảng thời gian.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **37. Giá tại thời điểm bắt đầu** nối từ **36. Thuật toán tối ưu mức thiếu hụt do thực thi** sang **38. Định tuyến lệnh thông minh**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. Giá tại thời điểm bắt đầu

Arrival price là benchmark cho quyết định bắt đầu thực thi. Nó phù hợp với tín hiệu mất giá nhanh, nhưng cần ghi rõ khi nào benchmark thay đổi vì delay là một phần của chiến lược.

**Giá lúc bắt đầu thực thi (arrival price)** là mức giá khi quá trình thực thi được khởi động và thường phù hợp với chiến lược có tín hiệu mất giá trị nhanh.

Chuẩn so sánh phải được chọn trước khi nhìn kết quả.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **38. Định tuyến lệnh thông minh** nối từ **37. Giá tại thời điểm bắt đầu** sang **39. Lựa chọn bất lợi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Định tuyến lệnh thông minh

SOR chọn venue bằng trade-off giữa giá, phí, queue, latency và xác suất fill. Routing tốt cần dữ liệu venue-level và phải được review khi cấu trúc thị trường thay đổi.

**Định tuyến lệnh thông minh (Smart Order Routing, SOR)** chọn nơi giao dịch dựa trên giá, phí, hàng chờ, độ trễ và xác suất khớp.

Mục tiêu là chất lượng khớp thực tế tốt hơn, không chỉ giá hiển thị tốt hơn.

# Phần VIII — Lựa chọn bất lợi và chất lượng dòng lệnh

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **39. Lựa chọn bất lợi** nối từ **38. Định tuyến lệnh thông minh** sang **40. Dòng lệnh bất lợi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 39. Lựa chọn bất lợi

Một lệnh thụ động có thể chỉ được khớp khi phía đối diện có lợi thế thông tin hoặc khi giá sắp di chuyển ngược vị thế.

Do đó “kiếm chênh lệch” chưa chắc tạo lợi nhuận thực.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **40. Dòng lệnh bất lợi** nối từ **39. Lựa chọn bất lợi** sang **41. Quét thanh khoản**, vì cơ chế trước tạo đầu vào cho bước sau.

## 40. Dòng lệnh bất lợi

Nhà cung cấp thanh khoản đôi khi gọi **dòng lệnh độc (toxic flow)** là dòng lệnh thường xuất hiện ngay trước biến động giá bất lợi cho họ.

Đây là vấn đề thông tin và thời điểm, không nên mặc định diễn giải thành thao túng.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **41. Quét thanh khoản** nối từ **40. Dòng lệnh bất lợi** sang **42. Giao dịch quanh sự kiện**, vì cơ chế trước tạo đầu vào cho bước sau.

## 41. Quét thanh khoản

Các lệnh dừng và lệnh phá vỡ thường tập trung quanh đỉnh/đáy rõ ràng. Khi vùng đó bị xuyên:

```text
Lệnh kích hoạt ↑
→ lệnh thị trường tăng mạnh
→ nếu có thanh khoản đối ứng hấp thụ
→ giá có thể đảo chiều
```

Cơ chế này giải thích nhiều hành vi thường bị gắn nhãn “săn stop” mà không cần giả định âm mưu.

# Phần IX — Tin tức, khoảng nhảy giá và cơ chế kiểm soát thị trường

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **42. Giao dịch quanh sự kiện** nối từ **41. Quét thanh khoản** sang **43. Rủi ro nhảy giá**, vì cơ chế trước tạo đầu vào cho bước sau.

## 42. Giao dịch quanh sự kiện

CPI, NFP, FOMC, báo cáo lợi nhuận hoặc địa chính trị có thể làm:

- chênh lệch tăng;
- độ sâu giảm;
- trượt giá tăng;
- lệnh dừng bị nhảy qua;
- biến động hàm ý của quyền chọn thay đổi mạnh.

Chiến lược không được thiết kế cho điều kiện sự kiện nên có quy tắc giảm quy mô hoặc tránh giao dịch.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **43. Rủi ro nhảy giá** nối từ **42. Giao dịch quanh sự kiện** sang **44. Ngắt giao dịch**, vì cơ chế trước tạo đầu vào cho bước sau.

## 43. Rủi ro nhảy giá

Gap risk phá vỡ giả định rằng giá đi qua mọi mức trung gian. Stop, margin và hedge cần được stress bằng kịch bản không có fill tại trigger.

**Rủi ro nhảy giá (gap risk)** xuất hiện khi giá thay đổi rời rạc và đi qua mức dừng mà không giao dịch tại mọi mức trung gian.

Mô hình rủi ro phải tính những bước nhảy này thay vì giả định đường giá liên tục.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **44. Ngắt giao dịch** nối từ **43. Rủi ro nhảy giá** sang **45. Biên độ giá hằng ngày**, vì cơ chế trước tạo đầu vào cho bước sau.

## 44. Ngắt giao dịch

Cơ chế ngắt giao dịch (circuit breaker) hoặc tạm dừng chỉ ngăn giao dịch trong thời gian nhất định; nó không xóa rủi ro. Khi mở lại, giá vẫn có thể nhảy tiếp.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **45. Biên độ giá hằng ngày** nối từ **44. Ngắt giao dịch** sang **46. Độ trễ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 45. Biên độ giá hằng ngày

Ở thị trường có biên độ, vị thế có thể bị kẹt nhiều phiên nếu không có thanh khoản đối ứng. Quy mô vị thế phải tính cả kịch bản thoát qua nhiều phiên.

# Phần X — Hệ thống và độ an toàn vận hành

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **46. Độ trễ** nối từ **45. Biên độ giá hằng ngày** sang **47. Đồng bộ thời gian**, vì cơ chế trước tạo đầu vào cho bước sau.

## 46. Độ trễ

Độ trễ chỉ quan trọng so với thời hạn của chiến lược. Với giao dịch theo ngày hoặc tuần, vài trăm mili giây thường không quyết định; với chênh lệch giá dưới giây, nó có thể là yếu tố sống còn.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **47. Đồng bộ thời gian** nối từ **46. Độ trễ** sang **48. Chất lượng dữ liệu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 47. Đồng bộ thời gian

Dữ liệu thị trường, tín hiệu, lệnh và khớp lệnh cần cùng chuẩn thời gian. Nếu đồng hồ sai, việc so sánh mô phỏng với giao dịch thật trở nên thiếu tin cậy.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **47. Đồng bộ thời gian** đặt vấn đề; **48. Chất lượng dữ liệu** đối chiếu bằng chứng, rồi **49. Trạng thái tại nhà môi giới** mở rộng hệ quả hoặc giới hạn liên quan.

## 48. Chất lượng dữ liệu

Giá cũ, dữ liệu mất, điểm dữ liệu lỗi hoặc điều chỉnh hành động doanh nghiệp sai có thể tạo tín hiệu giả.

Hệ thống thực tế cần kiểm tra đầu vào và có hành vi an toàn khi dữ liệu bất thường.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **48. Chất lượng dữ liệu** đặt vấn đề; **49. Trạng thái tại nhà môi giới** đối chiếu bằng chứng, rồi **50. Tính không lặp tác dụng** mở rộng hệ quả hoặc giới hạn liên quan.

## 49. Trạng thái tại nhà môi giới

Thông báo “đã gửi lệnh” không có nghĩa lệnh đã khớp. Nếu kết nối mất, hệ thống phải hỏi lại trạng thái thật trước khi gửi lại.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **50. Tính không lặp tác dụng** nối từ **49. Trạng thái tại nhà môi giới** sang **51. Đối soát**, vì cơ chế trước tạo đầu vào cho bước sau.

## 50. Tính không lặp tác dụng

Idempotency bảo đảm retry sau lỗi mạng không tạo lệnh trùng hoặc exposure ngoài ý muốn. Đây là lớp an toàn vận hành, ngang hàng với logic tín hiệu và risk limits.

**Tính bất biến khi gửi lại (idempotency)** giúp tránh tạo lệnh trùng khi hệ thống thử lại sau lỗi mạng. Mã định danh lệnh phía khách hàng là công cụ quan trọng.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **51. Đối soát** nối từ **50. Tính không lặp tác dụng** sang **52. Công tắc dừng khẩn cấp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 51. Đối soát

Vị thế, tiền mặt và lệnh đang mở trong hệ thống nội bộ phải được đối soát với nhà môi giới sau mất kết nối hoặc khởi động lại.

Trạng thái tại nhà môi giới hoặc sở giao dịch mới là nguồn sự thật của mức phơi nhiễm thật.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **52. Công tắc dừng khẩn cấp** nối từ **51. Đối soát** sang **53. Tổng rủi ro dự kiến của các vị thế**, vì cơ chế trước tạo đầu vào cho bước sau.

## 52. Công tắc dừng khẩn cấp

Cần định nghĩa trước điều kiện dừng giao dịch, ví dụ:

- dữ liệu thị trường lỗi;
- lệnh trùng;
- chênh lệch bất thường;
- nhà môi giới mất kết nối;
- lỗ ngày vượt giới hạn;
- rủi ro vượt ngưỡng.

**Công tắc dừng (kill switch)** là cơ chế sống còn của hệ thống thực tế.

# Phần XI — Danh mục giao dịch

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **53. Tổng rủi ro dự kiến của các vị thế** nối từ **52. Công tắc dừng khẩn cấp** sang **54. Phơi nhiễm ròng và tổng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 53. Tổng rủi ro dự kiến của các vị thế

Tổng các mức lỗ dừng dự kiến không thể chỉ cộng cơ học nếu nhiều vị thế cùng phụ thuộc một nhân tố.

Năm giao dịch đều cược USD giảm có thể cùng thất bại dù mỗi giao dịch chỉ chiếm 0,5% rủi ro danh nghĩa.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **54. Phơi nhiễm ròng và tổng** nối từ **53. Tổng rủi ro dự kiến của các vị thế** sang **55. Phơi nhiễm nhân tố**, vì cơ chế trước tạo đầu vào cho bước sau.

## 54. Phơi nhiễm ròng và tổng

Danh mục long–short có beta ròng gần 0 nhưng vẫn có đòn bẩy tổng rất lớn.

Phơi nhiễm tổng quyết định nhu cầu nguồn vốn, vòng quay, thanh khoản và rủi ro nhảy giá. Cần theo dõi cả ròng lẫn tổng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **55. Phơi nhiễm nhân tố** nối từ **54. Phơi nhiễm ròng và tổng** sang **56. Phơi nhiễm tương đương Delta**, vì cơ chế trước tạo đầu vào cho bước sau.

## 55. Phơi nhiễm nhân tố

Nên ánh xạ vị thế sang các nhân tố như:

- USD;
- lãi suất;
- beta cổ phiếu;
- tăng trưởng;
- hàng hóa;
- biến động;
- quốc gia;
- thanh khoản.

Cách này phát hiện tập trung ẩn tốt hơn chỉ nhìn tương quan từng cặp.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **56. Phơi nhiễm tương đương Delta** nối từ **55. Phơi nhiễm nhân tố** sang **57. DV01 và rủi ro lãi suất**, vì cơ chế trước tạo đầu vào cho bước sau.

## 56. Phơi nhiễm tương đương Delta

Danh mục quyền chọn cần quy đổi theo Delta và theo dõi thêm Gamma, Vega. Phí quyền chọn nhỏ không có nghĩa mức phơi nhiễm kinh tế nhỏ.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **57. DV01 và rủi ro lãi suất** nối từ **56. Phơi nhiễm tương đương Delta** sang **58. Rủi ro biến động**, vì cơ chế trước tạo đầu vào cho bước sau.

## 57. DV01 và rủi ro lãi suất

Với trái phiếu và lãi suất, nên cộng gộp DV01 và DV01 theo điểm kỳ hạn. Bù trừ giá trị danh nghĩa có thể che một cược đường cong lớn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **58. Rủi ro biến động** nối từ **57. DV01 và rủi ro lãi suất** sang **59. Rủi ro thanh khoản**, vì cơ chế trước tạo đầu vào cho bước sau.

## 58. Rủi ro biến động

Bán quyền chọn, chiến lược carry và một số chiến lược hồi quy về trung bình có thể đều đang bán biến động dù dùng công cụ khác nhau.

Biến động nên được xem như một nhóm rủi ro riêng.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **59. Rủi ro thanh khoản** nối từ **58. Rủi ro biến động** sang **60. Tương quan không ổn định**, vì cơ chế trước tạo đầu vào cho bước sau.

## 59. Rủi ro thanh khoản

Cổ phiếu nhỏ, tín dụng lợi suất cao, tài sản số ít thanh khoản và hợp đồng tương lai đông người cùng vị thế có thể cùng mất thanh khoản khi nguồn vốn căng.

Tương quan thanh khoản thường tăng trong khủng hoảng.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **60. Tương quan không ổn định** nối từ **59. Rủi ro thanh khoản** sang **61. Nhắm mục tiêu độ biến động**, vì cơ chế trước tạo đầu vào cho bước sau.

## 60. Tương quan không ổn định

Tương quan lịch sử có thể thay đổi mạnh theo chế độ và thường tăng khi hệ thống giảm đòn bẩy. Cần dùng thêm kịch bản căng thẳng thay vì chỉ ma trận tương quan quá khứ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **61. Nhắm mục tiêu độ biến động** nối từ **60. Tương quan không ổn định** sang **62. Phân bổ ngang bằng rủi ro giữa giao dịch**, vì cơ chế trước tạo đầu vào cho bước sau.

## 61. Nhắm mục tiêu độ biến động

Nhắm mục tiêu độ biến động điều chỉnh quy mô vị thế để giữ rủi ro kỳ vọng ổn định hơn.

Điểm yếu là tính thuận chu kỳ: biến động thấp khuyến khích tăng vị thế trước cú sốc; biến động cao buộc giảm vị thế sau khi giá đã giảm.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **62. Phân bổ ngang bằng rủi ro giữa giao dịch** nối từ **61. Nhắm mục tiêu độ biến động** sang **63. VaR và Expected Shortfall**, vì cơ chế trước tạo đầu vào cho bước sau.

## 62. Phân bổ ngang bằng rủi ro giữa giao dịch

Cân bằng đóng góp độ biến động giúp tránh một thị trường thống trị toàn bộ danh mục, nhưng “cùng độ biến động” không có nghĩa cùng rủi ro đuôi. Cần điều chỉnh thêm cho nhảy giá, thanh khoản và tính phi tuyến.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **63. VaR và Expected Shortfall** nối từ **62. Phân bổ ngang bằng rủi ro giữa giao dịch** sang **64. Kiểm soát mức suy giảm**, vì cơ chế trước tạo đầu vào cho bước sau.

## 63. VaR và Expected Shortfall

VaR ước lượng ngưỡng tổn thất ở mức tin cậy nhất định. Expected Shortfall ước lượng tổn thất trung bình sau khi đã vượt ngưỡng đó.

Cả hai vẫn phụ thuộc dữ liệu và mô hình; kiểm thử kịch bản không thể bỏ qua.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **64. Kiểm soát mức suy giảm** nối từ **63. VaR và Expected Shortfall** sang **65. MAE và MFE**, vì cơ chế trước tạo đầu vào cho bước sau.

## 64. Kiểm soát mức suy giảm

Quy tắc giảm rủi ro khi mức suy giảm tăng phải được định nghĩa trước, dựa trên phân phối của chiến lược và khả năng mô hình bị hỏng, không dựa trên cảm xúc trong thời điểm thua lỗ.

# Phần XII — Phân tích chi phí giao dịch và vòng học

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **65. MAE và MFE** nối từ **64. Kiểm soát mức suy giảm** sang **66. Phân rã chất lượng thực thi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 65. MAE và MFE

MAE/MFE giúp nghiên cứu đường đi của giao dịch trong thời gian nắm giữ. Chúng hữu ích cho chẩn đoán nhưng không nên được dùng để tối ưu lệnh dừng trên cùng một mẫu dữ liệu rồi coi kết quả là chắc chắn.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **66. Phân rã chất lượng thực thi** nối từ **65. MAE và MFE** sang **67. Phân tích chi phí giao dịch**, vì cơ chế trước tạo đầu vào cho bước sau.

## 66. Phân rã chất lượng thực thi

Khoảng cách giữa mô phỏng và kết quả thật có thể tách thành:

```text
Thời điểm tín hiệu
Quy mô vị thế
Chênh lệch mua–bán
Phí
Trượt giá
Lệnh không khớp
Tác động thị trường
Can thiệp thủ công
```

Phải sửa đúng lớp gây rò rỉ lợi thế.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **67. Phân tích chi phí giao dịch** nối từ **66. Phân rã chất lượng thực thi** sang **68. Chi phí kỳ vọng và chi phí thực tế**, vì cơ chế trước tạo đầu vào cho bước sau.

## 67. Phân tích chi phí giao dịch

TCA là bước tổng kết execution: gom lệnh theo strategy, venue, thời điểm, loại lệnh và market state để biết chi phí đến từ spread, impact, delay hay routing. Kết quả phải quay lại điều chỉnh model cost và rule thực thi.

**Phân tích chi phí giao dịch (Transaction Cost Analysis, TCA)** phân nhóm lệnh theo:

- chuẩn so sánh;
- nơi giao dịch;
- loại lệnh;
- kích thước;
- thời gian;
- biến động;
- thanh khoản.

Mục tiêu là phát hiện có hệ thống nơi chiến lược đang mất lợi thế.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **68. Chi phí kỳ vọng và chi phí thực tế** nối từ **67. Phân tích chi phí giao dịch** sang **69. Xác suất khớp và lựa chọn bất lợi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 68. Chi phí kỳ vọng và chi phí thực tế

Mô hình nên dự báo chi phí chênh lệch, trượt giá và tác động. Phân phối chi phí thực tế phải được so lại thường xuyên.

Chi phí xấu đi kéo dài có thể báo hiệu chiến lược bị đông người dùng, vượt công suất hoặc cấu trúc thị trường đã thay đổi.

> **Nối mạch:** Ở chặng này của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **69. Xác suất khớp và lựa chọn bất lợi** nối từ **68. Chi phí kỳ vọng và chi phí thực tế** sang **70. Theo dõi công suất**, vì cơ chế trước tạo đầu vào cho bước sau.

## 69. Xác suất khớp và lựa chọn bất lợi

Không nên chỉ tối ưu tỷ lệ khớp. Tỷ lệ khớp cao nhưng giá đi ngược ngay sau khớp có thể là dấu hiệu lựa chọn bất lợi.

Cần xem cùng:

```text
Xác suất khớp
Mức cải thiện giá
Biến động sau khớp
Chi phí cơ hội
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **70. Theo dõi công suất** nối từ **69. Xác suất khớp và lựa chọn bất lợi** sang **71. Kết luận**, vì cơ chế trước tạo đầu vào cho bước sau.

## 70. Theo dõi công suất

Khi quy mô vốn tăng, hãy theo dõi:

- tỷ lệ tham gia;
- tác động giá;
- thời gian thoát;
- tỷ lệ không khớp;
- chi phí trên mỗi đơn vị lợi thế.

Nếu chi phí tăng nhanh hơn lợi nhuận gộp, chiến lược đã gần hoặc vượt công suất.

> **Nối mạch:** Trong **Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch**, **71. Kết luận** tổng hợp từ **70. Theo dõi công suất** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 71. Kết luận

Một chiến lược giao dịch thực tế phải sống được qua toàn chuỗi:

```text
Tín hiệu
→ Quy mô rủi ro
→ Lệnh
→ Khớp lệnh
→ Chi phí
→ Mức phơi nhiễm danh mục
→ Kiểm soát vận hành
→ Đối soát
→ Phân tích kết quả
```

Lợi thế không nằm riêng ở tín hiệu. Nó nằm ở khả năng bảo toàn giá trị của tín hiệu sau chi phí, thanh khoản, thực thi và các giới hạn vận hành.

> **Bàn giao:** Sau **71. Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
