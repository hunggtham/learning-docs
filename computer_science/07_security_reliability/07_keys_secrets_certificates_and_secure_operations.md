# Keys, secrets, certificates và secure operations

> **Mạch đọc:** Đặt **Keys, secrets, certificates và secure operations** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Secret khác cấu hình (configuration / 구성) thường** sang **Key vòng đời (lifecycle / 생명주기)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Cryptographic thuật toán (algorithm / 알고리즘) có thể đúng nhưng hệ thống vẫn bị compromise vì key bị log, secret nằm trong repository, certificate hết hạn hoặc quyền decrypt quá rộng. bảo mật (security / 보안) operations tập trung vào **vòng đời (lifecycle / 생명주기) của trust material**: tạo, lưu, phân phối, sử dụng, rotate, revoke và kiểm tra (audit / 감사).

## Secret khác cấu hình (configuration / 구성) thường

Cơ sở dữ liệu (database / 데이터베이스) password, API đơn vị từ (token / 토큰), private key và encryption key có disclosure impact. Chúng cần kiểm soát truy cập (access control / 접근 제어), redaction và rotation chiến lược (strategy / 전략) khác tính năng (feature / 기능) flags hoặc công khai (public / 공개) endpoint URLs.

“môi trường (environment / 환경) variable” chỉ là vận chuyển (transport / 전송) cơ chế (mechanism / 메커니즘), không tự động là secret manager. tiến trình (process / 프로세스) môi trường (environment / 환경) có thể bị logs/gỡ lỗi (debug / 디버그) dumps/child processes expose tùy nền tảng (platform / 플랫폼).


> **Chuyển mạch:** Từ **Secret khác cấu hình (configuration / 구성) thường**, ta sang **Key vòng đời (lifecycle / 생명주기)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Key vòng đời (lifecycle / 생명주기)

Cryptographic key nên có purpose rõ: signing, encryption, MAC, key-encryption-key... Reuse cùng key cho nhiều protocols/purposes có thể tạo cross-protocol risks.

Vòng đời (lifecycle / 생명주기) gồm generation bằng CSPRNG, secure lưu trữ (storage / 저장소), limited use, rotation, archival nếu cần decrypt historical dữ liệu (data / 데이터), và destruction/revocation.


> **Chuyển mạch:** Từ **Key vòng đời (lifecycle / 생명주기)**, ta sang **Envelope encryption** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Envelope encryption

Thay vì dùng master key encrypt mọi dữ liệu (data / 데이터) trực tiếp, hệ thống (system / 시스템) có thể generate dữ liệu (data / 데이터) Encryption Key (DEK) cho dữ liệu (data / 데이터) rồi encrypt DEK bằng Key Encryption Key (KEK) trong KMS/HSM.

Điều này giúp rotate KEK mà không re-encrypt toàn bộ dataset và giới hạn direct exposure của master keys.


> **Chuyển mạch:** Từ **Envelope encryption**, ta sang **HSM và KMS** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## HSM và KMS

Hardware bảo mật (security / 보안) mô-đun (module / 모듈) giữ key material trong hardware ranh giới (boundary / 경계) và thực hiện crypto operations mà private key không rời mô-đun (module / 모듈) trong normal use. Cloud/on-prem Key Management dịch vụ (service / 서비스) cung cấp managed chính sách (policy / 정책), rotation và kiểm tra (audit / 감사) abstractions, đôi khi backed bởi HSM.

Chúng giảm key-handling burden nhưng không sửa overly broad IAM permissions.


> **Chuyển mạch:** Từ **HSM và KMS**, ta sang **Certificates và PKI operations** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Certificates và PKI operations

TLS certificate bind công khai (public / 공개) key với identities theo CA trust chuỗi (chain / 사슬). Operational thất bại (failure / 실패) thường là expiry, wrong hostname, incomplete chuỗi (chain / 사슬) hoặc private key leakage.

Automation như ACME giảm manual renewal rủi ro (risk / 위험). Certificate transparency logs giúp detect/monitor issued certificates.

Revocation mechanisms như CRL/OCSP có operational limitations; hiện đại (modern / 현대적) ecosystems dùng short-lived certs và trình duyệt (browser / 브라우저)/vendor mechanisms bổ sung.


> **Chuyển mạch:** Từ **Certificates và PKI operations**, ta sang **Secret rotation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Secret rotation

Rotation an toàn thường cần overlap: deploy hỗ trợ (support / 지원) cho new + old secret, switch producers/clients, verify, rồi revoke old.

Nếu rotate cơ sở dữ liệu (database / 데이터베이스) password ngay lập tức mà liên kết (connection / 연결) pools vẫn giữ old credentials cho reconnect, outage có thể xảy ra.

Rotation là phân tán (distributed / 분산) chuyển tiếp trạng thái (state transition / 상태 전이), không phải replace one string atomically.


> **Chuyển mạch:** Từ **Secret rotation**, ta sang **Break-glass truy cập (access / 접근)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Break-glass truy cập (access / 접근)

Emergency truy cập (access / 접근) đôi khi cần quyền mạnh tạm thời. Secure thiết kế (design / 설계) yêu cầu tường minh (explicit / 명시적) approval/kiểm tra (audit / 감사), short thời gian tồn tại (lifetime / 수명) và post-incident rà soát (review / 검토) thay vì dùng chung (shared / 공유) admin password vĩnh viễn.

Least privilege phải cân bằng recoverability; hệ thống (system / 시스템) không thể “an toàn” nếu sự cố khiến không ai có thể khôi phục hợp lệ.


> **Chuyển mạch:** Từ **Break-glass truy cập (access / 접근)**, ta sang **Logging và redaction** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Logging và redaction

Logs thường vô tình biến thành secret store: Authorization headers, tokens, passwords trong truy vấn (query / 쿼리) strings hoặc ngăn xếp (stack / 스택) traces. Logging chuỗi xử lý (pipeline / 파이프라인) cần structured redaction và dữ liệu (data / 데이터) classification.

Bảo mật (security / 보안) telemetry phải đủ điều tra mà không tạo thêm disclosure surface.


> **Chuyển mạch:** Từ **Logging và redaction**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Mã hóa secret trong repo là đủ nếu key nằm repo khác.”** Nếu triển khai (deployment / 배포) có thể truy cập (access / 접근) cả hai tự động, attacker compromise đường dẫn (path / 경로) tương tự có thể lấy cả hai.

**“Rotate càng thường càng an toàn.”** Rotation giảm exposure cửa sổ (window / 윈도우) nhưng quá phức tạp/manual có thể gây outages và humans tạo workarounds. Automation và revocation năng lực (capability / 역량) quan trọng hơn con số tùy ý.

**“Certificate công khai (public / 공개) nên private key cũng chỉ là tệp (file / 파일) cấu hình (config / 설정).”** Private key là trust anchor material; compromise cho phép impersonation/signing tùy use.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Crypto thành phần nguyên thủy (primitive / 기본 요소) bảo vệ bits; key management bảo vệ quyền sử dụng thành phần nguyên thủy (primitive / 기본 요소). Hãy lập luận (reasoning / 추론) toàn vòng đời (lifecycle / 생명주기), không chỉ encryption lời gọi (call / 호출).


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc [cryptography foundations](./01_cryptography_foundations.md), [identity/auth](./02_identity_authentication_and_authorization.md), [secure software lifecycle](./08_supply_chain_and_secure_software_lifecycle.md) và [deployment/operations](../09_software_engineering/03_delivery_configuration_and_operations.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 threat models and security principles](./00_threat_models_and_security_principles.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
