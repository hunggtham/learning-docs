# 10. Production backend case studies

Các case dưới đây luyện đường suy luận `symptom → invariant → evidence → design`.
Chúng không thay thế chapter trước và không gắn với một framework duy nhất.

## Case 1 — Double charge sau timeout

- **Symptom:** client nhận timeout và bấm lại; có hai charge.
- **Invariant:** một business operation của cùng subject/order chỉ được charge
  một lần.
- **Evidence:** payment provider có một request thành công; application retry có
  request ID khác.
- **Design:** idempotency key theo order/attempt, lưu result, query trạng thái
  trước retry và timeout budget rõ ràng.

## Case 2 — User thấy dữ liệu tenant khác

- **Symptom:** detail đúng ở cache nhưng thuộc tenant khác.
- **Invariant:** mọi read/write phải bị giới hạn bởi verified tenant identity.
- **Evidence:** cache key chỉ dùng `resource_id`, thiếu tenant; DB query chính có
  filter nhưng cache hit bypass filter.
- **Design:** key chứa tenant/subject scope, authorization trước cache read, test
  cross-tenant và không cache response nhạy cảm nếu policy chưa rõ.

## Case 3 — Queue backlog tăng sau deploy

- **Symptom:** queue age tăng, worker CPU thấp, retry count cao.
- **Invariant:** consumer phải xử lý message trong deadline và không tự nhân tải.
- **Evidence:** trace cho thấy dependency timeout; mỗi message bị retry ở worker
  và client library, tạo retry storm.
- **Design:** deadline propagation, một retry owner, backoff+jitter, concurrency
  cap, DLQ và alert theo queue age.

## Case 4 — Lost update khi hai tab cùng sửa

- **Symptom:** thay đổi của tab sau ghi đè tab trước.
- **Invariant:** write chỉ áp dụng trên version mà client đã đọc.
- **Evidence:** hai `UPDATE` đều thành công, không có version predicate.
- **Design:** optimistic concurrency với `ETag/If-Match` hoặc version column;
  trả `409/412`, cho client merge hoặc reload.

## Case 5 — Deploy làm API lỗi ngẫu nhiên

- **Symptom:** rolling deploy có 5xx khi schema mới/chưa mới cùng chạy.
- **Invariant:** mọi code version đang active phải đọc/ghi schema tương thích.
- **Evidence:** old instance không hiểu column/enum mới; migration destructive
  chạy trước drain traffic.
- **Design:** expand → deploy compatible readers/writers → backfill → contract;
  kiểm thử mixed-version và rollback plan.

## Cách dùng case

Với incident thật, viết lại symptom bằng scope/time window, nêu invariant bị đe
dọa, thu thập evidence trước khi chọn tool/framework fix. Sau mitigation, thêm
test hoặc metric đủ để lần sau phát hiện sớm hơn.

## Case 6 — Cache stampede sau invalidation

- **Symptom:** một key hết hạn, origin CPU tăng vọt dù traffic không đổi.
- **Invariant:** hot key không được tạo nhiều rebuild đồng thời vượt budget.
- **Evidence:** trace cho thấy hàng trăm miss cùng timestamp; không có lease và
  TTL của cả batch được set giống nhau.
- **Design:** single-flight/lease, jitter, stale-while-revalidate, origin
  concurrency cap và metric `rebuild_in_flight`.

## Case 7 — Retry storm làm dependency sập

- **Symptom:** provider chậm, số request tăng dù traffic vào ổn định.
- **Invariant:** retry không được làm tải lỗi lớn hơn tải gốc ngoài multiplier đã
  định trước.
- **Evidence:** gateway, service và SDK cùng retry; backoff không có jitter.
- **Design:** một retry owner, deadline propagation, bounded attempts, circuit
  breaker/bulkhead và alert theo retry ratio.

## Case 8 — Authorization đúng ở HTTP nhưng sai ở worker

- **Symptom:** user bị revoke nhưng export job vẫn đọc dữ liệu nhạy cảm.
- **Invariant:** policy của async path phải được định nghĩa như sync path.
- **Evidence:** worker tin snapshot request cũ, không kiểm tra tenant status và
  không có audit actor.
- **Design:** chọn snapshot hoặc just-in-time authorization có chủ ý, lưu actor,
  scope và policy version, thêm revoke test và kill switch.

## Capstone

Chọn một API thật và viết một design note gồm request state machine, contract,
identity, transaction matrix, cache policy, async handoff, timeout budget, test
matrix, telemetry và rollback. Design chỉ hoàn tất khi mỗi failure mode có owner
và evidence tương ứng.
