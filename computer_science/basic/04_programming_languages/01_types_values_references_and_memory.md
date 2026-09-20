# Types, values, references và memory management

Type system không chỉ là danh sách `int`, `string`, `class`. Type (타입 / kiểu) mô tả tập values và operations hợp lệ, giúp language/runtime encode assumptions. Memory management quyết định values sống ở đâu, ai sở hữu, khi nào reclaim và references có semantics gì.

## Value và representation

Value là semantic entity như integer 42; representation là bit pattern/object layout dùng để hiện thực. Hai values equal không nhất thiết same identity. Java `Integer`, JavaScript objects, Python integers hay C structs có representation/identity khác nhau.

Type có thể influence size/layout nhưng abstraction có thể che physical representation. `String` không phải “mảng chars” universal; Java uses compact-string implementation details, UTF-16 APIs; Rust `String` is UTF-8 buffer abstraction; JS string semantics use UTF-16 code units.

## Static và dynamic typing

Static type checker xác minh constraints trước runtime; dynamic system checks types/operations khi execution. Trade-off không đơn giản safety vs flexibility. Static systems có expressive levels khác nhau; dynamic languages có tests/contracts/static analyzers optional.

Strong/weak typing là thuật ngữ mơ hồ; nên nói cụ thể implicit coercion nào được phép, memory safety ra sao, casts/checks thế nào.

## Nominal và structural typing

Nominal typing dựa declared identity/relationship (`class A implements I`). Structural typing dựa shape/capabilities (“có methods này thì phù hợp”). Java chủ yếu nominal; TypeScript mạnh về structural typing.

Choice ảnh hưởng API evolution và accidental compatibility.

## Value semantics và reference semantics

Value semantics coi variable chứa/copy value conceptually; reference semantics coi variable giữ reference tới object identity. Nhưng languages có nhiều nuances: Java primitives vs object references; C++ value/reference/pointer; Python names bind objects; JavaScript primitives immutable values còn objects referenced.

Aliasing xuất hiện khi nhiều references trỏ cùng mutable object. Mutation qua một alias observable ở alias khác, làm reasoning phức tạp và cần synchronization trong concurrency.

## Stack và heap không phải type rule universal

Stack thường phục vụ call frames và automatic lifetimes; heap phục vụ dynamic lifetimes. Nhưng compiler/runtime có thể escape-analyze, scalar replace, allocate boxes hoặc move objects. Vì vậy “local variable nằm stack, object nằm heap” chỉ là rough implementation model ở một số environments.

Xem OS memory ở [Virtual Memory](../03_operating_systems/03_virtual_memory_and_address_spaces.md).

## Manual management, RAII và garbage collection

C `malloc/free` đặt responsibility reclaim vào programmer. C++ RAII gắn resource lifetime với object lifetime/destructors. Rust ownership/borrowing dùng static rules để kiểm soát aliases/lifetimes và deterministic drop mà không tracing GC.

Tracing GC bắt đầu từ roots, mark reachable objects, reclaim unreachable. Mark-sweep, copying, generational và concurrent collectors có trade-offs pause, throughput, footprint.

Reference counting reclaim khi count về zero, deterministic hơn nhưng cycles cần xử lý; increments/decrements có overhead.

## GC và generational hypothesis

Nhiều managed heaps tận dụng observation rằng nhiều objects “die young”. Young generation collection scan vùng nhỏ thường xuyên; survivors promote. Long-lived objects ít scan hơn.

Write barriers/card tables track references giữa generations để collector không phải scan toàn old heap mỗi young collection.

GC tuning là trade-off latency, throughput và memory headroom, không phải chỉ “increase heap”.

## Ownership và lifetime

Ownership trả lời ai chịu trách nhiệm resource. File descriptor, socket, DB connection và memory đều có lifetime. Memory-safe language vẫn có resource leaks nếu connection không close; GC chỉ reclaim memory/object, không guarantee timely release external resources.

`try-with-resources`, `defer`, `using`, RAII hay context manager encode deterministic cleanup.

## Null và optionality

Null reference đại diện absence nhưng cho phép “missing” xâm nhập mọi reference type nếu language không distinguish. Option/Maybe/nullable types đưa absence vào type system, buộc caller handle branches.

Không có representation miễn phí: tagged union có tag, nullable pointer có thể exploit invalid/null bit patterns. Nhưng semantic clarity thường quan trọng hơn byte tối ưu.

## Variance và generics ở intuition level

Nếu Dog <: Animal, `List<Dog>` có phải subtype `List<Animal>`? Nếu mutable list cho insert Animal, điều đó phá list chó. Vì vậy mutable generics thường invariant; read-only producers có thể covariant, consumers contravariant theo positions.

Java wildcard mnemonic PECS — Producer Extends, Consumer Super — xuất phát từ logic variance này, không phải rule ngẫu nhiên.

## Mental Model

> Type system quản lý **sets of values + allowed operations + assumptions**. Memory model quản lý **identity, aliasing, lifetime và reclamation**. Bugs thường xuất hiện khi assumptions về hai lớp này không khớp.

## Common Misconceptions

**“GC nghĩa không có memory leak.”** Reachable-but-unused objects, caches/listeners và native resources vẫn leak.

**“Reference là memory address.”** Runtime có thể move objects/encode references; semantic reference không bắt buộc expose raw address.

**“Static type system chứng minh program đúng.”** Nó loại classes lỗi trong model của type system, không chứng minh mọi business/property correctness.

## Kết nối

[Machine representation](../00_computation_information/02_numbers_and_machine_representation.md) giải thích bits; [memory layout](../01_algorithms_data_structures/02_memory_models_and_data_layout.md) giải thích locality; [GC/runtime](./03_compilers_interpreters_vm_and_jit.md) hiện thực lifetime; [concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) làm aliasing mutable nguy hiểm.
