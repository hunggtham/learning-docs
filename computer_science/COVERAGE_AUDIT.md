# Coverage kiểm tra (audit / 감사) — Khoa học máy tính (computer science / 컴퓨터 과학) chuẩn gốc (canonical / 정본) thư viện (library / 라이브러리)

> **Mạch đọc:** Đặt **Coverage kiểm tra (audit / 감사) — Khoa học máy tính (computer science / 컴퓨터 과학) chuẩn gốc (canonical / 정본) thư viện (library / 라이브러리)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. ranh giới (boundary / 경계) và cấu trúc tổng thể** sang **2. Computer kiến trúc (architecture / 아키텍처) — strong**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> kiểm tra (audit / 감사) cập nhật: 2026-09-23. Khoa học máy tính (computer science / 컴퓨터 과학) đã đủ rộng để vòng tiếp theo ưu tiên **deepening các gap trong đơn vị sở hữu (owner / 오너) hiện có**, không mở thêm lĩnh vực (domain / 도메인) lớn. Mục tiêu vẫn là: **foundation → internals → thất bại (failure / 실패) modes → pressure hành vi (behavior / 동작) → bằng chứng vận hành (production evidence / 운영 증거) → lower lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층)**.

Kiểm tra (audit / 감사) không hỏi “đã có từ khóa (keyword / 키워드) X chưa?”. Một lĩnh vực (domain / 도메인) được coi là mạnh khi người đọc có thể đi từ **bài toán (problem / 문제) → bất biến (invariant / 불변식) → cơ chế (mechanism / 메커니즘) → giả định (assumption / 가정) → thất bại (failure / 실패) → pressure-induced hành vi (behavior / 동작) → bằng chứng (evidence / 증거) → lower tầng (layer / 계층)** mà không cần rời chapter chỉ để hiểu prerequisite ẩn.

## 1. ranh giới (boundary / 경계) và cấu trúc tổng thể

`computer_science/basic/` là prerequisite/foundation tầng (layer / 계층). Các lĩnh vực (domain / 도메인) ở gốc (root / 루트) đi sâu theo conceptual ranh giới (boundary / 경계). `advanced/` chỉ chứa topic có mô hình tư duy (mental model / 사고 모델) riêng đủ bền. `90_connections/` nối các tầng (layer / 계층) thay vì duplicate nội dung.

Ranh giới (boundary / 경계) hiện tại:

```text
Computer Architecture
Operating Systems
Programming Languages & Runtime
Data & Databases
Networks & Distributed Systems
Security & Reliability
Software Systems / Performance / System Design
Software Engineering
AI Foundations
Cross-layer Connections
```

Không tách mạng (network / 네트워크), phân tán (distributed / 분산) các hệ thống (systems / 시스템들), bảo mật (security / 보안), độ tin cậy (reliability / 신뢰성), hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링), tính đồng thời (concurrency / 동시성) hay hệ thống (system / 시스템) thiết kế (design / 설계) thành gốc (root / 루트) thư viện (library / 라이브러리) mới. Specialized AI vẫn thuộc `02_artificial_intelligence/`; `10_ai_foundations/` chỉ giữ cầu nối (bridge / 브리지) CS các hệ thống (systems / 시스템들)/foundations. Các gốc (root / 루트) mới như `cybersecurity/`, `distributed_systems/` hay `system_design/` chỉ được xem xét sau khi các gap bên dưới đã được deepen và chứng minh không còn đơn vị sở hữu (owner / 오너) phù hợp.

## 2. Computer kiến trúc (architecture / 아키텍처) — strong

Coverage đã có OoO/ROB/register renaming, speculation, bộ nhớ đệm (cache / 캐시)/prefetch/replacement, NUMA/interconnect/coherence, TLB/page walk/virtualization, SIMD/GPU thực thi (execution / 실행) và bộ nhớ (memory / 메모리) consistency.

Memory-order đường dẫn (path / 경로) đủ để lập luận (reasoning / 추론) từ store buffer/coherence tới ISA thứ tự (ordering / 순서), trình biên dịch (compiler / 컴파일러) ánh xạ (mapping / 매핑), ngôn ngữ (language / 언어) happens-before, RMW contention, ABA/reclamation và PMU bằng chứng (evidence / 증거).

Vòng này đã thêm `02_computer_architecture/advanced/07_power_thermal_dvfs_and_sustained_performance.md`, sở hữu lập luận (reasoning / 추론) đường dẫn (path / 경로) từ activity → power/heat → DVFS/điều khiển (control / 제어) → sustained thông lượng (throughput / 처리량). Hardware-prefetch pathology đã được deepen trong `02_computer_architecture/advanced/03_advanced_cache_hierarchy_prefetching_and_replacement.md`, gồm accuracy/timeliness/coverage, pollution, bandwidth theft, hàng đợi (queue / 큐) pressure và controlled comparison. Bước tiếp theo là lower-layer kiểm tra hợp lệ (validation / 검증) bằng hardware-event bằng chứng (evidence / 증거), không mở chapter mới.

## 3. Operating các hệ thống (systems / 시스템들) — RCU/reclamation đã thành chuẩn gốc (canonical / 정본) đơn vị (unit / 단위)

OS advanced cover syscall/kernel contexts, scheduler/run queues, page faults/reclaim, VM/TLB shootdown, filesystem crash consistency, async I/O/DMA và bộ chứa (container / 컨테이너) isolation.

Vòng này thêm:

- `03_operating_systems/advanced/07_rcu_seqlock_and_safe_memory_reclamation.md`

Chapter mới sở hữu lập luận (reasoning / 추론) đường dẫn (path / 경로):

```text
publication
→ reader lifetime
→ logical removal
→ grace/quiescent proof
→ deferred reclamation
→ pressure/backlog
→ safe physical reuse
```

Nó phân biệt mutual exclusion với thời gian tồn tại (lifetime / 수명) an toàn (safety / 안전), grace period với hết thời gian chờ (timeout / 타임아웃), logical removal với vật lý (physical / 물리적) reclamation; đào sâu bộ nhớ (memory / 메모리) thứ tự (ordering / 순서), callback debt, seqlock thử lại (retry / 재시도), epoch/hazard-pointer comparison, ABA, scheduler tương tác (interaction / 상호작용), NUMA/cache-coherence chi phí (cost / 비용) và bằng chứng vận hành (production evidence / 운영 증거) của reclamation backlog.

`00_kernel_execution_contexts_and_syscall_path.md` vẫn giữ overview để người đọc hiểu ngữ cảnh (context / 맥락)/khóa (lock / 잠금)/thời gian tồn tại (lifetime / 수명) trước khi chuyển sang chapter chuyên sâu. Đây là cross-link có chủ đích, không phải hai chuẩn gốc (canonical / 정본) owners cạnh tranh.

Vòng này đã thêm `03_operating_systems/advanced/08_ebpf_tracing_kernel_observability_and_safety.md`, sở hữu verifier/JIT, helper/map/ring-buffer, sự kiện (event / 이벤트) mất mát (loss / 손실), overhead và an toàn (safety / 안전) ranh giới (boundary / 경계). Chapter đã được deepen thêm cho kernel networking đường dẫn (path / 경로): ingress/egress vòng đời (lifecycle / 생명주기), NAPI/softirq, socket/qdisc boundaries, GRO/GSO, drop-vs-delay-vs-retransmission và flow-correlated bằng chứng (evidence / 증거). Bước tiếp theo là lower-layer kiểm tra hợp lệ (validation / 검증) theo driver/tải công việc (workload / 워크로드) cụ thể, không mở chapter riêng nếu chỉ lặp packet-path overview.

## 4. Programming Languages & thời gian chạy (runtime / 런타임) — strong

Coverage mạnh ở kiểu (type / 타입)/tác động (effect / 효과)/thời gian chạy (runtime / 런타임) đặc tả hợp đồng (contract / 계약), quyền sở hữu (ownership / 소유권), trình biên dịch (compiler / 컴파일러) IR/SSA, JIT/deoptimization, GC barriers, coroutine, ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) và FFI/bản địa (native / 네이티브) ranh giới (boundary / 경계).

Bản địa (native / 네이티브) đường dẫn (path / 경로) hiện nối:

```text
source type
→ runtime representation
→ marshalling
→ ABI/calling convention
→ native ownership/lifetime
→ error/thread-state translation
→ result
```

RCU/reclamation chapter mới ở OS tạo thêm cross-layer link tới quyền sở hữu (ownership / 소유권)/memory-ordering mà không tạo gốc (root / 루트) tính đồng thời (concurrency / 동시성) thư viện (library / 라이브러리).

**Coverage status:** strong cho trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임)/JIT/GC/async/bản địa (native / 네이티브) interop.

## 5. tính đồng thời (concurrency / 동시성) — strong và đúng đơn vị sở hữu (owner / 오너) ranh giới (boundary / 경계)

Tính đồng thời (concurrency / 동시성) vẫn phân theo đơn vị sở hữu (owner / 오너) của bất biến (invariant / 불변식):

```text
Architecture   → cache/coherence/ordering cost
OS             → scheduler/threads/waiting/reclamation
Language       → happens-before/ownership
Runtime        → coroutine/task scheduling
Software Sys   → queue/backpressure/fairness
Distributed    → causality/partial failure
```

`90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md` là chuẩn gốc (canonical / 정본) cross-layer proof đường dẫn (path / 경로).

## 6. dữ liệu (data / 데이터) & Databases — OLTP + analytical vật lý (physical / 물리적) đường dẫn (path / 경로) đều mạnh

MVCC/WAL/khôi phục (recovery / 복구), khóa (lock / 잠금) manager, B+cây (tree / 트리), LSM, buffer pool, optimizer, phép nối (join / 조인)/vectorized thực thi (execution / 실행) và phân tán (distributed / 분산) transactions đã có chuẩn gốc (canonical / 정본) chapters.

Vòng này thêm:

- `05_data_databases/advanced/08_columnar_storage_encoding_pruning_and_vectorized_scans.md`

Columnar lưu trữ (storage / 저장소) đủ độc lập để thành chapter vì nó có physical-performance bất biến (invariant / 불변식) riêng:

```text
logical table
→ row group / column chunk
→ encoding + compression + metadata
→ partition/file/row-group pruning
→ projection/predicate pushdown
→ vectorized scan
→ selection vector
→ late materialization
→ spill / shuffle
```

Chapter làm rõ dictionary/RLE/delta/bit-packing sự đánh đổi (trade-off / 트레이드오프), min-max/zone map, Bloom negative pruning, clustering, null/nested biểu diễn (representation / 표현), immutable segment + delta/delete đường dẫn (path / 경로), reclustering debt, memory-bandwidth bottleneck, spill phase thay đổi (change / 변경), phân tán (distributed / 분산) skew và thời gian chạy (runtime / 런타임) counters.

Pruning siêu dữ liệu (metadata / 메타데이터) được giữ theo bất biến (invariant / 불변식): false-positive công việc (work / 작업) có thể chấp nhận; false-negative kết quả (result / 결과) không được phép nếu ngữ nghĩa (semantics / 의미론) là chính xác (exact / 정확한).

**Coverage status:** strong cho OLTP storage-engine internals và analytical lưu trữ (storage / 저장소)/thực thi (execution / 실행) đường dẫn (path / 경로).

Vòng này đã thêm `05_data_databases/advanced/09_adaptive_query_execution_runtime_filters_skew_and_reoptimization.md`, đóng gap chính về thời gian chạy (runtime / 런타임) phản hồi (feedback / 피드백), động (dynamic / 동적) filtering, skew và plan adaptation. **Gap còn lại:** analytical cost-model trường hợp (case / 사례) studies chỉ khi có bất biến (invariant / 불변식)/bằng chứng vận hành (production evidence / 운영 증거) mới, không mở chapter theo technology name.

## 7. Networks — vận chuyển (transport / 전송) và inter-domain routing đều có advanced lập luận (reasoning / 추론)

Foundation đã cover Ethernet/IP/routing, TCP/UDP/congestion, DNS/HTTP/TLS, sockets/IPv6/NAT/firewall/VPN, BGP và HTTP/2–HTTP/3/QUIC.

Hiện đại (modern / 현대적) vận chuyển (transport / 전송) đã đủ sâu ở TCP head-of-line, QUIC packet number vs stream offset, mất mát (loss / 손실) khôi phục (recovery / 복구), congestion/luồng (flow / 흐름) điều khiển (control / 제어), TLS/0-RTT, liên kết (connection / 연결) ID, PMTU black-hole, fallback và encrypted-transport bằng chứng (evidence / 증거).

Vòng này thêm:

- `06_networks_distributed_systems/advanced/07_bgp_routing_policy_convergence_and_route_security.md`

BGP chapter sở hữu trạng thái (state / 상태) đường dẫn (path / 경로):

```text
prefix reachability
→ advertisement/withdrawal
→ import/export policy
→ path selection
→ RIB
→ FIB
→ observed packet path
```

Đã phân biệt điều khiển (control / 제어) plane/mặt phẳng dữ liệu (data plane / 데이터 플레인), eBGP/iBGP/underlay, chính sách (policy / 정책) vs shortest đường dẫn (path / 경로), RIB/FIB, convergence/đường dẫn (path / 경로) exploration, aggregation, more-specific routes, tuyến (route / 경로) leak vs hijack, RPKI phạm vi (scope / 범위), filtering/max-prefix, communities, anycast, asymmetric routing, ECMP skew và multi-vantage-point sự cố (incident / 인시던트) bằng chứng (evidence / 증거).

**Coverage status:** strong cho web vận chuyển (transport / 전송) và routing-policy môi trường vận hành (production / 운영 환경) diagnosis.

**Gap còn lại:** kernel packet đường dẫn (path / 경로) hoặc congestion-control hiện thực (implementation / 구현) trường hợp (case / 사례) studies nếu tạo durable mô hình tư duy (mental model / 사고 모델).

## 8. phân tán (distributed / 분산) các hệ thống (systems / 시스템들) — strong

Thất bại (failure / 실패) detectors, membership/gossip, lease/fencing, consensus/reconfiguration, CRDT/nhân quả (causal / 인과적) consistency, clocks/causality, exactly-once ambiguity, phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션) ngữ nghĩa (semantics / 의미론) và multi-region authority/failover đã có lập luận (reasoning / 추론) đường dẫn (path / 경로) rõ.

BGP chapter bổ sung một phân tán (distributed / 분산) chính sách (policy / 정책)/control-plane trường hợp (case / 사례) nhưng không thay đơn vị sở hữu (owner / 오너) của consensus/replication material.

Joint-consensus/reconfiguration đã có đơn vị sở hữu (owner / 오너) trong `06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md`. **Gap còn lại:** queueing under partition và worked proof sâu hơn, ưu tiên deepen chapter consensus/replication hiện có.

## 9. bảo mật (security / 보안) & độ tin cậy (reliability / 신뢰성) — detection/forensics đã có chuẩn gốc (canonical / 정본) bằng chứng (evidence / 증거) đường dẫn (path / 경로)

Bảo mật (security / 보안) advanced có authority đồ thị (graph / 그래프) từ định danh (identity / 식별자) → authorization → credential/năng lực (capability / 역량) → TLS/dịch vụ (service / 서비스) ranh giới (boundary / 경계) → containment, cùng crypto composition, PKI/mTLS, OAuth/OIDC, bộ nhớ (memory / 메모리) an toàn (safety / 안전)/sandbox, trình duyệt (browser / 브라우저) isolation và KMS/HSM.

Vòng này thêm:

- `07_security_reliability/advanced/07_detection_engineering_forensics_and_incident_evidence.md`

Chapter mới đi theo:

```text
security invariant
→ trusted telemetry
→ detection hypothesis
→ correlation
→ triage/investigation
→ containment
→ recovery
→ learning
```

Đã bổ sung bằng chứng (evidence / 증거) trust, sự kiện (event / 이벤트) định danh (identity / 식별자)/causality, base-rate bài toán (problem / 문제), false positive/negative, correlation windows, clock bất định (uncertainty / 불확실성), tamper-resistant kiểm tra (audit / 감사) đường dẫn (path / 경로), provenance/chuỗi (chain / 사슬) of custody, ephemeral hạ tầng (infrastructure / 인프라), bộ nhớ (memory / 메모리)/tiến trình (process / 프로세스)/mạng (network / 네트워크) bằng chứng (evidence / 증거), định danh (identity / 식별자) đồ thị (graph / 그래프), effective secret revocation, logging overload, telemetry dữ liệu (data / 데이터) chất lượng (quality / 품질), privacy/retention và sự cố (incident / 인시던트) containment theo năng lực (capability / 역량) đồ thị (graph / 그래프).

**Coverage status:** strong cho preventive controls + môi trường vận hành (production / 운영 환경) detection/forensics.

Detection/forensics và detection-quality đo lường (measurement / 측정) đã có đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자) trong `07_security_reliability/advanced/07_detection_engineering_forensics_and_incident_evidence.md`; chapter hiện có đo lường (measurement / 측정) giao thức (protocol / 프로토콜) cho label provenance, prevalence, precision/recall, analyst sức chứa (capacity / 용량), false-negative exposure, calibration và regression gates. **Gap còn lại:** selected software-supply-chain trust cơ chế (mechanism / 메커니즘) nếu tạo independent lập luận (reasoning / 추론) đường dẫn (path / 경로).

## 10. Software các hệ thống (systems / 시스템들) & hiệu năng (performance / 성능) — từ single host đến fleet economics

Queueing/backpressure, sức chứa (capacity / 용량)/admission, caching, tải (load / 로드) balancing/pools, streams, idempotency và lược đồ (schema / 스키마) evolution đã có coverage tốt. Whole-system profiling đã nối SLO symptom với hàng đợi (queue / 큐)/dịch vụ (service / 서비스) split, on/off-CPU, scheduler, PMU/bộ nhớ đệm (cache / 캐시)/bộ nhớ (memory / 메모리) bandwidth, I/O hàng đợi (queue / 큐) độ sâu (depth / 깊이) và useful-outcome chi phí (cost / 비용).

Vòng này thêm:

- `08_software_systems/advanced/07_fleet_profiling_cost_attribution_and_multi_tenant_efficiency.md`

Chapter mới mở rộng quy mô (scale / 규모):

```text
useful demand
→ distributed critical path
→ fleet resource consumption
→ placement/skew/headroom
→ SLO outcome
→ cost attribution
→ capacity/architecture decision
```

Nó giải thích aggregation độ lệch (bias / 편향), hardware cohorts, chi phí (cost / 비용) per useful kết quả (outcome / 결과), thất bại (failure / 실패) headroom, bin-packing/blast-radius sự đánh đổi (trade-off / 트레이드오프), rightsizing, noisy neighbors, fairness work-unit, shared-cost allocation, showback/chargeback, tracing-vs-profiling-vs-metrics, sampling độ lệch (bias / 편향), rollout cohort comparison, tail cohort drill-down, autoscaling oscillation, cold start và accelerator bộ nhớ (memory / 메모리)/hàng đợi (queue / 큐) economics.

**Coverage status:** strong cho single-node + fleet-level hiệu năng (performance / 성능)/chi phí (cost / 비용) lập luận (reasoning / 추론).

**Gap còn lại:** fleet-wide nhân quả (causal / 인과적) profiling hoặc scheduler-specific hiện thực (implementation / 구현) chỉ khi có trường hợp (case / 사례) thật sự cần.

## 11. hệ thống (system / 시스템) thiết kế (design / 설계) — vẫn thuộc Software các hệ thống (systems / 시스템들)

Chuẩn gốc (canonical / 정본) entry điểm (point / 지점) vẫn là `08_software_systems/07_system_decomposition_services_and_boundaries.md`. ranh giới (boundary / 경계) được lập luận (reasoning / 추론) bằng bất biến (invariant / 불변식)/quyền sở hữu trạng thái (state ownership / 상태 소유권), thất bại (failure / 실패), sức chứa (capacity / 용량), bảo mật (security / 보안) authority và economics; không bằng checklist technology.

Fleet chapter làm rõ placement, multi-tenancy, fairness, headroom và chi phí (cost / 비용) attribution nhưng không tạo gốc (root / 루트) hiệu năng (performance / 성능)/hệ thống (system / 시스템) thiết kế (design / 설계) thư viện (library / 라이브러리) mới.

## 12. Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) — changeability giờ có debt economics riêng

Kiến trúc (architecture / 아키텍처) evolution, modularity economics, API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성), di chuyển (migration / 마이그레이션) máy trạng thái (state machine / 상태 머신), testing và triển khai (deployment / 배포) an toàn (safety / 안전) đã mạnh.

Vòng này thêm:

- `09_software_engineering/advanced/06_technical_debt_economics_metrics_and_goodhart.md`

Chapter mới định nghĩa debt bằng future thay đổi (change / 변경) chi phí (cost / 비용)/rủi ro (risk / 위험) thay vì mã (code / 코드) aesthetics; phân biệt deliberate/accidental/obsolescence debt; đào sâu thay đổi (change / 변경) amplification, coordination/dữ liệu (data / 데이터)/kiểm thử (test / 테스트)/operational debt, recurring interest bằng chứng (evidence / 증거), trigger/exit điều kiện (condition / 조건), option giá trị (value / 값), reversibility, compounding coupling và quyết định paydown/contain/accept/retire.

Chỉ số (metric / 지표) quản trị (governance / 거버넌스) đi theo kết quả (outcome / 결과) → guardrail → delivery/hệ thống (system / 시스템) signals. Goodhart rủi ro (risk / 위험) được giải thích qua coverage/deploy/ticket/LOC proxy; DORA-style metrics được dùng như diagnostic tín hiệu (signal / 신호) chứ không nhóm (team / 팀) leaderboard.

**Coverage status:** strong cho xác minh (verification / 확인), di chuyển (migration / 마이그레이션), triển khai (deployment / 배포) và economics/quản trị (governance / 거버넌스) của changeability.

**Gap còn lại:** deeper organizational thiết kế (design / 설계) hoặc portfolio-level modernization chỉ khi cần trường hợp (case / 사례) study lớn.

## 13. AI Foundations — giữ ranh giới (boundary / 경계) hẹp

Transformer suy luận (inference / 추론) và phân tán (distributed / 분산) huấn luyện (training / 학습) đã có KV quyền sở hữu (ownership / 소유권), batching/admission, bandwidth pressure, topology-aware collectives, stragglers, phân tán (distributed / 분산) checkpoint, restart storm và bằng chứng (evidence / 증거).

Fleet chi phí (cost / 비용) chapter tạo cầu nối (bridge / 브리지) tốt hơn cho accelerator utilization/chi phí (cost / 비용) nhưng không kéo khung phần mềm (framework / 프레임워크)/kernel vendor-specific vào CS.

**Gap còn lại:** accelerator trình biên dịch (compiler / 컴파일러)/kernel scheduling, suy luận (inference / 추론) disaggregation và heterogeneous-memory trường hợp (case / 사례) study nếu chúng tạo durable mô hình tư duy (mental model / 사고 모델).

## 14. Cross-layer Connections — chuẩn gốc (canonical / 정본) tích hợp (integration / 통합) tầng (layer / 계층)

`90_connections/advanced/` giữ bốn paths chính:

```text
Debugging:
symptom → invariant → evidence → lower layer → fix/containment

End-to-end request:
DNS/TCP-or-QUIC/TLS → routing/proxy/LB → runtime → pools/DB/storage
+ retry → timeout → queue → overload/backpressure

Correctness:
CPU cache/coherence → ordering → language memory model → concurrency/lifetime bug

Durability:
application commit → MVCC/WAL → filesystem/storage → replication authority
```

Các chapter mới cung cấp nguồn (source / 소스) sâu hơn để các liên kết (connection / 연결) trỏ tới; không tăng liên kết (connection / 연결) chapter chỉ để đổi tên cùng lập luận (reasoning / 추론).

## 15. Repository hygiene và branch chiến lược (strategy / 전략)

Khoa học máy tính (computer science / 컴퓨터 과학) vẫn có một chuẩn gốc (canonical / 정본) tính năng (feature / 기능) branch: `feat/computer-science`. cây (tree / 트리) không dùng naming mẫu (pattern / 패턴) duplicate/temp như `_final`, `_updated`, `_version2` cho vòng mới.

Repo không có dedicated glossary cho `computer_science/`; không tạo glossary chỉ để đủ checklist. Terminology được điều phối bởi `LANGUAGE_STYLE.md` và định nghĩa tại đơn vị sở hữu (owner / 오너) chapter.

`main` có các thay đổi mới hơn thuộc TypeScript/React/Mathematics, không thuộc Khoa học máy tính (computer science / 컴퓨터 과학). Khi đưa Khoa học máy tính (computer science / 컴퓨터 과학) lên `main`, phải preserve các thay đổi đó và merge/bản sao (copy / 복사) đúng `computer_science/` subtree thay vì reset hoặc force-update `main` về tính năng (feature / 기능) branch.

## 16. P1 — Khoa học máy tính (computer science / 컴퓨터 과학): chỉ deepen gap, không mở thêm lĩnh vực (domain / 도메인) lớn

Khoa học máy tính (computer science / 컴퓨터 과학) đã rất rộng: computation, DSA, kiến trúc (architecture / 아키텍처), OS, thời gian chạy (runtime / 런타임), cơ sở dữ liệu (database / 데이터베이스), networking/phân tán (distributed / 분산), bảo mật (security / 보안), software các hệ thống (systems / 시스템들), kỹ nghệ phần mềm (software engineering / 소프트웨어 공학), AI và HCI. Vì vậy, các gap dưới đây là backlog P1 trước khi cân nhắc mở thêm một lĩnh vực (domain / 도메인) gốc (root / 루트):

```text
Architecture
✓ power / thermal / DVFS (canonical chapter đã có)
✓ hardware-prefetch pathology (đã deepen trong canonical cache chapter)

Operating Systems
✓ eBPF / tracing internals (canonical chapter đã có)
✓ kernel networking path (đã deepen trong eBPF chapter; cần validation theo workload)

Database
✓ adaptive analytical execution (canonical chapter đã có)
→ deeper analytical cost-model case studies

Distributed Systems
✓ reconfiguration owner (canonical consensus chapter đã có)
→ reconfiguration worked proofs
→ partition + queueing behavior

Security
→ software supply-chain trust
✓ detection quality measurement (đã deepen trong detection chapter)

AI Systems
→ accelerator compiler / kernel scheduling
→ inference disaggregation

Cross-layer
→ incident → correctness / durability / cost
```

Đây là những việc cần làm trước khi nghĩ tới các gốc (root / 루트) như `cybersecurity/`, `distributed_systems/` hoặc `system_design/`; repository hiện đã có đơn vị sở hữu (owner / 오너) phù hợp cho các ranh giới (boundary / 경계) này.

Một chi tiết naming nên cân nhắc sau: hiện tồn tại cả `02_artificial_intelligence` và `02_computer_architecture`, đồng thời còn `10_ai_foundations`. README đã giải thích ranh giới (boundary / 경계), nhưng numbering vẫn dễ gây nhầm khi nhìn cây (tree / 트리) trực tiếp. Không rename trong vòng P1 này; chỉ chuẩn hóa khi có kế hoạch di chuyển (migration / 마이그레이션) và cập nhật toàn bộ nội bộ (internal / 내부) links.

Các dấu `✓` là gap đã có đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자); mũi tên `→` là phần cần deepen tiếp theo. Nguyên tắc tiếp tục vẫn là **absorb vào tệp chuẩn gốc (canonical file / 정본 파일) nếu cùng bất biến (invariant / 불변식); chỉ tăng chapter count khi topic có mô hình tư duy (mental model / 사고 모델) riêng, phụ thuộc (dependency / 의존성) rộng và đơn vị sở hữu (owner / 오너) ranh giới (boundary / 경계) rõ**.

## 17. cổng chất lượng (quality gate / 품질 게이트)

Một advanced chapter chỉ được coi là đủ sâu khi trả lời tự nhiên:

```text
Vấn đề ban đầu là gì?
Invariant nào cần giữ?
Mechanism bên trong giữ invariant bằng cách nào?
Assumption nào đang được dựa vào?
Failure xảy ra ở đâu và biểu hiện thế nào?
Pressure làm behavior đổi phase ra sao?
Security/consistency/concurrency boundary nào liên quan?
Production evidence nào phân biệt các hypotheses?
Tầng abstraction bên dưới nào thực sự quyết định behavior?
Canonical source nào sở hữu kiến thức để tránh duplicate?
```

Prose là phần chính; bullet chỉ dùng cho danh sách (list / 목록) tự nhiên. Thuật ngữ English/Korean được giữ khi hữu ích nhưng phải giải thích bằng tiếng Việt. API/sản phẩm (product / 제품)/phiên bản (version / 버전) chỉ neo cơ chế (mechanism / 메커니즘), không thay cơ chế (mechanism / 메커니즘).

## Kết luận

Chuẩn gốc (canonical / 정본) `computer_science/` đã chuyển từ chỉ độ sâu (depth / 깊이) consolidation sang **selective chapter expansion**. Sáu gap trước đây được giữ trong chapter lớn giờ đã đủ độc lập để trở thành chuẩn gốc (canonical / 정본) units: safe bộ nhớ (memory / 메모리) reclamation, columnar analytical lưu trữ (storage / 저장소), BGP/routing chính sách (policy / 정책), detection/forensics, fleet profiling/chi phí (cost / 비용) attribution và technical-debt economics/chỉ số (metric / 지표) quản trị (governance / 거버넌스).

Giá trị của các chapter mới không nằm ở tăng tệp (file / 파일) count mà ở việc tạo sáu lập luận (reasoning / 추론) paths mới có đơn vị sở hữu (owner / 오너) rõ, cross-link rõ và bằng chứng vận hành (production evidence / 운영 증거) rõ. Vòng tiếp theo nên ưu tiên trường hợp (case / 사례) study sâu và lower-layer kiểm tra hợp lệ (validation / 검증) hơn là tiếp tục tăng chapter count mặc định.

> **Bàn giao:** Sau **Kết luận**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [99 glossary](./99_glossary.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
