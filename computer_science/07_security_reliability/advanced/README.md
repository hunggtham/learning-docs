# Advanced Security & Reliability

Phần này giữ Security và Reliability trong cùng conceptual boundary vì security control luôn tạo availability dependency, còn reliability mechanism như retry, cache hoặc failover có thể mở rộng attack surface và blast radius.

## Canonical chapters

1. [Security boundaries, attack chains và exploitability](./00_security_boundaries_attack_chains_and_exploitability.md)
2. [Applied cryptographic protocol composition, nonce và key misuse](./01_cryptographic_protocol_composition_nonce_and_key_misuse.md)
3. [PKI, certificate validation, mTLS và service identity](./02_pki_certificate_validation_mtls_and_service_identity.md)
4. [OAuth, OIDC, token lifecycle và federation threats](./03_oauth_oidc_token_lifecycle_and_federation_threats.md)
5. [Memory safety, mitigations và sandbox boundaries](./04_memory_safety_mitigations_and_sandbox_boundaries.md)
6. [Browser isolation, CSP, SameSite và cross-origin trust](./05_browser_isolation_csp_samesite_and_cross_origin_trust.md)
7. [Secret, KMS, HSM, rotation và envelope encryption](./06_secrets_kms_hsm_rotation_and_envelope_encryption.md)

## Mental models cần đạt

Mỗi security concept phải trả lời được:

```text
asset/invariant nào cần bảo vệ?
principal nào có authority gì?
trust boundary nằm ở đâu?
credential/capability được cấp, dùng, rotate, revoke thế nào?
control fail-open hay fail-closed khi dependency hỏng?
compromise lan theo path nào?
containment cắt path đó ở đâu?
evidence nào reconstruct được authority path?
```

Identity không đồng nghĩa authorization. TLS không đồng nghĩa least privilege. Encryption at rest không đồng nghĩa database process không thấy plaintext. KMS không loại bỏ trust mà chuyển trust sang workload identity, policy và key-use capability.

## Reliability được đọc như failure containment

Retry, timeout, circuit breaker, bulkhead, backpressure, load shedding và error budget không cần tách thành root library mới. Foundation nằm ở [`basic/07_security_reliability`](../../basic/07_security_reliability/) và production queue/capacity mechanisms nằm tại [`08_software_systems/advanced`](../../08_software_systems/advanced/README.md).

Cross-layer containment được nối tại [Debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md) và [request path + retry overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

## Production evidence

Security/reliability evidence cần đủ để trả lời không chỉ “có lỗi không?” mà “principal nào, policy version nào, credential nào, boundary nào, retry/queue nào và failure domain nào liên quan?”.

Ưu tiên identity metadata, certificate/token issuer-audience-subject, policy decision, KMS key id/operation, service boundary, timeout/retry attempt, SLO burn, queue/saturation và containment timeline. Không log raw secret/token chỉ để tăng observability.

## Quy tắc mở rộng

Không thêm chapter riêng cho một product, mesh, vault, SIEM hay framework. Chỉ mở rộng khi có mental model mới về trust, authority, containment, correlated failure hoặc production evidence mà canonical chapter hiện có chưa giải thích.