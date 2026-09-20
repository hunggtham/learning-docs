# Virtual memory và address spaces

Nếu programs dùng physical addresses trực tiếp, chúng có thể đè memory nhau, relocation khó và mỗi process phải biết layout RAM thật. Virtual memory (가상 메모리 / bộ nhớ ảo) thêm một translation layer: program dùng virtual addresses, MMU + page tables map chúng tới physical frames hoặc trạng thái chưa resident.

## Address space như private coordinate system

Mỗi process thường thấy một virtual address space riêng. Cùng virtual address `0x...` trong hai processes có thể map tới physical pages khác. Điều này tạo isolation và cho loader đặt code/heap/stack theo consistent conventions.

Virtual memory không có nghĩa OS “tạo RAM vô hạn”. Nó là mapping abstraction; khi working set vượt physical memory, paging/storage pressure làm performance giảm mạnh.

## Pages và page tables

Address space chia thành virtual pages; physical RAM chia frames. Virtual address tách page number + offset. Page table entry chứa physical frame và permission/status bits.

Page size thường vài KiB nhưng huge pages lớn hơn. Smaller pages giảm internal fragmentation; larger pages giảm page-table/TLB overhead.

## TLB

Page table walk qua multiple levels tốn memory accesses. TLB cache translations gần đây. TLB miss không phải page fault: page có thể resident nhưng translation chưa cache. Page fault xảy ra khi current mapping cần OS intervention.

## Page fault và demand paging

Khi process access virtual page chưa mapped/resident, CPU traps kernel. OS có thể allocate zero page, load file-backed page, copy-on-write hoặc reject invalid access.

Major page fault có thể cần storage I/O; minor fault chỉ mapping/memory work. Vì vậy “page fault count” cần context.

## Copy-on-write

Fork/snapshot có thể share physical pages read-only giữa processes. Khi một bên write, fault trigger copy riêng page. Copy-on-write tránh eager copy toàn memory nếu phần lớn pages không đổi.

COW xuất hiện cả filesystem snapshots và data structures: same mental model “share until mutation”.

## Memory-mapped files

`mmap` map file pages vào address space. Reads/writes trở thành memory accesses và OS page cache quản lý loading/dirty pages. Nó có thể giảm copying và đơn giản random access, nhưng durability, truncation và error semantics cần hiểu.

## Heap và stack growth

Language runtime heap allocator quản lý virtual regions đã được OS cấp. Stack thường có mapped region/guard page và grow policy. “Out of memory” có thể đến từ address-space limits, commit, cgroup, physical memory hoặc runtime heap policy.

## Swapping và thrashing

Nếu active working set lớn hơn RAM, OS liên tục evict/load pages. Thrashing xảy ra khi time dành cho paging nhiều hơn useful computation. Locality chính là yếu tố cứu hierarchy.

## Protection bits và NX

Page permissions read/write/execute giúp enforce isolation. W^X policy tránh page vừa writable vừa executable; NX bit giúp chặn một class code injection. ASLR randomize mappings để tăng khó exploitation, dù không phải security guarantee độc lập.

## Mental Model

> Virtual address là **tên logic**, physical frame là **vị trí hiện tại**. Page table là mapping + permissions; TLB cache mapping; page fault là lúc mapping cần kernel xử lý.

## Common Misconceptions

**“Virtual memory = swap.”** Swap chỉ là một mechanism có thể hỗ trợ. VM chủ yếu là address translation, isolation, mapping và paging abstractions.

**“Page fault luôn do bug.”** Demand paging/COW tạo faults bình thường; invalid/protection fault mới có thể thành crash.

**“Malloc 1 GB nghĩa ngay lập tức dùng 1 GB physical RAM.”** Overcommit/lazy allocation/runtime behavior có thể khác; actual committed/resident pages thay đổi khi touched.

## Kết nối

MMU/TLB từ [memory hierarchy](../02_computer_architecture/02_memory_hierarchy_and_cache.md); process abstraction ở [kernel](./00_kernel_syscalls_and_os_abstractions.md); language heap/GC ở [types and memory management](../04_programming_languages/01_types_values_references_and_memory.md); security permissions ở [vulnerabilities](../07_security_reliability/03_software_vulnerabilities.md).
