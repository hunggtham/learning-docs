# Software supply chain và secure software lifecycle

Modern application hiếm khi chỉ chứa code team tự viết. Nó phụ thuộc package registries, build tools, container images, CI runners, deployment credentials và transitive dependencies. Vì vậy attack surface kéo dài từ source commit đến artifact chạy production.

## Supply chain là graph trust

Một dependency package phụ thuộc tiếp nhiều packages khác. Build tool tải plugins. CI workflow chạy third-party actions. Base image chứa OS packages. Mỗi node/edge là một trust decision.

“Code của chúng ta an toàn” không đủ nếu attacker compromise dependency publisher hoặc build pipeline.

## Dependency risks

Typosquatting đặt package tên gần package phổ biến; dependency confusion lợi dụng resolver chọn package public/internal sai; compromised maintainer có thể phát hành malicious version.

Defense gồm lockfiles, private registry policy, provenance verification, review dependency changes và giảm unnecessary dependencies.

Version pinning tăng reproducibility nhưng pin mãi một vulnerable version cũng nguy hiểm. Update strategy phải cân bằng reproducibility với patching.

## SBOM

Software Bill of Materials (SBOM) liệt kê components/versions trong artifact. Nó giúp trả lời nhanh “chúng ta có dùng vulnerable library X không?”.

SBOM không tự làm software secure; inventory chỉ là prerequisite cho vulnerability management.

## Build provenance và artifact integrity

Secure pipeline cần biết artifact production được build từ source/commit nào, bởi workflow nào, với inputs nào và có bị tamper không.

Signing/provenance frameworks giúp verify artifact origin. Reproducible builds đi xa hơn: cùng source+environment spec tạo identical output, tăng khả năng detect build tampering.

## CI/CD permissions

CI token thường có quyền đọc source, publish package hoặc deploy. Workflow pull request không đáng tin chạy với privileged secrets có thể trở thành remote code execution trên pipeline.

Principle là least privilege per job, isolate untrusted code, short-lived credentials và protected deployment environments.

## Secure Development Lifecycle

Security cần xuất hiện từ requirements/threat modeling, design review, coding, testing, dependency scanning, release, monitoring đến incident response.

Shift-left không có nghĩa đẩy toàn trách nhiệm cho developer. Một số controls tốt nhất là platform guardrails, secure defaults và centralized tooling.

## SAST, DAST, SCA và fuzzing

Static Application Security Testing phân tích code/IR; Dynamic Testing chạy system; Software Composition Analysis kiểm dependencies; fuzzing tạo inputs để tìm crashes/edge cases.

Mỗi technique có blind spots. Scanner findings cần triage theo reachability/context thay vì chỉ count CVEs.

## Vulnerability management

Severity score như CVSS mô tả generic technical severity, nhưng organizational risk còn phụ thuộc exposure, exploitability, asset value và compensating controls.

Prioritization cần context: một library vulnerable path không reachable khác internet-facing auth bypass.

## Incident response feedback loop

Sau incident, mục tiêu không chỉ patch symptom mà cập nhật threat model, detections, runbooks và preventive controls. Blameless analysis không có nghĩa không có accountability; nó nhằm hiểu system conditions thay vì dừng ở “human error”.

## Common Misconceptions

**“Không có CVE nghĩa là dependency an toàn.”** Unknown vulnerabilities và malicious behavior vẫn có thể tồn tại.

**“Scanner càng nhiều alerts càng tốt.”** Noise làm triage tệ; signal/actionability quan trọng.

**“CI là internal nên trusted.”** CI xử lý untrusted commits/dependencies và có credentials mạnh; nó là high-value target.

## Mental Model

> Software artifact là kết quả của một chain of custody. Security phải chứng minh/kiểm soát từng bước từ source identity tới build, dependency, signing và deployment.

## Kết nối

Đọc [version control/build/packages](../08_software_systems/01_version_control_build_link_and_packages.md), [keys/secrets](./07_keys_secrets_certificates_and_secure_operations.md), [testing/debugging](./04_testing_verification_and_debugging.md) và [software engineering lifecycle](../09_software_engineering/00_requirements_specification_and_engineering_process.md).