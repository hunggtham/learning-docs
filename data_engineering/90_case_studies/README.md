# 90 — Case studies: reasoning end-to-end

Case study là nơi kiểm tra mental model bằng failure thật, không phải nơi liệt kê sản phẩm.

## Case 1 — CDC duplicate sau retry

**Tình huống:** connector đọc transaction log, sink đã ghi event nhưng acknowledgement bị mất; connector đọc lại cùng event.

**Invariant:** mỗi immutable `event_id` đóng góp đúng một lần vào fact doanh thu.

**Thiết kế:** landing append-only giữ raw event; modeled layer `MERGE` theo event identity và kiểm tra payload conflict; serving aggregate chạy từ modeled state. Offset chỉ là source position, không phải business correctness.

**Evidence:** duplicate count, conflict count, source-to-sink reconciliation và replay test trên một khoảng offset.

## Case 2 — Late event làm thay đổi window

**Tình huống:** thiết bị offline gửi event 09:05 lúc 11:00; dashboard 09:00–10:00 đã finalize theo watermark.

**Invariant:** metric provisional/final phải được phân biệt; correction không tạo duplicate.

**Thiết kế:** lưu event time và ingestion time; late event đi vào correction path hoặc tạo version mới của aggregate; downstream biết policy finalization. State retention đủ dài để replay trong late-arrival bound.

**Evidence:** watermark lag distribution, late-event rate, correction reconciliation và số metric đã publish lại.

## Case 3 — Backfill logic mới không được ghi đè dữ liệu hiện tại

**Tình huống:** sửa timezone bug cho 12 tháng lịch sử trong khi partition hôm nay vẫn được streaming job ghi.

**Invariant:** writer lịch sử và writer hiện tại không làm mất update của nhau; output chỉ public khi reconciliation đạt.

**Thiết kế:** chạy backfill theo snapshot/version namespace, ghi target partitions riêng, so sánh row count/metric, rồi publish atomic pointer hoặc partition commit. Side effect ngoài data layer bị tắt hoặc deduplicate.

**Evidence:** input/code version, target range, diff metrics, rollback marker và consumer cutover time.

## Case 4 — Small files và compaction race

**Tình huống:** micro-batch tạo hàng triệu file nhỏ; compaction chạy đồng thời với reader và writer.

**Invariant:** reader thấy một snapshot hợp lệ; file chưa commit không được đọc; file cũ chỉ xóa sau retention.

**Thiết kế:** metadata commit xác định snapshot, compaction tạo files mới trước, publish pointer sau validation, garbage collection tách khỏi commit. Query/compaction có capacity budget riêng.

**Evidence:** snapshot lineage, file count/size distribution, reader error rate, compaction write amplification và restore test.

## Case 5 — Semantic metric fan-out

**Tình huống:** dashboard doanh thu join order, item và payment attempt ở grain khác nhau.

**Invariant:** metric amount được tính đúng grain và có definition version.

**Thiết kế:** aggregate mỗi fact về grain metric trước khi join; metric contract nêu refund, currency, event time và null policy; semantic layer không cho phép join path mơ hồ.

**Evidence:** reconciliation với ledger, cardinality check, golden queries và metric version diff.

## Cách viết case study mới

Mỗi case phải có `context → invariant → failure boundary → design → evidence → trade-off`. Không biến case study thành tutorial API; mục tiêu là chứng minh reasoning có thể chuyển giữa các tool và platform.
