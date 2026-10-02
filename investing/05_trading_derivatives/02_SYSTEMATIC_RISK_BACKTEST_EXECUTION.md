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

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **2. Giả thuyết nhân quả** tiếp nhận điểm tựa từ **1. Ý tưởng không phải chiến lược** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Giả thuyết phải có khả năng bị bác bỏ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **3. Giả thuyết phải có khả năng bị bác bỏ** tiếp nhận điểm tựa từ **2. Giả thuyết nhân quả** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Dữ liệu đúng tại thời điểm lịch sử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Giả thuyết phải có khả năng bị bác bỏ

Một giả thuyết tốt phải chỉ ra điều gì sẽ khiến nó không còn đúng.

Ví dụ:

```text
Nếu tín hiệu chỉ có lãi trước chi phí
hoặc mất hoàn toàn ngoài mẫu
→ giả thuyết cần xem lại
```

# Phần II — Dữ liệu

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **3. Giả thuyết phải có khả năng bị bác bỏ** nêu điều cần giải thích; **4. Dữ liệu đúng tại thời điểm lịch sử** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. Kiểm tra dấu thời gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **4. Dữ liệu đúng tại thời điểm lịch sử** nêu điều cần giải thích; **5. Kiểm tra dấu thời gian** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. Chất lượng dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Kiểm tra dấu thời gian

Mỗi nguồn dữ liệu cần biết:

- múi giờ;
- độ trễ;
- thời điểm đóng nến;
- dấu thời gian của sở giao dịch;
- thời điểm công bố.

Sai vài phút có thể biến một chiến lược theo sự kiện từ thua thành thắng giả tạo.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **5. Kiểm tra dấu thời gian** nêu điều cần giải thích; **6. Chất lượng dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. Thiên lệch nhìn trước** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **6. Chất lượng dữ liệu** nêu điều cần giải thích; **7. Thiên lệch nhìn trước** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. Thiên lệch sống sót** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Thiên lệch nhìn trước

Thiên lệch nhìn trước xuất hiện khi mô hình sử dụng thông tin tương lai trong quá khứ.

Ví dụ dùng giá đóng cửa của ngày để quyết định một lệnh được giả định xảy ra trước giờ đóng cửa.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **8. Thiên lệch sống sót** tiếp nhận điểm tựa từ **7. Thiên lệch nhìn trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Thiên lệch lựa chọn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Thiên lệch sống sót

Sau khi xác định dữ liệu và universe, cần kiểm tra xem mẫu lịch sử có loại bỏ những tài sản thất bại hay không. Survivorship bias làm chiến lược trông bền hơn vì chỉ giữ lại các “người sống sót”.

**Thiên lệch sống sót (survivorship bias)** xảy ra khi chỉ dùng những tài sản còn tồn tại hôm nay cho dữ liệu lịch sử, bỏ các công ty phá sản hoặc bị hủy niêm yết.

Kết quả thường đẹp giả tạo.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **9. Thiên lệch lựa chọn** tiếp nhận điểm tựa từ **8. Thiên lệch sống sót** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Đào bới dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Thiên lệch lựa chọn

Selection bias xảy ra khi ta chọn thị trường, giai đoạn hoặc tập tài sản vì đã biết nó phù hợp với rule. Cách chống là định nghĩa universe và khoảng thời gian trước khi xem kết quả.

**Thiên lệch lựa chọn (selection bias)** xuất hiện khi chọn thị trường hoặc giai đoạn vì đã biết trước nó phù hợp chiến lược.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **9. Thiên lệch lựa chọn** nêu điều cần giải thích; **10. Đào bới dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. Vấn đề thử nhiều giả thuyết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Đào bới dữ liệu

Data snooping biến một kết quả đẹp trong nhiều thử nghiệm thành ảo giác bằng chứng. Mỗi thử nghiệm thêm vào làm tăng xác suất tìm thấy pattern ngẫu nhiên, nên cần ghi log và kiểm tra ngoài mẫu.

**Đào bới dữ liệu (data snooping)** là thử quá nhiều biến, quy tắc và khung thời gian rồi chỉ giữ kết quả đẹp nhất.

Càng thử nhiều, xác suất tìm được một mẫu ngẫu nhiên càng cao.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **10. Đào bới dữ liệu** nêu điều cần giải thích; **11. Vấn đề thử nhiều giả thuyết** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. Tập huấn luyện, xác thực và kiểm tra** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Vấn đề thử nhiều giả thuyết

Nếu thử hàng nghìn chiến lược, một số sẽ có Sharpe cao chỉ do may mắn.

Do đó phải ghi lại số lần thử và mức độ độc lập giữa các thử nghiệm.

# Phần IV — Chia dữ liệu

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **12. Tập huấn luyện, xác thực và kiểm tra** tiếp nhận điểm tựa từ **11. Vấn đề thử nhiều giả thuyết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Ngoài mẫu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **13. Ngoài mẫu** tiếp nhận điểm tựa từ **12. Tập huấn luyện, xác thực và kiểm tra** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Kiểm thử cuốn chiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Ngoài mẫu

OOS là phần dữ liệu được giữ lại để kiểm tra sau khi rule đã khóa. Mục tiêu là đo khả năng tổng quát hóa, không phải tiếp tục chỉnh tham số cho đến khi OOS cũng đẹp.

**Ngoài mẫu (out-of-sample, OOS)** là phần dữ liệu không dùng để xây quy tắc.

Kết quả OOS thường đáng tin hơn trong mẫu, dù vẫn có thể chịu may mắn thống kê.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **14. Kiểm thử cuốn chiếu** tiếp nhận điểm tựa từ **13. Ngoài mẫu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Loại vùng chồng lấn và tạo khoảng cách** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **15. Loại vùng chồng lấn và tạo khoảng cách** tiếp nhận điểm tựa từ **14. Kiểm thử cuốn chiếu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Kỳ vọng mỗi giao dịch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Loại vùng chồng lấn và tạo khoảng cách

Khi nhãn hoặc giao dịch chồng lấn thời gian, tập huấn luyện và kiểm tra có thể rò rỉ thông tin.

**Loại mẫu chồng lấn (purging)** bỏ các quan sát gây giao thoa. **Khoảng cách an toàn (embargo)** tạo khoảng trống giữa hai tập.

Khái niệm này đặc biệt quan trọng với mô hình học máy dùng dữ liệu tài chính theo chuỗi thời gian.

# Phần V — Kỳ vọng và phân phối kết quả

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **16. Kỳ vọng mỗi giao dịch** tiếp nhận điểm tựa từ **15. Loại vùng chồng lấn và tạo khoảng cách** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Bội số R** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Kỳ vọng mỗi giao dịch

Expectancy là phép tóm tắt phân phối thắng/thua sau khi định nghĩa rõ sample, cost và execution. Hãy đọc công thức như điểm bắt đầu để kiểm tra độ bền, không như dự báo từng lệnh.

```text
E
= P(thắng) × Lãi trung bình
- P(thua) × Lỗ trung bình
```

Kỳ vọng dương mới là nền tảng; tỷ lệ thắng cao không đủ.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **17. Bội số R** tiếp nhận điểm tựa từ **16. Kỳ vọng mỗi giao dịch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Phân phối quan trọng hơn trung bình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Bội số R

R-multiple chuẩn hóa kết quả theo khoản lỗ ban đầu đã chấp nhận. Nhờ đó, các trade khác notional và stop có thể được so sánh trên cùng đơn vị rủi ro.

**Bội số R (R-multiple)** chuẩn hóa kết quả theo mức rủi ro ban đầu, giúp so sánh các giao dịch có quy mô khác nhau.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **18. Phân phối quan trọng hơn trung bình** tiếp nhận điểm tựa từ **17. Bội số R** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Mức suy giảm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Phân phối quan trọng hơn trung bình

Hai chiến lược có cùng lợi suất trung bình nhưng có thể khác mạnh về:

- độ lệch phân phối;
- đuôi dày;
- mức suy giảm;
- thua lỗ theo cụm;
- rủi ro thanh khoản.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **19. Mức suy giảm** tiếp nhận điểm tựa từ **18. Phân phối quan trọng hơn trung bình** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Không tìm “tham số thần kỳ”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Mức suy giảm

Mức suy giảm tối đa lịch sử không phải tổn thất tệ nhất có thể xảy ra trong tương lai.

Cần xem thêm:

- thời gian nằm trong suy giảm;
- thời gian phục hồi;
- đường giá trị khi chưa trở lại đỉnh.

# Phần VI — Độ bền của tham số

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **20. Không tìm “tham số thần kỳ”** tiếp nhận điểm tựa từ **19. Mức suy giảm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Bề mặt tham số** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Không tìm “tham số thần kỳ”

Nếu chiến lược chỉ có lãi ở MA = 47 nhưng thua ở 45, 46, 48 và 49 thì lợi thế có thể rất mong manh.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **21. Bề mặt tham số** tiếp nhận điểm tựa từ **20. Không tìm “tham số thần kỳ”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Độ ổn định qua nhiều thị trường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Bề mặt tham số

Nên xem cả vùng tham số thay vì một điểm tối ưu. Một vùng rộng có kết quả tương đối ổn định thường đáng tin hơn một đỉnh hẹp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **22. Độ ổn định qua nhiều thị trường** tiếp nhận điểm tựa từ **21. Bề mặt tham số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Độ ổn định qua nhiều chế độ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Độ ổn định qua nhiều thị trường

Nếu cùng lô-gic (logic / 논리) hoạt động ở nhiều thị trường liên quan, bằng chứng thường mạnh hơn trường hợp chỉ hoạt động ở một mã rất cụ thể.

Tuy nhiên không nên đòi hỏi lợi thế phải phổ quát nếu giả thuyết vốn chỉ phù hợp với một cấu trúc thị trường riêng.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **23. Độ ổn định qua nhiều chế độ** tiếp nhận điểm tựa từ **22. Độ ổn định qua nhiều thị trường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Kiểm tra giả** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **24. Kiểm tra giả** tiếp nhận điểm tựa từ **23. Độ ổn định qua nhiều chế độ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Điểm vào ngẫu nhiên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Kiểm tra giả

Placebo test thay tín hiệu có ý nghĩa bằng tín hiệu ngẫu nhiên hoặc thời điểm dịch chuyển để kiểm tra liệu kết quả có còn xuất hiện mà không có cơ chế hay không. Nếu có, edge ban đầu có thể chỉ là artifact.

**Kiểm tra giả (placebo test)** thay tín hiệu thật bằng tín hiệu ngẫu nhiên hoặc dịch thời gian để xem kết quả còn tương tự không.

Nếu có, “lợi thế” có thể chỉ đến từ xu hướng chung của thị trường hoặc một thiên lệch dữ liệu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **25. Điểm vào ngẫu nhiên** tiếp nhận điểm tựa từ **24. Kiểm tra giả** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Đảo chiều tín hiệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Điểm vào ngẫu nhiên

Giữ quy tắc thoát và quản trị rủi ro nhưng ngẫu nhiên hóa điểm vào giúp kiểm tra tín hiệu vào lệnh thật sự đóng góp bao nhiêu.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **26. Đảo chiều tín hiệu** tiếp nhận điểm tựa từ **25. Điểm vào ngẫu nhiên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Chênh lệch mua–bán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Đảo chiều tín hiệu

Đảo tín hiệu giúp hiểu lợi thế đến từ hướng dự báo thật hay chỉ từ lớp quản trị rủi ro và thoát lệnh.

# Phần VIII — Mô hình chi phí

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **27. Chênh lệch mua–bán** tiếp nhận điểm tựa từ **26. Đảo chiều tín hiệu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Trượt giá** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Chênh lệch mua–bán

Chênh lệch mua–bán là chi phí trực tiếp giữa giá mua tốt nhất và giá bán tốt nhất. Kiểm thử dùng giá giữa hoặc giá đóng cửa mà bỏ qua chênh lệch thường quá lạc quan.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **28. Trượt giá** tiếp nhận điểm tựa từ **27. Chênh lệch mua–bán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Tác động của lệnh lên thị trường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **29. Tác động của lệnh lên thị trường** tiếp nhận điểm tựa từ **28. Trượt giá** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Chi phí tài trợ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Tác động của lệnh lên thị trường

Lệnh lớn có thể tự làm giá đi ngược người giao dịch. **Công suất chiến lược (strategy capacity)** giảm khi quy mô tăng và chi phí tác động tăng.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **30. Chi phí tài trợ** tiếp nhận điểm tựa từ **29. Tác động của lệnh lên thị trường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Chi phí vay chứng khoán và khả năng bán khống** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Chi phí tài trợ

CFD, giao dịch ký quỹ, bán khống và sản phẩm đòn bẩy có chi phí tài trợ. Chiến lược giữ lâu phải tính đầy đủ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **31. Chi phí vay chứng khoán và khả năng bán khống** tiếp nhận điểm tựa từ **30. Chi phí tài trợ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Chuyển kỳ hạn hợp đồng tương lai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Chi phí vay chứng khoán và khả năng bán khống

Chiến lược bán khống phải tính:

- phí vay;
- khả năng tìm được chứng khoán để vay;
- rủi ro bị thu hồi;
- trạng thái khó vay.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **32. Chuyển kỳ hạn hợp đồng tương lai** tiếp nhận điểm tựa từ **31. Chi phí vay chứng khoán và khả năng bán khống** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Lấy mẫu lại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Chuyển kỳ hạn hợp đồng tương lai

Chiến lược futures cần mô hình hóa:

- ngày chuyển kỳ hạn;
- chênh lệch giữa hợp đồng;
- sự dịch chuyển thanh khoản;
- cơ sở giá;
- phí giao dịch.

# Phần IX — Bootstrap và Monte Carlo

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **33. Lấy mẫu lại** tiếp nhận điểm tựa từ **32. Chuyển kỳ hạn hợp đồng tương lai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Mô phỏng Monte Carlo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Lấy mẫu lại

Bootstrap tạo nhiều đường kết quả từ mẫu lịch sử để nhìn uncertainty của expectancy và drawdown. Nó không tạo thêm thông tin độc lập và không sửa được sample bias hoặc regime chưa xuất hiện.

**Bootstrap** lấy mẫu lại từ giao dịch hoặc lợi suất lịch sử để tạo nhiều đường kết quả khả dĩ.

Mục tiêu là đánh giá bất định của lợi suất và mức suy giảm, thay vì chỉ nhìn một đường lịch sử.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **34. Mô phỏng Monte Carlo** tiếp nhận điểm tựa từ **33. Lấy mẫu lại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Kích thước mẫu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Mô phỏng Monte Carlo

Monte Carlo có thể ngẫu nhiên hóa:

- thứ tự giao dịch;
- độ lớn thắng/thua;
- chế độ biến động;
- bất định tham số.

Kết quả cần được đọc như phân phối xác suất, không phải một đường vốn “dự báo tương lai”.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **35. Kích thước mẫu** tiếp nhận điểm tựa từ **34. Mô phỏng Monte Carlo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Tự tương quan** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Kích thước mẫu

100 giao dịch không luôn tương đương 100 quan sát độc lập. Nếu phần lớn giao dịch xảy ra trong cùng một chế độ, **kích thước mẫu hiệu dụng (effective sample size)** nhỏ hơn nhiều.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **36. Tự tương quan** tiếp nhận điểm tựa từ **35. Kích thước mẫu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Sharpe** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Tự tương quan

Nếu lợi suất phụ thuộc vào chuỗi trước đó, giả định độc lập sẽ làm sai số chuẩn trông nhỏ giả tạo.

# Phần X — Thước đo hiệu quả

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **37. Sharpe** tiếp nhận điểm tựa từ **36. Tự tương quan** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Sortino** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Sharpe

Sharpe đặt excess return cạnh volatility, nhưng có thể đánh giá sai chiến lược có skew, fat tail hoặc mark-to-market không thường xuyên. Luôn đọc nó cùng drawdown, liquidity và cost.

```text
Sharpe
= Lợi suất vượt chuẩn / Độ biến động
```

Sharpe hữu ích nhưng không mô tả đầy đủ rủi ro đuôi hoặc thanh khoản.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **38. Sortino** tiếp nhận điểm tựa từ **37. Sharpe** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Calmar** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Sortino

Sortino thay tổng độ biến động bằng độ lệch phía giảm, phù hợp khi quan tâm nhiều hơn tới biến động bất lợi.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **39. Calmar** tiếp nhận điểm tựa từ **38. Sortino** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Hệ số lợi nhuận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Calmar

Calmar so CAGR với maximum drawdown, nên gần với câu hỏi khả năng sống sót hơn Sharpe trong một số hệ thống. Tuy nhiên nó vẫn phụ thuộc cửa sổ quan sát và không mô tả đầy đủ tail risk tương lai.

```text
Calmar
≈ CAGR / Mức suy giảm tối đa
```

Thước đo này hữu ích với chiến lược có đường lợi nhuận kéo dài qua nhiều chu kỳ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **40. Hệ số lợi nhuận** tiếp nhận điểm tựa từ **39. Calmar** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Tỷ lệ thắng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Hệ số lợi nhuận

Profit factor so gross profit với gross loss. Chỉ số này cần được đặt cạnh số lượng trade, cost, drawdown và độ ổn định theo regime để tránh kết luận từ một mẫu nhỏ.

```text
Profit Factor
= Tổng lãi / Tổng lỗ tuyệt đối
```

Phải đọc cùng số giao dịch, độ tập trung lợi nhuận và chi phí.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **41. Tỷ lệ thắng** tiếp nhận điểm tựa từ **40. Hệ số lợi nhuận** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Rủi ro cố định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Tỷ lệ thắng

Tỷ lệ thắng chỉ cho biết số giao dịch có lãi, không cho biết độ lớn lãi/lỗ. Không nên dùng riêng lẻ.

# Phần XI — Xác định quy mô vị thế

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **42. Rủi ro cố định** tiếp nhận điểm tựa từ **41. Tỷ lệ thắng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Điều chỉnh theo biến động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Rủi ro cố định

Một cách đơn giản là cho mỗi giao dịch một tỷ lệ rủi ro cố định theo điều kiện vô hiệu hóa.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **43. Điều chỉnh theo biến động** tiếp nhận điểm tựa từ **42. Rủi ro cố định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Kelly** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Điều chỉnh theo biến động

Giảm quy mô khi biến động tăng giúp giữ mức rủi ro gần ổn định hơn.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **44. Kelly** tiếp nhận điểm tựa từ **43. Điều chỉnh theo biến động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. Tổng nhiệt rủi ro của danh mục** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Kelly

Tiêu chuẩn Kelly tối đa hóa tăng trưởng log dài hạn dưới giả định lợi thế được biết chính xác.

Trong thực tế thường dùng **Kelly phân số (fractional Kelly)** vì lợi thế chỉ được ước lượng và có sai số lớn.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **45. Tổng nhiệt rủi ro của danh mục** tiếp nhận điểm tựa từ **44. Kelly** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. Công suất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. Tổng nhiệt rủi ro của danh mục

Tổng rủi ro của nhiều vị thế có thể lớn hơn phép cộng cơ học nếu chúng phụ thuộc cùng một nhân tố.

# Phần XII — Công suất chiến lược

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **46. Công suất** tiếp nhận điểm tựa từ **45. Tổng nhiệt rủi ro của danh mục** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. Vòng quay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Công suất

Công suất là quy mô vốn có thể triển khai trước khi tác động giá và thiếu thanh khoản làm lợi thế giảm đáng kể.

Một chiến lược cổ phiếu vốn hóa rất nhỏ có Sharpe cao với 10.000 USD có thể không mở rộng được lên 10 triệu USD.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **47. Vòng quay** tiếp nhận điểm tựa từ **46. Công suất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. Kiểm thử tiến tới tương lai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Vòng quay

Vòng quay cao làm chiến lược nhạy hơn với phí, trượt giá và chất lượng thực thi.

# Phần XIII — Kiểm thử tiến tới tương lai

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **48. Kiểm thử tiến tới tương lai** tiếp nhận điểm tựa từ **47. Vòng quay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Giao dịch thật với quy mô rất nhỏ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. Kiểm thử tiến tới tương lai

Forward test là bước kiểm tra hệ thống trong dữ liệu mới theo thời gian thật sau khi logic đã khóa. Nó giúp phát hiện drift, lỗi vận hành và chênh lệch giữa execution giả định với execution thực tế.

**Kiểm thử tiến tới tương lai (forward test)** chạy chiến lược trên dữ liệu mới theo thời gian thật nhưng chưa nhất thiết dùng vốn thật.

Nó giúp phát hiện:

- khác biệt dữ liệu;
- độ trễ;
- giả định thực thi sai;
- lỗi vận hành.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **49. Giao dịch thật với quy mô rất nhỏ** tiếp nhận điểm tựa từ **48. Kiểm thử tiến tới tương lai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. Mã nghiên cứu và mã vận hành khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Giao dịch thật với quy mô rất nhỏ

Sau kiểm thử tiến tới tương lai, quy mô thật rất nhỏ giúp thu thập dữ liệu về khớp lệnh và trượt giá trước khi tăng vốn.

# Phần XIV — Hệ thống vận hành thực tế

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **50. Mã nghiên cứu và mã vận hành khác nhau** tiếp nhận điểm tựa từ **49. Giao dịch thật với quy mô rất nhỏ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. Đối soát** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. Mã nghiên cứu và mã vận hành khác nhau

Mã nghiên cứu có thể chấp nhận thao tác thủ công. Hệ thống vận hành cần:

- lô-gic (logic / 논리) xác định;
- nhật ký;
- cơ chế thử lại;
- giám sát;
- xử lý lỗi.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **51. Đối soát** tiếp nhận điểm tựa từ **50. Mã nghiên cứu và mã vận hành khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **52. Lệnh không tạo tác dụng lặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 51. Đối soát

Hệ thống phải đối chiếu:

```text
Vị thế kỳ vọng
với
Vị thế thật tại nhà môi giới
```

Nếu khác nhau, cần dừng hoặc xử lý theo quy tắc rõ ràng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **52. Lệnh không tạo tác dụng lặp** tiếp nhận điểm tựa từ **51. Đối soát** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **53. Công tắc dừng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 52. Lệnh không tạo tác dụng lặp

Cơ chế **không lặp tác dụng (idempotency)** bảo đảm việc gửi lại cùng yêu cầu sau lỗi mạng không vô tình tạo vị thế gấp đôi.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **53. Công tắc dừng** tiếp nhận điểm tựa từ **52. Lệnh không tạo tác dụng lặp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **54. Giới hạn an toàn nội bộ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. Công tắc dừng

Kill switch là điều kiện bảo vệ khi hệ thống lệch khỏi giả định an toàn: lỗi dữ liệu, lỗi lệnh, drawdown bất thường, exposure vượt giới hạn hoặc thị trường thay đổi trạng thái. Nó phải được viết trước khi có sự cố.

**Công tắc dừng (kill switch)** cho phép ngừng hệ thống khi:

- dữ liệu lỗi;
- API nhà môi giới lỗi;
- vị thế không khớp;
- lỗ vượt ngưỡng;
- thị trường bất thường.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **53. Công tắc dừng** đã nêu tiêu chí phân biệt, còn **54. Giới hạn an toàn nội bộ** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **55. Suy giảm lợi thế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 54. Giới hạn an toàn nội bộ

Có thể đặt trước:

- lỗ tối đa trong ngày;
- phơi nhiễm tổng tối đa;
- đòn bẩy tối đa;
- kích thước lệnh tối đa;
- trượt giá tối đa.

# Phần XV — Trôi dữ liệu và suy giảm chiến lược

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **54. Giới hạn an toàn nội bộ** đã nêu tiêu chí phân biệt, còn **55. Suy giảm lợi thế** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **56. Trôi phân phối đầu vào** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 55. Suy giảm lợi thế

Lợi thế có thể giảm vì:

- thị trường thích nghi;
- cạnh tranh;
- chi phí tăng;
- chế độ thay đổi;
- cách triển khai lệch khỏi nghiên cứu ban đầu.

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **56. Trôi phân phối đầu vào** tiếp nhận điểm tựa từ **55. Suy giảm lợi thế** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **57. Trôi hiệu quả** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 56. Trôi phân phối đầu vào

Feature drift xảy ra khi dữ liệu đầu vào hiện tại khác phân phối lúc xây mô hình. Khi drift làm thay đổi quan hệ giữa feature và outcome, cần giảm size, tái kiểm định hoặc dừng chiến lược thay vì giả định quá khứ còn đúng.

**Trôi đặc trưng (feature drift)** là khi phân phối đầu vào thay đổi so giai đoạn dùng để xây mô hình.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **57. Trôi hiệu quả** tiếp nhận điểm tựa từ **56. Trôi phân phối đầu vào** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **58. Không dừng chiến lược chỉ vì vài lệnh thua** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 57. Trôi hiệu quả

Nên theo dõi:

- tỷ lệ thắng;
- kỳ vọng;
- trượt giá;
- vòng quay;
- phơi nhiễm nhân tố;
- mức suy giảm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **58. Không dừng chiến lược chỉ vì vài lệnh thua** tiếp nhận điểm tựa từ **57. Trôi hiệu quả** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **59. Quản lý phiên bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 58. Không dừng chiến lược chỉ vì vài lệnh thua

Cần phân biệt biến động ngẫu nhiên bình thường với bằng chứng cho thấy lợi thế đã hỏng. Ngưỡng dừng nên được xác định trước, không dựa trên cảm xúc.

# Phần XVI — Nhật ký nghiên cứu và quản lý phiên bản

> **Chuyển mạch:** Trong **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **59. Quản lý phiên bản** tiếp nhận điểm tựa từ **58. Không dừng chiến lược chỉ vì vài lệnh thua** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **60. Không sửa lịch sử sau khi biết kết quả** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **60. Không sửa lịch sử sau khi biết kết quả** tiếp nhận điểm tựa từ **59. Quản lý phiên bản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **61. Tách nghiên cứu và phê duyệt triển khai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 60. Không sửa lịch sử sau khi biết kết quả

Nếu thay đổi mã rồi chạy lại toàn bộ lịch sử, phải coi đó là một chiến lược mới. Không được trình bày kết quả cũ như thể thay đổi đã tồn tại từ trước.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu hệ thống, kiểm thử quá khứ, rủi ro và triển khai thực tế**, **61. Tách nghiên cứu và phê duyệt triển khai** tiếp nhận điểm tựa từ **60. Không sửa lịch sử sau khi biết kết quả** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

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
