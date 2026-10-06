# Software supply chuỗi (chain / 사슬) và secure software vòng đời (lifecycle / 생명주기)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Software supply chain và secure software lifecycle**. Route đi từ trust graph/dependencies → SBOM/provenance → CI/CD permissions → secure development/testing → vulnerability management và incident feedback, để build artifact được truy nguyên tới nguồn và quyền.

Hiện đại (modern / 현대적) ứng dụng (application / 애플리케이션) hiếm khi chỉ chứa mã (code / 코드) nhóm (team / 팀) tự viết. Nó phụ thuộc gói (package / 패키지) registries, bản dựng (build / 빌드) tools, bộ chứa (container / 컨테이너) images, CI runners, triển khai (deployment / 배포) credentials và transitive dependencies. Vì vậy attack surface kéo dài từ nguồn (source / 소스) lần ghi nhận (commit / 커밋) đến sản phẩm tạo ra (artifact / 산출물) chạy môi trường vận hành (production / 운영 환경).

## Supply chuỗi (chain / 사슬) là đồ thị (graph / 그래프) trust

Một phụ thuộc (dependency / 의존성) gói (package / 패키지) phụ thuộc tiếp nhiều packages khác. bản dựng (build / 빌드) công cụ (tool / 도구) tải plugins. CI workflow chạy third-party actions. cơ sở (base / 기반) ảnh (image / 이미지) chứa OS packages. Mỗi nút (node / 노드)/edge là một trust quyết định (decision / 결정).

“mã (code / 코드) của chúng ta an toàn” không đủ nếu attacker compromise phụ thuộc (dependency / 의존성) publisher hoặc bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인).

> **Nối mạch:** Supply chain là trust graph; dependency risk đi theo node và provenance, còn SBOM làm inventory để triage lỗ hổng và kiểm soát vòng đời phát hành.

## Phụ thuộc (dependency / 의존성) risks

Typosquatting đặt gói (package / 패키지) tên gần gói (package / 패키지) phổ biến; phụ thuộc (dependency / 의존성) confusion lợi dụng resolver chọn gói (package / 패키지) công khai (public / 공개)/nội bộ (internal / 내부) sai; compromised maintainer có thể phát hành malicious phiên bản (version / 버전).

Defense gồm lockfiles, private registry chính sách (policy / 정책), provenance xác minh (verification / 확인), rà soát (review / 검토) phụ thuộc (dependency / 의존성) changes và giảm unnecessary dependencies.

Phiên bản (version / 버전) pinning tăng reproducibility nhưng pin mãi một vulnerable phiên bản (version / 버전) cũng nguy hiểm. cập nhật (update / 업데이트) chiến lược (strategy / 전략) phải cân bằng reproducibility với patching.

> **Nối mạch:** **SBOM** nối từ **Phụ thuộc (dependency / 의존성) risks** sang **Bản dựng (build / 빌드) provenance và sản phẩm tạo ra (artifact / 산출물) integrity**, vì cơ chế trước tạo đầu vào cho bước sau.

## SBOM

Software Bill of Materials (SBOM) liệt kê components/versions trong sản phẩm tạo ra (artifact / 산출물). Nó giúp trả lời nhanh “chúng ta có dùng vulnerable thư viện (library / 라이브러리) X không?”.

SBOM không tự làm software secure; inventory chỉ là prerequisite cho vulnerability management.

> **Nối mạch:** **Bản dựng (build / 빌드) provenance và sản phẩm tạo ra (artifact / 산출물) integrity** nối từ **SBOM** sang **CI/CD permissions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bản dựng (build / 빌드) provenance và sản phẩm tạo ra (artifact / 산출물) integrity

Secure chuỗi xử lý (pipeline / 파이프라인) cần biết sản phẩm tạo ra (artifact / 산출물) môi trường vận hành (production / 운영 환경) được bản dựng (build / 빌드) từ nguồn (source / 소스)/lần ghi nhận (commit / 커밋) nào, bởi workflow nào, với inputs nào và có bị tamper không.

Signing/provenance frameworks giúp verify sản phẩm tạo ra (artifact / 산출물) origin. Reproducible builds đi xa hơn: cùng nguồn (source / 소스)+môi trường (environment / 환경) spec tạo identical đầu ra (output / 출력), tăng khả năng detect bản dựng (build / 빌드) tampering.

> **Nối mạch:** **CI/CD permissions** nối từ **Bản dựng (build / 빌드) provenance và sản phẩm tạo ra (artifact / 산출물) integrity** sang **Secure Development vòng đời (lifecycle / 생명주기)**, vì cơ chế trước tạo đầu vào cho bước sau.

## CI/CD permissions

CI đơn vị từ (token / 토큰) thường có quyền đọc nguồn (source / 소스), publish gói (package / 패키지) hoặc deploy. Workflow pull yêu cầu (request / 요청) không đáng tin chạy với privileged secrets có thể trở thành remote mã (code / 코드) thực thi (execution / 실행) trên chuỗi xử lý (pipeline / 파이프라인).

Principle là least privilege per job, isolate untrusted mã (code / 코드), short-lived credentials và protected triển khai (deployment / 배포) environments.

> **Nối mạch:** **CI/CD permissions** đặt đầu vào cho **Secure Development vòng đời (lifecycle / 생명주기)**, rồi **SAST, DAST, SCA và fuzzing** mở rộng hệ quả.

## Secure Development vòng đời (lifecycle / 생명주기)

Bảo mật (security / 보안) cần xuất hiện từ requirements/threat modeling, thiết kế (design / 설계) rà soát (review / 검토), coding, testing, phụ thuộc (dependency / 의존성) scanning, bản phát hành (release / 릴리스), monitoring đến sự cố (incident / 인시던트) phản hồi (response / 응답).

Shift-left không có nghĩa đẩy toàn trách nhiệm cho nhà phát triển (developer / 개발자). Một số controls tốt nhất là nền tảng (platform / 플랫폼) guardrails, secure defaults và centralized tooling.

> **Nối mạch:** **Secure Development vòng đời (lifecycle / 생명주기)** đặt đầu vào cho **SAST, DAST, SCA và fuzzing**, rồi **Vulnerability management** mở rộng hệ quả.

## SAST, DAST, SCA và fuzzing

Static ứng dụng (application / 애플리케이션) bảo mật (security / 보안) Testing phân tích mã (code / 코드)/IR; động (dynamic / 동적) Testing chạy hệ thống (system / 시스템); Software Composition phân tích (analysis / 분석) kiểm dependencies; fuzzing tạo inputs để tìm crashes/edge cases.

Mỗi technique có blind spots. Scanner findings cần triage theo reachability/ngữ cảnh (context / 맥락) thay vì chỉ count CVEs.

> **Nối mạch:** **Vulnerability management** nối từ **SAST, DAST, SCA và fuzzing** sang **Sự cố (incident / 인시던트) phản hồi (response / 응답) vòng phản hồi (feedback loop / 피드백 루프)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vulnerability management

Severity score như CVSS mô tả generic technical severity, nhưng organizational rủi ro (risk / 위험) còn phụ thuộc exposure, exploitability, asset giá trị (value / 값) và compensating controls.

Prioritization cần ngữ cảnh (context / 맥락): một thư viện (library / 라이브러리) vulnerable đường dẫn (path / 경로) không reachable khác internet-facing auth bypass.

> **Nối mạch:** **Sự cố (incident / 인시던트) phản hồi (response / 응답) vòng phản hồi (feedback loop / 피드백 루프)** nối từ **Vulnerability management** sang **Dùng chung (common / 공통) Misconceptions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sự cố (incident / 인시던트) phản hồi (response / 응답) vòng phản hồi (feedback loop / 피드백 루프)

Sau sự cố (incident / 인시던트), mục tiêu không chỉ patch symptom mà cập nhật threat mô hình (model / 모델), detections, runbooks và preventive controls. Blameless phân tích (analysis / 분석) không có nghĩa không có accountability; nó nhằm hiểu hệ thống (system / 시스템) conditions thay vì dừng ở “human lỗi (error / 오류)”.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **Sự cố (incident / 인시던트) phản hồi (response / 응답) vòng phản hồi (feedback loop / 피드백 루프)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“Không có CVE nghĩa là phụ thuộc (dependency / 의존성) an toàn.”** Unknown vulnerabilities và malicious hành vi (behavior / 동작) vẫn có thể tồn tại.

**“Scanner càng nhiều alerts càng tốt.”** Noise làm triage tệ; tín hiệu (signal / 신호)/actionability quan trọng.

**“CI là nội bộ (internal / 내부) nên trusted.”** CI xử lý untrusted commits/dependencies và có credentials mạnh; nó là high-value mục tiêu (target / 대상).

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Software sản phẩm tạo ra (artifact / 산출물) là kết quả của một chuỗi (chain / 사슬) of custody. bảo mật (security / 보안) phải chứng minh/kiểm soát từng bước từ nguồn (source / 소스) định danh (identity / 식별자) tới bản dựng (build / 빌드), phụ thuộc (dependency / 의존성), signing và triển khai (deployment / 배포).

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Đọc [version control/build/packages](../08_software_systems/01_version_control_build_link_and_packages.md), [keys/secrets](./07_keys_secrets_certificates_and_secure_operations.md), [testing/debugging](./04_testing_verification_and_debugging.md) và [software engineering lifecycle](../09_software_engineering/00_requirements_specification_and_engineering_process.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
