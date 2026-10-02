# 05. Async jobs và messaging

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **05. Async jobs và messaging**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Chọn message ngữ nghĩa (semantics / 의미론)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Job vòng đời (lifecycle / 생명주기)** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Mạch này nối async jobs với messaging, delivery semantics và retry, để worker xử lý trùng lặp và mất mát theo hợp đồng rõ ràng.

## Chọn message ngữ nghĩa (semantics / 의미론)

Command yêu cầu một bên tiêu thụ (consumer / 소비자) thực hiện hành động; sự kiện (event / 이벤트) thông báo điều đã xảy
ra; truy vấn (query / 쿼리) yêu cầu dữ liệu. Tên message nên thể hiện intent và phiên bản (version / 버전) lược đồ (schema / 스키마).
Producer/bên tiêu thụ (consumer / 소비자) cần biết delivery là at-most-once, at-least-once hay một dạng
effectively-once có deduplication. “Exactly once” ở toàn hệ thống hiếm khi là
thuộc tính (property / 속성) miễn phí.

> **Chuyển mạch:** Message semantics quyết định consumer phải làm gì và chấp nhận delivery nào; **Job vòng đời (lifecycle / 생명주기)** chuyển hợp đồng đó thành các trạng thái accepted, retrying và failed có thể quan sát.

## Job vòng đời (lifecycle / 생명주기)

```text
accepted → queued → running → succeeded
                    ↘ retrying → dead-lettered/failed
```

Lưu job ID, attempt, next-attempt thời gian (time / 시간), lease/visibility hết thời gian chờ (timeout / 타임아웃) và lỗi (error / 오류) lớp (class / 클래스).
Worker phải idempotent: xử lý lại cùng message không nhân đôi email, charge hay
row. Dùng dedupe key, unique ràng buộc (constraint / 제약조건) hoặc máy trạng thái (state machine / 상태 머신) thay vì cờ trong RAM.

> **Chuyển mạch:** Các trạng thái job chỉ bền khi việc ghi dữ liệu và publish message không tách rời. **Transactional handoff** dùng outbox/inbox để nối commit với delivery, rồi đặt ra nhu cầu kiểm soát tải ở phần kế tiếp.

## Transactional handoff

Nếu cơ sở dữ liệu (database / 데이터베이스) lần ghi nhận (commit / 커밋) tạo ra việc cần publish, outbox ghi sự kiện (event / 이벤트) trong cùng
giao dịch (transaction / 트랜잭션); dispatcher đọc outbox và thử lại (retry / 재시도) publish. bên tiêu thụ (consumer / 소비자) ghi inbox/dedup
bản ghi (record / 레코드) trước hoặc cùng giao dịch (transaction / 트랜잭션) với side tác động (effect / 효과) cục bộ. Poison message đi vào
DLQ với ngữ cảnh (context / 맥락) đủ để replay có kiểm soát, không bị vứt âm thầm.

> **Chuyển mạch:** Outbox và dedupe bảo vệ tính đúng, nhưng không tự giới hạn backlog. **Backpressure và shutdown** xử lý sức chứa, lease và graceful drain; từ đó mới có thể quyết định ordering và replay an toàn.

## Backpressure và shutdown

Giới hạn hàng đợi (queue / 큐) độ sâu (depth / 깊이), tính đồng thời (concurrency / 동시성), payload kích thước (size / 크기) và thời gian chạy. Khi phụ thuộc (dependency / 의존성)
chậm, giảm intake thay vì để backlog vô hạn. Worker shutdown phải stop nhận việc
mới, hoàn tất hoặc trả lease công việc đang chạy, rồi đóng tài nguyên (resource / 자원).

Hàng đợi (queue / 큐) internals, thứ tự (ordering / 순서) và phân tán (distributed / 분산) delivery thuộc [Networks & Distributed Systems](../../computer_science/06_networks_distributed_systems/README.md); chapter này tập trung vào đặc tả ứng dụng (application contract / 애플리케이션 계약).

> **Chuyển mạch:** Backpressure và graceful shutdown đặt giới hạn lên intake, lease và worker lifecycle. **Đào sâu: thứ tự (ordering / 순서) và replay** dùng các giới hạn đó để xác định partition, duplicate handling và replay rate trước khi đưa vào tình huống kiểm tra.

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

> **Chuyển mạch:** Ordering, visibility timeout và replay policy đã tạo đủ ràng buộc để kiểm tra một tình huống duplicate thực tế. **Bài tập suy luận** gom các ràng buộc đó vào một invoice event để xác minh dedupe, DLQ và metric cùng hoạt động.

## Bài tập suy luận

Invoice sự kiện (event / 이벤트) bị xử lý hai lần: lần đầu gửi email thành công nhưng worker crash
trước ack. Thiết kế dedupe bản ghi (record / 레코드), unique key, email-provider idempotency, DLQ
chính sách (policy / 정책) và chỉ số (metric / 지표) chứng minh thử lại (retry / 재시도) không gửi email thứ hai.

> **Bàn giao:** Giữ lại delivery semantics, outbox/inbox, backpressure và replay guard; quay về [README](./README.md) khi cần nối sang timeout/retry hoặc observability của worker.
