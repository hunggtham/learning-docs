# 05. Async jobs và messaging

> **Mạch đọc:** Đặt **05. Async jobs và messaging** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Chọn message ngữ nghĩa (semantics / 의미론)** sang **Job vòng đời (lifecycle / 생명주기)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## Chọn message ngữ nghĩa (semantics / 의미론)

Command yêu cầu một bên tiêu thụ (consumer / 소비자) thực hiện hành động; sự kiện (event / 이벤트) thông báo điều đã xảy
ra; truy vấn (query / 쿼리) yêu cầu dữ liệu. Tên message nên thể hiện intent và phiên bản (version / 버전) lược đồ (schema / 스키마).
Producer/bên tiêu thụ (consumer / 소비자) cần biết delivery là at-most-once, at-least-once hay một dạng
effectively-once có deduplication. “Exactly once” ở toàn hệ thống hiếm khi là
thuộc tính (property / 속성) miễn phí.


> **Chuyển mạch:** Từ **Chọn message ngữ nghĩa (semantics / 의미론)**, ta sang **Job vòng đời (lifecycle / 생명주기)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Job vòng đời (lifecycle / 생명주기)
Phần “Job vòng đời (lifecycle / 생명주기)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
accepted → queued → running → succeeded
                    ↘ retrying → dead-lettered/failed
```

Lưu job ID, attempt, next-attempt thời gian (time / 시간), lease/visibility hết thời gian chờ (timeout / 타임아웃) và lỗi (error / 오류) lớp (class / 클래스).
Worker phải idempotent: xử lý lại cùng message không nhân đôi email, charge hay
row. Dùng dedupe key, unique ràng buộc (constraint / 제약조건) hoặc máy trạng thái (state machine / 상태 머신) thay vì cờ trong RAM.


> **Chuyển mạch:** Từ **Job vòng đời (lifecycle / 생명주기)**, ta sang **Transactional handoff** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Transactional handoff

Nếu cơ sở dữ liệu (database / 데이터베이스) lần ghi nhận (commit / 커밋) tạo ra việc cần publish, outbox ghi sự kiện (event / 이벤트) trong cùng
giao dịch (transaction / 트랜잭션); dispatcher đọc outbox và thử lại (retry / 재시도) publish. bên tiêu thụ (consumer / 소비자) ghi inbox/dedup
bản ghi (record / 레코드) trước hoặc cùng giao dịch (transaction / 트랜잭션) với side tác động (effect / 효과) cục bộ. Poison message đi vào
DLQ với ngữ cảnh (context / 맥락) đủ để replay có kiểm soát, không bị vứt âm thầm.


> **Chuyển mạch:** Từ **Transactional handoff**, ta sang **Backpressure và shutdown** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Backpressure và shutdown

Giới hạn hàng đợi (queue / 큐) độ sâu (depth / 깊이), tính đồng thời (concurrency / 동시성), payload kích thước (size / 크기) và thời gian chạy. Khi phụ thuộc (dependency / 의존성)
chậm, giảm intake thay vì để backlog vô hạn. Worker shutdown phải stop nhận việc
mới, hoàn tất hoặc trả lease công việc đang chạy, rồi đóng tài nguyên (resource / 자원).

Hàng đợi (queue / 큐) internals, thứ tự (ordering / 순서) và phân tán (distributed / 분산) delivery thuộc [Networks & Distributed Systems](../../computer_science/06_networks_distributed_systems/README.md); chapter này tập trung vào đặc tả ứng dụng (application contract / 애플리케이션 계약).


> **Chuyển mạch:** Từ **Backpressure và shutdown**, ta sang **Đào sâu: thứ tự (ordering / 순서) và replay** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Đào sâu: thứ tự (ordering / 순서) và replay

Thứ tự (ordering / 순서) thường chỉ có ý nghĩa trong một partition/key, không phải toàn hàng đợi (queue / 큐).
Nếu `OrderCreated` và `OrderCancelled` phải theo thứ tự, partition theo
`order_id` nhưng bên tiêu thụ (consumer / 소비자) vẫn phải xử lý duplicate/out-of-order defensively.
Đừng giữ toàn cục (global / 전역) thứ tự (ordering / 순서) đắt đỏ chỉ vì một bên tiêu thụ (consumer / 소비자) cần chuỗi (sequence / 시퀀스).

Replay là năng lực (capability / 역량) vận hành, không phải nút “run lại mọi thứ”. sự kiện (event / 이벤트) cần lược đồ (schema / 스키마)
phiên bản (version / 버전), sự kiện (event / 이벤트) ID, occurred-at, producer và dữ liệu đủ để bên tiêu thụ (consumer / 소비자) quyết định.
bên tiêu thụ (consumer / 소비자) phải phân biệt replay (không gửi charge/email lại) với compensation (có
chủ đích tạo side effect mới). DLQ replay cần tỷ lệ (rate / 비율) limit, visibility và quyền
riêng; message lỗi do lược đồ (schema / 스키마) không nên replay vô hạn.

Visibility hết thời gian chờ (timeout / 타임아웃) ngắn hơn thời gian xử lý gây duplicate; quá dài làm khôi phục (recovery / 복구)
chậm khi worker chết. Heartbeat/lease extension có giới hạn và không thay thế
idempotency, vì crash có thể xảy ra sau side tác động (effect / 효과) nhưng trước ack.


> **Chuyển mạch:** Từ **Đào sâu: thứ tự (ordering / 순서) và replay**, ta sang **Bài tập suy luận** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bài tập suy luận

Invoice sự kiện (event / 이벤트) bị xử lý hai lần: lần đầu gửi email thành công nhưng worker crash
trước ack. Thiết kế dedupe bản ghi (record / 레코드), unique key, email-provider idempotency, DLQ
chính sách (policy / 정책) và chỉ số (metric / 지표) chứng minh thử lại (retry / 재시도) không gửi email thứ hai.

> **Bàn giao:** Sau **Bài tập suy luận**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 backend request lifecycle](./00_backend_request_lifecycle.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
