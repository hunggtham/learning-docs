# DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)

> **Mạch đọc:** Đọc **DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Cách đọc** sang **Bản đồ thư viện (library / 라이브러리)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Thư viện này học DevOps và kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) như một **hệ thống cung cấp và vận hành phần mềm**, không phải danh sách công cụ. Câu hỏi trung tâm không phải “biết Docker, Kubernetes hay Terraform chưa?” mà là: làm thế nào một thay đổi từ máy của lập trình viên đi qua bản dựng (build / 빌드), kiểm thử, sản phẩm tạo ra (artifact / 산출물), hạ tầng, triển khai, quan sát và vận hành mà vẫn giữ được tốc độ, khả năng lặp lại, an toàn và khả năng phục hồi.

DevOps ở đây được hiểu là mô hình kỹ thuật và tổ chức làm giảm khoảng cách giữa phát triển và vận hành. kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) là bước tiếp theo khi các năng lực lặp lại được đóng gói thành một nền tảng nội bộ có giao diện tự phục vụ, đường đi chuẩn và guardrail để nhiều nhóm (team / 팀) sử dụng mà không phải trở thành chuyên gia hạ tầng.

Thư viện có conceptual ranh giới (boundary / 경계) riêng vì đối tượng nghiên cứu là **delivery hệ thống (system / 시스템) và operating nền tảng (platform / 플랫폼)**. Những cơ chế nền sâu hơn vẫn thuộc chuẩn gốc (canonical / 정본) `computer_science/`. Ví dụ, Linux tiến trình (process / 프로세스), không gian tên (namespace / 네임스페이스)/cgroup, TLS, phân tán (distributed / 분산) consensus, secrets, triển khai (deployment / 배포) lý thuyết (theory / 이론) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) không được viết lại từ đầu; chapter DevOps chỉ cung cấp mô hình tư duy (mental model / 사고 모델) đủ dùng rồi link sang chuẩn gốc (canonical / 정본) chapter tương ứng.

## Cách đọc

Lộ trình chính đi theo phụ thuộc (dependency / 의존성) tự nhiên:

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

Không cần học thuộc công cụ theo thứ tự này. phụ thuộc (dependency / 의존성) quan trọng hơn sản phẩm (product / 제품). Nếu đang dùng Docker/Kubernetes mỗi ngày nhưng chưa rõ tiến trình (process / 프로세스), filesystem, DNS hoặc tài nguyên (resource / 자원) limit, hãy quay lại thời gian chạy (runtime / 런타임) foundations. Nếu đã triển khai được tải công việc (workload / 워크로드) nhưng quay lui (rollback / 롤백) và sự cố (incident / 인시던트) vẫn dựa vào trực giác, hãy ưu tiên CI/CD, khả năng quan sát (observability / 관측 가능성) và SRE trước khi học thêm nền tảng (platform / 플랫폼) tính năng (feature / 기능).


> **Chuyển mạch:** Từ **Cách đọc**, ta sang **Bản đồ thư viện (library / 라이브러리)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bản đồ thư viện (library / 라이브러리)
Phần “Bản đồ thư viện (library / 라이브러리)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


| Phần | Mục tiêu |
|---|---|
| [`00_foundations`](./00_foundations/00_devops_platform_operating_model.md) | Hiểu DevOps/kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) như một socio-technical hệ thống (system / 시스템), luồng (flow / 흐름), phản hồi (feedback / 피드백), quyền sở hữu (ownership / 소유권) và cognitive tải (load / 로드) |
| [`01_runtime_foundations`](./01_runtime_foundations/00_linux_execution_and_service_model.md) | Hiểu thực thi (execution / 실행) môi trường (environment / 환경) và đường đi của yêu cầu (request path / 요청 경로) đủ sâu để vận hành môi trường vận hành (production / 운영 환경) |
| [`02_delivery_system`](./02_delivery_system/00_git_build_artifacts_and_reproducibility.md) | Từ nguồn (source / 소스) thay đổi (change / 변경) đến reproducible sản phẩm tạo ra (artifact / 산출물) và safe delivery |
| [`03_containers`](./03_containers/00_container_image_runtime_and_builds.md) | ảnh bộ chứa (container image / 컨테이너 이미지)/thời gian chạy (runtime / 런타임), bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시), isolation ranh giới (boundary / 경계) và môi trường vận hành (production / 운영 환경) usage |
| [`04_infrastructure_as_code`](./04_infrastructure_as_code/00_iac_state_drift_and_change_management.md) | Declarative hạ tầng (infrastructure / 인프라), trạng thái (state / 상태), plan/apply, drift, cloud primitives và vòng đời (lifecycle / 생명주기) |
| [`05_kubernetes`](./05_kubernetes/00_kubernetes_reconciliation_and_control_plane.md) | Reconciliation, điều khiển (control / 제어) plane, tải công việc (workload / 워크로드), networking, lưu trữ (storage / 저장소), scheduling và tài nguyên (resource / 자원) hành vi (behavior / 동작) |
| [`06_gitops`](./06_gitops/00_gitops_reconciliation_and_promotion.md) | Dùng Git làm desired-state giao diện (interface / 인터페이스) và reconciliation làm triển khai (deployment / 배포) cơ chế (mechanism / 메커니즘) |
| [`07_observability_sre`](./07_observability_sre/00_observability_telemetry_and_evidence_driven_debugging.md) | Telemetry, evidence-driven debugging, SLI/SLO, lỗi (error / 오류) ngân sách (budget / 예산), sự cố (incident / 인시던트), sức chứa (capacity / 용량) và DR |
| [`08_security_governance`](./08_security_governance/00_identity_secrets_policy_and_supply_chain.md) | định danh (identity / 식별자), secrets, chính sách (policy / 정책), sản phẩm tạo ra (artifact / 산출물) provenance và supply-chain controls |
| [`09_platform_engineering`](./09_platform_engineering/00_platform_as_product_golden_paths_and_abstractions.md) | nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로), self-service, tenancy, quản trị (governance / 거버넌스) và chi phí (cost / 비용) |
| [`10_production_practice`](./10_production_practice/00_production_troubleshooting_and_change_failure_patterns.md) | Troubleshooting xuyên tầng và các thất bại (failure / 실패) mẫu (pattern / 패턴) của thay đổi môi trường vận hành (production / 운영 환경) |
| [`90_connections`](./90_connections/00_devops_platform_cross_domain_map.md) | Bản đồ nối DevOps/nền tảng (platform / 플랫폼) với Khoa học máy tính (computer science / 컴퓨터 과학) và các chuẩn gốc (canonical / 정본) docs khác |


> **Chuyển mạch:** Từ **Bản đồ thư viện (library / 라이브러리)**, ta sang **Trình tự đọc chi tiết** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trình tự đọc chi tiết

1. [DevOps và Platform Engineering: từ vấn đề delivery đến operating model](./00_foundations/00_devops_platform_operating_model.md)
2. [Linux như môi trường thực thi production](./01_runtime_foundations/00_linux_execution_and_service_model.md)
3. [Từ URL đến process: DNS, TCP, TLS, proxy và request path](./01_runtime_foundations/01_network_dns_tls_and_request_path.md)
4. [Từ source đến artifact: Git, build và tính tái lập](./02_delivery_system/00_git_build_artifacts_and_reproducibility.md)
5. [CI/CD: biến thay đổi thành flow có bằng chứng](./02_delivery_system/01_ci_cd_change_flow_and_safe_delivery.md)
6. [Container: image, runtime, isolation và production behavior](./03_containers/00_container_image_runtime_and_builds.md)
7. [Infrastructure as Code: desired state, state model, drift và lifecycle](./04_infrastructure_as_code/00_iac_state_drift_and_change_management.md)
8. [Cloud primitives: identity, network, compute, storage và shared responsibility](./04_infrastructure_as_code/01_cloud_primitives_identity_network_compute_storage.md)
9. [Kubernetes: reconciliation, API objects và control plane](./05_kubernetes/00_kubernetes_reconciliation_and_control_plane.md)
10. [Kubernetes workload, networking, storage, scheduling và resource behavior](./05_kubernetes/01_kubernetes_workloads_networking_storage_and_resources.md)
11. [GitOps: desired state trong Git và reconciliation liên tục](./06_gitops/00_gitops_reconciliation_and_promotion.md)
12. [Observability: từ telemetry đến suy luận có bằng chứng](./07_observability_sre/00_observability_telemetry_and_evidence_driven_debugging.md)
13. [SLI, SLO, error budget và capacity: reliability có mục tiêu](./07_observability_sre/01_sli_slo_error_budget_and_capacity.md)
14. [Incident, resilience, backup và disaster recovery](./07_observability_sre/02_incidents_resilience_backup_and_disaster_recovery.md)
15. [Security và governance: identity, secrets, policy và software supply chain](./08_security_governance/00_identity_secrets_policy_and_supply_chain.md)
16. [Platform Engineering: platform as product, golden path và abstraction](./09_platform_engineering/00_platform_as_product_golden_paths_and_abstractions.md)
17. [Self-service, multi-tenancy, governance và FinOps](./09_platform_engineering/01_self_service_multitenancy_cost_and_governance.md)
18. [Production troubleshooting: từ symptom đến evidence xuyên tầng](./10_production_practice/00_production_troubleshooting_and_change_failure_patterns.md)
19. [Knowledge connections: DevOps / Platform Engineering ↔ Computer Science](./90_connections/00_devops_platform_cross_domain_map.md)

[`GLOSSARY.md`](./GLOSSARY.md) là tài liệu tra thuật ngữ. [`COVERAGE_AUDIT.md`](./COVERAGE_AUDIT.md) ghi rõ ranh giới (boundary / 경계), phần đã bao phủ, phần cố ý cross-link và các điểm cần kiểm tra (audit / 감사) khi mở rộng.


> **Chuyển mạch:** Từ **Trình tự đọc chi tiết**, ta sang **Nguyên tắc học** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Nguyên tắc học

Một nền tảng (platform / 플랫폼) tốt không được đánh giá bằng số lượng công cụ (tool / 도구). Nó được đánh giá bằng khả năng làm cho **đường đi đúng trở thành đường đi dễ nhất**. Vì vậy mỗi chapter cố gắng trả lời cùng một chuỗi câu hỏi: vấn đề nào buộc concept đó xuất hiện; desired bất biến (invariant / 불변식) là gì; cơ chế (mechanism / 메커니즘) giữ bất biến (invariant / 불변식) như thế nào; thất bại (failure / 실패) xảy ra ở đâu; bằng chứng (evidence / 증거) nào xác nhận giả thuyết; và lớp trừu tượng (abstraction / 추상화) nào nên được cung cấp cho người dùng nền tảng (platform / 플랫폼).

Khi gặp YAML, CLI hoặc API, hãy đọc chúng như một giao diện điều khiển trạng thái (state / 상태) chứ không phải thứ cần học thuộc. Cấu hình chỉ có ý nghĩa khi biết controller, thời gian chạy (runtime / 런타임) hoặc dịch vụ (service / 서비스) nào đọc nó, trạng thái (state / 상태) nào được tạo ra, ai là đơn vị sở hữu (owner / 오너) của trạng thái (state / 상태) đó và thất bại (failure / 실패) nào xuất hiện khi desired trạng thái (state / 상태) khác actual trạng thái (state / 상태).


> **Chuyển mạch:** Từ **Nguyên tắc học**, ta sang **chuẩn gốc (canonical / 정본) prerequisites thay vì duplicate** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chuẩn gốc (canonical / 정본) prerequisites thay vì duplicate

Để hiểu sâu tiến trình (process / 프로세스), syscall, filesystem và virtualization, dùng [Computer Science — Operating Systems](../computer_science/basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) và [privilege/isolation/virtualization](../computer_science/basic/03_operating_systems/05_privilege_isolation_and_virtualization.md). bộ chứa (container / 컨테이너) internals được đào sâu ở [namespaces, cgroups, capabilities và seccomp](../computer_science/03_operating_systems/advanced/06_containers_namespaces_cgroups_capabilities_and_seccomp.md).

Các vấn đề phân tán (distributed / 분산) thất bại (failure / 실패), thứ tự (ordering / 순서), consensus và multi-region thuộc [Networks & Distributed Systems](../computer_science/06_networks_distributed_systems/advanced/README.md). dịch vụ (service / 서비스) định danh (identity / 식별자), PKI, secrets và key vòng đời (lifecycle / 생명주기) thuộc [Security & Reliability](../computer_science/07_security_reliability/advanced/README.md). triển khai (deployment / 배포) chiến lược (strategy / 전략) và quay lui (rollback / 롤백) lý thuyết (theory / 이론) được nối sang [deployment safety](../computer_science/09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md).

DevOps thư viện (library / 라이브러리) sử dụng những nền đó để trả lời câu hỏi áp dụng: “thiết kế delivery/nền tảng (platform / 플랫폼) ra sao để nhiều nhóm (team / 팀) thay đổi môi trường vận hành (production / 운영 환경) an toàn và tự chủ?”.


> **Chuyển mạch:** Từ **chuẩn gốc (canonical / 정본) prerequisites thay vì duplicate**, ta sang **Đích đến** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Đích đến

Sau khi đi hết thư viện (library / 라이브러리), người đọc cần có khả năng nhìn một hệ thống môi trường vận hành (production / 운영 환경) như một chuỗi vòng điều khiển (control loop / 제어 루프) và đặc tả hợp đồng (contract / 계약). Có thể lần từ lần ghi nhận (commit / 커밋) đến sản phẩm tạo ra (artifact / 산출물), từ sản phẩm tạo ra (artifact / 산출물) đến tải công việc (workload / 워크로드), từ tải công việc (workload / 워크로드) đến mạng (network / 네트워크)/lưu trữ (storage / 저장소) phụ thuộc (dependency / 의존성), từ telemetry về symptom, và từ sự cố (incident / 인시던트) quay lại cải thiện nền tảng (platform / 플랫폼). Mục tiêu không phải trở thành người thuộc nhiều lệnh, mà là người có thể suy luận về hệ thống khi công cụ (tool / 도구), cloud provider hoặc tổ chức thay đổi.

> **Bàn giao:** Sau **Đích đến**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [COVERAGE AUDIT](./COVERAGE_AUDIT.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
