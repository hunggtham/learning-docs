# Software supply chuỗi (chain / 사슬) và secure software vòng đời (lifecycle / 생명주기)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Software supply chain và secure software lifecycle**. Route đi từ trust graph/dependencies → SBOM/provenance → CI/CD permissions → secure development/testing → vulnerability management và incident feedback, để build artifact được truy nguyên tới nguồn và quyền.

Hiện đại (modern / 현대적) ứng dụng (application / 애플리케이션) hiếm khi chỉ chứa mã (code / 코드) nhóm (team / 팀) tự viết. Nó phụ thuộc gói (package / 패키지) registries, bản dựng (build / 빌드) tools, bộ chứa (container / 컨테이너) images, CI runners, triển khai (deployment / 배포) credentials và transitive dependencies. Vì vậy attack surface kéo dài từ nguồn (source / 소스) lần ghi nhận (commit / 커밋) đến sản phẩm tạo ra (artifact / 산출물) chạy môi trường vận hành (production / 운영 환경).

## Supply chuỗi (chain / 사슬) là đồ thị (graph / 그래프) trust

Một phụ thuộc (dependency / 의존성) gói (package / 패키지) phụ thuộc tiếp nhiều packages khác. bản dựng (build / 빌드) công cụ (tool / 도구) tải plugins. CI workflow chạy third-party actions. cơ sở (base / 기반) ảnh (image / 이미지) chứa OS packages. Mỗi nút (node / 노드)/edge là một trust quyết định (decision / 결정).

“mã (code / 코드) của chúng ta an toàn” không đủ nếu attacker compromise phụ thuộc (dependency / 의존성) publisher hoặc bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인).

> **Chuyển mạch:** Supply chain là trust graph; dependency risk đi theo node và provenance, còn SBOM làm inventory để triage lỗ hổng và kiểm soát vòng đời phát hành.

## Phụ thuộc (dependency / 의존성) risks

Typosquatting đặt gói (package / 패키지) tên gần gói (package / 패키지) phổ biến; phụ thuộc (dependency / 의존성) confusion lợi dụng resolver chọn gói (package / 패키지) công khai (public / 공개)/nội bộ (internal / 내부) sai; compromised maintainer có thể phát hành malicious phiên bản (version / 버전).

Defense gồm lockfiles, private registry chính sách (policy / 정책), provenance xác minh (verification / 확인), rà soát (review / 검토) phụ thuộc (dependency / 의존성) changes và giảm unnecessary dependencies.

Phiên bản (version / 버전) pinning tăng reproducibility nhưng pin mãi một vulnerable phiên bản (version / 버전) cũng nguy hiểm. cập nhật (update / 업데이트) chiến lược (strategy / 전략) phải cân bằng reproducibility với patching.

> **Chuyển mạch:** Ở chặng này của **Software supply chuỗi (chain / 사슬) và secure software vòng đời (lifecycle / 생명주기)**, **SBOM** tiếp nhận điểm tựa từ **Phụ thuộc (dependency / 의존성) risks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bản dựng (build / 빌드) provenance và sản phẩm tạo ra (artifact / 산출물) integrity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SBOM

Software Bill of Materials (SBOM) liệt kê components/versions trong sản phẩm tạo ra (artifact / 산출물). Nó giúp trả lời nhanh “chúng ta có dùng vulnerable thư viện (library / 라이브러리) X không?”.

SBOM không tự làm software secure; inventory chỉ là prerequisite cho vulnerability management.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Software supply chuỗi (chain / 사슬) và secure software vòng đời (lifecycle / 생명주기)**, **Bản dựng (build / 빌드) provenance và sản phẩm tạo ra (artifact / 산출물) integrity** tiếp nhận điểm tựa từ **SBOM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CI/CD permissions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bản dựng (build / 빌드) provenance và sản phẩm tạo ra (artifact / 산출물) integrity

Secure chuỗi xử lý (pipeline / 파이프라인) cần biết sản phẩm tạo ra (artifact / 산출물) môi trường vận hành (production / 운영 환경) được bản dựng (build / 빌드) từ nguồn (source / 소스)/lần ghi nhận (commit / 커밋) nào, bởi workflow nào, với inputs nào và có bị tamper không.

Signing/provenance frameworks giúp verify sản phẩm tạo ra (artifact / 산출물) origin. Reproducible builds đi xa hơn: cùng nguồn (source / 소스)+môi trường (environment / 환경) spec tạo identical đầu ra (output / 출력), tăng khả năng detect bản dựng (build / 빌드) tampering.

> **Chuyển mạch:** Trong **Software supply chuỗi (chain / 사슬) và secure software vòng đời (lifecycle / 생명주기)**, **CI/CD permissions** tiếp nhận điểm tựa từ **Bản dựng (build / 빌드) provenance và sản phẩm tạo ra (artifact / 산출물) integrity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Secure Development vòng đời (lifecycle / 생명주기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CI/CD permissions

CI đơn vị từ (token / 토큰) thường có quyền đọc nguồn (source / 소스), publish gói (package / 패키지) hoặc deploy. Workflow pull yêu cầu (request / 요청) không đáng tin chạy với privileged secrets có thể trở thành remote mã (code / 코드) thực thi (execution / 실행) trên chuỗi xử lý (pipeline / 파이프라인).

Principle là least privilege per job, isolate untrusted mã (code / 코드), short-lived credentials và protected triển khai (deployment / 배포) environments.

> **Chuyển mạch:** Ở chặng này của **Software supply chuỗi (chain / 사슬) và secure software vòng đời (lifecycle / 생명주기)**, **CI/CD permissions** xác định đầu vào; **Secure Development vòng đời (lifecycle / 생명주기)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **SAST, DAST, SCA và fuzzing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Secure Development vòng đời (lifecycle / 생명주기)

Bảo mật (security / 보안) cần xuất hiện từ requirements/threat modeling, thiết kế (design / 설계) rà soát (review / 검토), coding, testing, phụ thuộc (dependency / 의존성) scanning, bản phát hành (release / 릴리스), monitoring đến sự cố (incident / 인시던트) phản hồi (response / 응답).

Shift-left không có nghĩa đẩy toàn trách nhiệm cho nhà phát triển (developer / 개발자). Một số controls tốt nhất là nền tảng (platform / 플랫폼) guardrails, secure defaults và centralized tooling.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Software supply chuỗi (chain / 사슬) và secure software vòng đời (lifecycle / 생명주기)**, **Secure Development vòng đời (lifecycle / 생명주기)** xác định đầu vào; **SAST, DAST, SCA và fuzzing** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Vulnerability management** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SAST, DAST, SCA và fuzzing

Static ứng dụng (application / 애플리케이션) bảo mật (security / 보안) Testing phân tích mã (code / 코드)/IR; động (dynamic / 동적) Testing chạy hệ thống (system / 시스템); Software Composition phân tích (analysis / 분석) kiểm dependencies; fuzzing tạo inputs để tìm crashes/edge cases.

Mỗi technique có blind spots. Scanner findings cần triage theo reachability/ngữ cảnh (context / 맥락) thay vì chỉ count CVEs.

> **Chuyển mạch:** Trong **Software supply chuỗi (chain / 사슬) và secure software vòng đời (lifecycle / 생명주기)**, **Vulnerability management** tiếp nhận điểm tựa từ **SAST, DAST, SCA và fuzzing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự cố (incident / 인시던트) phản hồi (response / 응답) vòng phản hồi (feedback loop / 피드백 루프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vulnerability management

Severity score như CVSS mô tả generic technical severity, nhưng organizational rủi ro (risk / 위험) còn phụ thuộc exposure, exploitability, asset giá trị (value / 값) và compensating controls.

Prioritization cần ngữ cảnh (context / 맥락): một thư viện (library / 라이브러리) vulnerable đường dẫn (path / 경로) không reachable khác internet-facing auth bypass.

> **Chuyển mạch:** Ở chặng này của **Software supply chuỗi (chain / 사슬) và secure software vòng đời (lifecycle / 생명주기)**, **Sự cố (incident / 인시던트) phản hồi (response / 응답) vòng phản hồi (feedback loop / 피드백 루프)** tiếp nhận điểm tựa từ **Vulnerability management** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự cố (incident / 인시던트) phản hồi (response / 응답) vòng phản hồi (feedback loop / 피드백 루프)

Sau sự cố (incident / 인시던트), mục tiêu không chỉ patch symptom mà cập nhật threat mô hình (model / 모델), detections, runbooks và preventive controls. Blameless phân tích (analysis / 분석) không có nghĩa không có accountability; nó nhằm hiểu hệ thống (system / 시스템) conditions thay vì dừng ở “human lỗi (error / 오류)”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Software supply chuỗi (chain / 사슬) và secure software vòng đời (lifecycle / 생명주기)**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Sự cố (incident / 인시던트) phản hồi (response / 응답) vòng phản hồi (feedback loop / 피드백 루프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Không có CVE nghĩa là phụ thuộc (dependency / 의존성) an toàn.”** Unknown vulnerabilities và malicious hành vi (behavior / 동작) vẫn có thể tồn tại.

**“Scanner càng nhiều alerts càng tốt.”** Noise làm triage tệ; tín hiệu (signal / 신호)/actionability quan trọng.

**“CI là nội bộ (internal / 내부) nên trusted.”** CI xử lý untrusted commits/dependencies và có credentials mạnh; nó là high-value mục tiêu (target / 대상).

> **Chuyển mạch:** Trong **Software supply chuỗi (chain / 사슬) và secure software vòng đời (lifecycle / 생명주기)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Software sản phẩm tạo ra (artifact / 산출물) là kết quả của một chuỗi (chain / 사슬) of custody. bảo mật (security / 보안) phải chứng minh/kiểm soát từng bước từ nguồn (source / 소스) định danh (identity / 식별자) tới bản dựng (build / 빌드), phụ thuộc (dependency / 의존성), signing và triển khai (deployment / 배포).

> **Chuyển mạch:** Ở chặng này của **Software supply chuỗi (chain / 사슬) và secure software vòng đời (lifecycle / 생명주기)**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [version control/build/packages](../08_software_systems/01_version_control_build_link_and_packages.md), [keys/secrets](./07_keys_secrets_certificates_and_secure_operations.md), [testing/debugging](./04_testing_verification_and_debugging.md) và [software engineering lifecycle](../09_software_engineering/00_requirements_specification_and_engineering_process.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
