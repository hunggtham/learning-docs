# Correctness path: language memory model → OS → CPU ordering

Concurrent bug thường bị giải thích quá đơn giản bằng câu “CPU reorder instruction”. Thực tế correctness contract đi qua nhiều layers: source-language memory model, compiler transformations, runtime primitives, OS scheduling và hardware memory ordering. Muốn reasoning đúng phải biết layer nào cho phép điều gì.

## Source code order không phải execution contract tuyệt đối

Compiler có thể reorder hoặc eliminate operations nếu observable behavior theo language model không đổi. CPU cũng thực thi/speculate out-of-order. Nhưng cả hai bị ràng buộc bởi synchronization semantics mà language/ISA định nghĩa.

Do đó nhìn assembly order riêng lẻ chưa đủ để kết luận source program data-race-free.

## Data race

Hai threads truy cập cùng mutable location, ít nhất một write, không có synchronization phù hợp tạo data race trong nhiều language models. Behavior có thể không chỉ là “đọc value cũ”; compiler optimization có thể dựa trên assumption race-free.

Java Memory Model định nghĩa **happens-before** qua monitor lock/unlock, volatile, thread start/join và các rules khác. Nếu write happens-before read, visibility/order được đảm bảo theo model.

## Volatile và atomic

Java `volatile` cung cấp visibility/order semantics mạnh hơn plain field nhưng không biến compound operation như `count++` thành atomic transaction.

Atomic classes dùng compare-and-set hoặc primitives khác để xây read-modify-write semantics. Lock cung cấp mutual exclusion và ordering nhưng có scheduling/contention cost.

## Compiler barrier và CPU fence

Compiler barrier ngăn compiler reorder qua boundary theo một số rules; hardware fence điều khiển memory-ordering visibility ở CPU. High-level synchronization primitive có thể compile thành fence hoặc atomic instruction khác nhau tùy architecture.

x86 tương đối strong-order cho nhiều cases; ARM/RISC-V có weaker ordering hơn. Portable language runtime phải map cùng high-level contract xuống mỗi ISA đúng cách.

## Cache coherence

Coherence đảm bảo các cores không giữ writable versions mâu thuẫn vô hạn cho cùng cache line, nhưng coherence một mình không định nghĩa order của nhiều locations. Vì vậy “cache coherent” không thay thế memory model.

Xem thêm: [Memory consistency, cache coherence và ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md).

## OS scheduler

Thread có thể bị preempt/migrate giữa cores bất kỳ lúc nào. Correct synchronization không được dựa vào assumption “thread A chắc chạy xong đoạn này trước vì thường nhanh hơn”. Sleep/timing không tạo happens-before đáng tin.

## Double-checked locking

Pattern lazy initialization lịch sử từng sai khi publication/order không được đảm bảo. Object reference có thể trở nên visible trước khi initialization effects được thread khác quan sát đúng theo weak model. Modern language patterns dùng volatile/synchronized/static initialization semantics để tạo safe publication.

## Debugging

Race có thể biến mất khi thêm logging vì timing, fences hoặc cache effects thay đổi. Đây là **Heisenbug**. Tool như race detector, stress test và model reasoning đáng tin hơn cố reproduce bằng sleep.

## Mental Model

> Concurrent correctness là contract xuyên layers. Language định nghĩa happens-before; compiler/runtime preserve contract; ISA cung cấp atomics/fences; cache/coherence thực thi visibility; OS quyết định interleaving. Đừng sửa race bằng timing—hãy tạo synchronization edge rõ ràng.