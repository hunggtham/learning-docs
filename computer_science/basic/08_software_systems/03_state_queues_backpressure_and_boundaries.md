# Trạng thái, hàng đợi, áp lực ngược và ranh giới hệ thống

Nhiều hệ thống thực tế có thể được hiểu bằng ba thành phần: bên tạo công việc, hàng đợi hoặc bộ đệm, và bên xử lý công việc. Dữ liệu hoặc sự kiện di chuyển giữa các thành phần qua những ranh giới rõ ràng. **Hàng đợi (queue)** giúp hấp thụ tải tăng đột biến và tách tốc độ của bên gửi khỏi bên nhận, nhưng nó không tự tạo thêm năng lực xử lý. Nếu không có **áp lực ngược (backpressure)** hoặc cơ chế giảm tải, tình trạng quá tải chỉ bị chuyển thành độ trễ và lượng dữ liệu chờ ngày càng lớn.

## Tại sao cần hàng đợi?

Bên tạo công việc có thể tạm thời tạo dữ liệu nhanh hơn bên xử lý. Hàng đợi lưu phần chênh lệch theo thời gian. Nó cũng tách một phần tính sẵn sàng: nếu broker đủ bền vững, bên gửi vẫn có thể đưa thông điệp vào hàng đợi trong lúc hệ thống phía sau tạm thời không hoạt động.

Tuy nhiên, nếu tốc độ đến `λ` liên tục lớn hơn tốc độ phục vụ `μ`, hàng đợi sẽ tăng không giới hạn. Một hệ thống ổn định cần năng lực xử lý dài hạn lớn hơn tải được chấp nhận, hoặc phải có chính sách từ chối hay giảm chất lượng dịch vụ.

## Hàng đợi có giới hạn và không giới hạn

Hàng đợi không giới hạn biến quá tải thành độ trễ ngày càng lớn và cuối cùng có thể làm cạn bộ nhớ hoặc dung lượng đĩa. **Hàng đợi có giới hạn (bounded queue)** buộc hệ thống phải có chính sách rõ ràng: chặn bên gửi, từ chối công việc mới, bỏ dữ liệu cũ hoặc mới, ưu tiên một số loại công việc hoặc chuyển sang nơi lưu trữ khác.

Lựa chọn phụ thuộc ngữ nghĩa nghiệp vụ. Mất một số metric có thể chấp nhận được; mất lệnh thanh toán thường không thể chấp nhận.

## Áp lực ngược

**Áp lực ngược (backpressure)** truyền tín hiệu ngược lên phía trước rằng bên xử lý không theo kịp. Cửa sổ nhận và điều khiển tắc nghẽn của TCP, cơ chế yêu cầu dữ liệu của Reactive Streams, channel có giới hạn và hàng đợi của thread pool đều là các ví dụ.

Nếu tầng phía trước bỏ qua tín hiệu rồi tự tích dữ liệu trong bộ nhớ, vấn đề quá tải chưa được giải quyết. Áp lực ngược cần lan đủ xa trong chuỗi xử lý hoặc phải kết thúc bằng một chính sách giới hạn, từ chối hay loại bỏ rõ ràng.

## Ngữ nghĩa truyền thông điệp

**Tối đa một lần (at-most-once)** có thể làm mất thông điệp nhưng tránh bản sao do thử lại. **Ít nhất một lần (at-least-once)** cho phép thử lại nên có thể tạo thông điệp trùng. Hiệu ứng **chính xác một lần (exactly-once)** đòi hỏi phối hợp hoặc loại trùng mạnh hơn và luôn phải xác định phạm vi bảo đảm.

Việc broker xác nhận đã giao thông điệp không đồng nghĩa giao dịch nghiệp vụ đã hoàn thành. Ví dụ consumer có thể ghi dữ liệu vào cơ sở dữ liệu rồi bị lỗi trước khi gửi `ack`; thông điệp sẽ được giao lại. Bộ xử lý lũy đẳng (idempotent handler), outbox và inbox là các mẫu thường dùng để xử lý tình huống này.

## Thứ tự

Thứ tự toàn cục tuyệt đối có chi phí cao và thường không cần thiết. Nhật ký được phân vùng có thể bảo đảm thứ tự trong từng partition hoặc khóa. Nếu bất biến nghiệp vụ chỉ yêu cầu các thao tác của cùng một tài khoản theo thứ tự, phân vùng theo tài khoản có thể đã đủ.

Xử lý đồng thời còn có thể làm thứ tự hoàn thành khác thứ tự lấy thông điệp. Vì vậy hợp đồng về thứ tự phải nói rõ đang bảo đảm thứ tự đưa vào hàng, thứ tự giao, thứ tự xử lý hay thứ tự commit.

## Vị trí của trạng thái

Trạng thái có thể nằm ở client, bộ nhớ ứng dụng, cache, cơ sở dữ liệu, nhật ký hoặc dịch vụ bên ngoài. Vị trí này ảnh hưởng trực tiếp tới tính sẵn sàng, khả năng mở rộng và phục hồi. Phiên người dùng nằm trong bộ nhớ cục bộ khiến việc mở rộng ngang cần định tuyến dính (sticky routing) hoặc sao chép; kho phiên bên ngoài lại thêm một phụ thuộc mạng.

Một **dịch vụ không trạng thái (stateless service)** thường chỉ có nghĩa trạng thái bền vững hoặc trạng thái phiên đã được đưa ra ngoài, chứ không phải tiến trình hoàn toàn không có trạng thái tạm thời.

## Nhật ký sự kiện và trạng thái

**Event sourcing** lưu chuỗi sự kiện miền làm nguồn dữ liệu chính và dựng trạng thái hiện tại bằng cách phát lại hoặc gấp các sự kiện. Cách này hỗ trợ lịch sử và kiểm toán nhưng làm tiến hóa schema, chi phí phát lại, tính đúng đắn của sự kiện và hiệu ứng phụ bên ngoài trở nên phức tạp. Không phải hệ thống nào cũng cần event sourcing.

**Change Data Capture (CDC)** phát các thay đổi trong cơ sở dữ liệu tới chỉ mục, hệ thống phân tích hoặc dịch vụ phía sau. Độ trễ nhất quán phát sinh từ quá trình này phải được chấp nhận và quan sát.

## Áp lực ngược và giới hạn tốc độ

**Giới hạn tốc độ (rate limiting)** bảo vệ ranh giới bằng cách giới hạn lượng yêu cầu được nhận từ một danh tính hoặc toàn hệ thống. Backpressure phản ánh áp lực động từ phía xử lý. Hai cơ chế có thể cùng tồn tại: rate limiter ngăn lạm dụng và tải vượt ngưỡng; backpressure phản ứng với năng lực hiện tại của hệ thống phía sau.

## Hàng đợi và bão thử lại

Khi một phụ thuộc chậm lại, hàng đợi tăng. Timeout có thể kích hoạt thử lại; thử lại làm tốc độ yêu cầu tăng; tải tăng lại khiến phụ thuộc chậm hơn. Đây là vòng phản hồi có thể tạo **bão thử lại (retry storm)**. Circuit breaker, ngân sách thử lại, hàng đợi có giới hạn và deadline giúp cắt vòng phản hồi này.

## Mô hình tư duy

> Hàng đợi là **thời gian chờ được lưu lại**. Nó hấp thụ tải tăng đột biến, không giải quyết thiếu năng lực kéo dài. Mỗi hàng đợi cần có giới hạn dung lượng, chính sách nhận tải, ngữ nghĩa lỗi, phạm vi thứ tự và khả năng quan sát.

## Những hiểu lầm thường gặp

**“Hàng đợi bất đồng bộ làm hệ thống nhanh hơn.”** Nó thay đổi thời điểm bên gọi phải chờ và làm tải mượt hơn; tổng lượng công việc và năng lực xử lý không tự tăng.

**“Kafka hoặc RabbitMQ bảo đảm exactly-once cho mọi thứ.”** Bảo đảm của broker luôn có phạm vi; hiệu ứng phụ trên cơ sở dữ liệu hoặc API bên ngoài vẫn cần phối hợp hoặc tính lũy đẳng.

**“Hàng đợi không giới hạn an toàn hơn vì không từ chối.”** Nó thường chỉ trì hoãn lỗi cho tới khi độ trễ hoặc tài nguyên bị cạn kiệt.

## Kết nối

[Hàng đợi tuyến tính](../01_algorithms_data_structures/03_linear_data_structures.md) là lớp trừu tượng cục bộ; [áp lực ngược trong TCP](../06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) là ví dụ ở tầng mạng; [khả năng chịu lỗi](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) sử dụng giảm tải và circuit breaker; phần [thời gian và tính lũy đẳng](./04_time_serialization_and_idempotency.md) giải thích cách xử lý hiệu ứng của việc thử lại.