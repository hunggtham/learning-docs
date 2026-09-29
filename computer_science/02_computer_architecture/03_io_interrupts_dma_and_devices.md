# I/O, interrupt, DMA và devices

> **Mạch đọc:** Đặt **I/O, interrupt, DMA và devices** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **thiết bị (device / 장치) registers và controllers** sang **Polling vs interrupt**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


CPU không hữu ích nếu không giao tiếp lưu trữ (storage / 저장소), keyboard, display, NIC, sensors hay accelerators. đầu vào (input / 입력)/đầu ra (output / 출력) — I/O (입출력) là ranh giới (boundary / 경계) giữa computation cốt lõi (core / 핵심) và bên ngoài (external / 외부) devices, nơi speed mismatch rất lớn và asynchronous hành vi (behavior / 동작) xuất hiện.

## Thiết bị (device / 장치) registers và controllers

Hardware thiết bị (device / 장치) thường được điều khiển qua controller expose registers/queues. CPU/driver ghi commands, đọc status và map buffers. Memory-mapped I/O làm thiết bị (device / 장치) registers xuất hiện trong address không gian (space / 공간); special instructions là một mô hình (model / 모델) khác.

Driver (장치 드라이버 / trình điều khiển) trong OS biến device-specific giao thức (protocol / 프로토콜) thành generic abstractions như khối (block / 블록) thiết bị (device / 장치), mạng (network / 네트워크) giao diện (interface / 인터페이스) hoặc character thiết bị (device / 장치).


> **Chuyển mạch:** Từ **thiết bị (device / 장치) registers và controllers**, ta sang **Polling vs interrupt** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Polling vs interrupt

Polling: CPU liên tục hỏi “xong chưa?”. Nếu sự kiện (event / 이벤트) rất nhanh/dày, polling có thể hiệu quả vì tránh interrupt overhead; nếu sự kiện (event / 이벤트) hiếm, nó lãng phí CPU.

Interrupt: thiết bị (device / 장치) báo CPU khi cần attention. CPU tạm chuyển tới handler, sau đó scheduler/driver tiếp tục processing. Interrupt giảm busy waiting nhưng có ngữ cảnh (context / 맥락)/coordination overhead; high-rate devices thường batch/interrupt-coalesce.

Sự đánh đổi (trade-off / 트레이드오프) không phải polling xấu, interrupt tốt; nó phụ thuộc sự kiện (event / 이벤트) tỷ lệ (rate / 비율) và độ trễ (latency / 지연 시간) mục tiêu (target / 대상).


> **Chuyển mạch:** Từ **Polling vs interrupt**, ta sang **DMA** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## DMA

Nếu CPU phải bản sao (copy / 복사) từng byte từ NIC/lưu trữ (storage / 저장소) controller vào RAM, thông lượng (throughput / 처리량) bị giới hạn và CPU bận việc đơn giản. Direct bộ nhớ (memory / 메모리) truy cập (access / 접근) — DMA cho phép thiết bị (device / 장치)/controller transfer dữ liệu (data / 데이터) trực tiếp tới/from bộ nhớ (memory / 메모리) sau khi CPU setup descriptor/buffer.

CPU vẫn orchestration, nhưng bulk transfer không cần instruction cho từng word. NIC rings, NVMe queues và GPU transfers đều dùng DMA concepts.


> **Chuyển mạch:** Từ **DMA**, ta sang **Memory-mapped I/O và thứ tự (ordering / 순서)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Memory-mapped I/O và thứ tự (ordering / 순서)

Truy cập (access / 접근) thiết bị (device / 장치) registers không giống normal cached RAM. Reads/writes có side effects và thứ tự (ordering / 순서) requirements. trình biên dịch (compiler / 컴파일러)/CPU reordering phải được kiểm soát bằng volatile ngữ nghĩa (semantics / 의미론), bộ nhớ (memory / 메모리) barriers hoặc architecture-specific rules trong kernel/driver mã (code / 코드).

Đây cho thấy “tải (load / 로드)/store” ở nguồn (source / 소스)/assembly có ngữ nghĩa (semantics / 의미론) phụ thuộc address region và bộ nhớ (memory / 메모리) mô hình (model / 모델).


> **Chuyển mạch:** Từ **Memory-mapped I/O và thứ tự (ordering / 순서)**, ta sang **Blocking, non-blocking và asynchronous I/O** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Blocking, non-blocking và asynchronous I/O

Blocking I/O cho caller ngủ/chờ đến khi thao tác (operation / 연산) progress đủ. Non-blocking trả ngay nếu chưa ready. Async I/O submit yêu cầu (request / 요청) rồi completion đến qua callback/sự kiện (event / 이벤트)/completion hàng đợi (queue / 큐).

Tầng API khác hardware interrupt nhưng mô hình tư duy (mental model / 사고 모델) tương tự: đừng giữ CPU busy khi độ trễ (latency / 지연 시간) nằm ngoài CPU.

High-concurrency servers dùng vòng lặp sự kiện (event loop / 이벤트 루프), async runtimes hoặc many lightweight threads để quản lý hàng nghìn I/O waits mà không cần one OS luồng thực thi (thread / 스레드) per idle liên kết (connection / 연결).


> **Chuyển mạch:** Từ **Blocking, non-blocking và asynchronous I/O**, ta sang **Buffering** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Buffering

Buffers hấp thụ speed mismatch và batch operations. người dùng (user / 사용자) buffer, kernel page bộ nhớ đệm (cache / 캐시), thiết bị (device / 장치) bộ nhớ đệm (cache / 캐시) và controller hàng đợi (queue / 큐) có thể cùng tồn tại. `write()` thành công không nhất thiết dữ liệu (data / 데이터) đã tới stable medium; durability cần flush/fsync ngữ nghĩa (semantics / 의미론) và lưu trữ (storage / 저장소) guarantees.

Điều này quan trọng cho cơ sở dữ liệu (database / 데이터베이스) WAL và filesystem tính đúng đắn (correctness / 정확성).


> **Chuyển mạch:** Từ **Buffering**, ta sang **thiết bị (device / 장치) độ trễ (latency / 지연 시간) và hàng đợi (queue / 큐) độ sâu (depth / 깊이)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thiết bị (device / 장치) độ trễ (latency / 지연 시간) và hàng đợi (queue / 큐) độ sâu (depth / 깊이)

Hiện đại (modern / 현대적) SSD/NVMe có thể xử lý nhiều requests concurrent. hàng đợi (queue / 큐) độ sâu (depth / 깊이) đủ giúp khai thác parallelism; quá nhiều requests tăng queueing độ trễ (latency / 지연 시간). thông lượng (throughput / 처리량) và độ trễ (latency / 지연 시간) vì vậy sự đánh đổi (trade-off / 트레이드오프) theo tải (load / 로드).


> **Chuyển mạch:** Từ **thiết bị (device / 장치) độ trễ (latency / 지연 시간) và hàng đợi (queue / 큐) độ sâu (depth / 깊이)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> I/O là **asynchronous conversation với thiết bị chậm/khác tốc độ**. CPU setup công việc (work / 작업), buffers giữ dữ liệu (data / 데이터), interrupt/completion báo tiến độ, DMA chuyển bulk bytes, OS driver cung cấp lớp trừu tượng (abstraction / 추상화).


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Interrupt luôn nhanh hơn polling.”** High-rate workloads có thể polling/batching tốt hơn.

**“ghi (write / 쓰기)() trả về nghĩa dữ liệu đã bền trên disk.”** Thường chỉ nghĩa kernel accepted bytes; durability phụ thuộc buffering/filesystem/thiết bị (device / 장치) flush.

**“DMA không dùng CPU.”** CPU vẫn setup queues/descriptors và xử lý completion; DMA giảm per-byte bản sao (copy / 복사) công việc (work / 작업).


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

I/O là nền của [kernel/syscalls](../03_operating_systems/00_kernel_syscalls_and_os_abstractions.md), [filesystem](../03_operating_systems/04_filesystems_storage_and_io.md), [database durability](../05_data_databases/04_storage_logs_recovery_and_durability.md) và [network packets](../06_networks_distributed_systems/00_network_layers_packets_and_encapsulation.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 digital logic and circuits](./00_digital_logic_and_circuits.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
