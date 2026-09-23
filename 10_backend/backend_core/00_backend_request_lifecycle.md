# 00. Backend request lifecycle

## Mục tiêu

Một backend request không chỉ là lời gọi đến controller. Nó là một đường đi qua
nhiều boundary, trong đó mỗi boundary có contract, timeout, state và evidence
riêng.

```text
client
  → DNS/TLS/proxy/load balancer
  → server process / framework adapter
  → middleware (request id, auth, limits)
  → handler/use case
  → repository/cache/remote dependency
  → commit hoặc rollback
  → response + logs/metrics/traces
```

## Invariant cần giữ

- Mỗi request có một correlation/request ID; log ở các layer có thể nối lại.
- Authentication được hoàn tất trước khi dùng identity để authorize.
- Validation ở boundary không thay thế invariant trong domain và database.
- Side effect chỉ được báo thành công khi trạng thái tương ứng đã commit, hoặc
  contract nói rõ nó được xử lý bất đồng bộ.
- Mọi dependency bên ngoài có timeout hữu hạn; không để request chờ vô hạn.

## Sync và async

Synchronous flow phù hợp khi caller cần kết quả ngay và ngân sách latency đủ.
Async flow phù hợp cho email, export, webhook, indexing hoặc công việc dài.
Đừng trả `200 OK` cho một side effect chưa có owner; dùng `202 Accepted` với job
ID và trạng thái có thể truy vấn khi processing còn tiếp diễn.

## Cách debug

Bắt đầu từ request ID, timestamp và route. Xác định request đã chết ở proxy,
queue, application, database hay remote dependency; sau đó so sánh latency theo
từng span thay vì đoán từ tổng thời gian. Một response error không chứng minh
transaction đã rollback nếu side effect ngoài database đã xảy ra.

## Liên kết canonical

Chi tiết process, network path và storage thuộc [Computer Science](../../computer_science/README.md).
Chapter này giữ application-level lifecycle và cách đặt boundary, không mô tả
lại TCP, scheduler hay WAL internals.

## Đào sâu: request như một state machine

Đừng coi request là một hàm `input → output` đơn giản. Trong production, nó có
thể đi qua các trạng thái:

```text
received → admitted → authenticated → authorized → executing
    → committed → response_sent
                 ↘ failed/retryable
```

`response_sent` không đồng nghĩa side effect đã được caller quan sát hoặc
consumer đã xử lý. Với async flow, response chỉ xác nhận `accepted`; trạng thái
hoàn tất phải nằm trong job state machine có owner và retention.

### Boundary và failure ownership

Mỗi boundary cần trả lời ba câu hỏi: ai sở hữu timeout và cancellation; state nào
đã commit nếu boundary chết giữa chừng; caller có thể query hoặc retry thế nào.
Nếu database commit thành công nhưng publish event thất bại, lỗi thuộc
transactional handoff và cần outbox/replay, không phải HTTP layer. Nếu proxy
timeout nhưng handler vẫn chạy, client không được tự suy ra transaction đã rollback.

### Admission control

Trước business logic, server có thể từ chối sớm vì body quá lớn, rate limit,
connection pool cạn hoặc shutdown đang drain. Theo dõi `rejected_total`, queueing
time và active request count để phân biệt overload với lỗi logic.

### Configuration và secrets

Configuration có lifecycle riêng: source of truth, precedence, validation, rollout
và rollback. Tách immutable startup config (port, schema compatibility) khỏi
dynamic config (feature flag, quota) và secret (credential, signing key). Process
nên fail fast với config bắt buộc sai, nhưng không in giá trị secret vào exception,
startup log hay trace. Rotation cần overlap window, version/key ID và khả năng
revoke; không giả định restart mọi instance là một transaction nguyên tử.

Environment variable là delivery mechanism, không tự động là secret manager.
Ghi rõ ai được đọc config, config thay đổi có audit nào, và instance đang chạy
version nào. Config drift giữa local/staging/production phải quan sát được như
một loại deployment change, không để debug bằng cách sửa thủ công trong process.

### Bài tập suy luận

Vẽ timeline cho một `POST /orders` khi client timeout ở 1.5 giây, database commit
ở giây 1.2 và event publish thất bại ở giây 1.3. Đánh dấu response caller thấy,
state authoritative, retry an toàn và metric chứng minh từng kết luận.
