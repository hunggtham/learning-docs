# Từ mô hình đe dọa → quyền hạn → dữ liệu bí mật → bằng chứng vận hành

> **Mạch đọc:** Chapter này là tuyến liên kết (connection route / 연결 경로), không tạo một thư viện bảo mật (security / 보안) mới. Nền tảng khái niệm thuộc [mô hình đe dọa và nguyên tắc bảo mật](../07_security_reliability/00_threat_models_and_security_principles.md); định danh (identity / 식별자), xác thực (authentication / 인증) và phân quyền (authorization / 인가) thuộc [identity, authentication and authorization](../07_security_reliability/02_identity_authentication_and_authorization.md); vòng đời khóa và bí mật thuộc [keys, secrets, certificates and secure operations](../07_security_reliability/07_keys_secrets_certificates_and_secure_operations.md). Chapter này nối các đơn vị sở hữu đó với Backend, Linux, DevOps và khả năng quan sát (observability / 관측 가능성) để trả lời một câu hỏi thực dụng: **từ một mối đe dọa cụ thể, làm thế nào đi tới điều khiển có thể kiểm chứng bằng bằng chứng?**

Một hệ thống thường thất bại trong bảo mật không phải vì thiếu một công nghệ riêng lẻ, mà vì chuỗi suy luận bị đứt ở giữa. Team có thể có mã hóa (encryption / 암호화) nhưng không biết asset nào đang được bảo vệ; có RBAC nhưng không biết quyền thực tế sau khi token, cache và service account kết hợp; có secret manager nhưng secret vẫn bị log; có audit log nhưng log không đủ dữ liệu để chứng minh ai đã làm gì.

Tuyến đúng nên được đọc như một chuỗi:

```text
asset + business invariant
→ threat actor + capability
→ trust boundary + attack path
→ required security property
→ identity + authority decision
→ secret/data handling control
→ runtime enforcement
→ telemetry + audit evidence
→ detection + response
→ review residual risk
```

## 1. Bắt đầu từ asset và bất biến, không bắt đầu từ tool

Một **tài sản cần bảo vệ (asset / 보호 자산)** có thể là tiền, dữ liệu người dùng, credential, khóa ký, source code, khả năng deploy production hoặc tính toàn vẹn của một bản ghi. Với mỗi asset, cần viết **bất biến bảo mật (security invariant / 보안 불변식)** mà hệ thống phải giữ.

Ví dụ với file hóa đơn của tenant:

```text
Invariant A: user chỉ đọc file thuộc tenant mà họ đang được phép truy cập.
Invariant B: URL hoặc token bị lộ không được cho quyền vượt quá scope và thời gian dự kiến.
Invariant C: mọi privileged access phải truy ngược được actor, reason và thời điểm.
```

Nếu chỉ viết “bảo vệ file bằng S3 private bucket” thì ta mới mô tả implementation, chưa mô tả property cần giữ. Bucket private không ngăn backend tạo signed URL quá dài hạn, không ngăn service account có quyền đọc toàn bộ tenant, và không bảo đảm audit trail.

> **Chuyển mạch:** Sau khi biết cái gì phải luôn đúng, câu hỏi kế tiếp là ai có thể cố làm nó sai và họ có năng lực gì.

## 2. Mô hình đe dọa phải mô tả capability, không chỉ tên attacker

**Mô hình đe dọa (threat model / 위협 모델)** có giá trị khi nó nói được attacker kiểm soát boundary nào. “Hacker Internet” quá chung. Các capability khác nhau tạo control khác nhau:

```text
attacker controls browser input
attacker steals one user session
attacker compromises one workload
attacker gains CI runner execution
malicious insider has support role
attacker reads one database replica
attacker obtains one long-lived API key
```

Nếu attacker chỉ kiểm soát browser input, server-side authorization và input validation là boundary quan trọng. Nếu attacker đã compromise workload identity của API service, việc UI ẩn nút hoặc JWT còn hạn không giúp nhiều; khi đó blast radius của service account, network/data permissions và secret exposure mới quyết định hậu quả.

Do đó threat model nên gắn với **năng lực đối thủ (adversary capability / 공격자 능력)** và **phạm vi chiếm quyền (compromise scope / 침해 범위)**. Cùng một vulnerability nhưng ở principal read-only và principal admin tạo residual risk rất khác.

## 3. Trust boundary là nơi assumption phải được kiểm tra lại

**Ranh giới tin cậy (trust boundary / 신뢰 경계)** xuất hiện khi dữ liệu hoặc quyền đi sang một ngữ cảnh có assumption khác:

```text
browser → API
API → database
service A → service B
job queue → worker
CI runner → artifact registry
Kubernetes workload → cloud API
support operator → production console
tenant A → shared platform
```

Mỗi boundary phải trả lời ít nhất bốn câu:

1. actor nào đang gọi;
2. actor được chứng minh bằng credential nào;
3. actor được phép làm operation nào trên resource nào;
4. evidence nào còn lại sau operation.

Bốn câu này biến “zero trust” từ khẩu hiệu thành các kiểm tra cụ thể. Mạng nội bộ không tự chứng minh identity; mTLS không tự cấp authorization; API gateway check một lần không có nghĩa worker bất đồng bộ được phép bỏ kiểm tra domain invariant.

## 4. Xác thực, định danh và phân quyền là ba state khác nhau

Backend đã có canonical owner tại [Auth, session và identity](../../10_backend/backend_core/02_auth_session_identity.md). Tuyến này chỉ nhấn mạnh sự nối tiếp:

```text
credential
→ authenticated principal
→ identity context
→ policy evaluation
→ effective authority
→ action
```

**Xác thực (authentication / 인증)** chứng minh credential thuộc principal nào. **Định danh (identity / 식별자)** là representation của subject, tenant, workload, assurance level hoặc delegation context. **Phân quyền (authorization / 인가)** quyết định principal đó được làm gì trên resource cụ thể.

Một bug phổ biến xảy ra khi hệ thống giữ identity nhưng làm mất context phân quyền. Ví dụ API enqueue job chỉ với `user_id`, worker chạy bằng service account có quyền rộng và không còn `tenant_id`, authorization reason hoặc scope ban đầu. Khi đó asynchronous boundary đã vô tình nâng quyền.

Vì vậy identity propagation phải có chủ ý. Không serialize cả HTTP request sang queue; chỉ truyền những claim cần thiết, operation intent và stable resource identifiers. Worker phải biết policy nào được snapshot lúc enqueue và policy nào phải kiểm tra lại tại thời điểm execute.

## 5. Quyền được cấp khác quyền thực tế

Policy file, IAM role hoặc RBAC object chỉ mô tả một phần. Điều cần quan tâm là **quyền thực tế (effective authority / 유효 권한)** sau composition:

```text
human role
+ group membership
+ session/token scope
+ resource policy
+ workload identity
+ delegated authority
+ cache / stale policy
+ emergency exception
= effective authority
```

Một account không có `admin` trực tiếp vẫn có thể đạt quyền admin thông qua `assume role`, secret đọc được, ability sửa CI workflow hoặc quyền attach policy. Đây là lý do threat model phải xem **đường nâng quyền (privilege-escalation path / 권한 상승 경로)** chứ không chỉ danh sách role.

Khi review một incident, hỏi “principal này có role gì?” chưa đủ. Cần hỏi “từ capability ban đầu, principal này có thể đi qua những edge nào trong authority graph?”.

## 6. Least privilege phải gắn với failure domain

**Đặc quyền tối thiểu (least privilege / 최소 권한)** không chỉ là giảm số permission. Nó là giảm blast radius theo failure domain thực tế.

Ví dụ một worker xử lý invoice của một tenant không nhất thiết cần:

```text
read all tenants
write all buckets
assume arbitrary roles
read deployment secrets
access production database admin endpoint
```

Nếu workload bị compromise, phạm vi quyền xác định damage tối đa. Thiết kế tốt có thể tách read/write role, tenant boundary, environment boundary và human/workload identity.

Nhưng least privilege quá chi tiết mà không có lifecycle sẽ tạo permission chaos. Do đó role/capability nên được thiết kế theo use case ổn định, có owner, review interval và telemetry về quyền thực sự được dùng.

## 7. Secret không phải chỉ là chuỗi ký tự cần giấu

**Bí mật (secret / 시크릿)** là một capability có vòng đời: ai tạo, ai consume, scope gì, TTL bao lâu, rotation thế nào, revoke ra sao và bằng chứng nào xác nhận credential cũ không còn được dùng.

Một secret manager không giải quyết toàn bộ bài toán. Workload vẫn phải có bootstrap identity để lấy secret; secret có thể bị copy vào environment variable, crash dump, shell history, build log hoặc trace attribute.

Tuyến vòng đời nên là:

```text
issue
→ distribute
→ consume
→ observe usage
→ rotate with overlap
→ verify new credential adoption
→ revoke old credential
→ prove old usage stopped
```

Điểm cuối rất quan trọng. Rotation “thành công” khi control plane ghi secret mới chưa đủ; cần evidence từ consumer rằng connection mới đang dùng credential mới và credential cũ có thể revoke an toàn.

DevOps triển khai chiều vận hành này tại [identity, secrets, policy and supply chain](../../devops_platform_engineering/08_security_governance/00_identity_secrets_policy_and_supply_chain.md).

## 8. Dữ liệu nhạy cảm cần classification và purpose boundary

Không phải dữ liệu nào cũng cần cùng control. **Phân loại dữ liệu (data classification / 데이터 분류)** giúp quyết định encryption, retention, logging, export và access review.

Một mô hình tối giản có thể phân biệt:

```text
public
internal
confidential
restricted / highly sensitive
```

Nhưng nhãn chỉ có giá trị khi gắn với behavior. Ví dụ `restricted` có thể yêu cầu encryption at rest, no plaintext logs, short retention, explicit export approval và audit trail.

Quan trọng hơn, confidentiality không phải boundary duy nhất. Dữ liệu có thể được đọc hợp lệ nhưng dùng sai purpose. Vì vậy một hệ thống mature cần trả lời cả “ai được đọc?” và “được đọc để làm gì?”.

Backend privacy lifecycle đã đề cập collect → purpose → retain → archive/delete. Tuyến này mở rộng rằng policy, log và analytics pipeline đều phải giữ cùng boundary; việc application không log password nhưng downstream observability exporter gửi full request body vẫn là data leak.

## 9. Logging và tracing có thể phá vỡ chính control bảo mật

**Khả năng quan sát (observability / 관측 가능성)** thường được xem là control hỗ trợ bảo mật, nhưng nó cũng có thể trở thành attack surface. Log có thể chứa access token, cookie, password-reset URL, customer record hoặc signed URL.

Redaction phải xảy ra trước serialization/export khi có thể. Nếu secret đã vào centralized log backend, việc xóa ở UI không loại bỏ bản sao trong storage, archive hoặc downstream sink.

Một telemetry contract tốt phân biệt:

```text
identifier needed for correlation
vs
credential capable of authorization
```

Request ID nên log; access token đầy đủ không nên. User/tenant identifier có thể cần pseudonymization tùy context; payload nhạy cảm cần field-level allowlist thay vì dump toàn object.

## 10. Audit log khác application log

**Nhật ký kiểm toán (audit log / 감사 로그)** trả lời câu hỏi trách nhiệm và thay đổi quyền hạn, không chỉ debug application.

Một privileged event hữu ích thường cần:

```text
who / principal
on-behalf-of / delegation
what action
which resource
tenant / scope
when
source context
policy decision / reason
result
correlation id
```

Nếu support operator đọc record nhạy cảm, audit event nên nói actor nào, ticket/reason gì và resource nào. “GET /users/123 200” trong HTTP log không đủ để chứng minh access hợp lệ.

Audit evidence cũng cần integrity và retention policy. Nếu principal bị nghi ngờ có thể tự sửa log của chính mình, log không còn là bằng chứng đáng tin.

## 11. Control chỉ có giá trị khi có bằng chứng rằng nó đang hoạt động

Ta có thể chia **điều khiển bảo mật (security control / 보안 통제)** thành ba lớp:

```text
preventive: chặn hành vi trước khi xảy ra
detective: phát hiện hành vi hoặc state bất thường
corrective: contain / revoke / recover sau phát hiện
```

Ví dụ credential ngắn hạn là preventive; alert về impossible travel hoặc anomalous role assumption là detective; revoke token family và rotate key là corrective.

Nhưng control được cấu hình không đồng nghĩa control hiệu quả. Cần **bằng chứng kiểm soát (control evidence / 통제 증거)**:

```text
policy exists
→ policy is enforced on real path
→ enforcement produces telemetry
→ telemetry reaches detector
→ detector is tested
→ response path can revoke/contain
```

Nếu admission policy tồn tại nhưng deployment path khác bypass nó, control chỉ tồn tại trên giấy. Nếu alert rule đúng nhưng telemetry pipeline chết khi incident xảy ra, detection coverage thấp hơn tưởng tượng.

## 12. Negative evidence phải được dùng cẩn thận

Không thấy alert không chứng minh không có attack. Điều đó chỉ có ý nghĩa nếu detector bao phủ attack path, telemetry còn tươi và pipeline đang hoạt động.

Mental model:

```text
no alert
+ detector coverage unknown
= almost no evidence

no alert
+ known coverage
+ healthy telemetry
+ tested detector
= stronger negative evidence
```

Nguyên tắc này giống production troubleshooting: sensor silence chỉ có ý nghĩa khi biết sensor đáng tin.

## 13. Ví dụ xuyên tầng — signed URL cho tài liệu nhạy cảm

Giả sử hệ thống cho phép user tải file riêng tư từ object storage.

Flow:

```text
browser
→ API authenticates session
→ API checks tenant + ownership
→ API asks storage service for signed URL
→ browser downloads directly from storage
```

Threat model:

```text
attacker steals URL
user role revoked after URL issuance
support account abuses download capability
storage service account compromised
URL accidentally enters logs/chat/history
```

Control chain:

```text
short TTL
+ resource-specific path
+ method restriction
+ tenant/ownership authorization at issuance
+ no secret query string in application logs
+ storage audit event
+ support privileged-access audit
+ revocation strategy for high-risk files
```

Quan trọng: authorization tại API chỉ kiểm tra thời điểm issuance. Nếu business invariant yêu cầu revoke gần như tức thời, signed URL dài 24 giờ vi phạm invariant dù endpoint API có authorization hoàn hảo. Control phải khớp temporal requirement.

## 14. Ví dụ xuyên tầng — CI runner tới production

Một pull request không đáng tin có thể sửa workflow. Nếu workflow chạy trên self-hosted runner có cloud credential production, attack path có thể là:

```text
untrusted code
→ CI execution
→ runner credential
→ registry / cloud API
→ production change
```

Threat model dẫn tới control:

```text
untrusted PR job
→ isolated ephemeral runner
→ no production credential
→ artifact built with provenance
→ separate trusted promotion identity
→ policy verifies artifact identity
→ production deploy emits audit event
```

Đây là ví dụ nơi secure supply chain, workload identity và audit evidence phải nối với nhau. Chỉ scan dependency không giải quyết quyền deploy.

## 15. Một template reasoning dùng lại được

Khi review một feature hoặc incident, có thể dùng chuỗi sau:

```text
1. Asset nào quan trọng?
2. Invariant nào phải luôn đúng?
3. Actor/capability nào có thể phá invariant?
4. Trust boundary nào nằm trên attack path?
5. Principal nào xuất hiện ở mỗi boundary?
6. Effective authority là gì?
7. Secret/data nào đi qua path?
8. Preventive control nào giữ invariant?
9. Telemetry/audit evidence nào chứng minh control hoạt động?
10. Detector nào phát hiện vi phạm?
11. Response nào contain/revoke/recover?
12. Residual risk nào còn lại?
```

Template này có thể áp dụng cho login, payment, admin console, CI/CD, data export, AI tool access hoặc multi-tenant platform mà không phụ thuộc vendor.

## 16. Ranh giới đơn vị sở hữu chuẩn gốc

Chapter này cố ý không giải thích lại cryptographic primitive, OAuth/OIDC internals, Linux isolation, Kubernetes RBAC syntax hoặc SIEM product. Các owner gần nhất là:

- [Computer Science Security](../07_security_reliability/README.md): threat model, cryptography, identity, vulnerabilities, reliability và secure operations.
- [Backend Core Auth](../../10_backend/backend_core/02_auth_session_identity.md): application/session/tenant/authorization semantics.
- [Linux](../../linux/README.md): process, identity, permissions, isolation và operational boundaries.
- [DevOps Security & Governance](../../devops_platform_engineering/08_security_governance/00_identity_secrets_policy_and_supply_chain.md): workload identity, secret rotation, policy, supply chain và platform guardrails.
- [DevOps Observability](../../devops_platform_engineering/07_observability_sre/00_observability_telemetry_and_evidence_driven_debugging.md): telemetry semantics và evidence quality.

> **Bàn giao:** Sau tuyến này, người đọc nên có khả năng đi từ một threat cụ thể đến control và evidence có thể kiểm tra. Khi cần áp dụng vào failure thực tế, đọc [case request → storage → queue → failure → recovery](../../devops_platform_engineering/10_production_practice/01_request_storage_queue_failure_and_recovery_case.md) để luyện cách nối state, identity, side effect và evidence xuyên nhiều boundary.