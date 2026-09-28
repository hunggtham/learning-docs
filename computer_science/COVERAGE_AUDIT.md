# Coverage Kiểm tra (audit / 감사) — Khoa học máy tính (computer science / 컴퓨터 과학) Chuẩn gốc (canonical / 정본) Thư viện (library / 라이브러리)

> Kiểm tra (audit / 감사) cập nhật: 2026-09-23 trên `feat/computer-science-depth-expansion`. Branch này được tạo từ `feat/computer-science` để tiếp tục đào sâu trong khi chuẩn gốc (canonical / 정본) parent/main đang được kiểm tra (audit / 감사) và merge. Không tạo Khoa học máy tính (computer science / 컴퓨터 과학) thư viện (library / 라이브러리) mới, không đổi conceptual ranh giới (boundary / 경계) hiện có.

Mục tiêu chất lượng vẫn là:

```text
foundation
→ internals
→ failure modes
→ performance / concurrency / consistency pressure
→ production evidence
→ lower abstraction layer
```

Kiểm tra (audit / 감사) không hỏi “đã có từ khóa (keyword / 키워드) X chưa?”. Một lĩnh vực (domain / 도메인) được coi là đủ mạnh khi người đọc có thể đi từ **bài toán (problem / 문제) → bất biến (invariant / 불변식) → cơ chế (mechanism / 메커니즘) → giả định (assumption / 가정) → thất bại (failure / 실패) → pressure-induced hành vi (behavior / 동작) → bằng chứng (evidence / 증거) → lower tầng (layer / 계층)** mà không phải rời chapter chỉ để hiểu prerequisite ẩn.

## 1. Ranh giới (boundary / 경계) và cấu trúc tổng thể

`computer_science/basic/` là prerequisite/foundation tầng (layer / 계층). Các lĩnh vực (domain / 도메인) ở gốc (root / 루트) đi sâu theo conceptual ranh giới (boundary / 경계). `advanced/` chỉ chứa topic có mô hình tư duy (mental model / 사고 모델) riêng đủ bền. `90_connections/` nối các tầng (layer / 계층) thay vì duplicate nội dung.

Ranh giới (boundary / 경계) chuẩn gốc (canonical / 정본) tiếp tục là:

```text
Computation & Information
Algorithms & Data Structures
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

Không tách Mạng (network / 네트워크), Phân tán (distributed / 분산) Các hệ thống (systems / 시스템들), Bảo mật (security / 보안), Độ tin cậy (reliability / 신뢰성), Hiệu năng (performance / 성능) Kỹ thuật (engineering / 엔지니어링), Tính đồng thời (concurrency / 동시성) hay Hệ thống (system / 시스템) Thiết kế (design / 설계) thành gốc (root / 루트) thư viện (library / 라이브러리) mới. Specialized AI vẫn thuộc thư viện (library / 라이브러리) AI chuyên sâu; `10_ai_foundations/` chỉ giữ cầu nối (bridge / 브리지) nền tảng các hệ thống (systems / 시스템들)/foundations của Khoa học máy tính (computer science / 컴퓨터 과학).

## 2. Computation & Thông tin (information / 정보) — từ computability tới xác minh (verification / 확인)

Nhánh học (track / 트랙) formal trước đây mạnh ở formal các mô hình (models / 모델들), automata và Rice/static-analysis limits nhưng còn dừng sớm trước thông tin (information / 정보)/randomness/resource-bounded computation. Vòng expansion này hoàn thiện chuẩn gốc (canonical / 정본) đường dẫn (path / 경로):

```text
formal model
→ computability / undecidability
→ semantic-analysis limits
→ Kolmogorov complexity
→ information theory
→ randomness / pseudorandomness
→ complexity classes beyond P/NP
→ interactive proofs / zero-knowledge / verifiable computation
```

Các chapter mới:

- `03_kolmogorov_complexity_compression_and_incompressibility.md`
- `04_information_theory_coding_bounds_and_noisy_channels.md`
- `05_randomness_entropy_sources_and_computational_unpredictability.md`
- `06_complexity_classes_conp_pspace_exp_and_randomized_classes.md`
- `07_interactive_proofs_zero_knowledge_and_verifiable_computation.md`

Coverage mới buộc người đọc phân biệt undecidable với computationally expensive; Kolmogorov độ phức tạp (complexity / 복잡도) của đối tượng (object / 객체) với Shannon entropy của phân phối (distribution / 분포); statistical randomness với cryptographic unpredictability; proof ngữ nghĩa (semantics / 의미론) với authorization/freshness/availability của môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템).

**Status:** strong cho formal lập luận (reasoning / 추론) nền tảng. Proof toán thuần dài vẫn nên cross-link sang `mathematics/` thay vì duplicate.

## 3. Algorithms & Dữ liệu (data / 데이터) Structures — mature specialized nhánh học (track / 트랙)

DSA advanced đã có foundation về modeling/bất biến (invariant / 불변식)/độ phức tạp (complexity / 복잡도)/bộ nhớ (memory / 메모리), tuyến tính (linear / 선형) structures, trees, graphs, algorithmic paradigms, specialized structures, C/Java/JavaScript hiện thực (implementation / 구현) và các hệ thống (systems / 시스템들) trường hợp (case / 사례) studies.

Ranh giới (boundary / 경계) hiện tại đủ mạnh; không cần tăng chapter count chỉ để thêm tên thuật toán. Gap mới chỉ nên mở khi biểu diễn (representation / 표현)/bất biến (invariant / 불변식)/độ phức tạp (complexity / 복잡도) mô hình (model / 모델) thực sự khác các đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자) hiện có.

**Status:** strong.

## 4. Computer Kiến trúc (architecture / 아키텍처) — bổ sung sustained-performance vòng điều khiển (control loop / 제어 루프)

Coverage đã có bộ nhớ (memory / 메모리) consistency/coherence, OoO/ROB/register renaming, speculation, bộ nhớ đệm (cache / 캐시)/prefetch/replacement, NUMA/interconnect, TLB/page walk/virtualization và SIMD/GPU thực thi (execution / 실행).

Vòng này chuẩn gốc (canonical / 정본) hóa:

- `07_power_thermal_dvfs_and_sustained_performance.md`

Chapter mới thêm lập luận (reasoning / 추론) đường dẫn (path / 경로):

```text
workload activity
→ switching / power / heat
→ voltage-frequency operating point
→ thermal/power controller
→ boost / throttling
→ sustained throughput
```

Điểm mới quan trọng là phân biệt peak benchmark với steady-state sức chứa (capacity / 용량). Thermal inertia, leakage phản hồi (feedback / 피드백), gói (package / 패키지) power ngân sách (budget / 예산) và cooling đường dẫn (path / 경로) có thể làm hành vi (behavior / 동작) đổi theo thời gian dù nhị phân (binary / 이진)/tải công việc (workload / 워크로드) không đổi.

**Status:** strong. Hardware-prefetch pathology tiếp tục thuộc bộ nhớ đệm (cache / 캐시) hierarchy trừ khi sau này đủ độc lập để thành đơn vị sở hữu (owner / 오너) mới.

## 5. Operating Các hệ thống (systems / 시스템들) — synchronization, tài nguyên (resource / 자원) pressure và khả năng quan sát (observability / 관측 가능성) đều có đơn vị sở hữu (owner / 오너)

OS advanced cover kernel thực thi (execution / 실행) contexts/syscall, scheduler/run hàng đợi (queue / 큐), bộ nhớ (memory / 메모리) pressure, virtual bộ nhớ (memory / 메모리)/TLB, filesystem crash consistency, async I/O/DMA, bộ chứa (container / 컨테이너) isolation và RCU/seqlock/safe reclamation.

Vòng này chuẩn gốc (canonical / 정본) hóa thêm:

- `08_ebpf_tracing_kernel_observability_and_safety.md`

Lập luận (reasoning / 추론) đường dẫn (path / 경로) mới:

```text
kernel event / hook
→ verifier safety gate
→ bounded program + helper contract
→ map / aggregation / event transport
→ user-space evidence
→ correlation với application symptom
```

Chapter làm rõ hook ngữ nghĩa (semantics / 의미론), verifier lập luận (reasoning / 추론), JIT/overhead, per-CPU trạng thái (state / 상태), ring-buffer mất mát (loss / 손실), cardinality pressure, sampling độ lệch (bias / 편향) và observer tác động (effect / 효과). Khả năng quan sát (observability / 관측 가능성) không còn được coi là “chọn công cụ (tool / 도구)”, mà là thu bằng chứng (evidence / 증거) tại đúng chuyển tiếp trạng thái (state transition / 상태 전이) với overhead được hiểu.

Kernel packet ngữ nghĩa (semantics / 의미론) được đặt ở Mạng (network / 네트워크) advanced để tránh duplicate; OS chapter sở hữu thực thi (execution / 실행)/an toàn (safety / 안전)/instrumentation cơ chế (mechanism / 메커니즘).

**Status:** strong.

## 6. Programming Languages & Thời gian chạy (runtime / 런타임) — strong

Coverage mạnh ở kiểu (type / 타입)/tác động (effect / 효과)/thời gian chạy (runtime / 런타임) đặc tả hợp đồng (contract / 계약), quyền sở hữu (ownership / 소유권), trình biên dịch (compiler / 컴파일러) IR/SSA, JIT/deoptimization, GC barriers, coroutine, ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) và FFI/bản địa (native / 네이티브) ranh giới (boundary / 경계).

Cross-layer tính đồng thời (concurrency / 동시성) hiện có đơn vị sở hữu (owner / 오너) rõ:

```text
Architecture → visibility/order cost
OS → scheduling/wait/reclamation
Language → happens-before/ownership
Runtime → task/coroutine execution
```

Không cần mở gốc (root / 루트) Tính đồng thời (concurrency / 동시성) thư viện (library / 라이브러리). Profile-guided/AOT/JIT details chỉ nên deepen trình biên dịch (compiler / 컴파일러)/JIT chapters nếu cùng bất biến (invariant / 불변식).

**Status:** strong.

## 7. Tính đồng thời (concurrency / 동시성) — integrated, không phải isolated thư viện (library / 라이브러리)

Tính đồng thời (concurrency / 동시성) vẫn được phân theo lớp trừu tượng (abstraction / 추상화) đơn vị sở hữu (owner / 오너). `90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md` là chuẩn gốc (canonical / 정본) proof đường dẫn (path / 경로) từ bộ nhớ đệm (cache / 캐시)/coherence → thứ tự (ordering / 순서) → ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) → bug/thời gian tồn tại (lifetime / 수명).

RCU/seqlock chapter ở OS và bộ nhớ (memory / 메모리) consistency chapter ở Kiến trúc (architecture / 아키텍처) đã đóng gap lớn về reclamation/thứ tự (order / 순서). Phân tán (distributed / 분산) causality vẫn thuộc Networks & Phân tán (distributed / 분산) Các hệ thống (systems / 시스템들).

**Status:** strong và đúng ranh giới (boundary / 경계).

## 8. Dữ liệu (data / 데이터) & Databases — từ OLTP internals tới adaptive analytical thực thi (execution / 실행)

Cơ sở dữ liệu (database / 데이터베이스) advanced hiện có MVCC/WAL/khôi phục (recovery / 복구), khóa (lock / 잠금) manager/serializable isolation, B+Cây (tree / 트리), LSM, buffer pool, cost-based optimizer, phép nối (join / 조인)/vectorized thực thi (execution / 실행), phân tán (distributed / 분산) transactions và columnar analytical lưu trữ (storage / 저장소).

Vòng này chuẩn gốc (canonical / 정본) hóa:

- `09_adaptive_query_execution_runtime_filters_skew_and_reoptimization.md`

Lập luận (reasoning / 추론) đường dẫn (path / 경로):

```text
logical query
→ compile-time statistics
→ initial physical plan
→ runtime cardinality/distribution evidence
→ safe adaptation boundary
→ revised physical strategy
→ same logical semantics
```

Chapter đóng gap giữa optimizer hypothesis và thời gian chạy (runtime / 런타임) reality: stale/correlated statistics, broadcast-vs-partitioned phép nối (join / 조인), thời gian chạy (runtime / 런타임) filters, skew splitting, bộ nhớ (memory / 메모리) grant/spill, stage materialization và re-optimization. Bất biến (invariant / 불변식) cốt lõi là vật lý (physical / 물리적) chiến lược (strategy / 전략) được phép đổi nhưng truy vấn (query / 쿼리) kết quả (result / 결과) ngữ nghĩa (semantics / 의미론) không được đổi.

Analytical lộ trình học (learning path / 학습 경로) giờ có thể đọc:

```text
optimizer estimate
→ join/operator execution
→ columnar physical layout/pruning
→ runtime adaptation under skew/pressure
```

**Status:** strong cho OLTP + analytical internals.

## 9. Networks — từ routing điều khiển (control / 제어) plane xuống host packet queues

Foundation đã cover Ethernet/IP/routing, TCP/UDP/congestion, DNS/HTTP/TLS, sockets/IPv6/NAT/firewall/VPN, BGP và HTTP/2–HTTP/3/QUIC. Advanced có phân tán (distributed / 분산) protocols, thời gian (time / 시간)/causality, multi-region và BGP/routing chính sách (policy / 정책).

Vòng này chuẩn gốc (canonical / 정본) hóa:

- `08_kernel_packet_path_qdisc_nic_offload_and_observability.md`

Trạng thái (state / 상태)/hàng đợi (queue / 큐) đường dẫn (path / 경로):

```text
application write
→ socket buffer / transport state
→ routing/policy
→ qdisc
→ driver/NIC queue
→ wire
→ RX queue / interrupt-polling
→ socket receive buffer
→ application read
```

Chapter phân biệt syscall progress với wire delivery, giải thích qdisc/bufferbloat, driver/NIC rings, RSS/ECMP skew, interrupt/NAPI-style batching, segmentation/coalescing/checksum offload và vì sao host packet capture có thể khác wire reality.

Mạng (network / 네트워크) diagnosis giờ có thể nối điều khiển (control / 제어) plane `BGP → RIB/FIB` với mặt phẳng dữ liệu (data plane / 데이터 플레인) `socket → qdisc → NIC → wire` và OS bằng chứng (evidence / 증거) `eBPF/scheduler/DMA`.

**Status:** strong cho vận chuyển (transport / 전송), routing chính sách (policy / 정책) và host packet-path môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론).

## 10. Phân tán (distributed / 분산) Các hệ thống (systems / 시스템들) — strong

Thất bại (failure / 실패) detectors, membership/gossip, lease/fencing, consensus/reconfiguration, CRDT/nhân quả (causal / 인과적) consistency, clocks/causality, exactly-once ambiguity, phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션) ngữ nghĩa (semantics / 의미론) và multi-region authority/failover đã có lập luận (reasoning / 추론) đường dẫn (path / 경로) rõ.

Gap còn lại chủ yếu là worked proofs/trường hợp (case / 사례) studies: joint-consensus/reconfiguration và queueing under partition. Các gap này nên deepen chapter hiện có trước, không mặc định mở tệp (file / 파일) mới.

**Status:** strong.

## 11. Bảo mật (security / 보안) & Độ tin cậy (reliability / 신뢰성) — từ preventive controls tới sản phẩm tạo ra (artifact / 산출물) trust và sự cố (incident / 인시던트) bằng chứng (evidence / 증거)

Bảo mật (security / 보안) advanced đã có bảo mật (security / 보안) boundaries/attack chains, crypto composition, PKI/mTLS, OAuth/OIDC, bộ nhớ (memory / 메모리) an toàn (safety / 안전)/sandbox, trình duyệt (browser / 브라우저) isolation, secrets/KMS/HSM và detection/forensics.

Vòng này chuẩn gốc (canonical / 정본) hóa:

- `08_software_supply_chain_provenance_signing_and_build_trust.md`

Trust đường dẫn (path / 경로):

```text
source/dependency
→ builder/workflow
→ artifact digest
→ provenance / attestation
→ signing authority
→ registry
→ deployment policy
→ runtime artifact
```

Chapter phân biệt digest, signature, provenance, SBOM và chính sách (policy / 정책); giải thích hermetic vs reproducible bản dựng (build / 빌드), phụ thuộc (dependency / 의존성) resolution, runner authority, mutable tag vs digest, build-cache poisoning, short-lived định danh (identity / 식별자), transparency bằng chứng (evidence / 증거), revocation và sự cố (incident / 인시던트) containment theo provenance đồ thị (graph / 그래프).

Điểm cốt lõi: signing không chứng minh sản phẩm tạo ra (artifact / 산출물) tốt; nó chứng minh một authority đã ký statement. Bảo mật (security / 보안) phụ thuộc vào ai được phép tạo statement, verifier chính sách (policy / 정책) và khả năng cắt authority sau compromise.

**Status:** strong cho preventive + detective + software supply-chain trust.

## 12. Độ tin cậy (reliability / 신뢰성) — thất bại (failure / 실패) containment vẫn cross-domain

Thử lại (retry / 재시도), hết thời gian chờ (timeout / 타임아웃), circuit breaker, bulkhead, backpressure, tải (load / 로드) shedding và lỗi (error / 오류) ngân sách (budget / 예산) tiếp tục được chia giữa Bảo mật (security / 보안)/Độ tin cậy (reliability / 신뢰성) foundation và Software Các hệ thống (systems / 시스템들) môi trường vận hành (production / 운영 환경) mechanisms.

Chuẩn gốc (canonical / 정본) vòng phản hồi (feedback loop / 피드백 루프):

```text
arrival tăng
→ queue
→ latency
→ timeout
→ retry
→ arrival tăng thêm
→ overload / cascading failure
```

Không tạo Độ tin cậy (reliability / 신뢰성) gốc (root / 루트) thư viện (library / 라이브러리) mới. Bảo mật (security / 보안) controls như registry/signing/định danh (identity / 식별자) phụ thuộc (dependency / 의존성) cũng phải được đọc theo fail-open/fail-closed và availability phụ thuộc (dependency / 의존성).

**Status:** strong.

## 13. Software Các hệ thống (systems / 시스템들) & Hiệu năng (performance / 성능) — single host tới fleet economics

Queueing/backpressure, sức chứa (capacity / 용량)/admission, caching, tải (load / 로드) balancing/pools, sự kiện (event / 이벤트) streams, idempotency, lược đồ (schema / 스키마) evolution và fleet profiling/chi phí (cost / 비용) attribution đã có coverage tốt.

Fleet chapter đã mở rộng lập luận (reasoning / 추론) từ single yêu cầu (request / 요청) sang cohort/hardware/tenant:

```text
useful demand
→ distributed resource consumption
→ placement/skew/headroom
→ SLO outcome
→ cost attribution
→ capacity/architecture decision
```

DVFS chapter bổ sung lower-layer explanation cho sustained sức chứa (capacity / 용량); kernel packet đường dẫn (path / 경로) bổ sung mạng (network / 네트워크) hàng đợi (queue / 큐) đơn vị sở hữu (owner / 오너); AI suy luận (inference / 추론) disaggregation bổ sung accelerator trạng thái (state / 상태)/hàng đợi (queue / 큐) trường hợp (case / 사례) study.

**Status:** strong cho Hiệu năng (performance / 성능) Kỹ thuật (engineering / 엔지니어링) và Hệ thống (system / 시스템) Thiết kế (design / 설계) lập luận (reasoning / 추론) mà không tách gốc (root / 루트) thư viện (library / 라이브러리).

## 14. Hệ thống (system / 시스템) Thiết kế (design / 설계) — vẫn thuộc Software Các hệ thống (systems / 시스템들)

Chuẩn gốc (canonical / 정본) entry điểm (point / 지점) vẫn là `08_software_systems/07_system_decomposition_services_and_boundaries.md`. Ranh giới (boundary / 경계) được lập luận (reasoning / 추론) bằng bất biến (invariant / 불변식)/quyền sở hữu trạng thái (state ownership / 상태 소유권), thất bại (failure / 실패), sức chứa (capacity / 용량), bảo mật (security / 보안) authority và economics; không bằng checklist technology.

Các expansion mới củng cố Hệ thống (system / 시스템) Thiết kế (design / 설계) theo quyền sở hữu trạng thái (state ownership / 상태 소유권):

```text
network packet → queue ownership
supply chain → artifact authority ownership
AI inference → KV state ownership
adaptive DB → execution-state adaptation boundary
```

Đây là mô hình tư duy (mental model / 사고 모델) bền hơn sản phẩm (product / 제품) kiến trúc (architecture / 아키텍처) diagram.

**Status:** strong.

## 15. Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) — changeability + debt economics

Kiến trúc (architecture / 아키텍처) evolution, modularity economics, API/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성), di chuyển (migration / 마이그레이션) máy trạng thái (state machine / 상태 머신), testing, triển khai (deployment / 배포) an toàn (safety / 안전) và technical-debt economics/Goodhart đã mạnh.

Supply-chain chapter cross-link Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) ở thay đổi (change / 변경) tiến trình (process / 프로세스) nhưng không duplicate: Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) sở hữu safe evolution/triển khai (deployment / 배포); Bảo mật (security / 보안) sở hữu trust/authority/provenance của sản phẩm tạo ra (artifact / 산출물) đường dẫn (path / 경로).

Gap organizational thiết kế (design / 설계) hoặc portfolio modernization chỉ nên mở khi có trường hợp (case / 사례) study đủ lớn và independent bất biến (invariant / 불변식).

**Status:** strong.

## 16. AI Foundations — suy luận (inference / 추론) quyền sở hữu trạng thái (state ownership / 상태 소유권) đã sâu hơn

AI Foundations trước đây có mô hình (model / 모델) vòng đời (lifecycle / 생명주기), Transformer/KV-cache internals và phân tán (distributed / 분산) huấn luyện (training / 학습). Vòng này chuẩn gốc (canonical / 정본) hóa:

- `03_inference_disaggregation_prefill_decode_and_kv_cache_placement.md`

Lập luận (reasoning / 추론) đường dẫn (path / 경로):

```text
admission
→ prefill
→ KV state creation
→ placement / transfer / ownership
→ decode scheduling
→ token stream
→ cancellation / cleanup
```

Chapter phân biệt TTFT, inter-token độ trễ (latency / 지연 시간) và total completion thời gian (time / 시간); prefill compute profile với decode bộ nhớ (memory / 메모리)/KV profile; colocated vs disaggregated serving; KV handoff; continuous batching; prefix reuse/phiên bản (version / 버전) định danh (identity / 식별자); thử lại (retry / 재시도)/cancellation ambiguity; bộ nhớ (memory / 메모리) headroom và phase chuyển tiếp (transition / 전이) khi hàng đợi (queue / 큐)/KV pressure tăng.

Điểm quan trọng là disaggregation không chỉ là triển khai (deployment / 배포) tối ưu hóa (optimization / 최적화). Nó đổi quyền sở hữu trạng thái (state ownership / 상태 소유권) ranh giới (boundary / 경계) và vì vậy tạo giao thức (protocol / 프로토콜) cho publication, transfer, thử lại (retry / 재시도), cleanup và thất bại (failure / 실패) khôi phục (recovery / 복구).

**Status:** strong cho foundational AI các hệ thống (systems / 시스템들). Accelerator trình biên dịch (compiler / 컴파일러)/kernel scheduling vẫn là gap tiềm năng nhưng chỉ nên mở nếu lập luận (reasoning / 추론) vượt khỏi SIMD/GPU + suy luận (inference / 추론)/huấn luyện (training / 학습) chapters hiện tại.

## 17. Cross-layer Connections — giữ bốn chuẩn gốc (canonical / 정본) tích hợp (integration / 통합) paths

`90_connections/advanced/` tiếp tục giữ bốn đường dẫn (path / 경로) chính:

```text
Debugging:
symptom → invariant → evidence → lower layer → fix/containment

End-to-end request:
DNS/TCP-or-QUIC/TLS → routing/proxy/LB → runtime → pools/DB/storage
+ socket/qdisc/NIC queues
+ retry → timeout → overload/backpressure

Correctness:
CPU cache/coherence → ordering → language memory model → concurrency/lifetime bug

Durability:
application commit → MVCC/WAL → filesystem/storage → replication authority
```

Không tăng liên kết (connection / 연결) chapter count chỉ để nhắc các chapter mới. Packet đường dẫn (path / 경로) được hấp thụ vào đường đi của yêu cầu (request path / 요청 경로); supply-chain authority được hấp thụ vào debugging/bảo mật (security / 보안) bằng chứng (evidence / 증거) khi sự cố (incident / 인시던트) liên quan sản phẩm tạo ra (artifact / 산출물); DVFS đi vào hiệu năng (performance / 성능) lower tầng (layer / 계층); suy luận (inference / 추론) quyền sở hữu trạng thái (state ownership / 상태 소유권) cross-link hàng đợi (queue / 큐)/sức chứa (capacity / 용량)/distributed-state chapters.

**Status:** strong.

## 18. Repository hygiene và branch chiến lược (strategy / 전략)

Chuẩn gốc (canonical / 정본) parent vẫn là `feat/computer-science`. Vòng này làm việc trên child branch `feat/computer-science-depth-expansion` để không can thiệp kiểm tra (audit / 감사)/merge đang diễn ra ở parent/main.

Không tạo gốc (root / 루트) thư viện (library / 라이브러리) mới. Không tạo tệp (file / 파일) `_final`, `_updated`, `_version2` trong chuẩn gốc (canonical / 정본) documentation cây (tree / 트리). Các chapter mới đều nằm trong đơn vị sở hữu (owner / 오너) lĩnh vực (domain / 도메인) hiện có và README lĩnh vực (domain / 도메인) đã được cập nhật để tránh orphan tệp (file / 파일).

## 19. Coverage còn thiếu sau expansion

Các gap đáng xem tiếp nhưng chưa mặc định cần chapter mới:

```text
Architecture:
- hardware prefetch pathology / bandwidth pollution case studies

OS:
- selected scheduler/NUMA/network interaction case studies

Programming Languages:
- deeper AOT/JIT/profile-guided optimization only if current JIT chapter becomes overloaded

Database:
- adaptive execution worked cases across distributed engines

Distributed:
- joint-consensus/reconfiguration worked proof
- queueing/admission behavior under partition

Security:
- deeper supply-chain incident case studies
- detection-quality measurement without turning into SIEM metrics catalog

Software Systems:
- causal fleet profiling and autoscaling-control-loop case studies

AI systems:
- accelerator compiler/kernel scheduling
- heterogeneous memory and KV migration case study

Cross-layer:
- incident case studies that reuse existing four paths instead of creating generic connection chapters
```

Nguyên tắc tiếp tục vẫn là: **absorb vào tệp chuẩn gốc (canonical file / 정본 파일) nếu cùng bất biến (invariant / 불변식); chỉ tăng chapter count khi topic có mô hình tư duy (mental model / 사고 모델) riêng, phụ thuộc (dependency / 의존성) rộng và đơn vị sở hữu (owner / 오너) ranh giới (boundary / 경계) rõ**.

## 20. Cổng chất lượng (quality gate / 품질 게이트) cho vòng tiếp theo

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

Prose là phần chính; bullet chỉ dùng cho danh sách (list / 목록) tự nhiên. Thuật ngữ English/Korean được giữ khi hữu ích nhưng phần giải thích phải là tiếng Việt tự nhiên. API/sản phẩm (product / 제품)/phiên bản (version / 버전) chỉ neo cơ chế (mechanism / 메커니즘), không thay cơ chế (mechanism / 메커니즘).

## Kết luận

Sau vòng độ sâu (depth / 깊이) expansion này, `computer_science/` không chỉ rộng hơn mà có thêm các trạng thái (state / 상태)/điều khiển (control / 제어) các mô hình (models / 모델들) còn thiếu: thông tin (information / 정보)/randomness/xác minh (verification / 확인) ở formal CS; sustained power/thermal điều khiển (control / 제어) ở Kiến trúc (architecture / 아키텍처); safe động (dynamic / 동적) tracing ở OS; adaptive thực thi (execution / 실행) ở Cơ sở dữ liệu (database / 데이터베이스); host packet queues/offload ở Mạng (network / 네트워크); sản phẩm tạo ra (artifact / 산출물) provenance/authority ở Bảo mật (security / 보안); và KV-state quyền sở hữu (ownership / 소유권)/disaggregation ở AI suy luận (inference / 추론).

Giá trị của expansion không nằm ở số tệp (file / 파일). Mỗi chapter mới tồn tại vì nó thêm một bất biến (invariant / 불변식) hoặc máy trạng thái (state machine / 상태 머신) đủ độc lập để cải thiện lập luận (reasoning / 추론) xuyên lĩnh vực (domain / 도메인), đồng thời vẫn trỏ về đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자) thay vì tạo thư viện (library / 라이브러리) cạnh tranh.