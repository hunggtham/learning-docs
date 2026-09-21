# Ownership, borrowing, linear/affine types và memory safety

Garbage collection là một cách quản lý lifetime, nhưng không phải cách duy nhất. Một hướng khác là đưa resource ownership vào type system để compiler kiểm tra khi nào value được move, borrow hoặc destroy. Rust làm ý tưởng này phổ biến, nhưng nền tảng lý thuyết liên quan linear/affine types rộng hơn một language cụ thể.

## Resource lifetime là vấn đề semantic

Memory bug như use-after-free xảy ra vì program tiếp tục dùng reference sau khi resource đã hết lifetime. Double free xảy ra khi nhiều path cùng tin rằng chúng chịu trách nhiệm giải phóng.

Nếu ownership chỉ tồn tại trong comment/convention, compiler không thể bảo đảm invariants đó.

## Unique owner

Mental model đơn giản: mỗi resource có một owner chịu trách nhiệm lifetime. Khi owner ra khỏi scope, resource được cleanup theo rule của language/runtime.

Nếu ownership chuyển từ biến `a` sang `b`, `a` không còn được phép sử dụng resource như trước.

```text
owner A --move--> owner B
A invalid         B owns resource
```

Move semantics tránh implicit deep copy và giúp responsibility rõ.

## Borrowing

Không phải function nào cũng cần ownership. Nó có thể chỉ mượn reference tạm thời.

Một rule phổ biến để giữ safety là:

```text
nhiều immutable borrows
        hoặc
một mutable borrow độc quyền
```

Mục tiêu là ngăn aliasing mutable không kiểm soát, nguồn gốc của nhiều data race và iterator invalidation bugs.

## Lifetime là quan hệ, không nhất thiết timestamp

Lifetime annotation không có nghĩa compiler chèn timer. Nó mô tả quan hệ như “reference trả về không được sống lâu hơn object được borrow”.

Compiler kiểm tra graph scope/control-flow để bảo đảm reference không escape quá lifetime cho phép.

## Linear và affine types

**Linear type** về ý tưởng yêu cầu resource được dùng chính xác một lần theo discipline nhất định.

**Affine type** thường cho phép dùng tối đa một lần — có thể bỏ nhưng không duplicate tùy semantics.

Ownership systems thực tế có thể kết hợp nhiều rule, nhưng intuition quan trọng là type system theo dõi **usage count/capability**, không chỉ shape dữ liệu.

## Không chỉ memory

Linear/affine thinking áp dụng cho file handle, socket, transaction token, lock guard hoặc protocol state.

Ví dụ một transaction object có thể được thiết kế sao cho sau `commit()` nó chuyển sang type `CommittedTransaction` và không thể commit lần hai.

Đây là typestate: type thay đổi theo state machine của resource.

## RAII và deterministic cleanup

C++/Rust dùng scope-based destruction mạnh. Resource được release khi owner ra scope, cho deterministic cleanup.

Java dùng GC cho memory nhưng resource như file/socket vẫn cần `try-with-resources` vì GC lifetime không tương đương external resource lifetime.

Điểm chung: memory management strategy và resource management strategy không phải lúc nào cùng một thứ.

## Borrow checker trade-offs

Static ownership checking loại nhiều bug trước runtime nhưng tăng constraints lên program structure. Một số graph/object patterns khó biểu đạt trực tiếp và cần indirection, arena, reference counting hoặc runtime checks.

Đây không phải “compiler quá khó tính” vô nghĩa; nó phản ánh trade-off giữa flexibility runtime và proof static.

## Shared ownership và reference counting

Khi nhiều owner thật sự cần share lifetime, reference counting tăng count khi clone handle và free khi count về zero.

Nhưng cycle `A -> B -> A` có thể giữ count > 0 mãi. Weak reference hoặc tracing GC có thể cần để phá cycle.

Không có một ownership model hoàn hảo cho mọi graph.

## Interior mutability

Đôi khi API muốn giữ outer shared reference nhưng vẫn mutate state qua synchronization/runtime check. Patterns như mutex, atomic cell hoặc runtime borrow checking đưa mutability control vào abstraction bên trong.

Điều này cho thấy “immutable reference” thường nghĩa không có unrestricted mutation qua reference đó, không phải universe đảm bảo bits không bao giờ đổi.

## Concurrency connection

Nếu type system chứng minh object không bị alias mutable giữa threads, một lớp data race biến mất. Rust traits/capabilities như `Send`/`Sync` thể hiện idea này ở language-specific level.

Java dùng memory model, synchronization và safe publication thay vì ownership static toàn diện. Hai ecosystems chọn boundary static/runtime khác nhau.

## FFI boundary

Khi code ownership-safe gọi C API raw pointer, compiler không thể tự biết contract external. `unsafe`/FFI boundary cần encode lại assumptions: ai allocate, ai free, pointer valid bao lâu, callback có giữ pointer không.

Một module safe chỉ mạnh bằng contract ở boundary không-safe.

## Mental Model

> Ownership biến câu hỏi “ai chịu trách nhiệm lifetime và ai được phép mutate?” thành một phần của program semantics. **Borrowing chia quyền truy cập tạm thời mà không chuyển ownership; linear/affine thinking theo dõi quyền sử dụng resource.**

## Common Misconceptions

**“Ownership = không dùng heap.”** Resource vẫn có thể nằm heap; khác ở cách lifetime/aliasing được kiểm soát.

**“GC giải quyết mọi resource bug.”** GC xử lý memory reachability, không tự đảm bảo file/socket/transaction được đóng đúng lúc.

**“Không có aliasing thì code luôn nhanh.”** Safety model và performance liên quan nhưng không đồng nhất; layout, allocation và optimization vẫn quan trọng.

## Kết nối

Chapter này chuẩn bị cho effect/capability systems và structured concurrency. Ở tầng OS, handle lifetime liên quan kernel resources; ở tầng database, transaction/lock ownership là resource protocol rất phù hợp để reasoning bằng typestate.