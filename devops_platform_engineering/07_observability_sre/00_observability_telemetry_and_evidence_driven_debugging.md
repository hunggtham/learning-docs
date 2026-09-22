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

## 22. Missing data khác zero và khác healthy

Một dashboard trả `0 errors` có thể nghĩa thật sự không có lỗi, nhưng cũng có thể vì exporter chết, target không scrape được hoặc query vô tình loại bỏ series mất dữ liệu. Đây là khác biệt giữa **absence of bad events** và **absence of observations**.

Monitoring design nên làm missing-data semantics explicit. Với metric critical, loss of signal có thể cần alert riêng. Một SLI pipeline không được mặc định coi missing sample là success nếu điều đó làm outage telemetry biến thành availability 100%.

Khi service biến mất khỏi dashboard đúng lúc incident, hãy hỏi target có còn emit không, collector có nhận không, backend có ingest không và query có còn match label mới không trước khi kết luận service idle.

## 23. Counter reset và process restart làm rate query dễ sai

Counter thường tăng đơn điệu trong lifetime của process, nhưng process restart đưa counter về 0. Query tính rate cần hiểu reset semantics; lấy chênh lệch hai sample thủ công có thể tạo rate âm hoặc spike giả.

Tương tự, một fleet scale-out tạo nhiều time series mới. Nếu dashboard cộng raw counter không chuẩn hóa theo thời gian hoặc instance lifetime, số nhìn có thể thay đổi chỉ vì topology thay đổi chứ business traffic không đổi.

Operational lesson là biết metric type và lifecycle. Dashboard formula là code; nó cần review, test với restart/gap và version cùng semantic contract giống application logic quan trọng khác.

## 24. Log delivery thường không có exactly-once semantics

Agent/collector có thể buffer rồi retry khi backend tạm lỗi. Điều này tốt cho durability nhưng có thể tạo duplicate log. Network/retry/batching cũng có thể làm event tới backend khác thứ tự timestamp hoặc ingestion order.

Vì vậy đếm business event bằng log line cần cẩn thận. Nếu một payment success log bị gửi lại hai lần, query `count()` không nhất thiết bằng số payment thật. Với audit/business invariant quan trọng, event cần stable identity/deduplication semantics hoặc source dữ liệu authoritative hơn.

Log là evidence tuyệt vời nhưng không nên vô thức biến thành transaction ledger nếu pipeline không có contract tương ứng.

## 25. Telemetry schema cũng tiến hóa như API

Đổi tên metric, label, log field hoặc span attribute có thể làm dashboard/alert/query im lặng mà application vẫn chạy. Nếu rollout application và dashboard không coordinated, một phần fleet dùng schema cũ, phần khác schema mới, aggregate có thể double-count hoặc bỏ sót.

Shared semantic convention cần version/migration window. Có thể emit old+new field tạm thời, update query trước rồi mới remove old, hoặc dùng recording/translation layer tùy system.

Đây là một compatibility problem: observability consumer cũng là consumer của telemetry API.

## 26. Observer effect: instrumentation có thể làm workload thay đổi

Tracing mọi request với payload lớn, synchronous log flush hoặc stack-profile quá nặng có thể tăng CPU, I/O và latency. Trong incident, bật debug log toàn fleet đôi khi làm disk/network pressure nặng thêm và che root cause ban đầu.

Instrumentation cần budget và activation scope. Debug mode nên có TTL, sampling hoặc targeted cohort khi có thể. Một diagnostic action tốt luôn hỏi thêm: evidence mới tạo ra có làm thay đổi system đủ lớn để invalidate observation không?

Điều này đặc biệt quan trọng với profiling, packet capture và verbose logging trên path latency-sensitive.

## 27. Sampling policy có thể bias chính failure muốn tìm

Nếu sampling quyết định dựa trên latency threshold, error code hoặc tenant, dataset giữ lại không còn đại diện traffic tổng thể. Điều đó không xấu nếu mục tiêu là debugging rare failure, nhưng không được dùng sample đó để ước lượng tỷ lệ toàn bộ user mà không biết selection bias.

Tail sampling còn phụ thuộc việc trace hoàn thành và collector có đủ buffer. Trong overload, slow trace có thể bị drop do memory pressure đúng lúc ta muốn giữ chúng nhất.

Một observability platform trưởng thành tách use case: metric đầy đủ cho population-level rate/SLO, sampled traces cho causal detail, và policy rõ về bias của sample.

## 28. Black-box và white-box telemetry trả lời hai phía khác nhau của contract

White-box metric nhìn từ bên trong service: queue, thread pool, GC, DB pool. Black-box probe nhìn như consumer: DNS resolve được không, TLS/HTTP có trả đúng không, synthetic transaction có hoàn thành không.

Một service có internal dashboard xanh nhưng edge route hỏng; ngược lại synthetic probe fail từ một region trong khi service process khỏe. Hai perspective không cạnh tranh mà giúp xác định boundary failure.

Với capability critical, một số external/synthetic check giúp phát hiện class failure mà self-reported telemetry không thể thấy — đặc biệt khi chính service hoặc telemetry agent đã chết.

## 29. Stale telemetry có thể nguy hiểm hơn missing telemetry

Missing signal thường dễ nhận ra. Stale signal khó hơn vì dashboard vẫn có giá trị cuối cùng và người xem tưởng nó mới. Cache, exporter stuck, delayed ingestion hoặc query window có thể giữ “CPU 40%, replicas 10” dù actual state đã đổi.

Mọi critical signal nên có freshness context: sample timestamp, scrape age, ingestion lag hoặc heartbeat phù hợp. Khi incident, một evidence item không chỉ cần hỏi “giá trị là gì?” mà còn “được quan sát khi nào và từ state version nào?”.

Senior reasoning coi freshness như một dimension của evidence. Dữ liệu chính xác nhưng quá cũ có thể dẫn tới action sai giống dữ liệu sai.

## 30. Telemetry cần priority khi chính observability pipeline quá tải

Khi ingestion vượt capacity, drop ngẫu nhiên mọi signal có thể làm mất đúng error/security event quan trọng trong khi giữ hàng triệu debug log ít giá trị. Vì vậy overload policy nên phản ánh giá trị evidence: SLO metric, audit/security event và critical error có thể cần durability/priority cao hơn verbose trace hoặc debug log.

Priority không có nghĩa mọi critical signal được giữ vô hạn. Nếu buffer không bound, observability agent có thể làm application/node OOM. Cần explicit queue limit, spill/durable path khi phù hợp, drop counter và degradation policy. Điều quan trọng là khi mất dữ liệu, ta biết **loại nào bị mất, bao nhiêu và vì sao**.

Đây là admission control áp dụng cho telemetry: system bảo vệ capability chẩn đoán cốt lõi thay vì để overload biến toàn bộ evidence thành ngẫu nhiên.

## 31. Observability backend cũng có noisy-neighbor và query blast radius

Một truy vấn regex rộng trên log nhiều tháng, dashboard fan-out hàng nghìn series hoặc tenant có cardinality bùng nổ có thể làm query/ingestion backend chậm cho người khác. Multi-tenancy của observability vì vậy cần quota không chỉ ở ingestion mà cả retained data, concurrent query, scan volume và cardinality.

Trong incident, operator cần query nhanh nhất đúng lúc toàn tổ chức cùng mở dashboard. Capacity model phải xét **incident concurrency**, không chỉ traffic ngày thường. Có thể cần precomputed/recording data cho SLO, query priority, per-tenant limit và isolation cho audit/critical telemetry.

Nếu observability backend là shared dependency toàn công ty, một query xấu không nên có blast radius tương đương outage monitoring toàn bộ fleet.

## 32. Retention nên đi từ câu hỏi điều tra và nghĩa vụ, không từ một con số chung

Không phải mọi telemetry cần giữ 90 ngày ở cùng độ chi tiết. High-resolution metric hữu ích cho incident gần; aggregate dài hạn hữu ích cho capacity/trend. Full trace có thể chỉ cần giữ ngắn, trong khi security/audit evidence có retention dài hơn vì forensic/compliance.

Một retention design tốt hỏi: failure thường được phát hiện sau bao lâu; capacity cần seasonality dài bao nhiêu; audit yêu cầu gì; replay/debug cần raw detail hay aggregate. Sau đó mới chọn tier hot/warm/archive hoặc downsampling. Xóa detail quá sớm làm forensic bất khả thi; giữ mọi thứ mãi mãi tăng cost, privacy exposure và query surface.

Retention vì vậy là product/security/reliability contract, không chỉ storage setting.

## 33. Telemetry cost cần attribution theo signal driver

Bill observability thường tăng vì một số driver cụ thể: log volume, retained bytes, high-cardinality series, trace span count, egress hoặc query scan. Nếu chỉ phân bổ theo số service, team ít có feedback để sửa instrumentation gây cost.

Platform nên expose cost/usage theo service hoặc tenant ở mức đủ gần causal driver: `GB ingested`, `GB-day retained`, active series/cardinality, sampled span volume, expensive query class. Nhưng cost guardrail phải đi cùng reliability guardrail; cắt trace sampling xuống gần zero để đạt budget có thể phá diagnosability.

Mental model FinOps ở đây là `question/evidence value → signal design → ingestion/retention/query cost → feedback cho owner`. Mục tiêu không phải telemetry rẻ nhất mà là **chi phí thấp nhất vẫn giữ được quyết định production cần thiết**.

## 34. Senior walkthrough: incident làm observability chết trước application

Giả sử release lỗi tạo exception loop, mỗi request phát hàng trăm log line. Application vẫn còn phục vụ một phần traffic nhưng log ingestion tăng 50 lần, collector queue đầy, backend query timeout và on-call mất visibility. Tăng log backend vô hạn không phải fix bền vững vì chính failure path có amplification factor không bound.

Causal chain là `application fault → telemetry amplification → collector/backend saturation → evidence loss → recovery chậm`. Mitigation có thể rate-limit/sampling log lặp, ưu tiên error summary/SLO signal, bảo vệ backend bằng tenant/query quota và giữ drop counter. Sau incident, instrumentation phải được sửa để một lỗi application không thể biến thành observability outage có blast radius lớn hơn lỗi gốc.

Đây là ví dụ rõ rằng observability nằm trong production dependency graph và cần overload/failure design giống mọi shared platform khác.