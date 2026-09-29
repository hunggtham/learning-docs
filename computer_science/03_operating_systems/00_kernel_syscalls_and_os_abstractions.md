# Kernel, lời gọi hệ thống (system call / 시스템 호출) và OS abstractions

> **Mạch đọc:** Đặt **Kernel, lời gọi hệ thống (system call / 시스템 호출) và OS abstractions** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Kernel là phần có quyền đặc biệt** sang **lời gọi hệ thống (system call / 시스템 호출)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Operating hệ thống (system / 시스템) — OS (운영체제 / hệ điều hành) giải quyết một mâu thuẫn cơ bản: nhiều programs muốn dùng cùng CPU, bộ nhớ (memory / 메모리), lưu trữ (storage / 저장소) và devices, nhưng nếu mỗi program điều khiển hardware trực tiếp thì isolation, portability và sharing gần như không thể quản lý. OS đặt một privileged kernel giữa applications và hardware, rồi cung cấp abstractions ổn định như tiến trình (process / 프로세스), virtual bộ nhớ (memory / 메모리), tệp (file / 파일) và socket.

## Kernel là phần có quyền đặc biệt

Kernel (커널) chạy ở CPU privilege mức (level / 수준) cao, quản lý page tables, interrupts, thiết bị (device / 장치) drivers, scheduling và protected resources. người dùng (user / 사용자) applications chạy ở chế độ người dùng (user mode / 사용자 모드) với quyền hạn chế.

Ranh giới (boundary / 경계) này được hardware enforce. Nếu một tiến trình (process / 프로세스) bình thường có thể sửa bảng trang (page table / 페이지 테이블) hoặc đọc arbitrary vật lý (physical / 물리적) bộ nhớ (memory / 메모리), tiến trình (process / 프로세스) isolation sẽ không tồn tại.

Kernel thiết kế (design / 설계) có nhiều dạng. Monolithic kernels như Linux đặt nhiều subsystems/drivers trong kernel không gian (space / 공간). Microkernel philosophy đẩy nhiều services ra người dùng (user / 사용자) không gian (space / 공간) và giữ kernel nhỏ hơn. Hybrid các hệ thống (systems / 시스템들) pha trộn. sự đánh đổi (trade-off / 트레이드오프) liên quan hiệu năng (performance / 성능), fault isolation và độ phức tạp (complexity / 복잡도).


> **Chuyển mạch:** Từ **Kernel là phần có quyền đặc biệt**, ta sang **lời gọi hệ thống (system call / 시스템 호출)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Lời gọi hệ thống (system call / 시스템 호출)

Lời gọi hệ thống (system call / 시스템 호출) là controlled entry từ chế độ người dùng (user mode / 사용자 모드) vào kernel để yêu cầu thao tác (operation / 연산) privileged: `read`, `write`, `open`, `mmap`, `fork`, `socket`... API ngôn ngữ (language / 언어)/thư viện (library / 라이브러리) có thể wrap syscall; không phải mọi thư viện (library / 라이브러리) lời gọi (call / 호출) đều tạo syscall.

Ví dụ `printf` có thể format hoàn toàn trong người dùng (user / 사용자) không gian (space / 공간) rồi cuối cùng buffer được flush qua `write`. bộ nhớ (memory / 메모리) allocation `malloc` có thể phục vụ từ user-space vùng nhớ động (heap / 힙) pool và chỉ thỉnh thoảng xin thêm pages từ OS.

Lời gọi hệ thống (system call / 시스템 호출) có overhead vì privilege chuyển tiếp (transition / 전이), kiểm tra hợp lệ (validation / 검증) và kernel công việc (work / 작업), nhưng hiện đại (modern / 현대적) kernels/runtimes tối ưu batching, dùng chung (shared / 공유) bộ nhớ (memory / 메모리) và async interfaces để giảm crossings.


> **Chuyển mạch:** Từ **lời gọi hệ thống (system call / 시스템 호출)**, ta sang **tệp (file / 파일) descriptor và handle** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tệp (file / 파일) descriptor và handle

Unix-like OS dùng tệp (file / 파일) descriptor — integer chỉ mục (index / 인덱스) vào per-process bảng (table / 테이블) của open resources. Files, sockets, pipes và devices có thể cùng dùng read/write-like giao diện (interface / 인터페이스). Đây là lớp trừu tượng (abstraction / 추상화) mạnh: “everything is a tệp (file / 파일)” không hoàn toàn literal, nhưng uniform I/O giao diện (interface / 인터페이스) làm composition dễ hơn.

Windows dùng handles rộng hơn. Principle chung là người dùng (user / 사용자) mã (code / 코드) giữ opaque tham chiếu (reference / 참조) thay vì trực tiếp nắm kernel đối tượng (object / 객체).


> **Chuyển mạch:** Từ **tệp (file / 파일) descriptor và handle**, ta sang **tiến trình (process / 프로세스) lớp trừu tượng (abstraction / 추상화)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tiến trình (process / 프로세스) lớp trừu tượng (abstraction / 추상화)

Tiến trình (process / 프로세스) cho program cảm giác có CPU thực thi (execution / 실행) ngữ cảnh (context / 맥락) và address không gian (space / 공간) riêng. Thực tế scheduler multiplex CPU cores giữa many runnable tasks; virtual bộ nhớ (memory / 메모리) maps private-looking addresses tới vật lý (physical / 물리적) pages có thể dùng chung (shared / 공유)/sao chép khi ghi (copy-on-write / 쓰기 시 복사).

OS vì vậy là **tài nguyên (resource / 자원) multiplexer + isolation tầng (layer / 계층)**.


> **Chuyển mạch:** Từ **tiến trình (process / 프로세스) lớp trừu tượng (abstraction / 추상화)**, ta sang **Virtualization của thời gian (time / 시간) và không gian (space / 공간)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Virtualization của thời gian (time / 시간) và không gian (space / 공간)

CPU virtualization: scheduling làm mỗi tiến trình (process / 프로세스) có vẻ đang tiến triển.

Bộ nhớ (memory / 메모리) virtualization: mỗi tiến trình (process / 프로세스) thấy virtual address không gian (space / 공간) riêng.

Lưu trữ (storage / 저장소) virtualization: filesystem biến raw blocks thành named hierarchical files.

Mạng (network / 네트워크) virtualization: sockets cung cấp endpoint lớp trừu tượng (abstraction / 추상화) trên NIC packets.

Lớp trừu tượng (abstraction / 추상화) biến hardware details thành contracts hữu dụng nhưng không xóa các ràng buộc (constraints / 제약조건들). CPU vẫn finite, RAM vẫn finite, disk/mạng (network / 네트워크) vẫn có độ trễ (latency / 지연 시간).


> **Chuyển mạch:** Từ **Virtualization của thời gian (time / 시간) và không gian (space / 공간)**, ta sang **người dùng (user / 사용자) không gian (space / 공간) và kernel không gian (space / 공간)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Người dùng (user / 사용자) không gian (space / 공간) và kernel không gian (space / 공간)

“Kernel không gian (space / 공간)” có thể nói về privileged address region/thực thi (execution / 실행) ngữ cảnh (context / 맥락); “người dùng (user / 사용자) không gian (space / 공간)” là môi trường (environment / 환경) của ordinary processes. dữ liệu (data / 데이터) crossing ranh giới (boundary / 경계) thường cần kiểm tra hợp lệ (validation / 검증)/bản sao (copy / 복사) hoặc dùng chung (shared / 공유) ánh xạ (mapping / 매핑).

Zero-copy techniques cố tránh redundant copies bằng mmap, sendfile, DMA buffers hoặc scatter/gather, nhưng ngữ nghĩa (semantics / 의미론) và bảo mật (security / 보안) vẫn cần kiểm soát quyền sở hữu (ownership / 소유권)/thời gian tồn tại (lifetime / 수명).


> **Chuyển mạch:** Từ **người dùng (user / 사용자) không gian (space / 공간) và kernel không gian (space / 공간)**, ta sang **Interrupt, exception và syscall** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Interrupt, exception và syscall

Cả ba đều có thể chuyển điều khiển (control / 제어) vào kernel nhưng nguyên nhân khác. Hardware interrupt đến từ thiết bị (device / 장치)/timer; exception từ instruction hiện tại như page fault; syscall là intentional yêu cầu (request / 요청) của người dùng (user / 사용자) program theo defined convention.

Phân biệt này giúp debugging: page fault có thể normal demand paging, segmentation fault là chính sách (policy / 정책) reaction khi address invalid, còn syscall thất bại (failure / 실패) thường trả lỗi (error / 오류) mã (code / 코드).


> **Chuyển mạch:** Từ **Interrupt, exception và syscall**, ta sang **Boot và initialization ở mức mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Boot và initialization ở mức mô hình tư duy (mental model / 사고 모델)

Firmware khởi tạo hardware cơ bản, bootloader tải (load / 로드) kernel, kernel setup bộ nhớ (memory / 메모리)/interrupts/drivers rồi start user-space init/dịch vụ (service / 서비스) manager. Không cần thuộc chi tiết để hiểu rằng OS itself cũng là software phải được loaded và granted điều khiển (control / 제어) trước khi applications chạy.


> **Chuyển mạch:** Từ **Boot và initialization ở mức mô hình tư duy (mental model / 사고 모델)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> OS là **mediator có đặc quyền**. Nó multiplex finite resources, enforce isolation và expose stable abstractions. lời gọi hệ thống (system call / 시스템 호출) là cửa có kiểm soát qua ranh giới (boundary / 경계) người dùng (user / 사용자) ↔ kernel.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Mọi hàm (function / 함수) I/O đều là syscall.”** thời gian chạy (runtime / 런타임)/thư viện (library / 라이브러리) buffering có thể gom nhiều operations trước khi syscall.

**“tiến trình (process / 프로세스) có CPU riêng.”** Đó là lớp trừu tượng (abstraction / 추상화); scheduler chia cores theo thời gian (time / 시간) và chính sách (policy / 정책).

**“Kernel là toàn bộ hệ điều hành.”** OS phân phối (distribution / 분포) còn có user-space libraries, daemons, shells, GUI và tools; kernel là privileged cốt lõi (core / 핵심).


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

CPU privilege trong [CPU/ISA](../02_computer_architecture/01_cpu_isa_and_instruction_cycle.md) cho kernel quyền enforce. [Process/thread scheduling](./01_processes_threads_and_scheduling.md), [virtual memory](./03_virtual_memory_and_address_spaces.md) và [filesystem](./04_filesystems_storage_and_io.md) là ba abstractions lớn tiếp theo.

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 processes threads and scheduling](./01_processes_threads_and_scheduling.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
