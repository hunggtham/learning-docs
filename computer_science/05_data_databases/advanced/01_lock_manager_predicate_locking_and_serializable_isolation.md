# Lock manager, predicate locking và serializable isolation

MVCC cho phép nhiều transaction đọc các version khác nhau mà không phải khóa mọi row, nhưng concurrency control không biến mất. Khi transaction cùng sửa dữ liệu hoặc khi database cần guarantee mạnh như **serializable isolation**, engine vẫn phải reasoning conflict giữa operations.

## Lock manager quản lý quyền truy cập logic

Database lock không giống mutex trong application code. Lock manager theo dõi transaction nào đang giữ lock trên resource nào, mode nào tương thích và transaction nào phải chờ.

Shared lock thường cho nhiều reader cùng tồn tại; exclusive lock ngăn conflicting access. Engine còn có intent locks ở nhiều granularity để phối hợp row/page/table locking mà không cần kiểm tra từng row khi khóa table.

## Lock compatibility tạo wait-for relation

Nếu transaction T1 giữ lock mà T2 cần một incompatible lock, T2 phải chờ. Nhiều wait relation tạo **wait-for graph**. Cycle trong graph nghĩa là deadlock.

Database thường phát hiện deadlock rồi abort một victim thay vì cố bảo đảm deadlock không bao giờ xảy ra. Đây là lựa chọn thực dụng: transaction application phải được thiết kế để retry an toàn.

## Two-phase locking và serializability

Trong **Two-Phase Locking (2PL)**, transaction có phase acquire lock rồi phase release; strict variants giữ write locks tới commit/abort. Protocol này có thể tạo conflict-serializable schedule nhưng đổi lại blocking và deadlock.

MVCC-based database có thể dùng kỹ thuật khác, nhưng mental model vẫn là database phải ngăn một tập interleaving tạo kết quả không tương đương execution tuần tự nếu isolation level hứa serializable.

## Row lock chưa đủ cho predicate

Giả sử transaction kiểm tra:

```sql
SELECT COUNT(*) FROM booking
WHERE room_id = 10
  AND start_time < :end
  AND end_time > :start;
```

Kết quả bằng 0 rồi transaction chuẩn bị insert booking. Nếu hai transaction cùng chạy, cả hai có thể thấy 0 vì row “xung đột” chưa tồn tại để khóa. Đây là **phantom problem**.

Serializable protection phải reasoning không chỉ existing rows mà cả **predicate/range** — tập row có thể xuất hiện và làm thay đổi kết quả query.

## Predicate lock và next-key/range locking

Predicate locking lý tưởng khóa logic “mọi row thỏa điều kiện P”, nhưng implementation tổng quát rất đắt. B-tree database thường xấp xỉ bằng key-range hoặc next-key locks: khóa record cùng khoảng index liên quan để insert mới vào khoảng đó bị conflict.

Điều này giải thích vì sao index không chỉ ảnh hưởng performance. Access path có thể ảnh hưởng phạm vi lock và concurrency behavior.

## Serializable Snapshot Isolation

Một hướng khác là **Serializable Snapshot Isolation (SSI)**. Thay vì block mọi conflict trước, engine cho transaction đọc snapshot rồi theo dõi dependency patterns có thể tạo serialization anomaly. Khi phát hiện dangerous structure, một transaction bị abort.

Trade-off chuyển từ blocking sang optimistic execution + abort/retry. Workload ít conflict có thể hưởng lợi; workload conflict cao có thể tạo nhiều abort.

## Write skew

Snapshot isolation ngăn nhiều lost-update case nhưng vẫn có thể cho phép **write skew**. Ví dụ hai bác sĩ cùng on-call; rule yêu cầu luôn có ít nhất một người. Hai transaction cùng đọc thấy cả hai đang on-call, mỗi transaction tắt trạng thái của một người khác nhau. Chúng update hai rows khác nhau nên không write-write conflict, nhưng invariant toàn cục bị phá.

Serializable isolation phải nhận diện dependency rộng hơn “hai transaction sửa cùng row”.

## Application consequence

Chọn isolation level là chọn loại anomaly application chấp nhận. `READ COMMITTED` không “sai”; nó chỉ có contract yếu hơn và thường concurrency tốt hơn. Nếu business invariant phụ thuộc nhiều rows/predicates, application cần explicit locking, atomic constraint hoặc serializable transaction phù hợp.

Unique constraint, exclusion constraint hoặc conditional update thường đáng tin hơn pattern “SELECT kiểm tra rồi INSERT” vì invariant được đưa gần storage engine hơn.

## Mental model

> Concurrency control bảo vệ invariant qua thời gian. Row locks giải quyết một phần conflict; predicate/range protection xử lý dữ liệu chưa tồn tại; serializability yêu cầu toàn schedule tương đương một thứ tự tuần tự. Isolation càng mạnh thường đổi lấy blocking, abort hoặc bookkeeping lớn hơn.