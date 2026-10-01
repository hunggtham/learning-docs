# Virtual bộ nhớ (memory / 메모리) và address spaces

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Virtual bộ nhớ (memory / 메모리) và address spaces**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Address không gian (space / 공간) như private coordinate hệ thống (system / 시스템)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Pages và page tables** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Nếu programs dùng vật lý (physical / 물리적) addresses trực tiếp, chúng có thể đè bộ nhớ (memory / 메모리) nhau, relocation khó và mỗi tiến trình (process / 프로세스) phải biết bố cục (layout / 레이아웃) RAM thật. Virtual bộ nhớ (memory / 메모리) thêm một translation tầng (layer / 계층): program dùng virtual addresses, MMU + page tables map chúng tới vật lý (physical / 물리적) frames hoặc trạng thái chưa resident.

## Address không gian (space / 공간) như private coordinate hệ thống (system / 시스템)

Mỗi tiến trình (process / 프로세스) thường thấy một virtual address không gian (space / 공간) riêng. Cùng virtual address `0x...` trong hai processes có thể map tới vật lý (physical / 물리적) pages khác. Điều này tạo isolation và cho loader đặt mã (code / 코드)/vùng nhớ động (heap / 힙)/ngăn xếp (stack / 스택) theo consistent conventions.

Virtual bộ nhớ (memory / 메모리) không có nghĩa OS “tạo RAM vô hạn”. Nó là ánh xạ (mapping / 매핑) lớp trừu tượng (abstraction / 추상화); khi working set vượt vật lý (physical / 물리적) bộ nhớ (memory / 메모리), paging/lưu trữ (storage / 저장소) pressure làm hiệu năng (performance / 성능) giảm mạnh.

> **Chuyển mạch:** Trong **Virtual bộ nhớ (memory / 메모리) và address spaces**, **Pages và page tables** tiếp nhận điểm tựa từ **Address không gian (space / 공간) như private coordinate hệ thống (system / 시스템)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TLB** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pages và page tables

Address không gian (space / 공간) chia thành virtual pages; vật lý (physical / 물리적) RAM chia frames. Virtual address tách page number + offset. Bảng trang (page table / 페이지 테이블) entry chứa vật lý (physical / 물리적) frame và permission/status bits.

Page kích thước (size / 크기) thường vài KiB nhưng huge pages lớn hơn. Smaller pages giảm nội bộ (internal / 내부) fragmentation; larger pages giảm page-table/TLB overhead.

> **Chuyển mạch:** Ở chặng này của **Virtual bộ nhớ (memory / 메모리) và address spaces**, **TLB** tiếp nhận điểm tựa từ **Pages và page tables** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Page fault và demand paging** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TLB

Bảng trang (page table / 페이지 테이블) walk qua multiple levels tốn bộ nhớ (memory / 메모리) accesses. TLB bộ nhớ đệm (cache / 캐시) translations gần đây. TLB miss không phải page fault: page có thể resident nhưng translation chưa bộ nhớ đệm (cache / 캐시). Page fault xảy ra khi hiện tại (current / 현재) ánh xạ (mapping / 매핑) cần OS intervention.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Virtual bộ nhớ (memory / 메모리) và address spaces**, **Page fault và demand paging** tiếp nhận điểm tựa từ **TLB** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sao chép khi ghi (copy-on-write / 쓰기 시 복사)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Page fault và demand paging

Khi tiến trình (process / 프로세스) truy cập (access / 접근) virtual page chưa mapped/resident, CPU traps kernel. OS có thể allocate zero page, tải (load / 로드) file-backed page, sao chép khi ghi (copy-on-write / 쓰기 시 복사) hoặc reject invalid truy cập (access / 접근).

Major page fault có thể cần lưu trữ (storage / 저장소) I/O; minor fault chỉ ánh xạ (mapping / 매핑)/bộ nhớ (memory / 메모리) công việc (work / 작업). Vì vậy “page fault count” cần ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Trong **Virtual bộ nhớ (memory / 메모리) và address spaces**, **Sao chép khi ghi (copy-on-write / 쓰기 시 복사)** tiếp nhận điểm tựa từ **Page fault và demand paging** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Memory-mapped files** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sao chép khi ghi (copy-on-write / 쓰기 시 복사)

Fork/snapshot có thể share vật lý (physical / 물리적) pages read-only giữa processes. Khi một bên ghi (write / 쓰기), fault trigger bản sao (copy / 복사) riêng page. sao chép khi ghi (copy-on-write / 쓰기 시 복사) tránh eager bản sao (copy / 복사) toàn bộ nhớ (memory / 메모리) nếu phần lớn pages không đổi.

COW xuất hiện cả filesystem snapshots và dữ liệu (data / 데이터) structures: same mô hình tư duy (mental model / 사고 모델) “share until mutation”.

> **Chuyển mạch:** Ở chặng này của **Virtual bộ nhớ (memory / 메모리) và address spaces**, **Memory-mapped files** tiếp nhận điểm tựa từ **Sao chép khi ghi (copy-on-write / 쓰기 시 복사)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vùng nhớ vùng nhớ động (heap / 힙) và ngăn xếp (stack / 스택) growth** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Memory-mapped files

`mmap` map tệp (file / 파일) pages vào address không gian (space / 공간). Reads/writes trở thành bộ nhớ (memory / 메모리) accesses và OS page bộ nhớ đệm (cache / 캐시) quản lý loading/dirty pages. Nó có thể giảm copying và đơn giản random truy cập (access / 접근), nhưng durability, truncation và lỗi (error / 오류) ngữ nghĩa (semantics / 의미론) cần hiểu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Virtual bộ nhớ (memory / 메모리) và address spaces**, **Vùng nhớ vùng nhớ động (heap / 힙) và ngăn xếp (stack / 스택) growth** tiếp nhận điểm tựa từ **Memory-mapped files** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Swapping và thrashing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vùng nhớ vùng nhớ động (heap / 힙) và ngăn xếp (stack / 스택) growth

Ngôn ngữ (language / 언어) thời gian chạy (runtime / 런타임) vùng nhớ động (heap / 힙) allocator quản lý virtual regions đã được OS cấp. ngăn xếp (stack / 스택) thường có mapped region/guard page và grow chính sách (policy / 정책). “Out of bộ nhớ (memory / 메모리)” có thể đến từ address-space limits, lần ghi nhận (commit / 커밋), cgroup, vật lý (physical / 물리적) bộ nhớ (memory / 메모리) hoặc thời gian chạy (runtime / 런타임) vùng nhớ động (heap / 힙) chính sách (policy / 정책).

> **Chuyển mạch:** Trong **Virtual bộ nhớ (memory / 메모리) và address spaces**, **Swapping và thrashing** tiếp nhận điểm tựa từ **Vùng nhớ vùng nhớ động (heap / 힙) và ngăn xếp (stack / 스택) growth** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Protection bits và NX** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Swapping và thrashing

Nếu active working set lớn hơn RAM, OS liên tục evict/tải (load / 로드) pages. Thrashing xảy ra khi thời gian (time / 시간) dành cho paging nhiều hơn useful computation. Locality chính là yếu tố cứu hierarchy.

> **Chuyển mạch:** Ở chặng này của **Virtual bộ nhớ (memory / 메모리) và address spaces**, **Protection bits và NX** tiếp nhận điểm tựa từ **Swapping và thrashing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Protection bits và NX

Page permissions read/ghi (write / 쓰기)/execute giúp enforce isolation. W^X chính sách (policy / 정책) tránh page vừa writable vừa executable; NX bit giúp chặn một lớp (class / 클래스) mã (code / 코드) injection. ASLR randomize mappings để tăng khó exploitation, dù không phải bảo mật (security / 보안) guarantee độc lập.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Virtual bộ nhớ (memory / 메모리) và address spaces**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Protection bits và NX** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Virtual address là **tên lô-gic (logic / 논리)**, vật lý (physical / 물리적) frame là **vị trí hiện tại**. Bảng trang (page table / 페이지 테이블) là ánh xạ (mapping / 매핑) + permissions; TLB bộ nhớ đệm (cache / 캐시) ánh xạ (mapping / 매핑); page fault là lúc ánh xạ (mapping / 매핑) cần kernel xử lý.

> **Chuyển mạch:** Trong **Virtual bộ nhớ (memory / 메모리) và address spaces**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Virtual bộ nhớ (memory / 메모리) = swap.”** Swap chỉ là một cơ chế (mechanism / 메커니즘) có thể hỗ trợ. VM chủ yếu là address translation, isolation, ánh xạ (mapping / 매핑) và paging abstractions.

**“Page fault luôn do bug.”** Demand paging/COW tạo faults bình thường; invalid/protection fault mới có thể thành crash.

**“Malloc 1 GB nghĩa ngay lập tức dùng 1 GB vật lý (physical / 물리적) RAM.”** Overcommit/lazy allocation/hành vi thời gian chạy (runtime behavior / 런타임 동작) có thể khác; actual committed/resident pages thay đổi khi touched.

> **Chuyển mạch:** Ở chặng này của **Virtual bộ nhớ (memory / 메모리) và address spaces**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

MMU/TLB từ [memory hierarchy](../02_computer_architecture/02_memory_hierarchy_and_cache.md); tiến trình (process / 프로세스) lớp trừu tượng (abstraction / 추상화) ở [kernel](./00_kernel_syscalls_and_os_abstractions.md); ngôn ngữ (language / 언어) vùng nhớ động (heap / 힙)/GC ở [types and memory management](../04_programming_languages/01_types_values_references_and_memory.md); bảo mật (security / 보안) permissions ở [vulnerabilities](../07_security_reliability/03_software_vulnerabilities.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
