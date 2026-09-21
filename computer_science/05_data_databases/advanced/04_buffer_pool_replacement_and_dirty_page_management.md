# Buffer pool, replacement và dirty-page management

Database không thể giả định toàn bộ data nằm trong RAM. **Buffer pool** là cache page-level do database quản lý để giữ hot pages gần CPU, đồng thời kiểm soát khi nào dirty data được flush xuống storage.

## Vì sao database tự quản cache

OS đã có page cache, nhưng database cần biết transaction semantics, page identity, pinning và WAL ordering. Một engine dùng direct I/O có thể tránh double caching và tự quyết replacement/flush. Engine khác dựa nhiều hơn vào OS. Cả hai là design choices với trade-off riêng.

## Page lifecycle

Khi query cần page, engine tra buffer pool. Hit trả frame đang resident; miss phải chọn frame/victim, đọc page từ storage rồi cập nhật metadata.

Page đang được operator sử dụng thường được **pinned** để replacement không lấy nó giữa chừng. Pin leak có thể làm effective pool capacity giảm dần.

## Replacement policy

Pure LRU dễ bị scan lớn đẩy toàn bộ hot working set ra ngoài. Database thường dùng biến thể như clock, LRU-K hoặc scan-resistant policies để phân biệt one-time scan với repeated access.

Replacement đang ước lượng future reuse từ access history, tương tự CPU cache nhưng time scale và metadata budget khác nhiều.

## Dirty page

Page bị update trở thành dirty. Engine không nhất thiết flush ngay vì batch writes hiệu quả hơn. Nhưng trước khi data page chứa update mới được persistent, WAL record tương ứng phải durable theo **write-ahead rule**.

Điều này cho phép recovery redo update nếu crash sau WAL flush nhưng trước data-page flush.

## Checkpoint

Checkpoint giới hạn lượng WAL phải replay khi recovery và thúc đẩy dirty pages ra storage. Nếu checkpoint quá aggressive, foreground I/O bị cạnh tranh; quá lỏng, recovery dài và dirty backlog lớn.

Database phải smooth writeback thay vì dồn flush thành spike.

## Buffer pool và query plan

Cost optimizer thường ước lượng I/O, nhưng actual cache state làm latency khác nhau. Index lookup ngẫu nhiên có thể rất nhanh nếu pages hot, rất chậm nếu mỗi lookup miss storage.

Vì vậy benchmark warm cache và cold cache trả lời hai câu hỏi khác nhau.

## Double buffering

Nếu database cache page trong buffer pool và OS lại cache cùng block, memory bị duplicate. Direct I/O giảm duplication nhưng engine phải tự xử lý alignment, readahead và I/O scheduling nhiều hơn.

## Memory pressure

Buffer pool quá lớn có thể làm OS thiếu memory cho process stacks, page tables và filesystem metadata. Trên JVM application kết hợp database local, heap + off-heap + OS cache phải được tính chung.

## Mental Model

> Buffer pool là working-memory manager của database. Nó không chỉ cache reads; nó phối hợp replacement, pinning, dirty lifecycle và WAL để cân bằng latency, throughput và recovery.