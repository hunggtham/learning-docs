# 06. Timeout, retry và idempotency

## Timeout budget

Timeout là một phần của contract. Nếu request có deadline 2 giây, các dependency
không được mỗi cái tự chờ 2 giây. Truyền deadline/cancellation xuống chain và
dành ngân sách cho serialization, queueing và response. Timeout cần phân biệt
connect, TLS, pool acquire, read và total deadline khi client hỗ trợ.

## Retry có điều kiện

Chỉ retry lỗi tạm thời, request còn deadline và operation an toàn để lặp. Không
retry validation, permission, business conflict hoặc mọi `5xx` một cách mù quáng.
Exponential backoff + jitter và giới hạn attempts ngăn synchronized retry storm.
Mỗi layer không nên retry độc lập đến khi tổng số lần nhân lên ngoài dự kiến.

## Idempotency

Một operation idempotent có thể được gửi lại mà không tạo thêm hiệu ứng logic.
Với mutation không tự idempotent:

1. caller gửi idempotency key ổn định;
2. server lưu key, request fingerprint và terminal result;
3. request trùng fingerprint trả lại result cũ;
4. key dùng với payload khác bị từ chối;
5. retention đủ dài so với cửa sổ retry/replay.

Unique constraint, state transition (`pending → completed`) và dedupe record bảo
vệ lớp database/consumer. Idempotency key không thay thế authorization: cùng key
nhưng subject/tenant khác phải bị từ chối.

## Quan sát

Ghi attempt number, original request ID, dependency, timeout reason và final
outcome. Phân biệt “timeout nhưng server đã commit” với “chưa tới server”; đây là
lý do caller phải query trạng thái trước khi tạo lại side effect.

## Đào sâu: retry topology

Vẽ toàn bộ retry graph trước khi thêm retry loop:

```text
browser → API client → service A → service B → database/provider
```

Nếu mỗi hop retry 3 lần, một request có thể tạo 81 attempts ở dependency cuối.
Chọn một retry owner, truyền deadline còn lại và để hop khác fail fast hoặc chỉ
retry lỗi transport rất hẹp. Circuit breaker/bulkhead bảo vệ pool nhưng không
thay thế timeout và idempotency.

Timeout tạo trạng thái “unknown”, không phải luôn là failure. Với read, retry có
thể an toàn; với mutation, query status bằng idempotency key/order ID trước khi
tạo operation mới. API nên cung cấp endpoint status nếu operation có thể chạy sau
khi caller mất kết nối.

## Bài tập suy luận

Cho deadline 2 giây, gateway overhead 100 ms, service A gọi B và B gọi provider.
Đề xuất budget từng hop, connect/read timeout, số retry tối đa và điều kiện dừng;
giải thích vì sao tổng timeout không được vượt deadline dù có backoff.

## Circuit breaker, bulkhead và load shedding

Ba cơ chế này giải quyết các failure khác nhau:

- **Circuit breaker:** ngừng gọi dependency đang lỗi sau ngưỡng có bằng chứng,
  chuyển sang half-open có giới hạn để probe recovery.
- **Bulkhead:** tách thread/connection/concurrency budget giữa dependency hoặc
  workload để một pool cạn không kéo sập toàn process.
- **Load shedding:** từ chối hoặc hạ chất lượng request khi hệ thống đã vượt
  capacity, ưu tiên traffic quan trọng thay vì để mọi request timeout.

Breaker cần tránh một trạng thái global quá thô: lỗi của một tenant hoặc một
route có thể không đại diện cho toàn provider. Probe recovery phải có jitter và
quota. Fallback chỉ được dùng khi semantics an toàn; trả dữ liệu cache cũ cho
permission-sensitive read có thể tạo security bug.

Dependency budget nên được mô hình hóa bằng concurrency × service time ≈ in-flight
work. Khi queueing và saturation tăng, retry thường làm tình hình xấu hơn; hãy
giảm intake trước khi tăng số worker.
