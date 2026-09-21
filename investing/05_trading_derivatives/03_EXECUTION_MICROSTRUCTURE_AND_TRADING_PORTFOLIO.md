# Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch

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

## 2. Giá quyết định và giá thực thi

**Giá quyết định (decision price)** là mức giá khi chiến lược quyết định giao dịch.

**Giá thực thi (execution price)** là mức giá khớp thật.

Khoảng cách giữa hai mức có thể đến từ:

- chênh lệch mua–bán (spread);
- độ trễ (latency);
- tác động của chính lệnh lên giá (market impact);
- thời gian chờ;
- lệnh không khớp;
- biến động thị trường trong lúc thực thi.

Đây là nền tảng của **mức thiếu hụt do thực thi (implementation shortfall)**.

# Phần II — Sổ lệnh giới hạn

## 3. Sổ lệnh

**Sổ lệnh giới hạn (limit order book)** chứa các lệnh mua và bán đang chờ theo từng mức giá.

```text
Giá mua tốt nhất = best bid
Giá bán tốt nhất = best ask
Chênh lệch = best ask - best bid
```

**Độ sâu (depth)** cho biết khối lượng có sẵn ở nhiều mức giá. Chênh lệch hẹp nhưng độ sâu rất mỏng vẫn có thể gây trượt giá lớn cho lệnh lớn.

## 4. Ưu tiên giá–thời gian

Nhiều sở giao dịch dùng nguyên tắc gần với **ưu tiên giá–thời gian (price-time priority)**:

```text
Giá tốt hơn được ưu tiên trước
→ nếu cùng giá, lệnh vào trước thường được ưu tiên trước
```

Do đó kiểm thử giả định “giá chạm lệnh giới hạn = chắc chắn khớp” thường quá lạc quan.

## 5. Vị trí trong hàng chờ

**Vị trí hàng chờ (queue position)** ảnh hưởng xác suất khớp. Nó phụ thuộc:

- khối lượng lệnh đang đứng trước;
- lệnh bị hủy;
- lệnh thị trường mới đi vào;
- quy tắc của nơi giao dịch;
- thời gian chờ.

Với chiến lược rất ngắn hạn, mô hình hàng chờ có thể quan trọng gần ngang chất lượng tín hiệu.

## 6. Bên cung cấp và bên lấy thanh khoản

**Bên cung cấp thanh khoản (maker)** thường đặt lệnh chờ. **Bên lấy thanh khoản (taker)** giao dịch chủ động với lệnh đang có sẵn.

Bên cung cấp thanh khoản có thể tiết kiệm chênh lệch nhưng chịu:

- rủi ro không khớp;
- lựa chọn bất lợi (adverse selection);
- chi phí cơ hội.

Bên lấy thanh khoản có khả năng khớp nhanh hơn nhưng trả chênh lệch và có thể gây tác động giá.

# Phần III — Các loại lệnh

## 7. Lệnh thị trường

**Lệnh thị trường (market order)** ưu tiên khả năng được khớp, không bảo đảm mức giá chính xác.

Trong thị trường mỏng hoặc khi có tin lớn, giá khớp có thể xa mức nhìn thấy trước khi gửi lệnh.

## 8. Lệnh giới hạn có thể khớp ngay

**Lệnh giới hạn chủ động (marketable limit order)** đi qua chênh lệch hiện tại nhưng vẫn đặt giới hạn cho mức giá tệ nhất chấp nhận được.

Nó giảm nguy cơ khớp cực xấu nhưng có thể chỉ khớp một phần trong thị trường chạy nhanh.

## 9. Lệnh giới hạn thụ động

**Lệnh giới hạn thụ động (passive limit order)** kiểm soát giá nhưng có thể không khớp.

Một vấn đề quan trọng là **lựa chọn bất lợi (adverse selection)**: lệnh có thể được khớp nhiều nhất đúng lúc giá sắp tiếp tục đi ngược vị thế.

## 10. Lệnh dừng

Lệnh dừng (stop order) chỉ kích hoạt sau khi đạt điều kiện. Giá kích hoạt không phải giá khớp được bảo đảm.

Khoảng nhảy giá có thể biến kế hoạch `-1R` thành tổn thất lớn hơn đáng kể.

## 11. Lệnh dừng–giới hạn

Lệnh dừng–giới hạn (stop-limit) kiểm soát mức giá tệ nhất nhưng có nguy cơ không thoát được nếu thị trường chạy qua vùng giới hạn quá nhanh.

Vì vậy nó không tự động an toàn hơn lệnh dừng thị trường.

## 12. Thời hạn hiệu lực của lệnh

Một số quy ước phổ biến:

- DAY;
- GTC;
- IOC;
- FOK.

**Thời hạn hiệu lực (time-in-force)** là một phần của logic thực thi, không chỉ là tùy chọn giao diện.

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

## 14. Giao dịch nhiều chân

Spread quyền chọn hoặc cấu trúc phòng vệ nhiều chân có thể giao dịch dưới dạng gói hoặc từng chân.

Thực thi từng chân tạo **rủi ro lệch chân (legging risk)**: chân đầu đã khớp nhưng chân sau di chuyển khỏi mức giá dự kiến.

# Phần IV — Chênh lệch mua–bán và thanh khoản

## 15. Vì sao chênh lệch tồn tại?

Chênh lệch mua–bán bù cho nhà cung cấp thanh khoản các rủi ro như:

- lựa chọn bất lợi;
- rủi ro tồn kho;
- biến động;
- sử dụng vốn;
- phí của nơi giao dịch.

Khi bất định tăng, chênh lệch thường rộng hơn.

## 16. Chênh lệch niêm yết và chênh lệch hiệu dụng

**Chênh lệch niêm yết (quoted spread)** là khoảng bid–ask đang hiển thị.

**Chênh lệch hiệu dụng (effective spread)** đo chi phí khớp thực tế so với điểm giữa hoặc mức tham chiếu.

Khớp được giá tốt hơn có thể làm chi phí thấp hơn chênh lệch niêm yết; thị trường biến động nhanh có thể làm chi phí cao hơn.

## 17. Chênh lệch thực giữ được

**Chênh lệch thực giữ được (realized spread)** đo phần chênh lệch còn lại sau một khoảng thời gian, giúp tách:

```text
Thu nhập từ chênh lệch
và
Tổn thất do lựa chọn bất lợi
```

## 18. Thanh khoản là khái niệm nhiều chiều

Cần nhìn cùng:

- chênh lệch;
- độ sâu;
- khả năng hồi phục của sổ lệnh;
- giá trị giao dịch;
- tác động giá;
- số ngày cần để thoát vị thế.

Khối lượng cao không bảo đảm một lệnh lớn có thể thoát với chi phí thấp.

## 19. Thanh khoản ẩn và lệnh iceberg

Một số lệnh chỉ hiển thị một phần khối lượng. Vì vậy độ sâu nhìn thấy có thể thấp hơn thanh khoản thật.

Ngược lại, thanh khoản đang hiển thị cũng có thể biến mất nhanh; ảnh chụp sổ lệnh không phải cam kết.

## 20. Nơi giao dịch không hiển thị trước lệnh

**Dark pool** hoặc nơi giao dịch ngoài sở có thể giảm khả năng lệnh lớn tự tiết lộ ý định trước giao dịch, nhưng làm quá trình khám phá giá và đánh giá chất lượng thực thi phức tạp hơn.

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

## 22. Khám phá giá

**Khám phá giá (price discovery)** là quá trình thông tin mới được phản ánh vào giá.

Tùy thị trường, thông tin có thể xuất hiện trước ở hợp đồng tương lai, ETF, quyền chọn, FX hoặc thị trường cơ sở.

Không nên dùng giá tham chiếu đã cũ như thể đó là giá trị hợp lý hiện tại.

## 23. Đấu giá mở cửa

Đấu giá mở cửa gom thông tin qua đêm và lệnh chờ. Kiểm thử “mua tại giá mở cửa” phải mô hình hóa khoảng nhảy giá và cơ chế đấu giá thực tế.

## 24. Đấu giá đóng cửa

Đấu giá đóng cửa thường có khối lượng lớn do:

- quỹ chỉ số;
- danh mục bám chuẩn;
- tái cân bằng;
- dòng lệnh tổ chức.

Giá đóng cửa chính thức không có nghĩa mọi nhà giao dịch đều có thể khớp đúng mức đó.

## 25. Mẫu hình trong ngày

Khối lượng và biến động thường có mẫu hình theo thời gian trong ngày. Cổ phiếu thường sôi động hơn đầu/cuối phiên; FX chịu ảnh hưởng các phiên châu Á, London và New York.

Mô hình chi phí nên phản ánh thời điểm giao dịch.

# Phần VI — Trượt giá và tác động thị trường

## 26. Trượt giá

**Trượt giá (slippage)** là chênh lệch giữa giá kỳ vọng và giá thực thi.

Nó phụ thuộc:

- biến động;
- mức khẩn cấp;
- kích thước lệnh so với độ sâu;
- độ trễ;
- loại lệnh;
- rủi ro sự kiện.

Không nên dùng một con số trượt giá cố định cho mọi chế độ thị trường.

## 27. Mức thiếu hụt do thực thi

**Mức thiếu hụt do thực thi (implementation shortfall)** đo khoảng cách giữa kết quả giả định nếu giao dịch được thực hiện tại giá quyết định và kết quả thật sau thực thi.

Có thể phân rã thành:

```text
Phí
+ chênh lệch mua–bán
+ chi phí trì hoãn
+ tác động thị trường
+ chi phí cơ hội
```

## 28. Chi phí cơ hội

Một lệnh thụ động không khớp có thể không mất phí nhưng vẫn tạo chi phí nếu bỏ lỡ một biến động có lợi.

“Không giao dịch được” cũng là một dạng chi phí thực thi.

## 29. Tác động thị trường

Chính lệnh của bạn có thể làm giá di chuyển. Tác động thường tăng khi:

- lệnh lớn so với thanh khoản;
- độ sâu thấp;
- yêu cầu hoàn tất nhanh;
- biến động cao.

**Công suất chiến lược (strategy capacity)** bị giới hạn bởi tác động thị trường, không chỉ bởi số dư tài khoản.

## 30. Tác động tạm thời và tác động lâu dài

Tác động tạm thời có thể hồi lại sau khi lệnh hoàn tất. Tác động lâu dài phản ánh thông tin hoặc tín hiệu từ lệnh đã được thị trường hấp thụ.

Thực thi tốt cố giảm phần tác động không cần thiết.

## 31. Tỷ lệ tham gia

```text
Tỷ lệ tham gia
= Khối lượng của mình / Khối lượng thị trường
```

Tỷ lệ cao giúp hoàn tất nhanh hơn nhưng thường làm tăng tác động giá và rủi ro tiết lộ ý định.

## 32. Công suất chiến lược

Công suất trả lời câu hỏi:

> Có thể triển khai bao nhiêu vốn trước khi chi phí ăn hết lợi thế?

Cần xem vòng quay, giá trị giao dịch trung bình, thời gian nắm giữ, tỷ lệ tham gia và kịch bản thoát khi căng thẳng.

# Phần VII — Thuật toán thực thi

## 33. TWAP

TWAP chia lệnh tương đối đều theo thời gian. Cách này đơn giản nhưng không thích nghi tốt khi thanh khoản trong ngày thay đổi mạnh.

## 34. VWAP

VWAP phân bổ lệnh theo hồ sơ khối lượng dự kiến hoặc thực tế. Đánh bại VWAP chỉ cho biết chất lượng thực thi so với chuẩn đó, không chứng minh quyết định đầu tư ban đầu là đúng.

## 35. POV

**Tỷ lệ theo khối lượng (Percentage-of-Volume, POV)** duy trì một tỷ lệ giao dịch gần cố định so với khối lượng thị trường. Nó thích nghi với mức độ hoạt động nhưng có thể giao dịch nhiều hơn đúng lúc biến động tăng.

## 36. Thuật toán tối ưu mức thiếu hụt do thực thi

Loại thuật toán này cân bằng:

```text
Tác động giá nếu giao dịch nhanh
với
Rủi ro giá nếu chờ lâu
```

Mức khẩn cấp cao thường dẫn tới thực thi nhiều hơn ở đầu khoảng thời gian.

## 37. Giá tại thời điểm bắt đầu

**Giá lúc bắt đầu thực thi (arrival price)** là mức giá khi quá trình thực thi được khởi động và thường phù hợp với chiến lược có tín hiệu mất giá trị nhanh.

Chuẩn so sánh phải được chọn trước khi nhìn kết quả.

## 38. Định tuyến lệnh thông minh

**Định tuyến lệnh thông minh (Smart Order Routing, SOR)** chọn nơi giao dịch dựa trên giá, phí, hàng chờ, độ trễ và xác suất khớp.

Mục tiêu là chất lượng khớp thực tế tốt hơn, không chỉ giá hiển thị tốt hơn.

# Phần VIII — Lựa chọn bất lợi và chất lượng dòng lệnh

## 39. Lựa chọn bất lợi

Một lệnh thụ động có thể chỉ được khớp khi phía đối diện có lợi thế thông tin hoặc khi giá sắp di chuyển ngược vị thế.

Do đó “kiếm chênh lệch” chưa chắc tạo lợi nhuận thực.

## 40. Dòng lệnh bất lợi

Nhà cung cấp thanh khoản đôi khi gọi **dòng lệnh độc (toxic flow)** là dòng lệnh thường xuất hiện ngay trước biến động giá bất lợi cho họ.

Đây là vấn đề thông tin và thời điểm, không nên mặc định diễn giải thành thao túng.

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

## 42. Giao dịch quanh sự kiện

CPI, NFP, FOMC, báo cáo lợi nhuận hoặc địa chính trị có thể làm:

- chênh lệch tăng;
- độ sâu giảm;
- trượt giá tăng;
- lệnh dừng bị nhảy qua;
- biến động hàm ý của quyền chọn thay đổi mạnh.

Chiến lược không được thiết kế cho điều kiện sự kiện nên có quy tắc giảm quy mô hoặc tránh giao dịch.

## 43. Rủi ro nhảy giá

**Rủi ro nhảy giá (gap risk)** xuất hiện khi giá thay đổi rời rạc và đi qua mức dừng mà không giao dịch tại mọi mức trung gian.

Mô hình rủi ro phải tính những bước nhảy này thay vì giả định đường giá liên tục.

## 44. Ngắt giao dịch

Cơ chế ngắt giao dịch (circuit breaker) hoặc tạm dừng chỉ ngăn giao dịch trong thời gian nhất định; nó không xóa rủi ro. Khi mở lại, giá vẫn có thể nhảy tiếp.

## 45. Biên độ giá hằng ngày

Ở thị trường có biên độ, vị thế có thể bị kẹt nhiều phiên nếu không có thanh khoản đối ứng. Quy mô vị thế phải tính cả kịch bản thoát qua nhiều phiên.

# Phần X — Hệ thống và độ an toàn vận hành

## 46. Độ trễ

Độ trễ chỉ quan trọng so với thời hạn của chiến lược. Với giao dịch theo ngày hoặc tuần, vài trăm mili giây thường không quyết định; với chênh lệch giá dưới giây, nó có thể là yếu tố sống còn.

## 47. Đồng bộ thời gian

Dữ liệu thị trường, tín hiệu, lệnh và khớp lệnh cần cùng chuẩn thời gian. Nếu đồng hồ sai, việc so sánh mô phỏng với giao dịch thật trở nên thiếu tin cậy.

## 48. Chất lượng dữ liệu

Giá cũ, dữ liệu mất, điểm dữ liệu lỗi hoặc điều chỉnh hành động doanh nghiệp sai có thể tạo tín hiệu giả.

Hệ thống thực tế cần kiểm tra đầu vào và có hành vi an toàn khi dữ liệu bất thường.

## 49. Trạng thái tại nhà môi giới

Thông báo “đã gửi lệnh” không có nghĩa lệnh đã khớp. Nếu kết nối mất, hệ thống phải hỏi lại trạng thái thật trước khi gửi lại.

## 50. Tính không lặp tác dụng

**Tính bất biến khi gửi lại (idempotency)** giúp tránh tạo lệnh trùng khi hệ thống thử lại sau lỗi mạng. Mã định danh lệnh phía khách hàng là công cụ quan trọng.

## 51. Đối soát

Vị thế, tiền mặt và lệnh đang mở trong hệ thống nội bộ phải được đối soát với nhà môi giới sau mất kết nối hoặc khởi động lại.

Trạng thái tại nhà môi giới hoặc sở giao dịch mới là nguồn sự thật của mức phơi nhiễm thật.

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

## 53. Tổng rủi ro dự kiến của các vị thế

Tổng các mức lỗ dừng dự kiến không thể chỉ cộng cơ học nếu nhiều vị thế cùng phụ thuộc một nhân tố.

Năm giao dịch đều cược USD giảm có thể cùng thất bại dù mỗi giao dịch chỉ chiếm 0,5% rủi ro danh nghĩa.

## 54. Phơi nhiễm ròng và tổng

Danh mục long–short có beta ròng gần 0 nhưng vẫn có đòn bẩy tổng rất lớn.

Phơi nhiễm tổng quyết định nhu cầu nguồn vốn, vòng quay, thanh khoản và rủi ro nhảy giá. Cần theo dõi cả ròng lẫn tổng.

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

## 56. Phơi nhiễm tương đương Delta

Danh mục quyền chọn cần quy đổi theo Delta và theo dõi thêm Gamma, Vega. Phí quyền chọn nhỏ không có nghĩa mức phơi nhiễm kinh tế nhỏ.

## 57. DV01 và rủi ro lãi suất

Với trái phiếu và lãi suất, nên cộng gộp DV01 và DV01 theo điểm kỳ hạn. Bù trừ giá trị danh nghĩa có thể che một cược đường cong lớn.

## 58. Rủi ro biến động

Bán quyền chọn, chiến lược carry và một số chiến lược hồi quy về trung bình có thể đều đang bán biến động dù dùng công cụ khác nhau.

Biến động nên được xem như một nhóm rủi ro riêng.

## 59. Rủi ro thanh khoản

Cổ phiếu nhỏ, tín dụng lợi suất cao, tài sản số ít thanh khoản và hợp đồng tương lai đông người cùng vị thế có thể cùng mất thanh khoản khi nguồn vốn căng.

Tương quan thanh khoản thường tăng trong khủng hoảng.

## 60. Tương quan không ổn định

Tương quan lịch sử có thể thay đổi mạnh theo chế độ và thường tăng khi hệ thống giảm đòn bẩy. Cần dùng thêm kịch bản căng thẳng thay vì chỉ ma trận tương quan quá khứ.

## 61. Nhắm mục tiêu độ biến động

Nhắm mục tiêu độ biến động điều chỉnh quy mô vị thế để giữ rủi ro kỳ vọng ổn định hơn.

Điểm yếu là tính thuận chu kỳ: biến động thấp khuyến khích tăng vị thế trước cú sốc; biến động cao buộc giảm vị thế sau khi giá đã giảm.

## 62. Phân bổ ngang bằng rủi ro giữa giao dịch

Cân bằng đóng góp độ biến động giúp tránh một thị trường thống trị toàn bộ danh mục, nhưng “cùng độ biến động” không có nghĩa cùng rủi ro đuôi. Cần điều chỉnh thêm cho nhảy giá, thanh khoản và tính phi tuyến.

## 63. VaR và Expected Shortfall

VaR ước lượng ngưỡng tổn thất ở mức tin cậy nhất định. Expected Shortfall ước lượng tổn thất trung bình sau khi đã vượt ngưỡng đó.

Cả hai vẫn phụ thuộc dữ liệu và mô hình; kiểm thử kịch bản không thể bỏ qua.

## 64. Kiểm soát mức suy giảm

Quy tắc giảm rủi ro khi mức suy giảm tăng phải được định nghĩa trước, dựa trên phân phối của chiến lược và khả năng mô hình bị hỏng, không dựa trên cảm xúc trong thời điểm thua lỗ.

# Phần XII — Phân tích chi phí giao dịch và vòng học

## 65. MAE và MFE

MAE/MFE giúp nghiên cứu đường đi của giao dịch trong thời gian nắm giữ. Chúng hữu ích cho chẩn đoán nhưng không nên được dùng để tối ưu lệnh dừng trên cùng một mẫu dữ liệu rồi coi kết quả là chắc chắn.

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

## 67. Phân tích chi phí giao dịch

**Phân tích chi phí giao dịch (Transaction Cost Analysis, TCA)** phân nhóm lệnh theo:

- chuẩn so sánh;
- nơi giao dịch;
- loại lệnh;
- kích thước;
- thời gian;
- biến động;
- thanh khoản.

Mục tiêu là phát hiện có hệ thống nơi chiến lược đang mất lợi thế.

## 68. Chi phí kỳ vọng và chi phí thực tế

Mô hình nên dự báo chi phí chênh lệch, trượt giá và tác động. Phân phối chi phí thực tế phải được so lại thường xuyên.

Chi phí xấu đi kéo dài có thể báo hiệu chiến lược bị đông người dùng, vượt công suất hoặc cấu trúc thị trường đã thay đổi.

## 69. Xác suất khớp và lựa chọn bất lợi

Không nên chỉ tối ưu tỷ lệ khớp. Tỷ lệ khớp cao nhưng giá đi ngược ngay sau khớp có thể là dấu hiệu lựa chọn bất lợi.

Cần xem cùng:

```text
Xác suất khớp
Mức cải thiện giá
Biến động sau khớp
Chi phí cơ hội
```

## 70. Theo dõi công suất

Khi quy mô vốn tăng, hãy theo dõi:

- tỷ lệ tham gia;
- tác động giá;
- thời gian thoát;
- tỷ lệ không khớp;
- chi phí trên mỗi đơn vị lợi thế.

Nếu chi phí tăng nhanh hơn lợi nhuận gộp, chiến lược đã gần hoặc vượt công suất.

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