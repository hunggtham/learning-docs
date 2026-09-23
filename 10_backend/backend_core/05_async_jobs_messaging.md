# 05. Async jobs và messaging

## Chọn message semantics

Command yêu cầu một consumer thực hiện hành động; event thông báo điều đã xảy
ra; query yêu cầu dữ liệu. Tên message nên thể hiện intent và version schema.
Producer/consumer cần biết delivery là at-most-once, at-least-once hay một dạng
effectively-once có deduplication. “Exactly once” ở toàn hệ thống hiếm khi là
property miễn phí.

## Job lifecycle

```text
accepted → queued → running → succeeded
                    ↘ retrying → dead-lettered/failed
```

Lưu job ID, attempt, next-attempt time, lease/visibility timeout và error class.
Worker phải idempotent: xử lý lại cùng message không nhân đôi email, charge hay
row. Dùng dedupe key, unique constraint hoặc state machine thay vì cờ trong RAM.

## Transactional handoff

Nếu database commit tạo ra việc cần publish, outbox ghi event trong cùng
transaction; dispatcher đọc outbox và retry publish. Consumer ghi inbox/dedup
record trước hoặc cùng transaction với side effect cục bộ. Poison message đi vào
DLQ với context đủ để replay có kiểm soát, không bị vứt âm thầm.

## Backpressure và shutdown

Giới hạn queue depth, concurrency, payload size và thời gian chạy. Khi dependency
chậm, giảm intake thay vì để backlog vô hạn. Worker shutdown phải stop nhận việc
mới, hoàn tất hoặc trả lease công việc đang chạy, rồi đóng resource.

Queue internals, ordering và distributed delivery thuộc [Networks & Distributed Systems](../../computer_science/06_networks_distributed_systems/README.md); chapter này tập trung vào application contract.

## Đào sâu: ordering và replay

Ordering thường chỉ có ý nghĩa trong một partition/key, không phải toàn queue.
Nếu `OrderCreated` và `OrderCancelled` phải theo thứ tự, partition theo
`order_id` nhưng consumer vẫn phải xử lý duplicate/out-of-order defensively.
Đừng giữ global ordering đắt đỏ chỉ vì một consumer cần sequence.

Replay là capability vận hành, không phải nút “run lại mọi thứ”. Event cần schema
version, event ID, occurred-at, producer và dữ liệu đủ để consumer quyết định.
Consumer phải phân biệt replay (không gửi charge/email lại) với compensation (có
chủ đích tạo side effect mới). DLQ replay cần rate limit, visibility và quyền
riêng; message lỗi do schema không nên replay vô hạn.

Visibility timeout ngắn hơn thời gian xử lý gây duplicate; quá dài làm recovery
chậm khi worker chết. Heartbeat/lease extension có giới hạn và không thay thế
idempotency, vì crash có thể xảy ra sau side effect nhưng trước ack.

## Bài tập suy luận

Invoice event bị xử lý hai lần: lần đầu gửi email thành công nhưng worker crash
trước ack. Thiết kế dedupe record, unique key, email-provider idempotency, DLQ
policy và metric chứng minh retry không gửi email thứ hai.
