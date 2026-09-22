# Observability: từ telemetry đến suy luận có bằng chứng

## 1. Monitoring và observability không hoàn toàn giống nhau

Monitoring thường trả lời các câu hỏi đã biết trước: CPU có cao không, error rate có vượt ngưỡng không. Khả năng quan sát (observability / 관측 가능성) rộng hơn: từ dữ liệu hệ thống phát ra, ta có thể đặt câu hỏi mới khi failure chưa từng biết trước.

Observability không được đo bằng số dashboard. Một hệ thống có hàng nghìn metric nhưng thiếu correlation giữa request, deployment và dependency vẫn khó debug.

## 2. Telemetry là evidence, không phải sự thật trọn vẹn

Metrics, logs, traces và events đều là phép quan sát có bias. Metric aggregate làm mất detail. Log có thể thiếu context. Trace có sampling. Event có thể bị drop. Vì vậy khi hai nguồn mâu thuẫn, không nên chọn nguồn “quen dùng”; phải hiểu semantics thu thập.

Một metric CPU 40% trung bình node không phủ định việc một container bị CPU throttling. Average latency 100 ms không phủ định p99 là 3 giây. Telemetry luôn cần dimensions và distribution phù hợp.

## 3. Metrics dùng cho trend và alert

Metric phù hợp để theo dõi quantity theo thời gian. Counter tăng đơn điệu cho event count; gauge biểu diễn value hiện tại; histogram/distribution giữ phân bố latency/size tốt hơn chỉ average.

Cardinality là trade-off quan trọng. Label như `status_code`, `region`, `service` hữu ích. Label như `user_id` hoặc request UUID có cardinality cực cao và làm metric system tốn resource. Detail per-request phù hợp hơn với trace/log.

## 4. Logs cần structure và context

Structured log giúp machine query field thay vì parse text tự do. Một log entry hữu ích thường có timestamp chuẩn, service/version, severity, request/trace correlation và domain context phù hợp.

Không log secret/token/PII tùy tiện. Logging là data pipeline có security/privacy cost. “Log mọi thứ để debug” có thể tạo rủi ro lớn hơn incident ban đầu.

## 5. Distributed trace nối causal path của request

Trace mô tả request đi qua nhiều span. Nó giúp thấy thời gian nằm ở service nào, downstream call nào và retry có xảy ra không. Trace context phải propagate qua boundary; nếu proxy/message queue làm mất context, graph bị đứt.

Trace không thay metric. Sampling có thể bỏ request hiếm; metric vẫn tốt để phát hiện xu hướng. Hai loại signal bổ sung nhau.

## 6. Events và change telemetry

Deployment, config update, node drain, autoscaler action và certificate rotation là event có giá trị cao. Overlay change event lên latency/error chart thường rút ngắn điều tra.

Một platform nên làm change event tự động thay vì dựa vào người deploy nhớ ghi chú.

## 7. RED và USE như khung hỏi, không phải luật thuộc lòng

Với request-serving service, Rate, Errors, Duration giúp bắt đầu từ user-facing behavior. Với resource, Utilization, Saturation, Errors giúp tìm bottleneck. Nhưng framework chỉ là câu hỏi mở đầu.

Ví dụ CPU utilization thấp nhưng run queue cao do quota/throttling cần evidence khác. Database latency cao có thể đến từ lock contention dù CPU/storage metric bình thường.

## 8. Alert phải gắn với action

Alert tốt nói có user/reliability risk và người nhận có action hợp lý. Alert “CPU > 80% 5 phút” có thể không actionable nếu service vẫn khỏe và autoscaler đang làm việc.

Alert nên ưu tiên symptom gần SLO/user impact, sau đó dùng lower-level telemetry để chẩn đoán. Cause-based alert vẫn hữu ích với condition chắc chắn cần action như disk sắp đầy hoặc certificate sắp hết hạn.

## 9. Dashboard là map, không phải investigation engine duy nhất

Dashboard chuẩn giúp shared context: traffic, errors, latency, saturation, deployment marker. Nhưng incident mới có thể cần query ad-hoc. Platform observability nên cho phép đi từ overview → service → trace/log/resource bằng shared identifiers.

## 10. Evidence-driven debugging

Quy trình tốt bắt đầu bằng câu hỏi có thể bác bỏ. “Có phải rollout mới gây lỗi không?” kiểm tra deployment time và version dimension. “Có phải downstream DB chậm?” xem trace span, DB latency/pool saturation. “Có phải node pressure?” xem pod distribution, throttling, memory pressure.

Mỗi bước nên giảm search space. Tránh nhảy sang restart/scale nếu chưa có bằng chứng, trừ khi recovery priority buộc phải hành động ngay.

## 11. Instrumentation có cost

Telemetry tiêu CPU/network/storage và cost tài chính. High-cardinality logs/traces có thể đắt hơn application. Sampling và retention cần dựa trên mục tiêu điều tra/compliance.

Đừng tối ưu cost bằng cách xóa signal quan trọng nhất cho incident hiếm. Tốt hơn là phân tier retention, dynamic sampling và giữ exemplar/correlation.

## 12. OpenTelemetry như semantic layer

OpenTelemetry cung cấp chuẩn instrumentation/telemetry pipeline cho traces, metrics và logs trong nhiều hệ sinh thái. Giá trị lớn nằm ở portability và semantic convention, không phải “cài collector là có observability”. Application vẫn phải tạo span/metric có meaning đúng.

## 13. Senior note: observability là thiết kế interface cho failure

Khi thiết kế service, hãy hỏi trước: nếu request chậm, evidence nào phân biệt app CPU, DB, network và retry? Nếu deployment xấu, version có dimension trong metric không? Nếu queue backlog, có metric age/depth không? Nếu customer báo một request lỗi, có correlation identifier nào truy ra không?

Observability tốt được thiết kế cùng system, không phải gắn dashboard sau khi production đã khó hiểu.