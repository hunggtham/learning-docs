# PKI, certificate validation, mTLS và service identity

TLS thường được tóm tắt là “mã hóa connection”, nhưng encryption chỉ hữu ích nếu endpoint biết mình đang nói chuyện với đúng peer và keys được cấp/thu hồi theo trust model đúng. **Public Key Infrastructure (PKI / 공개키 기반 구조)** giải quyết bài toán bind public key với identity thông qua certificate, trust anchor, issuance policy và validation rules.

Ở mức advanced, invariant cần giữ là: **mỗi secure channel chỉ được coi là authenticated khi peer identity đã được chứng minh theo trust policy hiện hành; identity đó sau đó chỉ được dùng trong phạm vi authorization phù hợp.**

## 1. Certificate là signed assertion, không phải “trust object” tự thân

X.509 certificate chứa public key, identity/constraints và chữ ký của issuer. Chữ ký không có nghĩa entity “an toàn” hay “được quyền làm mọi thứ”. Nó chỉ nói issuer xác nhận binding đó theo policy của issuer.

Trust vì thế là chain:

```text
leaf certificate
→ intermediate CA
→ root/trust anchor
```

Validation đúng phải chứng minh chain hợp lệ **và** leaf certificate phù hợp với identity/context đang yêu cầu.

## 2. Validation không chỉ là kiểm tra chữ ký

Một client thường cần kiểm tra:

```text
chain signatures
validity period
hostname/service identity
key usage / extended key usage
basic constraints/path constraints
algorithm/key policy
revocation/short-lived credential semantics tùy hệ thống
```

Certificate có chữ ký hợp lệ nhưng hostname không khớp vẫn không chứng minh đúng server cần kết nối.

Failure mode classic là “disable verification để test” rồi config đó lọt production. Khi đó encryption vẫn tồn tại nhưng peer authentication invariant đã bị phá.

## 3. DNS và certificate validation giải hai câu hỏi khác nhau

DNS trả lời “hostname này map tới endpoint nào?”. Certificate validation trả lời “endpoint đang nói chuyện có credential hợp lệ cho identity mình mong đợi không?”.

DNS bị redirect nhưng TLS hostname verification đúng có thể chặn impersonation nếu attacker không có certificate hợp lệ. Ngược lại, verify chain nhưng bỏ hostname check làm trust model yếu đi rất nhiều.

Đây là connection trực tiếp với [end-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

## 4. mTLS đưa authentication về cả hai phía

TLS server authentication chứng minh server với client. **Mutual TLS (mTLS / 상호 TLS)** yêu cầu client cũng trình certificate, từ đó server có cryptographic identity của caller.

Điểm quan trọng là mTLS không tự định nghĩa principal semantics. Certificate subject/SAN/workload identity phải được map vào identity model ổn định, rồi policy layer mới quyết định quyền.

## 5. Identity khác authorization

“Peer là service A” không đồng nghĩa “service A được đọc customer table”.

Authentication trả lời **ai**. Authorization trả lời **được làm gì trên resource nào trong context nào**.

Một design an toàn tránh nhét toàn bộ permission vào certificate nếu policy thay đổi thường xuyên. Certificate nên cung cấp identity đủ đáng tin; authorization layer áp least privilege dựa trên identity đó.

## 6. Trust domain quyết định blast radius

Nếu mọi workload trong toàn công ty tin cùng một root CA và policy cho phép identity rộng, compromise issuance path hoặc private key có thể có blast radius lớn.

Chia trust domain theo environment, region, tenant hoặc sensitivity có thể giảm phạm vi incident, nhưng tăng operational complexity.

Đây là trade-off security/reliability thực sự: trust graph càng rộng càng dễ vận hành, nhưng compromise scope càng lớn.

## 7. Issuance path là một security-critical control plane

PKI không chỉ là certificates trên disk. Nó gồm:

```text
identity proofing/workload attestation
→ certificate request
→ CA/issuer policy
→ signing key/HSM/KMS
→ certificate distribution
→ renewal/revocation
→ trust bundle distribution
```

Nếu attacker chiếm được issuance authority, TLS cryptography không cứu được trust model. Vì vậy CA key, issuer policy và workload-attestation path thường quan trọng hơn leaf certificate file.

## 8. Short-lived certificate giảm exposure nhưng tạo availability dependency

Credential lifetime ngắn giảm cửa sổ lạm dụng nếu key bị lộ và giảm phụ thuộc revocation phức tạp.

Đổi lại, renewal path phải rất đáng tin. Nếu issuer/control plane ngừng hoạt động đủ lâu, certificates hết hạn và workload có thể mất khả năng giao tiếp.

Security control vì thế là reliability dependency. Design cần biết fail mode:

```text
issuer down
→ existing cert còn sống bao lâu?
→ workload mới có start được không?
→ grace/rotation window bao nhiêu?
→ fail-closed hay degraded mode?
```

## 9. Revocation là distributed state propagation

CRL/OCSP hoặc internal deny/revocation list giúp vô hiệu certificate trước expiry, nhưng revocation state phải propagate tới verifiers.

Nếu verifier cache state cũ hoặc không reach revocation service, policy phải quyết định fail-open/fail-closed. Đây là security–availability trade-off.

Short-lived credential thường giảm dependency vào online revocation nhưng không loại bỏ toàn bộ incident-containment need.

## 10. Rotation cần overlap và version-aware rollout

Certificate/key rotation là distributed migration. Old/new trust anchors hoặc intermediate CAs có thể cùng tồn tại trong overlap window.

Safe rotation thường cần thứ tự như:

```text
publish trust mới
→ wait propagation
→ issue credential mới
→ migrate workloads
→ verify traffic
→ retire trust cũ
```

Đảo thứ tự có thể gây outage. Đây là cùng family với schema/protocol compatibility: multiple versions coexist tạm thời.

## 11. Service mesh tự động hóa PKI nhưng không xóa trust design

Service mesh có thể cấp workload identity và mTLS giữa proxies. Điều này giảm application boilerplate nhưng di chuyển complexity vào control plane.

Cần vẫn trả lời:

```text
CA/trust root nào được tin?
workload nào được cấp identity nào?
namespace/tenant isolation ra sao?
policy được phân phối thế nào?
control-plane compromise có blast radius gì?
```

Automation không loại bỏ trust boundary; nó làm trust boundary tập trung hơn.

## 12. Certificate pinning giảm trust surface nhưng tăng recovery risk

Pinning yêu cầu key/certificate cụ thể hoặc trust subset hẹp hơn. Nó giảm một số CA-based impersonation risk nhưng làm rotation và disaster recovery khó hơn.

Pin sai hoặc mất backup path có thể tạo self-inflicted outage. Pinning chỉ hợp lý khi threat model biện minh cho operational cost.

## 13. Clock là lower-layer dependency quan trọng

Certificate validity dựa trên time. Clock skew hoặc NTP incident có thể làm credential hợp lệ bị reject hàng loạt hoặc làm diagnostics sai timeline.

Khi nhiều services đồng loạt báo `certificate not yet valid`/`expired`, root cause có thể là time synchronization, không phải TLS implementation.

Đây là ví dụ lower abstraction quyết định behavior ở security layer.

## 14. TLS termination làm identity boundary thay đổi

Nếu TLS terminate ở CDN/reverse proxy/load balancer rồi proxy nói plaintext hoặc một TLS connection khác tới backend, end-to-end identity contract đã đổi.

Backend có thể xác thực proxy thay vì original client. Nếu cần original principal, proxy phải truyền identity assertion theo một contract được bảo vệ và backend phải tin đúng boundary.

Header như `X-User` không tự đáng tin chỉ vì nằm trong HTTP request. Trust phụ thuộc ai được phép set/forward header đó.

## 15. mTLS không thay thế application-level authorization

Một internal network có mTLS everywhere nhưng authorization policy “mọi authenticated service đều truy cập được mọi API” vẫn có blast radius lớn.

mTLS giúp loại anonymous/unauthenticated peer và bảo vệ channel. Least privilege vẫn phải được thực thi ở service/resource boundary.

## 16. Incident containment cần cắt authority path

Khi credential bị nghi compromise, chỉ rotate leaf cert có thể chưa đủ nếu attacker vẫn giữ workload identity cho phép xin cert mới.

Containment cần xác định root authority bị compromise ở đâu:

```text
leaf private key?
workload identity/token?
issuer policy?
intermediate/root CA?
trust bundle distribution?
```

Action phải cắt đúng level: revoke leaf, disable workload identity, remove issuer grant, rotate CA hoặc isolate service boundary tùy case.

Đọc cùng [Debugging và incident containment xuyên layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

## 17. Performance pressure và TLS

TLS handshake thêm CPU/network work; certificate chain lớn, cold connection rate cao hoặc không reuse connection có thể tăng latency. mTLS còn yêu cầu client authentication.

Nhưng optimization không được phá identity invariant. Connection/session reuse có thể giảm handshake cost, nhưng credential/policy rotation cần biết khi existing sessions được revalidated hoặc expire.

Performance và revocation freshness có thể xung đột nếu session lifetime quá dài.

## 18. Production evidence

Evidence nên đủ để reconstruct trust decision mà không log secret/private key:

```text
peer/server name mong đợi
certificate serial/fingerprint metadata
issuer/chain/trust-domain id
validity timestamps
TLS version/cipher nếu liên quan incident
mTLS principal/workload identity
policy decision/version
handshake error category
renewal/issuance/revocation event
clock/time-sync health
```

Một generic `SSL error` không đủ để phân biệt chain failure, hostname mismatch, expiry, unknown CA hay protocol incompatibility.

## 19. Mô hình tư duy

> PKI là **một distributed identity system**. Certificate bind key với identity; validation kiểm tra binding theo trust policy; TLS bảo vệ channel; mTLS đưa identity tới cả hai phía; authorization vẫn là layer riêng; issuance/rotation/revocation là control-plane state transitions. Security invariant chỉ mạnh bằng trust root, identity proofing và policy ở boundary thấp nhất mà hệ thống dựa vào.

## Kết nối

Đọc cùng [Secret/KMS lifecycle](./06_secrets_kms_hsm_rotation_and_envelope_encryption.md), [OAuth/OIDC lifecycle](./03_oauth_oidc_token_lifecycle_and_federation_threats.md), [End-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) và [Incident containment path](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).