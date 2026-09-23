# 08. Observability và debugging

## Ba tín hiệu, một câu hỏi

- **Logs**: sự kiện có ngữ cảnh, request ID, actor/tenant đã redact.
- **Metrics**: xu hướng và tỷ lệ (rate, error, duration, saturation).
- **Traces**: quan hệ nhân quả giữa request và dependency spans.

Observability không phải bật thật nhiều log. Cần chọn signal phân biệt các giả
thuyết: latency tăng ở queue hay database, lỗi theo tenant hay toàn hệ thống,
chỉ timeout hay đã commit.

## Debugging loop

1. Viết symptom có mốc thời gian, scope và expected behavior.
2. Đặt vài giả thuyết có thể bác bỏ.
3. Tìm evidence từ trace, log, metric, DB state và deploy/change history.
4. Khoanh boundary đầu tiên nơi invariant bị phá.
5. Mitigate an toàn, rồi tạo reproduction và fix lâu dài.

Correlation ID cần truyền qua HTTP, job và message; trace context không nên bị
drop ở adapter. Metric label không được chứa user ID/card number vô hạn cardinality.
Log structured, có severity và sampling; redact secret trước khi serialize.

## Reliability signals

Theo dõi availability, latency percentile, error class, saturation, queue age,
DB pool và cache hit/stale. Dashboard phải nối symptom với owner và runbook;
alert một metric không có hành động thường tạo noise.

Khi incident, tách mitigation (rollback, rate limit, disable feature, drain
queue) khỏi root-cause fix. Ghi rõ điều gì đã biết, điều gì chưa biết và evidence
nào làm thay đổi quyết định.

Nền fault tolerance và observability sâu hơn nằm ở [Security & Reliability](../../computer_science/07_security_reliability/README.md).

## Đào sâu: từ telemetry đến causal graph

Telemetry có giá trị khi nối được nhân quả:

```text
deploy/config change
  → pool saturation / queue age
  → dependency latency
  → request timeout
  → retry / duplicate work
  → user-visible error
```

Trace span nên có operation name, peer, status, timeout/deadline và retry
attempt; không đưa payload nhạy cảm vào span. Log mỗi event một lần ở layer có
context tốt nhất, tránh log cùng exception ở mọi layer rồi làm sai tỷ lệ.

Label `user_id`, request ID hoặc raw URL có thể làm metric backend nổ
cardinality. Đưa chúng vào trace/log; metric dùng route template, status class và
bounded dimensions. Tail sampling nên giữ trace lỗi, latency cao và một mẫu
success để so sánh.

Mitigation production phải có rollback/expiry/audit: disable feature, giảm
traffic, pause consumer, tăng capacity hoặc chuyển read-only. Không sửa dữ liệu
trực tiếp chỉ để dashboard “xanh”.

## Bài tập suy luận

Một endpoint p99 tăng từ 200 ms lên 2 s nhưng error rate chưa tăng. Chọn ba
metric/span cần xem trước, phân biệt queueing với database latency, và nêu alert
nào nên kích hoạt trước khi người dùng gặp timeout.

## Health, SLO và privacy-safe telemetry

`liveness` trả lời process còn tiến triển không; `readiness` trả lời instance có
nên nhận traffic; `startup` dành cho initialization dài. Readiness không nên
check mọi dependency ở mỗi probe rồi tạo thundering herd. Khi drain, đánh dấu
not-ready trước, ngừng nhận work mới, hoàn tất hoặc trả lease work đang chạy,
rồi shutdown trong grace period có giới hạn.

SLO nên gắn với user-visible outcome: availability, latency theo route/class,
job completion hoặc freshness. Error budget dùng để quyết định release/rollback,
không phải chỉ là dashboard. Alert cần symptom, owner, window và hành động; alert
chỉ vì CPU cao có thể bỏ sót latency do lock hoặc dependency.

Telemetry phải có data classification. Không dùng raw email, token, cookie,
request body hay full query làm label/log mặc định. Dùng allowlist field, redaction
trước serialize, retention theo purpose và access audit cho log/traces.
