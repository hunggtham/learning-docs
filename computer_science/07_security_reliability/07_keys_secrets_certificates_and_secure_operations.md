# Keys, secrets, certificates và secure operations

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Keys, secrets, certificates và secure operations**. Route đi từ secret/config boundary → key lifecycle/envelope encryption → HSM/KMS → certificates/PKI → rotation/break-glass/log redaction, để credential control có cả cơ chế lẫn audit trail.

Cryptographic thuật toán (algorithm / 알고리즘) có thể đúng nhưng hệ thống vẫn bị compromise vì key bị log, secret nằm trong repository, certificate hết hạn hoặc quyền decrypt quá rộng. bảo mật (security / 보안) operations tập trung vào **vòng đời (lifecycle / 생명주기) của trust material**: tạo, lưu, phân phối, sử dụng, rotate, revoke và kiểm tra (audit / 감사).

## Secret khác cấu hình (configuration / 구성) thường

Cơ sở dữ liệu (database / 데이터베이스) password, API đơn vị từ (token / 토큰), private key và encryption key có disclosure impact. Chúng cần kiểm soát truy cập (access control / 접근 제어), redaction và rotation chiến lược (strategy / 전략) khác tính năng (feature / 기능) flags hoặc công khai (public / 공개) endpoint URLs.

“môi trường (environment / 환경) variable” chỉ là vận chuyển (transport / 전송) cơ chế (mechanism / 메커니즘), không tự động là secret manager. tiến trình (process / 프로세스) môi trường (environment / 환경) có thể bị logs/gỡ lỗi (debug / 디버그) dumps/child processes expose tùy nền tảng (platform / 플랫폼).

> **Nối mạch:** Secret có giá trị bảo mật khác config thường; key lifecycle bao gồm tạo, phân phối, rotation và thu hồi, còn envelope encryption tách data key khỏi key mã hóa chủ.

## Key vòng đời (lifecycle / 생명주기)

Cryptographic key nên có purpose rõ: signing, encryption, MAC, key-encryption-key... Reuse cùng key cho nhiều protocols/purposes có thể tạo cross-protocol risks.

Vòng đời (lifecycle / 생명주기) gồm generation bằng CSPRNG, secure lưu trữ (storage / 저장소), limited use, rotation, archival nếu cần decrypt historical dữ liệu (data / 데이터), và destruction/revocation.

> **Nối mạch:** **Key vòng đời (lifecycle / 생명주기)** đặt đầu vào cho **Envelope encryption**, rồi **HSM và KMS** mở rộng hệ quả.

## Envelope encryption

Thay vì dùng master key encrypt mọi dữ liệu (data / 데이터) trực tiếp, hệ thống (system / 시스템) có thể generate dữ liệu (data / 데이터) Encryption Key (DEK) cho dữ liệu (data / 데이터) rồi encrypt DEK bằng Key Encryption Key (KEK) trong KMS/HSM.

Điều này giúp rotate KEK mà không re-encrypt toàn bộ dataset và giới hạn direct exposure của master keys.

> **Nối mạch:** **HSM và KMS** nối từ **Envelope encryption** sang **Certificates và PKI operations**, vì cơ chế trước tạo đầu vào cho bước sau.

## HSM và KMS

Hardware bảo mật (security / 보안) mô-đun (module / 모듈) giữ key material trong hardware ranh giới (boundary / 경계) và thực hiện crypto operations mà private key không rời mô-đun (module / 모듈) trong normal use. Cloud/on-prem Key Management dịch vụ (service / 서비스) cung cấp managed chính sách (policy / 정책), rotation và kiểm tra (audit / 감사) abstractions, đôi khi backed bởi HSM.

Chúng giảm key-handling burden nhưng không sửa overly broad IAM permissions.

> **Nối mạch:** **Certificates và PKI operations** nối từ **HSM và KMS** sang **Secret rotation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Certificates và PKI operations

TLS certificate bind công khai (public / 공개) key với identities theo CA trust chuỗi (chain / 사슬). Operational thất bại (failure / 실패) thường là expiry, wrong hostname, incomplete chuỗi (chain / 사슬) hoặc private key leakage.

Automation như ACME giảm manual renewal rủi ro (risk / 위험). Certificate transparency logs giúp detect/monitor issued certificates.

Revocation mechanisms như CRL/OCSP có operational limitations; hiện đại (modern / 현대적) ecosystems dùng short-lived certs và trình duyệt (browser / 브라우저)/vendor mechanisms bổ sung.

> **Nối mạch:** **Secret rotation** nối từ **Certificates và PKI operations** sang **Break-glass truy cập (access / 접근)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Secret rotation

Rotation an toàn thường cần overlap: deploy hỗ trợ (support / 지원) cho new + old secret, switch producers/clients, verify, rồi revoke old.

Nếu rotate cơ sở dữ liệu (database / 데이터베이스) password ngay lập tức mà liên kết (connection / 연결) pools vẫn giữ old credentials cho reconnect, outage có thể xảy ra.

Rotation là phân tán (distributed / 분산) chuyển tiếp trạng thái (state transition / 상태 전이), không phải replace one string atomically.

> **Nối mạch:** **Break-glass truy cập (access / 접근)** nối từ **Secret rotation** sang **Logging và redaction**, vì cơ chế trước tạo đầu vào cho bước sau.

## Break-glass truy cập (access / 접근)

Emergency truy cập (access / 접근) đôi khi cần quyền mạnh tạm thời. Secure thiết kế (design / 설계) yêu cầu tường minh (explicit / 명시적) approval/kiểm tra (audit / 감사), short thời gian tồn tại (lifetime / 수명) và post-incident rà soát (review / 검토) thay vì dùng chung (shared / 공유) admin password vĩnh viễn.

Least privilege phải cân bằng recoverability; hệ thống (system / 시스템) không thể “an toàn” nếu sự cố khiến không ai có thể khôi phục hợp lệ.

> **Nối mạch:** **Logging và redaction** nối từ **Break-glass truy cập (access / 접근)** sang **Dùng chung (common / 공통) Misconceptions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Logging và redaction

Logs thường vô tình biến thành secret store: Authorization headers, tokens, passwords trong truy vấn (query / 쿼리) strings hoặc ngăn xếp (stack / 스택) traces. Logging chuỗi xử lý (pipeline / 파이프라인) cần structured redaction và dữ liệu (data / 데이터) classification.

Bảo mật (security / 보안) telemetry phải đủ điều tra mà không tạo thêm disclosure surface.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **Logging và redaction** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“Mã hóa secret trong repo là đủ nếu key nằm repo khác.”** Nếu triển khai (deployment / 배포) có thể truy cập (access / 접근) cả hai tự động, attacker compromise đường dẫn (path / 경로) tương tự có thể lấy cả hai.

**“Rotate càng thường càng an toàn.”** Rotation giảm exposure cửa sổ (window / 윈도우) nhưng quá phức tạp/manual có thể gây outages và humans tạo workarounds. Automation và revocation năng lực (capability / 역량) quan trọng hơn con số tùy ý.

**“Certificate công khai (public / 공개) nên private key cũng chỉ là tệp (file / 파일) cấu hình (config / 설정).”** Private key là trust anchor material; compromise cho phép impersonation/signing tùy use.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Crypto thành phần nguyên thủy (primitive / 기본 요소) bảo vệ bits; key management bảo vệ quyền sử dụng thành phần nguyên thủy (primitive / 기본 요소). Hãy lập luận (reasoning / 추론) toàn vòng đời (lifecycle / 생명주기), không chỉ encryption lời gọi (call / 호출).

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Đọc [cryptography foundations](./01_cryptography_foundations.md), [identity/auth](./02_identity_authentication_and_authorization.md), [secure software lifecycle](./08_supply_chain_and_secure_software_lifecycle.md) và [deployment/operations](../09_software_engineering/03_delivery_configuration_and_operations.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
