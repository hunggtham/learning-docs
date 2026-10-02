# Coverage kiểm tra (audit / 감사) — DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Coverage kiểm tra (audit / 감사) — DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)**. Route đi từ conceptual boundary → dependency audit → coverage theo capability → canonical ownership và cross-links → remediation queue, để audit chỉ ra phần thiếu thật và vị trí cập nhật tiếp theo.

## 1. Conceptual ranh giới (boundary / 경계)

Thư viện (library / 라이브러리) sở hữu kiến thức về delivery hệ thống (system / 시스템), hạ tầng (infrastructure / 인프라) vòng đời (lifecycle / 생명주기), orchestration usage, GitOps, khả năng quan sát (observability / 관측 가능성)/SRE, bảo mật (security / 보안) guardrail, nền tảng (platform / 플랫폼) sản phẩm (product / 제품) và môi trường vận hành (production / 운영 환경) operations. thư viện (library / 라이브러리) **không** sở hữu internals nền đã có chuẩn gốc (canonical / 정본) home trong `computer_science/`.

Các phần cố ý cross-link thay vì duplicate gồm kernel/tiến trình (process / 프로세스)/filesystem internals, namespaces/cgroups internals, phân tán (distributed / 분산) consensus/thứ tự (ordering / 순서), cryptographic giao thức (protocol / 프로토콜), PKI internals, cơ sở dữ liệu (database / 데이터베이스) internals và software kiến trúc (architecture / 아키텍처)/kiểm thử (test / 테스트)/triển khai (deployment / 배포) lý thuyết (theory / 이론) ở mức Khoa học máy tính (computer science / 컴퓨터 과학).

Ranh giới (boundary / 경계) được giữ nguyên qua các vòng đào sâu. Không tạo thêm gốc (root / 루트) thư viện (library / 라이브러리), không tách chapter theo tên sản phẩm và không biến DevOps thành danh mục (catalog / 카탈로그) Docker/Kubernetes/Terraform/cloud provider.

> **Chuyển mạch:** Trong **Coverage kiểm tra (audit / 감사) — DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)**, **1. Conceptual ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **2. phụ thuộc (dependency / 의존성) kiểm tra (audit / 감사)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **3. Coverage ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. phụ thuộc (dependency / 의존성) kiểm tra (audit / 감사)

Phụ thuộc (dependency / 의존성) chính hiện tại:

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

Bảo mật (security / 보안) thực tế là concern xuyên suốt, nhưng được đặt sau các cơ chế (mechanism / 메커니즘) chính để người đọc biết định danh (identity / 식별자)/chính sách (policy / 정책) đang bảo vệ cái gì. khả năng quan sát (observability / 관측 가능성) cũng xuyên suốt nhưng được học sau tải công việc (workload / 워크로드)/vòng điều khiển (control loop / 제어 루프) để telemetry có ngữ cảnh (context / 맥락).

Phụ thuộc (dependency / 의존성) không được hiểu như “học xong phần trước mới được đọc phần sau”. Mỗi chapter vẫn giải thích đủ ngữ cảnh (context / 맥락) cục bộ để người đọc bắt đầu tại đó. Sơ đồ trên chỉ biểu diễn mô hình tư duy (mental model / 사고 모델) nào được tái sử dụng ở phần sau.

> **Chuyển mạch:** **2. Dependency audit** xác nhận prerequisite; **3. Coverage matrix** đối chiếu owner và topic, rồi **4. Readability audit** kiểm tra người học có theo được route hay không.

## 3. Coverage ma trận (matrix / 행렬)

| năng lực (capability / 역량) | Coverage | chuẩn gốc (canonical / 정본) phụ thuộc (dependency / 의존성) / ghi chú (note / 노트) |
|---|---|---|
| DevOps operating mô hình (model / 모델), luồng (flow / 흐름), phản hồi (feedback / 피드백), quyền sở hữu (ownership / 소유권) | Đủ sâu cho nền tảng (platform / 플랫폼) lập luận (reasoning / 추론) | Có hàng đợi (queue / 큐)/WIP/batch-size, ràng buộc (constraint / 제약조건), utilization-vs-flow, phản hồi (feedback / 피드백) delay, hàng đợi (queue / 큐) discipline, ngữ nghĩa (semantic / 의미적) handoff và toil lập luận (reasoning / 추론) |
| kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) ranh giới (boundary / 경계) và cognitive tải (load / 로드) | Đủ sâu | `00_foundations`, `09_platform_engineering` |
| Linux tiến trình (process / 프로세스)/dịch vụ (service / 서비스)/tín hiệu (signal / 신호)/tài nguyên (resource / 자원) | Đủ cho môi trường vận hành (production / 운영 환경) operations | Có effective-limit composition, accept hàng đợi (queue / 큐), dirty-page/writeback và clock phụ thuộc (dependency / 의존성); internals link `computer_science/03_operating_systems` |
| Linux pressure/throttling/bằng chứng (evidence / 증거) | Đủ applied | Có PSI, cgroup hierarchy, OOM phạm vi (scope / 범위), I/O service-rate lập luận (reasoning / 추론); kernel internals vẫn giữ ở OS chuẩn gốc (canonical / 정본) |
| DNS/TCP/TLS/proxy/đường đi của yêu cầu (request path / 요청 경로) | Đủ sâu cho troubleshooting/phụ thuộc (dependency / 의존성) resilience | Có thử lại (retry / 재시도)/deadline, negative bộ nhớ đệm (cache / 캐시), pool wait, MTU black-hole, HTTP/2 thất bại (failure / 실패) phạm vi (scope / 범위), health propagation, circuit breaker, bulkhead, hedged yêu cầu (request / 요청) và draining ngữ nghĩa (semantics / 의미론); giao thức (protocol / 프로토콜) độ sâu (depth / 깊이) cross-link CS |
| Git/thay đổi (change / 변경) luồng (flow / 흐름) | Đủ theo delivery ngữ cảnh (context / 맥락) | Không biến thành Git command manual |
| Reproducible/hermetic bản dựng (build / 빌드), sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자), bộ nhớ đệm (cache / 캐시) trust | Đủ sâu | Có hidden nondeterminism, build-time mạng (network / 네트워크), independent rebuild, nền tảng (platform / 플랫폼) mục tiêu (target / 대상) định danh (identity / 식별자) và generated-code/toolchain inputs |
| CI/CD, flaky tests, tính đồng thời (concurrency / 동시성), stale bằng chứng (evidence / 증거), di chuyển (migration / 마이그레이션) an toàn (safety / 안전) | Đủ sâu | Có superseded công việc (work / 작업), stale approval, shared-test-environment coupling, paused bản phát hành (release / 릴리스), comparative xác minh (verification / 확인), merge hàng đợi (queue / 큐), online schema-change rủi ro (risk / 위험), backfill, dual-write và consumer-lag đặc tả hợp đồng (contract / 계약) evolution |
| ảnh bộ chứa (container image / 컨테이너 이미지)/thời gian chạy (runtime / 런타임)/bản dựng (build / 빌드)/bảo mật (security / 보안)/tài nguyên (resource / 자원) | Đủ môi trường vận hành (production / 운영 환경) độ sâu (depth / 깊이) | Có ảnh (image / 이미지) pull/khôi phục (recovery / 복구), thời gian chạy (runtime / 런타임) override precedence, startup spike, init ngữ nghĩa (semantics / 의미론), writable-path đặc tả hợp đồng (contract / 계약), bên ngoài (external / 외부) side-effect ranh giới (boundary / 경계) và config-cohort lập luận (reasoning / 추론); internals link OS |
| IaC desired trạng thái (state / 상태)/trạng thái (state / 상태)/drift/modules/import/partial thất bại (failure / 실패) | Đủ sâu | Có unknown values, replacement thứ tự (ordering / 순서)/headroom, bên ngoài (external / 외부) lookup stability, trạng thái (state / 상태) khôi phục (recovery / 복구) và plan-vs-actual chính sách (policy / 정책) ranh giới (boundary / 경계) |
| Cloud IAM/mạng (network / 네트워크)/compute/lưu trữ (storage / 저장소)/miền lỗi (failure domain / 장애 도메인) | Đủ môi trường vận hành (production / 운영 환경) độ sâu (depth / 깊이) | Có API rate-limit, zonal sức chứa (capacity / 용량) scarcity, failure-state sức chứa (capacity / 용량), replication bandwidth/lag và private-endpoint composition; provider danh mục (catalog / 카탈로그) không duplicate |
| Kubernetes điều khiển (control / 제어) plane/reconciliation | Đủ sâu | Có optimistic tính đồng thời (concurrency / 동시성), watch/resync, công việc (work / 작업) hàng đợi (queue / 큐)/backoff, admission, API saturation, finalizer, đơn vị sở hữu (owner / 오너) đồ thị (graph / 그래프), bộ nhớ đệm (cache / 캐시) staleness, leader-election/fencing ranh giới (boundary / 경계) và control-plane fairness |
| Kubernetes tải công việc (workload / 워크로드)/mạng (network / 네트워크)/lưu trữ (storage / 저장소)/resources/autoscaling | Đủ sâu | Có schedulable-vs-aggregate sức chứa (capacity / 용량), PDB, topology, termination race, lưu trữ (storage / 저장소) attach/fencing, ephemeral lưu trữ (storage / 저장소), Job/CronJob nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론) và endpoint-churn chi phí (cost / 비용) |
| GitOps | Đủ sâu | Có trường dữ liệu (field / 필드) quyền sở hữu (ownership / 소유권), quay lui (rollback / 롤백) limits, revision-vs-serving distinction, deterministic rendering, prune ngữ nghĩa (semantics / 의미론), readiness-vs-ordering, multi-cluster fan-out và decrypt trust đường dẫn (path / 경로) |
| Metrics/logs/traces/events/alerting | Đủ sâu | Có telemetry-pipeline thất bại (failure / 실패), missing-vs-zero, freshness, counter reset, duplicate/reordering, lược đồ (schema / 스키마) evolution, observer tác động (effect / 효과), sampling độ lệch (bias / 편향), cardinality, percentile, priority under overload, backend multi-tenancy, retention và signal-cost attribution |
| SLI/SLO/lỗi (error / 오류) ngân sách (budget / 예산)/sức chứa (capacity / 용량)/backpressure | Đủ sâu | Có burn-rate, Little's Law, thử lại (retry / 재시도)/admission/tính đồng thời (concurrency / 동시성) ngân sách (budget / 예산), failover headroom, low-traffic ngữ nghĩa (semantics / 의미론), denominator/cửa sổ (window / 윈도우) tính đúng đắn (correctness / 정확성), async-work SLI, composite journey và đo lường (measurement / 측정) versioning |
| sự cố (incident / 인시던트)/postmortem/runbook | Đủ sâu | Có recovery-vs-root-cause, quyết định (decision / 결정) log, exit criteria, counterfactual/cohort lập luận (reasoning / 추론), nhân quả (causal / 인과적) đồ thị (graph / 그래프), intervention ngữ nghĩa (semantics / 의미론), mutation coordination, detector coverage và multi-loop oscillation |
| Backup/RPO/RTO/DR/chaos | Đủ sâu | Có consistency ranh giới (boundary / 경계), PITR chuỗi (chain / 사슬), DR bootstrap, fencing/failback, backlog-drain khôi phục (recovery / 복구), business-data kiểm tra hợp lệ (validation / 검증), immutable/cyber-recovery ranh giới (boundary / 경계) và experiment validity |
| IAM/tải công việc (workload / 워크로드) định danh (identity / 식별자)/secrets/chính sách (policy / 정책) | Đủ sâu ở nền tảng (platform / 플랫폼) tầng (layer / 계층) | Có confused deputy, authority propagation, TOCTOU, revocation, rotation-completion bằng chứng (evidence / 증거), break-glass vòng đời (lifecycle / 생명주기), kiểm tra (audit / 감사)→enforce rollout, fail-open/fail-closed và stale-principal/offboarding ngữ nghĩa (semantics / 의미론) |
| Supply chuỗi (chain / 사슬)/SBOM/provenance/signing | Đủ sâu về trust mô hình (model / 모델) | Có verifier trust chính sách (policy / 정책), CI untrusted-code ranh giới (boundary / 경계), phụ thuộc (dependency / 의존성) thực thi (execution / 실행) trust, subject-bound bằng chứng (evidence / 증거) chuỗi (chain / 사슬) và audit-evidence integrity |
| nền tảng (platform / 플랫폼) as sản phẩm (product / 제품)/golden đường dẫn (path / 경로)/IDP/danh mục (catalog / 카탈로그) | Đủ sâu | Có điều khiển (control / 제어)/mặt phẳng dữ liệu (data plane / 데이터 플레인), async vòng đời (lifecycle / 생명주기), idempotency, delete/cancel/compensate/adopt ngữ nghĩa (semantics / 의미론), bootstrap khôi phục (recovery / 복구), control-plane trạng thái (state / 상태) durability, safe chế độ (mode / 모드), admission priority, DR thứ tự (ordering / 순서), deprecation, cells và supportability |
| Self-service/multi-tenancy/quota/quản trị (governance / 거버넌스) | Đủ sâu | Có isolation theo thất bại (failure / 실패)/threat mô hình (model / 모델), control-plane fairness, blast-radius ngân sách (budget / 예산), tenant-aware SLO, khôi phục (recovery / 복구) tính đồng thời (concurrency / 동시성), reservation/borrowing/reclamation, preemption và khôi phục (recovery / 복구)/operator-path isolation |
| FinOps/chi phí (cost / 비용) attribution/rightsizing | Đủ sâu cho nền tảng (platform / 플랫폼) lập luận (reasoning / 추론) | Có showback/chargeback, đơn vị (unit / 단위) economics, commitment caveat, externality attribution, intentional reserve, recoverable sức chứa (capacity / 용량) và isolation-fragmentation sự đánh đổi (trade-off / 트레이드오프) |
| Cross-layer troubleshooting | Đủ sâu | Có độ trễ (latency / 지연 시간) decomposition, coordinated omission, hết thời gian chờ (timeout / 타임아웃)/cancellation, khôi phục (recovery / 복구) storm, bằng chứng (evidence / 증거) freshness, nhân quả (causal / 인과적) intervention và worked thất bại (failure / 실패) cases |
| Cross-domain links | Đủ | `90_connections` có 20 lập luận (reasoning / 추론) tuyến (route / 경로) xuyên lĩnh vực (domain / 도메인) |

> **Chuyển mạch:** Sau khi topic và owner khớp, **4. Readability audit** kiểm tra prose, bảng và link; **5. Duplicate audit** tìm phần lấn owner hoặc lặp claim.

## 4. Readability kiểm tra (audit / 감사)

Mỗi chapter mở đầu từ bài toán (problem / 문제)/mô hình tư duy (mental model / 사고 모델) trước API/công cụ (tool / 도구). Lệnh chỉ xuất hiện khi chúng kiểm tra một hypothesis cụ thể. Các khái niệm `desired state`, `actual state`, `reconciliation`, `artifact`, `blast radius`, `SLI/SLO`, `golden path` được định nghĩa trước khi dùng sâu và có glossary.

Giải thích dùng tiếng Việt; tên API/sản phẩm (product / 제품)/lệnh giữ nguyên. Thuật ngữ Hàn chỉ thêm khi có giá trị nhận diện, không ép ba ngôn ngữ vào mọi câu.

Độ sâu (depth / 깊이) pass hiện tại ưu tiên đoạn văn giải thích cơ chế, giả định (assumption / 가정) và thất bại (failure / 실패) chuỗi (chain / 사슬). Các danh sách chỉ còn dùng cho taxonomy, chuỗi (sequence / 시퀀스) hoặc checklist mà bản thân cấu trúc danh sách tạo giá trị.

> **Chuyển mạch:** **5. Duplicate audit** xử lý trùng lặp sau khi readability đã rõ; **6. Modern và legacy perspective** đặt gap vào bối cảnh version và hệ thống cũ.

## 5. Duplicate kiểm tra (audit / 감사)

Không tạo chapter riêng về Linux kernel, phân tán (distributed / 분산) consensus, OAuth/OIDC, cơ sở dữ liệu (database / 데이터베이스) WAL/MVCC hay generic software kiến trúc (architecture / 아키텍처) vì các phần đó đã có chuẩn gốc (canonical / 정본) docs.

Bộ chứa (container / 컨테이너) chapter link trực tiếp OS bộ chứa (container / 컨테이너) internals. Kubernetes chapter link thất bại (failure / 실패) detector/consensus/fencing. bảo mật (security / 보안) chapter link PKI/secrets. CI/CD chapter link triển khai (deployment / 배포) an toàn (safety / 안전). Connections tệp (file / 파일) ghi ranh giới (boundary / 경계) rõ để lần mở rộng sau không bản sao (copy / 복사) nội dung.

Sau độ sâu (depth / 깊이) pass, không xuất hiện thư viện (library / 라이브러리)/chapter duplicate, tệp (file / 파일) `_updated`, `_final`, `_version2` hoặc temporary ghi chú (note / 노트) mới. Nội dung mới được bổ sung trực tiếp vào tệp chuẩn gốc (canonical file / 정본 파일) hiện hữu.

> **Chuyển mạch:** **6. Modern/legacy perspective** phân biệt thay đổi mới với invariant cũ; **7. Production evidence audit** kiểm tra claim bằng log, metric và hành vi runtime.

## 6. hiện đại (modern / 현대적) và legacy perspective

Thư viện (library / 라이브러리) dùng control-loop, immutable sản phẩm tạo ra (artifact / 산출물), tải công việc (workload / 워크로드) định danh (identity / 식별자), GitOps, policy-as-code và self-service như practice hiện đại. Legacy approach như manual máy chủ (server / 서버) mutation, mutable tag, long-lived credential, push triển khai (deployment / 배포) quyền rộng và ticket-based provisioning được giữ dưới dạng contrast/dạng thất bại (failure mode / 실패 모드), không tạo một “legacy tutorial” riêng.

Điều này giúp người đọc nhận ra hệ thống cũ trong công việc mà không học thói quen cũ như default.

Hiện đại (modern / 현대적) không được đồng nghĩa với “công nghệ mới hơn”. Một practice chỉ được ưu tiên khi nó cải thiện bất biến (invariant / 불변식), phản hồi (feedback / 피드백), isolation, operability hoặc nhà phát triển (developer / 개발자) experience. công cụ (tool / 도구) mới không tự tạo chapter nếu không tạo mô hình tư duy (mental model / 사고 모델) mới.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Coverage kiểm tra (audit / 감사) — DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)**, **6. hiện đại (modern / 현대적) và legacy perspective** nêu điều cần giải thích; **7. bằng chứng vận hành (production evidence / 운영 증거) kiểm tra (audit / 감사)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. bảo mật (security / 보안) kiểm tra (audit / 감사)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. bằng chứng vận hành (production evidence / 운영 증거) kiểm tra (audit / 감사)

Các chapter đều nối concept với bằng chứng (evidence / 증거): tiến trình (process / 프로세스)/socket `/proc`, PSI/throttling/writeback/accept-queue tín hiệu (signal / 신호), DNS resolver/bộ nhớ đệm (cache / 캐시)/liên kết (connection / 연결)/draining/breaker bằng chứng (evidence / 증거), triển khai (deployment / 배포) sự kiện (event / 이벤트), sản phẩm tạo ra (artifact / 산출물) digest/provenance/toolchain định danh (identity / 식별자), di chuyển (migration / 마이그레이션)/backfill/discrepancy/consumer-adoption trạng thái (state / 상태), IaC plan/trạng thái (state / 상태)/remote actual trạng thái (state / 상태), cloud quota/rate-limit/sức chứa (capacity / 용량) status, Kubernetes generation/conditions/events/lưu trữ (storage / 저장소) attach trạng thái (state / 상태)/controller hàng đợi (queue / 큐), GitOps observed/applied/serving revision, telemetry chuỗi xử lý (pipeline / 파이프라인)/freshness/drop/priority/query-cost tín hiệu (signal / 신호), SLO đo lường (measurement / 측정) revision/denominator/cửa sổ (window / 윈도우), khôi phục (recovery / 복구)/backlog/data-integrity tín hiệu (signal / 신호), authority/rotation/chính sách (policy / 정책) bằng chứng (evidence / 증거), platform-state/adoption/safe-mode status, tenancy/fairness/reclamation/chi phí (cost / 비용) attribution và nhật ký kiểm tra (audit log / 감사 로그).

Các worked thất bại (failure / 실패) trường hợp (case / 사례) quan trọng đều cố gắng giữ chuỗi nhân quả (causal chain / 인과 사슬) `symptom → hypothesis → evidence → layer → mitigation → verify`, thay vì biến thành danh sách lệnh. Các vòng độ sâu (depth / 깊이) gần đây bổ sung counterfactual/cohort comparison, detector độ tin cậy (reliability / 신뢰성), transition-state sức chứa (capacity / 용량), sensor freshness, recovery-convergence bằng chứng (evidence / 증거) và intervention/counterfactual discipline để tránh kết luận nhân quả quá sớm.

> **Chuyển mạch:** Trong **Coverage kiểm tra (audit / 감사) — DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)**, **7. bằng chứng vận hành (production evidence / 운영 증거) kiểm tra (audit / 감사)** nêu điều cần giải thích; **8. bảo mật (security / 보안) kiểm tra (audit / 감사)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. hiệu năng (performance / 성능) và sức chứa (capacity / 용량) kiểm tra (audit / 감사)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. bảo mật (security / 보안) kiểm tra (audit / 감사)

Bảo mật (security / 보안) được trải từ nguồn (source / 소스)/bản dựng (build / 빌드) → CI runner → sản phẩm tạo ra (artifact / 산출물)/registry → GitOps repository → tải công việc (workload / 워크로드) định danh (identity / 식별자) → secrets → admission/chính sách (policy / 정책) → break-glass. Không coi “private mạng (network / 네트워크)”, “private repository”, “signed sản phẩm tạo ra (artifact / 산출물)” hay “short-lived đơn vị từ (token / 토큰)” là trust ranh giới (boundary / 경계) đầy đủ nếu authorization phạm vi (scope / 범위) hoặc verifier chính sách (policy / 정책) vẫn rộng.

Bảo mật (security / 보안) điều khiển (control / 제어) nằm trên môi trường vận hành (production / 운영 환경) điều khiển (control / 제어) đường dẫn (path / 경로) như admission/chính sách (policy / 정책) cũng được xem như môi trường vận hành (production / 운영 환경) software: cần kiểm thử (test / 테스트), staged rollout, telemetry và quay lui (rollback / 롤백)/fail-open/fail-closed quyết định (decision / 결정) có chủ đích.

Vòng độ sâu (depth / 깊이) trước kiểm tra effective authority: caller định danh (identity / 식별자) phải được bind với requested mục tiêu (target / 대상) trước khi automation định danh (identity / 식별자) mạnh hơn thực hiện hành động (action / 동작); đơn vị từ (token / 토큰) forwarding không được mặc định đồng nghĩa authority forwarding; chính sách (policy / 정책)/bằng chứng (evidence / 증거) phải bind vào immutable subject/revision để tránh TOCTOU.

Bản dựng (build / 빌드)/GitOps độ sâu (depth / 깊이) cũng củng cố chain-of-custody: sản phẩm tạo ra (artifact / 산출물) bằng chứng (evidence / 증거) phải bind đúng digest/mục tiêu (target / 대상) variant; desired-state rendering cần declared inputs; encrypted Git secret vẫn có decrypt định danh (identity / 식별자)/KMS vòng đời (lifecycle / 생명주기) riêng. DR độ sâu (depth / 깊이) tách region/hạ tầng (infrastructure / 인프라) disaster khỏi cyber khôi phục (recovery / 복구), nơi backup/điều khiển (control / 제어) plane/credential có thể cùng nằm trong threat mô hình (model / 모델).

Vòng authority-lifecycle bổ sung rotation completion dựa trên bên tiêu thụ (consumer / 소비자) bằng chứng (evidence / 증거), break-glass như privileged-session vòng đời (lifecycle / 생명주기), chính sách (policy / 정책) kiểm tra (audit / 감사)→enforce di chuyển (migration / 마이그레이션), fail-open/fail-closed đặc tả hợp đồng (contract / 계약), offboarding/stale-principal reconciliation, least-privilege rà soát (review / 검토) có rare-path ngữ cảnh (context / 맥락) và integrity/retention ranh giới (boundary / 경계) cho privileged kiểm tra (audit / 감사) bằng chứng (evidence / 증거).

> **Chuyển mạch:** **8. Security audit** đặt rào chắn trước khi đo; **9. Performance/capacity audit** lượng hóa tải, rồi **10. Coverage cố ý chưa tách chapter** ghi rõ phần chưa mở rộng.

## 9. hiệu năng (performance / 성능) và sức chứa (capacity / 용량) kiểm tra (audit / 감사)

Thư viện (library / 라이브러리) hiện nối hiệu năng (performance / 성능) từ Linux/cgroup pressure lên mạng (network / 네트워크) phụ thuộc (dependency / 의존성) isolation, bộ chứa (container / 컨테이너) startup/hành vi thời gian chạy (runtime behavior / 런타임 동작), Kubernetes scheduling/autoscaling/lưu trữ (storage / 저장소) attach, cloud provisioning/API/physical-capacity độ trễ (latency / 지연 시간), khả năng quan sát (observability / 관측 가능성) backend và SRE hàng đợi (queue / 큐)/sức chứa (capacity / 용량) mô hình (model / 모델).

Phần DevOps chỉ giữ hiệu năng (performance / 성능) ở mức operational lập luận (reasoning / 추론): saturation, headroom, hàng đợi (queue / 큐), throttling, warm-up, liên kết (connection / 연결) ngân sách (budget / 예산), breaker/bulkhead/hedge amplification, I/O dịch vụ (service / 서비스) tỷ lệ (rate / 비율), admission điều khiển (control / 제어), failover sức chứa (capacity / 용량) và bằng chứng (evidence / 증거). CPU kiến trúc (architecture / 아키텍처), scheduler thuật toán (algorithm / 알고리즘), virtual bộ nhớ (memory / 메모리), page-table hoặc formal queueing độ sâu (depth / 깊이) sâu hơn vẫn thuộc Khoa học máy tính (computer science / 컴퓨터 과학)/Mathematics chuẩn gốc (canonical / 정본) docs.

Sức chứa (capacity / 용량) không còn được hiểu chỉ là peak thông lượng (throughput / 처리량) hay steady-state utilization. kiểm tra (audit / 감사) hiện kiểm tra cả transition-state headroom cho replace/surge, khôi phục (recovery / 복구) tính đồng thời (concurrency / 동시성)/backlog drain, thất bại (failure / 실패) headroom, correlated thất bại (failure / 실패), control-plane tỷ lệ (rate / 비율) limit, vật lý (physical / 물리적) sức chứa (capacity / 용량) scarcity, fairness, intentional idle reserve, borrowed-capacity reclamation và khả năng quan sát (observability / 관측 가능성) sự cố (incident / 인시던트) tính đồng thời (concurrency / 동시성).

> **Chuyển mạch:** Khi gap có chủ đích đã ghi, **11. Internal-link checklist** xác nhận route và owner vẫn truy được dù chapter chưa tách.

## 10. Coverage cố ý chưa tách chapter

Dịch vụ (service / 서비스) mesh, eBPF, Crossplane, OpenTofu/Terraform sản phẩm (product / 제품) details, Helm/Argo CD/Flux, specific cloud provider, Backstage, Vault, Prometheus/Grafana, Jenkins/GitHub Actions/GitLab CI không có chapter riêng chỉ vì phổ biến. Chúng nên được dùng như hiện thực (implementation / 구현) example trong concept chapter khi cần.

Dịch vụ (service / 서비스) mesh hiện chưa cần chapter riêng vì control-plane/data-plane, mTLS định danh (identity / 식별자), thử lại (retry / 재시도)/hết thời gian chờ (timeout / 타임아웃), circuit-breaker/bulkhead ngữ nghĩa (semantics / 의미론) và routing thất bại (failure / 실패) đã có prerequisite ở mạng (network / 네트워크), bảo mật (security / 보안) và Kubernetes. Chỉ nên tách khi cần một lập luận (reasoning / 추론) đường dẫn (path / 경로) mới mà các chapter hiện tại không còn chứa tự nhiên được.

eBPF cũng không nên trở thành chapter DevOps chỉ vì khả năng quan sát (observability / 관측 가능성)/networking hiện đại sử dụng nó. Kernel thực thi (execution / 실행)/verifier/hook internals thuộc Khoa học máy tính (computer science / 컴퓨터 과학); DevOps chỉ cần đưa eBPF công cụ (tool / 도구) vào ví dụ nếu nó giúp thu bằng chứng (evidence / 증거) cho một hypothesis cụ thể.

> **Chuyển mạch:** **11. Internal-link checklist** đảm bảo đường đọc không gãy; **12. Dependency-hidden audit** tìm prerequisite ẩn sau khi nội dung đã được coi là depth pass.

## 11. Internal-link kiểm tra (audit / 감사) checklist

Các link từ DevOps sang Khoa học máy tính (computer science / 컴퓨터 과학) dùng relative đường dẫn (path / 경로) từ chapter hiện tại. README dùng direct `.md` links cho reading chuỗi (sequence / 시퀀스) thay vì phụ thuộc directory điều hướng (navigation / 내비게이션). Các cross-link chính trỏ tới chuẩn gốc (canonical / 정본) OS, phân tán (distributed / 분산) các hệ thống (systems / 시스템들), bảo mật (security / 보안), Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) và cơ sở dữ liệu (database / 데이터베이스) docs hiện có.

Khi đổi tên/move chuẩn gốc (canonical / 정본) CS chapter, cần cập nhật các link trong `README.md`, thời gian chạy (runtime / 런타임)/bộ chứa (container / 컨테이너), Kubernetes, bảo mật (security / 보안) và `90_connections`.

Không tạo link giả đến chapter tool-specific chưa tồn tại. Link tới sản phẩm (product / 제품) documentation bên ngoài cũng không được dùng để thay thế prerequisite nội bộ nếu repository đã có chuẩn gốc (canonical / 정본) explanation.

> **Chuyển mạch:** Sau khi lộ prerequisite ẩn, **13. Naming và canonical-state audit** kiểm tra tên, trạng thái và nguồn chuẩn để tránh drift giữa file.

## 12. Dependency-hidden kiểm tra (audit / 감사) sau độ sâu (depth / 깊이) pass

Các prerequisite dễ bị coi là “ai cũng biết” đã được làm rõ thêm trong chuẩn gốc (canonical / 정본) chapter thay vì tách tệp (file / 파일) mới: hàng đợi (queue / 큐)/WIP/ràng buộc (constraint / 제약조건)/phản hồi (feedback / 피드백) delay ở Foundations; pressure/tài nguyên (resource / 자원) ranh giới (boundary / 경계)/writeback/accept hàng đợi (queue / 큐)/clock ở Linux; deadline/thử lại (retry / 재시도)/bộ nhớ đệm (cache / 캐시)/liên kết (connection / 연결) pool/MTU/breaker/bulkhead/draining ở mạng (network / 네트워크); hermetic/reproducible/toolchain/remote đầu vào (input / 입력) ở bản dựng (build / 빌드); tính đồng thời (concurrency / 동시성)/stale bằng chứng (evidence / 증거)/approval/kiểm thử (test / 테스트) isolation/lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션)/backfill/dual-write/bên tiêu thụ (consumer / 소비자) lag ở CI; tầng (layer / 계층)/thời gian chạy (runtime / 런타임)/startup/effective cấu hình (config / 설정) ở bộ chứa (container / 컨테이너); trạng thái (state / 상태)/partial thất bại (failure / 실패)/unknown giá trị (value / 값)/chuyển tiếp (transition / 전이) headroom ở IaC; control-plane eventual hành vi (behavior / 동작)/API sức chứa (capacity / 용량)/vật lý (physical / 물리적) scarcity ở Cloud; reconciliation/trường dữ liệu (field / 필드) quyền sở hữu (ownership / 소유권)/vòng đời (lifecycle / 생명주기) đồ thị (graph / 그래프)/lưu trữ (storage / 저장소) fencing/batch ngữ nghĩa (semantics / 의미론) ở Kubernetes/GitOps; missing-data/freshness/sampling/lược đồ (schema / 스키마)/priority/retention/backend-fairness ngữ nghĩa (semantics / 의미론) ở khả năng quan sát (observability / 관측 가능성); low-traffic/denominator/cửa sổ (window / 윈도우)/async/composite ngữ nghĩa (semantics / 의미론) ở SRE; khôi phục (recovery / 복구) exit criteria/backlog/dữ liệu (data / 데이터) integrity ở sự cố (incident / 인시던트)/DR; rotation/break-glass/chính sách (policy / 정책)/offboarding/audit-evidence vòng đời (lifecycle / 생명주기) ở bảo mật (security / 보안); async vòng đời (lifecycle / 생명주기)/idempotency/cancellation/compensation/adoption/bootstrap/trạng thái (state / 상태) durability/safe chế độ (mode / 모드)/DR thứ tự (ordering / 순서) ở nền tảng (platform / 플랫폼); isolation/fairness/khôi phục (recovery / 복구)/reclamation/preemption ở Multi-tenancy; nhân quả (causal / 인과적) đồ thị (graph / 그래프)/intervention/detector coverage ở môi trường vận hành (production / 운영 환경) Practice.

Điểm này quan trọng vì một chapter có thể dài nhưng vẫn có prerequisite ẩn. Coverage hiện được đánh giá theo lập luận nhân quả (causal reasoning / 인과적 추론), không theo số heading hoặc số dòng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Coverage kiểm tra (audit / 감사) — DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)**, sau nội dung của **12. Dependency-hidden kiểm tra (audit / 감사) sau độ sâu (depth / 깊이) pass**, **13. Naming và canonical-state kiểm tra (audit / 감사)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **14. Criteria cho lần mở rộng tiếp theo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Naming và canonical-state kiểm tra (audit / 감사)

Gốc (root / 루트) lĩnh vực (domain / 도메인) duy nhất là `devops_platform_engineering/`. Các subdomain dùng numbering theo phụ thuộc (dependency / 의존성) `00` → `10`, sau đó `90_connections`. Không có gốc (root / 루트) DevOps thứ hai hoặc chapter trùng tên cần consolidate.

Các tệp (file / 파일) hiện tại đều có vai trò chuẩn gốc (canonical / 정본) rõ; không có raw/nguồn (source / 소스) trong lĩnh vực (domain / 도메인) cần sửa. `GLOSSARY.md`, `LANGUAGE_STYLE.md` và `COVERAGE_AUDIT.md` là tài liệu hỗ trợ, không cạnh tranh với chapter chính.

Branch lĩnh vực (domain / 도메인) duy nhất là `feat/devops-platform-engineering-knowledge-library`; không phát hiện branch DevOps/kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thứ hai cần hợp nhất hoặc xóa.

Branch đã từng được sync với `main` trước các vòng độ sâu (depth / 깊이); trạng thái ahead/behind phải được kiểm tra lại ở cuối mỗi editing pass vì repository có thể nhận lần ghi nhận (commit / 커밋) song song trong lúc lĩnh vực (domain / 도메인) đang được đào sâu.

> **Chuyển mạch:** **13. Naming/canonical-state audit** khóa vocabulary và state; **14. Criteria mở rộng** chỉ cho phép thêm topic khi invariant và failure semantics đã đủ.

## 14. Criteria cho lần mở rộng tiếp theo

Một chapter mới chỉ nên được thêm nếu đáp ứng ít nhất một điều kiện: tạo mô hình tư duy (mental model / 사고 모델) mới; giải một thất bại (failure / 실패) lớp (class / 클래스) quan trọng chưa có; bổ sung bằng chứng vận hành (production evidence / 운영 증거); hoặc nối nhiều lớp thành lập luận (reasoning / 추론) đường dẫn (path / 경로) mới mà việc nhét vào tệp chuẩn gốc (canonical file / 정본 파일) hiện tại làm mất conceptual ranh giới (boundary / 경계).

Nếu nhu cầu mới chủ yếu là cú pháp (syntax / 문법) hoặc sản phẩm — ví dụ “cách viết Helm chart”, “lệnh Argo CD”, “Terraform provider X” — ưu tiên example/tham chiếu (reference / 참조) bên trong chapter hiện có hoặc tài liệu thực hành riêng nếu repository sau này có ranh giới (boundary / 경계) cho labs. Không dùng số lượng chapter làm thước đo hoàn thành.

> **Chuyển mạch:** **15. Invariants/failure semantics** xác nhận mental model; **16. Source-to-runtime và transition-state pass** kiểm tra nó qua đường đi từ tài liệu đến runtime.

## 15. Invariants/failure-semantics độ sâu (depth / 깊이) pass

Một vòng đào sâu trước đó cố ý không mở chapter mới và tăng lập luận (reasoning / 추론) density ở các chuẩn gốc (canonical / 정본) area phía control-plane/nền tảng (platform / 플랫폼).

Kubernetes được bổ sung delete/finalizer giao thức (protocol / 프로토콜), đơn vị sở hữu (owner / 오너) đồ thị (graph / 그래프), leader-election/fencing ranh giới (boundary / 경계), informer-cache staleness, status-condition đặc tả hợp đồng (contract / 계약), CRD evolution và control-plane fairness. SRE được bổ sung admission/tính đồng thời (concurrency / 동시성) điều khiển (control / 제어), failover sức chứa (capacity / 용량), correlated thất bại (failure / 실패), brownout và error-budget chính sách (policy / 정책) như phản hồi (feedback / 피드백) controller. bảo mật (security / 보안) được bổ sung confused deputy, authority propagation, TOCTOU, revocation propagation và control-plane compromise blast radius.

Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) được bổ sung bất biến (invariant / 불변식) đằng sau `Ready`, end-to-end idempotency, delete retention ngữ nghĩa (semantics / 의미론), fault-containment cell, tested tính tương thích (compatibility / 호환성) set và abstraction-leak phản hồi (feedback / 피드백). Multi-tenancy/FinOps được bổ sung fairness, blast-radius ngân sách (budget / 예산), tenant-aware SLO, khôi phục (recovery / 복구) tính đồng thời (concurrency / 동시성), externality attribution, intentional reserve và vòng đời (lifecycle / 생명주기) của chính sách (policy / 정책)/exception.

Môi trường vận hành (production / 운영 환경) Practice được bổ sung counterfactual/cohort lập luận (reasoning / 추론), tương tác (interaction / 상호작용) của nhiều vòng phản hồi (feedback loop / 피드백 루프), hết thời gian chờ (timeout / 타임아웃) không cancel công việc (work / 작업), khôi phục (recovery / 복구) storm, tường minh (explicit / 명시적) brownout bằng chứng (evidence / 증거), timeline bất định (uncertainty / 불확실성) và detector/negative-evidence ngữ nghĩa (semantics / 의미론).

Các phần này đều tạo mô hình tư duy (mental model / 사고 모델)/thất bại (failure / 실패) lớp (class / 클래스) mới và đã được nối lại trong `90_connections`, thay vì tồn tại như các đoạn cấp cao (senior / 시니어) ghi chú (note / 노트) rời rạc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Coverage kiểm tra (audit / 감사) — DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)**, **15. Invariants/failure-semantics độ sâu (depth / 깊이) pass** nêu điều cần giải thích; **16. Source-to-runtime và transition-state độ sâu (depth / 깊이) pass** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. luồng (flow / 흐름), sensor và recovery-convergence độ sâu (depth / 깊이) pass** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Source-to-runtime và transition-state độ sâu (depth / 깊이) pass

Vòng đào sâu tiếp theo giữ nguyên chuẩn gốc (canonical / 정본) cấu trúc (structure / 구조) nhưng tăng độ sâu từ nguồn (source / 소스) cho tới tải công việc (workload / 워크로드) thời gian chạy (runtime / 런타임).

Linux bổ sung dirty-page/writeback stall, listen/accept hàng đợi (queue / 큐), effective limit composition và clock phụ thuộc (dependency / 의존성). mạng (network / 네트워크) bổ sung negative DNS caching, connection-pool hàng đợi (queue / 큐), đường dẫn (path / 경로) MTU black-hole, HTTP/2 multiplexing thất bại (failure / 실패) phạm vi (scope / 범위) và load-balancer health propagation. bản dựng (build / 빌드) bổ sung nondeterministic đầu vào (input / 입력), build-time mạng (network / 네트워크) trust, independent rebuild, mục tiêu (target / 대상) kiến trúc (architecture / 아키텍처) định danh (identity / 식별자) và generated-code/toolchain closure. CI/CD bổ sung superseded-work cancellation ngữ nghĩa (semantics / 의미론), subject-bound approval, dùng chung (shared / 공유) môi trường (environment / 환경) coupling, paused bản phát hành (release / 릴리스) trạng thái (state / 상태), cohort comparison và merge-queue sức chứa (capacity / 용량).

Bộ chứa (container / 컨테이너) bổ sung image-vs-runtime precedence, init-container limitation, startup tài nguyên (resource / 자원) spike, tường minh (explicit / 명시적) writable đường dẫn (path / 경로), external-side-effect ranh giới (boundary / 경계) và config-revision cohorts. IaC bổ sung unknown values, replacement thứ tự (ordering / 순서), chuyển tiếp (transition / 전이) headroom, remote lookup stability, trạng thái (state / 상태) khôi phục (recovery / 복구) và pre/post-apply chính sách (policy / 정책) ranh giới (boundary / 경계). Cloud bổ sung control-plane API sức chứa (capacity / 용량), zonal vật lý (physical / 물리적) sức chứa (capacity / 용량) scarcity, N-1/failure-state headroom, replication bandwidth/lag và private endpoint composition.

Kubernetes tải công việc (workload / 워크로드) bổ sung lưu trữ (storage / 저장소) topology/attach fencing, StatefulSet-vs-data bất biến (invariant / 불변식), ephemeral-storage pressure, Job/CronJob nghiệp vụ (business / 비즈니스) idempotency và endpoint churn. GitOps bổ sung observed/applied/serving revision separation, repository outage ngữ nghĩa (semantics / 의미론), deterministic rendering, prune rủi ro (risk / 위험), readiness-vs-ordering, multi-cluster rollout và decrypt/KMS đường dẫn (path / 경로).

Mô hình tư duy (mental model / 사고 모델) chung của vòng này là **steady trạng thái (state / 상태) không đủ để đánh giá an toàn (safety / 안전)**. Phải lập luận (reasoning / 추론) cả chuyển tiếp (transition / 전이) trạng thái (state / 상태): bản dựng (build / 빌드) đầu vào (input / 입력) thay đổi, bản phát hành (release / 릴리스) bằng chứng (evidence / 증거) stale, replacement/surge cần headroom, failover cần sức chứa (capacity / 용량), controller cần thời gian hội tụ và stateful quyền sở hữu (ownership / 소유권) transfer cần fencing.

> **Chuyển mạch:** Trong **Coverage kiểm tra (audit / 감사) — DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)**, **16. Source-to-runtime và transition-state độ sâu (depth / 깊이) pass** nêu điều cần giải thích; **17. luồng (flow / 흐름), sensor và recovery-convergence độ sâu (depth / 깊이) pass** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. đo lường (measurement / 측정), authority-lifecycle và platform-recovery độ sâu (depth / 깊이) pass** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. luồng (flow / 흐름), sensor và recovery-convergence độ sâu (depth / 깊이) pass

Vòng tiếp theo tiếp tục không mở chapter mới, mà tăng độ sâu (depth / 깊이) ở ba chỗ quyết định chất lượng lập luận (reasoning / 추론) môi trường vận hành (production / 운영 환경).

Foundations được bổ sung Theory-of-Constraints style lập luận (reasoning / 추론) ở mức applied: bottleneck/ràng buộc (constraint / 제약조건) quyết định thông lượng (throughput / 처리량), utilization cao có thể làm hàng đợi (queue / 큐) delay xấu, phản hồi (feedback / 피드백) delay tạo over-correction, hàng đợi (queue / 큐) discipline/expedite cần chính sách (policy / 정책), handoff làm mất ngữ nghĩa (semantic / 의미적) intent và toil phải được đánh giá cùng chi phí (cost / 비용)/rủi ro (risk / 위험) của automation.

Khả năng quan sát (observability / 관측 가능성) được bổ sung missing-vs-zero, counter reset/vòng đời (lifecycle / 생명주기), at-least-once log duplicate/reordering, telemetry lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성), observer tác động (effect / 효과), sampling-selection độ lệch (bias / 편향), black-box-vs-white-box perspective và stale-data freshness. Mục tiêu là làm rõ rằng sensor đúng loại nhưng sai ngữ nghĩa (semantics / 의미론) hoặc quá cũ vẫn dẫn tới quyết định (decision / 결정) sai.

Sự cố (incident / 인시던트)/DR được bổ sung khôi phục (recovery / 복구) exit criteria, backlog/replay điều khiển (control / 제어), business-data integrity kiểm tra hợp lệ (validation / 검증), immutable/cyber-recovery ranh giới (boundary / 경계), quyết định (decision / 결정) log, degraded-mode exit giao thức (protocol / 프로토콜), idempotent/resumable khôi phục (recovery / 복구) workflow và human/control-plane đường dẫn (path / 경로) trong game day. khôi phục (recovery / 복구) được coi là một chuyển tiếp trạng thái (state transition / 상태 전이) phải **converge về steady trạng thái (state / 상태)**, không phải thời điểm dashboard đổi từ đỏ sang xanh.

Ở thời điểm kết thúc vòng này, `90_connections` có 12 lập luận (reasoning / 추론) tuyến (route / 경로) và nối ba lớp mới thành chuỗi `constraint → feedback`, `sensor → decision`, và `mitigation → recovery convergence`.

> **Chuyển mạch:** Ở chặng này của **Coverage kiểm tra (audit / 감사) — DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)**, **17. luồng (flow / 흐름), sensor và recovery-convergence độ sâu (depth / 깊이) pass** nêu điều cần giải thích; **18. đo lường (measurement / 측정), authority-lifecycle và platform-recovery độ sâu (depth / 깊이) pass** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. Dependency-resilience, stateful-delivery và control-plane-survivability độ sâu (depth / 깊이) pass** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. đo lường (measurement / 측정), authority-lifecycle và platform-recovery độ sâu (depth / 깊이) pass

Vòng tiếp theo vẫn giữ nguyên toàn bộ tệp chuẩn gốc (canonical file / 정본 파일) set và chỉ mở rộng nơi còn gap thực sự.

SRE được bổ sung ngữ nghĩa (semantics / 의미론) cho low-traffic dịch vụ (service / 서비스), tính đúng đắn (correctness / 정확성) của valid-event denominator, rolling/calendar/bản phát hành (release / 릴리스) cửa sổ (window / 윈도우), asynchronous-work SLI, composite journey có fallback/conditional đường dẫn (path / 경로), sự đánh đổi (trade-off / 트레이드오프) availability-latency-correctness và versioning/kiểm tra (audit / 감사) của chính SLO đo lường (measurement / 측정) chuỗi xử lý (pipeline / 파이프라인). Mục tiêu là ngăn lỗi (error / 오류) ngân sách (budget / 예산) điều khiển kỹ thuật (engineering / 엔지니어링) bằng một sensor sai population hoặc sai revision.

Bảo mật (security / 보안) được bổ sung rotation completion dựa trên bên tiêu thụ (consumer / 소비자) bằng chứng (evidence / 증거), break-glass như privileged-session vòng đời (lifecycle / 생명주기), chính sách (policy / 정책) kiểm tra (audit / 감사)→enforce di chuyển (migration / 마이그레이션), fail-open/fail-closed đặc tả hợp đồng (contract / 계약), offboarding/stale-principal reconciliation, least-privilege rà soát (review / 검토) có rare-path ngữ cảnh (context / 맥락) và integrity/retention ranh giới (boundary / 경계) cho privileged kiểm tra (audit / 감사) bằng chứng (evidence / 증거).

Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) được bổ sung cancellation ngữ nghĩa (semantics / 의미론) cho long-running thao tác (operation / 연산), distinction giữa compensation và quay lui (rollback / 롤백), orphan/adoption vòng đời (lifecycle / 생명주기), bootstrap khôi phục (recovery / 복구) cho chính nền tảng (platform / 플랫폼) điều khiển (control / 제어) plane, telemetry cho deprecation/di chuyển (migration / 마이그레이션) trạng thái (state / 상태), global-metadata-vs-local-execution trong cell kiến trúc (architecture / 아키텍처) và supportability/failure-path diagnosability như một phần nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약).

Môi trường vận hành (production / 운영 환경) Practice được bổ sung nhân quả (causal / 인과적) đồ thị (graph / 그래프), intervention/counterfactual ngữ nghĩa (semantics / 의미론), sự cố (incident / 인시던트) state-mutation serialization, detector-coverage map, fault-injection điều khiển (control / 제어)/xác minh (verification / 확인) và worked example cho trường hợp restart phục hồi nhưng không xác định nguyên nhân gốc (root cause / 근본 원인).

`90_connections` ở thời điểm đó có 16 lập luận (reasoning / 추론) tuyến (route / 경로), nối trực tiếp `user contract → SLO measurement correctness`, `platform intent → cancel/compensate/adopt/bootstrap`, `security change → staged authority migration`, và `symptom → causal confidence`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Coverage kiểm tra (audit / 감사) — DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)**, **18. đo lường (measurement / 측정), authority-lifecycle và platform-recovery độ sâu (depth / 깊이) pass** nêu điều cần giải thích; **19. Dependency-resilience, stateful-delivery và control-plane-survivability độ sâu (depth / 깊이) pass** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. Kết luận kiểm tra (audit / 감사) hiện tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Dependency-resilience, stateful-delivery và control-plane-survivability độ sâu (depth / 깊이) pass

Vòng hiện tại tiếp tục không tạo tệp (file / 파일)/chapter mới. mạng (network / 네트워크) được bổ sung circuit breaker như phụ thuộc (dependency / 의존성) admission điều khiển (control / 제어), bulkhead theo miền lỗi (failure domain / 장애 도메인), hedged yêu cầu (request / 요청) với tải (load / 로드)/duplicate-work sự đánh đổi (trade-off / 트레이드오프) và draining bao phủ cả routing lẫn liên kết (connection / 연결) trạng thái (state / 상태).

CI/CD được đào sâu ở phần stateful bản phát hành (release / 릴리스): online lược đồ (schema / 스키마) thay đổi (change / 변경) phải xét khóa (lock / 잠금)/rewrite/replication chi phí (cost / 비용); backfill là tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경) có throttle/checkpoint/resume; dual-write cần source-of-truth, discrepancy detector và reconciliation; đặc tả hợp đồng (contract / 계약) removal phải chờ bên tiêu thụ (consumer / 소비자) adoption/replay cửa sổ (window / 윈도우) thay vì producer deploy success.

Khả năng quan sát (observability / 관측 가능성) được bổ sung telemetry priority khi overload, truy vấn (query / 쿼리)/ingestion noisy-neighbor, retention theo investigation/compliance need, chi phí (cost / 비용) attribution theo nhân quả (causal / 인과적) tín hiệu (signal / 신호) driver và thất bại (failure / 실패) chuỗi (chain / 사슬) nơi ứng dụng (application / 애플리케이션) fault làm khả năng quan sát (observability / 관측 가능성) backend chết trước ứng dụng (application / 애플리케이션).

Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) được bổ sung durability đặc tả hợp đồng (contract / 계약) giữa control-plane trạng thái (state / 상태) và bên ngoài (external / 외부) world, safe/read-only degraded chế độ (mode / 모드), priority/admission cho reconciliation công việc (work / 작업) và DR phụ thuộc (dependency / 의존성) thứ tự (ordering / 순서). Multi-tenancy được bổ sung reservation→borrowing→reclamation ngữ nghĩa (semantics / 의미론), preemption chính sách (policy / 정책), isolation-fragmentation economics và isolation của cả khôi phục (recovery / 복구)/operator đường dẫn (path / 경로).

`90_connections` hiện có 20 lập luận (reasoning / 추론) tuyến (route / 경로); bốn tuyến (route / 경로) mới nối `dependency latency → isolation/load amplification`, `schema change → migration convergence`, `telemetry amplification → observability survivability`, và `platform control-plane loss → safe recovery`.

> **Chuyển mạch:** **20. Kết luận audit hiện tại** gom resilience, stateful delivery và control-plane survivability thành trạng thái có bằng chứng, rồi ghi rõ ưu tiên cho vòng coverage kế tiếp.

## 20. Kết luận kiểm tra (audit / 감사) hiện tại

Thư viện (library / 라이브러리) hiện có đường lập luận (reasoning / 추론) liên tục:

```text
flow / ownership / constraint / feedback delay
→ runtime + request path + dependency isolation / resource pressure
→ source / artifact / stateful migration / evidence freshness
→ container runtime + effective inputs
→ infrastructure state transition + cloud capacity
→ Kubernetes workload/control loops + stateful ownership
→ GitOps desired/applied/serving state
→ telemetry semantics / observability survivability / SLO correctness / overload
→ incident mitigation / causal confidence / recovery convergence / DR correctness
→ identity / effective authority / rotation / policy lifecycle / supply-chain trust
→ platform contract / control-plane durability / safe recovery / tenancy / reclamation / economics
→ cross-layer causal production diagnosis
```

Coverage hiện đủ để đọc như một giáo trình DevOps/kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) tổng quát mà không biến thành danh mục (catalog / 카탈로그) sản phẩm. Các lần mở rộng tiếp theo nên tiếp tục xuất phát từ sự cố (incident / 인시던트)/thất bại (failure / 실패) lớp (class / 클래스), transition-state bất biến (invariant / 불변식), evidence-quality bài toán (problem / 문제) hoặc nền tảng (platform / 플랫폼) yêu cầu (requirement / 요구사항) thực tế, không từ xu hướng công nghệ.

> **Bàn giao:** Sau **20. Kết luận kiểm tra (audit / 감사) hiện tại**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
