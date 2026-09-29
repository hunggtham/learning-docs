# Từ truy vấn → giao dịch → pipeline → phục vụ phân tích

> **Mạch đọc:** Chapter này là tuyến liên kết, không tạo thêm một thư viện Database hoặc Data Engineering mới. Cơ chế truy vấn, giao dịch, MVCC/WAL và nội tại cơ sở dữ liệu thuộc [Computer Science — Data & Databases](../05_data_databases/README.md); persistence ở lớp ứng dụng thuộc Backend; pipeline, warehouse và lớp ngữ nghĩa thuộc [Data Engineering](../../data_engineering/README.md). Câu hỏi trung tâm là: **một fact nghiệp vụ được tạo trong hệ thống giao dịch như thế nào, rồi đi qua nhiều boundary để trở thành metric, dashboard hoặc feature mà người dùng có thể tin?**

Một business event thường trải qua chuỗi:

```text
HTTP command
→ validation ở ứng dụng
→ database transaction
→ durable state / WAL
→ change event / extract
→ raw landing
→ transformation
→ warehouse/lakehouse table
→ semantic metric
→ dashboard / report / ML feature
```

Nếu từng bước đúng riêng lẻ nhưng meaning không được giữ qua boundary, hai hệ thống có thể trả hai con số khác nhau cho cùng câu hỏi mà không ai biết semantic drift bắt đầu ở đâu.

## 1. Bắt đầu từ bất biến nghiệp vụ, không bắt đầu từ SQL

Trước query hoặc pipeline, phải biết điều gì cần luôn đúng.

Ví dụ với đơn hàng:

```text
đơn đã thanh toán chỉ được tính doanh thu một lần
refund phải giảm doanh thu ròng theo policy đã định nghĩa
đơn hủy trước settlement không được tính như realized revenue
ngày ghi nhận phải dựa trên một event-time rule rõ ràng
```

SQL chỉ là cách biểu diễn phép tính. Nếu invariant chưa rõ, query đúng cú pháp vẫn có thể tạo metric sai.

Điều này giải thích vì sao schema, transaction design và semantic layer không thể tối ưu độc lập: cả ba đang mã hóa cùng một business meaning ở các lớp khác nhau.

## 2. Truy vấn đọc một trạng thái, không đọc “sự thật tuyệt đối”

Một **truy vấn (query / 쿼리)** luôn chạy trên một trạng thái cụ thể của dữ liệu. Trong hệ thống concurrent, trạng thái đó phụ thuộc isolation level, snapshot, replica lag và thời điểm query bắt đầu.

Hai người chạy cùng SQL cách nhau vài giây có thể nhận kết quả khác nhau vì transaction mới commit. Một read replica có thể chưa thấy write vừa commit ở primary.

Khi API nói “đã thanh toán” nhưng dashboard chưa thấy, không nên kết luận pipeline hỏng ngay. Cần tách các mốc thời gian:

```text
thời điểm business event
→ transaction commit time
→ change capture time
→ pipeline processing time
→ warehouse availability time
→ semantic refresh time
→ user query time
```

Các mốc này có thể cách nhau từ mili giây tới nhiều giờ.

## 3. Transaction boundary là nơi trạng thái nghiệp vụ chuyển thành trạng thái bền

Ở lớp ứng dụng cần phân biệt:

```text
request đã được nhận
≠ transaction đã commit
≠ client đã nhận acknowledgement
≠ downstream analytics đã quan sát được thay đổi
```

Nếu response HTTP bị mất sau khi transaction commit, người dùng có thể retry. Nếu retry tạo một record mới thay vì nhận ra operation cũ, dữ liệu downstream có thể “nhất quán” với database nhưng business fact đã bị duplicate từ đầu.

Vì vậy chất lượng analytics nhiều khi bắt đầu từ idempotency và transaction correctness upstream chứ không phải từ cleaning job.

## 4. Isolation ảnh hưởng cả ứng dụng lẫn extraction

**Mức cô lập (isolation level / 격리 수준)** quyết định transaction đọc thấy version nào khi write đang diễn ra.

Ở application layer, isolation cân bằng correctness và throughput. Ở extraction layer, nó còn quyết định snapshot consistency.

Ví dụ một export đọc `orders` rồi `payments` bằng hai query riêng. Nếu transaction mới commit giữa hai query, export có thể thấy order mới nhưng chưa thấy payment tương ứng. Database có thể chưa bao giờ tồn tại trạng thái nghiệp vụ “order đã trả tiền nhưng không có payment” trong cùng một snapshot, nhưng extract lại tạo ra trạng thái đó.

Do đó batch extraction cần snapshot semantics rõ chứ không thể mặc định “SELECT từng bảng là đủ”.

## 5. WAL và durability không phải chỉ là chuyện của DBA

**Nhật ký ghi trước (write-ahead log, WAL / 선행기입 로그)** cho phép database bảo toàn durability và recovery. Application không cần biết mọi chi tiết implementation, nhưng cần hiểu commit acknowledgement dựa trên contract durability nào.

Một write có thể đi qua nhiều lớp:

```text
application
→ database buffer
→ WAL / storage engine
→ filesystem/page cache
→ block device
→ durable media
```

Đường này nối trực tiếp với Linux durability. Khi điều tra sự cố, phải biết lớp nào đã xác nhận điều gì thay vì dùng “đã ghi xuống disk” như một câu mơ hồ.

## 6. CDC biến thay đổi transaction thành dòng sự kiện

**Bắt thay đổi dữ liệu (change data capture, CDC / 변경 데이터 캡처)** đọc thay đổi từ log hoặc cơ chế tương đương rồi chuyển chúng sang downstream.

CDC hữu ích vì tránh quét toàn bảng liên tục, nhưng nó tạo thêm semantic boundary:

```text
row change
→ change event
→ delivery
→ consumer state
```

Cần xác định:

- event order có guarantee gì;
- duplicate có thể xảy ra không;
- delete/update biểu diễn thế nào;
- schema change ảnh hưởng ra sao;
- checkpoint/offset được lưu ở đâu;
- backfill phối hợp với CDC thế nào.

Nếu consumer giả định exactly-once trong khi source chỉ at-least-once, duplicate metric là kết quả dễ xảy ra.

## 7. Dual write là một lỗi boundary cổ điển

Nếu application vừa commit database vừa publish message bằng hai thao tác độc lập:

```text
DB commit thành công
message publish thất bại
```

hoặc ngược lại, hai hệ thống có thể lệch nhau.

**Mẫu outbox giao dịch (transactional outbox / 트랜잭셔널 아웃박스)** giải quyết bằng cách ghi business state và outbox record trong cùng transaction, sau đó process khác publish event từ outbox.

Outbox không xóa mọi failure; nó chuyển bài toán sang idempotent publishing/consuming và monitoring backlog. Nhưng nó làm boundary giữa commit và event rõ hơn.

## 8. Raw landing nên giữ provenance trước khi “làm sạch”

Khi dữ liệu rời source, lớp raw nên giúp truy nguyên:

```text
nguồn nào?
revision/offset nào?
arrived_at khi nào?
schema/version nào?
record gốc là gì?
```

Nếu transform đầu tiên phá mất identifier hoặc timestamp gốc, reconciliation sau này khó hơn nhiều.

Raw layer không phải nơi người dùng cuối đọc trực tiếp; nó là lớp provenance để có thể dựng lại hoặc audit transformation.

## 9. Event time và processing time phải tách nhau

Một order có thể được tạo lúc 23:59 nhưng pipeline xử lý lúc 00:03 ngày hôm sau.

**Thời gian sự kiện (event time / 이벤트 시간)** mô tả khi business event xảy ra. **Thời gian xử lý (processing time / 처리 시간)** mô tả khi hệ thống xử lý record.

Nếu metric doanh thu theo ngày vô tình dùng processing time, dữ liệu đến trễ sẽ bị ghi sai ngày. Vì vậy mỗi pipeline cần xác định timestamp nào mang business meaning.

## 10. Late data làm “kết quả cuối ngày” không thật sự cuối

Dữ liệu có thể đến trễ vì network, source outage, retry, mobile offline hoặc upstream batch delay.

Do đó analytical system phải định nghĩa:

```text
late data được chấp nhận tới bao lâu?
window nào được mở lại?
metric cũ có được cập nhật không?
consumer có biết số liệu còn provisional không?
```

Không có policy cho late data thì dashboard có thể thay số âm thầm sau nhiều ngày, làm người dùng mất niềm tin.

## 11. Grain là đơn vị ý nghĩa của một bảng

**Độ hạt (grain / 데이터 단위)** trả lời: mỗi row đại diện cho cái gì?

Ví dụ:

```text
1 row / order
1 row / order item
1 row / payment attempt
1 row / customer-day
```

Join hai bảng khác grain có thể nhân row mà query vẫn chạy hợp lệ.

Một metric đáng tin phải ghi rõ grain trước khi aggregate. “SUM(revenue)” không có nghĩa nếu chưa biết mỗi row có thể chứa revenue lặp theo item, payment attempt hoặc snapshot hay không.

## 12. Join cardinality là nguồn lỗi số liệu phổ biến

Join one-to-many hoặc many-to-many có thể làm duplicate measure.

Ví dụ:

```text
orders 1 --- N items
orders 1 --- N payment_attempts
```

Join cả ba rồi sum order revenue có thể nhân doanh thu theo số combination item × payment attempt.

Giải pháp không phải thêm `DISTINCT` theo phản xạ. Cần quay lại grain và business invariant, rồi aggregate/pre-join đúng cấp.

## 13. Deduplication cần khóa logic, không chỉ khóa kỹ thuật

Một record duplicate về byte chưa chắc là duplicate nghiệp vụ; hai record khác byte vẫn có thể đại diện cùng operation.

Cần xác định **khóa lũy đẳng (idempotency key / 멱등성 키)** hoặc logical business key dựa trên semantics.

Ví dụ payment retry có thể tạo nhiều attempt hợp lệ nhưng chỉ một successful settlement được tính revenue. Deduplication phải biết đang dedupe event, attempt hay business outcome.

## 14. Backfill là chạy lại lịch sử dưới code hiện tại

**Nạp bù lịch sử (backfill / 백필)** thường xảy ra khi sửa bug, đổi logic hoặc thêm dữ liệu cũ.

Backfill nguy hiểm vì có thể:

- chạy song song với data mới;
- dùng code/schema khác thời điểm lịch sử;
- tạo duplicate nếu sink không idempotent;
- sửa metric quá khứ mà downstream không biết;
- overload source/warehouse.

Một backfill tốt cần range, code revision, input snapshot, output target, idempotency strategy và validation/reconciliation.

## 15. Schema evolution là contract giữa producer và consumer

Thêm cột thường dễ hơn đổi meaning của cột cũ.

Một schema change an toàn cần hỏi:

```text
consumer cũ có đọc được không?
new field default thế nào?
rename có gây silent null không?
type change có làm mất precision không?
event version có cần song song không?
```

Đây là lý do expand/contract pattern xuất hiện cả trong database migration lẫn event/data contract.

## 16. Warehouse table chưa phải semantic truth

Warehouse có thể chứa dữ liệu “đúng” ở mức kỹ thuật nhưng người dùng vẫn hiểu metric khác nhau.

Ví dụ “doanh thu” có thể là:

- gross order value;
- paid amount;
- recognized revenue;
- net after refund;
- value theo order date hoặc settlement date.

Do đó cần **lớp ngữ nghĩa (semantic layer / 시맨틱 계층)** định nghĩa metric, dimension, filter và time semantics dùng chung.

Semantic layer không thay database correctness; nó chuẩn hóa cách business meaning được tiêu thụ.

## 17. Metric cần owner và definition version

Một metric quan trọng nên truy được:

```text
tên và meaning
→ công thức
→ grain
→ event-time rule
→ inclusion/exclusion policy
→ source tables
→ owner
→ version/change history
```

Nếu “active user” đổi từ 30 ngày sang 28 ngày nhưng dashboard không version/announce definition, trend bị semantic break dù pipeline vẫn chạy đúng.

## 18. Reconciliation nối operational truth với analytical truth

**Đối soát (reconciliation / 대조)** hỏi liệu hai lớp đại diện cùng business fact có khớp theo tolerance hợp lý không.

Ví dụ:

```text
số payment settlement ở source
so với
số successful-payment fact ở warehouse
```

Không phải lúc nào hai số phải giống tuyệt đối tại mọi thời điểm vì lag/late data tồn tại. Nhưng cần biết expected difference và thời gian hội tụ.

Reconciliation tốt giúp phân biệt:

- source bug;
- capture loss;
- duplicate;
- transform bug;
- timing lag;
- semantic-definition mismatch.

## 19. Dashboard freshness phải là một contract

Người dùng cần biết số liệu cập nhật tới đâu.

Một dashboard nên có thể trả lời:

```text
source data complete tới thời điểm nào?
pipeline cuối thành công khi nào?
metric đang provisional hay final?
late data còn có thể thay đổi range nào?
```

Nếu freshness không rõ, người dùng dễ so một dashboard realtime với báo cáo batch rồi cho rằng một bên “sai”.

## 20. Cache ở lớp BI có thể tạo một lớp trễ riêng

Ngay cả khi warehouse đã cập nhật, semantic engine hoặc BI cache có thể còn số cũ.

Do đó failure path có thể là:

```text
source đúng
CDC đúng
warehouse đúng
semantic layer đúng
BI cache cũ
```

Điều này nhắc rằng “data pipeline” không dừng ở table cuối; serving layer cũng thuộc đường evidence.

## 21. ML feature cũng là một consumer của semantic data

Feature cho machine learning có thể lấy từ cùng pipeline với dashboard nhưng yêu cầu point-in-time correctness nghiêm hơn.

Nếu feature training sử dụng thông tin xuất hiện sau prediction time, leakage xảy ra dù SQL và warehouse đều đúng.

Do đó analytical serving và feature serving cần cùng provenance/time semantics nhưng có thêm requirement về **đúng thời điểm (point-in-time correctness / 시점 정확성)**.

## 22. “Một nguồn chuẩn” không có nghĩa mọi câu hỏi chỉ đọc một hệ thống

Operational database có thể là source of record cho transaction; warehouse là source chuẩn cho historical analytics; semantic layer là source chuẩn cho metric definition.

Cần tách:

```text
source of record
source of analytical history
source of metric definition
```

Cố ép một hệ thống làm tất cả vai trò thường tạo coupling và hiểu nhầm.

## 23. Case: API đã paid nhưng dashboard chưa có

Đi theo evidence thay vì đoán:

```text
1. operation/idempotency key là gì?
2. transaction đã commit chưa?
3. source row có đúng business state không?
4. WAL/CDC offset đã đi qua chưa?
5. event có duplicate/missing không?
6. raw landing có record không?
7. transform có filter/drop không?
8. warehouse fact đã xuất hiện chưa?
9. semantic metric có include đúng không?
10. dashboard cache/freshness thế nào?
```

Mỗi bước thu hẹp failure domain. Không nên “chạy lại toàn pipeline” trước khi biết boundary nào hỏng.

## 24. Case: doanh thu tăng gấp đôi sau một schema change

Đầu tiên kiểm grain và join cardinality, không mặc định business tăng thật.

Có thể schema mới thêm payment attempt và transform join với order ở one-to-many rồi sum order amount nhiều lần.

Root cause lúc này là semantic/grain bug, không phải database corruption.

## 25. Case: backfill sửa lịch sử nhưng dashboard hiện hai bộ số

Nếu backfill ghi table mới nhưng semantic layer hoặc cache vẫn trỏ table cũ, hai số có thể cùng “đúng” theo hai version khác nhau.

Cần version/owner/promotion boundary rõ:

```text
backfill output
→ validation
→ reconciliation
→ semantic promotion
→ cache invalidation
→ communication
```

## 26. Mô hình tổng hợp

```text
business invariant
→ transaction correctness
→ durable commit
→ change capture
→ provenance/raw
→ transform với grain/time rõ
→ warehouse/lakehouse state
→ semantic definition
→ serving/cache
→ reconciliation/freshness evidence
```

Điểm quan trọng là **meaning phải sống sót qua mọi boundary**, không chỉ dữ liệu byte-level.

## 27. Bàn giao

Nếu cần hiểu sâu isolation, MVCC, WAL và recovery, đọc [Computer Science — Data & Databases](../05_data_databases/README.md). Nếu cần application transaction/idempotency, đọc [Backend Core](../../10_backend/backend_core/README.md). Nếu cần orchestration, backfill, warehouse/lakehouse hoặc semantic metric sâu hơn, bàn giao sang [Data Engineering](../../data_engineering/README.md). Nếu cần theo một failure xuyên request → database → queue → recovery, đọc [production case](../../devops_platform_engineering/10_production_practice/01_request_storage_queue_failure_and_recovery_case.md).

> **Bàn giao:** Sau chapter này, khi hai hệ thống trả hai con số khác nhau, đừng hỏi ngay “bên nào sai?”. Hãy truy **business invariant → commit → capture → transform → grain/time semantics → metric definition → serving freshness** để tìm chính xác nơi meaning bị thay đổi.