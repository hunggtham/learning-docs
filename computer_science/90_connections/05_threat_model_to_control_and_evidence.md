# Từ mô hình đe dọa → quyền hạn → bí mật → bằng chứng vận hành

> **Mạch đọc:** Chapter này là tuyến liên kết, không tạo thêm một thư viện bảo mật riêng. Nền tảng nằm ở [mô hình đe dọa và nguyên tắc bảo mật](../07_security_reliability/00_threat_models_and_security_principles.md), [định danh, xác thực và phân quyền](../07_security_reliability/02_identity_authentication_and_authorization.md), cùng [khóa, bí mật, chứng chỉ và vận hành an toàn](../07_security_reliability/07_keys_secrets_certificates_and_secure_operations.md). Chapter này nối các owner đó với Backend, Linux, DevOps và khả năng quan sát để trả lời câu hỏi: **từ một mối đe dọa cụ thể, làm thế nào đi tới control có thể kiểm chứng bằng evidence?**

Một hệ thống có thể có mã hóa, RBAC, secret manager và audit log nhưng vẫn không an toàn nếu chuỗi reasoning bị đứt. Ví dụ có RBAC nhưng không biết quyền hiệu lực sau delegation; có secret manager nhưng secret bị log; có audit log nhưng không chứng minh được ai đã làm gì.

Chuỗi cần giữ là:

```text
tài sản + bất biến nghiệp vụ
→ tác nhân đe dọa + năng lực
→ ranh giới tin cậy + đường tấn công
→ thuộc tính bảo mật cần giữ
→ quyết định identity + authority
→ control cho bí mật / dữ liệu
→ enforcement lúc chạy
→ telemetry + audit evidence
→ phát hiện + phản ứng
→ rủi ro còn lại
```

## 1. Bắt đầu từ tài sản và bất biến, không bắt đầu từ công cụ

**Tài sản cần bảo vệ (asset / 보호자산)** có thể là tiền, dữ liệu người dùng, credential, khóa ký, source code, quyền triển khai production hoặc tính toàn vẹn của một bản ghi.

Với mỗi tài sản, cần viết **bất biến bảo mật (security invariant / 보안불변식)**.

Ví dụ với file hóa đơn của một tenant:

```text
người dùng chỉ đọc file thuộc tenant được phép
token bị lộ không cho quyền vượt quá scope và thời gian dự kiến
mọi truy cập đặc quyền phải truy ngược được actor, lý do và thời điểm
```

Nếu chỉ viết “bucket phải private”, ta mới mô tả implementation, chưa mô tả property cần giữ. Bucket private không ngăn signed URL quá dài hạn hoặc service account có quyền quá rộng.

## 2. Mô hình đe dọa phải nói rõ năng lực đối thủ

**Mô hình đe dọa (threat model / 위협모델)** có giá trị khi mô tả kẻ tấn công kiểm soát boundary nào.

Các năng lực khác nhau dẫn tới control khác nhau:

```text
kiểm soát input từ browser
chiếm một user session
chiếm một workload identity
thực thi được trong CI runner
có support role nội bộ
đọc được một database replica
lấy được API key dài hạn
```

Nếu đối thủ chỉ điều khiển browser input, server-side authorization và validation là boundary quan trọng. Nếu workload identity đã bị compromise, UI ẩn nút hoặc token còn hạn không giúp nhiều; blast radius của service account mới quyết định hậu quả.

## 3. Ranh giới tin cậy là nơi phải kiểm lại giả định

**Ranh giới tin cậy (trust boundary / 신뢰경계)** xuất hiện khi dữ liệu hoặc quyền đi sang một ngữ cảnh mới:

```text
browser → API
API → database
service A → service B
queue → worker
CI runner → artifact registry
workload → cloud API
support operator → production console
tenant A → shared platform
```

Mỗi boundary phải trả lời:

```text
ai đang gọi?
credential nào chứng minh actor?
actor được làm gì trên resource nào?
evidence nào còn lại sau action?
```

Mạng nội bộ không tự chứng minh identity; mTLS không tự cấp authorization; gateway check một lần không có nghĩa worker downstream được bỏ domain invariant.

## 4. Xác thực, định danh và phân quyền là ba lớp khác nhau

**Xác thực (authentication / 인증)** chứng minh principal là ai. **Định danh (identity / 신원)** mang context như user, tenant, workload hoặc delegation. **Phân quyền (authorization / 인가)** quyết định principal được làm operation nào trên resource nào.

Chuỗi là:

```text
credential
→ principal đã xác thực
→ identity context
→ policy evaluation
→ quyền hiệu lực
→ action
```

Một bug phổ biến xuất hiện khi API enqueue job chỉ với `user_id`, còn worker chạy bằng service account quyền rộng và mất tenant/scope ban đầu. Boundary bất đồng bộ khi đó vô tình nâng quyền.

## 5. Quyền được cấp khác quyền hiệu lực

IAM role hoặc RBAC object chỉ mô tả một phần. **Quyền hiệu lực (effective authority / 유효권한)** là kết quả của nhiều lớp:

```text
human role
+ group membership
+ token scope
+ resource policy
+ workload identity
+ delegated authority
+ cached/stale policy
+ emergency exception
```

Một principal không có role admin trực tiếp vẫn có thể lên quyền cao qua `assume role`, secret đọc được hoặc quyền sửa CI workflow.

Vì vậy review nên nhìn **đường nâng quyền (privilege-escalation path / 권한상승경로)**, không chỉ danh sách role.

## 6. Đặc quyền tối thiểu phải gắn với phạm vi thiệt hại

**Đặc quyền tối thiểu (least privilege / 최소권한)** không chỉ là ít permission hơn; mục tiêu là giảm **phạm vi ảnh hưởng (blast radius / 피해범위)** khi credential hoặc workload bị compromise.

Một worker xử lý hóa đơn của một tenant không nên mặc định có quyền đọc mọi tenant, sửa mọi bucket hoặc lấy mọi secret.

Tuy vậy permission quá chi tiết nhưng không có lifecycle cũng tạo hỗn loạn. Role nên có use case ổn định, owner, review interval và telemetry về quyền thực sự được dùng.

## 7. Bí mật là capability có vòng đời

**Bí mật (secret / 시크릿)** không chỉ là chuỗi cần giấu. Nó là capability có lifecycle:

```text
cấp phát
→ phân phối
→ sử dụng
→ quan sát usage
→ xoay vòng
→ xác minh credential mới đã được dùng
→ thu hồi credential cũ
→ chứng minh credential cũ không còn usage
```

Secret manager chỉ giải quyết một phần. Secret vẫn có thể rò qua environment variable, crash dump, shell history, build log hoặc trace attribute.

Rotation chưa hoàn tất chỉ vì control plane đã tạo secret mới; cần evidence rằng consumer đã chuyển sang credential mới trước khi revoke cái cũ.

## 8. Dữ liệu nhạy cảm cần phân loại và ranh giới mục đích

**Phân loại dữ liệu (data classification / 데이터분류)** giúp quyết định encryption, retention, logging, export và access review.

Một mô hình đơn giản:

```text
public
internal
confidential
restricted
```

Nhãn chỉ có giá trị nếu gắn với behavior. Ví dụ dữ liệu restricted có thể yêu cầu mã hóa, không log plaintext, retention ngắn và audit trail.

Ngoài câu “ai được đọc?”, hệ thống còn phải hỏi “được đọc để làm gì?”. Đây là **ranh giới mục đích sử dụng (purpose boundary / 목적경계)**.

## 9. Logging và tracing có thể tự tạo lỗ hổng

**Khả năng quan sát (observability / 관측가능성)** vừa là evidence, vừa có thể là attack surface.

Log không nên chứa access token, cookie, password-reset URL, secret hoặc payload nhạy cảm chỉ vì “debug cho dễ”.

Cần phân biệt:

```text
identifier để correlation
≠
credential có quyền authorization
```

Request ID nên log; access token đầy đủ thì không.

## 10. Nhật ký kiểm toán khác nhật ký ứng dụng

**Nhật ký kiểm toán (audit log / 감사로그)** phục vụ trách nhiệm và điều tra quyền hạn.

Một sự kiện đặc quyền hữu ích cần có:

```text
actor / principal
delegation nếu có
action
resource
tenant / scope
time
source context
policy decision / reason
result
correlation id
```

`GET /users/123 200` trong application log không đủ để chứng minh một support operator đã truy cập hợp lệ.

## 11. Control chỉ có giá trị khi có bằng chứng nó đang hoạt động

Có thể tách control thành:

- **phòng ngừa (preventive control / 예방통제)** — cố ngăn sự cố;
- **phát hiện (detective control / 탐지통제)** — cho biết sự cố đã hoặc đang xảy ra;
- **khắc phục (corrective control / 교정통제)** — giới hạn và phục hồi hậu quả.

Ví dụ secret rotation là preventive/corrective; alert về credential cũ vẫn được dùng là detective.

Một control không có evidence khó phân biệt giữa “đang hoạt động” và “chỉ tồn tại trên sơ đồ”.

## 12. Không có cảnh báo không đồng nghĩa không có sự cố

**Bằng chứng âm (negative evidence / 부정증거)** như “không có alert” chỉ có ý nghĩa nếu biết telemetry coverage đủ và pipeline quan sát đang khỏe.

Nếu log exporter chết hoặc metric bị sampling sai, im lặng không chứng minh hệ thống an toàn.

Do đó cần phân biệt:

```text
không thấy signal vì sự cố không xảy ra
vs
không thấy signal vì sensor/telemetry không hoạt động
```

## 13. Correlation ID không phải credential

Một **mã tương quan (correlation identifier / 상관식별자)** giúp nối request, job, message và downstream call. Nó không nên được dùng như secret hoặc authorization proof.

Các loại ID nên có vai trò riêng:

```text
request/correlation id — nối telemetry
operation/idempotency id — đại diện ý định nghiệp vụ
message id — nhận diện delivery
principal id — actor
resource id — đối tượng bị tác động
```

Trộn vai trò làm log khó dùng và có thể tạo lỗ hổng.

## 14. Case: URL ký sẵn cho file tenant

Bài toán:

```text
user → API → storage signed URL → file
```

Bất biến:

- user chỉ lấy URL cho file thuộc tenant hợp lệ;
- URL có TTL và scope tối thiểu;
- URL không được log toàn bộ nếu nó là capability;
- audit phải truy được ai đã yêu cầu URL cho resource nào.

Failure có thể nằm ở nhiều lớp: authorization sai, TTL quá dài, bucket policy quá rộng, signed URL bị log hoặc audit thiếu tenant/resource.

Điểm quan trọng là không có một control đơn lẻ giải quyết toàn bộ chuỗi.

## 15. Case: CI runner có thể triển khai production

CI runner thường giữ capability mạnh: đọc source, lấy artifact credential, ký hoặc deploy.

Threat model phải hỏi:

```text
ai có thể sửa workflow?
workflow từ fork có chạy với secret không?
runner có persistent state không?
artifact nào được trust?
deploy credential có scope gì?
audit trail nối commit → build → artifact → deploy ra sao?
```

Nếu attacker sửa workflow và lấy cloud credential, vấn đề không còn là “CI bị lỗi” mà là authority graph đã cho một boundary không đáng tin quyền production.

## 16. Mẫu review 12 câu hỏi

Khi review một flow nhạy cảm, dùng bộ câu hỏi:

```text
1. Tài sản nào cần bảo vệ?
2. Bất biến nào phải luôn đúng?
3. Ai có thể cố phá bất biến?
4. Họ kiểm soát boundary nào?
5. Principal nào thực hiện action?
6. Quyền hiệu lực đến từ đâu?
7. Secret/data đi qua đâu?
8. Preventive control là gì?
9. Evidence nào chứng minh control hoạt động?
10. Detective/corrective control là gì?
11. Failure hoặc compromise lan tới đâu?
12. Rủi ro còn lại có được chấp nhận và review không?
```

## 17. Rủi ro còn lại phải được nêu rõ

Sau mọi control vẫn còn **rủi ro còn lại (residual risk / 잔여위험)**.

Không nên kết thúc review bằng “đã có MFA/encryption/WAF nên an toàn”. Cần nêu:

```text
failure nào vẫn có thể xảy ra?
blast radius còn bao nhiêu?
detection latency bao lâu?
recovery path là gì?
owner nào chấp nhận rủi ro?
```

Đây là bước nối security design với operational accountability.

## 18. Kết nối và bàn giao

Khi cần identity/session ở application layer, đọc [Backend Auth, Session & Identity](../../10_backend/backend_core/02_auth_session_identity.md). Khi cần cơ chế Linux enforcement, đọc [Linux](../../linux/README.md). Khi cần secret rotation, supply chain và production policy, đọc [DevOps Security Governance](../../devops_platform_engineering/08_security_governance/00_identity_secrets_policy_and_supply_chain.md). Khi cần failure xuyên nhiều lớp, đọc [Production Practice](../../devops_platform_engineering/10_production_practice/README.md).

> **Bàn giao:** Sau chapter này, một control chỉ được xem là hoàn chỉnh khi có thể nối **threat → authority/data boundary → enforcement → evidence → detection/response → residual risk**. Nếu thiếu một mắt xích, security review vẫn chưa khép kín.