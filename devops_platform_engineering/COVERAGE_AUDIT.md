# Coverage Audit — DevOps / Platform Engineering Knowledge Library

## 1. Conceptual boundary

Library sở hữu kiến thức về delivery system, infrastructure lifecycle, orchestration usage, GitOps, observability/SRE, security guardrail, platform product và production operations. Library **không** sở hữu internals nền đã có canonical home trong `computer_science/`.

Các phần cố ý cross-link thay vì duplicate gồm kernel/process/filesystem internals, namespaces/cgroups internals, distributed consensus/ordering, cryptographic protocol, PKI internals, database internals và software architecture/test/deployment theory ở mức Computer Science.

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

## 3. Coverage matrix

| Capability | Coverage | Canonical dependency / note |
|---|---|---|
| DevOps operating model, flow, feedback, ownership | Đủ nền | `00_foundations` |
| Platform Engineering boundary và cognitive load | Đủ nền | `00_foundations`, `09_platform_engineering` |
| Linux process/service/signal/resource | Đủ cho operations | Internals link `computer_science/03_operating_systems` |
| DNS/TCP/TLS/proxy/request path | Đủ cho troubleshooting | Protocol depth cross-link CS |
| Git/change flow | Đủ theo delivery context | Không biến thành Git command manual |
| Reproducible build/artifact/promotion | Đủ | Supply-chain nối security |
| CI/CD, flaky tests, verification, rollback | Đủ | Deployment theory link Software Engineering |
| Container image/runtime/build/security/resource | Đủ applied | Namespace/cgroup internals link OS |
| IaC desired state/state/drift/modules/import | Đủ concept | Tool-specific Terraform syntax cố ý không thành chapter riêng |
| Cloud IAM/network/compute/storage/failure domain | Đủ platform foundation | Provider-specific catalog không duplicate |
| Kubernetes control plane/reconciliation | Đủ | Consensus internals link Distributed Systems |
| Kubernetes workload/network/storage/resources/autoscaling | Đủ production foundation | CNI/CSI implementation chi tiết để mở rộng khi có mental-model need |
| GitOps | Đủ | Product-specific Argo CD/Flux syntax không phải canonical chapter |
| Metrics/logs/traces/events/alerting | Đủ | OpenTelemetry ở mức semantic layer |
| SLI/SLO/error budget/capacity/backpressure | Đủ | Queueing math có thể link performance/math khi cần |
| Incident/postmortem/runbook | Đủ | Có recovery-vs-root-cause distinction |
| Backup/RPO/RTO/DR/chaos | Đủ nền | Database-specific recovery nằm database domain |
| IAM/workload identity/secrets/policy | Đủ platform | Crypto/PKI/KMS internals link Security CS |
| Supply chain/SBOM/provenance/signing | Đủ concept | Có thể mở rộng standards khi repository cần reference chuyên sâu |
| Platform as product/golden path/IDP/catalog | Đủ | Portal product cụ thể không thành chapter |
| Self-service/multi-tenancy/quota/governance | Đủ | Cluster topology vendor-specific không canonical |
| FinOps/cost attribution/rightsizing | Đủ foundation | Không biến thành cloud pricing catalog |
| Cross-layer troubleshooting | Đủ | `10_production_practice` |
| Cross-domain links | Đủ | `90_connections` |

## 4. Readability audit

Mỗi chapter mở đầu từ problem/mental model trước API/tool. Lệnh chỉ xuất hiện khi chúng kiểm tra một hypothesis cụ thể. Các khái niệm `desired state`, `actual state`, `reconciliation`, `artifact`, `blast radius`, `SLI/SLO`, `golden path` được định nghĩa trước khi dùng sâu và có glossary.

Giải thích dùng tiếng Việt; tên API/product/lệnh giữ nguyên. Thuật ngữ Hàn chỉ thêm khi có giá trị nhận diện, không ép ba ngôn ngữ vào mọi câu.

## 5. Duplicate audit

Không tạo chapter riêng về Linux kernel, distributed consensus, OAuth/OIDC, database WAL/MVCC hay generic software architecture vì các phần đó đã có canonical docs.

Container chapter link trực tiếp OS container internals. Kubernetes chapter link failure detector/consensus. Security chapter link PKI/secrets. CI/CD chapter link deployment safety. Connections file ghi boundary rõ để lần mở rộng sau không copy nội dung.

## 6. Modern và legacy perspective

Library dùng control-loop, immutable artifact, workload identity, GitOps, policy-as-code và self-service như practice hiện đại. Legacy approach như manual server mutation, mutable tag, long-lived credential, push deployment quyền rộng và ticket-based provisioning được giữ dưới dạng contrast/failure mode, không tạo một “legacy tutorial” riêng.

Điều này giúp người đọc nhận ra hệ thống cũ trong công việc mà không học thói quen cũ như default.

## 7. Production evidence audit

Các chapter đều nối concept với evidence: process/socket `/proc`, deployment event, object status/conditions/events, telemetry, SLI burn, quota/capacity, audit/provenance. Đây là yêu cầu quan trọng để library không dừng ở configuration syntax.

## 8. Security audit

Security được trải từ build → CI runner → artifact → registry → workload identity → secrets → policy → break-glass. Không coi “private network” hoặc “private repository” là trust boundary đầy đủ.

## 9. Coverage cố ý chưa tách chapter

Service mesh, eBPF, Crossplane, OpenTofu/Terraform product details, Helm/Argo CD/Flux, specific cloud provider, Backstage, Vault, Prometheus/Grafana, Jenkins/GitHub Actions/GitLab CI không có chapter riêng chỉ vì phổ biến. Chúng nên được dùng như implementation example trong concept chapter khi cần.

Chỉ tạo chapter riêng nếu một technology mang mental model/invariant mới chưa được library giải thích. Ví dụ service mesh có thể đáng tách khi cần đào sâu control plane/data plane, traffic policy, mTLS identity và failure amplification; nhưng không nên tách chỉ để liệt kê resource/config.

## 10. Internal-link audit checklist

Các link từ DevOps sang Computer Science đều dùng relative path từ chapter hiện tại. README link xuống các section trong library. Không có link giả đến tool chapter chưa tồn tại.

Khi đổi tên/move canonical CS chapter, cần cập nhật các link trong `README.md`, container, Kubernetes, security và `90_connections`.

## 11. Criteria cho lần mở rộng tiếp theo

Một chapter mới chỉ nên được thêm nếu đáp ứng ít nhất một điều kiện: tạo mental model mới; giải một failure class quan trọng chưa có; bổ sung production evidence; hoặc nối nhiều lớp thành reasoning path mới.

Không dùng số lượng chapter làm thước đo hoàn thành.