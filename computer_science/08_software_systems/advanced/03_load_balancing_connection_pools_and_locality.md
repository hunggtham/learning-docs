# Thuật toán cân bằng tải, nhóm kết nối và tính cục bộ

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Load balancing, connection pools và locality**. Route đi từ round-robin/weighted routing → least-connections/in-flight load → pool limits/queueing → locality/consistent hashing → health, retry và failure, để phân phối tải không tạo hotspot mới.

Bộ cân bằng tải (load balancer / 로드 밸런서) không đơn giản là “chia đều số yêu cầu”. Mục tiêu thực tế là phân phối công việc sao cho tài nguyên không tạo điểm nóng, giữ độ trễ ổn định và tận dụng tính cục bộ mà không tạo mức phụ thuộc quá chặt.

## Round robin và round robin có trọng số

Round robin phù hợp khi các yêu cầu có chi phí gần nhau và các backend có năng lực tương đương. Nếu kích thước máy khác nhau, **round robin có trọng số (weighted round robin)** có thể phản ánh năng lực tương đối.

Tuy nhiên số lượng yêu cầu không bằng lượng công việc. Một truy vấn báo cáo chạy 5 giây và một health check 2 ms đều chỉ được đếm là một yêu cầu.

> **Nối mạch:** **Ít kết nối nhất và ít yêu cầu đang xử lý nhất** nối từ **Round robin và round robin có trọng số** sang **Sức mạnh của hai lựa chọn**, vì cơ chế trước tạo đầu vào cho bước sau.

## Ít kết nối nhất và ít yêu cầu đang xử lý nhất

**Least connections** dùng số kết nối đang hoạt động như đại diện cho tải. Với HTTP/2 ghép nhiều luồng hoặc khi có liên kết (connection / 연결) pool, số kết nối có thể không phản ánh số yêu cầu đang chạy đồng thời.

**Least outstanding requests** gần với lượng công việc hơn nhưng vẫn không biết trước chi phí của yêu cầu tương lai. Thuật toán thích nghi có thể dùng độ trễ và tải đã quan sát để điều chỉnh.

> **Nối mạch:** **Sức mạnh của hai lựa chọn** nối từ **Ít kết nối nhất và ít yêu cầu đang xử lý nhất** sang **Nhóm kết nối**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sức mạnh của hai lựa chọn

Chọn ngẫu nhiên hai backend rồi gửi yêu cầu tới backend nhẹ hơn thường tạo cân bằng rất tốt với chi phí thấp. Trực giác quan trọng là chỉ cần thêm một lượng nhỏ trạng thái và so sánh đã giảm điểm nóng mạnh hơn so với chọn ngẫu nhiên thuần túy.

> **Nối mạch:** **Nhóm kết nối** nối từ **Sức mạnh của hai lựa chọn** sang **Hàng đợi nằm ở đâu?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Nhóm kết nối

Mở kết nối TCP, TLS hoặc cơ sở dữ liệu mới cho mỗi yêu cầu rất đắt. **Nhóm kết nối (connection pool)** chia sẻ chi phí bắt tay qua nhiều yêu cầu và đồng thời giới hạn mức đồng thời gửi xuống hệ thống phía sau.

Kích thước pool không phải càng lớn càng tốt. Pool quá lớn có thể đẩy cơ sở dữ liệu vượt năng lực; pool quá nhỏ tạo hàng đợi tại ứng dụng. Vì vậy pool thực chất cũng là một ranh giới kiểm soát đầu vào (admission control).

> **Nối mạch:** **Hàng đợi nằm ở đâu?** nối từ **Nhóm kết nối** sang **Tính cục bộ**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hàng đợi nằm ở đâu?

Khi yêu cầu phải chờ, hàng đợi có thể nằm tại bộ cân bằng tải, pool của ứng dụng, luồng thực thi (thread / 스레드) pool hoặc cơ sở dữ liệu. Nhiều hàng đợi nối tiếp làm độ trễ phần đuôi khó quan sát và âm thầm tiêu hết ngân sách hết thời gian chờ (timeout / 타임아웃).

Thiết kế thường dễ kiểm soát hơn khi có hàng đợi hữu hạn rõ ràng gần tài nguyên nút thắt và từ chối hoặc giảm tải sớm khi năng lực đã cạn.

> **Nối mạch:** **Tính cục bộ** nối từ **Hàng đợi nằm ở đâu?** sang **Phiên bám dính**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tính cục bộ

Tính cục bộ của bộ nhớ đệm (cache / 캐시), vùng triển khai và phân mảnh dữ liệu có thể làm một backend “gần” yêu cầu hơn. **Băm nhất quán (consistent hashing)** hoặc định tuyến nhận biết vị trí giúp giảm trượt bộ nhớ đệm (cache / 캐시) và lưu lượng xuyên vùng.

Nhưng ép locality quá cứng có thể tạo điểm nóng khi một khóa hoặc người dùng trở nên quá tải. Hệ thống cần đường thoát để tái cân bằng khi giả định cục bộ không còn phù hợp.

> **Nối mạch:** **Phiên bám dính** nối từ **Tính cục bộ** sang **Kiểm tra sức khỏe**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phiên bám dính

**Phiên bám dính (sticky session / session affinity)** đơn giản hóa trạng thái phiên trong bộ nhớ nhưng làm chuyển đổi khi lỗi, tái cân bằng và co giãn khó hơn. Đưa trạng thái phiên ra kho dùng chung hoặc dùng đơn vị từ (token / 토큰) không trạng thái tạo những đánh đổi khác về nhất quán và bảo mật.

> **Nối mạch:** **Kiểm tra sức khỏe** nối từ **Phiên bám dính** sang **Mô hình tư duy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Kiểm tra sức khỏe

Backend trả lời được TCP hoặc endpoint `/health` không có nghĩa nó còn đủ khỏe để nhận thêm tải. Một nút đã quá tải vẫn có thể báo “healthy”. Tín hiệu thụ động như độ trễ, tỷ lệ lỗi và phát hiện điểm bất thường giúp định tuyến phản ánh điều kiện khi chạy tốt hơn.

> **Nối mạch:** **Mô hình tư duy** tổng hợp từ **Kiểm tra sức khỏe**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Mô hình tư duy

> Cân bằng tải là một vòng điều khiển giữa nhu cầu và năng lực không đồng nhất. Thuật toán định tuyến, liên kết (connection / 연결) pool và locality cùng quyết định hàng đợi hình thành ở đâu. Mục tiêu không phải làm số yêu cầu trên mỗi máy trông đẹp, mà là giữ từng nút thắt trong vùng vận hành an toàn.

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
