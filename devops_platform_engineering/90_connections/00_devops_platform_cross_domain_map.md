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