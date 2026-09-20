# Debugging xuyên abstraction layers

Production bug thường xuất hiện ở layer A nhưng nguyên nhân nằm layer B hoặc interaction giữa nhiều layers. Advanced debugging vì vậy cần tránh hai cực: nhảy ngay xuống assembly/kernel, hoặc chỉ nhìn application log và giả định abstraction luôn giữ.

## Bắt đầu ở layer cao nhất còn giải thích được symptom

Nếu API trả sai business result, kiểm tra invariant/domain state trước CPU cache. Nếu latency spike chỉ khi traffic cao, xem queues/pools/saturation trước tối ưu algorithm vi mô.

Đi xuống layer thấp hơn khi evidence cho thấy contract của layer hiện tại không đủ giải thích symptom.

## Xây timeline thay vì collection log rời rạc

Một incident cần ordering: request bắt đầu, acquire connection, query gửi, lock wait, timeout, retry, queue growth, downstream recovery. Trace ID, monotonic timestamp và resource metrics giúp ghép causal sequence.

Wall clock giữa hosts có uncertainty; distributed tracing order không nên giả định nanosecond timestamps từ hai machines là tuyệt đối chính xác.

## Symptom, mechanism và root condition

CPU 100% là symptom. Mechanism có thể GC loop, regex pathological, spin lock, serialization hoặc legitimate load. Root condition có thể retry storm do downstream timeout.

Nếu chỉ fix mechanism gần nhất—tăng CPU—system có thể tái phát. Debugging tốt truy ngược feedback loop gây state đó.

## Boundary checklist

Ở mỗi boundary, hỏi:

```text
representation có đổi không?
queue/buffer có xuất hiện không?
ownership/lifetime đổi không?
retry/timeout có tạo duplicate không?
clock/order assumption có đổi không?
security principal có đổi không?
cache có thể stale không?
```

Nhiều bug nằm đúng tại những transformations này.

## Ví dụ: request chậm nhưng DB query nhanh

DB dashboard báo query 20 ms, API mất 2 s. Có thể 1.8 s nằm ở connection-pool wait trước khi query bắt đầu. Query tracing chỉ đo service time sau acquire nên bỏ qua queue delay.

Fix index sẽ không giải. Cần đo pool utilization, acquire wait, transaction duration và caller concurrency.

## Ví dụ: file đã `write()` nhưng mất sau crash

Application thấy write syscall return thành công, nhưng data có thể mới ở page cache. Nếu durability contract cần survive power loss, cần hiểu `fsync`/DB WAL/storage cache behavior.

Abstraction “file write succeeded” khác “data durable on non-volatile medium”. Đây là leaky abstraction khi requirement đòi guarantee mạnh hơn API mặc định.

## Ví dụ: concurrent bug chỉ trên production hardware

Source code nhìn ordered, test x86 pass, nhưng port architecture khác fail. Có thể language code có data race/insufficient happens-before và vô tình dựa strong memory behavior.

Debugging cần đi từ language memory model → compiler transforms → ISA ordering, không patch bằng sleep.

## Evidence ladder

Ưu tiên evidence theo độ gần mechanism: reproducible minimal case; trace/timeline; profiler/counters; structured logs; metrics; anecdotal observation. Nhưng mỗi tool cũng có observer effect và blind spot.

Một metric aggregate có thể che tail. Sampling profiler có thể bỏ rare event. Log có thể bị buffered/drop khi overload. Confidence nên dựa nhiều independent signals khi incident quan trọng.

## Mental Model

> Debugging xuyên layers là **contract-driven descent**: bắt đầu ở abstraction cao nhất, xác định contract nào bị vi phạm hoặc không đủ mạnh, thu evidence tại boundary, rồi chỉ đi xuống layer thấp hơn khi cần giải thích mechanism.

## Kết nối

Đọc [leaky abstractions](../../basic/90_connections/04_abstraction_layers_and_leaky_abstractions.md), [browser→database](../../basic/90_connections/01_browser_to_database_request.md), [queueing/tail latency](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md) và [kernel syscall path](../../03_operating_systems/advanced/00_kernel_execution_contexts_and_syscall_path.md).