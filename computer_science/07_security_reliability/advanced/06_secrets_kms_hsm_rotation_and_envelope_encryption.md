# Secret, KMS, HSM, rotation và envelope encryption

Bảo mật ứng dụng không dừng ở việc chọn thuật toán mã hóa đúng. Sau khi một hệ thống quyết định dùng khóa bí mật, câu hỏi thực tế trở thành: khóa được tạo ở đâu, ai được dùng, lưu ở đâu, xoay vòng thế nào, audit ra sao và chuyện gì xảy ra nếu một bản sao bị lộ.

**Secret** là dữ liệu cần được bảo vệ khỏi truy cập trái phép, ví dụ API key, database password hoặc private key. **Khóa mật mã (cryptographic key)** là một loại secret có semantics đặc biệt vì nó trực tiếp quyết định khả năng mã hóa, giải mã, ký hoặc xác minh. Không nên coi mọi secret như chuỗi cấu hình bình thường.

## 1. Secret lifecycle

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

Nếu thiết kế chỉ giải quyết bước “lưu password ở đâu” mà không có rotation/revocation, hệ thống chưa có lifecycle hoàn chỉnh.

## 2. Không nên nhúng secret vào source code

Secret nằm trong Git có thể tồn tại trong lịch sử commit ngay cả khi file hiện tại đã xóa. Build log, CI artifact, shell history hoặc container image layer cũng có thể giữ bản sao.

Do đó cần tách **mã nguồn** khỏi **vật liệu bí mật (secret material)**. Application nhận secret thông qua secret manager, workload identity hoặc deployment mechanism có kiểm soát.

## 3. KMS là gì?

**Dịch vụ quản lý khóa (Key Management Service, KMS)** cung cấp API để tạo, bảo vệ và sử dụng key mà application không nhất thiết phải đọc raw key bytes.

Ví dụ application có thể gửi dữ liệu nhỏ hoặc data key đã mã hóa tới KMS để decrypt theo policy. KMS còn cung cấp audit log, rotation policy và access control tập trung.

Điểm quan trọng: KMS không loại bỏ trust. Application vẫn cần quyền gọi KMS, và quyền đó trở thành một capability cần bảo vệ.

## 4. HSM là gì?

**Mô-đun bảo mật phần cứng (Hardware Security Module, HSM)** là thiết bị/phần cứng chuyên dụng giữ key và thực hiện crypto operation trong boundary được bảo vệ.

Private key có thể không bao giờ rời HSM dưới dạng plaintext. Điều này đặc biệt quan trọng với root CA key, signing key hoặc tài sản mật mã có impact rất lớn nếu bị lộ.

HSM tăng assurance nhưng cũng tăng complexity, latency, cost và operational dependency.

## 5. Envelope encryption

Mã hóa trực tiếp mọi dữ liệu lớn bằng KMS master key là không hiệu quả. **Mã hóa phong bì (envelope encryption)** dùng hai tầng:

```text
KMS key / KEK
   ↓ bảo vệ
data encryption key / DEK
   ↓ mã hóa
dữ liệu thật
```

Application tạo DEK ngẫu nhiên, dùng DEK mã hóa data, sau đó dùng KMS key để mã hóa DEK. Hệ thống lưu ciphertext của data cùng encrypted DEK.

Khi đọc, application giải mã DEK thông qua KMS rồi dùng DEK để giải mã data.

## 6. Vì sao envelope encryption hữu ích?

Nó giảm số lần gọi KMS cho dữ liệu lớn, cho phép mỗi object/file có DEK riêng và giúp rotation master key không cần mã hóa lại toàn bộ dữ liệu ngay lập tức.

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

Một chiến lược an toàn thường có giai đoạn overlap: hệ thống có thể đọc bằng key cũ và mới nhưng chỉ ghi bằng key mới. Sau khi mọi dữ liệu/consumer đã migrate, key cũ mới bị retire.

## 8. Key versioning

Ciphertext nên có metadata chỉ ra key version hoặc key identifier cần thiết để decrypt.

```text
ciphertext
key_id = key-v42
algorithm = AES-GCM
nonce = ...
```

Nếu application chỉ giữ “current key” mà không biết dữ liệu cũ dùng phiên bản nào, rotation sẽ làm dữ liệu lịch sử không đọc được.

## 9. Revocation khác rotation

**Rotation** là thay key theo kế hoạch. **Revocation** là vô hiệu hóa key vì nghi ngờ compromise hoặc thay đổi quyền.

Revocation khẩn cấp có thể gây outage nếu dependency chưa hỗ trợ key mới. Security design cần playbook cân bằng giữa containment và availability.

## 10. Secret zero problem

Nếu application cần credential để gọi secret manager, credential đầu tiên đó đến từ đâu? Đây là **secret zero problem**.

Giải pháp hiện đại thường dùng workload identity dựa trên environment/platform, ví dụ identity gắn với VM, pod hoặc process. Application chứng minh mình là workload hợp lệ thay vì giữ một API key dài hạn khác.

## 11. Short-lived credential

Credential sống ngắn giảm cửa sổ lạm dụng nếu bị lộ. Thay vì password tĩnh tồn tại nhiều tháng, workload có thể đổi identity assertion lấy token chỉ sống vài phút.

Điều này chuyển yêu cầu từ “bảo vệ một secret vĩnh viễn” sang “bảo vệ identity + issuance path + rotation tự động”.

## 12. Least privilege cho key use

Không phải mọi service cần `decrypt` mọi key. Policy nên gắn quyền theo purpose:

```text
service A -> decrypt customer-profile keys
service B -> sign release artifacts
service C -> không có quyền raw decrypt
```

Nếu một service bị compromise, blast radius bị giới hạn bởi policy.

## 13. Auditability

Key operation quan trọng nên tạo audit event: ai/identity nào decrypt, sign, rotate hoặc disable key.

Audit log phải được bảo vệ khỏi việc attacker sửa xóa dấu vết. Detection pipeline có thể cảnh báo khi một workload gọi decrypt với volume hoặc pattern bất thường.

## 14. Secret trong memory

Ngay cả khi secret không nằm trên disk, application phải đưa nó vào memory để dùng trong nhiều trường hợp. Heap dump, core dump, debug log hoặc crash report có thể làm lộ secret.

Giảm lifetime của plaintext secret và tránh log toàn request/config là biện pháp quan trọng. Với một số ngôn ngữ managed, việc đảm bảo zeroization tuyệt đối khó vì object có thể bị copy hoặc di chuyển bởi runtime.

## 15. Cache secret

Gọi KMS cho mọi request có thể tạo latency và dependency pressure. Application thường cache decrypted data key hoặc token trong thời gian ngắn.

Caching cải thiện performance nhưng kéo dài thời gian secret tồn tại trong process. Đây là trade-off giữa availability/performance và exposure window.

## 16. Multi-region key dependency

Nếu data ở region A chỉ decrypt được bằng KMS endpoint ở region B, network partition có thể biến security dependency thành availability failure.

Thiết kế geo-distributed cần cân nhắc key replication, region-local key hierarchy và disaster recovery. “Key an toàn” nhưng không thể truy cập khi incident cũng có thể làm hệ thống không phục vụ được.

## 17. Backup và key destruction

Backup ciphertext vô dụng nếu key cần decrypt đã bị mất ngoài ý muốn. Ngược lại, nếu mục tiêu là crypto-shredding — làm dữ liệu vĩnh viễn không đọc được — hủy key có thể là cơ chế mạnh.

Do đó backup policy phải bao gồm key material hoặc recovery hierarchy phù hợp, với access control nghiêm ngặt hơn dữ liệu thông thường.

## 18. Database encryption và application encryption

Encryption at rest của disk/database bảo vệ một số threat như mất storage media, nhưng database process vẫn có thể đọc plaintext. Application-level encryption có thể thu hẹp trust boundary nhưng làm query/indexing phức tạp hơn.

Không nên hỏi “đã mã hóa chưa?” mà phải hỏi “mã hóa bảo vệ chống attacker nào và plaintext xuất hiện ở boundary nào?”.

## 19. Failure mode khi KMS unavailable

Nếu KMS không phản hồi, application có thể:

```text
fail closed
use cached key
serve read-only
reject sensitive operations
```

Lựa chọn phụ thuộc threat model. Fail-open có thể giữ availability nhưng phá security guarantee; fail-closed bảo vệ dữ liệu nhưng có thể gây outage.

Security và reliability không thể tách rời ở đây.

## Common Misconceptions

**“Đưa secret vào environment variable là đã an toàn.”** Nó tốt hơn hard-code trong nhiều trường hợp nhưng vẫn có thể bị lộ qua process inspection, crash dump hoặc logging.

**“KMS giữ key nên application không cần security.”** Application identity và KMS permission trở thành attack surface mới.

**“Rotation chỉ cần đổi secret.”** Rotation là distributed migration cần versioning, overlap và rollback.

**“Encryption at rest nghĩa là database admin không đọc được data.”** Không nhất thiết; boundary bảo vệ phụ thuộc tầng thực hiện encryption.

## Mô hình tư duy

> Key management là một distributed security protocol kéo dài toàn vòng đời của secret, không phải một file cấu hình được cất kỹ.

Ở mức Senior/Master, cần theo được đường: workload identity → authorization → KMS/HSM → key hierarchy → ciphertext metadata → rotation/revocation → audit → outage behavior.

Xem thêm: [Applied cryptography](./01_cryptographic_protocol_composition_nonce_and_key_misuse.md), [PKI](./02_pki_certificate_validation_mtls_and_service_identity.md) và [Container capabilities](../../03_operating_systems/advanced/06_containers_namespaces_cgroups_capabilities_and_seccomp.md).
