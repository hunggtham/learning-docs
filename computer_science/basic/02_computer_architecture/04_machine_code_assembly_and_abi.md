# Machine code, assembly, ABI và calling convention

High-level function call như `sum(a,b)` cuối cùng phải trở thành instructions, register usage, stack layout và binary interfaces mà CPU/OS hiểu. Machine code là encoded bytes của ISA instructions; assembly là human-readable symbolic notation cho chúng. ABI định nghĩa conventions để independently compiled pieces phối hợp.

## Machine code và assembly

Instruction có opcode và operands encoded theo ISA. Assembly viết symbolic mnemonics như `mov`, `add`, `ldr`, `bl`. Assembler biến chúng thành machine code; disassembler làm chiều ngược gần đúng.

Assembly không phải source “gần CPU tuyệt đối”: modern CPU có micro-ops và out-of-order internals. Nó là representation gần **architectural ISA**.

## Calling convention

Nếu compiler A và compiler B cùng target platform, chúng phải thống nhất function arguments ở registers/stack nào, return value ở đâu, registers nào caller/callee phải preserve, stack alignment ra sao.

Calling convention (호출 규약) là phần của Application Binary Interface — ABI. Không có convention, function từ library không biết caller đặt argument ở đâu.

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

Details khác giữa x86-64 System V, Windows x64, AArch64 ABI.

## Stack frame

Function may allocate stack frame cho locals/spilled registers/return metadata. Compiler optimization có thể omit frame pointer, inline function hoặc giữ local hoàn toàn trong registers. Vì vậy source-level call không map 1:1 với visible frames trong optimized binary.

Stack grows direction theo architecture/ABI convention; đừng đồng nhất “stack” abstraction với một address direction universal.

## Linker và symbols

Compiler có thể tạo object files chứa machine code + symbol/relocation information. Linker resolve references giữa modules/libraries, assign addresses và tạo executable/shared library.

Static linking copy needed code vào executable. Dynamic linking defer một phần tới load/runtime và share libraries. Position-independent code và relocation giúp binaries load ở varying addresses, quan trọng cho ASLR.

## ABI vs API

API là source-level contract: function names/types/semantics. ABI là binary-level contract. Có thể API-compatible nhưng ABI-incompatible nếu object layout/calling convention đổi; ngược lại wrapper có thể giữ ABI dù implementation source thay đổi.

Java/JVM ecosystem thường tương tác qua bytecode/class format thay vì native ABI ở application layer, nhưng JNI/native libraries vẫn quay lại platform ABI.

## Syscall convention

System call cũng dùng ABI-like contract: syscall number, argument registers, instruction/trap mechanism và return/error convention. User library như libc có thể wrap raw syscall bằng friendlier API.

## Debug symbols

Machine code không giữ đầy đủ names/types/source lines. Debug info như DWARF/PDB map addresses về source concepts. Strip symbols giảm binary metadata nhưng làm debugging/profiling khó hơn.

## Mental Model

> Compiler tạo code, assembler encode instructions, linker nối symbols, loader map binary, ABI bảo đảm các pieces đồng ý về **binary conversation**.

## Common Misconceptions

**“Assembly là machine code.”** Assembly là textual symbolic representation; assembler encode thành bytes.

**“API compatibility = binary compatibility.”** Không nhất thiết; ABI có thêm layout/calling/binary-format contracts.

**“Mỗi source function luôn có một stack frame.”** Optimization có thể inline, tail-call, scalar-replace hoặc omit frame.

## Kết nối

Chapter này nối [CPU/ISA](./01_cpu_isa_and_instruction_cycle.md) với [compiler/JIT](../04_programming_languages/03_compilers_interpreters_vm_and_jit.md), [kernel/syscalls](../03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) và [build/link/package](../08_software_systems/01_version_control_build_link_and_packages.md).
