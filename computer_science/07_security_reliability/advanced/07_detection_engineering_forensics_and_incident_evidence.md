# Detection engineering, forensics và incident evidence

Đọc trước [Security boundaries, attack chains và exploitability](./00_security_boundaries_attack_chains_and_exploitability.md). Chapter này bắt đầu từ một giới hạn căn bản: **preventive control không thể được giả định là hoàn hảo**. Authentication có thể bị bypass, credential có thể bị lộ, policy có thể cấu hình sai, dependency có thể fail-open, và một hành vi hợp lệ riêng lẻ có thể trở nên nguy hiểm khi ghép thành attack chain.

Vì vậy security production cần một đường reasoning khác:

```text
security invariant
→ telemetry về state/action
→ detection hypothesis
→ signal / correlation
→ triage
→ investigation
→ containment
→ recovery
→ learning / control improvement
```

Mục tiêu không phải “log thật nhiều”. Mục tiêu là giữ đủ evidence để phân biệt hypothesis và tái dựng authority path khi invariant bị vi phạm.

## 1. Detection bắt đầu từ invariant, không bắt đầu từ SIEM rule

Một detection rule chỉ có ý nghĩa khi ta biết nó đang bảo vệ điều gì. Ví dụ invariant có thể là:

```text
chỉ workload X được phép dùng key Y
một user không thể approve chính request do mình tạo
service A không được gọi admin endpoint của service B
```

Từ invariant đó mới suy ra event nào cần quan sát: principal, resource, action, policy decision, credential/key ID, source context, result và timestamp.

Nếu bắt đầu bằng “hãy collect tất cả logs”, hệ thống dễ tạo noise và cost nhưng không tăng khả năng reasoning.

## 2. Telemetry không phải sự thật tuyệt đối

Log là một observation được tạo bởi component cụ thể. Nếu component bị compromise, disabled hoặc overloaded, telemetry có thể thiếu hoặc sai.

Vì vậy evidence strength phụ thuộc trust boundary:

```text
application self-log
< independent gateway / identity-provider evidence
< tamper-resistant audit pipeline
```

Thứ tự này không phải universal ranking, nhưng nhắc rằng nguồn evidence và threat model phải được xét cùng nhau.

## 3. Event schema phải giữ identity và causality

Một event security hữu ích thường cần ít nhất:

```text
who: principal / workload / user / service identity
what: action
which: resource / object / tenant
why: policy / grant / role / token audience-scope
when: timestamp + ordering context
where: host / region / network / process / session
result: success / deny / error
correlation: request / trace / session / transaction id
```

Thiếu identity hoặc object scope khiến incident responder chỉ biết “API admin đã được gọi” nhưng không biết ai có authority tại thời điểm đó.

## 4. Base-rate problem làm alert hiếm rất khó

Giả sử detector có độ chính xác tưởng như rất tốt nhưng attack thực sự cực hiếm. Số false positive vẫn có thể lớn hơn true positive rất nhiều.

Đây là base-rate problem. Vì vậy detection engineering phải cân precision/recall theo prior probability và analyst capacity, không chỉ nhìn một metric classifier.

Alert fatigue là failure mode của system design, không chỉ là vấn đề con người “không tập trung”.

## 5. Correlation tạo context nhưng cũng có failure modes

Một login lạ chưa chắc là attack. Một privilege change riêng lẻ có thể hợp lệ. Nhưng chuỗi:

```text
new device login
→ privilege grant
→ secret read
→ unusual outbound transfer
```

có evidential value mạnh hơn.

Correlation có thể theo identity, host, resource, trace, temporal window hoặc graph relationship. Tuy nhiên window quá rộng tăng false positives; quá hẹp bỏ sót slow attack. Entity resolution sai có thể ghép nhầm hai users/services.

## 6. Detection là hypothesis test, không phải verdict

Một alert nên được đọc như:

> “Evidence hiện tại làm hypothesis X đáng điều tra hơn baseline.”

Không nên biến detector score thành sự thật tuyệt đối. Triage cần tìm disconfirming evidence, business context và known-change context.

Mental model gần với debugging:

```text
symptom
→ competing hypotheses
→ discriminating evidence
→ containment decision
```

## 7. Time là một phần của forensic correctness

Cross-system investigation phụ thuộc clocks. Nếu hosts lệch thời gian, cùng attack chain có thể trông đảo thứ tự.

Wall-clock timestamp nên đi cùng monotonic/sequence/correlation evidence khi có thể. Distributed-system clock uncertainty trong [time, clocks và causality](../../06_networks_distributed_systems/advanced/06_time_clocks_ordering_and_causality.md) áp dụng trực tiếp cho incident reconstruction.

Không nên suy luận causal order chỉ từ hai timestamps gần nhau khi uncertainty lớn hơn khoảng cách giữa chúng.

## 8. Immutable/tamper-evident audit log bảo vệ evidence path

Nếu attacker có cùng quyền sửa application state và xóa audit logs, forensic confidence giảm mạnh.

Audit architecture thường cố gắng tách quyền:

```text
producer can append event
producer cannot silently rewrite history
retention store has separate authority
access to evidence is itself audited
```

Cơ chế cụ thể có thể là append-only storage, WORM retention, signed batches hoặc restricted logging account. Mental model là **evidence authority phải độc lập hơn control plane đang bị điều tra**.

## 9. Chain of custody quan trọng khi evidence có hậu quả pháp lý hoặc compliance

Trong nhiều incident nội bộ, engineering chỉ cần đủ evidence để fix system. Nhưng khi evidence được dùng cho audit/pháp lý, cần provenance rõ: ai thu thập, tool/version nào, hash/integrity nào, thời điểm nào và bản gốc ở đâu.

Copy file log không kèm provenance có thể hữu ích kỹ thuật nhưng yếu hơn cho formal investigation.

## 10. Ephemeral infrastructure làm forensic window ngắn hơn

Container/pod/serverless instance có thể biến mất sau vài phút. Nếu chỉ giữ evidence trên local disk, autoscaling/restart có thể xóa context trước khi responder biết incident xảy ra.

Do đó telemetry pipeline phải cân:

```text
ephemeral lifetime
vs
export latency
vs
retention cost
```

Critical identity/policy/audit events thường cần ship ra ngoài failure domain sớm hơn debug logs thông thường.

## 11. Memory và process state đôi khi quan trọng hơn disk logs

Credential theft, injected code hoặc in-memory malware có thể không để lại artifact rõ trên filesystem. Process tree, open connections, loaded modules, memory mappings và runtime state có thể là evidence.

Tuy nhiên collection có overhead và privacy impact. Không có invariant “capture everything”. Điều cần thiết là forensic readiness phù hợp threat model.

## 12. Network evidence nói được path, không luôn nói được intent

Flow logs, connection metadata, DNS logs và proxy logs có thể cho biết ai nói chuyện với ai, volume, timing và route. Payload encrypted có thể không quan sát được nội dung.

Một outbound connection lớn không tự chứng minh exfiltration. Nó cần context về principal, dataset, destination trust và business behavior.

## 13. Identity evidence thường là trục chính của cloud/service incident

Trong distributed systems hiện đại, “host nào bị hack?” thường không đủ. Authority có thể đi qua workload identity, token exchange, role assumption, service account hoặc delegated OAuth scope.

Investigation nên dựng graph:

```text
credential source
→ principal
→ granted role/policy
→ resource access
→ downstream capability
→ impact
```

Đây là continuation của authority graph trong chapter security boundaries.

## 14. Secret rotation là một forensic state transition

Khi credential bị nghi compromise, rotation/revocation không phải chỉ thay secret string. Cần biết token/session/cache nào còn sống, service nào chưa reload, replica nào chưa nhận policy mới và old credential được chấp nhận đến khi nào.

Containment timeline phải đo **effective revocation**, không chỉ thời điểm operator bấm “rotate”. Đọc thêm [KMS, HSM, rotation và envelope encryption](./06_secrets_kms_hsm_rotation_and_envelope_encryption.md).

## 15. False negative thường đến từ missing telemetry hoặc attacker adaptation

Detector có thể bỏ sót vì event không được emit, parser fail, clock lệch, sampling quá mạnh, attacker dùng legitimate admin API hoặc hành vi thấp-chậm dưới threshold.

Vì vậy “không có alert” không chứng minh không có compromise.

Detection coverage nên được test bằng simulated benign/malicious scenarios theo invariant, giống test architecture chứ không chỉ review rule syntax.

## 16. Adversarial pressure thay đổi economics của observability

Attacker có thể cố tạo log flood để che signal hoặc làm pipeline quá tải. Một hệ thống logging không bounded có thể tự trở thành availability risk.

Cần rate limit, backpressure, priority classes và degradation policy. Security-critical audit event có thể cần guarantee khác debug event.

Connection này nối trực tiếp với [queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

## 17. Detection pipeline cũng có data-quality invariant

Nếu parser/schema evolution làm field `principal_id` biến mất ở 20% events, detector có thể silently mất coverage.

Do đó cần monitor:

```text
expected event rate
schema validity
field completeness
source freshness
pipeline lag
parse/drop rate
```

Security detection không thể tin pipeline mà không quan sát chính pipeline.

## 18. Incident containment cần cắt capability, không chỉ kill process

Kill compromised process có thể không đủ nếu token còn valid, role vẫn granted hoặc persistence mechanism còn tồn tại.

Containment phải xác định capability graph và cắt những edge quan trọng: revoke credential, disable principal, isolate workload, deny network path, freeze risky automation hoặc rotate keys.

Blast radius được giảm khi authority boundaries nhỏ từ trước.

## 19. Recovery cần chứng minh invariant được phục hồi

“Service đã lên lại” không đồng nghĩa incident kết thúc. Recovery cần xác minh:

```text
unauthorized capability đã bị loại bỏ
credentials/policies đã ở state mới
compromised data/state đã được xử lý
telemetry coverage đã phục hồi
backlog/retry không tái kích hoạt hành vi cũ
```

Đây là điểm Security giao với Reliability.

## 20. Incident learning không nên dừng ở “human error”

Nếu một operator có thể vô tình cấp quyền quá rộng mà không guardrail, system design đã cho phép failure đó.

Post-incident learning nên hỏi assumption nào sai, control nào thiếu, evidence nào khó lấy, detection nào chậm và containment nào quá blast radius.

Kết quả có thể là policy-as-code, approval separation, safer default, better audit event hoặc runbook; không phải chỉ thêm alert.

## 21. Privacy và retention là constraint thật

Security telemetry thường chứa user identifiers, IP, resource names hoặc request metadata. Retain vô hạn để “forensic cho chắc” có privacy/compliance/cost risk.

Cần data minimization, access control, retention tier và purpose limitation. Evidence hữu ích không đồng nghĩa thu mọi payload nhạy cảm.

## 22. Worked example: service account bị dùng sai scope

Giả sử service account của batch job bình thường chỉ đọc bucket A. Một misconfiguration cấp thêm quyền đọc bucket B chứa dữ liệu nhạy cảm. Sau đó workload bắt đầu đọc B với volume bất thường.

Một detector tốt không chỉ trigger “bytes tăng”. Nó correlate:

```text
policy change
→ effective principal capability
→ first access to bucket B
→ data-read volume
→ outbound destination / downstream action
```

Investigation cần biết change nào cấp authority, ai approve, token nào dùng, resource nào đọc và containment nào thu hồi capability. Nếu chỉ có application access log không có policy-history evidence, root cause sẽ mơ hồ.

## 23. Production evidence checklist theo reasoning path

Khi điều tra, ưu tiên dựng timeline và graph thay vì dump tất cả logs. Evidence hữu ích gồm identity/token metadata không chứa secret raw, policy version/decision, resource/object ID, process/workload identity, network peer, request/trace/session correlation, deployment version, clock uncertainty, audit-integrity status và containment actions.

Mục tiêu là trả lời được: **ai có authority gì, authority đó đến từ đâu, được dùng khi nào, đã tạo impact nào, và khi nào authority thực sự bị cắt**.

## 24. Kết nối sang các chapter khác

Detection/forensics nối với [security boundaries](./00_security_boundaries_attack_chains_and_exploitability.md), [OAuth/OIDC token lifecycle](./03_oauth_oidc_token_lifecycle_and_federation_threats.md), [secrets/KMS rotation](./06_secrets_kms_hsm_rotation_and_envelope_encryption.md), [test architecture và production verification](../../09_software_engineering/advanced/04_test_architecture_contract_mutation_property_and_production_verification.md) và [debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

Mental model cuối cùng: **security evidence là một distributed state/history problem. Detection chỉ mạnh khi identity, authority, time, provenance và pipeline reliability đều đủ để kiểm chứng hypothesis.**