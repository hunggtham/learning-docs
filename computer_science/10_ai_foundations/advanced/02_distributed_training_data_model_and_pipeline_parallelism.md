# Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống

Mô hình hiện đại có thể quá lớn hoặc quá chậm để huấn luyện trên một bộ tăng tốc duy nhất. **Huấn luyện phân tán (distributed training)** chia tính toán và trạng thái qua nhiều GPU hoặc nhiều nút, nhưng mức tăng tốc bị giới hạn bởi giao tiếp, đồng bộ và mất cân bằng tải chứ không chỉ phụ thuộc số thiết bị.

## Song song dữ liệu

Trong **song song dữ liệu (data parallelism)**, mỗi worker giữ một bản sao mô hình và xử lý mini-batch khác nhau. Sau bước lan truyền ngược, gradient được tổng hợp, thường bằng phép tập thể `all-reduce`, để các bản sao cập nhật nhất quán.

Nếu lượng tính toán mỗi bước nhỏ so với lượng dữ liệu gradient phải truyền, thêm GPU sẽ đem lại lợi ích giảm dần. Kích thước batch cũng thường tăng theo mức song song và có thể thay đổi động lực tối ưu hóa.

## Song song mô hình và tensor

Khi mô hình không vừa một thiết bị, các tensor hoặc phép toán ma trận được chia nhỏ giữa nhiều thiết bị. Một tầng có thể cần trao đổi dữ liệu tập thể giữa các GPU trong cả bước tiến và bước lùi.

Lúc này đường liên kết băng thông cao trở thành tài nguyên quan trọng. Cách phân chia tốt phải vừa cân bằng lượng tính toán vừa giảm khối lượng giao tiếp.

## Song song đường ống

Trong **song song đường ống (pipeline parallelism)**, các tầng được chia thành nhiều giai đoạn trên các thiết bị khác nhau. Các micro-batch đi qua hệ thống giống dây chuyền lắp ráp. Nếu một giai đoạn chậm hơn, toàn bộ đường ống bị giới hạn bởi giai đoạn đó; phần đầu và cuối lịch chạy còn tạo **khoảng trống đường ống (pipeline bubble)** khiến thiết bị chưa được sử dụng hết.

Chiến lược lập lịch khác nhau sẽ thay đổi lượng bộ nhớ cần, độ trễ trạng thái và mức sử dụng thiết bị.

## Trạng thái bộ tối ưu và phân mảnh trạng thái

Huấn luyện không chỉ lưu tham số mô hình. Gradient và trạng thái của bộ tối ưu như các moment của Adam có thể chiếm dung lượng nhiều lần kích thước tham số. Các kỹ thuật kiểu ZeRO phân tán trạng thái bộ tối ưu, gradient và tham số để giảm lượng bộ nhớ trên mỗi worker.

Khi tính ngân sách bộ nhớ phải tính cả activation, bộ đệm tạm và vùng làm việc cho giao tiếp, không chỉ kích thước file checkpoint.

## Giao tiếp tập thể

`all-reduce`, `all-gather` và `reduce-scatter` là các phép giao tiếp tập thể quan trọng. Thuật toán nhận biết topology cố tận dụng băng thông nhanh trong cùng máy, chẳng hạn NVLink, trước khi truyền qua mạng giữa các nút.

Một worker chậm có thể kéo dài toàn bộ bước đồng bộ vì các worker khác phải chờ phép tập thể hoàn thành.

## Khả năng chịu lỗi

Huấn luyện kéo dài nhiều ngày làm xác suất một nút gặp lỗi tăng lên. Checkpoint cần lưu đủ trạng thái mô hình, bộ tối ưu, bộ lập lịch và trạng thái ngẫu nhiên để có thể tiếp tục gần với quỹ đạo huấn luyện trước đó.

Checkpoint quá thường xuyên tốn I/O; quá thưa làm mất nhiều giờ tính toán khi xảy ra lỗi.

## Hiệu quả mở rộng

Nếu 8 GPU chỉ nhanh gấp 5 lần 1 GPU, hiệu quả mở rộng xấp xỉ 62,5%. Phần mất đi đến từ giao tiếp, thời gian rỗi và pipeline bubble, đường cấp dữ liệu đầu vào và đồng bộ.

Định luật Amdahl cung cấp mô hình tư duy hữu ích: phần tuần tự và chi phí phối hợp cuối cùng sẽ giới hạn mức tăng tốc.

## Mô hình tư duy

> Huấn luyện phân tán là bài toán phân chia **tính toán, bộ nhớ và giao tiếp**. Thêm bộ tăng tốc chỉ hữu ích khi mỗi thiết bị có đủ công việc và interconnect không biến đồng bộ thành nút thắt cổ chai.