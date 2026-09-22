# Coverage Audit — DevOps / Platform Engineering Knowledge Library

## 1. Conceptual boundary

Library sở hữu kiến thức về delivery system, infrastructure lifecycle, orchestration usage, GitOps, observability/SRE, security guardrail, platform product và production operations. Library **không** sở hữu internals nền đã có canonical home trong `computer_science/`.

Các phần cố ý cross-link thay vì duplicate gồm kernel/process/filesystem internals, namespaces/cgroups internals, distributed consensus/ordering, cryptographic protocol, PKI internals, database internals và software architecture/test/deployment theory ở mức Computer Science.

Boundary được giữ nguyên qua các vòng đào sâu. Không tạo thêm root library, không tách chapter theo tên sản phẩm và không biến DevOps thành catalog Docker/Kubernetes/Terraform/cloud provider.

## 2. Dependency audit

Dependency chính hiện tại:

```text
00 Foundations
  ↓
01 Runtime Foundations
  ↓
02 Delivery System
  ↓
03 Containers ───────┐
  ↓                  │
04 IaC + Cloud       │
  ↓                  │
05 Kubernetes ◄──────┘
  ↓
06 GitOps
  ↓
07 Observability / SRE
  ↓
08 Security / Governance
  ↓
09 Platform Engineering
  ↓
10 Production Practice
```

Security thực tế là concern xuyên suốt, nhưng được đặt sau các mechanism chính để người đọc biết identity/policy đang bảo vệ cái gì. Observability cũng xuyên suốt nhưng được học sau workload/control loop để telemetry có context.

Dependency không được hiểu như “học xong phần trước mới được đọc phần sau”. Mỗi chapter vẫn giải thích đủ context cục bộ để người đọc bắt đầu tại đó. Sơ đồ trên chỉ biểu diễn mental model nào được tái sử dụng ở phần sau.

## 3. Coverage matrix

| Capability | Coverage | Canonical dependency / note |
|---|---|---|
| DevOps operating model, flow, feedback, ownership | Đủ sâu cho platform reasoning | Có queue/WIP/batch-size, feedback quality và local-vs-system optimization |
| Platform Engineering boundary và cognitive load | Đủ sâu | `00_foundations`, `09_platform_engineering` |
| Linux process/service/signal/resource | Đủ cho production operations | Có effective-limit composition, accept queue, dirty-page/writeback và clock dependency; internals link `computer_science/03_operating_systems` |
| Linux pressure/throttling/evidence | Đủ applied | Có PSI, cgroup hierarchy, OOM scope, I/O service-rate reasoning; kernel internals vẫn giữ ở OS canonical |
| DNS/TCP/TLS/proxy/request path | Đủ cho troubleshooting | Có retry/deadline, negative cache, pool wait, MTU black-hole, HTTP/2 failure scope và load-balancer health propagation; protocol depth cross-link CS |
| Git/change flow | Đủ theo delivery context | Không biến thành Git command manual |
| Reproducible/hermetic build, artifact identity, cache trust | Đủ sâu | Có hidden nondeterminism, build-time network, independent rebuild, platform target identity và generated-code/toolchain inputs |
| CI/CD, flaky tests, concurrency, stale evidence, migration safety | Đủ sâu | Có superseded work, stale approval, shared-test-environment coupling, paused release state, comparative verification và merge-queue semantics |
| Container image/runtime/build/security/resource | Đủ production depth | Có image pull/recovery, runtime override precedence, startup spike, init semantics, writable-path contract, external side-effect boundary và config-cohort reasoning; internals link OS |
| IaC desired state/state/drift/modules/import/partial failure | Đủ sâu | Có unknown values, replacement ordering/headroom, external lookup stability, state recovery và plan-vs-actual policy boundary |
| Cloud IAM/network/compute/storage/failure domain | Đủ production depth | Có API rate-limit, zonal capacity scarcity, failure-state capacity, replication bandwidth/lag và private-endpoint composition; provider catalog không duplicate |
| Kubernetes control plane/reconciliation | Đủ sâu | Có optimistic concurrency, watch/resync, work queue/backoff, admission, API saturation, finalizer, owner graph, cache staleness, leader-election/fencing boundary và control-plane fairness |
| Kubernetes workload/network/storage/resources/autoscaling | Đủ sâu | Có schedulable-vs-aggregate capacity, PDB, topology, termination race, storage attach/fencing, ephemeral storage, Job/CronJob business semantics và endpoint-churn cost |
| GitOps | Đủ sâu | Có field ownership, rollback limits, revision-vs-serving distinction, deterministic rendering, prune semantics, readiness-vs-ordering, multi-cluster fan-out và decrypt trust path |
| Metrics/logs/traces/events/alerting | Đủ sâu | Có telemetry-pipeline failure, sampling, cardinality, percentile caveat và exemplars |
| SLI/SLO/error budget/capacity/backpressure | Đủ sâu | Có burn-rate reasoning, Little's Law, retry budget, admission/concurrency control, failover headroom, correlated failure, brownout và saturation cliff |
| Incident/postmortem/runbook | Đủ sâu | Có recovery-vs-root-cause, counterfactual/cohort reasoning, timeline uncertainty, negative evidence và multi-loop oscillation |
| Backup/RPO/RTO/DR/chaos | Đủ sâu | Có consistency boundary, PITR chain, DR bootstrap, fencing/failback và experiment validity |
| IAM/workload identity/secrets/policy | Đủ sâu ở platform layer | Có confused deputy, authority propagation, TOCTOU, revocation semantics và control-plane blast radius; crypto/PKI/KMS internals link Security CS |
| Supply chain/SBOM/provenance/signing | Đủ sâu về trust model | Có verifier trust policy, CI untrusted-code boundary, dependency execution trust và subject-bound evidence chain |
| Platform as product/golden path/IDP/catalog | Đủ sâu | Có control-plane/data-plane, async lifecycle, end-to-end idempotency, deletion semantics, compatibility set, fault-containment cell và platform SLO |
| Self-service/multi-tenancy/quota/governance | Đủ sâu | Có isolation theo failure/threat model, control-plane fairness, blast-radius budget, tenant-aware SLO, recovery concurrency và policy lifecycle |
| FinOps/cost attribution/rightsizing | Đủ sâu cho platform reasoning | Có showback/chargeback, unit economics, commitment caveat, externality attribution, intentional reserve và reliability headroom |
| Cross-layer troubleshooting | Đủ sâu | Có latency decomposition, coordinated omission, timeout/cancellation, recovery storm và worked failure cases |
| Cross-domain links | Đủ | `90_connections` có 9 reasoning route xuyên domain |

## 4. Readability audit

Mỗi chapter mở đầu từ problem/mental model trước API/tool. Lệnh chỉ xuất hiện khi chúng kiểm tra một hypothesis cụ thể. Các khái niệm `desired state`, `actual state`, `reconciliation`, `artifact`, `blast radius`, `SLI/SLO`, `golden path` được định nghĩa trước khi dùng sâu và có glossary.

Giải thích dùng tiếng Việt; tên API/product/lệnh giữ nguyên. Thuật ngữ Hàn chỉ thêm khi có giá trị nhận diện, không ép ba ngôn ngữ vào mọi câu.

Depth pass hiện tại ưu tiên đoạn văn giải thích cơ chế, assumption và failure chain. Các danh sách chỉ còn dùng cho taxonomy, sequence hoặc checklist mà bản thân cấu trúc danh sách tạo giá trị.

## 5. Duplicate audit

Không tạo chapter riêng về Linux kernel, distributed consensus, OAuth/OIDC, database WAL/MVCC hay generic software architecture vì các phần đó đã có canonical docs.

Container chapter link trực tiếp OS container internals. Kubernetes chapter link failure detector/consensus/fencing. Security chapter link PKI/secrets. CI/CD chapter link deployment safety. Connections file ghi boundary rõ để lần mở rộng sau không copy nội dung.

Sau depth pass, không xuất hiện library/chapter duplicate, file `_updated`, `_final`, `_version2` hoặc temporary note mới. Nội dung mới được bổ sung trực tiếp vào canonical file hiện hữu.

## 6. Modern và legacy perspective

Library dùng control-loop, immutable artifact, workload identity, GitOps, policy-as-code và self-service như practice hiện đại. Legacy approach như manual server mutation, mutable tag, long-lived credential, push deployment quyền rộng và ticket-based provisioning được giữ dưới dạng contrast/failure mode, không tạo một “legacy tutorial” riêng.

Điều này giúp người đọc nhận ra hệ thống cũ trong công việc mà không học thói quen cũ như default.

Modern không được đồng nghĩa với “công nghệ mới hơn”. Một practice chỉ được ưu tiên khi nó cải thiện invariant, feedback, isolation, operability hoặc developer experience. Tool mới không tự tạo chapter nếu không tạo mental model mới.

## 7. Production evidence audit

Các chapter đều nối concept với evidence: process/socket `/proc`, PSI/throttling/writeback/accept-queue signal, DNS resolver/cache và packet-size/path evidence, deployment event, artifact digest/provenance/toolchain identity, IaC plan/state/remote actual state, cloud quota/rate-limit/capacity status, Kubernetes generation/conditions/events/storage attach state/controller queue, GitOps observed/applied/serving revision, telemetry pipeline, SLI burn, tenancy/fairness/cost attribution và audit log.

Các worked failure case quan trọng đều cố gắng giữ causal chain `symptom → hypothesis → evidence → layer → mitigation → verify`, thay vì biến thành danh sách lệnh. Các vòng depth gần đây bổ sung counterfactual/cohort comparison, detector reliability, transition-state capacity và recovery-phase evidence để tránh kết luận nhân quả quá sớm.

## 8. Security audit

Security được trải từ source/build → CI runner → artifact/registry → GitOps repository → workload identity → secrets → admission/policy → break-glass. Không coi “private network”, “private repository”, “signed artifact” hay “short-lived token” là trust boundary đầy đủ nếu authorization scope hoặc verifier policy vẫn rộng.

Security control nằm trên production control path như admission/policy cũng được xem như production software: cần test, staged rollout, telemetry và rollback/fail-open/fail-closed decision có chủ đích.

Vòng depth mới kiểm tra thêm effective authority: caller identity phải được bind với requested target trước khi automation identity mạnh hơn thực hiện action; token forwarding không được mặc định đồng nghĩa authority forwarding; policy/evidence phải bind vào immutable subject/revision để tránh TOCTOU.

Build/GitOps depth mới cũng củng cố chain-of-custody: artifact evidence phải bind đúng digest/target variant; desired-state rendering cần declared inputs; encrypted Git secret vẫn có decrypt identity/KMS lifecycle riêng.

## 9. Performance và capacity audit

Library hiện nối performance từ Linux/cgroup pressure lên container startup/runtime behavior, Kubernetes scheduling/autoscaling/storage attach, cloud provisioning/API/physical-capacity latency và SRE queue/capacity model.

Phần DevOps chỉ giữ performance ở mức operational reasoning: saturation, headroom, queue, throttling, warm-up, connection budget, I/O service rate, admission control, failover capacity và evidence. CPU architecture, scheduler algorithm, virtual memory, page-table hoặc formal queueing depth sâu hơn vẫn thuộc Computer Science/Mathematics canonical docs.

Capacity không còn được hiểu chỉ là peak throughput hay steady-state utilization. Audit hiện kiểm tra cả transition-state headroom cho replace/surge, recovery concurrency, failure headroom, correlated failure, control-plane rate limit, physical capacity scarcity, fairness và intentional idle reserve phục vụ SLO.

## 10. Coverage cố ý chưa tách chapter

Service mesh, eBPF, Crossplane, OpenTofu/Terraform product details, Helm/Argo CD/Flux, specific cloud provider, Backstage, Vault, Prometheus/Grafana, Jenkins/GitHub Actions/GitLab CI không có chapter riêng chỉ vì phổ biến. Chúng nên được dùng như implementation example trong concept chapter khi cần.

Service mesh hiện chưa cần chapter riêng vì control-plane/data-plane, mTLS identity, retry/timeout và routing failure đã có prerequisite ở network, security và Kubernetes. Chỉ nên tách khi cần một reasoning path mới về traffic-policy composition hoặc failure amplification mà các chapter hiện tại không còn chứa tự nhiên được.

eBPF cũng không nên trở thành chapter DevOps chỉ vì observability/networking hiện đại sử dụng nó. Kernel execution/verifier/hook internals thuộc Computer Science; DevOps chỉ cần đưa eBPF tool vào ví dụ nếu nó giúp thu evidence cho một hypothesis cụ thể.

## 11. Internal-link audit checklist

Các link từ DevOps sang Computer Science dùng relative path từ chapter hiện tại. README dùng direct `.md` links cho reading sequence thay vì phụ thuộc directory navigation. Các cross-link chính trỏ tới canonical OS, Distributed Systems, Security, Software Engineering và Database docs hiện có.

Khi đổi tên/move canonical CS chapter, cần cập nhật các link trong `README.md`, runtime/container, Kubernetes, security và `90_connections`.

Không tạo link giả đến chapter tool-specific chưa tồn tại. Link tới product documentation bên ngoài cũng không được dùng để thay thế prerequisite nội bộ nếu repository đã có canonical explanation.

## 12. Dependency-hidden audit sau depth pass

Các prerequisite dễ bị coi là “ai cũng biết” đã được làm rõ thêm trong canonical chapter thay vì tách file mới: queue/WIP và feedback ở Foundations; pressure/resource boundary/writeback/accept queue/clock ở Linux; deadline/retry/cache/connection pool/MTU ở Network; hermetic/reproducible/toolchain/remote input ở Build; concurrency/stale evidence/approval subject/test isolation ở CI; layer/runtime/startup/effective config ở Container; state/partial failure/unknown value/transition headroom ở IaC; control-plane eventual behavior/API capacity/physical scarcity ở Cloud; reconciliation/field ownership/lifecycle graph/storage fencing/batch semantics ở Kubernetes/GitOps; sampling/aggregation ở Observability; queue/capacity/retry/admission ở SRE; effective authority và evidence binding ở Security; async lifecycle/idempotency/fault cell ở Platform; isolation/fairness/recovery capacity ở Multi-tenancy.

Điểm này quan trọng vì một chapter có thể dài nhưng vẫn có prerequisite ẩn. Coverage hiện được đánh giá theo causal reasoning, không theo số heading hoặc số dòng.

## 13. Naming và canonical-state audit

Root domain duy nhất là `devops_platform_engineering/`. Các subdomain dùng numbering theo dependency `00` → `10`, sau đó `90_connections`. Không có root DevOps thứ hai hoặc chapter trùng tên cần consolidate.

Các file hiện tại đều có vai trò canonical rõ; không có raw/source trong domain cần sửa. `GLOSSARY.md`, `LANGUAGE_STYLE.md` và `COVERAGE_AUDIT.md` là tài liệu hỗ trợ, không cạnh tranh với chapter chính.

Branch domain duy nhất là `feat/devops-platform-engineering-knowledge-library`; không phát hiện branch DevOps/Platform Engineering thứ hai cần hợp nhất hoặc xóa.

Branch đã từng được sync với `main` trước các vòng depth; trạng thái ahead/behind phải được kiểm tra lại ở cuối mỗi editing pass vì repository có thể nhận commit song song trong lúc domain đang được đào sâu.

## 14. Criteria cho lần mở rộng tiếp theo

Một chapter mới chỉ nên được thêm nếu đáp ứng ít nhất một điều kiện: tạo mental model mới; giải một failure class quan trọng chưa có; bổ sung production evidence; hoặc nối nhiều lớp thành reasoning path mới mà việc nhét vào canonical file hiện tại làm mất conceptual boundary.

Nếu nhu cầu mới chủ yếu là syntax hoặc sản phẩm — ví dụ “cách viết Helm chart”, “lệnh Argo CD”, “Terraform provider X” — ưu tiên example/reference bên trong chapter hiện có hoặc tài liệu thực hành riêng nếu repository sau này có boundary cho labs. Không dùng số lượng chapter làm thước đo hoàn thành.

## 15. Invariants/failure-semantics depth pass

Một vòng đào sâu trước đó cố ý không mở chapter mới và tăng reasoning density ở các canonical area phía control-plane/platform.

Kubernetes được bổ sung delete/finalizer protocol, owner graph, leader-election/fencing boundary, informer-cache staleness, status-condition contract, CRD evolution và control-plane fairness. SRE được bổ sung admission/concurrency control, failover capacity, correlated failure, brownout và error-budget policy như feedback controller. Security được bổ sung confused deputy, authority propagation, TOCTOU, revocation propagation và control-plane compromise blast radius.

Platform Engineering được bổ sung invariant đằng sau `Ready`, end-to-end idempotency, delete retention semantics, fault-containment cell, tested compatibility set và abstraction-leak feedback. Multi-tenancy/FinOps được bổ sung fairness, blast-radius budget, tenant-aware SLO, recovery concurrency, externality attribution, intentional reserve và lifecycle của policy/exception.

Production Practice được bổ sung counterfactual/cohort reasoning, interaction của nhiều feedback loop, timeout không cancel work, recovery storm, explicit brownout evidence, timeline uncertainty và detector/negative-evidence semantics.

Các phần này đều tạo mental model/failure class mới và đã được nối lại trong `90_connections`, thay vì tồn tại như các đoạn senior note rời rạc.

## 16. Source-to-runtime và transition-state depth pass

Vòng đào sâu mới nhất tiếp tục giữ nguyên canonical structure nhưng tăng độ sâu từ source cho tới workload runtime.

Linux bổ sung dirty-page/writeback stall, listen/accept queue, effective limit composition và clock dependency. Network bổ sung negative DNS caching, connection-pool queue, Path MTU black-hole, HTTP/2 multiplexing failure scope và load-balancer health propagation. Build bổ sung nondeterministic input, build-time network trust, independent rebuild, target architecture identity và generated-code/toolchain closure. CI/CD bổ sung superseded-work cancellation semantics, subject-bound approval, shared environment coupling, paused release state, cohort comparison và merge-queue capacity.

Container bổ sung image-vs-runtime precedence, init-container limitation, startup resource spike, explicit writable path, external-side-effect boundary và config-revision cohorts. IaC bổ sung unknown values, replacement ordering, transition headroom, remote lookup stability, state recovery và pre/post-apply policy boundary. Cloud bổ sung control-plane API capacity, zonal physical capacity scarcity, N-1/failure-state headroom, replication bandwidth/lag và private endpoint composition.

Kubernetes workload bổ sung storage topology/attach fencing, StatefulSet-vs-data invariant, ephemeral-storage pressure, Job/CronJob business idempotency và endpoint churn. GitOps bổ sung observed/applied/serving revision separation, repository outage semantics, deterministic rendering, prune risk, readiness-vs-ordering, multi-cluster rollout và decrypt/KMS path.

Mental model chung của vòng này là **steady state không đủ để đánh giá safety**. Phải reasoning cả transition state: build input thay đổi, release evidence stale, replacement/surge cần headroom, failover cần capacity, controller cần thời gian hội tụ và stateful ownership transfer cần fencing.

## 17. Kết luận audit hiện tại

Library hiện có đường reasoning liên tục:

```text
flow / ownership
→ runtime + request path + resource/queue pressure
→ source / artifact / evidence freshness
→ container runtime + effective inputs
→ infrastructure state transition + cloud capacity
→ Kubernetes workload/control loops + stateful ownership
→ GitOps desired/applied/serving state
→ telemetry / SLO / overload / capacity / recovery
→ identity / effective authority / policy / supply-chain trust
→ platform contract / distributed lifecycle / tenancy / fairness / economics
→ cross-layer causal production diagnosis
```

Coverage hiện đủ để đọc như một giáo trình DevOps/Platform Engineering tổng quát mà không biến thành catalog sản phẩm. Các lần mở rộng tiếp theo nên tiếp tục xuất phát từ incident/failure class, transition-state invariant hoặc platform requirement thực tế, không từ xu hướng công nghệ.