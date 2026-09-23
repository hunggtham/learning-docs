# 04 — Reliability, data quality và production reasoning

## 1. Pipeline success khác data success

Một process exit code `0` chỉ chứng minh code không báo lỗi theo contract của process. Nó không chứng minh output đầy đủ, đúng business rule hoặc fresh.

Ví dụ source trả về HTTP 200 nhưng chỉ có 20% records vì pagination bug. Pipeline có thể xanh từ đầu đến cuối. Vì vậy production Data Engineering cần quan sát cả system metrics lẫn data metrics.

## 2. Data quality theo invariant

Rule quality tốt xuất phát từ invariant thay vì danh sách check chung chung. `NOT NULL` hữu ích nếu null thực sự bất hợp lệ. `row_count > 0` không đủ nếu bình thường dataset có mười triệu row nhưng hôm nay chỉ còn một nghìn.

Các invariant có thể nằm ở nhiều tầng: schema invariant, uniqueness, referential integrity, accepted domain, volume distribution, reconciliation với source và business equation.

Ví dụ payment system có thể kiểm tra tổng captured amount theo source ledger và warehouse trong tolerance xác định. Reconciliation như vậy mạnh hơn chỉ kiểm tra column type.

## 3. Freshness, completeness và correctness

Freshness hỏi dữ liệu mới đến mức nào. Completeness hỏi dữ liệu cần có đã đến đủ chưa. Correctness hỏi giá trị có đúng theo semantics không.

Ba khái niệm không thay thế nhau. Dataset có thể fresh vì vừa update nhưng thiếu 30% partition. Nó có thể complete nhưng dùng sai exchange rate. Dashboard có timestamp mới không chứng minh business data đáng tin.

## 4. Data contract

Data contract làm expectation giữa producer và consumer trở nên explicit: schema, semantics, ownership, compatibility, quality và đôi khi SLO.

Contract không nhất thiết là một framework. Giá trị của nó nằm ở việc breaking change không còn là surprise. Producer biết consumer phụ thuộc vào điều gì; consumer biết dataset được hứa những guarantee nào.

Contract quá cứng cũng có trade-off: nó có thể làm evolution chậm. Vì vậy cần phân biệt field public/stable với implementation detail và có versioning/deprecation process.

## 5. Lineage

Lineage trả lời dataset này đến từ đâu và downstream nào phụ thuộc vào nó. Khi source column thay đổi, lineage giúp xác định blast radius.

Lineage chỉ từ static SQL parsing có thể thiếu dynamic job, UDF hoặc external process. Runtime lineage chính xác hơn ở một số trường hợp nhưng tốn instrumentation. Production platform thường cần kết hợp metadata từ orchestration, catalog, query engine và deployment system.

Lineage không tự tạo trust. Nó là evidence graph; quality và ownership vẫn phải được duy trì.

## 6. Observability

System observability theo dõi CPU, memory, latency, error rate, queue lag và resource saturation. Data observability bổ sung freshness, volume, schema drift, distribution và lineage-aware impact.

Một alert tốt phải actionable. "row count changed" không đủ nếu không có baseline, severity, dataset owner và runbook. Alert quá nhạy gây fatigue; alert quá lỏng phát hiện incident sau consumer.

Senior note: monitoring nên bám vào user-visible/data-product SLO trước rồi drill down tới component metrics. Nếu chỉ monitor từng task, có thể tất cả task đều xanh trong khi data product đã vi phạm freshness SLO.

## 7. Retry và poison data

Retry hữu ích cho transient failure như network timeout nhưng có thể làm tình hình tệ hơn với deterministic failure. Một malformed record retry 100 lần vẫn malformed và có thể block partition.

Cần phân biệt transient, permanent và unknown failure. Dead-letter/quarantine path cho phép tách poison data khỏi main flow, nhưng không được biến thành nơi âm thầm bỏ dữ liệu. Quarantine phải có owner, metric, retention và replay procedure.

Exponential backoff và jitter giúp tránh hàng nghìn worker retry đồng thời sau outage, gây thundering herd lên dependency vừa phục hồi.

## 8. Recovery và disaster thinking

Backup chỉ có giá trị nếu restore được. Tương tự, event retention chỉ có giá trị nếu đủ để replay trong recovery window.

Recovery design cần biết Recovery Point Objective (RPO) — chấp nhận mất tối đa bao nhiêu dữ liệu — và Recovery Time Objective (RTO) — chấp nhận mất bao lâu để phục hồi service/data product.

Một pipeline có thể rebuild từ immutable raw log có recovery model khác pipeline chỉ giữ transformed latest state. Khả năng recompute là một tài sản kiến trúc, nhưng phải cân bằng với storage cost và retention/privacy policy.

## 9. Security và governance

Data platform thường tập trung dữ liệu từ nhiều source nên blast radius của quyền truy cập rất lớn. Principle of least privilege cần áp dụng cho service account, engineer và consumer.

Encryption at rest/in transit là nền tảng nhưng không thay thế authorization. Sensitive field có thể cần masking/tokenization, row/column-level access và audit log. Development environment không nên mặc định copy production PII nguyên vẹn.

Retention cũng là security property. Giữ dữ liệu vô thời hạn làm tăng attack surface và có thể xung đột policy/pháp lý. Data lifecycle phải bao gồm deletion, không chỉ ingestion.

## 10. Performance và cost trong production

Khi pipeline chậm, đừng tối ưu theo cảm giác. Tách thời gian thành source read, serialization, network, compute, shuffle, sink write và orchestration wait. Xác định bottleneck trước.

Distributed job có thể chậm vì data skew: một key chiếm phần lớn records khiến một task xử lý lâu hơn tất cả task khác. Tăng số worker không nhất thiết giải quyết hotspot. Cần thay partition strategy, pre-aggregation, salting hoặc xử lý heavy hitter riêng tùy semantics.

Cost cũng phải nhìn theo unit kinh doanh như cost trên TB processed, cost trên pipeline run hoặc cost trên data product, thay vì chỉ tổng hóa đơn. Unit economics giúp thấy regression khi volume thay đổi.

## 11. Production incident reasoning

Khi metric sai, debugging nên đi ngược lineage: consumer thấy gì → serving table được publish khi nào → transformation dùng input snapshot nào → ingestion có gap/duplicate không → source có thay semantics không.

Giữ run metadata như code version, input partitions/snapshot, row counts, checkpoint, schema version và output commit giúp biến debugging từ suy đoán thành điều tra dựa trên evidence.

Một hệ thống dữ liệu trưởng thành không phải hệ thống không bao giờ lỗi. Nó là hệ thống phát hiện lỗi sớm, giới hạn blast radius, giải thích được trạng thái, replay/recover có kiểm soát và học được từ incident để invariant được bảo vệ tốt hơn ở lần sau.

## 12. Reliability budget cho data product

Data product nên có SLO riêng thay vì chỉ dùng task success rate:

```text
freshness SLO       = thời gian tối đa từ source event đến publish
completeness SLO    = tỷ lệ input cần có đã được xử lý
correctness SLO     = tỷ lệ reconciliation/quality gate đạt
availability SLO    = consumer có đọc được version hợp lệ không
```

Một job chạy xanh 99.9% nhưng freshness trễ 4 giờ vẫn có thể vi phạm product SLO. Error budget nên được dùng để quyết định có ưu tiên feature mới, backfill hay reliability work.

## 13. Quality gate theo tầng

Quality check nên đặt gần failure boundary:

1. ingestion: schema, checksum, duplicate identity, source cursor;
2. transformation: grain, uniqueness, referential integrity, accepted domain;
3. publish: row count, freshness, reconciliation, snapshot completeness;
4. serving: metric golden set, point-in-time correctness, consumer contract.

Check ở tầng cuối không thay thế check ở tầng trước. Nếu chỉ kiểm tra dashboard, rất khó biết mất dữ liệu xảy ra ở source, transport hay join.

## 14. Incident timeline và evidence

Một incident report tốt không chỉ có “job failed”. Nó ghi lại source watermark, input partitions, code/schema version, checkpoint, output commit, quality results, consumer impact và các quyết định rollback/replay.

Timeline cần phân biệt:

```text
first bad input → first bad transform → bad publish → first consumer observation
```

Phân biệt bốn mốc này giúp tránh sửa nhầm layer và đo được detection lag.

## 15. Chaos và recovery test

Recovery claim phải được kiểm chứng bằng thử nghiệm: kill worker trước/sau sink commit, làm mất acknowledgement, inject late event, truncate source retention giả lập, chạy duplicate backfill và restore snapshot. Test cần kiểm tra cả output correctness lẫn absence of unwanted side effect.

Một runbook chưa từng chạy trong điều kiện gần production chỉ là giả thuyết. Recovery time phải được đo, không suy ra từ sơ đồ architecture.
