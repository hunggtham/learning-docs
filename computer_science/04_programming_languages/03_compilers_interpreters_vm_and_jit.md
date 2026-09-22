# Compiler, interpreter, VM và JIT

Source code phải được biến thành actions ở machine level. Compiler design cho thấy một chuỗi abstractions: text → tokens → syntax tree → semantic representation → intermediate representation → optimized code → machine/runtime execution.

Điểm cần giữ xuyên toàn pipeline là **ngữ nghĩa quan sát được (observable semantics)** theo contract của ngôn ngữ. Mỗi stage được phép đổi representation rất mạnh, nhưng không được tùy ý đổi điều mà chương trình hợp lệ có quyền quan sát.

## Lexing và parsing

Lexer/tokenizer nhóm characters thành tokens như identifiers, numbers, operators. Parser dùng grammar để xây parse tree/AST.

Regular-language techniques phù hợp nhiều token patterns; context-free grammars mô tả nested syntax như parentheses/blocks. Nhưng real language parsing còn xử lý precedence, ambiguities và context-sensitive checks.

AST bỏ bớt punctuation không cần thiết và giữ semantic structure. `1 + 2 * 3` phải thành tree thể hiện multiplication binding mạnh hơn addition.

## Semantic analysis

Compiler resolve names, check types, validate control rules, infer types/generics tùy language. Syntax hợp lệ vẫn có thể semantically invalid, như use undefined variable hoặc return wrong type.

Symbol table là mapping names → declarations/metadata theo scopes.

## Intermediate Representation

IR là representation giữa source và target, giúp optimization độc lập language/hardware phần nào. SSA — Static Single Assignment — cho mỗi variable version một assignment, làm dataflow/use-def chains rõ.

LLVM IR, JVM bytecode và compiler-specific IRs ở abstraction levels khác nhau. Không nên đồng nhất mọi IR với “assembly trung gian”; một IR có thể giữ type, exception, control-flow hoặc runtime metadata mà machine ISA không biểu diễn trực tiếp.

## Optimization

Constant folding tính `2*3` trước. Dead-code elimination bỏ computations không observable. Inlining thay call bằng body để mở thêm optimization nhưng tăng code size. Common subexpression elimination reuse result. Loop optimizations/vectorization biến access/control patterns.

Compiler chỉ được optimize nếu giữ semantics theo language spec. Undefined behavior trong C/C++ mở optimization freedom vì compiler được assume UB không xảy ra trong valid program.

Source line không map một-một tới machine instruction. Debugger, profiler và disassembly đều đang quan sát một representation sau optimization, không phải “source chạy từng dòng”.

## Ahead-of-time compilation

AOT compile trước runtime thành machine code. Startup predictable, không cần runtime compiler, nhưng khó tận dụng exact runtime profile/hardware state trừ profile-guided optimization.

C/C++/Rust thường AOT. Native-image systems compile managed languages với trade-offs reflection/dynamic features.

## Interpretation

Interpreter có thể walk AST hoặc execute bytecode dispatch loop. Nó giảm compile startup và dễ dynamic behavior nhưng dispatch overhead mỗi operation có thể lớn.

Bytecode VM đưa source vào compact instruction set portable. JVM bytecode chạy trên JVM implementations cho platforms khác nhau.

## JIT compilation

Just-In-Time compiler quan sát running program, compile hot methods/loops thành optimized native code. Runtime profile cho biết actual receiver types, branch frequencies, hot paths. JIT có thể speculative optimize rồi deoptimize nếu assumptions fail.

Java HotSpot tiered compilation và modern JS engines dùng variants của idea này. Warm-up benchmark vì vậy quan trọng: code ban đầu và steady-state có thể khác.

Phần internals sâu hơn nằm ở [JIT profiling, speculative optimization và deoptimization](./advanced/05_jit_profiling_speculative_optimization_and_deoptimization.md).

## Garbage collector và runtime services

Managed runtime thường cung cấp GC, class loading, exceptions, synchronization, reflection và profiling. Performance không chỉ compiler generated code mà cả runtime behavior.

Safepoint là điểm runtime có thể dừng/coordinate threads cho GC/deoptimization. Stop-the-world pauses không phải toàn bộ GC; concurrent collectors làm nhiều phases song song với application nhưng vẫn cần coordination.

## Linker và loader

Native compiler output object files; linker resolve symbols/relocations. Loader map executable/shared libraries vào process. Dynamic linker có thể lazily resolve symbols. Đây là continuation của [machine code, assembly và ABI](../basic/02_computer_architecture/04_machine_code_assembly_and_abi.md).

API ở source level và ABI ở binary level không phải một contract. Hai thư viện có thể giữ function name giống nhau nhưng đổi layout/calling convention và trở thành binary-incompatible.

## FFI tồn tại vì hai runtime không chia sẻ cùng một thế giới mặc định

**Giao diện hàm ngoại (Foreign Function Interface, FFI / 외부 함수 인터페이스)** cho phép code trong một language/runtime gọi code được biên dịch theo runtime/ABI khác. Ví dụ Java JNI gọi native C/C++, Python extension gọi C, Rust gọi thư viện C, hoặc JavaScript runtime gọi native addon.

Một FFI call không chỉ là “gọi function ở language khác”. Nó là crossing point giữa nhiều contract:

```text
source type system
→ runtime representation
→ FFI marshalling
→ native ABI/calling convention
→ foreign code ownership/lifetime
→ result/error quay lại runtime
```

Nếu hai phía không thống nhất representation, ownership hoặc lifetime, type checker ở phía caller không thể tự cứu chương trình.

## Type ở source không tự quyết định binary representation

Một `String`, `boolean`, object reference hay generic collection ở managed language thường không có binary layout giống `char*`, `bool` hay C struct.

FFI layer phải quyết định cách **chuyển đổi biểu diễn (marshalling / 마샬링)**: copy bytes, pin object, expose pointer, allocate temporary buffer hoặc tạo wrapper/handle.

Ví dụ Java `String` không nên được suy luận là một C NUL-terminated string. Encoding, length, embedded NUL, allocation và ownership đều là contract riêng.

Signature nhìn giống nhau ở source chưa đủ chứng minh interoperability.

## Object layout là implementation contract, không nên đoán từ class definition

Object trong managed runtime có thể chứa header, mark word, class pointer, alignment padding hoặc compressed reference tùy runtime/configuration. GC cũng có thể di chuyển object.

Native code giữ raw pointer tới managed object mà không đi qua approved pin/handle mechanism có thể trở thành dangling pointer sau GC compaction.

Ngược lại, pin quá nhiều object để giữ address cố định có thể làm GC khó compact heap và tăng fragmentation/latency.

Đây là trade-off trực tiếp giữa interop convenience và memory-management invariant.

## Ownership và lifetime là nơi FFI bug thường nghiêm trọng nhất

Khi một pointer crossing boundary, cần trả lời rõ:

```text
ai sở hữu allocation?
ai được free?
allocator nào phải free?
pointer sống tới khi nào?
callback có thể chạy sau khi owner đã teardown không?
foreign side có giữ reference qua async boundary không?
```

Free memory bằng allocator khác allocator đã allocate có thể corrupt heap. Native library giữ callback/user-data pointer sau khi managed wrapper đã bị GC có thể gây use-after-free. Managed side quên release native handle lại gây leak mà GC không nhìn thấy.

Senior-level FFI code vì vậy thường dùng explicit ownership wrapper, `close`/`dispose`/RAII guard hoặc safe handle abstraction thay vì truyền raw pointer tự do.

## Error model cũng phải được dịch qua boundary

C có thể báo lỗi bằng return code + `errno`; C++ có exception; Java/Python có managed exception; Rust dùng `Result` và panic semantics riêng.

Một exception không được giả định có thể tự xuyên qua arbitrary ABI frame. FFI wrapper thường phải bắt lỗi ở phía sở hữu runtime, chuyển nó thành error representation ổn định rồi dựng lại exception/result ở phía caller.

Nếu C++ exception unwind xuyên qua C ABI hoặc panic crossing unsupported FFI boundary, behavior có thể undefined hoặc terminate process tùy platform/runtime.

Invariant an toàn là: **mỗi runtime xử lý stack-unwinding theo contract của chính nó; boundary chuyển error bằng protocol explicit**.

## Thread attachment và runtime state

Một native thread do foreign library tạo ra chưa chắc đã được managed runtime biết tới. Muốn gọi callback vào JVM/Python/VM khác, thread có thể phải attach/acquire runtime state hoặc tuân thủ Global Interpreter Lock/safepoint rules tùy ecosystem.

Ngược lại, giữ runtime lock khi gọi một native operation blocking lâu có thể làm các logical tasks khác bị stall.

Performance của FFI không chỉ là nanoseconds call overhead; nó còn phụ thuộc thread-state transition, lock, pin/copy, allocation và callback frequency.

## Crossing boundary có fixed cost nên call granularity quan trọng

Nếu mỗi element trong một array gọi native function riêng, marshalling/call transition có thể lớn hơn computation. Batching một buffer lớn qua một call thường hiệu quả hơn hàng triệu tiny FFI calls.

Nhưng batching quá lớn tăng temporary memory và latency trước first result. Đây vẫn là latency-throughput trade-off quen thuộc.

Khi benchmark interop, cần tách:

```text
pure native compute
boundary transition
marshalling/copy
allocation
runtime lock/attachment
actual I/O
```

Nếu không, ta dễ kết luận sai “native code chậm” trong khi cost nằm ở conversion path.

## ABI stability và version evolution

Source API có thể tương thích nhưng native binary vẫn hỏng nếu struct layout, symbol name, calling convention hoặc compiler ABI thay đổi. C ABI thường được dùng làm interoperability boundary vì tương đối ổn và đơn giản hơn C++ ABI, nhưng vẫn cần explicit versioning/size fields khi structure evolve.

Một idiom bền hơn là opaque handle:

```text
create_handle() -> opaque pointer/id
operate(handle, ...)
destroy_handle(handle)
```

Caller không phụ thuộc trực tiếp internal struct layout. Đây là information hiding ở binary boundary.

## Security: native boundary có thể bỏ qua safety guarantees của language

Một memory-safe language gọi native library không làm native library trở nên memory-safe. Buffer overflow, use-after-free, integer truncation hoặc unchecked length ở FFI có thể phá process dù phần application còn lại an toàn.

Input crossing FFI vẫn phải được validate theo trust boundary. Với parser/codec/image/native crypto library xử lý bytes từ network, native bug có thể trở thành remote attack surface.

Sandbox/process isolation đôi khi là boundary tốt hơn in-process FFI nếu component native có rủi ro cao hoặc crash không được phép kéo theo process chính.

## Debugging qua mixed stack

Crash ở FFI thường cần evidence ở cả hai worlds: managed stack, native stack, symbol/debug info, core dump/minidump, GC/native memory telemetry và boundary arguments.

Optimized code có thể inline/omit frames; JIT code còn cần runtime metadata để symbolize. Nếu chỉ nhìn exception log phía managed side, segmentation fault trong native code có thể mất context quan trọng.

Một debugging workflow tốt xác định boundary call gần nhất rồi kiểm tra ownership, lengths, thread identity, native error/crash address và version của shared library.

## Reproducibility và optimization traps

Microbenchmark dễ bị dead-code elimination, constant folding, JIT warmup, GC và CPU frequency changes. Benchmark framework như JMH tồn tại để giảm nhiều trap, nhưng vẫn cần representative workload.

Với native/FFI benchmark còn phải kiểm soát library build flags, symbol/version, allocator, CPU architecture và marshalling path. So sánh debug native build với optimized managed build thường không có ý nghĩa.

## Mental Model

> Compiler/runtime là **semantic-preserving transformation pipeline**. Khi chương trình đi qua FFI, nó rời một semantic universe duy nhất và phải dựng một contract mới về binary calling, representation, ownership, error, thread state và lifetime. ABI nói hai binary pieces “nói chuyện” thế nào; FFI quyết định cách semantics của hai runtime được dịch qua cuộc hội thoại đó.

## Common Misconceptions

**“Interpreter không compile gì.”** Nhiều interpreters compile source thành bytecode/IR trước evaluation.

**“JIT luôn nhanh hơn AOT.”** Startup, profile quality, code cache, workload duration và AOT PGO có thể đổi kết quả.

**“Optimizer chỉ làm code nhanh hơn mà không đổi gì.”** Nó giữ allowed observable semantics, nhưng timing/debug layout/code shape có thể đổi; UB/data race làm assumptions phức tạp.

**“Type giống nhau ở hai language thì binary representation giống nhau.”** Không; source type, object layout, encoding và ABI là các contract khác nhau.

**“Memory-safe language vẫn an toàn khi gọi native code.”** Safety guarantee có thể dừng ở FFI boundary nếu native component vi phạm memory/lifetime contract.

**“FFI chậm chỉ vì function call.”** Copy/marshalling, runtime locks, pinning, allocation và call granularity thường quyết định cost lớn hơn instruction `call`.

## Kết nối

Formal language/computability ở [Computability](../basic/00_computation_information/04_computability_and_limits.md), machine target và calling convention ở [CPU/ISA](../basic/02_computer_architecture/01_cpu_isa_and_instruction_cycle.md) và [machine code/ABI](../basic/02_computer_architecture/04_machine_code_assembly_and_abi.md), runtime memory ở [types/memory](./01_types_values_references_and_memory.md), ownership sâu hơn ở [Ownership, borrowing và linear types](./advanced/02_ownership_borrowing_linear_types_and_memory_safety.md), build/link pipeline ở [build/link/packages](../08_software_systems/01_version_control_build_link_and_packages.md), và sandbox boundary ở [Memory safety, mitigations và sandbox](../07_security_reliability/advanced/04_memory_safety_mitigations_and_sandbox_boundaries.md).