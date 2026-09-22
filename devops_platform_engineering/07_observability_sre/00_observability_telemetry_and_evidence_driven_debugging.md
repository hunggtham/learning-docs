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

## 14. Telemetry pipeline cũng là một distributed system có thể fail

Application phát metric/log/trace nhưng signal thường còn đi qua agent, collector, queue, network và backend lưu trữ. Vì vậy “không thấy log” có ít nhất hai khả năng: event không xảy ra hoặc telemetry path làm mất event.

Platform cần quan sát chính observability pipeline: queue/backpressure, dropped spans/logs, export error, backend ingestion latency và sampling policy. Nếu collector quá tải trong đúng lúc incident traffic spike, evidence quý giá nhất có thể bị mất.

Đây là lý do telemetry pipeline cần capacity và failure semantics, không nên được coi là hệ thống phụ “không thể lỗi”.

## 15. Sampling phải biết câu hỏi cần trả lời

Head sampling quyết định giữ trace từ đầu request, rẻ và đơn giản nhưng có thể bỏ rare error trước khi biết request sẽ lỗi. Tail sampling quyết định sau khi thấy nhiều span/kết quả, có thể ưu tiên error/slow trace nhưng cần buffering/state và tăng complexity.

Không có một tỷ lệ sampling tốt cho mọi service. High-volume healthy traffic có thể sample thấp; error/security/critical transaction có thể giữ nhiều hơn. Quan trọng là biết signal nào vẫn đầy đủ — thường metric aggregate — và signal nào chỉ đại diện sample.

Khi điều tra “không có trace của request lỗi”, trước hết kiểm tra sampling/propagation trước khi kết luận request chưa vào service.

## 16. Percentile không cộng và không average đơn giản qua service

Nếu service A p99 = 200 ms và B p99 = 300 ms, không thể kết luận end-to-end p99 = 500 ms. Hai percentile có thể đến từ các request khác nhau. Tương tự average của p99 giữa nhiều instance không tạo p99 toàn fleet.

Histogram/distribution giữ count theo bucket cho phép aggregate đúng hơn trong nhiều hệ thống. Khi dashboard hiển thị percentile, operator cần biết percentile được tính từ raw events, histogram merge hay average của precomputed percentile.

Đây là assumption quan trọng vì tail latency thường quyết định SLO.

## 17. Clock và timestamp có thể làm causal order khó đọc

Distributed trace/log dựa vào timestamp từ nhiều host/process. Clock skew nhỏ có thể làm span trông như child bắt đầu trước parent hoặc log order lộn xộn. Protocol tracing thường có parent/child relation giúp reasoning tốt hơn chỉ sort timestamp.

Time synchronization vẫn quan trọng cho incident timeline, certificate và audit. Nhưng khi hai log lệch vài trăm mili giây, đừng suy luận causality chỉ từ timestamp tuyệt đối nếu có trace/event relation mạnh hơn.

## 18. Correlation ID không thay trace context

Một request ID tự tạo giúp search log nhưng thường chỉ là opaque label. Trace context còn mang trace/span relationship và sampling state qua hop. Hai thứ có thể cùng tồn tại; platform nên chuẩn hóa propagation qua HTTP, messaging và background task.

Đặc biệt với asynchronous queue, request lifecycle không còn một call stack đồng bộ. Message ID, trace/link và business entity ID có vai trò khác nhau. Không nên nhét tất cả vào một `correlation_id` rồi kỳ vọng query nào cũng dễ.

## 19. Cardinality explosion thường đến từ dimension tưởng như vô hại

Label `endpoint` có thể an toàn nếu chỉ vài route template như `/orders/{id}`. Nhưng nếu instrumentation dùng raw URL `/orders/12345`, mỗi ID tạo series mới. Tương tự error message nguyên văn, SQL text hoặc user ID.

Cardinality cao làm memory/index/query cost tăng và có thể khiến backend drop data hoặc rate-limit đúng lúc incident. Instrumentation nên normalize dimension và để detail high-cardinality sang trace/log.

Platform observability cần lint/convention để ngăn lỗi này sớm thay vì chữa bill/backend outage sau đó.

## 20. Exemplars nối aggregate metric với request cụ thể

Metric histogram cho thấy p99/slow bucket nhưng không nói request nào. Exemplar có thể gắn một sample trace ID vào bucket/point, cho phép drill-down từ aggregate anomaly sang trace cụ thể mà không biến metric label thành high-cardinality.

Đây là pattern hữu ích cho developer experience: dashboard latency tăng → click exemplar → trace → downstream span → log tương ứng. Correlation tốt giảm thời gian chuyển tool và giữ causal context.

## 21. Senior walkthrough: dashboard im lặng trong lúc user báo lỗi

Giả sử support nhận nhiều complaint nhưng error dashboard không tăng. Có ba nhóm hypothesis: SLI/metric không bao phủ failure business; telemetry pipeline/drop lỗi; hoặc complaint nằm ở subset dimension bị aggregate che.

Kiểm tra raw edge/access evidence, telemetry exporter/collector drop metric, version/region/tenant dimension và business outcome. Nếu HTTP 200 nhưng payload chứa business failure, transport error metric sẽ vẫn xanh.

Bài học là observability chỉ tốt bằng semantics đã instrument. “Dashboard xanh” không phải bằng chứng user experience xanh nếu sensor đo sai contract.