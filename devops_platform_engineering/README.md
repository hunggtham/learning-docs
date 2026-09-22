# DevOps / Platform Engineering Knowledge Library

Thư viện này học DevOps và Platform Engineering như một **hệ thống cung cấp và vận hành phần mềm**, không phải danh sách công cụ. Câu hỏi trung tâm không phải “biết Docker, Kubernetes hay Terraform chưa?” mà là: làm thế nào một thay đổi từ máy của lập trình viên đi qua build, kiểm thử, artifact, hạ tầng, triển khai, quan sát và vận hành mà vẫn giữ được tốc độ, khả năng lặp lại, an toàn và khả năng phục hồi.

DevOps ở đây được hiểu là mô hình kỹ thuật và tổ chức làm giảm khoảng cách giữa phát triển và vận hành. Platform Engineering là bước tiếp theo khi các năng lực lặp lại được đóng gói thành một nền tảng nội bộ có giao diện tự phục vụ, đường đi chuẩn và guardrail để nhiều team sử dụng mà không phải trở thành chuyên gia hạ tầng.

Thư viện có conceptual boundary riêng vì đối tượng nghiên cứu là **delivery system và operating platform**. Những cơ chế nền sâu hơn vẫn thuộc canonical `computer_science/`. Ví dụ, Linux process, namespace/cgroup, TLS, distributed consensus, secrets, deployment theory và failure semantics không được viết lại từ đầu; chapter DevOps chỉ cung cấp mental model đủ dùng rồi link sang canonical chapter tương ứng.

## Cách đọc

Lộ trình chính đi theo dependency tự nhiên:

```text
software delivery problem
        ↓
operating model + ownership + feedback
        ↓
Linux/runtime + network request path
        ↓
Git → build → immutable artifact
        ↓
CI → CD → safe change
        ↓
container image/runtime
        ↓
infrastructure as code + cloud primitives
        ↓
Kubernetes reconciliation
        ↓
GitOps reconciliation
        ↓
observability + SRE + incident response
        ↓
security + policy + supply chain
        ↓
platform as product + self-service + guardrails
        ↓
production troubleshooting across layers
```

Không cần học thuộc công cụ theo thứ tự này. Dependency quan trọng hơn product. Nếu đang dùng Docker/Kubernetes mỗi ngày nhưng chưa rõ process, filesystem, DNS hoặc resource limit, hãy quay lại runtime foundations. Nếu đã triển khai được workload nhưng rollback và incident vẫn dựa vào trực giác, hãy ưu tiên CI/CD, observability và SRE trước khi học thêm platform feature.

## Bản đồ library

| Phần | Mục tiêu |
|---|---|
| [`00_foundations`](./00_foundations/00_devops_platform_operating_model.md) | Hiểu DevOps/Platform Engineering như một socio-technical system, flow, feedback, ownership và cognitive load |
| [`01_runtime_foundations`](./01_runtime_foundations/00_linux_execution_and_service_model.md) | Hiểu execution environment và request path đủ sâu để vận hành production |
| [`02_delivery_system`](./02_delivery_system/00_git_build_artifacts_and_reproducibility.md) | Từ source change đến reproducible artifact và safe delivery |
| [`03_containers`](./03_containers/00_container_image_runtime_and_builds.md) | Container image/runtime, build cache, isolation boundary và production usage |
| [`04_infrastructure_as_code`](./04_infrastructure_as_code/00_iac_state_drift_and_change_management.md) | Declarative infrastructure, state, plan/apply, drift, cloud primitives và lifecycle |
| [`05_kubernetes`](./05_kubernetes/00_kubernetes_reconciliation_and_control_plane.md) | Reconciliation, control plane, workload, networking, storage, scheduling và resource behavior |
| [`06_gitops`](./06_gitops/00_gitops_reconciliation_and_promotion.md) | Dùng Git làm desired-state interface và reconciliation làm deployment mechanism |
| [`07_observability_sre`](./07_observability_sre/00_observability_telemetry_and_evidence_driven_debugging.md) | Telemetry, evidence-driven debugging, SLI/SLO, error budget, incident, capacity và DR |
| [`08_security_governance`](./08_security_governance/00_identity_secrets_policy_and_supply_chain.md) | Identity, secrets, policy, artifact provenance và supply-chain controls |
| [`09_platform_engineering`](./09_platform_engineering/00_platform_as_product_golden_paths_and_abstractions.md) | Platform as product, golden path, self-service, tenancy, governance và cost |
| [`10_production_practice`](./10_production_practice/00_production_troubleshooting_and_change_failure_patterns.md) | Troubleshooting xuyên tầng và các failure pattern của thay đổi production |
| [`90_connections`](./90_connections/00_devops_platform_cross_domain_map.md) | Bản đồ nối DevOps/Platform với Computer Science và các canonical docs khác |

[`GLOSSARY.md`](./GLOSSARY.md) là tài liệu tra thuật ngữ. [`COVERAGE_AUDIT.md`](./COVERAGE_AUDIT.md) ghi rõ boundary, phần đã bao phủ, phần cố ý cross-link và các điểm cần audit khi mở rộng.

## Nguyên tắc học

Một platform tốt không được đánh giá bằng số lượng tool. Nó được đánh giá bằng khả năng làm cho **đường đi đúng trở thành đường đi dễ nhất**. Vì vậy mỗi chapter cố gắng trả lời cùng một chuỗi câu hỏi: vấn đề nào buộc concept đó xuất hiện; desired invariant là gì; mechanism giữ invariant như thế nào; failure xảy ra ở đâu; evidence nào xác nhận giả thuyết; và abstraction nào nên được cung cấp cho người dùng platform.

Khi gặp YAML, CLI hoặc API, hãy đọc chúng như một giao diện điều khiển state chứ không phải thứ cần học thuộc. Cấu hình chỉ có ý nghĩa khi biết controller, runtime hoặc service nào đọc nó, state nào được tạo ra, ai là owner của state đó và failure nào xuất hiện khi desired state khác actual state.

## Canonical prerequisites thay vì duplicate

Để hiểu sâu process, syscall, filesystem và virtualization, dùng [Computer Science — Operating Systems](../computer_science/basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) và [privilege/isolation/virtualization](../computer_science/basic/03_operating_systems/05_privilege_isolation_and_virtualization.md). Container internals được đào sâu ở [namespaces, cgroups, capabilities và seccomp](../computer_science/03_operating_systems/advanced/06_containers_namespaces_cgroups_capabilities_and_seccomp.md).

Các vấn đề distributed failure, ordering, consensus và multi-region thuộc [Networks & Distributed Systems](../computer_science/06_networks_distributed_systems/advanced/README.md). Service identity, PKI, secrets và key lifecycle thuộc [Security & Reliability](../computer_science/07_security_reliability/advanced/README.md). Deployment strategy và rollback theory được nối sang [deployment safety](../computer_science/09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md).

DevOps Library sử dụng những nền đó để trả lời câu hỏi áp dụng: “thiết kế delivery/platform ra sao để nhiều team thay đổi production an toàn và tự chủ?”.

## Đích đến

Sau khi đi hết library, người đọc cần có khả năng nhìn một hệ thống production như một chuỗi control loop và contract. Có thể lần từ commit đến artifact, từ artifact đến workload, từ workload đến network/storage dependency, từ telemetry về symptom, và từ incident quay lại cải thiện platform. Mục tiêu không phải trở thành người thuộc nhiều lệnh, mà là người có thể suy luận về hệ thống khi tool, cloud provider hoặc tổ chức thay đổi.