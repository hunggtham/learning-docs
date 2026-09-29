# Trạng thái, hàng đợi, áp lực ngược và ranh giới hệ thống

> **Mạch đọc:** Đọc **Trạng thái, hàng đợi, áp lực ngược và ranh giới hệ thống** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Tại sao cần hàng đợi?** sang **Hàng đợi có giới hạn và không giới hạn**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Nhiều hệ thống thực tế có thể được hiểu bằng ba thành phần: bên tạo công việc, hàng đợi hoặc bộ đệm, và bên xử lý công việc. Dữ liệu hoặc sự kiện di chuyển giữa các thành phần qua những ranh giới rõ ràng. **hàng đợi (queue / 큐)** giúp hấp thụ tải tăng đột biến và tách tốc độ của bên gửi khỏi bên nhận, nhưng nó không tự tạo thêm năng lực xử lý. Nếu không có **áp lực ngược (backpressure)** hoặc cơ chế giảm tải, tình trạng quá tải chỉ bị chuyển thành độ trễ và lượng dữ liệu chờ ngày càng lớn.

## Tại sao cần hàng đợi?

Bên tạo công việc có thể tạm thời tạo dữ liệu nhanh hơn bên xử lý. Hàng đợi lưu phần chênh lệch theo thời gian. Nó cũng tách một phần tính sẵn sàng: nếu broker đủ bền vững, bên gửi vẫn có thể đưa thông điệp vào hàng đợi trong lúc hệ thống phía sau tạm thời không hoạt động.

Tuy nhiên, nếu tốc độ đến `λ` liên tục lớn hơn tốc độ phục vụ `μ`, hàng đợi sẽ tăng không giới hạn. Một hệ thống ổn định cần năng lực xử lý dài hạn lớn hơn tải được chấp nhận, hoặc phải có chính sách từ chối hay giảm chất lượng dịch vụ.


> **Chuyển mạch:** Từ **Tại sao cần hàng đợi?**, ta sang **Hàng đợi có giới hạn và không giới hạn** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hàng đợi có giới hạn và không giới hạn

Hàng đợi không giới hạn biến quá tải thành độ trễ ngày càng lớn và cuối cùng có thể làm cạn bộ nhớ hoặc dung lượng đĩa. **Hàng đợi có giới hạn (bounded queue)** buộc hệ thống phải có chính sách rõ ràng: chặn bên gửi, từ chối công việc mới, bỏ dữ liệu cũ hoặc mới, ưu tiên một số loại công việc hoặc chuyển sang nơi lưu trữ khác.

Lựa chọn phụ thuộc ngữ nghĩa nghiệp vụ. Mất một số chỉ số (metric / 지표) có thể chấp nhận được; mất lệnh thanh toán thường không thể chấp nhận.


> **Chuyển mạch:** Từ **Hàng đợi có giới hạn và không giới hạn**, ta sang **Áp lực ngược** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Áp lực ngược

**Áp lực ngược (backpressure)** truyền tín hiệu ngược lên phía trước rằng bên xử lý không theo kịp. Cửa sổ nhận và điều khiển tắc nghẽn của TCP, cơ chế yêu cầu dữ liệu của Reactive Streams, channel có giới hạn và hàng đợi của luồng thực thi (thread / 스레드) pool đều là các ví dụ.

Nếu tầng phía trước bỏ qua tín hiệu rồi tự tích dữ liệu trong bộ nhớ, vấn đề quá tải chưa được giải quyết. Áp lực ngược cần lan đủ xa trong chuỗi xử lý hoặc phải kết thúc bằng một chính sách giới hạn, từ chối hay loại bỏ rõ ràng.


> **Chuyển mạch:** Từ **Áp lực ngược**, ta sang **Ngữ nghĩa truyền thông điệp** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Ngữ nghĩa truyền thông điệp

**Tối đa một lần (at-most-once)** có thể làm mất thông điệp nhưng tránh bản sao do thử lại. **Ít nhất một lần (at-least-once)** cho phép thử lại nên có thể tạo thông điệp trùng. Hiệu ứng **chính xác một lần (exactly-once)** đòi hỏi phối hợp hoặc loại trùng mạnh hơn và luôn phải xác định phạm vi bảo đảm.

Việc broker xác nhận đã giao thông điệp không đồng nghĩa giao dịch nghiệp vụ đã hoàn thành. Ví dụ bên tiêu thụ (consumer / 소비자) có thể ghi dữ liệu vào cơ sở dữ liệu rồi bị lỗi trước khi gửi `ack`; thông điệp sẽ được giao lại. Bộ xử lý lũy đẳng (idempotent handler), outbox và inbox là các mẫu thường dùng để xử lý tình huống này.


> **Chuyển mạch:** Từ **Ngữ nghĩa truyền thông điệp**, ta sang **Thứ tự** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thứ tự

Thứ tự toàn cục tuyệt đối có chi phí cao và thường không cần thiết. Nhật ký được phân vùng có thể bảo đảm thứ tự trong từng partition hoặc khóa. Nếu bất biến nghiệp vụ chỉ yêu cầu các thao tác của cùng một tài khoản theo thứ tự, phân vùng theo tài khoản có thể đã đủ.

Xử lý đồng thời còn có thể làm thứ tự hoàn thành khác thứ tự lấy thông điệp. Vì vậy hợp đồng về thứ tự phải nói rõ đang bảo đảm thứ tự đưa vào hàng, thứ tự giao, thứ tự xử lý hay thứ tự lần ghi nhận (commit / 커밋).


> **Chuyển mạch:** Từ **Thứ tự**, ta sang **Vị trí của trạng thái** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Vị trí của trạng thái

Trạng thái có thể nằm ở máy khách (client / 클라이언트), bộ nhớ ứng dụng, bộ nhớ đệm (cache / 캐시), cơ sở dữ liệu, nhật ký hoặc dịch vụ bên ngoài. Vị trí này ảnh hưởng trực tiếp tới tính sẵn sàng, khả năng mở rộng và phục hồi. Phiên người dùng nằm trong bộ nhớ cục bộ khiến việc mở rộng ngang cần định tuyến dính (sticky routing) hoặc sao chép; kho phiên bên ngoài lại thêm một phụ thuộc mạng.

Một **dịch vụ không trạng thái (stateless service)** thường chỉ có nghĩa trạng thái bền vững hoặc trạng thái phiên đã được đưa ra ngoài, chứ không phải tiến trình hoàn toàn không có trạng thái tạm thời.


> **Chuyển mạch:** Từ **Vị trí của trạng thái**, ta sang **Nhật ký sự kiện và trạng thái** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Nhật ký sự kiện và trạng thái

**sự kiện (event / 이벤트) sourcing** lưu chuỗi sự kiện miền làm nguồn dữ liệu chính và dựng trạng thái hiện tại bằng cách phát lại hoặc gấp các sự kiện. Cách này hỗ trợ lịch sử và kiểm toán nhưng làm tiến hóa lược đồ (schema / 스키마), chi phí phát lại, tính đúng đắn của sự kiện và hiệu ứng phụ bên ngoài trở nên phức tạp. Không phải hệ thống nào cũng cần sự kiện (event / 이벤트) sourcing.

**thay đổi (change / 변경) dữ liệu (data / 데이터) Capture (CDC)** phát các thay đổi trong cơ sở dữ liệu tới chỉ mục, hệ thống phân tích hoặc dịch vụ phía sau. Độ trễ nhất quán phát sinh từ quá trình này phải được chấp nhận và quan sát.


> **Chuyển mạch:** Từ **Nhật ký sự kiện và trạng thái**, ta sang **Áp lực ngược và giới hạn tốc độ** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Áp lực ngược và giới hạn tốc độ

**Giới hạn tốc độ (rate limiting)** bảo vệ ranh giới bằng cách giới hạn lượng yêu cầu được nhận từ một danh tính hoặc toàn hệ thống. Backpressure phản ánh áp lực động từ phía xử lý. Hai cơ chế có thể cùng tồn tại: tỷ lệ (rate / 비율) limiter ngăn lạm dụng và tải vượt ngưỡng; backpressure phản ứng với năng lực hiện tại của hệ thống phía sau.


> **Chuyển mạch:** Từ **Áp lực ngược và giới hạn tốc độ**, ta sang **Hàng đợi và bão thử lại** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hàng đợi và bão thử lại

Khi một phụ thuộc chậm lại, hàng đợi tăng. hết thời gian chờ (timeout / 타임아웃) có thể kích hoạt thử lại; thử lại làm tốc độ yêu cầu tăng; tải tăng lại khiến phụ thuộc chậm hơn. Đây là vòng phản hồi có thể tạo **bão thử lại (retry storm)**. Circuit breaker, ngân sách thử lại, hàng đợi có giới hạn và deadline giúp cắt vòng phản hồi này.


> **Chuyển mạch:** Từ **Hàng đợi và bão thử lại**, ta sang **Mô hình tư duy** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy

> Hàng đợi là **thời gian chờ được lưu lại**. Nó hấp thụ tải tăng đột biến, không giải quyết thiếu năng lực kéo dài. Mỗi hàng đợi cần có giới hạn dung lượng, chính sách nhận tải, ngữ nghĩa lỗi, phạm vi thứ tự và khả năng quan sát.


> **Chuyển mạch:** Từ **Mô hình tư duy**, ta sang **Những hiểu lầm thường gặp** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Những hiểu lầm thường gặp

**“Hàng đợi bất đồng bộ làm hệ thống nhanh hơn.”** Nó thay đổi thời điểm bên gọi phải chờ và làm tải mượt hơn; tổng lượng công việc và năng lực xử lý không tự tăng.

**“Kafka hoặc RabbitMQ bảo đảm exactly-once cho mọi thứ.”** Bảo đảm của broker luôn có phạm vi; hiệu ứng phụ trên cơ sở dữ liệu hoặc API bên ngoài vẫn cần phối hợp hoặc tính lũy đẳng.

**“Hàng đợi không giới hạn an toàn hơn vì không từ chối.”** Nó thường chỉ trì hoãn lỗi cho tới khi độ trễ hoặc tài nguyên bị cạn kiệt.


> **Chuyển mạch:** Từ **Những hiểu lầm thường gặp**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

[Hàng đợi tuyến tính](../01_algorithms_data_structures/03_linear_data_structures.md) là lớp trừu tượng cục bộ; [áp lực ngược trong TCP](../06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) là ví dụ ở tầng mạng; [khả năng chịu lỗi](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) sử dụng giảm tải và circuit breaker; phần [thời gian và tính lũy đẳng](./04_time_serialization_and_idempotency.md) giải thích cách xử lý hiệu ứng của việc thử lại.

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 abstraction modularity interfaces and apis](./00_abstraction_modularity_interfaces_and_apis.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
