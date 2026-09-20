# CPU, ISA và instruction cycle

CPU (Central Processing Unit / 중앙 처리 장치) là engine thực thi instructions. Để hiểu nó, cần tách hai tầng: **ISA** là contract software-visible; **microarchitecture** là cách chip cụ thể hiện thực contract đó.

## ISA như boundary giữa software và hardware

Instruction Set Architecture (명령어 집합 구조) định nghĩa instructions, registers, data types ở machine level, addressing modes, privilege behavior và memory model relevant cho software. x86-64 và ARM64 là hai ISA families phổ biến.

Một executable được compile cho ARM64 không trực tiếp chạy trên x86-64 vì machine instruction encoding và semantics khác. OS ABI còn thêm calling convention, syscall convention và binary format.

Microarchitecture có thể thay đổi mạnh giữa CPU generations nhưng vẫn chạy cùng ISA, giống hai database engines cùng expose SQL subset nhưng internal execution khác.

## Registers

Registers là storage cực nhanh trong CPU. General-purpose registers giữ operands, addresses hoặc intermediate values. Program Counter (PC / 명령어 포인터) chỉ instruction kế tiếp. Stack pointer theo dõi call stack convention. Status/flags registers giữ condition bits trên một số architectures.

Compiler register allocation cố giữ hot values trong registers thay vì spill ra memory.

## Fetch, decode, execute

Textbook mô tả instruction cycle:

1. fetch instruction từ address PC;
2. decode opcode/operands;
3. read operands;
4. execute;
5. memory access nếu cần;
6. write result;
7. update PC.

Đây là conceptual model. CPU hiện đại pipeline và overlap nhiều instructions, thậm chí execute out-of-order trong khi giữ architectural result tương đương allowed semantics.

## Load/store và computation

CPU không thường arithmetic trực tiếp trên arbitrary disk/file/object. Data phải nằm trong registers/cache/memory hierarchy. Load đọc memory vào register; store ghi register ra memory. ALU/FPU/vector units xử lý register operands.

Load/store distinction giải thích vì sao memory latency quan trọng: arithmetic có thể rất nhanh nhưng waiting data stall dependency chain.

## Branch và control flow

Conditional branch thay PC theo condition. High-level `if`, loops, function calls cuối cùng tạo control-flow edges. Pipeline cần đoán branch direction/target trước khi biết chắc để giữ units bận. Branch misprediction phải discard speculative work, tạo penalty.

Vì vậy data-dependent unpredictable branches đôi khi chậm hơn branchless vectorizable code, dù source operations count tương tự.

## Privilege levels

CPU hỗ trợ privilege modes để OS kernel chạy quyền cao hơn user applications. User mode không được trực tiếp thao tác page tables hay device registers tùy ý. System call dùng controlled transition vào kernel mode.

Hardware privilege là nền của process isolation và security boundaries; OS không thể chỉ “nhờ program ngoan”.

## Exceptions và interrupts

Synchronous exception phát sinh do current instruction, như divide-by-zero, page fault, invalid opcode. Interrupt thường asynchronous từ device/timer. CPU chuyển control tới handler theo architecture/OS convention, lưu đủ context để resume hoặc xử lý failure.

Page fault nghe như error nhưng có thể là normal mechanism để demand-load virtual memory page.

## Out-of-order và speculative execution

Modern CPU có thể decode instructions thành micro-operations, rename registers, issue operations khi operands ready, execute out-of-order và retire in architectural order. Mục tiêu là khai thác instruction-level parallelism.

Speculation tăng performance nhưng tạo side channels nếu microarchitectural traces như cache state lộ thông tin, điển hình Spectre-class attacks. Đây là connection sâu giữa performance optimization và security model.

## Mental Model

> ISA là **hợp đồng**: software thấy registers/instructions/memory semantics. Microarchitecture là **implementation** có pipeline, cache, speculation và execution units để thực hiện hợp đồng đó nhanh nhất có thể.

## Common Misconceptions

**“CPU chạy từng instruction tuần tự đúng thứ tự source.”** Architectural effects phải tuân semantics, nhưng internal execution có thể overlap/out-of-order.

**“Page fault luôn là lỗi nghiêm trọng.”** Nhiều page faults là demand paging bình thường; invalid access mới dẫn tới signal/exception.

**“x86/ARM chỉ khác cú pháp assembly.”** Chúng khác ISA encoding, registers, memory ordering và ecosystem ABI, dù compilers che nhiều chi tiết.

## Kết nối

[Machine representation](../00_computation_information/02_numbers_and_machine_representation.md) giải thích operands; [cache](./02_memory_hierarchy_and_cache.md) giải thích data arrival; [assembly/ABI](./04_machine_code_assembly_and_abi.md) nối instructions với compiled programs; [kernel/syscall](../03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) dùng privilege transition của CPU.
