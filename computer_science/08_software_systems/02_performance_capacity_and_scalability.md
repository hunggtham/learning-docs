# Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), sức chứa (capacity / 용량) và scalability

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Latency, throughput, capacity và scalability**. Route đi từ latency/throughput → utilization/saturation/queueing → Little’s Law/bottleneck → vertical-horizontal scaling → cache, batching, pools và load balancing, để capacity được đo theo workload thực.

Hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링) không phải “làm mã (code / 코드) nhanh” chung chung. Hệ thống có độ trễ (latency / 지연 시간) phân phối (distribution / 분포), thông lượng (throughput / 처리량), tài nguyên (resource / 자원) utilization, queueing và tải công việc (workload / 워크로드) shape. tối ưu hóa (optimization / 최적화) đúng phải xác định bottleneck theo measurements và mô hình (model / 모델).

## Độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량)

Độ trễ (latency / 지연 시간) = thời gian (time / 시간) một thao tác (operation / 연산)/yêu cầu (request / 요청) hoàn thành. thông lượng (throughput / 처리량) = operations per đơn vị (unit / 단위) thời gian (time / 시간). Chúng liên quan nhưng không identical: batching có thể tăng thông lượng (throughput / 처리량) nhưng tăng individual wait; low độ trễ (latency / 지연 시간) one yêu cầu (request / 요청) không chứng minh high thông lượng (throughput / 처리량) under tải (load / 로드).

Report averages alone hides tail. p95/p99 độ trễ (latency / 지연 시간) matter because phân tán (distributed / 분산) yêu cầu (request / 요청) fan-out can be dominated by slowest phụ thuộc (dependency / 의존성).

> **Chuyển mạch:** Latency/throughput đo output; utilization, saturation và queueing giải thích bottleneck, rồi Little’s Law liên hệ concurrency, throughput và latency bằng một invariant kiểm chứng được.

## Utilization, saturation và queueing

Khi arrival tỷ lệ (rate / 비율) gần dịch vụ (service / 서비스) sức chứa (capacity / 용량), hàng đợi (queue / 큐) grows và độ trễ (latency / 지연 시간) tăng nonlinearly. Simple M/M/1 intuition gives utilization `ρ=λ/μ`; expected hàng đợi (queue / 큐) delay blows up as ρ→1. Real workloads not M/M/1, but principle remains: running permanent 100% sức chứa (capacity / 용량) leaves no burst headroom.

Saturation tín hiệu (signal / 신호) can be CPU run hàng đợi (queue / 큐), disk hàng đợi (queue / 큐), liên kết (connection / 연결) pool wait, luồng thực thi (thread / 스레드) pool hàng đợi (queue / 큐) or GC pressure.

> **Chuyển mạch:** Ở chặng này của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), sức chứa (capacity / 용량) và scalability**, **Little's Law** tiếp nhận điểm tựa từ **Utilization, saturation và queueing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bottleneck** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Little's Law

For stable hệ thống (system / 시스템):

\[
L = \lambda W
\]

Average in-flight L = thông lượng (throughput / 처리량)/arrival tỷ lệ (rate / 비율) λ × average thời gian (time / 시간) W. If dịch vụ (service / 서비스) handles 1000 req/s and average độ trễ (latency / 지연 시간) 0.2 s, roughly 200 requests in hệ thống (system / 시스템) on average.

This connects tính đồng thời (concurrency / 동시성) limits to độ trễ (latency / 지연 시간)/thông lượng (throughput / 처리량) quantitatively.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), sức chứa (capacity / 용량) và scalability**, **Bottleneck** tiếp nhận điểm tựa từ **Little's Law** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vertical vs horizontal scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bottleneck

End-to-end thông lượng (throughput / 처리량) limited by constrained tài nguyên (resource / 자원)/stage. Speeding non-bottleneck gives little hệ thống (system / 시스템) gain. Profiling, tracing and tài nguyên (resource / 자원) metrics identify where thời gian (time / 시간)/sức chứa (capacity / 용량) spent.

Amdahl's Law similarly limits tối ưu hóa (optimization / 최적화) speedup by fraction improved.

> **Chuyển mạch:** Trong **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), sức chứa (capacity / 용량) và scalability**, **Vertical vs horizontal scaling** tiếp nhận điểm tựa từ **Bottleneck** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Caching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vertical vs horizontal scaling

Quy mô (scale / 규모) up adds CPU/RAM/faster thiết bị (device / 장치) to one machine. quy mô (scale / 규모) out adds nodes. Horizontal scaling requires partitionable tải công việc (workload / 워크로드)/trạng thái (state / 상태) management, tải (load / 로드) balancing and phân tán (distributed / 분산) coordination; it is not automatic.

Stateless yêu cầu (request / 요청) processing scales easier, but persistent trạng thái (state / 상태) still lives somewhere and can bottleneck DB/bộ nhớ đệm (cache / 캐시)/mạng (network / 네트워크).

> **Chuyển mạch:** Ở chặng này của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), sức chứa (capacity / 용량) và scalability**, **Caching** tiếp nhận điểm tựa từ **Vertical vs horizontal scaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Batching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Caching

Bộ nhớ đệm (cache / 캐시) stores expensive kết quả (result / 결과)/dữ liệu (data / 데이터) closer to use. Hit ratio, miss penalty, eviction, freshness và vô hiệu hóa (invalidation / 무효화) determine giá trị (value / 값).

Cache-aside loads on miss; write-through/write-back alter consistency. TTL bounds staleness but doesn't guarantee vô hiệu hóa (invalidation / 무효화) exactly when nguồn (source / 소스) changes.

Bộ nhớ đệm (cache / 캐시) stampede occurs many clients miss same hot key and recompute simultaneously; single-flight/locking/jittered expiry mitigate.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), sức chứa (capacity / 용량) và scalability**, **Batching** tiếp nhận điểm tựa từ **Caching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết (connection / 연결) pools** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Batching

Batching amortizes fixed overhead: syscall, mạng (network / 네트워크) RTT, giao dịch (transaction / 트랜잭션) lần ghi nhận (commit / 커밋), GPU launch. But batch too large increases wait/bộ nhớ (memory / 메모리) and thất bại (failure / 실패) phạm vi (scope / 범위). Choose batch by throughput-latency SLO.

> **Chuyển mạch:** Trong **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), sức chứa (capacity / 용량) và scalability**, sau nội dung của **Batching**, **Liên kết (connection / 연결) pools** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Tải (load / 로드) balancing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết (connection / 연결) pools

DB/mạng (network / 네트워크) liên kết (connection / 연결) setup costly, so pools reuse connections and bound tính đồng thời (concurrency / 동시성). Too small creates waits; too large overwhelms cơ sở dữ liệu (database / 데이터베이스) and raises contention. Pool is admission điều khiển (control / 제어), not just tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Ở chặng này của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), sức chứa (capacity / 용량) và scalability**, **Tải (load / 로드) balancing** tiếp nhận điểm tựa từ **Liên kết (connection / 연결) pools** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiệu năng (performance / 성능) đo lường (measurement / 측정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tải (load / 로드) balancing

Round-robin, least-connections, consistent hashing and weighted strategies distribute công việc (work / 작업) under different các giả định (assumptions / 가정들). Health check độ trễ (latency / 지연 시간)/staleness and sticky sessions affect balance. Locality/caching may favor affinity but rủi ro (risk / 위험) hotspots.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), sức chứa (capacity / 용량) và scalability**, **Tải (load / 로드) balancing** nêu điều cần giải thích; **Hiệu năng (performance / 성능) đo lường (measurement / 측정)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiệu năng (performance / 성능) đo lường (measurement / 측정)

Measure representative production-like tải công việc (workload / 워크로드), warm-up where thời gian chạy (runtime / 런타임) JIT/bộ nhớ đệm (cache / 캐시) matters, percentiles, tài nguyên (resource / 자원) counters and saturation. Microbenchmarks isolate thao tác (operation / 연산) but don't substitute end-to-end tests.

> **Chuyển mạch:** Trong **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), sức chứa (capacity / 용량) và scalability**, các dấu vết trong **Hiệu năng (performance / 성능) đo lường (measurement / 측정)** được đọc cùng nhau ở **Mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> hiệu năng (performance / 성능) is a **luồng (flow / 흐름) through finite resources**. Arrival tỷ lệ (rate / 비율) creates công việc (work / 작업); dịch vụ (service / 서비스) centers consume sức chứa (capacity / 용량); queues store excess; độ trễ (latency / 지연 시간) reveals waiting. Optimize bottleneck and protect headroom.

> **Chuyển mạch:** Ở chặng này của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), sức chứa (capacity / 용량) và scalability**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“CPU 100% means efficient.”** Under độ trễ (latency / 지연 시간) tải công việc (workload / 워크로드) it may mean saturated with exploding hàng đợi (queue / 큐).

**“bộ nhớ đệm (cache / 캐시) makes dữ liệu (data / 데이터) truy cập (access / 접근) O(1).”** Miss đường dẫn (path / 경로), mạng (network / 네트워크), eviction and consistency still matter.

**“Horizontal scaling solves cơ sở dữ liệu (database / 데이터베이스) bottleneck.”** trạng thái (state / 상태) partition/replication and coordination may become new bottlenecks.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), sức chứa (capacity / 용량) và scalability**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Complexity](../01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) các mô hình (models / 모델들) growth of cục bộ (local / 로컬) algorithms; [memory hierarchy](../02_computer_architecture/02_memory_hierarchy_and_cache.md) hardware hiệu năng (performance / 성능); [fault tolerance](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) uses sức chứa (capacity / 용량) headroom and tải (load / 로드) shedding.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
