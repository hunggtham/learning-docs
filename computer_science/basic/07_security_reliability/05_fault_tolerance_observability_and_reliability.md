# Fault tolerance, observability và reliability

Một hệ thống đáng tin cậy (reliable system / 신뢰성 높은 시스템) không phải là hệ thống không bao giờ hỏng. Component, network, disk, process, dependency và con người đều có thể fail. Reliability engineering bắt đầu từ giả định đó rồi thiết kế để **failure được phát hiện, giới hạn phạm vi ảnh hưởng, phục hồi có thể dự đoán và vẫn giữ service trong mục tiêu đã định lượng**.

Điểm cốt lõi là reliability không phải một collection pattern như retry, circuit breaker hay multi-zone. Nó là reasoning về **failure model + invariant + resource capacity + recovery evidence**.

## 1. Fault, error và failure

Trong dependability, ba từ thường được tách như sau:

```text
fault
→ nguyên nhân bên dưới

error
→ internal state đã sai

failure
→ service bên ngoài lệch contract
```

Ví dụ một bit flip là fault. Nếu memory state bị corrupt thì đó là error. Nếu checksum phát hiện corruption và request bị retry từ replica khỏe, user có thể chưa thấy failure.

Phân biệt này quan trọng vì reliability engineering cố chặn propagation trước khi internal error trở thành user-visible failure.

## 2. Reliability invariant phải nói bằng ngôn ngữ của người dùng

Component health không phải mục tiêu cuối. Một service có thể có tất cả processes `UP` nhưng user vẫn timeout vì queue dài hoặc dependency chậm.

Invariant reliability nên được diễn đạt bằng kết quả quan sát được, ví dụ:

```text
99.9% request hợp lệ hoàn tất dưới 300 ms trong 30 ngày

payment đã trả success không được mất sau failover thuộc failure model

một tenant quá tải không được làm tenant khác mất toàn bộ capacity
```

Từ invariant đó mới chọn SLI, timeout, replication, bulkhead hay fallback phù hợp.

## 3. Redundancy chỉ hữu ích khi failure đủ độc lập

Replication, extra instances, RAID/erasure coding và multi-zone deployment tạo redundancy. Nhưng hai replicas cùng rack, cùng power source, cùng database hoặc cùng broken deployment artifact vẫn có thể fail cùng lúc.

Đây là **correlated failure**. Vì vậy phải hỏi:

```text
replicas có cùng failure domain không?
control plane có phải shared dependency không?
config/deploy bug có lan tới mọi replica không?
corruption có được replicate không?
```

“Có ba bản sao” không đồng nghĩa ba failure domains độc lập.

## 4. Retry là load multiplier

Retry có thể biến transient failure thành success, nhưng mỗi retry là một request mới. Nếu dependency chậm vì overload, retry làm arrival rate tăng đúng lúc service rate đang giảm.

Do đó retry cần:

```text
bounded attempts
exponential backoff
jitter
retry budget
idempotency khi có side effect
```

Timeout + retry mà operation không idempotent có thể duplicate payment/order. Retry policy vì vậy vừa là reliability design vừa là capacity design.

## 5. Timeout là budget, không phải magic number

Không có timeout, caller có thể giữ thread/connection vô hạn. Timeout quá ngắn tạo false failure và retry storm; quá dài giữ resource lâu và làm recovery chậm.

Timeout nên xuất phát từ end-to-end latency budget. Nếu request còn 80 ms nhưng downstream call được timeout 2 giây, system đã mất deadline invariant.

**Deadline propagation** truyền remaining budget xuống các hop thay vì mỗi layer tự reset một timeout đầy đủ.

## 6. Circuit breaker không tạo capacity

Circuit breaker tạm dừng gửi traffic tới dependency đang fail để giảm wasted work và cho dependency cơ hội hồi phục. Half-open probing kiểm tra recovery dần dần.

Nhưng circuit breaker không tự tăng capacity. Nếu failure do overload toàn hệ thống, vẫn cần bounded queue, admission control, backpressure hoặc load shedding.

Một breaker reopen đồng loạt trên nhiều instances còn có thể tạo spike mới nếu không có jitter/ramp-up.

## 7. Bulkhead là isolation boundary

Bulkhead tách resource pools hoặc quotas để một workload không ăn hết resource của workload khác.

Ví dụ background export dùng pool khác request user-facing. Trade-off là có thể lãng phí một phần capacity khi pool A rảnh nhưng pool B đầy.

Isolation chỉ có ý nghĩa nếu nó được đặt ở resource thật sự bottleneck. Hai logical queues khác nhau nhưng cùng tranh một exhausted DB pool vẫn không phải isolation đầy đủ.

## 8. Load shedding và graceful degradation

Khi system gần overload, cố nhận 100% requests có thể dẫn tới 100% timeout. Reject sớm một phần traffic đôi khi giữ phần còn lại khỏe hơn.

Graceful degradation có thể gồm stale cache, read-only mode, bỏ optional enrichment hoặc giảm chất lượng output. Nhưng degradation không được bỏ correctness/security invariant chỉ để giữ success rate.

Ví dụ phục vụ stale recommendation có thể chấp nhận được; phục vụ stale authorization policy có thể không chấp nhận được.

## 9. Observability là khả năng suy ra internal state từ evidence

Logs, metrics và traces là công cụ. **Observability (옵저버빌리티 / khả năng quan sát)** là khả năng dùng output/telemetry để suy ra điều gì đang xảy ra bên trong.

Các nhóm signal thường hữu ích:

```text
latency
traffic / rate
errors
saturation / queue
```

RED phù hợp service-oriented view: Rate, Errors, Duration. USE phù hợp resource view: Utilization, Saturation, Errors.

Điểm quan trọng là correlation: request chậm phải nối được với queue/pool/resource/dependency nào thay vì chỉ nhìn từng dashboard rời rạc.

## 10. SLI, SLO và SLA

**SLI (Service Level Indicator)** là chỉ số đo, ví dụ tỷ lệ request hợp lệ hoàn tất dưới 300 ms.

**SLO (Service Level Objective)** là mục tiêu nội bộ, ví dụ 99.9% trong rolling 30-day window.

**SLA (Service Level Agreement)** là cam kết business/external có consequence, không phải synonym của SLO.

SLO nên đo thứ user thực sự quan tâm, không chỉ component uptime.

## 11. Error budget biến reliability thành một trade-off định lượng

Nếu SLO là 99.9%, phần unreliability được phép trong window là **error budget**.

Ví dụ đơn giản:

```text
30 ngày × 24 giờ × 60 phút = 43,200 phút
0.1% budget ≈ 43.2 phút tương đương full outage
```

Thực tế budget có thể được tiêu bởi partial errors/latency chứ không chỉ full outage.

Error budget giúp trả lời câu hỏi: hiện tại team còn đủ margin để tăng deployment risk hay cần ưu tiên reliability work?

## 12. Burn rate cho biết budget đang bị tiêu nhanh đến mức nào

Nếu service chỉ mới đi qua 10% của window nhưng đã tiêu 50% error budget, tốc độ tiêu budget đang quá cao.

**Burn rate** so sánh tốc độ lỗi hiện tại với tốc độ lỗi cho phép để vừa hết budget đúng cuối window.

Mental model:

```text
burn rate = 1
→ đang tiêu budget đúng tốc độ cho phép

burn rate > 1
→ nếu kéo dài sẽ hết budget sớm
```

Alert theo burn rate thường tốt hơn alert chỉ theo error rate tức thời vì nó nối symptom với SLO impact.

## 13. Availability math và dependency graph

Nếu hai independent components bắt buộc đều available và mỗi cái có availability 99.9%, combined availability gần:

```text
0.999 × 0.999 = 0.998001 ≈ 99.8001%
```

Series dependencies làm availability tổng giảm. Parallel redundancy có thể tăng availability nếu failover thật sự hoạt động và failure đủ độc lập.

Vì vậy reliability architecture phải nhìn **dependency graph**, không nhìn từng component score riêng.

## 14. Correlated failure quan trọng hơn công thức độc lập

Availability multiplication chỉ đúng dưới assumptions phù hợp. Shared DNS, shared KMS, same deployment, same region hoặc same operator mistake làm failures correlated.

Một dependency “99.99%” nhưng nằm trên critical path của mọi request có thể quyết định toàn service. Một control plane hiếm dùng nhưng khi fail lại chặn certificate renewal cho toàn fleet cũng là reliability dependency.

## 15. Fault containment và blast radius

Reliability tốt không chỉ phục hồi nhanh mà còn ngăn failure lan rộng.

Các boundary thường dùng:

```text
zone / region
process / container
thread or worker pool
connection pool
queue
tenant quota
service ownership boundary
```

Blast radius cần được thiết kế trước incident. Nếu mọi workload dùng cùng pool/credential/control plane, một lỗi nhỏ có thể trở thành systemic failure.

## 16. Recovery phải có state model rõ

Sau failover/restart, câu hỏi không chỉ là “service đã lên chưa?”. Cần biết state nào authoritative, request nào đang in-flight, side effect nào đã xảy ra và retry có tạo duplicate không.

Reliability của stateful system vì thế nối trực tiếp với idempotency, transaction durability, replication và consistency.

## 17. Chaos/fault injection là kiểm thử hypothesis

Fault injection không phải “randomly phá production”. Một experiment tốt có:

```text
hypothesis rõ
blast-radius limit
abort condition
observability đủ
recovery expectation
```

Ví dụ: “mất một replica không làm p99 vượt X và không mất committed write”. Ta inject failure rồi kiểm tra invariant bằng evidence.

Chaos không có hypothesis hoặc telemetry chỉ là tạo incident có chủ đích mà không học được gì.

## 18. Production evidence

Reliability diagnosis nên nối nhiều tầng:

```text
SLI/SLO và burn rate
request error/latency percentiles
queue depth/wait
retry attempts
rejection/load shedding
resource saturation
failover/leader/replica state
dependency health
recovery timeline
```

Một component “healthy” nhưng queue debt tăng vẫn có thể đang tiến tới failure. Một outage đã hồi phục nhưng replica chưa catch up cũng chưa chắc reliability state đã bình thường.

## 19. Failure modes cần phân biệt

Các failure khác nhau cần mitigation khác nhau:

```text
transient network failure
→ retry có kiểm soát

overload
→ backpressure/admission/load shedding

correlated dependency failure
→ isolation/redundancy khác failure domain

bad deploy/config
→ staged rollout/rollback/roll-forward

state corruption
→ validation, backup/PITR, recovery
```

Dùng một pattern cho mọi failure thường làm hệ thống khó đoán hơn.

## 20. Mô hình tư duy

> Reliability = **định nghĩa user-visible objective, giả định failure sẽ xảy ra, giới hạn blast radius, giữ resource trong vùng an toàn, phát hiện deviation bằng evidence và phục hồi state theo contract có thể kiểm chứng.** Retry, redundancy hay circuit breaker chỉ là mechanisms phục vụ invariant đó.

## Kết nối

Đọc [Distributed partial failure](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [Idempotency](../08_software_systems/04_time_serialization_and_idempotency.md), [Performance/capacity](../08_software_systems/02_performance_capacity_and_scalability.md), [Advanced capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md), [Request path và retry overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) và [Debugging/containment xuyên tầng](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).