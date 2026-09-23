# 08 — Orchestration và backfill correctness

Orchestration là quản lý dependency, schedule, retry, state và ownership của workflow. Nó không thay thế processing engine và cũng không chứng minh business data đúng.

## 1. DAG là dependency graph

Một task chỉ nên chạy khi upstream data và contract đã đạt điều kiện cần. Dependency không chỉ là “job A chạy trước job B”; có thể là partition D đã complete, schema version tương thích, quality gate pass hoặc external snapshot đã immutable.

## 2. Task semantics

Mỗi task cần định nghĩa:

- input version/partition;
- output path/table và atomic publish rule;
- retryable vs permanent error;
- idempotency key;
- side effect ngoài data write;
- reconciliation và completion evidence.

Retry an toàn chỉ có thể xảy ra khi chạy lại không phá invariant. Nếu task gửi email, gọi API hoặc cập nhật ticket, side effect phải tách ra hoặc có idempotency key.

## 3. Backfill là một loại deployment

Backfill thay đổi dữ liệu lịch sử bằng code/logic mới, nên phải được review như deployment. Trước khi chạy cần chốt:

```text
input range + source snapshot
→ code/schema version
→ target partitions/version
→ write mode
→ expected counts/reconciliation
→ publish/rollback plan
```

Không chạy backfill trực tiếp lên “latest” nếu chưa tách output namespace hoặc snapshot. Một job thành công có thể overwrite dữ liệu mới bằng kết quả cũ.

## 4. Partition completeness

Partition chỉ nên được đánh dấu complete khi có evidence: source watermark, expected file set, row count/tolerance, checksum hoặc reconciliation với source. “Task không lỗi” không đủ để publish partition.

Manifest/commit marker giúp downstream đọc tập file nhất quán thay vì nhìn thấy output đang ghi dở. Khi partition bị retry, marker cũ phải được thay thế có version hoặc transaction semantics rõ.

## 5. Catchup và schedule drift

Schedule interval không đồng nghĩa data interval. Job chạy lúc 01:00 có thể xử lý ngày D-1, hoặc xử lý source watermark tới 00:45. Nếu scheduler chậm, catchup có thể tạo hàng trăm run cạnh tranh tài nguyên.

Cần giới hạn concurrency, ưu tiên backfill so với freshness, và xác định run nào được phép ghi cùng partition. Một partition có nhiều writer mà không có commit protocol là race condition.

## 6. Recovery

Khi workflow thất bại, phân biệt task chưa bắt đầu, đang chạy, đã ghi output nhưng chưa publish, và đã publish nhưng downstream chưa acknowledge. Resume từ checkpoint khác với rerun toàn DAG.

Run metadata nên lưu input partitions, code commit, schema version, row counts, quality results và output commit. Đó là bằng chứng để quyết định retry hay rollback.

## 7. Tool-independent checklist

1. Dependency có phản ánh data readiness hay chỉ phản ánh process order?
2. Retry/backfill có idempotent không?
3. Output publish có atomic không?
4. Có thể chạy song song hai run trên cùng partition không?
5. Reconciliation nào ngăn job xanh nhưng data sai?
6. External side effect được deduplicate thế nào?

Đọc tiếp: [04 — Reliability](../04_reliability_and_production.md), [07 — Streaming](../07_streaming_systems/README.md), [90 — Case studies](../90_case_studies/README.md).

## 8. Backfill planner

Một backfill lớn nên có planner tách khỏi executor. Planner tạo manifest các input partition, output partition, code/schema version, expected row count và dependency. Executor chỉ chạy manifest immutable; không tự suy luận target range từ “now”.

```text
plan → validate conflicts → execute isolated output → reconcile → publish
```

Nếu plan thay đổi giữa chừng, tạo plan version mới thay vì sửa file đang chạy. Điều này giúp rollback và forensic analysis biết run đã dựa trên assumption nào.

## 9. Concurrency trên cùng partition

Cho phép hai run cùng ghi partition là race condition nếu không có fencing/lease/commit protocol. Scheduler cần một trong các invariant:

- một partition chỉ có một writer active;
- writer có epoch/fencing token, writer cũ bị từ chối;
- output version riêng, publish pointer tuần tự;
- merge semantics chứng minh hai write giao nhau là an toàn.

Distributed lock chỉ giải quyết mutual exclusion trong thời gian lock còn hiệu lực; nó không thay thế output reconciliation và stale-writer fencing.

## 10. Retry taxonomy

Retry theo lỗi, không theo cảm xúc:

| Lỗi | Hành động |
|---|---|
| timeout/network transient | exponential backoff + jitter |
| quota/capacity | retry có giới hạn hoặc reschedule |
| schema/contract breaking | stop, alert owner |
| malformed record | quarantine + metric |
| code bug | rollback/version fix rồi rerun |
| sink partial commit | inspect marker trước khi retry |

Retry vô hạn biến lỗi deterministic thành incident lớn hơn và che khuất data loss.
