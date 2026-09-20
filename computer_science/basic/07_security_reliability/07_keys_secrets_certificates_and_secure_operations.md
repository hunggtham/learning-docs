# Keys, secrets, certificates và secure operations

Cryptographic algorithm có thể đúng nhưng hệ thống vẫn bị compromise vì key bị log, secret nằm trong repository, certificate hết hạn hoặc quyền decrypt quá rộng. Security operations tập trung vào **lifecycle của trust material**: tạo, lưu, phân phối, sử dụng, rotate, revoke và audit.

## Secret khác configuration thường

Database password, API token, private key và encryption key có disclosure impact. Chúng cần access control, redaction và rotation strategy khác feature flags hoặc public endpoint URLs.

“Environment variable” chỉ là transport mechanism, không tự động là secret manager. Process environment có thể bị logs/debug dumps/child processes expose tùy platform.

## Key lifecycle

Cryptographic key nên có purpose rõ: signing, encryption, MAC, key-encryption-key... Reuse cùng key cho nhiều protocols/purposes có thể tạo cross-protocol risks.

Lifecycle gồm generation bằng CSPRNG, secure storage, limited use, rotation, archival nếu cần decrypt historical data, và destruction/revocation.

## Envelope encryption

Thay vì dùng master key encrypt mọi data trực tiếp, system có thể generate Data Encryption Key (DEK) cho data rồi encrypt DEK bằng Key Encryption Key (KEK) trong KMS/HSM.

Điều này giúp rotate KEK mà không re-encrypt toàn bộ dataset và giới hạn direct exposure của master keys.

## HSM và KMS

Hardware Security Module giữ key material trong hardware boundary và thực hiện crypto operations mà private key không rời module trong normal use. Cloud/on-prem Key Management Service cung cấp managed policy, rotation và audit abstractions, đôi khi backed bởi HSM.

Chúng giảm key-handling burden nhưng không sửa overly broad IAM permissions.

## Certificates và PKI operations

TLS certificate bind public key với identities theo CA trust chain. Operational failure thường là expiry, wrong hostname, incomplete chain hoặc private key leakage.

Automation như ACME giảm manual renewal risk. Certificate transparency logs giúp detect/monitor issued certificates.

Revocation mechanisms như CRL/OCSP có operational limitations; modern ecosystems dùng short-lived certs và browser/vendor mechanisms bổ sung.

## Secret rotation

Rotation an toàn thường cần overlap: deploy support cho new + old secret, switch producers/clients, verify, rồi revoke old.

Nếu rotate database password ngay lập tức mà connection pools vẫn giữ old credentials cho reconnect, outage có thể xảy ra.

Rotation là distributed state transition, không phải replace one string atomically.

## Break-glass access

Emergency access đôi khi cần quyền mạnh tạm thời. Secure design yêu cầu explicit approval/audit, short lifetime và post-incident review thay vì shared admin password vĩnh viễn.

Least privilege phải cân bằng recoverability; system không thể “an toàn” nếu sự cố khiến không ai có thể khôi phục hợp lệ.

## Logging và redaction

Logs thường vô tình biến thành secret store: Authorization headers, tokens, passwords trong query strings hoặc stack traces. Logging pipeline cần structured redaction và data classification.

Security telemetry phải đủ điều tra mà không tạo thêm disclosure surface.

## Common Misconceptions

**“Mã hóa secret trong repo là đủ nếu key nằm repo khác.”** Nếu deployment có thể access cả hai tự động, attacker compromise path tương tự có thể lấy cả hai.

**“Rotate càng thường càng an toàn.”** Rotation giảm exposure window nhưng quá phức tạp/manual có thể gây outages và humans tạo workarounds. Automation và revocation capability quan trọng hơn con số tùy ý.

**“Certificate public nên private key cũng chỉ là file config.”** Private key là trust anchor material; compromise cho phép impersonation/signing tùy use.

## Mental Model

> Crypto primitive bảo vệ bits; key management bảo vệ quyền sử dụng primitive. Hãy reasoning toàn lifecycle, không chỉ encryption call.

## Kết nối

Đọc [cryptography foundations](./01_cryptography_foundations.md), [identity/auth](./02_identity_authentication_and_authorization.md), [secure software lifecycle](./08_supply_chain_and_secure_software_lifecycle.md) và [deployment/operations](../09_software_engineering/03_delivery_configuration_and_operations.md).