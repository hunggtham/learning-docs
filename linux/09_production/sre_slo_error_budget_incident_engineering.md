# SRE, SLO, error budget và kỹ thuật xử lý sự cố

Linux cung cấp các chỉ số về CPU, memory, I/O, network và process. Nhưng production reliability không được quyết định chỉ bằng việc các chỉ số đó “trông đẹp”. Câu hỏi quan trọng hơn là: **người dùng đang nhận được mức dịch vụ nào, hệ thống có đáp ứng mục tiêu đã cam kết không, và khi có lỗi thì ta ưu tiên phục hồi hay điều tra như thế nào?**

Đây là vùng giao giữa Linux operations và **Site Reliability Engineering (SRE)**.

## Từ server health tới service reliability

Một server có CPU 20%, RAM còn nhiều và disk chưa đầy vẫn có thể phục vụ người dùng rất tệ nếu dependency timeout hoặc application error rate cao.

Ngược lại một server CPU 80% vẫn có thể hoàn toàn ổn nếu latency và error rate nằm trong mục tiêu.

Do đó:

```text
resource health ≠ user-visible reliability
```

Resource metrics là nguyên nhân tiềm năng hoặc tín hiệu hỗ trợ, không phải mục tiêu cuối cùng.

## SLI là gì?

**Chỉ số mức dịch vụ (Service Level Indicator - SLI)** là đại lượng đo trải nghiệm hoặc kết quả dịch vụ.

Ví dụ:

- tỷ lệ request thành công;
- p95/p99 latency;
- tỷ lệ job hoàn thành đúng thời gian;
- tỷ lệ dữ liệu được xử lý chính xác;
- availability từ góc nhìn người dùng.

SLI nên đo gần trải nghiệm thực tế nhất có thể.

## SLO là gì?

**Mục tiêu mức dịch vụ (Service Level Objective - SLO)** là mục tiêu cụ thể cho SLI trong một khoảng thời gian.

Ví dụ:

```text
99.9% request thành công trong 30 ngày
```

hoặc:

```text
99% request có latency < 300 ms trong 28 ngày
```

SLO là mục tiêu kỹ thuật/nội bộ để điều khiển quyết định reliability.

## SLA khác SLO

**Service Level Agreement (SLA)** thường là cam kết kinh doanh hoặc hợp đồng, có thể kèm penalty.

SLO thường là mục tiêu nội bộ nên chặt hơn SLA để có safety margin.

Không nên dùng hai thuật ngữ như đồng nghĩa.

## Error budget

Nếu SLO là 99.9%, phần còn lại là **ngân sách lỗi (error budget)**:

```text
100% - 99.9% = 0.1%
```

Trong 30 ngày:

```text
30 × 24 × 60 = 43,200 phút
0.1% ≈ 43.2 phút
```

Con số này chỉ là trực giác nếu SLI đo availability theo thời gian; với request-based SLI, budget tính trên số request xấu.

## Vì sao error budget hữu ích?

Reliability tuyệt đối 100% thường cực kỳ đắt và có thể làm tốc độ thay đổi chậm. Error budget tạo một ngôn ngữ chung:

```text
nếu budget còn nhiều
→ có thể chấp nhận nhiều thay đổi hơn

nếu budget gần cạn
→ ưu tiên reliability, giảm risky changes
```

Đây là cơ chế cân bằng tốc độ phát triển và độ ổn định.

## Good event và bad event

Với request-based availability:

```text
SLI = good requests / valid requests
```

Cần định nghĩa “good” cẩn thận. HTTP 200 chưa chắc là thành công nếu response sai nghiệp vụ. HTTP 500 có thể là lỗi rõ ràng, nhưng timeout ở load balancer cũng phải được tính dù backend không ghi log.

## Scope của denominator

Không phải request nào cũng nên vào denominator. Ví dụ traffic health check nội bộ có thể làm số liệu đẹp giả tạo nếu chiếm tỷ lệ lớn.

SLI phải phản ánh traffic có ý nghĩa với người dùng.

## Availability và latency

Service có thể trả response thành công nhưng quá chậm để hữu ích. Vì vậy thường cần nhiều SLI:

```text
availability SLI
latency SLI
correctness SLI
freshness SLI
```

Tùy sản phẩm.

## Percentile latency

Average latency thường che tail latency.

Ví dụ:

```text
90 request = 50 ms
9 request  = 500 ms
1 request  = 10 s
```

Average có thể vẫn nhìn chấp nhận được nhưng 1% người dùng trải nghiệm rất tệ.

Do đó p95/p99 thường quan trọng trong production.

## Percentile không cộng trực tiếp

Không nên lấy p99 của từng service rồi cộng để suy ra p99 end-to-end. Percentile không có tính cộng tuyến đơn giản như average.

Muốn hiểu request path, distributed tracing hoặc histogram đúng cách hữu ích hơn.

## Burn rate

**Burn rate** cho biết error budget đang bị tiêu nhanh gấp bao nhiêu tốc độ cho phép.

Nếu budget 30 ngày nhưng tốc độ lỗi hiện tại có thể làm cạn budget trong vài giờ, đó là burn rate rất cao.

Burn-rate alert thường tốt hơn alert trực tiếp “error rate > X” vì nó liên hệ lỗi với SLO.

## Multi-window alert

Một pattern phổ biến là kết hợp cửa sổ ngắn và dài:

```text
short window
→ phát hiện sự cố lớn nhanh

long window
→ tránh alert vì spike ngắn không đáng kể
```

Ví dụ một rule có thể yêu cầu burn rate cao ở cả 5 phút và 1 giờ trước khi page.

Mục tiêu là cân bằng detection speed với alert noise.

## Page, ticket và dashboard khác nhau

Không phải metric bất thường nào cũng cần đánh thức người trực.

Một phân loại hữu ích:

```text
page
→ cần hành động ngay để bảo vệ SLO/user

ticket
→ cần xử lý nhưng không khẩn cấp

dashboard
→ dùng quan sát/trend/capacity
```

Alert tốt phải gắn với hành động.

## Symptom-based alerting

Alert tốt thường bắt đầu từ triệu chứng người dùng:

- request failures;
- latency vượt SLO;
- queue không hoàn thành;
- dữ liệu stale.

Resource alerts như CPU cao hữu ích nhưng nên là supporting alert hoặc capacity signal nếu chưa gây impact.

## Cause-based alert vẫn có vai trò

Một số nguyên nhân cần alert trước khi user impact rõ ràng, ví dụ disk sắp đầy hoặc certificate sắp hết hạn.

Điểm quan trọng là phải biết alert thuộc loại **symptom** hay **cause** để đặt severity và response phù hợp.

## Incident là gì?

Incident là sự kiện production làm dịch vụ suy giảm đáng kể hoặc có nguy cơ cao vi phạm mục tiêu.

Không phải mọi lỗi log đều là incident.

Incident management cần ba dòng công việc song song:

```text
1. phục hồi dịch vụ
2. giao tiếp/trạng thái
3. thu thập bằng chứng và điều tra
```

## Incident commander

Trong sự cố lớn, nên có vai trò điều phối thay vì mọi kỹ sư cùng gõ lệnh không phối hợp.

**Incident commander** tập trung vào:

- ưu tiên hành động;
- phân công;
- quyết định rollback/failover;
- duy trì timeline;
- giảm xung đột thao tác.

Người hiểu sâu kỹ thuật nhất không nhất thiết phải là incident commander.

## Operational roles

Tùy tổ chức có thể tách:

- incident commander;
- operations lead;
- communications lead;
- subject-matter experts.

Trong team nhỏ, một người có thể kiêm nhiều vai trò.

## Timeline

Timeline chính xác cực kỳ quan trọng:

```text
14:02 deploy version A
14:05 latency tăng
14:07 alert firing
14:10 rollback bắt đầu
14:14 error rate phục hồi
```

Đối chiếu timeline với log/systemd/deploy history giúp tránh suy đoán bằng trí nhớ sau sự cố.

## Detection, acknowledgement, mitigation, recovery

Có thể tách thời gian incident:

```text
T0: failure bắt đầu
T1: phát hiện
T2: người vận hành nhận biết
T3: mitigation bắt đầu
T4: service phục hồi
```

Từ đó có các khoảng:

- time to detect;
- time to acknowledge;
- time to mitigate;
- time to recover.

Không nên gom tất cả thành một MTTR duy nhất nếu muốn cải tiến đúng chỗ.

## MTTR dễ bị hiểu sai

MTTR có thể được dùng cho mean time to repair/recover/resolve tùy tổ chức. Nếu không định nghĩa rõ, metric dễ gây hiểu nhầm.

Nên ưu tiên định nghĩa cụ thể từng timestamp và percentile của thời gian xử lý.

## Recovery trước, RCA sau

Khi user impact lớn, mục tiêu đầu tiên thường là giảm impact:

```text
rollback
failover
scale out
feature flag off
traffic shed
```

Không cần biết toàn bộ root cause trước khi thực hiện mitigation an toàn.

Nhưng phải thu thập evidence trước khi thao tác nếu có thể.

## Safe rollback

Rollback chỉ an toàn nếu state/data schema còn tương thích.

Nếu release mới đã chạy irreversible database migration, binary rollback có thể không đủ.

Do đó incident engineering liên kết trực tiếp với deployment design.

## Load shedding

Khi hệ thống overload, cố phục vụ mọi request có thể làm tất cả cùng timeout. **Load shedding** chủ động từ chối một phần traffic để bảo vệ core service.

Ví dụ:

```text
100% request → overload → 0% useful result
```

có thể tệ hơn:

```text
80% request accepted → healthy latency
20% rejected nhanh
```

Tùy business semantics.

## Graceful degradation

Một service có thể giữ chức năng chính nhưng tạm tắt chức năng phụ:

```text
recommendation unavailable
nhưng checkout vẫn hoạt động
```

Thiết kế degradation path trước incident tốt hơn phát minh trong lúc khẩn cấp.

## Retry storm

Retry không có backoff/jitter có thể biến lỗi nhỏ thành outage lớn:

```text
backend chậm
→ client timeout
→ tất cả retry ngay
→ backend tải cao hơn
→ chậm hơn
```

Đây là feedback loop dương nguy hiểm.

## Exponential backoff và jitter

Một retry policy tốt thường có:

- giới hạn số lần retry;
- exponential backoff;
- jitter;
- retry chỉ lỗi phù hợp;
- deadline tổng thể.

Retry phải nằm trong **timeout budget** end-to-end.

## Circuit breaker

Circuit breaker tạm ngừng gọi dependency khi failure rate cao, giúp giảm áp lực và fail fast.

Nhưng threshold/recovery sai có thể gây oscillation hoặc giữ service ở trạng thái mở quá lâu.

Đây là control system, không phải magic pattern.

## Bulkhead

**Bulkhead** tách resource pool để một dependency hoặc workload không làm cạn toàn bộ thread/connection của service.

Ví dụ:

```text
payment pool riêng
reporting pool riêng
```

Reporting chậm không làm payment hết thread.

## Queue và backpressure

Queue hấp thụ burst nhưng không tạo capacity. Nếu arrival rate trung bình > service rate, queue sẽ tăng tới giới hạn.

Do đó alert queue depth cần liên hệ với processing rate và age của item.

Một queue có 10,000 item nhưng xử lý 100,000/s có thể ổn; queue 100 item nhưng mỗi item chờ 30 phút có thể rất xấu.

## Saturation

Trong USE method:

```text
Utilization
Saturation
Errors
```

**Saturation** là lượng công việc đang chờ tài nguyên, ví dụ run queue hoặc I/O queue. Đây thường là dấu hiệu gần bottleneck hơn utilization đơn lẻ.

## RED method

Cho request-driven service:

```text
Rate
Errors
Duration
```

RED giúp nhìn service từ bên ngoài; USE giúp nhìn resource từ bên trong.

Hai phương pháp bổ sung nhau.

## Correlate SLI với Linux metrics

Ví dụ p99 latency tăng:

```text
SLI latency xấu
    ↓
kiểm tra RED
    ↓
request rate có tăng?
error có tăng?
    ↓
kiểm tra USE
    ↓
CPU saturation?
memory pressure?
I/O queue?
network retransmission?
```

Đây là cách nối business symptom với Linux evidence.

## Capacity headroom

Nếu service chỉ khỏe khi CPU < 70%, phần còn lại là headroom để hấp thụ burst/failure.

Capacity planning không nên tối ưu “average utilization cao nhất có thể”; cần đủ margin cho:

- node failure;
- traffic spike;
- deploy overlap;
- GC/compaction;
- retry burst.

## Failure domain

Không chỉ số lượng instance mà vị trí của chúng quan trọng.

```text
10 instance cùng một host
```

không có reliability giống:

```text
10 instance phân bố nhiều host/AZ
```

SLO cần xem xét failure domain thực tế.

## N+1 capacity

Nếu hệ thống cần chịu được mất một node, capacity còn lại sau khi mất node vẫn phải đáp ứng traffic mục tiêu.

Nếu 4 node mỗi node chạy 25% load, mất một node làm ba node còn lại khoảng 33%. Nếu bình thường mỗi node đã 80%, mất một node có thể gây cascade overload.

## Cascading failure

Một dependency chậm có thể giữ thread upstream, làm pool cạn, khiến request mới timeout, gây retry và lan ra nhiều service.

Cascading failure thường là chuỗi resource coupling, không chỉ một component lỗi.

## Postmortem

Sau incident đáng kể, postmortem nên ghi:

```text
impact
summary
trigger
contributing factors
timeline
detection
response
what went well
what went poorly
action items
```

Mục tiêu là cải thiện hệ thống, không tìm người để đổ lỗi.

## Root cause không luôn là một nguyên nhân

Hệ thống phức tạp thường có:

```text
trigger
+
latent condition
+
missing guardrail
+
weak detection
```

Ví dụ deploy bug là trigger, nhưng thiếu canary và rollback khó mới biến nó thành outage dài.

Do đó postmortem tốt phân tích **contributing factors** thay vì cố ép mọi thứ về một “root cause duy nhất”.

## Action item tốt

Action item nên cụ thể, có owner và tiêu chí hoàn thành.

Yếu:

```text
cẩn thận hơn khi deploy
```

Tốt hơn:

```text
thêm automated smoke test kiểm tra endpoint X trước khi chuyển 100% traffic
```

Hệ thống hóa tốt hơn nhắc nhở con người.

## Toil

Trong SRE, **toil** là công việc vận hành thủ công, lặp lại, có tính tactical và tăng theo quy mô dịch vụ.

Ví dụ:

- SSH vào từng server để restart định kỳ;
- sửa log rotation bằng tay;
- copy certificate thủ công mỗi tháng.

Automation nên giảm toil, nhưng automation kém có thể tăng blast radius. Vì vậy cần idempotency, validation và rollback.

## Runbook

Runbook tốt không chỉ là danh sách command. Nó cần:

```text
symptom
preconditions
safety checks
diagnostic decision points
mitigation
verification
rollback/escalation
```

Runbook càng gần causal model càng hữu ích khi stress cao.

## Game day và chaos testing

Không nên đợi incident thật mới biết failover không hoạt động. Game day mô phỏng failure có kiểm soát để kiểm tra:

- alert;
- runbook;
- communication;
- backup/restore;
- capacity khi mất node.

Chaos engineering là phiên bản có hệ thống hơn của tư duy thử failure hypothesis.

## Backup không có restore test không phải guarantee

Một backup job “success” chỉ chứng minh job đã tạo output theo cách nào đó. Reliability yêu cầu định kỳ restore và verify application/data consistency.

Điều này liên kết SRE với disaster recovery.

## Change failure rate

Một hệ thống có thể theo dõi tỷ lệ deploy gây incident/rollback. Đây là một signal về quality của delivery pipeline.

Nhưng metric không nên biến thành mục tiêu thưởng-phạt máy móc; nếu team sợ ghi nhận incident để giữ số đẹp, metric đã phản tác dụng.

## Mô hình tư duy

SRE nối ba tầng:

```text
user-visible objective
        ↓
service behavior
        ↓
Linux/runtime/resource evidence
```

Linux metrics trả lời **vì sao** service có thể xấu. SLO trả lời **mức xấu nào thực sự quan trọng**.

## Những hiểu lầm phổ biến

**“CPU dưới 80% nghĩa hệ thống khỏe.”** User-visible SLI có thể đang vi phạm.

**“SLO 99.9% nghĩa mỗi tháng được phép downtime 43 phút.”** Chỉ đúng với cách đo availability theo thời gian cụ thể; request-based SLI có semantics khác.

**“Mọi alert phải page.”** Page chỉ nên dành cho sự kiện cần hành động khẩn cấp.

**“Postmortem là tìm người gây lỗi.”** Mục tiêu là tìm điều kiện hệ thống cho phép incident xảy ra và kéo dài.

**“Retry làm hệ thống đáng tin cậy hơn.”** Retry không kiểm soát có thể gây retry storm.

**“Queue giải quyết overload.”** Queue chỉ trì hoãn công việc nếu arrival rate vượt service rate lâu dài.

**“Backup thành công nghĩa DR sẵn sàng.”** Chỉ restore test mới kiểm tra khả năng phục hồi thực tế.

## Kết nối kiến thức

Chương này nên được đọc sau [capacity planning](./capacity_planning_server_sizing.md), [production troubleshooting](./production_troubleshooting.md), [deployment/rollback](../08_operations/deployment_release_rollback.md) và [backup/DR](../08_operations/backup_restore_disaster_recovery.md). Nó cung cấp lớp ra quyết định ở trên các metric Linux: khi nào cần page, khi nào rollback, cách định nghĩa reliability và cách biến incident thành cải tiến hệ thống.