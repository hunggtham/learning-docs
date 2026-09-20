# Page faults, reclaim, dirty pages và memory pressure

Virtual memory tạo cảm giác mỗi process có một address space lớn và liên tục, nhưng physical memory hữu hạn. Khi workload tăng, kernel phải quyết định page nào giữ trong RAM, page nào có thể bỏ, page nào phải ghi ra storage và khi nào allocation nên bị throttled hoặc thất bại. Đây là vùng mà “còn bao nhiêu MB free” trở thành một chỉ số quá đơn giản.

## Page fault không đồng nghĩa lỗi nghiêm trọng

**Page fault (페이지 폴트)** xảy ra khi CPU không thể hoàn tất memory access bằng page-table state hiện tại và chuyển quyền xử lý cho kernel. Nhiều page fault là bình thường.

**Minor fault** có thể được xử lý mà không đọc dữ liệu từ disk, ví dụ anonymous page mới, copy-on-write sau `fork`, hoặc mapping đã có page trong page cache nhưng chưa map vào process. **Major fault** cần I/O để đưa dữ liệu vào RAM nên latency lớn hơn nhiều.

Vì vậy page-fault count phải được phân loại. Một application tạo nhiều minor faults lúc startup không nhất thiết có vấn đề; major faults tăng mạnh dưới load có thể báo hiệu working set không còn fit RAM.

## Working set và locality

Một process không cần toàn bộ address space nằm trong RAM cùng lúc. Nó cần **working set** — tập page đang được truy cập trong khoảng thời gian hiện tại. Virtual memory hiệu quả khi tổng active working set của hệ thống phù hợp physical memory.

Khi working set vượt capacity, kernel liên tục evict page rồi lại phải đọc chúng vào. Nếu phần lớn thời gian dành cho paging thay vì useful work, hệ thống rơi vào **thrashing**.

## File-backed và anonymous memory

File-backed page có nguồn gốc từ file. Nếu page sạch, kernel có thể bỏ nó vì có thể đọc lại từ storage. Anonymous memory như heap/stack không có file backing trực tiếp; để reclaim, hệ thống có thể cần swap hoặc phải giữ page.

Dirty file-backed page cũng không thể bỏ ngay: nội dung mới phải được write back trước. Do đó cùng “1 GB memory” nhưng reclaim cost khác nhau tùy page type và dirty state.

## Dirty pages và writeback

Application ghi file thông qua buffered I/O thường chỉ sửa page cache trước. Write syscall có thể return trước khi dữ liệu thực sự bền trên storage. Kernel writeback dirty pages theo policy và threshold.

Nếu dirty data tích tụ quá nhanh, kernel có thể throttle writer để storage bắt kịp. Đây là lý do latency của một write tưởng như memory-speed đôi lúc tăng đột biến: cost đã bị trì hoãn và cuối cùng phải trả.

Durability requirement như `fsync` thay đổi contract: application yêu cầu kernel/storage đưa dữ liệu tới mức persistence phù hợp trước khi return. Performance của database WAL phụ thuộc rất mạnh vào path này.

## Reclaim không chỉ xảy ra khi free = 0

Kernel duy trì watermarks và cố gắng reclaim trước khi hết memory hoàn toàn. Background reclaim có thể scan các page ít active; direct reclaim có thể buộc allocating thread tự tham gia reclaim, làm request latency tăng.

Vì vậy memory pressure thường xuất hiện trong latency trước khi OOM. Allocation chậm, reclaim CPU tăng, major fault tăng và I/O bận có thể là các dấu hiệu sớm.

## Page cache vừa là memory dùng vừa là memory có thể tái sử dụng

Trên Linux, RAM “used” cao không tự động xấu vì kernel tận dụng memory rảnh làm page cache. Cache này tăng file I/O performance và có thể bị reclaim khi application cần memory.

Điều cần quan sát là **available memory**, reclaim behavior, swap activity, PSI/memory pressure và workload working set, không chỉ cột `free`.

## OOM và cgroup

Khi hệ thống không thể thỏa allocation sau reclaim, kernel có thể kích hoạt out-of-memory handling. Trong container, cgroup memory limit tạo một boundary riêng: host còn RAM nhưng container vẫn có thể bị OOM nếu vượt limit.

Điều này rất quan trọng với JVM, database hoặc cache service. Heap limit không phải toàn bộ process memory; native buffers, thread stacks, mapped files, JIT metadata và page cache interaction vẫn tiêu thụ resource ngoài heap.

## Production example

Giả sử Java service có heap 6 GB trong container limit 8 GB. Khi traffic tăng, heap vẫn dưới 6 GB nhưng direct buffers, thread stacks và filesystem cache làm cgroup tiến gần limit. Reclaim tăng, request thread đôi lúc bị direct reclaim, tail latency tăng rồi process bị OOM-killed. Chỉ nhìn JVM heap graph sẽ dẫn đến kết luận sai.

## Mental model

> Memory pressure là bài toán working set và reclaim cost, không phải chỉ “RAM đã dùng bao nhiêu”. Page fault là cơ chế demand mapping; reclaim là quyết định bỏ page nào; dirty page biến reclaim thành I/O; cgroup thêm resource boundary. Khi pressure tăng, latency thường xấu đi trước khi allocation thực sự thất bại.