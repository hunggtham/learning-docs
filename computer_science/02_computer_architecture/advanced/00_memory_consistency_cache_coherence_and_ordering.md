# Memory consistency, cache coherence và ordering

Trong single-thread code, ta dễ tưởng tượng mỗi read/write xảy ra đúng thứ tự source. Trên multicore hiện đại, compiler, CPU pipeline, store buffer, invalidate queue và cache hierarchy đều được phép trì hoãn hoặc sắp xếp lại một số memory operations để che latency. Vì vậy concurrency correctness không thể reasoning chỉ bằng “dòng nào viết trước”.

Chương này tập trung vào invariant giữa phần cứng và software: **coherence giữ một location có lịch sử hợp lệ; memory-consistency model định nghĩa cross-location observations nào được phép; fence/atomic operations tạo ordering edges để tầng ngôn ngữ xây happens-before.**

## 1. Bài toán ban đầu: performance cần tự do, software cần một hợp đồng

Nếu mỗi store phải chờ mọi core khác quan sát được giá trị mới trước khi core hiện tại chạy tiếp, multicore sẽ lãng phí rất nhiều cycle. Hardware vì thế dùng store buffer, speculative execution và nhiều outstanding memory requests để tiếp tục làm việc trong khi coherence traffic còn đang chạy.

Nhưng software vẫn cần những invariant như:

```text
nếu lock được release rồi thread khác acquire lock đó,
state trong critical section trước phải được quan sát theo contract

nếu flag publication được release-store,
reader acquire-load flag đó phải có ordering đủ để dùng payload đã publish
```

Thiết kế memory model là thỏa hiệp: cho hardware/compiler đủ freedom để tối ưu nhưng định nghĩa các primitive đủ mạnh để software chứng minh correctness.

## 2. Coherence và consistency là hai câu hỏi khác nhau

**Nhất quán cache (cache coherence / 캐시 일관성)** chủ yếu hỏi: với **một memory location**, các cores có thể quan sát writes theo một lịch sử tương thích hay không? Protocol như MESI/MOESI quản lý ownership/state của cache lines để nhiều cache không tự do ghi các phiên bản mâu thuẫn.

**Mô hình nhất quán bộ nhớ (memory consistency model / 메모리 일관성 모델)** hỏi rộng hơn: với nhiều locations và nhiều processors, những order nào của reads/writes được phép quan sát?

Sequential consistency là model trực quan: kết quả như thể mọi memory operations của mọi threads được xen kẽ trong một global order trong khi mỗi thread giữ program order. Hardware thực tế thường cho phép model yếu hơn để đạt performance tốt hơn.

Điểm phải giữ là: **coherence không tự tạo cross-location ordering**. Hai locations `payload` và `ready` có thể từng location đều coherent nhưng reader vẫn không được suy luận `ready == true` kéo theo payload đã visible nếu thiếu synchronization contract.

## 3. Store buffer: vì sao write chưa chắc thấy ngay

Khi core thực hiện store, nó có thể đặt write vào store buffer rồi tiếp tục thay vì chờ ownership/cache propagation hoàn tất. Core đó thường forward được value từ buffer cho chính nó, nhưng core khác chưa chắc thấy write ngay.

Xét hai threads:

```text
Initially x = 0, y = 0

Thread A:        Thread B:
x = 1           y = 1
r1 = y           r2 = x
```

Trong intuition sequential đơn giản, ta dễ tin `r1 = 0` và `r2 = 0` không thể cùng xảy ra. Với memory model cho phép store→load reordering/visibility delay, outcome đó có thể hợp lệ nếu không có synchronization phù hợp.

Đây không phải cache “bị sai”. Hardware đang thực hiện đúng một model yếu hơn intuition source-order.

## 4. Invalidate queue và visibility không phải một sự kiện toàn cục tức thì

Coherence request cũng phải đi qua interconnect và queues. Một core có thể nhận invalidation, acknowledge theo protocol và xử lý local consequences ở thời điểm khác tùy microarchitecture, miễn behavior cuối vẫn nằm trong ISA memory model.

Vì vậy câu “write đã tới L1 nên core khác phải thấy ngay” không phải reasoning hợp lệ. Software không có contract trực tiếp với internal timing của coherence messages; software có contract với ISA ordering primitives và language memory model.

## 5. Fence/barrier làm gì?

Memory fence không phải “flush toàn bộ cache”. Nó áp ordering constraints lên classes memory operations theo semantics của ISA.

Acquire thường được dùng để ngăn operations sau acquire bị quan sát như đã đi trước synchronization point theo contract cần thiết. Release giữ effects trước release không bị đẩy qua publication point theo cách phá protocol. Full fence mạnh hơn và thường hạn chế optimization nhiều hơn.

Một fence đúng phải được reasoning theo câu hỏi:

```text
operation A phải đứng trước operation B trong quan sát nào?
reader/writer nào cần edge đó?
ISA primitive nào thực hiện guarantee tối thiểu cần thiết?
```

Dùng fence “cho chắc” có thể che design yếu và trả performance cost không cần thiết.

## 6. Language atomics không map một-một xuống instruction

Java `volatile`, C/C++/Rust atomics và lock primitives định nghĩa semantics ở **mô hình bộ nhớ ngôn ngữ (language memory model)**. Compiler/runtime ánh xạ contract đó xuống instruction/fence phù hợp với target ISA.

Cùng một acquire-load ở source có thể compile khác trên x86 và ARM vì baseline ordering của hai ISA khác nhau. Điều cần giữ invariant không phải “phải có instruction fence giống nhau”, mà là **machine code trên mỗi target phải thực hiện cùng language-level contract**.

Do đó porting bug thường xuất hiện khi code dựa vào accidental hardware property thay vì language guarantee.

## 7. Happens-before là abstraction software nên dùng

Ở application/runtime layer, ta hiếm khi reasoning trực tiếp bằng MESI states. Ta dùng relation như **xảy-ra-trước (happens-before)**: program order, synchronization edges và transitivity tạo ra visibility/order guarantees hợp lệ.

Điểm quan trọng: “thời gian thực xảy ra trước” không đồng nghĩa với happens-before. Một write có thể xảy ra vật lý trước, nhưng nếu reader không có synchronization edge, language model có thể không cho phép suy luận visibility cần thiết.

Lower layer giải thích **tại sao** stale/reordered observation có thể xuất hiện; language model quyết định **program có quyền dựa vào điều gì**.

## 8. False sharing: coherence đúng nhưng performance sụp

Coherence hoạt động theo cache line, không theo field. Hai threads sửa hai variables khác nhau nhưng nằm cùng cache line có thể làm line ping-pong giữa cores. Đây là **chia sẻ giả (false sharing)**: source không có logical sharing nhưng hardware có physical sharing ở coherence granularity.

Failure ở đây không phải correctness mà là scalability:

```text
thread count tăng
→ ownership transfer/invalidation tăng
→ cache-to-cache traffic tăng
→ stalled cycles tăng
→ throughput dừng tăng hoặc giảm
```

Padding/alignment hoặc thay data layout có thể sửa vì tầng abstraction thực sự quyết định behavior là cache-line placement.

## 9. NUMA làm “memory” không còn có một latency duy nhất

Trên NUMA machine, memory page có home node; core truy cập remote memory phải đi qua interconnect. Shared cache line bị ghi qua nhiều sockets có thể tạo coherence traffic đắt hơn nhiều so với cùng socket.

Synchronization design vì thế có topology. Một global counter/lock đúng về logic có thể trở thành bottleneck vật lý do remote cache-line bouncing.

Đọc tiếp [NUMA, interconnects và scalable coherence](./04_numa_interconnects_and_scalable_coherence.md).

## 10. Lock-free không đồng nghĩa wait-free

Atomics và compare-and-swap cho phép lock-free algorithms, nhưng correctness đòi hỏi memory ordering, ABA handling, reclamation và progress proof.

Lock-free chỉ hứa system-wide progress theo định nghĩa; một thread cụ thể vẫn có thể starve. Wait-free mạnh hơn: mỗi operation hoàn tất trong bounded number of steps theo model.

Memory order càng yếu, proof burden càng lớn. Nếu chọn `relaxed` chỉ vì benchmark nhanh hơn mà chưa chứng minh invariant, optimization đang đổi correctness contract.

## 11. Performance pressure làm behavior thay đổi như thế nào?

Ordering mạnh hơn có thể hạn chế compiler/hardware reordering, serialize một số paths hoặc tăng coherence/fence cost. Ordering yếu hơn cho nhiều performance latitude hơn nhưng yêu cầu protocol tinh vi hơn.

Ngoài fence cost, contention có thể khiến atomic read-modify-write trở thành serialization point. Khi nhiều cores CAS cùng một cache line, throughput bị giới hạn bởi ownership transfer chứ không phải ALU speed.

Vì vậy performance engineering của concurrency phải đo **contention topology**, không chỉ số threads.

## 12. Production evidence

Evidence phù hợp phụ thuộc tầng:

```text
Language/runtime:
- race detector hoặc concurrency sanitizer khi ecosystem hỗ trợ
- lock/park/contention profiler
- thread dump, structured-concurrency state

OS:
- context switch, migration, run queue, scheduler delay
- CPU affinity/NUMA placement

Hardware:
- cache miss và stalled-cycle counters
- cache-to-cache transfer / HITM-like events khi CPU/tool hỗ trợ
- memory bandwidth, NUMA local/remote accesses
```

PMU event name khác theo CPU vendor/model nên không nên hard-code một counter name như universal truth. Mental model phải là: **tìm evidence cho cache-line movement, ordering/contention cost và pipeline stalls**.

## 13. Failure reasoning theo abstraction layer

Nếu symptom là wrong value/data race, bắt đầu từ language-level ownership/happens-before. Nếu symptom là correct nhưng scaling xấu, kiểm tra lock contention, cache-line sharing, NUMA placement và memory bandwidth. Nếu chỉ một architecture fail, kiểm tra code có vô tình dựa ordering mạnh của ISA cũ hay không.

Không xuống microarchitecture chỉ vì nó thú vị; xuống khi evidence cho thấy abstraction trên không đủ giải thích symptom.

## 14. Mô hình tư duy

> Coherence giữ lịch sử của một location không tự mâu thuẫn; memory-consistency model định nghĩa những cross-location observations hợp lệ; synchronization primitives tạo ordering edge mà language/runtime có thể dựa vào. Store buffer, coherence traffic và NUMA topology giải thích cost/visibility vật lý, nhưng **program correctness phải được chứng minh ở language memory model**.

## Kết nối

Nền tảng: [Cache hierarchy](../../basic/02_computer_architecture/02_memory_hierarchy_and_cache.md) và [OS concurrency](../../basic/03_operating_systems/02_concurrency_synchronization_and_deadlock.md). Đường xuyên tầng hoàn chỉnh: [CPU cache → language memory model → concurrency bug](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md). Đọc tiếp [OoO/ROB](./01_out_of_order_execution_register_renaming_and_rob.md) và [NUMA](./04_numa_interconnects_and_scalable_coherence.md).