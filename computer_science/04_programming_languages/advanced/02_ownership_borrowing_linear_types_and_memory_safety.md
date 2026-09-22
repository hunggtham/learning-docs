# Ownership, borrowing, linear/affine types và memory safety

Memory safety traditionally được bảo vệ theo nhiều hướng. Garbage-collected languages giữ object sống khi còn reachable và thu hồi tự động. Systems languages như C trao quyền allocation/free trực tiếp cho programmer nhưng dễ tạo use-after-free, double-free hoặc dangling pointer. Ownership mở ra một hướng khác: đưa **resource lifetime, aliasing và quyền sử dụng** vào semantics/type system để compiler loại bỏ một lớp trạng thái nguy hiểm trước runtime.

Điểm advanced không phải học Rust syntax. Cần hiểu invariant: **ai sở hữu resource, ai được phép dùng hoặc mutate nó, quyền đó chuyển giao lúc nào, và boundary nào làm compiler không còn tự chứng minh được invariant.**

## 1. Resource lifetime là vấn đề semantic

Use-after-free xảy ra khi reference còn được dùng sau khi resource đã hết lifetime. Double-free xảy ra khi nhiều control paths cùng tin rằng chúng chịu trách nhiệm cleanup. Leak xảy ra khi không còn path nào thực hiện responsibility đó.

Nếu ownership chỉ tồn tại trong comment hoặc convention, compiler không thể bảo đảm invariant. Ownership-aware semantics biến responsibility thành thứ có thể được kiểm tra bằng data-flow/type rules.

Resource không chỉ là heap memory. File descriptor, socket, mutex guard, transaction handle, GPU buffer hay cryptographic capability đều có lifecycle.

## 2. Unique ownership làm responsibility rõ ràng

Mental model đơn giản là mỗi resource có một owner chịu trách nhiệm lifetime. Khi ownership được **move**, source cũ không còn quyền sử dụng resource như trước.

```text
owner A --move--> owner B
A mất quyền         B chịu trách nhiệm
```

Move semantics tránh implicit duplication của resource-sensitive values và giúp cleanup path rõ hơn.

Invariant cốt lõi là: **không tồn tại hai owner độc lập cùng tin rằng mình có quyền hủy cùng một unique resource.**

## 3. Borrowing tách quyền sử dụng khỏi quyền sở hữu

Function thường chỉ cần dùng resource tạm thời, không cần trở thành owner. **Borrowing (대여/차용)** cho phép code giữ reference trong một lifetime có kiểm soát mà không nhận trách nhiệm destroy resource.

Một discipline điển hình là:

```text
nhiều shared/immutable borrows
        hoặc
một mutable borrow độc quyền
```

Mục tiêu là ngăn unrestricted mutable aliasing — nguồn gốc của nhiều data race, iterator invalidation và temporal bugs.

## 4. Lifetime là quan hệ chứ không phải đồng hồ

Compiler không cần biết reference tồn tại “3 ms”. Nó cần chứng minh reference không sống lâu hơn referent.

Nếu function trả reference tới local stack value đã bị destroy, relation không thể thỏa. Nếu output reference được lấy từ input, compiler cần biết output lifetime bị ràng buộc bởi input nào.

Lifetime vì thế là property của scope/data-flow/ownership graph, không phải timestamp runtime.

## 5. Linear và affine types theo dõi quyền sử dụng

**Linear type** yêu cầu một resource được sử dụng đúng một lần theo discipline lý thuyết. **Affine type** thường cho phép sử dụng tối đa một lần: có thể bỏ nhưng không arbitrary duplicate.

Hệ thống thực tế có thể không tuân một calculus thuần túy, nhưng mental model quan trọng là type system theo dõi **usage/capability**, không chỉ shape của data.

Một integer có thể copy tự do; một unique file handle, lock guard hay signing capability có thể cần semantics khác.

## 6. Typestate: type có thể biểu diễn protocol state

Ownership thinking mở rộng tự nhiên sang **typestate**. Một transaction object có thể chuyển trạng thái:

```text
OpenTransaction
   ├─ commit()   → Committed
   └─ rollback() → RolledBack
```

Nếu API encode state transition vào type, operation như “commit lần hai” có thể trở thành trạng thái không biểu diễn được hoặc khó biểu diễn hơn.

Đây là cách type system giữ invariant của một protocol, không chỉ lifetime memory.

## 7. RAII và deterministic cleanup

C++ và Rust dùng pattern **RAII — Resource Acquisition Is Initialization**: lifetime của resource gắn với lifetime owner object. Khi owner rời scope, destructor/drop chạy deterministic.

Lock guard là ví dụ rõ: acquire lock tạo guard; scope kết thúc thì guard release lock ngay cả khi return sớm hoặc exception/unwind xảy ra theo semantics tương ứng.

Java dùng GC cho memory nhưng vẫn cần `try-with-resources` cho file/socket vì reachability lifetime không đồng nghĩa external-resource lifetime.

## 8. Shared ownership có cost model riêng

Khi nhiều owners thực sự cần share lifetime, reference counting là một strategy: clone handle tăng count, release giảm count, count về zero thì cleanup.

Nhưng cost không miễn phí. Atomic reference counting trong multi-threaded context tạo synchronization traffic. Cycle `A → B → A` có thể giữ count > 0 mãi nếu không có weak reference hoặc tracing mechanism.

“Không dùng GC” không có nghĩa memory management không có runtime cost; cost được chuyển sang refcount, allocator, static constraints hoặc explicit architecture.

## 9. Interior mutability: shared reference không đồng nghĩa bits bất biến

Đôi khi outer API muốn shared reference nhưng state bên trong vẫn thay đổi qua primitive có kiểm soát như mutex, atomic cell hoặc runtime borrow check.

Mental model đúng là: shared/immutable reference không cho phép **unrestricted mutation qua reference đó**. Mutation vẫn có thể xảy ra nếu abstraction bên trong giữ invariant bằng synchronization/runtime validation.

Điều này rất quan trọng khi reasoning concurrency: “API nhìn immutable” không có nghĩa object physically không đổi.

## 10. Ownership và concurrency safety

Nếu type system chứng minh mutable access không bị alias đồng thời giữa threads trừ qua synchronization-safe abstraction, một lớp data race bị loại structurally.

Tuy nhiên ownership không chứng minh toàn bộ concurrent program đúng. Deadlock, starvation, logical race, ordering giữa distributed messages và state-machine bug vẫn tồn tại.

Static ownership chỉ sở hữu một số invariant: lifetime, aliasing và transfer discipline. Đừng mở rộng guarantee vượt quá boundary đó.

## 11. Performance pressure thay đổi trade-off

Static ownership có thể loại runtime checks và giúp compiler reasoning aliasing tốt hơn, nhưng program structure đôi khi phải dùng arena, indirection, copying hoặc reference counting để biểu diễn graph phức tạp.

Shared atomic refcount có thể tạo cache-line contention. Deterministic destruction có thể đẩy cleanup cost vào latency-sensitive path. Arena giảm per-object allocation nhưng đổi lifetime granularity.

Vì vậy “ownership = nhanh” không phải invariant. Performance phụ thuộc layout, allocation strategy, sharing pattern và runtime boundary.

## 12. FFI là nơi static proof dừng lại

Khi code ownership-safe gọi C API bằng raw pointer, compiler không tự biết:

```text
ai allocate?
ai free?
pointer valid tới khi nào?
callee giữ pointer sau return không?
callback chạy thread nào?
resource có được share/mutate đồng thời không?
```

`unsafe`/FFI boundary nghĩa programmer phải chứng minh invariant mà compiler không thể kiểm tra trực tiếp. Safe wrapper chỉ mạnh bằng contract của boundary không-safe phía dưới.

Đây là leaky abstraction điển hình giữa language semantics và ABI/native runtime.

## 13. Failure modes cần phân biệt

Ownership discipline nhắm vào một số class failure:

```text
use-after-free
dangling reference
double free
uncontrolled mutable aliasing
resource leak do ownership không rõ
```

Nhưng vẫn có thể có:

```text
logical race
deadlock
starvation
protocol misuse qua unsafe/FFI
OOM
resource exhaustion
```

Một type-safe program không đồng nghĩa system-level correct.

## 14. Production evidence

Static checker/compiler diagnostic là evidence chính cho proof ở compile time. Runtime sanitizer, heap profiler, leak detector, crash dump và FFI boundary tests giúp tìm violation ở vùng unsafe/native code.

Với reference counting, contention/profile có thể chỉ ra atomic refcount hot path. Với deterministic cleanup, tracing/profiling có thể cho thấy destructor/drop đang nằm trên critical path.

Evidence nên gắn đúng hypothesis: lifetime bug, leak, allocator pressure hay contention không phải cùng một vấn đề.

## 15. Mô hình tư duy

> Ownership biến câu hỏi “ai chịu trách nhiệm lifetime và ai được phép mutate/use?” thành một phần của program semantics. **Move chuyển responsibility; borrow cấp quyền tạm thời; lifetime chứng minh reference không vượt resource; linear/affine discipline giới hạn duplication; typestate có thể encode resource protocol.** Static proof kết thúc ở boundary như FFI/unsafe, nơi programmer phải tái lập invariant bằng contract rõ.

## Kết nối

Đọc tiếp [Effect systems và capabilities](./03_effect_systems_capabilities_and_controlled_side_effects.md), [Coroutine/structured concurrency](./07_coroutines_continuations_async_runtimes_and_structured_concurrency.md), [OS resources/handles](../../03_operating_systems/advanced/00_kernel_execution_contexts_and_syscall_path.md) và [Security boundaries](../../07_security_reliability/advanced/00_security_boundaries_attack_chains_and_exploitability.md).