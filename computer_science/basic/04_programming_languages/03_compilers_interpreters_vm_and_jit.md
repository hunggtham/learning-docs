# Compiler, interpreter, VM và JIT

Source code phải được biến thành actions ở machine level. Compiler design cho thấy một chuỗi abstractions: text → tokens → syntax tree → semantic representation → intermediate representation → optimized code → machine/runtime execution.

## Lexing và parsing

Lexer/tokenizer nhóm characters thành tokens như identifiers, numbers, operators. Parser dùng grammar để xây parse tree/AST.

Regular-language techniques phù hợp nhiều token patterns; context-free grammars mô tả nested syntax như parentheses/blocks. Nhưng real language parsing còn xử lý precedence, ambiguities và context-sensitive checks.

AST bỏ bớt punctuation không cần thiết và giữ semantic structure. `1 + 2 * 3` phải thành tree thể hiện multiplication binding mạnh hơn addition.

## Semantic analysis

Compiler resolve names, check types, validate control rules, infer types/generics tùy language. Syntax hợp lệ vẫn có thể semantically invalid, như use undefined variable hoặc return wrong type.

Symbol table là mapping names → declarations/metadata theo scopes.

## Intermediate Representation

IR là representation giữa source và target, giúp optimization độc lập language/hardware phần nào. SSA — Static Single Assignment — cho mỗi variable version một assignment, làm dataflow/use-def chains rõ.

LLVM IR, JVM bytecode và compiler-specific IRs ở abstraction levels khác nhau.

## Optimization

Constant folding tính `2*3` trước. Dead-code elimination bỏ computations không observable. Inlining thay call bằng body để mở thêm optimization nhưng tăng code size. Common subexpression elimination reuse result. Loop optimizations/vectorization biến access/control patterns.

Compiler chỉ được optimize nếu giữ semantics theo language spec. Undefined behavior trong C/C++ mở optimization freedom vì compiler được assume UB không xảy ra trong valid program.

## Ahead-of-time compilation

AOT compile trước runtime thành machine code. Startup predictable, không cần runtime compiler, nhưng khó tận dụng exact runtime profile/hardware state trừ profile-guided optimization.

C/C++/Rust thường AOT. Native-image systems compile managed languages với trade-offs reflection/dynamic features.

## Interpretation

Interpreter có thể walk AST hoặc execute bytecode dispatch loop. Nó giảm compile startup và dễ dynamic behavior nhưng dispatch overhead mỗi operation có thể lớn.

Bytecode VM đưa source vào compact instruction set portable. JVM bytecode chạy trên JVM implementations cho platforms khác nhau.

## JIT compilation

Just-In-Time compiler quan sát running program, compile hot methods/loops thành optimized native code. Runtime profile cho biết actual receiver types, branch frequencies, hot paths. JIT có thể speculative optimize rồi deoptimize nếu assumptions fail.

Java HotSpot tiered compilation và modern JS engines dùng variants của idea này. Warm-up benchmark vì vậy quan trọng: code ban đầu và steady-state có thể khác.

## Garbage collector và runtime services

Managed runtime thường cung cấp GC, class loading, exceptions, synchronization, reflection và profiling. Performance không chỉ compiler generated code mà cả runtime behavior.

Safepoint là điểm runtime có thể dừng/coordinate threads cho GC/deoptimization. Stop-the-world pauses không phải toàn bộ GC; concurrent collectors làm nhiều phases song song với application nhưng vẫn cần coordination.

## Linker và loader

Native compiler output object files; linker resolve symbols/relocations. Loader map executable/shared libraries vào process. Dynamic linker có thể lazily resolve symbols. Đây là continuation của [assembly/ABI](../02_computer_architecture/04_machine_code_assembly_and_abi.md).

## Reproducibility và optimization traps

Microbenchmark dễ bị dead-code elimination, constant folding, JIT warmup, GC và CPU frequency changes. Benchmark framework như JMH exists để guard many traps, nhưng vẫn cần representative workload.

## Mental Model

> Compiler/runtime là **semantic-preserving transformation pipeline**. Mỗi stage thay representation để analysis/execution thuận lợi hơn nhưng phải giữ observable program meaning.

## Common Misconceptions

**“Interpreter không compile gì.”** Nhiều interpreters compile source thành bytecode/IR trước evaluation.

**“JIT luôn nhanh hơn AOT.”** Startup, profile quality, code cache, workload duration và AOT PGO có thể đổi kết quả.

**“Optimizer chỉ làm code nhanh hơn mà không đổi gì.”** Nó giữ allowed observable semantics, nhưng timing/debug layout/code shape có thể đổi; UB/data race làm assumptions phức tạp.

## Kết nối

Formal language/computability ở [Computability](../00_computation_information/04_computability_and_limits.md), machine target ở [CPU/ISA](../02_computer_architecture/01_cpu_isa_and_instruction_cycle.md), runtime memory ở [types/memory](./01_types_values_references_and_memory.md), build pipeline ở [build/link/packages](../08_software_systems/01_version_control_build_link_and_packages.md).
