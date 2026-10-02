# Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Không gian địa chỉ ảo không phải RAM được cấp phát sẵn** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **VMA: vùng bộ nhớ ảo** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối virtual memory với page fault, reclaim và allocator, để phân biệt thiếu bộ nhớ khả dụng với lỗi cấp phát của ứng dụng.

Chương [Bộ nhớ, bộ nhớ ảo, page cache và OOM](./memory_virtual_memory.md) cung cấp mô hình tổng quan. Chương này đi sâu vào các cơ chế bên dưới để giải thích vì sao một tiến trình có thể có `VSZ` rất lớn nhưng chưa dùng nhiều RAM, vì sao truy cập một địa chỉ hợp lệ vẫn gây page fault, vì sao kernel phải reclaim bộ nhớ (memory / 메모리), và tại sao hệ thống có thể bắt đầu chậm rất lâu trước khi OOM killer xuất hiện.

## Không gian địa chỉ ảo không phải RAM được cấp phát sẵn

Khi một tiến trình có một vùng địa chỉ ảo, điều đó không có nghĩa mọi byte tương ứng đã có khung trang vật lý trong RAM.

Kernel có thể chỉ ghi nhận một **vùng ánh xạ bộ nhớ (memory mapping)**. Khung trang vật lý được cấp khi tiến trình thực sự truy cập, tùy loại ánh xạ (mapping / 매핑).

Ví dụ conceptual:

```text
virtual address space
0x1000 ────────────────┐
                      │ mapped region
0x9000 ────────────────┘

physical RAM:
chưa chắc có frame cho mọi virtual page
```

Cơ chế này cho phép tiến trình (process / 프로세스) đặt trước không gian địa chỉ lớn mà không lập tức tiêu thụ lượng RAM tương ứng.

> **Chuyển mạch:** Trong **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **VMA: vùng bộ nhớ ảo** tiếp nhận điểm tựa từ **Không gian địa chỉ ảo không phải RAM được cấp phát sẵn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảng trang (page table / 페이지 테이블) và MMU** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## VMA: vùng bộ nhớ ảo

Kernel quản lý các vùng địa chỉ có cùng thuộc tính dưới dạng **VMA (Virtual memory Area)**.

Có thể quan sát qua:

```bash
cat /proc/<PID>/maps
```

hoặc chi tiết hơn:

```bash
cat /proc/<PID>/smaps
```

Các vùng có thể đại diện:

- executable mã (code / 코드);
- dùng chung (shared / 공유) libraries;
- vùng nhớ động (heap / 힙);
- ngăn xếp (stack / 스택);
- memory-mapped files;
- anonymous mappings;
- special mappings của kernel/thời gian chạy (runtime / 런타임).

Một JVM thường có nhiều ánh xạ (mapping / 매핑) và vùng reserve lớn, vì vậy nhìn `VIRT` riêng lẻ rất dễ gây hiểu nhầm.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Bảng trang (page table / 페이지 테이블) và MMU** tiếp nhận điểm tựa từ **VMA: vùng bộ nhớ ảo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TLB** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảng trang (page table / 페이지 테이블) và MMU

CPU dùng **MMU (memory Management Unit)** để dịch địa chỉ ảo thành địa chỉ vật lý dựa trên bảng trang (page table / 페이지 테이블) do kernel quản lý.

Có thể hình dung:

```text
virtual address
   ↓
page-table walk
   ↓
physical frame
```

Nếu ánh xạ (mapping / 매핑) không có hoặc permission không phù hợp, CPU tạo exception để kernel xử lý.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **TLB** tiếp nhận điểm tựa từ **Bảng trang (page table / 페이지 테이블) và MMU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Page fault không nhất thiết là lỗi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TLB

Page-table walk có thể cần nhiều lần truy cập bộ nhớ (memory / 메모리). CPU vì vậy dùng **TLB (Translation Lookaside Buffer)** để bộ nhớ đệm (cache / 캐시) kết quả dịch địa chỉ.

Nếu working set lớn hơn khả năng TLB, **TLB miss** tăng và CPU phải thực hiện nhiều page-table walk hơn.

Huge pages có thể giúp giảm số entry cần thiết trong TLB cho tải công việc (workload / 워크로드) lớn, nhưng đổi lại có sự đánh đổi (trade-off / 트레이드오프) về allocation, fragmentation và flexibility.

> **Chuyển mạch:** Trong **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Page fault không nhất thiết là lỗi** tiếp nhận điểm tựa từ **TLB** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Demand paging** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Page fault không nhất thiết là lỗi

Tên **page fault** dễ làm người mới nghĩ hệ thống đang gặp lỗi. Thực ra page fault là một cơ chế bình thường để kernel hoàn thiện ánh xạ (mapping / 매핑) khi tiến trình (process / 프로세스) truy cập một trang chưa sẵn sàng.

Có hai nhóm quan trọng:

- **minor page fault** — không cần đọc dữ liệu từ lưu trữ (storage / 저장소) chậm;
- **major page fault** — cần lấy dữ liệu từ backing lưu trữ (storage / 저장소), thường đắt hơn đáng kể.

Quan sát:

```bash
pidstat -r 1
```

hoặc:

```bash
ps -o pid,min_flt,maj_flt,cmd -p <PID>
```

Tên trường dữ liệu (field / 필드) cụ thể có thể phụ thuộc công cụ.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Demand paging** tiếp nhận điểm tựa từ **Page fault không nhất thiết là lỗi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sao chép khi ghi (copy-on-write / 쓰기 시 복사) sau fork()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Demand paging

Linux thường dùng **nạp trang theo nhu cầu (demand paging)**.

Ví dụ khi executable được map, kernel không nhất thiết đọc toàn bộ nhị phân (binary / 이진) vào RAM. Chỉ khi đường đi mã (code path / 코드 경로) cần một trang chưa resident, page fault mới kéo dữ liệu vào.

Điều này giúp startup và bộ nhớ (memory / 메모리) efficiency tốt hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Sao chép khi ghi (copy-on-write / 쓰기 시 복사) sau fork()** tiếp nhận điểm tựa từ **Demand paging** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Anonymous bộ nhớ (memory / 메모리) và file-backed bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sao chép khi ghi (copy-on-write / 쓰기 시 복사) sau `fork()`

Sau `fork()`, kernel không cần bản sao (copy / 복사) toàn bộ bộ nhớ (memory / 메모리) của parent ngay lập tức. Parent và child có thể tạm chia sẻ các page vật lý ở chế độ chỉ đọc.

Nếu một bên ghi vào page, page fault xảy ra và kernel tạo bản bản sao (copy / 복사) riêng. Đây là **sao chép khi ghi (copy-on-write / 쓰기 시 복사) (COW)**.

Mô hình tư duy (mental model / 사고 모델):

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

> **Chuyển mạch:** Trong **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Anonymous bộ nhớ (memory / 메모리) và file-backed bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Sao chép khi ghi (copy-on-write / 쓰기 시 복사) sau fork()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **malloc() không đồng nghĩa kernel cấp page ngay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Anonymous bộ nhớ (memory / 메모리) và file-backed bộ nhớ (memory / 메모리)

**Anonymous bộ nhớ (memory / 메모리)** không gắn trực tiếp với tệp (file / 파일) cụ thể, ví dụ vùng nhớ động (heap / 힙) hoặc nhiều vùng `malloc`.

**File-backed bộ nhớ (memory / 메모리)** gắn với tệp (file / 파일) hoặc dùng chung (shared / 공유) đối tượng (object / 객체).

Khi reclaim:

- clean file-backed page có thể bị bỏ khỏi RAM rồi đọc lại từ tệp (file / 파일) sau;
- dirty file-backed page cần writeback trước;
- anonymous page muốn reclaim có thể cần swap nếu còn cần giữ nội dung.

Đây là lý do page bộ nhớ đệm (cache / 캐시) thường dễ reclaim hơn anonymous working set.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **malloc() không đồng nghĩa kernel cấp page ngay** tiếp nhận điểm tựa từ **Anonymous bộ nhớ (memory / 메모리) và file-backed bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Allocator fragmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `malloc()` không đồng nghĩa kernel cấp page ngay

Trong bản địa (native / 네이티브) ứng dụng (application / 애플리케이션), `malloc()` thường được C allocator xử lý ở người dùng (user / 사용자) không gian (space / 공간) trước. Allocator có thể lấy vùng lớn từ kernel rồi chia nhỏ cho nhiều allocation.

Các cơ chế kernel thường liên quan gồm:

- `brk()` / vùng nhớ động (heap / 힙) growth;
- `mmap()` cho ánh xạ (mapping / 매핑) lớn hoặc riêng;
- page fault để cấp vật lý (physical / 물리적) page khi chạm vào vùng nhớ.

Vì vậy ứng dụng (application / 애플리케이션) allocation, virtual ánh xạ (mapping / 매핑) và vật lý (physical / 물리적) residency là ba tầng khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Allocator fragmentation** tiếp nhận điểm tựa từ **malloc() không đồng nghĩa kernel cấp page ngay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Buddy allocator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Allocator fragmentation

Ngay cả khi tổng bộ nhớ (memory / 메모리) còn đủ, allocator có thể có fragmentation khiến việc sử dụng không hiệu quả.

Hai khái niệm:

- **nội bộ (internal / 내부) fragmentation** — khối (block / 블록) được cấp lớn hơn nhu cầu;
- **bên ngoài (external / 외부) fragmentation** — free không gian (space / 공간) bị chia nhỏ thành nhiều vùng khó dùng cho allocation lớn.

Trong kernel còn có vấn đề fragmentation theo thứ tự (order / 순서) của buddy allocator.

> **Chuyển mạch:** Trong **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Buddy allocator** tiếp nhận điểm tựa từ **Allocator fragmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SLAB/SLUB allocator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Buddy allocator

Kernel quản lý vật lý (physical / 물리적) pages qua các allocator, trong đó **buddy allocator** là cơ chế nền tảng để cấp các khối (block / 블록) page có kích thước theo bậc lũy thừa hai.

Khi một khối (block / 블록) lớn bị chia thành hai “buddy”, các khối (block / 블록) có thể được hợp nhất lại khi cùng free.

Mô hình này hỗ trợ cấp phát nhanh nhưng contiguous allocation lớn có thể khó khi RAM bị phân mảnh.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Buddy allocator** cho ta quy tắc; **SLAB/SLUB allocator** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **/proc/meminfo sâu hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SLAB/SLUB allocator

Kernel cần cấp rất nhiều đối tượng (object / 객체) nhỏ như inode structures, dentries, tác vụ (task / 작업) structures, mạng (network / 네트워크) objects.

Dùng page allocator trực tiếp cho từng đối tượng (object / 객체) sẽ lãng phí. Linux vì vậy dùng đối tượng (object / 객체) allocator như **SLUB** để bộ nhớ đệm (cache / 캐시) các đối tượng (object / 객체) cùng loại.

Có thể quan sát tổng quan:

```bash
slabtop
```

Nếu kernel bộ nhớ (memory / 메모리) tăng mạnh, không phải mọi bộ nhớ (memory / 메모리) pressure đều nằm ở user-process RSS.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **SLAB/SLUB allocator** cho ta quy tắc; **/proc/meminfo sâu hơn** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Reclaim: kernel lấy lại RAM như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `/proc/meminfo` sâu hơn

Một số trường dữ liệu (field / 필드) hữu ích:

```bash
grep -E 'MemAvailable|Cached|Buffers|Slab|SReclaimable|SUnreclaim|AnonPages|Mapped|Dirty|Writeback|Swap' /proc/meminfo
```

Ý nghĩa quan trọng:

- `AnonPages` — anonymous pages;
- `Cached` — file-backed bộ nhớ đệm (cache / 캐시) theo cách accounting của kernel;
- `Slab` — bộ nhớ (memory / 메모리) cho kernel đối tượng (object / 객체) caches;
- `SReclaimable` — một phần slab có thể reclaim;
- `SUnreclaim` — slab khó hoặc không reclaim;
- `Dirty` — file-backed pages chưa ghi xuống;
- `Writeback` — pages đang writeback.

Không nên cộng trừ các trường dữ liệu (field / 필드) một cách máy móc vì accounting có overlap và ngữ nghĩa (semantics / 의미론) kernel-version dependent.

> **Chuyển mạch:** Trong **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Reclaim: kernel lấy lại RAM như thế nào?** tiếp nhận điểm tựa từ **/proc/meminfo sâu hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LRU là một mô hình gần đúng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reclaim: kernel lấy lại RAM như thế nào?

Khi bộ nhớ (memory / 메모리) pressure tăng, kernel phải tìm pages có thể giải phóng.

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

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **LRU là một mô hình gần đúng** tiếp nhận điểm tựa từ **Reclaim: kernel lấy lại RAM như thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Direct reclaim** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LRU là một mô hình gần đúng

Kernel dùng các danh sách và thuật toán để ước lượng pages hoạt động hay không hoạt động. Tài liệu thường nói “LRU”, nhưng hiện thực (implementation / 구현) thực tế tinh vi hơn một LRU textbook thuần túy.

Kernel hiện đại có thể dùng **multi-generational LRU (MGLRU)** tùy phiên bản (version / 버전)/cấu hình (configuration / 구성) để cải thiện reclaim hành vi (behavior / 동작).

Điểm cần nhớ là kernel phải trả lời câu hỏi: “page nào có xác suất ít được dùng lại nhất?”

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Direct reclaim** tiếp nhận điểm tựa từ **LRU là một mô hình gần đúng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kswapd** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Direct reclaim

Nếu background reclaim không theo kịp, luồng thực thi (thread / 스레드) đang yêu cầu bộ nhớ (memory / 메모리) có thể tự phải tham gia reclaim. Đây gọi là **direct reclaim**.

Khi đó ứng dụng (application / 애플리케이션) độ trễ (latency / 지연 시간) có thể tăng dù OOM chưa xảy ra.

Một hệ thống có bộ nhớ (memory / 메모리) pressure nặng có thể biểu hiện:

```text
request latency tăng
CPU không quá cao
I/O tăng
kswapd hoạt động
process stalls
sau đó mới OOM nếu không phục hồi
```

Vì vậy OOM là điểm cuối; hiệu năng (performance / 성능) degradation có thể xuất hiện sớm hơn nhiều.

> **Chuyển mạch:** Trong **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **kswapd** tiếp nhận điểm tựa từ **Direct reclaim** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) watermark** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `kswapd`

`kswapd` là kernel luồng thực thi (thread / 스레드) thực hiện background reclaim khi bộ nhớ (memory / 메모리) thấp hơn các watermark nhất định.

Nếu `kswapd` dùng CPU đáng kể và `vmstat` cho thấy swap/reclaim activity, bộ nhớ (memory / 메모리) pressure là giả thuyết mạnh.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Bộ nhớ (memory / 메모리) watermark** tiếp nhận điểm tựa từ **kswapd** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PSI: Pressure Stall thông tin (information / 정보)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) watermark

Kernel giữ các watermark cho vùng bộ nhớ (memory / 메모리) để biết khi nào bắt đầu background reclaim và khi nào allocation phải chịu áp lực mạnh hơn.

Các tham số như:

```bash
sysctl vm.min_free_kbytes
```

ảnh hưởng reserve và reclaim hành vi (behavior / 동작).

Không nên tuning nếu chưa hiểu tải công việc (workload / 워크로드) và kernel bộ nhớ (memory / 메모리) mô hình (model / 모델).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **PSI: Pressure Stall thông tin (information / 정보)** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) watermark** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Swap không chỉ là “RAM chậm”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PSI: Pressure Stall thông tin (information / 정보)

Linux có **PSI (Pressure Stall information)** để đo thời gian tasks bị stall vì thiếu CPU, bộ nhớ (memory / 메모리) hoặc I/O resources.

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

PSI rất hữu ích vì nó đo **tác động pressure lên tải công việc (workload / 워크로드)**, không chỉ lượng tài nguyên đã sử dụng.

Bộ nhớ (memory / 메모리) usage 90% có thể bình thường nếu không stall; bộ nhớ (memory / 메모리) pressure thấp hơn nhưng direct reclaim liên tục lại có thể gây độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Trong **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Swap không chỉ là “RAM chậm”** tiếp nhận điểm tựa từ **PSI: Pressure Stall thông tin (information / 정보)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thrashing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Swap không chỉ là “RAM chậm”

Swap cho phép kernel di chuyển anonymous pages ít dùng ra lưu trữ (storage / 저장소) để giữ RAM cho active working set và page bộ nhớ đệm (cache / 캐시).

Không có swap đôi khi làm OOM xảy ra sớm hơn trong một số tải công việc (workload / 워크로드); swap quá chậm hoặc thrashing lại có thể làm hệ thống gần như không phản hồi.

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

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Thrashing** tiếp nhận điểm tựa từ **Swap không chỉ là “RAM chậm”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **OOM killer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thrashing

**Thrashing** xảy ra khi hệ thống dành phần lớn thời gian di chuyển pages vào/ra bộ nhớ (memory / 메모리) thay vì chạy tải công việc (workload / 워크로드) hữu ích.

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

Độ trễ (latency / 지연 시간) tăng cực mạnh trong khi thông lượng (throughput / 처리량) sụt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **OOM killer** tiếp nhận điểm tựa từ **Thrashing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cgroup OOM khác toàn cục (global / 전역) OOM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## OOM killer

Khi kernel không thể đáp ứng allocation sau reclaim và các cơ chế khác, OOM killer có thể chọn tiến trình (process / 프로세스) để terminate.

Kiểm tra:

```bash
journalctl -k | grep -i -E 'oom|out of memory|killed process'
```

OOM killer chọn nạn nhân dựa trên heuristic và `oom_score`.

```bash
cat /proc/<PID>/oom_score
cat /proc/<PID>/oom_score_adj
```

`oom_score_adj` cho phép ảnh hưởng khả năng tiến trình (process / 프로세스) bị chọn. Không nên đặt mọi trọng yếu (critical / 중요) tiến trình (process / 프로세스) thành “không bao giờ kill”, vì kernel vẫn cần cách phục hồi khi thật sự cạn bộ nhớ (memory / 메모리).

> **Chuyển mạch:** Trong **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Cgroup OOM khác toàn cục (global / 전역) OOM** tiếp nhận điểm tựa từ **OOM killer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **memory.high và throttling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cgroup OOM khác toàn cục (global / 전역) OOM

Trong bộ chứa (container / 컨테이너)/cgroup, tải công việc (workload / 워크로드) có thể chạm `memory.max` dù host còn RAM.

Cgroup v2 cung cấp các tệp (file / 파일) như:

```text
memory.current
memory.max
memory.events
memory.stat
```

Tùy môi trường, có thể xem trong `/sys/fs/cgroup`.

Nếu host còn 30 GB RAM nhưng bộ chứa (container / 컨테이너) bị kill, cần kiểm tra cgroup trước khi kết luận kernel toàn cục (global / 전역) OOM.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **memory.high và throttling** tiếp nhận điểm tựa từ **Cgroup OOM khác toàn cục (global / 전역) OOM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **JVM và bản địa (native / 네이티브) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `memory.high` và throttling

Cgroup v2 có `memory.high` như một ngưỡng pressure/throttling mềm hơn `memory.max`.

Khi vượt `memory.high`, tải công việc (workload / 워크로드) có thể bị reclaim/throttle thay vì bị kill ngay.

Điều này tạo một tầng hiệu năng (performance / 성능) degradation trước hard limit.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **JVM và bản địa (native / 네이티브) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **memory.high và throttling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) và số lượng luồng thực thi (thread / 스레드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## JVM và bản địa (native / 네이티브) bộ nhớ (memory / 메모리)

Java vùng nhớ động (heap / 힙) chỉ là một phần của tiến trình (process / 프로세스) bộ nhớ (memory / 메모리):

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

nếu JVM được bật bản địa (native / 네이티브) bộ nhớ (memory / 메모리) Tracking phù hợp.

Khi RSS cao hơn `Xmx` nhiều, đây không nhất thiết là leak; cần phân rã các vùng bản địa (native / 네이티브).

> **Chuyển mạch:** Trong **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) và số lượng luồng thực thi (thread / 스레드)** tiếp nhận điểm tựa từ **JVM và bản địa (native / 네이티브) bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Direct buffer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) và số lượng luồng thực thi (thread / 스레드)

Mỗi luồng thực thi (thread / 스레드) có ngăn xếp (stack / 스택) reservation. Nếu tạo hàng nghìn threads, bản địa (native / 네이티브) bộ nhớ (memory / 메모리) cho stacks có thể rất lớn.

Ví dụ conceptual:

```text
2000 threads × 1 MiB stack reservation
≈ 2 GiB virtual space
```

Vật lý (physical / 물리적) residency thực tế có thể thấp hơn reservation, nhưng luồng thực thi (thread / 스레드) count vẫn ảnh hưởng bộ nhớ (memory / 메모리) và scheduler.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Direct buffer** tiếp nhận điểm tựa từ **Luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) và số lượng luồng thực thi (thread / 스레드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NUMA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Direct buffer

Java NIO có thể dùng direct buffer ngoài vùng nhớ động (heap / 힙).

Nếu ứng dụng (application / 애플리케이션) dùng Netty hoặc NIO mạnh, vùng nhớ động (heap / 힙) có thể ổn nhưng RSS vẫn tăng do off-heap/direct bộ nhớ (memory / 메모리).

Cần kết hợp JVM metrics với `/proc/<PID>/smaps` hoặc bản địa (native / 네이티브) bộ nhớ (memory / 메모리) Tracking.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **NUMA** tiếp nhận điểm tựa từ **Direct buffer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Transparent Huge Pages** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## NUMA

Trên multi-socket máy chủ (server / 서버), CPU truy cập cục bộ (local / 로컬) NUMA bộ nhớ (memory / 메모리) nhanh hơn remote bộ nhớ (memory / 메모리).

Quan sát:

```bash
numactl --hardware
numastat
```

NUMA imbalance có thể làm độ trễ (latency / 지연 시간) tăng dù tổng RAM còn nhiều.

Không nên pin bộ nhớ (memory / 메모리)/CPU tùy tiện; first-touch allocation và scheduler placement có thể ảnh hưởng lớn.

> **Chuyển mạch:** Trong **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Transparent Huge Pages** tiếp nhận điểm tựa từ **NUMA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) compaction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Transparent Huge Pages

Linux có thể dùng **Transparent Huge Pages (THP)** để tự động gom pages lớn hơn.

Kiểm tra:

```bash
cat /sys/kernel/mm/transparent_hugepage/enabled
```

THP có thể cải thiện TLB efficiency nhưng một số cơ sở dữ liệu (database / 데이터베이스) tải công việc (workload / 워크로드) không thích độ trễ (latency / 지연 시간) từ compaction hoặc allocation. Vì vậy khuyến nghị phụ thuộc tải công việc (workload / 워크로드).

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Bộ nhớ (memory / 메모리) compaction** tiếp nhận điểm tựa từ **Transparent Huge Pages** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): JVM không OOM vùng nhớ động (heap / 힙) nhưng bộ chứa (container / 컨테이너) vẫn bị kill** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) compaction

Để tạo contiguous khối (block / 블록) lớn hoặc huge page, kernel có thể phải **bộ nhớ (memory / 메모리) compaction** — di chuyển pages để tạo vùng liên tục.

Compaction có thể tạo độ trễ (latency / 지연 시간) spike trong một số trường hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Bộ nhớ (memory / 메모리) compaction** cho ta quy tắc; **Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): JVM không OOM vùng nhớ động (heap / 힙) nhưng bộ chứa (container / 컨테이너) vẫn bị kill** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): host còn RAM nhưng yêu cầu (request / 요청) độ trễ (latency / 지연 시간) tăng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): JVM không OOM vùng nhớ động (heap / 힙) nhưng bộ chứa (container / 컨테이너) vẫn bị kill

Giả sử:

```text
container memory.max = 4 GiB
-Xmx = 3 GiB
```

Ngoài vùng nhớ động (heap / 힙) còn:

```text
metaspace 300 MiB
thread stacks 400 MiB
direct buffers 500 MiB
native/runtime 300 MiB
```

Tổng tiến trình (process / 프로세스)/cgroup usage có thể vượt 4 GiB dù vùng nhớ động (heap / 힙) chưa đầy.

Giải pháp không phải chỉ tăng `Xmx`; ngược lại, đôi khi cần giảm vùng nhớ động (heap / 힙) để dành headroom cho bản địa (native / 네이티브) bộ nhớ (memory / 메모리).

> **Chuyển mạch:** Trong **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): JVM không OOM vùng nhớ động (heap / 힙) nhưng bộ chứa (container / 컨테이너) vẫn bị kill** cho ta quy tắc; **Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): host còn RAM nhưng yêu cầu (request / 요청) độ trễ (latency / 지연 시간) tăng** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): host còn RAM nhưng yêu cầu (request / 요청) độ trễ (latency / 지연 시간) tăng

Có thể bộ nhớ (memory / 메모리) pressure cục bộ trong cgroup hoặc reclaim activity làm tải công việc (workload / 워크로드) stall.

Kiểm tra:

```bash
cat /proc/pressure/memory
vmstat 1
cat /sys/fs/cgroup/.../memory.events
```

Nếu `memory.high` events tăng hoặc PSI bộ nhớ (memory / 메모리) cao, đây là bằng chứng (evidence / 증거) tốt hơn chỉ nhìn `free -h`.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): host còn RAM nhưng yêu cầu (request / 요청) độ trễ (latency / 지연 시간) tăng** cho ta quy tắc; **Mô hình tư duy** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Một tiến trình (process / 프로세스) có thể có ánh xạ (mapping / 매핑) nhưng chưa resident. Một page có thể resident rồi bị reclaim. Một cgroup có thể hết quota dù host chưa hết RAM.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“Page fault luôn là lỗi.”** Minor fault là một phần bình thường của demand paging.

**“`malloc(1GB)` nghĩa là lập tức dùng 1 GB RAM.”** Virtual allocation và vật lý (physical / 물리적) residency có thể xảy ra ở thời điểm khác.

**“OOM là dấu hiệu đầu tiên của bộ nhớ (memory / 메모리) pressure.”** Reclaim, PSI stall và độ trễ (latency / 지연 시간) tăng thường xuất hiện trước.

**“Không có swap luôn tốt hơn.”** Tùy tải công việc (workload / 워크로드); không swap có thể làm OOM sớm hơn, còn swap quá mạnh có thể gây thrashing.

**“`Xmx=4G` thì bộ chứa (container / 컨테이너) 4G là đủ.”** JVM còn bản địa (native / 네이티브)/off-heap bộ nhớ (memory / 메모리).

**“RSS cộng lại bằng đúng RAM used.”** dùng chung (shared / 공유) pages và kernel accounting làm phép cộng đơn giản sai.

> **Chuyển mạch:** Trong **Bộ nhớ ảo sâu hơn: page fault, allocator, reclaim và OOM**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Đọc [VFS, page cache và writeback](../01_filesystem/vfs_page_cache_writeback.md) để hiểu file-backed bộ nhớ (memory / 메모리), [Namespace và cgroup](../09_production/namespaces_cgroups_seccomp.md) để hiểu bộ nhớ (memory / 메모리) controller, và [Capacity planning](../09_production/capacity_planning_server_sizing.md) để chuyển bộ nhớ (memory / 메모리) mô hình (model / 모델) thành sizing thực tế.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
