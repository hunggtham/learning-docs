# Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Ý tưởng không phải chiến lược** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Giả thuyết nhân quả** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối systematic risk với backtest và execution, để chiến lược được đánh giá cả trong mô hình lịch sử lẫn chi phí giao dịch thật.

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

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **2. Giả thuyết nhân quả** nối từ **1. Ý tưởng không phải chiến lược** sang **3. Giả thuyết phải có khả năng bị bác bỏ**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **3. Giả thuyết phải có khả năng bị bác bỏ** nối từ **2. Giả thuyết nhân quả** sang **4. Dữ liệu đúng tại thời điểm lịch sử**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Giả thuyết phải có khả năng bị bác bỏ

Một giả thuyết tốt phải chỉ ra điều gì sẽ khiến nó không còn đúng.

Ví dụ:

```text
Nếu tín hiệu chỉ có lãi trước chi phí
hoặc mất hoàn toàn ngoài mẫu
→ giả thuyết cần xem lại
```

# Phần II — Dữ liệu

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **3. Giả thuyết phải có khả năng bị bác bỏ** đặt vấn đề; **4. Dữ liệu đúng tại thời điểm lịch sử** đối chiếu bằng chứng, rồi **5. Kiểm tra dấu thời gian** mở rộng hệ quả hoặc giới hạn liên quan.

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

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **4. Dữ liệu đúng tại thời điểm lịch sử** đặt vấn đề; **5. Kiểm tra dấu thời gian** đối chiếu bằng chứng, rồi **6. Chất lượng dữ liệu** mở rộng hệ quả hoặc giới hạn liên quan.

## 5. Kiểm tra dấu thời gian

Mỗi nguồn dữ liệu cần biết:

- múi giờ;
- độ trễ;
- thời điểm đóng nến;
- dấu thời gian của sở giao dịch;
- thời điểm công bố.

Sai vài phút có thể biến một chiến lược theo sự kiện từ thua thành thắng giả tạo.

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **5. Kiểm tra dấu thời gian** đặt vấn đề; **6. Chất lượng dữ liệu** đối chiếu bằng chứng, rồi **7. Thiên lệch nhìn trước** mở rộng hệ quả hoặc giới hạn liên quan.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **6. Chất lượng dữ liệu** đặt vấn đề; **7. Thiên lệch nhìn trước** đối chiếu bằng chứng, rồi **8. Thiên lệch sống sót** mở rộng hệ quả hoặc giới hạn liên quan.

## 7. Thiên lệch nhìn trước

Thiên lệch nhìn trước xuất hiện khi mô hình sử dụng thông tin tương lai trong quá khứ.

Ví dụ dùng giá đóng cửa của ngày để quyết định một lệnh được giả định xảy ra trước giờ đóng cửa.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **8. Thiên lệch sống sót** nối từ **7. Thiên lệch nhìn trước** sang **9. Thiên lệch lựa chọn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Thiên lệch sống sót

Sau khi xác định dữ liệu và universe, cần kiểm tra xem mẫu lịch sử có loại bỏ những tài sản thất bại hay không. Survivorship bias làm chiến lược trông bền hơn vì chỉ giữ lại các “người sống sót”.

**Thiên lệch sống sót (survivorship bias)** xảy ra khi chỉ dùng những tài sản còn tồn tại hôm nay cho dữ liệu lịch sử, bỏ các công ty phá sản hoặc bị hủy niêm yết.

Kết quả thường đẹp giả tạo.

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **9. Thiên lệch lựa chọn** nối từ **8. Thiên lệch sống sót** sang **10. Đào bới dữ liệu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Thiên lệch lựa chọn

Selection bias xảy ra khi ta chọn thị trường, giai đoạn hoặc tập tài sản vì đã biết nó phù hợp với rule. Cách chống là định nghĩa universe và khoảng thời gian trước khi xem kết quả.

**Thiên lệch lựa chọn (selection bias)** xuất hiện khi chọn thị trường hoặc giai đoạn vì đã biết trước nó phù hợp chiến lược.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **9. Thiên lệch lựa chọn** đặt vấn đề; **10. Đào bới dữ liệu** đối chiếu bằng chứng, rồi **11. Vấn đề thử nhiều giả thuyết** mở rộng hệ quả hoặc giới hạn liên quan.

## 10. Đào bới dữ liệu

Data snooping biến một kết quả đẹp trong nhiều thử nghiệm thành ảo giác bằng chứng. Mỗi thử nghiệm thêm vào làm tăng xác suất tìm thấy pattern ngẫu nhiên, nên cần ghi log và kiểm tra ngoài mẫu.

**Đào bới dữ liệu (data snooping)** là thử quá nhiều biến, quy tắc và khung thời gian rồi chỉ giữ kết quả đẹp nhất.

Càng thử nhiều, xác suất tìm được một mẫu ngẫu nhiên càng cao.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **10. Đào bới dữ liệu** đặt vấn đề; **11. Vấn đề thử nhiều giả thuyết** đối chiếu bằng chứng, rồi **12. Tập huấn luyện, xác thực và kiểm tra** mở rộng hệ quả hoặc giới hạn liên quan.

## 11. Vấn đề thử nhiều giả thuyết

Nếu thử hàng nghìn chiến lược, một số sẽ có Sharpe cao chỉ do may mắn.

Do đó phải ghi lại số lần thử và mức độ độc lập giữa các thử nghiệm.

# Phần IV — Chia dữ liệu

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **12. Tập huấn luyện, xác thực và kiểm tra** nối từ **11. Vấn đề thử nhiều giả thuyết** sang **13. Ngoài mẫu**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **13. Ngoài mẫu** nối từ **12. Tập huấn luyện, xác thực và kiểm tra** sang **14. Kiểm thử cuốn chiếu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Ngoài mẫu

OOS là phần dữ liệu được giữ lại để kiểm tra sau khi rule đã khóa. Mục tiêu là đo khả năng tổng quát hóa, không phải tiếp tục chỉnh tham số cho đến khi OOS cũng đẹp.

**Ngoài mẫu (out-of-sample, OOS)** là phần dữ liệu không dùng để xây quy tắc.

Kết quả OOS thường đáng tin hơn trong mẫu, dù vẫn có thể chịu may mắn thống kê.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **14. Kiểm thử cuốn chiếu** nối từ **13. Ngoài mẫu** sang **15. Loại vùng chồng lấn và tạo khoảng cách**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Kiểm thử cuốn chiếu

Walk-forward mô phỏng cách một hệ thống được cập nhật theo thời gian: train trên quá khứ, kiểm tra trên đoạn kế tiếp, rồi cuốn cửa sổ về phía trước. Nó nối nghiên cứu với môi trường thông tin thay đổi.

**Kiểm thử cuốn chiếu (walk-forward)** lặp quy trình:

```text
Huấn luyện trên quá khứ
→ kiểm tra đoạn tiếp theo
→ trượt cửa sổ
→ lặp lại
```

Cách này mô phỏng tốt hơn việc chiến lược được cập nhật theo thời gian thực.

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **15. Loại vùng chồng lấn và tạo khoảng cách** nối từ **14. Kiểm thử cuốn chiếu** sang **16. Kỳ vọng mỗi giao dịch**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Loại vùng chồng lấn và tạo khoảng cách

Khi nhãn hoặc giao dịch chồng lấn thời gian, tập huấn luyện và kiểm tra có thể rò rỉ thông tin.

**Loại mẫu chồng lấn (purging)** bỏ các quan sát gây giao thoa. **Khoảng cách an toàn (embargo)** tạo khoảng trống giữa hai tập.

Khái niệm này đặc biệt quan trọng với mô hình học máy dùng dữ liệu tài chính theo chuỗi thời gian.

# Phần V — Kỳ vọng và phân phối kết quả

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **16. Kỳ vọng mỗi giao dịch** nối từ **15. Loại vùng chồng lấn và tạo khoảng cách** sang **17. Bội số R**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Kỳ vọng mỗi giao dịch

Expectancy là phép tóm tắt phân phối thắng/thua sau khi định nghĩa rõ sample, cost và execution. Hãy đọc công thức như điểm bắt đầu để kiểm tra độ bền, không như dự báo từng lệnh.

```text
E
= P(thắng) × Lãi trung bình
- P(thua) × Lỗ trung bình
```

Kỳ vọng dương mới là nền tảng; tỷ lệ thắng cao không đủ.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **17. Bội số R** nối từ **16. Kỳ vọng mỗi giao dịch** sang **18. Phân phối quan trọng hơn trung bình**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Bội số R

R-multiple chuẩn hóa kết quả theo khoản lỗ ban đầu đã chấp nhận. Nhờ đó, các trade khác notional và stop có thể được so sánh trên cùng đơn vị rủi ro.

**Bội số R (R-multiple)** chuẩn hóa kết quả theo mức rủi ro ban đầu, giúp so sánh các giao dịch có quy mô khác nhau.

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **18. Phân phối quan trọng hơn trung bình** nối từ **17. Bội số R** sang **19. Mức suy giảm**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Phân phối quan trọng hơn trung bình

Hai chiến lược có cùng lợi suất trung bình nhưng có thể khác mạnh về:

- độ lệch phân phối;
- đuôi dày;
- mức suy giảm;
- thua lỗ theo cụm;
- rủi ro thanh khoản.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **19. Mức suy giảm** nối từ **18. Phân phối quan trọng hơn trung bình** sang **20. Không tìm “tham số thần kỳ”**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Mức suy giảm

Mức suy giảm tối đa lịch sử không phải tổn thất tệ nhất có thể xảy ra trong tương lai.

Cần xem thêm:

- thời gian nằm trong suy giảm;
- thời gian phục hồi;
- đường giá trị khi chưa trở lại đỉnh.

# Phần VI — Độ bền của tham số

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **20. Không tìm “tham số thần kỳ”** nối từ **19. Mức suy giảm** sang **21. Bề mặt tham số**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Không tìm “tham số thần kỳ”

Nếu chiến lược chỉ có lãi ở MA = 47 nhưng thua ở 45, 46, 48 và 49 thì lợi thế có thể rất mong manh.

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **21. Bề mặt tham số** nối từ **20. Không tìm “tham số thần kỳ”** sang **22. Độ ổn định qua nhiều thị trường**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Bề mặt tham số

Nên xem cả vùng tham số thay vì một điểm tối ưu. Một vùng rộng có kết quả tương đối ổn định thường đáng tin hơn một đỉnh hẹp.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **22. Độ ổn định qua nhiều thị trường** nối từ **21. Bề mặt tham số** sang **23. Độ ổn định qua nhiều chế độ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Độ ổn định qua nhiều thị trường

Nếu cùng lô-gic (logic / 논리) hoạt động ở nhiều thị trường liên quan, bằng chứng thường mạnh hơn trường hợp chỉ hoạt động ở một mã rất cụ thể.

Tuy nhiên không nên đòi hỏi lợi thế phải phổ quát nếu giả thuyết vốn chỉ phù hợp với một cấu trúc thị trường riêng.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **23. Độ ổn định qua nhiều chế độ** nối từ **22. Độ ổn định qua nhiều thị trường** sang **24. Kiểm tra giả**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **24. Kiểm tra giả** nối từ **23. Độ ổn định qua nhiều chế độ** sang **25. Điểm vào ngẫu nhiên**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Kiểm tra giả

Placebo test thay tín hiệu có ý nghĩa bằng tín hiệu ngẫu nhiên hoặc thời điểm dịch chuyển để kiểm tra liệu kết quả có còn xuất hiện mà không có cơ chế hay không. Nếu có, edge ban đầu có thể chỉ là artifact.

**Kiểm tra giả (placebo test)** thay tín hiệu thật bằng tín hiệu ngẫu nhiên hoặc dịch thời gian để xem kết quả còn tương tự không.

Nếu có, “lợi thế” có thể chỉ đến từ xu hướng chung của thị trường hoặc một thiên lệch dữ liệu.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **25. Điểm vào ngẫu nhiên** nối từ **24. Kiểm tra giả** sang **26. Đảo chiều tín hiệu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Điểm vào ngẫu nhiên

Giữ quy tắc thoát và quản trị rủi ro nhưng ngẫu nhiên hóa điểm vào giúp kiểm tra tín hiệu vào lệnh thật sự đóng góp bao nhiêu.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **26. Đảo chiều tín hiệu** nối từ **25. Điểm vào ngẫu nhiên** sang **27. Chênh lệch mua–bán**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Đảo chiều tín hiệu

Đảo tín hiệu giúp hiểu lợi thế đến từ hướng dự báo thật hay chỉ từ lớp quản trị rủi ro và thoát lệnh.

# Phần VIII — Mô hình chi phí

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **27. Chênh lệch mua–bán** nối từ **26. Đảo chiều tín hiệu** sang **28. Trượt giá**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Chênh lệch mua–bán

Chênh lệch mua–bán là chi phí trực tiếp giữa giá mua tốt nhất và giá bán tốt nhất. Kiểm thử dùng giá giữa hoặc giá đóng cửa mà bỏ qua chênh lệch thường quá lạc quan.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **28. Trượt giá** nối từ **27. Chênh lệch mua–bán** sang **29. Tác động của lệnh lên thị trường**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Trượt giá

Slippage nối backtest với giá khớp thật. Nó phụ thuộc thanh khoản, kích thước lệnh, thời điểm, loại lệnh và trạng thái thị trường; vì vậy không nên dùng một mức phí cố định cho mọi phiên.

**Trượt giá (slippage)** phụ thuộc:

- biến động;
- loại lệnh;
- quy mô;
- thanh khoản;
- độ trễ;
- rủi ro sự kiện.

Không nên dùng một con số trượt giá cố định cho mọi trạng thái thị trường.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **29. Tác động của lệnh lên thị trường** nối từ **28. Trượt giá** sang **30. Chi phí tài trợ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Tác động của lệnh lên thị trường

Lệnh lớn có thể tự làm giá đi ngược người giao dịch. **Công suất chiến lược (strategy capacity)** giảm khi quy mô tăng và chi phí tác động tăng.

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **30. Chi phí tài trợ** nối từ **29. Tác động của lệnh lên thị trường** sang **31. Chi phí vay chứng khoán và khả năng bán khống**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Chi phí tài trợ

CFD, giao dịch ký quỹ, bán khống và sản phẩm đòn bẩy có chi phí tài trợ. Chiến lược giữ lâu phải tính đầy đủ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **31. Chi phí vay chứng khoán và khả năng bán khống** nối từ **30. Chi phí tài trợ** sang **32. Chuyển kỳ hạn hợp đồng tương lai**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Chi phí vay chứng khoán và khả năng bán khống

Chiến lược bán khống phải tính:

- phí vay;
- khả năng tìm được chứng khoán để vay;
- rủi ro bị thu hồi;
- trạng thái khó vay.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **32. Chuyển kỳ hạn hợp đồng tương lai** nối từ **31. Chi phí vay chứng khoán và khả năng bán khống** sang **33. Lấy mẫu lại**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Chuyển kỳ hạn hợp đồng tương lai

Chiến lược futures cần mô hình hóa:

- ngày chuyển kỳ hạn;
- chênh lệch giữa hợp đồng;
- sự dịch chuyển thanh khoản;
- cơ sở giá;
- phí giao dịch.

# Phần IX — Bootstrap và Monte Carlo

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **33. Lấy mẫu lại** nối từ **32. Chuyển kỳ hạn hợp đồng tương lai** sang **34. Mô phỏng Monte Carlo**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Lấy mẫu lại

Bootstrap tạo nhiều đường kết quả từ mẫu lịch sử để nhìn uncertainty của expectancy và drawdown. Nó không tạo thêm thông tin độc lập và không sửa được sample bias hoặc regime chưa xuất hiện.

**Bootstrap** lấy mẫu lại từ giao dịch hoặc lợi suất lịch sử để tạo nhiều đường kết quả khả dĩ.

Mục tiêu là đánh giá bất định của lợi suất và mức suy giảm, thay vì chỉ nhìn một đường lịch sử.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **34. Mô phỏng Monte Carlo** nối từ **33. Lấy mẫu lại** sang **35. Kích thước mẫu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Mô phỏng Monte Carlo

Monte Carlo có thể ngẫu nhiên hóa:

- thứ tự giao dịch;
- độ lớn thắng/thua;
- chế độ biến động;
- bất định tham số.

Kết quả cần được đọc như phân phối xác suất, không phải một đường vốn “dự báo tương lai”.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **35. Kích thước mẫu** nối từ **34. Mô phỏng Monte Carlo** sang **36. Tự tương quan**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Kích thước mẫu

100 giao dịch không luôn tương đương 100 quan sát độc lập. Nếu phần lớn giao dịch xảy ra trong cùng một chế độ, **kích thước mẫu hiệu dụng (effective sample size)** nhỏ hơn nhiều.

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **36. Tự tương quan** nối từ **35. Kích thước mẫu** sang **37. Sharpe**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. Tự tương quan

Nếu lợi suất phụ thuộc vào chuỗi trước đó, giả định độc lập sẽ làm sai số chuẩn trông nhỏ giả tạo.

# Phần X — Thước đo hiệu quả

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **37. Sharpe** nối từ **36. Tự tương quan** sang **38. Sortino**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. Sharpe

Sharpe đặt excess return cạnh volatility, nhưng có thể đánh giá sai chiến lược có skew, fat tail hoặc mark-to-market không thường xuyên. Luôn đọc nó cùng drawdown, liquidity và cost.

```text
Sharpe
= Lợi suất vượt chuẩn / Độ biến động
```

Sharpe hữu ích nhưng không mô tả đầy đủ rủi ro đuôi hoặc thanh khoản.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **38. Sortino** nối từ **37. Sharpe** sang **39. Calmar**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Sortino

Sortino thay tổng độ biến động bằng độ lệch phía giảm, phù hợp khi quan tâm nhiều hơn tới biến động bất lợi.

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **39. Calmar** nối từ **38. Sortino** sang **40. Hệ số lợi nhuận**, vì cơ chế trước tạo đầu vào cho bước sau.

## 39. Calmar

Calmar so CAGR với maximum drawdown, nên gần với câu hỏi khả năng sống sót hơn Sharpe trong một số hệ thống. Tuy nhiên nó vẫn phụ thuộc cửa sổ quan sát và không mô tả đầy đủ tail risk tương lai.

```text
Calmar
≈ CAGR / Mức suy giảm tối đa
```

Thước đo này hữu ích với chiến lược có đường lợi nhuận kéo dài qua nhiều chu kỳ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **40. Hệ số lợi nhuận** nối từ **39. Calmar** sang **41. Tỷ lệ thắng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 40. Hệ số lợi nhuận

Profit factor so gross profit với gross loss. Chỉ số này cần được đặt cạnh số lượng trade, cost, drawdown và độ ổn định theo regime để tránh kết luận từ một mẫu nhỏ.

```text
Profit Factor
= Tổng lãi / Tổng lỗ tuyệt đối
```

Phải đọc cùng số giao dịch, độ tập trung lợi nhuận và chi phí.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **41. Tỷ lệ thắng** nối từ **40. Hệ số lợi nhuận** sang **42. Rủi ro cố định**, vì cơ chế trước tạo đầu vào cho bước sau.

## 41. Tỷ lệ thắng

Tỷ lệ thắng chỉ cho biết số giao dịch có lãi, không cho biết độ lớn lãi/lỗ. Không nên dùng riêng lẻ.

# Phần XI — Xác định quy mô vị thế

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **42. Rủi ro cố định** nối từ **41. Tỷ lệ thắng** sang **43. Điều chỉnh theo biến động**, vì cơ chế trước tạo đầu vào cho bước sau.

## 42. Rủi ro cố định

Một cách đơn giản là cho mỗi giao dịch một tỷ lệ rủi ro cố định theo điều kiện vô hiệu hóa.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **43. Điều chỉnh theo biến động** nối từ **42. Rủi ro cố định** sang **44. Kelly**, vì cơ chế trước tạo đầu vào cho bước sau.

## 43. Điều chỉnh theo biến động

Giảm quy mô khi biến động tăng giúp giữ mức rủi ro gần ổn định hơn.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **44. Kelly** nối từ **43. Điều chỉnh theo biến động** sang **45. Tổng nhiệt rủi ro của danh mục**, vì cơ chế trước tạo đầu vào cho bước sau.

## 44. Kelly

Tiêu chuẩn Kelly tối đa hóa tăng trưởng log dài hạn dưới giả định lợi thế được biết chính xác.

Trong thực tế thường dùng **Kelly phân số (fractional Kelly)** vì lợi thế chỉ được ước lượng và có sai số lớn.

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **45. Tổng nhiệt rủi ro của danh mục** nối từ **44. Kelly** sang **46. Công suất**, vì cơ chế trước tạo đầu vào cho bước sau.

## 45. Tổng nhiệt rủi ro của danh mục

Tổng rủi ro của nhiều vị thế có thể lớn hơn phép cộng cơ học nếu chúng phụ thuộc cùng một nhân tố.

# Phần XII — Công suất chiến lược

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **46. Công suất** nối từ **45. Tổng nhiệt rủi ro của danh mục** sang **47. Vòng quay**, vì cơ chế trước tạo đầu vào cho bước sau.

## 46. Công suất

Công suất là quy mô vốn có thể triển khai trước khi tác động giá và thiếu thanh khoản làm lợi thế giảm đáng kể.

Một chiến lược cổ phiếu vốn hóa rất nhỏ có Sharpe cao với 10.000 USD có thể không mở rộng được lên 10 triệu USD.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **47. Vòng quay** nối từ **46. Công suất** sang **48. Kiểm thử tiến tới tương lai**, vì cơ chế trước tạo đầu vào cho bước sau.

## 47. Vòng quay

Vòng quay cao làm chiến lược nhạy hơn với phí, trượt giá và chất lượng thực thi.

# Phần XIII — Kiểm thử tiến tới tương lai

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **48. Kiểm thử tiến tới tương lai** nối từ **47. Vòng quay** sang **49. Giao dịch thật với quy mô rất nhỏ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 48. Kiểm thử tiến tới tương lai

Forward test là bước kiểm tra hệ thống trong dữ liệu mới theo thời gian thật sau khi logic đã khóa. Nó giúp phát hiện drift, lỗi vận hành và chênh lệch giữa execution giả định với execution thực tế.

**Kiểm thử tiến tới tương lai (forward test)** chạy chiến lược trên dữ liệu mới theo thời gian thật nhưng chưa nhất thiết dùng vốn thật.

Nó giúp phát hiện:

- khác biệt dữ liệu;
- độ trễ;
- giả định thực thi sai;
- lỗi vận hành.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **49. Giao dịch thật với quy mô rất nhỏ** nối từ **48. Kiểm thử tiến tới tương lai** sang **50. Mã nghiên cứu và mã vận hành khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 49. Giao dịch thật với quy mô rất nhỏ

Sau kiểm thử tiến tới tương lai, quy mô thật rất nhỏ giúp thu thập dữ liệu về khớp lệnh và trượt giá trước khi tăng vốn.

# Phần XIV — Hệ thống vận hành thực tế

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **50. Mã nghiên cứu và mã vận hành khác nhau** nối từ **49. Giao dịch thật với quy mô rất nhỏ** sang **51. Đối soát**, vì cơ chế trước tạo đầu vào cho bước sau.

## 50. Mã nghiên cứu và mã vận hành khác nhau

Mã nghiên cứu có thể chấp nhận thao tác thủ công. Hệ thống vận hành cần:

- lô-gic (logic / 논리) xác định;
- nhật ký;
- cơ chế thử lại;
- giám sát;
- xử lý lỗi.

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **51. Đối soát** nối từ **50. Mã nghiên cứu và mã vận hành khác nhau** sang **52. Lệnh không tạo tác dụng lặp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 51. Đối soát

Hệ thống phải đối chiếu:

```text
Vị thế kỳ vọng
với
Vị thế thật tại nhà môi giới
```

Nếu khác nhau, cần dừng hoặc xử lý theo quy tắc rõ ràng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **52. Lệnh không tạo tác dụng lặp** nối từ **51. Đối soát** sang **53. Công tắc dừng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 52. Lệnh không tạo tác dụng lặp

Cơ chế **không lặp tác dụng (idempotency)** bảo đảm việc gửi lại cùng yêu cầu sau lỗi mạng không vô tình tạo vị thế gấp đôi.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **53. Công tắc dừng** nối từ **52. Lệnh không tạo tác dụng lặp** sang **54. Giới hạn an toàn nội bộ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 53. Công tắc dừng

Kill switch là điều kiện bảo vệ khi hệ thống lệch khỏi giả định an toàn: lỗi dữ liệu, lỗi lệnh, drawdown bất thường, exposure vượt giới hạn hoặc thị trường thay đổi trạng thái. Nó phải được viết trước khi có sự cố.

**Công tắc dừng (kill switch)** cho phép ngừng hệ thống khi:

- dữ liệu lỗi;
- API nhà môi giới lỗi;
- vị thế không khớp;
- lỗ vượt ngưỡng;
- thị trường bất thường.

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **53. Công tắc dừng** đặt tiêu chí; **54. Giới hạn an toàn nội bộ** dùng tiêu chí đó để kiểm tra ranh giới, rồi **55. Suy giảm lợi thế** mở rộng hệ quả.

## 54. Giới hạn an toàn nội bộ

Có thể đặt trước:

- lỗ tối đa trong ngày;
- phơi nhiễm tổng tối đa;
- đòn bẩy tối đa;
- kích thước lệnh tối đa;
- trượt giá tối đa.

# Phần XV — Trôi dữ liệu và suy giảm chiến lược

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **54. Giới hạn an toàn nội bộ** đặt tiêu chí; **55. Suy giảm lợi thế** dùng tiêu chí đó để kiểm tra ranh giới, rồi **56. Trôi phân phối đầu vào** mở rộng hệ quả.

## 55. Suy giảm lợi thế

Lợi thế có thể giảm vì:

- thị trường thích nghi;
- cạnh tranh;
- chi phí tăng;
- chế độ thay đổi;
- cách triển khai lệch khỏi nghiên cứu ban đầu.

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **56. Trôi phân phối đầu vào** nối từ **55. Suy giảm lợi thế** sang **57. Trôi hiệu quả**, vì cơ chế trước tạo đầu vào cho bước sau.

## 56. Trôi phân phối đầu vào

Feature drift xảy ra khi dữ liệu đầu vào hiện tại khác phân phối lúc xây mô hình. Khi drift làm thay đổi quan hệ giữa feature và outcome, cần giảm size, tái kiểm định hoặc dừng chiến lược thay vì giả định quá khứ còn đúng.

**Trôi đặc trưng (feature drift)** là khi phân phối đầu vào thay đổi so giai đoạn dùng để xây mô hình.

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **57. Trôi hiệu quả** nối từ **56. Trôi phân phối đầu vào** sang **58. Không dừng chiến lược chỉ vì vài lệnh thua**, vì cơ chế trước tạo đầu vào cho bước sau.

## 57. Trôi hiệu quả

Nên theo dõi:

- tỷ lệ thắng;
- kỳ vọng;
- trượt giá;
- vòng quay;
- phơi nhiễm nhân tố;
- mức suy giảm.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **58. Không dừng chiến lược chỉ vì vài lệnh thua** nối từ **57. Trôi hiệu quả** sang **59. Quản lý phiên bản**, vì cơ chế trước tạo đầu vào cho bước sau.

## 58. Không dừng chiến lược chỉ vì vài lệnh thua

Cần phân biệt biến động ngẫu nhiên bình thường với bằng chứng cho thấy lợi thế đã hỏng. Ngưỡng dừng nên được xác định trước, không dựa trên cảm xúc.

# Phần XVI — Nhật ký nghiên cứu và quản lý phiên bản

> **Nối mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **59. Quản lý phiên bản** nối từ **58. Không dừng chiến lược chỉ vì vài lệnh thua** sang **60. Không sửa lịch sử sau khi biết kết quả**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **60. Không sửa lịch sử sau khi biết kết quả** nối từ **59. Quản lý phiên bản** sang **61. Tách nghiên cứu và phê duyệt triển khai**, vì cơ chế trước tạo đầu vào cho bước sau.

## 60. Không sửa lịch sử sau khi biết kết quả

Nếu thay đổi mã rồi chạy lại toàn bộ lịch sử, phải coi đó là một chiến lược mới. Không được trình bày kết quả cũ như thể thay đổi đã tồn tại từ trước.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **61. Tách nghiên cứu và phê duyệt triển khai** nối từ **60. Không sửa lịch sử sau khi biết kết quả** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

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

> **Bàn giao:** Sau **61. Tách nghiên cứu và phê duyệt triển khai**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
