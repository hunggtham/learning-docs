# Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM

Chương [Bộ nhớ, bộ nhớ ảo, page cache và OOM](./memory_virtual_memory.md) cung cấp mô hình tổng quan. Chương này đi sâu vào các cơ chế bên dưới để giải thích vì sao một tiến trình có thể có `VSZ` rất lớn nhưng chưa dùng nhiều RAM, vì sao truy cập một địa chỉ hợp lệ vẫn gây page fault, vì sao kernel phải reclaim memory, và tại sao hệ thống có thể bắt đầu chậm rất lâu trước khi OOM killer xuất hiện.

## Không gian địa chỉ ảo không phải RAM được cấp phát sẵn

Khi một tiến trình có một vùng địa chỉ ảo, điều đó không có nghĩa mọi byte tương ứng đã có khung trang vật lý trong RAM.

Kernel có thể chỉ ghi nhận một **vùng ánh xạ bộ nhớ (memory mapping)**. Khung trang vật lý được cấp khi tiến trình thực sự truy cập, tùy loại mapping.

Ví dụ conceptual:

```text
virtual address space
0x1000 ────────────────┐
                      │ mapped region
0x9000 ────────────────┘

physical RAM:
chưa chắc có frame cho mọi virtual page
```

Cơ chế này cho phép process đặt trước không gian địa chỉ lớn mà không lập tức tiêu thụ lượng RAM tương ứng.

## VMA: vùng bộ nhớ ảo

Kernel quản lý các vùng địa chỉ có cùng thuộc tính dưới dạng **VMA (Virtual Memory Area)**.

Có thể quan sát qua:

```bash
cat /proc/<PID>/maps
```

hoặc chi tiết hơn:

```bash
cat /proc/<PID>/smaps
```

Các vùng có thể đại diện:

- executable code;
- shared libraries;
- heap;
- stack;
- memory-mapped files;
- anonymous mappings;
- special mappings của kernel/runtime.

Một JVM thường có nhiều mapping và vùng reserve lớn, vì vậy nhìn `VIRT` riêng lẻ rất dễ gây hiểu nhầm.

## Page table và MMU

CPU dùng **MMU (Memory Management Unit)** để dịch địa chỉ ảo thành địa chỉ vật lý dựa trên page table do kernel quản lý.

Có thể hình dung:

```text
virtual address
   ↓
page-table walk
   ↓
physical frame
```

Nếu mapping không có hoặc permission không phù hợp, CPU tạo exception để kernel xử lý.

## TLB

Page-table walk có thể cần nhiều lần truy cập memory. CPU vì vậy dùng **TLB (Translation Lookaside Buffer)** để cache kết quả dịch địa chỉ.

Nếu working set lớn hơn khả năng TLB, **TLB miss** tăng và CPU phải thực hiện nhiều page-table walk hơn.

Huge pages có thể giúp giảm số entry cần thiết trong TLB cho workload lớn, nhưng đổi lại có trade-off về allocation, fragmentation và flexibility.

## Page fault không nhất thiết là lỗi

Tên **page fault** dễ làm người mới nghĩ hệ thống đang gặp lỗi. Thực ra page fault là một cơ chế bình thường để kernel hoàn thiện mapping khi process truy cập một trang chưa sẵn sàng.

Có hai nhóm quan trọng:

- **minor page fault** — không cần đọc dữ liệu từ storage chậm;
- **major page fault** — cần lấy dữ liệu từ backing storage, thường đắt hơn đáng kể.

Quan sát:

```bash
pidstat -r 1
```

hoặc:

```bash
ps -o pid,min_flt,maj_flt,cmd -p <PID>
```

Tên field cụ thể có thể phụ thuộc công cụ.

## Demand paging

Linux thường dùng **nạp trang theo nhu cầu (demand paging)**.

Ví dụ khi executable được map, kernel không nhất thiết đọc toàn bộ binary vào RAM. Chỉ khi code path cần một trang chưa resident, page fault mới kéo dữ liệu vào.

Điều này giúp startup và memory efficiency tốt hơn.

## Copy-on-write sau `fork()`

Sau `fork()`, kernel không cần copy toàn bộ memory của parent ngay lập tức. Parent và child có thể tạm chia sẻ các page vật lý ở chế độ chỉ đọc.

Nếu một bên ghi vào page, page fault xảy ra và kernel tạo bản copy riêng. Đây là **copy-on-write (COW)**.

Mental model:

```text
before write:
parent ─┐
        ├── same physical page
child  ─┘

after child write:
parent ─── old page
child  ─── copied page
```

COW giúp `fork()` tương đối rẻ ban đầu, nhưng chi phí thực xuất hiện khi nhiều pages bị ghi sau đó.

## Anonymous memory và file-backed memory

**Anonymous memory** không gắn trực tiếp với file cụ thể, ví dụ heap hoặc nhiều vùng `malloc`.

**File-backed memory** gắn với file hoặc shared object.

Khi reclaim:

- clean file-backed page có thể bị bỏ khỏi RAM rồi đọc lại từ file sau;
- dirty file-backed page cần writeback trước;
- anonymous page muốn reclaim có thể cần swap nếu còn cần giữ nội dung.

Đây là lý do page cache thường dễ reclaim hơn anonymous working set.

## `malloc()` không đồng nghĩa kernel cấp page ngay

Trong native application, `malloc()` thường được C allocator xử lý ở user space trước. Allocator có thể lấy vùng lớn từ kernel rồi chia nhỏ cho nhiều allocation.

Các cơ chế kernel thường liên quan gồm:

- `brk()` / heap growth;
- `mmap()` cho mapping lớn hoặc riêng;
- page fault để cấp physical page khi chạm vào vùng nhớ.

Vì vậy application allocation, virtual mapping và physical residency là ba tầng khác nhau.

## Allocator fragmentation

Ngay cả khi tổng memory còn đủ, allocator có thể có fragmentation khiến việc sử dụng không hiệu quả.

Hai khái niệm:

- **internal fragmentation** — block được cấp lớn hơn nhu cầu;
- **external fragmentation** — free space bị chia nhỏ thành nhiều vùng khó dùng cho allocation lớn.

Trong kernel còn có vấn đề fragmentation theo order của buddy allocator.

## Buddy allocator

Kernel quản lý physical pages qua các allocator, trong đó **buddy allocator** là cơ chế nền tảng để cấp các block page có kích thước theo bậc lũy thừa hai.

Khi một block lớn bị chia thành hai “buddy”, các block có thể được hợp nhất lại khi cùng free.

Mô hình này hỗ trợ cấp phát nhanh nhưng contiguous allocation lớn có thể khó khi RAM bị phân mảnh.

## SLAB/SLUB allocator

Kernel cần cấp rất nhiều object nhỏ như inode structures, dentries, task structures, network objects.

Dùng page allocator trực tiếp cho từng object sẽ lãng phí. Linux vì vậy dùng object allocator như **SLUB** để cache các object cùng loại.

Có thể quan sát tổng quan:

```bash
slabtop
```

Nếu kernel memory tăng mạnh, không phải mọi memory pressure đều nằm ở user-process RSS.

## `/proc/meminfo` sâu hơn

Một số field hữu ích:

```bash
grep -E 'MemAvailable|Cached|Buffers|Slab|SReclaimable|SUnreclaim|AnonPages|Mapped|Dirty|Writeback|Swap' /proc/meminfo
```

Ý nghĩa quan trọng:

- `AnonPages` — anonymous pages;
- `Cached` — file-backed cache theo cách accounting của kernel;
- `Slab` — memory cho kernel object caches;
- `SReclaimable` — một phần slab có thể reclaim;
- `SUnreclaim` — slab khó hoặc không reclaim;
- `Dirty` — file-backed pages chưa ghi xuống;
- `Writeback` — pages đang writeback.

Không nên cộng trừ các field một cách máy móc vì accounting có overlap và semantics kernel-version dependent.

## Reclaim: kernel lấy lại RAM như thế nào?

Khi memory pressure tăng, kernel phải tìm pages có thể giải phóng.

Khái niệm tổng quát:

```text
memory pressure
   ↓
reclaim candidates
   ├─ clean file cache → drop
   ├─ dirty file pages → writeback rồi reclaim
   └─ anonymous pages → swap nếu có thể
```

Kernel cố giữ working set nóng và loại pages ít cần hơn.

## LRU là một mô hình gần đúng

Kernel dùng các danh sách và thuật toán để ước lượng pages hoạt động hay không hoạt động. Tài liệu thường nói “LRU”, nhưng implementation thực tế tinh vi hơn một LRU textbook thuần túy.

Kernel hiện đại có thể dùng **multi-generational LRU (MGLRU)** tùy version/configuration để cải thiện reclaim behavior.

Điểm cần nhớ là kernel phải trả lời câu hỏi: “page nào có xác suất ít được dùng lại nhất?”

## Direct reclaim

Nếu background reclaim không theo kịp, thread đang yêu cầu memory có thể tự phải tham gia reclaim. Đây gọi là **direct reclaim**.

Khi đó application latency có thể tăng dù OOM chưa xảy ra.

Một hệ thống có memory pressure nặng có thể biểu hiện:

```text
request latency tăng
CPU không quá cao
I/O tăng
kswapd hoạt động
process stalls
sau đó mới OOM nếu không phục hồi
```

Vì vậy OOM là điểm cuối; performance degradation có thể xuất hiện sớm hơn nhiều.

## `kswapd`

`kswapd` là kernel thread thực hiện background reclaim khi memory thấp hơn các watermark nhất định.

Nếu `kswapd` dùng CPU đáng kể và `vmstat` cho thấy swap/reclaim activity, memory pressure là giả thuyết mạnh.

## Memory watermark

Kernel giữ các watermark cho vùng memory để biết khi nào bắt đầu background reclaim và khi nào allocation phải chịu áp lực mạnh hơn.

Các tham số như:

```bash
sysctl vm.min_free_kbytes
```

ảnh hưởng reserve và reclaim behavior.

Không nên tuning nếu chưa hiểu workload và kernel memory model.

## PSI: Pressure Stall Information

Linux có **PSI (Pressure Stall Information)** để đo thời gian tasks bị stall vì thiếu CPU, memory hoặc I/O resources.

```bash
cat /proc/pressure/memory
cat /proc/pressure/cpu
cat /proc/pressure/io
```

Ví dụ:

```text
some avg10=...
full avg10=...
```

PSI rất hữu ích vì nó đo **tác động pressure lên workload**, không chỉ lượng tài nguyên đã sử dụng.

Memory usage 90% có thể bình thường nếu không stall; memory pressure thấp hơn nhưng direct reclaim liên tục lại có thể gây latency.

## Swap không chỉ là “RAM chậm”

Swap cho phép kernel di chuyển anonymous pages ít dùng ra storage để giữ RAM cho active working set và page cache.

Không có swap đôi khi làm OOM xảy ra sớm hơn trong một số workload; swap quá chậm hoặc thrashing lại có thể làm hệ thống gần như không phản hồi.

Cần phân biệt:

```text
swap đang chứa dữ liệu
≠
system đang swap liên tục
```

Quan sát activity:

```bash
vmstat 1
```

với `si` và `so`.

## Thrashing

**Thrashing** xảy ra khi hệ thống dành phần lớn thời gian di chuyển pages vào/ra memory thay vì chạy workload hữu ích.

Chuỗi điển hình:

```text
working set > RAM phù hợp
→ reclaim mạnh
→ page bị evict
→ ứng dụng cần lại page
→ page fault
→ I/O
→ lại evict page khác
```

Latency tăng cực mạnh trong khi throughput sụt.

## OOM killer

Khi kernel không thể đáp ứng allocation sau reclaim và các cơ chế khác, OOM killer có thể chọn process để terminate.

Kiểm tra:

```bash
journalctl -k | grep -i -E 'oom|out of memory|killed process'
```

OOM killer chọn nạn nhân dựa trên heuristic và `oom_score`.

```bash
cat /proc/<PID>/oom_score
cat /proc/<PID>/oom_score_adj
```

`oom_score_adj` cho phép ảnh hưởng khả năng process bị chọn. Không nên đặt mọi critical process thành “không bao giờ kill”, vì kernel vẫn cần cách phục hồi khi thật sự cạn memory.

## Cgroup OOM khác global OOM

Trong container/cgroup, workload có thể chạm `memory.max` dù host còn RAM.

Cgroup v2 cung cấp các file như:

```text
memory.current
memory.max
memory.events
memory.stat
```

Tùy môi trường, có thể xem trong `/sys/fs/cgroup`.

Nếu host còn 30 GB RAM nhưng container bị kill, cần kiểm tra cgroup trước khi kết luận kernel global OOM.

## `memory.high` và throttling

Cgroup v2 có `memory.high` như một ngưỡng pressure/throttling mềm hơn `memory.max`.

Khi vượt `memory.high`, workload có thể bị reclaim/throttle thay vì bị kill ngay.

Điều này tạo một tầng performance degradation trước hard limit.

## JVM và native memory

Java heap chỉ là một phần của process memory:

```text
Java heap
+ metaspace
+ code cache
+ thread stacks
+ direct buffers
+ GC structures
+ JNI/native libraries
+ mapped files
```

Có thể dùng:

```bash
jcmd <PID> VM.native_memory summary
```

nếu JVM được bật Native Memory Tracking phù hợp.

Khi RSS cao hơn `Xmx` nhiều, đây không nhất thiết là leak; cần phân rã các vùng native.

## Thread stack và số lượng thread

Mỗi thread có stack reservation. Nếu tạo hàng nghìn threads, native memory cho stacks có thể rất lớn.

Ví dụ conceptual:

```text
2000 threads × 1 MiB stack reservation
≈ 2 GiB virtual space
```

Physical residency thực tế có thể thấp hơn reservation, nhưng thread count vẫn ảnh hưởng memory và scheduler.

## Direct buffer

Java NIO có thể dùng direct buffer ngoài heap.

Nếu application dùng Netty hoặc NIO mạnh, heap có thể ổn nhưng RSS vẫn tăng do off-heap/direct memory.

Cần kết hợp JVM metrics với `/proc/<PID>/smaps` hoặc Native Memory Tracking.

## NUMA

Trên multi-socket server, CPU truy cập local NUMA memory nhanh hơn remote memory.

Quan sát:

```bash
numactl --hardware
numastat
```

NUMA imbalance có thể làm latency tăng dù tổng RAM còn nhiều.

Không nên pin memory/CPU tùy tiện; first-touch allocation và scheduler placement có thể ảnh hưởng lớn.

## Transparent Huge Pages

Linux có thể dùng **Transparent Huge Pages (THP)** để tự động gom pages lớn hơn.

Kiểm tra:

```bash
cat /sys/kernel/mm/transparent_hugepage/enabled
```

THP có thể cải thiện TLB efficiency nhưng một số database workload không thích latency từ compaction hoặc allocation. Vì vậy khuyến nghị phụ thuộc workload.

## Memory compaction

Để tạo contiguous block lớn hoặc huge page, kernel có thể phải **memory compaction** — di chuyển pages để tạo vùng liên tục.

Compaction có thể tạo latency spike trong một số trường hợp.

## Một case production: JVM không OOM heap nhưng container vẫn bị kill

Giả sử:

```text
container memory.max = 4 GiB
-Xmx = 3 GiB
```

Ngoài heap còn:

```text
metaspace 300 MiB
thread stacks 400 MiB
direct buffers 500 MiB
native/runtime 300 MiB
```

Tổng process/cgroup usage có thể vượt 4 GiB dù heap chưa đầy.

Giải pháp không phải chỉ tăng `Xmx`; ngược lại, đôi khi cần giảm heap để dành headroom cho native memory.

## Một case production: host còn RAM nhưng request latency tăng

Có thể memory pressure cục bộ trong cgroup hoặc reclaim activity làm workload stall.

Kiểm tra:

```bash
cat /proc/pressure/memory
vmstat 1
cat /sys/fs/cgroup/.../memory.events
```

Nếu `memory.high` events tăng hoặc PSI memory cao, đây là evidence tốt hơn chỉ nhìn `free -h`.

## Mô hình tư duy

Bộ nhớ Linux có thể nhìn thành bốn lớp:

```text
virtual address space
      ↓
page tables / mappings
      ↓
physical pages
      ↓
reclaim / swap / cgroup policy
```

Một process có thể có mapping nhưng chưa resident. Một page có thể resident rồi bị reclaim. Một cgroup có thể hết quota dù host chưa hết RAM.

## Những hiểu lầm phổ biến

**“Page fault luôn là lỗi.”** Minor fault là một phần bình thường của demand paging.

**“`malloc(1GB)` nghĩa là lập tức dùng 1 GB RAM.”** Virtual allocation và physical residency có thể xảy ra ở thời điểm khác.

**“OOM là dấu hiệu đầu tiên của memory pressure.”** Reclaim, PSI stall và latency tăng thường xuất hiện trước.

**“Không có swap luôn tốt hơn.”** Tùy workload; không swap có thể làm OOM sớm hơn, còn swap quá mạnh có thể gây thrashing.

**“`Xmx=4G` thì container 4G là đủ.”** JVM còn native/off-heap memory.

**“RSS cộng lại bằng đúng RAM used.”** Shared pages và kernel accounting làm phép cộng đơn giản sai.

## Kết nối kiến thức

Đọc [VFS, page cache và writeback](../01_filesystem/vfs_page_cache_writeback.md) để hiểu file-backed memory, [Namespace và cgroup](../09_production/namespaces_cgroups_seccomp.md) để hiểu memory controller, và [Capacity planning](../09_production/capacity_planning_server_sizing.md) để chuyển memory model thành sizing thực tế.