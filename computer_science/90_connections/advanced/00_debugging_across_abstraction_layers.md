# Debugging xuyên abstraction layers: từ symptom đến invariant và incident containment

Production bug thường xuất hiện ở layer A nhưng nguyên nhân nằm ở layer B hoặc interaction giữa nhiều layers. Advanced debugging vì vậy cần tránh hai cực: nhảy ngay xuống assembly/kernel, hoặc chỉ nhìn application log và giả định abstraction luôn giữ.

Mental model của chapter này là **contract-driven descent**: bắt đầu tại abstraction cao nhất còn giải thích được symptom, viết invariant đang bị vi phạm, thu evidence ở boundary, rồi chỉ đi xuống tầng dưới khi mechanism ở tầng hiện tại không đủ giải thích behavior.

## 1. Symptom không phải mechanism, mechanism chưa chắc là root condition

CPU 100% là symptom. Mechanism có thể là GC loop, regex pathological, spin lock, serialization hoặc legitimate compute. Root condition có thể là retry storm do downstream timeout.

Tương tự, `401`, TLS handshake failure hoặc “KMS timeout” đều là symptom. Root condition có thể là expired identity, policy rollout sai, clock skew, certificate chain lỗi, secret rotation không đồng bộ hoặc control plane unavailable.

Nếu chỉ sửa mechanism gần nhất—tăng CPU, restart pod, renew certificate bằng tay—incident có thể tái phát vì causal loop vẫn tồn tại.

## 2. Viết invariant trước khi mở thêm dashboard

Một investigation mạnh bắt đầu bằng câu có thể bị chứng minh sai, ví dụ:

```text
mỗi committed order chỉ bị charge một lần
reader thấy object chỉ sau safe publication
request chỉ được xử lý khi principal có quyền tương ứng
after COMMIT OK, transaction survive failure model đã công bố
queue không được giữ work đã quá deadline
service B chỉ chấp nhận workload identity thuộc trust domain X
```

Invariant giúp chọn evidence. Nếu không biết property nào phải đúng, rất dễ mở hàng chục graph nhưng không biết graph nào có ý nghĩa.

## 3. Boundary là nơi representation, authority hoặc ownership thay đổi

Ở mỗi boundary, hỏi:

```text
representation có đổi không?
queue/buffer có xuất hiện không?
ownership/lifetime đổi không?
retry/timeout có tạo duplicate không?
clock/order assumption có đổi không?
security principal hoặc authority có đổi không?
cache có thể stale không?
durability/consistency guarantee có đổi không?
```

Nhiều bug nằm ở transformation giữa hai components đều “đúng” khi xét riêng.

## 4. Evidence ladder: đi từ causal path tới lower-layer mechanism

Một investigation thường hiệu quả khi evidence được xếp theo câu hỏi:

```text
user-visible symptom là gì?
↓
request/transaction nào đại diện được symptom?
↓
timeline causal của request đó là gì?
↓
queue/wait/resource nào chiếm critical path?
↓
subsystem nào sở hữu resource đó?
↓
mechanism thấp hơn nào giải thích behavior?
```

Trace cho causal structure; metrics cho population/saturation; profiler/counters cho mechanism; logs cho event/context. Không tool nào một mình là “truth”.

## 5. Ví dụ: request chậm nhưng query nhanh

DB dashboard báo query 20 ms, API mất 2 s. Có thể 1.8 s nằm ở connection-pool wait trước khi query bắt đầu. Query tracing chỉ đo service time sau acquire nên bỏ qua queue delay.

Fix index không giải. Evidence cần pool utilization, acquire wait, transaction duration và caller concurrency. Lower abstraction quyết định behavior ở đây không phải query optimizer mà là admission boundary trước database.

## 6. Ví dụ: `write()` success nhưng data mất sau crash

Application thấy syscall return thành công, nhưng bytes có thể mới ở kernel page cache. Nếu requirement là survive power loss, abstraction “write succeeded” yếu hơn invariant business cần.

Đi xuống database WAL → syscall → filesystem → device flush semantics để xác định tầng nào thực sự cung cấp persistence. Xem [đường durability xuyên tầng](./03_durability_path_application_commit_wal_filesystem_device.md).

## 7. Ví dụ: concurrency bug chỉ lộ trên production hardware

Source code nhìn ordered, test trên một ISA pass nhưng production fail. Nếu program thiếu happens-before, test chỉ đang dựa vào accidental timing hoặc stronger ordering của một platform.

Đi xuống language memory model → compiler/runtime → ISA ordering → cache/coherence để giải thích behavior, nhưng fix phải quay lại tầng sở hữu invariant đồng bộ. Xem [đường correctness xuyên tầng](./02_correctness_path_language_os_cpu_memory_ordering.md).

## 8. Security path: identity → authorization → secret → TLS → service boundary

Một incident security/reliability thường đi qua chuỗi authority chứ không dừng ở một credential.

Ví dụ service A gọi service B:

```text
workload/process A
→ chứng minh identity
→ nhận certificate/token/credential
→ TLS hoặc mTLS bảo vệ channel và bind peer identity
→ B xác thực principal
→ authorization policy quyết định action
→ B dùng secret/KMS capability để truy cập resource C
→ audit trail ghi lại authority đã dùng
```

Invariant quan trọng là **identity không tự suy ra authorization**. “A là service hợp lệ” không có nghĩa A được phép đọc mọi dataset hoặc dùng mọi KMS key.

## 9. Secret là capability; nơi lưu secret không phải toàn bộ trust model

Một secret, token hoặc private key trao cho holder một capability. Nếu attacker lấy được credential có quyền decrypt mọi customer key, blast radius do authorization scope quyết định, không phải do encryption algorithm mạnh hay yếu.

Vì vậy khi debug credential compromise, đừng chỉ hỏi secret bị leak ở đâu. Hỏi thêm:

```text
credential có scope gì?
lifetime bao lâu?
service nào chấp nhận nó?
key/resource nào nó truy cập được?
log nào ghi lại use?
revoke ở boundary nào?
```

Đây là connection trực tiếp từ secret management sang incident containment.

## 10. TLS bảo vệ channel nhưng boundary phía sau vẫn cần policy

TLS/mTLS có thể chứng minh peer sở hữu credential cho identity đã được CA/trust domain cấp. Nó không tự quyết định business authorization.

Một service mesh bật mTLS toàn cluster nhưng policy `allow all authenticated workloads` vẫn có blast radius rất lớn nếu một workload bị compromise. Encryption in transit không thay least privilege.

Đọc [PKI, mTLS và service identity](../../07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md).

## 11. Incident containment là phá propagation path có chủ đích

Khi nghi compromise, response không chỉ là “đổi password”. Mục tiêu là cắt khả năng attacker tiếp tục đi qua trust graph.

Tùy incident, containment có thể cần:

```text
revoke/expire credential
narrow authorization policy
disable key version hoặc KMS grant
isolate workload/network boundary
rotate downstream secrets
block token/session family
stop deployment artifact hoặc supply-chain path
preserve forensic evidence
```

Thứ tự matters. Revoke secret nhưng để attacker mint secret mới qua compromised workload identity không giải quyết root authority.

## 12. Rotation và revocation là distributed state transition

Credential mới và cũ có thể cùng tồn tại trong overlap window. Cache, long-lived connection, token TTL và replica/config propagation làm policy không đổi atomically toàn hệ thống.

Invariant cần rõ: khi nào credential cũ không còn được chấp nhận? service nào đã nhận trust bundle mới? rollback có làm credential đã revoke sống lại không?

Security change vì vậy có cùng family với schema/protocol evolution: nhiều versions coexist và compatibility window phải được quản lý.

## 13. Security control cũng có failure mode reliability

Short-lived certificates giảm exposure window nhưng tăng dependency vào issuer/renewal path. KMS fail-closed bảo vệ key nhưng có thể gây outage. Online revocation check có thể tạo network dependency trên request critical path.

Không có nghĩa phải bỏ control. Nghĩa là design phải biết **security invariant nào không được hy sinh** và **availability degradation nào chấp nhận được** khi control plane fail.

## 14. Production evidence cho identity/security chain

Investigation cần nối application trace với security evidence:

```text
principal/workload identity
certificate serial / token issuer-audience-subject
policy decision và policy version
KMS/key id + operation
service boundary nguồn/đích
TLS/certificate validation error
credential issuance/rotation/revocation event
```

Không log raw secret/token. Mục tiêu là log identity và decision metadata đủ để reconstruct authority path mà không tạo thêm leakage.

## 15. Time là dependency security hay bị quên

Certificate validity, token expiry, nonce/replay window và log correlation đều phụ thuộc time. Clock skew có thể làm một credential hợp lệ bị reject hoặc credential đã hết hạn vẫn được một component hiểu sai nếu validation không nhất quán.

Khi nhiều services đồng loạt báo auth failure sau rollout/NTP incident, lower abstraction thực sự quyết định behavior có thể là clock discipline chứ không phải OAuth/TLS code.

## 16. Failure containment cần failure-domain reasoning

Nếu mọi services tin cùng một root credential cực mạnh, compromise root đó có blast radius toàn fleet. Nếu mỗi region/tenant/workload có authority boundaries phù hợp, incident có thể được khoanh vùng.

Đây là lý do least privilege, separate trust domains, scoped KMS grants và network/service boundaries đều là **containment architecture**, không chỉ compliance controls.

## 17. Retry có thể phá containment hoặc làm incident nặng hơn

Một service auth/KMS/TLS fail có thể bị caller retry hàng loạt. Nếu failure là policy deterministic, retry vô ích và chỉ tăng load lên issuer/KMS/proxy đang có incident.

Security errors cần được phân loại retryable hay non-retryable. `401/403`, certificate mismatch hoặc signature invalid thường không nên được đối xử giống timeout transient.

Điều này nối security trực tiếp với [retry → overload → backpressure](./01_end_to_end_latency_browser_edge_service_db_storage.md).

## 18. Abstraction nào thực sự quyết định behavior?

Khi symptom nằm ở tầng cao, hỏi contract nào bên dưới bị dependency:

```text
API timeout          -> queue/pool/network/runtime?
auth failure         -> identity, clock, trust chain hay policy?
data loss            -> WAL, filesystem, device hay replication ack rule?
concurrency bug       -> language model hay CPU ordering?
latency p99 spike     -> service time hay queue feedback loop?
```

Mục tiêu không phải luôn xuống tầng thấp nhất. Mục tiêu là xuống **đủ thấp để mechanism trở nên tất yếu**, rồi quay lại tầng sở hữu invariant để sửa.

## 19. Mô hình tư duy

> Debugging xuyên layers là contract-driven descent. Security incident containment cũng vậy: identity tạo principal, authorization giới hạn capability, secrets/keys mở quyền tới resource, TLS bảo vệ service boundary, còn containment cắt propagation path khi một boundary bị compromise. **Evidence phải reconstruct cả causal path của request lẫn authority path của principal.**

## Kết nối

Đọc cùng [leaky abstractions](../../basic/90_connections/04_abstraction_layers_and_leaky_abstractions.md), [PKI/mTLS](../../07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md), [Secret/KMS lifecycle](../../07_security_reliability/advanced/06_secrets_kms_hsm_rotation_and_envelope_encryption.md), [End-to-end request/overload](./01_end_to_end_latency_browser_edge_service_db_storage.md), [Correctness path](./02_correctness_path_language_os_cpu_memory_ordering.md) và [Durability path](./03_durability_path_application_commit_wal_filesystem_device.md).