# `mmap`, bộ nhớ ánh xạ tệp và quan hệ giữa memory với filesystem

`mmap()` là một trong những cơ chế quan trọng nhất để hiểu mối liên hệ giữa bộ nhớ ảo và hệ thống tệp. Thay vì yêu cầu ứng dụng đọc từng khối dữ liệu bằng `read()`, kernel có thể ánh xạ nội dung tệp vào không gian địa chỉ của tiến trình. Sau đó application truy cập dữ liệu như truy cập memory, còn kernel xử lý page fault và đưa dữ liệu từ page cache vào khi cần.

## `mmap()` giải quyết vấn đề gì?

Giả sử ứng dụng cần đọc một tệp lớn. Cách truyền thống:

```text
read()
→ kernel đọc dữ liệu vào page cache
→ copy từ kernel/page cache sang user buffer
→ application xử lý
```

Với memory mapping:

```text
mmap(file)
→ tạo vùng địa chỉ ảo gắn với file
→ application dereference memory
→ page fault khi trang chưa resident
→ kernel đưa trang file vào page cache và map vào process
```

Điều này có thể giảm một số lần copy và giúp access ngẫu nhiên thuận tiện hơn, nhưng không có nghĩa `mmap()` luôn nhanh hơn `read()`.

## VMA là gì?

Không gian địa chỉ của tiến trình được chia thành các **vùng bộ nhớ ảo (Virtual Memory Area / VMA)** có thuộc tính như:

- khoảng địa chỉ;
- quyền đọc/ghi/thực thi;
- anonymous hay file-backed;
- shared hay private;
- file offset nếu ánh xạ tệp.

Quan sát:

```bash
cat /proc/<PID>/maps
pmap -x <PID>
```

Một JVM thường có rất nhiều VMA cho heap, shared library, JIT code cache, thread stack, memory-mapped JAR/class data và native allocation.

## File-backed và anonymous memory

**File-backed memory** có backing store là file. Nếu trang sạch bị reclaim, kernel có thể bỏ trang khỏi RAM và đọc lại từ file khi cần.

**Anonymous memory** không gắn với file cụ thể, ví dụ heap/stack thông thường. Khi cần reclaim, các trang anonymous có thể phải swap nếu muốn giải phóng RAM mà vẫn giữ nội dung.

Đây là khác biệt quan trọng khi đọc memory pressure.

## `MAP_SHARED` và `MAP_PRIVATE`

`MAP_SHARED` cho phép thay đổi trên mapping có thể được nhìn thấy qua các mapping khác và có thể ghi lại xuống file tùy semantics.

`MAP_PRIVATE` dùng copy-on-write. Ban đầu trang có thể chia sẻ với page cache; khi process ghi, kernel tạo bản sao riêng và thay đổi đó không ghi ngược lại file.

Ví dụ khái niệm:

```text
MAP_PRIVATE
file page ──shared read──> process
              ↓ write
          copy-on-write
              ↓
       private anonymous page
```

## Page fault khi truy cập mapping

Gọi `mmap()` không có nghĩa toàn bộ file được đọc vào RAM ngay. Kernel chủ yếu thiết lập metadata mapping.

Khi code truy cập một địa chỉ chưa resident, CPU gây **page fault**. Kernel xác định VMA tương ứng, kiểm tra quyền và tìm/đọc trang cần thiết.

Nếu trang đã có trong page cache, đây có thể là minor fault. Nếu cần I/O để lấy dữ liệu từ storage, có thể trở thành major fault.

```bash
/usr/bin/time -v command
pidstat -r -p <PID> 1
```

## `mmap()` không loại bỏ page cache

Một hiểu lầm phổ biến là `mmap()` “đọc trực tiếp file vào process mà không qua cache”. Với file mapping thông thường, page cache vẫn là thành phần cốt lõi.

`read()` và `mmap()` có thể cùng nhìn cùng underlying cached file pages.

Điều này nối trực tiếp tới [VFS, page cache và writeback](../01_filesystem/vfs_page_cache_writeback.md).

## Memory-mapped write và durability

Ghi vào `MAP_SHARED` làm trang trở thành dirty. Kernel có thể write back xuống file sau đó.

Nhưng “đã ghi vào memory” không đồng nghĩa dữ liệu đã bền trên storage.

Application có thể cần `msync()` và/hoặc các semantics durability phù hợp, tùy use case.

Database và storage engine thường rất cẩn thận với ordering giữa data, WAL và flush.

## `msync()` không phải phép màu

`msync()` yêu cầu đồng bộ các trang mapping theo flags đã chọn, nhưng durability cuối cùng vẫn phụ thuộc filesystem, block layer, device cache và storage backend.

Mô hình vẫn là:

```text
application dirty page
→ kernel writeback
→ filesystem
→ block layer
→ device/controller
→ durable medium
```

## Shared memory bằng `mmap`

Hai process có thể map cùng file hoặc shared memory object và dùng vùng đó để trao đổi dữ liệu.

Ưu điểm là tránh copy nhiều lần giữa process. Nhưng synchronization trở thành trách nhiệm lớn: semaphore, futex, atomic operation hoặc protocol riêng cần bảo đảm consistency.

Shared memory nhanh không có nghĩa đơn giản.

## `tmpfs` và shared memory

`tmpfs` là filesystem dùng memory và có thể swap tùy cấu hình. `/dev/shm` thường là tmpfs dùng cho POSIX shared memory.

```bash
df -h /dev/shm
mount | grep tmpfs
```

Một container có thể có `/dev/shm` rất nhỏ mặc định, gây lỗi cho application dùng shared memory lớn.

## Executable mapping và shared library

Khi chạy ELF binary, code và shared libraries thường được memory-map vào process.

```bash
cat /proc/<PID>/maps | grep '\.so'
```

Nhiều process có thể chia sẻ các physical pages sạch chứa code của cùng shared library. Điều này tiết kiệm RAM.

## `mmap` và Java

Java sử dụng memory mapping ở nhiều nơi:

- `MappedByteBuffer`;
- class/JAR access tùy runtime;
- native library;
- code cache;
- memory-mapped files của database/search engine.

`MappedByteBuffer` có thể làm RSS/page cache tăng mà heap dump không phản ánh đầy đủ, vì đây không phải chỉ heap object data.

Do đó khi JVM có RSS lớn hơn `-Xmx`, memory mapping là một trong nhiều nguồn cần xem.

## Direct buffer và mmap khác nhau

Java `DirectByteBuffer` thường dùng native memory bên ngoài Java heap. Nó không nhất thiết là file-backed mapping.

Không nên gom mọi “off-heap” vào một loại.

Các nhóm có thể gồm:

- anonymous native allocation;
- thread stacks;
- direct buffers;
- JIT/code cache;
- file mappings;
- shared libraries.

## Address space reservation khác resident memory

Process có thể reserve vùng địa chỉ lớn nhưng chỉ một phần trang thực sự resident.

Đây là lý do VSZ/VIRT rất lớn không đồng nghĩa RAM vật lý tương ứng.

```bash
pmap -x <PID>
cat /proc/<PID>/smaps_rollup
```

`smaps` cung cấp chi tiết như RSS, PSS, shared/private dirty/clean cho từng mapping.

## PSS và shared pages

RSS tính toàn bộ resident pages thấy bởi process, kể cả trang chia sẻ. **PSS (Proportional Set Size)** chia chi phí trang shared theo số process sử dụng, nên hữu ích hơn khi muốn ước lượng footprint thực tế trong một số tình huống.

Không metric nào hoàn hảo cho mọi câu hỏi; cần biết đang đo gì.

## `madvise()` và access pattern

Application có thể đưa hint cho kernel bằng `madvise()` về access pattern, ví dụ sequential, random hoặc pages không còn cần.

Kernel có thể dùng hint để điều chỉnh read-ahead/reclaim.

Đây là tối ưu nâng cao; không nên dùng nếu chưa đo workload.

## `mlock()`

`mlock()` giữ trang không bị swap/reclaim theo semantics tương ứng. Hữu ích với một số workload nhạy latency hoặc secret material nhưng có thể gây áp lực memory nếu dùng quá rộng.

Giới hạn:

```bash
ulimit -l
```

Database đôi khi dùng locked memory hoặc huge pages theo configuration cụ thể.

## Huge pages và mapping

Transparent Huge Pages hoặc explicit huge pages có thể giảm TLB pressure, nhưng có trade-off về allocation latency, fragmentation và workload behavior.

Không nên bật/tắt theo “best practice” chung chung.

## SIGBUS khi file mapping thay đổi

Một failure mode quan trọng: process map file rồi file bị truncate nhỏ hơn vùng mapping. Truy cập phần mapping không còn backing hợp lệ có thể gây `SIGBUS`.

Đây là lỗi khác segmentation fault thông thường và thường xuất hiện ở hệ thống dùng mmap mạnh.

## File replacement và mapping cũ

Nếu một pathname bị rename để trỏ tới inode mới, process đã mmap inode cũ vẫn có thể tiếp tục nhìn dữ liệu cũ. Pathname và object lifetime là hai khái niệm khác nhau.

Điều này giống file descriptor mở trước khi file bị unlink.

## Mô hình tư duy

Hãy coi `mmap()` là cách tạo **liên kết giữa vùng địa chỉ ảo và backing object**:

```text
virtual address
    ↓ VMA
page table
    ↓
physical page
    ↕
page cache / anonymous memory
    ↕
file hoặc swap/storage
```

Application truy cập memory, còn kernel biến access đó thành page fault, cache lookup, I/O hoặc copy-on-write khi cần.

## Những hiểu lầm phổ biến

**“`mmap()` đọc toàn bộ file vào RAM.”** Không; mapping thường lazy và trang được đưa vào khi cần.

**“mmap không dùng page cache.”** File-backed mmap thường gắn chặt với page cache.

**“Ghi vào mmap nghĩa là dữ liệu đã durable.”** Dirty page vẫn cần writeback/flush semantics.

**“RSS lớn hơn heap nghĩa là memory leak.”** Mapping, direct buffer, stack và native memory đều có thể đóng góp.

**“`MAP_PRIVATE` sửa luôn file.”** Write private mapping thường dùng COW và không ghi ngược file.

## Kết nối kiến thức

Chương này nối [bộ nhớ ảo sâu](./virtual_memory_page_fault_reclaim_allocator.md), [VFS/page cache](../01_filesystem/vfs_page_cache_writeback.md), [ELF/dynamic linking](../08_operations/elf_dynamic_linking.md) và [Java incident playbook](../09_production/java_backend_incident_playbook.md).