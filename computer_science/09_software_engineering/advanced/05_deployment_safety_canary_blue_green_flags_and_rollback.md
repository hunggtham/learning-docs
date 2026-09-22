# Deployment safety: canary, blue-green, feature flags và rollback limits

Deploy không chỉ là copy artifact. Nó thay đổi một running socio-technical system có traffic, persistent data, caches, queues và dependencies đang ở nhiều versions. Deployment strategy tốt giữ một invariant quan trọng: **mỗi bước rollout phải giới hạn blast radius, giữ compatibility trong coexistence window và tạo đủ evidence để quyết định tiếp tục, dừng, rollback hay roll-forward.**

## 1. Deployment là một distributed state transition

Khi fleet có 100 instances, rollout hiếm khi đổi từ version N sang N+1 atomically. Trong nhiều phút hoặc lâu hơn, hệ thống ở trạng thái mixed-version:

```text
clients cũ + mới
servers N + N+1
schema cũ + expanded schema
events/messages của nhiều versions
cache entries cũ
background jobs cũ
```

Correctness phải giữ trong **transition state**, không chỉ ở trạng thái cuối.

## 2. Compatibility là invariant đầu tiên của rolling deployment

Old/new versions coexist nên protocol/schema cần hỗ trợ overlap window. Nếu N+1 ghi data mà N không đọc được, rolling deploy hoặc rollback có thể fail dù từng version riêng lẻ test pass.

Cần reasoning cả hai hướng khi cần:

```text
new reader đọc old data?
old reader đọc new data?
new writer tạo format old consumer có chịu được?
message/event consumer lag có kéo version cũ tồn tại lâu hơn dự kiến?
```

Compatibility boundary có thể là API, DB schema, event schema, cache encoding hoặc shared file format.

## 3. Rolling deployment giữ capacity nhưng làm state space lớn hơn

Thay instances dần giúp service tiếp tục phục vụ và giảm blast radius, nhưng mixed-version state tăng complexity.

Nếu readiness sai, deployment controller có thể đưa instance chưa warm vào traffic. Nếu terminate quá nhanh, in-flight work bị cắt. Nếu rollout đồng thời quá nhiều nodes, remaining capacity có thể đi qua utilization knee.

Deployment policy vì thế liên quan trực tiếp capacity engineering.

## 4. Blue-green giảm traffic-switch cost nhưng không tách state tự động

Blue-green duy trì hai environments và chuyển traffic. Binary rollback routing có thể rất nhanh nếu state/protocol tương thích.

Nhưng database, message broker, third-party side effects thường vẫn shared. Nếu green đã chạy destructive migration hoặc phát external side effect, chuyển traffic về blue không đưa world quay lại trạng thái trước.

“Blue-green rollback” chỉ mạnh tới boundary state mà hai environments thực sự tách được.

## 5. Canary là experiment dưới traffic thật

Canary gửi một phần traffic tới version mới rồi đo error, latency, saturation và business invariants.

Canary giảm blast radius nhưng chỉ có giá trị nếu traffic sample chạm failure mode cần phát hiện. 1% random traffic có thể bỏ sót rare workflow, large tenant, specific region hoặc high-cost request class.

Canary design nên chọn cohort theo risk, không chỉ percentage.

## 6. Guardrail phải gắn với invariant, không chỉ CPU/error rate

Một release có thể trả HTTP 200 nhưng phá business state. Guardrail tốt có thể gồm:

```text
error/latency SLO burn
resource saturation
queue/DB wait
business invariant violations
payment duplicate/reconciliation mismatch
authorization-denied anomaly
schema compatibility errors
```

Metric noisy hoặc label cardinality sai có thể làm auto rollback giả. Guardrail cần threshold, window và baseline hợp lý.

## 7. Feature flag tách code deployment khỏi feature exposure

Flag cho phép deploy dormant code rồi bật dần theo cohort.

Nhưng mỗi flag tạo thêm state dimension. N flags có thể tạo nhiều combinations khó test. Flag lâu ngày trở thành permanent branching complexity.

Flag cần owner, purpose, expiry/cleanup condition và safe default. Security-critical control không nên biến thành “flag có thể vô tình off” nếu invariant yêu cầu luôn enforce.

## 8. Rollback không phải time machine

Binary rollback không undo:

```text
DB migration đã mất data
message/event đã publish
email đã gửi
money đã movement
external API side effect
cache/state đã đổi format
```

Do đó cần tách **reversible code state** khỏi **irreversible world state**.

Nhiều incident an toàn hơn khi roll-forward bằng compatibility fix thay vì cố chạy old binary trên state mới.

## 9. Database migration là phần deployment khó đảo nhất

Expand-contract pattern:

```text
1. add compatible structure
2. deploy code hiểu old + new
3. backfill/throttle
4. switch reads/writes
5. verify
6. remove old structure sau safe window
```

Destructive drop/rename sớm phá rollback và mixed-version fleet.

Backfill cũng là workload production. Nó có thể saturate DB/storage và làm user traffic chậm, nên migration cần rate limit và observability.

## 10. Queue/event làm coexistence window dài hơn rollout window

Dù toàn fleet đã lên N+1, queue có thể còn message được producer N tạo từ trước. Consumer phải hỗ trợ format cũ tới khi backlog drain hoặc retention window hết.

Do đó protocol deprecation cần dựa **data/message lifetime**, không chỉ “deployment đã hoàn tất”.

Đây là reason schema evolution là distributed protocol theo thời gian.

## 11. Readiness, liveness và health là control-loop inputs

Process start không nghĩa ready nhận traffic. Readiness nên phản ánh local ability phục vụ request cần thiết.

Nhưng nếu readiness phụ thuộc mọi downstream service, một dependency incident có thể làm toàn fleet tự rút khỏi load balancer, tạo outage lớn hơn.

Health signal phải được thiết kế theo recovery action tương ứng:

```text
restart process giải được không?
rút khỏi traffic có giảm blast radius không?
dependency failure là local hay shared?
```

Health check sai là feedback controller sai.

## 12. Connection draining giữ in-flight invariant

Khi instance bị terminate/rút traffic, existing requests/connections cần thời gian hoàn tất hoặc cancellation semantics rõ.

HTTP/2, WebSocket, long polling hoặc background task có lifetime dài hơn request đơn giản. Drain timeout quá ngắn làm user-visible errors; quá dài làm rollout chậm và giữ old version lâu.

Deployment controller phải hiểu connection/work lifecycle thực tế.

## 13. Cache warm-up và cold-start là phase khác steady state

New instance có empty local cache, cold JIT, unloaded code/data pages và empty connection pools. Canary latency ban đầu có thể xấu vì warm-up, hoặc ngược lại canary nhẹ load nên trông tốt hơn full rollout.

Rollout evidence cần phân biệt warm-up effect với regression thật.

Một deployment có thể pass canary nhưng fail ở 50% traffic khi shared DB/cache pressure tăng phi tuyến.

## 14. Capacity headroom là điều kiện deployment safety

Rolling update làm một phần capacity unavailable. Nếu steady state đã chạy gần utilization knee, rollout itself có thể tạo overload.

Safe deploy cần headroom cho:

```text
instances terminating/startup
warm-up
canary duplication/shadow traffic
schema backfill
cache cold miss
rollback overlap
```

Deployment và capacity planning không thể tách rời.

## 15. Failure mode: retry storm trong rollout

Nếu new version chậm, client/proxy retry có thể tăng load lên cả old và new fleet. Auto rollback cũng tạo connection churn/cold cache, làm recovery khó hơn.

Guardrail cần nhìn attempt/retry rate và queue depth, không chỉ error rate. Rollback action bản thân cũng là một load event cần capacity.

## 16. Security rollout cũng có compatibility window

Certificate/trust bundle, authorization policy, signing key hoặc token issuer rotation đều là deployment-like distributed state changes.

Publish verifier trust trước khi issuer chuyển key thường an toàn hơn đổi issuer trước rồi hy vọng consumers update kịp.

Security config nên có canary/audit/rollback discipline tương tự code, nhưng không được rollback theo cách resurrect credential đã revoke vì compromise.

## 17. Production evidence trước khi tăng rollout

Một promotion decision nên dựa trên cohort-aware evidence:

```text
request success/error by version
latency percentiles by version/workload class
CPU/memory/GC/queue saturation
DB pool/lock/I/O waits
retry/timeout rate
business invariant checks
schema/protocol decode errors
log/trace anomalies
```

So sánh canary với control cùng traffic/time window tốt hơn nhìn metric tuyệt đối đơn lẻ.

## 18. Deployment incident timeline phải giữ version identity

Trace/log/metric cần biết instance/version/build/config/flag state. Nếu không, mixed-version incident khó reconstruct.

Useful metadata:

```text
artifact digest/version
schema/config version
feature flags relevant
deployment wave/cohort
instance/zone/region
```

Observability không version-aware sẽ biến deployment regression thành “random errors across fleet”.

## 19. Reversibility phải được test, không chỉ viết trong runbook

Rollback path có thể thối theo thời gian. Test cần bao gồm:

```text
deploy N+1 → rollback N
mixed-version traffic
schema expanded nhưng code cũ chạy lại
queue còn old/new messages
failure giữa migration steps
```

Nếu rollback chưa được test với production-like state, nó là hypothesis chứ chưa phải capability.

## 20. Mô hình tư duy

> Safe deployment là **controlled exposure dưới uncertainty**. Rolling/canary/blue-green/flags chỉ là mechanisms. Invariant thật là compatibility trong transition, bounded blast radius, sufficient capacity và evidence để quyết định bước tiếp theo. Rollback chỉ tồn tại trong phạm vi code/data/protocol còn reversible; ngoài phạm vi đó phải thiết kế roll-forward và reconciliation.

## Kết nối

Đọc cùng [Architecture decisions/System Design](./00_architecture_decisions_evolution_and_socio_technical_constraints.md), [Schema/protocol evolution](../../08_software_systems/advanced/06_schema_protocol_evolution_and_compatibility_contracts.md), [Capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md) và [Security identity rotation](../../07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md).