# Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược

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

## 2. Bắt đầu bằng giả thuyết

Giả thuyết nên giải thích vì sao lợi thế có thể tồn tại, ví dụ:

- phần bù rủi ro;
- thiên lệch hành vi;
- nhu cầu thanh khoản;
- giới hạn của tổ chức lớn;
- thông tin lan truyền chậm;
- cấu trúc thị trường.

Có một cơ chế hợp lý giúp giảm nguy cơ chỉ tìm thấy mẫu ngẫu nhiên sau khi nhìn dữ liệu.

## 3. Cố gắng bác bỏ giả thuyết

Một quy trình nghiên cứu tốt phải chủ động tìm bằng chứng chống lại chính giả thuyết của mình.

Ví dụ:

```text
Nếu lợi thế biến mất khi thêm chi phí hợp lý
hoặc không tồn tại ngoài mẫu
→ giả thuyết chưa đủ mạnh
```

# Phần II — Trong mẫu và ngoài mẫu

## 4. Dữ liệu trong mẫu

**Trong mẫu (in-sample)** là dữ liệu dùng để xây hoặc điều chỉnh chiến lược. Kết quả đẹp ở đây dễ bị khớp quá mức nhất.

## 5. Dữ liệu ngoài mẫu

**Ngoài mẫu (out-of-sample, OOS)** là dữ liệu chưa dùng để thiết kế quy tắc.

Nếu lợi thế giữ được ngoài mẫu, bằng chứng mạnh hơn nhưng vẫn không bảo đảm tương lai.

## 6. Kiểm thử cuốn chiếu

**Walk-forward** mô phỏng quá trình cập nhật chiến lược theo thời gian:

```text
Huấn luyện trên quá khứ
→ kiểm tra đoạn tiếp theo
→ trượt cửa sổ
→ lặp lại
```

Nó giúp kiểm tra khả năng thích nghi khi chế độ thị trường thay đổi.

# Phần III — Các thiên lệch làm kết quả đẹp giả tạo

## 7. Thiên lệch nhìn trước

**Thiên lệch nhìn trước (look-ahead bias)** xuất hiện khi dùng dữ liệu chưa tồn tại tại thời điểm quyết định.

## 8. Thiên lệch sống sót

**Thiên lệch sống sót (survivorship bias)** xuất hiện khi chỉ giữ các tài sản còn tồn tại hôm nay và bỏ những tài sản đã hủy niêm yết hoặc phá sản.

## 9. Đào bới dữ liệu

**Đào bới dữ liệu (data snooping)** là thử rất nhiều quy tắc rồi chỉ giữ kết quả đẹp nhất.

## 10. Vấn đề thử nhiều giả thuyết

Nếu thử hàng nghìn chiến lược, một số sẽ có Sharpe cao chỉ do may mắn. Phải tính tới số lượng thử nghiệm và mức độ tương quan giữa chúng.

# Phần IV — Độ ổn định của tham số

## 11. Không tìm một điểm tối ưu duy nhất

Nếu chiến lược chỉ có lãi ở tham số 47 nhưng thua ở 46 và 48, lợi thế có thể là nhiễu.

## 12. Vùng tham số ổn định

Một vùng tham số rộng có kết quả tương đối ổn định thường đáng tin hơn một đỉnh hẹp.

## 13. Tham số nên có ý nghĩa

Nếu có thể, tham số nên gắn với cơ chế kinh tế hoặc cấu trúc thị trường thay vì chỉ được chọn vì làm biểu đồ đẹp nhất.

# Phần V — Chi phí và công suất

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

## 15. Tác động thị trường

Khi vốn tăng, chính lệnh của chiến lược có thể làm giá di chuyển bất lợi. Kiểm thử bỏ qua yếu tố này thường đánh giá quá cao khả năng mở rộng.

## 16. Công suất chiến lược

**Công suất (capacity)** là lượng vốn có thể triển khai trước khi chi phí thực thi làm lợi thế biến mất.

Nó phụ thuộc:

- thanh khoản;
- vòng quay;
- thời gian nắm giữ;
- tỷ lệ tham gia;
- độ sâu thị trường.

# Phần VI — Phụ thuộc chế độ thị trường

## 17. Lợi thế có thể phụ thuộc chế độ

Chiến lược theo xu hướng có thể tốt khi xu hướng rõ nhưng kém trong thị trường đảo chiều liên tục.

Chiến lược kiếm lợi từ chênh lệch lãi suất có thể tốt khi biến động thấp nhưng chịu tổn thất đuôi khi nguồn vốn căng thẳng.

## 18. Không dùng “chế độ thay đổi” để giải thích mọi thất bại

Định nghĩa chế độ phải được đặt trước hoặc có quy tắc quan sát rõ. Nếu chỉ nói “chế độ đã thay đổi” sau khi thua, đó có thể là giải thích bằng nhận thức muộn.

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

## 20. Trung bình không đủ

Cần xem thêm:

- độ lệch phân phối;
- độ nhọn và đuôi dày;
- tổn thất đuôi;
- mức suy giảm;
- thua lỗ theo cụm.

## 21. Cấu trúc bán biến động

Chiến lược có nhiều lệnh thắng nhỏ và vài lệnh thua rất lớn thường mang **độ lệch âm (negative skew)**.

Tỷ lệ thắng 90% không đồng nghĩa an toàn.

## 22. Độ lồi

**Độ lồi (convexity)** mô tả mức kết quả thay đổi phi tuyến khi giá cơ sở biến động.

Mua độ lồi thường phải trả chi phí nhỏ thường xuyên để đổi lấy khoản chi trả lớn trong cú sốc. Bán độ lồi thường ngược lại.

Danh mục cần biết mình đang nghiêng về phía nào.

# Phần VIII — Kỳ vọng và bất định

## 23. Kỳ vọng

```text
Kỳ vọng
= P(thắng) × Lãi trung bình
- P(thua) × Lỗ trung bình
```

Bản thân ước lượng này cũng có sai số.

## 24. Khoảng tin cậy

Lợi suất trung bình dương nhưng khoảng tin cậy rất rộng có thể chưa đủ bằng chứng rằng lợi thế là thật.

## 25. Kích thước mẫu hiệu dụng

500 giao dịch trong cùng một chế độ kinh tế không tương đương 500 quan sát độc lập. Tương quan giữa giao dịch làm kích thước mẫu hiệu dụng nhỏ hơn.

# Phần IX — Bootstrap và Monte Carlo

## 26. Lấy mẫu lại

**Bootstrap** lấy mẫu lại các quan sát lịch sử để tạo nhiều đường kết quả khả dĩ.

Nó giúp thấy phân phối mức suy giảm và lợi suất thay vì chỉ một đường vốn.

## 27. Mô phỏng Monte Carlo

Monte Carlo có thể mô phỏng:

- thứ tự giao dịch;
- phân phối lãi/lỗ;
- biến động;
- chuyển đổi chế độ;
- bất định tham số.

## 28. Không biến mô phỏng thành độ chính xác giả

Kết quả phụ thuộc giả định đầu vào. Nếu phân phối giả định sai, mô phỏng phức tạp vẫn có thể sai.

# Phần X — Nguy cơ phá sản và quy mô vị thế

## 29. Nguy cơ phá sản

Nguy cơ phá sản tăng khi:

- rủi ro mỗi giao dịch lớn;
- đòn bẩy cao;
- lợi thế nhỏ;
- thua lỗ tương quan;
- rủi ro đuôi lớn.

## 30. Tiêu chuẩn Kelly

Kelly tối đa hóa tăng trưởng log dài hạn dưới giả định biết chính xác lợi thế. Trong thực tế thường dùng **Kelly phân số (fractional Kelly)** vì lợi thế chỉ được ước lượng.

## 31. Ngân sách mức suy giảm

Danh mục nên định trước mức suy giảm nào dẫn tới:

- giảm quy mô;
- dừng chiến lược;
- xem lại mô hình;
- kiểm tra vận hành.

Không nên quyết định trong lúc hoảng loạn.

# Phần XI — Suy giảm chiến lược

## 32. Vì sao lợi thế suy giảm?

Có thể do:

- nhiều người khai thác cùng bất thường;
- cấu trúc thị trường thay đổi;
- chi phí tăng;
- quy định thay đổi;
- chế độ kinh tế thay đổi;
- chất lượng thực thi giảm.

## 33. Phân biệt biến động bình thường và suy giảm thật

Một chuỗi thua không tự động chứng minh lợi thế đã mất. Cần so kết quả với phân phối đã kỳ vọng trước đó.

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

## 36. Không viết lại lịch sử

Nếu chiến lược được sửa sau một chuỗi lỗ, phải giữ phiên bản cũ để biết quyết định lúc đó dựa trên quy tắc nào. Điều này giúp chống thiên lệch nhận thức muộn.

# Phần XIII — Kiểm thử tiến tới tương lai và giao dịch thật nhỏ

## 37. Kiểm thử tiến tới tương lai

**Kiểm thử tiến tới tương lai (forward test)** chạy trên dữ liệu mới theo thời gian thật giúp phát hiện:

- trễ dữ liệu;
- khác biệt thực thi;
- lỗi phần mềm;
- chi phí cao hơn giả định.

## 38. Giao dịch thật với quy mô nhỏ

Quy mô nhỏ cho phép đo chất lượng khớp và vận hành trước khi tăng vốn.

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

## 40. Nhiều chiến lược không tự động tạo đa dạng hóa

Một danh mục có chiến lược theo xu hướng, kiếm chênh lệch lãi suất, bán quyền chọn và hồi quy về trung bình vẫn có thể cùng phụ thuộc vào biến động thấp hoặc thanh khoản dồi dào.

## 41. Tương quan giữa chiến lược

Tương quan nên được đo cả trong giai đoạn bình thường và giai đoạn căng thẳng. Trung bình lịch sử thấp không bảo đảm tương quan thấp khi khủng hoảng.

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

## 43. Chia vốn bằng nhau khác chia rủi ro bằng nhau

Một chiến lược có độ biến động 5% và một chiến lược 30% không đóng góp rủi ro ngang nhau chỉ vì tỷ trọng vốn giống nhau.

## 44. Điều chỉnh theo độ biến động

Có thể điều chỉnh quy mô để các chiến lược có mức rủi ro gần nhau hơn, nhưng vẫn cần giới hạn riêng cho rủi ro đuôi, đòn bẩy và thanh khoản.

## 45. Đóng góp rủi ro

Cần biết mỗi chiến lược đóng góp bao nhiêu vào độ biến động danh mục và tổn thất trong kịch bản căng thẳng.

## 46. Tương quan có thể vỡ cấu trúc

Trong khủng hoảng nguồn vốn, nhiều chiến lược cùng giảm đòn bẩy khiến tương quan tăng đột ngột. Vì vậy cần ma trận kịch bản ngoài hiệp phương sai lịch sử.

# Phần XV — Độ lồi và rủi ro đuôi trong danh mục

## 47. Tập trung bán biến động

Các chiến lược tưởng khác nhau như bán quyền chọn, kiếm carry, cung cấp thanh khoản và một số chiến lược hồi quy về trung bình có thể cùng chịu rủi ro bán biến động.

## 48. Phòng vệ đuôi

**Phòng vệ đuôi (tail hedge)** có thể giảm tổn thất cực đoan nhưng tạo chi phí mang vị thế. Phải đánh giá ở cấp toàn danh mục và qua nhiều năm.

## 49. Ngân sách phòng vệ

Định trước ngân sách phòng vệ giúp tránh mua bảo hiểm quá đắt sau khi khủng hoảng đã bắt đầu.

# Phần XVI — Rủi ro vận hành

## 50. Chiến lược đúng vẫn có thể mất tiền vì lỗi vận hành

Ví dụ:

- dữ liệu cũ;
- lệnh trùng;
- sai mã;
- sai hệ số hợp đồng;
- mất kết nối API;
- sai trạng thái ký quỹ.

## 51. Công tắc dừng

Mỗi chiến lược cần điều kiện dừng khi trạng thái vận hành không còn đáng tin.

## 52. Đối soát

Vị thế thực tế phải được đối chiếu với trạng thái tại nhà môi giới hoặc sở giao dịch.

# Phần XVII — Phân rã sau giao dịch

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

## 54. Chất lượng quyết định và kết quả

Một quyết định đúng quy trình vẫn có thể lỗ do bất định. Một quyết định tệ vẫn có thể lời do may mắn. Review phải tách hai thứ.

# Phần XVIII — Đánh giá định kỳ

## 55. Đánh giá theo chiến lược

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

## 56. Đánh giá toàn danh mục

```text
Phơi nhiễm tổng / ròng
Đóng góp rủi ro
Tương quan
Rủi ro đuôi
Thanh khoản
Ký quỹ
Tổn thất căng thẳng
```

## 57. Kỷ luật thay đổi quy tắc

Không thay quy tắc chỉ vì tháng vừa rồi xấu. Mọi thay đổi phải có giả thuyết, kiểm thử và phiên bản riêng.

# Phần XIX — Khi nào nên dừng chiến lược?

## 58. Bằng chứng lợi thế đã mất

Có thể cân nhắc dừng khi:

- kết quả ngoài mẫu hoặc giao dịch thật lệch lớn khỏi phân phối kỳ vọng;
- chi phí vượt lợi thế;
- cấu trúc thị trường thay đổi;
- công suất quá nhỏ;
- rủi ro vận hành quá cao.

## 59. Chi phí chìm

Thời gian đã bỏ vào nghiên cứu không phải lý do tiếp tục một chiến lược không còn hiệu quả.

# Phần XX — Quy trình nghiên cứu chuẩn

## 60. Chuỗi nghiên cứu

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

## Kết luận

Nghiên cứu chiến lược tốt không tìm “một biểu đồ đẹp nhất”. Nó cố trả lời ba câu hỏi:

```text
Lợi thế có thật không?
Lợi thế còn tồn tại sau chi phí không?
Lợi thế có đóng góp đa dạng hóa thật cho danh mục không?
```

Chỉ khi cả ba câu trả lời đều đủ thuyết phục, chiến lược mới đáng được tăng vốn.