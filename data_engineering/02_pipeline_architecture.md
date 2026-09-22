# 02 — Kiến trúc pipeline và processing semantics

## 1. Pipeline là chuỗi state transition

Sơ đồ `source → queue → processor → warehouse` che giấu phần khó nhất: ở mỗi mũi tên, hệ thống phải quyết định khi nào một piece of data được coi là đã xử lý thành công.

Nếu source đã phát event nhưng consumer chưa ghi được sink, event phải còn khả năng replay. Nếu sink đã ghi thành công nhưng acknowledgement bị mất, retry không được làm sai kết quả. Vì vậy kiến trúc pipeline nên được đọc như chuỗi state transition có failure boundary, không phải chuỗi logo sản phẩm.

## 2. ETL và ELT

ETL (Extract, Transform, Load) biến đổi dữ liệu trước khi nạp vào analytical store. ELT (Extract, Load, Transform) đưa raw hoặc near-raw data vào platform trước rồi transformation chạy bên trong analytical engine.

ELT trở nên phổ biến khi warehouse/lakehouse có compute mạnh và storage rẻ, nhưng đây không phải quy tắc rằng ELT luôn tốt hơn. Dữ liệu nhạy cảm có thể cần masking trước khi landing. Payload rất lớn có thể cần normalize/filter trước để tránh chi phí vận chuyển. Ngược lại, transform quá sớm có thể làm mất raw evidence cần cho replay hoặc audit.

Trade-off thật sự nằm ở nơi đặt transformation boundary, khả năng replay và governance chứ không nằm ở ba chữ viết tắt.

## 3. Full load và incremental load

Full load đọc lại toàn bộ dataset. Nó đơn giản về reasoning nhưng trở nên đắt khi dữ liệu lớn. Incremental load chỉ xử lý phần thay đổi, giảm I/O và compute nhưng đòi hỏi xác định chính xác "cái gì đã thay đổi".

Một filter kiểu `updated_at > last_run_time` có vẻ đơn giản nhưng có nhiều assumption: clock có đáng tin không, transaction commit sau khi timestamp được tạo có bị bỏ sót không, hai record cùng timestamp xử lý ra sao, job retry sử dụng checkpoint nào, và source có update timestamp cho mọi mutation hay không.

Một incremental boundary tốt thường cần overlap window cộng deduplication, monotonically increasing cursor đáng tin cậy, hoặc CDC log thay vì chỉ dựa vào wall-clock timestamp.

## 4. CDC và transaction log

Thu thập thay đổi dữ liệu (Change Data Capture, CDC / 변경 데이터 캡처) theo transaction log thường tốt hơn polling table vì database đã có log để phục vụ durability/recovery. CDC connector có thể đọc sequence của insert/update/delete mà không scan toàn bảng liên tục.

Nhưng CDC không phải magic. Consumer cần hiểu snapshot ban đầu nối với log position nào, delete được biểu diễn thế nào, schema change ảnh hưởng decoder ra sao, transaction lớn gây lag thế nào và retention của source log có đủ dài để connector phục hồi sau downtime hay không.

Một failure production phổ biến xảy ra khi connector ngừng lâu hơn log retention. Offset vẫn tồn tại nhưng log segment cần thiết đã bị xóa; lúc này không thể chỉ restart và mong pipeline tự bắt kịp. Recovery có thể cần snapshot/resync.

## 5. At-most-once, at-least-once và exactly-once

At-most-once ưu tiên không xử lý duplicate nhưng chấp nhận mất message nếu failure xảy ra ở thời điểm xấu. At-least-once ưu tiên không mất dữ liệu bằng retry, đổi lại consumer phải chịu duplicate. Exactly-once cố gắng để effect quan sát được tương đương một lần xử lý.

Trong thực tế, at-least-once cộng idempotent sink thường là mô hình dễ reasoning và robust. Ví dụ sink `MERGE` theo immutable `event_id` có thể hấp thụ retry. Tuy nhiên nếu business event không có identity ổn định, deduplication trở thành bài toán domain chứ không thể giải chỉ bằng framework setting.

## 6. Offset không phải business correctness

Broker offset chỉ nói consumer đã tiến tới đâu trong log. Nó không tự chứng minh downstream state đúng.

Nếu consumer commit offset trước khi sink commit, crash có thể làm mất effect. Nếu commit sink trước offset, crash có thể tạo duplicate khi replay. Transactional integration hoặc idempotency là cách nối hai state transition này.

Senior note: khi review pipeline, luôn vẽ riêng `source position`, `processing state` và `sink commit`. Đừng gộp chúng thành một khái niệm "processed".

## 7. Event time và processing time

Processing time là lúc hệ thống xử lý event. Event time là lúc sự kiện thực sự xảy ra theo domain. Hai thời điểm có thể lệch đáng kể.

Ví dụ điện thoại offline ghi nhận purchase lúc 09:00 nhưng upload lúc 11:00. Dashboard theo processing time sẽ đưa giao dịch vào 11:00; business report theo event time có thể cần đưa nó về 09:00.

Streaming window theo event time vì vậy phải chấp nhận dữ liệu đến muộn (late data / 지연 데이터). Watermark là tuyên bố thực dụng rằng hệ thống tin phần lớn event trước một mốc đã đến và có thể finalize/cleanup state theo policy. Watermark không làm late event biến mất; nó quyết định cách hệ thống đánh đổi completeness, latency và state size.

## 8. Backfill và replay

Backfill chạy lại dữ liệu lịch sử để sửa logic, bổ sung field hoặc khôi phục gap. Pipeline không được thiết kế cho replay thường trở nên nguy hiểm khi backfill: nó có thể gửi lại email, overwrite snapshot mới bằng dữ liệu cũ hoặc nhân đôi fact.

Một transformation thuần túy từ immutable input sang deterministic output dễ backfill hơn. External side effect cần được tách khỏi recomputable data transformation hoặc bảo vệ bằng idempotency key.

Trước một backfill lớn phải xác định input version, code version, target partitions, write mode, expected row counts, reconciliation rule và rollback strategy. "Chạy lại job" không phải một recovery plan.

## 9. Orchestration không phải processing

Orchestrator quản lý dependency, scheduling, retry và state của workflow. Nó không nên được nhầm với compute engine.

Một DAG xanh chỉ chứng minh task process trả về success theo điều kiện của nó. DAG không chứng minh business data đúng. Vì vậy data quality gate và reconciliation phải là một phần explicit của workflow khi dataset quan trọng.

## 10. Failure-oriented design

Thiết kế pipeline nên bắt đầu bằng câu hỏi "nếu process chết ở từng dòng code thì sao?". Thử failure trước và sau read, trước và sau write, trước và sau acknowledgement. Sau đó kiểm tra restart có tạo loss, duplicate, corruption hoặc inconsistent checkpoint không.

Cách reasoning này mạnh hơn việc chỉ đọc happy-path architecture diagram, bởi production system được định nghĩa phần lớn bởi behavior khi một phần của nó thất bại.