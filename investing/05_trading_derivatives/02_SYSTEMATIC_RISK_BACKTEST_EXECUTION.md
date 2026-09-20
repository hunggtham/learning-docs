# Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế

> Một ý tưởng giao dịch chỉ trở thành chiến lược khi được chuyển thành quy tắc rõ ràng, kiểm thử bằng dữ liệu đúng thời điểm, tính đủ chi phí giao dịch và vẫn hoạt động ngoài mẫu. Chương này dùng tiếng Việt làm ngôn ngữ giải thích; thuật ngữ tiếng Anh chỉ giữ trong ngoặc hoặc dưới dạng viết tắt chuẩn để tiện tra cứu.

# Phần I — Bắt đầu từ giả thuyết

## 1. Ý tưởng không phải chiến lược

“Giá thường bật lại sau khi quét thanh khoản” chỉ là một quan sát.

Muốn biến thành chiến lược cần xác định:

```text
Tập tài sản (universe)
Khung thời gian
Tín hiệu
Điểm vào
Điểm ra
Mức dừng
Quy mô vị thế
Mô hình chi phí
Điều kiện vô hiệu hóa
```

Nếu quy tắc chưa đủ rõ để hai người triển khai độc lập cho kết quả gần giống nhau, hệ thống vẫn quá mơ hồ.

## 2. Giả thuyết nhân quả

Một chiến lược tốt nên có lý do tại sao lợi thế có thể tồn tại.

Nguồn lợi thế có thể đến từ:

- phần bù rủi ro;
- thiên lệch hành vi;
- giới hạn của tổ chức lớn;
- nhu cầu thanh khoản;
- thông tin lan truyền chậm;
- cấu trúc thị trường.

Không phải mọi lợi thế cần một mô hình kinh tế hoàn hảo, nhưng câu chuyện nhân quả giúp giảm nguy cơ khai thác ngẫu nhiên dữ liệu.

## 3. Giả thuyết phải có khả năng bị bác bỏ

Một giả thuyết tốt phải chỉ ra điều gì sẽ khiến nó không còn đúng.

Ví dụ:

```text
Nếu tín hiệu chỉ có lãi trước chi phí
hoặc mất hoàn toàn ngoài mẫu
→ giả thuyết cần xem lại
```

# Phần II — Dữ liệu

## 4. Dữ liệu đúng tại thời điểm lịch sử

Dữ liệu dùng trong kiểm thử phải là dữ liệu **có thể biết tại thời điểm quyết định**.

Cần phân biệt:

```text
Thời điểm quan sát
Thời điểm công bố
Thời điểm chỉnh sửa dữ liệu
Thời điểm ra quyết định
Thời điểm thực thi
```

Dùng dữ liệu đã được sửa sau này cho quyết định trong quá khứ tạo **thiên lệch nhìn trước (look-ahead bias)**.

## 5. Kiểm tra dấu thời gian

Mỗi nguồn dữ liệu cần biết:

- múi giờ;
- độ trễ;
- thời điểm đóng nến;
- dấu thời gian của sở giao dịch;
- thời điểm công bố.

Sai vài phút có thể biến một chiến lược theo sự kiện từ thua thành thắng giả tạo.

## 6. Chất lượng dữ liệu

Cần kiểm tra:

- giá trị thiếu;
- bản ghi trùng;
- điểm dữ liệu lỗi;
- hành động doanh nghiệp;
- chuyển kỳ hạn hợp đồng tương lai;
- chứng khoán bị hủy niêm yết;
- thay đổi múi giờ.

Kiểm thử tốt bắt đầu từ dữ liệu sạch, không phải từ chỉ báo phức tạp.

# Phần III — Các thiên lệch phổ biến

## 7. Thiên lệch nhìn trước

Thiên lệch nhìn trước xuất hiện khi mô hình sử dụng thông tin tương lai trong quá khứ.

Ví dụ dùng giá đóng cửa của ngày để quyết định một lệnh được giả định xảy ra trước giờ đóng cửa.

## 8. Thiên lệch sống sót

**Thiên lệch sống sót (survivorship bias)** xảy ra khi chỉ dùng những tài sản còn tồn tại hôm nay cho dữ liệu lịch sử, bỏ các công ty phá sản hoặc bị hủy niêm yết.

Kết quả thường đẹp giả tạo.

## 9. Thiên lệch lựa chọn

**Thiên lệch lựa chọn (selection bias)** xuất hiện khi chọn thị trường hoặc giai đoạn vì đã biết trước nó phù hợp chiến lược.

## 10. Đào bới dữ liệu

**Đào bới dữ liệu (data snooping)** là thử quá nhiều biến, quy tắc và khung thời gian rồi chỉ giữ kết quả đẹp nhất.

Càng thử nhiều, xác suất tìm được một mẫu ngẫu nhiên càng cao.

## 11. Vấn đề thử nhiều giả thuyết

Nếu thử hàng nghìn chiến lược, một số sẽ có Sharpe cao chỉ do may mắn.

Do đó phải ghi lại số lần thử và mức độ độc lập giữa các thử nghiệm.

# Phần IV — Chia dữ liệu

## 12. Tập huấn luyện, xác thực và kiểm tra

Một cấu trúc phổ biến:

```text
Huấn luyện (train)
→ xây / hiệu chỉnh mô hình

Xác thực (validation)
→ chọn phiên bản

Kiểm tra (test)
→ đánh giá cuối ngoài mẫu
```

Không nên liên tục nhìn tập kiểm tra rồi sửa chiến lược, vì khi đó tập kiểm tra đã bị dùng như dữ liệu huấn luyện.

## 13. Ngoài mẫu

**Ngoài mẫu (out-of-sample, OOS)** là phần dữ liệu không dùng để xây quy tắc.

Kết quả OOS thường đáng tin hơn trong mẫu, dù vẫn có thể chịu may mắn thống kê.

## 14. Kiểm thử cuốn chiếu

**Kiểm thử cuốn chiếu (walk-forward)** lặp quy trình:

```text
Huấn luyện trên quá khứ
→ kiểm tra đoạn tiếp theo
→ trượt cửa sổ
→ lặp lại
```

Cách này mô phỏng tốt hơn việc chiến lược được cập nhật theo thời gian thực.

## 15. Loại vùng chồng lấn và tạo khoảng cách

Khi nhãn hoặc giao dịch chồng lấn thời gian, tập huấn luyện và kiểm tra có thể rò rỉ thông tin.

**Loại mẫu chồng lấn (purging)** bỏ các quan sát gây giao thoa. **Khoảng cách an toàn (embargo)** tạo khoảng trống giữa hai tập.

Khái niệm này đặc biệt quan trọng với mô hình học máy dùng dữ liệu tài chính theo chuỗi thời gian.

# Phần V — Kỳ vọng và phân phối kết quả

## 16. Kỳ vọng mỗi giao dịch

```text
E
= P(thắng) × Lãi trung bình
- P(thua) × Lỗ trung bình
```

Kỳ vọng dương mới là nền tảng; tỷ lệ thắng cao không đủ.

## 17. Bội số R

**Bội số R (R-multiple)** chuẩn hóa kết quả theo mức rủi ro ban đầu, giúp so sánh các giao dịch có quy mô khác nhau.

## 18. Phân phối quan trọng hơn trung bình

Hai chiến lược có cùng lợi suất trung bình nhưng có thể khác mạnh về:

- độ lệch phân phối;
- đuôi dày;
- mức suy giảm;
- thua lỗ theo cụm;
- rủi ro thanh khoản.

## 19. Mức suy giảm

Mức suy giảm tối đa lịch sử không phải tổn thất tệ nhất có thể xảy ra trong tương lai.

Cần xem thêm:

- thời gian nằm trong suy giảm;
- thời gian phục hồi;
- đường giá trị khi chưa trở lại đỉnh.

# Phần VI — Độ bền của tham số

## 20. Không tìm “tham số thần kỳ”

Nếu chiến lược chỉ có lãi ở MA = 47 nhưng thua ở 45, 46, 48 và 49 thì lợi thế có thể rất mong manh.

## 21. Bề mặt tham số

Nên xem cả vùng tham số thay vì một điểm tối ưu. Một vùng rộng có kết quả tương đối ổn định thường đáng tin hơn một đỉnh hẹp.

## 22. Độ ổn định qua nhiều thị trường

Nếu cùng logic hoạt động ở nhiều thị trường liên quan, bằng chứng thường mạnh hơn trường hợp chỉ hoạt động ở một mã rất cụ thể.

Tuy nhiên không nên đòi hỏi lợi thế phải phổ quát nếu giả thuyết vốn chỉ phù hợp với một cấu trúc thị trường riêng.

## 23. Độ ổn định qua nhiều chế độ

Nên kiểm tra ít nhất:

- xu hướng;
- đi ngang;
- biến động cao;
- biến động thấp;
- khủng hoảng;
- nới lỏng và thắt chặt.

Chiến lược có thể hợp lệ nhưng chỉ trong một chế độ; điều quan trọng là biết giới hạn đó.

# Phần VII — Kiểm tra giả và kiểm tra bác bỏ

## 24. Kiểm tra giả

**Kiểm tra giả (placebo test)** thay tín hiệu thật bằng tín hiệu ngẫu nhiên hoặc dịch thời gian để xem kết quả còn tương tự không.

Nếu có, “lợi thế” có thể chỉ đến từ xu hướng chung của thị trường hoặc một thiên lệch dữ liệu.

## 25. Điểm vào ngẫu nhiên

Giữ quy tắc thoát và quản trị rủi ro nhưng ngẫu nhiên hóa điểm vào giúp kiểm tra tín hiệu vào lệnh thật sự đóng góp bao nhiêu.

## 26. Đảo chiều tín hiệu

Đảo tín hiệu giúp hiểu lợi thế đến từ hướng dự báo thật hay chỉ từ lớp quản trị rủi ro và thoát lệnh.

# Phần VIII — Mô hình chi phí

## 27. Chênh lệch mua–bán

Chênh lệch mua–bán là chi phí trực tiếp giữa giá mua tốt nhất và giá bán tốt nhất. Kiểm thử dùng giá giữa hoặc giá đóng cửa mà bỏ qua chênh lệch thường quá lạc quan.

## 28. Trượt giá

**Trượt giá (slippage)** phụ thuộc:

- biến động;
- loại lệnh;
- quy mô;
- thanh khoản;
- độ trễ;
- rủi ro sự kiện.

Không nên dùng một con số trượt giá cố định cho mọi trạng thái thị trường.

## 29. Tác động của lệnh lên thị trường

Lệnh lớn có thể tự làm giá đi ngược người giao dịch. **Công suất chiến lược (strategy capacity)** giảm khi quy mô tăng và chi phí tác động tăng.

## 30. Chi phí tài trợ

CFD, giao dịch ký quỹ, bán khống và sản phẩm đòn bẩy có chi phí tài trợ. Chiến lược giữ lâu phải tính đầy đủ.

## 31. Chi phí vay chứng khoán và khả năng bán khống

Chiến lược bán khống phải tính:

- phí vay;
- khả năng tìm được chứng khoán để vay;
- rủi ro bị thu hồi;
- trạng thái khó vay.

## 32. Chuyển kỳ hạn hợp đồng tương lai

Chiến lược futures cần mô hình hóa:

- ngày chuyển kỳ hạn;
- chênh lệch giữa hợp đồng;
- sự dịch chuyển thanh khoản;
- cơ sở giá;
- phí giao dịch.

# Phần IX — Bootstrap và Monte Carlo

## 33. Lấy mẫu lại

**Bootstrap** lấy mẫu lại từ giao dịch hoặc lợi suất lịch sử để tạo nhiều đường kết quả khả dĩ.

Mục tiêu là đánh giá bất định của lợi suất và mức suy giảm, thay vì chỉ nhìn một đường lịch sử.

## 34. Mô phỏng Monte Carlo

Monte Carlo có thể ngẫu nhiên hóa:

- thứ tự giao dịch;
- độ lớn thắng/thua;
- chế độ biến động;
- bất định tham số.

Kết quả cần được đọc như phân phối xác suất, không phải một đường vốn “dự báo tương lai”.

## 35. Kích thước mẫu

100 giao dịch không luôn tương đương 100 quan sát độc lập. Nếu phần lớn giao dịch xảy ra trong cùng một chế độ, **kích thước mẫu hiệu dụng (effective sample size)** nhỏ hơn nhiều.

## 36. Tự tương quan

Nếu lợi suất phụ thuộc vào chuỗi trước đó, giả định độc lập sẽ làm sai số chuẩn trông nhỏ giả tạo.

# Phần X — Thước đo hiệu quả

## 37. Sharpe

```text
Sharpe
= Lợi suất vượt chuẩn / Độ biến động
```

Sharpe hữu ích nhưng không mô tả đầy đủ rủi ro đuôi hoặc thanh khoản.

## 38. Sortino

Sortino thay tổng độ biến động bằng độ lệch phía giảm, phù hợp khi quan tâm nhiều hơn tới biến động bất lợi.

## 39. Calmar

```text
Calmar
≈ CAGR / Mức suy giảm tối đa
```

Thước đo này hữu ích với chiến lược có đường lợi nhuận kéo dài qua nhiều chu kỳ.

## 40. Hệ số lợi nhuận

```text
Profit Factor
= Tổng lãi / Tổng lỗ tuyệt đối
```

Phải đọc cùng số giao dịch, độ tập trung lợi nhuận và chi phí.

## 41. Tỷ lệ thắng

Tỷ lệ thắng chỉ cho biết số giao dịch có lãi, không cho biết độ lớn lãi/lỗ. Không nên dùng riêng lẻ.

# Phần XI — Xác định quy mô vị thế

## 42. Rủi ro cố định

Một cách đơn giản là cho mỗi giao dịch một tỷ lệ rủi ro cố định theo điều kiện vô hiệu hóa.

## 43. Điều chỉnh theo biến động

Giảm quy mô khi biến động tăng giúp giữ mức rủi ro gần ổn định hơn.

## 44. Kelly

Tiêu chuẩn Kelly tối đa hóa tăng trưởng log dài hạn dưới giả định lợi thế được biết chính xác.

Trong thực tế thường dùng **Kelly phân số (fractional Kelly)** vì lợi thế chỉ được ước lượng và có sai số lớn.

## 45. Tổng nhiệt rủi ro của danh mục

Tổng rủi ro của nhiều vị thế có thể lớn hơn phép cộng cơ học nếu chúng phụ thuộc cùng một nhân tố.

# Phần XII — Công suất chiến lược

## 46. Công suất

Công suất là quy mô vốn có thể triển khai trước khi tác động giá và thiếu thanh khoản làm lợi thế giảm đáng kể.

Một chiến lược cổ phiếu vốn hóa rất nhỏ có Sharpe cao với 10.000 USD có thể không mở rộng được lên 10 triệu USD.

## 47. Vòng quay

Vòng quay cao làm chiến lược nhạy hơn với phí, trượt giá và chất lượng thực thi.

# Phần XIII — Kiểm thử tiến tới tương lai

## 48. Kiểm thử tiến tới tương lai

**Kiểm thử tiến tới tương lai (forward test)** chạy chiến lược trên dữ liệu mới theo thời gian thật nhưng chưa nhất thiết dùng vốn thật.

Nó giúp phát hiện:

- khác biệt dữ liệu;
- độ trễ;
- giả định thực thi sai;
- lỗi vận hành.

## 49. Giao dịch thật với quy mô rất nhỏ

Sau kiểm thử tiến tới tương lai, quy mô thật rất nhỏ giúp thu thập dữ liệu về khớp lệnh và trượt giá trước khi tăng vốn.

# Phần XIV — Hệ thống vận hành thực tế

## 50. Mã nghiên cứu và mã vận hành khác nhau

Mã nghiên cứu có thể chấp nhận thao tác thủ công. Hệ thống vận hành cần:

- logic xác định;
- nhật ký;
- cơ chế thử lại;
- giám sát;
- xử lý lỗi.

## 51. Đối soát

Hệ thống phải đối chiếu:

```text
Vị thế kỳ vọng
với
Vị thế thật tại nhà môi giới
```

Nếu khác nhau, cần dừng hoặc xử lý theo quy tắc rõ ràng.

## 52. Lệnh không tạo tác dụng lặp

Cơ chế **không lặp tác dụng (idempotency)** bảo đảm việc gửi lại cùng yêu cầu sau lỗi mạng không vô tình tạo vị thế gấp đôi.

## 53. Công tắc dừng

**Công tắc dừng (kill switch)** cho phép ngừng hệ thống khi:

- dữ liệu lỗi;
- API nhà môi giới lỗi;
- vị thế không khớp;
- lỗ vượt ngưỡng;
- thị trường bất thường.

## 54. Giới hạn an toàn nội bộ

Có thể đặt trước:

- lỗ tối đa trong ngày;
- phơi nhiễm tổng tối đa;
- đòn bẩy tối đa;
- kích thước lệnh tối đa;
- trượt giá tối đa.

# Phần XV — Trôi dữ liệu và suy giảm chiến lược

## 55. Suy giảm lợi thế

Lợi thế có thể giảm vì:

- thị trường thích nghi;
- cạnh tranh;
- chi phí tăng;
- chế độ thay đổi;
- cách triển khai lệch khỏi nghiên cứu ban đầu.

## 56. Trôi phân phối đầu vào

**Trôi đặc trưng (feature drift)** là khi phân phối đầu vào thay đổi so giai đoạn dùng để xây mô hình.

## 57. Trôi hiệu quả

Nên theo dõi:

- tỷ lệ thắng;
- kỳ vọng;
- trượt giá;
- vòng quay;
- phơi nhiễm nhân tố;
- mức suy giảm.

## 58. Không dừng chiến lược chỉ vì vài lệnh thua

Cần phân biệt biến động ngẫu nhiên bình thường với bằng chứng cho thấy lợi thế đã hỏng. Ngưỡng dừng nên được xác định trước, không dựa trên cảm xúc.

# Phần XVI — Nhật ký nghiên cứu và quản lý phiên bản

## 59. Quản lý phiên bản

Mỗi thay đổi chiến lược nên ghi:

```text
Phiên bản
Ngày
Giả thuyết
Thay đổi quy tắc
Lý do
Ảnh hưởng kỳ vọng
Kết quả xác thực
```

## 60. Không sửa lịch sử sau khi biết kết quả

Nếu thay đổi mã rồi chạy lại toàn bộ lịch sử, phải coi đó là một chiến lược mới. Không được trình bày kết quả cũ như thể thay đổi đã tồn tại từ trước.

## 61. Tách nghiên cứu và phê duyệt triển khai

Một quy trình tốt nên có cổng rõ:

```text
Ý tưởng
→ nghiên cứu
→ xác thực
→ kiểm tra chi phí
→ kiểm thử tiến tới tương lai
→ vốn thật nhỏ
→ phê duyệt tăng quy mô
```

# Phần XVII — Kết luận

Một quy trình hệ thống tốt không tối ưu một chỉ số duy nhất. Nó phải chịu được:

```text
Sai số dữ liệu
→ sai số mô hình
→ thay đổi chế độ
→ chi phí giao dịch
→ giới hạn thanh khoản
→ lỗi vận hành
```

Lợi thế thật là lợi thế còn tồn tại sau toàn bộ chuỗi đó, không phải đường kiểm thử đẹp nhất.