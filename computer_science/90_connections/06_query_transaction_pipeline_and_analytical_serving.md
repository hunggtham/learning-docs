# Từ truy vấn → giao dịch → pipeline → analytical serving

> **Mạch đọc:** Chapter này là một tuyến liên kết (connection route / 연결 경로), không tạo thêm một thư viện cơ sở dữ liệu (database / 데이터베이스) hay kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) mới. Cơ chế query, transaction, MVCC/WAL và database internals thuộc [Computer Science — Data & Databases](../05_data_databases/README.md); application persistence thuộc Backend; pipeline, warehouse và semantic serving thuộc [Data Engineering](../../data_engineering/README.md). Mục tiêu ở đây là nối các owner đó thành một mental model duy nhất: **một fact nghiệp vụ được tạo trong transactional system như thế nào, rồi đi qua pipeline để trở thành metric/dashboard/feature mà người dùng tin được?**

Một lỗi phổ biến là xem OLTP database và analytical system như hai thế giới tách rời. Trong thực tế, cùng một business event có thể xuất hiện dưới nhiều representation:

```text
HTTP command
→ application validation
→ database transaction
→ durable row / WAL
→ change event / extract
→ raw landing
→ transformation
→ warehouse/lakehouse table
→ semantic metric
→ dashboard / report / ML feature
```

Nếu mỗi bước được hiểu riêng nhưng không hiểu boundary giữa chúng, hệ thống có thể trả lời hai con số khác nhau cho cùng một câu hỏi mà không ai biết bước nào đã làm thay đổi meaning.

## 1. Bắt đầu từ business invariant, không bắt đầu từ SQL

Trước một query hay pipeline, phải biết **điều gì cần luôn đúng**.

Ví dụ với order:

```text
Một order đã thanh toán chỉ được tính revenue một lần.
Refund phải giảm net revenue đúng kỳ theo policy đã định nghĩa.
Order bị hủy trước settlement không được xuất hiện như realized revenue.
Dashboard phải nói rõ event time nào quyết định ngày ghi nhận.
```

SQL chỉ là cách biểu diễn computation. Nếu invariant chưa rõ, một query syntactically đúng vẫn tạo metric sai.

Điều này cũng giải thích vì sao schema design, transaction design và semantic layer không thể được tối ưu độc lập: tất cả đều đang encode cùng một business meaning ở các tầng khác nhau.

## 2. Query trả lời một snapshot, không tự trả lời “sự thật tuyệt đối”

Một truy vấn (query / 쿼리) luôn chạy trên một trạng thái dữ liệu cụ thể. Với hệ thống concurrent, trạng thái đó phụ thuộc isolation level, snapshot, replica lag và thời điểm query bắt đầu.

Hai analyst chạy cùng SQL cách nhau vài giây có thể nhận kết quả khác nhau nếu transaction mới commit. Một query đọc read replica có thể tạm thời chưa thấy write vừa commit ở primary.

Vì vậy khi hỏi:

> “Tại sao API nói order đã thanh toán nhưng dashboard chưa thấy?”

không nên nhảy ngay tới kết luận pipeline hỏng. Có thể transaction đã commit ở OLTP nhưng CDC chưa capture, event chưa được process, warehouse partition chưa refresh hoặc BI cache chưa hết hạn.

Tuyến thời gian đúng phải là:

```text
business event time
transaction commit time
change capture time
pipeline processing time
warehouse availability time
semantic refresh time
user query time
```

Sáu thời điểm này không giống nhau.

## 3. Transaction boundary là nơi business state trở thành durable state

Canonical mechanism nằm tại [Transactions, ACID và concurrency control](../05_data_databases/02_transactions_acid_and_concurrency_control.md) và [Storage, logs, recovery và durability](../05_data_databases/04_storage_logs_recovery_and_durability.md).

Ở connection layer, điều cần giữ là distinction:

```text
application accepted request
≠ transaction committed
≠ commit acknowledged to client
≠ downstream analytics observed change
```

Nếu HTTP response bị mất sau database commit, user có thể retry. Nếu retry tạo row mới thay vì nhận ra operation cũ, analytics sau đó sẽ “đúng” theo database nhưng business state đã bị duplicate từ đầu.

Do đó data quality downstream nhiều khi bắt đầu từ idempotency và transaction correctness upstream, không phải từ cleaning job.

## 4. Isolation level ảnh hưởng cả operational behavior lẫn analytical extraction

Concurrency control quyết định query thấy những version nào trong lúc write đang diễn ra. Read committed, repeatable read và serializable cho guarantee khác nhau.

Với application request, isolation chọn trade-off correctness/throughput. Với extraction job, isolation còn quyết định snapshot consistency.

Ví dụ một nightly export đọc `orders` rồi `payments` trong hai query độc lập. Nếu giữa hai query có transaction mới commit, export có thể lấy order mới nhưng chưa lấy payment tương ứng, dù database chưa từng tồn tại business state “order không payment” ở cùng một consistent snapshot.

Đây là lý do analytical extract lớn thường cần snapshot semantics rõ ràng thay vì giả định “SELECT từng bảng là đủ”.

## 5. WAL/redo log không chỉ phục vụ crash recovery

Write-ahead log (WAL / 선행 기록 로그) hoặc redo log tồn tại trước hết để durability/recovery. Nhưng cùng log-based change stream có thể trở thành nguồn cho change data capture (CDC / 변경 데이터 캡처).

Mental model:

```text
transaction mutates logical state
→ database records durable change information
→ replication / CDC reads ordered changes
→ downstream reconstructs another representation
```

Điều quan trọng là **log position** hoặc offset. Nếu consumer mất checkpoint, nó cần biết từ đâu resume. Nếu replay từ vị trí cũ, duplicate delivery có thể xảy ra; downstream phải có idempotency/deduplication strategy.

Database log vì vậy nối trực tiếp transaction semantics với streaming semantics.

## 6. “Exactly once” phải hỏi exactly once ở boundary nào

Một pipeline có thể quảng cáo exactly-once processing nhưng business metric vẫn duplicate nếu source event không có stable identity hoặc sink write không transactional theo cùng boundary.

Phải tách:

```text
message delivered once
record processed once
sink write committed once
business effect counted once
```

Bốn statement khác nhau.

Trong data engineering, thực tế thường đáng tin hơn khi thiết kế:

```text
at-least-once delivery
+ stable event identity
+ deterministic transformation
+ idempotent/transactional sink
+ reconciliation
```

thay vì dựa vào một nhãn “exactly once” chung chung.

## 7. Event identity quan trọng hơn row position

Một event nên có identity phản ánh business operation hoặc source change ổn định. Dùng row number, file line hoặc processing timestamp làm identity dễ vỡ khi backfill/repartition.

Ví dụ:

```text
order_id + event_type + version
```

có thể tốt hơn:

```text
partition=3, offset=98172
```

Offset hữu ích cho transport/checkpoint; business identity hữu ích cho deduplication và audit.

Không nên nhầm hai loại identity.

## 8. Snapshot + CDC là một migration problem, không chỉ connector configuration

Nhiều pipeline mới cần bootstrap toàn bộ dữ liệu lịch sử rồi theo CDC realtime.

Naive flow:

```text
full table copy
then start CDC
```

có thể tạo gap nếu write xảy ra giữa hai bước.

Một bootstrap đúng cần boundary rõ:

```text
capture source log position
→ take consistent snapshot corresponding to boundary
→ load snapshot
→ replay changes after boundary
→ validate convergence
```

Implementation cụ thể khác database/tool, nhưng invariant không đổi: **không mất change và không count change hai lần**.

## 9. Operational schema và analytical model tối ưu cho câu hỏi khác nhau

OLTP schema thường ưu tiên correctness của write, normalization, constraint và localized mutation. Analytical model ưu tiên stable business grain, scan efficiency và dễ aggregate.

Vì vậy normalization trong operational database không có nghĩa warehouse phải giữ y nguyên hàng chục join.

Nhưng denormalization chỉ hợp lệ nếu semantic transformation được document.

Ví dụ:

```text
operational:
orders
order_items
payments
refunds

analytical:
fact_order_item
fact_payment
fact_refund
dim_customer
dim_product
```

Một row trong `fact_order_item` phải có grain được nói thành câu, ví dụ “một item line tại một order version đã accepted”. Nếu không biết grain, aggregate gần như chắc chắn sẽ bị double-count ở đâu đó.

## 10. Grain là invariant trung tâm của bảng analytical

**Độ hạt (grain / 그레인)** trả lời: một row đại diện cho cái gì?

Trước khi thêm column, analyst/data engineer phải nói được:

> “Mỗi row trong bảng này là một ____.”

Nếu câu trả lời mơ hồ, join và aggregation sẽ mơ hồ.

Ví dụ một bảng trộn order-level và payment-level trong cùng row có thể duplicate order revenue khi một order có nhiều payment attempts.

Nhiều lỗi BI không phải lỗi SUM; chúng là lỗi grain.

## 11. Event time và processing time phải được tách

Một transaction có thể xảy ra lúc 23:59 nhưng pipeline xử lý lúc 00:05 hôm sau. Nếu dashboard group theo processing date thay vì event/business date, daily numbers bị lệch.

Các timestamp thường cần phân biệt:

```text
business_event_at
source_committed_at
ingested_at
processed_at
warehouse_loaded_at
```

Không phải dataset nào cũng cần đủ cả năm, nhưng pipeline phải biết timestamp nào mang semantic nào.

Late-arriving data làm distinction này quan trọng hơn.

## 12. Late data biến “final metric” thành khái niệm có thời gian

Dashboard ngày hôm qua có thể thay đổi hôm nay vì event đến muộn, refund được backfill hoặc source sửa dữ liệu.

Do đó metric cần freshness/completeness contract:

```text
preliminary until T+2h
mostly complete by T+1 day
closed after finance reconciliation
```

“Realtime” không đồng nghĩa “final”.

Người dùng business cần biết con số đang ở trạng thái nào thay vì chỉ thấy timestamp refresh gần nhất.

## 13. Backfill là re-execution của history, không phải copy file

Backfill xảy ra khi logic mới cần áp dụng lại lịch sử, dữ liệu cũ bị thiếu hoặc source correction cần propagate.

Một backfill an toàn cần trả lời:

```text
input version nào?
transformation version nào?
range thời gian nào?
sink overwrite hay merge?
job có idempotent không?
metric nào sẽ thay đổi?
consumer nào bị ảnh hưởng?
rollback/recompute thế nào?
```

Nếu transformation phụ thuộc “current lookup table” nhưng backfill lịch sử không biết dimension state tại thời điểm cũ, kết quả có thể không reproducible.

Đây là điểm nối giữa data lineage và temporal modeling.

## 14. Slowly changing dimension là bài toán thời gian của meaning

Customer có thể đổi country, subscription tier hoặc account owner. Câu hỏi analytical cần xác định dùng giá trị hiện tại hay giá trị tại thời điểm event.

```text
current-state question:
Khách hàng hiện thuộc segment nào?

historical-as-was question:
Khi order xảy ra, khách hàng thuộc segment nào?
```

Hai câu cần modeling khác nhau.

Nếu dimension overwrite current value nhưng analyst dùng nó để giải thích lịch sử, dashboard có thể “viết lại quá khứ” mà không ai nhận ra.

## 15. Data quality phải gắn với business invariant

Check `not null` và uniqueness hữu ích nhưng chưa đủ.

Data quality tốt nên có nhiều tầng:

```text
schema validity
→ key uniqueness
→ referential integrity
→ distribution/range sanity
→ freshness/completeness
→ cross-table invariant
→ business reconciliation
```

Ví dụ:

```text
sum(settled payments) - sum(refunds)
≈ recognized cash movement theo rule đã định nghĩa
```

Nếu check chỉ nói “pipeline green” nhưng finance total lệch 4%, reliability chưa đạt.

## 16. Reconciliation là cầu nối giữa source of truth và derived system

Một derived warehouse không nên được tin chỉ vì job thành công.

Cần định kỳ đối chiếu:

```text
source row/event counts
source business totals
CDC offsets / watermarks
warehouse totals
semantic metric totals
```

Chênh lệch phải có tolerance và explanation.

Reconciliation đặc biệt quan trọng sau incident, backfill, schema migration hoặc connector restart.

## 17. Data lineage phải trả lời được “con số này đến từ đâu?”

Lineage (계보 / nguồn gốc dữ liệu) không chỉ là graph đẹp giữa tables. Nó phải giúp answer incident:

> Metric `net_revenue` trên dashboard này lấy từ source column/event nào, qua transformation version nào, deploy nào và input window nào?

Một lineage hữu ích nên nối:

```text
source system
→ source schema/version
→ ingestion job/version
→ transformation/code version
→ dataset/table version
→ semantic definition
→ report/model consumer
```

Đây là provenance ở data system level.

## 18. Schema evolution là contract evolution

Source thêm nullable column thường ít nguy hiểm hơn source đổi meaning của column cũ.

Breaking change có thể là semantic chứ không syntactic:

```text
status='PAID'
```

trước đây nghĩa “payment authorized”, sau release nghĩa “funds settled”. Schema vẫn string; business meaning đã đổi hoàn toàn.

Vì vậy data contract phải quản lý cả type lẫn semantic definition.

## 19. Semantic layer tồn tại để centralize meaning, không chỉ centralize SQL

Một semantic layer (semantic layer / 시맨틱 레이어) nên định nghĩa metric, dimension, grain, filter và time semantics dùng chung.

Ví dụ `active_customer` cần nói rõ:

```text
active theo login?
active theo paid order?
trong 7, 30 hay 90 ngày?
timezone nào?
exclude test/internal account không?
```

Nếu mỗi dashboard tự viết SQL riêng, organization có nhiều “đúng” khác nhau.

Xem owner tại [Data Engineering — Serving & Semantic Layer](../../data_engineering/10_serving_semantic_layer/README.md).

## 20. Dashboard latency là tổng nhiều latency

Một user thấy dashboard chậm update. End-to-end freshness có thể được mô hình hóa:

```text
source commit lag
+ capture lag
+ transport lag
+ transform lag
+ warehouse load lag
+ semantic refresh/cache lag
```

Tối ưu warehouse query không giúp nếu capture lag đang 40 phút.

Vì vậy observability phải có watermark từng stage thay vì một metric “pipeline healthy”.

## 21. Data incident cần timeline giống production incident

Khi metric sai, incident analysis nên lập timeline:

```text
source deployment
schema change
first bad source event
CDC observation
pipeline run
warehouse write
semantic refresh
first user-visible bad metric
alert/report
backfill/reconciliation
```

Timeline này giúp phân biệt cause với propagation.

Một dashboard sai lúc 10:00 có thể do source bug từ 08:00, không phải BI release 09:55.

## 22. “Source of truth” nên nói theo loại sự thật

Một organization hiếm khi chỉ có một source of truth cho mọi câu hỏi.

Có thể có:

```text
OLTP database = source of truth cho current operational state
immutable event log = source of truth cho event history
finance ledger = source of truth cho accounting recognition
warehouse = source of truth cho standardized analytics
semantic layer = source of truth cho metric definition
```

Các owner khác nhau không mâu thuẫn nếu boundary rõ.

Câu “database nào là source of truth?” thường quá chung; câu tốt hơn là “source of truth cho fact nào và tại thời điểm nào?”.

## 23. Derived data không được mạnh hơn evidence upstream

Nếu source không thu thập một distinction, downstream model không thể khôi phục chắc chắn distinction đó chỉ bằng transformation.

Ví dụ source chỉ lưu `status='FAILED'` nhưng không phân biệt timeout với rejection. Warehouse có thể infer từ pattern, nhưng đó là estimate, không phải recorded fact.

Một semantic layer tốt nên giữ distinction:

```text
recorded fact
inferred attribute
business rule classification
prediction
```

Không biến inference thành fact bằng cách đặt tên column tự tin.

## 24. Query optimization và analytical correctness là hai trục khác nhau

Một query có thể chạy rất nhanh nhưng trả sai grain; một query đúng có thể chạy chậm vì scan/join lớn.

Canonical query optimization nằm tại [Indexes và query execution](../05_data_databases/03_indexes_and_query_execution.md) và [Query optimization & execution plans](../05_data_databases/06_query_optimization_and_execution_plans.md).

Connection layer phải kiểm tra theo thứ tự:

```text
1. semantic correctness
2. snapshot/time correctness
3. completeness/freshness
4. performance/cost
```

Không nên tối ưu query sai thành query sai nhanh hơn.

## 25. Worked case: payment metric lệch 3%

Giả sử API/payment service báo settled amount trong ngày là 10 tỷ nhưng dashboard chỉ có 9,7 tỷ.

Không bắt đầu bằng sửa SQL. Vẽ path:

```text
payment transaction
→ primary DB
→ WAL/CDC
→ ingestion
→ raw events
→ transform
→ fact_payment
→ semantic metric
→ dashboard
```

Sau đó kiểm tra boundary:

**Operational state:** query primary theo stable settlement rule có thật là 10 tỷ không?

**Snapshot:** con số 10 tỷ được query ở thời điểm nào? Có settlement sau dashboard watermark không?

**CDC:** source log position đã tới đâu? Có connector restart/gap không?

**Raw landing:** event count và total amount có khớp CDC không?

**Transformation:** dedupe key có vô tình drop legitimate repeated payments không? Currency conversion dùng rate/date nào?

**Warehouse:** partition ngày đúng business timezone không?

**Semantic layer:** metric có exclude refund/test account theo rule khác operational query không?

Khi tìm thấy nguyên nhân, recovery phải chọn đúng lớp. Nếu raw đủ nhưng transformation bug, backfill transform; không cần replay source. Nếu CDC thiếu range, cần recapture/replay từ source boundary. Nếu source business state đã sai, analytical backfill không thể sửa root cause.

## 26. Failure mode: silent duplication

Duplicate nguy hiểm vì pipeline có thể vẫn green.

Nguồn thường gặp:

```text
retry after unknown outcome
CDC replay
consumer restart
non-idempotent merge
many-to-many join
backfill overlap
```

Dấu hiệu tốt hơn CPU/job status là business invariant:

```text
unique business event count
sum by stable operation id
source-to-sink reconciliation
```

## 27. Failure mode: silent omission

Missing data cũng có thể không làm job fail nếu connector watermark nhảy qua range hoặc filter mới loại event hợp lệ.

Cần completeness evidence:

```text
expected partitions/windows
source watermark
sink watermark
row/event count envelope
business-total reconciliation
```

“Không có error log” không phải bằng chứng dữ liệu đầy đủ.

## 28. Failure mode: semantic drift

Schema không đổi nhưng business policy đổi. Dashboard vẫn chạy và số vẫn “hợp lý”, nhưng meaning khác trước.

Ví dụ definition “active subscriber” đổi từ `paid_in_last_30d` sang `subscription_status='ACTIVE'`.

Đây là semantic versioning problem. Metric definition cần owner, effective date và change note.

## 29. Failure mode: backfill rewrites history unexpectedly

Một transformation mới fix bug nhưng khi backfill toàn bộ lịch sử lại dùng current dimension mapping, làm historical segment distribution đổi mạnh.

Cần quyết định rõ:

```text
restate history theo current corrected logic
hay
preserve as-was historical reporting
```

Hai mục tiêu đều có thể hợp lệ tùy domain; không nên để implementation tự quyết.

## 30. Runbook suy luận cho data path

Khi một metric bị nghi sai, thứ tự hợp lý:

```text
1. viết metric/business invariant bằng lời
2. xác định grain và time semantics
3. tìm operational/ledger reference
4. kiểm tra source commit và snapshot
5. theo watermark/offset qua từng stage
6. đối chiếu count + business total
7. xác định first divergent boundary
8. chỉ sau đó đọc sâu query/job/log tại boundary đó
9. chọn replay/backfill/reconcile/compensate phù hợp
10. verify convergence sau recovery
```

Mental model này giảm việc debug ngẫu nhiên từ dashboard xuống database.

## 31. Canonical owner map

Đọc sâu cơ chế ở:

- [Data models & database systems](../05_data_databases/00_data_models_and_database_systems.md)
- [Transactions, ACID & concurrency](../05_data_databases/02_transactions_acid_and_concurrency_control.md)
- [Indexes & query execution](../05_data_databases/03_indexes_and_query_execution.md)
- [Storage logs, recovery & durability](../05_data_databases/04_storage_logs_recovery_and_durability.md)
- [Relational algebra & SQL semantics](../05_data_databases/05_relational_algebra_and_sql_semantics.md)
- [Query optimization & execution plans](../05_data_databases/06_query_optimization_and_execution_plans.md)
- [Data Engineering — Pipeline Architecture](../../data_engineering/02_pipeline_architecture.md)
- [Data Engineering — Reliability & Production](../../data_engineering/04_reliability_and_production.md)
- [Serving & Semantic Layer](../../data_engineering/10_serving_semantic_layer/README.md)
- [Production request → storage → queue → recovery](../../devops_platform_engineering/10_production_practice/01_request_storage_queue_failure_and_recovery_case.md)

`sql/` trong repository hiện chủ yếu là corpus/output học SQL và nguồn raw; các mental model database/SQL semantics chuẩn gốc vẫn thuộc `computer_science/05_data_databases/`.

## 32. Mô hình tư duy cuối

Hãy giữ chuỗi này:

```text
business invariant
→ operational command
→ transactional commit
→ durable change identity/order
→ capture + checkpoint
→ deterministic transformation
→ analytical grain + time semantics
→ semantic metric
→ user decision
→ reconciliation + feedback
```

Nếu một metric sai, tìm **first boundary nơi meaning hoặc completeness diverge**. Nếu một pipeline nhanh nhưng metric không định nghĩa grain/time/source-of-truth, hệ thống chưa đáng tin. Nếu một warehouse đúng nhưng source transaction đã duplicate, analytics không thể cứu business correctness.

> **Bàn giao:** Sau chapter này, người đọc nên có thể lấy một metric thực tế, vẽ toàn bộ lineage từ transaction tới dashboard, ghi rõ grain/time semantics/watermark và thiết kế một reconciliation rule. Sau đó chuyển sang [Data Engineering](../../data_engineering/README.md) để đào sâu pipeline/warehouse hoặc quay về [Computer Science Databases](../05_data_databases/README.md) để đào sâu query/transaction/storage mechanism.