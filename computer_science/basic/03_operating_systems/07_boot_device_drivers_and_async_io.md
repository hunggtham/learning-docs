# Boot, thiết bị (device / 장치) drivers và asynchronous I/O

> **Mạch đọc:** Đọc **Boot, thiết bị (device / 장치) drivers và asynchronous I/O** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Từ power-on đến người dùng (user / 사용자) không gian (space / 공간)** sang **trình điều khiển thiết bị (device driver / 장치 드라이버) là translator giữa OS mô hình (model / 모델) và hardware giao thức (protocol / 프로토콜)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một program gọi `read()` và nhận bytes, nhưng để bytes đi từ SSD/NIC/keyboard tới người dùng (user / 사용자) không gian (space / 공간) cần firmware, kernel, drivers, interrupts, DMA, queues và scheduler. Chapter này nối lớp trừu tượng (abstraction / 추상화) “thiết bị (device / 장치)/tệp (file / 파일)/socket” với cơ chế OS phía dưới.

## Từ power-on đến người dùng (user / 사용자) không gian (space / 공간)

Khi máy bật, CPU bắt đầu tại một reset véc-tơ (vector / 벡터) xác định bởi kiến trúc (architecture / 아키텍처). Firmware như UEFI khởi tạo phần cứng cơ bản, chọn boot mục tiêu (target / 대상) và tải (load / 로드) bootloader hoặc OS ảnh (image / 이미지).

Kernel sau đó thiết lập bộ nhớ (memory / 메모리) management, interrupt tables, scheduler, thiết bị (device / 장치) discovery/drivers, mount gốc (root / 루트) filesystem và cuối cùng start init/dịch vụ (service / 서비스) manager rồi user-space processes.

Boot chuỗi (sequence / 시퀀스) cho thấy OS không xuất hiện “từ hư không”; nó phải tự xây những abstractions mà applications sau đó coi là mặc định.


> **Chuyển mạch:** Từ **Từ power-on đến người dùng (user / 사용자) không gian (space / 공간)**, ta sang **trình điều khiển thiết bị (device driver / 장치 드라이버) là translator giữa OS mô hình (model / 모델) và hardware giao thức (protocol / 프로토콜)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trình điều khiển thiết bị (device driver / 장치 드라이버) là translator giữa OS mô hình (model / 모델) và hardware giao thức (protocol / 프로토콜)

Driver (장치 드라이버) biết registers, command queues và interrupt hành vi (behavior / 동작) của thiết bị (device / 장치), đồng thời expose giao diện (interface / 인터페이스) mà kernel subsystems hiểu.

Filesystem không nên biết chi tiết từng NVMe controller; mạng (network / 네트워크) ngăn xếp (stack / 스택) không nên biết từng NIC mô hình (model / 모델). Driver là lớp trừu tượng (abstraction / 추상화) adapter ở ranh giới (boundary / 경계) hardware-specific.

Một buggy kernel driver nguy hiểm vì chạy privileged. User-space drivers và sandboxing được dùng ở một số architectures để giảm blast radius.


> **Chuyển mạch:** Từ **trình điều khiển thiết bị (device driver / 장치 드라이버) là translator giữa OS mô hình (model / 모델) và hardware giao thức (protocol / 프로토콜)**, ta sang **Memory-mapped I/O và cổng (port / 포트) I/O** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Memory-mapped I/O và cổng (port / 포트) I/O

Nhiều devices expose điều khiển (control / 제어)/status registers vào bộ nhớ (memory / 메모리) address không gian (space / 공간). CPU đọc/ghi addresses đặc biệt để command thiết bị (device / 장치). Đây là memory-mapped I/O (MMIO).

Các accesses này có thứ tự (ordering / 순서)/volatility ngữ nghĩa (semantics / 의미론) khác normal RAM; trình biên dịch (compiler / 컴파일러)/CPU không được tự do optimize như ordinary bộ nhớ (memory / 메모리). Hardware programming vì vậy gắn chặt với bộ nhớ (memory / 메모리) barriers và kiến trúc (architecture / 아키텍처) rules.


> **Chuyển mạch:** Từ **Memory-mapped I/O và cổng (port / 포트) I/O**, ta sang **Interrupt và polling** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Interrupt và polling

Nếu CPU liên tục hỏi thiết bị (device / 장치) “xong chưa?” thì đó là polling. Polling đơn giản và có độ trễ (latency / 지연 시간) thấp khi sự kiện (event / 이벤트) tỷ lệ (rate / 비율) cực cao, nhưng waste CPU nếu events thưa.

Interrupt cho thiết bị (device / 장치) báo CPU khi cần attention. Interrupt có overhead ngữ cảnh (context / 맥락)/handler, nên hiện đại (modern / 현대적) các hệ thống (systems / 시스템들) có hybrid strategies như interrupt moderation hoặc busy polling trong high-performance networking.


> **Chuyển mạch:** Từ **Interrupt và polling**, ta sang **DMA: thiết bị (device / 장치) chuyển dữ liệu (data / 데이터) mà CPU không bản sao (copy / 복사) từng byte** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## DMA: thiết bị (device / 장치) chuyển dữ liệu (data / 데이터) mà CPU không bản sao (copy / 복사) từng byte

Direct bộ nhớ (memory / 메모리) truy cập (access / 접근) (DMA) cho thiết bị (device / 장치) đọc/ghi RAM theo descriptors do driver thiết lập. CPU setup transfer, thiết bị (device / 장치) thực hiện bulk dữ liệu (data / 데이터) movement, rồi completion được báo bằng interrupt hoặc hàng đợi (queue / 큐) polling.

DMA tăng hiệu năng (performance / 성능) nhưng tạo bảo mật (security / 보안) yêu cầu (requirement / 요구사항): thiết bị (device / 장치) không được tùy ý truy cập (access / 접근) toàn bộ nhớ (memory / 메모리). IOMMU cung cấp address translation/isolation cho thiết bị (device / 장치) tương tự virtual bộ nhớ (memory / 메모리) cho CPU.


> **Chuyển mạch:** Từ **DMA: thiết bị (device / 장치) chuyển dữ liệu (data / 데이터) mà CPU không bản sao (copy / 복사) từng byte**, ta sang **Blocking, non-blocking và asynchronous I/O** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Blocking, non-blocking và asynchronous I/O

Blocking I/O làm luồng thực thi (thread / 스레드) chờ cho tới khi thao tác (operation / 연산) có thể hoàn thành hoặc có dữ liệu (data / 데이터). Non-blocking I/O trả ngay nếu chưa sẵn sàng, thường với status như `EAGAIN`.

Readiness APIs như `select`, `poll`, `epoll`, `kqueue` báo descriptors nào sẵn sàng. Completion-based APIs như IOCP hoặc `io_uring` có thể biểu diễn “submit thao tác (operation / 연산), nhận completion sau”.

Async cú pháp (syntax / 문법) trong ngôn ngữ (language / 언어) không tự quyết OS I/O mô hình (model / 모델). Một `async/await` thời gian chạy (runtime / 런타임) có thể đứng trên readiness, completion ports, luồng thực thi (thread / 스레드) pool hoặc combination.


> **Chuyển mạch:** Từ **Blocking, non-blocking và asynchronous I/O**, ta sang **Thundering herd và sự kiện (event / 이벤트) loops** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thundering herd và sự kiện (event / 이벤트) loops

Nếu nhiều workers cùng thức dậy vì một sự kiện (event / 이벤트) nhưng chỉ một worker có công việc (work / 작업), hệ thống lãng phí scheduling/ngữ cảnh (context / 맥락) switches. Kernel/thời gian chạy (runtime / 런타임) designs cố tránh thundering herd bằng wakeup policies và hàng đợi (queue / 큐) quyền sở hữu (ownership / 소유권).

Vòng lặp sự kiện (event loop / 이벤트 루프) xử lý nhiều concurrent connections với ít threads bằng cách multiplex I/O readiness/completions. Nó hiệu quả khi tasks chủ yếu I/O-bound và handlers không khối (block / 블록) dài.


> **Chuyển mạch:** Từ **Thundering herd và sự kiện (event / 이벤트) loops**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Async nghĩa là chạy song song.”** Async là về waiting/tính đồng thời (concurrency / 동시성); parallel thực thi (execution / 실행) cần nhiều thực thi (execution / 실행) resources hoặc threads/cores.

**“Interrupt luôn tốt hơn polling.”** tải công việc (workload / 워크로드) event-rate cao có thể khiến polling hoặc hybrid efficient hơn.

**“Driver chỉ là thư viện.”** Kernel driver có privilege và hardware truy cập (access / 접근) đặc biệt; thất bại (failure / 실패) impact khác user-space thư viện (library / 라이브러리).


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> I/O là chuỗi xử lý (pipeline / 파이프라인) điều phối giữa CPU, bộ nhớ (memory / 메모리) và thiết bị (device / 장치). OS chọn khi CPU nên chạy, khi nên ngủ, ai sở hữu buffer và completion được báo bằng cơ chế nào.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc cùng [I/O, interrupt và DMA ở architecture](../02_computer_architecture/03_io_interrupts_dma_and_devices.md), [process scheduling](./01_processes_threads_and_scheduling.md), [IPC](./06_ipc_signals_pipes_and_shared_memory.md) và [network sockets](../06_networks_distributed_systems/06_sockets_ipv6_nat_firewalls_and_vpn.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 kernel syscalls and os abstractions](./00_kernel_syscalls_and_os_abstractions.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
