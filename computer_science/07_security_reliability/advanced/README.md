# Advanced Bảo mật (security / 보안) & Độ tin cậy (reliability / 신뢰성)

Phần này giữ Bảo mật (security / 보안) và Độ tin cậy (reliability / 신뢰성) trong cùng conceptual ranh giới (boundary / 경계) vì bảo mật (security / 보안) điều khiển (control / 제어) luôn tạo availability phụ thuộc (dependency / 의존성), còn độ tin cậy (reliability / 신뢰성) cơ chế (mechanism / 메커니즘) như thử lại (retry / 재시도), bộ nhớ đệm (cache / 캐시) hoặc failover có thể mở rộng attack surface và blast radius.

## Chuẩn gốc (canonical / 정본) chapters

1. [Security boundaries, attack chains và exploitability](./00_security_boundaries_attack_chains_and_exploitability.md)
2. [Applied cryptographic protocol composition, nonce và key misuse](./01_cryptographic_protocol_composition_nonce_and_key_misuse.md)
3. [PKI, certificate validation, mTLS và service identity](./02_pki_certificate_validation_mtls_and_service_identity.md)
4. [OAuth, OIDC, token lifecycle và federation threats](./03_oauth_oidc_token_lifecycle_and_federation_threats.md)
5. [Memory safety, mitigations và sandbox boundaries](./04_memory_safety_mitigations_and_sandbox_boundaries.md)
6. [Browser isolation, CSP, SameSite và cross-origin trust](./05_browser_isolation_csp_samesite_and_cross_origin_trust.md)
7. [Secret, KMS, HSM, rotation và envelope encryption](./06_secrets_kms_hsm_rotation_and_envelope_encryption.md)
8. [Detection engineering, forensics và incident evidence](./07_detection_engineering_forensics_and_incident_evidence.md)
9. [Software supply chain, provenance, signing và build trust](./08_software_supply_chain_provenance_signing_and_build_trust.md)

## Mô hình tư duy (mental models / 사고 모델들) cần đạt

Mỗi bảo mật (security / 보안) concept phải trả lời được:

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

Định danh (identity / 식별자) không đồng nghĩa authorization. TLS không đồng nghĩa least privilege. Encryption at rest không đồng nghĩa cơ sở dữ liệu (database / 데이터베이스) tiến trình (process / 프로세스) không thấy plaintext. KMS không loại bỏ trust mà chuyển trust sang tải công việc (workload / 워크로드) định danh (identity / 식별자), chính sách (policy / 정책) và key-use năng lực (capability / 역량).

Detection/forensics có chuẩn gốc (canonical / 정본) chapter riêng vì bằng chứng (evidence / 증거) trust, base-rate bài toán (problem / 문제), sự kiện (event / 이벤트) correlation, clock/provenance, tamper resistance, retention/privacy, containment và effective revocation tạo lập luận (reasoning / 추론) đường dẫn (path / 경로) độc lập với preventive controls.

Software supply chuỗi (chain / 사슬) bổ sung authority đồ thị (graph / 그래프) từ nguồn (source / 소스)/phụ thuộc (dependency / 의존성) → builder/workflow → sản phẩm tạo ra (artifact / 산출물) digest → provenance/signature → registry → triển khai (deployment / 배포) chính sách (policy / 정책) → thời gian chạy (runtime / 런타임). Digest chỉ cho content định danh (identity / 식별자); signature chỉ chứng minh cryptographic assertion của một authority; provenance mô tả bản dựng (build / 빌드) lịch sử (history / 이력); SBOM là inventory; chính sách (policy / 정책) mới biến bằng chứng (evidence / 증거) thành enforcement. Không điều khiển (control / 제어) nào tự đủ.

## Độ tin cậy (reliability / 신뢰성) được đọc như thất bại (failure / 실패) containment

Thử lại (retry / 재시도), hết thời gian chờ (timeout / 타임아웃), circuit breaker, bulkhead, backpressure, tải (load / 로드) shedding và lỗi (error / 오류) ngân sách (budget / 예산) không cần tách thành gốc (root / 루트) thư viện (library / 라이브러리) mới. Foundation nằm ở [`basic/07_security_reliability`](../../basic/07_security_reliability/) và môi trường vận hành (production / 운영 환경) hàng đợi (queue / 큐)/sức chứa (capacity / 용량) mechanisms nằm tại [`08_software_systems/advanced`](../../08_software_systems/advanced/README.md).

Supply-chain điều khiển (control / 제어) cũng có availability sự đánh đổi (trade-off / 트레이드오프): registry/signing/định danh (identity / 식별자) phụ thuộc (dependency / 의존성) có thể chặn triển khai (deployment / 배포) khi unavailable; exception đường dẫn (path / 경로) có thể trở thành bypass nếu thiết kế không rõ fail-open/fail-closed ngữ nghĩa (semantics / 의미론).

Cross-layer containment được nối tại [Debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md), [request path + retry overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) triển khai (deployment / 배포)/evolution chapters.

## Bằng chứng vận hành (production evidence / 운영 증거)

Bảo mật (security / 보안)/độ tin cậy (reliability / 신뢰성) bằng chứng (evidence / 증거) cần đủ để trả lời không chỉ “có lỗi không?” mà “principal nào, chính sách (policy / 정책) phiên bản (version / 버전) nào, credential nào, sản phẩm tạo ra (artifact / 산출물) digest nào, builder/workflow nào, ranh giới (boundary / 경계) nào, thử lại (retry / 재시도)/hàng đợi (queue / 큐) nào và miền lỗi (failure domain / 장애 도메인) nào liên quan?”.

Ưu tiên định danh (identity / 식별자) siêu dữ liệu (metadata / 메타데이터), certificate/đơn vị từ (token / 토큰) issuer-audience-subject, chính sách (policy / 정책) quyết định (decision / 결정), KMS key id/thao tác (operation / 연산), sản phẩm tạo ra (artifact / 산출물) digest/provenance, triển khai (deployment / 배포) cohort, dịch vụ (service / 서비스) ranh giới (boundary / 경계), hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도) attempt, SLO burn, hàng đợi (queue / 큐)/saturation, kiểm tra (audit / 감사) provenance và containment timeline. Không log raw secret/đơn vị từ (token / 토큰) chỉ để tăng khả năng quan sát (observability / 관측 가능성).

## Quy tắc mở rộng

Không thêm chapter riêng cho một sản phẩm (product / 제품), mesh, vault, SIEM, trình quản lý gói (package manager / 패키지 관리자) hay signing khung phần mềm (framework / 프레임워크). Chỉ mở rộng khi có mô hình tư duy (mental model / 사고 모델) mới về trust, authority, containment, correlated thất bại (failure / 실패) hoặc bằng chứng vận hành (production evidence / 운영 증거) mà chuẩn gốc (canonical / 정본) chapter hiện có chưa giải thích.