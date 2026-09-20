# Nền tảng Học máy

**Học máy (Machine Learning — ML / 기계 학습)** xây dựng mô hình từ dữ liệu thay vì viết tay toàn bộ ánh xạ đầu vào → đầu ra. Nhưng “học từ dữ liệu” không có nghĩa mô hình tự tìm ra chân lý. Quá trình học luôn diễn ra trong không gian giả thuyết, hàm mục tiêu, phân bố dữ liệu và quy trình đánh giá do con người hoặc hệ thống thiết kế.

## Học có giám sát

Trong **học có giám sát (supervised learning)**, ta có các ví dụ `(x, y)` và muốn học hàm `f(x) ≈ y`. Phân loại (classification) dự đoán nhóm hoặc nhãn; hồi quy (regression) dự đoán giá trị số.

Quá trình huấn luyện chọn tham số để giảm hàm mất mát trên dữ liệu huấn luyện. Mục tiêu thật sự không phải nhớ dữ liệu đó mà là **khái quát hóa (generalization)** tốt trên dữ liệu chưa thấy nhưng thuộc phân bố mục tiêu.

## Học không giám sát và tự giám sát

**Học không giám sát (unsupervised learning)** tìm cấu trúc khi không có nhãn tường minh, chẳng hạn phân cụm hoặc giảm chiều.

**Học tự giám sát (self-supervised learning)** tạo tín hiệu giám sát từ chính cấu trúc dữ liệu, ví dụ dự đoán token bị che hoặc token tiếp theo. Không cần gán nhãn thủ công, nhưng mục tiêu học vẫn do người thiết kế lựa chọn.

## Đặc trưng và biểu diễn

Học máy truyền thống phụ thuộc nhiều vào **kỹ thuật đặc trưng (feature engineering)**. Học sâu (deep learning) có thể học biểu diễn qua nhiều tầng từ dữ liệu đầu vào gần với dạng thô hơn.

Tuy nhiên cách biểu diễn vẫn quyết định thông tin nào có sẵn cho mô hình. Bỏ timestamp quan trọng hoặc vô tình thêm một đặc trưng làm rò rỉ đáp án có thể thay đổi hành vi mô hình rất mạnh.

## Hàm mất mát

**Hàm mất mát (loss function)** biến sai số dự đoán thành một giá trị vô hướng để tối ưu. Sai số bình phương trung bình phạt phần dư theo bình phương; cross-entropy phù hợp với nhiều bài toán phân loại xác suất dưới các giả định phổ biến.

Loss không đồng nghĩa với chỉ số nghiệp vụ. Một mô hình giảm log-loss vẫn có thể không tối ưu chi phí gian lận hoặc lợi ích y tế nếu ngưỡng quyết định và mức thiệt hại giữa các loại sai khác nhau.

## Tập huấn luyện, xác thực và kiểm thử

Dữ liệu huấn luyện dùng để khớp tham số. Dữ liệu xác thực (validation) dùng để chọn siêu tham số và quyết định mô hình. Dữ liệu kiểm thử (test) dùng để ước lượng khả năng khái quát cuối cùng và nên được giữ độc lập khỏi quá trình tinh chỉnh.

Nếu liên tục xem kết quả test rồi sửa mô hình theo kết quả đó, tập test trên thực tế đã biến thành một tập validation khác.

## Quá khớp và thiếu khớp

**Thiếu khớp (underfitting)** xảy ra khi mô hình quá hạn chế hoặc huấn luyện chưa đủ để nắm được quy luật. **Quá khớp (overfitting)** xảy ra khi mô hình học cả những đặc điểm ngẫu nhiên và nhiễu riêng của dữ liệu huấn luyện nên khái quát kém.

Trực giác thiên lệch–phương sai (bias–variance) giúp suy luận cách năng lực mô hình, regularization và lượng dữ liệu tạo ra sự đánh đổi.

## Điều chuẩn

Các kỹ thuật như phạt L1/L2, dropout, dừng sớm, tăng cường dữ liệu và ràng buộc kiến trúc đều hạn chế mức độ mô hình có thể khớp dữ liệu hoặc đưa giả định có trước vào quá trình học.

**Điều chuẩn (regularization)** không chỉ là “chống overfit”; nó hướng quá trình học về những nghiệm được xem là hợp lý hoặc đơn giản hơn theo cơ chế đã chọn.

## Dịch chuyển phân bố

Mô hình được huấn luyện trên phân bố A có thể thất bại khi phân bố thực tế B thay đổi. Dịch chuyển hiệp biến, dịch chuyển nhãn và trôi khái niệm là những dạng khác nhau của **dịch chuyển phân bố (distribution shift)**.

Giám sát mô hình cần xem phân bố đầu vào, độ tự tin đầu ra, nhãn kết quả khi có và chỉ số nghiệp vụ, thay vì chỉ theo dõi CPU hoặc lỗi hệ thống.

## Rò rỉ dữ liệu

**Rò rỉ dữ liệu (data leakage)** xảy ra khi đặc trưng huấn luyện chứa thông tin không tồn tại tại thời điểm dự đoán, hoặc cách chia dữ liệu làm cùng một thực thể hay cùng khoảng thời gian xuất hiện ở cả train và test theo cách không thực tế.

Khi đó chỉ số đánh giá có thể rất cao nhưng mô hình thất bại khi triển khai. Chiến lược chia dữ liệu phải phản ánh dòng thời gian và cấu trúc thực thể của môi trường sử dụng thật.

## Những hiểu nhầm thường gặp

**“Càng nhiều dữ liệu càng tốt.”** Không luôn đúng. Dữ liệu sai phân bố, nhãn nhiễu hoặc leakage có thể làm mô hình tệ hơn hoặc tạo cảm giác đánh giá sai lệch.

**“Accuracy cao nghĩa mô hình tốt.”** Không luôn đúng. Mất cân bằng lớp và chi phí sai lệch không đối xứng có thể làm accuracy trở thành chỉ số không phù hợp.

**“Mô hình học đúng mục tiêu mà chúng ta muốn.”** Không chính xác. Nó tối ưu một hàm mất mát đại diện trên dữ liệu; khoảng cách giữa đại diện và mục tiêu thật là nguồn lỗi quan trọng.

## Mô hình tư duy

> Học máy là **tối ưu trên dữ liệu dưới một tập giả định**. Mục tiêu là khả năng khái quát chứ không phải khớp dữ liệu huấn luyện; quy trình đánh giá phải mô phỏng càng gần thực tế triển khai càng tốt.

## Kết nối

Xem [thống kê và suy luận](../../../mathematics/06_probability_statistics/05_descriptive_and_inferential_statistics.md), [tối ưu hóa](../../../mathematics/08_optimization_numerical/00_optimization.md), [mạng nơ-ron](./03_neural_networks_and_representation_learning.md) và [đánh giá AI](./04_ai_evaluation_data_and_responsibility.md).