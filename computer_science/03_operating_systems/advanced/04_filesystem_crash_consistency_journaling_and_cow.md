# Filesystem crash consistency, journaling và copy-on-write

Filesystem phải biến một chuỗi writes có thể bị ngắt bất kỳ lúc nào thành trạng thái sau reboot vẫn có thể hiểu được. Vấn đề khó không nằm ở việc ghi bytes, mà ở việc nhiều metadata/data updates phải duy trì invariant dù mất điện giữa chừng.

## Một thao tác logic gồm nhiều writes vật lý

Tạo file có thể cần cập nhật directory entry, inode, free-space metadata và data blocks. Nếu crash sau khi một nửa đã persistent, filesystem có thể trỏ tới block chưa hợp lệ hoặc làm mất block khỏi free list.

**Crash consistency** hỏi: sau mọi điểm crash có thể xảy ra, on-disk state có nằm trong tập trạng thái hợp lệ và recoverable không?

## Page cache làm `write()` chưa đồng nghĩa durable

Application gọi `write()` thường chỉ copy data vào kernel page cache. Dirty pages được flush sau. Vì vậy syscall trả thành công không nhất thiết nghĩa bytes đã tới stable storage.

`fsync()`/`fdatasync()` cung cấp stronger durability contract, nhưng exact semantics còn phụ thuộc filesystem, device cache và ordering. Database WAL dựa rất mạnh vào contract này.

## Journaling

Journaling ghi description hoặc copy của updates vào log trước khi áp dụng chúng vào home locations. Sau crash, recovery replay hoặc bỏ transaction journal chưa hoàn tất.

Metadata journaling bảo vệ structure nhưng có thể không đảm bảo user data mới đã durable. Data journaling mạnh hơn nhưng tăng write amplification.

Journal không làm crash biến mất; nó biến recovery từ “đoán toàn filesystem” thành xử lý một protocol log có boundary rõ hơn.

## Write ordering và barriers

Nếu storage device reorder writes, filesystem cần barrier/flush semantics để đảm bảo journal commit record không persistent trước data mà nó tuyên bố bảo vệ. Đây là connection từ software protocol xuống hardware storage ordering.

Một durability design đúng ở filesystem layer có thể vẫn sai nếu device nói dối về flush hoặc mất volatile cache khi power loss.

## Copy-on-write filesystem

COW filesystem không overwrite structure đang live. Nó ghi block mới rồi cập nhật parent pointers, cuối cùng chuyển root/reference theo thứ tự an toàn. Snapshot trở nên tự nhiên vì old blocks vẫn tồn tại.

Nhưng COW tạo fragmentation và write amplification, đặc biệt với random overwrite workload. Database cũng có COW/B-tree variants với trade-off tương tự.

## Rename và atomicity

Pattern phổ biến khi cập nhật config là ghi file tạm, `fsync`, rồi atomic rename. Nhưng durability của rename và directory metadata vẫn cần hiểu contract filesystem. “Atomic” thường nói về visibility, không tự động bao hàm durability qua power failure.

## Database connection

Database dùng WAL vì không muốn phụ thuộc filesystem để atomically update hàng chục data pages. Nó append log record theo protocol riêng rồi flush. Filesystem lại dùng journal/COW để bảo vệ metadata của chính nó. Đây là nhiều lớp crash-consistency protocol xếp chồng.

Xem thêm: [MVCC, WAL và recovery internals](../../05_data_databases/advanced/00_mvcc_visibility_wal_and_recovery_internals.md).

## Mental Model

> Durability là một protocol ordering xuyên nhiều layers. `write()` tạo intent; page cache, filesystem, block layer và device quyết định khi nào intent thực sự sống sót qua crash. Muốn reasoning đúng phải biết boundary nào đã được flush và invariant nào recovery dựa vào.