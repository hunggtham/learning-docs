# Mã máy (machine code / 기계어), assembly, ABI và calling convention

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Mã máy (machine code / 기계어), assembly, ABI và calling convention**. Route đi từ instruction encoding → assembly/registers → stack/calling convention → ABI/linking/debugging, để ranh giới compiler–runtime–hardware được truy ra qua dữ liệu thực.

High-level hàm (function / 함수) lời gọi (call / 호출) như `sum(a,b)` cuối cùng phải trở thành instructions, register usage, ngăn xếp (stack / 스택) bố cục (layout / 레이아웃) và nhị phân (binary / 이진) interfaces mà CPU/OS hiểu. mã máy (machine code / 기계어) là encoded bytes của ISA instructions; assembly là human-readable symbolic notation cho chúng. ABI định nghĩa conventions để independently compiled pieces phối hợp.

## Mã máy (machine code / 기계어) và assembly

Instruction có opcode và operands encoded theo ISA. Assembly viết symbolic mnemonics như `mov`, `add`, `ldr`, `bl`. Assembler biến chúng thành mã máy (machine code / 기계어); disassembler làm chiều ngược gần đúng.

Assembly không phải nguồn (source / 소스) “gần CPU tuyệt đối”: hiện đại (modern / 현대적) CPU có micro-ops và out-of-order internals. Nó là biểu diễn (representation / 표현) gần **architectural ISA**.

Machine code là encoding mà CPU thực thi, còn assembly là notation để con người đọc encoding đó. Khi nhiều module được biên dịch độc lập phối hợp, ABI và calling convention quy định cách registers, arguments và stack frame gặp nhau.

## Calling convention

Nếu trình biên dịch (compiler / 컴파일러) A và trình biên dịch (compiler / 컴파일러) B cùng mục tiêu (target / 대상) nền tảng (platform / 플랫폼), chúng phải thống nhất hàm (function / 함수) arguments ở registers/ngăn xếp (stack / 스택) nào, return giá trị (value / 값) ở đâu, registers nào caller/callee phải preserve, ngăn xếp (stack / 스택) alignment ra sao.

Calling convention (호출 규약) là phần của ứng dụng (application / 애플리케이션) nhị phân (binary / 이진) giao diện (interface / 인터페이스) — ABI. Không có convention, hàm (function / 함수) từ thư viện (library / 라이브러리) không biết caller đặt argument ở đâu.

Ví dụ conceptual:

```text
caller:
  place args in agreed registers
  call target
callee:
  save required registers
  create stack frame if needed
  compute
  put result in return register
  restore state
  return
```

Details khác giữa x86-64 hệ thống (system / 시스템) V, Windows x64, AArch64 ABI.

Calling convention quy định nơi đặt arguments và kết quả; stack frame hiện thực một phần quy ước đó khi hàm cần locals, saved registers hoặc return metadata. Sau khi các hàm đã có layout, linker phải nối references giữa các object files.

## Ngăn xếp (stack / 스택) frame

Hàm (function / 함수) may allocate ngăn xếp (stack / 스택) frame cho locals/spilled registers/return siêu dữ liệu (metadata / 메타데이터). trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화) có thể omit frame pointer, inline hàm (function / 함수) hoặc giữ cục bộ (local / 로컬) hoàn toàn trong registers. Vì vậy tầng mã nguồn (source-level / 소스 수준) lời gọi (call / 호출) không map 1:1 với visible frames trong optimized nhị phân (binary / 이진).

Ngăn xếp (stack / 스택) grows direction theo kiến trúc (architecture / 아키텍처)/ABI convention; đừng đồng nhất “ngăn xếp (stack / 스택)” lớp trừu tượng (abstraction / 추상화) với một address direction universal.

Stack frame giải quyết layout trong một lời gọi. Linker và symbols giải quyết tên cùng địa chỉ giữa nhiều module, từ đó tạo binary có thể nạp; đây là chỗ cần phân biệt binary contract với source-level API.

## Linker và symbols

Trình biên dịch (compiler / 컴파일러) có thể tạo đối tượng (object / 객체) files chứa mã máy (machine code / 기계어) + symbol/relocation thông tin (information / 정보). Linker resolve references giữa modules/libraries, assign addresses và tạo executable/dùng chung (shared / 공유) thư viện (library / 라이브러리).

Static linking bản sao (copy / 복사) needed mã (code / 코드) vào executable. động (dynamic / 동적) linking defer một phần tới tải (load / 로드)/thời gian chạy (runtime / 런타임) và share libraries. Position-independent mã (code / 코드) và relocation giúp binaries tải (load / 로드) ở varying addresses, quan trọng cho ASLR.

Linker có thể nối được symbols chỉ khi các module chia sẻ những giả định binary phù hợp. ABI mô tả các giả định ấy ở mức rộng hơn API, còn syscall convention cho thấy một ABI đặc biệt giữa user space và kernel.

## ABI vs API

API là tầng mã nguồn (source-level / 소스 수준) đặc tả hợp đồng (contract / 계약): hàm (function / 함수) names/types/ngữ nghĩa (semantics / 의미론). ABI là binary-level đặc tả hợp đồng (contract / 계약). Có thể API-compatible nhưng ABI-incompatible nếu đối tượng (object / 객체) bố cục (layout / 레이아웃)/calling convention đổi; ngược lại wrapper có thể giữ ABI dù hiện thực (implementation / 구현) nguồn (source / 소스) thay đổi.

Java/JVM ecosystem thường tương tác qua bytecode/lớp (class / 클래스) format thay vì bản địa (native / 네이티브) ABI ở ứng dụng (application / 애플리케이션) tầng (layer / 계층), nhưng JNI/bản địa (native / 네이티브) libraries vẫn quay lại nền tảng (platform / 플랫폼) ABI.

Syscall convention mở rộng binary contract qua ranh giới user/kernel: ngoài arguments còn có syscall number, trap và error convention. Khi quan sát một binary đã chạy, debug symbols giúp ánh xạ địa chỉ và registers ngược về những khái niệm này.

## Syscall convention

Lời gọi hệ thống (system call / 시스템 호출) cũng dùng ABI-like đặc tả hợp đồng (contract / 계약): syscall number, argument registers, instruction/trap cơ chế (mechanism / 메커니즘) và return/lỗi (error / 오류) convention. người dùng (user / 사용자) thư viện (library / 라이브러리) như libc có thể wrap raw syscall bằng friendlier API.

Debug symbols không thay đổi code đang thực thi; chúng thêm bản đồ để debugger và profiler đọc code đó. Bản đồ này hoàn tất chuỗi từ instruction bytes tới nguồn và dẫn vào mô hình build/runtime ở phần sau.

## Gỡ lỗi (debug / 디버그) symbols

Mã máy (machine code / 기계어) không giữ đầy đủ names/types/nguồn (source / 소스) lines. gỡ lỗi (debug / 디버그) info như DWARF/PDB map addresses về nguồn (source / 소스) concepts. Strip symbols giảm nhị phân (binary / 이진) siêu dữ liệu (metadata / 메타데이터) nhưng làm debugging/profiling khó hơn.

Compiler, assembler, linker và loader nối các representation khác nhau thành một binary có thể chạy. Mô hình đó là nền để phân biệt các ngộ nhận về assembly, ABI và stack frame.

## Mô hình tư duy (mental model / 사고 모델)

> trình biên dịch (compiler / 컴파일러) tạo mã (code / 코드), assembler encode instructions, linker nối symbols, loader map nhị phân (binary / 이진), ABI bảo đảm các pieces đồng ý về **nhị phân (binary / 이진) conversation**.

## Dùng chung (common / 공통) Misconceptions

**“Assembly là mã máy (machine code / 기계어).”** Assembly là textual symbolic biểu diễn (representation / 표현); assembler encode thành bytes.

**“API tính tương thích (compatibility / 호환성) = nhị phân (binary / 이진) tính tương thích (compatibility / 호환성).”** Không nhất thiết; ABI có thêm bố cục (layout / 레이아웃)/calling/binary-format contracts.

**“Mỗi nguồn (source / 소스) hàm (function / 함수) luôn có một ngăn xếp (stack / 스택) frame.”** tối ưu hóa (optimization / 최적화) có thể inline, tail-call, scalar-replace hoặc omit frame.

Các ngộ nhận trên đều nhầm representation hoặc contract ở một tầng với tầng khác. Kết nối cuối file đưa chuỗi này về CPU/ISA, compiler/JIT, syscall và build system, nơi từng contract có owner riêng.

## Kết nối

Chapter này nối [CPU/ISA](./01_cpu_isa_and_instruction_cycle.md) với [compiler/JIT](../04_programming_languages/03_compilers_interpreters_vm_and_jit.md), [kernel/syscalls](../03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) và [build/link/package](../08_software_systems/01_version_control_build_link_and_packages.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
