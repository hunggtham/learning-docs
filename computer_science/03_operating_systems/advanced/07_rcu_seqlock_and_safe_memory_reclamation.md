# RCU, seqlock và safe memory reclamation

Đọc trước [Kernel execution contexts, synchronization và syscall path](./00_kernel_execution_contexts_and_syscall_path.md) để có mental model về process context, interrupt context, blocking, spinlock và object lifetime. Chapter này đi sâu vào một lớp bài toán riêng: **làm thế nào cho rất nhiều reader truy cập shared state với chi phí thấp mà writer vẫn có thể thay đổi hoặc thu hồi object an toàn**.

Nếu chỉ nghĩ synchronization là “khóa trước khi đọc/ghi”, ta sẽ bỏ lỡ vấn đề khó hơn: một pointer có thể đã được reader lấy ra đúng lúc writer xóa object khỏi structure. Xóa khỏi index không đồng nghĩa object có thể được `free` ngay. Vì vậy invariant trung tâm của chapter là:

> Một object chỉ được reclaim khi không còn execution context hợp lệ nào có thể dereference phiên bản cũ của nó.

Mental model xuyên suốt:

```text
publish
→ reader obtains reference
→ writer replaces/removes logical state
→ old readers may still exist
→ grace/reclamation protocol proves safety
→ physical memory can be reused
```

## 1. Mutual exclusion và lifetime safety là hai bài toán khác nhau

Mutex hoặc spinlock có thể bảo đảm hai writer không sửa cùng state đồng thời. Nhưng lock không tự động giải lifetime nếu reference sống lâu hơn critical section hoặc reader path cố ý không giữ writer lock.

Ví dụ một lookup trả về pointer `p`. Sau khi lookup hoàn tất, writer xóa `p` khỏi tree và `free(p)`. Nếu reader vẫn dùng `p`, correctness đã hỏng dù thao tác remove được bảo vệ bằng lock hoàn hảo.

Do đó cần phân biệt:

```text
state synchronization
≠
object lifetime management
```

Nhiều kernel structure, runtime table, routing table và read-mostly registry tối ưu reader bằng cách tách hai vấn đề này.

## 2. RCU là publication + grace period + deferred reclamation

Read-Copy-Update (RCU) là family technique trong đó reader thường không serialize với nhau. Writer chuẩn bị state mới, publish nó, rồi hoãn reclaim state cũ.

Một update điển hình có dạng:

```text
old = current
new = copy_or_new_version(old)
mutate(new)
publish(new)
wait_until_preexisting_readers_are_gone()
reclaim(old)
```

Từ “copy” không bắt buộc toàn bộ structure phải được clone. Nhiều implementation chỉ allocate node mới, relink một số pointer rồi retire node cũ. Bản chất là **reader có thể tiếp tục nhìn một version hợp lệ trong lúc writer tạo version kế tiếp**.

## 3. Grace period là điều kiện logic, không phải timeout

Grace period không có nghĩa “đợi 10 ms cho chắc”. Nó chứng minh rằng mọi reader có khả năng giữ reference từ trước publication đã đi qua một trạng thái mà protocol coi là quiescent.

Tùy implementation, quiescent state có thể liên quan đến context switch, rời read-side critical section, user/kernel transition hoặc một epoch progression. Điều quan trọng là proof về lifetime, không phải số milliseconds.

Nếu một CPU hoặc task giữ read-side section quá lâu, writer có thể publish state mới thành công nhưng memory cũ chưa được thu hồi. Khi đó latency reader vẫn tốt nhưng reclamation backlog tăng. Pressure chuyển từ lock contention sang memory retention.

## 4. Publication đúng còn phụ thuộc memory ordering

Writer không được publish pointer tới object mới trước khi fields của object được khởi tạo theo visibility contract. Nếu compiler hoặc CPU reordering làm reader thấy pointer mới nhưng state bên trong chưa visible đúng, RCU vẫn sai.

Correctness path là:

```text
initialize object
→ release/publication ordering
→ pointer becomes reachable
→ acquire/dependency semantics on reader side
→ object state becomes valid to observe
```

Vì vậy RCU không “đứng trên” memory model. Nó dựa vào language/compiler primitive và ISA ordering. Đọc thêm [memory consistency, cache coherence và ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md) và [correctness path xuyên tầng](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md).

## 5. Writer không được nhầm logical removal với physical reclamation

Khi writer unlink node khỏi list/tree/hash table, node đã biến mất khỏi **future lookup** nhưng vẫn có thể được **past reader** giữ reference.

Ta có ba thời điểm khác nhau:

```text
T1: object reachable
T2: object no longer reachable by new readers
T3: object safe to reclaim
```

`T2` và `T3` không giống nhau. Phần lớn bug use-after-free trong lock-free/read-mostly design xuất hiện khi implementation coi hai mốc này là một.

## 6. RCU callback biến reclaim thành asynchronous debt

Thay vì writer chờ đồng bộ grace period, hệ thống có thể enqueue callback để reclaim sau. Điều này giảm latency của update foreground nhưng tạo một queue hậu cảnh.

Khi update rate tăng hoặc readers giữ critical section lâu, callback queue có thể phình ra:

```text
update rate ↑
→ retired objects ↑
→ pending callbacks ↑
→ unreclaimed memory ↑
→ memory pressure / cache pressure ↑
```

Đây là phase change quan trọng. Một design rất tốt ở read-heavy steady state có thể trở nên nguy hiểm trong update storm.

## 7. Seqlock tối ưu một loại snapshot khác

Sequence lock (seqlock) phù hợp khi state nhỏ, writer cập nhật tương đối nhanh và reader có thể retry.

Writer tăng sequence counter sang trạng thái “đang ghi”, cập nhật fields rồi publish sequence mới. Reader làm:

```text
v1 = sequence
read snapshot fields
v2 = sequence
accept only if v1 == v2 and version means no writer overlap
otherwise retry
```

Invariant của seqlock không phải lifetime của object cũ mà là:

> Reader chỉ chấp nhận snapshot nếu không có writer làm thay đổi state trong khoảng đọc.

Seqlock tránh reader lock nhưng không bảo đảm reader hoàn tất nhanh khi writer liên tục. Write-heavy pressure có thể biến optimistic read thành retry storm.

## 8. Seqlock không phù hợp với pointer có lifetime phức tạp

Nếu snapshot chứa pointer tới object mà writer có thể free, việc sequence validation sau cùng có thể quá muộn: reader có thể đã dereference memory invalid trong lúc copy.

Vì vậy seqlock thường an toàn nhất với data có thể copy trực tiếp và lifetime ổn định trong protocol. Khi state chứa object graph phức tạp, cần kết hợp lifetime mechanism khác.

Điều này cho thấy “lock-free reader” không phải một category đồng nhất. Cần hỏi chính xác invariant nào đang được bảo vệ.

## 9. Epoch-based reclamation và hazard pointer giải cùng family problem bằng proof khác

RCU không phải kỹ thuật duy nhất. **Epoch-based reclamation** cho reader tham gia epoch; object retired ở epoch cũ chỉ được reclaim sau khi tất cả participant có thể giữ reference cũ đã tiến qua epoch an toàn.

**Hazard pointer** đi theo hướng khác: reader công bố pointer mà nó đang dùng; reclaimer không được free object còn xuất hiện trong hazard set.

Mental model:

```text
RCU / epoch:
prove old readers are gone

hazard pointer:
prove this object is not currently protected by any reader
```

Mỗi cách có chi phí metadata, scanning, memory ordering và stall behavior khác nhau. Không có lựa chọn universal.

## 10. ABA cho thấy CAS success chưa chắc state “vẫn như cũ”

Trong lock-free algorithm, thread có thể đọc pointer/value `A`, bị pause, trong lúc thread khác đổi `A → B → A`. Khi thread đầu dùng compare-and-swap, giá trị bề ngoài vẫn là `A` nên CAS có thể thành công dù object identity/lifetime đã thay đổi.

Đó là ABA problem. Tag/version counter, hazard pointer, epoch reclamation hoặc object identity discipline có thể cần thiết tùy structure.

Điểm cần nhớ: atomicity của một instruction không chứng minh semantic continuity của object.

## 11. Preemption và scheduler có thể trở thành một phần của reclamation proof

Nếu grace-period detection dựa vào quiescent states, một task bị preempt hoặc CPU không report progress có thể trì hoãn reclamation. Do đó scheduler behavior và RCU progress không hoàn toàn độc lập.

Trong production, symptom có thể là memory tăng dù allocation rate business không tăng tương ứng. Nguyên nhân thực sự có thể là reader stall hoặc callback backlog, không phải “memory leak” theo nghĩa object bị mất reference vĩnh viễn.

## 12. NUMA và cache coherence vẫn quyết định cost

Reader path nhẹ không có nghĩa miễn phí. Shared sequence counters, global epoch state hoặc callback metadata vẫn có cache-line traffic. Với nhiều sockets/NUMA nodes, location của shared metadata và frequency cập nhật có thể trở thành bottleneck.

Một design scale tốt thường cố gắng:

```text
reader-local fast path
+ batched/global coordination hiếm hơn
+ amortized reclamation work
```

Nếu mọi read đều update một global cache line, ta đã vô tình tái tạo contention ở dạng khác.

## 13. Failure modes đặc trưng

Use-after-free xuất hiện khi reclaim quá sớm. Memory retention xuất hiện khi grace period không hoàn tất hoặc reader quên exit protocol. Retry starvation xuất hiện với seqlock khi writer quá thường xuyên. ABA xuất hiện khi identity bị tái sử dụng mà version/protection không đủ. Publication bug xuất hiện khi memory ordering không đúng.

Đây là lý do cần mô tả failure theo invariant thay vì chỉ nhớ API.

## 14. Production evidence cần phân biệt contention với reclamation debt

Khi throughput giảm hoặc memory tăng, các tín hiệu hữu ích gồm reader critical-section duration, grace-period latency, số callback/retires pending, memory chưa reclaim, writer update rate, seqlock retry count, CPU spinning, cache-to-cache transfer, scheduler stall và NUMA locality.

Một causal chain thường có dạng:

```text
reader stall
→ grace period kéo dài
→ retired objects tích tụ
→ memory pressure tăng
→ reclaim/page fault/cache miss tăng
→ latency application tăng
```

Nếu chỉ nhìn heap/RSS cuối chain, dễ chẩn đoán sai thành allocator leak.

## 15. Worked example: read-mostly routing table

Giả sử dataplane lookup routing entry cho mỗi packet, trong khi control plane update route ít hơn nhiều. Nếu reader phải lấy global mutex cho mỗi lookup, throughput chịu lock/cache-line pressure.

Một versioned publication design cho phép writer tạo entry mới và atomically thay pointer. Packet đang dùng old entry vẫn hoàn tất; entry cũ chỉ reclaim sau khi read-side users cũ đã rời critical section.

Khi route churn tăng đột biến, lợi ích reader vẫn còn nhưng retired-entry backlog có thể tăng. Đây là lúc production evidence phải đo cả update rate và grace/reclaim progress.

## 16. Khi nào không nên dùng RCU hoặc seqlock?

Nếu workload write-heavy, invariant cần atomic update trên object graph lớn, reader không thể retry, hoặc team không đủ tooling để chứng minh lifetime/order correctness, mutex/RW-lock đơn giản có thể tốt hơn.

Senior engineering không phải chọn primitive “nhanh nhất”; là chọn proof dễ duy trì nhất trong workload và failure model thực tế.

## 17. Kết nối sang các chapter khác

RCU/seqlock nối trực tiếp với [kernel execution context](./00_kernel_execution_contexts_and_syscall_path.md), [scheduler](./01_scheduler_run_queues_fairness_and_latency.md), [memory ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md), [ownership và memory safety](../../04_programming_languages/advanced/02_ownership_borrowing_linear_types_and_memory_safety.md) và [whole-system debugging](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

Điểm cuối cùng cần giữ là: **reader speed chỉ an toàn khi publication, ordering và reclamation cùng tạo thành một proof hoàn chỉnh về object lifetime.**