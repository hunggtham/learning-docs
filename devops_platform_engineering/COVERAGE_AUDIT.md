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
| Linux process/service/signal/resource | Đủ cho production operations | Internals link `computer_science/03_operating_systems` |
| Linux pressure/throttling/evidence | Đủ applied | Kernel scheduler/memory internals vẫn giữ ở OS canonical |
| DNS/TCP/TLS/proxy/request path | Đủ cho troubleshooting | Có retry/deadline/connection-path reasoning; protocol depth cross-link CS |
| Git/change flow | Đủ theo delivery context | Không biến thành Git command manual |
| Reproducible/hermetic build, artifact identity, cache trust | Đủ sâu | Supply-chain nối security; language-specific build tool không tách chapter |
| CI/CD, flaky tests, concurrency, stale evidence, migration safety | Đủ sâu | Deployment theory link Software Engineering |
| Container image/runtime/build/security/resource | Đủ production depth | Có image pull/recovery, runtime contract, filesystem/layer, UID/PID1, multi-arch và memory-accounting concerns; internals link OS |
| IaC desired state/state/drift/modules/import/partial failure | Đủ sâu | Tool-specific Terraform/OpenTofu syntax cố ý không thành chapter riêng |
| Cloud IAM/network/compute/storage/failure domain | Đủ production depth | Có eventual consistency, control-plane/data-plane, managed failover, durability-vs-availability, quota, provisioning latency và locality; provider catalog không duplicate |
| Kubernetes control plane/reconciliation | Đủ sâu | Có optimistic concurrency, watch/resync, work queue/backoff, admission và API saturation; consensus internals link Distributed Systems |
| Kubernetes workload/network/storage/resources/autoscaling | Đủ sâu | Có schedulable-vs-aggregate capacity, PDB, topology, termination race và interacting autoscalers |
| GitOps | Đủ sâu | Có field ownership, rollback limits, promotion race, break-glass và repository trust; product syntax không canonical |
| Metrics/logs/traces/events/alerting | Đủ sâu | Có telemetry-pipeline failure, sampling, cardinality, percentile caveat và exemplars |
| SLI/SLO/error budget/capacity/backpressure | Đủ sâu | Có burn-rate reasoning, Little's Law, retry budget, dependency budget và saturation cliff |
| Incident/postmortem/runbook | Đủ sâu | Có recovery-vs-root-cause, timeline decomposition và evidence preservation |
| Backup/RPO/RTO/DR/chaos | Đủ sâu | Có consistency boundary, PITR chain, DR bootstrap, fencing/failback và experiment validity |
| IAM/workload identity/secrets/policy | Đủ sâu ở platform layer | Crypto/PKI/KMS internals link Security CS |
| Supply chain/SBOM/provenance/signing | Đủ sâu về trust model | Có verifier trust policy, CI untrusted-code boundary và dependency execution trust |
| Platform as product/golden path/IDP/catalog | Đủ sâu | Có control-plane/data-plane, async operation, failure contract, compatibility window và platform SLO |
| Self-service/multi-tenancy/quota/governance | Đủ sâu | Có isolation theo failure/threat model, control-plane fairness, recovery quota và Day-2 lifecycle |
| FinOps/cost attribution/rightsizing | Đủ sâu cho platform reasoning | Có showback/chargeback, unit economics, commitment caveat, shared cost, anomaly feedback và reliability headroom |
| Cross-layer troubleshooting | Đủ sâu | Có latency decomposition, coordinated omission và worked failure cases |
| Cross-domain links | Đủ | `90_connections` |

## 4. Readability audit

Mỗi chapter mở đầu từ problem/mental model trước API/tool. Lệnh chỉ xuất hiện khi chúng kiểm tra một hypothesis cụ thể. Các khái niệm `desired state`, `actual state`, `reconciliation`, `artifact`, `blast radius`, `SLI/SLO`, `golden path` được định nghĩa trước khi dùng sâu và có glossary.

Giải thích dùng tiếng Việt; tên API/product/lệnh giữ nguyên. Thuật ngữ Hàn chỉ thêm khi có giá trị nhận diện, không ép ba ngôn ngữ vào mọi câu.

Depth pass hiện tại ưu tiên đoạn văn giải thích cơ chế, assumption và failure chain. Các danh sách chỉ còn dùng cho taxonomy, sequence hoặc checklist mà bản thân cấu trúc danh sách tạo giá trị.

## 5. Duplicate audit

Không tạo chapter riêng về Linux kernel, distributed consensus, OAuth/OIDC, database WAL/MVCC hay generic software architecture vì các phần đó đã có canonical docs.

Container chapter link trực tiếp OS container internals. Kubernetes chapter link failure detector/consensus. Security chapter link PKI/secrets. CI/CD chapter link deployment safety. Connections file ghi boundary rõ để lần mở rộng sau không copy nội dung.

Sau depth pass, không xuất hiện library/chapter duplicate, file `_updated`, `_final`, `_version2` hoặc temporary note mới. Nội dung mới được bổ sung trực tiếp vào canonical file hiện hữu.

## 6. Modern và legacy perspective

Library dùng control-loop, immutable artifact, workload identity, GitOps, policy-as-code và self-service như practice hiện đại. Legacy approach như manual server mutation, mutable tag, long-lived credential, push deployment quyền rộng và ticket-based provisioning được giữ dưới dạng contrast/failure mode, không tạo một “legacy tutorial” riêng.

Điều này giúp người đọc nhận ra hệ thống cũ trong công việc mà không học thói quen cũ như default.

Modern không được đồng nghĩa với “công nghệ mới hơn”. Một practice chỉ được ưu tiên khi nó cải thiện invariant, feedback, isolation, operability hoặc developer experience. Tool mới không tự tạo chapter nếu không tạo mental model mới.

## 7. Production evidence audit

Các chapter đều nối concept với evidence: process/socket `/proc`, pressure/throttling signal, deployment event, artifact digest/provenance, IaC plan/state, cloud quota/control-plane status, Kubernetes object status/conditions/events, controller queue, telemetry pipeline, SLI burn, tenancy/cost attribution và audit log.

Các worked failure case quan trọng đều cố gắng giữ causal chain `symptom → hypothesis → evidence → layer → mitigation → verify`, thay vì biến thành danh sách lệnh.

## 8. Security audit

Security được trải từ source/build → CI runner → artifact/registry → GitOps repository → workload identity → secrets → admission/policy → break-glass. Không coi “private network”, “private repository”, “signed artifact” hay “short-lived token” là trust boundary đầy đủ nếu authorization scope hoặc verifier policy vẫn rộng.

Security control nằm trên production control path như admission/policy cũng được xem như production software: cần test, staged rollout, telemetry và rollback/fail-open/fail-closed decision có chủ đích.

## 9. Performance và capacity audit

Library hiện nối performance từ Linux/cgroup pressure lên container resource behavior, Kubernetes scheduling/autoscaling, cloud provisioning latency và SRE queue/capacity model.

Phần DevOps chỉ giữ performance ở mức operational reasoning: saturation, headroom, queue, throttling, warm-up, connection budget và evidence. CPU architecture, scheduler algorithm, virtual memory, page-table hoặc formal queueing depth sâu hơn vẫn thuộc Computer Science/Mathematics canonical docs.

## 10. Coverage cố ý chưa tách chapter

Service mesh, eBPF, Crossplane, OpenTofu/Terraform product details, Helm/Argo CD/Flux, specific cloud provider, Backstage, Vault, Prometheus/Grafana, Jenkins/GitHub Actions/GitLab CI không có chapter riêng chỉ vì phổ biến. Chúng nên được dùng như implementation example trong concept chapter khi cần.

Service mesh hiện chưa cần chapter riêng vì control-plane/data-plane, mTLS identity, retry/timeout và routing failure đã có prerequisite ở network, security và Kubernetes. Chỉ nên tách khi cần một reasoning path mới về traffic-policy composition hoặc failure amplification mà các chapter hiện tại không còn chứa tự nhiên được.

eBPF cũng không nên trở thành chapter DevOps chỉ vì observability/networking hiện đại sử dụng nó. Kernel execution/verifier/hook internals thuộc Computer Science; DevOps chỉ cần đưa eBPF tool vào ví dụ nếu nó giúp thu evidence cho một hypothesis cụ thể.

## 11. Internal-link audit checklist

Các link từ DevOps sang Computer Science dùng relative path từ chapter hiện tại. README dùng direct `.md` links cho reading sequence thay vì phụ thuộc directory navigation. Các cross-link chính trỏ tới canonical OS, Distributed Systems, Security, Software Engineering và Database docs hiện có.

Khi đổi tên/move canonical CS chapter, cần cập nhật các link trong `README.md`, runtime/container, Kubernetes, security và `90_connections`.

Không tạo link giả đến chapter tool-specific chưa tồn tại. Link tới product documentation bên ngoài cũng không được dùng để thay thế prerequisite nội bộ nếu repository đã có canonical explanation.

## 12. Dependency-hidden audit sau depth pass

Các prerequisite dễ bị coi là “ai cũng biết” đã được làm rõ thêm trong canonical chapter thay vì tách file mới: queue/WIP và feedback ở Foundations; pressure/resource boundary ở Linux; deadline/retry/connection path ở Network; hermetic/reproducible/trust ở Build; concurrency/stale evidence ở CI; layer/runtime/recovery dependency ở Container; state/partial failure ở IaC; control-plane eventual behavior ở Cloud; reconciliation/field ownership ở Kubernetes/GitOps; sampling/aggregation ở Observability; queue/capacity/retry budget ở SRE; trust policy ở Security; async contract/versioning ở Platform; isolation/control-plane fairness ở Multi-tenancy.

Điểm này quan trọng vì một chapter có thể dài nhưng vẫn có prerequisite ẩn. Coverage hiện được đánh giá theo causal reasoning, không theo số heading hoặc số dòng.

## 13. Naming và canonical-state audit

Root domain duy nhất là `devops_platform_engineering/`. Các subdomain dùng numbering theo dependency `00` → `10`, sau đó `90_connections`. Không có root DevOps thứ hai hoặc chapter trùng tên cần consolidate.

Các file hiện tại đều có vai trò canonical rõ; không có raw/source trong domain cần sửa. `GLOSSARY.md`, `LANGUAGE_STYLE.md` và `COVERAGE_AUDIT.md` là tài liệu hỗ trợ, không cạnh tranh với chapter chính.

Branch domain duy nhất là `feat/devops-platform-engineering-knowledge-library`; không phát hiện branch DevOps/Platform Engineering thứ hai cần hợp nhất hoặc xóa.

Trong lúc depth pass diễn ra, `main` nhận thêm hai commit canonical Mathematics. Branch DevOps đã được đồng bộ bằng merge commit với `main` mới nhất, giữ DevOps subtree và root README hiện tại. Sau sync, compare với `main` cho trạng thái **ahead, behind 0** và merge-base chính là HEAD `main`; vì vậy branch không còn drift repository-level trước final review.

## 14. Criteria cho lần mở rộng tiếp theo

Một chapter mới chỉ nên được thêm nếu đáp ứng ít nhất một điều kiện: tạo mental model mới; giải một failure class quan trọng chưa có; bổ sung production evidence; hoặc nối nhiều lớp thành reasoning path mới mà việc nhét vào canonical file hiện tại làm mất conceptual boundary.

Nếu nhu cầu mới chủ yếu là syntax hoặc sản phẩm — ví dụ “cách viết Helm chart”, “lệnh Argo CD”, “Terraform provider X” — ưu tiên example/reference bên trong chapter hiện có hoặc tài liệu thực hành riêng nếu repository sau này có boundary cho labs. Không dùng số lượng chapter làm thước đo hoàn thành.

## 15. Kết luận audit hiện tại

Library hiện có đường reasoning liên tục:

```text
flow / ownership
→ runtime + request path
→ source / artifact / evidence
→ container + infrastructure lifecycle
→ cloud + Kubernetes control loops
→ GitOps desired state
→ telemetry / SLO / capacity / recovery
→ identity / policy / supply-chain trust
→ platform contract / tenancy / economics
→ cross-layer production diagnosis
```

Coverage hiện đủ để đọc như một giáo trình DevOps/Platform Engineering tổng quát mà không biến thành catalog sản phẩm. Các lần mở rộng tiếp theo nên xuất phát từ incident/failure class hoặc platform requirement thực tế, không từ xu hướng công nghệ.
