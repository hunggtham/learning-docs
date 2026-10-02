# CPU, ISA và instruction cycle

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **CPU, ISA và instruction cycle**. Route đi từ ISA/binary interface → registers và fetch/decode/execute → datapath/control/exceptions → performance/compatibility, để phần mềm được nối với trạng thái phần cứng thực sự duy trì.

CPU (Central Processing Unit / 중앙 처리 장치) là engine thực thi instructions. Để hiểu nó, cần tách hai tầng: **ISA** là đặc tả hợp đồng (contract / 계약) software-visible; **microarchitecture** là cách chip cụ thể hiện thực đặc tả hợp đồng (contract / 계약) đó.

## ISA như ranh giới (boundary / 경계) giữa software và hardware

Instruction Set kiến trúc (architecture / 아키텍처) định nghĩa instructions, registers, dữ liệu (data / 데이터) types ở machine mức (level / 수준), addressing modes, privilege hành vi (behavior / 동작) và bộ nhớ (memory / 메모리) mô hình (model / 모델) relevant cho software. x86-64 và ARM64 là hai ISA families phổ biến.

Một executable được compile cho ARM64 không trực tiếp chạy trên x86-64 vì lệnh máy (machine instruction / 기계 명령어) encoding và ngữ nghĩa (semantics / 의미론) khác. OS ABI còn thêm calling convention, syscall convention và nhị phân (binary / 이진) format.

Microarchitecture có thể thay đổi mạnh giữa CPU generations nhưng vẫn chạy cùng ISA, giống hai cơ sở dữ liệu (database / 데이터베이스) engines cùng expose SQL subset nhưng nội bộ (internal / 내부) thực thi (execution / 실행) khác.

> **Chuyển mạch:** Trong **CPU, ISA và instruction cycle**, **ISA như ranh giới (boundary / 경계) giữa software và hardware** đã nêu tiêu chí phân biệt, còn **Registers** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Fetch, decode, execute** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Registers

Registers là lưu trữ (storage / 저장소) cực nhanh trong CPU. General-purpose registers giữ operands, addresses hoặc intermediate values. Program Counter (PC / 명령어 포인터) chỉ instruction kế tiếp. ngăn xếp (stack / 스택) pointer theo dõi ngăn xếp lời gọi (call stack / 호출 스택) convention. Status/flags registers giữ điều kiện (condition / 조건) bits trên một số architectures.

Trình biên dịch (compiler / 컴파일러) register allocation cố giữ hot values trong registers thay vì spill ra bộ nhớ (memory / 메모리).

> **Chuyển mạch:** Ở chặng này của **CPU, ISA và instruction cycle**, **Fetch, decode, execute** tiếp nhận điểm tựa từ **Registers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tải (load / 로드)/store và computation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fetch, decode, execute

Textbook mô tả instruction cycle:

1. fetch instruction từ address PC;
2. decode opcode/operands;
3. read operands;
4. execute;
5. bộ nhớ (memory / 메모리) truy cập (access / 접근) nếu cần;
6. ghi (write / 쓰기) kết quả (result / 결과);
7. cập nhật (update / 업데이트) PC.

Đây là conceptual mô hình (model / 모델). CPU hiện đại chuỗi xử lý (pipeline / 파이프라인) và overlap nhiều instructions, thậm chí execute out-of-order trong khi giữ architectural kết quả (result / 결과) tương đương allowed ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU, ISA và instruction cycle**, **Tải (load / 로드)/store và computation** tiếp nhận điểm tựa từ **Fetch, decode, execute** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Branch và điều khiển (control / 제어) luồng (flow / 흐름)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tải (load / 로드)/store và computation

CPU không thường arithmetic trực tiếp trên arbitrary disk/tệp (file / 파일)/đối tượng (object / 객체). dữ liệu (data / 데이터) phải nằm trong registers/bộ nhớ đệm (cache / 캐시)/bộ nhớ (memory / 메모리) hierarchy. tải (load / 로드) đọc bộ nhớ (memory / 메모리) vào register; store ghi register ra bộ nhớ (memory / 메모리). ALU/FPU/véc-tơ (vector / 벡터) units xử lý register operands.

Tải (load / 로드)/store distinction giải thích vì sao bộ nhớ (memory / 메모리) độ trễ (latency / 지연 시간) quan trọng: arithmetic có thể rất nhanh nhưng waiting dữ liệu (data / 데이터) stall phụ thuộc (dependency / 의존성) chuỗi (chain / 사슬).

> **Chuyển mạch:** Trong **CPU, ISA và instruction cycle**, **Tải (load / 로드)/store và computation** xác định đầu vào; **Branch và điều khiển (control / 제어) luồng (flow / 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Privilege levels** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Branch và điều khiển (control / 제어) luồng (flow / 흐름)

Conditional branch thay PC theo điều kiện (condition / 조건). High-level `if`, loops, hàm (function / 함수) calls cuối cùng tạo control-flow edges. chuỗi xử lý (pipeline / 파이프라인) cần đoán branch direction/mục tiêu (target / 대상) trước khi biết chắc để giữ units bận. Branch misprediction phải discard speculative công việc (work / 작업), tạo penalty.

Vì vậy data-dependent unpredictable branches đôi khi chậm hơn branchless vectorizable mã (code / 코드), dù nguồn (source / 소스) operations count tương tự.

> **Chuyển mạch:** Ở chặng này của **CPU, ISA và instruction cycle**, **Branch và điều khiển (control / 제어) luồng (flow / 흐름)** xác định đầu vào; **Privilege levels** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Exceptions và interrupts** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Privilege levels

CPU hỗ trợ privilege modes để OS kernel chạy quyền cao hơn người dùng (user / 사용자) applications. chế độ người dùng (user mode / 사용자 모드) không được trực tiếp thao tác page tables hay thiết bị (device / 장치) registers tùy ý. lời gọi hệ thống (system call / 시스템 호출) dùng controlled chuyển tiếp (transition / 전이) vào kernel chế độ (mode / 모드).

Hardware privilege là nền của tiến trình (process / 프로세스) isolation và bảo mật (security / 보안) boundaries; OS không thể chỉ “nhờ program ngoan”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU, ISA và instruction cycle**, **Exceptions và interrupts** tiếp nhận điểm tựa từ **Privilege levels** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Out-of-order và speculative thực thi (execution / 실행)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exceptions và interrupts

Synchronous exception phát sinh do hiện tại (current / 현재) instruction, như divide-by-zero, page fault, invalid opcode. Interrupt thường asynchronous từ thiết bị (device / 장치)/timer. CPU chuyển điều khiển (control / 제어) tới handler theo kiến trúc (architecture / 아키텍처)/OS convention, lưu đủ ngữ cảnh (context / 맥락) để resume hoặc xử lý thất bại (failure / 실패).

Page fault nghe như lỗi (error / 오류) nhưng có thể là normal cơ chế (mechanism / 메커니즘) để demand-load virtual bộ nhớ (memory / 메모리) page.

> **Chuyển mạch:** Trong **CPU, ISA và instruction cycle**, **Out-of-order và speculative thực thi (execution / 실행)** tiếp nhận điểm tựa từ **Exceptions và interrupts** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Out-of-order và speculative thực thi (execution / 실행)

Hiện đại (modern / 현대적) CPU có thể decode instructions thành micro-operations, rename registers, issue operations khi operands ready, execute out-of-order và retire in architectural thứ tự (order / 순서). Mục tiêu là khai thác instruction-level parallelism.

Speculation tăng hiệu năng (performance / 성능) nhưng tạo side channels nếu microarchitectural traces như bộ nhớ đệm (cache / 캐시) trạng thái (state / 상태) lộ thông tin, điển hình Spectre-class attacks. Đây là liên kết (connection / 연결) sâu giữa hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) và bảo mật (security / 보안) mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **CPU, ISA và instruction cycle**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Out-of-order và speculative thực thi (execution / 실행)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> ISA là **hợp đồng**: software thấy registers/instructions/bộ nhớ (memory / 메모리) ngữ nghĩa (semantics / 의미론). Microarchitecture là **hiện thực (implementation / 구현)** có chuỗi xử lý (pipeline / 파이프라인), bộ nhớ đệm (cache / 캐시), speculation và thực thi (execution / 실행) units để thực hiện hợp đồng đó nhanh nhất có thể.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU, ISA và instruction cycle**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“CPU chạy từng instruction tuần tự đúng thứ tự nguồn (source / 소스).”** Architectural effects phải tuân ngữ nghĩa (semantics / 의미론), nhưng nội bộ (internal / 내부) thực thi (execution / 실행) có thể overlap/out-of-order.

**“Page fault luôn là lỗi nghiêm trọng.”** Nhiều page faults là demand paging bình thường; invalid truy cập (access / 접근) mới dẫn tới tín hiệu (signal / 신호)/exception.

**“x86/ARM chỉ khác cú pháp assembly.”** Chúng khác ISA encoding, registers, bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) và ecosystem ABI, dù compilers che nhiều chi tiết.

> **Chuyển mạch:** Trong **CPU, ISA và instruction cycle**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Machine representation](../00_computation_information/02_numbers_and_machine_representation.md) giải thích operands; [cache](./02_memory_hierarchy_and_cache.md) giải thích dữ liệu (data / 데이터) arrival; [assembly/ABI](./04_machine_code_assembly_and_abi.md) nối instructions với compiled programs; [kernel/syscall](../03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) dùng privilege chuyển tiếp (transition / 전이) của CPU.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
