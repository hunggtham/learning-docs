# Secret, KMS, HSM, rotation và envelope encryption

> **Mạch đọc:** Đặt **Secret, KMS, HSM, rotation và envelope encryption** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Secret vòng đời (lifecycle / 생명주기)** sang **2. Không nên nhúng secret vào mã nguồn (source code / 소스 코드)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Bảo mật ứng dụng không dừng ở việc chọn thuật toán mã hóa đúng. Sau khi một hệ thống quyết định dùng khóa bí mật, câu hỏi thực tế trở thành: khóa được tạo ở đâu, ai được dùng, lưu ở đâu, xoay vòng thế nào, kiểm tra (audit / 감사) ra sao và chuyện gì xảy ra nếu một bản sao bị lộ.

**Secret** là dữ liệu cần được bảo vệ khỏi truy cập trái phép, ví dụ API key, cơ sở dữ liệu (database / 데이터베이스) password hoặc private key. **Khóa mật mã (cryptographic key)** là một loại secret có ngữ nghĩa (semantics / 의미론) đặc biệt vì nó trực tiếp quyết định khả năng mã hóa, giải mã, ký hoặc xác minh. Không nên coi mọi secret như chuỗi cấu hình bình thường.

## 1. Secret vòng đời (lifecycle / 생명주기)

Một secret có vòng đời:

```text
tạo
→ phân phối
→ sử dụng
→ lưu trữ
→ xoay vòng
→ thu hồi
→ hủy
```

Nếu thiết kế chỉ giải quyết bước “lưu password ở đâu” mà không có rotation/revocation, hệ thống chưa có vòng đời (lifecycle / 생명주기) hoàn chỉnh.

## 2. Không nên nhúng secret vào mã nguồn (source code / 소스 코드)

Secret nằm trong Git có thể tồn tại trong lịch sử lần ghi nhận (commit / 커밋) ngay cả khi tệp (file / 파일) hiện tại đã xóa. bản dựng (build / 빌드) log, CI sản phẩm tạo ra (artifact / 산출물), shell lịch sử (history / 이력) hoặc ảnh bộ chứa (container image / 컨테이너 이미지) tầng (layer / 계층) cũng có thể giữ bản sao.

Do đó cần tách **mã nguồn** khỏi **vật liệu bí mật (secret material)**. ứng dụng (application / 애플리케이션) nhận secret thông qua secret manager, tải công việc (workload / 워크로드) định danh (identity / 식별자) hoặc triển khai (deployment / 배포) cơ chế (mechanism / 메커니즘) có kiểm soát.

## 3. KMS là gì?

**Dịch vụ quản lý khóa (Key Management service, KMS)** cung cấp API để tạo, bảo vệ và sử dụng key mà ứng dụng (application / 애플리케이션) không nhất thiết phải đọc raw key bytes.

Ví dụ ứng dụng (application / 애플리케이션) có thể gửi dữ liệu nhỏ hoặc dữ liệu (data / 데이터) key đã mã hóa tới KMS để decrypt theo chính sách (policy / 정책). KMS còn cung cấp nhật ký kiểm tra (audit log / 감사 로그), rotation chính sách (policy / 정책) và kiểm soát truy cập (access control / 접근 제어) tập trung.

Điểm quan trọng: KMS không loại bỏ trust. ứng dụng (application / 애플리케이션) vẫn cần quyền gọi KMS, và quyền đó trở thành một năng lực (capability / 역량) cần bảo vệ.

## 4. HSM là gì?

**Mô-đun bảo mật phần cứng (Hardware security module, HSM)** là thiết bị/phần cứng chuyên dụng giữ key và thực hiện crypto thao tác (operation / 연산) trong ranh giới (boundary / 경계) được bảo vệ.

Private key có thể không bao giờ rời HSM dưới dạng plaintext. Điều này đặc biệt quan trọng với gốc (root / 루트) CA key, signing key hoặc tài sản mật mã có impact rất lớn nếu bị lộ.

HSM tăng assurance nhưng cũng tăng độ phức tạp (complexity / 복잡도), độ trễ (latency / 지연 시간), chi phí (cost / 비용) và operational phụ thuộc (dependency / 의존성).

## 5. Envelope encryption

Mã hóa trực tiếp mọi dữ liệu lớn bằng KMS master key là không hiệu quả. **Mã hóa phong bì (envelope encryption)** dùng hai tầng:

```text
KMS key / KEK
   ↓ bảo vệ
data encryption key / DEK
   ↓ mã hóa
dữ liệu thật
```

Ứng dụng (application / 애플리케이션) tạo DEK ngẫu nhiên, dùng DEK mã hóa dữ liệu (data / 데이터), sau đó dùng KMS key để mã hóa DEK. Hệ thống lưu ciphertext của dữ liệu (data / 데이터) cùng encrypted DEK.

Khi đọc, ứng dụng (application / 애플리케이션) giải mã DEK thông qua KMS rồi dùng DEK để giải mã dữ liệu (data / 데이터).

## 6. Vì sao envelope encryption hữu ích?

Nó giảm số lần gọi KMS cho dữ liệu lớn, cho phép mỗi đối tượng (object / 객체)/tệp (file / 파일) có DEK riêng và giúp rotation master key không cần mã hóa lại toàn bộ dữ liệu ngay lập tức.

Nếu chỉ thay KEK, có thể re-wrap encrypted DEK thay vì decrypt/re-encrypt toàn bộ payload.

## 7. Rotation không đồng nghĩa đổi chuỗi secret rồi restart

Rotation cần trả lời:

```text
secret cũ còn được chấp nhận trong bao lâu?
service nào đã nhận secret mới?
request đang chạy dùng phiên bản nào?
rollback thế nào?
secret cũ khi nào revoke hoàn toàn?
```

Một chiến lược an toàn thường có giai đoạn overlap: hệ thống có thể đọc bằng key cũ và mới nhưng chỉ ghi bằng key mới. Sau khi mọi dữ liệu/bên tiêu thụ (consumer / 소비자) đã migrate, key cũ mới bị retire.

## 8. Key versioning

Ciphertext nên có siêu dữ liệu (metadata / 메타데이터) chỉ ra key phiên bản (version / 버전) hoặc key identifier cần thiết để decrypt.

```text
ciphertext
key_id = key-v42
algorithm = AES-GCM
nonce = ...
```

Nếu ứng dụng (application / 애플리케이션) chỉ giữ “hiện tại (current / 현재) key” mà không biết dữ liệu cũ dùng phiên bản nào, rotation sẽ làm dữ liệu lịch sử không đọc được.

## 9. Revocation khác rotation

**Rotation** là thay key theo kế hoạch. **Revocation** là vô hiệu hóa key vì nghi ngờ compromise hoặc thay đổi quyền.

Revocation khẩn cấp có thể gây outage nếu phụ thuộc (dependency / 의존성) chưa hỗ trợ key mới. bảo mật (security / 보안) thiết kế (design / 설계) cần playbook cân bằng giữa containment và availability.

## 10. Secret zero bài toán (problem / 문제)

Nếu ứng dụng (application / 애플리케이션) cần credential để gọi secret manager, credential đầu tiên đó đến từ đâu? Đây là **secret zero bài toán (problem / 문제)**.

Giải pháp hiện đại thường dùng tải công việc (workload / 워크로드) định danh (identity / 식별자) dựa trên môi trường (environment / 환경)/nền tảng (platform / 플랫폼), ví dụ định danh (identity / 식별자) gắn với VM, pod hoặc tiến trình (process / 프로세스). ứng dụng (application / 애플리케이션) chứng minh mình là tải công việc (workload / 워크로드) hợp lệ thay vì giữ một API key dài hạn khác.

## 11. Short-lived credential

Credential sống ngắn giảm cửa sổ lạm dụng nếu bị lộ. Thay vì password tĩnh tồn tại nhiều tháng, tải công việc (workload / 워크로드) có thể đổi định danh (identity / 식별자) assertion lấy đơn vị từ (token / 토큰) chỉ sống vài phút.

Điều này chuyển yêu cầu từ “bảo vệ một secret vĩnh viễn” sang “bảo vệ định danh (identity / 식별자) + issuance đường dẫn (path / 경로) + rotation tự động”.

## 12. Least privilege cho key use

Không phải mọi dịch vụ (service / 서비스) cần `decrypt` mọi key. chính sách (policy / 정책) nên gắn quyền theo purpose:

```text
service A -> decrypt customer-profile keys
service B -> sign release artifacts
service C -> không có quyền raw decrypt
```

Nếu một dịch vụ (service / 서비스) bị compromise, blast radius bị giới hạn bởi chính sách (policy / 정책).

## 13. Auditability

Key thao tác (operation / 연산) quan trọng nên tạo kiểm tra (audit / 감사) sự kiện (event / 이벤트): ai/định danh (identity / 식별자) nào decrypt, sign, rotate hoặc disable key.

Nhật ký kiểm tra (audit log / 감사 로그) phải được bảo vệ khỏi việc attacker sửa xóa dấu vết. Detection chuỗi xử lý (pipeline / 파이프라인) có thể cảnh báo khi một tải công việc (workload / 워크로드) gọi decrypt với volume hoặc mẫu (pattern / 패턴) bất thường.

## 14. Secret trong bộ nhớ (memory / 메모리)

Ngay cả khi secret không nằm trên disk, ứng dụng (application / 애플리케이션) phải đưa nó vào bộ nhớ (memory / 메모리) để dùng trong nhiều trường hợp. vùng nhớ động (heap / 힙) dump, cốt lõi (core / 핵심) dump, gỡ lỗi (debug / 디버그) log hoặc crash report có thể làm lộ secret.

Giảm thời gian tồn tại (lifetime / 수명) của plaintext secret và tránh log toàn yêu cầu (request / 요청)/cấu hình (config / 설정) là biện pháp quan trọng. Với một số ngôn ngữ managed, việc đảm bảo zeroization tuyệt đối khó vì đối tượng (object / 객체) có thể bị bản sao (copy / 복사) hoặc di chuyển bởi thời gian chạy (runtime / 런타임).

## 15. bộ nhớ đệm (cache / 캐시) secret

Gọi KMS cho mọi yêu cầu (request / 요청) có thể tạo độ trễ (latency / 지연 시간) và phụ thuộc (dependency / 의존성) pressure. ứng dụng (application / 애플리케이션) thường bộ nhớ đệm (cache / 캐시) decrypted dữ liệu (data / 데이터) key hoặc đơn vị từ (token / 토큰) trong thời gian ngắn.

Caching cải thiện hiệu năng (performance / 성능) nhưng kéo dài thời gian secret tồn tại trong tiến trình (process / 프로세스). Đây là sự đánh đổi (trade-off / 트레이드오프) giữa availability/hiệu năng (performance / 성능) và exposure cửa sổ (window / 윈도우).

## 16. Multi-region key phụ thuộc (dependency / 의존성)

Nếu dữ liệu (data / 데이터) ở region A chỉ decrypt được bằng KMS endpoint ở region B, mạng (network / 네트워크) partition có thể biến bảo mật (security / 보안) phụ thuộc (dependency / 의존성) thành availability thất bại (failure / 실패).

Thiết kế geo-distributed cần cân nhắc key replication, region-local key hierarchy và disaster khôi phục (recovery / 복구). “Key an toàn” nhưng không thể truy cập khi sự cố (incident / 인시던트) cũng có thể làm hệ thống không phục vụ được.

## 17. Backup và key destruction

Backup ciphertext vô dụng nếu key cần decrypt đã bị mất ngoài ý muốn. Ngược lại, nếu mục tiêu là crypto-shredding — làm dữ liệu vĩnh viễn không đọc được — hủy key có thể là cơ chế mạnh.

Do đó backup chính sách (policy / 정책) phải bao gồm key material hoặc khôi phục (recovery / 복구) hierarchy phù hợp, với kiểm soát truy cập (access control / 접근 제어) nghiêm ngặt hơn dữ liệu thông thường.

## 18. cơ sở dữ liệu (database / 데이터베이스) encryption và ứng dụng (application / 애플리케이션) encryption

Encryption at rest của disk/cơ sở dữ liệu (database / 데이터베이스) bảo vệ một số threat như mất lưu trữ (storage / 저장소) media, nhưng cơ sở dữ liệu (database / 데이터베이스) tiến trình (process / 프로세스) vẫn có thể đọc plaintext. Application-level encryption có thể thu hẹp trust ranh giới (boundary / 경계) nhưng làm truy vấn (query / 쿼리)/indexing phức tạp hơn.

Không nên hỏi “đã mã hóa chưa?” mà phải hỏi “mã hóa bảo vệ chống attacker nào và plaintext xuất hiện ở ranh giới (boundary / 경계) nào?”.

## 19. dạng thất bại (failure mode / 실패 모드) khi KMS unavailable

Nếu KMS không phản hồi, ứng dụng (application / 애플리케이션) có thể:

```text
fail closed
use cached key
serve read-only
reject sensitive operations
```

Lựa chọn phụ thuộc threat mô hình (model / 모델). Fail-open có thể giữ availability nhưng phá bảo mật (security / 보안) guarantee; fail-closed bảo vệ dữ liệu nhưng có thể gây outage.

Bảo mật (security / 보안) và độ tin cậy (reliability / 신뢰성) không thể tách rời ở đây.

## Dùng chung (common / 공통) Misconceptions

**“Đưa secret vào môi trường (environment / 환경) variable là đã an toàn.”** Nó tốt hơn hard-code trong nhiều trường hợp nhưng vẫn có thể bị lộ qua tiến trình (process / 프로세스) inspection, crash dump hoặc logging.

**“KMS giữ key nên ứng dụng (application / 애플리케이션) không cần bảo mật (security / 보안).”** ứng dụng (application / 애플리케이션) định danh (identity / 식별자) và KMS permission trở thành attack surface mới.

**“Rotation chỉ cần đổi secret.”** Rotation là phân tán (distributed / 분산) di chuyển (migration / 마이그레이션) cần versioning, overlap và quay lui (rollback / 롤백).

**“Encryption at rest nghĩa là cơ sở dữ liệu (database / 데이터베이스) admin không đọc được dữ liệu (data / 데이터).”** Không nhất thiết; ranh giới (boundary / 경계) bảo vệ phụ thuộc tầng thực hiện encryption.

## Mô hình tư duy

> Key management là một phân tán (distributed / 분산) bảo mật (security / 보안) giao thức (protocol / 프로토콜) kéo dài toàn vòng đời của secret, không phải một tệp (file / 파일) cấu hình được cất kỹ.

Ở mức cấp cao (senior / 시니어)/Master, cần theo được đường: tải công việc (workload / 워크로드) định danh (identity / 식별자) → authorization → KMS/HSM → key hierarchy → ciphertext siêu dữ liệu (metadata / 메타데이터) → rotation/revocation → kiểm tra (audit / 감사) → outage hành vi (behavior / 동작).

Xem thêm: [Applied cryptography](./01_cryptographic_protocol_composition_nonce_and_key_misuse.md), [PKI](./02_pki_certificate_validation_mtls_and_service_identity.md) và [Container capabilities](../../03_operating_systems/advanced/06_containers_namespaces_cgroups_capabilities_and_seccomp.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 security boundaries attack chains and exploitability](./00_security_boundaries_attack_chains_and_exploitability.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
