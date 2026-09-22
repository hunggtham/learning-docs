# Knowledge connections: DevOps / Platform Engineering ↔ Computer Science

Thư viện này cố ý không sở hữu toàn bộ kiến thức hệ thống bên dưới. File này chỉ ra khi nào nên rời DevOps layer để đọc canonical chapter sâu hơn.

## 1. Container và Linux

Khi câu hỏi là “Dockerfile nên build ra sao, image nên promote thế nào, probe/resource nên cấu hình theo operational contract nào”, đọc [`03_containers`](../03_containers/00_container_image_runtime_and_builds.md).

Khi câu hỏi chuyển sang “namespace thật sự cô lập gì, cgroup enforce CPU/memory ra sao, capability/seccomp cắt quyền kernel thế nào”, đọc [OS advanced — containers/namespaces/cgroups](../../computer_science/03_operating_systems/advanced/06_containers_namespaces_cgroups_capabilities_and_seccomp.md).

Process, syscall, virtual memory, filesystem và scheduling thuộc [OS foundation](../../computer_science/basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) và [OS advanced](../../computer_science/03_operating_systems/advanced/README.md).

## 2. Kubernetes và distributed systems

Kubernetes chapter giải control loop, controller ownership, workload scheduling và operational failure. Khi cần hiểu vì sao heartbeat không chứng minh node chết, lease/fencing hay consensus store hoạt động thế nào, chuyển sang [Networks & Distributed Systems advanced](../../computer_science/06_networks_distributed_systems/advanced/README.md).

Các connection trực tiếp gồm [failure detectors](../../computer_science/06_networks_distributed_systems/advanced/01_failure_detectors_membership_and_gossip.md), [leases/fencing/split brain](../../computer_science/06_networks_distributed_systems/advanced/02_leases_fencing_tokens_and_split_brain_prevention.md) và [consensus/log replication](../../computer_science/06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md).

## 3. CI/CD và Software Engineering

DevOps delivery chapters quan tâm flow, artifact identity, evidence và automation. Khi cần lý thuyết compatibility/refactoring/test architecture, đọc [Software Engineering advanced](../../computer_science/09_software_engineering/advanced/README.md).

Safe rollout nối trực tiếp [deployment safety, canary, blue-green, flags và rollback](../../computer_science/09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md). Production verification nối [test architecture và production verification](../../computer_science/09_software_engineering/advanced/04_test_architecture_contract_mutation_property_and_production_verification.md).

## 4. Network platform và networking fundamentals

DevOps request-path chapter tập trung DNS/TLS/proxy/load balancer debugging. Protocol semantics và distributed networking sâu hơn thuộc [Networks & Distributed Systems](../../computer_science/06_networks_distributed_systems/advanced/README.md).

Khi symptom là connection/timeout, bắt đầu ở request path. Khi câu hỏi là ordering, failure semantics, causal consistency hoặc consensus, chuyển sang Computer Science.

## 5. Security platform và Security & Reliability

DevOps security chapter biến identity, secret, signature và policy thành secure default. Cryptographic mechanism, PKI validation, OAuth/OIDC và KMS internals nằm tại [Security & Reliability advanced](../../computer_science/07_security_reliability/advanced/README.md).

Các liên kết quan trọng: [PKI/mTLS/service identity](../../computer_science/07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md), [OAuth/OIDC token lifecycle](../../computer_science/07_security_reliability/advanced/03_oauth_oidc_token_lifecycle_and_federation_threats.md), [secrets/KMS/HSM](../../computer_science/07_security_reliability/advanced/06_secrets_kms_hsm_rotation_and_envelope_encryption.md).

## 6. Reliability, SLO và failure semantics

SRE chapter nói cách đặt SLI/SLO, error budget, incident và capacity. Khi cần hiểu retry/idempotency/exactly-once, đọc [distributed transactions và failure semantics](../../computer_science/06_networks_distributed_systems/advanced/00_distributed_transactions_exactly_once_and_failure_semantics.md).

Khi cần nối reliability với security boundary, đọc [Computer Science learning route 4](../../computer_science/README.md).

## 7. Database operations

DevOps library không dạy database internals riêng. Connection pool, backup/restore và deployment migration được nhắc ở operational boundary. MVCC, WAL, lock, query/storage internals thuộc [Data & Databases advanced](../../computer_science/05_data_databases/advanced/README.md).

Điều này tránh viết lại database book bên trong platform book.

## 8. Performance

Khi metric cho thấy CPU throttling, page fault, I/O hoặc scheduler latency và cần đi xuống kernel/hardware, đọc OS/Architecture canonical docs. DevOps giữ symptom→evidence path; Computer Science giải mechanism.

## 9. AI/LLMOps

AI library trong `computer_science/02_artificial_intelligence/` đã có LLMOps/AI Engineering. DevOps Platform chỉ nên cung cấp capability chung như CI/CD, secrets, Kubernetes, observability và platform API. Những vấn đề model evaluation, vector/RAG/agent reliability thuộc AI domain để tránh duplicate.

## 10. Nguyên tắc quyết định nơi đặt nội dung mới

Nếu nội dung giải thích **cơ chế nền độc lập với operating platform** như consensus, page table, TLS validation hoặc WAL, đặt/cải thiện canonical Computer Science.

Nếu nội dung giải thích **cách tổ chức delivery, automation, control loop, production operation hoặc developer self-service** trên các cơ chế đó, đặt trong DevOps / Platform Engineering.

Nếu một chapter mới chỉ mô tả một product/tool mà không tạo mental model mới, không nên tạo chapter riêng; thêm ví dụ vào chapter concept tương ứng là đủ.

## 11. Route reasoning 1 — từ latency user xuống scheduler/kernel

Khi user báo request chậm, không nên nhảy ngay xuống CPU flame graph. Đi từ contract ngoài vào trong:

```text
user-observed latency
→ edge / DNS / TLS / proxy
→ service routing
→ application queue / connection pool
→ downstream dependency
→ container cgroup pressure
→ node scheduler / memory / I/O
```

DevOps chapters giữ phần symptom, timeout budget, telemetry, resource boundary và production evidence. Khi evidence đã chỉ rõ scheduler latency, reclaim/page fault hoặc filesystem behavior là bottleneck, lúc đó chuyển sang OS canonical để hiểu internals.

Boundary này ngăn hai lỗi đối lập: operator chỉ nhìn dashboard cấp cao và không hiểu kernel, hoặc operator lao xuống kernel quá sớm khi failure thực ra là config/dependency.

## 12. Route reasoning 2 — từ commit đến bytes đang phục vụ production

Một release có thể được truy theo chuỗi:

```text
commit
→ reviewed source state
→ build inputs / dependency lock / builder
→ artifact digest + provenance
→ registry
→ desired deployment state
→ runtime image digest
→ workload version serving traffic
```

Mỗi arrow là một trust/identity boundary. Delivery System sở hữu reproducibility và artifact identity; Security sở hữu trust policy/provenance/signature; GitOps/Kubernetes sở hữu desired→actual reconciliation; Observability xác nhận version nào thực sự tạo outcome.

Nếu production khác staging, route này giúp hỏi đúng thứ tự: bytes có giống không, config có giống contract không, runtime có resolve đúng digest không, data/dependency có khác không. Không rebuild artifact giữa chừng vì rebuild làm mất biến kiểm soát.

## 13. Route reasoning 3 — từ desired state đến control-loop conflict

IaC, Kubernetes, GitOps, HPA, autoscaler và operator đều có thể được nhìn như controller:

```text
desired state
→ observe current state
→ compute difference
→ act
→ observe again
```

Khi state dao động hoặc “bị đổi ngược”, câu hỏi đầu tiên là **ai sở hữu field/state này**. Nếu hai loop có desired state khác nhau, từng controller có thể hoàn toàn đúng cục bộ nhưng hệ thống không hội tụ.

Distributed Systems canonical giải các vấn đề consensus/failure detector/fencing khi chúng đi xuống cơ chế nền. DevOps/Platform Engineering giữ bài toán ownership, reconciliation latency, backoff, operational evidence và safe emergency override.

## 14. Route reasoning 4 — từ SLO đến topology/cost

SLO không chỉ là monitoring target. Nó truyền ngược thành yêu cầu kiến trúc:

```text
business impact
→ SLO / RPO / RTO
→ failure domain cần chịu
→ redundancy + capacity headroom
→ rollout / recovery strategy
→ tenancy / isolation boundary
→ cost
```

Nếu FinOps tối ưu chi phí mà không giữ failure headroom cần cho SLO, optimization là sai boundary. Nếu multi-region được chọn mà business chỉ cần RTO dài và dữ liệu có thể restore, có thể đang trả complexity/cost không cần thiết.

Vì vậy Platform Engineering kết nối Reliability với Economics: platform tier nên biểu diễn capability và failure contract, không chỉ kích thước CPU/RAM.

## 15. Route reasoning 5 — incident quay lại platform default

Một incident có giá trị lâu dài khi causal factor được chuyển thành system improvement:

```text
incident evidence
→ failure class
→ missing signal / unsafe default / missing guardrail
→ canonical fix
→ platform default / automation / runbook
→ verify recurrence risk giảm
```

Nếu năm team đều gặp cùng lỗi certificate rotation, solution không nên chỉ là năm postmortem. Platform có thể chuẩn hóa issuance/rotation/expiry telemetry. Nếu nhiều service OOM vì heap bằng đúng container limit, golden path/runtime guidance có thể encode native headroom.

Đây là connection quan trọng nhất giữa Production Practice và Platform Engineering: troubleshooting không kết thúc ở chữa service; failure lặp lại phải trở thành feedback cho shared capability.

## 16. Route reasoning 6 — từ overload tới admission, degradation và recovery

Một saturation incident nên được nhìn như chuỗi control decision chứ không chỉ biểu đồ CPU:

```text
arrival rate / concurrency tăng
→ queue + held resource tăng
→ latency tăng
→ timeout / retry khuếch đại load
→ admission / load shedding / brownout
→ protected core work giữ SLO
→ recovery ramp-up + backlog drain
```

SRE sở hữu capacity, retry budget, admission và degradation contract. Production Practice quan sát xem timeout có cancel work thật không, retry có tạo duplicate hay recovery có tạo second storm. Platform Engineering biến các cơ chế lặp lại thành default hoặc tier.

Khi cần formal queueing sâu hơn, chuyển sang Mathematics/Computer Science; DevOps giữ operational invariant: **không nhận work vượt khả năng rồi để tất cả chết chậm**.

## 17. Route reasoning 7 — từ identity tới effective authority

Security incident không nên dừng ở “token này của ai”. Chuỗi cần theo authority:

```text
caller identity
→ requested intent / target
→ authorization decision
→ delegated / automation identity
→ downstream capability
→ audit evidence
```

Đây là nơi confused deputy và identity propagation xuất hiện. Caller hợp lệ vẫn có thể khiến privileged platform controller làm action ngoài scope nếu request intent không được bind vào caller authorization.

Computer Science Security giải token/PKI/OIDC mechanism; DevOps/Platform giữ scope, workload identity, delegated control và evidence chain trên production path.

## 18. Route reasoning 8 — từ tenant isolation tới fairness và economics

Multi-tenancy không chỉ hỏi “resource có tách không” mà còn:

```text
shared resource
→ failure/threat boundary
→ quota
→ fairness khi contention
→ recovery concurrency
→ tenant-aware SLO
→ shared-cost/externality attribution
```

Một tenant dưới CPU quota vẫn có thể làm API server, log backend hoặc scheduler quá tải. Vì vậy isolation contract phải phủ cả control plane, data plane và shared service. Economics phải phản ánh externality đủ tốt để feedback quay về đúng owner.

SLO quyết định blast-radius budget; blast-radius budget quyết định cell/dedicated/shared topology; topology lại quyết định cost. Đây là vòng Reliability ↔ Platform ↔ FinOps, không phải ba chủ đề rời nhau.

## 19. Route reasoning 9 — từ self-service intent tới distributed lifecycle

Một nút `Create` trên portal thực chất có thể là workflow phân tán:

```text
intent + stable identity
→ authn/authz/policy
→ accepted operation
→ multiple side effects
→ partial failure / retry
→ reconcile existing state
→ Ready / Degraded / Failed
→ Day-2 resize / rotate / migrate / delete
```

Platform API chỉ trưởng thành khi idempotency đi qua toàn workflow, status phản ánh invariant thật và delete có retention semantics rõ. Portal/UI là bề mặt; mechanism là state machine + reconciliation + ownership.

Khi semantics chuyển sang exactly-once/idempotency/distributed transaction nền, đọc Distributed Systems canonical. Platform chapter giữ contract mà developer/operator cần để không phải hiểu mọi provider detail.

## 20. Route reasoning 10 — từ delivery constraint tới feedback delay

Flow engineering nên đi theo constraint chứ không theo tool đang dễ tối ưu nhất:

```text
work arrives
→ queue / WIP
→ current constraint
→ processing
→ feedback delay
→ rework / next decision
```

Nếu constraint là review queue, tăng build speed không đổi throughput. Nếu feedback production đến quá muộn, batch change tăng và rework đắt hơn. Nếu shared environment luôn 100% utilization, urgent change phải chờ dù tài nguyên nhìn “được tận dụng tốt”.

Foundations giữ operating-model reasoning; khi cần queueing theory chính thức có thể đọc Mathematics. Platform Engineering dùng kết quả này để quyết định chỗ nào nên self-service, chỗ nào cần reserve capacity và chỗ nào automation chỉ đang đẩy queue sang layer khác.

## 21. Route reasoning 11 — từ sensor tới decision: evidence phải có semantics và freshness

Một decision production không nên chỉ hỏi “dashboard đang hiển thị gì” mà cần đi qua chuỗi:

```text
system event/state
→ instrumentation
→ export / sampling / buffering
→ backend ingestion
→ query / aggregation
→ displayed evidence
→ human/controller decision
```

Failure có thể xuất hiện ở bất kỳ arrow nào. `0 errors` có thể là zero thật hoặc missing series; log có thể duplicate; trace sample có bias; dashboard có thể stale. Vì vậy evidence cần biết metric type, population/sample, schema version và freshness.

Observability chapter sở hữu sensor semantics. Production Practice sở hữu cách evidence được dùng để bác bỏ hypothesis. Reliability/Security quyết định signal nào đủ quan trọng để loss-of-signal tự nó trở thành incident.

## 22. Route reasoning 12 — từ mitigation tới recovery convergence

Mitigation thành công chỉ là đầu recovery loop:

```text
user impact reduced
→ writer/traffic ownership stable
→ backlog / deferred work drain
→ data/business invariant verify
→ optional capability staged restore
→ degraded mode exit
→ steady state + headroom restored
```

Nếu mở toàn bộ backlog ngay sau failover, recovery có thể tạo outage thứ hai. Nếu endpoint 200 nhưng data giữa các system lệch, recovery chưa complete. Nếu old writer chưa fenced, failover có thể tạo split brain.

Incident/DR chapter giữ sequencing, exit criteria và validation; Distributed Systems canonical giải fencing/consistency mechanism; Platform Engineering có nhiệm vụ biến recovery pattern lặp lại thành workflow có idempotency, status và safe defaults.

## 23. Route reasoning 13 — từ user contract tới SLO measurement correctness

Một SLO có thể nhìn đẹp nhưng sai nếu denominator hoặc measurement window không đại diện user journey:

```text
user journey
→ valid-event population
→ good/bad semantics
→ sensor boundary
→ aggregation/window
→ SLO state
→ engineering action
```

Low-traffic service cần xem sample size/synthetic signal; asynchronous workload cần age/deadline chứ không chỉ request latency; composite journey cần vẽ mandatory/fallback path trước khi ghép availability.

Observability/SRE giữ measurement semantics. Architecture quyết định path nào thật sự critical; Platform/Security cần biết SLO state có đáng tin trước khi dùng nó để freeze release hay tự động thay policy.

## 24. Route reasoning 14 — từ self-service operation tới cancellation, compensation và adoption

Distributed platform workflow không dừng ở create/retry:

```text
intent
→ long-running operation
→ partial side effects
→ cancel / timeout / failure
→ observe external state
→ compensate | adopt | cleanup
→ reconcile ownership
```

Cancellation có thể chỉ dừng controller chứ không đảo external API. Compensation phục hồi invariant nhưng không nhất thiết trở lại exact state cũ. Resource orphan cần adoption/quarantine semantics thay vì xóa mù.

Khi platform control plane tự hỏng, route còn phải kéo dài tới bootstrap path: state backend, identity, artifact và recovery controller nào tồn tại ngoài failure domain. Đây là connection trực tiếp giữa Platform Engineering, Distributed Systems và Incident/DR.

## 25. Route reasoning 15 — từ secret/policy change tới security migration lifecycle

Security change cũng là state transition:

```text
new credential/policy
→ staged distribution or audit
→ consumer/policy evidence
→ cutover/enforce
→ revoke old / remove compatibility
→ verify no stale authority
```

Rotation chưa complete nếu consumer vẫn dùng credential cũ. Policy audit mode chưa bảo vệ invariant nếu không có đường sang enforce. Break-glass chưa kết thúc nếu privileged session/token chưa expire.

Security chapter giữ trust/authority lifecycle; Observability cung cấp evidence; Platform biến pattern này thành default workflow để security không phụ thuộc thao tác thủ công khó kiểm chứng.

## 26. Route reasoning 16 — từ symptom tới causal confidence

Production investigation trưởng thành đi xa hơn timeline:

```text
symptom
→ hypothesis
→ expected mechanism
→ detector / cohort
→ intervention or counterfactual
→ observed response
→ causal confidence + uncertainty
```

Deploy trước incident là correlation; causal graph phải giải thích arrow. Restart giúp service khỏe chỉ chứng minh một state nào đó bị reset, không tự chứng minh memory leak. Fault injection chỉ có giá trị khi fault boundary và control cohort được verify.

Production Practice giữ discipline này; Observability quyết định detector coverage; Incident process điều phối state mutation để intervention của nhiều operator không phá chính evidence đang dùng để suy luận.

## 27. Route reasoning 17 — từ dependency latency tới isolation và load amplification

Một dependency chậm có thể trở thành failure của caller trước khi dependency chết hoàn toàn:

```text
slow/error dependency
→ held connection/thread/concurrency
→ queue tăng
→ timeout
→ retry/hedge amplification
→ caller saturation
→ circuit breaker / bulkhead / shedding
→ controlled recovery probes
```

Network chapter giữ connection/deadline/retry/breaker/bulkhead semantics. SRE giữ admission và overload budget. Distributed Systems giữ idempotency/failure ambiguity khi attempt bị lặp. Platform có thể chuẩn hóa default nhưng không thể chọn threshold đúng nếu không biết workload/dependency contract.

Điểm quan trọng là resilience mechanism cũng là traffic generator. Retry, hedge và half-open probe phải được tính vào downstream load thay vì coi chúng là “free reliability”.

## 28. Route reasoning 18 — từ schema change tới migration convergence

Một release stateful nên được nhìn như workflow dài hơn deployment:

```text
expand compatible schema/contract
→ deploy code hiểu mixed state
→ backfill / dual-write / shadow-read
→ detect discrepancy + reconcile
→ consumer adoption evidence
→ cutover source of truth
→ compatibility window
→ contract old state
```

CI/CD giữ orchestration/evidence và rollback compatibility. Database canonical giải lock/WAL/MVCC/storage internals. Distributed Systems giải dual-write/idempotency ambiguity. Observability phải đo lag, mismatch và old-path usage.

Migration hoàn tất khi data và consumer dependency đã converge, không phải khi DDL/job/deploy trả exit code 0.

## 29. Route reasoning 19 — từ telemetry amplification tới observability survivability

Observability có thể trở thành amplifier của incident:

```text
application fault
→ log/span/cardinality volume tăng
→ collector/backend queue tăng
→ ingestion/query saturation
→ evidence drop/stale
→ operator mất visibility
```

Observability chapter giữ priority, retention, cardinality và backend multi-tenancy. FinOps nối signal driver với cost. Multi-tenancy đặt quota/fairness cho ingestion/query. Production Practice phải kiểm tra sensor health trước khi dùng dashboard im lặng làm negative evidence.

Mục tiêu không phải giữ mọi byte telemetry mà là bảo vệ **minimum diagnostic capability** khi hệ thống đang xấu nhất.

## 30. Route reasoning 20 — từ platform control-plane loss tới safe recovery

Platform DR không chỉ là restore database:

```text
control-plane failure
→ bootstrap identity/artifact/state access
→ restore state checkpoint
→ discover external world
→ adopt/reconcile ownership
→ safe/read-only mode
→ prioritized recovery reconciliation
→ staged mutation enablement
→ full self-service
```

Platform Engineering giữ state-machine/ownership/bootstrap semantics. Incident/DR giữ recovery ordering và drill. Security giữ break-glass authority. Multi-tenancy giữ priority/reservation để recovery của một tenant hoặc bulk create mới không starve control-plane work quan trọng.

Điểm kết thúc không phải portal HTTP 200 mà là state đủ đáng tin để mutation mới không tạo duplicate, orphan hoặc cross-tenant blast radius.