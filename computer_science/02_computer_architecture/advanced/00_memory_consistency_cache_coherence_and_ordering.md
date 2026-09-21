# Memory consistency, cache coherence và ordering

Trong single-thread code, ta dễ tưởng tượng mỗi read/write xảy ra đúng thứ tự source. Trên multicore hiện đại, compiler, CPU pipeline, store buffer và cache hierarchy đều có thể reorder hoặc trì hoãn visibility miễn vẫn tuân thủ memory model. Vì vậy concurrency correctness không thể reasoning chỉ bằng “dòng nào viết trước”.

## Coherence và consistency là hai câu hỏi khác nhau

**Cache coherence (캐시 일관성)** chủ yếu hỏi: với **một memory location**, các cores cuối cùng có thống nhất về thứ tự writes hay không? Protocol như MESI/MOESI quản lý ownership/state của cache lines để tránh hai cores độc lập sửa cùng một line mà không phối hợp.

**Memory consistency model (메모리 일관성 모델)** hỏi rộng hơn: với nhiều locations và nhiều processors, những order nào của reads/writes được phép quan sát? Sequential consistency là model trực quan: kết quả như thể mọi operations của mọi threads được xen kẽ trong một global order, trong khi mỗi thread giữ program order. Hardware thực tế thường cho phép yếu hơn để tăng performance.

## Store buffer và vì sao write chưa chắc thấy ngay

Khi core thực hiện store, nó có thể đặt write vào store buffer rồi tiếp tục thay vì chờ ownership/cache propagation hoàn tất. Core đó thường có thể forward value từ buffer cho chính nó, nhưng core khác chưa thấy write ngay.

Xét hai threads:

```text
Initially x = 0, y = 0

Thread A:        Thread B:
x = 1           y = 1
r1 = y           r2 = x
```

Trong mental model sequential đơn giản, ta dễ tin `r1 = 0` và `r2 = 0` không thể cùng xảy ra. Trên một số weak-memory behaviors, stores có thể chưa visible cho core kia khi loads xảy ra, nên outcome đó cần được xét theo architecture/language memory model.

## Memory fence/barrier làm gì?

Fence không phải “flush toàn bộ cache”. Nó áp ordering constraints lên classes memory operations theo ISA semantics. Một acquire operation ngăn các operations sau nó bị quan sát như đã xảy ra trước acquire theo model; release ngăn operations trước bị đẩy qua sau release. Full fence thường mạnh hơn và đắt hơn.

Language-level atomics map xuống primitives hardware nhưng không phải một-một. Java `volatile`, C++ atomics và Rust atomics định nghĩa semantics ở language memory model; compiler chọn instructions/fences phù hợp target ISA.

## Coherence protocol và false sharing

Coherence hoạt động theo cache line, không theo từng field. Hai threads sửa hai variables khác nhau nhưng nằm cùng cache line có thể làm line ping-pong giữa cores. Đây là **false sharing**: không có logical sharing ở source, nhưng có physical sharing ở coherence granularity.

Symptoms thường là throughput giảm khi tăng threads, cache-coherence traffic cao và performance tốt lên khi padding/alignment tách hot counters.

## Happens-before là abstraction để reasoning

Ở language/runtime layer, ta thường không reasoning trực tiếp bằng MESI states. Ta dùng relation như **happens-before**: program order, synchronization edges và transitivity tạo ra những visibility guarantees được phép dựa vào.

Điểm quan trọng: “thời gian thực xảy ra trước” và “happens-before theo memory model” không hoàn toàn đồng nghĩa. Nếu thiếu synchronization edge, một write có thể xảy ra vật lý trước nhưng reader vẫn không có guarantee hợp lệ để thấy nó.

## Lock-free không đồng nghĩa wait-free

Atomics và compare-and-swap cho phép lock-free algorithms, nhưng correctness đòi hỏi memory ordering, ABA problem, reclamation và progress guarantees. Lock-free chỉ hứa system-wide progress theo định nghĩa; một thread cụ thể vẫn có thể starve. Wait-free mạnh hơn: mỗi operation hoàn tất trong bounded number of steps theo model.

## Performance reasoning

Ordering mạnh thường dễ reasoning hơn nhưng có thể hạn chế compiler/hardware optimization. Ordering yếu cho performance latitude nhưng tăng proof burden. Chọn memory order vì “nhanh hơn” mà không chứng minh synchronization protocol là một source bug khó tái hiện.

## Mental Model

> Coherence giữ một location không tự mâu thuẫn; consistency định nghĩa những cross-location observations hợp lệ; synchronization primitives tạo ordering mà software có thể dựa vào.

## Kết nối

Nền tảng: [Cache hierarchy](../../basic/02_computer_architecture/02_memory_hierarchy_and_cache.md) và [OS concurrency](../../basic/03_operating_systems/02_concurrency_synchronization_and_deadlock.md). Phần này là prerequisite tự nhiên cho advanced lock-free/concurrency trong OS và programming languages.