# Liên kết kiến thức (knowledge connection / 지식 연결) — sự đánh đổi (trade-off / 트레이드오프) xuyên Khoa học máy tính (computer science / 컴퓨터 과학)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trade-offs xuyên Khoa học máy tính (computer science / 컴퓨터 과학)**. Route đi từ time↔space và latency↔throughput tới consistency↔availability, isolation↔concurrency, abstraction↔control, rồi kết thúc bằng SLO/invariant/workload để chọn trade-off có bằng chứng.


Nhiều câu hỏi kỹ thuật không có answer “cái nào tốt nhất” vì resources và guarantees cạnh tranh. Một cách trưởng thành để lập luận (reasoning / 추론) là xác định mục tiêu (objective / 목표), ràng buộc (constraint / 제약조건) và sự đánh đổi (trade-off / 트레이드오프) dimension thay vì học quy tắc (rule / 규칙) tuyệt đối.

## Thời gian (time / 시간) ↔ không gian (space / 공간)

Memoization dùng bộ nhớ (memory / 메모리) để giảm recomputation. chỉ mục (index / 인덱스) dùng lưu trữ (storage / 저장소)/RAM để giảm truy vấn (query / 쿼리) thời gian (time / 시간). bộ nhớ đệm (cache / 캐시) dùng duplicated trạng thái (state / 상태) để giảm độ trễ (latency / 지연 시간). Bloom filter dùng bits để tránh expensive lookups nhưng chấp nhận false positives.

Ngược lại, compression dùng CPU để giảm lưu trữ (storage / 저장소)/mạng (network / 네트워크) bandwidth.

Không có “optimize bộ nhớ (memory / 메모리)” hoặc “optimize speed” độc lập; tải công việc (workload / 워크로드) và bottleneck quyết định.

## Độ trễ (latency / 지연 시간) ↔ thông lượng (throughput / 처리량)

Batching tăng thông lượng (throughput / 처리량) bằng amortizing fixed chi phí (cost / 비용) nhưng item đầu chờ batch fill. Larger queues smooth bursts nhưng tăng queueing độ trễ (latency / 지연 시간). cơ sở dữ liệu (database / 데이터베이스) group lần ghi nhận (commit / 커밋) batches fsync to improve thông lượng (throughput / 처리량) at small độ trễ (latency / 지연 시간) chi phí (cost / 비용).

Interactive các hệ thống (systems / 시스템들) ưu tiên tails; batch analytics ưu tiên aggregate thông lượng (throughput / 처리량).

> **Chuyển mạch:** Time/space và latency/throughput đều nói về việc đổi tài nguyên này lấy tài nguyên kia. **Consistency ↔ Availability/độ trễ (latency / 지연 시간)** đưa trade-off vào guarantee quan sát được: chờ quorum để giữ durability/consistency hay trả sớm với replica lag.

## Consistency ↔ Availability/độ trễ (latency / 지연 시간)

Synchronous quorum ghi (write / 쓰기) waits more replicas: stronger durability/consistency under failures but higher độ trễ (latency / 지연 시간)/less availability during partition. Async replication returns earlier but allows lag.

CAP/PACELC are formalized views of some phân tán (distributed / 분산) trade-offs; they are not slogans for all thiết kế (design / 설계).

> **Chuyển mạch:** Khi consistency/availability đã được đặt thành guarantee của hệ thống phân tán, **Isolation ↔ tính đồng thời (concurrency / 동시성)** chuyển câu hỏi vào transaction và shared state. Cả hai đều yêu cầu nêu rõ anomaly nào chấp nhận được trước khi tối ưu throughput.

## Isolation ↔ tính đồng thời (concurrency / 동시성)

Serializable giao dịch (transaction / 트랜잭션) gives strong lập luận (reasoning / 추론) but may khối (block / 블록)/abort more. Weaker isolation permits more overlap but ứng dụng (application / 애플리케이션) must tolerate anomalies.

OS coarse khóa (lock / 잠금) simpler tính đúng đắn (correctness / 정확성) but reduces parallelism; fine locks increase tính đồng thời (concurrency / 동시성) and độ phức tạp (complexity / 복잡도)/deadlock surface.

Same mental cấu trúc (structure / 구조) at different layers.

> **Chuyển mạch:** Isolation và concurrency cho thấy một guarantee có thể mua bằng lock, abort hoặc complexity. **Lớp trừu tượng (abstraction / 추상화) ↔ điều khiển (control / 제어)** tiếp tục bằng câu hỏi layer nào sở hữu invariant và khi nào abstraction phải bị xuyên qua để chẩn đoán.

## Lớp trừu tượng (abstraction / 추상화) ↔ điều khiển (control / 제어)

High-level managed thời gian chạy (runtime / 런타임) hides bộ nhớ (memory / 메모리) and offers an toàn (safety / 안전)/productivity. Low-level ngôn ngữ (language / 언어) gives bố cục (layout / 레이아웃)/thời gian tồn tại (lifetime / 수명) điều khiển (control / 제어) but transfers responsibility. ORM hides SQL repetition but can produce N+1/truy vấn (query / 쿼리) inefficiency if nhà phát triển (developer / 개발자) ignores cơ sở dữ liệu (database / 데이터베이스) mô hình (model / 모델).

Lớp trừu tượng (abstraction / 추상화) reduces cognitive tải (load / 로드) until hidden detail affects yêu cầu (requirement / 요구사항); then leaky lớp trừu tượng (abstraction / 추상화) requires descending a tầng (layer / 계층).

## Generality ↔ tối ưu hóa (optimization / 최적화)

Generic thuật toán (algorithm / 알고리즘)/API works many inputs but cannot exploit specific cấu trúc (structure / 구조). Counting sort exploits integer phạm vi (range / 범위); specialized SIMD kernel exploits alignment; prepared kế hoạch truy vấn (query plan / 쿼리 계획) may exploit known parameter phân phối (distribution / 분포).

Specialization improves speed at chi phí (cost / 비용) mã (code / 코드) độ phức tạp (complexity / 복잡도)/portability.

## An toàn (safety / 안전) ↔ hiệu năng (performance / 성능)/Flexibility

Bounds checks prevent bộ nhớ (memory / 메모리) corruption but add checks (often optimized). Cryptographic xác minh (verification / 확인) adds CPU/độ trễ (latency / 지연 시간). Permission boundaries add syscalls/IPC. Removing checks for speed enlarges trusted computing cơ sở (base / 기반)/rủi ro (risk / 위험).

Good các hệ thống (systems / 시스템들) optimize an toàn (safety / 안전) mechanisms rather than silently remove guarantees.

## Redundancy ↔ chi phí (cost / 비용)/độ phức tạp (complexity / 복잡도)

Replication improves availability/read quy mô (scale / 규모) but costs hardware, bandwidth and consistency coordination. Backups chi phí (cost / 비용) lưu trữ (storage / 저장소)/operations but protect logical corruption. Multiple zones reduce correlated thất bại (failure / 실패) but increase mạng (network / 네트워크) độ trễ (latency / 지연 시간)/chi phí (cost / 비용).

## Freshness ↔ bộ nhớ đệm (cache / 캐시) hiệu năng (performance / 성능)

Long TTL raises hit ratio/lower tải (load / 로드) but returns stale dữ liệu (data / 데이터) longer. Short TTL improves freshness but increases origin traffic and stampede rủi ro (risk / 위험). sự kiện (event / 이벤트) vô hiệu hóa (invalidation / 무효화) improves freshness but adds delivery/thất bại (failure / 실패) độ phức tạp (complexity / 복잡도).

## Normalize ↔ Denormalize

Normalized DB reduces redundant facts/cập nhật (update / 업데이트) anomalies; denormalized read mô hình (model / 모델) avoids joins and supports analytics. Derived trạng thái (state / 상태) demands refresh/vô hiệu hóa (invalidation / 무효화) lô-gic (logic / 논리).

## Strong typing/static checks ↔ flexibility/bản dựng (build / 빌드) phản hồi (feedback / 피드백)

Static guarantees catch classes bugs earlier but require kiểu (type / 타입) modeling and compile checks. động (dynamic / 동적) các hệ thống (systems / 시스템들) permit rapid structural thay đổi (change / 변경) but shift detection to thời gian chạy (runtime / 런타임)/tests/tooling. hiện đại (modern / 현대적) ecosystems mix gradual typing, suy luận (inference / 추론) and thời gian chạy (runtime / 런타임) contracts.

## Optimize the real ràng buộc (constraint / 제약조건)

> **Chuyển mạch:** Các cặp trade-off đã cung cấp vocabulary; phần **Optimize the real ràng buộc (constraint / 제약조건)** gom chúng thành quy trình quyết định: xác định SLO/invariant, đo bottleneck, rồi kiểm tra option dưới workload đại diện thay vì tối ưu một nhãn công nghệ.

First-principles sự đánh đổi (trade-off / 트레이드오프) tiến trình (process / 프로세스):

1. define thuộc tính (property / 속성)/SLO/bất biến (invariant / 불변식);
2. identify bottleneck/tài nguyên (resource / 자원);
3. danh sách (list / 목록) các giả định (assumptions / 가정들) and thất bại (failure / 실패) mô hình (model / 모델);
4. compare options on dimensions, not labels;
5. measure/validate under representative tải công việc (workload / 워크로드);
6. preserve escape đường dẫn (path / 경로) if các giả định (assumptions / 가정들) thay đổi (change / 변경).

## Mô hình tư duy (mental model / 사고 모델)

> Most kiến trúc (architecture / 아키텍처) decisions are **moving chi phí (cost / 비용), rủi ro (risk / 위험) or độ phức tạp (complexity / 복잡도) between dimensions**, not eliminating it. Ask “what became cheaper, and what became more expensive?”

## Cross-references

This chapter connects [complexity](../01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md), [cache](../02_computer_architecture/02_memory_hierarchy_and_cache.md), [transaction isolation](../05_data_databases/02_transactions_acid_and_concurrency_control.md), [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [reliability](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) and [performance](../08_software_systems/02_performance_capacity_and_scalability.md).

> **Bàn giao:** Sau **Cross-references**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 source code to cpu](./00_source_code_to_cpu.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
