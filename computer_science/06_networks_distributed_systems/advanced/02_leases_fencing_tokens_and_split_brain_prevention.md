# Leases, fencing tokens và split-brain prevention

Distributed lock thường được mô tả như mutex qua network, nhưng phép so sánh này nguy hiểm. Process có thể giữ “lock” rồi pause rất lâu; network partition có thể khiến lock service cấp quyền cho client khác; client cũ sau đó tỉnh lại và tiếp tục ghi. Vì vậy distributed mutual exclusion cần nhiều hơn một boolean `locked=true`.

## Lease là quyền có thời hạn

**Lease (임대/리스)** cấp quyền sử dụng resource trong một khoảng thời gian. Nếu holder không renew, quyền hết hạn và coordinator có thể cấp cho client khác.

Lease giúp hệ thống phục hồi khi holder crash mà không cần chờ explicit unlock. Nhưng nó đưa clock/time assumption vào correctness. Client không nên tự kết luận lease còn hiệu lực chỉ dựa vào wall clock của mình nếu protocol không bảo đảm clock relation phù hợp.

## Pause tạo stale holder

Giả sử client A nhận lease 30 giây rồi bị stop-the-world pause 60 giây. Trong thời gian đó lease hết hạn và B nhận lease mới. Khi A tỉnh lại, local state của A vẫn có thể chứa object “I am leader” và tiếp tục gửi write.

Nếu storage chỉ tin lời client rằng “tôi từng có lock”, split-brain write có thể xảy ra.

## Fencing token biến generation thành authority

Mỗi lần cấp lease/lock, coordinator phát một **fencing token** tăng đơn điệu: 41, 42, 43...

Storage/resource server ghi nhớ token lớn nhất đã chấp nhận. Nếu A với token 41 tỉnh lại sau khi B đã dùng token 42, request của A bị từ chối vì stale generation.

Điểm cốt lõi: correctness được enforce ở **resource boundary**, không chỉ ở lock service.

## Vì sao random UUID chưa đủ?

UUID phân biệt holders nhưng không cho resource biết token nào mới hơn. Fencing cần ordering/generation để stale request bị nhận diện. Một epoch/term/monotonic sequence phù hợp hơn khi protocol yêu cầu “new authority supersedes old authority”.

## Leader election và term

Consensus systems thường có khái niệm term/epoch. Leader mới hoạt động trong term cao hơn; message từ term cũ bị reject. Đây là cùng một mental model với fencing: authority phải gắn generation để delayed message từ quá khứ không thể ghi đè hiện tại.

## Split brain không chỉ là hai leaders

Split brain rộng hơn việc hai node cùng tự gọi mình leader. Vấn đề thực sự là hai actor có thể đồng thời tạo **side effect không tương thích** trên shared resource.

Nếu hai leaders tồn tại tạm thời nhưng chỉ một bên có quorum/fencing authority để commit, safety vẫn có thể giữ. Vì vậy “single leader” nên được định nghĩa theo quyền commit, không theo label trong process memory.

## External side effect khó fence

Database có thể kiểm tra fencing token trong transaction. Nhưng email server, payment gateway hoặc thiết bị vật lý có thể không hiểu token của lock service. Khi side effect nằm ngoài authority boundary, cần idempotency key, provider-side deduplication, transactional outbox hoặc workflow design khác.

Distributed lock không magically biến arbitrary external action thành exactly-once.

## Lease duration là trade-off

Lease dài giảm renewal traffic và false expiration khi jitter, nhưng failover chậm. Lease ngắn failover nhanh hơn nhưng nhạy với pause/network delay. Renewal nên có safety margin thay vì đợi sát expiry.

Nếu correctness phụ thuộc chặt vào time, phải định nghĩa clock source, drift bound và behavior khi clock bất thường. Nhiều hệ thống cố dùng monotonic clock cho duration thay vì wall-clock time có thể nhảy.

## Practical pattern

Một robust flow có thể là: client acquire lease → nhận fencing token → mọi mutation tới storage kèm token → storage chỉ chấp nhận token >= generation đã ghi nhận → renewal duy trì lease nhưng không giảm token.

Nếu client mất lease, nó có thể tiếp tục chạy code nhưng không còn khả năng tạo authoritative mutation.

## Mental model

> Lease giải quyết quyền có thời hạn; fencing giải quyết stale actor. Distributed correctness không đến từ việc mọi node luôn đồng ý ai là leader, mà từ việc resource cuối cùng có thể từ chối authority cũ. Hãy đặt enforcement tại nơi side effect thực sự xảy ra.