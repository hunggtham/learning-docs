# Memory consistency, cache coherence và ordering

Trong single-thread code, ta thường hình dung read/write xảy ra theo đúng thứ tự source. Trên multicore hiện đại, compiler, CPU pipeline, store buffer, invalidate queue, cache hierarchy và interconnect đều được phép trì hoãn hoặc sắp xếp lại một số memory operations để che latency. Vì vậy concurrency correctness không thể reasoning bằng trực giác “dòng nào viết trước”.

Chương này giữ một invariant xuyên nhiều tầng: **cache coherence giữ lịch sử hợp lệ của từng location; ISA memory-consistency model giới hạn những quan sát cross-location phần cứng được phép tạo ra; language memory model định nghĩa contract mà source code có quyền dựa vào; synchronization primitives tạo ordering edges đủ để chứng minh invariant của chương trình.**

## 1. Bài toán ban đầu: performance cần tự do, software cần một hợp đồng

Nếu mỗi store phải chờ mọi core khác quan sát được giá trị mới trước khi core hiện tại chạy tiếp, CPU sẽ lãng phí rất nhiều cycle. Hardware vì thế dùng store buffer, speculative execution, out-of-order execution và nhiều outstanding memory requests để tiếp tục làm việc khi coherence traffic hoặc DRAM access còn đang chờ.

Software lại cần các property như:

```text
release lock xong
→ thread acquire cùng lock phải thấy state được bảo vệ

publish payload xong bằng release
→ reader acquire publication flag phải được phép dùng payload
```

Thiết kế memory model là một thỏa hiệp: cho compiler/hardware đủ freedom để tối ưu nhưng vẫn cung cấp primitive đủ mạnh để software chứng minh correctness.

## 2. Coherence và consistency trả lời hai câu hỏi khác nhau

**Nhất quán cache (cache coherence / 캐시 일관성)** chủ yếu hỏi: với **một memory location**, các cores có quan sát writes theo một lịch sử tương thích hay không? Protocol kiểu MESI/MOESI quản lý ownership/state của cache lines để nhiều cache không tự do ghi các phiên bản mâu thuẫn.

**Mô hình nhất quán bộ nhớ (memory consistency model / 메모리 일관성 모델)** hỏi rộng hơn: với nhiều locations và nhiều processors, những ordering nào của reads/writes được phép quan sát?

Sequential consistency là model trực quan: kết quả như thể mọi memory operations của mọi threads được xen kẽ trong một global order trong khi mỗi thread giữ program order. Hardware thực tế thường cho phép model yếu hơn để đạt performance tốt hơn.

Điểm phải giữ: **coherence của từng location không tự tạo cross-location ordering**. `payload` và `ready` có thể đều coherent nhưng reader không được suy luận `ready == true` kéo theo payload đã visible nếu protocol thiếu synchronization contract.

## 3. Store buffer giải thích vì sao store chưa chắc visible ngay

Khi core thực hiện store, nó có thể đặt write vào store buffer rồi tiếp tục thay vì chờ ownership/cache propagation hoàn tất. Core đó thường forward được value từ buffer cho chính nó, nhưng core khác chưa chắc thấy write ngay.

Xét litmus test Store Buffering:

```text
Initially x = 0, y = 0

Thread A:        Thread B:
x = 1           y = 1
r1 = y           r2 = x
```

Trực giác sequential dễ cho rằng `r1 = 0 && r2 = 0` “không thể”. Nhưng trên model cho phép store→load reordering hoặc delayed visibility, outcome này có thể hợp lệ khi không có synchronization phù hợp.

Litmus test không phải mẹo phỏng vấn. Nó là cách cô lập contract: đưa một execution rất nhỏ, liệt kê outcome nào model cho phép, rồi so sánh language → compiler → ISA. Nếu một outcome bị cấm ở language level thì compiler/runtime phải phát machine code đủ mạnh để cấm nó trên target ISA.

## 4. Message-passing test: publication cần một ordering edge

Xét:

```text
Writer:                 Reader:
payload = 42            if (ready) {
ready = true                use(payload)
                        }
```

Invariant mong muốn là: **nếu reader quan sát publication event `ready`, nó phải quan sát initialization của `payload` tương ứng**.

Plain stores/loads không nhất thiết tạo invariant này. Một protocol đúng thường biểu diễn publication bằng release-store và observation bằng acquire-load, hoặc dùng lock/monitor/primitive có semantics tương đương ở language level.

Điểm quan trọng là không hỏi “CPU có reorder hai instruction này không?” trước. Hãy hỏi **source-level protocol có happens-before edge không?** Nếu không, việc code “chạy đúng trên máy tôi” không tạo guarantee.

## 5. Invalidate queue và visibility không phải một sự kiện toàn cục tức thì

Coherence request đi qua interconnect, directories và queues. Một core có thể nhận invalidation/ownership traffic ở thời điểm khác core khác, miễn hành vi cuối vẫn nằm trong ISA memory model.

Vì vậy câu “write đã tới L1 nên mọi core phải thấy ngay” không phải reasoning hợp lệ. Software không có contract trực tiếp với thời điểm nội bộ của coherence messages; software có contract với ordering primitives của ISA và language memory model.

Tương tự, “cache coherent” không nghĩa “tất cả cores có cùng snapshot tại cùng nanosecond”. Coherence là protocol về thứ tự/ownership, không phải barrier toàn hệ thống sau mọi store.

## 6. Fence không phải lệnh “flush toàn bộ cache”

Memory fence áp ordering constraints lên classes memory operations theo semantics của ISA. Acquire thường ngăn operations sau acquire vượt qua synchronization point theo contract cần thiết; release giữ effects trước release không bị đẩy qua publication point theo cách phá protocol; full fence mạnh hơn và thường hạn chế optimization nhiều hơn.

Reasoning đúng phải bắt đầu bằng:

```text
operation A phải precede operation B trong quan sát nào?
writer và reader liên hệ qua primitive nào?
ordering tối thiểu nào đủ để giữ invariant?
```

Dùng fence “cho chắc” có thể che protocol yếu và tạo cost không cần thiết. Dùng fence quá yếu có thể giữ benchmark nhanh nhưng làm proof sai.

## 7. Compiler reordering và CPU reordering là hai tầng khác nhau

Compiler có thể hoist/sink load-store, giữ value trong register, eliminate redundant access hoặc transform control flow nếu language specification cho phép. CPU lại có freedom riêng theo ISA memory model.

Do đó cùng một source-level acquire/release có thể compile thành machine sequence khác nhau trên x86-64 và ARM64. Một ISA có baseline ordering mạnh hơn có thể cần ít explicit fence hơn; ISA yếu hơn có thể cần instruction/order primitive rõ hơn.

Invariant cần giữ không phải “assembly trên mọi CPU phải giống nhau”, mà là:

> Machine code trên mỗi target phải thực hiện cùng contract mà language memory model đã hứa.

Đây là lý do code tự chế dựa vào behavior accidental của một architecture có thể fail sau khi port, đổi compiler hoặc bật optimization khác.

## 8. Happens-before là abstraction software nên dùng

Ở application/runtime layer, ta hiếm khi reasoning trực tiếp bằng MESI states. Ta dùng **xảy-ra-trước (happens-before)**: program order, synchronization edges và transitivity tạo ra visibility/order guarantees hợp lệ.

```text
write data
   ↓ program order
release / unlock
   ↓ synchronization edge
acquire / lock
   ↓ program order
read data
```

“Xảy ra sớm hơn theo wall clock” không đồng nghĩa happens-before. Một write có thể vật lý xảy ra trước nhưng reader vẫn không có quyền suy luận visibility nếu thiếu synchronization edge.

Lower layer giải thích vì sao stale/reordered observation có thể xuất hiện; language model quyết định chương trình **được phép dựa vào điều gì**.

## 9. Atomicity, visibility và ordering phải được tách riêng

Một atomic load/store bảo vệ một loại property, nhưng protocol có thể còn cần ordering. Một fence tạo ordering nhưng không tự biến chuỗi read→modify→write thành atomic transaction.

Khi review code, tách ba câu hỏi:

```text
Atomicity   : operation có thể bị interleave thành lost update không?
Visibility  : write nào reader được bảo đảm nhìn thấy?
Ordering    : reader được phép suy luận operation nào đứng trước/sau?
```

Rất nhiều bug xuất phát từ việc lấy primitive giải một câu hỏi rồi giả định hai câu còn lại cũng được giải tự động.

## 10. Atomic RMW tạo serialization point vật lý

Compare-and-swap, fetch-add và các atomic read-modify-write thường cần exclusive ownership của cache line. Khi nhiều cores cùng cập nhật một global counter, correctness có thể hoàn hảo nhưng cache line phải ping-pong qua interconnect.

Causal path:

```text
threads tăng
→ nhiều RMW cùng một line
→ ownership transfer/invalidation tăng
→ retries hoặc serialization tăng
→ stalled cycles tăng
→ throughput dừng tăng hoặc giảm
```

Ở đây lower abstraction thực sự quyết định scalability là **coherence granularity + topology**, không phải ALU speed. Sharded/per-core counters, batching hoặc partitioned ownership có thể tốt hơn một atomic global counter tùy invariant.

## 11. False sharing: logic độc lập nhưng vật lý vẫn tranh một cache line

Hai threads sửa hai fields khác nhau nhưng nằm cùng cache line có thể làm line ping-pong giữa cores. Đây là **chia sẻ giả (false sharing)**: source không có logical sharing nhưng hardware có physical sharing ở coherence granularity.

Padding/alignment hoặc thay data layout có thể sửa vì abstraction quyết định behavior là cache-line placement. Đây cũng là lời nhắc rằng performance bug có thể nằm dưới abstraction mà correctness hoàn toàn đúng.

## 12. Lock-free không đồng nghĩa “không còn lifetime problem”

CAS cho phép xây lock-free structure, nhưng proof phải bao gồm linearization point, memory ordering, ABA, object lifetime và reclamation.

ABA minh họa leaky abstraction:

```text
thread A đọc pointer P
thread B remove P, free/reuse memory, rồi một pointer có cùng bit pattern P xuất hiện lại
thread A CAS thấy bit pattern vẫn giống
```

CAS chỉ so sánh value theo contract của nó; nó không chứng minh object identity/lifetime vẫn là object cũ. Hazard pointer, epoch-based reclamation, reference counting hoặc tagged/versioned pointer là các family giải pháp khác nhau vì chúng bổ sung **lifetime invariant** mà atomic primitive đơn lẻ không cung cấp.

Lock-free chỉ hứa system-wide progress theo định nghĩa; một thread cụ thể vẫn có thể starve. Wait-free mạnh hơn nhưng proof burden cũng cao hơn.

## 13. NUMA làm “memory” không còn có một latency duy nhất

Trên NUMA machine, page có home node; core truy cập remote memory phải đi qua interconnect. Shared cache line bị ghi xuyên socket có thể đắt hơn nhiều so với cùng socket.

Một global lock/counter đúng về logic có thể trở thành bottleneck vật lý do remote cache-line bouncing. Thread placement, page placement và ownership topology vì vậy thuộc performance reasoning của concurrency.

Đọc tiếp [NUMA, interconnects và scalable coherence](./04_numa_interconnects_and_scalable_coherence.md).

## 14. Performance pressure làm behavior thay đổi theo phase

Ở low contention, một atomic hoặc mutex có thể gần như miễn phí so với business work. Khi contention tăng, cost không còn tuyến tính vì ownership transfer, spinning, parking/unparking, scheduler interaction và cache miss bắt đầu dominate.

Ordering mạnh hơn có thể hạn chế compiler/hardware reordering; ordering yếu hơn cho nhiều performance latitude nhưng tăng proof burden. Optimization đúng phải giữ invariant và đo workload thật, không chọn `relaxed` chỉ vì microbenchmark ngắn hơn.

## 15. Vì sao bug có thể “chỉ xảy ra trên ARM” hoặc “chỉ khi tải cao”?

Hai trường hợp cần tách:

```text
Architecture-sensitive correctness:
program vô tình dựa vào ordering mạnh hơn của platform cũ
→ target ISA/compiler mới lộ execution vốn đã không được language guarantee

Load-sensitive correctness/performance:
contention/interleaving window mở rộng
→ race xuất hiện thường hơn hoặc coherence bottleneck tăng mạnh
```

Không nên kết luận “ARM có bug” hay “CPU quá tải làm sai dữ liệu”. Hãy kiểm tra contract source-level trước, rồi dùng ISA/microarchitecture để giải thích tại sao symptom lộ ở môi trường đó.

## 16. Production evidence: chọn evidence theo tầng

Ở language/runtime layer, tìm race detector hoặc concurrency sanitizer khi ecosystem hỗ trợ, lock/park/contention profile, thread/task dump và stress test có invariant check.

Ở OS layer, quan sát run queue, context switch, CPU migration, off-CPU wait, affinity và NUMA placement.

Ở hardware layer, dùng performance counters phù hợp CPU/tool để tìm cache miss, cache-to-cache transfer, stalled cycles, memory bandwidth và local/remote NUMA access. PMU event names khác theo vendor/model; mental model là tìm evidence cho **cache-line movement + ordering/contention cost + pipeline stalls**, không học thuộc một counter name.

Evidence không thay proof. PMU cho biết line đang ping-pong nhưng không chứng minh happens-before; race detector có thể bỏ sót execution. Correctness cần kết hợp:

```text
invariant/proof
+
reproducible stress/litmus execution
+
runtime/OS/hardware evidence
```

## 17. Failure reasoning theo abstraction layer

Nếu symptom là wrong value/data race, bắt đầu từ language-level ownership và happens-before. Nếu program đúng nhưng scaling xấu, kiểm tra lock/RMW contention, false sharing, NUMA placement và bandwidth. Nếu chỉ một architecture fail, kiểm tra code có dựa vào accidental ISA property hay undefined/data-race behavior không.

Không xuống microarchitecture chỉ vì nó thú vị; xuống khi evidence cho thấy abstraction trên không đủ giải thích symptom.

## 18. Mô hình tư duy

> Coherence giữ lịch sử của một location không tự mâu thuẫn; ISA memory model giới hạn những observation phần cứng được phép; language memory model biến chúng thành contract source-level; synchronization tạo happens-before; cache-line ownership và NUMA quyết định nhiều cost vật lý. **Program correctness phải được chứng minh ở abstraction sở hữu invariant, còn lower layer giải thích vì sao bug hoặc bottleneck có thể xuất hiện.**

## Kết nối

Nền tảng: [Cache hierarchy](../../basic/02_computer_architecture/02_memory_hierarchy_and_cache.md), [OS concurrency](../../basic/03_operating_systems/02_concurrency_synchronization_and_deadlock.md) và [Programming Languages concurrency](../../basic/04_programming_languages/08_concurrency_models_and_memory_safety.md). Đường xuyên tầng hoàn chỉnh: [CPU cache → language memory model → concurrency bug](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md). Đọc tiếp [OoO/ROB](./01_out_of_order_execution_register_renaming_and_rob.md), [NUMA](./04_numa_interconnects_and_scalable_coherence.md) và [Runtime concurrency](../../04_programming_languages/advanced/07_coroutines_continuations_async_runtimes_and_structured_concurrency.md).