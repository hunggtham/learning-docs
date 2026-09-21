# Phân rã kết quả đầu tư, chi phí, thuế và đánh giá hành vi

> Danh mục tăng 15% không tự động nghĩa chiến lược tốt; danh mục giảm 8% cũng không tự động nghĩa quyết định sai. Chương này xây vòng phản hồi để trả lời: kết quả đến từ đâu, bao nhiêu là beta thị trường, bao nhiêu là lựa chọn chủ động, bao nhiêu bị mất bởi chi phí/thuế và liệu quy trình ra quyết định có thật sự tốt lên hay không.

## 1. Kết quả đầu tư phải được đặt cạnh mục tiêu

Một danh mục 10% có thể tốt nếu mục tiêu là 6% với rủi ro thấp, nhưng kém nếu benchmark phù hợp tăng 20% với rủi ro tương đương.

Trước khi đánh giá phải xác định:

```text
Mục tiêu
Benchmark
Đồng tiền báo cáo
Khoảng thời gian
Lợi suất trước hay sau phí/thuế
```

Không thay benchmark sau khi đã biết kết quả.

## 2. Lợi suất tuyệt đối và lợi suất chủ động

Lợi suất tuyệt đối là lợi suất của chính danh mục. Lợi suất chủ động (active return) là phần chênh so với benchmark:

```text
Active Return = Portfolio Return - Benchmark Return
```

Nếu danh mục tăng 8% nhưng benchmark tăng 12%, lợi suất tuyệt đối dương nhưng lợi suất chủ động âm.

## 3. Time-Weighted Return và Money-Weighted Return

Time-Weighted Return (TWR) đánh giá chiến lược không phụ thuộc thời điểm dòng tiền của nhà đầu tư.

Money-Weighted Return (MWR/IRR) phản ánh trải nghiệm thực vì tính cả thời điểm nạp/rút tiền.

Nếu nhà đầu tư đổ nhiều tiền vào sau khi thị trường tăng và rút sau khi giảm, MWR có thể kém xa TWR của cùng quỹ.

## 4. Phân rã theo phân bổ và lựa chọn

Một khung phổ biến tách kết quả thành:

```text
Tác động phân bổ (allocation effect)
Tác động lựa chọn chứng khoán (selection effect)
Tác động tương tác (interaction effect)
```

Phân bổ trả lời: bạn tăng/giảm tỷ trọng đúng nhóm tài sản hoặc ngành chưa?

Lựa chọn trả lời: trong cùng nhóm, bạn chọn chứng khoán tốt hơn benchmark chưa?

## 5. Phân rã theo nhân tố

Một danh mục có thể vượt benchmark vì mang nhiều beta giá trị, động lượng, vốn hóa nhỏ, chất lượng hoặc duration.

Do đó nên hỏi:

```text
Bao nhiêu lợi suất đến từ nhân tố có hệ thống?
Bao nhiêu là alpha còn lại sau khi đã tính nhân tố?
```

Nếu toàn bộ phần vượt trội đến từ một nhân tố quen thuộc, không nên gọi tất cả là kỹ năng lựa chọn chứng khoán.

## 6. Phân rã tiền tệ

Với tài sản nước ngoài, lợi suất theo đồng tiền cơ sở gồm lợi suất tài sản và FX.

```text
Home Return = (1 + Local Return) × (1 + FX Return) - 1
```

Đánh giá nên tách:

```text
Lợi suất tài sản bằng đồng tiền địa phương
Tác động FX
Chi phí phòng vệ FX
Tương tác giữa hai phần
```

Điều này đặc biệt quan trọng khi so quỹ có phòng vệ và không phòng vệ.

## 7. Phân rã thu nhập

Tổng lợi suất có thể đến từ:

```text
Cổ tức
Coupon
Lãi tiền mặt
Carry
Lợi nhuận vốn
Thay đổi định giá
```

Nhà đầu tư cần biết phần nào có thể lặp lại. Một năm tốt do hệ số định giá mở rộng không giống một năm tốt do dòng tiền/cổ tức tăng.

## 8. Phí quản lý

Phí nhỏ nhưng kéo dài nhiều năm có tác động lớn do ghép lãi.

Sự khác biệt 0,5% mỗi năm giữa hai sản phẩm có thể trở thành khoảng cách đáng kể sau hàng chục năm.

Nhưng phí thấp không tự động tốt nếu sản phẩm bám chỉ số kém, spread rộng hoặc cấu trúc thuế bất lợi.

## 9. Chênh lệch mua bán và trượt giá

Chi phí thực thi gồm chênh lệch mua bán, phí môi giới, trượt giá và tác động thị trường.

Một chiến lược có lợi thế trước chi phí 30 điểm cơ bản mỗi giao dịch nhưng mất 25 điểm cơ bản cho thực thi chỉ còn rất ít biên an toàn.

Cần đo chi phí thực tế theo quy mô, thời điểm và điều kiện thanh khoản.

## 10. Implementation Shortfall

Thiếu hụt thực thi (implementation shortfall) so sánh kết quả thực tế với giá quyết định lý thuyết.

Nó có thể bao gồm:

```text
Độ trễ từ quyết định tới gửi lệnh
Spread
Slippage
Tác động thị trường
Lệnh không khớp
Chi phí cơ hội
```

Nếu chiến lược tốt trên giấy nhưng kém khi triển khai, đây thường là nơi cần kiểm tra đầu tiên.

## 11. Chi phí vốn và vay chứng khoán

Vị thế dùng đòn bẩy, CFD, short hoặc phái sinh có thể chịu chi phí vốn.

Bán khống còn có phí vay chứng khoán và rủi ro phí tăng đột biến.

Một giao dịch đúng hướng nhưng giữ lâu có thể bị carry âm làm mất phần lớn lợi nhuận.

## 12. Thuế kéo lùi lợi suất

Thuế có thể tác động qua:

```text
Cổ tức / lãi
Lãi vốn thực hiện
Khấu trừ tại nguồn
Thời điểm hiện thực hóa
Tài khoản ưu đãi thuế
```

Vì quy định thay đổi theo quốc gia và thời điểm, thư viện chỉ giữ logic. Trước quyết định thật cần kiểm tra nguồn chính thức.

## 13. Lợi suất sau thuế là thứ nhà đầu tư sử dụng được

Hai chiến lược cùng lợi suất trước thuế có thể khác lớn về kết quả sau thuế nếu một chiến lược quay vòng nhiều và tạo thu nhập chịu thuế thường xuyên.

Đối với mục tiêu dài hạn, trì hoãn thuế có thể có giá trị nhờ tiếp tục ghép lãi trên phần chưa nộp.

## 14. Turnover là một biến kinh tế

Vòng quay (turnover) cao không tự động xấu, nhưng phải được biện minh bằng lợi thế đủ lớn.

```text
Lợi thế gộp
- Spread
- Slippage
- Phí
- Thuế
- Tác động thị trường
= Lợi thế ròng
```

Nếu lợi thế ròng rất nhỏ, chiến lược khó bền vững khi quy mô tăng hoặc thanh khoản xấu đi.

## 15. Phân rã theo quyết định

Ngoài phân rã theo tài sản, có thể phân rã theo loại quyết định:

```text
Chọn tài sản
Chọn thời điểm
Quy mô vị thế
Tái cân bằng
Phòng vệ
Thực thi
Thoát vị thế
```

Điều này giúp phát hiện ví dụ: ý tưởng phân tích thường đúng nhưng sizing quá lớn làm kết quả xấu.

## 16. Phân rã luận điểm đầu tư

Mỗi vị thế chủ động nên có cây nguyên nhân:

```text
Động lực doanh thu
Biên lợi nhuận
Bảng cân đối
Định giá
Chất xúc tác
```

Khi kết quả khác dự kiến, phải xác định node nào sai. Không nên kết luận chung chung “thị trường vô lý”.

## 17. Điều chỉnh dự báo và hiệu chỉnh xác suất

Nếu thường xuyên dự báo xác suất 70% nhưng chỉ đúng khoảng 50%, bạn đang quá tự tin.

Ghi lại xác suất trước sự kiện và so với kết quả qua nhiều quyết định giúp cải thiện hiệu chỉnh (calibration).

Mục tiêu không phải đúng mọi lần mà là xác suất được ước lượng hợp lý.

## 18. Outcome bias

Một vị thế lời không chứng minh quyết định tốt. Một vị thế lỗ không chứng minh quyết định tệ.

Cần đánh giá:

```text
Thông tin khi ra quyết định có đủ không?
Giả định có hợp lý không?
Xác suất có được hiệu chỉnh không?
Quy mô có phù hợp không?
Quy trình có được tuân thủ không?
```

Sau đó mới dùng kết quả để cập nhật.

## 19. Hindsight bias

Sau khi sự kiện xảy ra, não dễ nghĩ “rõ ràng phải thế”. Điều này làm ta học sai vì xóa mất bất định đã tồn tại trước quyết định.

Nhật ký ex-ante nên được khóa hoặc lưu phiên bản để có thể xem lại mình thực sự biết gì tại thời điểm đó.

## 20. Behavior Gap

Khoảng cách hành vi (behavior gap) là chênh lệch giữa lợi suất sản phẩm và lợi suất nhà đầu tư do thời điểm mua bán, hoảng loạn, FOMO hoặc bỏ kế hoạch.

Một quỹ tốt không giúp ích nếu người dùng liên tục mua ở đỉnh và bán ở đáy.

Thiết kế danh mục phải phù hợp tâm lý thực của người sở hữu, không phải “phiên bản lý tưởng” của họ.

## 21. Nhật ký quyết định

Trước quyết định, ghi:

```text
Dữ kiện
Ước tính
Giả định
Kịch bản
Điều thị trường đang kỳ vọng
Định giá
Quy mô
Chất xúc tác
Điều kiện vô hiệu hóa
```

Sau quyết định, không sửa phần cũ. Chỉ thêm kết quả và đánh giá để tránh viết lại lịch sử.

## 22. Đánh giá hàng tháng

Đánh giá tháng nên ngắn và thiên về vận hành:

```text
Lợi suất tuyệt đối và tương đối
Dòng tiền vào/ra
Vi phạm tỷ trọng
Rủi ro tập trung
Phí / thuế / giao dịch lớn
Sự kiện cần theo dõi
```

Không nên biến mỗi tháng thành lý do thay đổi toàn bộ chiến lược dài hạn.

## 23. Đánh giá hàng quý

Hàng quý có thể đi sâu hơn:

```text
Phân rã theo nhóm tài sản
Phân rã theo nhân tố
Phân rã tiền tệ
Luận điểm chủ động
Sai số dự báo
Chất lượng thực thi
```

Đây là nhịp phù hợp để kiểm tra liệu các giả định kinh tế của danh mục còn đúng hay không.

## 24. Kiểm toán danh mục hàng năm

Hàng năm nên xem lại toàn hệ thống:

```text
Mục tiêu
Thu nhập / nợ
Nghĩa vụ
IPS
Khung thuế
Sản phẩm / môi giới
Chi phí
Tỷ trọng chiến lược
Giới hạn tập trung
Quy trình ra quyết định
```

Mục tiêu là thay đổi khi cuộc sống hoặc cấu trúc thị trường thay đổi thật sự, không phải theo biến động ngắn hạn.

## 25. Khi nào nên thay chiến lược?

Nên xem xét thay đổi khi:

```text
Cơ chế tạo lợi suất không còn tồn tại
Chi phí tăng làm lợi thế ròng âm
Quy mô vượt khả năng thị trường
Đặc điểm rủi ro thay đổi ngoài dự kiến
Mục tiêu / nghĩa vụ cá nhân thay đổi
```

Không nên đổi chỉ vì một giai đoạn ngắn hoạt động kém nhưng vẫn nằm trong phân phối dự kiến.

## 26. Benchmark phải phù hợp

Benchmark nên phản ánh tập cơ hội đầu tư và có thể đầu tư được.

Danh mục cổ phiếu Hàn Quốc không nên so với tiền gửi để tuyên bố “alpha”. Danh mục đa tài sản cũng không nên chỉ so với một chỉ số cổ phiếu nếu mục tiêu và rủi ro khác hẳn.

## 27. Phân rã lợi suất trái phiếu

Với thu nhập cố định, có thể tách:

```text
Thu nhập / Carry
Roll-down
Thay đổi lợi suất phi rủi ro
Thay đổi đường cong
Thay đổi credit spread
Vỡ nợ / thu hồi
FX
```

Điều này giúp biết “trái phiếu lời” vì income, vì duration hay vì spread nén lại.

## 28. Phân rã lợi suất cổ phiếu

Một trực giác đơn giản:

```text
Lợi suất cổ phiếu
≈ Tăng trưởng lợi nhuận
+ Cổ tức / Mua lại ròng
+ Thay đổi hệ số định giá
+ FX nếu có
```

Trong ngắn hạn hệ số định giá có thể chi phối; dài hạn tăng trưởng lợi nhuận trên mỗi cổ phiếu quan trọng hơn.

## 29. Phân rã quỹ ETF

ETF nên được đánh giá qua:

```text
Lợi suất chỉ số
Sai lệch bám chỉ số
Phí
Thuế
FX hedge
Securities lending
Spread / Premium / Discount khi giao dịch
```

Không chỉ nhìn expense ratio.

## 30. Attribution không phải để tự khen hoặc tự trách

Mục tiêu của phân rã kết quả không phải tìm một câu chuyện dễ chịu, mà tìm biến nào thật sự tạo ra lợi suất và biến nào đang làm quy trình rò rỉ.

Nếu phần lớn kết quả đến từ beta thị trường, hãy thừa nhận. Nếu ý tưởng đúng nhưng chi phí thực thi quá cao, sửa thực thi. Nếu sizing sai, sửa ngân sách rủi ro.

## 31. Vòng phản hồi hoàn chỉnh

```text
Quyết định
→ Ghi lại dữ kiện và giả định
→ Kết quả
→ Phân rã kết quả
→ So với xác suất dự báo
→ Xác định lỗi quy trình
→ Thay đổi quy tắc nếu có bằng chứng
→ Quyết định tiếp theo
```

Đây là cách biến đầu tư thành quá trình học có kỷ luật thay vì chuỗi câu chuyện được viết lại sau khi giá đã chạy.