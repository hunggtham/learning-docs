# Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng

Kỹ thuật hiệu năng (performance engineering) không đơn giản là “làm mã chạy nhanh”. Một hệ thống có phân bố độ trễ, thông lượng, mức sử dụng tài nguyên, hàng đợi và hình dạng tải. Muốn tối ưu đúng phải xác định nút thắt cổ chai bằng đo lường và mô hình, thay vì đoán.

## Độ trễ và thông lượng

**Độ trễ (latency)** là thời gian để một thao tác hoặc yêu cầu hoàn thành. **Thông lượng (throughput)** là số thao tác hoàn thành trong một đơn vị thời gian. Hai đại lượng liên quan nhưng không giống nhau: gom lô (batching) có thể tăng thông lượng nhưng làm từng yêu cầu phải chờ lâu hơn; một yêu cầu đơn lẻ có độ trễ thấp không chứng minh hệ thống chịu được thông lượng cao khi có tải.

Chỉ báo cáo giá trị trung bình dễ che giấu phần đuôi của phân bố. Độ trễ p95/p99 đặc biệt quan trọng vì một yêu cầu phân tán gọi nhiều dịch vụ có thể bị chi phối bởi thành phần chậm nhất.

## Mức sử dụng, bão hòa và hàng đợi

Khi tốc độ yêu cầu đến gần năng lực phục vụ, hàng đợi tăng và độ trễ thường tăng phi tuyến. Mô hình M/M/1 đơn giản cho trực giác với mức sử dụng `ρ = λ/μ`; thời gian chờ tăng rất mạnh khi `ρ` tiến gần 1. Hệ thống thực tế không hoàn toàn là M/M/1, nhưng nguyên lý vẫn hữu ích: vận hành liên tục ở 100% năng lực không để lại khoảng trống cho đột biến tải.

Dấu hiệu bão hòa có thể là hàng đợi CPU, hàng đợi đĩa, thời gian chờ connection pool, hàng đợi thread pool hoặc áp lực thu gom rác.

## Định luật Little

Với hệ thống ổn định:

\[
L = \lambda W
\]

`L` là số công việc trung bình đang ở trong hệ thống, `λ` là tốc độ đến hoặc thông lượng ổn định, còn `W` là thời gian trung bình mỗi công việc ở lại. Nếu dịch vụ xử lý 1000 yêu cầu/giây với độ trễ trung bình 0,2 giây, trung bình có khoảng 200 yêu cầu đang tồn tại trong hệ thống.

Định luật này nối giới hạn đồng thời với độ trễ và thông lượng bằng một quan hệ định lượng.

## Nút thắt cổ chai

Thông lượng từ đầu đến cuối bị giới hạn bởi tài nguyên hoặc giai đoạn bị ràng buộc nhất. Tăng tốc phần không phải nút thắt thường đem lại rất ít cải thiện cho toàn hệ thống. Hồ sơ hiệu năng, truy vết phân tán và chỉ số tài nguyên giúp xác định thời gian và năng lực đang bị tiêu tốn ở đâu.

Định luật Amdahl cũng diễn đạt cùng một trực giác: mức tăng tốc tổng thể bị giới hạn bởi phần công việc thực sự được cải thiện.

## Mở rộng theo chiều dọc và chiều ngang

**Mở rộng theo chiều dọc (vertical scaling)** tăng CPU, RAM hoặc thiết bị nhanh hơn cho một máy. **Mở rộng theo chiều ngang (horizontal scaling)** thêm nhiều nút. Mở rộng ngang đòi hỏi tải có thể phân chia, trạng thái được quản lý, có cân bằng tải và có cơ chế phối hợp phân tán; nó không tự động xảy ra chỉ vì thêm máy.

Xử lý yêu cầu không trạng thái thường dễ mở rộng hơn, nhưng dữ liệu bền vững vẫn phải nằm ở đâu đó và cơ sở dữ liệu, cache hoặc mạng vẫn có thể trở thành nút thắt mới.

## Bộ nhớ đệm

Cache giữ dữ liệu hoặc kết quả đắt tiền gần nơi sử dụng hơn. Giá trị của cache phụ thuộc tỷ lệ trúng, chi phí khi trượt, chính sách loại bỏ, độ mới và cơ chế vô hiệu hóa.

Mô hình cache-aside nạp dữ liệu khi trượt; write-through và write-back thay đổi cách đồng bộ ghi. TTL giới hạn thời gian dữ liệu có thể cũ nhưng không bảo đảm cache bị vô hiệu hóa đúng thời điểm nguồn thay đổi.

**Bão cache (cache stampede)** xảy ra khi nhiều máy khách cùng trượt trên một khóa nóng rồi đồng thời tính lại dữ liệu. Các kỹ thuật như single-flight, khóa và thêm nhiễu vào thời điểm hết hạn có thể giảm hiện tượng này.

## Gom lô

**Gom lô (batching)** chia sẻ chi phí cố định giữa nhiều công việc, chẳng hạn system call, vòng khứ hồi mạng, commit giao dịch hoặc khởi chạy GPU. Tuy nhiên lô quá lớn làm tăng thời gian chờ, bộ nhớ và phạm vi ảnh hưởng khi lỗi. Kích thước lô nên được chọn theo mục tiêu thông lượng và độ trễ của hệ thống.

## Nhóm kết nối

Thiết lập kết nối cơ sở dữ liệu hoặc mạng có chi phí, nên **nhóm kết nối (connection pool)** tái sử dụng kết nối và đồng thời giới hạn mức song song. Pool quá nhỏ tạo thời gian chờ; pool quá lớn có thể làm cơ sở dữ liệu quá tải và tăng tranh chấp. Vì vậy pool còn là cơ chế kiểm soát đầu vào (admission control), không chỉ là tối ưu.

## Cân bằng tải

Round-robin, least-connections, consistent hashing và chiến lược có trọng số phân phối công việc theo các giả định khác nhau. Độ trễ hoặc độ cũ của kiểm tra sức khỏe và phiên bám dính (sticky session) ảnh hưởng chất lượng cân bằng. Tính cục bộ và cache có thể khiến affinity có lợi, nhưng cũng có nguy cơ tạo điểm nóng.

## Đo lường hiệu năng

Cần đo với tải gần giống môi trường thực tế, có giai đoạn làm nóng khi JIT hoặc cache ảnh hưởng, theo dõi các phân vị độ trễ, bộ đếm tài nguyên và dấu hiệu bão hòa. Microbenchmark hữu ích để cô lập một thao tác nhưng không thay thế kiểm thử từ đầu đến cuối.

## Mô hình tư duy

> Hiệu năng là **dòng công việc đi qua các tài nguyên hữu hạn**. Tốc độ đến tạo tải; các trung tâm phục vụ tiêu thụ năng lực; hàng đợi giữ phần vượt quá khả năng xử lý; độ trễ cho thấy thời gian chờ. Hãy tối ưu nút thắt và bảo vệ khoảng trống năng lực.

## Những hiểu nhầm thường gặp

**“CPU 100% nghĩa là sử dụng hiệu quả.”** Với tải nhạy độ trễ, điều đó có thể nghĩa hệ thống đã bão hòa và hàng đợi đang tăng nhanh.

**“Có cache thì truy cập dữ liệu trở thành O(1).”** Đường khi trượt, mạng, loại bỏ dữ liệu và nhất quán vẫn tồn tại.

**“Mở rộng ngang sẽ giải quyết nút thắt cơ sở dữ liệu.”** Phân vùng, sao chép và phối hợp trạng thái có thể trở thành những nút thắt mới.

## Kết nối

[Độ phức tạp](../01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) mô hình hóa tốc độ tăng của thuật toán cục bộ; [phân cấp bộ nhớ](../02_computer_architecture/02_memory_hierarchy_and_cache.md) giải thích hiệu năng phần cứng; [khả năng chịu lỗi](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) sử dụng khoảng trống năng lực và cơ chế giảm tải để giữ hệ thống ổn định.
