# Programming language semantics và execution models

Programming language (ngôn ngữ lập trình / 프로그래밍 언어) là một formal system để mô tả computation cho cả con người và implementation tools. Syntax chỉ trả lời “viết thế nào”; semantics trả lời “chương trình đó có nghĩa gì”. Hai languages có syntax giống nhau nhưng evaluation, type conversion, memory, concurrency hoặc error semantics khác nhau có thể tạo behavior rất khác.

## Syntax, semantics và pragmatics

Syntax định nghĩa chuỗi token/construct nào hợp lệ. Semantics gán meaning cho constructs. Pragmatics liên quan cách language được dùng hiệu quả trong ecosystem.

Ví dụ `a + b` syntactically đơn giản nhưng semantics phụ thuộc types: integer addition, floating-point addition, string concatenation, overloaded operator hoặc user-defined method dispatch.

Parser chỉ xác định structure không đủ để biết result; type checker/runtime phải áp semantic rules.

## Static và dynamic semantics

Static semantics là properties có thể kiểm tra trước execution, như name resolution hoặc type constraints. Dynamic semantics mô tả evaluation khi program chạy.

“Static vs dynamic language” thường bị dùng quá rộng. Type checking time, binding time, dispatch, memory allocation và code generation là những dimensions riêng. Python dynamic typing không nghĩa mọi quyết định đều runtime; Java static typing vẫn có dynamic dispatch và JIT compilation.

## Execution model

Một source program có thể đi qua nhiều pipeline:

```text
source
  ↓ parse / analyze
AST / IR
  ↓ compile or interpret
bytecode / machine code / evaluator
  ↓ runtime + OS
CPU / memory / I/O
```

C, Rust thường ahead-of-time compile native code. Java compile source → JVM bytecode rồi interpreter/JIT execute. JavaScript engines parse → internal IR/bytecode → JIT optimize hot paths. Python CPython compile source → bytecode và evaluate trên VM, dù implementation alternatives tồn tại.

“Compiled vs interpreted” vì vậy không phải binary classification của language; nó là implementation strategy.

## Evaluation order

Language quy định hoặc để unspecified order expression evaluation. Side effects khiến order quan trọng. Short-circuit Boolean operators thường chỉ evaluate RHS khi cần. Lazy languages trì hoãn evaluation; eager languages evaluate arguments trước call theo rules.

Nếu code phụ thuộc unspecified order, portability/correctness dễ vỡ.

## Name binding và environment

Identifier như `x` phải được resolved tới binding. Lexical/static scoping dựa source nesting; dynamic scoping dựa call chain runtime. Most mainstream languages dùng lexical scope.

Environment có thể conceptualize mapping names → locations/values. Closure giữ environment cần thiết để function tiếp tục access lexical variables sau outer function return.

## Mutable state và effects

Expression thuần (pure) cho same input cùng output và không observable side effects. Imperative languages cho statements mutate state. I/O, exceptions, time, randomness và shared memory đều là effects.

Functional programming không xóa effects khỏi reality; nó cố isolate/model chúng để reasoning dễ hơn.

## Determinism

Program deterministic khi cùng relevant state/input tạo same observable result. Randomness, time, I/O, concurrency và undefined behavior làm determinism khó hơn. Reproducible builds/tests cố kiểm soát hidden inputs như timezone, locale, random seed và dependency versions.

## Language specification vs implementation

Language spec định nghĩa contract; compiler/runtime implementation có freedom tối ưu miễn observable behavior phù hợp. Java Memory Model, ECMAScript spec hay C standard là ví dụ semantic contracts.

Implementation bug khác language rule. Khi debugging subtle behavior, cần biết câu hỏi đang thuộc spec, runtime implementation hay library.

## Undefined, unspecified và implementation-defined behavior

C/C++ phân biệt các categories này. Undefined behavior không impose requirements, cho compiler optimization freedom nhưng khiến reasoning nguy hiểm nếu program vi phạm. Implementation-defined yêu cầu implementation document choice. Unspecified cho phép vài choices không cần document mỗi occurrence.

Managed languages thường giảm UB ở application level bằng checks/exceptions nhưng native boundaries và data races vẫn có nuances.

## Mental Model

> Programming language là **contract về meaning**, còn compiler/interpreter/runtime là machinery thực hiện contract. Đừng đồng nhất source construct với một implementation vật lý duy nhất.

## Common Misconceptions

**“Compiled language nhanh, interpreted language chậm.”** Implementation, JIT, workload, runtime libraries và optimization quan trọng; classification quá đơn giản.

**“Static typing nghĩa mọi thứ quyết định compile time.”** Dynamic dispatch, allocation, reflection và JIT vẫn runtime.

**“Semantics chỉ là lý thuyết.”** Evaluation order, overflow, equality, memory model và exceptions đều là semantics gây bugs thực tế.

## Kết nối

[Compiler/VM/JIT](./03_compilers_interpreters_vm_and_jit.md) hiện thực pipeline; [types/memory](./01_types_values_references_and_memory.md) làm rõ values/lifetime; [CPU/ABI](../02_computer_architecture/04_machine_code_assembly_and_abi.md) là target native; [concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) gặp language memory model.
