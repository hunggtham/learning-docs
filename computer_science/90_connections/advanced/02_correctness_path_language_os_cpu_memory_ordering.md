# Đường đi của tính đúng đắn: CPU cache → memory ordering → language memory model → concurrency bug

Lỗi đồng thời thường bị rút gọn thành câu “CPU reorder instruction”. Cách giải thích đó quá thấp tầng để sửa code và cũng quá đơn giản để giải thích behavior thật. Tính đúng đắn của chương trình concurrent là một hợp đồng xuyên nhiều abstraction: source code → mô hình bộ nhớ của ngôn ngữ (language memory model) → compiler/runtime → primitive đồng bộ của OS → ISA và memory ordering → cache/coherence → phần cứng thật.

Điểm quan trọng không phải nhớ từng fence instruction. Ta cần biết **invariant nào mỗi tầng phải giữ**, tầng nào được phép reorder, và evidence nào chứng minh contract đã bị vi phạm.

## 1. Bài toán ban đầu: nhiều execution context cùng nhìn một state

Khi hai threads truy cập cùng state, ta muốn một số property như:

```text
không có hai owner cùng giữ lock
reader chỉ thấy object sau khi object đã được khởi tạo hợp lệ
counter không mất update
state machine không đi qua trạng thái bất hợp lệ
```

Các property này là invariant của chương trình. “Thread A chạy trước thread B trong lần test của tôi” không phải invariant, vì scheduler có thể interleave khác và hardware có thể làm visibility khác intuition source-order.

Do đó concurrency correctness phải được chứng minh bằng **ordering edge** và **ownership rule**, không bằng timing.

## 2. Cache coherence không tạo ra language-level correctness

Nhất quán cache (cache coherence / 캐시 일관성) chủ yếu giải quyết một location: các core phải hội tụ về một thứ tự hợp lệ của writes trên cùng cache line. MESI/MOESI và interconnect protocol quản lý ownership, invalidation và transfer của cache lines.

Nhưng chương trình thường phụ thuộc nhiều locations:

```text
payload = 42
ready = true
```

Reader muốn suy luận rằng nếu thấy `ready == true` thì cũng phải thấy `payload == 42`. Coherence riêng lẻ của `ready` và `payload` không tạo ra quan hệ đó. Đây là lý do phải tách:

```text
coherence     -> một location được quan sát nhất quán ra sao
memory order  -> nhiều memory operations được phép xuất hiện theo thứ tự nào
synchronization -> software tạo ordering guarantee bằng cách nào
```

## 3. Vì sao hardware muốn reorder?

CPU hiện đại che latency bằng out-of-order execution, store buffer, invalidate queue, speculative execution và nhiều outstanding memory operations. Một store có thể được đặt vào store buffer để core tiếp tục chạy trước khi write đã globally visible. Một load độc lập có thể hoàn thành trong khi store cũ hơn còn chờ ownership của cache line.

Performance pressure vì thế đẩy hardware tới behavior yếu hơn intuition “mỗi instruction hoàn tất tuần tự”. Nếu bắt mọi core chờ mọi write visible toàn hệ thống trước khi đi tiếp, throughput và khả năng che memory latency sẽ giảm mạnh.

Invariant của hardware không phải “mọi core thấy mọi write ngay lập tức”. Invariant là **mọi behavior phải nằm trong memory model của ISA**, và các primitive ordering phải có semantics mà compiler/runtime có thể dựa vào.

Đọc sâu hơn tại [Memory consistency, cache coherence và ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md).

## 4. Compiler cũng reorder, nhưng theo contract khác

Compiler không chỉ chuyển source line thành machine instruction một-một. Nó có thể hoist load, eliminate redundant read, giữ value trong register, vectorize hoặc reorder operations nếu transformation giữ behavior mà language specification cho phép.

Điểm này rất quan trọng: một chương trình có data race có thể không chỉ “thỉnh thoảng đọc giá trị cũ”. Với những ngôn ngữ cho optimizer giả định absence của một số race/undefined behavior, compiler có thể tạo machine code khác hẳn intuition source-order.

Vì vậy debugging race bằng cách nhìn assembly rồi nói “CPU chưa reorder ở đây” là chưa đủ. Contract đầu tiên cần kiểm tra là language memory model.

## 5. Happens-before là abstraction chính để reasoning

Quan hệ xảy-ra-trước (happens-before) không có nghĩa “wall-clock xảy ra sớm hơn”. Nó là quan hệ logic được tạo bởi program order, synchronization edges và tính bắc cầu.

Ví dụ trong Java, monitor lock/unlock, `volatile`, thread start/join và các synchronization actions khác tạo những edge cụ thể. Trong C++/Rust atomics, acquire/release hoặc ordering mạnh hơn tạo contract tương ứng.

Mental model:

```text
write data
   ↓ program order
release / unlock / volatile write
   ↓ synchronization edge
acquire / lock / volatile read
   ↓ program order
read data
```

Nếu chuỗi edge tồn tại, software có cơ sở để yêu cầu runtime/compiler/hardware giữ visibility cần thiết. Nếu không có edge, việc “thường xuyên thấy đúng” chỉ là accidental behavior.

## 6. Publication bug: object đã có reference nhưng state chưa hợp lệ

Giả sử một thread khởi tạo object rồi publish reference cho thread khác mà không có synchronization đúng. Invariant mong muốn là:

> Nếu reader thấy reference, reader phải thấy toàn bộ initialization được contract bảo đảm.

Nếu publication không tạo happens-before, reader có thể quan sát state không được bảo đảm. Đây là gốc của nhiều double-checked-locking bug lịch sử và các lỗi lazy initialization tự chế.

Fix đúng không phải thêm `sleep`. Fix là dùng safe-publication mechanism như lock, `volatile`, atomic release/acquire, static initialization hoặc primitive runtime có contract rõ.

## 7. Atomicity, visibility và ordering là ba câu hỏi khác nhau

Một operation có thể atomic nhưng vẫn chưa cung cấp ordering mà protocol cần. Ngược lại, một fence có thể tạo ordering nhưng không biến read-modify-write ghép thành atomic.

Ví dụ `count++` về logic gồm read → add → write. `volatile` trong Java không tự biến toàn bộ sequence thành atomic increment. Atomic counter hoặc lock giải quyết invariant “mỗi increment chỉ được áp dụng đúng một lần”.

Khi review concurrent code, tách ba câu hỏi:

```text
Atomicity: operation có bị interleave thành lost update không?
Visibility: write có được reader hợp lệ quan sát không?
Ordering: reader được phép suy luận các operation khác trước/sau nó thế nào?
```

## 8. OS scheduler quyết định interleaving, không quyết định memory semantics

Hệ điều hành có thể preempt thread, migrate thread sang core khác, thay đổi run-queue placement hoặc làm thread ngủ vì page fault/I/O. Điều này làm interleaving đa dạng hơn và khiến bug dễ hoặc khó xuất hiện hơn.

Nhưng scheduler không sửa một protocol thiếu happens-before. `sleep(10)` chỉ thay xác suất interleaving; nó không tạo synchronization edge hợp lệ.

Đây là một abstraction boundary hay bị nhầm: **OS scheduling quyết định khi nào thread có cơ hội chạy; language/ISA memory model quyết định những quan sát memory nào được phép**.

## 9. False sharing: correctness đúng nhưng performance vẫn hỏng

Hai threads có thể hoàn toàn đúng về synchronization nhưng ghi hai counters khác nhau nằm cùng cache line. Coherence protocol lúc đó vẫn phải chuyển ownership của cả line qua lại giữa cores.

Invariant logic không bị phá, nhưng performance behavior thay đổi:

```text
threads ↑
→ invalidation/coherence traffic ↑
→ cache-line bouncing ↑
→ throughput không tăng hoặc giảm
```

Đây là ví dụ quan trọng cho triết lý của library: cùng một lower-layer mechanism có thể gây **correctness bug** khi ordering contract sai và gây **performance bug** khi data layout sai.

## 10. Lock-free làm proof burden tăng chứ không biến mất

Compare-and-swap (CAS) cho phép xây lock-free data structure, nhưng invariant phải bao gồm nhiều lớp hơn: linearization point, memory ordering, ABA, object reclamation và progress guarantee.

Một CAS thành công chỉ chứng minh value vẫn khớp điều kiện so sánh tại thời điểm primitive chạy. Nó không tự chứng minh node chưa bị free/reuse hoặc mọi field liên quan đã được publish đúng.

Vì vậy lock-free code cần reasoning formal hơn code dùng lock, không phải ít reasoning hơn.

## 11. Failure mode điển hình

Các failure thường xuất hiện dưới những dạng khác nhau nhưng cùng thiếu contract:

```text
lost update
stale read
unsafe publication
check-then-act race
ABA
use-after-free trong reclamation
livelock/starvation
false sharing và cache-line ping-pong
```

Một symptom có thể biến mất khi bật debugger hoặc thêm logging vì instrumentation đổi scheduling, code layout, fence behavior hoặc cache pressure. Đây là reason race thường trở thành Heisenbug.

## 12. Production evidence: đừng chỉ đọc source

Evidence nên đi theo tầng abstraction đang nghi ngờ.

Ở language/runtime layer, dùng race detector khi ecosystem hỗ trợ, thread dump, lock/park statistics, contention profiler, GC/runtime logs và minimal stress test. Ở OS layer, quan sát run queue, context switch, CPU migration, scheduler latency và blocked/off-CPU time. Ở hardware layer, performance counters có thể cho thấy LLC miss, cache-to-cache transfer, stalled cycles hoặc coherence pressure tùy CPU/tooling.

Evidence không thay proof. Race detector có thể không cover mọi interleaving; PMU counter không nói source line nào vi phạm happens-before. Mục tiêu là kết hợp:

```text
invariant/proof
+
reproducible execution
+
runtime/OS/hardware evidence
```

## 13. Causal walkthrough: CPU cache → memory ordering → language model → bug

Một reasoning chain hoàn chỉnh có thể là:

```text
hai cores ghi/đọc shared state
↓
store buffer + cache coherence làm visibility không đồng thời
↓
ISA chỉ bảo đảm ordering theo memory model/fence semantics
↓
compiler map atomic/volatile/lock của language xuống ISA primitive
↓
program thiếu synchronization edge cần thiết
↓
reader không có happens-before guarantee
↓
unsafe publication hoặc stale observation xuất hiện
↓
logging/debugger thay timing nên bug khó tái hiện
```

Điểm sửa đúng nằm ở tầng **program protocol/language memory model**, dù lower layer giải thích vì sao bug có thể lộ ra.

## 14. Checklist reasoning trước khi sửa concurrency bug

Hãy viết invariant bằng câu rõ ràng trước. Xác định shared mutable state và owner. Xác định operation nào cần atomic. Vẽ happens-before edge giữa writer và reader. Chỉ sau đó mới hỏi primitive đó map xuống fence/atomic nào và có cost gì.

Nếu fix performance, kiểm tra thêm contention topology: lock owner, cache line, NUMA node, run queue và memory bandwidth. Nếu fix correctness, không đổi sang ordering yếu hơn chỉ vì benchmark nhanh hơn khi chưa chứng minh protocol.

## Mô hình tư duy

> CPU cache và coherence quyết định dữ liệu di chuyển vật lý thế nào; ISA memory model giới hạn các ordering phần cứng được phép; compiler/runtime phải ánh xạ language memory model xuống các primitive đó; chương trình chỉ đúng khi invariant của nó được biểu diễn bằng synchronization edges hợp lệ. **Lower layer giải thích behavior, nhưng fix phải được đặt ở abstraction layer sở hữu invariant.**

## Kết nối

Đọc cùng [Cache hierarchy foundation](../../basic/02_computer_architecture/02_memory_hierarchy_and_cache.md), [OS concurrency foundation](../../basic/03_operating_systems/02_concurrency_synchronization_and_deadlock.md), [Programming Languages concurrency foundation](../../basic/04_programming_languages/08_concurrency_models_and_memory_safety.md), [Memory consistency advanced](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md) và [Debugging xuyên abstraction layers](./00_debugging_across_abstraction_layers.md).