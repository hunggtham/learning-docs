# Page faults, reclaim, dirty pages và memory pressure

Virtual memory tạo cảm giác mỗi process có một address space lớn và liên tục, nhưng physical memory hữu hạn. Câu hỏi advanced không phải “còn bao nhiêu MB free?” mà là: **working set nào cần ở RAM, page nào reclaim được, reclaim cost bao nhiêu, và pressure ở tầng kernel biến thành latency/OOM ở application như thế nào?**

Invariant cốt lõi là kernel phải tiếp tục cung cấp abstraction virtual memory đúng trong khi tái sử dụng physical pages: page bị reclaim chỉ khi data có thể được bỏ hoặc có backing strategy hợp lệ; dirty state phải được write back đúng; mapping/permission phải nhất quán với page-table state.

## 1. Free memory và available memory khác nhau

Free pages dùng được ngay, nhưng clean page cache cũng có thể reclaim tương đối rẻ vì data vẫn tồn tại trên storage. Vì vậy RAM `used` cao không tự động nghĩa memory pressure.

Ngược lại, hệ thống còn một ít free RAM nhưng anonymous working set lớn, dirty pages cao và allocation tăng nhanh có thể đang rất gần pressure.

Mental model tốt hơn là:

```text
memory pressure
≈ demand cho physical pages
  so với
  lượng page reclaimable và cost để reclaim chúng
```

## 2. Page fault là control transfer, không đồng nghĩa lỗi nghiêm trọng

**Page fault (페이지 폴트)** xảy ra khi CPU không thể hoàn tất memory access bằng page-table state hiện tại và chuyển quyền xử lý cho kernel.

**Minor fault** có thể xử lý không cần storage I/O, ví dụ anonymous page mới, copy-on-write hoặc page đã nằm trong page cache nhưng chưa map vào process. **Major fault** cần I/O để đưa data vào RAM và thường đắt hơn nhiều.

Page-fault count không đủ. Cần biết loại fault, working-set context và latency hậu quả.

## 3. Demand paging đổi startup cost thành first-touch cost

OS không cần materialize toàn bộ virtual address space khi process start. Physical page có thể chỉ được cấp/map khi address thật sự được truy cập.

Demand paging giảm startup memory footprint nhưng đưa cost vào first touch. Đây là cùng mental model lazy work ở nhiều tầng: cost không biến mất, nó được dời thời điểm.

Nếu latency-sensitive path first-touch một vùng memory lớn, page faults có thể xuất hiện đúng lúc request đang chạy dù startup graph nhìn rất nhanh.

## 4. Working set mới quyết định system có khỏe hay không

**Working set** là tập pages workload đang truy cập trong window hiện tại. Virtual memory hoạt động tốt khi active working sets phù hợp với physical memory và locality đủ ổn định.

Nếu working set vượt capacity, kernel evict page rồi workload lại fault page đó trở vào. Khi hệ thống dành phần lớn thời gian cho paging/reclaim thay vì useful work, ta có **thrashing**.

Thrashing là failure mode của một cache có capacity nhỏ hơn active demand, không phải chỉ là “swap chậm”.

## 5. File-backed và anonymous memory có reclaim cost khác nhau

Clean file-backed page có thể drop và đọc lại từ file. Dirty file-backed page phải write back trước khi reclaim nếu thay đổi cần được giữ. Anonymous pages như heap/stack không có file origin trực tiếp; để reclaim mà giữ data, hệ thống cần swap hoặc mechanism backing tương đương.

Vì vậy cùng 1 GB memory nhưng physical pressure khác nhau rất nhiều tùy loại page và dirty state.

Điều này cũng giải thích vì sao JVM heap, native/direct buffer và mmap/page cache không thể gom thành một con số “process dùng RAM” đơn giản.

## 6. Copy-on-write: optimization có failure mode khi write pattern thay đổi

Sau `fork`, parent/child có thể cùng map pages read-only. Khi một bên write, page fault tạo private copy. **Copy-on-write (COW)** làm `fork` rẻ nếu child sớm `exec`, nhưng workload ghi nhiều sau fork có thể tạo memory spike.

Optimization dựa trên assumption “chia sẻ chủ yếu read”. Khi pressure/workload đổi, behavior cũng đổi. Đây là pattern lặp lại xuyên Computer Science: optimization trì hoãn resource cost dựa trên expected access pattern.

## 7. Reclaim là eviction problem của OS

Khi available memory giảm, kernel chọn candidate pages để reclaim. OS không biết tương lai nên phải dùng access/reference information và replacement heuristics.

Bài toán cùng family với cache replacement:

```text
page nào có reuse probability thấp?
miss/reload cost của nó là bao nhiêu?
page có dirty không?
reclaim nó có tạo I/O không?
```

Khác biệt là miss cost có thể từ microseconds tới milliseconds và có thể nằm trực tiếp trên request critical path.

## 8. Background reclaim và direct reclaim khác impact

Kernel thường cố reclaim trước khi free memory bằng 0, dựa trên watermarks/pressure thresholds. Background reclaim làm việc ngoài allocation path. Khi không đủ, allocating thread có thể bị kéo vào **direct reclaim**.

Direct reclaim rất quan trọng cho production latency: application thread tưởng đang allocate memory nhưng thực tế phải scan/reclaim/writeback trước khi allocation tiến tiếp.

Do đó tail latency có thể tăng trước OOM rất lâu.

## 9. Dirty pages biến memory pressure thành storage pressure

Buffered file write thường cập nhật page cache rồi return trước khi bytes bền trên storage. Dirty pages tích tụ nếu producer ghi nhanh hơn writeback throughput.

Khi dirty threshold/pressure tăng, kernel có thể throttle writer hoặc foreground allocation bị ảnh hưởng bởi writeback.

Causal chain:

```text
write burst
→ dirty page growth
→ background writeback / throttling
→ storage queue depth tăng
→ allocation/write latency tăng
→ application tail latency tăng
```

Đây là connection trực tiếp giữa memory subsystem và durability/storage behavior.

## 10. `fsync` thay đổi contract

Buffered write chỉ nói kernel đã nhận data; `fsync`/equivalent yêu cầu persistence mạnh hơn theo filesystem/device contract. Khi database WAL gọi durability primitive, dirty/writeback state và storage queue có thể quyết định commit latency.

Memory pressure và durability vì vậy không độc lập. Xem [đường durability xuyên tầng](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

## 11. Swap: flexibility tốt, thrashing mới là failure

Swap có thể giúp giữ infrequently used anonymous pages ngoài RAM để active working set dùng memory tốt hơn. Vấn đề xảy ra khi workload liên tục cần lại pages vừa swap out.

Nếu storage/page-fault loop chiếm phần lớn thời gian, CPU có thể không full nhưng system gần như không tiến triển. Chỉ nhìn CPU utilization dễ bỏ sót failure này.

## 12. Huge pages: giảm translation cost, tăng allocation/fragmentation pressure

Huge pages giảm số page-table entries và TLB pressure cho large-memory workload. Đổi lại allocation/compaction khó hơn, internal fragmentation có thể tăng và policy như transparent huge pages có thể tạo latency spikes tùy workload/kernel.

Không có invariant “page lớn luôn nhanh hơn”. Cần đo TLB benefit so với compaction/allocation cost.

## 13. cgroup tạo memory boundary riêng

Container memory limit có thể gây OOM trong cgroup dù host còn RAM. Điều này làm câu hỏi “máy còn memory không?” sai abstraction layer.

Ví dụ JVM heap 6 GB trong container limit 8 GB vẫn có thể OOM vì ngoài heap còn direct buffers, thread stacks, JIT/runtime metadata, native libraries và mapped/file-backed state.

Capacity phải reasoning trên **total resident/resource footprint tại boundary bị limit**, không chỉ managed heap.

## 14. OOM là failure cuối, không phải tín hiệu đầu tiên

Trước OOM, system thường đã có evidence:

```text
reclaim scan tăng
allocation/direct-reclaim stalls
major faults tăng
swap I/O tăng
memory pressure tăng
writeback/dirty pressure tăng
latency p95/p99 xấu đi
```

Nếu alert chỉ đợi process bị OOM-killed thì observability bắt failure quá muộn.

## 15. Production evidence

Evidence nên nối symptom application với kernel memory state:

```text
Application/runtime:
- RSS/native/direct memory, heap/GC state nếu managed runtime
- allocation rate và request latency

Kernel:
- available memory thay vì chỉ free
- minor/major faults
- reclaim scan/stall, direct reclaim
- dirty/writeback pages
- swap in/out
- memory pressure/PSI-like signals khi OS hỗ trợ
- cgroup memory current/limit/events

Storage correlation:
- device latency/queue depth trong thời điểm writeback/fault storm
```

Một heap graph đẹp không loại trừ host/cgroup pressure; một `free` snapshot cũng không chứng minh working set khỏe.

## 16. Lower abstraction nào quyết định behavior?

Nếu symptom là major-fault latency, tầng storage quyết định miss cost. Nếu symptom là COW spike, page mapping và write pattern quyết định allocation. Nếu container OOM trong khi host khỏe, cgroup boundary quyết định failure. Nếu dirty reclaim chậm, filesystem/block device throughput quyết định pressure propagation.

Advanced debugging phải theo contract tới đúng lower layer thay vì gắn nhãn chung “memory leak”.

## 17. Mô hình tư duy

> RAM trong OS là **working-set cache + backing strategy + allocation system**. Page fault là mechanism đưa mapping/data vào trạng thái dùng được; reclaim chọn page để tái sử dụng; dirty state biến reclaim thành I/O; cgroup tạo resource boundary; performance pressure xuất hiện thành stall/tail latency trước khi OOM. Câu hỏi đúng không phải “RAM dùng bao nhiêu?” mà là **resource nào reclaim được với cost nào, và request đang trả cost đó ở đâu?**

## Kết nối

Đọc tiếp [Virtual memory, page table và TLB shootdown](./03_virtual_memory_page_tables_tlb_shootdown_and_huge_pages.md), [Filesystem crash consistency](./04_filesystem_crash_consistency_journaling_and_cow.md), [Runtime GC](../../04_programming_languages/advanced/06_garbage_collection_generational_concurrent_compacting_and_barriers.md), [Database buffer pool](../../05_data_databases/advanced/04_buffer_pool_replacement_and_dirty_page_management.md) và [Durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).