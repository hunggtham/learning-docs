# DevOps / Platform Engineering — source ledger và release/config boundary

> **Owner:** `devops_platform_engineering/` (canonical delivery and operations content). Ledger này tách platform invariant, product semantics, provider behavior và observed production evidence.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| DPE-K8S-01 | Kubernetes project | API objects, controllers, scheduling, networking, storage và lifecycle semantics | https://kubernetes.io/docs/ | docs live; cluster/Kubernetes version phải ghi | Defaults, feature gates, API availability và provider behavior phụ thuộc release/config; không suy từ docs mới sang cluster cũ | `05_kubernetes/` |
| DPE-OCI-01 | Open Container Initiative | image/runtime/distribution specifications | https://opencontainers.org/specs/ | spec revision phải ghi; portal kiểm tra 2026-10-09 | Spec không đảm bảo behavior của registry/runtime; ghi implementation/version và digest | `03_containers/` |
| DPE-OTEL-01 | OpenTelemetry project | telemetry API/SDK, semantic conventions và collector pipeline | https://opentelemetry.io/docs/ | docs/spec version phải ghi | Instrumentation, sampling, exporter và backend config quyết định observed signal; không gọi missing signal là zero | `07_observability_sre/` |
| DPE-PROM-01 | Prometheus project | metrics model, PromQL và server behavior | https://prometheus.io/docs/ | release/config phải ghi | Retention, scrape, federation, remote-write và query cost phụ thuộc config/version | observability/SRE |
| DPE-SLSA-01 | SLSA project | software supply-chain provenance levels and verification model | https://slsa.dev/spec/v1.0/ | SLSA v1.0; kiểm tra 2026-10-09 | Level/spec không tự chứng minh builder integrity hoặc deployment policy; cần attestation/verifier evidence | `08_security_governance/` |
| DPE-HASHI-01 | HashiCorp Terraform documentation | IaC language, plan/state/provider semantics | https://developer.hashicorp.com/terraform/docs | product/version/provider phải ghi | Provider version, remote state, credentials và cloud API làm behavior thay đổi; docs không thay thế plan/actual evidence | `04_infrastructure_as_code/` |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| DPE-DEFAULT-01 | `NEEDS_SOURCE` | Claim về default, guarantee, availability, quota, pricing hoặc deprecation phải ghi product/version/provider/region và ngày kiểm tra. | Owner chapter/tool |
| DPE-PERF-01 | `NEEDS_SOURCE` | Throughput, SLO, latency, cost và capacity cần workload, topology, hardware/cloud, sample window và observed evidence. | Owner production practice |
| DPE-SECURITY-01 | `REVIEW_REQUIRED` | Supply-chain/IAM/secrets claim phải nối threat model → control → verifier evidence → rollout/revocation; không coi config snippet là proof. | Owner security/governance |
| DPE-INCIDENT-01 | `REVIEW_REQUIRED` | Case study phải phân biệt observed fact, hypothesis, intervention và counterfactual; không suy causal từ một dashboard snapshot. | Owner case study + reviewer |

## Quy trình refresh

1. Ghi product/version/provider/region/config và ngày kiểm tra cho mọi claim implementation hoặc cloud.
2. Tách spec/invariant khỏi defaults, managed-service behavior và observed production evidence.
3. Khi release/deprecation/API/price/quota đổi, mở review cho affected chapters; regenerate examples và re-run lab.
4. Chỉ đánh dấu claim hoàn tất khi có evidence phù hợp; structural audit/build không thay thế runtime/provider check.
