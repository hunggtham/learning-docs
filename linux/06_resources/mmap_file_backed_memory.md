# `mmap`, bộ nhớ ánh xạ tệp và quan hệ giữa bộ nhớ (memory / 메모리) với filesystem

> **Mạch đọc:** Đọc **mmap, bộ nhớ ánh xạ tệp và quan hệ giữa bộ nhớ (memory / 메모리) với filesystem** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **mmap() giải quyết vấn đề gì?** sang **VMA là gì?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


`mmap()` là một trong những cơ chế quan trọng nhất để hiểu mối liên hệ giữa bộ nhớ ảo và hệ thống tệp. Thay vì yêu cầu ứng dụng đọc từng khối dữ liệu bằng `read()`, kernel có thể ánh xạ nội dung tệp vào không gian địa chỉ của tiến trình. Sau đó ứng dụng (application / 애플리케이션) truy cập dữ liệu như truy cập bộ nhớ (memory / 메모리), còn kernel xử lý page fault và đưa dữ liệu từ page bộ nhớ đệm (cache / 캐시) vào khi cần.

## `mmap()` giải quyết vấn đề gì?

Giả sử ứng dụng cần đọc một tệp lớn. Cách truyền thống:

```text
read()
→ kernel đọc dữ liệu vào page cache
→ copy từ kernel/page cache sang user buffer
→ application xử lý
```

Với bộ nhớ (memory / 메모리) ánh xạ (mapping / 매핑):

```text
mmap(file)
→ tạo vùng địa chỉ ảo gắn với file
→ application dereference memory
→ page fault khi trang chưa resident
→ kernel đưa trang file vào page cache và map vào process
```

Điều này có thể giảm một số lần bản sao (copy / 복사) và giúp truy cập (access / 접근) ngẫu nhiên thuận tiện hơn, nhưng không có nghĩa `mmap()` luôn nhanh hơn `read()`.

## VMA là gì?

Không gian địa chỉ của tiến trình được chia thành các **vùng bộ nhớ ảo (Virtual Memory Area / VMA)** có thuộc tính như:

- khoảng địa chỉ;
- quyền đọc/ghi/thực thi;
- anonymous hay file-backed;
- dùng chung (shared / 공유) hay private;
- tệp (file / 파일) offset nếu ánh xạ tệp.

Quan sát:

```bash
cat /proc/<PID>/maps
pmap -x <PID>
```

Một JVM thường có rất nhiều VMA cho vùng nhớ động (heap / 힙), dùng chung (shared / 공유) thư viện (library / 라이브러리), JIT mã (code / 코드) bộ nhớ đệm (cache / 캐시), luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택), memory-mapped JAR/lớp (class / 클래스) dữ liệu (data / 데이터) và bản địa (native / 네이티브) allocation.

## File-backed và anonymous bộ nhớ (memory / 메모리)

**File-backed bộ nhớ (memory / 메모리)** có backing store là tệp (file / 파일). Nếu trang sạch bị reclaim, kernel có thể bỏ trang khỏi RAM và đọc lại từ tệp (file / 파일) khi cần.

**Anonymous bộ nhớ (memory / 메모리)** không gắn với tệp (file / 파일) cụ thể, ví dụ vùng nhớ động (heap / 힙)/ngăn xếp (stack / 스택) thông thường. Khi cần reclaim, các trang anonymous có thể phải swap nếu muốn giải phóng RAM mà vẫn giữ nội dung.

Đây là khác biệt quan trọng khi đọc bộ nhớ (memory / 메모리) pressure.

## `MAP_SHARED` và `MAP_PRIVATE`

`MAP_SHARED` cho phép thay đổi trên ánh xạ (mapping / 매핑) có thể được nhìn thấy qua các ánh xạ (mapping / 매핑) khác và có thể ghi lại xuống tệp (file / 파일) tùy ngữ nghĩa (semantics / 의미론).

`MAP_PRIVATE` dùng sao chép khi ghi (copy-on-write / 쓰기 시 복사). Ban đầu trang có thể chia sẻ với page bộ nhớ đệm (cache / 캐시); khi tiến trình (process / 프로세스) ghi, kernel tạo bản sao riêng và thay đổi đó không ghi ngược lại tệp (file / 파일).

Ví dụ khái niệm:

```text
MAP_PRIVATE
file page ──shared read──> process
              ↓ write
          copy-on-write
              ↓
       private anonymous page
```

## Page fault khi truy cập ánh xạ (mapping / 매핑)

Gọi `mmap()` không có nghĩa toàn bộ tệp (file / 파일) được đọc vào RAM ngay. Kernel chủ yếu thiết lập siêu dữ liệu (metadata / 메타데이터) ánh xạ (mapping / 매핑).

Khi mã (code / 코드) truy cập một địa chỉ chưa resident, CPU gây **page fault**. Kernel xác định VMA tương ứng, kiểm tra quyền và tìm/đọc trang cần thiết.

Nếu trang đã có trong page bộ nhớ đệm (cache / 캐시), đây có thể là minor fault. Nếu cần I/O để lấy dữ liệu từ lưu trữ (storage / 저장소), có thể trở thành major fault.

```bash
/usr/bin/time -v command
pidstat -r -p <PID> 1
```

## `mmap()` không loại bỏ page bộ nhớ đệm (cache / 캐시)

Một hiểu lầm phổ biến là `mmap()` “đọc trực tiếp tệp (file / 파일) vào tiến trình (process / 프로세스) mà không qua bộ nhớ đệm (cache / 캐시)”. Với tệp (file / 파일) ánh xạ (mapping / 매핑) thông thường, page bộ nhớ đệm (cache / 캐시) vẫn là thành phần cốt lõi.

`read()` và `mmap()` có thể cùng nhìn cùng underlying cached tệp (file / 파일) pages.

Điều này nối trực tiếp tới [VFS, page cache và writeback](../01_filesystem/vfs_page_cache_writeback.md).

## Memory-mapped ghi (write / 쓰기) và durability

Ghi vào `MAP_SHARED` làm trang trở thành dirty. Kernel có thể ghi (write / 쓰기) back xuống tệp (file / 파일) sau đó.

Nhưng “đã ghi vào bộ nhớ (memory / 메모리)” không đồng nghĩa dữ liệu đã bền trên lưu trữ (storage / 저장소).

Ứng dụng (application / 애플리케이션) có thể cần `msync()` và/hoặc các ngữ nghĩa (semantics / 의미론) durability phù hợp, tùy use trường hợp (case / 사례).

Cơ sở dữ liệu (database / 데이터베이스) và lưu trữ (storage / 저장소) engine thường rất cẩn thận với thứ tự (ordering / 순서) giữa dữ liệu (data / 데이터), WAL và flush.

## `msync()` không phải phép màu

`msync()` yêu cầu đồng bộ các trang ánh xạ (mapping / 매핑) theo flags đã chọn, nhưng durability cuối cùng vẫn phụ thuộc filesystem, khối (block / 블록) tầng (layer / 계층), thiết bị (device / 장치) bộ nhớ đệm (cache / 캐시) và lưu trữ (storage / 저장소) backend.

Mô hình vẫn là:

```text
application dirty page
→ kernel writeback
→ filesystem
→ block layer
→ device/controller
→ durable medium
```

## Dùng chung (shared / 공유) bộ nhớ (memory / 메모리) bằng `mmap`

Hai tiến trình (process / 프로세스) có thể map cùng tệp (file / 파일) hoặc dùng chung (shared / 공유) bộ nhớ (memory / 메모리) đối tượng (object / 객체) và dùng vùng đó để trao đổi dữ liệu.

Ưu điểm là tránh bản sao (copy / 복사) nhiều lần giữa tiến trình (process / 프로세스). Nhưng synchronization trở thành trách nhiệm lớn: semaphore, futex, atomic thao tác (operation / 연산) hoặc giao thức (protocol / 프로토콜) riêng cần bảo đảm consistency.

Dùng chung (shared / 공유) bộ nhớ (memory / 메모리) nhanh không có nghĩa đơn giản.

## `tmpfs` và dùng chung (shared / 공유) bộ nhớ (memory / 메모리)

`tmpfs` là filesystem dùng bộ nhớ (memory / 메모리) và có thể swap tùy cấu hình. `/dev/shm` thường là tmpfs dùng cho POSIX dùng chung (shared / 공유) bộ nhớ (memory / 메모리).

```bash
df -h /dev/shm
mount | grep tmpfs
```

Một bộ chứa (container / 컨테이너) có thể có `/dev/shm` rất nhỏ mặc định, gây lỗi cho ứng dụng (application / 애플리케이션) dùng dùng chung (shared / 공유) bộ nhớ (memory / 메모리) lớn.

## Executable ánh xạ (mapping / 매핑) và dùng chung (shared / 공유) thư viện (library / 라이브러리)

Khi chạy ELF nhị phân (binary / 이진), mã (code / 코드) và dùng chung (shared / 공유) libraries thường được memory-map vào tiến trình (process / 프로세스).

```bash
cat /proc/<PID>/maps | grep '\.so'
```

Nhiều tiến trình (process / 프로세스) có thể chia sẻ các vật lý (physical / 물리적) pages sạch chứa mã (code / 코드) của cùng dùng chung (shared / 공유) thư viện (library / 라이브러리). Điều này tiết kiệm RAM.

## `mmap` và Java

Java sử dụng bộ nhớ (memory / 메모리) ánh xạ (mapping / 매핑) ở nhiều nơi:

- `MappedByteBuffer`;
- lớp (class / 클래스)/JAR truy cập (access / 접근) tùy thời gian chạy (runtime / 런타임);
- bản địa (native / 네이티브) thư viện (library / 라이브러리);
- mã (code / 코드) bộ nhớ đệm (cache / 캐시);
- memory-mapped files của cơ sở dữ liệu (database / 데이터베이스)/tìm kiếm (search / 검색) engine.

`MappedByteBuffer` có thể làm RSS/page bộ nhớ đệm (cache / 캐시) tăng mà vùng nhớ động (heap / 힙) dump không phản ánh đầy đủ, vì đây không phải chỉ vùng nhớ động (heap / 힙) đối tượng (object / 객체) dữ liệu (data / 데이터).

Do đó khi JVM có RSS lớn hơn `-Xmx`, bộ nhớ (memory / 메모리) ánh xạ (mapping / 매핑) là một trong nhiều nguồn cần xem.

## Direct buffer và mmap khác nhau

Java `DirectByteBuffer` thường dùng bản địa (native / 네이티브) bộ nhớ (memory / 메모리) bên ngoài Java vùng nhớ động (heap / 힙). Nó không nhất thiết là file-backed ánh xạ (mapping / 매핑).

Không nên gom mọi “off-heap” vào một loại.

Các nhóm có thể gồm:

- anonymous bản địa (native / 네이티브) allocation;
- luồng thực thi (thread / 스레드) stacks;
- direct buffers;
- JIT/mã (code / 코드) bộ nhớ đệm (cache / 캐시);
- tệp (file / 파일) mappings;
- dùng chung (shared / 공유) libraries.

## Address không gian (space / 공간) reservation khác resident bộ nhớ (memory / 메모리)

Tiến trình (process / 프로세스) có thể reserve vùng địa chỉ lớn nhưng chỉ một phần trang thực sự resident.

Đây là lý do VSZ/VIRT rất lớn không đồng nghĩa RAM vật lý tương ứng.

```bash
pmap -x <PID>
cat /proc/<PID>/smaps_rollup
```

`smaps` cung cấp chi tiết như RSS, PSS, dùng chung (shared / 공유)/private dirty/clean cho từng ánh xạ (mapping / 매핑).

## PSS và dùng chung (shared / 공유) pages

RSS tính toàn bộ resident pages thấy bởi tiến trình (process / 프로세스), kể cả trang chia sẻ. **PSS (Proportional Set Size)** chia chi phí trang dùng chung (shared / 공유) theo số tiến trình (process / 프로세스) sử dụng, nên hữu ích hơn khi muốn ước lượng footprint thực tế trong một số tình huống.

Không chỉ số (metric / 지표) nào hoàn hảo cho mọi câu hỏi; cần biết đang đo gì.

## `madvise()` và truy cập (access / 접근) mẫu (pattern / 패턴)

Ứng dụng (application / 애플리케이션) có thể đưa hint cho kernel bằng `madvise()` về truy cập (access / 접근) mẫu (pattern / 패턴), ví dụ sequential, random hoặc pages không còn cần.

Kernel có thể dùng hint để điều chỉnh read-ahead/reclaim.

Đây là tối ưu nâng cao; không nên dùng nếu chưa đo tải công việc (workload / 워크로드).

## `mlock()`

`mlock()` giữ trang không bị swap/reclaim theo ngữ nghĩa (semantics / 의미론) tương ứng. Hữu ích với một số tải công việc (workload / 워크로드) nhạy độ trễ (latency / 지연 시간) hoặc secret material nhưng có thể gây áp lực bộ nhớ (memory / 메모리) nếu dùng quá rộng.

Giới hạn:

```bash
ulimit -l
```

Cơ sở dữ liệu (database / 데이터베이스) đôi khi dùng locked bộ nhớ (memory / 메모리) hoặc huge pages theo cấu hình (configuration / 구성) cụ thể.

## Huge pages và ánh xạ (mapping / 매핑)

Transparent Huge Pages hoặc tường minh (explicit / 명시적) huge pages có thể giảm TLB pressure, nhưng có sự đánh đổi (trade-off / 트레이드오프) về allocation độ trễ (latency / 지연 시간), fragmentation và tải công việc (workload / 워크로드) hành vi (behavior / 동작).

Không nên bật/tắt theo “best practice” chung chung.

## SIGBUS khi tệp (file / 파일) ánh xạ (mapping / 매핑) thay đổi

Một dạng thất bại (failure mode / 실패 모드) quan trọng: tiến trình (process / 프로세스) map tệp (file / 파일) rồi tệp (file / 파일) bị truncate nhỏ hơn vùng ánh xạ (mapping / 매핑). Truy cập phần ánh xạ (mapping / 매핑) không còn backing hợp lệ có thể gây `SIGBUS`.

Đây là lỗi khác segmentation fault thông thường và thường xuất hiện ở hệ thống dùng mmap mạnh.

## Tệp (file / 파일) replacement và ánh xạ (mapping / 매핑) cũ

Nếu một pathname bị rename để trỏ tới inode mới, tiến trình (process / 프로세스) đã mmap inode cũ vẫn có thể tiếp tục nhìn dữ liệu cũ. Pathname và đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명) là hai khái niệm khác nhau.

Điều này giống tệp (file / 파일) descriptor mở trước khi tệp (file / 파일) bị unlink.

## Mô hình tư duy

Hãy coi `mmap()` là cách tạo **liên kết giữa vùng địa chỉ ảo và backing đối tượng (object / 객체)**:

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

Ứng dụng (application / 애플리케이션) truy cập bộ nhớ (memory / 메모리), còn kernel biến truy cập (access / 접근) đó thành page fault, bộ nhớ đệm (cache / 캐시) lookup, I/O hoặc sao chép khi ghi (copy-on-write / 쓰기 시 복사) khi cần.

## Những hiểu lầm phổ biến

**“`mmap()` đọc toàn bộ tệp (file / 파일) vào RAM.”** Không; ánh xạ (mapping / 매핑) thường lazy và trang được đưa vào khi cần.

**“mmap không dùng page bộ nhớ đệm (cache / 캐시).”** File-backed mmap thường gắn chặt với page bộ nhớ đệm (cache / 캐시).

**“Ghi vào mmap nghĩa là dữ liệu đã durable.”** Dirty page vẫn cần writeback/flush ngữ nghĩa (semantics / 의미론).

**“RSS lớn hơn vùng nhớ động (heap / 힙) nghĩa là bộ nhớ (memory / 메모리) leak.”** ánh xạ (mapping / 매핑), direct buffer, ngăn xếp (stack / 스택) và bản địa (native / 네이티브) bộ nhớ (memory / 메모리) đều có thể đóng góp.

**“`MAP_PRIVATE` sửa luôn tệp (file / 파일).”** ghi (write / 쓰기) private ánh xạ (mapping / 매핑) thường dùng COW và không ghi ngược tệp (file / 파일).

## Kết nối kiến thức

Chương này nối [bộ nhớ ảo sâu](./virtual_memory_page_fault_reclaim_allocator.md), [VFS/page cache](../01_filesystem/vfs_page_cache_writeback.md), [ELF/dynamic linking](../08_operations/elf_dynamic_linking.md) và [Java incident playbook](../09_production/java_backend_incident_playbook.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [block layer io scheduler](./block_layer_io_scheduler.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
