# Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Runnable không có nghĩa đang chạy** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Per-CPU run hàng đợi (queue / 큐): giảm contention nhưng tạo bài toán cân bằng** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối scheduler với run queues, fairness và latency, để hiệu năng tiến trình được đọc qua trạng thái chờ và phân bổ CPU.

Operating-system scheduler quyết định tác vụ (task / 작업) nào được chạy trên CPU nào, trong bao lâu và khi nào bị preempt. Ở mức advanced, bài toán không phải nhớ tên scheduling thuật toán (algorithm / 알고리즘) mà là hiểu bất biến (invariant / 불변식) của một tài nguyên (resource / 자원) allocator: **CPU thời gian (time / 시간) hữu hạn phải được phân phối theo chính sách (policy / 정책) trong khi scheduler cố giữ fairness/deadline, hạn chế starvation và không phá locality nhiều hơn mức cần thiết.**

Hiệu năng (performance / 성능) pressure làm bài toán khó vì cùng một quyết định có thể tốt cho fairness nhưng xấu cho bộ nhớ đệm (cache / 캐시) locality, tốt cho thông lượng (throughput / 처리량) nhưng xấu cho wake-up độ trễ (latency / 지연 시간).

## 1. Runnable không có nghĩa đang chạy

Một tác vụ (task / 작업) có thể đang running, runnable nhưng chờ CPU, sleeping/blocked vì I/O hoặc synchronization, hoặc stopped. Scheduler chủ yếu lựa chọn trong tập **runnable tasks**.

Nếu một dịch vụ (service / 서비스) có 64 runnable threads trên 8 cores, phần lớn threads đang chờ CPU dù tiến trình (process / 프로세스) không “blocked” theo nghĩa I/O. Đây là queueing ở tầng OS:

```text
arrival of runnable work
→ per-CPU run queue
→ CPU service time
→ completion/block/preemption
```

Khi arrival pressure gần CPU dịch vụ (service / 서비스) sức chứa (capacity / 용량), scheduler delay trở thành thành phần của tail độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Runnable chỉ có nghĩa đủ điều kiện chạy; per-CPU run queues giảm contention nhưng cần load balancing, rồi fairness policy cân bằng throughput với latency theo thời gian.

## 2. Per-CPU run hàng đợi (queue / 큐): giảm contention nhưng tạo bài toán cân bằng

Một toàn cục (global / 전역) hàng đợi (queue / 큐) duy nhất trên multicore vừa tạo khóa (lock / 잠금)/contention vừa làm tác vụ (task / 작업) dễ nhảy cốt lõi (core / 핵심) và mất bộ nhớ đệm (cache / 캐시) warmth. Kernel hiện đại thường giữ scheduling trạng thái (state / 상태) theo CPU hoặc theo cấu trúc có tính cục bộ cao.

Điều này tạo sự đánh đổi (trade-off / 트레이드오프) nền tảng:

```text
keep task local  <------>  migrate task
cache/NUMA warmth          load balance/fairness
```

Nếu CPU A có hàng đợi (queue / 큐) dài còn CPU B rảnh, di chuyển (migration / 마이그레이션) có thể giảm wait. Nhưng migrate tác vụ (task / 작업) có working set lớn sang cốt lõi (core / 핵심)/socket khác có thể tăng trượt bộ nhớ đệm (cache miss / 캐시 미스) và remote NUMA truy cập (access / 접근).

Bất biến (invariant / 불변식) không phải “hàng đợi (queue / 큐) mọi CPU luôn bằng nhau”. Mục tiêu là policy-level fairness/sức chứa (capacity / 용량) mà vẫn giữ locality hợp lý.

> **Chuyển mạch:** Ở chặng này của **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **3. Fairness là chính sách (policy / 정책) theo thời gian** tiếp nhận điểm tựa từ **2. Per-CPU run hàng đợi (queue / 큐): giảm contention nhưng tạo bài toán cân bằng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Wake-up đường dẫn (path / 경로) và độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Fairness là chính sách (policy / 정책) theo thời gian

Round-robin là mô hình tư duy (mental model / 사고 모델) dễ hiểu nhưng môi trường vận hành (production / 운영 환경) scheduler thường cần weighted fairness. Linux CFS lịch sử dùng **virtual thời gian chạy (runtime / 런타임)** để biểu diễn lượng CPU dịch vụ (service / 서비스) đã nhận tương đối theo weight; hiện thực (implementation / 구현) scheduler có thể thay đổi qua kernel versions, nhưng mô hình tư duy (mental model / 사고 모델) bền hơn tên cấu trúc dữ liệu cụ thể.

Fairness cần trả lời câu hỏi: trong một cửa sổ (window / 윈도우) đủ dài, tác vụ (task / 작업) runnable liên tục nhận bao nhiêu CPU so với weight/chính sách (policy / 정책) của nó?

Fairness không đồng nghĩa độ trễ (latency / 지연 시간) tối thiểu. Một tác vụ (task / 작업) có thể nhận “phần CPU công bằng” nhưng wake-up phải chờ quá lâu đối với yêu cầu (request / 요청) latency-sensitive.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **3. Fairness là chính sách (policy / 정책) theo thời gian** xác định đầu vào; **4. Wake-up đường dẫn (path / 경로) và độ trễ (latency / 지연 시간)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. ngữ cảnh (context / 맥락) switch chi phí (cost / 비용) không chỉ là save/restore register** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Wake-up đường dẫn (path / 경로) và độ trễ (latency / 지연 시간)

Một máy chủ (server / 서버) luồng thực thi (thread / 스레드) thường:

```text
sleep/block chờ socket/futex/timer
→ event/interrupt xảy ra
→ kernel đánh thức task
→ chọn target CPU
→ enqueue runnable
→ có thể preempt task hiện tại
→ thread thật sự chạy application code
```

Thời gian từ wake-up tới thực thi (execution / 실행) là **scheduler độ trễ (latency / 지연 시간)**. Khi run hàng đợi (queue / 큐) dài hoặc CPU bị throttled, yêu cầu (request / 요청) có thể mất phần lớn độ trễ (latency / 지연 시간) ngân sách (budget / 예산) trước khi handler thực thi instruction hữu ích nào.

Đây là lower tầng (layer / 계층) thường bị che bởi ứng dụng (application / 애플리케이션) tracing nếu span chỉ bắt đầu sau khi worker được schedule.

> **Chuyển mạch:** Trong **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **4. Wake-up đường dẫn (path / 경로) và độ trễ (latency / 지연 시간)** xác định đầu vào; **5. ngữ cảnh (context / 맥락) switch chi phí (cost / 비용) không chỉ là save/restore register** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. CPU affinity và pinning là ràng buộc (constraint / 제약조건), không phải default tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. ngữ cảnh (context / 맥락) switch chi phí (cost / 비용) không chỉ là save/restore register

Direct context-switch công việc (work / 작업) gồm lưu/khôi phục architectural trạng thái (state / 상태), scheduler accounting và có thể address-space-related trạng thái (state / 상태). Nhưng indirect chi phí (cost / 비용) thường lớn hơn:

```text
cache working set bị thay
TLB locality thay đổi
branch predictor/pipeline phải warm lại
NUMA locality có thể xấu đi
```

Quantum quá nhỏ tăng responsiveness nhưng tăng switching/locality chi phí (cost / 비용). Quantum quá lớn amortize overhead tốt nhưng làm interactive/wakeup độ trễ (latency / 지연 시간) xấu.

Vì vậy “nhiều threads để tận dụng CPU” chỉ đúng tới điểm tính đồng thời (concurrency / 동시성) còn tạo useful parallelism. Sau đó scheduler và bộ nhớ đệm (cache / 캐시) interference có thể làm dịch vụ (service / 서비스) thời gian (time / 시간) tăng.

> **Chuyển mạch:** Ở chặng này của **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **6. CPU affinity và pinning là ràng buộc (constraint / 제약조건), không phải default tối ưu hóa (optimization / 최적화)** tiếp nhận điểm tựa từ **5. ngữ cảnh (context / 맥락) switch chi phí (cost / 비용) không chỉ là save/restore register** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. NUMA nối scheduler với bộ nhớ (memory / 메모리) subsystem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. CPU affinity và pinning là ràng buộc (constraint / 제약조건), không phải default tối ưu hóa (optimization / 최적화)

**CPU affinity (CPU 친화성)** giới hạn tác vụ (task / 작업) chạy trên tập CPU nhất định. Pinning có thể hữu ích cho benchmark ổn định, latency-sensitive tải công việc (workload / 워크로드), bộ nhớ đệm (cache / 캐시) locality hoặc NUMA placement.

Nhưng pinning sai tạo hotspot và ngăn scheduler dùng idle sức chứa (capacity / 용량). Nếu bộ nhớ (memory / 메모리) của tác vụ (task / 작업) nằm chủ yếu ở nút (node / 노드) khác, pinning còn có thể cố định remote-memory penalty.

Trước khi pin, cần có hypothesis và bằng chứng (evidence / 증거): di chuyển (migration / 마이그레이션) có thật sự là bottleneck hay không?

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **7. NUMA nối scheduler với bộ nhớ (memory / 메모리) subsystem** tiếp nhận điểm tựa từ **6. CPU affinity và pinning là ràng buộc (constraint / 제약조건), không phải default tối ưu hóa (optimization / 최적화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Priority inversion: scheduling và synchronization giao nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. NUMA nối scheduler với bộ nhớ (memory / 메모리) subsystem

Trên NUMA machine, “CPU balance” và “bộ nhớ (memory / 메모리) locality” có thể xung đột. tác vụ (task / 작업) chạy trên nút (node / 노드) 0 nhưng working pages ở nút (node / 노드) 1 tạo remote accesses; migrate tác vụ (task / 작업) hoặc migrate pages đều có chi phí (cost / 비용).

Vì vậy hiệu năng (performance / 성능) anomaly có thể xuất hiện như scheduler/tải (load / 로드) issue nhưng tầng dưới quyết định chi phí (cost / 비용) là interconnect + bộ nhớ (memory / 메모리) placement. Đọc cùng [NUMA và scalable coherence](../../02_computer_architecture/advanced/04_numa_interconnects_and_scalable_coherence.md).

> **Chuyển mạch:** Trong **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **8. Priority inversion: scheduling và synchronization giao nhau** tiếp nhận điểm tựa từ **7. NUMA nối scheduler với bộ nhớ (memory / 메모리) subsystem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Real-time khác với “nhanh”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Priority inversion: scheduling và synchronization giao nhau

High-priority tác vụ (task / 작업) có thể chờ khóa (lock / 잠금) do low-priority tác vụ (task / 작업) giữ. Nếu medium-priority tasks liên tục preempt low-priority holder, high-priority tác vụ (task / 작업) bị trì hoãn gián tiếp. Đây là **đảo ngược ưu tiên (priority inversion / 우선순위 역전)**.

Priority inheritance tạm nâng priority của khóa (lock / 잠금) holder để nó hoàn tất trọng yếu (critical / 중요) section. Bài học rộng hơn: scheduler chính sách (policy / 정책) không thể lập luận (reasoning / 추론) tách khỏi khóa (lock / 잠금) quyền sở hữu (ownership / 소유권) và blocking đồ thị (graph / 그래프).

Bất biến (invariant / 불변식) real-time không phải “tác vụ (task / 작업) priority cao luôn chạy”. Nó là deadline/blocking bound có thể chứng minh dưới các giả định (assumptions / 가정들) của scheduler + synchronization giao thức (protocol / 프로토콜).

> **Chuyển mạch:** Ở chặng này của **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **9. Real-time khác với “nhanh”** tiếp nhận điểm tựa từ **8. Priority inversion: scheduling và synchronization giao nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. cgroup, VM và scheduler tạo thêm tài nguyên (resource / 자원) boundaries** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Real-time khác với “nhanh”

Real-time quan tâm bounded worst-case/known độ trễ (latency / 지연 시간) hơn average speed. tác vụ (task / 작업) trung bình 1 ms nhưng đôi lúc 100 ms có thể không phù hợp deadline 10 ms, trong khi tác vụ (task / 작업) ổn định 5 ms lại phù hợp hơn.

Hard real-time đòi hỏi điều khiển (control / 제어) chặt scheduling, interrupt, bộ nhớ (memory / 메모리) allocation, locks và I/O. Soft real-time chấp nhận một số misses nhưng vẫn cần tail-bound lập luận (reasoning / 추론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **9. Real-time khác với “nhanh”** nêu điều cần giải thích; **10. cgroup, VM và scheduler tạo thêm tài nguyên (resource / 자원) boundaries** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. thất bại (failure / 실패) modes dưới hiệu năng (performance / 성능) pressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. cgroup, VM và scheduler tạo thêm tài nguyên (resource / 자원) boundaries

Trong bộ chứa (container / 컨테이너), CPU quota/weight có thể throttle tải công việc (workload / 워크로드) dù host còn idle CPU theo cách nhìn tổng quát. Trong VM, **steal thời gian (time / 시간)** cho thấy vCPU runnable nhưng hypervisor chưa cấp vật lý (physical / 물리적) CPU.

Do đó bất biến (invariant / 불변식) “dịch vụ (service / 서비스) có 4 vCPU” không đồng nghĩa bốn cores luôn available. sức chứa (capacity / 용량) thực tế phụ thuộc scheduler ở nhiều tầng:

```text
application workers
→ guest/container scheduler boundary
→ host scheduler
→ physical CPU
```

> **Chuyển mạch:** Trong **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **10. cgroup, VM và scheduler tạo thêm tài nguyên (resource / 자원) boundaries** nêu điều cần giải thích; **11. thất bại (failure / 실패) modes dưới hiệu năng (performance / 성능) pressure** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. bằng chứng vận hành (production evidence / 운영 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. thất bại (failure / 실패) modes dưới hiệu năng (performance / 성능) pressure

Scheduler hiếm khi “crash” ứng dụng (application / 애플리케이션) theo nghĩa lô-gic (logic / 논리), nhưng pressure có thể tạo hành vi khi thất bại (failure behavior / 실패 동작) cấp hệ thống:

```text
run queue dài → wake-up latency tăng → timeout
threads quá nhiều → context-switch/cache interference → service time tăng
CPU throttle → queue tăng dù host utilization nhìn chưa đầy
priority inversion → deadline miss
bad affinity → hotspot + remote NUMA access
```

Các thất bại (failure / 실패) này thường phản hồi (feedback / 피드백) sang thử lại (retry / 재시도)/overload ở tầng ứng dụng (application / 애플리케이션).

> **Chuyển mạch:** Ở chặng này của **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **11. thất bại (failure / 실패) modes dưới hiệu năng (performance / 성능) pressure** nêu điều cần giải thích; **12. bằng chứng vận hành (production evidence / 운영 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **13. liên kết (connection / 연결) với queueing/backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. bằng chứng vận hành (production evidence / 운영 증거)

CPU utilization một mình không đủ. Khi điều tra scheduler pressure, cần kết hợp:

```text
per-CPU utilization và runnable queue
voluntary/involuntary context switches
scheduler/run-queue latency
CPU migrations và affinity
cgroup throttled time/quota pressure
VM steal time nếu có
NUMA local/remote memory evidence
on-CPU vs off-CPU profile
```

Linux có nhiều facility như scheduler tracepoints, `perf`, pressure metrics và eBPF-based tooling; tên công cụ (tool / 도구) có thể thay nhưng bằng chứng (evidence / 증거) mô hình (model / 모델) không đổi: **tác vụ (task / 작업) runnable từ lúc nào, thật sự chạy lúc nào, bị preempt/khối (block / 블록) bởi gì, trên CPU/nút (node / 노드) nào**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **12. bằng chứng vận hành (production evidence / 운영 증거)** nêu điều cần giải thích; **13. liên kết (connection / 연결) với queueing/backpressure** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **14. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. liên kết (connection / 연결) với queueing/backpressure

Run hàng đợi (queue / 큐) là một hàng đợi (queue / 큐) giống nhiều hàng đợi (queue / 큐) khác trong hệ thống (system / 시스템). Nếu ứng dụng (application / 애플리케이션) tiếp tục accept công việc (work / 작업) trong khi CPU already saturated, hàng đợi (queue / 큐) debt tăng rồi deadline hết hạn. Admission điều khiển (control / 제어) ở tầng ứng dụng (application / 애플리케이션) có thể bảo vệ scheduler khỏi phải giữ quá nhiều runnable công việc (work / 작업).

Đây là lý do tính đồng thời (concurrency / 동시성) limit thường tốt hơn “spawn thêm threads khi chậm”. Đọc [Queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

> **Chuyển mạch:** Trong **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **14. Mô hình tư duy** gom các mảnh từ **13. liên kết (connection / 연결) với queueing/backpressure** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Mô hình tư duy

> Scheduler là tài nguyên (resource / 자원) allocator theo thời gian trên topology CPU/NUMA. **Run hàng đợi (queue / 큐) biểu diễn demand chưa được CPU phục vụ; chính sách (policy / 정책) quyết định fairness/priority; preemption/di chuyển (migration / 마이그레이션) đổi độ trễ (latency / 지연 시간) và locality; bằng chứng vận hành (production evidence / 운영 증거) phải tách useful CPU công việc (work / 작업) khỏi queueing, throttling và interference.** Khi pressure tăng, scheduler hành vi (behavior / 동작) trở thành một phần của end-to-end độ trễ (latency / 지연 시간) chứ không còn là chi tiết “bên dưới OS”.

> **Chuyển mạch:** Ở chặng này của **Scheduler internals, run hàng đợi (queue / 큐) và fairness/độ trễ (latency / 지연 시간) trade-offs**, **Kết nối** gom các mảnh từ **14. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc tiếp [Page faults, reclaim và memory pressure](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md), [NUMA architecture](../../02_computer_architecture/advanced/04_numa_interconnects_and_scalable_coherence.md), [End-to-end request latency](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) và [Debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

> **Bàn giao:** Giữ lại distinction giữa runnable, actually running, throttled và blocked trước khi diễn giải latency. Sang [Page faults, reclaim và memory pressure](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md) khi scheduler delay gắn với reclaim/I/O; quay về [README](./README.md) để xác nhận owner của OS advanced.
