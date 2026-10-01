# Thuật toán cân bằng tải, nhóm kết nối và tính cục bộ

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Thuật toán cân bằng tải, nhóm kết nối và tính cục bộ**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Round robin và round robin có trọng số** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Ít kết nối nhất và ít yêu cầu đang xử lý nhất** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Bộ cân bằng tải (load balancer / 로드 밸런서) không đơn giản là “chia đều số yêu cầu”. Mục tiêu thực tế là phân phối công việc sao cho tài nguyên không tạo điểm nóng, giữ độ trễ ổn định và tận dụng tính cục bộ mà không tạo mức phụ thuộc quá chặt.

## Round robin và round robin có trọng số

Round robin phù hợp khi các yêu cầu có chi phí gần nhau và các backend có năng lực tương đương. Nếu kích thước máy khác nhau, **round robin có trọng số (weighted round robin)** có thể phản ánh năng lực tương đối.

Tuy nhiên số lượng yêu cầu không bằng lượng công việc. Một truy vấn báo cáo chạy 5 giây và một health check 2 ms đều chỉ được đếm là một yêu cầu.

> **Chuyển mạch:** Trong **Thuật toán cân bằng tải, nhóm kết nối và tính cục bộ**, **Ít kết nối nhất và ít yêu cầu đang xử lý nhất** tiếp nhận điểm tựa từ **Round robin và round robin có trọng số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sức mạnh của hai lựa chọn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ít kết nối nhất và ít yêu cầu đang xử lý nhất

**Least connections** dùng số kết nối đang hoạt động như đại diện cho tải. Với HTTP/2 ghép nhiều luồng hoặc khi có liên kết (connection / 연결) pool, số kết nối có thể không phản ánh số yêu cầu đang chạy đồng thời.

**Least outstanding requests** gần với lượng công việc hơn nhưng vẫn không biết trước chi phí của yêu cầu tương lai. Thuật toán thích nghi có thể dùng độ trễ và tải đã quan sát để điều chỉnh.

> **Chuyển mạch:** Ở chặng này của **Thuật toán cân bằng tải, nhóm kết nối và tính cục bộ**, **Sức mạnh của hai lựa chọn** tiếp nhận điểm tựa từ **Ít kết nối nhất và ít yêu cầu đang xử lý nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhóm kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sức mạnh của hai lựa chọn

Chọn ngẫu nhiên hai backend rồi gửi yêu cầu tới backend nhẹ hơn thường tạo cân bằng rất tốt với chi phí thấp. Trực giác quan trọng là chỉ cần thêm một lượng nhỏ trạng thái và so sánh đã giảm điểm nóng mạnh hơn so với chọn ngẫu nhiên thuần túy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thuật toán cân bằng tải, nhóm kết nối và tính cục bộ**, **Nhóm kết nối** tiếp nhận điểm tựa từ **Sức mạnh của hai lựa chọn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàng đợi nằm ở đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhóm kết nối

Mở kết nối TCP, TLS hoặc cơ sở dữ liệu mới cho mỗi yêu cầu rất đắt. **Nhóm kết nối (connection pool)** chia sẻ chi phí bắt tay qua nhiều yêu cầu và đồng thời giới hạn mức đồng thời gửi xuống hệ thống phía sau.

Kích thước pool không phải càng lớn càng tốt. Pool quá lớn có thể đẩy cơ sở dữ liệu vượt năng lực; pool quá nhỏ tạo hàng đợi tại ứng dụng. Vì vậy pool thực chất cũng là một ranh giới kiểm soát đầu vào (admission control).

> **Chuyển mạch:** Trong **Thuật toán cân bằng tải, nhóm kết nối và tính cục bộ**, **Hàng đợi nằm ở đâu?** tiếp nhận điểm tựa từ **Nhóm kết nối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính cục bộ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàng đợi nằm ở đâu?

Khi yêu cầu phải chờ, hàng đợi có thể nằm tại bộ cân bằng tải, pool của ứng dụng, luồng thực thi (thread / 스레드) pool hoặc cơ sở dữ liệu. Nhiều hàng đợi nối tiếp làm độ trễ phần đuôi khó quan sát và âm thầm tiêu hết ngân sách hết thời gian chờ (timeout / 타임아웃).

Thiết kế thường dễ kiểm soát hơn khi có hàng đợi hữu hạn rõ ràng gần tài nguyên nút thắt và từ chối hoặc giảm tải sớm khi năng lực đã cạn.

> **Chuyển mạch:** Ở chặng này của **Thuật toán cân bằng tải, nhóm kết nối và tính cục bộ**, **Tính cục bộ** tiếp nhận điểm tựa từ **Hàng đợi nằm ở đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phiên bám dính** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính cục bộ

Tính cục bộ của bộ nhớ đệm (cache / 캐시), vùng triển khai và phân mảnh dữ liệu có thể làm một backend “gần” yêu cầu hơn. **Băm nhất quán (consistent hashing)** hoặc định tuyến nhận biết vị trí giúp giảm trượt bộ nhớ đệm (cache / 캐시) và lưu lượng xuyên vùng.

Nhưng ép locality quá cứng có thể tạo điểm nóng khi một khóa hoặc người dùng trở nên quá tải. Hệ thống cần đường thoát để tái cân bằng khi giả định cục bộ không còn phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thuật toán cân bằng tải, nhóm kết nối và tính cục bộ**, **Phiên bám dính** tiếp nhận điểm tựa từ **Tính cục bộ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiểm tra sức khỏe** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phiên bám dính

**Phiên bám dính (sticky session / session affinity)** đơn giản hóa trạng thái phiên trong bộ nhớ nhưng làm chuyển đổi khi lỗi, tái cân bằng và co giãn khó hơn. Đưa trạng thái phiên ra kho dùng chung hoặc dùng đơn vị từ (token / 토큰) không trạng thái tạo những đánh đổi khác về nhất quán và bảo mật.

> **Chuyển mạch:** Trong **Thuật toán cân bằng tải, nhóm kết nối và tính cục bộ**, **Kiểm tra sức khỏe** tiếp nhận điểm tựa từ **Phiên bám dính** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm tra sức khỏe

Backend trả lời được TCP hoặc endpoint `/health` không có nghĩa nó còn đủ khỏe để nhận thêm tải. Một nút đã quá tải vẫn có thể báo “healthy”. Tín hiệu thụ động như độ trễ, tỷ lệ lỗi và phát hiện điểm bất thường giúp định tuyến phản ánh điều kiện khi chạy tốt hơn.

> **Chuyển mạch:** Ở chặng này của **Thuật toán cân bằng tải, nhóm kết nối và tính cục bộ**, **Mô hình tư duy** gom các mảnh từ **Kiểm tra sức khỏe** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Cân bằng tải là một vòng điều khiển giữa nhu cầu và năng lực không đồng nhất. Thuật toán định tuyến, liên kết (connection / 연결) pool và locality cùng quyết định hàng đợi hình thành ở đâu. Mục tiêu không phải làm số yêu cầu trên mỗi máy trông đẹp, mà là giữ từng nút thắt trong vùng vận hành an toàn.

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
