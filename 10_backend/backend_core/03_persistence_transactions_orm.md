# 03. Persistence, transaction và ORM

## Từ use case đến state transition

Persistence không bắt đầu từ entity annotation. Bắt đầu bằng invariant: state
nào phải cùng thay đổi, uniqueness nào phải được bảo vệ, và lúc nào dữ liệu được
coi là committed. Transaction boundary nên bao quanh một use case có tính nguyên
tử, không mặc định bao quanh toàn bộ request nếu request còn gọi remote service.

```text
input → validate command → load state → decide transition
      → write state + audit/outbox → commit
```

Database constraint là lớp bảo vệ cuối cùng cho uniqueness, foreign key và check
invariant; application validation chỉ cải thiện thông báo lỗi. Chọn isolation
theo anomaly cần ngăn, không theo khẩu hiệu “strongest luôn tốt nhất”.

## ORM boundary

ORM giúp mapping object/record và quản lý unit of work, nhưng không che được
query plan, lock, transaction hay cardinality. Review generated SQL. Tránh:

- N+1 query do lazy relationship trong vòng lặp;
- trả entity trực tiếp làm lộ field và kéo cả graph;
- transaction đã đóng nhưng proxy còn lazy-load;
- bulk update bỏ qua domain event/audit;
- migration schema không tương thích với code đang chạy.

Đọc model bằng DTO/projection khi cần API ổn định. Dùng migration versioned,
backward-compatible (expand → migrate → contract) cho deploy rolling.

## Remote side effect

Không giữ database transaction mở trong lúc chờ payment/API khác. Dùng outbox,
saga hoặc trạng thái pending tùy invariant. Nếu commit thành công nhưng gửi event
thất bại, phải có cơ chế retry và quan sát được; nếu gửi trước commit, consumer
có thể nhìn thấy state chưa tồn tại.

Chi tiết ACID, MVCC, WAL và query execution thuộc [Data & Databases](../../computer_science/05_data_databases/README.md).

## Đào sâu: transaction boundary và failure matrix

Transaction boundary nên được kiểm tra bằng ma trận thay vì annotation. Với mỗi
operation, ghi bước nào nằm trong transaction và state nào còn tồn tại nếu process
chết sau bước đó:

| Bước | Boundary | Nếu process chết |
|---|---|---|
| validate command | ngoài | không có state |
| ghi aggregate | trong | commit hoặc rollback |
| ghi outbox | trong | event còn để dispatcher đọc |
| gọi payment API | ngoài | cần idempotency/query status |
| cập nhật projection | thường ngoài | replay từ event |

Nếu invariant yêu cầu hai row cùng đúng, constraint/transaction phải bảo vệ chúng.
Nếu invariant kéo dài qua service hoặc thời gian, dùng state machine và
reconciliation thay vì cố kéo một transaction phân tán.

Đọc rồi ghi trong hai transaction riêng có thể mất update dù mỗi transaction đều
thành công. Chọn optimistic version check khi conflict hiếm; chọn locking khi
critical section ngắn và conflict thường xuyên. Đo lock wait, deadlock và
transaction duration thay vì chỉ nhìn throughput.

## Bài tập suy luận

Thiết kế migration thêm `status=ARCHIVED` trong rolling deploy: schema expand,
code tương thích, backfill, index rollout, contract và rollback nếu backfill mới
chạy 30%.

## Connection pool và read consistency

Connection pool là shared concurrency budget, không phải cách làm cho database
nhanh hơn. Pool quá lớn gây contention và làm database chết nhanh hơn; quá nhỏ
tạo queueing trong application. Theo dõi active/idle/awaiting connections,
acquire latency, transaction duration và timeout theo pool.

Read replica tạo thêm consistency contract. Sau một write, read-your-write có
thể cần primary route, session stickiness hoặc version token; không nên giấu
replica lag bằng retry vô hạn. Nếu endpoint chấp nhận eventual consistency, trả
version/updated-at để client biết dữ liệu có thể chưa phản ánh mutation mới.

Data retention là một phần của schema lifecycle: partition/archival, delete
cascade, audit retention và backup expiry phải được thiết kế cùng migration.
Không dùng ORM cascade như bằng chứng rằng mọi bản sao, cache hay event đã được
xóa.
