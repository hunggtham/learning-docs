# Memory pressure, reclaim, dirty pages và page faults

“Máy còn bao nhiêu RAM trống?” là câu hỏi quá đơn giản để hiểu memory behavior của OS. Kernel cố dùng RAM làm page cache, anonymous memory, buffers và metadata vì RAM bỏ trống không tạo giá trị. Vấn đề thực sự là: **khi cần page mới, kernel có thể thu hồi page nào với cost bao nhiêu?**

## Free memory và available memory khác nhau

Free pages có thể dùng ngay. Nhưng page cache sạch cũng có thể reclaim tương đối rẻ vì data vẫn tồn tại trên disk. Một hệ thống free RAM thấp vẫn khỏe nếu có nhiều reclaimable cache.

Ngược lại, free RAM còn nhưng workload allocation tăng nhanh, dirty pages lớn hoặc anonymous working set khó reclaim có thể sớm gây pressure.

Do đó “used RAM cao” không tự động là memory leak.

## Anonymous pages và file-backed pages

**File-backed pages** đại diện nội dung file/mmap. Nếu clean, kernel có thể drop và đọc lại sau.

**Anonymous pages** như heap/stack không có bản gốc trong filesystem. Để reclaim mà vẫn bảo toàn data, OS cần swap hoặc phải giữ page trong RAM.

Điều này khiến anonymous memory pressure thường khác page-cache pressure.

## Page fault không đồng nghĩa lỗi nghiêm trọng

Page fault xảy ra khi CPU access virtual address nhưng page table hiện tại chưa cho translation hợp lệ theo yêu cầu.

**Minor fault** có thể được xử lý mà không cần disk I/O, ví dụ map một page đã có trong page cache hoặc allocate zero page/COW page.

**Major fault** cần storage I/O để lấy data, latency cao hơn nhiều.

Vì vậy metric page faults phải phân biệt loại và context.

## Demand paging

OS không cần map/load mọi page khi process start. Virtual address space có thể rất lớn nhưng physical pages chỉ được cấp khi access xảy ra.

Demand paging giảm startup/memory footprint nhưng đưa cost vào first-touch. Đây là trade-off lazy allocation quen thuộc xuyên nhiều layer system.

## Copy-on-write

Sau `fork`, parent và child có thể cùng map physical pages read-only. Khi một bên write, page fault xảy ra và kernel tạo private copy.

COW giúp fork rẻ nếu child sớm `exec`, nhưng workload ghi nhiều sau fork có thể tạo memory spike. Container/process model vì vậy liên hệ trực tiếp tới VM internals.

## Reclaim hoạt động như một eviction problem

Khi free pages xuống thấp, kernel scan candidate pages để reclaim. Mục tiêu là giữ working set nóng và loại page ít có khả năng dùng lại, nhưng OS không biết tương lai.

Reclaim policy dùng access/reference information, active/inactive generations hoặc heuristic tương tự cache replacement. Đây là cùng family problem với cache eviction, chỉ khác cost miss có thể rất lớn.

## Dirty pages làm reclaim đắt hơn

File-backed clean page có thể drop ngay. Dirty page phải write back trước khi reclaim nếu data cần persistence.

Nếu application ghi nhanh hơn storage flush, dirty data tích tụ. Kernel có thể throttle writer hoặc background flush. Khi pressure cao, process tưởng đang “ghi memory nhanh” có thể bất ngờ chịu writeback latency.

Đây là ví dụ buffered I/O che latency tạm thời chứ không xóa physical constraint.

## Swap và thrashing

Swap có thể giải phóng RAM bằng cách đẩy anonymous pages ra storage. Nhưng nếu working set lớn hơn RAM và pages liên tục bị swap out rồi fault back in, system rơi vào **thrashing**.

CPU có thể không full nhưng application gần như không tiến triển vì storage/page-fault loop.

Thrashing là failure mode của cache quá nhỏ so với active working set.

## Memory pressure và OOM

Khi kernel không reclaim đủ memory để đáp ứng allocation, nó phải fail allocation hoặc chọn process để kill tùy OS/policy.

Linux OOM killer dùng scoring/policy để chọn victim trong tình huống cực hạn. Container cgroup memory limit có thể gây OOM trong cgroup dù host còn RAM, vì resource boundary logic khác host-global availability.

Do đó production debugging phải hỏi “memory limit ở layer nào?” chứ không chỉ `free -m`.

## Direct reclaim và latency spike

Nếu allocation path tự phải reclaim pages, application thread có thể bị stall. Tail latency tăng dù average memory usage nhìn ổn.

Memory pressure metrics, reclaim activity, major faults, swap I/O và allocation stalls thường quan trọng hơn một snapshot phần trăm RAM.

## Huge pages và trade-off

Huge pages giảm số page-table entries và TLB misses cho workload lớn, nhưng allocation/compaction khó hơn và internal fragmentation có thể tăng.

Transparent huge page policy có thể giúp hoặc gây latency spikes tùy workload/kernel. Đây là ví dụ optimization cần quan sát production behavior, không chỉ bật vì “page lớn nhanh hơn”.

## Mental Model

> RAM trong OS là một **cache + backing strategy + allocation system**. Khi memory pressure tăng, câu hỏi chính là page nào reclaim được, reclaim cost bao nhiêu và working set có còn fit không.

## Common Misconceptions

**“RAM dùng 90% nghĩa sắp hết.”** Page cache reclaimable có thể chiếm phần lớn.

**“Page fault luôn cần disk.”** Minor fault không nhất thiết có I/O.

**“Swap chỉ xấu.”** Swap có thể tăng flexibility; vấn đề là working-set thrashing và latency không phù hợp workload.

## Kết nối

Foundation liên quan là virtual memory, page cache và filesystem. Tiếp theo roadmap đi sâu page tables/TLB shootdown. Ở tầng Database, buffer pool cạnh tranh hoặc hợp tác với OS page cache tùy engine; ở tầng JVM, GC heap sizing ảnh hưởng trực tiếp tới host memory pressure.