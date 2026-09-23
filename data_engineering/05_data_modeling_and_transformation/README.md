# 05 — Data modeling và transformation

Data model là cách biến record có nguồn gốc khác nhau thành một contract mà consumer có thể hiểu. Mục tiêu không phải là tạo thật nhiều table, mà là làm cho **grain, identity, history và business meaning** không bị mơ hồ sau mỗi lần join hoặc aggregate.

## 1. Grain trước schema

Trước khi chọn column, viết một câu: “mỗi row đại diện cho ...”. Một row có thể là một `order`, một `order_item`, một `payment_attempt`, một event bất biến, hoặc một snapshot của customer tại ngày D. Nếu không xác định grain, mọi metric phía sau đều có nguy cơ bị nhân bản.

Ví dụ một order có 3 item và 2 payment attempt. Join trực tiếp ba bảng tạo 6 row; `SUM(order_amount)` sẽ sai dù SQL hợp lệ. Cách an toàn là aggregate mỗi nguồn về grain cần thiết trước khi join, hoặc dùng bảng bridge có invariant rõ ràng.

## 2. Identity và deduplication

`id` của source không luôn là identity của business event. Một retry có thể tạo cùng `event_id`, một hệ thống migrate có thể đổi key, hoặc hai nguồn cùng đại diện một customer. Model phải phân biệt:

- technical key: định danh row trong storage;
- business key: định danh thực thể theo domain;
- event identity: định danh một occurrence bất biến;
- version/effective time: thứ tự và thời gian hiệu lực của state.

Deduplication không nên dùng “row mới nhất” một cách mù quáng. Rule phải nêu rõ tie-breaker, cửa sổ nhận diện duplicate và xử lý khi hai payload cùng key nhưng khác nội dung.

## 3. Event, state và snapshot

Event trả lời “điều gì đã xảy ra”; state trả lời “hiện tại đang là gì”; snapshot trả lời “tại thời điểm T hệ thống quan sát điều gì”. Không thể thay thế chúng cho nhau:

```text
event log → state projection → periodic snapshot
```

Event log giúp replay nhưng có thể đắt để query. State projection phục vụ lookup nhanh nhưng mất history nếu không lưu version. Snapshot thuận tiện cho point-in-time reporting nhưng phải định nghĩa completeness và late correction.

## 4. Transformation deterministic

Transformation tốt nhận input version rõ ràng và tạo output có thể tái tạo. Tránh đọc clock hiện tại, random value hoặc external API không version trong phép biến đổi recomputable. Nếu cần enrichment bên ngoài, lưu lại reference/version của enrichment để backfill không tạo kết quả khác chỉ vì thời gian chạy khác.

Idempotent model thường dùng `MERGE` theo business/event key, overwrite theo partition, hoặc tạo output version mới rồi publish pointer. `INSERT` nối tiếp không đủ an toàn cho replay nếu không có uniqueness invariant.

## 5. Slowly changing history

Với dimension thay đổi theo thời gian, phải chọn semantics:

- Type 1: chỉ giữ giá trị mới nhất;
- Type 2: giữ các phiên bản với `valid_from`, `valid_to`, `is_current`;
- event-sourced: giữ mutation và dựng state khi cần.

Không có lựa chọn “đúng tuyệt đối”. Type 1 đơn giản nhưng không trả lời được câu hỏi lịch sử. Type 2 dễ query hơn event log nhưng cần xử lý late correction, overlap và cùng thời điểm hiệu lực.

## 6. Transformation boundary

Raw layer giữ evidence gần source; modeled layer chuẩn hóa grain, key và semantics; serving layer tối ưu cho consumer. Đừng làm sạch đến mức mất payload gốc trước khi xác định retention/audit requirement. Ngược lại, đừng đẩy mọi logic vào serving khiến mỗi dashboard tự định nghĩa metric khác nhau.

## 7. Checklist review model

1. Grain của mỗi input/output là gì?
2. Key nào bảo đảm uniqueness và identity?
3. Join cardinality có thể fan-out ở đâu?
4. Replay cùng input/version có tạo cùng output không?
5. Late correction và delete được biểu diễn thế nào?
6. Consumer nào phụ thuộc schema/metric này?
7. Có thể reconcile output với source hoặc upstream invariant nào?

Đọc tiếp: [06 — Distributed processing](../06_distributed_processing/README.md), [08 — Orchestration và backfill](../08_orchestration_and_backfill/README.md), [10 — Serving và semantic layer](../10_serving_semantic_layer/README.md).

## 8. Snapshot fact và temporal join

Một fact event thường có `occurred_at`, `captured_at` và `loaded_at`. Khi dựng snapshot ngày D, filter theo `occurred_at` chưa đủ: event có thể được capture sau khi snapshot đã publish. Cần chọn một trong hai semantics:

- snapshot as-of event time: phản ánh domain tại D và chấp nhận late correction;
- snapshot as-observed: phản ánh platform đã biết gì tại D và không backdate event.

Hai semantics cho hai câu hỏi khác nhau. Không đặt tên chung như `daily_sales` nếu không ghi rõ kiểu snapshot.

Temporal join giữa fact và dimension phải chọn version thỏa `valid_from <= event_time < valid_to`. Nếu dimension có hai version cùng effective time, cần tie-breaker deterministic. Join với row `is_current = true` là shortcut nguy hiểm cho lịch sử.

## 9. Null, unknown và deleted

`NULL` có thể nghĩa là unknown, not-applicable, chưa nhận được hoặc đã bị redact. Nếu gom tất cả vào một giá trị, aggregate và quality check sẽ sai. Nên dùng semantic enum/flags khi domain cần phân biệt.

Delete cũng có nhiều nghĩa: entity bị xóa thật, record bị retract, privacy deletion, hoặc source chỉ không còn trả row. Model phải biết tombstone nào là business event và tombstone nào là storage cleanup.

## 10. Transformation test matrix

Test model không chỉ dùng một happy-path fixture. Tối thiểu cần có:

```text
duplicate event
late correction
missing dimension
duplicate dimension version
empty partition
timezone boundary / DST
currency or unit conversion
```

Mỗi fixture nên kiểm tra cả expected rows và invariant tổng hợp. Một model có thể trả đúng sample row nhưng sai tổng vì fan-out hoặc filter null.
