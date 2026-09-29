# PKI, certificate kiểm tra hợp lệ (validation / 검증), mTLS và dịch vụ (service / 서비스) định danh (identity / 식별자)

> **Mạch đọc:** Đặt **PKI, certificate kiểm tra hợp lệ (validation / 검증), mTLS và dịch vụ (service / 서비스) định danh (identity / 식별자)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Certificate là signed assertion, không phải “trust đối tượng (object / 객체)” tự thân** sang **2. kiểm tra hợp lệ (validation / 검증) không chỉ là kiểm tra chữ ký**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


TLS thường được tóm tắt là “mã hóa liên kết (connection / 연결)”, nhưng encryption chỉ hữu ích nếu endpoint biết mình đang nói chuyện với đúng peer và keys được cấp/thu hồi theo trust mô hình (model / 모델) đúng. **công khai (public / 공개) Key hạ tầng (infrastructure / 인프라)** giải quyết bài toán bind công khai (public / 공개) key với định danh (identity / 식별자) thông qua certificate, trust anchor, issuance chính sách (policy / 정책) và kiểm tra hợp lệ (validation / 검증) rules.

Ở mức advanced, bất biến (invariant / 불변식) cần giữ là: **mỗi secure channel chỉ được coi là authenticated khi peer định danh (identity / 식별자) đã được chứng minh theo trust chính sách (policy / 정책) hiện hành; định danh (identity / 식별자) đó sau đó chỉ được dùng trong phạm vi authorization phù hợp.**

## 1. Certificate là signed assertion, không phải “trust đối tượng (object / 객체)” tự thân

X.509 certificate chứa công khai (public / 공개) key, định danh (identity / 식별자)/các ràng buộc (constraints / 제약조건들) và chữ ký của issuer. Chữ ký không có nghĩa thực thể (entity / 엔터티) “an toàn” hay “được quyền làm mọi thứ”. Nó chỉ nói issuer xác nhận binding đó theo chính sách (policy / 정책) của issuer.

Trust vì thế là chuỗi (chain / 사슬):

```text
leaf certificate
→ intermediate CA
→ root/trust anchor
```

Kiểm tra hợp lệ (validation / 검증) đúng phải chứng minh chuỗi (chain / 사슬) hợp lệ **và** leaf certificate phù hợp với định danh (identity / 식별자)/ngữ cảnh (context / 맥락) đang yêu cầu.

## 2. kiểm tra hợp lệ (validation / 검증) không chỉ là kiểm tra chữ ký

Một máy khách (client / 클라이언트) thường cần kiểm tra:

```text
chain signatures
validity period
hostname/service identity
key usage / extended key usage
basic constraints/path constraints
algorithm/key policy
revocation/short-lived credential semantics tùy hệ thống
```

Certificate có chữ ký hợp lệ nhưng hostname không khớp vẫn không chứng minh đúng máy chủ (server / 서버) cần kết nối.

Dạng thất bại (failure mode / 실패 모드) classic là “disable xác minh (verification / 확인) để kiểm thử (test / 테스트)” rồi cấu hình (config / 설정) đó lọt môi trường vận hành (production / 운영 환경). Khi đó encryption vẫn tồn tại nhưng peer authentication bất biến (invariant / 불변식) đã bị phá.

## 3. DNS và certificate kiểm tra hợp lệ (validation / 검증) giải hai câu hỏi khác nhau

DNS trả lời “hostname này map tới endpoint nào?”. Certificate kiểm tra hợp lệ (validation / 검증) trả lời “endpoint đang nói chuyện có credential hợp lệ cho định danh (identity / 식별자) mình mong đợi không?”.

DNS bị redirect nhưng TLS hostname xác minh (verification / 확인) đúng có thể chặn impersonation nếu attacker không có certificate hợp lệ. Ngược lại, verify chuỗi (chain / 사슬) nhưng bỏ hostname check làm trust mô hình (model / 모델) yếu đi rất nhiều.

Đây là liên kết (connection / 연결) trực tiếp với [end-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

## 4. mTLS đưa authentication về cả hai phía

TLS máy chủ (server / 서버) authentication chứng minh máy chủ (server / 서버) với máy khách (client / 클라이언트). **Mutual TLS (mTLS / 상호 TLS)** yêu cầu máy khách (client / 클라이언트) cũng trình certificate, từ đó máy chủ (server / 서버) có cryptographic định danh (identity / 식별자) của caller.

Điểm quan trọng là mTLS không tự định nghĩa principal ngữ nghĩa (semantics / 의미론). Certificate subject/SAN/tải công việc (workload / 워크로드) định danh (identity / 식별자) phải được map vào định danh (identity / 식별자) mô hình (model / 모델) ổn định, rồi chính sách (policy / 정책) tầng (layer / 계층) mới quyết định quyền.

## 5. định danh (identity / 식별자) khác authorization

“Peer là dịch vụ (service / 서비스) A” không đồng nghĩa “dịch vụ (service / 서비스) A được đọc customer bảng (table / 테이블)”.

Authentication trả lời **ai**. Authorization trả lời **được làm gì trên tài nguyên (resource / 자원) nào trong ngữ cảnh (context / 맥락) nào**.

Một thiết kế (design / 설계) an toàn tránh nhét toàn bộ permission vào certificate nếu chính sách (policy / 정책) thay đổi thường xuyên. Certificate nên cung cấp định danh (identity / 식별자) đủ đáng tin; authorization tầng (layer / 계층) áp least privilege dựa trên định danh (identity / 식별자) đó.

## 6. Trust lĩnh vực (domain / 도메인) quyết định blast radius

Nếu mọi tải công việc (workload / 워크로드) trong toàn công ty tin cùng một gốc (root / 루트) CA và chính sách (policy / 정책) cho phép định danh (identity / 식별자) rộng, compromise issuance đường dẫn (path / 경로) hoặc private key có thể có blast radius lớn.

Chia trust lĩnh vực (domain / 도메인) theo môi trường (environment / 환경), region, tenant hoặc sensitivity có thể giảm phạm vi sự cố (incident / 인시던트), nhưng tăng operational độ phức tạp (complexity / 복잡도).

Đây là sự đánh đổi (trade-off / 트레이드오프) bảo mật (security / 보안)/độ tin cậy (reliability / 신뢰성) thực sự: trust đồ thị (graph / 그래프) càng rộng càng dễ vận hành, nhưng compromise phạm vi (scope / 범위) càng lớn.

## 7. Issuance đường dẫn (path / 경로) là một security-critical điều khiển (control / 제어) plane

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

Nếu attacker chiếm được issuance authority, TLS cryptography không cứu được trust mô hình (model / 모델). Vì vậy CA key, issuer chính sách (policy / 정책) và workload-attestation đường dẫn (path / 경로) thường quan trọng hơn leaf certificate tệp (file / 파일).

## 8. Short-lived certificate giảm exposure nhưng tạo availability phụ thuộc (dependency / 의존성)

Credential thời gian tồn tại (lifetime / 수명) ngắn giảm cửa sổ lạm dụng nếu key bị lộ và giảm phụ thuộc revocation phức tạp.

Đổi lại, renewal đường dẫn (path / 경로) phải rất đáng tin. Nếu issuer/điều khiển (control / 제어) plane ngừng hoạt động đủ lâu, certificates hết hạn và tải công việc (workload / 워크로드) có thể mất khả năng giao tiếp.

Bảo mật (security / 보안) điều khiển (control / 제어) vì thế là độ tin cậy (reliability / 신뢰성) phụ thuộc (dependency / 의존성). thiết kế (design / 설계) cần biết thất bại (fail / 실패) chế độ (mode / 모드):

```text
issuer down
→ existing cert còn sống bao lâu?
→ workload mới có start được không?
→ grace/rotation window bao nhiêu?
→ fail-closed hay degraded mode?
```

## 9. Revocation là phân tán (distributed / 분산) trạng thái (state / 상태) propagation

CRL/OCSP hoặc nội bộ (internal / 내부) deny/revocation danh sách (list / 목록) giúp vô hiệu certificate trước expiry, nhưng revocation trạng thái (state / 상태) phải propagate tới verifiers.

Nếu verifier bộ nhớ đệm (cache / 캐시) trạng thái (state / 상태) cũ hoặc không reach revocation dịch vụ (service / 서비스), chính sách (policy / 정책) phải quyết định fail-open/fail-closed. Đây là bảo mật (security / 보안)–availability sự đánh đổi (trade-off / 트레이드오프).

Short-lived credential thường giảm phụ thuộc (dependency / 의존성) vào online revocation nhưng không loại bỏ toàn bộ incident-containment need.

## 10. Rotation cần overlap và version-aware rollout

Certificate/key rotation là phân tán (distributed / 분산) di chuyển (migration / 마이그레이션). Old/new trust anchors hoặc intermediate CAs có thể cùng tồn tại trong overlap cửa sổ (window / 윈도우).

Safe rotation thường cần thứ tự như:

```text
publish trust mới
→ wait propagation
→ issue credential mới
→ migrate workloads
→ verify traffic
→ retire trust cũ
```

Đảo thứ tự có thể gây outage. Đây là cùng family với lược đồ (schema / 스키마)/giao thức (protocol / 프로토콜) tính tương thích (compatibility / 호환성): multiple versions coexist tạm thời.

## 11. dịch vụ (service / 서비스) mesh tự động hóa PKI nhưng không xóa trust thiết kế (design / 설계)

Dịch vụ (service / 서비스) mesh có thể cấp tải công việc (workload / 워크로드) định danh (identity / 식별자) và mTLS giữa proxies. Điều này giảm ứng dụng (application / 애플리케이션) boilerplate nhưng di chuyển độ phức tạp (complexity / 복잡도) vào điều khiển (control / 제어) plane.

Cần vẫn trả lời:

```text
CA/trust root nào được tin?
workload nào được cấp identity nào?
namespace/tenant isolation ra sao?
policy được phân phối thế nào?
control-plane compromise có blast radius gì?
```

Automation không loại bỏ trust ranh giới (boundary / 경계); nó làm trust ranh giới (boundary / 경계) tập trung hơn.

## 12. Certificate pinning giảm trust surface nhưng tăng khôi phục (recovery / 복구) rủi ro (risk / 위험)

Pinning yêu cầu key/certificate cụ thể hoặc trust subset hẹp hơn. Nó giảm một số CA-based impersonation rủi ro (risk / 위험) nhưng làm rotation và disaster khôi phục (recovery / 복구) khó hơn.

Pin sai hoặc mất backup đường dẫn (path / 경로) có thể tạo self-inflicted outage. Pinning chỉ hợp lý khi threat mô hình (model / 모델) biện minh cho operational chi phí (cost / 비용).

## 13. Clock là lower-layer phụ thuộc (dependency / 의존성) quan trọng

Certificate validity dựa trên thời gian (time / 시간). Clock skew hoặc NTP sự cố (incident / 인시던트) có thể làm credential hợp lệ bị reject hàng loạt hoặc làm diagnostics sai timeline.

Khi nhiều services đồng loạt báo `certificate not yet valid`/`expired`, nguyên nhân gốc (root cause / 근본 원인) có thể là thời gian (time / 시간) synchronization, không phải TLS hiện thực (implementation / 구현).

Đây là ví dụ lower lớp trừu tượng (abstraction / 추상화) quyết định hành vi (behavior / 동작) ở bảo mật (security / 보안) tầng (layer / 계층).

## 14. TLS termination làm định danh (identity / 식별자) ranh giới (boundary / 경계) thay đổi

Nếu TLS terminate ở CDN/reverse proxy/bộ cân bằng tải (load balancer / 로드 밸런서) rồi proxy nói plaintext hoặc một TLS liên kết (connection / 연결) khác tới backend, end-to-end định danh (identity / 식별자) đặc tả hợp đồng (contract / 계약) đã đổi.

Backend có thể xác thực proxy thay vì original máy khách (client / 클라이언트). Nếu cần original principal, proxy phải truyền định danh (identity / 식별자) assertion theo một đặc tả hợp đồng (contract / 계약) được bảo vệ và backend phải tin đúng ranh giới (boundary / 경계).

Header như `X-User` không tự đáng tin chỉ vì nằm trong HTTP yêu cầu (request / 요청). Trust phụ thuộc ai được phép set/forward header đó.

## 15. mTLS không thay thế application-level authorization

Một nội bộ (internal / 내부) mạng (network / 네트워크) có mTLS everywhere nhưng authorization chính sách (policy / 정책) “mọi authenticated dịch vụ (service / 서비스) đều truy cập được mọi API” vẫn có blast radius lớn.

mTLS giúp loại anonymous/unauthenticated peer và bảo vệ channel. Least privilege vẫn phải được thực thi ở dịch vụ (service / 서비스)/tài nguyên (resource / 자원) ranh giới (boundary / 경계).

## 16. sự cố (incident / 인시던트) containment cần cắt authority đường dẫn (path / 경로)

Khi credential bị nghi compromise, chỉ rotate leaf cert có thể chưa đủ nếu attacker vẫn giữ tải công việc (workload / 워크로드) định danh (identity / 식별자) cho phép xin cert mới.

Containment cần xác định gốc (root / 루트) authority bị compromise ở đâu:

```text
leaf private key?
workload identity/token?
issuer policy?
intermediate/root CA?
trust bundle distribution?
```

Hành động (action / 동작) phải cắt đúng mức (level / 수준): revoke leaf, disable tải công việc (workload / 워크로드) định danh (identity / 식별자), remove issuer grant, rotate CA hoặc isolate dịch vụ (service / 서비스) ranh giới (boundary / 경계) tùy trường hợp (case / 사례).

Đọc cùng [Debugging và incident containment xuyên layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

## 17. hiệu năng (performance / 성능) pressure và TLS

TLS handshake thêm CPU/mạng (network / 네트워크) công việc (work / 작업); certificate chuỗi (chain / 사슬) lớn, cold liên kết (connection / 연결) tỷ lệ (rate / 비율) cao hoặc không reuse liên kết (connection / 연결) có thể tăng độ trễ (latency / 지연 시간). mTLS còn yêu cầu máy khách (client / 클라이언트) authentication.

Nhưng tối ưu hóa (optimization / 최적화) không được phá định danh (identity / 식별자) bất biến (invariant / 불변식). liên kết (connection / 연결)/session reuse có thể giảm handshake chi phí (cost / 비용), nhưng credential/chính sách (policy / 정책) rotation cần biết khi existing sessions được revalidated hoặc expire.

Hiệu năng (performance / 성능) và revocation freshness có thể xung đột nếu session thời gian tồn tại (lifetime / 수명) quá dài.

## 18. bằng chứng vận hành (production evidence / 운영 증거)

Bằng chứng (evidence / 증거) nên đủ để reconstruct trust quyết định (decision / 결정) mà không log secret/private key:

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

Một generic `SSL error` không đủ để phân biệt chuỗi (chain / 사슬) thất bại (failure / 실패), hostname mismatch, expiry, unknown CA hay giao thức (protocol / 프로토콜) incompatibility.

## 19. Mô hình tư duy

> PKI là **một phân tán (distributed / 분산) định danh (identity / 식별자) hệ thống (system / 시스템)**. Certificate bind key với định danh (identity / 식별자); kiểm tra hợp lệ (validation / 검증) kiểm tra binding theo trust chính sách (policy / 정책); TLS bảo vệ channel; mTLS đưa định danh (identity / 식별자) tới cả hai phía; authorization vẫn là tầng (layer / 계층) riêng; issuance/rotation/revocation là control-plane trạng thái (state / 상태) transitions. bảo mật (security / 보안) bất biến (invariant / 불변식) chỉ mạnh bằng trust gốc (root / 루트), định danh (identity / 식별자) proofing và chính sách (policy / 정책) ở ranh giới (boundary / 경계) thấp nhất mà hệ thống dựa vào.

## Kết nối

Đọc cùng [Secret/KMS lifecycle](./06_secrets_kms_hsm_rotation_and_envelope_encryption.md), [OAuth/OIDC lifecycle](./03_oauth_oidc_token_lifecycle_and_federation_threats.md), [End-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) và [Incident containment path](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 security boundaries attack chains and exploitability](./00_security_boundaries_attack_chains_and_exploitability.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
