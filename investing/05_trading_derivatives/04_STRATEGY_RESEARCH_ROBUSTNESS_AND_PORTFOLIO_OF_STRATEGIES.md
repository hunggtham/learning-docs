# Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Ý tưởng chưa phải chiến lược** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Bắt đầu bằng giả thuyết** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối strategy research với robustness và portfolio of strategies, để một ý tưởng chỉ được dùng khi vượt qua sensitivity và correlation.

> Một chiến lược đẹp trong kiểm thử quá khứ chưa đủ. Câu hỏi quan trọng hơn là: lợi thế có thật không, có tồn tại ngoài mẫu không, có còn dương sau chi phí không và nhiều chiến lược trong cùng danh mục có thật sự đa dạng hay chỉ lặp lại cùng một nhân tố? Nội dung giải thích dùng tiếng Việt; thuật ngữ tiếng Anh chỉ giữ trong ngoặc hoặc dưới dạng viết tắt chuẩn.

# Phần I — Từ ý tưởng tới chiến lược có thể kiểm chứng

## 1. Ý tưởng chưa phải chiến lược

Một nhận định như “giá thường hồi sau trạng thái quá bán” chỉ là ý tưởng.

Chiến lược phải chỉ rõ:

```text
Tập tài sản
Tín hiệu
Điểm vào
Điểm ra
Quy mô vị thế
Chi phí
Giới hạn rủi ro
Điều kiện vô hiệu hóa
```

Nếu hai người đọc mô tả rồi triển khai ra hai hệ thống khác nhau đáng kể, quy tắc vẫn chưa đủ rõ.

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **2. Bắt đầu bằng giả thuyết** tiếp nhận điểm tựa từ **1. Ý tưởng chưa phải chiến lược** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Cố gắng bác bỏ giả thuyết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Bắt đầu bằng giả thuyết

Giả thuyết nên giải thích vì sao lợi thế có thể tồn tại, ví dụ:

- phần bù rủi ro;
- thiên lệch hành vi;
- nhu cầu thanh khoản;
- giới hạn của tổ chức lớn;
- thông tin lan truyền chậm;
- cấu trúc thị trường.

Có một cơ chế hợp lý giúp giảm nguy cơ chỉ tìm thấy mẫu ngẫu nhiên sau khi nhìn dữ liệu.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **3. Cố gắng bác bỏ giả thuyết** tiếp nhận điểm tựa từ **2. Bắt đầu bằng giả thuyết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Dữ liệu trong mẫu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Cố gắng bác bỏ giả thuyết

Một quy trình nghiên cứu tốt phải chủ động tìm bằng chứng chống lại chính giả thuyết của mình.

Ví dụ:

```text
Nếu lợi thế biến mất khi thêm chi phí hợp lý
hoặc không tồn tại ngoài mẫu
→ giả thuyết chưa đủ mạnh
```

# Phần II — Trong mẫu và ngoài mẫu

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **3. Cố gắng bác bỏ giả thuyết** nêu điều cần giải thích; **4. Dữ liệu trong mẫu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. Dữ liệu ngoài mẫu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Dữ liệu trong mẫu

In-sample là nơi hình thành rule và ước lượng tham số, nhưng cũng là nơi overfit dễ nhất. Hãy xem kết quả trong mẫu như bằng chứng để xây giả thuyết, không phải xác nhận cuối cùng.

**Trong mẫu (in-sample)** là dữ liệu dùng để xây hoặc điều chỉnh chiến lược. Kết quả đẹp ở đây dễ bị khớp quá mức nhất.

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **4. Dữ liệu trong mẫu** nêu điều cần giải thích; **5. Dữ liệu ngoài mẫu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. Kiểm thử cuốn chiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Dữ liệu ngoài mẫu

OOS giữ lại một đoạn dữ liệu chưa từng dùng để thiết kế chiến lược. Nó kiểm tra khả năng tổng quát hóa sau khi quy tắc đã khóa, nên không được dùng để tiếp tục “sửa cho đẹp”.

**Ngoài mẫu (out-of-sample, OOS)** là dữ liệu chưa dùng để thiết kế quy tắc.

Nếu lợi thế giữ được ngoài mẫu, bằng chứng mạnh hơn nhưng vẫn không bảo đảm tương lai.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **5. Dữ liệu ngoài mẫu** nêu điều cần giải thích; **6. Kiểm thử cuốn chiếu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. Thiên lệch nhìn trước** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Kiểm thử cuốn chiếu

Walk-forward nối train/test theo thời gian và mô phỏng việc cập nhật hệ thống khi thông tin mới xuất hiện. Mục tiêu là xem edge có sống qua các cửa sổ khác nhau hay chỉ tồn tại ở một đoạn lịch sử.

**Walk-forward** mô phỏng quá trình cập nhật chiến lược theo thời gian:

```text
Huấn luyện trên quá khứ
→ kiểm tra đoạn tiếp theo
→ trượt cửa sổ
→ lặp lại
```

Nó giúp kiểm tra khả năng thích nghi khi chế độ thị trường thay đổi.

# Phần III — Các thiên lệch làm kết quả đẹp giả tạo

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **7. Thiên lệch nhìn trước** tiếp nhận điểm tựa từ **6. Kiểm thử cuốn chiếu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Thiên lệch sống sót** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Thiên lệch nhìn trước

Look-ahead bias làm chiến lược dùng thông tin mà tại thời điểm giao dịch chưa tồn tại. Hãy kiểm tra timestamp của observation, publication, revision và execution trước khi tin vào kết quả backtest.

**Thiên lệch nhìn trước (look-ahead bias)** xuất hiện khi dùng dữ liệu chưa tồn tại tại thời điểm quyết định.

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **8. Thiên lệch sống sót** tiếp nhận điểm tựa từ **7. Thiên lệch nhìn trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Đào bới dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Thiên lệch sống sót

Survivorship bias loại bỏ những tài sản thất bại khỏi mẫu, khiến distribution lịch sử quá lạc quan. Universe phải được xây theo trạng thái có thể biết tại từng thời điểm, không theo danh sách còn tồn tại hôm nay.

**Thiên lệch sống sót (survivorship bias)** xuất hiện khi chỉ giữ các tài sản còn tồn tại hôm nay và bỏ những tài sản đã hủy niêm yết hoặc phá sản.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **8. Thiên lệch sống sót** nêu điều cần giải thích; **9. Đào bới dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. Vấn đề thử nhiều giả thuyết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Đào bới dữ liệu

Data snooping biến số lần thử thành nguồn bias. Mỗi rule, feature và timeframe được thử đều làm tăng xác suất tìm thấy pattern ngẫu nhiên, nên cần log thử nghiệm và kiểm tra độc lập.

**Đào bới dữ liệu (data snooping)** là thử rất nhiều quy tắc rồi chỉ giữ kết quả đẹp nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **9. Đào bới dữ liệu** nêu điều cần giải thích; **10. Vấn đề thử nhiều giả thuyết** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. Không tìm một điểm tối ưu duy nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Vấn đề thử nhiều giả thuyết

Nếu thử hàng nghìn chiến lược, một số sẽ có Sharpe cao chỉ do may mắn. Phải tính tới số lượng thử nghiệm và mức độ tương quan giữa chúng.

# Phần IV — Độ ổn định của tham số

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **11. Không tìm một điểm tối ưu duy nhất** tiếp nhận điểm tựa từ **10. Vấn đề thử nhiều giả thuyết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Vùng tham số ổn định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Không tìm một điểm tối ưu duy nhất

Nếu chiến lược chỉ có lãi ở tham số 47 nhưng thua ở 46 và 48, lợi thế có thể là nhiễu.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **12. Vùng tham số ổn định** tiếp nhận điểm tựa từ **11. Không tìm một điểm tối ưu duy nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Tham số nên có ý nghĩa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Vùng tham số ổn định

Một vùng tham số rộng có kết quả tương đối ổn định thường đáng tin hơn một đỉnh hẹp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **13. Tham số nên có ý nghĩa** tiếp nhận điểm tựa từ **12. Vùng tham số ổn định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Lợi thế trước và sau chi phí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Tham số nên có ý nghĩa

Nếu có thể, tham số nên gắn với cơ chế kinh tế hoặc cấu trúc thị trường thay vì chỉ được chọn vì làm biểu đồ đẹp nhất.

# Phần V — Chi phí và công suất

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **14. Lợi thế trước và sau chi phí** tiếp nhận điểm tựa từ **13. Tham số nên có ý nghĩa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Tác động thị trường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Lợi thế trước và sau chi phí

Chiến lược chỉ có giá trị nếu:

```text
Lợi thế gộp
- chênh lệch mua–bán
- phí giao dịch
- trượt giá
- tác động thị trường
- chi phí tài trợ
- phí vay / chi phí cuộn kỳ hạn
> 0
```

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **15. Tác động thị trường** tiếp nhận điểm tựa từ **14. Lợi thế trước và sau chi phí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Công suất chiến lược** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Tác động thị trường

Khi vốn tăng, chính lệnh của chiến lược có thể làm giá di chuyển bất lợi. Kiểm thử bỏ qua yếu tố này thường đánh giá quá cao khả năng mở rộng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **16. Công suất chiến lược** tiếp nhận điểm tựa từ **15. Tác động thị trường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Lợi thế có thể phụ thuộc chế độ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Công suất chiến lược

Capacity hỏi chiến lược còn giữ expectancy bao lâu khi vốn tăng. Spread, impact, borrow, liquidity và market depth có thể làm edge biến mất trước khi giới hạn vốn danh nghĩa đạt tới.

**Công suất (capacity)** là lượng vốn có thể triển khai trước khi chi phí thực thi làm lợi thế biến mất.

Nó phụ thuộc:

- thanh khoản;
- vòng quay;
- thời gian nắm giữ;
- tỷ lệ tham gia;
- độ sâu thị trường.

# Phần VI — Phụ thuộc chế độ thị trường

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **17. Lợi thế có thể phụ thuộc chế độ** tiếp nhận điểm tựa từ **16. Công suất chiến lược** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Không dùng “chế độ thay đổi” để giải thích mọi thất bại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Lợi thế có thể phụ thuộc chế độ

Chiến lược theo xu hướng có thể tốt khi xu hướng rõ nhưng kém trong thị trường đảo chiều liên tục.

Chiến lược kiếm lợi từ chênh lệch lãi suất có thể tốt khi biến động thấp nhưng chịu tổn thất đuôi khi nguồn vốn căng thẳng.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **18. Không dùng “chế độ thay đổi” để giải thích mọi thất bại** tiếp nhận điểm tựa từ **17. Lợi thế có thể phụ thuộc chế độ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Các chế độ nên kiểm thử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Không dùng “chế độ thay đổi” để giải thích mọi thất bại

Định nghĩa chế độ phải được đặt trước hoặc có quy tắc quan sát rõ. Nếu chỉ nói “chế độ đã thay đổi” sau khi thua, đó có thể là giải thích bằng nhận thức muộn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **19. Các chế độ nên kiểm thử** tiếp nhận điểm tựa từ **18. Không dùng “chế độ thay đổi” để giải thích mọi thất bại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Trung bình không đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Các chế độ nên kiểm thử

Ít nhất nên có:

- biến động cao;
- biến động thấp;
- khủng hoảng thanh khoản;
- xu hướng mạnh;
- đi ngang;
- cú sốc chính sách;
- khoảng nhảy giá.

# Phần VII — Phân phối và rủi ro đuôi

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **20. Trung bình không đủ** tiếp nhận điểm tựa từ **19. Các chế độ nên kiểm thử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Cấu trúc bán biến động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Trung bình không đủ

Cần xem thêm:

- độ lệch phân phối;
- độ nhọn và đuôi dày;
- tổn thất đuôi;
- mức suy giảm;
- thua lỗ theo cụm.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **21. Cấu trúc bán biến động** tiếp nhận điểm tựa từ **20. Trung bình không đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Độ lồi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Cấu trúc bán biến động

Chiến lược có nhiều lệnh thắng nhỏ và vài lệnh thua rất lớn thường mang **độ lệch âm (negative skew)**.

Tỷ lệ thắng 90% không đồng nghĩa an toàn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **22. Độ lồi** tiếp nhận điểm tựa từ **21. Cấu trúc bán biến động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Kỳ vọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Độ lồi

Convexity mô tả payoff thay đổi phi tuyến khi giá cơ sở dịch chuyển. Nó có thể bảo vệ danh mục trong tail nhưng cũng tạo chi phí carry hoặc rủi ro margin, nên phải đọc cùng scenario chứ không chỉ direction.

**Độ lồi (convexity)** mô tả mức kết quả thay đổi phi tuyến khi giá cơ sở biến động.

Mua độ lồi thường phải trả chi phí nhỏ thường xuyên để đổi lấy khoản chi trả lớn trong cú sốc. Bán độ lồi thường ngược lại.

Danh mục cần biết mình đang nghiêng về phía nào.

# Phần VIII — Kỳ vọng và bất định

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **23. Kỳ vọng** tiếp nhận điểm tựa từ **22. Độ lồi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Khoảng tin cậy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Kỳ vọng

Expectancy là điểm nối giữa signal và khả năng sống sót: sau win rate, average win/loss, cost và sizing, hệ thống còn tạo phân phối dương hay không? Công thức chỉ có ý nghĩa khi sample và execution được mô tả rõ.

```text
Kỳ vọng
= P(thắng) × Lãi trung bình
- P(thua) × Lỗ trung bình
```

Bản thân ước lượng này cũng có sai số.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **24. Khoảng tin cậy** tiếp nhận điểm tựa từ **23. Kỳ vọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Kích thước mẫu hiệu dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Khoảng tin cậy

Lợi suất trung bình dương nhưng khoảng tin cậy rất rộng có thể chưa đủ bằng chứng rằng lợi thế là thật.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **25. Kích thước mẫu hiệu dụng** tiếp nhận điểm tựa từ **24. Khoảng tin cậy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Lấy mẫu lại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Kích thước mẫu hiệu dụng

500 giao dịch trong cùng một chế độ kinh tế không tương đương 500 quan sát độc lập. Tương quan giữa giao dịch làm kích thước mẫu hiệu dụng nhỏ hơn.

# Phần IX — Bootstrap và Monte Carlo

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **26. Lấy mẫu lại** tiếp nhận điểm tựa từ **25. Kích thước mẫu hiệu dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Mô phỏng Monte Carlo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Lấy mẫu lại

Bootstrap giúp nhìn độ bất định của kết quả khi thứ tự và mẫu quan sát thay đổi. Nó không tạo dữ liệu mới và không thể sửa bias hoặc regime chưa xuất hiện trong lịch sử.

**Bootstrap** lấy mẫu lại các quan sát lịch sử để tạo nhiều đường kết quả khả dĩ.

Nó giúp thấy phân phối mức suy giảm và lợi suất thay vì chỉ một đường vốn.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **27. Mô phỏng Monte Carlo** tiếp nhận điểm tựa từ **26. Lấy mẫu lại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Không biến mô phỏng thành độ chính xác giả** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Mô phỏng Monte Carlo

Monte Carlo có thể mô phỏng:

- thứ tự giao dịch;
- phân phối lãi/lỗ;
- biến động;
- chuyển đổi chế độ;
- bất định tham số.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **28. Không biến mô phỏng thành độ chính xác giả** tiếp nhận điểm tựa từ **27. Mô phỏng Monte Carlo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Nguy cơ phá sản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Không biến mô phỏng thành độ chính xác giả

Kết quả phụ thuộc giả định đầu vào. Nếu phân phối giả định sai, mô phỏng phức tạp vẫn có thể sai.

# Phần X — Nguy cơ phá sản và quy mô vị thế

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **29. Nguy cơ phá sản** tiếp nhận điểm tựa từ **28. Không biến mô phỏng thành độ chính xác giả** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Tiêu chuẩn Kelly** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Nguy cơ phá sản

Nguy cơ phá sản tăng khi:

- rủi ro mỗi giao dịch lớn;
- đòn bẩy cao;
- lợi thế nhỏ;
- thua lỗ tương quan;
- rủi ro đuôi lớn.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **30. Tiêu chuẩn Kelly** tiếp nhận điểm tựa từ **29. Nguy cơ phá sản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Ngân sách mức suy giảm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Tiêu chuẩn Kelly

Kelly tối đa hóa tăng trưởng log dài hạn dưới giả định biết chính xác lợi thế. Trong thực tế thường dùng **Kelly phân số (fractional Kelly)** vì lợi thế chỉ được ước lượng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **31. Ngân sách mức suy giảm** tiếp nhận điểm tựa từ **30. Tiêu chuẩn Kelly** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Vì sao lợi thế suy giảm?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Ngân sách mức suy giảm

Danh mục nên định trước mức suy giảm nào dẫn tới:

- giảm quy mô;
- dừng chiến lược;
- xem lại mô hình;
- kiểm tra vận hành.

Không nên quyết định trong lúc hoảng loạn.

# Phần XI — Suy giảm chiến lược

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **32. Vì sao lợi thế suy giảm?** tiếp nhận điểm tựa từ **31. Ngân sách mức suy giảm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Phân biệt biến động bình thường và suy giảm thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Vì sao lợi thế suy giảm?

Có thể do:

- nhiều người khai thác cùng bất thường;
- cấu trúc thị trường thay đổi;
- chi phí tăng;
- quy định thay đổi;
- chế độ kinh tế thay đổi;
- chất lượng thực thi giảm.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **33. Phân biệt biến động bình thường và suy giảm thật** tiếp nhận điểm tựa từ **32. Vì sao lợi thế suy giảm?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Chỉ số theo dõi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Phân biệt biến động bình thường và suy giảm thật

Một chuỗi thua không tự động chứng minh lợi thế đã mất. Cần so kết quả với phân phối đã kỳ vọng trước đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **34. Chỉ số theo dõi** tiếp nhận điểm tựa từ **33. Phân biệt biến động bình thường và suy giảm thật** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Mỗi thay đổi phải có lý do** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Chỉ số theo dõi

Theo dõi:

```text
Kỳ vọng
Tỷ lệ thắng
Tỷ lệ lãi/lỗ
Mức suy giảm
Trượt giá
Vòng quay
Phơi nhiễm nhân tố
Công suất
```

# Phần XII — Nhật ký nghiên cứu

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **35. Mỗi thay đổi phải có lý do** tiếp nhận điểm tựa từ **34. Chỉ số theo dõi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Không viết lại lịch sử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Mỗi thay đổi phải có lý do

Ghi:

```text
Ngày
Phiên bản
Giả thuyết
Thay đổi quy tắc
Lý do
Ảnh hưởng kỳ vọng
Kết quả xác thực
```

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **36. Không viết lại lịch sử** tiếp nhận điểm tựa từ **35. Mỗi thay đổi phải có lý do** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Kiểm thử tiến tới tương lai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Không viết lại lịch sử

Nếu chiến lược được sửa sau một chuỗi lỗ, phải giữ phiên bản cũ để biết quyết định lúc đó dựa trên quy tắc nào. Điều này giúp chống thiên lệch nhận thức muộn.

# Phần XIII — Kiểm thử tiến tới tương lai và giao dịch thật nhỏ

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **37. Kiểm thử tiến tới tương lai** tiếp nhận điểm tựa từ **36. Không viết lại lịch sử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Giao dịch thật với quy mô nhỏ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Kiểm thử tiến tới tương lai

Forward test đưa chiến lược vào dữ liệu mới với rule đã khóa, giúp phát hiện chênh lệch giữa backtest và vận hành. Giai đoạn này cần ghi phiên bản, cost, latency và mọi can thiệp thủ công.

**Kiểm thử tiến tới tương lai (forward test)** chạy trên dữ liệu mới theo thời gian thật giúp phát hiện:

- trễ dữ liệu;
- khác biệt thực thi;
- lỗi phần mềm;
- chi phí cao hơn giả định.

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **38. Giao dịch thật với quy mô nhỏ** tiếp nhận điểm tựa từ **37. Kiểm thử tiến tới tương lai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Tăng quy mô từng bước** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Giao dịch thật với quy mô nhỏ

Quy mô nhỏ cho phép đo chất lượng khớp và vận hành trước khi tăng vốn.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **39. Tăng quy mô từng bước** tiếp nhận điểm tựa từ **38. Giao dịch thật với quy mô nhỏ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Nhiều chiến lược không tự động tạo đa dạng hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Tăng quy mô từng bước

Không nên đi trực tiếp từ kiểm thử quá khứ sang toàn bộ vốn.

Một lộ trình hợp lý:

```text
Kiểm thử quá khứ
→ ngoài mẫu
→ walk-forward
→ mô phỏng thời gian thật
→ vốn thật nhỏ
→ tăng quy mô dần
```

# Phần XIV — Danh mục nhiều chiến lược

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **40. Nhiều chiến lược không tự động tạo đa dạng hóa** tiếp nhận điểm tựa từ **39. Tăng quy mô từng bước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Tương quan giữa chiến lược** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Nhiều chiến lược không tự động tạo đa dạng hóa

Một danh mục có chiến lược theo xu hướng, kiếm chênh lệch lãi suất, bán quyền chọn và hồi quy về trung bình vẫn có thể cùng phụ thuộc vào biến động thấp hoặc thanh khoản dồi dào.

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **41. Tương quan giữa chiến lược** tiếp nhận điểm tựa từ **40. Nhiều chiến lược không tự động tạo đa dạng hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Phân rã theo nhân tố** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Tương quan giữa chiến lược

Tương quan nên được đo cả trong giai đoạn bình thường và giai đoạn căng thẳng. Trung bình lịch sử thấp không bảo đảm tương quan thấp khi khủng hoảng.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **42. Phân rã theo nhân tố** tiếp nhận điểm tựa từ **41. Tương quan giữa chiến lược** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Chia vốn bằng nhau khác chia rủi ro bằng nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Phân rã theo nhân tố

Ánh xạ chiến lược về các nhân tố:

```text
Beta cổ phiếu
Lãi suất
USD
Carry
Xu hướng
Biến động
Thanh khoản
Hàng hóa
Quốc gia
```

Hai chiến lược dùng công cụ khác nhau có thể thực chất là cùng một cược nhân tố.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **43. Chia vốn bằng nhau khác chia rủi ro bằng nhau** tiếp nhận điểm tựa từ **42. Phân rã theo nhân tố** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Điều chỉnh theo độ biến động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Chia vốn bằng nhau khác chia rủi ro bằng nhau

Một chiến lược có độ biến động 5% và một chiến lược 30% không đóng góp rủi ro ngang nhau chỉ vì tỷ trọng vốn giống nhau.

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **44. Điều chỉnh theo độ biến động** tiếp nhận điểm tựa từ **43. Chia vốn bằng nhau khác chia rủi ro bằng nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. Đóng góp rủi ro** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Điều chỉnh theo độ biến động

Có thể điều chỉnh quy mô để các chiến lược có mức rủi ro gần nhau hơn, nhưng vẫn cần giới hạn riêng cho rủi ro đuôi, đòn bẩy và thanh khoản.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **45. Đóng góp rủi ro** tiếp nhận điểm tựa từ **44. Điều chỉnh theo độ biến động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. Tương quan có thể vỡ cấu trúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. Đóng góp rủi ro

Cần biết mỗi chiến lược đóng góp bao nhiêu vào độ biến động danh mục và tổn thất trong kịch bản căng thẳng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **46. Tương quan có thể vỡ cấu trúc** tiếp nhận điểm tựa từ **45. Đóng góp rủi ro** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. Tập trung bán biến động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Tương quan có thể vỡ cấu trúc

Trong khủng hoảng nguồn vốn, nhiều chiến lược cùng giảm đòn bẩy khiến tương quan tăng đột ngột. Vì vậy cần ma trận kịch bản ngoài hiệp phương sai lịch sử.

# Phần XV — Độ lồi và rủi ro đuôi trong danh mục

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **47. Tập trung bán biến động** tiếp nhận điểm tựa từ **46. Tương quan có thể vỡ cấu trúc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. Phòng vệ đuôi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Tập trung bán biến động

Các chiến lược tưởng khác nhau như bán quyền chọn, kiếm carry, cung cấp thanh khoản và một số chiến lược hồi quy về trung bình có thể cùng chịu rủi ro bán biến động.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **48. Phòng vệ đuôi** tiếp nhận điểm tựa từ **47. Tập trung bán biến động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Ngân sách phòng vệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. Phòng vệ đuôi

Tail hedge cần được đánh giá ở cấp portfolio và theo nhiều năm: chi phí thường xuyên đổi lấy khả năng giảm loss cực đoan, forced selling và margin stress. P/L riêng của hedge không phải tiêu chí duy nhất.

**Phòng vệ đuôi (tail hedge)** có thể giảm tổn thất cực đoan nhưng tạo chi phí mang vị thế. Phải đánh giá ở cấp toàn danh mục và qua nhiều năm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **49. Ngân sách phòng vệ** tiếp nhận điểm tựa từ **48. Phòng vệ đuôi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. Chiến lược đúng vẫn có thể mất tiền vì lỗi vận hành** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Ngân sách phòng vệ

Định trước ngân sách phòng vệ giúp tránh mua bảo hiểm quá đắt sau khi khủng hoảng đã bắt đầu.

# Phần XVI — Rủi ro vận hành

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **50. Chiến lược đúng vẫn có thể mất tiền vì lỗi vận hành** tiếp nhận điểm tựa từ **49. Ngân sách phòng vệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. Công tắc dừng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. Chiến lược đúng vẫn có thể mất tiền vì lỗi vận hành

Ví dụ:

- dữ liệu cũ;
- lệnh trùng;
- sai mã;
- sai hệ số hợp đồng;
- mất kết nối API;
- sai trạng thái ký quỹ.

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **51. Công tắc dừng** tiếp nhận điểm tựa từ **50. Chiến lược đúng vẫn có thể mất tiền vì lỗi vận hành** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **52. Đối soát** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 51. Công tắc dừng

Mỗi chiến lược cần điều kiện dừng khi trạng thái vận hành không còn đáng tin.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **52. Đối soát** tiếp nhận điểm tựa từ **51. Công tắc dừng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **53. Không chỉ hỏi giao dịch lời hay lỗ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 52. Đối soát

Vị thế thực tế phải được đối chiếu với trạng thái tại nhà môi giới hoặc sở giao dịch.

# Phần XVII — Phân rã sau giao dịch

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **53. Không chỉ hỏi giao dịch lời hay lỗ** tiếp nhận điểm tựa từ **52. Đối soát** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **54. Chất lượng quyết định và kết quả** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. Không chỉ hỏi giao dịch lời hay lỗ

Phân rã:

```text
Chất lượng tín hiệu
Quy mô vị thế
Thực thi
Chi phí
Chế độ thị trường
Biến động nhân tố
Can thiệp thủ công
```

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **54. Chất lượng quyết định và kết quả** tiếp nhận điểm tựa từ **53. Không chỉ hỏi giao dịch lời hay lỗ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **55. Đánh giá theo chiến lược** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 54. Chất lượng quyết định và kết quả

Một quyết định đúng quy trình vẫn có thể lỗ do bất định. Một quyết định tệ vẫn có thể lời do may mắn. rà soát (review / 검토) phải tách hai thứ.

# Phần XVIII — Đánh giá định kỳ

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **55. Đánh giá theo chiến lược** tiếp nhận điểm tựa từ **54. Chất lượng quyết định và kết quả** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **56. Đánh giá toàn danh mục** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 55. Đánh giá theo chiến lược

Đánh giá từng chiến lược cần tách signal edge, cost, capacity, drawdown và regime dependence. Một chiến lược tốt riêng lẻ vẫn có thể làm danh mục xấu hơn nếu trùng factor với các chiến lược khác.

```text
Lợi suất
Mức suy giảm
Kỳ vọng
Tỷ lệ thắng
Lãi/lỗ trung bình
Trượt giá
Chi phí
Công suất
Phơi nhiễm nhân tố
```

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **56. Đánh giá toàn danh mục** tiếp nhận điểm tựa từ **55. Đánh giá theo chiến lược** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **57. Kỷ luật thay đổi quy tắc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 56. Đánh giá toàn danh mục

Portfolio review tổng hợp beta, carry, volatility, liquidity, correlation và tail exposure của toàn bộ chiến lược. Mục tiêu là biết hệ thống cùng thất bại ở trạng thái nào và có cần giảm trùng lặp hay không.

```text
Phơi nhiễm tổng / ròng
Đóng góp rủi ro
Tương quan
Rủi ro đuôi
Thanh khoản
Ký quỹ
Tổn thất căng thẳng
```

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **57. Kỷ luật thay đổi quy tắc** tiếp nhận điểm tựa từ **56. Đánh giá toàn danh mục** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **58. Bằng chứng lợi thế đã mất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 57. Kỷ luật thay đổi quy tắc

Không thay quy tắc chỉ vì tháng vừa rồi xấu. Mọi thay đổi phải có giả thuyết, kiểm thử và phiên bản riêng.

# Phần XIX — Khi nào nên dừng chiến lược?

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **57. Kỷ luật thay đổi quy tắc** nêu điều cần giải thích; **58. Bằng chứng lợi thế đã mất** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **59. Chi phí chìm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 58. Bằng chứng lợi thế đã mất

Có thể cân nhắc dừng khi:

- kết quả ngoài mẫu hoặc giao dịch thật lệch lớn khỏi phân phối kỳ vọng;
- chi phí vượt lợi thế;
- cấu trúc thị trường thay đổi;
- công suất quá nhỏ;
- rủi ro vận hành quá cao.

> **Chuyển mạch:** Trong **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **58. Bằng chứng lợi thế đã mất** nêu điều cần giải thích; **59. Chi phí chìm** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **60. Chuỗi nghiên cứu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 59. Chi phí chìm

Thời gian đã bỏ vào nghiên cứu không phải lý do tiếp tục một chiến lược không còn hiệu quả.

# Phần XX — Quy trình nghiên cứu chuẩn

> **Chuyển mạch:** Ở chặng này của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **59. Chi phí chìm** xác định đầu vào; **60. Chuỗi nghiên cứu** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 60. Chuỗi nghiên cứu

Chuỗi cuối cùng biến nghiên cứu thành quy trình lặp: giả thuyết, dữ liệu, test, robustness, sizing, execution, monitoring và retirement. Mỗi bước phải có đầu ra và điều kiện dừng để hệ thống không tiếp tục vì quán tính.

```text
Giả thuyết
→ quy tắc chính thức
→ kiểm tra dữ liệu
→ trong mẫu
→ kiểm tra độ bền
→ ngoài mẫu
→ walk-forward
→ chi phí / công suất
→ bootstrap / Monte Carlo
→ kiểm thử tiến tới tương lai
→ vốn thật nhỏ
→ tích hợp vào danh mục
→ giám sát
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược**, **Kết luận** gom các mảnh từ **60. Chuỗi nghiên cứu** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết luận

Nghiên cứu chiến lược tốt không tìm “một biểu đồ đẹp nhất”. Nó cố trả lời ba câu hỏi:

```text
Lợi thế có thật không?
Lợi thế còn tồn tại sau chi phí không?
Lợi thế có đóng góp đa dạng hóa thật cho danh mục không?
```

Chỉ khi cả ba câu trả lời đều đủ thuyết phục, chiến lược mới đáng được tăng vốn.

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
