# Errors, exceptions, resources và runtime safety

Failure là một phần của computation contract. Invalid input, unavailable network, exhausted memory, violated invariant và programmer bug không nên bị gộp thành một “error” mơ hồ. Error model tốt giúp caller biết điều gì recoverable, resource nào cần cleanup và state nào còn valid.

## Error categories

Có thể phân biệt rough categories: domain validation failure; environmental/transient failure như timeout; resource exhaustion; programmer invariant violation; hardware/system failure. Boundary không tuyệt đối nhưng recovery policy khác nhau.

Retry invalid password vô hạn không giúp; retry transient 503 có thể hợp lý với backoff; retry non-idempotent payment request mù quáng có thể duplicate charge.

## Return values, result types và exceptions

C-style error codes buộc caller check manually. Exceptions tách error propagation khỏi normal return nhưng tạo non-local control flow. Result/Either types làm success/error explicit trong type system và compose transformations.

Không có mechanism nào tự đảm bảo good design. Quan trọng là encode context, preserve cause và tránh swallowing failures.

## Checked vs unchecked

Checked exceptions buộc declaration/handling một số failures compile-time; unchecked giảm signature noise nhưng dễ bỏ sót. Ecosystems có trade-offs khác. Thay vì tranh luận tuyệt đối, hãy hỏi caller có meaningful recovery không và contract API cần expose gì.

## Resource safety

Memory GC không tự close socket/file/DB connection đúng lúc. Resource lifetime cần deterministic cleanup. RAII, `try/finally`, `try-with-resources`, `defer`, context manager đảm bảo cleanup cả normal và exceptional paths.

Cancellation cũng là error-like control path. Async task cancelled phải release locks/connections/buffers và không để partial state.

## Exception safety và invariants

Một operation có thể fail giữa chừng. Strong exception-safety style cố giữ state unchanged nếu fail; basic guarantee giữ invariants/no leaks dù state thay đổi. Database transaction rollback là analogous mechanism ở persistent state layer.

## Panic/abort vs recoverable error

Invariant corruption đôi khi không nên tiếp tục local recovery vì state không trustworthy. Fail-fast có thể an toàn hơn silently continuing. Nhưng crash whole process có blast radius; supervision/restart architecture có thể isolate failures.

## Memory safety

Memory-safe environment ngăn classes lỗi như use-after-free, out-of-bounds hoặc dangling references ở safe subset/runtime. C/C++ đòi discipline/tooling; Rust ownership enforces many properties statically; Java/.NET checks + GC. Memory safety không ngăn logic bugs, injection hay authorization errors.

## Type safety và runtime safety khác nhau

Type-safe program có thể divide by zero, timeout, OOM hoặc deadlock. Type system chỉ cover properties được model. Richer types/effect systems có thể encode thêm states, nhưng real world luôn có external failures.

## Defensive programming vs contracts

Checking everything everywhere có thể hide programming bugs hoặc duplicate validation. Validate at trust boundaries, assert internal invariants, encode impossible states in types khi hợp lý, và document contract.

## Mental Model

> Error handling là **state-transition design dưới failure**. Hỏi failure xảy ra ở đâu, state còn valid không, operation có retry-safe không, resources nào đang held, và boundary nào chịu trách nhiệm recovery.

## Common Misconceptions

**“Catch Exception rồi log là xử lý lỗi.”** Nếu caller cần biết failure hoặc transaction state chưa recovery, swallowing exception làm hệ thống khó đúng hơn.

**“GC xử lý mọi resource cleanup.”** External resources cần explicit/deterministic lifetime.

**“Retry làm hệ thống reliable.”** Retry có thể khuếch đại overload hoặc duplicate side effects nếu thiếu backoff/idempotency.

## Kết nối

[Transactions](../05_data_databases/02_transactions_acid_and_concurrency_control.md) cung cấp atomic recovery cho DB state; [idempotency](../08_software_systems/04_time_serialization_and_idempotency.md) làm retries an toàn hơn; [fault tolerance](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) mở rộng error handling lên service/system level.
