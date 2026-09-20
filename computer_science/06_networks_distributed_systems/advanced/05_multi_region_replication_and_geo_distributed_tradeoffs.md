# Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý

Khi các bản sao nằm ở nhiều vùng địa lý, tốc độ ánh sáng và cấu trúc mạng trở thành một phần của mô hình nhất quán. Không giao thức nào có thể biến một vòng khứ hồi Seoul–Virginia thành truy cập bộ nhớ cục bộ. Kiến trúc phải quyết định thao tác nào cần chờ phối hợp xuyên vùng và thao tác nào có thể xử lý tại chỗ rồi hòa giải sau.

## Sàn độ trễ do khoảng cách vật lý

Vòng khứ hồi mạng giữa các vùng tạo **giới hạn dưới của độ trễ (latency floor)** cho giao thức đồng bộ. Nếu một lần ghi cần quorum trải trên nhiều châu lục, người dùng phải trả ít nhất một phần chi phí của các vòng truyền mạng đó.

Tối ưu phần mềm có thể giảm chi phí xử lý nhưng không loại bỏ khoảng cách vật lý. Vì vậy vị trí triển khai là quyết định kiến trúc, không chỉ là chi tiết vận hành.

## Sao chép đồng bộ và bất đồng bộ

**Sao chép đồng bộ (synchronous replication)** giảm mục tiêu mất dữ liệu RPO vì chỉ xác nhận ghi sau khi các bản sao cần thiết đã lưu bền vững, nhưng làm tăng độ trễ và có thể giảm khả năng phục vụ khi vùng từ xa không truy cập được.

**Sao chép bất đồng bộ (asynchronous replication)** cho phép xác nhận tại vùng cục bộ nhanh hơn, nhưng khi chuyển vùng có thể mất các lần ghi gần nhất hoặc phải xử lý xung đột.

RPO và RTO phải gắn với ngữ nghĩa sao chép thật sự, không chỉ với con số SLA trong tài liệu tiếp thị.

## Sao chép địa lý với một leader

Một leader toàn cục đơn giản hóa thứ tự ghi nhưng máy khách ở xa leader phải chịu độ trễ cao. Replica đọc tại địa phương giảm độ trễ đọc nhưng có thể trả dữ liệu cũ.

Bảo đảm “đọc thấy lần ghi của chính mình” (read-your-writes) có thể cần giữ phiên tại một vùng, dùng token phiên bản hoặc định tuyến yêu cầu đọc tới replica đã theo kịp.

## Nhiều leader

Cho phép mỗi vùng nhận ghi cục bộ cải thiện khả năng phục vụ và độ trễ, nhưng cập nhật đồng thời tạo xung đột. Ràng buộc duy nhất, bộ đếm và tồn kho trở nên khó vì bất biến có thể bị vi phạm trước khi các vùng trao đổi dữ liệu.

Giải quyết xung đột cần ngữ nghĩa của miền nghiệp vụ, không nên chỉ áp dụng máy móc “timestamp mới nhất thắng”.

## Chủ quyền dữ liệu và vị trí lưu trữ

Kiến trúc địa lý còn bị ràng buộc bởi yêu cầu cư trú dữ liệu và tuân thủ: dữ liệu nào được phép rời một khu vực pháp lý, bản sao lưu nằm ở đâu, log có chứa dữ liệu cá nhân hay không. Vì vậy chính sách vị trí vừa là vấn đề hiệu năng vừa là vấn đề quản trị.

## Chuyển đổi khi lỗi

**Chuyển đổi dự phòng (failover)** không chỉ là nâng một replica thành primary. TTL của DNS và cache, connection pool, máy khách còn giữ thông tin cũ, độ trễ sao chép và split-brain đều ảnh hưởng quá trình.

Khóa quyền ghi của primary cũ bằng cơ chế fencing là bước quan trọng để tránh hai writer cùng có thẩm quyền. Xem thêm: [Lease, fencing token và ngăn split-brain](./02_leases_fencing_tokens_and_split_brain_prevention.md).

## Active-active không đồng nghĩa không bao giờ gián đoạn

Hai vùng cùng hoạt động vẫn có thể chia sẻ dependency, control plane toàn cục hoặc đường dữ liệu sao chép. Một lỗi phần mềm có tương quan có thể làm cả hai vùng cùng hỏng. Đánh giá khả năng sẵn sàng cần phân tích miền lỗi (failure domain), không chỉ đếm số vùng.

## Phân vùng theo địa lý

Nếu người dùng hoặc dữ liệu có tính cục bộ tự nhiên, phân vùng theo “vùng nhà” có thể giữ phần lớn giao dịch ở địa phương và chỉ đi xuyên vùng cho thao tác thật sự cần thiết. Cách này thường hiệu quả hơn việc sao chép mọi lần ghi tới mọi nơi.

## Mô hình tư duy

> Thiết kế phân tán theo địa lý là bài toán phân bổ sự phối hợp theo khoảng cách. Đồng thuận toàn cục mạnh hơn phải trả bằng độ trễ và khả năng phục vụ; tự chủ cục bộ phải trả bằng dữ liệu cũ và xung đột. Kiến trúc tốt chỉ đặt phối hợp toàn cục tại những bất biến thật sự cần nó và giữ phần còn lại gần người dùng hoặc dữ liệu.