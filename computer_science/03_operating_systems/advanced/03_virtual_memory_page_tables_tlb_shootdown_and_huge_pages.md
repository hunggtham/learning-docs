# Virtual memory internals: page tables, TLB shootdown và huge pages

Ở mức API, process thấy một dải virtual addresses gần như riêng tư. Ở mức kernel, abstraction đó phải được duy trì bằng page tables, permission bits, fault handling và coordination với CPU TLB. Virtual memory vì thế không chỉ là “dùng disk làm RAM”; nó là cơ chế isolation, relocation và demand allocation cốt lõi của OS.

## Address space là một contract

Hai processes có thể dùng cùng virtual address nhưng map tới physical frames khác nhau. Kernel kiểm soát mapping và permissions như read/write/execute, user/kernel. Isolation này là nền cho process security.

`mmap`, heap growth, shared libraries và file mappings đều là các cách xây dựng address space. Nhiều mapping ban đầu chỉ tạo metadata; physical page có thể chưa được cấp cho tới khi access gây fault.

## Multi-level page table

Một flat page table cho address space lớn sẽ lãng phí memory. Multi-level table chỉ materialize các nhánh cần thiết. Đổi lại translation có nhiều levels và cần TLB để không phải walk liên tục.

Kernel phải quản lý lifecycle của page-table pages, permission changes và synchronization khi nhiều threads cùng process chạy trên nhiều cores.

## Minor và major fault

**Minor page fault** không cần đọc dữ liệu từ storage: ví dụ page đã ở page cache nhưng chưa map vào process, hoặc anonymous page cần cấp mới. **Major page fault** cần I/O từ storage và có latency lớn hơn nhiều.

Page fault không tự động là lỗi. Demand paging cố ý dùng fault như control mechanism. Điều đáng quan tâm là frequency và cost trong context workload.

## Copy-on-write

Sau `fork`, parent và child có thể tạm share physical pages ở chế độ read-only. Khi một bên ghi, write fault khiến kernel copy page. **Copy-on-write (COW)** tránh copy toàn bộ address space ngay lập tức.

COW hiệu quả khi phần lớn pages không bị sửa; nếu child ghi gần hết memory, deferred copies vẫn xảy ra và có thể tạo latency/memory spike.

## TLB shootdown từ góc nhìn OS

Khi kernel unmap page hoặc giảm permission, CPU khác có thể còn stale TLB entry. Kernel phải gửi invalidation và chờ mức synchronization cần thiết. Với nhiều cores, frequent mapping changes có thể tạo scalability cost.

Đây là connection trực tiếp với [TLB và virtualization ở tầng architecture](../../02_computer_architecture/advanced/05_tlb_page_walkers_huge_pages_and_virtualization.md).

## Huge pages và THP

Huge pages tăng TLB reach nhưng làm physical allocation khó hơn. Linux Transparent Huge Pages cố tự động collapse pages nhỏ, nhưng compaction có thể tạo latency. Database thường cân nhắc explicit huge pages để kiểm soát behavior tốt hơn.

Không có policy đúng cho mọi workload. Memory fragmentation, latency sensitivity và access pattern quyết định trade-off.

## Overcommit và OOM

Một OS có thể cho processes reserve virtual memory lớn hơn physical RAM hiện có với giả định không phải mọi reservation đều được touch. Khi assumption sai và reclaim không đủ, hệ thống có thể vào memory pressure hoặc OOM handling.

Điều này giải thích vì sao “application đã allocate X GB” có nhiều nghĩa: virtual address reservation, committed anonymous memory, resident set và working set không đồng nhất.

## Mental Model

> Virtual memory là bảng ánh xạ có quyền truy cập và lifecycle, không phải một vùng RAM giả. Performance phụ thuộc vào locality của translation, fault behavior, reclaim và coordination giữa cores.