# Thời gian, lỗi và tính nhất quán trong hệ thống phân tán

**Hệ thống phân tán (distributed system / 분산 시스템)** gồm nhiều thành phần chạy trên các máy hoặc tiến trình khác nhau và giao tiếp qua mạng. Điều làm nó khó không chỉ là “có nhiều máy”, mà là **không có bộ nhớ chia sẻ hoàn hảo, không có đồng hồ toàn cục hoàn hảo, độ trễ thông điệp không có giới hạn chắc chắn và lỗi có thể chỉ xảy ra ở một phần hệ thống**.

## Lỗi một phần

Một tiến trình đơn lẻ bị crash thường dễ nhận biết vì nó dừng. Trong hệ thống phân tán, nút A có thể thấy B bị timeout trong khi C vẫn giao tiếp được với B. Phân vùng mạng, định tuyến bất đối xứng, GC pause, quá tải và mất gói đều có thể tạo biểu hiện giống lỗi.

Timeout chỉ cho biết “chưa nhận được phản hồi trong thời gian chờ”; nó không chứng minh thao tác ở phía xa chưa được thực hiện. Đây là nguồn phổ biến của hiệu ứng phụ bị lặp khi hệ thống thử lại.

## Không có thời gian toàn cục đơn giản

Đồng hồ vật lý bị trôi theo thời gian. NTP hoặc PTP giúp đồng bộ tương đối nhưng vẫn tồn tại sai số. Việc máy A ghi `10:00:00.100` còn máy B ghi `10:00:00.090` không đủ để kết luận sự kiện B xảy ra trước A theo quan hệ nhân quả.

**Đồng hồ Lamport (Lamport clock)** biểu diễn thứ tự từng phần “xảy ra trước” (happens-before): sự kiện cục bộ tăng bộ đếm; thông điệp gửi kèm giá trị đồng hồ; bên nhận cập nhật theo `max + 1`. **Đồng hồ vector (vector clock)** còn có thể nhận biết hai sự kiện đồng thời nhưng lượng siêu dữ liệu tăng theo số bên tham gia.

Đồng hồ logic không đo thời gian thực; nó mã hóa thông tin về thứ tự.

## Quan hệ nhân quả

Sự kiện A **đi trước theo nhân quả (causally precedes)** sự kiện B nếu B có thể bị ảnh hưởng bởi A thông qua chuỗi thực thi hoặc thông điệp. Hai sự kiện đồng thời không có quan hệ nhân quả với nhau. Nhiều mô hình nhất quán chỉ cần bảo toàn thứ tự nhân quả chứ không cần ép toàn bộ hệ thống vào một thứ tự toàn cục.

## Các mô hình nhất quán

“Tính nhất quán mạnh” là một nhóm khái niệm chứ không phải một định nghĩa duy nhất.

**Linearizability** làm các thao tác trông như xảy ra nguyên tử theo một thứ tự phù hợp với thời gian thực. **Sequential consistency** giữ thứ tự thao tác của từng tiến trình nhưng không bắt buộc phù hợp với thời gian thực toàn cục. **Causal consistency** bảo toàn quan hệ nhân quả. **Eventual consistency** bảo đảm các bản sao cuối cùng sẽ hội tụ nếu cập nhật dừng lại và việc truyền dữ liệu tiếp tục, nhưng cách giải quyết xung đột vẫn phải được định nghĩa.

Các bảo đảm theo phiên như **đọc thấy dữ liệu vừa ghi (read-your-writes)** và **đọc đơn điệu (monotonic reads)** giúp hệ thống nhất quán yếu dễ sử dụng hơn.

## Hiểu đúng định lý CAP

CAP nói rằng trong một hệ thống dữ liệu phân tán có mạng bất đồng bộ, khi xảy ra **phân vùng mạng (partition)** thì không thể đồng thời bảo đảm cả tính nhất quán mạnh kiểu linearizability và khả năng phục vụ mọi yêu cầu. Phân vùng mạng là khả năng thực tế phải chấp nhận; khi nó xảy ra, thiết kế phải lựa chọn giữa từ chối/trì hoãn một số yêu cầu hoặc tiếp tục phục vụ với nguy cơ trạng thái các phía tạm thời khác nhau.

CAP không có nghĩa “luôn chọn 2 trong 3” trong vận hành bình thường. Khái niệm availability trong định lý cũng có nghĩa kỹ thuật cụ thể, không đồng nhất với tỷ lệ uptime trong SLA.

PACELC mở rộng trực giác này: khi có phân vùng thì đánh đổi giữa khả năng sẵn sàng và tính nhất quán; khi không có phân vùng thì thường còn đánh đổi giữa độ trễ và tính nhất quán.

## Safety và liveness

**Thuộc tính an toàn (safety)** nói rằng điều xấu không bao giờ được xảy ra, ví dụ hai leader không được cùng commit hai giá trị xung đột vào cùng vị trí log. **Thuộc tính tiến triển (liveness)** nói rằng điều tốt cuối cùng sẽ xảy ra, ví dụ yêu cầu cuối cùng hoàn thành khi điều kiện hệ thống phục hồi.

Thuật toán đồng thuận thường chấp nhận mất liveness trong một số kiểu phân vùng để giữ safety.

## Huyền thoại “exactly once”

Mạng có thể làm mất yêu cầu hoặc phản hồi. Khi client bị timeout, nó không thể tự biết chắc server đã thực hiện thao tác hay chưa. Hiệu ứng **chính xác một lần (exactly-once effect)** từ đầu đến cuối thường cần khóa lũy đẳng, loại trùng hoặc trạng thái giao dịch, chứ không thể chỉ dựa vào cơ chế vận chuyển mạng.

Broker thông điệp có thể cung cấp bảo đảm exactly-once trong một phạm vi cụ thể, nhưng hiệu ứng phụ ở cơ sở dữ liệu hoặc API bên ngoài vẫn cần giao thức phối hợp.

## Bộ phát hiện lỗi

Trong mô hình hoàn toàn bất đồng bộ, không thể luôn phân biệt hoàn hảo một nút “rất chậm” với một nút “đã chết”. Hệ thống thực tế dùng heartbeat, timeout và các giả định cuối cùng đủ chính xác. Phát hiện quá nhạy tạo dương tính giả; phát hiện quá chậm làm failover bị trì hoãn.

## Mô hình tư duy

> Hệ thống phân tán thay sự chắc chắn bằng **thông điệp + bất định**. Không được suy ra “không xảy ra” chỉ từ timeout. Hãy mô tả riêng các bảo đảm về thứ tự, độ bền dữ liệu, khả năng sẵn sàng và độ trễ.

## Những hiểu lầm thường gặp

**“Eventual consistency nghĩa là dữ liệu có thể ngẫu nhiên hoặc cũ mãi mãi.”** Nó bảo đảm hội tụ dưới những điều kiện nhất định; cách giải quyết xung đột và ngữ nghĩa phiên vẫn phải được xác định.

**“CAP nghĩa là mọi cơ sở dữ liệu phân tán phải thuộc đúng CA, CP hoặc AP.”** Định lý tập trung vào giai đoạn có phân vùng và các bảo đảm cụ thể; hệ thống thực tế có thể cung cấp nhiều chế độ hoặc mức bảo đảm khác nhau theo thao tác.

**“Sắp xếp timestamp sẽ cho đúng thứ tự toàn cục.”** Sai lệch và bất định đồng hồ phá vỡ suy luận nhân quả nếu không có giao thức hoặc giả định mạnh hơn.

## Kết nối

[Đồng thời](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) xử lý thứ tự trong bộ nhớ chia sẻ; hệ thống phân tán loại bỏ giả định về bộ nhớ và đồng hồ chung đồng thời thêm lỗi một phần. Phần [sao chép, phân vùng và đồng thuận](./05_replication_partitioning_and_consensus.md) xây dựng các cơ chế cho những ràng buộc này.